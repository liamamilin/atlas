# Research Notes — Demand-side Platform / DSP

## Research Goal

Understand what a "Demand-side Platform (DSP)" is as an Application Type from real products: the buyer-side objects (advertiser, insertion order/campaign, line item, creative, audience segments), the per-impression trading loop the platform executes, who operates it (agencies, trading desks, in-house teams, self-serve advertisers), the money and accountability model (budgets, bids, spend reporting, billing), the rules that govern buying (targeting, deals, inventory quality, pacing), and where the boundary sits against neighboring advertising-stack Types (SSP, ad server, programmatic category, media buying platform, advertising campaign management, DMP/attribution, ABM, creative management).

This pass also discharges joint-review flags pre-hung by sibling passes: supply-side-platform-ssp (mirror pole), programmatic-advertising-platform (category vs pole), media-buying-platform (layering), advertising-campaign-management (gradient), abm-platform (primary object).

## Initial Boundary

- A DSP is hypothesized to be the **advertiser's side** of the automated digital-advertising marketplace: the platform a buyer uses to transact ad impressions automatically across many external sellers, configuring demand (budgets, targeting, bids, creatives) that the platform's own bid engine evaluates per impression.
- Nearest neighbors: SSP (mirror sell-side pole, processed), Ad Server (processed; request-time selection on managed placements), Programmatic Advertising Platform (processed; two-sided category), Media Buying Platform (processed; whole buying operation), Advertising Campaign Management (processed; per-platform campaign lifecycle), DMP/CDP (data supply), Marketing Attribution (measurement), ABM Platform (account-centric demand).
- Obvious unknowns: whether "real-time auction bidding" is definitional or the invariant is the automated per-impression transaction (deals/guaranteed buying may soften it); how far "managed service vs self-serve" and walled-garden DSPs stretch the Type; whether older first-generation DSPs fit a modern-derived definition.

## Research Questions

1. What objects does the buyer configure, and how do they nest (advertiser → campaign/insertion order → line item → creative/audience)?
2. What does the platform do per impression — what is the bid loop, who runs the auction decision, where does the win get served?
3. What demand controls exist: budget, targeting dimensions, bidding strategies, pacing, splits, frequency?
4. How does inventory reach the platform (exchanges, SSPs, networks, direct publishers; walled gardens) and how is quality handled?
5. How do audiences/data enter: pixels, first-party files, third-party providers, data marketplaces, identity frameworks?
6. What deal machinery exists from the buyer side (open exchange, PMP, preferred/fixed price, programmatic guaranteed)?
7. How does money work: budgets, cost models, seats, consolidated billing, spend/delivery reporting?
8. Who are the users and service postures (agency trading desk, in-house, self-serve, managed service)?
9. Which capabilities are era-current (CTV, identity frameworks, AI decisioning) vs structural?
10. Where are the exact seams to SSP, ad server, programmatic category, media buying, campaign management, DMP, attribution, ABM?

## Representative Products

| Product | Why sampled | Evidence tier reached |
|---|---|---|
| Microsoft Invest (Xandr) | Full-stack heritage DSP (suite also contains Monetize sell side + ad serving); deep public docs | Tier 1 — 5 official doc pages fetched 2026-09-08 |
| The Trade Desk | Largest independent buy-side-only DSP; market anchor | Tier 1/2 — positioning page fetched 2026-09-08; glossary + capability pages fetched in programmatic pass 2026-09-06 |
| StackAdapt | Self-serve independent DSP pole; mid-market agencies/brands; now repositioning as "AI advertising platform" | Tier 2 — homepage + platform page fetched 2026-09-08 |
| Basis (Centro/Basis Global Technologies) | Media-buying-suite pole with an embedded DSP; vendor-articulated DSP seam | Layer A via media-buying-platform pass (FAQ captured 2026-09-08) |
| Microsoft Monetize (Xandr) | The sell-side sibling inside the same suite; corroborates the bid loop and deal machinery | Layer A via programmatic pass (docs fetched 2026-09-06) |

Market anchors attempted but unreachable: Amazon DSP (advertising.amazon.com — 3 URL attempts, 404/JS shell, abandoned), Google Display & Video 360 (support.google.com — 2 timeouts, abandoned). DV360/Amazon DSP appear below only as market context, not as evidence.

