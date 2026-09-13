# Research Notes — Data Explorer

Research date: 2026-09-07
Leaf: Data Explorer (DIRECTORY.md §02.12 Data Exploration; sibling leaf: Public Data Portal)
Slug: data-explorer

---

## Research Goal

Understand what a Data Explorer (as an Application Type under "Content, Knowledge & Information") really is, by studying real products that let users explore published structured data interactively:

> What objects make up this type of application's world, what does the user actually do, what interfaces recur, what rules matter, and where are the boundaries against Public Data Portal, Business Intelligence, Data Visualization, and OLAP types?

The directory placement is itself a strong signal: Data Explorer sits in **02 Content, Knowledge & Information**, NOT in **13 Data, Analytics & AI Systems**. The intended referent is therefore the *published-data* explorer (statistical agencies, central banks, research/media organizations, aggregators) — not enterprise BI "explore" surfaces, SQL clients, or database consoles, which belong to §13 types.

## Initial Boundary

Working hypothesis at start:

- A Data Explorer is an interactive application for exploring pre-published structured data: the user selects indicators/series and filters dimensions (geography, time, category), and the application renders the result as tables, charts, and maps computed live from the data.
- Nearest neighbors: Public Data Portal (catalog + file distribution), Business Intelligence Platform (org-internal governed data), Data Visualization Application (user brings data, designs charts), OLAP platform (enterprise multidimensional analysis), SQL Workbench / Ad-hoc Query (query languages over raw databases).
- Potential confusion: the product name "Data Explorer" is used by several enterprise analytics and database tools (an "explore" surface in BI tools, database consoles). This is a naming collision to record, not a second referent of this leaf.

## Research Questions

1. What are the core objects? (dataset / database / indicator / series / dimension / dimension member / observation / view)
2. How does a user compose a view — what is the canonical interaction loop?
3. What renderings are standard (table, chart forms, map)? Which are conditional?
4. What outputs exist (download, share links, embed, API)?
5. What metadata is user-visible (source, unit, notes, last update)?
6. What role do accounts play (save, share, embed)?
7. What publisher-side behavior matters (data updates, revisions, releases)?
8. Where are the boundaries vs the neighboring types listed above?
9. What varies: publisher posture (statistical agency vs central bank vs research/media vs aggregator), back end (SDMX warehouse vs relational indicator store vs flat files), transform depth (unit/frequency transformations, series arithmetic), map depth, accounts?

## Representative Products

Selected for market representativeness + documentation completeness + different product philosophies + different operator tiers:

| # | Product | Operator type | Philosophy pole | Evidence tier reached |
|---|---|---|---|---|
| A | World Bank DataBank | Development bank / statistical publisher | Query-builder: select Countries × Indicators × Time, then view Table/Chart/Map | Tier 1 — Data Help Desk KB articles fetched |
| B | FRED (FRED Graph, GeoFRED) | US central bank (Federal Reserve Bank of St. Louis) | Series-centric time-series explorer with transforms | Tier 1 — FRED Help Center fetched |
| C | Our World in Data Grapher | Research/media organization | Client-side chart explorer embedded in narrative pages; open config+data model | Tier 1 — official Grapher technical docs fetched |
| D | OECD Data Explorer | Intergovernmental statistical agency | SDMX-grade statistical explorer (literal archetype of the type name) | Market context only — product page 403, app root is a JS shell (2 attempts each, abandoned) |
| E | Google Public Data Explorer | Aggregator platform (historical) | Multi-publisher dataset directory + exploration (motion-chart heritage) | Historical context only — fetch timed out (1 attempt, abandoned) |

## Sources

Fetched 2026-09-07:

- World Bank Data Help Desk — Knowledge Base topic "DataBank" (13 articles list): https://datahelpdesk.worldbank.org/knowledgebase/topics/19283-databank
  - "How do I start in DataBank?": https://datahelpdesk.worldbank.org/knowledgebase/articles/193416-how-do-i-start-in-databank
  - "How do I choose the type of Chart for visualizing my data in DataBank?": https://datahelpdesk.worldbank.org/knowledgebase/articles/193427-how-do-i-choose-the-type-of-chart-for-visualizing
