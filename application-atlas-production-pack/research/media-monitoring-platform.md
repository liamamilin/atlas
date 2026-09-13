# Research Notes — Media Monitoring Platform

## Research Goal

Understand what a "Media Monitoring Platform" actually is as an Application Type, from real products: what objects exist inside it (watch definitions/saved searches, collected media items, coverage metrics, alerts, reports), what its defining workflow is (define → collect → measure → deliver), who operates it, and where its boundary runs against the neighboring §06 Types (Social Listening, Brand Reputation Management, Competitive Intelligence, Public Relations Management, Media Relations, Social Media Analytics) and against consumer news products (§02.04) and security-side monitoring (§15).

This pass also carries three joint-review flags left by processed siblings:

1. **social-listening-platform** (2026-09-07): "sharpest open seam — center-of-gravity discriminator (public consumer-authored conversation, social-first vs editorial journalist-authored coverage, news-first)… joint review recommended when media-monitoring-platform is processed."
2. **brand-reputation-management** (2026-09-06): "the corporate reputation-intelligence pole (Signal AI-style media/narrative sensing, benchmarking, reporting for comms/risk teams)… has no review loop and belongs with Media Monitoring/Social Listening."
3. **competitive-intelligence-platform** (2026-09-07) and **public-relations-management-platform** (2026-09-06): boundary rows naming media monitoring as the own-brand / no-outreach counterpart — to be confirmed from this side.

## Initial Boundary

Working hypothesis before research:

- A media monitoring platform continuously watches published media (news, broadcast, print — commonly extended with social and web sources) for mentions of the organization's own brand, competitors, spokespeople, and industry topics, and turns the collected coverage into item records, alerts, dashboards, and reports for communications/PR/risk use.
- Likely confusions:
  1. Social Listening Platform — same monitoring grammar; the held seam is center of gravity (conversation vs coverage).
  2. Brand Reputation Management — the "reputation" word; the corporate media-narrative pole calls itself reputation management but has no review loop.
  3. Competitive Intelligence Platform — same collect→curate→distribute skeleton; own brand vs external entities.
  4. Public Relations Management Platform — PR suites bundle monitoring; monitoring without contacts/outreach is the slice.
  5. News Aggregator / News Application — both "read the news"; organizational subject + measurement vs consumer reading.
  6. Digital Risk Protection / adverse-media screening — security-side monitoring with enforcement; media monitoring is observational.
- Unknowns going in: (a) is social listening part of the core or a suite module? (b) are broadcast/print monitoring definitional or variant? (c) is the measurement/reporting layer definitional or common? (d) does the AI-first reputation-intelligence pole (Signal AI) fit inside this Type as a variant? (e) what is the minimal pole (Google Alerts class)?

## Research Questions

1. What is the central managed object — the watch definition (saved search / mention stream / topic)? What does defining one involve?
2. What sources are monitored, and what is the signature source class vs common extensions?
3. What accumulates — is there a persistent item-level record with historical depth?
4. What measurement is computed over the collected coverage (volume, sentiment, share of voice, reach, message pull-through)?
5. How do alerts work and how do insights leave the product (dashboards, reports, newsletters, exports, APIs)?
6. Where does AI sit (summaries, assistants, harmful-content detection, LLM-visibility monitoring)?
7. Do products include outreach/engagement (acting on coverage)? Is that core or module?
8. Where is the seam vs social listening, brand reputation management, CI, PR management, media relations, news apps?
9. What is the minimal pole (free alert tools) and does it satisfy the Type?
10. Does the historical clip-service era satisfy the same structure (historical check)?

## Representative Products

Selected for market representation + documentation completeness + different product philosophy + different customer tier:

| Product | Pole | Customer tier | Evidence tier reached |
|---|---|---|---|
| Meltwater | media-intelligence suite, news-first heritage; sells Media Monitoring and Social Listening as separate capabilities | enterprise | Tier 2 (root + Media Monitoring product page, incl. FAQ) |
| Cision (CisionOne) | PR incumbent suite with Media Monitoring as the flagship module | enterprise/agency | Tier 2 (CisionOne overview + Media Monitoring + Instant Insights & Reporting pages) |
| Factiva (Dow Jones) | content-archive-first: licensed premium news archive + watch/alerts; no social suite | enterprise | Tier 2 (Factiva product page) |
| Signal AI | AI-first corporate reputation/risk intelligence (the pole flagged by the brand-reputation pass) | enterprise | Tier 2 (root + Reputation Intelligence Platform page) |
| Mention (Agorapulse) | lightweight SMB monitor; one engine sold under many neighboring labels | SMB | Tier 2 (Media Monitoring page; root-page structure from the listening pass) |

The sample spans: suite (Meltwater) vs PR-incumbent (Cision) vs archive-first (Factiva) vs AI-first reputation intelligence (Signal AI) vs SMB lightweight (Mention); news-only (Factiva) vs full multi-source (Meltwater/Cision); enterprise vs SMB.

## Sources

Research date: **2026-09-08**. All fetches direct from official vendor surfaces.

