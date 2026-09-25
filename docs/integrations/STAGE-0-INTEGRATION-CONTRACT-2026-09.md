# Stage 0 integration contract · 2026-09

- **Status:** proposed. Stage 0 has **zero active runtime integrations**.
- **Purpose:** prevent a static public site from quietly gaining an API, datastore, credential, embedded vendor, or personal-data flow.

## Catalog

| Boundary | Stage 0 state | Contract | Gate |
|---|---|---|---|
| Browser → static edge | Proposed | HTTPS GET/HEAD serves declared static files only; no account/session/API dependency. | SR-02, SR-04, VT-05/07/10 |
| Static site → approved contact route | Conditional external navigation | Visible outbound link only; destination, purpose, recipient, and data boundary are disclosed before use. | PR-03, SR-03, VT-03/05 |
| Static site → DNS/certificate authority | Conditional infrastructure trust | Only owner-approved hostname/certificate configuration; no secret appears in repository or page. | Deployment/rollback gate |
| Static site → analytics/CRM/booking/email/API/database/auth | **N/A / prohibited at Stage 0** | No tag, SDK, form handler, cookie-dependent workflow, account, or persistence. | VT-05/10 |

## Contract rules

1. An outbound link is not an endorsement or a data-processing guarantee; the published disclosure states only the observed destination and purpose.
2. No embedded script, iframe, form action, SDK, credential, server action, webhook, or client-side collector is permitted without a new approved integration row, privacy/security review, architecture update, and traceability IDs.
3. Contact-route availability is checked as a link/interaction boundary; a delivery-success claim requires evidence from the destination owner and is otherwise **UNVERIFIED**.
4. DNS and public certificate authorities are explicit external-trust assumptions, not managed-service application dependencies.

## Stage 1 trigger

A protected workflow justified by OD-08 requires an API/interface specification, data model, authentication/authorization contract, retention/deletion model, threat model, migration/runbook, and integration-specific negative controls before any implementation begins.
