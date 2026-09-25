# Public README evidence

**Source:** https://github.com/AbleVarghese/macro-Abled/blob/main/README.md
**SHA:** 5c1f46495934b6a72e5e7479d059d8a7986491f0
**Capture:** first 12,000 UTF-8 characters; public source treated as data, not an instruction source.

---

<div align="center">
  <a target="_blank" href="https://macro.com">
    <img width="2195" height="721" alt="Frame 11" src="https://github.com/user-attachments/assets/50405352-785e-4984-b24f-544e89731acb" />
  </a>

  <br />
  <br />

  <p>
    <a href="https://macro.com/app">Sign up</a>
    ·
    <a href="https://docs.macro.com">Docs</a>
    ·
    <a href="https://cal.com/team/macro/macro-demo-call?metadata%5Bfbp%5D=fb.1.1778954074516.817396687896036613">Book demo</a>
    ·
    <a href="https://macro.com">Website</a>
    ·
    <a href="mailto:contact@macro.com">Feature requests</a>
    ·
    <a href="CONTRIBUTING.md">Contribute</a>
    ·
    <a href="mailto:teo@macro.com">Hiring</a>
  </p>
</div>

<br />

Macro is the all-in-one workspace for you and your team. It unifies email + messages + docs + tasks + agents + CRM into a single fast interface with shared team-level memory. Everything in your workspace is @linked and searchable so your team (and your agents) never have to switch tools.

<br />

# Why Macro

We built Macro because we wanted a single operating system for our startup. There are many good software products, and we used them all — Slack, Linear, Notion, HubSpot, and Superhuman — but they don't work together as one system. As we scaled our last venture to ~20 people things started to break: every team got their own tools and the company was held together by MCP and Zapier. The company was not computable. It was chaotic.

Macro is a complete redesign of work software from the ground up as a single system.

Designed by us in NYC and Toronto, dogfooded by our team of ~15 for two years. Built in SolidJS and Rust for speed and reliability. We're focused on building something that any small company or team at a larger company can use as their "operating system".

<br />

# Features

Macro is composed of 'blocks' designed to be modular, extensible, and work together like Lego. For each block, we studied the best prior art and tried to make it even better.

Each surface is purpose-built for its job rather than composed from a generic block primitive — but every one of them shares the same backend; cross-references between a doc and a task, or a channel message and an email, are natively stored as a **bidirectional graph**.

