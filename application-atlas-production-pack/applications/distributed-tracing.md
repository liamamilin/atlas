# Distributed Tracing

## Overview

A **Distributed Tracing** application records, stores, and makes inspectable the end-to-end path of individual requests through a distributed software system. Each request's journey is captured as a **trace**: a causally ordered set of timed **spans** — one per unit of work — assembled across service boundaries by propagating trace context between services. Engineers use it to answer questions that aggregates cannot: where did this specific request go, how long did each step take, which hop failed or slowed down.

The defining structure is small:

```text
Instrumented services report spans
└── propagated trace context stitches spans across services into one per-request trace
    └── stored traces are individually retrievable (by ID or by search)
        └── traces are inspected span-by-span (structure, timing, attributes)
```

Everything else commonly associated with modern tracing — vendor SDKs, automatic instrumentation, sampling dashboards, service maps, span-derived metrics, log correlation — is widespread in current products but is not part of the defining core. The longest-standing tracing systems satisfied this definition with nothing more than instrumented libraries, HTTP or queue transports, and storage backends, without OpenTelemetry, cloud delivery, or AI analysis.

## Users & Context

The primary user is a software engineer or SRE who is debugging a specific request or investigating latency and errors in a system made of many services. Typical reasons to open the application:

- a customer, log line, or alert carries a trace ID — look up exactly what happened to that request
- an error rate or latency spike was reported by an aggregate signal — find example requests and locate the failing or slow hop
- a code change is suspected of slowing an endpoint down — compare recent traces against expected behavior
- a rare failure needs reproduction — find the traces in which it occurred and read their exact code path

Secondary users and concerns:

- service owners review their own services' trace-derived health (throughput, latency, error share)
- platform / observability engineers configure instrumentation rollout, sampling, and retention

The work context is incident triage and performance investigation in engineering teams operating microservice or multi-tier architectures. The characteristic position of tracing in the debugging loop: a metrics alert tells you that something is wrong; a trace investigation tells you why.

## Core Model

### The Defining Core

Four concepts. Remove any one and the product is no longer recognizable as distributed tracing.

- **Span** — the unit of recorded work. One operation — a service handling a request, a database query, a call to another service — recorded with an operation name, a start time, a duration, and **attributes**: structured key-value details (HTTP method and route, status, database system, queue name, error details). Spans nest: a span can contain child spans for the work it triggered.
- **Trace** — the per-request record. All spans sharing one trace ID, organized by parent-child relations into a tree (or more generally a directed acyclic graph) representing the request's causal path through the system. A trace is the answer to "what happened to this request".
- **Trace context propagation** — the mechanism that makes tracing *distributed*. The current trace ID and parent span ID travel with the request — injected into and extracted from request metadata such as HTTP headers or messaging properties — as it crosses service boundaries; each downstream service continues the same trace rather than starting a new one. Without propagation, each service would record isolated timing, which is precisely not tracing.
- **Trace retrieval & inspection** — stored traces are individually addressable. A specific trace can be looked up by its ID (the standard handoff from a log line, alert, or support ticket), and traces can be searched by attributes (service, operation, duration, tags, error state). An found trace is inspected span-by-span: the causal structure, the timing breakdown, and each span's attributes.

### Standard Capabilities of Mature Products

A typical modern tracing product carries most of these. They are not what makes the product tracing, but they make tracing practical:

- **Instrumentation tooling** — libraries and SDKs for producing spans, automatic instrumentation of common frameworks and protocols, and support for manual/custom spans. The origin of all trace data.
- **Open-protocol ingest** — collector endpoints accepting standard trace formats; mature products accept spans from more than one instrumentation ecosystem.
- **Sampling and ingestion controls** — because trace volume scales with request volume, products provide controls over what gets recorded and kept: sampling at the source (before a trace is complete), sampling in a processing layer after seeing whole traces, and tag- or attribute-based retention rules (for example, keep every error trace).
- **Trace storage** — pluggable or managed backends, with retention windows for individual traces that are typically far shorter than what teams want for aggregates.
- **Trace search and query** — attribute-based search over stored spans and traces; some products add a dedicated query language for selecting spans by structured conditions.
- **Trace detail visualization** — a waterfall or flame-graph view of the trace's spans, with per-span timing and attributes, plus links out to related logs and metrics.
- **Derived aggregates** — metrics computed from spans (per-service request rate, latency distributions, error rates) and service dependency maps inferred from observed calls between services.
- **Cross-signal correlation** — the trace ID as the join key: jump from a log line to its trace, from a metric data point (exemplar) to a representative trace, from a browser session or synthetic test run to the backend traces it triggered.

