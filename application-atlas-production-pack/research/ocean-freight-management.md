# Research Notes — Ocean Freight Management

Research date: 2026-09-09
Slug: ocean-freight-management
Directory leaf: Ocean Freight Management (Section 18 — Transportation, Mobility & Logistics)

## Research Goal

Understand what "Ocean Freight Management" software actually is in the market: who uses it, what objects exist inside it, what work flows through it, and where its boundary lies against neighboring Types (Freight Forwarding System, TMS, Shipment Visibility Platform, Vessel Operations Platform, Port Terminal Operating System, Air Cargo Management).

## Initial Boundary (hypothesis before research)

- Hypothesis: cargo-side (shipper / freight forwarder / NVOCC) system for managing containerized ocean freight — booking space with carriers, transport documentation (bill of lading), container-level tracking, and ocean-specific costs.
- Not the carrier side (vessel operations / marine fleet management), not the terminal side (port TOS), not generic multi-modal TMS, not tracking-only visibility.
- Nearest neighbors: Freight Forwarding System (multi-modal business system), TMS (multi-modal planning/execution), Shipment Visibility Platform (tracking-only), Air Cargo Management (air-mode analog).

## Research Questions

1. What is the unit of record? What objects compose an ocean shipment (booking, containers, ports, vessel/voyage, documents, charges)?
2. How does the carrier execution loop work (quote → booking → confirmation → shipping instructions → bill of lading)?
3. How does container-level tracking work, and who "owns" the status truth?
4. What ocean-specific commercial machinery exists (rates, surcharges, free time, demurrage/detention, invoicing)?
5. Who uses the system and in what roles (forwarder ops, NVOCC, BCO shipper, documentation, finance)?
6. What market forms exist (forwarding-platform module, standalone ocean SaaS, booking network, rate network, visibility API)?
7. What are the important rules/exceptions (cut-offs, rollover, container reuse, house vs master B/L)?
8. Historical check: would a paper-era forwarder/NVOCC practice still fit the definition?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Form | Philosophy | Customer tier |
|---|---|---|---|
| CargoWise (WiseTech Global) | ocean mode of a multi-modal forwarding platform | single-database end-to-end forwarding; ocean as one mode | large global forwarders (DHL-class tier referenced via customer logos: CEVA, Hellmann, Yusen...) |
| Magaya | modular forwarder/NVOCC platform | modular suite (Supply Chain + Rate Management + Portal + extensions) | mid-market forwarders, NVOCCs, 3PLs |
| INTTRA (by e2open) | neutral ocean booking network | one interface to the largest ocean-carrier network; booking/SI/tracking exchange | BCO shippers + forwarders + carriers |
| CargoSphere (WiseTech) | ocean rate management network | rates-first: contract digitization + confidential rate distribution | forwarders/NVOs, carriers, shippers/BCOs |
| Vizion | container tracking API / visibility data layer | standardized milestone events pushed into other systems | LSPs, software vendors, BCOs (data consumers) |

Note: CargoSphere and Vizion were sampled deliberately as boundary probes — to test whether rate management alone or tracking alone constitutes the Type (finding: they do not; they are adjacent specialist layers).

## Sources

All fetched 2026-09-09 (official vendor pages; Tier 1/2 mix — product/solution pages, no gated help-center content):

- CargoWise — https://www.cargowise.com/ (root) and https://www.cargowise.com/solutions/cargowise-forwarding/ocean/ (Ocean page)
- Magaya — https://www.magaya.com/ (root), https://www.magaya.com/nvocc-software/ (NVOCC page), https://www.magaya.com/container-tracking-software/ (Container Tracking page)
- INTTRA — https://www.inttra.com/ (root) and https://inttra.com/shipper-solutions/ocean_trade_platform (Ocean Trade Platform)
- CargoSphere — https://www.cargosphere.com/ (root)
- Vizion — https://www.vizionapi.com/ (root)

Source-access limitation: deep operational help centers (CargoWise product docs, Magaya Help Site, INTTRA Knowledge Center) were not fetched; the evidence base is official product/solution pages. Precise operational facts (exact milestone name lists, exact free-time defaults, exact cut-off windows, numeric limits) are therefore NOT asserted anywhere in this research or in the final document. Shipwell ocean page returned 404 and was abandoned after one attempt (not retried).

