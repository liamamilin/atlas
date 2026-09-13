# Research Notes — Data Visualization Application

## Research Goal

Understand what a Data Visualization Application actually is as an Application Type: its defining structure (and how small it can be made), the authoring workflow, its interfaces, its output semantics, and its boundaries against neighboring Types — especially Business Intelligence Platform (joint-review flag to discharge), Dashboard Platform (secondary seam to discharge), Data Explorer, Ad-hoc Query Application, Data Science Workbench, Diagramming Application, and Spreadsheet.

## Initial Boundary

Initial hypothesis (pre-research):

- Core use: an application whose purpose is turning a user's own data into a chart/map/table visualization that is completed and used elsewhere (article, report, presentation, web page).
- Primary users: people who need to *produce* visualizations as content — journalists, analysts, researchers, designers, communicators — rather than organizations consuming governed analytics.
- Nearest neighbors: Business Intelligence Platform (adds hosted repository + consumer audience + governance), Dashboard Platform (standing live multi-panel displays), Data Explorer (selection over published data), Ad-hoc Query Application (the question loop), Data Science Workbench (code-first analysis with inline charts), Diagramming Application (hand-authored shapes), Spreadsheet (charts as a capability).
- Prior recorded seams to honor:
  - business-intelligence-platform (processed): "A data-visualization application centers on authoring charts/visuals — conceivably single-user, file-based, without a consumer audience or access governance. **Test**: remove multi-user hosting/consumption/governance → data viz application remains." → Flag for joint review; discharge expected from this side.
  - dashboard-platform (processed): "Single-user or file-based chart authoring vs a platform that maintains connected, current, shared displays. Removal test: remove the viewer audience + currency + connection plumbing → Data Visualization Application."
  - data-explorer (processed): "Viz app: user imports arbitrary data and designs charts (data ownership + design freedom). Explorer: data fixed by publisher; user selects within a published structure."
  - ad-hoc-query-application (processed): "Visualization is the presentation layer; an ad-hoc query can return a plain table, and a data-viz tool can exist without live querying (authoring from static data)."
  - diagramming-application (processed): "data viz renders charts from data automatically; diagramming is hand-authored structure where data linking is an optional layer."
  - data-explorer name-collision note: "§13 leaves whose products ship surfaces literally named 'data explorer' should note the collision at their own passes." → Noted below.
- Likely confusion #1: in the current market the flagship visualization tools are embedded inside BI platforms (Tableau inside the Tableau platform, Power BI Desktop inside Power BI) — the Type must be defined by the authoring act, not by the platform that ships it.
- Likely confusion #2: "visualization" is a capability of half the data stack (explorers, query tools, workbenches, dashboards) — the definition must capture the application whose *center* is the crafted visual artifact.

## Research Questions

1. What are the core objects? (data, chart/visualization, chart model/type, field-to-channel binding, project, output artifact)
2. What is the authoring loop, end to end? (bring data → choose visual form → bind fields → customize → complete/publish)
3. What does "the visualization" become after authoring — a file, an embed, a hosted page? Is output portability definitional?
4. Is a hosted repository / viewer audience / access governance part of the Type, or the BI platform's addition?
5. Where does data come from (paste/upload/link/live connection), and is live currency definitional?
6. How do the different authoring philosophies differ (template-first, wizard/recommendation, free-form encoding mapping, direct manipulation)?
7. Historical check: do desktop charting applications and command-line plotting tools of earlier eras fit the same definition?
8. Where is the boundary vs each sibling Type, expressible as a removal test?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Philosophy / Tier | Why selected |
|---|---|---|
| Datawrapper | Chart/map/table builder for newsrooms & journalists; step-based SaaS; free to enterprise plans | The cleanest "author → publish/export" product in the media segment; chart-family and export behavior documented in an open Academy |
| Flourish | Template-driven visualization & storytelling; newsrooms to marketing; Canva-owned | The template-first philosophy at scale; explicitly polices its own boundary against BI in its FAQ |
| RAWGraphs | Free open-source, free-form visual models; designer/research audience; browser-only (no server) | The no-repository, no-audience, export-only pole — proves the Type survives without any platform structure |
| Tableau (Desktop authoring) | Professional direct-manipulation authoring (shelves/marks) inside a larger platform | The canonical free-form encoding-binding model; also a living illustration of the packaging boundary (Desktop = viz authoring; Cloud/Server = BI platform) |

