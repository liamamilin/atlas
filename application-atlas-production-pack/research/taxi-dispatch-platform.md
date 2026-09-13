# Research Notes — Taxi Dispatch Platform

Research date: 2026-09-10
Slug: taxi-dispatch-platform (DIRECTORY §18 Transportation, Mobility & Logistics)

## Research Goal

Understand what a Taxi Dispatch Platform actually is as an Application Type: the operator-side software a taxi (and private-hire / livery) company runs its dispatch operation on. Produce a vendor-neutral Application Document explaining the core structure, the dispatch workflow, the interfaces, the rules that matter, and the boundaries against neighboring Types — especially Ride-hailing Platform (which held a "keep-both" flag against this leaf from its own pass) and Dispatch Management (which explicitly carved taxi out as its own leaf).

## Initial Boundary (hypothesis before research)

- Hypothesis: operator-side system of record for a taxi fleet's dispatch operation — bookings in, live driver/vehicle availability, allocation, job lifecycle, fare/settlement.
- Nearest neighbors: Ride-hailing Platform (passenger-side marketplace), Dispatch Management (generic), Computer-aided Dispatch (emergency), Courier Management (goods), Towing Dispatch (recovery), Fleet Management System (vehicle health), NEMT / School / Employee transportation (closed-population scheduled transport), Public Transit (scheduled routes).
- Key pre-hung flags to discharge:
  - ride-hailing-platform pass (2026-09-09): "keep-both held vs taxi-dispatch-platform (passenger-created request + marketplace fare record vs operator-side fleet dispatch; taxi-as-supply-class inside ride-hailing = supply mix not Type change)".
  - dispatch-management pass (2026-09-07): "industry work semantics (freight/delivery/service — taxi/towing/courier specialized as their own leaves)".
  - non-emergency-medical-transportation-platform pass (2026-09-09): "remove → anonymous ride booking = ride-hailing/taxi territory" (NEMT vs taxi seam).

## Research Questions

1. What objects exist in the system (booking/job, driver, vehicle, zone, shift, tariff, account, passenger)?
2. How does a booking enter, and what is its lifecycle?
3. How is driver/vehicle availability represented and maintained (shifts, zone queues, book-in)?
4. How does allocation happen (manual, assisted, automatic; nearest / ETA / FIFO / broadcast-bid)?
5. What are the dispatcher's working surfaces?
6. What does the driver see and do?
7. What passenger-facing channels exist and how do they relate to the operator?
8. What taxi-specific rules matter (tariffs, zones, licensing, meter, overbooking)?
9. How is money handled (fare capture, payment channels, driver settlement, accounts)?
10. What variants exist (fleet scale, service mix, prebook vs on-demand, networks, chauffeur pole)?
11. Historical check: would radio-dispatch / MDT-era operations still satisfy the definition?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer levels and geographies:

| Product | Pole | Geography | Evidence tier reached |
|---|---|---|---|
| iCabbi (Coolnagour Ltd, ex-Autocab) | enterprise taxi + private-hire platform, inter-fleet networking | UK/IE/global (14 countries) | Tier 2 product pages + FAQ (help center is login-walled Zendesk) |
| TaxiCaller (TaxiCaller Nordic AB) | self-serve cloud dispatch for SME fleets, multi-service | Sweden/global | Tier 2 product pages + Tier 1 knowledge-base articles |
| Limo Anywhere | chauffeur / livery / black-car pole (reservation-centric) | US/global (5,400+ operators claimed) | Tier 2 product pages + Tier 1 knowledge-base articles |
| Curb Fleet Systems (Way2Cloud / e-Fleet / Call Center / Optima) | US taxi-fleet systems, meter+payments heritage, outsourced call center, demand network | US | Tier 2 product pages only |

Rejected/abandoned samples:
- T Dispatch — domain parked for sale (product defunct/moved); abandoned.
- Cordic — www.cordicgroup.com transport error ×2; abandoned.
- Cab9 — cab9.uk empty response, www.cab9.uk transport error; abandoned.
- G7 — www.g7.fr HTTP 403; abandoned.

## Sources

