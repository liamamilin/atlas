# Research Notes — SQL Client

Research date: **2026-09-09**
Leaf: `SQL Client` (DIRECTORY.md §12 Software Development & Product Engineering, line 946)
Slug: `sql-client`

---

## Research Goal

Understand what a SQL Client is as an Application Type: the smallest structure that makes a product recognizable as one, who works in it, how a work session proceeds, and where its boundaries sit against the neighboring database-surface Types.

This pass also **discharges pre-hung cross-check flags** recorded by earlier passes:

1. **database-ide** (processed 2026-09-07): "the two leaves share the connection+query loop; held apart by environment breadth (catalog navigation + object/data development + persistent script workspace vs bare query surface), but the boundary is a gradient — the same products are commonly marketed in both roles depending on usage depth; sql-client should be documented with this joint-review flag in mind."
2. **database-management-console** (processed 2026-09-07): "sql-client + sql-workbench (§12/§13) should apply the same center-of-gravity test (query surfaces, no deployment administration)."
3. **graph-database-explorer** (processed 2026-09-08) + **rdf-sparql-workbench** (processed 2026-09-09): "sql-client + sql-workbench (§12/§13) are the same query-surface family over other engine classes — the console/explorer center-of-gravity test is expected to hold at those passes"; "vs SQL Workbench + SQL Client — engine-class siblings of the same query-surface family, the same test expected to hold at those passes."

## Initial Boundary (hypothesis before research)

A SQL Client is the *query surface alone*: a front-end that connects to a running SQL database system and lets the user work by writing and executing SQL, with results returned in inspectable form. Expected confusions:

1. **vs Database IDE (§12, processed)** — the IDE pass explicitly defined its own L0's removal test as "remove object/data development surfaces → it collapses to a bare query console, i.e. an SQL Client." The client is the smaller core; the IDE = client core + environment structures. Gradient expected.
2. **vs Database Management Console (§13, processed)** — console = deployment-centric administration; client = data/query-centric. Center-of-gravity test expected to hold.
3. **vs SQL Workbench (§13, unprocessed)** — suspected near-alias; vocabularies overlap heavily. Flag for joint review at that pass.
4. **vs engine-class §13 leaves** (Graph Database Explorer, Vector Database Console, Time-series Database Workbench, RDF/SPARQL Workbench) — same family shape, different engine class; the SQL binding should be part of this leaf's invariant.
5. **vs Analytical Query Editor (§13, processed)** — that pass recorded Redshift QE v2 self-describing as a "web-based SQL client application"; platform binding is the discriminator.

## Research Questions

1. What is the smallest structure every SQL client shares? (connection? SQL loop? results?)
2. Is the GUI form factor definitional, or is the terminal client first-class?
3. Is catalog browsing part of the client's core, or a convenience beside the query surface?
4. Is object/data development (create/alter tables, grid editing) part of the core, or the IDE seam?
5. Is persistence (saved connections, saved scripts, history) definitional?
6. How do clients reach databases (drivers, tunnels, auth) and how much plumbing do they own?
7. Where does the client end and the Database IDE / Management Console / SQL Workbench begin?
8. Does the definition survive the oldest form (interactive terminal clients) and engine-native single-dialect clients?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers — deliberately spanning the CLI/GUI axis and the engine-native/universal axis:

| Product | Philosophy / position | Tier & model | Form |
|---|---|---|---|
| psql | PostgreSQL's own interactive terminal; the engine-native CLI pole | free OSS, ships with PostgreSQL | terminal CLI |
| sqlcmd | Microsoft's command-line utility for T-SQL; vendor-ecosystem CLI pole, scriptable | free, ships with / alongside SQL Server | terminal CLI |
| TablePlus | modern commercial native GUI client, multi-DBMS, minimalism ("we only focus on the most important features") | commercial with free tier | desktop GUI (+ iOS) |
| Beekeeper Studio | open-source friendly SQL client, multi-DBMS, team/cloud layer | OSS community edition + paid tiers | desktop GUI |
| HeidiSQL | classic lightweight Windows-heritage client, multi-DBMS, power-tool | free OSS (GPL) | desktop GUI |

