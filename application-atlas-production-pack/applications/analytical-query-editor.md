# Analytical Query Editor

## Overview

An **Analytical Query Editor** is the query-authoring surface of an analytical data platform: an editor in which a user composes analytical queries — in practice, SQL statements and scripts — runs them immediately against the platform's data (a cloud data warehouse, a lakehouse, or a serverless analytical query service), reads the answer as a result grid, and refines the query in place until it answers the question.

The defining core is small:

```text
Analytical data platform (its warehouse / lakehouse / query service)
└── Query editor surface (SQL-first text editing of queries)
    └── Immediate execution against that platform's data
        └── Result returned as a data grid
            └── In-place edit-and-re-run refinement
```

Everything else commonly associated with these editors — result charts, saved queries, query history, sharing, AI assistance, scheduling, query profiles — is standard capability that mature products add around this core, not what makes the product an analytical query editor.

The boundary in one sentence: this is the surface where a technical user writes queries against an analytical platform's own data — not a general-purpose tool for any database (SQL client / database IDE territory), not a governed question-answering surface for business users (ad-hoc query territory), and not an administration console (database management console territory).

## Users & Context

The primary users are technical data practitioners who work directly with an analytical platform's data:

- **data analysts** — exploring datasets, validating metrics, prototyping the queries that later become reports or dashboards
- **data engineers** — inspecting data, testing transformations, debugging pipeline outputs, profiling query performance
- **technically skilled power users** — writing one-off queries that no prepared report answers

Secondary users include data scientists (running SQL alongside notebook work) and developers (testing SQL that applications will issue). The work context is almost always the analytical platform's own web interface — a worksheet or query tab inside the platform's portal, or in one observed pattern, a dedicated web client for the platform. The editor is a working surface, not a consumption surface: people come here to *ask new questions of the data*, not to read prepared content.

## Core Model

### The Defining Core

Five properties. If any one is removed, the product is no longer recognizable as an analytical query editor:

- **Bound to an analytical data platform** — the editor operates on one platform's analytical data: its warehouse, lakehouse, or query service. It is not a connection-agnostic tool for arbitrary databases. This binding is what makes the editor *analytical*: the data is analytical storage, the queries are analytical workloads (scans and aggregations over large datasets), and the surrounding affordances are analytical (results at scale, data-scanned and cost visibility, query performance tooling).
- **Query editor surface** — a text editor for composing query statements and scripts in the platform's SQL dialect. The unit of work is the query, authored by the user. Editing affordances (completion, highlighting, formatting) exist to serve this act.
- **Immediate execution** — the query runs now, in the user's session, and the answer returns in seconds to minutes. Long-running analytical queries are a normal case, not an exception.
- **Result grid** — the answer is a tabular result set the user can inspect directly. Most products cap the interactive preview at a defined row count; the full result may live elsewhere (see Rules).
- **In-place refinement** — the user edits the query and re-runs it in the same surface. The loop — compose, run, read, adjust, re-run — is the working rhythm of the Type.

### Standard Capabilities

Mature products commonly add a ring of capabilities around the core. They make the editor practical for real work but do not define it:

- **Saved query artifacts** — the query (or the worksheet holding it) persists as a named object, organized in folders or a workspace, so work accumulates instead of evaporating.
- **Query history** — a record of past runs (what ran, when, how long, with what status), per editor surface and often account-wide, with a defined retention window.
- **Result charts** — visualization generated from the current result set without leaving the editor.
- **Export** — download results as CSV/TSV or open them in spreadsheet tools; size limits vary by product.
- **Schema/object browsing** — a tree or explorer of the platform's databases, schemas, tables, and views, usually with the ability to insert object or column names into the editor.
- **Editing aids** — autocomplete (keywords, functions, table and column names, sometimes tracked aliases), syntax highlighting, formatting, keyboard shortcuts.
- **Query observability** — per-run details (duration, row count, data scanned) and, in several products, an execution-plan view (query profile) with automatic performance insights.
- **AI assistance** — natural-language help for writing, explaining, or fixing queries; now common across the category, but one authoring aid over the same loop.
- **Sharing and collaboration** — shared worksheets or queries, folder-level sharing, comments; one sampled product supports real-time co-editing.
- **Scheduling** — running saved queries on a schedule as jobs, in some products.
- **Cost visibility** — how much data a query scanned or how much compute it consumed; in at least one product, even some result-manipulation interactions carry compute cost.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Query artifact:      worksheet holding statements · named query object · auto-saved query tab
Editor embedding:    pane in the platform portal · dedicated web client for the platform
Result substrate:    in-session grid only · grid plus service-stored result files
Execution compute:   platform warehouse · dedicated SQL compute · serverless per-query
```

A reader who has only seen one implementation (say, a query tab inside a cloud platform's portal) should still be able to recognize the others — including older standalone query clients aimed at a single warehouse — from the core model.

## How It Works

### Author the query

```text
Open the editor (new worksheet / query tab / last-open query)
→ set the context (database/schema, role, or compute resource the query will use)
→ write the query, with completion and object browsing at hand
→ optionally: ask an AI assistant to draft, explain, or fix the SQL
```

There is no question wizard and no field-dragging surface here — authoring means writing the query, with aids to speed it up. (Some platforms ship a separate visual query editor as a sibling surface; the SQL editor remains the Type's center.)

### Run and read

```text
Run the current statement — or the whole script
→ the query executes against the platform's data (seconds to minutes; long runs are normal)
→ the result grid appears (commonly a capped preview of the full result set)
→ inspect: navigate cells, copy selections, view per-run details (duration, rows, data scanned)
→ optionally: switch the result to a chart, or download/export it
```

In some products a running query can be left to finish in the background, with a notification when it completes.

### Refine

```text
Adjust the query (filter, regroup, rewrite, parameterize)
→ re-run in the same surface
→ compare against the previous result (history makes earlier runs retrievable)
```

### Persist and hand off

```text
Save the query/worksheet (named artifact in a folder or workspace)
→ share it with teammates (permissions apply)
→ optionally: schedule it as a recurring job
→ optionally: turn the result into a database object (a view, or a table populated from the query)
→ optionally: hand the result onward to visualization or notebook surfaces
```

### Capability tiers

**The defining core** — without these, not an analytical query editor:

- analytical-platform data binding
- SQL-first query editor surface
- immediate execution
- result grid
- in-place refinement

**Standard capabilities** — present in most mature products:

- saved query artifacts and organization
- query history
- result charts
- export/download
- schema/object browsing
- completion, highlighting, formatting
- query observability (details, profiles, insights)
- AI assistance
- sharing/collaboration
- cost visibility
- scheduling (category-common)

**Common variants and optional capabilities** — depend on platform and product:

- parameters with input widgets
- saving results as views/tables
- background execution with notification
- DDL/administration from the editor (creating databases, schemas, tables, functions)
- sibling surfaces: notebooks, dashboards, visual query editors, semantic/metric layers
- programmatic (API) access to the same query objects

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Query editor (worksheet / query tab)

The primary surface.

- a text editor for the platform's SQL dialect, usually one tab per query or worksheet
- context selectors (database/schema, role, compute resource) and an object explorer alongside
- primary actions: write, format, run statement, run all, save, share

### Results grid

Where the answer is read.

- the tabular result set with spreadsheet-like navigation and selection
- per-run metadata (status, duration, rows returned) and a messages area for errors/notices
- primary actions: inspect, search within results, copy, chart, download/export

### Object / schema explorer

The map of what can be queried.

- databases, schemas, tables, views (and in some products functions and procedures) in a tree
- primary actions: browse, search, insert object or column names into the editor

### Query history

The record of past runs.

- per-surface and/or account-wide list: query text, time, duration, status, identifiers
- primary actions: filter, open a past run, re-open its query or results

### Query details / profile

The observability surface.

- execution details (duration, data scanned, compute used) and, where offered, the execution plan
- primary actions: inspect, identify bottlenecks, follow optimization suggestions

### Charts from results

A lightweight visualization surface over the current result set — not a dashboard builder; dashboards, where the platform offers them, are sibling surfaces.

## Important Rules / Behaviors

### Results are previews, not extracts

The interactive grid commonly shows a capped portion of the result set; the full result may be retained by the service (in some platforms, results are written to service-managed or customer-owned storage) and exported separately. Reading a result grid is therefore not the same as extracting all query output.

### Execution semantics are per-run

Several products document that each run is an independent session or batch: session state set in one run does not carry into the next, and transaction control across runs is limited or unsupported. Scripts that depend on session continuity need product-specific handling. This is a first-class behavior of the Type, not an implementation footnote.

### Cost follows the query — and sometimes the result

Analytical queries consume real compute. Products surface this as data-scanned or compute-cost metadata, and in at least one product some result-manipulation interactions (such as sorting the full result set) themselves incur compute cost billed to the resource that ran the query. Cost visibility is a structural concern of the Type, not a nice-to-have.

### Permissions and roles shape everything

What a user can query, which objects are visible in the explorer, whether results can be shared or even read, and under which role a shared query executes — all are governed by the platform's permission model. Sharing a query does not automatically grant the recipient the right to run it against the underlying data.

### Long-running is normal

Analytical queries over large data routinely take longer than interactive web users expect. Products respond with running/queued status display, cancellation, and in some cases background continuation with completion notification.

### The editor is one surface of a platform

In the current market the editor almost always lives inside a larger platform UI alongside notebooks, dashboards, catalogs, and administration consoles. The editor's identity stays distinct: its center of gravity is authoring and running queries.

## Variants

- **Platform workspace editor** — a worksheet/query surface embedded in the analytical platform's portal, alongside notebooks, dashboards, and catalogs (the dominant modern form).
- **Standalone web client for a platform** — a dedicated web application for authoring and running queries on one platform's data, separable from the platform's main console.
- **Console service editor** — the query surface of a serverless analytical query service, where results persist to service-configured storage and cost is per query.
- **Dialect families** — the same structure over different SQL dialects (ANSI-style, T-SQL, platform-specific extensions); the Type is dialect-agnostic.
- **Historical standalone query clients** — desktop query tools aimed at a single warehouse; they satisfy the defining core without portal embedding, AI, or sharing, and remain valid members of the Type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| SQL Workbench | general-purpose SQL surface across many databases/connections; not bound to one analytical platform; general database work rather than analytical-platform work — a binding/audience gradient, flagged for joint review |
| Ad-hoc Query Application | the same compose→run→read→refine loop, but for business users: question-first authoring (GUI/search/natural language) over governed data spaces, with saved shareable questions feeding dashboards; here the user writes the query itself against the platform's raw analytical data |
| Database Management Console | administers the database/instance (users, roles, compute, cost, security); this Type authors and runs queries; some editors allow object creation, but administration is not their center |
| Database IDE / SQL Client | development tools across databases (schema design, debugging, refactoring); connection-agnostic; this Type is the analytics platform's own query surface |
| Business Intelligence Platform | curates persistent artifacts (dashboards, reports) for consumption and distribution; the editor produces queries and result sets that may feed those artifacts |
| Dashboard Platform | persistent, curated, viewer-facing surfaces; remove query authoring from an analytical query editor and a viewer remains — restore it and this Type returns |
| Data Science Workbench | notebook-centered (Python/R) modeling and statistics; the platforms ship both as sibling surfaces, but the notebook is not the query editor |
| Query APIs / CLI tools | programmatic query submission without an authoring editor or result grid — developer plumbing, not this Type |

The two most important boundaries: against the **SQL Workbench** (the vocabulary overlaps — one sampled product self-describes as a "web-based SQL client application" — but the binding to one analytical platform's data and the analytical-result affordances are what define this Type), and against the **Ad-hoc Query Application** (the loop is shared; the difference is who authors what — a SQL statement for technical users vs a governed question for business users).

## Representative Products

- Snowflake — Snowsight worksheets
- Databricks — SQL editor
- Amazon Athena — console query editor
- Amazon Redshift — query editor v2
- Microsoft Fabric — SQL query editor

The core model was checked against the standalone-client form (a sampled product that is explicitly a separate web client rather than a portal pane) and against the historical standalone warehouse query client pattern, to avoid defining the Type by today's portal-embedded, AI-assisted implementation.

## Sources

Research date: **2026-09-06**

Primary vendor documentation (official product documentation sites):

- Snowflake — https://docs.snowflake.com/en/user-guide/ui-snowsight , https://docs.snowflake.com/en/user-guide/ui-snowsight-query
- Databricks — https://docs.databricks.com/en/sql/index.html , https://docs.databricks.com/aws/en/sql/user/sql-editor/
- Amazon Athena — https://docs.aws.amazon.com/athena/latest/ug/what-is.html , https://docs.aws.amazon.com/athena/latest/ug/querying.html
- Amazon Redshift — https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor.html , https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2.html
- Microsoft Fabric — https://learn.microsoft.com/en-us/fabric/data-warehouse/sql-query-editor

> Sourcing limitations: Google BigQuery documentation could not be reached from the research environment (timeouts on 2026-09-06) and ClickHouse Cloud's SQL console page was not retrievable — neither product is sampled and no claims are made about them. The Athena console page returned an empty shell, so Athena's editor-surface specifics are evidenced only at the service/results/history level. Precise operational values (row caps, retention windows, size and duration limits) are product-specific and are intentionally not stated in this document; they are recorded in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
