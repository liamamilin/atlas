# Research Notes — Change Data Capture Platform

Research date: 2026-09-07
Slug: `change-data-capture-platform`
Directory position: §13 Data, Analytics & AI Systems (between Data Integration Platform and Data Replication Platform)

---

## Research Goal

Understand what a Change Data Capture (CDC) Platform actually is as an Application Type: its core objects, its delivery contract, its lifecycle, its operational rules, and — critically — its boundary against the neighboring Types Data Replication Platform, ETL/ELT Platform, Event Stream Processing Platform, and Reverse ETL Platform. The directory places CDC adjacent to Data Replication, and market flagship products self-describe as "replication" products, so the boundary work is the central risk of this leaf.

## Initial Boundary (hypothesis before research)

- CDC = continuously capture row-level changes from a source system of record (typically a database transaction log) and deliver them as ordered change events to downstream consumers.
- Nearest neighbors: Data Replication Platform (synchronized copy), ETL/ELT Platform (batch/full-state movement), Event Stream Processing Platform (computation over streams), Reverse ETL (opposite direction), Message Queue Management (the broker itself).
- Suspected taxonomy issue: the flagship products of this market (GoldenGate, Qlik Replicate, AWS DMS) brand themselves as replication/migration products that use CDC as the mechanism. Both directory leaves may describe two contracts over the same machinery.

## Research Questions

1. What are the core objects? (source/target connector or endpoint, task/pipeline, change event, snapshot, capture position)
2. What capture mechanisms exist, and how do the products themselves characterize the tradeoffs (log-based vs trigger vs query/polling)?
3. What is the delivery contract? (operation types, ordering, delivery guarantees, event format)
4. How does the initial load → streaming handoff work?
5. How is schema change (DDL) handled?
6. What do users configure? (table/column selection, filtering, mapping, transformations)
7. What operational surfaces exist? (console, monitoring, metrics, alerts, recovery)
8. What source-side prerequisites and rules matter? (log retention, supplemental logging, primary keys, privileges)
9. Where exactly is the boundary vs replication / ETL-ELT / stream processing / reverse ETL?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy / tier | Role in sample |
|---|---|---|
| Debezium | open-source, Kafka-ecosystem, developer-facing connector framework | pure-CDC pole; log-based capture as explicit doctrine |
| Oracle GoldenGate | enterprise heritage (1990s), on-prem microservices + managed cloud (OCI), heterogeneous | enterprise replication+CDC pole |
| Qlik Replicate (ex-Attunity) | enterprise, GUI-driven, wide endpoint matrix, client-managed server | GUI-administration pole |
| AWS DMS | fully managed cloud service, migration-first with CDC mode | managed-service pole; rich CDC mechanics docs |
| Fivetran | fully managed SaaS ELT (scheduled syncs, cursors; HVR for replication) | boundary anchor vs ETL/ELT — NOT treated as a core CDC sample |

## Sources

All fetched 2026-09-07 (Tier 1 official documentation unless noted):

- Debezium — Architecture: https://debezium.io/documentation/reference/stable/architecture.html ; Features: https://debezium.io/documentation/reference/stable/features.html
- AWS DMS — Introduction: https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.html ; Components: https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.Components.md ; Ongoing replication/CDC: https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html
- Oracle GoldenGate — family landing: https://docs.oracle.com/en/middleware/goldengate/index.html ; core index: https://docs.oracle.com/en/database/goldengate/core/index.html ; 19c overview ("What is Oracle GoldenGate"): https://docs.oracle.com/en/middleware/goldengate/core/19.1/coredoc/overview-oracle-goldengate.html
- Qlik Replicate — online help home: https://help.qlik.com/en-US/replicate/Content/Replicate/Main/Home.htm ; System Architecture: https://help.qlik.com/en-US/replicate/May2026/Content/Replicate/Main/Introduction/System_Architecture.htm ; Using Change Tables: https://help.qlik.com/en-US/replicate/May2026/Content/Replicate/Main/Change%20Tables/use_change_tables.htm
- Fivetran — Documentation root: https://fivetran.com/docs ; Core Concepts: https://fivetran.com/docs/core-concepts ; Sync Overview: https://fivetran.com/docs/core-concepts/syncoverview ; Sync Modes: https://fivetran.com/docs/core-concepts/syncoverview/sync-modes

