# Research Notes — LLM Observability Platform

Research date: 2026-09-08
Leaf: LLM Observability Platform (DIRECTORY §13 Data, Analytics & AI Systems)
Slug: llm-observability-platform

## Research Goal

Understand what an "LLM Observability Platform" actually is as an Application Type, from real products branded on the LLM-observability side:

- what the central persistent record is (trace? span? request log? session?)
- how execution data gets from a running LLM application into the platform (SDK, auto-instrumentation, gateway/proxy, OTel)
- what step types are modeled (model calls, tool calls, retrieval, agent containers, …) and what each carries
- what users do with captured executions (inspect, aggregate, score, alert, export)
- **primary goal this pass**: resolve the joint-review flag hung by the agent-observability-platform pass — whether "LLM Observability Platform" and "Agent Observability Platform" are one Type (probable alias) or two
- confirm or sharpen the other pre-hung flags: llm-evaluation-platform (scored run vs trace), ai-gateway-model-routing-platform (gateway logging), ai-cost-finops-platform (cost as one metric vs money center), ai-safety-guardrail-platform (measurement vs enforcement)

Prior context from earlier passes (recorded in STATUS.md Boundary Issues):

- agent-observability-platform pass (2026-09-06): probable alias — Datadog renamed its product from "LLM Observability" to "Agent Observability" (page title/breadcrumbs; URL path still /llm_observability/) while keeping the identical span/trace data model; all four of its sampled products (Langfuse, LangSmith, Phoenix, Datadog) serve single-turn LLM apps and agents with one data model; Datadog's docs frame inference→workflow→agent as a complexity gradient of the same tracing tier.
- llm-evaluation-platform pass (2026-09-08): observability seam re-forwarded — evaluation's central record = scored run against criteria vs observability's execution trace; evaluation consumes traces (online scoring, span-level scoring, datasets-from-traces); gradient not wall.
- ai-gateway-model-routing-platform pass: gateway logging is a byproduct of being on the path (Portkey bundles a full observability suite; Helicone cited); gradient/capability.
- ai-cost-finops-platform pass: observability centers traces/quality with cost as one metric; FinOps centers money (attribution, budgets, chargeback).
- ai-safety-guardrail-platform pass: observability = measurement without decisions; guardrails = runtime screening + per-content decisions.

## Initial Boundary (pre-research hypothesis)

An LLM Observability Platform captures the runtime executions of LLM applications (model calls, chains, RAG steps, agent workflows), reconstructs each execution as a structured trace, stores traces persistently, and provides inspection and monitoring surfaces. Expected neighbors:

- Agent Observability Platform (sibling, processed) — the flagged probable alias
- LLM Evaluation Platform (sibling, processed) — scores executions; consumes traces
- Observability Platform / APM / Distributed Tracing / Log Management (§14) — same trace/span machinery, non-AI step semantics
- AI Gateway / Model Routing Platform (sibling, processed) — logging as byproduct of being on the request path
- AI Cost / FinOps Platform (sibling, processed) — money as the center vs cost as one metric
- ML Model Monitoring Platform (§13) — model health/drift, not application executions
- Data Observability Platform (§13) — data pipelines, namesake only

## Research Questions

1. What is the central persistent record, and what is its internal structure?
2. What step types exist, and what does each carry (prompts, completions, tokens, errors)?
3. How is data captured — SDK, auto-instrumentation, gateway/proxy, OTel?
4. Do products branded "LLM observability" model agent executions (tool calls, agent containers, multi-step workflows)? — **the alias test**
5. How are multi-turn interactions grouped (sessions/threads)?
6. What aggregation surfaces exist (dashboards, cost/latency/volume metrics, alerts, anomaly detection)?
7. How is quality attached to traces, and where does evaluation begin?
8. What delivery postures exist (OSS self-host, SaaS, suite-embedded, gateway-bundled, dev-companion)?
9. Where are the boundaries: vs evaluation, vs agent observability, vs gateway, vs FinOps, vs guardrails, vs APM/log management?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, different capture loci, and different customer tiers. Deliberately weighted toward products whose own branding says "LLM observability" (not "agent observability") to test the alias question from the LLM side; one product overlaps with the sibling pass's sample (Langfuse) as a direct comparison anchor.

