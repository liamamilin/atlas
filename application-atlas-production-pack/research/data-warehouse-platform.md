# Research Notes — Data Warehouse Platform

## Research Goal

Understand what a **Data Warehouse Platform** actually is as an Application Type — the managed platform that stores an organization's analytical data centrally, in modeled form, and serves governed SQL analytics to many consumers at scale — by observing real products' documentation, not vendor marketing. Produce a vendor-agnostic Application Document with a deliberately minimal defining core, checked against older / differently-architected samples so the definition does not over-fit the modern cloud-native pattern.

## Initial Boundary

Hypothesis before research:

- **What it is**: the storage/compute substrate of an organization's analytical estate. Data is modeled at write (schema-on-write) into a centrally managed store, and the platform's own SQL engine serves large-scale, read-heavy analytical queries for many users, roles, and downstream tools.
- **Primary users**: data engineers, analytics engineers, warehouse administrators, analysts, data scientists; primary downstream consumers: BI tools and SQL clients.
- **Nearest neighbors**: Data Lake Platform, Lakehouse Platform, Business Intelligence Platform, OLAP / Multidimensional Analytics Platform, Data Virtualization Platform, SQL Workbench / Analytical Query Editor, ETL/ELT & Data Integration Platforms.
- **Potential confusions**:
  - vs Data Lake: schema-on-write modeled store vs schema-on-read raw store (the fork that created the lake in the first place).
  - vs Lakehouse: whether the product's store is the modeled warehouse substrate or an open lake substrate with warehouse-grade SQL on top.
  - vs BI Platform: substrate (stores and serves data) vs authored consumer content (dashboards/reports living in a repository).
  - vs OLAP: relational SQL substrate vs cube/multidimensional model as the defining object.
- **Known prior-pass flags to respect**:
  - data-lake-platform pass (2026-09-07): lake/warehouse fork recorded as stable ("schema-on-read open store + engine-neutral governed access vs schema-on-write compute-coupled store"); three-way lake/warehouse/lakehouse seam flagged for joint review; lakehouse discriminator suggested = "transactional tables as the product's centerpiece".
  - business-intelligence-platform pass: warehouse = "the storage/compute substrate (modeling and serving data at scale, no authored consumer content)"; no conflict.
  - analytical-query-editor pass (referenced): editors author/run queries; warehouses store/serve the data they run against.

## Research Questions

1. What are the platform's core objects (store, tables, compute, roles) and how do they relate?
2. How does data enter the warehouse, and what does "modeling at write" concretely require?
3. Is compute part of the platform or attachable? Is storage/compute separation definitional or architectural variant?
4. How is access governed (roles, permissions, row/column controls, audit)?
5. Who consumes the warehouse and through what interfaces?
6. What operational behaviors matter (scaling, concurrency, cost, retention/recovery, time travel)?
7. What is common mature structure vs defining core? (columnar storage? cloud? serverless? data sharing? AI features?)
8. Does an older, on-premises, compute-coupled warehouse still fit the minimal core? (historical check)
9. Where is the seam with Data Lake, Lakehouse, BI, OLAP, Data Virtualization — and is the leaf a real Type or a drift continuum?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy / tier | Why sampled |
|---|---|---|
| **Snowflake** | cloud-native pure-play; storage/compute separation; multi-cluster virtual warehouses; credit-based | the archetype of the modern cloud warehouse pattern; excellent operational docs |
| **Amazon Redshift** | hyperscaler cluster-managed warehouse (provisioned + serverless); PostgreSQL lineage | shows the cluster/leader-node MPP pattern and managed-storage tiering inside a hyperscaler |
| **Microsoft Fabric Data Warehouse** | SaaS suite warehouse "on a data lake foundation" (Delta open format); capacity-based | the boundary-drift case: warehouse converging toward lake/lakehouse substrate |
| **Teradata (VantageCloud / Teradata Cloud)** | long-established enterprise MPP vendor; cloud, on-premises (Factory), hybrid | historical/on-prem pole and enterprise tier; compute-model contrast (active vs elastic) |

Deliberately excluded: **Databricks** (self-identifies as lakehouse platform; belongs to the sibling leaf — used by the lake pass as its boundary case). **Google BigQuery** intended as the serverless hyperscaler pole but abandoned (see Sources — network limitation); no Google-specific claims are made anywhere in this research.

## Sources

Research date: 2026-09-07. Tier 1 (official operational documentation) unless noted.

