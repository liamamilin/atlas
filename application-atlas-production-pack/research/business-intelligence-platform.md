# Research Notes — Business Intelligence Platform

## Research Goal

Understand what a Business Intelligence Platform actually is as an Application Type: its defining structure (and how small it can be made), its standard workflow, its interfaces, its governance rules, and its boundaries against neighboring Types — especially Ad-hoc Query Application (joint-review flag to discharge), Dashboard Platform, Reporting Platform, Data Visualization Application, OLAP Platform, Data Warehouse Platform, Analytical Query Editor, and Data Science Workbench.

## Initial Boundary

Initial hypothesis (pre-research):

- Core use: an organizational system that connects to the organization's data, lets analysts author curated analytics content (dashboards, reports), and distributes that content to business consumers who view and interact with it under access control.
- Primary users: three roles — authors/designers (analysts), consumers (business users), administrators (governance).
- Nearest neighbors: Dashboard Platform / Reporting Platform (artifact-centric slices), Ad-hoc Query Application (the interactive question loop), Data Visualization Application (single-user authoring), OLAP Platform (cube-centric analytics), Data Warehouse Platform (the storage/compute substrate BI consumes), Data Science Workbench (code-first analysis).
- Prior recorded seams to honor:
  - ad-hoc-query-application (processed): "BI Platform: persistent curated artifacts + distribution + governance as the primary structure; Ad-hoc Query Application: the interactive question loop as the primary structure" — flag for joint review discharged in this pass.
  - analytical-query-editor (processed): "Editors produce queries and result sets; BI platforms curate persistent artifacts (dashboards/reports) for consumption and distribution."
  - process-mining-platform (processed): "BI Platform (case-sequence derivation vs generic aggregation)" — boundary held, consistent.
- Likely confusion #1: dashboards are the flagship artifact of BI platforms — how does Dashboard Platform stay a separate leaf?
- Likely confusion #2: the category absorbs capabilities from every sibling (query loop, formatted reports, charts, AI Q&A) — the Type definition must be structure-based, not feature-based.

## Research Questions

1. What are the core objects? (data connection, data/semantic model, visualization, dashboard/report, workspace/repository, app/distribution container)
2. What is the authoring loop, end to end? (connect → prepare/model → visualize → compose → publish)
3. How is the author/consumer split implemented? What can consumers do without authoring rights?
4. What does governance look like? (content permissions, data permissions, row-level security, certification)
5. What distribution machinery exists? (apps/audiences, links, embeds, subscriptions, alerts, mobile)
6. Is the semantic/metric layer definitional or common? How do viz-first vs semantic-first vs search-first philosophies differ?
7. Where is the boundary vs each sibling Type, and can each be expressed as a removal test?
8. Historical check: do classic enterprise BI suites (Cognos/BusinessObjects/MicroStrategy era) and modern self-service/warehouse-native products fit the same definition?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Philosophy / Tier | Why selected |
|---|---|---|
| Tableau (Salesforce) | Visual-analysis pioneer; desktop author + Cloud/Server platform; enterprise standard | The canonical "build a view by dragging fields" authoring model; strongest evidence for the visualization-first pole |
| Power BI (Microsoft) | Ecosystem suite inside Microsoft Fabric; desktop author + cloud service; mass-market to enterprise | Richest documented platform layer: workspaces, roles, apps with audiences, semantic models as shared objects, licensing/capacity |
| Qlik Cloud Analytics | Associative-engine analytics inside a broader data-integration cloud; enterprise | App/selection-based exploration model; governed activity centers; shows BI bundled with a full data stack |
| Metabase | Open-source + cloud; self-service BI for teams | Lowest customer tier in the sample; platform structure (permissions, collections, embedding) documented openly; proves the Type without enterprise scale |

Supporting cross-checks (evidence gathered in the paired ad-hoc-query-application pass, same research date): ThoughtSpot (search/AI-first enterprise BI; Liveboards, semantic layer), Zoho Analytics (drag-and-drop self-service BI; workspaces, dashboards, sharing). Looker (semantic-layer-first pole) could not be reached (see Source-access limitations) — no Looker-specific claims are made.

## Sources

Research date: 2026-09-06.

### Tableau (Tier 1 — official help site, help.tableau.com)

