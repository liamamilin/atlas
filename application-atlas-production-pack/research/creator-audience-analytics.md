# Research Notes — Creator Audience Analytics

## Research Goal

Understand the software Type placed at directory leaf "Creator Audience Analytics" (§27 Media, Entertainment, Creator & Culture): applications through which an individual content creator measures and interprets their own audience and content performance on the platforms where they publish. Determine the defining core, the standard capability set, the variant poles, and the boundaries against the neighboring Types (Social Media Analytics Platform §06, Influencer Marketing Platform §06, platform-native analytics, Creator CRM / Creator Revenue Management / Creator Content Planner §27, Media Audience Management §27).

## Initial Boundary

Working hypothesis before research:

- The Type is the **creator-facing counterpart** of social-media analytics: the operator is the creator (an individual or small creator team), the measured subject is the creator's **own** channels/profiles, and the purpose is audience understanding + content/growth decisions — not brand campaign measurement.
- The data substrate is platform-sourced: either authorized connections to the creator's accounts (OAuth/API) or public observation of channel pages.
- Nearest confusions: (1) Social Media Analytics Platform (§06) — same mechanics, different operator/purpose; (2) platform-native analytics (YouTube Studio, TikTok Analytics, Instagram Insights) — the free built-in layer every creator already has; (3) Influencer Marketing Platform (§06) — brand-side evaluation of creators' audiences; (4) Creator CRM (§27) — audience as individual records vs aggregate metrics; (5) Creator Revenue Management / Creator Affiliate Dashboard (§27, processed) — money objects vs audience objects.
- Prior sibling research already recorded the seam from the other side: research/creator-affiliate-dashboard.md — "Remove commission records, keep audience metrics → Creator Audience Analytics."

## Research Questions

1. Who operates the application (individual creator, creator team, agency, brand)?
2. What is the measured subject — which platform objects (channel, profile, show) and whose?
3. How does data enter the system — authorized account connection, public observation, or both?
4. What are the core metric families (audience size, growth, per-content performance, composition, revenue)?
5. What data-availability rules exist (history backfill limits, platform-imposed aggregation, retroactive corrections)?
6. What do users do with the data (diagnose content, track growth, benchmark, find opportunities, report to sponsors)?
7. What interfaces exist (dashboard, per-content drilldown, competitor views, reports)?
8. Which capabilities are definitional vs common vs optional vs vendor-specific?
9. Where is the boundary to Social Media Analytics Platform (§06) and to platform-native analytics?

## Representative Products

| Product | Pole | Why selected | Evidence tier reached |
|---|---|---|---|
| **Metricool** | multi-network analytics+management suite, freemium, creators→SMBs→agencies | strongest documentation; shows the full metric model and data-availability rules | Tier 1 (help center ×6) + Tier 2 (root, analytics page) |
| **TubeBuddy** | YouTube-specialist growth toolkit (browser extension + web) | platform-specialist pole, toolkit philosophy, public-data competitor tracking | Tier 2 (root, Channelytics tool page) |
| **Morningfame** | YouTube-specialist analytics/benchmark product | benchmark-led philosophy (compare against similar-size channels) | Tier 2 (root) |
| **Iconosquare** | analytics-first multi-network suite for brands/agencies | boundary sample: the brand/agency pole of the same mechanics | Tier 2 (root) |

Rejected/unreachable samples (recorded, no claims made):

- **VidIQ** — vidiq.com and support.vidiq.com timed out repeatedly (3 attempts). Would have been the second YouTube-specialist insights pole. Market context only.
- **Social Blade** — socialblade.com, socialblade.com/info, support.socialblade.com all timed out (3 attempts). The canonical public-data stat-tracker pole is therefore treated **structurally only**; no product-specific claims.
- **SpeakRJ** (2 timeouts), **Trackalytics** (403) — additional public-tracker candidates, unreachable.
- **YouTube Studio analytics help** (support.google.com) — 3 timeouts. The platform-native layer is evidenced indirectly through Metricool's documented platform semantics (YouTube rounding rules, demographics limitations, view-count methodology changes, cited YouTube Help pages).

## Sources

Fetched 2026-09-07:

- Metricool root — https://metricool.com/
- Metricool Analytics product page — https://metricool.com/metricoolanalytics/
- Metricool Help Center root — https://help.metricool.com/en/
- Metrics by social network (hub) — https://help.metricool.com/en/metrics-by-social-network-dnxxf
- YouTube Metrics — https://help.metricool.com/en/youtube-metrics-k8haa
- Instagram Account metrics: breakdowns and charts — https://help.metricool.com/en/instagram-account-metrics-breakdowns-and-charts-is1su
- Historical data available — https://help.metricool.com/en/historical-data-available-5zavf
- Demographics — https://help.metricool.com/en/demographics-c5k5t
- Understanding your metrics (hub) — https://help.metricool.com/en/unserstanding-your-metrics-3lxo2
- TubeBuddy root — https://www.tubebuddy.com/
- TubeBuddy Channelytics — https://www.tubebuddy.com/tools/channelytics/
- Morningfame root — https://morningfa.me/
- Iconosquare root — https://www.iconosquare.com/

Unreachable (limitation recorded): vidiq.com, support.vidiq.com, socialblade.com, support.socialblade.com, speakrj.com, trackalytics.com, support.google.com/youtube, support.tubebuddy.com.

## Product Observations

### Metricool (evidence layer A — official help center, Tier 1)

**Positioning & scope.** Self-described "social media management tool": Planner, Analytics, Reports, Inbox, Flows (DM automation), SmartLinks (link-in-bio), Ads, Approval System, Hashtag Tracker, Campaign Dashboards, Looker Studio connector, AI assistant. Networks: Instagram, TikTok, YouTube, Threads, X, Bluesky, Facebook, Pinterest, LinkedIn, Twitch, Google Business Profile + Meta/Google/TikTok Ads + web/blog metrics. Audience: "3.5M professionals" — creators, SMBs, agencies (white-label for agencies).

**Account structure.** User → **Brand** (a business, brand, or client) → one connected profile per social network under each brand. Connection Dashboard manages the connections. Collaborators can be given access to a specific brand without exposing others (Advanced plan).

**Analytics module structure.** Analytics → select network in sidebar → sections per network. Instagram Account section subtabs: General evolution / Reach-Views / Interactions / Profile activity. Metric selector + "Divide by" breakdown pattern (follower type: Followers/Non-followers/Unknown; content type: Posts/Reels/Stories/Carousel/Ads). Charts over time with hover values; summary cards; comparison with previous period "displayed only when data is available".

**YouTube metric families (documented per network).**
- Growth: Subscribers (rounded down to three significant figures by YouTube), Video views, Revenue, Videos posted.
- Subscriber balance: gained vs lost as two separate values ("Follower Change Breakdown" provided by YouTube).
- Demographics: gender, age, viewers by country, traffic source; age/gender based on logged-in viewers, country on IP; "YouTube may display the demographics of a limited group of viewers. The data may not represent the overall composition of your traffic."
- Revenue: per-video total/partner/ad revenue, impressions, monetized playbacks.
- Published videos (published in period, accumulated performance to date) vs **Viewed videos** (generated views in period regardless of publish date) — a documented distinction with its own help article.
- Per-video: views (can be **negative** — YouTube subtracts fraudulent views), engaged views (legacy counting method), watch time, avg views duration, likes, dislikes, comments, shares.
- Competitors: subscriptions, total views, videos, average likes/dislikes/comments per video.

