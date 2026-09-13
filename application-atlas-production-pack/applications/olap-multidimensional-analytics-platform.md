# OLAP / Multidimensional Analytics Platform

## Overview

An **OLAP / Multidimensional Analytics Platform** is a server-side analytical system whose defining object is the **multidimensional model — the cube**: a persistent, named model of an organization's data, organized as **dimensions** (categories, arranged in hierarchies) crossed with **measures** (the numbers being analyzed). The platform builds the cube from source data, serves it to many users and tools as the shared analytical source, and answers navigational analytical questions — drill down, roll up, slice, dice, pivot — with interactive response times.

The defining core is small:

```text
Cube (persistent multidimensional model: dimensions × measures)
└── Cube-navigation querying (drill down / roll up / slice / dice / pivot)
    └── Serving engine (stores, optimizes, and executes cube queries
        for many users and client tools)
```

Everything else the market associates with the category — precomputed storage, a dedicated query language, Excel add-ins, write-back planning, streaming ingestion, AI modeling assistants — is standard capability or variant posture, not what makes the product an OLAP platform. The category's continuity is unusually deep: an engine conceived in 1983, long-lineage independent engines, enterprise database-bundled servers, open-source big-data engines, and current cloud "semantic layer" products all realize the same three-part core, and current vendors explicitly market their products as the successors of the classic engines.

## Users & Context

Three user groups work around the same object, the cube, at different points in its life:

- **Modelers / BI developers** design and build cubes: they connect to source data, define dimensions, hierarchies, and measures, configure aggregation and storage, and deploy the cube to the server. In most organizations this is a specialized role; the cube is deliberately built once and consumed many times.
- **Business analysts and information consumers** explore cubes through client tools — spreadsheet add-ins, web grids, BI platforms — navigating along dimensions and hierarchies to answer questions like "sales by region, by quarter, drilled into one product family". They do not write queries against raw tables; they navigate a prepared model.
- **Administrators** operate the platform: processing and refreshing cubes, managing security roles, monitoring queries and jobs, tuning performance.

A fourth, important context is **finance and planning teams**: in the planning-oriented variant of this Type, analysts do not just read the cube — they write plans, budgets, and scenario assumptions back into it. The typical environment is an enterprise data stack: source systems feed a warehouse or data platform, the OLAP platform models that data multidimensionally, and client tools connect to the cube.

## Core Model

### The Cube

The cube is the system's central and persistent object. It is a named, reusable model of one business subject area — sales, finance, supply chain — held on the server and queried by many people and tools. A platform typically hosts many cubes, often sharing dimensions between them. The cube is what clients connect to; it is the analytical "single source" that keeps numbers consistent across reports and teams.

A cube is not a copy of the data in a new shape chosen per query. It is a **designed model**: someone decided which dimensions exist, how they nest, and which measures are computed. That design is the product's unit of record.

### Dimension

A dimension is a category along which data is analyzed — time, product, geography, organization, account, scenario. Dimensions provide the "perspectives" of the cube. Each dimension contains **members** (the individual values: Q1 2026, Product A, EMEA) organized into **hierarchies** — parent-child structures such as year → quarter → month → day, or region → country → city. Hierarchies are what make navigation meaningful: they define what "drill down" and "roll up" mean.

### Measure

A measure is the quantitative fact being aggregated — sales amount, units, cost, headcount. Measures are the values returned at every point of the cube. Most platforms add a **calculation layer**: calculated measures, member formulas, or rule statements that derive new numbers from existing ones (margins, variances, allocations, exchange-rate conversions). This calculation layer is a first-class part of the model, not a per-query afterthought.

### One Structure, Many Implementations

The core model is deliberately written in conceptual terms. Products realize each concept differently, and none of the realizations is definitional:

```text
Concept:            Storage of the cube
Implementations:    precomputed multidimensional storage (MOLAP),
                    relational storage with dimensional queries (ROLAP),
                    hybrid splits (HOLAP),
                    in-memory cell arrays,
                    precomputed aggregate indexes over big data,
                    elastic cloud structures

Concept:            Query language
Implementations:    dedicated multidimensional query languages (MDX family),
                    standard SQL against precomputed structures,
                    visual/grid navigation without a textual language

Concept:            Client surface
Implementations:    spreadsheet add-ins (the most widespread client),
                    web grid explorers,
                    BI-platform connectors,
                    programmatic APIs
```

A reader who has only seen one implementation — say, an in-memory planning cube or a SQL-served big-data engine — should still be able to recognize the others from the core model.

## How It Works

### Build the cube

```text
Connect to source data (warehouse, databases, files, applications)
→ design the model: choose dimensions, build hierarchies,
  define measures and calculations
→ load data and build dimensions
→ process / aggregate: prepare the structures that make
  navigation fast (mechanism varies by product)
→ deploy and secure the cube on the server
```

This is a modeling discipline, not an ad-hoc one: the cube is designed for the questions the organization will ask repeatedly. Mature products accelerate it with templates, workbook-driven design, and — increasingly — model recommendations generated from query history.

### Explore the cube

```text
Open the cube from a client tool (spreadsheet add-in, web grid, BI platform)
→ pick dimensions for rows/columns/filters and measures for values
→ read the aggregated numbers
→ drill down into a hierarchy (year → quarter → month)
→ roll up to a coarser level
→ slice (fix one member, e.g. one quarter) or dice
  (restrict several dimensions at once)
→ pivot (rotate axes to see the same numbers from another angle)
→ optionally drill through to the underlying detail records
```

This loop is the product's defining interaction. The user never leaves the model: every question is a navigation act on the cube, and the engine returns aggregated results quickly enough that exploration feels interactive.

### Maintain the cube

```text
Refresh: load new source data and re-process the cube
  (until processing completes, users see the previous state)
→ govern: manage roles and fine-grained access
  (down to individual dimension members or cells)
→ monitor: query activity, job status, performance
→ evolve: change the model as the business changes,
  reprocess, and redeploy
```

### Capability tiers

**Defining core** — without these, not an OLAP platform:

- the cube as a persistent, named, shared multidimensional model
- dimensions with hierarchies and members; measures
- navigation operations (drill down / roll up / slice / dice / pivot) as the primary query mode
- a serving engine executing cube queries for multiple users and tools

**Standard capabilities** — present in essentially all mature products:

- hierarchies with named levels as the navigation spine
- a calculation layer (calculated measures / formulas / rules)
- aggregation machinery tuned for interactive response
- client-tool integration (spreadsheet add-ins, BI connectors, APIs)
- role-based security, commonly with dimension- or cell-level granularity
- data-load and processing pipelines; administration consoles
- drill-through from aggregated cells to detail data

**Variant / optional** — depends on segment and posture:

- write-back into the cube (planning-oriented products)
- what-if / scenario sandboxes
- streaming or real-time data ingestion
- partitions and distributed cube topologies
- AI assistance (model recommendations, natural-language exploration)
- deployment shape: on-premises, cloud, database-embedded, open-source, SaaS

## Interfaces

### Cube designer / modeling surface

Where modelers work.

- Purpose: define and change the cube — dimensions, hierarchies, members, measures, calculations, storage and aggregation settings.
- Typical information: source connections, dimension structures, measure definitions, processing options.
- Primary actions: create/modify model objects, map source fields, load data, process, deploy.
- Realized variously as a dedicated design tool, a project deployed to the server, an Excel-based designer driving from workbooks, or a web modeling canvas.

### Client exploration surface (grid / pivot)

Where analysts spend their time.

- Purpose: navigate the cube and read aggregated numbers.
- Typical information: a grid or pivot of dimensions on rows/columns, filters, measure values; hierarchy expand/collapse controls.
- Primary actions: drill down / roll up, slice / dice, pivot, drill through to detail, save the view.
- The most widespread realization is inside spreadsheets via an add-in; web grid explorers and BI-platform connections are equally standard today.

