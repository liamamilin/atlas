# Research Notes — Agent Development Platform

Research date: 2026-09-06
Leaf: Agent Development Platform (DIRECTORY §13 Data, Analytics & AI Systems)
Slug: agent-development-platform

## Research Goal

Understand what an "Agent Development Platform" actually is as an Application Type, from real products:

- what the "agent" object is in each product's own documentation
- what a user must define to create one
- what the platform executes (the loop) and what the user controls
- how tools, knowledge, memory, safety, evaluation, and deployment fit
- where the Type's boundary sits against neighboring leaves (LLM Application Development Platform, Agent Orchestration Platform, Agent Evaluation/Observability Platform, Agent Tool / Computer-use Platform, RAG Development Platform, AI Coding Agent, Enterprise AI Assistant)

## Initial Boundary (pre-research hypothesis)

An Agent Development Platform is a product for building AI agents: LLM-driven systems that autonomously plan and execute multi-step tasks by invoking tools. Expected neighbors:

- LLM Application Development Platform — builds model-powered applications (prompt → response, RAG chat) without necessarily an autonomous loop
- Agent Orchestration Platform — coordinates multiple agents at runtime
- Agent Evaluation / Agent Observability Platforms — lifecycle-specific slices
- Agent Tool / Computer-use Platform — supplies executable tools/environments to agents
- AI Coding Agent (§12) — a finished agent product for coding, not a builder of agents
- Enterprise AI Assistant — a deployed end-user assistant product, not a builder
- (historical, not in directory) chatbot builders (intent-routing era) and RPA — rule-based, no model-driven loop

## Research Questions

1. What is an "agent" in each product's documentation? What objects define it?
2. How is agent behavior authored (code SDK / visual / natural language)?
3. How are tools and actions integrated (function calling, connectors, MCP, OpenAPI)?
4. What does the platform execute — who owns the loop, what terminates it?
5. What state does the platform hold (sessions, threads, memory, checkpoints)?
6. How is the agent invoked and deployed (local run, API, chat channels, triggers)?
7. What safety/guardrail/human-in-the-loop controls exist in-platform?
8. What evaluation/observability exists in-platform vs. as separate products?
9. What roles use the platform (developer / maker / admin)?
10. Where are the boundaries with neighboring Types?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

| Product | Philosophy | Customer tier | Docs fetched |
|---|---|---|---|
| LangGraph (LangChain) | open-source low-level orchestration framework + runtime; code-first | OSS/enterprise developers | docs.langchain.com/oss/python/langgraph/overview |
| OpenAI Agents SDK | model-vendor SDK; minimal primitives (agents, handoffs, guardrails) | API developers | openai.github.io/openai-agents-python |
| Amazon Bedrock Agents (Classic) + AgentCore | managed cloud service; config-driven agents; then modular agent infrastructure | AWS enterprise | docs.aws.amazon.com/bedrock/.../agents.html; .../what-is-bedrock-agentcore.html |
| Google ADK (+ Agent Runtime / Cloud Run / GKE deployment) | open-source multi-language framework + managed deployment | developers + enterprise | google.github.io/adk-docs |
| Microsoft Copilot Studio | graphical low-code studio; natural-language authoring; channel publishing | enterprise makers / business units | learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio |

Coverage check: open framework vs model-vendor SDK vs managed cloud vs open-SDK+managed-runtime vs enterprise low-code. Historical check performed against Bedrock Agents Classic (config-era) and against non-agentic neighbors (chatbot builders, RPA) conceptually.

## Sources

All fetched 2026-09-06 (Layer A unless noted):

1. OpenAI Agents SDK — https://openai.github.io/openai-agents-python/ (intro page; primitives, features, SDK-vs-Responses-API guidance)
2. Amazon Bedrock Agents — https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html (agent workflow, action groups, knowledge bases, traces, versions/aliases; notes Classic is in maintenance mode)
3. Amazon Bedrock AgentCore — https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html (full modular service table)
4. LangGraph — https://docs.langchain.com/oss/python/langgraph/overview (positioning, core benefits, ecosystem split)
5. Microsoft Copilot Studio — https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio (agents/workflows/agent flows, harnesses, authoring, management)
6. Google ADK — https://google.github.io/adk-docs/ (home page: definition, hello-world agent shape, feature map, FAQ on frameworks/context/deployment)

