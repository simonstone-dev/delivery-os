# Project home

Read PROJECT_STATE.json and registers.json first: current baseline, actual status, open gaps and next action.

- [Project understanding](01-understanding.md)
- [Business and requirements](02-requirements.md)
- [Technical approach](03-architecture.md)
- [Implementation and commercial plan](04-estimation.md)
- [Validation and handoff](05-validation-handoff.md)
- [Questions and change control](06-decisions-changes.md)
- [Retrospective](07-retrospective.md)

Put original material in inbox/; save changed files as new versions. Update this page and state each session; keep prior conclusions in history.

Ask your agent to read AGENTS.md and the bundled skill. Commands:

```bash
python .agents/skills/project-delivery/scripts/project.py index .
python .agents/skills/project-delivery/scripts/project.py check . --strict --verify-files
python .agents/skills/project-delivery/scripts/project.py report .
```

Indexing is not reading; record checks are not business acceptance.
