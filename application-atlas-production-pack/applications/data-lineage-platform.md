# Data Lineage Platform

## Overview

A **Data Lineage Platform** maintains a navigable graph of how data actually flows through an organization's data estate — which sources feed which tables, which jobs and queries transform them, and which reports and models consume the results — and is built around tracing that flow: from any point in the graph, follow it upstream to its origins or downstream to its consumers.

The defining core is deliberately small:

```text
Data assets & data-moving processes in systems the platform does not hold
└── The flow graph (nodes = assets and processes; edges = actual flows)
    └── Trace operations (follow any node upstream / downstream)
        └── Impact analysis & root-cause tracing
    └── Kept current against reality (a maintained record, not a drawing)
```

The platform describes flows; it never holds the data itself. Everything else commonly associated with modern lineage products — automated SQL parsing, column-level tracing, runtime event collection, time-window filters, quality overlays, natural-language questions — is widespread in current products but is not what makes the product a lineage platform. ETL suites that have shipped dependency views over their own jobs for two decades, and governance tools with manually curated flow maps, satisfy the same defining core.

When the primary object becomes the asset inventory and its discovery experience, the product is a Data Catalog; when it becomes the runtime health of data, it is Data Observability; when it becomes the execution of the flows themselves, it is an ETL/ELT platform.

## Users & Context

A lineage platform sits over a multi-system estate — warehouses, databases, transformation pipelines, orchestration schedulers, BI tools — because the problem it solves is cross-tool: no single system knows the whole journey of the data.

Typical users:

- **Data engineers and analytics engineers** — the primary operators. Before changing or deleting a table or column, they check what depends on it; when a pipeline breaks or numbers look wrong, they trace upstream to find where the data diverged.
- **BI developers and analysts** — consumers of the downstream end. They trace a metric or a report back to its foundational sources to explain why a number changed or a dashboard is stale.
- **Data stewards and governance teams** — use the graph to document how data moves, understand cross-team dependencies, and attach governance context to the flows.
- **Compliance and audit functions** — trace where regulated or sensitive data originates, how it is transformed, and which downstream assets consume it.
- **Platform/data-infrastructure teams** — configure and operate the capture machinery that feeds the graph.

The recurring questions the product exists to answer are two: *"What happens if I change this?"* (impact analysis) and *"Where did this come from / why is this wrong?"* (root-cause tracing). In organizations without such a tool, answering them means tribal knowledge, code archaeology, or days of asking around.

## Core Model

### The defining core

**1. The flow graph.** The central object is a graph with two kinds of nodes and one kind of edge:

- **Data-asset nodes** stand for the things data lives in — tables, views, files, topics, dashboards, ML models — identified as real, addressable assets in real systems. The platform holds a record *about* each asset; the asset itself stays where it lives.
- **Process nodes** stand for the things that move or transform data — pipelines, jobs, queries, scripts, notebooks, stored procedures. They explain *how* an edge came to exist.
- **Edges** record an actual flow: data moved or was derived from source to target. An edge is evidence of movement, not an arrow someone drew.

**2. Trace operations.** The graph is navigable: from any node, a user can expand upstream (what feeds this) and downstream (what depends on this), hop by hop, across systems. Two canonical jobs are built directly on this:

- **Impact analysis** — before changing or removing something, enumerate what is affected downstream (directly and transitively), often grouped by type or by owning team, with a way to notify the people who own the affected assets.
- **Root-cause tracing** — when a downstream result is wrong or stale, walk upstream to locate where the data last changed hands.

**3. A maintained record of actual flows.** The graph reflects how data *really* moves, and is kept current as systems change. This is what separates a lineage platform from a flow diagram: the nodes are managed records of identified assets, the edges are backed by captured evidence, and the picture decays if capture stops. How the graph is kept current varies widely (see below); that it is kept current does not.

### What mature products add

These capabilities are standard in mature products. They deepen the capture-and-trace loop but do not define the Type:

