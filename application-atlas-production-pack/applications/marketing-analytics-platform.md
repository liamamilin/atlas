# Marketing Analytics Platform

## Overview

A **Marketing Analytics Platform** is an organization-side application that measures the performance of the organization's own marketing across all of its channels and campaigns. It consolidates data from the many platforms the organization markets through — ad platforms, social platforms, email tools, search and SEO tools, CRM and ecommerce systems, web analytics — into one unified view it owns, computes cross-channel marketing metrics on that consolidated data, and surfaces the results through dashboards, reports, and increasingly AI-generated answers that inform marketing decisions and stakeholder or client reporting.

The defining core is small:

```text
The organization's marketing performance (the measured subject)
└── Marketing data consolidated from many sources into one unified view
    └── Cross-channel marketing metrics computed on that view
        └── Interpretation & reporting surfaces for marketing decisions
```

The Type exists because of a fragmentation problem no single marketing platform solves: each ad, social, email, and analytics platform reports only itself, with its own metric definitions, update behavior, and aggregation rules. A marketing analytics platform's job is to transcend that fragmentation — to keep one trusted, current set of marketing numbers that spans the whole stack.

Everything commonly associated with modern products — huge connector libraries, semantic layers, KPI targets and alerts, benchmarks, budget pacing, white-label client portals, AI analysts — is standard capability layered on this core, not what makes the product a marketing analytics platform. A manually consolidated marketing report built from exported files satisfies the same core; the definition does not depend on cloud APIs or AI.

## Users & Context

The primary users are people responsible for marketing performance and for answering "what is our marketing doing, and what should we do next":

- **marketers / channel managers** — monitor their channels and campaigns, check spend and results, prepare for reviews
- **marketing analysts** — build and maintain the unified data view, define metrics, investigate changes
- **agency account teams** — operate reporting for many client accounts, deliver client-facing reports
- **data teams** — pipe consolidated marketing data into warehouses and BI tools, govern definitions

Secondary consumers read rather than build: executives and clients who receive dashboards and scheduled reports, often without logging in.

The work context is recurring and cyclical: connect the stack once, keep it current, monitor continuously, and report on a schedule (weekly, monthly, per campaign flight). The agency context adds a multi-client dimension: the same loop runs per client, at scale, under the agency's brand.

## Core Model

### The Defining Core

**The measured subject: the organization's own marketing performance.** The application exists to measure one organization's marketing activity — its channels, campaigns, spend, delivery, response, conversion, and revenue outcomes — as a standing subject. It is not a tool for measuring someone else's audience, and it is not a generic data tool: the subject is marketing performance, held persistently.

**Multi-source consolidation into one unified view.** Data enters from the organization's marketing stack through connections the user establishes. The platform maintains a single normalized store of that data — it is a lens over data it does not own and does not generate. This is the structural reason the Type exists: remove the consolidation and every remaining capability collapses into what each source platform already offers by itself.

**The marketing analytics layer.** On the consolidated data, the platform computes marketing metrics — spend, impressions, clicks, conversions, revenue, and efficiency ratios that relate spend to outcomes — organized along marketing dimensions (channel, campaign, account, client, date). These metrics are surfaced through interpretation and reporting surfaces: dashboards, reports, KPI views, and AI answers. Without this layer the product is a data pipeline; without the consolidation beneath it, it is single-channel reporting.

All three structures are held jointly. A product with only the subject is a BI tool with a marketing customer. Consolidation without the analytics layer is a data pipeline. The analytics layer without consolidation is single-channel reporting. The joint hold is the Type.

### The Connection Structure

Mature products document a consistent three-part structure for how data enters, under varying names:

- **Connector / integration** — the built-in link to an external platform (an ad platform, a social platform, an email tool, a web analytics service). The connector is a gateway, not data; its availability typically depends on the product tier, and products without a needed connector commonly offer a request workflow or a custom-connection path.
- **Account** — the specific account, property, store, or view the organization owns or manages on that platform. Platforms name it differently (ad account, store, property), but the concept is the same: the entity that holds the data. One connector commonly serves many accounts — the standard pattern for multi-brand organizations and agencies.
- **Data stream / data source** — a configured extraction from an account: which metrics and dimensions to pull, with what structure and filters. One account can feed several differently configured streams.

