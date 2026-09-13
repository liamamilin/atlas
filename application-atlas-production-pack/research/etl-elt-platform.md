# Research Notes — ETL / ELT Platform

## Research Goal

Define the Application Type behind the directory leaf **ETL / ELT Platform** (§13 Data, Analytics & AI Systems), and **close the §13 data-movement family joint review** left open by four prior passes (data-integration-platform, data-replication-platform, reverse-etl-platform, event-stream-processing-platform + stream-analytics-platform corroboration).

This leaf is the last unprocessed member of the five-leaf movement cluster (etl-elt-platform, data-integration-platform, data-replication-platform, change-data-capture-platform, reverse-etl-platform). The data-integration-platform pass recorded two candidate outcomes for this pass: (a) technique/contract slice with a documented overlap zone (CDC-style), or (b) consolidation view treating ETL/ELT as technique-variant/alias. This pass must rule.

## Initial Boundary (pre-research hypothesis)

- ETL/ELT Platform is probably the transformation-centric member of the data-movement family: the pipeline whose defining promise includes a **designed transformation step**, not merely movement.
- ETL (transform before load) vs ELT (load raw, transform post-load) is probably a **placement variant**, not two Types.
- Nearest neighbors: data-integration-platform (movement contract, transformation optional), data-replication-platform (state-copy contract), change-data-capture-platform (event-delivery contract), reverse-etl-platform (activation-direction contract), dbt-class transformation tools (transformation without movement — counter-shape), lakehouse/warehouse platforms (destinations, not movers).
- The integration pass explicitly rejected "transformation is definitional" **for the integration Type** (Fivetran ships no arbitrary in-flight transformation yet remains squarely an integration platform) — which leaves transformation-as-contract available as this leaf's discriminator.

## Research Questions

1. What do vendors themselves mean by ETL vs ELT? Is the placement of transformation a product-class boundary or a variant axis?
2. What is the persistent unit of work in ETL/ELT platforms (job / package / pipeline / connection), and what does it contain?
3. How is transformation authored, versioned, tested, and executed? Where does it run (platform engine / pushdown / destination)?
4. What is the destination contract (data stores? table-load semantics?) and the source contract (systems the platform does not own)?
5. How do movement-first managed-ELT products (Fivetran-class) relate to the transformation contract — in-type, straddle, or out?
6. What is the counter-shape (transformation without movement) and does the market treat it as a different product category?
7. Do the pending cross-checks hold: bounded/scheduled vs unbounded/continuous (ESP/ASA passes); lakehouse ingestion-as-entry-machinery (lakehouse pass); scheduled-incremental state-sync straddle (replication pass)?
8. Historical check: does the definition hold for designer-era and pre-graphical ETL?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers + coverage of both technique poles:

| Product | Pole | Tier / model | Docs reached |
|---|---|---|---|
| SQL Server Integration Services (SSIS) | designer-era enterprise ETL (historical anchor, still current) | platform-bundled, enterprise | Tier 1 (Microsoft Learn overview + Data Flow) |
| Matillion ETL / Data Productivity Cloud | cloud pushdown ETL/ELT, transformation-first visual designer | cloud marketplace, mid-market→enterprise | Tier 1 (product page + docs structure) |
| AWS Glue | serverless cloud ETL, visual job canvas + Spark engine | cloud service, all tiers | Tier 1 (what-is doc) |
| Fivetran | managed automation ELT, movement-first (straddle specimen) | SaaS, mid-market→enterprise | Tier 1 (core concepts + transformations) |
| Airbyte | OSS connector-catalog platform, ETL+ELT both | OSS self-host + managed cloud | Tier 1 (core concepts) |
| dbt | **counter-shape**: transformation without movement | OSS + platform | Tier 1 (introduction) |

SSIS serves the historical/market-sample check (2005-era designer ETL, still a current product). Fivetran serves as the movement-first pole and the documented straddle zone with data-integration-platform. dbt serves as the boundary specimen proving the movement leg is load-bearing.

## Sources

All fetched 2026-09-10 (evidence layer A unless noted):