- Snowflake Documentation: "Key concepts and architecture" — https://docs.snowflake.com/en/user-guide/intro-key-concepts
- Snowflake Documentation: "Virtual warehouses" — https://docs.snowflake.com/en/user-guide/warehouses
- Snowflake Documentation: "Overview of Access Control" — https://docs.snowflake.com/en/user-guide/security-access-control-overview
- Amazon Redshift Developer Guide: "Introduction to Amazon Redshift" — https://docs.aws.amazon.com/redshift/latest/dg/welcome.html
- Amazon Redshift Developer Guide: "Amazon Redshift architecture" + "Data warehouse system architecture" — https://docs.aws.amazon.com/redshift/latest/dg/c_redshift_system_overview.html , https://docs.aws.amazon.com/redshift/latest/dg/c_high_level_system_architecture.html
- Microsoft Learn: "What is data warehousing in Microsoft Fabric?" + Fabric Data Warehouse documentation TOC — https://learn.microsoft.com/en-us/fabric/data-warehouse/data-warehousing , https://learn.microsoft.com/en-us/fabric/data-warehouse/
- Teradata developer portal + Teradata Cloud platform page (Tier 2 — product/positioning pages; docs.teradata.com content is JavaScript-rendered and not readable by fetch) — https://developers.teradata.com/quickstarts/ , https://www.teradata.com/platform/vantagecloud

Source-access limitations:

- **Google BigQuery** (cloud.google.com): timed out ×2 this pass (intro + quickstart pages); the BI pass also recorded repeated timeouts ×2. Abandoned per the network rule. BigQuery is therefore NOT usable as a sampled product; no Google-specific claims appear in this research or the final document.
- **docs.teradata.com**: JavaScript application; page content does not render. Teradata evidence is limited to the developer portal and platform product pages (Tier 2) plus doc-section titles visible in links (users/roles/compute-groups console, RBAC, SSO, JDBC/Python/REST/dbt/Jupyter connectivity). Teradata-specific operational claims are kept correspondently modest.
- Amazon Redshift workload-management and cluster-management sub-pages were not fetched (architecture page provides the structural evidence needed; stop conditions met).

## Product observations

### Snowflake — key concepts, virtual warehouses, access control

Evidence layer: A (directly observed, official docs).

- Positioned as "an advanced data platform … provided as a self-managed service": no hardware or software to select/install/manage; runs on public cloud infrastructure; cannot be installed on-premises.
- Architecture described as hybrid shared-disk/shared-nothing: a **central data repository** for persisted data accessible from all compute nodes, with **MPP compute clusters** processing queries. Three layers: **database storage**, **compute**, **cloud services**.
- **Database storage**: structured data "follows a strict tabular schema"; when data is loaded into a Snowflake table, it is **reorganized into an internally optimized, compressed, columnar format**; storage is fully managed (organization, file size, structure, compression, metadata, statistics); data automatically divided into micro-partitions. Table types: standard Snowflake tables ("ideal for data warehouses"), **Iceberg tables** (data/metadata in *external* cloud storage the customer manages — "ideal for existing data lakes and data lakehouses"), hybrid tables (low-latency, row locking, referential integrity — transactional workloads).
- **Compute**: a **virtual warehouse** is "a cluster of compute resources"; each is independent, shares no compute with other warehouses, "has no effect on the performance of other virtual warehouses"; required for queries and all DML including loading; must be running; consumes credits while running. Multi-cluster warehouses scale for concurrency. Sizes and auto-activity properties; Snowpark-optimized type for large-memory ML workloads.
- **Cloud services layer**: authentication/access control, metadata management, query parsing/optimization, infrastructure management — coordinates everything from sign-in to query dispatch.
- **Loading**: COPY INTO from files; Snowpipe (auto-load as files land in a stage); Snowpipe Streaming (row-level continuous); Openflow connectors; connectors. **Transforming**: dynamic tables (target-freshness auto-refresh), streams & tasks (change capture + scheduled transformations), Snowpark (Python/Java/Scala), dbt projects.
- **Analytics**: aggregate/window functions, CTEs; **semantic views** storing business concepts/metrics in the database; Cortex AI functions (LLM SQL over text/images); Snowflake ML.
- **Collaboration**: secure data sharing (share selected objects with other accounts, no copying), listings + marketplace, data clean rooms; cross-region/cloud layer (Snowgrid), replication for DR.
- **Connecting**: web UI (Snowsight), CLI, Python/REST APIs, **JDBC/ODBC drivers for other applications**, connectors (Kafka, Spark), third-party ETL and BI tools.
- **Access control**: combines DAC (object owners grant) + **RBAC** (privileges → roles → users) + UBAC; securable objects in a container hierarchy (organization → account → database → schema → tables/views/functions/stages); role hierarchies with inheritance; system-defined roles (ACCOUNTADMIN, SYSADMIN, SECURITYADMIN, USERADMIN, PUBLIC …); "There is no concept of a 'super-user' or 'super-role' … All access requires appropriate access privileges"; access-request flow from the web UI when a query fails on missing privileges.

