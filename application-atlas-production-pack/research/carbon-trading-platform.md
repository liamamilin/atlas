# Research Notes — Carbon Trading Platform

## Research Goal

Understand what a Carbon Trading Platform actually is and how it works, from real products:
what is traded, through what mechanism, among whom, and how trades are settled — so that the
Application Document can explain the Type without copying any vendor's framing.

## Initial Boundary

Working hypothesis before research:

- Core use: organized market execution for carbon instruments — emissions allowances
  (compliance markets) and carbon credits (voluntary markets) — with price discovery and
  post-trade settlement.
- Nearest Types: Carbon Credit Management (already documented: custody/lifecycle/evidence,
  not execution), Energy Trading Platform (carbon as one instrument among energy commodities),
  Registry systems (authoritative issuance/transfer/retirement), Marketplace (05.02),
  Online Auction Platform (05.18), Retail Trading Platform (08), Cryptocurrency Exchange.
- Known unknowns: is venue-operated custody part of the defining core or a common
  implementation? Are order books, auctions, RFQs alternative forms of one execution concept?
  How do compliance and voluntary instruments coexist on one venue?
  Does the venue retire credits or only trade and settle them?

## Research Questions

1. What instruments are traded, and how are they represented (standardized contracts vs
   project-specific credit lots vs allowances)?
2. What execution mechanisms exist (order book, auction, RFQ, market board, OTC recordation)?
3. What are the core objects and how do they relate (instrument, participant, order/bid/offer,
   trade, holding/position, settlement, rules, market data)?
4. What is the end-to-end trade lifecycle, especially how settlement interacts with registries
   and who does retirement?
5. How does price discovery manifest?
6. What roles exist (trading members, brokers, clearing members, compliance entities, developers)?
7. What rules govern participation and instrument eligibility?
8. Where are the boundaries with neighboring Types — with the "remove what" test?

## Representative Products

Selected for market representation, different product philosophies, and accessible official
documentation:

1. **Xpansiv / CBL** — the market-leading environmental commodities exchange; spot order book +
   auctions + RFQ + OTC post-trade settlement + market data + registry integration. Institutional.
2. **ACX (AirCarbon Exchange)** — carbon-focused exchange with standardized contract families
   (CET/GNT/GNT+/SDGT/RET/HOT/XCT) and venue-integrated custody; membership model; also sells
   exchange infrastructure as SaaS. Institutional.
3. **ICE (EUA Futures on ICE Endex)** — the compliance-market pole: regulated derivatives
   exchange trading EU allowances as standardized futures with physical delivery into registry
   trading accounts via a clearing house.

Boundary-case products (fetched, used for boundary reasoning, not as core samples):

- **Puro.earth** — carbon-removal registry + certification + marketplace; trading happens
  largely through intermediaries; useful to mark the trading-platform vs registry/marketplace seam.

Unreachable (per source-access rule, dropped after repeated failures; no claims made about them):

- **Climate Impact X (CIX)** — 403 ×2.
- **Carbon Trade Exchange (CTX, carbon.trade)** — transport error ×2.

## Sources

All fetched 2026-09-07 from official vendor surfaces (Tier 1/2: product pages, market pages,
product specification pages):

- Xpansiv — https://xpansiv.com/ (home), https://xpansiv.com/trading-platforms/cbl/ (CBL),
  https://xpansiv.com/commodities/carbon/ (carbon commodity page)
- ACX — https://acx.net/ (home), https://acx.net/carbon/ (carbon contracts),
  https://acx.net/acx-singapore/ (platform mechanics)
- ICE — https://www.theice.com/products/197/EU-Carbon-Futures (EUA Futures contract specification);
  note: https://www.theice.com/carbon returned 404 and a products-hub path returned an
  unsupported-browser shell before the spec page succeeded
- Puro.earth — https://puro.earth/ (home; registry/certification/marketplace surfaces)

Documentation access was at product/marketing-page depth for Xpansiv and ACX (help-center-level
operational docs, rulebooks, and full contract specifications were not fetched for them — the
CBL Rulebook and Standard Instruments Program are referenced on-page as documents but were not
retrieved). ICE's EUA product page is a true contract specification. Assertion strength in this
file reflects that depth: Xpansiv/ACX observations are marketing-surface-verified; only ICE's
mechanics reach contract-specification precision.

