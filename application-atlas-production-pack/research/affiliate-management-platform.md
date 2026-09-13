# Research Notes — Affiliate Management Platform

Research date: 2026-09-06

## Research Goal

Understand what an Affiliate Management Platform actually is as a software structure: what objects exist inside it, who operates it on which surfaces, how the merchant↔affiliate workflow flows from recruitment to payout, which states and rules govern commissions, and where its boundary lies against Affiliate Network, Referral Marketing Platform, Influencer Marketing Platform, PRM, and generic tracking/attribution tools.

## Initial Boundary

Working hypothesis before research:

- An Affiliate Management Platform is **merchant-side** (advertiser-side) software: a brand uses it to run its *own* affiliate program — recruit promoters, give them trackable links/codes, attribute referred conversions, compute commissions, and pay them.
- It is NOT the Affiliate Network itself (a multi-advertiser intermediary where publishers discover many programs), NOT a customer-referral program (participants are customers, not professional promoters), NOT influencer campaign software (content/campaign-centric rather than commission-per-conversion-centric), NOT PRM (B2B partner organizations, deal registration, channel selling).
- Suspected gray zones to verify: (a) whether representative products themselves blur into networks/marketplaces; (b) whether referral/influencer support inside these products breaks the boundary; (c) what happens when payout execution sits inside vs outside the product.

## Research Questions

1. Who operates the system day to day, and who else touches it (affiliates, finance, admins)?
2. What are the core objects: affiliate record, tracking identifier, referral/conversion, commission, payout, program/campaign container, creative asset?
3. How does the central loop work: enroll → promote → track → attribute → commission → approve → pay?
4. What lifecycle states exist for affiliates, conversions, commissions, payouts?
5. What rules actually govern behavior: attribution windows/methods, commission models, approval gates, fraud controls, refund handling, thresholds, tax/KYC?
6. What interfaces exist: merchant dashboard, affiliate portal, signup surfaces, API?
7. How do deployments vary (SaaS, self-host, plugin/native embedding)?
8. What distinguishes this Type from Affiliate Network, Referral Marketing, Influencer Marketing, PRM, and attribution tools?
9. Does the definition survive older/regional/platform-native samples (self-hosted scripts, plugins, network-connected programs)?

## Representative Products

| Product | Segment / philosophy | Why selected |
|---|---|---|
| Tapfiliate | Cloud-native SaaS, SMB/mid-market, "all-in-one but simple", white-label focus | Market-visible mid-market posture; strong marketing-page documentation of features and launch flow |
| Rewardful | Minimal Stripe-native SaaS affiliate tool, SMB | Opposite philosophy: deliberately narrow, billing-integration-first; unusually good Help Center (Tier 1) reached |
| Post Affiliate Pro | Long-lived (2004), feature-dense, integration-heavy; same vendor sells both "Affiliate Program Software" and "Affiliate Network Software" | Legacy/feature-rich pole; explicit in-house-program vs network product split inside one vendor — directly informative for the Type boundary |
| impact.com | Enterprise "partnership management platform" (affiliate + creator + referral), two-sided with publisher sign-up and vetted marketplace | Enterprise anchor; shows where the category converges at scale and how affiliate sits inside a broader partnership platform |

Rejected/adjusted sample:
- **Refersion** (e-commerce/Shopify-centric affiliate platform): both www.refersion.com and help.refersion.com returned HTTP 403 on 2026-09-06. Dropped from the sample rather than reconstructed from model memory. The e-commerce pole is still covered indirectly (Tapfiliate and Post Affiliate Pro both document Shopify/WooCommerce integrations).
- Not selected: TUNE, Affise, Everflow, PartnerStack — predominantly network-side or partner-ecosystem-side products; better treated as boundary evidence for Affiliate Network / PRM than as core samples here.

## Sources

Fetched 2026-09-06 (all Layer A unless noted):

- Tapfiliate — homepage (product/positioning): https://tapfiliate.com/
- Tapfiliate — developer docs portal (integration surfaces): https://tapfiliate.com/docs/
- Rewardful — homepage (product/positioning/FAQ): https://www.getrewardful.com/
- Rewardful — Help Center article "How do I set a minimum payout threshold?": https://help.rewardful.com/en/articles/6665058-how-do-i-set-a-minimum-payout-threshold
- Post Affiliate Pro — homepage: https://www.postaffiliatepro.com/
- Post Affiliate Pro — "Affiliate management software" page: https://www.postaffiliatepro.com/affiliate-management-software/
- impact.com — homepage / platform overview: https://impact.com/

