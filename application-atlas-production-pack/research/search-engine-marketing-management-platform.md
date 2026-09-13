# Research Notes — Search Engine Marketing Management Platform

Research date: 2026-09-07

## Research Goal

Understand what a Search Engine Marketing (SEM) Management Platform actually is as an Application Type: what objects it manages, how it relates to the search engines' own ad platforms (the "engines"), what its core workflows are, and where its boundaries lie against SEO platforms, DSPs/programmatic tools, ad servers, engine-native editors, and generic advertising campaign management.

## Initial Boundary (hypothesis before research)

- Hypothesis: a third-party SaaS layer that links to search-engine ad accounts (Google Ads / Microsoft Advertising class), manages the campaign structure and spend controls (keywords, bids, budgets, ads) from one workspace, pulls performance data back from the engines, and automates optimization and reporting.
- Users: PPC/SEM specialists, agencies managing many advertiser accounts, in-house performance teams, SMBs via guided tools.
- Adjacent types to test: SEO Platform (organic vs paid), Advertising Campaign Management (generic cross-channel), DSP/Programmatic (exchange inventory vs search auctions), Ad Server (serving vs managing), Media Buying Platform, Marketing Analytics/Attribution (measurement layer), Keyword Research Application (capability vs Type).
- Risk noted up front: the "platform" framing may be eroding as products broaden to social/retail media — the search-specific framing may be a slice of a broader ad-management category.

## Research Questions

1. How does the platform connect to the engines (account linking, APIs)? Who is system of record?
2. What objects does it manage (campaigns, ad groups, keywords, ads, extensions, bids, budgets, targeting) and through what mechanisms (grid, bulk sheets, APIs, scripts)?
3. What is the standing work loop (monitor → decide → change → measure → report)?
4. How far does automation go — rules, scripts, algorithmic bidding, auto-apply vs human approval?
5. What reporting/agency machinery exists (cross-client ops, white-label, scheduled reports)?
6. Where are the boundaries vs SEO, DSP, ad server, engine-native editors, generic ad campaign management?
7. Historical check: would 2000s-era bid-management platforms and engine-native editors still fit / be excluded?

## Representative Products

| Product | Pole / rationale |
|---|---|
| Marin Software (MarinOne) | enterprise incumbent, multi-engine search-first with social/retail-media extensions; deep official help center |
| Optmyzr | agency/mid-market optimization-workflow philosophy ("layer over the ad platforms", rule engine, one-click optimizations); rich help center |
| Adalysis | specialist Google Ads + Microsoft Ads audit/monitoring/automation pole; GitBook product docs with full index |
| Skai (formerly Kenshoo) | enterprise omnichannel "commerce media" pole where search is one channel among retail media/social |

Selection notes: WordStream Advisor (SMB guided-advice pole) was attempted but the domain returned 403 twice — abandoned per network rules; the SMB-guided pole is therefore under-sampled (recorded under Uncertainties). Google Ads Editor's own page timed out; the engine-native boundary is evidenced from the third-party side (a vendor comparison page) and used with that caveat.

## Sources

- Marin: https://www.marinsoftware.com/ (root; acquisition notice), https://www.marinsoftware.com/lp/search-ads (paid search solution page), https://support.marinsoftware.com/ (help center home), https://support.marinsoftware.com/en_US/Managing_Campaigns (Managing Campaigns category). All fetched 2026-09-07.
- Optmyzr: https://www.optmyzr.com/ (root; capabilities, platforms, workflow, security), https://help.optmyzr.com/en (help center collections). Fetched 2026-09-07.
- Adalysis: https://adalysis.com/ (root), https://docs.adalysis.com/ (help center index + llms.txt), https://docs.adalysis.com/onboarding/getting-started/quick-start.md (quick start), https://adalysis.com/free-tool-comparisons/ (comparison hub), https://adalysis.com/google-ads-editor-alternative/ (vs engine-native editor). Fetched 2026-09-07.
- Skai: https://skai.io/ (root; platform nav, positioning). Fetched 2026-09-07.
- WordStream: https://www.wordstream.com/ and https://www.wordstream.com/advisor — HTTP 403 both, abandoned.

