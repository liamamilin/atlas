# Research Notes — Dashboard Platform

Research date: 2026-09-07
Leaf: Dashboard Platform (DIRECTORY §13 Data, Analytics & AI Systems)
Slug: dashboard-platform

## Research Goal

Determine what a Dashboard Platform is as an Application Type: its defining core, its standard capability set, its variants, and — most importantly — its boundary against the already-processed **Business Intelligence Platform** sibling, whose research pass pre-flagged this leaf as a "probable capability-slice/partial-alias (lightweight dashboard-first composition/sharing with thinner modeling/governance/repository)" (STATUS.md Boundary Issues, 2026-09-06). This pass must either confirm the alias/slice hypothesis or establish Dashboard Platform as a distinct Type with a documented seam.

## Initial Boundary

Working hypothesis before research:

- A Dashboard Platform is software whose unit of work is the **dashboard**: a composed, persistent screen of multiple data-bound visual panels that stays current as its data changes and is distributed to viewers.
- Nearest neighbors: Business Intelligence Platform (dashboards are the BI flagship artifact), Reporting Platform (document-shaped output), Data Visualization Application (single-user chart authoring), Observability/Infrastructure Monitoring (dashboards as a capability), Personal Dashboard (§03.13, life-widget lineage — different data substrate), Status Page Platform (public incident communication).
- Known unknowns: does a distinct market population exist that never grows the BI structure? Is "live/current data" definitional or merely universal today? Is "viewer audience" definitional or merely common?

## Research Questions

1. What exactly is a "dashboard" in these products — what are its parts (panels/widgets/tiles), and what binds a panel to data?
2. How do data sources connect (integrations, databases, APIs, spreadsheets, CSV)? Is external connection universal?
3. How is currency maintained (live query vs scheduled refresh)? Is "live" a market-defining claim?
4. How are dashboards distributed (links, no-login links, embeds, TV/wallboards, scheduled email snapshots, mobile)? Is a viewer audience beyond the author universal?
5. What authoring model is used (drag-and-drop widgets, query-based panels, templates, AI-built)?
6. What governance exists (roles, permissions, audit) and how thin is it vs BI?
7. What KPI/metric machinery exists (goals, targets, thresholds, status colors, alerts)?
8. What do vendors say about their own category — do they call themselves dashboard platforms, and do they explicitly distinguish themselves from BI?
9. Where does the Type drift into BI (semantic layers, metric governance, AI analysts)?
10. Would older / non-SaaS / non-cloud dashboard products still fit the definition?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Pole | Customer tier | Why sampled |
|---|---|---|---|
| Grafana | open-source, observability/ops, query-driven panels | dev/ops teams → global enterprises | the strongest dashboard-first platform; proves the Type over database/time-series data, not SaaS integrations |
| Geckoboard | team KPI visibility (TVs/Slack/email), explicitly anti-BI positioning | SMB/mid-market teams | self-describes as "real-time dashboard platform"; the cleanest statement of the display-first philosophy |
| Klipfolio Klips | KPI dashboard platform with spreadsheet-formula model, agency/client-reporting channel | SMB → agencies/partners | formula-driven authoring + deep sharing/permission machinery + white-label |
| Databox | KPI dashboards that have grown a semantic layer + AI analyst (drift pole toward BI) | SMB/mid-market, agencies | shows the drift boundary from inside: dashboards remain flagship artifact while BI structure grows around them |
| DashThis | automated marketing/client reporting dashboards | agencies, marketing teams | the most template-automated pole; dashboards as client deliverables |

Not sampled (recorded as limitation): Looker Studio, Metabase, Apache Superset/Preset (BI-adjacent dashboard-first tools), Luzmo/Cumul.io (embedded-dashboard specialists), Plecto, Scoro. The five sampled products span the poles; adding more would mostly repeat evidence.

## Sources

All fetched 2026-09-07 (Tier 1 official documentation / product surfaces):

