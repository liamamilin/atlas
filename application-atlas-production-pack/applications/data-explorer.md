# Data Explorer

## Overview

A **Data Explorer** is an interactive application for exploring published structured data. Its content is a body of observations — indicators or data series organized along dimensions such as geography, category, and time — published and maintained by a data publisher (a statistical agency, central bank, development institution, or research organization). The application surfaces what data exists, lets the user compose a view by selecting indicators and filtering dimensions, and renders the composed selection live as tables, charts, and — where the data has geography — maps.

The defining core is small:

```text
Published structured observation data
  └── Surfacing of what data exists (catalog)
      └── View composed by selection
          └── Live rendering that re-computes as the selection changes
```

Everything else commonly associated with these tools — full-text search, chart-type switching, map views, downloads, share links, embeds, APIs, saved views — is standard capability that makes the core practical, not what makes the product a data explorer.

The defining act is **re-cutting published data live by selection**: the user never brings their own data, never models or joins it, and never writes queries. Remove that — let users import and model arbitrary data — and the product drifts toward a business intelligence or data visualization tool. Remove the live, in-app data itself and it becomes a public data portal: a catalog of files to download rather than observations to explore.

## Users & Context

The primary user is a non-specialist consumer of published data — a journalist, student, researcher, policy analyst, or interested member of the public — who wants to answer a question about what the data says without acquiring data-analysis tooling or skills.

Typical reasons to open the application:

- look up how a metric (GDP, unemployment, emissions, population, prices) has moved over time for one or a few countries or regions
- compare several entities on the same indicator
- check the level and trend of a series, with the source and units visible
- produce a chart or map to cite, share, or embed in their own writing

Secondary users include analysts who download the underlying data for further work in their own tools, and educators who use live views in teaching. There is no operator role on the consumer side: users explore a read-only published dataset. The publisher operates the data and the application out of sight of the end user.

The context is overwhelmingly the web browser. The same content is typically exposed through programmatic interfaces (APIs) for technical users and through companion surfaces such as spreadsheet add-ins or mobile apps, but the explorer itself is a web application used anonymously in most cases.

## Core Model

### The world inside a data explorer

```text
Observation data (publisher-owned)
  Indicator / series  ── has ──> dimensions (entity/geography, category, …) ── has ──> members
        │                            time (periods, from annual to intraday depending on data)
        └── observed values with units, sources, notes, update history

Catalog          — the enumeration of available indicators/series/datasets
Composed view    — indicator selection + dimension-member filters + time scope
Rendered view    — table / chart / map computed live from the composed view
Outputs          — download, share link, embed; API access to the same data
```

### Observation data

The central object is the **published observation**: a measured value of an indicator (or a point in a data series) tied to a position on each dimension — most commonly *which entity* (country, region, institution), *which category breakdown* (age group, sector, product), and *which time period*. Indicators carry metadata: definition, unit of measure, source, methodology notes, and a revision/update history. The data is structured before the user ever arrives; the user's entire experience operates on this pre-published structure. The exact organizational unit varies — one product speaks of *databases* containing *indicators*, another of *series* contributed by many *sources*, another of indicator *datasets* behind individual charts — but the underlying shape (measures × dimensions × time) is common across mature products.

### Catalog

The application must make its contents discoverable: a browsable, enumerated view of available indicators, series, or datasets, commonly organized by topic with search on top. The catalog is the bridge between "what data does this publisher have?" and "show me a view." Its richness varies — from topic trees to source/release/tag-based organization — but some surfacing of available data is constitutive; without it there is nothing to explore.

### Composed view

The user's central act is composing a view through selection:

- choose the indicator(s) or series of interest
- choose the dimension members to include (which countries or regions; which categories)
- choose the time scope (which period range; at what frequency, where data supports it)

This is selection, not querying. There is no query language, no formula entry, no schema design. The product constrains composition to what the published data actually supports — a user cannot select a breakdown the data does not contain.

### Rendered view

The composed view is rendered live:

- **table** — the exact observations selected, inspectable cell by cell
- **charts** — typically line charts by default, with bar, stacked, pie, and scatter forms commonly available and switchable without re-selecting the data
- **map** — where the data has geographic dimension, the same selection rendered as a choropleth-style map

The critical property is that these renderings are **computed from the composed selection**: change the selection and every view re-renders. The views are windows onto the same underlying observations, not static images.

