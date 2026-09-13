# Research Notes — Data Integration Platform

Research date: 2026-09-07
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand what a Data Integration Platform actually is as a Type of application: what objects exist inside it, what users do with them, how a pipeline's life runs, and where the boundary lies against the dense cluster of §13 siblings (ETL/ELT Platform, Change Data Capture Platform, Data Replication Platform, Reverse ETL Platform, Data Virtualization Platform, Data Fabric Platform, Data Exchange Platform, Managed File Transfer, EDI Platform).

Two prior passes left binding cross-checks:

- **data-exchange-platform pass**: held the boundary "intra-org movement vs inter-org entitlement" against data-integration-platform / data-replication-platform / data-virtualization-platform; recommended cross-check at their passes.
- **data-fabric-platform pass**: ratified a split — fabric = estate-spanning unified metadata layer with integration/governance/delivery as functions of one system; **integration platform = pipeline building/running as the center**; virtualization platform = logical access technique as the center. Joint review recommended when either leaf is processed.
- **change-data-capture-platform pass** (processed): CDC = ordered row-level change-event stream contract; replication = synchronized target copy; ETL/ELT = destination reflects source as of each scheduled sync; described Data Integration Platform as "umbrella sibling — broader family covering batch, API, and application connectors."

The CDC pass's "umbrella" wording is a warning: if the integration leaf is defined only as the family umbrella, it is a category word, not a Type. The synthesis must give it a center of its own (the pipeline) or record a taxonomy problem.

## Initial Boundary

Initial hypothesis before research:

- Core use: connect source systems to destination systems and move/transform data between them on an ongoing basis.
- Users: data engineers / analytics engineers; enterprise variants add data architects.
- Nearest neighbors: ETL/ELT Platform (likely heavy overlap — possible alias), CDC / replication / reverse ETL (technique or contract slices), data virtualization (no-copy alternative), iPaaS / workflow automation (record-level business operations), Managed File Transfer (file-event movement), data warehouse/lakehouse (destination platforms that own storage).
- Unknowns: whether "data integration platform" has a distinct managed object of its own; whether transformation is definitional; where design surface variance (wizard vs canvas vs code) lands; historical check (pre-cloud designer-era tools).

## Research Questions

1. What are the core objects? (connection, connector, pipeline, mapping/transformation, schedule, run/job, logs)
2. How does a user build a new pipeline, end to end?
3. How are pipelines executed and triggered (schedule, manual, event, external orchestrator)?
4. What happens when a pipeline fails? (checkpoints, cursors, resumability, retries, re-sync)
5. What sync modes exist (full refresh, incremental, CDC, append vs upsert)? Which are universal?
6. Where do transformations happen (in-platform engine, pushdown to destination, post-load)? Is transformation definitional?
7. How is schema change in sources handled?
8. Who uses the product, and what are the interfaces (config UI, visual canvas, code/API)?
9. Does the platform own the data (storage/compute) or only the movement?
10. Where is the boundary against CDC/replication/ELT labels, virtualization, exchange, fabric, iPaaS, MFT?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Pole | Tier / model | Docs reached |
|---|---|---|---|
| Fivetran | managed automation ELT (config-driven, vendor-operated connectors) | SaaS, mid-market→enterprise | Tier 1 (docs + core concepts) |
| Airbyte | open-source connector-catalog replication platform | OSS self-host + managed cloud, SMB→enterprise | Tier 1 (platform + core concepts) |
| Matillion ETL | visual low-code designer with pushdown transformation to cloud warehouses | cloud marketplace editions, mid-market→enterprise | Tier 1 (docs structure + feature pages) |
| Apache NiFi | OSS flow-based dataflow/routing framework (visual, continuous) | self-hosted OSS, engineering teams | Tier 1 (project overview doc) |
| Informatica (IDMC Data Integration & Engineering) | enterprise data-management suite, integration as flagship service | enterprise suite | Tier 2 (product page; docs portal not article-fetchable) |
| SQL Server Integration Services (SSIS) | historical / platform-embedded designer-era ETL (checked for §24) | platform-bundled | Tier 1 (Microsoft Learn overview) |

SSIS serves the historical/market-sample check: a 2005-era, on-premises, designer-built ETL platform that is still a current product, used to prevent over-fitting the definition to the modern managed-ELT implementation.

