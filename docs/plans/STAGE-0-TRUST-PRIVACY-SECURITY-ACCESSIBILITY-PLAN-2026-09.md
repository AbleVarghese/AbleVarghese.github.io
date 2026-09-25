# Stage 0 trust plan — privacy, security, accessibility, and disclosure · 2026-09

- **Status:** proposed. This is engineering/privacy discovery, not legal advice or a compliance certification.
- **Goal:** make the public static site trustworthy by default, while preventing a small contact surface from quietly becoming an unbounded data/security system.
- **Inputs:** [professional evidence reconciliation](https://github.com/AbleVarghese/Consult-Able/blob/Portfolio-consult/docs/research/professional-evidence-reconciliation-2026-09.md) · [approval pack](https://github.com/AbleVarghese/Consult-Able/blob/Portfolio-consult/docs/strategy/PUBLIC-CLAIM-APPROVAL-PACK-2026-09.md) · [verification plan](STAGE-0-VERIFICATION-PLAN-2026-09.md).

## Data and disclosure boundary

| Surface | Stage 0 default | Evidence required before enabling |
|---|---|---|
| Public pages | No personal data collected | Approved public claims and content-freshness review |
| Contact path | Prefer no form until purpose, fields, recipient, retention, deletion, and failure behavior are specified | Data inventory and owner-approved privacy wording |
| Files/uploads | Disabled | Separate threat, malware, retention, access, and legal review |
| Accounts/authentication | Disabled | Stage 1 workflow/actor/authorization decision and synthetic security spike |
| Analytics/cookies | Disabled by default | Purpose, consent/jurisdiction analysis, retention, vendor/egress decision, and test evidence |
| Financial/trading references | Omitted | Qualified review plus exact owner-approved, non-regulated wording |

## Public-edge threat model

| Asset / boundary | Threat | Preventive control | Detection / recovery proof |
|---|---|---|---|
| Published copy | Unsupported, stale, confidential, or regulated claim | Approval pack, proof-card expiry, content-review gate | Content scan/review blocks candidate; remove/revert evidence exists |
| Static artifact | Tampered, partial, or wrong version | Source revision, artifact manifest/digest, controlled switch | Served-digest mismatch prevents/prompts rollback |
| Host/TLS/DNS | Wrong host, expired/misissued certificate, hijacked route | Named configuration owner and pre-switch review | Host/certificate/route negative checks and rollback |
| Contact data, if enabled | Over-collection, misdelivery, retention drift, spam | Minimum fields, server-side validation, defined recipient/retention, no default marketing | Failure-path, deletion/read-back, and abuse-response tests |
| Build/release authority | Credential leakage or unauthorized release | Least privilege, no secret in source/logs, owner release gate | Secret scan/review and release record |
| Visitor accessibility | Interaction or information inaccessible | Semantic structure, keyboard/focus, labels/errors, contrast, reduced motion | Automated/manual accessibility checks with planted defect |

## Accessibility acceptance ownership

| Check | Must show | Negative control |
|---|---|---|
| Structure | Logical heading order, landmarks, meaningful link text | Remove a heading/label and observe the review/test failure |
| Keyboard | Reachable controls and visible focus without pointer | Remove focus or trap focus and observe failure |
| Forms, if enabled | Labels, instructions, recoverable error, announced status | Submit invalid/missing input and observe clear recovery |
| Visual | Contrast, zoom/reflow, target size, reduced motion | Check narrow/mobile and reduced-motion states before release |
| Content | Plain language, explicit source/disclosure boundary | Replace approved wording with blocked claim token and observe block |

## Security and disclosure lifecycle

1. **Before source change:** approve copy, identify data fields, update threat/risk entry, define acceptance and rollback.
2. **Before release:** inspect dependencies/configuration, run content/security/accessibility/privacy checks, and record candidate digest.
3. **After release:** verify served host/certificate/digest; record content review/expiry dates and response owner.
4. **When a defect/report arrives:** preserve evidence, contain exposure, communicate according to impact/owner approval, correct/revert, and record a post-incident review.
5. **Before Stage 1:** replace this Stage 0 model with a full application threat model covering sessions, authorization, APIs, persistence, audit, recovery, dependencies, and operational access.

## Legal/compliance discovery questions

These must be answered by the owner and, where applicable, qualified counsel—not inferred from this plan:

- Which jurisdictions, audiences, and personal-data purposes apply to the public site and any inquiry route?
- Are any employer, customer, education, financial, testimonial, logo, or project-status statements permitted?
- Does outreach, cookies/analytics, email, calendar booking, or a form trigger consent/notice/retention obligations?
- Who receives a privacy/security/reporting request, and how is it answered and recorded?

**Stop condition:** any answer that changes data collection, disclosure, or regulated-service exposure becomes a new requirement and cannot be shipped as a content-only change.
