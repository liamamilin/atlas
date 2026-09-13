# AI Software Engineering Agent

## Overview

An **AI Software Engineering Agent** is an application in which software-engineering work is delegated to an AI that operates as an autonomous member of the engineering team: it receives tasks through the team's own channels — prompts, tickets, chat threads — executes each task end to end in its own working environment, and delivers the result as changes the team reviews through its normal workflow.

The defining structure is small:

```text
Delegated engineering task (from a prompt, ticket, or chat thread)
└── Autonomous multi-step execution
    (the agent plans, uses tools, observes results, adjusts — no human action per step)
    └── in its own working environment, over the team's real codebase
        └── delivering reviewable changes
            (a diff, branch, or pull request the team accepts, modifies, or rejects)
```

This is the same defining structure as the **AI Coding Agent**. "AI software engineer" is the market positioning of that structure when the emphasis falls on the team-member operating model: the agent as a colleague with its own environment, reachable where the team already works, handling whole engineering tasks — tickets, migrations, reviews, documentation — rather than single edits. On current evidence the two names describe one Application Type; this document covers the team-member positioning cluster from its own lens, and the alias relationship is recorded for taxonomy review.

Everything commonly associated with current products in this category — cloud session workspaces, embedded IDEs and browsers, chat-channel presence, ticket integration, org-wide automation dashboards — is widespread but is not what makes a product an instance of this Type. A research prototype that takes a GitHub issue and autonomously fixes it in a local sandbox satisfies the defining core with none of that furniture.

## Users & Context

The primary users are **software engineers and engineering teams** with work that is well-defined enough to hand to an agent: backlog tickets, bug reports, incremental features, test writing and repair, migrations and framework upgrades, documentation upkeep, pull-request review, codebase questions.

The relationship between the team and the application is a **delegation relationship between colleagues**, and it changes what people do:

- **Before the run**: an engineer frames the task — goal, constraints, completion criteria — and often does so inside the tools the team already uses (a ticket, a chat thread, a prompt box), rather than in a separate workflow.
- **During the run**: the engineer monitors progress, answers questions, and can redirect or take over — pausing the agent, working in its environment directly, then resuming it and telling it what changed.
- **After the run**: the team reviews the delivered changes through its normal review workflow (diffs, pull requests) and merges, revises, or discards. The agent's output remains a proposal until a human accepts it.

Secondary users: **team leads and administrators**, who configure what the agents may access, which autonomy levels and models they use, and how they connect to the organization's repositories, tickets, and chat; and **teammates**, who interact with an agent's output through the same channels they use with human colleagues — commenting on its pull requests, tagging it in a thread, reading its status updates.

Typical contexts: a team's issue tracker and chat workspace (where delegation and status happen), the agent's own working environment (cloud or local), and the code-hosting platform where the work lands for review. The same structure serves an individual developer on a laptop and an organization running a managed fleet of agents; what changes is the substrate and the governance.

## Core Model

### The Defining Core

```text
Delegated engineering task
└── Autonomous multi-step execution
    └── Real project environment
        └── Reviewable changes
```

Four properties. If any one is removed, the product is no longer recognizable as an AI software engineering agent:

- **Task delegation as the unit of input.** The team hands over a goal — "fix this ticket," "upgrade this framework," "write tests for this module and make them pass" — not a sequence of editing steps. Input is a natural-language task, optionally enriched with an issue, a screenshot, an error log, or a chat thread. Without this, the product is an assistant or a build tool.
- **Autonomous multi-step execution.** The agent itself decides and performs the sequence of actions — gather context, take action, verify results — chaining many steps and course-correcting from what it observes, with no human action per step. Without this, it is a suggestion engine or a scripted pipeline.
- **Real project environment.** The agent acts on the team's actual codebase — files, dependencies, runnable toolchain — inside a working environment provisioned for it, where actions have real, inspectable effects. Without this, it is a chatbot producing code text with no ground truth.
- **Reviewable changes as the deliverable.** The work culminates in a changed project state the team can inspect — a diff, commits on a branch, a pull request — and accept, modify, or reject. The human checkpoint on output is part of the Type's contract. Without this, it is unreviewed automation, not an engineering tool.

