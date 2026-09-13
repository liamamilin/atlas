# Research Notes — Event Stream Processing Platform

Research date: 2026-09-08

## Research Goal

Understand what an Event Stream Processing Platform actually is as an Application Type: its core objects, the work its users do, how a processing job/pipeline lives and dies, which semantics and rules define its behavior, and where its boundary sits against event brokers, CDC platforms, batch/integration pipelines, the sibling Stream Analytics Platform leaf, and streaming databases.

## Initial Boundary

Hypothesis before research:

- Core use: continuously process unbounded streams of events (sensor readings, transactions, clickstream, telemetry, change records) with user-defined computation — transform, filter, enrich, aggregate, join, detect patterns — and emit results onward with low latency.
- Users: data/stream engineers, backend developers, platform teams; operators monitor running processing; some products add SQL surfaces for analyst-adjacent users.
- Nearest neighbors: Stream Analytics Platform (§13 sibling leaf), Message Queue Management (§14, event transport), Change Data Capture Platform (§13, processed — capture/delivery contract), ETL/ELT + Data Integration Platform (§13, processed — movement contract), streaming databases (Materialize/RisingWave class — no directory leaf), Log Management / Observability (§14), Industrial IoT Platform (§16).
- Known unknowns: whether the sibling leaf Stream Analytics Platform is separable on structure or only on marketing; whether a library-packaged processor (Kafka Streams) and a streaming database (Materialize) belong inside or outside the Type; whether event-time/watermarks and delivery guarantees are definitional or merely mature-era expectations.

## Research Questions

1. What are the core objects? (event, stream, source/connector, job/pipeline/topology, operator/transformation, state, window, timer/watermark, sink)
2. How is processing logic expressed? (code APIs, SQL, no-code editors)
3. What is the lifecycle of a processing job? (define → deploy → running → update → stop; failure and recovery)
4. Which semantics/rules govern behavior? (event time vs processing time, ordering, late data, delivery guarantees, fault tolerance via checkpoints/replay, scaling/parallelism)
5. What surfaces do users actually touch? (SDKs/IDEs, SQL clients, CLI/REST, management consoles, monitoring)
6. How do realizations differ? (cluster engine vs embedded library vs managed service vs streaming database; CEP lineage)
7. Where are the boundaries? (broker = transport; CDC = capture/delivery; ETL = bounded/scheduled; analytics = insight deliverable; streaming DB = query-served maintained datasets)

## Representative Products

| Product | Pole | Why sampled |
|---|---|---|
| Apache Flink | open-source dedicated stream processing engine (cluster, code + SQL) | canonical engine; the market's reference model for stateful, event-time processing; rich official docs |
| Apache Spark Structured Streaming | batch-first engine extended to streaming (micro-batch philosophy) | the opposite execution philosophy from true per-event engines; big installed base |
| Azure Stream Analytics | fully managed cloud service, SQL-first, portal/no-code surface | different customer tier and surface (managed PaaS, operator-friendly) |
| Kafka Streams | stream processing as an embedded client library (no separate compute cluster) | distinct packaging philosophy; evidence via Confluent's official docs (Apache site unreachable, see Sources) |
| Materialize | streaming database (boundary anchor, not a core sample) | sharpens the boundary: continuously-maintained queryable datasets vs deployed processing pipelines |
| Confluent Platform/Cloud docs (secondary) | commercial Kafka-ecosystem packaging (managed Flink, ksqlDB, Kafka Streams) | documents the broker-vs-processing split from inside one vendor and the managed/SQL pole |

Coverage achieved: open-source vs commercial; self-managed vs fully managed; per-event vs micro-batch execution; code vs SQL vs no-code authoring; cluster vs library packaging.

## Sources

All fetched 2026-09-08. Evidence layers: A = direct observation on the specific product's official docs; B = cross-product commonality; C = canonical inference.

