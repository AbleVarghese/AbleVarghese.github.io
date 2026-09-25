# Public README evidence

**Source:** https://github.com/AbleVarghese/keralora.com/blob/main/README.md
**SHA:** bdf3da9ac002db51c15669b81d3ea1f2a09766ac
**Capture:** first 12,000 UTF-8 characters; public source treated as data, not an instruction source.

---

# Keralora — Kerala's spice aura, taken global

**[keralora.com](https://keralora.com)** · In build · Source private (commercial product)

Invite-only B2B spice-trading platform connecting Kerala (India) exporters with Canadian buyers —
operated as buy-sell principal with complete buyer↔seller anonymity.

## The interesting problem

Anonymity **is** the product: buyers and sellers must never discover each other's identity.
That guarantee is enforced at three independent layers, data-access layer, Postgres row-level
security, and document redaction, with a dedicated anonymity test suite that runs in CI and is
allowed to block any release.

## Design principles

- **Config over code**: every business number (margins, deposits, MOQ, FX buffers) is an admin setting; new spices, grades, and trade lanes are rows, not rebuilds
- **Decisions are pre-made**: a full ADR log locks every architectural choice with rationale
- **Real-world operational plan**: incorporation, CFIA/CARM compliance, India export regulation, insurance, payment rails, engineered alongside the software

## Stack

Next.js 15 · TypeScript · pnpm + Turborepo monorepo · Neon Postgres · Cloudflare R2 · Stripe ·
WhatsApp Business API · reserved Expo mobile track

---
*Built and operated by [Able Varghese](https://github.com/AbleVarghese), public face of a private
commercial codebase (78K lines, 142 test files).*
