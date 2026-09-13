# Research Notes — Grain Origination Platform

Research date: 2026-09-08
Slug: grain-origination-platform
Directory location: §20 Agriculture, Food & Natural Resources (between Grain Elevator Management and — after — Grain Management, both already processed)

---

## Research Goal

Determine what a "Grain Origination Platform" is as an Application Type: what objects it manages, who operates it, how grain is acquired from growers through it, how it relates to the two already-processed sibling Types (Grain Elevator Management, Grain Management), and whether the leaf is a distinct Type, an alias, or a variant.

## Initial Boundary (hypothesis before research)

- "Origination" in commodity trade vocabulary = the buy-side sourcing of physical product from producers at origin. A grain origination platform should therefore be the grain buyer's (elevator, merchant, processor) acquisition machinery: bids, grower offers, contracts.
- The grain-elevator-management pass hung a joint-review flag: its working seam was "origination = the grower-acquisition/contracting front end without custody or settlement; elevator management = the full ticketed-movement + settlement + bin-inventory system of record"; probable keep-both, ratification requested from this side.
- The grain-management pass supported keep-both (no offers/contracts/cash-bid machinery in its 4/4 samples) and asked this pass to ratify finally.
- Adjacent Types to hold: Grain Elevator Management (strongest), Grain Management, Farm Management Platform (grower side), Agribusiness ERP (packaging), Commodity Trading & Risk Management (paper positions), generic CRM, online marketplaces (grain marketplaces).
- Unknowns: is the cash-bid layer definitional or just one vendor's emphasis? Is there a marketplace/listing pole? How much settlement/delivery machinery do "origination" products actually carry?

## Research Questions

1. What are the core objects (bids/prices, offers, contracts, commitments, growers, deliveries)?
2. Who operates the system (grain buyer/merchandiser desk? network operator? grower?) and who are the external counterparties?
3. What is the canonical workflow from market price to contracted bushel to fulfilled commitment?
4. What pricing mechanics exist (price-now vs price-later, basis, grade/location spreads, discount tables, carry)?
5. Where does the Type end and Grain Elevator Management begin (tickets, settlement, bin inventory)?
6. How do implementations differ: standalone layer over ERP vs module inside ERP vs full-chain platform vs marketplace?
7. What survives the historical check (paper-era origination desk) and the regional check (AU machinery)?

## Representative Products

Selection principles applied: market representation, documentation completeness, different product philosophies, different customer tiers, regional spread.

| Product | Vendor | Pole / philosophy | Region |
|---|---|---|---|
| Bushel | Bushel Inc. (Fargo, ND) | pure-play digital origination & payments layer operated over grain buyers' ERPs; grower-app-first | US |
| AgriDigital Platform | AgriDigital (Sydney, AU) | full-chain agri-commodity supply chain platform: contracts+prices+deliveries+inventory+settlements+funding; network posture | Australia |
| Agvance Grain + Grower360 | Software Solutions Integrated (SSI) | co-op ag-retail ERP grain module; grower portal with integrated offer platform (Barchart-linked) | US |
| Ever.Ag CMS | Ever.Ag | commodity/merchandising ERP whose origination machinery (CRM, contracts, position) sits beside inventory+accounting — the seam/straddle pole | US |

Also examined / unreachable:
- **Grain Discovery** (US, online grain marketplace) — SPA returns "You need to enable JavaScript to run this app"; abandoned after 1 attempt per network rule. The marketplace/listing pole therefore rests on unverified market memory and is NOT used for definitional claims.
- **Bushel Knowledge Base** (support.bushelpowered.com) — request timed out (this pass ×1; also unreachable in the elevator pass). Bushel evidence rests on product pages + release notes.
- **AGRIS** (classic grain ERP; integrates with Bushel per Bushel release notes) — unreachable in the elevator pass; not retried.

## Sources

Tier-1:
- AgriDigital Help Centre — https://knowledgebase.agridigital.io/en — collections: Growers & Buyers Portal (15 articles), FAQ (21), Transactions/Storage/Connections/Reports modules
  - Contracts for Buyers: https://knowledgebase.agridigital.io/en/articles/7923202-contracts-for-buyers
  - Prices for Growers: https://knowledgebase.agridigital.io/en/articles/7923214-prices-for-growers
  - Definitions of common terms: https://knowledgebase.agridigital.io/en/articles/7923264-definitions-of-common-terms