The setup flow is correspondingly stable: choose a connector → authorize and link accounts → configure data streams. Non-API sources are first-class too: file uploads, spreadsheets, and webhooks are documented implementation paths, which is what keeps the core independent of any particular integration mechanics.

### The Unified Data Layer

Raw source data is not analysis-ready. Mature products normalize it into a shared structure before analysis:

- **metric normalization** — mapping each platform's fields onto common definitions, so "spend" or "clicks" means the same thing across channels
- **custom metrics** — user-defined calculations (efficiency ratios, blended cross-channel figures) built with rule or formula builders
- **custom dimensions** — user-defined groupings (campaign naming conventions, brand or client taxonomies) applied across sources
- **currency and date handling** — conversion and period alignment across sources that report in different currencies and on different clocks
- **blending** — combining data from multiple sources into one dataset for cross-channel questions

### The Analytics and Reporting Layer

On top of the unified data:

- **dashboards** — standing, current views of marketing performance across channels
- **KPI machinery** — targets, thresholds, alerts, anomaly detection, forecasts on chosen metrics
- **reports** — composed, schedulable, distributable documents; in the agency pole, white-labeled and delivered through client portals
- **cross-client views** — aggregate performance across many client accounts in one table or dashboard
- **AI interpretation** — natural-language questions answered from the unified data, increasingly with governed access for external AI tools

## How It Works

### Connect the marketing stack

```text
Choose a connector for a platform
→ authorize access to the organization's account(s) on that platform
→ configure what to pull (metrics, dimensions, filters)
→ data begins flowing into the platform's own store
→ repeat across the stack (ads, social, email, search, ecommerce, web analytics)
→ add non-API sources (files, spreadsheets) where needed
```

Connection is the first-class setup act. The platform then keeps the data current on its own schedule, per source.

### Unify and organize

```text
Map source fields to common definitions
→ clean, group, and normalize (naming conventions, taxonomies)
→ define custom metrics and dimensions
→ resolve currency and date differences
→ blend sources where cross-channel questions need it
```

This is the step that turns many platform-specific feeds into one marketing numberset. Its depth varies by product shape — from no-code rules to full transformation layers — but some unification is always present, because cross-channel metrics cannot be computed on unnormalized data.

### Monitor and analyze

```text
Watch dashboards of cross-channel performance
→ compare periods, channels, campaigns, clients
→ track KPIs against targets; receive alerts on anomalies
→ ask questions in natural language (where AI surfaces exist)
→ drill into the underlying data when an answer needs checking
```

### Report and distribute

```text
Compose a report or dashboard for an audience
→ schedule it (weekly, monthly, per flight)
→ deliver: email, share links, PDFs, client portals
→ in the agency pole: white-label under the agency's brand
→ export or pipe the data onward (spreadsheets, warehouses, BI tools)
```

The loop closes: reporting drives questions, questions drive deeper analysis, analysis drives reconfiguration of what is measured and how.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Connections / data sources management

The setup and health surface for the consolidation layer.

- lists connectors, linked accounts, and configured data streams, with status and freshness
- primary actions: add a connection, authorize an account, configure or edit a stream, troubleshoot a broken connection, request a missing connector

### Unified data exploration

The working surface over the consolidated data.

- table/explorer views with metrics and dimensions, filters, date ranges, currency switching
- primary actions: build a view, create custom metrics or dimensions, blend sources, export

### Dashboards

The standing monitoring surface.

- multi-panel views of cross-channel marketing metrics, current by automatic refresh
- primary actions: compose panels from any connected source, set date ranges and comparisons, share

### KPI / target views

The performance-management surface.

- metrics with targets, thresholds, progress, alerts, and (in mature products) forecasts and anomaly flags
- primary actions: define a KPI (metric + filter + target + alert condition), review status, manage alerts

### Reports

The distribution surface.

