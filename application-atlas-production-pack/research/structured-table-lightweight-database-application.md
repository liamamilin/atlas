# Research Notes — Structured Table / Lightweight Database Application

## Research Goal

Understand the Structured Table / Lightweight Database Application as an Application Type: the data model users build on (tables, typed fields, records), the query and view machinery that makes it database-like, how far the "lightweight" posture goes (what the user never has to do that a database engineer would), and where the boundary sits against the processed siblings Spreadsheet Application and Collaborative Spreadsheet, the processed No-code Application Builder and Low-code Application Platform, Online Form Builder, domain systems of record (CRM-class), database management tools, and work-management grid products.

This leaf completes §03.03 Spreadsheets & Tables. Two sibling passes left forward obligations for this pass:

- `research/spreadsheet-application.md` (processed 2026-09-09): "the seam is formula-recalculation-as-computation-model over a semantically empty addressed grid vs typed-field/record semantics with app-imposed meaning and relational record links — that pass should ratify."
- `research/no-code-application-builder.md` and `research/low-code-application-platform.md` (both processed): the structured-table seam was "reasoned not evidenced (Airtable-class unexamined)" — this pass examines Airtable-class products directly and must discharge that flag with evidence.
- `research/online-form-builder.md` pre-hung a watch item: "table/data-model center vs respondent-intake center."

## Initial Boundary

- Sits under 03.03 as the third leaf: the record/field pole of the family (vs the addressed-cell grid of the two spreadsheet leaves).
- Working hypothesis: the type = user-defined tables of records with typed fields, queried and re-presented through multiple views, operated entirely by direct manipulation (no query language, no server administration) — the "database for everyone" posture.
- Nearest neighbors: Spreadsheet Application (semantically empty addressed grid + cell formulas + recalculation), Collaborative Spreadsheet (same grammar + shared-live layer), No-code Application Builder (composed app as unit of record vs data table as unit of record), Low-code Application Platform (full application factory), Online Form Builder (respondent-intake instrument vs owner-side data model), CRM / domain systems (predefined schema vs user-defined schema), Database IDE / SQL clients (query-language operation on real servers), Work Management (rows-as-tasks drift), Notion-class workspaces (databases embedded in a page/workspace product).

## Research Questions

1. What is the container model (base / database / document / workspace) and the table model inside it?
2. What exactly is a field — is typing definitional, and how strictly is it enforced?
3. What is a record — how is it addressed, opened, acted on as a unit?
4. How do users query — sort/filter/find/group; where does query configuration live?
5. What is the view model — which view types, what does a view configure, is multi-view definitional?
6. How do relations work (linked records, lookups, rollups) — and are they definitional or common?
7. Where do computed values live (formula fields/columns) and how do their semantics differ from spreadsheet formulas?
8. What does "lightweight" exclude — SQL, server administration, deployment, programming?
9. What standard machinery surrounds the core (collaboration, permissions, forms, import/export, API, automations, interfaces/dashboards, AI)?
10. Where are the boundaries vs spreadsheets, no-code/low-code builders, form builders, domain systems, database tools, work management, and workspace products?

## Representative Products

| Product | Why selected | Evidence level reached |
|---|---|---|
| Airtable | category-defining commercial product; "app-building platform" drift pole; enterprise tier | Tier-1 deep (glossary + field-types overview + linked-record hub + homepage positioning) |
| Grist | spreadsheet-formula hybrid pole ("relational spreadsheet"); open-source + self-host; regulated-industry tier | Tier-1 deep (positioning + columns & types + formulas articles) |
| Baserow | open-source no-code database pole; self-hostable; developer-extensible | Tier-1 (docs index self-definition + technical introduction + database-plugin concepts) |
| NocoDB | database-first open-source pole ("no-code interface for databases"); connects to real databases | Tier-1 (product overview + features + mission) |
| Notion (boundary anchor) | workspace-embedded databases; record-as-page variant | Tier-1 (Intro to databases help article) |
| FileMaker (boundary anchor) | the older forms-over-data generation still alive; low-code straddle pole | Tier-2 (product page positioning incl. "more than 40 years of history") |
| Smartsheet (boundary anchor, via sibling passes) | grid-as-work-management drift pole | Tier-1 evidence already recorded in `research/collaborative-spreadsheet.md`; reused for boundary only |

Selection covers: market representation (Airtable), different product philosophies (Grist keeps spreadsheet formulas; NocoDB starts from real databases; Baserow is plugin-extensible OSS), different customer tiers (enterprise SaaS → regulated/self-host → OSS self-host), and the historical bridge (FileMaker).

## Sources

- Airtable — homepage positioning: https://www.airtable.com/ (fetched 2026-09-09)
- Airtable Help Center root (collection taxonomy): https://support.airtable.com/ (fetched 2026-09-09)
- Airtable — Glossary of Airtable terminology: https://support.airtable.com/articles/6687333754-glossary-of-airtable-terminology (fetched 2026-09-09)
- Airtable — Supported field types overview: https://support.airtable.com/docs/field-types-overview (fetched 2026-09-09)
- Airtable — Linked Record Field (article hub): https://support.airtable.com/docs/linked-record-field (fetched 2026-09-09)
- Grist — homepage positioning: https://www.getgrist.com/ (fetched 2026-09-09)
- Grist Help Center root (doc taxonomy): https://support.getgrist.com/ (fetched 2026-09-09)
- Grist — Columns and data types: https://support.getgrist.com/col-types/ (fetched 2026-09-09)
- Grist — Intro to formulas: https://support.getgrist.com/formulas/ (fetched 2026-09-09)
- Baserow — Docs index (self-definition): https://baserow.io/docs/index (fetched 2026-09-09)
- Baserow — Technical Introduction (workspaces/applications): https://baserow.io/docs/technical%2Fintroduction (fetched 2026-09-09)
- Baserow — Database plugin (tables/fields/views/rows): https://baserow.io/docs/technical%2Fdatabase-plugin (fetched 2026-09-09)
- NocoDB — Documentation product overview: https://nocodb.com/docs/ (fetched 2026-09-09)
- Notion — Intro to databases: https://www.notion.com/help/intro-to-databases (fetched 2026-09-09)
- Claris FileMaker — product page (positioning + FAQ): https://www.claris.com/filemaker/ (fetched 2026-09-09)
- Sibling-pass sources reused for boundaries only: Smartsheet help center (3 articles), Airtable homepage (see `research/collaborative-spreadsheet.md`, `research/spreadsheet-application.md`)

