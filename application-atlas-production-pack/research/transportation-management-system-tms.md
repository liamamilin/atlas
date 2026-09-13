# Research Notes — Transportation Management System / TMS

Research date: 2026-09-08
Slug: transportation-management-system-tms
Directory leaf: §10 Enterprise Operations & Administration → "Transportation Management System / TMS"

## Research Goal

Understand what a Transportation Management System (TMS) actually is as an Application Type: its core objects, its defining workflow (how freight demand becomes an executed, tracked, settled movement), who sits in front of it, which states and rules govern it, and where its boundaries sit against the dense cluster of neighboring logistics Types (trucking management system, dispatch management, freight brokerage, shipment visibility, freight audit & payment, WMS, supply chain planning, route optimization, freight forwarding, dock/yard scheduling).

## Initial Boundary (pre-research hypothesis)

- A TMS is the **shipper-side** (beneficial cargo owner / logistics service provider) system for planning, buying, executing, and settling transportation — not the carrier's own dispatch/settlement system (that is the Trucking Management System leaf's territory).
- Its center is the **shipment** (a movement of goods), procured from **carriers at rates**, executed through a **tender-and-track loop**, and closed through **freight cost settlement**.
- Nearest confusions: Dispatch Management (assignment act), Shipment Visibility Platform (tracking layer), Freight Audit & Payment (settlement loop), Supply Chain Planning (plans but never executes), WMS (warehouse execution), Freight Forwarding System (intermediary seat), Route Optimization (algorithm capability).

## Research Questions

1. What is the central object of record — order, shipment, load, or something else? How do demand objects relate to executed movements?
2. How does the procurement side work: carriers, rates, routing guides, spot quotes, bid/RFP events?
3. What exactly is the tender/booking loop, and what happens on carrier rejection?
4. How is execution tracked (milestones, events, ETAs) and how are exceptions handled?
5. How deep does settlement go inside a TMS (rating → invoice match → pay), and where is the FAP seam?
6. Which modes appear (parcel/LTL/TL/intermodal/drayage/ocean/air/rail) and is multi-modal definitional?
7. Who are the users (shipper transportation team, 3PL/LSP operators, carriers, finance) and what surfaces do they use?
8. Where is the line against carrier-side systems (Trucking Management System), dispatch, visibility, and planning?
9. Would a pre-software traffic-management practice (tariff books, carrier files, phone tender, check calls, freight-bill audit) still satisfy the definition?

## Representative Products

Selected for market representativeness, documentation reachability, different product philosophies, and different customer tiers:

| Product | Segment / posture | Philosophy |
|---|---|---|
| Oracle Transportation Management (OTM/GTM Cloud) | enterprise suite module, global shippers/LSPs | deepest planning/orchestration; paired with Global Trade Management; private-fleet module |
| SAP Transportation Management | enterprise, ERP-embedded | planning + tendering + settlement inside the ERP landscape; carrier collaboration via SAP Business Network |
| Shipwell | mid-market cloud-native SaaS, shipper-side | modular end-to-end TMS ("plan, rate, ship, & manage"); AI-era; standalone modules with path to full platform |
| Kuebix (by FreightWise) | SMB/mid-market SaaS | quote-book-track simplicity; published pricing tiers; carrier portal for trading partners |
| Turvo | collaborative TMS across 3PL/broker/shipper/carrier seats | collaboration layer over the shipment; driver app; network integrations (load boards, visibility) |

Rejected/considered: MercuryGate (site unreachable ×2), Rose Rocket (403; carrier-side), Blue Yonder / e2open / Descartes (gated or not attempted within budget), project44 (visibility platform, not TMS — different leaf).

## Sources

All fetched 2026-09-08. Evidence is official vendor surfaces: product/solution pages, FAQ, glossary, and Oracle's documentation-library structure. Deep operational help-center articles were NOT reachable for any sampled product (see Uncertainties).

