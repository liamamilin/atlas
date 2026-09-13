# Research Notes — Distributed Tracing

Research date: 2026-09-08

## Research Goal

Understand Distributed Tracing as an Application Type from real products:

- what objects exist (trace, span, trace context) and how they relate;
- how the data pipeline works (instrument → propagate → report → sample → store → search → inspect);
- which capabilities are defining vs common-mature vs variant/optional vs vendor-specific;
- where the Type boundary sits relative to APM, Observability Platform, Log Management, Metrics Monitoring, Profiler, Synthetic Monitoring;
- resolve the pre-recorded joint-review flag vs `application-performance-monitoring-apm` (STATUS.md, recorded 2026-09-08 from the APM side).

## Initial Boundary (hypothesis before research)

- Core hypothesis: a distributed tracing application records the end-to-end path of individual requests across a distributed system as causally linked timed spans, stores them, and lets engineers find and inspect individual traces.
- Nearest neighbors: APM (drill-down core vs monitoring loop), Observability Platform (trace as one pillar), Log Management (per-service records vs request-scoped causal records), Metrics Monitoring (aggregates vs individual requests), Profiler (code hotspots vs request paths), Synthetic Monitoring (simulated vs real traffic).
- Open questions going in: is context propagation definitional or merely universal? Is instrumentation ownership definitional (must the product ship SDKs)? How thin is the standalone market? Where does sampling sit? Does alerting belong in the Type?

## Research Questions

1. How does each product's official documentation define trace and span?
2. How do spans produced in different services become one trace (propagation mechanism)?
3. How do traces get in (instrumentation, protocols, transports), get kept (sampling, retention), and get found (trace-ID lookup, attribute search)?
4. What inspection surfaces do users get (waterfall/flame graph, span attributes, dependency maps, derived metrics)?
5. What deployment shapes exist (self-hosted OSS backend vs SaaS vs suite module)?
6. Which capabilities repeat across the sample, and which are single-product?
7. Boundary test: what distinguishes a distributed tracing product from an APM / observability platform / log product?
8. Historical check: does the definition survive on Zipkin-era (pre-OTel, pre-cloud, pre-AI) machinery?

## Representative Products

| Product | Pole | Why selected |
|---|---|---|
| Jaeger | CNCF OSS trace backend, self-hosted, pluggable storage | ecosystem-standard standalone tracing; complete architecture docs |
| Zipkin | longest-standing OSS tracing system (early-2010s origin, background knowledge) | historical anchor for the market-sample check |
| Grafana Tempo | OSS high-scale backend, object-storage-only philosophy, dedicated query language | different storage/cost philosophy; explicitly backend-for-protocols |
| Datadog APM / Distributed Tracing | SaaS suite in which distributed tracing is a named product area | suite pole; shows how tracing is packaged inside APM |
| Honeycomb | observability platform, structured-event/high-cardinality philosophy | data-centric pole; traces as one signal with distinctive analysis model |

Coverage: market representativeness (2 OSS backends + 1 OSS stack backend + 2 SaaS), documentation completeness (all fetched successfully), different product philosophies (pluggable vs object-store vs event-store; standalone vs suite vs platform), different customer tiers (self-host free OSS → SaaS enterprise).

## Sources

All fetched 2026-09-08; all fetches succeeded on first attempt.

- Jaeger — Documentation index, Terminology (2.20): https://www.jaegertracing.io/docs/ , https://www.jaegertracing.io/docs/2.20/architecture/terminology/
- Zipkin — Home/overview: https://zipkin.io/
- Grafana Tempo — Docs home: https://grafana.com/docs/tempo/latest/
- Datadog — APM docs home, APM Terms and Concepts: https://docs.datadoghq.com/tracing/ , https://docs.datadoghq.com/tracing/glossary/
- Honeycomb — Get Started overview, Traces/Metrics/Logs: https://docs.honeycomb.io/get-started/ , https://docs.honeycomb.io/get-started/honeycomb/traces-metrics-logs/

## Product Observations

Evidence tags: A = directly observed in fetched official documentation; B = cross-product commonality; background = general market knowledge not verified this pass.

### Jaeger

