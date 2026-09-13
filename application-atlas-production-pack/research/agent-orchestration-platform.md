# Research Notes — Agent Orchestration Platform

Research date: 2026-09-06
Leaf: Agent Orchestration Platform (DIRECTORY §13 Data, Analytics & AI Systems)
Slug: agent-orchestration-platform

## Research Goal

Understand what an "Agent Orchestration Platform" actually is as an Application Type, from real products:

- what "orchestration" means in each product's own documentation (the word is used loosely across the market)
- what the coordinated working set is (which agents, where they come from)
- what structure defines how work moves between agents (patterns, topologies, plans, manager roles)
- what the platform executes at coordination time vs. what each agent does internally
- where the Type's boundary sits against Agent Development Platform (the flagged sibling), Agent Evaluation / Observability / Tool platforms, workflow/BPM automation, and RPA

This pass was explicitly framed by the boundary issue recorded in research/agent-development-platform.md: in that sample, multi-agent composition was an in-product capability of every agent development product, and the hypothesis was that a standalone orchestration platform would "center on coordinating pre-existing agents at runtime". This research tests that hypothesis.

## Initial Boundary (pre-research hypothesis)

An Agent Orchestration Platform coordinates multiple AI agents at runtime: it decides which agent acts when, routes tasks/messages/context between them, and drives the multi-agent work to completion. Expected neighbors:

- Agent Development Platform — defines and runs a single agent unit; orchestration may be bundled
- Agent Evaluation / Observability Platforms — lifecycle slices (quality / traces)
- Agent Tool / Computer-use Platform — supplies executable environments to agents
- Workflow Management / BPM (§10) — orchestrates deterministic steps and humans, not model-driven agents
- RPA platforms — orchestrate scripted bots (the RPA "Orchestrator" naming predates agentic AI)
- AI Gateway / Model Routing — routes model calls, not agent tasks

## Research Questions

1. What does each product call its orchestration structure (crew, flow, workflow, orchestration, plan, control plane)?
2. What is the coordinated unit — agents defined in-product, agents registered from elsewhere, or both?
3. What coordination patterns exist (sequential, parallel, handoff, group discussion, manager/supervisor)?
4. Who or what decides "who acts next" — deterministic control flow, a manager agent, or a routing model?
5. What passes between agents (task outputs, shared conversation, shared state)?
6. What does the platform own at runtime (state, checkpoints, retries, human escalation)?
7. What governance/observability wraps the multi-agent run?
8. How do framework-side and control-plane-side products differ in structure?
9. Where is the boundary with Agent Development Platform, and is it a wall or a gradient?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

| Product | Philosophy | Customer tier | Docs fetched |
|---|---|---|---|
| CrewAI (open-source framework + AMP platform) | multi-agent orchestration framework; crews + flows; hierarchical manager pattern; AMP = deploy/monitor/scale | OSS developers + enterprise | docs.crewai.com intro + processes; docs-platform.crewai.com intro |
| Microsoft Agent Framework | enterprise SDK (successor of AutoGen + Semantic Kernel); graph/functional workflows + named orchestration patterns | enterprise developers | learn.microsoft.com overview + workflow concepts + orchestrations |
| IBM watsonx Orchestrate | enterprise agent-management control plane; orchestrate native + external agents "wherever they are built or run" | enterprise (IT/security/AI leaders) | ibm.com product page (docs unreachable) |
| Amazon Bedrock multi-agent collaboration (Agents Classic) | managed cloud supervisor/collaborator pattern | AWS enterprise | docs.aws.amazon.com multi-agent collaboration page |

Cross-check evidence (Layer A, fetched 2026-09-06 in the sibling agent-development-platform pass, reused here): LangGraph ("low-level orchestration framework and runtime"), OpenAI Agents SDK (handoffs, agents-as-tools), Google ADK (multi-agent workflow agents, routing, A2A), Microsoft Copilot Studio (agents/workflows call each other), Amazon Bedrock AgentCore (Registry, multi-agent workloads).

Coverage check: code framework vs enterprise SDK vs managed control plane vs managed cloud pattern; OSS vs enterprise; native-only vs heterogeneous agent estates. Historical check: Bedrock Agents Classic (maintenance mode) as the older-generation managed sample; RPA Orchestrator and BPM/workflow engines considered as non-agentic structural neighbors (conceptual, not fetched).

## Sources

Fetched 2026-09-06 (Layer A unless noted):