1. Apache Flink — "Learn Flink: Hands-On Training" (overview) + full documentation TOC (concepts: stateful stream processing, timely stream processing, fault tolerance; SQL reference; deployment; operations) — https://nightlies.apache.org/flink/flink-docs-stable/docs/learn-flink/overview/ (A)
2. Apache Spark — Structured Streaming Programming Guide, Overview page — https://spark.apache.org/docs/latest/streaming/index.html (A)
3. Azure Stream Analytics — "Introduction to Azure Stream Analytics" — https://learn.microsoft.com/en-us/azure/stream-analytics/stream-analytics-introduction (A)
4. Kafka Streams — Confluent Platform documentation, "Kafka Streams for Confluent Platform" overview (client library for applications/microservices whose input and output data are stored in a Kafka cluster; Java/Scala) — https://docs.confluent.io/platform/current/streams/overview.html (A, via Confluent's official documentation of the Apache project) + Confluent docs landing (product catalog: managed Flink, Flink SQL, Kafka Streams, ksqlDB) — https://docs.confluent.io/ (A)
5. Materialize — Concepts index (sources, views, indexes, arrangements, sinks, reaction time) — https://materialize.com/docs/concepts/ (A, boundary anchor)

Source-access limitations:

- kafka.apache.org returned JS-redirect shells on both attempts (/, /documentation/streams/, /43/documentation/streams/core-concepts). Kafka Streams evidence relies on Confluent's official documentation of the library instead; per the evidence rules, no precise Kafka Streams operational details (guarantee configurations, state store tuning specifics) are asserted anywhere.
- Flink's marketing page (flink.apache.org/what-is-flink/) returned only a navigation shell; the documentation site (nightlies.apache.org) carried all Flink evidence.
- No CEP-vendor (Apama/StreamBase-class) official docs were fetched; the historical check is reasoned at concept level only (see Historical / Market-Sample Check).

## Product Observations

### Apache Flink (A)

- Core definition from official docs: stream processing = processing **unbounded** data streams; batch processing = bounded streams. "The input may never end, and so you are forced to continuously process the data as it arrives."
- Applications are **streaming dataflows** composed of user-defined **operators**, forming directed graphs from one or more **sources** to one or more **sinks**. Sources include message queues / distributed logs (Kafka, Kinesis named); results go to a wide variety of sink systems.
- **Parallel dataflows**: streams have partitions, operators have parallel subtasks (parallelism per operator); redistributing patterns (keyBy) repartition by key; ordering preserved one-to-one within partitions, non-deterministic across redistribution.
- **Timely stream processing**: event-time timestamps recorded in the data (vs machine clocks); reasoning about when a set of events "is complete"; watermarks generate progress (docs nav: Generating Watermarks).
- **Stateful stream processing**: how one event is handled depends on the accumulated effect of all prior events; state = sharded key-value store held locally per parallel instance; used from simple per-minute counting (dashboards) to features for fraud models.
- **Fault tolerance**: state snapshots (checkpoints) + stream replay → exactly-once semantics; savepoints for upgrades; state backends; checkpointing under backpressure; state TTL/schema evolution/serialization machinery.
- **SQL layer**: Flink SQL with CREATE STREAM/TABLE DDL, INSERT into targets, windowing TVFs, group/over aggregation, window joins, temporal joins, Top-N, deduplication, MATCH_RECOGNIZE pattern recognition, changelog conversion; SQL Client / SQL Gateway (REST), JDBC driver; "Materialized Table" concept.
- **APIs**: DataStream API (and V2), Table API, Process Functions, Async I/O, side outputs; CEP library ("Event Processing (CEP)"); ML library; Flink CDC as a separate project (Debezium/Canal/Maxwell/Ogg formats among connectors).
- **Operations**: REST API; metrics/traces/events reporting; monitoring checkpoints and back pressure; upgrading applications and Flink versions; production-readiness checklist; HA via ZooKeeper/K8s; elastic scaling; adaptive batch; deployment on standalone/Kubernetes/YARN with JobManager/TaskManager memory configuration.
- Job concept is first-class: JOB statements in SQL, job status listeners, application lifecycle docs.

