# Research Notes — Data Lineage Platform

Research date: 2026-09-07
Leaf: Data Lineage Platform (DIRECTORY.md §13 Data, Analytics & AI Systems, line 996)

## Research Goal

Understand what a Data Lineage Platform actually is as an Application Type: what its world is made of (the flow graph and its node/edge structure), how the graph gets populated and kept current, what users do with it (trace, impact analysis, root-cause, compliance evidence), which structures are definitional vs. merely common in the current market, and where its boundaries lie against neighboring data-platform Types — especially Data Catalog (the closest sibling, already processed), Metadata Management, Data Observability, ETL/ELT platforms, and Data Governance.

## Initial Boundary

Working hypothesis before research:

- Core purpose: capture and render the graph of how data flows through an organization's data estate — from sources through transformations to consumption — and let users trace it: where did this come from, what breaks if I change this, where did this wrong number come from.
- Likely central object: a navigable graph whose nodes are data assets (tables, files, dashboards, models) and data-moving processes (pipelines, jobs, queries), with edges recording actual flows.
- Likely core loop: capture flows (automatically or manually) → maintain the graph → select a node → traverse upstream/downstream → impact analysis / root-cause → act in the source system.
- Nearest Types: Data Catalog, Metadata Management Platform, Data Observability Platform, ETL/ELT Platform, Data Integration Platform, Data Governance Platform, Diagramming Application.
- Likely confusions: lineage as "one view inside a catalog" vs. lineage as the product; lineage vs. data observability (both serve debugging); lineage vs. ETL-tool-native dependency views.
- Market-structure hypothesis: dedicated standalone lineage vendors have been consolidating into platforms (Manta → IBM; Octopai → data.world → Cloudera), so the Type's market realization is mostly embedded — needs confirmation.

## Research Questions