Not fetched (time-boxed): Copilot Studio per-feature pages, ADK sub-pages, AgentCore per-service pages, LangSmith pages, Vertex AI Agent Engine pages. Observations below are limited to what the fetched pages state.

## Product Observations

### OpenAI Agents SDK (Layer A)

- Self-description: "enables you to build agentic AI apps in a lightweight, easy-to-use package with very few abstractions"; production-ready upgrade of the Swarm experiment.
- Primitives named by the vendor: **Agents** ("LLMs equipped with instructions and tools"), **Agents as tools / Handoffs** (delegate to other agents), **Guardrails** (validate agent inputs/outputs).
- Agent loop: "a built-in loop that continues until the task is complete."
- Function tools: "Turn any Python function into a tool with automatic schema generation"; MCP server tool calling built in.
- Sessions: "a persistent memory layer for maintaining working context within an agent loop" (SQLite/Redis/Mongo/encrypted backends listed in reference).
- Human-in-the-loop: "built-in mechanisms for involving humans during agent runs."
- Tracing: built-in; ties to OpenAI evaluation/fine-tuning tools.
- Boundary drawn by the vendor itself (SDK vs Responses API): use the raw API "when you want to own the loop, tool dispatch, and state handling yourself"; use the SDK "when you want the runtime to manage turns, tool execution, guardrails, handoffs, or sessions." → the loop-ownership line separates plain LLM app dev from agent development.
- Extras: sandbox agents (isolated workspaces), realtime agents, voice pipelines; model adapters (LiteLLM, multi-provider) → not strictly single-model.

### Amazon Bedrock Agents — Classic (Layer A)

- Self-description: "build and configure autonomous agents in your application"; agent "orchestrates interactions between foundation models (FMs), data sources, software applications, and user conversations"; "automatically call APIs to take actions and invoke knowledge bases."
- Agent components: at least one **action group** (actions the agent can perform) and/or an associated **knowledge base**; optional customization of **prompt templates** for pre-processing, orchestration, knowledge-base response generation, post-processing stages.
- Workflow: configure agent → test in console or via test alias (TSTALIASID) → examine **traces** of "agent's reasoning process at each step of its orchestration" → create **alias pointing to a version** → application calls the agent alias via API → iterate with more versions/aliases.
- Platform-managed concerns: "prompt engineering, memory, monitoring, encryption, user permissions, and API invocation."
- Status note in docs: Agents Classic "no longer open to new customers", maintenance mode; successor is AgentCore. → useful as the older-generation sample.

### Amazon Bedrock AgentCore (Layer A)

- Self-description: "an agentic platform for building, deploying, and operating highly effective agents securely at scale using any framework and foundation model"; works with CrewAI, LangGraph, LlamaIndex, Strands, Google ADK, OpenAI Agents SDK; any model; MCP and A2A protocols.
- Modular services (use together or independently):
  - **Harness** — "a managed agent loop... define and invoke AI agents with a single API call. Specify a model, system prompt, and tools inline. Harness handles orchestration, tool execution, memory management, and response generation"; isolated microVM per session.
  - **Runtime** — "secure, serverless runtime environment purpose-built for deploying and scaling dynamic AI agents and tools"; session isolation; extended runtime for asynchronous agents.
  - **Memory** — short-term (multi-turn) + long-term (across sessions), shareable stores.
  - **Gateway** — converts APIs/Lambda/services into **MCP-compatible tools**; connects existing MCP servers.
  - **Identity** — agent identity/access management compatible with existing IdPs.
  - **Code Interpreter** — isolated sandbox for agent code execution.
  - **Browser** — managed cloud browser runtime for agents.
  - **Observability** — trace/debug/monitor each step; OTEL-compatible.
  - **Evaluations** — automated agent assessment on sessions/traces/spans.
  - **Optimization** — AI-generated config recommendations + A/B testing of prompts/tool descriptions.
  - **Policy** — deterministic control intercepting every tool call (natural-language or Cedar rules).
  - **Registry** — catalog for agents, MCP servers, tools, skills; publish/review/approve workflow.
  - **Payments** — managed microtransactions for agents (x402/MPP).