### The Team-Member Operating Model

What distinguishes this positioning from a bare coding agent is not a new object but a coherent operating model around the same core. Mature products in this cluster commonly implement it as:

- **Delegation through the team's own channels.** Tasks arrive where work already lives: a ticket assigned to the agent, a chat mention, a message in a thread about a bug. The agent joins existing conversations rather than demanding a separate intake process.
- **Its own working environment.** The agent works in a provisioned environment — commonly a cloud machine with the repositories loaded — equipped with the tools a developer would use: a shell, an editor, a browser. The team can watch this environment and, when needed, step into it.
- **Status communication.** The agent reports progress back into the team's channels: replies in the thread that started the task, status indicators (working / blocked / done), notifications on completion, and a log of what it did. Some products give each task its own dedicated chat channel with the pull requests attached.
- **Take-over.** A human can stop the agent and work in its environment directly — editing code, running commands, completing login steps the agent cannot — then resume the agent and tell it what changed.
- **Side questions.** Teammates can ask the agent questions about its ongoing work without interrupting it; answers come from reading the codebase, not from modifying the run.
- **Delivery through the normal review workflow.** The agent's work lands as pull requests or reviewable diffs and is iterated on through the same comment-and-revise loop used for human contributions.

### Capabilities Shared by Mature Products

A typical modern product carries most of these capabilities. They are not what makes the product an AI software engineering agent, but they make it practical:

- **Tool set** — shell/command execution, file reading and editing, codebase search, web and documentation access, and commonly browser automation for testing the software it builds.
- **Verification behavior** — running tests, builds, and linters, and treating "the checks pass" as part of the task. Delegation guidance commonly asks users to frame tasks with verifiable completion criteria.
- **Sessions with progress logs** — each task runs as a monitorable session with a unified log of commands, edits, and agent activity.
- **Steering** — interrupting the agent, queueing corrections, or sending follow-ups that take effect at its next step, without restarting the run.
- **Persistent project instructions** — repository-level instruction files and/or learned environment configurations that shape every session: coding standards, verification commands, setup.
- **VCS integration** — branches, commits, and pull requests; asynchronous forms make the pull request the deliverable and route iteration through its comments.
- **Extensibility** — connections to external tools and services (commonly via an open tool-integration protocol), reusable skills or playbooks, lifecycle hooks, sub-agents.
- **Parallel execution** — multiple concurrent agent sessions, isolated via separate working copies or separate machines.
- **Autonomy controls** — an explicit layer bounding what the agent may do without asking: approval settings, sandboxing, trust boundaries over files and network, administrator policy.
- **Multiple entry surfaces** — the same agent reachable from a web app, a CLI, an IDE, chat, an issue tracker, or an API.

### One Structure, Many Implementations

The Core Model is written in conceptual terms. The Variants section enumerates how specific implementations realize each concept.

```text
Concept:            Delegated task input
Implementations:    typed prompt, ticket assignment, chat mention,
                    scheduled or event-triggered automation

Concept:            Real project environment
Implementations:    vendor-managed cloud machine, local working directory,
                    container or VM backend, research sandbox

Concept:            Reviewable changes
Implementations:    pull request with review request, working-tree diff,
                    commits on a branch

Concept:            Status communication
Implementations:    chat-thread replies, per-task channels with status chips,
                    notifications, session progress logs
```

A reader who has only seen one form — for example, a cloud agent that lives in a chat channel — should still be able to recognize a command-line agent working on a local repository as the same Type from the Core Model.

## How It Works

### The delegation loop

The defining workflow runs end to end like this:

```text
Frame the task
→ an engineer states a goal with completion criteria
  (a ticket, a chat message, a prompt — often with attached context:
   the issue, the error log, the relevant links)

Prepare the environment
→ the product provisions a place for the agent to work:
   a cloud machine or local environment with the repositories,
   dependencies, and toolchain loaded

Run the agentic loop
→ gather context: search and read the codebase, consult instructions
→ take action: edit files, create files, run commands
→ verify results: run tests / builds; check behavior
→ adjust: course-correct from what was learned; repeat until done
   (the human may steer, answer questions, or take over at any point)

Deliver and communicate
→ changes land as a pull request or reviewable diff
→ the agent reports status back into the team's channels

Human review and iteration
→ the team inspects the changes through the normal review workflow
→ revision requests become follow-up messages or PR comments
→ the team merges, discards, or takes the work over manually
```

### The team-channel form

When the agent is integrated with the team's chat and ticket systems, delegation and status flow through ordinary collaboration. An engineer tags the agent in a thread about a bug; the agent starts a session, replies in the thread, and works. The thread and the session stay synchronized — messages in either place reach the other. Some products give the session its own dedicated channel, named after the task, with a live status indicator and the pull requests it opens attached as links. Questions can be asked alongside the run without interrupting it; the agent answers from the codebase while the work continues.

### Take-over and side questions

Two interaction patterns run alongside the main loop:

- **Take-over**: the human stops the agent and uses its environment directly — the same shell, editor, and browser the agent was using — then resumes the agent and tells it what changed. Products differ in how literal this is (an embedded IDE inside the session workspace, a diff shown before changes are applied, a shared terminal); the pattern — pause, intervene, resume with context — is common across the cluster.
- **Side questions**: read-only question channels about the ongoing work, answered by searching and reading the codebase, without the ability to edit or run anything.

### Scaling to team-wide automation

Beyond individual delegated tasks, mature products let teams turn repeated engineering work into persistent automations: scheduled or event-triggered runs that triage incoming tickets, review pull requests, keep documentation current, or respond to incidents. At organizational scale this becomes a managed layer over the same session core — dashboards tracking which stages of the delivery lifecycle have automation coverage, metrics on tickets processed and pull requests merged, and administrative control over what agents may access. The unit of work underneath remains the delegated task executed in a session.

### Core vs Common vs Optional

**Defining core** — without these, not an AI software engineering agent:

- task delegation as the unit of input
- autonomous multi-step execution
- real project environment
- reviewable changes as the deliverable

**Standard capabilities** — present in most modern products:

- tool set (shell, files, search, web, browser)
- verification behavior (tests/builds/CI as completion criteria)
- sessions with progress logs
- steering and take-over
- persistent project instructions
- VCS / pull-request integration
- extensibility (external tools, skills, hooks, sub-agents)
- parallel execution
- autonomy controls
- team-channel integration and status communication
- multiple entry surfaces

**Common variants** — depend on substrate, scale, and positioning:

- execution substrate (cloud machine / local / container / self-hosted)
- team-channel depth (dedicated per-task channels vs simple thread sync vs connectors)
- org governance (admin policy, access controls, usage reporting, budgets)
- org-wide SDLC automation layers
- agent specialization (task modes, sibling agent types)
- open-source vs proprietary distribution

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product, and a given product may expose only a subset.

### Session workspace

The agent's room: where one delegated task lives.

- the conversation with the agent, a unified progress log of its steps, and its working tools — commonly a shell view, a code editor view, and a browser view into its environment
- typical information: current step, commands and outputs, files changed, status (working / blocked / done), elapsed effort
- primary actions: send messages, steer or redirect, take over (stop the agent and use the tools directly), resume with context, open the resulting changes

### Team chat surface

Where delegation and status meet the team's everyday collaboration.

