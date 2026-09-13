# Research Notes — Air Cargo Management

## Research Goal

Understand what an Air Cargo Management application actually is from real products: what objects exist inside it, who operates it, how a shipment moves through the air carriage chain, what rules constrain the work, and where the Type's boundary sits against Freight Forwarding System, TMS, Ocean Freight Management, Airline Reservation/PSS, Airline Operations, Ground Handling Management, and Parcel/Courier systems.

## Initial Boundary

Working hypothesis before research:

- Core purpose: manage air freight — goods carried by air under air waybills — across booking on flights, airport terminal handling, the airport-to-airport carriage, and the associated commercial cycle (rating, charging, settlement).
- Likely operators: airline cargo divisions, ground handling agents / cargo terminal operators; freight forwarders interact as customers and run their own (adjacent) systems.
- Nearest neighbors: Freight Forwarding System (forwarder-side), Ocean Freight Management (mode sibling), Airline Reservation/PSS (passenger analog), Airline Operations Platform (flight ops), Ground Handling Management (passenger/ramp handling), Parcel/Courier (door-to-door express), TMS (shipper-side ground planning), Shipment Visibility Platform (read-only layer).
- Open questions: is rating definitional? Are GHA cargo-terminal systems a variant of this Type or a separate one? Is the directory leaf carrier-side only, or does it span the air cargo chain?

## Research Questions

1. What is the central record — booking, air waybill, shipment, consignment? How do MAWB/HAWB relate?
2. What is the shipment lifecycle, and which statuses/events are exchanged between parties?
3. How is capacity managed (flights, allotments, load control)?
4. How does rating/charging work, and where does it sit in the system?
5. How do the three operator sides (airline, ground handler/terminal, forwarder) divide the work, and how do their systems differ?
6. What physical-handling objects exist (ULDs, warehouse locations, screening)?
7. What compliance rules are embedded (dangerous goods, security screening, customs)?
8. What interfaces exist (back-office, warehouse, portals, messaging)?
9. Where exactly is the boundary to Freight Forwarding System and to Ocean Freight Management?

## Representative Products

Selected for market coverage across the three operator sides, different product philosophies, and different customer tiers:

| Product | Vendor | Side | Tier / Philosophy |
|---|---|---|---|
| CargoWise | WiseTech Global | Freight forwarder (air freight module) | Global enterprise standard; single-platform logistics OS |
| iCargo | IBS Software | Airline cargo + ground handlers | Tier-1 carrier platform; modular suite (sales, RM, terminal, ULD, revenue accounting, mail) |
| Hermes 5 | Hermes Logistics Technologies | Ground handling / cargo terminal | Specialist GHA cargo management ecosystem, SaaS |
| Magaya (Supply Chain) | Magaya | Freight forwarder / 3PL (SMB–mid) | Integrated forwarding + warehouse + compliance for smaller operators |

Industry-standard layer (not a product, but defines the shared objects and flows): IATA e-freight/e-AWB, ONE Record, Cargo iQ route maps, Dangerous Goods Regulations, Cargo Agency Program/CASS.

Rejected/abandoned sample: CHAMP Cargosystems (Cargospot) — the historically dominant carrier-side vendor — could not be reached (see Sources).

## Sources

Fetched 2026-09-06:

- CargoWise — Air Visibility solution page: https://www.cargowise.com/solutions/cargowise-forwarding/air/ (Tier 2, product marketing with feature detail)
- CargoWise — root: https://www.cargowise.com/ (Tier 2)
- IBS Software — Air Cargo solutions: https://www.ibsplc.com/product/air-cargo-solutions (Tier 2)
- IBS Software — iCargo product page: https://www.ibsplc.com/product/air-cargo-solutions/icargo (Tier 2, module-level detail)
- Hermes Logistics Technologies — root: https://hermes-cargo.com/ (Tier 2)
- Hermes Logistics Technologies — Hermes 5 SaaS: https://hermes-cargo.com/products-services/hermes-5-saas/ (Tier 2)
- Magaya — root: https://www.magaya.com/ (Tier 2)
- IATA — Cargo: https://www.iata.org/en/programs/cargo/ (industry standards body)
- IATA — Digital Cargo (e-freight/e-AWB, ONE Record): https://www.iata.org/en/programs/cargo/e/ (industry standards body)
- Cargo iQ: https://www.cargoiq.org/ (industry standards body)