Source-access limitations:

- Oracle GoldenGate 19c/21c/26ai concept-page bodies (Extract/Replicat/trails chapters) are JavaScript-rendered and returned only headings. The 12c classic-docs URL attempted returned 404. GoldenGate mechanics below are therefore asserted from the family landing, the core index topic structure (Install → Deploy → Configure → Extract → Instantiate → Distribute → Replicat), and the 19c overview page only. No precise GoldenGate internals are claimed.
- Fivetran database-connector capture internals (log-based vs other methods) were not fetched; Fivetran is used only as an ELT-boundary anchor with claims limited to its documented sync model.
- One GoldenGate URL attempt failed (404) and was abandoned per the retry-limit rule; Qlik/GoldenGate deep pages otherwise fetched successfully.

---

## Product A — Debezium (evidence layer A)

Key observations (from Architecture + Features pages, Debezium 3.6 docs):

- Self-description: "a set of source connectors for Apache Kafka Connect. Each connector ingests changes from a different database by using that database's features for change data capture (CDC)."
- Explicit doctrine on capture mechanisms: log-based CDC "unlike other approaches, such as polling or dual writes" — advantages listed: all data changes captured; very low delay (millisecond range for MySQL/PostgreSQL) without polling CPU cost; no data-model changes (no "Last Updated" column); captures deletes; captures old record state and metadata (transaction ID, causing query) depending on database capabilities.
  - → Important: the product itself frames log-based vs polling/dual-writes as alternative *implementations* of CDC. This is direct evidence that "log-based" is not definitional for the Type.
- Deployment forms: (1) Kafka Connect runtime — source connectors write change events to Kafka topics (default: one topic per table, name = table name; topic routing transformation can rename/merge); sink connectors then stream records to Elasticsearch, warehouses, caches. (2) Debezium Server — ready-to-use app streaming to Kinesis, Google Cloud Pub/Sub, Apache Pulsar etc. (3) Debezium Engine — embedded library in custom Java apps. Also Debezium Operator (Kubernetes) and a "Debezium Management Platform" (UI) exist in the docs TOC.
- Snapshots: "optionally, an initial snapshot of a database's current state can be taken if a connector is started and not all logs still exist"; multiple snapshot modes including incremental snapshots triggerable at runtime.
- Filters: include/exclude lists over schemas, tables, columns. Masking of sensitive column values.
- Transformations (SMTs): topic routing, new-record-state extraction (event flattening — propagates the `after` structure to sinks), message filtering, schema-change-event filtering, content-based routing, outbox event router, etc.
- Schema change events exist as a first-class concept (schema change event filtering SMT; schema history topic implied by configuration docs).
- Monitoring via JMX; exactly-once delivery documented as a configuration topic; signalling (ad-hoc operational signals to connectors) and notifications documented.
- Connector matrix: MySQL, MariaDB, MongoDB, PostgreSQL, Oracle, SQL Server, Db2, Cassandra, Vitess, Spanner, Informix, CockroachDB, etc. Sink connectors: JDBC, MongoDB.

## Product B — Oracle GoldenGate (evidence layer A, reduced depth — see limitations)

Key observations (family landing + core index + 19c overview):

