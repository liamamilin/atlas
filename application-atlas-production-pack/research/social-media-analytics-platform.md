# Research Notes — Social Media Analytics Platform

## Research Goal

Understand the software Type placed at directory leaf "Social Media Analytics Platform" (§06 Marketing, Advertising & Growth): applications through which an organization (marketing team, brand, agency) measures the performance of its own social media presence and, commonly, its competitors — and turns platform-sourced metrics into dashboards, benchmarks, and reports that inform social-marketing decisions. Determine the defining core, the standard capability set, the variant poles, and the boundaries against the neighboring Types (Social Media Management Platform §06, Social Listening Platform §06, Creator Audience Analytics §27, Social Publishing Platform §06, platform-native analytics, Marketing Analytics Platform §06, Influencer Marketing Platform §06, Competitive Intelligence Platform §06).

Two sibling passes pre-flagged joint reviews that this pass must discharge:

- research/creator-audience-analytics.md — "same mechanics… different operator and decision purpose… Joint review recommended when social-media-analytics-platform is processed."
- research/social-listening-platform.md — "own connected accounts vs public conversation… Joint review recommended when social-media-analytics-platform is processed."

## Initial Boundary

Working hypothesis before research:

- The Type is the **organization-side measurement application** for social media: the operator is a marketing/social team (brand, agency), the measured subject is the organization's **own** connected profiles plus (commonly) competitor profiles, and the deliverable is performance understanding + stakeholder reporting.
- The data substrate is platform-sourced, with authorized account connections as the standard implementation and public observation as the standard implementation for competitor data.
- Likely confusions:
  1. Social Media Management Platform (§06 sibling) — suites bundle publishing + engagement + analytics; seam must be center of gravity, not feature lists.
  2. Social Listening Platform (§06, processed) — own connected accounts vs query-defined public conversation.
  3. Creator Audience Analytics (§27, processed) — same mechanics, different operator and decision loop.
  4. Platform-native analytics (Instagram Insights, TikTok Analytics, YouTube Studio, Meta Business Suite) — the free built-in layer every network provides; not a directory Type but must be positioned.
  5. Marketing Analytics Platform / Marketing Attribution (§06) — whole-funnel measurement vs channel-specific social measurement.
  6. Social Publishing Platform (§06), Influencer Marketing Platform (§06), Competitive Intelligence Platform (§06, processed).
- Unknowns going in: (a) is connected-account ingestion definitional or an implementation detail; (b) is competitor benchmarking definitional or common-not-core; (c) are paid-social metrics core or extension; (d) what data-availability rules are documented well enough to assert.

## Research Questions

1. What is the central measured object — the profile, the post, the network, the campaign?
2. How does data enter the system — authorized connections, public observation, ad-account connections, manual/other sources?
3. What metric families are computed (audience size & growth, content performance, engagement, reach, paid)?
4. What data-availability rules exist (backfill limits, audience-count backfill, refresh cycles, latency, reporting-period vs lifetime semantics)?
5. What do users do with the data (monitor, compare periods, benchmark competitors, diagnose content, report to stakeholders/clients)?
6. How do reports and exports work (custom builders, scheduling, white-label, PDF/CSV, BI connectors, APIs)?
7. What interpretation layer exists (automated insights, takeaways, best-time insights, AI)?
8. How does the analytics module relate to publishing/engagement in suite-embedded products?
9. Where is the seam vs SMM, listening, creator analytics, platform-native analytics, marketing analytics?
10. Which capabilities are definitional vs common vs optional vs vendor-specific?

## Representative Products

Selected for market representation + documentation completeness + different product philosophy + different customer tier:

| Product | Pole | Customer tier | Evidence tier reached |
|---|---|---|---|
| **Sprout Social** | suite-embedded analytics (core pillar) + upsold Premium Analytics | mid-market/enterprise | Tier 1 (help center: data-availability article + metrics article + category structure) + Tier 2 (analytics feature page) |
| **Buffer** | SMB freemium suite; publishing-first with a rebuilt analytics layer ("Insights") | SMB/creators/agencies | Tier 2 (Insights feature page, incl. FAQ) + Tier 1-structure (help center category listing) |
| **Rival IQ** | standalone, competitive-benchmark-led analytics | agencies/mid-market (agency, CPG, higher-ed, nonprofit verticals) | Tier 2 (root + competitive-analysis product page) |
| **quintly / Facelift Data Studio** | analytics-only enterprise data platform (no publishing/engagement at all) | enterprise (brands, agencies, media) | Tier 2 (root; includes rename announcement + platform structure) |

