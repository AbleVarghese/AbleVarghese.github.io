# ADR-003: Stage identity and integrations behind a protected actor contract

- **Status:** Proposed · pending independent red-team challenge · candidate-selection direction in items 3–4 superseded by [ADR-004](ADR-004-self-hosted-authority-platform-2026-09.md) · 2026-09-23
- **Decision type:** Type 1 architecture; no identity provider, package, service, deployment, account, or integration is adopted here.
- **Related:** [foundation architecture plan](../architecture/FOUNDATION-ARCHITECTURE-PLAN-2026-09.md) · [identity Solvemax matrix](identity-foundation-matrix-2026-09.output.txt) · [self-host matrix](self-hosted-authority-platform-matrix-2026-09.output.txt) · [ADR-002](ADR-002-admin-portal-foundation-2026-09.md).

## Context

The platform has three materially different access stages: public authority content, protected owner/staff operations, and a later invite-only client workspace. Treating them as one generic account system would create premature identity surface, blur authentication (who signed in) with authorization (what they may do), and weaken ADR-002’s private-core/data-command controls.

A bounded eight-repository screen found permissive, mature candidates but no evidence that a full identity platform is needed now. The current local portfolio contains a Better Auth source pattern in Keralora, Supabase/RLS patterns in LawyerServed, and a single-operator Authelia configuration under Scrapos. These are source observations, not runtime validation or automatic reuse. Direct candidate evidence is preserved under [`foundation-architecture-evidence-2026-09`](../research/foundation-architecture-evidence-2026-09/).

## Decision

1. **Keep the public site account-free.** Visitors can read public proof and submit a minimized intake; no generic sign-up, client dashboard, social login, or self-service organization system is added.
2. **Create a stable internal actor contract before provider-specific application logic.** It contains a provider identifier, provider subject, internal actor identifier, session assurance, and revocation state. It contains no business authorization claim.
3. **Under the owner’s self-hosted direction, test Better Auth as the first embedded authentication candidate when protected staff access becomes real.** It is MIT, TypeScript-native, and must prove the protected actor/command behavior against synthetic data.
4. **Defer full self-hosted Supabase as a platform alternative.** Its database/auth/API/realtime/storage/dashboard scope is available if a measured need earns it; it is not a default fallback or a parallel identity source.
5. **Select exactly one identity issuer after the spike.** Do not operate Supabase Auth and Better Auth as parallel sources of account truth.
6. **Keep authorization in the private database/server-command boundary.** Provider sessions authenticate; commands and database policy authorize. Admin UI permissions do not decide access.
7. **Add integrations only through narrow adapters and an outbox.** Calendar, billing, email, storage, analytics, and future CRM copies cannot write core tables directly or become a second operational truth.
8. **Defer Authelia, Ory Kratos/Hydra, and Keycloak** until a measured access requirement needs a perimeter gateway, enterprise federation, or cross-product identity. Exclude ZITADEL (AGPL-3.0); do not admit Logto (MPL-2.0) under the current permitted-license list.
9. **Require explicit owner approval before any managed identity service is provisioned or receives identity data.** The recommended future spike is synthetic/local only; a provider’s open-source repository does not authorize managed-service use or a new personal-data egress path.

## Why this direction

| Evidence | Implication |
|---|---|
| ADR-004 self-host screen: full Supabase platform is Apache-2.0 and self-hostable, but includes database/auth/API/realtime/storage/dashboard capability | Defer it until a measured requirement earns the operating surface |
| Better Auth: MIT, framework-agnostic TypeScript; current Keralora source uses version `1.6.25` | First embedded candidate, not a free pass; current local runtime has not been revalidated |
| Auth.js README recommends Better Auth for new projects except specific stateless-session gaps | Avoid a redundant new Auth.js route |
| Ory/Kratos and Keycloak direct documentation | Mature but add a separate identity operations surface before current evidence requires one |
| Authelia direct README and owner template | Useful future perimeter reference; owner template is deliberately single-operator and unsuitable as the assumed client identity model |
| Original identity matrix | Historical comparison only: its fragile 62.0% staged result is superseded for self-host candidate selection by ADR-004’s 93.7% direct-self-host result |

