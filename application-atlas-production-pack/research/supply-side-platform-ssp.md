# Research Notes — Supply-side Platform / SSP

## Research Goal

Understand what a "Supply-side Platform / SSP" is as an Application Type: the sell-side pole of the automated digital-advertising marketplace. Determine the core objects (inventory owners, inventory hierarchy, demand sources, floors, deals), the per-impression transaction loop as seen from the seller's side, the users, the historical breadth of the definition, and the boundaries against the neighboring advertising-stack Types in §06 (Demand-side Platform / DSP, Ad Server, Programmatic Advertising Platform, Advertising Campaign Management, Media Buying Platform, DMP) plus the historical ad network.

This leaf carries two explicit priors from already-processed siblings:

1. **ad-server + ad-delivery-platform passes**: "the SSP packages and sells inventory (deals, packages, payment rules, buyer eligibility, reselling exposure); request-time selection is the ad server's job. Remove selection, keep selling machinery → SSP."
2. **programmatic-advertising-platform pass**: "the SSP is the sell-side instantiation of the two-sided programmatic category. Strip buyers/campaign machinery, keep inventory packaging/floors/deals → SSP. Joint review required because both leaves exist in the directory."

This pass tests the SSP on its own terms (not merely as "the category minus buyers") and completes the sell-side half of the joint review.

## Initial Boundary

