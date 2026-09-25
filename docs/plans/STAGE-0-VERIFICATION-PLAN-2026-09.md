# Stage 0 verification plan — static site and edge · 2026-09

- **Status:** proposed. The exact source-repository test commands are intentionally pending source inspection.
- **Goal:** prove the requested public path works, wrong paths fail visibly, and a release can be reversed without relying on a green build alone.
- **Inputs:** [implementation plan](STAGE-0-IMPLEMENTATION-PLAN-2026-09.md) · [ADR-004](../decisions/ADR-004-self-hosted-authority-platform-2026-09.md) · [design plan](STAGE-0-DESIGN-PLAN-2026-09.md).

## Test matrix

| Dimension | Expected path | Negative control | Receipt |
|---|---|---|---|
| Content | Approved text/link appears in the static artifact | A blocked claim token makes the content check fail | Test name, assertion, source revision |
| Structure | Required pages/headings/metadata resolve from the served artifact | Missing route/asset yields a clear non-success response | Local server request/response record |
| Accessibility | Keyboard, heading order, labels, contrast, errors, and reduced-motion behavior work | Remove a label/focus style and verify the check/review fails | Automated result plus manual-review checklist |
| Privacy | Only approved inquiry fields exist and match the published purpose | Add an unapproved field or hidden marketing default; review fails | Data-map and failure-path receipt |
| Artifact integrity | Exact approved static files are what the edge serves | Alter one served asset; digest/read-back mismatch fails | Manifest/digest before and after deployment |
| Edge/TLS | Intended host responds over HTTPS with the intended certificate/host | Wrong host, expired/wrong certificate, or broken route is detected | External request and certificate/host receipt |
| Rollback | Previous static artifact can return intact | Candidate health failure prevents switch or restores prior version | Version/read-back/rollback log |
| Operations | Backup/restore and health checks work on the actual Mini | Restore or health negative control fails closed | Isolated restore/read-back and service-health receipt |

## TDD rule for the source repository

1. Express each new page or public claim as a failing source-repository check.
2. Observe the failure because the approved structure/content is missing, not because a test harness is broken.
3. Make the smallest static change.
4. Re-run the targeted check and retain the observed green output.
5. For a pre-existing path where RED is unavailable, deliberately remove/alter the protected content or route, observe the expected failure, then restore it.

## Two-speed execution

| Speed | When | Scope |
|---|---|---|
| Targeted | Each static markup/content change | The exact content/structure test and local page render |
| Release candidate | Before a deployment handoff | Full static build, link/asset checks, accessibility review, artifact digest, and security/privacy review |
| Live edge | After a reversible deployment only | Host, certificate, routing, served-digest, rollback, and Mini operational checks |

## Limits

No test can prove employment, product operation, customer outcome, or regulatory permission merely because a sentence renders. Those remain evidence/disclosure decisions in the approval pack. No Mini/edge test is valid until read-only access and operational preconditions are restored.