1. What exactly is the central object — a graph over what entities? What sits on nodes, what sits on edges?
2. How is lineage captured? (SQL/query-log parsing, runtime event collection, platform instrumentation, code/ETL/BI harvesting, manual curation)
3. What granularity exists (asset-level vs column-level; data nodes vs process nodes)?
4. What operations does the graph support (upstream/downstream traversal, impact analysis, root-cause, search, filtering, time ranges)?
5. Is there a time/history dimension (lineage as of a date, retention windows, run history, versioned lineage)?
6. How do permissions interact with the graph (can users see flows through assets they can't access)?
7. What programmatic surfaces exist (lineage APIs, system tables, event standards like OpenLineage)?
8. Which capabilities are definitional, and which are common-but-not-definitional or optional?
9. What breaks the boundary toward neighboring Types?
10. How is the Type packaged in the 2026 market (standalone vs embedded)?

## Representative Products

Selected for market representation, documentation quality, distinct product philosophies, and distinct customer tiers:

| Product | Philosophy / position | Tier |
|---|---|---|
| Marquez | open-source lineage platform; reference implementation of the OpenLineage event standard; runtime event collection | OSS / engineering teams |
| Microsoft Fabric (lineage view + impact analysis) | hyperscaler platform-bundled lineage; workspace-scoped graph inside a catalog/governance surface | Microsoft estates |
| OpenMetadata (lineage) | unified metadata platform where lineage is a flagship capability; query-log parsing + dbt + manual curation | OSS to enterprise |
| Cloudera Data Lineage (formerly Octopai) | dedicated automated-lineage vendor (absorbed into Cloudera's data fabric); harvests sources/ETL/scripts/BI across hybrid estates | large enterprise |
| Databricks Unity Catalog lineage | platform-native lineage captured automatically at query time inside the lakehouse; extended by external-lineage registration | Databricks estates |

Note: IBM Manta — the archetypal dedicated lineage vendor — was selected first but could not be researched (see Sources). Cloudera Data Lineage (formerly Octopai) stands in for the dedicated-vendor pole; both share the same automated-harvesting philosophy.

## Sources

Tier 1/2 official surfaces fetched 2026-09-07:

- Marquez
  - https://marquezproject.ai/ (project home: positioning, OpenLineage framing, UI/API description)
  - https://marquezproject.ai/docs/quickstart (data model: jobs/datasets/runs, metadata versioning, run states, UI walkthrough)
  - https://marquezproject.ai/docs/faq (thin; only logging config)
- Microsoft Fabric
  - https://learn.microsoft.com/en-us/fabric/governance/lineage (lineage view: scope, permissions, cards, highlight, zoom)
  - https://learn.microsoft.com/en-us/fabric/governance/impact-analysis (impact pane: direct children vs all downstream, notify contacts, privacy)
- OpenMetadata
  - https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage (overview)
  - https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/explore (lineage view, edge details, layers)
  - https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/workflow (capture machinery: view parsing, Lineage Agent, YAML workflow, dbt, CSV fallback, manual)
  - https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage/column (column-level lineage, manual editing)
- Cloudera Data Lineage (formerly Octopai)
  - https://octopai.com/ (redirects to Cloudera product page: positioning, features, integrations, user framing) — Tier 2 only; operational docs not fetched
- Databricks
  - https://docs.databricks.com/data-governance/unity-catalog/data-lineage (automatic capture, column level, external lineage, system tables, permissions, retention, limitations)
  - https://docs.databricks.com/llms.txt (used to locate the lineage doc URL)
- OpenLineage (ecosystem context)
  - https://openlineage.io/ (open framework for lineage collection; standard event API; datasets/jobs/runs)

Blocked sources (recorded per source-access limitation rules):

- IBM Manta: https://www.ibm.com/docs/en/manta → HTTP 403; https://www.manta.com/ → HTTP 403; https://docs.manta.com/ → transport error. Abandoned after the allowed retries. No Manta-specific claims are made anywhere in this research.
- Cloudera operational documentation (docs.cloudera.com) not attempted beyond the product page; all Cloudera/Octopai claims are product-page strength.

Evidence layers: A = directly observed on the cited official page; B = cross-product commonality; C = canonical inference.

## Product A — Marquez

### Key observations (Layer A unless noted)

- Positioning: "The complete OpenLineage solution" — consuming, storing, and visualizing OpenLineage metadata from across an organization, "serving use cases including data governance, data quality monitoring, and performance analytics."
- Three-part framing: (1) real-time metadata server with an OpenLineage-compatible endpoint for "real-time collection of information from running jobs and applications"; (2) unified visual graph — a web UI showing "complex interdependencies within your data ecosystem," browse metadata, "see the inputs and outputs of each job, trace the lineage of individual datasets, and study performance metrics and execution details"; (3) flexible Lineage API — "metadata can be queried for automation of key tasks like backfills and root cause analysis… traverse the dependency tree and establish context for datasets across multiple pipelines and orchestration platforms. This can be used to enrich data catalogs and data quality systems."
- Reference implementation of OpenLineage; works with community integrations: Apache Airflow, Apache Spark, Apache Flink, dbt, Dagster.
- Data model (quickstart): a centralized, normalized model of end-to-end pipeline metadata "composed of multiple jobs" with built-in metadata versioning; enables "highly flexible data lineage queries across all datasets" and associates (upstream, downstream) dependencies between jobs and the datasets they produce and consume.
- Run-level metadata is tracked via HTTP calls to `/lineage` using OpenLineage. A run has a unique ID and records code version, inputs and outputs, run args, and run state transitions. When a run completes, its output datasets are created if not already registered.
- Dataset versioning: each input/output dataset carries a version pointer; each immutable dataset version is mapped to the metadata change and the run ID that modified it — "preserving its state at some given point in time." Job version pointers map to a code link, the latest run ID, and versioned inputs/outputs.
- History use: "query the history of schema changes for a given dataset and compare a previous schema version with the latest… especially useful for auditing or troubleshooting impacted jobs downstream of a schema change."
- UI: search bar (search a job by name from a drop-down); job page shows namespace, name, query, and a run-history tab; dataset page shows name, schema, description.

## Product B — Microsoft Fabric lineage

### Key observations

- Problem framing: "understanding the flow of data from the data source to its destination can be a challenge… Questions like 'What happens if I change this data?' or 'Why isn't this report up to date?' can be hard to answer."
- Lineage view: "you see the lineage relationships between all the items in a workspace, as well as data sources external to the workspace one-step upstream." "Every workspace automatically has a lineage view" — no setup; the graph is derived from the platform's own item relationships.
- Scope: downstream items in different workspaces are not shown in lineage view; cross-workspace downstream exploration is the job of the separate impact-analysis surface.
- Permissions: any user with a workspace role can access that workspace's lineage view; Viewer-role users don't see data sources.
- Entry points: workspace toolbar, an item's option menu (e.g., in the OneLake catalog), an item's details page.
- Rendering: items as cards with identifying info; data-source cards show connection-identifying info (e.g., server + database name for Azure SQL). Highlight one item's lineage (related items highlighted, rest dimmed); interactive canvas with zoom and full screen; keyboard/screen-reader accessibility following a DFS traversal of the graph.
- Impact analysis (separate pane): "shows you the workspaces and Fabric items that might be affected by your change"; tabs for direct children vs. all downstream items; browse affected items by type or by workspace; "Notify contacts" sends an email to the contact lists of all impacted workspaces; for data sources, shows the connection string; permission-aware — items the user can't access are listed as "Limited access" without names (privacy).
- Caveat documented by the vendor: correct display of semantic-model ↔ dataflow lineage is guaranteed only when a specific connection method is used — capture coverage has known conditions.

## Product C — OpenMetadata lineage

### Key observations

- Framing: "OpenMetadata tracks data lineage, showing how data moves through the organization's systems. Users can visualize how data is transformed and where it is used, helping with data traceability and impact analysis." Lineage supported for Database, Dashboard, and Pipelines.
- Explore: "end-to-end lineage traceability for the table and column levels. Just search for a data asset and expand the graph to unfold lineage… upstreams and downstreams edges for each node." Edge details: "the Source, Target, Description, and SQL Query… The SQL query provides information on how the target table was generated from the source table."
- Lineage Config: display up to 3 upstream and downstream nodes per layer (display-depth control).
- Asset quick view from the graph: source, name, description, owner, tier, usage; type-specific info (table type, query count, columns); data-quality/profiler metrics (tests passed/aborted/failed); tags; schema.
- Capture machinery (workflow page):
  - View lineage from metadata ingestion: views' generating queries are parsed during metadata ingestion; source/target tables resolved against the catalog; lineage relationships created, including column-level lineage for views.
  - Lineage Agent (UI-configured): "obtain the query log and table creation information from the underlying database and feed it to OpenMetadata." Options: Query Log Duration (days of lookback), Parsing Timeout Limit (seconds), Result Limit (max query-log rows per batch), Filter Condition (SQL filter on query history), Process Cross Database Lineage toggle + Cross Database Service Names (resolve table references across services).
  - External YAML workflow (`DatabaseLineage`): toggles for processViewLineage / processQueryLineage / processStoredProcedureLineage; overrideViewLineage; threads; database/schema/table regex filter patterns; optional queryLogFilePath to feed queries from a file.
  - dbt ingestion: "can fetch queries that carry lineage information… We also fetch the column level lineage through dbt."
  - CSV fallback: for unsupported connectors, lineage workflows can run over query logs supplied in a CSV file.
  - Manual lineage: "Lineage can also be added and edited manually" — table and column level; anchor points on columns to create links; add new tables into the trace.
- Lineage layers (explore page): Column layer (trace specific fields across tables/pipelines); Observability layer (test outcomes — passes/failures/pending — displayed in lineage); Service layer (flows across platforms: Hive, Redshift, Power BI, Tableau — "system-level view of the end-to-end data journey"); Domain layer (business categories); Data Product layer (curated consumption-ready outputs).
- Pipeline lineage: when setting up pipeline ingestion, the database service name is specified, connecting pipeline nodes to database tables; dashboard ingestion connects data models/charts to database tables.

## Product D — Cloudera Data Lineage (formerly Octopai)

### Key observations (product-page strength — Tier 2)

- Positioning: "Metadata management and automated data lineage for enterprise data estates"; "the only SaaS-based solution built to navigate the most complex cloud, on-premises, and hybrid data environments instantly and automatically."
- Value framing: "Harvest every data source, ETL process, script, and BI report automatically (without manual tagging), delivering a complete, up-to-date lineage graph." "Empower technical data teams and business users to trace any issue back to its origin or assess the impact of an upcoming change in seconds." "Give IT and business users interactive lineage diagrams, audit trails, and data-quality metrics, providing evidence for governance and regulatory audits."
- Key features listed: automated metadata harvesting; automated data lineage mapping; data discoverability; deep, multi-layered lineage; hybrid compatibility & multi-dimensional lineage; inferred lineage & augmented links ("fill gaps with inferred relationships").
- Coverage: "more than 60 native integrations and support for non-native systems through the Custom Lineage Connector"; "cross-system, intra-system, and granular lineage"; integration logos span databases (Oracle, Teradata, Redshift), processing (Spark, PySpark, dbt, Impala, Iceberg, Kubernetes), BI (Tableau), ML (TensorFlow, Jupyter, MLOps), Databricks.
- Technical-user framing: trace failures/bottlenecks; eliminate redundant processes and data copies; enforce consistent quality rules across pipelines; accelerate data-product delivery; preserve full audit trails for compliance.
- Business-user framing: trust the numbers; reduce "black box" concerns; trace key metrics to foundational data sources; investigate upstream factors behind KPI changes.
- Vendor-cited survey stats (Dataversity/Octopai 2023 — kept here, not promoted): 50% spend >5h/week tracing data flows; 75% wait weeks to find the source of an error; 90% of manual work saved in impact analysis.

## Product E — Databricks Unity Catalog lineage

### Key observations

- Definition: "Data lineage shows where data in Databricks came from and where it goes: which queries and files populate a table, which jobs and notebooks transform it, and which dashboards consume the results."
- Capture: "Unity Catalog captures lineage automatically for queries run on Databricks, down to the column level, and aggregates it across all workspaces attached to the metastore."
- Named use cases: impact analysis ("before changing or deleting a table or column, identify the downstream tables, jobs, and dashboards that depend on it"); investigate root causes ("when a downstream report shows unexpected results, trace upstream sources"); track sensitive data flow ("for compliance audits, see where regulated data originates, how it is transformed, and which downstream assets consume it"); understand cross-team dependencies.
- Graph contents: nodes represent tables and views, ML model versions, external assets, and file paths; model-API/provider lineage appears "as nodes in the same lineage graph as your tables."
- External lineage: "Register upstream sources like Salesforce or MySQL and downstream tools like Tableau or Power BI as external assets in Unity Catalog, and they appear alongside your Unity Catalog tables in a single graph."
- Catalog Explorer flow: table → Lineage tab → related tables panel → "See Lineage Graph"; one level displayed by default, expand nodes for more; click an edge → Lineage details panel (source/target tables); filter associated assets by notebooks/jobs/pipelines/queries; click a column → column-level links.
- Job/dashboard lineage: from a table's Lineage tab, list downstream jobs / dashboards as consumers.
- Natural-language access: Genie Code answers lineage questions (`/getTableLineages` — "show me downstream lineages", "who queries this table most often").
- Programmatic access: lineage system tables (`system.access.table_lineage`, `system.access.column_lineage`) for SQL queries over lineage data; rolling 1-year retention in system tables.
- Permissions: lineage shares the Unity Catalog permission model; `BROWSE` privilege required; objects the user can't access appear as masked nodes that cannot be expanded; workspace-object details (notebooks, dashboards) visible only in their own workspace.
- Retention/time: Catalog Explorer lineage retained indefinitely; all lineage captured after Sep 1, 2024 available; time-range dropdown (default 1 year; "All time" for newer metastores).
- Documented capture limitations: renames not preserved; RDDs and global temp views not captured; UDFs can obscure column mapping; path-referenced tables lack column lineage; transactions emit lineage even when rolled back; Spark checkpointing not captured.

## Ecosystem context — OpenLineage

- "An open framework for data lineage collection and analysis… an open standard for lineage data collection, libraries for common languages, and integrations with data pipeline tools."
- "At the core of OpenLineage is a standard API for capturing lineage events. Pipeline components — like schedulers, warehouses, analysis tools, and SQL engines — can use this API to send data about runs, jobs, and datasets to a compatible OpenLineage backend."
- Tracks "metadata about datasets, jobs, and runs, giving users the information required to identify the root cause of complex issues and understand the impact of changes."

## Cross-product Comparison

| Dimension | Marquez | Microsoft Fabric | OpenMetadata | Cloudera Data Lineage (Octopai) | Databricks UC | Strength |
|---|---|---|---|---|---|---|
| Flow graph: nodes = data assets, edges = actual flows | A (datasets + jobs; upstream/downstream dependencies) | A (items + data sources connected) | A (tables/dashboards/pipelines; edges) | A ("map data flows across systems") | A (tables/views/models/external assets/file paths) | B — universal |
| Process/job nodes alongside data nodes | A (jobs first-class, with run history) | A (items include pipelines/dataflows) | A (pipelines; dashboards) | A (ETL processes, scripts, BI reports) | A (jobs/notebooks/queries as associated assets) | B — universal |
| Automatic capture machinery | A (OpenLineage events from running jobs) | A (auto-derived workspace graph) | A (query-log parsing agent, view parsing, dbt) | A (harvests sources/ETL/scripts/BI "without manual tagging") | A (captured automatically at query time) | B — universal in modern products; mechanism varies |
| Manual lineage editing | (not on fetched pages) | (not on fetched pages) | A (table + column level, anchor-point editing) | (positioned as automated; "without manual tagging") | (not on fetched pages) | B — common-optional |
| Column-level lineage | (not confirmed on fetched pages) | (not on fetched pages; item-level view) | A (rich column-level; layers) | A ("granular lineage") | A ("down to the column level… as much as possible") | B — common, not universal |
| Upstream/downstream traversal from a node | A (trace lineage of datasets; dependency tree) | A (highlight lineage; one-step upstream) | A (expand graph; upstream/downstream edges) | A (trace any issue back to origin) | A (expand nodes; upstream/downstream) | B — universal |
| Impact analysis as a named capability | (implied via lineage API automation) | A (dedicated pane; direct children vs all downstream; notify contacts) | A (named purpose) | A (named; "assess the impact of an upcoming change") | A (named use case) | B — universal |
| Root-cause / troubleshooting framing | A ("root cause analysis" via Lineage API) | A ("Why isn't this report up to date?") | (debugging implied) | A ("trace any issue back to its origin") | A (named use case) | B — universal |
| Search/browse entry point into the graph | A (search bar for jobs) | (workspace-scoped view; entry from item menus) | A (search asset, expand graph) | A (data discoverability) | A (search/browse table → Lineage tab) | B — universal (form varies) |
| Edge details (the transformation behind an edge) | A (job query shown) | (cards; not edge-level on fetched page) | A (SQL query on edge) | (implied by "analyzing transformations") | A (Lineage details panel: source/target) | B — common |
| Time dimension (history/retention/time ranges) | A (run history; dataset/job versions; schema-change history) | (not on fetched pages) | (not on fetched pages) | A (audit trails) | A (time-range dropdown; retention windows; system tables 1-year rolling) | B — common, depth varies |
| Permission-aware graph visibility | (not on fetched pages) | A (Viewer role limits; limited-access items unnamed) | (roles exist; lineage-specific behavior not on fetched pages) | (not on fetched pages) | A (BROWSE privilege; masked nodes) | B — common |
| Programmatic access (API/system tables) | A (Lineage API for traversal/automation) | (not on fetched pages) | A (YAML workflows; APIs from prior pass) | (Custom Lineage Connector is inbound; API not on fetched page) | A (lineage system tables) | B — common |
| BI/dashboard lineage | (not on fetched pages) | A (native items) | A (dashboards/charts connected to tables) | A (BI reports harvested) | A (dashboards; external Tableau/Power BI) | B — common |
| Cross-system span | A (multi-pipeline, multi-orchestrator) | (workspace-scoped + one-step external upstream) | A (cross-database lineage; service layer) | A (cross-system, hybrid cloud/on-prem) | A via external-lineage registration (native graph is platform-scoped) | B — typical, realization varies |
| Data-quality overlay on the graph | (positioning mentions DQ use case) | (not on fetched pages) | A (observability layer: test outcomes in lineage) | A (data-quality metrics alongside diagrams) | (not on fetched pages) | B — common-optional |
| AI/ML model lineage | (not on fetched pages) | (not on fetched pages) | A (ML models as lineage asset type) | A (TensorFlow/MLOps integrations listed) | A (model versions as nodes) | B — emerging |
| Natural-language lineage Q&A | (not on fetched pages) | (not on fetched pages) | (not on fetched pages) | (not on fetched pages) | A (Genie Code /getTableLineages) | single-product direct (A) |
| Compliance/audit framing | A (auditing schema changes) | (not explicit on fetched pages) | (not on fetched pages) | A (evidence for governance and regulatory audits) | A (sensitive-data flow tracking) | B — common |

## Canonical Abstraction (for synthesis only — not for final doc)

### L0 — Defining Invariant (deliberately minimal)

1. **The data-flow graph as the object of record** — a maintained graph whose nodes stand for data assets (tables, files, dashboards, models, topics…) and the processes that move or transform data (pipelines, jobs, queries, scripts), living in systems whose data the platform does not hold; edges record how data actually flows from source to target. The platform holds metadata about flows, never the data itself.
2. **Trace operations on the graph** — from any node, follow edges upstream (where did this come from) and downstream (what depends on this). The two canonical jobs built on this are impact analysis (assess what a change affects) and root-cause tracing (follow unexpected results back to origin).
3. **Maintained against actual flows** — the graph is a record of how data really moves through real systems, kept current by capture machinery of some kind (automatic harvesting, event collection, platform instrumentation, or curated registration) — not a free-form drawing surface.

Drop (1) and there is no lineage. Drop (2) and the product is a static flow picture — documentation, not a platform. Drop (3) and it becomes a generic diagramming tool: the graph's meaning ("this is how our data actually moves") is the product.

### Historical / market-sample check

- Pre-automation era: ETL suites have shipped built-in dependency/lineage views over their own jobs since the 2000s, and governance tools supported manually curated flow maps over registered assets. Both satisfy L0 — capture mechanism is not definitional.
- A hand-drawn Visio data-flow diagram fails L0(1)+(3): nodes are shapes, not managed records of identified external assets, and nothing keeps it current. This confirms the "maintained against actual flows" clause is load-bearing.
- Therefore: automatic capture, query-log parsing, event standards, column-level depth, time travel, quality overlays, AI Q&A are all NOT definitional — L1/L2. The historical check passes.

### L1 — Common Mature Structure

- Automatic capture machinery, in one of several philosophies: query-log parsing (read a database's query history, parse SQL, resolve source/target), runtime lineage events (jobs emit events when they run — OpenLineage), platform instrumentation (the platform itself records reads/writes as they happen), code/ETL/BI harvesting (parse scripts, ETL exports, BI report definitions), and view/stored-procedure parsing.
- A search/browse entry point into the graph (find the starting node).
- Column-level lineage (trace a specific field through its transformations) — common in current products, with documented blind spots (UDFs, path references).
- Edge details: the SQL/transformation or job that produced an edge.
- Process nodes with run history; association of flows with the jobs/queries that produced them.
- Impact-analysis surfaces: direct children vs. all downstream; grouping by type/workspace; notifying affected owners.
- Time dimension: time-range filters on the graph, retention windows, lineage/run history, versioned lineage ("as of" views) in some products.
- Permission-aware graph visibility: users see flows only through assets they may know about; inaccessible nodes are masked or unnamed.
- Programmatic access: lineage APIs for traversal/automation; lineage exposed as queryable tables.
- BI/dashboard lineage: reports and dashboards as downstream consumers.
- Cross-system aggregation: registering external systems' assets into one graph.

### L2 — Variant / Optional Structure

- Data-quality/observability overlays (test outcomes rendered on the graph).
- AI/ML model lineage nodes.
- Natural-language lineage Q&A.
- Inferred lineage (relationships inferred beyond parsed statements to fill gaps).
- Lineage "layers" (service-level, domain-level, data-product-level views of the same graph).
- Compliance packaging (sensitive-data flow tracking, audit-trail exports).
- Packaging: standalone dedicated product vs. catalog-embedded module vs. platform-native capability vs. OSS event-collected service vs. ETL-suite-native.
- Manual-only or manual-supplement curation modes.
- Display-depth controls (how many hops/nodes to render).

### L3 — Vendor-specific (research notes only)

- Marquez: OpenLineage reference implementation; namespace/job/dataset/run model; `/lineage` HTTP endpoint; immutable dataset versions mapped to run IDs; job version pointers to code.
- Microsoft Fabric: workspace-scoped lineage view (downstream cross-workspace handled by the separate impact-analysis pane); "Notify contacts" email machinery; OneLake catalog entry points; documented dataflow-connection caveat; Viewer-role data-source hiding.
- OpenMetadata: Lineage Agent configuration surface (query-log duration, parsing timeout, result limit, filter condition); cross-database lineage with service-name resolution; dbt manifest-based column lineage; CSV query-log fallback for unsupported connectors; lineage layers (column/observability/service/domain/data-product); display-depth config (up to 3 nodes per layer).
- Cloudera Data Lineage (Octopai): Custom Lineage Connector for non-native systems; "inferred lineage & augmented links"; 60+ integrations claim; vendor-cited survey statistics.
- Databricks: `system.access.table_lineage` / `system.access.column_lineage` system tables; BROWSE-privilege gating and masked nodes; metastore-wide aggregation; Genie Code `/getTableLineages`; lineage availability boundary (Sep 1, 2024); documented blind spots (renames, RDDs, UDFs, path references, rolled-back transactions).

## Rejected Findings

Considered and rejected as definitional (with reasons):

- **Column-level lineage** — common in current products but absent (at least on evidence) in platform-bundled views; a table-level-only lineage platform is still a lineage platform (→ L1).
- **Automatic capture** — manually curated lineage satisfies the Type; the historical check excludes automation from the definition (→ L1).
- **Cross-system span as a hard requirement** — platform-native lineage starts single-platform and extends outward via registration; typical but not invariant (→ L1/L2).
- **Time-travel / historical lineage** — common (run history, retention, time ranges) but not universal on evidence (→ L1).
- **OpenLineage specifically** — one ecosystem mechanism for event collection, not a property of the Type (→ L3 context).
- **Data-quality overlays** — present in some products; observability is its own Type (→ L2).
- **AI/natural-language lineage Q&A** — single-product direct evidence in the sample; recent era (→ L2).
- **BI lineage** — common but some products start data-engineering-only (→ L1).
- **Compliance/audit packaging** — a framing and feature layer, not the structure (→ L2).
- **"Metadata management" breadth** (standards, exchange, metadata lifecycle) — belongs to Metadata Management Platform (→ boundary).

## Boundary Findings

- **vs. Data Catalog** — the closest sibling, already processed from the catalog side (its pass recorded: "lineage is one relationship structure inside a catalog; a dedicated lineage platform centers on capture/tracing/debugging of data flows at pipeline depth"). Confirmed from this side: the catalog's primary object is the asset inventory + discovery/understanding loop ("what is this, what does it mean, can I trust it"); the lineage platform's primary object is the flow graph itself (capture, trace, impact, root-cause). A catalog without lineage is still a catalog; a lineage platform without a discovery inventory is still a lineage platform. In suites the two merge (lineage becomes a tab on the catalog entry page) — packaging overlap, not a Type merge.
- **vs. Metadata Management Platform** — metadata management treats metadata itself as governed enterprise content (models, standards, exchange, lifecycle); lineage is one relationship structure within that content. A lineage platform stores and serves flow metadata but its product center is the graph and its trace operations.
- **vs. Data Observability Platform** — observability monitors the runtime health of data (freshness, volume, schema, quality tests, incidents); lineage describes the structure of flows. They interlock: lineage supplies the blast radius, observability supplies the failing node. OpenMetadata's "observability layer" on the lineage graph shows the seam from the lineage side.
- **vs. ETL/ELT / Data Integration Platform** — integration platforms execute data movement and typically emit lineage for their own flows as a byproduct; the lineage platform's job is the cross-tool graph and its traversal, not execution. ETL-native lineage covers only that tool's flows (a real but partial realization).
- **vs. Data Governance Platform** — governance organizes policy, stewardship, and compliance workflows over the estate; lineage supplies evidence those workflows consume (impact analysis before changes, sensitive-data flow for audits). Governance suites embed lineage; lineage platforms serve governance use cases without being policy engines.
- **vs. Diagramming Application** — diagramming authors free-form shapes and connectors; a lineage platform maintains a record of actual flows over identified external assets, kept current by capture machinery. The "maintained against reality" clause is the wall.
- **vs. Database Management Console / query history** — query history is one system's log of its own queries; lineage aggregates across systems into a navigable graph with resolved asset identity. Query-log parsing is one capture input to lineage, not the Type.
- **vs. Data Warehouse / Lakehouse Platform** — they hold the data; lineage describes flows over data wherever it lives. Platform-native lineage (Databricks) is a capability of the platform, extended outward via external-asset registration — a packaging pole, not a separate Type.
- **"去掉什么就变成另一个 Type" tests**:
  - Remove the flow/edge structure, keep the asset inventory + descriptions → Data Catalog.
  - Hold the data instead of describing flows → warehouse/lakehouse (no longer a lineage platform at all).
  - Remove trace/traversal operations → a static flow picture → drifts to documentation/diagramming.
  - Remove "maintained against actual flows" → generic diagramming tool.
  - Center on runtime health/tests/alerts instead of the flow structure → Data Observability Platform.
  - Center on executing the flows → ETL/ELT/Data Integration Platform.
  - Center on policy/stewardship workflows over the estate → Data Governance Platform.

## Market-structure observation

Both dedicated standalone lineage vendors sampled or targeted have been absorbed: Manta → IBM (2023), Octopai → data.world (2024) → Cloudera Data Lineage (2026 product page). The 2026 market realizes this Type mostly as: (a) dedicated automated-lineage products inside larger platforms, (b) lineage modules of catalogs/governance suites, (c) platform-native lineage in lakehouses, (d) OSS event-collected services. This is a packaging observation, not evidence that the Type has dissolved — the flow-graph-with-trace-operations structure remains the product in every realization.

## Uncertainties

- Manta could not be fetched at all (403s / transport error); the dedicated-vendor pole rests on Cloudera Data Lineage (formerly Octopai) at product-page strength only — no operational documentation was fetched for it, so its workflow details (harvest scheduling, graph operations, UI specifics) are unverified.
- Marquez column-level lineage and manual-editing support were not confirmed on fetched pages; left unstated rather than guessed.
- OpenMetadata historical/time-travel lineage and permission behavior on the graph were not on fetched pages; left unstated.
- Fabric's lineage view is workspace-scoped on the fetched page; deeper cross-workspace graph behavior (beyond impact analysis) unverified.
- The exact edge between this leaf and Metadata Management Platform remains soft in suites; consistent with the data-catalog pass, held on "primary object of work."
- Vendor-cited survey statistics (Octopai/Dataversity 2023) are marketing-sourced; kept out of the final document.

## Final Synthesis

A Data Lineage Platform is an application that maintains a navigable graph of how data actually flows through an organization's data estate: nodes standing for data assets and the processes that move or transform them, edges recording real flows between systems whose data the platform never holds. The graph is kept current by capture machinery of one kind or another — query-log parsing, runtime lineage events, platform instrumentation, code/ETL/BI harvesting, or curated manual registration — and the product's reason to exist is tracing: from any node, follow the graph upstream to origins or downstream to consumers, so that impact analysis ("what breaks if I change this?") and root-cause analysis ("where did this wrong number come from?") become graph operations instead of tribal knowledge. Column-level depth, time windows, quality overlays, permission-aware visibility, programmatic access, and AI question-answering all enrich the graph; none of them defines it. The Type survives the consolidation of its standalone vendors because every catalog, governance suite, and lakehouse platform that absorbs it still ships the same defining structure: the maintained flow graph and the ability to trace it.