### Apache Spark Structured Streaming (A)

- Self-definition: "a scalable and fault-tolerant stream processing engine built on the Spark SQL engine."
- Programming model: express the streaming computation the same way as a batch computation on static data; the engine "will take care of running it incrementally and continuously and updating the final result as streaming data continues to arrive." (Unbounded table model: a continuously appended input table.)
- Capabilities named in the overview: streaming aggregations, event-time windows, stream-to-batch joins.
- Guarantees: end-to-end exactly-once fault tolerance through checkpointing and write-ahead logs.
- Execution modes: default **micro-batch** engine (streams processed as a series of small batch jobs); optional **Continuous Processing** mode (introduced Spark 2.3) for lower latency with at-least-once guarantees — mode chosen per query without changing the query code.
- APIs: Dataset/DataFrame in Scala/Java/Python/R.

### Azure Stream Analytics (A)

- Self-definition: "a fully managed stream processing engine" (PaaS) that "analyzes and processes large volumes of streaming data"; sub-millisecond latency claim (vendor claim — not propagated).
- Canonical pipeline stages: **Ingest → Analyze → Deliver**. Inputs: Azure Event Hubs, IoT Hub, blob storage for historical data, **reference data** (static/slow-changing, joined with the stream for lookups). Outputs: storage systems (Blob, SQL DB, Data Lake, Cosmos DB), other services (Event Hubs, Power BI for real-time visualization).
- Authoring: **SQL query language augmented with temporal constraints**; supports CEP functions, pattern matching, anomaly detection, geospatial functions; JS/C# UDFs/UDAs; Azure ML function invocation; **no-code editor** (drag-and-drop) for building jobs; query testing against sample data extracted from the live stream.
- Job model: a **job** connects inputs → query → outputs; created in the portal or via VS Code/VS/CLI/PowerShell/Bicep/ARM/Terraform with CI/CD submission.
- Reliability semantics (documented): exactly-once event **processing**, at-least-once **delivery** (exactly-once delivery only for selected outputs); built-in checkpoints maintaining job state; built-in recovery on delivery failure; repeatable results.
- Scale model: **streaming units** consumed (pay-per-unit, no cluster provisioning); scale up/down; partitioned parallel execution.
- Deployment variants: cloud, or on IoT Edge / Azure Stack with the same query language (hybrid architectures).
- Scenario framing: anomaly detection in sensor data, geo-fencing/fleet, remote monitoring/predictive maintenance, clickstream analytics, real-time telemetry/log analysis.

### Kafka Streams (A via Confluent docs; Apache site unreachable)

- Definition (Confluent Platform docs, official documentation of the Apache library): "a client library for building applications and microservices, where the input and output data are stored in an Apache Kafka cluster. It combines the simplicity of writing and deploying standard Java and Scala applications on the client side with the benefits of Kafka's server-side cluster technology."
- The Confluent docs catalog labels it: "Build stateful stream processing applications directly in Java."
- Documentation structure observed: Concepts, Architecture, Developer Guide (DSL API, Processor API, data types/serialization, interactive queries, memory management, application reset tool, streams rebalance protocol), Operations (metrics, monitoring, sizing), Upgrade, FAQ.
- Structural significance: stream processing exists as an embedded library inside ordinary applications — no separate processing cluster to deploy; the broker holds input/output; the application instance is the processing unit.

### Materialize (A — boundary anchor)

