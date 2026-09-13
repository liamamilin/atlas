# Research Notes — Creator Affiliate Dashboard

Research date: 2026-09-07

## Research Goal

Understand the creator-side (affiliate-side / publisher-side) application through which a content creator participates in affiliate monetization: joining programs, generating trackable links and placements, seeing which audience actions earned commissions, and getting paid. Produce a vendor-neutral Application Document that explains the Type's core structure, workflow, surfaces, rules, and boundaries.

## Initial Boundary

Working hypothesis at start:

- The Type is the **creator-facing counterpart** of the affiliate domain. The directory already contains brand-side leaves (Affiliate Management Platform, Affiliate Network, Influencer Campaign Management, Influencer Marketing Platform — section 06) and creator-economy neighbors (Creator CRM, Creator Sponsorship Management, Creator Storefront, Creator Revenue Management, Creator Audience Analytics — section 27).
- "Creator Affiliate Dashboard" most plausibly means: the application where a creator who is an **affiliate** (earns commission from promoting other parties' products) manages that side of their business. Not a tool for running a brand's affiliate program, and not a tool for selling the creator's own products.
- Naming risk: "dashboard" names a **surface**, not a platform. In the real market the creator-facing affiliate experience is delivered as (a) the partner-side of affiliate networks/platforms, (b) merchant-run affiliate program dashboards, (c) creator-first commerce platforms, (d) cross-network affiliate analytics layers. Whether this is a fully independent Type or a side/pole of the affiliate domain is a taxonomy question — recorded in Boundary Findings and STATUS.md.
- Easy confusions to resolve: Affiliate Network (two-sided marketplace), Affiliate Management Platform (brand-side), Creator Storefront (shopper-facing surface), Creator Revenue Management (own-product/membership/tip revenue), Link-in-Bio Platform (link aggregation), Creator Audience Analytics (audience metrics, not commerce attribution).

## Research Questions

1. What objects exist in the creator's affiliate world? (programs/partnerships, links, placements, storefronts, clicks, conversions, commissions, payouts)
2. How does a creator join monetization programs? (open enrollment, application/review, marketplace, invitation, pre-approval)
3. How are trackable assets created? (link builders, extensions, deep links, storefronts/collections/idea lists)
4. What performance data returns, at what granularity? (clicks, orders, conversion rate, EPC, per-link/per-page/per-program)
5. What is the commission record lifecycle? (pending → confirmed/locked → paid; reversals, refunds, declined)
6. How do payouts work? (methods, thresholds, schedules, payment history, tax)
7. What is creator-specific vs generic-affiliate? (storefronts, campaigns, gifting/seeding, boosted commissions, brand relationships)
8. Where does the Type end? (vs network, brand-side management, storefront, analytics, link-in-bio)

## Representative Products

Selected for market coverage + different product philosophies + different customer levels + documentation accessibility:

| Product | Pole | Why selected |
|---|---|---|
| **Amazon Associates** (+ Amazon Influencer Program) | merchant-operated classic affiliate program, creator-agnostic | the archetype of the affiliate dashboard; excellent official docs; includes a creator-specific storefront variant for the historical check |
| **Impact.com (partner side)** | network / partnership platform partner dashboard | modern partner-side experience: marketplace, applications, links, finance widgets, creator+affiliate personas |
| **LTK** (formerly rewardStyle / LIKEtoKNOW.it) | creator-first curated affiliate commerce platform | the creator-economy pole: invite/application-based community, personalized Shop, shoppable links |
| **Affilimate** | cross-network affiliate data/analytics layer for content publishers/creators | the aggregation/analytics pole: unifies 100+ networks, commission lifecycle, page/link-level attribution |

Rejected as samples: ShareASale/Awin (redundant with the network pole given Impact coverage; time budget), MagicLinks (video-creator niche, not fetched), Geniuslink/Lasso/Pretty Links (affiliate link-management utilities — adjacent, not fetched; market context only, unverified). ShopMy was intended as a second creator-commerce sample but the domain was unreachable (transport errors ×2) — abandoned per network-restriction rule; market context only, no claims.

## Sources

All fetched 2026-09-07.

### Amazon Associates (affiliate-program.amazon.com)

- Root / program overview: https://affiliate-program.amazon.com/ — program framing ("helps content creators, publishers and bloggers monetize their traffic"), customized linking tools, commission structure ("up to 10%" by category), payment timing statement ("approximately 60 days after the end of the month in which it was earned"), sign-up → review → approval flow, Influencer Program pointer.
- Help home: https://affiliate-program.amazon.com/help — Associates Central nav directly observed: **Home / Tools / Commission Income Statement / Reports / Creator University / Help**; help categories: Getting Started (incl. Application Review Process, Tax Interview, Appropriate Conduct, identification requirement), About your account, About commissions and Payments, About Links, Tools and Features, About Reporting, Amazon Influencer Program, Operating Agreement.
- About Reporting: https://affiliate-program.amazon.com/help/node/topic/G37BNSA75FNE9HF4 — report types: Consolidated Summary of Earnings, Earnings Report, Order Report, Link-Type Report; downloads (tab-delimited), custom reports via XML; refund/return semantics; negative numbers in earnings reports.
- Amazon Influencer Program: https://affiliate-program.amazon.com/help/node/topic/GRQNGNJP89KNPBAG — Influencer page/storefront with Idea Lists, product comments, image uploads, vanity URL, categorization, follower discovery, single-product links, Amazon Live, storefront video uploads, "Earning Onsite Commissions", "onamz" Store ID inside Associates Central, identification-as-Associate requirement, Instagram single-link guidance.
- About commissions and Payments: https://affiliate-program.amazon.com/help/node/topic/GFGFAFN33TYZCXTE — commission qualification/calculation, attribution window topic ("How long do visitors have to add an item to their Shopping Cart after clicking…"), personal-use deduction, negative account balance, payment methods, Payment Threshold Settings, payment schedule topics ("When Will I Get Paid?", payment history), tax interview topics (1099, withholding, W-8/W-9 equivalents, non-US persons).
- Note: individual help-topic bodies beyond category listings largely require sign-in; assertions kept to what the fetched pages directly show.
- Amazon Influencer Program landing page https://affiliate-program.amazon.com/influencers returned an empty JS shell — no content.

### Impact.com (partner side)

- Main site: https://impact.com/ — platform framing (partnership management: Discover & Recruit, Contract & Pay, Track, Engage, Protect & Monitor, Optimize); publisher/creator-side pages listed (Affiliates, Influencers and creators); partner sign-up flow exists (app.impact.com).
- Help center (GitBook, queried 2026-09-07 via https://help.impact.com/readme.md?ask=…):
  - Partner Dashboard & Widgets: Home dashboard widgets — Brand Application status (In Review / Approved / Declined), Tasks / To Do List, **Create A Link** (short/vanity tracked links), My Social Accounts, **Boosted Product Widget** (product boost campaigns with higher-than-default commission), **Finance Widget** (daily earnings, pending payouts, current balance), **Snapshot** (performance over date range; **creator/affiliate persona toggle**); marketplace opportunities ("Find Your Next Campaign", "Brands To Work With Instantly").
  - Marketplace & applications: partner must first be approved to the **impact.com Marketplace** (terms, tax info for non-US partners, profile enhancement, add/verify promotional channels, submit); status In Review → Approved/Declined; then Discover → Find Brands → All Brands → brand tile → Apply; review brand contract terms; answer attached survey; pre-approved partners may apply to multiple brands (documented as **up to 10 at once**); pending status shown as clock → checkmark when accepted; brand insights include **earnings-per-click and application response/acceptance rates**; "I'm a creator" onboarding steps exist (polish profile → apply to affiliate programs); Chrome extension exists for applying to programs and creating/managing links.
  - Partner payments: withdraw to **bank account or PayPal**; action lifecycle **Pending → Locked → Clearing** (payout possible) with **Overdue** (brand unfunded) and **Reversed** (action cost voided); brand balance check gates payout; partner-side gates (bank + tax requirements; dashboard banners when unmet); **AutoPay** by balance threshold or fixed day (documented: 1st/15th; eligibility checks documented as Tuesdays/Thursdays; **minimum threshold documented as USD $10**); bank-detail changes pause payouts (documented 48h for certain changes); compliance review of new bank details can delay a couple of days.
- One ask query (partner reporting detail) timed out twice; reporting understood from widget/report pages surfaced in sources (e.g., Campaign Dashboard Report for Partners exists).

### LTK

- Consumer/product site: https://www.ltk.com/ — LTK app framing; "over 450 million products, 8,000 brands, hundreds of thousands of global Creators" (marketing claims — vendor figures, not asserted in final doc).
- Creator recruiting page: https://company.shopltk.com/influencers/ — application-based enrollment ("APPLY NOW"), creator eligibility signals (public social profile, high engaged following, regular content), accepted-creator benefits: **personalized LTK Shop** visible to shoppers in the LTK app, **network of over 7K retailers** (vendor figure), **tools to create shoppable links and Collections**, retargeting capabilities, growth consulting, mobile + desktop tools to create/distribute/track content, brand-partnership emphasis; login split: brand portal vs **creator portal (auth-creator.shopltk.com)**.
- Help center root: https://help.liketoknow.it/ — categories: Getting Started, My Account, Troubleshooting, Partner with Us; promoted articles incl. "How to Apply to LTK & Authenticate Your Instagram Profile", "How Do I See the Creator Version of LTK".
- Article: https://help.liketoknow.it/hc/en-us/articles/360014556934 — after acceptance: set up profile at **creator.shopltk.com**, set up LTK Shop, **post via the LTK Creator App (iOS only; Android posts from the LTK App)**, publish "looks", self-follow guidance.
- **Source-access limitation**: the creator-dashboard help center (help.rewardstyle.com) is JS-gated ("doesn't work properly without JavaScript") and its public Zendesk API returned 401. Deep creator-dashboard mechanics (earnings reports, payout settings, link tool detail) could NOT be directly observed for LTK. Assertions about LTK's dashboard internals are therefore avoided or kept weak.

### Affilimate

- Root: https://affilimate.com/ — positioning "AI commerce infrastructure for content publishers"; product pillars: **Unify** (all affiliate data from 100+ networks in one place), **Optimize** (heatmaps, offsite tracking, channel insights for editorial teams), **Amplify** (sponsorship and yield optimization campaigns); audience: news/media publishers, newsletter publishers, shopping/loyalty platforms, publisher finance teams — "and creators" appears in trust claims; sample unified commission records across networks (CJ, Skimlinks, Rakuten, Awin, Webgains, Linkby) with **amounts, statuses (Confirmed / Pending / Rejected / Paid / declined / locked), commission types (CPA, CPC, bonus)**; article-level metrics shown: clicks, CTR, revenue, sales count, GMV, EPC.
- Unify product page: https://affilimate.com/product/unify/ — connect **100+ networks without a developer** (step-by-step guides; e.g., Awin connection via Publisher ID + API Token, test connection); **multiple accounts per network**; unified partnerships/rates across networks; catch **merchant network moves, rate changes, program shutdowns**; **isolate bonus payments**, classify lines as bonus/CPA/CPC/other; custom reports + **CSV/XLSX export**; **full commission lifecycle from click → purchase → lock → payout**; role-based permissions; dashboard metrics: total earnings, earnings by day and by platform, Revenue / Orders / EPC; warehouse/BI destinations (BigQuery, Snowflake, Redshift, Power BI, Looker, Tableau, Databricks, Metabase); APIs + MCP + AI Agent ("answer earnings questions", "what is still pending payout").
- Note: Optimize/Amplify detail pages were not fetched; their capabilities are known only from nav descriptions and homepage copy — kept weak.

## Product Observations (evidence-tagged)

### Amazon Associates — Key observations

- (A) Enrollment: sign-up → application review → approval; qualifying website or mobile app required; separate **Amazon Influencer Program** for influencers with an established social following; both can coexist (help topic list shows "can I be part of Associates and the Influencer Program").
- (A) Dashboard (Associates Central) nav: Home, Tools, **Commission Income Statement**, Reports, Creator University.
- (A) Money model: commissions on qualifying purchases and programs; rates vary by product category ("up to 10%" claim on program page); payment "approximately 60 days after the end of the month in which it was earned" (program page statement).
- (A) Attribution: a dedicated help topic governs how long a visitor has after clicking to add an item to the cart and still earn commission — i.e., link-click attribution with a time window.
- (A) Commission lifecycle/exceptions: refund vs return distinction documented; negative numbers in earnings reports explained; negative account balance documented; deduction for personal use documented.
- (A) Reports: Consolidated Summary of Earnings, Earnings Report, Order Report, Link-Type Report; downloadable (tab-delimited) and custom (XML).
- (A) Payments: payment-method topics, Payment Threshold Settings, payment schedule topics, payment history, tax interview (incl. non-US persons, withholding, 1099 forms), two-factor authentication when accessing payment details.
- (A) Compliance: "Why do I have to identify myself as an Associate? How should I do this on social media?" — identification/disclosure is an explicit program requirement with help support; also policies on redirects, pop-ups, self-order restrictions (topic titles observed).
- (A) Creator variant: Influencer Program = storefront page on Amazon with Idea Lists (curated product lists), comments, images, vanity URL; onsite earning (commissions when purchases happen on Amazon surfaces like the storefront/videos/livestream); video uploads; Amazon Live; the influencer account appears inside Associates Central (Store ID "onamz…").
- (B→A) The dashboard is link/content-oriented: no shopper-facing community feed in Associates itself (contrast with LTK).

### Impact.com partner side — Key observations

- (A) Two-sided platform; partner side is a first-class product ("For Publishers: Affiliates / Influencers and creators / Mobile apps / Content publishers").
- (A) Onboarding ladder: create account → join the **Marketplace** (application with terms, tax info for non-US, profile, **add/verify promotional channels**) → apply to brands (contract terms + survey per brand; pre-approval enables batch applications, documented up to 10; invitation path also exists brand-side).
- (A) Dashboard widgets: Brand Application statuses (In Review/Approved/Declined), Tasks/To Do, Create A Link (short/vanity tracked links), My Social Accounts, Boosted Product Widget (**higher-than-default commission** campaigns), Finance Widget (daily earnings, pending payouts, current balance), Snapshot (date-range performance; **creator vs affiliate persona toggle**).
- (A) Discovery: Brands Marketplace with filters and brand insights (earnings-per-click, application response/acceptance rates); "Find Your Next Campaign"; pre-approved list.
- (A) Money: action lifecycle Pending → Locked → Clearing; Overdue/Reversed states; brand-balance gate; partner gates (bank + tax); withdrawal to bank/PayPal; AutoPay threshold-or-fixed-day; minimum threshold documented ($10); payouts blocked until requirements met (banners shown).
- (A) Tracking: TrueLink, cross-device tracking, partner-side impressions, Chrome extension for link creation; "Create and manage links" documentation family exists.
- (A) Campaign shape: brand-assigned **Tasks**, product-boost campaigns — campaign-ish structures appear on the partner side, mirroring the brand-side campaign machinery.
- (A) Multi-persona: the same account can hold creator and affiliate personas with toggleable metrics.

### LTK — Key observations

- (A) Enrollment is curated: application (with Instagram authentication) + acceptance criteria (public profile, engaged following, frequent posting). Not open enrollment — a positioning difference from Amazon/Impact.
- (A) Creator surfaces: creator profile at creator.shopltk.com; **personalized LTK Shop** (shopper-facing) inside the LTK consumer app; posting "looks" via LTK Creator App (iOS; Android posts from consumer app).
- (A) Monetization machinery: tools to create **shoppable links and Collections**; retailer/brand network; brand collaborations; retargeting of the creator's followers; growth consulting.
- (A) Community: consumer app (feed of creators' posts, search of products/creators) — the creator's affiliate storefront is embedded in a consumer-facing shopping community.
- (B, weak) Earnings tracking exists ("create, distribute, and track content", "data-driven strategy" from proprietary Brand/Shopper/Creator performance data) — but dashboard internals unverified (JS-gated help center).
- (L3 candidates, not asserted in final doc): exact commission rates, payout schedules, creator app platform restrictions.

### Affilimate — Key observations

- (A) The product is a **cross-network aggregation/analytics layer**: the publisher/creator connects each affiliate network account (publisher ID + API token), and the platform normalizes transactions, rates, and finance data into one record.
- (A) Commission records carry network, type (CPA/CPC/bonus), amount, currency, and **status** (pending/confirmed/declined/locked/paid) — the same lifecycle vocabulary networks use.
- (A) Full lifecycle view: click → purchase → lock → payout, for reconciling pending balances and discrepancies.
- (A) Attribution granularity beyond network dashboards: revenue by **page URL and link**, by traffic source, by offsite channel (newsletters, YouTube, social, syndication), heatmaps; product-level matching at portfolio scale.
- (A) Rate/program monitoring: catch merchant network moves, rate changes, program shutdowns without checking each dashboard.
- (A) Finance posture: payout/reconciliation tools for finance teams; bonus isolation; CSV/XLSX export; warehouse/BI destinations; role-based access.
- (A) AI layer: Agent + MCP to answer earnings questions ("what is still pending payout", "which merchants dropped commission rates").
- (B) Note the drift: Affilimate positions increasingly toward enterprise publishers and sponsorship campaign management (Amplify) — but Unify is squarely the affiliate dashboard/aggregation layer. It does NOT pay the creator itself (payouts happen at networks) — important for the payout question: payout processing is NOT definitional; payout visibility is.

## Cross-product Comparison

| Dimension | Amazon Associates | Impact.com partner | LTK | Affilimate |
|---|---|---|---|---|
| Who operates it | merchant (Amazon) runs its own program | network/platform (two-sided) | creator-first commerce platform | third-party analytics layer over networks |
| How creator joins | apply → review → approve | join marketplace → apply per brand (survey, terms) → approve; or invited | apply + Instagram auth; curated acceptance | connect existing network accounts (no program join — analytics only) |
| Trackable assets | link-building tools; influencer storefront (Idea Lists) | Create A Link (short/vanity), Chrome extension | shoppable links, Collections, LTK Shop | centralized linking via extension/API (plus per-network links) |
| Performance data | Earnings/Order/Link-Type reports; consolidated summary | Snapshot widget, date-range performance, campaign reports | content/shop performance (unverified detail) | unified transactions; per-page/per-link/per-channel revenue; EPC; GMV |
| Commission record lifecycle | earned → (refunds/returns → negative adjustments) → paid on schedule | Pending → Locked → Clearing → paid; Reversed/Overdue | (not directly observed) | pending/confirmed/declined/locked/paid; click→purchase→lock→payout |
| Payout machinery | payment methods, threshold settings, schedule (~60 days after month end, documented), payment history, tax interview | bank/PayPal, AutoPay threshold/fixed day, min threshold, payment gates | (not directly observed) | not payer — payout data reconciled from networks |
| Shopper-facing storefront | Influencer Program page (optional variant) | no (links only) | core: LTK Shop in consumer app | no |
| Program discovery | n/a (single program) | Brands Marketplace w/ insights | brand network + collaborations | n/a (no programs — connects networks) |
| Brand-side campaign touchpoints | (onsite earning programs) | Tasks, product-boost campaigns | brand collaborations, campaigns | sponsorship campaigns (Amplify, separate pillar) |
| Multi-network scope | single program | many brands within the network | many retailers within platform | 100+ networks unified |
| Compliance surfaces | identify-as-Associate requirement; conduct policies | contract terms per brand; promo-channel verification | (not directly observed) | (not core) |
| Personas/roles | one associate identity (influencer variant shares account) | creator vs affiliate persona toggle | creator identity in community | role-based access, multi-account/multi-property |

## Canonical Model (abstraction)

### L0 — Defining Invariant (deliberately small)

The creator affiliate dashboard exists to make "my audience's purchases earn me commissions" legible and collectable. Remove any of these and the thing stops being this Type:

1. **Creator affiliate identity under programs** — an identified affiliate/partner account standing in an enrollment relationship with one or more monetization programs (a merchant program, a network, or a platform's brand partners). Without enrollment-in-programs, it's just analytics or a link utility.
2. **Creator-attributed trackable assets** — links (or equivalent placements/storefronts) bound to the creator's identity, so that audience actions through them are attributable to this specific creator. Without creator-attributed tracking, no commission can belong to anyone.
3. **Commission records** — recorded conversion/commission events (amount, source program, status) tied to those assets. Without commission records, it's a link shortener with click stats.
4. **Earnings visibility** — a money-oriented view (pending/earned/paid balances over time) as the primary surface. Without an earnings view, it's campaign management, not an affiliate dashboard.

### L1 — Common Mature Structure

Very common in mature products, not definitional:

- Performance reporting: clicks, orders/conversions, earnings; by link, content/page, program/brand; date ranges; export
- Link creation tooling: link builders, deep links, browser extension, short/vanity links
- Payment machinery where the platform is the payer: payment methods, minimum thresholds, payout schedules, payment history; and universally, **payment/tax setup as a gate on payout**
- Program discovery & application: marketplace/directory of brands/programs with approval states (where the product hosts multiple programs)
- Brand/partnership relationship surfaces: contract terms, commission terms, tasks/campaigns, messages
- Compliance/disclosure support: identification-as-affiliate requirements
- Attribution-window semantics documented per program (click-time windows; return/refund reversal semantics)

### L2 — Variant / Optional Structure

Depends on segment/era/product family:

- Shopper-facing storefront/community surface (LTK Shop; Amazon Influencer page) — creator-first platforms expose the creator's monetized presence to consumers
- Cross-network aggregation & reconciliation as the product's whole point (Affilimate) — including rate-change monitoring, multi-account portfolios, warehouse/BI exports
- Campaign/gifting mechanics from the brand side: tasks, product seeding, boosted/higher commission campaigns
- Onsite vs offsite earning split (commissions from purchases on the platform's own surfaces vs external merchant sites)
- Multi-persona accounts (creator vs affiliate), multi-property/multi-account management, team roles
- AI assistance (earnings Q&A, anomaly/rate-change detection) — era-common
- Educational/consulting services attached to the dashboard (Creator University, growth consulting)

### L3 — Vendor-specific (research notes only)

- Amazon: ~60-days-after-month-end payment timing; category commission schedule; personal-use deduction; "onamz" Store IDs; Idea Lists; Amazon Live; SiteStripe-style on-page tooling (not verified in this pass — excluded); Associates program policies (pop-ups, redirects, self-orders).
- Impact: USD $10 minimum withdrawal threshold; AutoPay fixed days 1st/15th; AutoPay eligibility checks Tuesdays/Thursdays; 48-hour payout pause after certain bank changes; batch applications "up to 10" pre-approved brands; TrueLink; Boosted Product Widget naming; creator/affiliate persona toggle.
- LTK: 7K retailers / 450M products / 40M users (vendor figures); iOS-only LTK Creator App; Instagram authentication at application.
- Affilimate: 100+ networks claim; MCP/AI Agent; named warehouse destinations; Amplify sponsorship campaign machinery; AI Influence Exchange.

## Vendor-specific Findings

See L3 above. None of these are load-bearing for the Type. The most tempting over-generalizations, rejected:

- **"Paid ~60 days after month end"** — Amazon-specific schedule; do not generalize (Impact uses threshold/fixed-day AutoPay; networks differ).
- **"Minimum payout is $10"** — Impact-specific.
- **"Creators must apply and be accepted"** — LTK/Amazon/Impact all gate enrollment, but the *analytics-layer* variant (Affilimate) has no program enrollment at all; and some merchant programs historically accept nearly instantly. Enrollment *relationship* is definitional; *curated acceptance* is common, not definitional.
- **"Storefronts are part of the Type"** — LTK/Amazon-Influencer have them; Impact/Affilimate do not. Storefront = L2.
- **"The product pays the creator"** — only true where the platform is the payer (Amazon, Impact, LTK presumably); Affilimate deliberately does not. Payout *processing* is not definitional; payout *visibility* is part of the commission record lifecycle.

## Boundary Findings

- **vs Affiliate Network (§06)**: the network is the two-sided marketplace + tracking infrastructure (advertisers × publishers). The Creator Affiliate Dashboard is the **affiliate-side application** of that world. Diagnostic: a network's brand side manages programs; its partner side IS this Type's experience. The directory holding both is defensible only if side-of-marketplace is the distinguishing axis — recorded as a taxonomy observation.
- **vs Affiliate Management Platform (§06)**: brand-side software for operating an affiliate program (recruit partners, set contract terms, pay out). The creator dashboard is the receiving end: the same contract terms, tasks, and payouts appear from the other side. Cleanest seam: who operates the account (brand vs creator).
- **vs Influencer Campaign Management (§06)**: brand-side campaign machinery (briefs, deliverables). Creator-side echoes appear as Tasks/campaigns inside partner dashboards — but the creator Type is organized around commissions/earnings, not deliverable management.
- **vs Referral Marketing Platform (§06)**: referral programs reward *customers* of a brand for referring peers; identity is customer, reward is often store credit/discount. Affiliate dashboards serve *creators/publishers* as a professional monetization channel with cash commissions. Different user, different object model.
- **vs Creator Storefront (§27)**: the storefront is the shopper-facing selling surface; the dashboard is the creator-facing monetization surface. Bundled in creator-first platforms (LTK), optional variant elsewhere (Amazon Influencer). Remove the storefront and the Type stands; remove the commission ledger and it becomes a storefront.
- **vs Creator Revenue Management (§27)**: that Type centers the creator's own products/services/memberships/tips (revenue from audience). This Type centers commissions from third parties (revenue via audience). Different objects: subscription/tip/own-product records vs third-party commission records.
- **vs Link-in-Bio Platform (§27)**: link aggregation for social profiles; monetization optional. No program relationships, no commission records → not this Type, even when it carries affiliate links.
- **vs Creator Audience Analytics (§27) / Social Media Analytics (§06)**: audience/engagement analytics vs commerce attribution. Affilimate straddles the seam (traffic sources + commerce), but its defining objects are commission transactions, not audience metrics.
- **"去掉什么就变成另一个 Type" tests**:
  - Remove creator-attribution + commission records → link-in-bio / URL builder.
  - Remove the creator side (keep brand side) → Affiliate Management Platform.
  - Remove the affiliate/commission world, keep own-product selling → Creator Storefront / commerce.
  - Remove commission records, keep audience metrics → Creator Audience Analytics.
  - Remove the creator, keep the marketplace machinery → Affiliate Network.

### Taxonomy observation (for STATUS.md Boundary Issues)

"Creator Affiliate Dashboard" names a surface rather than a product family; in the market it is realized as the partner-side of networks, merchant program dashboards, creator-commerce platforms, and cross-network analytics layers. The leaf is best understood as **the creator-side affiliate monetization application** — the creator-side counterpart of Affiliate Management Platform / Affiliate Network. Documented as a legitimate Type on that reading; flagged as a side-of-marketplace sibling of the §06 affiliate leaves rather than a fully independent species.

## Uncertainties

1. **LTK dashboard internals unverified** — earnings reports, payout settings, and link-tool detail for LTK could not be observed (JS-gated help center; API 401). All LTK-specific dashboard claims in the final doc are kept to directly observed surfaces (apply → creator profile → Shop → links/Collections → track).
2. **Amazon Influencer Program landing page** returned an empty shell; Influencer detail comes from help-topic listings (titles + some bodies), not the marketing page.
3. **Amazon help-topic bodies** largely sit behind sign-in; category listings and a few rendered pages were used. Payment-method specifics (gift card balance option, check fee) observed only as topic titles — not asserted.
4. **Impact partner reporting granularity** (report types beyond widgets) — the dedicated ask timed out; understood from source listings (Campaign Dashboard Report for Partners) only.
5. **Affilimate Optimize/Amplify detail pages** not fetched; capabilities known from nav/home copy only — kept out of the final doc except as weak "analytics-layer" statements already supported by Unify + homepage copy.
6. Historical/regional breadth: no pre-2000 affiliate systems were sampled (the Type predates the web in door-to-door/referral forms, but the software Type is web-native). The classic-pole sample (Amazon Associates, operating since the 1990s per its own © notice) serves as the historical anchor; older regional networks (e.g., European affiliate networks) were not directly examined — the L0 was checked against them conceptually (enrollment + tracked links + commission records + earnings view all predate modern creator-economy features).
7. ShopMy (intended second creator-commerce sample) unreachable — the creator-commerce pole rests on LTK alone; its canonicality is supported by the other poles.

## Final Synthesis

The Creator Affiliate Dashboard is the **creator-side affiliate monetization application**: an identified creator account enrolled in one or more commission programs; creator-attributed trackable assets (links, and often storefronts/collections) that bind audience actions to that creator; a ledger of commission records with a provisional lifecycle (pending → confirmed/locked → paid, with reversals); and an earnings view as the primary surface. Around this core, mature products add performance reporting (by link/content/program), link-creation tooling, program discovery/application with approval states, payment machinery with tax gates (where the platform pays), brand/campaign touchpoints, and disclosure support. The market delivers the Type through four poles — merchant program dashboard, network partner dashboard, creator-first commerce platform, cross-network analytics layer — which differ in scope (one program ↔ many networks), shopper-facing surfaces, and whether they pay the creator themselves. The Type is the creator-side counterpart of the brand-side affiliate management leaves in the directory.
