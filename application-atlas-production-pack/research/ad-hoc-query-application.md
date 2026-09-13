# Research Notes — Ad-hoc Query Application

## Research Goal

Understand what an Ad-hoc Query Application actually is as an Application Type: its defining structure, its standard workflow, its interfaces, its rules, and its boundaries against neighboring Types (SQL Workbench, Analytical Query Editor, Business Intelligence Platform, Dashboard Platform, Reporting Platform, Data Visualization Application, OLAP Platform, Data Explorer, Data Science Workbench).

## Initial Boundary

Initial hypothesis (pre-research):

- Core use: let a user pose a one-off question to data at the moment the question arises — compose a query interactively, run it immediately, read the result, refine.
- Primary users: business users (self-service), analysts; data engineers/admins govern the data side.
- Nearest neighbors: SQL Workbench / Analytical Query Editor / Database Management Console (developer-facing query authoring); Business Intelligence Platform / Dashboard Platform / Reporting Platform (persistent curated artifacts); Data Visualization Application; OLAP / Multidimensional Analytics Platform; Data Explorer / Public Data Portal (published datasets).
- Likely confusion #1: "ad-hoc query" is historically a *capability* of BI suites (Cognos QueryStudio, BusinessObjects, Brio) — is the leaf an independent Type or a capability?
- Likely confusion #2: the boundary vs SQL Workbench / Analytical Query Editor (both separate leaves in the same directory section) may be an audience/abstraction gradient rather than a structural wall.

## Research Questions

1. What is the core object? (query / question / search / answer / report)
2. How does a user compose a query? (GUI step builder, drag-and-drop field wells, search bar, natural language, SQL)
3. What data does it run against? (live connection, extract/import, semantic model, uploads)
4. What is the interaction loop? (ask → result → refine → save/share?)
5. What happens to results? (ephemeral vs saved artifact; export; pin to dashboard; alerts)
6. What roles use it, and how do permissions shape what can be asked?
7. What rules/constraints matter? (data permissions, row/column security, query load management, drill-through availability)
8. Where is the boundary vs SQL Workbench, BI Platform, Dashboard/Reporting Platform, Data Visualization, OLAP, Data Explorer?
9. Historical check: do classic ad-hoc query tools (Cognos QueryStudio-era, Brio, BusinessObjects Web Intelligence) and SQL workbenches still fit the definition?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Philosophy / Tier | Why selected |
|---|---|---|
| Metabase | Question-builder-first; open-source + cloud; self-serve BI for teams | The purest "ad-hoc question" framing: the core object is literally named "Question"; GUI builder + SQL editor + AI |
| ThoughtSpot | Search-first analytics; enterprise SaaS (+ on-prem software) | Search/natural-language as the primary query surface; governed semantic layer; AI agents |
| Power BI | Desktop-authored self-service BI inside a platform ecosystem; Microsoft tier | Market-leading authoring surface (field drag + visual pane) + Q&A natural language; shows the Type bundled in a BI platform |
| Zoho Analytics | Drag-and-drop report designer; mid-market self-service BI | Closest modern descendant of the classic "ad-hoc query/report designer" style; Query Tables (SQL) + Ask Zia (NL) |

Note: Tableau (visual-analysis pioneer) and Apache Superset (SQL-Lab engineering-first) were originally targeted but their documentation could not be reached from this environment (see Sources — limitations). The four sampled products still cover the four main authoring philosophies (step builder, search/NL, field-drag, drag-and-drop designer) and three customer tiers.

## Sources

Research date: 2026-09-06.

### Metabase (Tier 1 — official documentation site)

- Questions overview: https://www.metabase.com/docs/latest/questions/start
- Question introduction: https://www.metabase.com/docs/latest/questions/introduction
- The query builder: https://www.metabase.com/docs/latest/questions/query-builder/editor
- Full docs TOC captured from the same pages (query builder steps, native/SQL editor, visualizations, dashboards, data modeling: models/metrics/segments, permissions: data/row-and-column-security, caching, alerts, exporting, embedding).

### ThoughtSpot (Tier 1 — official documentation site)

- Documentation index (llms.txt): https://docs.thoughtspot.com/llms.txt
- Cloud docs root: https://docs.thoughtspot.com/cloud/latest/
- Answer experience: https://docs.thoughtspot.com/cloud/26.8.0.cl/answer-experience-new.md
- Index entries used: Answers ("A saved search that can be used in a Liveboard"), Liveboards, Views ("A saved SQL query or search-based dataset… used as a source for further analysis, just like a physical table"), Semantic layer, Spotter agents, SpotIQ, Monitor KPIs, Analyst Studio, Data Workspace.