Evidence for Tableau is reused from the paired business-intelligence-platform pass (same research effort, 2026-09-06, Tier 1 help.tableau.com pages — recorded there with URLs and observations).

## Sources

Research date: 2026-09-07 (Tableau evidence: 2026-09-06 via the BI pass).

### Datawrapper (Tier 1 — official Academy, academy.datawrapper.de)

- Academy home: https://academy.datawrapper.de/ ("Here you can learn how to build charts, maps and tables with Datawrapper")
- Welcome category: https://academy.datawrapper.de/category/welcome (tour, first chart/line chart/choropleth map, Annotate tab article, accessibility/alt-text articles, River showcase article)

Observed structure: chart-family categories (Bar, Column, Line & Area incl. slope, Dual-axis & Waterfall [plan-gated], Pie & Donut, Scatter, Dot [dot/range/arrow], Tables "with bar charts, images & links", Choropleth / Symbol / Locator maps); workflow categories (Uploading & Changing Data; Displaying Data [dates/numbers]; Organizing visualizations in an Archive; Embedding & Exporting [publish/embed/export]; Live-updating Visualizations; Workspaces & Teams); feature nav (Custom Themes, Dark Mode, Print Export, Localization, Teams, Accessibility, Privacy, Security, PowerPoint Integration, API docs); product nav (Charts / Maps / Tables); plans (Free/Pro/Business/Enterprise).

### Flourish (Tier 1 help center home + Tier 2 product site)

- Help center home: https://flourish.studio/help/ (category structure)
- Product site: https://flourish.studio/ (positioning, product menu, FAQ)

Observed: help categories — Charts ("Flourish chart templates from Line, bar, pie to Bar chart race"), Shared settings (colors, popups, annotations), Maps (Projection, 3D, Marker, Globe), Tables and heatmaps ("mini-charts, images and shading"), Content-based templates (Cards, Interactive SVG, Timeline, Quiz, Word Cloud), Stories and scrollies, Data ("Adding and editing data"), Exporting ("Exporting, Images, Canva and Powerpoint"), AI features, Premium & Account settings. Product site: "Create interactive charts and maps using no-code templates"; "Flourish stories: Build multi-step explainers with charts and captions"; "Simply import your data and transform it into interactive visuals"; "share and embed your visualisations across platforms—websites, presentations, social media assets"; FAQ: "Is Flourish a business intelligence tool? Flourish is not typically regarded as a business intelligence tool. While its templates and API allow for data exploration and dashboard integration, its primary focus is on data storytelling, especially for presentations and digital publications." Canva acquired Flourish in 2022; SDK for custom templates; Flourish Assistant (AI) + MCP Connector.

### RAWGraphs (Tier 2 — product site + documentation page)

- Home: https://www.rawgraphs.io/
- Documentation: https://www.rawgraphs.io/documentation

Observed: "A free and open source tool for data visualization"; "Almost 30 visual models to visualize quantities, hierarchies, time series and find insights in your data"; "Your data is safe — Even though RAWGraphs is a web app, the data you insert will be processed only by your web browser"; "Export and go anywhere — Save your project, or export it as vector or raster image. Edit it within your favourite softwares."; docs: "RAWGraphs app: A web interface to create custom vector-based visualizations on top of RAWGraphs core"; Tutorials / Courses / FAQ / Gallery / Custom charts; built by DensityDesign research lab; GitHub-based open source.

### Tableau (Tier 1 — help.tableau.com, fetched in the paired BI pass 2026-09-06)

- Get Started: https://help.tableau.com/current/pro/desktop/en-us/gettingstarted_overview.htm
- Build a Basic View: https://help.tableau.com/current/pro/desktop/en-us/getstarted_buildmanual_ex1basic.htm
- Use Tableau on the Web: https://help.tableau.com/current/pro/desktop/en-us/web_author_home.htm

Recorded observations reused: connect-to-data start page; Data Source page; worksheet with Data pane fields split into dimensions (categorical/discrete) and measures (numeric/aggregated); drag fields onto shelves (Columns, Rows, Filters) and the Marks card (Color etc.); the view re-renders as the answer to the implied question ("Every view that you build in Tableau should start with a question"); drill, level of detail (small multiples), filter, unlimited undo/redo; Show Me chart-type suggestions; views → workbooks; dashboards compose views; stories sequence views.

### Source-access limitations