- World Bank Data Help Desk — Developer Information topic (Indicators API, SDMX API, Metadata API): https://datahelpdesk.worldbank.org/knowledgebase/topics/125589
- FRED Help Center — "Getting To Know FRED" hub + "What is FRED?" article: https://fredhelp.stlouisfed.org/ , https://fredhelp.stlouisfed.org/fred/about/about-fred/what-is-fred/
- OWID documentation — Grapher project docs (home, chart config): https://docs.owid.io/ , https://docs.owid.io/projects/grapher/ , https://docs.owid.io/projects/grapher/chart-config/
- OECD Data Explorer: https://www.oecd.org/en/data/tools/oecd-data-explorer.html (403), https://data-explorer.oecd.org/ (JS shell) — **unreachable**
- .Stat Suite community docs (sis-cc.gitlab.io): 403 — **unreachable**
- Google Public Data Explorer: https://www.google.com/publicdata/directory — **timed out**

Source-access limitation: the SDMX-grade statistical pole (OECD) and the historical aggregator pole (Google PDE) could not be directly documented from the research environment. All claims about those products in these notes and in the final document are accordingly hedged as market context; no precise operational details are asserted for them.

---

## Product A — World Bank DataBank

### Key observations (evidence layer A — directly observed)

From the Data Help Desk DataBank articles:

- **Access model**: usable as an unregistered user (generate customized reports; view tables, charts and maps; download data) or registered user (additionally: save the data selection in the system, render it at any point in time, share tables/charts/maps with other users, embed data visualizations directly into blogs or websites).
- **Entry**: a "Databases" tab on the left side; user selects from a list of databases (e.g., WDI and others).
- **Canonical selection axes**: "Select from Countries, Indicators and Time" — three selection variables. This is the product's own articulation of the multidimensional shape of published statistical data.
- **Views**: Table, Chart, Map (open one; edit the country/series/year selection while a table/chart/map is open).
- **Chart mechanics**: default chart type is a line chart; options include vertical/horizontal bar chart, stacked area chart, vertical/horizontal stacked bar chart, pie chart; changed via a "Chart options" tab → "Chart Type & Style" → dropdown → "Apply Changes".
- **Metadata**: user can view country and indicator notes/metadata inside the tool.
- **Selection management**: edit the list of countries/indicators/years selected; view all data selected; a separate FAQ ("Why doesn't the Table show all of the data I have selected") evidences that table views have display-capacity constraints; table can be customized.
- **Outputs**: download data; share table/chart/map on social media; save reports (registered); embed visualizations (registered).
- **Behind it**: World Bank publishes Indicators API (V2), Metadata API, and SDMX API — the same data the explorer shows is programmatically accessible.

## Product B — FRED (Federal Reserve Economic Data, St. Louis Fed)

### Key observations (evidence layer A — directly observed)

From the FRED Help Center ("What is FRED?" and hub structure):

- **What it is**: "an online database consisting of hundreds of thousands of economic data time series from scores of national, international, public, and private sources" — combined with "tools that help the user understand, interact with, display, and disseminate the data."
- **Discovery surfaces**: homepage search; browse by (1) source, (2) release, (3) category, (4) latest update, (5) tags. Release calendar exists. Organization-by-tags described as the flexible cataloging structure.
- **FRED Graph**: most popular view is a line chart; user can "completely customize the aesthetic" (fonts, colors, line weights); also pie, bar, scatter plot forms.
- **Multi-series + arithmetic**: multiple series can be interacted with on a single chart; series can be subtracted from one another (documented example: yield spread = bond rate − Treasury rate).
- **Unit transformations**: levels → change, percent change, compounded annual rate of change, "among the many selections available" (documented example: real GDP in billions of chained dollars → percent change from a year ago).
- **Frequency aggregation**: aggregate a series from higher to lower frequency (documented example: monthly → annual) to align series of different frequencies.
- **Maps (GeoFRED)**: view data at state, MSA, and county level; help center has dedicated "Maps" section (find / customize / share a FRED map).
- **Notes/metadata**: "many series in FRED contain notes that help the user understand or interpret the data" — sometimes off-site links, sometimes full construction/interpretation explanations.
- **Outputs**: download data (Excel format since 2006); share my FRED graph; share my FRED map; FRED API (released 2009); Excel add-in; mobile apps; wrappers for R/STATA/MatLAB/RATS/EViews.
- **Account**: FRED Account section — what you can do with an account; FRED Dashboards; Published Data Lists (2007: "allowing users to post created groupings of data").
- **History/structure**: FRED Graph + Excel download + unit transformations introduced 2006; frequency aggregation 2010. Sibling product ALFRED (2006) serves vintage data (all revisions of a series) — FRED always shows the most recent revision.
- **Help-center structure**: Data / Graphs / Maps / Account / FAQ sections — mapping exactly to the app's major surfaces.

