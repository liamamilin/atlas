# Research Notes — Programmatic Advertising Platform

## Research Goal

Understand what a "Programmatic Advertising Platform" is as an Application Type: whether it is a distinct product architecture with its own core structure, or a market-category (umbrella) term whose concrete products instantiate other named roles (DSP, SSP, exchange, ad server). Determine the core objects, the transaction loop, the users, the historical breadth, and the boundaries against the neighboring advertising-stack leaves in §06 (Demand-side Platform / DSP, Supply-side Platform / SSP, Ad Server, Advertising Campaign Management, Media Buying Platform).

This leaf carries an explicit prior: both already-processed siblings (ad-delivery-platform, ad-server) recorded the judgment "Programmatic Advertising Platform — umbrella/marketing term spanning DSP + SSP + exchange + data; no distinct structure of its own." This pass tests that judgment independently.

## Initial Boundary

- **Hypothesis (pre-research):** "Programmatic advertising" names a buying/selling *method* (automated, auction-based trading of ad impressions), not a product shape. A "programmatic advertising platform" is any platform whose primary job is executing that method — which decomposes into buy-side (DSP), sell-side (SSP), auction venue (exchange), or combined suites.
- **Nearest Types:** Demand-side Platform / DSP; Supply-side Platform / SSP (both unprocessed §06 siblings); Ad Server (processed); Advertising Campaign Management (processed); Media Buying Platform (unprocessed sibling); Data Management Platform / DMP.
- **Initial unknowns:** Do any products self-identify as "programmatic advertising platform" with a structure that is neither DSP nor SSP? Is the per-impression auction definitional, or does programmatic-guaranteed (fixed-price) volume break that? Does the category have its own object model or only the two poles' models?

## Research Questions

1. What does "programmatic" mean operationally in official documentation (vs marketing usage)?
2. How do market products self-describe — as "programmatic advertising platforms", or as DSP/SSP/ad server/advertising-automation platforms?
3. What is the buy-side object model (advertiser → campaign → …) and its transaction loop?
4. What is the sell-side object model (publisher → inventory → deals) and its transaction loop?
5. What deal/access types exist (open exchange, PMP, preferred/fixed price, programmatic guaranteed) and are they shared machinery across poles?
6. What rules govern the auction (floors, ask prices, deal priority, first/second price)?
7. Where do the boundaries run: vs ad server (request-time selection on managed placements), vs campaign management (walled-garden publisher platforms), vs DMP, vs ad network (historical negative case)?
8. Historical/market-sample check: would era-earlier exchanges and non-US programmatic markets fit the same definition? Does the ad network fail it?

## Representative Products

Selection: market anchors from each pole + the two products most associated with the "programmatic advertising platform" self-label + one full-stack suite whose docs are publicly reachable. Six products, five poles/roles, three customer tiers.

| Product | Role in sample | Why selected |
|---|---|---|
| Microsoft Monetize (Xandr) | full-stack suite (buy + sell + ad server) | its official docs explicitly use "programmatic advertising" as the platform's own description; learn.microsoft.com reachable (Tier 1) |
| The Trade Desk | buy-side market anchor (DSP) | largest independent DSP; public glossary + capability pages (Tier 1/2) |
| StackAdapt | buy-side, mid-market/agency; historically self-labeled "programmatic advertising platform" | shows how the phrase was used as a category self-label and how it is drifting |
| Basis (Centro) | buy-side + advertising automation suite; SMB/mid-market | second historical "programmatic platform" self-label; DSP as one named module |
| Magnite | sell-side market anchor (SSP-led) | largest independent sell-side company; both-seller-and-buyer posture |
| PubMatic | sell-side with buyer tools | second SSP anchor; public documentation portal |

## Sources