## Product Observations

### CargoWise — Ocean (forwarding platform, ocean mode) [Evidence layer: A]

From https://www.cargowise.com/solutions/cargowise-forwarding/ocean/:

- Positioning: "Master the movement of your ocean freight" — "full visibility and control across bookings, schedules, and container movements, with direct carrier connections and workflows built to handle every stage from origin to destination."
- Sailing schedules: search and compare schedules; automatic carrier updates; real-time voyage details.
- Rates: "Search and apply competitive ocean rates, calculate precise costs and margins, and seamlessly move from quote to confirmed booking."
- eBookings: "direct, data-driven ocean eBookings with carriers, giving you faster confirmations, fewer errors, and complete visibility from booking to bill of lading."
- Direct carrier connections: "Exchange direct electronic messages for schedules, booking, tracking, verified gross mass, shipping instructions, and bill of lading data"; view "fully digital, confidential contracted rates and published global tariff surcharges."
- Electronic port connections: send shipment data to ports, submit documents, per-port message standards "built into the CargoWise platform", exception management if messages not sent by a certain date/time, complete audit trail of shipment transactions.
- NVOCC electronic messaging: automate "booking requests, shipping instructions and consolidation advice"; CargoWise-to-CargoWise messaging between forwarders and NVOCCs.
- CarrierConnect: compare carrier options side by side (charges, service levels, transit times, terms); rates from CargoWise and external rate sources in one view; connect selected rates into forwarding workflows.
- Container Automation: "integrated carrier data and global AIS coverage... transforms complex vessel movements into clear, actionable intelligence. Every delay, diversion, or status change triggers automated workflows."
- Stated end-to-end flow: "End-to-end shipment visibility from first email to final invoice": (1) optimize quote-to-booking (rates from real-time carrier tariffs, pre-populated margins and surcharges, accepted quotes transfer into bookings without re-entry); (2) monitor job shipments (real-time container movement updates, automatic delay notifications, messages to customers, "minimize penalties or wasted charges"); (3) automate operations (close completed tasks, generate and distribute documentation and EDI, "raise exceptions like missed cargo ready dates").
- Milestones: "Track hundreds of events in real time. From the point of pickup through to delivery... data connectivity from multiple parties including shipping lines, port systems, vessel AIS, as well as customs and transport... in addition to your internal events, such as document creation, invoice production."
- Exceptions: "A full log of every current and historical exception, with configurable alerts... if something is missed or nearing its deadline."
- Workflow engine: configurable templates per shipment type (modes, trade lanes, directions, clients); task ownership ("who is doing what and when"); triggers for milestone communication.
- Users named: freight forwarders and NVOCCs (solutions pages); carriers are served by a separate product line ("Liner and Agency" — "Control your entire ocean operations from a single platform" — carrier-side, different system).

### Magaya (forwarder/NVOCC platform) [Evidence layer: A]

From https://www.magaya.com/nvocc-software/:

- Audience: NVOCCs ("managing or holding cargo containers for shippers... organizing shipments for a company using another company's carrier"), freight forwarders, 3PLs, customs brokers.
- Core operations: "create quick FCL (full container load) and LCL (less than a full container load) bookings on ocean carriers, receive online booking requests"; "set up easy-to-understand air, ocean, and ground shipment consolidations, exchange shipping instructions (from freight to ocean to air and back), and quickly generate the Bill of Lading and other required documents."
- Shipment types: export/import/domestic; ocean/air/ground; "Consolidations, Straights, LCL or FCL"; RORO.
- Rate Management module: "searching and comparing rates, managing margins and allocation commitments, filing tariffs, responding to RFQs, and preparing winning quotes"; "direct integration to ocean carrier rate data with DCX (digital contract exchange)"; "compare contract base rates as well as conditions like transit time, free-time, floating surcharges, spot rates, and benchmark rates"; FMC tariff filing.
- Feature list: freight charges/quotes/margins/rate management; freight bookings; shipments; purchase order management; customs compliance and documentation; container tracking; billing, invoicing, accounting; configurable documents; cargo insurance; INTTRA and carrier integration; digital customer portal.
- Flow claim (Supply Chain): "pulling information from quotes to create bookings, pickup orders, warehouse receipts, shipments, and invoices" — one transaction chain; accounting records generated from logistics transactions.

