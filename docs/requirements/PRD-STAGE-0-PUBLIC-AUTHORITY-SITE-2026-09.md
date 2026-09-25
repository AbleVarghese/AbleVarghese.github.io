# PRD — Stage 0 public authority site · 2026-09

- **Status:** proposed. This defines the smallest approved static visitor experience; it authorizes neither copy nor deployment.
- **Inputs:** [BRD](BRD-STAGE-0-PUBLIC-AUTHORITY-SITE-2026-09.md) · [approval pack](https://github.com/AbleVarghese/Consult-Able/blob/Portfolio-consult/docs/strategy/PUBLIC-CLAIM-APPROVAL-PACK-2026-09.md) · [open decisions](https://github.com/AbleVarghese/Consult-Able/blob/Portfolio-consult/docs/OPEN-DECISIONS-REGISTER.md).

## Product outcome

A relevant B2B visitor can understand one approved operations-diagnostic offer, inspect only approved proof, identify fit, and choose one privacy-described next step without an account or hidden collection.

## User stories and acceptance

| ID | Story | Acceptance criterion | Exclusion |
|---|---|---|---|
| PR-01 | As a visitor, I can identify the offer and intended audience. | Approved home route exposes approved proposition, scope, and fit/non-fit statement. | No unapproved performance/customer/employer claim. |
| PR-02 | As a visitor, I can judge credibility. | Every proof card links to an approved public source/disclosure row and review date. | Private résumé/LinkedIn source is never rendered or linked. |
| PR-03 | As a visitor, I can take one minimal next step. | One owner-approved contact route states purpose, recipient, and data boundary before use. | No account, CRM, calendar, payment, upload, or invisible tracker. |
| PR-04 | As a visitor, I can use the site accessibly. | Keyboard path, semantic headings, readable contrast, alt text, and reduced-motion behavior pass the approved verification plan. | No accessibility conformance claim before measured evidence. |
| PR-05 | As an operator, I can publish/reverse the static release safely. | Release has source/artifact digest, host read-back, rollback target, and approval record. | No DNS/certificate/Mini change before gated approval. |

## Product boundaries

| Included after approval | Explicitly not Stage 0 |
|---|---|
| Static pages: home, offer, proof, insight, contact/privacy | Dynamic account, protected portal, database, API, auth, forms that persist data, analytics, AI/chat, booking, payment |
| Public-safe proof cards and outbound links | Any source or claim outside the approval pack |
| One minimal approved contact path | Collection beyond what that third-party contact route necessarily receives |

## Product acceptance gate

PR-01 through PR-05 must map to SRD requirements and verification IDs. Owner-approved wording/proof and a measured repository/host path are preconditions; absent either, this remains a proposed product definition.
