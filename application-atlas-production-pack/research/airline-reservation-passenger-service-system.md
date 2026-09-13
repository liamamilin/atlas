# Research Notes — Airline Reservation / Passenger Service System

Research date: 2026-09-06

## Research Goal

Understand what an Airline Reservation / Passenger Service System (industry term: PSS) really is, from real products: what objects exist inside it (flight inventory, passenger reservations, fares, tickets/orders, boarding passes), who operates it (airline reservations agents, airport staff, revenue teams, and consumers via direct channels), how a seat is sold from schedule to boarding, and where its boundary lies against the flight search/booking platform (consumer side), the airline operations platform (operational side), revenue management (optimization side), air cargo (freight analog), and hotel reservation systems (structural analog in hospitality).

## Initial Boundary

- Hypothesis going in: this Type is the airline's passenger-side commercial system of record. It holds the airline's flights as sellable seat inventory, records bookings, converts them into ticketed/passenger orders, and processes passengers through check-in and boarding on the day of travel.
- The directory leaf merges two historical industry names: "airline reservation system" (ARS/CRS lineage) and "Passenger Service System" (PSS). In current industry usage, a PSS is understood as an integrated suite of reservations + departure control (documented directly in a vendor case study below). Working assumption: one Type, with the reservation/commercial spine as the defining core and departure control as the standard second half.
- Adjacent Types flagged from the start: Flight Search / Booking Platform (consumer-side), Airline Operations Platform / Airline Crew Management (airline operational side, already documented as sibling leaves), Airline Revenue Management (inventory/pricing optimization), Air Cargo Management (freight analog), Hotel CRS / PMS (hospitality analog).

## Research Questions

1. What are the core objects? (flight/inventory, booking/PNR, fare, ticket/order, seat, ancillary, boarding pass)
2. How does selling work? Where does availability come from and how is it controlled?
3. How does a booking become a confirmed right to travel? What enforces the transition?
4. How do the day-of-travel processes (check-in, boarding, bags, irregularities) relate to the reservation record?
5. Which channels sell the inventory, and how do external parties (GDS, agencies, partner airlines, handling agents) connect?
6. What roles operate the system, and what permissions matter?
7. What happens when reality diverges (no-show, go-show, no-record passengers, cancellations, denied boarding, delays)?
8. Where are the boundaries: consumer booking platforms, airline ops, revenue management, cargo, hotels?

## Representative Products

Sample selection intent: market representativeness + different product philosophies + different customer tiers. Reachability constrained the final sample (see Sources).

| Product | Vendor | Tier / philosophy | Status |
|---|---|---|---|
| iFly RES | IBS Software | Cloud-native PSS for modern airline retailing (NDC / One Order); LCC and hybrid carriers prominent in the customer list | Researched (official product pages + case study) |
| VRS | Videcom | Traditional IATA-compliance-first reservation system + integrated DCS; hosted dedicated instances for smaller carriers | Researched (official product pages, unusually detailed) |
| Altéa PSS | Amadeus | Largest enterprise hosted-PSS family | Unreachable (site bot-blocked) |
| Sabre PSS (SabreSonic lineage) | Sabre | Enterprise hosted PSS from GDS lineage | Unreachable (site bot-blocked / 404) |
| Radixx | Radixx/Sabre | LCC-focused PSS | Unreachable (transport errors) |
| Crane PSS | Hitit | Regional/mid-tier PSS | Unreachable (wrong domains; real site not reachable) |
| Accelya FLX ONE / AccelAero lineage | Accelya | Airline retailing (offer/order), NDC distribution, financial/settlement | Rejected sample: current catalog shows retailing + financial products, not an integrated reservations+DCS suite; used only as industry-structure corroboration |

## Sources