From https://www.magaya.com/container-tracking-software/:

- "Track all your ocean containers worldwide with one click, right from Magaya Supply Chain. Get real-time updates from terminals, rail carriers, and 200+ ocean carriers. Spot issues early and take action before costly demurrage and detention fees stack up."
- Data source: "Ocean carrier EDI... as well as direct connections to North American ocean terminals and U.S. rail carriers."
- "The vessel line sets the statuses." (carrier is the source of status truth)
- Milestones: "over 1,000 configurable milestones using Transaction Tracking"; events flow into the Magaya system and surface in customer portals/apps.
- Container identity: "Since container numbers are not always unique... Once the sealine has ended a shipment, this is communicated via the Container Tracking updates, and when the container is reused for future shipments, the system will not start a brand new tracking."
- Multiple containers per shipment: "Yes... adding and repacking the additional containers on a single shipment."
- Tracking is opt-in per container ("You do need to select which containers to track") — i.e., tracking is an extension attached to the shipment record, not the record itself.
- Works for import and export; keyed on container number.
- Exception framing: "Alerts you to exceptions so that you can take swift action, avoiding demurrage and detention fees."

### INTTRA Ocean Trade Platform (booking network) [Evidence layer: A]

From https://inttra.com/shipper-solutions/ocean_trade_platform:

- Positioning: "digitalizes the entire container booking process for BCOs and Freight Forwarders"; "electronic booking, digital transmission of shipping instructions and real-time container status tracking. Your one-stop connection to the most extensive network of ocean carriers."
- Capabilities: Booking ("book directly on one interface with the industry's largest ocean carrier community"); Maersk Spot Rates ("Grab spot rates with Maersk and book your ocean shipment"); Shipping Instructions ("electronic shipping instructions... meet carrier documentation cut-off times – preventing your containers from being rolled or held"); Track and Trace ("real-time container status events and alerts"); Electronic Shipping Orders ("simplify China's unique shipping procedures... enable exporters and Booking Agents in North China to quickly create and send shipping documentation").
- Documented 7-step flow: "Step 1: Create Booking Request → Step 2: Carrier Spot Rate results will list available 'offers' → Step 3: Shipper can view details associated with the Spot Rate offer → Step 4: Submit spot rate or standard booking request → Step 5: Receive booking confirmations → Step 6: Submit shipping instructions → Step 7: Receive Bill of Lading."
- Other shipper solutions: Ocean Schedules, eVGM (verified gross mass), Reporting and Analytics.
- Testimonial evidence of usage pattern: AGT Foods ("consolidation platform has led to saving on Bill of Lading fees per shipment"); Kuehne & Nagel ("standards for electronic entry with a number of carriers... data quality"); Intercomex (staff ratio per 100 shipments improved using "INTTRA Desktop").
- No freight invoicing/rate-contract management in the described scope (rates appear only as carrier spot offers) — booking/SI/tracking exchange is the center.

### CargoSphere (ocean rate network) [Evidence layer: A — boundary probe]

From https://www.cargosphere.com/:

- Positioning: "The world's connector for ocean rates. Join CargoSphere's neutral rate network for container shipping." "Shipping Rates Management Software."
- SUDS: "Turn static rate contracts into clean, actionable, accurate data" — upload carrier contracts fast, in-house.
- Rate Mesh: "an intertwined online network of carriers, forwarders and shippers who confidentially distribute rates to one another... service providers delivering rates to customers confidentially and in real-time using cloud-based technology rather than static files."
- Buy/sell margins on quotes; "quote more shipments and close more deals."
- Audiences: forwarders & NVOs, carriers & consolidators, shippers & BCOs.
- No shipment record, no booking, no container tracking in the described scope — rates only. Confirms rate management alone is a specialist layer, not the Type.

### Vizion (container tracking API) [Evidence layer: A — boundary probe]

From https://www.vizionapi.com/:

