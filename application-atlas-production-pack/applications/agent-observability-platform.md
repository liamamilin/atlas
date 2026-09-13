# Agent Observability Platform

## Overview

An **Agent Observability Platform** captures the runtime executions of AI agents and LLM applications and makes them inspectable as structured, step-level traces.

AI agents are non-deterministic: the same input can produce different reasoning paths, tool calls, and outputs, and a failure can sit anywhere in a multi-step chain. This Type of application solves the resulting visibility problem. It receives execution data from the running agent, reconstructs each request as a trace — a nested hierarchy of steps such as model calls, tool calls, and retrieval operations, each with its inputs, outputs, timing, and errors — stores traces persistently, and provides surfaces to inspect single executions and monitor aggregates.

The defining core is small:

```text
Instrumented capture from the running agent
└── Execution trace (one request, reconstructed as nested typed steps)
    └── Persistent, queryable store of traces
        └── Inspection surface (walk one execution step by step)
```

Everything else commonly associated with the category — cost dashboards, session grouping, quality scores, alerting, OpenTelemetry support, sensitive-data redaction — is standard capability that mature products add, not what makes the product an observability platform. The platform observes and records; it does not define, host, or run the agent, and it does not decide whether an execution was good (that is the evaluation loop built on top of it).

## Users & Context

The primary user is an **AI engineer or developer** who has put an LLM-powered application or agent into development or production and needs to answer "what exactly did the agent do, and why did it behave this way?". Typical moments of use:

- a user report or an error came in — find the trace, see which step failed and what the model actually received and produced
- a change to a prompt, model, or tool is about to ship — inspect representative executions of the new version
- latency or cost is climbing — find which steps and which models drive it

Secondary users and contexts:

- **on-call / operations engineers** (especially where the platform is embedded in a broader observability suite): watch error rates, latency, and cost dashboards, and respond to alerts or anomalies
- **product and quality owners**: review samples of production conversations, attach feedback, and see quality trends over time
- **platform teams**: manage environments, retention, access, and instrumentation standards across several agent applications

The work context is the development-and-operations loop of LLM applications: build → deploy → observe → fix → redeploy. The platform is read-side infrastructure for that loop.

## Core Model

### The Defining Core

```text
Instrumented capture
└── Trace  (one request / operation)
    └── Steps  (nested, ordered, typed)
        ├── model call      — prompts in, completions out, token usage
        ├── tool call       — invocation of an external function or service
        ├── retrieval       — lookup against a knowledge source
        └── agent step      — the LLM-decided sequence that contains the above
    └── Attributes  (user, tags, metadata, environment, version)
└── Persistent, queryable trace store
└── Inspection surface
```

Four properties. If any one is removed, the product is no longer recognizable as an agent observability platform:

- **Instrumented capture from the running system** — execution data is emitted by the agent application itself (through an SDK, automatic framework instrumentation, or explicit span creation) and received by the platform. The platform does not guess what happened; the application reports it.
- **The execution trace as the central record** — one request or operation, reconstructed as a structured, ordered hierarchy of steps. Steps carry inputs, outputs, duration, and error state. Two step semantics are what make the trace *AI-specific*: model invocations, which carry prompts, completions, and token usage as first-class data; and tool invocations, which carry the call an agent made to an external function or service. An agent-level step type groups the LLM-decided, dynamic sequence of a run — the container that distinguishes an agent execution from a fixed chain of calls.
- **Persistent, queryable store across executions** — traces survive the live session and accumulate into a searchable body of history that can be filtered and segmented by attributes (user, tags, metadata, environment, application version).
- **Inspection surface** — open a single trace and walk its steps: what was sent to the model, what came back, which tool was called with which arguments, where time went, where it failed.

### Standard Capabilities

Mature products commonly add the following around the defining core. They make the platform practical, but a product lacking some of them can still be an observability platform:

- **Multi-turn grouping** — sessions or threads that collect the traces belonging to one user conversation, so a multi-turn interaction can be read as a whole.
- **Typed step vocabulary** — a shared set of step kinds beyond the minimum: embeddings, retrieval, fixed workflow containers, guardrail checks, evaluator steps. Automatic framework instrumentation typically assigns these types; aggregation and filtering depend on them.
- **Token usage and cost tracking** — per model call and aggregated, usually broken down by model and provider.
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
Implementations:    span (OpenTelemetry lineage), run, observation

Concept:            Model call step
Implementations:    "generation" with prompt/completion/token fields,
                    LLM-kind span with prompt/completion attributes

