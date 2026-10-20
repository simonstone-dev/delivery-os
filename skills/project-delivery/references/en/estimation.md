# Effort, schedule and price

## Define the estimate

State scope version, date, purpose, unit, exclusions, evidence and assumptions. The template uses eight hours per person-day as an editable planning unit, not a contractual promise. Labor cost, vendor price, selling price and customer budget are different quantities.

An early estimate may be a range with explicit sensitivity. Refine it with task evidence. A commitment also requires scope, resources, dependencies, risk allocation and acceptance. Do not invent a universal accuracy percentage.

## Estimate work before capacity

Break deliverables into assignable, verifiable work packages whose actual labor can be measured. Record requirement links, output, role, prerequisites, optimistic/likely/pessimistic days, basis, dependencies and completion criteria. Include discovery, design, data, integration, implementation, QA, security, management, deployment, training and agreed support without double counting.

Bases include comparable accepted tasks, representative trials, expert decomposition and actual supplier quotes, with their limits. Summed likely values are one planning scenario. Summed pessimistic values are a conservative scenario, not a P80 confidence level or guarantee. Probability claims require a calibrated model including correlated risks.

Capacity equals available people × working days × project allocation. It cross-checks whether the plan fits; it does not prove how much work is needed. Reconcile mismatches by investigating omissions, duplication, assumptions and role contention. Two AI-generated estimates are not independent evidence merely because their numbers agree.

Schedule from dependencies, role availability, parallel work, critical path, customer response, approvals and business seasons. Total days divided by headcount is not a delivery commitment. Waiting time is not automatically labor, although support, remobilization and necessary attendance can add labor.

## Measure AI net savings

Use representative tasks and the same completion standard. Count preparation, prompting/generation, human review, integration, testing, correction and communication. Compare the entire accepted task, not typing or generation time. State whether the baseline was measured or estimated.

Transfer measured savings only to sufficiently similar tasks with uncertainty. Record model, tooling and compute cost separately. Do not apply an arbitrary universal AI discount. Parallel agents are not interchangeable with employees; interviews, site work, approval and seasonal verification do not vanish.

## Cost, price and terms

Labor cost can be calculated from work-package days × role-specific cost rate. List hardware, licenses, interfaces, compute, travel, specialist services, backups, support and maintenance with quantities, periods, evidence, currency, tax basis, quote validity and procurement responsibility. Distinguish one-time and recurring costs.

Missing rates remain missing, not zero or a rate borrowed from another project. If only roles, effort and duration are requested, omit prices. Selling price is a commercial decision; distinguish markup from margin with a consistent cost basis. Check applicable tax and payment conditions separately.

Risk reserves should map to identified risks. Avoid adding the same risk both inside a conservative scenario and again as a blanket reserve. Fixed prices need bounded scope and a change mechanism; unresolved items may be provisional, separately investigated or staged.

Explain acceptance and payment triggers, customer obligations, supplier payments, working-capital exposure, support boundaries and change pricing. Appropriate responsible people confirm contractual terms.

## Operating cost and feedback

Estimate ownership cost over an agreed period using explicit volume, price, replacement and support assumptions. Freed labor is not automatically reduced cash expenditure. Capture actual labor, rework, waiting, changes and support, and distinguish scope growth from estimation error.

Only comparable tasks with known boundaries, acceptance and actual labor belong in a reference-rate library. Unaccepted plans remain historical drafts.

## CLI boundary

`estimate` sums task scenarios and complete role-rate labor cost. It rejects empty work lists and invalid intervals; missing rates return a null total. It does not calculate selling price, external cost, tax, schedule, AI discount or probabilistic confidence. `report` omits cost unless `--include-cost` is requested.
