# LLM Observability Platform

## Overview

An **LLM Observability Platform** captures the runtime executions of LLM applications and makes them inspectable as structured, step-level traces.

LLM applications are non-deterministic: the same input can produce different outputs, and a failure can sit anywhere in the chain of calls an application makes — the model call itself, a retrieval step, a tool invocation, an orchestration decision. This Type of application solves the resulting visibility problem. It receives execution data from the running application, reconstructs each request as a trace — a structured, ordered record of steps such as model calls, tool calls, and retrieval operations, each with its inputs, outputs, timing, and errors — stores traces persistently, and provides surfaces to inspect single executions and monitor aggregates.

The defining core is small:

```text
Instrumented capture from the running application
└── Execution trace (one request, reconstructed as ordered, typed steps)
    └── Persistent, queryable store of traces
        └── Inspection surface (walk one execution step by step)
```

Everything else commonly associated with the category — cost dashboards, session grouping, quality scores, alerting, OpenTelemetry support, sensitive-data redaction — is standard capability that mature products add, not what makes the product an observability platform. The platform observes and records; it does not define, host, or run the application, does not sit in the request path deciding anything, and does not judge whether an execution was good (that is the evaluation loop built on top of it).

The workload spectrum of this Type runs from a single model call, through fixed multi-step chains and retrieval workflows, to autonomous agent executions where the model decides the sequence. The same platform and the same trace model serve all three; agents are the complex end of the spectrum, not a separate category. The same Type is also documented under the workload-centric name "Agent Observability Platform" (see Related Application Types).

## Users & Context

The primary user is an **AI engineer or developer** who has put an LLM-powered application into development or production and needs to answer "what exactly did the application do, and why did it behave this way?". Typical moments of use:

- a user report or an error came in — find the trace, see which step failed and what the model actually received and produced
- a change to a prompt, model, or tool is about to ship — inspect representative executions of the new version
- latency or cost is climbing — find which steps and which models drive it

Secondary users and contexts:

- **on-call / operations engineers** (especially where the platform is embedded in a broader observability suite): watch error rates, latency, and cost dashboards, and respond to alerts or anomalies
- **product and quality owners**: review samples of production conversations, attach feedback, and see quality trends over time
- **platform teams**: manage environments, retention, access, and instrumentation standards across several LLM applications

The work context is the development-and-operations loop of LLM applications: build → deploy → observe → fix → redeploy. The platform is read-side infrastructure for that loop.

## Core Model

### The Defining Core

```text
Instrumented capture
└── Trace  (one request / operation)
    └── Steps  (ordered, typed)
        ├── model call     — prompts in, completions out, token usage
        ├── tool call       — invocation of an external function or service
        ├── retrieval       — lookup against a knowledge source
        └── chain / workflow / agent step — the container grouping the above
    └── Attributes  (user, session, tags, metadata, environment, version)
└── Persistent, queryable trace store
└── Inspection surface
```

Four properties. If any one is removed, the product is no longer recognizable as an LLM observability platform:

- **Instrumented capture from the running system** — execution data is emitted by the LLM application itself (through an SDK, automatic framework instrumentation, explicit span creation, or collection at the model/gateway boundary) and received by the platform. The platform does not guess what happened; the application reports it.
- **The execution trace as the central record** — one request or operation, reconstructed as a structured, ordered record of steps. Steps carry inputs, outputs, duration, and error state. What makes the record *LLM-specific* is that model invocations are first-class steps carrying prompts, completions, and token usage — not opaque outbound HTTP calls — and that the non-model steps an LLM application performs (tool calls, retrieval, workflow containers) are typed steps too, so a chain or an agent execution reads as one structured whole rather than a pile of unrelated logs.
- **Persistent, queryable store across executions** — traces survive the live session and accumulate into a searchable body of history that can be filtered and segmented by attributes (user, session, tags, metadata, environment, application version).
- **Inspection surface** — open a single trace and walk its steps: what was sent to the model, what came back, which tool was called with which arguments, where time went, where it failed.

### Standard Capabilities

Mature products commonly add the following around the defining core. They make the platform practical, but a product lacking some of them can still be an observability platform:

- **Multi-turn grouping** — sessions or threads that collect the traces belonging to one user conversation, so a multi-turn interaction can be read as a whole.
- **Typed step vocabulary** — a shared set of step kinds beyond the minimum: embeddings, retrieval, fixed workflow containers, agent containers, guardrail checks, evaluator steps. Automatic framework instrumentation typically assigns these types; aggregation and filtering depend on them.
- **Token usage and cost tracking** — per model call and aggregated, usually broken down by model, provider, user, or feature.
- **Operational dashboards** — volume, latency, error rates, cost, and quality trends over time.
- **Alerts and anomaly surfacing** — notifications when a metric crosses a threshold; some products automatically detect outliers across dimensions such as step name, workflow type, or conversation topic.
- **Quality attachment** — scores, human annotations, or automated evaluations attached to individual traces or steps. This is the bridge to the evaluation loop (see Related Application Types).
- **Dual capture paths** — automatic instrumentation for popular frameworks and model providers, plus a manual instrumentation API for custom code and unsupported providers.
- **Asynchronous ingestion** — trace data is queued and sent in the background so recording does not slow the application.
- **OpenTelemetry compatibility** — the common modern substrate; several products accept standard telemetry so the same instrumentation can feed multiple destinations.
- **Governance surfaces** — project or workspace containers, environments (production / staging / development), release and version labels, retention management, and access control.
- **Privacy controls** — scanning and redaction of sensitive data inside prompts and completions; some products also flag prompt-injection attempts as recorded evaluations.
- **Export to datasets** — turning selected production traces into reusable test cases, which is how observability feeds evaluation.

### One Structure, Many Implementations

The core model is conceptual. Implementations differ in naming and substrate:

```text
Concept:            Step unit
Implementations:    span (OpenTelemetry lineage), run, observation, request log entry

Concept:            Model call step
Implementations:    "generation" with prompt/completion/token fields,
                    LLM-kind span with prompt/completion attributes

Concept:            Multi-step container
Implementations:    agent/workflow-kind span, agent-type observation,
                    session paths over related requests

Concept:            Multi-turn grouping
Implementations:    sessions, threads, conversation views

Concept:            Capture substrate
Implementations:    OpenTelemetry with AI semantic conventions,
                    vendor SDK with framework integrations, gateway/proxy capture
```

A reader who has only seen one product should still be able to recognize any other from this model.

## How It Works

### Instrument the application

The developer adds capture to the LLM application. The typical path is automatic instrumentation: enable an integration for the framework or model provider in use, and model calls, tool calls, and retrieval steps are recorded without further code changes. For custom logic or unsupported providers, the developer creates steps explicitly through an SDK or API, naming them and choosing their type. Where capture happens at a gateway or proxy instead, the application routes its model calls through the gateway, and each request is logged with its prompts, completions, tokens, and errors as a byproduct of passing through; the gateway posture expresses multi-step structure by tagging requests with a shared session and hierarchical path. Capture is configured per environment, so development and production traces can be separated.

### Capture an execution

```text
User request arrives
→ the application starts a trace
→ each step (model call, retrieval, tool call, decision) is recorded
   with inputs, outputs, timing, and errors as it happens
→ steps nest under their parent step
→ the completed trace is sent to the platform (usually asynchronously, in batches)
```

The trace is written once the execution happens; it is a record, not a plan. Multi-turn applications tag each trace with a session or thread identifier so later turns link to the same conversation.

### Inspect a single execution

```text
Open the trace list → filter to the failing or slow requests
→ open one trace → walk the step tree
→ read the exact prompt sent to the model and the completion returned
→ inspect the tool call: arguments generated, response received
→ see where time was spent and which step errored
```

This is the platform's defining interaction: turning "something went wrong" into "this retrieval returned irrelevant documents at step 3, so the model answered from the wrong context".

### Aggregate and monitor

Across many traces, the platform aggregates: request volume, latency distributions, error rates, token consumption and cost by model, and — where quality signals are attached — quality trends. Dashboards and saved views make these aggregates standing surfaces; alerts and anomaly detection turn them into proactive monitoring.

### Attach quality signals and feed the improvement loop

Humans review traces and record scores or annotations; automated evaluators (including LLM-as-judge patterns) score traces as they arrive — some products run these evaluators continuously over spans matching defined filters. Selected traces are exported into datasets, where a separate evaluation process scores new application versions against them. Observability thus supplies the raw material — real executions — for the evaluation and improvement loop, while remaining itself a record of what happened.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Trace list / explorer

The entry surface over all captured executions.

- typical information: time, duration, status, session, user, tags, environment, cost or token totals, top-level step name
- primary actions: filter and search, open a trace, save a view

### Trace detail (step tree)

The inspection surface for one execution.