- IBS Software — Airline Passenger Solutions overview: https://www.ibsplc.com/product/airline-passenger-solutions (fetched 2026-09-06)
- IBS Software — iFly (RES) product page: https://www.ibsplc.com/product/airline-passenger-solutions/ifly (fetched 2026-09-06)
- IBS Software — Fly Gangwon PSS migration case study: https://www.ibsplc.com/case-studies/airline-passenger-solutions/opening-new-skies-for-fly-gangwon-with-an-agile-pss-migration (fetched 2026-09-06)
- Videcom — Airline Systems Overview: https://www.videcom.com/airline-system.aspx (fetched 2026-09-06)
- Videcom — Ticket Time Limits: https://www.videcom.com/airline-ticket-time-limits.aspx (fetched 2026-09-06)
- Videcom — Departure Control System: https://www.videcom.com/airline-departure-control-system.aspx (fetched 2026-09-06)
- Videcom — home / module index: https://www.videcom.com/ (fetched 2026-09-06)
- Accelya — product catalog (industry-structure reference only): https://www.accelya.com/ (fetched 2026-09-06)
- Amadeus — https://www.amadeus.com/en/portfolio/airlines — BLOCKED (bot wall)
- Sabre — https://www.sabre.com/products/air-solutions/ (404), https://www.sabre.com/airlines/ (404), https://www.sabre.com/ (bot wall)
- Radixx — https://www.radixx.com/ — transport errors (x2)
- Hitit — https://www.hitit.co/ (wrong site), https://www.hitit.com.tr/en (404), https://www.hitit.com.tr/ (unrelated HVAC company), https://www.hititcrs.com/ (transport error)
- IATA program pages — 404 on attempted paths (x2)

