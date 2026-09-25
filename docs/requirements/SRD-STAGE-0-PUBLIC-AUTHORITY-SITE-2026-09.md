# SRD — Stage 0 public authority site · 2026-09

- **Status:** proposed system requirements. Stage 0 is a static artifact only; this does not specify a future application backend.
- **Inputs:** [PRD](PRD-STAGE-0-PUBLIC-AUTHORITY-SITE-2026-09.md) · [trust plan](../plans/STAGE-0-TRUST-PRIVACY-SECURITY-ACCESSIBILITY-PLAN-2026-09.md) · [deployment plan](../plans/STAGE-0-DEPLOYMENT-ROLLBACK-PLAN-2026-09.md).

## System requirements

| ID | Requirement | Verification evidence | Boundary |
|---|---|---|---|
| SR-01 | Build produces a static, versioned artifact from the approved source revision. | Reproducible build command, source/artifact SHA-256 manifest, and clean build check. | Build tool/repository remain UNVERIFIED until inspected. |
| SR-02 | Edge serves only declared static files over approved HTTPS configuration. | Configuration review, response/header read-back, and negative route test. | DNS/certificate/Mini changes remain owner-gated. |
| SR-03 | Published content is constrained to owner-approved claim/proof rows. | Claim approval identifier on each public item; stale/missing approval fails review. | Approval is not inferable from a source file or model output. |
| SR-04 | Public routes require no account, cookie-dependent feature, or application datastore. | Route inventory and network/storage inspection show no protected/runtime dependency. | Browser verification is required before release. |
| SR-05 | The artifact provides accessible semantic structure and respects reduced motion. | Automated checks plus keyboard/viewport review per verification plan. | No WCAG level claim without measured scope/result. |
| SR-06 | Release can be identified and restored to the last verified artifact. | Release record names source/artifact digest, rollback target, operator, and read-back. | Restore drill must be measured before a production-ready claim. |
| SR-07 | Failure and unavailable dependencies are observable rather than silently treated as release success. | Negative build/serve/rollback controls preserve expected-versus-actual output. | Monitoring design remains proposed until host is available. |

## Non-functional requirements

| ID | Requirement | Acceptance boundary |
|---|---|---|
| NFR-01 | Content, route inventory, artifact manifest, and link results have deterministic generation/validation where inputs are stable. | A planted bad link/missing artifact makes the relevant gate fail. |
| NFR-02 | No personal data is intentionally stored by Stage 0. | Data inventory remains empty except operational logs approved by the trust plan. |
| NFR-03 | Release is least-privilege and reversible. | No credential, host mutation, or deployment is performed outside the approved runbook. |

## Out of scope

API, data-model, authentication, authorization, persistence, migration, and runtime integration specifications are N/A until OD-08 has a measured protected-workflow trigger.