Official (fetched 2026-09-10):
- iCabbi — https://icabbi.com/ ; https://icabbi.com/platform/dispatch/
- TaxiCaller — https://www.taxicaller.com/ ; /en/features/dispatch-system ; /en/features/driver-app ; knowledge base https://www.taxicaller.com/en/help/ ; KB articles /en/help/kb/741220 ("How does Automatic assignment work (assign to)?") and /en/help/kb/579405 ("What booking channels does your system include?")
- Limo Anywhere — https://www.limoanywhere.com/ ; /dispatch-software/ ; knowledge center https://kb.limoanywhere.com/ ; /docs-category/dispatch/ ; /docs/new-dispatch-grid/
- Curb — https://www.gocurb.com/ ; /fleet/dispatch-management/

Historical / industry (Tier 3, used only for structure-existence claims):
- "Taxi – Dispatching" overview (primidi.com) — callbox → 1950s radio dispatch → zone pegboard → MDT computer dispatch.
- Don McCurdy, "Taxi Dispatch Technology" (taxi-library.org) — MDT dispatch types, zone book-in validation (DDS "Book in Validation", Raywood "Restricted Plotting"), "Soon to Clear".
- Gandalf MDCP brochure (sigidwiki.com PDF) — Anaheim Yellow Cab fully computerized dispatch (call-taker terminals + dispatch computer + MDTs; auto-dispatch of standard fares, timed calls, regular runs, priority calls).
- The Independent (1994-12-12), "Taxis on the super highway" — Computer Cab London: 1974 paper dockets + voice radio → 1982 VDU computer-aided dispatch → 1989 in-cab computers + card swipe → 1995 GPS auto-dispatch; advance bookings reactivated before pickup time.
- TaxiPoint (2024), "ComCab's Journey" — 1974 manual paper dockets + voice radio dispatch; 1980s VDU computer-aided dispatch; 1995 GPS auto dispatch.
- TaxiCom '95 (FTA report, drivingresearch.com) — European adoption of computer dispatch, mobile data transmission, fleet management software.

## Product Observations

### iCabbi (evidence layer A unless noted)

Positioning: "fully-integrated taxi dispatch platform" for taxi companies; per-driver SaaS licensing; markets include UK, IE, US, CA, AU, NZ, Nordics, NL, BE, ES, PT. Suite: Dispatch, Move AI (NEMT route optimization), Driver App ("Drive"), Driver Docs (driver onboarding/records), Driver Pay (driver payouts/wallet), Passenger App, Voice (iVR phone booking), Voice AI, Business Solution (corporate accounts), The Exchange (inter-fleet network).

Dispatch page observations:
- "highly-configurable… translate your expert local knowledge into rules that help you intelligently match supply and demand"; handles "simplest trips from A to B, to recurring bookings, to complex bookings with multiple pickups and drop-offs".
- Flexible Dispatch Rules: "configure your system to dispatch your bookings in many different ways… schedule these dispatch rules for different times of the day".
- Zone Profiling: separate Zones each with own Dispatch Rules; profiles scheduled day/time (e.g. stadium during a concert) or manually invoked.
- Dispatch by Fleet (Sites): multiple fleets inside one system dispatching separately; Site Profiles share uncovered bookings across fleets during busy periods. Bureaus: connect separate fleets' instances (growth by acquisition).
- Overbooking Protection: monitors driver availability in real time; if capacity falls below a configurable threshold the system can hold new bookings, redirect them to partner fleets via Dispatch Networking, or alert the dispatch team.
- Networking: partner with other taxi companies to form a "super fleet" (supply-side sharing); The Exchange: send bookings you cannot service to other fleets, accept inbound bookings; app roaming network for passenger apps.
- Dispatch by ETA: real-time traffic-aware ETA (Google Fleet Engine) selects fastest driver; pure on-demand mode or "customisable driver wait time loaders to layer in a queue consideration".
- Fixed Rates & Tariffs: price models by distance, time in car, council-regulated time changes, public holidays, fixed-fare journeys (airport runs), zone surcharges (clean-air/congestion), discount codes.
- Corporate Account Management: portal for business-account users, travel rules, invoicing, reporting.
- Payments: in-car, SMS, multi-provider pre/post-paid card processing. Billing: business-account and driver invoicing.
- Driver Records: profiles, license, insurance, police record/PVG disclosure, performance booking statistics. Vehicle Records: license/plate expiry, inspections, council compliance, vehicle attributes (wheelchair accessible, people carrier, VIP), CO2.
- Staff Records & user management with access levels. Passenger Records & "Traffic Light": priority status for good customers (VIP queue jumping), flag undesirable passengers to prevent booking.
- Hooks: event-triggered tasks/communications (e.g. thank-you SMS after trip completion). Enhanced Flight Tracker in Driver App for airport jobs.
- FAQ: allocation based on proximity, real-time ETA, driver availability, vehicle type, zone rules, and shift constraints; configurable to prioritise speed, fairness, earnings equity, or zone coverage; advance bookings up to 7 days; multi-stop; recurring; account bookings with custom billing rules; driver app offline capability; Data Suite 290+ reporting parameters; 1,000+ real-time configuration options (vendor claim).