- Meltwater — https://www.meltwater.com/en (root); https://www.meltwater.com/en/products/media-monitoring (product page incl. FAQ). Note: /en/solutions/media-intelligence and /en/solutions/media-monitoring returned 404; correct paths found via root navigation.
- Cision — https://www.cision.com/cisionone/ ; https://www.cision.com/media-monitoring/ ; https://www.cision.com/instant-insights-and-reporting/
- Dow Jones — https://www.dowjones.com/products/factiva/ (redirects to /business-intelligence/factiva/products/factiva/)
- Signal AI — https://signal-ai.com/ ; https://signal-ai.com/solutions/webapp/
- Mention — https://mention.com/en/media-monitoring/
- Cross-reference (prior pass, same research program): research/social-listening-platform.md (Talkwalker/Meltwater/Brandwatch/Mention/Sprout observations, 2026-09-07).

Unreachable / not attempted further (per network-restriction rule): help.meltwater.com (prior listening pass could not reach help-center article bodies; not re-attempted), Cision help/knowledge base (JS-gated in prior passes), Factiva in-product help, Signal AI app (login-gated), Mention help center article bodies. No third-party review sites used. All evidence below is Tier-2 official product-page level unless marked otherwise.

## Product Observations

### Meltwater — media-intelligence suite, news-first heritage

Key observations (evidence layer A unless noted):

- Definition offered on the product page: "Media monitoring is how brands track, analyze, and measure what's being said about them across news, social, print, broadcast, and podcasts." — the vendor's own four-verb grammar (track, analyze, measure) over multi-source coverage.
- Stated workflow (named steps on the page): **Collect** ("Capture mentions across millions of sources worldwide in real time") → **Analyze** ("Apply AI to identify sentiment, trends, key themes, and anomalies") → **Surface insights** ("Deliver relevant insights through dashboards, alerts, and AI-generated summaries") → **Enable action** ("Empower your team to respond quickly, refine messaging, and prove impact").
- Source classes monitored (page section "What we monitor"): social media (global platforms + APAC: WeChat, Weibo, RED, Douyin, Toutiao, QQ, Bilibili, Youku, Naver, Kakao Talk, LINE); online news ("over 200 million online publications, including blogs, review sites, and forums"); print ("over 400,000 traditional media sources, including newspapers and magazines"); broadcast ("comprehensive TV and radio monitoring, covering all 210 US DMAs and thousands of television and radio stations globally"); podcasts ("over 20,000 podcasts"); LLMs/AI ("ChatGPT, Perplexity, Google AI Overviews, Google AI mode, Deepseek, Llama, Claude, Gemini, Grok").
- Metrics enumerated ("track everything you need"): volume of mentions over a time period; share of voice per platform; potential reach/impressions of coverage; sentiment analysis; trends analysis ("most common topics associated with your brand"); top publications; top location; top influencers and journalists.
- Key features: real-time monitoring and alerts ("instant notifications on key mentions, spikes, and breaking stories"); AI-powered insights ("sentiment, emotion, and narrative shifts"); custom dashboards and reporting; comparative analysis and benchmarking ("across campaigns, competitors, regions, and time periods"); global coverage and multilingual support; integrated AI assistant (Mira) for summaries/reports/insights via conversation.
- Earned-media framing: "The complete earned media monitoring solution… Track coverage across channels, measure sentiment and reach, and understand how your brand is positioned against competitors."
- Historical-baseline evidence: "More than just clip tracking — Unlike traditional media monitoring tools, Meltwater combines AI, media tracking, analysis, and reporting in a single platform. Media monitoring is no longer about collecting links." FAQ repeats: "Unlike traditional tools that focus on clip collection…" — the vendor itself names clip collection as the traditional baseline of this Type.
- FAQ: "Meltwater provides metrics like sentiment, reach, share of voice, and message pull-through, helping you connect PR efforts to business outcomes." — message pull-through named as a metric.
- FAQ: "Does Media Monitoring include social media conversations? Yes. Meltwater includes social media monitoring…" — social explicitly inside the media-monitoring product.
- FAQ: LLM coverage via "AI Visibility Tracking / GenAI Lens… captures LLM responses… aggregates outputs across models for a multi-model view, and enriches results with emotion, keywords, link analysis and trend history."
- Root page: "Built for PR, Communications, and Marketing leaders"; scale claims "1.3+ Billion Documents Ingested Daily, 1M Alerts Delivered Daily, 240+ Languages Supported" (vendor claims, layer A-as-claim); capability family: Media Intelligence / Social Listening / AI Visibility Tracking / Media Relations / Influencer Marketing — monitoring and listening are separate named capabilities of one platform.
- Customer quote (NASCAR): "eight-figure advertising value" — coverage-value vocabulary in the market (customer claim, not product rule).

### Cision (CisionOne) — PR incumbent, monitoring as flagship module

Key observations (A):

