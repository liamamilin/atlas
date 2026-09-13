# Research Notes — LLM Application Development Platform

Research date: 2026-09-08
Leaf: LLM Application Development Platform (DIRECTORY §13 Data, Analytics & AI Systems)
Slug: llm-application-development-platform

## Research Goal

Understand what an "LLM Application Development Platform" actually is as an Application Type, from real products:

- what the product's unit of work is (the application? the prompt? the agent? the model?)
- what construction machinery the platform supplies around the model call
- who owns the control flow — the developer or the platform's runtime
- how models, prompts, knowledge/RAG, evaluation, observability, and publishing fit
- where the Type's boundary sits against neighboring leaves — especially **Agent Development Platform** (flagged for joint review by the sibling pass), Model API Platform, AI Model Hosting Platform, AI Gateway / Model Routing Platform, RAG Development Platform, Prompt Management Platform, LLM Evaluation / Observability Platforms
- whether the Type is still coherent in 2026 given the market's drift toward "agents" in marketing and docs

## Initial Boundary (pre-research hypothesis)

An LLM Application Development Platform is a product for building applications whose core intelligence comes from calling large language models: the developer composes prompts, context, knowledge retrieval, and application logic; the platform supplies the model-access surface and the construction machinery.

Expected neighbors:

- Agent Development Platform — the platform owns an autonomous model-driven loop (flagged gradient)
- Model API Platform / AI Model Hosting Platform — the substrate layer (serving model inference itself)
- AI Gateway / Model Routing Platform — runtime traffic layer beneath the application
- RAG Development Platform — retrieval-pipeline-centered specialization
- Prompt Management Platform — prompt-asset lifecycle slice
- LLM Evaluation Platform / LLM Observability Platform — lifecycle slices (often companion products)
- Enterprise AI Assistant — a deployed end-user product built with/for this ecosystem
- Low-code / No-code Application Builder (§12) — general app builders without a model substrate

## Research Questions

1. What does each vendor say its product is for? What is the unit of work?
2. What does a user do, step by step, to build and ship an LLM-powered application?
3. What construction machinery exists around the model call (prompts, context, retrieval, memory, structured output, composition)?
4. Who owns the control flow — designed-by-developer or runtime-directed?
5. How do models enter (catalog, provider integrations, credentials)?
6. How is what's built run, tested, evaluated, published, and operated?
7. Where does "agent" sit in each product — defining core, standard capability, or advanced sub-mode?
8. What is the historical shape of the category (pre-agent era) and does the definition still cover it?
9. Where are the boundaries with the neighboring Types listed above?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

| Product | Philosophy | Customer tier | Docs fetched |
|---|---|---|---|
| LangChain (LangChain) | open-source code-first framework; the category's lineage product; docs now agent-harness-centric (drift evidence) | OSS / enterprise developers | docs.langchain.com/oss/python/langchain/overview |
| LlamaIndex | open-source data-centric framework ("building an LLM application" as its own Learn track); RAG-first heritage | OSS developers | docs.llamaindex.ai/en/stable/understanding/ |
| Dify | open-source + cloud all-in-one visual platform; build → publish as web app / API | makers → teams | docs.dify.ai/ (root + 30-minute quick start) |
| Amazon Bedrock | managed cloud suite: multi-vendor model access + application machinery (Knowledge Bases etc.) | enterprise | docs.aws.amazon.com/bedrock (what-is + knowledge-base) |
| Microsoft Foundry (Azure AI Foundry) | managed cloud suite: model catalog + agents + tools/knowledge + observability + governance | enterprise | learn.microsoft.com/azure/foundry (hub + what-is-foundry) |

Coverage check: OSS framework (×2, code-first, different centers: general vs data) / visual all-in-one platform / managed cloud (×2, different clouds). The model-vendor pole (OpenAI platform) is covered indirectly: the sibling pass (agent-development-platform, 2026-09-06) recorded OpenAI's own SDK-vs-API boundary statement, imported here as cited evidence. Historical check performed against the pre-agent generation of these same products (conceptually: prompt+completion-era construction; Bedrock Knowledge Bases as a pre-agent-generation capability line; Dify chatbot/workflow app types) and against non-LLM neighbors (chatbot builders, RPA).