MySQL's CLI (`mysql`) was considered but excluded: dev.mysql.com returned HTTP 403 in two prior passes (database-ide, database-schema-design-tool); not retried per the network rule. The MySQL CLI pole is represented structurally (HeidiSQL's command-line parameters are explicitly "based on those used by the MariaDB/MySQL command line applications"; Beekeeper's alternatives map lists the family).

## Sources

Fetched 2026-09-09 (all Layer A — official documentation/product pages):

- psql reference — https://www.postgresql.org/docs/current/app-psql.html
- sqlcmd utility — https://learn.microsoft.com/en-us/sql/tools/sqlcmd/sqlcmd-utility
- TablePlus product page — https://tableplus.com/
- Beekeeper Studio product page — https://www.beekeeperstudio.io/
- HeidiSQL help — https://heidisql.com/help.php

Unreachable / degraded:

- docs.beekeeperstudio.io — transport error (1 attempt, abandoned per network rule); Beekeeper evidence limited to its product page
- dev.mysql.com / mysql.com — HTTP 403 in prior passes; not retried
- TablePlus docs not fetched (product page only); operational depth unverified

Prior-pass context (read, not fetched this pass): research/database-ide.md, research/database-management-console.md, research/graph-database-explorer.md, research/rdf-sparql-workbench.md, STATUS.md boundary entries.

---

## Product A — psql (PostgreSQL interactive terminal)

*(Layer A: official reference page)*

### Key observations

- Self-description: "psql is a **terminal-based front-end to PostgreSQL**. It enables you to type in queries interactively, issue them to PostgreSQL, and see the query results. Alternatively, input can be from a file or from command line arguments."
- Client premise, verbatim: "psql is a **regular PostgreSQL client application**. In order to connect to a database you need to know the name of your target database, the host name and port number of the server, and what database user name you want to connect as."
- Connection specification: command-line options (`-d`, `-h`, `-p`, `-U`), environment variables (PGDATABASE/PGHOST/PGPORT/PGUSER), conninfo strings and URIs (`psql "service=myservice sslmode=require"`, `psql postgresql://dbmaster:5433/mydb?sslmode=require`), LDAP lookup, `.pgpass` password file.
- **The SQL conversation**: prompt `testdb=>`; "the user can type in SQL commands. Ordinarily, input lines are sent to the server when a command-terminating semicolon is reached… If the command was sent and executed without error, **the results of the command are displayed on the screen**."
- **Meta-commands** (backslash commands) processed by psql itself: `\d` family (describe relations/functions/types — catalog *inspection*), `\l` (list databases), `\c`/`\connect` (switch connection), `\copy` (client-side bulk copy between server and local file system), `\o` (output to file), `\i` (read commands from file), `\pset` (output formats: aligned/unaligned/CSV/HTML/LaTeX), `\g`, `\bind` (query parameters via extended protocol), `\conninfo`, `\crosstabview`, `\watch`.
- Scripting/automation: `-c` command strings, `-f` script files, `--single-transaction` wrapping, `ON_ERROR_STOP`, defined exit statuses (0/1/2/3), single-step mode for debugging scripts, echo options.
- Readline: line editing and command history.
- LISTEN/NOTIFY asynchronous notification polling after each command.
- No GUI, no object editors, no saved-connection manager (connection is per-invocation), no result grid — the interactive loop is the whole product.

### Layer notes

All Layer A. psql doubles as the historical pole: the interactive terminal loop it documents is the oldest form of the Type, still first-class today.

## Product B — sqlcmd (Microsoft)

*(Layer A: official utility documentation)*

### Key observations