- typical information: steps with type, name, duration; inputs and outputs per step (prompts, completions, tool arguments and results, retrieved documents); error type, message, and stack; model parameters and token usage
- primary actions: expand/collapse steps, copy or export content, attach a score or annotation, add the trace to a dataset

### Session / thread view

The conversation surface grouping a multi-turn interaction.

- typical information: the turns of the conversation, each linked to its trace; the step hierarchy across a multi-step workflow
- primary actions: read the exchange as messages, jump into an individual turn's trace, evaluate the conversation as a whole

### Dashboards

The aggregate surface.

- typical information: volume, latency, error rate, token usage and cost over time, breakdowns by model, provider, step type, user, or application version; quality trends where scores exist
- primary actions: change time range and filters, drill from an aggregate into the underlying traces

### Alerts / insights

The proactive-monitoring surface.

- typical information: threshold conditions and triggered alerts; automatically surfaced anomalies or outliers in operational metrics; quality monitors running over defined span groups
- primary actions: configure monitors, acknowledge and investigate an alert (which leads back to the trace explorer)

### Settings / governance

- typical information: projects or workspaces, environments, retention configuration, API keys, member roles, sensitive-data rules
- primary actions: create and configure projects and environments, manage retention and access, set redaction rules

## Important Rules / Behaviors

### Capture must not slow the application

Mature implementations send trace data asynchronously: events are queued locally and flushed in batches in the background. A consequence for practitioners: short-lived processes (scripts, jobs) can exit before buffered traces are sent, so some SDKs require an explicit flush before termination or the trace is lost.

### The trace is a record, not a control plane

The platform observes executions that the application performs; it does not decide, rewrite, or block them. Guardrail checks and policy decisions appear in traces as recorded steps or evaluations, but enforcing them at runtime belongs to guardrail and safety products, not to observability.

### Step typing drives everything downstream

Filtering, cost attribution, and quality aggregation depend on steps being typed correctly (model call vs tool call vs retrieval vs container). Framework integrations assign types automatically; manually created steps must be typed by the developer. An untyped or mislabeled step silently disappears from type-based aggregates.

### Coverage equals visibility

Only instrumented steps appear in traces. A tool the integration does not recognize, or a code path without manual spans, is invisible — the trace will show a gap, not the missing work. In the gateway posture, only what passes through the gateway is recorded: calls made directly to a provider from elsewhere never appear. Teams therefore extend instrumentation until the trace explains the whole execution.

### Traces are finite-lived; datasets are not

Hosted products typically retain traces for a limited period, after which they are deleted. The common pattern for preserving important executions is exporting them into datasets, which persist independently of trace retention.

### Prompts and completions are sensitive data

Traces contain exactly what users sent and what the model answered — often including personal or confidential content. Mature products provide scanning and redaction of sensitive data inside traces, and access control over who can read them.

### Quality scores are attached metadata

Scores, annotations, and evaluations are bound to traces or steps as attached signals. They change no execution state; they enrich the record and feed aggregate quality metrics.

## Variants

Common forms of the Type:

- **Open-source, self-hosted platform** — the trace store and UI run on the team's own infrastructure; chosen for data control and vendor neutrality; cloud editions usually exist alongside (e.g. Langfuse)
- **Gateway-bundled observability** — capture happens at an AI gateway that also provides routing, fallbacks, and billing; every logged request is a byproduct of passing through, with multi-step structure expressed via session grouping (e.g. Helicone)
- **OpenTelemetry-native platform** — built directly on OpenTelemetry and open AI semantic conventions; positions instrumentation as portable across vendors; offered as OSS, SaaS, and self-hosted tiers (e.g. Traceloop, Arize Phoenix)
- **Engineering-workspace companion** — observability, evaluation, and prompt tooling sold as one workspace attached to a developer ecosystem; agents and single-call applications share one data model (e.g. W&B Weave, LangSmith)
- **Embedded in an infrastructure-observability suite** — AI tracing as a product area inside a general observability platform, sharing its dashboards, alerting, security scanning, and billing; typical for enterprises that already run the suite (e.g. Datadog)