## Non-negotiable controls

1. Core tables stay non-exposed; browser roles have no broad direct `INSERT`, `UPDATE`, or `DELETE` permissions.
2. An identity session does not grant access by itself. Every protected action rechecks authorization against the internal actor, scope, role/grant, and current revocation state; business roles do not live only in a long-lived token.
3. Provider identity links are unique on `(provider, subject)`. Never auto-link or merge accounts merely because email addresses match; a conflicting link requires an audited staff-controlled recovery path.
4. Staff operations require a verified multi-factor-authentication (MFA) assurance level. The chosen provider must expose enough evidence for that check; otherwise it fails the spike.
5. No provider secret or service-role secret reaches browser code or an admin framework. Any service-role worker is separately scoped to one named outbox/reconciliation duty; generic server routes do not inherit it.
6. An inbound provider event is authenticated, schema-validated, timestamp-bounded, replay-protected, idempotent, auditable, and translated into one named command.
7. An outbound effect originates in a transactional outbox record; delivery is at-least-once, so the receiving adapter must be idempotent and a retry/reconciliation receipt remains visible.
8. Evidence sealing, stage changes, concurrency checks, and billing reference updates obey ADR-002 unchanged.
9. A provider outage or token-validation failure fails closed for protected access and produces an observable error; it never silently grants access through a fallback. Before staff access is relied upon, a separately documented, owner-attended, time-bounded, audited break-glass recovery process must be tested. It is not a standing second identity provider or a generic database bypass.
10. Before adoption, pin the selected version, inspect its transitive dependency/security advisories locally, and prove upgrade, rollback, and account-link migration behavior with synthetic data.

## Candidate screen

| Candidate | License gate | Role in this ADR |
|---|---|---|
| Supabase Auth | MIT — passes | Deferred as part of the broader self-hosted Supabase-platform alternative |
| Better Auth | MIT — passes | First synthetic spike candidate |
| Auth.js | ISC — passes but direct source recommends Better Auth for new projects | Do not start a new route |
| Authelia | Apache-2.0 — passes | Future internal/perimeter reference only |
| Ory Kratos/Hydra | Apache-2.0 — passes | Future enterprise-federation reference only |
| Keycloak | Apache-2.0 — passes | Future large-IAM reference only |
| ZITADEL | AGPL-3.0 — fails | Default exclusion |
| Logto | MPL-2.0 — outside permitted list | Not admitted without a separate owner decision |

## Council: Tier 1 inline review

| Lens | Finding | Effect |
|---|---|---|
| Contrarian | A second identity provider in production creates account and authorization drift | One issuer only; any later alternative is a synthetic test, not a parallel deployment |
| First-principles | The immediate business need is public proof plus protected staff work, not customer self-service identity | Keep public users account-free |
| Expansionist | A stable actor contract can later support clients, SSO, and products without rewriting domain records | Preserve the actor seam now |
| Outsider | A mature IAM platform may be correct for enterprise federation but is excessive for a founder-stage authority site | Defer Ory/Keycloak class systems |
| Executor | A synthetic two-provider test settles the only consequential uncertainty cheaply | Use the spike before installation/adoption |

| Anonymized peer review | Finding folded into the plan |
|---|---|
| A | Break-glass recovery can become a permanent shadow identity provider; make it owner-attended, time-bounded, audited, and unavailable to normal application routes. |
| B | A private schema still fails if generic server routes carry a service-role secret; scope it only to a named worker duty. |
| C | Any second-provider comparison becomes drift if both providers receive live accounts; test only with synthetic identities, then choose one. |
| D | An adapter layer becomes hidden microservice sprawl if added speculatively; create each only with a measured integration need. |
| E | A managed identity option changes the personal-data boundary even if its source is open; require per-instance owner authorization. |

**Chairman:** stage public-first; test Better Auth only when a real protected workflow exists; retain one private authorization model regardless of identity provider. Re-open the candidate screen if it fails rather than starting a parallel provider. The accepted risk is a delayed client workspace in exchange for avoiding an unproven identity/operations burden.

## Required spike

