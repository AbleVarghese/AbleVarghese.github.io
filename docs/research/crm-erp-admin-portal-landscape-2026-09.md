# Lightweight CRM/ERP admin-portal landscape — 2026-09

- **Status:** collection in progress.
- **Decision purpose:** compare a lightweight, self-hostable customer-relationship-management (CRM), enterprise-resource-planning (ERP), or internal-admin foundation for the proposed professional/agency platform; do not adopt, install, execute, or contact vendors.

## Research overlap

**INDEX checked; overlaps** [`consulting-growth-plan-research-2026-09.md`](consulting-growth-plan-research-2026-09.md) §H3/H5 and [`consulting-growth-source-register-2026-09.md`](consulting-growth-source-register-2026-09.md) on intake, client onboarding, security, and deferred CRM complexity. **Extension only:** this study evaluates concrete public GitHub candidates and the owner’s public GitHub evidence; it does not re-derive general funnel advice.

## Collection admission record

| Field | Boundary |
|---|---|
| Authority | Owner explicitly requested public GitHub candidate search, comparison of the owner’s GitHub profile/projects, and incorporation of LinkedIn/GitHub/resume context on 2026-09-22. |
| Sources | Public GitHub REST API through the authenticated `gh` CLI: `users/AbleVarghese`, public owner repositories, and public repository search. GitHub social metadata identifies the exact LinkedIn URL; a public profile fetch is **BLOCKED** because LinkedIn’s 2026-09 `robots.txt` disallows generic agents for that path. |
| Purpose | Select or reject a lightweight CRM/ERP/admin foundation; build an evidence-backed professional capability map. |
| Allowed fields | Repository identity, description, public topics, language, stars/forks/watchers, timestamps, licence metadata/text, release/issue indicators, README architecture/operations facts, and public profile/project claims. |
| Prohibited fields | Private repositories, credentials, personal contacts, follower lists, employment data not published by the owner, message/contact actions, source-code execution, installation, and vendor sign-up. |
| Destination | This research file plus bounded JSON/TSV metadata under `docs/research/crm-erp-admin-portal-evidence-2026-09/`. |
| Retrieval limits | One owner-profile request; ≤100 public owner repositories; ≤7 GitHub-search queries × ≤50 results; detailed inspection of ≤15 finalists; 90 seconds per batch; no retries after authentication/rate-limit/access-control failure. |
| Success test | A candidate comparison has enough primary GitHub evidence to classify: fit, licence, maintenance signal, deployment/data model, likely operating burden, and explicit unknowns. |
| Stop conditions | Missing/ambiguous owner identity, rate limit, inaccessible/private source, licence ambiguity, unexpected sensitive data, or a candidate requiring unbounded code review. |

## Current local evidence

| Source | Finding | Evidence grade |
|---|---|---|
| Website blueprint | Proposes shared CRM, calendar, evidence, analytics, Recruit/Consult/Build journeys, and a specialist consulting brand. | `[reported]` local source extract |
| Evidence registry | Proposes a canonical proof graph and records GitHub history as a dynamic source when accessible. | `[reported]` local source extract |
| Current growth plan | Requires a minimal canonical opportunity record now; defers full CRM/portal complexity until the data model and demand prove stable. | `[verified]` current strategy document |
| User statement | GitHub and LinkedIn are the current professional sources; résumé contains latest Interac position details; the owner has ten years of side trading/investing experience. | `[reported]` 2026-09-22 message |

## Non-negotiable evaluation gates

1. **No adoption from repository existence alone.** A candidate must pass licence, maintenance, operational, data-control, security, and real-workflow checks.
2. **Native-first.** A small canonical opportunity/client ledger plus existing approved scheduling/shared-workspace tools remains the baseline. A full system must beat that baseline on a real repeated workflow.
3. **Data minimization.** The initial site must not collect or retain more prospect/client data merely because a CRM permits it.
4. **Finance separation.** Personal-finance, investment, and trading coaching are not CRM fields or service flows until their jurisdiction/scope/legal boundaries are independently resolved.
5. **Profile truth.** GitHub and LinkedIn evidence may update project/current-work claims; résumé remains the named source for latest Interac-role detail until independently reconciled.

## Candidate evaluation rubric

