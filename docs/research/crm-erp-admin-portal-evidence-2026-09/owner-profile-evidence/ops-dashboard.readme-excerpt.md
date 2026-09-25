# Public README evidence

**Source:** https://github.com/AbleVarghese/ops-dashboard/blob/main/README.md
**SHA:** 0673591c393645c455779001079461cf7b318928
**Capture:** first 12,000 UTF-8 characters; public source treated as data, not an instruction source.

---

# Ops Dashboard v3

A live, **project-agnostic**, **multi-project** SDLC / agent-activity monitor for Claude Code repos.
Zero npm dependencies, no build step, Node ≥22 built-ins only. Watches N projects' `~/.claude/projects/*`
transcripts, `reports/*.md` ledgers, and git state **simultaneously**, and pushes every change to the
browser over Server-Sent Events (typically <1s from disk write to UI).

> Built by [Able Varghese](https://github.com/AbleVarghese) as part of the agentic engineering system
> behind a [10-platform portfolio](https://github.com/AbleVarghese). Free and open source (MIT).
> **If it saves you time, a ⭐ helps other agent-fleet operators find it.**

v3's headline change from v2: there is no longer a single "active" project you switch between —
every enabled project is watched at once, with a unified project-tagged feed, per-project lanes, a
plain-English narrative strip summarizing all of them, and live stall detection.

---

## Repository index

| Repo | Purpose |
|---|---|
| **[ops-dashboard](https://github.com/AbleVarghese/ops-dashboard)** | This project — a live SDLC / agent-activity monitor for Claude Code repos (open source, MIT) |
| claude-config | The author's global Claude Code config it grew out of (private) |

Relocated 2026-07-24 from `~/.claude/lib/ops-dashboard` to its own standalone project so the config
backup stays pure config.

---

## Install

Nothing to install — it's a self-contained folder. Just have Node ≥22.

```bash
node --version   # must be >=22
```

## Run

```bash
cd ~/ops-dashboard
node server.mjs [repoPath]      # optional: adds + enables this repo on first boot if not already configured
```

Then open **http://127.0.0.1:4650**. Add, rename, enable/disable, or remove projects any time from
the **Settings** tab — every change applies live, no restart, no CLI re-run. "Suggested" projects
under Settings are auto-discovered from recently-active `~/.claude/projects/*` sessions (matched by
the `cwd` field inside their own transcripts — never a guessed/reconstructed path).

First run creates `config.json` (all settings including the project list, editable from the Settings
tab or by hand) and `data/<projectKey>/control.json` (the per-project control ledger) next to
`server.mjs`. A v2 `config.json` (single `projectRepoMap`) is migrated automatically on first v3 boot.

## Integrating with a project — local & remote

The dashboard is **project-agnostic and read-only against the project**: point it at any repo, no code
edits, no per-project install. It never writes into a watched repo — all control state lives under this
package's own `data/`.

### What it reads FROM a project (the integration surface)

| Source in the project | Feeds which tab | Required? |
|---|---|---|
| `.git` (branch, remotes, ahead/behind, tags, commit cadence) | Git, Overview | recommended |
| `~/.claude/projects/<hyphenated-abs-path>/*` transcripts | Agents, Live Feed | auto (Claude Code writes these) |
| `reports/*.md` ledgers | Live Feed | optional |
| `STATUS.md` (phase board) | Kanban | optional |
| `tasks.json` | Kanban | optional |
| `TEST-RUNS.md` | Tests & Quality | optional |

A project with none of the optional files still renders cleanly — those tabs just stay empty until the
files exist. **To enrich the dashboard for a project, have it maintain `reports/*.md`, `STATUS.md`,
`TEST-RUNS.md`, and/or `tasks.json`** (nothing else needed).

### A) Local integration (same machine as the projects)

Run natively, pointed at one project (adds + enables it on first boot); add more live from **Settings**:

```bash
cd ~/ops-dashboard
node server.mjs ~/keralora     # watch keralora
# open http://127.0.0.1:4650  → Settings tab to add solvemax-app, LawyerServed, … (all live, no restart)
```

Or containerized (mounts `$HOME` read-only at the same absolute path so transcript-dir names resolve):

```bash
REPO_PATH=~/keralora docker compose up --build   # http://127.0.0.1:4650
```

Local mode is bound to `127.0.0.1` — not reachable from other machines. Auth (`dashToken`) is optional here.

### B) Remote integration (hub + collectors, across machines)

For watching agents running on **other** machines, run a **hub** on a server and a **collector** on each
agent machine. The hub never touches any agent machine's filesystem — collectors push over authenticated
`POST /ingest`.

```bash
# On the hub server:
openssl rand -hex 32                       # generate DASH_TOKEN once
echo "DASH_TOKEN=<paste>" > .env
touch config.json                          # first run only
docker compose -f docker-compose.hub.yml up -d --build    # binds 0.0.0.0:4650

# On each machine that runs agents:
node collector.mjs --hub https://your-hub:4650 --token <paste> --project /path/to/project
```

- **Auth**: every route requires `Authorization: Bearer <DASH_TOKEN>` (or `?token=` for the SSE stream).
  Set a separate `COLLECTOR_TOKEN` so a leaked collector config can't be replayed against the dashboard's
  read/control routes.
- **TLS**: `DASH_TOKEN` is bearer-auth over plain HTTP — put a reverse proxy / TLS terminator in front of
  the hub for anything leaving your LAN.

## Uninstall

```bash
rm -rf ~/ops-dashboard
```

Nothing else on the machine references this folder — it's not a system service, it doesn't touch
any project's own files (control state lives under this package's own `data/`, not inside a watched
repo), and it isn't wired into any shell profile or launchd agent.

## The 9 tabs

| # | Tab | What it shows |
|---|---|---|
| 1 | Overview | KPI band aggregated across every enabled project (active agents, possibly-stalled count, kanban progress, last test result, pending control) + a 30-minute activity sparkline combining all projects |
| 2 | Projects (lanes) | One card per enabled project: live/building/verifying/stalled/idle agent counts, the top active agent's "currently doing" line, and its last git milestone |
| 3 | Live Feed | Every tool call, commit, tag, and ledger-row append from every watched project, pushed the instant it hits disk — project-tagged, filterable |
| 4 | Agents | Every agent across every project, sorted worst-first (possibly-stalled agents lead, sorted by longest-quiet; then live/active; idle collapsed behind a "+N idle" disclosure) — each row shows model/turns/tokens AND a live "currently doing" line parsed from its last tool call |
| 5 | Kanban | Cards from the selected project's `STATUS.md` phase board (+ optional `tasks.json`); a card whose owning agent is stalled is flagged red |
| 6 | Tests & Quality | The selected project's `TEST-RUNS.md` parsed into a pass/fail trend + full table |
| 7 | Git | The selected project's full git status: branch/remotes/ahead-behind, working-tree dirty summary, a 14-day commit-cadence sparkline, a committed→pushed→merged work-disposition matrix per branch, and a tags timeline |
| 8 | Control | Submit a request (ping/stand_down/respawn/pause_campaign/resume_campaign) targeting ONE project's control ledger, for that project's orchestrator watchdog to pick up |
| 9 | Settings | Project management (add/rename/enable-disable/remove, live, plus auto-discovered suggestions) + every other knob (ports, theme colors, feed timing, liveness thresholds, watched files, kanban columns, secret-redaction patterns) — persists to `config.json` |

A project with no `reports/` dir, no `.git`, or no Claude Code transcripts yet still renders a clean
dashboard with each panel's own empty state — nothing crashes on a fresh/unrecognized repo. A project
with `enabled: false` stays listed in Settings (re-enable any time) but its watcher is torn down.

## The narrative strip

Below the header, a plain-English sentence auto-generated from live state answers, in one glance:
how many projects are watched, which agent is doing what right now (with its actual last tool call),
when the last git milestone landed, and whether anything is stalled — e.g. *"2 projects watched. In
keralora, build-phase9c (live) — Read: .../competing-bids.tsx, 3s ago. Last milestone: tag rbac-a5 in
keralora. 1 agent possibly stalled: build-phase9b (keralora, 13m quiet)."* Jargon (agent, orchestrator,
tag, gate, SSE, transcript, kanban) has inline glossary tooltips (click the term); every panel has a
"?" button explaining what it shows and why it matters.

## Agent liveness — 6 states

Computed once (`lib/agent-status.mjs`) and used consistently everywhere (dots, chips, kanban
cards, the narrative) so nothing can disagree about whether an agent is stalled — or, just as
important, disagree about whether it's actually FINISHED rather than stuck:

| State | Meaning | Color |
|---|---|---|
| live | quiet < 60s (configurable) | green pulse |
| building | active, last tool edited/wrote/ran something | amber |
| verifying | active, last tool looked like a test/gate run | blue |
| **done** | the agent's own last TEXT message reads as a genuine sign-off (stand-down, "nothing further", a completion statement) — checked BEFORE the stall/idle timers, so a deliberately-finished agent never reads as stuck | dim, calm — deliberately NOT the alarming stalled-red |
| stalled | quiet 5+ min with NO sign-off — genuinely, nominally still in-progress | red, flagged, sorted to the top |
| idle | quiet 30+ min, no sign-off | dim, collapsed behind a disclosure |

`done` exists because a pure quiet-timer read can't tell "finished on purpose" from "stuck" — a
real false alarm the owner caught live (a stood-down agent reading as "possibly stalled") got
fixed by reading the agent's own words first. This is intentionally the SCOPED version of a much
larger agent-status taxonomy directive (8 states, multi-source cross-checking, a full "sensing
layer") — see `CLOSE-OUT.md`'s open items for what shipped here vs. what's proposed as a
follow-up pass.

## Control contract

The dashboard cannot reach into a running orchestrator session directly — there's no IPC channel
into another Claude Code process. Instead, submitting an action on the Control tab **appends a
request** to `data/<projectKey>/control.json` for the SELECTED project. An orchestrator that wants to
be controllable reads that file on its own cycle and marks entries `honored: true` once acted on.
This is a request/ack ledger, not a live command channel — treat it accordingly.

```json
{ "requests": [
  { "id": "...", "action": "ping", "agent": null, "note": "...", "ts": "...", "honored": false }
]}
```

**v3.3 — optional honoring metadata.** `honored: true` is the only REQUIRED field to mark a request
acted on. An orchestrator MAY additionally stamp `honoredAt` (ISO timestamp), `honoredBy` (who/what
honored it), and `honoredNote` (why/how) when it flips the flag — the dashboard's reader passes any
extra fields straight through untouched, and the Control tab renders them when present ("Honored
2026-07-24T… by build-orchestrator — stood down cleanly"). When they're absent (the minimum
contract above), the tab says so plainly ("Honored — n/a" for when/by/why) rather than inventing a
detail that was never recorded. This is additive and backward-compatible — nothing in the minimum
contract changed.

## Secret redaction

Every feed summary is sanitized (key/token/password/secret/`whsec_`/`sk_`/`Bearer` patterns
redacted) **before** it's truncated — so a secret can never be cut in half and partially leaked. Add
project-specific patterns (regex source strings) under Settings -> "Extra secret-strip regex patterns".

## Settings that need a restart

Everything in the Settings tab applies live — INCLUDING the project list (add/remove/enable/disable) —
**except** port, bind address, and the dash token, which require stopping and re-running
`node server.mjs` (the HTTP listener and auth middleware are bound at process start). The UI shows a
"restart required" chip when you save one of these.

## Docker

This section is LOCAL mode: the container runs on the same machine as your agents and bind-mounts
`$HOME` to watch them directly. Running the container on a DIFFERENT se