### Amazon Redshift — introduction & system architecture

Evidence layer: A.

- "A fully managed, petabyte-scale data warehouse service in the cloud." Serverless variant: access/analyze "without the usual configurations of a provisioned data warehouse"; capacity auto-scaled; no charges when idle. Load data and query "in the Amazon Redshift query editor v2 or in your favorite business intelligence (BI) tool".
- "An enterprise-class relational database query and management system"; based on **open standard PostgreSQL** (with documented SQL differences); integrates with ETL and BI/reporting/data mining/analytics tools.
- "Achieves efficient storage and optimum query performance through a combination of **massively parallel processing, columnar data storage**, and … targeted data compression."
- Architecture: the **cluster** is the core infrastructure component — one or more **compute nodes**; with two or more nodes a **leader node** "parses and develops execution plans", compiles code, distributes to compute nodes, handles external communication; client applications interact only with the leader node; compute nodes transparent to clients. Compute nodes partitioned into **slices**, each processing a portion of the workload.
- **Distribution key**: when creating a table you may specify one column as the distribution key; rows are distributed to node slices according to it at load time.
- **Redshift Managed Storage (RMS)**: "a separate storage tier" using Amazon S3, scaling to petabytes; "you can scale and pay for computing and storage independently, so that you can size your cluster based only on your computing needs"; SSD local storage as tier-1 cache.
- A cluster contains one or more **databases**; user data stored on compute nodes. "Although it provides the same functionality as a typical RDBMS, including online transaction processing (OLTP) functions such as inserting and deleting data, Amazon Redshift is **optimized for high-performance analysis and reporting of very large datasets**."
- Workload management exists as a documented subsystem (classification/queues — TOC-level evidence only).

### Microsoft Fabric Data Warehouse — overview

Evidence layer: A.

- "Fabric Data Warehouse is an enterprise scale relational warehouse **on a data lake foundation**." Ideal use cases: "star or snowflake schemas, curated corporate data marts, governed semantic models for business intelligence."
- "Not a traditional enterprise data warehouse, it's a **lake warehouse**": data "like all Fabric data, is stored in **Delta tables** (Parquet data files with a file-based transaction log)" — the Fabric open data format; sharing/collaboration without compromising security/governance.
- Developed primarily with **T-SQL**; shares the SQL Database Engine surface; **full multi-table ACID transactions**, materialized views, functions, stored procedures.
- Loading: COPY INTO, Pipelines, Dataflows, CTAS/INSERT..SELECT cross-database ingestion, bulk via Spark written directly to Delta tables.
- "Autonomous workload management … no knobs to turn"; "Scale near instantaneously … **Storage and compute are separated**"; data automatically replicated to OneLake Files for external access.
- Two warehousing items: the **Warehouse** (full DDL+DML) and the autogenerated **SQL analytics endpoint** over a Lakehouse's Delta folders (T-SQL define/query + views/functions/procedures + permissions, but no data modification) — the "SQL view" of the lake.
- Decision guidance: choose warehouse for "enterprise-scale solution with open standard format, no knobs performance, and minimal setup … semi-structured and structured data"; choose lakehouse for "highly unstructured data … Spark as your primary development tool".
- Suite integration: "tightly integrated with Power BI"; semantic models; cross-database queries "for fast insights with zero data duplication"; built for "any skill level, from the citizen developer to DBA or data engineer".
- Governance/ops surfaces (from doc TOC): workspace roles, SQL granular permissions, row-level and column-level security, Entra ID authentication, audit logs; capacity: burstable capacity, pause and resume, smoothing/throttling, workload management; recovery: restore in-place, table clones, warehouse snapshots; monitoring: capacity metrics app, DMVs, query insights.