- Self-description: "Use the **sqlcmd** utility to **enter Transact-SQL statements, system procedures, and script files** through various modes: At the command prompt. In Query Editor in SQLCMD mode. In a Windows script file. In an operating system job step of a SQL Server Agent job."
- Two variants documented: **sqlcmd (Go)** — standalone cross-platform tool (go-mssqldb based); **sqlcmd (ODBC)** — platform-aligned, ships with SQL Server / mssql-tools.
- Connection: `-S [protocol:]server[instance][,port]` (tcp/lpc/np), `-U`/`-P`, `-E` trusted connection, `-G` Microsoft Entra ID, DSN support (`-D`), encryption options (`-N` mandatory/optional/strict, `-C` trust certificate, `-F`/`-J` certificate pinning), dedicated administrator connection (`-A`), login timeout.
- **Query execution**: `-q` (run at start, stay), `-Q` (run and exit), `-i` input files (multiple, processed in order), batch terminator `GO` (customizable via `-c`), query timeout.
- **Output**: `-o` output file, column separator/width/headers options, display-width truncation for large types, Unicode output, vertical format (Go variant), performance statistics (`-p`).
- **Scripting variables**: `SQLCMDDBNAME`, `SQLCMDPASSWORD`, `SQLCMDSERVER`… set via `-v` or `:setvar`; `$(var)` substitution in scripts; `-x` to disable substitution.
- Interactive commands: `:connect` (switch connection mid-session), `:r` (read file), error-handling switches (`-b` ERRORLEVEL, `-m` error level, `-V` severity).
- No GUI, no catalog tree, no grid editing — batch/interactive T-SQL execution is the whole product.

### Layer notes

All Layer A. Precise defaults (login timeout 8s, packet size 4096, width 80) are documented product facts — L3, not promoted.

## Product C — TablePlus

*(Layer A: official product page; docs not fetched)*

### Key observations

- Self-description: "Modern, native, and friendly **GUI tool for relational databases**: MySQL, PostgreSQL, SQLite & more"; page title "Modern, Native Tool for Database Management."
- Multi-DBMS: MySQL, PostgreSQL, SQL Server, SQLite, Redis, MariaDB, Redshift, MongoDB, CockroachDB, Oracle, Cassandra, BigQuery, ClickHouse, Turso.
- **Inline edit**: "Edit data rows, table structure, or query results directly with just a click."
- **Advanced filters** over records; **code review** ("Always stay in control of what you have changed on your database"); **safe mode** ("Prevent any mistakes from being made on your production database").
- **Export & import database** (SQL dump migration).
- **Open anything**: "A quick jump to a table, schema, database, view, function, literally anything from your connection."
- **Multiple tabs & windows** across databases/connections.
- **Smart query editor**: instant autocomplete, syntax highlighting, split panes, SQL reformatter, favorite & history, streaming results.
- Metrics Board (internal dashboards); native builds for macOS/Windows/Linux/iOS; plugin extensibility (beta).
- Philosophy: "We don't want to be an app that does many things, but masters none. We only focus on the most important features."

### Layer notes

All Layer A (product page). Operational mechanics (transaction handling, connection dialogs) not verified — do not assert.

## Product D — Beekeeper Studio

*(Layer A: official product page; docs domain unreachable)*

### Key observations

- Self-description, verbatim: "A modern, easy to use, and good looking **SQL client** for MySQL, Postgres, SQLite, SQL Server, Firebird, and more. Oh, it's also open source :-)." — direct market use of the Type's name.
- Supported databases: MongoDB, MySQL, PostgreSQL, SQLite, SQL Anywhere, SQL Server, BedrockDB, Cassandra, ClickHouse, CockroachDB, DuckDB, DynamoDB, Firebird, BigQuery, Greengage, libSQL, MariaDB, Oracle, Redis, Redshift, ScyllaDB, Snowflake, StarRocks, SurrealDB, TiDB, Trino.
- **Connect through firewalls**: SSL encryption, SSH tunneling, encrypted saved connection passwords.
- **Write SQL**: built-in editor with syntax highlighting and auto-complete "for your tables"; saved queries and connections organized in folders.
- **AI Shell**: connects the database with an AI model; "can explore your schema, run SQL (with permission) and check its work with real data."
- **Open lots of tabs**; **easily view & edit data**: "Open tables in a spreadsheet-like interface to browse and edit, or modify cells directly in your SQL query results with a single click"; JSON editing with highlighting.
- **Create tables without writing SQL**: table creator with indexes and foreign keys.
- **Import & export**: create a table from CSV; export to CSV/JSON/JSONL/SQL with filters.
- **Cloud Workspaces**: sync connections and saved queries across devices, share with teams, per-item permissions; "Workspace data is encrypted at rest and in transit, and we never see the rows you query."
- Commitments: works offline, privacy-respecting, open-source community edition.
- **Market map**: Beekeeper's own alternatives index lists the SQL-client family: DBeaver, DataGrip, TablePlus, pgAdmin, Navicat, Azure Data Studio, DBVisualizer, HeidiSQL, MySQL Workbench, Oracle SQL Developer, phpMyAdmin, PopSQL, Postico, psql, RazorSQL, Sequel Pro, SSMS, DB Browser for SQLite, SQLPro Studio, SQuirreL SQL, Valentina Studio — direct evidence of the product population's breadth.

