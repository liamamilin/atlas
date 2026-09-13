# Research Notes — Database IDE

Research date: **2026-09-07**
Leaf: `Database IDE` (DIRECTORY.md §12 Software Development & Product Engineering)
Slug: `database-ide`

---

## Research Goal

Understand what a Database IDE is as an Application Type: the objects inside it, the users, the working loop, the interfaces, the rules that govern behavior, and — critically — how it is distinguished from the neighboring leaves in the same directory region:

- SQL Client (§12)
- Database Management Console (§13)
- SQL Workbench / Analytical Query Application (§13)
- Database Schema Design Tool (§12)
- Database Sandbox Platform / Database Dev/Test Environment Manager (§12; the latter already processed)
- Integrated Development Environment / IDE (§12)

## Initial Boundary (hypothesis before research)

A Database IDE is a development environment whose "code world" is a running database rather than a file system: it connects to external DBMSs, exposes the schema catalog, supports schema-aware SQL authoring and execution, and lets the user work directly on objects and data.

Adjacent confusions expected up front:

1. **vs SQL Client** — both execute SQL against a connection. Suspected discriminator: the IDE is a fuller *environment* (catalog browsing, object/data development, persistent script workspace) while a client is a lighter query surface.
2. **vs Database Management Console** — both may administer; suspected discriminator: development loop vs administration operations as center of gravity.
3. **vs general IDE** — suspected discriminator: the object world is database metadata, not source files.
4. Note: sampled products self-describe across a spectrum ("IDE", "management tool", "administration and development platform", "integrated environment"), so the category is expected to be a pole, not a wall.

## Research Questions

1. What objects does the user see and manipulate? (connections, catalog nodes, scripts, results, plans…)
2. What is the core interaction loop?
3. How is the SQL authoring surface made "aware" of the database (completion, navigation, analysis)?
4. How do object development and data editing work, and under which rules (e.g. when is a result set editable)?
5. How are transactions and execution modes surfaced?
6. How does the tool persist work (scripts, connections, history)?
7. How does the tool reach databases (drivers, tunnels, auth) and how much security plumbing does it own?
8. Where does administration depth live, and is it definitional or variant?
9. Where does the Type end and SQL Client / Management Console / Schema Design Tool begin?
10. Does the definition survive older / ecosystem-bound / web-deployed products?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

| Product | Philosophy / position | Tier & model |
|---|---|---|
| JetBrains DataGrip | commercial universal cross-DBMS IDE, developer-first, IntelliJ platform | commercial subscription; free for non-commercial use tier |
| DBeaver | universal database tool, freemium/open-source; editions from business-user Lite to Ultimate | Community + commercial editions; desktop + server (CloudBeaver/Team) + CLI (dbvr) |
| pgAdmin 4 | open-source PostgreSQL "administration and development platform"; web client/server | free OSS; deployable as desktop or multi-user web server |
| SQL Server Management Studio (SSMS) | ecosystem-bound integrated environment, admin-leaning, for the Microsoft SQL engine family | free, vendor-ecosystem |

MySQL Workbench was considered as a fifth sample (vendor-ecosystem + visual-modeling pole) but its official docs (dev.mysql.com, mysql.com) returned HTTP 403 on two attempts; it is therefore **not** used as an evidence source (see Source-access Limitations).

## Sources

Fetched 2026-09-07:

- DataGrip product page — https://www.jetbrains.com/datagrip/
- DBeaver documentation root — https://dbeaver.com/docs/dbeaver/
- DBeaver SQL Editor — https://dbeaver.com/docs/dbeaver/SQL-Editor/
- pgAdmin 4 documentation index — https://www.pgadmin.org/docs/pgadmin4/latest/
- pgAdmin 4 Query Tool — https://www.pgadmin.org/docs/pgadmin4/latest/query_tool.html
- SSMS overview — https://learn.microsoft.com/en-us/sql/ssms/sql-server-management-studio-ssms

Unreachable / degraded:

- dev.mysql.com & mysql.com — HTTP 403 (Workbench excluded from evidence)
- JetBrains DataGrip help center (meet-the-product page JS-empty; query-console page 404) — DataGrip evidence limited to its product page
- learn.microsoft.com SSMS sub-pages (components-features, object-explorer-overview) — HTTP 404 with and without view parameter; SSMS evidence limited to its overview page

---

## Product A — JetBrains DataGrip

*(evidence layer A = direct observation of the official product page; help-center depth not reachable)*

### Key observations