## Product C — Our World in Data Grapher

### Key observations (evidence layer A — directly observed)

From official Grapher technical documentation (docs.owid.io):

- **What it is**: "Our World in Data's client-side data exploration and visualization library — the code behind every interactive chart on ourworldindata.org", available as an npm package (private registry, proprietary license).
- **Core model, in the vendor's own words**: "A chart is a JSON **config** (title, chart type, selected entities, …) plus the tabular **data** it renders, which Grapher can ingest from an in-memory table, a CSV, or OWID's data API."
- **Config fields commonly used**: `title`, `subtitle`, `note`, `chartTypes` (example `["LineChart"]`), `tab`, `hasMapTab`, `selectedEntityNames` (example `["France", "Germany"]`).
- **Data shape**: tabular data with typed, metadata-carrying columns (`OwidColumnDef`, `ColumnTypeNames` — example column def: slug `gdpPerCapita`, type `Numeric`, name "GDP per capita"); entity is a first-class concept (entities selected by name).
- **Views implied by config**: chart types list + map tab flag + active `tab` — i.e., chart / table / map tab machinery.
- **Embedding/position**: the explorer is the embeddable interactive layer of a publication; charts live inside narrative articles on the public site.
- **API**: data API + in-memory/CSV ingestion; full JSON schema published (`grapher-schema.011.json`) with browsable field-by-field reference.

## Product D — OECD Data Explorer (market context only)

No direct fetch succeeded (product page 403; app root requires JavaScript). Known market context, intentionally NOT used for precise claims:

- It is a literal namesake of the type and the flagship explorer of a major intergovernmental statistical agency; the agency's published-data architecture is SDMX-oriented (statistical data and metadata exchange). Claims about its internals remain unverified in this pass.

## Product E — Google Public Data Explorer (historical context only)

Fetch timed out. Known market context, NOT used for precise claims:

- Historically a hosted directory of datasets from multiple publishers (World Bank, OECD, etc.) with interactive exploration and motion-chart-style animation; important as (a) an aggregator-pole data point and (b) a §24-style historical sample from ~2010.

---

## Cross-product Comparison

