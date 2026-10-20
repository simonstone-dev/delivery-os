# Quick start

Use Python 3.10+ (`python3` or `py` may be your local command). Clone the repository or download and extract its ZIP, then open a terminal in that folder. The CLI needs no installed packages, credentials or API access.

## Try a complete authored example

```bash
python delivery.py demo --dest demo-en --lang en
python delivery.py check demo-en --strict --verify-files
python delivery.py estimate demo-en
python delivery.py report demo-en
```

Expected: the plan record check exits 0 with no findings. Effort is optimistic 7.5, likely 13, pessimistic 23; labor cost is null because analyst, architect, engineer and QA rates are absent. Open questions and pending acceptance remain visible. Inspect the three text sources in `demo-en/inbox/` and [the guided interpretation](../../examples/scenario-review.en.md).

```bash
python delivery.py check demo-en --gate handover
```

This intentionally exits 1. The authored example is not an accepted or approved business system.

## Use real material

```bash
python delivery.py init --name "My client project" --dest projects/my-client --lang en
python delivery.py index projects/my-client
```

Copy originals into `projects/my-client/inbox/` before indexing. Preserve changed versions under new paths. Indexing collects metadata and checksums, not document meaning; sources start unread.

Open the generated project in your file-capable coding agent. Ask it to read `AGENTS.md` and `.agents/skills/project-delivery/SKILL.md`, then inventory, read and explain the material. The agent uses its own available PDF, spreadsheet, OCR or research tools. No provider or model is embedded in this repository.

Work from the one-page understanding into source-linked requirements, feasibility, work packages and acceptance. Use plain business names, examples and diagrams before technical detail. Keep unknowns explicit; ask the client only for private facts, access and decisions the team cannot resolve itself.

## Resume or move

The project contains its own guidance, both language references, templates and CLI. After moving it, run:

```bash
python .agents/skills/project-delivery/scripts/project.py check . --strict --verify-files
```

Read project state at each session. Edit canonical registers rather than manually reconciling duplicate totals. Regenerate reports with `report .`; output is written to stdout, so existing files are not silently overwritten. `--include-cost` opts into labor-cost output.

## Common outcomes

- Existing destination: choose a new directory; the initializer preserves the existing one.
- Strict exit 2: read warnings; do not mark sources read or claims confirmed just to silence them.
- Changed source: save the new version under a new path and re-index.
- Unknown cost: collect role rates or keep the estimate as person-days.
- No Python command: install Python from its official distribution, then retry.
- Formatting: choose the recipient's required style; this public project does not impose any maintainer's personal document template.

[中文](../zh/quickstart.md) · [Validation](validation.md) · [Home](../../README.md)
