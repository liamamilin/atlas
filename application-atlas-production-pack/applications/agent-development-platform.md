# Agent Development Platform

## Overview

An **Agent Development Platform** is a product whose primary job is to let users **define AI agents and run them**. An agent, in this context, is a persistent, configurable software unit that combines a reasoning model with instructions and a set of callable tools; when invoked, the platform executes a model-driven loop in which the agent interprets the task, decides the next step, calls tools or services, and iterates until the task is complete.

The defining core is small:

```text
Agent definition (identity + instructions + model + tools)
        ↓
Platform-run execution loop (model decides steps, invokes tools, iterates)
        ↓
Invocation surface (run / test / API / chat channel / trigger)
```

Everything else commonly associated with the category — memory, knowledge integration, guardrails, human-in-the-loop approval, multi-agent delegation, tracing, evaluation, managed deployment — is standard capability that mature products add around this core, not part of what makes the product an agent development platform.

The boundary against plain LLM application development is the ownership of the loop: with a model API, the developer owns control flow and issues each model call; with an agent development platform, the runtime carries the agent through multiple model turns and tool calls toward a goal.

## Users & Context

Three builder audiences appear across the market, and most products serve more than one:

- **Developers** — author agents in code with an SDK or framework, wire tools as functions or protocol endpoints, run agents locally, and deploy them as services.
- **Enterprise makers / IT** — author agents in a graphical low-code studio, connect them to company data and systems through connectors, and publish them to the channels where colleagues and customers already work.
- **Business users** — in some products, describe the agent they want in plain language and refine a generated draft, without touching code.

A fourth, operational role matters once agents are in production: **administrators** who inventory agents, control access, manage cost, and govern what agents may do.

Typical deliverables built on such platforms: customer-support and internal-help agents, workflow automation that reasons across systems, data-analysis and research agents, coding or document agents, and voice agents. The work environment is a development toolchain (IDE, CLI, web studio, cloud console) rather than an end-user surface; the agent's end users usually meet it elsewhere — in a chat channel, an application, or an API.

## Core Model

### The Defining Core

Four properties. If any one is removed, the product is no longer recognizable as an agent development platform:

- **Agent as a defined, persistent unit** — a named, configured artifact that holds its instructions, model binding, and tool set, survives between runs, and can be versioned and re-invoked. Without this, the product is prompt tooling or a model playground.
- **Tool / action integration** — the agent can invoke external functions, APIs, or services: it acts, rather than only generating text. Without this, the product is a chatbot or text generator.
- **Model-driven execution loop owned by the platform** — the runtime carries the agent through multiple model turns and tool calls toward a goal; the user does not hand-execute each step. Without this, the product is model-call plumbing or a conventional workflow engine with no reasoning core.
- **Invocation surface** — a way to run, test, or invoke the agent: a local run command, an API endpoint, a chat channel, or a trigger. Without this, it is an agent designer, not a development platform.

### Standard Capabilities

Mature products commonly add the following around the core. They make agents practical and production-safe, but any of them can be absent and the product remains an agent development platform:

- **Session and conversation state** — threads or sessions that carry context across turns within a run.
- **Memory** — short-term working context during a task and long-term memory that persists across sessions; some products make memory stores shareable between agents.
- **Knowledge integration** — connecting data sources, knowledge bases, or grounding services so answers and decisions draw on private or fresh information.
- **Human-in-the-loop** — interrupts, approvals, action confirmations, and review steps that pause the loop until a person responds.
- **Guardrails and policy** — validation of agent inputs and outputs, and rules that gate which tools the agent may call under which conditions.
- **Multi-agent structure** — handoffs, subagents, delegation, and template workflows (sequential, parallel, looped) that compose agents into larger systems; inter-agent protocols are an emerging integration surface.
- **Tracing and observability** — a step-by-step record of the agent's reasoning and tool calls, inspectable during development and monitored in production.
- **Evaluation** — test sets, graders, and simulation of users or environments to score agent behavior before and after release.
- **Deployment targets** — managed runtimes, serverless or containerized hosting, or publication to chat channels.
- **Versioning and promotion** — versions or aliases that separate what is being tested from what production calls.
- **Governance** — agent inventory, role-based access, and cost management for organizations running many agents.

### One Structure, Many Implementations

The core is conceptual; products realize each piece differently:

```text
Concept:            Agent definition
Implementations:    code object (SDK) · visual configuration · natural-language description

Concept:            Tools / actions
Implementations:    annotated functions · MCP servers · OpenAPI specs ·
                    prebuilt connectors · flows attached as tools

Concept:            State
Implementations:    in-process sessions · pluggable session stores ·
                    platform-managed memory services · checkpoints

Concept:            Invocation
Implementations:    local run / CLI · API endpoint · chat channel publish ·
                    scheduled or proactive triggers
```

A reader who has only seen one implementation — say, a code-first framework — should still be able to recognize a low-code studio or a managed cloud service as the same Type from the core.