### Teradata — developer portal & Teradata Cloud (Tier 2)

Evidence layer: B (official product pages; operational docs unreachable).

- Deployment breadth: cloud (AWS, Azure, Google Cloud), **on-premises ("Factory")**, hybrid; "Run where it makes the most sense—cloud, hybrid, or edge". One of the longest-established enterprise data-warehouse vendors (appliance lineage — IntelliFlex/Enterprise families appear in doc links).
- Compute model: "**active compute**" (always-on, mission-critical) vs "**elastic compute**" (on-demand, for "training, experimentation, and burst workloads"); "Elastic, modular compute scales up or down as demand changes—without over-provisioning."
- Open table formats: "Elastic compute … operates directly on **Iceberg and Delta tables in object storage**." Platform runs "AI and analytics, **lakehouse, EDW**, and data engineering side-by-side on a single platform."
- Governance: console-managed **users, roles, compute groups**; role-based access control; identity-provider SSO; "consistent identity, access, and policy controls across cloud and hybrid environments."
- Connectivity: JDBC, Python, REST API, dbt, Jupyter notebooks, Airflow/Dagster orchestration, BI tools; "Build for cloud, on-premises, or hybrid environments without giving up enterprise governance or scale."

## Cross-product Comparison

| Dimension | Snowflake | Redshift | Fabric DW | Teradata | Verdict |
|---|---|---|---|---|---|
| Central managed analytical store | central repository; managed storage, micro-partitions | RMS on S3; user data on compute nodes | OneLake Delta tables | platform-held enterprise store (cloud/on-prem) | **Core** — all four hold the organization's analytical data in a platform-managed store |
| Schema-on-write modeling | tables with strict tabular schema; data reorganized on load into optimized format | typed relational tables; distribution key defined at table creation | T-SQL DDL; star/snowflake schemas; curated marts | EDW modeling tradition | **Core** — data is conformed to defined structures; modeling is the usage discipline |
| Platform-owned SQL compute | virtual warehouses; cloud-services layer parses/optimizes/dispatches | leader + compute nodes; proprietary distribution | SQL Database Engine; autonomous workload mgmt | active/elastic compute; MPP lineage | **Core** — users connect to the platform's engine; they do not attach engines to a store |
| Many consumers via SQL interfaces | Snowsight, JDBC/ODBC, BI tools, connectors | query editor v2, BI tools, PostgreSQL-compatible clients | SQL query editor, T-SQL endpoints, Power BI | JDBC/Python/REST/dbt, BI tools | **Core** — standard SQL surface for humans and tools |
| Governed multi-user access | RBAC/DAC object hierarchy; no super-user; access requests | RDBMS permission model (details not fetched) | workspace roles, SQL granular permissions, RLS/CLS, audit | RBAC, roles/compute groups, SSO | **Core (as platform property)** — permission-controlled shared serving; fine granularity is common mature structure |
| Storage/compute separation | yes (defining architecture) | yes (RMS; scale/pay independently) | yes ("scale near instantaneously") | variant (active vs elastic; appliance heritage couples them) | **Common-modern, NOT core** — appliance-era warehouses lacked it |
| MPP / distributed | yes (MPP clusters) | yes (leader/compute/slices) | distributed query processing | MPP lineage | **Common, NOT core** (single-box warehouses existed; phrase as "scaled analytical compute") |
| Columnar storage | yes (reorganized columnar) | yes | Delta/Parquet (columnar) | not verified from fetched evidence | **Common-modern, NOT core** |
| Cloud-only | yes (cannot run on-prem) | cloud service | SaaS | cloud OR on-prem OR hybrid | **NOT core** — on-prem/hybrid pole exists (historical check) |
| Serverless / autosuspend compute | sized warehouses, auto-activity properties, credit consumption | serverless variant; no idle charges | capacity pause/resume; smoothing/throttling | active vs elastic compute | **Common-modern, NOT core** |
| In-place ELT transforms | dynamic tables, streams/tasks, Snowpark, dbt | SQL, UDFs (Python UDF end-of-life noted in docs) | CTAS, stored procedures, materialized views | in-database analytics functions | **Standard capability** |
| Bulk + continuous ingestion | COPY INTO, Snowpipe, Snowpipe Streaming, connectors | COPY from S3 (docs welcome page) | COPY INTO, Pipelines, Dataflows, Spark bulk | connectors/orchestration | **Standard capability** |
| RBAC + row/column-level security | explicit, deep | present (not fetched in detail) | explicit | explicit | **Standard capability** |
| Time travel / cloning / recovery | (documented elsewhere; referenced in ecosystem) | — | warehouse snapshots, table clones, restore in-place | — | **Common/Optional** |
| Cross-account data sharing | secure data sharing, listings, marketplace, clean rooms | — | share warehouse permissions; OneLake replication | — | **Optional / variant** (strong in some products, absent in others) |
| Semantic/metric layer in-database | semantic views | — | semantic models (Power BI side) | — | **Optional** |
| AI/ML in-platform | Cortex, Snowflake ML | — | AI functions | AI Studio, agentic recipes | **Optional, current-market common** |
| Open-format substrate (Delta/Iceberg) | Iceberg tables (external storage option) | — | Delta everywhere ("lake warehouse") | elastic compute on Iceberg/Delta | **Variant — boundary drift toward lakehouse** (see Boundary Findings) |

