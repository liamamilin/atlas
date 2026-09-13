# AI Coding Agent

## Overview

An **AI Coding Agent** is a developer-facing application in which a software-engineering task is **delegated in natural language** to an AI that **autonomously executes a multi-step tool loop** — searching, reading, editing files, and running commands — against a **real project environment**, and whose work culminates in **changes the developer can review and accept, modify, or reject**.

The defining structure is small:

```text
Developer-issued Task (natural-language goal, optionally with attached context)
└── Autonomous multi-step execution loop
    (the agent plans, acts through tools, observes results, adjusts — no human action per step)
    └── acting on a Real Project Environment
        (an actual codebase inside an execution environment where actions have real effects)
        └── culminating in Reviewable Changes
            (project changes the human can inspect as diffs and accept / modify / reject)
```

Everything commonly associated with current products — cloud sandboxes, pull-request deliverables, issue-assignment triggers, classifier-gated auto-execution, embedded IDEs — is widespread in current products but is not part of the defining core. A terminal agent working on the developer's own machine and a cloud agent opening pull requests from an ephemeral environment are the same Type with different substrates.

The boundary against the **AI Coding Assistant** is who holds the execution loop: the assistant helps a human who performs each step; the agent performs the steps itself while the human directs and reviews.

## Users & Context

The primary user is a **software developer** who has work that is well-defined enough to delegate: fixing a bug, implementing an incremental feature, writing or fixing tests, updating documentation, resolving merge conflicts, refactoring, upgrading dependencies, triaging a backlog of small tickets.

The relationship between the developer and the application is a **delegation contract**, and it changes what the developer does:

- **Before the run**: the developer frames the task (goal, constraints, pointers to relevant code or issues) and chooses how much autonomy to grant.
- **During the run**: the developer monitors progress and may steer — interrupting, queueing corrections, or answering the agent's questions — without taking the work back.
- **After the run**: the developer reviews the resulting changes as diffs, requests revisions, and ultimately merges or discards them. The developer remains the reviewer and merger; the agent's output is a proposal until a human accepts it.

Secondary users appear in team and enterprise contexts: **team leads or administrators** who configure which autonomy levels, models, tools, and repositories agents may use; and **teammates** who interact with an agent's output through the normal review workflow (comments on a pull request, for example).

Typical contexts of use: an individual developer's machine (terminal or editor), a team's code-hosting platform (web UI, issue tracker, chat), and unattended automation (scheduled or event-triggered runs). The same agent structure serves all three; what changes is the trigger and the substrate.

## Core Model

### The Defining Core

```text
Developer-issued Task
└── Autonomous multi-step execution loop
    └── Real Project Environment
        └── Reviewable Changes
```

Four properties. If any one is removed, the product is no longer recognizable as an AI Coding Agent:

- **Task delegation as the unit of input.** The human hands over a goal — "fix this bug," "implement this ticket," "write tests for this module and make them pass" — not a sequence of editing steps. Input is a natural-language task, optionally enriched with an issue, a screenshot, an error log, or a chat thread. Without this, the product is an assistant or a build tool.
- **Autonomous multi-step execution.** The agent itself decides and performs the sequence of actions — gather context, take action, verify results — chaining many steps and course-correcting from what it observes, with no human action per step. Without this, the product is a suggestion engine or a scripted pipeline.
- **Real project environment.** The agent acts on an actual software project — its files, dependencies, and runnable toolchain — inside an execution environment where actions have real, inspectable effects. Without this, it is a chatbot producing code text with no ground truth.
- **Reviewable changes as the deliverable.** The work culminates in a changed project state that the human can inspect — as a diff, a set of commits, or a pull request — and accept, modify, or reject. The human checkpoint on output is part of the Type's contract. Without this, it is an unreviewed autonomous system, not a developer's tool.

### Capabilities Shared by Mature Products

A typical modern product carries most of these capabilities. They are not what makes the product an AI Coding Agent, but they make it practical.

