# Research Notes — Time-series Database Workbench

Research date: 2026-09-09

## Research Goal

Understand what a Time-series Database Workbench is as an Application Type: what its world contains, who works in it, how a work session actually proceeds, and where its boundaries sit against the neighboring database-surface Types (Database Management Console, SQL Client / SQL Workbench, Analytical Query Editor, Graph Database Explorer, RDF/SPARQL Workbench, Vector Database Console, Database IDE) and against the monitoring/dashboard and industrial-historian Types.

This pass discharges three cross-check requests recorded by earlier passes:

1. **database-management-console** (processed 2026-09-07): "graph-database-explorer / vector-database-console / time-series-database-workbench / rdf-sparql-workbench are data-centric exploration Types — cross-check recommended where a sampled engine console also administers deployments."
2. **graph-database-explorer** (processed 2026-09-08) + **rdf-sparql-workbench** (processed 2026-09-09): the §13 query-surface family expectation — "vector-database-console + time-series-database-workbench (§13) and sql-client + sql-workbench (§12/§13) are the same query-surface family over other engine classes — the console/explorer center-of-gravity test is expected to hold at those passes."
3. **industrial-historian** (processed 2026-09-08) FORWARD FLAG: "convergence zone documented (historians exposing SQL/APIs, TSDBs gaining industrial connectors) — seam held at source+semantics+consumer (control-system acquisition, quality-carrying process data, plant consumers vs arbitrary machine telemetry)." The historian pass also placed "generic IT time-series database" in this leaf's territory ("2+3 without 1 = generic IT time-series database = time-series-database-workbench territory").

## Initial Boundary (hypothesis before research)

A Time-series Database Workbench is an interactive query-and-exploration surface over a live time-series database (TSDB): the user connects to a running TSDB, issues queries in the engine's query language, works with time as a first-class dimension (time ranges, windows, downsampling), inspects results as tables and time-series charts, and commonly loads data and watches ingestion. Expected confusions:

- **Database Management Console (§13, processed)** — deployment-centric; the console pass predicted data-centric exploration Types keep administration as a secondary surface.
- **SQL Client / SQL Workbench (§12/§13, processed as one population)** — connection-agnostic SQL surfaces; this leaf should be engine-class-bound (TSDBs) with time-native structure.
- **Analytical Query Editor (§13, processed)** — platform-bound SQL editor for analytical platforms; genus overlap ("engine-bound query surface"), different engine class and different structure.
- **Industrial Historian (§16, processed)** — plant-side archival system of record; convergence zone flagged by that pass.
- **Dashboard Platform / Metrics Monitoring (§14)** — dashboards and alerting consume TSDBs; the workbench is where practitioners query the raw series. Grafana-class products expected to sit on the other side.
- **Graph Database Explorer / RDF-SPARQL Workbench / Vector Database Console (§13)** — engine-class siblings of the same query-surface family.
- **The TSDB itself / CLI shells** — the workbench is a surface; CLI shells expected to be the thin ancestor pole.

## Research Questions

1. What is the object of work — the deployment, the stored series data, or curated views?
2. What is the working context (bundled UI, cloud console, GUI component, CLI) and the connection model?
3. What query languages appear, and is any single language definitional?
4. How does time enter the interaction (time-range controls, windowing, downsampling, chart-over-time)?
5. What result forms exist, and how is the time-ordered structure preserved?
6. What data operations exist beyond querying (import, schema browsing, deletion, retention)?
7. What feedback/monitoring surfaces exist, and where does the console seam sit?
8. Where do dashboards/notebooks appear, and is dashboard-building part of the Type?
9. How do older / leaner / text-mode surfaces fit (historical check)?
10. Does the historian seam (source + semantics + consumer) hold from this side?

## Representative Products

