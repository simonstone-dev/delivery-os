# Contributing / 贡献指南

Explain the real failure or recurring cost your change addresses. Include an anonymized reproducer, expected outcome and applicable limits. Keep changes focused; avoid adding mandatory steps for one unusual incident.

说明改动解决的实际问题或重复成本，提供脱敏复现、预期结果和适用边界。改动保持聚焦，不因单次特殊情况增加所有项目的必经步骤。

Run `python -m unittest discover -s tests -v` and `python scripts/verify_release.py`. New behavior needs meaningful tests. Update both languages, templates, fixtures and command documentation when the contract changes.

运行测试与发布检查。新行为需要有意义的验证；约定改变时同步中英文件、模板、案例和命令说明。

Do not submit client files, confidential prompts, account details, raw meeting records or production keys. Synthetic examples are welcome. Public-method contributions use the repository's MIT license; third-party assets retain their own license.

不提交客户原件、保密提示词、账户资料、原始会议记录或生产密钥。欢迎合成案例；通用方法贡献采用MIT，第三方资产保留自身许可。