Rejected/unreachable samples (recorded, no claims made):

- **Hootsuite Analytics** — hootsuite.com product pages timed out twice (2 attempts). Would have been the second suite-embedded pole; Sprout covers that pole with stronger evidence. Market context only.
- quintly help center — help.quintly.com 404; the product's knowledge base has moved to a Facelift-hosted URL (not fetched; root page sufficed).

## Sources

Fetched 2026-09-07. All direct from official vendor surfaces.

- Sprout Social analytics feature page — https://sproutsocial.com/features/social-media-analytics/
- Sprout Social help center search (analytics) — https://support.sproutsocial.com/hc/en-us/search?query=analytics (article-title structure)
- Sprout Social — "What data is available in Reports?" — https://support.sproutsocial.com/hc/en-us/articles/360027867052-What-data-is-available-in-Reports (full per-network backfill/update table)
- Sprout Social — "What metrics are available in-plan and for Premium Analytics?" — https://support.sproutsocial.com/hc/en-us/articles/360034074631-What-metrics-are-available-in-plan-and-for-Premium-Analytics (metric catalog + plan gating)
- Buffer Insights feature page — https://buffer.com/analytics (incl. FAQs)
- Buffer help center root — https://help.buffer.com/en/ (category structure; "Analyzing Your Data" category)
- Rival IQ root — https://www.rivaliq.com/
- Rival IQ competitive analysis product page — https://www.rivaliq.com/product/competitive-analysis/
- quintly / Facelift Data Studio root — https://www.quintly.com/

Unreachable (limitation recorded): hootsuite.com product pages (2 timeouts); help.quintly.com (404). No third-party review sites used.

## Product Observations

### Sprout Social (evidence layer A — official help center Tier 1 + feature page Tier 2)

**Positioning & scope.** Analytics is one of three core platform pillars (Publishing / Engagement / Analytics), with **Premium Analytics** as an upsold premium solution ("Prove your social media ROI with customized data and reports") and Listening, Influencer Marketing, Employee Advocacy, NewsWhip as additional/premium products. Feature page promise: "Leverage network specific, cross-network, paid, competitive and internal reports."

**Report family (feature page).** Profile Performance Report ("high-level overview of performance across all connected profiles"), Post Performance Report ("cross-channel performance at the post level"), Tag Report (inbound/outbound tagged messages — campaign aggregation via tags), Case Team Activity Report (team productivity), Network Reports (per-network: Instagram, Facebook, X, Bluesky, Threads, TikTok, LinkedIn, YouTube, Pinterest), Competitor Reports ("benchmark against your organization's performance"), Paid Performance Reporting ("Evaluate social advertising across channels"; separate paid-social feature page), Hashtag Tracking. Explicit organic-vs-paid separation ("Distinguish between organic and paid performance").

**Trial onboarding flow (feature page).** "Start your trial → Connect profile(s) → Get data" — account connection is the first-class setup step.

**Data-availability rules (help article — the strongest single source, per-network table).**

- "When you connect a profile, Sprout automatically retrieves historical data for that profile. The length of historical backfill and the time it takes to pull data into Sprout depends on the network you connect."
- Backfill depths vary per network and per metric class: e.g. Facebook profile metrics 2 years but Facebook profile *engagement* metrics "No Backfill"; Facebook posts "Last 500 posts"; Instagram "Up to 90 days back for most metrics, but only as early as the date you converted to Instagram Business. 30 days for follower count"; TikTok "60 days of metrics upon initial connection… **Follower count cannot be backfilled**. Only net audience growth for 60 days"; X profile metrics 1 year; Threads and Bluesky 185 days; Pinterest profile metrics "None"; YouTube "full video list along with the last 30 days of metrics", deeper history available "within 36–72 hours, as Sprout needs to register a reporting job with YouTube's API"; GA4 backfill 1 year / 10,000 data entries.
- **Competitor data is governed differently**: X Competitor "Profile Metrics: Audience — **No Backfill** — every day, take today's snapshot"; Facebook Competitor followers "Does not backfill Audience data… Follower counts for owned Facebook Pages are delayed up to 48 hours"; Instagram Competitor audience "Does not backfill Audience data but can backfill the last 30 days of posts"; X Competitor engagement "Last 30 days of posts"; Facebook Competitor posts "500 posts".
- **Refresh schedules** documented per network: daily updates standard; Instagram posts refresh "every 15 minutes you're active"; Stories hourly; TikTok/YouTube data "may be delayed by 72 hours".
- **Measurement semantics**: article link defines the difference between "Reporting Period" and "Publishing Period (Lifetime)" data gathering — a documented two-mode semantics (metrics aggregated over a reporting window vs metrics accumulated on a post since publication).

