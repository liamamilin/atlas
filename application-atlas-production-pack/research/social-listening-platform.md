# Research Notes — Social Listening Platform

## Research Goal

Understand what a "Social Listening Platform" actually is as an Application Type, from real products: what objects exist inside it (queries/topics, collected conversation, metrics, alerts, reports), what its defining workflow is (define → collect → analyze → alert → report), who operates it, and where its boundary runs against the neighboring §06 Types (Social Media Analytics, Social Media Management, Media Monitoring, Brand Reputation Management, Competitive Intelligence, Consumer/Market Research, Voice of Customer) and against search engines / feed readers.

## Initial Boundary

Working hypothesis before research:

- A social listening platform continuously collects public online conversation (social networks foremost, plus forums, reviews, blogs, news) matching user-defined queries, and turns the collected stream into aggregated insight (volume, sentiment, share of voice, themes, audiences).
- Likely confusions:
  1. Social Media Analytics Platform — same "social data" domain, but connected own accounts vs public conversation.
  2. Media Monitoring Platform — same "monitoring" grammar, but editorial coverage vs public conversation.
  3. Brand Reputation Management (processed sibling) — flagged this leaf as its sharpest seam: "remove per-signal organizational action → a listening platform remains".
  4. Competitive Intelligence Platform (processed sibling) — its boundary row already proposes: social-listening is source-bound (social) and topic/consumer-conversation-centric; CI is entity-bound and source-agnostic.
  5. Consumer Research Platform (processed sibling) — held "asked vs observed".
  6. Search Engine / Feed Reader — retrieval and triage vs standing collection + aggregation.
- Unknowns going in: (a) is the analysis layer definitional or is query+collection enough (alert-only free tools exist); (b) is "social" source-binding definitional when products cover news/blogs/reviews; (c) how the engagement/publishing modules inside suites relate to the listening core; (d) whether the new "AI/GenAI visibility monitoring" wave is a variant or a new Type.

## Research Questions

1. What is the central managed object — the query/topic? What does defining one involve?
2. What sources are collected, and what bounds coverage (platform APIs, privacy, plan)?
3. What accumulates — is there a persistent corpus with historical depth?
4. What analysis is computed over the stream (volume, sentiment, SOV, themes, demographics, influencers)?
5. How do alerts work (conditions, thresholds, channels)?
6. How do insights leave the product (dashboards, reports, exports, APIs, live walls)?
7. Where does AI sit (assistants, summaries, plain-language research questions)?
8. Do products include engagement/publishing (acting on what was heard)? Is that core or module?
9. Where is the seam vs media monitoring, social media analytics, reputation management, CI, consumer research?
10. What is the minimal pole (free alert tools) and does it satisfy the Type?

## Representative Products

Selected for market representation + documentation completeness + different product philosophy + different customer tier:

| Product | Pole | Customer tier | Evidence tier reached |
|---|---|---|---|
| Brandwatch (Cision) | pure-play enterprise listening / "consumer intelligence" | enterprise | Tier 2 (root + Consumer Intelligence product page) |
| Talkwalker (now "Lumen by Talkwalker", Hootsuite) | pure-play listening + media monitoring + benchmarking | enterprise | Tier 2 (root + Social Listening product page) |
| Sprout Social | suite-embedded listening module (premium add-on to a social media management suite) | mid-market/enterprise | Tier 1 (help center category + article titles) + Tier 2 (listening feature page) |
| Mention (Agorapulse) | lightweight SMB monitor, self-labeled "social listening & media monitoring tool" | SMB | Tier 2 (root page, feature/use-case rich) |
| Meltwater | media-intelligence suite bridge (listening + media monitoring + influencer in one platform) | enterprise/agency | Tier 2 (social listening solution page + FAQ) |

The sample spans: pure-play vs suite-module vs SMB vs media-suite bridge; Western global vs regional-platform coverage (Meltwater documents CN/KR/JP platforms).

## Sources