## Sources

- Microsoft Invest — About Microsoft Invest: https://learn.microsoft.com/en-us/xandr/invest/about-invest (fetched 2026-09-08)
- Microsoft Invest — Object Hierarchy: https://learn.microsoft.com/en-us/xandr/invest/object-hierarchy (fetched 2026-09-08)
- Microsoft Invest — Ad Buying with Microsoft Advertising: https://learn.microsoft.com/en-us/xandr/invest/ad-buying-with-xandr (fetched 2026-09-08)
- Microsoft Invest — Basic Buy-side Setup Procedures: https://learn.microsoft.com/en-us/xandr/invest/basic-buy-side-setup-procedures (fetched 2026-09-08)
- Microsoft Invest — Product Documentation landing (module map: ALI Optimization, Creatives, Guaranteed Outcomes, Viewability, Planner, Reporting): https://learn.microsoft.com/en-us/xandr/invest/ (fetched 2026-09-08)
- The Trade Desk — Our Demand Side Platform: https://www.thetradedesk.com/us/our-demand-side-platform (fetched 2026-09-08)
- The Trade Desk — official glossary + programmatic-buying-solutions page (fetched 2026-09-06, recorded in research/programmatic-advertising-platform.md)
- StackAdapt — homepage https://www.stackadapt.com/ and platform page https://www.stackadapt.com/platform (fetched 2026-09-08)
- Basis DSP seam — vendor FAQ recorded in research/media-buying-platform.md (fetched 2026-09-08)
- Microsoft Monetize docs (bid loop, PG line items) — recorded in research/programmatic-advertising-platform.md (fetched 2026-09-06)

> Source-access limitation: DV360 (support.google.com) timed out twice; Amazon DSP (advertising.amazon.com) returned 404s and a JS-only shell across three paths — both abandoned per network rules. TTD's Knowledge Portal is login-walled (established in the programmatic pass). StackAdapt operational help was not fetched; its evidence stays positioning-level. Claims about walled-garden DSP operations are therefore kept out of the final document.

## Product Observations

### Microsoft Invest (Xandr) — evidence layer A (fetched 2026-09-08)

**Positioning (About):** "a strategic buying platform built for the needs of today's advertisers"; "set up managed media buys and auction-based buys using a unique interface where you can easily monitor your insertion order and line item delivery and performance"; "an end-to-end, integrated platform across the buy and sell side." Technical self-description: "a real-time bidding system and ad server."

**The trading loop (About, technical details — load-bearing):**
- Main processing system is the "impression bus": receives ad requests, applies data to the request, receives bids, makes decisions, serves creatives, logs auctions.
- Ad calls come in via supply partners: exchanges, SSPs, ad networks, "a few valued publishers." Client-side (Microsoft tag on page) or server-side (partner fields the call, asks for a bid).
- Data overlay: server-side cookie store fed by segment pixels or client data files; third-party data providers overlaid.
- "We contact all of the bidders on our platform. The ad call includes whatever user data belongs to each bidder, and information about the inventory. Bidders have a certain number of milliseconds in which to respond with a bid and the creative they want to serve."
- "Microsoft Invest serves as our proprietary bidder, which has a suite of features including targeting, bidding algorithms, multi-currency support… accessed by either a UI or API."
- Win decision: "based on the amount of the bid, and any preferences the publisher has." Client-side → platform serves the ad; server-side → platform passes the bid and creative location to the partner who serves.

**Object hierarchy (Object Hierarchy — load-bearing):**
- **Member** — the account as a whole: "who's eligible to sell to you," inventory-audit level required, domain/app allowlists and blocklists for campaigns, a cap on daily spend on third-party inventory.
- **Advertiser** — "a single client or brand on whose behalf you want to serve ads"; defaults (currency, time zone), brand + offer category applied to creatives; "many advertisers in your network."
- **Insertion order** — "a financial agreement you have with your advertiser that specifies what they would like you to execute": total budget allocated for a period, third-party verification; groups line items.
- **Line item** — "the agreed upon strategies you will be executing for the advertiser": budget toward an offering, targeting. (Setup docs: "Augmented Line Item (ALI)" with geo restrictions, inventory lists; "Configure a Programmable Split.")
- **Creative** — "the actual ad, hosted either by Microsoft Advertising or by a third-party ad server"; belongs to an advertiser; associable to many line items.
- **Segment pixel** — placed on web pages, adds users to segments; "targeted in campaigns to attempt to reach the user again (retargeting)."
- **Conversion pixel** — tracks user actions; the platform determines whether the conversion "can be 'attributed', or tied to the user clicking on or viewing one of the advertiser's creatives."
- Third-party creative pixels, impression trackers, click trackers for externally hosted creatives.