| Product | Philosophy | Capture locus | Customer tier | Docs fetched this pass |
|---|---|---|---|---|
| Langfuse | open-source, vendor-neutral "LLM observability & application tracing"; self-host or cloud | SDK / OTel from the app | OSS + SaaS | langfuse.com/docs/tracing; /docs/observability/data-model.md; /docs/observability/features/observation-types.md |
| Helicone | AI gateway + observability in one platform; cost/reliability-forward; request-log substrate | gateway/proxy or SDK at the request boundary | developer/SMB + enterprise | docs.helicone.ai/getting-started/quick-start; /getting-started/platform-overview; /features/sessions |
| Traceloop | OpenTelemetry-native LLM monitoring (OpenLLMetry); quality-monitors on spans | SDK (OpenLLMetry) or Hub smart proxy | OSS + SaaS + self-host | traceloop.com/docs/introduction; /docs/monitoring/introduction |
| W&B Weave | observability + evaluation companion for AI engineering teams; agents-first framing but LLM apps equally served | OTel-compatible SDK / OTLP endpoint | enterprise (W&B customers) | weave-docs.wandb.ai (root) |

Imported first-hand evidence from sibling passes (recorded in the repo's research files, fetched by those passes):

| Product | Sibling pass | Key imported evidence |
|---|---|---|
| Datadog Agent Observability (fka LLM Observability) | agent-observability-platform | product rename with identical data model; span kinds (LLM/Workflow/Agent/Tool/Task/Embedding/Retrieval); three monitoring tiers keyed to trace shape (inference → workflow → agent) |
| LangSmith | agent-observability-platform | run/trace/thread/trajectory model; feedback/tags/metadata; projects |
| Arize Phoenix | agent-observability-platform | OTel+OpenInference; tracing/annotations/sessions triad |

Coverage check: OSS self-host vs gateway-bundled vs OTel-native vs dev-companion; SDK-side vs gateway-side capture; quality-forward vs cost-forward emphasis; plus the incumbent-suite perspective via the imported Datadog record. This complements (not duplicates) the sibling sample: 4 fresh poles, 1 overlap anchor.

## Sources

Fetched 2026-09-08 (Layer A unless noted):

1. Langfuse — Observability & Application Tracing overview: https://langfuse.com/docs/tracing
2. Langfuse — Observability Data Model: https://langfuse.com/docs/observability/data-model.md
3. Langfuse — Observation Types: https://langfuse.com/docs/observability/features/observation-types.md
4. Helicone — Quickstart: https://docs.helicone.ai/getting-started/quick-start
5. Helicone — Platform Overview: https://docs.helicone.ai/getting-started/platform-overview
6. Helicone — Sessions: https://docs.helicone.ai/features/sessions
7. Traceloop — Introduction: https://www.traceloop.com/docs/introduction
8. Traceloop — Monitoring Introduction: https://www.traceloop.com/docs/monitoring/introduction
9. W&B Weave — Documentation root: https://weave-docs.wandb.ai/

Imported from sibling-pass records (fetched by those passes on their research dates; see research/agent-observability-platform.md, research/llm-evaluation-platform.md):

10. Datadog — Agent Observability overview + Terms and Concepts (fetched 2026-09-06)
11. LangSmith — Observability concepts (fetched 2026-09-06)
12. Arize Phoenix — Tracing tutorial (fetched 2026-09-06)
13. W&B Weave — apply-scorer-to-call evidence (recorded in the llm-evaluation-platform pass)

Source-access limitations:

- New Relic AI Monitoring: attempted as the incumbent-APM pole; three different docs paths returned 404 (2026-09-08); abandoned per the retry rule. The incumbent-suite perspective is instead covered by the imported Datadog record. No New Relic claims are made anywhere in this research.
- W&B Weave: deeper doc pages (/weave/concepts/what-is-weave, /weave/quickstart, /llms.txt) returned 404 after the root page fetched successfully; Weave observations are limited to the root documentation page plus the evaluation pass's recorded evidence. Weave claims are correspondingly weakened.
- Helicone's evaluation surface: not verified on the fetched pages (platform overview mentions prompt management and cost, not evaluators); no Helicone evaluation claims are made beyond what the fetched pages state.
- No precise numeric limits, retention windows, or pricing figures from this pass's fetches are asserted beyond what the fetched pages literally state (Helicone's own published comparison table figures are recorded as L3 vendor marketing content only).

## Product Observations

### Langfuse (Layer A)

