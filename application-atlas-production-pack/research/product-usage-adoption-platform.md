# Research Notes — Product Usage / Adoption Platform

Research date: 2026-09-06
Slug: `product-usage-adoption-platform` · Directory leaf: **Product Usage / Adoption Platform** (§07 Sales, Customer & Revenue)
Methodology: WORKFLOW_v1.1 (10-step) · WRITING_GUIDE_v1.1

---

## Research Goal

Understand the generic **Product Usage / Adoption Platform** as an Application Type: what objects exist inside it, how usage data is captured from an organization's own software product, how that data is analyzed into adoption measurements, how it rolls up to customer accounts, and where its boundary sits against the neighboring Types in §07 (Customer Success Platform, Customer Health Monitoring, Voice of Customer, Customer Feedback Management), §14 (APM, Digital Experience Monitoring), §06 (CDP, A/B Testing, Marketing Analytics), §12 (Product Management Platform), and §13 (BI Platform).

The leaf name joins two market labels ("product usage" and "product adoption") that vendors use interchangeably for the same category. The market also uses "product analytics", "product experience", and "digital adoption" for overlapping products. The sample was therefore drawn across the category's poles: analytics-first products, analytics+guidance hybrids, and a CS-integrated product-experience product, plus a Customer Success platform as a boundary check.

## Initial Boundary (hypothesis before research)

- Hypothesis: this Type is the vendor-side instrumentation + analytics layer that measures how end users actually use the vendor's own software product, with adoption (feature uptake, activation, retention, stickiness) as the central analytical subject.
- Nearest neighbors: Customer Success Platform (consumes usage, manages customer workflow), Customer Health Monitoring (aggregates signals into scores), APM (same instrumented product, different telemetry subject), Web Analytics (same event capture, different subject), CDP (same event capture, different center), BI (analysis without capture), A/B Testing (experiment structure), in-app guidance products (drive adoption without necessarily measuring it).
- Risk: the leaf could collapse into either "product analytics" (too narrow — misses the adoption-driving modules) or "digital adoption platform" (guidance-first products). Both risks were checked against the sample.

## Research Questions

1. What are the core objects? (product/app, tracked user, account, event, feature/page definitions, segments, reports, dashboards)
2. How does usage data get in? (SDK, visual tagging, autocapture, server API, warehouse sync, browser extension)
3. What analyses are canonical across products? (trends, funnels, retention, paths, adoption rankings, stickiness, time-to-first-use, license utilization)
4. How does usage roll up to customer accounts, and what account-level metrics exist?
5. Which adoption-driving modules are common (in-app guides, surveys, orchestration) and which are optional (experimentation, feedback-to-roadmap, replay, AI)?
6. Who are the users of the platform itself (product teams, CS, growth, IT)?
7. Where are the boundaries vs CS Platform, Health Monitoring, APM, Web Analytics, CDP, BI?
8. Historical check: do older/regional/platform-native usage-tracking products (mobile-analytics era, admin-console usage reports, license-utilization reports) fit the same definition?

## Representative Products

| Product | Positioning | Why sampled | Evidence tier |
|---|---|---|---|
| **Pendo** | "Product experience" platform; analytics + in-app guides + feedback; strong B2B SaaS / CS adjacency | The category's hybrid pole; richest account/CS-facing structure (accounts, license utilization, PES) | A — Help Center (Tier 1) fetched |
| **Amplitude** | Digital analytics / product analytics platform; product-led growth orientation | The analytics-first pole; strongest data-governance and experimentation structure | A — official docs (Tier 1) fetched |
| **Mixpanel** | Product analytics; events/users/properties model | The pure-analytics pole with no native in-app guidance — the sharpest test of what is defining vs bundled | A — official docs (Tier 1) fetched |
| **Gainsight PX** | "Product Experience" platform inside the Gainsight CS ecosystem | The CS-integrated pole; explicit Tracked Account/User object model and Adoption Analysis | A — support docs (Tier 1) fetched |
| **ChurnZero** | Customer Success platform (boundary check only) | Confirms the CS-side consumption of usage data (integrates Pendo/Mixpanel as sources) | B — official marketing site (Tier 2) only |

## Sources

All fetched 2026-09-06.

