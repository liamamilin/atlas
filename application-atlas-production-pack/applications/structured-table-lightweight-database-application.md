# Structured Table / Lightweight Database Application

## Overview

A **Structured Table / Lightweight Database Application** lets non-technical users build and operate their own databases: tables of records whose columns are named, typed fields the user defines, queried and re-presented through multiple views — all by direct manipulation, with no query language, no server administration, and no programming required.

The defining core is small:

```text
User-defined table of records
└── Named, typed fields (the schema the user defines)
└── Records (rows addressed and acted on as individual items)
└── Views (multiple named presentations over the same records,
    each with its own sort / filter / find configuration)
```

This is the record-and-field pole of the table family. A spreadsheet organizes an empty grid of addressable cells and computes over it; a structured-table application organizes *meaning* — what the columns are, what kind of values they hold, how records relate — and then lets the user query, reshape, and share that meaning. The "lightweight database" half of the name is the posture: the user gets database semantics (schema, records, queries, relations) without database engineering.

When the rows stop being records in a user-defined table and become scheduled, dependent work items, the product has drifted toward Work Management. When the composed application — not the data table — becomes the unit being built and run, the product has drifted toward the no-code/low-code app-builder family. Both drifts are common in today's market; the data table remains this Type's center.

## Users & Context

The primary user is a knowledge worker or small team who has outgrown a spreadsheet but cannot justify (or operate) a real database deployment: an operations coordinator tracking inventory and vendors, a marketer running a content calendar, a researcher managing a catalog, a founder assembling a lightweight CRM, a team lead tracking projects and assets. They define what their data *is* — the fields, the types, the relationships — because no pre-built application matches their exact need.

Typical reasons to open the application:

- enter and update records in a table the user (or a teammate) defined
- find and filter records to answer a question ("what's overdue?", "what's in this status?")
- re-shape the same data for a different audience or task through another view
- connect two tables so one record can reference another
- share the table with collaborators at different access levels, or collect entries through a form

Secondary roles appear in team settings: an administrator who owns the schema and permissions, editors who maintain records, viewers who only consume views, and — where the product offers them — end users of curated interfaces built on top of the data. The work environment is predominantly the browser; desktop and mobile clients typically share the same hosted data.

## Core Model

### The Defining Core

```text
User-defined table of records
└── Named, typed fields
└── Records
└── Views
```

**The user-defined table of records** is the unit of record. A table holds information about one type of item — products, contacts, tasks, projects. The user creates it, names it, and defines its columns. Nothing about the table's meaning is pre-installed; the schema is entirely the user's construction. This is what separates the Type from domain applications (a CRM ships its schema; here the user builds one) and from spreadsheets (whose grid imposes no meaning at all).

**Named, typed fields.** Each column is a field with a name and a defined kind — text, number, date, single- or multi-select from a list of options the user maintains, checkbox, attachment, collaborator, and similar. The type is not decoration: it shapes how values are entered (pickers, calendars, file drops), how they are displayed (formatting, colors, thumbnails), and how they can be filtered and grouped. The application therefore imposes field-level meaning on the data — the property the spreadsheet's semantically empty grid deliberately lacks. Enforcement depth varies by product: some products hard-restrict what a field accepts, others accept any entry and flag values that don't match the declared type; the invariant is that the field carries defined semantics that shape behavior, not a specific validation mechanism. One field per table typically serves as the record's name or description — the value used to refer to the record elsewhere in the product.

**Records.** A row is a record: an individual item, addressed and acted on as a whole. The user opens a record (as a detail card or page), reads and edits its fields, attaches files and comments to it, links it to records in other tables, tracks its change history, and deletes or restores it as a unit. Records — not cells — are what views present, what forms collect, what APIs read and write, and what collaborators mention each other about.

**Views.** The same records are presented through multiple named views, and this multiplicity is structural, not cosmetic. At minimum the Type offers a tabular grid (each record a row, each field a column) and a per-record form or detail surface; mature products add card/gallery, board, calendar, timeline, and chart layouts. Crucially, each view carries its own query configuration — which records appear (filter conditions built from a field, an operator, and a value), how they are ordered (sort), how they are grouped, which fields are visible. Views are windows over one shared record set, not copies of it.