### One Structure, Many Implementations

The Core Model is written in conceptual terms. Common implementations differ:

```text
Concept:      Trace context propagation
Realized as:  standard header/metadata formats carried over HTTP, gRPC, or message queues

Concept:      Instrumentation
Realized as:  vendor SDKs, OpenTelemetry SDKs, framework auto-instrumentation,
              agent-based attach, or zero-code capture mechanisms

Concept:      Trace storage
Realized as:  in-memory (development use), search or columnar stores,
              object storage, or fully managed SaaS storage

Concept:      Trace query
Realized as:  form-based attribute search, or a dedicated query language
```

A reader who has only seen one implementation (for example, an OpenTelemetry-based SaaS product) should still be able to recognize an older or self-hosted tracing system from the Core Model.

## How It Works

### The tracing pipeline

```text
Instrument services
→ propagate trace context on every request hop
→ report spans to the ingest endpoint (often batched, via HTTP/gRPC/queue)
→ apply sampling and ingestion rules
→ store spans in the trace backend
→ find a trace (by ID or by search)
→ inspect the waterfall, span timings, and attributes
```

1. **Instrument services.** Each service gains the ability to produce spans — through an SDK, automatic instrumentation, or a capture mechanism. This is a one-time setup per service, revisited when new frameworks or services appear.
2. **Propagate context.** During each request, the first instrumented service starts (or continues) a trace; on every hop, the trace ID and current parent span ID ride along with the request metadata. Downstream services extract them and record their spans as children.
3. **Report spans.** Instrumented processes ship spans to the product's ingest endpoint, commonly in batches, over direct transports or through a message queue.
4. **Sample and retain.** Ingestion rules decide what is recorded and for how long: head sampling discards or keeps a trace at its first span; tail sampling decides after seeing the whole trace (for example, keep all traces with errors); retention rules decide how long stored traces live.
5. **Store.** Spans persist into the backend — a search or columnar store, object storage, or managed SaaS storage — indexed by the attributes needed for later search.
6. **Find a trace.** Either directly by trace ID (the common handoff from logs, alerts, or incident channels) or by search over attributes: which service, which operation, how slow, which error.
7. **Inspect.** The trace's waterfall shows the causal span structure and where the request's time went; each span exposes its attributes, and errors point at the failing hop.
8. **Move between signals.** From the trace, jump to the logs emitted during those spans; from a metrics anomaly or exemplar, jump to representative traces; service maps and span-derived metrics summarize what thousands of traces showed.

### Defining core vs standard capabilities vs optional

**Defining core** — without these, not distributed tracing:

- spans as the recorded unit of work
- causal assembly of spans into a per-request trace across service boundaries (context propagation)
- individual trace retrieval (ID lookup and/or attribute search)
- span-level inspection of structure, timing, and attributes

**Standard capabilities** — present in most modern products:

- instrumentation tooling (SDKs, auto-instrumentation)
- open-protocol ingest and collector pipelines
- sampling and ingestion controls
- trace search over structured attributes
- waterfall / flame-graph trace detail
- span-derived metrics and service dependency maps
- log↔trace and metric↔trace correlation

**Optional / variant** — depends on product philosophy, scale, and packaging:

- dedicated query language
- storage substrate choice (pluggable stores vs object storage vs managed)
- tail-based sampling infrastructure
- correlation breadth (RUM sessions, synthetic runs, profiles, database monitoring)
- alerting (present in suite and platform packages, absent from pure trace backends)
- zero-code capture mechanisms (era-current)

## Interfaces

The following surfaces are described conceptually. Exact names and layouts vary by product.

### Trace search / explorer