- Positioning: "LLM Observability & Application Tracing (Open Source)" (page seoTitle); "open source application tracing and observability for LLM apps. Capture traces, monitor latency, track costs, and debug issues across OpenAI, LangChain, LlamaIndex, and more."
- Problem framing: "Generative AI systems are inherently non-deterministic. Therefore, debugging your application without any observability tool is more like guesswork."
- The core of observability is "application tracing — structured logs of every request that capture the exact prompt sent, the model's response, token usage, latency, and any tools or retrieval steps in between."
- FAQ: observability = tracing + metrics + logging; tracing "records the flow of a request through your system, preserving causal relationships between operations"; in LLM apps tracing is "the most important observability tool because it captures the full context of each request — prompts, responses, tool calls, and their relationships."
- FAQ vs APM: "Langfuse is purpose-built for LLM applications… natively understands LLM-specific concepts like token usage, model parameters, prompt/completion pairs, and evaluation scores. Unlike general-purpose APM tools, Langfuse provides features specific to AI engineering: LLM-as-a-Judge evaluation, prompt management, experiments and datasets, and custom dashboards."
- Data model (first-hand): observations (individual steps: LLM calls, tool calls, retrieval steps; nestable; typed) → trace (single request/operation, e.g. one chatbot interaction; logical grouping of observations sharing a trace_id) → sessions (optional grouping of traces for the same user interaction, e.g. a chat thread). Trace-level attributes (user_id, session_id, tags, metadata) propagate onto every observation row.
- Observation types (first-hand): `event` (discrete), `span` (duration of a unit of work), `generation` (AI model generations incl. prompts, token usage and costs), `agent` ("decides on the application flow and can for example use tools with the guidance of a LLM"), `tool` (single action, e.g. function or API call), `chain` (link between steps, e.g. passing context from retriever to LLM call), `retriever` (read-only data retrieval, e.g. vector store), `evaluator` (assesses relevance/correctness/helpfulness of outputs), `embedding`, `guardrail` (protects against malicious content or jailbreaks).
- Framework integrations auto-set observation types (e.g. LangChain `@tool` → tool type); manual `as_type`/`asType` parameter; manual agent-workflow decorator example with nested tool observations.
- Capture: built on OpenTelemetry; "you're not locked into using only Langfuse-specific SDKs. You can also send your traces to multiple destinations at once, like Langfuse for LLM observability and Datadog for infrastructure monitoring."
- Ingestion: asynchronous, batched, non-blocking background export; short-lived applications "must explicitly call flush() before exiting" or traces are lost (first-hand, with diagrams).
- Use-of-traces features: model usage and cost tracking, quality monitoring with scores, custom dashboards (cost/latency/volume/quality), alerts when a metric crosses a threshold.
- **Alias-test relevance: a product whose own SEO title is "LLM Observability" carries the full agent step vocabulary (`agent`, `tool`, `chain`, `retriever`, `guardrail`) as first-class observation types.**

### Helicone (Layer A)

- Positioning: "We built Helicone to solve the hardest problems in production LLM applications: provider outages that break your app, unpredictable costs, and debugging issues that are impossible to reproduce. Our platform combines observability with intelligent routing… In short: monitor everything, route intelligently, never go down."
- Two operating modes: AI Gateway with pass-through billing (point the OpenAI SDK at the gateway URL; "Automatic Observability — Every request is logged with costs, latency, and errors tracked") or bring-your-own-keys observability-only mode.
- Capture locus: gateway/proxy — "Integration: Proxy or SDK" (its own comparison table vs LangSmith "SDK only" and Langfuse "SDK only").
- Self-description in the comparison table: "Helicone is unique in offering both AI Gateway and full observability in one platform"; table lists LangSmith and Langfuse as its observability peers (Full Observability ✅, Session Debugging ✅) — no LLM-vs-agent line exists anywhere in the vendor's own market map.
- Sessions (first-hand): "When building AI agents or complex workflows, your application often makes multiple LLM calls, vector database queries, and tool calls to complete a single task. Sessions group these related requests together, letting you trace the entire agent flow from initial user input to final response in one unified view."
- Sessions track "LLM calls", "vector database queries" (embeddings, similarity searches, retrievals), "tool calls" (function executions, API calls, custom tools), "any logged request". Hierarchy expressed via session-path headers with `/parent/child/grandchild` path syntax; session IDs group; session names filter.
- Documented real scenarios: cost spike attribution ("instant breakdown by user, feature, or any custom dimension"), wrong-answer debugging ("view the complete conversation history with session tracking; trace through multi-step workflows to find where it failed"), provider outage fallback, **"AI agent workflow is broken — session trees visualize the entire workflow across multiple LLM calls; trace exactly where the sequence breaks down"**.
- **Alias-test relevance: the gateway-capture pole explicitly serves agent workflows — its sessions feature is titled around AI agents, and its own marketing scenario list leads with an agent-workflow debugging case.**