- Positioning: "The all-new AI platform for real-time media intelligence"; module family: Media Monitoring / Instant Insights & Reporting / Journalist Outreach / Social Listening & Management / Professional Services / CisionOne AI / AI Visibility — monitoring, listening, and outreach are separately named modules of one platform.
- Media Monitoring module: "access to the most comprehensive collection of traditional, digital, and premium sources… Gain unlimited insight using Mention Streams, AI coverage tracking, smart alerting, and iOS & Android apps to monitor brand, competitor, industry, and stakeholder coverage in real time."
- Watch object named: "Real-time mention streams — Instantly add Mention Streams to track your brand, competitor, spokespeople, industry mentions, and much more. Compare your Mention Streams side by side and watch the news roll in as it happens." — the standing watch is a first-class, comparable object.
- Source breadth: "hundreds of thousands of news sources, top social platforms, leading global print publications, 3000+ TV and radio stations, 60,000+ podcasts, and over 10,000 premium paywalled titles"; "190+ countries and 96 languages, accessing full-text content from top sources"; "Surface real-time online content, stream and share TV and radio, and view print, podcast, magazine and social content through CisionOne's live Mention Streams."
- AI metrics: "Cision's proprietary, AI-powered React Score instantly detects potentially harmful content… understand the context behind your coverage so you can take the appropriate action"; reporting page adds: "Whether it's hate speech, fake news, controversial remarks, sarcasm, or spam."
- Alerts/delivery: "Get realtime alerts through the CisionOne mobile app for iOS and Android, integrate with Slack or Teams, and receive reports directly in your inbox."
- Measurement layer (Instant Insights & Reporting): "Unify traditional and social media in a single dashboard, then turn insights into interactive, executive-ready reports"; "In just three simple steps, build a custom dashboard… Select from dozens of metrics"; "Measure the reach of your coverage, monitor the effectiveness of your key messages, track sentiment, benchmark share of voice, and connect earned media results to business outcomes"; "Track the competition & industry trends"; "Effortless reporting… brand the report with your logos and style guide."
- Use cases: PR Corporate & Communications, Brand Reputations & Crisis Management, Public Sector Communications, Campaign and Event Reporting, Social Media Listening, Investor and Analyst Relations, Regulatory Compliance.
- Customer quotes: crisis-communications firm ("monitor breaking news… able to respond quickly to complex stories"); asset manager ("deliver timely insights to senior leadership and stay on top of real-time mentions").
- Journalist Outreach module ("500k+ validated journalists") is a separate module — the media-relations slice lives beside monitoring, not inside it.

### Factiva (Dow Jones) — content-archive-first pole

Key observations (A):

- Positioning: "Factiva brings together powerful research tools, millions of company profiles, and access to thousands of premium sources in 33 languages across 200 countries — all in one platform." "Premium News & Data: …access to trusted news, global insights and comprehensive corporate and executive profiles."
- Watch grammar present: "Track interests globally — Follow the topics, industries, and companies that matter most. Your personalized news stream keeps you informed with relevant, real-time updates." + "real-time alerts" on mobile.
- AI layer: "Factiva's AI Assistant is grounded in trusted, licensed content, and every response includes direct source links for total confidence." — licensed-content grounding as the differentiator.
- Company intelligence: "Company Insights reports delivering comprehensive analysis on public and private companies covering financials, up-to-the moment news analysis, and risk factors, all with source links included for verification."
- Content: "global news coverage from 200+ countries in 33 languages—spanning top national outlets, regional sources, video, and podcasts—with source links for deeper exploration and analysis."
- Use cases: Business Development, Competitive Intelligence, **Corporate Communications & Reputational Risk Management**, Research.
- Product family: Factiva AI Research Solutions, Factiva Curated Newsletters, Factiva Feeds & APIs, Factiva Sentiment Signals (sold under Dow Jones Risk).
- No social listening suite, no outreach module — the archive-first pole proves social sources and outreach are not definitional. News/editorial coverage is the entire substrate here.

### Signal AI — AI-first corporate reputation/risk intelligence pole

Key observations (A):