### Source-access limitations

- Historical flat-file / end-user database products (AppleWorks/ClarisWorks database module, dBase-class products, Lotus Approach, Borland Paradox, Microsoft Access) have no reachable official documentation for their historical eras; the era check is conceptual, anchored by two fetched artifacts: FileMaker's own "more than 40 years of history" claim and a Grist case-study quote ("sits somewhere between Excel and Access"; "Sharing an Access database is near impossible, but Grist makes sharing a relational database simple"). No precise historical capability claims are asserted from memory.
- Airtable's "Getting started" collection article bodies beyond the glossary were not fetched; Airtable operational claims rest on the glossary + field-types overview + linked-record hub.
- Grist's reference-columns (col-refs), page-widgets, and search-sort-filter articles were reached at title level only (via help-center taxonomy); Grist claims rest on the fetched col-types and formulas articles plus positioning.
- NocoDB's deeper per-feature docs were not fetched; NocoDB claims rest on the product overview page (which is itself a Tier-1 features/mission statement).
- Knack, Zoho Tables, SeaTable, Teable, Smartsheet's data layer, and the spreadsheet products' own "Tables" features were not fetched — market anchors / uncertainty notes only.
- No numeric limits (record caps, field counts, plan gates) are asserted in the final document; figures observed in fetched pages (e.g., Airtable HyperDB "100M records", Notion's 1,000-item sort note, Baserow's 72-hour trash default) are kept here as vendor specifics.

## Product A — Airtable

### Key observations (evidence A — glossary)

- Positioning (homepage): "Airtable is the system of record for your workflows, data, and agents"; "next-gen app-building platform"; Databases feature = "Use relational databases to connect data from apps, workflows, and tools"; onboarding: "Describe the app you need in plain words, or drop in a spreadsheet you already have"; "All your teams and their agents build on the same records. Change one thing, everyone sees it."
- **Base**: "a collection of data in Airtable, designed to contain all of the information related to a project or workflow. Bases can have multiple tables, each containing data. Within each table, there are records with data for each record stored in fields."
- **App**: "The sum of parts including the base, automations, any interfaces, extensions, and more. **The base is the underlying relational database structure of an app you build.**" — the data table is the substrate; interfaces/automations are layers on it.
- **Table**: "holds information about one type of item — for example, products, projects, tasks, campaigns. Each base needs at least one table. Individual tables appear as their own tabs in a base."
- **Record**: "an individual item in a table. Records are the basic unit of data that are pulled into various views and interfaces. Each record can include data in multiple fields."
- **Field**: "a vertical column in a table. It contains the details or data for each record in the table."
- **Field type**: "specifies the kind or format of data stored in a given field — for example, long text, date, multiple select, or attachment. Users can customize most field types within their base."
- **Primary field**: "always the first column, or field, in any table. It represents a description of each record in the table and cannot be deleted, moved, or hidden. The primary field is used as a brief description of a record in other parts of the UI." — record identity surfaced by name.
- **Linked record**: "connects to another table or record. This connection is always within the same base. Linked records allow users to create relationships or dependencies between records and to pull in existing data without duplicating it."
- **View**: "a particular way to look at and organize the underlying data in a table. The default type of view is a grid, but other types include form, calendar, gallery, and Kanban. A given table can have multiple views (and multiple types of views)."
- **Grid view**: "display data as a series of rows and columns, with each record a row, and each field a column. Grid is the default view for a new base."
- **Condition** (filtering): "A rule used to filter records; records must meet a condition to be visible in a given view or interface. A condition contains three parts: A field, An operator (ex. 'contains,' 'has any of,' 'is greater than'), A value."
- **Formula**: "A function or numerical, text, or logical operation that allows users to output numbers, dates, strings, and more in a record based on static or dynamic information from other fields in that same record. **Formulas must be added in a formula field.**" — per-record computation bound to a field, not cell-addressed.
- **Expression**: "a combination of values, fields, and/or formulas that evaluates to a single value."
- **Form view**: "allows users to create a form to collect data that is then saved to an Airtable base."
- **Automations**: "always include a trigger and one or more actions."
- **Interface**: "a curated representation of base data created using Interface Designer."
- **Permissions ladder**: Owner / Creator / Editor / Commenter / Read-only; base-level and workspace-level grants; interface-only collaborators.
- **Record-level machinery**: comments on records, record revision history, trash (deleted items restorable for a vendor-defined window), base snapshots (restore copies into a new base).
- **Sync**: "sync records from a source base to one or more destination bases, creating a single source of truth"; two-way sync in limited beta.

### Key observations (evidence A — field types overview)

27 field types documented, including: single line text, long text (rich text), attachment, autonumber, barcode, button, checkbox, count, created time, created by, currency, date & time, duration, email, **formula** ("compute a value in each record based on other cells in that same record"), last modified by/time, **linked record** ("represent the relationships between related records by creating links between them… for example, a table of contacts and a table of companies"), **lookup** ("look up a specific field in a linked record"), multiple select, number, percent, phone, rating, **rollup** ("performs calculations or formulas on an aggregate of inputs from another field based upon a linked record relationship"), single select, URL, user (collaborator).