**Buying breadth (Ad Buying):** "manage both traditional media buys and real-time bidding through a single, unified interface"; "seamless integration with major ad networks, exchanges, aggregators, and SSPs"; "site list with volume and price estimates"; "no need for contracts with each publisher or exchange"; inventory quality — top domains reviewed, sensitive categories targetable; "fly-by-wire trafficking" — interface changes effective within minutes, reporting "usually available within a couple of hours" (product-stated); **seats and payment** — platform holds a seat on major exchanges by default, pays the media bill, "clients receive a single consolidated bill at the end of the month"; clients can use their own seats where technically possible, in which case the media bill comes directly from the exchange.

**Other documented modules (landing TOC):** ALI Optimization (Adaptive Pacing; improve CTR), Creatives (working with, troubleshooting, auditing), Guaranteed Outcomes (what they are, how they work, auction mechanics), Viewability (methodology; improve video viewability), Planner (create and activate a plan), Reporting (dimensions/metrics/filtering/grouping; impression counting).

### The Trade Desk — evidence layer A (self-description + glossary, per programmatic pass) / positioning (this pass)

- Self-label: "The leading demand-side platform for data-driven advertising"; "the leading independent DSP built for data-driven marketers."
- Job framing: "plan, execute, and measure your programmatic advertising campaigns, so you can maximize the value of every single impression — all within a simple self-serve experience."
- Independence claim: "Because we don't own media. We just help you buy it better" — objective/unbiased inventory prioritization; open and interoperable ("industry's largest marketplace of data, measurement, brand safety, and inventory providers"); transparency and real-time adjustment.
- Channels: omnichannel — audio, CTV/OTT, DOOH, display, mobile, native, video.
- Data/identity: first- and third-party audience targeting, "durable identity framework" (UID2, EUID, OpenPath direct-supply connection), retail data for targeting + sales/ROI linkage.
- AI decisioning (marketing-stated): "Our AI analyzes up to 15 million ad opportunities each second… optimize campaigns in real time"; Koa conversational assistant; Kokai/Zuma platform generations (L3 branding).
- Measurement: outcome-based measurement "from awareness to conversion," media spend aligned to business goals.
- (From programmatic pass, glossary — layer A): RTB, deal ID, PMP and related marketplace definitions; DSP defined as the buyer-side platform in the two-sided programmatic world.

### StackAdapt — evidence layer A (self-description) / positioning level

- Self-labels: homepage 2026 "AI Advertising Platform"; platform page "AI-powered marketing orchestration in one platform"; maintains a "Best DSP" page — DSP remains its recognized category anchor.
- Audience: "Trusted by 40,000+ brands and agencies worldwide"; FAQ: agencies manage cross-channel campaigns for clients, brands unify media and messaging.
- Channels: CTV, video, display, native, audio, DOOH, in-game, email, direct mail, ChatGPT Ads — programmatic core with owned-channel/adjacent extensions.
- Demand configuration: "Activate 1st-party audiences, leverage contextual targeting, reach key accounts with ABM targeting"; real-time forecasting ("predict impressions, reach, clicks, and conversions"); dynamic creative; Data Hub for first-party data/CRM integration; cross-channel attribution; brand lift studies (client quotes).
- Pricing models (FAQ): "CPM (cost per mille), CPC (cost per click), and CPE (cost per engagement)."
- AI layer: Ivy Studio hub; marketing-stated "465 billion optimization decisions every second."
- Self-serve posture: Forrester Wave citation highlighting self-serve capabilities; sign-up without sales contact.

### Basis (via media-buying-platform pass) — evidence layer A for the seam

- Vendor FAQ: "A demand-side platform handles programmatic media buying. Basis includes a proprietary DSP but goes much further, connecting media activation with campaign planning, team collaboration, workflow automation, financial reconciliation, and AI-powered optimization across all digital channels… It's built to serve as the operational foundation for an entire advertising organization, not just the buying function."
- DSP integrations named: TTD, MediaMath, AdForm, StackAdapt, DV360, Simpli.fi — DSP is an activation channel inside the broader buying operation.