- Self-description: "the foundational product for data replication and change data capture"; "real-time data integration, data replication, transactional change data capture, data transformations, high availability solutions, and verification between operational and analytical enterprise systems."
- Core semantics: "move committed transactions across multiple systems"; "Only committed transactions are moved, to leverage consistency and improved performance."
- Process model (from doc topic structure): Install → Deploy → Configure (databases) → **Extract** → **Instantiate** → **Distribute** → **Replicat**. Extract = capture side; Instantiate = initial-load side; Distribute = routing between deployments; Replicat = apply side. (Topic titles are direct evidence of the pipeline shape; bodies unreachable.)
- Topologies: "ranging from simple unidirectional topology to more complex peer-to-peer", depending on database support.
- Initial load: "Initial load is a process of extracting data records from a source database and loading those records onto a target database... performed only once... without taking your systems offline."
- Use cases named by the vendor: business continuity / high availability, initial load & database migration (near zero-downtime), real-time data integration (warehouses/lakehouses), application data streams (publish/subscribe APIs for change data), stream processing (separate Stream Analytics product).
- Product family structure (evidence of Type boundary inside one vendor): core GoldenGate (databases) + GoldenGate for Distributed Applications and Analytics (DAA: lakehouses — Snowflake/Databricks/Fabric/Redshift; messaging — Kafka/Confluent/Kinesis/JMS; NoSQL — MongoDB/Cassandra; application APIs) + Stream Analytics (separate product) + Veridata (source-vs-target comparison/repair — separate product) + Studio (recipe-driven design GUI) + OCI GoldenGate (fully managed cloud service) + GoldenGate Free (free license, recipe UI, Docker) + Monitor/Director (legacy monitoring consoles, end-of-life) + EMCC plug-in.
- Supported heterogeneity: Oracle, PostgreSQL, MySQL, SQL Server, Db2 (LUW/i/z/OS), Sybase, Teradata, TimesTen, Yugabyte, etc.

## Product C — Qlik Replicate (evidence layer A)

Key observations (help home + System Architecture + Change Tables + TOC):

- Self-description: "accelerate data replication, ingestion and streaming across a wide variety of heterogeneous databases, data warehouses, and Big Data platforms. After loading the selected tables to the target, Qlik Replicate's high-performance change data capture (CDC) technology remotely scans transaction logs and rapidly delivers real-time data updates." GUI emphasis: "intuitive graphical interface minimizes the administrative burden... without the need for manual coding."
- System architecture: initial load reads "a filtered stream of rows (with relevant columns only)" → transformation → target. CDC process "obtains a stream of filtered events or changes in data or metadata from the transaction log file", then "buffers all changes for a given transaction into a single unit before forwarding them to the target when the transaction commits." During initial load, CDC buffers changes until affected tables are loaded.
- Object model: source endpoints, target endpoints, tasks (design in web Console/Designer), table/view selection, task settings, table settings, global transformation rules wizard.
- Operational machinery: monitoring of full-load and change-processing (CDC) operations, monitor tools, notifications, global error handling, logging, scheduling, server settings, user permissions (RBAC), cluster environment support, dump files for error/crash handling.
- Distinctive structures: **Log Stream Staging** (capture once from a source, stage the log stream, feed multiple targets); **Change Tables** ("use Qlik Replicate tasks to save the change events in change tables" — target style that stores events instead of applying state); **Audit table**; **Control tables** (task bookkeeping on targets); metadata (.dfm) files; add-on SDK; Avro consumers API (Kafka target).
- Positioning inside a data-integration suite: sibling products Compose, Enterprise Manager, Talend; Replicate is the CDC/replication engine member.

## Product D — AWS DMS (evidence layer A)

Key observations (Introduction + Components + CDC pages):

- Self-description: web service to "migrate data from a source data store to a target data store" — endpoints. Homogeneous or heterogeneous. Requires one endpoint on AWS.
- Component model: **replication instance** (managed EC2 hosting one or more tasks; Multi-AZ HA option; storage for logs and spilled changes; Serverless option), **endpoints** (source/target; type, engine, server, port, SSL, credentials; connection test mandatory; schema info downloaded at test time), **replication tasks** (source endpoint + target endpoint + settings).
- Task migration types: **Full load** / **Full load + CDC** ("performs a full data load while capturing changes on the source. After the full load is complete, captured changes are applied to the target... Eventually... a steady state") / **CDC only** ("replicate data changes only" — used when existing data was copied by other means).
- Target table preparation modes: do nothing / drop & recreate / truncate. LOB modes (exclude / full / limited). Table mappings (JSON) with selection rules and transformations (rename schema/table/column, define target PKs/indexes). Data validation. CloudWatch logging.
- CDC mechanics: "collects changes to the database logs by using the database engine's native API." Per-engine: Oracle LogMiner or binary reader (SCN-based, online/archive redo logs); SQL Server MS-Replication/MS-CDC + fn_dblog()/fn_dump_dblog() (LSN-based); MySQL row-based binlogs; PostgreSQL logical replication slots + test_decoding plugin.
- Source prerequisites documented: Oracle supplemental logging; MySQL row-level binary logging; RDS log retention (docs recommend ensuring backups and retaining change logs — "24 hours is usually enough" appears as vendor guidance, kept out of final doc).
- CDC start points: custom UTC timestamp (converted to engine-native point), **CDC native start point** (SCN/LSN/binlog position; per-engine support list), **checkpoint** (recovery checkpoint cached by the task; optionally persisted to a target metadata table `awsdms_txn_state`; retrievable via API/console). Start point fixed at task creation. Stop points (commit/server time) also supported.
- Latency model: in-memory buffers; spill to "Change Cache" on disk when target applies slower than capture; **CDCLatencySource / CDCLatencyTarget** metrics on the Task Monitoring tab. Explicit vendor note: "AWS DMS CDC does not provide real-time replication... There are no SLAs for CDC latency."
- Bidirectional replication: two tasks A→B and B→A with **loopback prevention** (a `awsdms_loopback_prevention` table marks applied transactions; echo transactions ignored). Explicit limits: DML only (no DDL loopback), no conflict detection/resolution, "isn't intended as a full multi-master solution."
- Scope notes: views migrate via full-load only (CDC covers tables); DMS Fleet Advisor (discovery) and DMS Schema Conversion (schema/code conversion) are adjacent components of the same service.