Interpretation: Airtable documents the full canonical chain — base (container) → tables (one per item type) → records (the unit) → typed fields (the schema) → views (grid default + form/calendar/gallery/kanban) with per-view filter conditions → linked records with lookup/rollup → formula fields computing per record → automations/interfaces as layers on the base. The "App" definition explicitly names the base as "the underlying relational database structure."

## Product B — Grist

### Key observations (evidence A — positioning)

- "Spreadsheet Software to End Data Chaos"; "Turn the spreadsheets running your business into secure applications"; "Full-featured relational spreadsheet software"; "the modern spreadsheet-database software"; open-source "spreadsheet-database tool"; "Can be self-hosted… Uses SQLite format, great for portability and backups."
- Feature set: "Formulas with Excel functions and Python power"; access rules ("Control who sees what, down to each row and column"); forms & surveys; flexible layout ("Drag-and-drop widgets… Link data to quickly pull up details and related records. Turn rows into data cards"); visualizations ("Summarize data into charts or pivot tables").
- Customer quote (case study): "It sits somewhere between Excel and Access—powerful, relational, and flexible enough for prototyping real data-driven applications." Another: "Sharing an Access database is near impossible, but Grist makes sharing a relational database simple." — the vendor's own market frames Grist against the end-user database lineage.

### Key observations (evidence A — columns & types)

- "Grist columns have types, similar to other spreadsheets or databases. The type of a column controls its appearance and the help Grist will offer you when editing cells."
- New columns start as `Any` type; Grist auto-narrows on first entry (number → Numeric; non-number → Text). Users set types manually: **Text, Numeric, Integer, Toggle, Date, DateTime, Choice, Choice List, Reference, Reference List, Attachment**.
- **Soft typing**: "Regardless of the column type, you can enter any value in cells. If a value entered is incompatible with the defined type, the cell will be highlighted with an error (and columns referencing the invalid value will also display an error)." — typing shapes behavior and surfaces violations; it does not hard-block entry.
- **Reference columns**: "This sets up a cross-reference to another table. You can specify the table to reference, and a column within that table to show." Reference List stores multiple references per cell.
- **Lookups**: the Add Column menu offers "Lookups — allows you to add data columns from related tables. You can use reference columns to relate data in different tables."
- Choice columns carry user-defined option sets (with colors, reordering, rename-propagates); attachment columns hold files/images per cell.
- Every new table starts with columns named A, B, C — renamed into fields; column IDs are Python-friendly identifiers used in formulas.

### Key observations (evidence A — formulas)

- "Grist has a powerful data engine to calculate the cells of your tables using formulas… If you've used spreadsheets before, or database expressions, you'll be on familiar territory."
- **Column-bound formulas**: "In Grist, a single formula applies to a whole column. You don't have to worry about filling it in for all rows, and can refer to values in the same row without fuss." `$Column` syntax references fields of the same record; "Press Enter, and your formula is applied to all cells in the column."
- **Column behaviors**: Data column (manual values, optionally trigger formulas) / Formula column ("always reflects the result of formula calculation, and is kept up-to-date by Grist") / Empty column. "Convert column to data" freezes computed values.
- **Python + Excel-like functions**: formulas are Python; "we've also added a suite of Excel-like functions, with all-uppercase names."
- **Cross-table access**: every table is available by name in formulas; `Materials.lookupOne(Quantity=52).Product`, `lookupRecords` with `order_by`; summary tables ("For common use cases, Summary tables may be exactly what you need") as aggregation widgets; aggregate formulas like `SUM(Materials.all.Price)` live in separate summary widgets, not in data rows.
- **Trigger formulas**: data columns that recompute on record creation/update or on entry into the field (timestamps, authorship, data cleanup, defaults) — formula power attached to data fields.
- Recalculation: "When we provide a formula for a column we tell Grist to update its value on every change in a document."

Interpretation: Grist is the hybrid pole — it keeps the spreadsheet's formula-and-recalculation engine but re-anchors it on the structured-table model: typed columns, records addressed as records (`rec` is "the current row"), references to other tables, lookups, summary widgets. The formula is column-bound and record-scoped, not cell-addressed. This product proves the seam vs spreadsheets is the data model, not the presence of formulas.

## Product C — Baserow

### Key observations (evidence A — docs index + technical introduction + database plugin)

- Self-definition (docs index): "Baserow is an open-source online database tool. Users can use this no-code platform to create a database without any technical experience. It lowers the barriers to app creation so that anyone who can work with a spreadsheet can also create a database. **The interface looks a lot like a spreadsheet.**"
- Architecture: backend (Python/Django, REST API, PostgreSQL persistence) + web frontend; the database functionality is itself a **plugin** ("the plugin that allows creating a database with a spreadsheet-like interface") inside an application abstraction — plugins can add field types, view types, view filters, whole application types.
- **Workspaces** contain **applications**; the database application is the default.
- **Tables**: "Each database application can have multiple tables… It contains rows and columns, but in Baserow the columns are called fields. Every table has its own schema representation in the PostgreSQL database." (User tables are materialized as real database tables with generated models — the database-first implementation.)
- **Fields**: "A field is actually a column definition of a table. It accepts only a certain data type for its cell values." Default field types: text, long text, number, boolean, date (EU/ISO/US formats, optional time) — extensible via plugins.
- **Views**: "Views define how the table data is displayed to the user. By default the `grid` view type is included, which displays the data in a spreadsheet-like interface. Multiple views can be added to each table and each view has its own settings" (per-view column widths etc.). View types (calendar, kanban, etc.) are pluggable; view filters are a pluggable concept.
- **Rows**: "Rows are the table data. The values that are accepted depend on the fields of the table."
- Live collaboration inside workspaces ("Live collaboration allows users to immediately see changes made by others without having to refresh the page"); REST API + WebSocket API; trash with a vendor-default retention window.

