# Software-delivery completeness audit — 2026-09

- **Status:** partial, evidence-gated audit. It identifies the missing planning artifacts for this project; it does not claim current external standards were fully revalidated.
- **Question:** what planning/documentation work is still required before a static authority site can safely move from proposed architecture to a controlled release, and what additional artifacts must precede a protected Stage 1 application?
- **Overlap check:** existing SSDF/ASVS source records (`S09`, `S01`) and existing architecture, ADRs, strategy, verification, CI/CD, and deployment plans were read. This audit adds the cross-cutting lifecycle coverage map; it does not duplicate their decisions.

## Evidence limits

| Source set | Observation on 2026-09-24 | Allowed use |
|---|---|---|
| Prior local SSDF/ASVS source records | Existing records identify the official NIST SSDF and OWASP ASVS sources, but do not contain a software-delivery planning crosswalk | Source discovery only; not a current normative quotation |
| New official-source collection SD01–SD06 | All six URL retrievals failed on DNS resolution timeout; raw empty response, headers, stderr, status, access time, and SHA-256 are preserved under `sources/` | `BLOCKED`; do not reconstruct current standard wording |
| This repository’s architecture/ADRs/plans | Directly readable, current local planning evidence | Current-scope gap analysis |

**Result:** there is no single universal “gold-standard plan set.” A defensible standard for this project is an evidence-gated lifecycle: every phase has a named owner, entry/exit criteria, failure path, artifact, and a traceable connection to the next phase. The lifecycle below is an internal proposed control model, not an assertion about any blocked external source.

## Lifecycle coverage map

| # | Artifact family | Why it exists | Current coverage | Disposition |
|---:|---|---|---|---|
| 1 | Vision, outcomes, and commercial hypothesis | Prevent solution-first building | B2B strategy and ADR-001 | ✅ Existing |
| 2 | Stakeholder, ownership, and decision rights | Prevent anonymous approval and scope drift | Open-decision queue exists; no responsibility/decision map | ➕ Governance plan |
| 3 | Requirements, scope, and acceptance traceability | Make “build the site” testable | Page intent exists; no source-to-acceptance traceability | ➕ Requirements plan |
| 4 | UX/content and accessibility | Make the public path understandable and usable | Design plan exists; needs ownership/review cadence | ➕ Extend through governance plan |
| 5 | Architecture and ADRs | Bound technology, data, and reversibility | Foundation architecture and ADR-002–004 | ✅ Existing |
| 6 | Data inventory, privacy, retention, and legal discovery | Avoid collecting/storing data without purpose | Minimality policy exists; no operational inventory/retention/compliance discovery plan | ➕ Trust plan |
| 7 | Threat model and security verification | Identify abuse paths before implementation | ADR FMEA exists; no dedicated public-edge/contact threat model | ➕ Trust plan |
| 8 | Implementation/work-breakdown plan | Sequence smallest reversible change | Stage 0 implementation plan | ✅ Existing |
| 9 | Quality, test, and non-functional verification | Prove functional, negative, accessibility, privacy, and recovery paths | Verification plan exists | ✅ Existing |
| 10 | Configuration, secrets, environments, and dependency governance | Keep deploy state reproducible and least-privileged | Scattered boundaries; no operational plan | ➕ Release-control plan |
| 11 | CI/CD, artifact provenance, and change control | Make releases reproducible and reviewable | CI/CD plan exists; needs named release/configuration control | ➕ Release-control plan |
| 12 | Deployment and rollback | Make release reversible | Deployment/rollback plan exists | ✅ Existing |
| 13 | Observability, service objectives, incident response | Detect/recover from real service failure | ADR notes health; no objectives, alert, incident/exercise plan | ➕ Operations plan |
| 14 | Backup, recovery, continuity, and maintenance | Survive host, data, and dependency failure | ADR has a restore gate; no runbook/maintenance ownership | ➕ Operations plan |
| 15 | Documentation, support, content governance, and release notes | Keep operation/claims understandable after handoff | Plan index and artifact register exist; no public-content/support lifecycle | ➕ Operations plan |
| 16 | Measurement, feedback, experiment, and post-launch review | Learn without inventing success | B2B funnel model exists; no privacy-safe Stage 0 measurement/review contract | ➕ Measurement plan |
| 17 | Retirement and data deletion | Avoid an unowned site, stale claims, or retained inquiry data | No end-of-life/retention exit plan | ➕ Operations/trust plans |