- Microsoft Monetize (Xandr) official docs on Microsoft Learn: About Monetize; Buying Guide; Buying Deals; Deal Auction Mechanics; Programmatic Guaranteed Buying Line Items — learn.microsoft.com/en-us/xandr/monetize/* (fetched 2026-09-06)
- The Trade Desk official site: homepage, our-demand-side-platform, programmatic-buying-solutions, glossary (fetched 2026-09-06)
- StackAdapt official site: homepage, best-demand-side-platform-dsp (fetched 2026-09-06)
- Basis official site: basis.net homepage (fetched 2026-09-06)
- Magnite official site: homepage, sellers page (fetched 2026-09-06)
- PubMatic official site: homepage (fetched 2026-09-06)

Limitations: The Trade Desk's detailed product documentation ("Knowledge Portal") and Magnite/PubMatic help centers were not fetched this pass (login-walled or not attempted within budget); buy-side operational depth relies on Microsoft Learn (fully reachable) plus TTD/StackAdapt public pages. Google Display & Video 360 and Amazon DSP were not sampled (their help centers were unreachable for the advertising-campaign-management sibling the same day; avoided repeat). No numeric limits, fees, or timing windows are asserted anywhere below beyond what fetched pages state.

## Product Observations

### Microsoft Monetize (Xandr) — full-stack suite (evidence layer A)

- Positioning (About Monetize): "Microsoft Monetize is a web-based application for your programmatic advertising. Whether you're buying or selling ad space, or both, Monetize provides all the tools that you need to manage your accounts." — the platform's own docs treat "programmatic advertising" as covering both sides.
- Buyers: "Monetize can manage both traditional media buys and real-time bidding through a single, unified interface. Instead of operating an ad server and a buying platform, Monetize can perform both functions." Single-point access to "programmatic buying features"; "direct and managed media buys and auction-based buys through one simple interface"; site lists with volume/price estimates; fraud/inventory-quality protections; no per-publisher contracts.
- Sellers: set up publishers and traffic campaigns on managed inventory; "resell inventory on the Microsoft Advertising platform"; optimization for direct campaigns; per-publisher ad quality requirements.
- Named roles inside the suite: "Ad server" is an explicit role ("set up publishers and available inventory, as well as advertisers and their selling specifications … manage forecasting, priorities"); there is a distinct "buying platform"/bidder and selling machinery.
- Documented process flow (About Monetize): ad calls from supply partners (exchanges, SSPs, networks, publishers) → data overlay (server-side cookie store, segment pixels, data files, third-party data) → bid request sent to all bidders with a limited response window ("milliseconds") → proprietary bidder processes the request ("campaigns, targeting options, bidding algorithms"; UI or API) → Impression Bus evaluates bids (bid amount + publisher preferences) → winning ad served client-side or handed back to the partner.
- Buy-side object model (Buying Guide): **Advertiser → (Insertion Order) → Line Items → Campaigns**. Line item = the financial agreement (budget, revenue type, advertiser goals). Campaign = media budget, buy type (direct/third-party/both), buying strategies (how to bid), targeting. Augmented Line Items fold campaign settings into the line item. Programmable splits = rulesets allocating delivery/budget to specific segments.
- Buy-side machinery: budgeting and pacing ("control the frequency with which the system attempts to win impressions in order to spend a budget as evenly as possible"); creatives (hosted or third-party-tracked); segments (pixel-assigned user groups); conversion pixels with attribution; impression/click trackers; deal lists; deal targeting; viewability; mobile/video/audio/native inventory guides; data marketplace (auto-cleared third-party segment data).
- Deals (Buying Deals): "A deal is an agreement between a buyer and a seller that provides special access to inventory and/or data." Buyers can kick off negotiations; deal lists at member and advertiser level; buy-side deal reporting.
- Deal auction mechanics (Deal Auction Mechanics page, first-price basis): deals can be **open** or **private** auctions; private deals can carry numeric **deal priority** (higher always wins over lower); **fixed price** deals (winning buyer pays ask price; bids below ask ineligible); ask price vs reserve price precedence ("deal prices take priority over floor prices"); yield-management floors with reserve-price-override rules.
- Programmatic Guaranteed (PG): "PG deals bring the targeting, messaging, and reporting benefits of programmatic advertising to guaranteed media buys… an automated solution for getting guaranteed access to media." PG buying line items "transact (bid) on sellers' PG deals"; targeting/budgeting/frequency determined by the deal, not the buyer; billing capped at booked impressions ("you'll never pay for more than a deal's agreed-to number of booked impressions"); auto-monitoring deactivates the line item when its bid rate drops (line item switches to Inactive). — Direct evidence that guaranteed programmatic volume still flows through the bid/request machinery.

### The Trade Desk — buy-side anchor (evidence layer A for self-description + glossary, B for operational detail)

- Positioning: "The leading independent DSP built for data-driven marketers"; "our advertising platform"; platform capabilities list includes a distinct "Programmatic buying solutions" page.
- Glossary (official, vendor-maintained industry definitions):
  - **DSP**: "An ad platform that helps advertisers buy ads through real-time bidding exchanges. By using a DSP, advertisers can manage multiple ad exchange accounts and automatically optimize the bidding process through a single interface."
  - **SSP**: "A technology company that enables publishers to manage and automate the selling of their ad inventory so they can generate the maximum amount of revenue per ad impression."
  - **Ad exchange**: "A service that connects publishers, advertisers, and DSPs and conducts an auction among bidders per impression."
  - **RTB**: "The buying and selling of ad impressions in an ad exchange. In RTB, auctions are automated and occur within milliseconds. During this time, the ad exchange invites advertisers to bid on an impression through DSPs, and the winning bid's ad is served."
  - **Bid request** (SSP→DSP signal with impression details) / **bid response** (DSP→SSP with price and creative specs).
  - **Buy side**: "advertisers, agencies, DSPs, and DMPs. Also known as demand side." **Sell side**: "publishers and supply-side platforms. Also known as supply side."
  - **Private marketplace (PMP)**: "An auction that requires an invitation (typically in the form of a deal ID) to access. PMPs combine the auction environment of real-time bidding with the buyer-seller relationship of direct buys."
  - **Deal ID**: unique number matching buyers and sellers on pre-negotiated criteria. **Contract groups** group PMP contracts; **delivery profiles** apply permissions across contracts; **deal quality score** compares deal value vs open market.
  - **Campaign**: "A strategy for purchasing ad inventory that is driven by goals, or KPIs… set budget for a set period of time." **Ad group**: strategy within a campaign assembling targeting, budgets, creatives, site lists. **Base bid / bid factors / max bid** bidding mechanics. **AutoAllocator** budget optimization (Koa). **Forecasted spend**. **Frequency capping**. **Dayparting**.
- "Programmatic buying solutions" page: audience-first strategy, bid factors ("express what you value through bid factors to guide your optimizations — or let Koa optimize for you"), real-time forecast before changes go live, "Access premium inventory… Target the Sellers and Publishers 500+".
- Glossary "Decisioning": "Refers to the power advertisers have to make decisions on who, where, when, what, and how to spend. Programmatic advertising increases advertisers' decisioning power." — the vendor's own framing of what "programmatic" gives the buyer.
- Kokai / Koa AI platform layer (named, vendor-specific).

### StackAdapt — buy-side mid-market (evidence layer A)

- 2026 homepage positioning: "AI Advertising Platform"; "The AI platform for every stage of advertising… connects planning, audiences, creative, channels, and measurement into one intelligent platform." (Historically the company's standing self-label was "the #1 programmatic advertising platform"; today the phrase survives in its published report title "The State of Programmatic Advertising 2026" and blog vocabulary, not as the homepage label.)
- Category anchor: "Leading DSP trusted by agencies and brands… the DSP of choice for mid-size and large agencies across North America"; G2 category "Demand-Side Platform (DSP)"; competitive set in the same grid: Simpli.fi, Basis, The Trade Desk, Google Marketing Platform, Criteo, Viant, Nexxen, Roku OneView, MediaMath, Yahoo AdTech DSP…
- FAQ defines the category it competes in: "A demand-side platform (DSP) is a software that enables advertisers to serve their digital ads on multiple publishers, across different advertising channels… consolidating inventory into a single platform…" and "The key benefit of a DSP is the ad-buying process, providing advertisers multi-channel reach from a single programmatic platform."
- Channels: CTV, video, display, native, audio, DOOH, email, direct mail, in-game, ChatGPT ads. Solutions: Creative Studio, Client Services, Cross-Channel Attribution, Enterprise API ("StackAdapt API"), Data Hub, partner integrations. Ivy Studio AI hub (vendor-specific).
- Reader quotes use the trade vocabulary: "Director of Programmatic… I love using StackAdapt for programmatic campaigns…"

### Basis (Centro) — buy-side + advertising automation (evidence layer A)

- Positioning: "Advertising Automation Platform for Omnichannel Media"; "Basis Platform — Advertising Operating System."
- A distinct named product line inside the suite: "**Demand Side Platform** — Top-Ranked DSP", with DSP features (cross-device targeting, brand safety & fraud protection, private marketplaces, DMP solutions) and DSP channels (audio, CTV, display, DOOH, native, video). So the DSP is a module of a wider automation suite that also covers planning, communication, billing, and dashboards.
- "Bring together search, social, programmatic, CTV, and site direct via Basis' straightforward API" — "programmatic" appears as one acquisition family among several channels; "Integrations — Partners Beyond Programmatic"; "Enterprise API — Custom Programmatic Solutions."
- Digital Advertising Automation modules: automated planning / performance / measurement / billing (vendor-specific suite framing).

### Magnite — sell-side anchor (evidence layer A)

- Positioning: "The Largest Independent Sell-Side Advertising Company"; "Magnite is the modular ad platform media owners rely on to drive durable revenue, and buyers & agencies trust to curate premium inventory across every screen."
- Seller product lines: **SpringServe** video platform ("combining ad serving, mediation, and programmatic into one powerful solution"; "the best of an ad server and SSP in one platform"; "manage all your demand in one interface, including direct, programmatic, OpenPath, and Magnite ClearLine"); **DV+ Supply-Side Platform** (display, online video, audio, native, DOOH; "AI-powered, outbound traffic shaping and floor price recommendations"); **Demand Manager** (header-bidding wrapper management; Prebid.org co-founder); **Mobile In-App SDK**; **Deals & Marketplaces** ("robust Programmatic Guaranteed (PG), Private Marketplaces (PMP), Auction Packages, and curated marketplaces… Package premium inventory for strategic buyers to deliver pre-negotiated rates, volume commitments"); **Magnite Access Audience Suite** (identity, DMP integration, first/third-party data activation, GDPR/CCPA/TCF alignment); **Demand Facilitation** (human team connecting sellers to agencies/DSPs).
- Buyer-facing line exists too (Buyers nav; "Magnite, for Buyers" appears in the G2 DSP grid).
- Login surfaces: DV+ (platform.rubiconproject.com), Streaming, SpringServe consoles; Magnite Help Center exists (help.magnite.com) but was not fetched this pass.

### PubMatic — sell-side with buyer tools (evidence layer A)

- Positioning: "PubMatic is the leading AI-powered ad tech company delivering measurable advertising performance through an intelligent, unified platform that connects buyers, publishers, data partners, and commerce media across CTV, mobile app, and omnichannel environments."
- Product names: **PubMatic SSP** — sold separately "for publishers" and "for buyers"; **Connect**; **Identity Hub**; **OpenWrap** (header bidding, plus OpenWrap SDK); **Activate**; **Auction Packages** (curated inventory packages, e.g. MLB live-sports package); **Convert** (commerce media); **AgenticOS** ("the first operating system that lets AI agents plan, execute, and optimize media").
- Two login consoles: Publishers (apps.pubmatic.com/publisher/) and Media Buyers (apps.pubmatic.com/mediaconsole/). Documentation portal at help.pubmatic.com (not fetched this pass).
- Scale figures on homepage (2.7T advertiser bids/day, 1028B daily impressions) are vendor marketing numbers — recorded here as positioning only, not used as evidence of structure.

## Cross-product Comparison

| Dimension | Monetize (Xandr) | The Trade Desk | StackAdapt | Basis | Magnite | PubMatic |
|---|---|---|---|---|---|---|
| Primary pole | full-stack (buy + sell + ad server) | buy (DSP) | buy (DSP) | buy (DSP inside automation suite) | sell (SSP-led) | sell (SSP with buyer products) |
| "Programmatic" usage | platform's own description ("web-based application for your programmatic advertising") | capability page + glossary method terms | former homepage self-label, now report/blog vocabulary | one channel family inside the suite | tag/product vocabulary | search topic + case-study vocabulary |
| Tradeable unit | impression (bid request per impression, ms window) | impression ("auctions… within milliseconds") | impression (DSP FAQ) | impression (DSP module) | impression (auction packages, PG) | impression (2.7T bids/day positioning) |
| Buy-side structure | Advertiser → IO → Line Item → Campaign; ALI variant | Campaign → Ad group; base bid × bid factors; AutoAllocator | campaign objects (public pages); self-serve | DSP module w/ PMP + DMP features | buyer tools (secondary) | buyer console + SSP-for-buyers |
| Sell-side structure | publishers, reselling, ad quality, YM floors | sellers.json sellers, SP500+ curated supply | — | — | publisher inventory, DV+ SSP, SpringServe mediation | publisher console, SSP, OpenWrap |
| Deal machinery | open/private/fixed-price; deal priority; PG w/ booked impressions + auto-deactivation | PMP, Deal ID, contract groups, deal quality score | (not detailed on public pages) | private marketplaces feature | PG, PMP, Auction Packages, curated marketplaces | Auction Packages, SSP deals |
| Auction rules | first-price basis documented; ask price > reserve; YM floors | first- vs second-price defined; floor price | — | — | floor price recommendations | — |
| Data layer | segment pixels, data files, third-party data marketplace | data segments/marketplace, DMP defined, UID2/OpenPath | Data Hub, contextual | DMP solutions feature | Access Audience Suite, DMP integration | Identity Hub, data partners |
| AI layer | bidding algorithms | Kokai / Koa (named) | Ivy Studio (named) | Basis AI / Compass (named) | traffic shaping, Intelligent assistance | Intelligent Yield, AgenticOS (named) |
| Formats | display, video, CTV, audio, native, mobile | audio, CTV, DOOH, display, mobile, native, video | CTV, DOOH, email, direct mail, audio, video, native, display, in-game, ChatGPT | audio, CTV, display, DOOH, native, video | CTV/OTT streaming, display, video, audio, native, DOOH, mobile | CTV, mobile app, omnichannel, commerce media |
| Customer tier | enterprise | enterprise | mid-market/agency, self-serve option | SMB/mid-market, managed option | enterprise publishers | enterprise publishers + buyers |

### Convergent findings (evidence layer B unless noted)

1. **Two-pole role vocabulary is universal.** Every sampled product positions itself relative to the buy side (advertisers/agencies/DSPs) or sell side (publishers/SSPs); full-stack products contain both. TTD's glossary and Monetize's docs define the same two-sided world independently.
2. **The impression is the tradeable unit, transacted through an automated per-impression request/response loop.** Bid request → bid response → evaluation → winner → serving is documented at Monetize (A) and defined identically in TTD's glossary (A); PubMatic's and Magnite's products presuppose it. Even Programmatic Guaranteed flows through the bidding machinery (Monetize PG line items "are required to bid on every possible impression associated with the targeted PG deal") — the price may be pre-agreed but the transaction path is not hand-trafficking.
3. **Deal machinery is shared, named, and standardized across poles.** Open exchange / private marketplace (PMP) / preferred or fixed-price / programmatic guaranteed appears in Monetize (A), TTD glossary (A), Magnite (A), PubMatic (A, auction packages), Basis (feature). Deal ID as the interoperable key (TTD glossary).
4. **The category label is drifting, the roles are not.** Products once marketed as "programmatic advertising platforms" (StackAdapt; Basis's predecessor marketing) now lead with newer labels (AI advertising platform; advertising operating system) while anchoring to the DSP category; the category's competitive sets (G2 grids) are organized by pole role (DSP category), not by "programmatic platform".
5. **Convergence at both poles.** SSPs build buyer products (Magnite buyers line; PubMatic SSP-for-buyers; "Magnite, for Buyers" in the DSP grid); DSPs market premium-supply access and curation (TTD SP500+). Full-stack suites merge ad server + buying + selling (Monetize; SpringServe "best of an ad server and SSP in one platform").
6. **Data and measurement layers attach to both poles.** Segments/data marketplaces (Monetize), data elements/segments (TTD), audience suites (Magnite, PubMatic), DMP modules (Basis); conversion tracking/attribution is standard buy-side machinery.
7. **AI optimization is now a named layer everywhere** (Kokai/Koa, Ivy Studio, Compass, AgenticOS, Intelligent Yield) — but as product names, not structure (L3).

## Canonical Model

### L0 — Defining Invariant (category-level, deliberately small)

A programmatic advertising platform is a platform whose job is the automated, per-impression transaction of digital advertising inventory between buyers and sellers:

1. **Tradeable impressions** — advertising inventory is exposed as individually transactable impressions (auction-eligible), not as pre-committed, hand-trafficked placements.
2. **Automated transaction loop** — each impression opportunity triggers an automated request/response cycle (bid request → bids → evaluation → winner) under platform-executed rules; the price may be auctioned or pre-agreed (fixed-price/guaranteed deal), but the transaction machinery is the platform's, not manual insertion-order trafficking.
3. **Two-sided participation** — buyers acting for advertisers (campaign with budget, bidding, targeting) and sellers acting for inventory owners (supply with pricing/access rules) both configure and are accountable to the platform.
4. **Recorded transaction outcomes** — won impressions/spend are logged and feed reporting, pacing, and billing.

Remove the per-impression automated transaction (only scheduled fixed placements) → not programmatic (that is the direct-sold/ad-server world). Remove the two-sided trade (no buyers or no sellers participating in a market) → not this category. Remove accountability (no recorded outcomes) → not an advertising trading system.

### L1 — Common Mature Structure

- Omnichannel format coverage (display, video, CTV, audio, native, mobile in-app, DOOH — sometimes email/direct mail/in-game as adjacent "programmatic" channels)
- Deal machinery depth: open exchange, PMP/private auction, preferred/fixed-price deals, programmatic guaranteed with booked-impression billing
- Buy-side control machinery: budgeting, pacing, bidding strategies (base bid/bid factors/algorithms), frequency capping, dayparting, optimization
- Sell-side yield machinery: floor prices/reserve rules, yield-management rules, packaging (auction packages), demand facilitation
- Audience/data layer: segment management, first/third-party data marketplaces, identity/identifier solutions
- Brand safety / inventory quality / fraud protection
- Conversion tracking and attribution
- Reporting/analytics (delivery, spend, deal health) and forecasting
- Management and reporting APIs; self-serve consoles for both sides
- Roles/scoping (advertiser users, member-level and account-level separation)

### L2 — Variant / Optional Structure

- Pole emphasis: buy-side-first (DSP) vs sell-side-first (SSP) vs balanced full-stack suite
- Header bidding / wrapper products (Prebid ecosystem) vs server-side paths; direct supply connections (OpenPath-style)
- Channel specialization (CTV/streaming-first, audio, DOOH, in-game, retail/commerce media)
- Identity strategy (UID2/EUID, identity hubs, contextual fallback)
- Self-serve vs managed-service operating models; agency vs brand direct as primary customer
- Regional/market regime differences (including non-Western programmatic ecosystems)
- AI/agentic operating layers (vendor-specific today)
- Commerce-media extensions (sponsored-product style buying through the same rails)

### L3 — Vendor-specific Structure (research notes only)

- Monetize: Impression Bus, Augmented Line Items, programmable splits, Sherlock deactivations, member-level constructs
- TTD: Kokai, Koa, Ad groups/base bid × bid factors, AutoAllocator, Sellers and Publishers 500+, OpenPath, UID2, deal quality score, expressiveness metric
- StackAdapt: Ivy Studio, Data Hub, ChatGPT Ads channel
- Basis: Compass AI, Communication Portal, Unify by Basis, Basis Assistant
- Magnite: DV+, SpringServe, ClearLine, Demand Manager, Access, streamr.ai, Orchestration (agentic)
- PubMatic: OpenWrap, Connect, Activate, Convert, AgenticOS, Intelligent Yield
- G2 grid memberships and scores (market-structure corroboration only)

## Rejected Findings (over-fit candidates examined and rejected)

1. **"Real-time auction competition is definitional" — qualified.** Programmatic Guaranteed trades at pre-agreed fixed terms yet is documented as flowing through the same bid machinery (Monetize PG line items must bid on every deal impression). The invariant is the automated per-impression transaction machinery, not necessarily price competition. (If even the machinery is removed — insertion-order + ad-server trafficking only — the activity leaves the category.)
2. **"Open-exchange access is definitional" — rejected.** Deals/PMP/PG are mature, first-class structures in every sampled product; open exchange is one access tier, not the definition.
3. **"Programmatic = DSP" — rejected as the whole story.** True for buy-side-instantiated products (TTD, StackAdapt, Basis) but the sell-side products (Magnite, PubMatic) are equally "programmatic advertising platforms" in market usage, and Monetize uses the phrase for a both-sides suite. The category is two-sided.
4. **"'Programmatic advertising platform' is a stable product self-label" — rejected.** The two products historically using the phrase as self-label have both moved to newer positioning while anchoring to the DSP category; no sampled product currently leads with the phrase as its architecture description. It is market-category language (cf. report titles: "The State of Programmatic Advertising").
5. **"Header bidding is definitional" — rejected.** It is a supply-side technique variant (L2); products work without it.
6. **"Omnichannel breadth (email, direct mail, DOOH, in-game) defines the modern platform" — rejected.** Channel extension is L1/L2; a display/video exchange of the 2010s satisfies L0.

## Boundary Findings

1. **vs Demand-side Platform / DSP (§06 sibling, unprocessed)** — the DSP is the buy-side instantiation of this category: same transaction loop, buyer-side objects only (no publisher/supply registry, no floors). Test: strip the sell-side pole (sellers/floors/packaging) → a DSP. The DSP leaf and this leaf are in a pole-of-category relationship, not two independent Types. Joint review required because both leaves exist in the directory.
2. **vs Supply-side Platform / SSP (§06 sibling, unprocessed)** — mirror case: the SSP is the sell-side instantiation. Strip buyers/campaign machinery, keep inventory packaging/floors/deals → SSP. Same joint-review requirement.
3. **vs Ad Server (§06, processed)** — sharpest structural seam: the ad server's unit of work is selection from a managed ad pool on known placements; the programmatic platform's unit of work is the transaction on external/aggregate impressions. The seam is bridged in practice: ad servers take "programmatic backfill"; suites contain both roles (Monetize); SpringServe markets "the best of an ad server and SSP in one platform." The boundary holds at the unit-of-work level but is consciously porous at suite level.
4. **vs Advertising Campaign Management (§06, processed)** — campaign management governs campaigns executed on specific publisher platforms (walled gardens: their consoles, their auction); programmatic platforms transact on the open marketplace/deal layer across many sellers, with the seller relationship mediated by the platform rather than owned by the publisher's console. (Corroboration: the campaign-management sibling documented exactly this split.)
5. **vs Media Buying Platform (§06 sibling, unprocessed)** — media buying is the whole buying operation (planning, negotiation, insertion orders, reconciliation across all channel types incl. non-programmatic); programmatic platforms are the trading infrastructure for the programmatic subset. Basis illustrates the layering: an "advertising operating system" (media-buying breadth) containing a DSP module (programmatic trading).
6. **vs Data Management Platform / DMP (§06 sibling)** — data supply vs transaction machinery; DMPs are attached data layers (every sampled platform integrates DMPs or ships an equivalent module), not the trading system itself.
7. **Ad network as historical negative case** — TTD's glossary: "A company that connects advertisers with publishers by matching a supply of ad inventory with a demand for ad placement." Aggregation without per-impression automated transactions = not this category. The ad network is the pre-programmatic neighbor that fails L0 by design — useful as the boundary marker on the historical axis.

### The "remove-what" tests

- Remove the automated per-impression transaction loop → ad server + insertion orders (direct-sold world).
- Remove the sell-side participation → DSP.
- Remove the buy-side participation → SSP.
- Remove the market/many-buyers-many-sellers aspect, keep one seller's own placements → ad server.
- Remove the trading focus and widen to planning/ops/billing across all channels → media buying platform / advertising automation suite.

## Historical / Market-Sample Check (§24)

- **Early ad exchanges (pre-DSP era, e.g. 2007–2010 vintage)** — auction venue conducting per-impression auctions among bidders, with publisher floors: satisfies L0 without audience data marketplaces, AI, or omnichannel breadth. Fits.
- **Regional programmatic ecosystems (e.g., China's exchange-centric stacks)** — structurally the same two-sided impression trading with local identity/data regimes; L0 holds, L2 differs. (Recorded conceptually; not document-fetched this pass.)
- **Ad networks** — fail L0 deliberately (no per-impression automated transaction); they are the pre-programmatic neighbor, not an era variant of it.
- **Conclusion:** L0 does not over-fit the current omnichannel-AI era. The definition is anchored to the transaction mechanism, which is the category's stable core across its ~15-year history.

## Uncertainties

1. Detailed operational documentation for TTD (Knowledge Portal), Magnite, and PubMatic help centers was not fetched this pass; sell-side operational depth rests on Monetize docs + Magnite/PubMatic product pages. Claims about sell-side consoles are calibrated to positioning-level for those two vendors.
2. Google DV360 and Amazon DSP were not sampled (help centers unreachable for the sibling pass the same day); their absence does not affect the two-pole conclusion but leaves the walled-garden-adjacent end of the spectrum thinner.
3. Whether the directory ultimately wants this leaf as an independent Type, a category-alias note, or a merge into DSP/SSP is a taxonomy-owner decision; this pass documents the category honestly and flags the issue (see STATUS.md Boundary Issues).
4. The claim "StackAdapt formerly self-labeled 'programmatic advertising platform'" rests on general market knowledge of its prior positioning plus current-page evidence of the phrase's residual use; today's fetched pages lead with "AI Advertising Platform" and "Leading DSP."

## Final Synthesis

"Programmatic Advertising Platform" is the market-category name for the layer of digital advertising infrastructure through which ad inventory is transacted programmatically: inventory exposed as individually tradeable impressions, transacted through an automated per-impression request-and-bid loop (auction or pre-agreed deal machinery), between buyers configured on the advertiser side (campaigns, budgets, bids, targeting) and sellers configured on the inventory-owner side (supply, pricing floors, deal access), with every won impression logged to feed reporting and billing. The category has two canonical product poles — the demand-side platform (buy side) and the supply-side platform (sell side) — plus the exchange venue and full-stack suites that contain both; no sampled product carries a distinct "programmatic platform" architecture beyond these roles. The label functions as category language (in report titles, capability pages, and trade vocabulary) rather than as a product architecture name, and products that once used it as a self-label have moved to role-anchored or newer positioning. The leaf is best documented as this two-sided transaction category, with explicit joint-review flags to the DSP and SSP sibling leaves.