### TaxiCaller (evidence layer A)

Positioning: "flexible, cloud-based dispatch platform for taxi and passenger transportation companies"; solutions: Taxi, School-Run, Paratransit (NEMT), Shuttle, Corporate, Special-needs student transportation. Pay per vehicle per month; separate Owner and Dispatcher logins.

Dispatch console page:
- Real-time vehicle tracking; Caller ID + VoIP integration (SIP) — booking form autopopulates with caller's details; auto-complete addresses; "Check" gives time & price estimates before booking.
- Live map with vehicle status; text and voice messages to drivers ("fast feedback with no noisy radio").
- Zone queues: "see who's been waiting the longest in certain zones… for fair assignment".
- Job tabs: Unassigned, Assigned, Active — "follow the status of every job"; Jobs Overview chronological + searchable; multi-monitor; job alerts & alarm; corporate accounts.
- FAQ: auto-assignment "can use a 'closest car' scheme, or you can utilize a zone and queue system where there's a FIFO scheme (First In - First Out), or you can have the jobs broadcasted to all or certain vehicles for drivers to bid on them". Multiple dispatchers simultaneously; dispatcher login can be IP-restricted; continuous communication with driver device, location updates when signal returns.

Driver app page:
- Start shift ("set up shifts and schedules so that drivers can't work overtime"); job offers ("receive jobs straight to your phone or tablet with no need to radio dispatch"); job details (directions, estimated time, distance, price); in-app taximeter (choose tariffs, time & distance); payments (split payments, extra charges, e-signature for account customers); chat & voice messages; zone queues (drivers see activity in zones); driver documents (licenses, permits uploaded in app); automatic accounting (set charge rate, track driver transactions); alarm; broadcast bidding; shift history; driver can act as dispatcher from Android app (create/assign jobs).

Knowledge base (Tier 1):
- "How does Automatic assignment work (assign to)?" — "The system can automatically choose the most suitable vehicle and offer the job to it… determined by two criteria (closest vehicle or zone queue selection) depending on what has been chosen in the dispatch settings."
- "What booking channels does your system include?" — four channels: Dispatch console (calling a dispatcher), Passenger App booking, Web booking tool, Reception booking tool (corporate bookings).

### Limo Anywhere (evidence layer A)

Positioning: "livery software… booking, scheduling, dispatch, and reservation management" for limousine/black-car operators; plans Core/Plus/Black; LA Pay payments; LA Network affiliate network ("become the preferred supplier for other Limo Anywhere customers in your home market").

Dispatch software page:
- Reservation Management: "create, edit, and dispatch your reservations, and accept/reject online and eFarm-in trips".
- Dispatch Management: "customize your dispatch grid… schedule and assign trips, mass text your drivers, and track flights in real-time".
- Customer & Account Management (preferences); Accounting, Billing & Driver Payroll ("manage customer invoices, process credit card payments, and track payroll disbursements"); mobile apps; "Track Progress Of Trips… make sure that your trips are assigned and dispatched and drivers are properly servicing your customers".
- Roles: drivers (real-time trip details, alerts), support/ops (centralized trip management, notifications, visibility), management (reservations, driver activity, payments, performance).