- Positioning: "Signal AI transforms external data from traditional and social media across 226 markets and 120+ languages, providing companies with actionable insights designed to navigate enterprise risk, strengthen reputation, and fuel growth." Page title: "AI-Powered Reputation Management & Risk Intelligence" — the pole that calls itself reputation management (flag from the brand-reputation pass).
- Expertise areas: Enterprise Risk / Reputation Risk / PR & Comms / ESG / Regulation — comms and risk teams as the audience.
- PR & Comms expertise items: "Traditional & Social Media Monitoring: Evaluate and optimize your media campaigns, backed by quantifiable metrics"; "Corporate Narrative Planning: Identify dominant narratives"; "Reputation Threat Sensing"; "Benchmarking & Measurement: Compare, assess, and align your reputation with top-tier industry players."
- Platform features (Reputation Intelligence Platform): **360° View** ("media coverage metrics like Share of Voice, sentiment analysis, readership data, and AI citations"); **Unlimited AI-Powered Search** ("Dive into insights from published media, podcasts, broadcasts, regulatory documents, LLM monitoring, and social media with no limits. Monitor competitors, campaigns, and spokespeople as extensively as you wish. Set up and edit as many searches as you need"); **Real-time alerts** ("Set up unlimited real-time alerts… Track evolving stories as they happen"); **Add Custom Content** ("tagging entities and topics, easily sorted by publish date, media type, source, and location. Your personalized inputs seamlessly integrate into saved searches and dashboards").
- Ask AIQ: "conversational AI agent transforming how reputation management teams identify and investigate threats… Drill down into specific events, understand underlying factors."
- Delivery surfaces: Insight Reports (Risk / Reputation Risk / Reputation / Media Impact / Deep Dive), Advanced Dashboards, Newsletters and Briefings (Risk Briefings, Alerts, Media Newsletters), API.
- Scale claims: "100M+ entities and topics labeled per day by AIQ; 5.5M+ articles ingested per day; 120+ languages translated" (vendor claims).
- Customer quotes: DEC CEO — "We considered a number of platforms for media monitoring, but Signal AI stood out… unlimited clippings during busy times without extra cost and the flexibility of controlling our media monitoring service from our desktops" (clipping vocabulary persists; customer classifies the product as media monitoring); Northumbria University — "organize coverage based on the areas and build this into our Dashboards… demonstrate ROI on our comms activities"; BCW — "'shrink the internet'… evaluate what's happening now and anticipate what's coming next"; agency topic-framework quote — "50,000 or 100,000 articles over a year… topic framework… see a peak in January related to cyber issues at the client."
- Signal AI 500: "harnesses AI to assess narratives of the top global companies" — reputation ranking as an adjacent data product.
- No review loop anywhere — confirms the brand-reputation pass's classification of this pole under media monitoring.

### Mention (Agorapulse) — SMB lightweight pole

Key observations (A; root-page structure cross-referenced from the listening pass):

- Page title: "Media Monitoring: Track Your Brand Online & On Social Media"; headline: "Track earned media with our Monitoring tools & measure the impact of your PR campaigns."
- "An online media monitoring tool that fits your needs — whether that's news media monitoring, social media monitoring or web monitoring as a whole." Goals: "Discover industry trends / Measure your campaign performance / Learn what people love or hate."
- Mechanism: "Mention crawls extensive sources across the web such as forums, blogs, news and review websites, as well as social media channels. This allows us to identify every instance when a keyword of your choosing is mentioned. Once the media tracking has been done, we aggregate the information in a comprehensive way, allowing you to see the key metrics - or review each mention to have a more detailed view." — item-level review AND aggregation both named.
- Vendor blog definition: "Media monitoring is the process of tracking, collecting and analyzing mentions of brands, topics or keywords on different platforms."
- Use cases: brand management, PR management, competitive analysis, crisis management, market research, social media management.
- From the listening pass (same vendor, 2026-09-07): Monitor/Analyze/Engage pillars; "keyword-based and page-based monitoring alerts"; sentiment, share of voice, reach, volume, location, source metrics; "1 billion sources"; "data up to 2 years"; footer sells the same engine under Social Listening / Social Publishing / Media Monitoring / Social Media Listening / Social Media Management / Competitive Analysis / Web Monitoring labels.

## Cross-product Comparison

