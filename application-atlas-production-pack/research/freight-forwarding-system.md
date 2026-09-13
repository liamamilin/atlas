# Research Notes — Freight Forwarding System

## Research Goal

Understand the software a freight forwarder runs its business on (directory leaf §18 "Freight Forwarding System", slug `freight-forwarding-system`): what the system's world consists of (consignment/job, quotes, carrier bookings, documents, charges, agents), how a consignment moves from quote to final delivery and settlement, what the forwarder's documents and charges look like structurally, and where the boundary sits against the processed siblings that have pre-hung flags on this leaf: Freight Brokerage Platform, Air Cargo Management, Transportation Management System, Customs Compliance Platform, Dangerous Goods Transportation Management, and the unprocessed Ocean Freight Management.

## Initial Boundary

Working hypothesis before research:

- A freight forwarder is an intermediary that arranges international freight movements for customers without operating vessels or aircraft, buying line-haul capacity from ocean/air/land carriers and orchestrating the surrounding services (origin pickup and handling, consolidation, export and import customs formalities, destination delivery), earning income between what the customer pays and what the carriage chain costs.
- Its system should hold: the consignment (shipment job) as unit of record; quotes and buy/sell rates; carrier bookings; forwarder transport documents (house documents layered under carrier masters in the consolidating posture); commercial and trade documents; customs filings; milestone tracking; agent/partner collaboration; two-direction settlement and per-job profitability.
- Nearest neighbors: Freight Brokerage Platform (domestic asset-free intermediary), TMS (shipper seat), Ocean/Air Cargo Management (mode-operating systems), Customs Compliance Platform (filing machinery), Global Trade Management (importer/exporter-side compliance), Shipment Visibility Platform (watching layer), Courier/Last-mile (own-workforce delivery), NVOCC (forwarder-as-carrier posture — expected to be a variant of this Type, not a separate directory Type).

Pre-hung flags this pass must answer (from STATUS.md Boundary Issues):

1. TMS pass (2026-09-08), seam #4: "freight-forwarding-system = intermediary consignment/document/charge machinery, overlapping at the LSP seat."
2. Freight-brokerage pass (2026-09-08), flag #5: "both asset-free intermediaries; expected seam = domestic truckload/LTL buy-sell on rate confirmations vs international consignment/document/charge machinery."
3. Air-cargo pass (2026-09-08): "forwarder products contain a genuine air module (booking with airlines, HAWB over MAWB, tracking)… boundary held on center of gravity (air carriage itself vs the forwarder's multi-mode customer order)… recommend boundary cross-check when Freight Forwarding System is processed."
4. Dangerous-goods pass: "apply the object test (compliance determination vs carriage execution) when TMS and Freight Forwarding are processed."
5. Customs-compliance pass (2026-09-08, processed): held "vs TMS/Freight Forwarding (carriage execution vs customs filing; forwarders/brokers operate this type for clients)" — this pass should not pull the customs-declaration machinery into the forwarder's defining core.

## Research Questions

1. What is the unit of record (job/shipment/consignment)? How is it identified and typed (mode, direction, consolidations)?
2. What is the consignment lifecycle from customer quote to final invoice and job close?
3. How are buy rates (carriers) and sell rates (customers) held, and is per-job margin/profitability machinery definitional?
4. What documents does the system produce — transport documents (house/master, AWB/B-L), commercial documents, trade/regulatory documents — and how are they generated?
5. How does carrier booking work (schedules, capacity, eBooking, shipping instructions), and what carrier connectivity exists?
6. What role do consolidation (LCL/FCL, CFS) and the warehouse play?
7. How are customs formalities handled inside the forwarder system vs handed to separate machinery?
8. How do multi-branch, multi-entity, and overseas agent networks work (shipment transfer between origin and destination databases)?
9. What roles staff a forwarder (operations, customs, accounting, branch/agent)?
10. How do SMB modular vs enterprise single-platform vs regional-ERP postures differ?
11. Historical check: does the paper-era forwarder office satisfy the same core?
12. Boundary tests against the neighbors listed above.

## Representative Products

| Product | Segment / philosophy | Why chosen | Evidence tier |
|---|---|---|---|
| CargoWise (WiseTech Global) | Global enterprise standard; "single platform" logistics OS for large forwarders | The dominant global forwarder platform; richest forwarding-specific feature page | Tier-2 (official forwarding solution page; in-repo air-cargo research adds its air module) |
| Magaya (Digital Freight Platform / Supply Chain) | SMB/mid-market modular suite; forwarder + NVOCC + warehouse + customs | Shows the full consignment transaction chain and the agent-network posture at the SMB tier; NVOCC page evidences the forwarder-as-carrier variant | Tier-2 (root, export-operations, NVOCC pages) |
| Riege Scope | European mid/enterprise forwarder TMS; air + ocean + customs, community network | Different region and philosophy (lean TMS + community); self-labels "TMS" — naming evidence | Tier-2 (root + freight-forwarding-software page) |
| Softlink Logi-Sys | Regional (India-origin) mid-market "cloud ERP for freight forwarders", 50+ countries | Non-US/EU regime pole (ICEGATE/SCMTR/E-Way Bill); UI menu exposes the forwarder's actual object vocabulary (job orders, AE/SE/AI/SI shipments, custom clearing, freight station) | Tier-2 (corporate root + Logi-Sys product interface screenshot) |
| CargoSphere | Ocean-rate network pole (WiseTech-owned) | Isolates the rate layer: contract ingestion, confidential rate distribution, buy/sell margins | Tier-2 (root page) |