## Sources

All fetched 2026-09-08 unless noted (Layer A = direct observation):

1. LangChain overview — https://docs.langchain.com/oss/python/langchain/overview (agent-harness framing, standard model interface, LangGraph base, LangSmith debug, ecosystem split)
2. LlamaIndex — Building an LLM application — https://docs.llamaindex.ai/en/stable/understanding/ (RAG pipeline / agent / workflows tracks; component map)
3. Dify Documentation root — https://docs.dify.ai/ (platform self-description: "open-source platform for building AI applications… publish them as web apps or integrate them through APIs"; Cloud vs Self-Host; plugins; marketplace)
4. Dify — 30-Minute Quick Start — https://docs.dify.ai/en/quick-start (full build→publish workflow: model provider setup, workflow canvas, node vocabulary, test run, cached variables, last-run logs, publish updates)
5. Amazon Bedrock — What is Bedrock — https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html (managed service, enterprise-grade FM access, unified APIs: Messages/Responses/Chat Completions/Converse/Invoke, 100+ models, customization)
6. Amazon Bedrock Knowledge Bases — https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html (managed RAG machinery, managed vs customer-managed KBs, augment prompts, citations, deploy/test/modify lifecycle)
7. Microsoft Foundry documentation hub — https://learn.microsoft.com/en-us/azure/ai-foundry/ ("The AI app and agent factory"; module map)
8. Microsoft Foundry — What is Microsoft Foundry — https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry (agents/models/tools+knowledge; declarative↔code spectrum; surfaces; enterprise observability/governance; evolution table Azure OpenAI→Foundry, Assistants API→Responses API)
9. [Imported, Layer A, fetched 2026-09-06 by sibling pass] OpenAI Agents SDK intro — https://openai.github.io/openai-agents-python/ — vendor-drawn boundary: use the raw API "when you want to own the loop, tool dispatch, and state handling yourself"; use the SDK "when you want the runtime to manage turns, tool execution, guardrails, handoffs, or sessions" (recorded in research/agent-development-platform.md)

Fetch failures (recorded per source-access rules): docs.dify.ai/en/getting-started/readme → 404; raw.githubusercontent.com/langgenius/dify README → timeout; python.langchain.com/docs/concepts/ redirected to the same agent-centric overview (no broader "concepts" framing retrievable); learn.microsoft.com/azure/ai-foundry/overview-what-is-azure-ai-foundry → 404 (correct path found at /azure/foundry/what-is-foundry). Bedrock Guardrails / Prompt Management / Foundry per-feature sub-pages not fetched (time-boxed); claims kept at overview/quick-start granularity.

## Product Observations

### LangChain (Layer A)

- Current self-description: "LangChain provides `create_agent`: a minimal, highly configurable agent harness. Compose exactly the agent your use case needs from model, tools, prompt, and middleware."
- "**Agent = Model + Harness.** The harness is everything around the model loop: the prompt, the tools, and any middleware that shapes behavior."
- Docs quickstart says users build "your own agents **and applications** with LangChain" — the application word survives alongside the agent rebrand.
- Standard model interface: "Use one interface for chat models, embeddings, and more across providers. Switch models with minimal code changes and keep your application portable."
- Built on LangGraph (durable execution, human-in-the-loop, persistence); LangSmith for tracing/debug/evaluation. Vendor's own ecosystem split (from sibling pass, Layer A 2026-09-06): LangChain = "abstractions and integrations for models, tools, and agent loops"; LangGraph = orchestration runtime; LangSmith = "tracing, evaluation, prompts, and deployment".
- Observation: the category's canonical framework now *leads* with agents, but the underlying units (model interface, prompts, tools, middleware, traces) are the same construction machinery; the agent harness is a packaged pattern on top. This is the straddling-pole evidence for the flagged boundary.

### LlamaIndex (Layer A)