### Microsoft Monetize (via programmatic pass) — evidence layer A, corroborating the machinery

- Bid loop documented identically on the sell-side doc set: ad calls from supply partners → data overlay → bid request to all bidders (milliseconds window) → bidder processes ("campaigns, targeting options, bidding algorithms") → Impression Bus evaluates (bid amount + publisher preferences) → winning ad served or handed back.
- Programmatic Guaranteed line items "are required to bid on every possible impression associated with the targeted PG deal" — pre-agreed price still flows through bid machinery.

## Cross-product Comparison

| Dimension | Microsoft Invest | The Trade Desk | StackAdapt | Basis (DSP module) |
|---|---|---|---|---|
| Customer | Advertisers/agencies (managed + auction buys); suite spans buy+sell | Brands and agencies; buy-side only | Brands and agencies; self-serve emphasis | Agencies/advertisers; DSP inside buying suite |
| Self-description | "strategic buying platform… real-time bidding system and ad server" | "leading independent DSP" | "AI advertising platform" (DSP page retained) | "proprietary DSP" inside platform |
| Buy-side object stack | Member → Advertiser → Insertion order → Line item (ALI) → Creative (+ pixels/trackers) | Campaign-family objects (glossary level) | Campaign workflows (positioning level) | Campaign objects (positioning level) |
| Supply access | Exchanges, SSPs, networks, publishers; "no need for contracts with each publisher or exchange" | Open internet; OpenPath direct connections | Programmatic supply across 10+ channels (positioning) | Proprietary DSP + third-party DSP integrations |
| Data layer | Segment pixels, client data files, third-party providers | First/third-party data, UID2/EUID, retail data | 1st-party Data Hub, contextual, ABM key accounts | Data/DMP modules |
| Deal machinery | Guaranteed Outcomes (module) | PMP/deal machinery (glossary) | Positioning-level | Positioning-level |
| Optimization | ALI optimization, adaptive pacing, splits | AI decisioning, Koa/Kokai | Ivy Studio AI, forecasting | AI-powered optimization |
| Money | Seats, consolidated monthly bill, multi-currency | Positioning-level | CPM/CPC/CPE models | Financial reconciliation at suite level |
| Measurement | Conversion pixels/attribution, viewability, reporting, log-level feeds | Outcome-based measurement | Cross-channel attribution, brand lift | Reporting within suite |

Stable across all sampled products: buyer-side representation; external multi-seller programmatic supply; per-impression automated transaction machinery with the platform's own bid engine; buyer-configured demand objects (budget/targeting/bid/creative); spend-and-delivery accountability feeding optimization; deal machinery from open exchange to guaranteed; audience/data ingestion; conversion measurement.

## Canonical Model — L0 / L1 / L2 / L3

### L0 — Defining Invariant (the advertiser's side of the automated ad marketplace)

Four jointly-held structures. Remove any one and the product stops being a DSP:

1. **The advertiser-side buying role of record.** The platform acts on behalf of identified advertisers/brands (registered advertiser objects, client/agency accounts) to acquire advertising for them; it never owns or represents the inventory. Evidence: Invest's Advertiser object ("a single client or brand on whose behalf you want to serve ads"); TTD's "we don't own media. We just help you buy it better"; StackAdapt serving brands and agencies. Remove → sell-side territory (SSP) or ad-network aggregation.
2. **External multi-seller inventory access through automated per-impression transactions.** The buying mechanism is the automated request/bid/response loop executed against external supply sources (exchanges, SSPs, networks, publishers) — not contracts with each publisher and not a single platform's console. Evidence: Invest ("seamless integration with major ad networks, exchanges, aggregators, and SSPs"; "no need for contracts with each publisher or exchange"; impression-bus loop); Monetize flow; TTD "every single impression." Remove → Advertising Campaign Management (per-platform consoles) or Media Buying Platform (order-based buying).
3. **Buyer-configured demand evaluated per impression by the platform's own bid engine.** A persisted object stack — budget, targeting, bids, creatives — that the platform's bidder evaluates on every opportunity, including pre-agreed deals (which still flow through the machinery). Evidence: Invest line items + "proprietary bidder… targeting, bidding algorithms"; Monetize PG line items required to bid on every deal impression. Remove → anonymous demand conduit / raw bidding infrastructure, or a campaign tracker with no trading.
4. **Outcome accountability to the buyer.** Spend, impressions, and delivery are logged and reported against the buy configuration, feeding optimization and settlement (consolidated billing, reporting, conversion feedback). Evidence: Invest reporting module, impression counting, consolidated bill; TTD outcome-based measurement; StackAdapt attribution. Remove → blind bidder.

