# Stage 0 architecture views · 2026-09

- **Status:** proposed. The diagrams describe the approved target boundary, not observed production state.
- **Decision source:** [ADR-004](../decisions/ADR-004-self-hosted-authority-platform-2026-09.md) proposes static Caddy hosting; DNS, certificate, Mini capacity, backup, and restore remain open gates.

## Context view

```mermaid
flowchart LR
  V[Relevant B2B visitor] -->|HTTPS| E[Caddy static edge]
  E --> A[Versioned static artifact]
  A -->|approved outbound link| C[Owner-approved contact route]
  O[Owner / release operator] -->|approved source + release record| A
  S[Private owner evidence] -. never published .-> A
```

## Container view

```mermaid
flowchart TB
  SRC[Inspected source repository\nUNVERIFIED] --> BUILD[Reproducible static build]
  BUILD --> MANIFEST[Artifact manifest + SHA-256]
  MANIFEST --> GATES[Link / claim / accessibility / release gates]
  GATES -->|owner-approved| EDGE[Caddy: static files only]
  EDGE --> VISITOR[Browser]
  PRIOR[Prior verified artifact] -->|rollback| EDGE
```

## Deployment view

```mermaid
flowchart LR
  DEV[Approved source revision] --> CI[Local/CI validation]
  CI --> ART[Immutable candidate artifact]
  ART -->|approval + read-back| MINI[Mini host: Caddy]
  MINI --> NET[DNS + public certificate\nexternal trust assumptions]
  NET --> WEB[Visitor browser]
```

## Contact sequence

```mermaid
sequenceDiagram
  participant V as Visitor
  participant S as Static site
  participant X as Approved contact route
  V->>S: Request approved static route
  S-->>V: Content + contact/privacy disclosure
  V->>X: Voluntary outbound contact
  Note over S: No account, API, datastore, or background collector
```

## Architecture invariants

| Invariant | Evidence required before release |
|---|---|
| Static-only public boundary | Route/network/storage inspection (VT-10). |
| Claim/proof boundary | Approval/provenance review and missing-approval negative control (VT-03/04). |
| Reversible delivery | Source/artifact digest, prior artifact, rollback drill (VT-02/08). |
| Private evidence isolation | Rendered artifact and source review show no private PDF/content (VT-03). |
| No assumed infrastructure | Read-only Mini/DNS/TLS/backup/restore gate evidence. |