- the agent present as a mentionable participant in channels and threads
- typical information: the task thread, the agent's in-thread replies, status indicators, links to the session and its pull requests
- primary actions: mention the agent with a task, reply to steer it, ask side questions, mute or end the session

### Ticket / issue surface

Where backlog work is handed over.

- the team's issue tracker with the agent available as an assignee
- typical information: the ticket's description, acceptance criteria, linked repository
- primary actions: assign the ticket to the agent, follow the resulting session, review the delivered pull request

### Review surface

Where the deliverable is judged.

- the diff or pull request the agent produced, in the product's own UI or the standard code-review workflow
- typical information: changed files, per-file diffs, verification results, the agent's summary of what it did and why
- primary actions: approve, request changes (which become follow-up instructions), comment, merge, discard

### Management surface (team/organization)

- lists of agent sessions across the team; configuration for repositories, connectors, autonomy levels, and models; automation coverage and outcome metrics; administrative policy

## Important Rules / Behaviors

### The agent's output is a proposal

Everything the agent produces — edits, commits, pull requests — remains reviewable and reversible until a human accepts it. The work lands on a branch or in a reviewable diff, never directly on the mainline; merging, not editing, is the moment the work is accepted. This is the Type's core safety contract: autonomy in execution, human authority over acceptance.

### Autonomy is bounded by an explicit control layer

Products ship a control layer between "ask before everything" and "do everything": approval settings, allowlists, sandboxing, and administrator policy. A structural pattern recurs across the cluster: **agents running on the team's own machines gate individual actions** (asking before risky commands, restricting file and network access), while **agents running in their own isolated environments gate at the boundary** — the isolation replaces per-action approval, and the human gate moves to the output (review the changes, approve the checks). Either way, the human decides what the agent may do unattended.

### The agent works on a copy, not the mainline

Whether by branch, working copy, or disposable environment, the agent's changes are isolated from the primary line of development until review.

### Verification is part of the task

"Done" conventionally means the checks pass, not merely that code was written. Products run tests, builds, and linters as part of the loop, and delegation guidance explicitly asks users to frame tasks with verifiable completion criteria. Visual verification (the agent testing the software it builds in a browser) extends this to user-facing changes.

### Status flows back to the team

Unlike a tool that waits to be consulted, the agent communicates: replies in the thread that started the task, status indicators, completion notifications, and logs of what it did. This is what makes the team-member framing operational rather than cosmetic.

### Sessions are durable units of work

A session's transcript and progress log persist after the run; follow-up requests on the same deliverable commonly reuse the context of earlier runs. Manual changes made during a take-over are communicated back to the agent when it resumes.

### Scope and resource limits exist

Products commonly scope a run — to a repository, a branch, a task — and unattended runs may be bounded by execution limits. The exact limits are product policy; the structural point is that runs are deliberately scoped rather than open-ended.

### Persistent instructions shape every run

Repository-level instruction files and learned environment configurations are read at session start. They are the mechanism by which team standards survive across tasks and across agents.

## Variants

The Type is implemented in several recognizable forms. Common variants:

- **Cloud team-member agent** — the agent works in vendor-managed cloud environments provisioned per task; delegation and status flow through the team's chat and ticket systems; the session workspace exposes the agent's shell, editor, and browser for monitoring and take-over.
- **Local-first agent with cloud option** — the same agent runs in a CLI or desktop app on the developer's machine, showing diffs before applying changes, with cloud machines available for background or parallel work.
- **Org-wide SDLC automation platform** — the same session core wrapped in an organizational layer: automations across triage, code review, QA, documentation, and incident response, with coverage dashboards and enterprise governance.
- **Open-source self-hosted stack** — the agent client, execution backends, and automation server as open components the organization runs itself, choosing where agents execute and what they may access; commercial cloud and enterprise tiers on top.
- **Research prototype** — the minimal form: a language model driving tools against real repositories to resolve issues, evaluated on benchmarks; no team channels, no session workspace, no governance layer.