- Learn track is literally titled "Building an LLM application": three main parts — **Building a RAG pipeline**, **Building an agent**, **Building Workflows**; "short, bite-sized tutorials on every stage of building an agentic LLM application."
- Using LLMs: "dozens of supported LLMs… whether via remote API calls or running locally."
- Component map (doc tree): LLMs, prompts, embeddings, vector stores, retrievers, node postprocessors, response synthesizers, routers, structured outputs; loading (connectors, LlamaHub, LlamaParse), ingestion pipeline, storing (doc/index/kv/vector/chat stores); deploying: agents (memory, tools), chat engines, query engines; evaluating (response + retrieval evaluators, cost analysis); observability (callbacks, instrumentation; OpenTelemetry/Arize Phoenix integrations); MCP integration.
- Workflows described as "a lower-level, event-driven abstraction for building agentic applications… the base layer you should be using to build any advanced agentic application," with looping/branching, concurrent execution, stateful workflows, streaming events.
- Observation: a data/RAG-centered framework that still names its unit of work "the LLM application"; RAG machinery (load→index→store→retrieve→synthesize) is its deepest leg; agent and workflow layers are the advanced tiers. Same straddling pattern, different center of gravity.

### Dify (Layer A)

- Self-description (docs root): "Dify is an open-source platform for building AI applications. Create agents, agentic workflows, and chatbots that draw on your own data, then publish them as web apps or integrate them through APIs."
- Delivery: Dify Cloud (managed, "free Sandbox plan included," AI credits) vs self-host open-source Community Edition (Docker Compose). Extensibility via plugins (own tools, models, integrations) and a marketplace of integrations/app templates; REST API and CLI for integration.
- Quick start (full build→publish lifecycle, Layer A for mechanics):
  - Set up **Model Provider** (install provider integration; platform AI credits or your own API key); set a **Default Model** (System Reasoning Model).
  - **Studio → Create from Blank → Workflow** — visual canvas.
  - Node vocabulary observed: User Input (input fields become variables), Parameter Extractor (LLM-powered structured extraction with instructions and output schema), IF/ELSE branch, List Operator (filter/split), Doc Extractor (documents → text), LLM node (system/user prompts, variable interpolation, vision, structured output with JSON schema), Iteration (loop with parallel mode), Template (rule-based Jinja2 formatting, "zero token cost"), Output.
  - Test: checklist, **Test Run**, "View cached variables" to re-run a node with edited inputs without re-running the whole workflow; "Last Run" per-node logs for error diagnosis.
  - **Publish → Publish Update**: "If you make any changes later, always remember to publish again so the updates take effect" — versioned publishing.
  - Design guidance straight from the docs: "While LLMs can handle output formatting as well, their outputs can be inconsistent and unpredictable. For rule-based formatting that requires no reasoning, the Template node gets things done in a more stable and reliable way at zero token cost."
- Observation: the clearest "platform" form — the application (chatbot / agent / workflow) is an artifact *in* the platform, run and published by it; the developer (or maker) designs the flow; the canvas executes designed steps, not a self-directed loop (the "agent" app type and LLM-node loops are packaged patterns).

### Amazon Bedrock (Layer A)

- What-is: "Amazon Bedrock is a fully managed service that provides secure, enterprise-grade access to high-performing foundation models from leading AI companies, enabling you to build and scale generative AI applications."
- Unified access: multiple vendor APIs surfaced on one endpoint (Anthropic Messages API, OpenAI Responses API, OpenAI Chat Completions API, AWS Converse API, Invoke API); "100+ foundation models" from many providers; model customization (fine-tuning, continued pre-training, distillation); cross-region inference.
- Knowledge Bases (separate guide page): "you can further improve their responses by using Retrieval Augmented Generation (RAG)… integrate proprietary information into your generative-AI applications." Two forms: **Managed Knowledge Base** (Bedrock manages ingestion, indexing, storage, retrieval; smart parsing; agentic retrieval with multi-hop decomposition; connectors: S3, SharePoint, Confluence, Google Drive, OneDrive, Web Crawler; document-level ACL permission filtering; native AgentCore Gateway integration so "any MCP-compatible agent framework can discover and invoke your Knowledge Base as a tool") and **Customer-managed Knowledge Base** (your own vector store: OpenSearch Serverless, Aurora, Neptune; your own pipeline).
- KB capabilities: "Augment your own prompts by feeding the returned relevant information into the prompt"; citations in generated responses; multimodal retrieval; reranking; per-KB lifecycle pages: build → test (queries and responses) → **deploy your knowledge base for your application** → view/modify/delete.
- Observation: the managed cloud pole. Model access is the substrate; Knowledge Bases is the app-side machinery (a pre-agent-generation product line that predates and outlives the agent wave); agents exist (sibling pass covered Bedrock Agents/AgentCore) but the platform's own top-level framing is "build and scale generative AI applications."

