# 关联台账的最小字段

`registers.json` 由 AI 维护，用户主要看中文成果。先建立必要条目，再按项目增加字段；不要求在首轮填满所有列表。不适用项说明原因。跨列表引用使用稳定 id；本工具不实现完整数据库或自动签认。

## 来源 sources

`id/title/path/sha256/read_status/origin_group/authority/coverage/notes`。网页或聊天可用 `url/thread_id` 替代本地路径，并补获取时间。`read_status` 为 `unread/partial/read/unreadable`。同源摘要标同一 `origin_group`，`coverage` 写页码、工作表、单元格或时间段。自动索引只填文件元数据，来源权威与内容覆盖由阅读后补充。

## 需求 requirements

`id/title/source_ids/source_locator/claim_type/deliverable/acceptance_ids/status/owner`。`claim_type` 可为 `documented/confirmed/inferred/assumed/conflicting`；它们分别表示资料记载、有效确认、推断、假设和冲突。业务确认补 `confirmed_by/confirmed_at/confirmation_scope`；客户要求与我方建议分清。

## 验收 acceptance

`id/requirement_ids/criterion/dataset/environment/method/threshold/status/evidence_ids/approver/approved_at`。`status` 为 `pending/passed/failed/conditional`。附条件通过写明限制；通过至少记录证据、确认人和时间。脚本仅检查这些元数据是否存在，不能验证签字真假或证明指标达标。

## 任务 tasks

`id/title/requirement_ids/deliverable/role/depends_on/days/basis/done_when/status`。`days` 含 `optimistic/likely/pessimistic`，均为有限非负数，按顺序递增。`basis` 记录估算证据及假设。`depends_on` 引用任务，禁止成环。通用管理、治理等支撑任务可关联相应非功能需求，不能为凑覆盖虚造关联。

## 证据 evidence

`id/source_ids/locator/kind/test_case/version/environment/result/verification/checked_by/checked_at/limitations`。区分历史报告、原始响应、本轮复核、目标环境测试和签认记录；是否重验必须如实。原始结果与正式汇总保留对应关系，失败和局限不可删去。

## 问题、风险、决策和变更

`questions`：`id/question/source_ids/impact/suggested_contact/needed_material/priority/owner/status`。

`risks`：`id/trigger/impact/owner/mitigation/reserve_basis/status`。

`decisions`：`id/context/options/evidence_ids/decision/decided_by/decided_at/scope/supersedes`。

`changes`：`id/source/description/affected_ids/effort_impact/schedule_impact/cost_impact/decision/effective_version/owner/status`。

这些扩展字段由流程要求维护，当前脚本不做全部语义及跨字段检查；不能用结构通过声称变更、确认或验收完整。

## 估算元数据

`hours_per_person_day` 为人天工时约定，模板为 8，按项目修订。`cost_rates` 是角色到成本单价的映射，默认空，不自带市场价。`currency` 为单一币种；跨币种需先明确汇率来源、日期及转换方式，脚本不换汇。

演示条目见工具包 `assets/demo/zh/registers.json`，所有数字、名称和确认信息均为合成数据，不是任何客户事实。