- composed, branded documents assembled from the same data; scheduled delivery to stakeholders or clients
- primary actions: build from templates, schedule, white-label, deliver via email/link/portal, export

### Cross-client views (agency context)

The portfolio surface for agencies.

- one table or dashboard aggregating metrics across many client accounts, with totals and comparisons
- primary actions: filter by client or group, compare periods, publish as roll-up dashboards/reports

### AI analyst surfaces

The interpretation layer (era-current standard capability).

- natural-language questions answered from the unified data, with the same definitions reports use; some products expose the data to external AI tools under governed access

### Administration

Users, roles, workspaces (per client or brand), metric governance, and plan/billing visibility — deeper in enterprise and agency packaging.

## Important Rules / Behaviors

### The platform is a lens over data it does not own

Source platforms own their metric definitions and their numbers. A marketing analytics platform re-serves those numbers under its own normalization; figures may legitimately differ from what a source's own UI shows at a given moment, and products document reconciliation and troubleshooting paths for exactly this. The platform's authority is the unified view, not the source systems.

### Recent data moves

Freshness varies per source platform: some metrics appear near-instantly, others finalize hours or days later, and recently fetched values are commonly revised. Mature products treat this as documented data physics — per-source freshness, scheduled re-fetches, and caution when optimizing on very recent numbers — rather than as an error state.

### Not every number can be aggregated naively

Cross-channel aggregation has documented traps: ratio metrics (spend-per-click class) must be recomputed from their components, not averaged; unique-count metrics (people reached class) must not be summed across campaigns or dates, because the same person counts once. Products encode this as metric rules — some metrics are marked non-aggregatable or get custom aggregation definitions — because wrong aggregates lead to wrong budget decisions.

### Some sources give more than others

Source platforms differ in what they expose: some provide granular records that can be filtered, merged, and rebuilt; others expose only predefined summary figures that resist breakdown. This shapes what blending and custom metrics can do per source — which is why the granularity of each integration is worth documenting rather than assuming.

### Connection health is operational

Credentials expire, accounts change, platforms revise APIs. A broken or reconnected connection can leave historical gaps; keeping the unified view trustworthy is an ongoing operational task, not a one-time setup.

### Access is layered

Access control typically operates at two levels: which data sources and clients a user may see, and which analytics content they may edit or only view. In the agency pole, client-facing surfaces are deliberately separated from internal working surfaces.

## Variants

- **Pipeline-first products** — data-hub/warehouse-centric: deep ingestion and transformation, semantic layers, delivery to warehouses and BI tools; dashboards present but the data foundation is the product's center.
- **Reporting-first products** — dashboard/report-centric: fast connection of many sources, template-driven dashboards and client reports, lighter transformation; the deliverable is the center.
- **Brand-side deployments** — one organization's stack; subjects are its channels and campaigns.
- **Agency deployments** — many client containers under one operator; white-label reporting, client portals, cross-client roll-ups; the deepest multi-client structures.
- **Data-team deployments** — the platform as the marketing data layer of a wider stack: warehouse delivery, as-code configuration, governance of definitions.
- **Products with attached collection tools** — some add first-party data collection (rank tracking, site auditing, AI-search visibility) alongside aggregation; others aggregate only.
- **Products with measurement modules** — some bundle attribution or marketing-mix modeling as a separate line or add-on; others leave measurement modeling to neighboring products.
- **Self-serve vs enterprise packaging** — template-driven SMB onboarding vs governed, compliance-oriented enterprise deployments.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Social Media Analytics Platform | adjacent sibling | measures the organization's **social profiles** (platform-sourced audience/content/engagement metrics) for social-marketing decisions; this Type measures the **whole marketing stack** with spend/outcome semantics. Social analytics products appear here as data sources |
| Marketing Attribution Platform | neighboring layer | assigns conversion **credit** across touchpoints (modeling); this Type measures and reports performance without credit modeling as the center. Attribution may be bundled as an optional module |
| Marketing Mix Modeling Application | neighboring layer | models aggregate spend effects top-down (often including offline); this Type measures granular channel/campaign performance bottom-up |
| Business Intelligence Platform | structural neighbor | BI is the generic governed analytics-content lifecycle over any data; this Type is domain-bound — marketing connectors, marketing metric semantics, marketing report structures. The boundary is the marketing subject, not the artifact mechanics |
| Dashboard Platform | artifact overlap | dashboards are a flagship artifact here too, but the center is marketing consolidation + semantics; a dashboard platform is domain-agnostic display over connected sources |
| Conversion Rate Optimization Platform | different substrate | CRO runs a diagnosis-and-improvement loop over the organization's own property using **visitor behavior** (recordings, heatmaps, funnels, experiments); this Type measures **channel performance** (spend/outcomes) across the stack |
| Marketing Automation Platform | execution vs measurement | automation sends campaigns and runs journeys; this Type measures results. Automation suites bundle analytics modules — packaging, not the same Type |
| Marketing Campaign Management Platform | planning vs measurement | campaign management plans and executes campaigns; this Type measures how they performed |
| Web analytics (e.g., site analytics tools) | data source | site/app behavior measurement (traffic, sessions, behavior) is one input among many; the directory treats it as a capability baseline rather than a separate Type |
| Data Integration / ETL Platform | capability overlap | generic pipelines move any data; this Type is marketing-bound and carries the analytics surface. Strip the analytics surface and the remainder is a marketing data pipeline |