Research date: **2026-09-07**. All fetches direct from official vendor surfaces.

- Brandwatch — https://www.brandwatch.com/ ; https://www.brandwatch.com/products/consumer-intelligence/ (both fetched; /products/listening/ is 404)
- Talkwalker — https://www.talkwalker.com/ ; https://www.talkwalker.com/products/social-listening (both fetched)
- Sprout Social — https://support.sproutsocial.com/hc/en-us (help center root); https://support.sproutsocial.com/hc/en-us/categories/115001209366-Social-Listening (category); https://support.sproutsocial.com/hc/en-us/search?query=social+listening (article-title list); https://sproutsocial.com/features/social-media-listening/ (feature page). Note: individual help articles not fetched (URLs not extractable from saved output); article titles used as structural evidence only.
- Mention — https://mention.com/en/ (fetched)
- Meltwater — https://www.meltwater.com/en/solutions/social-listening (fetched, incl. FAQ)

Unreachable / not attempted further (per network-restriction rule): help.brandwatch.com (not attempted after product pages sufficed); individual Sprout article bodies; Talkwalker help center; Meltwater help center. No third-party review sites used.

## Product Observations

### Brandwatch (Cision) — pure-play enterprise pole

Key observations (evidence layer A unless noted):

- Suite structure: Consumer Intelligence / Search Intelligence ("Search Intelligence and GenAI Monitoring") / Social Media Management / Influencer Marketing / Media Intelligence & Insights. Listening lives inside Consumer Intelligence.
- "Consumer Research forms the basis of Brandwatch's consumer intelligence solution, with add-on apps providing enhanced functionality for specific use cases." — the listening engine is the substrate; add-on apps specialize it.
- Collection: "Collect millions of posts, comments, and conversations that are relevant to you"; "Conversations from 100 million unique sites and billions of sources"; "Official firehose access to Twitter, and Tumblr"; "Only Brandwatch provides the most historical and real-time consumer data."
- Analysis: "Categorize conversations by feedback, complaints, opinions, and more"; "Machine learning classifiers automatically segment data to fit your needs"; "Image analysis uncovers the objects, scenes, actions, and logos in every image"; "Choose from 50+ live visualizations to analyze data"; "Flexible UI can be combined in thousands of ways to find any insight."
- AI: "Iris, your AI assistant, turns data into human-readable insights instantly"; "17+ years developing industry-leading AI combining large language models with proprietary technology."
- Delivery: "Set up automated AI-powered email alerts to key stakeholders"; "Share insights across your organization with alerts and live reports"; "Instantly share insights via Excel, PPT, PDF, or via the Brandwatch API"; Vizia — "Send live data to any screen across your organization"; "Measure how many people view, engage with, and rate your reports with Vizia."
- First-party blending: "Upload your own data to spot sentiment, key topics, and historical trends."
- Use cases marketed: Market Research, Brand Management, Crisis Management, Stakeholder Management, Social Media Management, Content Marketing, Influencer Marketing, Customer Care; industries from agencies to pharma; roles incl. Market Researchers.
- Positioning language: "Social Listening & Consumer Insights"; "Understand and be understood across all key platforms."

### Talkwalker (Lumen by Talkwalker, part of Hootsuite) — pure-play listening + media monitoring + benchmarking

Key observations (A):

