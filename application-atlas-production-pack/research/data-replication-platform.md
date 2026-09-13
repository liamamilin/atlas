# Research Notes — Data Replication Platform

Research date: 2026-09-07
Slug: `data-replication-platform`
Directory position: §13 Data, Analytics & AI Systems (between Change Data Capture Platform and Reverse ETL Platform)

---

## Research Goal

Understand what a Data Replication Platform actually is as an Application Type: its core objects, its delivery contract, its lifecycle, its operational rules, and — critically — its boundary against the neighboring Types Change Data Capture Platform, Data Integration Platform, ETL/ELT Platform, Data Virtualization Platform, Data Exchange Platform, and Backup/Disaster Recovery.

Three prior passes left binding cross-checks for this leaf:

- **change-data-capture-platform pass (processed)**: recorded a taxonomy-level finding — CDC and replication are two delivery contracts over the same machinery; flagship products (GoldenGate, Qlik Replicate, AWS DMS) implement CDC as the capture mechanism of replication while branding themselves as replication/migration products. Joint review recommended at this pass; candidate outcomes: (a) two Types split by delivery contract with a documented straddle zone, or (b) a consolidation view treating CDC as the capture-capability slice of replication platforms.
- **data-integration-platform pass (processed 2026-09-07)**: the §13 data-movement cluster (etl-elt-platform, data-integration-platform, data-replication-platform, change-data-capture-platform, reverse-etl-platform) is one product population under five leaves with documented label drift (Airbyte self-labels "data replication platform" while behaving as a pipeline platform). Integration was defined as the pipeline-centric Type. Cross-check recommended at this pass.
- **data-exchange-platform pass (processed 2026-09-07)**: boundary held on intra-org movement vs inter-org entitlement; cross-check recommended at this pass.

## Initial Boundary (hypothesis before research)

- Replication = keep a target copy of a data store synchronized with its source (state-oriented contract), as distinct from CDC (event-oriented) and ETL/ELT (batch transformation-oriented).
- Users: DBAs, data engineers, platform/migration teams.
- Nearest neighbors: CDC Platform (sharpest seam), ETL/ELT, Data Integration Platform, Data Virtualization (no-copy alternative), Data Exchange (inter-org), Backup/DR (point-in-time recovery vs running replica), DBMS-native replication features (embedded capability, not standalone product).
- Unknowns: whether "one-shot migration" use (headline use of AWS DMS) breaks the "ongoing sync" definitional requirement; whether scheduled-incremental managed-ELT sync (Airbyte/Fivetran pole) is replication or ELT; whether "replication" requires heterogeneity; how much transformation is allowed before the product becomes an integration platform.

## Research Questions

1. What are the core objects? (source/target endpoint, replication instance/engine, task, replica, checkpoint/position)
2. What is the delivery contract — state at the target, events to consumers, or both?
3. How does initial load → ongoing synchronization work, and what task modes exist?
4. What selection/mapping/transformation depth exists before the product becomes an integration platform?
5. How are schema changes, failures, drift handled?
6. What do users monitor (status, latency, throughput, validation)?
7. What topologies exist (unidirectional, one-to-many, bidirectional, peer-to-peer)?
8. Where is the boundary vs CDC / ETL-ELT / integration / virtualization / exchange / backup-DR / DBMS-native replication?
9. How do the labels behave — which products call themselves replication, and do their contracts match?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy / tier | Role in sample |
|---|---|---|
| Oracle GoldenGate | enterprise heritage (1990s), on-prem microservices + managed cloud (OCI), replication-first with CDC machinery | enterprise HA/continuity pole; homogeneous + heterogeneous; bidirectional/peer-to-peer |
| Qlik Replicate (ex-Attunity) | enterprise, GUI-driven replication specialist, wide endpoint matrix, client-managed server | GUI-administration replication pole |
| AWS DMS | fully managed hyperscaler service, migration-first with ongoing-replication mode | managed-service pole; migration vs replication straddle inside one product |
| Airbyte | OSS/SaaS modern platform self-labeled "data replication platform", scheduled ELT-shaped syncs | label-drift anchor; tests whether the replication label tracks a contract or a population |
| Fivetran | fully managed SaaS ELT (scheduled syncs, cursors; separate HVR replication engine) | boundary anchor vs ELT; not a core replication sample |

