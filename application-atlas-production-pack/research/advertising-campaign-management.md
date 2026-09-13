# Research Notes — Advertising Campaign Management

Research date: 2026-09-06
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand what an "Advertising Campaign Management" application actually is from real products: what the central objects are, how campaigns are defined and launched, how spend is controlled, how delivery is monitored and adjusted, and where the Type's boundary sits against the many neighboring advertising leaves in directory section 06 (SEM Management, Media Buying, DSP, SSP, Programmatic, Ad Server, Ad Delivery, Creative Management, DCO, DMP, Audience Management, Marketing Campaign Management).

## Initial Boundary (hypothesis before research)

- Core use: advertisers/agencies define, launch, monitor, and adjust **paid advertising campaigns** — the campaign is the central managed object (budget, schedule, targeting, creatives) running on real advertising inventory.
- Likely two embodiments: (a) the native console of an ad platform (the platform's own buying interface), (b) third-party management layers that operate campaigns on external publisher platforms via APIs.
- Nearest neighbors: Search Engine Marketing Management Platform (channel-specific?), DSP (programmatic buying), Ad Server (delivery side), Media Buying Platform (planning/negotiation), Marketing Campaign Management Platform (broader marketing programs), Creative Management Platform (creative production).
- Unknowns: whether the market treats this as its own category or only as a function of ad platforms; how deep the planning layer goes; exact hierarchy variants.

## Research Questions

1. What does a "campaign" bind together in each product (creative, targeting, budget, schedule, objective)?
2. What is the canonical hierarchy (campaign → ad group / ad set → ad; anything above or below)?
3. How do objectives/goals shape configuration and delivery optimization?
4. How is spend controlled (budget types, pacing, bids, bid strategies)?
5. How is delivery/outcome data reported back, and what does the adjustment loop look like?
6. How do third-party management tools differ from native consoles (account linking, cross-channel views, automation, approval gates)?
7. What states and rules matter (ad review, account holds, eligibility, immutable settings)?
8. Where exactly is the line to DSP, Ad Server, Media Buying, Creative Management, and Marketing Campaign Management?

## Representative Products

Selected for market representation + documentation reachability + different philosophies + different customer tiers:

| Product | Kind | Tier / philosophy |
|---|---|---|
| Amazon Ads (advertising console / Campaign Manager) | native platform console | retail media + search; self-service sellers/vendors; eligibility-driven |
| LinkedIn Campaign Manager | native platform console | B2B social; objective-driven ad sets; formal hierarchy |
| Skai (formerly Kenshoo) | third-party cross-channel platform | enterprise brands/agencies; omnichannel planning + activation across 300+ publishers |
| Optmyzr | third-party agency-tier PPC tool | agencies/freelancers/in-house; monitoring, rules, budget/bid protection on top of ad platforms |
| Marin (MarinOne) | third-party cross-channel platform | enterprise/agencies; Connect/Ascend/One packaging; paid search/social/retail media/app |

Google Ads and Meta Ads Manager were intended as primary native samples but their official domains were unreachable from the research environment (see Source-access Limitation). They appear in this research only as publisher platforms referenced by the third-party tools' official pages.

## Sources

Evidence layers: A = directly observed on official product/help pages; B = cross-product commonality; C = canonical inference.

Fetched successfully (Layer A):

- Amazon Ads — homepage FAQ, Sponsored ads product page, "A new advertiser's guide to Sponsored Products success" (advertising.amazon.com) — 2026-09-06
- LinkedIn Marketing Solutions Help — help root, "Understanding settings for ad sets in Campaign Manager" (a423332), "Ads under review" (a421048), plus "About Campaigns" (a424035) surfaced in-page (linkedin.com/help/lms) — 2026-09-06
- Skai — homepage and Omnichannel Media Planning page (skai.io) — 2026-09-06
- Optmyzr — homepage and Budget Management solutions page (optmyzr.com) — 2026-09-06
- Marin — homepage (marinsoftware.com, post-acquisition state) — 2026-09-06

Failed / abandoned (per network rules, 1–2 attempts each):

- support.google.com/google-ads — timed out twice
- developers.google.com/google-ads/api — timed out
- facebook.com/business (Meta Business Help) — transport error twice
- help.pinterest.com — timed out
- ads.tiktok.com — timed out
- advertising.amazon.com/library/guides (index path) — 404 (root and article paths worked)

## Product Observations

### Amazon Ads (native console — retail media / search) [Layer A]

From the homepage FAQ, Sponsored ads page, and the new-advertiser guide:

- Sponsored ads are "run through the Amazon Ads console and Amazon Ads API"; sellers access them via the "Advertising" tab in Seller Central → "Campaign Manager" → "Create campaign".
- Campaign creation steps (guide, verbatim structure): pick your products → give your campaign a name → set the budget (daily; "Just $10 a day" suggested) → choose your duration (start immediately, optionally no end date) → select your targeting type (automatic targeting targets relevant keywords and products) → choose your bid (CPC) and launch.
- Campaign = named container binding products + budget + duration + targeting + bid.
- Charging: cost-per-click; "You bid the maximum amount that you're willing to pay when a shopper clicks an ad"; Sponsored Brands also supports vCPM.
- Reporting: "The advertising console provides reporting tools that track sales, monitor campaign metrics... You can view performance by campaign, keyword, or product to help optimize your ad spend."
- Eligibility rules: active professional seller/vendor account, eligible categories, products must be in stock and present the featured offer or the ad will not display.
- Optimization: "Amazon's first-party signals and machine learning to make faster and more accurate optimizations and recommendations... when you set up and launch your campaigns."
- Tiering: sponsored ads are self-service; display/video/Amazon DSP can be managed independently or via an account executive (managed service, minimum spend stated on the FAQ page).
- Product suite: Sponsored Products, Sponsored Brands, Sponsored Display, Brand Stores, Sponsored Products across retailers.

### LinkedIn Campaign Manager (native console — B2B social) [Layer A]

From LinkedIn Marketing Solutions Help articles:

- Hierarchy: "Ads Accounts, Campaign Groups, and Campaigns" + ad sets inside campaigns + ads. (Help root shortcuts name all levels.)
- Ad set settings determine "who your ad is displayed to, where your ad is displayed, how much your ad set spends, and when your ad set runs" (audience, placement, budget, schedule).
- Objective-first configuration: "The first step when you select your ad set settings is to choose a marketing objective... Ad sets are optimized for delivery to people most likely to take the action you want based on the objective you select. Each objective offers ad formats and bidding strategies that align with the goals of that objective."
- Ad set settings enumerated: Objective, Audience, Ad format (flexible ads to mix formats), URL tracking parameters, Placement (e.g., LinkedIn Audience Network), Budget and schedule (bid type determines charging; budget determines spend; schedule determines when), Conversion tracking.
- Campaign semantics ("About Campaigns" article): ad sets in the same campaign share objective type, bidding strategy, optimization goal, and (with Dynamic Group Budget) daily/lifetime budget and schedule; a campaign provides shared objective, shared budget/schedule, status management of its ad sets, and aggregated performance metrics.
- Rules: "The objective and ad format can't be changed after the ad set is launched"; changing the objective resets already-selected settings.
- Ad review state machine: "new ad sets (and changes to existing ad sets) will not run live until the associated ad or Lead Gen Form is approved through our ad review process"; review "usually within 24 hours"; rejected ads get a reason and an appeal path; ad status visible in the Ads tab.
- Account-level states: ad account can be put "On hold" (commonly billing issues); "ads won't run while the account is on hold but will resume once the hold is removed."
- Payments: credit card receipts, coupon codes/advertising credits converted to account currency.

### Skai (third-party cross-channel platform) [Layer A]

From skai.io homepage and Omnichannel Media Planning page:

- Positioning: "AI-Powered Commerce Media Platform"; "omnichannel platform helps brands centralize their media data, activate across channels, and measure what works"; 300+ publishers; 8,200+ brands.
- Media modules: Omnichannel Planning, Retail Media, Search, Social; plus Data & Insights (Data Centralization, Digital Shelf, Retail Insights, Content Optimization, Celeste AI) and Commerce modules (Ticketing Automation, Revenue Recovery).
- Connected publishers shown: Facebook/Meta, Google, Walmart, Target, Kroger, GoPuff, TikTok, Microsoft, LinkedIn, Instacart, Sam's Club, Amazon.
- Planning layer: "one command center"; "Unified view of spend and performance across channels"; "Drill down by region, campaign, brand, or product line"; "Centralized media plans... keeps budgets, goals, and pacing in sync"; "Track planned vs. actual spend"; "autofill from past performance"; "Simulate cross-channel budget scenarios"; "Forecast revenue, conversions, and ROI"; "Reallocate spend".
- FAQ self-description: "Comprehensive Campaign Management — oversee all their paid advertising campaigns from a centralized location... manage budgets, bids, and performance metrics"; "Scalable Automation and Optimization — algorithmic bidding, automated reporting, and custom optimization algorithms."
- Case-study evidence of DSP coverage: "Skai capabilities for Amazon DSP" (PepsiCo case study).

### Optmyzr (third-party agency-tier PPC tool) [Layer A]

From optmyzr.com homepage and Budget Management page:

- Positioning: "PPC Management Software"; "Worry-free account management for the AI and automation era of PPC"; platforms supported: Google Ads, Microsoft Ads, Amazon Ads, Meta Ads, LinkedIn Ads.
- Onboarding model: "Sign up and connect an ad account" → audit → optimize via Rule Engine or other tools. 461,000+ ad accounts connected; $5.37B ad spend managed (self-reported).
- Monitoring: "Real-Time Campaign Monitoring... monitors your accounts and lets you know when intervention is needed"; "Guardrails to prevent overspending and wastage"; alerts delivered via Email, Slack, Microsoft Teams.
- Budget machinery: "Monitor Budget Pacing throughout the month and create rules to change budgets on automation"; "automatically pause campaigns once their monthly budgets are hit and reenable them next month"; spend projections "based on account history, seasonality, and recent budget changes"; reallocation "based on spend potential... impression share lost due to budget, and structural limits"; change limits (e.g., a 20% limit keeps a $100 budget between $80 and $120 — product-specific detail); "Recent Changes Summary" panel showing every budget change in the last 7 days with trigger attribution.
- Bidding: supports manual bidding, enhanced CPC, Target CPA, Target ROAS, Maximize Conversions, Maximize Conversion Value; "layer on top of Google's smart bidding algorithms"; bid adjustments (geo, audience, device).
- One-click optimizations: "make changes without ever opening the ad platform UI" — update ad text, product feeds, campaign settings; target new keywords.
- Approval posture: "No changes without your approval, ever"; "Optmyzr only applies changes to platforms based on the suggestions you select."
- Reporting: templates, scheduled delivery, interactive links; audits ("bird's eye view of account health"); Cause Charts; PPC Investigator; N-Gram analysis; Auction Insights Visualizer.
- Audience: PPC agencies, freelancers, in-house marketers, enterprise teams (>$500K/month spend tier).

### Marin / MarinOne (third-party cross-channel platform) [Layer A, limited]

From marinsoftware.com (site now largely an acquisition-announcement page; navigation structure still visible):

- Solutions: Connect ("Collect, understand, and share marketing data"), Ascend ("Maximize results across ad platforms"), One ("Automate and manage ad platforms at scale"), Managed Services, Marin for Agencies.
- Channels: Paid Search, Paid Social, Retail Media, App Advertising.
- Positioning post-acquisition: "AI that plans, optimizes, and learns with every campaign" (Predict / Automate / Prove).
- Evidence depth limited by the site's current state; used only to confirm the third-party cross-channel category shape, not for structural claims.

## Cross-product Comparison

| Dimension | Amazon Ads console | LinkedIn Campaign Manager | Skai | Optmyzr | Marin |
|---|---|---|---|---|---|
| Campaign as central object | Yes (Campaign Manager; named container) | Yes (campaign + ad sets) | Yes ("oversee all their paid advertising campaigns from a centralized location") | Yes (campaigns/accounts monitored & optimized) | Yes (campaigns across ad platforms) |
| Hierarchy | campaign → (ad groups/keywords per ad product) | account → campaign group → campaign → ad set → ad | publisher-native hierarchy mirrored cross-platform | mirrors linked platforms' hierarchies | mirrors ad platforms |
| Objective model | targeting-type-first (automatic/keyword/product) | objective-first (drives formats, bidding, optimization) | goal/KPI-driven planning layer | KPI-driven (ROAS/CPA targets) | goal-driven (Predict/Automate) |
| Targeting | keywords, products, automatic | audience, placement, format | cross-channel audiences | keywords, placements, audiences, PMax targets | channel-native |
| Budget/bid | daily budget + CPC bid; vCPM option | bid type + budget + schedule per ad set; shared campaign budget | budgets, bids, pacing across channels; algorithmic bidding | pacing, projections, reallocation, change limits; bid strategies incl. smart-bidding layering | budgets/bids at scale, automation |
| Reporting | by campaign, keyword, product | per ad set/campaign/account; status views | unified cross-channel spend & performance; drill by region/campaign/brand/product | dashboards, audits, scheduled reports | cross-platform reporting |
| Automation | platform ML recommendations | delivery optimization per objective | algorithmic bidding, custom optimization algorithms | rule engine, alerts, auto-pause/enable, approval-gated | always-on optimization |
| Multi-account | per seller/vendor account | per ad account (+ campaign groups) | many publisher accounts, one login | many linked accounts, agency portfolio | agency/client accounts |
| Execution locus | platform's own auction | platform's own auction | external publishers via integrations | external platforms via linked accounts | external ad platforms |
| Ad review states | eligibility rules (featured offer, stock) | review → approved/rejected; account hold | n/a (delegates to publishers) | n/a (delegates) | n/a (delegates) |

Layer B commonalities (across the whole sample): campaign as named bounded object; budget as enforced constraint; targeting configuration; delivery/performance reporting attributed to the campaign; an adjust-and-relaunch loop; multi-level organization of ads under campaigns; automation layered over delivery.

Layer C canonical inference: the Type is the advertiser-side campaign lifecycle application; the native-vs-third-party difference is an execution-locus posture, not a different structure.

## Canonical Abstraction Hierarchy

### L0 — Defining Invariant

An Advertising Campaign Management application is an advertiser-side application in which:

1. **The advertising campaign is the central managed object** — a named, bounded advertising effort that binds together what is promoted (ads/creatives or products), who/where it is shown (targeting/placement), how much may be spent (budget), and when it runs (schedule).
2. **Campaigns launch onto real advertising inventory** — the campaign is not merely a plan; it executes on actual ad delivery (the platform's own auction or an external publisher's), under the application's control.
3. **Spend is a first-class enforced constraint** — budget (and typically per-interaction bids) is part of the campaign definition and the delivery system respects it.
4. **Delivery and outcomes are observable against the campaign** — spend, delivery volume, and outcome metrics are reported back attributed to the campaign, enabling the monitor → adjust → re-run loop.

Remove any of these and the product stops being advertising campaign management: no campaign object → generic ad analytics or media planning; no real delivery → media planning/forecasting tool; no spend enforcement → creative or audience tooling; no delivery feedback → a campaign *builder* only, not management.

### L1 — Common Mature Structure

- **Hierarchy** — ads organized under campaigns via an intermediate grouping level (ad group / ad set); optional higher grouping (campaign groups / portfolios / account trees).
- **Objectives** — a goal selection that constrains available formats, bidding strategies, and delivery optimization (objective-first in some products; targeting-type-first or absent in others).
- **Targeting machinery** — keywords, audiences, placements, geo/device, product/catalog targeting.
- **Bidding strategies** — manual per-interaction bids through automated target-CPA/target-ROAS/maximize-conversion strategies; bid adjustments.
- **Budget machinery** — daily/lifetime budgets, pacing, shared budgets, budget status and spend projections.
- **Performance reporting** — impressions, clicks, spend, conversions, efficiency metrics (CPA/ROAS), breakdowns by campaign/ad/keyword/product, exports.
- **Ad review / approval states** — on native platforms, new or edited ads pass a review gate before running; rejected ads carry reasons and appeal paths.
- **Multi-account operation** — account linking (third-party tools) or account trees/manager accounts (native); agency-style portfolio management.
- **Automation** — rules engines, alerts, scheduled actions, algorithmic bidding; increasingly approval-gated.
- **Change history / audit trail** — who changed what and when.
- **Organization aids** — labels, saved views/filters, naming conventions.

### L2 — Variant / Optional Structure

- **Execution locus** — native console (platform runs its own auction and delivery) vs third-party management layer (operates campaigns on external publishers via APIs/linked accounts).
- **Channel scope** — single-channel (search-only, social-only, retail-media-only) vs cross-channel command center.
- **Planning layer** — media plans, planned-vs-actual tracking, cross-channel budget scenario simulation, forecasting (present in enterprise third-party platforms; absent in basic consoles).
- **Retail-media specifics** — product catalogs/feeds, per-product eligibility (stock, featured-offer), ASIN-level reporting.
- **Creative tooling depth** — ad variation generation and creative testing inside the console; deeper production belongs to Creative Management Platforms.
- **Billing/commerce** — payment methods, credits/coupons, invoicing, account-hold states.
- **AI assistance** — recommendations, projections, natural-language assistants, agentic operation.
- **Managed-service tier** — platform-run campaign management with spend minimums (e.g., Amazon account-executive model).
- **Team/agency features** — client portfolios, white-label reporting, role-based access.

### L3 — Vendor-specific (research notes only)

- LinkedIn: Campaign Groups; Dynamic Group Budget; objective and ad format immutable after ad-set launch; 24-hour review expectation; account "On hold" state with red banner.
- Amazon: featured-offer eligibility; Seller Central "Advertising" tab entry; "$10 a day" starter suggestion; Sponsored Brands vCPM; managed-service minimum spend.
- Optmyzr: Rule Engine; Budget Control Center; percentage change limits (20% example); Recent Changes Summary (7-day window); PPC Investigator; Cause Charts; "no changes without approval" posture; MCP/AI Sidekick.
- Skai: Celeste AI; Data Hub; Digital Shelf; Ticketing Automation; Revenue Recovery (commerce modules beyond campaign management); 300+ publisher integrations.
- Marin: Connect/Ascend/One packaging; post-acquisition AI-first repositioning.

## Historical / Market-Sample Check

- Early search-ad consoles (AdWords-era pattern: campaign → ad group → keyword → ad, daily budget, CPC bid, basic reporting) satisfy the L0 fully — campaign object, real delivery, spend enforcement, campaign-attributed reporting. The objective-driven model (LinkedIn/Meta style) is a modern addition, not a requirement — Amazon's Sponsored Products campaigns configure targeting type rather than a marketing objective.
- Regional platform consoles (Baidu PPC, Yandex Direct, Criteo-style retail consoles) follow the same campaign/budget/bid/reporting shape; nothing in L0 assumes a specific region, currency, or channel.
- Therefore L0 is written channel-agnostic and objective-agnostic. Objectives, hierarchy depth, and automation depth are L1; execution locus and planning depth are L2.

## Vendor-specific Findings

See L3 above. None promoted to the canonical model.

## Boundary Findings

1. **vs Search Engine Marketing Management Platform** — SEM management is the search-channel-specific embodiment of this Type (keywords, search terms, bids as the core machinery). The generic Type spans all paid channels. Probable Variant relationship; flag for joint review when that leaf is processed.
2. **vs Demand-side Platform / DSP** — a DSP buys impressions in real time through exchanges/SSPs with its own bid engine; campaign management operates campaigns on publisher platforms (or is the publisher's own buying console). Overlap is real (Skai manages Amazon DSP; modern DSPs expose campaign objects), so the boundary is a gradient: impression-level real-time buying machinery vs campaign-level lifecycle management. DSP deserves its own research pass.
3. **vs Ad Server / Ad Delivery Platform** — opposite side of the market: delivery-side selection/serving engine (publisher-operated) vs advertiser-side campaign lifecycle. (STATUS already records the ad-server/ad-delivery-platform alias.)
4. **vs Media Buying Platform** — media buying centers on planning/negotiating media purchases (upfronts, IOs, programmatic deals); campaign management centers on the operational campaign lifecycle. The planning layer of enterprise tools (Skai media plans) overlaps; the boundary is planning/negotiation vs execution/optimization.
5. **vs Marketing Campaign Management Platform** — broader marketing programs across owned/earned/paid channels (email, organic social, web experiences); paid ads are one channel there, whereas the ad campaign is the core object here. Different central object → different Type.
6. **vs Creative Management Platform / DCO** — creative production at scale vs campaign lifecycle; campaign management binds creatives into campaigns but does not produce them at scale.
7. **vs Social Media Management Platform** — organic publishing/community first with paid boosting secondary; campaign management is paid-first with spend/bid machinery.
8. **Native console vs third-party tool** — same core objects and loop; differs by execution locus (own auction vs external publishers via linked accounts) and by who bears review/eligibility states (native) vs delegates them (third-party). Posture, not separate Types.

## Uncertainties

- Google Ads and Meta Ads Manager official documentation was unreachable; their campaign structures are known here only through third-party official pages (Optmyzr/Skai references to Google Ads features such as Performance Max, smart bidding, RSAs). Claims about those two products are kept generic and are not load-bearing for L0.
- Exact numeric limits (budget minimums, bid floors, review windows, account limits) were not asserted beyond directly observed product-specific examples (LinkedIn 24-hour review expectation; Amazon $10/day suggestion; Optmyzr 20% change-limit example) — all kept product-specific.
- The relative market weight of native consoles vs third-party tools within the Type was not quantified; both are treated as first-class embodiments.
- Marin's structural detail is limited by its current post-acquisition website state.

## Final Synthesis

Advertising Campaign Management is the advertiser-side application type whose world is organized around the campaign: a named, bounded advertising effort binding creatives, targeting, budget, and schedule; launched onto real advertising inventory under enforced spend controls; observed through campaign-attributed delivery and outcome data; and adjusted in a continuous monitor → optimize → re-run loop. Mature products add hierarchy, objectives, bidding strategies, budget machinery, review states, multi-account operation, automation, and audit trails. The type splits by execution locus (native platform consoles vs third-party cross-channel management layers) and by channel scope, but both embodiments share the same core model. The planning layer (media plans, forecasting, cross-channel budget allocation) is an optional strategic extension, not the definition.