### Administration console

- Purpose: operate the platform.
- Typical information: applications/cubes, jobs (loads, processing, calculations), users and roles, performance and audit logs.
- Primary actions: process/refresh cubes, manage security, run and monitor jobs, tune settings.

### Query and programmatic interfaces

- Purpose: let applications and tools query the cube.
- Typical realizations: a multidimensional query language, SQL endpoints, REST APIs. The specific language is a product decision, not a property of the Type.

## Important Rules / Behaviors

### Aggregation follows the hierarchy

Numbers roll up along the designed hierarchies. A quarter's value is the aggregation of its months; a region's value of its countries. Changing the hierarchy definition changes what every roll-up means — which is why hierarchy design is treated as a governed modeling decision, not a user preference.

### The cube is the shared source

Many users and tools query the same cube, which is the point: one definition of "sales", "margin", or "budget" served consistently everywhere. Divergent numbers usually trace back to divergent models, so organizations treat the cube as a controlled artifact with owners and change processes.

### Freshness is bounded by processing

The cube answers from its processed state. After new source data arrives, the numbers users see remain the previously processed state until a load/processing cycle completes. Products differ in how long that cycle takes and whether incremental or streaming processing narrows the gap, but the "model is refreshed, not live-by-default" behavior is structural.

### Security reaches into the data shape

Access control is not just per-cube: mature products restrict access at the dimension, member, or cell level — a user may see the cube but only their region's members, or all measures except salary-related ones. This fine granularity exists because cubes concentrate sensitive business numbers in one shared place.

### Navigation is bounded by the model

Users can only explore what the model contains. A dimension that was not designed in cannot be pivoted in later; a measure that was not defined cannot be queried. This is the deliberate trade of the Type: less per-query freedom than raw SQL, far more speed and consistency for the modeled questions.

### Drill-through reaches past aggregation

Aggregated cells summarize detail that still exists in source systems. Drill-through lets an authorized user step from an aggregated number to the underlying records — the safety valve that keeps the model from becoming an opaque black box.

### Write-back (planning variant)

In planning-oriented products, authorized users save changes directly into cube cells — budgets, forecasts, scenario assumptions — and the engine recalculates dependent results. This behavior turns the cube from a read-only analytical source into the system of record for planning numbers; it is the defining behavior of the planning variant and absent from read-oriented engines.

## Variants

- **Enterprise engine bundled with a database stack** — the OLAP server ships as part of a broader database/BI stack; cubes serve as the analytical layer for the vendor's own and third-party reporting tools.
- **Independent multidimensional engine** — a standalone server sold on its own, with deep roots in finance and performance-management estates; carries deep calculation languages and cell-level security.
- **Planning-first in-memory engine** — the cube engine packaged as the substrate of a financial-planning product; write-back and real-time calculation are the point; the planning workflow lives in the surrounding product.
- **Open-source big-data engine** — cube modeling and precomputed aggregation over large-scale data platforms, consumed through BI tools; modeling assistance from query history.
- **Cloud multidimensional semantic layer** — the current packaging: multidimensional models served elastically in the cloud, positioned explicitly as the modern replacement for the classic engines, connecting to any BI tool.
- **Tabular / in-memory semantic models** — the modern relational-shaped evolution of the same serving purpose (model once, serve fast to many tools). It trades some multidimensional structure for simplicity and is treated here as adjacent evolution; this Type's center remains the multidimensional cube.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Business Intelligence Platform | adjacent, heavily interlocking | BI centers the governed lifecycle of analytics content (authoring, repository, audiences, access control) and is model-agnostic; this Type centers the served multidimensional model itself. BI platforms have absorbed slice-drill interactions as capabilities; the persistent cube remains this Type's object. |
| Data Warehouse Platform | substrate | The warehouse stores and serves data at scale with a model-agnostic relational engine; the OLAP platform builds the multidimensional model on top of it and serves cube navigation. An OLAP server is classically the analytical tier above the warehouse. |
| Spreadsheet Application | client-side capability seam | Pivot navigation is a spreadsheet capability; this Type is the server-side model and engine that pivot clients connect to. A pivot over local data has no served shared cube. |
| SQL Workbench / Ad-hoc Query Application | adjacent | Those Types center authoring and running queries against data; here the persistent object is the model, and questions are navigations of it. A SQL interface on an OLAP engine serves the cube; it does not make the product a query editor. |
| Data Visualization Application | adjacent | Chart authoring (field-to-channel binding, finished visual artifacts) vs serving a navigable multidimensional model. Charts rendered from cube queries are client output, not this Type's object. |
| Financial Planning & Analysis Platform | straddle via the planning variant | FP&A products center the planning workflow (budget cycles, versions, approvals); this Type centers the cube model and engine such products deploy as their substrate. Write-back is the interlock capability. |
| "OLAP database" (columnar analytical DBMS) | naming overlap, different territory | The market also uses "OLAP" for columnar analytical database engines that serve fast SQL aggregation over tables with no multidimensional model. That territory belongs with data-warehouse/query-engine Types, not this leaf. |