| Criterion | What proves it |
|---|---|
| Lightweight fit | Can support opportunities, contacts, engagements, consent, tasks, and an internal admin workflow without a large ERP rollout. |
| Licence/ownership | Repository licence is read directly; any dual/open-core restriction is named. |
| Maintenance | Recent public activity, releases/issues, contributors, and clear operating documentation—not stars alone. |
| Data/security | Role/access model, auditability, exports, backups, deletion/retention, deployment, and authentication surface are documented. |
| Integration | Can connect to a form, calendar, email, shared workspace, and evidence ledger without making any external service the new source of truth. |
| Operating burden | Runtime components, upgrades, backups, administration, and support fit a lean founder-stage operation. |
| Project fit | Supports the staged professional/career, B2B agency, expert-session, and private-client flows without forcing financial-advice workflows into the same model. |

## Initial hypotheses to test

- A full ERP is likely disproportionate for the first paid diagnostic and career/portfolio flows.
- A dedicated CRM may be justified only after repeatable opportunity/engagement workflow evidence exists.
- A self-hosted internal-tool platform may win if it preserves a small owner-controlled data model and replaces several point tools.
- The owner’s public GitHub projects may offer reusable evidence or a partial admin foundation, but must be independently executed before dependence.

## Unknowns that block a final selection

- Exact website stack, hosting, database, calendar, email, accounting, and identity choices.
- Whether the system must support invoicing/accounting, client support, project delivery, or only opportunity/onboarding records.
- Latest résumé. An owner-provided LinkedIn PDF is now available and reconciled as a bounded source; the exact public URL remains unavailable to a generic agent under the observed `robots.txt` policy.
- Jurisdiction and lawful boundary for personal-finance/investment/trading education or advice.

## Collection checkpoint 1 — public GitHub metadata

- **GitHub Directory check:** a focused Directory query returned Donorbox only, which is unrelated to a self-hosted CRM/ERP/admin foundation. It is rejected; no provider was engaged.
- **Owner public profile:** direct GitHub API returned `AbleVarghese` and the public profile URL `https://github.com/AbleVarghese`. The profile reports **291** public repositories and identifies Licentric, LawyerServed, SolveRight, ArgusTest, ShellJolt, and Keralora. Profile text is public self-description, not independent proof of every metric.
- **Owner repository sample:** the bounded current-repository response contains 100 public repositories. Early relevance candidates include `erpnext-Abled`, `macro-Abled`, `homepage-Abled`, `ops-dashboard`, `qlib-Abled`, and the portfolio/career repositories. Their presence is not proof that they are maintained, secure, legally reusable, or suitable.
- **External GitHub scan:** seven bounded repository searches returned 218 unique metadata candidates. Search results contain irrelevant “awesome” lists and tutorials, so no search-rank or star count is treated as a recommendation.
- **LinkedIn:** exact public URL is `https://www.linkedin.com/in/ablevt/`; a bounded `robots.txt` check returned HTTP 200 and disallowed generic-agent access to that path. No profile request was made. The owner-provided `sources/2026-09/private/linkedin-profile-owner-provided-2026-09.pdf` is now the permitted local source; see `professional-evidence-reconciliation-2026-09.md`.
- **Trading/investing:** the owner-provided PDF states a 2020–2023 securities/options-trader role. It remains an owner-provided source claim, not a publishable financial-services credential, performance claim, or permission to provide advice.

## Collection checkpoint 2 — candidates, licences, and public project evidence

### Candidate landscape

The public GitHub scan produced **218 unique metadata candidates**. Direct repository, licence-file, README, release, community-health, and workflow checks narrowed the active implementation field; stars and search rank were never used as selection proof.

| Family | Candidate | Direct-source finding | Current disposition |
|---|---|---|---|
| TypeScript admin framework | `refinedev/refine` | MIT; React headless framework for admin panels, dashboards, internal tools, auth/access/routing; 13 public GitHub workflows observed. | Active spike finalist |
| TypeScript admin framework | `marmelab/react-admin` | MIT; React/TypeScript REST/GraphQL admin framework with roles, permissions, CRM example, and 7 public workflows observed. | Active spike finalist |
| Node embedded admin | `SoftwareBrothers/adminjs` | MIT; automatic Node admin interface with custom actions; one public workflow observed. | Active comparison only; matrix-dominated by the two React candidates |
| Self-hosted app builder | `appsmithorg/appsmith` | Apache-2.0; Docker/Kubernetes deployment documented; distinct large runtime. | Deferred fallback if a separate internal-tool service earns its operating cost |
| Data/app platform | `baserow/baserow` | MIT applies to Open Source Edition outside premium/enterprise restrictions; Docker/PostgreSQL documented. | Deferred: distinct Django/Vue/PostgreSQL platform risks a second source of truth |
| Low-code business platform | `cortezaproject/corteza` | Apache-2.0; CRM/process/RBAC/privacy/automation scope documented. | Reference only: broad Go platform is disproportionate before a repeated workflow proves it |
| Conventional CRM | `krayin/laravel-crm` | MIT; Laravel/Vue/MySQL/MariaDB and 3 GB+ RAM requirements documented. | Reference only: separate PHP/MySQL runtime and CRM model do not match the current canonical-data plan |
| Full ERP | `frappe/erpnext` / owner fork `erpnext-Abled` | GPL-3.0; upstream describes accounting, inventory, manufacturing, assets, and projects. Owner repo is a fork, not independent CRM evidence. | Excluded by default licence gate and scope mismatch |

