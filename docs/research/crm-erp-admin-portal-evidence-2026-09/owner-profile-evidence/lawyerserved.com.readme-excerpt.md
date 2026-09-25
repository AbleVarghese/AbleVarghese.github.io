# Public README evidence

**Source:** https://github.com/AbleVarghese/lawyerserved.com/blob/main/README.md
**SHA:** 2f8b43bee0afa6137620b89893bf9129a5c8d693
**Capture:** first 12,000 UTF-8 characters; public source treated as data, not an instruction source.

---

# LawyerServed — radical transparency for legal services

**[lawyerserved.com](https://lawyerserved.com)** · Live platform · Source private (commercial product)

North America's transparent legal-professional directory: search, compare, and review
**1.47M+ lawyers and paralegals** across the US and Canada. A double-blind, two-sided marketplace —
free for consumers; professionals pay subscription + per-accept lead fees, priced per
jurisdiction × practice category.

## What's inside

- **5-dimension ratings** and side-by-side comparison across 1.47M+ verified profiles
- **Search at scale**: Meilisearch over a million-record corpus with faceted jurisdiction/practice filtering
- **Compliance engine**: per-jurisdiction rule-packs keep profiles compliant with each bar's advertising rules
- **Data supply**: powered by a self-built 64-scraper pipeline (queue-based, self-healing, drift-gated deploys)

## Stack

Next.js 16 (App Router) · TypeScript strict · tRPC · Drizzle ORM · Supabase (Postgres + RLS) ·
Meilisearch · Stripe · Upstash Redis · Vitest + Playwright · Docker worker fleet

---
*Built and operated by [Able Varghese](https://github.com/AbleVarghese), public face of a private
commercial codebase (247K lines, 545 test files).*