## Product A — Marin Software (MarinOne)

### Key observations (evidence layer A unless noted)

Positioning & scope:
- Root page: "Automate and manage ad platforms at scale" (MarinOne); solutions by channel: Paid Search, Paid Social, Retail Media, App Advertising; "Marin for Agencies — automate, optimize, and analyze all of your clients' paid media campaigns". Acquired by Zax Capital ("AI-first era").
- Paid search page: "Unmatched platform for paid search — identify growth opportunities and maximize revenue across Google, Microsoft, Apple Search Ads, and more"; publisher logos include Google, Microsoft, Yahoo, Yahoo Japan, 360 (regional engines), plus social publishers (Meta, TikTok, LinkedIn, X, Snap, Pinterest, Reddit) and retail media publishers (Amazon, Walmart, Instacart, Criteo, CitrusAd, Target). Comparison table positions Marin against a search publisher's own tool, an enterprise cross-platform manager, and other third-party suites on publisher coverage, PMax support, data-warehouse integration, budget pacing, automation (no-code and script-based), dynamic campaign creation.
- "Bringing it all together — a single interface for measuring, managing, and optimizing all your paid search programs."
- "Extends Google Ads — supercharge Google Ads platform with in-app and bulk management for all major ad formats" (text, responsive search, dynamic search, video, shopping, Display, YouTube, Discovery campaigns). → Direct evidence of the layer-over-engine framing.

Connection & system of record:
- Help center: "The Publisher Account Linking Wizard allows you to integrate your publisher accounts into the platform." (Article: The Publisher Account Linking Wizard.)
- Help categories: Optimization with Ascend, Managing Campaigns, Revenue Tracking, Search, Social, Ecommerce, Reports, Your Account, Marin University, Customization, Scripts.
- API article: "Marin offers two different APIs for customers to programmatically create and manage campaigns… the Marin API can be used to programmatically write data to" the platform; "post-only REST API for select objects: campaigns, groups, keywords, ads and strategies."
- Sizmek workflow visualization article: "the specific campaign management workflow that occurs between our platform and [third-party tracking]… from campaign creation all the way to the campaigns going live, for publishers like Google and Microsoft."
- Status/lifecycle evidence: pause/resume/delete campaigns, groups, keywords, creatives; error "Item has a pending change that is being posted or is in Held status. Please post or cancel held changes before making further edits." → staged-change model between platform and engine; "Keyword has been Deleted and Can Not be Modified" when deleted at publisher → engine is authoritative for object existence.
- Publisher editorial control: "Bulk uploading holiday ads and keywords in paused status at least a week before [Black Friday] will allow enough time for publisher editorial review." → engines review/approve creative content.

Managed objects & mechanisms (Managing Campaigns category, 74 articles):
- Bulk uploads: "create or edit hundreds – or even thousands – of campaigns, groups, keywords, or ads"; bulk sheet format rules (CSV/Unicode text, column headers, error rows); uploads via FTP "for repetitive tasks such as keyword bid changes or monthly budget setting"; cross-client bulk uploads: "submit a single bulk sheet and use it to edit objects in different client accounts" (agency machinery).
- Grid editing: "edit objects at all levels of the account hierarchy… single edit mode or multi-edit mode"; Copy Tool (campaigns, groups, keywords, creatives, placements); renaming campaigns/ad groups via bulk sheets.
- Dimensions: tagging objects at Account/Campaign/Group/Keyword/Creative level for custom segmentation, roll-up reporting, testing by dimension.
- Marin Scripts: "leverage the power of Python for streamlined reporting, management, and optimization… Scripts can run across the wide range of publishers… tag dimensions, change an object's status, set campaign budgets, set bids."
- Keyword Expansion: "identifies new keywords and negatives based on your existing set of keywords for Amazon, Google, and Microsoft publisher accounts."
- Negative keywords; geo targeting ("access to search engine geo-targeting capabilities provided by each publisher"); network/distribution targeting (Search / Search Partners / Display); ad scheduling (dayparting: "adjust keyword bids by day-of-week or time-of-day… percent of the keyword bid"); A/B creative testing ("automatically analyzes performance to identify any creatives over/under performing relative to the ad group average"); landing-page testing.
- URL machinery: URL Builder, Destination vs Click-Through URL columns, tracking parameters across publisher accounts (attribution/tracking integration).