- **Data model (A, Terminology page)**: span = "a logical unit of work that has an operation name, the start time of the operation, and the duration"; "spans may be nested and ordered to model causal relationships". Trace = "represents the data or execution path through the system. It can be thought of as a directed acyclic graph of spans." Baggage = "arbitrary user-defined metadata (key-value pairs) that can be attached to distributed context and propagated by the tracing SDKs" (references W3C Baggage).
- **Data-model lineage (A)**: model "inspired by the OpenTracing Specification", "logically very similar to OpenTelemetry Traces"; explicit mapping table tags↔attributes, span logs↔span events, span references↔span links, process↔resource.
- **Architecture surface (A, docs structure)**: APIs, Sampling (documented architecture component), Service Performance Monitoring (SPM — derived per-service metrics), Terminology; Deployment (Kubernetes, custom distribution, security); Storage Backends (Badger, Cassandra, ClickHouse, Elasticsearch, Kafka, Memory, OpenSearch); Operations (monitoring, performance tuning, troubleshooting); UI configuration page (UI exists as product surface).
- **Deployment (A)**: self-hosted, CNCF project.

### Zipkin

- **Self-definition (A, home)**: "Zipkin is a distributed tracing system. It helps gather timing data needed to troubleshoot latency problems in service architectures. Features include both the collection and lookup of this data."
- **Trace-ID retrieval (A)**: "If you have a trace ID in a log file, you can jump directly to it. Otherwise, you can query based on attributes such as service, operation name, tags and duration."
- **Summaries (A)**: "percentage of time spent in a service, and whether or not operations failed."
- **Dependency diagram (A)**: "showing how many traced requests went through each application… helpful for identifying aggregate behavior including error paths or calls to deprecated services."
- **Instrumentation (A)**: "Applications need to be 'instrumented' to report trace data to Zipkin. This usually means configuration of a tracer or instrumentation library." Reporting "via HTTP or Kafka, though many other options exist, such as Apache ActiveMQ, gRPC and RabbitMQ."
- **Storage (A)**: "stored in-memory, or persistently with a supported backend such as Apache Cassandra or Elasticsearch."
- **Historical anchor (A + background)**: the docs as fetched describe the full Type machinery with no OpenTelemetry, no cloud, no AI dependency. Origin early-2010s, Twitter lineage (background knowledge, not fetched).

### Grafana Tempo

- **Self-definition (A, docs home)**: "Grafana Tempo is an open-source, easy-to-use, and high-scale distributed tracing backend. Tempo lets you search for traces, generate metrics from spans, and link your tracing data with logs and metrics."
- **Type definition sentence (A)**: "Distributed tracing visualizes the lifecycle of a request as it passes through a set of applications."
- **Storage philosophy (A)**: "cost-efficient and only requires an object storage to operate."
- **Protocol openness (A)**: "use Tempo with open source tracing protocols, including Jaeger, Zipkin, or OpenTelemetry" — the backend explicitly does not own the instrumentation; it consumes standard formats.
- **Query language (A)**: TraceQL, "inspired by PromQL and LogQL… lets you precisely and easily select spans and jump directly to the spans fulfilling the specified conditions."
- **Metrics from traces (A)**: metrics-generator processor and TraceQL metrics.
- **Correlation (A)**: Grafana built-in data source; Loki derived fields ("jump to traces" from logs); Prometheus exemplars ("jump from Prometheus metrics to Tempo traces").

### Datadog APM / Distributed Tracing