## Product A — Xpansiv / CBL (evidence layer: A — directly observed, product pages)

### Key observations

- Xpansiv positions itself as a multi-product platform: Trading Platforms (online exchanges &
  marketplaces), Market Execution (brokerage), Registries, Power, Connect (portfolio management
  & integration), Data (market data). Carbon is one commodity among renewables, fuels, water,
  recycled materials.
- **CBL** described as "the world's largest and most active spot marketplace for environmental
  commodities" with a "transparent matching engine and automated settlement mechanism";
  "centralized price discovery and efficient settlement for exchange and OTC trades".
- Scale claims (marketing-surface, kept out of final doc): 1,100+ participants; 300 million
  tonnes of carbon traded since 2020 including exchange-matched and OTC-settled transactions;
  T+0 automated same-day settlement of CBL-matched trades.
- **Project-specific credit trading**: "full depth-of-book transparency, instant trade matching
  and same-day settlement. Filter the market by project type, registry, vintage, region and
  country. Use CBL's full range of order types and RFQ and auction capabilities… Settle OTC
  transactions via the exchange's post-trade settlement mechanism, enabling trades with hundreds
  of qualified exchange participants without bilateral agreements."
- **Standardized benchmark contracts**: GEO® (first VCM standardized contract, 2020), N-GEO®
  (nature-based), C-GEO® (technology-based), ICVCM CCP® GEO contracts ("specific to leading
  carbon registries, including Climate Action Reserve and Verra, ensuring the delivery of
  CCP-eligible credits"), GEO CORSIA CP1 ("eligible emissions units (EEUs) that meet the CORSIA
  First Compliance Phase eligibility criteria"; "Automated tagging via Xpansiv Connect ensures
  EEUs delivered through the contract are CP1 eligible").
- **Compliance instruments on the same venue class**: live screen trading of generic and
  project-specific ACCUs (Australian Carbon Credit Units) "alongside other compliance markets
  including California Carbon, the Regional Greenhouse Gas Initiative"; CBL Markets (Australia)
  holds an Australian Financial Services Licence for making a market in ACCUs to wholesale clients.
- **Auctions**: participants "bid and offer directly into the world's deepest VCM liquidity pool";
  corporate buyers, fund managers, trading houses, financial intermediaries; "a range of auction
  types"; "same-day settlement of credits and payments"; marketing services to generate buyer demand.
- **RFQ**: buyer or seller sets specifics — "project type, volume, price, timing and vintage";
  distributed across the participant base; quotes submitted; "negotiate terms, then finalize
  through CBL's platform with immediate T+0 settlement".
- **OTC post-trade settlement**: bilateral trades can be settled through CBL's automated
  post-trade infrastructure — the venue acts as settlement rail for trades executed off-book.
- **Adjacent layers**: Xpansiv Connect ("unified visibility and full lifecycle management of
  credits across 15+ registries" — portfolio layer), Xpansiv Data (spot transaction and bid/offer
  data; spot/forward data), Evolution Markets (brokerage, structured transactions), Xpansiv
  Registries (issue/track/transfer), C-Capsule (durable-removal registry), developer portal
  (APIs), "Join CBL — apply to participate".
- **Powered-by model**: Xpansiv runs or powers partner exchanges — IATA Aviation Carbon Exchange
  (ACE: "centralized trading platform… live, secure electronic trade matching, a range of clearing
  and settlement options"), JSE Ventures Carbon Market (South Africa), RVCMC (Saudi Arabia).

### Interpretation

CBL shows the fullest anatomy of the Type: a governed venue where project-specific credits and
standardized carbon contracts are executed via an order book (plus auctions and RFQs), with an
automated post-trade settlement mechanism that also serves OTC trades, registry integration for
delivery, market data for price discovery, and an application/membership admission process.

## Product B — ACX (AirCarbon Exchange) (evidence layer: A — directly observed, product pages)

### Key observations

- Self-description: "a leading trading platform for environmental products, empowering nations
  and corporations… With 24/7 access… trading of environmental products, fostering transparency,
  efficiency, and scalability".
- Scale claims (kept out of final doc): +21 Mt transacted; +190 active trading members; +30
  countries represented; "Best Carbon Exchange" awards 2021–2024.
- Platform elements (their own decomposition — five named surfaces):
  - **Spot platform** — "carbon is traded via a standardised contract with full control over
    bid/ask prices"; "fast trades"; "instant trade settlement/clearing".
  - **Market board** — "sellers transact with trusted counterparties, efficiently allowing them
    to share offers at a chosen price".
  - **Settlement portal** — "simplifies trade settlement… efficient trade input and tracking";
    cost-effective, secure, error-reducing tools.
  - **Auctions** — "an avenue for bulk sale of credits and price discovery"; "full flexibility
    on auction rules".
  - **Inventory collateral management** (named surface; detail not documented on fetched pages).
- **Venue-integrated custody**: "carbon credits trading, custody and portfolio management are
  integrated into the exchange"; "traders can access various types of carbon credits without
  opening separate registry accounts".
- **Standardized contract families**, each defined by credit-eligibility criteria:
  - CET — CORSIA-eligible tonnes (credits eligible under CORSIA 2021–2023 pilot phase)
  - GNT / GNT+ — nature-based credits, with/without co-benefit certifications
  - SDGT — credits with UN SDG certifications
  - RET — renewable-energy-project credits; HOT — improved-cooking-solution credits
  - XCT — "credits issued under an eligible Market Registry, which does not meet another ACX
    contract specification"
  - Sampled specification detail: "Denominations: 1 Tco2e; Contract Size: 1000 Tco2e
    (1 Contract = 1,000 Tco2e)".
- **Target participant types named**: airlines, financials, brokers, institutions, speculators,
  fuel companies, voluntary (CSR) buyers.
- **Integrity posture**: "operational best practices systemically defeat double-counting,
  spending, and retirements"; "ACX captures the complete trading lifecycle of each carbon credit,
  delivering detailed ownership history and secure settlement records… an immutable record for
  every transaction"; "check project eligibility" is a named flow; works "with a wide range of
  registries, national standards agencies, and brokerages"; partnerships with verifiers (BSI
  quote) and ratings providers (BeZero quote).
- **Trade platform login** at trade.aircarbon.co — the venue is a member-facing application.
- **SaaS product line**: ACX offers its exchange platform as SaaS (white-label market
  infrastructure) — a variant of the Type sold as infrastructure.

### Interpretation

ACX shows the carbon-centric pole of the Type: standardization by eligibility class, membership
trading, venue-operated custody replacing per-registry accounts, an explicit settlement layer,
auctions for bulk sale and price discovery, and integrity safeguards (double-counting/retirement
controls, lifecycle records) as first-class features.

## Product C — ICE EUA Futures, ICE Endex (evidence layer: A — directly observed, contract specification)

### Key observations

- **Instrument is legally defined**: "EUA is an Allowance within the meaning of Article 3 of
  Directive 2003/87/EC" (the EU ETS directive) — "an entitlement to emit one tonne of carbon
  dioxide equivalent gas".
- **Standardized contract**: one lot = 1,000 EUAs; contract series up to 7 December, 9 quarterly,
  3 August, 2 monthly contracts; price in euros per metric tonne; minimum price fluctuation
  €0.01/tonne; minimum trading sizes for futures (1 lot), Exchange for Swap (50 lots), block
  orders (50 lots); Trade-at-Settlement markers.
- **Physical delivery via clearing**: "Contracts are for physical delivery where each Clearing
  Member with a position open at cessation of trading… is obliged to make or take delivery of
  EUAs to or from a Trading Account within the EUA Delivery Period and in accordance with the
  Rules." Delivery period, delivery delay, and delivery failure are formally defined
  (delivery into a "Trading Account" — the registry-account structure of the EU ETS).
- **Clearing venues and rulebook** named (ICE clearing; ICE Endex Market Rulebook); margin
  rates, expiry details, and fees exist as separate operational surfaces.
- **Trading-hours surface**: pre-open and continuous sessions listed per city — a session-based
  market, not 24/7.

### Interpretation

The compliance pole shows the same structural skeleton (standardized carbon instrument, governed
execution among admitted participants, priced trades, formal settlement into allowance accounts)
under a regulated-derivatives posture with a central clearing counterparty and delivery windows.
Carbon here is legally a compliance allowance, not a voluntary credit — but the venue mechanics
are recognizably the same Type.

## Boundary cases

### Puro.earth (evidence layer: A — directly observed, home page)

- Self-description: "certification infrastructure that turns carbon removal into a… bankable…
  asset"; "the essential infrastructure – registry, standards, and governance"; methodologies
  under the Puro Standard; CORCs (CO2 Removal Certificates) issued in the Puro Registry.
- Demand side: "buy carbon credits" flows, "Carbon Removal Indexes" (price signals), partners &
  intermediaries ("connecting buyers, projects, and financial intermediaries"), MyPuro platform,
  Puro Connect APIs.
- Boundary value: Puro anchors issuance/registry, with buying channels and intermediaries around
  it — an example of the registry/marketplace pole rather than a governed multi-party execution
  venue. Used to draw the trading-platform vs registry/marketplace seam. (Nasdaq is named as a
  partner/owner; a Nasdaq-operated marketplace for CORCs is referenced in blog content but was
  not verified in detail.)

### Unreachable products

- CIX (climateimpactx.com) — 403 twice; abandoned per source-access rule.
- CTX (carbon.trade) — transport error twice; abandoned.
- No claims are made about either product. Their existence is general market context only.

## Cross-product Comparison

| Dimension | Xpansiv / CBL | ACX | ICE EUA Futures | Puro.earth (boundary) |
|---|---|---|---|---|
| Instruments | project-specific credits + standardized GEO/N-GEO/C-GEO/CCP/CORSIA contracts + ACCUs | standardized contract families by eligibility (CET/GNT/GNT+/SDGT/RET/HOT/XCT) | EUA allowances as standardized futures (1 lot = 1,000 EUAs) | CORCs (removal certificates) issued via registry |
| Execution mechanisms | central limit order book + auctions + RFQ + OTC post-trade settlement | spot platform (standardized contract, bid/ask control) + market board + auctions | exchange trading (sessions) incl. block orders and Exchange for Swap | not an execution venue; buying via intermediaries/channels |
| Price discovery | "centralized price discovery"; depth-of-book; market data products | bid/ask control; auctions "for price discovery"; consistent pricing in immutable records | continuous order-book pricing in €/tonne; settlement prices | Carbon Removal Indexes (published index) |
| Settlement | "automated settlement mechanism"; T+0 claim; integrated registry network; OTC settlement rail | settlement portal; instant settlement/clearing; venue custody ("no separate registry accounts") | physical delivery via clearing house into EUA Trading Accounts with delivery-period rules | registry transfer; retirement tracked at registry |
| Custody model | registry-linked (Connect spans 15+ registries) | venue-operated custody + portfolio management integrated | clearing-member accounts delivering into registry accounts | registry accounts |
| Participation | "apply to participate"; qualified participants; brokers | trading members (+190 claim); brokers, airlines, corporates, speculators | clearing members + traders under exchange rules | buyers, suppliers, intermediaries |
| Integrity mechanics | CCP-eligible contract delivery; registry network; automated tagging for eligibility | double-counting/retirement safeguards; immutable lifecycle records; eligibility checks | legal instrument under EU ETS directive; clearing-house delivery rules | ICVCM CCP-eligible programme; registry retirement |
| Regulatory posture | AFSL for ACCU market-making (wholesale clients); futures broker disclosures | member exchange (jurisdiction pages: Singapore/Brasil/UK) | regulated derivatives exchange + clearing house | registry/standard-body posture |
| Market data | Xpansiv Data (spot transactions, bid/offer, forwards) | live pricing; transparent fees | settlement prices; margin rates | published indexes |
| Adjacent layers | brokerage (Evolution), portfolio (Connect), registries, powered-by partner exchanges | SaaS exchange infrastructure; collateral management; ratings/verification partnerships | options/EFP/related futures; education; data | methodologies, certification, buyer channels |

### Stability across the sample

Present in all three core samples (B/C evidence for cross-product claims):

1. carbon instruments anchored to an issuing program/registry or compliance scheme [B]
2. standardized instruments (spec-defined contracts or allowance definitions) alongside,
   for some venues, project-specific units [B]
3. governed participation (admission/membership/clearing membership) and venue rules [B]
4. an execution mechanism producing priced, recorded trades [B]
5. post-trade settlement that transfers the instrument between the parties' holdings
   (venue custody, registry accounts, or clearing delivery) [B]
6. registry linkage / provenance anchoring of what is delivered [B]
7. integrity mechanics against double-counting (explicit at ACX; structural at CBL via registry
   network and eligibility-tagged contracts; legal at ICE via the allowance construct) [B]
8. price discovery as a first-class output (books, auctions, data feeds, settlement prices) [B]

Present in two of three (common, not defining): auctions [A:CBL, ACX]; RFQ-like offer surfaces
[A:CBL RFQ, ACX market board]; OTC recordation/settlement rails [A:CBL explicit, ACX settlement
portal]; market data products [A:CBL, ACX]; portfolio/position management surface [A:CBL Connect,
ACX custody+portfolio]; brokerage/intermediary channel [A:CBL Evolution, ACX broker membership,
Puro intermediaries].

Single-product (kept product-specific): AFSL licensing detail (Xpansiv); immutable-record and
no-separate-registry-accounts claims (ACX); delivery-period/delay/failure formalism (ICE);
indexes (Puro); SaaS white-label exchange offering (ACX); powered-by partner exchanges (Xpansiv).

## Canonical Model

### Level 0 — Defining Invariant

Four properties; removing any one stops the product from being recognizable as a carbon trading
platform:

1. **Tradable carbon instruments** — emissions allowances or carbon credits represented on the
   venue as transactable units (standardized contracts and/or project-specific lots), each
   anchored to an issuing program, registry, or compliance scheme. Remove → a generic commodity
   or financial venue, not a carbon venue.
2. **Governed multi-party execution** — the venue admits eligible participants and provides a
   rule-governed mechanism (order book matching, auction, RFQ/offer board, or recorded bilateral
   execution) that produces executed trades between counterparties. Remove → a listing site,
   data service, or marketing catalog.
3. **Priced, recorded trades feeding price discovery** — every execution yields a record with
   price and quantity that the venue surfaces (book, prints, indices, settlement prices).
   Remove → brokerage directory / price-reporting service.
4. **Post-trade settlement of instrument ownership** — a defined process that transfers the
   instrument between the parties' holdings (venue custody, registry accounts, or clearing-house
   delivery), with integrity safeguards that prevent the same unit being sold or claimed twice.
   Remove → a betting/quote surface, not a market for the instrument itself.