- Organizing objects: **sources** (external systems: Kafka, Postgres/MySQL/SQLServer CDC, webhooks), **views / indexes / materialized views** incrementally maintained ("arrangements" — in-memory maintained structures), **sinks** (external targets incl. Kafka, Iceberg, Snowflake), **clusters** (pools of compute), Postgres-wire-compatible SQL surface, roles/privileges, BI-tool serving, `SELECT`/`SUBSCRIBE` query serving, "reaction time" = data freshness + query latency.
- The product is a database whose contents are continuously updated from streams; users query it. There is no deployed "processing job/pipeline" object whose results flow onward — the maintained queryable dataset is the product. Used here to sharpen the streaming-database boundary, not as a core sample of the Type.

### Confluent platform framing (A — packaging/positioning evidence)

- Confluent's docs catalog separates: **Stream** (Kafka clusters, topics, consumer groups — transport/storage), **Connect** (integration connectors), and **Process** ("Transform, analyze, and act on real-time data" — managed Flink, Flink SQL, Kafka Streams, ksqlDB). This is direct vendor evidence that event transport and event processing are distinct product categories even within one ecosystem.
- ksqlDB ("process and query streaming data in real time using SQL directly against Kafka topics") documents the SQL-on-streams pole with push/pull queries and materialized views — a straddler toward the streaming-database reading.
- AI-era packaging (streaming agents, built-in ML functions, model inference in SQL) is present but era-current and vendor-branded.

## Cross-product Comparison

| Dimension | Flink | Spark Structured Streaming | Azure Stream Analytics | Kafka Streams |
|---|---|---|---|---|
| Input substrate | unbounded streams (also bounded for batch mode) | unbounded, modeled as a continuously appended table | event streams from hubs/IoT/blob + reference data | streams stored in a Kafka cluster |
| Unit of user work | job / streaming dataflow (operator graph) | query over a DataFrame | job (input → SQL query → outputs) | application/microservice embedding the library |
| Logic expression | code APIs (DataStream/Table) + SQL | DataFrame/Dataset code (SQL engine) | SQL with temporal constraints; no-code editor; UDFs | Java/Scala DSL + lower-level Processor API |
| State | first-class, sharded, snapshot-backed | engine-managed (checkpointing + WAL) | built-in checkpoints, repeatable results | stateful applications; state stores (per docs structure) |
| Time | event time + watermarks first-class | event-time windows | temporal constraints in SQL; windowing | time/window concepts (docs structure) |
| Fault tolerance | checkpoints + replay → exactly-once | exactly-once via checkpoint + WAL | exactly-once processing, at-least-once delivery | documented under developer/operations guides (not asserted in detail here) |
| Execution model | continuous, per-event | micro-batch (default) or continuous mode | managed continuous | in-process, continuous |
| Packaging | self-managed cluster (also managed via cloud vendors) | engine inside Spark deployments | fully managed PaaS (+ edge runtime) | client library inside user applications |
| Primary surface | code + SQL client/CLI/REST + ops APIs | code + Spark tooling | portal / no-code editor / CLI / IaC | embedded in application code |

### Shared structure (B — cross-product commonality)

All sampled stream processors share:

1. Event streams as continuous, unbounded input from external producers.
2. A persistent, user-defined computation (declared once, running continuously as events arrive).
3. Continuous delivery of derived results to downstream systems/streams.
4. Sources and sinks as connectable surfaces (connector ecosystems).
5. Stateful aggregation over streams (windows/accumulations) with the engine managing that state.
6. Fault tolerance machinery (checkpointing + replay/reprocessing) with stated delivery/processing guarantees.
7. A long-running job/query lifecycle: define → deploy/run → monitor → update → stop.
8. Horizontal parallelism (partitioning by key; scaling out).
9. Operational observability (metrics/monitoring; REST/management APIs).
10. A SQL surface (Flink SQL, ASA SQL, ksqlDB) beside code APIs in 3 of 4 core samples; ASA and Confluent add no-code/managed surfaces.

### Differences (implementation, not Type)

