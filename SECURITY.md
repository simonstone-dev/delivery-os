# Security / 安全说明

The CLI runs locally with Python's standard library. It does not upload files, call models, execute source content or retrieve credentials. Your chosen agent and integrations have their own data-access behavior.

命令行使用Python标准库在本地运行，不上传资料、调用模型、执行资料内容或获取凭据。所选AI助手和连接器有各自的数据访问行为。

Keep originals, credentials and client records outside the public method repository. Generated projects ignore inbox/ and local working files, but Git ignore rules are not access control or backup. Review staged content before publishing.

客户原件、凭据与项目台账不进入公开方法库。忽略规则不是权限控制或备份，公开前检查实际暂存内容。

For sensitive findings, use GitHub private vulnerability reporting when available. Otherwise ask the maintainer for a private reporting channel without posting secrets in an issue. Do not include actual customer data in a reproduction.

敏感问题优先使用GitHub私密漏洞报告；若不可用，先向维护者询问私密渠道，不在Issue发布敏感内容。复现不得含真实客户数据。