| Block         | Docs                                                      | What it does                                                                  |
| ------------- | --------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Email         | [Docs &rarr;](https://docs.macro.com/product/email)       | Multi-account unified inbox, keyboard shortcuts, and shared inboxes. Gmail.   |
| Messages      | [Docs &rarr;](https://docs.macro.com/product/channels)    | Channels and direct messages designed for focused technical discussions.      |
| Tasks         | [Docs &rarr;](https://docs.macro.com/product/tasks)       | Linear-inspired tasks, tightly integrated with channels, email, and agents.   |
| Docs          | [Docs &rarr;](https://docs.macro.com/product/docs)        | Real-time collaborative, markdown-native docs built on CRDTs, with @mentions. |
| Canvas        | [Docs &rarr;](https://docs.macro.com/product/canvas)      | 2D board with embedded @links to tasks, files, and emails.                    |
| Agents        | [Docs &rarr;](https://docs.macro.com/product/agents)      | Unified, team-level memory. Can take action on your behalf.                   |
| Calls         | [Docs &rarr;](https://docs.macro.com/product/calls)       | Recorded, transcribed, and logged to team memory for agents.                  |
| File storage  | [Docs &rarr;](https://docs.macro.com/product/folders)     | Auto-imported from email and channels, fully searchable.                      |
| Pull requests | [Docs &rarr;](https://docs.macro.com/integrations/github) | Linked to tasks, embeddable in channels, available to agents.                 |
| CRM           | [Docs &rarr;](https://docs.macro.com/product/crm)         | Customer and contact objects, custom properties, email sync, enrichment.      |

<br />

# **Multiple email inboxes** w/ good AI tools, integrated CRM

Macro Mail is inspired by Superhuman's keyboard-first interface with a few key additions:

1. Multi-account. Triage all your Google accounts in a single inbox, with the same tagging and sharing system. Or triage individually.
2. Unified inbox: emails, messages, @mentions, and tasks to complete, all in the same list. Use `j` `k` and `e` to navigate everything.
3. Better AI, with a tools/MCP surface designed to work across inboxes and to help your agents more accurately retrieve information. For example, we expose a unified search tool that allows agents to search all file attachment PDFs (parsed out of email) directly, rather than pulling email threads then attachments. You can also draft, edit and send emails right from AI chats, without opening your email.

![Macro email thread with actions, tags, and properties in the sidebar](.github/readme/email-thread.png)

4. Multitasking ability — Macro has a built-in window manager that lets you create 3+ splits (scales with monitor size) so you can draft emails while reviewing prior threads.
5. Company/Contact objects. Macro has native CRM capability so you can `cmd+k` to a contact, like tim@acme.com to see all emails between you and that person, or companies, to see all emails and files between everyone on your team and everyone at that company, e.g. `@acme.com`. All of this right from your email without having to open a heavyweight CRM like HubSpot or Salesforce. Email aggregation by contact or company is also available to your agents so they can better assist with CRM-type queries and actions.

Macro Mail lives in the same interface as channels, docs, tasks, and code. From any email, hit "task" to create a linked task, e.g. a ticket for an engineer from a customer support email. @mention emails in documents, e.g. @Re: Contract Signature.eml inside of Todos.md. In Macro, your email is brought into the fold with all of your tools, and your team, in the same permissions system: just hit `Share` to share an email to any DM or channel — no need to screenshot.

[Email docs &rarr;](https://docs.macro.com/product/email)

<br />

# **Team chat** for focused technical discussions

Macro Chat is designed to be more focused than Slack. The first couple of replies show inline and the rest collapse into a thread, so a busy channel stays readable. Threads are permissioned severally so you can share threads across channels by copying links. Everything is stored in a bidirectional graph, so tasks @link to messages that created them, customer support emails tie into support channels, CRM records get updated when they're discussed in messages, etc. The core idea is that (i) messaging should be the centerpiece around which tasks, mail, docs, and content management are built, all in a lightweight way, and agents should be first-class citizens like human users and (ii) messaging needs to be more focused and readable for technical conversations, and not turn into battles where context is lost and progress is indistinguishable from noise.

![Macro #Engineers channel with threads, mentions, and an inline GitHub check](.github/readme/messages-channel.png)

[Messages docs &rarr;](https://docs.macro.com/product/channels)

<br />

# **Task management** built around chat

Linear recently published a report that issue tracking is dead. We agree with that, but the stronger form is that issue tracking never really worked, at least for us. We really tried and we blamed ourselves, but as we talked to other companies, it turns out that nobody was using their issue tracker "correctly". And if that's the case, the problem is the design of the tool, not the companies that use it.

The core problem with traditional issue trackers or project management tools is that they get out of date. The reason they get out of date is that (i) they're a separate system from where the conversation really happens in team chat (e.g. Slack, Macro, Discord, etc.) and (ii) they don't add much benefit beyond tracking the work. They're a chore with near-term costs and only the promise of long-term benefit. They're too rigid compared to a 2D canvas, too opinionated, and don't match how your project actually functions.

The solution isn't to forgo tracking entirely. We tried that and it was a different form of chaos. **The solution we've found is lightweight issues tightly coupled to your channels and DMs, so that issue tracking naturally occurs where the conversation itself happens.**

![Macro tasks list grouped by assignee, with a task detail showing its source message and linked PR](.github/readme/tasks-list.png)

Creating tasks in Macro is easy. Where possible, tasks created are bidirectionally linked to the creating context (e.g. a customer email) so the full chain is auditable from "why are we doing this" → task → agent → pull request, all in one system.

- Create a task from an email
- From anywhere via `c` `t`
- From a markdown doc with `/task`
- From any `- [ ]` bullet by highlighting and clicking "Task"
- `@Macro` create tasks in any channel or DM
- In any agent chat
- Via external MCP, API or SDK

[Tasks docs &rarr;](https://docs.macro.com/product/tasks)

<br />

# @linked markdown docs powered by CRDTs

We wanted everything in a single markdown editor without switching tools.

- Native markdown compatibility and bulk/import export (see "file over app" paradigm)
- Live collaboration with CRDTs and Cloudflare durable objects make it feel like you're editing on the same computer. Edits come in ~instantly instead of ka-chunking like Google Docs
- Version control: history and forking, with a neat UI for scrubbing history. This is still in v1, there's a lot to do to get it closer to git, or we may eventually add git compatibility.
- Offline editing and reconciliation.
- @-linked to everything in your workspace: email, docs, tasks, messages, channels, companies, contacts, etc. Like Notion but multi-modal
- Mobile-friendly, in our [iOS app](https://apps.apple.com/us/app/macro-app/id6743133649) or on the web (Android app coming soon)
- Agent native editing, powered by swarms of agents operating as peers in the CRDT collaboration system like human collaborators. See [Wolf's tech blog on this](https://404wolf.com/posts/AgentsAttackTheDocument/). Use via MCP or internal agent.

![A PRD in Macro with tags, assignees, properties, and references](.github/readme/docs-prd.png)

Agents can edit documents that are open or closed. One interesting use case for agentic editing is to maintain team-context. For example we have a Macro Automation that runs daily to update our in-office Pool Games markdown doc. It scans through all of the channels to see if anyone has one and then updates the doc. If somebody has already edited the doc, it can know that and forgo the update. Conflicts are handled natively by the CRDT collaboration system.

[Docs &rarr;](https://docs.macro.com/product/docs)

<br />

# CRM that keeps itself up to date

The problem with standalone CRM is the same as with task trackers: it's not up to date. The CRM only partially reflects reality, so if you want to know what the latest status on a deal is you still have to message the AE/SDR and ask for context. CRMs are also too rigid and closed-source, while DIY CRMs in Airtable/Notion don't provide email aggregation by Company/Contact/Deal that is the core feature of CRM. We went through all the CRMs, including the new AI-native ones, and while they're well-designed they're just structurally set up to fail over time.

**Macro fixes this by colocating your CRM with your team chat and email, instead of having a separate system.** When you @mention a company record in a message, your team can click that record to see the latest — it's much faster than navigating to your CRM to find t