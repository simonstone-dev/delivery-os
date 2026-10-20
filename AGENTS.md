# Maintain DeliveryOS / 维护约定

Read README.md and the relevant language's references before changing the method. Keep client material out of this public repository. Use synthetic examples. Preserve existing project files and current user authorization.

修改前读首页和对应语言参考；公开仓库只使用合成案例，不加入客户资料。保留项目原文件，遵守当前用户授权。

Canonical CLI: `skills/project-delivery/scripts/project.py`. Version source: `skills/project-delivery/VERSION`. Shared data contract: both demo registers and `docs/translation-map.json`. Root `delivery.py` is a launcher, not a second implementation.

命令只有一份实现，版本只有一个源，中英共用数据约定。改动时同步文档、模板与测试。

Checks / 验证:

```bash
python -m unittest discover -s tests -v
python scripts/verify_release.py
```

Test observable behavior and failure boundaries. Do not label a record check as business acceptance or an authored fixture as an autonomous AI benchmark. Upgrade copied project methods intentionally, never by overwriting live client records.

验证实际行为与失败边界；结构检查不等于业务验收，人工案例不等于自主AI效果评测。项目方法升级应审查，不覆盖客户台账。