- **Datawrapper deep articles**: the "first chart" walkthrough URL redirected to the Academy home (2 attempts). Evidence stays at Academy-structure level (categories, feature list, product surfaces); no per-step editor claims asserted beyond the directly observed "Annotate" tab article title.
- **Flourish help-center category pages**: two category URLs 404'd after the home page fetched successfully. Evidence stays at help-home + product-site level; no per-template claims.
- **Tableau Public**: public.tableau.com returned a JavaScript-only shell (no content). No Tableau Public positioning claims made; Tableau evidence is Desktop-authoring-surface level from the BI pass.
- **RAWGraphs app itself** (app.rawgraphs.io) and per-chart tutorials not fetched (JS app); evidence is product-site level.
- No precise operational limits (row caps, file-size limits, plan prices) are asserted anywhere.

## Product Observations

### Datawrapper

Evidence layer: A (directly observed, Academy structure).

- **Purpose framing**: "build charts, maps and tables" — the chart/map/table is the product's unit.
- **Chart families as first-class curriculum**: bar (stacked, bullet, split, grouped), column, line/area/slope, pie/donut, scatter (annotations, custom lines), dot/range/arrow, tables (with embedded mini bar charts, images, links), choropleth/symbol/locator maps. Some families are plan-gated (dual-axis & waterfall on Business plan) — chart-type breadth is part of the commercial packaging.
- **Data side**: a dedicated "Uploading & Changing Data" knowledge area ("which kind of data Datawrapper accepts & how to change it") and "Displaying Data" (formatting of dates and numbers) — data intake and display-formatting are managed steps.
- **Output side**: "Embedding & Exporting — How to publish, embed, and export your Datawrapper visualizations" (17 articles); Print Export and PowerPoint Integration as named features; Live-updating Visualizations as a separate area (data currency is an optional capability, not the default frame).
- **Annotation**: an "Annotate" tab exists as a distinct editor step (article title directly observed).
- **Organization & collaboration**: Archive ("organize your charts, maps, and tables"), Workspaces & Teams (31 articles); Custom Themes for repeatable house style; Localization; Accessibility (alt-text guidance as a dedicated article area); River (public showcase of visualizations); developer API.
- **Center of gravity**: single visualization authored from imported data and completed into a publishable/embeddable/exportable artifact. No modeling layer, no consumer-permission subsystem in evidence.

### Flourish

Evidence layer: A (help home + product site, incl. FAQ).

- **Template-first authoring**: the product menu itself is "Create interactive charts and maps using no-code templates"; help is organized by template families (Line, bar, pie → Bar chart race; Projection/3D/Marker/Globe maps; tables with mini-charts; content-based templates: cards, interactive SVG, timelines, quizzes, word clouds).
- **Data**: "Adding and editing data" category; "Simply import your data and transform it into interactive visuals" — import-then-configure, not query-then-render.
- **Shared settings**: colors, popups (tooltips), annotations configurable across templates — chart-configuration semantics above the template layer.
- **Output**: Exporting category ("Images, Canva and Powerpoint"); "Share anywhere… share and embed your visualisations across platforms"; "All outputs are styled for robustness, capable of reaching unlimited audiences, and optimized for mobile viewing" (FAQ answer).
- **Storytelling extension**: Flourish stories ("multi-step explainers with charts and captions"), stories and scrollies category — narrative sequencing of visualizations as a product pillar beyond single charts.
- **Boundary self-policing** (vendor-acknowledged seam): "Is Flourish a business intelligence tool? Flourish is not typically regarded as a business intelligence tool… its primary focus is on data storytelling, especially for presentations and digital publications."
- **Extensibility & AI**: Flourish SDK for custom templates; Flourish Assistant (AI guidance on charts); MCP Connector for AI tools; Canva ownership (2022) — sits adjacent to a design platform without becoming one.

### RAWGraphs

Evidence layer: A (product site + documentation page).

- **Free-form visual models**: "Almost 30 visual models to visualize quantities, hierarchies, time series" — a library of chart layouts chosen by the user, not templates keyed to a house style.
- **Explicit no-server posture**: "Even though RAWGraphs is a web app, the data you insert will be processed only by your web browser." No account, no hosted repository, no viewer audience — the strongest evidence in the sample that platform structure is not part of the Type.
- **Output-centric**: "Export and go anywhere — Save your project, or export it as vector or raster image. Edit it within your favourite softwares." Project persistence is a local file; the deliverable is a vector/raster asset for use in other software.
- **Docs framing**: "A web interface to create custom vector-based visualizations" — creating custom visuals from one's own data is the whole product.
- **Extensibility**: custom chart models (a documented extension path); open source; academic/design-research origin (DensityDesign) — the designer/researcher pole.