- **Positioning (A)**: "Datadog Application Performance Monitoring (APM) provides AI-powered, code-level distributed tracing from browser and mobile applications to backend services and databases." Distributed tracing is the named core of the APM area.
- **Trace definition (A, glossary)**: "A trace is used to track the time spent by an application processing a request and the status of this request. Each trace consists of one or more spans."
- **Propagation (A)**: "Trace context propagation is the method of passing trace identifiers between services… injects identifiers, such as the trace ID and parent span ID, into HTTP headers as the request flows through the system. The downstream service then extracts these identifiers and continues the trace… stitch together individual spans from different services into a single distributed trace."
- **Instrumentation (A)**: Single Step Instrumentation (agent install + auto-instrumentation), Datadog SDKs, custom instrumentation, Dynamic Instrumentation from the UI.
- **Pipeline controls (A)**: Ingestion Controls ("adjust ingestion configuration and sampling rates by service and resource"; "send up to 100% of traces… for live search and analytics for 15 minutes"); Retention Filters (tag-based, "determine what spans to index… for 15 days"). The precise numbers (15 min live window, 15-day indexed retention) are product-specific and stay in these notes.
- **Surfaces (A)**: Trace Explorer (real-time search/analyze), Trace View (flame graph), Service page / Resource page (trace metrics: throughput, latency, error rates; deployment tracking with version comparison), Service Map, Software Catalog, APM Monitors (alerts).
- **Correlation (A)**: logs side-by-side with traces; RUM↔backend traces; synthetics↔traces; profiles; runtime metrics; span-based metrics ("track historical trends in application performance"); Baggage "propagate key-value pairs… across service boundaries… transmission of business data and other contextual information alongside traces."
- **Service model (A)**: Service/Resource taxonomy built on top of trace data; trace metrics "exportable to a dashboard or can be used to create monitors."

### Honeycomb

- **Signals model (A)**: traces, metrics, logs. Traces and logs stored as *structured events*: "labeled JSON objects sent over HTTP, indexed automatically on every field at ingest, and queryable without a predefined schema"; metrics are time-series in dedicated datasets.
- **Trace definition (A)**: "A trace is a record of a request as it travels through your system. It is made up of spans, each representing one unit of work, such as a database query or a service call. Spans share a trace ID that identifies which trace they belong to."
- **Parent-child rendering (A)**: "Honeycomb uses the parent-child relationships between spans, expressed via `trace.parent_id` and `trace.span_id`, to render a waterfall view of execution flow across your services." Span example shows fields: `service.name`, `http.*`, `db.system`, `duration_ms`, `trace.trace_id`, `trace.span_id`, `trace.parent_id` (OpenTelemetry instrumentation).
- **When to use traces (A)**: "Follow a specific request across multiple services; Understand execution flow and latency at the span level; Correlate errors or slowdowns with the exact code path that produced them."
- **Investigation pattern (A)**: "A metrics alert surfaces a problem… A trace investigation explains the cause"; "A metrics alert can tell you that something is wrong; a trace investigation tells you why."
- **Sampling (A)**: "you can sample your data to reduce volume while keeping aggregates statistically accurate… send one in a hundred `status:200`s but send every `status:500`. When your instrumentation includes a `sample_rate` on each event, Honeycomb uses it to scale counts."
- **Analysis layer (A, named feature)**: BubbleUp — "identify which dimensions differ most across a selected region of your data." Service map exists (A: sandbox tour "explore a service map").
- **Position (A)**: self-describes as observability platform ("high-cardinality observability"); trace is one of three signals, with the debugging-explanation role central. Private Cloud option for self-hosted-platform delivery.

## Cross-product Comparison

| Dimension | Jaeger | Zipkin | Tempo | Datadog APM | Honeycomb |
|---|---|---|---|---|---|
| Self-description | tracing system/backend (docs nav + terminology) | "a distributed tracing system" (A) | "distributed tracing backend" (A) | APM providing distributed tracing (A) | observability platform; traces one signal (A) |
| Span/trace model documented | A | A | A | A | A |
| Propagation documented | A (baggage, OTel alignment) | A− (implied by instrumented tracers; mechanism page not fetched) | A (accepts OTel/propagating protocols) | A (detailed inject/extract mechanism) | A (trace.parent_id/trace.trace_id fields) |
| Trace-ID direct lookup | not verified this pass | A (explicit) | A (search/TraceQL jump to spans) | A (trace search) | A (trace-ID fields queryable) |
| Attribute search over spans | A (query surface; nav) | A | A (TraceQL) | A (Trace Explorer) | A (any-field events query) |
| Waterfall / flame-graph inspection | A (UI + config page exists) | A (trace view screenshot) | A (Grafana visualization) | A (flame graph) | A (waterfall) |
| Sampling controls | A (Sampling architecture page) | not fetched | not fetched | A (Ingestion Controls) | A (sample_rate + guidelines) |
| Retention management | A (storage backends page set) | A (in-memory vs persistent backends) | A (object storage) | A (Retention Filters) | A (retention/cost docs) |
| Metrics derived from spans | A (SPM) | A (% time per service summaries) | A (metrics-generator, TraceQL metrics) | A (trace/span metrics) | A (aggregations over span events) |
| Dependency / service map | not verified this pass | A (dependency diagram) | not verified this pass | A (Service Map) | A (service map) |
| Log↔trace correlation | not verified this pass | A (trace ID in log jump) | A (Loki derived fields) | A (logs side-by-side) | A (OTel auto trace correlation) |
| Alerting in-product | no (out of OSS backend scope) | no | no | A (APM monitors) | A (triggers) |
| Deployment | self-hosted OSS | self-hosted OSS | self-hosted OSS | managed SaaS | managed SaaS (+ Private Cloud) |
| Owns instrumentation SDKs | ecosystem/OTel client orientation | ecosystem tracers | explicitly protocol-consumer (A) | yes (A) | yes (OTel-based; A) |