## Sources

All fetched 2026-09-07 (Tier 1 official documentation unless noted):

- Oracle GoldenGate 19c overview — https://docs.oracle.com/en/middleware/goldengate/core/19.1/coredoc/overview-oracle-goldengate.html (evidence layer A)
- Qlik Replicate online help home (May 2026) — https://help.qlik.com/en-US/replicate/Content/Replicate/Main/Home.htm (A)
- Qlik Replicate System Architecture (May 2026) — https://help.qlik.com/en-US/replicate/May2026/Content/Replicate/Main/Introduction/System_Architecture.htm (A)
- AWS DMS Introduction — https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.html (A)
- AWS DMS Components — https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.Components.md (A)
- Airbyte Data replication platform — https://docs.airbyte.com/platform/ (A)
- Airbyte Core Concepts — https://docs.airbyte.com/platform/using-airbyte/core-concepts (A)
- Fivetran Core Concepts — https://fivetran.com/docs/core-concepts (A — boundary anchor)
- Prior-pass evidence reused under citation: research/change-data-capture-platform.md (GoldenGate family landing/core index; Qlik Change Tables body; AWS DMS CDC/bidirectional pages; Debezium framing), research/data-integration-platform.md (Airbyte self-labels; Fivetran sync model; Informatica "replication/CDC as integration patterns")

### Source-access limitations

- Oracle GoldenGate concept-page bodies (Extract/Replicat/trails chapters) remain JavaScript-rendered and returned only headings on both passes. GoldenGate assertions here are limited to the 19c overview page and the product-family descriptions it carries. No GoldenGate internals are claimed.
- Qlik Change Tables / Control Tables / Log Stream bodies were fetched in the prior CDC pass; this pass confirms the same topics exist in the May 2026 TOC. Claims about them cite the prior pass.
- AWS DMS bidirectional replication and per-engine CDC prerequisites were fetched in the prior CDC pass; reused by citation, not re-fetched.
- No numeric limits, latency numbers, or SLA values are asserted anywhere in the final document.

---

## Product A — Oracle GoldenGate (evidence layer A)

Observations from the 19c overview page (this pass):

- Self-description: "an application that provides real-time data integration, data replication, transactional change data capture, data transformations, high availability solutions, and verification between operational and analytical enterprise systems."
- Semantics: "move committed transactions across multiple systems"; "Only committed transactions are moved, to leverage consistency and improved performance."
- **Homogeneous AND heterogeneous explicitly documented**: "It supports a wide range of databases and data sources, providing replication between same types or between different databases" — with examples: Oracle Autonomous DB → Oracle DB; two Oracle DB instances; two-way replication between MySQL and Oracle; also replicate to Java Messaging Queues, flat files, and Big Data (via the DAA family member).
- Stated functions in "a data replication environment": real-time data movement reducing latency; committed-transaction movement; REST-based microservices for different replication environments; high performance with minimal overhead; wide database integration; security at different levels and topologies.
- Use cases: **Business Continuity and High Availability** (multinational-bank scenario: continuously synchronize branch transactions to a centralized database at massive volume where "even the slightest delay can greatly impact the business", monitored continuously "preferably through some sort of GUI-based tool"); **Initial Load and Database Migration** ("performed only once... without taking your systems offline"); **Data Integration**.
- Topologies: "ranging from simple unidirectional topology to more complex peer-to-peer. Supported topologies depend on the underlying database requirements and its supported configurations."
- Product family (each a separate product): GoldenGate for Oracle / for Non-Oracle (Db2 i/z/LUW, MySQL, PostgreSQL, SQL Server, Sybase, TimesTen, Teradata); **OCI GoldenGate** ("fully managed, native cloud service... design, run, orchestrate, and monitor data replication tasks without having to allocate or manage any compute environments"); **GoldenGate Free** (recipe-driven UI, Docker, free); Marketplace off-box deployment; HP NonStop edition; **Veridata** ("compares one set of data to another and identifies data that is out-of-sync, and allows you to repair any out-of-sync data"); **DAA** (handlers for Big Data, NoSQL, Messaging, Data Warehouse, Data Lakehouse); EMCC monitoring plug-in.
- From prior pass (cited): Extract → Instantiate → Distribute → Replicat topic structure; initial load = one-time extract/load without taking systems offline; use cases include near zero-downtime migration.