| Product | Why selected | Philosophy / delivery | Evidence |
|---|---|---|---|
| InfluxDB (InfluxData) | The market-defining modern TSDB; UI documented across three language generations | Embedded InfluxDB UI with Data Explorer (Flux builder ⇄ script editor); separate CLI shells; InfluxDB 3 Explorer as a new separate UI | A — official Data Explorer page + docs TOC fetched |
| QuestDB | Open-source TSDB with the richest documented bundled workbench | Web Console bundled with every instance: Code Editor, Notebooks, Schema Explorer, Result Grid, Query Log, Import CSV, Metrics View, Table Details | A — Web Console overview + docs index (llms.txt) fetched |
| Timescale / Tiger Data (TimescaleDB) | The SQL/Postgres-extension pole; managed-cloud console surface | Tiger Console SQL Editor; psql as the equal first-class alternative; standard SQL throughout | A — docs root + 5-minute quickstart fetched |
| Prometheus | The monitoring-native TSDB pole; PromQL | Expression browser served by the server itself; explicitly positioned for ad-hoc queries/debugging, with dashboards delegated to Grafana | A — official expression browser page fetched |
| TDengine | IoT/industrial pole; non-Western-origin vendor | SQL language; taos CLI; taosExplorer GUI (Enterprise) with query + monitoring + permissions + backup; taosX industrial connectors | A — docs root + components overview fetched |

Sample spans: dominant vendor, open-source challenger, Postgres-extension/cloud vendor, monitoring-native project, IoT/industrial vendor. Delivery forms: embedded engine UI (3), cloud console (1), enterprise GUI component (1), CLI shells (multiple, as the thin pole). Languages: Flux/InfluxQL/SQL, SQL, SQL, PromQL, SQL. All five Tier A.

## Sources

Fetched 2026-09-09:

1. InfluxDB OSS v2 — "Query in Data Explorer": https://docs.influxdata.com/influxdb/v2/query-data/execute-queries/data-explorer/ (redirected from /visualize-data/explore-metrics/)
2. InfluxDB OSS v2 — documentation table of contents (same fetch; surfaces: Dashboards, Notebooks, Tasks, Checks/Alerts, Buckets/Tokens/Users admin, influx CLI, InfluxQL shell, Flux REPL, Chronograf, Grafana integration; InfluxDB 3 Explorer release-notes blurb: InfluxQL support, AI-assisted Flux→SQL converter beta, sample-data simulators)
3. QuestDB — documentation index (llms.txt): https://questdb.com/docs/llms.txt
4. QuestDB — "Web Console overview": https://questdb.com/docs/getting-started/web-console/overview.md
5. Tiger Data (Timescale) — documentation root: https://docs.timescale.com/
6. Tiger Data (Timescale) — "5-minute quickstart": https://docs.timescale.com/get-started/quickstart/quickstart-5-minutes/
7. Prometheus — "Expression browser": https://prometheus.io/docs/visualization/browser/
8. TDengine — documentation root / reading guide: https://docs.tdengine.com/
9. TDengine — "TDengine Components" (Operations and Tooling overview): https://docs.tdengine.com/operations-and-tooling/overview/

Prior-pass context (read, not fetched this pass): research/database-management-console.md, research/graph-database-explorer.md, research/industrial-historian.md, research/sql-client.md, research/sql-workbench.md, research/rdf-sparql-workbench.md.

Attempted and abandoned per source-access rules:

- questdb.io/docs/reference/web-console/ and questdb.io/docs/get-started/web-console/ 404'd (docs moved to questdb.com); resolved via the documented llms.txt index rather than further guessing.
- docs.timescale.com/get-started/quickstart/quickstart-5-minutes/index.md 404'd (the .md suffix is not served at that path); the plain URL was fetched successfully.
- docs.tdengine.com/cloud/explorer/ 404'd (TDengine Cloud docs live under a separate version selector); the OSS components overview was used instead — taosExplorer is therefore evidenced at component-overview level only.

## Product Observations

### InfluxDB — Data Explorer in the InfluxDB UI (evidence layer A unless noted)

From the official "Query in Data Explorer" page and the docs TOC:

- Positioning: "Build, execute, and visualize your queries in InfluxDB UI's **Data Explorer**." Entry via the UI navigation menu.
- **Dual authoring modes**: a Flux **query builder** (select bucket as data source, edit time range, add filters, group data into tables) and a **Script Editor** for manually editing the query; seamless switching between builder and script ("Move seamlessly between using the Flux builder or templates and manually editing the query"); builder edits are not preserved when switching to script.
- **Functions list**: browse available Flux functions; click to insert into the query.
- **Execution**: Submit (or Ctrl+Enter); **Cancel** while running; multiple query **tabs** (add tab, rename, hide/show a tab's visualization).
- **Results**: preview graph in the upper pane; **View Raw Data** toggle to see data in table format with paging, group keys and data types identifiable; **Save as CSV**; manual refresh.
- **Time range**: dropdown of presets plus **Custom Time Range** with precision to nanoseconds; timezone selection (local/UTC). (Default range observed as 5m — vendor default, research-notes only.)
- **Visualization types**: dropdown selection (Band, Gauge, Graph, Graph + Single Stat, Heatmap, Histogram, Mosaic, Scatter, Single Stat, Table per the TOC).
- **Save as**: Dashboard Cell, Task, or Variable — the query loop feeds the platform's dashboard/task/variable objects.
- Surrounding UI surfaces (TOC): Dashboards, Notebooks, Tasks, Checks/Notification endpoints/Rules (monitor & alert), Load data source in UI (Telegraf, scrapers, client libraries, CSV), Buckets/Tokens/Users/Orgs admin, Telegraf configs, Templates/Stacks.
- **CLI poles** (TOC): influx CLI, InfluxQL shell, Flux REPL — first-class tools alongside the UI.
- **Language generations** (TOC): InfluxQL (v1-lineage, SQL-like), Flux (v2), SQL (v3); **InfluxDB 3 Explorer** is a separate newer UI product whose release notes list InfluxQL support and an AI-assisted Flux→SQL converter (beta).
- **External tools** (TOC): Grafana and Chronograf listed as separate tools; Chronograf was the v1-era UI, shipped as its own product.

### QuestDB — Web Console (evidence layer A unless noted)

From the official Web Console overview and the docs index:

- Positioning: "The QuestDB Web Console is a browser-based SQL client bundled with every QuestDB instance. Write and run SQL, explore your schema, build notebook dashboards with live charts, bring in AI assistance, and monitor ingestion, all without installing anything." Served at a fixed port on the server (port observed in docs; research-notes only).
- **Layout**: Schema Explorer on the left; editor and notebook tabs in the center with the **Result Grid** and **Query Log** below; right sidebar with quick tools (AI Assistant, Table Details, Help, News).
- **Code Editor**: "write and execute SQL queries with features like syntax highlighting, auto-completion, and error tracing. It supports executing queries by selection, multiple query execution, and query planning."
- **Notebooks**: "combine SQL cells, markdown notes, and live charts in a single tab. Use them to explore data step by step, or flip to the grid layout and arrange cells into an auto-refreshing dashboard." (Index TOC adds: notebook cells, nine chart types, notebook-wide variables via DECLARE, live dashboards, manage/share/export/restore.)
- **Schema Explorer**: "the navigation hub for exploring tables and materialized views… columns with data types, storage configuration (partitioning and WAL status)".
- **Table Details**: "real-time monitoring and detailed metadata for any table or materialized view… health status indicators, WAL ingestion metrics such as pending rows and transaction lag, performance alerts, and a full view of the table's DDL, columns, and storage configuration."
- **Result Grid**: "displays your query results in an interactive table format with features for data navigation, export, and visualization."
- **Query Log**: "monitors query execution status and performance metrics… shows execution times, row counts, and detailed error information."
- **Metrics View**: "real-time monitoring and telemetry capabilities for your QuestDB instance… interactive charts and widgets to track database performance, WAL operations, and table-specific metrics."
- **Import CSV**: "upload and import CSV files into QuestDB with automatic schema detection, flexible configuration options, and detailed progress tracking… create new tables or append to existing ones."
- **AI Assistant** (bring-your-own-key) and **QuestDB MCP server** (links AI coding agents to the running Web Console "with a four-level permission model").
- **Governance**: instance naming/type/color editable; gated by configuration or RBAC permissions in QuestDB Enterprise ("only the users with `SETTINGS` or `DATABASE ADMIN` permission can edit the instance information").
- Language: SQL with time-series extensions (SAMPLE BY, ASOF JOIN, LATEST ON, WINDOW JOIN, designated timestamps, TTL) per the SQL reference TOC.

### Timescale / Tiger Data — Console SQL Editor (evidence layer A unless noted)

From the docs root and the 5-minute quickstart:

- Positioning (docs root): "TimescaleDB is a PostgreSQL extension, not a separate database or fork, so you keep the same clients, drivers, and SQL you use with plain PostgreSQL." Tiger Cloud is the fully-managed service; Tiger Console is its web console.
- **SQL Editor in Tiger Console**: the quickstart's "Pick one way to run SQL" offers exactly two first-class options — **Tiger Console's SQL Editor** ("In Tiger Console, select your service. Click `SQL Editor` at the bottom. You're connected as soon as you see the query panel.") or **psql** in a terminal with the service connection string.
- The workflow is plain standard SQL: create a hypertable (`tsdb.hypertable` option, time-partitioned into chunks automatically), insert rows, `SELECT … ORDER BY time DESC`.
- Engine concepts (docs root): hypertables, continuous aggregates, columnstore compression, retention policies — the time-series machinery lives in the engine, exposed through SQL.
- Deeper SQL Editor features (history, charts, result-grid behavior) were not documented at the fetched level; no claims drawn.

### Prometheus — Expression browser (evidence layer A)

From the official "Expression browser" page:

- "The expression browser is available at `/graph` on the Prometheus server, allowing you to enter any expression and see its result either in a table or graphed over time."
- Explicit positioning: "This is primarily useful for ad-hoc queries and debugging. For graphs, use Grafana or Console templates."
- Language: PromQL (per the Querying docs section). The browser is served by the Prometheus server itself — no separate install, no connection management.
- The page is brief; typeahead/schema-browsing detail was not directly observed; no claims drawn beyond the page.

### TDengine — taos CLI + taosExplorer (evidence layer A unless noted)

From the docs root and the components overview:

- Positioning: open-source, high-performance time-series database "purpose-built for IoT, connected vehicles, industrial internet, finance, IT operations, and similar scenarios." "TDengine uses SQL as its query language… and extends SQL for time-series scenarios such as interpolation, downsampling, and time-weighted averages."
- **taosExplorer**: "a graphical management tool" (Enterprise visual component) — "execute SQL queries, monitor system status in real-time, manage user permissions, and perform data backup and recovery operations… data synchronization with other clusters, data export, and management of topics and stream computing." Feature set differs between the OSS and Enterprise editions.
- **taosX** (Enterprise pipeline): connects third-party sources "without the need for coding" — "AVEVA PI System, AVEVA Historian, OPC-UA/DA, InfluxDB, OpenTSDB, MQTT, Kafka, CSV, … MySQL, PostgreSQL, and Oracle" — accessed "through the browser user interface provided by taosExplorer."
- **taosKeeper**: monitoring-metric export tool; **taosAdapter**: REST/WebSocket bridge with InfluxDB/OpenTSDB-compatible write interfaces and Prometheus remote read/write.
- **External visualization/BI**: "TDengine supports seamless integration with numerous visualization and BI tools, such as Grafana, Power BI" — dashboards sit outside the database's own tooling.
- **TDengine IDMP**: a separate AI-native platform component for "visualization, event management, root-cause analysis, and AI insights in industrial scenarios" — outside the TSDB workbench surface.
- taos CLI detail lives in the Tools section (not fetched); the CLI pole is evidenced by the client-driver/CLI component structure and the SQL-first design.

## Cross-product Comparison

| Dimension | InfluxDB Data Explorer | QuestDB Web Console | Tiger Console SQL Editor | Prometheus Expression browser | TDengine taos CLI / taosExplorer |
|---|---|---|---|---|---|
| Working context | InfluxDB UI bundled with OSS/Cloud; org + bucket as data source | Web Console bundled with every instance, served by the server | Tiger Console (cloud) SQL Editor bound to the selected service; psql equal alternative | served by the Prometheus server itself at /graph | taos CLI client; taosExplorer GUI (Enterprise) |
| Object of work | buckets, measurements, tags/fields; time-ordered points | tables/materialized views, columns, WAL/ingestion state; time-ordered rows | hypertables (time-partitioned tables), rows | metrics (series with labels), time-ordered samples | databases/supertables/subtables; time-ordered rows |
| Query language | Flux (builder + script); InfluxQL; SQL (v3) | SQL + time-series extensions (SAMPLE BY, ASOF JOIN, LATEST ON) | standard SQL (PostgreSQL) | PromQL | SQL extended for time series (interpolation, downsampling) |
| Time-native controls | time-range presets + custom range (nanosecond precision), timezone | charts over time; time-series SQL extensions | time handled in SQL/data | result "graphed over time"; expression evaluation over ranges | interpolation/downsampling language extensions |
| Result forms | graph + View Raw Data table; CSV export | Result Grid (interactive table, export, visualization) + notebook charts | query panel results | table or graph over time | CLI result tables; Explorer surfaces |
| Schema browsing | bucket selection; filters by attributes/columns | Schema Explorer (objects, columns, storage config) | not observed at fetched level | not observed | Explorer manages databases/supertables/subtables |
| Import/ingestion surface | Load-data UI (Telegraf, scrapers, CSV, client libs) | Import CSV (auto schema detection, create/append) | not observed | not part of the browser | taosX pipelines driven through Explorer UI (Enterprise) |
| Query feedback | cancel; multi-tab; functions list | Query Log (times, row counts, errors); error tracing; query planning | not observed | not observed | not observed |
| Instance monitoring | separate UI surfaces | Metrics View (instance telemetry); Table Details (ingestion health, WAL lag) | not observed | separate status endpoints | Explorer: real-time system status |
| Save/share | Save as Dashboard Cell / Task / Variable | Notebooks (manage/share/export); live dashboards | not observed | not observed | not observed |
| Dashboards | separate Dashboards area; Explorer feeds cells | notebooks flip to auto-refreshing dashboards | — | explicitly delegated: "For graphs, use Grafana" | external (Grafana, Power BI) |
| Administration | buckets/tokens/users/orgs in UI admin | RBAC-gated settings (Enterprise); instance naming | service management elsewhere in console | — | Explorer: user permissions, backup/recovery (Enterprise) |
| AI / agents | InfluxDB 3 Explorer: AI-assisted Flux→SQL (beta) | AI Assistant (BYOK); MCP server with permission model | Tiger MCP for AI agents | — | IDMP as separate AI platform |
| Packaging | embedded UI of the engine (+ separate 3.x Explorer product) | embedded web console of the engine | cloud-console editor of the managed service | embedded page of the server | CLI + Enterprise GUI component |

## Canonical Model (abstraction levels)

The Type's world, in conceptual terms:

```text
Connection (a specific running time-series database, reached through the engine's own surface or client)
  └── Stored time-series data (measurements/tables/metrics with tags/labels + fields/values;
        time-ordered points; schema incl. partitioning/retention where the engine holds it)
        └── Queries (the engine's own query language; time range as a first-class scope)
              └── Results (time-ordered series/tables — rendered as tables and commonly as charts over time;
                    inspectable, exportable)
        └── Data operations (import/load; schema browsing; retention/delete where offered)
        └── Feedback surfaces (query log/history, execution times, ingestion/instance monitoring)
```

### L0 — Defining Invariant

Three jointly-held structures, deliberately small:

1. **A live time-series database as the working context.** The workbench operates against a specific running TSDB, reached through the engine's own surface (embedded UI, cloud console, GUI component) or its CLI — it is engine-class-bound (a TSDB family and its query language, never arbitrary data substrates). Remove → a generic SQL client or charting tool.
2. **The stored time-series data as the object of work.** The database's schema (measurements/tables/metrics; tags/labels; fields/values; partitioning/retention where the engine holds it) and its time-ordered points are what the user browses, queries, loads, inspects, and (in SQL-speaking engines) modifies. Remove (object = the deployment's lifecycle/configuration) → Database Management Console; (object = curated views for an audience) → Dashboard Platform.
3. **The author-and-execute query loop with time-ordered results.** The user writes queries in the engine's own query language — SQL where the engine speaks SQL, engine-specific languages otherwise — executes them against the connected database, and results come back as time-ordered series/tables that stay inspectable, commonly rendered both as tables and as charts over the selected time range. Time is the organizing dimension of both the query scope and the result presentation. Remove → a fire-and-forget runner, a metrics endpoint, or a fixed dashboard.