Reading: the trace substrate (spans → propagated causal traces → storage → retrieval → inspection) is A-evidenced in all five. Derived aggregates, log correlation, and dependency maps are common-mature (A in 3–5 products each; not verified in the remainder). Alerting is absent from all OSS backends and present in the two SaaS poles — packaging split, boundary-relevant.

## L0 — Defining Invariant

Three jointly-held structures. If any one is removed, the product is no longer recognizable as Distributed Tracing:

1. **Spans as the unit of recorded work** — timed operation records (operation name, start time, duration; attributes) reported from the application's own runtime via instrumentation. Spans nest and carry the raw material of the trace. Remove → request execution is recorded nowhere; nothing for the Type to exist on.
2. **Causal assembly into a per-request trace across service boundaries** — each span carries trace/parent identifiers that propagate across service calls, so spans produced in different services stitch into one per-request causal chain (the property that makes it *distributed* tracing rather than per-service timing). Remove → per-service timing logs or single-process profilers.
3. **Trace retrieval & inspection** — stored traces are individually addressable (trace-ID lookup and/or attribute search) and inspectable span-by-span (structure, timing, attributes). Remove → a telemetry collection pipeline; if only aggregates are computed and kept, the product becomes metrics monitoring.

Jointly-held is load-bearing:
- 1+3 without 2 = per-service timing-log search (not distributed)
- 2+3 without 1 = nothing recorded to retrieve
- 1+2 without 3 = a span pipeline with no trace-facing application

Note on "distributed": the invariant is the *capability* to assemble spans across process/service boundaries via propagated context. A deployment tracing a single service is a degenerate use of the same machinery (the products do not require a minimum service count).

## L1 — Common Mature Structure

Present in most/all sampled products (A in the noted products), but not required to recognize the Type:

- instrumentation layer as a first-class product surface: SDKs/libraries, automatic instrumentation of common frameworks, manual/custom spans (A ×5)
- open-protocol ingest: collectors/endpoints accepting standard trace formats (OpenTelemetry, Jaeger, Zipkin wire formats — A at Tempo explicitly; Jaeger data model OTel-aligned)
- sampling and ingestion controls (A ×3 direct: Jaeger page, Datadog, Honeycomb; structural reason: trace volume ∝ request volume)
- retention management for stored traces (A ×5 at page level; mechanics vary widely)
- attribute-based trace search (A ×5)
- waterfall/flame-graph trace detail with per-span attributes (A ×5)
- metrics derived from spans (per-service throughput/latency/errors, % time by service) (A ×5 under different names: SPM, metrics-generator, trace metrics, span summaries, span-event aggregations)
- service/dependency map derived from trace data (A ×3: Zipkin, Datadog, Honeycomb; not verified in Jaeger/Tempo this pass → phrase as "common", not universal)
- log↔trace correlation via trace ID (A ×4: Zipkin, Tempo, Datadog, Honeycomb; not verified in Jaeger this pass)
- collector/ingest pipeline with multiple transports (HTTP, gRPC, message queues) (A ×3+: Zipkin, Tempo, Datadog Agent)

## L2 — Variant / Optional Structure