Tier-2 (official product/marketing pages, release notes):
- Bushel — https://www.bushelpowered.com/agribusiness/grain ; /challenges-we-solve/drive-origination ; /agribusiness/solutions/trade ; /release-notes (Aug 2026, Q4 2025, Q3 2025, Q2 2025, Q1 2025, Q4 2024, Oct 2024, Sept 2024, Summer 2024, July 2024, Q1 2024)
- AgriDigital — https://www.agridigital.io/ ; /agridigital-platform
- Ever.Ag CMS — https://ever.ag/agribusiness/cms/
- Agvance Grain — https://agvance.net/products/grain

Sibling documents consulted (internal cross-reference):
- applications/grain-elevator-management.md + research + STATUS flag (seam + joint-review request)
- applications/grain-management.md STATUS entry (support for keep-both; condition-vs-commerce seam)

Failed fetches (network rule applied): Grain Discovery (JS-gated, ×1); Bushel KB (timeout ×1 this pass, prior-pass failure recorded); no further retries.

---

## Product Observations

### Bushel (US — digital origination layer over grain buyers' ERPs) — Evidence A

- Positioning ("Agribusiness > Grain"): "Originate More. Move Faster. Build Trust." — "Every offer, contract, and payment moves through you. But too often, it's slowed by phone calls, paper trails, and double entry. Bushel helps grain buyers unlock flow—connecting your team, your farmers, and your data so origination runs faster, cleaner, and smarter." Audiences: "Grain Traders and Processors", "Ag Retailers"; SMB vs Enterprise tiers. Solutions: CRM, Customer Portal, Commercial Portal, Trade, Bushel Pay, Farm Management, Website Management, Loyalty, Quoting, Professional Services.
- "Drive Origination" challenge page: "Origination drives your business — but every extra phone call, missing offer, or slow contract slows your growth… capture more bushels, faster, by giving farmers the digital tools they already expect and your team the visibility they need to act in real time." Farmer-side: "Let farmers make offers anytime—right from their phones—so you can keep origination moving even after hours."
- Vendor performance claims (NOT carried into the final doc): Make Offer takes "42 seconds" vs "5 minutes on the phone"; "$1.14 labor savings per offer"; customers "originate an average of 2 million bushels digitally"; mobile offers fill "58.6% vs 41.4%"; CRM saves "800+ hours per rep per year".
- Trade solution page: "Trade Management Software Built for How Farmers Actually Sell. Digital cash bid management that captures every offer — day, night, or weekend." — "producers submit firm offers, accept live cash bids, and price contracts from their phone, while your team manages everything from a single dashboard built for grain buyers." Scope of risk/admin tasks named: "updating and publishing digital cash bids in multiple systems; soliciting and managing grain offers from customers; and placing and tracking futures market orders, all in one."
- Bid distribution: "Digital cash bid management pushes one update to every channel at once: the farmer's app, your website, the in-office display, and your origination system." Slippage framing: "Bushel's Trade solution locks the price the moment the farmer taps 'accept,' with a timestamped paper trail that protects both sides."
- CRM page framing: "your merchandisers and traders see every customer's activity, position, and history—all in one place… No more guessing who's ready to sell or where contracts stand."
- Commercial Portal (outbound sales side): "Streamline execution of truck grain sales with near real-time digital tickets, grade factor alerts, and contract balances."
- Bushel Pay: "accounts receivables/payables, invoicing, embedded payments, and line of credit management"; deferred settlement options (release notes Sept 2024, Q1 2024).
- Bushel Farm pairing: "When farmers understand their cost of production, they market their grain with greater confidence—and engage sooner in conversations that drive origination… Agribusinesses can license Bushel Farm in bulk—providing farmers with premium access that strengthens engagement, loyalty, and origination potential."
- Release notes (near-Tier-1): "ERP contract creation upon filled offers" (July 2024); "self-service offer editing for farmers" (July 2024); "cash bid location searches" (July 2024); "embeddable cash bids and futures widget for non-Bushel websites" (Summer 2024); "'Trade Anywhere' for mobile offer and bid management" (Oct 2024); "minimum trade offer sizes" (Q3 2025); "upgraded Agris contract features" (Q3 2025 — Agris ERP integration named); "instant contract and settlement summary views" (Aug 2026); "CRM bin-level tracking" (Q3 2025); "PDF Discount Schedule uploads" (Q2 2025) and "manage and share discount schedules" (Q1 2025); "automated contract creation" (Q4 2025); "search scale tickets, contracts, and settlements by ID number" (Oct 2024); e-sign tools (Q4 2025).
- Interpretation: Bushel OWNS the acquisition front end (bids, offers, contracts, customer relationships, payments) and READS the elevator ERP's records (settlement summaries, scale tickets, bin levels) — the ERP keeps the books. This is exactly the "origination without custody or settlement ownership" posture the elevator pass predicted.