Scope also varies along a complexity gradient that the products themselves acknowledge: from single model-call monitoring (one step per trace), through fixed multi-step workflows, to autonomous agent executions. The same platform typically serves all three.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Agent Observability Platform | same Type under a workload-centric name | the researched products serve single-call LLM applications and agents with one data model; "agent" names the complex end (tool calls, agent steps, sessions), not a separate structure; market evidence — a major infrastructure vendor renaming its LLM observability product to "Agent Observability" while keeping the identical data model — supports treating the two names as one Type; consolidation is recommended |
| LLM Evaluation Platform | consumer of this Type's output | evaluation's central record is a scored run against defined criteria ("how good"); observability's is the execution trace ("what happened"); evaluation consumes traces and every observability product bundles some scoring — a gradient, not a wall |
| AI Gateway / Model Routing Platform | adjacent, shared request path | the gateway's defining act is routing and model selection, with logging as a byproduct; this Type's defining act is the trace record and inspection surface; one product can carry both capabilities |
| AI Cost / FinOps Platform | adjacent, shared telemetry | cost is one aggregated metric dimension here; the FinOps Type centers money — attribution, budgets, chargeback, forecasting |
| AI Safety / Guardrail Platform | complementary | guardrail results appear here as recorded steps or evaluations; runtime enforcement and blocking belong to the guardrail Type |
| Observability Platform / Distributed Tracing / APM | adjacent, shared machinery | same trace/span concepts, but generic service semantics; the AI-specific step content (prompts, completions, token usage, LLM-generated tool arguments) and AI analytics (cost per model, topic clustering) are what distinguish this Type |
| Log Management | degraded form without structure | application tracing is sometimes described as structured logs of requests; the enforced causal structure (nested steps bound to a trace) and typed AI semantics separate it from plain log management |
| ML Model Monitoring Platform | adjacent | centers on model health and drift in serving; this Type centers on application executions; both may consume inference telemetry |
| LLM Application Development Platform | bundler of this capability | the development platform defines and runs applications and typically includes tracing as a standard capability; the standalone platform captures executions of applications built anywhere |
| Data Observability Platform | unrelated namesake | observes data pipelines (freshness, schema, quality of data assets), not LLM application executions |

The two most important boundaries: against **evaluation** (trace vs scored run — the record of what happened vs the judgment of how good) and against **generic APM** (identical machinery, different step semantics). The boundary against Agent Observability Platform is not a structural one at all: research on both sides shows one Type, two names, and an audience gradient.

## Representative Products

- **Langfuse** — open-source, vendor-neutral LLM observability and application tracing; self-hostable or cloud; OpenTelemetry-based
- **Helicone** — AI gateway with observability in one platform; request-log substrate with session grouping; cost and reliability emphasis
- **Traceloop** — OpenTelemetry-native LLM monitoring (OpenLLMetry SDK or proxy capture); quality monitors on spans
- **W&B Weave** — observability and evaluation companion for AI engineering teams; agents and LLM applications on one data model

The defining model was cross-checked against the sample of the sibling pass (LangSmith, Arize Phoenix, Datadog), which covers the same Type from the agent-centric angle; the two samples converge on one structure.

## Sources

Research date: **2026-09-08**

Fetched this pass:

- Langfuse — Observability & Application Tracing: https://langfuse.com/docs/tracing
- Langfuse — Observability Data Model: https://langfuse.com/docs/observability/data-model.md
- Langfuse — Observation Types: https://langfuse.com/docs/observability/features/observation-types.md
- Helicone — Quickstart: https://docs.helicone.ai/getting-started/quick-start
- Helicone — Platform Overview: https://docs.helicone.ai/getting-started/platform-overview
- Helicone — Sessions: https://docs.helicone.ai/features/sessions
- Traceloop — Introduction: https://www.traceloop.com/docs/introduction
- Traceloop — Monitoring Introduction: https://www.traceloop.com/docs/monitoring/introduction
- W&B Weave — Documentation root: https://weave-docs.wandb.ai/

Imported research records covering the same Type from the agent-centric angle (fetched on their research dates):

- Datadog — Agent Observability overview and Terms and Concepts (fetched 2026-09-06)
- LangSmith — Observability concepts (fetched 2026-09-06)
- Arize Phoenix — Tracing tutorial (fetched 2026-09-06)

> Sourcing limitations: an incumbent-APM-vendor alternative (New Relic AI Monitoring) was unreachable (repeated 404s) and is not characterized anywhere in this document; W&B Weave observations are limited to its documentation root page (deeper pages were unreachable), so claims about that product are deliberately weakened; quality attachment and multi-turn grouping are stated as common based on the majority of the sample, not universally. Precise vendor-specific figures (retention periods, size limits, pricing) are intentionally omitted from this document.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis against neighboring Types are recorded in the paired Research Notes.