- storage substrate: pluggable search/columnar stores (Cassandra/Elasticsearch/ClickHouse class) vs object-store-only vs managed SaaS storage (A; philosophy-level split between Tempo and Jaeger is explicit)
- query surface: form-based attribute search vs dedicated query language (TraceQL) (A)
- sampling economics: 100% ingest with short live window + indexed subset (Datadog pattern, A) vs sampled ingest with count-scaling (Honeycomb pattern, A) vs head/tail-based sampling machinery (Jaeger page; tail-sampling not verified this pass)
- correlation breadth: traces correlated with RUM/synthetics/profiling/DBM in suite poles (A Datadog) vs single-signal focus in backends
- alerting presence: none in OSS backends (A: out of scope of their docs) vs APM monitors / triggers in suite & platform poles (A) → packaging variant, boundary-relevant
- instrumentation mode: vendor SDKs vs OTel SDKs vs agent auto-attach vs eBPF-based capture (eBPF not verified this pass; era-current)
- private/self-managed SaaS delivery (Honeycomb Private Cloud, A)
- AI-era drift: Datadog markets "AI-powered" APM analysis; LLM/AI-workflow tracing extensions exist in market but were not researched this pass → do not promote

## L3 — Vendor-specific (research notes only)

- Datadog: Ingestion Controls semantics (100% live for 15 minutes; tag-based Retention Filters; 15-day indexed retention), Single Step Instrumentation, Dynamic Instrumentation from UI, Software Catalog, baggage propagated "between traces, metrics, and logs"
- Honeycomb: structured-event model (spans as JSON events indexed on every field), BubbleUp divergence analysis, dataset/environment/team resource structure, sample_rate count-scaling semantics
- Tempo: TraceQL (PromQL/LogQL-inspired), metrics-generator processor, Parquet backend + dedicated attribute columns, "only requires an object storage" positioning, Grafana-data-source embedding
- Jaeger: SPM naming, OpenTracing-lineage data model with explicit OTel mapping, Badger/Kafka/Memory storage options, adaptive sampling (page exists, content not fetched)
- Zipkin: dependency diagram prominence, B3 propagation (origin of B3 is background knowledge, not fetched)

## Rejected Findings (considered and NOT placed in the defining core)

- "Requires SaaS/cloud" — rejected: three self-hosted OSS products are complete trace systems (A).
- "Requires OpenTelemetry" — rejected: Zipkin predates it; Jaeger's model is OpenTracing-lineage; Tempo treats OTel as one of three accepted protocol families (A).
- "Requires alerting" — rejected: no OSS backend ships alerting; alerting belongs to the monitoring loop (APM/observability), not to the trace substrate (A ×3 absence).
- "Requires proprietary agents/SDKs" — rejected: Tempo explicitly consumes external protocols; instrumentation ownership is not definitional (A).
- "Service map is definitional" — rejected: it is a derived aggregate; not verified in 2 of 5 this pass (A ×3).
- "100% capture is definitional" — rejected: sampling is the norm and full capture is a configurable posture (A); conversely, sampling itself is also NOT definitional (small deployments run unsampled) → sampling sits in common/variant, not core.
- "Waterfall rendering is definitional" — rejected: the *inspection capability* is the invariant; waterfall/flame-graph is the standard presentation (A ×5 but presentation-level).
- "Multi-service minimum" — rejected as hard requirement: single-service tracing is a degenerate-but-valid use; the invariant is the cross-service assembly capability.

## Boundary Findings

**vs Application Performance Monitoring (APM)** — the load-bearing boundary; joint review with the APM pass:
- Shared substrate: spans/traces/propagation. The APM research characterized tracing as "APM's defining drill-down core".
- Seam test (confirmed from both sides): remove the service-health monitoring loop (aggregation dashboards, alerting, deployment tracking) but keep raw trace collection/search/inspection → you have a Distributed Tracing system (every OSS backend in this sample is exactly this). Remove trace drill-down but keep aggregates → metrics monitoring.
- Evidence: Datadog documents tracing *inside* APM together with monitors, deployment tracking, service pages (A); Jaeger/Zipkin/Tempo ship complete tracing with no alerting machinery (A); Honeycomb embeds traces in an observability platform (A).
- Market shape: products sold as standalone distributed tracing are predominantly OSS backends; commercial SaaS consumption of tracing is mostly inside APM/observability suites (consistent with the APM-side flag).
- **Joint review resolution: keep-both RATIFIED.** Sibling Types sharing the trace substrate: APM owns the service-health monitoring loop (its center of gravity) with tracing as its drill-down core; Distributed Tracing owns the trace of record itself (collection, storage, retrieval, inspection) as its center of gravity. Suite packaging that merges both is packaging convergence, not Type collapse.