**Metric model (help article).** Metrics organized per network by **Type — Owned Profile, Owned Post, Paid**. Catalog examples: Followers, Net Follower Growth, Followers Gained / Followers Lost (gained/lost balance), Following, Impressions, Organic Impressions, Paid Impressions, Engagements, Organic/Paid Engagements, Engagement Rate (per Impression), Video Views (organic/paid, autoplay/click-to-play, partial/complete), Reactions, Comments, Shares, Saves, Post Link Clicks, Profile Views/Actions, Audience by Age/Gender/Country/City. A subset of metrics is **plan-gated** ("What's included with Premium Analytics?"); e.g. Threads reposts/quotes and some audience-demographic metrics are Premium-only. A Google Analytics connection exists as an additional data source.

**Help-center structure.** "Analytics & Reporting" category with sections My Reports / Report Glossaries & Guides / Additional Reporting Features; per-network sections ("Analyzing your Instagram performance", "Facebook reporting features", …); "Business Intelligence (BI)" section under integrations; article titles: "My Reports", "Introduction to Reporting", "How do I use the Competitor Posts Report?", "How do I use the Tag Performance Report?", "How do I connect Google Analytics to Sprout?".

### Buffer (evidence layer A for scope/positioning — official feature page with FAQ, Tier 2)

**Positioning.** Buffer's analytics product is **Insights** — "Analytics that show you your next move… for everyone from a solo creator to an agency reporting to a client." FAQ documents lineage: "Insights is a complete rebuild of the analytics that used to live in Analyze." Networks: Facebook, Instagram, TikTok, LinkedIn, Threads, YouTube, X, Pinterest, Bluesky, Mastodon — "All the networks you manage in Buffer, in one place."

**Structural observations.**

- All-channels view + per-channel drilldown ("See all your channels at a glance, or drill into any one for a closer look"); side-by-side channel comparison.
- Metric families shown live: likes, comments, impressions, new followers — each with **previous-period comparison** ("6,892 in previous period", "-27%").
- **Takeaways** — an interpretation layer that "turn your results into clear suggestions you can act on in a click": "Revise Posting Schedule", "Boost Posting Frequency" (posting-goal tracking), "Repost Your Engaging Content" — each carrying a one-click handoff into Buffer's own publish/schedule/post-detail surfaces. Measurement feeding action inside the same suite.
- **Metric transparency**: "Every metric carries a clear definition and update frequency" (tooltip showing last update + next sync window) — refresh semantics surfaced in-product.
- **Plan-gated history depth**: "The core of Insights is included on Buffer's free plan… Paid plans add more for teams and agencies who need a **longer view of their history** and client-ready exports."
- **Exports**: PDF/CSV on paid plans, framed for agencies' client reporting.
- **Benchmarks**: aggregate industry/product benchmarks ("how posts perform across platforms, industries, and account sizes"; Instagram "over 250,000 other creators") — a vendor-aggregated benchmark layer alongside (not replacing) competitor tracking.
- **AI/MCP**: MCP server + public API so Claude/ChatGPT-class agents can answer performance questions; Buffer API listed as a first-class product surface.
- Help center category "Analyzing Your Data" (5 articles) — analytics is one module beside Channel Management, Creating/Scheduling Posts, Engaging with Comments, Team Collaboration, etc. (publishing-first suite structure).

### Rival IQ (evidence layer A — official product pages, Tier 2)

**Positioning.** "Powerful social media analytics. No data scientist required… on-demand social media analytics, alerts, and custom reports" for digital marketers. Solutions verticals: Agencies, Consumer Packaged Goods, Health & Beauty, Higher Ed, Nonprofits. Channels: Facebook, Instagram, X/Twitter, YouTube, LinkedIn, TikTok. Now part of Quid (announcement on site).

