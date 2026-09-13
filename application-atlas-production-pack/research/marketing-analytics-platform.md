# Research Notes — Marketing Analytics Platform

## Research Goal

Understand the software Type placed at directory leaf "Marketing Analytics Platform" (§06 Marketing, Advertising & Growth): applications through which an organization (marketing team, agency, data team) measures the performance of its own marketing across channels and campaigns — consolidating data from many marketing platforms into one unified view, computing cross-channel marketing metrics, and surfacing dashboards/reports that inform marketing decisions and stakeholder/client reporting. Determine the defining core, the standard capability set, the variant poles, and the boundaries against neighboring Types (Social Media Analytics Platform §06 processed, Marketing Attribution Platform §06 unprocessed, Marketing Mix Modeling Application §06 unprocessed, Business Intelligence Platform §13 processed, Dashboard Platform §13 processed, Conversion Rate Optimization Platform §06 processed, Marketing Automation Platform §06 unprocessed, Marketing Campaign Management Platform §06 unprocessed, web analytics [no directory leaf], Data Integration/ETL §13).

Context from prior passes that this pass must address:

- research/social-media-analytics-platform.md (§06, processed 2026-09-07) positioned "Marketing Analytics Platform §06 — whole-funnel measurement vs channel-specific social measurement" as a neighboring Type and left the seam to this pass. This pass discharges that flag from this side.
- research/business-intelligence-platform.md and research/dashboard-platform.md (§13, processed) established the BI/dashboard seams; Databox's current self-label drifts into "BI / agentic analytics", so the BI seam must be handled head-on.
- STATUS.md Boundary Issues (performance-attribution-platform pass, §08) recorded an "attribution" naming hazard and recommended the §06 attribution leaf's pass state the mirror-side distinction — that obligation belongs to the marketing-attribution-platform pass, not this one; this pass records the analytics-vs-attribution seam only.

## Initial Boundary

Working hypothesis before research:

- The Type is the **cross-channel marketing measurement application**: the operator is a marketing team, agency, or data team; the measured subject is the organization's **own marketing performance** (channels, campaigns, spend, outcomes); the deliverable is a unified cross-channel view + marketing KPIs + dashboards/reports.
- The reason the Type exists: no single marketing platform reports the whole picture — each ad/social/email/SEO platform reports only itself, with its own metric definitions — so a product that consolidates the stack into one normalized view and computes cross-channel KPIs is doing something none of the sources do.
- Likely confusions:
  1. Social Media Analytics Platform (§06, processed) — channel-specific measurement (social profiles) vs whole-stack measurement.
  2. Marketing Attribution Platform / Marketing Mix Modeling Application (§06, unprocessed) — credit-assignment modeling and aggregate spend-effect modeling vs performance measurement/reporting.
  3. Business Intelligence Platform / Dashboard Platform (§13, processed) — generic analytics/display vs marketing-domain packaging.
  4. Conversion Rate Optimization Platform (§06, processed) — visitor-behavior diagnosis loop vs channel-performance measurement.
  5. Marketing Automation / Marketing Campaign Management (§06, unprocessed) — execution vs measurement.
  6. Web analytics (GA-class; no directory leaf) — site/app behavior measurement; a data source for this Type.
  7. Data Integration/ETL Platform (§13) — generic pipelines vs marketing-specific consolidation + analytics surface.
- Unknowns going in: (a) is multi-source consolidation definitional or just universal implementation; (b) is the interpretation/reporting surface definitional or can a pure pipeline qualify; (c) are marketing KPI semantics (ROAS/CPA-class ratios, channel/campaign dimensions) part of the core or just common; (d) how deep the documented data physics goes (freshness, aggregation rules, backfill).

## Research Questions

1. What is the central measured object — the channel, the campaign, the account, the metric, the client?
2. How does data enter the system — connectors/APIs, file imports, warehouses, own collection tools? What is the connection object model?
3. What does the platform do to the data — normalize, map to a shared model, blend, currency-convert, deduplicate?
4. What marketing metrics/KPIs are computed, and what metric semantics are documented (aggregatability, freshness, source-owned definitions)?
5. What surfaces exist — dashboards, reports, explorers, KPI tables, roll-ups, AI answers — and who consumes them (marketers, clients, executives, data teams)?
6. How do agency-specific structures work (client containers, white-label, roll-ups, scheduled client reports)?
7. Where do attribution/MMM sit relative to this Type — core, optional module, or separate product?
8. Where is the seam vs social-media analytics, BI, dashboard platforms, CRO, marketing automation, web analytics?
9. Which capabilities are definitional vs common vs optional vs vendor-specific?
10. Would older/manual implementations (spreadsheet-consolidated marketing reports) still satisfy the definition?

