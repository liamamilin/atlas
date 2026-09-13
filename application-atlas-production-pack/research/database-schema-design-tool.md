# Research Notes — Database Schema Design Tool

Research date: **2026-09-07**
Leaf: `Database Schema Design Tool` (DIRECTORY.md §12 Software Development & Product Engineering)
Slug: `database-schema-design-tool`

---

## Research Goal

Understand what a Database Schema Design Tool is as an Application Type: the objects inside it, the users, the working loops, the interfaces, the rules that govern behavior, and — critically — how it is distinguished from the neighboring leaves in the same directory region:

- Database IDE (§12, processed — this pass ratifies the boundary its research flagged)
- SQL Client (§12), Database Management Console (§13, processed), SQL Workbench (§13)
- Database Sandbox Platform (§12, processed — its pass named this leaf as a neighbor)
- Diagramming Application (§03.05/§12 region, processed — its pass named this leaf as a semantics-carrying sibling)
- API Design Platform (§12, processed — its pass recorded a "clean" boundary)
- Software Architecture Modeling / System Design Application (§12)
- Low-code / No-code Application Builders (§12)

## Initial Boundary (hypothesis before research)

A Database Schema Design Tool is a tool whose object of work is a **schema model**: an editable, persistent, database-semantic definition of a database structure (tables with typed columns, keys, constraints, relationships), presented as an entity-relationship diagram and realized as concrete schema artifacts (DDL) for a specific DBMS dialect.

Adjacent confusions expected up front:

1. **vs Database IDE** — both may show diagrams and both may touch live databases. Suspected discriminator: the IDE's object world is a *live* catalog and its loop is execution; the design tool's object world is a *model* that precedes or abstracts from any live database. (The processed Database IDE research already states this; this pass must verify it from the design-tool side.)
2. **vs Diagramming Application** — both draw ER-style diagrams. Suspected discriminator: schema semantics (typed columns, keys, FK constraints) and schema generation; a diagramming tool draws pictures of schemas, not managed schemas.
3. **vs SQL Client / Management Console** — those operate live instances; no persistent design model.
4. **Is "visual canvas editing" definitional?** — suspected NO: a code-first pole (schema-as-code with rendered diagram) plausibly belongs to the Type. Must test.
5. **Is "connecting to a live database" definitional?** — suspected NO: reverse engineering is an input mode, not the defining loop.

## Research Questions

1. What is the central artifact — diagram, model, project, file? How do model and diagram relate?
2. What schema constructs does the model cover (tables, columns, types, keys, constraints, indexes, enums, views, routines)? Are constructs dialect-specific?
3. How is the model edited — canvas-first, form-first, code-first? Does the diagram render from the model or is the canvas the store?
4. What does the model produce — full DDL, migration/ALTER scripts, direct schema creation? Which dialects?
5. How do models enter the tool — blank, SQL script import, live-database reverse engineering?
6. How does the tool treat a change of target dialect (type remapping, conversion)?
7. What lifecycle does the model have — versions, history, diffs, review/approval, team collaboration?
8. What adjacent capabilities live inside such tools (data browsing, generators, documentation, publishing) and where is the line?
9. Who uses these tools and in what team context?
10. Where does the Type end vs Database IDE, Diagramming Application, SQL Client, Sandbox Platform, API Design Platform, and generic architecture modeling?
11. Does the definition survive older (ERwin/PowerDesigner-era), ecosystem-bound, desktop-file, and code-first products?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

| Product | Philosophy / position | Tier & model |
|---|---|---|
| dbdiagram.io | code-first (DBML "database diagram as code"), web, lightweight | free + professional subscriptions; part of the Holistics dbx family |
| DbSchema | visual model-first desktop designer, universal multi-DBMS (70+ SQL & NoSQL), offline-capable | free Community Edition + Pro/Architect commercial |
| SqlDBM | web enterprise data-modeling platform for cloud data platforms (Snowflake/Databricks/BigQuery era), collaboration + governance | commercial SaaS, enterprise tier |
| Redgate Data Modeler (formerly Vertabelo) | web collaborative physical data modeling, SQL generation | commercial SaaS (Redgate) |
| DrawSQL | team schema-diagram tool, SQL import → diagram → DDL export, multiplayer | free + paid SaaS, developer-team tier |

MySQL Workbench (vendor-ecosystem classic modeling pole) was considered but **excluded as an evidence source**: dev.mysql.com returned HTTP 403 on repeated attempts (same finding as the processed Database IDE pass on the same date). Historical ERwin / PowerDesigner / Oracle CASE-era tools are used only as unverified historical-fit sanity checks; no specific claims drawn from them.

## Sources

Fetched 2026-09-07:

- dbdiagram docs root — https://dbdiagram.io/docs
- DBML reference (core syntax) — https://dbml.dbdiagram.io/docs/
- DBML database support matrix — https://dbml.dbdiagram.io/database-support
- DbSchema documentation root — https://www.dbschema.com/docs/
- DbSchema Tables, Columns & Indexes — https://www.dbschema.com/documentation/schema.html
- DbSchema Synchronize with the Database — https://www.dbschema.com/documentation/synchronize-database.html
- SqlDBM product page — https://www.sqldbm.com/
- Redgate Data Modeler documentation home — https://vertabelo.com/documentation (redirects to Redgate docs; product page states "formerly known as Vertabelo")
- DrawSQL landing page — https://drawsql.app/

Unreachable / degraded:

- dev.mysql.com / mysql.com — HTTP 403 (MySQL Workbench excluded from evidence; consistent with the Database IDE pass)
- SqlDBM Help Center (support.sqldbm.com category page) — request timed out; SqlDBM evidence limited to its product page (Tier 2)
- dbdiagram.io sub-pages under /basic-editing-experience and /dbml — JavaScript-rendered, returned empty bodies; dbdiagram editor-canvas mechanics not directly verified (DBML reference site does verify the language and its SQL mapping)

---

## Product A — dbdiagram.io

*(evidence layer A: docs root + DBML reference + support matrix)*

### Key observations

- Self-description: "a free, simple tool to draw database diagrams (ERDs) by **typing DSL code**. dbdiagram uses the popular DBML (Database Markup Language)." DBML is branded "Database Definition As Code".
- **The model is code; the diagram renders from it.** The DBML core-syntax page states: "This part covers all constructs that define database structure and **map directly to SQL output**."
- **Target dialect declared inside the model**: `Project project_name { database_type: 'PostgreSQL' ... }` — the DBMS target is a property of the model itself.
- Constructs attested in DBML: schemas (default `public`); tables; columns with types (parenthesized types like `varchar(255)`, `decimal(1,2)` supported as-is; spaced types quoted); column settings (`pk`, `null`/`not null`, `unique`, `default:` incl. expression defaults in backticks, `increment`, `check` expressions); composite primary keys via index blocks; indexes (single, composite, expression-based; `type: btree|hash`); relationships (`Ref`) in four cardinality kinds (`<` one-to-many, `>` many-to-one, `-` one-to-one, `<>` many-to-many) with per-side optionality (`>?` nullable FK side), referential actions (`delete/update: cascade|restrict|set null|set default|no action`), composite foreign keys, cross-schema relationships; enums; TablePartial (reusable field/settings/index sets injected into tables with defined conflict resolution); Records (sample data rows, CSV-style, type-checked against column SQL types).
- **SQL import and export**: support matrix — SQL→DBML import supported for PostgreSQL, MySQL, MSSQL, Oracle, Snowflake; DBML→SQL export for PostgreSQL, MySQL, MSSQL, Oracle; live-database connectors (via `@dbml/connector`) for PostgreSQL, MySQL, MSSQL, Oracle, Snowflake, BigQuery. Import/export also available programmatically via the `@dbml/core` JS module, CLI, and a VS Code extension ("Use dbdiagram locally").
- Product surfaces attested in docs navigation: Diagram Views; Version History; Sharing & Collaboration (workspaces, real-time collaboration, password-protected & private diagrams, embedding diagrams in other applications, "DBML-in-Link" share without an account); working with complex diagrams (detail levels, table groups, sticky notes, header/relationship colors); AI Assistant; SAML/SSO authentication; free vs professional plan split.
- Sibling product in the same vendor family: **dbdocs** ("Database Docs As Code") — documentation rendering exists as a separate product, not the diagram tool itself.

### Layer notes

- All above layer A. Canvas-interaction mechanics (drag behavior, auto-layout specifics) **not verified** — JS pages empty; do not assert.

## Product B — DbSchema

*(evidence layer A: docs root, schema page, synchronize page — deepest documentation of the sample)*

### Key observations

