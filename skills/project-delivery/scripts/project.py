"""DeliveryOS: offline project records and checks. Python 3.10+, standard library."""
from __future__ import annotations

import argparse
from collections import deque
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile

SKILL = Path(__file__).resolve().parents[1]
VERSION = (SKILL / "VERSION").read_text(encoding="utf-8").strip()
COLLECTIONS = ("sources", "requirements", "acceptance", "tasks", "evidence", "questions", "risks", "decisions", "changes")
NOTICE = {"en": "Record checks do not prove technical feasibility, business acceptance or production approval.",
          "zh": "台账检查不能证明技术可行、业务验收或生产上线已获批准。"}


def now():
    return datetime.now(timezone.utc).isoformat()


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def save_json(path, value):
    path = Path(path)
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, prefix=".delivery-", suffix=".tmp", delete=False) as stream:
        temporary = Path(stream.name)
        json.dump(value, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write("\n")
    try:
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def amount(value):
    if value is None or isinstance(value, (bool, dict, list)):
        raise ValueError("Expected a finite nonnegative number / 需要有限非负数")
    try:
        result = Decimal(str(value))
    except InvalidOperation as exc:
        raise ValueError("Invalid number / 无效数字") from exc
    if not result.is_finite() or result < 0:
        raise ValueError("Expected a finite nonnegative number / 需要有限非负数")
    return result


def digest(path):
    hasher = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            hasher.update(block)
    return hasher.hexdigest()


def initialize(destination, name, lang="en"):
    if lang not in {"en", "zh"}:
        raise ValueError("Unsupported language / 不支持的语言")
    original = Path(destination).absolute()
    destination = original.resolve()
    if original.is_symlink() or destination.exists():
        raise ValueError("Destination exists; nothing overwritten / 目标已存在，未覆盖文件")
    if destination == SKILL or SKILL in destination.parents:
        raise ValueError("Destination cannot be inside the skill / 不能在技能目录内初始化")
    shutil.copytree(SKILL / "assets" / "templates" / lang, destination)
    shutil.copytree(SKILL, destination / ".agents/skills/project-delivery",
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    (destination / "inbox").mkdir()
    state = {"project_name": name, "method_version": VERSION, "language": lang,
             "updated_at": now(), "phase": "intake", "implementation_status": "not_started",
             "technical_validation": "not_tested", "business_acceptance": "pending",
             "go_live_status": "not_ready", "current_baseline": None,
             "next_action": "Inventory and read sources; identify this submission's requirements." if lang == "en" else "登记并阅读资料，核对本次提交要求。"}
    save_json(destination / "PROJECT_STATE.json", state)
    save_json(destination / "registers.json", {"schema_version": 1, "currency": "CNY", "hours_per_person_day": 8,
                                              "cost_rates": {}, **{key: [] for key in COLLECTIONS}})
    return {"created": str(destination), "method_version": VERSION, "language": lang}


def index_sources(root):
    root = Path(root).resolve()
    register = root / "registers.json"
    data = read_json(register)
    if not isinstance(data, dict) or not isinstance(data.get("sources"), list):
        raise ValueError("Invalid source register / 资料台账结构无效")
    raw = root / "inbox"
    if raw.is_symlink() or not raw.is_dir():
        raise ValueError("Missing or linked inbox / 资料目录缺失或为链接")
    by_path, by_hash, used = {}, {}, set()
    for source in data["sources"]:
        if not isinstance(source, dict) or not isinstance(source.get("id"), str):
            raise ValueError("Invalid source item / 来源条目无效")
        used.add(source["id"])
        for path in [source.get("path"), *source.get("aliases", [])]:
            if path:
                by_path[path] = source
        if source.get("sha256"):
            by_hash[source["sha256"]] = source
    added = aliases = 0
    for path in sorted(raw.rglob("*")):
        if path.is_symlink():
            raise ValueError("Linked sources are not indexed / 不登记链接资料")
        if not path.is_file():
            continue
        if raw.resolve() not in path.resolve().parents:
            raise ValueError("Source escapes inbox / 来源路径超出资料目录")
        relative, checksum = path.relative_to(root).as_posix(), digest(path)
        previous = by_path.get(relative)
        if previous:
            if previous.get("sha256") != checksum:
                raise ValueError(f"Source changed in place; save a new version / 请另存新版本: {relative}")
            continue
        if checksum in by_hash:
            source = by_hash[checksum]
            source.setdefault("aliases", []).append(relative)
            by_path[relative] = source
            aliases += 1
            continue
        sequence = 1
        while f"S{sequence:04d}" in used:
            sequence += 1
        source = {"id": f"S{sequence:04d}", "title": path.name, "path": relative, "aliases": [],
                  "sha256": checksum, "registered_at": now(), "read_status": "unread",
                  "origin_group": None, "authority": "unknown", "coverage": None}
        used.add(source["id"])
        data["sources"].append(source)
        by_path[relative], by_hash[checksum] = source, source
        added += 1
    save_json(register, data)
    return {"new_sources": added, "duplicate_aliases": aliases, "total_sources": len(data["sources"]),
            "notice": "Indexed, not read / 已登记，不代表已读"}


def validate(data, root=None, gate="plan", state=None):
    errors, warnings, maps = [], [], {}

    def add(target, code, en, zh, item=None):
        target.append({"code": code, "item": item, "message": en, "message_zh": zh})

    if not isinstance(data, dict):
        add(errors, "INVALID_ROOT", "Register must be an object", "台账必须为对象")
        return errors, warnings
    if data.get("schema_version") != 1 or isinstance(data.get("schema_version"), bool):
        add(errors, "SCHEMA_VERSION", "Unsupported schema version", "不支持的台账版本")
    for key in COLLECTIONS:
        maps[key] = {}
        items = data.get(key)
        if not isinstance(items, list):
            add(errors, "INVALID_COLLECTION", f"{key} must be a list", f"{key} 必须为列表")
            continue
        for item in items:
            if not isinstance(item, dict) or not isinstance(item.get("id"), str) or not item["id"].strip():
                add(errors, "INVALID_ID", f"Invalid ID in {key}", f"{key} 中条目编号无效")
                continue
            if item["id"] in maps[key]:
                add(errors, "DUPLICATE_ID", "Duplicate ID", "编号重复", item["id"])
            maps[key][item["id"]] = item

    def refs(item, field, collection, required=False):
        values = item.get(field, [])
        if not isinstance(values, list) or any(not isinstance(v, str) for v in values):
            add(errors, "INVALID_REFERENCE_LIST", f"{field} must be a list of IDs", f"{field} 必须为编号列表", item["id"])
            return []
        for value in values:
            if value not in maps[collection]:
                add(errors, "DANGLING_REFERENCE", f"Missing {collection}: {value}", f"引用不存在: {collection}/{value}", item["id"])
        if required and not values:
            add(warnings, "MISSING_REFERENCE", f"Missing {field}", f"缺少 {field}", item["id"])
        return values

    for key in ("sources", "requirements", "acceptance", "tasks"):
        if not maps[key]:
            add(errors if gate == "handover" else warnings, "EMPTY_COLLECTION", f"No {key} recorded", f"尚无 {key} 记录")
    for source in maps["sources"].values():
        status = source.get("read_status")
        if status not in ("unread", "partial", "read", "unreadable"):
            add(errors, "READ_STATUS", "Invalid reading status", "阅读状态无效", source["id"])
        elif status != "read":
            add(warnings, "SOURCE_NOT_READ", "Source not fully read", "来源尚未完整阅读", source["id"])
        for field in ("coverage", "origin_group", "authority"):
            if not source.get(field) or source.get(field) == "unknown":
                add(warnings, "SOURCE_CONTEXT", f"Missing source {field}", f"来源缺少 {field}", source["id"])
        if root and source.get("path"):
            path = (Path(root) / source["path"]).resolve()
            if Path(root).resolve() not in path.parents or not path.is_file():
                add(errors, "SOURCE_PATH", "Source missing or outside project", "来源缺失或超出项目目录", source["id"])
            elif not source.get("sha256") or digest(path) != source["sha256"]:
                add(errors, "SOURCE_HASH", "Source checksum changed or absent", "来源校验值缺失或内容改变", source["id"])
    for requirement in maps["requirements"].values():
        refs(requirement, "source_ids", "sources", True)
        refs(requirement, "acceptance_ids", "acceptance", True)
        if requirement.get("claim_type") not in ("documented", "confirmed", "inferred", "assumed", "conflicting"):
            add(errors, "CLAIM_TYPE", "Invalid claim type", "结论性质无效", requirement["id"])
        for field in ("title", "deliverable", "source_locator"):
            if not requirement.get(field):
                add(warnings, "REQUIREMENT_DETAIL", f"Missing {field}", f"缺少 {field}", requirement["id"])
        if requirement.get("claim_type") == "confirmed" and any(not requirement.get(f) for f in ("confirmed_by", "confirmed_at", "confirmation_scope")):
            add(errors, "CONFIRMATION_MISSING", "Confirmed claim lacks authority, time or scope", "已确认结论缺确认人、时间或范围", requirement["id"])
        if requirement.get("claim_type") == "conflicting" and not requirement.get("question_ids"):
            add(warnings, "CONFLICT_UNTRACKED", "Conflict needs a tracked question", "冲突需要关联澄清事项", requirement["id"])
        refs(requirement, "question_ids", "questions")
    for acceptance in maps["acceptance"].values():
        refs(acceptance, "requirement_ids", "requirements", True)
        evidence_ids = refs(acceptance, "evidence_ids", "evidence")
        for field in ("criterion", "dataset", "method", "threshold", "environment"):
            if not acceptance.get(field):
                add(warnings, "ACCEPTANCE_DETAIL", f"Missing {field}", f"验收缺少 {field}", acceptance["id"])
        status = acceptance.get("status")
        if status not in ("pending", "passed", "failed", "conditional"):
            add(errors, "ACCEPTANCE_STATUS", "Invalid acceptance status", "验收状态无效", acceptance["id"])
        if status == "passed" and (not evidence_ids or not acceptance.get("approver") or not acceptance.get("approved_at")):
            add(errors, "UNSUBSTANTIATED_PASS", "Pass lacks evidence or approval metadata", "验收通过缺证据或签认记录", acceptance["id"])
        if gate == "handover" and status != "passed":
            add(errors, "ACCEPTANCE_PENDING", "Acceptance has not passed", "业务验收尚未通过", acceptance["id"])
    covered, dependencies = set(), {}
    for task in maps["tasks"].values():
        covered.update(refs(task, "requirement_ids", "requirements", True))
        dependencies[task["id"]] = {v for v in refs(task, "depends_on", "tasks") if v in maps["tasks"]}
        try:
            values = [amount(task["days"][key]) for key in ("optimistic", "likely", "pessimistic")]
            if not values[0] <= values[1] <= values[2]:
                raise ValueError("Unordered effort interval")
        except (ValueError, KeyError, TypeError):
            add(errors, "INVALID_EFFORT", "Effort must be finite, nonnegative and ordered", "人天必须有限、非负且按乐观到保守排列", task["id"])
        for field in ("role", "deliverable", "basis", "done_when"):
            if not isinstance(task.get(field), str) or not task[field].strip():
                add(errors if field == "role" else warnings, "TASK_DETAIL", f"Missing text field {field}", f"任务缺少文本字段 {field}", task["id"])
    for requirement_id in maps["requirements"]:
        if requirement_id not in covered:
            add(warnings, "UNCOVERED_REQUIREMENT", "Requirement has no work package", "需求尚无工作包", requirement_id)
    counts = {key: len(value) for key, value in dependencies.items()}
    successors = {key: set() for key in dependencies}
    for task_id, parents in dependencies.items():
        for parent in parents:
            successors[parent].add(task_id)
    queue = deque(key for key, count in counts.items() if count == 0)
    visited = 0
    while queue:
        key = queue.popleft()
        visited += 1
        for successor in successors[key]:
            counts[successor] -= 1
            if counts[successor] == 0:
                queue.append(successor)
    if visited != len(dependencies):
        add(errors, "DEPENDENCY_CYCLE", "Work-package dependency cycle", "工作包依赖存在环")
    for evidence in maps["evidence"].values():
        refs(evidence, "source_ids", "sources", True)
        if not evidence.get("limitations"):
            add(warnings, "EVIDENCE_LIMITS", "Evidence limits not described", "证据未说明适用边界", evidence["id"])
    for question in maps["questions"].values():
        refs(question, "source_ids", "sources")
        if not question.get("owner") or not question.get("impact"):
            add(warnings, "QUESTION_DETAIL", "Question needs owner and impact", "问题缺负责人或影响", question["id"])
        if gate == "handover" and question.get("blocking") and question.get("status") != "resolved":
            add(errors, "BLOCKING_QUESTION", "Blocking question remains unresolved", "阻断事项尚未解决", question["id"])
    for decision in maps["decisions"].values():
        refs(decision, "evidence_ids", "evidence")
    try:
        if amount(data.get("hours_per_person_day")) == 0:
            raise ValueError("Zero hours")
        if not isinstance(data.get("currency"), str) or not data["currency"].strip():
            raise ValueError("Missing currency")
        if not isinstance(data.get("cost_rates"), dict):
            raise ValueError("Invalid rate map")
        for rate in data["cost_rates"].values():
            amount(rate)
    except ValueError:
        add(errors, "ESTIMATION_METADATA", "Invalid workday, currency or cost rate", "工时单位、币种或成本单价无效")
    if gate == "handover":
        state = state or {}
        for field, allowed in {"technical_validation": {"passed"}, "business_acceptance": {"passed"}, "go_live_status": {"approved", "live"}}.items():
            if state.get(field) not in allowed:
                add(errors, "HANDOVER_STATE", f"{field} is not approved", f"{field} 未满足移交条件")
    return errors, warnings


def estimate(data):
    errors, warnings = validate(data)
    if errors or not data.get("tasks"):
        raise ValueError("Fix register errors or add work packages / 请修正台账错误或补充任务")
    totals = {key: Decimal(0) for key in ("optimistic", "likely", "pessimistic")}
    missing, cost = set(), Decimal(0)
    for task in data["tasks"]:
        for key in totals:
            totals[key] += amount(task["days"][key])
        rate = data["cost_rates"].get(task["role"])
        if rate is None:
            missing.add(task["role"])
        else:
            cost += amount(task["days"]["likely"]) * amount(rate)
    return {"person_days": {key: str(value) for key, value in totals.items()}, "currency": data["currency"],
            "likely_labor_cost": None if missing else str(cost.quantize(Decimal("0.01"))),
            "missing_cost_rates": sorted(missing), "warnings": warnings,
            "notice": "Scenario totals, not a quote, schedule or probability guarantee / 情景汇总，不是报价、工期或概率保证"}


def report(root, include_cost=False):
    root = Path(root)
    state, data = read_json(root / "PROJECT_STATE.json"), read_json(root / "registers.json")
    zh = state.get("language") == "zh"
    errors, warnings = validate(data)
    if errors:
        raise ValueError("Cannot report invalid register / 台账结构错误，不能生成报告")
    def cell(value):
        return str(value if value is not None else "—").replace("|", "\\|").replace("\n", " ")
    title = "项目计划快照" if zh else "Project planning snapshot"
    lines = [f"# {title}: {cell(state['project_name'])}", "", f"DeliveryOS {state['method_version']}", "", NOTICE["zh" if zh else "en"], "",
             ("实现 / 技术 / 业务 / 上线" if zh else "Implementation / technical / business / go-live") + ": " + " / ".join(cell(state.get(k)) for k in ("implementation_status", "technical_validation", "business_acceptance", "go_live_status")), "",
             "## " + ("需求追溯" if zh else "Traceability"), "",
             "| ID | " + ("需求 | 来源 | 验收 | 工作包 | 性质 |" if zh else "Requirement | Sources | Acceptance | Work packages | Claim |"),
             "|---|---|---|---|---|---|"]
    for requirement in data["requirements"]:
        tasks = [t["id"] for t in data["tasks"] if requirement["id"] in t.get("requirement_ids", [])]
        lines.append("| " + " | ".join(cell(v) for v in (requirement["id"], requirement["title"], ", ".join(requirement.get("source_ids", [])), ", ".join(requirement.get("acceptance_ids", [])), ", ".join(tasks), requirement["claim_type"])) + " |")
    lines += ["", "## " + ("人天情景" if zh else "Effort scenarios"), ""]
    if data["tasks"]:
        totals = estimate(data)
        lines.append(" / ".join(f"{key}: {value}" for key, value in totals["person_days"].items()) + (" 人天" if zh else " person-days"))
        if include_cost:
            lines.append(f"{totals['currency']} labor cost / 人力成本: {totals['likely_labor_cost'] if totals['likely_labor_cost'] is not None else 'INCOMPLETE / 缺失'}")
    else:
        lines.append("尚无任务，不能估算。" if zh else "No work packages; no estimate.")
    lines += ["", "## " + ("待确认事项" if zh else "Open questions"), ""]
    for question in data["questions"]:
        lines.append(f"- {cell(question['id'])}: {cell(question.get('question'))} — {cell(question.get('impact'))}")
    lines += ["", "## " + ("结构检查提醒" if zh else "Record warnings"), ""]
    lines.extend(f"- {w['code']}: {w['message_zh'] if zh else w['message']}" for w in warnings)
    if not warnings:
        lines.append("无结构提醒；不代表业务验收已通过。" if zh else "No record warnings; business acceptance remains a separate decision.")
    return "\n".join(lines) + "\n"


def demo(destination, lang="en"):
    result = initialize(destination, "Synthetic expense-intake pilot" if lang == "en" else "合成报销资料处理试点", lang)
    root = Path(destination)
    case = SKILL / "assets" / "demo" / lang
    for path in sorted((case / "inbox").iterdir()):
        shutil.copy2(path, root / "inbox" / path.name)
    index_sources(root)
    data = read_json(case / "registers.json")
    indexed = read_json(root / "registers.json")["sources"]
    for source in data["sources"]:
        match = next(s for s in indexed if s["path"] == source["path"])
        source.update(sha256=match["sha256"], registered_at=match["registered_at"])
    save_json(root / "registers.json", data)
    state = read_json(root / "PROJECT_STATE.json")
    state.update(phase="discovery", next_action="Resolve Q001; validate OCR on representative samples." if lang == "en" else "澄清Q001，并用代表样本验证OCR。")
    save_json(root / "PROJECT_STATE.json", state)
    (root / "PROJECT_REPORT.md").write_text(report(root), encoding="utf-8")
    result.update(synthetic=True, report="PROJECT_REPORT.md", notice="Authored example, not an autonomous AI run / 人工编写合成案例，非自主AI实测")
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", action="version", version=VERSION)
    commands = parser.add_subparsers(dest="command", required=True)
    for command in ("init", "demo"):
        sub = commands.add_parser(command)
        sub.add_argument("--dest", required=True)
        sub.add_argument("--lang", choices=("en", "zh"), default="en")
        if command == "init":
            sub.add_argument("--name", required=True)
    for command in ("index", "check", "estimate", "report"):
        sub = commands.add_parser(command)
        sub.add_argument("project", type=Path)
        if command == "check":
            sub.add_argument("--strict", action="store_true")
            sub.add_argument("--verify-files", action="store_true")
            sub.add_argument("--gate", choices=("plan", "handover"), default="plan")
        if command == "report":
            sub.add_argument("--include-cost", action="store_true")
    args = parser.parse_args(argv)
    code = 0
    try:
        if args.command == "init":
            result = initialize(args.dest, args.name, args.lang)
        elif args.command == "demo":
            result = demo(args.dest, args.lang)
        elif args.command == "index":
            result = index_sources(args.project)
        elif args.command == "report":
            print(report(args.project, args.include_cost), end="")
            return 0
        else:
            data = read_json(args.project / "registers.json")
            if args.command == "estimate":
                result = estimate(data)
            else:
                errors, warnings = validate(data, args.project if args.verify_files else None, args.gate,
                                            read_json(args.project / "PROJECT_STATE.json"))
                code = 1 if errors else (2 if args.strict and warnings else 0)
                result = {"structure_valid": not errors, "gate": args.gate, "errors": errors, "warnings": warnings, "notice": NOTICE}
    except (OSError, ValueError, TypeError, KeyError) as exc:
        result, code = {"error": str(exc)}, 1
    print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
    return code


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