- **Tool set** — file read/edit/create, codebase search (by file name and content), shell/command execution, and web search or documentation fetch. Tools are the agent's only way of acting; each tool result feeds the next decision.
- **Verification behavior** — running tests, builds, or linters and iterating on failures. Mature products treat "make the checks pass" as part of the task, not an extra.
- **Sessions** — the unit of work is a session: a named, monitorable run with a progress log of steps, commands, and edits. Local sessions are commonly resumable; cloud sessions are listed and trackable.
- **Steering** — the human can inject direction while the agent works: interrupting, queueing messages to be processed in order, or sending follow-ups that take effect at the agent's next step, without restarting the run.
- **Checkpoints / undo** — snapshots of the project taken before changes, restorable independently of version control, so a wrong turn can be rolled back.
- **Persistent project instructions** — instruction or rules files in the repository (and/or learned memory) that shape every session: coding standards, architecture notes, preferred libraries, verification commands.
- **VCS integration** — branches, commits, and pull requests. Async, platform-embedded products make the pull request the deliverable and route iteration through its comments; local-first products treat commits and PRs as optional final steps.
- **Extensibility** — connections to external tools and data sources (commonly via an open tool-integration protocol), reusable skills or playbooks, lifecycle hooks, and sub-agents for delegated sub-tasks.
- **Parallel execution** — multiple concurrent agent sessions or agents, isolated from each other via separate working copies (worktrees) or separate machines.
- **Permission / autonomy controls** — an explicit layer that bounds what the agent may do without asking: approval modes, allowlists, classifier review of risky actions, OS-level sandboxing, and administrator policy. The existence of this layer is common structure; its default posture is a variant.
- **Multiple entry surfaces** — the same agent reachable from a terminal, an IDE, a web interface, a chat tool, an issue tracker, or CI pipelines.

### One Structure, Many Implementations

The Core Model is written in conceptual terms. The Variants section enumerates how specific implementations realize each concept.

```text
Concept:            Autonomous execution loop
Implementations:    interactive terminal session, IDE-embedded agent mode,
                    cloud session on an ephemeral machine, scheduled/automated run

Concept:            Real Project Environment
Implementations:    local working directory, ephemeral CI-powered environment,
                    vendor-managed cloud machine, self-hosted runner

Concept:            Reviewable Changes
Implementations:    working-tree diff + checkpoints, commits on a branch,
                    pull request with review request and comment iteration

Concept:            Task input
Implementations:    typed prompt, issue assignment, @mention in chat or PR,
                    "fix this" buttons, scheduled/automated prompts
```

A reader who has only seen one form (for example, a cloud agent that opens pull requests) should still be able to recognize the local terminal form — and vice versa — from the Core Model.

## How It Works

### The delegation loop

The defining workflow runs end to end like this:

```text
Frame the task
→ the developer states a goal in natural language
  (optionally attaching an issue, screenshot, error log, or design notes)
→ choose autonomy level and target
  (permission mode / run mode; repository and base branch, or local directory)

Prepare the environment
→ the product provisions a place to work:
  a local directory, a fresh branch, or an ephemeral/cloud machine
  with the project's dependencies and toolchain available

Run the agentic loop
→ gather context: search and read the codebase, consult instructions/memory
→ take action: edit files, create files, run commands
→ verify results: run tests / builds / linters; observe output
→ adjust: course-correct from what was learned; repeat until done
  (the human may steer at any point without restarting)

Produce the deliverable
→ changes left in the working tree, and/or
→ commits pushed to a branch, and/or
→ a pull request opened for review

Human review and iteration
→ the developer inspects the diff
→ revision requests become follow-up messages / PR comments / new runs
→ the developer merges, discards, or takes the work over manually
```

### What the agent actually does inside the loop

A typical bug-fix task illustrates the loop's texture. Given "fix the failing tests in the auth module," the agent will commonly: run the test suite to see what fails; read the error output; search for and read the relevant source files; edit them; re-run the tests; and repeat until they pass — each observation informing the next action. The agent decides which steps to take and in what order; the human chose the goal, not the steps.

### Steering and take-over

Two interaction patterns run alongside the main loop:

- **Steering**: while the agent works, the human can interrupt it, queue messages for after the current step, or send corrections that take effect at the agent's next tool call. The run continues; the plan bends.
- **Take-over**: the human can stop the agent and work in the environment directly — editing files or running commands in the same workspace — then hand control back and tell the agent what changed. Products differ in how literal this is (an embedded IDE inside the agent's workspace vs the agent running inside the human's editor vs a shared terminal); the pattern — pause, intervene, resume with context — appears across the sample in different forms.

### The asynchronous form

When the agent runs unattended (issue assignment, @mention, scheduled or event-triggered runs), the same loop executes without a human at the keyboard. The deliverable is conventionally a pull request; iteration happens through comments on that pull request, which spawn follow-up runs that retain the context of the original task. Progress is observable after the fact through session logs and timeline events.

### Core vs Common vs Optional

**Defining core** — without these, not an AI Coding Agent:

- task delegation as the unit of input
- autonomous multi-step execution loop
- real project environment
- reviewable changes as the deliverable

**Common mature structure** — present in most modern products:

- tool set (files, search, shell, web)
- verification behavior (tests/builds/linters)
- sessions with progress logs
- steering and take-over
- checkpoints / undo
- persistent project instructions
- VCS integration
- extensibility (external tools, skills, hooks, sub-agents)
- parallel execution
- permission / autonomy controls
- multiple entry surfaces

**Variant / optional** — depends on substrate, positioning, and customer scale:

- execution substrate (local / cloud / ephemeral CI / self-hosted)
- output convention (working-tree-centric vs PR-centric)
- trigger model (interactive / async delegation / automation)
- autonomy posture (ask-first / classifier-mediated / full-auto)
- environment provisioning and take-over mechanics
- enterprise governance and model strategy

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product, and a given product may expose only a subset.

### Task input surface

Where delegation begins.

- a prompt field (in a terminal, IDE panel, web app, or chat tool), an issue-assignment control, a mention, or an action button
- typical information: the task description; target repository/directory; base branch; autonomy or model selection
- primary actions: submit the task; attach context (images, logs, links); select agent profile or model

### Session / progress view

The window into a running or finished run.

- a live or replayable log of the agent's steps: commands executed, files edited, observations made
- typical information: current step, tool calls and outputs, elapsed effort, status (working / waiting for input / finished / failed)
- primary actions: steer (queue or send a message), interrupt, take over, open the resulting changes

### Change review surface

Where the deliverable is judged.

- a diff of what the agent changed, in the product's own UI or in the standard code-review workflow (pull request)
- typical information: changed files, per-file diffs, verification results (tests/checks), the agent's summary of what it did and why
- primary actions: approve, request changes (which become follow-up instructions), comment, merge, discard, restore a checkpoint

### Permission / approval surface

Where autonomy is bounded.

- prompts or settings controlling what the agent may do without asking: run this command? edit this file? access the network?
- typical information: the pending action, the rule or classifier decision behind it, scope of the grant
- primary actions: allow once / always, deny, edit allowlists, switch autonomy mode

### Embedded environment surfaces (variant)

Some products expose the agent's working environment directly:

- a terminal pane showing the agent's shell activity (and accepting human commands)
- an embedded editor for inspecting or taking over the agent's edits
- an embedded browser for testing web UIs the agent builds, or for completing authentication steps the agent cannot

### Management surface (team/enterprise)

- lists of agent sessions across a team; admin controls for autonomy levels, model access, tool integrations, and repository scope; usage and outcome metrics

## Important Rules / Behaviors

### The agent's output is a proposal

Everything an agent produces — edits, commits, pull requests — remains reviewable and reversible until a human accepts it. Products reinforce this with checkpoints (restorable snapshots taken before changes) and with the standard review workflow the changes flow into. This is the Type's core safety contract: autonomy in execution, human authority over acceptance.

### Autonomy is bounded by an explicit control layer

Every mature product ships a control layer between "ask before everything" and "do everything": approval modes, allowlists of trusted commands, classifier review of risky actions, OS-level sandboxing (workspace-scoped file access, restricted network), and administrator policy that overrides individual settings. Two structural behaviors follow:

- **Local agents gate actions; cloud agents gate environments.** A local agent asks (or a classifier reviews) before risky commands, because it runs where the human's files live. A cloud agent typically runs in a disposable environment where per-action approval is unnecessary — the isolation itself is the control — and the human gate moves to the output (review the PR, approve CI runs).
- **Dangerous categories can keep hard gates.** Some products reserve certain action classes — deleting files, writing outside the workspace, browser automation — for explicit approval even in permissive modes.

### The agent works on a copy, not the mainline

Whether by branch, worktree, or ephemeral machine, the agent's changes are isolated from the primary line of development. Merging — not editing — is the moment the work lands.

### Verification is part of the task

"Done" conventionally means the checks pass, not merely that code was written. Mature products run tests/builds/linters as part of the loop, and delegation guidance explicitly asks users to frame tasks with verifiable completion criteria.

### Sessions are durable units of work

A session's transcript and progress log persist after the run; local sessions can be resumed or forked; follow-up requests on the same deliverable (e.g., the same pull request) commonly reuse the context of earlier runs.

### Scope and resource limits exist

Products commonly scope a run — for example to a single repository, a single branch, or a single deliverable — and unattended runs may be bounded by a maximum execution time. The exact limits are product policy (they vary and change); the structural point is that runs are deliberately scoped rather than open-ended.

### Persistent instructions shape every run

Repository-level instruction files and learned memory are read at session start. They are the mechanism by which team standards survive across tasks and across agents — and the recommended place for rules the agent must always follow, precisely because in-loop conversation context can be compacted away on long runs.

## Variants

The Type is implemented in several recognizable forms. Common variants:

- **Local interactive agent** — runs on the developer's machine (terminal or inside the editor); works directly on the working tree; per-action gating via permission modes and sandboxing; commits/PRs on request.
- **Cloud/async agent** — runs on vendor-managed or ephemeral infrastructure; triggered by prompts, issue assignments, mentions, buttons, or automations; delivers pull requests; per-action approval replaced by environment isolation plus PR review.
- **IDE-embedded agent mode** — the agent lives inside the human's editor as one mode among assistant features (chat, autocomplete); shares the editor's terminal and diff tooling.
- **Autonomous "AI software engineer" positioning** — the same structure marketed as a team member: ticket-level delegation, session workspaces with embedded IDE/browser, take-over interaction; typically cloud-only.
- **Self-hosted / enterprise deployment** — agents run on organization-operated runners or containers; admin policy, model access control, audit, and usage metrics layered on top.
- **Automated/scheduled agent** — the same loop triggered by schedules, events, or CI, used for triage, dependency upgrades, and routine maintenance.

A variant should remain a **Variant**, not become a separate Type, unless it changes users, core objects, workflow, or rules in a way the Core Model no longer describes.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| AI Coding Assistant | closest sibling | the assistant helps a human who performs each step (suggestions, answers, single-shot edits); the agent performs the multi-step loop itself. Boundary test: who holds the execution loop |
| AI Software Engineering Agent | probable alias/variant | "AI software engineer" is a positioning of the same core structure (task → autonomous loop → reviewable changes) emphasizing ticket-level delegation and team-member framing; not a distinct structure on current evidence |
| Code Editor / IDE | adjacent bundle | the editor's primary object is the file the human edits; the agent's primary object is the delegated task and it can run with no editor present. IDEs with agent features bundle two Types |
| Agent Development Platform | different primary job | its users build agent software (SDKs, orchestration, tool wiring); the coding agent's users delegate coding work to a finished agent. They meet where a coding agent exposes an SDK |
| Code Review Platform | downstream / overlapping task | review adjudicates changes from anyone; the coding agent produces changes. Agent-as-reviewer is a task variant, not the Type |
| Issue Tracker | trigger surface | assigning an issue to an agent delegates work; the tracker's object is the issue workflow, not the executed task loop |

The boundary with the **AI Coding Assistant** is the most important one, because vendors ship both structures in a single product line and the frontier between them is an autonomy gradient, not a wall. The structural test — can the product complete an end-to-end task unattended and hand back a diff? — separates exercising the agent structure from exercising the assistant structure.

## Representative Products

- **Claude Code** (Anthropic) — terminal-first agentic coding tool; local execution by default; also usable from IDEs, desktop, web, chat, and CI.
- **GitHub Copilot coding agent** (GitHub) — platform-embedded asynchronous agent; works in ephemeral GitHub-powered environments; delivers pull requests on GitHub.
- **Codex** (OpenAI) — coding agent delivered through ChatGPT, an IDE extension, and a CLI; cloud environments and parallel agents.
- **Cursor** (Anysphere) — IDE-native coding agent; interactive agent with plan mode, checkpoints, and run-mode/sandbox controls; cloud agents for background work.
- **Devin** (Cognition) — autonomous cloud agent positioned as an "AI software engineer"; session workspace with embedded IDE, shell, and browser; take-over interaction.

The Core Model was checked across local-first, cloud/async, IDE-embedded, and autonomous-positioned forms to avoid over-fitting to any single substrate or deliverable convention.

## Sources

Research date: **2026-09-06**

Primary official documentation:

- Claude Code — Overview; How Claude Code works — https://code.claude.com/docs/en/overview , https://code.claude.com/docs/en/how-claude-code-works
- GitHub Copilot coding agent — About Copilot cloud agent; Using Copilot cloud agent on GitHub — https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent , https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/use-cloud-agent-on-github
- Codex — product page — https://openai.com/codex/
- Cursor — Agent overview; Run Modes — https://cursor.com/docs/agent/overview , https://cursor.com/docs/agent/security/run-modes
- Devin — Introducing Devin; Devin session tools — https://docs.devin.ai/get-started/devin-intro , https://docs.devin.ai/work-with-devin/devin-session-tools

> Sourcing limitation: the Codex developer documentation (developers.openai.com/codex/) returned HTTP 403 on 2026-09-06 and could not be fetched. Codex observations therefore rely on the official product page (positioning level) only; no precise operational claims about Codex are made in this document. Precise single-product figures (for example, documented session-time limits) are intentionally kept in the Research Notes rather than stated here.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, rejected findings, and the historical/market-sample breadth check are recorded in the paired Research Notes.