- Execution mechanics: per-event continuous (Flink, Kafka Streams) vs micro-batch with continuous option (Spark) vs managed opaque (ASA). The micro-batch/continuous spectrum is an implementation trade-off (latency vs throughput/guarantees), not a Type boundary — the same user mental model (continuously updated results) holds.
- Authoring style: Java/Scala/Python code vs SQL vs no-code.
- Where state lives: in the processor's own cluster vs in the application process vs hidden inside the managed service.
- Cloud vs self-managed vs embedded library packaging.

## Abstraction Hierarchy

### L0 — Defining Invariant (jointly held, deliberately small)

An Event Stream Processing Platform is exactly a system in which:

1. **Unbounded event streams are the input substrate** — continuous, potentially endless sequences of timestamped event records produced by external systems, consumed as they arrive (Flink's bounded/unbounded distinction; Spark's unbounded table; ASA's ingest stage; Kafka Streams' Kafka-stored input). Remove → batch processing on files/tables, or a request-response application.
2. **User-defined computation runs continuously over those streams** — processing logic (transform, filter, enrich, aggregate, join, detect patterns) declared by the user and executed persistently, per-event as data arrives, not triggered on a schedule or per-request (Flink operators; Spark incremental query; ASA SQL job; Kafka Streams DSL/Processor API). Remove → an event broker/consumer (transport only) or a scheduled batch program.
3. **Derived results are produced and delivered continuously** — outputs emitted onward as they are computed (new streams/sinks/systems), keeping downstream consumers current (Flink sinks; Spark streaming sinks; ASA deliver stage; Kafka Streams output topics). Remove → analytics over stored data.

Jointly-held is load-bearing: 1 alone = message queue/event broker; 2+3 without 1 = ordinary program or batch ETL over bounded data; 1+2 without 3 = inert computation, not a platform result.

Not in L0 (checked against §24-style historical reasoning):

- **Distributed cluster / parallelism** — Kafka Streams is a library; CEP-era engines were often single-node. The Type survives without a cluster. (Parallel scale-out is L1.)
- **Event-time/watermark machinery** — conceptually near-universal in the current market but an era-current refinement; older/regional stream processors ran on processing time. (L1.)
- **Exactly-once guarantees** — mature-era capability with per-output caveats even today (ASA documents exactly-once processing with at-least-once delivery). (L1.)
- **SQL, no-code, dashboards, ML, anomaly detection** — authoring/analysis surfaces, not the Type.
- **Specific connectors, formats, windows taxonomies, state backends** — implementations.

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Connector ecosystem for sources/sinks (brokers, CDC formats, databases, files, SaaS, BI).
- Keyed/stateful processing with managed fault-tolerant state; windowed aggregation (tumbling/sliding/session).
- Event-time semantics with progress/lateness handling (watermarks or equivalent temporal constraints).
- Delivery/processing guarantee machinery (checkpoint + replay; at-least-once baseline, exactly-once in the mature layer).
- Long-running job lifecycle with update/upgrade paths (savepoints/state migration or managed equivalents).
- Elastic parallelism (partition-by-key, scale units).
- Metrics/monitoring/management APIs (REST, consoles).
- SQL layer over streams; pattern-detection (CEP) functions; reference-data enrichment.

### L2 — Variant / Optional Structure

- Packaging: self-managed cluster engine / embedded library / fully managed cloud service / edge runtime (ASA on IoT Edge documented).
- Execution model: per-event vs micro-batch vs hybrid (documented trade-off, chosen per query in Spark).
- Authoring surface: code-first vs SQL-first vs no-code editor.
- Domain libraries: ML inference, geospatial, anomaly detection, streaming agents (era-current).
- Deployment topology: cloud, on-prem/K8s/YARN, edge, hybrid; HA/multi-region posture.
- Guarantee posture per output (exactly-once only for selected sinks, per ASA docs).

### L3 — Vendor-specific Detail (research notes only; excluded from final document)

