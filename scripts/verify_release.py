"""Offline consistency and public-file checks; no third-party packages."""
import ast
import importlib.util
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/project-delivery"
SPEC = importlib.util.spec_from_file_location("delivery_release", SKILL / "scripts/project.py")
tool = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(tool)
EXCLUDED = {".git", "work", "projects", "local-only", "__pycache__", "demo-en", "demo-zh"}


def main():
    failures = []
    files = [p for p in ROOT.rglob("*") if p.is_file() and not any(part in EXCLUDED for part in p.relative_to(ROOT).parts)]
    local_links = 0
    patterns = {"machine_home_path": re.compile(r"[A-Za-z]:[\\/](?:Users|Documents and Settings)[\\/]"),
                "private_key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
                "github_token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b")}
    for path in files:
        if path.suffix.lower() in {".sqlite", ".sqlite3", ".db", ".pem", ".key", ".docx", ".pdf"}:
            failures.append(f"Unexpected public asset: {path.relative_to(ROOT)}")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeError:
            failures.append(f"Non-text asset requires explicit review: {path.relative_to(ROOT)}")
            continue
        for label, pattern in patterns.items():
            if pattern.search(text):
                failures.append(f"{label}: {path.relative_to(ROOT)}")
        if path.suffix == ".py":
            ast.parse(text, filename=str(path))
        if path.suffix == ".json":
            json.loads(text)
        if path.suffix == ".svg":
            ET.fromstring(text)
        if path.suffix == ".md":
            targets = re.findall(r"\[[^\]]*\]\(([^)]+)\)", text)
            targets += re.findall(r'(?:src|href)="([^"#]+)"', text)
            for target in targets:
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                target = target.split("#", 1)[0]
                if target:
                    local_links += 1
                    if not (path.parent / target).exists():
                        failures.append(f"Broken link: {path.relative_to(ROOT)} -> {target}")
    contract = tool.read_json(ROOT / "docs/translation-map.json")
    for lang in contract["languages"]:
        for filename in contract["reference_pairs"]:
            if not (SKILL / "references" / lang / filename).is_file():
                failures.append(f"Missing {lang} reference: {filename}")
        for filename in contract["template_files"]:
            if not (SKILL / "assets/templates" / lang / filename).is_file():
                failures.append(f"Missing {lang} template: {filename}")
        for filename in ("quickstart.md", "validation.md", "references.md"):
            if not (ROOT / "docs" / lang / filename).is_file():
                failures.append(f"Missing {lang} guide: {filename}")
        data = tool.read_json(SKILL / "assets/demo" / lang / "registers.json")
        errors, warnings = tool.validate(data)
        if errors or warnings:
            failures.append(f"Demo contract findings: {lang}")
        if tool.estimate(data)["person_days"] != {"optimistic": "7.5", "likely": "13", "pessimistic": "23"}:
            failures.append(f"Unexpected effort: {lang}")
    for filename in ("README.md", "README.zh-CN.md", "CHANGELOG.md"):
        if tool.VERSION not in (ROOT / filename).read_text(encoding="utf-8"):
            failures.append(f"Version missing in {filename}")
    readme_commands = []
    for filename in ("README.md", "README.zh-CN.md"):
        text = (ROOT / filename).read_text(encoding="utf-8")
        readme_commands.append(set(re.findall(r"python delivery\.py ([a-z]+)", text)))
    if readme_commands[0] != readme_commands[1]:
        failures.append("README command examples differ across languages")
    skill_text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    if not skill_text.startswith("---\nname: project-delivery\ndescription:"):
        failures.append("Skill frontmatter does not identify name and description")
    test_tree = ast.parse((ROOT / "tests/test_delivery.py").read_text(encoding="utf-8"))
    test_count = sum(isinstance(node, ast.FunctionDef) and node.name.startswith("test_") for node in ast.walk(test_tree))
    result = {"passed": not failures, "version": tool.VERSION, "public_files_checked": len(files),
              "local_links_checked": local_links, "declared_behavior_tests": test_count,
              "language_contracts": contract["languages"], "failures": failures,
              "scope": "Offline consistency and limited hygiene scan; not runtime/business certification"}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