Load-bearing: 1 alone = connection manager/driver; 2 without 1+3 = a data dump; 3 without 1+2 = a query playground with no live database; 1+3 without 2 = blind execution (2 is the content anchor); 1+2 without 3 = a viewer below the Type. Remove the TSDB class binding → SQL Client / generic workbench territory. Remove the query loop, keep curated views → Dashboard Platform / monitoring dashboards.

### L1 — Common Mature Structure (standard capabilities, not definitional)

- query editor with syntax highlighting, completion, error tracing; run/cancel; multiple tabs; execute-selection
- time-range selection as a first-class control (presets + custom ranges, timezone handling)
- dual result rendering — table ⇄ time-series chart — with visualization-type choice and a raw-data view
- schema/series browsing (measurements/tables/metrics, tags/labels, fields/columns, storage configuration)
- result export (CSV-class); paging/in-view caps for large results
- query history/log with execution times, row counts, error detail
- data import surfaces (CSV upload with schema detection; line-protocol-class ingestion; load-data wizards)
- saved queries / notebooks combining queries, notes, and charts
- ingestion and instance monitoring surfaces (real-time metrics, ingestion lag/health, WAL state)
- save query into neighboring objects (dashboard cell, task, variable) — the seam features

### L2 — Variant / Optional Structure

