# Verification scope

The release separates three questions: do the tools run, do records remain consistent, and does the method improve real project decisions?

## Reproducible tool checks

```bash
python -m unittest discover -s tests -v
python scripts/verify_release.py
```

Behavior tests cover the two README walkthroughs, empty and existing destinations, portable copied projects, duplicate sources, immutable path versions, checksum changes, invalid references and numbers, a 2,000-task dependency chain, cycles, missing prices, decimal arithmetic, fresh reports, approval metadata and premature handoff rejection.

The release checker verifies local links, declared language pairs, matching demo IDs and estimation contracts, version references, skill frontmatter and a limited public-file hygiene scan. It does not scan the network, certify all sensitive-data patterns or prove semantic translation equivalence.

CI is configured for Windows, Ubuntu and macOS with Python 3.10 and 3.12. Consult the Actions run for actual remote results; a configured matrix is not a completed matrix. Local release results are described in [release verification](../../examples/release-verification.md).

## Scenario rubric

The synthetic expense-intake example intentionally contains unconfirmed AI notes, a deployment conflict, missing samples, no price and no business-system implementation. A useful interpretation must:

1. Preserve the two-template, human-reviewed phase-one boundary.
2. Exclude payment execution from the proposed phase.
3. Track deployment as a question for the authorized customer IT owner.
4. Treat OCR as unverified until samples and scoring criteria exist.
5. Leave budget, rates, approvals and test evidence unknown.
6. Trace requirements to sources, work packages and acceptance items.
7. Explain the project in business terms before implementation detail.
8. Preserve pending acceptance and prevent premature handoff.

See [the authored walkthrough](../../examples/scenario-review.en.md). The fixtures and interpretation were written by the maintainer, and tests check mechanics and declared boundaries. They are **not an independent model evaluation**, a measured project success rate or proof that every agent will follow the method.

## Proving real-world effect

On an actual project, record first-pass omissions, clarification cycles, rework and its causes, estimate-versus-actual labor, external waiting, accepted output quality and total AI-assisted effort. Compare equivalent scope and quality standards; disclose whether the baseline is measured or estimated. Keep client information private and publish only permitted, anonymized results.

No universal estimation accuracy, AI-efficiency percentage or guaranteed delivery outcome is claimed. Record completeness is useful evidence of control, not proof of business correctness.

[中文](../zh/validation.md) · [Home](../../README.md)