## Abstraction Levels (internal synthesis)

### L0 — Defining Invariant (minimal)

Three properties; each removal test was run against all sampled products:

1. **The central modeled store of record** — the platform holds the organization's analytical data as a central, platform-managed store, conformed at write time into defined relational structures (databases/schemas/tables with typed columns). Removal test: drop schema-on-write (store raw, schema-on-read, engines interpret) → Data Lake Platform. Drop the store (query without holding) → Data Virtualization.
2. **Platform-owned analytical SQL compute** — the platform provides its own query/compute engine(s) optimized for large-scale, read-heavy analytical SQL over the whole store; consumers connect to the platform's engine rather than attaching their own engines to the store. Removal test: drop platform-owned compute (engine-neutral store with attachable engines) → the lake pattern; drop scale-out analytical optimization (row-oriented operational processing) → an operational RDBMS, not a warehouse.
3. **Governed serving of many consumers** — the store+compute is offered as a shared, permission-controlled resource to multiple users, roles, and workloads, and to downstream tools, through standard SQL interfaces. Removal test: drop the multi-consumer governed serving and platform management (bare engine + files) → an analytic DBMS/library rather than a platform; a single-user tool → not this Type (it is the substrate without the platform).

### L1 — Common Mature Structure

- ingestion machinery: bulk load (COPY-class), continuous/streaming load (pipe-class), connector/orchestration integration
- in-place ELT transformation: CTAS/INSERT-SELECT, views, stored procedures, materialized views, scheduled tasks/pipelines, change capture; dbt-class external SQL frameworks operate on the same model
- compute management: sized/elastic compute units (virtual warehouses / clusters / capacity), scale up/down/out, workload management, auto-suspend/pause or active-vs-elastic poles
- governance: RBAC roles + object hierarchy, row-/column-level security, masking, audit logs
- monitoring/operations: query history, load monitoring, usage/cost metrics, capacity management
- recovery: retention/time travel or snapshot/clone/restore (mechanism varies by product/era)
- interface set: SQL editor/worksheets, object explorer, load/ingest wizards, compute console, permission administration, monitoring/cost views
- connectivity spine: JDBC/ODBC drivers, REST/SDKs, CLI, native BI-tool integration, ETL/ELT tool integration

### L2 — Variant / Optional Structure

- **storage/compute separation** — the modern cloud pattern (Snowflake, Redshift RMS, Fabric) vs coupled appliance (Teradata heritage); not definitional
- **compute provisioning poles** — provisioned clusters (Redshift) vs serverless (Redshift Serverless) vs capacity-based SaaS (Fabric) vs active+elastic (Teradata) vs credit-metered warehouses (Snowflake)
- **deployment** — cloud-only vs cloud+on-prem+hybrid (Teradata); SaaS multi-tenant (Fabric)
- **open-format substrate** — proprietary managed store (Snowflake native tables, Redshift internals) vs open Delta/Iceberg substrate (Fabric "lake warehouse", Teradata elastic on Iceberg/Delta, Snowflake Iceberg tables as an external option) — the converging seam with the Lakehouse leaf
- **store extensions** — semi-structured (JSON/VARIANT) and even unstructured data in the store; hybrid/transactional tables
- **cross-account sharing / marketplace / clean rooms** — strong in some products, absent in others
- **in-database ML / LLM SQL assistants / semantic layers** — current-market optional

### L3 — Vendor-specific (research notes only)