- Positioning: "Get Real-Time Container Tracking and Monitor Global Trade"; "Push the most complete, standardized, and detailed container tracking events via API to any spreadsheet, ERP, TMS or other software system."
- "7000 Unique events turned into 60 standardized milestones"; sources: EDI, AIS, port/terminal connections.
- Ocean-specific cost signal: "Our Last Free Date (or Free Time to Expire) event alerts you to when demurrage charges will start so that you can plan for pickups and reduce these avoidable costs."
- Also: intermodal rail tracking, customs clearance API, port performance, global trade intelligence (TradeView).
- No booking, no shipping instructions, no B/L, no shipment of record — tracking data only. Confirms visibility alone is a specialist layer (Shipment Visibility Platform territory), not the Type.

## Cross-product Comparison

| Dimension | CargoWise | Magaya | INTTRA | CargoSphere | Vizion |
|---|---|---|---|---|---|
| Ocean shipment as managed record | Yes (job/shipment with docs, charges, events) | Yes (shipment transaction chain quote→booking→shipment→invoice) | Booking-level records (booking request→confirmation→SI→B/L) | No | No |
| Booking with ocean carrier | Yes (eBookings, direct carrier connections) | Yes (FCL/LCL bookings, online booking requests) | Yes (core purpose; carrier network) | No | No |
| Shipping instructions exchange | Yes (electronic messages) | Yes ("exchange shipping instructions") | Yes (electronic SI; cut-off framing) | No | No |
| Bill of lading | Yes ("booking to bill of lading"; B/L data messages) | Yes ("generate the Bill of Lading and other required documents") | Yes ("Receive Bill of Lading") | No | No |
| Container-level milestone tracking | Yes (carrier data + AIS; delay/diversion triggers) | Yes (extension; 200+ carriers; EDI + terminals + rail) | Yes (track & trace events and alerts) | No | Yes (core purpose; standardized milestones) |
| Rates / surcharges | Yes (search/apply rates, margins, tariff surcharges) | Yes (rate management module; free-time, floating surcharges, spot) | Spot offers only (Maersk) | Yes (core purpose; contract digitization, distribution) | No |
| Demurrage/detention framing | "minimize penalties or wasted charges" | "avoiding demurrage and detention fees" | "preventing your containers from being rolled or held" | No | Yes (Last Free Date / free-time-to-expire alerts) |
| Freight cost / invoicing | Yes ("first email to final invoice"; invoice production as internal events) | Yes (billing, invoicing, accounting) | No | No | No |
| Customer-facing portal | Yes (portal for trading parties) | Yes (Digital Freight Portal) | Portal (ship.inttra.com) | No | App/API (BoxTrack) |
| Customs/regulatory touchpoints | Port messaging, customs authorities, VGM | AMS/ABI customs compliance; VGM via integrations | eVGM; China Shipping Orders | No | Customs clearance API |
| Serves carriers as customers | Separate product line (Liner & Agency) | No (forwarder/NVOCC side) | Yes (carrier solutions) | Yes (carrier rate distribution) | No (data consumers) |

Reading of the comparison:

- The three capabilities that co-occur only in the shipment-management population (CargoWise, Magaya, INTTRA): shipment record + carrier execution loop (booking → shipping instructions → B/L) + container follow-through.
- Rate machinery is present in the platform-form products and the rate specialist, but absent in the booking network's core scope and the visibility layer → common, not definitional.
- Invoicing/accounting is present only in the platform-form products → common, not definitional.
- Tracking-only (Vizion) and rates-only (CargoSphere) each fail to constitute the Type → they are adjacent specialist layers whose capabilities get bundled into full products.

## Canonical Model

### L0 — Defining Invariant (minimal)

The Type is the cargo-side system of record for moving goods by sea. Three jointly-held structures:

1. **The ocean shipment as the unit of record.** A persistent, individually identified record of moving specific cargo by sea between named ports — carrying the booking with a carrier, the containers that physically hold the cargo, the route/vessel/voyage context, and the shipment's documents and charges. Remove → rate tables, tracking feeds, or one-off booking transactions with no managed shipment.
2. **The carrier execution loop.** The cargo-side party books space with an ocean carrier (or acts as NVOCC issuing its own document), exchanges shipping instructions, and obtains/produces the bill of lading that governs the cargo. Remove → a visibility tool or schedule search; the execution is gone.
3. **The voyage follow-through.** The shipment's containers are tracked through port-to-port milestones against the plan, with exceptions (delays, rollover, missed cut-offs, free-time expiry) surfaced for action until the cargo is delivered. Remove → a booking portal with no follow-through; the "management" is gone.