- Named use cases: Agents; Tools/MCP servers; **Agent Platforms** ("paved path" for internal developers — i.e., AgentCore itself can be the substrate of another agent platform).

### LangGraph (Layer A)

- Self-description: "a low-level orchestration framework and runtime for building, managing, and deploying long-running, stateful agents"; "very low-level, and focused entirely on agent orchestration."
- Core capability: "mix deterministic, hand-coded steps with LLM-driven agentic steps in the same graph."
- Core benefits listed: persistence (durable execution, resume after failure), human-in-the-loop (interrupts; inspect/modify state at any point), comprehensive memory (short-term working + long-term across sessions), streaming, debugging via LangSmith, production-ready deployment.
- Graph model: StateGraph / nodes / edges / START / END; `graph.invoke(...)`.
- Ecosystem split stated by the vendor: LangChain = "the agent framework: abstractions and integrations for models, tools, and agent loops"; LangGraph = "the orchestration runtime"; LangSmith = "tracing, evaluation, prompts, and deployment"; Deep Agents = "agent harness: planning, subagents, filesystem tools, context management"; LangSmith Fleet = "no-code agent builder." → the market itself layers framework / runtime / harness / builder / observability.
- Note: LangGraph calls itself an *orchestration* framework while being the canonical agent-development framework — direct evidence for the Development↔Orchestration boundary problem.

### Google ADK (Layer A)

- Self-description: "the open-source agent development framework that lets you build, debug, and deploy reliable AI agents at enterprise scale"; Python/TypeScript/Go/Java/Kotlin.
- Minimal agent shape (hello world): `Agent(name, model, instruction, tools)` — identical shape across five languages.
- Feature map: simple (LLM) agents + managed agents; **graph workflows** (deterministic + AI reasoning, new in 2.0); **multi-agent workflows** (sequential/loop/parallel template workflow agents, agent routing, collaboration); model-agnostic (Gemini, Claude, OpenAI, Ollama, vLLM, LiteLLM, model routing); custom tools (function tools, **MCP tools**, OpenAPI tools, tool authentication, **action confirmations**); artifacts; skills; callbacks/plugins; agent context (sessions, state, events, memory, context compression, caching); MCP; **A2A protocol**; live/voice agents; grounding.
- Run surfaces: dev **web interface** (with visual builder), CLI, **API server**, ambient agents, resume, cancel.
- Deployment: managed **Agent Runtime (Agent Platform)**, Cloud Run, GKE — "containerize and run on your own infrastructure" or one-command Google Cloud deploy.
- Observability: logging/metrics/traces. Evaluation: criteria, **user simulation**, environment simulation, custom metrics, optimization. Safety & security section.
- FAQ definition of the category: "when you need to accomplish complex, multi-step processes, an agent framework lets you create a managed, repeatable task structure that can run *hands-off* with minimal human input... automatically initiate tasks, make multiple iterative AI model requests, manage context, handle tool calls, record data, run parallel jobs, handle failures, and resume tasks."
- "Build agents *with* agents": Agents CLI scaffolds/builds/tests/evaluates/deploys agents via AI coding environments.

### Microsoft Copilot Studio (Layer A)

- Self-description: "a graphical, low-code studio for building and managing AI-powered agents and workflows"; "Because it's low-code, you can build capable solutions without an extensive technical background, while still giving professional makers the depth they need."
- Agent definition: "An agent is an AI assistant that handles conversations and completes tasks. It follows the instructions you give it, draws on the knowledge sources you connect, and uses tools to take action—reasoning through a request and deciding the best next step based on its instructions and context."
- Authoring: "create an agent by describing it in plain language, then test it before you publish"; natural-language build mode generates combinations of agents and workflows.
- Building blocks: **Agents**, **Workflows** (drag-and-drop automation), **Agent flows** (Power Automate-like flows, attachable to an agent as a tool); blocks can call each other.
- **Harnesses**: GitHub Copilot harness (reasoning-heavy multi-step), standard harness (rule-based; NLU matches request to a **topic** — a designed conversation portion with steps/questions/conditions; falls back to knowledge-generated answers), Copilot chat harness (extends M365 Copilot Chat). Harness choice affects reasoning, capability, billing.
- Tools/data: prebuilt or custom **connectors**; knowledge sources.
- Publish: channels where users work — Teams, Microsoft 365 Copilot, websites, mobile apps; some agents get their own account and work proactively.
- Operate: **Analytics** (performance, session outcomes), **Evaluations** (test sets, shared grader library, pre/post publish), **Administration** (agent inventory, role-based access, cost management).
- Legacy gradient visible inside one product: standard harness = topic/intent routing (chatbot-builder era); GitHub Copilot harness = autonomous reasoning loop (agent era).