**Data-availability rules (Historical data article — the strongest single source).**
- Daily sync runs in the early morning, in the account's configured timezone.
- On first connection, the previous 30 days of data are displayed.
- **Follower/subscriber counts cannot be backfilled**: X, TikTok, Instagram, Threads, Bluesky, personal LinkedIn followers, YouTube subscribers, and Instagram Stories "will start being recorded from the day you connect your account and will only be tracked while the account remains linked."
- Changing the Instagram connection method loses prior history (Meta's two API paths access different data).
- New metrics start recording when added to the platform.
- Paid accounts can request deeper synchronization via support chat; the platform API determines the maximum ("Generally, social networks and ad platforms provide data from January 1st of the previous year to the connection date").
- Per-network backfill limits documented: Bluesky 30 days; Threads ~3 months; Pinterest 90 days; YouTube 30 days (+ ~7 days to gather all metrics); X posts 5 days/100 posts on new connection, manual sync up to 1,000 posts within 30 days (Advanced plan).
- Competitors: data synced from the 1st day of the previous month; competitor follower/like counts only from connection day; paid plans can sync up to 300 competitor posts; "It would be possible to have more historical data if it happens that the same competitor has been added by another user before" (shared-observation pool).
- Recent-data lag: "YouTube channel data is organic and some metrics may not be available during the last 2-3 days."

**Demographics rules.** Age/gender/geography available for Facebook, Instagram, Threads, LinkedIn, YouTube, TikTok (business accounts only); platforms generate it only above a **minimum of 100 followers**; **no demographic history** — only the most recent snapshot ("If you want to save the history, we recommend downloading a report from time to time"); "Unknown" gender category; platform deprecation drift documented (Facebook deprecated gender/age demographics in 2024).

**Measurement semantics documented in-product.** Reach is daily-deduplicated by Meta's API; Metricool shows average daily unique reach per content type and explains why it differs from per-publication averages; FAQ: "Why do my metrics differ from Instagram? Differences may occur due to data refresh and aggregation"; "Breakdown availability depends on Instagram API"; "Metricool does not reclassify content."

**Plans.** Free forever (1 brand), Starter, Advanced (collaborators, Looker Studio & API, custom report templates, Zapier). CSV export; Looker Studio connector; MCP connector to AI tools.

### TubeBuddy (evidence layer A for scope/positioning — official product pages, Tier 2)

**Positioning.** "YouTube video and creator workflow optimization software as a service"; browser extension that "shows up in your YouTube Studio"; sign in with Google; requires channel authorization. Tool families: YouTube SEO (Keyword Explorer, SEO Studio, Tag Generator, Rank Tracker), Growth (A/B Thumbnail Test with automatic variant rotation and winner declaration, Best Time to Publish, Trend Alerts, CTR Optimizer), Content management (bulk processing, scheduling), **Audience Discovery** ("Understand what your audience wants with competitor analysis, trend insights, and behavior data": Competitor Analysis, Trend Insights, Audience Behaviour/Retention Analyzer, Niche Finder, Revenue Estimator, Channel Audit).

**Channelytics (analytics tool page).** Competitor/channel comparison: "Visit any competitor's YouTube page… Channelytics will automatically appear and display relevant data for that channel" — public-data observation, no OAuth needed for competitor data. Metrics: total views, subscriber count, **30-day growth**, upload frequency, tags used by competitors; side-by-side comparison with own channel; works on any channel including your own; "real-time data directly on YouTube."

**Tiers.** Free / Pro / Legend / Enterprise plan ladder; audience segments: New Creators / Growing Creators / Teams & Brands (agencies, media companies, multi-channel management). Analytics dashboard ("Channelytics"/"data-analytics") described as revealing "which content drives views, subscribers, and revenue."

### Morningfame (evidence layer A for positioning — official product page, Tier 2)

**Positioning.** "Smarter Analytics for YouTube" + SEO tool. Three stated reasons: (1) guided video optimization for search; (2) **"Morningfame compares your channel with other channels of similar size. With that your statistics are put into perspective and weak spots become visible. Specific recommendations will direct your attention"** — peer benchmarking as the core analytical philosophy; (3) "At a glance Morningfame will show you which videos worked and which didn't" — video-level diagnosis to repeat successes. Explicitly supports small channels.

### Iconosquare (evidence layer A for positioning — official product page, Tier 2; boundary sample)

**Positioning.** "Analytics-first social media management" for **brands and agencies** ("Trusted by +10,000 brands & agencies"; sectors: agencies, multi-location brands, retail, F&B…). Modules: Analytics ("Monitor 100+ real-time social media metrics across every account, post, and platform"; best times to post; custom dashboards), Reporting (automated white-label reports), Scheduling, Collaboration (approval workflows, roles), Conversations (unified inbox), Listening (competitor performance, industry benchmarking, hashtag tracking), AI tools ("Uma" AI analyst — "Ask Uma why your numbers changed"; MCP connection to Claude/ChatGPT/Gemini). Networks: Instagram, Facebook, TikTok, Pinterest, LinkedIn, X, Threads, YouTube. Plans named (e.g., "Excel" plan); 2-week trial; SMB/agency/multi-location segmentation.

**Boundary relevance.** Iconosquare demonstrates that the *same mechanics* (connected accounts → per-network metrics → dashboards/reports/competitor benchmarking) are sold to brand/agency operators as "social media management/analytics." The mechanics do not distinguish the Types; the operator and decision purpose do.

## Cross-product Comparison

| Capability | TubeBuddy | Morningfame | Metricool | Iconosquare |
|---|---|---|---|---|
| Measured subject | own YouTube channel + any public channel | own YouTube channel (+ similar-size peers) | own connected profiles across 11+ networks (+ competitors) | own connected profiles across 8 networks (+ competitors) |
| Data substrate | connected (own channel) + public observation (any channel page) | connected + peer statistics | connected accounts (OAuth/API) + public competitor data | connected accounts + listening |
| Audience size & growth | subscribers, 30-day growth | channel growth vs peers | followers/subscribers + gained/lost balance | follower growth (100+ metrics claim) |
| Per-content performance | video-level (views, CTR patterns via Click Magnet) | video-level worked/didn't-work diagnosis | per-video/per-post views, watch time, engagement; published-vs-viewed distinction | per-post/per-platform metrics |
| Audience composition | (not observed on fetched pages) | (not observed) | demographics: age/gender/geo, platform-gated | (not observed on fetched page) |
| Competitor tracking | Channelytics (public, in-extension) | similar-size channel comparison | Competitors section (public data, shared history pool) | Listening module (competitors, industry, hashtags) |
| Benchmarks | competitor side-by-side | **similar-size channel benchmark (core philosophy)** | competitor comparison; industry inspiration | industry benchmarking |
| Recommendations/interpretation | SEO recommendations, A/B winner declaration | specific recommendations from weak spots | plain-language metric explanations; AI analysis | Uma AI analyst; MCP to LLMs |
| Best-time-to-post | Best Time to Publish tool | (not observed) | best hours to post | best times to post |
| Reports/exports | (not observed) | (not observed) | PDF/CSV reports, Looker Studio, scheduled reports | white-label reports |
| Publishing/action integration | scheduling, bulk edits, A/B testing | guided optimization workflow | planner, inbox, ads, SmartLinks | scheduler, inbox, approval workflows |
| Revenue metrics | Revenue Estimator (calculator) | (not observed) | YouTube revenue per video | (not observed) |
| Operator | creator (new→growing→teams/brands) | creator (small channels emphasized) | creator/SMB/agency | brand/agency/SMB |
| Pricing posture | freemium plan ladder | (not observed on fetched page) | free forever + paid tiers | trial + paid plans |

## Canonical Model (abstraction layers)

### L0 — Defining Invariant

The smallest structure without which the product stops being recognizable as creator audience analytics:

1. **Creator-owned platform channels/profiles as the measured subject** — the accounts the creator publishes under (YouTube channel, TikTok/Instagram profile, podcast show, etc.).
2. **Platform-sourced audience & content metrics accumulated over time** — audience size (followers/subscribers), content performance (views/engagement), observed as time series from the platforms (via authorized connection or public observation).
3. **A creator-facing interpretation surface** — the data is presented to the creator for their own growth and content decisions.

Remove creator-ownership → third-party audience research / influencer evaluation (different Type). Remove platform sourcing → web analytics (different Type). Remove the time dimension → a snapshot counter, not analytics. Remove the creator-facing surface → a data pipeline, not an application of this Type.

### L1 — Common Mature Structure

Present across the sampled market, not required for recognition:

- **Connected-account ingestion** — OAuth/API authorization of the creator's platform accounts (Metricool Connection Dashboard; TubeBuddy channel authorization).
- **Growth tracking with gained/lost balance** — follower/subscriber counts plus subscriber gains and losses as separate values (Metricool documents YouTube's Follower Change Breakdown).
- **Per-content performance drilldown** — views, watch time, engagement per video/post; published-in-period vs viewed-in-period distinction.
- **Audience composition** — platform-aggregated demographics (age/gender/geography), availability-gated by the platforms.
- **Competitor/peer tracking** — public-data observation of other channels (TubeBuddy Channelytics, Metricool Competitors, Iconosquare Listening; Morningfame's similar-size peers).
- **Period comparison** — current vs previous period deltas.
- **Best-time-to-post / audience-activity insights.**
- **Reports and exports** — PDF/CSV, scheduled and (in the brand pole) white-label reports.
- **Benchmarks** — comparison against competitors or similar-size peers.
- **Recommendation/interpretation layer** — plain-language explanations, guided recommendations, AI analysts.

### L2 — Variant / Optional Structure

- **Platform scope**: single-platform specialist (TubeBuddy, Morningfame — YouTube) vs multi-network (Metricool, Iconosquare).
- **Data substrate emphasis**: connected-account analytics vs public-observation tracking (the Social Blade-class pole; structurally inferred, product unreachable) vs both.
- **Analytics-only vs analytics+action**: pure measurement vs bundled publishing/planning/inbox/ads (Metricool, Iconosquare, TubeBuddy all bundle action; the pure-analytics pole exists in the market but was not directly sampled).
- **Operator**: individual creator (freemium self-serve) vs creator teams vs agencies/brands (white-label, roles, client brands).
- **SEO/keyword research** (YouTube-specialist pole), **A/B testing** (TubeBuddy thumbnails/titles), **revenue metrics** (YouTube revenue; revenue estimators), **listening/hashtags** (Iconosquare), **web/ads analytics extension** (Metricool), **AI interpretation depth** (metric Q&A, MCP connectors).
- **Public-data competitor history pooling** (Metricool: a competitor's history can be deeper if another user already tracked it).

### L3 — Vendor-specific (research notes only)

- Metricool: Brand container concept; per-network backfill limits (Bluesky 30d / Threads ~3mo / Pinterest 90d / YouTube 30d+7d / X 5d-100-posts new + 1,000-post manual sync); competitor 300-post paid sync; SmartLinks, Flows, Hashtag Tracker, Looker Studio connector, MCP.
- TubeBuddy: Channelytics in-extension overlay; Click Magnet (CTR analysis, Legend+Enterprise); automatic A/B winner declaration; Free/Pro/Legend/Enterprise ladder; "10M+ creators" marketing claim.
- Morningfame: similar-size-channel benchmark method; guided optimization flow; invite/credit model (not verified — not claimed).
- Iconosquare: Uma AI analyst; MCP integration; white-label reports; "100+ metrics" and "10,000+ brands" marketing claims.

## Vendor-specific Findings

See L3 above. Additionally: Metricool documents platform-side metric-definition drift handling (Instagram replacing Impressions with Views; YouTube's August 2026 view-count change) — evidence that these products must continuously re-map platform metric definitions, a structural property of the Type rather than a vendor feature.

## Boundary Findings

1. **vs Social Media Analytics Platform (§06)** — sharpest seam. Same mechanics (connected accounts, per-network metrics, dashboards, competitor benchmarking); different operator and decision purpose: §06 serves marketing teams measuring brand presence/campaigns; this Type serves the creator measuring their own audience for content/growth decisions. Products straddle deliberately (Metricool and Iconosquare sell to both creators and brands/agencies; TubeBuddy sells "Teams & Brands" plans). The mechanics cannot separate the Types; the operator + data-subject + decision loop can. **Joint review recommended when social-media-analytics-platform is processed.**
2. **vs platform-native analytics (YouTube Studio, TikTok Analytics, Instagram Insights)** — the platforms provide creator-facing analytics natively and free. The third-party Type exists because of: cross-platform unification, self-accumulated history beyond platform retention, competitor/peer tracking, benchmarks, recommendations, reporting/export, and action integration. Remove the third-party layer → platform-native analytics is a capability of the publishing platform, not this Type. (Platform-native help pages unreachable; layer evidenced structurally and via Metricool's documented platform semantics.)
3. **vs Influencer Marketing Platform (§06)** — brand-side evaluation of creators' audiences (audience quality, fake-follower detection, discovery). Same data objects, opposite side of the relationship. Remove creator-as-owner → influencer marketing.
4. **vs Creator CRM (§27)** — aggregate audience metrics vs individual fan relationship records. Remove aggregation, add person-level records and outreach → Creator CRM.
5. **vs Creator Revenue Management (§27) / Creator Affiliate Dashboard (§27, processed)** — money objects (commissions, payouts, memberships) vs audience objects. Sibling research recorded the seam from the affiliate side: "Remove commission records, keep audience metrics → Creator Audience Analytics." Revenue metrics *inside* analytics (e.g., YouTube revenue display) are a measurement view, not a revenue system of record.
6. **vs Creator Content Planner (§27) / Social Media Management tools** — measurement as primary vs planning/publishing as primary. Products bundle both (Metricool planner+analytics); the seam is the primary object (metrics/time series vs content calendar).
7. **vs Media Audience Management (§27)** — broadcast/panel/ratings audience measurement for media organizations vs creator platform metrics. Different industry substrate and data sources.
8. **vs Consumer Research Platform (§06)** (SparkToro-class) — researching external audiences vs measuring one's own audience.

**"Remove what, and it becomes another Type" tests:**
- Remove creator-ownership (measure others' audiences for a brand) → Influencer Marketing / Social Media Analytics.
- Remove platform sourcing (own-site data) → Web Analytics.
- Remove the time series (snapshot only) → a counter widget, not this Type.
- Keep metrics, add fan-level records → Creator CRM.
- Keep metrics, add money objects as system of record → Creator Revenue Management.
- Remove measurement, keep scheduling/publishing → Creator Content Planner / Social Media Management.
- Remove the third-party layer → platform-native analytics capability.

## Historical / Market-Sample Check

- Platform-native creator analytics predates the modern third-party market (YouTube's early creator-facing analytics; podcast download-stat dashboards; newsletter subscriber/open analytics). All fit L0: creator-facing, platform-sourced, over time.
- Public stat trackers (the Social Blade-class pole) historically accumulated audience-size history by observing public counts — the same "history begins when tracking begins" rule Metricool documents for connected data. The pole fits L0 via the public-observation substrate.
- No OAuth, multi-network unification, AI, or publishing integration is required by the definition — all are L1/L2. The definition is not overfit to the current multi-network SaaS pattern.

## Uncertainties

1. **VidIQ and Social Blade unreachable** — the insights-led YouTube-specialist pole rests on TubeBuddy/Morningfame; the public-tracker pole is treated structurally (no product claims). Both are canonical market names; their absence weakens breadth, not the core model.
2. **TubeBuddy / Morningfame / Iconosquare evidence is Tier-2** (marketing/product pages). Claims kept at positioning/scope level; no internal-workflow claims made for them.
3. **Platform-native analytics help pages unreachable** — the platform-native layer is evidenced structurally and through Metricool's documented platform semantics (rounding, demographics gating, view-count methodology changes).
4. **Audience-composition depth in the specialist pole** — TubeBuddy/Morningfame demographic surfaces were not observed on fetched pages; composition is therefore L1 with the multi-network pole as primary evidence.
5. **Pure-analytics-only products** (no publishing/action layer) were not directly sampled; their existence is market context, not documented fact.
6. **Category naming** — the leaf name is a directory construction; observed market labels are "YouTube analytics tool," "channel analytics," "social media analytics," "smarter analytics for YouTube." The referent (creator-facing audience/content measurement) is real and stable across labels.

## Final Synthesis

Creator Audience Analytics is the **creator-side measurement application**: the creator's own platform channels/profiles are the measured subject; platform-sourced metrics about audience size, growth (including gained/lost balance), per-content performance, and (platform-gated) audience composition accumulate as time series; and a creator-facing surface interprets them for growth and content decisions. The defining data rule of the Type is that **audience-size history begins when tracking begins** — platforms do not backfill follower/subscriber history, so the application's value compounds with continued connection (and the public-observation pole exists largely to accumulate such history independently). Around this core, mature products add connected-account ingestion, competitor/peer tracking, benchmarks, period comparison, best-time insights, reports/exports, and an interpretation layer (increasingly AI-assisted). The market expresses the Type through poles: platform-specialist (toolkit-led or benchmark-led) vs multi-network suite; analytics-only vs analytics bundled with publishing/action; individual-creator freemium vs team/agency packaging. The same mechanics are sold to brand/agency operators as Social Media Analytics — the operator, data subject, and decision loop are what keep the Types distinct.
