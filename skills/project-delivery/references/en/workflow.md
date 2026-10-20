# From first files to handoff

Method version 0.2.0. This is a tailored working method, not a certification standard. Stages organize decisions and evidence; they do not require repeated approval for ordinary reversible work.

## Lifecycle

| Stage | Work | Observable outcome |
|---|---|---|
| 0 Intake and opportunity | Inventory files; identify business goal, owner, users, deadline and submission requirements | Source inventory, submission checklist and provisional scope; explain what is being considered and for whom; stopping is an available decision |
| 1 Understanding | Walk through real operations, data, rules, pain and value baseline | One-page explanation, current/target journeys and glossary; include normal, exception and correction paths |
| 2 Requirements and acceptance | Separate documented requirements, proposals, assumptions and conflicts; define functional and operational constraints | Source-to-deliverable-to-acceptance links, this/later-phase scope, decision authorities and measurable criteria |
| 3 Investigation and feasibility | Compare build, buy and reuse; eliminate hard-constraint violations; test high-impact assumptions | Recommendation and fallback, architecture, experiment evidence and explicit unresolved conditions |
| 4 Delivery and commercial baseline | Estimate work packages; reconcile roles, dependencies, calendar, external costs, support and terms | Explainable effort and cost scenarios, actual resource plan, assumptions, responsibilities and milestone plan |
| 5 Iterative build and integration | Deliver small end-to-end business slices; review, test and demonstrate | Real input-to-output behavior including necessary permissions, exception paths and records; controlled scope changes |
| 6 Business verification and go-live preparation | Replay, held-out samples, pilot/shadow operation, migration rehearsal and recovery checks as appropriate | Acceptance evidence, resolved or assigned defects, cutover and rollback plan, responsible approvals |
| 7 Launch, handoff and closeout | Controlled cutover; observe; transfer code, configuration, manuals, training and support | Agreed release and handoff records; acceptance, remaining obligations and payment status tracked separately |
| 8 Operation, learning and exit | Compare actual labor, rework, cost and realized value; plan maintenance or exit | Estimation variance and AI net savings with evidence; data export, retention and access closure as agreed |

Pre-sales can deliver a bounded initial proposal before all production tests exist. Mark assumptions and the validation plan. High uncertainty may justify a separate paid discovery or pilot. Customer deadlines do not justify inventing proof; missing noncritical material does not justify indefinite waiting.

## Sources and authority

Preserve originals and versions. OCR, extracted text, screenshots and summaries are derivatives that point back to originals. Record source ID, path or URL, checksum when applicable, origin group, authority, actual coverage and location: page, sheet, cell or timestamp.

Inventory everything before reading in focused batches. Report unread, partial, missing or unreadable material. Multiple summaries of one meeting share an origin and do not become independent corroboration. An AI summary is not a verbatim transcript. A written requirement establishes what was written, not whether an API works, a budget is authorized or a target has been achieved.

Label claims as documented, confirmed, inferred, assumed or conflicting. Confirmation needs a responsible person, date and scope. Resolve conflicts using originals and valid later decisions; file dates alone do not establish authority. Never fabricate missing source metadata.

## Business understanding

Use a representative transaction: initiator → inputs → judgment/calculation → action → output → review → execution → correction. Explain dependencies across journeys and distinguish physical/business order from development priority.

Ask for a complete connected business packet before collecting disconnected examples: original inputs, intermediate work, approved result, applicable rules and subsequent corrections. Keep formulas, hidden sheets, macros and reference IDs in electronic originals. Anonymization must preserve relationships. A demonstration by the operator can replace a specially authored technical flowchart.

Check identifiers, units, states, effective dates, formulas, versions and exceptions. Historical outputs and spreadsheet formulas can be wrong; do not silently make them the algorithm.

## Requirements and submission

Track mandatory, optional and later submission items separately. Include team evidence, site work, support, formats and exit requirements when relevant. A presentation or prototype does not substitute for every required submission item.

Acceptance specifies dataset/version, scale, environment, measurement start/end, denominator, threshold, exception and infeasible-case handling, reviewer and approval authority. Clarify vague promises such as zero errors, optimal, all sources and real time. Measure extraction quality, automation coverage, final business result, total human effort and cash savings separately.

## Technical judgment

Show system boundaries, data movement, module responsibilities, runtime, deployment, failure recovery, permissions, audit and maintenance ownership. Use an architecture checklist to catch omissions without filling every section mechanically. Add complexity only for a concrete need.

Separate AI-assisted delivery from AI embedded in the product. Evaluate the latter by quality, latency, cost, privacy and fallback. Exact calculations often belong to deterministic code or solvers; models can assist recognition, interpretation and explanation. Customer-specific constraints remain customer-specific.

For dependencies, examine version compatibility, rights for code/model/weights/data, additional terms, authorization, limits, costs, maintenance and service commitments. A public webpage is not automatically a supported commercial API. Mark documentation research, local tests and target-environment evidence separately.

## Experiments and stopping

Test uncertainties whose failure could change the architecture or go/no-go decision. Record question, criteria, fixed inputs, versions, environment, steps, raw outputs, labor/resources, observations, limits and next decision. Check relevance before reusing historical evidence.

Compare candidates with consistent business scope and inputs where possible. Changed duration, framing, hardware or input creates a variant with its own results. Joint changes can be compared as a bundle but cannot be attributed to a single parameter. Retry only after a repair or a reason to expect new information.

## Control and handoff

Name responsibility for business rules, engineering, security, acceptance and support. A list of roles does not prove people are available. Shared environments and expensive resources may need a single scheduler and idempotent job records; the exact concurrency limit depends on the project and authorization.

Maintain one current project state. Move historical decisions to history without deleting evidence. Change records identify source and authority, affected requirements/design/tasks/tests, effort, schedule and commercial impact, decision, owner and effective baseline. Routine internal corrections can proceed within existing authorization; external commitments follow actual authority.

Record four distinct states: implementation, technical validation, business acceptance and production approval. Generated files, playable media and successful HTTP responses prove only the relevant technical facts. A subjective-quality requirement needs appropriate observation and review.

At milestones, capture estimates versus actuals, scope changes, waiting, rework, dependency costs and failed acceptance. Share only anonymized, evidenced lessons. A new rule should change a concrete decision and be checked against the next project, not accumulate as permanent ceremony after every incident.