### Tableau (Desktop authoring surface; from the BI pass)

Evidence layer: A (help.tableau.com, 2026-09-06 pass).

- **The canonical binding model**: fields split into dimensions (categorical) and measures (numeric, auto-aggregated); the user drags fields onto shelves (Columns, Rows, Filters) and the Marks card (Color, etc.); the view re-renders the answer to the implied question. This is field-to-visual-channel binding in its most explicit form.
- **Chart-form assistance**: Show Me suggests appropriate chart types for the selected fields — recommendation machinery on top of free-form binding.
- **Artifact hierarchy**: worksheets (views) → workbooks; dashboards compose views; stories sequence views. The single visualization (view) is the atom.
- **Live data connections**: Desktop connects to databases/warehouses natively — heavier data plumbing than the media-pole products, but in service of the same authoring act.
- **Packaging boundary made visible**: the same vendor ships the authoring surface (Desktop) and the platform (Cloud/Server with sites, permissions, viewers, subscriptions) — the viz application is one surface of a BI platform, exactly the seam the BI pass predicted.

### Cross-checks from processed sibling passes (evidence layer A in those passes)

- Ad-hoc query pass: the question loop can return "a plain table", and chart authoring can proceed "from static data" without querying — the two acts are separable.
- Data-explorer pass: explorer users "never import, model, or query the data"; viz-app users import their own data and design charts.
- Diagramming pass: data viz "renders charts from data automatically"; diagramming is hand-authored.
- Data-science-workbench pass: inline visualization is a workbench capability; the workbench's center is the interactive code session.

## Cross-product Comparison

