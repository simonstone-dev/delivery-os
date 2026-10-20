# References and tool choices

Reviewed 2026-10-20. These are sources of ideas and potential integrations, not endorsements, certifications or installed dependencies. DeliveryOS scripts, wording and templates are original; no third-party framework code is bundled.

| Reference | What we use | Boundary |
|---|---|---|
| [GOV.UK Service Manual](https://www.gov.uk/service-manual/agile-delivery) | Understand the problem, test risky assumptions, progress through delivery stages | Adapt the method; government approval rules and typical durations do not become universal requirements |
| [GAO Cost Estimating Guide](https://www.gao.gov/products/gao-20-195g) | Technical baseline, work breakdown, evidence, assumptions, risk and actual-cost feedback | Provides estimating principles, not support for any specific estimate |
| [arc42](https://arc42.org/overview/) | Check architecture context, constraints, runtime, deployment, decisions and quality | Consult and tailor; its template is not reproduced here |
| [GitHub Spec Kit](https://github.com/github/spec-kit) | Candidate implementation workflow from specification to tasks and code | Optional future integration; it does not by itself cover commercial terms or field delivery |
| [BMad Method](https://github.com/bmad-code-org/BMAD-METHOD) | Product, architecture, UX, development and test perspectives | Method reference; do not install competing workflows by default |
| [Promptfoo](https://github.com/promptfoo/promptfoo) | Candidate automated regression tool for models, prompts and RAG | Use when an AI component needs it; not full business acceptance |
| [OpenAI Skills](https://developers.openai.com/plugins/concepts/skills) | Portable instructions with focused references, scripts and templates | The agent still needs appropriate tools, access and review |

Spec Kit, BMad and Promptfoo publish MIT licenses in their repositories. arc42 documentation/templates publish CC BY-SA 4.0; its [license explanation](https://github.com/arc42/arc42-template/blob/main/LICENSE.txt) distinguishes adapted templates from users' own architecture content. If integrating external code or templates later, retain applicable notices and review the exact version and additional terms. Model weights, data and services can have separate licenses.

The workflow was also informed by anonymized observations about source authority, missing submission items, untested assumptions, capacity-based estimates and acceptance-state confusion. No client names, original materials or claimed completed-project results are included.

[中文](../zh/references.md) · [Home](../../README.md)