## Product B — Qlik Replicate (evidence layer A)

Observations from the May 2026 help home + System Architecture (this pass):

- Self-description: "accelerate data replication, ingestion and streaming across a wide variety of heterogeneous databases, data warehouses, and Big Data platforms. After loading the selected tables to the target, Qlik Replicate's high-performance change data capture (CDC) technology remotely scans transaction logs and rapidly delivers real-time data updates."
- Audience framing: "an intuitive graphical interface minimizes the administrative burden by enabling **database administrators and enterprise architects** to quickly configure, control and monitor data replication without the need for manual coding."
- System architecture: **initial load** reads "a filtered stream of rows (with relevant columns only)" → transformation → write to target endpoint in expected output format. **CDC process** "obtains a stream of filtered events or changes in data or metadata from the transaction log file", then "buffers all changes for a given transaction into a single unit before forwarding them to the target when the transaction commits"; during initial load, CDC buffers changes until affected tables are loaded. → The default contract is apply-to-target state delivery, transaction-ordered.
- Designer/Console server: "a Web-based application that serves as the user interface for dealing with designing or modifying the replication system and displaying and controlling its operation."
- Documentation structure (the operating model): System Architecture; Console; step-by-step tutorial; security considerations + user permissions (RBAC); adding/defining/managing tasks; **defining and managing endpoints** (source endpoints; target endpoints; "basic one-to-one replication"); selecting tables and/or views for replication; migrating tasks (import/export); task settings; table settings; Global Transformation Rules wizard ("define global transformations to render the source data compatible with the target"); **monitoring full-load operations** and **monitoring change processing operations**; monitor tools; notifications; global error handling; logging; scheduling jobs; server settings; cluster environment; dump files; Log Stream ("optimize data transfer between a single source and multiple targets"); file channel; change tables; audit table; control tables; supported platforms/endpoints matrix; add-ons API (SDK); Avro consumers API (Kafka target).
- From prior pass (cited): Log Stream Staging semantics (capture once, stage, feed multiple targets); Change Tables ("save the change events in change tables" — a store-events target style instead of applying state); control tables as target-side bookkeeping.

## Product C — AWS DMS (evidence layer A)

Observations from Introduction + Components (this pass):

- Self-description: web service to "migrate data from a source data store to a target data store. These two data stores are called **endpoints**." Homogeneous or heterogeneous engines supported. Constraint: "The only requirement to use AWS DMS is that one of your endpoints must be on an AWS service. You can't use AWS DMS to migrate from an on-premises database to another on-premises database."
- Five components: **database discovery** (Fleet Advisor inventory), **schema conversion** (DMS Schema Conversion), **replication instance** ("a managed Amazon EC2 instance that hosts one or more replication tasks"; Multi-AZ standby for HA/failover; storage for logs and spilled changes; **DMS Serverless** provisioning option), **endpoints** (type source/target, engine, server, port, SSL, credentials; **connection test mandatory** before use; on success DMS "downloads and stores schema information" incl. table, primary-key, unique-key definitions; endpoint settings per engine; **one endpoint reusable by multiple tasks**), **replication task** ("move a set of data from the source endpoint to the target endpoint").
- Task settings: **migration type** — Full load / **Full load + CDC** ("performs a full data load while capturing changes on the source. After the full load is complete, captured changes are applied to the target. Eventually... a steady state") / **CDC only** ("replicate data changes only" — for when existing data was copied by other means; "bring and keep your source and target databases in sync"); **target table preparation** (do nothing / drop & recreate / truncate); LOB modes (exclude/full/limited); **table mappings** (which tables; selection rules); **data transformations** (rename schema/table/column; change tablespace names; **define target primary keys and unique indexes**); **data validation**; CloudWatch logging; parallel full-load tuning.
- CDC mechanics: "collects changes to the database logs by using the database engine's native API"; in-memory buffers; spill to Change Cache when apply is slower than capture; **CDCLatencySource / CDCLatencyTarget** graphs on the Task Monitoring tab.
- From prior pass (cited): CDC start points (timestamp, native SCN/LSN, persisted checkpoint); bidirectional replication with loopback-prevention table, DML-only, "isn't intended as a full multi-master solution"; "AWS DMS CDC does not provide real-time replication... no SLAs for CDC latency"; per-engine prerequisites (supplemental logging, row binlog, replication slots).

