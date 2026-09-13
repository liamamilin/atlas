# Research Notes — OLAP / Multidimensional Analytics Platform

## Research Goal

Understand what an OLAP / Multidimensional Analytics Platform actually is as an Application Type: what its defining object is, how cubes are built and served, how users query them, which structures are definitional vs common vs variant, and where the boundary lies with BI platforms, data warehouses, spreadsheets, and the overloaded "OLAP database" usage of the term.

This pass also discharges three pre-hung flags from sibling passes:
- business-intelligence-platform (processed): "OLAP seam = cube/multidimensional model as defining object vs model-agnostic consumption lifecycle (BI has absorbed OLAP-style slice-drill interactions)"
- data-visualization-application (processed): "OLAP = cube/multidimensional model as the defining object vs model-agnostic chart authoring — light flag for the OLAP pass"
- lakehouse-platform (processed): "vs olap-multidimensional-analytics-platform (no multidimensional-modeling semantics observed in the lakehouse population)"

## Initial Boundary

Initial hypothesis (to be tested, not asserted):

- Core purpose: a server-side analytical system whose defining object is the **multidimensional model (cube)** — dimensions with hierarchies × measures — which it builds from the organization's data, serves to many users/tools, and answers navigational analytical queries against (slice, dice, drill down/up, roll up, pivot) with interactive response times.
- Likely users: BI/OLAP developers and modelers (build cubes), business analysts and finance users (consume via Excel/BI clients), administrators (process, secure, monitor).
- Nearest neighbors: Business Intelligence Platform, Data Warehouse Platform, Spreadsheet Application (pivot), SQL Workbench / Ad-hoc Query Application, Financial Planning & Analysis Platform (write-back planning on OLAP engines), and the "OLAP database" sense of the word (columnar analytical DBMS — a different territory).
- Known unknowns: whether preaggregation is definitional; whether write-back is definitional; whether MDX is definitional; how tabular/semantic-model evolution relates; whether the "OLAP" term overload creates a taxonomy problem.

## Research Questions

1. What objects constitute the cube model (dimension, hierarchy, level, member, measure, calculated measure)?
2. How is a cube built and maintained (source → modeling → load → aggregation/processing → serve)?
3. How is a cube queried and navigated (query languages; slice/dice/drill/roll-up/pivot operations)?
4. Which storage architectures exist (MOLAP / ROLAP / HOLAP / in-memory / precompute / cloud elastic) — invariant or variant?
5. What security model do these platforms expose (roles, dimension/cell-level security)?
6. Is write-back (planning) definitional or a variant?
7. How do client tools (Excel, BI tools, web grids) consume cubes?
8. How does the modern evolution (tabular semantic models, semantic layers on cloud platforms) relate to this Type?
9. Historical check: do 1980s/1990s-generation products fit the same definition?
10. Boundary: vs BI platform, warehouse, spreadsheet pivot, "OLAP database" (columnar DBMS) sense, FP&A platform.

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, different eras, and different customer tiers:

1. **Microsoft SQL Server Analysis Services (SSAS), multidimensional mode** — the canonical enterprise OLAP server bundled with the SQL Server stack; multidimensional + tabular server modes; MOLAP/ROLAP/HOLAP storage. (Enterprise DB-bundled pole.)
2. **Oracle Essbase** — independent multidimensional engine with financial/EPM heritage and a long continuous release lineage (its own docs carry 11g→21c migration paths); block storage + aggregate storage engines; MDX; cell-level filters. (Independent-engine pole + historical anchor.)
3. **IBM Planning Analytics (TM1 engine)** — in-memory, cell-oriented OLAP database invented 1983, repositioned as the engine of an FP&A product; write-back; rules. (Planning-first in-memory pole + oldest anchor.)
4. **Apache Kylin** — open-source OLAP engine for big data, created at eBay 2014, Apache top-level project 2015; precomputation-centric; SQL interface; star/snowflake modeling. (Open-source big-data pole + modern-era precompute philosophy.)
5. **Kyvos** — cloud "semantic layer" product that explicitly positions its multidimensional semantic data models as the modern replacement for SSAS/Essbase/TM1/Azure AS; slices/dices/pivots on cloud platforms. (Modern cloud semantic-layer pole — evidence that the market itself treats "multidimensional analytics" as the continuation of OLAP.)

Rejected/considered: AtScale (docs 503 ×2, abandoned per network rule); Mondrian/Pentaho (docs site defunct — redirects to Pentaho homepage); Power BI (BI platform Type; its tabular engine is SSAS-lineage — noted as evolution, not sampled as an OLAP platform).

## Sources

Fetched 2026-09-09:

- Microsoft Learn — "Multidimensional models" (Analysis Services): https://learn.microsoft.com/en-us/analysis-services/multidimensional-models/multidimensional-models-ssas?view=asallproducts-allversions
- Microsoft Learn — "Multidimensional Model Databases (SSAS)": https://learn.microsoft.com/en-us/analysis-services/multidimensional-models/multidimensional-model-databases-ssas?view=asallproducts-allversions
- Oracle Docs — Oracle Essbase 21c "What Is Oracle Essbase?": https://docs.oracle.com/en/database/other-databases/essbase/21/essdb/what-is-oracle-essbase.html (reached via 21c Get Started index: https://docs.oracle.com/en/database/other-databases/essbase/21/index.html)
- Apache Kylin — Overview (5.0.4): https://kylin.apache.org/docs/overview ; Model introduction: https://kylin.apache.org/docs/model/intro ; product home: https://kylin.apache.org/
- IBM Think — "What is TM1?": https://www.ibm.com/think/topics/tm1 ; IBM Planning Analytics product page: https://www.ibm.com/products/planning-analytics
- IBM Think — "What is OLAP?": https://www.ibm.com/think/topics/olap (official IBM educational article; used for canonical concept vocabulary: cube, drill-down, roll-up, slice, dice, pivot, MOLAP/ROLAP/HOLAP, OLAP vs OLTP)
- Kyvos — home: https://www.kyvos.io/ ; "Multidimensional Analytics" page: https://www.kyvosinsights.com/semantic-layer/multidimensional-analytics/

Unreachable / abandoned (recorded per source-access limitation rules):

- IBM product documentation (ibm.com/docs) — 403 ×2 (both /planning-analytics paths). TM1 operational detail limited to IBM's think article + product page; no precise TM1 operational claims made.
- AtScale docs (docs.atscale.com) — 503 ×2, abandoned. No AtScale claims made anywhere.
- Mondrian docs (mondrian.pentaho.org) — redirects to Pentaho marketing homepage; open-source ROLAP pole not directly evidenced. ROLAP storage mode instead evidenced via SSAS docs and IBM's OLAP article.
- SSAS deeper pages (cube architecture, dimensions, MDX fundamentals) — guessed slugs 404 ×2; SSAS claims limited to the two fetched pages.
- Essbase outline/dimension deep-dive pages — not fetched; outline terminology used only as observed on the fetched page ("rich outline editor", "hierarchically organized cubes").

## Product A — Microsoft SQL Server Analysis Services (multidimensional mode)

Evidence layer: A (directly observed, Microsoft Learn, 2 pages).

Key observations:

- "An Analysis Services multidimensional solution uses **cube structures** for analyzing business data across multiple dimensions. Multidimensional mode is the default server mode of Analysis Services. It includes a **query and calculation engine for OLAP data**, with **MOLAP, ROLAP, and HOLAP storage modes** to balance performance with scalable data requirements."
- "The Analysis Services OLAP engine is an industry-leading OLAP server that works well with a broad range of BI tools. Most Analysis Services deployments are installed as classic OLAP servers."
- Purpose framing: "The primary reason for building an Analysis Services multidimensional model is to achieve **fast query performance** against business data. A multidimensional model is composed of **cubes and dimensions** that can be annotated and extended to support complex query constructions. BI developers create cubes to support fast response times, and to provide a **single data source for business reporting**."
- "having a single source of analytical data ensures that discrepancies are kept to a minimum" — the cube as the shared analytical source.
- Client integration: "integration with commonly used BI reporting tools such as Excel, Reporting Services ... as well as custom applications and third-party solutions."
- Database composition: "An SQL Server Analysis Services database is a collection of **data sources, data source views, cubes, dimensions, and roles**."
- "Cubes are the **fundamental query objects** in Analysis Services. When you connect to an Analysis Services database via a client application, you **connect to a cube** within that database. A database might contain multiple cubes if you are reusing dimensions, assemblies, roles ... across multiple contexts."
- Authoring/administration surfaces: SQL Server Data Tools (projects, deployment) for creation; SQL Server Management Studio for administration (partitions, roles); source-control integration for team development.
- Note: SSAS also has a separate "tabular" mode (the docs treat multidimensional and tabular as distinct solution types); tabular is the modern in-memory semantic-model line (used by Power BI) — recorded as evolution, not as this leaf's center.

## Product B — Oracle Essbase

Evidence layer: A (directly observed, Oracle docs, "What Is Oracle Essbase?" + 21c index).

Key observations:

- Positioning: "Oracle Essbase is a business analytics solution ... for analysis, reporting, and collaboration ... for your business users, analysts, modelers, and decision-makers."
- "from **multi-dimensional analysis** to complex procedural business logic applied to your data. You can easily create and share **on-the-fly transient models** or deliver **enterprise-wide long-established databases**."
- Cube lifecycle breadth: "A **gallery of cube templates** helps you get started"; "Create and manage Essbase applications from Microsoft Excel using **Cube Designer**"; "Cube Designer infers patterns found in unstructured workbooks, to help you shape raw data into **hierarchically organized cubes**."
- Query engine: "**Hybrid mode** is the default query engine for **block storage cubes**, providing robust dependency analysis and **fast aggregation**." Two storage engines exist: block storage cubes and **aggregate storage** ("Aggregate Storage Calculation ... automate the creation and maintenance of default aggregate views").
- Query language: "**MDX**'s well-known utility as a **multidimensional query language**"; "Query, Insert, and Export Essbase Data with MDX"; "you can use its Insert and Export directives to shape, copy, move, and update any custom **slice of multidimensional data**."
- Exploration surfaces: "Using **Smart View**, you can interact with Essbase in Microsoft Excel to query and analyze data"; "You can perform **ad hoc data queries/grid analyses** on cube data from the administrative Essbase web interface ... save your grid layouts, run report scripts, and run and save named MDX queries."
- Data intake: "Data Load and Dimension Build — ... load rules editor ... import of data and dimension from the Catalog or from outside sources"; "flat-file, Excel-based, and SQL-based import and export"; "Create connections and Datasources for **drill through**, data loads, and dimension builds."
- Drill-through: "When you need more data than what you can see in the Essbase cube, you can use **drill through reports** to access external data sources."
- Security: "There are three Essbase user roles: User, Power User, and Service Administrator. Application permissions ... Application Manager, Database Manager, Database Update, and Database Access." "**Essbase filters** help you implement fine-tuned, **cell-level access controls** to your cubes."
- Planning-flavored capabilities: "**Scenario Management** — ... private work areas or 'sandboxes' in which users can model different assumptions ... without affecting the cube"; "Perform What-if Analysis"; "Forecasting and Allocation — top-down and bottom-up forecasting and allocations."
- Calculation: "rich library of calculation functions"; "Calculation tracing"; member formulas; "custom defined functions and macros built using Java."
- Distribution: "transparent and replicated **partitions**"; shadow applications for low-downtime restructures.
- Heritage signals: migration paths from "Essbase 11g on-premises" and "Essbase Cloud Service"; "robust new features added since Release 11g" — the product explicitly carries a long release lineage.

## Product C — IBM Planning Analytics (TM1 engine)

Evidence layer: A for the IBM think article and product page (official IBM surfaces); IBM product documentation unreachable (403 ×2) — operational depth limited accordingly.

Key observations (IBM think, "What is TM1?"):

- Definition: "Table Manager 1 (TM1) is a **multidimensional, in-memory online analytical processing (OLAP) database** with a **cell-oriented structure**."
- "In TM1, data is stored as **multidimensional arrays (or 'cubes')** that can be easily manipulated and analyzed in real-time."
- Cell orientation: "Data is stored and processed at the level of individual cells ... allows for a high degree of flexibility in modeling and analyzing data."
- History: "Manny Perez invented Table Manager 1 (TM1) in **1983** to solve complex, forward-looking business modeling problems associated with budgeting, forecasting and financial reporting." Applix 1996 → Cognos 2007 → IBM; "In 2016, IBM rebranded the product name to Planning Analytics." "TM1 is still used to define IBM Planning Analytics core component, the TM1 Server."
- Core components: "**Cubes** are the central building blocks ... multidimensional arrays of data that allow users to analyze and explore data from different perspectives"; "**Dimensions** are the categories or attributes by which data is organized within a cube ... allow users to **slice and dice** data along different axes. Typical dimensions ... time, versions, regions, products, departments and metrics"; "**Hierarchies** are the logical organization of dimension members into a parent-child relationship ... e.g. year, quarter, month and day"; "**Rules** are statements or instructions that govern ... how the database processes and calculates data."
- Key mechanisms: "**In-memory**"; "**Write-back** — ... enables users to update and save changes made directly to cells in the database"; "**Real-time calculation** — TM1 optimizes calculations by performing them only on data that has actual values or changes."
- Security: "TM1 provides **granular security** capabilities, allowing for data access to be restricted to specific users or user groups."
- Integration: "Using **TurboIntegrator**, TM1 can integrate data from various data sources, including spreadsheets, leading EPM (for example, Oracle, SAP) and other data management systems."
- Front ends: "the web interface, IBM Planning Analytics Workspace and native Microsoft Excel add-in called Planning Analytics for Excel (PAX)."
- Positioning (product page): "From plans to decisions with AI-powered planning and analytics **powered by the IBM TM1 engine**"; use cases: FP&A, supply chain, workforce, sales, IT, marketing planning; pricing tiers (Essentials/Standard/Premium).