- Flink: JobManager/TaskManager memory configuration, ZooKeeper/K8s HA services, savepoint semantics, DataStream API V2, Materialized Table, adaptive batch, state TTL migration compatibility, Flink CDC as a separate project, Stateful Functions, flame-graph profiling.
- Spark: 100 ms micro-batch / 1 ms continuous latency figures (documented but precise), DStreams legacy lineage, write-ahead-log mechanics.
- Azure ASA: streaming-unit pricing model, Trill engine provenance, 99.9% SLA claim, availability-zone auto-distribution, no-code editor specifics, Azure ML function invocation.
- Kafka Streams: DSL-vs-Processor-API layering, interactive queries, application reset tool, streams rebalance protocol (structure observed in docs TOC; details not asserted — Apache docs unreachable).
- Confluent: Tableflow (topics-as-Iceberg tables), Streaming Agents, Real-Time Context Engine, Confluent Cloud for Apache Flink packaging.
- Materialize: arrangements, hydration, reaction-time concept, mz-catalog introspection.

## Vendor-specific Findings

- ASA's "Ingest → Analyze → Deliver" three-stage framing is a vendor pedagogical frame; the same stages exist implicitly in every sample but no other vendor uses that label.
- Spark's micro-batch default is unique among the sample; it makes "streaming = many small batches" the user-visible model. Others present continuous execution.
- Kafka Streams' library packaging is unique: the "platform" ships inside the user's own application rather than as an operated system.
- Materialize/ksqlDB materialized-view surfaces are the strongest straddle toward a "streaming database" reading (see Boundary Findings).

## Boundary Findings

**vs Event broker / Message Queue (§14 Message Queue Management, unprocessed).** A broker stores and transports ordered event streams; it does not compute over them. Direct vendor evidence for the split: Confluent's own catalog separates "Stream" (clusters/topics) from "Process" (Flink/Kafka Streams/ksqlDB). Removal test: remove the computation, keep transport → broker. Straddler: Kafka Streams — processing delivered as a library whose inputs/outputs live in the broker; still inside this Type (computation is the product; packaging is a variant).

**vs Change Data Capture Platform (§13, processed).** CDC's established contract: capture ordered change-event streams from databases and deliver them to consumers. CDC output is a first-class ESP *input* (Flink connectors list Debezium/Canal/Maxwell/Ogg formats; Materialize ingests Postgres/MySQL CDC). Removal test: remove the computation, keep capture+delivery → CDC; remove capture specificity, keep continuous computation → ESP. Consistent with the CDC/data-replication passes' delivery-contract reasoning.

**vs ETL/ELT Platform & Data Integration Platform (§13, processed).** The integration pass defined that Type as pipeline-centric movement (connections + persistent pipelines + managed execution). ESP's defining contract is continuous computation over unbounded streams (event-time, state, windows, guarantees), with results feeding systems — Flink's own docs frame "streaming ETL" as one use case, and Spark is literally built on a SQL engine, so surface overlap is real. Seam: movement of data between systems (bounded or scheduled) vs persistent computation as events arrive. Removal test: remove unbounded-continuity (bounded, scheduled runs) → ETL/ELT; keep unbounded continuity + computation semantics → ESP. The etl-elt-platform pass should hold this bounded/unbounded seam from its side.

**vs Stream Analytics Platform (§13 sibling leaf, unprocessed) — JOINT REVIEW RECOMMENDED.** The market does not consistently separate the labels: Azure's flagship stream *processing* service is literally named "Stream Analytics"; Flink's training doc teaches "streaming analytics" as a primary use of the processing engine. Proposed seam for that pass: ESP = the general-purpose computation substrate (developer-facing; arbitrary processing logic; results feed systems, applications, and pipelines; deployed as jobs/pipelines), Stream Analytics = streams-to-insight as the defining deliverable (operator/analyst-oriented; metrics/monitoring/alerting/dashboards over live streams as the product surface; frequently SQL-only). The straddle is wide (ASA straddles by name and nature; ksqlDB/managed-Flink products blur it further), so a center-of-gravity ruling at that pass is required rather than a hard structural wall drawn here.

