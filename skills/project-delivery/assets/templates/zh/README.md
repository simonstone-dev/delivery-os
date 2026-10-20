# 项目首页

先读 PROJECT_STATE.json 和 registers.json，确认当前有效版本、真实状态、缺口和下一步。

- [项目理解](01-understanding.md)
- [业务与需求](02-requirements.md)
- [技术方案](03-architecture.md)
- [实施与商务](04-estimation.md)
- [验证与移交](05-validation-handoff.md)
- [问题与变更](06-decisions-changes.md)
- [复盘](07-retrospective.md)

原始资料放 inbox/，同名更新另存版本。每轮更新本页与状态，旧过程移入历史。

打开本项目后要求AI读取 AGENTS.md 和随项目携带的技能。可运行：

```bash
python .agents/skills/project-delivery/scripts/project.py index .
python .agents/skills/project-delivery/scripts/project.py check . --strict --verify-files
python .agents/skills/project-delivery/scripts/project.py report .
```

登记不是阅读，结构通过不是业务验收。