Abandoned/failed: Softlink Global `.net` domain timed out once (recovered via `.com`); no help-center/user-guide level documentation was reachable for any sampled product. All product evidence is therefore Tier-2 (official product/solution pages). Consequences applied: workflows written at conceptual level; no precise numeric parameters (charge-code lists, cutoff times, document field lists) asserted; single-source behaviors marked.

## Sources

- CargoWise International Forwarding — https://www.cargowise.com/solutions/cargowise-forwarding/ (2026-09-08)
- Magaya homepage — https://www.magaya.com/ (2026-09-08)
- Magaya Export Operations — https://www.magaya.com/freight-forwarding-software-for-export-operations/ (2026-09-08)
- Magaya NVOCC Software — https://www.magaya.com/nvocc-software/ (2026-09-08)
- Riege Software homepage — https://www.riege.com/ (2026-09-08)
- Riege Scope Freight Forwarding Software — https://www.riege.com/solutions/freight-forwarding-software (2026-09-08)
- Softlink Global homepage (Logi-Sys product interface) — https://www.softlinkglobal.com/ (2026-09-08)
- CargoSphere homepage — https://www.cargosphere.com/ (2026-09-08)
- In-repo prior research (context, not new fetches): research/air-cargo-management.md (CargoWise/Magaya forwarder-side observations), research/freight-brokerage-platform.md, research/customs-compliance-platform.md, research/dangerous-goods-transportation-management.md, research/freight-audit-payment-platform.md, STATUS.md seam notes.

**Source-access limitation:** no Tier-1 help-center or user-guide documentation was reachable for any sampled product this pass. All product evidence is Tier-2 official product/solution pages. No precise operational parameters (rates, cutoffs, charge-code schemas, message code lists) are asserted anywhere; workflow claims are conceptual-level; claims resting on a single product are marked product-specific.

## Product Observations

### CargoWise (WiseTech Global) — global enterprise platform

Evidence layer: A (direct, official forwarding page) + in-repo air-cargo research for the air module.