| Dimension | Datawrapper | Flourish | RAWGraphs | Tableau (Desktop) | Verdict |
|---|---|---|---|---|---|
| User brings own data (import/paste) | Yes (Uploading & Changing Data) | Yes ("import your data") | Yes (browser-processed input) | Yes (connect to data; files) | **L0** |
| Choose a visual form / chart model | Yes (chart-family catalog) | Yes (template library) | Yes (~30 visual models) | Yes (Show Me + free-form) | **L0** |
| Bind data fields to visual channels | Yes (column assignment per chart type) | Yes (template data columns) | Yes (dimension mapping per model) | Yes (shelves + marks — most explicit) | **L0** |
| Computed rendering from data (re-renders on change) | Yes | Yes | Yes | Yes ("view re-renders") | **L0** |
| Completed artifact leaves the tool (export/publish) | Yes (publish/embed/export/print/PowerPoint) | Yes (export images/Canva/PowerPoint; share/embed) | Yes ("export as vector or raster… edit in your favourite softwares") | Yes (export/copy views; workbooks) | **L0** |
| Data preparation in service of the chart (formats, cleanup) | Yes (Displaying Data) | Yes (shared settings; data editing) | Limited (model-oriented) | Yes (data-source prep) | L1 |
| Chart-form recommendations | Yes (recommended per data shape) | (template choice guided by goal) | (not asserted) | Yes (Show Me) | L1 (observed in 2 of 4 directly) |
| Customization (titles, colors, legends, tooltips, annotations) | Yes (+ Annotate tab) | Yes (shared settings: colors, popups, annotations) | (per-model options; not detailed) | Yes (marks, filters) | L1 |
| Templates/themes as repeatable style | Yes (Custom Themes) | Yes (templates are the model) | (not asserted) | (not asserted) | L1 (Flourish pole) |
| Maps as a chart family | Yes (choropleth/symbol/locator) | Yes (projection/3D/marker/globe) | No (quantities/hierarchies/time series) | Yes (maps as view type — BI pass TOC) | L1 (not definitional: RAWGraphs lacks maps) |
| Interactive published output (tooltips, responsive) | Yes (embeds; privacy controls) | Yes ("fully interactive", mobile-optimized) | No (static vector/raster export) | Yes (embedded views) | L1 — static output remains fully in-Type |
| Chart project as revisable object | Yes (Archive, editable charts) | Yes (projects) | Yes ("Save your project" — local file) | Yes (workbook file) | L1 (storage locus varies: local file ↔ cloud) |
| Organization of many charts (archive/folders) | Yes (Archive) | Yes (projects) | No | (workbook organization; platform outside Type) | L1/L2 |
| Team collaboration (workspaces/teams) | Yes (31 articles) | Yes (teams, on-brand) | No (single user) | (platform layer) | L1/L2 |
| Live-updating data connections | Yes (Live-updating area) | Yes (via API/dashboard integration) | No | Yes (native connectors) | L2 (optional capability; currency is the dashboard platform's center) |
| Hosted repository + viewer audience + access governance | No (publish links only; privacy feature) | No (unlimited audience via embeds — no governance layer in evidence) | No (no server at all) | Only in the platform half (Cloud/Server) | **absence confirms the boundary** — BI platform's addition |
| Storytelling/narrative extension | (not asserted) | Yes (stories/scrollies) | No | Yes (stories — BI pass) | L2 |
| AI assistance | (not asserted) | Yes (Assistant, MCP Connector) | No | Yes (Copilot — platform; BI pass) | L2 (era-typical) |
| No-code only | Yes | Yes | Yes | No (code-adjacent ecosystem exists; drag-based authoring) | L2 |
| Open source / self-hostable | No | (SDK yes; hosted product) | Yes | No | L2 |
| Public showcase of visualizations | Yes (River) | Yes (examples gallery) | Yes (gallery) | Yes (Tableau Public — surface not fetched) | L2 |
| Plan-gated chart types | Yes (Business plan: dual-axis/waterfall) | (premium features) | n/a (free) | (licensing — out of scope) | L3 |

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the product stops being recognizable as a Data Visualization Application:

```text
User-supplied structured data (brought into the application by the user)
└── Visual form + field-to-channel binding (choose a chart model; map data
    fields onto visual channels — axes, position, length, color, size)
    └── Computed rendering (marks are drawn from the data and the binding;
        the picture re-renders when data or mapping changes)
        └── Finished visual artifact (the authored visualization is completed
            and taken out of the authoring session — image, vector, print,
            embed, or published chart)
```

Four properties:

1. **User-supplied structured data** — the working material is the user's own data, brought in by paste, upload, file, or link. Without this, the product operates over someone else's published data (Data Explorer) or over connected organizational sources governed elsewhere (BI), or has no data at all (drawing tool).
2. **Visual form + field-to-channel binding** — the user chooses a chart model and maps data fields onto visual channels. The mapping is the authoring act; it may be done by drag-and-drop, dialog, template column assignment, or commands. Without the binding, the product composes by selection (Data Explorer) or hand-draws (diagramming/design tools).
3. **Computed rendering** — the marks are computed from the data under the binding and re-render when either changes. Without this, the product is an illustration/infographic tool with data-shaped decoration.
4. **Finished visual artifact** — the goal of the session is a completed visualization that leaves the tool in portable form (image/vector/print file, embed code, published chart) to be used in an article, report, presentation, or web page. Without this, the tool is an interactive scratchpad or explorer, not a production tool.

Removal tests:

- Remove the user's own data (only publisher-published data) → Data Explorer
- Remove the field-to-channel binding (selection over fixed structure) → Data Explorer; (hand-authored marks) → Diagramming / design tools
- Remove computed rendering (hand-placed marks) → Graphic design / infographic tools
- Remove the finished artifact (interactive viewing only, no completed output) → explorer/scratchpad territory
- Add hosted repository + consumer audience + access governance → Business Intelligence Platform

### L1 — Common Mature Structure

Present in most mature products; expected by the market but not definitional:

- **Chart-form library** — the standard families (bar/column, line/area, pie/donut, scatter/dot, tables) near-universally; maps (choropleth/symbol/locator) and exotic layouts (sankey, treemap, bar chart race, parliament, chord) in template-rich products.
- **Data intake & display machinery** — paste/upload (CSV/XLSX), spreadsheet/URL links, column typing, number/date formatting, light cleanup/transposition in service of the chart.
- **Customization layer** — titles/subtitles, labels, legends, color palettes, axes/gridlines, tooltips/popups, annotations, source lines; per-chart and (in some products) cross-chart shared settings.
- **Chart-form assistance** — recommended chart types based on the data's shape (wizard-style products; "Show Me"-style suggestion in direct-manipulation products).
- **Output mechanics** — PNG/SVG/PDF/print export, responsive embed code, share links, presentation-software export integrations.
- **The chart project as a revisable object** — save/re-edit; the storage locus varies (local file ↔ cloud archive) and is a variant, not the structure.
- **Organization of a body of work** — archives/folders/projects of charts (in SaaS-pole products).
- **Accessibility support** — alt text/descriptions, colorblind-safe palettes (documented as a dedicated concern in the media-pole products).
- **Theming/templates for repeatable style** — house-style themes, brand colors, reusable configurations.
- **API access** — programmatic creation/management of charts in SaaS products.

### L2 — Variant / Optional Structure

Depends on audience, philosophy, deployment, business model:

- **Authoring philosophy poles**: template-first (pick a template, fill its columns) vs wizard/recommendation (chart suggested from data shape) vs free-form visual models (pick a layout, map dimensions) vs direct-manipulation binding (drag fields to shelves/marks).
- **Audience poles**: newsroom/journalist (publishing workflows, localization, accessibility) vs designer/researcher (free-form models, vector handoff to other software) vs professional/enterprise analyst (live data connections, heavy customization).
- **Storage posture**: browser-only with no server (data never leaves the browser; project saved as a local file) vs cloud SaaS projects/archives vs desktop files with an optional platform behind them.
- **Data currency**: static imports by default; live-updating charts / live connectors as an optional capability (where currency becomes the point, the product is drifting toward Dashboard Platform).
- **Output interactivity**: static vector/raster vs interactive embeds (tooltips, hover, responsive) — both fully in-Type.
- **Narrative extensions**: multi-step stories/scrollytelling sequencing multiple visualizations (a capability extension; a distinct concern from single-chart authoring).
- **Maps**: a first-class family in some products, absent in others.
- **Extensibility**: SDKs / custom chart models; open-source editions.
- **Code-adjacent authoring**: command-line/code-driven plotting as the same Type's historical and specialist pole (see Historical Check).
- **Public showcases** of published visualizations; plan-gated chart families (commercial packaging).

### L3 — Vendor-specific Structure

Stays in Research Notes only:

- **Tableau**: dimensions/measures with discrete/continuous color coding; shelves (Columns/Rows/Filters); Marks card; Show Me; "every view starts with a question" framing; level-of-detail/small multiples; unlimited undo in authoring; worksheet→workbook hierarchy; stories; the Desktop/Cloud/Server packaging split.
- **Datawrapper**: step-based editor with a named "Annotate" tab; Archive organization; Workspaces & Teams; Custom Themes; Print Export; PowerPoint Integration; Localization; chart families incl. locator maps; plan-gated dual-axis & waterfall charts; River showcase; developer API.
- **Flourish**: template library as the primary navigation (Line/bar/pie → Bar chart race; content-based templates: cards, interactive SVG, timeline, quiz, word cloud); shared settings (colors, popups, annotations); stories/scrollytelling; Flourish Assistant; MCP Connector; SDK; export to Canva/PowerPoint; FAQ self-positioning against BI; Canva ownership (2022).
- **RAWGraphs**: ~30 visual models; browser-only processing; local project files; SVG/PNG export; custom chart model extension; DensityDesign origin; GitHub sponsors model.

### Rejected Findings (Anti-overfitting)

- **"No-code" is tempting as definitional** → rejected: the code-adjacent pole (command-line/code-driven plotting lineage; SDK extensibility) and free-form binding products show the binding act, not the absence of code, is the invariant.
- **"Interactive output" is tempting** → rejected: a sampled product's entire output model is static vector/raster, and the print/PDF tradition is mature; interactivity is an output variant.
- **"Embeds" as definitional** → rejected: image/vector export satisfies the finished-artifact property; embeds are one delivery form.
- **"Newsroom audience" as definitional** → rejected: designer/research and professional analyst poles exist with the same structure.
- **"Maps" as definitional** → rejected: a sampled product has no map family at all.
- **"Templates" as the model** → rejected: template-first is one philosophy; wizard, visual-model, and direct-manipulation philosophies coexist.
- **Cloud SaaS / accounts / teams** → rejected: the browser-only no-server product and desktop-file products satisfy the definition.
- **AI assistance** → rejected: era-typical capability, not structure.
- **Hosted repository + viewer audience + access governance** → rejected as definitional, and their absence is precisely the BI boundary; publish links/embeds that expose a finished chart to "unlimited audiences" (Flourish FAQ wording) do not constitute a governed analytics estate.
- **Chart-form breadth (30 models vs 8 families)** → rejected: breadth is commercial/packaging variance; the binding act is the invariant.

### Historical / Market-Sample Check

- **Desktop charting applications of earlier eras** (scientific/business charting packages; presentation-chart modules): enter/import data → choose chart type → customize → print/export to slide or paper. Satisfy all four properties with no cloud, no teams, no interactivity, no AI. ✓
- **Command-line/code-driven plotting lineage** (gnuplot-class): data-file columns bound to plot styles via commands; output written to files/terminals. The binding act is present (stated as commands rather than gestures), rendering is computed, output is portable. Satisfies the definition as the code-adjacent pole. ✓ (Category-level inference from documented lineage — no primary docs fetched this pass.)
- **Spreadsheet chart wizards**: the authoring act is the same, but the core object of the enclosing Type is the cell grid; charts are a capability of the Spreadsheet Type, not a standalone Data Visualization Application. ✓ (boundary, not counter-example)
- **Statistical packages' plotting layers**: code-adjacent pole, same reasoning. ✓
- The definition does not depend on web vs desktop, cloud vs local, interactive vs static, template vs free-form — the era-typical wrappers all pass.

## Vendor-specific Findings

See L3. Additional notes worth keeping:

- Flourish's FAQ explicitly answers "Is Flourish a business intelligence tool?" in the negative while acknowledging template/API-based "data exploration and dashboard integration" — a vendor-policing of exactly the seam the BI pass predicted (presentation/digital-publication focus vs governed analytics).
- Flourish's "unlimited audiences" FAQ phrasing describes publish reach, not governed distribution — distribution-as-publication, not BI's access-controlled consumption.
- Datawrapper gates chart families by plan (dual-axis/waterfall on Business plan) — chart-type breadth as commercial packaging.
- RAWGraphs' data-privacy posture ("processed only by your web browser") is a direct articulation of the no-server pole: the application is the interface, the user's machine is the infrastructure.
- Tableau's Desktop vs Cloud/Server split makes the viz-application/BI-platform packaging boundary observable within one vendor: the authoring surface (shelves/marks/views) is the viz application; sites/permissions/viewers/subscriptions are the platform.

## Boundary Findings

### vs Business Intelligence Platform (processed sibling; joint-review flag DISCHARGED from this side)

Confirmed from the DVA side. The BI pass's test — "remove multi-user hosted repository + consumer audience + access governance → data viz application remains" — holds: the sampled DVA population centers on the authoring act over user-supplied data; none of the three SaaS/cloud products carries a governed content repository, author/consumer split, or data-access-control subsystem as its center, and the no-server product has no repository at all. Flourish polices the same seam in its own FAQ (not typically a BI tool; primary focus is data storytelling for presentations and digital publications).

- Data Visualization Application: the visualization authoring act — user data → binding → computed rendering → finished artifact.
- BI Platform: the governed analytics supply chain — connected org data + authored content + hosted repository + consumer audience + controlled access.

Removal tests (both directions): strip a BI platform to authoring charts from imported data with no repository/audience/governance → a data visualization application; add hosted repository + consumer audience + access governance to a DVA → it becomes a BI platform (observable as the packaging boundary in the Tableau product line: Desktop is the authoring surface; Cloud/Server is the platform). → Recommendation to taxonomy owner: keep both Types with the authoring-act-as-capability seam documented on both sides; no re-scoping needed.

### vs Dashboard Platform (processed sibling; secondary seam DISCHARGED from this side)

Confirmed from the DVA side. Dashboard-side test — "remove the viewer audience + currency + connection plumbing → Data Visualization Application" — holds: the DVA sample authors single finished visualizations from imported, static-by-default data; publish links expose one completed chart, not a standing display. Dashboards are persistent composed displays of multiple live data-bound panels kept current over connected sources for a viewer audience; the DVA artifact is a content element consumed inside an article/report/page. Datawrapper's live-updating charts and Flourish's API/dashboard integration are optional capability extensions — the currency is not the center of gravity in any sampled product. → Boundary held; no re-scoping needed.

### vs Data Explorer (processed sibling, §02.12)

Confirmed from both sides (explorer pass: "Let users bring their own data and author free-form charts → viz app"). The explorer composes views by selection within publisher-published, pre-structured data; the DVA imports the user's own arbitrary data and binds fields to channels. Name-collision note recorded as requested: "Data Explorer" also names enterprise explore-mode surfaces in §13 products (BI explore modes, consoles, ad-hoc UIs); the §02.12 leaf keeps the published-data consumer sense, and this pass claims none of those surfaces for the DVA Type.

### vs Ad-hoc Query Application (processed sibling)

Consistent with the recorded seam: "Visualization is the presentation layer; an ad-hoc query can return a plain table, and a data-viz tool can exist without live querying (authoring from static data)." The question loop's center is composing and refining a query; the chart is the answer's rendering. The DVA's center is crafting the visual artifact; aggregation exists only in service of encoding. Modern products fuse the loops, but the centers of gravity separate. Boundary held.

### vs Data Science Workbench (processed sibling)

The workbench's defining structure is the interactive stateful code session; visualization is an inline output capability. The DVA's defining structure is the binding act and the finished artifact; a code editor is absent (or peripheral). Publishing notebooks as apps/dashboards (workbench drift) and code-driven plotting (DVA's code-adjacent pole) approach each other but the centers remain distinct. Boundary held.

### vs Diagramming Application (processed sibling)

Confirmed from the diagramming side: data viz renders marks from data automatically; diagramming hand-authors shape structures with optional data linking. Removal test: remove hand-authoring of shapes → data visualization; remove computed rendering → diagramming. Boundary held.

### vs Spreadsheet Application (§03.03, unprocessed leaf family)

Charts in spreadsheets are a capability of a Type whose core object is the cell grid (calculation model). The DVA inverts this: the chart is the object, the data is supporting material. No conflict recorded; light flag for the spreadsheet passes.

### vs Reporting Platform (§13 sibling, unprocessed)

Formatted, document-shaped output (paginated reports) vs chart artifacts: reports are documents that *contain* visualizations; the DVA produces the visualization itself. Charts feed reports. → Light flag for joint review when Reporting Platform is processed (same seam family the BI pass recorded).

### vs Graphic/Template Design Platforms (§04.01) and Presentation Application (§03.04)

Design platforms author marks by hand (no computed data binding) even when arranging "data-looking" decoration; presentations consume finished charts as slide content. The Canva acquisition of Flourish is adjacency without identity: Flourish keeps the data-binding core inside a design company. Boundary held.

### vs OLAP / Multidimensional Analytics Platform (§13 sibling, unprocessed)

OLAP's defining object is the multidimensional cube with slice/dice/drill navigation; the DVA has no cube semantics. Historical OLAP clients were visualization-heavy but the model, not the picture, is the object. → Light flag for the OLAP pass.

## Uncertainties

1. **Deep workflow evidence is TOC-level for three of four products** (Datawrapper deep articles redirected; Flourish category pages 404'd; RAWGraphs app is a JS surface). The authoring loop is asserted from help-center structure, product positioning, and the Tableau deep evidence — step-by-step editor mechanics for the media-pole products are not directly observed. No per-step claims are made in the final document.
2. **Tableau Public surface not fetched** (JS shell); Tableau evidence is Desktop-authoring level. No Tableau Public-specific claims.
3. **Historical check is category-level inference** for the desktop-charting and command-line lineages (no primary docs fetched); marked as inference.
4. **Code-adjacent pole (Plotly Chart Studio-class) not sampled**; its existence is lineage-level reasoning, not direct observation this pass.
5. **Precise limits** (data-size caps, row limits, plan-gated feature lists beyond the observed chart-family example) not asserted anywhere.
6. **Interactive-output detail** (tooltip behavior, responsive breakpoints) observed only as capability-level claims; no mechanics asserted.
7. **Unprocessed siblings** (reporting-platform, olap, spreadsheet family) — flags recorded here for joint review; no unilateral taxonomy change made.

## Final Synthesis

A Data Visualization Application is best modeled as **the chart-production craft as a standalone application**:

```text
Bring your own data (paste / upload / link / connect)
→ choose a visual form (chart model or template)
→ bind data fields to visual channels
   (drag to shelves, assign columns, fill a template, or state a mapping)
→ the application computes and re-renders the picture from data + binding
→ customize (titles, colors, legends, tooltips, annotations, formats)
→ complete the artifact (export image/vector/print, embed, publish chart)
→ use it elsewhere (article, report, presentation, web page)
```

The defining core is deliberately small: user-supplied data + field-to-channel binding under a chosen visual form + computed rendering + a finished portable artifact. Everything the market associates with the category — template libraries, chart-type breadth, maps, interactive embeds, live-updating data, teams, AI, accessibility machinery — is common mature structure or variant posture, not definition. The Type's position in the data stack: it is the *production* end of visualization (making the picture), while Data Explorer is the *consumption* end over published data, Dashboard Platform is the *standing display* end, and the BI Platform is the *governed estate* end — each obtainable from this one by a recorded removal test.
