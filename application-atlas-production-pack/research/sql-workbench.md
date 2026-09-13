# Research Notes — SQL Workbench

Research date: **2026-09-09**
Leaf: `SQL Workbench` (DIRECTORY.md §13 Data, Analytics & AI Systems, line 1002)
Slug: `sql-workbench`

---

## Research Goal

Understand what "SQL Workbench" is as a directory leaf: whether the market contains a distinct Application Type behind the name, or whether the name resolves into the already-documented query-surface family (SQL Client §12 / Database IDE §12 / Analytical Query Editor §13).

This pass carries the heaviest pre-hung flag load of the §13 query-surface family:

1. **sql-client** (§12, processed 2026-09-09): suspected **NEAR-ALIAS**; joint review recommended at this pass; proposed seam = audience center (developer/DBA working on databases vs data/analytics work over governed data spaces) with center of gravity deciding.
2. **analytical-query-editor** (§13, processed 2026-09-06): recorded "sql-workbench = connection-agnostic general SQL tooling"; flagged joint review when SQL Workbench is processed.
3. **ad-hoc-query-application** (§13, processed): flagged the trio (ad-hoc / sql-workbench / analytical-query-editor) as an audience/abstraction gradient, not a wall.
4. **database-management-console** (§13, processed 2026-09-07): "sql-client + sql-workbench (§12/§13) should apply the same center-of-gravity test (query surfaces, no deployment administration)."
5. **graph-database-explorer** (§13, processed 2026-09-08) + **rdf-sparql-workbench** (§13, processed 2026-09-09): sql-client + sql-workbench are the same query-surface family over other engine classes; the engine-class test is expected to hold at this pass.
6. **lakehouse-platform** (§13, processed 2026-09-08): "vs sql-workbench/analytical-query-editor (serving surfaces of this Type, distinct leaves)."

## Initial Boundary (hypothesis before research)

Three candidate readings of the leaf, to be decided by evidence:

- **(a) Distinct Type** — a data/analytics-facing SQL work surface, connection-agnostic, separated from the developer-facing SQL Client by audience and data context (the sql-client pass's proposed seam).
- **(b) Alias** — the §13 name for the same query-surface population §12 calls SQL Client; the literal namesake product (SQL Workbench/J) being a universal SQL query tool.
- **(c) Packaging word** — "workbench" as a vendor word attaching to query editors (platform worksheets) or IDEs (MySQL Workbench), with no own population.

Expected confusions: Database IDE (environment breadth), Analytical Query Editor (platform binding), Database Management Console (administration), engine-class siblings (Graph/Vector/Time-series/RDF), BI family (result grids/charts).

## Research Questions

1. What is the literal namesake (SQL Workbench/J)? What does it self-describe as? Where does it sit relative to the SQL Client / Database IDE / Analytical Query Editor cores?
2. Does any product population self-label "SQL workbench" as a category distinct from SQL clients/editors?
3. Does the proposed developer-vs-analytics audience seam produce two structural Types, or one Type with audience variants?
4. Do the family tests hold — center of gravity (no deployment administration), engine-class binding (SQL), platform binding (vs Analytical Query Editor)?
5. How is the word "workbench" used across the market (SQL Workbench/J, MySQL Workbench, platform worksheets/editors)?
6. What does the "workbench" lens itself emphasize (accumulated work: workspaces, scripts, macros, profiles, history, data movement), and is that layer definitional or standard capability?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers — deliberately spanning the namesake/universal/team axes:

| Product | Why selected | Philosophy / position | Tier & model | Form |
|---|---|---|---|---|
| SQL Workbench/J | the literal namesake — the decisive specimen | free, DBMS-independent SQL query tool; scripting + export/import focus; explicitly not an IDE, no DBA focus | free OSS (modified Apache 2.0), Java | desktop GUI + console mode + batch CLI |
| DBeaver | the dominant universal database tool; population anchor; IDE-gradient end | "Universal Database Tool"; community/PRO/dbvr split | free OSS community + commercial PRO | desktop GUI (+ dbvr CLI) |
| PopSQL | the strongest candidate for a distinct analytics-facing population; the seam test | "The SQL editor for team collaboration"; data-team framing, connection-agnostic across the analytical stack | commercial SaaS + desktop (Timescale/TigerData) | web + desktop app |

Boundary specimens (prior passes, not re-fetched): Snowsight worksheets / Databricks SQL editor / Redshift query editor v2 / Fabric SQL query editor (analytical-query-editor pass — the platform-bound Type); Beekeeper Studio's alternatives market map (sql-client pass — the family's own population map); MySQL Workbench (naming specimen only — docs 403 in two prior passes, no structural claims).