**Competitive-led philosophy (product page).** "Benchmarking is critical to achieving social success… measuring your success against [the competitive landscape], **instead of just relying on your own performance over time**" — the benchmark layer articulated as the product's organizing idea. "Always-on benchmarks" supply "competitive context to all your social metrics."

**Named capabilities.** Competitive leaderboards (engagement metrics, post frequency, follower count); Alerts ("always-on social post and profile monitoring" — in-app and email alerts when competitors post high-performing content); Boosted post detection (machine-learning detection of competitor paid amplification); Positioning comparison (bios/about statements/profile attributes); Landscape and company filters (industry-wide vs head-to-head); Automated insights ("Generate key takeaways based on your performance and time period"); Popular Topics ("phrases and topics that drive social engagement in your landscape"); Custom Dashboards (pre-built + customizable templates).

**Tooling.** Custom Dashboards ("to use interactively or for export"), Scheduled Exports ("delivered via email — even to external collaborators or clients"), Multi-user accounts, Custom Branding ("export any report or chart in your (or your client's) brand colors"), Social Insights API, Google Data Studio Connector, Facebook Ads Analytics, Influencer Tracking, Hashtag Analytics, a Social Listening module ("sentiment and mention data from millions of sources"), Social Media Audits. Free pole: Head-to-Head free reports (one competitor, one network).

### quintly / Facelift Data Studio (evidence layer A — official root page, Tier 2)

**Positioning.** "Social Media Analytics and Competitive Benchmarking Tool… Solving your data and reporting challenges with the most precise analytics." Announcement banner: "quintly officially becomes Facelift Data Studio" (naming drift). Solutions: Brands, Agencies, Media. Networks: Facebook, LinkedIn, Instagram, YouTube, X, Snapchat, TikTok. "Over 10 years" building the tool.

**Pure-analytics structure** — no publishing/inbox module anywhere on the page:

- Analytics: "Track, benchmark and optimize your social media"; "track performance across **hundreds of profiles** in one place. Analyse your performance and gain insights into your competitors, inspiring brands, future clients, social media influencers and more."
- Metrics/dashboards: "Choose from **500+ social media metrics** and from hundreds of customizable dashboards… Create your own dashboards within a few clicks."
- Reporting: "Create or automate reports, exports and live links… set up clients to access **private stats securely**… automated delivery times and formats." (agency/client reporting pole)
- Data/API pole: "Data in Depth — Secure, trusted data quality"; "extensive and powerful API — integrate data… with your favourite analytics tools, business intelligence systems or data warehouses"; **quintly Query Language (QQL)** for writing custom metrics; push to Google BigQuery; integrations with Tableau, Google Data Studio, Brandwatch Vizia.
- Use cases: "Advanced analysis of owned channels"; "Competitive benchmarking"; "Content optimization" (cross-network content performance); "Ad analytics" (paid vs organic); "Customer care and community analysis"; "Campaign analytics"; "Monitoring and focused social listening" (profile-scoped word detection); "Influencer marketing" (campaign ROI).
- Roles named: Social Media Managers, Data Analysts/Strategists, Marketing Directors/CMOs.

## Cross-product Comparison