### Layer notes

All Layer A (product page). Operational depth unverified (docs unreachable).

## Product E — HeidiSQL

*(Layer A: official help page)*

### Key observations

- **Client premise, verbatim**: "HeidiSQL is a so called ***client* application, only usable when you have some *server* available**. So, make sure you have some MariaDB, MySQL, MS SQL, PostgreSQL server or SQLite database file to connect to."
- **Session manager**: stored sessions in folders; credential prompting; Windows authentication; SSH tunnel connections (plink/ssh) with explicit local-port forwarding setup; per-session database filtering; SQLite file + cipher encryption.
- **Driver libraries**: "HeidiSQL needs a database-specific dynamic library for connecting to your server" (libmysql/libmariadb/libpq/sqlite3/Interbase/Firebird clients).
- **Database tree**: objects grouped by type; favorites; per-database filtering.
- **Object development convenience**: GUI editors for creating tables, views, stored procedures/functions, triggers, scheduled events (right-click → Create new).
- **Data tab**: grid display of table/view contents; F2 cell editing; quick filters generating WHERE clauses; client-side filter panel; BLOB hex/text toggle; UNIX-timestamp rendering.
- **Query tabs**: multiple query tabs; write queries or load .sql files; F9 execute; configurable query delimiter for compound statements; "query helpers" panel (columns of selected table, reserved words, SQL functions, generate SELECT/INSERT/UPDATE/DELETE); query profile (SHOW PROFILE-based timings); bind parameters; batch execution "in one go".
- **SQL export**: mysqldump-like output to .sql file / ZIP / clipboard / another database on the same or another configured server; structure-only or with INSERT data; import of .sql/.csv/BLOB files.
- **Command line switches**: connect and open .sql files in query tabs from the CLI; parameters "based on those used by the MariaDB/MySQL command line applications, e.g. mysqldump"; portable mode.

### Layer notes

All Layer A. HeidiSQL is the gradient specimen: a self-described *client* that also carries object-development editors — evidence that object development appears in clients as convenience, not as the organizing environment.

---

## Cross-product Comparison