- Snowflake: micro-partitions, Snowpipe/Snowpipe Streaming names, Snowpark, Cortex, Snowgrid, Native App Framework, system-defined role names, credit model, managed-access schemas, future grants, Iceberg/hybrid table products, Snowsight, access-request workflow.
- Redshift: leader/compute-node/slice terminology, distribution keys & dist styles, RMS data-block temperature caching, PostgreSQL differences doc, Python UDF end-of-life policy, query editor v2.
- Fabric: Warehouse vs SQL analytics endpoint item split, OneLake, mirroring (Snowflake/Databricks/Cosmos DB…), capacity smoothing/throttling semantics, DMVs, workspace roles naming, Fabric decision guide.
- Teradata: VantageCloud Lake/Enterprise editions, compute groups, active vs elastic compute naming, ClearScape Analytics, AI Studio, agentic recipe book, Factory (on-prem).

## Rejected Findings (anti-overfitting)

Each of the following is common in the current market but was rejected from the defining core, with reasons:

1. **Storage/compute separation** — universal in the cloud-native generation but absent in appliance-era and on-premises warehouses (Teradata Factory heritage); the historical check fails if it is required. Kept as variant.
2. **Columnar storage** — three of four sampled products document columnar (Teradata unverified); a defining-core candidate by frequency, but it is an implementation technique, not the structure that makes the Type recognizable; also unverified in one sample. Kept as common implementation detail.
3. **Cloud delivery / SaaS** — Teradata's on-premises and hybrid poles directly contradict; the appliance era passes the historical check without cloud. Kept as variant.
4. **Serverless or auto-suspending compute** — modern commercial mechanics, not structure. Variant.
5. **MPP** — dominant but a scaling technique; "optimized for large-scale analytical SQL" is the abstraction. Kept generic in core.
6. **Data sharing/marketplace, semantic layers, in-database ML/AI, clean rooms** — optional/variant; present in some products only; several are L3-named modules.
7. **Streaming ingestion, dynamic/materialized tables, time travel** — standard or optional capabilities, all removable without the product ceasing to be a warehouse.
8. **"Dimensional model required"** — star/snowflake schemas are the classic usage discipline (Fabric names them ideal use cases), but warehouses also host operational reporting stores, ELT landing zones, and semi-structured analytics; modeling-at-write is the invariant, dimensional modeling is the traditional discipline. Not core.

## Boundary Findings

With "remove X → becomes Y" tests for the nearest directory neighbors:

1. **vs Data Lake Platform** — the founding fork. Warehouse: schema-on-write, data conformed into defined relational structures in a platform-managed store, platform-owned compute. Lake: schema-on-read raw store in open formats, engine-neutral, governed multi-engine access. Remove schema-on-write modeling and platform-owned compute → lake. Consistent with the lake pass's recorded seam ("schema-on-write compute-coupled store"). The one refinement: "compute-coupled" is precise only for the appliance era; the modern warehouse couples compute *organizationally* (one platform, one engine family, one permission authority) even when storage and compute are physically separated. Both documents describe the seam compatibly.
2. **vs Lakehouse Platform** (unprocessed sibling) — per the lake pass's recommended discriminator: the lakehouse makes **transactional (ACID) tables over open lake formats the product's centerpiece**. The warehouse's centerpiece is the modeled analytical store of record with its own SQL platform. Drift is real and documented: Fabric self-describes as a "lake warehouse" on Delta (open format, ACID, SQL engine — nearly the lakehouse definition while still naming itself a warehouse); Teradata elastic compute operates on Iceberg/Delta; Snowflake offers Iceberg tables over external storage. The population is converging from both sides. Flag for joint review at the lakehouse pass: the discriminator may need to be "what is the substrate of record" (modeled warehouse store vs open lake tables) rather than feature presence.
3. **vs Business Intelligence Platform** — substrate vs authored content. The warehouse models and serves governed data at scale; it does not author, repository, or distribute analytical content for consumers. BI connects via SQL/drivers (direct evidence in all four products). Matches the BI pass's recorded seam. Remove the store/compute and keep authoring/repository/distribution → BI; remove authoring and keep store/compute → warehouse. Boundary clean.
4. **vs OLAP / Multidimensional Analytics Platform** — the cube/multidimensional model (dimensions/measures, slice-dice-drill) is the OLAP leaf's defining object, historically served *from* a warehouse; the warehouse is model-agnostic relational substrate. Remove the modeled store and serve cubes only → OLAP. Consistent with the BI pass's flag.
5. **vs Data Virtualization Platform** — virtualization answers queries over data it does not physically hold; the warehouse physically holds its store of record. Remove the store → virtualization.
6. **vs SQL Workbench / Analytical Query Editor** — editors author/run queries against data living elsewhere (including warehouses); the warehouse is where the data and compute live. The warehouse ships its own query editor as an interface (all four sampled products do), which is why the boundary needs stating: the editor surface is an interface of the platform, not the Type's center of gravity.
7. **vs ETL/ELT & Data Integration Platforms** — integrations are custodians of data in *movement* and typically fill the warehouse; the warehouse is a destination system of record with in-place transforms (ELT). The warehouse's load machinery (COPY/pipe-class) is ingestion to its own store, not cross-system movement.
8. **vs operational RDBMS / Database Management Console** — the warehouse is optimized for analytical scan/aggregation over very large datasets (Redshift doc explicitly contrasts with OLTP function); a management console administers whatever DBMS it targets; the warehouse's admin surfaces are internal to the platform.
9. **vs Data Catalog / Governance / Quality Platforms** — standalone catalog/governance products describe and govern data living in systems they do not own; the warehouse embeds governance machinery *for its own store* (roles, RLS/CLS, audit). The embedded subset is not the standalone Type.