Interpretation note: IBM's own framing shows the OLAP engine (TM1) being packaged as the substrate of an FP&A product (Planning Analytics) — the engine belongs to this Type's territory; the planning workflow belongs to the FP&A Type. Recorded as a straddle, not a boundary failure.

## Product D — Apache Kylin

Evidence layer: A (directly observed, kylin.apache.org, 3 pages).

Key observations:

- Self-definition: "Apache Kylin is a leading **open source OLAP engine** for Big Data capable for **sub-second query latency** on trillions of records" (created at eBay 2014, Apache TLP 2015).
- "Kylin utilizes **multidimensional modeling theory** to build **star or snowflake schemas** based on tables ... The **model** is Kylin's core component, consisting of three key aspects: *model design*, *index design*, and *data loading*."
- Model design: "The core elements of model design are **computed columns, dimensions, measures, and join relations**."
- Index design: "creating indexes (**CUBEs**) within the model to **precompute query results**, thereby reducing query response time."
- Core concepts: "**Dimension**: A perspective of viewing data ... for example, product category"; "**Measure**: An aggregated sum ... for example, product sales"; "**Pre-computation**: The process of aggregating data based on model dimension combinations and of storing the results as indexes to accelerate data query"; "**Index**: Also called CUBE ... **Aggregate Index** ... **Table Index**."
- Pre-computation vs runtime: "Kylin primarily focuses on **pre-computation** to enhance query performance. However, we also offer advanced features that partially support runtime computation" (table snapshot, runtime join, internal table).
- Modeling evolution: "Before Kylin 5.0, model design had to be done manually ... We now offer ... **recommendation**, which allows models to be created by importing SQL, along with an automatic way to remove unnecessary indexes ... leverage query history to generate index recommendations."
- Streaming: "In the OLAP field, data has traditionally been processed in batches ... support for streaming data ... fusion model ... streaming-batch hybrid analysis."
- BI integration: "Support connecting to different BI tools, like Tableau/Power BI/Excel"; "Seamless integration with BI tools"; "Unified big data warehouse architecture."
- Compute evolution: 5.0 integrates Gluten-ClickHouse backend as native compute engine; internal tables with native storage format.

Interpretation note: Kylin names its precomputed aggregate structures "CUBE" and centers dimensions/measures — the cube concept survives in a SQL-interface, big-data, precompute architecture. Strong anti-overfit evidence: the cube model does not require MDX, does not require MOLAP block storage, and does not require Excel.

## Product E — Kyvos

Evidence layer: A for product-page content (official Kyvos marketing/product surfaces; Tier-2 positioning evidence — no operational docs fetched).

Key observations:

- "Multidimensional Analytics That Surpasses OLAP — Kyvos' **multidimensional semantic data models** deliver everything OLAP was supposed to and everything OLAP cannot."
- "Your Perfect Replacement for Legacy OLAP — Kyvos is the modern alternative for teams looking for **cloud-native multidimensional analytics** — or outgrowing **SSAS, TM1, Essbase, Strategy Intelligence Server or Azure AS**."
- "Unified data model that **replaces fragmented cubes** across SSAS, TM1, Essbase, Azure AS."
- "Multi-level **hierarchies** and nested relationships that mirror real-world business complexities."
- "Sub-second responses — Run complex **slices, dices and pivots** on billions of rows on cloud or on-premises platforms — without performance degradation."
- "Preserve familiar behaviors, remove platform limits — Continue to support advanced analytics functions, **MDX-style logic, drilldowns and complex hierarchies** — now running on elastic cloud infrastructure."
- "Any BI tool, any cloud platform — no vendor lock-in" (Power BI/Tableau/Excel/Looker/Strategy connectors; Snowflake/Databricks/BigQuery/AWS/Azure/GCP backends).
- FP&A use case: "P&L, budgeting, allocations, variance, and **scenario modeling** across product, region, cost centers, customer, and time dimensions."

Interpretation note: a current-market vendor independently frames its product as the continuation of OLAP (same model vocabulary: hierarchies, slices/dices/pivots, MDX-style logic, drilldowns) on new infrastructure. This is direct market evidence that the Type persists under new packaging ("semantic layer") and that the classic engines (SSAS/Essbase/TM1) are the recognized incumbent population of this Type.

## Cross-product Comparison

