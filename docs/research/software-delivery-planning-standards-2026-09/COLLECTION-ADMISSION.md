# Collection admission — software-delivery planning standards · 2026-09

- **Purpose:** identify missing planning, governance, verification, release, operational, and security artifacts for this Stage 0/Stage 1 software effort.
- **Question:** which documented plans are needed to make the existing architecture, design, implementation, verification, CI/CD, and deployment plans operationally complete without inventing a heavyweight process?
- **Authority:** this is a planning-completeness study, not a claim that one framework is universally “gold standard.” Requirements remain proportional to the product, risk, and current Stage 0 static scope.

## Overlap check

`docs/research/INDEX.md` was checked before collection. It has earlier primary-source records naming NIST SSDF (`S09`) and OWASP ASVS (`S01`), plus security/accessibility research, but no dedicated software-delivery planning study or operative SSDF/ASVS planning crosswalk. Existing architecture/ADRs are inputs; this study extends rather than re-derives them.

## Approved primary sources

| ID | Source | Why it is in scope | Planned evidence use |
|---|---|---|---|
| SD01 | NIST SP 800-218 SSDF | Secure software-development practice baseline | Planning/governance/implementation/verification/release artifact families |
| SD02 | NIST SP 800-61r3 | Incident-response lifecycle integration | Incident, recovery, and exercise planning |
| SD03 | OWASP SAMM | Software-assurance maturity model | Coverage-gap taxonomy and incremental maturity sequencing |
| SD04 | OWASP ASVS | Application-security verification requirements | Security-verification plan boundary, later Stage 1 |
| SD05 | SLSA specification | Build provenance and supply-chain controls | CI/CD, artifact, and release evidence |
| SD06 | CISA Secure by Design | Secure-by-design operational expectations | Ownership, vulnerability response, and customer-facing security posture |

## Boundaries

- Fetch official primary-source pages only; no vendor marketing or Wikipedia as verification sources.
- Preserve URL, access date, HTTP result, SHA-256, and quoted operative wording. A blocked or unavailable source is recorded as blocked, not reconstructed.
- Do not collect project source code, credentials, private evidence, customer data, or Mini data.
- The output will map source-backed artifact families to the current plan suite, distinguish Stage 0 from Stage 1, and mark owner/Mini-dependent work as blocked.
