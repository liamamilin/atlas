# Agent Tool / Computer-use Platform

## Overview

An **Agent Tool / Computer-use Platform** provides executable tools and managed execution environments that AI agents invoke at runtime. An agent's reasoning model can only produce text and decisions; this class of platform supplies the "hands": cloud browsers the agent drives, sandboxed computers where the agent runs code, virtual desktops the agent controls through a virtual mouse and keyboard, and managed tool services — web search, page fetching, API-to-tool conversion — that the agent calls. The platform executes each action outside the model, in an environment it operates or designates, and returns the observations (page state, screenshots, code output, extracted data) that the agent needs to decide its next step.

The defining structure is small:

```text
Agent (model-driven loop, owned elsewhere)
   ↓ invokes
Tool (callable capability addressed to the agent)
   ↓ executed by
Platform-operated environment (managed, isolated, session-based)
   ↓ returns
Observation → feeds the agent's next decision
```

The defining core is the invocation → execution → observation triangle. Everything commonly associated with the category — cloud browser farms, code sandboxes, screen-level "computer use", credential vaults, session replay — is a realization of that triangle, not a replacement for it.

Two boundaries follow. This is **not** the agent itself: agent development platforms define and run the reasoning loop, and many of them bundle tool services as optional add-ons. And it is **not** scripted automation: robotic process automation executes human-designed, deterministic sequences, while here a model decides each action at runtime from live observations.

## Users & Context

The primary user is a **developer building AI agents**, who integrates the platform's tools into an agent's execution loop — connecting a cloud browser or code sandbox to an agent framework, wiring tool calls, and handling the observations that come back.

A second audience is the **low-code maker**, who configures tools inside an agent-building platform: describing in natural language what the tool should do on a computer, selecting the execution model, and attaching credentials — without writing integration code.

Around both sits a governance circle: **security and platform teams** who define what tools may touch (website and application allowlists, network restrictions), where credentials live, and who gets consulted when a run needs human judgment; and **operations staff** who watch live sessions, review recordings, and debug failed runs.

The work context is always "behind the agent": during development, tools are tested through the platform's inspection surfaces; in production, every agent run creates and consumes environments — browser sessions, sandboxes, desktop machines — that must be isolated, observed, and cleaned up.

## Core Model

### The Defining Core

```text
Agent-invocable tool
└── Platform-executed action (managed environment or service)
    └── Observation returned to the agent loop
```

Three properties. If any one is removed, the product is no longer recognizable as this Type:

- **Agent-invocable tool surface** — capabilities exposed as callable interfaces that a model-driven agent invokes at runtime, with the model choosing each action from what it observes. The surface may be an SDK object, a REST session API, a managed tool resource, or a natural-language tool configuration inside a low-code platform. Without this property the product is generic cloud infrastructure (browser or VM hosting) or human-scripted automation.
- **Platform-executed action in a managed environment** — the platform, not the model and not the end user's hands, performs the action in an environment it operates or designates: an isolated cloud browser session, a sandboxed virtual machine, a virtual desktop, or a managed service endpoint. Without this property the product is an SDK library or a model API alone.
- **Observation returned into the agent loop** — the result of the action (rendered page state, screenshot, command output, extracted data) flows back so the agent can decide its next step. Without this property the product is a fire-and-forget actuator, not a tool.

### Standard Capabilities of Mature Products

These make the core practical; they are not what makes the product a tool platform:

- **Execution environment as a session** — the dominant shape of an environment tool is a session: a managed runtime instance (browser, sandbox, desktop) created on demand, driven for a bounded lifetime, then destroyed. Sessions are isolated from the caller's systems (containerized or VM-based) and from each other.
- **Session lifecycle machinery** — creation with configuration (region, screen size, network posture, identity), interaction, and termination by explicit stop, timeout, or time-to-live expiry. Ephemeral-by-default is the norm; some products add pause/resume with full state preservation, or persistent contexts that carry login state across sessions.
- **Execution observability** — live view of what the agent is doing, session recording and replay (actions, screen changes, console and network events), and logs, so humans can debug and audit agent behavior.
- **Human-oversight surfaces** — watch-only live streams, interactive takeover of a running session, test panels that show the tool's reasoning step by step, and supervision gates that route potentially harmful situations to a designated reviewer.
- **Security boundary controls** — restrictions on what tools may touch (website and application allowlists, network modes, HTTPS enforcement), and credential custody kept separate from the agent's reasoning (stored sign-ins, vaults, maker-vs-end-user identity).
- **Tool catalog and integration layer** — built-in capability tools (web search, page fetching, code interpretation) alongside environment tools; SDKs and adapters for popular agent and automation frameworks; protocol compatibility (notably MCP) so tools can be reached from any compliant agent.

### One Structure, Many Implementations

The core model is conceptual. Specific products realize each piece differently:

```text
Concept:            Tool surface
Implementations:    SDK objects, REST session APIs, managed tool resources,
                    natural-language tool forms in low-code platforms

Concept:            Execution environment
Implementations:    cloud browser instance, code-execution sandbox,
                    virtual Linux/Windows desktop, customer-designated machine,
                    managed search/fetch/API service

Concept:            Observation
Implementations:    page state via automation frameworks, screenshots,
                    command output and streams, extracted text or JSON
```