Failed / abandoned:

- CHAMP Cargosystems (https://www.champcargosystems.com/) — transport error + timeout, two attempts, abandoned per network-limitation rule.
- IATA e-AWB direct URL (https://www.iata.org/en/programs/cargo/eairwaybill/) — 404; covered instead via the Digital Cargo page.

**Source-access limitation:** No vendor help-center / user-guide level documentation was reachable for any sampled product (carrier-side vendors publish almost no operational documentation publicly; forwarder-side help sites were not fetched). All product evidence is therefore Tier 2 (official product/solution pages). Consequences applied: (1) operational workflows are written at conceptual level, not screen/keystroke level; (2) no precise numeric parameters (volumetric divisors, message code lists, time windows, stock thresholds) are asserted anywhere; (3) carrier-side observations rest on one deep source (iCargo) plus industry standards, and are marked accordingly.

## Product Observations

### CargoWise (WiseTech Global) — forwarder-side air freight

Evidence layer: A (directly observed on official product pages).

- Air freight execution is a mode inside the forwarding platform: "Optimize the execution of your air freight… keeping every shipment on schedule and every process aligned."
- **eBookings**: direct connections to airlines; book faster, access live capacity, receive instant updates, automate air waybill and shipment status handling.
- **Rates**: search/compare air freight rates by origin, destination, airline, or commodity; calculate costs and margins; accepted quotes convert into confirmed bookings without re-keying.
- **Flight Schedules**: global airline schedules and connections in real time; automatic departure/arrival change updates; "instantly complete voyage details from live data."
- **Air Waybill Automation**: flight status events delivered into the system ("corresponding flight status events directly to your CargoWise system"); events flow "through the whole of the freight lifecycle, triggering automatic alerts, exceptions and processes"; key events contain date/time/location of the aircraft, including pre-advices, delays, estimate changes; any involved party (BCO, origin/destination agent, customs broker) can track flights on all routing legs.
- **AirlineConnect**: explore flight options, dynamic pricing, transit times across routes/airlines; real-time eBooking status updates after submission; direct API connections to named airlines (Air Canada, Air France, BA, Cathay Cargo, Emirates, Etihad, Finnair, Iberia, ITA, Korean Air, KLM, Lufthansa, Qatar, etc.).
- **Electronic Messaging**: replaces "missing, incorrect or illegible paper-based Air Waybills"; exchange information with the network "up until the cargo arrives at its intended destination"; customs clearance acceleration; compliance with "ever-changing and evolving cargo security regulations"; automated eDocs filing with audit trail.
- **CargoTracker**: map-based visualization; current cargo position, past/predictive routes across multiple legs; split cargo identification with ETAs per part; "current flight statuses, key milestones, consignment details, MAWB number, and number of pieces."
- **Workflow engine**: configurable tasks/milestones/triggers per shipment type (mode, trade lane, direction, client); exception log with configurable alerts; "from the point of pickup through to delivery."
- Status updates: bookings move "from planned to confirmed", single or multi-leg; airline changes after confirmation propagate.

Interpretation: the forwarder-side air module centers on the shipment job + booking + AWB + status events; it consumes airline capacity as a buyer. No ULD or terminal-warehouse control on the air page (forwarders don't operate terminals).

### iCargo (IBS Software) — carrier-side platform

Evidence layer: A (directly observed on official product pages).

Positioning: "modern cloud platform for air cargo management and stakeholder collaboration" for "cargo carriers and ground handlers"; "match real-time demand with available capacity for maximum profitability"; "dynamic pricing engine, advanced forecasting algorithms, and instant accounting reconciliation."

Modules (independently deployable):

- **iCargo Airline** — "sales, inventory and reservation system": accurate available-capacity forecasts; shipment yield/revenue visibility; "powerful and flexible up-front rating function" (shipment value identification at booking); "real-time visibility of cargo demand and capacity on flights with powerful tools to optimize load"; "shipment transportation plan and tracking function"; configurable customer database with loyalty; "product and service-based allotment of capacity to POS and customers"; "automate screen and review workflows at booking or AWB/HAWB modification" (security compliance).
- **iCargo Revenue Management** — dynamic pricing; "dedicated RM engine built specifically for air cargo business"; AI-driven revenue protection; integrated to sales and operations.
- **iCargo CRA / MRA (revenue accounting)** — back-office accounting for air cargo and mail; electronic billing/payables; "automated interline settlement processing: fully compliant to IATA SIS (Simplified Invoicing and Settlement)."
- **iCargo Mail** — UPU-compliant mail handling; piece (mailbag) level tracking; RF hand-held barcode scanners; mail invoicing/accounting.
- **iCargo CTO (Cargo Terminal Operations)** — "automates self-handled facility and compliance processes for airlines, ground handlers, and airports"; one-time real-time data capture with mobile scanner devices; "robust messaging function with coverage of Cargo IMP, AHM and ULD related messages"; integration with warehouse equipment (weigh scales, ETV) and Customs EDI; centralized multi-airport deployment with airport-specific configuration; e-Freight & Cargo2000 compliance; integrated SLA management.
- **iCargo ULD** — "all aspects of ULD asset management and tracking"; airlines track ULDs across the network; airports/ground handlers track customer airlines' ULDs; loan/borrow transactions with demurrage calculation; "ULD movements and stock are instantly updated based on flight departures and arrivals"; stock thresholds; universal ULD messaging standards; "airline or network mode, as well as cargo handler or airport mode."
- **iPartner** — Airline (interline partnerships: partner routes, schedules, availability, rates), Handling (airline↔ground-handler task collaboration over common mobile/web apps replacing paper/email/phone), Customer (airline sales platform connecting to digital freight marketplaces and global forwarders via APIs).

Customer base (from the same pages): belly-cargo airlines (Lufthansa Cargo, American Airlines Cargo, Korean Air Cargo, Qantas Freight, Delta, ANA Cargo, Singapore Airlines Cargo, Turkish Cargo…), all-cargo carriers (Cargolux, Nippon Cargo Airlines, MSC Air Cargo), and ground handlers/terminal operators (Dnata, IACT, TIACT, POS Aviation). Case studies: American Airlines replaced "91 disparate systems"; Korean Air replaced "core mainframe systems integrated to 35 satellite systems"; Qantas Freight mobile transformation ("iCargo Mobility").

Interpretation: the carrier-side system is a commercial + operations suite around capacity: sell (reservation, rating, allotments), optimize (RM), carry (transportation plan, tracking), handle (terminal ops), control equipment (ULD), account (revenue accounting, interline settlement), plus mail as a special commodity.

### Hermes 5 (Hermes Logistics Technologies) — GHA / cargo terminal side

Evidence layer: A (directly observed on official product pages).

- "Hermes 5 (H5) is… the core Cargo Management System, which digitalises the management of import, export, and transit processes within cargo warehouses" at airports; "monitors and controls the import and export processes of your cargo at the airport."
- "real time, mobile warehouse control, process steering and automated messaging and accounting."
- Compliance scope: "From Customs, to bonded goods, and NOtification TO Captain (NOTOC)"; "ensures your cargo meets Dangerous Goods Regulations according to IATA specifications."
- **Hub Management System (HMS)**: same system configured for transit-heavy operations; "auto-prioritisation of tasks based on when specific shipments need to meet outbound bookings or special product Service Level Agreements (SLAs)"; administrator controls processing/prioritization.
- Ecosystem modules: slot booking, track & trace (self-serve), companion app, Business Intelligence, Datalakes, Landside Management; integrations with third-party tech (Nallian, e-CARGOWARE, DGM).
- Data: "from planning, budgeting and invoicing, to scheduling, resource allocation, and reporting."
- Customers: "handling agents and airlines"; 70+ live implementations across four continents.

Interpretation: the GHA-side system centers on the warehouse/terminal execution of the same shipments: import/export/transit processes, task steering against flight bookings and SLAs, DG/NOTOC and customs compliance, messaging to partners, and handling charges (accounting). It manages the same AWB-identified shipments and ULD flows but from the physical-handling seat, not the commercial seat.

### Magaya (Supply Chain) — forwarder-side, SMB/mid tier

Evidence layer: A (directly observed on official pages).

- "single solution for shipping, transportation management, warehouse operations, tracking, connectivity, accounting, and compliance."
- Transaction chain: "pulling information from quotes to create bookings, pickup orders, warehouse receipts, shipments, and invoices" (avoid double data entry).
- Air is one mode among others; **Air Tracking** is an extension; **Carrier Connections** integrate carriers; **Rate Management** searches/compares rates, manages margins/allocation commitments, quotes; **Digital Freight Portal** gives customers quotes→booking conversion and visibility of "freight on the move."
- Industries: freight forwarding (export/import), 3PL, NVOCC, warehouse, courier, customs brokerage.

Interpretation: at the SMB tier, air freight is a shipment mode inside a general forwarding/warehouse platform; the air-specific depth (capacity, ULDs, terminal control) is thin; booking/tracking/rating/invoicing structure matches the CargoWise pattern.

### Industry-standard layer (IATA / Cargo iQ)

Evidence layer: A (official standards-body pages).

- IATA Cargo: airlines transport 62M+ tonnes/year; priorities include digitalization ("air cargo still sits in fragmented systems across the supply chain"), standards (DGR, airport slots), safety/security.
- **Digital Cargo / e-freight / e-AWB**: "e-freight / e-AWB aims to build an end-to-end paperless process for air cargo."
- **ONE Record**: "a standard for data sharing and creates a single record view of the shipment."
- **Cargo iQ**: IATA interest group; "Route Maps concept" and "data-driven performance management approach to improve the end-to-end air cargo shipments flow"; members: airlines, freight forwarders, ground handling agents, trucking companies, IT providers, airports.
- **Cargo Agency Program**: accredits forwarders "to simplify their interaction with airlines" (financial/settlement streamlining — CASS).
- **Dangerous Goods Regulations**: the standards framework referenced by Hermes (NOTOC) and embedded in products.

Interpretation: the industry itself models the world as: shipment with a single record view (ONE Record), paperless AWB (e-AWB), milestone/route-map managed flow (Cargo iQ), standardized messaging between airlines/handlers/forwarders, and regulated commodities (DG). This confirms the shipment+AWB+lifecycle+multi-party-messaging structure at industry level, independent of any vendor.

## Cross-product Comparison

| Dimension | CargoWise (forwarder) | iCargo (carrier/GHA) | Hermes 5 (GHA terminal) | Magaya (forwarder SMB) |
|---|---|---|---|---|
| Central record | Shipment job with MAWB number, pieces, legs | Shipment under AWB/HAWB; transportation plan | Shipment in import/export/transit warehouse processes | Shipment (quote→booking→receipt→shipment→invoice chain) |
| Flight/capacity | eBookings, live capacity, schedules, multi-leg | Reservation + capacity forecasts + load optimization + allotments | Outbound bookings drive task prioritization | Schedules/booking via carrier connections (thin) |
| AWB handling | AWB automation, electronic messaging, eDocs | AWB/HAWB modification workflows; e-Freight | Messaging (Cargo IMP family) | AWB within shipment docs (not detailed) |
| Terminal/warehouse | Not on air page (forwarder doesn't run terminal) | CTO module: mobile scanning, weigh scales, ETV, SLA | Core: mobile warehouse control, process steering, storage | WMS built-in (general warehouse, not air terminal) |
| ULD | Not evidenced | Dedicated ULD module (stock, loan/borrow, demurrage) | ULD-related messages | Not evidenced |
| Rating/charging | Rates by lane/airline/commodity; margins; invoices | Up-front rating at booking; RM engine; revenue accounting; SIS settlement | Automated accounting (handling charges) | Rate management; invoices |
| Status/visibility | Flight status events, map tracking, split cargo, exceptions | Shipment tracking function; messaging | Track & trace module; automated messaging | Air tracking extension; portal visibility |
| Compliance | Cargo security regulations; customs eDocs | Security screening workflows at booking/AWB; Customs EDI; Cargo2000 | DG/NOTOC, customs, bonded | Customs compliance suite (ABI/ACE) |
| Multi-party messaging | Electronic messaging to network | Cargo IMP/AHM/ULD messages; iPartner APIs | Automated messaging | Carrier connections |
| Mail | Not evidenced | Dedicated UPU mail module | Airmail handling (per Lufthansa case study via IBS) | Not evidenced |

### Stable commonalities (Layer B — cross-product)

1. The shipment, identified by an air waybill number, is the central managed record in every sampled product (forwarder-side: MAWB on the job; carrier-side: AWB/HAWB; GHA-side: shipments moving through import/export/transit processes).
2. Scheduled flights are the transport resource; every product binds shipments to flights (booking, transportation plan, outbound bookings, schedules).
3. The carriage is tracked as a lifecycle of status events exchanged between parties (booking confirmed → tendered → departed → arrived → delivered; pre-advices, delays, estimate changes).
4. Rating/charging against the shipment exists in every sampled product (rate tables by lane/airline/commodity; up-front rating; handling accounting; invoicing).
5. Multi-party electronic messaging is structural (Cargo IMP family, ULD messages, e-AWB exchange, APIs to marketplaces/forwarders).
6. Compliance is embedded in the flow: dangerous goods (DGR/NOTOC), security screening, customs linkage.

### Canonical inference (Layer C)

The Type can be modeled as: **air-freight shipments (under air waybills) + flight capacity allocation + a tracked airport-to-airport carriage lifecycle + charge computation, operated across an inter-organizational chain (airline ↔ handler ↔ forwarder ↔ customs) through standardized status messaging.** The operator side (commercial seller vs physical handler vs buying forwarder) determines which slice of this model the product emphasizes, not the model itself.

## Abstraction Levels

### L0 — Defining Invariant

Minimal structure without which the product stops being recognizable as Air Cargo Management:

1. **Air-freight shipment as central record, identified by an air waybill** — the standardized document that is simultaneously the contract of carriage, the operational identifier, and the accounting basis (MAWB; HAWB layered on top when a forwarder consolidates).
2. **Allocation of shipments onto scheduled flights** — aircraft capacity (weight/volume) as the transport resource being booked, planned, and consumed.
3. **Tracked airport-to-airport carriage lifecycle** — acceptance at origin → uplift → arrival → release for delivery, with recorded status events.

Historical check: mainframe-era airline cargo systems (the ones iCargo's customers replaced) already centered on booking, AWB, rating, ULDs, and manifests; regional and all-cargo carriers fit the same triple. The AWB predates computerization as the industry's document. e-AWB and ONE Record change the medium, not the invariant. Passes.

### L1 — Common Mature Structure

Present in essentially all mature products; not required for recognition:

- Rating & charging (rate application on the shipment's measured characteristics; invoicing; on the carrier side revenue accounting and interline settlement)
- Terminal/warehouse handling control (acceptance, screening, build-up, storage, breakdown; mobile scanning; process steering)
- ULD management (stock, movement, loan/borrow, demurrage) on carrier/handler side
- Status messaging with partners (Cargo IMP family today; ONE Record emerging) and pre-advices/exceptions
- Track & trace surfaces (internal + customer-facing)
- Security screening and dangerous-goods compliance workflows
- Capacity management tooling (forecasts, allotments, load optimization) on the carrier side
- Customer/sales portals (quotes, booking requests, self-service tracking)
- Workflow/task engines with exception handling

### L2 — Variant / Optional Structure

- Operator-side emphasis: airline commercial suite vs GHA terminal system vs forwarder air module
- Mail handling (UPU standards, mailbag-level tracking)
- Dynamic pricing / revenue-management optimization (carrier-side advanced)
- Hub/transit management with auto-prioritization (transit-heavy terminals)
- Special products: pharma cold chain, perishables, live animals, DG-heavy flows
- Landside/trucking and slot booking integration
- Customs EDI depth (varies by jurisdiction)
- Deployment: SaaS vs licensed/self-hosted; multi-airport/multi-airline tenancy
- Interline partnership tooling (carrier-to-carrier)

### L3 — Vendor-specific (kept out of the final document)

- iCargo module names (CTO, CRA/MRA, iPartner…), "Core Group of Influencers" governance
- Hermes HMS/CMS naming, ecosystem partners (Nallian, e-CARGOWARE, DGM)
- CargoWise AirlineConnect / CargoTracker / Neo branding; named airline API list
- Magaya extension names (Air Tracking, ACEbridge…)
- Marketing metrics (36 customers, 36,000 shipments daily, 8M tonnes processed, 91 disparate systems, etc.)

## Vendor-specific Findings

- CargoWise: direct airline API connections for eBooking and live capacity (named carriers); map-based live flight tracking with split-cargo handling; workflow templates per trade lane/client.
- iCargo: dedicated UPU-compliant mail module with mailbag tracking; ULD demurrage calculation; IATA SIS-compliant interline settlement; dedicated RM engine "built specifically for air cargo."
- Hermes: HMS configuration of the same CMS for hub operations; auto-prioritization against outbound bookings and product SLAs; slot booking and landside modules in the ecosystem.
- Magaya: air freight as a mode inside a general forwarding platform; ACE/ABI customs compliance emphasis (US).

## Boundary Findings

- **vs Freight Forwarding System**: the forwarder's air module shares shipment/AWB/booking/tracking objects, but the forwarder system's center of gravity is the customer order across all modes + customs + warehouse + accounting (Magaya's own positioning: "shipping, transportation management, warehouse operations, tracking, connectivity, accounting"). Air Cargo Management centers on the air carriage itself: capacity, flights, terminal handling, AWB lifecycle. Test: remove flight capacity and terminal/airline-side handling → what remains is a Freight Forwarding System. Remove the multi-mode customer-order layer → what remains is Air Cargo Management. The forwarder air module is therefore an overlap zone, documented as a variant/adjacent, not a reason to merge Types.
- **vs Ocean Freight Management**: same structural pattern (shipment + booking + carriage lifecycle + charges) but different objects: vessel/container/BL vs flight/ULD/AWB; different terminal model. Sibling Type, not the same.
- **vs Airline Reservation / PSS**: passenger systems manage persons/itineraries/tickets; cargo systems manage goods/AWBs; capacity is seats vs weight/volume. Distinct Types even when one vendor sells both.
- **vs Airline Operations Platform**: flight ops (dispatch, crew, fuel) operates the aircraft; the cargo system consumes flight schedules and contributes payload/weight data. Cargo is a customer of ops, not part of it.
- **vs Ground Handling Management**: that Type centers on passenger/ramp handling services; cargo terminal handling systems (Hermes) are the air-cargo-specific slice and are treated here as a variant of Air Cargo Management (they manage the same AWB/ULD objects and flight bindings).
- **vs Parcel/Courier Management**: integrators run door-to-door single-piece networks with their own aircraft/vehicles and piece-level scans; air cargo management is airport-to-airport, consignment-based, multi-party, and does not own the door-to-door legs.
- **vs TMS**: TMS plans/executes ground transportation for shippers; no AWB, no flight capacity, no terminal handling.
- **vs Shipment Visibility Platform**: visibility products observe; Air Cargo Management is the operational system of record that produces the events.
- **vs Port Terminal Operating System**: ocean-terminal analog of the GHA cargo terminal slice; different mode objects.

## Uncertainties

1. Carrier-side operational depth (exact booking→allocation→load-control workflow steps, offload handling) rests on one deep product source (iCargo) plus industry standards; CHAMP — the other major carrier-side vendor — was unreachable. Assertions kept at conceptual level.
2. Whether rating belongs in the defining core is a judgment call: it is present in all four sampled products and central to the carrier-side commercial cycle, but a handling-focused system without charging would still be recognizable; rating was placed in the common-mature layer with an explicit note.
3. Exact status-code vocabularies (Cargo IMP/FSU message names) were not fetched from a primary standard document; only their existence and family naming are asserted (iCargo page names "Cargo IMP, AHM and ULD related messages").
4. Forwarder-side ULD/terminal behavior was not evidenced (forwarders generally don't operate terminals); not asserted.
5. The directory leaf's intended scope (carrier-only vs whole air cargo chain) is ambiguous; resolved here by centering the Type on the carrier/handler operational core and treating the forwarder air module as an overlap variant. Flagged for taxonomy awareness, no directory change proposed.

## Final Synthesis

Air Cargo Management is the operational application family for the air freight carriage chain. Its world is built from: shipments identified by air waybills, scheduled flights with weight/volume capacity, terminal handling processes at both airports, ULDs as the physical grouping unit, status events exchanged between the airline, the ground handler, the forwarder and customs, and a commercial layer that rates and charges the carriage. The airline side sells and manages capacity (reservation, rating, allotments, revenue management, revenue accounting); the handler side executes the physical flow (acceptance, screening, build-up, storage, breakdown, handover, DG/NOTOC, handling charges); the forwarder side buys capacity and consolidates (its general system belongs to Freight Forwarding System, with the air module overlapping this Type). The defining core is the shipment-under-AWB + flight-capacity allocation + tracked airport-to-airport lifecycle triple; everything else — rating, ULD control, terminal control, messaging standards, portals, RM, mail — is mature common structure or variant scope.
