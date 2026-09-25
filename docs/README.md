# Documentation artifact map

This directory is the durable record for the Portfolio-consult work. The generated [`ARTIFACT-REGISTER.md`](ARTIFACT-REGISTER.md) lists every documentation file and every row in the source manifest with lifecycle, version token, size, and SHA-256 prefix.

| Location | Holds | Lifecycle |
|---|---|---|
| `architecture/` | Cross-cutting technical and operational plans and Stage 0 views | Active proposed architecture |
| `requirements/` | BRD, PRD, SRD, and BRD→PRD→SRD→verification traceability | Proposed requirements; machine-checked baseline |
| `design/` | Stage 0 technical/content/release design | Proposed design; no implementation authority |
| `integrations/` | Runtime integration catalog and boundary contracts | Stage 0 has zero active runtime integrations |
| `plans/` | Stage 0 design, implementation, verification, CI/CD, and deployment/rollback plans | Proposed execution plans; each has explicit entry gates |
| `decisions/` | ADRs, matrices, validation receipts, and style receipts | Active decision record |
| `decisions/_archive/` | Superseded matrix inputs and failed/pre-amendment receipts | Preserved history; never active evidence |
| `research/` | Research syntheses, source registers, extraction contracts, evidence, and generated research index | Active evidence corpus |
| `research/_archive/` | Earlier retrieval/analysis attempts retained for provenance | Preserved history |
| `strategy/` | Commercial execution plan | Active proposed strategy |
| `ledgers/` | Dated phase facts, unresolved items, decisions, and checkpoints | Append-only task state |
| `OPEN-DECISIONS-REGISTER.md` | Owner decisions and external dependencies that block the plan | Active owner-decision queue |
| `INTEGRATION-REGISTER.md` | Every candidate/actual cross-repository tool, role, state, evidence, and admission gate | Active integration-discovery register |

## Naming and versioning contract

- Active records use a stable subject plus `YYYY-MM`; ADRs also use a stable ordinal (`ADR-001`, `ADR-002`, and so on).
- A replaced artifact moves to `_archive/YYYY-MM/<topic>/`; it keeps its original filename and remains discoverable through the artifact register.
- Raw inputs live under [`../sources/`](../sources/README.md). The source manifest records original path, canonical path, SHA-256, lifecycle, and source-set version.
- `sources/2026-09/private/` contains owner-provided personal inputs. Its raw bytes stay Git-ignored; the manifest is the versioned provenance record until the owner explicitly approves Git retention.
- Captured upstream README/security-policy excerpts are evidence data, not locally authored navigation. Their original source URL/header is authoritative; relative upstream links are intentionally excluded from local-link validation.
- `ARTIFACT-REGISTER.md` is generated, not hand-maintained. Regenerate it after any documentation or source-manifest change:

```bash
python3 docs/build-artifact-register.py --sources-manifest sources/2026-09/MANIFEST.tsv
python3 docs/research/build-index.py
python3 docs/validate-documentation-baseline.py --root .
```

A local Git commit is still required to create repository history. This map does not imply a commit, push, or publication.