### AgriDigital Platform (AU — full-chain supply chain platform) — Evidence A (Tier-1 help centre)

- Root: "Australia's leading grain management software"; "agri-commodity supply chain platform… We digitize grain & fertilizer management for global agribusiness." Capabilities: real-time inventory across sites; "robust contract creation and tracking, providing live positions, automated transaction updates, and secure contract acceptance"; "Instantly access and view daily cash prices for commodities. Drive transactions by sharing price visibility across your connections"; digital settlements ("accurate recipient created tax invoices (grower payments), tax invoices, bills, deductions, levies, royalties and adjustments through automated settlements"); reporting; "The AgriDigital Platform seamlessly links contracts, deliveries, inventory and payments… every transaction is visible and verified by your Platform connections."
- Platform page: "Trade, store & broker commodities." Modules: Contracts ("Create and access a single live view of contracts with status updates"), Deliveries, Inventory, Orders, Prices ("Publish daily cash prices easily to your network"), Reporting, Payments, Invoices ("Automatic deductions including grain levies and end point royalties"), Funding (Digital Commodity Finance). Audiences: Growers, Traders, Site Operators, Brokers, Consumers (processors), Plant Breeders.
- Grower posture: "Clear, accurate records of all your contracts, deliveries, RCTIs and cash prices. Transfer stored and warehoused grain onto cash prices or contracts." Levies and varietal end point royalties auto-deducted from RCTIs. Integrations: National Grower Register (NGR), ABR, Xero, NHVR, Mettler-Toledo and Rinstrum weighing hardware.
- Help Centre — Growers & Buyers Portal (15 articles): Growers guides (Dashboard; Broker Notes "View and Download a Broker Note"; Deliveries; Inventory; Orders; **Prices** — "Confidently make grain marketing decisions with real time visibility, all in one place"; Invoices — RCTI/Tax/Brokerage). Buyers guides (**Contracts** for Buyers; Deliveries; Inventory; Invoices).
- Contracts for Buyers (Tier-1): contract list columns = Status; Created Date & Time; Date; Contract Number; Type; Price Basis; Counterparty; Location; Commodity; Primary Grade; Quantity (mt); **Quantity remaining (mt)**; Base Price; End Date. Actions: filter (System Default / Active Contracts views), Print, PDF, Share via "copy public URL link".
- Prices for Growers (Tier-1): "You can view all available Prices posted at many AgriDigital sites" — filter by "Commodity, Grade, Season, Location and Buyer"; "Only 'Available' Prices will appear"; locations without active Prices are not shown. Note the multi-buyer dimension: growers filter posted prices BY BUYER across sites — network price-board evidence.
- Definitions of common terms (Tier-1) — contract vocabulary: Season (harvest year, e.g. 2024/25); Commodity; "Price (Excluding GST): … the price … that is set by the buyer and agreed upon by the seller"; Contract Type (buyer/seller side; MT or Ha measures); Price Basis ("the delivery mode of the contract"); Counterparty (+ optional counterparty reference); Base Grade + additional grades "priced as a spread from this grade"; Total Quantity; Base Price (AUD/MT); Primary Location ("where the commodity is to be delivered to (not where it has come from)") + Add Location + Location Spread (price adjustment for alternative delivery sites); Time of Delivery; Packaging (bulk/bagged); Weights (where weight is verified); Inspection (where quality is verified); Tolerance ("allowed variation of the quantity to be delivered"); Delivery Period ("range of dates in which the contract can be delivered"); Payment Scales ("whether the contract is priced flat, or with a premium and discount table"); Carry Fee / Carry Frequency / Carry Start Date ("an increase to the base price on a contract over time"); Payment Terms (customizable); Contract Terms and Conditions (buyer-defined). Delivery terms: Location; Delivery Date; Supplier ("the Grower from which the commodity is being purchased"); Truck Registration/State Registered/Truck Type/Driver Name; Paddock; Commodity; Variety; Gross Weight Start/End; Grain Details → Calculated Grade; Selected Grade ("chosen by the bulk handler"). Order terms: origin can be "Contract, Inventory or Reference"; Order window "must be the same as or within the Contract Delivery window"; Available Qty; Order Qty.
- Interpretation: AgriDigital is the full-chain realization — origination machinery (prices, contracts, orders) PLUS custody (deliveries, inventory, storage module) PLUS settlement (RCTIs, invoices) PLUS finance (DCF funding). For the origination Type, its Contracts+Prices+Orders machinery is the relevant legs; the rest demonstrates the upward (chain-wide) straddle.

