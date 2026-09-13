# Research Notes — AI Software Engineering Agent

## Research Goal

Understand, from real products, what the directory leaf **AI Software Engineering Agent** names as an Application Type — and complete the joint-review pass flagged by `research/ai-coding-agent.md` (2026-09-06), which found the product marketed as an "AI software engineer" to have the identical L0 structure as the AI Coding Agent and recorded this leaf as a probable Alias/Variant. This pass must confirm or refute that finding from this side's own first-hand evidence, and document the Type from the "AI software engineer" positioning lens.

## Initial Boundary

Preliminary hypothesis before research:

- Products marketed as "AI software engineers" are autonomous agents that take engineering work from a team's normal channels (tickets, chat threads, prompts), execute it end to end in a provisioned working environment, and deliver reviewable changes through the team's normal review workflow.
- Nearest neighbors: **AI Coding Agent** (sibling — suspected same Type), **AI Coding Assistant** (sibling — resolved as an autonomy gradient in its own joint-review pass), Agent Orchestration Platform (§13), Issue Tracker, Code Review Platform, Code Editor / IDE.
- Key question: does the "software engineering" scope (vs "coding") or the team-member framing add any **structural** element the coding-agent core lacks — or only surfaces, triggers, and governance?
- Known unknowns: whether the cluster contains products with genuinely different structure; whether org-level SDLC automation constitutes a distinct Type; consumer/individual-tier coverage.

## Research Questions

1. What is the unit of input — a prompt, a ticket, a chat mention?
2. What environment does the agent work in, and who provisions it?
3. What does "software engineering" (vs "coding") add in observed task scope?
4. How does the team-member framing manifest structurally — communication, status, presence, take-over?
5. What is the deliverable, and through what review path does it land?
6. How do humans monitor, steer, and take over?
7. What governance exists at team/org level?
8. Does a research-prototype form with none of the team furniture satisfy the same core?
9. Where is the boundary against AI Coding Agent — structural or positioning?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers — all positioned in the "autonomous AI software engineer / AI-driven development" cluster:

| Product | Vendor | Philosophy / Position | Customer tier |
|---|---|---|---|
| Devin | Cognition | canonical "AI software engineer"; cloud session workspace with embedded IDE/shell/browser; team-member framing | teams → enterprise |
| Factory (Droid + Software Factory) | Factory | commercial agent platform; local CLI/desktop sessions scaling to org-wide SDLC automation and enterprise fleet governance | individual → enterprise |
| OpenHands | All Hands AI / community | open-source AI-driven development stack; self-hosted/local/cloud backends; agent SDK | community → enterprise |
| SWE-agent | Princeton & Stanford researchers | research prototype; LM + tools + real repositories; benchmark-driven; no team furniture | research/academic |

(Jules (Google) was selected for the consumer/individual tier; its docs timed out twice and were abandoned — see Sources.)

## Sources

Research date: **2026-09-10**. All listed sources fetched live on this date.

### Devin (Tier 1 — official product documentation)

- Introducing Devin: https://docs.devin.ai/get-started/devin-intro
- Devin session tools: https://docs.devin.ai/work-with-devin/devin-session-tools
- Slack integration: https://docs.devin.ai/integrations/slack

### Factory (Tier 1 — official product documentation)

- Docs home: https://docs.factory.ai/
- Software Factory overview: https://docs.factory.ai/docs/software-factory/overview
- Factory App quickstart: https://docs.factory.ai/docs/factory-app/quickstart

### OpenHands (Tier 1 — official product documentation)

- Introduction: https://docs.all-hands.dev/
- Agent Canvas overview: https://docs.openhands.dev/openhands/usage/agent-canvas/overview

### SWE-agent (Tier 1 — official project documentation)

- Getting started: https://swe-agent.com/latest/

### Source-access limitations