- Oracle — Transportation Management product page: https://www.oracle.com/scm/logistics/transportation-management/
- Oracle — "What is a transportation management system (TMS)?": https://www.oracle.com/scm/logistics/transportation-management/what-is-transportation-management-system/
- Oracle — Logistics Cloud Suite docs root: https://docs.oracle.com/en/cloud/saas/logistics-cloud-suite/index.html
- Oracle — Transportation and Global Trade Management 26C Get Started: https://docs.oracle.com/pls/topic/lookup?ctx=otm-latest&id=otm-gs (redirect resolved)
- Oracle — 26C All Books (guide list incl. Administration, Integration, WMS-integration KB, REST APIs): https://docs.oracle.com/en/cloud/saas/transportation/26c/books.html
- SAP — Transportation Management overview: https://www.sap.com/products/scm/transportation-logistics.html
- SAP — Transportation Management features: https://www.sap.com/products/scm/transportation-logistics/features.html
- Shipwell — homepage: https://www.shipwell.com/
- Shipwell — TMS platform page: https://www.shipwell.com/tms-platform
- Shipwell — FAQ: https://www.shipwell.com/faq
- Shipwell — Glossary: https://www.shipwell.com/glossary
- Kuebix — homepage: https://www.kuebix.com/
- Kuebix — product page (FreightWise): https://www.freightwisellc.com/kuebix/
- Turvo — homepage: https://www.turvo.com/
- Turvo — TMS page: https://turvo.com/transportation-management-system/