## Product D — Airbyte (evidence layer A — label-drift anchor)

Observations from /platform + core concepts (this pass):

- Self-label: docs root section literally "Data replication platform"; logo tagline "Simple, secure and extensible data integration". Both labels on one product.
- "Use Airbyte's data replication platform to consolidate data from hundreds of sources into your data warehouses, data lakes, and databases. Then, move data into the operational tools where work happens, like CRMs, marketing platforms, and support systems."
- Explicit self-framing: "Airbyte's data replication platform is an extract, load, and data activation solution. You might know this as ELT/reverse ETL."
- Use-case fit: replication ideal when "you need all your data in one place / join across datasets / more pipelines that can be slower / want storage / update content, but not trigger side effects"; **not** ideal when "you don't want storage / care a lot about freshness and latency / ... / need to trigger side effects". → Airbyte's own docs disclaim the low-latency posture that defines the replication-contract pole.
- "Taxonomy of data movement" table: **data replication = the ELT/ETL row** (in → storage); reverse ETL and operations rows are separate postures. Vendor itself maps "data replication" onto ELT.
- Core objects: Source (API/file/database/warehouse), Destination, Connector, **Connection** ("an automated data pipeline that replicates data from a source to a destination" — replication frequency hourly/daily/manual; stream & field selection; sync mode; sync schedule; destination namespace & stream prefix; schema propagation policy), Stream/Record/Field, Delivery Method (typed records vs raw file copy), Sync Mode, Resumability (checkpoint + auto re-attempt), Typing & Deduping, Custom Transformations (dbt, post-sync), Workspace/Organization.
- Deployment: self-managed OSS (Core), managed cloud tiers (Standard; Plus adds "15-minute sync schedules" and mappings; Pro adds RBAC/SSO; Enterprise Flex hybrid data planes). 600+ connectors, No-Code Connector Builder, UI/API/SDK/Terraform/PyAirbyte.

## Product E — Fivetran (boundary anchor; evidence layer A)

Observations from core concepts (this pass):