- Self-description: "Your powerful cross-platform IDE for relational and **NoSQL** databases"; positioning "one tool for many databases". Category language "IDE for databases" directly attested.
- **Query console**: "Intelligent query console — Execute queries in different modes and keep track of all your activity with the **local history**, preventing you from losing your work."
- **Schema-aware completion**: "DataGrip is aware of the table structure, foreign keys, and even database objects created in the code you're editing" — schema-awareness includes objects not yet persisted, only authored in the editor buffer.
- **Static analysis**: on-the-fly analysis and quick-fixes; "immediately let you know about unresolved objects".
- **Query history** preserved in a log; parameterized SQL with customizable patterns; SQL dialect options.
- **Import/export**: import from script/CSV/TSV/delimited text; export to CSV, JSON, HTML, Markdown, Excel, custom formats.
- **Version control integration** (Git, SVN, Mercurial…) — the tool treats database work as versioned project work.
- Broad multi-DBMS support: PostgreSQL, MySQL, Oracle, SQL Server, MongoDB, Redis, DynamoDB, Snowflake, ClickHouse, BigQuery, SQLite, Db2, MariaDB, Cassandra, CockroachDB, and more — SQL and NoSQL alike.
- Same "Database Tools and SQL" functionality is embedded into other JetBrains IDEs (the environment also exists as a component).
- AI assistance: schema- and context-aware query writing, error fixing, SQL dialect conversion; multi-model/multi-agent.

### Layer notes

- All above: Layer A (product page).
- Object tree naming, data editor mechanics, transaction UI specifics: **not verified** (help center unreachable). Do not assert.

## Product B — DBeaver

*(evidence layer A; docs root + SQL Editor page)*

### Key observations

- Self-description: "a **universal database management tool** for anyone who needs to work with data professionally"; "manipulate your data as if working in a regular spreadsheet… For advanced database users, DBeaver offers a powerful SQL editor, extensive administration features, tools for data and schema migration, database connection session monitoring".
- Editions ladder by audience: **Lite** ("essential database tools… simplified interface for data viewing and query execution… perfect for business users") → **Enterprise** (advanced visualization, SQL development tools, security, admin) → **Ultimate** (+ cloud); plus server-based **CloudBeaver** (browser-based) and **Team Edition** (collaboration, access control), and a headless **dbvr** CLI.
- **Connection layer**: driver manager (JDBC/ODBC), connection creation/editing, connection types, multiple datasource connections; network plumbing documented at depth — SSH tunnels, SSL with truststore/certificate management, proxies, Kubernetes, AWS SSM; authentication models (native DB user/password, DBeaver profiles, Microsoft Entra ID, Kerberos); secure password storage with master password; admin-managed pre-configured connections (data-sources.json).
- **Catalog navigation**: "Database Navigator" over connections; simple/advanced view; object filters; bookmarks; metadata search, database full-text search, file search.
- **Projects**: scripts organized in Projects; Project Explorer shows a **Scripts** folder.
- **SQL Editor** (SQL Editor page): "write and execute multiple SQL scripts within a single database connection, **save them as files, and reuse them later**". Explicit contrast: "SQL Editor for a connection is different from SQL console for a table or view. **Unlike the console, it can save scripts and changes made to them.**" — direct evidence that script persistence is what elevates a console into the editor/environment.
- Editor affordances: syntax highlighting **per database dialect** ("different databases have different sets of reserved keywords"); Ctrl-hover **hyperlinks** on identifiers that open the object's editor (code→catalog navigation); outline tree of the query; error indication distinguishing **server issues, semantic errors, spelling** (semantic analysis for relational DBs); AI error explanation (paid editions).
- **Results**: result tabs are instances of the Data Editor; charts from result sets; multiple result sets in one tab; layout controls.
- **Active context switching**: change the editor's connection or active schema while retaining the SQL text (active datasource / active catalog-schema selectors; link-with-editor).
- **Transaction mode** documented as a first-class concept: auto vs manual commit, **pending transactions**, **transaction log**.
- **Data Editor**: spreadsheet-like grid editing with filters, value/metadata/references/grouping/calc panels, charts, mock-data generation, dashboards, spatial/GIS data, virtual columns/keys.
- Object development: Database Object Editor; tutorials for creating tables, columns, indexes, constraints, triggers.
- SQL assistance: auto-complete/SQL assist, templates, formatter, variables, visual query builder, execution plans, query manager, SQL generation, client-side scripting/commands.
- Broader tooling: ER diagrams (including custom diagrams, edit mode); data transfer (import/export/migration, transfer to external storage); structure & data compare, schema compare, Liquibase changelog export; tasks + task scheduler; backup & restore, Git integration, PostgreSQL debugger, session manager, lock manager; cloud explorer (AWS/Azure/GCP); AI assistant incl. MCP tool integration.