## Product E — Fivetran (boundary anchor; evidence layer A)

Key observations (docs root + Core Concepts + Sync Overview + Sync Modes):

- Self-description: managed connectors that "reach out to your source, receives data from it, and writes it to your destination" — ELT framing (extract/load raw, transform post-load). Shared-responsibility model; canonical schema philosophy.
- Sync model: **historical sync** (initial full extraction) → **incremental sync** mode ("only data that has been modified or added... extracted, processed, and loaded on schedule"), using **cursors** to record sync history; **re-sync** (invalidate cursors, re-fetch everything) as the integrity-repair mechanism; **rollback sync** for some API connectors (re-pull a trailing window daily).
- Scheduling: fixed interval (default 6h; options 1 min–24h), cron, manual. This is a *scheduled batch* cadence, not continuous streaming.
- Sync modes (how changes are represented in the destination): **soft delete** (mark deleted rows), **live** (destination mirrors current source state), **history** (every row version kept). The contract is destination *state/history*, not an ordered event stream.
- Checkpoints: "a checkpoint marks the point in the sync operation up to which data have been retrieved, and written"; failed syncs restart from last checkpoint.
- HVR 6 documentation exists as a separate section (Fivetran's acquired replication engine) — evidence that the vendor itself separates managed-ELT sync from replication/CDC machinery.
- Pricing: usage-based (Monthly Active Rows) — an ELT-business-model marker, not a CDC marker.

---

## Cross-product Comparison

| Aspect | Debezium | GoldenGate | Qlik Replicate | AWS DMS | Fivetran (boundary anchor) |
|---|---|---|---|---|---|
| Capture mechanism | log-based via DB native CDC (binlog, logical replication, …); docs contrast with polling/dual writes | log-based (Extract reads source logs; topic structure) | "remotely scans transaction logs" | engine-native log APIs (LogMiner, binlog, LSN fns, replication slots) | scheduled incremental syncs with cursors (capture method per connector; HVR for replication) |
| Unit of delivery | change event record → Kafka topic | committed transaction (Extract → trail → Replicat) | change event; per-transaction buffering, forwarded at commit | change records within a task stream | row changes per scheduled sync |
| Initial load | optional snapshot; multiple modes incl. runtime-triggered incremental | initial load (one-time, online) | full load + CDC buffering during load | full load / full load + CDC / CDC only | historical sync |
| Capture position | Kafka Connect offsets; state storage config | trail/checkpoint files (topic structure) | task state | CDC start point (SCN/LSN/timestamp) + recovery checkpoint (+ target metadata table) | cursors/checkpoints |
| Destinations | Kafka topics; Server → Kinesis/PubSub/Pulsar; sinks (JDBC, MongoDB, ES…) | databases, lakehouses, messaging, NoSQL, files (core + DAA) | databases, warehouses, Big Data, streaming targets | databases, S3, Kinesis, Redshift, etc. | warehouse/lake destination schemas |
| Ordering | per-topic/partition (Kafka semantics) | transaction order (committed only) | transaction-buffered, commit-ordered | per-task stream from log order | per-sync; state contract, no event ordering contract |
| Schema/DDL | schema change events; schema history topic; filtering SMT | DDL support (configure step; not verified in detail) | change events include "changes in data or metadata" | table mappings; per-engine DDL behavior varies | automatic schema evolution, type promotion |
| Transformations | SMTs: routing, filtering, flattening, masking, outbox | transformations between extract and apply | global transformation rules, table settings | table-mapping transformations (rename, PK definition) | minimal in-flight (row filter, type mapping); post-load transforms |
| Interfaces | config files + Kafka Connect REST; JMX; optional Platform UI; Operator | Admin CLI/microservices REST; Studio GUI; OCI console | web Console (design + monitor) | AWS Console, CLI/API, CloudWatch | web dashboard, REST API |
| Monitoring | JMX metrics; notifications | Monitor/EMCC plug-in (legacy); metrics | console monitoring (full load + CDC), notifications | Task Monitoring; CDCLatencySource/Target | Sync History chart (extract/process/load volumes) |
| Delivery guarantee | exactly-once documented as configurable | committed-transaction semantics | commit-boundary delivery | checkpoint recovery; data validation option | checkpoint restart; re-sync repair |
| Deployment | OSS on Kafka Connect / Server / Operator / Platform | on-prem microservices; OCI managed; Free edition | client-managed server (+ suite siblings) | fully managed AWS service | fully managed SaaS |
| Distinctive extras | outbox pattern, signalling, embedded engine | Veridata comparison; Stream Analytics; peer-to-peer topologies | Log Stream staging; Change/Audit/Control tables; add-on SDK | Fleet Advisor; Schema Conversion; bidirectional + loopback prevention; Serverless | MAR pricing; rollback sync; Connector SDK; HVR section |

### Evidence-layer notes

- All five products: observations are Layer A (directly observed in official docs).
- GoldenGate: Layer A but reduced depth (landing + overview + topic structure only). Claims kept generic.
- Cross-product commonalities (Layer B): source/target endpoint objects; task/pipeline as the unit of configuration; initial-load + CDC task types; capture position/checkpoint; table/column selection & filtering; lightweight transformations; monitoring with latency metrics; heterogeneous connector libraries; committed-transaction orientation.
- Canonical inference (Layer C): the Type is best modeled as an event-delivery contract over a source of record, with replication/ELT as sibling contracts over overlapping machinery.

---

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

A Change Data Capture Platform is recognizable as such iff it has:

1. **A source system of record whose changes are captured through that system's own change mechanism** — in modern products the transaction/log stream; historically and alternatively trigger-written change tables or change-tracking queries. (Evidence: Debezium explicitly names polling/dual-writes as alternative CDC approaches; DMS documents per-engine log APIs; Qlik "scans transaction logs"; GoldenGate Extract; trigger-based CDC is the classic older pattern.)
2. **The change event as the unit of delivery** — a row-level change carrying operation semantics (insert / update / delete, with before/after or after state) and identity (which table/record).
3. **Continuous, ordered delivery of those events to downstream destination(s)** — order follows the source's commit/transaction order; the destination may be another database, a warehouse, an event bus, a search index, or event-store tables.
4. **A resumable capture position** — a recorded point in the source's change stream (offset, SCN/LSN, checkpoint, cursor) from which capture continues after interruption, so the stream is continuous rather than a one-off extract.

Remove #1–2 → it is not capturing changes at all (generic integration). Remove #3 → it is a change *detector*, not a delivery platform. Remove #4 → it cannot be a continuous platform, only a repeated one-off job. Remove "ordered" → the contract degrades into state sync (replication) or batch sync (ELT).

### L1 — Common Mature Structure (very common, not definitional)

- Initial snapshot / backfill of existing data with handoff to streaming (full load + CDC; historical sync; initial load; snapshot modes incl. incremental).
- Table/column selection with include/exclude filters; column masking for sensitive data.
- Per-table mapping/routing to destinations (topic naming, schema/table mapping, rename transformations).
- Lightweight in-flight transformations (filtering, routing, flattening, renaming, masking) — not general-purpose compute.
- Schema-change (DDL) handling: schema change events, schema history, per-product evolution policies.
- Monitoring: task status, source/target latency metrics, logs, notifications/alerts.
- Error handling and recovery: restart from checkpoint, error tables/dump files, data validation/comparison.
- Heterogeneous connector libraries (many sources, many targets) as the commercial core of "platform" products.
- Administration surfaces: GUI console and/or CLI/API; RBAC in enterprise products.
- Delivery-guarantee postures: at-least-once as the working default; exactly-once/idempotent apply as a documented option (Debezium EOS; checkpoint+validation patterns elsewhere).

### L2 — Variant / Optional Structure

- Deployment form: OSS framework (Debezium) / client-managed server (Qlik, GoldenGate microservices) / fully managed cloud service (AWS DMS, OCI GoldenGate) / managed SaaS ELT with embedded capture (Fivetran).
- Target style: apply-to-mirror (state sync), store-events (change tables / audit tables — Qlik), publish-to-bus (Kafka/Kinesis/PubSub), land-in-warehouse (analytics).
- Capture-once-serve-many staging (Qlik Log Stream Staging; GoldenGate Distributor/trails topology).
- Bidirectional replication with loopback prevention; peer-to-peer topologies (DMS, GoldenGate) — explicitly *not* full multi-master conflict resolution in the sampled products.
- Data comparison / validation tooling as companion products (GoldenGate Veridata; DMS data validation).
- Adjacent suite components: schema conversion (DMS Schema Conversion), discovery/inventory (DMS Fleet Advisor), stream analytics (GoldenGate Stream Analytics), design studios/recipes (GoldenGate Studio, Qlik Designer).
- AI-era extensions (GoldenGate "AI Ready Data" feeds; Debezium AI transformations) — era-current marketing-adjacent, optional.
- Business models: OSS + support, license, managed instance, usage-based (MAR).

### L3 — Vendor-specific (kept out of the final document)

- Debezium: SMT catalog names, Debezium Server/Operator/Management Platform, signalling API, Reselect Columns post-processor, JMX metric names.
- GoldenGate: Extract/Replicat/trail/Distributor vocabulary, Veridata/Studio/Free/OCI editions, EMCC plug-in, HP NonStop edition, "99.999% uptime" marketing claim.
- Qlik: Log Stream Staging, Change/Audit/Control tables, .dfm metadata files, add-on SDK, Avro consumers API, Enterprise Manager.
- AWS DMS: replication instance/Multi-AZ/Serverless, Fleet Advisor, Schema Conversion, `awsdms_txn_state` / `awsdms_loopback_prevention` tables, CDCLatencySource/Target metric names, LOB modes, `StartFromContext`, open-transaction window setting, "no SLAs for CDC latency" note.
- Fivetran: MAR pricing, sync-frequency ladder, rollback sync, Connector SDK, canonical-schema philosophy, HVR.

---

## Vendor-specific Findings

See L3 above. Additionally:

- Only AWS DMS documents an explicit "no SLAs for CDC latency" statement — do not generalize latency claims to the Type.
- Only Debezium documents exactly-once as an explicit configuration topic — do not generalize exactly-once to the Type; at-least-once + idempotent/validated apply is the safer cross-product statement.
- Only Qlik documents change-tables/audit-tables as a first-class target style — treat "store events in tables" as a common variant, not a defining structure (it is, however, the historical trigger-CDC shape, which supports keeping it at L2).
- GoldenGate's "only committed transactions are moved" is a vendor-stated semantic; Qlik's commit-boundary buffering is consistent; Debezium emits per-transaction metadata but Kafka delivery semantics differ. Cross-product statement kept at "respects source commit/transaction order" level.

## Boundary Findings

1. **vs Data Replication Platform (sharpest seam; taxonomy-relevant).** The machinery overlaps almost completely: the same products (GoldenGate, Qlik Replicate, AWS DMS) self-describe as replication/migration products and implement CDC as the capture mechanism. The distinguishing contract:
   - Replication: keep a target *copy* in sync with the source (state-oriented; apply changes so the target mirrors the source; topologies, failover, bidirectional sync, comparison/repair).
   - CDC: deliver *change events* to consumers (event-oriented; the target may be a warehouse, bus, search index, or event store; the event stream itself is the product).
   - Test: "去掉什么就变成另一个 Type" — remove the event-delivery contract and keep only state-sync → Data Replication Platform; remove continuous capture and keep only full-state batch movement → ETL/ELT Platform.
   - Taxonomy note: both directory leaves exist ("Change Data Capture Platform", "Data Replication Platform"). Research supports keeping both as distinct *contracts*, but flags that most flagship products serve both contracts and market themselves under the replication label. Sibling leaf unprocessed — recommend joint review when Data Replication Platform is produced.
2. **vs ETL/ELT Platform.** Fivetran evidence: scheduled cadence (fixed interval/cron), cursor-based incremental syncs, destination-state contract (soft delete / live / history modes), re-sync as repair, MAR pricing. CDC appears inside ELT as a capture mechanism for database sources, but the delivery contract (state per sync, not ordered continuous events) and operational posture (scheduled, managed, schema-canonical) differ. Debezium/DMS-style CDC is continuous and event-contract-shaped.
3. **vs Event Stream Processing Platform.** CDC moves changes; stream processing computes over event streams (windows, joins, aggregates). Vendor-internal evidence: GoldenGate ships Stream Analytics as a *separate* product consuming GoldenGate feeds; Debezium's role ends at the Kafka topic boundary. CDC output commonly *feeds* stream platforms.
4. **vs Reverse ETL Platform.** Direction: CDC sources are operational systems of record feeding analytics/other consumers; Reverse ETL moves warehouse data back to operational tools. Different source class, different contract.
5. **vs Message Queue Management.** CDC platforms produce into / consume from brokers (Debezium requires Kafka Connect; GoldenGate DAA targets Kafka/Kinesis) but the managed object is the change stream, not the queue infrastructure.
6. **vs Database Management Console / Database IDE.** Those operate the database (sessions, schema, queries); CDC observes and streams its changes. CDC does require database-level configuration (supplemental logging, binlog, replication slots) — a source-prerequisite overlap, but the object of work differs.

## Historical / Market-Sample Check (per §24)

- Older/regional products: trigger-based CDC (e.g., classic SQL Server trigger-to-change-table patterns) and timestamp/query-based CDC fit the L0 definition — capture via the source's change mechanism, typed change events stored/delivered, implicit or explicit position. GoldenGate's 1990s log-based heritage also fits.
- Therefore the canonical definition must NOT say "log-based" (that is the dominant modern implementation, per Debezium's own framing of alternatives) and must NOT require a GUI, cloud delivery, or schema-evolution automation.
- Modern managed-ELT products (Fivetran) embed change capture but under a different contract — kept out of the core, documented as the adjacent-Type overlap.

## Uncertainties

- GoldenGate deep mechanics (trail files, Extract types, Replicat modes) unverified — docs JS-gated. No precise claims made anywhere for GoldenGate.
- Exact delivery-guarantee semantics per product (beyond Debezium's documented exactly-once option) not deeply verified; final doc stays at "at-least-once default, stronger guarantees product-dependent".
- Fivetran database-connector capture internals not fetched; Fivetran claims limited to its documented sync model.
- Whether "platform" in the leaf name requires a GUI/management layer: Debezium (a connector framework with optional UI) is treated as a valid member; the final doc treats management surfaces as common, not definitional.
- No numeric limits, defaults, or time windows asserted in the final document (per evidence rules).

## Final Synthesis

A Change Data Capture Platform is a system that continuously captures row-level changes from a source system of record through that system's own change mechanism (transaction log in modern implementations; triggers or change-tracking queries in older ones), turns each change into an operation-typed change event, and delivers those events in source commit order to one or more downstream destinations, maintaining a resumable capture position so the stream survives interruptions. Around this defining core, mature products add: initial snapshot/backfill with handoff to streaming; table/column selection and filtering; mapping/routing and lightweight transformations; schema-change handling; latency-oriented monitoring and alerting; checkpoint-based recovery; heterogeneous connector libraries; and admin consoles/APIs. The market's flagship products straddle CDC and data replication because both are contracts over the same machinery; the distinguishing test is whether the product's promise is an event stream delivered to consumers (CDC) or a synchronized target copy (replication). Managed ELT platforms embed change capture under a scheduled, state-oriented contract and are therefore adjacent, not core.