### Power BI (Tier 1 — official Microsoft Learn documentation)

- What is Power BI: https://learn.microsoft.com/en-us/power-bi/fundamentals/desktop-what-is-desktop
- Get started with Power BI Desktop: https://learn.microsoft.com/en-us/power-bi/fundamentals/desktop-getting-started
- (Both pages fetched 2026-09-06; service-side ad-hoc behaviors only partially covered.)

### Zoho Analytics (Tier 1 — official help center)

- Help center root: https://www.zoho.com/analytics/help/
- User Guide overview (full TOC): https://www.zoho.com/analytics/help/overview.html
- Creating Reports: https://www.zoho.com/analytics/help/creating-reports.html
- TOC entries used: Workspaces, Tables, Query Tables, Creating Reports (Charts/Pivot/Summary/Tabular), Dashboards, Ask Zia, Sharing/Publishing/Export.

### Source-access limitations

- **Tableau**: help.tableau.com returned 404 on both attempted URLs (getstarted.htm, section root). Abandoned after 2 failures per network rule. Tableau is acknowledged as a canonical ad-hoc visual-analysis product but was NOT directly researched; no Tableau-specific claims are made in either file.
- **Apache Superset**: superset.apache.org/docs returned empty twice; raw.githubusercontent.com timed out once. Abandoned. Superset's SQL Lab (SQL-first ad-hoc surface) is therefore represented in this research only indirectly, via Metabase's native SQL editor.
- **Looker**: cloud.google.com/looker/docs timed out twice. Abandoned. The "governed semantic layer" philosophy is covered via ThoughtSpot's semantic layer/Models instead.
- **Zoho Analytics**: ad-hoc-reporting.html 404'd; help root and User Guide overview succeeded. Zoho observations are from the help TOC + Creating Reports page (positioning + report-type level), not from deep per-feature pages.

## Product Observations

### Metabase

Evidence layer: A (directly observed from official docs).

Key observations:

- **Core object = "Question"**: "Questions in Metabase are queries, their results, and their visualization. Questions are the basic analytical unit in Metabase." A question can be saved, organized into collections and dashboards, embedded, shared by link, exported, and set to alert.
- **Three authoring modes**: graphical query builder (+ New > Question), native/SQL query editor (+ New > SQL query — "native" because non-SQL databases like MongoDB are supported), and Metabot (natural language; generates charts and queries).
- **Query builder steps** (documented): Pick data (table from a database, a model, a metric, or another saved question; searchable/browseable data picker) → Join tables → Custom columns (spreadsheet-like expressions; not persisted to the underlying table) → Filter → Summarize and group (built-in aggregations + custom expressions) → Sort → Row limit → Visualize (auto-picks a visualization; user can change).
- **Preview at every step**: a Preview button shows the first 10 rows of results up to that step — the refinement loop is built into the editor.
- **Transparency of the generated query**: "Under the hood, all Metabase questions are converted to SQL or another language native to your query engine"; a View SQL button shows it; conversion of a builder question to SQL is possible and one-way (SQL cannot convert back to builder).
- **Drill-through**: clicking chart elements/column headings opens a drill menu (options depend on what is clicked); full drill menu only for query-builder questions; SQL questions have limited drill actions. Explorations can be saved as new questions.
- **Saved artifact lifecycle**: save to a dashboard (visible only there) or a collection (reusable across dashboards); info sidesheet (description, creator, last editor, source data, entity ID); history; bookmark; verification (content verification); delete/restore; can be turned into a "Model" (a curated starting point for new questions); breaking-change detection on save (Pro/Enterprise).
- **Queries as data sources**: saved questions and models can be picked as the data source of new questions; native queries can reference saved questions.
- **Governance**: data permissions (separate query-builder vs native-query permissions), row and column security, collection permissions, impersonation, database routing; snippet folders with permissions; hiding columns explicitly documented as NOT a security mechanism.
- **Operational behaviors**: caching of question results (per-question policy, paid tiers), alerts (scheduled or "when something interesting happens"), exports, usage analytics, uploads (CSV), writable connections and actions (write-back).

### ThoughtSpot