| Dimension | psql | sqlcmd | TablePlus | Beekeeper Studio | HeidiSQL |
|---|---|---|---|---|---|
| Self-label | "terminal-based front-end" / "regular PostgreSQL client application" | "utility to enter Transact-SQL statements… and script files" | "GUI tool for relational databases" / "Native Tool for Database Management" | "SQL client" (verbatim) | "so called client application, only usable when you have some server available" |
| DBMS scope | engine-native (PostgreSQL) | vendor-ecosystem (SQL Server family) | universal (14+ engines) | universal (26 engines listed) | multi-DBMS (MariaDB/MySQL/MSSQL/PostgreSQL/SQLite + Interbase/Firebird) |
| Form factor | terminal CLI | terminal CLI | native desktop GUI (+iOS) | desktop GUI (Electron-class) | desktop GUI (Windows-heritage) |
| Connection model | per-invocation flags/env/conninfo/URI; `.pgpass`; `\connect` switch | flags/env/DSN; `:connect` switch; protocols tcp/lpc/np | saved connections; multiple tabs & windows | saved connections in folders; SSH tunnel; SSL | session manager with folders; SSH tunnel; SSL; Windows auth |
| SQL as primary interface | interactive prompt + `-c`/`-f` scripts | interactive + `-q`/`-Q`/`-i` batches | smart query editor (autocomplete, highlighting, reformatter, split panes) | SQL editor (highlighting, autocomplete, saved queries) | query tabs (F9 execute, .sql files, delimiter, helpers, bind params) |
| Results | displayed at prompt; formats aligned/unaligned/CSV/HTML/LaTeX; `\o` file | result sets with separator/width/headers options; `-o` file; vertical format | streaming results; inline edit of query results | result grids; edit cells in results | results pane; data tab grid; quick filters |
| Catalog inspection | `\d` family, `\l` (meta-command convenience) | none documented | sidebar + "open anything" jump | sidebar | database tree (group by type, favorites) |
| Object development | none | none | edit table structure | table creator without SQL | GUI editors: table/view/procedure/trigger/event |
| Data-grid editing | none (bulk `\copy` only) | none | inline edit | spreadsheet-like edit | data tab grid edit |
| Script/automation | `-c`/`-f`, single-transaction, ON_ERROR_STOP, exit codes | `-i`/`-q`/`-Q`, scripting variables, ERRORLEVEL, Agent job steps | — | — | CLI switches; open .sql files; portable mode |
| Import/export | `\copy` (client-side) | `-i`/`-o` files | SQL dump export/import | CSV/JSON/JSONL/SQL both ways | SQL export (file/zip/clipboard/other DB), .sql/.csv/BLOB import |
| History/persistence | Readline history; `\i` files | scripting variables; input files | favorite & history | saved queries in folders; cloud sync | sessions; .sql files |
| Team/cloud | — | — | — | Cloud Workspaces (sync, share, per-item permissions) | — |
| AI | — | — | — | AI Shell (schema explore, run SQL with permission) | — |
| Dashboards | — | — | Metrics Board | — | — |
| Safety postures | single-step mode; ON_ERROR_STOP | `-b`/`-V` error gates | safe mode; code review | — | — |

### Stable cross-product reading (Layer B where applicable)

1. **Every sampled product is a front-end to an external running SQL database system** and holds no data of record. Two products state the client premise verbatim (psql: "regular PostgreSQL client application"; HeidiSQL: "client application, only usable when you have some server available").
2. **Every sampled product's primary working interface is SQL itself** — typed at a prompt, written in an editor, or supplied as a script file. No sampled product replaces SQL authorship with a form/visual layer as the primary path (Beekeeper's table creator and HeidiSQL's editors are conveniences beside it).
3. **Every sampled product returns results in inspectable form** — row sets plus status/error feedback, displayed at a prompt or in a grid.
4. **Form factor is an axis, not the definition**: the terminal CLI pole (psql, sqlcmd) carries the full defining core with no GUI at all.
5. **Catalog inspection is common but convenience-grade**: psql's `\d` meta-commands, HeidiSQL's tree, TablePlus's "open anything", Beekeeper's sidebar — all sit *beside* the query surface; none organizes the product around the catalog as the IDE does.
6. **Object/data development is the IDE seam**: entirely absent from the CLI pole; present as convenience editors in GUI clients (HeidiSQL, Beekeeper, TablePlus). Its presence/depth is a gradient, not a binary.
7. **Persistence is common, not definitional**: psql's interactive session (per-invocation connection, no saved-connection manager) satisfies the core with none of it.
8. **Connectivity plumbing (SSH tunnels, SSL, encrypted credential storage, driver libraries) is common mature structure** across GUI clients; CLI clients carry the equivalent (conninfo/SSL options, protocols, env vars).
9. **Scripting/automation surfaces** (batch files, variables, exit codes, single-transaction wrapping) are common in CLI clients and absent in GUI clients — an axis.
10. **Team/cloud sync, AI assistance, dashboards** appear in single products (Layer A single-source) — optional/era-current, not definitional.

---

## Canonical Abstraction