- "a Fivetran connector reaches out to your source, receives data from it, and writes it to your destination"; canonical-schema shared-responsibility ELT; "Our philosophy is to make a faithful **replication** of source data with as few transformations as necessary" — the replication *vocabulary* is used by the ELT pole too.
- Sync model: historical sync → incremental syncs with cursors; re-sync (invalidate cursors, re-fetch everything) as continuity repair; checkpoints; scheduled cadence; MAR usage pricing; HVR 6 documented as a separate section (the vendor's separate replication engine).
- From prior pass (cited): sync modes soft delete / live ("destination mirrors current source state") / history — a destination-state contract, not an event contract.

---

## Cross-product Comparison

| Aspect | GoldenGate | Qlik Replicate | AWS DMS | Airbyte | Fivetran (anchor) |
|---|---|---|---|---|---|
| Self-label | "data replication and change data capture" | "data replication, ingestion and streaming" | "migrate... data store to target data store" | "data replication platform" (= ELT/reverse ETL per its own table) | "faithful replication" vocabulary under ELT |
| Primary contract | synchronized copies between operational systems (+ event delivery via DAA handlers) | apply-to-target state delivery, transaction-ordered | synchronized target ("bring and keep your source and target databases in sync") | scheduled syncs into warehouse/lake (destination state) | scheduled syncs (destination state: soft delete/live/history) |
| Core objects | deployment/processes (Extract→Replicat structure), initial load | endpoints + tasks + table/view selection | endpoints + replication instance + replication task | connection (source+destination+sync config) | connector/connection + sync |
| Initial load | initial load (one-time, online) | full load (filtered rows) | full load / full load + CDC / CDC only | historical sync | historical sync |
| Ongoing alignment | committed transactions moved (log-based) | CDC from transaction logs, transaction-buffered, commit-ordered | engine-native log APIs; in-memory buffers + Change Cache | scheduled incremental syncs, resumable | scheduled incremental syncs with cursors |
| Replica position | trails/checkpoints (prior pass, topic structure) | task state | CDC start point + checkpoint | checkpoints/resumability | cursors/checkpoints |
| Selection/mapping | filter/distribute (overview level) | table/view selection; table settings; global transformation rules | table mappings; transformations (rename, target PKs) | stream/field selection; namespace/prefix | automatic canonical schema; limited user transforms |
| Transformation depth | "data transformations" listed as capability (depth unverified) | global rules "render the source data compatible with the target" | rename/schema/PK-level only (documented list) | minimal in-flight; dbt post-sync | minimal in-flight; post-load |
| Monitoring | family monitoring products; GUI emphasized in use case | full-load + change-processing monitors, notifications | Task Monitoring; CDCLatency graphs; CloudWatch | run history/dashboards | sync history |
| Repair/verification | Veridata (compare + repair out-of-sync) | dump files, error handling | data validation (task setting) | re-sync (full re-fetch) | re-sync |
| Topology | unidirectional → peer-to-peer; two-way MySQL↔Oracle | one-to-one; one-to-many via Log Stream | one-to-one; bidirectional w/ loopback prevention (prior pass) | one source → one destination per connection | one source → one destination |
| Interfaces | microservices/CLI; recipe GUI (Free); OCI console | web Console/Designer | AWS Console/CLI/API | UI + API/SDK/Terraform/PyAirbyte | dashboard + API |
| Deployment | on-prem microservices; OCI managed; Free | client-managed server (+ suite siblings) | fully managed AWS service | OSS + managed cloud | fully managed SaaS |

### Evidence-layer notes

- All five products: observations are Layer A (directly observed in official docs this pass or cited from prior passes).
- GoldenGate: Layer A but reduced depth (overview + family only; deep mechanics JS-gated on both passes).
- Cross-product commonalities (Layer B): source/target endpoint objects; persistent configured task/connection as the unit; initial load + ongoing-change modes; selection/mapping with only light transformations; monitoring incl. lag/latency; recovery from checkpoints; verification/repair machinery; administration consoles + programmatic control; endpoint reuse across tasks.
- Canonical inference (Layer C): the Type is best modeled as a **state-copy delivery contract** over a source of record — the target is a usable synchronized copy — with CDC (event contract), integration (pipeline contract), and ETL/ELT (transformation-technique slice) as sibling contracts over overlapping machinery.

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

A Data Replication Platform is recognizable as such iff it has:

1. **Connections to external data systems the platform does not own** — a source data system whose contents are read, and a target data system where the replica is maintained (databases, warehouses, file/object stores in the classic pole; SaaS/API sources additionally in the managed-ELT-adjacent pole). The platform is custodian of the copy, never the system of record. Remove → a DBMS-native replication feature or a storage product, not this platform.
2. **The replication task as a persistent configured unit** — a named, kept, editable pairing of source objects to a target shape: what is selected, how it maps, how it lands; re-runnable and revisited. Remove persistence → one-shot migration tooling / export-import scripts.
3. **The synchronized-copy contract** — the defining promise: the target holds the source's data state and is kept aligned with it as the source changes. Realized as an initial load of existing state plus ongoing application of subsequent changes (continuous log-based propagation in the mature pole; scheduled incremental sync in the managed-ELT-adjacent pole), applied so the target remains a usable replica. Remove the copy promise (deliver change events to consumers instead) → CDC Platform. Remove the ongoing alignment (one-shot movement only) → migration tooling. Remove the as-is state shape (derive transformed artifacts per business logic) → ETL/ELT / Data Integration Platform. Remove the target store entirely (logical query-time access) → Data Virtualization Platform.

Remove-tests against §24 (historical check): GoldenGate's 1990s log-based heritage satisfies all three; homogeneous same-engine replication satisfies all three (GoldenGate Oracle→Oracle example is direct evidence); scheduled-incremental state-sync satisfies all three (Airbyte/Fivetran). The definition does NOT depend on: log-based capture specifically, continuous low-latency delivery, heterogeneous engines, cloud, GUI, or warehouse targets. A tool that only performs full-state refreshes without change propagation fails #3 — per the ratified seam it belongs to the ETL/ELT / migration zone.

### L1 — Common Mature Structure (very common, not definitional)

- Full-load (initial load / historical sync) + ongoing-change modes as selectable task behavior, with a documented handoff between the two (Qlik CDC buffering during full load; DMS "eventually... a steady state").
- In the continuous pole, changes obtained through the source's own change mechanism — transaction/log APIs (DMS "database engine's native API"; Qlik "transaction log file"; GoldenGate committed transactions); in the scheduled pole, cursors/checkpoints per sync (Airbyte/Fivetran). Source-side prerequisites exist (supplemental logging, binlog format, replication slots — prior-pass evidence).
- Table/view/stream-level selection with include/exclude; column selection (Qlik "filtered stream of rows (with relevant columns only)"; Airbyte stream & field selection).
- Mapping into target shape: naming/namespace/prefix, schema/table/column renaming; key definitions on the target (DMS mappings); "global transformations to render the source data compatible with the target" (Qlik). Light, compatibility-oriented transformations only.
- Monitoring surfaces: task status, **lag/latency** (DMS CDCLatency graphs), throughput, per-operation phase (full load vs change processing monitored separately in Qlik).
- Failure handling: checkpoints/resumability (Airbyte; DMS spill/Change Cache), error handling policies, dump files (Qlik).
- Out-of-sync detection and repair: data validation (DMS task setting); source-vs-target comparison and repair (GoldenGate Veridata as a family product); full re-sync as the coarse repair (Airbyte/Fivetran).
- Endpoint/connection reuse across tasks (DMS documented; Qlik endpoint object).
- Administration: web console/Designer (Qlik), recipes GUI (GoldenGate Free), cloud consoles; plus programmatic control (AWS CLI/API; Airbyte API/Terraform/SDK).
- Team/security machinery: RBAC/user permissions (Qlik; Airbyte upper tiers), server settings, logging, notifications; cluster/HA options for the replication machinery itself (Qlik cluster environment; DMS Multi-AZ).

### L2 — Variant / Optional Structure

- Deployment form: client-managed engine (Qlik server; GoldenGate microservices) / fully managed service (AWS DMS; OCI GoldenGate) / OSS + managed cloud (Airbyte).
- Positioning pole: replication-first specialist (Qlik, GoldenGate) vs migration-first managed service with ongoing replication (DMS) vs managed-ELT under the replication label (Airbyte).
- Cadence/posture: continuous low-latency propagation (GoldenGate/Qlik/DMS CDC) vs scheduled incremental syncs (Airbyte/Fivetran) — the ELT straddle zone.
- Topology: unidirectional; one-to-many staging (Qlik Log Stream); bidirectional with loopback prevention (DMS; GoldenGate two-way MySQL↔Oracle); peer-to-peer (GoldenGate) — with documented limits in sampled products (DMS bidirectional is DML-only, no conflict resolution).
- Target style: apply-to-mirror (default) vs store-change-events (Qlik Change Tables) vs publish-to-stream (Kafka/Kinesis targets — the CDC straddle) vs flat files (GoldenGate).
- Homogeneous vs heterogeneous endpoint pairs; delivery-platform constraints (DMS requires one endpoint on AWS).
- Companion machinery: schema discovery/conversion (DMS Fleet Advisor, Schema Conversion), design recipes/studios (GoldenGate Free/Studio), comparison products (Veridata).
- Business model: license, managed service, usage-based (Airbyte plans; Fivetran MAR).

### L3 — Vendor-specific Structure (kept out of the final document)

- GoldenGate: Extract/Replicat/trail vocabulary, Distribute step, Veridata/Studio/Free/OCI/NonStop/EMCC editions, DAA handlers, "99.999%" marketing (prior pass).
- Qlik: Log Stream Staging, Change/Audit/Control tables, .dfm metadata files, add-on SDK, Avro consumers API, Enterprise Manager.
- AWS DMS: replication instance/Multi-AZ/Serverless, Fleet Advisor, Schema Conversion, LOB modes, `awsdms_txn_state` / `awsdms_loopback_prevention` tables, CDCLatency metric names, "no SLAs for CDC latency" note, one-endpoint-on-AWS constraint.
- Airbyte: plan ladder (Core/Standard/Plus/Pro/Enterprise Flex), 15-minute sync schedule tier, PyAirbyte, connector builder, taxonomy-of-movement table, agents/context product line.
- Fivetran: MAR pricing, canonical-schema shared-responsibility model, type-inference hierarchy, HVR.

## Rejected Findings

- **"Replication = log-based CDC"** — rejected. Airbyte/Fivetran replicate with scheduled cursors; the historical trigger/change-table pattern exists (prior-pass Debezium framing); log-based is the dominant continuous-pole implementation, not the definition.
- **"Replication = one-shot migration"** — rejected. DMS's full-load-only is one task mode; the product's own language for the platform's capability is "bring and keep your source and target databases in sync" — a standing capability. A one-shot-only tool fails L0-3.
- **"Replication requires heterogeneous engines"** — rejected. GoldenGate explicitly documents same-engine replication; DMS documents homogeneous migrations.
- **"Replication = ELT into warehouses"** — rejected. The HA/business-continuity pole (GoldenGate bank scenario) replicates operational state between operational systems with no warehouse involved.
- **"Low latency / real-time is definitional"** — rejected. DMS explicitly disclaims real-time CDC and latency SLAs (prior pass); freshness posture varies (Airbyte disclaims it outright). Monitoring lag is common; guaranteeing freshness is not definitional.
- **"Modern connector-catalog breadth is definitional"** — rejected. Classic replication products are organized around endpoint matrices per engine, not hundreds of SaaS connectors.
- **"The platform owns the replica's storage"** — rejected. All sampled products write into target systems the customer owns; the platform holds at most bookkeeping/control tables and staging.
- Marketing figures (Airbyte 600+ connectors etc.) recorded as catalog-breadth evidence only, not asserted as facts about the Type.

## Boundary Findings

1. **vs Change Data Capture Platform (processed) — JOINT REVIEW DISCHARGED.** Determination: **two Types split by delivery contract, straddle zone documented** (outcome (a) from the CDC pass's candidates). Same machinery, same products, different promise:
   - Replication: keep a target *copy* synchronized (state contract — apply changes so the target mirrors the source; topologies, bidirectional sync, comparison/repair).
   - CDC: deliver *change events* to consumers (event contract — the ordered stream is the product).
   - Evidence: GoldenGate self-describes both ("data replication and change data capture") and splits its family (core replication vs DAA messaging handlers; Veridata for replication-side repair). Qlik's default is apply-to-target but ships Change Tables (store events) and Kafka/Avro consumers. DMS targets databases/warehouses but also streams. The straddle zone (event-stream targets inside replication products; apply-style sinks in CDC products) is real and documented from both sides. Consolidation (outcome (b)) is rejected: the two leaves carry genuinely different user promises, monitoring objects (replica state vs event lag), and failure models.
2. **vs Data Integration Platform (processed) — CROSS-CHECK DISCHARGED.** Boundary held per the ratified split: integration's center is the managed pipeline (flow contract); replication's center is the synchronized copy (state contract). Label drift confirmed from this side (Airbyte self-labels both "data replication platform" and "data integration"; Fivetran uses "faithful replication" vocabulary under ELT) — one product population under multiple leaves, as the integration pass recorded. The consolidation-vs-slice decision for **etl-elt-platform** remains that leaf's own pass; this pass records the replication side: cadence (scheduled vs continuous) is a variant axis, not a contract boundary.
3. **vs Data Exchange Platform (processed) — CROSS-CHECK DISCHARGED.** Boundary held: exchange = inter-org entitlement/delivery of dataset offerings (publish → discover → consume across organizations); replication = intra-org infrastructure movement between data systems the same operator controls (GoldenGate's branch-to-HQ bank scenario; DMS's one-endpoint constraint keeps both endpoints in one customer's estate). No entitlement/publication surface exists in any sampled replication product.
4. **vs ETL/ELT Platform (unprocessed).** The scheduled-incremental state-sync zone (Airbyte/Fivetran pole) is the straddle: managed-ELT platforms mirror source state on schedules and use replication vocabulary, while replication platforms promise the same destination state with a continuous/low-latency posture. Recorded as a joint-review flag for the etl-elt-platform pass, alongside the integration pass's earlier flag.
5. **vs Backup / Disaster Recovery Platform (§14).** Replication maintains a *running, usable* synchronized copy; backup/DR manages *restore points and recovery orchestration*. Replication is used as a DR mechanism (GoldenGate's business-continuity use case is direct evidence), but the replication platform's managed object is the data-copy relationship, not the recovery plan. Conceptual boundary (Layer C); no DR-product docs fetched this pass.
6. **vs Data Virtualization Platform (unprocessed).** Virtualization = query-time logical access, no physical copy; replication = materialized physical copy kept in sync. Consistent with the fabric pass's ratified split.
7. **vs DBMS-native replication / Database Management Consoles.** Database engines ship native replication features, and consoles operate a single database. The Data Replication Platform population is standalone products connecting systems the platform does not own — including same-engine pairs (GoldenGate evidence). Same-engine replication between two separate systems is in-type; replication confined inside one engine instance is an engine capability, not this Type. (Layer C; no DBMS-replication docs fetched — no product-specific claims made.)
8. **vs Managed File Transfer.** Files can be a target medium (Qlik file channel; GoldenGate flat files) but the managed object is the replica relationship, not the transfer event. Consistent with the integration pass's note.
9. **vs Data Warehouse / Lakehouse Platforms.** Destinations that own storage + compute; the replication platform owns neither. Clear in all sampled products.

## Historical / Market-Sample Check (per §24)

- Older products: GoldenGate's 1990s log-based heritage fits the three-structure definition; trigger-based and change-table replication (the classic older pattern, prior-pass evidence) fits — capture via the source's change mechanism, state applied to a target, persistent configuration.
- Platform-embedded replication (DBMS features) satisfies the conceptual core but is not the standalone product population — recorded as boundary #7; the definition is not written so as to exclude it conceptually (same-engine pairs in-type).
- Therefore the canonical definition must NOT say: log-based, real-time, cloud, GUI, heterogeneous, warehouse-target, or connector-catalog. None of these survive the historical check.

## Uncertainties

- GoldenGate deep mechanics (trail files, Extract types, Replicat modes) unverified on both passes — JS-gated docs. No precise GoldenGate internals claimed anywhere.
- Whether scheduled-incremental state-sync (Airbyte/Fivetran pole) ultimately belongs to replication or ETL/ELT is a market blur, not resolved here; treated as a documented straddle zone with the decision deferred to the etl-elt-platform pass.
- DMS bidirectional replication and per-engine prerequisites are cited from the prior CDC pass (not re-fetched); treated as Layer A evidence of one product.
- Qlik Change Tables / Log Stream bodies cite the prior pass; this pass confirms topic existence in the current TOC only.
- No numeric limits, latency values, or SLA figures are asserted in either document (per evidence rules).
- GoldenGate "data transformations" capability depth unverified; kept generic.

## Final Synthesis

A Data Replication Platform is a system that maintains a synchronized copy of a data system's contents in another data system, both external to and owned by the platform's operator. Its defining core is three structures: connections to source and target data systems it does not own; a persistent, configured replication task pairing selected source objects with a target shape; and the synchronized-copy contract — an initial load of existing state plus ongoing application of source changes so the target remains a usable replica. Around that core, mature products add: selectable task modes (full load, full load + change application, changes only), selection/mapping with light compatibility transformations, lag- and status-oriented monitoring, checkpoint-based recovery, out-of-sync validation and repair, endpoint reuse, administration consoles plus programmatic control, RBAC and HA for the machinery itself. The market straddles: flagship products implement CDC as their capture mechanism (CDC = the event-delivery sibling contract), managed-ELT platforms use the replication label for scheduled syncs, and migration tools overlap the full-load mode — but the Type's center holds: the promise is a synchronized target copy, not an event stream, not a transformation pipeline, not an entitlement offering.