## Cross-product Comparison

| Dimension | OpenAI Agents SDK | Bedrock Agents Classic | Bedrock AgentCore | LangGraph | Google ADK | Copilot Studio |
|---|---|---|---|---|---|---|
| Agent = defined unit with instructions + model + tools | Yes (Agent object) | Yes (configured agent) | Yes (Harness inline spec) | Yes (graph + LangChain agent abstractions) | Yes (Agent(name, model, instruction, tools)) | Yes (described agent w/ instructions, knowledge, tools) |
| Platform/runtime executes the loop | Yes ("runtime to manage turns, tool execution") | Yes ("orchestration" stages) | Yes (Harness = "managed agent loop") | Yes (runtime; durable execution) | Yes (event loop, runtime) | Yes (harness executes) |
| Tools beyond text | Function tools, MCP, hosted tools | Action groups (API calls) | Gateway (MCP), Code Interpreter, Browser | via LangChain tools | Function/MCP/OpenAPI tools, confirmations | Connectors, agent flows as tools |
| Knowledge/RAG integration | — (not on fetched page) | Knowledge bases | via Memory/Gateway (not RAG-specific on page) | via LangChain | Grounding (Google Search); artifacts | Knowledge sources |
| Session/conversation state | Sessions (pluggable stores) | Memory (platform-managed) | Memory service (short+long term) | Persistence/checkpoints | Sessions/state/events | Conversation context (implied) |
| Human-in-the-loop | Built-in | — (not on page) | Policy gates tool calls | Interrupts (first-class) | Action confirmations; graph human input | Human review steps in flows |
| Guardrails/safety | Guardrails primitive | — | Policy service | — (not on page) | Safety section; confirmations | — (admin governance) |
| Multi-agent | Handoffs, agents-as-tools | — | multi-agent workloads (Runtime) | graphs compose agents | workflow agents, routing, A2A | agents/workflows call each other |
| Tracing/observability | Built-in tracing | Traces of reasoning | Observability service | via LangSmith | Logging/metrics/traces | Analytics |
| Evaluation | ties to OpenAI eval tools | — | Evaluations service | via LangSmith | Evaluation module (simulation, criteria) | Evaluations (test sets, graders) |
| Deployment | library (self-run) | version + alias, API | Runtime (serverless) | LangSmith Deployment | Agent Runtime/Cloud Run/GKE | Publish to channels |
| Authoring surface | Python code | console config | API/CLI | Python/JS code | code + CLI + web UI + visual builder | graphical low-code + natural language |
| Model posture | OpenAI default + adapters | Bedrock FMs | any model | any (via LangChain) | any (adapters, routing) | Microsoft models (per harness) |

## Abstraction Levels

### L0 — Defining Invariant

An Agent Development Platform is a product whose primary job is to let users **define AI agents** — persistent, configurable units that combine a reasoning model with instructions and a set of callable tools — and to **run them**, where the platform executes the model-driven loop: the agent interprets the task, decides steps, invokes tools/actions, and iterates until the task is complete.

Four properties; remove any one and the product stops being this Type:

1. **Agent as a defined, persistent unit** — a named/configured artifact (not a one-off prompt) that survives between runs and can be versioned/re-invoked. Without it: prompt tooling / model playground.
2. **Tool/action integration** — the agent can invoke external functions, APIs, or services, i.e., act beyond generating text. Without it: chatbot / text generator.
3. **Model-driven execution loop owned by the platform** — the runtime carries the agent through multiple model turns and tool calls toward a goal (the user does not hand-execute each step). Without it: LLM Application Development (model-call plumbing) or an orchestration/workflow engine with no reasoning core.
4. **Invocation surface** — a way to run/test/invoke the agent (local run, API endpoint, chat channel, trigger). Without it: an agent *designer* only, not a development platform.