- SSIS overview — https://learn.microsoft.com/en-us/sql/integration-services/sql-server-integration-services
- SSIS Data Flow — https://learn.microsoft.com/en-us/sql/integration-services/data-flow/data-flow
- Matillion product page (Data Productivity Cloud) — https://www.matillion.com/products
- Matillion ETL docs root (structure) — https://docs.matillion.com/metl/ (redirects from docs.matillion.com; Maia docs moved to docs.maia.ai — noted, not fetched)
- AWS Glue — https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html
- Fivetran Core Concepts — https://www.fivetran.com/docs/core-concepts
- Fivetran Transformations — https://www.fivetran.com/docs/transformations
- Airbyte Core Concepts — https://docs.airbyte.com/using-airbyte/core-concepts
- dbt introduction — https://docs.getdbt.com/docs/introduction

Prior-pass evidence cross-referenced (layer A from those passes, not re-fetched): data-integration-platform research notes (Fivetran/Airbyte/Matillion/NiFi/Informatica/SSIS observations, 2026-09-07); data-replication-platform research notes (2026-09-07); reverse-etl-platform research notes (2026-09-09); event-stream-processing-platform + stream-analytics-platform STATUS entries (2026-09-08/09); lakehouse-platform STATUS entry (2026-09-08).

### Source-access limitations

- Matillion's newer Maia documentation (docs.maia.ai) was not fetched; Matillion assertions are limited to the Data Productivity Cloud product page and the Matillion ETL docs information architecture. No Maia-specific claims made.
- Informatica, Talend, Pentaho, Hevo, Stitch not fetched this pass; the integration pass's Informatica page-level evidence and its sourcing limitation (operational docs not article-accessible) are carried forward — no Informatica operational claims made anywhere.
- Pre-graphical ETL (script-based pipelines on schedulers) is covered by structural inference, not fetched legacy docs — recorded as inference, not observation.

## Product Observations

### SQL Server Integration Services (evidence layer A)

From the Microsoft Learn overview and Data Flow pages:

- Self-description: "a platform for building enterprise-level data integration and data transformations solutions." Use cases: copy/download files, load data warehouses, cleanse and mine data, manage SQL Server objects.
- **Data flow structure is the transformation engine made explicit**: "three different types of data flow components: sources, transformations, and destinations. Sources extract data from data stores… Transformations modify, summarize, and clean data. Destinations load data into data stores." Paths connect components; a data flow is "not required to include transformations" (light-movement flows are legal).
- Transformation breadth documented as a first-class category: "updating, summarizing, cleaning, merging, and distributing data… modify values in columns, look up values in tables, clean data, and aggregate column values." Named transformation classes with property expressions (Conditional Split, Derived Column, Fuzzy Grouping/Lookup, Percentage/Row Sampling, Pivot, Unpivot, Sort, OLE DB Command).
- **Error handling is a design surface**: row-level errors at runtime (type conversion, lookup, expression failures) routed to error outputs carrying ErrorCode/ErrorColumn; error flows can feed further transformations or alternate destinations. Inputs configurable to fail / ignore / redirect per column.
- **External metadata snapshots**: designer copies source/destination schema into external columns; validation compares snapshot against live schema and posts errors/warnings on drift. Offline mode exists.
- Packages are the persistent unit; multiple Data Flow tasks per package; SSIS Catalog database "to store, run, and manage packages"; graphical designer + programmable object model; connection managers as the credential/connection abstraction.

### Matillion ETL / Data Productivity Cloud (evidence layer A — product page + docs structure)

From the product page:

- Positioning: "The all-in-one platform to build and manage data pipelines, create no-code data transformations, and deliver data for AI and analytics." Data Transformation pillar: "Cleanse, aggregate, and transform data with ETL no-code and high-code options."
- **Pushdown architecture is the philosophy**: "purpose-built for cloud data platforms including Snowflake, Databricks and Amazon Redshift. Completely native pushdown architecture… data never leaves your cloud platform."
- Connectivity pillar: batch loading ("Automate data pipelines with no coding required"), CDC ("Replicate database changes as they occur with log-based data capture"), 150+ connectors, custom connector via open REST API.
- Transformation/management pillar: Business Logic ("Unify pipeline steps and manage extraction, loading, and transformation"), Pipeline Observability, Scheduling, DataOps (GitHub), Lineage ("trace data from source to target").
- AI-era additions: RAG loaders, prompt components, "Reverse ETL for AI", agentic data engineers (Maia line; Data Productivity Cloud renamed Maia Foundation).