- Pendo Help Center: https://support.pendo.io/hc/en-us (root), Data in Pendo category, Analytics category, Guides category, Dashboard widgets article, Measure overall feature adoption article
- Amplitude Documentation: https://amplitude.com/docs (docs home; product-area index)
- Mixpanel Docs: https://docs.mixpanel.com/ (What is Mixpanel; full llms.txt documentation index)
- Gainsight PX: https://support.gainsight.com/PX (Product Experience root), PX Object Glossary → Product Experience (PX) Objects, Analytics category
- ChurnZero: https://churnzero.com/ (marketing site; feature and integration lists)

No fetch failures. ChurnZero was used only at positioning level (Tier 2); no operational ChurnZero claims are made.

---

## Product A — Pendo

### Key observations (Layer A unless noted)

- **Implementation surfaces**: direct web implementation (JavaScript snippet inserted into the application), browser-extension implementation (Pendo Launcher deployed on third-party applications), mobile SDK ("analytics and guides across all of your mobile apps"). Settings exist at organization, subscription, and **application** levels — the app is a first-class object.
- **Data model** ("Data in Pendo"): Visitor and account data (metadata mappings, custom metadata fields, historical metadata, **account revenue**, visitor/account ID merge); Segments (rules); Events (overview, event properties, time-on-page calculations); **Product Areas**; **Pages and Features** (tagged visually with the Visual Design Studio; AI tagging in beta); **Track Events** (custom API events, usable in non-web environments); mobile tagging.
- **Analytics**: Dashboards with a large widget catalog; People (Visitors, Visitor details/reports; Accounts, Account details/reports); Behavior reports (Data Explorer, formulas, Retention); Employee analytics (App catalog, Application usage, **Employee license utilization**, Command Center, Portfolio overview).
- **Dashboard widgets observed** (widget catalog article): Account Overview (daily/weekly/monthly active accounts), Visitor Overview, Account/Visitor Frequency (low/medium/high activity bands over trailing 30 days), **Feature Adoption** (Pareto-style: which Features make up a configurable benchmark share of clicks, default 80%), Feature/Page Use by Account/Visitor scatterplots, Page/Feature Use Over Time, **Retention**, **Retention by Usage** (account retention by first-use cohort within first 30 days), **Stickiness** (DAU/MAU ratio), **Time to First Use** (box plot), **User License Utilization** (active users vs seats purchased — requires account metadata representing total possible users), **Product Engagement Score (PES)**, Goals (usage goals), Funnel, Path, Workflow/Workflow Journeys, Guide widgets (activity, engagement, goals, time-on-guide), NPS, Poll Results, App Usage, Browser/Device/OS usage, AI Agent analytics (usage trends, feedback, quality), Replay saved filters, Object Analytics.
- **Guides** (in-app communication): overlay and embedded guides, guide designers/layouts/themes, ordering and throttling, automations, branching with conditional logic, guide metrics (effectiveness, goals, views, poll responses), **A/B testing with guides**, mobile guides, Help Center module, permalink guides.
- **Adjacent modules**: Sentiment (NPS, PMF, CSAT, UX-Lite surveys), Replay (session replay), Listen (feedback to inform product development; classic Feedback retired), Orchestrate (cross-channel journeys using emails and in-app guides), Predict (AI prediction models), Agent Analytics (AI-agent usage), Integrations, OEM partners (manage analytics and guides for end customers of ISVs).
- **AI**: Leo (natural-language product-usage analysis, beta), Signals (anomaly alerts, Slack delivery).

## Product B — Amplitude

### Key observations (Layer A)

- **Docs structure** (product areas): Amplitude AI; **Data** ("Govern your event taxonomy" — tracking plan, autocapture, validate events on ingest); **Analytics** ("Understand product behavior" — event segmentation charts, funnels, cohorts, dashboards); Session Replay; Zoning Insights (page-region engagement); Heatmaps; Web Experiment (visual A/B); Feature Experiment (feature flags + A/B); AI Assistant (in-product AI support); **Guides and Surveys** ("Deliver targeted guides, onboarding flows, and surveys").
- **Role-based quickstarts**: engineers (SDK setup, event tracking, identity); product teams (funnels, retention, segmentation charts, dashboards); growth teams ("Activate cohorts in your marketing stack, measure attribution"); data teams (tracking plan, schema enforcement on ingest, warehouse export).
- **SDKs**: browser, iOS, Android, React Native for Analytics; separate SDK lines for Experiment, Guides & Surveys, Session Replay.
- **Identity**: identify users at runtime; cohorts as first-class objects; cohort-targeted experiments.
- The docs home describes the pipeline as "from your first `track()` call to cohort-targeted experiments".

## Product C — Mixpanel

### Key observations (Layer A)

