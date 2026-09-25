# Documentation baseline — Stage 0 public authority site · 2026-09

- **Status:** active documentation map. This names every planning/document category applicable to the current static-site stage and every deliberate non-applicability.
- **Rule:** a document is not evidence of implementation. Each is proposed until its own entry/exit gate is met.

## Coverage matrix

| Domain | Artifact | Current home | Status | Stage 0 disposition |
|---|---|---|---|---|
| Business | Business requirements document (BRD) | `requirements/BRD-STAGE-0-PUBLIC-AUTHORITY-SITE-2026-09.md` | Proposed | Required |
| Product | Product requirements document (PRD) | `requirements/PRD-STAGE-0-PUBLIC-AUTHORITY-SITE-2026-09.md` | Proposed | Required |
| System | System requirements document (SRD) | `requirements/SRD-STAGE-0-PUBLIC-AUTHORITY-SITE-2026-09.md` | Proposed | Required |
| Traceability | BRD → PRD → SRD → test/release matrix | `requirements/STAGE-0-TRACEABILITY-MATRIX-2026-09.md` | Proposed | Required |
| UX/technical design | Technical design specification | `design/STAGE-0-TECHNICAL-DESIGN-SPECIFICATION-2026-09.md` | Proposed | Required |
| Architecture | Foundation architecture and ADRs | `architecture/FOUNDATION-ARCHITECTURE-PLAN-2026-09.md`, `decisions/ADR-001…ADR-004` | Proposed | Required |
| Architecture views | Context/container/deployment/sequence diagrams | `architecture/STAGE-0-ARCHITECTURE-VIEWS-2026-09.md` | Proposed | Required |
| Integration | Integration catalog and adapter contract | `integrations/STAGE-0-INTEGRATION-CONTRACT-2026-09.md` | Proposed | Required; zero active runtime integrations |
| Data | Data inventory/retention/handling | `plans/STAGE-0-TRUST-PRIVACY-SECURITY-ACCESSIBILITY-PLAN-2026-09.md` | Proposed | Required; no data store at Stage 0 |
| API | API/interface specification | Integration contract §Stage 0 | N/A | No API/account/backend exists; required before Stage 1 |
| Security | Threat/disclosure/accessibility plan | `plans/STAGE-0-TRUST-PRIVACY-SECURITY-ACCESSIBILITY-PLAN-2026-09.md` | Proposed | Required |
| Quality | Test/verification plan | `plans/STAGE-0-VERIFICATION-PLAN-2026-09.md` | Proposed | Required |
| Delivery | CI/CD, release control, deployment/rollback | `plans/STAGE-0-CI-CD-PLAN-2026-09.md` and related plans | Proposed | Required |
| Operations | Operations, measurement, lifecycle | `plans/STAGE-0-OPERATIONS-MEASUREMENT-LIFECYCLE-PLAN-2026-09.md` | Proposed | Required |
| Governance | Ownership, decisions, change/risk | `OPEN-DECISIONS-REGISTER.md`, governance plan | Active/proposed | Required |
| Legal/commercial | Privacy/disclosure/legal discovery | Trust plan and approval pack | Owner/specialist gated | Required before affected feature/claim |
| Stage 1 | Data model, API contract, auth design, migration/runbooks | Future Stage 1 documentation set | N/A now | Triggered only by OD-08 protected workflow |

## Determinism boundary

| Work class | Treatment | Examples |
|---|---|---|
| Deterministic rails | Script, generate, hash, validate, or gate it; a clean pass and planted failure both remain reproducible | Document-presence checks, links, traceability IDs, source hashes, artifact manifests, test results, release records |
| Evidence-constrained judgment | Keep the reasoning visible, state sources/assumptions/tripwires, and record who decides | Architecture trade-offs, security/threat assessment, requirement priority, acceptance-risk decision |
| Owner/specialist judgment | Never automate or infer it; capture the exact decision and boundary | Public wording, disclosure permission, legal/privacy/financial advice, commercial price, DNS/certificate acceptance |
| Exploratory work | Encourage option generation and challenge, then promote only through deterministic evidence gates | Buyer discovery, design alternatives, incident hypotheses, future Stage 1 architecture |

## Machine-checked artifact contract

`docs/validate-documentation-baseline.py` reads the markers below. The marker list is the machine contract for the required documentation set; an absent artifact fails loudly rather than becoming an unnamed gap.

<!-- baseline-required: docs/requirements/BRD-STAGE-0-PUBLIC-AUTHORITY-SITE-2026-09.md -->
<!-- baseline-required: docs/requirements/PRD-STAGE-0-PUBLIC-AUTHORITY-SITE-2026-09.md -->
<!-- baseline-required: docs/requirements/SRD-STAGE-0-PUBLIC-AUTHORITY-SITE-2026-09.md -->
<!-- baseline-required: docs/requirements/STAGE-0-TRACEABILITY-MATRIX-2026-09.md -->
<!-- baseline-required: docs/design/STAGE-0-TECHNICAL-DESIGN-SPECIFICATION-2026-09.md -->
<!-- baseline-required: docs/architecture/FOUNDATION-ARCHITECTURE-PLAN-2026-09.md -->
<!-- baseline-required: docs/architecture/STAGE-0-ARCHITECTURE-VIEWS-2026-09.md -->
<!-- baseline-required: docs/integrations/STAGE-0-INTEGRATION-CONTRACT-2026-09.md -->
<!-- baseline-required: docs/plans/STAGE-0-DESIGN-PLAN-2026-09.md -->
<!-- baseline-required: docs/plans/STAGE-0-IMPLEMENTATION-PLAN-2026-09.md -->
<!-- baseline-required: docs/plans/STAGE-0-VERIFICATION-PLAN-2026-09.md -->
<!-- baseline-required: docs/plans/STAGE-0-CI-CD-PLAN-2026-09.md -->
<!-- baseline-required: docs/plans/STAGE-0-DEPLOYMENT-ROLLBACK-PLAN-2026-09.md -->
<!-- baseline-required: docs/plans/STAGE-0-PRODUCT-REQUIREMENTS-GOVERNANCE-PLAN-2026-09.md -->
<!-- baseline-required: docs/plans/STAGE-0-TRUST-PRIVACY-SECURITY-ACCESSIBILITY-PLAN-2026-09.md -->
<!-- baseline-required: docs/plans/STAGE-0-RELEASE-CONTROL-CONFIGURATION-PLAN-2026-09.md -->
<!-- baseline-required: docs/plans/STAGE-0-OPERATIONS-MEASUREMENT-LIFECYCLE-PLAN-2026-09.md -->

## No-silent-gap rule

A new capability must either: (1) attach to an existing artifact row and update its requirements/tests/controls, (2) create a new named artifact with an owner and gate, or (3) be explicitly recorded as not applicable with its trigger. “Small” does not bypass this rule.