The entry surface for finding requests.

- Purpose: locate individual traces by attribute conditions or by trace ID.
- Typical information: service, operation, duration, error state, timestamp, trace ID; result lists with distribution summaries (latency percentiles, error shares).
- Primary actions: search/filter, open a trace, paste a trace ID, save or refine a query.

### Trace detail (waterfall / flame graph)

The core inspection surface — the reason the Type exists.

- Purpose: show one request's full causal path and time breakdown.
- Typical information: span tree, per-span duration bars on a shared time axis, service and operation names, span attributes, error markers, links to related logs.
- Primary actions: expand/collapse spans, inspect span attributes, jump to logs for a span, compare slow spans, copy the trace ID.

### Service / dependency map

- Purpose: show which services call which, as observed by traced traffic.
- Typical information: services as nodes, call relationships as edges, request volume/error/latency summaries per edge or node.
- Primary actions: navigate to a service's derived metrics, open representative traces.

### Derived metrics / service pages

- Purpose: monitor per-service and per-operation health computed from trace data, without reading individual traces.
- Typical information: request rate, latency distributions, error rates over time; sometimes deployment/version annotations.
- Primary actions: inspect trends, jump to example traces, build dashboards.

### Ingestion, sampling, and retention configuration

- Purpose: control what trace data is recorded and how long it is kept.
- Typical information: per-service sampling rates, retention rules, ingestion volumes.
- Primary actions: adjust sampling, define keep rules (for example, retain error traces), review ingest volume.

### Instrumentation setup surface

- Purpose: get services producing spans and sending them to the product.
- Typical information: per-language installation steps, supported frameworks, propagation configuration.
- Primary actions: install an SDK or agent, enable auto-instrumentation, add custom spans.

For self-hosted backends, a deployment/administration surface (storage backend configuration, ingest endpoints) replaces or complements the SaaS settings pages.

## Important Rules / Behaviors

### A trace is assembled from independently reported spans

Spans are produced and shipped by many services at different moments. The trace exists as a stitched whole only because context propagation and instrumentation are present on the request's path; where a service lacks instrumentation or fails to propagate context, the trace shows a gap or fragment. Trace completeness is therefore a property of the deployment, not a guarantee of the tool.

### Volume forces choices, and choices affect what can be found later

Trace volume scales with request volume, so every product exposes some control over capture and retention. The sampling decision has a lasting consequence: with source-side sampling, a request that was not sampled typically leaves no retrievable trace at all; with tag-based retention, only matching traces survive past the retention window. Understanding a product's sampling posture is part of understanding what its trace store means.

### Individual traces are ephemeral relative to their aggregates

Stored traces live for limited windows; the metrics derived from them are aggregated and kept far longer. A team can see from span-derived metrics that a service's latency rose last month, yet be unable to open an individual trace from that period. Aggregates answer "what changed"; traces answer "what happened" only within their retention horizon.

### The trace ID is the correlation key

The trace ID is the practical hinge between signals: it appears in log lines, can annotate metric exemplars, and links browser or synthetic-test sessions to backend paths. Much of the product's cross-surface value — "click the log, see the request" — rests on this single identifier being carried everywhere.

### Attributes are the query surface

What can be found later depends on what was recorded on spans now. This is why structured, richly attributed spans (service, operation, HTTP and database details, custom business keys) are the raw material of the whole Type: search, derived metrics, dependency maps, and correlation all read the same attribute fields.

## Variants

- **Self-hosted open-source trace backend** — pluggable storage backends, ingest APIs, and a web UI; the team operates storage and scaling. (e.g. Jaeger, Zipkin)
- **Object-storage-first backend** — a high-scale backend that deliberately reduces trace storage to cheap object storage and adds a query language on top; typically embedded in a broader open-source observability stack. (e.g. Grafana Tempo)
- **SaaS suite module** — distributed tracing as the drill-down core of an Application Performance Monitoring product, bundled with service pages, alerting, deployment tracking, and cross-signal correlation. (e.g. Datadog APM)
- **Observability-platform embedding** — traces as one signal among events, metrics, and logs, stored as structured events and analyzed with cross-signal, high-cardinality tooling. (e.g. Honeycomb)
- **Cloud-vendor tracing services** — tracing shipped as a native feature of a cloud provider's monitoring stack, with cloud-native instrumentation hooks.
- **Era-current extensions** — agent-based zero-code capture, and tracing applied to AI/LLM application flows, are emerging extension surfaces in current products.

