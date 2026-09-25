# Stage 0 delivery-plan suite · 2026-09

- **Status:** proposed planning artifacts. They authorize no source edit, dependency installation, DNS change, deployment, or service account.
- **Scope:** the existing static professional-site source identified in the foundation architecture. This planning repository remains the decision/evidence home, not the application source.

| Plan | Owns | Entry gate |
|---|---|---|
| [Design](STAGE-0-DESIGN-PLAN-2026-09.md) | Public-safe page structure and approval boundary | OD-01 through OD-05 |
| [Implementation](STAGE-0-IMPLEMENTATION-PLAN-2026-09.md) | Smallest static-source change sequence | Actual site worktree/branch inspected |
| [Verification](STAGE-0-VERIFICATION-PLAN-2026-09.md) | TDD, negative controls, accessibility, and release evidence | Actual source structure measured |
| [CI/CD](STAGE-0-CI-CD-PLAN-2026-09.md) | Source-controlled quality and release pipeline | Mini/runner capability measured |
| [Deployment and rollback](STAGE-0-DEPLOYMENT-ROLLBACK-PLAN-2026-09.md) | Direct Compose/Caddy release and reversal | OD-06, OD-07, and all operational proofs |
| [Product requirements and governance](STAGE-0-PRODUCT-REQUIREMENTS-GOVERNANCE-PLAN-2026-09.md) | Decision rights, requirements, traceability, milestones, and scope/risk change control | Actual source/worktree discovery |
| [Trust](STAGE-0-TRUST-PRIVACY-SECURITY-ACCESSIBILITY-PLAN-2026-09.md) | Privacy, disclosure, threat, security, accessibility, and legal-discovery boundary | Relevant owner disclosure/data decisions |
| [Release control](STAGE-0-RELEASE-CONTROL-CONFIGURATION-PLAN-2026-09.md) | Configuration, secrets, dependencies, artifact, and change records | Actual source/runner/edge inventory |
| [Operations and lifecycle](STAGE-0-OPERATIONS-MEASUREMENT-LIFECYCLE-PLAN-2026-09.md) | Health, recovery, maintenance, content freshness, measurement, and retirement | Mini health/recovery evidence |

**Coverage audit:** [software-delivery completeness audit](../research/software-delivery-planning-standards-2026-09/SOFTWARE-DELIVERY-COMPLETENESS-AUDIT-2026-09.md) identifies these additions, preserves the blocked official-source collection, and distinguishes Stage 0 from Stage 1.

**Authority order:** [open decisions](https://github.com/AbleVarghese/Consult-Able/blob/Portfolio-consult/docs/OPEN-DECISIONS-REGISTER.md) → [foundation architecture](../architecture/FOUNDATION-ARCHITECTURE-PLAN-2026-09.md) → [ADR-004](../decisions/ADR-004-self-hosted-authority-platform-2026-09.md) → these execution plans.