- Get Started (Desktop and Web Authoring Help): https://help.tableau.com/current/pro/desktop/en-us/gettingstarted_overview.htm
- Build a Basic View to Explore Your Data: https://help.tableau.com/current/pro/desktop/en-us/getstarted_buildmanual_ex1basic.htm
- Use Tableau on the Web (Tableau Cloud / Tableau Server surfaces): https://help.tableau.com/current/pro/desktop/en-us/web_author_home.htm
- Observed TOC structure: creators vs viewers tracks; connect/prepare data; explore/inspect data in a view; custom views; tags; content revisions; refresh/pause automatic updates; web authoring (connect to data on the web, prepare data on the web, edit views on the web, upload workbooks, connect to published data sources); dashboards; stories; share web content; subscriptions to views/workbooks; data-driven alerts; embed views and metrics; comment on views.
- Note: the paired ad-hoc pass recorded help.tableau.com 404s on different URLs; this pass's URLs fetched successfully — Tableau evidence is Tier 1 here.

### Power BI / Microsoft Learn (Tier 1)

- Power BI service basics (key concepts): https://learn.microsoft.com/en-us/power-bi/fundamentals/service-basic-concepts
- Publish an app in Power BI: https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-create-distribute-apps
- Plus (paired ad-hoc pass, same date): desktop-what-is-desktop, desktop-getting-started.

### Qlik (Tier 1 — official help site, help.qlik.com)

- Qlik Cloud Help home / Welcome: https://help.qlik.com/en-US/cloud-services/ (structure observed from nav: Analytics, Data Integration, Administration, Automations; client-managed Qlik Sense; QlikView legacy)
- Using analytics to explore data: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/using-analytics-to-explore-data.htm

### Metabase (Tier 1 — official documentation site)

- Dashboards overview: https://www.metabase.com/docs/latest/dashboards/start (with full docs TOC captured)
- Plus (paired ad-hoc pass, same date): questions/start, questions/introduction, query-builder/editor.
- TOC sections observed this pass: Dashboards (filters, linked filters, interactivity, multiple series, subscriptions, actions), Documents, AI (Metabot, MCP server, agent API, usage controls), Data modeling (models, metrics, semantic types, segments, editable tables), Data Studio (transforms incl. Python, dependency graph), Organization (collections, data reference, X-rays, content verification, history, delete/restore), Embedding (modular embedding SDK, guest embedding, full app embedding, public links, tenants), Administration (databases incl. ~20 drivers, sync/scanning, authentication: SSO/SAML/JWT/OIDC/LDAP/Google, Permissions: data/collections/application/row-and-column security/database routing/impersonation), Usage analytics, Serialization.

### Source-access limitations

- **Looker (Google Cloud)**: cloud.google.com/looker/docs timed out again this pass (in addition to two timeouts recorded in the ad-hoc pass). Abandoned per network rule (4 total failures across passes). The semantic-model-first philosophy is represented instead by Power BI semantic models (Tier 1) and Metabase models/metrics (Tier 1), with ThoughtSpot's semantic layer from the paired pass.
- **IBM Cognos Analytics docs**: ibm.com/docs returned 403 on the single attempt. Abandoned. The classic-enterprise-BI historical check is therefore category-level inference (see Historical / Market-Sample Check), not direct observation.
- **Qlik depth**: observations are from the help-site home/TOC structure and the explore-data page (page titles + intro prose); deep per-feature mechanics (selection engine internals, load script specifics, section access) were not fetched. Assertions kept at structure level.
- **Tableau platform governance**: sites/projects/permissions and row-level-security specifics were not fetched; Tableau platform claims are limited to what the three fetched pages document (creators/viewers, sites, content management, revisions, subscriptions, alerts, embedding, comments).
- **Power BI**: app-page precision (audience-count limits, license mechanics) is product/plan-specific and kept in Research Notes only.

## Product Observations

### Tableau

Evidence layer: A (directly observed from official help pages).

Key observations:

- **Authoring loop** (Desktop): connect to data (start page → pick source; Data Source page shows tables; drag table to canvas) → worksheet: Data pane lists fields split into **dimensions** (categorical; discrete/blue) above a line and **measures** (numeric; continuous/green; auto-aggregated, e.g. SUM) → drag fields onto **shelves** (Columns, Rows, Filters) and the **Marks card** (Color etc.) → the view re-renders as the answer to the question implied by field placement ("Every view that you build in Tableau should start with a question") → drill hierarchies (+/−), add level of detail (small multiples), filter, undo/redo unlimited.
- **Show Me**: chart-type suggestions appropriate to selected fields.
- **Views are the unit of analysis**; a **workbook** contains views and its data-source connections; **dashboards** compose views; **stories** sequence views for narrative.
- **Platform surfaces** (Tableau Cloud / Tableau Server, "a Tableau site"): role tracks documented for **Creators** (web authoring: connect to data on the web, prepare data, edit views, create dashboards/stories, upload workbooks, connect to **published data sources**) and **Viewers** (what can I do with a web view). Content management: explore/inspect data in a view, **custom views** (personal), tags, **content revisions**, refresh data or pause automatic updates, manage web content. Share and collaborate: share web content, **subscriptions** to views/workbooks, **data-driven alerts**, **embed views and metrics**, **comment on views**.
- Data freshness is a managed property (refresh or pause automatic updates).