1. CrewAI — Introduction: https://docs.crewai.com/en/introduction (framework positioning; Flows vs Crews architecture; Flow→Crew delegation loop)
2. CrewAI — Processes: https://docs.crewai.com/en/concepts/processes (sequential + hierarchical processes; manager_llm / manager_agent; manager planning/delegation/validation)
3. CrewAI AMP — Introduction: https://docs-platform.crewai.com/platform/en/introduction (deployments, API access, observability, tool repository, webhook streaming, Crew Studio)
4. Microsoft Agent Framework — Overview: https://learn.microsoft.com/en-us/agent-framework/overview/agent-framework-overview (agents/harness/workflows/integrations; AutoGen+Semantic Kernel lineage; "graph-based workflows for explicit multi-agent orchestration")
5. Microsoft Agent Framework — Workflow concepts: https://learn.microsoft.com/en-us/agent-framework/concepts/workflows/ (graph primitives: executors/edges/events/state; fan-out/fan-in; superstep checkpoints; HITL; sub-workflows; workflows-as-agents)
6. Microsoft Agent Framework — Workflow orchestrations: https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/ (sequential, concurrent, handoff, group chat, Magentic; HITL via tool approval)
7. IBM watsonx Orchestrate — product page: https://www.ibm.com/products/watsonx-orchestrate (Tier 2; control-plane positioning; discover/orchestrate/evaluate/govern/cost/risk features; A2A + MCP; pricing tiers)
8. Amazon Bedrock — Multi-agent collaboration: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html (supervisor + collaborator agents; plan-and-route; natural-language role descriptions; Classic maintenance-mode note)

Unreachable (recorded per source-access limitation rules):

- ServiceNow (www.servicenow.com) — product and docs URLs timed out twice; no claims based on this vendor. Enterprise workflow vendors are known to market products under "agent orchestrator" names, but nothing from them is asserted in this research.
- IBM docs (ibm.com/docs) — 403 twice; watsonx Orchestrate evidence stays at product-page (Tier 2) level; no operational mechanics asserted.
- LangGraph multi-agent doc path — 404 twice; LangGraph evidence reused from the sibling pass's fetched overview page instead.

## Product Observations

### CrewAI (Layer A)

- Self-description: "the leading open-source framework for orchestrating autonomous AI agents and building complex workflows"; "build production-ready multi-agent systems by combining the collaborative intelligence of Crews with the precise control of Flows."
- Two primitives: **Flows** ("the backbone... structured, event-driven workflows that manage state and control execution... the scaffolding for your AI agents") and **Crews** ("teams of autonomous agents that collaborate to solve specific tasks delegated to them by the Flow").
- Explicit division of labor: Flow = "the 'manager' or the 'process definition'"; Crew = "the 'teams' that do the heavy lifting."
- Runtime loop: Flow triggers → manages state → delegates a complex task to a Crew → Crew's agents collaborate → result returns to the Flow → Flow continues based on the result.
- Crews provide "Role-Playing Agents" (specialized agents with goals and tools), "Autonomous Collaboration", and "Task Delegation... based on agent capabilities."
- Processes (execution strategy of a crew): **Sequential** (tasks in predefined order; output of one task serves as context for the next) and **Hierarchical** ("tasks are delegated and executed based on a structured chain of command"; requires a `manager_llm` or `manager_agent`; "Tasks are not pre-assigned; the manager allocates tasks to agents based on their capabilities, reviews outputs, and assesses task completion").
- AMP (Agent Management Platform): "deploy, monitor, and scale your AI agent workflows"; crew deployments to managed infrastructure, REST API access, observability (execution traces and logs), tool repository, webhook streaming, no-code/low-code Crew Studio, GitHub/CLI deployment options.

### Microsoft Agent Framework (Layer A)

