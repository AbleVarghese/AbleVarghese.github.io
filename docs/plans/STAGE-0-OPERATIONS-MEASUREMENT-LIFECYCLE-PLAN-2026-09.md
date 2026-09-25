# Stage 0 operations, measurement, and lifecycle plan · 2026-09

- **Status:** proposed. No target, alerting service, analytics product, uptime target, or on-call obligation is assumed.
- **Goal:** make the static site observable, recoverable, current, and worth keeping without creating surveillance or an unmanaged operations burden.
- **Inputs:** [deployment/rollback plan](STAGE-0-DEPLOYMENT-ROLLBACK-PLAN-2026-09.md) · [trust plan](STAGE-0-TRUST-PRIVACY-SECURITY-ACCESSIBILITY-PLAN-2026-09.md) · [B2B strategy](https://github.com/AbleVarghese/Consult-Able/blob/Portfolio-consult/docs/strategy/B2B-CONSULTING-GROWTH-EXECUTION-PLAN-2026-09.md).

## Operating model

| Area | Stage 0 minimum | Evidence before calling it active |
|---|---|---|
| Service definition | Named host, intended visitor path, content owner, estate operator, and release owner | Owner/host map in release record |
| Health | External host/route/certificate/static-asset check after release and on a defined cadence | Successful normal check and planted bad-host/bad-route control |
| Availability target | Baseline first; target/alert window approved only after real host measurement | Dated baseline and owner-approved target; no invented uptime number |
| Logs | Minimum edge/release/error evidence with access/retention owner | Log fields, privacy classification, retention/deletion method, and read-back |
| Incident response | Named contact, containment/revert path, evidence preservation, post-incident review | Tabletop or controlled failed-candidate exercise |
| Backup/recovery | Current configuration/artifact backup and tested restore/read-back | Isolated restore receipt; no backup claim from “job succeeded” alone |
| Maintenance | Content freshness, certificate, dependency, host, backup, and recovery review cadence | Dated review entries and overdue escalation |
| Cost/capacity | Mini disk/RAM/CPU/listeners measured before hosting | Read-only capacity snapshot and resource boundary |

## Measurement without surveillance

```mermaid
flowchart LR
  P[Published approved content] --> Q[Consent-respecting inquiry or feedback]
  Q --> R[Qualified conversation]
  R --> D[Paid diagnostic signal]
  D --> L[Learning record]
  L --> P
```

| Question | Stage 0 measurement | Do not use as proof |
|---|---|---|
| Does the site communicate the offer? | Owner review, qualitative feedback, relevant inquiry context, source/content review | Raw pageviews or vanity traffic alone |
| Does the diagnostic attract fit? | Qualified-conversation and paid-diagnostic signals from the B2B strategy | A contact-form submission count without fit/outcome |
| Is the site trustworthy/usable? | Accessibility review, complaint/issue log, host/certificate/route checks | Absence of reported problems |
| Is data use proportionate? | Field/retention review and consent/notice evidence | A hidden analytics default or “anonymous” assertion |
| Is content current? | Scheduled proof-card/source/claim expiry review | Original publication date |

## Incident, recovery, and review loop

| Trigger | First response | Closure evidence |
|---|---|---|
| Broken host/TLS/route | Preserve observation; contain by retaining/restoring known-good artifact/configuration | Expected path/certificate/digest read-back |
| Unsupported/stale claim | Remove or revert the claim; preserve source/review evidence | Corrected content, owner decision, updated expiry/review date |
| Privacy/security concern | Stop the affected collection/release path; minimize further exposure; escalate to owner/specialist | Scope, actions, communication decision, corrective/verification record |
| Mini resource/recovery failure | Freeze expansion; protect existing workloads; use recovery plan | Capacity/recovery evidence and revised deployment decision |
| Material outcome miss | Run a blame-free review: expected, actual, why, sustain/change | Dated learning and revised requirement/plan |

## Lifecycle and retirement

1. Review published proof/cards/links at their recorded expiry; unverified items are removed rather than silently retained.
2. Review the operational path after each material change and on the cadence chosen from real baseline data.
3. Retire the site or a data-collection surface by disabling public exposure, preserving required release/evidence records, applying approved data-retention/deletion actions, and verifying the retired path is unreachable.
4. A Stage 1 application is not an upgrade-by-default. It needs the protected-workflow decision, its own SLO/data/incident/recovery plan, and an explicit migration/rollback strategy.

**Exit gate:** operations are ready only when normal health, a planted failure, restore/read-back, an incident/revert exercise, content-expiry handling, and the next-review owner/date have all been observed.