- **Self-description**: "Mixpanel product analytics … track how users engage with your product and analyze this data with interactive reports". Three core concepts: **Events** (actions in your product), **Users** (people who use your product, with unique identifiers — email, username, or unique ID), **Properties** (attributes of users and events).
- **Data model**: events + properties; user profiles (persistent attributes, import via API/CSV, delete); **Group Analytics** ("Group users together as an aggregated unit of measurement" — B2B Company Analytics via group keys; events can attribute to multiple groups); lookup tables (CSV enrichment).
- **Tracking methods**: SDKs (web, iOS, Android, RN, Flutter, Unity, server languages), **Autocapture**, warehouse connectors (ingest from warehouse), tracking integrations (Segment, mParticle, Rudderstack, GTM, Snowplow, Freshpaint…), first-party domains.
- **Identity management**: identify users (simplified ID merge), alias, merge identities; Data Inspector.
- **Reports**: **Insights** (trends/compositions), **Funnels** (conversion through event series), **Retention** (engagement over time), **Flows** (frequent paths to/from an event), Impact (effect of a launch on KPIs), Signal (correlation between events), JQL (custom JS queries).
- **Boards** (dashboards): collect reports, templates, sharing/permissions, public boards, nested boards.
- **Users/Cohorts**: cohorts by demographic and behavior; **cohort sync** to third-party tools (Braze, Marketo, Mailchimp, Iterable, Facebook/Google Ads, **Appcues, Chameleon** (guidance tools), Intercom, mParticle…).
- **Feature Flags** ("rollout with precision control", runtime events targeting by behavior) and **Experiments** (A/B impact measurement).
- **Session Replay** + **Heatmaps** (web).
- **Data governance**: **Lexicon** (data dictionary), data views & classification, data standards, **event approval** (review unexpected events before visible), **data volume monitoring**, clean-up, AI-powered governance.
- **Org/admin**: organizations, projects, roles & permissions, SSO, audit log; privacy (opt-out, anonymization, GDPR, EU/India data residency); pricing (MTU billing legacy; event-based).
- **AI**: Mixpanel Agent (question→answer), agentic automations, **Root Cause Analysis** (AI explanations for metric changes), MCP server, Headless (programmatic access), Business Context.
- **No native in-app guidance module** — guidance is reached via cohort sync to Appcues/Chameleon etc. This absence is analytically important (see Rejected Findings).

## Product D — Gainsight PX

### Key observations (Layer A)

- **Positioning**: "Gainsight PX is the easy, powerful, and complete Product Experience Platform"; part of Gainsight (the Customer Success company); docs sit beside Gainsight CS.
- **Install**: PX Web, PX Mobile, PX Desktop (SDK instrumentation).
- **Object model** (PX Object Glossary — objects synced into the Gainsight ecosystem):
  - **Tracked Account** (customer org: account ID, name, customer ID, employees, parent group, SFDC ID, monthly active users)
  - **Tracked User** (individual: identify ID, email, name, linked Tracked Account, SFDC contact)
  - **Tracked Account Product** and **Tracked Account Product User** (account × product; user × account × product)
  - **Account Usage Data** (1/7/30/90-day active-user counts and visit counts per account × product, with percentage changes)
  - **Account Engagement Data** (7/30/90-day NPS scores and responses with percentage changes)
  - **Engagement** (in-app message object: audience URLs, channel, environments, product, status)
  - Config object (SDK session timeout, event cache)
- **Product Mapper**: "Instrument your product with PX to begin tracking customer usage and launch in-app engagements" — visual tagging of the product.
- **Analytics**: Reports, custom filters, data dictionary; **Tracking: Accounts Explorer, Audience Explorer**, server-side usage data; Dashboards (widgets, templates, comparison widget); **Adoption → Adoption Analysis**; Path Analysis (Funnels, Path Analyzer); Query Builder; Retention Analytics; Engagement Analytics (NPS analysis); KC Bot / In-App Hub analytics.
- **Engagements**: "Build engagements (i.e. dialogs, sliders, guides, etc.) to inform and guide your users."
- **Integrations**: native integrations to popular SaaS platforms (incl. Gainsight CS sync — the object glossary shows PX data landing in Gainsight Company/Person objects).

## Product E — ChurnZero (boundary check only)

### Key observations (Layer B, positioning-level)