- packaging: embedded engine UI (dominant) vs cloud-console SQL editor vs enterprise GUI component vs CLI shell (the thin ancestor)
- language: SQL (increasingly common across the class) vs engine-specific languages (Flux, InfluxQL, PromQL); language families change across engine generations — one vendor's docs span three
- breadth: query-only surface vs studio (schema + import + monitoring + notebooks + admin)
- dashboards inside the workbench (live dashboards, save-as-cell) — accretion toward the Dashboard Platform seam
- AI assistance (NL→SQL, query explanation/fixing, BYOK) and MCP/agent integration (era-current)
- permission/RBAC administration and backup operations in enterprise editions
- multi-instance naming/organization for users managing many deployments

### L3 — Vendor-specific (research notes only)

- InfluxData: Flux builder ⇄ Script Editor toggle; default 5-minute time range; Save-as Dashboard Cell/Task/Variable; buckets/orgs/tokens model; Telegraf configs UI; Chronograf as the separate v1-era UI; InfluxDB 3 Explorer as a separate new UI (InfluxQL support, AI Flux→SQL converter beta, sample-data simulators); nanosecond-precision custom time ranges.
- QuestDB: fixed server port for the Web Console; Notebooks with nine chart types, notebook variables via DECLARE, grid-layout live dashboards, manage/share/export/restore; four-level MCP permission model; BYOK AI assistant; Table Details WAL pending-rows/transaction-lag metrics; instance naming/type/color; Unicode-block-character inline chart SQL functions; RBAC permission names.
- Timescale/Tiger: hypertable/chunk vocabulary; `tsdb.hypertable`/`segmentby`/`orderby` options; SQL Editor "at the bottom" of the console service view; Tiger CLI; Tiger MCP; continuous aggregates/columnstore/retention as engine features.
- Prometheus: `/graph` path; "primarily useful for ad-hoc queries and debugging"; "For graphs, use Grafana or Console templates"; console templates as the server-side alternative.
- TDengine: taosExplorer Enterprise-only with OSS/Enterprise feature split; taosX connector list (AVEVA PI System, AVEVA Historian, OPC-UA/DA, InfluxDB, OpenTSDB, MQTT, Kafka, CSV, MySQL, PostgreSQL, Oracle); taosKeeper; taosAdapter compatibility writes; IDMP as separate AI platform; Grafana/Power BI named as external BI.