## Sources

All fetched 2026-09-07.

- Fivetran Documentation — https://fivetran.com/docs (evidence layer A)
- Fivetran Core Concepts — https://fivetran.com/docs/core-concepts (A)
- Airbyte Documentation root — https://docs.airbyte.com/ (A)
- Airbyte Data replication platform — https://docs.airbyte.com/platform/ (A)
- Airbyte Core Concepts — https://docs.airbyte.com/platform/using-airbyte/core-concepts (A)
- Matillion ETL Docs — https://docs.matillion.com/metl/ (A — docs structure; individual feature pages sampled from TOC)
- Apache NiFi — https://nifi.apache.org/ (A)
- Apache NiFi Overview — https://nifi.apache.org/docs/nifi-docs/html/overview.html (A)
- Informatica Data Integration and Engineering product page — https://www.informatica.com/products/cloud-data-integration.html (A at product-page level; operational docs at docs.informatica.com were not article-fetchable from this environment — see Limitations)
- Microsoft SQL Server Integration Services overview — https://learn.microsoft.com/en-us/sql/integration-services/sql-server-integration-services (A)

### Source-access limitations

- Informatica's operational documentation portal (docs.informatica.com) did not yield readable article content; evidence for Informatica is **product-page level only** (Tier 2). Per the evidence rules, no precise operational claims (object names, limits, defaults) are asserted for Informatica in the canonical document; its role in the sample is to confirm the suite-embedded pole and the "single platform for virtually all integration patterns" positioning, with marketing figures (TCO/time claims) deliberately discarded.
- Matillion evidence comes from the docs information architecture plus sampled feature pages, not a full read of every feature page. Assertions kept at structure level (jobs, components, orchestration vs transformation, schedules, task history, CDC support, permissions).
- NiFi evidence is from the project overview document, which is explicit about concepts (FlowFile, Processor, Connection, Process Group, provenance). Fine-grained UI behavior was not fetched; not asserted.

## Product Observations

### Fivetran (evidence layer A)

Observations from /docs and /docs/core-concepts:

- Core vocabulary: **connector** ("a Fivetran connector reaches out to your source, receives data from it, and writes it to your destination"), **destination**, **connection** (configured instance), **sync**. Docs sections: Getting Started, Core Concepts, Connectors, Connector SDK, Destinations, Transformations, Activations, Logs, Managed Data Lake Service, Context Layer.
- Each connector "creates and manages its own schema" in the destination; naming conventions offered (Fivetran naming / source naming).
- Explicit ELT philosophy: extract+load is vendor-operated; transformation happens post-load in the destination (dbt-compatible data models; push-down transformations). "We do not support arbitrary in-flight transformations"; limited user-configurable in-flight transformation (row filtering, custom data type mapping).
- Shared responsibility model: vendor designs/builds/operates/maintains extract-load and maintains the canonical schema; customer owns queries/models in the destination.
- Automatic type mapping/inference with a data-type hierarchy; type change handled via lossless promotion (column rebuild pattern described).
- Sync mechanics: **incremental sync cursors**, **data checkpoints** (restart from last checkpoint on failure), **re-sync** (invalidate cursors, re-fetch all records, overwrite).
- No visual pipeline canvas: setup is configuration-driven. Philosphy is automation-first ("fragile ETL pipelines" framed as the past).
- Custom connectors via Connector SDK (Python).
- Release phases for connectors (private preview → public preview → beta → GA → sunset). Usage-based pricing (Monthly Active Rows) — vendor-specific, not asserted in final doc.

### Airbyte (evidence layer A)

Observations from /platform and core-concepts:

- Self-label: "open source **data replication platform**"; tagline "simple, secure and extensible **data integration**". Both labels used for one product — direct evidence that market labels drift across the movement-family leaves.
- Core objects (defined on the Core Concepts page): **Source** (configured API/file/database/warehouse to ingest from), **Destination** (warehouse/lake/database/analytics tool to load to), **Connector** (component pulling from a source or pushing to a destination), **Connection** ("an automated data pipeline that replicates data from a source to a destination" — links configured source to configured destination), **Stream** (group of related records; generalized table/file/endpoint), **Record**, **Field**, **Sync Schedule** (scheduled / CRON / manual "Sync Now"), **Destination Namespace** (generalized schema/dataset/bucket), **Delivery Method** (typed record replication vs raw file copy), **Sync Mode** (governs read/write behavior; duplicates question), **Resumability** (checkpoint progress, automatic re-attempt), **Typing and Deduping**, **Custom Transformations** (dbt post-sync, cloud), **Workspace**, **Organization**.
- Connection configuration parameters: stream/field selection, sync mode, sync schedule, namespace/prefix, schema propagation (schema drift policy).
- 600+ pre-built connectors; long-tail coverage via No-Code Connector Builder; connector development in code; community marketplace.
- Interfaces: UI, REST API, Python/Java SDKs, Terraform provider, PyAirbyte library — "manage connectors as infrastructure."
- Own **taxonomy of data movement** table: ELT/ETL ("need all the data… join across datasets… storage") vs **Reverse ETL** ("update content, not trigger side effects"; requires good vendor APIs) vs **Operations Get** ("don't want storage; freshness matters") vs **Operations Write** ("trigger side effects, like sending an email or closing a ticket"). Data replication targets the storage-oriented rows; operations rows are explicitly a different posture. This is vendor-documented support for the dataset-movement vs per-record-operations boundary (→ iPaaS/automation).
- Plans: self-managed OSS (Core), managed cloud tiers, Enterprise Flex (separate data planes for compliance/sovereignty). RBAC/SSO at upper tiers.
- Also markets an agents/context-layer product line (AI era) — noted as vendor drift, excluded from canonical core.

### Matillion ETL (evidence layer A — docs structure)

Observations from docs.matillion.com/metl information architecture:

- Product framed around **Jobs** built on a visual canvas from **Components**. Two job families: **Orchestration** jobs (flow control: Start, If, And/Or, Retry, Iterator components, Run Transformation, transactions Begin/Commit/Rollback, messaging/webhook components, scripting Bash/Python/dbt commands) and **Transformation** jobs (Read: Table Input, Fixed Flow, Wildcard; Transform: Join, Aggregate, Calculator, Filter, Pivot/Unpivot, Window Calculation, Rank, Flatten, Convert Type, SQL component; Write: Table Output/Rewrite/Update, Create View).
- **Connectors / Query components** as a large library (Salesforce, SAP ODP, Workday, NetSuite, ServiceNow, Stripe, Shopify, Zendesk, JDBC Database Query, S3/Azure/GCS Load/Unload, API Query/Extract profiles…). API Profiles machinery for custom REST sources (pagination, parameters, authentication).
- **Environments** (per cloud data platform: Snowflake, Redshift, Delta Lake on Databricks, BigQuery, Azure Synapse), **Variables** (job/environment/grid), **Manage Schedules**, **Task History**, **Task management**, **Performance monitor**, **Job concurrency**, **Shared Jobs**, **Versions**, **Git integration**, **Import-Export**, **Recycle Bin**, **Audit log**, **Groups and Permissions**, **Manage Credentials/Passwords/Secret managers**.
- **CDC** present as a module (Manage CDC, configure source database for CDC, CDC shared jobs) — CDC is a feature inside the integration platform, not the platform's center.
- Projects are bound to a cloud data platform; transformation executes via pushdown (components generate platform-native processing — e.g., DDL components, warehouse-specific components). Instance-based deployment via cloud marketplaces; editions; HA cluster; backups.
- Newer "Maia" (formerly Data Productivity Cloud) line exists alongside Matillion ETL — brand/product evolution noted, not asserted in final doc.

### Apache NiFi (evidence layer A)

Observations from the NiFi overview document:

- Self-description: "automate the flow of data between systems… the automated and managed flow of information between systems." Problem framing is Enterprise Integration Patterns: systems fail, sources outpace consumers, boundary conditions, changing priorities, security/compliance.
- Core concepts (Flow-Based Programming mapping): **FlowFile** (each object moving through the system: attributes + content), **Processor** (performs work — routing, transformation, mediation), **Connection** (bounded queue between processors; prioritization; back pressure), **Flow Controller** (scheduler/broker), **Process Group** (composable sub-flows with input/output ports).
- Architecture: web server (command & control API), FlowFile repository (persistent WAL), content repository, provenance repository — **guaranteed delivery** as a core philosophy; **data provenance** recorded/indexed/searchable; click-to-content download and **replay** at a lifecycle point.
- Visual command and control in the browser: real-time modification of running flows ("molding clay", not design-then-deploy); flow templates for reuse.
- Back pressure, prioritized queuing, per-flow QoS (latency vs throughput, loss tolerance); multi-tenant authorization (read-only / dataflow manager / admin levels); 2-way SSL; sensitive property encryption.
- Extensibility (processors, controller services, prioritizers); Site-to-Site protocol between instances; clustering (zero-leader, ZooKeeper-coordinated); MiNiFi for edge collection.
- NiFi is continuous/queued (not schedule-centric) and general-purpose routing/mediation rather than warehouse-ELT-shaped. It still satisfies the pipeline + connectors + execution/monitoring center — with the pipeline modeled as a directed graph of processors.

### Informatica — IDMC Data Integration and Engineering (evidence layer A, product-page level)

Observations from the product page:

- Positioning: "Ingest, integrate and cleanse your data with a data engineering solution optimized for analytics and AI"; part of the IDMC suite alongside Data Catalog, API & App Integration, Data Quality, MDM, Governance, Data Marketplace.
- Scope claims: "a single platform for virtually all integration patterns, including ELT"; "Ingest data with high-performance ELT/ETL, data replication or change data capture" (CDC/replication via Cloud Mass Ingestion); ETL, ELT, Spark, or fully managed serverless execution options.
- Design posture: AI-powered low-code/no-code tools; operational insights into "the health of your data at virtually every stage of the pipeline"; hundreds of connectors; consumption-based pricing (figure claims discarded as marketing).
- Suite context confirms the pole: integration is one service of a broader data-management cloud (mirrors the data-fabric pass's observation about suite bundles).

### SQL Server Integration Services (evidence layer A — historical/platform-embedded check)

Observations from Microsoft Learn overview:

- "A platform for building enterprise-level data integration and data transformations solutions." Use cases: copy/download files, load data warehouses, cleanse and mine data, manage SQL Server objects.
- Capabilities: extract and transform data from a wide variety of sources (XML data files, flat files, relational sources) and load into one or more destinations; built-in **tasks** and **transformations**; **graphical tools for building packages**; an **SSIS Catalog database to store, run, and manage packages**; solutions can be built without code or programmed via the object model.
- Structure confirms the same center in the designer era: connections to external sources/destinations, persistent packages (pipelines), execution/management machinery (catalog), transformation-centric design. No prebuilt SaaS connector automation, no managed ELT — those are modern additions, not definitional.

## Cross-product Comparison

| Aspect | Fivetran | Airbyte | Matillion ETL | Apache NiFi | Informatica (page-level) | SSIS |
|---|---|---|---|---|---|---|
| Pipeline unit | connector/connection (config) | connection (source+destination+sync config) | job (orchestration + transformation, canvas) | flow (directed graph of processors) | mapping/task (page-level) | package (designer) |
| Connectors to external systems | 700+ marketed; connector + destination libraries | 600+ prebuilt + builder + SDK | connector/query component library + API profiles | 100s of processors; protocol-level connectivity | "hundreds of connections" | built-in tasks/transformations; wide source types |
| Design surface | setup wizard / config | UI wizard + no-code builder + API/Terraform/PyAirbyte | visual canvas (components) | visual canvas, real-time editing | low/no-code (AI-assisted) | graphical designer + object model |
| Transformation depth | minimal in-flight; post-load in destination (dbt) | minimal in-flight; post-load (dbt, cloud) | rich in-platform pushdown components | processors on FlowFiles (routing/mediation/transform) | rich (ETL/ELT/Spark) | rich (tasks + transformations engine) |
| Execution trigger | managed schedules; incremental | scheduled / CRON / manual | schedules; orchestration jobs; webhooks/queues | continuous, queue-driven; real-time editing | managed (serverless or runtime) | catalog run; scheduled via platform tooling |
| Movement mechanics | incremental cursors + checkpoints; re-sync | sync modes (full/incremental/CDC); resumability | pushdown jobs; incremental load tools; CDC module | queued FlowFiles, back pressure, guaranteed delivery | ELT/ETL + replication + CDC | package execution |
| Run visibility | logs, dashboard | run history / monitoring | task history, performance monitor | provenance repository (searchable lineage, replay) | operational insights (pipeline health) | SSIS Catalog (store/run/manage) |
| Data ownership | none (sources/destinations own data) | none | none (executes on warehouse compute) | stages content in own repositories transiently | none | none (data stays in SQL Server/destinations) |
| Schema-drift handling | automatic type promotion/rebuild | schema propagation policies | platform-specific; manual tooling | processor-level | page-level claim | manual (designer era) |
| Roles/permissions | account/team levels | workspaces/orgs; RBAC/SSO upper tiers | groups and permissions, users, audit | multi-tenant authorization levels | enterprise suite | platform security |

Cross-product commonalities (evidence layer B):

1. Every product manages **connections to external systems** on at least a source side, almost always a destination side.
2. Every product keeps a **persistent, named, re-runnable unit of data movement** (connection / connection / job / flow / mapping / package). Nothing in the sample treats a pipeline as a one-shot throwaway.
3. Every product **executes** those units and exposes **run visibility** (logs/history/provenance/insights).
4. Every product holds **credentials** as managed configuration objects.
5. Every product offers **selection** of what moves (tables/streams/objects/columns) and **mapping** into destination naming/structure.
6. Transformation presence is universal, **depth** is not: two products push transformation out of the platform; three make it the design center.
7. Scheduling/triggering exists everywhere; the *model* differs (managed schedules vs continuous queues vs catalog-run packages).
8. Failure handling exists everywhere; the modern pair automatizes it (checkpoints/cursors/resumability), the designer era left it to the package author.

## Abstraction Levels

### L0 — Defining Invariant

The Data Integration Platform is recognizable as such when all three of these hold:

1. **Connections to external data systems the platform does not own.** Source systems (databases, SaaS applications, files, event systems) it reads from, and destination systems it writes to. The platform is not the system of record for the data; it is the mover. Without this, the product is a transformation engine, a query tool, or an SDK — not an integration platform.
2. **The pipeline as a persistent configured unit of movement.** A named, kept, editable data flow from source(s) to destination(s), specifying what data moves, how it is mapped/selected, and how it lands. The pipeline's content is data *moving between systems* (physical movement posture). Remove persistence → one-shot migration tooling; remove movement (unified logical view without copying) → data virtualization.
3. **Managed execution with run visibility.** The platform runs pipelines (scheduled, manual, event-triggered, or continuous) and records outcomes — status, history, logs or equivalent — so an operator can see and diagnose what happened. Remove this → a design tool or framework, not an operating platform.

Test against §24 (historical check): SSIS (2005-era, still current) satisfies all three — connections, packages, catalog-run execution with management. A 1990s-era scheduler-driven ETL tool satisfies all three. The definition does not depend on cloud, ELT, managed connectors, or visual canvases.

### L1 — Common Mature Structure

Present in most mature modern products (B-level evidence):

- Connector catalog spanning databases, SaaS/business applications, files/object storage, warehouses/lakes; separate source and destination connector types; SDK/no-code builder for custom connectors
- Initial historical load (backfill/snapshot) followed by ongoing sync; re-sync/replay machinery
- Sync modes: full refresh vs incremental (cursor/watermark-based); CDC-based sync; append vs upsert/merge write behavior
- Checkpointing/resumability, automatic retry; re-sync when incremental continuity breaks
- Schema-change handling (drift policies, type mapping/inference, naming conventions)
- Monitoring surfaces: run history, task/job status, logs, alerts; increasingly lineage/provenance
- Scheduling machinery (intervals, CRON, manual runs); programmatic control (API/CLI/Terraform/SDK)
- Transformation layer in some form (see L2 for where it lives)
- Team/organization structure: workspaces/projects/environments, roles and permissions, audit, credential/secret management
- Git/version-control integration and import/export of pipeline definitions (designer-era and modern)

### L2 — Variant / Optional Structure

Depends on segment, era, deployment, workflow:

- Technique emphasis: batch ELT into warehouses/lakes vs log-based CDC vs continuous streaming/dataflow vs designer-era batch ETL
- Where transformation happens: post-load in destination (ELT philosophy) vs in-platform pushdown components vs in-platform engine vs minimal routing/mediation only
- Design surface: configuration wizards vs visual canvas vs code/API/infrastructure-as-code
- Direction of movement: toward the analytical estate (ELT) vs outward activation (reverse ETL) vs system-to-system routing
- Deployment: fully managed SaaS vs self-hosted OSS vs hybrid data planes vs platform-embedded (SSIS inside SQL Server; suite service inside IDMC)
- Destination focus: warehouse/lake-centric vs general system-to-system
- Scale-out architecture, clustering, edge collection (NiFi-class), serverless execution (Informatica-class)
- AI-era additions: context layers for agents, AI-assisted design (era-typical; not definitional)

### L3 — Vendor-specific Structure

Stays in Research Notes only:

- Fivetran: Monthly Active Rows usage pricing; release phases (private preview→GA→sunset); canonical-schema shared-responsibility model; Managed Data Lake Service; Context Layer; HVR line
- Airbyte: plan ladder (Core/Standard/Plus/Pro/Enterprise Flex); PyAirbyte; connector builder UI + marketplace; agents/context product line; its published taxonomy-of-data-movement table
- Matillion: Maia / Data Productivity Cloud line; Maia Foundation binding; shared jobs; queue messaging components; marketplace instance editions
- NiFi: FlowFile/provenance internals; Site-to-Site protocol; MiNiFi; ZooKeeper cluster coordination
- Informatica: CLAIRE AI; IDMC service catalog; Mass Ingestion; Headless Data Management; consumption pricing; TCO/time marketing figures

## Rejected Findings

- **"Data integration platform = ETL/ELT tool"** — rejected as the definition; ETL/ELT is one technique emphasis inside a broader pipeline platform. The transformation-first reading overfits the designer era and the warehouse-ELT era simultaneously.
- **"Transformation is definitional"** — rejected. Fivetran explicitly does not support arbitrary in-flight transformations; the platform remains squarely an integration platform. Mapping/selection is definitional; transformation depth is not.
- **"Visual canvas / low-code designer is definitional"** — rejected. Fivetran has no canvas; NiFi and Matillion and SSIS are canvas-centric. The design surface is an L2 axis.
- **"CDC is a differentiator from the family"** — rejected; CDC appears as a sync mechanism inside Matillion and Informatica (and as sync mode in Airbyte/Fivetran). CDC's *contract* (event stream delivery) is the CDC Type's center, not the integration platform's.
- **"The platform owns/stores the data"** — rejected. Across the sample, data at rest belongs to sources/destinations. NiFi's transient content staging and Fivetran's in-flight staging do not make any sampled platform the system of record.
- **"Reverse ETL is part of the definition"** — rejected as definitional; it is an optional direction some platforms add (Airbyte markets it; Fivetran ships an "Activations" section — product-specific evidence, treated as optional extension).
- **Marketing figures** (Informatica TCO/time claims, connector counts as quality claims) — discarded; connector-count numbers recorded only as catalog-breadth evidence, not asserted in the final document.

## Boundary Findings

Against the §13 sibling cluster:

- **vs ETL/ELT Platform (unprocessed leaf)**: the population overlaps almost completely. Market labels drift (Airbyte: "data replication platform" + "data integration"; Informatica: integration patterns including ELT; Fivetran defines itself against "ETL software vendors"). Proposed standing split for the future ETL/ELT pass: either treat ETL/ELT as the technique-defined slice (transformation job as managed object) with the integration platform as the pipeline-management platform spanning techniques — or as alias/variant. **Recorded as taxonomy issue; joint review recommended.**
- **vs Change Data Capture Platform (processed)**: CDC's managed object is the ordered change-event stream with resumable capture position; the integration platform's managed object is the pipeline. CDC machinery appears inside integration platforms as one sync mechanism. Boundary held; consistent with the CDC pass's wording.
- **vs Data Replication Platform (unprocessed)**: replication promises a synchronized target *copy* (state contract); integration promises managed pipelines (flow contract). Same machinery, different promise — consistent with the CDC pass's recorded split. Airbyte self-labels as replication while behaving as a pipeline platform — evidence that these leaves share one population; joint review recommended at the replication pass.
- **vs Reverse ETL Platform (unprocessed)**: reverse ETL's defining direction is warehouse → operational/SaaS tools with content updates; some integration platforms include it as an outward-facing capability. Distinct managed direction; joint review recommended.
- **vs Data Virtualization Platform (unprocessed)**: virtualization = query-time logical access, no physical copy; integration = physical movement between systems. Both connect systems; only one copies data. Consistent with the fabric pass's ratified split.
- **vs Data Fabric Platform (processed)**: fabric = estate-spanning unified metadata/governance layer with integration as one function; integration platform = pipeline building/running as the center. DISCHARGES the fabric pass's cross-check request from this side.
- **vs Data Exchange Platform (processed)**: exchange = inter-org dataset offerings with entitlements/delivery; integration = intra-org pipeline machinery. DISCHARGES the exchange pass's cross-check request from this side.
- **vs Workflow automation / iPaaS (directory §03.16 / §10)**: dataset-level bulk sync without business side effects vs record/event-level operations that trigger actions (send email, close ticket). Airbyte's own docs draw exactly this line ("update content, not trigger side effects" vs "trigger side effects"). This is vendor-documented support for the Type boundary.
- **vs Managed File Transfer (unprocessed)**: MFT's managed object is the transfer event (file movement with transfer semantics); integration pipelines may carry files, but the managed object remains the pipeline. Overlap when files are the medium; note for the MFT pass.
- **vs Data Warehouse / Lakehouse Platforms (unprocessed)**: destination platforms own storage + compute; the integration platform owns neither. The integration platform is the connector *into* them. Boundary clear in all sampled products.
- **vs Database migration tooling (no leaf)**: one-shot cutover vs standing pipeline. A standing pipeline is definitional (L0-2); one-shot movement tools do not fit the Type.
- **vs API & Application Integration / iPaaS suites (Informatica ships a separate "API & App Integration" service)**: the market itself separates data-integration (dataset movement) from application-integration (process/API mediation) inside one suite — supporting evidence that the two are distinct Types.

Remove-tests for the canonical document:

- Remove connectors → transformation engine / SQL SDK (not integration)
- Remove pipeline persistence → one-shot migration service
- Remove managed execution/monitoring → pipeline design tool / library
- Remove movement (keep logical view) → data virtualization
- Shift managed object to estate-wide metadata/governance → data fabric
- Shift to inter-org entitlement/delivery → data exchange
- Shift to per-record operations with side effects → workflow automation / iPaaS
- Promise ordered change-event delivery instead of managed pipelines → CDC platform
- Promise exact synchronized state copy instead of managed flow → replication platform

## Uncertainties

- Informatica operational mechanics (mapping designer structure, task flows, monitoring objects) unverified — page-level evidence only. Kept out of the canonical document except as the suite pole.
- Matillion's newer Maia/Data Productivity Cloud line not examined; Matillion assertions limited to the Matillion ETL docs structure.
- NiFi's fit is the widest in the sample: it is a general dataflow/routing system (EIP-framed) rather than warehouse-ELT-shaped. It satisfies the L0 (connections, persistent flows, managed execution/monitoring) but its inclusion relies on the overview document; UI-specific behavior not verified.
- Historical depth: SSIS confirms the designer-era pattern; PowerCenter/Kettle/DataStage were not fetched (memory only — not used for assertions). If a future pass needs a deeper historical base, fetch at least one of those.
- Connector-count numbers (700+/600+/hundreds) are vendor claims recorded as catalog-breadth evidence only.

## Final Synthesis

The Data Integration Platform's center is the **pipeline**: a persistent, configured, managed unit that moves data between external systems the platform does not own. Around that center mature products add: connector catalogs on the source and destination sides, selection/mapping, some form of transformation (depth varies by philosophy), scheduling/triggering, checkpoints/retries/re-sync, schema-drift policies, monitoring surfaces, programmatic control, team/permission/credential machinery.

The Type is defined neither by technique (batch vs CDC vs streaming), nor by design surface (wizard vs canvas vs code), nor by transformation depth, nor by era (designer packages and managed ELT satisfy the same core). It is defined by: connections to systems it doesn't own + persistent pipelines carrying data between them + managed execution with run visibility.

The family boundaries (CDC / replication / ETL-ELT / reverse ETL) are contract-and-direction slices over one product population with heavy label drift; this is recorded as a taxonomy issue with joint-review recommendations, not silently resolved here.