### Licence gate outcomes

| Outcome | Candidates | Reason |
|---|---|---|
| Permissive candidate | Refine, React-admin, AdminJS, Appsmith, Corteza, Krayin, Baserow OSE | Direct MIT/Apache-2.0 source, or Baserow OSE’s explicit MIT scope. Still needs operational and security validation. |
| Isolated-tool only | Odoo | Direct source says LGPLv3; policy permits only an unmodified standalone process. |
| Default exclusion | ToolJet, Twenty, EspoCRM, SuiteCRM, Dolibarr, ERPNext, Budibase, Invoice Ninja, NocoBase | Direct source shows AGPL/GPL, ELv2, GPL/BSL package rules, or a custom restrictive licence. None is adopted by this research. |

### Owner GitHub/project evidence

| Public source | What it supports | Limit |
|---|---|---|
| `AbleVarghese` profile README | Current self-described platform portfolio, current Interac-member role statement, product links, and public LinkedIn URL. | Public self-description; individual metrics remain unverified until source history is independently checked. |
| Public Licentric/LawyerServed/SolveRight/ArgusTest/ShellJolt/Keralora README files | A current public product narrative covering Next.js/TypeScript, Supabase/RLS, payment, decision, security, and operational themes. | Each is a public product-facing source; private code and reported counts were not inspected. |
| `ops-dashboard` README | An MIT, Node-based, project-agnostic read-only observability dashboard and its documented security boundary. | Potential observability pattern only; it is not a CRM/ERP/admin-data foundation and has not been independently executed in this study. |
| `macro-Abled`, `career-ops-Abled`, `qlib-Abled`, `erpnext-Abled` | These are direct GitHub forks with named upstreams. | A fork is not proof of owner-authored functionality or a safe reuse candidate. |

### LinkedIn and résumé status

- Public GitHub social-account metadata resolves the owner’s exact LinkedIn URL as `https://www.linkedin.com/in/ablevt/`.
- A bounded `robots.txt` check disallows generic-agent access to the exact profile path. No profile page, substitute scraping, or installation was attempted. An owner-provided `sources/2026-09/private/linkedin-profile-owner-provided-2026-09.pdf` is now available for a minimized local claim map; it does not independently verify the profile’s assertions.
- The latest résumé file is still absent from this repository. The owner-provided PDF has an Interac-role statement, but the résumé remains the named latest-position source until its exact path is supplied and reconciled.

## Profile-source hierarchy by claim type

| Claim type | Preferred source | Rule |
|---|---|---|
| Current public project/work evidence | GitHub repository, release, commit, issue, and deployed-project evidence | Read the underlying repository state; profile README alone is not enough. |
| Public career identity and current narrative | Owner-provided LinkedIn PDF plus source-cleared résumé | Reconcile conflict rather than choosing whichever wording is stronger. |
| Latest Interac position facts | Current résumé plus source-cleared employment/professional record | The résumé remains the named latest-position source until a direct reconciliation occurs. |
| Trading/investing experience | Owner-approved source records plus legally safe public wording | Experience is not automatically permission to provide financial advice. |
| Derived site/proposal/AI claims | Canonical claim record linked to the above sources | A public statement inherits the weakest unresolved source. |

## Next action gates

1. **Source reconciliation:** reconcile the owner-provided LinkedIn PDF with the GitHub project evidence and supply the still-missing latest résumé through an approved, non-restricted path. An extractor cannot override the observed `robots.txt` block.
2. **Website-repository boundary:** create/identify the actual website repository and confirm its stack before selecting an admin dependency. This document does not authorize work in another repository.
3. **Control-first spike:** implement the ADR-002 synthetic-data schema and negative controls before installing Refine or React-admin in a production path.
4. **Framework selection:** run the same guarded data-provider test against Refine and React-admin; select only the framework that passes every positive and negative control.
5. **Finance boundary:** keep personal-finance/investment/trading data and workflows absent until dedicated legal, product, security, and retention research is accepted.