Optimization & measurement:
- "Marin's Insights feature… provides you with actionable optimization [opportunities]"; paid search page: "Each Insight offers an estimated impact to help you prioritize your efforts."
- Marin Bidding: "Outperform Smart Bidding with Marin Bidding that runs across publishers and accounts"; "Predict conversions, revenue, and profit at varying levels of spend across publishers for better budgeting decisions" (predictive budgeting).
- Marin Attribution: "Track online and offline conversions… or any other third-party tracking system."

## Product B — Optmyzr

### Key observations (evidence layer A unless noted)

Positioning & scope:
- "PPC Management Software"; "Worry-free account management for the AI and automation era of PPC… Review insights, monitor campaigns, optimize performance, and build safeguards with Optmyzr's round-the-clock PPC automation." Hero lists "Google Search & Shopping, Performance Max, Microsoft Ads".
- Platform lines: "Optmyzr for Search", "Optmyzr for Social" (Meta/LinkedIn), "Optmyzr for Amazon Ads". "Platforms We Support: Google Ads, Microsoft Ads, Amazon Ads, Meta Ads, LinkedIn Ads."
- Audiences: PPC & digital agencies, PPC freelancers, in-house marketers, enterprise teams ("manage over $500,000 a month in ad spend… unlimited accounts").
- Scale stats (vendor claims, L3): $5.37B ad spend managed, 461,000+ ad accounts connected, 6.1B+ "optimization actions".

Workflow (getting started — A):
- "1 Sign up and connect an ad account. 2 Start with an audit (recommended). 3 Optimize using Rule Engine or other tools." → connect → audit → optimize loop.

Capability families (root page — A):
- Real-Time Campaign Monitoring: "alerts to monitor KPI metrics and budgets", "guardrails to prevent overspending and wastage", alert delivery options (testimonials confirm Slack delivery).
- User-Controlled Automation: "Build and layer your automation over the ad platforms. Reclaim control over performance, even when you're not around"; "Build creative, fully customizable automated rules"; security blurb: "No changes without your approval, ever" → human-approval automation posture.
- AI for Paid Search: "AI Sidekick is your natural language copilot for any account questions."
- Bid & Budget Protections: "simplified analysis & management of manual bids", "assisted optimization of ROAS and CPA targets", "budget pacing and alerts".
- Rapid Audits & Analysis: "audits for a bird's eye view of account health", "cause charts highlighting the impact of previous optimizations".
- One-Click Optimizations: "Get your campaigns as close to perfect as possible and make changes without ever opening the ad platform UI" → write-back to engine without opening the engine UI.
- Quick-Fire Reporting: templates, automated delivery with interactive links.

Named tools (testimonials + footer — A, L3 naming): Rule Engine, PPC Investigator, Negative Keyword Finder, N-Gram analysis, Spend Projection, Projected Spend report, Auction Insights Visualiser, Ad Text Optimisation (RSAs), Google Shopping toolbox, Feed Audits, Blueprints, weather-based bid changes, Sale Day Command Centre, Enhanced Scripts for Google Ads (help center collection), Workflows & Bulk Operations.

Help center collections (A): General Information & Getting Started; Manage Your Accounts & Portfolios ("How to link, set up, and overview your accounts"); Performance Monitoring, Audits & Insights; Optmyzr Express ("one-click optimizations suggestions across multiple ads accounts"); Search Query and Keyword Management; Ad & Campaign Optimization; Bids & Budget Management; Rule Engine (58 articles); Manage Shopping Ads; Reporting; Workflows & Bulk Operations; Enhanced Scripts for Google Ads; Utilities.

