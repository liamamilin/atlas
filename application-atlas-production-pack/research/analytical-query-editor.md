# Research Notes — Analytical Query Editor

## Research Goal

Understand what an Analytical Query Editor actually is as an Application Type: its defining structure, its standard workflow, its interfaces, its rules, and its boundaries against neighboring Types — SQL Workbench, Ad-hoc Query Application (already processed; this leaf was explicitly flagged there for joint review), Database Management Console, Database IDE / SQL Client (§12), Business Intelligence Platform, Data Science Workbench.

## Initial Boundary

Initial hypothesis (pre-research):

- Core use: an editor surface for composing and running analytical queries (SQL-first) against a connected analytical data platform (cloud data warehouse, lakehouse, or serverless analytical query service), reading results as grids/charts, and iterating.
- Primary users: technical data practitioners — data analysts, data engineers; not business end users, not database administrators.
- Nearest neighbors: SQL Workbench (general SQL tooling, sibling leaf), Ad-hoc Query Application (business question loop, sibling section), Database Management Console (instance administration, sibling leaf), Database IDE / SQL Client (§12 development tools), BI Platform (curated artifacts), Data Science Workbench (notebooks).
- Likely confusion #1: the boundary vs SQL Workbench may be an audience/binding gradient rather than a structural wall (the ad-hoc pass already recorded this trio as a gradient).
- Likely confusion #2: "analytical query editor" is not a common vendor marketing term — the market instantiates the Type as the query editor surfaces of analytical data platforms (Snowsight worksheets, Databricks SQL editor, BigQuery query editor, Athena console, Redshift query editor, Fabric SQL query editor). The Type must be defined from these real surfaces, not from the leaf name.

## Research Questions