- Self-description: "a **visual database design and management tool** for 70+ SQL and NoSQL databases."
- Three ways to start a project: **connect to a database to reverse-engineer an existing schema**; **design from scratch** on a blank canvas; **import from file** (SQL, CSV, SQLite data).
- **Design model**: "The **design model** is a single `.dbs` file that stores your schemas, diagrams, queries, and saved editors. You can work offline, share the file via Git, and reopen it without a live database connection."
- **Offline design is explicit**: "Create and modify tables in the model **without affecting any live database**. When you are ready, connect to a target database and deploy your changes with schema synchronization." FAQ: "Can I design tables in DbSchema without a live database? **Yes.** DbSchema supports offline design."
- Diagrams: interactive; double-click a table on the canvas to open an inline editor (columns, data types, primary keys, comments); changes reflected instantly; **multiple diagrams per project** saved in the same project file (one per module/microservice/feature area); view detail toggles (show data types, hide/show FK columns, relationship labels); primary-key columns highlighted with a key icon.
- Schema constructs (Tables/Columns/Indexes page): schema as named container/namespace; tables; columns with data types incl. precision/scale; NOT NULL; defaults; `Unsigned` (MySQL-specific, flagged as such); `Identity/Auto-increment` with documented dialect variance (MySQL `AUTO_INCREMENT` vs PostgreSQL/SQL Server `IDENTITY`); primary keys; indexes (Normal/Unique/Primary Key); table-level check constraints; **Options tab for database-specific table settings (engine, charset, tablespace) "without writing DDL manually"**; foreign keys incl. virtual foreign keys and composite keys; a **Logical Design** page exists; Bulk/Grid Editor.
- **Typical workflow documented**: "create or reverse-engineer the tables you need → define column data types and defaults → set the primary key and any unique indexes → add foreign keys between related tables → document the schema and sync the changes to the live database."
- **Synchronization (Synchronize page)**: online mode (changes executed against live DB immediately, logged in SQL History) vs offline mode (design freely, reconnect, review and selectively apply accumulated differences). Refresh schema from database pulls external changes (e.g., a colleague's migration) and prompts for action. **Diff review**: "The diff view lists added, removed, and modified objects — tables, columns, indexes, foreign keys. For each difference you can choose to update the model, push the change to the database, or skip it." **Sync Dialog generates the SQL migration statements** to bring the database in line with the model (or vice versa); statements are editable before executing; "Create or Upgrade Schema in Database" reviews generated DDL before executing.
- **Dialect conversion**: "DbSchema can migrate a schema from one database engine to another (e.g. MySQL to PostgreSQL) by **remapping data types automatically**" — via the model's **RDBMS** property; "Procedures, functions, and triggers with vendor-specific syntax must be rewritten manually." Changing target modifies the model's type mapping.
- Team collaboration via Git (`.dbs` in a repository; commits per schema change; branches; merges). **Interactive HTML5 documentation export** (diagrams, table descriptions, column tooltips) shareable with stakeholders without the tool. CLI / Groovy automation scripts for headless synchronization ("integrating schema deployments into CI/CD pipelines").
- Adjacent companion capabilities inside the same product: Relational Data Explorer (browse/edit rows following FK links), test-data generator (referential integrity maintained), data importer/loader, visual Query Builder, SQL Editor, MongoDB support, AI assistant, Community/Pro/Architect licensing.

### Layer notes

- All above layer A. This product directly attests: persistent file model, offline design, model↔database diff, migration-SQL generation, dialect remapping — the strongest operational evidence in the sample.

## Product C — SqlDBM

*(evidence layer A but Tier-2 only: product/marketing page; help center timed out)*

### Key observations

- Self-description: "Enterprise Data Modeling Platform"; "Data Modeling that Grows with your Team. From schema to semantic layer in one platform."
- **Modeling Platform tier**: "Conceptual, logical, and physical modeling; Reverse and forward engineering with version control; Real-time collaboration for the modeling team; Native dbt, Git, and API integrations."
- "Visual data modeling — Design schemas, define relationships, and structure data in a collaborative, visual environment **before implementation** across systems."
- **Model-to-database synchronization**: "Compare models to live environments and push changes with confidence, keeping design and production aligned."
- **Global Standards** (governance pole): enforce naming conventions, data types, and modeling patterns across every team and project; UI mock shows case standards (UPPER_CASE / lowercase), name mapping, primary keys, **virtual relationships**, glossary (synonym mapping), table templates (e.g., "TYPE 1 DIMENSION"), column templates, color flags; "Validate in project saver."
- **Target platforms** (cloud-data-platform era): Snowflake, Databricks, BigQuery, Azure Synapse, Amazon Redshift, Microsoft Fabric, plus SQL Server, Oracle, MySQL, PostgreSQL. Claims first online modeling tool to support Snowflake (2019); "natively modify, track, Reverse/Forward engineer Snowflake objects" including Views, Functions, Procedures.
- Understand layer: column-level lineage; dependency & impact analysis ("understand how changes affect downstream systems before deployment").
- Govern layer: data standards & modeling rules; **change review & approval workflows** ("manage schema changes with approvals, comments, and audit trails").
- Collaborate layer: Git & DataOps integration; shared model workspace "for engineers, analysts, and stakeholders."
- **AI Copilot** throughout: pre-prompts Design/Document/Analyze; project-level generate schema, modify relationships, suggest indexes; semantic modeling layer with governed metric definitions; MCP access for AI agents; bring-your-own model.
- UI mock shows an objects panel (Dim_Customer, Dim_Date, Fact_Customer_Order…), per-table metadata (data type, logical name, semantic type, synonyms), and a generated DDL preview (`CREATE TABLE "dbo"."ProductTable" ...`).

### Layer notes

- Marketing/product page only → positioning + capability-enumeration claims (layer A on the page, Tier 2 in nature). Operational mechanics (how sync and review actually behave step-by-step) **not verified**; keep qualified. Marketing metrics ("cut model design time by 60%") are vendor claims — do not repeat.

## Product D — Redgate Data Modeler (formerly Vertabelo)

*(evidence layer A: documentation home page)*

### Key observations

- Self-description: "an **online data modeling tool** that helps teams design, visualize, and manage databases collaboratively. It supports a wide range of database engines and offers a clean, intuitive interface for **creating entity–relationship diagrams, reverse-engineering existing databases, and generating SQL scripts**. As a cloud-based platform… share models, track changes, and work together in real time." Rebrand explicitly stated: "Redgate Data Modeler (formerly known as Vertabelo)".
- Feature-level evidence from the official modeling-tips index (each tip is an official article title, so the underlying capability is documented):
  - multicolumn primary keys; naming a primary key; multiple references between two tables; **reference to an alternate key**; quoting table names in generated SQL script; including comments in the SQL script; data types beyond the panel's list and "data type not supported" handling (**dialect-governed types**); moving/copying columns, copying tables between models; same table placed in a diagram twice / **shortcuts** from the navigation tree; **subject areas** to visually group tables and organize large models; displaying all references between two tables; **export selected tables as an image**; **model preview link and embedding the model in a website**; printout configuration; finding tables in diagrams; **"How to identify problems with my model"** (validation); **naming a version of the model** (model versioning); automatically downloading the SQL script.

### Layer notes

- Documentation home + tips titles = layer A for capability existence; per-feature mechanics not fetched. All claims kept at capability level.

## Product E — DrawSQL

*(evidence layer A: landing page)*

### Key observations

- Self-description: "The **database schema diagram tool** where teams design, review, and evolve together"; "Visual database design for engineering teams."
- **SQL import**: "Paste CREATE TABLE statements and get a diagram you can actually work with." Positioning: "Get your database schema out of migrations… Reason about changes in context — not in migration files, a stale screenshot, or someone's head."
- **DDL export**: "Get DDL for **MySQL, PostgreSQL, or SQL Server**. Or export as **Laravel migrations** and JSON." Dialect badges: MySQL, PostgreSQL, SQL Server, MariaDB.
- Team surfaces: real-time multiplayer on the live diagram; **discussion threads attached to tables** ("it stays there until someone resolves it"); embeds in Notion/Confluence; groups by domain, sticky notes, auto layout ("80 tables stays navigable").
- **Version history**: "Go back to earlier schema states when you need to compare approaches."
- **Templates**: "200+ real-world schemas to start from — SaaS, e-commerce, CRM, and more" (multi-tenant, CRM, e-commerce, SaaS billing tags).
- **AI on the schema**: Review (missing indexes — e.g., a missing index on an FK column flagged with "Apply Fix"; naming consistency — "Rename planName to plan_name… the rest of the diagram is already using snake_case"), Generate ("Add invoicing to the billing schema — with invoices linked to teams and subscriptions", applied as a diff: "+2 tables △1 table +3 relationships"), Diff ("see exactly what changes before applying").

### Layer notes

- Landing page = layer A for positioning and listed capabilities; editor mechanics beyond the mock not verified.

---

## Cross-product Comparison

| Dimension | dbdiagram.io | DbSchema | SqlDBM | Redgate Data Modeler | DrawSQL |
|---|---|---|---|---|---|
| Self-label | "draw database diagrams (ERDs) by typing DSL code" | "visual database design and management tool" | "Enterprise Data Modeling Platform" | "online data modeling tool" (ER diagrams, reverse-engineering, SQL generation) | "database schema diagram tool" |
| Central artifact | DBML text document (model) rendering an ERD | `.dbs` design-model file (schemas, diagrams, queries) | project model (conceptual/logical/physical) | model with named versions | editable schema diagram (with imported SQL provenance) |
| Schema constructs attested | tables, columns, types, pk/unique/not null/default/check, indexes (composite/expression/btree/hash), Ref FKs w/ referential actions, composite + cross-schema FKs, enums, TablePartial, Records | tables, columns w/ types/precision, NOT NULL, defaults, identity/auto-increment (dialect-varied), PK, indexes, check constraints, DB-specific table options, FKs incl. virtual/composite | tables/objects, relationships, per-object metadata (logical name, semantic type) | multicolumn PKs, alternate-key references, multiple references between tables, dialect-governed data types | tables w/ typed columns, PK glyph, FK relationships, enums |
| Diagram presentation | ERD rendered from code; diagram views, detail levels, groups, notes | interactive canvas; inline editing on diagram; multiple diagrams per model | visual environment; diagram display of platform objects incl. Snowflake views/functions/procedures | ER diagrams; subject areas; shortcuts (same table twice); printouts | the diagram IS the primary surface; groups/notes/auto-layout |
| Dialect handling | `database_type` in model; SQL export per dialect (PG/MySQL/MSSQL/Oracle); import matrix incl. Snowflake | RDBMS property; automatic data-type remapping on conversion; engine/charset/tablespace options; dialect-varied auto-increment | per-platform projects (Snowflake, Databricks, BigQuery, Synapse, Redshift…); reverse/forward engineering per platform | "wide range of database engines"; unsupported-data-type handling; SQL quoting/comments per dialect | DDL export for MySQL/PostgreSQL/SQL Server; MariaDB badges |
| Forward realization | DBML→SQL DDL export (+CLI/JS programmatic) | generated migration SQL + Create/Upgrade schema DDL, editable before execute | forward engineering (+ model-to-DB sync push) | generates SQL scripts; auto-download script | DDL + Laravel migrations + JSON export |
| Reverse input | SQL→DBML import; live-DB connectors | connect & reverse-engineer; import SQL/CSV/SQLite | reverse engineering (per platform; direct connect or file upload per partner text) | reverse-engineering existing databases | paste CREATE TABLE import |
| Model↔DB diff | (import/connect only attested) | refresh + diff view (added/removed/modified objects), per-difference update-model/push/skip | "compare models to live environments and push changes" | (not attested on fetched page) | (AI diff on model changes) |
| Validation | (docs list AI assistant; validation not attested) | Model Validation page; FAQ | "Validate in project saver" | "identify problems with my model" | AI review (missing indexes, naming) |
| Versioning | version history | Git-based (commits/branches/merges) | version control (+ change review & approval workflows) | named model versions | version history w/ earlier states |
| Sharing / docs | private/password links, embedding, DBML-in-link, workspaces | interactive HTML5 docs, Git sharing | shared workspace; Confluence/Jira; MCP/semantic layer for consumers | image export, preview link, embed, printouts | embeds (Notion/Confluence), templates gallery |
| Collaboration | real-time collaboration, SSO | Git | real-time for modeling team; approvals; audit trails | real-time, share models | real-time multiplayer; per-table discussion threads |
| Programmatic | CLI, VS Code extension, @dbml/core JS | CLI, Groovy automation, Java API | API, Git, dbt | (not attested on fetched page) | (not attested on fetched page) |
| AI | AI assistant page | AI assistant page | Copilot (generate/modify/suggest), semantic layer, MCP | (not on fetched page) | review/generate/diff on schema |
| Adjacent data tooling | Records (sample data) | data generator/importer/loader, relational data explorer, query builder, SQL editor | column-level lineage, impact analysis, semantic modeling | — | — |
| Delivery | web (+ local via CLI/VS Code) | desktop (+CLI) | web SaaS | web SaaS | web SaaS |
| Tier | free + professional | free CE + Pro/Architect | enterprise SaaS | commercial SaaS | free + paid SaaS |

### Stable cross-product reading (layer B where applicable)

1. **Every sampled product holds a persistent, editable schema model as the object of work** (DBML document, `.dbs` file, project, model, editable diagram) — distinct from any live database.
2. **Every sampled product's model is database-semantic and dialect-aware**: constructs map to DBMS schema constructs; the target dialect is a property of the model (dbdiagram `database_type`, DbSchema RDBMS property, SqlDBM per-platform projects, Redgate engine-specific types/quoting, DrawSQL per-dialect DDL export).
3. **Every sampled product presents the model as an entity-relationship diagram** — hand-edited canvas (DbSchema, SqlDBM, Redgate, DrawSQL) or code-rendered (dbdiagram).
4. **Every sampled product closes the loop into a concrete database schema**: generated DDL / SQL scripts / migration statements / forward engineering (all five).
5. **Every sampled product supports reverse input** — SQL script import and/or live-database reverse engineering (all five). This is an input mode, not the defining loop: DbSchema explicitly supports full offline design.
6. Model **validation/problem identification** appears in four of five (DbSchema, SqlDBM, Redgate, DrawSQL-AI).
7. **Model versioning/history** appears in all five (named versions, Git, version history, version control).
8. **Diagram-organization machinery for large models** (multiple diagrams, subject areas, groups, notes, detail levels) appears in four of five.
9. **Sharing/publication** (image/HTML/print export, preview links, embeds) appears in four of five.
10. Team collaboration (real-time and/or Git/approvals) is current-market common across the sample; depth varies from Git-file sharing (DbSchema) to governed approval workflows (SqlDBM).
11. AI assistance appears in four of five current products (current-market common, not definitional).
12. Programmatic access (CLI/API/JS module) appears in three of five.

---

## Canonical Abstraction

### L0 — Defining Invariant

```text
Persistent editable schema model (design object held independently of any live database)
└── Database-semantic constructs with a concrete DBMS/dialect target
    (tables with typed columns, keys, constraints, relationships — mapped to real schema language)
    └── ER-diagram presentation of the model
        (hand-edited canvas or rendered from the model's code)
        └── Forward realization: the model generates concrete schema-creation artifacts
            (DDL scripts / migration SQL / direct schema application)
```

Four conjuncts; each is load-bearing:

- Remove the **persistent editable model** → one-shot DDL generators or diagram snapshots; no design work accumulates. Not a design tool.
- Remove **database-semantic, dialect-targeted constructs** → generic boxes-and-lines drawing, i.e. a Diagramming Application. (The dialect target is what makes the model *realizable* rather than illustrative.)
- Remove the **ER-diagram presentation** → a schema DSL compiler or a form-based schema editor, i.e. SQL-editor/schema-as-code territory (SQL Client / Database IDE family), not the recognizable design-tool surface. Note the presentation invariant is compatible with code-first editing: dbdiagram's diagram is rendered from DBML, not hand-arranged.
- Remove **forward realization** → an ER-documentation/viewer tool (render or import schemas for reading, never produce the schema). Design implies the model can *become* a database schema.

Historical check: the ERwin / PowerDesigner / Oracle CASE generation (1980s–90s) was model-first, diagram-presented, DDL-generating — all four conjuncts hold without any of the modern specifics (cloud, collaboration, subscriptions, AI). Desktop-file tools (DbSchema) and code-first tools (dbdiagram) satisfy the same conjuncts today; the conjuncts presume no delivery form, era, collaboration model, or DBMS scope. Check passed.

### L1 — Common Mature Structure

- **Reverse engineering as an input mode** — import SQL DDL scripts and/or connect to a live database and extract its schema into the model (all five sampled products). Complements but does not replace blank-canvas design (DbSchema documents offline design explicitly).
- **Model↔database synchronization** — compare model against a live database, review per-object differences, generate migration SQL, push or pull selectively (DbSchema in operational depth; SqlDBM as capability claim).
- **Model validation / problem identification** — integrity problems, unsupported data types for the dialect, missing indexes, naming inconsistencies (four of five; DrawSQL's is AI-delivered).
- **Model versioning** — named versions, version history, or Git-based commit/branch/merge (all five).
- **Large-model organization** — multiple diagrams per model, subject areas, groups, shortcuts/aliases, notes, detail-level toggles (four of five).
- **Sharing and publication** — image/print/HTML export, preview links, embedding in wikis/docs, private/password-protected links (four of five).
- **Team collaboration** — real-time co-editing, discussion threads on objects, workspaces, or Git-file workflows (current-market common; depth is a variant axis).
- **Generated-SQL review** — DDL/migration output is presented for human review (and commonly editable) before execution (DbSchema directly; DrawSQL's AI diff variant).
- **Column-level documentation** — notes/comments on tables and columns carried into the model and often into generated SQL (dbdiagram notes, DbSchema column comments, Redgate comments-in-SQL tip).
- **AI assistance** — generate tables/relationships from descriptions, review designs, explain or propose changes against the model (current-market common).
- **Programmatic access** — CLI / API / language modules for import-export and automation (three of five).

### L2 — Variant / Optional Structure

- **Editing philosophy**: visual canvas-first (DbSchema, SqlDBM, Redgate, DrawSQL) vs code-first (DBML) with rendered diagram (dbdiagram) — a philosophy axis, not a Type boundary.
- **Scope**: universal multi-DBMS (DbSchema 70+; dbdiagram multi-dialect matrix) vs ecosystem/platform-bound (SqlDBM's cloud-data-platform pole; historically MySQL Workbench for the MySQL ecosystem).
- **Delivery**: desktop with a local model file (DbSchema `.dbs`, Git-collaborated) vs cloud SaaS with accounts and real-time sharing (dbdiagram, SqlDBM, Redgate, DrawSQL).
- **Abstraction layers**: physical-only vs conceptual/logical/physical layering (SqlDBM explicitly; DbSchema has a Logical Design surface) — enterprise-modeling-pole feature.
- **Governance depth**: naming standards/case conventions, glossaries, table/column templates, change review & approval workflows, audit trails (SqlDBM pole; lighter tools have none).
- **Target class**: OLTP engines vs cloud warehouses/lakehouses (Snowflake/Databricks/BigQuery objects incl. views, functions, procedures in SqlDBM) — a segment variant.
- **Team tier**: individual free tools vs team/enterprise subscriptions (all poles present in sample).
- **Migration vs full DDL**: generated output may be full DDL, ALTER/migration statements, or framework migrations (Laravel) — depth and form vary by product.
- **Adjacent data tooling** inside the same product: test-data generators, relational data explorers, visual query builders, SQL editors, column-level lineage (DbSchema, SqlDBM poles) — companion capabilities, not definitional.
- **Semantic-layer / AI-consumer extensions**: governed metric definitions, MCP access for AI agents (SqlDBM pole) — an emerging extension axis.

### L3 — Vendor-specific (research notes only)

- dbdiagram: DBML specifics (Ref operators with optionality markers, TablePartial conflict-resolution rules, Records type-checking, DBML-in-link accountless sharing); Holistics dbx family (dbdocs, RunSQL); VS Code extension; support-matrix asymmetries (Snowflake import-only, BigQuery connector-only).
- DbSchema: `.dbs` single-file model storing queries and editors; virtual foreign keys (display-only references); RDBMS-property dialect conversion with manual rewrite of vendor-specific routines; Groovy automation scripts; MongoDB modeling; Community/Pro/Architect ladder.
- SqlDBM: Global Standards object (case standards, name mapping, glossary, flags, templates, validate-on-save); semantic modeling layer with governed metrics; MCP access; Snowflake premier-partner claims; strategic-advisor program; marketing metrics (excluded from canonical claims).
- Redgate Data Modeler: Vertabelo rebrand; subject areas; shortcuts (same table twice); alternate-key references; printout configuration; auto-download SQL script.
- DrawSQL: Laravel-migrations export; 200+-schema template marketplace; per-table discussion threads; AI "Apply Fix" flow.

## Rejected Findings

- "A schema design tool is visual-canvas-driven by definition" — **rejected**: dbdiagram edits the model as DBML code and renders the diagram. The invariant is ER-diagram *presentation* of the model, not hand-arranged canvas editing.
- "Reverse engineering from a live database is definitional" — **rejected**: it is an input mode (albeit universal in the sample); DbSchema explicitly supports fully offline design, and SQL-script import covers the same need without a connection.
- "The tool operates/queries live databases" — **rejected as definitional**: some sampled tools carry companion query/data surfaces, but the object of record is the model; operating live instances is Database IDE / SQL Client / Console territory.
- "Conceptual and logical modeling layers are definitional" — **rejected**: physical, dialect-targeted modeling is the core; conceptual/logical layers appear in the enterprise pole only (SqlDBM explicitly; DbSchema has a logical-design surface; lighter tools have none).
- "Cloud collaboration defines the modern form" — **rejected**: the desktop file-model pole (DbSchema, Git-collaborated) satisfies the Type fully.
- "AI assistance is part of the Type" — **rejected**: current-market common (4/5), not defining.
- "Migration/ALTER generation is definitional" — **kept qualified**: full DDL generation is universal in the sample; migration-SQL generation is directly documented in DbSchema and (as framework migrations) DrawSQL, asserted as common, not definitional.
- "An ER-diagram documentation/viewer tool is a schema design tool" — **rejected**: without forward realization there is no design→schema closure (docs rendering exists as a separate product even within the dbdiagram vendor family: dbdocs).

## Boundary Findings

| Neighbor Type | Shared ground | Discriminator (what flips the Type) |
|---|---|---|
| Database IDE (§12, processed) | schemas, diagrams, DDL, possibly live connections | The IDE's object world is a **live database catalog** and its loop is authoring→execution→result inspection. The design tool's object world is a **model** that precedes or abstracts from any live database; its loop is design→validate→generate→(sync). A design tool's connection features are model-input (reverse engineering) and model-output (sync), never the query-and-inspect loop. Ratifies the boundary recorded in the Database IDE pass; the IDE's "deep visual data modeling" variant leans here. |
| Diagramming Application (processed) | ER-style boxes and lines | A diagramming application draws the notation without enforcing or deriving schema semantics — no typed-column identity, no key/constraint machinery, no dialect target, no DDL. An ERD drawn there is a picture of a schema, not a managed schema. (Consistent with the processed Diagramming Application pass, which named exactly this seam.) |
| SQL Client (§12) / Database Management Console (§13, processed) / SQL Workbench (§13) | may connect to the same databases, may run SQL | Those operate/query **live instances**; they hold no persistent schema design model and produce no schema artifacts. Strip the model + generation from a design tool → at most a schema-aware editor/client. |
| Database Sandbox Platform (§12, processed) | both give teams a place to try schemas | The sandbox **provisions working database environments** for hands-on experimentation (real instances, bounded/expenderable); the design tool **authors the model** before/instead of any environment. Consistent with the processed sandbox pass, which framed this leaf as "authors schema models before any database exists." |
| API Design Platform (§12, processed) | both are design-first modeling tools for engineers | The API platform's artifact of record is the **service interface** (paths, operations, request/response schemas); no DBMS-schema semantics. Clean boundary as recorded in its pass. |
| Software Architecture Modeling / System Design Application (§12) | diagrams with semantics, often including data stores | Architecture models capture systems/components/interactions (C4-style); they do not manage dialect-targeted physical schemas with type mappings and DDL realization. |
| Data Catalog / Metadata Management (§13, processed) | schema structure, diagrams, metadata | A catalog **describes existing** data assets owned by other systems (discovery lens); a design tool **authors planned** schemas as realizing artifacts. Reverse engineering creates a documented overlap, not an identity. |
| Low-code / No-code Application Builder (§12) | both model data structures | The builder's data model serves app-screen composition inside its own runtime; it is not a standalone dialect-targeted schema design artifact for an external DBMS. |
| Database Dev/Test Environment Manager (§12) | schemas, databases | That Type governs fleets of **environments** (provisioning, refresh, masking); the design tool authors one schema model. |
| Database Documentation generators (dbdocs-class, outside directory) | schemas, diagrams | Documentation tools render existing models/schemas for reading; no editing model, no realization loop. (Note: such tools may be a directory-adjacent gap; not a DIRECTORY.md leaf today.) |

## Boundary Issues (for STATUS.md)

None requiring taxonomy change. The boundary flagged by the Database IDE pass is **discharged from this side**: sampled design tools consistently place the model — not a live catalog — at the center (offline design attested verbatim in one product; dialect target carried inside the model in four of five). The **Diagramming Application** seam is also clean given the semantics+generation test. One observation recorded without action: ER-documentation tools (docs-as-code renderers of DBML-class models) sit just outside this Type and have no dedicated DIRECTORY.md leaf; a future taxonomy pass may want to consider whether they belong somewhere (they are currently absorbed by no leaf). No rewrite attempted.

## Uncertainties

- SqlDBM's operational depth (project structure, sync UX, approval mechanics) rests on its product page; the help center timed out. All SqlDBM-specific mechanics are kept at capability level.
- dbdiagram's canvas-editor mechanics were not verifiable (JS-rendered pages empty); the DBML language and SQL mapping are verified. No canvas-behavior claims are made.
- MySQL Workbench remains unreachable (403), so the classic vendor-ecosystem modeling pole is evidenced only indirectly; no claim in this research depends on it.
- Per-product notation conventions (crow's foot vs IDEF1X etc.) were not directly attested; cardinality display is attested only at the level of "relationships with cardinality semantics" (DBML operators, key icons, FK lines).
- Whether products other than DbSchema generate ALTER/migration scripts (vs full DDL) was not verified product-by-product; treated as product-evidenced common capability.
- Redgate Data Modeler per-feature mechanics were verified only at tips-title level (capability existence, not behavior detail).

## Final Synthesis

A Database Schema Design Tool is a **modeling application whose object of record is a schema model**: a persistent, editable, database-semantic definition of a database structure — tables with typed columns, keys and constraints, and relationships — carrying a concrete DBMS/dialect target inside the model, presented as an entity-relationship diagram (hand-edited or rendered from the model's code), and closed by **forward realization**: generation of the schema-creation artifacts (DDL scripts, migration SQL, or direct schema application) that turn the design into a real database schema. Around that core, mature products add reverse engineering (from SQL scripts or live databases), model↔database synchronization with reviewable diffs, validation, versioning, large-model organization, publication/sharing, collaboration, and — currently — AI assistance. Editing philosophy (visual vs code-first), scope (universal vs platform-bound), delivery (desktop file vs cloud), abstraction depth (physical-only vs conceptual/logical/physical), and governance depth are variant axes. The definition is independent of era, delivery form, collaboration model, and DBMS scope, and it cleanly separates the Type from Database IDEs (live-catalog execution loop), diagramming tools (no schema semantics), SQL clients/consoles (no design model), and sandbox/environment platforms (provisioned environments, not authored models).