A reader who has only seen one realization — say, an agent clicking through a remote browser — should still be able to recognize a code sandbox or a search tool as the same Type from the core triangle.

## How It Works

### Connect tools to the agent

The developer (or maker) first makes tools available to the agent's loop. Common patterns across the researched market:

- call the platform's API/SDK directly from the agent's code
- register the platform's tools with an agent framework through an adapter
- expose or consume tools through a standard protocol (MCP)
- in a low-code platform, add the tool to the agent from a catalog and configure it with a name, a description the agent uses to decide when to use it, an execution model, and natural-language instructions

### Start an execution environment

For environment tools, each unit of work begins by starting a session: an isolated browser instance, a fresh sandbox VM, or a virtual desktop. The session is configured at creation — where it runs, its screen and network posture, what identity it presents, whether it records. Sessions are typically created on demand, per task or per user interaction, and multiple sessions can run concurrently.

### The agent loop drives execution

Once the environment is live, the agent's model decides actions and the platform executes them. The canonical computer-use loop, as documented across the sampled products:

```text
capture the current state (screenshot / page snapshot)
→ model decides the next action
→ platform executes it (click, type, scroll, navigate, run code)
→ capture the new state
→ repeat until the task is complete
```

The same loop governs code sandboxes (run code → read output → run more code) and capability tools (search → read results → fetch a page → extract data). The platform never decides; it executes and reports.

### Oversee, monitor, record

While execution runs, humans can watch through live-view streams, interact directly with the session if needed, or receive escalation requests when the tool detects potentially harmful instructions. Every session can leave an audit trail — recorded actions, screen changes, console and network events — replayable afterward for debugging and compliance.

### Terminate and clean up

Sessions end by explicit stop, by timeout, or by time-to-live expiry, and their resources are reclaimed. The default posture is ephemeral: state disappears with the session unless the product explicitly offers persistence (pause/resume, persistent browser contexts, or files saved to customer storage).

### Capability tiers

**Defining core** — without these, not this Type:

- agent-invocable tool surface
- platform-executed action in a managed environment
- observation returned into the agent loop

**Standard capabilities** — present in most mature products:

- session-based environments with lifecycle management
- isolation of execution
- execution observability (live view, replay, logs)
- human-oversight surfaces
- security boundary controls and credential custody
- framework/protocol integrations and built-in tool catalogs

**Optional / variant** — depends on product and segment:

- screen-level GUI control (computer use proper)
- pause/resume state preservation or persistent contexts
- serverless deployment of agent scripts onto the platform's infrastructure
- customer-designated (rather than vendor-operated) execution machines
- consumption-based billing meters (per session, per step, or per credit)

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Tool API / SDK

The primary developer surface: programmatic creation and control of sessions and tools.

- typical information: session/environment identifiers, connection URLs, configuration options, execution results
- primary actions: create a session or tool, execute actions, retrieve observations, terminate

### Live view / session inspector

The human-oversight surface for running and past executions.

- typical information: real-time stream of the environment, recorded replays with timelines, action logs, console and network events
- primary actions: watch, interact with or stop a live session, open a replay, inspect logs

### Dashboard

The management surface over the estate of sessions and tools.

- typical information: running and completed sessions, usage and performance metrics, recordings, API credentials
- primary actions: find a session, open its inspector, manage keys and settings

### Tool configuration surface (low-code form)

In platforms aimed at makers, the tool is configured through a form rather than code.

- typical information: tool name and description, chosen execution model, natural-language instructions, dynamic inputs, target machine, credentials, access restrictions
- primary actions: add/configure the tool, test it with a step-by-step reasoning log and live preview, save and publish

### Test experience

A dedicated authoring-time surface where a configured tool can be run once and observed: the tool's reasoning and actions logged step by step beside a live preview of the machine or environment, with an immediate stop control.

## Important Rules / Behaviors

### Sessions are ephemeral and bounded

Environments exist for a bounded lifetime. Timeouts and time-to-live limits terminate sessions automatically; state is not preserved unless the product explicitly offers persistence. Agents must therefore treat each session as fresh, and integrations must re-establish any needed state (sign-ins, files) per session or use explicit persistence features.

### Isolation is the default security posture

Execution happens in environments separated from the caller's systems — containerized or VM-based — and sessions are isolated from each other. This is what makes it acceptable for an agent to run arbitrary code or drive arbitrary websites: the blast radius is the session, not the host.

### Access control binds the agent's actions

Allowlists of websites, domains, or applications constrain what the tool may do; network modes and HTTPS enforcement constrain where it may connect. Allowlists are one layer in a defense that, across the researched products, also includes dedicated or hardened execution environments and least-privilege accounts.

### Credentials are custody-separated from reasoning

Sign-in secrets live in credential stores (platform-internal or customer-provided vaults), scoped per website or application, and are used by the platform at execution time — the agent's model never handles the raw secret. Whose identity acts (the maker's or the interacting end user's) is an explicit configuration choice with governance consequences.