- Customer Success software: customer health scoring, customer journeys, plays/automation, in-app communications, renewal forecasting, surveys (NPS/CES/CSAT), reporting, AI agents.
- **"Increase Adoption" is marketed as a solution**, but the mechanism is CS-side (plays, journeys, in-app communications) — not event-level product analytics.
- **Integration list includes Pendo and Mixpanel** — the CS platform ingests usage data from product usage platforms. This confirms the direction of the boundary: usage platform = producer/analyzer of usage signal; CS platform = consumer/workflow system.

---

## Cross-product Comparison

| Structure / capability | Pendo | Amplitude | Mixpanel | Gainsight PX | Verdict |
|---|---|---|---|---|---|
| Instrumented product as first-class object | App (under subscription) | Project | Project | Product (Product ID; Tracked Account Product) | **Defining** (all four) |
| Tracked end-user records | Visitor | User | User profile | Tracked User | **Defining** (all four) |
| Usage events bound to user + time | auto-captured clicks, Page views, Track Events | track() events, autocapture | events + properties | feature usage via tagging | **Defining** (all four) |
| Usage/adoption analytics over time | Data Explorer, Retention, Feature Adoption, Stickiness, Time to First Use | event segmentation, funnels, retention, cohorts | Insights, Funnels, Retention, Flows | Adoption Analysis, Retention, Funnels, Path Analyzer | **Defining** (all four) |
| Account/customer rollup (B2B) | Accounts (+ parent accounts, account revenue) | (not verified in fetched pages) | Group Analytics (B2B company) | Tracked Account + Account Usage Data | Common (B2B deployments); implementation varies |
| Feature/page tagging or taxonomy definition | Visual Design Studio tagging, Product Areas | tracking plan, autocapture, validation | Lexicon dictionary, event approval | Product Mapper | Common (all four, different mechanics) |
| Segments/cohorts | Segments | cohorts | cohorts | audience/filters | Common |
| Dashboards | Dashboards + widget catalog | dashboards | Boards | Dashboards + templates | Common |
| Identity management (identify/merge) | visitor/account ID merge | identify users | identify/alias/merge | identify ID | Common |
| In-app guidance module | Guides | Guides and Surveys | **absent** (cohort sync to guidance tools) | Engagements | Common-but-not-universal module |
| In-product surveys/feedback | Sentiment (NPS/PMF/CSAT), polls | Guides and Surveys | (not native) | Engagement Analytics (NPS) | Common module |
| Session replay / heatmaps | Replay | Session Replay, Heatmaps, Zoning | Session Replay, Heatmaps | (not observed in fetched pages) | Common module |
| Experimentation / feature flags | A/B testing with guides | Web + Feature Experiment | Feature Flags + Experiments | (not observed) | Optional module |
| Feedback → product requests | Listen | (not observed) | (not observed) | (not observed) | Optional module |
| Warehouse pipelines / export | Integrations | warehouse export (data-team quickstart) | warehouse connectors + data pipelines | integrations | Common |
| Cohort sync to marketing/CS tools | Integrations | growth-team activation | cohort sync (broad catalog) | Gainsight CS sync | Common |
| Data governance (validation/approval/volume) | tagging management | Data (validate on ingest) | Lexicon, event approval, volume monitoring | data dictionary | Common in mature products |
| AI assistance | Leo, Signals, Predict | Amplitude AI, AI Assistant | Agent, Root Cause Analysis, MCP | (not observed in fetched pages) | Common (current market) |
| Employee/third-party-app analytics | browser extension, Employee analytics, license utilization | (not observed) | (not observed) | (not observed) | Product-specific variant |
| OEM/embedded analytics for ISVs | OEM partners | (not observed) | (not observed) | (not observed) | Product-specific variant |
| Cross-channel orchestration (email + in-app) | Orchestrate | (not observed) | (not observed) | (not observed) | Product-specific variant |

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

1. **Instrumented product as first-class subject** — the platform is deployed inside an organization's own software product(s); the product (app/project) is a managed object in the platform, and all data belongs to it.
2. **Tracked end-user population** — individual users of that product exist as tracked records (identified or anonymized), each with an identity that can be resolved across sessions/devices.
3. **Captured usage events** — records of actual product interactions (feature use, page/screen views, custom events) bound to user, product, and time, collected continuously from live use.
4. **Usage/adoption analytics** — analytical surfaces that aggregate events into usage measurements over time (who uses what, how much, how it changes, which features drive engagement).

Remove #1 → generic event pipeline/CDP. Remove #2 → anonymous traffic analytics (web analytics). Remove #3 → survey-only feedback tool. Remove #4 → raw instrumentation without a product. All four are required.