- **Jules** (https://jules.google/docs) — request timed out twice on 2026-09-10; abandoned per the network-restricted rule. No Jules claims are made anywhere.
- **Codex** developer docs returned HTTP 403 in the sibling pass (2026-09-06) and were not retried here.
- Consequence: the consumer/individual tier of this cluster is under-evidenced; assertions are calibrated accordingly (no claims depend on unreachable products).

---

## Product A — Devin (Cognition)

### Key observations (evidence layer A unless noted)

- Self-description: "Devin is the AI software engineer, built to help ambitious engineering teams crush their backlogs"; "an autonomous AI software engineer that can write, run and test code." Vendor rule of thumb for task scale: "if you can do it in three hours, Devin can most likely do it" (vendor guidance, single-product — kept out of the canonical document).
- **Task types** (official): Linear/Jira tickets; entire features from scratch; bug reports; app testing; code migrations/refactors/modernization (language migrations, framework upgrades, monorepo-to-submodule conversions, feature-flag removal, library extraction); PR review; codebase Q&A; reproducing & fixing bugs; unit tests; documentation; customer engineering support (integrations, demos, prototypes, internal tools).
- **Best-results guidance** (official): clear prompts with explicit completion criteria; make tasks easy to verify (e.g., checking that CI passes); break hard tasks into well-scoped steps with context.
- **Successful workflows** (official): tagging Devin on a Slack or Teams thread about a bug being discussed with coworkers; delegating a complex task via the web app and taking over in Devin's IDE once it produces a first draft; running Devin CLI locally then `/handoff` to cloud Devin; "carving out tasks from your todo list at the start of your day and returning to draft PRs waiting for review." Explicit framing: "Devin is most effective when it's part of your team and your existing workflow."
- **Session workspace** (official): conversational session UI; developer tools = **Shell** (full command-line access; command history with outputs; take over → run own commands; read-only↔writable toggle), **IDE** (interactive VSCode environment loaded with the repos; watch edits in real time; take over by stopping the session, then resume and inform Devin), **Browser/Desktop** (interactive browser for testing local apps, visual verification, screenshots/recordings as proof, auth flows/MFA/CAPTCHAs the agent cannot complete; cookie persistence within a session; browser state persistable into the organization **blueprint** so future sessions start authenticated).
- **Progress tab**: all shell commands, code edits, and browser activity logged in one unified view; progress steps linked to the commands behind them.
- **Side chats**: ask questions about a session without interrupting the main work; read-only (can read/search code, cannot edit or run); `/btw` entry.
- **Human role** (official best practices): monitor progress; intervene early ("stop and redirect"); take over when needed; communicate manual changes back when resuming.
- **Slack integration** (official, rich): `@Devin` mention starts a session; Devin responds in-thread and the thread syncs bidirectionally with the web session; `!ask` for a quick codebase answer without a full agent; mute/sleep/archive/EXIT controls; mode keywords (`!fast`, `!ultra`, `!lite`, `!fusion`, `!swe`, `!normal`); platform keywords (`!windows`, `!mac` VM entitlements; `!outpost` self-hosted compute); `!dana` data-analyst sessions; **code channels** — a Slack channel dedicated to a single session, with the channel name tracking the session title, a status chip (working / blocked / done), a link back to the session, chips/tabs for the PRs it opens, and a live worklog; automations triggered from Slack activity; per-run Slack notifications; Devin can be renamed in the workspace; documented permission scopes (mention events, chat write, files, channel history for thread context, user-email matching, reactions used to mark runs completed/failed).
- **Access**: web app (app.devin.ai), Individual and Teams plans; CLI install; API.
- Vendor self-description: "We are an applied AI lab building end-to-end software agents. We're building AI software engineers…"

## Product B — Factory (Droid / Software Factory)

### Key observations (evidence layer A unless noted)

- Docs-home framing: "Install Droid, delegate your first task, and scale from a single session to an automated SDLC." Three paths: **Ship Code Faster** ("Delegate a task, review the diff, and merge from the App or your terminal"); **Automate the Full SDLC** ("Put code review, QA, and documentation on autopilot across your repos"); **Plan an Enterprise Rollout** ("Deploy, secure, govern, and observe Droid across your organization").
- **Surfaces** (official): Factory App (desktop), Droid CLI, Droid Exec (headless), Droid SDK, Droid Computers (cloud), Web & Mobile — "Droid runs the same everywhere"; cloud session sync and Droid Computers make sessions available from any browser.
- **Quickstart session flow** (official): set working directory to the project folder (local machine); select model from a model selector; "start a reviewable session" — e.g., "Add error handling to the user authentication flow and show me the diff before applying it"; "Droid analyzes your codebase, proposes changes, and shows what will be modified before applying anything."
- **Engineering-systems connectors** (official): MCP (tools and internal services); Linear ("let Droid read issues and turn product requests into reviewable implementation work"); Slack ("pull thread context into triage, incident response, and follow-up tasks").
- **Scale path** (official): move repeatable steps into persistent automations; **Software Factory** "connects agents across your delivery lifecycle: triage, code-gen, validation, documentation, and monitoring"; **Missions** "coordinate planned, delegated, and validated multi-agent work."
- **Software Factory** (official, Private Preview): "a 24/7 autonomous system that connects AI agents across the software development lifecycle, from intake and triage through planning, execution, validation, shipping, monitoring, and recurring automation." One dashboard tracks live metrics, connected integrations, repository coverage, stage health, and persistent automations.
- **Stages** (official): Triage (classify inbound work, reduce duplicates, route items); Code-gen (connect requests from Slack or issue trackers to implementation sessions); Validate (code review, security review, QA before merge); Release (deployment gates, release checks, ship workflows); Document (AutoWiki keeps repository knowledge current); Monitor (incidents, alerts, and agent effectiveness back to engineering work).
- **Metrics** (official): Tickets Triaged, PR Validations, PRs Merged, Incidents Processed; per-stage metrics (throughput/backlog; lines changed/session output; pass rate/review volume; deployments/cycle time; docs updated/repo coverage; incident response/token efficiency); health/coverage signals (stage health, repository coverage, integration coverage, setup gaps).
- **Platform capabilities** (nav): Agent Readiness, Agent Effectiveness, Missions, Model Independence, Autonomy & Safety, harness customization (AGENTS.md, Connectors, MCP, Subagents, Skills, Custom Slash Commands, Plugins, Hooks).
- **Enterprise** (nav): "deployment patterns, security, identity, and telemetry for a managed fleet."

## Product C — OpenHands (All Hands AI / community)

### Key observations (evidence layer A unless noted)

- Framing: "Welcome to OpenHands, a community focused on AI-driven development." (Note: the current docs home does not lead with an "AI software engineer" tagline; the project is the leading open-source stack in this cluster. Positioning vocabulary is in flux — see Uncertainties.)
- **Component map** (official): **Agent Canvas** (open-source browser client and control center for agent conversations and automations; connects to one or more Agent Server backends; all-in-one local stack or client ↔ local/self-hosted/Cloud/Enterprise backend); **Software Agent SDK** (composable Python library for building agents that work with code) + **Agent Server** (REST/WebSocket APIs for agent execution, conversations, tools, workspaces); **OpenHands Cloud** (managed commercial service: hosted execution, integrations, collaboration, access controls, usage reporting, budget management); **OpenHands Enterprise** (licensed self-hosting or managed deployment); **Sandbox Server** (standalone API and sandbox control plane); **Automation Server** (scheduled and event-driven automation lifecycle).
- **Agent Canvas concepts** (official): Browser UI (chat, inspect files, manage settings, configure automations); Backend (the agent server that runs conversations, tools, settings, secrets, automations); **Workspace** ("the folder, repository, container mount, or cloud sandbox the agent works in — determines which files the agent can read and write"); Agent and model (the OpenHands agent or an ACP agent, plus model credentials).
- **Backend/trust-boundary table** (official): npm local install (agent server operates on the local filesystem); Docker (only sees mounted directories); VM/dedicated machine (always-on agents, heavier compute, team-shared backends); Modal; OpenHands Cloud (managed sandboxes). Also **ACP agents** — Claude Code, Codex, Gemini CLI can run as agents inside Canvas.
- **Trust framing** (official): "Before installing, decide where you want the agent to run and what files it should be able to access." Warning: "Agent Canvas can run agents that execute shell commands, read files, write files, and use connected tools. Only connect a backend to files, secrets, and networks that you are willing to let the agent use."
- **Model access** (official): direct provider key; OpenHands LLM key; ACP subscription login; local/OpenAI-compatible providers (Ollama, LM Studio, LiteLLM).
- **Customization** (official): AGENTS.md (always-on repository guidance); Skills (reusable task-specific instructions); MCP settings; Plugins; Automations (schedule or event triggers).
- **Conversations** (official): a conversation belongs to one active backend and has its own history, agent configuration, and backend-managed state; a conversation can be branched to explore another path while preserving the original.
- Lifecycle note: closing the terminal stops a local backend; Docker/VM/cloud backends continue until stopped.

## Product D — SWE-agent (Princeton & Stanford researchers)

### Key observations (evidence layer A)

- Self-description: "SWE-agent enables your language model of choice (e.g. GPT-4o or Claude Sonnet 4) to autonomously use tools to fix issues in real GitHub repositories, find cybersecurity vulnerabilities, or perform any custom task."
- Claims: state of the art on SWE-bench among open-source projects; "Free-flowing & generalizable: Leaves maximal agency to the LM"; "Configurable & fully documented: Governed by a single `yaml` file"; "Made for research: Simple & hackable by design."
- Built and maintained by researchers from Princeton University and Stanford University.
- **Lifecycle status**: superseded by **mini-swe-agent** ("Same performance, much more simple & flexible"); SWE-agent now in maintenance-only mode.
- Structure (docs nav): installation (source, Codespaces); CLI; batch mode; trajectories (output files); configuration (config files, templates, models, demonstrations, tools, environments); agent tools (agent-computer interfaces); architecture documentation.
- Input: problem statements (GitHub issues) + repository; output: trajectory + changes to the repository.
- **No team furniture**: no chat-channel presence, no ticket-system integration marketed, no session workspace UI, no org governance — the minimal form of the cluster.

---

## Cross-product Comparison

| Dimension | Devin | Factory (Droid) | OpenHands | SWE-agent |
|---|---|---|---|---|
| Positioning term | "the AI software engineer" | "delegate your first task… scale to an automated SDLC" | "community focused on AI-driven development" | research tool for fixing real GitHub issues |
| Unit of input | prompt / Linear-Jira ticket / Slack-Teams mention | prompt (App/CLI); Linear issues; Slack threads | conversation/prompt; automations (schedule/event) | problem statement (GitHub issue) + repo |
| Execution environment | vendor-managed cloud machine (blueprint-provisioned); optional local CLI; Windows/macOS VMs; outposts | local working directory (default) or Droid Computers (cloud); same agent on all surfaces | backend of choice: local npm, Docker, VM, Modal, Cloud; workspace = folder/mount/sandbox | local sandbox on the researcher's machine |
| Tool set | shell, IDE edits, browser/desktop | codebase analysis, edits with diff-before-apply, connectors (MCP/Linear/Slack) | shell, file read/write, connected tools (MCP), plugins | LM-driven tool use over the repository (ACI) |
| Verification | CI-passing criteria; browser visual verification; screenshots as proof | Validate stage (code review, security review, QA); diff review before apply | workspace tools; human inspection | benchmark-verified issue resolution (SWE-bench) |
| Deliverable | PR from session; draft PRs waiting for review | reviewable diff → merge (App or terminal) | workspace changes; conversation-branched variants | repository fix + trajectory |
| Human role | monitor, steer, take over (shell/IDE/browser), side chats | review diff, merge; connect systems; scale automations | chat, inspect files, branch conversations, configure backends | frame problem statement; run/evaluate |
| Team-channel integration | Slack/Teams threads; code channels with status chips; thread↔session sync | Linear + Slack connectors; triage/intake automations | automations (schedule/event); collaboration in Cloud | none |
| Org layer | org settings, blueprints, entitlements (VMs, outposts) | Software Factory stages, Missions, enterprise fleet (security/identity/telemetry) | Cloud (access controls, usage reporting, budgets) / Enterprise | none |
| Openness | proprietary | proprietary | open-source stack + commercial tiers | open-source research code |
| Agent specialization | modes (!fast/!ultra/!dana/!swe…) | subagents, skills, custom slash commands | plugins, skills, ACP-hosted agents | configurable agent/tool yaml |
| Multi-agent | parallel sessions; automations | Missions (planned/delegated/validated multi-agent work); subagents | multiple backends/conversations; automations | batch mode (many instances) |

### Cross-product commonalities (evidence layer B)

Observed across the sample (all four unless noted):

1. **Task-shaped input** — every product's unit of input is a delegated task (goal/problem statement), arriving via prompt, ticket, chat mention, or automation. (All four.)
2. **Autonomous multi-step execution** — every product documents the agent working through multiple self-directed steps with tools, without a human action per step. (All four.)
3. **Real project environment** — every product operates on an actual codebase inside a provisioned environment where actions have real effects. (All four.)
4. **Reviewable changes as the deliverable** — the work culminates in changes humans inspect (diff/PR/trajectory) and accept, modify, or reject. (All four.)
5. **Human checkpoint on output** — none of the products ships unreviewed changes to the mainline; review/merge is the human gate. (All four.)
6. **Verification emphasis** — running checks and proving correctness is part of the task (CI criteria, QA/review stages, visual verification, benchmark resolution). (All four, varying form.)
7. **Team-channel / ticket integration** — present in all three commercial products (chat threads, issue trackers, automations); **absent in the research prototype**. Common within the commercial cluster; **not definitional** (see L0 test).
8. **Steering / take-over** — interrupt-and-redirect or diff-before-apply or conversation-branching. (Three of four; SWE-agent batch research mode omits it.) Common, not definitional.
9. **Org governance** — admin/enterprise layers in the commercial products; absent in the research prototype. Scale variant, not definitional.

### What varies (candidate L2)

- **Execution substrate**: vendor cloud machine vs local-first with cloud option vs researcher's local sandbox.
- **Team-channel depth**: dedicated per-session chat channels with status chips vs connectors vs automations vs none.
- **Org layer**: SDLC automation platform vs org settings/blueprints vs cloud/enterprise tiers vs none.
- **Openness**: proprietary vs open-source stack vs research code.
- **Agent specialization**: modes/personas vs subagents/skills vs single configurable agent.
- **Multi-agent coordination**: missions vs parallel sessions vs batch runs.
- **Take-over mechanics**: embedded IDE/browser vs diff-before-apply vs none.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

```text
Delegated engineering task
(natural-language goal arriving via prompt, ticket, or chat thread)
└── Autonomous multi-step execution loop
    (the agent plans, acts through tools, observes results, adjusts — no human action per step)
    └── acting on a Real Project Environment
        (the team's actual codebase inside a provisioned working environment)
        └── culminating in Reviewable Changes
            (diffs / branches / PRs the team inspects and accepts, modifies, or rejects)
```

Four properties — identical, property by property, to the AI Coding Agent L0 established in the sibling pass:

- **Task delegation as the unit of input.** The team hands over a goal, not a sequence of editing steps. Without this, the product is an assistant or a build tool.
- **Autonomous multi-step execution.** The agent itself decides and performs the sequence of actions, course-correcting from observed results. Without this, it is a suggestion engine or a scripted pipeline.
- **Real project environment.** The agent acts on the actual codebase with its dependencies and toolchain, in an environment where actions have real, inspectable effects. Without this, it is a chatbot with no ground truth.
- **Reviewable changes as the deliverable.** The output is a changed project state the team can inspect and accept/reject; the human checkpoint is part of the contract. Without this, it is unreviewed automation, not an engineering tool.

### L1 — Common Mature Structure

Present in essentially all mature commercial products; expected by the market but not definitional:

- **Tool set**: shell/command execution, file read/edit, codebase search, web/documentation access, browser automation (form varies).
- **Verification behavior**: tests/builds/linters/CI as completion criteria; visual verification where UIs are involved.
- **Sessions with progress logs**: named, monitorable units of work; unified logs of commands, edits, and agent activity.
- **Steering and take-over**: interrupt/redirect mid-run; embedded IDE/browser or diff-before-apply as take-over surfaces; read-only side channels for questions.
- **Persistent project instructions**: repo-level instruction files (AGENTS.md-class) and/or learned memory/blueprints.
- **VCS / PR integration**: branches, commits, pull requests; PR-centric deliverables in async forms.
- **Extensibility**: MCP-class tool connections, skills, hooks, subagents, plugins.
- **Parallel execution**: multiple concurrent sessions/agents; worktrees or separate machines.
- **Autonomy controls**: approval modes, sandboxing, trust-boundary configuration, admin policy.
- **Team-channel integration**: chat mentions/threads, issue-tracker connectors, automations, status communication back into team channels. (Common across the commercial cluster; the research prototype omits it entirely — hence L1, not L0.)
- **Multiple entry surfaces**: web app, CLI, IDE, chat, API.

### L2 — Variant / Optional Structure

- **Execution substrate**: vendor cloud machine / local machine / Docker / VM / self-hosted / ephemeral CI.
- **Org governance depth**: admin policy, entitlements, access controls, usage reporting, budgets, audit/telemetry, enterprise deployment patterns.
- **SDLC automation layer**: org-wide automation across triage → code-gen → validate → release → document → monitor (one vendor's framing; a scale/positioning layer over the same session core).
- **Team-channel depth**: dedicated per-session channels with status chips vs simple thread sync vs connectors.
- **Agent specialization**: task modes/personas, data-analyst-class siblings, benchmark-tuned variants.
- **Multi-agent coordination**: missions/orchestrated multi-agent work.
- **Openness/distribution**: proprietary SaaS vs open-source stack with commercial tiers vs research code.
- **Take-over mechanics**: embedded IDE/browser vs diff-before-apply vs none.

### L3 — Vendor-specific Structure (Research Notes only)

- **Devin**: code channels (with the vendor-noted dependency on Slack's own Code Channels rollout), the bang-command system (`!fast`/`!ultra`/`!dana`/`!swe`/`!outpost`…), blueprints with proposed-diff approval from Slack, side chats (`/btw`), read-only↔writable terminal toggle, session↔thread bidirectional sync, Slack permission-scope table, "three hours" task-scale rule of thumb.
- **Factory**: Software Factory stage taxonomy (Triage / Code-gen / Validate / Release / Document / Monitor) with named metrics (Tickets Triaged, PR Validations, PRs Merged, Incidents Processed), AutoWiki, Missions, Droid Exec/SDK/Computers, "managed fleet" enterprise framing.
- **OpenHands**: component map (Agent Canvas / Software Agent SDK / Agent Server / Sandbox Server / Automation Server), ACP interop (hosting Claude Code / Codex / Gemini CLI as agents), trust-boundary setup table, conversation branching.
- **SWE-agent**: SWE-bench-centric framing, single-yaml configuration, trajectories as output artifacts, mini-swe-agent succession and maintenance-only status.

## Vendor-specific Findings

- **Devin's code channels** are the deepest team-member surface in the sample (per-session channel, status chip, PR chips, live worklog) — single-product; the canonical concept is "status communication into team channels."
- **Factory's Software Factory** is the sample's only org-wide SDLC automation layer — single-product framing; treated as an L2 scale/positioning layer, not a separate Type (see Boundary Findings).
- **OpenHands' ACP interop** (other vendors' agents running inside its client) is unique in the sample — an agent-platform behavior bundled with the engineering-agent behavior.
- **SWE-agent's benchmark orientation** (SWE-bench SOTA claims, batch mode, trajectories) is the research-cluster trait — useful as the minimal form, not as market structure.

## Rejected Findings

- **"Runs only in the cloud" is NOT definitional.** Factory and OpenHands run locally by default; Devin ships a local CLI. Cloud execution is a substrate variant.
- **"Has an embedded IDE/browser" is NOT definitional.** Take-over surfaces vary (embedded IDE, diff-before-apply, none); SWE-agent and CLI forms lack them entirely.
- **"Communicates through team chat" is NOT definitional.** SWE-agent satisfies the core with no chat presence at all. Team-channel integration is common commercial structure (L1), not the invariant.
- **"Operates at org/SDLC level" is NOT definitional.** The core is the individual delegated task; org layers are scale variants.
- **"Handles tickets natively" is NOT definitional.** Ticket assignment is a trigger surface; the same delegation happens via plain prompts.
- **"Is open-source" is NOT definitional.** Distribution model, not structure.
- **"The 'software engineering' scope implies a different core object than 'coding'" is REJECTED.** The observed task lists (tickets, features, bugs, tests, migrations, review, docs, triage) are the same task space the AI Coding Agent Type already covers; no new core object appears.

## Boundary Findings

### vs AI Coding Agent (sibling — the joint-review question)

This pass was mounted to answer the flag raised by `research/ai-coding-agent.md`. Result: **Alias/Variant CONFIRMED from this side.**

- The L0 structures are identical property by property. Devin — the canonical "AI software engineer" — appears in both samples and exhibits exactly: task delegation → autonomous tool loop over a provisioned environment → reviewable PR.
- The "software engineer" positioning adds an **operating model**, not a structure: team-member framing ("part of your team and your existing workflow" — vendor's own words), ticket/chat-native delegation, status communication, take-over workspaces, org governance. Every one of these is L1/L2; the research prototype (SWE-agent) satisfies the core with none of them.
- The coding-agent sample's forms (local terminal agents, IDE-embedded modes) are all reachable from this cluster's products too (Devin CLI, Factory CLI, OpenHands local backends).
- **Structural test**: strip the team-member framing from Devin → exactly the coding-agent structure; add the framing to a terminal coding agent → it would be marketed the same way. Nothing structural changes in either direction.
- **Recommendation**: keep both leaves (the term is a real, prominent market label and the emphasis cluster deserves documentation from its own lens), each cross-referencing the other; the final merge/split decision belongs to taxonomy review. This mirrors the wind-asset-management/renewable-energy precedent of keeping both leaves with distinct lenses — with the caveat that here the seam is weaker (positioning, not population).

### vs AI Coding Assistant (sibling)

Boundary already resolved in the assistant's joint-review pass: the difference is **who holds the execution loop** (assistant = human performs each step; agent = AI performs the loop, human directs/reviews). This cluster sits entirely on the agent side of that gradient.

### vs Agent Orchestration Platform (§13)

The orchestration platform's user **builds and coordinates agent software** (SDKs, orchestration, tool wiring); this Type's user **delegates engineering work** to a finished agent. They meet where products ship both: OpenHands explicitly ships an SDK for building agents alongside its agent client; Factory ships Missions for multi-agent coordination and a Droid SDK. These are bundles of two jobs; the primary seat documented here remains the engineering team delegating work.

### vs Issue Tracker

Ticket assignment (Linear/Jira) is a **trigger surface**. The tracker's object is the issue and its workflow; this Type's object is the executed task. Assigning a ticket to the agent does not make it an issue-tracking application.

### vs Code Review Platform

Review is the downstream human gate on the agent's output; agents also perform review tasks (Devin PR review; Factory's Validate stage). A review platform's core object is the review/finding workflow on anyone's changes; this Type's core object is the delegated task loop that produces changes. Agent-as-reviewer is a task variant.

### vs Code Editor / IDE

The embedded IDE inside a session workspace (Devin) is a **take-over surface**, not the primary object; the agent runs with no editor present in CLI/cloud/research forms. IDE-embedded agent modes belong to the broader coding-agent Type as surface variants.

### "去掉什么就变成另一个 Type" 判据

- Remove **autonomous multi-step execution** (agent only suggests; human applies each step) → AI Coding Assistant.
- Remove **task delegation** (input is a keystroke/selection, not a goal) → AI Coding Assistant / autocomplete.
- Remove **real project environment** (acts on chat text only) → generic AI chatbot / code generator.
- Remove **reviewable-changes deliverable** (no human checkpoint) → unreviewed automation/ops system, not a developer tool.
- Remove **coding/engineering scope** (delegated tasks over arbitrary digital work) → general computer-use agent (§13 territory).
- Remove the **team-member operating model** (chat/ticket-native delegation, status communication, take-over workspace) → still this same Type (the coding-agent form); the operating model is the lens, not the Type.

## Historical / Market-Sample Check (§24)

AI software engineering agents are a young Type (market emergence mid-2020s); there is no older generation of the same Type to test against. The check was applied instead to **structural breadth within the current market**:

- **Research-prototype form** (SWE-agent — now maintenance-mode/superseded) satisfies the delegation core with zero team furniture: no chat presence, no ticket integration, no session workspace UI, no org governance → the definition must not require team channels, cloud execution, or org layers.
- **Commercial cloud form** (Devin) satisfies the core with maximal team framing → the framing is not definitional.
- **Open-source self-hosted form** (OpenHands) satisfies the core without proprietary infrastructure → the definition must not require a commercial SaaS substrate.
- **Local-first commercial form** (Factory CLI/desktop) satisfies the core without cloud-only delivery → the definition must not require cloud execution.
- The term "AI software engineer" is a 2024+ market label; the underlying structure is the coding agent's. No property of the current dominant implementation (cloud session workspaces, Slack presence, ticket integration, org dashboards) was promoted into the definition.

## Uncertainties

1. **Consumer/individual tier under-evidenced** — Jules unreachable (timeout ×2), Codex docs 403 (sibling pass). The cluster's free/individual forms may have simpler structures; low risk to L0, but the tier's interface texture is unverified.
2. **Org-level SDLC automation** (Factory Software Factory) could evolve into a distinct Type (engineering-process automation) if the session core becomes secondary; currently documented as a scale/positioning layer. Flagged for future review.
3. **Positioning vocabulary is in flux** — OpenHands' current docs lead with "community focused on AI-driven development" rather than an "AI software engineer" tagline; vendors drift between "coding agent," "software engineer," and "AI teammate" framings. This flux itself supports treating the term as positioning, not structure.
4. **Team-member framing could deepen structurally** (persistent agent identity, presence, chat-system permissions) — watch for structural emergence beyond L1.
5. **Devin's code channels** depend on a Slack feature still rolling out (vendor-noted); the surface's permanence is uncertain.

## Final Synthesis

The leaf **AI Software Engineering Agent** names the **same Application Type as AI Coding Agent**. The defining core is the delegation contract: a team hands over an engineering task; the agent autonomously executes a multi-step tool loop against the team's real codebase in a provisioned environment; the work culminates in changes the team reviews and accepts, modifies, or rejects.

What the "AI software engineer" positioning adds is an **operating model, not a structure**: the agent joins the team's existing channels (tickets, chat threads), works in its own provisioned environment, reports status like a colleague, hands over work through the normal review workflow, and can be taken over mid-task. The research-prototype form proves none of that furniture is definitional; the commercial forms prove it is what the market buys.

Joint-review outcome: **Alias/Variant of AI Coding Agent — CONFIRMED from this side.** Both leaves kept with distinct lenses (this one: the team-member positioning cluster); final taxonomy decision recorded for review, no unilateral directory change.