- **Hypothesis (pre-research):** An SSP is the media owner's platform for selling advertising inventory automatically to external demand: it registers the seller and their inventory, exposes each ad opportunity to multiple demand sources through an automated request/bid loop, enforces the seller's monetization rules (floors, buyer access, deal terms), and reports revenue back to the seller.
- **Nearest Types:** Demand-side Platform / DSP (§06 sibling, unprocessed — mirror pole); Ad Server (processed); Programmatic Advertising Platform (processed — category umbrella); Advertising Campaign Management (processed); Media Buying Platform (unprocessed sibling); Data Management Platform / DMP (unprocessed sibling); historical ad network (not in directory — negative case).
- **Initial unknowns:** Is the per-impression automated loop definitional, or do guaranteed/direct deal paths break it? Is "multiple demand sources" definitional or just the common shape? Where exactly does the SSP end and the ad server begin in products that bundle both? Do resellers (media owners selling inventory they don't own outright) fit the seller definition? Does the exchange venue survive as a separate role or has the SSP absorbed it?

## Research Questions

1. How do sell-side products self-describe — as "SSP", "supply-side platform", "exchange", or something else?
2. What is the sell-side object model: how is the seller and their inventory represented (hierarchy, ad units, supply domains)?
3. What is the transaction loop from the seller's side: what happens when an ad opportunity occurs, and what does the platform send to demand?
4. What seller-controlled rules exist: floors/reserve prices, buyer allow/block, ad quality, creative review?
5. What deal/access machinery exists: open exchange, private marketplace, preferred/fixed price, programmatic guaranteed, packages/curated marketplaces?
6. How is revenue accounted and reported back to the seller (fill, price, buyer attribution, payment basis, take rates)?
7. What integration shapes exist: tags/SDKs, OpenRTB inbound from publisher ad servers, header-bidding wrappers, resellers?
8. Where do the boundaries run: vs DSP (mirror), vs ad server (selection vs selling), vs ad network (agency vs principal), vs exchange (agent vs venue), vs programmatic category (pole vs umbrella)?
9. Historical/market-sample check: would the first-generation "yield optimizer" SSPs (pre-header-bidding, pre-CTV) fit the definition? Does the ad network fail it? Does a publisher ad server with direct-sold-only fail it?

## Representative Products

Selection: the two sell-side market anchors (also sampled by the programmatic pass, giving cross-pass corroboration) + two independent pure-play SSPs with different philosophies + one mobile-first SSP for format/customer-tier breadth. Five products, four product philosophies, three customer tiers.

| Product | Role in sample | Why selected |
|---|---|---|
| Magnite | sell-side market anchor; suite of sell-side product lines (DV+ SSP, SpringServe, Demand Manager, ClearLine) | largest independent sell-side company; public help-center glossary with deep operational vocabulary (Tier 1) |
| PubMatic | second sell-side anchor; publisher console + buyer tools + wrapper product | public documentation portal (Tier 1 root; deep docs login-walled — see Limitations) |
| Index Exchange | independent pure-play SSP/exchange; transparency-and-standards philosophy | public Knowledge Base organized by audience incl. Media Owners (Tier 1); co-author of ads.txt/sellers.json standards |
| OpenX | independent pure-play SSP; self-labels "The Intelligent SSP™" | four named product lines (Select/Build/Control/Exchange) show how the SSP role decomposes (Tier 2) |
| Verve (Smaato SPX) | mobile-first SSP pole; app-developer customer tier | SDK-first integration, mobile/CTV/web; formerly Smaato, rebranded under Verve Group (Tier 2) |

## Sources

- Magnite official site: homepage, Sellers page (magnite.com, magnite.com/sellers/) — fetched 2026-09-08
- Magnite Help Center: help.magnite.com/help (structure: DV+, Demand Manager, Magnite Buyers, ClearLine; quick-start guides; deals walkthrough; ad source walkthrough; ad quality guidelines; inventory health; reporting glossary) and help.magnite.com/help/glossary (full public glossary) — fetched 2026-09-08
- PubMatic Help portal root: help.pubmatic.com (Publisher / Activate / Buyer / Commerce Media / OpenWrap sections) — fetched 2026-09-08; deeper docs (help.pubmatic.com/publisher/, /openwrap/) redirect to login — not accessible
- Index Exchange official site: homepage, solution/publishers/, platform/programmatic-deals/ — fetched 2026-09-08
- Index Exchange Knowledge Base: kb.indexexchange.com/Home.htm, publishers/getting_started_for_publishers.htm, publishers/pmp/create_a_pmp_deal.htm — fetched 2026-09-08
- OpenX official site: openx.com homepage (product lines OpenXSelect/OpenXBuild/OpenXControl/OpenXExchange; publisher/advertiser/partner audiences) — fetched 2026-09-08
- Verve Group (Smaato) official site: verve.com publisher pages ("Brand+ Marketplace (formerly Smaato)"; mobile app / CTV / web monetization; technical specifications) — fetched 2026-09-08
- Sibling-pass corroboration (fetched 2026-09-06 by the programmatic-advertising-platform pass, recorded in research/programmatic-advertising-platform.md): The Trade Desk official glossary (SSP, sell side, bid request/response, PMP, Deal ID definitions); Microsoft Monetize (Xandr) docs on Microsoft Learn (sell-side roles, deal auction mechanics, programmatic guaranteed); Magnite/PubMatic product pages.

Limitations: PubMatic's operational documentation (publisher console docs, OpenWrap docs) is login-walled; PubMatic evidence is positioning-level plus the public help-portal root. Magnite's deep help articles beyond the glossary require SSO; the glossary and help-center structure are public and unusually detailed. OpenX and Verve evidence is product-page level (Tier 2); no operational console docs were fetched for them. No numeric limits, fee percentages, or timing windows are asserted beyond what fetched pages state. No historical vendor documentation (2007–2012 era) was fetched this pass; the historical check is canonical inference (see Historical Check).

## Product Observations

### Magnite — sell-side anchor (evidence layer A)

- Positioning (homepage): "Magnite is the modular ad platform media owners rely on to drive durable revenue, and buyers & agencies trust to curate premium inventory across every screen." Sellers page: "You work hard to build your audience. Together, we'll make every impression count."
- Seller product lines (Sellers page): **SpringServe** video platform ("combining ad serving, mediation, and programmatic into one powerful solution"; "the best of an ad server and SSP in one platform"; "manage all your demand in one interface, including direct, programmatic, OpenPath, and Magnite ClearLine"); **DV+ Supply-Side Platform** (display, online video, audio, native, DOOH; "AI-powered, outbound traffic shaping and floor price recommendations based on real-time marketplace signals"); **Demand Manager** (turnkey wrapper management for header bidding; Prebid.org co-founder); **Mobile In-App SDK**; **Deals & Marketplaces** ("robust Programmatic Guaranteed (PG), Private Marketplaces (PMP), Auction Packages, and curated marketplaces… Package premium inventory for strategic buyers to deliver pre-negotiated rates, volume commitments"); **Magnite Access Audience Suite** (identity, DMP integration, first/third-party data, GDPR/CCPA/TCF alignment); **Demand Facilitation** (dedicated team connecting sellers to agencies, buyers, and DSPs).
- Help Center structure (public): sections for DV+, Demand Manager, Magnite Buyers, ClearLine; articles include Quick Start Guide, Deals Walkthrough ("create a deal, edit/copy a deal, add targeting"), Ad Source Walkthrough ("create an Ad Source, edit/copy"), Ad Quality Guidelines, Inventory Management Health, Reporting Glossary. Separate login consoles: DV+ (apps.rubiconproject.com), Streaming, SpringServe (console.springserve.com), ClearLine.
- Glossary (public, operational vocabulary — the deepest single source this pass):
  - **Inventory Hierarchy**: "describes the relationship between the Publisher and the Ad Unit. There are five levels… Seat, Publisher, Brand, Supply and Ad Unit."
  - **Inventory**: "the collection of Ad Units that are created by a Publisher and are intended for sale to Buyers. Each Ad Unit identifies a place where an ad can be displayed."
  - **Floor / Floor Price**: "A Floor describes the lowest amount of money the Publisher is willing to accept to display an ad. It is expressed in CPM." Floors are set on the inventory hierarchy and "by default, [are] inherited by child elements underneath them."
  - **Ad Source / auction types**: Ad Source Auction Type Default offers "First Price Auction: Winning bidders will pay the price that they bid; Second Price Auction: Winning bidders will pay 1 cent higher than the next highest bid (or floor)"; a VAST extension enumerates Ad Source Types: 2 = Fixed Price, 3 = Auction Price, 4 = Open Auction, 6 = Programmatic Guaranteed.
  - **Deal machinery**: Deal ID ("A Deal ID associated with the Bid Request"); Authorized Marketplaces ("entities that have additional demand behind them (with their own set of PMP deals)"); deal Status (Active/Paused/Expired).
  - **Seller-controlled demand rules**: Blocked Buyer Seat List ("nominate which buyer seats will be blocked from participating in auctions across your seat"); Advertisers Allow List ("allows a publisher to ONLY run ads from Advertisers that they have created"); Block Advertiser Domains (inherited down the hierarchy); Blocked Categories (IAB categories "sent on bid requests to buyers to indicate that they should not bid with advertisers that belong to the selected categories… the platform will enforce these blocks"); Creative Block Mode (CRID review status: Off/Block/Allow/Inherited); Ad Quality Guidelines.
  - **Revenue metrics**: Requests, Fills ("Count of responses to the publisher that contain an ad for display"), Fill Rate, Impressions, Use Rate, Gross Revenue ("Total 'Revenue' collected… relevant to the payout to the seller"), Net Revenue ("Total post-margin 'Cost' paid out to the seller"), Est Price ("what potential revenue may have been at different floor settings").
  - **Supply quality / operations**: QPS Limits ("set a limit on the number of queries-per-second that this SSP will process"); Smart Throttling (tiers supply by performance when QPS limits hit); Rejected Requests ("requests that were not processed… due to reasons related to supply quality, excessive qps or performance"); fraud detection default-on; Ladle diagnostic tool (shows "both a bid and a bid response").
  - **Seat roles**: Client Type — "SSP Client is for Publisher clients, creating a standard Publisher style seat. Network Client is used to manage DSP Partners."
  - **Ad-server integration / mediation**: Unified Decisioning (UD) — "an advanced mediation solution designed to incorporate a publishers Direct Sold lines as another demand source within their SSP Seat… the platform will become the central point for managing all demand and generate final Ad Responses"; UD LID Discovery Mode extracts line-item identifiers "from the External Ad Server (e.g. GAM, Freewheel)"; SSP Connect — "mapping rules to handle requests from different inbound integrations (e.g. SpringServe, Publica, Google Open Bidding, Generic OpenRTB)".
  - **Transparency/privacy**: sellers.json ("Business Domain… used in industry transparency initiatives (e.g. Sellers.json)"); ads.txt/app-ads.txt (Inventory Partner Domain); GDPR consent passing; COPPA flag; IFA/device-ID masking per demand partner; Source Relationship ("Direct if the inventory is owned by the seat holder", "Indirect if the inventory is sourced from a third-party partner" — direct evidence of reseller inventory).
  - **CTV machinery**: Ad Pods, Max Pod Seconds, competitive separation ("prevent ads from one or more IAB Categories/Industries from running within the same Ad Pod"), SSAI Type flags, live-stream acceleration.
  - Vendor-specific names (L3): Moka (traffic shaping), Calculon (aDomain throttling), Ladle, DV+, SpringServe, ClearLine, Magnite Access, Orchestration (agentic).

### PubMatic — sell-side anchor, buyer tools (evidence layer A for portal structure/positioning; deep docs inaccessible)

- Help portal root (public) organizes the product by audience: **Publisher** ("PubMatic brings together technical innovation, unique demand, and sophisticated analytics to ensure you control your revenue opportunities and user experience across all the major channels and formats, including CTV, online video, mobile app, web, and more"); **Activate** ("a self-serve platform for programmatic deals that brings buyers and publishers closer together… increased efficiency, transparency, and versatility of inventory curation and procurement"); **Buyer** ("all-in-one-place, self-serve deal management UI for buyers that creates a direct connection with publishers… in omni-channel auctions"); **Commerce Media**; **OpenWrap** ("a transparent wrapper solution for Prebid [that] lets publishers evaluate programmatic bids from multiple sources").
- Two login consoles exist (publisher and media-buyer; recorded by the programmatic pass from apps.pubmatic.com).
- Deeper operational docs are login-walled this pass — no console-level claims asserted.

### Index Exchange — pure-play SSP/exchange, standards-first philosophy (evidence layer A)

- Positioning (homepage): "We're a global supply-side platform revolutionizing ad technology. Our ad exchange enables media owners to grow revenue and marketers to reach consumers on any screen, through any ad format." Platform nav: Exchange Standards (Efficiency / Quality / Transparency), Addressability Portfolio, Channels and Formats, Data and Analytics, Deals, Index Cloud, Index Marketplaces.
- Publishers page: "Index Exchange connects you to premium global demand through an efficient and transparent exchange." Capabilities: cross-channel monetization ("full control and transparency over how you transact across each channel"); premium demand ("preferred supply partner of industry-leading DSPs and agency holding companies"); exchange quality ("Our dedicated quality team inspects each ad that flows through our platform… We helped write the standards for transparency in programmatic advertising, including ads.txt and app-ads.txt, ads.cert, and sellers.json"); addressability ("Our real-time identity framework connects your inventory and publisher data to the graphs and DMPs that buyers trust"); deal activation; data and analytics ("Our Client Audit Logs provide a receipt for every transaction, offering unparalleled price transparency and accountability… impression-level reporting"); integration and support ("We'll help you integrate on your terms, optimize bid requests, and configure inventory to meet the needs of media buyers").
- Deals page: "Seamlessly create and execute deals to transact on your terms." Deal types: **1:1 Deals** ("media owners and buyers connect directly to build dedicated deals"); **Programmatic guaranteed** ("buyer agrees to a guaranteed budget, and the Media Owner agrees to deliver a specific number of impressions for a fixed price based on the targeting specified by the buyer"); **Always-on deals** ("evergreen deals with premium media owners… turnkey activation across all major DSPs"); **Inventory packages** ("Buyers can curate inventory across media owners based on audience, content category, device delivery, format, or other needs").
- Knowledge Base (public, organized by audience: Media Owners / Buyers / DSPs / Marketplace Partners / Marketplace Vendors / Integration Partners):
  - Getting started for Media Owners: "Index provides various integration options to make it as easy as possible for Media Owners to monetize content across all inventory types such as web, mobile app, and STV." Two starting points: media owners **without** their own ad-serving technology choose a direct integration; "If you are a reseller or you have built your own in-house ad serving technology, see Integrate with Index as a Media Owner using OpenRTB." — direct evidence of (a) the SSP sitting behind publisher ad servers via OpenRTB and (b) resellers as a supported seller type.
  - Creating and managing deals: "Deals are exclusive auctions that allow you to offer specific inventory directly to selected buyers. Terms are negotiated and agreed upon before the auction occurs. You generally offer your premium inventory through deals, with the floor prices often higher than open market bids." Deal options: **Direct** ("a direct agreement between a Media Owner and a buyer"); **Programmatic guaranteed (open beta)** (as above); **Deal with Marketplaces** ("an agreement between a Media Owner and a Marketplace Partner… where terms are negotiated to sell a Media Owner's inventory in a Marketplace Package"; a Marketplace Partner is "the owner of an Index Marketplace that curates their media solutions… For example, a media agency, a data provider, or retail media network").
  - Floor (glossary tooltip): "A pricing control used by media owners and exchanges to set a minimum sale price on inventory."
  - Fixed price (glossary tooltip): "If the advertisers bid at this fixed price or above, their bid responses are eligible to compete in the auction, and, if they win the auction, they only pay the fixed price regardless of what their bid amount was."
  - DSP-side articles: integrate as a DSP using OpenRTB; targeting options to manage traffic; Market Floors ("optimize price guidance through Index").
  - Marketplace Vendors: data vendors register segments; vendor fees documented.
- Blog titles corroborate structure: "How Index Managed Demand Sources Revenue for Media Owners" (demand facilitation program); "A New Model for Dynamic Take Rates That Puts Media Owners First" (take-rate/revenue-share transparency; first-price auction context); "Introducing Index Cloud: Bring Your Own Intelligence Inside the Exchange" (neutral compute for decisioning).

### OpenX — pure-play SSP, productized role decomposition (evidence layer A, positioning)

- Positioning (homepage): "Simplify Advertising With The Intelligent SSP™." Audiences: Advertisers / Publishers / Partners.
- Product lines: **OpenXSelect** ("An interoperable curation, supply-side targeting, and deal creation platform"); **OpenXBuild** ("A software suite for building better, more flexible advertising solutions" — a partner quote describes "apply[ing] our audience enrichment and bidding algorithms directly inside the exchange… bidding more selectively"); **OpenXControl** ("A yield and monetization platform, connected to quality demand partners"; publisher audience: "Maximize yield with advanced controls and full transparency"); **OpenXExchange** ("A real-time, scalable marketplace for quality inventory and automated ad buying").
- Differentiators: Quality ("direct publisher partnerships, actionable data, AI-driven fraud detection"), Performance ("the industry's largest supply-side identity graph"), Adaptability.
- Partner quotes corroborate the sell-side role: The Guardian ("OpenX helps us maintain transparency, protect the user experience, and ensure our inventory is valued appropriately in the marketplace"); an agency partner ("evolved from an SSP you target in a DSP to a partner we have built custom solutions with… particularly in CTV").

### Verve (Smaato SPX) — mobile-first SSP pole (evidence layer A, positioning)

- Branding: "Brand+ Marketplace (formerly Smaato)" under Verve Group; login products "PubNative" and "Smaato: SPX".
- Publisher offer: "Maximize revenue potential with impactful ad experiences from the world's leading multi-channel advertisers"; direct-sourced demand ("high-quality omnichannel demand from 100+ DSPs and direct relationships with agencies and brand advertisers"); deal curation ("Amplify demand by exclusively curating your inventory for advertisers"); user value enrichment ("Enrich ad requests with exclusive behavioral and contextual intelligence for better user value prediction and higher eCPMs").
- Platforms: mobile app ("Scale ad revenue… via the Verve NextGen mobile SDK"), CTV, web; formats: interstitial, video, native.
- Technical specifications: global data centers; "IAB OpenRTB-compliant — Standardized ad delivery and transparency"; regulatory compliance (CCPA, GDPR, COPPA); supply-chain transparency ("Supports Sellers.json and App-ads.txt"); ID-less addressability; independent measurement partners (GeoEdge ad quality, IAB OMSDK viewability, Human/Pixalate fraud); member of Prebid and IAB Tech Lab.

### Sibling-pass corroboration (evidence layer B — fetched by the programmatic pass 2026-09-06)

- The Trade Desk glossary (buy-side vendor's independent definition): **SSP** — "A technology company that enables publishers to manage and automate the selling of their ad inventory so they can generate the maximum amount of revenue per ad impression." **Sell side** — "publishers and supply-side platforms." **Bid request** — SSP→DSP signal with impression details; **bid response** — DSP→SSP with price and creative specs.
- Microsoft Monetize (Xandr) docs: sell-side roles (publishers, reselling inventory, ad quality requirements, yield-management floors) documented as distinct from the ad-server role and the buying platform; deal auction mechanics (open/private auctions, deal priority, fixed price, ask vs reserve price precedence); programmatic guaranteed flows through the bid machinery.
- Magnite/PubMatic product pages (same content as this pass's fetches, cross-pass consistent).

## Cross-product Comparison

| Dimension | Magnite | PubMatic | Index Exchange | OpenX | Verve (Smaato SPX) |
|---|---|---|---|---|---|
| Self-description | "modular ad platform media owners rely on"; product lines named "Supply-Side Platform" (DV+) | "control your revenue opportunities… across all the major channels and formats" (Publisher docs) | "global supply-side platform… our ad exchange" | "The Intelligent SSP™" | multi-channel monetization marketplace (formerly Smaato SSP) |
| Seller term | media owners / publishers | publishers | media owners (publishers, resellers, streaming TV) | publishers | publishers / app developers |
| Inventory representation | Seat → Publisher → Brand → Supply → Ad Unit hierarchy; Ad Unit = "a place where an ad can be displayed" | publisher console over channels/formats (CTV, video, mobile app, web) | integration options per inventory type (web, app, STV); direct or OpenRTB inbound | publisher yield platform + exchange | SDK (mobile), connections (CTV, web) |
| Demand exposure | bid requests to DSPs; Authorized Marketplaces; buyer seats | "unique demand"; omni-channel auctions | "premium global demand"; preferred supply partner of DSPs; OpenRTB to DSPs | OpenXExchange "real-time, scalable marketplace… automated ad buying" | "100+ DSPs and direct relationships" |
| Seller pricing rules | Floor/Floor Price (CPM) with hierarchy inheritance; Est Price floor simulation | (positioning-level this pass) | Floor = "minimum sale price on inventory"; Market Floors for DSPs | "advanced controls" (yield platform) | user-value enrichment → higher eCPMs |
| Deal machinery | PG, PMP, Auction Packages, curated marketplaces; deal status Active/Paused/Expired | Activate (self-serve deals); Auction Packages | Direct, Programmatic guaranteed, Always-on, Inventory packages, Deals with Marketplaces | OpenXSelect (curation + deal creation) | deal curation; Deals Library for DSPs |
| Auction mechanics | First-price / second-price / fixed / open auction / PG as Ad Source types | (not accessible) | fixed price: bid ≥ fixed → eligible; winner pays fixed | (positioning-level) | OpenRTB-compliant |
| Demand access control | Blocked Buyer Seat List, Advertisers Allow List, blocked aDomains/categories, CRID creative review | (positioning-level) | Exchange Quality team inspects each ad; MFA-site prohibition | AI-driven fraud detection; quality focus | ad quality (GeoEdge), fraud (Human/Pixalate) |
| Revenue accountability | Requests/Fills/Fill Rate/Impressions/Use Rate; Gross vs Net Revenue; reporting glossary | analytics positioning | Client Audit Logs ("a receipt for every transaction"); impression-level reporting | transparency positioning | eCPM/revenue positioning |
| Ad-server relationship | SpringServe ("best of an ad server and SSP"); Unified Decisioning folds direct-sold lines into the SSP seat; UD reads GAM/FreeWheel line items | OpenWrap wrapper alongside | SSP behind publisher ad servers via OpenRTB (resellers/in-house ad servers) | OpenXBuild lets partners run decisioning inside the exchange | SDK-first (no ad server claimed) |
| Wrapper/header bidding | Demand Manager (Prebid co-founder) | OpenWrap (Prebid) | (not a named line) | (not a named line) | (not a named line) |
| Buyer-side products | Magnite Buyers (help section; "In Development") | SSP-for-buyers console; Activate | Buyers + DSPs solution pages | Advertisers audience | DSP-facing pages + Deals Library |
| Formats | CTV/OTT streaming, display, video, audio, native, DOOH, mobile in-app | CTV, online video, mobile app, web | display, video, streaming TV, mobile, native | omnichannel; CTV emphasized | mobile app, CTV, web; interstitial/video/native |
| Identity/data | Magnite Access (IDs, DMP integration, first/third-party data) | Identity Hub | Addressability Portfolio; real-time identity framework | supply-side identity graph | user value enrichment; ID-less addressability |
| Transparency standards | sellers.json, ads.txt/app-ads.txt | sellers.json, app-ads.txt (via Verve page) | co-authored ads.txt/app-ads.txt/ads.cert/sellers.json | supply-path visibility | Sellers.json, App-ads.txt |
| Customer tier | enterprise publishers/streamers | enterprise publishers + buyers | enterprise media owners | enterprise publishers | app developers / mobile-first publishers |

### Convergent findings (evidence layer B unless noted)

1. **The SSP is defined by whose side it is on.** Every sampled product addresses the media owner/publisher as its customer and frames its job as the seller's revenue ("make every impression count", "control your revenue opportunities", "maximize yield", "inventory is valued appropriately"). The buy side appears only as the demand to be won. (A across all five; TTD's buy-side glossary defines the SSP identically from the other side of the market.)
2. **Inventory is registered, structured, and exposed automatically.** All sampled products represent the seller's inventory as structured objects (Magnite's five-level hierarchy is the most explicit; Index's integration options per inventory type; PubMatic's channel/format coverage; Verve's SDK connections) and expose ad opportunities to external demand through automated request/bid machinery (OpenRTB named by Index, Verve; bid request/response named by Magnite metrics and TTD glossary).
3. **Seller-controlled monetization rules are universal.** Floors (Magnite glossary definition; Index glossary definition; OpenX "advanced controls"), buyer/demand access control (Magnite's blocked buyer seats/allow lists; Index's quality team; OpenX quality), and pre-negotiated deals (all five) are the seller's levers. The platform enforces them in the per-impression decision.
4. **Deal machinery is a shared, named, standardized layer.** Open exchange, private marketplace/PMP, preferred/fixed price, programmatic guaranteed, and packages/curated marketplaces appear across Magnite, Index, PubMatic, OpenX (and, from the sibling pass, Monetize and TTD). Deal ID is the interoperable key (Magnite metric; TTD glossary).
5. **Revenue accountability to the seller is universal.** Fill/fill-rate/revenue metrics (Magnite), audit-log receipts (Index), yield reporting (OpenX Control), revenue-opportunity framing (PubMatic). Gross-vs-net revenue and take rates are explicit where documented (Magnite; Index dynamic take rates).
6. **The SSP absorbs neighboring roles rather than shedding them.** Ad-server bundling (SpringServe; Unified Decisioning reading GAM/FreeWalker line items), wrapper products (Demand Manager, OpenWrap), buyer-side consoles (PubMatic SSP-for-buyers, Magnite Buyers), curation/marketplace products (Auction Packages, Index Marketplaces, OpenXSelect), and demand facilitation teams (Magnite, Index Managed Demand) all appear as product lines inside SSP-led vendors.
7. **Transparency standards are a shared posture.** sellers.json / ads.txt / app-ads.txt support is documented by four of five sampled products; Index claims co-authorship. The SSP is the entity these standards govern (the "seller" in sellers.json).
8. **The exchange venue has been absorbed.** Index self-describes as both "supply-side platform" and "ad exchange"; OpenX sells "OpenXExchange" as a product line; Magnite runs auction machinery inside its SSP products. No sampled product sells a separate standalone "exchange" distinct from its SSP.

## Canonical Model

### L0 — Defining Invariant (deliberately small)

A Supply-side Platform is the inventory owner's side of the automated advertising marketplace. Four jointly-held structures:

1. **The seller relationship of record** — the platform registers media owners (publishers, app developers, streaming services, resellers) and their sellable inventory as structured supply it represents. The SSP acts *for* the seller; the media owner is its customer. Remove → the product serves buyers (DSP) or itself (ad network), not sellers.
2. **Automated exposure of inventory to external demand** — each ad opportunity is automatically offered to external demand sources (DSPs, exchanges, networks, deal buyers) through a platform-executed request/bid loop; the seller does not negotiate each impression. Remove → direct-sold insertion orders only (ad server / direct sales), not an SSP.
3. **Seller-controlled monetization decisioning** — the seller's rules govern the transaction and the platform enforces them per impression: minimum prices (floors), which demand may participate (buyer access, ad quality), and pre-negotiated deal terms (direct, preferred/fixed, private marketplace, programmatic guaranteed). Remove → a conduit that aggregates inventory without seller agency (ad network) or a neutral relay with no seller side.
4. **Seller-facing revenue accountability** — won impressions are logged (fill, price, buyer) and reported back to the seller as revenue, forming the basis for payment and yield management. Remove → traffic redirection with no monetization record.

Jointly-held is load-bearing: 1 alone = a publisher CRM/roster; 2 without 1+3 = anonymous traffic resale; 3 without 2 = a rate card with no automated selling; 1+2 without 3 = an ad network with a dashboard; 1+2+3 without 4 = a redirector with no revenue record.

### L1 — Common Mature Structure

- Multi-demand mediation: simultaneous/sequential exposure to many DSPs, exchanges, networks, and deal buyers (open auction as the default access tier); supply-path optimization
- Deal machinery depth: open exchange, private marketplace (PMP), preferred/fixed-price deals, programmatic guaranteed (fixed price + volume/budget commitments), auction packages and curated marketplaces; Deal ID interoperability
- Floor/reserve-price machinery with inheritance across the inventory hierarchy; yield optimization (floor recommendations, traffic shaping, throttling)
- Structured inventory hierarchy (account/seat → publisher → property/brand → supply → ad unit; naming varies by product)
- Ad quality and brand-safety controls: blocked advertiser domains/categories, creative review, buyer-seat blocks, fraud detection
- Omnichannel format coverage: display, online video, CTV/streaming (incl. ad pods, competitive separation, SSAI), mobile in-app, audio, native, DOOH
- Identity/addressability layer: ID frameworks, first-party data activation, DMP integration, ID-less fallbacks
- Transparency standards: sellers.json, ads.txt/app-ads.txt; consent/privacy regime passing (GDPR/CCPA/COPPA-class)
- Reporting and analytics: requests, fills, fill rate, impressions, revenue (gross/net), buyer-level and impression-level detail; audit logs
- Revenue-share/take-rate economics and payment basis
- Demand facilitation (human/program teams sourcing incremental demand)
- Management/reporting APIs; self-serve consoles for sellers (and increasingly buyers)

### L2 — Variant / Optional Structure

- Ad-server bundling: SSP products that also select and serve ads (SpringServe "best of an ad server and SSP"; unified decisioning folding the publisher's direct-sold lines into the SSP seat as one more demand source)
- Header-bidding wrapper products as separate lines (publisher-side demand mediation ahead of/alongside the SSP path)
- Buyer-side products sold by SSP vendors (SSP-for-buyers deal consoles)
- Curation/marketplace extensions (curated packages, retail/commerce media, data-vendor marketplaces)
- Channel specialization: mobile-first (SDK integration, app developers), CTV/streaming-first (SSAI, ad pods), web-first (tags/header)
- Exchange-venue absorption (the SSP runs its own auction venue; standalone "exchange" as a separate product is rare)
- Reseller support (inventory sourced from third-party partners; OpenRTB inbound from publisher-side ad servers)
- Self-serve vs managed-service operating models; regional/regime differences (identity, consent frameworks, local market structures)
- Compute/deployment variants (neutral compute environments for partner decisioning inside the exchange)

### L3 — Vendor-specific Structure (research notes only)

- Magnite: DV+, SpringServe, ClearLine, Demand Manager, Magnite Access, Orchestration; Seat/Publisher/Brand/Supply/Ad Unit hierarchy; Ad Source types (IOA/UFR/AG); Moka traffic shaping; Calculon aDomain throttling; Ladle diagnostics; Unified Decisioning (UD) with LID discovery; SSP Connect inbound-integration mapping; Smart Throttling tiers; Fill Guaranteed legacy setting
- PubMatic: OpenWrap (+ SDK), Activate, Connect, Identity Hub, Convert (commerce media), AgenticOS, Intelligent Yield
- Index Exchange: Index Cloud (neutral compute), Index Marketplaces, Client Audit Logs, Market Floors, Managed Demand, dynamic take rates, always-on deals, inventory packages
- OpenX: OpenXSelect (curation/supply-side targeting/deal creation), OpenXBuild (partner decisioning inside the exchange), OpenXControl, OpenXExchange
- Verve: Brand+ Marketplace (formerly Smaato), Smaato SPX console, PubNative, NextGen SDK
- Market-structure corroboration: G2 grid memberships (from sibling pass)

## Rejected Findings (over-fit candidates examined and rejected)

1. **"Real-time auction competition is definitional" — qualified.** Programmatic guaranteed trades at pre-agreed fixed terms yet flows through the same automated machinery (Index: buyer commits budget, seller commits impressions at a fixed price, created and executed in the platform; Magnite: PG is an Ad Source type in the same machinery; sibling pass: Monetize PG line items bid on every deal impression). The invariant is the automated per-impression transaction under seller rules, not necessarily price competition.
2. **"Open-exchange access is definitional" — rejected.** Deals/PMP/PG are first-class structures in every sampled product; open exchange is one access tier. Index: "You generally offer your premium inventory through deals, with the floor prices often higher than open market bids."
3. **"Multiple simultaneous demand sources per impression is definitional" — qualified.** Multi-demand mediation is the universal mature shape (all five products), but the defining act is automated exposure to external demand under seller rules; a single-demand-source configuration still exercises the same machinery. Plurality is held as L1.
4. **"Header bidding is definitional" — rejected.** It is a publisher-side technique variant; only two of five sampled vendors sell a wrapper product as a named line, and SSPs work without it (sibling pass reached the same judgment for the category).
5. **"The SSP owns the ad-serving decision" — rejected as definitional.** Selection/serving is the ad server's unit of work; SSPs bundle it (SpringServe, UD) but the SSP's own unit of work is the transaction with external demand. Bundling is L2.
6. **"CTV/streaming machinery defines the modern SSP" — rejected.** Ad pods/SSAI/competitive separation are format machinery (L1/L2); a display/video SSP of the 2010s satisfies L0.
7. **"SSP = exchange" — rejected as an identity claim.** The venue role has been absorbed (finding 8 above), but the SSP's defining relationship is with the seller, not the venue; Index's dual self-description ("supply-side platform… our ad exchange") shows absorption, not equivalence.

## Boundary Findings

1. **vs Demand-side Platform / DSP (§06 sibling, unprocessed)** — mirror pole. The DSP's customer is the advertiser/agency; its objects are campaigns/budgets/bids/targeting; its job is winning impressions. The SSP's customer is the media owner; its objects are inventory/floors/deals; its job is selling impressions. Test: strip the seller side (inventory registry, floors, deal packaging, seller revenue reporting) → a DSP. The two leaves are poles of one marketplace, not overlapping Types. Joint review flagged (see STATUS.md).
2. **vs Ad Server (§06, processed)** — unit-of-work seam, consistent with both sibling passes: the ad server selects from a managed ad pool on known placements (priorities, forecasting); the SSP transacts inventory with external demand (floors, deals, buyer access). Bridged in practice: ad servers take programmatic backfill; SSPs bundle ad serving (SpringServe; UD folds direct-sold lines in as demand); Index accepts OpenRTB inbound from publisher ad servers. The seam holds at the unit-of-work level and is consciously porous at suite level.
3. **vs Ad network (historical, not in directory)** — agency-vs-principal seam. The ad network takes ownership of inventory (or exclusive rights to it) and resells it under its own terms; the SSP never takes ownership — it exposes the seller's inventory under the seller's rules and reports revenue back. The ad network fails L0-3 (no seller-controlled per-impression decisioning) and is the pre-programmatic neighbor on the historical axis.
4. **vs Ad exchange** — agent-vs-venue seam. The exchange is a neutral venue conducting auctions among many buyers and sellers; the SSP is the seller's agent. In current products the venue role has been absorbed into SSP platforms (Index "our ad exchange"; OpenXExchange; Magnite auction machinery), so the exchange survives as a role inside products rather than a separate Type in this sample.
5. **vs Programmatic Advertising Platform (§06, processed)** — pole-vs-category. The programmatic pass documented the two-sided trading category and named the SSP as its sell-side instantiation. This pass documents the pole itself. Joint review recommendation stands: decide whether the category leaf remains a Type or becomes an alias/see-also of the two poles.
6. **vs Advertising Campaign Management (§06, processed)** — buy-side walled-garden consoles govern campaigns on specific publisher platforms; the SSP is the seller-side machinery those campaigns buy from. Opposite sides of the same transaction.
7. **vs Media Buying Platform (§06 sibling, unprocessed)** — media buying is the whole buying operation (planning, negotiation, insertion orders, reconciliation across all channels); the SSP is sell-side infrastructure. No overlap in customer or objects.
8. **vs Data Management Platform / DMP (§06 sibling, unprocessed)** — data supply vs transaction machinery; DMPs/identity layers attach to the SSP (Magnite Access, Index addressability, PubMatic Identity Hub) but are not the selling system.
9. **vs Header-bidding wrapper** — publisher-side demand-mediation technique/product; adjacent and often same-vendor (Demand Manager, OpenWrap), but the wrapper's unit of work is mediating demand sources before the ad server, not transacting inventory as the seller's agent. Held as L2 variant when bundled, adjacent product when standalone.

### The "remove-what" tests

- Remove the seller agency (platform takes ownership and resells under its own terms) → ad network.
- Remove automated external-demand exposure (direct-sold only) → ad server + direct sales.
- Remove seller-controlled rules (no floors, no access control, no deals) → anonymous conduit.
- Remove revenue accountability → traffic redirector.
- Remove the sell side entirely (buyer-side objects only) → DSP.
- Remove the transaction focus, keep only request-time selection on managed placements → ad server.

## Historical / Market-Sample Check

- **First-generation SSPs ("yield optimizers", roughly 2007–2012)** — publisher inventory exposed automatically to multiple demand sources (then: ad networks + emerging exchanges), publisher-set floors, yield rules choosing the winning demand, revenue reporting to the publisher. Satisfies all four L0 structures without header bidding, CTV machinery, identity layers, or AI. Fits. (Canonical inference from the structure of the current market and the vendors' own lineage claims — e.g., OpenX's exchange heritage, PubMatic's publisher-revenue-optimization origin; no historical vendor docs fetched this pass, so no precise dates or feature claims are asserted.)
- **Publisher ad server with direct-sold campaigns only** — fails L0-2 (no automated external-demand exposure); it is the ad-server/direct-sales world the SSP sits beside (and increasingly absorbs).
- **Ad networks** — fail L0-3 by design (principal, not agent); correctly excluded as a different Type, not an era variant.
- **Regional programmatic ecosystems** — same sell-side structure with local identity/consent/regime differences; L0 holds, L2 differs. (Recorded conceptually; not document-fetched this pass.)
- **Conclusion:** L0 does not over-fit the current omnichannel-identity-AI era. The definition is anchored to the seller agency + automated exposure + seller rules + revenue accountability, which is the stable core across the SSP's history.

## Uncertainties

1. PubMatic's operational documentation is login-walled; PubMatic claims are positioning-level plus the public help-portal root. Its inclusion of buyer-side consoles and OpenWrap is corroborated by the sibling pass's independent fetch of pubmatic.com product pages.
2. OpenX and Verve evidence is product-page level (Tier 2); no console-level operational claims are asserted for them. Verve/Smaato is mid-rebrand ("Brand+ Marketplace (formerly Smaato)"), so its product naming may shift.
3. Magnite's deep help articles (beyond the public glossary) require SSO; console-level workflow detail for DV+/Streaming rests on the glossary + help-center structure + sellers-page claims.
4. The historical check is canonical inference; no 2007–2012 vendor documentation was fetched. If a future pass fetches first-generation SSP docs, the L0 should be re-tested against them.
5. Whether the directory ultimately wants the SSP as an independent Type, a pole-of-category note, or a merge with DSP under the programmatic category is a taxonomy-owner decision; this pass documents the pole honestly and flags the joint review (see STATUS.md Boundary Issues).
6. The exact revenue-share/take-rate mechanics vary by product and deal and are not asserted beyond what fetched pages state (Magnite gross/net definitions; Index dynamic-take-rate blog title).

## Final Synthesis

A Supply-side Platform is the media owner's side of the automated digital-advertising marketplace. Its defining structure is fourfold: it registers inventory owners and their sellable inventory as the supply it represents (the seller relationship of record); it exposes each ad opportunity to external demand sources automatically through a request/bid loop the platform executes; it enforces the seller's monetization rules per impression — minimum prices (floors), demand access (buyer allow/block, ad quality), and pre-negotiated deal terms (direct, preferred/fixed, private marketplace, programmatic guaranteed); and it accounts for every won impression back to the seller as revenue. Around this core, mature products add multi-demand mediation, deal machinery depth, floor inheritance and yield optimization, ad-quality and fraud controls, omnichannel format coverage, identity/data layers, transparency standards (sellers.json/ads.txt), and seller-facing reporting down to the impression. The SSP's neighbors are defined by three seams: the ad server (selection on managed placements vs transacting with external demand), the ad network (principal vs agent — the historical negative case), and the DSP (the mirror pole on the buy side). The exchange venue has been absorbed into SSP platforms rather than remaining a separate product shape. The SSP stands as a distinct Type — the sell-side pole of the programmatic category documented by the sibling pass — with a joint-review flag linking it to the DSP leaf and the programmatic category leaf.