Knowledge base — New Dispatch Grid (Tier 1):
- List View (row-based grid of trips) + Map View (trips plotted at pickup locations).
- Trip row / details panel: Conf#, Status, PU Date, PU Time, DO Time, Trip Type; account info, trip routing, pickup date/time, vehicle capacity and type, grand total, "current status of the reservation (Unassigned)", type of trip (in-house), car assigned to the trip, and the driver.
- Attention Flags: red exclamation on trips with special requirements — "Meet & Greet, child seat, or missing flight number".
- Filters (Column / Operator / Value: Status, Vehicle Type, PU Date…); Batch Edit panel for multiple trips; Quick Edit + Detailed Edit via double-click; auto-updates on the grid; integrated mapping; calendar.

### Curb Fleet Systems (evidence layer A, product-page tier)

Positioning: Curb is a US taxi technology company (rider app + driver app + fleet systems). Fleet Systems: Payments, Digital Meter ("Weights and Measures-Approved Taxi Meter Tables and BYOD Solutions"), Curb One ("all-in-one driver app with a built-in meter, payments, trip offers, and management tools — no hardware"), Dispatch & Management, eFleet Access.

Dispatch & Management page:
- "cloud-based taxi and NEMT dispatch software… scheduling, routing, dispatching, and billing".
- Way2Cloud: "cloud-based taxi dispatch and fleet management system. A highly customizable, feature-rich dispatch platform built to manage taxi and NEMT operations of any size"; "Need to dispatch trips to customers from the office? We give you all the controls you need to run your business."
- e-Fleet: "centralized web portal for fleet data management, administration, compliance documentation, and operations".
- Call Center: "Three-tier call center coverage: automation, live agents, and dispatcher. Fleets and health plans pay only for what each call needs." (outsourced call handling as a product option)
- Curb Optima: AI-powered route optimization engine (partnership-built).
- Customer testimonials (fleet presidents): fleets run dispatch operations on Way2Cloud + Curb Call Center; Curb Flow feeds additional demand ("receiving Curb Flow trips… new revenue opportunities for our drivers"); Pair & Pay improves passenger experience.
- Rider app side: Ride Now / Ride Later (advance booking), Pair & Pay (pay in-cab metered ride through app).

## Cross-product Comparison