### L0 — Defining Invariant

```text
Connection to an external running SQL database system (client premise; no data of record)
└── SQL as the primary working interface (author → execute against the connection)
    └── Results returned in inspectable form (row sets + status/error feedback)
```

Three conjuncts; the SQL binding is part of the invariant (remove SQL → a generic database client or an engine-class sibling). Each is load-bearing:

- Remove the external-database premise → it becomes a driver/library or a connection manager; the client dies.
- Remove SQL as the primary interface → it becomes a point-and-click data browser (data-explorer territory) or a bare connection manager.
- Remove inspectable results → it becomes fire-and-forget execution (a batch runner), not a conversation with the database.

Jointly-held load-bearing:

- 1 alone = connection manager / driver
- 2 without 1 = SQL tutorial / formatter / offline playground
- 3 without 2 = pre-canned reporting or GUI-only data browser
- 1+2 without 3 = blind batch execution
- 1+3 without 2 = point-and-click browser, not an SQL client

Historical check: the interactive terminal client — the oldest form of the Type (the 1970s–90s monitor/isql/SQL*Plus lineage, and psql itself, whose documented loop is exactly this) — satisfies all three conjuncts with no GUI, no autocomplete, no saved connections, no grid editing. Engine-native single-dialect clients (psql, sqlcmd) and universal multi-DBMS clients (TablePlus, Beekeeper, HeidiSQL) both satisfy. Nothing in the definition presumes an era, a form factor, a DBMS scope, or a delivery model. **Check passed.**

### L1 — Common Mature Structure

- Saved connections / session manager (GUI pole); connection strings/env vars/password files (CLI pole).
- Catalog inspection beside the query surface: sidebar trees, describe meta-commands (`\d` class), quick-jump palettes — read-mostly convenience.
- Editor affordances: syntax highlighting, autocomplete over catalog objects, formatting/reformatting, multiple query tabs.
- Query history; saved queries/scripts; favorites.
- Result-grid data editing (GUI pole) — spreadsheet-like cell editing, quick filters, editable query results.
- Import/export: CSV/JSON/SQL-dump both directions; client-side bulk copy (`\copy` class).
- Connectivity plumbing: SSH tunnels, SSL/TLS with certificate options, encrypted credential storage, driver libraries, Windows/Entra-class auth.
- Execution feedback: timing/profiles, row counts, error levels/severity gates.
- Output formatting and redirection (aligned/unaligned/CSV/HTML; output files).
- Scripting/automation surfaces in CLI clients: batch files, scripting variables, exit codes, single-transaction wrapping.

### L2 — Variant / Optional Structure

- Form factor: terminal CLI ↔ native desktop GUI ↔ web-delivered variants (family-wide).
- Scope: engine-native single-dialect client ↔ universal multi-DBMS client.
- Object-development convenience (create/alter tables, views, routines via GUI) — the IDE seam; present in some GUI clients, absent in CLI.
- Automation posture: the client as a script endpoint (Agent job steps, cron + psql) vs purely interactive.
- Team/cloud sync of connections and saved queries (single-product in-sample).
- AI assistance (single-product in-sample) — era-current.
- Dashboards/metrics boards (single-product in-sample).
- Safety postures: safe mode / read-only production protection, code review of pending changes (single-product in-sample), error-severity gates (CLI).
- Parameterized queries / bind variables.

### L3 — Vendor-specific (research notes only)

- psql: meta-command vocabulary (`\d`, `\copy`, `\pset`, `\bind`, `\g`, `\watch`, `\crosstabview`), `.psqlrc` startup file, ON_ERROR_STOP, single-step mode, LISTEN/NOTIFY polling, exit-status code 0/1/2/3 semantics, extended-protocol testing commands.
- sqlcmd: scripting-variable namespace (SQLCMD*), `GO` batch terminator, `:connect`/`:r`/`:setvar` commands, ERRORLEVEL semantics, DAC (`-A`), Go-vs-ODBC variant split, TDS 8.0 support.
- HeidiSQL: session-manager folders, query-helpers panel with generate-SELECT/INSERT/UPDATE/DELETE, quick-filter menus, BLOB hex/text toggle, custom query delimiter, portable mode, plink-based SSH tunneling, mysqldump-parameter-compatible CLI.
- TablePlus: native-app philosophy, safe mode, code review, Metrics Board, iOS companion, plugin system (beta).
- Beekeeper: Cloud Workspaces with per-item permissions, AI Shell, works-offline commitment, alternatives market map.