Interpretation: Baserow independently documents the same chain — database application → tables → typed fields ("column definition… accepts only a certain data type") → rows → multiple per-table views with own settings, grid default, spreadsheet-like interface — with an explicit no-code posture ("create a database without any technical experience").

## Product D — NocoDB

### Key observations (evidence A — product overview)

- Self-definition: "NocoDB is a no-code database platform that allows teams to collaborate and build processes with ease of a familiar and intuitive spreadsheet interface. This allows even non-developers or business users to become software creators."
- **Features** (structured as the product's own taxonomy):
  - Rich Spreadsheet Interface: "Basic Operations: Create, Read, Update and Delete on Tables, Fields, and Records"; "Fields Operations: Sort, Filter, Group By, Search, Hide / Reorder Fields"; "Rich Field Types: Text, Number, Date/Time, Select, Attachment, Formula, Links, Lookup, Rollup and more"; "Multiple View Types: Grid (default), Form, Gallery, Kanban, Calendar, Timeline, Gantt, List and Map"; "View Permissions: Collaborative Views, Locked Views, and Personal Views"; "Access Control with Roles: Fine-grained access control at Workspace, Base, Table, Field, and Record levels."
  - Automation & Scripting: workflows (triggers/actions/conditions/loops), JavaScript scripts, webhooks on record create/update/delete.
  - Dashboards & Extensions; AI (NocoAI assisted creation of "bases, tables, fields, views, filters, formulas, and select options"); NocoDocs; NocoSync; integrations connecting external data sources (PostgreSQL, MySQL, SQL Server, and more).
  - Programmatic access: REST APIs, MCP server.
- Mission: "to provide the most powerful no-code interface for databases" — the database-first pole: databases are the substrate; the spreadsheet interface is the access layer.

Interpretation: NocoDB independently confirms the canonical chain (tables/fields/records CRUD; typed fields incl. Links/Lookup/Rollup/Formula; grid-default multi-view; per-view sort/filter/group; role-based access down to record level) and adds the database-connectivity variant (operating external SQL databases through the same interface).

## Product E — Notion (boundary anchor)

### Key observations (evidence A — Intro to databases)

- "Databases in Notion are collections of pages." Three uniqueness claims: "Every item is its own page" (the record opens as a full Notion page with free-form content beneath the properties); "You can customize properties: Add properties to contextualize, label, and augment any database item with things like dates, status, and links"; "You can visualize your data in different ways: Your data isn't limited to a table. Organize your database as a list, calendar, chart, and more."
- Views with filters/sorts/grouping; full-page vs inline databases; linked views / data sources ("build an all-in-one CRM database where information on contacts, companies, and deals are managed all in the same database, while also being treated as separate sources of data").
- **Data-vs-structure permission split**: the "Can edit content" permission level "allows users to create, edit, and delete pages within the database [and] edit property values" but NOT "add, edit, or remove database properties or views… change filters or sorts… lock or unlock the database." Lock database / lock views controls.
- Record-as-page extras: comments, backlinks, page customization.

Interpretation: Notion's database satisfies the record/field/view core with a distinctive variant — the record is a page whose body is free-form content. It is embedded in a workspace product (pages, docs, wiki are the container world), which makes it the workspace-embedded pole rather than a standalone Type instance.

## Product F — FileMaker (boundary anchor, historical bridge)

### Key observations (evidence A/B — product page)

- "Claris FileMaker is a low-code platform for building custom apps tailored to your exact business needs, running natively on Mac, Windows, iPhone, iPad, and the web… FileMaker has **more than 40 years of history** helping businesses solve real problems with software built specifically for them."
- Core features framing: Script Engine ("automates hundreds of steps… without needing a traditional programming language"); "Build once. Deploy everywhere"; "Security is native to the data architecture"; record-level security ("define precisely what each user or group can view, create, edit, or delete").
- Product family: Pro (build), Server/Cloud (host), Go (mobile), WebDirect (browser).

Interpretation: FileMaker is the living representative of the forms-over-data generation (user-defined fields, records, layouts as views, find/sort, calculation fields) that today self-positions as a low-code app platform. It is the straddle pole between this Type and the low-code/no-code app-builder family — the low-code pass already claimed it as that family's ancestry. For this Type it serves as the historical bridge: the record/field/layout model predates the web era by decades.

## Product G — Smartsheet (boundary/drift pole; evidence via sibling passes)

Sibling-pass Tier-1 evidence (help center): rows explicitly "individual items or tasks"; permission ladder; dependencies/critical path/baselines; forms feeding rows; Gantt/board/calendar/timeline views; formula layer present. Reused here only to mark the drift boundary: when rows become managed, scheduled, dependent work items and the grid becomes the surface for a work-management object model, the product has left this Type (documented in `research/collaborative-spreadsheet.md` and `research/spreadsheet-application.md`).

## Cross-product Comparison

| Dimension | Airtable | Grist | Baserow | NocoDB | Notion (anchor) |
|---|---|---|---|---|---|
| Self-label | "system of record… next-gen app-building platform"; Databases = "relational databases" | "relational spreadsheet"; "spreadsheet-database tool" | "open-source online database tool"; "no-code platform to create a database" | "no-code database platform"; "no-code interface for databases" | "Databases… are collections of pages" (feature of a workspace) |
| Container | Base (tables as tabs) | Document (tables; pages of widgets) | Workspace → database application → tables | Base (tables) | Database (full-page or inline in a page tree) |
| Table | "holds information about one type of item"; records + fields | table of records; starts with A/B/C columns renamed to fields | "rows and columns, but… the columns are called fields"; own schema in PostgreSQL | CRUD on Tables, Fields, Records | collection of pages with properties |
| Field typing | 27 documented field types; "users can customize most field types" | 11 types + Any with auto-narrowing; soft enforcement (error highlight, entry allowed) | "column definition… accepts only a certain data type"; default set + plugin extensible | "Rich Field Types: Text, Number, Date/Time, Select, Attachment, Formula, Links, Lookup, Rollup and more" | properties with types (dates, status, links…) |
| Record | "individual item in a table… basic unit of data"; primary field as its description; comments + revision history per record | row addressed as `rec`; record cards; row IDs | rows; values accepted depend on fields | records (CRUD; webhooks on create/update/delete) | item = its own page (free-form body) |
| Query | per-view filter conditions (field + operator + value); sort; group | search/sort/filter; lookups; summary tables | view filters (pluggable); sort | "Sort, Filter, Group By, Search" per view | per-view filters/sorts/group |
| Views | grid (default), form, calendar, gallery, kanban, list, timeline, gantt; collaborative/personal/locked views | widgets: table, card/card list, form, chart, calendar, custom; custom layouts; linking widgets | grid (default) + pluggable view types; per-view settings | grid (default), form, gallery, kanban, calendar, timeline, gantt, list, map; collaborative/locked/personal | table (default), list, board, calendar, gallery, chart |
| Relations | linked record field (within base); lookup; rollup; count | Reference / Reference List columns; lookups; `lookupOne/lookupRecords` | link fields (link-to-table) | Links, Lookup, Rollup | relations property; linked data sources |
| Computed values | formula fields ("based on… fields in that same record"); rollup aggregates | formula columns (column-bound, Python + Excel-like functions); trigger formulas; summary formulas | formula field (tutorial + technical guide) | Formula field type | formulas (property type) |
| Forms | form view ("collect data that is then saved to an Airtable base") | form widget | form view type | form view type | forms (database feature) |
| Collaboration | permission ladder (Owner/Creator/Editor/Commenter/Read-only); record comments; real-time | real-time; granular access rules "down to each row and column" | live collaboration in workspaces; roles | roles at workspace/base/table/field/record levels; collaborative/locked/personal views | sharing + "Can edit content" data-vs-structure split; lock database/views |
| Automation layer | automations (trigger + actions); scripting; agents | automations; webhooks; integrators | (API/webhook surface; plugin extensibility) | workflows; scripts; webhooks | automations |
| App-building layer | Interface Designer ("curated representation of base data"); extensions; "App = base + automations + interfaces…" | dashboards via custom layouts/widgets | application abstraction (plugins can add application types) | dashboards; page designer extension | (the whole workspace is the surface) |
| AI | Omni assistant; field agents; AI app building | AI formula assistant; AI spreadsheet generator | AI-assistant setup docs | NocoAI (assisted base/table/field/view/formula creation) | Notion AI; build-with-AI database creation |
| API | REST API; personal access tokens; MCP server | REST API; webhooks; SQL endpoint; MCP | REST API + WebSocket API | REST APIs; MCP server | Notion API |
| Substrate | vendor cloud (multi-tenant); HyperDB scale tier | cloud or self-host; SQLite file format | cloud or self-host (Docker/K8s/…); PostgreSQL-backed | cloud or self-host; connects to external SQL databases | vendor cloud |
| Interchange | CSV import (extension); sync integrations | import/export (CSV/Excel); Airtable import webinar | CSV import; REST API | import/export; NocoSync from dev tools | import/export |

## Canonical Model

### L0 — Defining Invariant

```text
User-defined table of records — the unit of record
└── Named, typed fields — the schema the user defines; the application
    imposes field-level meaning on entry, display, and filtering
    (the "structured" pole: app-imposed semantics, vs the spreadsheet's
    semantically empty addressed grid)
└── Records — rows are individual items, addressed and acted on as wholes
    (opened, edited field-by-field, linked, commented, deleted as a unit)
└── Views — multiple named presentations over the same records, each
    combining a layout (tabular grid and a per-record form/detail surface
    at minimum) with its own sort / filter / find configuration
    (the "database" pole: query and re-presentation over records)
```

Three structures, jointly held. The whole is operated by direct manipulation — schema defined by creating and typing fields, data entered and edited in views, queries configured as view settings — with no query language, no server administration, and no programming required for core operation (the "lightweight database" posture).

Removal tests:

- **Remove typed fields** (columns become untyped) → a semantically empty value grid — Spreadsheet Application territory.
- **Remove record identity** (data addressed by cell position, no record as a unit) → the spreadsheet's cell model.
- **Remove views** (one fixed presentation, no per-view query configuration) → a static table document / bare data grid; the record model loses its user-facing surface.
- **Remove user-definition of the schema** (fields predefined by the vendor for a domain) → a domain system of record (CRM-class), not this Type.

Nothing about multi-table containers, linked records, computed fields, choice/attachment fields, collaboration, permissions, forms-for-collection, APIs, automations, interfaces/dashboards, AI, cloud vs self-host, or the specific view catalog beyond grid+form is required by the definition — the flat-file/end-user database generation that predates all of those is still unambiguously this Type (see Historical Check).

### L1 — Common Mature Structure

Present in essentially all mature modern products; makes the Type practical but does not define it:

- **Multi-table container** — base (Airtable) / document (Grist) / database application (Baserow) / base (NocoDB) holding several tables, each for one type of item, commonly shown as tabs.
- **Linked records / relations** — a field type that connects records across tables (Airtable linked record "always within the same base"; Grist Reference columns; Baserow link fields; NocoDB Links; Notion relations), with **lookup** (pull a field from the linked record) and **rollup/count** (aggregate over linked records) as the companion machinery.
- **Computed fields** — formula fields/columns computing a per-record value from other fields of the same record (Airtable formula field; Grist formula columns; NocoDB/Baserow/Notion formula types). Semantics are field-bound and record-scoped — categorically different from the spreadsheet's cell-addressed formula graph (see Boundary Findings).
- **Choice / select fields** with user-defined option sets (colors, ordering); **attachment** fields holding files/images per record; **user/collaborator** fields; **date/number/currency** formatting per field.
- **Record-level collaboration** — sharing with permission ladders (Airtable Owner/Creator/Editor/Commenter/Read-only; NocoDB workspace→record levels; Notion's data-vs-structure "Can edit content" split), record comments, real-time co-editing, record revision history, trash/restore, snapshots (Airtable) / document history (Grist).
- **Forms for data entry** — a form view/widget that collects submissions into the table (Airtable form view; Grist form widget; Baserow/NocoDB form view types).
- **Import/export interchange** — CSV/Excel-class import-export as the lingua franca; "drop in a spreadsheet" as the universal on-ramp (Airtable's own onboarding line).
- **API access** — REST APIs across the modern sample (plus webhooks, WebSocket, SQL endpoints, MCP servers at various poles).
- **Templates** — preconfigured bases/databases per use case (CRM, inventory, projects…).
- **Aggregation surfaces** — group-by, summary tables/widgets, charts over records (Grist summary tables; NocoDB dashboards; Airtable reporting/extensions).
- **Search** across records and fields.

### L2 — Variant / Optional Structure

- **Automations / workflows / scripts** — trigger→action machinery, JavaScript/Python scripting, webhooks (Airtable automations; NocoDB workflows/scripts; Grist automations/webhooks). Optional layer on the record store.
- **Interfaces / dashboards / app-building layer** — curated UIs over the data (Airtable Interface Designer; NocoDB dashboards + page designer; Grist custom layouts). The drift layer toward the no-code/low-code app-builder family; presence does not change the Type as long as the data table remains the unit of record (see Boundary Findings).
- **AI assistance** — formula generation, base/table/view generation, AI field agents, conversational analysis (all sampled products ship some form; era machinery).
- **Deployment substrate** — vendor cloud multi-tenant (Airtable, Notion) vs self-hostable open source (Grist SQLite files, Baserow Docker/K8s, NocoDB self-host) vs database-connected (NocoDB operating external PostgreSQL/MySQL/SQL Server through the same interface).
- **Record-as-page** — Notion's variant where the record opens as a free-form page (properties on top, arbitrary content beneath).
- **Granular access rules** — row/column-level access control as a differentiating depth (Grist access rules; NocoDB field/record-level roles) vs container-level ladders.
- **View-type catalog breadth** — kanban, calendar, gallery, timeline, gantt, map, list, chart; collaborative/personal/locked view permission postures. Only grid+form duality is constant.
- **Sync / federation** — syncing records from external sources into tables (Airtable Sync; NocoDB NocoSync).
- **Scale machinery** — large-record tiers (Airtable HyperDB positioning), performance guidance (Notion load-time docs).
- **Suite/workspace embedding** — standalone product (Airtable, Grist, Baserow, NocoDB) vs database-as-feature inside a workspace product (Notion).

### L3 — Vendor-specific Structure (Research Notes only)

- Airtable: base guide; Omni AI assistant; field agents (AI-powered dynamic fields) + field agent catalog; HyperDB ("record limits in the hundreds of millions" positioning); verified data library (Enterprise); billable-collaborator billing model; interface-only collaborators; invite links; Universe (public base sharing); extensions marketplace; two-way sync (limited beta); trash retention window; primary-field cannot be deleted/moved/hidden; MCP server.
- Grist: Python formula language + all-caps Excel-like function suite; `$Column` / `rec` / `table` formula bindings; trigger formulas (apply-to-new-records / apply-on-record-changes with column conditions; `value` and `user` variables); column behaviors (Data/Formula/Empty) with freeze-to-data conversion; summary tables & summary formulas; access rules with link keys; document history; SQLite storage format; self-hosted editions incl. sovereign deployments (France's LaSuite); Airtable-import tooling.
- Baserow: plugin architecture (field types, view types, view filters, application types as extension points); user tables materialized as PostgreSQL tables with generated models; per-view settings isolation (column width per view); 72-hour trash default (environment variable); extensive self-hosting guide catalog.
- NocoDB: NocoAI / NocoDocs / NocoSync branded layers; extensions (Bulk Update, Data Exporter, Dedupe, Org Chart, Page Designer, URL Preview); MCP server; external-database connections.
- Notion: record-as-page with backlinks and page comments; data sources & linked databases; "Can edit content" permission level; lock database/lock views; 1,000-item sort/index behavior note.
- FileMaker: Script Engine; layouts; FileMaker Server/Cloud/Go/WebDirect product family; record-level security; 45-day trial; "more than 40 years of history" self-claim.
- Smartsheet (sibling passes): rows-as-tasks overlay, dependencies/critical path/baselines, premium modules — the work-management drift pole.

## Vendor-specific Findings

- Airtable's "App = base + automations + interfaces + extensions" definition, with "the base is the underlying relational database structure of an app you build," is the clearest vendor articulation of the data-table-as-substrate posture — used as boundary evidence vs app builders, but the Interfaces/agents machinery itself is vendor-specific layer.
- Grist's Python-in-cells formula model and trigger formulas are product-specific realizations of the computed-field capability; the canonical concept is "per-record computed values," not Python.
- Baserow's PostgreSQL materialization (user tables as real database tables) is an implementation choice; Grist's SQLite files and Airtable's proprietary cloud store are the counter-poles — substrate is not definitional.
- NocoDB's external-database connectivity is the database-first variant; the other sampled products store in their own substrate.
- Notion's record-as-page is a variant that stretches (but does not break) the record model; its workspace embedding is a packaging variant.
- Type-enforcement depth varies: Grist documents soft typing (any value enterable, incompatible values flagged); Baserow documents fields that "accept only a certain data type"; Airtable documents per-type behaviors without a blanket hard/soft claim. The canonical invariant is "the field carries defined kind/semantics that shape behavior," not a specific enforcement mechanism.

## Rejected Findings (considered for the core, rejected)

- **Linked records / relations as definitional** — rejected: the flat-file generation (single-table databases with browse+form views) satisfies the Type without relations; relations are the strongest common-mature structure (universal in the modern sample) but the historical check keeps them at L1. The seam vs spreadsheets stands on typed fields + records + views even for single-table use.
- **Computed fields / formulas as definitional** — rejected: the Type works with no computed fields at all (pure data entry + query); and where present, their semantics (field-bound, record-scoped) are a capability inside the record model, not the Type's computation model. Grist's spreadsheet-engine heritage makes this the tempting over-generalization; the other sampled products treat formulas as one field type among many.
- **Cloud / real-time multi-user as definitional** — rejected: historical single-user products and self-hosted single-user poles fit; collaboration depth is L1/L2.
- **Specific view catalog (kanban/calendar/gallery/gantt) as definitional** — rejected: only the grid+form duality is constant across eras; the rest is variant breadth.
- **"No-code" label machinery (drag-and-drop, AI base generation) as definitional** — rejected: the defining posture is direct-manipulation operation without query language or server administration; AI generation is era-current implementation.
- **SQL/query-language access as definitional** — rejected: none of the sampled products require SQL for core operation; NocoDB's SQL connectivity is a variant substrate choice.
- **Multi-table containers as definitional** — rejected: single-table documents/bases satisfy the Type; the container is L1 organization.
- **Forms-for-collection as definitional** — rejected: a form view is one entry surface; the Type operates fully without it.

## Historical / Market-Sample Check

Check applied: would older, regional, platform-native, or differently positioned products still fit the L0?

- **Era**: the flat-file / end-user database generation (1980s works-suite database modules and dBase-class products; the FileMaker lineage) is described by its surviving structure: user-defined typed fields, records, browse/list + form/layout views, sort/find — exactly the L0 chain, with no linked records, no APIs, no collaboration, no cloud required. Fetched anchors: FileMaker's own "more than 40 years of history" claim (the lineage predates the web era); a Grist case-study quote positioning Grist "between Excel and Access" and against "sharing an Access database" — the vendor's own market frames this Type as the continuation of the end-user database lineage. No precise historical capability claims asserted beyond these fetched artifacts. ✓
- **Platform-native / regional**: Grist's sovereign-deployment pole (LaSuite, France) and the OSS self-host poles (Baserow, NocoDB) fit with no change to the core. ✓
- **Differently positioned**: Notion's workspace-embedded databases fit the core with the record-as-page variant; FileMaker fits the core historically but has drifted to self-identify as a low-code app platform (straddle pole, recorded as boundary evidence, not a counterexample). Smartsheet fails the record-model test in its work-management overlay (rows become scheduled dependent tasks) — drift pole, consistent with the sibling passes. ✓
- **The spreadsheet's own "Tables" features** (named columns/filtering over ranges inside spreadsheet products) were not sampled this pass; conceptually they sit on the spreadsheet side of the seam (the addressed cell grid remains the model; column names are annotations over it). Recorded as an uncertainty, not asserted.

## Boundary Findings

| Neighbor | Seam (what to remove / what remains) | Evidence |
|---|---|---|
| **Spreadsheet Application** (§03.03 sibling, processed — forward note RATIFIED with refinement) | The spreadsheet's center is the addressed cell grid — semantically empty — with cell-addressed formulas and dependency-driven recalculation as the computation model. This Type's center is the user-defined record table — typed fields impose meaning, rows are records, and views query/re-present records. Computation, where present, is field-bound and record-scoped (a formula field computes "based on… fields in that same record" per Airtable; a Grist formula "applies to a whole column" referencing same-row fields). Remove typed-field/record semantics → spreadsheet; add them → this Type. **Refinement of the sibling's proposed seam:** relational record links are NOT required for the seam — the flat-file era and single-table use satisfy this Type without them; the load-bearing seam is typed fields + records + views. Grist is the decisive hybrid evidence: it keeps a spreadsheet formula engine but binds it to columns/records and adds typed columns + references + views → structured-table side. | A (Airtable glossary/field-types; Grist col-types/formulas; Baserow database-plugin; NocoDB features) + sibling-pass cross-reference |
| **Collaborative Spreadsheet** (§03.03 sibling, processed) | Same data-model seam as above; the collaboration layer is the sibling's defining layer, not this Type's. Structured-table products are typically multi-user by default, but multi-user operation is not what makes them this Type. | sibling-pass definitions + A |
| **No-code Application Builder** (§12, processed — flag DISCHARGED with evidence) | The no-code builder centers the composed application (data substrate + interfaces + logic as one managed artifact, platform-run). This Type centers the data table with views; interfaces/dashboards are curated layers OVER the data. Airtable's own glossary draws the seam: "App = the sum of parts including the base, automations, any interfaces, extensions… **The base is the underlying relational database structure of an app you build**"; an interface is "a curated representation of base data." Airtable is the straddling pole (Interface Designer, app-building positioning) — center-of-gravity test: the base/table remains the unit of record and the primary surface; in a no-code builder the application is the unit of record and the data is a component. NocoDB's "no-code database platform" self-label and Baserow's "no-code platform to create a database" show the market naming the same posture from the data side. | A (Airtable glossary; NocoDB overview; Baserow docs) + no-code-pass cross-reference |
| **Low-code Application Platform** (§12, processed — flag DISCHARGED with evidence) | The LCAP centers the full application factory (logic depth, SDLC machinery, governance, multi-target deployment). This Type centers the data table. FileMaker is the living straddle: it self-positions as "a low-code platform for building custom apps" while carrying the record/field/layout model — the shared ancestry both passes recorded. The gradient: when script engines, deployment machinery, and application lifecycle become the center, the product is LCAP; when the table + views remain the center, it is this Type. | A (FileMaker positioning) + low-code-pass cross-reference |
| **Online Form Builder** (§03.11, processed — watch item DISCHARGED) | The form builder centers the question instrument and the collected per-submission records for downstream use; this Type centers the owner-side data model the form feeds. Database products' form views (Airtable form view "collect data that is then saved to an Airtable base"; Grist form widget; Baserow/NocoDB form view types) are entry surfaces into the table — the reverse direction of the form builder's form-to-records pipeline. Center-of-gravity test holds. | A (Airtable glossary; NocoDB/Baserow view types) + form-builder-pass cross-reference |
| **CRM / domain systems of record** (§05–§25 family) | Domain systems carry predefined schemas and workflows (contacts, deals, patients, work orders); this Type is the generic tool where the user defines the schema. The relationship is compositional: users build lightweight domain systems IN this Type (Grist ships a "Lightweight CRM template"; Notion documents building "an all-in-one CRM database"; Airtable's template gallery is CRM/inventory/project-shaped). Remove user-defined schema → domain Type. | A (Grist templates; Notion intro; Airtable templates) |
| **Database IDE / SQL Client / Database Management Console** (§12/§13) | Those Types operate real database servers through query languages and admin tooling for technical users. This Type gives end users database semantics (schema, records, queries, relations) through direct manipulation — no query language, no server administration. NocoDB is the bridge pole: it connects to real databases but operates them through the spreadsheet interface. | A (NocoDB overview) + prior-pass definitions |
| **Work Management Platform / Project Management** (§03.06/03.07) | The drift path (Smartsheet, documented in sibling passes): when rows become scheduled, dependent, approvable work items and the grid becomes the surface for a work object model, the product has moved to Work Management. If rows remain records in a user-defined table, it stays this Type. | sibling-pass Tier-1 evidence |
| **Notion-class workspace / PKM products** (§03.02) | The workspace product's center is pages/docs/wiki; databases are one object type inside it. The database capability itself satisfies this Type's core (properties, items, views) with the record-as-page variant. Boundary anchor, not a taxonomy conflict: the capability is real inside both product shapes. | A (Notion intro-to-databases) |
| **BI / Dashboard Platform** (§13) | BI presents governed data for consumption; this Type is the editable record store the dashboards read from. Dashboard/interface layers in sampled products are presentation surfaces over records. | A (Airtable interface definition; NocoDB dashboards) + prior-pass definitions |

**"去掉什么就变成另一个 Type" summary:** remove typed fields → spreadsheet/value grid; remove record identity → spreadsheet; remove views/query → static table document; remove user-defined schema → domain system of record; remove direct-manipulation posture (require SQL/admin) → database tooling; make the composed app (not the table) the unit of record → no-code/low-code builder; make rows managed work items → work management.

## Uncertainties

- The spreadsheet products' own "Tables" features (named columns/filtering inside Excel/Sheets-class products) were not sampled; their placement on the spreadsheet side of the seam is reasoned, not evidenced.
- Historical flat-file products (AppleWorks DB module, dBase, Approach, Paradox, Access) have no reachable official documentation; the era check is conceptual, anchored by FileMaker's fetched 40-year claim and Grist's fetched Access-comparison quotes.
- Knack, Zoho Tables, SeaTable, Teable, and Airtable's deeper guides (permissions article bodies, automations internals) were not fetched; market anchors only.
- Type-enforcement depth (hard vs soft typing) is documented explicitly only by Grist (soft) and Baserow (accepts-only); Airtable's enforcement posture was not directly evidenced — the canonical invariant is phrased at "field carries defined semantics" strength.
- Airtable's current app-building positioning (Interfaces, agents, HyperDB) is drifting toward the app-builder family; the center-of-gravity judgment (base remains the unit of record) rests on the glossary's own definitions, not on long-term market observation.
- No numeric limits (record caps, field counts, view counts, plan gates) are asserted in the final document; observed figures live here as L3.

## Final Synthesis

The Structured Table / Lightweight Database Application is the end user's database: a tool where the user defines tables of records — named, typed fields imposing meaning the spreadsheet's empty grid never has — and then queries and re-presents those records through multiple views (the tabular grid and the per-record form at minimum, each carrying its own sort/filter configuration), all by direct manipulation, with no query language, no server administration, and no programming required. Around that core, mature products add the standard layer: multi-table containers, linked records with lookups and rollups, per-record computed fields, choice/attachment/user fields, collaboration with permission ladders and record comments/history, forms for collection, CSV/Excel interchange, APIs, templates, aggregation surfaces, and search. Automations, interfaces/dashboards, AI assistance, deployment substrate (cloud/self-host/database-connected), record-as-page, granular access rules, and view-catalog breadth are variant layers. The Type is the record/field pole of §03.03: the spreadsheet computes over an empty grid; this Type organizes meaning into records. It is the generic schema-defining tool from which users assemble lightweight domain systems, the data substrate over which app-builder layers are optional, and the direct descendant — by the vendors' own framing — of the end-user database lineage that predates the web.
