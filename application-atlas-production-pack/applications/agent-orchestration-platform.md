# Agent Orchestration Platform

## Overview

An **Agent Orchestration Platform** coordinates multiple AI agents at runtime. Users define a coordination structure over a set of agents — an order of execution, a delegation pattern, a handoff rule, a shared discussion, or a manager that plans and routes — and the platform executes that structure: it routes tasks, messages, and context between the agents and drives the coordinated run to completion.

The defining core is small:

```text
Set of AI agents (each with its own instructions and tools)
└── Coordination structure over them (topology / plan / pattern)
    └── Platform-executed coordination
        (routing work and context between agents, run to completion)
```

Everything else commonly associated with the category — manager agents, named patterns, shared state, human approval points, durability, observability, agent registries, governance — is standard capability that mature products add, not what makes the product an orchestration platform.

The category has two recognizable philosophies that share this core. In **framework-style** products, coordination is authored in code over agents the same product helps define. In **control-plane-style** products, coordination is operated as a management layer over an agent estate that may include agents built elsewhere. When the coordination layer disappears — when agents are only defined and run one at a time — the product is an Agent Development Platform, not an orchestration platform.

## Users & Context

The primary users are the people responsible for making several agents work together as one system:

- **Agent developers / engineers** — assemble agent teams, author the coordination structure in code or configuration, and debug multi-agent runs.
- **Platform / automation teams** — operate orchestrated agents in production: monitor runs, manage the agent inventory, control cost and risk.
- **Governance and security owners** (control-plane products) — set access and policy across the agent portfolio and intervene when runs misbehave.

The work context is an organization that has moved past single-agent prototypes: several specialized agents exist (or are being built), tasks are too complex or too varied for one agent, and someone must decide how the agents' work is sequenced, delegated, and handed off. Framework-style products serve engineering teams building the system; control-plane products serve organizations running many agents, often from mixed origins, and needing one place to coordinate and govern them.

## Core Model

### The Defining Core

Three structures. If any one is removed, the product is no longer recognizable as an agent orchestration platform:

- **A plurality of agents as coordinated units** — the working set is several model-driven agents, each with its own role, instructions, and tools. The agents are the things being coordinated; they may be defined in the product or registered from elsewhere. Without a plurality, the product is a single-agent runtime or development tool.
- **An explicit coordination structure** — a user-defined topology, plan, or pattern that determines how work moves between the agents: what runs first, what runs in parallel, who delegates to whom, when control transfers, which agents share a conversation. Without it, the agents are just a catalog of independently invoked tools.
- **Platform-executed coordination** — the platform itself carries out the structure at runtime: it routes tasks and messages to the right agent, passes each agent's outputs into the next agent's context, sequences or parallelizes execution, and drives the run until it completes or stops. The user does not hand-carry results from one agent to the next.

### Standard Capabilities Mature Products Add

These are widespread across the researched products and expected in practice, but they are not the definition:

- **A coordinator role** — either a dedicated *manager* or *supervisor* agent that plans the work, delegates tasks based on each agent's capabilities, and reviews results, or deterministic control flow (a flow or workflow graph) that plays the same role without a model in the loop. Many products support both.
- **Named coordination patterns** — reusable shapes such as sequential execution, concurrent/parallel execution, handoff (control transfers between agents based on context), and group discussion (agents collaborate in a shared conversation).
- **Shared run state and context passing** — task outputs feeding subsequent agents, a shared conversation thread, and run-scoped state that persists across steps.
- **Human-in-the-loop** — the run pauses for human approval or input at defined points (for example, before a sensitive tool executes), then resumes.
- **Durability** — checkpoints and resumption for long-running coordinated work.
- **Observability of the multi-agent run** — traces and logs showing which agent did what, plus visualization of the coordination topology.
- **Interoperability protocols** — standard connection surfaces (such as MCP for tools and A2A for agent-to-agent communication) so agents and tools from different origins can participate.
- **Agent registry / discovery** — a catalog of the agents available for orchestration; control-plane products may discover and register agents running in external environments.
- **Governance** — access control and policy enforcement applied across the coordinated agents.
- **Cost and quality measurement** — token usage, tool-call success, and evaluation of how well agents perform inside runs.
- **Deployment and invocation** — managed execution of the orchestrated system, exposed through APIs, webhooks, or chat surfaces.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Coordinated agents:      agents authored in the same framework, or agents
                         discovered/registered from external environments
Coordination structure:  code-defined graphs and flows, named patterns,
                         console-configured supervisor plans, no-code studios
Coordinator:             deterministic control flow, a manager agent, or both
Agent provenance:        native-only, or heterogeneous estates spanning vendors
```

A reader who has only seen one style — say, a code framework where the coordination graph and the agents live in one codebase — should still be able to recognize a control-plane product that orchestrates agents built by other teams in other environments.

## How It Works

### Assemble the agent set

```text
Define agents in the product (instructions + model + tools)
or register/discover agents from other environments
→ each agent becomes an addressable participant with a declared role
```

In framework-style products this is code; in control-plane products it may be connecting to external agent environments and scanning them into a registry.

### Author the coordination structure

```text
Choose or build the structure:
  - a fixed order (agents execute one after another)
  - parallel execution (agents work simultaneously)
  - handoff rules (control transfers based on context)
  - a shared conversation (agents collaborate on one thread)
  - a manager/supervisor that plans, delegates, and validates