| Dimension | iCabbi | TaxiCaller | Limo Anywhere | Curb Fleet Systems |
|---|---|---|---|---|
| Unit of work | booking (A-to-B, multi-stop, recurring, advance) | job (unassigned/assigned/active) | reservation/trip (Conf#, PU/DO, trip type) | trip (dispatched from office) |
| Who creates the work record | operator channels (call/app/web/account/partner) | dispatcher console, passenger app, web tool, reception tool | operator + online reservation system + passenger app | office dispatch + call center + Curb Flow feed |
| Availability model | driver availability + shift constraints + zones | shifts/schedules + zone queues (book-in/waiting) | scheduled grid + chauffeur assignment | fleet availability (details not public) |
| Allocation | configurable rules: proximity, ETA (traffic-aware), vehicle type, zone rules, shift constraints; scheduled profiles | manual, or auto: closest car / zone-queue FIFO / broadcast-bid | manual assign on dispatch grid (schedule + assign) | office dispatch controls (details not public) |
| Live picture | dispatch engine + map (Google Fleet Engine) | map + vehicle status + job tabs + zone queues | dispatch grid list + map view + attention flags | dispatch console (screenshots) |
| Driver surface | Driver App (jobs, flight info, offline) | Driver App (shift start, offers, meter, payments, docs, chat) | Driver App (trip details, GPS tracking) | Curb One driver app (built-in meter, trip offers) |
| Pricing | tariffs: distance/time/council-regulated/holiday/fixed-fare/zone surcharges/discounts | in-app taximeter tariffs; Check estimates | rates engine (16 KB articles), quotes | digital meter tables (Weights & Measures), payments |
| Money | in-car/SMS/pre-post-paid cards; business + driver billing; Driver Pay | split payments, e-signature for accounts, driver accounting | invoices, card processing, driver payroll | payments platform, Pair & Pay |
| Accounts | Business Solution portal (users, travel rules, invoicing) | corporate accounts + reception booking tool | accounts with preferences, receivables | health plans / NEMT payers (call center) |
| Fleet records | driver records (license/insurance/disclosure), vehicle records (plates/compliance/attributes) | driver documents in app | driver management (12 KB articles) | e-Fleet compliance documentation |
| Networks | The Exchange (dispatch networking + app roaming) | — | LA Network (affiliate work exchange) | Curb Flow (demand feed into fleets) |
| Service mix | taxi + private hire + NEMT (Move AI) | taxi + school-run + paratransit + shuttle + corporate | limo/livery/black car | taxi + NEMT |
| Commercial model | per-driver SaaS | per-vehicle/month | plan tiers (Core/Plus/Black) | fleet systems + payments + call-center services |

Cross-product commonalities (evidence layer B):
- The booking/job/reservation is the universal unit of work; every product names it differently.
- Unassigned → assigned is the central managed transition (TaxiCaller tabs; Limo Anywhere "Unassigned" status; iCabbi dispatch queue).
- Availability is organized by time (shifts/schedules) and space (zones/queues) in the taxi-specific products.
- Allocation spans the same spectrum: manual assignment ↔ rule-based auto (closest/ETA/FIFO) ↔ broadcast/bid.
- Multi-channel intake with the dispatch console as the phone channel (caller ID integration in two products).
- Driver app as the field surface; messaging replaces radio ("no noisy radio" — TaxiCaller; radio heritage in historical sources).
- Fare machinery is intrinsic: tariffs/meter/quotes + payment capture + driver settlement in all four.
- Driver/vehicle records with compliance documents in all four.
- Inter-fleet work exchange appears in three of four (iCabbi Exchange, LA Network, Curb Flow) — demand aggregation is a common modern layer, not definitional.

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

The taxi operator's real-time allocation of fare-bearing passenger transport jobs to its own fleet of licensed driver-and-vehicle units, consuming a continuously maintained availability state, with each job tracked from capture through completion into the operator's commercial record.

Four jointly-held structures:

1. **Operator-side dispatch over the operator's own fleet** — jobs enter through operator-managed channels; operator staff (or operator-configured automation) allocate them; the supply is the operator's own fleet. Remove → ride-hailing marketplace (passenger creates the request; platform aggregates supply) or a lead-referral directory.
2. **The fare-bearing passenger transport job** — the unit of work is a passenger ride carrying pickup/destination and its pricing basis (tariff, fixed quote, or meter). Remove passenger semantics → courier/towing dispatch; remove the fare basis → generic dispatch management.
3. **Continuously maintained fleet availability** — drivers+vehicles held as dispatchable capacity organized by shift and zone/queue posting; allocation consumes and updates this state. Remove → job board or reservation-only booking system.
4. **Tracked job lifecycle closing into the commercial record** — capture → allocate → perform → complete/terminal exception, with fare, payment, and driver settlement recorded. Remove → pure tracking/telematics, or dispatch theater with no record.

Jointly-held load-bearing analysis:
- 1 alone = fleet/company registry; 2 alone = tariff table/fare calculator; 3 alone = shift roster; 4 alone = trip log.
- 1+2 without 3+4 = booking intake with no operation (lead referral).
- 1+3 without 2 = generic dispatch management (any work, no fare semantics).
- 2+4 without 1+3 = accounting shell over trips.
- 1+2+3 without 4 = allocation with no commercial record.
- 2+3+4 without 1 = marketplace-side dispatch (ride-hailing territory).

Historical check (§24): radio-era dispatch satisfies the core without any modern machinery — callbox/phone bookings taken at a dispatch office; dispatcher assigns by zone board (magnetic pegs on an engraved zone map) or voice; drivers "book into" zones and report position by radio; paper dockets record jobs and fares; drivers call back with payment amounts for accounts and commission. MDT-era (1980s–90s) adds call-taker terminals, auto-dispatch of standard/timed/priority calls, GPS zone book-in validation, in-cab card swipe — still the same four structures. Therefore GPS, apps, cloud, auto-allocation algorithms, and payment platforms are NOT definitional.

### L1 — Common Mature Structure (standard capabilities)

- Multi-channel booking intake: call-taking console with caller ID/VoIP, passenger app, web booking widget, corporate account portal, partner/API feeds.
- Allocation assistance/automation: closest-car, traffic-aware ETA, zone-queue FIFO, broadcast/bid; configurable rule sets; time-scheduled dispatch profiles.
- Live operational picture: map with real-time vehicle positions + job board (unassigned/assigned/active) + zone queues.
- Driver app: job offers/acceptance, navigation, status progression, messaging, in-app meter/tariff selection, document access.
- Pricing machinery: tariff tables, fixed rates, surcharges (holiday/zone), quotes/estimates.
- Payment capture + driver settlement: in-car card, app pay, account invoicing; driver accounting/commission/payouts.
- Driver & vehicle records: licenses, insurance, disclosures, plate/inspection compliance, vehicle attributes (wheelchair-accessible, executive).
- Corporate account management: users, travel rules, invoicing, reporting.
- Passenger records: history, preferences, flags/prioritization.
- Exception machinery: cancellation, no-show, reassignment, overbooking protection, overflow routing.
- Reporting/analytics; passenger notifications and tracking links; flight tracking for airport work.

### L2 — Variant / Optional Structure

- Service mix: taxi / private-hire / executive-chauffeur (reservation-centric pole) / NEMT-paratransit / school-run / shuttle / corporate shuttles.
- Demand posture: on-demand-dominant vs prebook-dominant (chauffeur pole runs a scheduled dispatch grid over future reservations).
- Scale & structure: single fleet vs multi-site/bureau (multiple fleets, shared overflow) vs inter-fleet network/exchange.
- Call handling: own dispatch office vs outsourced call center vs IVR/voice-AI automation.
- Meter posture: hardware meter integration vs in-app meter vs BYOD.
- Regulatory regime: council-regulated tariffs and licensing (UK-style) vs market-rate livery (US-style).
- Demand aggregation: none vs e-hail network feeds vs inter-fleet exchange vs app roaming.
- Deployment: cloud SaaS vs legacy on-prem MDT/radio systems (still the same Type).

### L3 — Vendor-specific (kept out of the final document)

- iCabbi: Google Fleet Engine dispatch, The Exchange, Move AI, Voice AI, Traffic Light passenger status, Sites/Bureaus, "1,000+ configurations" and "99.999% uptime" claims, per-driver licensing.
- TaxiCaller: SIP softphone/caller-ID integration, broadcast bidding, dispatcher IP restriction, per-vehicle pricing, driver-as-dispatcher Android mode.
- Limo Anywhere: eFarm-in trips, LA Network, ORES, Attention Flags, LA Pay, Lead Quote Close, plan tiers.
- Curb: Way2Cloud, e-Fleet, Curb Flow, Pair & Pay, Curb One, Optima, three-tier call center, Weights & Measures meter tables.

## Vendor-specific Findings

See L3 above. Also: iCabbi's "advance bookings up to 7 days" and "290+ reporting parameters" are vendor-specific numbers (product-page claims) — not generalized. TaxiCaller's four named booking channels are product-specific enumeration; the conceptual set (operator console / passenger self-serve / web / account portal) is the cross-product finding.

## Boundary Findings

1. **vs Ride-hailing Platform** — keep-both DISCHARGED from this side (flag was held by the ride-hailing pass). Structural test: who creates the work record, and whose supply is allocated. Taxi dispatch: the job record is created through operator-managed channels and allocated to the operator's own fleet under the operator's tariff rules; the platform is the fleet operation's system of record. Ride-hailing: the passenger creates the request in a marketplace; the platform matches across an aggregated supply pool under platform pricing rules. Overlap zones and why they don't collapse the boundary: (a) operator passenger apps are the operator's own demand channel — the record still lands in the operator's dispatch system; (b) inter-fleet exchanges and e-hail demand feeds (iCabbi Exchange, Curb Flow) are demand-aggregation variants layered on an operator-side core; (c) ride-hailing platforms listing licensed taxi supply is supply mix inside the marketplace, not a dispatch system. Remove the operator-side posture (passenger creates the request in a shared marketplace) → ride-hailing.
2. **vs Dispatch Management** — keep-both DISCHARGED. The generic leaf holds the four-structure dispatch spine (work queue + resource availability + assignment act + live picture); taxi dispatch shares that spine but is bound to passenger-transport job semantics with intrinsic fare machinery, licensed driver+vehicle pairing, shift/zone availability culture, and regulated tariffs. The dispatch-management pass explicitly named taxi as its own specialized leaf. Remove the taxi work semantics + fare machinery → generic dispatch management.
3. **vs Computer-aided Dispatch (CAD)** — different work unit (emergency incident vs commercial ride), different governing rules (response priorities/agency status codes vs tariffs/fairness/shifts), different users (public-safety telecommunicators vs taxi dispatchers). Shared ancestry (dispatch board + unit status + assignment) but no collapse.
4. **vs Courier Management Platform** — goods pickup→delivery with proof-of-delivery vs passenger transport with pickup/dropoff; both have customer-account rate engines (structural similarity), but the work unit, execution surface, and settlement shape differ.
5. **vs NEMT Platform** — the NEMT leaf centers on scheduled medical transport with passenger needs/eligibility context and payer/broker settlement. Taxi dispatch products carry NEMT/paratransit as a service-mix variant (iCabbi Move AI, TaxiCaller Paratransit, Curb NEMT dispatch). Boundary: eligibility-bound scheduled program transport vs general public on-demand/prebook demand. Consistent with the NEMT pass's own note ("remove → anonymous ride booking = ride-hailing/taxi territory").
6. **vs Fleet Management System** — FMS centers on the vehicle register + in-service record + oversight; its pass classified dispatch as L1. Taxi dispatch centers on job allocation; vehicle records are supporting data. Remove job allocation → fleet management.
7. **vs Towing Dispatch Platform** — same dispatch spine, different work semantics (vehicle recovery). Leaf not yet processed; no definition asserted here.
8. **vs scheduled transport Types (Public Transit, School, Employee, Shuttle)** — scheduled route/run plans vs job-based on-demand/prebook allocation. TaxiCaller's school-run/shuttle solutions are variant poles; the school-transportation and employee-transportation passes hold their own closed-population/route-plan cores.
9. **Chauffeur/livery pole** — Limo Anywhere is reservation-centric (quotes, scheduled dispatch grid, payroll) but remains operator-side fleet dispatch of fare-bearing jobs → variant within this Type, not a separate Type (no separate directory leaf exists).

## Uncertainties

- iCabbi's help center is login-walled (Zendesk); operational depth for iCabbi rests on product pages + FAQ. No iCabbi state vocabularies or numeric limits are asserted in the final document.
- Exact job-state vocabularies are not standardized across the industry; only TaxiCaller (Unassigned/Assigned/Active tabs) and Limo Anywhere ("Unassigned" reservation status) were directly observed. Final document keeps states conceptual.
- Curb Way2Cloud's allocation mechanics are not publicly documented at article level; Curb evidence is product-page tier only.
- Driver settlement mechanics (commission vs lease vs payout) observed as capabilities but not researched to numeric depth — no numbers asserted.
- Historical sources are Tier 3 (encyclopedic/trade press); used only to establish that the core structure predates modern machinery, not for precise dates beyond what the sources state.
- Towing Dispatch Platform leaf unprocessed — boundary described structurally, not against its eventual definition.

## Final Synthesis

A Taxi Dispatch Platform is the taxi operator's side of the passenger-transport market: the operational system of record that turns a stream of fare-bearing ride bookings into allocations against a live fleet of licensed driver-and-vehicle units, tracks each job to completion, and closes it into the operator's commercial records (payment + driver settlement). Its defining core is small and predates computing: bookings, availability, allocation, tracked completion with fare records. Everything modern — apps, GPS maps, auto-allocation, caller ID, payment platforms, inter-fleet networks — is mature structure layered on that core. The Type is distinct from ride-hailing (operator-side vs marketplace-side), from generic dispatch management (taxi work semantics + fare machinery), and from the scheduled/closed-population transport Types (open public demand, job-based allocation).