## Representative Products

Selected for market representation + documentation completeness + different product philosophy + different customer tier:

| Product | Pole | Customer tier | Evidence tier reached |
|---|---|---|---|
| **Funnel** (funnel.io) | data-hub/pipeline-first ("marketing data hub" / "marketing intelligence platform") | mid-market/enterprise (marketers + data teams + agencies) | Tier 1 (help center: "What is Funnel?", "Connector, platform account and data source", "What are non-aggregatable metrics?", "Data freshness") + Tier 2 (root) |
| **Improvado** | enterprise pipeline-first with governance + AI layer ("marketing agentic OS" / "reporting layer for marketing teams") | enterprise (brands, agencies, regulated industries) | Tier 1 (docs section structure: Extracting/Transforming/Loading/Governance/BI) + Tier 2 (root) |
| **Databox** | dashboard/KPI-first, self-serve (current self-label: "agentic analytics platform" / "BI & analytics software" — drifted from its earlier marketing-analytics label) | SMB/growing businesses + agencies | Tier 1 (KB structure + "Understanding datasets") + Tier 2 (root) |
| **AgencyAnalytics** | agency client-reporting-first ("client reporting and performance insights for marketing agencies") | agencies (7,000+ claimed) | Tier 1 (KB structure + "Tracking KPIs" + "Roll-up Table") + Tier 2 (root) |

Rejected/unreachable samples (recorded, no claims made):

- **Whatagraph / NinjaCat / TapClicks / DashThis / Supermetrics / Adverity** — additional reporting-first and connector-first candidates not fetched; the four sampled products already cover both poles and both customer tiers, and further samples would mostly repeat existing evidence.
- **Databox's earlier "marketing analytics software" positioning** — current site self-labels BI/agentic; the drift itself is recorded as evidence (see Boundary Findings), not treated as a defect of the sample.

## Sources

Fetched 2026-09-08. All direct from official vendor surfaces.

- Funnel root — https://funnel.io/
- Funnel — "What is Funnel?" — https://help.funnel.io/en/articles/8020917-what-is-funnel
- Funnel — "Connector, platform account and data source" — https://help.funnel.io/en/articles/13616444-connector-platform-account-and-data-source
- Funnel — "What are non-aggregatable metrics?" — https://help.funnel.io/en/articles/2624615-what-are-non-aggregatable-metrics
- Funnel — "Data freshness" — https://help.funnel.io/en/articles/5745199-data-freshness
- Funnel help center root (collection/article structure) — https://help.funnel.io/en/
- Improvado root — https://improvado.io/
- Improvado Documentation root + Extracting data + Transforming data sections — https://improvado.io/help , https://improvado.io/docs-section/data-extraction , https://improvado.io/docs-section/transformations
- Databox root — https://databox.com/
- Databox Knowledge Base root — https://help.databox.com/ , https://help.databox.com/docs
- Databox — "Understanding datasets" — https://help.databox.com/understanding-datasets
- AgencyAnalytics root — https://www.agencyanalytics.com/
- AgencyAnalytics Help Center root — https://agencyanalytics.com/help-center , https://help.agencyanalytics.com/en
- AgencyAnalytics — "Tracking KPIs in AgencyAnalytics" — https://help.agencyanalytics.com/en/articles/15382468-tracking-kpis-in-agencyanalytics
- AgencyAnalytics — "Monitor Performance Across All Your Clients with the Roll-up Table" — https://help.agencyanalytics.com/en/articles/10034853-monitor-performance-across-all-your-clients-with-the-roll-up-table

Unreachable/unused: databox.com/marketing-analytics (404 — URL guess; root + KB used instead). No third-party review sites used.

## Product Observations

### Funnel (evidence layer A — official help center Tier 1 + root Tier 2)

**Positioning.** Root: "The leading marketing intelligence platform… The marketing data foundation your teams can rely on." Help center: "Funnel is a browser-based marketing data hub where you can connect, store, organize, visualize, and share marketing data in an automated way… a single source of truth… the control center for monitoring and improving marketing performance."

**Product lines.** Funnel Data Hub (connectors, semantic layer, currency conversion, built-in dashboards, Funnel AI and MCP) and Funnel Measure (Marketing Mix Modeling, Multi-Touch Attribution, incrementality testing, budget optimization, scenario simulation) — measurement modeling is a **separate product line** from the data hub. Use cases: centralize marketing data, automate reporting, enable measurement ("clean data ready for MMM and attribution"), power AI workflows, deliver data to a warehouse, build data products. Teams: marketers, data teams, agencies.