- **Automated capture machinery** — the graph populates itself, by one or more of: parsing a database's query history and resolving which tables each query read and wrote; collecting events emitted by running jobs; recording reads and writes natively as the platform executes them; harvesting ETL exports, scripts, and BI report definitions; parsing view and stored-procedure definitions.
- **A search/browse entry point** — users find a starting node by name, then expand the graph from it.
- **Column-level lineage** — tracing a specific field through its transformations, not just whole tables. Common in current products and genuinely useful, with documented blind spots (transformations that obscure column mapping).
- **Edge details** — the SQL statement, job, or transformation that produced an edge, attached to the edge itself.
- **Run history on process nodes** — what ran, when, with what inputs and outputs; in some products, versioned lineage that preserves what the flow looked like at a past point in time.
- **Time windows and retention** — lineage graphs commonly support time-range filters, and lineage data is retained per the product's policy rather than forever.
- **Permission-aware visibility** — users see flows only through assets they are allowed to know about; assets they cannot access appear masked or unnamed rather than absent.
- **Programmatic access** — lineage APIs for traversal and automation, and in some platforms lineage exposed as queryable tables.
- **BI and dashboard lineage** — reports and dashboards appear as downstream consumers of tables.
- **Cross-system registration** — assets from systems outside the platform's native scope can be registered so they appear in the same graph.

### One structure, many implementations

```text
Concept:            Data-asset node
Realizations:       table/view records, file paths, topics, dashboards,
                    ML model versions, externally registered assets

Concept:            Process node
Realizations:       pipeline/job records, queries, notebooks, scripts,
                    stored procedures, BI report definitions

Concept:            Edge (evidence of a flow)
Realizations:       parsed SQL dependency, job run event (inputs → outputs),
                    platform-recorded read/write, curated manual link

Concept:            Keeping the graph current
Realizations:       query-log parsing, runtime lineage events,
                    platform-native instrumentation, code/ETL/BI harvesting,
                    manual curation
```

A reader who has only seen one implementation — say, a platform that records lineage automatically as queries execute — should still be able to recognize an open-source service that builds its graph purely from events emitted by external schedulers, or a governance tool whose stewards curate flows by hand, as the same Type.

## How It Works

A lineage platform runs three loops.

### Capture loop — building and keeping the graph

```text
Connect to / register the systems whose flows matter
→ capture evidence of flows (parse query logs, receive job events,
   record native reads/writes, harvest ETL/BI definitions)
→ resolve each flow's endpoints against known assets
   (create asset records for new ones)
→ attach the transformation detail to the edge
→ repeat on a schedule or continuously, so the graph tracks reality
```

Every capture mechanism has known blind spots — code patterns that obscure mapping, objects that get renamed, statements that never reach the log — so mature products also allow **manual lineage**: a steward draws or edits the missing links (including at column level) directly on the graph. Manual and automatic lineage coexist; automatic capture provides the scale, curation patches the gaps.

### Trace loop — the reason users open the product

```text
Find the starting node (search or browse)
→ expand the graph: upstream sources, downstream consumers
→ inspect an edge: what query/job produced this flow?
→ impact analysis: enumerate everything downstream that a change
   would affect (directly or transitively), grouped by type or owner;
   notify the affected teams
→ root-cause tracing: walk upstream from a wrong/stale result
   to the last point where the data changed
→ leave the lineage platform and act in the source system
```

The trace loop ends outside the product: lineage tells you *where* to look and *what* is affected; the fix happens in the system that owns the data.

### Maintenance loop — keeping the record trustworthy

```text
Review capture coverage (which systems, which flows are missing)
→ add manual links where automated capture cannot reach
→ reconcile the graph as assets are renamed, moved, or retired
→ use the graph's history (run records, time ranges) to answer
   "what did this flow look like when things went wrong?"
```

## Interfaces