## Representative Products

- **Microsoft SQL Server Analysis Services (multidimensional mode)** — enterprise OLAP server bundled with the database stack; cube structures with MOLAP/ROLAP/HOLAP storage; the classic anchor of the Type.
- **Oracle Essbase** — independent multidimensional engine with a long continuous release lineage (its own documentation carries migration paths from its 11g generation to the current release); block and aggregate storage, MDX, cell-level security filters, scenario sandboxes.
- **IBM Planning Analytics (TM1 engine)** — in-memory, cell-oriented OLAP database conceived in 1983, packaged as the engine of a financial-planning product; write-back and rules.
- **Apache Kylin** — open-source OLAP engine for big data; star/snowflake modeling with dimensions and measures, precomputed aggregate indexes ("cubes"), SQL-based modeling, BI-tool integration.
- **Kyvos** — cloud multidimensional semantic layer positioned explicitly as the modern replacement for the classic engines; multi-level hierarchies, slices/dices/pivots on cloud platforms.

The definition was checked against the oldest anchors (a 1983 in-memory engine; a long-lineage engine still sold today) to avoid over-fitting to any current packaging.

## Sources

Research date: **2026-09-09**

- Microsoft Learn — Multidimensional models (Analysis Services): https://learn.microsoft.com/en-us/analysis-services/multidimensional-models/multidimensional-models-ssas?view=asallproducts-allversions
- Microsoft Learn — Multidimensional Model Databases (SSAS): https://learn.microsoft.com/en-us/analysis-services/multidimensional-models/multidimensional-model-databases-ssas?view=asallproducts-allversions
- Oracle — What Is Oracle Essbase? (Essbase 21c documentation): https://docs.oracle.com/en/database/other-databases/essbase/21/essdb/what-is-oracle-essbase.html
- Apache Kylin — Overview and Model documentation (5.0.4): https://kylin.apache.org/docs/overview , https://kylin.apache.org/docs/model/intro
- IBM — What is TM1?: https://www.ibm.com/think/topics/tm1 ; IBM Planning Analytics product page: https://www.ibm.com/products/planning-analytics
- IBM — What is OLAP?: https://www.ibm.com/think/topics/olap
- Kyvos — Multidimensional Analytics: https://www.kyvosinsights.com/semantic-layer/multidimensional-analytics/ ; product home: https://www.kyvos.io/

> Sourcing limitations: IBM product documentation (ibm.com/docs) was unreachable (403) — TM1 claims are limited to IBM's official article and product page, with no precise operational details asserted. AtScale documentation was unreachable (503, abandoned) — the modern semantic-layer pole rests on Kyvos's official product pages (positioning-level evidence). Deeper SSAS, Essbase outline, and Kylin security pages were not fetched; no claims are made beyond the fetched pages. Precise vendor limits, storage internals, and performance figures are intentionally not stated in this document; they remain in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical market-sample check are recorded in the paired Research Notes.