**Building blocks (help article).** Connect (500+ marketing apps; "simply enter your credentials"), Store ("store 24 months of marketing data"), Organize ("transform raw data without code… clean, group, and map… normalize, harmonize, and enrich"), Visualize ("customizable, easy-to-create dashboards for reporting and KPI monitoring"), Share ("dashboards, industry-leading visualization tools, or data warehouses"). Who: digital marketers, marketing analysts, data analysts, IT administrators.

**Connection object model (help article — the strongest single source).** A documented 3-tier hierarchy:

- **Connector** — "Funnel's built-in integration that links your workspace to an external platform, such as Facebook Ads, Shopify or Google Analytics 4… The connector itself doesn't contain any data. It's only a gateway… You cannot delete a connector, and the number of connectors you get vary based on your plan." Custom connectors via data request.
- **Platform account** — "the specific account, property, store or view that you own or manage within a data source platform. It's the entity that holds your marketing data." Platforms name it differently (Google Ads ad account, Shopify store, GA4 property); multiple platform accounts per connector (multi-brand/multi-client example documented).
- **Data source** — "a specific configuration you create from a platform account… defines which metrics and dimensions you want to pull, how you want it structured, and any filters you apply." Multiple data sources per platform account.
- Flow: "Choose a connector > Link platform accounts > Create data sources." Connectors and platform accounts consume "flexpoints" (usage unit).

**Metric semantics (help articles).**

- **Non-aggregatable metrics**: ratio metrics (CPC) must not be averaged across periods ("the naïve approach ended up exaggerating my actual CPC with 32%"); unique-count metrics (Reach) must not be summed across campaigns/dates (person counted twice); "The only way to accurately perform data aggregation… is to have access to the most granular breakdown possible… Very few advertising platforms allow access to this data." Funnel marks such metrics non-aggregatable.
- **Data freshness**: "how up-to-date a set of data is… will depend heavily on… the types of metrics… the platform itself… change to recent data is to be expected… Funnel continuously downloads new data from platforms, in most cases several times per day." Quotes platform docs (Google Ads, X Ads, Bing, LinkedIn) on per-platform freshness and revision of recent data; rate limits & quotas considered.
- Other documented data physics: currency conversion; date/time-zone handling; historical-data gaps after reconnecting; double-counting avoidance in Data Explorer; file import / Google Sheets / webhook / email import as data-source types; connecting the same source twice with different dimensions; reduced download frequency for empty accounts; per-connector "Dimensions and metrics" reference articles for hundreds of platforms (ad platforms, social organic, affiliate networks, email, CRM, ecommerce, call tracking, app measurement).

**Interfaces.** Data Explorer (views, currency switching), Organize (custom metrics via rules/formulas — e.g., documented ROAS custom metric; custom dimensions via regex/lookups; datasets), Budgets, Conventions (governance), destinations (warehouses/BI), Funnel AI (workspace instructions, skills, prompt library), Funnel MCP (external LLM access "using the same definitions your reports run on"), Funnel as Code (version-controlled setup, private beta).

### Improvado (evidence layer A for docs structure — Tier 1; layer A for positioning — Tier 2 root)

**Positioning (root).** "Your marketing agentic OS… The reporting layer for marketing teams that have outgrown their spreadsheets, their dashboards, and their patience." Platform stages: Data Extraction and Loading ("gather data from online and offline sources") → Data Ownership ("centralize all your data into one trusted warehouse") → Data Transformation ("get a quality dataset ready for further analysis") → Marketing Data Governance ("get notified of any data, campaign or ops issues") → Reporting & Insights → AI Agent. Claims: 1,000+ connectors, 46K+ metrics unified, "map every channel to one shared model… channels, campaigns, and metrics in a single structure."

**Docs structure (Tier 1).**

- Extracting data: Connect your data; Data sources; Connected sources; Set up data extraction; **Improvado Data Dictionary** ("an extensive overview of all common Report types by data sources. It includes metrics, properties, dimensions"); Extraction templates; Custom Configuration flow; Extraction orders; Data tables; Best practices; Product Models; Monitor Data (Dataflow Dashboard, Billing Dashboard).
- Transforming data: Build Transformation; Recipe Templates; **Cross-Channel Wizard** ("simplify data modeling with an intuitive, step-by-step flow"); Analyze Transformation; Transformation Use Cases; AI Agent for Transformation.
- Loading data: Set up data load; Destinations; Monitor Data.
- Marketing Data Governance: Naming Convention; Build Rules; Review Compliance; Assign Account Owner; Acknowledge Violations; Discovery API Rules; Budgets Feature Overview.
- AI-Native Business Intelligence (AI Dashboards); Creative Analytics Intelligence; Administrative (Workspaces, Members, SSO); Service Desk.