### L1 — Common Mature Structure

- Account/customer rollup for B2B (accounts, active users per period, license/seats utilization; native account objects in some products, group-analytics constructs in others)
- Usage-taxonomy machinery: feature/page tagging (visual or code-defined), tracking plans/dictionaries, autocapture, event validation/approval, volume monitoring
- Segments/cohorts from behavior + attributes
- Standard report vocabulary: trends/event segmentation, funnels, retention, paths/flows, stickiness (DAU/MAU), time-to-first-use, feature-adoption rankings, usage goals
- Dashboards with widget catalogs; sharing/collaboration
- Identity management (identify, alias, merge; anonymous→known)
- Integrations/export: warehouse pipelines, APIs, cohort sync to marketing/CS tools
- In-app guidance module (guides/engagements/onboarding) — the "drive adoption" side
- In-product surveys/feedback (NPS, polls)
- Session replay / heatmaps
- AI assistance (natural-language analysis, anomaly signals, root cause)

### L2 — Variant / Optional Structure

- Experimentation and feature flags (module in some products; standalone platforms exist as a separate Type)
- Feedback aggregation into product requests/roadmap handoff
- Employee analytics over third-party apps via browser extension (DEX-adjacent posture)
- AI-agent usage analytics
- Cross-channel orchestration (email + in-app journeys)
- Predictive models (churn/propensity-style predictions)
- OEM/embedded analytics (usage platform resold inside ISV products)
- Identity posture: identified B2B users vs anonymous B2C visitors vs hybrid
- Privacy/regional posture: opt-out, PII minimization, data residency (EU/India observed), consent
- Deployment/packaging: standalone platform vs suite module (CS-suite embedded)

### L3 — Vendor-specific Structure (research notes only)

- Pendo: Product Engagement Score (PES), Leo, Visual Design Studio, Pendo Launcher, Orchestrate, Listen, widget-catalog specifics (e.g., funnel/path widget refresh cadence), frequency bands (low/medium/high thresholds over trailing 30 days), Feature Adoption Pareto benchmark default (80%)
- Gainsight PX: Product Mapper, Tracked Account/User object names, Account Usage Data field set (1/7/30/90-day windows), KC Bot / In-App Hub, Gainsight CS object sync (Company/Person GSIDs)
- Mixpanel: Lexicon, JQL, MTU billing, Mirror, Headless, MCP server, Business Context, simplified ID merge
- Amplitude: Zoning Insights, AI Assistant, Amplitude MCP server, Data (tracking-plan product), Web/Feature Experiment split

## Rejected Findings

