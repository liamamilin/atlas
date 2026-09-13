# Research Notes — Stream Analytics Platform

Research date: 2026-09-09

## Research Goal

Understand what a Stream Analytics Platform actually is as an Application Type: its core objects, the work its users do, how an analysis lives and dies, which time/state semantics define its behavior, and — because the neighboring leaf Event Stream Processing Platform (§13, processed 2026-09-08) left a delegated JOINT REVIEW flag for this pass — where its boundary sits against ESP, BI/dashboards, monitoring, streaming databases, and the data-movement siblings. This pass must ratify or refute the ESP pass's proposed keep-both seam.

## Initial Boundary

Hypothesis before research:

- Core use: continuously analyze live event streams — compute metrics, aggregates, patterns, anomaly detections — and keep analytical results permanently current for consumption (dashboards, alerts, real-time analytics).
- Users: data engineers/developers author the continuous analysis; analysts, operators, and product/business people consume the living results.
- Nearest neighbors: Event Stream Processing Platform (the closest sibling — vocabulary and population overlap), Business Intelligence / Dashboard Platform (consumes stored results), Metrics Monitoring / Observability (§14, IT telemetry), streaming databases (no directory leaf), ETL/ELT (movement contract), Message Queue Management (transport).
- Known unknowns: whether the ESP pass's proposed seam (computation substrate vs streams-to-insight deliverable, "frequently SQL-only", "analyst-facing") survives fresh evidence from this side; where the insight surface lives (in-product vs fed to external BI); whether the Kinesis Data Analytics brand history matters.

## Research Questions

1. What does the market itself call this Type, and what products carry the "stream analytics" label?
2. What is the unit of user work (job/query/notebook) and what does it bind (sources, logic, results)?
3. How is the analysis expressed — SQL, code, notebooks, no-code — and which is primary?
4. What time semantics govern results (windows, event time, late data)?
5. Where do results go and who consumes them — in-product dashboards/alerts, push to BI, served streams?
6. What lifecycle and capacity model does the always-on analysis have?
7. What separates this Type from ESP, BI/dashboards, monitoring, and streaming databases?

## Representative Products

| Product | Pole | Why sampled |
|---|---|---|
| Azure Stream Analytics | fully managed cloud PaaS, SQL-first, portal/no-code surface; the product literally named "Stream Analytics" | the namesake anchor; different customer tier; rich official docs |
| Amazon Managed Service for Apache Flink (successor brand of Kinesis Data Analytics) | managed Flink runtime, code-first + SQL + notebooks | AWS's stream-analytics flagship; documents the label→engine drift directly |
| Timeplus | startup streaming-analytics-native platform, single binary, edge-to-cloud, in-product dashboards + alerting | the insight-deliverable pole with first-class in-product surfaces |
| Confluent ksqlDB | streaming SQL database over Kafka, push/pull queries, materialized views | the SQL-over-broker analytics pole and streaming-database straddler |

Coverage: managed cloud vs self-managed/OSS; SQL-first vs code-first; in-product insight surfaces vs feed-outward; enterprise cloud vs startup tiers. The ESP pass's sample (Flink, Spark Structured Streaming, Kafka Streams, ASA, Materialize) provides the cross-side comparison base.

## Sources

All fetched 2026-09-09. Evidence layers: A = direct observation on the specific product's official docs; B = cross-product commonality; C = canonical inference.