## Sources

Fetched 2026-09-09 (all Layer A — official product/documentation pages):

- SQL Workbench/J — home page: https://www.sql-workbench.eu/
- SQL Workbench/J — User's Manual (table of contents / structure): https://www.sql-workbench.eu/manual/workbench-manual.html
- DBeaver Community — https://dbeaver.io/
- PopSQL — https://www.popsql.com/
- PopSQL — buyer's guide page: https://www.popsql.com/sql-editor-buyers-guide (nav shell only; no category vocabulary content)

**Source-integrity note**: the fetched SQL Workbench/J homepage contained a block of injected non-product text (a prompt-injection attempt) between the navigation and the product description. The injected text was ignored entirely; only the genuine product-description portions were used, and every structural claim taken from that page was corroborated against the separately fetched manual page (clean). Recorded here for sourcing hygiene.

Unreachable / not retried (per the network rule):

- dev.mysql.com / mysql.com — HTTP 403 in two prior passes (database-ide, database-schema-design-tool); MySQL Workbench used as naming specimen only, no structural claims.
- cloud.google.com — timed out ×2 in prior passes (analytical-query-editor, ad-hoc); BigQuery not sampled.
- docs.beekeeperstudio.io — transport error in the sql-client pass; not retried.
- docs.popsql.com — linked from the fetched page but not fetched this pass; PopSQL evidence held at product-page strength.

Prior-pass context (read, not fetched this pass): research/sql-client.md, research/analytical-query-editor.md, research/database-ide.md, research/database-management-console.md, research/graph-database-explorer.md, research/rdf-sparql-workbench.md, research/ad-hoc-query-application.md (boundary sections), STATUS.md boundary entries.

---

## Product A — SQL Workbench/J (the literal namesake)