### Human oversight can gate execution

Products provide at least one mechanism by which a human can watch, interrupt, or review execution — live takeover, stop controls, or supervision gates that route a run to a designated reviewer before it proceeds.

### The platform returns observations, not conclusions

The tool layer reports raw state — screenshots, page content, command output — and the model interprets it. This division of labor is why the tool layer stays model-agnostic: the same browser or sandbox serves agents built on any foundation model.

## Variants

- **Cloud-browser platforms** — managed browser sessions as the core product, often with identity/proxy/captcha machinery and lighter-weight search/fetch tools beside them; consumed via automation frameworks or agent SDKs.
- **Code-sandbox platforms** — on-demand VMs or containers where agents execute generated code, process data, and run tools; popular both for conversational agents and as the execution layer inside coding workflows.
- **Computer-use / virtual-desktop platforms** — full GUI environments (Linux or Windows desktops) driven through virtual mouse, keyboard, and screen capture; the flagship form of "computer use", used where no API exists for the target system.
- **Multi-tool suites inside agent platforms** — browser, code interpreter, and API-to-tool gateways offered as modular services beside an agent runtime; the bundled form of the same layer.
- **Model-vendor built-in tools** — execution tools shipped inside a model API; same core triangle, delivered as part of the model product.
- **Low-code maker tools** — the same machinery exposed as configurable tool forms inside business agent builders, with natural-language instructions and governance controls.
- **Execution-locus variants** — vendor-operated cloud runtimes, customer-designated machines (e.g., a managed Windows machine for desktop automation), or self-hosted open-source substrates.

A variant remains a variant unless it changes the core triangle; all of the above keep agent-invocation, platform-executed action, and returned observation intact.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Agent Development Platform | defines and runs the agent's reasoning loop; this Type provides the executable capabilities that loop calls. Agent platforms commonly bundle tool services as optional add-ons, but a tool platform has no agent builder |
| Agent Orchestration Platform | coordinates multiple agents at runtime; this Type executes single actions/environments for one agent at a time |
| Robotic Process Automation Platform | also acts on GUIs, but executes human-designed deterministic scripts triggered by schedules; here the model decides each action at runtime from observations |
| Desktop Automation Application | personal-computer scripting for a human user's own tasks; no model-driven agent loop and no managed multi-tenant environments |
| Browser Compatibility Testing Platform | same cloud-browser substrate, but invoked by human-written test suites asserting expected behavior, not by agents accomplishing tasks |
| AI Coding Agent | a finished agent product that produces code; this Type is substrate such agents may call (e.g., sandboxes for running and testing code) |
| Cloud IDE / Dev Container | managed environments operated for human developers to enter and work in; here environments are created and driven by agents |
| Model API Platform | provides model inference (tokens); this Type provides execution of actions; the two meet at tool/function calling and are deliberately model-agnostic on this side |

The boundary with the Agent Development Platform is the most important one, because the market bundles the two constantly. The structural test: remove agent definition and the runtime loop — a tool platform survives (standalone browser/sandbox infrastructure exists with no agent builder); remove the tool environments — an agent development platform survives (frameworks exist that ship no managed environments).

## Representative Products

- Amazon Bedrock AgentCore (Browser, Code Interpreter) — modular tool services beside an agent platform
- Microsoft Copilot Studio (computer use) — a natural-language computer-use tool inside a low-code agent platform
- E2B — open-source sandboxes (code execution and Linux desktops) for any agent
- Browserbase — cloud-browser infrastructure with sessions, search/fetch tools, and serverless browser agents

The core model was checked across hyperscaler, low-code, open-source, and specialist-infrastructure delivery forms to avoid over-fitting to any one packaging.

## Sources

Research date: **2026-09-06**

- Amazon Bedrock AgentCore — AgentCore overview: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html ; Browser: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-tool.html ; Code Interpreter: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-tool.html
- Microsoft Copilot Studio — Computer use: https://learn.microsoft.com/en-us/microsoft-copilot-studio/computer-use
- E2B — Documentation index: https://e2b.dev/docs ; Sandbox lifecycle: https://e2b.dev/docs/sandbox ; Computer use: https://e2b.dev/docs/use-cases/computer-use
- Browserbase — Introduction: https://docs.browserbase.com/introduction ; Create a browser session: https://docs.browserbase.com/platform/browser/getting-started/create-browser-session ; Getting started: https://docs.browserbase.com/welcome/getting-started ; Functions: https://docs.browserbase.com/platform/runtime/overview

> Sourcing limitation: official documentation for two model vendors' computer-use tool APIs (Anthropic, OpenAI) was unreachable from the research environment on 2026-09-06 (region block and HTTP 403). Their existence and general shape are evidenced indirectly through fetched third-party pages (a low-code platform's selectable execution-model table; an open-source platform's integration guide). No claims about those vendors' internal tool schemas, defaults, or pricing are made in this document. Precise operational numbers observed in fetched docs (session time limits, file-size ceilings, per-step billing rates, plan-tier caps) are deliberately excluded from this document and recorded in the Research Notes.