| Structure | A: DataBank | B: FRED | C: OWID Grapher |
|---|---|---|---|
| Published structured data as content | yes — multiple databases of country indicators | yes — economic time series from many sources | yes — indicator datasets behind each chart (tabular data + column metadata) |
| Catalog / discovery of available data | Databases tab + indicator/country lists | search + browse by source/release/category/last-update/tags | site-level indicator pages (publication surface); explorer renders a given dataset |
| Selection = indicator/series + entity/geography + time | Countries × Indicators × Time (product's own framing) | series selection; date range; geography via GeoFRED maps | selectedEntityNames; indicator dimensions in config |
| Live re-render on selection change | yes — edit selection while table/chart/map open | yes — add/remove series, change transforms, chart re-renders | yes — client-side rendering from config+data |
| Table view | yes (Table view; customizable; capacity-limited) | tabular download; Excel add-in (table surface) | tabs machinery incl. table (config `tab`) |
| Chart types + switching | line (default), bar V/H, stacked area, stacked bar V/H, pie | line primary; pie/bar/scatter; aesthetic customization | chartTypes list (e.g., LineChart); map tab |
| Map view | yes (Map view) | yes (GeoFRED: state/MSA/county) | yes (hasMapTab) — conditional on geography |
| Derived transforms (unit change, % change, frequency aggregation, series arithmetic) | not directly evidenced | yes — unit transformations, frequency aggregation, multi-series arithmetic | not user-evidenced (client-side table transforms internal) |
| User-visible metadata/notes | country and indicator notes/metadata | series notes (construction/interpretation, off-site links) | title/subtitle/note; typed column metadata; published JSON schema |
| Download/export | yes (download data) | yes (download, Excel) | (public site exports — not evidenced in fetched docs; not asserted) |
| Share / embed | share table/chart/map; embed into blogs/websites (registered) | share graph; share map | charts embedded across narrative articles (the site's primary mode) |
| Save / account artifacts | save selections; render later (registered) | account: saved graphs, dashboards, data lists | not evidenced as user account feature |
| Programmatic access to same data | Indicators API, Metadata API, SDMX API | FRED API, Excel add-in, R/STATA/MatLAB wrappers | data API; Grapher library ingestion (CSV/API/in-memory) |
| Anonymous use fully functional | yes (view/download; save/share/embed gated) | yes (browsing/graphing; account adds save/share artifacts) | yes (public pages) |

### Reading of the comparison

- The **selection model** differs in surface form (three-axis query builder vs series picker vs config-driven entity selection) but is the same conceptual act: choose measures + choose members of other dimensions + choose time scope.
- **Table / chart / map** recur as the view triad; maps exist only where the data has geography (conditional capability).
- **Outputs** (download, share link, embed) and **programmatic access to the same data** recur across all three.
- **Accounts** are consistently an *enhancement* (save/share/embed), never a prerequisite for exploring.
- **Derived transforms** (unit change, % change, frequency aggregation, arithmetic between series) are strong in the time-series pole (FRED) but not evidenced across the sample → common variant, not core.
- Metadata visibility (notes, sources, units) recurs in all three.

---

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately minimal)

A Data Explorer is recognizable by exactly this structure:

```text
Published structured observation data
  (indicators/series × dimensions [entity/geography/category] × time)
  └── Surfacing of what data exists (catalog-like enumeration)
      └── View composition by selection
          (pick indicators/series + dimension members + time scope)
          └── Live computed rendering of the composed selection
              (table and/or chart; the view re-renders when the selection changes)
```

Four invariants. Remove any one and the type collapses:

1. **Published structured observation data as the content** — the data is owned and structured by the publisher into measures/indicators and dimensions; the user never brings their own data and never models it. Without this it is a visualization tool or spreadsheet.
2. **Surfacing of what data exists** — the application presents its available indicators/series/datasets so the user can select from them. Without this there is nothing to explore (only pre-made charts).
3. **View composition by selection** — the user composes the view through selections (indicators, entities/geography, time), not through query languages, code, or data modeling. Without this it is a query tool / SQL workbench.
4. **Live computed rendering** — the composed selection determines what is rendered, and changing the selection re-renders (table and/or chart). Without this it is a static statistical publication / chart gallery.

Deliberately NOT in L0 (tested against §24-style historical/edge samples):

- **Search** — early/legacy statistical browsers (table-first, hierarchical browse only) and single-dataset tools (e.g., a Gapminder-style tool preloaded with one dataset) still qualify. Enumeration ≠ full-text search.
- **Maps** — some explorers hold no geographic data; early national statistical browsers were table-only. Map is conditional on data having geography.
- **Charts** — a table-only re-cuttable view would still be an explorer (the "live re-cut" is the invariant, not the chart form). In practice all sampled modern products offer charts; a table-only explorer would be recognized as a legacy form of the same type.
- **Download / share / embed / API** — present in every sampled product, but an explorer without exports is still an explorer.
- **Accounts** — DataBank and FRED both fully explore anonymously.
- **Transforms** (unit change, % change, frequency aggregation, arithmetic) — FRED-only strength in this sample.
- **Multi-publisher aggregation** — DataBank/FRED/OWID are single-publisher.

### L1 — Common Mature Structure (cross-product, layer B)

Present in all/most sampled mature products:

- searchable catalog with topical organization (categories/tags/topics) and freshness cues (latest updates, release calendar)
- multiple chart forms with switching (line, bar, stacked forms, pie/scatter; DataBank: apply-changes cycle; FRED: aesthetic customization; OWID: chartTypes list)
- table view of the composed selection (DataBank explicit; FRED via download/add-in; OWID via tab machinery)
- map view where data has geography (all three, each explicitly)
- metadata visibility: source, unit, definitions/notes, data notes/interpretation
- download of data (CSV/Excel-style), share links / permalinks to composed views, embedding
- programmatic access to the same data (APIs of various grades)
- optional account unlocking saved views/lists/dashboards and sharing/embedding of artifacts
- multi-series / multi-entity comparison on one chart

### L2 — Variant / Optional Structure

- **Derived transforms on the composed view**: unit conversions (levels → change / percent change / compounded annual rate), frequency aggregation (higher→lower), arithmetic between series (spreads). Strongly evidenced only in the time-series pole (FRED).
- **Data revision/vintage handling**: latest-revision display vs historical vintages (FRED vs ALFRED as separate sibling product).
- **Publisher posture**: single-publisher statistical explorer (DataBank, OECD-style), central-bank time-series explorer (FRED), research/media narrative explorer (OWID — charts embedded in articles, open config schema), multi-publisher aggregator (Google PDE historically).
- **Back end**: SDMX-grade statistical warehouse vs relational indicator store vs flat files/CSV ingestion (OWID).
- **Embeddability of the engine itself**: OWID ships the explorer as a library/package others can configure; other products embed only finished views.
- **Animation over time / motion charts** (Gapminder/Google PDE heritage) — market-known, not directly evidenced in this pass → hedge as "some products".
- **Projections/forecast series** included alongside observations (market-known in some statistical explorers) — not evidenced here → variant, hedged.
- **Subnational geography depth** (state/MSA/county — FRED) vs country-only.
- **Paywalls/registration** for premium tiers (adjacent subscription statistics platforms) — outside the sampled free-public-data products.

### L3 — Vendor-specific (research notes only; never canonical)

- DataBank: three-tab "Countries / Indicators / Time" selection UI; "Chart options → Chart Type & Style → Apply Changes" flow; databank.worldbank.org home.aspx shell; 13-article KB; registered-user save/share/embed framing.
- FRED: GeoFRED branding; ALFRED sibling (vintages); Published Data Lists; FRED Dashboards; release calendar; digital badges; Excel add-in; mobile apps; "over two million persons per year" scale claim; waffle-menu sibling apps (FRASER, CASSIDI).
- OWID Grapher: `GrapherInterface` config schema ($schema, dimensions requiredness rules); GrapherLoader.fromCsv/fromApi/fromTable; OwidTable; ColumnTypeNames/DimensionProperty enums; grapher-schema.011.json; private npm registry; slug-based chart pages; CC BY 4.0 docs.
- OECD: SDMX structures, .Stat Suite heritage — unverified in this pass.
- Google PDE: publisher dataset upload machinery, motion-chart lineage — unverified in this pass.

---

## Vendor-specific Findings (summary)

- Account-gated embed is DataBank's specific framing; FRED gates only saving artifacts; OWID has no account layer at all. → "saving/sharing may require an account" is cross-product; "embed requires registration" is product-specific.
- Series arithmetic (spread construction) is FRED-documented; do not generalize to the type.
- Frequency aggregation as a user-facing operation is FRED-documented; do not generalize.
- Table display-capacity limits exist (DataBank FAQ) but magnitudes are unknown → phrase as "some products cap how much of a large selection a table displays."

## Boundary Findings

| Neighbor type | Seam | Test |
|---|---|---|
| **Public Data Portal** (sibling leaf) | Portal = catalog of dataset *files* + metadata + license + download for external use. Explorer = the observations themselves are query-able and rendered in-app. | Remove live view composition/rendering → it becomes a portal (find → download). Add a CKAN-style file-catalog to an explorer and it's still an explorer with a catalog. |
| **Business Intelligence Platform / Dashboard Platform** (§13) | BI: organization connects and models its OWN governed data; curated dashboards for internal roles; monitoring/alerts; permissions stack. Explorer: publisher-curated published data; user composes single views within the publisher's model; no modeling, no governance stack. | Remove published-data posture + selection-only composition (allow modeling/joining arbitrary sources) → BI. The audience and data ownership are the sharpest seams. |
| **Data Visualization Application** | Viz app: user imports arbitrary data and designs charts (data ownership + design freedom). Explorer: data fixed by publisher; user selects within a published structure. | Let users bring their own data and author free-form charts → viz app. |
| **OLAP / Multidimensional Analytics Platform** (§13) | Shares the dimensions × measures shape, but OLAP is an enterprise data-stack component (cube modeling, write-back of models, query engines like MDX). Explorer is consumer-facing and read-only over published data. | Move it into the data stack with cube design + enterprise roles → OLAP. |
| **SQL Workbench / Ad-hoc Query Application / Database IDE** (§13) | Those query raw stores with query languages; the explorer exposes curated indicator/series semantics through selection UIs. | Require a query language → different type. |
| **Spreadsheet Application** | Spreadsheet: user owns cells and formulas. Explorer: publisher owns observations; user only composes selections. | Give users editable cells/formulas → spreadsheet. |
| **General Reference Database** (02.05) | Published structured content too, but records are text/reference objects, not numeric observation sets composed into charts. | Numeric observations + composed views vs reference records + lookup. |

Naming-collision note: several enterprise products name internal surfaces "Data Explorer" (BI explore modes, database consoles, storage browsers). Those belong to §13 types. The §02.12 leaf is documented as the published-data explorer per directory placement. Recorded in STATUS.md as a boundary issue.

Historical/market-sample check (per §24): early national statistical browsers (table-first, browse-only), Gapminder-style single-dataset tools (no search), Google PDE (~2010 aggregator with animation), FRED pre-2006 (data distribution without the graph/transform tooling — which reads as a *data service*, not an explorer). All fit the minimal L0 except pre-2006 FRED, correctly reading as "database without explorer" — confirming that live composed views (not the database alone) are the type's defining act.

## Uncertainties

1. OECD Data Explorer — no direct evidence this pass (403/JS-shell). Its exact catalog/view mechanics unverified; only market-context status asserted.
2. Google Public Data Explorer — no direct evidence (timeout); historical posture inferred from general market knowledge, explicitly hedged.
3. Whether "table-only explorer" exists in the current market — argued from L0 minimalism + legacy browsers, not from a fetched current product.
4. OWID public-site export/download buttons — not evidenced in fetched docs; not asserted in the final document.
5. Precise display-capacity limits, dataset counts, series counts — deliberately unnumbered (evidence rule).
6. Whether animation-over-time is currently common — not evidenced in this sample; left as hedged variant.

## Final Synthesis

A Data Explorer is an application operated by (or on behalf of) a data publisher, whose content is a body of published structured observations — indicators/series organized along dimensions such as entity/geography, category, and time. The application surfaces what data exists, lets users compose views by selecting indicators and filtering dimensions (no query language, no data modeling), and renders the composed selection live as tables, charts, and — where the data has geography — maps. Mature products add searchable catalogs with freshness cues, chart-form switching with styling, user-visible metadata (source, units, notes), download and share/embed outputs, programmatic access to the same data, and optional accounts that unlock saved views and shared artifacts. Some products add derived transforms (unit change, percent change, frequency aggregation, arithmetic between series); these are variant capabilities, strongest in time-series explorers.

The type's defining act is **re-cutting published data live by selection**. Remove the publisher-owned structured data and it becomes a visualization tool; remove selection-based composition and it becomes a query tool; remove live re-rendering and it becomes a statistical publication; remove the in-app data and it becomes a public data portal.