Concept:            Agent execution container
Implementations:    agent-kind span, agent-type observation,
                    implicit nesting of runs under a root

Concept:            Multi-turn grouping
Implementations:    sessions, threads, conversation views

Concept:            Capture substrate
Implementations:    OpenTelemetry with AI semantic conventions,
                    vendor SDK with framework integrations, manual span API
```

A reader who has only seen one product should still be able to recognize any other from this model.

## How It Works

### Instrument the agent

The developer adds capture to the agent application. The typical path is automatic instrumentation: enable an integration for the framework or model provider in use, and model calls, tool calls, and retrieval steps are recorded without further code changes. For custom logic or unsupported providers, the developer creates steps explicitly through an SDK or API, naming them and choosing their type. Capture is configured per environment, so development and production traces can be separated.

### Capture an execution

```text
User request arrives
→ agent application starts a trace
→ each step (model call, tool call, retrieval, decision) is recorded
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

Humans review traces and record scores or annotations; automated evaluators (including LLM-as-judge patterns) score traces as they arrive; managed evaluation services grade conversations on dimensions such as relevance or failure to answer. Selected traces are exported into datasets, where a separate evaluation process scores new agent versions against them. Observability thus supplies the raw material — real executions — for the evaluation and improvement loop, while remaining itself a record of what happened.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Trace list / explorer

The entry surface over all captured executions.

- typical information: time, duration, status, session, user, tags, environment, cost or token totals, top-level step name
- primary actions: filter and search, open a trace, save a view

### Trace detail (step tree)

The inspection surface for one execution.

- typical information: nested steps with type, name, duration; inputs and outputs per step (prompts, completions, tool arguments and results, retrieved documents); error type, message, and stack; model parameters and token usage
- primary actions: expand/collapse steps, copy or export content, attach a score or annotation, add the trace to a dataset

### Session / thread view

The conversation surface grouping a multi-turn interaction.

- typical information: the turns of the conversation, each linked to its trace; timing and nesting across turns
- primary actions: read the exchange as messages, jump into an individual turn's trace, evaluate the conversation as a whole

### Dashboards

The aggregate surface.

- typical information: volume, latency, error rate, token usage and cost over time, breakdowns by model, provider, step type, or application version; quality trends where scores exist
- primary actions: change time range and filters, drill from an aggregate into the underlying traces

### Alerts / insights

The proactive-monitoring surface.

- typical information: threshold conditions and triggered alerts; automatically surfaced anomalies or outliers in operational metrics
- primary actions: configure monitors, acknowledge and investigate an alert (which leads back to the trace explorer)

### Settings / governance

- typical information: projects or workspaces, environments, retention configuration, API keys, member roles, sensitive-data rules
- primary actions: create and configure projects and environments, manage retention and access, set redaction rules

## Important Rules / Behaviors

### Capture must not slow the application

Mature implementations send trace data asynchronously: events are queued locally and flushed in batches in the background. A consequence for practitioners: short-lived processes (scripts, jobs) can exit before buffered traces are sent, so some SDKs require an explicit flush before termination or the trace is lost.

### The trace is a record, not a control plane

The platform observes executions that the agent application performs; it does not decide, rewrite, or block them. Guardrail checks and policy decisions appear in traces as recorded steps or evaluations, but enforcing them at runtime belongs to guardrail and safety products, not to observability.

### Step typing drives everything downstream

Filtering, cost attribution, and quality aggregation depend on steps being typed correctly (model call vs tool call vs retrieval vs agent container). Framework integrations assign types automatically; manually created steps must be typed by the developer. An untyped or mislabeled step silently disappears from type-based aggregates.

### Coverage equals visibility

Only instrumented steps appear in traces. A tool the integration does not recognize, or a code path without manual spans, is invisible — the trace will show a gap, not the missing work. Teams therefore extend instrumentation until the trace explains the whole execution.

### Traces are finite-lived; datasets are not

Hosted products typically retain traces for a limited period, after which they are deleted. The common pattern for preserving important executions is exporting them into datasets, which persist independently of trace retention.

### Prompts and completions are sensitive data

Traces contain exactly what users sent and what the model answered — often including personal or confidential content. Mature products provide scanning and redaction of sensitive data inside traces, and access control over who can read them.

### Quality scores are attached metadata

Scores, annotations, and evaluations are bound to traces or steps as attached signals. They change no execution state; they enrich the record and feed aggregate quality metrics.

## Variants

Common forms of the Type:

- **Open-source, self-hosted platform** — the trace store and UI run on the team's own infrastructure; chosen for data control and vendor neutrality; cloud editions usually exist alongside.
- **Framework-attached SaaS platform** — commercial platform tightly integrated with one agent-framework ecosystem; tracing, evaluation, and prompt tooling sold as one workspace.
- **Open-standards observability product** — built directly on OpenTelemetry and open AI semantic conventions; positions instrumentation as portable across vendors; offered both as OSS and as a managed enterprise tier.
- **Embedded in an infrastructure-observability suite** — AI tracing as a product area inside a general observability platform, sharing its dashboards, alerting, security scanning, and billing; typical for enterprises that already run the suite.
- **Embedded in an agent development platform** — tracing and analytics as a standard capability inside the platform where the agent is built; the standalone Type exists for teams whose agents are built across frameworks or in code.

Scope also varies along a complexity gradient that the products themselves acknowledge: from single model-call monitoring (one step per trace), through fixed multi-step workflows, to autonomous agent executions where the model decides the sequence. The same platform typically serves all three; agents are the complex end that gives the Type its name.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| LLM Observability Platform | closest sibling — probable same Type, different emphasis | the researched products serve single-turn LLM applications and agents with one data model; "agent" names the complex end (tool calls, agent steps, sessions), not a separate structure |
| Agent Evaluation Platform | consumer of this Type's output | evaluation's central record is a scored run against defined criteria ("how good"); observability's is the execution trace ("what happened"); evaluation consumes traces and every observability product bundles some scoring — a gradient, not a wall |
| Agent Development Platform | bundler of this capability | the development platform defines and runs agents and typically includes tracing as a standard capability; the standalone platform captures executions of agents built anywhere |
| Observability Platform / Distributed Tracing / APM | adjacent, shared machinery | same trace/span/session concepts, but generic service semantics; the AI-specific step content (prompts, completions, token usage, LLM-generated tool arguments) and AI analytics (cost per model, topic clustering) are what distinguish this Type |
| Log Management | degraded form without structure | application tracing is sometimes described as structured logs of requests; the enforced causal structure (nested steps bound to a trace) and typed AI semantics separate it from plain log management |
| ML Model Monitoring Platform | adjacent | centers on model health and drift in serving; this Type centers on application executions; both may consume inference telemetry |
| AI Safety / Guardrail Platform | complementary | guardrail results appear here as recorded steps or evaluations; runtime enforcement and blocking belong to the guardrail Type |
| Data Observability Platform | unrelated namesake | observes data pipelines (freshness, schema, quality of data assets), not agent executions |

The two most important boundaries: against **evaluation** (trace vs scored run — the record of what happened vs the judgment of how good) and against **generic APM** (identical machinery, different step semantics). Market evidence — including a major infrastructure vendor renaming its LLM observability product to "Agent Observability" while keeping the same data model — indicates the agent/LLM naming split describes audience emphasis, not two structures.

## Representative Products

- **Langfuse** — open-source, vendor-neutral LLM/agent observability; self-hostable or cloud; OpenTelemetry-based
- **LangSmith** (LangChain) — commercial platform attached to the LangChain ecosystem; tracing, evaluation, and prompt tooling in one workspace
- **Arize Phoenix** — open-standards observability (OpenTelemetry + OpenInference); OSS local deployment and managed enterprise tier
- **Datadog Agent Observability** — AI tracing embedded in a general infrastructure-observability platform (renamed from Datadog LLM Observability)

## Sources

Research date: **2026-09-06**

- Langfuse — Observability & Application Tracing: https://langfuse.com/docs/tracing
- Langfuse — Observability Data Model: https://langfuse.com/docs/observability/data-model
- Langfuse — Observation Types: https://langfuse.com/docs/observability/features/observation-types
- LangSmith — Observability concepts: https://docs.smith.langchain.com/observability/concepts
- Arize Phoenix — Tracing tutorial: https://arize.com/docs/phoenix/tracing
- Datadog — Agent Observability overview: https://docs.datadoghq.com/llm_observability/
- Datadog — Agent Observability Terms and Concepts: https://docs.datadoghq.com/llm_observability/quickstart/terms/

> Sourcing limitation: observations are drawn from the official documentation pages listed above, fetched on 2026-09-06. Deeper per-feature pages (Phoenix span reference, Datadog session grouping, LangSmith aggregation features) were not fetched; claims that depend on them are stated only where the fetched pages support them, and precise vendor-specific figures (retention periods, size limits) are intentionally omitted from this document.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis against neighboring Types are recorded in the paired Research Notes.