Historical check: this definition does not require "LLM", "function-calling API", "MCP", cloud hosting, or any specific authoring surface. A future non-LLM reasoning model, or a local library runtime, still satisfies it. Conversely, intent-routing chatbot builders (Dialogflow/Lex era) fail property 3 (no model-driven autonomous loop) — they are a different Type, not an older instance of this one.

### L1 — Common Mature Structure

Present in most mature products; not required for the definition:

- session/conversation state (threads, sessions, checkpoints) and memory (short-term working context; long-term across sessions)
- knowledge integration (connect data sources / knowledge bases / grounding)
- human-in-the-loop (approvals, interrupts, action confirmations, review steps)
- guardrails / input-output validation / policy gates on tool calls
- multi-agent structure (handoffs, subagents, workflow agents, delegation, inter-agent protocols)
- tracing / observability of the agent's step-by-step reasoning
- evaluation (test sets, graders, simulation of users/environments)
- deployment targets (managed runtime, serverless, containers, channel publishing)
- tool-connection machinery (function tools, MCP, OpenAPI, prebuilt connectors)
- versioning and promotion (versions/aliases, publish, environments)
- production analytics/monitoring and governance (inventory, RBAC, cost management)

### L2 — Variant / Optional Structure

- authoring surface: code SDK vs graphical low-code vs natural-language description (same core, different maker audience)
- product form: open-source library/framework vs managed cloud service vs hybrid (open SDK + managed runtime) vs modular infrastructure services
- model posture: single-vendor vs model-agnostic; model routing
- agent embodiment: conversational assistant vs background/proactive agent (own account) vs voice/realtime agents
- deterministic+agentic mixing (graph workflows) vs pure agent loop
- protocols: MCP, A2A, OpenAPI as first-class integration surfaces
- governance depth: policy engines, registries, admin inventory (enterprise posture)
- optional tool services: browser runtime, code interpreter sandbox, agent payments
- pricing/billing model (per-message, consumption, harness-dependent)

### L3 — Vendor-specific (Research Notes only)

- Copilot Studio: topics, harness taxonomy (GitHub Copilot / standard / Copilot chat), agent flows, M365 Copilot extension, agent inventory
- Bedrock: action groups, four-stage prompt templates (pre-processing/orchestration/KB generation/post-processing), TSTALIASID test alias, AgentCore service split (Harness/Runtime/Gateway/Identity/Policy/Registry/Payments/Optimization)
- LangGraph: StateGraph/nodes/edges API, Pregel/Beam inspiration, LangSmith Engine (trace issue detection → fix PRs), LangSmith Fleet (no-code builder), Deep Agents harness
- OpenAI: Swarm heritage, Responses-API relationship, sandbox agents with manifests/capabilities, realtime/voice pipelines
- Google: A2A protocol, Agent Runtime (Agent Platform), artifacts, five-language SDK parity, Agents CLI

## Vendor-specific Findings

See L3. None of these entered the canonical model. The AgentCore service decomposition is notable as evidence that "agent platform" can itself be decomposed into infrastructure services — but that is one vendor's architecture, not the Type's structure.

## Rejected Findings

- "Agent platforms are code-first Python libraries" — rejected: Copilot Studio is graphical low-code; Bedrock is config/API-driven. Authoring surface is L2.
- "Agent platforms are tied to one model vendor" — rejected: AgentCore, ADK, LangGraph all advertise any-model; even OpenAI SDK ships third-party adapters. Model posture is L2.
- "Multi-agent orchestration is a separate platform" — rejected as a *structural* claim for this sample: every researched product includes multi-agent composition as an in-product capability (handoffs, workflow agents, graphs, agent flows). Recorded as a boundary issue instead.
- "RAG/knowledge is the defining core" — rejected: knowledge integration is absent or peripheral in several sampled products (OpenAI SDK page, LangGraph page); it is L1.
- "Deployment/hosting is part of the definition" — rejected: LangGraph and OpenAI SDK are libraries that run anywhere; what is invariant is *invocability*, not managed hosting.
- "Agents are inherently conversational" — rejected: proactive/background agents (Copilot Studio own-account agents; AgentCore extended runtime for asynchronous agents; ADK ambient agents) satisfy the same core without a chat surface.

## Boundary Findings