Deliberately NOT in Level 0 (checked against the historical/alt-form question): order books
(auctions and RFQs are equally valid execution forms), spot vs futures (both observed),
venue-operated custody vs registry-account delivery (both observed), market data feeds,
portfolio tools, API access, tokenization, 24/7 operation, retail access (the sample is
uniformly professional/wholesale — but that is a market-structure observation, not the
defining structure), multi-instrument scope (RECs/water/fuels are adjacency).

Historical check: a 2000s-era carbon exchange (e.g., the Chicago Climate Exchange pattern:
own registry + trading facility + clearing; or early EU ETS OTC executed via brokers and
recorded on a venue) satisfies the four properties without any modern feature. Regional
compliance venues (e.g., allowance futures on a national exchange) satisfy it with no
voluntary-market features at all. So the minimal definition is not an artifact of the
2020s voluntary-market platform wave.

### Level 1 — Common Mature Structure

- **Instrument specification & eligibility** — published criteria for what a deliverable unit
  must be (registry of origin, eligibility scheme, vintage/type classes); standardized benchmark
  contracts built on those criteria, alongside project-specific credit trading.
- **Auction mechanism** — bulk-sale and allocation auctions as a second execution surface.
- **RFQ / offer-board channel** — buyer- or seller-specified requests distributed to the
  participant base, with negotiation and platform-finalized execution.
