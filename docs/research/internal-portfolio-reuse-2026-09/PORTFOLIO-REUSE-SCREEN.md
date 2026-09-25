# Internal portfolio reuse screen · 2026-09

- **Status:** read-only screen complete. No repository, tool, package, service, or code has been integrated.
- **Authority:** owner request in this session.
- **OVERLAP-CHECK:** extends the bounded owner-site discovery in the self-host research and the prior-art observations in foundation/admin research. It does not claim that a public repository is operationally compatible.

## Collection result

| Scope | Result | Evidence |
|---|---:|---|
| Public owner repository metadata | 292 rows | `github-public-repositories.json` |
| Keyword shortlist | 61 rows | `keyword-candidates.tsv` |
| Deep shortlist | 7 owner repositories | `shortlist-evidence.tsv` and `shortlist/` |
| Private repositories/source code/package installs | 0 | Prohibited by collection admission |

## Stage-0 source comparison

| Candidate | Direct evidence | Fit to the approved static-first boundary | Operational / license risk | Disposition |
|---|---|---|---|---|
| **`AbleVarghese.github.io`** | Public owner repo; HTML; root contains `index.html` and `assets/` | Exact current public portfolio source shape; account-free and zero-dependency | GitHub metadata reports `NOASSERTION`; source/release/host still need inspection and owner approval | **Best source candidate — conditional** |
| Direct Caddy static artifact | Prior self-host research: Apache-2.0 Caddy candidate; same static artifact can be served | Best Stage-0 hosting target once OD-06/07 gates pass | Mini/DNS/TLS/rollback unproven | **Best hosting candidate — conditional** |
| GitHub Pages status quo | Existing public static source-hosting posture | Lowest change cost, but not the proposed owner-operated target | Does not prove private deployment/rollback control | **Keep as source/status quo, not selected production target** |
| Coolify route | Prior research: optional Compose deployment adapter | Same artifact is possible, but adds a platform layer before it is needed | Live health/restore evidence absent | **Defer** |

**Decision:** do not rebuild a portfolio site from scratch. Once OD-01 through OD-07 close, inspect and change `AbleVarghese.github.io` in its own worktree, generate one static artifact, and prove it behind Caddy. No code copying is justified now.

## Reuse comparison beyond the source site

| Candidate | What it demonstrably offers | Why it is not a direct integration now | Reconsideration gate |
|---|---|---|---|
| `ops-dashboard` | MIT JavaScript dashboard; project Git/test/agent monitoring, localhost server, tests and Compose files visible at root | Stage 0 needs release proof, not a second web runtime; functionality was not executed for this project | A real operator needs live release/agent telemetry; run isolated read-only compatibility and failure probes first |
| `relay` | Partner/creator outreach, attribution, commissions, payouts; JavaScript/Compose shape visible | Far beyond one diagnostic offer; creates data, outreach, payment, and license obligations | Paid partner programme with approved consent, privacy, payout, and license review |
| `solveright.ai` | Public decision-intelligence face | Its decision method is already used as documented analysis; root currently exposes README only | A product integration need, not a planning-method need |
| `lawyerserved.com`, `keralora.com`, `licentric.com` | Public-face repositories for distinct vertical products | Different regulated/domain boundaries; root-tree evidence is README-only or unavailable; copying brand/site code would be unproved and misleading | Independently inspect the authoritative source repository and establish a shared component need |

## Best external contenders already screened

| Need | Winner now | Strong alternative | Why the alternative does not win now |
|---|---|---|---|
| Static edge | Caddy | Coolify | Caddy is the smaller direct static seam; Coolify is only an optional deployment adapter |
| Future identity | No identity at Stage 0 | Better Auth / Supabase Auth | A protected workflow has not been named; adding auth is speculative |
| Future private UI | No admin UI at Stage 0 | Refine / React-admin | The matrix is fragile and no private workflow/data model exists |
| Operations visibility | Existing validation receipts | ops-dashboard | Telemetry does not replace static artifact, rollback, or host proof |

## Evidence limits and next tests

Repository descriptions, root trees, stars, and public metadata are **not** compatibility, security, maintenance, license, or operational proof. Before any conditional item becomes integrated: inspect its real source/manifest/license at the intended revision, run a synthetic/isolated positive and negative control, record version/owner/rollback/egress, and update `docs/INTEGRATION-REGISTER.md`.