## Missing-stage verdict

```mermaid
flowchart LR
  A[Strategy + architecture] --> B[Governance + requirements]
  B --> C[Approved design + trust]
  C --> D[Implementation + verification]
  D --> E[Release control + deployment]
  E --> F[Operations + measurement]
  F --> G[Review, renewal, or retirement]
```

The project had strong coverage from architecture through deployment planning, but four control planes were unnamed or incomplete: **governance/requirements**, **trust**, **release control**, and **operations/measurement**. These are now the required plan additions.

## Council lite — plan-suite decision

| Lens | Finding | Change adopted |
|---|---|---|
| Contrarian | More documents can hide missing ownership behind apparent completeness | Every new plan has an owner, entry/exit gate, failure path, and evidence record |
| First-principles | A release cannot be trusted unless it identifies what changes, who approves it, how it is tested, and how it reverses | Requirements traceability and release-control records are mandatory |
| Expansionist | A small Stage 0 should leave a clean path to Stage 1 without prebuilding it | Stage separation is explicit; Stage 1 remains a workflow-triggered decision |
| Outsider | Privacy, accessibility, operations, and retirement are often omitted because they are not visible in a page mockup | Trust and operations/lifecycle plans are separate control surfaces |
| Executor | Mini access and copy approval are the immediate constraints, not more platform selection | Every plan stays proposed and blocks source/deploy execution until its stated gate passes |

**Chairman verdict:** add the four grouped control plans, not a ceremony-heavy universal framework. The accepted risk is that official-source wording could not be refreshed while DNS resolution is unavailable; all affected external-framework claims remain `UNVERIFIED` pending the preserved re-fetch gate.

## Stage separation

| Concern | Stage 0 static public site | Stage 1 protected application |
|---|---|---|
| Data | No account; no unnecessary form; retention purpose before collection | Data classification, actor model, authorization, audit, deletion, migration, recovery |
| Security | Static artifact, host/TLS, contact boundary, supply-chain/release controls | Full threat model, auth/session/revocation, authorization, API, dependency and security test suite |
| Operations | Host/edge availability, content review, certificate/backup/rollback | SLOs, database recovery, queue/outbox reconciliation, on-call/incident exercises |
| Compliance | Privacy/cookie/contact disclosure review | Jurisdiction-specific privacy/security/financial/legal assessment before handling regulated data |
| Measurement | Consent-respecting qualitative inquiry and published-content review | Product/outcome metrics with data minimization and access control |

## Planned additions

1. **Product requirements and governance plan** — scope, owners, approval rights, requirements-to-test traceability, milestones, risks, and change control.
2. **Trust plan** — data inventory, privacy/retention, legal discovery, threat model, accessibility ownership, security verification, and vulnerability disclosure path.
3. **Release-control plan** — environment/configuration/secrets/dependencies, artifact provenance, release criteria, change records, and configuration rollback.
4. **Operations and continuous-improvement plan** — service objectives, monitoring, incident/backup/recovery/maintenance runbooks, content support, measurement, review, and retirement.

## External-research recovery gate

When network name resolution is working, re-fetch SD01–SD06 from the exact URLs in `COLLECTION-ADMISSION.md`, retain their operative wording and access dates, then revise this audit only where primary-source evidence changes a proposed control. Until then, all external-framework mappings remain `UNVERIFIED` rather than implied.
