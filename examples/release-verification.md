# Release verification / 发布验证

Version 0.2.0. Local validation on 2026-10-20 used Windows and Python 3.12. The 27 behavior tests passed, including both language quickstarts, portability and rejected premature handoff. The release consistency command is independently reproducible below.

0.2.0版于2026-10-20在Windows、Python 3.12本地验证，27项行为测试通过，包含双语上手、独立移动和过早移交拦截。发布一致性检查可按下面命令复现。

```bash
python -m unittest discover -s tests -v
python scripts/verify_release.py
```

The public repository contains no private case source material or machine-specific test logs. CI is configured for a six-combination OS/Python matrix; remote results are established only by completed Actions runs, not by this local result. See the repository's Actions tab after publication.

公开仓库不含私有案例原件或本机测试日志。CI配置了六种操作系统与Python组合，远程结果只以已完成Actions为准，本地通过不等于远程矩阵已通过。发布后请查看仓库Actions。

The guided scenario is authored synthetic material. No autonomous-agent accuracy, real-project delivery success, universal effort reduction or production acceptance is claimed.

案例为人工编写的合成材料，没有宣称自主AI准确率、真实项目交付成功率、统一工时降幅或生产验收达标。