### Layer notes

- All above: Layer A (two official doc pages + docs TOC structure).
- Edition-gated features (AI, some compare/debugger tools) noted as edition-dependent.

## Product C — pgAdmin 4

*(evidence layer A; docs index + Query Tool page)*

### Key observations

- Self-description: "the leading Open Source **management tool** for Postgres"; "the most popular and feature-rich open source **administration and development platform** for PostgreSQL"; "a powerful graphical interface that simplifies the **creation, maintenance and use of database objects**".
- Form factor: client/**server** web application — deployment docs, login page, 2FA, its own **user management**, LDAP/Kerberos/OAuth2/webserver authentication. The tool itself has accounts (multi-user deployment is a product property, not the DBMS's).
- **Server registration model**: server groups; Server Dialog (host/port/credentials); master password; connect-to-server flow; import/export of server definitions; newer "Workspace layout" allows **ad-hoc server connections** from a Welcome page without prior registration.
- **Catalog as the hub**: Object Explorer tree; dialog-generators for the full PostgreSQL object catalog — cluster level (databases, login/group roles, tablespaces, resource groups, replica nodes) and database level (schemas, tables, views, materialized views, functions, procedures, trigger functions, types, sequences, collations, domains, extensions, FDW/foreign tables, FTS configurations, publications/subscriptions…).
- **Table development**: dedicated dialogs for columns, PK/FK/unique/check/exclusion constraints, indexes, triggers, RLS policies, rules.
- **Developer Tools** section: Query Tool, **View/Edit Data**, **Schema Diff**, **ERD Tool**, PSQL tool, **Debugger**, AI Reports.
- **Query Tool** (deep documentation):
  - "execute arbitrary SQL commands and review the result set"; ad-hoc queries; multiple simultaneous Query Tool tabs.
  - Two-panel structure: upper SQL Editor (syntax coloring, **autocomplete** on Ctrl+Space; execute script vs execute-query-at-cursor; auto-indent; **drag-and-drop objects from the tree into the editor**, fully schema-qualified and quoted) and lower output panel (result set, plan, server messages, async notifications).
  - **Updatable result sets** with explicit rules: updatable only if all columns come directly from a single table and all PK/OID columns are selected; renamed/duplicated columns read-only; per-column **pencil (editable) / lock (read-only)** icons; grid-identical to View/Edit Data mode.
  - **Transaction semantics surfaced**: with auto-commit off, grid changes join the ongoing transaction; on save errors, changes roll back to an automatically created **SAVEPOINT** so prior statements in the transaction survive.
  - **Connection & transaction status** indicator; change connection mid-session.
  - **Explain panel**: EXPLAIN / EXPLAIN ANALYZE in text/graphical/table renderings; color-coded timing/row misestimates; AI insights tab.
  - **Query history** retained **across sessions per database per user** (default last 20, configurable); internal-tool queries attributable.
  - Messages panel with error underlining in the editor; LISTEN/NOTIFY notification panel; graph visualizer of results; **macros** with `$SELECTION$` placeholder; server-side cursors for large result sets (only in transaction mode); save results to CSV; AI assistant (NL→SQL, schema-aware, with insert/replace actions).
- **Management side**: backup/restore (database/globals/server), maintenance dialog, grant wizard, import/export data, storage manager, named restore points; **Processes** watcher (long-running maintenance jobs); **pgAgent** job scheduling.
- AI features throughout (AI Reports, plan insights) where a provider is configured.

### Layer notes

- All above: Layer A. Precise numbers (history default 20) are documented facts about this product — L3, not promoted.

## Product D — SQL Server Management Studio (SSMS)

*(evidence layer A; overview page only — sub-pages unreachable)*

### Key observations

- Self-description: "an **integrated environment for managing any SQL infrastructure**. Use SSMS to access, configure, manage, administer, and **develop** platforms that use the Microsoft SQL Database Engine" (SQL Server, Azure SQL DB, Managed Instance, Fabric SQL, …).
- "combines a broad group of graphical tools with many rich **script editors** to provide access to SQL Server for **developers and database administrators** of all skill levels."
- Capabilities enumerated: connect securely; **manage objects using Object Explorer and design tools**; "**Query, script, and tune workloads** using the Query Editor, execution plans, and built-in performance tools"; administer BI servers (SSIS/SSAS/SSRS) at server level.
- Development of packages/models/reports explicitly delegated to a **separate** product (SQL Server Data Tools) — the IDE boundary stops at database-engine work.
- Recent highlights: AI assistance (GitHub Copilot chat + code actions), query-hint recommendation tool, modern connection dialog with Fabric browsing and encryption visibility, source control support.

### Layer notes

- All above: Layer A (overview). Deeper UI mechanics (templates browser, registered servers, output panes): **not verified** — do not assert.

---

## Cross-product Comparison

| Dimension | DataGrip | DBeaver | pgAdmin 4 | SSMS |
|---|---|---|---|---|
| Self-label | "IDE for relational and NoSQL databases" | "universal database management tool" | "administration and development platform" for Postgres | "integrated environment for managing… and developing" SQL infrastructure |
| DBMS scope | universal (SQL + NoSQL) | universal (SQL + NoSQL + file/CSV drivers + graph) | single engine (PostgreSQL) | single vendor family (MS SQL ecosystem) |
| Connection concept | data sources | connections/datasources w/ driver manager | registered servers (groups), ad-hoc connections | connections to MS engine family |
| Catalog browsing | attested (schema-aware engine) | Database Navigator tree | Object Explorer tree, full PG object dialogs | Object Explorer + design tools |
| SQL authoring | query console, completion incl. in-buffer objects, dialects, params | SQL editor, per-dialect highlighting, templates, visual builder | Query Tool, autocomplete, macros | Query Editor, script editors |
| Script persistence | local history; console activity tracked | scripts saved as files in projects; console-vs-editor contrast documented | file open/save; history across sessions | "rich script editors" (mechanics unverified) |
| Data editing | export/import attested; grid editing attested only via marketing tier | Data Editor grids, panels, virtual keys | updatable result sets + View/Edit Data with explicit rules | attested as object/design tooling (detail unverified) |
| Plans/performance | (AI optimize; details thin) | execution plans, session/lock managers | EXPLAIN graph/table/statistics + AI insights | Query Editor, execution plans, performance tools |
| Object development | (schema-aware; help unreachable) | object editor, create/alter tutorials | dialog-per-object-type, table editor | design tools |
| Admin depth | thin (dev-first) | extensive administration features (optional pole) | deep: backup/restore, maintenance, roles, pgAgent jobs | deep: manage/administer infrastructure, BI servers |
| Delivery form | desktop (also embedded in other IDEs) | desktop + web server + team server + CLI | web client/server (own users) or desktop | desktop |
| Team/versioning | VCS integration | Git integration, Team Edition | import/export server defs; pgAdmin user mgmt | source control |
| AI assistance | yes (schema/context-aware) | yes (chat, fix, MCP) | yes (NL→SQL, plan insights) | yes (Copilot, preview) |
| Pricing shape | commercial sub, free non-commercial | OSS core + Lite/EE/UE/Team | free OSS | free |

### Stable cross-product reading (Layer B where applicable)

1. Every sampled product centers on **connections to external database systems** and never holds the data of record.
2. Every sampled product exposes a **browsable catalog** of the connected database's objects as the primary navigation surface (Database Navigator / Object Explorer / schema-aware engine / Object Explorer).
3. Every sampled product provides a **SQL authoring → execution → result inspection loop** with dialect awareness.
4. Every sampled product persists the working environment in some form (saved connections; saved scripts and/or query history across sessions; local history).
5. Multiple sampled products (DBeaver, pgAdmin explicitly; SSMS implied) let the user **develop the database itself** — create/alter objects, edit data — not merely query it.
6. Transaction visibility (commit mode, pending transactions, status indicators) is documented in DBeaver and pgAdmin; DataGrip "execute in different modes" is consistent but thinner.
7. Administration depth varies enormously — from DataGrip (thin) to SSMS/pgAdmin (deep) — i.e. **an axis, not the axis**.
8. Multi-DBMS universality vs ecosystem binding is **an axis** (DataGrip/DBeaver vs SSMS/pgAdmin).
9. Delivery form (desktop vs web/server vs embedded component) and audience tuning (business-user Lite edition vs developer-first) are axes.
10. AI assistance appears in all four current-generation products (Layer B, current-market common).

---

## Canonical Abstraction

### L0 — Defining Invariant

```text
Connection to external running database systems (front-end premise; no data of record)
└── Browsable catalog of the connected databases' schema objects
    └── SQL authoring → execution → result inspection loop (dialect-aware)
        └── Development surfaces for the database itself (objects + data), not only queries
            └── Persistent working environment (saved connections, retained scripts/history)
```

Five conjuncts; each is load-bearing:

- Remove the external-database premise → it becomes a data platform / sandbox / warehouse tool.
- Remove the browsable catalog → it degrades to a text editor with a SQL runner (generic IDE territory).
- Remove the SQL execution loop → it becomes a schema-documentation/ER viewer.
- Remove object/data development surfaces → it collapses to a bare query console, i.e. an SQL Client.
- Remove persistence → it becomes an ephemeral console; the "environment" claim dies. (Direct evidence: DBeaver's own docs define the difference between its non-persistent *SQL console* and its persistent *SQL editor*.)

Historical check: older desktop database IDEs (Oracle SQL Developer-era, TOAD-era, DBArtisan/Aqua-era), platform-native file tools (SQLite file browsers), and modern web-deployed tools (CloudBeaver/pgAdmin-as-server) all satisfy these five conjuncts; nothing in the definition presumes a specific era, platform, delivery form, or DBMS scope. Check passed.

### L1 — Common Mature Structure

- Driver-based connectivity abstraction (JDBC/ODBC-class) with a driver manager; broad DBMS support in universal tools.
- Schema-aware assistance: completion over catalog objects (DataGrip even completes objects created in the current buffer), identifier hyperlinks that open object editors, per-dialect highlighting, error/semantic analysis.
- Query history across sessions; scripts organized as files/projects.
- Data editor: spreadsheet-like grids, filters, pagination, updatable result sets with explicit updatability rules.
- Execution-plan visualization and basic performance insight.
- Data import/export (CSV-class formats) and data transfer/migration between connections.
- Transaction surfacing: auto/manual commit modes, pending-transaction indicators, transaction log.
- ER diagrams over live schemas; schema compare/diff; DDL viewing/generation.
- Connection security plumbing: SSH tunnels, SSL/certificates, proxies, secure credential storage, master passwords, enterprise auth (Kerberos/Entra/OAuth2).
- Object editors / dialog-generators for creating and altering catalog objects.
- Cloud-database reach (cloud explorers / hosted-DB drivers) — current-market common.
- AI assistance for query writing, error fixing, plan insight — current-market common.

### L2 — Variant / Optional Structure

- Scope: universal multi-DBMS vs ecosystem-bound (single engine/vendor family).
- Administration depth: dev-first thin (DataGrip) ↔ full administration/backup/jobs (SSMS, pgAdmin) — overlapping the Database Management Console region.
- Delivery: desktop app vs web client/server (tool-owned accounts, e.g. pgAdmin server deployment, CloudBeaver/Team Edition) vs embedded component of a larger IDE vs CLI companion.
- Edition tiering: free/OSS core vs paid tiers; business-user Lite editions vs developer-first editions.
- Team surfaces: VCS integration, server-shared connections/access control.
- Stored-code debugging (PostgreSQL debugger class), job scheduling companions (pgAgent class).
- Deep visual data modeling (ER-model-first design) leans toward Database Schema Design Tool.
- AI posture: built-in multi-model vs bring-your-own vs optional.

### L3 — Vendor-specific (research notes only)

- DataGrip: IntelliJ-platform mechanics (keymaps, themes, VCS), local history, embedded "Database Tools and SQL" in other JetBrains IDEs, AI credits/agent model.
- DBeaver: Eclipse-platform plugin install, data-sources.json admin configuration, workspace location, composite tasks, Liquibase changelog generation, Tableau integration, dbvr CLI, driver-artifact management details.
- pgAdmin: server groups, master password, PSQL tool, PGD replication-node dialogs, Storage Manager, pgAgent, process watcher, MAX_QUERY_HIST_STORED (default 20) — precise default kept here only.
- SSMS: BI server administration (SSIS/SSAS/SSRS), SSDT split for package/model/report development, Copilot integration, query-hint tool, Fabric browsing.

## Rejected Findings

- "A Database IDE is multi-database by definition" — **rejected**: SSMS and pgAdmin are ecosystem-bound yet uncontroversially belong. Universality is L2.
- "A Database IDE includes backup/restore and server administration" — **rejected as definitional**: only some products (DataGrip lacks it and remains an IDE). L1/L2 admin-depth axis.
- "AI assistance is part of the Type" — **rejected**: current-market common (L1), not defining.
- "Web delivery defines the modern form" — **rejected**: desktop remains the dominant realization; pgAdmin/CloudBeaver show web is a variant.
- "The IDE stores the data" — **rejected**: all sampled products are front-ends; data of record stays in the DBMS.
- "File-based project structure is definitional" — **partially rejected**: script persistence is L0, but the *file/project organization shape* is vendor-specific (DBeaver projects, JetBrains consoles).

## Boundary Findings

| Neighbor Type | Shared ground | Discriminator (what flips the Type) |
|---|---|---|
| SQL Client (§12) | connection + SQL execution loop + results | SQL Client is the query surface alone; Database IDE adds the catalog as first-class navigation, object/data development surfaces, and a persistent script workspace. Strip catalog + object/data development from the IDE → an SQL Client. (Products shade into each other; gradient boundary.) |
| Database Management Console (§13) | may administer the same DBMS, same connections | Console's center of gravity is operating the instance (sessions, configuration, availability, backup). IDE's center of gravity is the development loop over objects, data, and SQL. Deep admin depth inside an IDE is a variant, not a Type flip. |
| SQL Workbench / Analytical Query Application (§13) | compose→run→read loop | Those are analytics/analyst-facing query surfaces (governed data spaces, analytical affordances); Database IDE is database-development-facing over raw catalogs. |
| Database Schema Design Tool (§12) | diagrams, DDL, schemas | Design tool's artifacts (models) precede/abstract from a live connection; the IDE's diagrams are views/derivatives of a **live** catalog and its loop is execution, not modeling. |
| Integrated Development Environment (§12) | editor, completion, projects, VCS | General IDE's object world is the file system/codebase; Database IDE's object world is the **live database catalog**. (DataGrip embedding into JetBrains IDEs shows the seam: same tooling, different object world.) |
| Database Dev/Test Environment Manager (§12) | connects to databases, may run SQL | That Type manages **disposable environments** (provisioning, refresh, masking, governance of a fleet); the IDE works on a target database whatever it is. |
| Data Explorer / BI family (§13) | data grids, charts | Those curate data for consumers; the IDE exposes raw catalogs to technical authors. |
| Cloud IDE (§12) | hosted editor shell | Cloud IDE hosts general code development; a browser-delivered database tool remains a Database IDE (form factor is L2). |

Adjacent-leaf consistency (already-processed docs): Data Virtualization doc names "SQL Client / Database IDE" as user-facing tools connecting to one system at a time — consistent. CDC doc names "Database IDE" as a source-side neighbor operating schema/sessions — consistent. API Development Workbench names "SQL Client / Database IDE" as a structural parallel of the compose→execute→inspect→save loop — consistent with this research.

## Boundary Issues (for STATUS.md)

The **Database IDE vs SQL Client** pair shares the most vocabulary. Both leaves exist in DIRECTORY.md and can be held with the environment-breadth discriminator (catalog + object/data development + persistent workspace vs bare query loop), but the boundary is a gradient: the same product is commonly marketed in both roles depending on usage depth. Flagged for potential joint review; no taxonomy rewrite attempted.

## Uncertainties

- DataGrip's operational depth (data editor mechanics, transaction UI, object editor forms) could not be verified — help center unreachable. DataGrip evidence therefore supports positioning + capability claims only.
- SSMS's operational depth (editor mechanics, script files, templates) could not be verified beyond the overview page.
- MySQL Workbench excluded entirely (403); the "visual modeler pole" is therefore described only generically (ER diagrams attested in DBeaver/pgAdmin).
- Historical products (TOAD, SQL Developer, DBArtisan) were used only as unverified sanity checks for the historical-fit question; no specific claims drawn from them.
- Whether every product allows ad-hoc (unregistered) connections is uncertain — pgAdmin's newer workspace layout documents it; others not checked. Ad-hoc connection treated as variant capability.

## Final Synthesis

A Database IDE is a development **environment** for databases: it is a persistent front-end to external database systems, organized around (1) defined connections, (2) a browsable catalog of the live schema, (3) a dialect-aware SQL authoring→execution→result loop, and (4) direct development of the database itself — objects and data — all retained in a working environment of scripts and history. Around that core, mature products add schema-aware assistance, data-grid editing with transaction surfacing, plans and import/export, diagrams, compare/diff, and security plumbing; scope (universal vs ecosystem), administration depth, delivery form, and audience tuning are variant axes. The definition is deliberately independent of era, DBMS scope, and delivery form.