### Traceloop (Layer A)

- Positioning: "Monitor, debug and test the quality of your LLM outputs"; features listed: "Get real-time alerts about your model's quality; Execution tracing for every request; Gradually rollout changes to models and prompts; Debug and re-run issues from production in your IDE."
- Capture: "Traceloop uses OpenTelemetry to monitor and trace your LLM application. You can install the OpenLLMetry SDK in your application, or use Traceloop Hub as a smart proxy to all your LLM calls." (SDK or proxy — both loci.)
- Quality attachment (first-hand, Monitoring intro): "Detect hallucinations and regressions in the quality of your LLMs… A monitor is an evaluator that runs on a group of defined spans with specific characteristics in real time. For every span that matches the group filter, it will run the evaluator and log the monitor result." Monitor evaluators: LLM-as-a-Judge (custom prompts) and built-in deterministic evaluators (structural validation, safety checks, syntactic analysis), connected to an evaluators library.
- If not using a supported LLM framework, "make sure to annotate workflows and tasks" — workflow/task step vocabulary present on the LLM-observability side too (consistent with Datadog's span kinds).
- Other product areas on the LLM-observability platform: datasets, playgrounds, evaluators/guardrails, experiments, prompt management (prompt registry), projects and environments, self-hosting (hybrid/full).

### W&B Weave (Layer A, root page only — see limitations)

- Positioning: "W&B Weave is an observability and evaluation platform that helps you track, evaluate, and improve your agents and LLM applications."
- Capabilities listed: "Trace and collect metrics about your agents built with popular SDKs and harnesses using Weave OTel-compatible SDK"; "Manually instrument your application's LLM calls and arbitrary functions to trace, version, and collect feedback about your application"; "Evaluate your agent's or application's responses using LLM judges and custom scorers."
- Agents view: "Pick a built-in integration for your agent SDK or harness and start tracing sessions, turns, LLM calls, and tool calls in the Agents view."
- OTel without SDK: "Quickly configure your OTel-instrumented agent to send traces to Weave's OTLP endpoint. No Weave SDK installation required."
- Workload tabs: "Trace an agent" and "Trace functions" — one platform, two workload entry points, one data substrate.
- **Alias-test relevance: a product that leads with "agents and LLM applications" models the same primitives (sessions, turns, LLM calls, tool calls) — the agent content is step vocabulary + views, not a separate structure.**

### Imported sibling evidence (Layer A from sibling passes)

- **Datadog** (agent-observability-platform pass, 2026-09-06): product renamed "LLM Observability" → "Agent Observability" with page breadcrumbs updated and URL path /llm_observability/ unchanged; "Each request fulfilled by your application is represented as a trace… A trace can represent: an individual LLM inference…; a predetermined LLM workflow…; a dynamic LLM workflow executed by an LLM agent." Span kinds: LLM, Workflow, Agent, Tool, Task, Embedding, Retrieval; three monitoring tiers keyed to trace shape (inference → workflow → agent); dashboards (cost/latency/performance/usage), Patterns (topic clustering), Insights (anomaly detection); evaluations (managed, custom/external); sensitive-data scan/redaction; OTel GenAI semantic conventions.
- **LangSmith** (agent-observability-platform pass): run = "a single unit of work executed by an agent" ("think of a run as a span"); trace = collection of runs for a single operation; thread = sequence of traces for a multi-turn session; trajectory = flat ordered message list; feedback/tags/metadata on runs; projects; integrations = "the equivalent of auto-instrumentation in general observability".
- **Arize Phoenix** (agent-observability-platform pass): "Observability is the practice of instrumenting your application so you can understand its internal state from its external outputs. For AI applications, this means capturing every LLM call, tool execution, retrieval operation, and generation"; tracing/annotations/sessions triad; OTel + OpenInference.
- **W&B Weave scoring** (llm-evaluation-platform pass): apply-scorer-to-call machinery (span/call-level scoring) — the shared trace-attachment substrate for evaluation.

## Cross-product Comparison

| Dimension | Langfuse | Helicone | Traceloop | W&B Weave | (imported) Datadog | (imported) LangSmith / Phoenix |
|---|---|---|---|---|---|---|
| Central record | Trace (trace_id grouping of observations) | Request log; session trees over requests | Trace via OTel spans | Traces/calls via OTel-compatible SDK | Trace (nested spans) | Trace (runs / spans) |
| Step unit | Observation (typed) | Request (hierarchy via session paths) | Span (OTel; workflow/task annotations) | Call | Span (typed: LLM/Workflow/Agent/Tool/Task/Embedding/Retrieval) | Run / span |
| Model-call step payload | prompts, completions, token usage, costs | prompts/completions, costs, latency, errors | spans with prompts/completions | inputs/outputs | prompts/completions, token metrics, model params | prompts/completions, tokens |
| Non-model step types | tool, chain, retriever, agent, embedding, guardrail, evaluator | vector-DB queries, tool calls, any logged request | workflow, task annotations | tool calls | tool, task, embedding, retrieval, workflow, agent | tool/retrieval runs; tool execution/retrieval spans |
| Multi-turn grouping | Sessions (optional) | Sessions (id + path + name headers) | not verified this pass | sessions, turns (Agents view) | unverified in sibling record | threads (LangSmith); sessions (Phoenix) |
| Capture locus | SDK / OTel from app | gateway/proxy or SDK | OpenLLMetry SDK or Hub proxy | OTel-compatible SDK or OTLP endpoint | SDK + auto-instrumentation | integrations + manual |
| Async/batched ingestion | first-hand documented (flush for short-lived) | not verified | not verified | not verified | not verified | not verified |
| Aggregation | cost/latency/volume/quality dashboards; alerts | cost breakdowns by user/feature/dimension; user metrics | real-time alerts on quality monitors | metrics collection (Agents view) | OOTB dashboards; Patterns clustering; Insights anomalies | not verified |
| Quality attachment | scores (LLM-as-judge, human, custom) | not verified this pass | monitors = evaluators on span groups (LLM judge + deterministic) | LLM judges + custom scorers | evaluations (managed/custom/external) | feedback (LangSmith); annotations (Phoenix) |
| OTel posture | built on OTel; multi-destination export | not verified | OTel-native (OpenLLMetry) | OTel-compatible; OTLP endpoint | OTel GenAI conventions | OTel analogy (LangSmith, unverified); OTel+OpenInference (Phoenix) |
| Governance | environments, releases/versions, tags, users | projects, environments; user/session segmentation | projects, environments | W&B account/project context | enterprise suite governance | projects |
| Delivery posture | OSS self-host + cloud | SaaS (+OSS heritage; self-describes open source) | OSS self-host + SaaS + hybrid | SaaS on W&B platform | embedded in infra-observability suite | SaaS (LangSmith); OSS+managed (Phoenix) |

**Cross-product commonalities (Layer B):** every product in the combined sample (fresh + imported, 7 products) has (1) a persistent central record per request/operation — the trace; (2) model invocations as first-class steps carrying prompts, completions, and token usage; (3) non-model steps (tool calls, retrieval, workflow containers) as first-class step types; (4) a persistent, queryable store segmentable by attributes (user, session, tags, metadata, environment, version); (5) an inspection surface over single executions; (6) multi-turn/session grouping (verified in 5 of 7; Datadog and Traceloop unverified on the fetched pages); (7) aggregation over traces (cost, latency, volume; dashboards; alerts/anomaly detection where evidenced); (8) quality attachment onto traces (scores/evaluations/monitors — verified in 5 of 7; Helicone unverified); (9) OTel compatibility or native OTel capture (verified in 5 of 7 fresh+imported; Helicone, LangSmith unverified).

**Alias-test verdict (the pass's central finding, Layer B):** the step vocabularies converge across both brandings. Langfuse ("LLM Observability" in its own SEO title) ships `agent`, `tool`, `chain`, `retriever`, `guardrail` observation types; Helicone's sessions feature is documented around AI agents (session trees over tool calls and vector queries; the "AI agent workflow is broken" scenario); Weave — nominally the agents-first pole — models "sessions, turns, LLM calls, and tool calls" for "agents and LLM applications" alike; Traceloop annotates workflows and tasks; Datadog's single data model spans inference→workflow→agent tiers with the rename as direct naming evidence; LangSmith's run is defined by what the agent does yet its same platform records single LLM calls. No product in either sample draws a structural line between "LLM observability" and "agent observability". The two leaf names describe one Application Type with an audience/naming gradient.

## Abstraction Levels

### L0 — Defining Invariant

An LLM Observability Platform is a product whose primary job is to capture the runtime executions of LLM applications and make them inspectable as structured, step-level traces.

Four invariants; remove any one and the product stops being this Type:

1. **Instrumented capture from the running system** — execution data is emitted by the LLM application itself (SDK, auto-instrumentation, manual spans, or collection at the model/gateway boundary) and received by the platform. Without it: nothing is observable.
2. **The execution trace as the central record** — one request/operation reconstructed as a structured, ordered record of steps, where model invocations (prompts, completions, token usage) are first-class steps and non-model steps (tool calls, retrieval, workflow containers) are first-class wherever the application performs them. Without the step-level structure and AI step semantics: log management or generic APM.
3. **Persistent, queryable store across executions** — traces survive the live session and can be searched, filtered, and segmented by attributes. Without it: an ephemeral debug console.
4. **Inspection surface** — open a single trace and walk its steps (inputs, outputs, errors, timing) to answer "what exactly happened in this execution". Without it: a telemetry pipeline, not an observability product.

Historical/market-sample check: the definition deliberately excludes OpenTelemetry (common modern substrate, not universal — Helicone and LangSmith posture unverified), SaaS delivery (Langfuse and Traceloop self-host), cost metrics and dashboards (aggregation layer), sessions/threads (optional grouping; Langfuse: "optionally"), scores/evaluations (the evaluation bridge), and any specific step-type vocabulary names (vendor taxonomies differ: observation vs span vs run vs request). The thin end of the market — early LLM request loggers of the pre-chain era (each captured request a single-step trace with prompt/completion/tokens/errors) — satisfies all four invariants, so the definition does not over-fit to today's chain/agent-era implementations. Conversely, a generic APM satisfies invariants 1, 3, 4 but fails the AI step semantics of invariant 2 — that semantics is what makes this a distinct Type rather than a configuration of APM; Langfuse's own FAQ draws exactly this line ("unlike general-purpose APM tools…").

### L1 — Common Mature Structure

Present in most mature products (Layer B), expected by the market, not definitional:

- multi-turn grouping: sessions/threads over traces
- typed step vocabulary beyond the minimum: model call (generation), tool call, retrieval, embedding, chain/workflow container, agent container, plus auxiliary types (event/task, evaluator, guardrail)
- token usage and cost tracking per call and aggregated, broken down by model/provider/user/feature
- operational dashboards: volume, latency, error rates, cost, quality trends
- alerts/monitors on metrics; anomaly/outlier surfacing (where evidenced: Langfuse alerts, Traceloop monitors, Datadog Insights)
- attribute segmentation: user, session, tags, metadata, environment, release/version
- quality attachment onto traces: human annotations/feedback, LLM-as-judge scores, managed evaluations, monitors
- dual capture paths: framework/provider auto-instrumentation + manual instrumentation API
- asynchronous, non-blocking ingestion (verified first-hand for Langfuse; treated as common practice)
- OpenTelemetry compatibility / open semantic conventions
- workspace/project containers; environments (production/staging/development)
- export of traces into datasets (bridge to evaluation); prompt management adjacency

### L2 — Variant / Optional Structure

Depends on segment, delivery, ecosystem, or workflow:

- delivery posture: OSS self-host vs SaaS vs embedded in an infrastructure-observability suite vs bundled with an AI gateway vs dev-companion bundling
- capture locus: SDK-side nested tracing vs gateway/proxy-side request capture with header-expressed hierarchies vs OTel pipeline ingestion (Helicone documents both proxy and SDK; Traceloop both SDK and Hub proxy)
- data substrate: OTel-native with open semantic conventions vs proprietary schema
- emphasis gradient: cost/reliability-forward (gateway posture) vs quality-forward (evaluator/monitor posture) vs engineering-workspace posture (eval+prompt+datasets around the trace store)
- production-traffic analytics: topic clustering of inputs/outputs (imported Datadog Patterns); user/feature cost attribution (Helicone)
- security posture: sensitive-data scanning/redaction, prompt-injection detection as monitoring features
- agent-graph / trajectory views as alternative projections (imported LangSmith trajectory)
- AI-assisted trace analysis (imported LangSmith Chat)
- IDE round-trip debugging (Traceloop: "debug and re-run issues from production in your IDE")

### L3 — Vendor-specific Structure (Research Notes only)

- Langfuse: observation-type list; observations-table storage with propagated trace attributes; flush() requirement for short-lived processes; multi-destination OTel export; SEO title literally "LLM Observability & Application Tracing (Open Source)"
- Helicone: Helicone-Session-Id/Path/Name header scheme; `/parent/child` path-syntax hierarchy; "group by function, not by time" path philosophy; AI Gateway with credits/0%-markup billing; edge deployment latency claims; its own comparison table vs OpenRouter/LangSmith/Langfuse (pricing figures, feature matrix) — marketing content, not structure
- Traceloop: OpenLLMetry SDK naming; Hub smart proxy; monitors = evaluators-on-span-groups with evaluator slugs; guardrails as evaluator category; experiments/playgrounds/datasets areas; hybrid self-hosting
- Weave: Agents view; workload tabs (agent vs functions); OTLP endpoint without SDK; W&B account context
- Datadog (imported): span-kind root-validity rules; three monitoring tiers; Patterns/Insights; Sensitive Data Scanner; product rename history
- LangSmith (imported): run/trace/thread/trajectory naming; 180-day SaaS retention; 25,000-run trace cap
- Phoenix (imported): OpenInference; uvx local serve

## Vendor-specific / Rejected Findings

- "LLM observability stops at single LLM calls; agents belong to a separate agent observability Type" — **rejected**: the alias-test evidence (Langfuse agent/tool types; Helicone agent sessions; Weave agents view; Traceloop workflow/task annotations; Datadog's inference→workflow→agent tiers on one data model; the rename). One Type.
- "LLM observability requires OpenTelemetry" — rejected as definitional: common substrate, not invariant. L1.
- "LLM observability requires cost tracking" — rejected: aggregation is L1; a minimal trace viewer satisfies the Type.
- "LLM observability = evaluation" — rejected: central records differ (trace vs scored run); scoring is attached capability (L1); the evaluation loop is the sibling Type's core.
- "LLM observability is the gateway" — rejected: the gateway is a capture locus (L2) and a bundling posture; Helicone's own product treats observability and routing as two capabilities of one platform, and standalone SDK-side products (Langfuse, Traceloop, Weave) are squarely in-Type without any gateway.
- "Sessions/threads are part of the definition" — rejected: optional grouping ("Optionally, sessions aggregate traces"). L1.
- Precise figures from vendor marketing tables (Helicone pricing rows) — L3 marketing content, kept out of the final document.

## Boundary Findings

1. **vs Agent Observability Platform (sibling, processed — JOINT REVIEW FLAG DISCHARGED).** Verdict: **same Type; probable alias confirmed; keep-both with consolidation recommendation.** Evidence: (a) Datadog renamed its product from "LLM Observability" to "Agent Observability" while keeping the identical span/trace data model and URL (imported Layer A); (b) every product branded on the LLM side carries the full agent step vocabulary and serves agent workflows first-hand (Langfuse `agent/tool/chain/retriever` types; Helicone agent session trees; Traceloop workflow/task annotations); (c) every product on the agent side equally serves single LLM calls (Datadog's LLM-inference tier; LangSmith runs; sibling record); (d) vendor market maps (Helicone's comparison table) list observability peers without any LLM-vs-agent line; (e) the L0 four-part core is identical on both sides. The load-bearing content of "agent" is step vocabulary (tool calls, agent containers), multi-turn grouping, and trajectory views — not a separate structure. "LLM" is the older/broader label (the application-centric name), "Agent" the newer workload-centric emphasis at the complex end of the same spectrum. Both documents stand, cross-referenced; alias consolidation recommended for the taxonomy owner; no directory change made from this side.
2. **vs LLM Evaluation Platform (sibling, processed — FLAG DISCHARGED, resolves the re-forwarded seam).** Gradient, not a wall — keep-both. The observability Type's central record is the execution trace ("what happened"); the evaluation Type's is the scored run against criteria ("how good"). Evaluation consumes traces (Traceloop monitors run evaluators on span groups; Weave applies scorers to calls — first-hand this pass + imported); every evaluation product bundles tracing and most observability products bundle scoring. Boundary test: remove scoring-against-criteria → observability remains; remove the persistent trace store → an eval runner remains. Consistent with the agent-evaluation and llm-evaluation passes' framing.
3. **vs AI Gateway / Model Routing Platform (sibling, processed — FLAG CONFIRMED from this side).** Gradient/capability relationship. The gateway is on the request path and logs as a byproduct; its defining act is routing/model selection. Helicone is the straddling pole — one product, two capabilities (its own words: "combines observability with intelligent routing") — while Langfuse/Traceloop/Weave are observability-only with no routing. Budget enforcement at the request path is the shared zone with FinOps (per the gateway pass).
4. **vs AI Cost / FinOps Platform (sibling, processed — FLAG CONFIRMED from this side).** Cost is one aggregated metric dimension of this Type (token/cost tracking, cost dashboards, cost attribution); the FinOps Type centers money (attribution, budgets, chargeback, forecasting). Same telemetry substrate, different center. Gradient.
5. **vs AI Safety / Guardrail Platform (sibling, processed — FLAG CONFIRMED from this side).** Guardrail results appear here as step types (Langfuse `guardrail` observation) and as evaluations (Traceloop guardrail evaluators; imported Datadog prompt-injection detection); runtime enforcement/blocking on the live I/O path is the other Type. Observability records; guardrails decide.
6. **vs Observability Platform / Distributed Tracing / APM (§14)** — adjacent Types sharing machinery. Same trace/span concepts and vocabulary (LangSmith: "think of a run as a span"; Langfuse built on OTel). The differentiator is the AI step semantics: prompts/completions, token usage, model parameters, tool calls with LLM-generated arguments, and AI-specific analytics (cost per model, topic clustering). Langfuse's own FAQ draws the line ("unlike general-purpose APM tools…"). Remove the AI step semantics → generic APM.
7. **vs Log Management (§14)** — the enforced causal structure (nested steps bound to a trace) plus typed AI semantics is the boundary; Langfuse itself defines application tracing as "structured logs of every request" — the structure is what separates it from plain log management.
8. **vs ML Model Monitoring Platform (§13)** — different center: model health/drift/serving metrics vs application executions. Adjacent; both may consume inference telemetry. Not researched in depth this pass.
9. **vs LLM Application Development Platform (sibling, processed)** — capability relationship, consistent with prior flags: dev platforms bundle tracing as a standard capability; this Type is the standalone form capturing executions of applications built anywhere. Bundling, not identity.
10. **Taxonomy observation.** The leaf name says "LLM", the market's products center LLM applications with agents as the complex end (consistent with the sibling's finding 8). Both names should eventually consolidate; until then both documents define the same Type from their respective angles.

## Uncertainties

- Helicone's quality-attachment surface (scores/evaluators) not verified on fetched pages; quality attachment claimed as common on 5-of-7 evidence, not 7-of-7.
- Datadog session grouping and Traceloop multi-turn grouping not verified on the pages fetched (by this pass or the sibling); multi-turn grouping claimed as common on 5-of-7 evidence only.
- Weave evidence limited to the docs root page (deeper pages 404); Weave claims are weakened accordingly.
- New Relic unreachable (404 ×3); the incumbent-APM-vendor pole is covered only via the imported Datadog record.
- Async/batched ingestion verified first-hand only for Langfuse; treated as common practice, not universal.
- Market share/adoption not researched; product selection reflects documentation accessibility and philosophical diversity.
- The market moves fast (Datadog renamed its product mid-2026); the naming gradient may drift further before any taxonomy consolidation.

## Final Synthesis

An LLM Observability Platform is a persistent platform for capturing and inspecting the executions of LLM applications. Its world contains four defining structures: (1) instrumented capture from the running application (SDK, auto-instrumentation, manual spans, or collection at the model/gateway boundary, increasingly over OpenTelemetry); (2) the execution trace as the central record — one request reconstructed as a structured, ordered set of steps, model invocations carrying prompts/completions/token usage as first-class data, tool calls, retrieval, and workflow/agent containers as first-class step types wherever the application performs them; (3) a persistent, queryable trace store segmented by attributes (user, session, tags, metadata, environment, version); (4) an inspection surface that answers "what exactly happened in this execution" step by step.

Work flows in a loop: instrument the application → capture executions as traces → inspect individual traces to debug failures → aggregate traces into metrics (cost, latency, volume, error rates) → attach quality signals (human annotations, LLM-as-judge scores, monitors) → alert on thresholds/anomalies → export interesting traces into datasets for the evaluation loop.

The Type's center of gravity is the trace, not the score (evaluation), not the request path (gateway), not money (FinOps), not runtime decisions (guardrails), not generic service spans (APM), and not unstructured request logs (log management). The workload spectrum runs from single model calls through fixed chains/RAG workflows to autonomous agent executions — one data model across all three, as the products' own tier framings and the Datadog rename confirm. "LLM Observability Platform" and "Agent Observability Platform" are two names for this one Type: an audience/naming gradient, recommended for consolidation while both documents stand.