- **OTC post-trade settlement** — bilateral trades recorded and settled through the venue's
  rails without needing bilateral counterparty agreements with every participant.
- **Market data & price-signal products** — transaction prints, bid/offer data, settlement
  prices, sometimes indexes.
- **Holdings/positions view** — venue custody accounts or portfolio views of what the
  participant holds and has traded.
- **Registry integration** — delivery/settlement lands in, or is mirrored against, authoritative
  registries; eligibility tagging across registries.
- **Integrity machinery** — double-counting/retirement safeguards, immutable/lifecycle trade
  records, eligibility verification.
- **Admission & rules framework** — participant application/membership, rulebooks, fee
  structures; wholesale/professional orientation.

### Level 2 — Variant / Optional Structure

- Instrument scope: compliance allowances only / voluntary credits only / both;
  carbon-only vs multi-environmental (RECs, water, fuels) — both poles observed.
- Spot vs derivatives (futures/options with clearing and margin) — ICE pole.
- Delivery form: venue custody vs direct registry-account delivery vs clearing-house delivery.
- Session-based vs continuous/24-7 operation.
- Powered-by/white-label infrastructure: venue operator selling the platform itself (SaaS) or
  operating regional partner exchanges.
- Intermediary layer: integrated brokerage/execution services vs open member access.
- API/programmatic access; indexes; collateral management of credits.
- Auction-based primary allocation (e.g., government allowance auctions) — plausible variant,
  not directly observed in the fetched sample; not asserted in the final document.