**Roles/industries.** Marketers, Analysts, Leadership; brands, agencies, entertainment, retail, healthcare, finance, etc. MMM listed as a use case/solution (adjacent, not the center).

### Databox (evidence layer A for KB/datasets — Tier 1; layer A for positioning — Tier 2 root)

**Positioning (root).** "Agentic analytics platform… Business Intelligence & Analytics Software." Structure: Integrations ("Connect 130+ tools, spreadsheets, databases, and APIs") → Semantic layer ("give every metric a shared meaning") → Data governance → Metrics & KPIs ("build, monitor, and forecast the metrics that matter") → Dashboards & Reports ("visualize performance and share clear updates with anyone", no-login sharing) → Goals & OKRs → Agentic analytics (AI Analyst "Genie", Agents & automations, MCP). Compares itself vs Looker Studio, Tableau, Power BI, Klipfolio, Supermetrics, Geckoboard, Qlik, DashThis, **AgencyAnalytics**. Who we help: agencies, growing businesses, AI implementers. Setup flow: "Connect your data → Define & Govern → Analyze with AI → Report & Share → Automate & Delegate."

**KB structure (Tier 1).** Account Management; AI (Genie); **Data Management (connections, data sources, datasets, sync settings)**; Databoards; Forecasts; General (visualization types, templates); Goals; **Integrations ("Connect 100+ tools: CRM, ads, analytics, cloud warehouses, and more")**; Metrics (custom metric library); Mobile; Notifications (alerts, scorecards, scheduled snapshots); Reports ("create, schedule, and share automated performance reports").

**Datasets (help article).** "A dataset is a custom table of data, where each row represents an individual record from the data source, and each column defines a specific field." Flow: "One or more data sources are added through an integration → one or more datasets are created from a data source → datasets can be exported as-is or used to create custom metrics via the metric builder." Use cases: filtered views, multi-step calculations, segmented analysis, combining data points, custom aggregations, **merging/joining data across sources ("blending CRM data with product analytics")**, custom date windows, niche KPIs. Documented data physics: "Some providers deliver analytical data through predefined metrics, which typically consist only of dates and numerical values. These metrics lack the underlying raw records… difficult, if not impossible, to break down, filter, or merge with other data sources" — Databox "prioritize[s] developing integrations that offer flexible and granular data."

### AgencyAnalytics (evidence layer A — official help center Tier 1 + root Tier 2)

**Positioning.** "Client reporting and performance insights for marketing agencies… Connect every data source, uncover what matters, and turn insights into reports, dashboards, and better client conversations." Product menu: Connect your data (Integrations "85+ marketing platforms" categorized SEO 14 / Paid Advertising 12 / Social Media 16 / Ecommerce 9 / Database 5; Client Knowledge; MCP Server) → Analyze performance (AgencyAI, Dashboards, Metrics) → Share results with clients (Reports, Client Portal, White Label) → Track visibility (Rank Tracker, AI Tracker — own data-collection tools). Also: anomaly detection, benchmarks, forecasting.

**KB structure (Tier 1).** Getting Started (7); Manage Your Clients (6); **Connect Your Data (109 articles)**; Account & Setup (30); **Build Reports & Dashboards (28)**; Customize Your Branding (4); **Analyze Your Data (26)**; News & Updates.

**KPIs (help article).** "KPIs give you a single place to track, target, and monitor the metrics that matter most to your clients… available at both the account and client levels… replace[d] the previously separate Goals and Alerts sections." Every KPI has 4 parts: choose a metric (integration metrics, custom metrics, or Google Sheets data); filter it; add a target value + condition (one-time or recurring; time period; repeat daily/weekly/monthly/quarterly/annually; condition operators incl. greater/less/increase-by/decrease-by); optionally an alert condition. KPI data "refreshes automatically every 12 hours"; custom metrics update in real time when viewed directly, so totals "may not always match exactly." Some data sources are excluded from KPIs (no date filter → cannot be broken down by date).

**Roll-up Table (help article).** "A centralized, always-on snapshot of how your clients are performing… across every account, all in one place." Supported integrations listed; multiple accounts per integration aggregated; historical roll-up data "over the past 3 years"; warehoused sources hydrate in two steps (fetch → warehouse → roll-up storage); Totals row computed with SUM / AVG / RATIO aggregations plus one custom-defined aggregation (GA4 bounce rate recomputed from components: "(SUM(sessions) − SUM(engaged_sessions)) / SUM(sessions) × 100"); comparison date ranges; roll-up dashboards and reports (agency-level, not client-level); breakdown by dimensions not yet available for roll-up data.

