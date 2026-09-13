# Research Notes — Affiliate Network

Research date: 2026-09-06

## Research Goal

Understand what an Affiliate Network actually is as a software structure: who operates it and who uses it on each side, what objects exist inside it (advertiser accounts, publisher accounts, programs/offers, tracking, commissions, payouts), how the two-sided workflow flows from program listing through publisher discovery to settlement, which states and rules govern commissions and money, and where its boundary lies against Affiliate Management Platform (the sibling leaf, already processed), ad networks/DSPs, online marketplaces, Referral Marketing, Influencer Marketing, and PRM.

This pass also discharges the joint-reference flag recorded by the affiliate-management-platform pass: "structural test = remove single-merchant operation (many merchants + publisher-discovery marketplace + network-mediated economics) → Affiliate Network; keep one merchant's own program with its own commission ledger → this Type."

## Initial Boundary

Working hypothesis before research:

- An Affiliate Network is an **intermediary-operated, two-sided platform**: a network company (neither the seller nor the promoter) aggregates many advertisers' affiliate programs on one side and many publishers/affiliates on the other.
- Publishers join the network **once** and discover/apply to many advertisers' programs through a network-operated directory or marketplace.
- The network issues the tracking identifiers, attributes conversions to publisher × advertiser-program pairs, keeps a cross-advertiser commission ledger per publisher, and **mediates the money**: it bills advertisers (commissions + its own fee) and pays publishers (consolidated across programs).
- It is NOT one merchant's own program tool (Affiliate Management Platform), NOT an ad network selling impressions/clicks (DSP/ad-server family), NOT a consumer shopping marketplace, NOT influencer campaign software, NOT PRM.
- Suspected gray zones to verify: (a) whether the settlement function is truly defining or merely universal; (b) the ClickBank retailer-of-record model — does selling to consumers break the Type?; (c) network-operator software (launch-your-own-network platforms) vs operated networks; (d) enterprise partnership platforms straddling network + merchant-side tool.

## Research Questions

1. Who operates the system, and who are the users on each side (advertiser, publisher, network staff)?
2. What are the core objects: advertiser account, publisher account, program/offer listing, tracking identifier, transaction/commission, payout, invoice?
3. How does the central loop work: advertiser joins → integrates → lists program → publisher joins network → discovers → applies → promotes → tracked conversion → validation → settlement?
4. What lifecycle states exist for program participation, transactions/commissions, payouts?
5. What rules govern behavior: program approval gates, attribution windows/methods, commission validation, network fees, payment thresholds, anti-fraud requirements, compliance enforcement?
6. What interfaces exist: advertiser dashboard, publisher dashboard, public directory/marketplace, signup surfaces, APIs?
7. How does the money flow — who pays whom, and where does the network's fee enter?
8. What variants exist: settlement models, vertical focus, publisher taxonomy, regional structure, service posture, network-operator software?
9. Does the definition survive older/regional/differently-positioned samples (classic 1990s networks, regional CPA networks, retailer-of-record models, network-operator software)?

## Representative Products

| Product | Segment / philosophy | Why selected |
|---|---|---|
| Awin (incl. ShareASale, merged 2017→unified) | Global classic network, 30k+ advertisers / 1M+ partners, plan-tiered self-serve + managed; strong advertiser-side pricing documentation | Market-leading classic-network pole; ShareASale legacy brand confirms consolidation; unusually explicit fee economics (tracking fee per transaction) |
| CJ Affiliate (Commission Junction, since 1998) | Largest US classic network, enterprise posture, deep service layer | Enterprise anchor; documents publisher-side payments (two monthly payouts, 150+ currencies), network-curated discovery, and network-level compliance (pre-payment validation) |
| ClickBank (since 1998) | Digital-goods network with **retailer-of-record** model — processes orders itself and routes funds | Opposite settlement philosophy; exceptionally good Tier-1 help center (HopLinks, payment mechanics) reached |
| Admitad (since 2009, CIS-origin, now German) | CPA/CPL/CPS network with broad publisher taxonomy (cashback, loyalty, bank apps, OEM, Telegram) and "one invoice" settlement | Regional/global CPA pole; broadest publisher-population variant; explicit "all on one invoice" settlement framing |

Rejected/adjusted sample:
- **ShareASale**: no longer a separate product — shareasale.com now redirects into Awin onboarding ("ShareASale is now part of Awin... new customers are invited to launch directly with Awin"). Treated as Awin's legacy brand, not a distinct sample.
- Not selected: Rakuten Advertising, TradeDoubler, Commission Factory (additional classic networks — would repeat existing evidence); PartnerStack (B2B SaaS partner ecosystem — recorded as boundary note, likely fits the structure with recurring commissions; unverified this pass); TUNE/Affise/Everflow (tracking/platform tools, better boundary evidence for merchant-side or network-operator software); impact.com (already sampled in the sibling pass as a straddling enterprise partnership platform).