| Dimension | Meltwater | Cision CisionOne | Factiva | Signal AI | Mention | Layer |
|---|---|---|---|---|---|---|
| Standing watch definitions as central object (saved searches / Mention Streams / topics / interests) | yes ("track… mentions", alerts on spikes) | yes — "Mention Streams… add… compare side by side" | yes — "Follow the topics, industries, and companies" | yes — "Set up and edit as many searches as you need" | yes — "a keyword of your choosing" | **L0** |
| Organization's own presence as primary monitored subject (brand/competitors/spokespeople/industry) | yes ("what's being said about them") | yes ("brand, competitor, spokespeople, industry") | yes (companies/industries; comms & reputational-risk use case) | yes ("your company, competitors, or industry"; spokespeople) | yes ("Track Your Brand") | **L0** |
| Continuous automated collection into accumulating record | yes ("continuously analyzes millions of sources"; historical data) | yes ("watch the news roll in as it happens") | yes ("personalized news stream… real-time updates") | yes ("5.5M+ articles ingested per day" claim; real-time alerts) | yes ("crawls… real time"; "data up to 2 years") | **L0** |
| Item-level mention/coverage records (review each item) | yes ("mentions that matter most"; clip-tracking baseline named) | yes (Mention Streams of items) | yes (articles with source links) | yes ("unlimited clippings"; "review each mention" analog via search) | yes ("review each mention to have a more detailed view") | **L0** |
| Editorial/news coverage as signature source class | yes (news/print/broadcast named first) | yes (news/print/TV/radio first) | yes (news only — the whole substrate) | yes ("traditional and social media"; published media, broadcasts) | yes (news among web sources) | **L0** (center of gravity) |
| Social/web sources as extensions | yes (explicit FAQ) | yes ("top social platforms") | no (not observed) | yes ("social media" in search scope) | yes | L1/L2 |
| Organizational measurement (volume/trends at minimum) | yes (volume, trends) | yes (dozens of metrics) | yes (news stream + company analysis) | yes (SOV, sentiment, readership) | yes (key metrics) | **L0** |
| Sentiment analysis | yes | yes (track sentiment) | via Sentiment Signals (sibling product) | yes | yes | L1 |
| Share of voice / competitor benchmarking | yes | yes ("benchmark share of voice"; "track the competition") | not observed at fetched level | yes (SOV; benchmarking) | yes (SOV) | L1 |
| Reach/impressions & coverage-value framing | yes (potential reach; customer "advertising value" quote) | yes ("measure the reach of your coverage… connect earned media results to business outcomes") | not observed | yes (readership data) | not observed at fetched level | L1 |
| Key-message / message pull-through tracking | yes (named metric) | yes ("effectiveness of your key messages") | not observed | not observed | not observed | L1 |
| Alerts on conditions + delivery channels | yes (email/Slack-class; "1M alerts daily" claim) | yes (mobile app, Slack/Teams, inbox reports) | yes (real-time alerts) | yes (unlimited real-time alerts; newsletters/briefings) | yes (keyword/page-based alerts) | L1 |
| Dashboards / reports / exports | yes (custom dashboards, AI summaries) | yes (executive-ready branded reports) | yes (Company Insights reports; curated newsletters) | yes (Advanced Dashboards; Insight Reports) | yes (auto-updating reports, templates) | L1 |
| Top publications / journalists / influencers | yes (top publications, influencers, journalists) | not observed at fetched level (database is outreach module) | not observed | not observed | yes (influence indicator, per listening pass) | L1 |
| Harmful-content / risk detection on coverage | yes (anomaly/narrative-shift detection) | yes (React Score: hate speech/fake news/sarcasm/spam) | not observed (Risk family is sibling) | yes (Reputation Threat Sensing; Ask AIQ investigation) | not observed | L1 |
| AI summaries / conversational assistant | yes (Mira) | yes (CisionOne AI) | yes (AI Assistant grounded in licensed content) | yes (Ask AIQ) | yes (AI tools) | L1 (current-gen) |
| Campaign-scoped measurement | yes (campaign comparisons) | yes ("measure campaign performance") | not observed | yes ("evaluate and optimize your media campaigns"; campaign monitoring guide) | yes ("measure your campaign performance") | L1 |
| Broadcast TV/radio monitoring | yes (210 US DMAs claim) | yes (3000+ stations, stream and share) | video sources in archive | yes (broadcasts in search scope) | not observed | L2 |
| Print monitoring | yes (400k+ traditional) | yes (global print publications) | archive includes print lineage | not observed | not observed | L2 |
| Social listening module (suite packaging) | yes (separate capability) | yes (separate module) | no | partial (social in search scope; no engagement suite) | yes (same engine, separate label) | L2 |
| Journalist database / outreach module | yes (Media Relations capability) | yes (Journalist Outreach module) | no | no | no | L2 |
| LLM/AI-answer visibility monitoring | yes (GenAI Lens / AI Visibility Tracking) | yes (AI Visibility module) | not observed | yes (LLM monitoring; AI citations) | not observed | L2 (new-gen) |
| Licensed premium/paywalled content | not observed as differentiator | yes (10k+ premium titles) | yes (defining posture) | yes ("premium and licensed content sources") | not observed | L2 |
| Custom/first-party content upload | not observed | not observed | not observed | yes (Add Custom Content with tagging) | not observed | L2 |
| API / data feeds | yes (API access per listening pass) | not observed | yes (Feeds & APIs) | yes (API product) | not observed | L2 |
| Curated newsletters / analyst briefings | not observed | not observed (Professional Services module) | yes (Curated Newsletters) | yes (Newsletters and Briefings; Insight Reports) | not observed | L2 |
| Managed/professional services | yes (professional services org per customer quote) | yes (Professional Services module) | not observed | yes (customer success; report services) | no | L2 |
| Reputation ranking/scoring data product | no | no | no | yes (Signal AI 500) | no | L2 |
| Free alert-only pole | no | no | no | no | free trial only | L2 (boundary pole; Google Alerts class) |
| Historical depth stated | "extensive historical data" (unquantified) | not quantified | deep archive (unquantified at fetched level) | not quantified | "up to 2 years" | L3 (per-product) |

Stable commonalities across all five (layer B): the define → collect → measure → deliver loop; standing watch definitions over the organization's own media presence; continuous collection into an accumulating item-level record; editorial coverage as the signature source class; organizational measurement (volume/trends at minimum); alerts; dashboards/reports. Sentiment, SOV, reach, key-message tracking, AI assistance are near-universal in the modern sample (L1). Broadcast/print/social/LLM sources, outreach modules, licensed content, APIs, managed services are packaging- and segment-dependent (L2).

## Canonical Abstraction

### L0 — Defining Invariant

Three structures held jointly, plus the purpose clause:

1. **The organization's own media presence as the monitored subject, held as standing watch definitions.** Persistent, user-maintained watch expressions (saved searches, mention streams, topics, tracked interests) over the organization's name, brands, products, and spokespeople — commonly extended to competitors, industry topics, and stakeholders. The watch outlives any single session and defines everything downstream. Remove → one-off news search or a consumer news app.
2. **Continuous collection of matching published media into an accumulating item-level record.** The platform sweeps media sources continuously and captures each matching item — news article, broadcast segment, print piece, social post, podcast mention — as an individual, attributable, time-stamped record with source metadata. **Editorial coverage (news, broadcast, print — journalist-authored media) is the signature source class**; social platforms, forums, blogs, review sites, and podcasts are common extensions. Remove the standing collection → one-off search; remove the editorial center of gravity (social-only substrate) → Social Listening; remove item-level capture → aggregate-only analytics.
3. **Organizational measurement and delivery of the collected coverage.** The record is computed into coverage measurement — volume and trends at minimum; sentiment, share of voice, reach, and key-message tracking as the mature layer — and surfaced to the organization through alerts, digests, dashboards, and reports for communications decisions. Remove → a raw feed or clip archive with no organizational use.

Purpose clause: the platform exists so the organization knows what published media say about it — and can act on that knowledge and prove impact — for communications, PR, reputation, and risk decisions.

Jointly-held is load-bearing: 1 alone = saved news searches / an alert service (the Google Alerts class); 2 without 1 = a news archive or data feed; 3 without 1+2 = reporting with nothing behind it; 1+2 without 3 = a clip archive, not a monitoring platform; 2+3 without 1 = generic media-data mining.

### L1 — Common Mature Structure

Present in essentially all mature modern products; not required to recognize the Type:

- sentiment analysis (machine-inferred at scale)
- share of voice / competitor benchmarking
- reach/impressions estimation and coverage-value framing (business-outcome linkage language)
- condition-based alerts (spikes, sentiment shifts, harmful content) with delivery channels (email, chat tools, mobile push)
- dashboards, scheduled/automated reports, executive-ready branded reports, exports
- top publications / journalists / influencer identification
- key-message / message pull-through tracking
- campaign-scoped measurement
- multilingual, multi-market coverage
- AI summaries / conversational assistants (current generation)
- mobile apps

### L2 — Variant / Optional Structure

- broadcast TV/radio monitoring (live streams, clips; region-priced data)
- print monitoring (legacy/regional emphasis)
- social listening module (suite packaging — the same engine family sold as a separate pillar)
- journalist database / media relations module (PR-suite packaging)
- press release distribution (sibling product family)
- LLM/AI-answer visibility monitoring (new-generation surface)
- licensed premium/paywalled content access (archive-first pole's defining posture)
- custom/first-party content upload blended into the coverage record
- API / data feeds (platform-as-data posture)
- curated newsletters / analyst briefings as managed output
- professional/managed services layer
- reputation ranking/scoring data products
- free alert-only tools (the minimal adjacent pole — Google Alerts class)

### L3 — Vendor-specific (kept out of the final document)

- Meltwater: Mira AI assistant; GenAI Lens; 400k+ traditional sources / 200M+ online publications / 20k+ podcasts / 210 US DMAs / 240+ languages; "1.3B documents ingested daily / 1M alerts daily" claims; message pull-through naming; Collect→Analyze→Surface→Enable action step naming; NASCAR "advertising value" customer quote.
- Cision: Mention Streams; React Score (harmful-content classes: hate speech, fake news, sarcasm, spam); CisionOne AI; AI Visibility module; 500k+ journalist database; 3000+ TV/radio stations / 60k+ podcasts / 10k+ premium titles / 190+ countries / 96 languages; three-step dashboard builder; branded report styling.
- Factiva: AI Assistant grounded in licensed content with source links; Company Insights reports; Curated Newsletters; Feeds & APIs; Sentiment Signals; 33 languages / 200+ countries; Dow Jones/WSJ content lineage.
- Signal AI: AIQ; Ask AIQ agent; Signal AI 500 reputation ranking; 226 markets / 120+ languages; "5.5M+ articles ingested per day / 100M+ entities labeled per day" claims; readership data; AI citations; Add Custom Content tagging model; Insight Reports catalog.
- Mention: Monitor/Analyze/Engage pillar naming; "1 billion sources"; "data up to 2 years"; keyword-based and page-based alert triggers; Agorapulse ownership; one-engine-many-labels footer.

## Vendor-specific Findings

- The monitoring/listening split is packaged differently per vendor: CisionOne sells Media Monitoring and Social Listening & Management as separate modules; Meltwater sells Media Monitoring and Social Listening as separate capabilities; Talkwalker (per the listening pass) sells them as separate product pillars; Mention sells one engine under both labels. Packaging variance over a shared engine family — boundary evidence, not Type evidence.
- Cision's "Compare your Mention Streams side by side" documents the watch object as first-class and comparable — structural observation, single-product phrasing.
- Signal AI's "Add Custom Content… seamlessly integrate into saved searches and dashboards" documents first-party content blending into the coverage record — single-product evidence, held L2.
- Meltwater's "message pull-through" and Cision's "effectiveness of your key messages" independently name key-message tracking — two products, held L1.
- The clipping vocabulary persists in the market's own language ("unlimited clippings" — Signal AI customer quote; "clip tracking"/"clip collection" — Meltwater's framing of the traditional baseline). Historical continuity evidence.

## Rejected Findings

