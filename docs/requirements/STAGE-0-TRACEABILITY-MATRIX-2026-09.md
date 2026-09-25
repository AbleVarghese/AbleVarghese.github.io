# Stage 0 traceability matrix · 2026-09

- **Status:** proposed traceability contract. IDs are stable; each release must attach executed evidence before any row is called complete.

| BRD | PRD | SRD/NFR | Design / architecture | Verification / release evidence | Status |
|---|---|---|---|---|---|
| BR-01 | PR-01 | SR-01, SR-03 | TDS content model; architecture context | VT-01 approved-content review; VT-02 static build | Proposed |
| BR-02 | PR-02 | SR-03 | TDS proof-card model; integration contract | VT-03 approval/provenance check; VT-04 bad approval negative control | Proposed |
| BR-03 | PR-03 | SR-04, NFR-02 | TDS contact boundary; integration contract | VT-05 route/network/storage inspection | Proposed |
| BR-04 | PR-04, PR-05 | SR-02, SR-05, SR-06, SR-07, NFR-01, NFR-03 | Architecture deployment view; TDS accessibility/release rules | VT-06 accessibility review; VT-07 serve negative; VT-08 rollback drill | Proposed |
| BR-05 | — | NFR-01, NFR-02 | TDS measurement boundary | VT-09 approved measurement review | Proposed |
| BR-06 | — | SR-04, NFR-02, NFR-03 | Architecture container/deployment view | VT-10 no-runtime-dependency inspection | Proposed |

## Traceability rules

1. A requirement may not move beyond proposed without an executed evidence link and a named reviewer.
2. A design or source change updates its affected ID row before release review.
3. A missing ID, missing test/evidence, or an evidence item that exercises only a mock is a release-blocking gap.
4. Stage 1 requirements receive new IDs; they do not silently expand Stage 0 rows.

## Verification ID index

| ID | Required observation |
|---|---|
| VT-01 | Approved wording/proof rendered only from approved rows. |
| VT-02 | Static artifact rebuild and digest are reproducible. |
| VT-03 | Every proof/contact claim has approval, provenance, and review date. |
| VT-04 | Missing/expired approval is rejected before publication. |
| VT-05 | Browser/network/storage inspection sees no account, datastore, or unexpected collection. |
| VT-06 | Keyboard, semantic, contrast, viewport, and reduced-motion review is recorded. |
| VT-07 | Invalid route/config/build failure is loud and cannot publish an artifact. |
| VT-08 | Prior verified artifact restores and is read back. |
| VT-09 | Only owner-approved, privacy-bounded learning signals are configured. |
| VT-10 | Route/dependency inspection confirms no Stage 1 runtime boundary. |