Source-access limitation:
- No full help-center deep dives were reachable for Tapfiliate (docs portal reachable but article bodies not fetched), Post Affiliate Pro (support.qualityunit.com not fetched), or impact.com (help.impact.com not fetched). Observations for these three therefore lean on Tier-2 official product pages, which document features and flows at a coarser grain than help articles.
- Refersion unreachable (2× HTTP 403).
- Consequence: assertion strengths below are calibrated accordingly; precise operational details (exact attribution-window durations, exact payout schedules, exact fraud rule parameters) are deliberately NOT stated anywhere, because no sampled source documented them at that precision.

## Product Observations

### Tapfiliate (Layer A — official homepage + docs portal)

- Positioning: "The Affiliate Tracking Platform"; also marketed as "All-in-One Affiliate, Referral, and Influencer Program Management" (affiliate, referral, influencer, content-creator, brand-ambassador, solution-partner/reseller program types on one platform).
- Named feature pillars: Tracking and Attribution ("track clicks and conversions to measure your partner-driven revenue"); Flexible Commissions ("percentage, fixed, or tiered"; recurring commissions for SaaS, lifetime commissions, fixed/percentage for e-commerce); Real-Time Reporting (segment by geography, device, custom segments); Partner Recruitment ("automatically invite and onboard"); Automation and Workflows ("from recruit to payout"); In-platform Messenger; Affiliate Offers marketplace ("get discovered by active affiliates"); Multi-level-marketing (sub-affiliate commissions); White Label (portal, sign-up pages, custom domain).
- Documented launch flow (3 steps): 1) Connect your platform (30+ pre-built integrations: Shopify, Stripe, WooCommerce, Paddle, etc.; custom sites via JS snippet or REST API), 2) Invite your partners (branded invite links / recruitment tools), 3) tracking "attribute[s] every sale".
- Coupon tracking: unique coupon codes per creator (example "SARAH20"); if the code is used at checkout the commission is tracked — explicitly positioned for conversions "even when they don't click" (social/offline).
- Bonuses: performance bonuses triggered automatically when an affiliate hits a goal (example given: "sell 100 items → $500 bonus").
- Bulk operations: approve affiliates, change commission structures, send payouts to hundreds of partners in bulk.
- Closed programs supported (customer testimonial: invite-only program with approval control over who can promote).
- Integration surfaces from docs portal: JavaScript tracking library, REST API, web hooks, platform integrations, Zapier; support portal at support.tapfiliate.com; "Access to Partner Network" via admitad integration (network connectivity as an add-on).
- FAQ: performance-based model ("you only pay commissions after a successful sale"); monthly plans keyed to usage (clicks/conversions), no transaction fee on sales.

### Rewardful (Layer A — official homepage/FAQ + Tier-1 help article)

- Positioning: "Affiliate and referral management platform" for SaaS; "All-in-One Affiliate Management Software for SaaS"; Stripe/Paddle-native.
- How it works (as documented): connect Stripe; Rewardful "automatically track[s] recurring commissions, upgrades, downgrades, and cancellations"; two-way Stripe sync with webhook updates; last-touch attribution listed as a feature; customizable cookie; coupon-code tracking alongside links; self-service affiliate portal (links, coupon codes, earnings).
- Commission configuration: recurring or one-time; percentage or fixed; minimum payout thresholds (help article: thresholds are set at the **campaign level**; different campaigns can have different thresholds).
- Payout lifecycle (Tier-1 evidence, verbatim structure): payout statuses **Pending → Due → Processing → Paid**; Pending = commissions due by timing but affiliate below the minimum payout threshold; Due = due by timing and above threshold; Processing = system updating the underlying commissions; Paid = historical payouts already marked paid. "Rewardful does NOT automatically pay your affiliates, you must do this yourself" — merchant executes payouts, optionally via PayPal/Wise mass payment; newer "Managed Payouts" mode: merchant funds one invoice, platform distributes (bank transfer/SEPA/wire/PayPal/check), collecting tax docs and KYC automatically during onboarding.
- Refund handling: "automated refund handling" listed; FAQ says the system handles "recurring commissions, upgrades, downgrades, cancellations, refunds".
- Fraud: self-referral fraud detection listed.
- Recruitment: "Affiliate Finder" search engine that crawls the web to surface proven affiliates; FAQ explicitly contrasts it with affiliate marketplaces ("marketplaces are a passive approach... filled with low quality, poorly vetted affiliates").
- Program container: **campaign** ("setting up your first campaign typically takes under 15 minutes"; campaign-level thresholds).
- API: developer API for fully white-labeled programs (custom dashboard layout/colors/data).