## Rejected Findings

- "A SQL client is a GUI application" — **rejected**: the CLI pole (psql, sqlcmd) carries the full defining core with no GUI.
- "A SQL client is universal / multi-DBMS" — **rejected**: engine-native clients (psql, sqlcmd) are uncontroversially the Type; scope is a variant axis.
- "A SQL client browses the schema in a tree" — **rejected as definitional**: psql's `\d` is a meta-command convenience; the CLI pole has no tree. Common, not core.
- "A SQL client edits data in grids" — **rejected as definitional**: absent from the CLI pole entirely. Common in GUI clients.
- "A SQL client saves connections and scripts" — **rejected as definitional**: psql's per-invocation connection model satisfies the core with none of it. Common, not core.
- "A SQL client creates/alters tables" — **rejected as definitional**: absent from the CLI pole; present as convenience in GUI clients; deep object development is the Database IDE's distinguishing addition.
- "A SQL client administers the server (users, backups, configuration)" — **rejected as definitional**: no sampled client centers deployment administration; that is the Database Management Console's center of gravity. (HeidiSQL's user-management surface exists but is peripheral — held optional/variant, unverified in depth.)
- "AI assistance is part of the Type" — **rejected**: single-product, era-current.

## Boundary Findings

| Neighbor Type | Shared ground | Discriminator (what flips the Type) |
|---|---|---|
| **Database IDE (§12, processed)** | connection + SQL authoring→execution→result loop + results | Environment breadth. The IDE adds: catalog as *primary navigation*, object/data development surfaces, a persistent script workspace (DBeaver's own console-cannot-save vs editor-saves line). The client is the query surface alone; its catalog view (where present) is a convenience beside the query surface, not the organizing frame; object development is absent (CLI) or convenience-grade (GUI). Test: strip catalog-as-frame + object/data development + persistent workspace from the IDE → an SQL client; accrete them onto a client → it becomes an IDE. **Gradient, not a wall** — the same products are marketed in both roles depending on usage depth (DBeaver Lite "data viewing and query execution" vs EE "SQL development tools"; HeidiSQL and Beekeeper carry table editors while self-labeling as clients). |
| **Database Management Console (§13, processed)** | may connect to the same engines; some clients carry peripheral admin conveniences | Center of gravity: the console's object is the *running deployment* (lifecycle, configuration, backups, state-aware administration); the client's object is the *data/query loop*. Test holds: remove query authoring → console remains; remove deployment administration → client remains. No sampled client centers deployment administration. |
| **SQL Workbench (§13, unprocessed)** | the same query-surface family; vocabularies overlap heavily | Expected to hold the same family tests (engine-class sibling). From this side the two leaves look like **near-aliases**: the analytical-query-editor pass recorded "sql-workbench = connection-agnostic general SQL tooling", which reads as this Type's definition. The §12/§13 placement suggests an intended developer-facing (§12) vs data/analytics-facing (§13) split, but the market does not clearly split products along that line (Beekeeper self-labels "SQL client" while serving analyst-style workflows). **Flagged for joint review when SQL Workbench is processed.** |
| **Analytical Query Editor (§13, processed)** | SQL editor + execution + result grid | Platform binding: that Type is bound to ONE analytical platform's data space; the client is connection-agnostic across engines. Vocabulary overlap acknowledged (Redshift QE v2 self-describes as a "web-based SQL client application") — consistent with that pass's gradient framing. |
| **Ad-hoc Query Application (§13, processed)** | SQL composition and execution | Audience and abstraction: ad-hoc is a governed question layer for business users; the client is an SQL-first technical surface. |
| **Graph Database Explorer / Vector Database Console / Time-series Database Workbench / RDF-SPARQL Workbench (§13)** | interactive query surface over a live database | Engine class: those bind to graph/vector/time-series/RDF engines and their query languages; this leaf binds to SQL-speaking relational (and SQL-speaking analytical) systems. The engine-class binding is part of each invariant. **Ratified from this side** — the family test the explorer and workbench passes expected holds. |
| **Data Explorer / BI family (§13)** | data grids, filters | Those curate data for consumers; the client exposes raw SQL to technical users. |
| **Database Schema Design Tool (§12, processed)** | DDL, tables | The design tool's artifact is an offline model that precedes a live connection; the client's loop is execution against a live connection. |
| **Database Sandbox / Dev-Test Environment Manager (§12, processed)** | connects to databases | Those manage disposable environments (provision/refresh/mask); the client works on whatever target it is pointed at. |
| **Driver / CLI library** | executes SQL against a server | A driver has no user-facing conversation surface; the client is the interactive/scriptable surface *over* the driver (HeidiSQL's own docs: the client "needs a database-specific dynamic library for connecting"). |

## Boundary Issues (for STATUS.md)

1. **database-ide joint-review flag DISCHARGED from this side** — keep-both RATIFIED on the environment-breadth seam (query surface alone vs catalog-as-frame + object/data development + persistent workspace), with the gradient explicitly documented in both directions (client-side specimens: HeidiSQL/Beekeeper table editors; IDE-side specimen: DBeaver's console-vs-editor line). Both documents cross-reference.
2. **database-management-console center-of-gravity test APPLIED and holds** — the client's object is the data/query loop; no sampled client centers deployment administration.
3. **Engine-class family test RATIFIED** — graph-database-explorer / rdf-sparql-workbench expectations confirmed; the SQL binding is part of this leaf's invariant.
4. **NEW flag: SQL Client (§12) vs SQL Workbench (§13, unprocessed)** — suspected near-alias; vocabularies overlap; the §12/§13 placement suggests a developer-vs-analytics audience split the market does not clearly honor. Joint review flagged for the SQL Workbench pass.
5. Taxonomy observation (no action): the SQL-client product population (per Beekeeper's own alternatives map) spans tools the directory places in §12 (Database IDE, Schema Design Tool) and §13 (analytical editors, engine-class explorers) — the client is the *shared core* of that family, not a competitor to those leaves.

## Uncertainties

- TablePlus evidence is product-page-only; operational mechanics (transaction handling, connection dialogs, export depth) unverified — no precise claims drawn.
- Beekeeper's docs domain was unreachable (transport error ×1, abandoned); operational depth unverified; Cloud Workspaces/AI Shell claims held at product-page strength.
- HeidiSQL's user-management surface (forum-mentioned) not verified — administration held optional/variant, not asserted as a capability.
- The MySQL CLI pole (`mysql`) excluded (dev.mysql.com 403 in prior passes); represented structurally only.
- Historical CLI clients (isql, SQL*Plus, Query Analyzer) used as conceptual lineage only — not fetched, no specific claims.
- Whether web-delivered pure clients (browser-only, no install) form a distinct sub-population was not researched; the family's web members known from prior passes (CloudBeaver, Redshift QE v2) sit at the IDE/editor seams.

## Final Synthesis

A **SQL Client** is the query surface of the database-tool family: a front-end that connects to an external running SQL database system, takes SQL as its primary working interface — typed interactively, written in an editor, or supplied as a script — and returns results in inspectable form (row sets plus status/error feedback). That three-part core is the whole definition; it is deliberately smaller than the Database IDE (which adds catalog-as-primary-navigation, object/data development, and a persistent workspace) and does not include the Management Console's deployment administration. Around the core, mature products add saved connections, catalog inspection, editor affordances, query history, result-grid editing, import/export, and connectivity plumbing; form factor (terminal ↔ GUI), scope (engine-native ↔ universal), automation posture, team sync, and AI assistance are variant axes. The definition is era-agnostic — the interactive terminal client, the Type's oldest form, satisfies it completely today.