Jointly-held load-bearing analysis:

- 1 alone = a shipment data log (no execution, no follow-through)
- 2 without 1+3 = booking transactions with no memory and no follow-through
- 3 without 1+2 = pure container visibility (Vizion pole — different Type)
- 1+2 without 3 = booking + documentation with no operational follow-through
- 1+3 without 2 = tracking attached to records but no execution capability (shipper tracking sheet — visibility territory)

Mode binding is part of the invariant: ocean objects (containers, vessel/voyage, bill of lading, ports, free time) are what the record is made of. Remove the ocean binding → generic forwarding/TMS territory.

### L1 — Common Mature Structure (very common, not definitional)

- Rate search and quote-to-booking flow (rates, surcharges, margins) — CargoWise, Magaya; spot offers at INTTRA
- Freight charges on the shipment and invoicing/accounting hand-off — CargoWise ("first email to final invoice"), Magaya
- Sailing schedule search and comparison — CargoWise, INTTRA
- Automated carrier connectivity (EDI/API) as the dominant implementation of the execution loop and tracking — all three shipment-management products
- Customer-facing portal / self-service quotes-booking-tracking — CargoWise, Magaya, INTTRA
- Exception management (missed cargo ready dates, delays, cut-off risk) — CargoWise, Magaya, INTTRA
- Demurrage/detention awareness (free time, last-free-date, penalty avoidance) — Magaya, Vizion, INTTRA (rolled/held), CargoWise (penalties)
- Consolidations (LCL/FCL, consolidation advice) — Magaya, CargoWise
- Customs/regulatory touchpoints (VGM, port messaging, AMS/ABI filings as integrations) — CargoWise, Magaya, INTTRA
- Workflow automation / task management over shipments — CargoWise, Magaya

### L2 — Variant / Optional Structure

- Operator posture: forwarder (arranges on behalf of customers) vs NVOCC (issues own house B/L, buys vessel space) vs BCO shipper (manages own ocean moves) — all three in-sample audiences
- Load type: FCL vs LCL consolidation vs RORO/breakbulk (Magaya lists RORO; containerized is dominant)
- Direction: export vs import vs domestic legs (Magaya)
- Regional regulatory machinery: US AMS/ISF (ABI), FMC tariff filing, SOLAS VGM, China Shipping Orders (INTTRA North China)
- Network form: neutral booking network (INTTRA) and confidential rate-distribution network (CargoSphere) as specialist realizations of single lifecycle stages
- Visibility-first form: API/data-layer products (Vizion) consumed by the systems of record
- Deployment: cloud-hosted vs on-premise lineage (Magaya Cloud)
- Multi-modal breadth: ocean-only vs ocean-inside-multi-modal platform (CargoWise, Magaya both multi-modal)

### L3 — Vendor-specific (research notes only)

- CargoWise CarrierConnect (side-by-side carrier comparison), CargoWise-to-CargoWise NVOCC electronic messaging, Electronic Port Connections with per-port message standards
- Magaya DCX (digital contract exchange with ocean carriers), LiveTrack mobile app, Transaction Tracking with 1,000+ configurable milestones, Magaya Network (inter-customer document exchange)
- INTTRA Maersk Spot integration, INTTRA Desktop (legacy client), Electronic Shipping Orders for North China
- CargoSphere SUDS (Smart Upload and Diagnostic Solution) and Rate Mesh
- Vizion "7000 unique events → 60 standardized milestones", BoxTrack, TradeView

## Vendor-specific Findings

See L3 above. None of these are promoted to the canonical model. The NVOCC/forwarder/BCO role split is market-structural, not vendor-specific.

## Boundary Findings