The whole model is operated by direct manipulation: fields are created by clicking, types are chosen from menus, queries are configured with condition builders, records are entered in place. No query language, no server administration, no deployment step, and no programming are required for any of it. That posture is the "lightweight" in the Type's name.

### Standard Capabilities Mature Products Add

These are widespread in current products and expected by the market, but a product lacking them can still be recognized as this Type — the flat-file databases of the personal-computer era, the direct ancestors of this category, operated on single tables with typed fields, records, and list-plus-form views and nothing else.

- **Multi-table containers** — a base, database, or document holding several related tables (each for one type of item), commonly shown as tabs; the container is the natural unit of sharing and templating.
- **Linked records** — a field type that connects a record to records in another table (a contact to its company, a task to its project), always within the container. Companion machinery reads across the link: lookups (pull a field from the linked record into this one) and rollups or counts (aggregate over the linked records).
- **Computed fields** — a field whose value is calculated from other fields of the same record (extended-price from quantity and unit price, age from a date). Where present, the computation is bound to the field and scoped to the record — categorically different from a spreadsheet, where any cell may hold a formula referencing arbitrary other cells.
- **Rich field kinds** — select fields with user-maintained option sets (colors, ordering), attachment fields holding files and images per record, collaborator fields, formatted number/currency/date fields, auto-generated identifiers and timestamps.
- **Collaboration** — sharing a container or table with named people or links; permission ladders from read-only through commenting and editing to schema-level control; comments on records; real-time co-editing; record revision history; trash/restore and snapshots.
- **Forms for collection** — a form view that turns the table's fields into a shareable entry form whose submissions become records.
- **Interchange** — CSV/Excel import-export as the lingua franca; "drop in a spreadsheet you already have" is the industry's standard on-ramp.
- **API access** — programmatic read/write over tables and records for integrations and automations.
- **Templates** — preconfigured tables and containers for common jobs (CRM, inventory, projects), which double as the product's teaching surface.
- **Aggregation and search** — group-by summaries, summary tables and charts over records, and search across fields.

### One Structure, Many Implementations

The core model is conceptual. Products realize each piece differently, and recognizing the concept behind the implementation is what makes the whole product family legible:

```text
Concept:            the container of tables
Implementations:    base (shared with a team), document, workspace-resident
                    database, standalone table set

Concept:            typed fields
Implementations:    hard-typed columns, soft-typed columns that flag
                    mismatches, property systems on page-records

Concept:            the record
Implementations:    a grid row with a detail card, a row that opens as a
                    full free-form page, a form-collected submission

Concept:            views
Implementations:    named grid/form/board/calendar/gallery/timeline views,
                    widget layouts on a page, per-view saved filters

Concept:            relations
Implementations:    link-to-table fields, reference columns, relation
                    properties, connected data sources

Concept:            storage substrate
Implementations:    vendor cloud, self-hosted open source (file- or
                    server-database-backed), connections to external
                    SQL databases operated through the same interface
```

## How It Works

### Define the schema

```text
Create a table (or start from a template, or import a spreadsheet)
→ add fields, name them, choose each field's type
→ configure the type's behavior (option lists, formats, defaults)
→ designate the field that names each record
```

Schema definition is ongoing: fields are added, retyped, and reordered as understanding of the data evolves, and mature products track what depends on a field before it is changed or deleted.

### Enter and maintain records

```text
Add a record (in the grid, via a form, through an import or API call)
→ fill its fields (type-appropriate editors: pickers, calendars, file drops)
→ open the record as a detail surface for the full picture
→ edit over time; comments and revision history accumulate on the record
```

Records persist. The table is a living system of record for whatever the user defined it to hold — the application's value is that the record set survives sessions, users, and years.

### Query and re-present

```text
Create a view over the table
→ choose its layout (grid, card, board, calendar, timeline…)
→ configure filters (field + operator + value), sorts, grouping
→ name and share the view
→ switch between views; every view shows the same underlying records
```

This is the daily loop: the data is entered once and read many ways. A filter built for "my open items this week" coexists with an unfiltered grid and a board grouped by status — all over one record set.

### Relate tables

```text
In table A, add a link field pointing at table B
→ on each record, select the related B-records
→ pull B's fields into A with lookups; aggregate over them with rollups
→ navigate across the link in both directions
```

Relations are what turn a set of tables into a small database: tasks reference projects, line items reference products, contacts reference organizations — without duplicating anyone's data.