### Power BI

Evidence layer: A (directly observed from Microsoft Learn).

Key observations:

- **Two named user classes**: **designers/creators** ("build reports and dashboards; organize content; collaborate; assign roles; manage permissions; publish apps") and **end users/consumers/business users** ("view and explore reports; monitor dashboards; use apps; collaborate on goals").
- **Key concepts** (official glossary): **Visualization** (interactive chart type built by designers, sliceable/filterable/drillable); **Semantic model** (formerly dataset — "a container of data used by designers to build reports, dashboards, and apps; can combine multiple data sources into a single model"); **Dashboard** ("a single screen with tiles... often used to monitor metrics"); **Report** ("one or more pages of interactive visuals... based on a single semantic model"); **App** ("a collection of dashboards, reports, and semantic models bundled together for sharing"); **Workspace** ("a collaborative area where designers store and manage collections..." with roles **Admin, Member, Contributor, Viewer**); licenses/capacity as access/feature layers; **Copilot** AI assistant (report-scoped and app-scoped).
- **Distribution machinery** (apps page): workspace = **staging area**; "create app → add content → create and manage multiple audiences → publish"; app users "can't modify the contents" but "can filter, highlight, and sort the data"; **audiences** let authors show/hide different content per group; **build permissions** on semantic models let consumers create their own reports from the underlying model; access-request flow for unauthorized users; unpublishing removes consumer access and **loses consumer customizations** (bookmarks, comments); licensing gates consumption (Pro vs Premium-capacity).
- **Governance coupling**: reports depend on semantic models; sharing/building rights on models are granted separately from report access; dashboards' tiles break if underlying reports are removed/hidden (dependency rules documented).
- Deployment pipelines referenced as the content-promotion mechanism (mentioned in limitations).

### Qlik Cloud Analytics

Evidence layer: A for structure (help-site home + explore-data page); depth limited to page titles and intro prose.

Key observations:

- **Positioning**: "modern analytics capabilities across a full range of users and use cases — from self-service analytics to interactive dashboards and applications, conversational analytics, metadata catalog and lineage, mobile analytics, reporting and alerting."
- **Core object = the application (app)**: analytics applications built by loading and modeling data ("Add your data sources first, load the data into your application and start modeling your data model"); users explore apps via **selections** (associative exploration), **smart search** ("search the entire dataset used in an application"), **Insight Advisor** (AI-assisted analysis generation), **conversational analytics** (Insight Advisor Chat), **bookmarks** of selections.
- **Governed content organization**: **activity centers** ("the central point of access for applications, spaces, and other content... formerly known as hubs") — Insights, Analytics, Data Integration, Administration; **spaces** for collaboration; **business glossaries**.
- **Distribution**: share/download content (PDF, images, Excel), **data storytelling** ("direct, in-context linking to live analytics"), **subscriptions** (scheduled emails of visualizations and sheets), **alerts** (outliers/anomalies), monitoring visualizations, requesting application access, analyzing anonymous content (shareable without a tenant account), mobile app.
- **Suite context**: data integration (Qlik Talend), automations (Qlik Automate), ML (Qlik Predict), MCP server; client-managed Qlik Sense and QlikView exist as older deployment/generation forms; NPrinting is the formatted-reporting companion.

### Metabase

Evidence layer: A (docs TOC + dashboards start + prior-pass question/builder pages).

Key observations:

- **Self-description**: "Business Intelligence — Self-service analytics for your team"; the paired ad-hoc pass documented the **Question** as "the basic analytical unit" (query + result + visualization), with builder/SQL/NL authoring.
- **Dashboards**: compose questions (tables/charts) with **text cards**; **dashboard filters** (incl. **linked filters**); **interactive dashboards** (customized click-through); multiple series; **subscriptions** ("email or Slack its results on a schedule"); **actions** (buttons to write back to data).
- **Content organization**: **collections** (with permissions), **history** (of edits), **content verification**, **delete and restore**, **events and timelines**, **X-rays** (auto-exploration), **data reference** (glossary of fields).
- **Data modeling**: **models** (curated starting points), **metrics**, **segments**, table **metadata/semantic types**, **editable tables**, JSON unfolding; **Data Studio** layer with **transforms** (incl. Python) and a **dependency graph** for impact analysis.
- **Permissions** (a full documented subsystem): **data permissions** (database/table-level, separate builder vs native-query rights), **row and column security**, **collection permissions**, **application permissions**, **database routing** (multi-tenant data isolation), **impersonation**, embedding permissions.
- **Authentication/admin**: users and groups, SSO (SAML/JWT/OIDC/LDAP/Google), API keys, sessions; **usage analytics** (out-of-the-box analytics about the platform's own usage); **serialization/remote sync** (environment migration); caching; database connections (~20 drivers) with **syncing and scanning**.
- **Distribution beyond the org**: **public links**, **embedding** (modular embedding SDK with components; guest embedding; full-app embedding; **tenants** for multi-customer isolation).

### ThoughtSpot / Zoho Analytics (from the paired ad-hoc pass; evidence layer A there)

Key platform-level observations reused as cross-checks:

- ThoughtSpot: **Liveboards** (dashboards) as curated consumption surfaces; Answers saved into Liveboards; **semantic layer/Models** as governed query substrate; **collections**; admin console/privileges; monitoring (KPI alerts); embedded analytics; TML for artifact portability.
- Zoho Analytics: **Workspaces** grouping tables + reports + dashboards; drag-and-drop report designer; sharing to users/groups; embedding/white-label/portals; email scheduling of reports; 40+ app connectors.

## Cross-product Comparison

| Dimension | Tableau | Power BI | Qlik Cloud | Metabase | ThoughtSpot/Zoho (prior pass) | Verdict |
|---|---|---|---|---|---|---|
| Connects to external org data sources | Yes | Yes (multi-source semantic models) | Yes (sources → load into app) | Yes (~20 DB drivers, uploads, Sheets) | Yes | **L0** |
| User-authored analytics artifacts (dashboards/reports) | Yes (views→workbooks, dashboards, stories) | Yes (reports, dashboards) | Yes (apps: sheets/visualizations, stories) | Yes (dashboards of questions) | Yes (Liveboards; dashboards/reports) | **L0** |
| Hosted persistent content repository with organization | Yes (site, content management, revisions) | Yes (workspaces) | Yes (spaces, activity centers) | Yes (collections, history) | Yes (collections; workspaces) | **L0** |
| Consumer audience beyond the author (view/explore without authoring) | Yes (viewers track; web view interactions) | Yes (end users; app consumers) | Yes (app consumers; anonymous analysis) | Yes (view-only via shared content/embeds) | Yes | **L0** |
| Controlled access (content + data permissions) | Yes (role tracks; implied site permissions — depth not fetched) | Yes (workspace roles; build permissions; access requests) | Yes (spaces; governed content areas; request access) | Yes (data/collection/app permissions; row/column security) | Yes | **L0** |
| Visualization-centric composition | Defining style (shelves/marks) | Yes | Yes | Yes | Yes | L1 (form; tables also valid) |
| Shared data/semantic model layer | Published data sources; workbook data model | Semantic models central, shared, permissioned | App data model; business glossary | Models/metrics/segments (optional layer) | TS: Models/semantic layer central; Zoho: light | L1 (near-universal; depth varies) |
| Interactive consumption (filter/drill/sort) | Yes (plus personal custom views) | Yes (filter/highlight/sort/drill) | Yes (selections drive the whole app; bookmarks) | Yes (dashboard filters, drill-through) | Yes | L1 |
| Ad-hoc question loop as bundled capability | Yes ("every view starts with a question"; undo any path) | Yes (field selection, Q&A/Copilot) | Yes (Insight Advisor, smart search, chat) | Yes (builder/SQL/Metabot — core object) | Yes (search bar; Ask Zia) | L1 (capability, not the platform's definition) |
| Scheduled delivery (subscriptions) | Yes (views/workbooks) | Yes (subscriptions; apps as bundles) | Yes (scheduled emails of visuals/sheets) | Yes (email/Slack schedules) | Yes (Monitor; email scheduling) | L1 |
| Data-driven alerts | Yes | Yes | Yes | Yes | Yes | L1 |
| Data refresh management | Yes (refresh/pause updates) | Yes (scheduled refresh) | Yes (load/refresh model) | Yes (sync/scanning; model persistence) | Yes | L1 |
| AI assistance (NL Q&A, auto-insight, agents) | (not fetched this pass) | Yes (Copilot, report- and app-scoped) | Yes (Insight Advisor + Chat, Discovery Agent feeds) | Yes (Metabot, MCP) | Yes (Spotter; Ask Zia/Insights) | L1 |
| Embedded analytics | Yes (embed views/metrics) | Yes | Yes (developer surface) | Yes (SDK, guest, full-app, tenants) | Yes | L1 |
| Mobile app | (not asserted — not fetched) | Yes | Yes | (mobile not asserted) | (not asserted) | L1 (observed in 2–3 of 4 primaries) |
| Formatted/pixel-perfect reporting | (separate lineage; not asserted) | Yes (paginated reports) | Yes (NPrinting companion; cloud reporting service) | (not asserted) | (Zoho export/email) | L2 (capability; separate sibling leaf) |
| Certification/endorsement of content | (not asserted) | (verified answers via Copilot docs; promoted content not fetched) | (governed areas + glossary) | Yes (content verification) | (not asserted) | L1/L2 (observed directly in 1–2) |
| Version/revision of content | Yes (content revisions) | (deployment pipelines referenced) | (not asserted) | Yes (history, delete/restore) | Yes (TML) | L1 |
| Platform usage analytics | (not asserted) | (usage metrics referenced) | (monitoring visualizations) | Yes (usage analytics module) | (not asserted) | L1/L2 |
| Desktop-installed authoring app | Yes (Desktop) | Yes (Desktop) | No (web; Qlik Sense Desktop exists client-managed) | No (web) | No | L2 |
| Cloud SaaS vs client-managed/self-host | Cloud + Server (client-managed) | Cloud (+ Report Server) | Cloud + client-managed | Cloud + self-host (OSS) | Cloud + on-prem (TS) | L2 |
| Suite expansion (integration/ETL, catalog, ML, automations) | (Salesforce ecosystem, not asserted here) | Yes (Fabric items in workspaces) | Yes (Talend, catalog/lineage, Predict, Automate) | Yes (Data Studio transforms; editable tables) | Yes (Analyst Studio; Zia suite) | L2 |
| Write-back/actions on data | (not asserted) | (not observed) | (not asserted) | Yes (actions, editable tables) | (not observed) | L2 (product-specific so far) |
| Environment migration/serialization of content | (not asserted) | (pipelines referenced) | (not asserted) | Yes (serialization, remote sync) | Yes (TML) | L2 |

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the product stops being recognizable as a Business Intelligence Platform:

```text
Connected data sources (the organization's external data, connected into the platform)
└── User-authored analytics content (dashboards / reports composed of
    visualizations and tables, built inside the product)
    └── Hosted persistent repository (content stored, organized, and
        versioned by the platform — not passed around as files)
        └── Consumer audience beyond the author (non-authoring users
            view and interact with published content)
            └── Controlled access (permissions governing who can see
                which content and which data)
```

Five properties:

1. **Connected data sources** — the platform connects to data that lives outside itself (databases, warehouses, files, business applications). Without this, analytics over "the organization's data" is impossible and the product is an application-embedded analytics module or a personal tool.
2. **User-authored analytics content** — dashboards and reports are composed by users inside the product from visualizations/tables over the connected data. Without authoring, the product is a fixed metrics portal, not a BI platform.
3. **Hosted persistent repository** — content lives in the platform's own storage, organized (workspaces/projects/spaces/collections), durable and current. Without this, content is files passed between people — a desktop authoring tool, not a platform.
4. **Consumer audience beyond the author** — a distinct population views and interacts with the content without authoring it (the author/consumer split). Without this, it is a single-user visualization application.
5. **Controlled access** — permissions govern which users can see which content and which data (including data-level restriction). Without control, the shared repository could not safely serve an organization; every observed product implements it as a first-class subsystem.

Removal tests:

- Remove consumer audience (single-user) → Data Visualization Application / desktop authoring tool
- Remove hosting/repository (files passed around) → desktop BI authoring, not a platform
- Remove authoring (fixed predefined views only) → metrics portal / report distribution viewer
- Remove data-source connection (product's own data only) → product-embedded analytics
- Remove access control → not deployable as an organizational platform; the market never ships this state

### L1 — Common Mature Structure

Present in essentially all mature products; expected by the market but not definitional:

- **Shared data/semantic layer** — data prepared, related, and (to varying depth) modeled once and reused across content: published data sources, semantic models with relationships and defined measures, metrics/modeled tables. Depth ranges from thin metadata to a governed, permissioned model layer.
- **Interactive consumption** — consumers filter, drill, sort, and highlight inside published content; personal views/bookmarks/customization.
- **Self-service authoring/exploration loop** — the ad-hoc question loop (query builders, field-drag, search, natural-language questions, drill) available to authors and, to a governed degree, to consumers.
- **Scheduled delivery** — subscriptions that email/push content or its results on a schedule.
- **Data-driven alerts** — notifications when metrics cross thresholds.
- **Data freshness management** — scheduled refresh, caching/extracts vs live query, sync of source schemas.
- **Content organization & discovery** — containers (workspaces/projects/spaces/collections), search, tags, favorites.
- **Content lifecycle** — revision history, restore, deletion; endorsement/certification signals in some products.
- **Embedded analytics** — distributing content inside other applications (links, iframes, SDKs, white-labeling).
- **Mobile consumption surfaces** — in the larger enterprise products.
- **AI assistance** — natural-language Q&A, auto-generated insights, AI agents over the platform's data.
- **Administration & governance of the platform itself** — user/group management, SSO, audit/usage analytics, licensing.
- **Export** — PDF/image/Excel/CSV of content and data.

### L2 — Variant / Optional Structure

Depends on segment, philosophy, deployment, ecosystem:

- **Product philosophy poles**: visualization-first authoring (Tableau), ecosystem suite with shared semantic models (Power BI), associative-app exploration (Qlik), search/AI-first (ThoughtSpot), lightweight question-first self-service (Metabase), semantic-model-first governance (Looker pole — not directly researched, philosophy-level only).
- **Authoring substrate**: desktop-installed authoring app + web platform vs web-only authoring vs viewer-only tiers.
- **Deployment**: cloud SaaS vs client-managed/self-hosted/on-premises (including open-source editions).
- **Suite expansion**: bundled data integration/ETL, data catalog/lineage, AutoML, automations, spreadsheets-like prep surfaces — the platform absorbing neighboring data-stack Types.
- **Formatted reporting**: pixel-perfect/paginated report output, often via companion engines (capability; the Reporting Platform leaf is the standalone form).
- **Write-back/actions** on data from within content (observed in one product; optional).
- **Multi-tenant/OEM posture**: embedding-first product lines with per-customer tenant isolation.
- **Content DevOps**: deployment pipelines, serialization/environment sync, artifact text formats.
- **Data connectivity breadth**: files, cloud drives, SaaS app connectors, uploads.
- **Licensing/capacity models** shaping who can consume (per-user vs capacity-gated).

### L3 — Vendor-specific Structure

Stays in Research Notes only:

- **Tableau**: dimensions vs measures (blue/green), shelves (Columns/Rows/Filters), Marks card, Show Me, unlimited undo in authoring, small multiples, published data sources, site-level content management with custom views/tags/revisions, stories.
- **Power BI**: semantic model (formerly dataset) as the permissioned central object; report-vs-dashboard distinction (report = pages on one semantic model; dashboard = tile screen aggregating content); apps with up to 25 audience groups and ~10,000 user/group entries (documented limits — product-specific, not asserted in the final doc); workspace roles (Admin/Member/Contributor/Viewer); Pro/Premium licensing and capacity gating; Fabric workspace cohabitation (lakehouses, notebooks); Copilot capacity requirements; unpublish losing consumer customizations; dashboard-tile dependency errors; deployment pipelines.
- **Qlik**: associative selections as the exploration primitive; apps with load-script data modeling; Insight Advisor / Insight Advisor Chat; Discovery Agent feeds; activity centers (formerly hubs); spaces; business glossaries; anonymous-analysis links; NPrinting (formatted reports); QlikView legacy line; client-managed Qlik Sense.
- **Metabase**: Question as basic analytical unit; collections with permissions; content verification; row-and-column security; database routing/impersonation (multi-tenant isolation); embedding tenants; guest embedding; Data Studio transforms with Python runner; dependency graph; editable tables; X-rays; events/timelines; serialization/remote sync; usage-analytics module.
- **ThoughtSpot/Zoho** (prior pass): Answers as saved searches; TML; Spotter agents; Query Tables; Ask Zia training; white-label portals.

### Rejected Findings (Anti-overfitting)

- **Dashboards are universal** → tempting for L0 as "the BI object". Rejected as *the* defining structure: dashboards are one artifact form; reports (paginated/operational) and apps/stories are equally first-class in the sample, and a BI platform defined as "dashboard software" would exclude half the category's work. Dashboards live in the artifact layer (L0 property 2) without being the definition.
- **Semantic layer is central in enterprise products** → rejected for L0: lightweight products (Metabase) treat models/metrics as optional; classic BI predates modern semantic layers while still being BI (metadata models existed, but thin deployments did fine). Strong L1, not definition.
- **Self-service question loop is now everywhere** → rejected for L0: the loop is a capability the platform bundles (see Boundary Findings vs Ad-hoc Query Application); classic scheduled-report BI satisfied L0 without it.
- **AI assistants are now near-universal in the sample** → rejected for L0/L1-as-definition: one more authoring/consumption aid over the same structure.
- **Cloud SaaS delivery is near-universal** → rejected for L0: client-managed/self-hosted deployments (Tableau Server, Qlik Sense on Windows, Metabase OSS) are still BI platforms. L2.
- **Mobile apps** → only some products observed; L1/L2, not definitional.
- **Per-user licensing/capacity** → vendor commercial detail; excluded from the Type definition entirely.

### Historical / Market-Sample Check

- **Classic enterprise BI suites (Cognos, BusinessObjects, MicroStrategy, Brio era)**: metadata/semantic model + report authoring + dashboards + OLAP navigation + server-hosted content store + security + scheduling/distribution to business consumers. They satisfy the five L0 properties without any modern feature (web-first, AI, mobile, embed SDKs). ✓ (Category-level inference from documented category history — IBM docs unreachable (403); marked as inference, not observation.)
- **Reporting-first products (Crystal Reports-class)**: report authoring + distribution, but centered on formatted document output rather than interactive visual analytics over a governed repository — they sit nearer the Reporting Platform leaf; the boundary is recorded there (unprocessed sibling).
- **Spreadsheet-based analysis (Excel + pivots)**: satisfies the analysis act but not the platform structure (no hosted shared repository, no author/consumer split, no access control over published content) → outside the Type; BI platforms exist precisely to industrialize what spreadsheets did ad hoc. ✓
- **OLAP-era clients**: cube browsers fit the consumption layer; the OLAP Platform leaf remains the cube-centric Type (boundary recorded below). ✓
- **Warehouse-native / modern self-service products (Sigma-class, Superset-class)**: same five L0 properties over different substrates; the definition does not depend on cloud vs self-host, desktop vs web, or live vs extracted data. ✓ (Inference for non-sampled members; consistent with sampled structure.)

## Vendor-specific Findings

See L3. Additional governance-relevant rules worth keeping:

- Power BI documents that distribution copies can carry consumer-created personalizations (bookmarks/comments) and that unpublishing destroys them — distribution state is user-stateful. (Product-specific.)
- Power BI documents that content dependencies (dashboard tiles → reports → semantic models) create permission chains; hiding/removing a dependency breaks downstream content. (Product-specific articulation of a general dependency problem.)
- Metabase separates query-authoring rights from data-access rights (builder vs native-query permissions) and documents that hiding columns in visualization settings is not a security mechanism — exclusion must happen in the data step or row/column security. (Product-specific rule; illustrates the data-permission layer.)
- Qlik documents anonymous analysis links (consumption without tenant membership) and request-access flows. (Product-specific distribution posture.)
- Tableau documents data-freshness control as a user-facing content property (pause automatic updates). (Product-specific framing.)

## Boundary Findings

### vs Ad-hoc Query Application (processed sibling; joint-review flag discharged from this side)

Confirmed from the BI side. Every sampled BI platform bundles the interactive question loop (Tableau's "every view starts with a question" + unlimited-undo exploration; Power BI field-selection authoring + Copilot Q&A; Qlik Insight Advisor + smart search + chat; Metabase's Question as core object; ThoughtSpot's search bar). The distinguishing structures remain:

- BI Platform: the governed lifecycle of curated artifacts for an audience — authored content hosted in a repository, distributed to consumers, access-controlled, maintained over time.
- Ad-hoc Query Application: the interactive question loop itself (compose → run → refine), whose artifacts are saved questions.

Removal tests (both directions): strip the BI platform to the loop alone (no repository/audience/governance) → ad-hoc query application remains; give the loop's saved questions a repository, audiences, and governance → a BI platform. In the current market the loop ships inside BI platforms as a core capability; the standalone Ad-hoc Query Application Type survives as the loop-centered products (and as the bundle's interactive core). → Joint review recommendation for the taxonomy owner: keep both Types with the loop-as-capability seam documented on both sides, or re-scope ad-hoc-query-application as the interactive slice of the BI family; both docs are consistent either way.

### vs Dashboard Platform (sibling leaf, unprocessed)

Dashboards are the flagship artifact of BI platforms; a standalone "dashboard platform" in the market is typically a lightweight, dashboard-first slice (compose dashboards from data sources, share them) with thinner governance, modeling, and repository machinery. Probable partial alias / capability-slice relationship. → Flag for joint review when Dashboard Platform is processed.

### vs Reporting Platform (sibling leaf, unprocessed)

Formatted, document-shaped output (pixel-perfect, often scheduled delivery to email/print) exists inside BI platforms as a capability (paginated reports, NPrinting, subscriptions) and as standalone reporting products. BI center = interactive visual analytics over a governed hosted repository for exploration; reporting center = production and delivery of formatted documents. Modern products fuse both. → Flag for joint review when Reporting Platform is processed.

### vs Data Visualization Application (sibling leaf, unprocessed)

A data-visualization application centers on authoring charts/visuals — conceivably single-user, file-based, without a consumer audience or access governance. The BI platform adds the hosted repository, the author/consumer split, and controlled access. **Test**: remove multi-user hosting/consumption/governance → data viz application remains. → Flag for joint review when Data Visualization Application is processed.

### vs OLAP / Multidimensional Analytics Platform (sibling leaf, unprocessed)

Historical BI bundled OLAP (cubes, dimensions/measures, slice-dice-drill navigation); modern BI platforms absorb the same interactions over relational/search substrates. OLAP Platform stays the cube-centric Type (multidimensional model as the defining object); BI Platform is model-agnostic and consumption-lifecycle-centered. → Flag for joint review when the OLAP leaf is processed.

### vs Data Warehouse Platform (sibling leaf, unprocessed)

Clear and consistent with the analytical-query-editor pass: the warehouse is the storage/compute substrate (modeling and serving data at scale, no authored consumer content); the BI platform connects to it and adds authoring/repository/distribution/governance. No conflict; "warehouse-native BI" is a posture variant of this Type, not a boundary problem.

### vs SQL Workbench / Analytical Query Editor (processed sibling)

Consistent with the recorded seams: editors author and run queries against analytical data; BI platforms curate the resulting analyses into persistent, governed, distributed content. Editors feed BI surfaces (platform dashboards); the editor's center of gravity stays query authoring. Boundary held.

### vs Data Science Workbench (sibling leaf, unprocessed)

Notebooks/code for modeling/statistics vs governed visual analytics for business consumption. Adjacent; platforms increasingly host both as sibling surfaces. → Light flag when that leaf is processed.

### vs Process Mining Platform (processed sibling)

Recorded seam honored: process mining derives case sequences and process models from event logs; BI platforms aggregate generic measures over governed data. No conflict.

### vs Enterprise AI Assistant (sibling leaf, unprocessed)

AI Q&A/insight features inside BI platforms (Copilot, Metabot, Insight Advisor Chat) are capabilities of this Type, not instances of an assistant Type; the assistant Type centers on conversational access to knowledge/tasks, not on a governed analytics repository. → Light flag when that leaf is processed.

## Uncertainties

1. **Looker not researched** (cloud.google.com timeouts ×2 this pass, ×2 in the prior pass — abandoned per network rule). The semantic-model-first philosophy is represented by Power BI/Metabase/ThoughtSpot evidence; no Looker-specific claims are made anywhere.
2. **IBM Cognos unreachable (403)** — the classic-enterprise-BI historical check is category-level inference, explicitly marked as such.
3. **Qlik depth**: structure-level evidence only (help TOC + explore-data page); selection-engine internals, load-script mechanics, and section access not verified.
4. **Tableau platform governance depth** (sites/projects/permissions/RLS specifics) not fetched; Tableau platform claims limited to the fetched pages' content.
5. **Precise vendor limits** (Power BI app audience/user caps, license tiers; Metabase display row caps from the prior pass) are product/plan-specific and kept out of the final document.
6. **Mobile/embedding coverage** varies across the sample; claims about them are scoped to products where observed.
7. **Unprocessed siblings** (dashboard-platform, reporting-platform, data-visualization-application, olap, data-warehouse-platform, data-science-workbench, enterprise-ai-assistant) — boundaries recorded here for joint review; no unilateral taxonomy change made.

## Final Synthesis

A Business Intelligence Platform is best modeled as **the governed analytics supply chain of an organization**:

```text
Connect the organization's data sources
→ prepare and (to varying depth) model the data once (shared data/semantic layer)
→ author analytics content in the product (visualizations → dashboards/reports)
→ host it persistently in an organized repository (workspaces/projects/spaces)
→ govern it (content permissions + data permissions incl. data-level security;
   certification; revision history)
→ distribute it to a defined non-authoring audience
   (publish/share/apps, links, embeds, subscriptions, alerts, mobile)
→ consumers view, filter, drill, and (within granted rights) extend
→ maintain over time (refresh data, revise content, measure usage, retire)
```

The defining core is deliberately small: connected external data + authored hosted content + consumer audience + controlled access. Everything the market associates with the category — interactive question loops, semantic/metric layers, natural-language AI, formatted reports, embedding, mobile, DevOps for content — is common mature structure or variant posture, not definition. The Type's market reality: it is the umbrella platform under which most neighboring analytics capabilities (ad-hoc querying, dashboards, reporting, even data preparation) are shipped as features, which is exactly why its definition must be structural rather than feature-based.