- Self-positioning (page title): "Social Listening and Media Monitoring Tool". Rebrand note: "Talkwalker is now Lumen by Talkwalker… bring Hootsuite and Talkwalker closer together. Same data, same reports, same workflows and integrations."
- Three product pillars: Social listening / Media monitoring / Social benchmarking — the listening/monitoring split is explicit in one vendor's own packaging (boundary evidence for the media-monitoring seam).
- Coverage: "30 social networks" (Instagram, Facebook, X, Pinterest…); "150+ million websites" (news sites, forums, newsletters, blogs) "across 239 countries and regions"; "100 customer feedback sources" (reviews, surveys, support interactions).
- Visual/audio listening: "Discover brand mentions — including references to your logo — in videos, images, podcasts, and more with Talkwalker's visual social listening."
- Analysis surfaces: sentiment analysis; conversation clusters ("visual map of conversations that are connected to each other"); virality maps; hashtag tracking; customizable dashboards "tailored to each team"; AI summaries ("daily, weekly, or monthly").
- Alerts: "real-time, custom alerts" — "Find out when a crisis might be forming, when sentiment is changing, and when to jump on a topic."
- AI: "Wisdom, our AI assistant" — "instant, plain language answer to a quick question about your audience."
- Use-case teams: PR & comms ("Protect your brand. Manage your reputation and mitigate crises"), social marketing, consumer insights ("Find the unmet needs… build an innovation engine"), agencies.
- Customer evidence: Bayes Business School (flag misinformation "before it became a media story"); Orange (listening across 1,300 employees in 28 countries, embedded in marketing/operations/CX/strategy); Yves Rocher (emerging consumer trends → product development).
- Free pole: "Talkwalker Alerts is one of the best free alternatives to Google Alerts… monitor their brand name, competitors, and other topics online. More than 600,000 people use TalkWalker Alerts." — direct evidence that the alert-only minimal pole exists as a free tool adjacent to the platform.

### Sprout Social — suite-embedded premium module

Key observations (A for structure; article titles as structural evidence):

- Positioning in suite: Listening is a "Premium solution" beside Premium Analytics and Employee Advocacy; core features are Engagement/Publishing/Analytics; additional products: Influencer Marketing, NewsWhip. FAQ exists on whether Listening is included in all plans + an article on checking plan inclusion — listening is plan-gated.
- Help center category "Social Listening" with sections: Listening Basics / Additional Listening Features / Listening Strategies. Category description: "Start uncovering trends and insights from social conversations to inform your strategy."
- Article titles (object-model evidence): "Social Listening FAQs"; "Social Listening Query Builder"; "Social Listening data availability and limitations"; "What types of insights can I get from Social Listening?"; "Using Smart Categories in Social Listening"; "How to Build Your First Social Listening Topic"; "How do I use the Conversation Breakdown widget in Social Listening?"; "How to Create Themes in Sprout Social Listening"; "How to Use Trellis in Sprout Social Listening: Sprout's AI Agent."
- Feature page: "Build sophisticated listening queries easily… without prior boolean knowledge or experience needed"; "adjust filters instantly—without needing to change your query"; "Automatically sift through billions of data points to zero in on trends, insights and key learnings"; "Leverage Trellis, your AI teammate, to ask complex research questions in plain language and get specific, contextual answers… without running a single report."
- Named capability areas: Consumer Research (audience demographics: age, gender, geographic location, device usage); Brand Health (sentiment + trends around brand, products, leadership); Competitor Comparison (share of voice, consumer attitudes toward competitors); Sentiment Research; Campaign Analysis (audience reactions to campaigns); Industry Analysis (trends); Influencer Recognition (identify influencers/thought leaders); Customer Feedback (conversations illuminating consumer attitudes/CX).
- Scale claim (vendor-commissioned study): "processes up to 50k posts per second and an average volume of 600 million messages a day" (Forrester TEI 2023). Recorded as vendor claim, not asserted as fact.
- FAQ topics listed: plan inclusion; business impact beyond social; competitor tracking; "How far back does Sprout's social media listening data go?"; "How is share of voice (SOV) calculated?"

### Mention (Agorapulse) — SMB lightweight pole

Key observations (A):