| Dimension | Sprout Social | Buffer (Insights) | Rival IQ | quintly/Facelift | Layer |
|---|---|---|---|---|---|
| Measured subject | own connected profiles across ~9 networks + competitor profiles | all channels managed in Buffer (10 networks) | own landscape + tracked competitor profiles ("landscape") | hundreds of own profiles + competitors/inspiring brands/influencers | **Core** |
| Data substrate | authorized profile connections + ad accounts + public competitor data + GA connection | authorized channel connections | tracked profiles (own + competitors) + benchmark data | authorized connections + API/data-quality layer | **Core** (connected = standard implementation) |
| Metrics as time series | yes — profile metrics over reporting periods, gained/lost, per-post lifetime | yes — period-over-period charts, follower trends | yes — always-on tracked profiles | yes — 500+ metrics, dashboards over time | **Core** |
| Marketer-facing interpretation surface | yes — report suite + dashboards | yes — dashboards + Takeaways | yes — dashboards, leaderboards | yes — dashboards, custom metrics | **Core** |
| Audience growth w/ gained/lost balance | yes (Followers Gained/Lost, Net Follower Growth) | yes (New followers vs previous period) | yes (follower count leaderboards) | yes | Standard (common) |
| Per-content performance drilldown | yes (Post Performance Report, lifetime metrics) | yes (top posts, per-post) | yes (Social Posts Analysis) | yes (cross-network content comparison) | Standard (common) |
| Organic vs paid separation | yes (explicit; Paid Performance Reporting; paid metric types) | not observed as explicit paid/organic split | yes (Boosted post detection; Facebook Ads Analytics) | yes ("Ad analytics… paid social ads… against your organic content") | Standard (common; ad-account-dependent) |
| Competitor tracking & benchmarking | yes (Competitor Reports; per-network competitor data rules) | not a first-class competitor module (aggregate benchmarks instead) | **yes — organizing philosophy** (leaderboards, alerts, boosted detection, head-to-head) | yes (competitive benchmarking use case; competitor insights) | Standard (common; competitive-led pole exists) |
| Period comparison | yes (reporting-period model, previous-period data in tables) | yes (explicit previous-period deltas) | yes (performance by time period in automated insights) | yes (dashboards over time) | Standard (common) |
| Custom/automated reports | yes (My Reports; scheduled; PDF/CSV via reporting) | yes (PDF/CSV paid) | yes (custom dashboards, scheduled email exports, custom branding) | yes (create/automate reports, exports, live links, automated delivery) | Standard (common) |
| White-label / client reporting | yes (agencies solution; report branding in premium tiers per product pages) | yes (client-ready exports framing) | yes (client brand colors; scheduled exports to clients) | yes (client access to private stats; branded reports) | Standard (common; agency-pole emphasis) |
| API / BI handoff | yes (BI integrations section; Looker Studio-class connectors per integrations pages) | yes (public API + MCP server) | yes (Social Insights API; Google Data Studio connector) | yes (API, QQL custom metrics, BigQuery push, Tableau/Looker/Vizia) | Standard (common; enterprise pole deepest) |
| Interpretation layer (auto-insights/AI) | yes (Premium Analytics positioning; AI pillar in suite) | yes (Takeaways with action handoffs) | yes (Automated insights) | (not observed as a named feature on fetched page) | Standard (common; current-gen) |
| Alerts | not observed at fetched level | not observed | yes (competitor post/profile alerts) | not observed | Optional |
| Best-time/posting-schedule insights | not observed at fetched level | yes (posting-goal takeaway; schedule advice) | not observed | (not observed) | Optional |
| Tag-based campaign aggregation | yes (Tag Report) | yes (tags in client reporting testimonial) | not observed (Post Tags announced) | not observed | Optional |
| Publishing/engagement modules | yes (suite pillars) | yes (suite pillars) | no | **no** | Optional (suite packaging) |
| Listening module | yes (premium product) | no | yes (module) | yes (profile-scoped monitoring use case) | Optional |
| Influencer tracking | yes (separate product) | no | yes (module) | yes (use case) | Optional |
| Web analytics extension | yes (Google Analytics connection) | no | no | no | Optional |
| Aggregate industry benchmarks | no | yes (250k/200k creator pools) | yes (always-on industry benchmarks; live benchmark content) | no | Optional (vendor-aggregated pole) |
| Custom metric authoring | no (plan-gated metric catalog) | no | no | yes (QQL) | Optional (enterprise data pole) |
| Free pole | trial | free core (history depth plan-gated) | free head-to-head reports; free trial | demo-led (no free tier observed) | Optional (packaging) |
| Operator | marketing teams/agencies (mid-market→enterprise) | SMB/creators/agencies | digital marketers/agencies (verticals) | brands/agencies/media (enterprise) | variant |

Stable commonalities across all four (evidence layer B): the own-presence measured subject; platform-sourced metrics accumulated over time; the marketer-facing dashboard/report surface; audience-growth and per-content metric families; period comparison; competitor/benchmark layer; report/export machinery. The suite-embedded products (Sprout, Buffer) additionally bundle publishing/engagement; the standalone products (Rival IQ, quintly) do not — measurement-first is viable, so measurement is the Type's center.

## Canonical Abstraction

### L0 — Defining Invariant

Three structures held jointly, plus the organizational purpose:

1. **The organization's own social media presence as the measured subject** — a defined set of social profiles/accounts operated by the organization (brand, agency client, media outlet), tracked as durable entities in the application. Remove → the tool measures someone else's audiences (influencer marketing) or the public conversation at large (listening) — different Types.
2. **Platform-sourced performance metrics accumulated as time series** — audience size and growth, content performance, engagement, reach — pulled from the social networks and retained as history the application owns. The authorized connection is the standard implementation (reach/impressions/paid metrics exist only through it); public observation is the standard implementation for third-party/competitor data. Remove the time dimension → a snapshot counter; remove platform sourcing → web analytics.
3. **A marketing-facing interpretation surface** — dashboards, cross-network and per-network views, period comparisons, and reports that turn the accumulated metrics into social-marketing decisions and stakeholder-facing reporting. Remove → a data pipeline/connector, not an application.

Purpose clause: operated by the organization's marketing/social function to understand, benchmark, and prove the performance of its social media activity.

Jointly-held is load-bearing: 1+2 without 3 = an ingestion pipeline; 1+3 without 2 = a snapshot viewer; 2+3 without 1 = generic social-data analytics with no organizational subject (the listening/creator poles).

### L1 — Common Mature Structure

Present across the sampled market; not required for recognition:

- connected-account ingestion with a connection-management surface (the "connect profiles → get data" onboarding grammar)
- audience growth with gained/lost (net) follower balance
- per-content (post/video-level) performance drilldown with lifetime metrics
- organic vs paid separation; paid metrics via ad-account connections
- competitor tracking and benchmarking (head-to-head, leaderboards, industry context)
- period-over-period comparison as a default reading mode
- custom report builders, scheduled/automated delivery, exports (PDF/CSV), branded/white-label reporting for clients
- API/BI handoff (connectors, data-warehouse push)
- interpretation layer: automated insights/takeaways, AI assistance (current generation)
- metric transparency (definitions + refresh frequency surfaced)

### L2 — Variant / Optional Structure

- packaging: suite-embedded module (analytics beside publishing/engagement) vs standalone analytics product vs enterprise data-platform pole (custom metrics, warehouse push, API-first)
- competitive-led pole (benchmarking as the organizing philosophy vs measurement of own presence as the base grammar)
- customer tier: SMB freemium (history depth plan-gated) vs enterprise (demo-led, custom metric authoring)
- agency/multi-client structures (client spaces, white-label, scheduled client exports)
- alerts on competitor activity/performance
- tag-based campaign aggregation
- aggregate industry benchmarks (vendor-maintained pools)
- optional modules: listening, influencer tracking, hashtag analytics, web-analytics connection (Google Analytics), customer-care metrics
- free poles: free-core analytics, free head-to-head competitor reports

### L3 — Vendor-specific (research notes only)

- Sprout: Premium Analytics plan gating of specific metrics; the per-network backfill table (Facebook 2y profile metrics / no-backfill engagement profile metrics / 500 posts; Instagram 90d + 30d followers + business-conversion date floor; TikTok 60d + no follower backfill; X 1y; Threads/Bluesky 185d; Pinterest none; YouTube 30d + 36–72h reporting-job history; GA4 1y/10k entries); Reporting Period vs Publishing Period (Lifetime) semantics article; per-network refresh schedules (15-min Instagram while active, hourly Stories, 48h/72h delay classes); Tag Report / Case Team Activity Report; competitor-data rules per network.
- Buffer: Analyze→Insights rebuild; Takeaways with one-click action handoffs into Buffer's own create/schedule surfaces; metric-definition + update-frequency tooltips; free-core with plan-gated history; MCP server + public API; 250k/200k-creator benchmark pools.
- Rival IQ: always-on industry benchmarks; boosted-post ML detection; positioning comparison (bios/profile attributes); landscape vs head-to-head filters; scheduled email exports to clients; custom branding; Quid membership.
- quintly/Facelift: 500+ metrics claim; QQL custom-metric language; BigQuery push; Tableau/Looker Studio/Brandwatch Vizia integrations; client "private stats" spaces; Facelift rename; "hundreds of profiles" scale claim.

## Vendor-specific Findings

- Packaging variance around a shared engine: Sprout sells Analytics as a core pillar plus a separate "Premium Analytics" upsell; Buffer renamed and rebuilt its analytics (Analyze→Insights); Rival IQ sells competitive analysis with listening/ads/influencer as modules; quintly sells pure analytics+data and even renamed (quintly→Facelift Data Studio). One Type, many packaging names.
- Buffer's Takeaways document a structural pattern: measurement surfaces that emit one-click actions into the same suite's publishing tools — the analytics-to-action handoff. Single-product phrasing; generalized cautiously (layer A single-source).
- Rival IQ's page articulates the benchmark layer's value proposition explicitly ("instead of just relying on your own performance over time") — the clearest one-sentence statement of why competitor/benchmark structure sits beside own-presence measurement.
- Sprout's help center is the strongest evidence base for the Type's data-availability physics: backfill varies by network AND by metric class; audience counts and competitor audience data generally cannot be backfilled; refresh cycles and latencies are per-network and documented in product help.