- Self-description: SDK for building "AI agents and multi-agent workflows in .NET, Python, and Go"; four areas: **Agents** (LLM units with tools/MCP), **Harness Agent** (opinionated long-task agent), **Workflows** ("functional and graph-based workflows that connect agents and functions through explicit execution paths"), **Integrations**.
- Lineage: "combines AutoGen's simple agent abstractions with Semantic Kernel's enterprise features... adds graph-based workflows for explicit multi-agent orchestration"; AutoGen and Semantic Kernel "pioneered the concepts of AI agents and multi-agent orchestration"; Agent Framework is "the direct successor".
- Agents-vs-workflows decision table: agent for open-ended/conversational/autonomous; workflow for "well-defined steps", "explicit control over execution order", "multiple agents or functions must coordinate".
- Workflow model: **executors** (receive inputs, perform work, emit outputs — agents can be executors), **edges** (route values between executors), **events**, **state management** (durable and run-scoped); fan-out/fan-in; superstep-boundary checkpoints; human-in-the-loop (`RequestInfoExecutor` / `ctx.request_info()`); sub-workflows compose as executors; a workflow can be exposed "through the standard agent interface" (workflows-as-agents).
- Named orchestration patterns: **Sequential** (agents execute one after another in a defined order), **Concurrent** (parallel), **Handoff** ("agents transfer control to each other based on context"), **Group Chat** ("agents collaborate in a shared conversation"), **Magentic** ("a manager agent dynamically coordinates specialized agents").
- Orchestration HITL: tool approval pauses the workflow for human review before execution.

### IBM watsonx Orchestrate (Layer A at product-page level; Tier 2)

- Self-description: "a comprehensive agent management platform to build and manage all your AI agents in one control plane"; "build, deploy, orchestrate, manage and govern AI agents — wherever they are built or run."
- Positioning: "More agents shouldn't mean more chaos"; "All your agents, working together seamlessly"; "one control plane without forcing every workload into the same vendor environment"; "Keep your stack. Add control."
- Feature structure: **Discover** (connect supported third-party agent environments, automatically scan for agents — example given: agents running in Amazon Bedrock — and bring them into the control plane); **Orchestrate** ("intelligently coordinate native and external agents, tools and workflows across the enterprise... so the right agent or system can act at the right time"); **Evaluate** agent quality (user feedback, operational signals, tool-call success); **Govern** (consistent access, policy, oversight across the portfolio); **Control costs** (token usage, LLM calls); **Mitigate risk** (policies across agents/tools/models, enforcement during execution).
- Interop posture: "built to support open standards — connect through APIs and open standards like A2A and MCP"; multi-cloud/on-prem deployment.
- Audience: IT, security, and AI leaders ("built for the leaders responsible for AI at scale").
- Pricing tiers observed (Trial / Essentials / Standard / Premium) with "Agent building/orchestration" listed as a plan feature — evidence that orchestration is sold as a platform capability, not only a code library.

### Amazon Bedrock multi-agent collaboration (Layer A; Classic in maintenance mode)

- Self-description: "enables multiple Amazon Bedrock Agents to collaboratively plan and solve complex tasks... assemble a team of agents that can break down tasks, assign specific tasks to domain specialist sub-agents, work in parallel, and use each other's strengths"; "a centralized mechanism for planning, orchestration, and user interaction."
- Structure: designate one agent as **supervisor**, associate one or more **collaborator agents**; hierarchical collaboration model; supervisor uses provided instructions to "understand the structure and role of each collaborator agent"; roles/responsibilities described in natural language; guidance to "clearly designate the role and responsibilities... and minimize overlapping responsibilities."
- Runtime behavior: "When you invoke the supervisor agent, it automatically creates and executes a plan across a set of collaborator agents and routes relevant requests and tasks to the appropriate collaborator agent."
- Each collaborator retains full agent capabilities (tools, action groups, knowledge bases, guardrails).
- Status: Agents Classic "no longer open to new customers" (maintenance mode; successor AgentCore) — used here as the older-generation managed sample.

### Cross-check evidence from the sibling pass (Layer A, 2026-09-06)

- **LangGraph**: "a low-level orchestration framework and runtime for building, managing, and deploying long-running, stateful agents"; "focused entirely on agent orchestration"; vendor's own ecosystem split: LangChain = agent framework, LangGraph = "the orchestration runtime", LangSmith = tracing/evaluation/deployment, Deep Agents = harness, Fleet = no-code builder.
- **OpenAI Agents SDK**: primitives include **handoffs** (delegate to other agents) and **agents-as-tools**; the runtime "manages turns, tool execution, guardrails, handoffs, or sessions".
- **Google ADK**: multi-agent workflows (sequential/loop/parallel template workflow agents), agent routing, collaboration; A2A protocol.
- **Copilot Studio**: agents, workflows, and agent flows can call each other.
- **Bedrock AgentCore**: Registry (catalog for agents/MCP servers/tools with publish/review/approve), multi-agent workloads on Runtime.

## Cross-product Comparison

