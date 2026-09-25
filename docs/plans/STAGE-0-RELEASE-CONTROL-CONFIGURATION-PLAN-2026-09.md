# Stage 0 release-control plan — configuration, dependencies, artifacts, and change · 2026-09

- **Status:** proposed. It selects no CI provider, registry, package, secret, or deployment console.
- **Goal:** ensure the static-site delivery path has one identifiable source revision, configuration boundary, artifact, approval, release receipt, and rollback target.
- **Inputs:** [CI/CD plan](STAGE-0-CI-CD-PLAN-2026-09.md) · [deployment/rollback plan](STAGE-0-DEPLOYMENT-ROLLBACK-PLAN-2026-09.md) · [requirements/governance plan](STAGE-0-PRODUCT-REQUIREMENTS-GOVERNANCE-PLAN-2026-09.md).

## Configuration contract

| Class | Stage 0 rule | Release evidence |
|---|---|---|
| Source content/assets | Versioned in the actual static-site repository | Source revision and review scope |
| Build settings | Versioned and reproducible; no per-machine hidden default | Exact build/validation command and output path |
| Edge configuration | Versioned declaration, reviewed separately from content | Configuration revision, host, static root, and pre/post check |
| DNS/certificate parameters | Never embedded in source; named owner and approved external-trust scope | OD-06 closure and host/certificate receipt |
| Credentials/tokens | Minimum privilege, non-source storage, never in logs/artifacts | Credential owner/scope/rotation record; secret scan evidence |
| Runtime environment | Stage 0 should have no application runtime configuration | Any runtime/data need is a Stage 1 trigger |

## Dependency and supply-chain control

| Event | Required control |
|---|---|
| Existing site has no build dependency | Record that fact from source inspection; do not add one for ceremony |
| A build/deploy dependency is proposed | Verify native alternative first; record license, version, integrity source, maintenance/security evidence, and rollback/removal path |
| Container/image is proposed | Pin/identify exact image digest, retain SBOM/provenance if available, and scan/verify before deployment; no unpinned tag is a release candidate |
| Vulnerability or upstream release appears | Assess scope/impact, patch or formally defer with expiry, and retain the decision receipt |
| Tool/runner cannot be verified | Mark `UNKNOWN`; do not count a skipped scan/build as pass |

## Release record

Every candidate needs one immutable record:

```text
source revision → requirement IDs → approved-copy receipt → validation receipts
→ artifact manifest + SHA-256 → edge/configuration revision → approver
→ deployment time → post-release host/TLS/digest checks → rollback target
```

| Change class | Minimum approval | Rollback expectation |
|---|---|---|
| Copy/layout with no data/edge change | Owner-approved wording + tested source revision | Re-deploy prior static artifact |
| Form/data/analytics/cookie change | Owner + trust-plan review | Disable surface and restore prior artifact/configuration |
| Edge/DNS/certificate/host change | Owner + estate operator after preflight | Restore prior configuration/host mapping with verification |
| Dependency/build/runtime change | Owner + dependency/security review | Pinned prior version/digest and tested source/build rollback |
| Emergency correction | Authorized owner/operator; preserve fault evidence | Immediate reversible correction followed by normal review |

## Change-control rules

1. One release candidate contains one explicit intended scope. Unrelated docs/source changes do not ride along.
2. Every change carries a requirement ID, a targeted verification result, and a named rollback target before release approval.
3. A deployment console may execute a source-controlled declaration but cannot be the only record of configuration or release history.
4. Failed candidates, logs, and manifests are preserved with attempt/time identity; a later green does not erase a prior failure.
5. Secrets, private evidence, and owner-provided profile material are excluded from release artifacts and CI inputs.

**Exit gate:** release control is active only after an actual repository/runner/edge path demonstrates a clean candidate, a planted failure blocks it, and a rollback returns the previous verified artifact.