## Boundary Findings

1. **vs Social Media Management Platform (§06 sibling)** — sharpest §06-internal seam. Center-of-gravity discriminator: publishing/engagement center (queue, composer, inbox, conversations as primary objects) vs measurement center (metrics, dashboards, reports as primary objects). Every sampled suite ships analytics (Sprout pillar; Buffer pillar; Rival IQ/quintly do not ship publishing), so features cannot separate the Types; the center of gravity can. Removal tests: remove measurement, keep publishing/engagement → SMM; remove publishing/engagement, keep measurement → this Type. **Keep both Types; joint review from the SMM pass recommended.**
2. **vs Social Listening Platform (§06, processed) — DISCHARGES that pass's joint-review flag from this side.** The seam holds: this Type measures the organization's **own connected accounts** (performance of its own posts/channels/ads); listening observes the **public conversation at large** via standing queries (untagged, cross-channel, mostly not the org's own posts). Removal tests both directions: restrict the substrate to connected own accounts → this Type; restrict to query-defined public conversation → listening. Products straddle deliberately: this pass's Rival IQ sells a "Social Listening" module and quintly a profile-scoped "focused social listening" use case; the listening pass's Meltwater sells "Social Media Analytics" as a suite feature. Modules inside a suite do not merge the Types. The listening pass's Meltwater FAQ quote (native analytics "only show activity within individual platforms") also states this Type's third-party value proposition from the outside.
3. **vs Creator Audience Analytics (§27, processed) — DISCHARGES that pass's joint-review flag from this side.** The seam holds and is operator + data subject + decision loop, exactly as the creator pass proposed: a marketing team measuring **brand presence/campaign performance** for marketing decisions vs a creator measuring their **own audience** for content/growth decisions. The mechanics (connected accounts, metric time series, dashboards, competitor benchmarking, reports) are identical and products straddle deliberately — Buffer markets Insights "from a solo creator to an agency"; quintly sells to brands, agencies, and media; the creator pass documented Metricool/Iconosquare selling to both poles. Both Types kept; the §06 leaf is the organization/marketing operator pole, the §27 leaf the individual-creator pole. The identical "history begins when tracking begins" data rule appears on both sides (Sprout's no-backfill audience rows; Metricool's documented backfill limits) — a shared property of platform-sourced measurement, not a discriminator.
4. **vs platform-native analytics (Instagram Insights, Meta Business Suite, TikTok Analytics, YouTube Studio, X Analytics)** — not a separate directory Type; the built-in capability baseline every network provides. The third-party Type's reason to exist is what native tools lack: cross-network unification, self-accumulated history beyond platform-imposed backfill limits, competitor/industry benchmarking, client-grade branded reporting, API/BI handoff, and (in suites) measurement welded to publishing. Consistent with the creator pass's treatment of the native layer. (Platform-native help pages were not fetched in this pass either; positioned structurally.)
5. **vs Social Publishing Platform (§06 sibling)** — publishing center vs measurement center; a subset of finding 1 where the sibling is publishing-only. Suites absorb both.
6. **vs Marketing Analytics Platform (§06)** — channel-specific social measurement vs whole-marketing measurement across web/email/ads/funnel. The seam blurs at the edges: Sprout connects Google Analytics as an extension (web data imported into a social report), but the measured subject remains the social presence. Restrict measured subject to social platform data → this Type.
7. **vs Marketing Attribution Platform / Business Intelligence (§06/§13)** — attribution ties spend to conversions across channels; BI platforms are the reader layer for exported data. Social analytics tools hand data to both (BI connectors, warehouse push in the quintly pole) — the handoff marks the seam rather than a merger.
8. **vs Influencer Marketing Platform (§06)** — third-party creators' audiences vs own brand presence. Influencer tracking appears as an optional module (Rival IQ, quintly, Sprout's separate product) without converting the Type.
9. **vs Competitive Intelligence Platform (§06, processed)** — consistent with that pass's source-bound-vs-entity-bound row: competitive features in this Type remain social-metric-bound (leaderboards, post engagement, follower counts, boosted detection); CI is entity-bound and source-agnostic. Rival IQ's competitive analytics is benchmarking of social presence, not CI.