The closest seams are with Social Media Analytics (channel-specific vs whole-stack) and Business Intelligence (generic vs marketing-bound). Both are held by the measured subject and the marketing semantics, not by feature lists — suites bundle neighboring modules on both seams, which is packaging rather than Type merger.

## Representative Products

- **Funnel** — marketing data hub; pipeline-first pole with deep connector coverage and warehouse delivery
- **Improvado** — enterprise marketing data pipeline with transformation, governance, and AI reporting layers
- **Databox** — self-serve connect→metrics→dashboards/reports platform (now positioned broadly as analytics/BI software; retained as the reporting-first pole's clearest documentation)
- **AgencyAnalytics** — agency client-reporting platform; the deepest documented multi-client structures (roll-ups, white label, client portals)

The defining core was checked against manual-import implementations documented inside these products (file and spreadsheet sources) to avoid over-fitting the definition to current API-and-AI-era packaging.

## Sources

Research date: **2026-09-08**. All sources are official vendor surfaces.

- Funnel — root: https://funnel.io/ ; help center: https://help.funnel.io/en/ ; "What is Funnel?": https://help.funnel.io/en/articles/8020917-what-is-funnel ; "Connector, platform account and data source": https://help.funnel.io/en/articles/13616444-connector-platform-account-and-data-source ; "What are non-aggregatable metrics?": https://help.funnel.io/en/articles/2624615-what-are-non-aggregatable-metrics ; "Data freshness": https://help.funnel.io/en/articles/5745199-data-freshness
- Improvado — root: https://improvado.io/ ; documentation: https://improvado.io/help ; Extracting data: https://improvado.io/docs-section/data-extraction ; Transforming data: https://improvado.io/docs-section/transformations
- Databox — root: https://databox.com/ ; knowledge base: https://help.databox.com/docs ; "Understanding datasets": https://help.databox.com/understanding-datasets
- AgencyAnalytics — root: https://www.agencyanalytics.com/ ; help center: https://help.agencyanalytics.com/en ; "Tracking KPIs in AgencyAnalytics": https://help.agencyanalytics.com/en/articles/15382468-tracking-kpis-in-agencyanalytics ; "Monitor Performance Across All Your Clients with the Roll-up Table": https://help.agencyanalytics.com/en/articles/10034853-monitor-performance-across-all-your-clients-with-the-roll-up-table

> Sourcing notes: connector counts, storage windows, refresh intervals, and compliance certifications observed on vendor pages are vendor-stated figures and are deliberately not asserted as Type facts in this document. Improvado's documentation was reachable at section level; product-mechanics claims for it are kept at moderate strength. One URL guess (a marketing-specific Databox page) returned 404; the vendor's root and knowledge base were used instead.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