## How It Works

The typical lifecycle runs in six movements. Products differ in surface, not in sequence.

### 1. Define the agent

The user creates the agent unit and gives it its behavior:

```text
name the agent
→ write or describe its instructions (role, rules, tone, escalation)
→ bind a model
→ attach tools
```

In code-first products this is a constructor call; in low-code studios it is a form or a plain-language description that the platform turns into configuration.

### 2. Connect tools and knowledge

Tools are registered so the model can discover and call them: local functions with generated schemas, remote protocol endpoints, API specifications, prebuilt connectors to business systems, or entire flows packaged as tools. Knowledge sources are attached in parallel where the product supports them.

### 3. Run and test in a development surface

The user invokes the agent against sample tasks — a test chat, a local run command, a console — and inspects what happened:

```text
invoke agent with a task
→ platform runs the loop (model turn → tool call → model turn → …)
→ trace shows each step: reasoning, tool calls, outputs
→ user adjusts instructions, tools, or model and repeats
```

The trace is the primary debugging instrument: agent failures are usually diagnosed by reading the step-by-step record, not by reading code.

### 4. Evaluate

Before release, behavior is scored against test sets or simulated users and environments; regressions are caught by re-running evaluations after changes. Depth varies widely between products, from built-in tracing review to dedicated evaluation services.

### 5. Deploy

The agent is promoted to a runtime: a managed service endpoint, a container the user hosts, or publication to chat channels where end users already work. Versioning separates the tested definition from the one production invokes.

### 6. Operate

In production the platform (or its companion services) monitors runs, collects analytics, enforces guardrails on tool calls, and supports iteration — new versions and, in some products, controlled experiments comparing alternative agent configurations — under governance over who may change what.

### Core vs Common vs Optional

**Defining core** — without these, not an agent development platform:

- agent as a defined, persistent unit
- tool / action integration
- platform-run, model-driven execution loop
- invocation surface

**Standard capabilities** — present in most mature products:

- session state and memory
- knowledge integration
- human-in-the-loop controls
- guardrails / policy
- multi-agent composition
- tracing and observability
- evaluation
- deployment targets and versioning
- governance (inventory, access, cost)

**Variant / optional** — depends on product form and audience:

- authoring surface (code / low-code / natural language)
- model posture (single-vendor / model-agnostic / model routing)
- product form (library / managed service / modular infrastructure)
- agent embodiment (conversational / background-proactive / voice-realtime)
- deterministic-plus-agentic graph workflows
- optional tool services (browser runtime, code-interpreter sandbox, agent payments)

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Authoring surface

Where the agent is defined.

- code SDK in an IDE, or a graphical canvas, or a plain-language description box
- typical information: agent name, instructions editor, model selector, tool list, knowledge sources
- primary actions: create agent, edit instructions, attach/detach tools, configure model

### Test / playground surface

Where a draft agent is exercised.

- a conversation or task panel plus a step-by-step trace of the run
- primary actions: send a test task, inspect reasoning and tool calls, modify and re-run

### Trace / observability view

The record of what the agent actually did.

- per-step entries: model reasoning, tool invocations, inputs/outputs, errors, token usage
- primary actions: filter runs, open a step, compare runs, export telemetry

### Evaluation view

Where behavior is scored.

- test sets, grader definitions, run results against criteria, simulation controls
- primary actions: create test set, run evaluation, compare versions

### Deployment / configuration surface

Where the agent goes live.

- runtime or hosting target, environment and version selection, channel publication, access settings
- primary actions: deploy or publish, create version/alias, roll back, set permissions

### Administration surface

Where organizations govern agents at scale.

- agent inventory, ownership, access roles, cost and usage reporting
- primary actions: review agents, change access, manage policies

### Invocation endpoints

What the agent's consumers touch: an API endpoint, a chat channel entry, or an event/schedule trigger. The platform's own surfaces end here; the end-user experience belongs to the channel or application the agent is published into.

## Important Rules / Behaviors

### The loop is model-driven and platform-owned

The defining behavior: the runtime, not the user, advances the agent from step to step. The user steers through instructions, tools, and guardrails; termination is reached when the model judges the task complete, a step limit or policy stops it, or a human-in-the-loop gate pauses it. Exact stopping rules vary by product.

### Tools execute with the agent's authority

When an agent calls a tool, the action happens in the world — an API is called, a record changes, a message is sent. Mature products therefore surround tool execution with controls: confirmation prompts before sensitive actions, and restrictions on which tools may be called under which conditions; some products add agent-specific identity mechanisms so actions carry the right credentials. This is the main safety surface of the Type.

### Human-in-the-loop pauses are structural

Interrupts and approvals are not UI conveniences but execution states: the run suspends, its state is preserved, and it resumes when a person responds. Products differ in where such gates can be placed, but the pause-and-resume pattern is common.

### State outlives the run