## Cross-product Comparison

| Dimension | Funnel | Improvado | Databox | AgencyAnalytics |
|---|---|---|---|---|
| Self-label (current) | marketing data hub / marketing intelligence platform | marketing agentic OS / reporting layer for marketing teams | agentic analytics platform / BI & analytics software (drifted) | client reporting & performance insights for marketing agencies |
| Multi-source consolidation | 600+ connectors (vendor claim); connector→platform account→data source model | 1,000+ connectors (vendor claim); extraction templates/orders; data dictionary | 130+ integrations incl. spreadsheets/databases (vendor claim) | 85+ integrations in marketing categories (vendor claim) |
| Unified data layer | Organize (no-code transform, semantic layer, currency conversion) | Transformation layer + shared model ("map every channel to one shared model") | Datasets + semantic layer + metric governance | Custom metrics + roll-up aggregation |
| Marketing KPI semantics | custom metrics (documented ROAS), non-aggregatable rules | 46K+ unified metrics (vendor claim); blended ROAS surfaces | metric library + custom metrics via metric builder | KPIs (metric+filter+target+alert), benchmarks |
| Interpretation/reporting surface | built-in dashboards + Data Explorer + destinations to BI | Reporting & Insights + AI dashboards | Databoards + scheduled reports + no-login sharing | Dashboards + automated white-label client reports + client portal |
| Agency structures | agencies as audience; multi-account per connector | agencies as industry solution | agencies as audience (client accounts) | client containers, roll-up tables, white label, client portal (deepest) |
| Own data-collection tools | no (aggregation only) | no (aggregation only) | no (aggregation only) | yes — Rank Tracker, Site Auditor, AI Tracker |
| Measurement modeling (attribution/MMM) | separate product line (Funnel Measure: MTA, MMM, incrementality) | use case/solution (MMM) | not central | not central |
| AI layer | Funnel AI + MCP | AI Agent + MCP + AI dashboards | Genie AI analyst + agents + MCP | AgencyAI + MCP |
| Data physics documented | freshness per platform; recent data revised; non-aggregatable metrics; rate limits | data dictionary per source; dataflow monitoring | predefined-metrics-vs-raw-records limitation | 12h KPI refresh; warehoused-source hydration; dateless sources excluded from KPIs |
| Warehouse/export posture | destinations to warehouses/BI first-class | warehouse centralization is a platform stage | warehouse integrations; dataset export | roll-up warehousing internal |

Cross-product commonalities (evidence layer B):

1. **Multi-source marketing data consolidation is universal** — every sampled product's foundation is a connector/integration library over the marketing stack (ad platforms, social, email, SEO, CRM, ecommerce, web analytics) plus non-API sources (file/Sheets imports).
2. **A unified/normalized marketing data layer is universal** — every product transforms/maps source data into a shared structure (semantic layer, shared model, datasets, custom metrics) before analysis.
3. **Cross-channel marketing KPI computation is universal** — spend, response, conversion, revenue, and efficiency ratios organized by channel/campaign dimensions; custom metric builders documented in 3/4 samples (Funnel, Databox, AgencyAnalytics; Improvado via transformation layer).
4. **Dashboards + scheduled/shareable reports are universal** — with stakeholder/client distribution (no-login links, white label, portals, scheduled email) as the delivery layer.
5. **Agencies are a first-class audience in all four** — multi-client operation (client containers, roll-ups, white-label) deepest in the agency pole.
6. **An AI interpretation layer is present in all four** (era-current standard capability, not definitional).
7. **Documented data physics is a Type-level phenomenon** — freshness varies per source platform and recent data is revised; some metrics cannot be aggregated naively; some sources expose only predefined metrics without raw records; refresh cycles and backfill are per-source.
8. **Measurement modeling (attribution/MMM) is not the center** — it appears as a separate product line (Funnel Measure), a use case (Improvado), or is absent (Databox, AgencyAnalytics).

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Three structures held jointly:

1. **The organization's own marketing performance as the measured subject.** The application exists to measure *this organization's* marketing activity — its channels, campaigns, spend, delivery, response, conversion, and revenue outcomes — as a standing subject. Remove → generic BI (measures any data) or web analytics (measures site behavior, not marketing performance across channels).
2. **Multi-source marketing data consolidated into one unified view the application owns.** Data is pulled from the organization's marketing stack (ad platforms, social platforms, email platforms, search/SEO tools, CRM/ecommerce systems, web analytics) through connectors/imports into a single normalized store the application maintains — the platform is a lens over data it does not own and does not generate. Remove → single-channel platform-native analytics (each ad/social platform's own reporting), which is exactly what the consolidation exists to transcend.
3. **The marketing analytics layer: cross-channel marketing metrics surfaced for interpretation and reporting.** Marketing KPIs (spend, response, conversion, revenue, efficiency ratios such as ROAS/CPA-class metrics) are computed on the consolidated data along channel/campaign/client dimensions and surfaced through dashboards/reports/AI answers serving marketing decisions and stakeholder/client reporting. Remove → a raw data pipeline/connector (data movement without analytics) or a generic dashboard tool (display without marketing consolidation).

Jointly-held is load-bearing:

- 1 alone = BI/dashboard platform with a marketing customer.
- 2 without 3 = marketing data pipeline/connector (data transport, not analytics).
- 3 without 2 = single-channel analytics (platform-native reporting) or a generic dashboard over one source.
- 1+3 without 2 = single-channel marketing measurement.
- 2+3 without 1 = generic data integration + BI with no marketing subject.

### L1 — Common Mature Structure

Present in essentially all mature modern products, but not required to recognize the Type:

- connector/integration library breadth as a competitive axis (with request-a-connector workflows)
- a marketing semantic/data model (normalized metrics & dimensions across channels; data dictionaries)
- custom metric/formula builders (ROAS, CPA, blended and cross-source metrics)
- KPI targets, alerts, anomaly detection, forecasting
- scheduled reports and stakeholder distribution (email delivery, share links, PDF/slide exports)
- benchmarks (vendor-aggregated industry/peer context)
- budget tracking/pacing against targets
- export/destinations (data warehouses, BI tools, spreadsheets) and APIs
- AI interpretation surfaces (natural-language analysts, MCP-style external agent access)
- data governance at enterprise depth (naming conventions, metric ownership, compliance review)
- cross-client/roll-up views and white-label client portals (agency pole)

### L2 — Variant / Optional Structure

- **Product shape**: pipeline-first (data hub/warehouse-centric, deep transformation: Funnel, Improvado) vs reporting-first (dashboard/report-centric, lighter transformation: Databox, AgencyAnalytics).
- **Audience**: brand marketing teams vs agencies (multi-client containers, white label, roll-ups) vs data teams (warehouse-first, as-code configuration).
- **Own data-collection tools**: some products attach first-party collection (rank tracking, site audit, AI-search visibility) alongside aggregation; others aggregate only.
- **Measurement modules**: attribution/MMM/incrementality bundled as a product line or use case, or absent.
- **Deployment posture**: SaaS-hosted store vs customer-warehouse-centric; depth of transformation (no-code rules vs SQL/recipes).
- **Customer scale/compliance**: enterprise governance/compliance packaging vs self-serve SMB templates.

### L3 — Vendor-specific Structure (kept out of the final document)

- Funnel: flexpoints usage unit; 24-month storage figure; Funnel as Code; Spend Mapper; per-connector "Dimensions and metrics" reference corpus.
- Improvado: Cross-Channel Wizard; Recipe Templates; Dataflow/Billing Dashboards; Creative Analytics Intelligence; named compliance certifications (marketing claims).
- Databox: Databoards/datablocks; Genie; Skills Marketplace; specific comparison pages.
- AgencyAnalytics: Roll-up Table implementation details; Client Portal; Rank Tracker/Site Auditor/AI Tracker specifics; 12-hour KPI refresh figure; Client Knowledge.

### Historical / Market-Sample Check

Would older, regional, platform-native, or differently positioned products still fit?

- Pre-API era: a marketing analyst manually consolidating channel/campaign data (exported files, spreadsheets) into marketing reports/dashboards satisfies all three L0 structures — subject (own marketing performance), consolidation (manual import), analytics layer (computed KPIs + report). The sampled products document manual import as a first-class implementation (Funnel file import; AgencyAnalytics Google Sheets as KPI source; Databox spreadsheets/CSV), so the core does not require cloud APIs, AI, or any specific connector mechanics. **Historical check passed.**
- Platform-native analytics (Google Ads reporting, Meta Ads reporting, GA4) fail L0 leg 2 (single-source) — they are the *sources* this Type consolidates, and (with no web-analytics leaf in the directory) are positioned as the built-in per-channel baseline rather than a directory Type.
- Marketing mix modeling (decades-old discipline) is excluded by directory convention — it has its own leaf; the seam is recorded, not adjudicated here.