### Level 3 — Vendor-specific (kept out of the final document)

- Xpansiv: GEO®/N-GEO®/C-GEO®/CCP-GEO/CORSIA-CP1 contract brands; "first VCM standardized
  contract in 2020"; T+0 claim; 1,100+ participants / 300 Mt claims; Connect "15+ registries";
  AFSL 536825; IATA ACE partnership; JSE-V and RVCMC powered-by venues; Evolution Markets
  brokerage stack; C-Capsule registry.
- ACX: CET/GNT/GNT+/SDGT/RET/HOT/XCT contract acronyms; "1 contract = 1,000 tCO2e"
  specification; +21 Mt / +190 members / +30 countries claims; "first integrated system /
  first digital standardised contract / first turnkey solution / first platform to eliminate
  the doubles" self-claims; BSI verification and BeZero ratings partnership quotes; trade
  portal at trade.aircarbon.co; SaaS offering.
- ICE: EUA contract code C, lot = 1,000 EUAs, €0.01 tick, quarterly series structure, TAS
  markers, delivery-period/delay/failure definitions, ICE Endex rulebook reference.
- Puro.earth: CORC instrument, Puro Standard methodologies list, MyPuro, Puro Connect APIs,
  CDR market stats (74% share claim, 1.82 Mt removed, €131.27/tonne, 865 buyers, 332 suppliers).