- Self-positioning (page title): "Social listening & Media Monitoring tool". Banner: "Agorapulse has acquired Mention."
- Three feature pillars: **Monitor** ("Track any topic on social media and the web"; "1 billion sources"; "Real time monitoring"; "Data up to 2 years"), **Analyze** ("Ready-to-use templates"; "Sentiment analysis"; "Share of voice"), **Engage** ("Interact with your community on social media"; AI tools).
- Query/alert mechanics: "Easy and intuitive query building"; "Keyword-based and page-based monitoring alerts"; "Valuable indicators like influence and sentiment."
- Analysis: "insightful, auto-updating reports and dashboards in just a few clicks"; "Comprehensive analytics such as reach, volume, sentiment, location, source, emotion and more"; "Over 10 templates based on your use case or fully customizable"; "Instant visualizations of your tracked topics with charts, maps, and key numbers."
- Engage module: "Curate, create, and schedule impactful social media content. Respond instantly to customers with all your social inboxes combined in one place"; approval workflow, content library.
- Use cases: brand management, PR management, competitive analysis, crisis management, market research, social media management.
- Footer platform pages: Social Listening, Social Publishing, Media Monitoring, Social Media Listening, Social Media Management, Competitive Analysis, Web Monitoring — one vendor selling under all the neighboring labels; the product is one engine with multiple marketing names.

### Meltwater — media-intelligence suite bridge

Key observations (A):

- Self-positioning (page title): "Social Media Monitoring & Social Listening". "Meltwater brings everything together in one platform—combining social listening, media intelligence, and influencer capabilities into a single solution."
- Definition offered: "Social media monitoring is the real-time tracking of brand mentions, keywords, and conversations across social platforms, so you can act before a moment passes."
- Coverage: "20+ networks, including X, Meta, TikTok, YouTube, LinkedIn, Reddit, Bluesky, and Threads, across 200+ countries and 240+ languages"; regional platforms listed: WeChat, Weibo, RED (Xiaohongshu), Douyin, Toutiao, QQ, Bilibili, Youku, Naver, Kakao Talk, LINE. "Full Reddit firehose access."
- Alerts: "real-time alerts… the moment something changes—whether it's a spike in mentions, a surge in negative sentiment, or a trending topic"; "Custom thresholds let you define what matters most"; delivery "via email, Slack, or other channels"; "alerts that reach you within minutes."
- Analysis: "AI-powered sentiment analysis and trend detection"; "Competitor tracking and share of voice analysis"; "Automated dashboards and reporting"; "Historical data analysis for trend comparisons"; automated summaries; AI-powered search.
- Integration: "API access, flexible data exports, and integrations with common business tools."
- FAQ (direct evidence for data-availability rules): "Due to privacy restrictions, monitoring on Meta platforms is limited to publicly available data"; LinkedIn monitoring "focusing on publicly available content"; alerts "near real time"; "Meltwater provides access to extensive historical data"; "Why not just use native platform analytics? Native tools only show activity within individual platforms and often miss untagged or cross-channel conversations."
- Platform family: Media Intelligence / Social Listening / AI Visibility Tracking / Media Relations / Influencer Marketing; features incl. Media Monitoring, GenAI Lens, Social Media Monitoring, Influencer Management, Consumer Insights, Media Database, Press Distribution, PR Reporting, Social Media Analytics.

## Cross-product Comparison