Evidence layer: A (directly observed from official docs index + Answer experience page).

Key observations:

- **Positioning**: "AI-powered analytics that puts self-service analysis in the hands of everyone in your organization—no SQL or data expertise required"; "a business intelligence and analytics platform that leverages Search and AI (Spotter) for data exploration."
- **Core object = "Answer"**: defined in the docs index as "A saved search that can be used in a Liveboard." The search bar is the primary query surface; a search becomes an Answer when saved.
- **Answer experience features** (documented): formula editor; table column summaries/headlines (each headline summary executes one SQL query against the underlying database); table/chart configuration panels; conditional formatting; KPI chart type; Monitor (notifications when a KPI meets a threshold, or scheduled); pivot tables with multi-sort; **undo/redo/reset buttons next to the search bar** ("each time you make a change in a search or saved Answer — for example, when you add a new column to the search, drill down, or sort"); drill down on data points (including by measure); SpotIQ auto-analysis of Answer data points; learning cards; HTML in titles; download footer (admin-configured).
- **Join-path rule**: when searching on columns with more than one possible join path, the user can no longer resolve the path inside the search — the system prompts to create a Model with the correct join path. (Governed semantic layer shapes what is askable.)
- **Surrounding structure**: Liveboards (dashboards of charts/tables/headlines); Collections (organizational containers); Views ("a saved SQL query or search-based dataset… used as a source for further analysis, just like a physical table"); Models + semantic layer (governed, AI-native); Data Workspace (warehouse connections + modeling); Analyst Studio (data prep); TML (text representation of objects for version control/migration); SpotIQ (automated insight surfacing); Monitor KPIs; plug-ins (Sheets/Excel/PowerPoint/Teams/Slack); embedded analytics; AgentSpot (AI agents).
- **Spotter agents** (current generation): Spotter ("discover insights from your data just by asking"), SpotterModel (prompts → data models), SpotterViz (questions → Liveboards), SpotterCode (IDE coding).

### Power BI

Evidence layer: A (directly observed from official Microsoft Learn pages).

Key observations:

- **Positioning**: "Microsoft's business analytics platform"; Power BI Desktop = "a free Windows application that lets you connect to data, transform it, and create interactive visual reports"; the service = publishing/sharing/collaboration; part of Microsoft Fabric.
- **Authoring workflow** (documented): Get Data (Excel/databases/web/100+ sources) → Power Query Editor (transform: remove columns, filter rows, change types; Close & Apply) → data model (relationships, DAX, calculated columns) → build visuals: check fields in the Fields pane (a visual is created automatically), change type in the Visualizations pane, drag fields into Values/Axis/Legend wells → arrange visuals on the report canvas → save (.pbix) → Publish to the service.
- **The ad-hoc loop inside authoring**: selecting fields immediately renders a visual; the user filters, sorts, drills, and re-arranges interactively ("Explore and analyze: Filter, sort, and drill down to find insights").
- **Q&A (natural language)**: "Ask natural language questions like 'What were sales by region?' and get instant visuals"; listed as a Power BI (not Fabric-shared) feature alongside Smart Narratives (auto text summaries).
- **Governance/operations**: workspaces, apps for distribution, shared datasets, scheduled refresh, email subscriptions, alerts, RLS (row-level security), sensitivity labels, usage metrics, audit logs; paginated reports (Report Builder) and Report Server (on-prem) as separate artifacts; Direct Lake mode (query OneLake without import/caching).

### Zoho Analytics

Evidence layer: A for the help-TOC structure and Creating Reports page; positioning-level for features not deep-fetched.

Key observations:

- **Positioning**: "self-service BI and data analytics software"; "intuitive drag and drop interface… create reports with ease."
- **Structure**: Workspace (logical grouping of data sets stored as Tables + the reports/dashboards created over them) → Tables (columns with name + type; "reports will be plotted based on these columns") → Reports (Charts, Pivot Tables, Summary View, Tabular View; 75+ visualization types claimed) → Dashboards (reports + widgets + user filters + text).
- **Report creation**: drag-and-drop designer; per report type: create, apply filters, customize (axes, thresholds, palette, legend), work with; interactive elements: tooltips, drill downs ("explore data at different levels of granularity").
- **Alternative authoring modes**: Query Tables (SQL-based data preparation/merging; "a saved SQL query… used as a source… just like a physical table" analog in this product's TOC), formulas (custom metrics), Ask Zia (natural-language questions, conversational mode, training, visualization choice), Zia Insights (automated narration), auto-analysis, forecasting/trend/what-if.
- **Data acquisition**: files, feeds, cloud drives, cloud/local databases, Zoho apps, 40+ business-app connectors, API, direct entry.
- **Sharing/publishing**: share views to users/groups, enable shared users to create reports, embed, permalinks, public views, export (view/multiple/dashboard), email scheduling, templates, portals, white label, mobile apps.

## Cross-product Comparison

| Dimension | Metabase | ThoughtSpot | Power BI | Zoho Analytics | Verdict |
|---|---|---|---|---|---|
| Queryable data source connection | Yes (20+ DBs, uploads, cloud storage) | Yes (warehouse connections via Data Workspace) | Yes (100+ sources) | Yes (files, DBs, 40+ app connectors) | **L0** |
| User-composed query at question time | Yes (builder / SQL / Metabot) | Yes (search bar / Spotter) | Yes (field selection / Q&A) | Yes (drag-drop / Query Tables / Ask Zia) | **L0** |
| Immediate execution in the user's session | Yes (Visualize; per-step preview) | Yes (search runs live; undo/redo/reset) | Yes (visual renders on field selection) | Yes (report renders as fields are dropped) | **L0** |
| Result returned as table and/or chart | Yes (table default + 15+ viz types) | Yes (table + charts + KPI + pivot) | Yes (table + 30+ visuals) | Yes (Tabular/Summary + 75+ chart types) | **L0** (table OR chart; chart not required) |
| Interactive refinement loop | Yes (edit steps, drill-through, preview) | Yes (add columns, drill down, undo/redo/reset) | Yes (filter/sort/drill, re-drag fields) | Yes (filters, drill downs, re-drag) | **L0** |
| Saved query artifact | Yes ("Question") | Yes ("Answer" = saved search) | Yes (report/visual in .pbix) | Yes ("Report") | L1 |
| Dashboards composed from saved queries | Yes (dashboards) | Yes (Liveboards) | Yes (dashboards/reports in service) | Yes (dashboards) | L1 |
| Drill from result to finer detail | Yes (drill-through menus) | Yes (drill down incl. by measure) | Yes (drill down) | Yes (drill downs) | L1 |
| Natural-language query | Yes (Metabot) | Yes (Spotter; search bar) | Yes (Q&A) | Yes (Ask Zia) | L1 (mode, not definition) |
| SQL/native editor as alternative mode | Yes (native editor; one-way conversion) | Partial (Views = saved SQL; Analyst Studio for prep; search is the end-user surface) | No (DAX/M are modeling languages, not ad-hoc query) | Yes (Query Tables) | L1/L2 (mode availability varies) |
| Export/download results | Yes | Yes (download footer) | Yes | Yes | L1 |
| Alerts/monitoring on saved queries | Yes (alerts) | Yes (Monitor KPIs, watchlists) | Yes (alerts, subscriptions) | Yes (data alerts) | L1 |
| Result caching / query-load management | Yes (per-question caching) | Yes (headline-summary cost controls) | Yes (import mode, Direct Lake; scheduled refresh) | Yes (implied; not deep-fetched) | L1 |
| Data permissions / row-column security | Yes (data permissions, row/column security, impersonation) | Yes (admin console, privileges, orgs) | Yes (RLS, workspaces, sensitivity labels) | Yes (sharing to users/groups) | L1 |
| Formulas / custom columns / calculated fields | Yes (custom columns, custom expressions) | Yes (formula editor) | Yes (DAX calculated columns) | Yes (formula column) | L1 |
| Joining multiple tables/sources | Yes (join step; join saved questions) | Yes (join paths governed by Models) | Yes (relationships; composite models) | Yes (joining/linking tables) | L1 |
| Governed semantic layer (models/metrics) | Optional (models, metrics, metadata editing) | Yes (central: Models, semantic layer) | Yes (central: semantic model, DAX) | Light (table metadata, formulas) | L2 |
| Live connection vs imported/extracted data | Live (plus model persistence option) | Live (warehouse) | Both (import vs DirectQuery/Direct Lake) | Both (import + live connections) | L2 |
| Auto-analysis / AI insight surfacing | Yes (X-rays) | Yes (SpotIQ, Spotter) | Yes (Smart Narratives; Q&A) | Yes (Zia Insights, auto-analysis) | L2 |
| Embedded analytics / OEM | Yes (embedding SDK, public links) | Yes (developers docs) | Yes (embed) | Yes (white label, embed) | L2 |
| Write-back / actions on data | Yes (actions, writable connections) | Not observed | Not observed | Not observed | L2 (product-specific so far) |
| Version control of query artifacts | Partial (serialization, entity IDs) | Yes (TML) | Not observed (pbix is file-based) | Partial (templates) | L2 |
| Desktop-installed authoring app | No (web) | No (web) | Yes (Desktop) | No (web; on-prem available) | L2 |
| Deployment: cloud / self-host / on-prem | Cloud + self-host (OSS) | Cloud + on-prem software | Cloud service + Report Server | Cloud + on-premise | L2 |
| Query artifacts as data sources for new queries | Yes (saved questions, models) | Yes (Views) | Yes (shared datasets) | Yes (Query Tables, workspace tables) | L1 |

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the product stops being an Ad-hoc Query Application:

```text
Queryable data source (connected, user-authorized)
└── User-composed query (built at question time, not predefined)
    └── Immediate execution against the data
        └── Result returned to the user (table and/or visualization)
            └── Interactive refinement (adjust the query and re-run in place)
```

Five properties:

1. **Queryable data source** — a live connection to data the user is authorized to query (database, warehouse, dataset, uploaded file). Without it, there is nothing to ask.
2. **User-composed query at question time** — the query is constructed by the user in the moment the question arises, from the data's fields; it is not a predefined, IT-authored artifact being merely consumed. Without this, the product is a report/dashboard *viewer*.
3. **Immediate execution** — the query runs against the data now, within the user's session, and the answer comes back in seconds-to-minutes, not on a schedule. Without this, it is batch/scheduled reporting.
4. **Result presentation** — the answer is rendered for direct reading: a table and/or a chart. (A table alone satisfies this; charts are near-universal but not definitional.) Without this, it is a raw query API/CLI.
5. **Interactive refinement loop** — the user adjusts the query in the same surface (filter, regroup, drill, re-sort, change visualization) and re-runs. Without this, it is a one-shot export tool.

Removal tests:

- Remove user composition (queries predefined) → Reporting Platform / Dashboard Platform
- Remove immediacy (scheduled/batch) → scheduled reporting
- Remove refinement loop → static report viewer / export tool
- Remove result presentation → query API / CLI (developer tool territory)
- Remove data connection → nothing remains

### L1 — Common Mature Structure

Present in all or nearly all mature products; expected by the market but not definitional:

- saved query artifact (Question / Answer / report) with name, description, history, verification
- dashboards composed from saved queries
- drill-through / drill-down from a result to finer detail
- multiple authoring modes: GUI step builder, drag-and-drop field wells, search bar, natural-language assistant, SQL/native editor
- visualization choice beyond the default table
- export/download of results
- alerts/monitoring on saved queries
- formulas / custom columns / calculated fields
- joining multiple tables (or sources)
- saved queries usable as data sources for new queries
- data permissions + row/column-level security
- result caching / query-load management
- data source management (connections, sync, uploads)
- search/browse over available data (data picker, data reference)

### L2 — Variant / Optional Structure

Depends on segment, philosophy, deployment, maturity:

- governed semantic layer as the primary query substrate (models/metrics) vs raw tables
- live connection vs imported/extracted (in-memory) data
- desktop-installed authoring app vs web-only
- AI auto-analysis (automated insight surfacing, smart narratives)
- embedded analytics / OEM distribution
- write-back / actions on data
- version control of query artifacts (text serialization)
- multi-source / cross-database querying
- deployment: cloud / self-hosted / on-premises
- audience posture: business-user-first vs analyst-first vs engineer-first

### L3 — Vendor-specific Structure

Stays in Research Notes only:

- Metabase: "Question" as basic analytical unit; per-step preview (first 10 rows); one-way builder→SQL conversion; display row caps for unaggregated/aggregated queries (2,000/10,000 documented); breaking-change detection on save; entity IDs/serialization; snippet folders; models/metrics/segments; actions and writable connections; Metabot AI
- ThoughtSpot: Liveboards; Answers as saved searches; headline summaries (one SQL per summary; pinning requires manual re-enable due to query cost); join-path resolution pushed to Models; Spotter agent family (Spotter/SpotterModel/SpotterViz/SpotterCode); SpotIQ; Monitor KPIs + watchlists; TML; Analyst Studio; in-product undo/redo/reset
- Power BI: Power Query Editor (M); DAX; .pbix files; Fabric/OneLake/Direct Lake; workspaces/apps; paginated reports; Report Server; Q&A visual; Smart Narratives
- Zoho Analytics: Workspaces; Query Tables; Ask Zia (with training and conversational mode); 75+ chart types claim; Zia Insights; white-label; Zoho app connectors

### Anti-overfitting Check

- **Visualization is universal in the sample** → tempting to promote to L0. Rejected: classic ad-hoc query tools returned tables/cross-tabs only and were still ad-hoc query applications; the defining act is the question loop, not the chart. Charts = L1.
- **Dashboards are universal in the sample** → rejected for L0: dashboards are the defining structure of the Dashboard/BI Platform Types; for this Type they are downstream artifacts of saved queries. L1.
- **NLQ/AI is now universal in the sample** → rejected for L0 and even L1-as-definition: it is one authoring mode over the same loop; older products without it still satisfy the Type. Listed under authoring modes (L1) with AI insight surfacing as L2.
- **Semantic layer is central in 2 of 4** (ThoughtSpot, Power BI) → L2; Metabase treats it as optional modeling; a raw-tables ad-hoc query tool remains valid.
- **"Saved query" is universal** → but the pure ad-hoc act is ephemeral; saving is what turns the loop into organizational content (and is where the boundary with BI Platforms begins). L1, not L0.

### Historical / Market-Sample Check

- Classic ad-hoc query tools of the 1990s–2000s (Cognos Impromptu/QueryStudio, BusinessObjects, Brio Query, MicroStrategy desktop report editors): user picked tables/columns, joined, filtered, grouped, ran against the warehouse, read a table/cross-tab. They satisfy L0 with none of: NLQ, AI, dashboards, semantic layers, embedding. ✓
- SQL workbenches / query editors (developer-facing): satisfy the same loop (compose → run → result → refine) but centered on the SQL statement against a raw database, for a technical audience, with grid output. They fit the L0 loop — which is exactly why the boundary is an audience/abstraction gradient, recorded under Boundary Findings. ✓
- Spreadsheet pivot tables against a cube or data model: the same loop embedded in another Application Type — supporting the reading that the ad-hoc query loop is a portable structure and the standalone Type is the dedicated application. ✓
- The definition does not depend on web vs desktop, cloud vs on-prem, or live vs extracted data. ✓

## Vendor-specific Findings

See L3 above. Additionally:

- Metabase documents a security-relevant rule: hiding columns in visualization settings is explicitly NOT a security mechanism (viewers can unhide); exclusion must happen in the query's data step. (Product-specific rule; used as an example of the kind of rules this Type carries.)
- Metabase separates "query builder and native permissions" — the ability to use the GUI builder and the ability to write raw SQL are separately grantable. (Product-specific implementation of a general governance concern.)
- ThoughtSpot documents that headline summaries execute one SQL query each against the underlying database, and that multiple join paths must be resolved by creating a Model rather than inside the search. (Product-specific; illustrates governance-through-semantics.)
- Power BI's ad-hoc loop is embedded in a report-authoring artifact (.pbix) that must be published before sharing — the loop and the distribution artifact are more fused than in Metabase/ThoughtSpot. (Product-specific packaging.)

## Boundary Findings

### vs SQL Workbench / Analytical Query Editor (sibling leaves, same directory section)

The researched products share the L0 loop with SQL workbenches (compose → run → result → refine). The differences are:

- audience: developer/DBA vs business user/analyst
- authoring abstraction: SQL text vs GUI/search/NL over fields
- unit of work: the statement vs the question
- context: raw database vs governed data space (permissions, semantic layer)
- result treatment: grid/export vs visualization + saving + sharing + dashboards

But the products blur the line: Metabase embeds a full SQL editor (with one-way conversion from builder to SQL); Zoho's Query Tables are SQL; ThoughtSpot's Views are saved SQL. The boundary is an **audience/abstraction gradient**, not a wall.

**Test**: remove the GUI/semantic abstraction (SQL-only, raw database, grid output) → SQL Workbench remains; add governed data space + non-SQL authoring + saved/shareable questions → Ad-hoc Query Application remains. → Flag for joint review when SQL Workbench and Analytical Query Editor are processed.

### vs Business Intelligence Platform (sibling leaf, same section)

In the current market the two are almost always one product: all four sampled products bundle the ad-hoc loop with dashboards, sharing, governance, and (for some) semantic modeling. The distinguishing structure:

- BI Platform: persistent curated artifacts (dashboards, reports) + distribution + governance as the primary structure
- Ad-hoc Query Application: the interactive question loop as the primary structure

Metabase ("Questions are the basic analytical unit") and ThoughtSpot ("Answers = saved search") name the loop's artifact as their core object, which keeps the Type recognizable inside a bundle. → The leaf is best understood as the interactive-query core that BI platforms bundle; flag for joint review when Business Intelligence Platform is processed.

### vs Dashboard Platform / Reporting Platform

Those center on persistent, curated, often scheduled artifacts consumed by viewers. Ad-hoc query centers on composing new queries at question time. **Test**: remove the ability to compose new queries → a dashboard/report viewer remains; restore composition → the Type returns.

### vs Data Visualization Application

Visualization is the presentation layer; an ad-hoc query can return a plain table, and a data-viz tool can exist without live querying (authoring from static data). Modern products fuse both. **Test**: remove query composition → chart authoring tool remains; remove chart authoring → table-only ad-hoc query tool remains.

### vs OLAP / Multidimensional Analytics Platform

OLAP centers on the multidimensional cube (dimensions/measures/aggregation navigation); ad-hoc query is model-agnostic (relational, cube, search index). Classic OLAP clients were one historical form of ad-hoc query. Adjacent, not identical.

### vs Data Explorer / Public Data Portal (section 02.12)

Those explore curated, published datasets (often read-only, fixed schema, portal-framed). Ad-hoc query runs user-composed queries against connected live data sources with permissions. Different core structure.

### vs Data Science Workbench

Data science workbenches center on code notebooks (Python/R) for modeling/statistics; ad-hoc query centers on no-code/low-code question answering over governed data. Adjacent; some overlap via SQL cells.

## Uncertainties

1. **Tableau not directly researched** (help center unreachable, 2× 404). Tableau is a canonical ad-hoc visual-analysis product; the visual-analysis philosophy is represented here by Power BI and Zoho Analytics instead. No Tableau-specific claims are made.
2. **Apache Superset not researched** (site empty 2×, GitHub raw timeout). The SQL-first engineering surface is represented indirectly via Metabase's native editor and Zoho's Query Tables.
3. **Looker not researched** (2× timeout). The semantic-layer-first philosophy is represented via ThoughtSpot's semantic layer/Models.
4. **Power BI service-side ad-hoc behaviors** (Q&A in the service, quick insights, explore from a dataset) were only partially covered; observations are Desktop-centric.
5. **Zoho Analytics depth**: observations come from the help TOC + Creating Reports page; per-feature mechanics (e.g., exact Query Table behavior, Ask Zia internals) not deep-fetched; assertions kept at structure level.
6. **Precise operational limits** (row caps, timeouts, cache TTLs) are product-specific and documented only for Metabase/ThoughtSpot in fetched pages; they are kept in Research Notes and excluded from the final document.
7. **Market edges not sampled**: Qlik (associative engine), Databricks SQL/Snowsight (warehouse-native), Google Sheets/Excel as ad-hoc surfaces. The L0 is expected to hold for them but this is inference, not observation.

## Final Synthesis

An Ad-hoc Query Application is best modeled as an **interactive question-answering surface over connected data**:

```text
Connect to data (authorized, queryable)
→ compose a query at question time (step builder / drag-drop / search / NL / SQL)
→ run it immediately
→ read the result (table and/or chart)
→ refine in place (filter, regroup, drill, re-sort, change visualization) and re-run
→ optionally: save the question → share it → pin it to a dashboard → export it → alert on it
```

The defining core is deliberately small: queryable data + user-composed query + immediate execution + result + refinement loop. Everything else the market associates with the category — charts, dashboards, natural-language AI, semantic layers, alerts, embedding, version control — is common mature structure or variant structure, not definition.

The Type's market reality: the loop is almost always bundled inside BI platforms today, but it remains the recognizable core object of the category (Question/Answer), and the boundary to SQL Workbench / Analytical Query Editor is an audience-and-abstraction gradient rather than a structural wall — recorded as boundary issues for joint review.