### One structure, many implementations

```text
Concept:   Indicator / series selection
Forms:     country-indicator-time query panels, series pickers,
           per-indicator chart pages with configurable selections

Concept:   Entity / geography dimension
Forms:     country lists, regional hierarchies (national → subnational),
           "entities" as first-class chart concepts

Concept:   Outputs
Forms:     file downloads (CSV/Excel-style), share links to the composed view,
           embeddable widgets/frames, programmatic APIs over the same data
```

A reader who has only seen one form — say, a query-panel-style explorer — should still recognize a per-indicator chart page or a series-picker tool as the same type of application.

## How It Works

### Find what exists

```text
Open the catalog
→ browse by topic/category (or search, or browse by source/release)
→ inspect an indicator or series: title, definition, units, source, notes, last update
```

### Compose and refine a view

```text
Select indicator(s) / series
→ choose entities or geography (and category members where offered)
→ set the time range
→ the table / chart / map renders
→ adjust the selection; every view re-renders
→ switch chart form or open the map view without changing the selection
```

This compose–render–refine loop is the interaction core of the type. Mature products keep the selection editable from any open view, so the user can move fluidly between "which data" and "how it looks."

### Extract and carry away

```text
Download the selected data in a tabular format
→ or copy a share link that reproduces the composed view
→ or embed the rendered view in a page or article
→ or, for technical users, pull the same data through the publisher's API
```

Depending on the product, saving a composed view for later or producing embeds may require a free account; exploring and downloading typically do not.

### Publisher-side lifecycle (behind the scenes)

The publisher loads, revises, and extends the data on its own schedule. Users see the current published state, with update history and notes visible where the product surfaces them. Data may be revised or re-based; published series are typically accompanied by notes explaining construction and interpretation. This lifecycle is the publisher's work, invisible as an operation to the exploring user — a structural difference from tools where the user curates their own data.

## Interfaces

### Catalog / home surface

- Purpose: show what data exists and route the user to it
- Typical information: topic or category groupings, searchable indicator/series lists, featured or recently updated data, sources
- Primary actions: search, browse, open an indicator/series/dataset

### Selection / filter panel

- Purpose: compose and edit the view's selection
- Typical information: available indicators/series, entity or geography lists (often hierarchical: world → region → country → subnational region), category breakdowns, time-range controls
- Primary actions: add/remove indicators or series, select or clear dimension members, set time scope

### Table view

- Purpose: show the exact selected observations
- Typical information: rows and columns arranged by the selected dimensions (entity × indicator × period), units, notes
- Primary actions: read, re-sort/customize the layout, download

### Chart view

- Purpose: show the composed selection visually
- Typical information: the chart (line as the common default; bar, stacked, pie, scatter as common alternatives), title, units, legend, source line
- Primary actions: switch chart type, restyle, add or remove series/entities on the same chart

### Map view

- Purpose: show a geographic dimension of the selection
- Typical information: shaded regions, legend, period shown
- Primary actions: change geographic level where supported (national/subnational), change the displayed period

### Metadata / notes surface

- Purpose: let the user judge the data's provenance and meaning
- Typical information: definition, unit, source institution, methodology or interpretation notes, last-updated information
- Primary actions: read, follow links to fuller documentation

### Output / share surface

- Purpose: carry the work out of the application
- Typical information: download formats, the shareable link reproducing the current view, embed code
- Primary actions: download, copy link, embed, (with account where required) save the view

## Important Rules / Behaviors

### The data is read-only and publisher-owned

Users cannot edit observations, add their own data, or change the published structure. Everything the user does is selection and rendering over the publisher's data. This is the load-bearing rule of the type.

### The selection defines the view — always consistently

Every view (table, chart, map) reflects the same composed selection. There is no per-view data state that can silently diverge from the selection; changing the selection changes all views.

### Composition is bounded by what the data supports

The application only offers dimension members and breakdowns that exist in the published data. Selecting combinations with no observations yields empty views or explicit gaps — missing data is typically shown as a gap rather than invented or interpolated silently. Some products also cap how much of a very large selection a single table view displays.

### Provenance is part of the surface

Units, sources, and notes are user-visible first-class content, not documentation hidden behind a link. A view without its source line is considered incomplete in this type of application.

### Accounts unlock persistence, not access

