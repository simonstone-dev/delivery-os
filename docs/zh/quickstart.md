# 快速上手

需要Python 3.10+，本机命令也可能是 `python3` 或 `py`。克隆仓库或下载ZIP解压，在该目录打开终端。命令行无需第三方包、凭据或API。

## 体验完整合成案例

```bash
python delivery.py demo --dest demo-zh --lang zh
python delivery.py check demo-zh --strict --verify-files
python delivery.py estimate demo-zh
python delivery.py report demo-zh
```

预期：计划台账检查退出码0，无结构问题；乐观7.5、基准13、保守23人天。分析、架构、开发、测试的单价都未提供，所以金额保持null；问题和待验收状态保留。查看 `demo-zh/inbox/` 的三份文本及[案例解读](../../examples/scenario-review.zh-CN.md)。

```bash
python delivery.py check demo-zh --gate handover
```

这条命令应退出码1，表示案例尚不是通过验收和上线批准的业务系统。

## 使用真实资料

```bash
python delivery.py init --name "客户项目" --dest projects/my-client --lang zh
python delivery.py index projects/my-client
```

先把原件复制到 `projects/my-client/inbox/`。更新文件另存版本。索引只记录元数据和哈希，不理解内容，资料初始仍为未读。

用有文件访问能力的编程助手打开新项目，要求读取 `AGENTS.md` 和 `.agents/skills/project-delivery/SKILL.md`，再登记、阅读和讲解。PDF、表格、OCR和研究由助手现有工具完成，本仓库不绑定模型或服务商。

从一页项目理解逐步形成有关联的需求、可行性、工作包和验收。先用业务名称、案例和图示解释，再深入技术。未知明确保留；我方能查的先查，客户只补私有事实、权限和需其决定的事项。

## 接续和移动

项目自身携带指引、两种语言参考、模板和命令行。移动后可在该项目运行：

```bash
python .agents/skills/project-delivery/scripts/project.py check . --strict --verify-files
```

每轮先读状态，维护统一台账，避免手工对多份总数。用 `report .` 重新生成快照，默认输出到终端，不悄悄覆盖文件；加 `--include-cost` 才包含人力成本。

## 常见情况

- 目录已存在：选新目录，原目录保持不动。
- 严格模式退出码2：处理提醒，不为消除提示而虚报已读或确认。
- 来源内容改变：新版本另存路径，再登记。
- 金额未知：补角色单价，或继续只给人天。
- 找不到Python命令：从官方发行渠道安装后重试。
- 正式排版：使用接收方要求的规范，公开项目不强加维护者个人模板。

[English](../en/quickstart.md) · [验证说明](validation.md) · [首页](../../README.zh-CN.md)