Jointly-held is load-bearing:
- 1 alone = an ad account holder
- 2 alone = trading infrastructure (a bidder/exchange)
- 3 without 2 = campaign configuration with no programmatic execution
- 4 without 2+3 = media analytics
- 1+3 without 2 = trafficking tool with no marketplace
- 1+2 without 3 = anonymous demand pipe
- 2+3 without 1 = unattributed demand infrastructure
- 1+4 without 2+3 = advertiser-side reporting with no buying

### L1 — Common Mature Structure (standard capabilities, not definitional)

- **Audience/data layer**: segment pixels, first-party data files/CRM upload, third-party data providers, data marketplaces, retargeting, lookalike modeling, identity-framework integration
- **Deal machinery from the buyer side**: open exchange, private marketplace, preferred/fixed-price deals, programmatic guaranteed with Deal IDs
- **Targeting breadth**: geography, device, inventory allow/block lists, sensitive-category targeting, contextual, key-account lists
- **Optimization machinery**: bidding algorithms, pacing, programmable splits, AI-driven decisioning, forecasting
- **Creative management**: creative library (hosted or third-party-hosted), bulk upload, creative auditing, third-party trackers
- **Measurement**: conversion pixels with attribution, viewability, reporting dimensions/metrics, log-level data feeds, cross-channel attribution
- **Money machinery**: cost models (CPM/CPC/CPE), exchange seats, consolidated billing
- **Inventory quality**: fraud protection, inventory audits, brand-safety tooling
- **Omnichannel formats**: display, video, CTV, audio, native, mobile, DOOH
- **API surface**: management/reporting APIs, log-level data
- **Service postures**: self-serve vs managed service

### L2 — Variant / Optional Structure

- **Platform posture**: independent buy-side-only (TTD, StackAdapt) vs full-stack suite whose buying side sits beside a sell side and ad server (Microsoft Invest within Buying and Selling Platforms) vs platforms affiliated with large owned inventory pools (market context — Amazon DSP, DV360 unreachable this pass; low-precision wording only)
- **Service posture**: self-serve-first (StackAdapt) vs sales-led/managed (Invest onboarding "get in touch with a representative"; managed service teams)
- **Operator type**: agency trading desks, in-house advertiser teams, self-serve brands
- **Channel emphasis**: CTV-first, retail/commerce-data pole, DOOH/audio inclusion, owned-channel extensions (email, direct mail — StackAdapt)
- **Segment packaging**: B2B/ABM emphasis, political, regulated industries
- **Regional structure**: regional marketplaces and identity regimes vary; not directly evidenced this pass

### L3 — Vendor-specific (research notes only)

- Microsoft: Member object naming; Impression Bus; Augmented Line Items; ALI Optimization; programmable splits; Guaranteed Outcomes; Planner; "fly-by-wire trafficking" (minutes-to-effect, hours-to-report, product-stated); seat/payment model wording; multi-currency support
- The Trade Desk: Kokai/Zuma platform generations; Koa AI assistant; UID2/EUID; OpenPath; OpenTTD; "15 million ad opportunities each second" (marketing claim); Frost Radar/Gartner badges
- StackAdapt: Ivy Studio; Data Hub; "465 billion optimization decisions every second" (marketing claim); ChatGPT Ads channel; email/direct-mail channels; CPM/CPC/CPE packaging; Forrester Wave citation
- Basis: FAQ framing of DSP vs "operational foundation for an entire advertising organization"

## Rejected Findings