Exact layouts and names vary by product. The following surfaces recur.

### Lineage graph canvas

The primary surface: an interactive, zoomable rendering of the flow graph.

- nodes rendered as cards (asset or process) with name, system, and summary info
- expandable in both directions; display depth commonly configurable
- highlight-one-node mode (related paths emphasized, rest dimmed)
- primary actions: expand, collapse, select a node or edge, filter by time range

### Node / asset panel

The detail view behind a node.

- asset identity, owning team, description, schema (for tables), usage signals
- for process nodes: run history, inputs and outputs, the code or query behind them
- primary actions: open the asset in its source system, jump to connected nodes

### Edge details

The evidence behind a flow.

- source and target, the SQL query or job that produced the flow, column-level mappings where supported
- primary actions: inspect the transformation, trace further

### Impact analysis pane

The change-assessment surface.

- affected items listed directly vs. all downstream, grouped by item type or by workspace/team
- affected items the viewer cannot access shown as restricted entries
- primary actions: switch scope, notify affected owners, open affected items

### Capture / administration configuration

The operator surface.

- source and connection registration, capture schedules and lookback windows, parsing options, filters, cross-system resolution settings
- primary actions: enable/disable capture per system, tune parsing, schedule runs

### Programmatic surfaces

- lineage APIs for graph traversal and automation (backfills, pipeline tooling)
- in some platforms, lineage exposed as queryable tables for SQL analysis
- increasingly, natural-language question-answering over the graph

## Important Rules / Behaviors

- **The platform describes flows; it never holds the data.** Following a lead means leaving for the source system. This boundary is structural — it is what lets one graph span an entire estate.
- **Graph currency is a maintained property, not a given.** The graph reflects the last successful capture. Systems change continuously; how promptly and how completely the graph tracks those changes varies by product and by capture mechanism.
- **Every capture mechanism has blind spots.** Vendors document them explicitly: transformations that obscure column mapping, renamed objects whose history is lost, code paths that never reach the query log. A complete graph is an aspiration; coverage claims should always be read as "captured where the mechanism can see."
- **Lineage records events, not necessarily outcomes.** Depending on the capture mechanism, the graph may show a flow that was attempted even if the surrounding transaction was later reversed — at least one platform documents exactly this behavior. Read edges as "data moved through here," and verify persistence in the source system when it matters.
- **Visibility follows permissions.** Users typically see only the parts of the graph they are entitled to; inaccessible nodes are masked or unnamed rather than hidden entirely, so the graph's shape stays honest without leaking names.
- **Manual lineage is a first-class supplement, not a fallback embarrassment.** Automated capture cannot reach everything; curated links (including column-level) are an expected part of a trustworthy graph.
- **Time matters.** Lineage answers are often time-bound — "what fed this table last Tuesday" — so mature products attach run records, time-range filters, and retention policies to the graph.

## Variants