A variant should remain a **Variant**, not become a separate Type, unless it changes users, core objects, workflow, or rules in a way the Core Model no longer describes.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| AI Coding Agent | same Type — alias/variant relationship recorded | the defining structure is identical (task → autonomous loop → real project environment → reviewable changes); "AI software engineer" names the team-member positioning of it. This document covers that positioning cluster from its own lens |
| AI Coding Assistant | closest sibling on the autonomy gradient | the assistant helps a human who performs each step (suggestions, answers, single-shot edits); the agent performs the multi-step loop itself. Boundary test: who holds the execution loop |
| Agent Orchestration Platform | different primary job | its users build and coordinate agent software (SDKs, orchestration, tool wiring); this Type's users delegate engineering work to a finished agent. They meet where a product ships both (an agent SDK beside an agent client) |
| Issue Tracker | trigger surface | assigning a ticket to the agent delegates work; the tracker's object is the issue workflow, not the executed task loop |
| Code Review Platform | downstream / overlapping task | review adjudicates changes from anyone; this Type produces changes. Agent-as-reviewer is a task variant, not the Type |
| Code Editor / IDE | adjacent bundle | the editor's primary object is the file the human edits; the agent's primary object is the delegated task, and it runs with no editor present. An embedded IDE inside the agent's workspace is a take-over surface, not the Type |

The boundary with the **AI Coding Agent** is the defining relationship for this leaf: the structures are the same, and the distinction is the operating model emphasized — the agent as a team member reachable through the team's own channels. The boundary with the **AI Coding Assistant** is who holds the execution loop; vendors ship both structures in single product lines, and the frontier between them is a gradient, not a wall.

## Representative Products

- **Devin** (Cognition) — the canonical "AI software engineer": cloud session workspaces with embedded shell, IDE, and browser; delegation and status through Slack/Teams and Linear/Jira; take-over interaction; CLI and API.
- **Factory (Droid / Software Factory)** — commercial agent platform: local CLI/desktop sessions with diff-before-apply review, scaling to org-wide SDLC automations and enterprise fleet governance.
- **OpenHands** (All Hands AI / community) — open-source AI-driven development stack: browser client over selectable backends (local, container, VM, cloud), agent SDK, automations; commercial cloud and enterprise tiers.
- **SWE-agent** (Princeton & Stanford researchers) — research prototype: a language model autonomously fixing real GitHub issues with tools; benchmark-driven; the minimal form of the cluster.

The Core Model was checked across cloud team-member, local-first, open-source self-hosted, and research-prototype forms to avoid over-fitting to any single substrate or positioning.

## Sources

Research date: **2026-09-10**

Primary official documentation:

- Devin — Introducing Devin; Devin session tools; Slack integration — https://docs.devin.ai/get-started/devin-intro , https://docs.devin.ai/work-with-devin/devin-session-tools , https://docs.devin.ai/integrations/slack
- Factory — Docs home; Software Factory overview; Factory App quickstart — https://docs.factory.ai/ , https://docs.factory.ai/docs/software-factory/overview , https://docs.factory.ai/docs/factory-app/quickstart
- OpenHands — Introduction; Agent Canvas overview — https://docs.all-hands.dev/ , https://docs.openhands.dev/openhands/usage/agent-canvas/overview
- SWE-agent — Getting started — https://swe-agent.com/latest/

> Sourcing limitation: the docs of one additional sampled candidate (a consumer-tier async coding agent) timed out twice on 2026-09-10 and were abandoned; the consumer/individual tier of this cluster is therefore under-evidenced, and no claims in this document depend on it. Precise single-product figures and vendor-specific mechanics (mode keywords, channel behaviors, stage taxonomies, benchmark claims) are intentionally kept in the Research Notes rather than stated here.

Detailed evidence, product-by-product observations, the cross-product comparison, rejected findings, and the structural breadth check are recorded in the paired Research Notes.