Sourcing limitation: the enterprise-flagship tier (Amadeus, Sabre) could not be observed directly. Vendor help centers / user guides were not reachable for any sampled product. All claims below are calibrated accordingly; no precise operational parameters (exact time limits, exact class counts, message formats' technical detail) are asserted for the market as a whole, and Videcom's own numeric examples stay in these notes.

## Product A — iFly RES (IBS Software)

### Key observations (evidence layer A = directly observed on official pages; interpretation marked)

- A1. The vendor's own case study defines the product class: "iFly RES, an integrated reservations (RES) and departure control system (DCS) product suite." (case study, Fly Gangwon PSS migration). The same case study confirms the category consolidates: it describes airlines evaluating multiple PSS vendors after an incumbent (SITA) announced it would discontinue its PSS business.
- A2. Positioning: "omnichannel platform for airline retailing, reservations, servicing, and end-to-end passenger processing" (iFly page). Channels named: traditional GDS, interline, codeshare, and direct sales "using native and NDC APIs".
- A3. Distribution paradigms coexist: "supports traditional as well as NDC based codeshare, interlining, and GDS distribution, in a One Order or e-Ticketed fashion" — i.e., the ticket (e-ticket) and the newer "order" are alternative forms of the confirmed travel entitlement. Evidence for abstracting "commercial confirmation" beyond the e-ticket document.
- A4. Retailing layer: offer management + dynamic pricing ("infinite price points", dynamic pricing "during each pricing request"), ancillary pricing via rules engines or ML; fare families / branded fares displays in the IBE.
- A5. Departure control: "Fully integrated departure control capabilities with a shared single-seat map … real time service delivery, retailing at airport customer touch points, and advanced check-in options." Single shared seat map between reservation and DCS = strong evidence that reservation and check-in operate on one inventory/seat state.
- A6. Internet booking engine (IBE) as a distinct module: shopping, fare families, dynamic packaging, web check-in including ancillary sales, agency portal for "allocation requests and bookings", content management console for product offerings.
- A7. Tour operator allotments: a dedicated contract module manages tour-operator allotments on the same flight inventory ("integrated tour operator allotment and seat-only flight inventory record that can be optimized through a revenue management system"); case study (SunExpress) describes migrating from separate systems to "a unified seat only and tour operator allotment PSS platform". Evidence that the same flight inventory serves multiple channel-specific allocation schemes.
- A8. Inventory ↔ revenue management coupling: an external revenue management system can optimize the inventory; iFly holds and executes the inventory record. (Mirrors Videcom's nightly RM export/import, see B6.)
- A9. Inter-airline messaging: a messaging module delivering "any Type A or Type B message sets" to partners — the classic airline inter-system message families remain the connective tissue.
- A10. Staff travel: a dedicated staff/duty-travel product (iFly Staff) and corporate negotiated fares (iFly Corporate) live in the passenger-services product family — evidence that airline staff (non-revenue) travel is part of the passenger population the PSS family serves, though deliverable as a separate module.
- A11. Travel credits / digital wallet: vouchers and flight credits managed when travel plans change — the refund/credit side of servicing.
- A12. Scale markers on the page (passenger volumes, agent users connected "using GDS bypass") — marketing figures; recorded but not used for market claims.

## Product B — VRS (Videcom)

### Key observations

- B1. Scope statement: "An IATA compliant Airline Reservation System providing Inventory Hosting, IATA Eticketing, Internet Booking Engine, GDS Distribution, Codeshare and Interline connections." and "Inventory, schedule, fares and agent control modules provide a complete solution". Plus: "The standard solution provides an integrated Departure Control System … for rapid passenger check-in and real time access to reservations."
- B2. Single shared data core: "One Database. Real Time Processing. … a single database for reservations, check-in, reporting, inventory control and management functions." (central-database page summary). Same architectural claim as A5 in different vocabulary.
- B3. Channel set enumerated: direct public (IBE), mobile booking engine, direct travel agency booking engine, call center, GDS participation (named: Amadeus, Sabre, Worldspan, Galileo, Apollo, Abacus, Sirena), bilateral interline (IATA Interline E-ticket), codeshare, XML API. "All airlines need Call Centre bookings."
- B4. GDS connectivity is real-time interactive: "real time interactive availability, sales and IATA BSP Eticketing"; full "Type A & Type B reservation connectivity". GDS e-ticket (ET) and IATA Interline E-ticket (IET) with IDEC interline settlement; BSP settlement.
- B5. Ticket time limits (dedicated page — the most concrete rule documentation found in the whole sample):
  - TTL exists for "Revenue Integrity … to reduce the number of empty seats left on an aircraft due to late cancellations"; travel agents make "speculative or duplicate bookings which need to be cancelled if they are not confirmed within a predefined time limit and seats returned to inventory."
  - Three TTL kinds, mixable: (a) global default (bookings auto-cancel after N hours if unticketed); (b) variable limits based on how far ahead of departure the booking is made (the page documents one airline-configurable example ladder: bookings 90–60 days ahead expire 20 days before flight; 59–30 days → 5 days; 29–7 days → 24 hours; 6–4 days → 24 hours after booking; 3–2 days → 12 hours; 1–6 hours → 6 hours) — **product-specific example, not a market norm**; (c) manual limits by authorized supervisors (gated by user security level, with configurable expiry date/time and a target queue).
  - TTL can also be set per flight number ("flights that sell quickly … may attract a short ticketing period").
  - On expiry: held space returns to inventory and the expired booking is placed on a **queue** for agents to process.
  - Interpretation: the hold → ticket transition is *policed*, with unconfirmed demand automatically returned to sale. This is a defining economic behavior of seat selling, visible in the product as a first-class configurable rule.
- B6. Revenue management boundary: VRS provides revenue reporting for yield teams and "can also be integrated with external Revenue Management system … Data is exported nightly to your chosen provider and receives updates to inventory levels." Confirms division: RM computes inventory levels; the PSS holds and executes them.
- B7. Revenue accounting boundary: "automated transfer of sales data to your revenue accounting system", including standard "BSP HOT files". The PSS is the source of sales/ticketing data, not the ledger.
- B8. DCS detail: graphical seat map (multi-seat selection for groups), boarding passes and bag tags "in any format", IATA boarding pass / bag tag printing, through check-in, seat blocking, group check-in, excess baggage handling, cabin classes, CUTE certification, BSM (baggage source message) integration.
- B9. Passenger-state deviations handled at the airport: "No Rec Passengers" (no reservation on file) and "Go Show Passengers" (present to fly without having completed the expected pre-travel state) are named DCS features. Evidence that day-of-travel processing must absorb mismatches between the booking record and reality.
- B10. Handling-agent split: at outstations, the airline's reservation system sends IATA-standard PNLs (passenger name lists) and ADLs (additions/deletions) to a third-party airport DCS, and receives back an Electronic Ticket List (ETL), from which "used tickets" are lifted automatically for revenue accounting reconciliation. Evidence: (a) reservation and DCS can be separate systems communicating via standard messages — DCS is not definitionally inside the reservation system; (b) the ticket's lifecycle ends in a reconciliation loop (sold → used → settled).
- B11. Online check-in: configurable per departing station, with a configurable window (example: open up to 24h before flight where PNLs are sent 24h ahead), operating on the same e-ticket database so that check-in state is immediately visible to airport staff. Online boarding pass content configurable.
- B12. APIS: passport data collected (scanned at airport or entered online) and transmitted to authorities per route — government security data collection as a PSS-adjacent capability in the DCS/booking flow.
- B13. Commercial administration modules: schedules, inventory, fares engine, service fees (change/refund fees), promotional codes, ancillary sales (hotels, car hire, transfers, insurance alongside flights), payment gateways, user management (users across "sales offices, ticket offices, airport check-in"), passenger profiles, frequent-traveller module, reporting.
- B14. Access/permissions: user sign-in codes, security levels ("99 levels" — product-specific), protected functional areas, full transaction audit trail, sessions time out (20 min — product-specific).
- B15. Hosting model: the vendor hosts dedicated instances for airlines ("dozens of other airlines hosted at Videcom") — the hosted/outsourced deployment model in its small-carrier form.
- B16. Longevity marker: "Since 1972, Videcom have been integrating airline systems" — soft evidence that computerized airline reservation/distribution predates the modern web era by decades (historical check input; no precise market history asserted).

## Product C — Accelya (rejected sample, industry-structure corroboration)

- C1. Current catalog decomposes airline passenger commerce into: Offer Management, Shop and Price, Availability Calculator, Product Catalog, Stock Keeper, Order Accounting, Revenue Management, Dynamic Pricing, NDC distribution, settlement and audit products (BIDT/Sales audit), Revenue Accounting, Refund Management, Payments. No integrated reservations+DCS suite is offered today → rejected as a representative of THIS Type.
- C2. The same catalog, however, corroborates the industry's decomposition of the passenger flow (offer → order → settle → deliver) and the existence of availability/ordering/settlement as distinct concerns — used only as cross-industry confirmation of concepts already evidenced in A/B, never as the source of a claim about PSS products.

## Cross-product Comparison

| Aspect | iFly RES (IBS) | VRS (Videcom) | Reading |
|---|---|---|---|
| Core scope | reservations + inventory + retailing + integrated DCS | inventory hosting + reservations + fares + ticketing + integrated DCS | identical spine; vocabulary differs (retailing vs reservation) |
| Inventory | seat-only + tour-operator allotments on one inventory record | inventory hosting with channel/agent control; RM can set levels | flight inventory with controlled availability is the shared core |
| Commercial confirmation | e-ticket OR One Order (offer/order paradigm) | IATA e-ticket database, ET/IET, BSP settlement | ticket/order forms vary; confirmed-entitlement concept is invariant |
| Hold policing | implicit in offer/order flows | explicit ticket-time-limit engine + expiry queues | the hold→confirmed transition is policed in both; mechanism depth differs |
| Channels | direct (IBE/mobile), NDC APIs, GDS, interline, codeshare, agency portal, tour operators | direct (IBE/mobile), agency, call center, GDS, interline (IET), codeshare, XML API | multi-channel sell-through of one inventory is structural |
| Departure control | integrated DCS, shared single seat map, advanced check-in | integrated DCS at own stations OR third-party DCS via PNL/ADL; web check-in | both integrate DCS; both also acknowledge external DCS (message-based) — DCS is standard scope with a pluggable boundary |
| Day-of-travel deviations | airport retailing touch points, real-time service delivery | go-show / no-rec handling, excess baggage, through check-in | reality-vs-record mismatches are a named concern in both |
| Passenger identity | customer profiles, data-driven personalization | passenger profiles, frequent traveller module | profile/loyalty common, not defining |
| Government data | (not observed on pages) | APIS module, passport capture | region/regime-dependent — variant |
| Revenue data out | NDC/One Order native flows | BSP HOT files, ETL-based used-ticket lifting, RA exports | the PSS feeds settlement/accounting downstream in both |
| Deployment | cloud-native SaaS platform | vendor-hosted dedicated instance | hosting model is a variant, not the type |

## Abstraction Hierarchy

### L0 — Defining Invariant

Three elements. Removing any one stops the product from being recognizable as this Type:

1. **Sellable flight inventory.** The airline's own scheduled flights held as availability-controlled inventory (seats offered under controlled classes/allocations, consuming as sold, perishing at departure). Without it, the product is a shopping/booking front-end that does not hold what it sells.
2. **Passenger reservation record.** Identified passengers bound to specific flights, maintained (create, modify, cancel, service) through the pre-travel window. Without it, there are no bookings to service.
3. **Commercial commitment.** The reservation's transition from held demand to a confirmed right to travel, by applying the fare and recording payment (realized in the market as an e-ticket, an order, or the booking confirmation itself), with the unconfirmed transition actively policed (ticketing time limits returning held space to inventory). Without it, the system is an enquiry/display engine, not a selling system of record.

§24 historical check: the reservation/inventory/ticketing spine is exactly what airline reservation systems consisted of before computerized check-in existed (one sampled vendor's airline-systems lineage is documented back to 1972; reservation-without-DCS is visible today in the message-based split where a third-party airport DCS processes passengers against PNLs). Departure control is therefore *not* in L0 — it is the standard second half of a modern PSS, with an established pluggable boundary.

### L1 — Common Mature Structure

Present across the researched sample; expected in the market; not defining:

- multi-channel distribution of the one inventory: direct web/mobile (IBE), call-center/agent desktop, travel agencies via GDS, interline and codeshare partners, plus API distribution (XML/NDC)
- fares management: fare database/rules engine, fare families / branded fares, promotions, change/refund service fees
- ticketing: IATA-style e-ticket database; interline e-ticket; settlement data handoff (BSP-family exports, used-ticket reconciliation)
- seat management: seat maps shared between selling and check-in; paid/free seat selection
- ancillary retailing: bags, seats, non-air products (hotels, cars, insurance) sold alongside the flight
- departure control: airport check-in (seat assignment, bag tags, boarding passes), web/online check-in on the same record, boarding, through-check-in
- queue-based agent workflow: expiries, follow-ups, and exceptions land in queues rather than requiring polling
- passenger profiles and frequent-flyer/loyalty integration
- reporting and downstream data feeds (revenue accounting, statistics)
- group bookings and partner allotments (tour-operator contracts)
- user/office model with security levels and a transaction audit trail

### L2 — Variant / Optional Structure

- hosting/deployment model: vendor-hosted dedicated instance, cloud-native multi-tenant SaaS, (historically) airline-owned in-house platforms
- confirmation paradigm: classic e-ticket vs offer/order (NDC / One Order) retailing; the two coexist even inside one product
- fare/pricing architecture: class-availability-based published fares vs continuous/dynamic pricing and ML-priced ancillaries
- carrier segment shape: full-service network carrier (interline, codeshare, through-check, cabins) vs low-cost (direct-channel-centric, ancillary-led, little/no interline) vs hybrid/charter with tour-operator allotments
- staff/non-revenue travel handling (own family of modules in one sampled vendor)
- regional/regulatory packs: APIS/government data transmission, security-document requirements, settlement-plan regimes
- external DCS at outstations vs own integrated DCS at every station
- loyalty integrated vs third-party; travel credits/wallets depth
- baggage: tags/BSM integration depth, excess-baggage charging

### L3 — Vendor-specific Detail (research notes only)

- iFly module names: IBE, Non-air Commerce Engine, Tour Operator Contract Management, Shopping Cache, Direct Messaging, iFly Staff / iFly Corporate; "single seat map" phrasing; NDC/One Order certification claims
- Videcom specifics: "VRS" product name; TTL example ladder (90–60d → 20d before flight, etc.); "99 levels of security"; 20-minute session timeout; per-flight-number TTLs; .NET/SQL Server stack; CUTE certification claim; specific GDS name list (Amadeus, Sabre, Worldspan, Galileo, Apollo, Abacus, Sirena); ETL file name; PNL/ADL terminology
- IBS marketing metrics (passenger volumes, growth percentages) — not used

## Vendor-specific Findings

- The explicit three-kind ticket-time-limit engine (global / variable-by-booking-window / manual-supervisor) is documented only by Videcom → keep product-specific; the *existence of TTL-style policing* as a revenue-integrity mechanism is cross-product (IBS expresses it through offer/order expiry flows), but its mechanism shape must not be generalized.
- "Shared single-seat map" as an explicit architectural claim is iFly's wording; Videcom's version is "single database … reservations, check-in, inventory control". The shared-state concept generalizes; the phrasing does not.
- Tour-operator allotment management as an inventory-native feature is prominently iFly (+ SunExpress case). Not observed in Videcom's pages → present as a variant capability, not a common requirement.
- APIS/passport capture is documented only by Videcom → regional/regime variant, weakly generalized.

## Boundary Findings

- **Flight Search / Booking Platform (OTA)**: consumer-side. It searches across airlines and hands the resulting booking to the airline PSS (through GDS/API). Remove the airline's own inventory and ticketing from this Type and you have the OTA. Conversely, an OTA holds no perishable seat inventory of its own.
- **Airline Operations Platform** (documented sibling): holds the flight as an *operational* object (legs, aircraft rotations, delays) and makes delay/cancel decisions; the PSS holds the same flights as *sellable* inventory and executes the passenger consequences (rebooking, refunds). Per the sibling leaf's own text: selling seats and checking in passengers belongs to the PSS; a delay decision is made there and consumed here.
- **Airline Revenue Management**: computes what availability/allocations to offer (including overbooking posture); the PSS holds and executes the inventory and records the sales. In one sample the coupling is a nightly data exchange; in the other it is native. Remove execution/selling from RM or optimization from the PSS and the two Types separate cleanly.
- **Airline Crew Management** (documented sibling): passengers vs crew; itineraries vs rosters; fare rules vs duty-time legality.
- **Air Cargo Management** (documented sibling): freight analog — air waybill vs ticket, capacity in weight/volume vs seats, terminal handling vs check-in. The two never share a record.
- **Airport Operations Platform**: airport-side resources (stands, gates, turnarounds for *all* airlines) vs airline-side passenger processing. The PNL/ADL exchange between the airline's reservation system and third-party airport DCS shows the organizational seam: the passenger record belongs to the airline; the airport processes on a copy.
- **Hotel Central Reservation System / PMS** (hospitality analog): same shape (inventory → reservation → confirmation → check-in), different economics: rooms have length-of-stay occupancy, no fare-class availability ladder, no ticket document, no interline/codeshare semantics, no government security-data regime. Remove the airline flight semantics (perishable seat classes, tickets, interline) and this Type collapses into the hotel pattern — which is exactly why they are different Types.
- **Reserved Seating / Event Ticketing**: sells numbered seats with inventory controls, but no fare-rule-driven repricing, no multi-carrier interline, no day-of-travel document check/bag process.
- **What would dissolve the Type**: remove inventory holding (→ pure distribution/shopping platform), remove the commercial commitment (→ availability display), remove the airline flight object (→ generic booking engine), remove passenger servicing/ticketing while keeping check-in (→ a DCS capability, which the industry treats as a module of the PSS, not a separate Type; no DCS leaf exists in the directory).

## Uncertainties

1. **Enterprise-flagship tier under-observed.** Amadeus and Sabre (and Radixx, Hitit) were unreachable. Claims about the Type rest on two verified products at different tiers plus industry-structure corroboration. Anything that only enterprise hosted platforms do (e.g., large-scale interline settlement mechanics, fare-proration) is deliberately not claimed.
2. **Ticket time limit universality.** Explicitly documented by one product; implied by offer/order expiry flows in another. Treated as a common mature mechanism, with mechanism shape flagged product-specific.
3. **Exact L0 boundary of DCS.** Industry usage (one vendor's own case-study wording) defines PSS = RES + DCS; historical form shows RES without DCS. Resolved by keeping DCS out of the defining core but presenting it as the standard second half; if a future pass finds the market treats check-in as inseparable, the L0 could be revisited.
4. **Offer/order (NDC/One Order) convergence.** Documented as an available paradigm in one product and as the industry roadmap in vendor literature; the pace and end-state (ticket vs order) is uncertain — the document therefore abstracts the *commercial commitment* rather than betting on the ticket.
5. **Denied boarding / overbooking handling detail.** Overbooking is referenced in vendor literature as an industry practice; specific denied-boarding workflows were not observed and are not described.
6. **Help-center depth.** No user guides reachable; UI-level workflows (exact screen names, keystroke flows) are described conceptually only.

## Final Synthesis

The Airline Reservation / Passenger Service System is the airline's passenger-side system of record. Its defining spine is small: the airline's scheduled flights held as availability-controlled sellable inventory; named passengers bound to flights in maintainable reservation records; and the policed commercial commitment that turns held demand into a confirmed right to travel. Around that spine, mature products add multi-channel distribution (direct, agency/GDS, interline/codeshare), fares and ancillary retailing, and the day-of-travel half — check-in, bags, boarding — either integrated on the same record or connected to third-party airport systems through standard passenger-name messages, with used-ticket data flowing onward to settlement and revenue accounting. The operational control of the flights belongs to the operations platform; the optimization of what to sell belongs to revenue management; the consumer-side search and cross-airline shopping belongs to booking platforms. What remains — holding, selling, committing, and delivering the airline's own seats to its own passengers — is this Type.