### Ever.Ag CMS (US — commodity/merchandising ERP; seam pole) — Evidence A (Tier-2)

- "CMS: An integrated solution for agribusiness… Empowering feed mills and commodity processors with one integrated ERP solution." — "a fully integrated software solution that specializes in managing the complexities of inventory management and grain accounting for commodity traders and feed manufacturers."
- Users: "grain merchandisers, elevators, feed mills, ethanol plants, and other agribusinesses involved in buying, selling, storing, and processing commodities."
- Modules: Dispatch; CRM ("maintain… one customer database. CMS offers a fully integrated CRM to capture all activity around sale and purchase opportunities"); Accounting ("tools and financial reports designed for the specific needs of the grain industry… from accounts receivable to the general ledger"); Logistics (inbound/outbound multimodal); Inventory Management ("costing methods and selling prices on a product and location level… nested formula capabilities and bin tracking features").
- FAQ: "CMS provides tools for managing commodity contracts throughout their lifecycle, including contract creation, tracking, and settlement. Users can monitor pricing terms, delivery schedules, and contract performance in real time"; "features such as contract management, position tracking, inventory management, settlement processing, and accounting integration"; "automates settlement calculations based on contract terms, deliveries, and pricing"; "visibility into commodity positions and financial exposure."
- Interpretation: the origination functions (CRM for purchase opportunities, contract lifecycle, position) exist as machinery inside an ERP whose center of gravity is inventory+accounting. No grower-facing bid/offer channel documented on the reachable page. This pole shows origination-as-module — the packaging that proves the boundary: an ERP can carry origination machinery without BEING an origination platform, just as an origination platform can exist without custody/accounting.

### Agvance Grain + Grower360 (US — co-op ag-retail ERP grain module) — Evidence A (Tier-2)

- "The Complete Grain Management System… Stay on top of your grain elevation workload and be in-step with your markets." "Agvance Grain fully automates your entire grain elevator operation."
- Grower360 portal ("comprehensive online grower portal"): growers "monitor contracts, balances, payments and more from home or on-site"; scale tickets visible "instantaneously" (customer quote, Farmward Cooperative).
- "Integrated Offer Platform": "Use Barchart right inside Grower360… Grower360 simplifies the process by collecting all your active offers in one list, including Barchart and Agvance. Offers created in Grower360 are still viewable in the Barchart app, and grain merchandisers can easily review, accept and reject them. Grower360 updates immediately when merchandisers change an offer's status, so growers can keep track effectively."
- "Contract Management: Simplify contract management. Categorize and monitor contractual obligations, plus easily capture e-signatures."
- "Market Reporting: Review real-time assessments of the market value of contracts to monitor your operation's efficiency."
- "Synchronized Dashboards: … an interactive view of your grain positions and market activities… monitor real-time activity and isolate specific commodities company-wide or by individual location." Commodity markets + trucks in yard + top customers surfaced.
- Interpretation: the offer→accept/reject→contract loop (with e-sign) and contract market-value tracking live inside the elevator ERP's grower-facing portal. Offer sourcing can be federated (Barchart app offers flow into the merchandiser's queue) — external market apps act as origination channels.

