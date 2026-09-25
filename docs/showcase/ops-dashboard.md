# Ops Dashboard

A live, project-agnostic SDLC and agent-activity monitor for AI coding workflows.

## What it does

- Watches multiple projects' transcripts, report ledgers, and git state simultaneously
- Pushes every change to the browser over Server-Sent Events (typically under one second from disk write to UI)
- Provides a unified project-tagged activity feed, per-project lanes, a plain-English narrative summary, and live stall detection
- Runs with zero third-party dependencies on Node.js built-ins only; no build step

## Why it exists

Operators running several AI coding agents across many repositories need one place to see what is happening right now — which agent is working, what changed, and where work has stalled — without switching between projects.

## Technical highlights

- **Zero-dependency architecture:** Node.js built-ins only
- **Real-time transport:** Server-Sent Events for sub-second UI updates
- **Multi-project:** every enabled project watched at once, live-configurable with no restart

## Status

Private source repository. This showcase describes the project in public-safe terms.

---

*Built and maintained by [Able Varghese](https://github.com/AbleVarghese).*

<!-- owner-confirm: this showcase was previously an MIT open-source project with a public README; owner directive 2026-09-25 made the source private. Confirm whether to state "previously open source" or omit. -->