1. Azure Stream Analytics — "Introduction to Azure Stream Analytics" — https://learn.microsoft.com/en-us/azure/stream-analytics/stream-analytics-introduction (A)
2. Amazon Managed Service for Apache Flink — "What is Amazon Managed Service for Apache Flink?" — https://docs.aws.amazon.com/managed-flink/latest/java/what-is.html (A)
3. Amazon Managed Service for Apache Flink — product overview page (served at the former https://aws.amazon.com/kinesis/data-analytics/ URL, now titled/branded Managed Service for Apache Flink) — https://aws.amazon.com/kinesis/data-analytics/ (A)
4. Timeplus — "Introduction" (docs home) — https://docs.timeplus.com/ (A)
5. Timeplus — "Why Timeplus" (capabilities: transformation, routing, analytics and alerting, deployment) — https://docs.timeplus.com/why-timeplus (A)
6. Confluent ksqlDB — "ksqlDB for Confluent Platform" overview — https://docs.confluent.io/platform/current/ksqldb/overview.html (A) + concepts/how-to/tutorial TOC — https://docs.confluent.io/platform/current/ksqldb/index.html (A)
7. Cross-side base (fetched by the ESP pass, 2026-09-08): Apache Flink docs, Spark Structured Streaming guide, Kafka Streams via Confluent docs, Materialize concepts — see research/event-stream-processing-platform.md §Sources (B, secondary)

Source-access limitations:

- Google's "what is stream analytics" explainer (cloud.google.com/learn/what-is-stream-analytics) timed out on both attempts — abandoned per the network rule; no Google vocabulary evidence in this pass.
- aws.amazon.com/streaming-analytics/ (category page) returned 404; AWS evidence taken from the product page and docs instead.
- Kinesis Data Analytics for SQL (the legacy SQL runtime): its retirement/replacement timeline was NOT directly fetched or verified — no precise claims about it anywhere. What IS directly observed: the /kinesis/data-analytics/ product URL now serves "Amazon Managed Service for Apache Flink" content, i.e., the stream-analytics-branded service is today documented as a managed Flink stream-processing service.

## Product Observations

### Azure Stream Analytics (A)

- Self-definition (2026-02-updated doc): "a fully managed stream processing engine that analyzes and processes large volumes of streaming data with submillisecond latencies" (latency claim = vendor, not propagated). Pipeline framing: **Ingest → Analyze → Deliver**.
- Job model: a **job** connects **inputs** (Event Hubs, IoT Hub, blob historical data, static/slow-changing **reference data** joined for lookups) → **SQL query** → **outputs** (Blob/SQL DB/Data Lake/Cosmos DB; Event Hubs; **Power BI for real-time visualization**; Azure Functions).
- Scenario framing (the product's own examples): anomaly detection in sensor data (spikes/dips/slow trends), geo-spatial analytics for fleets, remote monitoring and predictive maintenance, **clickstream analytics**, real-time telemetry/log analysis; patterns used to "trigger actions and initiate workflows such as raising alerts, feeding information to a reporting tool, or storing transformed data".
- Query language: SQL "augmented with temporal constraints"; CEP functions, pattern matching, anomaly detection, geospatial; JS/C# UDFs/UDAs; Azure ML function invocation. Testing: sample data extracted from the live stream. Authoring: portal, no-code drag-and-drop editor, VS Code/VS/CLI/PowerShell/Bicep/ARM/Terraform with CI/CD.
- Runtime: cloud or IoT Edge/Azure Stack with the same query language (hybrid). Scale: streaming units, scale up/down, partitioned parallelism. Reliability: exactly-once event processing + at-least-once delivery (exactly-once delivery only for selected outputs); built-in checkpoints; repeatable results; availability-zone auto-distribution. Built on Trill (vendor-stated).

### Amazon Managed Service for Apache Flink (A)

- Self-definition: "use Java, Scala, Python, or SQL to process and analyze streaming data… author and run code against streaming sources and static sources to **perform time-series analytics, feed real-time dashboards, and metrics**."
- Two modes: **applications** (Flink DataStream/Table APIs authored in an IDE; workloads named "Streaming ETL or Continuous Applications") and **Studio notebooks** ("interactively query data streams in real time", SQL/Python/Scala, "create private real-time dashboards", promotable to long-running applications).
- Managed machinery: provisioning, AZ failover, parallel computation, automatic scaling, application backups as checkpoints and snapshots.
- Product page use cases: "Deliver streaming data in seconds" (to S3/OpenSearch), "Create real-time analytics — …continuously produce insights for time-sensitive use cases", "Perform stateful processing — …anomaly detection based on historical data trends".
- Naming observation: the product page formerly branded "Kinesis Data Analytics" now presents as Amazon Managed Service for Apache Flink ("run stream processing applications") — the vendor's own stream-analytics flagship is marketed today with stream-processing vocabulary.

### Timeplus (A)

- Self-labels: "a simple, powerful, and cost-efficient vectorized **stream processing platform**" (Introduction); "unified real-time data processing platform built for developers" (Why Timeplus); "fast, powerful, and efficient **SQL stream processing platform**" (single-binary section). Editions: **Proton** (OSS streaming SQL engine) and **Timeplus Enterprise**.
- Docs structure itself is the canonical pipeline: **Connect Data In → Transform Data → Store & Serve Data → Send Data Out** + SQL Reference.
- Connect: Kafka, Confluent Cloud, Redpanda, NATS, WebSocket/SSE, CSV uploads; SDKs (Java/Go/Python), JDBC/ODBC, REST; EXTERNAL STREAM/TABLE native integration (Kafka, ClickHouse, another Timeplus).
- Transform: streaming SQL console; Streams (append, mutable with UPSERT/DELETE), Views, incremental **Materialized Views**; MULTI-JOIN / ASOF JOIN; aggregations, downsampling; JS/Python UDFs/UDAFs. Ad-hoc historical queries on the same data; "Business Intelligence and analytical queries can be executed directly in Timeplus" (vendor claim).
- **Insight surfaces in-product**: "push-based, low-latency dashboards to visualize real-time insights" (SSE-powered); Grafana plugins for observability dashboards; **Timeplus Alert** — "SQL-based rules can be used to trigger or resolve alerts in systems such as PagerDuty, Slack, and other downstream platforms". Routing by SQL criteria with a data lineage view; single result can feed "analytics, alerting, compliance" sinks.
- Deployment: single binary, no JVM/ZooKeeper; edge to cloud; MPP / storage-compute separation / hybrid; K8s HPA / AWS Auto Scaling.

### Confluent ksqlDB (A)

- Self-definition: "Confluent's purpose-built **streaming SQL database** that enables developers to build **real-time, event-driven applications** on Apache Kafka using familiar SQL syntax"; "the industry-leading solution for **stream processing with SQL**".
- Named use cases: "real-time analytics, event-driven microservices, or continuous data transformations". Audience language: "developers and data engineers".
- Concepts: Streams, Tables, **Materialized Views**, Queries (**push and pull**), Time and Windows, Connectors, Functions/UDFs, Lambda functions. Tutorials: Materialized View, Streaming ETL Pipeline, Event-Driven Microservice, **Clickstream Data Analysis Pipeline**.
- Surfaces: CLI, REST API (query/streaming endpoints), Java client, Control Center integration; operations docs: processing guarantees, high availability (incl. HA pull queries), monitoring, capacity planning, schema inference via Schema Registry.
- Distributions: packaged in Confluent Platform (self-managed, incl. RBAC) or hosted in Confluent Cloud.

## Cross-product Comparison

| Dimension | Azure Stream Analytics | AWS Managed Service for Apache Flink | Timeplus | ksqlDB |
|---|---|---|---|---|
| Self-label | "fully managed stream processing engine" (name: Stream Analytics) | managed Flink service for "stream processing applications" (name carries Kinesis Data Analytics lineage) | "stream processing platform" / "SQL stream processing platform" | "streaming SQL database" / "stream processing with SQL" |
| Analyzed subject | event streams from hubs/IoT/blob + reference data | streaming sources + static sources | Kafka/Redpanda/NATS/WebSocket/CSV + historical store | Kafka topics (streams/tables) |
| Unit of work | job (input → SQL query → outputs) | application (Flink APIs) or Studio notebook | stream + continuous SQL query/view/materialized view | persistent query (CREATE STREAM/TABLE AS SELECT), push/pull queries |
| Logic expression | SQL + temporal constraints; no-code editor; UDFs; Azure ML | Java/Scala/Python (DataStream/Table), SQL, notebooks | streaming SQL console; JS/Python UDFs | SQL only (UDFs) |
| Time semantics | temporal constraints in SQL | Flink event-time windows (per Flink docs) | windows in streaming SQL | "Time and Windows in ksqlDB Queries" concept |
| Results destination | Power BI real-time visualization, storage, Event Hubs, Functions; alerting workflows | "feed real-time dashboards and metrics", S3/OpenSearch, downstream services | in-product dashboards, Timeplus Alert → PagerDuty/Slack, sinks (ClickHouse/Iceberg/S3/Splunk/ES/MongoDB) | materialized views + push queries to consumers; output topics |
| Insight surface in-product | no (BI/feed-outward; portal monitoring only) | partial (Studio notebooks: "private real-time dashboards") | yes, first-class (dashboards + alerting) | no (serves via push/pull queries) |
| Lifecycle/capacity | streaming units; scale up/down; checkpoints | managed scaling; checkpoints/snapshots | single binary → clusters; K8s/ASG scaling; checkpoints | self-managed or hosted clusters |
| Failure semantics | exactly-once processing, at-least-once delivery | Flink checkpoint/snapshot machinery | checkpoints (query state) | processing-guarantees docs (exact content not asserted) |

### Shared structure (B — cross-product commonality across the fresh sample, consistent with the ESP pass's sample)

1. Live, unbounded event streams as the analyzed subject, consumed as they arrive.
2. A persistent, user-defined analytical computation (metrics, aggregations, joins, patterns, anomaly logic) declared once and running continuously.
3. Results kept permanently current — the deliverable is a living analytical result, not a one-off report: dashboards, metrics, alerts, or continuously-served analytics.
4. The insight deliverable is named by every product as the purpose of the computation (ASA scenarios + Power BI; AWS "time-series analytics, feed real-time dashboards, and metrics"; Timeplus dashboards + alerting; ksqlDB "real-time analytics" first-listed).
5. SQL is the dominant authoring mode across the population (ASA SQL, Timeplus SQL, ksqlDB SQL, AWS SQL/notebooks) but not universal (AWS code-first applications; ASA UDFs extend SQL).
6. Windowing over time as the normal shape of stream aggregation; event-time concepts present throughout.
7. Joining streams against static/reference/historical data is standard (ASA reference data; AWS "static sources"; Timeplus historical store/ASOF; ksqlDB tables).
8. Testing the analysis before/while it runs (ASA sample-data testing; AWS Studio interactive notebooks; Timeplus console).
9. An always-on lifecycle: create → test → deploy/run continuously → monitor → scale → update/stop, with engine-managed state and checkpoints.
10. Elastic capacity models (streaming units / managed scaling / clusters / hosted cloud).

### Differences (implementation, not Type)

- Where the insight surface lives: in-product dashboards+alerting (Timeplus) vs feeding external BI/visualization (ASA→Power BI; AWS→"real-time dashboards") vs serving query results to consumers (ksqlDB push/pull). A posture, not a boundary.
- Authoring style: SQL console / no-code editor / notebook / IDE code.
- Packaging: managed PaaS / managed Flink runtime / self-managed or OSS single binary / hosted cloud offering.
- Whether historical data shares the same engine (Timeplus unified stream+historical; ASA ingests historical blobs; others lean pure-stream).

## Abstraction Hierarchy

### L0 — Defining Invariant (jointly held, deliberately small)

A Stream Analytics Platform is exactly a system in which:

1. **Live event streams are the analyzed subject** — continuous, unbounded, timestamped event records from external producers (clicks, sensor readings, transactions, telemetry), consumed as they arrive (all four products' input side). Remove → analytics over stored/bounded data (BI/warehouse territory).
2. **Continuous analytical computation over those streams** — user-defined metric/aggregation/pattern/anomaly logic declared once and running persistently, so the analytical result stays continuously current as events arrive (ASA SQL job; AWS applications/notebooks; Timeplus continuous SQL/materialized views; ksqlDB persistent queries). Remove → a dashboard or query run on demand over stored data.
3. **The deliverable is a continuously-current analytical result for human/decision consumption** — live metrics and dashboards, triggered alerts, or continuously-served real-time analytics, whether surfaced in-product or pushed to BI/alerting destinations (ASA: Power BI, alerting workflows; AWS: "feed real-time dashboards and metrics"; Timeplus: dashboards + Timeplus Alert; ksqlDB: real-time analytics via materialized views/push queries). Remove → a general stream computation whose results flow onward into systems and pipelines as data — the sibling Event Stream Processing Type.

Jointly-held is load-bearing: 1 alone = event hub/log; 2 without 1 = batch analytics on bounded data; 3 without 1+2 = a BI/alerting layer over stored data; 1+2 without 3 = ESP territory; 1+3 without 2 = a monitoring/alert surface over raw events with no platform computation.

The seam to ESP is a **center-of-gravity ruling, not a hard wall**: both leaves share the continuous-computation spine (unbounded streams + persistent computation + continuously produced results), and straddling products are expected. What makes a product fall on this side is that the analytics result consumed by people is the center of what it ships, not an incidental output.

Not in L0 (checked against the historical/market-sample rule):

- **SQL authoring** — dominant but not universal (AWS code-first; ASA UDFs). Common mature structure.
- **In-product dashboards/alerting** — a posture (Timeplus first-class; ASA feeds Power BI). Common-to-variant.
- **Event-time/watermark machinery as a user-visible concept** — common mature structure; older CEP-era analytics ran on coarser time semantics.
- **Exactly-once guarantees, connector catalogs, no-code editors, notebooks, anomaly/geospatial/ML function libraries** — standard capabilities or optional extensions.
- **Cloud units, managed PaaS, single-binary OSS, edge runtimes** — packaging variants.

### L1 — Common Mature Structure (standard capabilities, not definitional)

- SQL authoring surface over streams (windowed aggregation, joins, pattern functions), commonly extended with UDFs; code APIs and notebooks beside it in parts of the population.
- Windows over event time; stateful aggregation with engine-managed state.
- Reference-data/static-source enrichment (lookups, ASOF-style joins).
- Fault tolerance: checkpoints/state snapshots, repeatable results; stated processing/delivery guarantees.
- Always-on job lifecycle with test-before-run (sample data or interactive notebooks), monitoring, scaling (units or clusters), and in-place update.
- Connector catalogs for sources and destinations; result routing to multiple destinations from one computation.
- Insight delivery: push-based dashboards and/or alerting rules and/or served result streams (push queries, BI feeds).
- Observability of the computation itself (lag, throughput, checkpoint health).

### L2 — Variant / Optional Structure

- Insight-surface posture: in-product dashboards + alerting vs feed-outward to BI/alert destinations vs query-served results.
- Packaging: fully managed cloud service / managed engine runtime / self-hosted cluster / OSS single binary / edge runtime (ASA on IoT Edge documented).
- Authoring surface mix: SQL console, no-code editor, notebooks, IDE code.
- Stream+historical unification (one engine serving both ad-hoc historical and streaming queries) vs pure-stream.
- Audience tilt: developer/data-engineer primary with analyst-adjacent accessibility (notebooks, no-code) — the population's own docs address "developers and data engineers".
- Domain function libraries: anomaly detection, geospatial, ML invocation (ASA, AWS); era-current AI-era packaging (noted in ESP pass too).

### L3 — Vendor-specific Detail (research notes only; excluded from final document)

- Azure ASA: Ingest→Analyze→Deliver pedagogy; streaming-unit pricing; Trill engine provenance; 99.9% availability claim; no-code editor specifics; Azure ML function invocation; availability-zone auto-distribution; IoT Edge/Azure Stack runtimes; VS/CLI/Bicep/ARM/Terraform authoring matrix.
- AWS: Managed Service for Apache Flink naming (Kinesis Data Analytics lineage observed via URL/brand drift); Studio notebook promotion path; the Flink-API decision-tree guidance; AZ failover; "gigabytes per second" marketing claims (not propagated).
- Timeplus: Proton OSS engine; NativeLog WAL + Historical Store; append vs mutable streams; MULTI-JOIN/ASOF JOIN; EXTERNAL STREAM/TABLE; Timeplus Alert; Grafana plugin; SSE push dashboards; data-lineage view; MPP/storage-compute-separated/hybrid deployment models; "eliminates the need for a separate data warehouse" claim.
- ksqlDB: push vs pull query split; Control Center integration; schema inference via Schema Registry; migrations tool; RBAC packaging; processing-log.

## Vendor-specific Findings

- ASA is the only sampled product that carries "Stream Analytics" in its product *name*; its own docs today define it as a "stream processing engine". The label/population mismatch is real and vendor-level.
- AWS's brand drift (Kinesis Data Analytics → Managed Service for Apache Flink) is direct vendor evidence that "analytics" and "processing" labels are interchangeable at the marketing layer.
- Timeplus is the only sample with dashboards AND alerting as first-class in-product surfaces; it defines the insight-delivery pole.
- ksqlDB is the strongest straddler toward the streaming-database reading (materialized views + pull queries + "streaming SQL database" self-label) — consistent with the ESP pass's finding; no directory leaf exists for that category.

## Boundary Findings

**vs Event Stream Processing Platform (§13 sibling — JOINT REVIEW DISCHARGED from this side).** The ESP pass proposed keep-both with the seam: ESP = general-purpose computation substrate (developer-facing, arbitrary logic, results feed systems/pipelines); Stream Analytics = streams-to-insight deliverable (analyst-facing, frequently SQL-only). Fresh evidence from this side **ratifies keep-both** with two refinements: (a) the load-bearing seam property is the **deliverable orientation** — insight consumed by people (dashboards/metrics/alerts/served analytics) vs data flowing onward into systems/applications — not the authoring audience: every product in this sample addresses developers/data engineers, so "analyst-facing" is dropped; (b) "frequently SQL-only" is dropped — SQL-first is the dominant authoring mode of this population (B, 4/4 with SQL surfaces) but not exclusive (AWS code-first; ASA UDFs), and it does not separate the Types. Vocabulary convergence is total: all four sampled "stream analytics" products self-label with stream-processing language, and the flagship AWS stream-analytics brand became a managed stream-processing service. The two leaves therefore describe one product family read through two centers of gravity; both final documents reference the shared spine and the deliverable seam. Straddlers named in both passes: Azure Stream Analytics (namesake; analytics-leaning center), ksqlDB (streaming-database-leaning), managed-Flink products (both), Timeplus (spans; insight-pole features first-class).

**vs Business Intelligence Platform / Dashboard Platform (§13).** BI consumes stored/served data and centers the visualization/exploration surface; this Type computes over live unbounded streams and centers the continuous computation (windows, event time, state) that keeps results current. The hand-off is a documented pattern (ASA → Power BI); Timeplus's claim that BI queries run directly in-product is the recognized straddle, not a merge.

**vs Metrics Monitoring / Observability (§14).** Monitoring platforms ingest IT telemetry (hosts, services, traces) for operations; this Type computes over arbitrary business/IoT/application event streams with user-defined analytical logic. Operational monitoring of the computation itself (lag, checkpoints) is standard machinery, not the boundary.

**vs Streaming databases (no directory leaf; Materialize/RisingWave/ksqlDB class).** Consistent with the ESP pass: continuously-maintained queryable datasets vs deployed continuous computation with delivered results. ksqlDB deliberately straddles (push/pull queries, materialized views). No directory change proposed from this side either.

**vs ETL/ELT Platform & Data Integration Platform (§13, processed).** Bounded/scheduled movement vs continuous computation. This sample supports the seam: movement appears only as input/output plumbing (ASA historical-blob ingestion; Timeplus "streaming ETL" tutorials; AWS "deliver streaming data in seconds"), never as the center.

**vs Message Queue Management (§14, unprocessed).** Transport vs computation — unchanged from the ESP pass; every sampled product reads from brokers as a source.

**vs Industrial IoT Platform (§16).** ASA's IoT Edge runtime and IoT scenarios sit at the capability seam; device/fleet/asset management remains IoT-platform territory.

## Historical / Market-Sample Check

Would older, regional, or differently positioned products still fit the L0?

- Complex-event-processing lineage products (the generation ASA's query language still references): pattern-detection engines over live event feeds producing operator-facing alerts/dashboards — continuous events + declared logic + living insight, without SQL, clouds, or modern surfaces. Fit the core.
- Continuous-query academic lineage (CQ engines over data streams): fits the same three-invariant shape.
- Real-time analytics engines of the 2010s (Lambda-architecture speed layers feeding real-time dashboards) fit the spine with different packaging.
- A plain dashboard over a database, a scheduled report, or an app that computes its own metrics in-process fail the L0 (no live unbounded subject + no platform-held continuous computation + no living deliverable) — correctly outside.
- No era-, region-, or vendor-specific machinery (cloud units, SQL dialects, SSE dashboards, notebooks) is load-bearing. Check passed.

## Uncertainties

1. The ratified seam is a center-of-gravity ruling by design; individual products legitimately straddle (ASA, managed Flink, ksqlDB, Timeplus). Future passes touching these products should keep both references rather than forcing exclusive placement.
2. Kinesis Data Analytics for SQL runtime status/timeline not verified (not fetched) — no claims made.
3. Google vocabulary page unreachable (2 timeouts) — the "stream analytics" label evidence rests on the Azure product name, AWS use-case language, and general market usage, not on Google's own definition.
4. ksqlDB's processing-guarantee *content* (exact semantics) not asserted from this pass's fetches; docs TOC confirms the machinery exists.
5. Timeplus's "BI queries directly in-product" is a vendor claim, recorded as such.

## Final Synthesis

A Stream Analytics Platform is the insight-deliverable face of the continuous stream-computation family: it takes live, unbounded event streams as the analyzed subject, runs a persistent user-defined analytical computation over them (metrics, windowed aggregations, joins, patterns, anomaly logic — SQL-first as the common authoring mode), and keeps a continuously-current analytical result in front of the people who act on it — live dashboards, triggered alerts, or served real-time analytics — whether those surfaces live inside the product or are fed outward to BI and alerting destinations. The defining core is the jointly-held triad (live streams as subject + continuous analytical computation + living insight deliverable); everything else — SQL vs code authoring, in-product vs outward insight surfaces, managed vs self-hosted packaging, edge runtimes, anomaly/ML function libraries — is standard capability, posture, or variant. The joint review with Event Stream Processing Platform is discharged: keep-both ratified on the deliverable seam (insight for people vs computation feeding systems), with the shared spine and the straddle zone acknowledged in both directions.