Exploring is anonymous in most products. Registration, where offered, exists to save composed views, maintain lists or dashboards of them, and unlock sharing/embedding conveniences — not to gate the exploration itself.

### Updates arrive from the publisher, not the user

Users see revisions when the publisher makes them. Where revision history matters (as in economic data subject to ongoing revision), some publishers expose vintage or archival views as a distinct surface.

## Variants

- **Statistical-agency / development-institution explorer** — multi-database catalogs of country indicators with query-panel-style selection over country, indicator, and time; table, chart, and map views; download and share (e.g. World Bank DataBank, OECD Data Explorer)
- **Central-bank / time-series explorer** — series contributed by many sources; strong transform capabilities such as unit conversions (levels to changes or percent changes), frequency aggregation, and arithmetic between series on one chart; regional maps (e.g. FRED)
- **Research / media narrative explorer** — interactive charts embedded in published articles; the explorer is also shipped as an embeddable component with a documented configuration-and-data model (e.g. Our World in Data's Grapher)
- **Aggregator explorer** — one exploration surface over datasets contributed by multiple publishers (historically, Google Public Data Explorer)
- **Transform depth** — from pure selection-and-render to substantial on-the-fly derivation of new series from published ones
- **Geography depth** — country-only vs multi-level subnational mapping
- **Vintage handling** — current-values-only vs explicit historical revision views
- **Animation over time** — some products in this lineage animate the view across periods

## Related Application Types

| Application Type | Distinction |
|---|---|
| Public Data Portal | catalog of dataset *files* with metadata, licenses, and downloads; the observations are not query-able and rendered in-app. Find-then-download, not select-and-view |
| Business Intelligence Platform | organization connects and models its *own* governed data; users build curated dashboards for internal roles; includes modeling, governance, alerting. The data owner and audience differ fundamentally |
| Data Visualization Application | user imports arbitrary data and authors charts with design freedom; no published catalog, no publisher-owned structure |
| OLAP / Multidimensional Analytics Platform | shares the dimensions × measures shape but is an enterprise data-stack component with cube modeling and query engines; not a consumer-facing published-data surface |
| SQL Workbench / Ad-hoc Query Application / Database IDE | query languages over raw data stores; requires technical skill; no curated indicator semantics or catalog of published series |
| Spreadsheet Application | user owns cells and formulas over their own data; no published observations, no catalog, no rendering pipeline owned by the publisher |
| General Reference Database | also published structured content, but of reference records (textual, encyclopedic) rather than numeric observations composed into charts |
| Dashboard Platform | fixed, curated views designed by an author for repeated monitoring; the explorer's views are composed ad hoc by each user |

The two most important seams: against the **Public Data Portal** (its directory sibling), the test is whether the data itself can be re-cut and rendered inside the application; against **BI platforms**, the test is whether the data is publisher-published with selection-only composition, versus organization-internal with modeling.

## Representative Products

- World Bank — DataBank
- Federal Reserve Bank of St. Louis — FRED (FRED Graph / GeoFRED)
- Our World in Data — Grapher (the interactive chart/exploration layer of ourworldindata.org)
- OECD — Data Explorer (market context; not directly documented in this research pass)
- Google — Public Data Explorer (historical aggregator; market context)

## Sources

Research date: **2026-09-07**

- World Bank Data Help Desk — DataBank knowledge-base articles (getting started; chart types; related DataBank articles) — https://datahelpdesk.worldbank.org/knowledgebase/topics/19283-databank
- World Bank Data Help Desk — Developer Information (Indicators API, SDMX API, Metadata API) — https://datahelpdesk.worldbank.org/knowledgebase/topics/125589
- FRED Help Center — "Getting To Know FRED" and "What is FRED?" — https://fredhelp.stlouisfed.org/ , https://fredhelp.stlouisfed.org/fred/about/about-fred/what-is-fred/
- Our World in Data — Grapher technical documentation (overview, chart config) — https://docs.owid.io/projects/grapher/ , https://docs.owid.io/projects/grapher/chart-config/

> Sourcing limitation: official documentation for the OECD Data Explorer and Google Public Data Explorer could not be fetched from the research environment (access denied / JavaScript-only app / timeout). Both are included as market context only; no operational details are asserted about them, and no claims in this document rest on their internals. Precision-sensitive facts (numeric limits, exact format lists, plan gating) are stated only where directly evidenced, and remain unnumbered elsewhere.