| Dimension | CrewAI | Microsoft Agent Framework | IBM watsonx Orchestrate | Bedrock multi-agent (Classic) |
|---|---|---|---|---|
| Coordinated unit | Crew of role-playing agents | Agents (+ functions) as workflow executors | Native + external/discovered agents, tools, workflows | Supervisor + collaborator agents (all Bedrock agents) |
| Coordination structure | Flow (event-driven, stateful) wrapping Crews; crew process = sequential / hierarchical | Workflow graph (executors/edges) or named orchestration pattern | Orchestration across the agent estate ("right agent or system acts at the right time") | Supervisor's plan over collaborator agents |
| Who decides next actor | Flow logic (deterministic) or manager agent (hierarchical) | Graph edges/conditions (deterministic) or manager agent (Magentic) | Platform orchestration logic (mechanics not documented on fetched page) | Supervisor agent (model-driven plan + routing) |
| What passes between agents | Task outputs as context; delegation | Typed values along edges; shared conversation (group chat) | Work routed to agents/systems (mechanics not on page) | Requests/tasks routed; plan shared |
| Platform-owned runtime | Flow state; crew execution | Workflow run model, checkpoints, events | Control plane: discovery, governance, cost, policy | Plan execution, routing (agent internals platform-managed) |
| Human-in-the-loop | — (not on fetched pages) | First-class (request info, tool approval) | Govern/intervene posture ("intervene before small failures become enterprise problems") | — (not on page) |
| Agent provenance | Agents defined in the framework | Agents defined in the framework (any model provider) | Native + third-party (scanned from environments like Bedrock; A2A/MCP) | Agents configured in the same service |
| Observability | AMP traces/logs | Workflow events, spans, visualization | Evaluate quality, trace activity, cost visibility | — (traces exist at agent level, not on this page) |
| Governance | Enterprise security posture | (via enterprise features) | Access, policy, risk enforcement across portfolio | Guardrails per agent |
| Form | OSS library + managed platform (AMP) | OSS SDK (multi-language) | Managed SaaS control plane (+ build tooling) | Managed cloud service feature |
| Authoring surface | Python code; Crew Studio (no-code) | Code (C#/Python/Go); declarative workflows | Console/control plane (build + orchestrate) | Console/API configuration |

## Abstraction Levels

### L0 — Defining Invariant

An Agent Orchestration Platform is a product whose primary job is to **coordinate multiple AI agents at runtime**: the user defines a coordination structure over a set of agents, and the platform executes that structure — routing tasks, messages, and context between agents and driving the multi-agent run toward completion.

Three properties; remove any one and the product stops being this Type:

1. **A plurality of agents as first-class coordinated units** — the working set is several model-driven agents (defined in-product or registered from elsewhere), each with its own instructions/tools. Without it: an agent runtime or agent development platform (single-agent loop).
2. **An explicit, user-defined coordination structure** — a topology, plan, or pattern (order, parallelism, delegation, handoff, manager) that determines how work moves between the agents. Without it: a pool of independently invoked agents (agent catalog/registry), not an orchestrated system.
3. **Platform-executed runtime coordination** — the platform itself routes work and passes outputs/context between agents during the run; the user does not hand-carry each agent's output to the next agent. Without it: a code library of agent abstractions with no coordinating runtime, or a diagramming/design surface.

Historical check: the definition does not require LLMs, any specific protocol (MCP/A2A), a manager agent, code authoring, or managed hosting. Early LLM-era multi-agent frameworks (AutoGen lineage) satisfy it; a future non-LLM reasoning-agent world still satisfies it. Non-agentic neighbors fail property 1: BPM/workflow engines orchestrate deterministic steps and human approvals (no model-driven agent units); RPA "Orchestrators" orchestrate scripted bots (deterministic automation, no reasoning agent) — they are different Types, not older instances of this one.

### L1 — Common Mature Structure

Present across the researched sample; not required for the definition:

- **Manager/supervisor coordination role** — a dedicated coordinator agent (CrewAI hierarchical manager, Microsoft Magentic manager, Bedrock supervisor) that plans, delegates, routes, and validates; or deterministic control flow playing the same role (Flows, workflow graphs)
- **Named coordination patterns** — sequential, concurrent/parallel, handoff, group discussion appear as reusable patterns across products
- **Shared run state / context passing** — task outputs feeding subsequent agents; shared conversation; durable run-scoped state
- **Human-in-the-loop** — pause for approval/input mid-run (tool approval, request-info), escalation to humans
- **Durability** — checkpoints, resume, long-running runs
- **Observability of the multi-agent run** — traces/logs of which agent did what; workflow visualization
- **Interoperability protocols** — MCP (tools) and A2A (agent-to-agent) as connection surfaces
- **Agent registry / discovery** — cataloging agents (native or scanned from external environments) so they can be orchestrated
- **Governance** — access control, policy enforcement, risk controls across the agent set
- **Cost/quality measurement** — token usage, tool-call success, evaluation of agent performance
- **Deployment/invocation of the orchestrated system** — managed runtime, API endpoints, webhooks

### L2 — Variant / Optional Structure

- Product form: open-source code framework vs enterprise SDK vs managed control plane vs managed-cloud feature
- Agent provenance: native-only (agents built in the same product) vs heterogeneous estates (agents discovered/registered from other environments and vendors)
- Coordination authoring: code (graphs/flows) vs named patterns vs console configuration vs no-code studio
- Coordinator realization: deterministic control flow vs manager agent vs hybrid
- Topology scope: single-team orchestration (one crew/workflow) vs estate-wide orchestration (portfolio of many agents across business units)
- Deployment: self-run library, managed cloud, multi-cloud/on-prem
- Bundled adjacent capabilities: agent building, evaluation, governance depth (control-plane products bundle more)

### L3 — Vendor-specific (Research Notes only)

- CrewAI: Crews/Flows vocabulary; `Process` enum (sequential/hierarchical); `manager_llm`/`manager_agent` parameters; AMP branding ("Agent Management Platform"); Crew Studio; tool repository
- Microsoft: Magentic and Group Chat pattern names; Harness Agent; `WorkflowBuilder`/functional API split; superstep checkpoints; `AsAIAgent()` workflows-as-agents; AutoGen/Semantic Kernel lineage claims
- IBM: "Discover" agent scanning (example: Amazon Bedrock environments); plan tiers and pricing structure; "agent management platform" positioning; Omdia "unified control plane" analyst framing
- Bedrock: supervisor/collaborator configuration; natural-language role descriptions; Classic maintenance-mode status; TSTALIASID-era agent machinery (from sibling pass)
- LangGraph: StateGraph API; vendor's own framework/runtime/harness/builder ecosystem split (from sibling pass)

## Vendor-specific Findings

See L3. None entered the canonical model. Notable: two vendors (IBM, CrewAI) independently brand their platform tier "Agent Management Platform" — the control-plane side of this market is converging on "agent management" as the umbrella name, with orchestration as one capability inside it. Recorded as a taxonomy observation, not a structure.

## Rejected Findings

- "Orchestration means a manager agent" — rejected: deterministic control flow (CrewAI Flows, Microsoft workflow graphs) coordinates agents without any manager agent; the manager is one realization (L1), not the definition.
- "Orchestration platforms only coordinate agents built in the same product" — rejected: IBM watsonx Orchestrate explicitly coordinates native + external agents discovered from other environments; heterogeneity is a variant (L2), and the control-plane philosophy treats agent provenance as open.
- "Orchestration requires code" — rejected: Crew Studio (no-code), console configuration (Bedrock), and control-plane consoles (IBM) author coordination without code; authoring surface is L2.
- "Orchestration = workflow automation with AI inside" — rejected: BPM/workflow engines lack model-driven agent units (L0 property 1); the coordination target, not the presence of control flow, defines this Type.
- "Multi-agent orchestration is a capability, not a Type" — partially rejected: true for the framework sample (every agent development product bundles composition primitives), but the control-plane sample (IBM; CrewAI AMP's platform tier) centers the coordination/management layer as the product's primary job. The Type is defensible where coordination is the center of gravity; the overlap with Agent Development Platform remains a gradient (see Boundary Findings).
- "Orchestration platforms own the agents' internal loop" — rejected: in the control-plane sample the platform coordinates agents whose internal loops run elsewhere or independently; owning the inner loop is the Agent Development Platform's job, not this Type's.

## Boundary Findings

1. **vs Agent Development Platform (sibling, flagged)** — gradient with two distinct centers of gravity, confirmed from this side:
   - Agent Development Platform centers on **defining and running one agent unit** (identity + instructions + model + tools) and the platform-owned inner loop; multi-agent composition is a bundled capability (L1 there).
   - Agent Orchestration Platform centers on **the coordination structure over multiple agents**; the inner loops may run in-product (framework side) or elsewhere (control-plane side).
   - Structural test: remove multi-agent coordination → an orchestration platform has nothing left (it collapses into an agent runtime); an agent development platform survives (single-agent products exist). Remove agent-definition tooling → an orchestration platform still functions when agents arrive from elsewhere (IBM's "wherever they are built or run"; Bedrock supervisor over pre-configured agents); an agent development platform without definition tooling does not.
   - The market itself straddles the line: LangGraph self-describes as an "orchestration framework" while being a development framework; IBM and CrewAI brand their platform tiers "agent management platforms". Joint review should consider whether this leaf's center is the control-plane/management form (where it is clearly distinct) rather than the framework form (where it is a capability of agent development).
2. **vs Agent Evaluation / Agent Observability Platforms (siblings)** — evaluation and observability appear as bundled L1 capabilities in this sample (CrewAI AMP traces, IBM evaluate/trace, Microsoft workflow observability); standalone products exist (per sibling passes) but the capability relationship dominates. Consistent with prior flags.
3. **vs Agent Tool / Computer-use Platform (sibling)** — tools/tool-repositories appear as L1 (CrewAI AMP tool repository; agents' tool access); a standalone tool platform centers on providing executable environments, not on coordinating agents. Distinct centers.
4. **vs Workflow Management Platform / BPM (§10)** — both have "orchestration" vocabularies (control flow, routing, human approvals). The structural test is the coordinated unit: model-driven agents (this Type) vs deterministic steps/human tasks (BPM). Remove the agent units → this Type collapses; BPM remains. Adjacent, not overlapping. (Conceptual; BPM not fetched in this pass.)
5. **vs RPA platforms (§10)** — RPA "Orchestrators" (the term's older tenant) coordinate scripted deterministic bots; they fail L0 property 1 (no model-driven agent unit). The naming lineage explains why enterprise vendors reach for "orchestrator" branding, but the structures differ. (Conceptual; not fetched.)
6. **vs AI Gateway / Model Routing Platform (sibling)** — routing model calls vs routing agent tasks; different coordinated unit and different run structure. Adjacent.
7. **vs Enterprise AI Assistant (sibling)** — an assistant is a deployed end-user product; an orchestration platform is coordination infrastructure behind agent work. An orchestrated agent team may power an assistant; the Types remain distinct.

## Uncertainties

- IBM watsonx Orchestrate operational mechanics (how orchestration is authored, what the runtime guarantees) could not be verified — docs unreachable (403 ×2); all IBM observations are product-page level. No mechanics asserted.
- ServiceNow-class enterprise "agent orchestrator" products could not be reached at all (timeouts ×2); the control-plane sample rests on IBM + CrewAI AMP. If those products' docs were examined, the control-plane L1 list might grow (e.g., use-case plans, supervisor dashboards).
- Bedrock multi-agent collaboration is documented under Agents Classic (maintenance mode); the current-generation equivalent (AgentCore) was not re-fetched for multi-agent specifics. The supervisor pattern is treated as documented-but-older-generation evidence.
- Whether the market will keep "agent orchestration platform" as a separate purchase category, or fold it into "agent management platform" / agent development suites, is unresolved; this research establishes the structural centers, not the commercial outcome.
- CrewAI's human-in-the-loop story was not on the fetched pages (Microsoft's was); HITL is kept in L1 on the strength of Microsoft + control-plane "intervene" posture, not as universal.

## Final Synthesis

The Type's center of gravity is a **coordination structure → coordinated run** pair:

```text
Set of agents (native-defined or registered from elsewhere)
        ↓ bound into
Coordination structure (topology / plan / pattern: order, parallelism, delegation, handoff, manager)
        ↓ executed by
Platform-run coordination (routes tasks/messages/context between agents, drives the run to completion)
        ↓ wrapped by (standard capabilities)
shared state · human-in-the-loop · durability · observability · protocols (MCP/A2A) ·
registry/discovery · governance · cost/quality measurement · deployment/invocation
```

Two philosophies implement the same center:

- **Framework-side** (CrewAI, Microsoft Agent Framework, LangGraph, OpenAI SDK, ADK): coordination is authored in code over agents the framework also helps define; the runtime executes graphs/flows/patterns.
- **Control-plane-side** (IBM watsonx Orchestrate; CrewAI AMP tier): coordination is operated as a management layer over an agent estate, including agents built elsewhere; governance, discovery, and cost/quality oversight wrap the coordination.

The definition is deliberately model-agnostic, protocol-agnostic, authoring-agnostic, and hosting-agnostic. The overlap with Agent Development Platform is a gradient (frameworks bundle orchestration; control planes assume agents exist), and the sharpest standalone identity for this leaf is the coordination layer itself — the structure over multiple agents and the runtime that executes it.