1. What is the unit of work? (query statement / script / worksheet / question)
2. How are queries composed? (SQL text editor; AI/NL assist; visual query editor as secondary surface)
3. What data do they run against? (the platform's own analytical data; cross-database/cross-warehouse querying)
4. What is the interaction loop? (compose → run → result grid → refine → re-run)
5. What happens to results? (grid preview with caps, charts, download, save as view/table, external persistence)
6. What artifacts persist? (saved queries/worksheets, query history, shared queries, scheduled queries/jobs)
7. What observability exists? (duration, rows, data scanned, query profile/execution plan, cost)
8. What rules/constraints matter? (roles/permissions, result limits, session/batch semantics, cost-bearing interactions)
9. Where is the boundary vs SQL Workbench, Ad-hoc Query Application, Database Management Console, Database IDE/SQL Client, BI Platform, Data Science Workbench?
10. Historical check: do standalone warehouse query clients of earlier eras still fit the definition?

## Representative Products

Selected for market representativeness, documentation quality, different product forms, and different ecosystems:

| Product | Form | Why selected |
|---|---|---|
| Snowflake Snowsight (worksheets) | platform workspace web editor | The flagship cloud data warehouse's own query surface; worksheets + results + charts + history + sharing + admin surfaces |
| Databricks SQL editor | platform workspace web editor | Lakehouse-native; collaborative real-time editing; AI assistant (Genie Code); query profile/performance insights |
| Amazon Athena (console query editor) | cloud console service editor | Serverless analytical query service over S3; S3-resident results; workgroup/history model |
| Amazon Redshift query editor v2 | standalone web SQL client for a warehouse | Explicitly self-described as "a separate web-based SQL client application" — shows the Type need not be embedded in a portal |
| Microsoft Fabric SQL query editor | portal editor for warehouse / SQL analytics endpoint | T-SQL editor with save-as-view/table, visualize results, Copilot; unusually well-documented limitations/session semantics |

Note: Google BigQuery (a canonical warehouse query editor) could not be reached — cloud.google.com timed out twice on 2026-09-06 (the ad-hoc pass hit the same limitation with Looker docs on the same domain). ClickHouse Cloud SQL console returned 404. Both are recorded as unsampled; no claims are made about them. The five sampled products cover four ecosystems (Snowflake, Databricks, AWS ×2, Microsoft) and three product forms (workspace editor, console service editor, standalone web client).

## Sources

Research date: 2026-09-06.

### Snowflake (Tier 1 — official documentation)

- Snowsight overview: https://docs.snowflake.com/en/user-guide/ui-snowsight
- Querying data using worksheets: https://docs.snowflake.com/en/user-guide/ui-snowsight-query
- (Both fetched 2026-09-06; the worksheets page is the primary evidence for editor/results/history behavior.)

### Databricks (Tier 1 — official documentation)

- Data warehousing on Databricks: https://docs.databricks.com/en/sql/index.html
- Write queries and explore data in the new SQL editor: https://docs.databricks.com/aws/en/sql/user/sql-editor/
- (Both fetched 2026-09-06.)

### Amazon Athena (Tier 1 — official documentation)

- What is Amazon Athena: https://docs.aws.amazon.com/athena/latest/ug/what-is.html
- Work with query results and recent queries: https://docs.aws.amazon.com/athena/latest/ug/querying.html
- (Both fetched 2026-09-06. The console page https://docs.aws.amazon.com/athena/latest/ug/console.html returned an empty shell — editor-surface specifics such as tab layout and saved-queries UI were NOT directly observed; Athena assertions are kept at service/results/history level.)

### Amazon Redshift (Tier 1 — official documentation)

- Query editor v1: https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor.html
- Query editor v2: https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2.html
- (Both fetched 2026-09-06.)

### Microsoft Fabric (Tier 1 — official Microsoft Learn documentation)

- Query using the SQL query editor: https://learn.microsoft.com/en-us/fabric/data-warehouse/sql-query-editor
- (Fetched 2026-09-06.)

### Source-access limitations

- **Google BigQuery**: cloud.google.com timed out ×2 (run-queries and bigquery-studio pages). Abandoned per network rule. Not sampled; no BigQuery claims made.
- **ClickHouse Cloud**: docs.clickhouse.com SQL console path 404. Abandoned. Not sampled.
- **Athena console page**: returned an empty shell (title only). Athena editor-surface observations are limited to what the what-is and querying pages document.

## Product Observations

### Snowflake Snowsight (worksheets)

Evidence layer: A (directly observed from official docs).

Key observations:

- **Positioning**: Snowsight is "a unified experience for working with your Snowflake data by using SQL or Python"; worksheets are where you "write and run SQL queries".
- **Worksheet as unit of work**: a worksheet holds SQL statements; worksheet context (database + optional schema) lets queries reference objects without full qualification; multiple statements run sequentially (Run single query via cursor placement, or Run All).
- **Editing affordances**: autocomplete (syntax keywords, functions, aliases — Snowflake tracks table aliases — and table/column values); query formatting; keyboard shortcuts; import SQL from file (appended to worksheet).
- **Object browsing**: Databases explorer — browse/search databases/schemas/objects, pin objects, "Place Name in Editor" (inserts fully qualified name), "Add Columns in Editor" (inserts comma-separated column names).
- **AI assist**: Snowflake Copilot — LLM assistant for exploring datasets, generating and refining queries in natural language.
- **Results**: displayed as a table with spreadsheet-like keyboard navigation; select/copy cells, rows, ranges; **contextual statistics** for selections (filled/empty meters; histograms for date/time/numeric; frequency distributions for categorical; email-domain distributions; JSON key distributions) for up to 1 million rows; **Chart** view of results; results are cached; some accounts see results limited to 10,000 rows.
- **Cost-bearing interactions**: some result transformations (e.g., sorting all rows) incur compute cost billed to the warehouse that ran the query; identifiable in query history via `snowsight_transform_cte`; display-only formatting (thousands separators, percentages, precision, date formats) does not incur cost.
- **Query details**: duration, row count, completion time, quantity of data scanned, executing role, executing warehouse; some details retained only 14 days; query profile opens in a new tab.
- **Download**: results as CSV or TSV; no file-size limit.
- **Query history**: per-worksheet history (up to 25 queries over the last 14 days) with status (running/queued), time, duration, query ID; filterable by status/warehouse/SQL text/query ID/duration; account-level Query History page also exists (Activity).
- **Sharing/roles**: worksheets organized in folders and shareable; running a shared worksheet requires the same role as the worksheet (or duplicating it); `USE ROLE` can switch roles mid-worksheet.
- **Adjacent surfaces in the same web platform**: notebooks, dashboards, Streamlit apps, data marketplace listings, plus admin surfaces (users, roles, cost management, Trust Center) — the worksheet is one surface of a broader platform UI.

### Databricks SQL editor

Evidence layer: A (directly observed from official docs).

Key observations:

- **Positioning**: "The Databricks UI includes a SQL editor that you can use to write queries, collaborate with colleagues, find available data, and create visualizations." Databricks SQL is "a cloud data warehouse built on lakehouse architecture" running on SQL warehouses.
- **Editor as workspace object**: opens to the last open query; queries are persistent workspace objects organized in the workspace file system; version history of changes; code comments for collaboration; **real-time collaborative editing** ("edit them together in real time"); results shared with all collaborators and limited to 64,000 rows.
- **Editing affordances**: code collapse for large files; command palette (actions, shortcuts, themes); customizable SQL auto-formatting; keyboard shortcuts; catalog and schema selectors; workspace file browser inside the editor.
- **AI assist**: Genie Code — chat to write, refine, or understand queries; generated code runnable from the side pane.
- **Parameters**: named parameter markers with configurable parameter widgets (query-based dropdown lists unsupported in the new editor).
- **Results**: explore, visualize, download, filter; multiple result sets for multi-statement runs.
- **Observability**: Query history page (past runs, execution times, resource usage across the warehouse); Query profile (inspect the execution plan for bottlenecks); Query performance insights (automatic insights and recommendations for inefficient queries).
- **Surrounding structure**: Jobs (schedule SQL queries as jobs); Alerts (monitor query results, evaluate conditions, deliver notifications); AI/BI Dashboards; Metric views (semantic layer for consistent business metrics reused across queries and dashboards); REST API to automate and manage SQL objects; notebooks can attach to SQL warehouses to run SQL alongside Python/Scala/R.
- **Editor migration**: new SQL editor replacing the legacy editor (workspace-level opt-out being removed; legacy retirement announced) — evidence that the editor surface itself is a productized, versioned component.

### Amazon Athena

Evidence layer: A for service positioning and results/history behavior; editor-surface specifics not directly observed (console page empty).

Key observations:

- **Positioning**: "an interactive query service that makes it easy to analyze data directly in Amazon S3 using standard SQL… begin using standard SQL to run ad-hoc queries and get results in seconds." Serverless; pay only for queries run; scales automatically, running queries in parallel.
- **Results persistence**: every query's results and result metadata are automatically stored in a query result location in Amazon S3 — either a customer-owned bucket (full control over storage/permissions/lifecycle/retention) or a managed query results option (service-managed storage and cleanup after a retention period). Results downloadable directly from the console.
- **Permission model**: viewing output files requires S3 GetObject on the result location plus Athena GetQueryResults; encrypted result locations require key permissions; S3 GetObject alone is sufficient to retrieve results (documented as an important caveat).
- **Failure semantics**: canceled/failed queries may leave partial results in S3; Athena does not delete partial results; multipart-upload cleanup recommended via bucket lifecycle policy; automatic retries may mark a query Completed after partial writes.
- **History**: recent queries view in the console; download multiple recent queries to CSV; configurable display options; history retained 45 days by default with an option to keep it longer.
- **Adjacent surface**: Apache Spark notebooks in the console (separate mode for Python Spark work).

### Amazon Redshift query editor (v1 and v2)

Evidence layer: A (directly observed from official docs).

Key observations:

- **v1 (console editor)**: run single SQL statement queries; download result sets up to 100 MB as CSV; save queries for reuse (region-dependent availability); view query runtime details for user-defined tables; schedule queries to run at a future time; view a history of queries created in the editor; runs via the Redshift Data API with IAM-managed permissions (statement-owner requirement; Secrets Manager for DB connections).
- **v1 limits** (documented): max query duration 24 hours; max result size 100 MB; results retained 24 hours; max statement size 100 KB; saved queries up to 3,000 characters; no transactions in the editor; cluster must be VPC-based.
- **v2**: "a separate web-based SQL client application that you use to author and run queries on your Amazon Redshift data warehouse… primarily used to edit and run queries, visualize results, and share your work with your team." Can also create databases, schemas, tables, and UDFs; tree-view panel per database showing schemas, tables, views, UDFs, stored procedures; replaces v1.
- **Significance for the Type**: v2's self-description ("web-based SQL client application") shows the Type's surface can be a standalone client, not only a portal pane — the binding to the platform's data is the constant, not the embedding.

### Microsoft Fabric SQL query editor

Evidence layer: A (directly observed from official Microsoft Learn docs).

Key observations:

- **Scope**: applies to SQL analytics endpoint, Warehouse, and Mirrored Database in Microsoft Fabric; "a text editor to write queries by using T-SQL" in the Fabric portal.
- **Editing affordances**: IntelliSense, code completion, syntax highlighting, client-side parsing and validation; SQL templates dropdown populating T-SQL object templates; auto-save every few seconds with a saving indicator; full keyboard-shortcut set (run, cancel, find/replace, comment, Copilot actions).
- **Execution semantics**: Run executes the query; each Run opens a separate session closed at execution end — session context is not maintained across runs; each Run is an independent batch request; TCL limitations (BEGIN TRAN in one run cannot be committed in the next); `GO` creates a new independent batch; `USE` must be submitted as a single request; DDL/DML/DCL supported.
- **Results**: grid preview showing the first 10,000 rows for larger result sets; in-grid string search; Messages tab for SQL messages; status bar with query status, duration, rows and columns returned; multiple result sets selectable via dropdown.
- **Result actions** (enabled by highlighting a SELECT): Save as view (creates a view, appears in Explorer); Save as table (CTAS into a chosen warehouse/schema/table); Open in Excel (downloads a live-query workbook); Explore this data (side-by-side matrix/visual ad-hoc exploration in Power BI service); Visualize results (build reports from results inside the editor; ORDER BY queries unsupported); Copy (with/without column names).
- **Cross-warehouse querying**: three-part naming to join across warehouses.
- **Background execution**: closing a tab with a running query prompts keep-running-in-background (with completion notification) or cancel.
- **AI assist**: Copilot — Explain query, Fix query shortcuts, Copilot chat pane.
- **Adjacent surfaces**: Visual query editor (graphical query building), Data preview, modeling tab, semantic model creation, Monitor hub — the SQL editor is one surface of the platform's warehouse experience.

## Cross-product Comparison

| Dimension | Snowsight worksheets | Databricks SQL editor | Athena console | Redshift QE v2 | Fabric SQL editor | Verdict |
|---|---|---|---|---|---|---|
| SQL text editor as primary authoring surface | Yes | Yes | Yes (console editor) | Yes | Yes (T-SQL) | **L0** |
| Bound to one analytical data platform's data | Yes (Snowflake) | Yes (lakehouse / Unity Catalog) | Yes (S3 + catalogs) | Yes (Redshift) | Yes (Fabric warehouse/endpoint) | **L0** |
| Immediate execution in the user's session | Yes | Yes | Yes ("results in seconds") | Yes | Yes | **L0** |
| Result grid | Yes | Yes | Yes (console/S3) | Yes | Yes (10k preview) | **L0** |
| In-place edit-and-re-run refinement | Yes | Yes | Yes | Yes | Yes | **L0** |
| Charts/visualization from results | Yes (Chart) | Yes (visualize) | Not observed | Yes ("visualize results") | Yes (Visualize/Explore) | L1 |
| Saved/persistent query artifacts | Yes (worksheets, folders) | Yes (queries as workspace objects) | Yes (saved queries; not deep-fetched) | Yes (v1 save; v2 shared) | Yes (auto-saved tabs) | L1 |
| Query history | Yes (per-worksheet + account) | Yes (history page) | Yes (recent queries, 45-day default) | Yes (v1 history) | Not observed as page | L1 |
| Download/export results | Yes (CSV/TSV, no cap) | Yes | Yes (S3 + console CSV) | Yes (CSV ≤100 MB v1) | Yes (Excel/copy) | L1 |
| Save results as DB objects (view/table) | Not observed | Not observed | Not observed | Not observed (DDL via editor) | Yes (Save as view/table) | L1/L2 |
| Query observability (duration/scanned/profile) | Yes (details + profile + stats) | Yes (history/profile/insights) | Partial | Yes (runtime details) | Yes (status bar) | L1 |
| Cost visibility | Yes (data scanned; transform cost) | Yes (resource usage) | Yes (pay-per-query model) | Partial | Partial | L1/L2 |
| AI/NL assistance | Yes (Copilot) | Yes (Genie Code) | Not observed | Not observed | Yes (Copilot explain/fix) | L1 (mode) |
| Scheduling queries as jobs | Not observed in editor (Tasks elsewhere) | Yes (Jobs) | Not observed (Athena scheduled queries exist; not fetched) | Yes (v1 schedule) | Not observed in editor | L1/L2 |
| Alerts on query results | Not observed | Yes | Not observed | Not observed | Not observed | L2 |
| Sharing/collaboration | Yes (shared worksheets/folders, role-gated) | Yes (real-time co-edit, comments, shared results) | Not observed | Yes ("share your work") | Partial (auto-save; no co-edit observed) | L1/L2 |
| Schema/object browsing | Yes (Databases explorer, pin, insert names/columns) | Yes (catalog/schema selectors, workspace browser) | Not observed | Yes (tree-view) | Yes (Explorer) | L1 |
| Autocomplete/highlighting/formatting | Yes | Yes (custom format) | Not observed | Not observed | Yes (IntelliSense) | L1 |
| Parameters/parameter widgets | Not observed | Yes (named markers + widgets) | Not observed | Not observed | Not observed | L2 |
| Background execution with notification | Not observed | Not observed | Not observed | Not observed | Yes (keep running on close) | L2 |
| Multi-statement scripts | Yes (Run All) | Yes (multi-statement) | Not observed | Yes (statements) | Yes (batches; GO) | L1 |
| Session/batch semantics documented | Partial (role context) | Not observed | Not observed | Partial (no transactions v1) | Yes (per-run session) | L2 |
| DDL/admin from the editor | Partial (Load Data; admin surfaces elsewhere) | Partial | Not observed | Yes (create DB/schemas/tables/UDFs) | Partial (templates; modeling tab) | L2 |
| Platform-integrated surface (portal/console/sidebar) | Yes | Yes | Yes | No — standalone web client | Yes (portal) | L1 (common, not definitional) |
| Sibling surfaces in the same product | Notebooks, dashboards, Streamlit, admin | Notebooks, dashboards, alerts, metric views | Spark notebooks | — | Visual query editor, data preview, modeling, semantic models | L2 |

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the product stops being an Analytical Query Editor:

```text
Connected analytical data platform (cloud warehouse / lakehouse / analytical query service)
└── Query editor surface for composing analytical queries (SQL or the platform's query language)
    └── Immediate execution of the composed query against that platform's data
        └── Result returned as a data grid
            └── In-place edit-and-re-run refinement
```

Five properties:

1. **Bound to a specific analytical data platform** — the editor operates on one platform's analytical data (its warehouse, lakehouse, or query service), not on arbitrary user-collected datasets and not on any database via generic connections. Without this, the product is a general SQL client / database IDE.
2. **Query editor surface (SQL-first)** — a text editor for composing query statements/scripts in the platform's SQL dialect, with editing affordances. The unit of work is the query, authored by the user. Without this, the product is a dashboard/report viewer or a question-answering surface.
3. **Immediate execution** — the query runs now, in the user's session; results return in seconds-to-minutes; long-running analytical queries are a normal case (some products let runs continue in the background). Without this, it is batch/scheduled processing.
4. **Result grid** — the answer is a tabular result set the user can inspect directly (commonly with preview caps). Without this, it is a query API/CLI.
5. **In-place refinement** — the user edits the query and re-runs in the same surface. Without this, it is a one-shot execution tool.

Removal tests:

- Remove the editor (predefined questions/GUI-only composition) → Ad-hoc Query Application / BI territory
- Remove the analytical-platform binding (generic multi-DB connections) → SQL Client / Database IDE territory
- Remove query authoring (administration only) → Database Management Console territory
- Remove the result grid (API/CLI only) → developer tooling, not an editor application
- Remove refinement → one-shot execution utility

### L1 — Common Mature Structure

Present in most mature products; expected by the market but not definitional:

- saved/persistent query artifacts (worksheets, queries as named objects, saved queries) with organization (folders, workspace)
- query history (per-surface and account-level; retention windows vary by product)
- charts/visualization generated from query results
- download/export of results (CSV/TSV/Excel; size caps vary)
- schema/object browsing (tree/explorer; insert object/column names into the editor)
- autocomplete/completion, syntax highlighting, formatting, keyboard shortcuts
- sharing/collaboration on queries (shared worksheets/queries; real-time co-edit in one sampled product)
- query observability: duration, row counts, data scanned, query profile/execution plan, performance insights
- AI/NL assistance for writing, explaining, and fixing queries (now common across the sample)
- multi-statement scripts with run-all semantics
- cost visibility (data scanned, compute cost of queries and even of some result interactions)
- scheduling queries as jobs (observed directly in 2 of 5; category-common)

### L2 — Variant / Optional Structure

Depends on platform, segment, maturity:

- parameters/parameter widgets in queries
- saving results as database objects (views, CTAS tables)
- background execution with completion notification
- documented session/batch semantics (per-run sessions, transaction limits)
- DDL/administration from the editor (create databases/schemas/tables/UDFs)
- sibling surfaces in the same product: notebooks (SQL/Python), dashboards, visual query editors, data previews, semantic layers/metric views
- alerts on query results
- REST/programmatic access to the same query objects
- result persistence substrate outside the grid (e.g., service-managed or customer-owned result storage)
- result/preview row caps and retention windows (product-specific values)
- editor versioning/migration programs (legacy → new editor)

### L3 — Vendor-specific Structure

Stays in Research Notes only:

- Snowflake: per-worksheet query history (25 queries / 14 days); contextual statistics (histograms, frequency/email-domain/JSON-key distributions, up to 1M rows); transform-cost billing identifiable via `snowsight_transform_cte`; role-gated shared worksheets (`USE ROLE`); pinned objects; "Place Name in Editor"/"Add Columns in Editor"; 10,000-row cap for government/VPS/private-connectivity accounts; Copilot
- Databricks: new-vs-legacy editor migration program; 64,000-row shared results; Genie Code; named parameter markers + widgets (query-based dropdown lists unsupported in the new editor); command palette; code comments; version history; real-time co-edit; query profile + performance insights; AI/BI dashboards; metric views; Unity Catalog; REST API
- Athena: S3 query result location (customer bucket vs managed results); IAM GetObject/GetQueryResults split (GetObject alone suffices to read results — documented caveat); partial results on failure + multipart-upload cleanup guidance; 45-day default history; multi-query CSV download
- Redshift: v1 limits (24 h duration, 100 MB results, 24 h result retention, 100 KB statement, 3,000-char saved queries, no transactions, region-dependent save availability); v2 as standalone web client with tree-view and DB-object creation
- Fabric: per-run session/batch semantics (TCL/GO/USE limitations documented); 10,000-row results preview; Save as view/table (CTAS); Open in Excel live-query flow; Explore this data (Power BI); Visualize results (no ORDER BY); Copilot shortcuts; auto-save indicator; keep-running-on-close choice; cross-warehouse three-part naming

### Anti-overfitting Check

- **Charts from results are near-universal** → tempting for L0. Rejected: Redshift v1 is documented without charts and is still squarely this Type; the defining act is authoring and running queries, not visualizing. L1.
- **AI assistants are now common (3 of 5)** → rejected for L0 and for definitional status: one authoring aid over the same loop; older editors without AI still satisfy the Type. L1.
- **Platform-portal integration is nearly universal** → rejected for L0: Redshift QE v2 is explicitly "a separate web-based SQL client application". The constant is the binding to the platform's data, not the embedding. L1.
- **Saved queries/history are universal** → but the pure authoring loop can exist without persistence; persistence is what turns queries into organizational assets. L1.
- **SQL as the language** → universal in the sample (ANSI SQL, T-SQL, dialects). The Type name does not logically require SQL, but every observed product is SQL-based; phrased as "SQL or the platform's query language" with SQL as the observed universal.
- **Collaboration** → only some products (real-time co-edit in one); L1/L2, not definitional.

### Historical / Market-Sample Check

- Standalone warehouse query clients of earlier eras (e.g., ODBC/JDBC query tools aimed at Teradata/other warehouses — Teradata SQL Assistant-style products): editor + warehouse binding + grid + refine, without platform-portal integration, AI, sharing, or profiles. They satisfy the L0. ✓ (category-level inference from product knowledge, not directly fetched — marked as inference)
- Generic multi-DB SQL clients (DBeaver, DataGrip, SQL Workbench/J): can run analytical queries but are connection-agnostic general database tooling → belong to SQL Client / Database IDE, not this leaf. The binding test separates them. ✓
- The definition does not depend on web vs desktop (Redshift v2 is a web client; historical clients were desktop), on cloud vs on-premises, or on a specific SQL dialect. ✓
- The definition does not require the editor to be part of a bigger platform UI, though in the current market it almost always is. ✓

## Vendor-specific Findings

See L3 above. Additionally:

- Snowflake documents that some *result-viewing interactions* (sorting all rows) incur compute cost — an unusual cost-bearing UX rule, product-specific.
- Databricks documents that query results are shared with all collaborators and capped (64,000 rows) — collaboration and result caps fused.
- Athena documents a security-relevant caveat: S3 GetObject on the result location alone is sufficient to read query results even if Athena GetQueryResults is denied — the result substrate is a real access-control surface.
- Fabric documents per-run session semantics in unusual depth (transactions, GO, USE) — evidence that the editor's execution model is a first-class product behavior, not an implementation detail.
- Redshift v1 documents region-dependent feature availability (saving queries) — regional variation exists even inside one product.

## Boundary Findings

### vs SQL Workbench (sibling leaf, §13, unprocessed)

The ad-hoc pass already flagged this trio (ad-hoc / SQL workbench / analytical query editor) as an audience/abstraction gradient. From this sample:

- Analytical Query Editor: bound to one analytical data platform; the platform's own (or platform-native) query surface; analytical workload framing (results at scale with caps, data-scanned/cost observability, query profiles, history, sharing); audience = the platform's data practitioners.
- SQL Workbench (expected): general-purpose SQL surface across databases/connections; not bound to one platform; general database work framing.
- Products blur the vocabulary: Redshift QE v2 calls itself "a web-based SQL client application" — the words overlap; the platform binding and analytical framing are what differ.
- **Test**: bind the editor to one analytical platform's data and add analytical-result affordances → this Type; make it connection-agnostic multi-DB tooling → SQL Workbench / SQL Client. → Flag for joint review when SQL Workbench is processed.

### vs Ad-hoc Query Application (processed sibling; joint-review flag discharged from this side)

- Shared: the compose → run → result → refine loop.
- Differences: audience (data practitioners vs business users); authoring abstraction (SQL statement/script vs question built via GUI/search/NL); data substrate (raw analytical platform data vs governed data spaces/semantic layers); result treatment (grid + export + save-as-object vs saved shareable questions feeding dashboards); observability emphasis (query profile/cost vs data permissions/governance).
- Products blur: Fabric's "Explore this data" hands query results to Power BI ad-hoc exploration; Databricks/AWS editors schedule queries and raise alerts like BI tools; conversely Metabase embeds a full SQL editor (recorded in the ad-hoc research).
- **Test**: strip the governed question layer and hand the user a SQL editor on raw analytical data → this Type; wrap the SQL editor in a governed question layer with saved shareable questions → Ad-hoc Query Application. The gradient recorded in the ad-hoc pass is confirmed from this side; the two Types remain distinct on audience + authoring abstraction + substrate.

### vs Database Management Console (sibling leaf, §13, unprocessed)

- The editor authors and runs queries; the console administers the database/instance (users, roles, warehouses/compute, cost, replication, security). Snowsight includes admin surfaces but the worksheet remains the query surface; Redshift QE v2 can create DB objects but its primary purpose is authoring/running queries.
- **Test**: remove query authoring (administration only) → management console; remove administration (authoring only) → this Type. → Flag for joint review when Database Management Console is processed.

### vs Database IDE / SQL Client (§12)

- Those are development tools across databases (schema design, debugging, refactoring, many connection types). This Type is the analytics platform's own query surface for analytical work. Editor mechanics overlap; binding and purpose differ.

### vs Business Intelligence Platform / Dashboard Platform

- Editors produce queries and result sets; BI platforms curate persistent artifacts (dashboards/reports) for consumption and distribution. In the sample, editors feed BI surfaces (Databricks AI/BI dashboards, Snowsight dashboards, Fabric Visualize/Explore) but the editor's center of gravity stays query authoring.

### vs Data Science Workbench

- Notebooks (Python/R) for modeling/statistics vs SQL query editing. The platforms themselves ship both as sibling surfaces (Snowflake notebooks, Databricks notebooks, Athena Spark notebooks) — adjacent, not the same Type.

## Uncertainties

1. **BigQuery not researched** (cloud.google.com timeout ×2) — a canonical warehouse query editor; the pattern is covered by four other ecosystems, but BigQuery-specific structure (e.g., Studio, Data Canvas) is unverified.
2. **ClickHouse Cloud SQL console not researched** (404).
3. **Athena editor-surface specifics** (tab layout, saved-queries UI, workgroups) not directly observed — the console page returned an empty shell; Athena evidence is service/results/history level.
4. **Audience claims** (data analysts/engineers) are inferred from product positioning and feature framing (sharing, profiles, cost observability), not from explicit audience statements in every doc — kept moderate in the final document.
5. **Historical standalone warehouse clients** not directly researched; the historical check is category-level inference, marked as such.
6. **Precise operational limits** (row caps, retention windows, size caps, durations) are product-specific and documented per product in Research Notes only; none are asserted in the final document.
7. **SQL Workbench and Database Management Console leaves are unprocessed** — boundaries recorded here for joint review; no unilateral taxonomy change made.

## Final Synthesis

An Analytical Query Editor is best modeled as **the query-authoring surface of an analytical data platform**:

```text
Open the platform's query editor (worksheet / query tab / editor pane)
→ compose a query in the platform's SQL dialect (completion, formatting, AI assist)
→ run it (single statement or script) against the platform's analytical data
→ read the result grid (inspect, chart, download)
→ refine and re-run in place
→ persist the work: saved query/worksheet, history, sharing, scheduling, save results as objects
```

The defining core is deliberately small: platform-bound analytical data + SQL-first editor + immediate execution + result grid + refinement loop. Everything else the market associates with these editors — charts, history, sharing, AI assistants, scheduling, query profiles, parameters, save-as-object — is common mature or variant structure, not definition.

The Type's market reality: the editor is almost always one surface of a larger analytical platform UI (alongside notebooks, dashboards, catalogs, admin consoles), and the boundary to SQL Workbench (general SQL tooling) and to Ad-hoc Query Application (governed question loop) is a binding/audience/abstraction gradient rather than a wall — recorded as boundary issues for joint review.