**"Remove what, and it becomes another Type" tests:**

- Remove the own-presence subject (watch public conversation via queries) → Social Listening.
- Remove the organization (creator measures own audience) → Creator Audience Analytics.
- Remove measurement (keep publishing/inbox) → Social Media Management / Social Publishing.
- Remove platform sourcing (own website data) → Web/Marketing Analytics.
- Keep metrics, add per-signal organizational action loops → drifts toward reputation/engagement territory.
- Remove the time series → snapshot viewer, not analytics.
- Remove the interpretation surface → data pipeline/connector, not an application.

## Historical / Market-Sample Check

- The defining triple (own profiles → platform metrics over time → marketer dashboards/reports) predates the current AI- and benchmark-heavy generation. quintly self-documents "over 10 years" building the same tool; Buffer's FAQ documents its analytics lineage (Analyze → Insights rebuild); the early-2010s standalone social-analytics generation (market context; not fetched, no claims) already ran this grammar. The mid-2000s-to-early-2010s platform-native layer (Facebook Page Insights era) satisfies the same structures inside the network — the Type is era-robust.
- Implementation-check: OAuth-connected ingestion is the modern standard but is treated as implementation, not definition — competitor public-observation data and platform-API-variance (Sprout's YouTube "reporting job" mechanics) show the data path is a negotiated, evolving substrate, and the Type remains recognizable across access regimes.
- Scale/scope check: single-network and multi-network both satisfy the core; "hundreds of profiles" (quintly) vs a handful (SMB Buffer) is scale variance.
- AI check: AI takeaways/assistants are current-generation common structure, not definitional — the Type is fully recognizable without them (Rival IQ/quintly pages stand on pre-AI structures).

## Uncertainties

1. **Hootsuite unreachable** (2 timeouts) — the second suite-embedded pole is held by Sprout alone with strong Tier-1 evidence; market breadth slightly weakened, core model unaffected.
2. **Buffer/quintly/Rival IQ evidence is Tier-2** (product pages). Claims kept at positioning/scope level; no internal-workflow claims asserted for them beyond what their pages state.
3. **Platform-native analytics pages unfetched** — the native layer positioned structurally (consistent with the creator pass's limitation).
4. **Paid-social depth** varies and is ad-account-dependent; the organic/paid split is asserted as common (3 of 4 sampled), not definitional.
5. **Plan-gating details** (which metrics sit behind Premium Analytics, Buffer's history-depth ladder) are vendor plan facts — recorded in research notes, not asserted in the final document.
6. **Category naming drift**: market labels include "social media analytics," "Insights," "competitive social media analytics," "social media analytics and competitive benchmarking," "data studio." The referent (organization-side social performance measurement) is stable across labels.

## Final Synthesis

A Social Media Analytics Platform is the **organization-side measurement application** for social media. Its world is built around three jointly-held structures: the organization's own social profiles as the durable measured subject; platform-sourced performance metrics — audience size and growth (with gained/lost balance), per-content performance, engagement, reach, paid results — accumulated as time series the application owns; and a marketing-facing interpretation surface (dashboards, period comparisons, benchmarks, reports) that turns those metrics into social-marketing decisions and stakeholder-facing reporting. Around this core, mature products add connected-account ingestion, competitor tracking and benchmarking (head-to-head and industry), organic-vs-paid separation, custom/scheduled/branded reports with client-grade exports, API/BI handoff, and an interpretation layer (automated takeaways, increasingly AI-assisted). The Type's data physics are distinctive and well-documented: history depth and backfill are network- and metric-class-dependent, audience-count history generally cannot be backfilled (value compounds with continuous connection), metric definitions belong to the platforms and drift, and refresh cycles/latencies are documented per network. The market expresses the Type through poles: suite-embedded module vs standalone analytics vs enterprise data-platform; competitive-benchmark-led vs own-presence-led; SMB freemium vs agency/multi-client vs enterprise custom-metric. The defining boundaries: vs Social Media Management (publishing/engagement center vs measurement center), vs Social Listening (own connected accounts vs public conversation), vs Creator Audience Analytics (marketing-team operator vs creator operator over the same mechanics), and vs platform-native analytics (the built-in baseline this Type exists to extend).
