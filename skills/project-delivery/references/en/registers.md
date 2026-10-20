# Linked records

The agent maintains `registers.json`; people primarily read the project documents. Start with needed entries and expand them. IDs are stable within a collection. The CLI checks documented structural rules, not every field's meaning or real-world truth.

| Collection | Important fields |
|---|---|
| sources | id, title, path or URL, sha256 for files, read_status, origin_group, authority, coverage |
| requirements | id, title, source_ids, source_locator, claim_type, deliverable, acceptance_ids, question_ids |
| acceptance | id, requirement_ids, criterion, dataset, environment, method, threshold, status, evidence_ids, approver, approved_at |
| tasks | id, title, requirement_ids, deliverable, role, depends_on, days, basis, done_when |
| evidence | id, source_ids, locator, kind, test_case, version, environment, result, verification, checked_by, checked_at, limitations |
| questions | id, question, source_ids, impact, owner, status, blocking |
| risks | id, trigger, impact, owner, mitigation, reserve_basis, status |
| decisions | id, context, options, evidence_ids, decision, decided_by, decided_at, scope, supersedes |
| changes | id, source, description, affected_ids, effort_impact, schedule_impact, cost_impact, decision, effective_version, owner, status |

Reading states: `unread`, `partial`, `read`, `unreadable`. Inventory does not mark a source read. Same-origin summaries share origin_group. Coverage identifies page, sheet, cell or time range. Full reading still does not establish technical truth or client approval.

Claim types: `documented`, `confirmed`, `inferred`, `assumed`, `conflicting`. Confirmed claims need `confirmed_by`, `confirmed_at`, `confirmation_scope`. Conflicts link to questions. Do not relabel a proposal to avoid a warning.

Acceptance states: `pending`, `passed`, `failed`, `conditional`. Passed items need evidence links and approval metadata. The tool cannot authenticate approvals. Define metric semantics rather than filling placeholders solely to make checks pass.

Effort fields: days.optimistic, days.likely, days.pessimistic, finite, nonnegative and ordered. Dependencies reference tasks and must be acyclic. Support tasks should link to appropriate delivery or operational requirements rather than fabricated associations.

Metadata: schema_version is 1; hours_per_person_day is an editable workday unit; cost_rates maps roles to cost rates; currency is one nonempty currency code. The tool performs no exchange-rate conversion. Empty rates mean unknown costs. No default market rates are supplied.

`check --strict` returns exit code 2 for warnings, 1 for errors, 0 for no structural findings. `--verify-files` verifies registered primary file paths and hashes. Aliases preserve deduplication metadata; they are not independently reread or authenticated. `--gate handover` additionally checks recorded acceptance, blocking questions and production state; it cannot certify runtime behavior.

`report` renders a fresh snapshot from canonical records so totals and trace links do not rely on a separately edited summary. Open questions remain visible. Generated reports should be regenerated after register changes.

See the synthetic dataset in `assets/demo/en/registers.json`. Its effort and text are authored examples, not customer facts, actual delivery measurements or an AI-accuracy benchmark.