## Vendor-specific Findings

- Funnel's 3-tier connection object model (connector / platform account / data source) is the most explicit documentation of a structure that all sampled products share in some form (Databox: data sources + datasets; Improvado: data sources + data tables; AgencyAnalytics: integrations + client accounts). The *concept* (connection → account → configured stream) is treated as common mature structure; the *specific terminology* stays vendor-specific.
- AgencyAnalytics's Roll-up Table (cross-client aggregation with documented SUM/AVG/RATIO semantics and a custom-defined bounce-rate aggregation) is the deepest documented cross-client structure; Databox and Funnel support multi-account/multi-client aggregation more generically.
- Databox's documented limitation (some providers expose only predefined metrics without raw records, blocking filtering/merging) is a data-physics rule likely shared industry-wide but documented explicitly only in this sample — held as common-with-single-source-documentation.
- Improvado's governance module (naming conventions, rule compliance, account owners, violation acknowledgment) is the deepest documented governance packaging; Funnel documents lighter equivalents (Conventions, Budgets).

## Rejected Findings

- "Marketing analytics platform = BI platform with marketing connectors" — rejected as the definition: the marketing subject + marketing KPI semantics + marketing reporting surfaces are structural, not packaging; but the drift zone is real (Databox self-labels BI; Improvado ships an "AI-Native Business Intelligence" docs section). Recorded as a boundary, not a merger.
- "Attribution is part of marketing analytics" — rejected as definitional: measurement modeling appears as a separate product line (Funnel Measure) or use case (Improvado), and 2/4 samples lack it entirely.
- "Own data collection (rank tracking etc.) is part of the Type" — rejected: 3/4 samples aggregate only; AgencyAnalytics's collection tools are an attached pole.
- "AI analysts are definitional" — rejected: era-current capability, uniformly present in the 2026 sample but not required by the structure (historical check).
- Precise connector counts (600+/1,000+/130+/85+), storage windows (24 months), refresh intervals (12 hours), and compliance certifications — vendor claims/figures; kept in Research Notes, not asserted as Type facts in the final document.

## Boundary Findings