---

## Cross-product Comparison

| Structure / capability | Bushel | AgriDigital | Agvance Grain / Grower360 | Ever.Ag CMS | Layer |
|---|---|---|---|---|---|
| Buyer-published purchase prices (cash bids), commodity/grade/location-dimensioned | YES — "digital cash bid management", multi-channel push, location searches, embeddable widget | YES — Prices module: "Publish daily cash prices… to your network"; growers filter by commodity/grade/season/location/buyer | PARTIAL — commodity markets + Barchart offer platform in grower portal; bid publication not explicit on reachable page | ABSENT on reachable page | A (2 strong, 1 partial) |
| Grower-initiated firm offers / bid acceptances | YES — "submit firm offers, accept live cash bids", Make Offer, minimum offer sizes | YES — "secure contract acceptance"; grower transfers grain "onto cash prices or contracts" | YES — offers collected (incl. from Barchart), merchandiser review "accept and reject", status sync | not documented | A (3/4) |
| Buyer accept/reject decision loop | YES | YES | YES (explicit "review, accept and reject") | not documented | A (3/4) |
| Purchase contracts as typed records (price basis, counterparty, location, commodity, grade, quantity, dates) | YES (contract management, e-sign, contract summaries; field depth not documented) | YES — full field set documented Tier-1 | YES — "categorize and monitor contractual obligations, e-signatures" | YES — contract lifecycle "creation, tracking, settlement" | A (4/4) |
| Contract fulfillment tracking (quantity remaining / contract balances) | YES — "contract balances" (Commercial Portal) | YES — "Quantity remaining (mt)" as contract-list column (Tier-1) | implied ("monitor contractual obligations") | YES — "contract performance" | A (3–4/4) |
| Pricing status / price-later mechanics (unpriced commitments; "price contracts from their phone") | YES — "price contracts from their phone" | YES — Price Basis field; carry fee machinery; transfer warehoused grain onto prices/contracts | not explicit | pricing terms monitored "in real time" | A (2–3/4) |
| Market value of open contracts / position views | YES — CRM "position, and history" | YES — "live positions" | YES — "real-time assessments of the market value of contracts" | YES — "position tracking" | A (4/4) |
| Grower-facing portal/app | YES — customer portal + farmer apps | YES — Growers portal (Tier-1 guides) | YES — Grower360 | not documented | A (3/4) |
| E-signature / timestamped acceptance | YES — "timestamped paper trail", eSign | YES — "secure contract acceptance" | YES — "easily capture e-signatures" | not documented | A (3/4) |
| CRM / customer relationship records for merchandisers | YES (dedicated solution) | Connections module (7 articles) | customer DB (suite-wide) | YES (integrated CRM) | A (4/4, varying depth) |
| Discount schedules / premium-discount tables | YES — PDF uploads, sharing | YES — Payment Scales "flat, or with a premium and discount table" | not explicit | not explicit | A (2/4) |
| Futures order placement / hedging linkage | YES — "placing and tracking futures market orders" | not documented (funding yes, hedging no) | not documented (Barchart = market data/offers channel) | separate Ever.Ag risk products | A (1/4) → optional |
| Digital payments to growers | YES — Bushel Pay | YES — RCTIs, payments at click of a button | YES — payments visibility (portal) | YES — settlement processing | A (4/4) — BUT see boundary: settlement ownership varies |
| Scale tickets / custody / bin inventory of record | NO — reads from ERP (summaries, bin-level CRM tracking) | YES — Deliveries/Inventory/Storage modules | YES — scale tickets (RFID), bin inventory | YES — inventory/bin tracking | SPLIT — the elevator seam |
| Multi-location delivery terms / location pricing | YES — cash bid location searches | YES — Primary/Add Location + Location Spread (Tier-1) | not explicit | multi-location inventory | A (2–3/4) |
| Broker intermediation | not documented | YES — Broker Notes, brokerage invoices, Brokers audience | not documented | not documented | A (1/4) → regional variant |
| Network/multi-buyer price visibility | NO (single-buyer tools) | YES — growers filter posted prices by Buyer across many sites | NO (Barchart = external channel, not a marketplace) | NO | A (1/4) → network-posture variant |