| Aspect | SSAS (multidimensional) | Essbase | TM1 / Planning Analytics | Apache Kylin | Kyvos |
|---|---|---|---|---|---|
| Defining object | Cube (in a database of data sources, DSVs, cubes, dimensions, roles) | Cube (application/database; hierarchically organized; outlines) | Cube (multidimensional array, cell-oriented) | Model + Index ("also called CUBE") | Multidimensional semantic data model ("replaces fragmented cubes") |
| Dimensions | Yes (shared across cubes) | Yes (dimension build; outlines) | Yes ("categories ... slice and dice along different axes") | Yes ("a perspective of viewing data") | Yes (multi-level hierarchies) |
| Hierarchies | Yes (dimensions carry structures) | Yes ("hierarchically organized cubes") | Yes (parent-child; year→quarter→month→day) | Yes (star/snowflake modeling) | Yes ("multi-level hierarchies and nested relationships") |
| Measures | Yes | Yes (member formulas; calculation layer) | Yes (metrics as a dimension; rules compute) | Yes ("an aggregated sum") | Yes |
| Navigation operations | Via clients (Excel etc.); fast query response | Ad hoc grid analysis; drill through; MDX slices | Slice and dice along axes | BI-tool exploration over precomputed model | Slices, dices, pivots, drilldowns |
| Query language | (MDX is the engine's language; not restated on fetched pages — not claimed) | MDX (query/insert/export) | Not verified (docs unreachable) | SQL | "MDX-style logic" |
| Storage mechanism | MOLAP / ROLAP / HOLAP (product-documented choice) | Block storage + Aggregate storage; hybrid default | In-memory | Precomputation (aggregate indexes) + internal tables | Cloud elastic (unspecified mechanism on fetched pages) |
| Write-back | Not verified on fetched pages | Scenario sandboxes (private work areas) | Explicit write-back to cells | Not claimed (read-oriented) | Scenario modeling (FP&A use case) |
| Security | Roles (database roles) | Roles + filters (cell-level access) | Granular security (users/groups) | Not fetched | Governance claims (positioning) |
| Primary clients | Excel, Reporting Services, third-party BI | Smart View (Excel), web grid analysis | Excel add-in (PAX), Workspace web | Tableau / Power BI / Excel | Power BI / Tableau / Excel / Looker |
| Data intake | Data sources + DSV; project deployment | Load rules; flat-file/Excel/SQL; dimension build | TurboIntegrator | Datasource → model → build | Connects to cloud platforms |
| Speed framing | "fast query performance" is the primary reason | "fast aggregation"; hybrid query engine | Real-time, in-memory | Sub-second on trillions of records | Sub-second on billions of rows |
| Era / posture | Enterprise DB-bundled; classic OLAP server | Independent engine; long lineage (11g→current) | 1983 invention; FP&A-packaged engine | Open-source big data (2014→) | Cloud semantic layer (current) |

### What is shared by ALL sampled products (candidate definitional core)

1. **The cube / multidimensional model as a persistent, named, reusable object** — dimensions (organized in hierarchies) × measures, designed once and queried many times. Every product names this object "cube" or treats it as the core (Kylin: "Index: also called CUBE"; Kyvos: "replaces fragmented cubes").
2. **Multidimensional navigation as the primary analytical interaction** — selecting members, aggregating along hierarchies (drill down / roll up), restricting to sub-spaces (slice / dice), re-orienting axes (pivot). Present in every product's own vocabulary or documented behavior.
3. **A serving engine that stores/optimizes and executes queries against the model for many consumers** — every product is a server/platform (not a file-format library), serves multiple users and multiple client tools, and frames speed ("fast", "sub-second", "real-time") as the design goal.

### What varies (candidate variant axes)

- Storage mechanism: MOLAP / ROLAP / HOLAP / block+aggregate storage / in-memory / precomputed indexes / cloud elastic.
- Query language: MDX / SQL / proprietary / "MDX-style".
- Write-back: present (TM1 explicit; Essbase scenarios) vs absent (Kylin read-oriented).
- Client surface: Excel add-ins / web grids / BI connectors / APIs.
- Positioning: standalone engine vs DB-bundled engine vs FP&A product substrate vs open-source engine vs cloud semantic layer.
- Data latency: batch loads vs streaming/fusion (Kylin) vs real-time (TM1).

## Canonical Abstraction

### L0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being an OLAP / Multidimensional Analytics Platform:

1. **The cube as the defining persistent object** — a named, reusable multidimensional model of the organization's data: dimensions (with hierarchies of members) × measures, designed once and queried many times. Remove → a query engine or BI tool with no model of record (SQL workbench / ad-hoc query / BI platform territory).
2. **Multidimensional navigation as the primary query mode** — analytical questions are expressed as operations on the model (select members, aggregate up/down hierarchies, slice/dice/pivot) returning aggregated measures — not as record-oriented retrieval. Remove → generic analytical querying (warehouse / SQL analytics territory).
3. **A serving engine that executes cube queries for many consumers** — the platform stores/optimizes (by any mechanism) and serves the cube to multiple users and client tools as the shared analytical source, with interactive response as the design goal. Remove → a personal/offline model (spreadsheet pivot over local data) or a model definition with no execution (a schema document).

Jointly-held load-bearing checks:

- 1 alone = a semantic/data model with no engine (modeling documentation).
- 2 without 1 = generic aggregation querying (SQL analytics over tables).
- 3 without 1+2 = generic query serving (a warehouse).
- 1+2 without 3 = desktop pivot/prototype (spreadsheet pivot over local data).
- 1+3 without 2 = a relational store with a dimensional schema but no cube-navigation semantics (warehouse with star schema).

### L1 — Common Mature Structure

Present across the sample (multiple products each), expected in mature products, not definitional:

- Hierarchies with named levels (year→quarter→month→day; region→country→city) as the navigation spine.
- A calculation layer: calculated measures / member formulas / rules (Essbase calc library + member formulas; TM1 rules; Kylin computed columns; SSAS "query and calculation engine").
- Aggregation machinery for interactive speed — precomputation, aggregations, in-memory structures (mechanism varies; the goal is universal).
- Client-tool integration: Excel add-ins, BI-tool connectors, APIs (Essbase Smart View + web grids; TM1 PAX + Workspace; Kylin Tableau/Power BI/Excel; Kyvos multi-BI; SSAS Excel/Reporting Services/third-party).
- Security: role-based access plus finer-grained dimension/cell-level controls (Essbase filters; TM1 granular security; SSAS roles; Kyvos governance).
- Data intake and processing pipeline: source connections, data load, dimension build, cube processing/refresh (all five).
- Drill-through to detail/source data (Essbase documented; IBM OLAP article describes drill-through as a standard OLAP operation; SSAS/Kylin not verified on fetched pages — held at common-with-evidence-gaps strength).
- Administration surface: manage cubes/applications, run/monitor jobs (Essbase Jobs interface; SSAS SSMS; Kylin web UI; Kyvos cloud console positioning).
- Saved analytical artifacts: named MDX queries, saved grid layouts (Essbase); saved views (TM1-family); model definitions (Kylin).

### L2 — Variant / Optional Structure

- **Write-back / planning orientation**: TM1 (explicit cell write-back), Essbase (scenario sandboxes, what-if, forecasting/allocation), Kyvos (scenario modeling use case) vs read-oriented engines (Kylin). Planning-oriented OLAP is a major market variant, not the definition.
- **Storage architecture**: MOLAP vs ROLAP vs HOLAP (SSAS product-documented); block vs aggregate storage (Essbase); in-memory (TM1); precompute (Kylin); cloud elastic (Kyvos). NOT definitional — the same Type is realized across all of them.
- **Query language**: MDX (Essbase documented; Kyvos "MDX-style logic"), SQL (Kylin), proprietary/visual (TM1 not verified). NOT definitional.
- **Streaming / real-time ingestion** (Kylin streaming-batch fusion; TM1 real-time calculation) vs classic batch loads.
- **What-if / scenario sandboxes** (Essbase, TM1-family, Kyvos).
- **Partitions / distributed cube topologies** (Essbase transparent/replicated partitions, shadow applications; SSAS partitions mentioned in administration context).
- **AI assistance** (Kylin auto-modeling/index recommendation; IBM Planning Analytics Agent; Kyvos AI positioning).
- **Deployment posture**: on-premises, cloud, DB-embedded, open-source self-hosted, SaaS.
- **Tabular/in-memory semantic models** (SSAS tabular line, Power BI lineage): the modern relational-shaped evolution of the same serving purpose; treated as adjacent evolution — the multidimensional cube remains this leaf's center (the leaf name itself says "Multidimensional").

### L3 — Vendor-specific Structure (research notes only)

- Essbase: outlines, dense/sparse storage configuration, calc scripts, MaxL/ESSCMD scripting, Report Writer, Smart View, Cube Designer (Excel-based cube design from application workbooks), Catalog + Gallery templates, Lifecycle Management migration, EAS Lite.
- SSAS: data source views, SQL Server Data Tools projects + deployment model, SSMS administration, multidimensional-vs-tabular server modes, Azure AS / Power BI Premium lineage.
- TM1: rules language, TurboIntegrator, Planning Analytics Workspace, PAX/PAfE Excel add-in naming, 1983 Sinper → Applix → Cognos → IBM lineage, Essentials/Standard/Premium tiers.
- Kylin: aggregate index vs table index, model recommendation engine, Gluten-ClickHouse native compute backend, internal tables, project/metadata model, streaming fusion models.
- Kyvos: "semantic layer" branding, replace-SSAS/Essbase/TM1 marketing, cloud-platform connector matrix, "1000x faster" claims (marketing, not asserted).

## Vendor-specific Findings

See L3 above. Additionally:

- Kyvos's "Replace SSAS/Essbase/TM1" positioning is itself useful market-structure evidence (it names the incumbent population of this Type), but its performance claims ("1000x faster", ">50% cost savings") are marketing and are not carried into the canonical document.
- IBM's think article ("What is OLAP?") is an educational article, not product documentation; its operation vocabulary (drill-down, roll-up, slice, dice, pivot) is used as corroborating canonical vocabulary, cross-checked against product-level evidence (Essbase MDX slices, TM1 slice-and-dice, Kyvos slices/dices/pivots).

## Boundary Findings

### vs Business Intelligence Platform (discharges the BI pass's flag from this side)

CONFIRMED, keep both. The BI pass recorded: "OLAP Platform stays the cube-centric Type (multidimensional model as the defining object); BI Platform is model-agnostic and consumption-lifecycle-centered." This pass confirms from the OLAP side:

- The OLAP platform's defining object is the **cube model + serving engine**; its consumers are tools and analysts navigating the model.
- The BI platform's defining structure is the **governed analytics supply chain** (authored content → hosted repository → audience → access control), model-agnostic over relational/search/cube substrates.
- Removal tests hold both directions: strip the cube model from an OLAP platform → a BI-like consumption surface remains possible but the Type's center is gone; strip the repository/audience/governance from a BI platform → cube serving remains OLAP territory.
- BI platforms have absorbed OLAP-style interactions (drill, slice) as capabilities — consistent with the BI pass's observation. The seam is the persistent served multidimensional model, not the interaction vocabulary.
- → Flag DISCHARGED; keep-both; cross-reference recorded in both directions.

### vs Data Visualization Application (discharges the data-viz pass's light flag from this side)

CONFIRMED, no overlap of centers. The data-viz Type centers on authoring chart artifacts (field-to-channel binding, finished visual taken out of the authoring session). The OLAP Type centers on the served multidimensional model; charts are client-side renderings of cube queries, not the Type's object. The OLAP platform's own surfaces are grids/models/admin consoles, not chart authoring. → Flag DISCHARGED; keep-both.

### vs Data Warehouse Platform

Clean substrate boundary, consistent with the BI and analytical-query-editor passes. The warehouse is the model-agnostic storage/compute substrate; the OLAP platform is the multidimensional model + serving layer historically built on top of it (IBM: "an OLAP server is typically the middle, analytical tier of a data warehousing solution"). Naming overlap noted: Kylin markets a "unified big data warehouse architecture" while its center remains the model+precompute serving layer — packaging language, not a boundary failure. Keep both.

### vs Spreadsheet Application (pivot capability)

The pivot interaction is a capability of spreadsheets; the OLAP platform is the server-side model+engine that pivot clients connect to. Excel is the dominant historical client of OLAP servers (SSAS integration; Essbase Smart View; TM1 PAX). A pivot over local spreadsheet data lacks the served shared cube — removal test holds. Keep both; the seam is the served shared model.

### vs SQL Workbench / Ad-hoc Query Application

Query authoring against data (row/SQL-oriented loop) vs navigation over a persistent multidimensional model. Kylin accepts SQL as its interface — but the SQL is served against precomputed cube structures; the model, not the query text, is the persistent object. Keep both.

### vs Financial Planning & Analysis Platform

Straddle documented, keep both. IBM packages the TM1 OLAP engine inside Planning Analytics (an FP&A product); Essbase carries planning-flavored capabilities (scenarios, what-if, allocations); Kyvos markets FP&A use cases. The seam: the FP&A Type centers the planning workflow (budget cycles, versions, approvals, planning process); this Type centers the cube model + engine that planning products deploy as their substrate. Write-back is the interlock capability (planning needs it; analytics-only engines lack it). Both documents should cross-reference.

### vs the "OLAP database" sense of the term (taxonomy note)

The market uses "OLAP" in two senses: (a) the multidimensional analytics platform sense (this leaf), and (b) the columnar analytical DBMS sense (ClickHouse/DuckDB-class engines — fast SQL aggregation over tables, no multidimensional model as defining object). Sense (b) belongs to Data Warehouse Platform / query-engine territory, not this leaf. The leaf name "OLAP / Multidimensional Analytics Platform" is read here in sense (a); the double naming in the leaf is actually helpful disambiguation. Recorded as a taxonomy observation, no directory change.

### vs modern "semantic layer" products

Kyvos (and, per its own comparison pages, AtScale/Cube-class products) market "semantic layer" while carrying multidimensional models, hierarchies, MDX-style logic, and slice/dice/pivot — i.e., this Type's structure on cloud infrastructure. This pass treats the multidimensional semantic-layer pole as a **variant posture of this Type** (Kyvos explicitly claims the "replace SSAS/Essbase/TM1" position), while noting that "semantic layer" as a general concept is broader (any governed model serving BI/AI tools) and partially overlaps the BI platform's semantic-model capability. No new leaf proposed; the seam is recorded for any future semantic-layer leaf.

## Historical / Market-Sample Check

- **TM1 (invented 1983)**: cell-oriented in-memory OLAP database; cubes/dimensions/hierarchies/rules; satisfies the L0 with zero cloud, AI, streaming, or modern-client machinery. Oldest anchor passes.
- **Essbase (long lineage, current 21c/26ai releases)**: the product's own docs carry the 11g→21c migration lineage; block-storage cubes, outlines, MDX, cell filters are all documented in the current release with no modern-stack machinery required by the definition. Passes. (Note: Essbase's pre-11g history is not verified from fetched sources; the long-lineage claim is anchored to the product's own migration documentation.)
- **Dedicated OLAP front-end clients of earlier generations**: clients of this Type's servers, not instances of the platform Type; the definition (server-side model + engine) is unaffected.
- **Excel PivotTables**: client-side pivot over local or server data — a capability of the spreadsheet Type; the platform Type is what serves the cube. Passes.
- The definition names no storage mechanism, no query language, no client, no deployment shape, no era machinery → historical check PASSED.

## Uncertainties

1. **IBM product documentation unreachable (403 ×2)** — TM1 operational details (query language support, dimension editor mechanics, security object model) not verified; TM1 claims limited to IBM's think article + product page content.
2. **AtScale unreachable (503 ×2, abandoned)** — the second modern semantic-layer vendor not directly evidenced; the modern pole rests on Kyvos alone (positioning-level evidence).
3. **Mondrian docs defunct** — the classic open-source ROLAP server not directly evidenced; ROLAP storage mode evidenced via SSAS product docs (MOLAP/ROLAP/HOLAP) and IBM's OLAP article instead.
4. **SSAS deeper pages not fetched** (guessed slugs 404 ×2) — no claims made about SSAS measure groups, partitions, perspectives, translations, or MDX specifics beyond the two fetched pages; SSAS MDX support is NOT asserted from fetched evidence (it is general knowledge but held out of the canonical document per evidence rules).
5. **Kylin security and write-back** not fetched — no claims.
6. **Kyvos evidence is positioning-level** (marketing/product pages); operational mechanics (aggregation strategy, security model) not verified.
7. **Essbase outline/dimension deep structure** (dense/sparse, attribute dimensions) not fetched; outline terminology used only as observed ("rich outline editor", "hierarchically organized cubes"). Essbase's pre-11g corporate history (original vendor, launch era) not verified from fetched sources — long-lineage claims anchored only to the product's own 11g→21c migration documentation.
8. **Drill-through** documented Tier-1 for Essbase and described in IBM's OLAP article; held at common-with-evidence-gaps strength for the other products.

## Final Synthesis

An OLAP / Multidimensional Analytics Platform is best modeled as **the served multidimensional model of an organization's data**:

```text
Connect the organization's data
→ model it once as a cube (dimensions with hierarchies × measures)
→ load / process / aggregate it (mechanism varies: MOLAP, ROLAP, HOLAP,
   in-memory, precomputed indexes, cloud elastic)
→ serve the cube to many users and tools
→ users navigate the model: pick members, drill down / roll up
   hierarchies, slice / dice / pivot
→ the engine returns aggregated measures with interactive response
→ govern it: roles, dimension/cell-level security, processing cycles
→ (variant) write back into the cube for planning workflows
```

The defining core is deliberately small: **the cube (persistent multidimensional model) + cube-navigation querying + a serving engine for many consumers**. Everything the market associates with the category — MOLAP preaggregation, MDX, Excel add-ins, write-back, streaming, AI modeling assistants, "semantic layer" branding — is common mature structure or variant posture, not definition. The Type's continuity is unusually visible: a 1983 in-memory engine, a long-lineage independent engine, a DB-bundled enterprise engine, a 2014 open-source big-data engine, and a current cloud semantic-layer product all satisfy the same three-part core, and the current market explicitly frames the newest pole as the successor of the classic ones ("replace SSAS/Essbase/TM1").