From the Matillion ETL docs information architecture:

- **Two job families**: Orchestration jobs (flow control: Start, If, And/Or, Retry, Iterator components, transactions Begin/Commit/Rollback, Run Orchestration, **Run Transformation**, messaging/webhook, scripting Bash/Python/**dbt Core commands**, variables machinery) and **Transformation jobs** (Read: Table Input, Fixed Flow, Multi/Wildcard Table Input, Stream Input; Transform: Join/Except/Intersect/Unite, Aggregate, Calculator, Convert Type, Distinct, Filter, First-Last, Lead-Lag, Pivot/Unpivot, Rank, Rename, Replicate, Split Field, SQL, Transpose, Window Calculation, Extract Nested Data, Flatten/Construct Variant; Write: Table Output/Rewrite/Update, Create View, External Table Output).
- Connector/Query component library (Salesforce, SAP ODP, Workday, NetSuite, Stripe, Shopify, Zendesk, JDBC Database Query, API Query/Extract with profiles for pagination/parameters/auth), Output components (Oracle/SQL Server/Salesforce…), Cloud Storage Load/Unload, platform-specific DDL components (Create External Table, Create Stream, Refresh Materialized View…), Load generators.
- **Assert components** (Assert Table, Assert View, Assert External Table, Assert Scalar Variables) — data-quality assertions as pipeline components.
- CDC as a module (Manage CDC, configure source database for CDC, CDC shared jobs: Sync All Tables, Sync Single Table).
- Team/ops machinery: Projects bound to a cloud data platform (Snowflake/Redshift/Delta Lake/BigQuery/Synapse), Environments, Variables (job/environment/grid), Manage Schedules, Task History, Task management, Performance monitor, Shared Jobs, Versions, Git integration, Import-Export, Recycle Bin, Audit log, Groups and Permissions, credentials/secret managers, HA cluster, backups.

### AWS Glue (evidence layer A)

From the what-is page:

- Self-description: "a serverless data integration service that makes it easy for analytics users to discover, prepare, move, and integrate data from multiple sources."
- **ETL named directly**: "You can visually create, run, and monitor extract, transform, and load (ETL) pipelines to load data into your data lakes." "With flexible support for all workloads like ETL, ELT, and streaming in one service."
- AWS Glue Studio: "graphical interface… visually compose data transformation workflows and seamlessly run them on the Apache Spark–based serverless ETL engine"; the visual job editor "automatically generate[s] the code to extract, transform, and load your data."
- Feature triad: Discover and organize (crawlers infer schema into the Glue Data Catalog; connections to 70+ sources); Transform/prepare/clean (visual job canvas; job scheduling on schedule/on demand/event; **streaming ETL** "clean and transform streaming data in transit"; FindMatches ML dedup; notebooks; interactive sessions; sensitive-data detection); Build and monitor pipelines (auto-scaling, event-based triggers, "design a chain of dependent jobs and crawlers", workflows, run monitoring with Spark UI/CloudTrail).
- Related services split at the catalog/authorization layer (Lake Formation) and visual no-code preparation (Glue DataBrew) — the market itself separates adjacent functions.

### Fivetran (evidence layer A — the movement-first pole and the ETL/ELT vocabulary source)

From Core Concepts:

- **Vendor's own ETL vs ELT definition**: "accessing data involved building and maintaining fragile ETL (Extract, Transform, Load) pipelines that pre-aggregated and filtered data down to a consumable size. ETL software vendors competed on how customizable, and therefore specialized, their data pipelines were. … Modern data architecture is ELT—extract and load the raw data into the destination, then transform it post-load."
- Connector model: "a Fivetran connector reaches out to your source, receives data from it, and writes it to your destination"; each connector "creates and manages its own schema" (canonical schema); shared-responsibility model — vendor designs/builds/operates extract+load and "orchestrates the transformation, modeling, and validation within the destination"; customer "write[s] SQL queries that transform and model the data we deliver."
- **Transformation posture**: "Our philosophy is to make a faithful replication of source data with as few transformations as necessary"; "a limited set of user-configurable in-flight transformations before loading your data: row filtering and Custom Data Type Mapping. **We do not support arbitrary in-flight transformations** before we load your data. We do support custom push-down transformations in the destination after your data is loaded."
- "Because transformations happen post-load in the destination, your raw data is always available along with the transformed data."
- Sync machinery: incremental cursors, data checkpoints (restart from last checkpoint), re-sync (invalidate cursors, re-fetch all, overwrite), automatic type mapping/inference with a lossless-promotion column-rebuild pattern, naming conventions, release phases (private preview→public preview→beta→GA→sunset).

From Transformations:

- "Orchestrate pre-built and custom data transformations in your destination with Fivetran. … Transformations are automatically executed after connection syncs or on a set schedule."
- Two solutions: pre-built data models (Quickstart; "transform your data into analytics-ready tables") and integrations (Fivetran-hosted dbt, dbt Cloud, Coalesce) — "write, test, version, and document all of your SQL transformations in one place."
- "We use the ELT model, so your raw data is always available alongside your transformed data. If a transformation fails or you need to rethink your data model, you can edit your transformations and run them again on your raw data."
- Scheduling options: integrated (run as soon as relevant destination data updates), frequency-based, deployment.yml.
- Usage metered in monthly model runs (free tier 5,000/month — vendor-specific, research notes only). Limitation: no transformations for Managed Data Lake Service destinations.

### Airbyte (evidence layer A)

From Core Concepts:

- Self-labels: "Data Replication" section title; logo tagline "Simple, secure and extensible data integration"; body: "Airbyte enables you to build data pipelines and replicate data from a source to a destination." (Label drift across the family, consistent with prior passes.)
- Objects: Source, Destination, Connector, **Connection** ("an automated data pipeline that replicates data from a source to a destination"), Stream/Record/Field, Sync Schedule (scheduled/CRON/manual), Destination Namespace, Delivery Method (typed record replication vs raw file copy), Sync Mode, Resumability (checkpoint + auto re-attempt), Typing and Deduping, **Custom Transformations** ("Airbyte Cloud integrates natively with dbt to allow you to use dbt for post-sync transformations… not available for Airbyte Open-Source"), Workspace, Organization.
- Connection configuration parameters: stream/field selection, sync mode, sync schedule, namespace/prefix, schema propagation (drift policy).

### dbt (evidence layer A — counter-shape)

From the introduction:

- "dbt transforms raw warehouse data into trusted data products. You write simple SQL select statements, and dbt handles the heavy lifting by creating modular, maintainable data models…"
- "dbt is the industry standard for data transformation."
- Positioning diagram caption: "dbt works alongside your ingestion, visualization, and other data tools, so you can transform data directly in your cloud data platform."
- Framework = language (SQL select, Jinja, YAML, tests) + engine (compiles the project, executes the transformation graph, produces metadata). Materialization, incremental models, data tests, documentation, version control, CI/CD, idempotence ("Build idempotent transformations that are safe to rerun").
- **No extract/load surface anywhere in the self-description**: dbt's world begins at "raw warehouse data". This is the market's own proof that transformation-without-movement is a different product category.

## Cross-product Comparison

| Aspect | SSIS | Matillion | AWS Glue | Fivetran | Airbyte | dbt (counter-shape) |
|---|---|---|---|---|---|---|
| Persistent unit | package (control flow + data flow tasks) | orchestration job + transformation job | job (visual canvas / code) | connector + connection (config) | connection (source+destination+sync config) | project (models/tests) |
| Movement between external systems | yes (sources/destinations via connection managers) | yes (connector/query components; cloud storage load/unload) | yes (70+ sources; connections) | yes (connector reaches source, writes destination) | yes (source→destination syncs) | **no** (transforms in place) |
| Designed transformation as managed content | yes (transformation component graph; expressions; error flows) | yes (transformation jobs; component library; assert components) | yes (visual transformation workflows; generated code) | partial — orchestrated post-load (pre-built models; dbt/Coalesce integration); minimal in-flight | partial — post-sync dbt (cloud only); typing/deduping in-flight | yes — but it is the whole product |
| Transformation placement | in platform engine (before load) | pushdown to warehouse (generates platform-native processing) | in Spark engine (serverless) | post-load in destination (ELT) | post-load in destination (ELT) | in destination (always) |
| Destination nature | data stores (DBs, files, analytic objects) | cloud data platforms (Snowflake/Redshift/Databricks/BigQuery/Synapse) | data lakes (S3) + catalogs | warehouses/lakes (destinations library) | warehouses/lakes/DBs/analytics tools | the warehouse itself |
| Execution | catalog run; schedulable | schedules; orchestration jobs; webhooks/queues | schedule/on-demand/event triggers; dependent chains | managed schedules; run-after-sync | scheduled/CRON/manual | platform scheduling / CLI / CI |
| Run visibility | SSIS Catalog (store/run/manage); error outputs | task history, performance monitor, lineage | job run insights, Spark UI, CloudTrail | logs, dashboard | run history/monitoring | platform monitoring, docs, lineage |
| Incremental machinery | designer-era (manual patterns) | incremental load tools; CDC module | checkpoint/bookmark machinery (streaming ETL) | cursors + checkpoints + re-sync | sync modes + resumability | incremental models |
| Schema-drift handling | external-metadata snapshot validation | platform-specific tooling | catalog/crawler inference | type inference + lossless promotion | schema propagation policies | tests/contracts |
| Data ownership | none | none (pushdown: data never leaves the platform) | none | none | none | none |

Cross-product commonalities (evidence layer B):

1. Every ETL/ELT product manages **connections to external data systems it does not own** — sources to extract from, destination data stores to load into. (Also the integration Type's L0-1; shared family machinery.)
2. Every product keeps a **persistent, named, re-runnable unit** (package / job / connection / project) — never one-shot.
3. Every product **executes** those units with **run visibility** (catalog / task history / run insights / logs).
4. Every product carries **transformation content in some managed form** — the depth and placement differ (see below), but none of the ETL/ELT-labeled products ships movement alone with no transformation story. (Fivetran, the most movement-first, still ships a Transformations section with pre-built models and dbt orchestration.)
5. **Transformation placement is the great divider — and it is a spectrum, not a binary**: in-engine before load (SSIS) → pushdown to the destination engine (Matillion, Glue-on-warehouse targets) → post-load in destination via SQL/dbt-class tooling (Fivetran, Airbyte). The vendor vocabulary (Fivetran's own ETL-vs-ELT page; Glue's "ETL, ELT, and streaming in one service") treats ETL and ELT as two placements of the same pipeline paradigm.
6. Scheduling/triggering, incremental-loading machinery, schema-drift handling, error/retry machinery, and team/credential/version-control machinery appear across the sample with era- and segment-dependent depth.

## Canonical Abstraction

### L0 — Defining Invariant (jointly-held; each leg's remove-test)

The ETL/ELT Platform is recognizable as such when **both** of these hold:

1. **The movement pipeline between external data systems.** The platform extracts data from source systems it does not own and loads it into a destination data store (warehouse, lake, database), as a persistent, configured, re-runnable unit with managed execution and run visibility. Remove the movement → a transformation tool with no extract/load (dbt-class — the market's own counter-shape); remove persistence/managed execution → one-shot migration scripts or a design tool.
2. **The designed transformation as the pipeline's load-bearing step.** Transformation logic — mapping, cleansing, joining, aggregating, business rules — is authored as a managed, versioned, re-runnable part of the pipeline and determines the shape of the data at the destination. The pipeline's promise is "data arrives in the shape the transformation designed", not merely "data arrives". Remove the designed transformation → pure movement (data-integration / replication territory).

**The placement of the transformation step — before load in the platform's engine (ETL) or after load in the destination (ELT) — is a variant axis, not a contract boundary.** This is what lets designer-era ETL (SSIS), pushdown ELT (Matillion), serverless ETL (Glue), and managed ELT (Fivetran, Airbyte) satisfy the same two structures.

Jointly-held is load-bearing:

- 1 alone = data-integration-platform / replication territory (movement or copy without a designed shape)
- 2 alone = dbt-class transformation tool (the market's own separate category)
- 1+2 = ETL/ELT Platform

### L1 — Common Mature Structure

Present across the sample (B-level):

- Connector catalogs on source and destination sides; custom-connector machinery (SDKs, API profiles, no-code builders)
- Selection of what moves (tables/streams/columns) and mapping into destination naming/structure (namespaces, naming conventions)
- Incremental-loading machinery (cursors/watermarks, incremental-load components, CDC as a sync mechanism)
- Checkpointing/resumability/retries; re-sync/reload paths
- Schema-drift handling (type mapping/inference, lossless promotion, propagation policies, design-time metadata validation)
- Scheduling and triggering (intervals, CRON, manual, event triggers, run-after-sync chaining)
- Orchestration layer over pipelines (dependencies, conditionals, iterators, transactions, run-transformation chaining)
- Run visibility: task/run history, logs, performance monitors; lineage in some products
- Transformation authoring machinery: visual component libraries, SQL/script components, expression languages, assertion/test components, dbt integration
- Team machinery: projects/environments/workspaces, variables, roles/permissions, credential/secret management, Git/version control, import/export, audit

### L2 — Variant / Optional Structure

- **Transformation placement** (the ETL/ELT axis itself): in-platform engine before load; pushdown to the destination engine; post-load in destination via SQL/dbt-class tooling; minimal in-flight only (movement-first pole)
- Design surface: graphical designer/canvas vs configuration-driven vs code/API/infrastructure-as-code
- Destination focus: warehouse/lake-centric vs general databases/files/analytic objects
- Deployment: on-premises designer era; cloud marketplace instances; serverless SaaS; OSS self-host; hybrid data planes
- Streaming ETL as an option (Glue: "clean and transform streaming data in transit") — bounded/scheduled remains the center
- Reverse ETL as an outward extension (Matillion markets it; Fivetran ships Activations) — optional direction, not the contract
- Data-catalog integration, sensitive-data detection, ML-assisted cleansing (Glue FindMatches), AI-era additions (prompt components, RAG loaders, agentic data engineers)
- Data-quality assertions as pipeline components (Assert components; dbt tests) vs standalone data-quality platforms

### L3 — Vendor-specific Structure (Research Notes only)

- Fivetran: Monthly Active Rows pricing; model-run pricing (5,000 free runs/month tier); release phases (private preview→sunset with 90-day notice); canonical-schema shared-responsibility model; Managed Data Lake Service; Context Layer; HVR line
- Matillion: Maia rename (Data Productivity Cloud → Maia Foundation); PipelineOS stateless agents; marketplace editions/subscriptions; HA clusters; queue-messaging components; Maia agentic line
- SSIS: package/catalog architecture; Attunity Oracle/Teradata/SAP connectors; property expressions; ErrorCode/ErrorColumn error outputs; offline mode
- Airbyte: plan ladder (Core/Standard/Plus/Pro/Enterprise Flex); PyAirbyte; no-code connector builder; typing & deduping; its published taxonomy-of-data-movement table
- AWS Glue: crawlers + Glue Data Catalog; Glue DataBrew; Lake Formation; Ray engine end-of-support; FindMatches
- dbt: language/engine split; v1 (Python) vs v2 (Rust) generations; platform vs Core packaging

## Rejected Findings

- **"ETL/ELT Platform = alias of data-integration-platform" (outcome b)** — rejected. The transformation-defined product category is real, long-lived, and self-labeled: a product literally named "Matillion ETL"; AWS Glue marketing "extract, transform, and load (ETL) pipelines" as its visual centerpiece; SSIS self-describing as "data integration and data transformations solutions" with a transformations engine as its core; Fivetran shipping a Transformations section with its own pricing. The transformation contract carries a different user promise (designed shape at the destination), a different monitoring object (transformation success, not just sync success), and a different failure model (type conversions, lookup misses, assertion failures — SSIS's error-output machinery documents this in detail). Outcome (a) — contract slice — is the ruling.
- **"ETL and ELT are two different Types"** — rejected. The placement of transformation is a variant axis: same pipeline object, same promise (shaped data at the destination), different execution placement. Vendor vocabulary treats them as one paradigm with two placements (Fivetran's ETL-vs-ELT page; Glue's "ETL, ELT, and streaming in one service").
- **"Transformation must execute inside the platform"** — rejected (would exclude the managed-ELT pole). Fivetran orchestrates destination-side transformation (pre-built models, dbt/Coalesce) as a managed surface; the transformation remains a managed, scheduled, re-runnable part of the platform's contract even though the execution happens in the destination.
- **"Movement-first managed ELT is out of type"** — rejected as an exclusion; recorded instead as the documented straddle zone. A Fivetran-class product used without its transformation surface behaves as a pure movement platform (integration territory); used with its transformation surface it satisfies both L0 legs. The Type's center of gravity is the designed-transformation pipeline; the movement-first pole sits at the boundary.
- **"Visual canvas / designer is definitional"** — rejected. Fivetran is config-driven with no canvas; SSIS/Matillion/Glue are canvas-centric. Design surface is an L2 axis.
- **"CDC/streaming is definitional"** — rejected. CDC appears as a sync mechanism (Matillion CDC module, Airbyte CDC sync mode, Fivetran connectors); streaming ETL appears as an option (Glue). The bounded/scheduled pipeline remains the center.
- **"The platform owns or stores the data"** — rejected. Across the sample, data at rest belongs to sources/destinations; Matillion's pushdown ("data never leaves your cloud platform") makes this explicit.

## Boundary Findings

### The five-leaf family review — CLOSED (this pass's ruling)

The §13 data-movement cluster is one product population under five leaves, split by **contract** over shared machinery (connections, persistent units, managed execution, run visibility):

| Leaf | Contract | Defining promise |
|---|---|---|
| data-integration-platform | pipeline/movement (generic umbrella) | managed pipelines move data between systems; transformation optional |
| data-replication-platform | synchronized copy | target holds the source's state, kept aligned as the source changes |
| change-data-capture-platform | change-event delivery | the ordered change stream is the product, delivered to consumers |
| reverse-etl-platform | activation direction | consolidated analytical store → business tools, business-object writes |
| **etl-elt-platform (this pass)** | **designed transformation** | **data arrives at the destination in the shape the pipeline's transformation designed** |

This DISCHARGES:

- **data-integration-platform pass's joint-review request** (candidate outcomes recorded 2026-09-07): outcome (a) chosen — ETL/ELT is the transformation-contract slice; the integration platform is the pipeline-management platform spanning techniques, exactly as that pass proposed ("technique-defined slice (transformation job as managed object) with the integration platform as the pipeline-management platform spanning techniques"). Consolidation/alias view (outcome b) rejected with evidence above.
- **data-replication-platform pass's flag** (scheduled-incremental state-sync straddle): resolved from this side — when the promise is "destination mirrors the source's state" (as-is shape, replication vocabulary), it is replication; when the promise is "destination holds transformed/modeled data" (designed shape), it is ETL/ELT. Cadence (scheduled vs continuous) remains a variant axis, confirming that pass's treatment. The straddle zone is real: managed-ELT platforms mirroring source state on schedules sit on the replication side of the seam even when marketed under ELT vocabulary.
- **reverse-etl-platform pass's open family review**: closed. That pass's split (integration/ETL-ELT = consolidation INTO data stores with table-load semantics vs reverse ETL = delivery OUT to business tools with business-object semantics) is ratified from this side; this pass adds the transformation-contract discriminator as the ETL/ELT side's own load-bearing property.
- **event-stream-processing-platform + stream-analytics-platform passes' cross-checks** (bounded/scheduled vs unbounded/continuous): confirmed from this side. Streaming appears in ETL/ELT products only as an ingestion/processing option (Glue streaming ETL; CDC-based incremental sync), never as the center; the managed object remains the bounded, scheduled, re-runnable pipeline. The seam holds.
- **lakehouse-platform pass's note** (lakehouse ingestion is entry machinery; pipeline building/running as center belongs here): consistent — warehouse/lakehouse platforms are the destination estate this Type loads into; they own storage+compute, the ETL/ELT platform owns neither.
- **data-lineage-platform pass's note** (ETL-native lineage is a partial realization): consistent — lineage appears inside ETL/ELT products (Matillion Lineage) as a capability, not the center.

### Other boundaries

- **vs dbt-class transformation tools (no directory leaf)**: transformation without movement is a different product category — dbt's own positioning ("works alongside your ingestion… tools"; transforms "directly in your cloud data platform") is the market's proof. Remove the movement leg from an ETL/ELT platform and you get this category, not this Type.
- **vs data-warehouse / lakehouse platforms (processed)**: destinations own storage + compute; the ETL/ELT platform owns neither (Matillion pushdown executes on warehouse compute but stores nothing). Clear in all sampled products.
- **vs data-quality platform**: assertion/test components exist inside ETL/ELT pipelines (SSIS error outputs, Matillion Assert components, dbt tests), but data quality as a governed discipline is a separate Type; the ETL/ELT platform's assertions serve pipeline correctness.
- **vs workflow automation / iPaaS**: dataset-level bulk movement vs record/event-level operations with business side effects (consistent with the integration pass's vendor-documented split).
- **vs managed-file-transfer**: files may be the medium (S3/Azure/GCS Load/Unload components), but the managed object is the pipeline, not the transfer event.
- **vs database migration tooling (no leaf)**: one-shot cutover vs standing pipeline; persistence is definitional.
- **vs data-virtualization platform (processed)**: virtualization has no movement and no target store; consistent with that pass's remove-tests.

### Remove-tests for the canonical document

- Remove the movement → transformation tool (dbt-class), not this Type
- Remove the designed transformation → pure movement platform (data-integration / replication territory)
- Remove persistence/managed execution → one-shot migration scripts or a design tool
- Promise a synchronized as-is copy instead of a designed shape → data-replication-platform
- Promise an ordered change-event stream → change-data-capture-platform
- Invert the direction to business tools with business-object writes → reverse-etl-platform
- Make the destination the product (storage+compute) → warehouse/lakehouse platform

## Historical / Market-Sample Check (per §24)

- **Designer-era ETL (SSIS, 2005-era, still current)**: packages + data flow (sources/transformations/destinations) + catalog-run execution — satisfies both L0 legs. Passed with direct evidence.
- **Pre-graphical ETL (structural inference, no legacy docs fetched)**: script-based pipelines (shell/SQL scripts under a scheduler) satisfy the conceptual core — movement between systems + designed transformation logic + scheduled re-runnable execution. The definition is written structurally (persistent configured unit + designed transformation + managed execution) so this form fits.
- **The definition does NOT depend on**: graphical designers, visual canvases, cloud, pushdown, connector catalogs, managed ELT, dbt integration, CDC, streaming, usage pricing. All are era/segment implementations (L1/L2).
- **Regional/platform-native check**: SSIS is platform-native (SQL Server-bundled) and fits; OSS cross-platform (Airbyte) fits; cloud-marketplace (Matillion) fits. No region-specific vocabulary is definitional.

Check passed.

## Uncertainties

- Matillion's Maia line (docs.maia.ai) not fetched; Maia-specific behavior unverified — no claims made.
- Informatica/Talend/Pentaho/Hevo/Stitch not fetched this pass; the enterprise-suite pole rests on the integration pass's page-level Informatica evidence (with its recorded sourcing limitation). No operational claims for those products anywhere.
- The usage share of the movement-first pole (Fivetran-class used without transformation surfaces) vs the transformation-first pole is unknown; the straddle zone is documented structurally, not quantitatively.
- Pre-graphical ETL coverage is structural inference, not fetched evidence.
- Stitch's "ETL" self-label with EL-only behavior is prior-pass/market knowledge, not re-verified this pass — recorded as label-drift anecdote only, no claims built on it.

## Final Synthesis

The ETL/ELT Platform is the **transformation-contract slice of the §13 data-movement family**: the platform whose pipelines exist to deliver data to a destination **in a designed shape** — extracted from source systems the platform does not own, transformed through managed, versioned, re-runnable logic, and loaded into a destination data store. ETL and ELT name two placements of the same transformation step (before load in the platform's engine; after load in the destination), not two Types. The family review closes with five contracts over one machinery population: movement (integration), synchronized copy (replication), change-event delivery (CDC), activation direction (reverse ETL), and designed transformation (this leaf). The movement-first managed-ELT pole is the documented straddle zone with the integration platform — in-type when its transformation surface is in use, integration-territory behavior when it is not.