## Canonical Model (L0–L3)

### L0 — Defining Invariant (deliberately small)

The Type is the **grain buyer's acquisition-side system**: it exists to convert market-facing pricing into contracted, tracked bushel commitments from growers. Three structures, jointly held:

1. **Buyer-published acquisition pricing (the cash-bid layer).** The buyer's standing offer to purchase grain — dimensioned by commodity, grade, delivery location and period/season, revised as markets move, and made visible where growers decide to sell (app, website, in-office display, network boards). This is the acquisition "shop window"; historically the posted daily bid sheet.
   - Remove → a contract desk with no acquisition surface: the system no longer performs origination, only records it after the fact.
2. **The offer → acceptance → contract formation loop between grower and buyer.** Growers initiate (firm offers, or acceptance of posted bids); the buyer accepts/rejects; acceptance is a binding, timestamped price-lock that produces a **purchase contract** — a typed record carrying counterparty, commodity, grade(s) (often priced as spreads to a base grade), quantity, price (fixed at signing or pricable later), delivery location(s) (often with location price adjustments), delivery period/window, and payment terms.
   - Remove → a price list with no deal-making machinery; no commitments can form.
3. **The open commitment book.** Contracts are managed as live acquisition commitments: quantity filled vs remaining toward delivery, pricing status of not-yet-fully-priced contracts, and the current market value of open commitments — worked until fulfillment.
   - Remove → disconnected contract documents; no managed acquisition position.

Jointly-held load-bearing tests:
- 1+2 without 3 = a bid page plus an offer inbox (below the Type).
- 1+3 without 2 = posted prices and a hand-maintained contract ledger (below the Type).
- 2+3 without 1 = the back-office contract book — which is exactly the contract module of an elevator ERP (the Ever.Ag CMS pole): real machinery, but not the origination Type's market-facing whole.