1. **vs Agent Orchestration Platform (sibling leaf)** — sharpest issue. LangGraph self-describes as "orchestration framework and runtime" while being the canonical agent-development framework; OpenAI SDK has "Agent orchestration" as a doc section; ADK has multi-agent workflows; Copilot Studio composes agents/workflows. In this sample, orchestration is an in-product capability (L1), not a separate structure. A standalone "orchestration platform" would center on coordinating *pre-existing* agents at runtime (scheduling, routing, inter-agent messaging at fleet scale) — none of the sampled products is primarily that. Flag for joint review when Agent Orchestration Platform is processed.
2. **vs LLM Application Development Platform (sibling leaf)** — gradient, not a wall. The vendor-drawn line (OpenAI: own the loop vs runtime manages the loop) is the best discriminator: LLM app dev = model calls/RAG apps where the developer owns control flow; agent dev = the platform owns an autonomous model-driven loop. Products blur it (LangChain contains both; one codebase often mixes both).
3. **vs Agent Evaluation Platform / Agent Observability Platform (siblings)** — in the sampled products, evaluation and observability are bundled L1 capabilities (LangSmith, AgentCore Evaluations/Observability, ADK evaluation module, Copilot Studio evaluations/analytics, OpenAI tracing). Standalone products exist, but the capability relationship dominates. Flag for joint review.
4. **vs Agent Tool / Computer-use Platform (sibling)** — tools are L1 inside agent platforms; AgentCore ships Browser/Code Interpreter as *optional tool services*; OpenAI SDK has sandbox/computer surfaces. A standalone tool/computer-use platform would center on providing executable environments rather than on agent definition. Flag for joint review.
5. **vs AI Coding Agent (§12)** — different object: a coding agent is a finished agent product used to produce code; an agent development platform is the construction environment for agents of any kind. They meet (ADK's Agents CLI builds agents *with* coding agents) but the Types are distinct: user = developer-using vs developer-building.
6. **vs Enterprise AI Assistant (sibling)** — assistant = deployed end-user product; agent dev platform = builder. Copilot Studio is a builder whose outputs are assistants published to channels — the builder/product distinction holds.
7. **vs chatbot builders (no directory leaf; historical)** — intent/topic-routing platforms lack the model-driven autonomous loop; Copilot Studio's standard harness preserves topic routing as one harness, showing the gradient *inside* one product. Recorded as historical context, no directory conflict.
8. **vs RAG Development Platform (sibling)** — knowledge integration is L1 in agent platforms; a RAG platform centers on building retrieval pipelines. Distinct centers of gravity.
9. **vs RPA / workflow automation (§10, not sampled)** — rule-based automation without a reasoning core fails L0 property 3; adjacent, not overlapping. (Conceptual note; not researched in depth.)

## Uncertainties

- Vertex AI Agent Engine (Google's managed runtime) details were not fetched; ADK deployment section referenced it only as "Agent Runtime (Agent Platform)". Assertion strength kept low for Google's managed tier.
- Copilot Studio's tool/connectors and evaluation details come from the overview page only; per-feature pages not fetched. Claims kept at overview granularity.
- Bedrock Agents Classic is in maintenance mode; it was used as the older-generation sample. Current-generation Bedrock agent building = AgentCore. The canonical model was checked against both.
- Whether the market will keep "agent platform" and "agent orchestration platform" as separate purchase categories is unresolved; this research only establishes that the *structures* overlap heavily in the sampled products.
- No no-code business-tier product (e.g., Zapier-style agent builders) was sampled; Copilot Studio's natural-language authoring partially covers that tier. Definition should not assume developer-only users — it doesn't.

## Final Synthesis

The Type's center of gravity is a **definition → execution** pair:

```text
Agent definition (identity + instructions + model + tools)
        ↓
Platform-run execution loop (model decides steps, invokes tools, iterates to completion)
        ↓
Invocation surface (run/test locally, API endpoint, chat channel, trigger)
        ↓ (standard capabilities around it)
state/memory · knowledge · human-in-the-loop · guardrails · multi-agent ·
tracing · evaluation · deployment · versioning · governance
```

Everything else — authoring surface, product form, model posture, protocols, embodiment — is variation around this pair. The definition is deliberately model-agnostic, surface-agnostic, and hosting-agnostic.