### Share, collect, and extend

```text
Invite collaborators (or share a link) at a permission level
→ optionally publish a form so outsiders submit records
→ optionally add computed fields, automations, or curated interfaces
→ integrate through the API as needs grow
```

The extension layers — automations (trigger → action), scripted logic, curated dashboards and interfaces over the data — are where products differentiate and where the boundary toward app-building platforms begins. They are optional: the Type is complete without them.

### Capability tiers

**Defining core** — without these, not this Type:

- user-defined table of records
- named, typed fields
- records addressed and acted on as units
- multiple views over the same records, each with its own sort/filter configuration
- direct-manipulation operation (no query language or administration required)

**Standard capabilities** — present in most mature products:

- multi-table containers
- linked records with lookups and rollups
- computed fields
- select/attachment/collaborator field kinds
- sharing, permission levels, record comments and history
- forms for collection
- CSV/Excel interchange, APIs, templates
- aggregation surfaces and search

**Optional / variant** — depends on product, segment, and era:

- automations, scripts, webhooks
- curated interfaces and dashboards
- AI assistance (generated schemas, formula help, conversational analysis)
- self-hosting, open source, external-database connectivity
- record-as-page (the record opens as a free-form document)
- row/column-level access rules
- broad view catalogs (map, gantt, chart layouts)

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Table / grid view

The default working surface.

- records as rows, fields as columns, type-appropriate cell editors
- primary actions: add/edit records inline, sort, filter, group, hide/reorder fields, open a record's detail

### Record detail / form surface

The per-record surface where the record is handled as a unit.

- all of the record's fields with their editors, plus comments, revision history, and linked-record context; in the record-as-page variant, free-form content beneath the fields
- primary actions: edit fields, link records, comment, view history, delete/restore

### View configuration

Where query and presentation are set.

- layout picker, filter condition builder (field / operator / value), sort and group controls, field visibility
- primary actions: create/duplicate views, adjust and save view settings, share a view

### Schema / field management

Where the data model is maintained.

- field list with types, add/rename/retype/reorder/delete fields, dependency hints before destructive changes
- primary actions: create and configure fields, manage option sets

### Container navigation

The home surface listing the user's bases/databases/documents and their tables as tabs or a sidebar tree — the entry point for creating, importing, templating, and sharing.

### Collection form

A shareable entry form generated from the table's fields; submissions land as records.

### Extension surfaces (optional)

Automation builders (trigger → action editors), script consoles, and interface/dashboard builders that assemble curated pages of charts, record lists, and buttons over the data.

## Important Rules / Behaviors

### The schema governs behavior

The declared field type shapes what entry looks like, what display and formatting are available, and what filters make sense. Changing a field's type is a structural operation that mature products treat with care (conversion rules, dependency warnings), because everything downstream — views, forms, automations, integrations — assumes it.

### Views are windows, not copies

Editing a record in any view changes the same record everywhere. A view's filters and sorts are configuration, not data; deleting a view never deletes records. This is the property that lets one record set serve many audiences safely.

### Records are the unit of action

Open, link, comment on, restore, and delete happen at the record level. The record's name field is how the rest of the product refers to it — in links, mentions, and pickers — which is why that field is typically protected from removal.

### Linked records reference, they do not duplicate

A link stores a reference to an existing record; the linked record's data is pulled in through lookups and aggregates, so correcting it at the source corrects it everywhere it is referenced.

### Computed fields are derived

Where a field's value is computed from other fields, it is maintained by the system on every relevant change and is not directly editable; converting a computed field into plain stored values (or the reverse) is an explicit user action where products support it.

### Structure and data are governed separately

Team products commonly separate the right to change the schema and views (add fields, change filters) from the right to change data (edit records), with permission levels — and sometimes locks — enforcing the split. This is what allows a controlled schema with many hands in the data.

### The lightweight posture is a boundary, not a limitation to apologize for

Everything the Type does is done through direct manipulation. The moment operating the data requires a query language, a server, or a deployment, the user has left this Type for database tooling — and the moment building the surrounding application becomes the point, the user has left for the app-builder family.

## Variants

Common shapes of the Type in the market:

- **standalone team product** — the classic shape: hosted containers of tables shared with a team, templates, forms, API (e.g. Airtable, Baserow, NocoDB)
- **spreadsheet-hybrid** — keeps a spreadsheet-style formula engine but binds it to typed columns and records, easing migration from spreadsheets (e.g. Grist)
- **database-connected** — the interface operates tables that live in external SQL databases, bridging to existing infrastructure (e.g. NocoDB's connectivity mode)
- **self-hosted / open source** — the same core deployed on the user's own infrastructure, often with plugin extensibility (e.g. Baserow, Grist, NocoDB)
- **workspace-embedded** — databases as one object type inside a broader docs/wiki workspace, with the record realized as a page (e.g. Notion databases)
- **app-platform-leaning** — the data core wrapped in substantial interface-building, automation, and agent layers; still this Type while the table remains the unit of record (e.g. Airtable's current positioning)
- **work-management-leaning** — the grid re-centered on scheduled, dependent work items; the drift boundary toward Work Management (e.g. Smartsheet's overlay)

A variant remains a variant unless it changes the core: if rows stop being records in a user-defined table, or the composed application replaces the table as the unit of record, the product belongs to a neighboring Type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Spreadsheet Application | the center is an addressed cell grid with no imposed meaning, computed over by cell-addressed formulas and recalculation; here the center is typed fields, records, and views |
| Collaborative Spreadsheet | the same spreadsheet grammar plus a shared-live multi-user layer; the seam with this Type is the data model, not collaboration |
| No-code Application Builder | centers the composed application (data + interfaces + logic as one managed, platform-run artifact); here the data table is the unit of record and interfaces are optional layers over it |
| Low-code Application Platform | centers the full application factory — logic depth, lifecycle, governance, deployment; here the schema-and-records store is the center |
| Online Form Builder | centers the question instrument and the collected submissions it produces; here the form (where present) is one entry surface into the owner's data model |
| CRM / domain systems of record | carry predefined schemas and workflows for a domain; this Type is the generic tool users build lightweight domain systems in |
| Database IDE / SQL Client / Database Management Console | operate real database servers through query languages and admin tooling for technical users; this Type gives end users database semantics through direct manipulation |
| Work Management Platform / Project Management Application | organize scheduled, dependent, approvable work items; here rows are records in a user-defined table, not managed work |
| Business Intelligence / Dashboard Platform | presents governed data for consumption; this Type is the editable record store such presentations read from |
| Note-taking / Personal Knowledge Management Application | centers authored pages and links; its database feature (where present) is an instance of this Type's core inside a workspace product |

The sharpest seam is with the Spreadsheet Application, because the two share a visual language — rows, columns, cells — while organizing fundamentally different worlds: the empty computed grid versus the meaningful record table. The next sharpest is with the app-builder family, because the leading products of this Type have grown interface and automation layers upward; the test is always what the product's center of gravity is.

## Representative Products

- Airtable
- Grist
- Baserow
- NocoDB

The core model was checked against differently positioned samples to avoid over-fitting to the current cloud era: Notion's workspace-embedded databases (record-as-page variant), Claris FileMaker (the living representative of the older forms-over-data generation, which self-identifies today as a low-code platform), and Smartsheet (the work-management drift pole, via the sibling passes' documented evidence).

## Sources

Research date: **2026-09-09**

Primary vendor surfaces:

- Airtable — homepage; Help Center (glossary of terminology; supported field types overview; linked record field): https://www.airtable.com/ , https://support.airtable.com/
- Grist — homepage; Help Center (columns and data types; intro to formulas): https://www.getgrist.com/ , https://support.getgrist.com/
- Baserow — documentation (index/self-definition; technical introduction; database plugin concepts): https://baserow.io/docs
- NocoDB — documentation product overview: https://nocodb.com/docs/
- Notion — Help Center, Intro to databases: https://www.notion.com/help/intro-to-databases
- Claris FileMaker — product page: https://www.claris.com/filemaker/

> Sourcing limitation: official documentation for the historical flat-file / end-user database generation (works-suite database modules, dBase-class products, Microsoft Access) could not be reached; the era check is conceptual, anchored by FileMaker's own published "more than 40 years of history" claim and by Grist's published comparisons against spreadsheets and Access. Precise operational figures (record limits, field counts, plan gates, retention windows) observed in vendor pages are intentionally not stated in this document; they remain in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample breadth check are recorded in the paired Research Notes.