## Sources

Fetched 2026-09-06 (Layer A unless noted):

- Awin — ShareASale migration page (merger confirmation + network positioning): https://www.shareasale.com/
- Awin — advertiser solution page: https://www.awin.com/us/advertisers
- Awin — advertiser pricing/plans page (fee economics, feature matrix): https://www.awin.com/us/pricing/advertisers
- Awin — publisher (content creators & influencers) page: https://www.awin.com/us/publishers
- Awin — Help Center root + article "Batch validate pending transactions" (Tier 1): https://help.awin.com , https://help.awin.com/docs/batch-validate-pending-transactions
- CJ Affiliate — homepage: https://www.cj.com/
- CJ Affiliate — publisher page: https://www.cj.com/publisher
- CJ Affiliate — advertiser page: https://www.cj.com/advertiser
- ClickBank — homepage/FAQ: https://www.clickbank.com/
- ClickBank — "How ClickBank Works" (Tier 1/2 flow documentation): https://www.clickbank.com/how-clickbank-works/
- ClickBank — Help Center root: https://support.clickbank.com/
- ClickBank — "How is my payment amount determined?" (Tier 1): https://support.clickbank.com/en/articles/10535135-how-is-my-payment-amount-determined
- ClickBank — "HopLinks Guide" (Tier 1): https://support.clickbank.com/en/articles/10535278-hoplinks-guide
- Admitad — homepage/platform overview: https://www.admitad.com/

Source-access limitation:
- Awin's partner-facing help section (help.awin.com/partners) is "under construction" and redirects to the Partner Success Centre (success.awin.com); a guessed article URL there returned 404 and the portal is JS-rendered. Awin publisher-side lifecycle vocabulary is therefore unverified at help-article grain; publisher-side observations lean on official product pages (Tier 2).
- CJ help center (help.cj.com / support.cj.com) was not fetched; CJ observations lean on Tier-2 official product pages, which document features and flows at coarser grain than help articles.
- Admitad help center (support.admitad.com) and developer docs were not fetched; observations are homepage/product-page grain.
- Consequence: assertion strengths calibrated accordingly. Precise operational details are stated ONLY where a fetched source documents them (Awin fee example, ClickBank fee/window/threshold/return-allowance mechanics, CJ payout cadence claim). All other lifecycle and rule descriptions are written conceptually.

## Product Observations

### Awin (Layer A — official product/pricing pages + one Tier-1 help article)

- ShareASale merger: shareasale.com now serves Awin onboarding — "ShareASale is now part of Awin... Instead of signing up to ShareASale, new customers are invited to launch directly with Awin." Same mission, one platform.
- Two-sided scale claims: 30,000+ brands (advertisers), 1M+ global partners (publishers: content creators, influencers, tech partners, cashback sites).
- Advertiser plans: **Access** ($49/month + **3.5% per transaction tracking fee**), **Accelerate** (from $99/month + 2.5% tracking fee), **Advanced** (custom pricing). Documented example: "On a $100 sale with 6% commission, your partner gets $6 and Awin gets $3.50" — the advertiser pays both the partner commission and the network's tracking fee. Alternative rates for businesses without transaction values (finance/telecom).
- Feature matrix (advertiser): Discover — "Search partners through our 1M+ trusted directory", "Discover new promotional campaigns in our marketplace", personalized partner recommendations; Engage — campaigns in one tool, "Chat with partners using the Communication Center", automated partner emails, "Customize your branded private network" (Accelerate+); Measure — campaign tracking, reports, customer-journey analysis, benchmarks; Reward — commission rules ("Create up to three/unlimited commission groups" with rules on Product ID, product category, SKU, new/existing customers, coupon code, clicks on website, campaign, publisher, sub partner ID, transaction date, attribution), **"Auto-approve transactions to validate partner sales"**, **"Manage partner payments with secure processing"** (Accelerate+), "Manage payments and invoicing with flexible options".
- Tier-1 help article "Batch validate pending transactions": transactions have a **pending** state; advertisers validate them via **Commission > Validate > Batch Process Commission** — manual or automated; upload Accepted/Declined files keyed by Order Reference + Transaction Date + Status, with a Status Note selecting from listed decline reasons. Confirms an advertiser-side validation gate over network-recorded transactions.
- Integration: self-managed wizard; plugins for Shopify, WooCommerce, Magento; technical integration add-ons.
- Publisher side (content creators & influencers page): "Connect with 30,000+ top brands"; tools — **Link Builder** (create links from your phone), **Offers** (exclusive discount codes/promotions from brands), **Product Search**, **Storefronts** (curated shoppable page), mobile app; "Our tracking captures every sale you make."
- Publisher payments (FAQ): "Awin offers a range of payment methods including SEPA, BACS, ACH, and Domestic payments... For International Wire Transfers (IWT), we have partnered with Payoneer" — the network pays publishers.
- Public **Advertiser Directory** ("Search and connect with brands across every industry").
- Regional structure: "you'll need to complete an application form and establish a program separately for each region" — per-region programs; APAC access via sister network Commission Factory.
- AI assistant "Ava" (24/7 answers, insights, recommendations).