1. **"Real-time auction bidding is the definition" — qualified.** Pre-agreed deals (programmatic guaranteed / preferred) are documented flowing through the same per-impression machinery (Monetize PG; Invest Guaranteed Outcomes with its own auction-mechanics doc). The invariant is the automated per-impression transaction; auction price competition is its dominant form, not the whole of it.
2. **"A DSP is an ad server" — rejected as identity, retained as overlap.** Invest self-describes as "a real-time bidding system and ad server" and serves creatives client-side — but the ad-server function (selection on known placements, priorities, forecasting) is the suite's other half; the DSP's unit of work remains the external per-impression transaction. Suites bundle both roles; the Types stay distinct (consistent with ad-server pass).
3. **"DSP = all digital media buying" — rejected.** Basis's own FAQ separates the DSP (programmatic buying) from the buying platform (planning, reconciliation, collaboration). A DSP holds no cross-channel media plan of record, no insertion-order reconciliation, no vendor-bill closing.
4. **"Every campaign console is a DSP" — rejected.** Walled-garden campaign managers (search/social consoles) configure campaigns on one platform's own inventory; they do not transact external per-impression opportunities across many sellers. Where such a platform also runs an open-exchange DSP (Amazon DSP, DV360 class), the DSP module is the part that meets L0 — not directly evidenced this pass; kept as market context.
5. **"AI decisioning / identity frameworks are definitional" — rejected as era-current.** First-generation DSPs predate them; they are L1 capabilities layered on the trading loop.
6. **"Self-serve is definitional" — rejected.** Managed-service DSPs (and managed line-item operations) are a documented posture; service depth is L2.

## Boundary Findings

1. **vs Supply-side Platform / SSP (§06, processed) — mirror pole; joint review RATIFIED from this side.** Same marketplace, opposite customers and objects: the DSP's customer is the advertiser/agency and its objects are budgets, targeting, bids, creatives; the SSP's customer is the media owner and its objects are inventory, floors, deals, revenue. Remove test: strip the buyer's campaign machinery and the advertiser relationship, keep seller-side monetization → SSP; strip the seller side, keep buying → DSP. Evidence: Invest (Member decides "who's eligible to sell to you" — the DSP is a demand consumer of SSP/exchange supply) vs the SSP pass's seller-side core.
2. **vs Programmatic Advertising Platform (§06, processed) — category vs pole; DISCHARGED from this side.** The programmatic pass documented that leaf as the two-sided automated impression-trading category and asked the DSP/SSP passes to ratify the pole seams. Ratified: the DSP is the buy-side instantiation; no sampled DSP carries a separate "programmatic platform" structure beyond the pole role. The category leaf's final status (category-level Type vs alias) remains a taxonomy-owner decision already flagged there; this pass adds no contrary evidence.
3. **vs Ad Server / Ad Delivery Platform (§06, processed) — unit-of-work seam; consistent with both prior passes.** DSP's unit of work: the bid response to external opportunities across many sellers; no placement registry, no managed ad pool on known inventory. Ad server's unit: managed pool + per-request selection on known placements. Suites contain both (Invest: bidder + "premium ad server" features + Monetize ad serving).
4. **vs Media Buying Platform (§06, processed) — layered, not competing; DISCHARGED from this side per that pass's forward note.** A media buying platform may CONTAIN a DSP (Basis) and push approved line items into it; a DSP holds no cross-channel plan of record, no insertion-order/approval workflow across vendors, no vendor-bill reconciliation. Vendor-articulated seam preserved verbatim in that pass's research.
5. **vs Advertising Campaign Management (§06, processed) — gradient, as pre-hung.** Campaign management governs campaign configuration/spend/performance on named publisher platforms (its pass noted Skai officially manages Amazon DSP — an overlap zone where a campaign tool operates a DSP's console). Seam from this side: the DSP transacts impressions on open external marketplaces under its own bid engine; campaign management executes within a specific platform's buying surface. Modern DSPs exposing campaign-shaped objects (advertiser → insertion order → line item) show why the gradient is real, but the marketplace act is the DSP's center.
6. **vs DMP / Audience Management / CDP (§06) — data-supply layer.** Audience data enters the DSP as segments/files/providers (Invest: segment pixels, data files, third-party providers); the DMP/CDP is upstream supply, the DSP the buying actuator. A DSP's internal segment tooling is a capability, not the DMP Type.
7. **vs Marketing Attribution Platform (§06, processed) — feedback vs measurement of record.** DSPs track conversions and attribute them (Invest conversion pixels + attribution) as optimization feedback for their own buys; the attribution Type's center is cross-channel credit assignment across the advertiser's whole media mix.
8. **vs ABM Platform (§06/§07) — primary-object seam; DISCHARGED from this side.** The abm-platform pass flagged that the boundary is the primary object (named accounts vs anonymous audience). Evidence from this side: StackAdapt's "reach key accounts with ABM targeting" — account lists enter the DSP as one targeting input; the DSP's transacted unit remains the anonymous impression, not the account record.
9. **vs Creative Management Platform (§06, processed) — production vs delivery.** The CMP pass recorded Bannerflow's articulation: "you own the data and media… your DCO engine or DSP then applies rules… to serve the right message." Creatives are inputs to DSP buying; the DSP hosts and traffics them but does not author variant systems.
10. **vs Ad network (historical negative case).** TTD's glossary (via programmatic pass): an ad network connects advertisers and publishers by aggregating supply; aggregation + principal reselling fails L0 leg 2/3 (no buyer-configured per-impression transactions under the advertiser's configuration). The ad network is the pre-programmatic neighbor.
11. **vs Trading desk (market role, no directory leaf).** The agency trading desk is the operating organization; the DSP is its tool. No directory node conflicts.