- **Standalone dedicated platforms** — lineage is the product; positioning emphasizes the breadth of harvested systems (databases, ETL, scripts, BI) across hybrid estates, and trace/impact speed.
- **Catalog-embedded lineage** — the lineage graph ships as a capability of a Data Catalog or governance suite, usually rendered as a tab on the asset's catalog page; the catalog's discovery loop is the front door.
- **Platform-native lineage** — a data platform records lineage automatically for workloads it executes, then extends the graph outward by letting users register external upstream sources and downstream tools.
- **Event-collected OSS services** — an open lineage-event standard; jobs and schedulers emit events to a lineage server that stores and renders the graph; popular with engineering teams assembling their own stack.
- **ETL-suite-native lineage** — transformation tools render dependency views over their own jobs; a real but partial realization (one tool's flows, not the estate).
- **Audience emphasis** — engineering-first products lead with debugging and impact analysis; governance-first products lead with compliance evidence, audit trails, and sensitive-data flow.

A variant remains a variant as long as the defining core — the maintained flow graph with trace operations — is intact. If the product's primary object becomes the asset inventory (catalog), the runtime health of data (observability), or the execution of flows (ETL), it has become a neighboring Type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Data Catalog | primary object is the asset inventory + discovery/understanding loop ("what is this, what does it mean, can I trust it"); lineage is one view inside it. A catalog without lineage is still a catalog; a lineage platform without a discovery inventory is still a lineage platform |
| Metadata Management Platform | manages metadata itself as governed enterprise content (models, standards, exchange) across its lifecycle; the flow graph is one relationship structure within that content |
| Data Observability Platform | monitors the runtime health of data (freshness, volume, schema, quality tests, incidents); lineage describes the structure of flows. They interlock: lineage supplies the blast radius, observability supplies the failing node |
| ETL / ELT / Data Integration Platform | executes data movement; typically emits lineage for its own flows as a byproduct. The lineage platform's job is the cross-tool graph and its traversal, not execution |
| Data Governance Platform | organizes policy, stewardship, and compliance workflows; consumes lineage as evidence (impact before change, sensitive-data flow for audits) |
| Diagramming Application | authors free-form shapes and connectors; a lineage platform maintains a record of actual flows over identified assets, kept current by capture machinery |
| Database Management Console / SQL Client | operates one engine; its query history is one system's log. Lineage aggregates across systems into a navigable graph with resolved asset identity (query logs are one capture input, not the Type) |
| Data Warehouse / Lakehouse Platform | holds the data; lineage describes flows over data wherever it lives. Platform-native lineage is a capability of such platforms, not a separate store |

The two seams most often blurred in the market are with the **Data Catalog** (suites merge the inventory and the graph; the working distinction is the primary object of work) and with **Data Observability** (both serve debugging; the distinction is structure versus health).

## Representative Products

- Marquez — open-source lineage platform; reference implementation of the OpenLineage lineage-event standard
- Microsoft Fabric (lineage view + impact analysis) — platform-bundled, workspace-scoped lineage inside a catalog/governance surface
- OpenMetadata — unified metadata platform with lineage as a flagship capability (query-log parsing, dbt, manual curation)
- Cloudera Data Lineage (formerly Octopai) — dedicated automated-lineage product harvesting sources, ETL, scripts, and BI across hybrid estates
- Databricks Unity Catalog lineage — platform-native lineage captured automatically at query time, extended by external-asset registration

The definition was checked against older and differently-shaped realizations — ETL suites' built-in dependency views and manually curated governance flow maps — to avoid defining the Type by today's automated, cloud-era implementations.

## Sources

Research date: **2026-09-07**

- Marquez — project home: https://marquezproject.ai/ ; quickstart & data model: https://marquezproject.ai/docs/quickstart
- Microsoft Fabric — lineage view: https://learn.microsoft.com/en-us/fabric/governance/lineage ; impact analysis: https://learn.microsoft.com/en-us/fabric/governance/impact-analysis
- OpenMetadata — lineage guides: https://docs.open-metadata.org/v2.0.x/how-to-guides/data-lineage (overview, explore, workflow, column)
- Cloudera Data Lineage (formerly Octopai) — product page: https://octopai.com/ (redirects to Cloudera)
- Databricks — Unity Catalog lineage: https://docs.databricks.com/data-governance/unity-catalog/data-lineage
- OpenLineage (ecosystem context) — https://openlineage.io/

> Sourcing limitations: IBM Manta — the archetypal dedicated lineage vendor — could not be fetched from the research environment (vendor documentation returned access errors); the dedicated-vendor pole is evidenced through Cloudera Data Lineage (formerly Octopai) at product-page strength only, and no Manta-specific claims are made. Cloudera operational documentation was not fetched, so its workflow details are stated only at product-page strength. Precise vendor figures (integration counts, retention lengths, configuration defaults) are recorded in the Research Notes and intentionally not asserted as Type-level facts here.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