## Vendor-specific Findings

See L3. Notable market facts: (a) the workbench ships as a component surface of one engine family in every sampled case — embedded UI, cloud console, or GUI component — plus the engine's CLI as the text pole; never a universal multi-engine SKU; (b) two vendors explicitly delegate dashboards outward (Prometheus → Grafana; TDengine → Grafana/Power BI), while two others absorb dashboard-adjacent features into the workbench (QuestDB notebook live dashboards; InfluxDB save-as-dashboard-cell) — the seam is live in the market, in both directions; (c) SQL is becoming the class's common language (four of five sampled engines speak SQL in their current generation), but engine-specific languages remain first-class (Flux, PromQL), so no single language can be definitional; (d) TSDB workbenches bundle more instance-observation machinery than graph explorers do (QuestDB Metrics View/Table Details; taosExplorer system status) — the same nuance the RDF pass recorded for commercial RDF workbenches.

## Rejected Findings

- **"The workbench is a DBaaS/cloud console"** — rejected. Embedded engine UIs (InfluxDB UI, QuestDB Web Console, Prometheus expression browser) and CLI shells satisfy the core with no cloud machinery; the cloud-console SQL editor is one packaging pole.
- **"SQL is the defining language"** — rejected. PromQL and Flux are first-class engine languages in the sample; the invariant is the engine's own query language, with SQL as the current majority realization.
- **"Chart rendering is the defining structure"** — rejected. Rendering is the common presentation; the CLI pole returns tables and still satisfies the core. The invariant is time-ordered results kept inspectable, with chart-over-time as the dominant modern realization.
- **"Dashboard building belongs to the workbench"** — rejected as definitional. Two vendors explicitly delegate dashboards (Prometheus→Grafana; TDengine→Grafana/Power BI); where dashboard features appear inside a workbench (QuestDB notebooks, InfluxDB save-as-cell) they are accretions on the query loop, not its replacement.
- **"The workbench is read-only"** — rejected. SQL-speaking engines expose writes through the same surface (QuestDB SQL spans DDL/DML; Timescale quickstart creates tables and inserts through the SQL Editor); ingestion surfaces load data. Read-only posture is a variant (Prometheus's browser is query-only).
- **"Instance monitoring belongs to the workbench"** — rejected as definitional. Monitoring surfaces appear inside some workbenches (QuestDB Metrics View, taosExplorer) and outside others (Prometheus status endpoints, InfluxDB's separate surfaces); it is the console seam, common-optional at best.

## Boundary Findings

1. **vs Database Management Console (§13, processed) — cross-check DISCHARGED from this side.** The console's object is the running deployment (lifecycle, configuration, backups); this Type's object is the stored time-series data plus the query loop. The center-of-gravity test holds: remove the query/explore loop from QuestDB's Web Console → an instance monitoring panel (console work); remove the Metrics View/admin surfaces → still a full workbench. Sampled workbenches bundle more administration than graph explorers do (QuestDB Metrics View/Table Details; taosExplorer permissions/backup; InfluxDB UI buckets/tokens/users) — the same center-of-gravity-not-wall nuance the RDF pass recorded. Both leaves kept distinct; documents cross-reference.
2. **vs SQL Client / SQL Workbench (§12/§13, processed as one population) — family expectation RATIFIED from this side.** Same query-surface family shape; the engine-class binding is part of this leaf's invariant (TSDB engines + their query languages + time-native structure). For SQL-speaking TSDBs a generic SQL client can query the data (Timescale's own docs offer psql as an equal path) — but the engine's workbench carries the time-native structure (time-range controls, series/schema browsing, ingestion surfaces, series charting, ingestion monitoring) that generic clients lack. The sql-client pass's prediction holds verbatim.
3. **vs Analytical Query Editor (§13, processed)** — same genus (engine/platform-bound query surface), different class and structure: the analytical query editor binds to analytical platforms (warehouses/lakehouses) with a SQL-worksheet shape; this leaf binds to the TSDB engine class and adds time-native exploration, ingestion surfaces, and engine-specific languages. Keep-both; the binding class is the seam.
4. **vs Industrial Historian (§16, processed) — FORWARD FLAG DISCHARGED from this side.** The historian pass's seam (source + semantics + consumer) holds: the historian is the plant's archival system of record — automated control-system acquisition, quality-carrying process data, plant consumers (trends, replay, operations reporting); this Type is a query/explore surface over a TSDB holding arbitrary machine telemetry ingested through generic channels (line protocol, CSV, Kafka, Telegraf, Prometheus remote write — all directly evidenced in-sample). Convergence confirmed from this side too: TDengine's taosX ingests AVEVA PI System/AVEVA Historian/OPC-UA data — a TSDB absorbing historian-source data through a connector, while the workbench surface remains a data-query surface with no process-semantics machinery (no quality codes as first-class objects, no plant hierarchy). The historian pass's placement of "generic IT time-series database" in this leaf's territory is consistent. No directory change.
5. **vs Dashboard Platform / monitoring dashboards (§14 family)** — Prometheus's own documentation draws the line: the expression browser is "primarily useful for ad-hoc queries and debugging. For graphs, use Grafana or Console templates." The workbench's center is the query loop over the stored data; dashboards are curated, persistent, audience-facing views. Seam features exist in both directions (QuestDB live dashboards; InfluxDB save-as-cell; Grafana querying TSDBs as a data source) — accretion and integration, not identity.
6. **vs Metrics Monitoring / Observability Platform (§14)** — those Types consume TSDBs for alerting, dashboards, and incident response; the workbench is where practitioners query and explore the raw series. Prometheus is the boundary specimen: a monitoring system whose TSDB ships with a workbench surface inside it.
7. **vs Graph Database Explorer / RDF-SPARQL Workbench (§13, processed) / Vector Database Console (§13, unprocessed)** — engine-class siblings of the same query-surface family; the family test (engine-class binding part of the invariant; console center-of-gravity test) holds at this pass. Forward note for the vector-database-console pass: the same tests are expected to hold there.
8. **vs Database IDE (§12, processed)** — the IDE's center is the development loop over schema/objects/code with a persistent working environment; TSDB workbenches center live-data work. SQL-speaking TSDBs are schema-bearing, so a development surface could accrete — but no sampled workbench centers object development. Removal test holds both ways.
9. **vs Data Explorer (§02.12)** — naming collision only: InfluxDB's "Data Explorer" is a workbench surface name; the §02.12 Data Explorer Type is public-data exploration for end users, unrelated to database surfaces.
10. **Component-view nature** — mirroring the Database Management Console, Graph Database Explorer, and API Gateway Management Console precedents: the workbench is essentially never a standalone universal SKU; it ships as the query/explore surface of one TSDB family or database service (embedded UI, cloud console, GUI component, CLI). The Type is genuine (distinct defining work: interactive time-native work on the stored series) but is realized as a component surface. Recorded for the directory author; no unilateral change.

## Uncertainties

1. **Tiger Console SQL Editor depth** — documented only at quickstart level (connect + query panel); editor features (history, charts, export) not directly observed. All Timescale-specific surface claims held at that level.
2. **TDengine taosExplorer detail** — evidenced at component-overview level (Enterprise component); per-surface behavior not fetched. The taos CLI's own documentation was not fetched; the CLI pole for TDengine is inferred from the component structure, not directly observed.
3. **Prometheus expression browser depth** — the official page is brief; typeahead/schema browsing and range-control detail not directly observed.
4. **QuestDB notebook specifics** (nine chart types, variables, share/restore) — taken from the docs index TOC descriptions; page bodies not fetched. Held at TOC level.
5. **kdb+, OpenTSDB, VictoriaMetrics, AWS Timestream, Azure Data Explorer not sampled** — the financial-tick and metrics-platform breadth rests on Prometheus plus the sampled SQL poles; no claims drawn about unsampled products. Azure Data Explorer in particular is a known boundary case (log/telemetry analytics service with its own rich query UIs) — flagged for any future pass that touches it.
6. **InfluxDB 3 Explorer** — evidenced only via the release-notes blurb in the fetched page; its full surface not researched.

## Historical / Market-Sample Check

Applied before freezing the core: would older, regional, platform-native, or leaner products still fit?

- **CLI shells**: psql against TimescaleDB (explicitly offered by the vendor as an equal first-class way to run SQL) and InfluxDB's influx CLI / InfluxQL shell / Flux REPL satisfy legs 1–3 with no GUI: connection, query loop, tabular time-ordered results. The thin ancestor. **Passes.**
- **Language generations**: one vendor's own docs span InfluxQL → Flux → SQL across engine generations; the definition therefore names "the engine's own query language," not any specific language. **Passes.**
- **v1-era packaging**: InfluxDB's v1-era UI (Chronograf) shipped as a separate product — packaging variant, core unchanged. **Passes.**
- **Non-Western origin**: TDengine (a Chinese-origin vendor) fully satisfies the core — no regional bias. **Passes.**
- Era-current capabilities (AI assistants, MCP integration, notebooks, live dashboards, RBAC) are excluded from the core.

The defining core is written implementation- and era-agnostic: live TSDB context + stored time-series data as object + interactive query loop in the engine's language with time-ordered, inspectable results.

## Final Synthesis

A **Time-series Database Workbench** is the interactive work surface over a live time-series database, bound to one TSDB engine family and its query language, whose object of work is the stored time-series data itself — the schema (measurements/tables/metrics, tags/labels, fields) and the time-ordered points — reached through an author-and-execute query loop in which time is the organizing dimension: queries are scoped by time ranges, and results come back as time-ordered series/tables that stay inspectable, rendered as tables and commonly as charts over time. Around that core, mature workbenches add time-range controls, dual table/chart rendering with visualization-type choice, schema/series browsing, result export, query logs with execution feedback, data-import surfaces, saved queries and notebooks, ingestion/instance monitoring, and — in studio-shaped or enterprise products — permissions and backup operations. The Type's disciplines: it does not center the deployment's lifecycle (that is the Database Management Console's work; monitoring surfaces are common-optional accretions), it is not a dashboard builder (dashboards are curated audience-facing views — two vendors delegate them outward explicitly, two absorb seam features), it is not the plant's system of record (that is the Industrial Historian, whose control-system acquisition and process semantics this Type lacks even when a TSDB ingests historian-source data through connectors), and it is always a component surface of one engine family rather than a universal product. Sibling engine-class query surfaces (Graph Database Explorer, RDF/SPARQL Workbench, Vector Database Console, the SQL Client/Workbench population) share the family shape with different substrates.