- **vs Freight Forwarding System**: forwarding is the multi-modal business system of a forwarder (air + ocean + road, customs brokerage, warehousing, agent networks, accounting). Ocean Freight Management is the ocean-mode slice. In the sampled market, the Type is heavily realized as the ocean module inside forwarding platforms (CargoWise ocean mode; Magaya Supply Chain ocean shipments). Test: remove the multi-modal business breadth (customs, warehouse, other modes) and keep the ocean shipment lifecycle → this Type; remove the mode-specificity → forwarding system.
- **vs Transportation Management System / TMS**: TMS plans and executes transportation across modes (procurement, routing, load tendering). The ocean slice of an enterprise TMS overlaps this Type; the difference is the object set (containers, B/L, vessel schedules, demurrage vs trucks/loads/carrier procurement). Not directly sampled (Shipwell 404) — assertion kept weak.
- **vs Shipment Visibility Platform**: visibility products aggregate and standardize tracking events (Vizion) but hold no booking, no documents, no shipment of record, no execution loop. Test: remove the execution loop (booking/SI/B/L) → visibility platform.
- **vs Vessel Operations Platform / Marine Fleet Management**: those are carrier-side (operating vessels and container fleets). CargoWise explicitly serves that side with a different product line ("Liner and Agency"). Ocean Freight Management is cargo-side (buying space / arranging carriage).
- **vs Port Terminal Operating System**: terminal-side yard and vessel operations at a port; not shipment-of-record management for cargo owners.
- **vs Air Cargo Management**: air-mode analog with different objects (AWB, ULD, flight vs B/L, container, vessel/voyage). Same cargo-side logic, different mode machinery.
- **vs Freight Audit & Payment**: invoice auditing/payment is a specialist downstream slice; ocean freight management carries freight costs on the shipment but audit/payment is not its center.
- **vs Customs Compliance Platform / Global Trade Management**: border filings and trade regulation are adjacent integrations (AMS/ABI, VGM, port messaging), not the defining core.
- **"去掉什么就变成另一个 Type" 判据**: remove the carrier execution loop → Shipment Visibility Platform; remove the ocean mode binding → Freight Forwarding System / TMS; remove the shipment record (keep only rates) → ocean rate management (specialist layer, no directory leaf of its own); move to the carrier side → Vessel Operations Platform.

## Historical / Market-Sample Check

- Paper-era forwarder/NVOCC practice: a shipment file (folder) per consignment; booking arranged by telex/phone with the liner; a rate quote sheet with surcharges; the bill of lading typed and released; status notes from agents recorded by hand. All three L0 structures are present (record + execution loop + follow-through) with no EDI, no cloud, no AIS. The definition holds.
- Older/regional NVOCCs running spreadsheets + carrier portals + email also satisfy the core (the loop is executed through portals/email rather than embedded EDI).
- The modern dominant implementation (direct EDI/API carrier connectivity, automated milestone feeds, AIS vessel data) is therefore the implementation layer, not the definition. Anti-overfit rule applied: EDI connectivity is how the loop is usually wired today, but the loop itself (booking → SI → B/L) is the invariant.

## Uncertainties

- Exact milestone vocabularies vary by product and by carrier (Magaya: "the vessel line sets the statuses"; Vizion: thousands of raw events standardized into a smaller milestone set). No canonical milestone list is asserted.
- Whether BCO-facing shipper-side products (without any forwarding/NVOCC function) form a distinct sub-population was not deeply sampled; INTTRA serves BCOs with booking/SI/tracking, which suggests BCO-side ocean shipment management fits the same core. Confidence: moderate.
- Enterprise TMS ocean modules (Oracle OTM, SAP TM class) were not sampled (source 404 / out of budget); their overlap with this Type is asserted only as a boundary relationship, not characterized in detail.
- Demurrage/detention depth (dispute workflows, per-terminal free-time tables) was observed only as alerts/conditions, not as full cost machinery; depth unknown.
- Precise numeric facts (free-time durations, cut-off windows, carrier counts beyond what vendors publish) intentionally not stated.

## Final Synthesis

Ocean Freight Management is the cargo-side system of record for containerized ocean freight. Its defining core is three jointly-held structures: the ocean shipment as a persistent managed record (booking + containers + route + documents + charges), the carrier execution loop (book space → exchange shipping instructions → obtain the bill of lading), and the voyage follow-through (container-level milestones and exceptions from gate-in to delivery). Rates/surcharges, invoicing, customer portals, consolidations, customs touchpoints, and workflow automation are common mature additions; booking networks, rate networks, and visibility APIs are specialist realizations of single lifecycle stages that bundle into full products. The Type is heavily realized as the ocean module of multi-modal forwarding platforms, but the ocean shipment lifecycle itself — not the forwarding business as a whole — is what defines it.