*(Layer A: official home page + user's manual)*

### Key observations

- Self-description, verbatim: "SQL Workbench/J is a **DBMS-independent, cross-platform SQL query tool**. It is written in Java and should run on any operating system that provides a Java Runtime Environment."
- Explicit scope statement, verbatim: "Its main focus is on running SQL scripts (either interactively or as a batch) and export/import features. **Graphical query building or more advanced DBA tasks are not the focus and are not planned. It's not intended as a full blown 'development IDE', but more as a powerful command line.**"
  - Two boundary disclaimers in the vendor's own words: not a DBA console (the management-console center-of-gravity test), not an IDE (the environment-breadth test).
- **Connection**: JDBC-driver based ("DBMS-independent"); connection profiles with profile groups, JDBC extended properties, SSH tunnels, Oracle SYSDBA privilege connection, quick filter; command-line start with a pre-defined profile or without a profile; configuration directory; JDBC driver configuration with a library directory.
- **Workspaces** as a first-class concept: create a copy of the current workspace, load a different workspace, workspace and external files, workspace variables — the accumulated-work layer the word "workbench" points at.
- **SQL editor**: code completion, hints for INSERT statements, custom keyword highlighting, reformatting (pretty-print), bookmarks, SQL value-list generation, programming-related editor functions.
- **Execution and results**: executing statements, displaying results, BLOB/CLOB handling, editing data in the result (insert/delete rows), sorting, filtering, server messages, performance tuning of execution, saving/loading SQL scripts, displaying table structure, running stored procedures.
- **Alternate delimiters** for creating stored procedures/triggers (PostgreSQL, Oracle PL/SQL, static and dynamic delimiters) — dialect-aware script handling.
- **Annotations in SQL comments** (product-specific machinery): naming result tabs, re-using named tabs, appending results, suppressing empty results, automatic refresh, keep-result, result-as-text, crosstab (pivot) from a result, BLOB-as-image preview, row-height optimization, macro menu annotations.
- **Macros and text clips**; **variable substitution** (define variables, populate from a SELECT or a file, edit, prompt for values during execution, ordering, scoping).
- **Batch mode**: script files, connection specification, delimiters, encoding, logfile, error handling, scripts on success/failure, ignoring DROP errors, changing connection mid-script, console output control, running batch scripts interactively — the automation endpoint.
- **Console mode**: interactive console (entering statements, displaying result sets, max rows, query timeout, profile management, external pager) with **PostgreSQL psql command support**.
- **Wb\* command vocabulary** (client-side commands beside SQL): WbExport (text/CSV, XML, HTML, SQL INSERT/UPDATE/DELETEINSERT, spreadsheets ods/xls/xlsx/xlsm, JSON; compression; all-tables directory export), WbImport (text/XML/spreadsheet; update mode; native UPSERT/insertIgnore; FK-order detection), WbCopy (copy data across databases, by table or query, update mode, table sync), WbSchemaDiff / WbDataDiff (compare schemas/data across databases), WbGrepSource / WbGrepData (search object source / data across all tables), WbGenerateScript / WbTableSource / WbViewSource / WbProcSource / WbTriggerSource / WbGenerateDrop / WbGenerateFKScript / WbGenerateImpTable (DDL generation), WbGenerateDelete / WbGenerateInsert (DML generation with dependencies), WbSchemaReport / WbDescribe / WbList* (catalog information), WbDefineMacro / WbVarDef / WbVarList, WbInclude, WbCall, WbHistory, WbConnect / WbSwitchDB / WbSetSchema, WbMode (read-only), WbStartBatch/WbEndBatch, WbSelectBlob, WbFetchSize, WbRunLB (run SQL from a Liquibase changelog), WbXslt, WbSysExec / WbSysOpen, WbFeedback, WbConfirm, WbEcho, WbMessage.
- **DataPumper** — a separate GUI tool for copying tables between two connections.
- **Database Object Explorer + object tree**: objects tab, table details, modifying object definitions, table data tab, procedure tab, search table data, tree filtering/drag-and-drop/context menus.
- **DBMS coverage and analytical usage**: the manual's "Common DBMS problems" chapter covers Oracle, MySQL, Microsoft SQL Server, IBM DB2, **Amazon Redshift**, PostgreSQL, and Sybase SQL Anywhere — the namesake's own documentation treats a cloud analytical warehouse (Redshift) as a routine target.
- License/distribution: free "for almost everyone" under a modified Apache 2.0 license; source hosted on Codeberg; current stable Build 133 (2026-05-31).

### Layer notes

All Layer A. The namesake self-identifies into the universal SQL query-tool population — the SQL Client population — positioned at its scripting/data-movement pole, explicitly below the IDE and beside the DBA console. Its Redshift documentation is direct evidence that the same tool serves analytical-warehouse work; no separate analytics-facing structure appears.

## Product B — DBeaver (population anchor)

*(Layer A: official community site; DBeaver's docs were doc-sampled in the database-ide pass)*

### Key observations

- Self-description: "DBeaver Community is a free, open-source **database management tool** recommended for personal projects. Manage and explore SQL databases like MySQL, MariaDB, PostgreSQL, SQLite, Apache Family, and more." Site title: "Free Open-Source Database Management Tool"; hero heading: "**Universal Database Tool**".
- Community edition: basic relational support, Data Editor, SQL Editor, task management, database maintenance tools, AI Chat & @ai command.
- PRO edition: advanced security, ODBC connectivity, NoSQL support (MongoDB, Cassandra, Redis, CouchDB), **cloud databases (Redshift, Google BigQuery, Oracle Cloud)**, native AWS/Google Cloud/Azure support, cloud storage support, database development tools, database performance visual tools, multi-component task management, task scheduler, **visual query builder**.
- **dbvr** — a CLI companion (community + commercial): query result export, metadata management, SSH tunnels, SSO/SSL/Kerberos, secret management (AWS, Vault, CyberArk), cloud-storage export, MCP configuration to expose a database connection as an MCP server.
- Release notes evidence one tool over heterogeneous engines including the analytical stack: Athena, BigQuery, ClickHouse, Databricks, Snowflake, Netezza, TDengine, GreptimeDB, StarRocks, Apache Doris, Exasol, Flight SQL, LibSQL...

### Layer notes

All Layer A (site). DBeaver was already doc-sampled in the database-ide pass (its console-cannot-save vs editor-saves line is that pass's IDE-gradient specimen). Here it anchors the population: the universal tool family spans the client↔IDE gradient and already serves analytical engines in its commercial tier — the same observation the sql-client pass made for Beekeeper's 26-engine list.

## Product C — PopSQL (the analytics-facing pole; strongest distinct-population candidate)

*(Layer A: official product page)*

### Key observations

- Self-description, verbatim: "**The SQL editor for team collaboration**" — "Work better together on data with centralized SQL queries, real-time collaboration, and interactive visuals." Page title: "PopSQL - Collaborative SQL Editor". Framing: "Bring order to SQL chaos... It's time to modernize your SQL development process."
- Audience framing: "trusted by 2000+ of the world's top data teams"; "a home for your data team"; customer quotes from analytics/data roles (VP Analytics, Analytics Lead, Data Scientists, Head of Data & Analytics, Engineering Director).
- **Connection-agnostic across the analytical stack**: Amazon Athena, Azure Synapse, BigQuery, ClickHouse, MySQL, PostgreSQL, Presto, Amazon Redshift, Snowflake, SQL Server, TigerData/Timescale, Trino — "Works with any database... PopSQL supports every major database provider out there." Per-engine landing pages self-label "…SQL client" (e.g., /connections/athena-sql-client).
- **Data-team layer**: folders, search over queries/dashboards/tables/columns, **data catalog** (definitions, tags, usage statistics, common joins, top users), schema browser with popular/pinned tables and filtering, autocomplete surfacing descriptions/tags/usage.
- **Collaboration layer**: real-time collaboration, peer review, inline comments on queries, Markdown descriptions, **version history** (who changed what, when, diffs, revert/copy), **shared connections** ("Never waste time hunting and waiting for credentials again"), granular permissions per connection ("share Postgres Primary with Engineering, and Snowflake with everyone else").
- **Insight layer**: in-app charts, lightweight dashboards, self-service analytics ("business users safely customize reports with variables, like date ranges or user IDs"), Slack integration.
- **Engineering layer**: Git integration ("Keep track of every change and review PRs with Git"), APIs for query management and scheduling, scheduled queries, dbt Core integration, notebooks.
- **Connectivity/security**: bridge connector for databases behind private networks, SSH tunnels, static IPs, desktop app; SSO and SCIM provisioning (Okta, AzureAD, Google), SOC 2 and GDPR compliance.
- Ownership: "2026 (c) Timescale, Inc., d/b/a TigerData" — a database-company-owned SQL editor.

### Layer notes

All Layer A (product page). PopSQL is the market's clearest "analytics-facing, connection-agnostic SQL work surface" — and it self-labels "SQL editor"/"collaborative SQL editor", not a distinct workbench category. Its additions (catalog, collaboration, charts, dashboards, Git) are layers over the connection + SQL editor + results core — the same core the sql-client pass defined. The buyer's-guide page fetched for category vocabulary was a nav shell (no content).

---

## Cross-product Comparison

| Dimension | SQL Workbench/J | DBeaver | PopSQL |
|---|---|---|---|
| Self-label | "DBMS-independent, cross-platform SQL query tool" | "Universal Database Tool" / "database management tool" | "The SQL editor for team collaboration" / "Collaborative SQL Editor" |
| Uses the word "workbench" | in the product name only | no | no |
| Engine scope | DBMS-independent (JDBC); docs cover Oracle/MySQL/MSSQL/DB2/Redshift/PostgreSQL/SQL Anywhere | universal; PRO adds NoSQL + cloud warehouses (Redshift, BigQuery) | 12+ engines incl. Athena/BigQuery/ClickHouse/Presto/Redshift/Snowflake/Synapse/Trino |
| Form | desktop GUI + console mode + batch CLI | desktop GUI + dbvr CLI | web + desktop app |
| Connection model | connection profiles (groups, SSH tunnels, SYSDBA, quick filter); CLI with/without profile | connection manager; native cloud support (PRO) | shared connections with granular permissions; bridge connector, SSH tunnels, static IPs |
| SQL as primary interface | SQL editor + scripts + Wb* commands + console mode | SQL Editor (+ visual query builder in PRO) | SQL editor (+ query variables, templates) |
| Results | result display; edit in result; sort/filter; BLOB/CLOB; annotations (named tabs, crosstab, keep-result) | Data Editor; result sets | result grids → charts/dashboards |
| Accumulated work | workspaces, macros, text clips, bookmarks, variables, script files | projects/tasks; saved work | shared query repository, folders, version history, Git |
| Data movement | WbExport/WbImport/WbCopy/DataPumper (cross-DB copy, schema/data diff) | data transfer/export | export, scheduled queries, Slack push |
| Catalog inspection | Database Object Explorer + object tree + WbDescribe/WbList* | Navigator tree | schema browser + data catalog |
| Object development | DDL/DML generation commands; "not an IDE" by its own statement | development tools (PRO); ER diagrams (prior pass) | none observed |
| Deployment administration | explicitly "not the focus and are not planned" | maintenance tools (community) — convenience-grade | none |
| Team/collaboration | none | none | real-time collaboration, comments, shared connections, permissions |
| BI layer | none (crosstab annotation only) | none | charts, dashboards, self-service variables |
| AI | none observed | AI Chat & @ai | not observed on fetched page |
| Audience framing | general/power SQL users, scripting, data movement | database professionals | data teams (analysts, data scientists) |

### Stable cross-product reading

1. **All three are front-ends to external running SQL database systems**; none holds data of record.
2. **All three take SQL as the primary working interface** (editor / scripts / console).
3. **All three return results in inspectable form** (grids, plus status/error feedback).
   → All three satisfy the SQL Client defining core exactly as the sql-client pass wrote it.
4. **The word "workbench" does not mark a category**: the namesake uses it as a product name; the other two never use it. The family's own market map (Beekeeper's alternatives list, prior pass) mixes "Workbench"-named products (MySQL Workbench) into the client/IDE population.
5. **The proposed developer-vs-analytics audience seam does not split the population**: the universal tools already serve analytical engines (SQL Workbench/J documents Redshift; DBeaver PRO lists Redshift/BigQuery; PopSQL is analytics-first yet connection-agnostic), and the analytics-facing candidate self-labels "SQL editor" with the identical core. Audience is a variant axis, not a Type boundary.
6. **The only structural split in this space is platform binding**: connection-agnostic tools (this population) vs one-platform-bound editors (Analytical Query Editor, prior pass).

---

## Canonical Abstraction

### L0 — Defining Invariant

The evidence resolves the leaf as an **alias**: the market population behind "SQL Workbench" is the same query-surface population the atlas documents as **SQL Client** (§12). Its defining core is therefore the SQL Client's core, re-stated:

```text
Connection to an external running SQL database system (client premise; no data of record)
└── SQL as the primary working interface (author → execute against the connection)
    └── Results returned in inspectable form (row sets + status/error feedback)
```

Alias evidence (the decision):

1. **The literal namesake self-identifies into the SQL Client population.** SQL Workbench/J: "a DBMS-independent, cross-platform SQL query tool", "not intended as a full blown 'development IDE'", DBA tasks "not the focus and are not planned" — the client core at its scripting/data-movement pole, with the two neighboring Types explicitly disclaimed in the vendor's own words.
2. **The strongest candidate for a distinct analytics-facing population carries the identical core.** PopSQL self-labels "SQL editor"/"collaborative SQL editor"; its structure is connection + SQL editor + results with team/catalog/BI layers on top — layers, not a different defining structure.
3. **The population anchor is the same family.** DBeaver self-labels "Universal Database Tool"; the database-ide pass already sampled it as the gradient specimen between client and IDE.
4. **No product population self-labels "SQL workbench" as a distinct category.** The word attaches to (i) a universal query tool's product name (SQL Workbench/J), (ii) a vendor IDE's product name (MySQL Workbench — naming specimen only, docs unreachable), and (iii) loose genericism for platform query surfaces, which are the Analytical Query Editor Type on the binding discriminator.
5. **The proposed developer-vs-analytics audience seam fails as a Type boundary.** Universal clients already span both audiences (Redshift in the namesake's own docs; Redshift/BigQuery in the anchor's commercial tier; the analytics-first candidate is connection-agnostic). Audience without structural difference is a variant axis. The only structural split in the space is platform binding vs connection-agnostic.

### L1 — Common Mature Structure (the "workbench" lens' own emphasis)

The word "workbench" points at the **accumulated-work layer** of the query surface — present across the population as standard capabilities, not definition:

- saved connections / connection profiles (folders, groups, tunnels, enterprise auth)
- workspaces / projects / saved-query repositories — where SQL work accumulates (SQL Workbench/J workspaces; DBeaver projects/tasks; PopSQL shared query folders with version history and Git)
- editor affordances: completion, highlighting, formatting, bookmarks, snippets/macros/text clips
- query/script history; variables and parameterization with prompting
- catalog inspection beside the query surface (object explorer/tree, describe commands, schema browser)
- result-grid data editing; result annotations (named tabs, crosstab, keep-result)
- data movement: export/import (text/CSV/XML/HTML/SQL/spreadsheet/JSON), cross-database copy, schema/data diff, search across object source and data
- execution feedback: timings, server messages, error handling with gates
- connectivity plumbing: SSH tunnels, TLS, driver libraries, cloud-native auth, secret management
- team layer (web-era pole): shared connections with permissions, real-time collaboration, comments, data catalog

### L2 — Variant / Optional Structure

- form factor: desktop GUI ↔ console mode ↔ batch CLI ↔ web/team SaaS
- scope: engine-native ↔ universal/multi-DBMS; relational-only ↔ NoSQL/cloud-warehouse breadth
- audience posture: developer/DBA ↔ data-team/analytics (variant axis — the alias decision's key test)
- object-development convenience (DDL/DML generation, table editors) — the IDE seam; the namesake disclaims IDE ambition while carrying generation commands
- visual query building (PRO-tier in the anchor; explicitly "not the focus" in the namesake)
- BI layers (charts, dashboards, self-service variables) — the PopSQL pole; drift toward BI/ad-hoc territory when they become the center
- AI assistance (era-current)
- automation posture: batch endpoint (scripts, exit codes, success/failure hooks) ↔ purely interactive
- business model: free OSS ↔ freemium ↔ commercial SaaS; single-user ↔ team/cloud

### L3 — Vendor-specific (research notes only)

- **SQL Workbench/J**: Wb* command vocabulary; SQL-comment annotations; alternate delimiters for PL/SQL/T-SQL procedure bodies; workspace files; DataPumper; console mode with psql-command support; Liquibase changelog runner (WbRunLB); modified Apache 2.0 license with conduct restrictions; Codeberg source hosting.
- **DBeaver**: Eclipse-platform heritage (per the database-ide pass); community/PRO/dbvr product split; MCP exposure of connections (dbvr); AI Chat @ai command.
- **PopSQL**: shared connections with granular per-connection permissions; bridge connector; data catalog with usage statistics/common joins/top users; Timescale/TigerData ownership; per-engine "SQL client" landing pages.

## Rejected Findings

- **"SQL Workbench is a distinct data/analytics-facing Type separate from the SQL Client"** — rejected: the namesake self-identifies into the client population; the analytics-facing candidate carries the identical core; the audience seam produces variants, not Types.
- **"A SQL workbench is defined by workspaces/saved work"** — rejected as definitional: accumulated-work machinery is standard capability; the namesake's own core loop (connect → SQL → results) stands without it, and the sql-client pass already classified persistence as common-not-definitional.
- **"SQL Workbench = the platform query editors (worksheets)"** — rejected: those are bound to one analytical platform's data and are the Analytical Query Editor Type (prior pass); the binding discriminator separates them.
- **"MySQL Workbench proves a workbench Type"** — rejected as evidence: docs unreachable in prior passes (403); it stands only as a naming specimen; no structural claims made.
- **"The word 'workbench' marks a category"** — rejected: the family's own market map mixes Workbench-named products into the client/IDE population; two of three sampled products never use the word.

## Boundary Findings

| Neighbor Type | Shared ground | Discriminator (what flips the Type) |
|---|---|---|
| **SQL Client (§12, processed) — ALIAS** | the entire defining core | none — one market population, two directory names. "SQL client" is the living category label (Beekeeper verbatim; psql/HeidiSQL "client application"); "SQL workbench" survives as a product name (SQL Workbench/J) and loose genericism. Remove-test is trivially symmetric: nothing to remove. |
| **Database IDE (§12, processed)** | connection + SQL loop + results | environment breadth: catalog as primary navigation + object/data development + persistent workspace. The namesake draws the line itself: "not intended as a full blown 'development IDE'". DBeaver sits at the gradient's IDE end (prior pass's console-vs-editor specimen). Test: strip the environment structures from an IDE → a client/workbench; accrete them → an IDE. |
| **Analytical Query Editor (§13, processed)** | SQL editor + execution + result grid | platform binding: bound to ONE analytical platform's data space vs connection-agnostic across engines. Redshift QE v2's "web-based SQL client application" self-label shows the vocabulary overlap; the binding is the constant. Test: bind the surface to one platform's data → Analytical Query Editor; make it connection-agnostic → this population. |
| **Ad-hoc Query Application (§13, processed)** | SQL composition and execution | audience + authoring abstraction: governed question layer for business users vs SQL-first technical surface. The trio gradient resolves: ad-hoc (question layer) / analytical query editor (platform-bound) / sql workbench = sql client (connection-agnostic). |
| **Database Management Console (§13, processed)** | may connect to the same engines | center of gravity: deployment administration vs data/query loop. Holds verbatim in the namesake's own words: DBA tasks "not the focus and are not planned". Test: remove query authoring → console remains; remove administration → this population remains. |
| **Graph Database Explorer / Vector Database Console / Time-series Database Workbench / RDF-SPARQL Workbench (§13)** | query-surface family shape | engine class: those bind to graph/vector/time-series/RDF engines and their query languages; this population binds to SQL-speaking systems. The family test the prior passes expected holds; the SQL binding is part of the invariant. |
| **BI Platform / Dashboard Platform / Data Visualization Application** | result grids, charts (PopSQL pole) | those curate persistent artifacts for consumers; the query surface's center is the SQL loop. PopSQL's charts/dashboards are a layer; a product whose center is curated dashboards has left the Type. |
| **Data Science Workbench (§13, processed)** | interactive data work | unit of work: notebook cells/code sessions vs SQL statements against connections. |
| **ETL/ELT Platform / Data Integration Platform** | data movement (WbCopy/DataPumper class) | those build and run pipelines as managed jobs; the query surface's copy/export commands are interactive conveniences beside the SQL loop. |

## Boundary Issues (for STATUS.md)

1. **ALIAS RESOLVED with sql-client (§12, processed same day)** — that pass's near-alias joint-review flag DISCHARGED: keep-one-family, two directory names (SQL Workbench §13 = SQL Client §12). The proposed audience seam was tested and rejected as a Type boundary (audience is a variant axis; the only structural split in the space is platform binding vs connection-agnostic). Directory recommendation recorded for taxonomy review: the two leaves name one population; no directory change made from this side.
2. **analytical-query-editor's joint-review flag DISCHARGED**: its expected reading ("sql-workbench = connection-agnostic general SQL tooling") is confirmed as exactly the SQL Client core; the binding test separates it from the Analytical Query Editor Type.
3. **ad-hoc-query-application's trio gradient RESOLVED**: ad-hoc (governed question layer) / analytical query editor (platform-bound) / sql workbench = sql client (connection-agnostic query surface).
4. **database-management-console's center-of-gravity test APPLIED and holds** — verbatim in the namesake's own scope statement.
5. **graph-database-explorer / rdf-sparql-workbench engine-class family expectation RATIFIED**: the SQL binding is part of the invariant; the §13 query-surface family pattern holds.
6. **lakehouse-platform's serving-surface note CONSISTENT**: the lakehouse's serving surfaces are the platform-bound editors (Analytical Query Editor); the connection-agnostic population is not a lakehouse serving surface.
7. Taxonomy observation (no action): the §12/§13 double placement of one query-surface population is the structural cause of this alias; the client is the family's shared core (as the sql-client pass observed), and the §13 leaf adds no second population.

## Uncertainties

1. **MySQL Workbench unreachable** (403 in two prior passes) — used as naming specimen only; its classification as a Database IDE rests on the directory's §12 placement and the database-ide pass's consideration note, not on fetched evidence.
2. **PopSQL evidence is product-page strength**; its docs domain was not fetched this pass — operational mechanics unverified; no precise operational claims drawn from it.
3. **The SQL Workbench/J homepage carried injected non-product text**; product-description content was corroborated against the clean manual page. Low risk, recorded for integrity.
4. Whether any regional/non-English market uses "SQL workbench" as a living category label could not be verified from reachable sources; the conclusion rests on the English-language market.
5. **Historical check**: the namesake itself (early-2000s Java/JDBC generation, alongside SQuirreL SQL) is the historical pole — a universal JDBC query tool satisfying the SQL Client core completely with no web/team/AI machinery; the terminal-client pole (psql) was already verified in the sql-client pass. The Type's era-agnosticism is inherited from the alias; no separate historical fetch was needed.

## Final Synthesis

"SQL Workbench" does not name a distinct Application Type. The market population behind the name is the generic SQL query surface — the population the atlas documents as the **SQL Client**: a front-end that connects to an external running SQL database system, takes SQL as its primary working interface, and returns results in inspectable form. The literal namesake (SQL Workbench/J) self-identifies into that population at its scripting/data-movement pole and explicitly disclaims both neighboring Types ("not a development IDE"; DBA tasks "not the focus and are not planned"). The strongest candidate for a distinct analytics-facing population (PopSQL) carries the identical core with team/catalog/BI layers and self-labels "SQL editor". The proposed developer-vs-analytics seam fails as a Type boundary because universal clients already span both audiences; the only structural split in the space is platform binding (Analytical Query Editor) vs connection-agnostic (this population). The atlas therefore documents this leaf as an **alias of SQL Client**, written from the workbench lens — the query surface together with its accumulated-work environment — with the alias recorded for taxonomy review.