## Historical / Market-Sample Check (§24)

- **Older products:** First-generation DSPs (circa 2009–2012, display-only RTB) satisfy all four L0 legs structurally: advertiser objects, exchange connectivity, campaign/line configuration evaluated per impression, spend/delivery reporting. No archived first-generation doc set was fetched this pass; the check is argued structurally from the fact that every capability named as era-current (CTV, identity frameworks, AI decisioning, DOOH) is absent from L0. Invest's own docs still describe the older coexistence ("traditional media buys and real-time bidding through a single, unified interface"), showing the trading core does not depend on modern machinery.
- **Regional products:** The L0 is region-neutral (identity regime, channel mix, and data rules are L2). Not directly evidenced with a regional doc set; kept as a structural claim.
- **Platform-native products:** A platform's own buying console meets L0 only where it transacts external per-impression opportunities; a console limited to its own inventory fails leg 2 and is Advertising Campaign Management. This is the boundary marker that keeps the DSP from absorbing every ad-buying surface.

## Uncertainties

1. Walled-garden DSP operations (Amazon DSP, DV360) unobserved — their inclusion as "DSPs that also own inventory" rests on market context and TTD's contrast framing, not fetched documentation.
2. TTD operational depth (Knowledge Portal) login-walled; TTD object hierarchy asserted only at glossary/capability level.
3. StackAdapt evidence is positioning-level; its console's object model was not observed.
4. Frequency capping: expected industry-standard delivery control, but not directly documented in any fetched page this pass — deliberately kept out of the final document rather than asserted from memory.
5. Exact billing mechanics (deposit/prepay vs monthly credit), fee models (percentage of spend vs CPM licensing), and pacing defaults vary and were not researched to precision.
6. The exact status of "Programmatic Advertising Platform" (category-level Type vs alias) is a taxonomy-owner decision flagged in that pass; not resolvable from this side.

## Final Synthesis

A Demand-side Platform is the advertiser's side of the automated digital-advertising marketplace. Its defining core is four jointly-held structures: (1) it acts for identified advertisers/brands and never owns the inventory; (2) it reaches many external sellers' inventory through automated per-impression transactions — exchanges, SSPs, networks, publishers — with no per-publisher contracts; (3) it holds the buyer's persisted demand configuration (advertiser → financial agreement → line items with budgets, targeting, bids, creatives) and evaluates every opportunity against it with its own bid engine, with pre-agreed deals flowing through the same machinery; (4) it records spend, impressions, and delivery against that configuration, feeding optimization and consolidated settlement. Around this core, mature products add the audience/data layer, deal machinery, optimization and AI decisioning, creative management, measurement, brand safety, omnichannel formats, APIs, and a service posture. The Type is bounded by the SSP (mirror pole), the ad server (managed-pool selection), the media buying platform (the whole buying operation that may embed a DSP), advertising campaign management (named-platform consoles), the DMP/attribution/ABM/CMP layers (data, credit, accounts, creative supply), and the historical ad network (aggregation without per-impression buyer-configured transactions).