| Test | Positive proof | Negative control |
|---|---|---|
| Session | Allowed staff identity maps to one stable actor | Expired, invalid, revoked, or wrong-issuer session fails closed |
| Authorization | Granted actor can execute one named command | Ungranted actor cannot read or mutate another scope |
| Private core | Curated view returns permitted data | Authenticated raw `PATCH`/`DELETE` to protected record returns `401`/`403` |
| Identity uniqueness | Repeated provider callback resolves the same actor safely | Conflicting provider subject/account link fails visibly |
| Revocation | Revoked actor loses access on the next protected request | Cached browser state cannot keep access alive |
| Provider parity | Both candidate providers satisfy the same fixture | Any candidate requiring browser-held privileged credentials is rejected |
| Account link | One provider subject maps to one actor | Same email from a different provider subject cannot silently merge accounts |
| Assurance | MFA-qualified staff session can execute the protected test command | Password-only or unverifiable-assurance session is refused for staff operations |
| Integration event | Valid signed event records one idempotent delivery result | Duplicate, unsigned, stale, or malformed event cannot mutate core state |
| Recovery | Owner-controlled recovery can restore a deliberately revoked test staff account with an audit record | Provider outage cannot silently bypass authorization or leave recovery undefined |

## Internal adversarial amendments

The mandatory independent challenge tool was invoked twice—once before and once after these amendments—but each call returned only a receipt rather than a substantive verdict. Neither can certify this ADR. An internal threat-model pass therefore adds these concrete attack controls; a future substantive independent review may overturn them.

| Attack | Risk | Required control |
|---|---:|---|
| OAuth or email collision links an attacker to a real actor | 9×4×8 = 288 | Unique provider/subject link; no automatic email merge; audited recovery only |
| Revoked staff token retains an old role | 9×5×7 = 315 | Recheck grant/revocation at each protected command; short-lived provider session alone is insufficient |
| MFA is presented in the UI but not proven by the session | 9×4×8 = 288 | Verify provider assurance in the command path; reject if the provider cannot prove it |
| Forged or replayed calendar/billing webhook changes an engagement | 8×5×7 = 280 | Signature, timestamp window, replay/event-id ledger, schema validation, idempotent command |
| Outbox retry charges/sends twice | 8×4×7 = 224 | At-least-once semantics named; provider idempotency key and reconciliation required |
| Identity provider outage locks the owner out or causes an unsafe bypass | 8×4×8 = 256 | Fail closed plus an audited, owner-controlled break-glass procedure tested before reliance |
| Managed auth receives identity data without approved egress scope | 9×3×9 = 243 | No provisioning/data transfer without explicit owner approval for that instance and data class |
| Break-glass becomes a standing shadow provider | 9×3×8 = 216 | Owner-attended, time-bounded, audited recovery only; no ordinary route or generic database bypass |
| A generic server route gains a service-role secret | 9×4×8 = 288 | Scope service credentials to a named worker; tests prove ordinary routes cannot invoke privileged mutations |

## Reversal / kill criteria

1. Better Auth cannot pass every spike negative control, requires a browser-facing privileged key, or needs a second authoritative authorization store → reject it and re-open the self-host candidate screen.
2. A measured requirement needs the Supabase platform’s realtime/storage/generated-API capabilities and its operational burden remains acceptable → re-open ADR-004 rather than adding individual platform services ad hoc.
3. A real paid requirement needs SAML, SCIM, cross-product identity, or a separate perimeter gateway → re-open this ADR with Ory/Keycloak/Authelia evidence.
4. A candidate’s license, release, security, or operating posture materially changes → re-run the repository admission gate before upgrade/adoption.
5. A public-account feature cannot demonstrate an immediate, measured user need → keep it out of scope.

## What would reverse this decision

An actual website repository that uses a different data/runtime stack, a failed Better Auth protected-core spike, a measured need for the self-hosted Supabase platform, or a paid enterprise identity requirement would reverse or refine this staged direction.

## Verification status

**UNRESOLVED CRUX:** the choice is intentionally uncommitted because the matrix is fragile and no target website runtime exists. Two red-team tool calls returned only receipts, not verdicts; a substantive independent review is still required before this ADR can be promoted from Proposed.