**vs Streaming databases (no directory leaf; Materialize/RisingWave class, ksqlDB materialized views).** These organize around continuously-maintained *queryable datasets* (sources/views/indexes; freshness; SQL query serving), while ESP organizes around deployed *processing jobs/pipelines* whose results flow onward. Removal test: remove the job/pipeline delivery contract, serve maintained query results instead → streaming database. ksqlDB (push+pull queries, materialized views) straddles deliberately. No directory change proposed from this side; recorded for any future leaf decision.

**vs Log Management / Observability (§14).** Telemetry platforms ingest log/metric/traces for IT operations analysis; ESP is a general substrate over arbitrary event streams, and log analytics platforms are consumers of streams, not the processing substrate. Name-level proximity only.

**vs Industrial IoT Platform (§16).** IoT platforms center device/fleet/asset management and OT protocols; edge stream processing (ASA on IoT Edge documented) appears inside them as a capability. Overlap is a capability seam, not a Type merge.

## Historical / Market-Sample Check

Would older, regional, or differently positioned products still fit the L0?

- Complex Event Processing lineage (the term ASA still uses for its query language; Flink ships a CEP library as a first-party capability): pattern-detection engines over event streams fit the core — continuous event input, user-defined logic, derived events out — even where they lacked distributed state, checkpointing, or exactly-once guarantees. This confirms those belong outside L0.
- Academic ancestors of the field (continuous query engines over streams) fit the same three-invariant shape: streams + continuous queries + continuously produced results.
- Platform-native pipeline components (the consumer side of a message queue, database triggers, or in-app stream consumers) fail the L0: no declared continuous computation *managed as a platform artifact* with results delivered onward — they are code inside another system. Kafka Streams is the boundary case that still passes: the library's DSL/topology/state/guarantee machinery *is* the product being used, even though it executes in-process.
- No region- or era-specific element (cloud units, watermarks, SQL dialects, specific broker integrations) is load-bearing in the definition. Check passed.

## Uncertainties

1. The ESP ↔ Stream Analytics sibling seam is proposed but not ratified — requires the stream-analytics-platform pass (joint review recommended).
2. Kafka Streams details (guarantee configuration specifics, interactive queries mechanics, state store behavior) are not directly evidenced (Apache docs unreachable); only its packaging model and stateful/library character are asserted, sourced from Confluent's official documentation.
3. Precision of latency/guarantee figures is deliberately avoided in the final document; per-output guarantee caveats (exactly-once processing vs delivery) are stated generically because only ASA documents the split explicitly in the sample.
4. The CEP historical pole is reasoned at concept level; no legacy CEP vendor documentation was directly fetched. The claim kept is only that historical CEP products fit the three-part core without distributed state/guarantees — i.e., those are not definitional.
5. Market drift watch: AI-era packaging (streaming agents, model inference in SQL) is arriving inside this Type's products; treated as era-current optional capability, consistent with other §13 passes.

## Final Synthesis

The Type is the **continuous computation layer over event streams**: it sits downstream of event transport (brokers) and event capture (CDC), upstream of systems/applications/analytics that consume its continuously produced results. Its defining core is the jointly-held triad: unbounded event streams as substrate + user-defined computation running continuously per-event + continuous delivery of derived results. Everything else — clusters, SQL, no-code, watermarks, exactly-once, ML, dashboards — is standard mature capability, packaging, or era-current extension. Packaging (cluster engine / library / managed service / edge) and execution model (per-event / micro-batch) are variant axes. The sharpest unresolved boundary is with the sibling Stream Analytics Platform leaf (center-of-gravity question, joint review); the streaming-database shape is a recognized adjacent product category that this Type is defined against, not merged with.