- "Media monitoring = news only" — rejected: four of five sampled products extend beyond news (social, podcasts, broadcast, LLMs); but the reverse also fails — "media monitoring = any public source including social-first conversation" is rejected because the editorial-coverage center of gravity is what separates the Type from social listening (Factiva, the news-only pole, is unmistakably media monitoring; a social-only monitor is listening).
- "Social listening is part of the definition" — rejected: Factiva ships none; suites package it as a separate module/capability. L2.
- "Broadcast/print monitoring is definitional" — rejected: regional/expensive data; Mention and Signal AI's fetched pages do not center it; the clip-service era handled print, the modern era adds broadcast — coverage-class variance, not structure. L2.
- "AI is part of the definition" — rejected: the clip-service and database-alert eras satisfy the core without AI; all five sampled products are AI-led today (era-typical). L1.
- "Media value / AVE is a defining metric" — rejected: observed only as vendor/customer vocabulary (Meltwater NASCAR quote; Cision's "connect earned media results to business outcomes" is outcome-linkage language, not a specific AVE metric); no canonical metric asserted.
- "The Type is defined by the PR audience" — rejected as sole criterion: Signal AI's primary audience includes risk/compliance teams; Factiva sells to research and business development. Communications-first, risk-extended — the purpose clause covers both without hard-coding a job title.
- "Alert-only free tools are the Type" — rejected: Google Alerts class satisfies watch + notification but has no accumulating platform record and no measurement layer; held as the minimal adjacent pole (consistent with the listening pass's treatment of Talkwalker Alerts).

## Boundary Findings

1. **vs Social Listening Platform (§06, processed 2026-09-07) — DISCHARGES that pass's joint-review flag from this side.** The center-of-gravity discriminator holds from both directions: this Type's signature source class is editorial coverage (journalist-authored news/broadcast/print; the mention item is a coverage item/clip), listening's is public consumer-authored conversation (social-first; the item is a post/comment). Every sampled suite spans both grammars (CisionOne modules; Meltwater capabilities; Talkwalker pillars per the listening pass; Mention's dual self-label), so the seam is center of gravity, not exclusive source sets. Removal tests recorded both directions: restrict sources to editorial media + coverage metrics → media monitoring; restrict to social/consumer conversation → social listening. **Keep-both RATIFIED.** Secondary confirmation: the two Types' L0s share the watch→collect→analyze skeleton; the source grammar and item grammar differ.
2. **vs Brand Reputation Management (§06, processed 2026-09-06) — DISCHARGES that pass's joint-review flag from this side.** The corporate reputation-intelligence pole (Signal AI-style: media/narrative sensing, benchmarking, reporting for comms/risk teams) is documented in this pass's sample and has no review loop — it belongs with media monitoring, exactly as that pass predicted. Reputation management's center remains the review/feedback loop with per-signal organizational action (respond/solicit/route). Structural test: remove per-signal action from reputation → a monitoring/listening platform remains; add per-signal response workflows to monitoring → drift into reputation territory. **Keep-both RATIFIED; the pole is held as a variant emphasis inside this Type (AI-first reputation intelligence), not a separate leaf.**
3. **vs Competitive Intelligence Platform (§06, processed 2026-09-07)** — consistent with that pass's boundary row, confirmed from this side: media monitoring tracks the organization's OWN presence across media; CI tracks external entities (competitors at the center) and adds curation/distribution machinery (battlecards, embedded delivery). Remove tracked external competitors and point collection at the own brand → media monitoring; add competitor-entity curation and internal distribution programs → CI. Sampled products straddle deliberately (Factiva sells a Competitive Intelligence use case; Meltwater lists competitive intelligence as an AI use case) — center of gravity decides. No new flag.
4. **vs Public Relations Management Platform (§06, processed 2026-09-06)** — consistent with that pass's boundary row, confirmed from this side: monitoring listens and measures after publication; it holds no media contacts, sends no pitches, organizes no campaigns. PR management consumes monitoring as a coverage source (that pass: "Remove contacts/outreach → Media Monitoring"). In-suite evidence: CisionOne ships Journalist Outreach as a separate module beside Media Monitoring; Meltwater ships Media Relations as a separate capability. No new flag.
5. **vs Media Relations Platform (§06 sibling, unprocessed)** — the journalist-database/outreach modules inside monitoring suites (Cision Journalist Outreach; Meltwater Media Relations) are that Type's subject matter; monitoring itself has no outreach. Flag recorded for that pass.
6. **vs Social Media Analytics Platform (§06 sibling, unprocessed)** — consistent with the listening pass's flag: analytics measures the organization's own connected accounts (performance of its own posts); media monitoring observes third-party published coverage. Monitoring suites bundle analytics modules; the substrate (own accounts vs public coverage) decides. Flag stands for that pass.
7. **vs News Application / News Aggregator (§02.04)** — both present news items, but the news app's subject is the reader's interests and its unit is the feed for reading; the monitoring platform's subject is the organization's own media presence and its units are the watch definition, the item-level coverage record, and organizational measurement. Factiva's "personalized news stream" shows the watch grammar can look feed-like; the organizational subject + measurement/delivery layer decides. Removal test: remove the organizational monitored-subject and measurement → a news reader.
8. **vs Digital Risk Protection (§15, processed 2026-09-08)** — DRP monitors impersonation/abuse of the organization's external footprint and drives takedown/enforcement; media monitoring observes coverage with no enforcement path. Adverse-media/negative-news screening (per the sanctions pass) is one data family inside risk products; a pure negative-news monitor without list screening is this Type's territory. Seam held.
9. **vs Press Release Distribution Platform (§06, processed)** — no unit overlap: PRD's unit is one authored release broadcast through a gated network; monitoring's unit is the standing watch over third-party coverage. Distribution appears in suites as a sibling product (Cision↔PR Newswire; Meltwater Press Distribution). Seam held.
10. **Alert-only minimal pole** — free tools (Google Alerts class) satisfy watch + notification but lack the retained item-level platform record and the measurement layer; classified as the Type's minimal adjacent pole (a service, not a platform). Removal test: remove the platform record + measurement → alert service.

## Historical / Market-Sample Check

- **Clip-service era (late 19th–20th century press clipping bureaus; broadcast monitoring services):** monitored subject (client's name/topics), collection (readers/monitors sweeping publications and airwaves), item records (physical clippings, tape segments), delivery (clip reports/books on a periodic cycle, client reporting). All three L0 structures hold without any software. ✓
- **Database-alert era (LexisNexis/Factiva-lineage news archives):** saved searches + alerts over licensed news archives + item records with source metadata. ✓ (Factiva in the sample is this pole's living form.)
- **Regional check:** broadcast/print monitoring depth is region-priced and varies by market (Cision/Meltwater document US DMA coverage; regional monitoring agencies persist) — coverage-class variance, not a different Type. ✓
- **Minimal-pole check:** alert-only free tools fail the platform-record + measurement legs; held as the adjacent minimal pole. ✓
- **AI-era check:** AI summaries/assistants, harmful-content detection, and LLM-visibility monitoring are current-generation L1/L2 structures on the same L0; the Type is fully recognizable without them. ✓

Conclusion: the definition is not over-fitted to the modern AI-suite implementation; the clip-service and database-alert eras satisfy the same three-part structure.

## Uncertainties

1. Help-center article bodies were not fetched for any product (prior passes found Meltwater/Cision help centers JS-gated; not re-attempted per network rule). Operational specifics — query/boolean syntax, per-source retention windows, plan gating, alert-latency defaults — are NOT asserted anywhere; only Mention's "data up to 2 years" is a directly documented window (product-specific).
2. All scale figures (Meltwater 1.3B documents/day, 1M alerts/day, 240+ languages; Cision 3000+ stations, 60k+ podcasts, 10k+ premium titles, 190+ countries/96 languages, 500k+ journalists; Signal AI 5.5M articles/day, 100M+ entities/day, 226 markets; Mention 1B sources) are vendor marketing claims — carried as claims only, none promoted to the final document as fact.
3. Reach/impressions methodology and coverage-value (AVE-class) metrics are vendor-defined and contested in the industry; no canonical formula asserted.
4. Whether the LLM/AI-answer visibility wave (Meltwater GenAI Lens, Cision AI Visibility, Signal AI LLM monitoring) stays a surface extension of this Type or becomes its own Type — watch item, consistent with the listening pass's note.
5. The media-relations and social-media-analytics siblings are unprocessed; those seams are held from this side only and flagged for their passes.
6. Factiva's social-source posture (whether any social monitoring exists beyond the fetched pages) unverified; Factiva is used as the news-only pole on fetched evidence only.

## Final Synthesis

A Media Monitoring Platform is the organization's standing instrument for knowing what published media say about it. Its world is built around three jointly-held structures: standing watch definitions over the organization's own media presence (brand, products, spokespeople, commonly competitors and industry topics); continuous collection of the matching published media into an accumulating item-level record — editorial coverage (news, broadcast, print) as the signature source class, with social, web, podcast, and increasingly LLM-answer sources as common extensions; and organizational measurement and delivery that computes the record into coverage insight (volume and trends at minimum; sentiment, share of voice, reach, and key-message tracking as the mature layer) and surfaces it through alerts, digests, dashboards, and reports for communications, PR, reputation, and risk decisions. Around this core, mature products add competitor benchmarking, harmful-content detection, AI summaries and conversational assistants, executive-ready branded reporting, mobile apps, and — depending on packaging — broadcast/print depth, social listening modules, journalist databases and outreach, licensed premium archives, APIs, curated newsletters, and managed services. The Type's sharpest boundaries: vs social listening (coverage-centric vs conversation-centric — the same engine family sold across both grammars), vs brand reputation management (observational measurement vs the per-signal review loop; the corporate reputation-intelligence pole belongs here), vs competitive intelligence (own brand vs external entities), vs PR management and media relations (no contacts, no outreach), vs news apps (organizational subject + measurement vs consumer reading), and vs digital risk protection (observation vs enforcement). The definition survives the historical check: the clip-service era and the database-alert era satisfy the same three-part core without any modern feature.