- Lifecycle framing: "From initial quote to final invoice, CargoWise streamlines your supply chain across every mode and border."
- Unit of work named "job": "end-to-end supply chain visibility across every job, mode and workflow."
- Operation center: "Manage bookings, documentation, carrier connections, customer updates, and internal workflows from a single platform."
- Mode coverage as forwarding legs: Air ("connects you directly to airlines, manages bookings and updates in real-time… Compare options, secure capacity, and track progress"), Ocean ("full visibility across bookings, schedules, and container movements… from port to port"), Road and rail ("drives your inland operations from first mile to last, whether it's port drayage, container pickup and delivery, or long-haul rail. Movements across carriers, terminals, and legs are assigned, tracked, and managed in a single workflow, keeping landside logistics fully aligned with the rest of your forwarding operation").
- Rates: "Compare buy and sell rates by lane, carrier, and commodity. Quote faster with built-in margin logic, then convert directly to bookings." — buy/sell rates + margin + quote→booking conversion, one sentence.
- Schedules: "Search schedules from leading carriers and airlines, compare routes, and apply voyage details with real-time ETD and ETA updates - all directly in your workflow."
- eBookings: "Book and manage shipments electronically and directly within the platform, then convert them to a bill of lading or air waybill with just one click." — carrier booking and the forwarder's transport document generated from job data.
- Documentation: "Create bills of lading, air waybills, invoices, and packing lists directly from bookings and job data"; "Issue Certificates of Origin, permits, and other trade documents based on cargo details, routing, and destination requirements"; "Link documents to shipments, milestones, and transport events"; "Deliver trade documentation and EDI to customers, partners, and authorities with full traceability."
- Surrounding services as integrated modules: Customs & compliance ("Automate screenings, classifications, and declarations"); Landside ("Coordinate inland pickup, delivery, and empty return milestones"); Warehousing ("Manage receival, consolidation, and outbound dispatch"); Accounting ("Automate costs, invoicing, and multi-currency compliance").
- Workflow machinery: "Configure workflow templates by mode, lane, direction, or customer… standardize execution, and ensure shipments follow the right process"; "Track accountability at every step… who owns it, and what comes next"; "Automate communication and exception handling… trigger milestone alerts… configurable alerts and exception logs."
- Customer surface: CargoWise Neo — "Give your customers live access to their shipments, orders, declarations, invoices, and more."
- Direct carrier connections to "the world's largest airlines and ocean carriers" (branded list).
- Suite taxonomy (vendor's own): Forwarding / Customs / Warehouse / Ecommerce / Enterprise / Transport ("Domestic Transport Management") / Parcel / Carrier — domestic transport management is a separate module beside Forwarding.
- In-repo air-cargo research (same vendor, air page): forwarder air module centers on shipment job + booking + AWB + status events, consuming airline capacity as a buyer; no ULD/terminal control.

### Magaya (Digital Freight Platform / Supply Chain) — SMB/mid modular suite

Evidence layer: A (direct, official root + export + NVOCC pages).

- Positioning: "The #1 Freight Management Platform for Freight Forwarders and Customs Brokers"; Supply Chain is "a single solution for shipping, transportation management, warehouse operations, tracking, connectivity, accounting, and compliance."
- Transaction chain (vendor's own chain): "Avoid double data entry by pulling information from quotes to create bookings, pickup orders, warehouse receipts, shipments, and invoices."
- Export feature list (vendor's list): Quotes; Bookings; Pickup Orders; Purchase Orders; "Consolidated Export Shipment, or FCL"; Warehouse Receipts with "Full WMS to Manage Receiving, Consolidation, Loading, Photos, Shipping"; ACE EEI Filings; Visibility and Tracking; Container Tracking; "Booking Requests and Shipping Instructions via INTTRA"; eAWB; "Shipment Transfer to Destination Database via Magaya Network (if dest. Agent has Magaya)"; "Shipment Receipt in Destination Database"; "Shipment Liquidation in One Click"; Online Payments; Accounting Integration with QuickBooks Online; "Full PnL by Operations and Other Profitability Reports Built-In"; Cargo Insurance; INTTRA and Carrier Integration.
- Shipment typing (NVOCC page): "Shipments: Export, Import, or Domestic; Ocean Freight; Air Freight; Ground Freight; Consolidations, Straights, LCL or FCL; Roll-On Roll-Off (RORO)."
- NVOCC posture: "create quick FCL (full container load) and LCL (less than a full container load) bookings on ocean carriers, receive online booking requests"; "set up easy-to-understand air, ocean, and ground shipment consolidations, exchange shipping instructions (from freight to ocean to air and back), and quickly generate the Bill of Lading and other required documents."
- Rates/charges: "Freight Charges, Quotes, Margins, and Rate Management"; Rate Management = "control tower for searching and comparing rates, managing margins and allocation commitments, filing tariffs, responding to RFQs, and preparing winning quotes," with "direct integration to ocean carrier rate data with DCX (digital contract exchange)" and comparison of "contract base rates as well as conditions like transit time, free-time, floating surcharges, spot rates, and benchmark rates"; FMC tariff filing.
- Customs: Magaya Customs Compliance = "ACE-certified ABI solution"; AMS & Entry Type 86 API; FTZ inventory control — a module beside Supply Chain.
- Agent network: Magaya Network — "instant access to a global community of over 2,300 supply chain companies… 100+ countries"; "instantly exchange documents and data with your partners and agents"; shipment transfer/receipt between origin and destination databases.
- Customer surface: Digital Freight Portal — customers "request quotes, review rates, track shipments"; "convert a quote, schedule or PO into a booking in seconds."
- Industries served by the same platform: Freight Forwarding (export/import), 3PL, NVOCC, Warehouse, Courier, Customs Brokerage.

### Riege Scope — European forwarder TMS

Evidence layer: A (direct, official root + forwarding page).

- Self-label: "Our user-friendly TMS (Transport Management System) automates your logistics processes and connects you globally." Also: "the integrated freight management software… Scope is the integrated freight management software that automates your processes, communicates with third party providers and portals, and thus enables you to digitally manage shipments along the global supply chain."
- Scope: "a single software solution for air freight, ocean freight and customs" — "Without changing systems, without fault-prone multiple data entry."
- Air freight: "From offer to booking or shipment creation to invoicing. Intelligent integrations enable you to communicate with airlines, customers and external providers without changing systems."
- Ocean freight: "reduces your effort in creating a shipment and enables tracking from the first to the last mile. By integrating all relevant port and news portals you get full information about events and status of your shipment."
- Customs: "seamlessly exchange data with the customs authorities - directly after completing shipment creation in Scope or from any WMS/ERP system. Available for Germany, Switzerland, the Netherlands and the USA."
- Airline Messaging Premium: "automatically provides you with event data, covers over 200 airlines, and automatically subscribes to events once you enter the IATA AWB number (fully available to freight forwarders who are not IATA members)."
- Named features: Denied Party Screening ("Execution of denied party checks on demand"); Airline Messaging ("Reliable message exchange in highest data quality"); Shipment Monitor ("Tracking of shipment status and milestones"); Ocean Carrier Messaging; Track & Trace ("Tracking and booking via web"); Quotations ("From quotation to booking or shipment in one step"); International and local; Quick data entry; US AES/ISF ("fully automated and integrated"); emissions calculation per shipment.
- Community: Scope Community — "a global network for digital logistics with thousands of specialists"; vendor blog: "Scope is evolving step by step beyond a traditional Transport Management System (TMS)."

### Softlink Logi-Sys — regional cloud ERP for forwarders

Evidence layer: A (direct; corporate homepage + the Logi-Sys product interface exposed on it).

- Positioning: "Logi-Sys is an all-in-one cloud ERP that helps freight forwarders, consolidators, and customs brokers scale faster—without complexity. It simplifies every process from quotation to delivery, finance to compliance, and connects teams, branches, and partners in real time."
- Product interface menu (the forwarder's working object vocabulary, verbatim from the screenshot): "Job Order · AE - Shipment · SE - Shipment · AI - Shipment · SI - Shipment · Forwarding · Custom Clearing · Import Job · Import Tracking · Export · Quotation · Carrier Operations · ICEGATE · Transport · Warehouse · Freight Station · Purchase Order · SCMTR / E-Way Bill · Sales & Service (CRM) · Billing · Transactions · Reports · Directories · Administration · Messages · Origin / Destination / Origin-Destination Routes."
- Industry blurb: "Streamline air, ocean, and multimodal freight with one intelligent platform—manage bookings, documentation, tracking, and billing across global operations."
- Regime depth (India): ICEGATE (customs gateway), SCMTR / E-Way Bill; customs-clearance industry pole: "In India, Live IMPEX powers 80% of filings via ICEGATE" (vendor scale claim, not asserted).
- Breadth: "5,000+ logistics businesses in 50+ countries… localized compliance, multi-currency, and region-specific workflows"; heritage line "From DOS to AI — over 3 decades."

### CargoSphere — ocean-rate network (WiseTech-owned)

Evidence layer: A (direct, official root page).

- Identity: "The world's connector for ocean rates. Join CargoSphere's neutral rate network for container shipping."
- Rate ingestion: SUDS (Smart Upload and Diagnostic Solution) — "Turn static rate contracts into clean, actionable, accurate data… allowing you to upload rate contracts fast, accurately, and do it all in-house."
- Rate distribution: Rate Mesh — "an intertwined online network of carriers, forwarders and shippers who confidentially distribute rates to one another"; "quickly connect with other shipping partners to quote more shipments and close more deals. Plus, you can easily set your buy/sell margins in order to protect profitability of every quote."
- Seats served: "Solutions for Forwarders & NVOs / Carriers & Consolidators / Shippers & BCOs."
- Ecosystem: rate integration and single sign-on with CargoWise; digital rate distribution by Maersk and Hapag-Lloyd.
- Reading: the rate layer of the forwarder world isolated as a network product — buy rates arrive from carriers/agents as contract data; sell rates are distributed confidentially; margins set per quote. Confirms the rate/buy-sell substrate without carrying the consignment.

## Cross-product Comparison

| Dimension | CargoWise | Magaya | Riege Scope | Softlink Logi-Sys | CargoSphere | Reading |
|---|---|---|---|---|---|---|
| Unit of record | "every job, mode and workflow" (job) | "shipments" (Export/Import/Domestic × air/ocean/ground; consol/straight, LCL/FCL) | "shipment creation… from offer to booking or shipment creation to invoicing" | "Job Order" + typed shipments AE/SE/AI/SI | (rate contracts, not consignments) | **All four full systems: the consignment/shipment job is the unit of record; CargoSphere isolates the rate layer** |
| Lifecycle | "from initial quote to final invoice" | quote → booking → pickup order → warehouse receipt → shipment → invoice | offer → booking/shipment → invoicing | quotation → delivery; "quotation to delivery, finance to compliance" | quote-side only | **Consensus: quote → booking → operation → invoice** |
| Buy/sell economics | "Compare buy and sell rates… built-in margin logic, then convert directly to bookings" | "Freight Charges, Quotes, Margins, and Rate Management"; "Full PnL by Operations" | (rating implied by quotations; not explicit on page) | Billing + Purchase Order machinery | "set your buy/sell margins… protect profitability of every quote" | **3/5 explicit buy/sell margin machinery; PnL per job explicit in 2** |
| Carrier booking | eBookings "converted to a bill of lading or air waybill with just one click"; direct airline/ocean-carrier connections | "Booking Requests and Shipping Instructions via INTTRA"; FCL/LCL bookings on ocean carriers; carrier connections | "communicate with airlines, customers and external providers"; Ocean Carrier Messaging; airline event messaging (200+ airlines) | "Carrier Operations"; ICEGATE-side ops | carrier rate distribution (Maersk, Hapag-Lloyd) | **Common: booking capacity from operating carriers + structured carrier messaging** |
| Transport documents | "Create bills of lading, air waybills, invoices, and packing lists directly from bookings and job data" | eAWB; "quickly generate the Bill of Lading and other required documents"; "Configurable Documents" | (document flows implied; shipment-creation focus) | documentation inside Forwarding module; eSanchit (India) | — | **Common: transport documents generated from job data** |
| Trade/regulatory documents | "Issue Certificates of Origin, permits, and other trade documents" | ACE EEI Filings; customs compliance module | Denied Party Screening; US AES/ISF; customs data exchange (4 countries) | Custom Clearing; ICEGATE; SCMTR/E-Way Bill | — | **Common: customs/trade formalities as consignment steps; depth and lodging vary by market** |
| Consolidation & warehouse | Warehousing: "receival, consolidation, and outbound dispatch" | "Consolidated Export Shipment, or FCL"; warehouse receipts; full WMS | (not on fetched pages) | Warehouse; Freight Station (CFS) | — | **Common in the sample; module depth varies** |
| Inland legs | Landside: "inland pickup, delivery, and empty return milestones"; road & rail legs "assigned, tracked… in a single workflow" | Pickup Orders; "Local Pick-ups and Last Mile Deliveries" | (first/last mile tracking) | Transport | — | **Common: origin/destination land legs inside the same operation** |
| Milestones/visibility | "trigger milestone alerts… exception logs"; workflow templates by "mode, lane, direction, or customer" | Visibility and Tracking; Container Tracking | Shipment Monitor ("status and milestones"); Track & Trace | Import Tracking; Messages | — | **Common: milestone/tracking machinery on the job** |
| Agent/partner network | EDI "to customers, partners, and authorities"; Neo portal | Magaya Network (2,300+ companies); shipment transfer between origin/destination databases | Scope Community ("thousands of specialists") | "connects teams, branches, and partners in real time" | Rate Mesh network | **Common: the partner/agent network is structural; implementation differs (platform network vs community vs message exchange)** |
| Accounting | "Automate costs, invoicing, and multi-currency compliance" | QuickBooks integration; online payments; "Billing, Invoicing, and Accounting" | (not on fetched pages) | Billing; Transactions; multi-currency | — | **Common: two-direction settlement + per-job financials in-product** |
| Customer surface | CargoWise Neo (shipments, orders, declarations, invoices) | Digital Freight Portal (quotes/schedules/bookings/tracking) | Track & Trace via web | (customer-facing machinery implied) | — | **Common: customer self-service layer** |
| Posture | enterprise single-platform OS | modular suite (mix-and-match) | lean TMS + community | all-in-one ERP | rate network | **Posture varies by segment; the consignment spine is shared** |

Commonality reading: every full system runs the same spine — a customer's consignment enters as quote, converts to booking/shipment job; the forwarder buys carriage from operating carriers (ocean/air/land) and arranges the surrounding legs (pickup, receiving/consolidation, customs formalities, delivery); the job accumulates transport documents (commonly house documents under carrier masters in the consolidating posture), trade documents, charges on both sides (sell to customer, buy from carriers/agents), milestone events, and ends in invoicing and job-level profitability. Around the spine: rate management, partner/agent networks, customer portals, accounting, regime-specific compliance modules.

## Abstraction Hierarchy

### L0 — Defining Invariant (minimal, jointly-held)

Three jointly-held structures:

1. **The consignment as the unit of business record** — a customer's freight shipment held as one persistent identified record, typed by mode and direction, accumulating the whole operation (quote, booking, carriage, handling, formalities, delivery, charges, documents) on a single job. (Remove → a booking tool, document generator, or tracking board with nothing that runs the whole job.)

2. **Arranged, not operated, multi-leg carriage with both-ends orchestration** — the system plans and records carriage bought from operating carriers (ocean/air/land) for the consignment's line-haul legs, and orchestrates the services at both ends (origin pickup/receiving/handling, border formalities, destination delivery) as parts of the same managed consignment; the forwarder operates no vessels/aircraft in the defining posture. (Remove → the system of a carrier operating its own capacity, or a single-leg dispatch tool; the forwarder seat is gone.)

3. **The forwarder's document-and-charge layer on the consignment** — the job generates the forwarder's own paperwork and carries two-sided economics: transport documents produced from job data (commonly the forwarder's house documents layered under the carrier's master document in the consolidating posture, plus commercial and trade/regulatory documents), and a charge ledger holding sell charges (freight plus origin/destination local charges billed to the customer) against buy costs (carriers and partner agents), with per-consignment profitability visible. (Remove → an agent/matchmaker with no documents or held economics; a pure visibility tracker.)

Jointly-held is load-bearing: 1 alone = job tracker/CRM; 2 alone = carrier-booking/TMS slice; 3 alone = document generator with a calculator; 1+2 without 3 = arrangement/visibility layer with no forwarder paperwork or economics; 1+3 without 2 = paperwork desk; 2+3 without 1 = disconnected bookings and bills; nothing persists as one managed consignment.

### L1 — Common Mature Structure

- Rate machinery: buy-rate capture from carriers/agents (contracts, spot, surcharges), sell/quote construction with margin logic, quote→booking conversion, schedule search (ETD/ETA).
- Carrier connectivity: electronic booking on ocean/air carriers, shipping instructions, status/event messaging (airline/ocean carrier messaging), container and air tracking feeds.
- Workflow/operations: workflow templates by mode/lane/direction/customer, task assignment and accountability, milestone tracking, exception alerts/logs.
- Consolidation and warehouse: LCL/FCL consolidation, warehouse/CFS receiving and loading, warehouse receipts, automated dimensioning/weighing.
- Customs and trade formalities as consignment steps: export filings (EEI/AES/ISF-class), import entries/declarations (embedded or handed to broker machinery), denied-party screening, certificates of origin, permits.
- Document machinery: configurable transport/commercial/trade documents generated from job data, eAWB/eB-L era forms, document-to-milestone linking, distribution to customers/partners/authorities.
- Inland legs: pickup orders, drayage/container transport, empty return, last-mile delivery.
- Partner/agent layer: overseas agent networks, inter-company/inter-branch shipment transfer, document/data exchange with partners, community/marketplace networks.
- Financials: per-job PnL (job "liquidation" close-out), AR/AP, multi-currency, accounting-system integration, credit/insurance adjuncts.
- Customer self-service portal: quotes/schedules/bookings/tracking/documents.
- Role model: operations staff per leg/mode, customs teams, accounting, branch management (inferred from modules and menus; staffing titles not directly evidenced — marked single-source/unverified).

### L2 — Variant / Optional Structure

- Forwarder-as-carrier posture: NVOCC (issues its own bill of lading, buys vessel space), indirect air carrier, consolidator — the same platform type, sold as such (Magaya's NVOCC page is the same product line).
- Mode emphasis: air-heavy, ocean-heavy, multimodal; domestic/ground adjuncts; RORO, e-commerce cross-border.
- Regime depth: US (ACE/ABI, EEI, ISF), India (ICEGATE, SCMTR, E-Way Bill, eSanchit), EU/CH/NL customs, NZ — the definition names no specific authority or filing.
- Deployment/segment: enterprise single-platform OS vs modular SMB suite vs regional ERP vs lean TMS-plus-community.
- Adjacent modules carried by the same products: 3PL warehousing, courier/parcel, CRM, cargo insurance, emissions calculation, AI extraction/agents (era-typical).
- Domestic-only forwarding postures (national consignments with the same machinery) exist as edge cases; the sample's center of gravity is cross-border.

### L3 — Vendor-specific (research notes only)

- CargoWise: Neo customer portal; suite taxonomy (Transport = "Domestic Transport Management" sold beside Forwarding); 5,700+ enhancements claim; airline tail branding wall.
- Magaya: Magaya Network (2,300+ companies), DCX digital contract exchange, ACEbridge AI Compliance Agent, "Magaya vs CargoWise/Descartes" comparison pages, LiveTrack/Transaction Tracking extensions, golden-MVP awards.
- Riege: Scope Community, Airline Messaging Premium (200+ airlines, non-IATA-members clause), family-company heritage, ISO 27001 certification.
- Softlink: Live IMPEX (ICEGATE filings; "80% of filings" vendor claim), LogiLEARN/LogiSKILL/LogiEXPERT academy, "From DOS to AI" heritage, AE/SE/AI/SI naming.
- CargoSphere: SUDS, Rate Mesh, WiseTech ownership, carrier-branded rate distribution (Maersk, Hapag-Lloyd).
- All vendor scale/productivity claims recorded but excluded from the final document.

## Rejected Findings

- **"Freight forwarding systems are just international TMS"** — REJECTED as a Type identity. The shared word "TMS" spans seats (Riege self-labels Scope a TMS; Magaya's portal advertises compatibility "with the TMS of your choice"). The forwarder system's center is the consignment of record with its document/charge world, not move-planning for one's own freight. Naming note, no alias.
- **"Customs declaration machinery is part of the defining core"** — REJECTED. Forwarder products embed or connect customs filing (Riege: data exchange "directly after completing shipment creation in Scope or from any WMS/ERP system"; Magaya: separate customs module; Logi-Sys: ICEGATE module), but the declaration itself has its own Type (customs-compliance-platform, processed) whose pass recorded "forwarder-embedded" as an operating-side variant. The forwarder's core is orchestrating that the formalities happen on the consignment, not building the declaration.
- **"Consolidation (LCL/FCL) is definitional"** — REJECTED as L0. Strongly documented (Magaya consol/straight/FCL/LCL; CargoWise warehousing consolidation; Logi-Sys freight station), but straight shipments and agent-posture forwarding run the same spine without consolidation. L1.
- **"Agent-network shipment transfer is definitional"** — REJECTED. Common mature structure; networks are product-posture differences (platform network vs community vs message exchange). L1.
- **"Customer portals / digital forwarder surfaces are definitional"** — REJECTED. Common; the pre-portal era satisfied the core. L1.
- **"NVOCC is a separate Type"** — REJECTED. The market sells NVOCC software as the same platform (Magaya's NVOCC page describes the same objects: shipments, consolidations, bill of lading, margins); NVOCC is the forwarder-as-carrier posture (variant), and the directory has no NVOCC leaf.
- **"Margin machinery is vendor marketing"** — REJECTED (the opposite): buy/sell + per-job profitability is named by 3/5 sampled products and is the forwarder's income model; kept in L0 leg 3 at conceptual strength (charge ledger + profitability visible), without numeric claims.

## Boundary Findings

1. **vs Freight Brokerage Platform (§18, processed — DISCHARGES the brokerage pass's flag #5 and the TMS pass's seam #4 from this side)** — RATIFIED with first-hand evidence. Both are asset-free intermediaries holding two-sided economics on procured carriage. The seam runs on scope and document/charge world: the brokerage's center is the domestic truckload/LTL load bought and sold on rate confirmations with a simple two-price record; the forwarder's center is the multi-leg consignment with both-ends service orchestration (origin handling, border formalities, destination delivery) and a layered document/charge world (house-under-master transport documents, trade documents, freight plus origin/destination local charges, partner-agent cost flows). Direct evidence: CargoWise sells "Domestic Transport Management" as a separate module beside Forwarding (the market's own internal line); Magaya/Riege/Logi-Sys pages lead with air/ocean modes and customs/trade documents; no sampled forwarder product leads with load boards or carrier sourcing from truckload boards (the brokerage's sourcing surfaces). Structural test: strip the multi-leg/both-ends/trade-document machinery → the machinery converges toward a domestic brokerage/intermediary system; strip the resale margin and keep procurement → shipper-side TMS. Keep-both as separate Types; overlap seat (large forwarders broker domestic truck legs — recorded as variant overlap, not Type merger).
2. **vs Air Cargo Management (§18, processed — DISCHARGES the air-cargo pass's cross-check flag from this side)** — RATIFIED center-of-gravity seam. The forwarder system contains a genuine air module (booking with airlines, AWB creation from job data, airline event messaging — direct in CargoWise/Riege/Magaya evidence), but its center is the multi-mode customer consignment; air cargo's center is the air carriage itself (flight capacity, terminal handling, AWB lifecycle). Removal tests hold in both directions: remove flight capacity/terminal machinery → a forwarder system still stands (all four sampled forwarder systems run on ocean/air/land consignments); remove the multi-mode consignment layer → what remains is a carrier/terminal system. Keep-both.
3. **vs Ocean Freight Management (§18, unprocessed — flag forwarded)** — expected seam by pattern: ocean objects (vessel/container/BL as carriage operations) vs the forwarder's multi-mode consignment. Forwarder products contain genuine ocean modules (FCL/LCL bookings, container tracking, ocean-carrier messaging, sailing schedules); the ocean pass should apply the same center-of-gravity test as air cargo. Recorded for joint review.
4. **vs Transportation Management System / TMS (§10, processed)** — RATIFIED. The TMS pass's seam #4 ("intermediary consignment/document/charge machinery, overlapping at the LSP seat") is confirmed: a shipper TMS plans/executes its own freight; a forwarder system runs other customers' consignments as the business itself, with resale economics and forwarder documents. The shared word "TMS" (Riege's self-label) is a naming overlap, not a boundary failure — the seam is whose freight and whether carriage is resold.
5. **vs Customs Compliance Platform (§10, processed)** — HELD from both sides. That pass recorded "carriage execution vs customs filing; forwarders/brokers operate this type for clients" and "forwarder-embedded" as an operating-side variant. This pass confirms: forwarder products raise customs as a consignment step (export filings, entries, screening) and either embed filing modules or hand off; the declaration-of-record machinery remains the other Type's center. The DG pass's object test (compliance determination vs carriage execution) likewise holds: dangerous-goods declarations appear in forwarder workflows as gates/documents consumed from compliance machinery.
6. **vs Global Trade Management (§10, processed)** — complementary: GTM centers the importer/exporter's transaction-level trade-control determination (classification, screening, licensing, duty programs); the forwarder system centers the consignment's execution for a service customer. A forwarder may run both; the objects differ (trade transaction of one's own goods vs consignment for a customer).
7. **vs Freight Audit & Payment Platform (§10, processed)** — the forwarder holds its own buy-side costs on the job and settles its own carrier/agent payables; FAP is the shipper's freight-payables control over invoices for freight the shipper already moved. Direction of the money and ownership of the transaction differ.
8. **vs Shipment Visibility Platform (§18, unprocessed)** — forwarder systems consume tracking events into the consignment record and act on them; a visibility platform watches without committing, documenting, or settling. Consistent with the TMS pass's seam #3.
9. **vs Courier / Last-mile / Delivery Types** — those center the operator's own delivery workforce; the forwarder procures carriage from operating carriers and orchestrates the international chain. Local pickup/delivery legs inside a consignment are L1 machinery of this Type.
10. **Naming note (no alias):** market vocabulary includes "freight forwarding software/system", "forwarder TMS", "freight management platform", "cloud ERP for freight forwarders", "logistics OS". The leaf "Freight Forwarding System" is read as the forwarder's business system of record — the market's dominant product category. No directory change proposed.

## Uncertainties

- **No Tier-1 help-center documentation reachable** for any sampled product; all observations are Tier-2 product-page depth. Workflow details (exact task queues, document field schemas, charge-code mechanics, workflow-template internals) are not asserted.
- **"Shipment liquidation" semantics** (Magaya's per-job close-out): name directly observed; the estimate-vs-actuals mechanics are inferred from the "Full PnL by Operations" context, marked as inference.
- **House/master document layering**: house-document issuance is directly evidenced for the NVOCC posture (Magaya NVOCC bill-of-lading generation) and via in-repo air-cargo research (CargoWise air module: MAWB on the forwarder job; HAWB layered when consolidating). The general "house under master" pattern is industry-standard but was not re-verified at help-center depth this pass; written as the common form, not the invariant.
- **Agent intercompany settlement flows** (how origin/destination agents charge each other) not directly evidenced; only document/data exchange between agents is.
- **Enterprise/legacy poles beyond the sample** (e.g., large-suite modules inside global SIs) not sampled; no claim depends on them.
- **Domestic-only forwarders**: whether purely domestic forwarding postures are a distinct market segment or edge cases of this Type was not settled by the sample; recorded as a variant note.

## Historical / Market-Sample Check (§24-style)

Paper-era forwarder office (steamship/air-cargo era, mid-20th century): a customer hands over an export consignment; the forwarder opens a consignment file (the job); quotes the customer a sell price covering freight plus local charges; books space on the steamship line/airline (the carrier's master document) — often consolidating several customers' shipments under its own house waybill/house bill of lading; arranges pickup, receiving, and export customs papers; correspondences with the overseas agent for destination handling and delivery; keeps a charge sheet of what it bought (freight, handling, duties advanced) against what it sold; invoices the customer at completion. All three L0 legs are satisfied at analog level — consignment file, arranged multi-leg carriage with both-ends orchestration, house/trade documents and two-sided charges — with zero software. The vendors' own heritage lines corroborate the pre-history (Softlink: "From DOS to AI — over 3 decades"; Riege's decades-old family software; Magaya customers "since 2006"). The digital check passes: the definition names no cloud, EDI, networks, portals, or AI.

Regional check: the same office exists across regimes with different customs authorities, document conventions, and languages (Riege sells 4-country customs variants; Softlink runs "localized compliance, multi-currency, and region-specific workflows"); the L0 names no authority, document standard, or region.

## Final Synthesis

A Freight Forwarding System is the freight forwarder's business system of record. Its defining core is three jointly-held structures: the consignment (shipment job) as the single persistent record accumulating the customer's whole freight operation; arranged-not-operated multi-leg carriage procured from operating carriers with both-ends services (origin pickup/receiving/handling, border formalities, destination delivery) orchestrated on that same record; and the forwarder's document-and-charge layer — transport, commercial, and trade documents generated from the job (commonly the forwarder's house documents under the carrier's master when consolidating) plus a two-sided charge ledger (sell charges to the customer against buy costs to carriers and partner agents) with per-consignment profitability. Around this core, mature products add rate management (buy/sell, schedules, quote-to-booking), carrier connectivity and event messaging, workflow templates and milestone/exception machinery, LCL/FCL consolidation with warehouse/CFS, customs and trade formalities as consignment steps, inland pickup/delivery legs, overseas agent networks with shipment transfer between branches/partners, per-job financial close-out, and customer self-service portals. Postures vary (enterprise single-platform, modular SMB suite, regional ERP, lean TMS-plus-community), the forwarder-as-carrier NVOCC posture is a variant of the same Type, and regime depth varies by market — none of it moves the core. The Type is separated from the brokerage by scope and document/charge world (ratified), from air/ocean cargo systems by center of gravity (ratified for air; flagged for ocean), from the TMS by whose freight and resale economics (ratified), from customs-compliance platforms by declaration-vs-consignment centers (held), and from visibility/courier/audit-payment Types by transacting-vs-watching, procured-carriage-vs-own-workforce, and whose-payables seams.