**vs Observability Platform**: platform bundles traces + metrics + logs with cross-signal investigation as the center (Honeycomb self-describes this way, A). When trace machinery is one equally-weighted pillar among several signals and the product's center is the cross-signal analysis loop, the product is the platform Type with a tracing capability. Distributed Tracing's center is the individual trace of record.

**vs Log Management**: logs are per-service discrete event records without request-scoped causal structure; a trace is a request-scoped causal chain stitched across services. Seam: trace-ID-in-log correlation with jump links in both directions (A ×4).

**vs Metrics Monitoring**: time-series aggregates vs individual request records. Derived span metrics (trace metrics, SPM, TraceQL metrics) ride exactly this seam — they are computed *from* traces and retained as metrics (A ×5).

**vs Profiler**: code-level hotspots within a process/run vs request paths across services. Suite products blur slightly (Dynamic Instrumentation attaches live debug data to spans, A) but the centers differ.

**vs Synthetic Monitoring**: synthetic probes execute simulated requests; tracing observes real traffic. They connect: a synthetic test run can inject trace context so the test's backend path appears as a trace (A Datadog).

**vs Service Mesh Management**: a mesh can supply the propagation substrate (sidecars emitting/forwarding trace context) without application code; the trace system receiving and storing the result remains a Distributed Tracing product. Substrate provider vs record keeper.

## Historical / Market-Sample Check (applied before freezing L0)

- **Zipkin (early-2010s origin, background knowledge; fetched docs contain no OTel/cloud/AI/eBPF)**: satisfies the L0 candidate fully — instrumented reporting, HTTP/Kafka transports, persistent/in-memory storage, trace-ID lookup, attribute query, trace view, dependency diagram. No modern-era dependency is required. PASS.
- **Log-file trace-ID practice**: Zipkin's homepage documents jumping from a trace ID in a log file — the retrieval pattern predates modern backends. PASS.
- **Cloud-vendor native tracing (AWS X-Ray)**: noted by the APM pass as trace-centric with thin service-health aggregation; fits the L0 candidate with suite-adjacent packaging (background knowledge, not fetched this pass).
- **Conclusion**: L0 is not overfit to the current OTel/suite era. OTel, eBPF, AI analysis, cloud delivery all correctly excluded from the defining core.

## Uncertainties

- Jaeger/Tempo service-map presence not verified at page level this pass → final document says "common", not universal.
- Zipkin/Tempo sampling details not fetched; sampling as common-mature rests on 3/5 direct evidence + structural volume reasoning.
- Jaeger trace-ID lookup / log correlation not fetched; the claim is kept out of the comparison for Jaeger and phrased as common-mature from the other four.
- eBPF/zero-code instrumentation breadth not verified; kept as era-current variant with low strength.
- Standalone commercial market shape (e.g., cloud-vendor trace services, ServiceNow Cloud Observability lineage) not researched this pass; market-thinness judgment relies on the APM-side flag plus this pass's product set. No marketing-position claims made.
- LLM/AI-workflow tracing not researched; excluded from the final document.

## Final Synthesis

Distributed Tracing is the Application Type whose defining core is the **per-request trace of record**: spans reported by instrumented services, causally assembled across service boundaries through propagated trace context, stored, individually retrievable (by ID or search), and inspectable span-by-span. Around that core, mature products add instrumentation tooling, open-protocol ingest, sampling/retention controls, derived aggregates (span metrics, service maps), and log/metric correlation. Deployment spans self-hosted OSS backends, object-storage-first backends, SaaS suites (where tracing is the APM drill-down core), and observability platforms (where traces are one signal). The joint review with APM resolves as **keep-both sibling Types sharing the trace substrate**: APM owns the monitoring loop; Distributed Tracing owns the trace of record.