1. **"In-app guidance defines the Type"** — rejected. Mixpanel, a leading product in this category, has no native guidance module and reaches guidance tools only via cohort sync. Guidance is a common module (L1), not defining.
2. **"Account rollup defines the Type"** — rejected as L0. B2C product analytics (mobile-analytics era; consumer apps) functions without accounts. Account rollup is the standard B2B deployment shape (L1), near-universal in the §07 context but not required for recognition.
3. **"Adoption = onboarding"** — rejected. Adoption in this Type is a measurement subject (feature uptake, activation, retention, stickiness, utilization); onboarding guidance is one lever some products add.
4. **"This is just web analytics applied to apps"** — rejected. The tracked-user population, product-feature semantics, and account rollup have no equivalent in public-web traffic analytics; the fetched Pendo "Web analytics" article is a dashboard widget, not the core.
5. **"This is a BI tool"** — rejected. The defining difference is the capture layer (SDK/tagging/autocapture into the vendor's own product) and product-usage semantics; BI connects to already-existing data sources.
6. **"This is APM for the UI"** — rejected. APM measures request/operation performance telemetry; this Type measures user/feature behavior. Same instrumented product, different telemetry subject (consistent with the processed APM research notes, which list usage analytics as an adjacent extension).

## Boundary Findings

1. **vs Customer Success Platform (§07 sibling)** — the sharpest boundary. Usage platform = capture + analysis of product usage (measurement). CS platform = managed customer workflow (health scores, success plans, plays, renewals, QBRs) that *consumes* usage as one input. Evidence: ChurnZero (CS) integrates Pendo and Mixpanel as data sources; Gainsight PX objects sync into Gainsight CS objects. Structural test: remove usage capture → a CS platform still functions on support/billing/CRM signals; remove CS workflow → a usage platform still functions for product teams. Products straddle: Gainsight PX exists *because* the two are adjacent.
2. **vs Customer Health Monitoring (§07 sibling)** — health monitoring aggregates multiple signal types into account-level scores with thresholds/alerts; the usage platform produces and analyzes the usage signal at event/user/feature granularity. Adoption dashboards per account are the overlap zone.
3. **vs APM / Observability (§14, processed)** — same instrumented product, different telemetry: performance (latency/error/traces per operation) vs behavior (who used which feature). Both may ship "usage analytics" extensions; the centers differ.
4. **vs Web Analytics** — public-site traffic (sessions, campaigns, anonymous visitors) vs product feature usage by tracked users. Different subject, different identity model, different semantics.
5. **vs CDP (§06)** — both ingest behavioral events; CDP centers on the unified customer profile for marketing activation across channels; usage platform centers on product usage/adoption measurement. Cohort sync is the bridge between them.
6. **vs A/B Testing Platform (§06, processed)** — experimentation (variants, randomization, causal decision) is a distinct structure; present here only as an optional module (Amplitude Experiment, Mixpanel flags, Pendo guide A/B).
7. **vs BI Platform (§13)** — BI analyzes connected data sources; usage platform owns its capture layer and product-usage semantics. Some usage platforms export to warehouses and can then be queried by BI — complementary, not the same Type.
8. **vs Product Management Platform (§12)** — roadmap/backlog system of record vs usage measurement. Pendo Listen (feedback → product requests) creates a one-way bridge; roadmap management is not this Type's core.
9. **vs in-app guidance-first products (Digital Adoption Platform category — no directory leaf)** — guidance-first products center on delivering in-app onboarding/guidance; usage platforms center on measuring usage and may bundle guidance. The directory currently has no leaf for the guidance-first category; flagged in STATUS Boundary Issues.
10. **vs Digital Employee Experience Management (§14)** — Pendo's browser-extension employee analytics (app catalog, license utilization of third-party apps) approaches DEX territory; it is a variant posture of this Type, not the core.
11. **vs Voice of Customer / Customer Feedback Management (§07)** — in-product surveys are a module here; VoC platforms center on feedback programs across channels.

## Historical / Market-Sample Check (§24)

- **Mobile-analytics era products** (event + user + retention/funnel analytics for consumer apps): fit L0 fully — no accounts, no guidance required.
- **Admin-console usage reports** (SaaS vendor dashboards showing per-customer usage and license utilization): fit L0 — instrumented product + users + events + usage analytics, without funnels/cohorts/AI.
- **License-utilization tracking**: fits (Pendo ships it as a widget requiring seat metadata).
- **Public-web analytics products**: do NOT fit L0 (anonymous visitors, no product-feature semantics, no tracked user population) — this non-fit is the boundary discriminator, not a failure of the definition.
The definition therefore survives older and differently positioned products; it does not over-fit to the current B2B SaaS + AI-assistant implementation.

## Uncertainties

- Amplitude's account-level reporting was not verified in the fetched pages (docs home only); account rollup is asserted as "common across B2B deployments" via Pendo/PX/Mixpanel evidence, with implementation variance noted.
- Gainsight PX "Adoption Analysis" report details were not fetched (category page only); adoption analysis is asserted at structure level, not metric level.
- ChurnZero evidence is Tier-2 marketing only; used solely for the boundary direction (integration list), not for operational claims.
- Exact pricing models (MTU vs event-based), numeric limits, and refresh cadences are vendor facts (L3) and are deliberately excluded from the final document.
- The directory has no leaf for guidance-first (digital-adoption) products; if one is added later, the guidance-module boundary should be re-examined jointly.

## Final Synthesis

A Product Usage / Adoption Platform is vendor-side software that instruments an organization's own digital product, captures how real end users actually use it as user-bound usage events, and analyzes those events into adoption measurements — which features are used, by whom, how often, how usage develops over time, and how it rolls up to customer accounts. Around that core, mature products add: a usage-taxonomy layer (tagging/tracking plans/dictionaries with validation), segments and cohorts, a standard report vocabulary (trends, funnels, retention, paths, stickiness, time-to-first-use, adoption rankings, license utilization), dashboards, identity resolution, warehouse/API integration and cohort sync to marketing and CS tools, and — in many but not all products — adoption-driving modules: in-app guidance, in-product surveys, session replay, experimentation, feedback-to-roadmap, and AI assistance. Its center of gravity is measurement; its neighbors are distinguished by what they do with the measurement (CS workflow, health scoring, experimentation, marketing activation) or by what they instrument instead (server performance, public web traffic).