1. **vs Social Media Analytics Platform (§06, processed — flag DISCHARGED from this side).** Same mechanics family (connected accounts, metric time series, dashboards, reports) but different measured subject and decision loop: social media analytics measures the organization's **social profiles** (platform-sourced social metrics: audience, content, engagement, reach) for social-marketing decisions; marketing analytics measures the **whole marketing stack** (paid search, paid social, email, SEO, ecommerce, CRM) for cross-channel marketing decisions. Removal tests: restrict the subject to connected social profiles + social metric families → social media analytics; extend the subject to the full marketing stack with spend/outcome semantics → marketing analytics. Social analytics products appear as *data sources* inside marketing analytics platforms (GA4/social connectors documented in-sample). Keep both Types; module straddling (suites bundling both) is packaging.
2. **vs Marketing Attribution Platform (§06, unprocessed).** Attribution assigns conversion credit across touchpoints (modeling); marketing analytics measures and reports performance without credit-assignment modeling as the center. Vendor-policing evidence: Funnel ships Measure (MTA/MMM/incrementality) as a separate product line from its Data Hub; Improvado lists MMM as a use case. Attribution may be bundled as an optional module here. The attribution pass should record the mirror-side seam.
3. **vs Marketing Mix Modeling Application (§06, unprocessed).** MMM models aggregate spend effects top-down (often including offline); marketing analytics measures granular channel/campaign performance bottom-up. Same substrate relationship as attribution (Funnel's Measure line spans both).
4. **vs Business Intelligence Platform (§13, processed).** BI's defining core is the governed analytics-content lifecycle over any data; marketing analytics is domain-bound: marketing connectors, marketing data model, marketing KPI semantics, marketing report templates, client-reporting structures. Drift zone documented: Databox now self-labels "BI & analytics software" while retaining the connect→unify→KPI→report loop and agency audience; Improvado ships "AI-Native Business Intelligence" as a docs section. The working seam: strip the marketing subject/semantics → BI; add the marketing subject + consolidation + marketing semantics → marketing analytics. Keep both Types; the drift is recorded as naming/market drift, not a directory error.
5. **vs Dashboard Platform (§13, processed).** Dashboards are a flagship artifact here too, but the center of gravity is marketing data consolidation + marketing semantics; the dashboard platform's center is the display artifact + connect→compose→keep-current→distribute loop with no domain semantics. Removal tests recorded both directions.
6. **vs Conversion Rate Optimization Platform (§06, processed).** CRO runs a conversion diagnosis-and-improvement loop over the organization's own digital property (visitor-behavior observation: recordings, heatmaps, funnels; experiments); marketing analytics measures channel/campaign performance (spend/outcomes) across the stack. Different data substrate (visitor behavior vs channel performance data); CRO's web-analytics dashboards are a capability, not this Type's center.
7. **vs Marketing Automation Platform / Marketing Campaign Management Platform (§06, unprocessed).** Execution (sending campaigns, journeys, campaign planning) vs measurement. Automation/campaign suites bundle analytics modules — packaging, not Type merger. Removal test: remove the execution loops → the analytics platform remains; add execution → drift toward those Types.
8. **vs Web analytics (GA-class; no directory leaf).** Web analytics measures site/app behavior (traffic, sessions, behavior flow); it is a *data source* for this Type (GA4 connectors documented in all four samples where present). The directory has no Web Analytics leaf; this pass positions GA-class tools as the per-channel baseline (same treatment the social passes gave platform-native analytics). Recorded in STATUS Boundary Issues as a directory observation, not a change.
9. **vs Data Integration Platform / ETL (§13).** Generic pipelines move any data; marketing analytics platforms are marketing-bound (marketing APIs, marketing metric semantics, marketing reporting surfaces). Funnel/Improvado straddle deliberately (both sell warehouse delivery); the marketing packaging + analytics surface is the discriminator. Removal test: strip the analytics surface → a marketing data pipeline (a capability of §13 Types, marketed differently).
10. **Naming drift observation (no directory change).** The market label has moved: "marketing analytics platform" (Improvado's historical label) → "marketing data hub" / "marketing intelligence platform" (Funnel) → "agentic analytics platform" (Databox) → "client reporting platform" (AgencyAnalytics). The referent — cross-channel marketing performance measurement and reporting — is stable across all four.

## Uncertainties

- **Single-source edge**: whether a product consolidating exactly one source could still qualify. No such product self-labels as a marketing analytics platform in the sample; the consolidation is the Type's reason to exist. Held as definitional with this reasoning, but the edge is untested against a real counter-example.
- **Surface necessity**: the interpretation/reporting surface is held definitional (a pure pipe is not "analytics"). Supermetrics-class connector products were not fetched; the reasoning rests on the sampled products all shipping surfaces + the market's separate labeling of pure pipes.
- **Connector counts, storage windows, refresh intervals, compliance certifications**: vendor claims (Tier 2); not independently verified; excluded from the final document's assertions.
- **Historical products** (2010s marketing dashboards, e.g., early DashThis/Klipfolio marketing use): not directly fetched; the historical check is structural (manual-import implementations documented in-sample satisfy the core).
- **Improvado Tier-1 depth**: docs section pages list topics without article bodies; observations rest on section structure + root claims. Assertion strength kept moderate for Improvado-specific mechanics.
- **Databox's marketing relevance**: its current self-label is BI/agentic; it remains in the sample because its documented structure (integrations → datasets → metrics → dashboards/reports → goals/alerts) is the reporting-first pole's clearest documentation and its agency audience is explicit. If the taxonomy owner later prefers a pure marketing-labeled sample, Whatagraph/NinjaCat are the candidates.

## Final Synthesis

The Marketing Analytics Platform is the organization-side, cross-channel marketing measurement application. Its defining core is three structures held jointly: the organization's own marketing performance as the standing measured subject; multi-source marketing data consolidated from the marketing stack into one unified view the application owns; and a marketing analytics layer that computes cross-channel marketing KPIs on that consolidated data and surfaces them through dashboards/reports (increasingly AI answers) for marketing decisions and stakeholder/client reporting. The Type exists because no single marketing platform reports the whole picture: each source reports only itself, with its own metric definitions, freshness, and aggregation rules — the platform's job is to transcend that fragmentation and keep one trusted marketing numberset.

Everything else is layered on top: connector breadth, semantic layers, custom metric builders, KPI targets/alerts/anomaly detection/forecasting, benchmarks, budget pacing, warehouse/BI destinations, governance, AI analysts, white-label client reporting, roll-ups. Two product shapes realize the same core — pipeline-first (data hub/warehouse-centric) and reporting-first (dashboard/report-centric) — serving brand teams, agencies, and data teams at different depths. Measurement modeling (attribution, MMM) is a neighboring layer, sometimes bundled, not the center. The definition survives the historical check: a manually consolidated marketing report satisfies all three structures without cloud, APIs, or AI.
