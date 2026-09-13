# Research Notes — Energy Trading Platform

## Research Goal

Understand what an "Energy Trading Platform" is as an Application Type: what the market actually means by the term, which side of the energy market the software sits on (market venue vs. participant's own desk), what objects and workflows define it, and how it differs from the neighboring Types already processed in the atlas (Energy Scheduling & Settlement, Energy Forecasting Platform, Carbon Trading Platform) and from the financial-trading family in the finance domain.

## Initial Boundary (hypothesis before research)

The term "energy trading platform" is used loosely in the market for at least two different things:

1. **Venue-side systems** — power exchanges and gas hubs (Nord Pool, EPEX SPOT, EEX, Trayport-style broker platforms) that organize multi-party price formation, matching, clearing, and rulebooks.
2. **Participant-side systems** — what the energy industry calls ETRM/CTRM (Energy Trading & Risk Management / Commodity Trading & Risk Management): one company's system for capturing its own deals, building positions, valuing them, and managing risk.

Internal consistency signals before any product research:

- The already-processed sibling **Energy Scheduling & Settlement** explicitly ratified the participant-side reading: its document describes the trading system as the thing that "captures deals and manages risk before anything must be scheduled" and its boundary test reads: "if the system's center of gravity is deal capture, valuation, and risk, it is trading; if it is submissions under deadline and settlement statements reconciled to closure, it is this Type." Its Related-Types row says Energy Trading Platform "holds deals, positions, and risk — the front and middle office."
- **Energy Forecasting Platform** (processed) describes Energy Trading Platform as the "downstream consumer" whose work "centers on positions, orders, and bids."
- The finance-domain directory convention (three processed leaves: Retail Trading Platform, Professional Trading Terminal, Algorithmic Trading Platform) treats "Trading Platform" naming as participant-side software; the directory has no generic exchange/venue leaf outside crypto and carbon.
- **Carbon Trading Platform** (processed, §21) flagged a joint-review seam under the *venue* assumption ("remove carbon → the energy exchange continues"). This flag needs discharge from this side.

Decision taken: research the participant-side reading as primary (consistent with both §19 neighbors and the §08 naming convention), while sampling one venue product as a boundary anchor and one asset-optimization bidding product as the modern asset-backed pole. The carbon seam is discharged via the side-of-market test (see Boundary Findings).

## Research Questions

1. What is the unit of record? What does a "deal" carry (commodity, delivery period, volume, price, counterparty, channel)?
2. How do positions form from deals, and how are they valued (mark-to-market, price curves)?
3. What market channels feed the record (exchange connectivity, broker/OTC capture, bid submission for owned assets)?
4. What risk machinery is present (market risk, credit exposure, limits)?
5. What energy-specific structure exists (delivery periods/tenors, physical vs. financial, multi-commodity, grid/pipeline logistics)?
6. Where does the handoff to scheduling/settlement happen, and what stays on each side of that seam?
7. Where do physical assets (generation, storage, load) enter — asset-backed trading vs. merchant trading?
8. What variants exist (suite vs. point tools, SaaS vs. on-prem, commodity focus, regional market packs, automated bidding)?
9. Venue-vs-participant side test: which side is this Type on, and what does the other side look like in primary evidence?

## Representative Products

| Product | Vendor | Role in sample | Tier / posture |
|---|---|---|---|
| Allegro | ION Commodities | full-suite, energy-native ETRM for utilities/power producers | institutional, front-to-back |
| Openlink | ION | largest multi-commodity CTRM, global scale, sophisticated risk | institutional, front-to-back |
| Aspect | ION (Aspect Enterprise) | mid-market, multi-tenant SaaS ETRM; oil/products/metals/carbon | mid-tier, SaaS-first |
| Mosaic | Fluence | AI bidding/optimization software for solar, wind, storage assets | modern asset-backed pole |
| Nord Pool | Nord Pool AS | European power exchange — venue-side **boundary anchor** (not part of the Type) | market operator |

Rationale: three ETRM products give the Type's center of gravity at different scales and philosophies (suite vs. SaaS; energy-native vs. multi-commodity); Mosaic probes the asset-automation edge; Nord Pool anchors the venue boundary from primary evidence. Note: Aspect's own domain (aspectenterprise.com) now redirects into ION's site; official evidence for all three ION products is the vendor's product pages.

## Sources

Fetched 2026-09-08 (WebFetch, markdown):

1. ION — Allegro product page — https://iongroup.com/products/commodities/allegro/ (Tier 2)
2. ION — Openlink product page — https://iongroup.com/products/commodities/openlink/ (Tier 2)
3. ION — Aspect product page — https://iongroup.com/products/commodities/aspect/ (Tier 2, fetched via aspectenterprise.com redirect → iongroup.com)
4. Fluence — Mosaic Intelligent Bidding Software — https://fluenceenergy.com/mosaic-intelligent-bidding-software/ (Tier 2; per-market login portals for CAISO/NEM/ERCOT visible in nav but gated)
5. Nord Pool — site root and navigation structure — https://www.nordpoolgroup.com/en/ (Tier 2; used for venue boundary only)

Internal cross-references: applications/energy-scheduling-settlement.md, applications/energy-forecasting-platform.md, applications/carbon-trading-platform.md, STATUS.md boundary lines.

**Source-access limitation:** All product evidence is vendor product pages (Tier 2 marketing/positioning material). None of the vendors expose operational help centers or user guides at reachable URLs this pass (ION resources are gated behind a resource center; Fluence per-market portals require login). Consequently: no precise operational details (field-level deal schemas, confirmation flows, exact limit types, numeric tolerances, screen-by-screen workflows) are asserted anywhere; all workflow claims are kept at the strength the vendor pages support.

## Product Observations

### Product 1 — Allegro (ION Commodities)

Evidence layer: A (directly observed on the official product page).

- Self-positioning: "an energy trading and risk management (ETRM) solution uniquely designed for utilities and energy companies trading and managing power and renewables, natural gas, liquid hydrocarbons, and environmental products."
- Commodity breadth is energy-specific: power and renewables, natural gas, liquid hydrocarbons, environmental products; FAQ claims "architected from its core to address the specific needs of energy commodities."
- Front-to-back framing: "As a front-to-back, multi-commodity solution, Allegro unifies processes across the enterprise to streamline energy trading operations, risk management, and regulatory compliance reporting in a single solution."
- Key-feature list (vendor's own enumeration): real-time position visibility; robust risk management; advanced analytics; regulatory compliance; **flexible deal capture**; extensible framework.
- Workflow framing: "Centralize physical and financial trading. Connect the front-, middle-, and back-office." — "supports the management of physical and financial energy transactions from deal to cash."
- Analytics: "Measure portfolio risk with sophisticated models. Value complex and esoteric contracts." — "asset optimization insights."
- Logistics: "Automate scheduling activities. Connect seamlessly to external operational systems."
- Connectivity module ("Connect"): "Connectivity is available for market price data providers, various trading exchanges, gas pipelines, power system operators, and regulatory trade repositories."
- Credit module: "Manage and report on credit requests, credit ratings, credit review procedures, limits, credit availability, and credit value at risk."
- Anti-spreadsheet positioning (FAQ): a CTRM is pitched as the replacement for running the business on spreadsheets, providing "controls, approvals, and messaging."

### Product 2 — Openlink (ION)

Evidence layer: A.

- Self-positioning: "for companies that engage across multiple commodities markets on a global scale, with sophisticated needs around risk and physical logistics. The front-to-back solution supports all commodity asset classes with advanced risk management, extensive workflow automation, and customization capabilities."
- Scope statement (FAQ): "one integrated solution … covers end-to-end processes from equity production, gas processing, forecasting, sourcing, and storage/transport optimization to marketing, trading, contract management, and position management through to risk, accounting, reporting, and compliance … ensures that traders and risk managers can see correct positions at all times."
- Connectivity: "Connect to market data providers and exchanges."
- Trading and analytics module: "Streamline trade capture with direct integration to major exchanges. Retrieve existing trades, run reports, and calculate impromptu or on-the-fly simulations and stress testing scenarios."
- Risk module: "real-time mark-to-market, Greeks, VaR, and credit exposure monitoring."
- P&L: "Optimize trading strategies with real-time P&L visibility."
- Post-trade module: "Facilitate P&L reconciliation, invoicing, and book closure (end-of-day, month-end, and year-end closure)."
- Scheduling and logistics module: "Easily plan and replan asset allocations and movements for any mode of transportation, including truck, rail, pipeline, vessel, and grid."
- Scale claims: "aggregated real-time position reporting for the largest trading operations"; in-memory data grid.

### Product 3 — Aspect (ION)

Evidence layer: A.

- Self-positioning: "for traders, refiners, producers, and marketers of crude oil, refined petroleum products, petrochemicals, and metals, as well as carbon traders. The front-to-back, multi-tenant SaaS solution covers physical and financial trading workflows with integrated market data, sophisticated analytics, and real-time reporting."
- System-of-record framing (FAQ): "a trusted, company-wide system of record, ensuring your entire business can access a single source of truth on demand."
- Coverage: "complete coverage of the entire trade capture and risk management lifecycle."
- Data: "Standard exchange connectivity with seamless continuity of service"; "Integrated with DSC [Decision Support Center] for real-time market prices"; "Pre-packaged with industry-standard reference data."
- Reporting/UX: web-based, "hundreds of standard reports," customizable screens via a scripting language, real-time calculations.
- Environmental-adjacent module: Carbon Zero — "a simple, fast trading and inventory solution that covers the full carbon and renewable certificate lifecycle."
- Same anti-spreadsheet FAQ framing as Allegro (shared ION template).

### Product 4 — Fluence Mosaic (asset-optimization / bidding pole)

Evidence layer: A.

- Self-positioning: "Intelligent, AI-powered bidding for solar, wind, and energy storage" — "maximizes renewables and storage revenue with intelligent, automated bidding software and trading solutions."
- Workflow (vendor's own three-step enumeration): FORECASTING with machine learning (prices, supply, demand) → OPTIMIZATION ("advanced co-optimization of all applicable products for day-ahead and real-time markets") → AUTOMATION ("Incorporate your organization's risk tolerance levels with our bidding strategy expertise to prepare ISO-compliant bids for submission while following operational constraints").
- Market-bounded: per-market editions (CAISO, ERCOT, MISO, NEM Australia, Japan); separate market-specific login portals.
- Asset-anchored: "Technology Agnostic — Mosaic supports energy storage and renewable technologies from any provider, and is configured to meet the unique warranty constraints and operating parameters of each asset."
- Simulation environment ("Experiment with simulated assets and varying risk preferences"); cloud-based platform.
- Service posture: "Mosaic Trading Solutions provide expert support … including bid-to-bill trading services" (managed-service wrapper).
- **Structurally notable:** the page nowhere claims deal capture, position keeping, mark-to-market, or a trade blotter. The object of work is the bid/offer for owned assets and its revenue outcome, not a book of deals. (Vendor-published revenue-uplift percentages on the page are marketing claims and are deliberately not carried into any document.)

### Product 5 — Nord Pool (venue-side boundary anchor)

Evidence layer: A (site structure and public market pages).

- Self-positioning: "Nord Pool runs the leading power market in Europe … We offer day-ahead and intraday markets to our customers."
- Venue machinery visible in navigation: membership ("Becoming a customer," "Membership list"), day-ahead trading (order types, price calculation, capacities, ramping, curtailment/decoupling), intraday trading (order types, continuous), power futures (with Euronext), clearing (settlement, collateral, margin model), APIs and ISV partners, rules & regulations, market surveillance, REMIT compliance reporting services, member trading UIs (Intraday Web, auction portals), data portal.
- The venue's jobs — price calculation for many parties, market coupling across bidding areas, clearing/collateral, rulebook and surveillance — are all multi-party functions. None of them is the participant's own book.

## Cross-product Comparison

| Structure / capability | Allegro | Openlink | Aspect | Mosaic | Nord Pool (venue) |
|---|---|---|---|---|---|
| Own-book participant posture (one company's own trading) | ✔ | ✔ | ✔ | ✔ (own assets) | ✘ (multi-party market) |
| Deal / trade capture as record (physical + financial) | ✔ "flexible deal capture," "deal to cash" | ✔ "trade capture," "retrieve existing trades" | ✔ "trade capture and risk management lifecycle" | ✘ (bids, not booked deals) | ✘ (venue executes; doesn't hold a participant's book) |
| Position / exposure view derived from deals | ✔ "real-time position visibility" | ✔ "see correct positions at all times," aggregated real-time position reporting | implied by trade lifecycle + reporting (not explicit on page) | ✘ | ✘ |
| Valuation / P&L | ✔ "value complex and esoteric contracts" | ✔ real-time P&L, mark-to-market | ✔ real-time calculations and reporting | ✘ (revenue maximization claims, not a book) | ✘ (publishes prices, not participant P&L) |
| Market risk measurement | ✔ "portfolio risk with sophisticated models" | ✔ VaR, Greeks, what-if, stress | ✔ "risk management lifecycle" | ✔ (risk tolerance in bidding; forecast uncertainty) | ✘ (surveillance ≠ participant risk) |
| Credit / counterparty exposure | ✔ credit module incl. credit VaR | ✔ credit exposure monitoring | not stated on page | ✘ | ✘ (venue collateral is different) |
| Market data / price curves | ✔ via Connect (price data providers) | ✔ market data providers | ✔ DSC integration, exchange data | ✔ (forecasts prices) | ✔ publishes market data (its own product) |
| Exchange / venue connectivity | ✔ trading exchanges | ✔ direct integration to major exchanges | ✔ standard exchange connectivity | ✔ (ISO market submission) | n/a (is the venue) |
| Bid preparation / submission to market | via connectivity, not core claim | not core claim | not core claim | ✔ ISO-compliant bids, automated | receives bids |
| Scheduling / logistics integration | ✔ automate scheduling activities | ✔ scheduling & logistics module (truck/rail/pipeline/vessel/grid) | not stated | ✘ (operational constraints respected, not logistics) | ✘ |
| Settlement / invoicing / book close | ✔ "deal to cash" | ✔ reconciliation, invoicing, end-of-day/month/year book closure | not stated | ✘ ("bid-to-bill" is a managed service, not a book-close feature) | ✔ clears & settles the market (multi-party) |
| Regulatory / trade reporting | ✔ regulatory compliance reporting | ✔ compliance in end-to-end scope | not stated | ✘ | ✔ REMIT reporting services (its own product) |
| Price formation for many parties / clearing / rulebook | ✘ | ✘ | ✘ | ✘ | ✔ its defining machinery |

Reading of the table:

- The three ETRM products agree on a stable structure: **own-book deals → positions → valuation/P&L → risk → downstream handoff (scheduling, settlement, reporting)**, fed by market data and connected to exchanges (evidence B, cross-product commonality).
- Mosaic shares the own-book posture and the market-boundedness but replaces the deal/position record with forecast→optimize→submit automation around owned assets — a different center of gravity (evidence A per product).
- Nord Pool shows the opposite side: the venue's core (matching, price calculation, clearing, rulebook) is absent from every participant-side product, and the participant-side core (deal book, positions, P&L) is absent from the venue (evidence A).

## Canonical Model — abstraction layers

### L0 — Defining Invariant (minimal)

Three jointly-held structures. Removing any one collapses the Type:

1. **Own-book participant side.** The system exists for one energy market participant's own trading — its deals, its positions, its money, its risk. Not a multi-party venue. (Remove → an energy exchange/venue, a different Type; energy venues currently have no dedicated leaf in the directory.)
2. **Energy deals / trades of record.** Persistent, individually held records of energy transactions — commodity, time-structured delivery (period/tenor), volume, price, direction, counterparty and channel; in physical and/or financial form; entering the record either through execution via market channels (exchange connectivity) or through capture of bilateral/broker deals. (Remove → analytics or risk tooling with nothing traded.)
3. **Position-and-value view derived from the deals.** Net exposure aggregated by delivery period, instrument, asset, book, and market, measured against price data — the basis for P&L and risk. (Remove → a deal blotter/log with no book.)

Load-bearing check (jointly-held):
- 1 alone = market data/decision tooling with no record.
- 2 without 3 = deal log/blotter.
- 3 without 2 = analytics sandbox with no transactions.
- 1+3 without 2 = position dashboard with no transaction source.

Energy-specificity inside L0: the deals are denominated in energy commodities and carry **time-structured delivery** (hours for power, days for gas, cargoes/periods for liquid fuels) — this is what makes the record an energy book rather than a securities book. Physical form is common but not required: a financially settled energy book still satisfies L0.

Historical / market-sample check: the paper-era ancestor — a trade book (deals recorded as they are struck by phone/telex), a position ledger aggregated by delivery period, and hand-computed P&L against posted prices — satisfies all three L0 legs with no exchange APIs, no cloud, no AI. The vendors' own FAQs confirm the thin ancestor is the spreadsheet: both Allegro's and Aspect's FAQ pitch the product as the replacement for "running the business on spreadsheets," i.e., spreadsheets are the pre-software realization of the same three structures. L0 passes the check.

### L1 — Common Mature Structure

Present across the sampled mature products (evidence B), not required to recognize the Type:

- Market data and price curves ingested from external providers (the valuation input).
- Execution connectivity: direct integration to exchanges/venues; in modern products also market API access.
- Market-risk apparatus: portfolio risk models, VaR-family measures, what-if/stress simulation.
- Credit/counterparty exposure monitoring and limits (module-level in the suites).
- Downstream handoff machinery: scheduling/logistics automation, settlement/invoicing, P&L reconciliation, end-of-day/month/year book closure.
- Regulatory/trade reporting support (e.g., trade-repository connectivity).
- Front/middle/back-office role separation and configurable screens/desktops; standard report libraries.
- Physical-side support: logistics modes, asset linkages (this is also where commodity diversity shows: pipeline/vessel/grid scheduling in one product).

### L2 — Variant / Optional Structure

- Commodity focus: power/renewables-centric, gas-centric, oil/products-centric, multi-commodity.
- Deployment: multi-tenant SaaS vs. on-prem enterprise; in-memory/high-volume editions.
- Asset-backed vs. merchant posture: trading around owned generation/storage/load vs. proprietary trading.
- **Asset-optimization / automated-bidding pole** (Mosaic): forecast→optimize→submit-ISO-bid automation for renewables/storage portfolios, per-market editions, risk-tolerance configuration, simulation environments, managed "bid-to-bill" service wrappers. Structurally adjacent: its object of work is the bid and the asset's revenue, not the deal book — see Boundary Findings.
- Certificate/carbon instrument modules (trading and inventory for carbon and renewable certificates) inside an ETRM.
- Regional market packs (market-specific rules/deadlines), language/regulatory localization.
- Suite composition: some suites extend back into forecasting, optimization, hedge accounting, shipping; others are deliberately lean.

### L3 — Vendor-specific (Research Notes only)

- ION's portfolio packaging (Allegro/Openlink/Aspect share a template; "Connect," DSC, Carbon Zero, FEA, WAM, Softmar module names; ION Cloud).
- Openlink's Apache Kafka streaming and in-memory data grid positioning.
- Fluence Mosaic's per-market portal structure (CAISO/NEM/ERCOT logins), named Mosaic Trading Solutions service tier, and vendor-published uplift percentages (marketing claims — not carried into the final document).
- Nord Pool's specific market mechanics (bidding areas, SIDC coupling, 15-minute MTU transition, EPAD auctions) — venue-side detail kept for boundary purposes only.

## Boundary Findings

1. **Energy Scheduling & Settlement (downstream seam — most important).** Both Types live on the participant side of wholesale markets and suites bundle them. Object-of-record test ratified from that leaf's side: deal capture + valuation + risk = trading; submissions under deadline + settlement statements + reconciliation = scheduling & settlement. From this side the same test holds: the ETRM sample's center is the deal/position/value record; scheduling products' center is the market submission and the settlement statement. Where a suite contains both (Allegro, Openlink do scheduling/logistics), the leaf boundary follows the object of record, not the suite box.
2. **Energy Forecasting Platform (upstream input).** Forecasts (price, production, load) are an input to trading decisions and bid construction; the trading platform does not own the forecast record. Consistent with that leaf's recorded boundary (trading = "downstream consumer").
3. **Carbon Trading Platform (§21) — joint-review flag DISCHARGED.** That leaf's seam assumed both leaves were venues and proposed an instrument-scope test. From the evidence of this pass, the two Types sit on **opposite sides of the market**: a carbon trading platform is the venue organized around environmental instruments; an Energy Trading Platform is a participant's own-book system. No overlap of defining structures. The participant platform may even *trade* carbon instruments (environmental products are among Allegro's named commodities; Aspect ships a carbon-certificate module) — which confirms rather than blurs the seam: the carbon venue is a market the participant platform trades against. Instrument-scope test is moot; recommend closing the flag.
4. **Energy venues (power/gas exchanges) — directory gap.** Under the ratified participant-side reading, venue-side energy market software (Nord Pool, EPEX SPOT, EEX, broker platforms like Trayport) is not covered by this leaf, by carbon-trading-platform (carbon-only scope), or by any finance-domain leaf (the directory has no generic exchange/venue Type). Recorded as a taxonomy gap; not resolvable within this leaf.
5. **Finance-domain trading platforms (§08): Retail Trading Platform / Professional Trading Terminal / Algorithmic Trading Platform.** Different instruments (securities vs. energy commodities with delivery obligations), different principals (individual investor vs. organization), different record structure (account/position in a broker vs. delivery-period energy book). The who-decides test from the algo leaf separates automation of decisions; here even the automated-bidding pole remains asset-and-market-submission anchored rather than a generic strategy framework.
6. **Brokerage Platform (§08).** Broker-operated client platform centered on the account relationship; the energy trading platform has no customer of its own being served — it is the participant itself.
7. **Asset-optimization / bidding software (Mosaic pole).** Held as an L2 variant leaning boundary: shares own-book + market-boundedness but lacks the deal/position/value record. If future directory work creates a "market bidding/optimization" leaf, the split would happen there. Kept inside this Type's variant space because suites integrate the same capability ("asset optimization insights") and because asset-backed participants experience it as part of trading.
8. **Financial Risk Management Platform / Treasury Management (§08).** Generic financial risk and cash/funding systems do not hold delivery-period energy deals; energy risk here is deal-native (volume/shape/credit on physical deliveries). Boundary noted, not deeply evidenced this pass (no §08 sample fetched) — assertion kept weak.
9. **Battery Energy Storage Management / VPP / Demand Response (§19).** Asset operations and DER dispatch systems run the physical asset; the trading platform holds the commercial record and the market interactions. Mosaic's operational-constraint respect (warranty constraints, operating parameters) shows the seam: constraints come from the asset system, revenue and bids live in the trading side.

## Uncertainties

1. All product evidence is Tier 2 (vendor product pages). Operational depth (deal lifecycle states, confirmation flows, exact limit/breach handling, screen inventories) is unverified; the final document deliberately stays at structure level and uses calibrated wording.
2. Aspect's page is lighter than its peers on positions/P&L specifics (it emphasizes the trade-capture/risk lifecycle and reporting); position-keeping was taken as implied rather than explicitly quoted.
3. The Mosaic classification (variant vs. separate Type) is a judgment call based on one product's pages; flagged in Boundary Findings for future review.
4. Venue-side breadth (broker platforms like Trayport, regional exchanges, gas hubs) was not sampled this pass; the venue boundary rests on Nord Pool alone — adequate for the side-of-market test, insufficient to characterize venues as a Type.
5. Regional products (Asian/Japanese desks, Latin American markets, Indian power exchanges) were not sampled; the L0's historical and structural checks are the mitigation.

## Final Synthesis

An **Energy Trading Platform** is an energy market participant's own-book trading system of record. Its defining core is three jointly-held structures: (1) the own-book participant posture — the system serves one organization's own energy trading, not a multi-party market; (2) the energy deal of record — a persistent record of each energy transaction with its commodity, time-structured delivery, volume, price, direction, and counterparty/channel, in physical or financial form; (3) the position-and-value view derived from the deals — net exposure by delivery period, instrument, asset, and book, measured against prices as the basis for P&L and risk. Around this core, mature products add market-data/curve ingestion, exchange connectivity, market-risk and credit machinery, scheduling/logistics and settlement/invoicing handoffs, regulatory reporting, and configurable front/middle/back-office workspaces. The Type's boundary is ratified on both sides: upstream forecasts feed it; downstream scheduling & settlement carries its deals into market submissions and settled money; the venue side (exchanges) and the registry side (carbon/environmental venues) are different Types on the other side of the market. The asset-optimization bidding pole is held as a variant at the Type's edge.