### CJ Affiliate (Layer A — official product pages; Tier-2 grain)

- Positioning: "the world's largest and most established partnership-based performance marketing ecosystem"; operating since 1998; vendor-reported scale: $1.8B+ annual publisher commissions, 4.8M relationships created annually, 157M transactions annually.
- Two-sided structure with separate sign-up flows: Advertiser/Agency ("You sell or promote products and services and work with websites and creators, paying commissions for sales, leads or traffic") and Publisher/Creator ("You've built an audience or following and want to earn commissions by promoting brands and products you believe in").
- Publisher-side flow (documented): interactive onboarding showcasing publisher value "for greater discovery with brands"; "Gain instant access to our global network of brands and **join programs with a single click**"; **"Instant Approval from Top Brands"** via the Content Certification program (pre-vetted influencers) — implying the default is an application/approval relationship with fast-paths for certified publishers.
- Publisher link tooling: select links in-platform; **Deep Link Generator** ("create tracking links directly from a brand site"); auto-detect and convert existing URLs into trackable links.
- Publisher payments: "access on-demand details for all earned commissions and historical payouts. We offer dozens of payout currencies and **two monthly payouts**"; "Get paid in over 150 currencies via direct deposit or our global payments partner, Payoneer" — network pays publishers directly.
- Tracking: "Comprehensive Omni-Channel Tracking... From online to offline, across devices (including mobile and in-app), phone calls, and in-store... protected from browser restrictions and compliant with privacy regulations."
- Advertiser-side: **Partnership Discovery** ("Find and activate new partnerships... by promotional model, global footprint, audience uniqueness, social reach & engagement, category performance, keyword... Discover network-curated partnerships... for content, rising stars, new-to-network, and top performers"); **Situational Commissioning** ("dynamic commissioning solution... create commissioning scenarios that reward publishers based on a wide range of high-value order attribute combinations, such as customer status, promotion type, and customer location"; commission structures per partner and promotional property); **Placements Marketplace** ("Access and manage your placements and media campaigns"); turnkey Shopify/Magento plugins.
- Network-level compliance: **Network Quality Assurance** ("prevent, detect, and address fraud and other non-compliant activity"); **Pre-Payment Validation** ("We proactively review each and every publisher for compliance prior to their first payment"); Program Compliance Services with a real-time Compliance Dashboard.
- Service options: self-managed, agency partner, or white-glove strategy/recruitment/execution.
- APIs: Developer Portal (developers.cj.com) — "find or manage relationships, access offers, discover products to promote, and view program performance details."

### ClickBank (Layer A — homepage/FAQ + Tier-1 "How ClickBank Works", payment article, HopLinks Guide)