- Grafana — "Dashboards" docs hub: https://grafana.com/docs/grafana/latest/dashboards/
- Grafana — "Build dashboards": https://grafana.com/docs/grafana/latest/dashboards/build-dashboards/
- Grafana — "Panel overview": https://grafana.com/docs/grafana/latest/panels-visualizations/panel-overview/
- Grafana — "Share dashboards and panels": https://grafana.com/docs/grafana/latest/dashboards/share-dashboards-panels/
- Geckoboard — homepage: https://www.geckoboard.com/
- Geckoboard — platform overview: https://www.geckoboard.com/product/
- Klipfolio — homepage (Klips): https://www.klipfolio.com/
- Klipfolio — "Share" feature page: https://www.klipfolio.com/features/share
- Databox — homepage: https://databox.com/
- Databox — "Dashboard Software": https://databox.com/dashboard-software
- DashThis — homepage: https://dashthis.com/

Sourcing limitations: evidence is strongest for Grafana (operational docs) and Geckoboard/Databox/Klipfolio/DashThis (product/marketing surfaces with embedded FAQ and feature documentation). Deep help-center articles for Geckoboard (support.geckoboard.com), Klipfolio (support.klipfolio.com), and Databox (help.databox.com) were not individually fetched; claims from those products are calibrated to what their fetched pages directly state. No numeric limits, refresh intervals (beyond Geckoboard's own qualitative "every few minutes" statement), or plan-tier details are carried into the final document.

## Product Observations

### Grafana (evidence layer A — operational docs)

- **Dashboard definition (vendor's own):** "a set of one or more panels, organized and arranged into one or more rows or tabs, that provide an at-a-glance view of related information."
- **Panel:** "a visual representation of data composed of a query and a visualization"; transformations process query results before visualization; per-data-source query editor; panels can be dragged, dropped, resized.
- **Data sources:** SQL databases, Loki, Mimir, API endpoints, CSV files; 150+ data source plugins; "query, transform, visualize, and understand your data no matter where it's stored."
- **Dashboard machinery:** variables (interactive/dynamic dashboards), library panels (reusable across dashboards), version history, annotations, dashboard links, JSON model, import/export, folders, generative AI features for dashboards.
- **Time:** dashboard-level time range; panel-level overrides, time shift, time comparison; pan/zoom on time-series panels.
- **Panel configuration:** thresholds, value mappings, field overrides, legends, tooltips, data links.
- **Sharing:** internal links (viewer permission required), externally shared dashboards (managed list), scheduled reports (Enterprise), snapshots (public link, sensitive data such as queries stripped, expiration options), PDF export (Enterprise), JSON export ("as code"), PNG image export (image renderer), iframe embeds (Enterprise/OSS + anonymous access), community dashboard catalog (publish/import).
- **Alerting:** alert rules can be created from panel queries.
- **Exploration:** "Explore" surface (query-focused ad-hoc exploration) reachable from panels; metrics drilldown.

### Geckoboard (evidence layer A — product pages with embedded FAQ)

- **Self-positioning:** "KPI dashboard software"; "real-time dashboard platform built to share performance on TVs, in Slack, by email and on mobile. No BI team required!" Explicit FAQ: "Is Geckoboard a BI tool? No. BI tools are built for analysts to explore data. Geckoboard is a real-time dashboard platform…"
- **Anti-report framing:** "Reports explain what happened. Geckoboard changes what happens next." Live team view vs last week's PDF report comparison on the homepage.
- **Connect:** 90+ integrations (Salesforce, HubSpot, Zendesk, Aircall, Google Sheets, Intercom, Shopify, GA, Google Ads, Jira, Monday, Excel, Zapier, Pipedrive, LinkedIn…); spreadsheets; API for custom metrics; multiple accounts per service.
- **Build:** drag-and-drop widgets; "one clear number with a goal, built in minutes and readable by anyone"; filters; combine data from different sources on one dashboard; no developer/analyst required.
- **Make visible:** TVs/wallboards (any TV with a browser; remote screen management; rotation loops between dashboards), Slack, Teams, email, mobile, live links (no login required), embeds.
- **Scheduled snapshots:** automatic dashboard snapshots to email/Slack/Teams on day/week/shift schedules.
- **Alerts:** threshold on any KPI → notify people in Slack/Teams.
- **Understand:** drilldowns to source data; click-through to CRM/support tool to act.
- **Motivate:** goals, status indicators, gamification, leaderboards, celebrations.
- **Currency:** "Most integrations refresh automatically every few minutes. Where real-time is essential… we update within a few seconds."
- **Access:** free view-only users; per-dashboard sharing to specific people; Enterprise: SSO, audit logs.
- **AI:** Metrics for AI (MCP) — external AI clients query Geckoboard's metrics engine so answers match the dashboards.

### Klipfolio Klips (evidence layer A — product pages)

- **Self-positioning:** "Spreadsheet power with dashboard clarity"; "a complete dashboard solution that automates data retrieval and offers limitless dashboard presentation and distribution options."
- **Connect:** 200+ services; SQL/REST query connectors; Excel/Sheets; "works great with or without a data warehouse."
- **Build:** 30+ chart types, thousands of styling combinations, infinite custom layouts, pixel-level control, dark mode, white-label, drill-down, Klip comments; spreadsheet-formula model (the product's signature).
- **Data machinery:** automatic data refresh, refresh scheduling, dynamic data sources, debugging tools, asset management API.
- **Share:** roles (admins/editors/viewers), group-based access (edit or view rights), SSO, access control at data source / Klip / dashboard level; mobile/desktop/TV surfaces; scheduled email reports (PDF or image snapshots, one-time or scheduled); public or password-protected dashboard links; embedded Klips (external websites/host applications); distribute dashboards into 100s of client accounts (agency model); audit logs and usage tracking.
- **Templates:** client dashboard templates; curated template library; dashboard examples per function (finance/executive/sales/SaaS/marketing/social).

### Databox (evidence layer A — product pages with embedded FAQ)

- **Self-positioning (current):** "agentic analytics platform" — the company has grown beyond dashboards; but "Dashboards & Reports" remains a flagship pillar alongside Metrics & KPIs and Goals & OKRs.
- **Dashboard builder:** drag metrics ("datablocks") onto a dashboard canvas; AI Analyst builds dashboards from a description; 218 prebuilt templates (marketing/sales/support/ecommerce/PM/financial/dev/SaaS); flexible visualizations (toggle chart types); custom branding + white-label add-on.
- **Analyze:** filter/break down by dimension (campaign/channel/segment) in one click; drill down to individual records behind a metric; period comparison (last month/quarter/year).
- **Share:** public shareable link (always current data, no login required); stream to TV (smart TV); scheduled snapshots (PDF/JPG to email/Slack on a schedule); embeds (web pages, ClickUp/Notion).
- **Dashboard vs report (vendor's own distinction):** "Dashboards show live, real-time performance, best for month-to-date or week-to-date tracking. Reports are built for deeper analysis of historical periods… typically sent as a PDF or scheduled email."
- **BI-structure growth (drift evidence):** 130+ integrations; semantic layer ("give every metric a shared meaning"); data governance (metric definitions, ownership, access); permission-aware AI; Goals & OKRs; AI Analyst ("Genie") answering questions, building dashboards, explaining changes; agents & automations; MCP.
- **Packaging:** free-forever plan; unlimited dashboards on all plans.

### DashThis (evidence layer A — product pages)

- **Self-positioning:** "an automated marketing reporting dashboard software that integrates data from over 30 platforms to create branded, client-ready dashboards."
- **Connect:** 30+ marketing platforms (GA4, Google Ads, Search Console, Meta, LinkedIn Ads/Pages, TikTok, YouTube, Ahrefs, SEMrush, Moz, Bing Ads…); CSV import for custom data.
- **Build:** ready-made report templates per channel (SEO/social/PPC/ecommerce); preset widgets and KPI bundles; clone dashboards and reuse templates across clients; calculated widgets; section headers and comments; preset color themes.
- **Share:** scheduled email dispatch; real-time dashboard access for clients; white-label (custom report URLs, color themes, branded widgets).
- **AI:** AI Insights (one-click wins/drops/opportunities); AI Insights Pro (chat mode, client-tailored explanations).
- **Packaging:** unlimited users on every plan; per-dashboard pricing; 14-day trial.

## Cross-product Comparison

| Dimension | Grafana | Geckoboard | Klipfolio Klips | Databox | DashThis |
|---|---|---|---|---|---|
| Unit of work | dashboard (panels in rows/tabs) | dashboard (widgets) | dashboard (Klips) | dashboard ("databoard" of datablocks) | dashboard (widgets/KPI bundles) |
| Data connection | 150+ datasource plugins (DBs, APIs, CSV) | 90+ SaaS integrations + sheets + API | 200+ services + SQL/REST + sheets | 130+ integrations + sheets + DBs + APIs | 30+ marketing platforms + CSV |
| Panel↔data binding | query per panel (+ transformations) | metric selection per widget | formula per Klip | metric/datablock per tile | preset KPI widgets |
| Currency | live queries | auto refresh (minutes; seconds where possible) | automatic refresh + scheduling | real-time/live | automatic refresh |
| Time controls | dashboard + panel time range, shift, comparison | period widgets | period settings | period comparison | date ranges per report |
| Goals/targets/status | thresholds, value mappings | goals, status, leaderboards, celebrations | custom indicators | goals & OKRs module | KPI bundles |
| Alerts | alert rules from panels | threshold → Slack/Teams | (not surfaced on fetched pages) | monitoring/goals | (not surfaced) |
| Sharing | links, external links, snapshots, embeds, PDF, JSON, image, reports, community catalog | TVs, Slack/Teams/email, live links (no login), mobile, embeds | roles/groups/SSO, TV/mobile/desktop, scheduled email PDF/image, public/password links, embeds, client accounts, audit | public link (no login), TV streaming, scheduled snapshots, embeds | scheduled email, client access links, white-label URLs |
| Templates/library | template dashboards, community catalog, library panels | dashboard examples | client templates, curated library | 218 templates | channel templates, KPI bundles |
| Governance depth | folders, viewer permission, (Enterprise) datasource permissions | per-dashboard sharing, view-only users, SSO/audit (Enterprise) | roles/groups, source/Klip/dashboard-level access, audit logs | permission-aware access, metric governance | unlimited users, client scoping |
| Modeling layer | per-panel transformations (no shared semantic layer) | none (metrics engine per integration) | per-Klip formulas (no shared semantic layer in Klips) | semantic layer + metric governance (BI-grade) | calculated widgets only |
| Ad-hoc exploration | Explore surface | drilldown + click-through | drill-down | drilldown + AI analyst | AI insights |
| White-label | no (community catalog instead) | not surfaced | yes | yes (add-on) | yes (core feature) |
| Deployment | OSS self-host / Enterprise / Cloud | SaaS | SaaS | SaaS | SaaS |
| AI | generative dashboard features, assistant | MCP metrics access | separate product (PowerMetrics) | AI Analyst, agents, MCP | AI insights (+Pro chat) |

### Cross-product commonalities (evidence layer B)

Present in all five sampled products:

1. **Connected external data sources** — every product defines itself by connecting to data that lives elsewhere (SaaS tools, databases, APIs, spreadsheets, CSV).
2. **Dashboard as a persistent composed display** — a named, saved screen of multiple data-bound panels/widgets arranged on one surface; not a throwaway chart.
3. **Currency** — the display stays current as its data changes (live query or automatic refresh); no product requires manual re-export to update.
4. **Distribution to viewers beyond the author** — links (including no-login links in four of five), embeds, TV/wallboard surfaces, scheduled email snapshots (PDF/image), mobile.
5. **Time dimension** — period selection and comparison are built into the dashboard view.
6. **KPI/status orientation** — numbers with targets, thresholds, status colors, or progress indicators.
7. **Templates/examples** — every product ships template galleries or community/example libraries.
8. **Export/snapshot output** — PDF/image/JSON exports or scheduled snapshot delivery.

Present in most (common, not definitional):

9. Threshold alerts pushed to chat/notification channels (Grafana, Geckoboard, Databox; not surfaced for Klipfolio/DashThis on fetched pages).
10. Drilldown to underlying data / click-through to source tools (Grafana inspect, Geckoboard, Klipfolio, Databox).
11. White-label/branding (agency pole: Klipfolio, Databox, DashThis).
12. AI assistance (era-common: all five in some form).
13. Version history / import-export of dashboard definitions (Grafana explicit; others not surfaced).

### What is absent relative to BI platforms (the negative space)

Across the display-first products (Geckoboard, DashThis, and largely Klipfolio Klips):

- no shared semantic/model layer (metrics defined per widget/panel, not once for the organization);
- no broad artifact estate (no paginated report authoring, no story/narrative formats as first-class artifacts);
- no data-prep/ETL surface;
- no certification/endorsement workflows for content;
- no data-level security (row/column filtering by viewer identity) — access control stops at content/source level;
- no analyst-grade ad-hoc exploration loop as the primary surface (drilldown exists; free composition does not).

Databox is the exception that proves the drift boundary: it has grown a semantic layer, metric governance, and an AI analyst — i.e., it is growing the BI structure while dashboards remain the flagship artifact.

## Canonical Model (L0–L3)

### L0 — Defining Invariant

```text
Connected external data sources
└── Dashboard: a persistent composed display surface
    of multiple data-bound panels
    └── Kept current as its data changes
        (live query or automatic refresh)
        └── Distributed to viewers beyond the author
```

Four properties. Removal tests:

- Remove **connected external data** → a mockup/design tool or a hand-maintained page; not a data dashboard platform. (All five products define themselves by connection.)
- Remove **composed multi-panel persistent display** → a chart builder / single-visualization tool (Data Visualization Application territory).
- Remove **currency** → a static report or snapshot; the artifact becomes a document consulted after the fact (Reporting Platform territory). The dashboard's essence is a standing display consulted in place.
- Remove **viewers beyond the author** → single-user authoring software; the "platform" aspect (serving an audience) disappears.

Historical/market-sample check (per §24): the definition must not require SaaS integrations, TV mode, cloud delivery, or AI. 1990s executive-information-system dashboards (multi-panel shared displays over database/mainframe feeds, periodically refreshed) satisfy the core; early-2000s portal-era and BI-suite dashboards satisfy it; a hand-updated production wall board satisfies the *display* concept but not the *platform* (no software plumbing) — the software Type begins where the platform maintains the display. The definition holds.

### L1 — Common Mature Structure

- Panel/widget vocabulary: KPI number cards, time series, tables, gauges, leaderboards, top-N lists
- Time-range control and period comparison built into the view
- Goals/targets with progress and status indicators (threshold colors)
- Threshold alerts delivered to chat/notification channels
- Drilldown to underlying records; click-through to source tools
- Template galleries / example libraries / community catalogs
- Scheduled snapshot delivery (PDF/image to email/chat)
- TV/wallboard mode and mobile surfaces
- Embeds (iframe) and public no-login links
- Version history; import/export of dashboard definitions; reusable panel/component libraries
- Variables/filters for interactive dashboards
- Comments/annotations for context
- White-label/branding (agency-facing products)
- AI assistance (build-from-prompt, explain-changes, metrics access for external AI clients)

### L2 — Variant / Optional Structure

- **Data substrate:** SaaS business tools (Geckoboard/Databox/DashThis) vs databases/time-series/observability sources (Grafana) vs spreadsheets/CSV as first-class sources
- **Audience:** internal team visibility vs client/agency reporting (white-label, per-client dashboards) vs ops/observability teams
- **Analytics depth:** pure display (Geckoboard/DashThis) vs formula-driven per-panel modeling (Klips) vs metric-managed with semantic layer (Databox — drift pole)
- **Delivery:** cloud SaaS vs open-source self-hosted + commercial editions (Grafana)
- **Refresh posture:** live query vs scheduled integration refresh vs hybrid
- **Business model:** freemium/free-forever, per-dashboard pricing, per-user, open-source core + enterprise tier
- **Embedded distribution:** dashboards embedded into other products/web pages as a first-class channel

### L3 — Vendor-specific (research notes only)

- Grafana: panels/rows/tabs JSON model; library panels; Explore; annotations; snapshots.raintank.io; community dashboard catalog; Enterprise-gated PDF/reports/external-sharing/anonymous access; datasource plugin architecture; panel time settings (public preview); view-panel sidebar fan-out.
- Geckoboard: TV screen management with rotation loops; celebrations/gamification/leaderboards; Metrics for AI (MCP); Geckoboard for Zendesk packaged product; "every few minutes" refresh statement.
- Klipfolio: Klip formula model (spreadsheet functions per visualization); client-account import for agencies; PowerMetrics as a separate next-gen product; access control scoped at data source/Klip/dashboard levels.
- Databox: "Datablocks"/"Databoards" terminology; AI Analyst "Genie"; Skills Marketplace; Goals & OKRs module; universal semantic layer; free-forever plan; unlimited dashboards.
- DashThis: KPI bundles; white-label report URLs; AI Insights Pro chat mode; per-dashboard pricing; unlimited users on all plans.

## Vendor-specific Findings

See L3 above. None of these are promoted to the canonical model. The most consequential: Databox's semantic layer and metric governance demonstrate that the drift from Dashboard Platform toward BI Platform happens *by addition* (modeling + governance + artifact breadth), while the dashboard artifact remains the center — this is the observable mechanism behind the BI pass's "capability-slice" hypothesis.

## Boundary Findings

### vs Business Intelligence Platform (the pre-flagged joint review — discharged from this side)

The BI pass hypothesized: "dashboards are the BI flagship artifact, so Dashboard Platform is a probable capability-slice/partial-alias (lightweight dashboard-first composition/sharing with thinner modeling/governance/repository)."

This pass's verdict: **Dashboard Platform is a distinct sibling Type, not an alias** — but the seam is real and must be documented on both sides.

Evidence for distinctness:

1. A sustained market population exists whose products never grow the BI structure: Geckoboard ("Is Geckoboard a BI tool? No."), DashThis (template-automated client dashboards, no modeling), Klipfolio Klips (formula-per-panel, explicitly "with or without a data warehouse"). These are stable, commercially successful products, not immature BI.
2. The market itself draws the line: Geckoboard publishes a point-by-point BI comparison ("Do you need BI, or do you need visibility?") and Databox documents a dashboard-vs-report distinction. Vendors police this seam.
3. The center of gravity differs: BI's defining core is the governed artifact lifecycle (authored content + hosted repository + consumer audience + content-and-data access control) with a broad artifact estate and a shared model layer. The Dashboard Platform's defining core is the dashboard artifact itself with the connect→compose→keep-current→distribute loop. A dashboard platform can be described entirely without the BI core's modeling/repository/governance depth; a BI platform cannot be described without its repository/governance even though it ships dashboards.

Structural tests (both directions):

- Strip a BI platform to dashboard composition + sharing with thin modeling/governance → you have a Dashboard Platform (this is what the lightweight pole is).
- Add a shared semantic/model layer, a broad governed artifact estate, and deep content+data governance to a Dashboard Platform → you have a BI Platform (this is Databox's trajectory, observable in its own product architecture).

So: partial capability overlap (BI ships dashboards as flagship artifact; dashboard platforms are the display-first slice of the analytics family), but not an alias — the display-first population is self-sustaining and vendor-acknowledged. Recommendation to taxonomy owner: keep both Types; document the seam symmetrically (BI document already does; this document adds the other side).

### vs Reporting Platform

Dashboard = standing live display consulted in place; report = document-shaped point-in-time output delivered to an audience. The seam: dashboard platforms ship **scheduled snapshots** (PDF/image to email/chat) — report-shaped delivery as a *capability* (all five products have some form). Databox's own FAQ draws the line: dashboards = live month-to-date/week-to-date tracking; reports = historical periods delivered as PDF/scheduled email. Removal test: if the document-shaped output and its delivery become the center of gravity, the product is a Reporting Platform.

### vs Data Visualization Application

Single-user or file-based chart authoring vs a platform that maintains connected, current, shared displays. Removal test: remove the viewer audience + currency + connection plumbing → Data Visualization Application.

### vs Ad-hoc Query Application

Dashboards are persistent standing displays; the ad-hoc loop is question-time composition (compose → run → refine). Grafana's Explore and Databox's AI Analyst are the ad-hoc loop appearing as a *capability* inside dashboard-first products — the same bundling pattern the BI pass documented. Removal test: center the loop, drop the standing display → Ad-hoc Query Application.

### vs Observability / Infrastructure Monitoring (§14)

Monitoring products add detection, alerting, incident machinery over telemetry as their core; dashboards are one of their surfaces. Grafana is the boundary case: dashboard-first architecture serving the observability world. Verdict: Grafana satisfies the Dashboard Platform core (connected sources, composed panels, currency, distribution) and is treated as the observability-flavored pole of this Type; monitoring products whose center is detection/response belong to §14 Types even though they ship dashboards.

### vs Personal Dashboard (§03.13)

Different data substrate and audience: personal life widgets (tasks, calendar, habits) vs organizational/business data displayed to a team. The shared word "dashboard" is a surface metaphor, not a shared core.

### vs Status Page Platform (§14)

Public incident/service-status communication with subscriber notifications vs internal/organizational data display. Different audience contract (public trust communication vs internal visibility).

### vs Embedded-analytics products

Embedding dashboards into other applications is a distribution capability of this Type (Klipfolio embeds, Databox embeds, Grafana embeds). Specialist embedded-dashboard vendors (not sampled) would be a variant pole of this Type, not a separate one, unless research shows their core differs.

## Uncertainties

1. **Refresh mechanics per product** — only Geckoboard states refresh behavior qualitatively ("every few minutes; seconds where possible"). Others were not verified at help-center depth; the final document says only "live query or automatic refresh."
2. **Alerts in Klipfolio/DashThis** — not surfaced on the fetched pages; recorded as "not surfaced," not "absent."
3. **Geckoboard white-label** — not surfaced; excluded from cross-product claims.
4. **BI-adjacent dashboard-first tools** (Looker Studio, Metabase, Superset) not sampled; the BI↔Dashboard seam is documented from the five sampled products plus the BI pass's evidence. Risk: those tools may blur the seam further (they are BI platforms with dashboard-first UX). Does not affect the L0.
5. **Embedded-dashboard specialists** (Luzmo/Cumul.io) not sampled; the embedded pole is documented structurally (embedding as capability), not from a specialist product.
6. **Market label usage** — "dashboard platform" as a self-label is directly evidenced only at Geckoboard ("real-time dashboard platform"); others use "dashboard software/solution." The Type name is the directory's, not a uniform vendor label.

## Final Synthesis

A Dashboard Platform is an organizational display system: it connects to data sources the organization already uses, lets users compose dashboards — persistent screens of multiple data-bound panels — keeps those displays current automatically, and distributes them to the people who need to see them (on screens, TVs, chat tools, inboxes, phones, or embedded surfaces), under permissions that separate builders from viewers.

Its defining core is small: connected external data + composed persistent dashboard + currency + viewer distribution. Everything else — KPI goals, alerts, templates, TV mode, snapshots, white-labeling, AI — is standard capability that makes the display practical and reachable, not what makes it a dashboard platform.

The Type sits between the Data Visualization Application (authoring without audience) and the Business Intelligence Platform (governed analytics estate with modeling and repository). The market sustains it as a distinct pole: display-first products that never grow the BI structure, serving teams whose need is visibility ("see what's happening now") rather than analysis ("explain what happened"). The BI pass's capability-slice hypothesis is therefore only partially confirmed: the overlap is real, but the display-first population is self-sustaining and vendor-acknowledged, so the leaf stands as a distinct Type with a documented seam.