Sessions, checkpoints, and memory persist beyond a single invocation. Long-running or interrupted tasks resume from stored state rather than starting over; memory can carry lessons across sessions.

### Tested and production definitions are separated

Changes to a live agent are managed through versions, aliases, or publish flows: production consumers keep calling a pinned definition until the operator promotes a new one. This mirrors release management in other software Types and is the standard answer to "the agent misbehaved after I changed its instructions."

### Deterministic and model-driven steps can be mixed

Many products allow hand-coded, fully predictable steps alongside model-driven agentic steps in the same agent. Teams use deterministic segments where reliability or auditability matters and agentic segments where flexibility matters.

## Variants

Common forms of the Type. A variant remains a variant unless it changes the core users, objects, or workflow so much that the core model no longer applies.

- **Open-source framework / library** — code-first; the developer runs the loop anywhere and owns hosting; the vendor's managed deployment is optional.
- **Model-vendor SDK** — a small-primitive SDK from a model provider; tightest integration with that vendor's models and APIs, with adapters for others.
- **Managed cloud agent service** — configuration-driven agents on a cloud platform; the provider operates the loop, memory, monitoring, and invocation; no infrastructure for the user.
- **Modular agent infrastructure** — a set of independent services (runtime, memory, tool gateway, identity, policy, registry, evaluation) that teams compose; can even serve as the substrate for other agent platforms.
- **Enterprise low-code studio** — graphical authoring plus natural-language generation; strong connector catalogs; publication to workplace chat channels; governance built in; often serves mixed developer/maker teams.
- **Embodiment variants** — conversational assistants, background/proactive agents that act on their own schedule or account, voice/realtime agents, and coding-style agents working in isolated workspaces.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| LLM Application Development Platform | adjacent, gradient | model calls and RAG applications where the developer owns control flow; here the platform owns an autonomous model-driven loop |
| Agent Orchestration Platform | overlapping sibling | in researched products, multi-agent composition is an in-product capability; a standalone orchestration platform would center on coordinating pre-existing agents at runtime rather than on agent definition |
| Agent Evaluation Platform | capability sibling | evaluation is a bundled standard capability here; a standalone product centers the evaluation lifecycle |
| Agent Observability Platform | capability sibling | tracing/monitoring is a bundled standard capability here; a standalone product centers production telemetry |
| Agent Tool / Computer-use Platform | capability sibling | tools and execution environments are standard capabilities here; a standalone product centers supplying them |
| RAG Development Platform | adjacent | centers building retrieval pipelines; knowledge integration here is one standard capability among many |
| AI Coding Agent | different object | a finished agent product used to produce code; this Type is the construction environment for agents of any kind (they meet where coding agents scaffold platform agents) |
| Enterprise AI Assistant | downstream | a deployed end-user assistant product; this Type is what builders use to produce and operate such assistants |
| AI Gateway / Model Routing Platform | adjacent infrastructure | routes model traffic; here model binding is configuration, not the product's job |
| Prompt Management Platform | adjacent | manages prompt assets; here instructions live inside the agent definition |
| AI Safety / Guardrail Platform | capability sibling | guardrails are a standard capability here; a standalone product centers enforcement across many AI systems |
| Robotic Process Automation Platform | historical neighbor | rule-based automation without a reasoning core; no model-driven loop, so a different Type |

The two most important boundaries: against **LLM Application Development** (who owns the loop) and against **Agent Orchestration** (definition of agents vs coordination of already-built agents). Both are gradients rather than walls, and vendors ship products that straddle them.

## Representative Products

- LangGraph (LangChain) — open-source orchestration framework and runtime for stateful agents
- OpenAI Agents SDK — model-vendor SDK with minimal primitives (agents, handoffs, guardrails)
- Amazon Bedrock Agents / Amazon Bedrock AgentCore — managed cloud agent service and modular agent infrastructure
- Google Agent Development Kit (ADK) — open-source multi-language framework with managed deployment options
- Microsoft Copilot Studio — graphical low-code studio for building and publishing agents

The defining core was checked across all five, including an older-generation managed service (Bedrock Agents Classic, now in maintenance mode) to avoid over-fitting to the current product generation.

## Sources

Research date: **2026-09-06**

- OpenAI Agents SDK — introduction and primitives: https://openai.github.io/openai-agents-python/
- Amazon Bedrock Agents (user guide): https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html
- Amazon Bedrock AgentCore (overview): https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- LangGraph (overview): https://docs.langchain.com/oss/python/langgraph/overview
- Microsoft Copilot Studio (overview): https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio
- Google Agent Development Kit (home): https://google.github.io/adk-docs/

> Sourcing limitation: research relied on each product's top-level documentation pages fetched on 2026-09-06; per-feature sub-pages (individual tool, evaluation, and deployment pages) were not fetched. Claims are therefore kept at the granularity those pages support, and precise operational details (numeric limits, default settings, pricing mechanics, exact state names) are intentionally not stated. Detailed observations are recorded in the paired Research Notes.