### Post Affiliate Pro (Layer A — official homepage + dedicated "Affiliate management software" page)

- Positioning: "all-in-one affiliate tracking software that allows companies to launch, track, and scale their own affiliate, referral, and influencer programs. From a single dashboard, you can track clicks and conversions accurately, manage payouts, provide marketing assets to your partners" (own FAQ definition).
- Vendor's own definition of the category (on the affiliate-management page): "a dedicated platform designed to fully manage your partner marketing. It handles everything from tracking referral links and adjusting commission structures to organizing payouts and optimizing campaign performance."
- **Critical boundary evidence**: the vendor sells two distinct products — "Affiliate Program Software (create and manage affiliate programs)" and "Affiliate Network Software (set up your own affiliate network to manage merchants and affiliates)". The in-house-program mode and the network-operator mode are separate SKUs in the same family.
- Affiliate management features: organize partners into custom tiers/groups from one dashboard; multi-tier commission structures; track affiliate account balances; mass payout files; multi-currency support with automatic exchange-rate conversion; commission table depicted with "pending and approved payouts" in multiple currencies.
- Tracking: "every click attributed correctly"; tracking links, conversions, traffic sources; fraud protection feature page: "block invalid clicks, decline repeated transactions, and flag suspicious referral activities automatically".
- Promotional materials: image/HTML banners, customizable smartlinks, discount codes, delivered through the affiliate dashboard.
- Administrators: multiple administrator accounts with specific permissions and data-access levels (higher plan).
- Automation: custom automations for routine affiliate-management tasks.
- Reports: top-performing affiliates, active promotional links, program growth over custom timeframes.
- Integrations: 200+ (Shopify, WooCommerce, WordPress...), plugins, tracking scripts, API configurations; REST API v3; mobile apps for Android/iOS.
- Deployment posture: "Cloud software with free updates... We handle all server management" (current materials emphasize cloud; self-hosted licensing is part of this product's history but is NOT claimed on the fetched pages — recorded as uncertain).
- Pricing keyed to monthly tracking volume, unlimited affiliates (pricing detail — research notes only).

### impact.com (Layer A — official homepage/platform overview)

- Positioning: "All-in-One Partnership Management Platform" / "partnership management platform"; affiliate, creator/influencer, and customer-referral programs unified on one platform; two-sided (separate brand and publisher/affiliate sign-up flows; vetted marketplace "connects you with partners who have proven track records in your vertical").
- Platform pillar structure (documented): **Discover & Recruit** (find partners globally, recruitment automation); **Contract & Pay** ("choose your business outcomes, then reward the partners that drive them"; "pay at any point in the conversion funnel"; participation bonuses); **Track** (traffic partners drive "on all your properties, across any device"; tracking-mode choice; cross-device tracking; privacy posture; branded link handling); **Engage** (proactive messaging, automated partner-management workflows, creative and offer management, 40+ performance reports); **Protect & Monitor** (full-stack protection: keyword violations, promo-code misuse, fake leads/conversions, compliance/brand-safety, invalid-traffic filtering); **Optimize** (partner value evaluation, customer LTV, predictive optimization).
- Affiliate-specific claims: shows which partnerships generate revenue "not just clicks"; case-study themes include affiliate compliance automation and program growth.
- Enterprise posture: partnerships treated as a portfolio including mobile app partnerships, business development, agencies — the affiliate program is one partnership type among many.

## Cross-product Comparison

| Structure / capability | Tapfiliate | Rewardful | Post Affiliate Pro | impact.com | Evidence layer |
|---|---|---|---|---|---|
| Merchant operates its own program (brand-side administration) | Y | Y | Y ("launch your own in-house affiliate program") | Y (brands; affiliate among partnership types) | B (all four) |
| Registry of individually identified affiliates | Y (invite/recruit, bulk approve) | Y (portal accounts) | Y ("unlimited number of affiliates"; partner database) | Y (partner profiles) | B |
| Trackable per-promoter identifiers | links + coupon codes | links + coupon codes | links + smartlinks + discount codes | branded links (TrueLink) + promo-code protection | B |
| Click/conversion tracking wired into the merchant's site/checkout via integration | Y (JS snippet, REST, 30+ integrations) | Y (Stripe/Paddle sync, 20+ integrations, API) | Y (plugins, scripts, 200+ integrations, S2S) | Y (tracking on "all your properties") | B |
| Attribution of a conversion to a specific affiliate | Y ("attribute every sale") | Y (last-touch attribution listed) | Y ("every click attributed correctly") | Y (revenue attribution per partnership) | B (method itself varies per product) |
| Commission computed from configured rules | Y (%, fixed, tiered; recurring/lifetime) | Y (recurring/one-time; %/fixed) | Y (multi-tier structures; performance rewards) | Y (contract terms; "pay at any point in the conversion funnel") | B |
| Commission status lifecycle before payout | implied (approval workflows) | payout statuses Pending/Due/Processing/Paid (A); commissions updated by system | commission table with "pending and approved payouts" (A) | fraud/compliance checks gate payouts | B (conceptual: recorded → reviewable → approved → paid; exact labels vary) |
| Payout execution inside the product | Y (bulk payouts) | Y (PayPal/Wise mass pay; merchant-executed; optional platform-managed mode) | Y (mass payout files, account balances) | Y (Contract & Pay) | B (execution locus varies: merchant-executed vs platform-managed) |
| Self-service affiliate portal | Y (white-labeled portal) | Y (links, codes, earnings) | Y (affiliate dashboard with banners/smartlinks) | Y (partner side) | B |
| Creative/asset distribution to affiliates | Y (asset management; offers) | lighter (links/codes) | Y (banners, smartlinks, discount codes) | Y (creative & offer management) | B (depth varies) |
| Recruitment machinery | Y (invite links, recruitment tools, Offers marketplace) | Y (Affiliate Finder web crawler; explicitly anti-marketplace) | Y (implied; directory exists) | Y (Discover & Recruit; vetted marketplace) | B (mechanism varies; marketplace optional) |
| Affiliate approval / open vs closed program | Y (bulk approval; invite-only supported) | implied | Y (automation of admin workflows) | Y (compliance workflow) | B |
| Fraud controls | not prominent on fetched page | self-referral detection (A) | invalid-click blocking, repeated-transaction decline, suspicious-referral flagging (A) | Protect & Monitor suite (keyword/code/fake-lead protections) (A) | B (3 of 4 directly; kind varies) |
| Reporting & analytics | Y | Y (real-time) | Y (advanced reports) | Y (40+ reports) | B |
| Program container naming | program | **campaign** (A) | **campaign** (campaign manager) | contract (per-partner terms) | B (concept: one program, optionally partitioned; names vary) |
| Marketplace / network connectivity | Y (Offers marketplace; admitad partner-network access) | N (explicitly rejects marketplace model) | Y (separate Network product; program directory) | Y (vetted marketplace; publisher side) | B — split; **optional**, not defining |
| Multi-level / tiered-downline commissions (MLM) | Y (feature) | — | Y (multi-tier commissions) | — | B-ish (2 of 4; segment variant) |
| Recurring/lifetime commissions (subscription economics) | Y | Y (core) | Y (lifetime referrals manager) | — | B (3 of 4; SaaS-segment common) |
| White-labeling | Y | Y (via API) | — | — | B-ish |
| Platform-managed payouts incl. tax/KYC collection | — | Y (Managed Payouts) | — | — | product-specific |
| Web-crawler-based affiliate prospecting | — | Y (Affiliate Finder) | — | — | product-specific |
| Two-sided publisher marketplace sign-up | optional (Offers) | N | separate product | Y (core) | B — network-flavored, optional |
| Conversational AI assistant over program data | Y (MCP/AI assistant) | — | Y (AI assistant) | AI positioning | B-ish (2026-era convergence; optional) |

## Canonical Model

### L0 — Defining Invariant

The smallest structure without which the product stops being an Affiliate Management Platform:

```text
Merchant-run program
└── Affiliate registry (external promoters, individually identified)
    └── Per-affiliate trackable identifier (link and/or code)
        └── Referral attribution (a tracked customer conversion credited to one affiliate)
            └── Commission accrual (computed from the program's configured commission rules)
```

Five properties, each removable-failure tested:

- **Merchant-side program administration** — the operator is the seller of the goods, running *its own* program. Without this (operator = an intermediary aggregating many merchants), it becomes Affiliate Network software.
- **Affiliate registry with individual identity** — promoters exist as identifiable, enrollable records. Without this, it is anonymous link tracking.
- **Per-affiliate trackable identifier** — a token embedded in the world (link or code) that makes a promoter's influence observable. Without this, attribution is impossible and the "affiliate" object is decorative.
- **Referral attribution** — a customer conversion event is recorded and credited to a specific affiliate. Without this, it is just marketing analytics.
- **Commission accrual** — the platform computes what each affiliate has earned under configured rules. Without this, it is a tracking/attribution tool, not affiliate *management* (no economic relationship to administer).

Attribution *mechanism* (cookies, server-to-server, coupon matching), commission *models* (%, fixed, tiered, recurring), and payout *execution* are deliberately NOT L0 — see below.

### L1 — Common Mature Structure

Present in essentially all mature modern products, but not required to recognize the Type:

- affiliate self-service portal (own links/codes, stats, earnings history)
- creative asset distribution (banners, smartlinks, text assets) from the platform
- recruitment machinery (invite links, signup forms, approval workflow) with open vs closed (invite-only) program postures
- commission review lifecycle (recorded → pending/reviewable → approved/declined → payable) with merchant-side approval gates
- payout support (mass payout, account balances, thresholds; executed by merchant or by the platform)
- fraud controls (self-referral detection, invalid-click filtering, promo-code misuse protection)
- reporting/analytics (per-affiliate, per-asset, program-level performance)
- commerce/billing integration layer (connectors into the merchant's checkout/billing as the conversion source)
- program container with optional partitioning (campaigns/contracts) and per-container commission settings
- team/administration surfaces (multiple admin accounts, permissions) at scale

### L2 — Variant / Optional Structure

Depends on segment, business model, scale, or posture:

- commission-model family: recurring/lifetime (SaaS), tiered/bonuses, multi-level MLM downlines, pay-per-lead vs pay-per-sale
- marketplace/network connectivity (listed in an affiliate marketplace, or bridging into a partner network) — optional in merchant-side tools; the defining structure of the *Affiliate Network* leaf
- white-labeling and custom domains (agency/brand posture)
- platform-managed payouts with tax-document and KYC collection (scale posture)
- AI assistants / conversational analytics (2026-era convergence)
- deployment substrate: SaaS vs plugin/native embedding (Shopify/WordPress apps) vs self-hostable licensing; mobile companion apps
- identity substrate of the affiliate: individual creator, media site, agency, sub-affiliate networks
- privacy/attribution regime: cookie-window configurability, cross-device/server-side tracking options

### L3 — Vendor-specific Detail (stays here)

- Rewardful payout status vocabulary (Pending/Due/Processing/Paid) and "we do not automatically pay" execution model; Affiliate Finder credit mechanics; campaign-level threshold placement.
- Tapfiliate "Affiliate Offers" marketplace; admitad partner-network integration; MCP-based AI assistant positioning; "Sell 100 items → $500 bonus" bonus framing.
- Post Affiliate Pro dual-SKU split (Program vs Network software); "tracking requests"-based plan metering; 24/7 support posture; multi-currency auto-conversion; smartlinks terminology.
- impact.com six-pillar platform naming (Discover & Recruit / Contract & Pay / Track / Engage / Protect & Monitor / Optimize); TrueLink branding; vetted-marketplace positioning; LTV-based optimization claims.

## Anti-overfitting Notes

- All four sampled products are contemporary SaaS-shaped web products. Checks against other eras/postures: self-hosted WordPress-style affiliate plugins and platform-native storefront affiliate apps (e.g., Shopify-native apps) implement the same L0 (registry → trackable ID → attribution → commission) with the plugin marketplace as the deployment substrate — fits. Legacy self-hosted affiliate scripts (the pre-SaaS generation this category grew from, e.g., early 2000s tracking scripts) implement the same four invariants with payouts executed entirely outside the tool — fits, which is exactly why payout execution stays L1. Regional network-connected programs (admitad-style) still reduce to the merchant-side loop — fits. The definition does not depend on cookies specifically: cookie-based windows are one attribution implementation; coupon codes and server-to-server tracking are alternatives present in the sample.

## Vendor-specific Findings

See L3 above. The most consequential: **Post Affiliate Pro sells "Affiliate Program Software" and "Affiliate Network Software" as separate products** — the same vendor treats merchant-side program management and network operation as distinct software categories, which is the cleanest market-side confirmation of the Affiliate Management Platform vs Affiliate Network boundary. Second: **Rewardful explicitly positions itself against marketplaces** ("marketplaces are a passive approach... filled with low quality, poorly vetted affiliates") while Tapfiliate and impact.com sell marketplace access — marketplace participation is a contested optional feature, not part of the Type.

## Boundary Findings

1. **vs Affiliate Network** (adjacent leaf): the network aggregates *many* merchants/programs on one side and a discoverable publisher population on the other, and typically mediates/commissions the economics between them; the Affiliate Management Platform serves *one merchant's own* program. Market evidence: Post Affiliate Pro's product split; impact.com's two-sided sign-up and marketplace (network-flavored) vs Rewardful's explicit anti-marketplace stance; Tapfiliate's marketplace as an optional add-on. Judge-line: remove the multi-merchant aggregation and publisher-discovery marketplace (keep one merchant, its own promoters, its own commission ledger) → still this Type; remove single-merchant operation (many merchants, publisher marketplace) → Affiliate Network.
2. **vs Referral Marketing Platform**: referral programs recruit the seller's own *customers* as promoters (relationship precedes the program; rewards often non-cash/store-credit) while affiliate programs recruit external professional promoters (no prior customer relationship; cash commissions). The machinery generalizes — Tapfiliate, Rewardful and impact.com all ship both program types on shared tracking/commission infrastructure — so the boundary is the participant population and reward basis, not the objects. Risk of overlap is real and recorded; the directory keeps them as separate leaves because the canonical participant (customer vs external promoter) changes recruitment, fraud, and payout semantics.
3. **vs Influencer Marketing Platform**: influencer tools center discovery, content campaigns, gifting, and audience metrics; affiliate tools center commission-per-conversion economics. Convergence trend: impact.com merges both; Tapfiliate markets "influencer programs" that are really affiliate tracking pointed at creators. Boundary: if the primary object is the campaign/content relationship, it is influencer marketing; if the primary object is the attributed conversion and its commission, it is this Type.
4. **vs Partner Relationship Management / PRM** (already-processed leaf, consistent with its research): PRM manages external *partner organizations* (resellers, distributors, ISVs) with partner-side authenticated users and channel-selling workflows (deal registration, lead distribution); affiliate platforms manage *individual promoters* rewarded per conversion via links/codes. Affiliates may appear as one partner type inside a PRM, and enterprise partnership platforms (impact.com) drift toward both — boundary holds structurally.
5. **vs Marketing Attribution / link-tracking tools**: those measure channels; this Type adds the promoter registry and the commission economics built on top of attribution. Remove commissions and promoter enrollment → attribution tool, not this Type.

## Uncertainties

- Tapfiliate help-center article bodies were not fetched; its affiliate/commission status vocabulary is unverified beyond marketing-page descriptions. Mitigation: lifecycle described conceptually in the final document.
- Post Affiliate Pro self-hosted availability: part of the product's known history but not asserted on fetched pages; deployment variants are written without naming self-hosting as current fact.
- impact.com operational depth (contract engine, payout scheduling) documented only at platform-pillar grain; no precise workflow claims made.
- Refersion dropped (403 ×2); e-commerce pole covered indirectly. Low residual risk: Tapfiliate and Post Affiliate Pro both document Shopify/WooCommerce integrations extensively.
- Exact attribution-window durations, payout schedules, and fraud-rule parameters: intentionally not stated anywhere (no sampled source documented them at precision).

## Final Synthesis

An Affiliate Management Platform is the software a merchant uses to operate its own performance-based promoter program: it keeps a registry of enrolled affiliates, issues each one a trackable identifier (link and/or coupon code), records customer conversions flowing through the merchant's own commerce/billing stack, attributes each conversion to a specific affiliate, computes commissions from configurable rules, and carries those commissions through a review-and-settlement lifecycle that ends in payout. Around this loop, mature products add an affiliate self-service portal, creative distribution, recruitment and approval machinery, fraud controls, analytics, and deep integration with the merchant's storefront/billing substrate. The Type is bounded against Affiliate Network (multi-merchant aggregation + publisher marketplace vs one merchant's own program), Referral Marketing (customers vs external promoters), Influencer Marketing (campaign/content vs conversion/commission objects), and PRM (partner organizations vs individual promoters). Marketplace/network connectivity, recurring-commission models, white-labeling, platform-managed payouts with KYC, and AI assistants are variants layered on a stable four-part core.
