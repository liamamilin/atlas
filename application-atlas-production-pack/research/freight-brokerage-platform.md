# Research Notes — Freight Brokerage Platform

## Research Goal

Understand the software a freight brokerage runs its business on (directory leaf §18 "Freight Brokerage Platform", slug `freight-brokerage-platform`): what the system's world consists of, how a load moves from quote to carrier payment, what makes the brokerage seat structurally different from the shipper (TMS) and carrier (trucking TMS) seats, and where the boundaries sit against Load Board / Freight Marketplace, Dispatch Management, Freight Forwarding System, Freight Audit & Payment, and Shipment Visibility.

This leaf owes an answer to a seam recorded by the processed Transportation Management System pass (2026-09-08): "freight-brokerage-platform = principal buying/reselling capacity with margin machinery vs TMS as operational system regardless of margin-holder." This pass ratifies or challenges that seam from the brokerage side.

## Initial Boundary

Working hypothesis before research:

- A freight brokerage is an intermediary that arranges freight transportation using third-party motor carriers, does not own/operate trucks, and earns a margin between what the shipper customer pays and what the carrier is paid.
- The platform for this business should hold: shipper customers, loads/shipments, a vetted carrier network, two-sided pricing, dispatch/tracking, documents (rate confirmation, BOL, POD), invoicing, carrier settlement.
- Nearest neighbors: TMS (shipper seat), Trucking Management System (carrier seat), Load Board / Freight Marketplace (market venue), Dispatch Management (assignment act), Freight Forwarding System (international intermediary), Shipment Visibility Platform (watching layer), Freight Audit & Payment Platform (shipper's payable machinery).
- Known prior context: TMS pass sampled Turvo as a straddling multi-seat product; FAP pass recorded "brokerage moves freight, FAP moves money about freight already moving"; carrier-management pass noted the homonym.

## Research Questions

1. What objects compose the brokerage's world (customer, load, carrier, rates, documents, settlements)?
2. What is the canonical load lifecycle, and which act is the commitment gate (rate confirmation? carrier acceptance?)?
3. How is the two-sided price (customer charge vs carrier pay) held and used? Is margin machinery definitional?
4. What does carrier management look like: sourcing, vetting (authority/insurance), onboarding packets, compliance monitoring, scorecards?
5. How does the platform source capacity: load boards, broadcasting, routing guides, bid boards, carrier lists?
6. What settlement runs in both directions (customer invoicing, carrier bill audit, carrier payment, factoring, quick pay)?
7. What roles does a brokerage staff (dispatcher, carrier sales, accounting, admin, agents)?
8. What integrations are structural (load boards, tracking, EDI with shippers, accounting, payments)?
9. How do pure-brokerage vs hybrid asset-based vs multi-seat network postures differ?
10. Historical check: does the paper-era brokerage office fit the same core?
11. Boundary tests vs the seven neighbors above.

## Representative Products

| Product | Segment / philosophy | Why chosen | Evidence tier |
|---|---|---|---|
| Tai TMS (Tai Software, now part of Descartes) | Brokerage-native pure-play TMS; explicitly NOT for asset-based companies; mid-market→enterprise US brokers | The pure intermediary pole; richest public documentation (22-answer FAQ) | Tier-1 FAQ + Tier-2 homepage |
| Alvys | All-in-one TMS sold to carriers, brokers, and "hybrid (asset-based freight broker)" operations; SMB/mid-market; load-based pricing | Shows the shared substrate with carrier operations and the hybrid variant; full Tier-1 help center reachable | Tier-1 help center + Tier-2 product/FAQ pages |
| Turvo | Multi-seat collaborative network platform sold to freight brokers, 3PLs, shippers, carriers; startup→Fortune 500 brokers | The straddling pole for the TMS seam; network/collaboration philosophy; broker-specific role and routing-guide evidence | Tier-2 product pages (freight-brokers page, homepage) |

Rejected/abandoned samples: AscendTMS (JS-rendered SPA; root and /faq unreachable twice — dropped per source-abandonment rule), McLeod Software (403 — the traditional enterprise brokerage-suite pole, incl. its brokerage product line, unverified), Descartes Aljex (product URL 404 on first guess; not retried), Rose Rocket (403 in the prior TMS pass, not retried). MercuryGate was already unreachable in the TMS pass. The enterprise/legacy pole is therefore structurally inferred only; no claims in this research depend on it.

## Sources

- Tai TMS homepage — https://tai-software.com/ (2026-09-08)
- Tai TMS Freight Broker TMS FAQ (22 answers) — https://tai-software.com/freight-broker-tms-faq/ (2026-09-08)
- Alvys homepage — https://www.alvys.com/ (2026-09-08)
- Alvys Freight Broker TMS page — https://alvys.com/freight-broker-tms (2026-09-08)
- Alvys Help Center (index) — https://help.alvys.com/en/ (2026-09-08)
- Turvo homepage — https://turvo.com/ (2026-09-08)
- Turvo Freight Brokers page — https://turvo.com/freight-brokers/ (2026-09-08)
- Prior sibling research (context, not new fetches): research/transportation-management-system-tms.md, applications/transportation-management-system-tms.md, applications/freight-audit-payment-platform.md, applications/dispatch-management.md, STATUS.md seam notes.

## Product Observations

### Tai TMS (brokerage-native pure-play)

Evidence layer: A (direct, official FAQ/homepage).

- Self-definition: "a comprehensive Transportation Management System built specifically for freight brokers… automates the shipment lifecycle for both FTL and LTL freight, from initial quote through final delivery and invoicing."
- Seat exclusion, explicit: "Tai is NOT designed for asset-based brokers or carriers (companies with their own trucks) or shippers managing in-house transportation." Strong first-hand evidence for the asset-free intermediary identity of the pure pole.
- Enumerated core capability blocks (vendor's own list):
  1. Quoting & rating — instant LTL rates via carrier API/EDI; FTL rating with lane history and pricing tools; quote templates; self-service quotes; historical rate analysis and market trends.
  2. Load coverage & carrier management — integrated load-board access (DAT, Truckstop, 123Loadboard); "historical carrier database with performance history"; automated carrier selection based on lane and rate; "one-click carrier dispatch"; "carrier compliance management (insurance, authority, etc.)".
  3. Shipment tracking & visibility — real-time tracking; automated check-calls replacement; customer tracking portal; proactive exception alerts; delivery confirmation capture.
  4. Documentation & billing — document upload/processing; automated POD collection; customer invoicing; "carrier bill audit and reconciliation"; "discrepancy flagging and resolution workflow".
  5. Accounting integration — QuickBooks sync; automated AR/AP; commission calculation; financial reporting.
  6. Analytics — dashboards for revenue, margin, volume; carrier performance scorecards; lane profitability.
- FTL flow named by the vendor: "Carrier sourcing and rate comparison → automated dispatching → real-time FTL tracking → carrier rate confirmation and booking." The rate confirmation is the named booking artifact.
- Carrier invoice audit framed as margin protection: "auto-audits carrier invoices against the rate con before AP… reweights, reclasses, and accessorial discrepancies are flagged for review… Exceptions get flagged; clean invoices get paid."
- One-screen booking: "Go from quote to covered load without leaving the screen. Source capacity, broadcast to your network, select the best option, and send the rate confirmation from a single screen." "Covered load" is the vendor's term for the commitment act.
- Customer portal: white-label branded; shippers request quotes, book, track, download BOLs/PODs/invoices; "Each customer gets their own secure login and can only see their own shipments and data."
- Integration taxonomy (vendor's own categories — direct evidence of the broker ecosystem): Accounting (QuickBooks); Load boards & capacity (DAT, Truckstop, Direct Freight, 123Loadboard, Parade, CargoChief); LTL carriers (100+ via API/EDI: FedEx Freight, XPO, Estes, ODFL, ABF, Saia, R+L, SEFL); FTL rate intelligence; document processing; email/SMS; Payment processing (Denim, HaulPay, Global Payments, Road Sync, Triumph); **Carrier onboarding (HIGHWAY, RMIS, Truckstop)**.
- Roles named in training: admin, dispatcher, accounting.
- Modes: FTL, LTL, partials, drayage.
- AI-era features: email-scraping AI builds shipments from inbox; AI Track & Trace agent calls drivers for location/ETA (product-specific).

### Alvys (all-in-one; carriers + brokers + hybrid)

Evidence layer: A (direct; help-center index is Tier-1; product pages Tier-2).

- Positioning: "all-in-one operating system for logistics companies" sold to Carriers, Brokers, **Hybrid ("Asset-based freight broker")**, Enterprise, Private fleets. The demo form lists business types: Carrier, Shipper, Broker, Hybrid, Freight Forwarder, Partner.
- Hybrid posture, named: "Uniting your carrier and brokerage sides… the best TMS software for asset-based brokers, uniting carrier and brokerage operations on one seamless platform… Quickly toggle between your fleet and brokerage."
- Broker page value chain: "Pricing, load management, and planning; Carrier management and settlement; Native AI automation; 120+ integrations; Built-in EDI."
- Broker page sourcing claim: "Find competitive, third-party loads and tender to **vetted third-party carriers** without leaving Alvys." — third-party capacity + vetting language.
- Native EDI: "Easily accept loads and send automatic load updates with native EDI… Get loads created automatically from the rate confirmation." — the broker receives shipper tenders via EDI, and the carrier-side rate confirmation document is itself a load-creation source (hybrid/subcontracted flows).
- Help-center structure (Tier-1, the operation's actual object vocabulary):
  - "Create a Load — Enter the **customer, stops, and rates** for a new shipment." (rates plural on one load record)
  - "Loads & Trips — Create, dispatch, modify, and track loads and trips end to end." (internal "Alvys Load Board")
  - "Accounting & Settlements — Invoicing, **driver and carrier settlements**, deductions, and **e-checks**."
  - "Safety & Compliance — **Verify motor carriers** and keep your operation compliant."
  - "Assets & Fleet — Add and manage drivers, trucks, trailers, and fleets." (carrier-side substrate present in the same product)
  - Integrations: ELD & telematics (HOS/location); Accounting (QuickBooks, Sage Intacct, Business Central); **Load Boards — "Post and source freight on DAT, Truckstop, and other boards"**; EDI & Visibility — "Trade tenders and status updates with your customers"; Fuel & Tolls (settlements/IFTA); **Factoring & Payments — "Set up factoring and move money against your invoices."**
  - Administration: "Roles, permissions, offices, and subscription management."
- Load-lifecycle behaviors (product page): automatic load creation; notes attached to the load visible in real time; automatic alerts when loads fall behind; "New carriers are added in seconds with the help of automation"; "With each action by the driver, the load status is updated automatically"; "Accessorials are automatically deducted so the right amount is invoiced"; "POD reconciliation… driver app automatically attaches all needed documents and receipts for fast invoicing"; "Carrier data is stored from every quote, and interested carriers can be registered in seconds."
- Analytics: "insights on every load, customer, and lane… improve your margins."
- Pricing: per-load; unlimited users/divisions.

### Turvo (multi-seat collaborative network)

Evidence layer: A (direct, official pages) + B for the straddle (prior TMS pass sampled the same product's TMS page).

- Homepage: "end-to-end communication and analytics solutions for freight brokers, 3PLs, shippers, and carriers" — one platform, four seats. Broker blurb: "delivers real-time intelligence while allowing brokers to streamline services and maintain complete control."
- Freight-brokers page, key broker-seat facts:
  - "Easily share tenders and rate confirmation data."
  - Configurable brokerage roles: "operators, carrier sales, finance admins, customer service reps, and tracking support." — the brokerage's own division of labor, first-hand.
  - **Routing Guide**: "Set rules and automate workflows for shipments to be offered out to various carriers, carrier groups, and bid boards." — offer-out automation incl. bid boards.
  - Driver App: location tracking, ETAs, document capture "including BOLs, PODs, etc."; >1M drivers claimed.
  - Integration hub named categories: load boards (DAT, Truckstop), capacity management (Parade), visibility (Project44), **carrier onboarding packets (MyCarrierPackets)**, **broker factoring/payments (Denim)**.
  - Analytics: "carrier performance, shipper reliability, financial data."
- Fraud/margin context (article teaser): "automates carrier vetting, and protects freight margins from modern **double brokering**" — double-brokering (an unvetted broker re-brokering a load) named as a brokerage-platform risk category.
- Customers: "High-Growth Startups and Fortune 500 Freight Brokers."
- Free access for carriers/partners/shippers; unlimited users (network posture: counterparties are users of the same platform, not external systems).

## Cross-product Comparison

| Dimension | Tai TMS | Alvys | Turvo | Reading |
|---|---|---|---|---|
| Unit of work | Load/shipment, quote→invoicing lifecycle ("shipment lifecycle… from initial quote through final delivery and invoicing") | Load ("customer, stops, and rates"), create→dispatch→track→invoice | Shipment/order, order-to-shipment planning→execution | **All three: the load is the unit of record with a quote-to-cash lifecycle** |
| Two-sided pricing on the load | Customer invoicing + carrier bill audit against "the rate con"; margin dashboards; commission calc | Customer rates + carrier settlements on the same load; "improve your margins"; accessorials deducted from invoicing | "protects freight margins"; financial data analytics; tenders + rate confirmations shared | **All three hold the customer charge and carrier pay and manage the spread** |
| Supply side | Third-party carriers; vendor explicitly excludes asset-based companies | "vetted third-party carriers"; hybrid = own fleet TOGGLED alongside (variant) | Carriers as platform participants (network) | **All three source independent third-party capacity; hybrid/fleet is an explicit variant, not the pure pole** |
| Carrier records | "Historical carrier database with performance history"; compliance management (insurance, authority) | "Verify motor carriers"; carrier data stored from every quote; onboarding in seconds | Carrier vetting; carrier performance analytics | **Common: carrier as managed record with credentials + performance** |
| Capacity sourcing | Load boards (search+post, DAT/Truckstop/123Loadboard/Direct Freight), broadcast to network | Post and source freight on DAT/Truckstop; marketplace feature | Load boards, capacity tools (Parade), routing guides, bid boards | **Common: external load boards + internal coverage surfaces; broadcast/offer-out machinery** |
| Commitment act | "send the rate confirmation"; "carrier rate confirmation and booking"; "one-click carrier dispatch" | rate confirmation (incl. EDI load creation from rate cons); dispatch | "share tenders and rate confirmation data"; routing-guide offer-out | **Common: tender/rate-confirmation as the named commitment artifact** |
| Execution tracking | Real-time tracking; automated check-calls replacement; exception alerts; delivery confirmation | Driver app status auto-updates; alerts when loads fall behind | Driver app + telematics/ELD; visibility integrations | **Common: event-driven tracking from carrier/driver, not self-declared** |
| Documents | BOL, POD, invoices; automated POD collection; document processing | BOL/rate-con scanning (AI), POD reconciliation, driver-app document upload | BOL/POD capture via driver app | **Common: rate confirmation, BOL, POD as the paper trio** |
| Settlement both directions | Customer invoicing + AR/AP sync + carrier payment (payments integrations: Denim, HaulPay, Triumph…) | Invoicing + driver AND carrier settlements + e-checks + factoring | Financial data; Denim integration (broker factoring) | **Common: two settlement directions + factoring/quick-pay ecosystem** |
| Customer-facing surface | White-label portal (quote/book/track/documents, per-customer isolation) | Customer tracking links; EDI updates to customers | Collaboration Cloud links shippers into the shipment | **Common: customer self-service visibility** |
| Roles | admin, dispatcher, accounting | roles, permissions, offices; unlimited divisions | operators, carrier sales, finance admins, CS reps, tracking support | **Common: dispatcher/load-manager, carrier-sales, accounting, admin split** |
| Modes | FTL, LTL, partials, drayage | truckload-centric (carrier heritage) + broker | truckload-centric; multi-seat | **Mode scope varies; core mode-agnostic on loads** |
| Seat breadth | broker/3PL only (explicit exclusions) | carrier + broker + hybrid in one product | broker + 3PL + shipper + carrier in one network | **Seat breadth is a product posture, not the Type's center** |

Commonality reading: every sampled product runs the same spine — load with two-sided price → source a third-party carrier → commit via rate confirmation/tender → track from the truck → document → invoice the customer → audit and pay the carrier. Around that spine: carrier lifecycle (vet/onboard/score), capacity sourcing (load boards/broadcast/routing guides), customer self-service, analytics with margin per load/lane/customer, factoring/payments integrations, EDI/telematics/accounting connectivity, role division (dispatch / carrier sales / accounting / admin).

## Abstraction Hierarchy

### L0 — Defining Invariant (minimal, jointly-held)

Three jointly-held structures:

1. **The load as the unit of business record** — a freight movement for a shipper customer held as a persistent identified record that carries the commercial terms and accumulates the operational lifecycle from quote through delivery to invoicing. (Remove → CRM/quote tool or generic tracking; nothing to run.)

2. **The two-sided price on the same load** — the platform holds BOTH the customer-facing charge and the carrier-facing pay as priced commitments on each load, and manages the spread (margin) between them across the load's life, settling in both directions (invoice the shipper; verify and pay the carrier). (Remove → a dispatch board or internal TMS with no intermediary economics; the "brokerage" is gone.)

3. **The external carrier network as procured supply** — the capacity that hauls the load comes from independent third-party motor carriers held as standing records (identity, operating authority, insurance, performance) that are sourced, vetted, committed, and settled by the platform; the brokerage operates no trucks of its own in the defining posture. (Remove → trucking/fleet dispatch territory; the intermediary seat is gone.)

Jointly-held is load-bearing: 1 alone = load log / TMS slice; 2 alone = quote-and-invoice calculator; 3 alone = carrier CRM/directory; 1+2 without 3 = an asset carrier's own books (trucking company); 1+3 without 2 = matching/arranging with no held economics (load board / agent); 2+3 without 1 = rate procurement with nothing moving.

### L1 — Common Mature Structure

- Carrier lifecycle: sourcing/recruiting, vetting & compliance (operating authority, insurance verification, carrier packets/registration), onboarding automation, performance scorecards.
- Capacity-sourcing surfaces: load-board search and posting (external boards), broadcasting/offer-out to the carrier network and email/SMS lists, routing guides and bid boards for automated offer-out.
- Dispatch & execution: carrier selection/assignment, rate-confirmation issuance, event-driven tracking (ELD/telematics/driver app/tracking services replacing check calls), exception alerts, POD capture.
- Document machinery: rate confirmation, bill of lading, signed POD, carrier paperwork; document imaging/processing (AI extraction era-typical).
- Two-direction settlement: customer invoicing (commonly on delivery/POD), carrier-bill audit against the rate confirmation (reweighs, reclasses, accessorials), discrepancy/dispute handling, carrier payment incl. quick-pay and e-check/ACH, factoring integration, shipper credit risk.
- Customer self-service portal (white-label quote/book/track/documents with per-customer data isolation).
- Margin & performance analytics: revenue/margin by load, lane, customer, carrier; sales commissions.
- Internal role model: dispatcher/load manager, carrier sales, accounting/finance, admin; agent models in some brokerages.
- Integration spine: EDI/API with shipper customers (tenders in, status out, invoices), accounting sync, load boards, tracking/visibility providers, carrier onboarding/identity services, payments/factoring.

### L2 — Variant / Optional Structure

- Posture of the platform's customer: pure brokerage vs 3PL use vs hybrid asset-based brokerage (carrier + broker sides toggled in one product) vs multi-seat network platform (counterparties as users).
- Mode scope: FTL, LTL (direct carrier API/EDI rating depth), partials, drayage, refrigerated; intermodal/international reaches toward forwarding.
- Era/business-model variants: digitally-operated brokerages (the brokerage's own tech operated as a service, marketing-facing); embedded finance depth (factoring, quick-pay, fuel/toll cards); AI agents for quoting, tracking calls, document extraction.
- Regional regime: the researched sample is US-centric (FMCSA-style authority/insurance verification named by vendors); other markets have equivalent intermediary regimes — the definition must not name a specific regulator.
- Commercial terms: per-user vs per-load pricing; contract vs spot emphasis; agent vs employee sales models.

### L3 — Vendor-specific (research notes only)

- Tai: AI Track & Trace agent that phones drivers; "11 hours/week saved" claims; 12-month terms; explicit "not for asset-based" positioning; specific integration brand list.
- Alvys: hybrid toggle between fleet and brokerage sides; driver app as status engine; per-load pricing; e-checks; IFTA/fuel-toll machinery (carrier-side).
- Turvo: Collaboration Cloud shared-shipment model; free counterparty access; 3-clicks UX claims; specific partner integrations (Parade, MyCarrierPackets, Denim).
- All vendor productivity/percentage claims recorded but excluded from the final document (marketing claims, unverifiable precision).

## Rejected Findings

- **"TMS for brokers = a different Type from brokerage platforms"** — REJECTED as a separation criterion. The market's own name for this software is "freight broker TMS"; the directory separates the leaves by seat, and the shared word "TMS" cannot isolate the Type. The seam is the seat/principal, not the word.
- **"Load boards are part of this Type"** — REJECTED. Load-board integration (search/post) is standard capability; the boards themselves are external market venues (own leaf: Load Board / Freight Marketplace). An internal dispatch board inside the platform is a coverage surface, not the marketplace.
- **"Carrier vetting is definitional"** — REJECTED as L0. Vetting is universal in the sample and regulation-shaped, but the historical paper-era brokerage operated on carrier files without software compliance modules; the software Type exists at the transaction level without deep compliance tooling. L1, strongly documented.
- **"Customer portals are definitional"** — REJECTED. Common mature structure; the pre-portal era satisfied the core.
- **"Double-brokering fraud tooling is definitional"** — REJECTED. Risk concern of the intermediary posture; tooling depth varies (one sampled product headlines it).
- **"Owning no trucks is enough to be a brokerage"** — REJECTED as a complete criterion: a freight forwarder also owns no trucks; the two-sided buy-sell on truckload/LTL loads with rate-confirmations is what distinguishes the domestic brokerage machinery (see Boundary Findings).

## Boundary Findings

1. **vs Transportation Management System / TMS (processed)** — RATIFIED from this side. The TMS pass recorded the seam as "principal buying/reselling capacity with margin machinery vs TMS as operational system regardless of margin-holder." This pass confirms it first-hand: the brokerage platform's world is the two-sided transaction on each load (customer charge + carrier pay + margin), while a shipper TMS holds its own freight's moves with procurement records and no resale. Tai's explicit exclusion of shippers and asset-based companies marks the seat; Turvo's one-platform-many-seats posture shows the seam runs through product families, not vendors. Structural test: strip the resale/margin machinery (hold only one side of the price) → shipper TMS or carrier settlement system; strip procurement-of-others' capacity → trucking territory.
2. **vs Trucking Management System (§18, unprocessed)** — same freight substrate, opposite supply identity: the carrier operates trucks under its own authority (incl. owner-operators dispatched by it) and has driver/fuel/maintenance machinery; the brokerage never operates the trucks. The hybrid asset-based broker (Alvys "Hybrid" pole) runs both in one product — flagged for joint review when trucking-management-system is processed.
3. **vs Load Board / Freight Marketplace (§18, unprocessed)** — the market venue (many brokers ↔ many carriers, postings, bookings) vs one brokerage's business system of record. Integration is structural (every sampled product integrates DAT/Truckstop-class boards), membership is not. Internal coverage boards inside brokerage platforms exist as surfaces. Flag for joint review when load-board-freight-marketplace is processed.
4. **vs Dispatch Management (processed)** — dispatch is the assignment act over a live board, domain-generic; brokerage contains dispatch-like machinery (one-click dispatch) but its center is the commercial two-sided record across the whole quote-to-settle lifecycle. Remove the buy-sell machinery → dispatch board.
5. **vs Freight Forwarding System (§18, unprocessed)** — both are asset-free intermediaries. The forwarder's center is international consignment machinery (multi-leg carriage, forwarder documents/charges, customs-adjacent paperwork, ocean/air bookings); the brokerage's center is domestic truckload/LTL buy-sell with rate confirmations. Overlap seat; different document/charge world. Flag for joint review when freight-forwarding-system is processed.
6. **vs Freight Audit & Payment Platform (processed)** — FAP runs the SHIPPER's freight-payables lifecycle as a financial control over invoices from its carriers; the brokerage's settlement is internal to its own transaction (it audits its own supplier invoices against its own rate cons). FAP moves money about freight already moving under someone else's transaction; the brokerage owns the transaction.
7. **vs Shipment Visibility Platform** — watching/tracking without committing or settling vs the transaction system of record. Tracking feeds INTO the brokerage platform; the visibility product holds no two-sided price.
8. **Naming note (no alias):** market vocabulary is "freight broker TMS", "brokerage management system", "broker TMS". The leaf name "Freight Brokerage Platform" is also colloquially used for the digital freight brokerage's customer-facing app/service (the broker-operated market). That consumer-facing surface (shipper/carrier portals) is L1 machinery of THIS Type's system of record; the leaf is best read as the brokerage's business system — the market's dominant product category. No directory change proposed.

## Uncertainties

- **Enterprise/legacy pole unverified** (McLeod 403, MercuryGate unreachable, Descartes Aljex not found): the enterprise brokerage suite's structure (deep EDI departments, carrier packet compliance desks, agency networks) is inferred from the mid-market samples and ecosystem integrations, not directly observed. No final-document claim depends on it.
- **Commitment-gate formality**: rate confirmation is the named artifact in all samples, but whether a carrier's acceptance is always a recorded two-sided state (vs a one-way document send) could not be verified to the same depth in every product. The final document states the commitment act without asserting a universal acceptance handshake.
- **Regional breadth**: all sampled products are US-market; other jurisdictions' intermediary software was not sampled. The L0 is written regime-neutral as a hedge.
- **Digital freight brokerage operated platforms** (broker-as-tech-company) were not sampled (avoided model-memory claims); recorded as a variant hypothesis only.
- **Factoring mechanics** (recourse, NOA handling) observed only as integration categories; not asserted in detail.

## Historical / Market-Sample Check (§24-style)

Paper-era brokerage office: a shipper phones in a load; the broker writes it on the load board/logbook; quotes the shipper a price and calls carriers from the carrier file (which holds their authority and insurance copies); agrees a lower price with the chosen carrier; issues a rate confirmation and dispatch instructions; takes check calls; collects the signed BOL/POD; invoices the shipper; pays the carrier. All three L0 legs are satisfied at analog level — load record, two-sided price, third-party carrier file — with zero software. Vendors themselves name this pre-history (check calls, carrier files, load boards as physical artifacts). The digital check therefore passes: the definition names no AI, no portals, no EDI, no GPS, no cloud.

Regional check: the same intermediary office exists in other markets under different regimes (subcontracting/exchange models); the L0's regime-neutral wording (operating authority held as credential, not "FMCSA authority") keeps them inside the Type.

## Final Synthesis

A Freight Brokerage Platform is the freight intermediary's business system of record. Its defining core is three jointly-held structures: the load as the unit of business record carrying a quote-to-cash lifecycle; the two-sided price held on that same load (customer charge and carrier pay, with the margin spread managed and settled in both directions); and the external carrier network as procured, vetted, committed, and settled supply — the brokerage operates no trucks. Around this core, mature products add carrier lifecycle management, capacity-sourcing surfaces (load boards, broadcast, routing guides), dispatch and event-driven tracking, the rate-confirmation/BOL/POD document trio, both-direction settlement with factoring/quick-pay, white-label customer portals, margin analytics, a dispatch/carrier-sales/accounting/admin role model, and an EDI/API integration spine. Postures vary (pure brokerage, 3PL, hybrid asset-based, multi-seat network), mode scope varies, and the era's AI machinery varies — none of it moves the core. The Type is separated from the shipper-seat TMS by the resale/margin principal (ratified), from the carrier seat by whose trucks, from the load board by venue vs system of record, from dispatch by the commercial record, from forwarding by document/charge world, from FAP by whose payables, and from visibility by watching vs transacting.