## Vendor-specific Findings

Consolidated above under Level 3. Additionally:

- CBL explicitly frames itself as both exchange and OTC settlement rail — i.e., the venue
  competes with bilateral settlement rather than only hosting on-book trades. Treated as a
  common posture (ACX settlement portal is analogous) but the "without bilateral agreements"
  phrasing is vendor-specific.
- ACX's "no separate registry accounts" custody is a deliberate departure from the
  registry-account settlement pattern (CBL/ICE). Both are settlements of the same L0
  property; neither is definitional.
- ICE's contract is the only fetched evidence reaching true contract-specification precision;
  numeric claims about the other venues stay out of the final document.

## Boundary Findings

1. **vs Carbon Credit Management** (documented sibling): management is the holder-side system
   of record — custody, lifecycle, evidence, retirement records. Trading is the venue-side
   execution and price formation. Test: remove the multi-party execution mechanism and what
   remains is credit management; remove the holder's custody/evidence posture and what remains
   is trading. Real products blur at the edges (venues offer custody accounts; Connect offers
   lifecycle views), but the defining jobs differ. Also: retirement/claims live on the
   registry/management side; venues settle ownership and reference registries.
2. **vs Energy Trading Platform**: energy exchanges trade power/gas (and other commodities)
   with carbon as one instrument among many; the carbon venue is organized around carbon/
   environmental instruments. Test: strip energy commodities and the carbon venue stands;
   strip carbon and a carbon venue stops existing while an energy exchange continues.
   (Xpansiv and ICE both span this line — they are multi-commodity platforms whose carbon
   markets instantiate this Type.)