Evidence: all three legs are A-evidenced in at least two independent products (Bushel, AgriDigital strongly; Agvance for legs 2–3 with partial leg 1; the multi-buyer price board in AgriDigital shows leg 1 generalizes beyond one vendor's packaging).

### Historical / market-sample check (§24-style reasoning)

The paper-era origination desk satisfies all three legs with no digital machinery: the posted/chalked daily bid sheet by commodity and location (leg 1); the phone-in offer, the buyer's yes, the signed contract in the contract book (leg 2); the contract ledger tracking filled bushels against commitments and the unpriced basis contracts marked at market (leg 3). The definition therefore names no app, portal, e-signature, ERP integration, or cloud. Regional check: the Australian realization carries different settlement instruments (RCTIs) and levies/royalty deductions — the acquisition core (prices posted by buyers, contracts with grade/location spreads and delivery periods, transfer of warehoused grain onto prices/contracts) is identical in structure.

### L1 — Common mature structure (expected in current products, not defining)

- Grower-facing portal/app: prices, offers, contracts, balances, (often) tickets and payments visibility.
- Electronic signatures and timestamped acceptance records on offers/contracts.
- Offer status synchronization and notifications (grower sees accept/reject immediately).
- Market data integration (commodity markets/futures references) and market-value tracking of open contracts.
- CRM for the origination desk: customer activity, position, history, follow-ups.
- Discount schedules / premium-discount tables as managed configuration.
- Multi-location bid and delivery pricing (location searches, location spreads).
- Reporting/analytics on origination activity.
- Digital payments to growers and settlement visibility (in the sample all four products carry payment/settlement machinery in some form — but WHERE settlement is owned varies, see boundary).

### L2 — Variant / optional structure

- **Packaging posture**: standalone origination layer over a grain ERP (Bushel) ↔ origination module inside a grain/ag-retail ERP (Agvance, Ever.Ag CMS) ↔ full-chain platform that adds custody, inventory and settlement (AgriDigital).
- **Operator posture**: single-buyer desk tools ↔ network platform where multiple buyers' posted prices are visible to growers on one board (AgriDigital; "filter … by Buyer" across sites) ↔ brokered intermediation (broker notes, brokerage invoices — AgriDigital).
- **Regional machinery**: US-style discount schedules vs AU instruments (RCTIs, levy and end-point-royalty deduction, warehouse-transfer pricing of stored grain).
- **Grower-engagement pairing**: licensed farm-management tools feeding grower marketing confidence (Bushel Farm bulk licensing) — single-product, optional.
- **Futures order placement** inside the origination desk (Bushel Trade) — single-product, optional; elsewhere hedging sits in companion risk products.
- **After-hours / mobile-first offer capture** as a deliberate philosophy (Bushel) — a realization emphasis, not a structure.

### L3 — Vendor-specific detail (research notes only)

- Bushel: "Make Offer" flow, "Trade Anywhere", embeddable cash-bids-and-futures widget, BushelOne analytics, Buddy CRM AI assistant, minimum trade offer sizes, QT News feeds, Agris-specific contract features, Bushel Business Account (Bancorp-provided), SOC 2 Type II claim, all vendor performance figures (42 seconds, $1.14/offer, 2M bushels, 58.6%/41.4%, 800+ hours, 15–25%, 90% contract-risk reduction, growth percentages).
- AgriDigital: Digital Commodity Finance funding, NGR/ABR/Xero/NHVR/Mettler-Toledo/Rinstrum integrations, carry fee/frequency/start-date fields, paddock/truck/driver delivery fields, "coming soon" per-grade quantities, shrink article, varietal end-point royalty remittance for plant breeders.
- Agvance: Barchart integration, Grower360 branding, Analytics product, RFID automation details.
- Ever.Ag: module names (Dispatch/Roger logistics), dairy-suite adjacency, AI assistant on site.

## Vendor-specific Findings

See L3 above. None of these entered the final document.

## Rejected Findings (considered and rejected for the core)

1. **"Payments/settlement as a defining leg"** — REJECTED. All sampled products carry payment machinery, but ownership of the settlement of record splits along the elevator seam: Bushel explicitly reads settlement summaries from the ERP and defers to it; AgriDigital owns RCTIs as part of the full chain; Ever.Ag CMS settles inside the ERP. Settlement ownership is packaging, not invariant. (Also matches the elevator pass, which owns the settlement money loop as ITS core leg.)
2. **"CRM as a defining leg"** — REJECTED. Present 4/4 at varying depth (dedicated solution, connections module, suite customer DB); historically the relationship lived in the buyer's head and ledger cards. Standard capability.
3. **"Grower app/portal as a defining leg"** — REJECTED via the historical check: offers ran by phone for decades; the portal is the current channel, not the structure.
4. **"Futures/hedging machinery as a defining leg"** — REJECTED (single-product evidence; companion products elsewhere; paper-era origination had none inside the acquisition record).
5. **"Marketplace matching (many buyers bidding against each other) as the defining core"** — REJECTED for now: directly evidenced only at the network price-board level (AgriDigital, one product); the dedicated grain-marketplace population (Grain Discovery class) was unreachable. Held as a variant; flagged in STATUS as a taxonomy watch item.
6. **"Delivery scheduling/dispatch as a defining leg"** — REJECTED. Outbound/inbound load logistics belong to the elevator/ERP side (Ever.Ag Dispatch, Bushel Commercial Portal); origination's fulfillment tracking is contract-side (quantity remaining), not truck-side.
7. **"The contract must be e-signed"** — REJECTED as invariant (paper contract book satisfies leg 2; e-sign is the common modern closure mechanism).

## Boundary Findings

1. **vs Grain Elevator Management (the primary seam — RATIFIED from this side).** Working seam adopted by the elevator pass: "origination = the grower-acquisition/contracting front end without custody or settlement; elevator management = the full ticketed-movement + settlement + bin-inventory system of record." This pass confirms the seam from the origination side with product evidence in BOTH directions:
   - Strip tickets/settlement/bin-inventory from elevator machinery → what remains is precisely this Type (Bushel is the pure-play member, operating bids/offers/contracts/CRM over an ERP incl. Agris — "ERP contract creation upon filled offers", "instant contract and settlement summary views", "CRM bin-level tracking" — reading the elevator's records without owning them; Agvance Grower360 is the origination surface of an elevator module).
   - Add custody/deliveries/inventory/settlements to an origination platform → the full-chain platform posture (AgriDigital: contracts+prices+deliveries+inventory+RCTI settlements+funding), which straddles upward without dissolving the origination core (contracts+prices remain first-class modules).
   - Keep-both RATIFIED. The elevator pass's own statement — "a product that only publishes bids and captures grower offers — without tickets, settlement, or custody — is the origination front end, not this Type" — is consistent with this L0.
2. **vs Grain Management (storage condition)** — disjoint cores confirmed from this side: no storage-condition machinery (sensing, out-of-condition alerts, aeration) appears anywhere in the origination sample. Keep-both ×3 across the grain cluster.
3. **vs Farm Management Platform (grower side)** — origination is the buyer-side mirror of the same grain. Grower marketing-decision tooling (cost of production, "what price makes sense to sell") is farm-management territory (Bushel Farm is explicitly a paired product that "helps both sides" — the pairing itself documents the boundary).
4. **vs Commodity Trading & Risk Management (paper side)** — origination contracts are grower-facing physical-delivery commitments (delivery locations, grade machinery, grower counterparties), not market positions; the elevator pass already holds this seam; no CTRM evidence contradicts it.
5. **vs Agribusiness ERP** — packaging relationship: origination machinery appears as a module inside ag-retail/commodity ERPs (Agvance, Ever.Ag CMS); standalone realization exists (Bushel). Module-vs-standalone is posture, not identity — consistent with the elevator pass's identical finding.
6. **vs generic CRM** — a CRM inside an origination platform manages grower relationships toward bushel commitments with price-basis semantics; generic CRM lacks bids, contracts-as-commitments, and the acquisition book. Bushel's CRM being a solution *inside* the platform documents the containment.
7. **vs Online Marketplace** — the network price board (multiple buyers' prices visible to growers on one platform) approaches marketplace territory; dedicated online grain marketplaces exist in the market but were not directly researchable this pass (Grain Discovery JS-gated). Held as a variant of this Type on the strength of the in-sample network evidence; flagged as a watch item rather than asserted.

## Uncertainties

1. Marketplace/listing pole (dedicated grain marketplaces) — unreachable; the variant is asserted only at "network price board" strength.
2. Bushel's contract field depth and offer validity rules — KB unreachable; documented only at product-page/release-note granularity. No precise offer-expiry, minimum-size values, or contract-type taxonomies asserted in the final doc.
3. Ever.Ag CMS and Agvance grower-facing bid publication — not evidenced on reachable pages; these poles are used for legs 2–3 and the packaging seam, not for leg 1 strength.
4. Contract-type vocabularies (forward cash / basis / HTA-class structures) — the mechanics (price now vs price later, price basis, carry) are evidenced, but a canonical contract-type taxonomy is NOT asserted; the market's naming was not directly verified this pass.
5. Regional spread beyond US/AU — unverified; the definition is written region-neutral, but all direct evidence is North American + Australian.
6. Whether any product runs origination WITHOUT any grower-facing surface at all (pure desk) — not directly observed; Ever.Ag CMS comes closest on its reachable page.

## Final Synthesis

A Grain Origination Platform is the grain buyer's acquisition-side system of record for forming and working grower grain commitments: it publishes the buyer's purchase prices where growers decide to sell, turns grower offers and bid acceptances — through a binding, timestamped acceptance act — into typed purchase contracts, and manages the resulting open commitment book (quantity remaining, pricing status, market value) until fulfillment. Custody of the grain (scale tickets, bin inventory) and the settlement of money owed live in the connected elevator/back-office system, or in the same product's fuller modules where the platform spans the whole chain. The Type's relationship to its siblings is a clean division of the grain trade: origination acquires, the elevator takes custody and settles, grain management protects the physical asset. The leaf is a distinct Type, not an alias or variant; keep-both with both siblings is ratified from this side.
