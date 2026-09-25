# Public README evidence

**Source:** https://github.com/AbleVarghese/licentric.com/blob/main/README.md
**SHA:** f8e4403ff1d20a0083d5cd7594b69b799f6f7cdd
**Capture:** first 12,000 UTF-8 characters; public source treated as data, not an instruction source.

---

# Licentric — licensing built for the AI era

**[licentric.com](https://licentric.com)** · Live platform · Source private (commercial product)

The monetization platform for the AI era, from license keys to AI-agent tokens. Licensing,
entitlements, metering, and billing in one API. **Five lines of code to first validation.**

## Why it exists

Every incumbent makes the same mistakes: hours of integration time, API-only admin, hundreds of
lines of Stripe webhook glue, seven-entity data models for what should be Product → License.
Licentric's answers:

- **Zero billing code**: connect Stripe, map a product to a license policy in the dashboard; purchase → license → key, no webhook handler written
- **Offline-first**: Ed25519-signed license files with configurable TTL; air-gapped deployments just work
- **3 clicks to first license**: template-driven setup for desktop apps, CLI tools, SaaS, trials
- **Container-aware machine identity**: logical identifiers, not hardware UUIDs that break in Docker/K8s

## Stack & surface

TypeScript · Next.js · Stripe · Ed25519 cryptography · REST API (OpenAPI 3.1) ·
**Python SDK on [PyPI](https://pypi.org/project/licentric/)** (`pip install licentric`) · TS SDK pending

---
*Built and operated by [Able Varghese](https://github.com/AbleVarghese), this repo is the public
face of a private commercial codebase (329K lines, 836 test files).*