Unreachable (recorded per source-access limitation): docs.oracle.com deep help topics (JS-gated beyond structure; Getting Started/What's New render only titles), help.sap.com (JS app), mercurygate.com (transport error ×2), developer.shipwell.com (transport error ×2), help.shipwell.com / support.shipwell.com (transport errors), freightwisellc.zendesk.com KB (transport error), roserocket.com (403).

## Product Observations

### Oracle Transportation Management (OTM) — enterprise suite pole [Layer A]

From the product page and what-is page:

- Positioning: "Manage all transportation activity throughout your global supply chain." Named a Leader in the Gartner Magic Quadrant for TMS (vendor-claimed, 19th time).
- Module structure on the page: **Operational Planning** ("determine the best way to fulfill transportation requirements from simple point-to-point to complex multimodal, multileg, and cross-dock operations"; "secure bids and efficiently plan inbound, outbound, and interfacility orders by collaborating with logistics service providers and shipping partners"; "build effective shipping plans... efficient lane combinations of freight or cooperative routes"), **Transportation Management** ("proactively manage the lifecycle of orders and shipments through automated milestone monitoring"; "automate freight billing and payment. Consolidate and execute transportation orders from multiple sources and eliminate inefficient and redundant settlement procedures"; "measure performance and monitor trends... internal operations and trading partner performance"), **Fleet Management** ("manage all orders and shipments in a single system that considers all available fulfillment capabilities including contract and private transportation"; costing, payables, cost accruals, claims/disputes), **Logistics Network Modeling** (what-if scenario modeling over the transportation network), **Digital Assistant** (shipment-status Q&A), **Machine Learning** (transit-time/ETA prediction feeding planning; "at-risk shipments").
- What-is page definition (vendor's own): "A transportation management system (TMS) is a logistics platform that uses technology to help businesses plan, execute, and optimize the physical movement of goods, both incoming and outgoing... plan, execute, and optimize." Planning = "select the optimal mode of shipment and the best carrier, based on cost, efficiency, and distance, including optimizing multi-leg carrier routes." Execution = "matching loads and communicating with carriers, documenting and tracking shipments, and assisting with freight billing and settlement... track and trace services — enabling real-time information exchange among carriers, distributors, warehouses, and customers." Optimization = "measure and track performance with reports, dashboards, analytics."
- Users named: manufacturers, distributors, ecommerce companies, retail businesses, 3PL/4PL/LSPs. "Primary users are businesses that spend $100 million or more annually on freight, but... cloud-based TMS solutions has made it more affordable for smaller businesses."
- Packaging: standalone TMS integrated with ERP/SCM, or "less feature-rich TMSs... as modules within ERP and SCM suites"; trade documentation either inside the TMS or complemented by a GTM application.
- Docs structure (26C): product ships as "Transportation and Global Trade Management" — one cloud service pairing OTM with GTM. Guides include Administration, Data Management, Integration (incl. "Warehouse Management to Transportation Management Integrations" KB), REST APIs for "business object resources", XML interfaces. (Deep topic content JS-gated — structure only.)

### SAP Transportation Management — ERP-embedded enterprise pole [Layer A]

From the overview and features pages:

- Positioning: "Integrated transportation management plays a critical role in building and maintaining a sustainable, risk-resilient supply chain." Three headline capabilities: "**Transportation and demand planning. Interactive freight tendering. Freight settlement.**"
- Feature groups:
  - **Strategic freight management** — "streamlined quote-to-contract processes" (bid rounds with predictive insight), "automated rate determination" ("exchange information efficiently with logistics service providers").
  - **Order management** — "rules-based orders can be supported by dynamically generating the best routing proposals"; "real-time response — manage changes in transportation demand with real-time order-to-cash and procure-to-pay processes"; "aligned sales and orders"; "integrated intelligence — integrate order and delivery data in the SAP ERP application."
  - **Transportation planning** — "a choice of manual, map-based, and automated planning and dynamic replanning functions helps balance freight costs and service levels"; "build pallets with flexible, rules-based optimization"; "track and manage driver resources with default assignments in an interactive cockpit or Gantt chart"; "visualize load planning of vehicle space and loading."
- Companion products: **SAP Business Network Freight Collaboration** — "connect and collaborate directly with your carriers — from tender to settlement"; **Global Track and Trace** — real-time shipment tracking "with data from any source."
- APIs: SAP Business Accelerator Hub package "TmsForCloudPub" (APIs and prepackaged integrations).

### Shipwell — mid-market cloud-native SaaS pole [Layer A]

From homepage, TMS platform page, FAQ, glossary:

- Positioning: "End-to-End TMS — Plan, rate, ship, & manage with our multimodal TMS." "From the first sales order to final freight audit, Shipwell connects every step of your transportation operation."
- FAQ key-feature list (vendor's own enumeration): "Strategic freight sourcing, Procurement planning, Shipment planning, Load consolidation/optimization, Carrier tendering, Track-and-trace, Real-time visibility, Exception management, Carrier and broker communication, Responsive ETA projection, Freight pay, audit and settlement, and Performance analytics."
- Modes: "TL, LTL, IM [intermodal], Drayage, Parcel, Ocean Container/Rail Visibility, and a roadmap to support Ocean/Air schedules and booking." FAQ: "trucking (both full truckload and less-than-truckload) and parcel, as well as rail and ocean visibility." Multi-stop and cross-border supported.
- Named modules (standalone or in-platform): Load Optimization ("tailoring every order for optimal consolidation"), Settlements ("automated freight audits and payments... from invoice identification to reconciliation"), Pricing Intelligence ("real-time spot rates, contract rate benchmarking"), Visibility ("precise ETAs, real-time tracking, and seamless incident management"), RFP Automation ("bid with ease, award with intelligence, and route with automation"), Dock Scheduling, Freight Document Processing (AI document extraction).
- Inbound side: **Supplier Portal** — supplier onboarding, purchase-order creation/release, "allow suppliers to create shipments directly, support load optimization, and bulk shipment creation from multiple orders," "automating the carrier tendering process through routing guide integration."
- Integrations: "ERP, WMS, CRM, ELDs, Carrier, and BI platforms... including EDI and real-time APIs." API-first posture (REST/webhooks).
- AI-era layer: Track & Trace AI Worker ("monitors every shipment, detects exceptions in real time, and communicates with carriers"), in-app AI assistant (create orders, build recurring shipments), MCP server.
- Glossary vocabulary (definitional terms the product itself publishes): consignee/consignor, FTL/LTL, drayage, intermodal, load optimization ("consolidating LTL shipments into full truckload shipments"), order consolidation, shipment consolidation, freight audit, settlement automation, exception management ("missed pickups or inaccurate delivery addresses"), POD, manifest, spot market rates, RFP automation, lane benchmarking, historical lane insights, multimodal TMS ("supporting multiple transportation modes such as truckload, LTL, air, rail, and sea"), inbound/outbound freight management, transportation spend management.

### Kuebix (by FreightWise) — SMB/mid-market SaaS pole [Layer A]

From homepage and product page:

- Positioning: "Multi-modal Freight Management — Kuebix is the industry's leading full-featured, SaaS TMS for midmarket and larger shippers." (Now part of FreightWise; recognized in Gartner Midmarket Context MQ for TMS.)
- Four headline pillars: **Planning** ("easily plan your shipments from any location and get rates back in seconds"), **Shipment Execution** ("schedule pickups within the platform and directly communicate with the carriers"), **Tracking & Visibility** ("complete visibility into all your shipments in transit and delivered"), **BI & Analytics** ("pull reports, audit, and invoice data with all data stored within Kuebix").
- Key capabilities: "Quote, Book, Track — request rates, book freight, automate pickup requests, and track the progress of LTL, parcel, and full truckload shipments"; Preferred Carrier Rates (supplement existing carriers via FreightWise program); Document Management ("generate BOLs, labels, and other shipping documents stored in a single platform"); Appointment Scheduling ("automatically schedule inbound/outbound shipments and track carrier on-time performance"); Carrier Portal ("extend TMS access to trading partners to automate communication"); API Connectivity ("out-of-the-box, public APIs and pre-built carrier APIs to connect your ERP, WMS, OMS, and transportation providers").
- Modes: "truckload, less-than-truckload (LTL), and parcel." Spot/volume quotes supported ("request rates directly from the connected carrier of their choice").
- Published pricing tiers (evidence that the Type reaches very small shippers): SMB $69/month (single user/location, up to 100 rate quotes/month, LTL/Parcel/FTL, document/BOL creation); mid-market $253/month (5 users/locations, 400 quotes); enterprise unlimited with appointment scheduling, public API, SSO.

### Turvo — collaborative TMS, multi-seat pole [Layer A]

From homepage and TMS page:

- Positioning: "The only Collaborative TMS." Serves "freight brokers, 3PLs, shippers, and carriers" — the same product family sold to all four seats.
- Workflow claim: "Plan, Execute, and Settle Better — automate order-to-shipment activities... end-to-end visibility." Applications: **Order to Shipment Planning**, **Shipment Execution**, Inventory & Warehouse Visibility, Appointment Scheduling, Analytics, **Driver App**, Integration Hub.
- Execution depth: "Deeper than track and trace... route matching, contract execution, driver performance monitoring, and turnaround time optimization." "Eliminate check calls, texts, emails, and faxes." "Manage by exception and set rules and notifications to identify issues and solve them."
- Driver app: "digitally uploaded PODs and shipment sharing... used by more than 1 Million drivers" (vendor claim).
- Network integrations: "load boards, capacity management software, and visibility solutions like DAT, Parade, Truckstop.com, P44, MyCarrierPackets" — i.e., the TMS consumes external capacity/visibility services rather than being one.
- Carrier vetting / double-brokering protection (fraud article) — carrier-relationship machinery inside the TMS.

## Cross-product Comparison

| Dimension | Oracle OTM | SAP TM | Shipwell | Kuebix | Turvo |
|---|---|---|---|---|---|
| Central object language | "lifecycle of orders and shipments" | order management → routing proposals → planning | "shipment planning... carrier tendering" | "quote, book, track" shipments | "order-to-shipment activities" |
| Carrier + rate layer | "collaborating with logistics service providers"; bids | "automated rate determination"; quote-to-contract | carrier tendering; pricing intelligence; spot rates | "request rates... connected carriers"; preferred rates | carrier vetting; capacity integrations |
| Tender/booking | "secure bids... plan orders"; consolidation of orders | "interactive freight tendering" | "carrier tendering"; routing-guide automation | "book freight, automate pickup requests" | shipment execution; contract execution |
| Execution tracking | "automated milestone monitoring" | (via Global Track and Trace companion) | "track-and-trace, real-time visibility, exception management" | "tracking & visibility... in transit and delivered" | "100% visibility, live tracking"; driver app PODs |
| Freight cost/settlement | "automate freight billing and payment" | "freight settlement" | "freight pay, audit and settlement" | "audit, and invoice data" | "settle better" |
| Modes | multimodal, multileg, cross-dock | global + domestic | TL/LTL/IM/drayage/parcel + ocean/rail visibility | LTL/parcel/FTL | truckload-centric (broker/3PL freight) |
| Optimization/planning | operational planning; network modeling; ML ETA | manual/map/automated planning; pallet build; replanning | load optimization; RFP automation | planning + rates in seconds | route matching; predictive planning |
| Documents | documentation (what-is page); GTM pairing | (via collaboration network) | BOLs, labels; document AI | BOLs, labels | digital PODs |
| Analytics | transportation intelligence | (implied) | performance analytics; spend analysis | BI & analytics | analytics app |
| Integrations | ERP/WMS (integration guides), REST/XML | ERP; Business Network | ERP/WMS/CRM/ELD/BI; EDI+API | ERP/WMS/OMS; carrier APIs | load boards (DAT/Truckstop), P44, capacity tools |
| Seat | shipper/LSP (fleet module optional) | shipper (ERP side) | shipper | shipper | 3PL/broker/shipper/carrier |
| Tier | global enterprise | global enterprise | mid-market | SMB→enterprise | mid-market logistics operators |

**Cross-product commonalities (Layer B):** all five hold (1) a shipment/order lifecycle as the managed record, (2) carriers with rates as the supply side, (3) a tender/booking act that commits a carrier, (4) execution tracking with exceptions, (5) freight-cost determination and (in all five, in some form) settlement/audit, (6) documents, (7) analytics, (8) ERP/WMS/OMS integration. Multi-modal breadth varies (Kuebix: 3 modes; Oracle: multimodal/multileg/cross-dock) — breadth is not uniform, so it is not definitional.

**Stable differences (Layer A):** planning depth (Oracle/SAP deep optimization vs Kuebix quote-book-track), seat (Turvo multi-seat vs others shipper-side), packaging (ERP-embedded vs standalone vs modular SaaS), AI layer (era-current, present in Shipwell/Oracle marketing).

## Canonical Abstraction

### L0 — Defining Invariant

The TMS is the **shipper-side system of record for buying and managing the movement of freight**. Three jointly-held structures:

1. **The shipment as the unit of record** — a movement of goods from origin(s) to destination(s) — with contents, mode, dates, and parties — held as a persistent, individually identified record that carries the move from demand through delivery. (Remove → rate calculators, carrier directories, or visibility feeds with nothing managed.)
2. **The carrier-and-rate layer** — external transportation providers held as the supply side with their rates/services, against which each shipment is priced and a carrier is selected. (Remove → private-fleet-only dispatch = Fleet/Dispatch territory; or a tracking tool with no procurement.)
3. **The tender-execute-track loop** — the shipment offered/booked to the selected carrier, its execution tracked through milestones/events to delivery with exceptions managed — the system of record for the move's execution. (Remove → planning-only = supply chain planning; or visibility-only = Shipment Visibility Platform.)

Jointly-held is load-bearing: 1 alone = a shipment log; 2 alone = a carrier/rate database; 3 without 1+2 = a dispatch/tracking board; 1+2 without 3 = a rate-shopping calculator that never executes; 1+3 without 2 = internal dispatch (no procurement); 2+3 without 1 = a tendering conduit with no shipment of record.

Deliberately NOT in L0: multi-modal breadth, optimization engines, settlement/audit (contested — see Rejected Findings), documents, analytics, AI, carrier portals, dock scheduling, private fleet.

### L1 — Common Mature Structure

Present in most mature products (Layer B, 4–5 of 5 sampled):

- multi-modal support (mode set varies by product)
- load planning / consolidation (orders → loads; LTL→FTL consolidation; pallet building)
- routing guides / rules-based carrier selection
- rating depth: contract rates, spot quotes, accessorials/fuel
- milestone/event tracking with ETA projection; exception management
- freight audit & settlement (often as an embedded module)
- shipping documents (BOL, labels, POD)
- appointment/dock scheduling
- carrier portals / carrier communication channels
- analytics: freight spend, carrier performance/on-time, lane benchmarking
- procurement events: bid/RFP, spot
- integration spine: ERP, OMS, WMS, ELD/telematics, load boards, visibility providers

### L2 — Variant / Optional Structure

- **Seat**: shipper (BCO) vs 3PL/LSP vs broker vs carrier — the same product family can be sold to several seats (Turvo); the carrier-side seat is the Trucking Management System sibling's center.
- **Mode depth**: parcel-only thin pole (multi-carrier shipping), truckload-centric, full multimodal, international ocean/air depth (containers, drayage, port operations).
- **Packaging**: standalone SaaS vs ERP-embedded module vs SCM-suite member vs modular (buy one capability) vs managed transportation (software + people).
- **Private fleet**: fleet-inclusive planning (Oracle Fleet Management) as a module, not the norm.
- **International/trade**: GTM pairing (Oracle), customs/trade-document depth.
- **Strategic layer**: network modeling/scenario tools, freight procurement analytics.
- **AI/ML**: ETA prediction, AI workers/assistants, document AI (era-current).
- **Inbound machinery**: supplier portals, PO-driven inbound freight.

### L3 — Vendor-specific (kept out of the final document)

- Oracle: OTM/GTM as one cloud service; order/shipment lifecycle with "automated milestone monitoring"; Fleet Management module (costing, payables, accruals, claims); Logistics Network Modeling; ML transit-time prediction with no-code model config; Logistics Digital Assistant; integration guide set (WMS↔TM KB, XML interface changes, data dictionary in MOS).
- SAP: quote-to-contract rounds; routing proposals from rules-based orders; cockpit/Gantt planning with driver-resource assignment; pallet building; SAP Business Network Freight Collaboration ("from tender to settlement"); Global Track and Trace companion; TmsForCloudPub API package.
- Shipwell: Swifty AI assistant; Track & Trace AI Worker; MCP server; Supplier Portal (PO release, supplier-created shipments); Pricing Intelligence; Freight Document Processing; published uptime/SOC2 claims; "Shipping Evolution" branding.
- Kuebix: published pricing tiers ($69/$253/enterprise); FreightWise Preferred Carrier Program; rate-quote monthly caps on lower tiers; Carrier Portal; OnKue sibling product.
- Turvo: Shipment Link; "3 clicks vs 100" UX claims; driver app scale claims (1M+ drivers); double-brokering/fraud positioning; RyderShare partnership.

## Rejected Findings

- **"TMS = route optimization"** — rejected. Optimization depth varies enormously (Kuebix SMB tier is quote-book-track; the dispatch pass documented a dispatch-centric trucking product with no optimization that is fully in-type for its own leaf). Optimization is a capability, not the defining structure.
- **"TMS = visibility platform"** — rejected. All sampled TMS products include tracking, but the market itself distinguishes the two (Shipwell FAQ: "Do I need a visibility platform and a TMS? Do I need both?"). Standalone visibility = Shipment Visibility Platform leaf.
- **"Settlement is definitional"** — rejected as L0. The Freight Audit & Payment pass ratified the seam from its side: "TMS plans, rates, tenders, executes, and tracks shipments; FAP verifies and settles the freight payables... Remove the payable audit-and-settlement loop and keep tender/rate/track → TMS." Settlement appears in all five sampled products (as embedded module or capability) → L1, with the contested-territory note preserved.
- **"TMS is only for big enterprises"** — rejected. Oracle's own page notes cloud pricing brought smaller shippers in; Kuebix publishes a $69/month tier.
- **"TMS requires AI/ML"** — rejected as era-current capability (L2).
- **"Multi-modal breadth is definitional"** — rejected. Mode sets vary (Kuebix 3 modes; Shipwell adds drayage/intermodal; ocean/air often visibility-only). The invariant is mode-agnostic carriage procurement, not a specific mode list.

## Boundary Findings

- **vs Trucking Management System (§18 sibling, unprocessed)**: seat seam. This leaf = the buyer side (shipper/BCO/LSP procures carriage); trucking TMS = the seller side (carrier runs loads, dispatch, driver settlements). Evidence: Turvo sells the same collaborative TMS to shippers AND carriers (seat as variant); the dispatch pass sampled Truckbase as a carrier-side trucking TMS whose center is dispatch/settlement for the carrier. The trucking-management-system pass should treat this document as its boundary counterparty; the shared substrate (loads, carriers, settlement) differs by whose money and whose fleet.
- **vs Dispatch Management (§18, processed)**: the dispatch pass's L0 is the assignment act over work items × resources with a live board; TMS's L0 is procurement-execution-settlement of record. TMS products contain dispatch-like load boards (Turvo shipment execution), and dispatch products appear as a "stage of FSM/TMS business suite" (that pass's own variant note). Object test: assignment act vs shipment-of-record procurement loop. The construction-materials watch-item is discharged from this side: bulk hauling whose object of record is material quantity stays in Construction Materials Management; moves held as shipments with carriers/rates belong here.
- **vs Freight Brokerage Platform (§18, unprocessed)**: the broker is a principal buying and reselling capacity (margin machinery); the TMS is the operational system for moves regardless of who pays. Turvo serves brokers with a TMS — the operational frame is shared; brokerage's buy-sell-spread and load-board market machinery is the difference. Flag for the brokerage pass.
- **vs Shipment Visibility Platform (§18, unprocessed)**: visibility = the location/status layer over moves (often carrier-network-fed, mode-agnostic, no procurement); TMS = the system of record that commits and executes moves. Shipwell's own FAQ treats them as potentially separate purchases. Turvo integrates P44 (a visibility provider) rather than being one.
- **vs Freight Audit & Payment Platform (§10, processed)**: seam ratified from the FAP side (see Rejected Findings). This pass confirms from the TMS side: settlement appears as an embedded module (Shipwell Settlements; Oracle "Freight Payment, Billing, and Claims" data sheet) — capability, not the defining core. Discharges that pass's flag from this side.
- **vs Supply Chain Planning Platform / Demand Planning / Supply Planning (§10, processed)**: those passes hold "the platform plans, never executes" and "WMS/TMS execute the movement of goods." Confirmed: TMS executes (tender, track, settle). The TMS's planning is operational (which carrier, which mode, which load), not forward network planning.
- **vs Warehouse Management System (§10, unprocessed)**: warehouse execution vs transportation execution; Oracle publishes a dedicated WMS↔TM integration guide (KB104569) — paired products, separate Types. Flag for the WMS pass.
- **vs Route Optimization Platform (§18, unprocessed)**: optimization as a standalone algorithm capability vs TMS as the management system that may embed it. Flag for that pass.
- **vs Global Trade Management (§10, processed)**: GTM = whether goods may legally cross and what they owe; TMS = carriage execution. Oracle ships OTM+GTM as one cloud service — packaging overlap, object separation intact (consistent with the GTM pass's own table).
- **vs Freight Forwarding System (§18, unprocessed)**: forwarder = intermediary orchestrating international moves (quotes, carrier bookings, documents, charges per consignment); TMS = shipper-side procurement/execution. Overlap at the LSP seat (Oracle explicitly names LSPs as users). Flag for the forwarding pass.
- **vs Dock Scheduling Platform / Yard Management System (§10, unprocessed)**: facility-level machinery; Shipwell ships Dock Scheduling as a module inside the TMS — capability inside this Type, standalone form = sibling leaf. Flag for those passes.
- **vs Order Management System (§05.07, unprocessed)**: OMS owns the commercial order lifecycle; the TMS receives order/demand input and executes movement. Shipwell's "from the first sales order to final freight audit" phrasing marks the seam (sales order = upstream input).
- **vs Fleet Management System (§18, processed)**: FMS = own vehicles as assets; TMS = bought transportation. Oracle's Fleet Management module bridges both (private fleet + contract carriers in one system) — held as variant, consistent with the FMS pass treating freight/loads as TMS/dispatch territory.
- **vs Electronic Logging Device / HOS Platform (§18, processed)**: duty-status compliance vs freight execution; ELDs appear in TMS integration lists (Shipwell: "ELDs" integration) as data suppliers.
- **vs Dangerous Goods Transportation Management (§18, processed)**: DG pass's object test confirmed from this side — TMS consumes DG flags/data at booking; it does not determine hazard compliance.
- **vs Cold Chain Transportation Monitoring (§18, processed)**: condition monitoring vs execution; consistent with that pass's boundary table.
- **vs Transportation Exception Management (§18, unprocessed)**: exception management is an L1 capability inside the TMS (Shipwell FAQ names it; Turvo "manage by exception"); the standalone leaf is presumably the exception-workflow specialist. Flag for that pass to define against this document.
- **vs carrier-management (§19 telecom, processed)**: homonym only (telecom carriers vs freight carriers); no action.
- **vs Corporate Travel Management Platform (§10, processed)**: people travel vs goods freight — different object entirely; both are "movement management" only by word.

## Historical / Market-Sample Check

- **Paper-era traffic management** (shipper's traffic department, pre-1980s): carrier files with tariff/rate tables; shipment files with bills of lading; tender by phone/telegraph; check calls for tracking; freight bills checked against tariffs before payment. This satisfies all three L0 legs (shipment record, carrier/rate layer, tender-track loop) with zero software — the Type's heritage is the traffic-management function, and the software digitized it. PASSES.
- **Early PC-era TMS** (1980s–90s rating/routing packages): shipment entry, tariff-based rating, carrier selection, tender documents, freight-bill audit. PASSES with no cloud/AI/multi-modal dashboards.
- **Regional/platform variants**: European freight exchanges, ocean/air forwarder-side systems, parcel-only multi-carrier shipping tools — all satisfy the mode-agnostic core (procure carriage from carriers at rates, execute and track). PASSES.
- The L0 does not depend on any specific mode list, optimization engine, cloud delivery, or AI layer. No over-fitting to the current SaaS era detected.

## Uncertainties

- **No Tier-1 help-center articles were reachable for any sampled product** (Oracle deep docs JS-gated; SAP help JS-gated; MercuryGate/Shipwell-help/Kuebix-Zendesk transport errors; Rose Rocket 403). All evidence is official product pages, FAQ, glossary, and Oracle's documentation structure. Consequently:
  - Exact status vocabularies, tender-timeout defaults, invoice-match tolerances, and permission models are deliberately NOT asserted anywhere.
  - The tender-acceptance/rejection mechanics are asserted only at the conceptual level (tendering is named by SAP/Shipwell/Kuebix; rejection handling inferred as the reason routing guides exist — Shipwell's "automating the carrier tendering process through routing guide integration" is direct but the fallback behavior is not documented in reachable sources).
- **Carrier-side TMS boundary** rests on the dispatch pass's Truckbase evidence plus Turvo's multi-seat marketing; Rose Rocket (a named carrier TMS) was unreachable. The trucking-management-system pass must ratify the seat seam from its side.
- **Ocean/air depth**: Shipwell marks ocean/air booking as "roadmap"; Kuebix excludes it; Oracle/SAP claim global scope. International TMS depth is therefore held as a variant with product-dependent depth, not a uniform capability.
- **Settlement depth inside TMS** varies (module vs checklist item); the FAP seam is ratified but the exact division inside any one product is not documented in reachable sources.
- Vendor scale/ROI claims (Turvo "3 clicks vs 100", "1M+ drivers", Shipwell uptime) were excluded from all assertions.

## Final Synthesis

The TMS is the shipper-side system of record for bought transportation. Its world is organized around the shipment — a movement of goods held as a persistent record — priced against a maintained layer of carriers and rates, committed through a tender/booking act, executed and tracked through milestones and exceptions to delivery, and closed through freight-cost determination and (commonly, as an embedded module) invoice audit and settlement. Around this spine mature products add mode breadth, load consolidation, routing guides, documents, appointment scheduling, carrier portals, analytics, and an ERP/WMS/OMS integration spine. The Type's edges are held by seat (carrier-side = Trucking Management System), by act (assignment = Dispatch), by layer (visibility = Shipment Visibility Platform), by money loop (audit/pay = Freight Audit & Payment), and by horizon (forward planning = Supply Chain Planning). The paper-era traffic department — carrier files, tariff books, phone tender, check calls, freight-bill audit — satisfies the defining core, so the abstraction is not an artifact of the current SaaS market.