→ bind agents to positions in the structure
→ declare what each agent is responsible for
```

Routing and delegation key off the agents' declared specializations, so each agent's role and responsibilities must be clearly defined; at least one managed product's documentation explicitly warns against overlapping responsibilities.

### Invoke and run

```text
A task or request enters the orchestrated system
→ the coordinator (control flow or manager agent) decides who acts
→ the platform routes the work to that agent
→ the agent's output flows into the structure as context for the next step
→ steps repeat — sequential, parallel, or delegated — until the run completes
→ the result returns to the invoker
```

Two coordination styles exist side by side. In **deterministic coordination**, the structure fixes the paths (edges, conditions, order) and the platform executes them; agents fill the steps. In **manager-led coordination**, a coordinator agent interprets the task, forms a plan across the agent team, allocates work based on declared capabilities, and validates results; the structure defines the team and its roles rather than every path. Products frequently mix both — a deterministic flow may hand a bounded subtask to a self-coordinating agent team.

### Intervene, observe, and govern

```text
Human approval points pause the run where configured
→ traces record each agent's contribution to the run
→ operators monitor status, cost, and quality
→ policy and access rules are enforced across the agents
→ long runs checkpoint and resume after interruption
```

### Core vs standard vs optional

**Defining core** — without these, not an orchestration platform:

- plurality of agents as coordinated units
- explicit user-defined coordination structure
- platform-executed runtime coordination (routing, context passing, run-to-completion)

**Standard capabilities** — present in most mature products:

- coordinator role (manager/supervisor agent or deterministic control flow)
- named patterns (sequential, parallel, handoff, group discussion)
- shared run state and context passing
- human-in-the-loop checkpoints
- durability (checkpoints, resume)
- run observability and topology visualization
- interoperability protocols (tool and agent-to-agent)
- agent registry / discovery
- governance (access, policy)
- cost and quality measurement
- deployment and invocation surfaces

**Variant / optional** — depends on product form and customer tier:

- authoring surface: code SDK, visual graph, console configuration, no-code studio
- agent provenance: native-only vs heterogeneous estates spanning vendors
- coordination scope: one team/workflow vs estate-wide orchestration across business units
- product form: open-source framework, enterprise SDK, managed control plane, managed-cloud feature
- bundled extras: agent building, evaluation suites, deep governance

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Coordination authoring surface

Where the coordination structure is created.

- code SDK (graphs, flows, pattern constructors), visual workflow editor, console configuration, or no-code studio depending on the product
- typical information: available agents, their roles and tools, the structure's steps and connections
- primary actions: add/remove agents, define order/branches/parallelism, set delegation or handoff rules, assign a manager, configure human approval points

### Agent registry / catalog

The inventory of agents available for coordination.

- lists agents with their roles, capabilities, tools, origin (native or external), owner, and status
- primary actions: register or discover agents, review details, publish/approve, add to a coordination structure

### Run monitoring surface

The view of a coordinated run in progress or completed.

- shows the structure's execution: which agent acted, in what order, with what inputs and outputs, where the run is now
- typical information: per-agent steps, handoffs and delegations, status, duration, token/cost indicators
- primary actions: inspect a step, view traces/logs, cancel or resume, replay

### Human-in-the-loop checkpoint

The surface where a paused run waits for a person.

- shows the pending action or question and the context around it
- primary actions: approve, reject, edit input, provide requested information, resume

### Governance and operations surface

The control-plane view across orchestrated agents (prominent in control-plane products).

- typical information: agent inventory, owners, dependencies, activity, policy status, cost and quality indicators
- primary actions: set access and policy, review quality and cost, intervene in runs

### Invocation endpoints

How the outside world triggers the orchestrated system.

- API endpoints, webhooks/event triggers, chat surfaces; the orchestrated team is invoked like a single service

## Important Rules / Behaviors

### Coordination is explicit

Nothing moves between agents unless the structure provides for it. Adding an agent to the product does not make it participate in any run; it must be bound into a structure and given a role.

### The coordinator decides who acts next

Every run has a decision point per step: deterministic logic (edges, conditions, order) or a manager agent (plan, delegate, validate). Products differ in which they favor, and many support both; which one governs a given run is part of the structure, not an accident.

### The platform coordinates between agents, not inside them

Each agent keeps its own internal reasoning-and-tool loop. The orchestration layer routes work to agents and moves results between them; it does not normally reach into an agent's internal decisions. Control-plane products make this separation explicit by coordinating agents whose inner loops run elsewhere entirely.

### Outputs are the medium of coordination

An agent's contribution reaches the rest of the team only by flowing through the structure — as the next step's context, as a message in a shared conversation, or as a delegated task result. Agents do not implicitly share memory; shared state, where offered, is a capability configured in the structure.

### Human approval can pause the run

Where human-in-the-loop is configured, the run stops at the defined point — for example, before a tool executes, or when the run needs information only a person can provide — and waits; execution resumes only after the human responds. This makes the approval point part of the run's structure, not an external afterthought.

### Specialization drives routing

Agents in a coordinated set are typically specialized, and both deterministic routing and manager delegation rely on those declared specializations. Overlapping or vague roles are a known failure mode; products commonly require or advise clearly bounded responsibilities.

### Long runs are durable

Mature products checkpoint coordinated runs so they can resume after interruption or failure rather than restart from zero; the granularity of checkpointing varies by product.

## Variants

- **Open-source orchestration framework** — code-first; developers author agent teams and coordination structures (flows, graphs, patterns) that run anywhere (e.g. CrewAI, LangGraph)
- **Enterprise SDK with named patterns** — vendor-maintained multi-language SDKs exposing predefined coordination patterns plus graph workflows (e.g. Microsoft Agent Framework)
- **Managed control plane / agent management platform** — orchestration operated as an enterprise management layer: discovers and registers agents from multiple environments, coordinates native and external agents, and wraps runs in governance, cost, and quality oversight (e.g. IBM watsonx Orchestrate)
- **Managed-cloud supervisor pattern** — a cloud service where one agent is designated supervisor over collaborator agents and automatically plans and routes across them (e.g. Amazon Bedrock multi-agent collaboration)
- **No-code/low-code studio tier** — visual authoring of agent teams and coordination for non-developer makers, usually atop one of the above

A variant remains a variant as long as the defining core holds. When the "orchestration" is over deterministic steps and human tasks with no model-driven agent units, the product belongs to workflow/BPM automation instead; when it is over scripted robots, it belongs to RPA.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Agent Development Platform | closest sibling; gradient | centers on defining and running a single agent unit and its inner loop; multi-agent composition is a bundled capability there, while here the coordination structure over many agents is the primary object. Framework products bundle both, which keeps the boundary a gradient rather than a wall |
| Agent Evaluation Platform | adjacent lifecycle slice | scores how good agent runs are; this Type executes the runs. Evaluation appears as a bundled capability in many orchestration products |
| Agent Observability Platform | adjacent lifecycle slice | records and inspects execution traces; this Type consumes that visibility operationally but its center is coordination, not trace capture |
| Agent Tool / Computer-use Platform | adjacent supplier | provides executable environments and tools agents use; this Type coordinates the agents, not the tool runtime |
| LLM Application Development Platform | adjacent | builds model-powered applications where the developer owns control flow; no plurality of autonomous agent units to coordinate |
| Workflow Management / BPM Platform | structural neighbor, different unit | also routes work through ordered steps with human approvals, but the steps are deterministic tasks and human actions, not model-driven agents |
| RPA Platform | naming neighbor, different unit | RPA "orchestrators" coordinate scripted deterministic bots; the orchestrator vocabulary predates agentic AI but the coordinated unit differs |
| AI Gateway / Model Routing Platform | adjacent infrastructure | routes individual model calls; this Type routes tasks between agents |
| Enterprise AI Assistant | downstream consumer | a deployed end-user assistant product; an orchestrated agent team may power one, but the assistant is the product, not the coordination layer |

The boundary with Agent Development Platform is the most important one. The working test: remove multi-agent coordination — an orchestration platform is left with nothing, while an agent development platform survives; remove agent-definition tooling — an orchestration platform still functions when agents arrive from elsewhere, while a development platform does not. Buyers should expect the two categories to appear inside single product lines, with the distinction living in what the product's center of gravity is.

## Representative Products

- CrewAI (open-source framework; AMP platform tier)
- Microsoft Agent Framework
- IBM watsonx Orchestrate
- Amazon Bedrock multi-agent collaboration (Agents Classic generation)

The core model was checked against framework-style and control-plane-style products, and against the older managed-cloud generation, to avoid over-fitting to any one product form.

## Sources

Research date: **2026-09-06**

- CrewAI — Introduction: https://docs.crewai.com/en/introduction ; Processes: https://docs.crewai.com/en/concepts/processes ; AMP Introduction: https://docs-platform.crewai.com/platform/en/introduction
- Microsoft Agent Framework — Overview: https://learn.microsoft.com/en-us/agent-framework/overview/agent-framework-overview ; Workflow concepts: https://learn.microsoft.com/en-us/agent-framework/concepts/workflows/ ; Workflow orchestrations: https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/
- IBM watsonx Orchestrate — product page: https://www.ibm.com/products/watsonx-orchestrate
- Amazon Bedrock — Multi-agent collaboration: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html

> Sourcing limitations: IBM's product documentation site was unreachable (access denied) on 2026-09-06, so watsonx Orchestrate observations rest on the official product page and operational mechanics are intentionally not asserted. ServiceNow's site (a major enterprise vendor marketing an "agent orchestrator" product line) timed out repeatedly and is excluded from the evidence base entirely. The Amazon Bedrock multi-agent page documents the Agents Classic generation, which is in maintenance mode. Cross-product context for framework-style products (LangGraph, OpenAI Agents SDK, Google ADK, Copilot Studio) is carried over from the same-day Agent Development Platform research pass.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