| Dimension | Brandwatch | Talkwalker/Lumen | Sprout Social | Mention | Meltwater | Layer |
|---|---|---|---|---|---|---|
| Standing queries/topics as central object | yes (queries implied; flexible UI over collected data) | yes (topic monitoring) | yes — "Topic", "Query Builder" named | yes — "query building" named | yes (keyword/conversation tracking) | **L0** |
| Public third-party conversation sources | yes — 100M sites, billions of sources; firehose | yes — 30 networks + 150M websites + feedback sources | yes — "social conversations" | yes — 1B sources, web + social | yes — 20+ networks + regional + Reddit firehose | **L0** |
| Continuous collection into accumulating corpus | yes — "most historical and real-time" | yes — real-time + historical | yes — data-availability article; "how far back" FAQ | yes — "data up to 2 years" | yes — "extensive historical data" | **L0** |
| Aggregated analysis (volume/trends at minimum) | yes — visualizations, classifiers | yes — dashboards, clusters, virality | yes — insights, widgets | yes — reports/dashboards, charts | yes — dashboards, trend detection | **L0** |
| Sentiment analysis | yes | yes | yes (Brand Health, Sentiment Research) | yes | yes | L1 |
| Share of voice / competitor comparison | yes (implied via benchmarking use cases) | yes (Social benchmarking pillar) | yes (Competitor Comparison, SOV FAQ) | yes (SOV named) | yes (SOV named) | L1 |
| Theme/topic discovery | yes (classifiers, categorization) | yes (conversation clusters, virality maps) | yes (Themes, Smart Categories, Conversation Breakdown) | yes (templates, visualizations) | yes (trend detection) | L1 |
| Alerts on conditions | yes (automated email alerts) | yes (real-time custom alerts) | not directly observed at fetched level | yes (keyword/page-based alerts) | yes (custom thresholds, email/Slack) | L1 |
| Dashboards / reports / exports | yes (50+ visualizations, Excel/PPT/PDF, API, Vizia walls) | yes (custom dashboards, AI summaries) | yes (widgets; reports in suite) | yes (auto-updating reports, 10+ templates) | yes (automated dashboards, scheduled reports) | L1 |
| Audience demographics | yes (custom audiences overlay) | yes (implied via consumer insights) | yes (Consumer Research: age/gender/geo/device) | yes (location analytics) | not directly observed | L1 |
| Influencer/author identification | yes (Influencer Marketing suite sibling) | yes (key influencer monitoring) | yes (Influencer Recognition) | yes (influence indicator) | yes (Influencer Management sibling) | L1 |
| AI assistant / plain-language answers | yes (Iris) | yes (Wisdom) | yes (Trellis) | yes (AI tools) | yes (AI summaries, AI search) | L1 (current-gen) |
| Engagement/publishing module | yes (SMM suite sibling) | no (Hootsuite is the sibling) | yes (suite core) | yes (Engage pillar) | yes (publishing via suite) | L2 |
| News/media coverage sources | yes (Media Intelligence sibling; Cision) | yes (Media monitoring pillar) | not observed | yes (self-labeled media monitoring; web monitoring) | yes (media intelligence family) | L2 |
| Review/feedback sources | not directly observed | yes (100 customer feedback sources) | yes (Customer Feedback area) | not observed | not observed | L2 |
| Visual/audio listening (logo/image/video) | yes (image analysis, logos) | yes (visual listening) | not observed | not observed | not observed | L2 |
| Regional platform coverage (CN/KR/JP) | not observed | not observed | not observed | not observed | yes (WeChat/Weibo/RED/Douyin/Naver/Kakao/LINE…) | L2 |
| Search/GenAI visibility monitoring | yes (Search Intelligence + GenAI Monitoring) | not observed | not observed | not observed | yes (AI Visibility Tracking, GenAI Lens) | L2 |
| First-party data upload | yes ("upload your own data") | not observed | not observed | not observed | not observed | L2 |
| Free alert-only pole | no | yes (Talkwalker Alerts) | no | free trial only | no | L2 (boundary pole) |
| Historical depth stated | "most historical" (unquantified) | not quantified at fetched level | FAQ exists (answer not fetched) | "up to 2 years" | "extensive" (unquantified) | L3 (per-product) |

Stable commonalities across all five (layer B): the define → collect → analyze → deliver loop; standing queries/topics as the central object; public third-party conversation as the substrate; an accumulating corpus; aggregated metrics; sentiment; competitor/SOV; alerts; dashboards/reports; AI assistance (current generation).

## Canonical Abstraction

### L0 — Defining Invariant

Three structures held jointly, plus the observational purpose:

1. **Standing topic/query definitions** — persistent, user-maintained watch expressions (keywords, phrases, exclusions, source/language/country scoping) over public online conversation. Not one-off searches; the query outlives any single session and defines everything downstream. Remove → a search engine (query-time retrieval, no standing watch).
2. **Continuous collection of matching public third-party conversation into an accumulating corpus** — the platform ingests publicly posted content (posts, comments, mentions, articles) as it is published and retains it as a queryable, time-stamped record. Social networks are the signature source class; forums, reviews, blogs, news extend it. The substrate is third-party and public — not the organization's own connected accounts, not private/solicited data. Remove the third-party substrate (keep only own connected accounts) → social media analytics; remove "public" (asked people directly) → survey/consumer research; remove the accumulating corpus (notify only) → an alert service.
3. **Aggregated analysis of the collected conversation** — the stream is computed into measures (at minimum volume over time; typically sentiment, themes, share of voice, sources, authors) whose deliverable is understanding about monitored subjects. Remove → a raw feed reader or archive with no insight layer.

Purpose clause: the organization operates these structures to understand what the public is saying — about its brand, its competitors, its category, its topics — and to inform marketing, communications, product, and risk decisions.

Jointly-held is load-bearing: 1+2 without 3 = alert/archive service; 1+3 without 2 = search/analytics over someone else's corpus; 2+3 without 1 = generic social-data mining without the user-defined watch.

### L1 — Common Mature Structure

Present in essentially all mature products; not required to recognize the Type:

- sentiment analysis (machine-inferred at scale)
- share of voice / competitor benchmarking
- theme/topic discovery (clusters, categories, word clouds)
- condition-based alerts (spikes, sentiment shifts) with delivery channels
- dashboards, scheduled/automated reports, exports (slides/CSV/PDF), APIs
- audience demographics (age/gender/geo/device where source permits)
- influencer/author identification
- historical archives with per-source depth
- AI assistants / plain-language research answers / automated summaries (current generation)

### L2 — Variant / Optional Structure

- engagement/publishing modules (act on what was heard — suite-embedded pole)
- news/editorial coverage sources (media-inclusive suites)
- review/customer-feedback sources (reputation-adjacent intake)
- visual/audio listening (logo detection in images/video, podcast/audio)
- regional platform coverage (Chinese/Korean/Japanese networks)
- search-engine and GenAI-answer visibility monitoring (new-generation surface)
- first-party data upload/blending
- free alert-only tools (the minimal pole — Google Alerts / Talkwalker Alerts class)
- agency/multi-client packaging; firehose vs API data access posture

### L3 — Vendor-specific (kept out of the final document)

- Brandwatch: Iris AI; Vizia live-data walls with report-viewership measurement; Consumer Research + add-on apps architecture; official Twitter/Tumblr firehose; "17+ years" AI claim; Cision ownership.
- Talkwalker/Lumen: Wisdom AI; virality maps; conversation clusters; the Lumen rename and Hootsuite pairing; Talkwalker Alerts free tool; 30 networks / 150M websites / 239 countries / 100 feedback sources figures.
- Sprout Social: Trellis AI agent; Smart Categories; Themes; Conversation Breakdown widget; premium-plan gating; "50k posts/second, 600M messages/day" commissioned-study claim; boolean-free query builder positioning.
- Mention: Monitor/Analyze/Engage pillar naming; "1 billion sources"; "data up to 2 years"; influence indicator; Agorapulse acquisition.
- Meltwater: GenAI Lens; AI Visibility Tracking; Reddit full firehose; 240+ languages; 200+ countries; custom alert thresholds with Slack delivery; the monitoring-vs-listening definitional sentence in its FAQ.

## Vendor-specific Findings

- The listening/monitoring split is packaged differently per vendor: Talkwalker sells Social listening and Media monitoring as separate product pillars; Meltwater sells one "Social Media Monitoring & Social Listening" surface inside a media-intelligence suite; Mention self-labels as both in its page title; Brandwatch separates Consumer Intelligence (listening) from Media Intelligence (via Cision). This is packaging variance over one shared engine family — recorded as boundary evidence, not Type evidence.
- Sprout's "adjust filters instantly without needing to change your query" documents a two-layer model inside the product: the query defines the collected corpus; filters/views re-slice it without re-collection. Structural observation, single-product phrasing — kept qualified.
- Mention's "keyword-based and page-based monitoring alerts" documents two alert triggers (terms vs specific pages/profiles). Single-product detail.
- Meltwater's FAQ is the only fetched source that states the privacy boundary explicitly ("Meta platforms… limited to publicly available data"). Generalized cautiously as a source-governed coverage rule (layer B inference from one explicit statement + Sprout's "data availability and limitations" article title).