3. **vs Registry systems / standards-body infrastructure**: registries authoritatively issue,
   transfer, and retire; venues execute and settle trades between parties and depend on
   registries for delivery and integrity. Puro.earth marks the seam: registry + certification
   + buying channels, but not a governed multi-party execution venue.
4. **vs Marketplace (05.02) / Online Auction Platform (05.18)**: marketplaces list offers and
   negotiate bespoke, often non-fungible deals; trading venues standardize the instrument,
   govern execution under a rulebook, and operate settlement. Test: if each deal is a bespoke
   negotiated transaction over uniquely described goods, it is a marketplace; if units are
   spec-defined and fungible-class with venue-governed execution and settlement, it is trading.
   Auctions exist in both — the difference is what is auctioned (standardized instrument lots
   under venue rules vs bespoke listings).
5. **vs Retail Trading Platform / Brokerage (08)**: carbon venues are professional/wholesale
   markets with admission criteria (members, qualified participants, clearing members);
   retail trading platforms serve consumers. No consumer accounts in the sample.
6. **vs Cryptocurrency Exchange / tokenized-carbon platforms**: tokenized credits traded on
   crypto venues exist in the wider market but were not observed in the fetched sample; the
   boundary is recorded as structural inference only (issuance/anchor differs), no claims made.
7. **vs Brokerage/market execution services**: broker-mediated execution (e.g., phone/OTC desks)
   is a service, not a venue; venues are where execution and recordation are governed. Products
   bundle both (Evolution Markets alongside CBL).

## Uncertainties

- Two planned samples (CIX, CTX) were unreachable; the model rests on three core products
  (Xpansiv/CBL, ACX, ICE EUA) plus Puro.earth as boundary context. All three core products are
  exchange-form venues; a strong marketplace-form "carbon trading platform" (if any exists in
  the market) may be under-sampled. Mitigation: the L0 does not assume exchange-form mechanics
  (order book), so an auction/RFQ-form venue is covered.
- Help-center-level operational docs (rulebooks, membership guides, fee schedules) were not
  fetched for Xpansiv and ACX; their mechanics are known at product-page depth. Precision in
  the final document is calibrated accordingly (no numeric limits, no fee values, no T+0
  claims generalized).
- Cash-settled carbon derivatives and government-run allowance auctions are plausibly in-market
  but were not directly observed; recorded as unverified variants only.
- Tokenized-carbon venues (Toucan/KlimaDAO/Carbonmark) not researched; boundary recorded
  structurally.
- Retirement at the venue: ACX claims safeguards against double retirements and CBL's Connect
  offers lifecycle management, but none of the sampled venues positions retirement (the claim
  event) as the venue's primary job; the canonical reading — venues settle ownership, registries
  retire — is calibrated as "settlement vs claims" rather than a hard universal rule.

## Final Synthesis

A Carbon Trading Platform is a governed market venue for carbon instruments. Its defining core:
(1) tradable carbon instruments — allowances or credits anchored to issuing programs/registries;
(2) governed multi-party execution under venue rules (order book, auction, RFQ/offer board, or
recorded bilateral execution); (3) priced, recorded trades that form the market's price signals;
(4) post-trade settlement that transfers instrument ownership between parties' holdings with
integrity safeguards against double-counting. Around this core, mature venues add standardized
benchmark contracts and eligibility criteria, auctions, RFQ channels, OTC settlement rails,
market data, holdings views, registry integration, and admission/rulebook frameworks. Variants
split along compliance vs voluntary scope, spot vs derivatives, custody model, instrument breadth,
and infrastructure (white-label/SaaS) posture. The Type is distinct from custody-side credit
management (execution vs evidence), from energy trading (instrument scope), from registries
(execution vs authoritative issuance/retirement), from marketplaces (standardized governed
execution vs bespoke deals), and from retail brokerage (professional membership markets).
