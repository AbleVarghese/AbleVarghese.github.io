# Collection admission — internal portfolio reuse screen · 2026-09

- **Authority:** owner request in this session: inspect `https://github.com/AbleVarghese?tab=repositories` to find reusable owner projects/tools for Portfolio-consult; compare viable candidates against best alternatives; record every adopted integration.
- **Purpose:** identify an already-owned, compatible source repository or reusable pattern for the proposed public authority site and later protected operations. Prevent rebuilding a capability already owned.
- **OVERLAP-CHECK:** `docs/research/INDEX.md` checked. This extends the prior bounded owner-site, foundation, and admin-pattern screens; it does not re-collect external CRM/identity candidates or re-adopt a package.

## Bounded source and data contract

| Field | Limit |
|---|---|
| Source | GitHub public `users/AbleVarghese/repos` API plus public metadata and non-recursive root-tree endpoints for the seven shortlisted owner repositories; `visibility=public`, `type=owner` |
| Method | Authenticated `gh api` only to GitHub, a sanctioned owner-account destination/source |
| Population | At most 300 public repository metadata rows / three 100-item pages, plus 18 named public-repository endpoint responses (seven reuse candidates plus four approved-proof URL candidates, with overlap retained as provenance) |
| Allowed fields | Repository name, URL, description, topics, default branch, archive/fork flag, language, license metadata, timestamps, counts, visibility |
| Prohibited | Private repository metadata, source cloning, code execution, credentials, issues/PRs, contributor/contact data, package install, deployment, GitHub write |
| Destination | This local research directory, raw response plus derived candidate register; no production store |
| Stop conditions | Pagination exceeds 300 rows; auth/authorization failure; private data appears; source scope changes; unexpected sensitive data; rate-limit failure |
| Success | Bounded provenance receipt; source-backed shortlist; explicit `reuse`, `reference-only`, `defer`, or `exclude` disposition for each candidate |
| Retention | Versioned local research evidence; generated research index and artifact register describe it; no raw private data retained |

## Decision boundary

This authorizes read-only discovery only. Reuse, copying, integration, package adoption, source edits, website replacement, and deployment require an owner-approved candidate decision plus repository-specific compatibility, security, license, and isolation evidence.