### Microsoft Foundry (Azure AI Foundry) (Layer A)

- Hub tagline: "The AI app and agent factory - build, optimize, and govern AI apps and agents at scale."
- What-is: "Microsoft Foundry unifies agents, models, and tools under a single management grouping with built-in enterprise-readiness capabilities including tracing, monitoring, evaluations… unified role-based access control (RBAC), networking, and policies."
- What you can build: **Agents** (declarative "prompt agents" in portal/SDK, or "hosted agents" running your own code as a container); **Models** ("more than 10,000 models from Microsoft, OpenAI, Anthropic, Meta, and others"); **Tools and knowledge** (Foundry Toolbox: built-in tools, memory, retrieval — Foundry IQ knowledge base).
- The gradient, stated by the vendor: "Most projects on Foundry center on an agent… Think of it as a spectrum from declarative to full code." And: "**Not building an agent yet?** If you only need to send prompts to a model with no tools or orchestration, start with a single model call." — the platform explicitly spans model-call apps to agents.
- Developer surfaces: Foundry portal (playgrounds, prompt prototyping, "playgrounds and quick evaluation"), SDKs (Python/C#/JS/Java), Azure Developer CLI, VS Code extension, coding agents via Foundry Skill/MCP server.
- Evolution table (platform history, Layer A): Azure AI Studio/Azure OpenAI → Microsoft Foundry; Assistants API (Agents v0.5/v1) → **Responses API (Agents v2)**; hub+multiple resources → single Foundry resource with projects; multiple SDK packages → unified project client against one project endpoint; Threads/Messages/Runs/Assistants → Conversations/Items/Responses/Agent Versions.
- Observation: enterprise cloud pole #2; same straddling shape as Bedrock, with the model-call ↔ agent spectrum stated explicitly in prose.

## Cross-product Comparison

| Dimension | LangChain | LlamaIndex | Dify | Amazon Bedrock | Microsoft Foundry |
|---|---|---|---|---|---|
| Unit of work named by vendor | agent harness / "agents and applications" | "LLM application" (RAG / agent / workflows) | the app: chatbot / agent / workflow, published as web app or API | "generative AI applications" on managed model access | "AI apps and agents" |
| Model access | standard interface across many providers (chat models, embeddings) | dozens of LLMs via remote API or local | model-provider integrations; platform credits or own keys; default model setting | 100+ FMs, many vendors, unified APIs on one endpoint | 10,000+ model catalog, one project endpoint |
| Prompt construction | prompt + middleware in harness; prompts in LangSmith ecosystem | prompts as first-class components (usage patterns) | LLM node with system/user prompts, variable interpolation, instructions fields | prompts via APIs; KB output fed into prompts | prompt prototyping in portal playgrounds; SDK |
| Knowledge / RAG | via LangChain/LlamaIndex-style integrations (ecosystem) | the deepest leg: loading→indexing→storing→querying→response synthesis | "draw on your own data"; knowledge as platform feature (datasets) | Knowledge Bases: managed or customer-managed RAG, citations, deploy/test lifecycle | Foundry IQ knowledge base; Toolbox retrieval |
| Control flow owner | developer composes; harness is a packaged loop pattern | developer composes; workflows are event-driven but designed | developer/maker designs the canvas; engine executes designed steps | developer calls APIs; designed orchestration (agents optional) | developer designs; "spectrum from declarative to full code" |
| Composition machinery | create_agent harness, middleware, LangGraph graphs | Workflows (events, loops, branches, concurrency, state) | node canvas: extract/branch/split/loop/template/output | API composition by developer; agents as managed pattern | prompt agent (declarative) ↔ hosted agent (own code/container) |
| Structured output | via middleware/model features | structured LLMs, structured prediction, output parsers | structured output toggle with JSON schema; Parameter Extractor | model APIs (JSON/structured modes on providers) | via SDKs/model features |
| Run / test surface | local run (library); LangSmith tracing | local run; tracing & debugging guides; evaluators | Test Run, cached variables, per-node last-run logs | test KB pages; console playgrounds; API | playgrounds + quick evaluation; SDK quickstarts |
| Evaluation | via LangSmith ("trace, debug, and evaluate") | built-in evaluators + cost analysis | (not on fetched pages) | (referenced in sibling pass: AgentCore evals; not on fetched pages) | built-in tracing, monitoring, evaluations |
| Observability | via LangSmith (traces, tool calls, latency) | callbacks, instrumentation, OTEL integrations | per-node run logs (lightweight) | AgentCore Observability (sibling pass) | built-in tracing/monitoring/evaluation dashboards |
| Publish / deploy | library — runs in your process; LangSmith Deployment (sibling pass) | guides for full-stack web apps; deployments via your stack | Publish Update → web app; REST API; CLI | deploy KB for application; API consumption | hosted agent endpoints; Foundry portal publish |
| Non-determinism handling | middleware (retries, guardrails) | response synthesizers, evaluators | Template node guidance ("rule-based formatting… more stable… zero token cost") | model choice/cross-region; KB citations | quick evaluation; content filters |
| Agent sub-mode? | foregrounded (create_agent) | foregrounded (agent track) | app type: agent | Agents/AgentCore (sibling pass) | foregrounded (prompt/hosted agents) |

Cross-product commonalities (Layer B): multi-provider model access with a normalized interface; prompt construction as first-class material; knowledge/RAG machinery; session/conversation state; structured outputs; a run-test-iterate loop with some trace/log surface; publish as API or hosted app; evaluation and observability present in every ecosystem (often as companion product); agent capability present in every product as a sub-mode or foregrounded frame.

## Abstraction Levels

### L0 — Defining Invariant

An LLM Application Development Platform is a product whose primary job is to help users **build, run, and operate applications whose core intelligence is delivered by calling hosted foundation models**, by supplying the model-call surface plus construction machinery around it, while the **developer designs and owns the application's control flow**.

Four properties; remove any one and the product stops being this Type:

1. **Foundation-model call as the intelligence substrate** — what is being built works by sending requests (prompts/messages) to hosted foundation models and using the responses as the application's core content or decisions. The platform's whole reason to exist starts from that call. Without it: an ordinary application framework, workflow tool, or chatbot builder.
2. **Construction machinery around the model call** — reusable building blocks that assemble requests and process responses: prompt construction, context/knowledge assembly, output shaping/structuring, and composition of multiple model calls and logic steps into a designed application flow. The unit of work is the **application** (an artifact with designed behavior), not the model itself and not a self-directed agent. Without it: a raw model API/SDK (Model API Platform territory) or a bare playground.
3. **Developer-owned control flow** — the developer designs when and how model calls happen (in code, or in an explicitly designed flow/canvas); the platform executes what is designed. Prebuilt components execute deterministic steps or fixed call patterns. Without this — i.e., if the platform runtime owns a self-directing model-driven loop — the product is an Agent Development Platform (the flagged gradient; see Boundary Findings).
4. **Run/test surface for what is built** — a way to exercise and iterate on the constructed application (playground/test run, local run as a library, API endpoint, published app). Without it: a prompt-authoring or design tool with nothing to run.

Jointly-held is load-bearing:
- 1 alone = model API/SDK (Model API Platform / AI Model Hosting Platform)
- 2 alone = generic low-code/workflow app builder (no model substrate)
- 3 removed = Agent Development Platform
- 4 removed = prompt library / design-only tool (Prompt Management territory)
- 1+3 without 2 = thin wrapper over model calls, still model-access territory
- 2+3 without 1 = no-code app builder / chatbot-builder era
- 1+2 without 4 = authoring tool with no runnable artifact

Historical check (pre-agent era, conceptual + product-internal evidence): the 2020–2022 generation of LLM apps — a prompt template, a completion call, response handling in the developer's code — satisfies all four legs (machinery = prompt template + response handling; run surface = local code/playground). Bedrock Knowledge Bases and Dify's chatbot/workflow app types are product-internal evidence that the machinery predates the agent wave and still ships first-class. The definition names no "LLM" mechanism beyond hosted foundation models (a non-LLM generative substrate would still satisfy it), no RAG/vector stores, no workflows, no agents, no cloud, no specific authoring surface. Conversely, intent-routing chatbot builders (Dialogflow/Lex era) fail leg 1 (the model was a classifier, not the application's content engine) — a different Type, not an older instance of this one.

### L1 — Common Mature Structure

Present across the sample; not required for the definition:

- **Model catalog / unified model interface** — multi-provider access behind a normalized call surface; model switching as a configuration-level act
- **Prompt tooling** — prompt editors/templates with variables, playgrounds, parameter control
- **Knowledge/RAG machinery** — connect data sources, ingest/chunk/embed/index, retrieve, feed into prompts, optional citations; depth varies from simple augmentation to managed knowledge bases
- **Session/conversation state and memory** — history carried across calls (chat stores, memory modules)
- **Structured outputs** — schemas/parsers/extraction so downstream logic can consume responses reliably
- **Composition abstractions** — chains/flows/graphs/canvas nodes composing model calls with logic steps, branching, iteration, parallelism
- **Guardrails / content safety hooks** on inputs and outputs
- **Evaluation** — test sets, graders, comparisons (often a companion product: LangSmith)
- **Tracing/observability** — per-call or per-node logs/traces for debugging quality and cost
- **Streaming responses** — progressive output as a UX primitive
- **Publishing/versioning** — API endpoints, hosted web apps, embedded widgets; publish-update semantics
- **Provider/tool ecosystems** — integrations, plugins, marketplaces of components
- **Cost/usage surfaces** — token metering, credits, usage views

### L2 — Variant / Optional Structure

- Product form: open-source library/framework vs OSS+managed-cloud platform vs managed cloud suite vs (untested here, conceptual) model-vendor platform
- Authoring surface: code SDK vs visual canvas vs console/playground (many products offer several; portal→code progression is explicitly vendor-recommended)
- Model posture: multi-provider catalog vs single-vendor; platform credits vs bring-your-own-key
- Delivery of the built app: hosted web app in-product vs API endpoint vs embedded in the customer's product vs library running in the customer's process
- Knowledge posture: none / prompt-stuffing / customer-managed vector pipeline / fully managed knowledge service
- Agent support: sub-mode vs foregrounded frame (the straddling pole — every sampled product has one)
- Audience tier: developers only ↔ makers/business users (visual/no-code pole)
- Governance depth: enterprise RBAC, network isolation, content filters, policy (cloud suites)
- Local/offline posture (Foundry Local-style device runtime) vs cloud-only

### L3 — Vendor-specific (Research Notes only)

- LangChain: create_agent harness, middleware model, "Agent = Model + Harness" framing, Deep Agents, LangGraph/LangSmith ecosystem split, docs repositioned agent-first in the current generation
- LlamaIndex: LlamaHub connector registry, LlamaParse/LiteParse parsing products, query engines/chat engines/response synthesizers taxonomy, Workflows as "base layer," LlamaAgents/LlamaCloud
- Dify: model-provider "integrations" with AI credits and Sandbox plan, node vocabulary (User Input, Parameter Extractor, Doc Extractor, List Operator, Iteration, Template), cached-variables re-run, Publish Update model, difyctl CLI, plugin/marketplace model
- Amazon Bedrock: managed vs customer-managed Knowledge Bases, Smart Parsing, agentic retrieval (multi-hop, sub-queries, sufficiency evaluation), document-level ACLs, AgentCore Gateway integration, Kendra GenAI index / Neptune Analytics graph options, cross-region inference, model customization line
- Microsoft Foundry: prompt agent vs hosted agent taxonomy, Foundry IQ / Foundry Toolbox, Foundry Control Plane, evolution table (Assistants API → Responses API "Agents v2"; Threads/Messages/Runs → Conversations/Items/Responses/Agent Versions), Foundry Local, AI Red Teaming Agent, Foundry Skill/MCP for coding agents

## Vendor-specific Findings

See L3. None entered the canonical model. Two vendor patterns deserve note as *era markers* rather than structure: (1) the wholesale docs rebrand of frameworks from "LLM application" to "agent" (LangChain leads with create_agent; LlamaIndex's track is "building an agentic LLM application"; Foundry calls itself an "agent factory") — the construction machinery underneath is unchanged; (2) the consolidation of model access into one endpoint/resource (Bedrock unified APIs; Foundry unified project client) — a packaging shift in the substrate, not the app-building layer.

## Rejected Findings

- "LLM app dev platforms are code-first Python frameworks" — rejected: Dify is a visual canvas with publishing; Bedrock/Foundry are cloud consoles + APIs. Authoring surface is L2.
- "RAG is the defining core" — rejected as definitional: every product has some knowledge machinery, but Bedrock's top-level framing, LangChain's current docs, and Dify's quick start build apps without any RAG step. Knowledge assembly is L1. (Center-of-gravity for LlamaIndex only.)
- "Agent-building is the defining core" — rejected: all five products build non-agent applications first-class (single model call — Foundry's own words; Dify chatbot/workflow types; Bedrock "build and scale generative AI applications"); agent support is universal but as a packaged pattern/sub-mode. This rejection is the joint-review resolution for the flagged boundary.
- "The platform owns/publishes the application" — rejected as definitional: LangChain/LlamaIndex are libraries; the application runs in the developer's process. Run/test surface is invariant; *hosting* the artifact is variant.
- "Model access is just plumbing, not part of the Type" — rejected: normalized multi-model access (catalog, unified interface, provider credentials) is Layer-B universal across the sample and is the substrate leg; what is NOT definitional is *hosting or serving models* (that's Model API/Hosting territory).
- "Prompt engineering tools are a separate, incidental slice" — rejected for this Type: prompt construction is the primary programming act of the Type (L1 mandatory-ish); what stays separate is *prompt-asset lifecycle management* as a standalone product (Prompt Management Platform — flagged for joint review).
- "Evaluation/observability are out of scope" — partially rejected: they appear in every ecosystem (L1), but as capabilities/companions, not the defining center (LLM Evaluation / Observability Platforms — flagged for joint review).

## Boundary Findings

1. **vs Agent Development Platform (sibling; FLAG DISCHARGED — joint review resolved, keep-both).** The sibling pass flagged a gradient boundary drawn by vendor docs themselves (model API = developer owns the loop; agent SDK = runtime manages turns/tool execution/sessions) with products straddling it. This pass confirms all three observations first-hand: (a) OpenAI's own line (imported Layer A evidence); (b) Foundry's prose spectrum "declarative ↔ full code" and its explicit "Not building an agent yet? … start with a single model call"; (c) straddling products — LangChain leads with an agent harness while keeping "applications" in its quickstart; LlamaIndex puts RAG/agents/workflows in one Learn track; Dify offers chatbot/agent/workflow app types in one studio; Bedrock and Foundry both ship agent services on the same platform as their model APIs. **Resolution: keep-both as a layered gradient, not an alias.** LLM Application Development Platform is the *broader substrate Type* — its defining posture is developer-owned control flow over model calls plus construction machinery. Agent Development Platform is the *loop-ownership specialization* — the platform runtime owns a self-directing model-driven loop over tools. The boundary is real at the definitional level (each has a load-bearing property the other lacks: LLM-app-dev's "developer-owned control flow" vs agent-dev's "platform-owned loop") and gradient at the market level (every mature LLM-app platform now bundles an agent mode; every agent platform rests on the same model-call substrate). Neither pass should harden the boundary into a wall; both documents cross-reference the gradient.
2. **vs Model API Platform (unprocessed sibling)** — substrate layer: serving model inference and model access itself; this Type builds applications on top of that substrate. Products straddle from the other side (Bedrock/Foundry sell model access *and* app machinery in one service). Keep-both, layer distinction; flag for joint review when Model API Platform is processed.
3. **vs AI Model Hosting Platform (processed)** — hosting = deploying/serving models (often customer-supplied weights) as the product's job; this Type consumes hosted models as inputs. Different layer; no conflict observed.
4. **vs AI Gateway / Model Routing Platform (processed)** — gateway = runtime traffic intermediary beneath applications (routing, credentials, budgets); this Type = the build layer above. The gateway doc already records the relationship ("different layer"); confirmed symmetrically here.
5. **vs RAG Development Platform (unprocessed sibling)** — knowledge assembly is one L1 capability here; a RAG platform would center the retrieval pipeline (ingest→index→retrieve→rerank→synthesize) as its defining job. LlamaIndex is the closest straddler (its deepest leg is RAG) but its own unit of work remains "the LLM application." Flag for joint review when RAG Development Platform is processed.
6. **vs Prompt Management Platform (unprocessed sibling)** — prompt construction is a defining-layer *activity* here; a prompt-management platform would center prompt assets' lifecycle (versions, testing, collaboration, registry) as a standalone product. Flag for joint review.
7. **vs LLM Evaluation Platform / LLM Observability Platform (unprocessed siblings)** — evaluation/observability are L1 capabilities, frequently delivered as companion products (LangSmith) or bundled services (Foundry observability/evaluations). Capability-sibling relationship; flag for joint review.
8. **vs Enterprise AI Assistant (processed)** — assistant = deployed end-user product; this Type = the build layer that produces apps *including* assistants. Downstream relationship; consistent with the sibling's framing.
9. **vs Low-code / No-code Application Builder (§12)** — general app builders lack leg 1 (model substrate) as defining; Dify's visual canvas overlaps in *surface* but its canvas nodes are model-centered. Adjacent, not overlapping.
10. **vs chatbot builders (no leaf; historical)** — intent/NLU-era builders fail leg 1; different Type. The gradient survives *inside* products (Foundry's declarative prompt agent; Dify's chatbot type) but the defining substrate differs.
11. **vs AI Coding Assistant / AI Coding Agent (§12, processed)** — finished coding products vs the build layer for LLM apps. They increasingly meet (Foundry Skill/MCP driven *by* coding agents; LangChain docs consumed via MCP) — a usage relationship, not a Type overlap.

## Uncertainties

- OpenAI platform docs were not fetched this pass; the model-vendor pole rests on the sibling pass's Layer A record (Agents SDK intro) plus general market knowledge — deliberately excluded from the canonical model. Product count kept at five.
- Dify's knowledge/RAG feature details come from the docs root's "draw on your own data" phrase only; per-feature pages not fetched. Knowledge assembly asserted as platform capability (Layer A for existence), not for mechanics.
- Bedrock Guardrails / Prompt Management pages not fetched; guardrails and prompt tooling asserted at Layer B (cross-product) strength only.
- LlamaIndex's fetched page is the Learn overview + doc tree; specific component mechanics (response synthesizer modes etc.) not verified beyond titles.
- The category is being actively rebranded around "agents" (2025–2026); whether the market will keep "LLM application development" as a distinct purchase category or fold it into agent platforms is unresolved. The structures are layered (agents sit on the app-building substrate), which supports keep-both; purchase-category evolution cannot be settled from documentation.
- Historical check is conceptual for the 2020–2022 completion-era (no archived docs fetched); it is corroborated internally by the pre-agent product lines still shipping (Bedrock KBs, Dify chatbot/workflow types, Foundry's model-call quickstart).

## Final Synthesis

The Type's center of gravity is a **substrate + construction + designed-control** triple:

```text
Hosted foundation-model access (catalog / unified call surface)
        ↓
Construction machinery around the call
(prompt assembly · context & knowledge · structured output ·
 composition of calls and logic into a designed flow · session state)
        ↓
Developer-owned control flow (the platform runs what is designed)
        ↓
Run/test/publish surface (playground → traces/logs → endpoint / hosted app / library)
        ↓ (standard capabilities around it)
evaluation · observability · guardrails · versioning · governance · provider ecosystems
```

The agent wave did not displace this Type; it stratified on top of it. Every sampled product still offers the model-call-first, developer-owned posture (Foundry's "single model call" tier; Dify's workflow/chatbot types; Bedrock's application framing; LangChain's "agents and applications"), while packaging the loop-owning agent pattern as a sub-mode. The canonical definition therefore stays at the substrate level, deliberately naming neither RAG, workflows, agents, cloud, nor any authoring surface.