A variant remains a variant unless it changes the defining core: any product in which individual requests cannot be traced end-to-end across services, retrieved by ID or search, and inspected span-by-span is not this Type regardless of its name.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Application Performance Monitoring / APM | closest sibling; shares the trace substrate | APM owns the service-health monitoring loop — aggregation dashboards, alerting, deployment tracking — with tracing as its drill-down core; a product whose center is the trace of record itself (collect, store, retrieve, inspect) without that monitoring loop is a tracing backend |
| Observability Platform | umbrella embedding | bundles traces, metrics, and logs with cross-signal investigation as the center; tracing machinery is one pillar among equally weighted signals |
| Log Management | adjacent; joined by trace-ID correlation | logs are per-service discrete records without request-scoped causal structure; tracing stitches request-scoped causal chains across services |
| Metrics Monitoring | adjacent; joined by span-derived metrics | time-series aggregates over time vs individual per-request records; metrics computed from spans ride exactly this seam |
| Profiler | adjacent | profilers analyze code-level hotspots within a process or run; tracing follows request paths across services |
| Synthetic Monitoring | adjacent; complementary | synthetic probes execute simulated requests; tracing observes real traffic; synthetic runs can inject trace context so their backend path appears as a trace |
| Service Mesh Management | substrate provider | a service mesh can supply propagation and telemetry via sidecars without application code; the trace system that receives and stores the result remains a tracing product |

The boundary with APM is the most consequential one because the market increasingly sells tracing inside APM and observability suites. The structural test: remove the service-health monitoring loop and keep raw trace collection, search, and inspection — what remains is still a complete Distributed Tracing application; remove the trace drill-down and keep only aggregates — what remains is metrics monitoring, not tracing.

## Representative Products

- **Jaeger** — CNCF open-source tracing backend; OpenTracing/OpenTelemetry-lineage data model; pluggable storage backends; self-hosted.
- **Zipkin** — the longest-standing open-source distributed tracing system; the historical anchor for this Type.
- **Grafana Tempo** — open-source high-scale trace backend requiring only object storage; TraceQL query language; part of the Grafana observability stack.
- **Datadog APM (distributed tracing)** — SaaS suite in which distributed tracing is the named core, bundled with service pages, monitors, and cross-telemetry correlation.
- **Honeycomb** — observability platform storing traces as structured events; trace-centric debugging with high-cardinality analysis.

The defining core was checked against the oldest sampled product (Zipkin, whose documentation requires no OpenTelemetry, cloud, or AI machinery) to avoid over-fitting the definition to the current era.

## Sources

Research date: **2026-09-08**. All sources below were fetched successfully on this date.

- Jaeger — Documentation and Terminology (v2.20): https://www.jaegertracing.io/docs/ , https://www.jaegertracing.io/docs/2.20/architecture/terminology/
- Zipkin — Project overview: https://zipkin.io/
- Grafana Tempo — Documentation home: https://grafana.com/docs/tempo/latest/
- Datadog — APM documentation home and APM Terms and Concepts: https://docs.datadoghq.com/tracing/ , https://docs.datadoghq.com/tracing/glossary/
- Honeycomb — Get Started and Traces, Metrics, and Logs: https://docs.honeycomb.io/get-started/ , https://docs.honeycomb.io/get-started/honeycomb/traces-metrics-logs/

> Sourcing note: research was based on each product's official documentation, one to two pages deep per product. Product-specific numeric controls (for example, exact retention windows or live-search windows) were observed in one vendor's documentation and are deliberately not stated as general facts in this document. Some capability presence (service maps in two open-source backends, sampling details in two products) was not verified at page level this pass and is phrased accordingly.

Detailed product-by-product observations, the cross-product comparison matrix, and the boundary analysis (including the joint review with the APM research) are recorded in the paired Research Notes.