## Uncertainties

1. **Google BigQuery not sampled** (cloud.google.com unreachable ×2 this pass, ×2 in the BI pass). The serverless-hyperscaler philosophy is therefore represented only indirectly (Redshift Serverless, Fabric capacity model). No BigQuery-specific claims made.
2. **Teradata operational depth**: docs.teradata.com is JS-rendered; Teradata evidence is Tier 2 (product pages + doc-section titles). Claims kept at structure level (deployments, compute poles, RBAC/compute-group surfaces, connectivity). No precise operational rules asserted for Teradata.
3. **Redshift workload management / permission model details** not fetched (TOC-level only); Redshift governance is not cited as direct evidence beyond what the fetched pages state.
4. **Fabric's exact position on the lake/warehouse/lakehouse continuum** is partly a naming decision by Microsoft ("not a traditional enterprise data warehouse, it's a lake warehouse"); treated here as the boundary-drift case, not as a definitional counterexample.
5. **Warehouse "mart/EDW" layering** (enterprise warehouse vs data marts vs operational data stores) is an architecture-era vocabulary; not directly evidenced in fetched pages beyond Fabric's "curated corporate data marts" phrase; the final document mentions the discipline only qualitatively.
6. **Precise operational details** (credits, sizes, SLAs, limits, retention windows) intentionally excluded; vendor-specific where observed (L3 above).

## Final Synthesis

A **Data Warehouse Platform** is the modeled-store-and-compute substrate of an organization's analytical estate, operated as a governed platform:

```text
Organization's analytical data
→ loaded and conformed at write into a central, platform-managed store
   (databases → schemas → tables/views, typed, modeled)
→ the platform's own SQL compute runs analytical queries at scale over it
→ access is permission-governed (roles, row/column controls, audit)
→ many consumers are served through standard SQL surfaces
   (SQL editors, BI tools, applications, pipelines)
→ operated continuously: scale, cost, recovery, retention
```

The defining core is small: **central modeled store of record + platform-owned analytical SQL compute + governed serving of many consumers**. Everything else the market associates with the category — storage/compute separation, columnar formats, serverless elasticity, streaming ingestion, time travel, data sharing, marketplaces, semantic layers, AI features — is common mature structure or variant, verified removable without the product ceasing to be a warehouse. The historical check passes: an on-premises appliance-era enterprise warehouse (Teradata pole) satisfies all three core properties with no cloud, no separated storage, and no modern formats.

The market's live seam is with the **Lakehouse** leaf: modern warehouses increasingly adopt open lake table formats (Delta/Iceberg) as their substrate (Fabric's self-described "lake warehouse"; Teradata elastic compute on Iceberg/Delta; Snowflake Iceberg tables), while lakehouse platforms add warehouse-grade SQL. The recommended discriminator (from the lake pass, to be ratified at the lakehouse pass): whether the product's store of record is the modeled warehouse substrate (this Type) or open lake tables upgraded with transactional semantics (Lakehouse), with the convergence explicitly flagged for joint review.