Security posture (A): encryption, two-factor authentication, "we do not share your personal or account data with advertising platforms", "you retain full control over your campaigns — only you or those you authorize can make changes."

## Product C — Adalysis

### Key observations (evidence layer A unless noted)

Positioning & scope:
- "Meet your PPC copilot… Adalysis audits, monitors, optimizes, and automates your Google Ads and Microsoft Ads campaigns." → two-engine specialist scope.
- Audiences: digital agencies, PPC advertisers/brand advertisers, PPC specialists, team leads. "2,000+ PPC agencies and brand advertisers" (L3).

Getting-started workflow (docs — A):
- Quick start: "1 Start with your audit alerts to see what needs fixing first (daily). 2 Check your performance monitors to spot changes (weekly). 3 Set up budget pacing to stay on track with your spend (monthly…). Automating your pacing doesn't make any changes to your account." → audit-first cadence; explicit default automation posture (monitor, don't mutate).
- Account organization docs: "Linking accounts — link and unlink PPC accounts from your Adalysis plan"; "Data refresh frequency — learn how often your data is updated and how to run manual updates"; "Change history — get a full change history for your whole team"; team members, account tags, filters, notes.

Audit machinery (docs — A):
- "Audit: get started in minutes, with 100+ prebuilt checks, custom alerts, and audit automation." Prebuilt alert list spans: account (recommendations from Google), campaigns (network targeting, broad-match settings, search partner traffic), ad groups (no/too many RSAs, ads, keywords), ads (disapproved assets, falling CTR, misspellings), keywords (poor conversions, rising CPC/CPA, falling ROAS, duplicates, conflicts with negatives, match-type misuse, quality score), negative keywords (missing, repeated, shared lists, misuse), search terms (duplicates, new keyword/negative suggestions incl. n-gram), placements, landing pages (broken URLs, poor conversions), ad extensions, bid suggestions (device/location/age/gender/parental/income/audience adjustments, keyword bids below first-page/top-of-page), product groups, PMax assets/asset groups/search terms. Custom alerts; auto-resolve ("resolve straightforward alerts automatically").

Performance & analysis (docs — A):
- Performance monitors ("detect big trends before anyone else"), root cause analysis via "Performance Analyzer" (visual flowchart), performance goals, impression share analysis, segments (hour-of-week, ad schedule editing "create and edit ad schedules directly in Adalysis", matched locations).

Budget machinery (docs — A):
- Budget overview: "manage your PPC budgets at scale"; pacing ("manage your target pacing without the spreadsheets"); "Daily budget recommendations — convert an account monthly target budget into individual campaign daily budgets"; Auto manage ("activate your budget copilot"); "Future targets & rollover — set future targets and manage budget rollover"; "Daily stop — automatically pause campaigns that pass their daily budget limit"; "Budget groups — manage groups of budgets"; custom schedule budgets (seasonal); budget boost alerts; budget analytics; CSV bulk updates.

Bidding & management (docs — A):
- Bidding: "manage your bid adjustments" (device/location/demographic/audience), keyword bid suggestions, bidding change review reminders.
- Campaigns: campaign settings ("get insights and make updates in the same place"), "Build campaigns from CSV files — populate your campaigns in just a few easy steps" (campaign builder "with hundreds of ad groups… unique ads using variables from your file"), link missing campaigns.
- Keywords: match-type changes in bulk, negative keywords "at the ad group, campaign, account, and list level", "build campaigns from keyword lists — organize your keywords into structured ad groups."
- Search terms: search terms and n-grams, search term tools, PMax search terms, keyword mining tutorial.
- Ads: RSA creation/management/A-B testing ("boost efficiency with smart tools and AI"), add headlines/descriptions to multiple ads, ETA→RSA bulk conversion, copy expanded DSAs, bulk pause.
- Ad testing: "test your ads without manual setup", single & multi ad-group testing, "automatic pausing of losing ads", thresholds/confidence FAQs.
- Labels; placements; landing pages; quality score (impression-weighted aggregate insights).

Reporting (docs — A):
- Reporting is deliberately built on Looker Studio ("Why Looker Studio — the Adalysis take on native reporting features"); setup guides for Google Ads/Microsoft Ads/Facebook/Google Analytics data sources; template customization; "white-label options are available."

Boundary evidence (A, vendor-comparison source — use for the distinction, not as neutral benchmark):
- "Adalysis vs Google Ads Editor": "Google Ads Editor stops at basic bulk execution. Adalysis takes you further with performance insights…"; "Google Ads Editor waits for manual input. Adalysis acts as your PPC copilot…"; "Adalysis keeps optimizing — even when you're logged out."; budget framing: "Google Ads Editor just tells you when a campaign is 'limited by budget'. Adalysis offers budget boost alerts…"; "Automate daily budget adjustments at the account level or across custom budget groups."
- Comparison hub also contrasts vs the engine's web interface ("why the Google Ads interface isn't enough") and vs engine-native scripts ("a powerful alternative to Google Ads scripts").

Era-typical AI (A): MCP server — "connect Adalysis to Claude, ChatGPT, or any AI assistant"; AI Max tools.

## Product D — Skai (formerly Kenshoo)

### Key observations (evidence layer A; shallow — positioning page only)

- "AI-Powered Commerce Media Platform… centralize their media data, activate across channels, and measure what works."
- Platform nav: MEDIA — Omnichannel Planning, Retail Media, Search, Social; DATA & INSIGHTS — Data Centralization, Strategic Digital Shelf, Retail Insights, Content Optimization, Celeste AI; COMMERCE — Ticketing Automation, Revenue Recovery.
- "Manage retail media, search and social from one platform to run campaigns across every channel."
- Scale claims (L3): 300+ publishers, 8,200+ brands; "all your data in one place — media data, first-party data, commerce data… with a single login."
- Audiences: CPG brands, media agencies (case studies: Dentsu, Jellyfish, Publicis; brands: PepsiCo, Heinz, Dr. Squatch).
- Sign-in domain app.kenshoo.com; developer hub developers.kenshoo.com (API surface implied; not fetched).

Interpretation: Skai evidences the enterprise omnichannel pole — search campaign management exists as one module of a broader commerce-media platform (evidence for the scope-broadening variant, layer B for "search is a managed module" since the search page itself was not fetched).

## Cross-product Comparison

| Aspect | Marin | Skai | Optmyzr | Adalysis |
|---|---|---|---|---|
| Linked engine accounts (A) | Publisher Account Linking Wizard; Google, Microsoft, Apple Search Ads, Yahoo, Yahoo Japan, 360 + social + retail media | "300+ publishers"; Google/Amazon/Microsoft/Walmart/TikTok-class logos | "connect an ad account"; Google, Microsoft, Amazon, Meta, LinkedIn | "link and unlink PPC accounts"; Google Ads + Microsoft Ads only |
| System of record (A) | engine (publisher) — deleted-at-publisher objects uneditable; publisher editorial review | engine (implied by module framing) | engine ("no changes without your approval"; changes applied "over the ad platforms") | engine (linking model; data refresh from engines) |
| Managed objects (A) | campaigns, groups, keywords, creatives, bids, budgets, extensions, URLs, targeting via grid/bulk/API/scripts | search/social/retail media campaigns via one platform (search module detail not fetched) | campaigns, ads, keywords, search queries, bids, budgets, shopping feeds via tools/rules | campaigns, ad groups, ads/RSAs, keywords, negatives, search terms, bids/bid adjustments, budgets, labels via docs tools |
| Write-back mechanism (A) | bulk sheets (CSV/FTP), multi-edit, Marin API, Scripts; staged/Held → posted to publisher | platform activation (detail not fetched) | one-click optimizations "without ever opening the ad platform UI"; rules | in-platform edits, bulk CSV builders, automation/auto-resolve |
| Performance feedback (A) | "measuring, managing, and optimizing… in one interface"; dimensions roll-up | "centralize… and measure" | monitoring, cause charts, PPC Investigator | monitors, root-cause analyzer, impression share, segments |
| Automation (A) | Scripts (Python, cross-publisher), API, no-code automation; Bidding "runs across publishers and accounts" | Celeste AI agent era | Rule Engine (58 help articles), "no changes without your approval", scripts | 100+ prebuilt checks, custom alerts, auto-resolve, "automating your pacing doesn't make any changes" (default posture), auto-pause losing ads |
| Bid management (A) | algorithmic bidding + dayparting + bid strategy objects | (search module; not fetched) | manual-bid analysis, ROAS/CPA targets, weather bids | bid adjustments by device/location/demographics, keyword bid suggestions |
| Budget machinery (A) | predictive budgeting ("predict… at varying levels of spend") | omnichannel planning | pacing + alerts, Spend Projection | pacing, monthly→daily recommendations, budget groups, daily stop, rollover, boost alerts |
| Audits (A) | Insights with estimated impact | — | account audits, Blueprints | 100+ prebuilt checks (explicit catalog) |
| Search terms/negatives (A) | negative keywords, keyword expansion | — | Negative Keyword Finder, N-gram | search-terms & n-gram tools, keyword mining |
| Ad testing (A) | creative A/B testing tool | — | ad text optimization (RSAs) | always-on ad testing with auto-pause |
| Reporting (A) | reports category; dimensions roll-ups | data centralization | templates, scheduled delivery | Looker Studio templates, white-label |
| Agency machinery (A) | cross-client bulk uploads, agencies solution | agency case studies | agencies/freelancers pages, portfolios | agency pages, multiple accounts, white-label |
| Channel scope (A) | search-first + social + retail media + app | search + retail media + social + commerce | Search product line + Social + Amazon lines | search only (Google + Microsoft) |

Layer B (cross-product commonality): every sampled product (1) links to engine ad accounts it does not own; (2) edits search-campaign spend controls and writes them back; (3) consolidates performance data in the same workspace; (4) offers rules/automation of some form; (5) addresses agency/portfolio operation. These recur across all four poles → candidate defining/standard structure.

## Canonical Model (four-layer synthesis)

### L0 — Defining Invariant (deliberately small)

A Search Engine Marketing Management Platform is a third-party management layer that operates search-engine ad accounts it does not own. Three properties; remove any one and the product is no longer this Type:

1. **Linked engine ad accounts.** The platform connects to search engines' own advertising platforms (Google Ads / Microsoft Advertising class, historically also Yahoo/Baidu/Yahoo Japan class) through official APIs/credentials, linking the advertiser's or agency's engine accounts. The engines remain the system of record: they bill, serve, and editorially review the ads; objects deleted at the engine are not editable in the platform (Marin A). Remove → the product is either a measurement layer (analytics/attribution) or its own ad platform (DSP/ad network), not a management layer.
2. **Spend-controlling campaign parameters as managed objects.** Keyword bids and campaign budgets — and, in all sampled modern products, the wider structure (keywords with match types, ads, negatives, extensions, targeting) — are edited inside the platform and written back to the engines (grid edits, bulk sheets, APIs, rules; Marin staged-change and held-status model A). Remove → a read-only reporting/audit tool.
3. **Consolidated performance feedback in the same workspace.** Spend, clicks, impressions, and conversions of the managed campaigns flow back from the engines into the platform and are attributed to the same campaign objects the user edits ("measuring, managing, and optimizing… in one interface" — Marin A; monitors/audits — Adalysis A; monitoring — Optmyzr A). Remove → a blind bulk editor (the engine-native editor case — see Boundary Findings).

The defining posture is therefore: connect → manage → measure on the engines' own accounts, as a standing layer rather than a one-off tool.

### L1 — Common Mature Structure (present across the sample; not required for recognition)

- Cross-account / cross-engine consolidation: one workspace over many engine accounts; portfolio/client grouping (Marin cross-client bulk uploads A; Optmyzr portfolios A; Adalysis multiple accounts A).
- Audit & alert machinery: prebuilt best-practice checks, custom alerts, issue prioritization (Adalysis 100+ checks A; Optmyzr audits/guardrails A; Marin Insights A).
- Rules/automation: user-defined rules, scheduled automation, script layer; spectrum from suggest-then-approve (Optmyzr "no changes without your approval" A; Adalysis pacing default non-mutating A) to auto-execution.
- Bid management: manual-bid tooling, bid adjustments by device/location/audience, algorithmic/target bidding at the enterprise pole (Marin Bidding A; Adalysis bid tools A; Optmyzr bid protections A).
- Budget management: pacing, targets, overspend/underspend alerts, recommendations, auto-adjustment (Adalysis budget suite A; Optmyzr pacing A; Marin predictive budgeting A).
- Search-term & negative keyword management: waste identification, n-gram analysis, keyword/negative suggestions, expansion (all A).
- Ad/creative management & testing: bulk ad operations, RSA handling, A/B testing with losers auto-paused (all A).
- Change history & attribution of edits to team members (Marin Activity Log A; Adalysis change history A).
- Reporting: templates, scheduled delivery, white-label/agency variants (all A).
- Bulk operations: grid multi-edit + CSV/bulk sheets, sometimes FTP (Marin, Adalysis A).
- Programmatic access: APIs (Marin API A; Adalysis MCP A), scripts (Marin Scripts, Optmyzr Enhanced Scripts A).

### L2 — Variant / Optional Structure

- Channel scope: search-only specialist vs search + paid social + retail media/"commerce media" (Adalysis two-engine specialist vs Marin/Skai/Optmyzr multi-channel A) — the dominant variant axis.
- Engine breadth: Google+Microsoft duopoly vs many engines incl. regional (Yahoo Japan, 360) and app-store search (Apple Search Ads) (Marin A).
- Optimization philosophy: insight-first workbench with human approval vs algorithmic bidding at scale (Optmyzr/Adalysis vs Marin Bidding) vs guided advice for SMB (under-sampled — WordStream unreachable).
- Reporting stack: built-in reports vs external BI surfaces (Adalysis on Looker Studio A).
- Tracking/attribution integration: URL builders, redirect tracking, revenue tracking (Marin A; capability overlaps the Attribution Type when deep).
- AI layer: natural-language assistants, MCP servers, agent-era features (all sampled, era-typical — not definitional).
- Segmentation aids: custom dimension/tag layers over the engine hierarchy (Marin Dimensions A; Adalysis labels/tags A).
- Commerce depth: shopping/PMax/feed machinery (Optmyzr shopping toolbox A; Adalysis PMax tools A).

### L3 — Vendor-specific (kept out of the final document)

Marin: MarinOne/Ascend/Connect packaging, Dimensions, Insights with estimated impact, Publisher Account Linking Wizard, held-status change model naming, publisher coverage table vs named competitors. Optmyzr: Rule Engine, PPC Investigator, One-Click Optimizations, Blueprints, Sidekick, weather-based bids, "461,000+ accounts". Adalysis: Budget Groups, Daily Stop, auto-resolve, Performance Analyzer naming, "100+ prebuilt checks", Looker Studio commitment, MCP server. Skai: Celeste AI, Data Hub, "300+ publishers", commerce framing. WordStream: (unreached) "20-Minute Work Week" concept known from memory only — not used as evidence.

### Historical / Market-Sample Check

- 2000s-era bid-management platforms (the founding generation of this category, incl. Marin and Kenshoo's original form) were bid-and-reporting layers across engines — they satisfy the L0 triple (linked accounts, bid/budget controls, performance data) without necessarily rich structure editing → confirms structure editing belongs in L1, not L0.
- Regional engines (Yahoo Japan, Qihoo 360) appear as supported publishers (Marin A) → multi-engine is a variant; Google+Microsoft is the common case, not the definition.
- Engine-native tools (Google Ads Editor; engine automated rules/scripts) are excluded by invariant 1: they are the engine's own tools for its own accounts, not a third-party layer. Third-party products themselves position against exactly this distinction (Adalysis comparison pages A).
- Therefore the definition holds across eras and regions; it is not overfit to the current four-product sample.

## Rejected Findings

- "SEM management = keyword research" — rejected: keyword research/expansion is a supporting capability; a research-only product (the separate Keyword Research Application leaf) never writes campaigns back to engines.
- "SEM management = bid automation only" — rejected for the modern Type: all sampled products are broader workbenches; bid-only heritage noted under the historical check.
- "The platform is the system of record for campaigns" — rejected: engines keep billing, serving, editorial review; platform edits are staged and written back (Marin evidence A).
- "Cross-channel = same Type renamed" — rejected as a definition change: cross-channel scope is a variant axis (L2); the search-auction management core persists. Taxonomy risk recorded below.

## Boundary Findings

| vs Type | Distinction | Test |
|---|---|---|
| SEO Platform | organic ranking optimization vs paid placement management | no bids/budgets/write-back to ad accounts → SEO |
| Advertising Campaign Management (generic, §06 sibling) | potential umbrella: sampled SEM products increasingly span social + retail media | if "management of paid campaigns across channels" is the generic core, this leaf is its search slice — joint review flagged |
| DSP / Programmatic Advertising Platform | buys exchange inventory in real-time auctions on third-party inventory vs operates keyword-triggered auctions on the engines' own platforms | buying on exchanges = DSP; operating linked engine accounts = this Type |
| Ad Server / Ad Delivery | serving/tracking ad creatives vs managing campaigns in engine accounts | serves impressions = ad server; manages engine accounts = this Type |
| Media Buying Platform | broader negotiation/planning of media across channels (incl. offline) vs the search-auction management slice | no engine-account write-back = media buying/planning |
| Marketing Analytics / Attribution | measurement-only layer vs management layer with write-back | no campaign write-back = analytics |
| Keyword Research Application | research tool vs management layer | no account linkage/write-back = research |
| Engine-native editors (Google Ads Editor class) | engine's own free bulk-edit tool for its own accounts vs third-party standing layer | first-party + single-engine = not this Type (vendor comparison evidence A) |

Remove-the-invariant tests: remove engine-account linkage → analytics/SEO/research; remove write-back → read-only reporting; remove performance feedback → blind editor; remove search-engine specificity (keyword auctions) → generic Advertising Campaign Management.

## Uncertainties

- WordStream (SMB guided-advice pole) unreachable (403 ×2): the SMB-governed-experience variant is under-evidenced; the final document avoids precise claims about guided-SMB machinery.
- Skai observed at positioning depth only; search-module operational detail not fetched → Skai evidence used for scope/packaging variants, not workflow claims.
- Google Ads Editor's own documentation not fetched (timeout); the engine-native boundary rests on third-party comparison pages (biased source) plus structural reasoning → kept qualified.
- Engine-API mechanics (OAuth scopes, sync cadence) observed only via product docs (linking wizards, data-refresh docs); no engine-side documentation consulted.
- Exact pricing/limits/refresh intervals deliberately not stated (precision not researched).

## Final Synthesis

The Type is a standing third-party management layer over search-engine ad accounts: link the engines' accounts, manage their campaign spend controls from one workspace, watch consolidated performance flow back, and optimize on a repeat cadence — with rules/automation, audits, budget/bid machinery, bulk operations, and agency-scale reporting as the mature structure, and channel breadth (social/retail media) as the dominant variant. The engine stays the system of record; the platform's value is consolidation, automation, and cadence across accounts and engines. This yields the final document's defining core (three properties) and standard capabilities as summarized in the L0/L1 sections above.