## Boundary Findings

1. **vs Social Media Analytics Platform (§06 sibling, unprocessed) — sharpest open seam.** Analytics measures the organization's own connected accounts (performance of its own posts/channels); listening observes the public conversation at large via standing queries (mostly untagged, cross-channel, not the org's own posts). Meltwater's own FAQ articulates the seam from the listening side: native platform analytics "only show activity within individual platforms and often miss untagged or cross-channel conversations." Removal tests: restrict the substrate to connected own accounts → analytics; restrict to query-defined public conversation → listening. Products straddle deliberately (suites ship both). Consistent with the influencer-marketing pass's actor/object holding (own content vs aggregate measurement vs monitoring). **Joint review recommended when social-media-analytics-platform is processed.**
2. **vs Media Monitoring Platform (§06 sibling, unprocessed) — second sharpest seam.** Center-of-gravity discriminator: public conversation (social-first, consumer-authored) vs editorial coverage (news/broadcast/print-first, journalist-authored). Every sampled suite spans both (Talkwalker pillars; Meltwater family; Brandwatch+Cision; Mention's self-label), so the seam is center of gravity, not exclusive source sets. Removal tests: restrict sources to editorial media + coverage metrics → media monitoring; restrict to social/consumer conversation → social listening. **Joint review recommended when media-monitoring-platform is processed.**
3. **vs Brand Reputation Management (§06, processed) — DISCHARGES that pass's joint-review flag from the listening side.** The structural test holds: reputation management captures external feedback signals as individual records and acts per signal (public response, solicitation, routing) while tracking entity reputation state; listening aggregates conversation for insight without per-signal organizational action. Remove per-signal action from reputation → a listening platform remains; add per-signal response workflows to listening → it drifts into reputation territory. Listening products' engagement modules (Mention Engage, Sprout's suite inbox) are adjacent capability, not the listening core. Keep both Types.
4. **vs Competitive Intelligence Platform (§06, processed)** — consistent with that pass's boundary row: listening is source-bound (public online conversation) and topic/consumer-conversation-centric; CI is entity-bound and source-agnostic (competitors' moves across any source). Restrict sources to social + own-brand/consumer topics → listening. No new flag; seam confirmed from this side.
5. **vs Consumer Research Platform (§06, processed)** — consistent with that pass's "asked vs observed" seam: consumer research fields structured studies to sampled humans; listening observes unsolicited public behavior. Listening data can feed consumer research (Talkwalker's consumer-insights positioning; Brandwatch's Consumer Intelligence naming) — the observation substrate serving a research purpose is a variant emphasis, not a Type merger.
6. **vs Voice of Customer Platform (§06 sibling, unprocessed)** — proposed seam for that pass: VoC manages solicited, private, structured customer feedback (surveys, feedback requests) often tied to the customer relationship; listening observes unsolicited public conversation. Talkwalker's "customer feedback sources" (reviews/surveys/support interactions as listening inputs) is intake variance, not VoC conversion. Flag recorded for that pass.
7. **vs Search Engine / Answer Engine (§02.02/§02.03)** — one-off query-time retrieval vs standing collection + aggregation. The new "GenAI/AI visibility monitoring" wave (Brandwatch Search Intelligence; Meltwater AI Visibility Tracking) extends the standing-watch grammar to AI-generated answers — classified as an L2 surface extension of this Type, watch for drift when answer-engine-adjacent leaves are processed.
8. **vs Feed Reader / Content Aggregator (§02.08)** — the listening platform's unit is the query/topic over a source-agnostic public corpus, aggregated into metrics; the feed reader's unit is the user-curated source list triaged chronologically. A listening product can subscribe to specific pages (Mention's page-based alerts) without becoming a feed reader — aggregation into insight is the discriminator.
9. **Alert-only minimal pole** — free tools (Google Alerts class; Talkwalker Alerts directly documented) satisfy query + notification but lack the retained corpus + analysis layer. Classified as the Type's minimal adjacent pole (a service, not a platform); the "platform" leaf implies the analysis layer. Removal test: remove analysis → alert service, not a listening platform.

## Historical / Market-Sample Check

- The defining core (standing queries → collected public conversation → aggregated analysis) predates the current AI-heavy generation: the sampled products' own framing ("17+ years developing AI" at Brandwatch; Talkwalker Alerts as a "free alternative to Google Alerts" — Google Alerts dating to the early 2000s as market context) shows the watch-grammar long predates LLM-era features. The mid-2000s "buzz monitoring / brand monitoring" generation (market-context names only; not fetched, no claims asserted) already centered keyword queries over social sources with dashboards — the L0 triple is era-robust.
- Regional check: Meltwater documents Chinese/Korean/Japanese platform coverage (WeChat, Weibo, RED, Douyin, Naver, Kakao Talk, LINE) — regional platform sets are variant coverage, not a different Type.
- Minimal-pole check: alert-only free tools fail the analysis leg and are held as the adjacent minimal pole, not the Type.
- AI-era check: AI assistants/summaries are treated as current-generation common structure (L1), not definitional — the Type is fully recognizable without them.

## Uncertainties

1. Help-center article bodies were not fetched for any product (Sprout article URLs not extractable; Brandwatch/Talkwalker/Meltwater help centers not reached). Operational specifics — query syntax capabilities, exact widget catalogs, plan gating details, per-source retention windows — are therefore NOT asserted anywhere; only Mention's "data up to 2 years" is a directly documented window (product-specific).
2. Whether the market is renaming the Type ("consumer intelligence" at Brandwatch; "media intelligence" at Meltwater; "Lumen" at Talkwalker) — recorded as naming/packaging drift; the working grammar (listening/monitoring) remains the market's operative vocabulary.
3. Sprout's "50k posts/second / 600M messages/day" is a vendor-commissioned-study claim — carried as claim only.
4. The media-monitoring and social-media-analytics siblings are unprocessed; both seams are held from this side only and flagged for joint review.
5. Whether engagement-equipped listening products (Mention Engage) should eventually be classed with Social Media Management — held as module-vs-Type question for the SMM pass; no directory change made.

## Final Synthesis

A Social Listening Platform is the organization's standing instrument for observing public online conversation at scale. Its world is built around three jointly-held structures: user-defined standing queries/topics that express what to listen to; continuous collection of the matching public third-party conversation (social networks foremost, extended by forums, reviews, blogs, and news) into an accumulating, time-stamped corpus the platform owns as its record; and aggregated analysis that computes the corpus into insight — volume and trends at minimum, with sentiment, share of voice, themes, demographics, and influential authors as the mature standard layer. Around this core, mature products add alerts on defined conditions, dashboards/reports/exports/APIs for delivery, AI assistants that answer research questions in plain language, and — depending on packaging — engagement modules, media-coverage sources, visual/audio listening, regional platforms, and GenAI-visibility monitoring. The Type's sharpest boundaries: vs social media analytics (own connected accounts vs public conversation), vs media monitoring (conversation-centric vs coverage-centric), vs brand reputation management (insight loop vs per-signal action loop), vs competitive intelligence (source-bound consumer conversation vs entity-bound source-agnostic), and vs consumer research/VoC (observed vs asked). The definition survives the historical check: the watch-grammar predates the AI generation, regional platform coverage is variant, and the alert-only free tool is the minimal adjacent pole rather than the Type itself.