- Positioning: "an e-commerce platform and affiliate marketplace that serves as an intermediary between the end customer, product owner, and affiliate marketer... **As the merchant of record, ClickBank processes each order and routes the funds from each transaction to the parties involved in a purchase.**"
- Affiliate journey (documented): generate traffic → **choose offer** (scan the ClickBank marketplace) → **create tracking link** (HopLink) → promote → **get paid directly from ClickBank** "out of the funds collected from the transaction."
- Seller journey (documented): launch affiliate program → create a **direct response offer** → **list product on the ClickBank Marketplace** → use the ClickBank order form → "**ClickBank Pays Affiliates, Taxes, and You**" — routes incoming funds from each sale, including paying affiliates, covering taxes, and paying the seller.
- Fee economics (documented): ClickBank takes **7.5% + $1** per transaction off the top; the remainder is split between seller and affiliate per the agreed RevShare or CPA structure. Worked example given on the page ($100 sale → $8.50 fee → taxes/shipping → remainder split, e.g., 65% revshare).
- Marketplace: "the hub where product owners and affiliates can connect"; public product listings share "key metrics about its performance" to help affiliates choose; **"Get Affiliate Link"** button on listings.
- Per-seller approval gate (Tier 1, HopLinks Guide): "If the seller requires affiliates to be approved before they start promoting, you won't be able to get a tracking link from the listing. Instead, you can reach out to the seller for approval." Also: sellers can maintain **allowed-affiliate lists** — "if the seller creates a list of allowed affiliates that does not include your account," HopLinks stop working. Open promotion is the default posture.
- HopLinks (Tier 1): network-issued tracking URL containing affiliate account nickname + seller account nickname (+ optional tracking ID); **encrypted by default** to protect affiliate IDs from spy tools; Encode/Decode tooling; **60-day referral window** ("If a customer buys a product within 60 days of clicking on a HopLink, the affiliate who referred the customer receives credit"); **last-touch attribution** ("The most recent affiliate to promote the offer using a HopLink receives credit for the sale"); sellers see which affiliates sent traffic in their reporting; commission type (revshare vs CPA) is a seller-controlled setting that does not change the link.
- Invalid-use rules (Tier 1): HopLinks must open in a top-level window — frames/iframes/layers prohibited; "in the case of abuse of the HopLink system... account termination without notice."
- Payment mechanics (Tier 1, "How is my payment amount determined?"): **Customer Distribution Requirement** (anti-fraud: minimum five sales using at least two payment methods before first payment); **Payment Threshold** (user-selected, documented range $10–$1,000,000, default $100); **Return Allowance** (a fraction of each pay period's revenue withheld — standard 10% — released after about 12 weeks, to cover delayed refunds/chargebacks); dormant-account fees; refunds (100% refund paid out of the corresponding client account; recurring-product refund cancels further recurring payments); tiered chargeback fees.
- Refund window (How-It-Works page): "the customer usually has 60 days to request a refund"; the party covering the refund depends on RevShare vs CPA.
- Vendor-reported scale: $7.3B commissions paid over 27+ years; 100k active affiliates; 190 countries.

### Admitad (Layer A — homepage/platform overview; Tier-2 grain)

- Positioning: "Collaboration Platform for Management Partners"; tagline: "**One platform to pay every marketing partner.** Find partners or bring your own. Onboarding, compliance, and global payouts — **all on one invoice.**"
- Scale claims: 2000+ advertisers, 300,000+ publishers, 50+ countries.
- "Partnership collaboration management with **internal marketplace** of affiliates, influencers, ambassadors, OEM providers, loyalty programs and cashback services, bank apps and others."
- **Admitad Store**: publisher-facing marketplace — "Find 3000+ brands to partner with."
- Admitad Perform: "A robust, tech-driven affiliate platform for customer acquisition via **CPA, CPL, and CPS models**. Connect with a global ecosystem of **vetted partners**, leverage real-time tracking and deep analytics, and **automate every step — from integration to payouts**."
- Publisher taxonomy (broadest in sample): affiliate publishers, coupons & deals sites, influencers & creators, loyalty & rewards (cashback/mileage/bank loyalty), mobile apps & OEM, premium media publishers, call centers, Telegram channels, bank apps.
- Admitad Flow: "Contract and Pay for any external partners... we take care of contracts, compliance, and global payouts" — network-side contract/compliance/payout services.
- Separate registration flows: "Start as Advertiser" vs "Start as Publisher" (store.admitad.com webmaster registration).
- Help center (support.admitad.com) and developer API (developers.admitad.com) exist; not fetched this pass.

## Cross-product Comparison

| Structure / capability | Awin | CJ Affiliate | ClickBank | Admitad | Evidence layer |
|---|---|---|---|---|---|
| Operated by an intermediary (network company, not a merchant) | Y (Awin AG) | Y (Commission Junction) | Y (ClickBank as merchant of record) | Y (Admitad/Mitgo) | B (all four) |
| Many advertisers, each with program(s)/offer(s) | Y (30k+ brands) | Y (enterprise advertisers) | Y (sellers listing offers) | Y (2000+ advertisers) | B |
| Many publishers with a single network membership | Y (1M+ partners) | Y | Y (100k affiliates) | Y (300k+ publishers) | B |
| Publisher-facing discovery across many programs (directory/marketplace) | Y (directory + marketplace + recommendations) | Y (in-platform brand discovery, network-curated partnerships) | Y (ClickBank Marketplace with public listings + metrics) | Y (Admitad Store, 3000+ brands) | B |
| Network-issued tracking identifiers | Y (Link Builder, MasterTag per FAQ links) | Y (Deep Link Generator, URL auto-conversion) | Y (HopLinks, encrypted, TIDs) | Y (link/promo-code tracking per Perform) | B |
| Attribution of conversion to publisher × program | Y (tracking "captures every sale") | Y (omni-channel tracking) | Y (60-day window, last-touch — documented) | Y (real-time tracking) | B (mechanism documented in ClickBank; conceptual elsewhere) |
| Cross-advertiser commission ledger per publisher | Y (publisher earnings across brands) | Y ("all earned commissions and historical payouts") | Y (account activity across sellers) | Y | B |
| Network mediates settlement (party in the money flow) | Y (bills advertiser commission + tracking fee; "manage partner payments") | Y (pays publishers; two monthly payouts) | Y (merchant of record; routes funds; pays affiliates, taxes, seller) | Y ("all on one invoice"; global payouts) | B — with three different settlement shapes |
| Program participation gate (approval per advertiser) | Y (implied by directory/application; auto-approve transactions documented) | Y (single-click join + Content Certification instant approval implies default approval flow) | Y (per-seller approval; allowed-affiliate lists — documented) | Y ("vetted partners") | B (default open vs approval-required varies) |
| Commission validation lifecycle | Y (pending → Accepted/Declined with reasons; auto-approve option — Tier 1) | Y (pre-payment validation; fraud monitoring) | Y (return allowance covers delayed refunds/chargebacks — Tier 1) | Y (order validation mentioned in testimonial; Perform automation) | B (Awin/ClickBank documented; conceptual elsewhere) |
| Commission rules engines | Y (commission groups by product/customer/coupon/publisher/etc.) | Y (Situational Commissioning by order attributes) | Y (revshare vs CPA per seller; seller-controlled) | Y (CPA/CPL/CPS models) | B |
| Creative/offer distribution | Y (Offers, creatives) | Y (links, placements) | Y (affiliate resources pages; marketplace listings) | Y (offers in Store) | B (depth varies) |
| Publisher-side tooling | Y (Link Builder, Product Search, Storefronts, app) | Y (Deep Link Generator, URL converter) | Y (HopLink tools, encode/decode, TIDs) | Y (link/promo tools) | B |
| Reporting & APIs for both sides | Y (reports, benchmarks, APIs) | Y (insights, Developer Portal) | Y (Sales Analytics, developer tools) | Y (analytics, API) | B |
| Compliance/fraud controls | Y (auto-approve vs manual validation; approved partners) | Y (Network QA, Pre-Payment Validation, Compliance Dashboard) | Y (CDR, return allowance, invalid-HopLink rules, termination) | Y (vetted partners, compliance service) | B |
| Payment infrastructure (thresholds, currencies, partners) | Y (SEPA/BACS/ACH/Payoneer) | Y (two monthly payouts, 150+ currencies, Payoneer) | Y (threshold default $100 documented; CDR; return allowance) | Y (global payouts) | B (parameters documented only in ClickBank; cadence claimed by CJ) |
| Recruitment/matching machinery | Y (AI recommendations, directory search) | Y (network-curated discovery) | Y (marketplace metrics aid choice) | Y ("find partners or bring your own") | B |
| Advertiser onboarding/integration | Y (wizard, Shopify/WooCommerce/Magento plugins) | Y (turnkey Shopify/Magento plugins) | Y (seller launch checklist; order form provided) | Y ("from integration to payouts") | B |
| **Settlement shape: tracking-fee + invoicing** | Y (3.5%/2.5% tracking fee documented) | — | — | Y-ish ("one invoice") | B |
| **Settlement shape: retailer-of-record** | — | — | Y (processes orders, routes funds) | — | product-specific variant |
| **Settlement shape: consolidated publisher payouts** | Y | Y (two monthly payouts) | Y (from collected funds) | Y | B |
| Consumer-facing checkout operated by the network | N | N | Y (ClickBank order form) | N | product-specific variant |
| Adjacent partnership types bundled (influencer/placements/mobile) | partial (creators/influencers as publisher class) | Y (CJ Influence, Placements Marketplace) | N (direct-response focus) | Y (Creator, Mobile, Rewards, Flow, Seller product lines) | B — optional breadth |
| Private/branded network inside the network | Y (Advanced plan) | — | — | — | product-specific |
| Network-operator software (launch your own network) | — | — | — | — | out-of-sample note: Post Affiliate Pro Network SKU (sibling-pass evidence) |

## Canonical Model

### L0 — Defining Invariant

The smallest structure without which the product stops being an Affiliate Network:

```text
Network-operated intermediary (operator is neither seller nor promoter)
└── Two-sided multi-party registry
    ├── many advertiser accounts, each running program(s)/offer(s)
    └── many publisher accounts, each holding ONE network membership
        └── Publisher-facing discovery of many programs (directory/marketplace)
            └── Network-issued tracking → conversion attributed to publisher × advertiser-program
                └── Cross-advertiser commission ledger per publisher
                    └── Network-mediated settlement (network bills advertisers commission + fee;
                        pays publishers consolidated across programs)
```

Five properties, each removable-failure tested:

- **Intermediary operation** — the operator is a third party serving both sides and party to the economics. Without this (operator = one merchant running its own program), it becomes an Affiliate Management Platform.
- **Two-sided multi-party registry** — many advertisers AND many publishers; a publisher's single network membership spans many advertisers' programs. Without the many-advertiser side, it is a merchant tool; without the many-publisher side, it is an advertiser's private portal.
- **Publisher-facing program discovery** — a network-operated surface (directory/marketplace) where publishers find, evaluate, and join many advertisers' programs. Without this, publishers would need bilateral relationships only; the aggregation — the reason networks exist — disappears.
- **Network-issued tracking + attribution** — conversions are tracked through network identifiers and credited to a specific publisher for a specific advertiser program. Without this, it is a directory without economics.
- **Network-mediated settlement** — the network is a party in the money flow: it bills advertisers (partner commissions plus its own fee) and pays publishers (consolidated across programs). Without this, it is a discovery/tracking layer, not the economic intermediary that defines the network model.

Attribution *mechanism* (cookies, windows, last-touch vs other), commission *models* (revshare/CPA/CPL), fee *rates*, and the *form* of settlement (invoice+tracking-fee vs retailer-of-record vs payout service) are deliberately NOT L0 — see L2.

### L1 — Common Mature Structure

Present in essentially all mature networks, but not required to recognize the Type:

- program participation gates: per-advertiser control over which publishers may promote (approval-required vs open; allowed-publisher lists; vetted/fast-track publisher classes)
- commission validation lifecycle: recorded transaction → pending → validated (accepted/declined with reasons; manual or auto-approval) → payable
- commission rules engines: per-product/category/SKU, new-vs-existing customer, coupon-based, publisher-specific, order-attribute-based rules
- creative & offer distribution: banners, product feeds, deep links, exclusive discount codes/offers
- publisher tooling: link builders, deep-link generators, product search, storefronts, mobile apps
- reporting/analytics + APIs for both sides (clicks, conversions, commissions, payouts; developer portals)
- compliance & fraud controls: network quality assurance, pre-payment validation, invalid-traffic filtering, affiliate-ID encryption, promotional-method enforcement
- payment infrastructure: payment thresholds, anti-fraud eligibility requirements, multi-currency payouts, payment partners, defined payout cadences
- recruitment/matching machinery: directory search, AI recommendations, curated partner lists, account management
- advertiser onboarding/integration: setup wizards, ecommerce platform plugins, tracking integration

### L2 — Variant / Optional Structure

Depends on segment, settlement philosophy, geography, or posture:

- **settlement model**: (a) tracking-fee + invoicing — conversion happens on the advertiser's site, network bills advertiser commission + per-transaction fee (Awin-documented); (b) retailer-of-record — conversion happens on the network's own checkout, network collects payment, deducts its fee, splits the remainder (ClickBank-documented); (c) consolidated-payout service — network invoices advertisers and pays publishers at scale ("one invoice", Admitad; CJ payouts). All three keep the network in the money flow; the shape varies.
- offer/vertical focus: physical retail (Awin/CJ), digital direct-response goods (ClickBank), CPA/CPL/mobile/finance lead-gen (Admitad)
- publisher taxonomy breadth: media sites + creators vs coupons/deals/cashback/loyalty/OEM/bank-app/Telegram publishers
- regional structure: per-region programs under one network (Awin) vs regional sister networks vs global single pool
- private/branded networks walled inside a shared network (Awin Advanced)
- service posture: self-serve plans vs managed/white-glove service layers
- network-operator software: platforms sold to entrepreneurs/companies to launch their own network (Post Affiliate Pro "Affiliate Network Software" — sibling-pass evidence); same core structure, different operator posture
- adjacent partnership types bundled into the platform: influencer campaigns, placements marketplaces, mobile/OEM inventory, contract-and-pay services
- consumer-facing checkout operated by the network (retailer-of-record variant only)

### L3 — Vendor-specific Detail (stays here)

- Awin: plan names/pricing (Access $49 + 3.5%, Accelerate $99 + 2.5%, Advanced custom), "Ava" AI assistant, MasterTag, Storefronts, Link Builder, Commission Manager / Batch Process Commission UI paths, per-region program requirement, Commission Factory sister network, LTK integration mention.
- CJ: Situational Commissioning, Placements Marketplace, Content Certification, CJ Influence / CJ Leads / CJ Marketplaces product lines, CJU conference, Deep Link Generator, "two monthly payouts" cadence claim, vendor-reported scale figures.
- ClickBank: HopLink format/encryption/Decode tooling, TIDs, 60-day referral window, 60-day refund window, 7.5% + $1 fee, CDR (5 sales / 2 payment methods), payment threshold default $100 (range $10–$1M), 10% return allowance released after ~12 weeks, dormant-account fee schedule, chargeback fee schedule, direct-response offer concept, Spark education program, Platinum Program.
- Admitad: product-suite naming (Perform / Creator / Rewards / Mobile / Flow / Seller), Admitad Store, "Back to School Marathon" promotions, Mitgo group structure.

## Anti-overfitting Notes (historical / market-sample check)

- Classic networks of the late-1990s founding generation (CJ 1998, ClickBank 1998) fit the five-property L0 exactly: two-sided registries, publisher directories/marketplaces, network tracking, network-mediated money. The definition is not an artifact of the modern SaaS era.
- Regional networks (Admitad, CIS-origin; Commission Factory, APAC; TradeDoubler, Europe — the latter two unsampled but structurally identical per the sampled regional case) fit: multi-advertiser aggregation + publisher discovery + network settlement are region-independent.
- The retailer-of-record variant (ClickBank) fits: the network still aggregates many sellers, publishes a marketplace, issues tracking, and mediates money — it simply also owns the checkout. The L0 holds; the checkout ownership is L2.
- Network-operator software (Post Affiliate Pro Network SKU) fits as a deployment/operator variant: the software implements the same five properties for a network entrepreneur.
- B2B SaaS partner ecosystems (PartnerStack — unsampled, recorded as boundary note): multi-vendor programs + partner discovery + consolidated recurring-commission payouts — structurally the same L0 with recurring-commission economics; flagged, not asserted.
- The definition does not depend on cookies specifically (ClickBank documents cookie-based windows; promo-code and server-side tracking exist across the family), nor on any specific fee rate (documented rates vary: 2.5–3.5% tracking fee vs 7.5% + $1 transaction fee), nor on payout cadence.

## Vendor-specific Findings

See L3. Most consequential for boundaries:

1. **Post Affiliate Pro sells "Affiliate Program Software" and "Affiliate Network Software" as separate products** (sibling-pass evidence) — the same vendor treats merchant-side program management and network operation as distinct software categories. This is the market-side confirmation of the Affiliate Management Platform vs Affiliate Network split, now corroborated from this side: all four sampled networks are intermediary-operated with publisher marketplaces and network-mediated money — none is a merchant's own-program tool.
2. **Settlement shape is a contested variant, not the definition**: ClickBank's retailer-of-record model (network owns the checkout, collects consumer payment) vs Awin's tracking-fee model (conversion on the advertiser's site; network bills a per-transaction fee) vs Admitad's "one invoice" service model. All keep the network in the money flow; none is universal.
3. **Awin Access is the instructive gradient case**: a merchant self-serve plan that looks like merchant-side software but sits inside the network — the publisher pool, discovery, tracking, and settlement are network-operated, and the network takes a per-transaction fee. It confirms that "self-serve" does not make a product merchant-side; the operator identity and money path do.
4. **Open vs approval-required programs vary per advertiser within one network** (ClickBank documents both: default open promotion with "Get Affiliate Link", plus per-seller approval and allowed-affiliate lists; CJ documents single-click join plus instant-approval fast-paths). Program participation gating is L1 machinery; its default posture is per-program configuration.

## Boundary Findings

1. **vs Affiliate Management Platform** (sibling leaf, joint reference discharged): the discriminator is the operator identity and the money path. AMP = one merchant runs its own program: its own promoters, its own commission ledger, conversions observed in the merchant's own commerce/billing stack, merchant pays affiliates. AN = an intermediary aggregates many merchants: publishers hold one network membership across many programs, discovery is network-operated, and the network mediates settlement (bills advertisers, pays publishers, collects its fee). Judge-line confirmed from both sides: remove multi-merchant aggregation + publisher marketplace + network-mediated settlement → AMP; add them → AN. Marketplace/network connectivity appears as an *optional feature* inside merchant-side tools (sibling-pass evidence: Tapfiliate Offers marketplace, admitad integration; impact.com two-sided marketplace) — the gradient is real, and enterprise partnership platforms straddle it, but the canonical centers are distinct. No taxonomy conflict.
2. **vs Ad Network / DSP / Ad Server**: ad networks sell media inventory priced per impression/click (CPM/CPC) with bidding/pacing machinery; affiliate networks pay per result (CPA/CPS/revenue share) with a promoter registry and commission ledger. The publisher is inventory in one and a compensated promoter in the other. CJ's Placements Marketplace (fixed media placements inside an affiliate network) is an adjacent capability, not the core.
3. **vs Online Marketplace (commerce)**: ClickBank makes the boundary explicit — it operates a consumer checkout and calls itself a "marketplace", but the two-sided population is advertisers × publishers, and its marketplace is a *partner-discovery* surface (sellers list offers for affiliates to promote), not a consumer shopping surface. The consumer-facing storefront is the retailer-of-record variant's byproduct, not the defining structure. Remove the affiliate/commission machinery and ClickBank's shape would become an e-commerce platform — a different Type.
4. **vs Referral Marketing Platform**: referral programs recruit the seller's own customers as promoters (relationship precedes the program; rewards often non-cash); networks recruit professional external promoters at scale (no prior customer relationship; cash commissions). Consistent with the sibling pass's finding that the machinery generalizes across both.
5. **vs Partner Relationship Management / PRM** (processed leaf): PRM manages external partner *organizations* (resellers, distributors, ISVs) with partner-side authenticated users and channel-selling workflows; networks manage individual promoters rewarded per conversion via network-issued links. Enterprise partnership platforms drift toward both; boundary holds structurally.
6. **vs Influencer Marketing Platform**: influencer tools center discovery, content campaigns, gifting, audience metrics; networks center attributed conversions and commissions. Convergence is visible inside the sample (CJ Influence; Admitad Creator; Awin's creator/influencer publisher classes) — influencer activity is absorbed as a publisher class with campaign add-ons, while the commission-per-conversion core remains the network's spine.
7. **vs Marketing Attribution / link-tracking tools**: those measure channels; the network adds the two-sided registry, the discovery marketplace, and the settlement economics. Remove any of the three → not a network.

## Uncertainties

- Awin publisher-side lifecycle vocabulary (application states, commission statuses as labeled in its portal) unverified — partner help section under construction; success.awin.com article fetch failed (404 on guessed URL; portal JS-rendered). Mitigation: lifecycle described conceptually; Awin advertiser-side validation documented at Tier 1.
- CJ operational depth (program application mechanics, commission lock/validation vocabulary, invoice mechanics) documented only at product-page grain; no precise CJ workflow claims made. The "two monthly payouts" cadence is a vendor marketing claim, attributed as such.
- Admitad help center and developer docs not fetched; observations are homepage/product-page grain. "Order validation" appears only in a customer testimonial.
- Exact commission lock/hold periods (beyond ClickBank's documented return-allowance mechanics), payout schedules (beyond CJ's claim and ClickBank's pay-period mechanics), and network fee rates (beyond the two documented examples) are intentionally not generalized.
- PartnerStack and other B2B SaaS partner ecosystems not sampled; their fit is recorded as a boundary note, not a finding.
- Network-staff (operator-side) administration surfaces were not directly documented by any fetched source (they sit behind the operated service); the final document deliberately does not invent their structure.

## Final Synthesis

An Affiliate Network is a two-sided intermediary platform operated by a network company — neither the seller nor the promoter. On one side, many advertisers run affiliate programs/offers listed in the network; on the other, a large population of publishers holds a single network membership that spans all of them. Publishers discover and join programs through a network-operated directory/marketplace; the network issues the tracking identifiers that attribute each conversion to a specific publisher for a specific advertiser program; a cross-advertiser commission ledger accumulates per publisher; and the network settles the money — billing advertisers for partner commissions plus its own fee, and paying publishers consolidated across all their programs, subject to validation gates, thresholds, and anti-fraud requirements. Around this core, mature networks add program-approval machinery, commission rules engines, validation lifecycles, creative/offer distribution, publisher link tooling, reporting and APIs, compliance and fraud controls, and recruitment/matching services. The Type's variants are mostly about settlement shape (tracking-fee invoicing vs retailer-of-record vs consolidated-payout service), vertical focus, publisher taxonomy breadth, regional structure, and service posture. The Type is bounded against Affiliate Management Platform (one merchant's own program vs multi-merchant intermediary — vendor-confirmed split), ad networks (per-result commissions vs per-impression media), consumer marketplaces (partner discovery vs consumer shopping), Referral Marketing (customers vs professional promoters), PRM (partner organizations vs individual promoters), and Influencer Marketing (campaign/content objects vs conversion/commission objects).
