# Research Notes — Parking Management Platform

Slug: parking-management-platform
Research date: 2026-09-09
Methodology: v1.1 (update-v1/)
Directory leaf: §18 Transportation, Mobility & Logistics — "Parking Management Platform"

## Research Goal

Understand what an operator-side Parking Management Platform is as an Application Type: its core objects (parking inventory, stays/permissions, rates, payments, enforcement), its defining workflows (admission, fee computation, permit administration, compliance), who uses it, which interfaces it presents, which rules and states matter, and where its boundary lies against neighboring Types — above all the §18 sibling Parking Application (driver-side), plus EV Charging Network Management, Building Access & Visitor Management, Space/Workplace Management, Yard Management System, Marina Management, and Self-storage Management.

## Initial Boundary

Initial hypothesis (pre-research):

- Core use: a parking operator (municipal, commercial garage, airport, campus, hospital, workplace, event venue) holds its parking capacity as a managed, priced resource and administers vehicle access, stays, permits, payments, and compliance from an operator-facing system.
- Users: parking operators/managers, admin staff, enforcement officers, cashiers; drivers as a connected but secondary audience (via apps/portals).
- Nearest neighbors: Parking Application (driver-side find/park/pay), EV Charging Network Management, Building Access & Visitor Management (people vs vehicles), Space Management Platform (desks/rooms vs parking), Yard Management System (trailer yards), Marina Management (berths), Self-storage Management.
- Unknowns: whether enforcement/citations are definitional or a municipal/campus variant; whether gated access control is definitional or only the off-street realization (on-street has no gates); whether occupancy sensing is definitional; how the driver app vs operator platform split works in market practice.

## Research Questions

1. What objects make up the parking world (facility/lot/zone/space/bay, gates/lanes, equipment)?
2. What is the unit of work — stay/session/permit — and what is its lifecycle?
3. How is admission decided (barrier, LPR, ticket, permit, app) and how does this differ on-street vs off-street?
4. How are rates configured and fees computed (transient vs monthly, time-tiered, zone-based)?
5. What payment surfaces exist (pay stations, mobile, pay-on-foot, pay-by-plate, validations)?
6. What is enforcement, who performs it, and is it definitional?
7. How is occupancy tracked (sensors, cameras, counters, permit inventory)?
8. What interfaces exist (operator back office, enforcement handheld, driver portal/app, kiosk)?
9. What variants exist (on-street/off-street/valet; municipal/commercial/campus/airport/healthcare/events)?
10. Where is the boundary vs Parking Application and other neighbors?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

1. **T2 Systems** (T2 Flex / UPsafety / Logan PARCS) — permit- and enforcement-centric; universities, municipalities, private operators, airports, healthcare (North America). Vendor now part of Verra Mobility.
2. **Flash (FlashParking)** — off-street commercial platform (garages, surface lots, valet); access + revenue + demand network + business intelligence (North America).
3. **SKIDATA** — European access & revenue control (hardware + software) across airport/city/retail/office/education/healthcare/hospitality/stadia segments.
4. **Flowbird** — municipal on-street/off-street payments and terminals (Europe/US); now part of Arrive (EasyPark Group).

Considered and rejected/blocked:
- **Passport (Passport Labs)** — major municipal pay-by-phone/permits/enforcement vendor; passportinc.com returned HTTP 403 on both attempts; abandoned per network rules. Sourcing limitation recorded.
- **Genetec AutoVu** — LPR-enforcement-centric pole; two guessed official URLs returned 404; abandoned. LPR enforcement is instead evidenced through T2's LPR/enforcement pages.

## Sources

All fetched 2026-09-09 (Tier 1/2 official surfaces):

- T2 Systems — root https://www.t2systems.com/ ; Permit Management https://www.t2systems.com/parking-permit-management/ ; Enforcement https://www.t2systems.com/parking-enforcement-software/ ; PARCS https://www.t2systems.com/parcs-parking-access/
- Flash — root https://www.flashparking.com/ ; Knowledge Base home https://help.flashos.com/support/home ; Monthly Billing category https://help.flashos.com/support/solutions/60000333833
- SKIDATA — root https://www.skidata.com/ ; Access Control & LPR https://www.skidata.com/solutions/mobility-parking/access-control-lpr
- Flowbird — root https://www.flowbird.group/ (flowbird.com) ; On-Street https://www.flowbird.com/our-solutions/parking-solutions/on-street/
- Passport — https://www.passportinc.com/ and /products/ — HTTP 403 ×2, abandoned (limitation)
- Genetec AutoVu — https://www.genetec.com/solutions/unified-security/autovu and /solutions/autovu — HTTP 404 ×2, abandoned (limitation)

Evidence layers: **A** = directly observed on the named product's official page; **B** = cross-product commonality across the sample.

## Product Observations

### T2 Systems (A)

Positioning: "All-in-One Parking Management System for Total Operational Control" for universities, municipalities, private operators, corporate campuses, hospitals, airports. Solutions list: Enforcement Management, Permit Management, PARCS, LPR, Pay Stations, Mobile Payments, Citation Services. Two platforms: T2 Flex (universities/large municipalities, "most configurable") and UPsafety (small/mid-size operations, cloud-first).

Permit management (A):
- Digital permits tied to license plates ("no decals to print or mail"); self-service portal for applications, renewals, account management.
- "Flexible rules & eligibility by user type, location, time, and price."
- "Real-time inventory and waitlists to prevent oversubscription."
- Online payments & invoicing with recurring billing and refunds; reporting/exports for audits, budgeting, demand planning.
- Compatible with LPR and access systems to automate validation.
- Flow: Apply & Verify → Pay & Assign (payment captured, permit issued digitally, plate instantly authorized) → Access & Validate (access systems and/or LPR recognize valid plates) → Renew & Optimize (reminders, self-service renewals, analytics).
- Vertical fits: universities (student/faculty-staff/commuter/resident permits with academic calendars); municipalities (residential/business permits, guest passes, seasonal programs); private operators (contracts, monthly parkers, tenant allocations, corporate accounts, tiered pricing, validations, renewals, invoicing, real-time inventory across garages and surface lots); airports (employee/tenant permits, zone-based access); healthcare (employee shifts, contractor credentials, patient/visitor options).
- FAQ: mixed physical-decal + digital programs during transition; renewal windows, automated reminders, waitlists with auto-notifications when inventory becomes available.

Enforcement (A):
- Mobile enforcement: officers search plates, validate permits, issue citations "in seconds — online or offline"; citations via Bluetooth printers or all-in-one devices with customizable violation codes and fee schedules.
- Digital tire chalking ("virtual chalk"): time-stamped scans to track overstay violations, reduce disputes.
- Evidence: multiple photos, notes, GPS breadcrumbs per citation; "audit-ready records."
- Scofflaw alerts: flag boot-eligible vehicles or tow candidates from hotlists; supervisors manage boot/tow eligibility criteria; flagged plate read → officer alert with history and guidance.
- Offline-first: work without connection, sync when back online.
- Device insights: officer GPS locations, route review, ticketing-behavior analysis, heatmaps/plots.
- LPR/ALPR enforcement: mobile (vehicle-mounted) or fixed cameras; "capture plates and match them against paid parking, active permits, and scofflaw hotlists"; officers get "enforce/no-enforce" guidance with evidence and location context; plate-based enforcement eliminates paper hangtags; automated enforcement: violation → owner lookup (DMV integrations, owner lookup services) → mailed citations.
- Citation issuance & management: templates, violation schedules, fee tiers mirroring ordinance/policy; time/GPS/weather/photos auto-attach; supervisor review queues, void/waive permissions, audit logs; status tracked "from issuance through payment, appeal, or collections in a single system."
- Citation payments & collections: online/mobile/kiosk/in-person payment channels; automated reminders, late fees, escalation paths; collections workflows/export; public portal to look up citations, pay, submit appeals with evidence, track status.
- Reporting: citation volume, payment rates, capture rate, appeal outcomes, route coverage, officer productivity; hot zones, repeat violators; compliance/revenue trends.
- FAQ: integrates with meters and pay-by-plate platforms so officers see "up-to-the-minute compliance data."

PARCS (A):
- "Parking access and revenue control system"; T2 Flex software + T2 Logan PARCS hardware (gated solutions; airports, healthcare, municipalities, property management, universities).
- "Complete control over who is parking in your facilities"; "wide array of revenue control options"; "hassle-free and configurable validations"; "remote management of every aspect of your facilities."
- Logan: configurable access credentials, ticket processing, payment methods; full offline functionality.
- FlexPort: patron portal — purchase permits, update personal information, renew online; "extend validations to external organizations, such as local businesses and merchants."
- Fixed LPR: "automatically link license plates for both access and transient transactions and calculate parking fees based on the license plate"; "prevents both access and revenue fraud, addresses lost ticket and switched ticket scenarios."
- FlexVal Mobile: mobile validation; third parties self-manage validation requests; browser-based, deployable as self-service kiosk or at help desks.
- SecurePay: PCI P2PE card-data security layer for Logan hardware.
- PARCS Pay-on-Phone: parkers scan QR code, settle "as if they paid at a physical pay-on-foot."

### Flash (A)

Positioning: "Mobility infrastructure for every parking asset"; connects asset owners, operators, and drivers through "cloud-native software, purpose-built hardware, and demand channels." Assets: garages, surface lots, valet; sectors: venues & events, commercial real estate, airport, healthcare, higher education, municipalities, new build.

Driver loop (A): Find (AI recommendations) → Reserve (reservations in apps/ticket platforms/vehicle interfaces via demand network) → Park (access "through AI-powered cameras") → Charge (EV charging alongside parking) → Pay (preferred payment method) → Repeat (opt-in "drive in, drive out and pay" — Express Pay).

Knowledge base structure (A):
- **FlashPARCS** — gated equipment: "hardware guides, configuration steps, and common issues."
- **Parkonect** — ungated readers: "reader setup, account configuration, and troubleshooting."
- **Digital Solutions** — ungated: "drive in, register, and drive out, never having to register again."
- **Express Pay** — "digital payment solution that uses license plate recognition (LPR) to automate parking transactions. Powered by the ParkWhiz platform and supported by both Flash PARCS and Parkonect; enables contactless entry, seamless payments, and faster exits." Enroll once through ParkMobile or ParkWhiz; "No tickets. No kiosk."
- **Valet** — "touchless check-in, ticketless transactions, and contactless payments"; customers text to request their car.
- **Flash Vision and LPR** — "AI-based computer vision technologies designed to simplify modern parking access, revenue control, and remote management."
- **EV Charging** — chargers as part of the location's offer.
- **Monthly Billing** — "Give parkers their own self-service portal to manage their parking account and easily request spaces to purchase. With the FLASH Monthly AR Module, you can automate applications, billing, and reporting, allowing you to eliminate accounts receivable." Articles: AR account profiles, advanced settings, recurring invoices, pending requests, active accounts, manage parkers, bulk parker import, late payment management, payment adjustments, dashboard, one-time invoices, manual payments/credits, invoice overview, **rate code management**, **charge types**, add accounts/users, **Monthly Pools**, billing accounts.
- **Flash Admin Portal** — user accounts; validations/coupons processed "via Validation Portal"; receipt search/generator.

### SKIDATA (A)

Positioning: "Smart access. Genuine welcome." — access solutions for parking & mobility (and mountain/stadia). Segments: airport, city & municipality, parking operator, retail & shopping mall, office, education, healthcare, hospitality, stadia, theme parks, leisure, concerts. Claims "6+ billion parking access transactions per year."

Parking & Mobility solution set (A):
- Efficient in Operations: Access Control & LPR; Monitoring & Control; Reporting & Analytics; Parking Guidance & Digital Signage.
- Successful in Selling: Online Reservations & Subscriptions; B2B Parker Management; Digital & Onsite Payment; Validation; EV-Charging.
- City Solutions: Zone Management; Curb Management; Mobility Hub.

Access control & LPR page (A):
- "Develop your standard ticket-based system into a fast & convenient LPR-based system, also a combination of LPR and tickets possible."
- Ticketless operation: smartphone for access and payment; "no need to stop to pull a ticket, no lost tickets."
- "Or go completely barrier-less and easy Pay-Per-Use for subscribers and Pay-Later for unregistered parkers."
- "Very secure and reliable for operators: no ticket fraud, less or no ticket costs, low operational effort."
- Combine plate-based access with classic tickets, or RFID cards "for employees, tenants, or other contract parkers."
- "Manage access to buildings or restricted areas the same way: dedicate access rights based on employee cards, mobile phone, or license plate number."
- Centralized multi-site operation (testimonial): "manage more than 40 car parks in Belgium with only six people."

### Flowbird (A)

Positioning: urban mobility — parking solutions (On-Street, Off-Street, EV Charging, Mobile, Open platform for parking and e-mobility, Parking business services) plus transport fare collection. Now part of Arrive (EasyPark Group). Municipal case studies: Las Vegas (pay stations + mobile), New York (ParkNYC app; pay-by-plate pay stations), Warsaw (paid parking zones, 10-year contract), Bratislava (500 pay-and-display meters), Beverly Hills (garage → on-street expansion), SEPTA commuter parking.

On-street page (A):
- Parking terminals/kiosks (Strada line): coin/contact/contactless card/banknote/barcode payment; solar or mains powered; ADA-compliant variants; SMS/Email/QR receipts.
- "Centralized management: enhanced communication systems allow for remote, centralized management, simplifying maintenance and maximizing terminal uptime."
- Upgrade kits to modernize existing terminals.
- Access S5 kiosk: "Controls garage access, internal relay" — the off-street edge of the terminal line.

## Cross-product Comparison

| Structure | T2 | Flash | SKIDATA | Flowbird | Evidence |
|---|---|---|---|---|---|
| Parking inventory as managed, capacity-bearing space (facilities/lots/zones; spaces where managed at finer grain) | ✓ (facilities, lots, zones; real-time permit inventory + waitlists) | ✓ (garages, surface lots, valet locations; monthly pools) | ✓ (car parks, zones, restricted areas) | ✓ (on-street zones, off-street garages) | A, 4/4 |
| Stay/permission record (transient stay or standing permit/subscription, identified by ticket/plate/credential, time-bounded) | ✓ (permits, transient transactions, paid sessions) | ✓ (transient tickets, Express Pay sessions, monthly accounts) | ✓ (tickets, subscriptions, Pay-Per-Use/Pay-Later) | ✓ (meter sessions, pay-by-plate, pay & display) | A, 4/4 |
| Operator-configured rates/rules applied to stays; fee computation + payment collection | ✓ (fee schedules, pay stations, mobile pay, invoicing) | ✓ (rate codes, charge types, Express Pay, validations) | ✓ (digital & onsite payment; dynamic pricing in mountain segment) | ✓ (meters, mobile, pay-by-plate) | A, 4/4 |
| Gated access control (barriers/lanes/readers) | ✓ (Logan PARCS, Fixed LPR) | ✓ (FlashPARCS, Vision cameras) | ✓ (barriers, gates, LPR) | partial (Access S5 "controls garage access"); on-street has no gates | A, 3/4 + partial |
| Enforcement/citations (violations, evidence, appeals, collections) | ✓ (core: citations, chalking, scofflaw, boot/tow, LPR enforce/no-enforce) | not on fetched surfaces (LPR used for access/revenue) | not on fetched surfaces | not on fetched surfaces | A, 1/4 |
| Permit/subscription administration (eligibility, waitlists, renewals, recurring billing) | ✓ (core) | ✓ (Monthly AR, monthly pools, pending requests) | ✓ (subscriptions, B2B parker management) | limited on fetched surfaces | A, 3/4 |
| Occupancy tracking / guidance | ✓ (real-time inventory; device/route analytics) | ✓ (Vision; BI) | ✓ (Monitoring & Control; Guidance & Digital Signage) | ✓ ("real-time availability") | A, 4/4 (form varies) |
| Validations (third-party/merchant) | ✓ (FlexVal, FlexPort external validations) | ✓ (Validation Portal, coupons) | ✓ (Validation solution) | not on fetched surfaces | A, 3/4 |
| Driver-facing self-service (portal/app: buy, pay, extend, receipts) | ✓ (FlexPort, MobilePay, Pay-on-Phone) | ✓ (ParkWhiz/ParkMobile, Express Pay enrollment) | ✓ (smartphone ticketless, online reservations) | ✓ (ParkNYC app, pay-by-text) | A, 4/4 |
| Reservations / pre-booking | not on fetched surfaces | ✓ (Demand Network) | ✓ (Online Reservations) | not on fetched surfaces | A, 2/4 |
| EV charging | not on fetched surfaces | ✓ | ✓ | ✓ | A, 3/4 |
| Reporting & analytics | ✓ | ✓ (Business Intelligence) | ✓ | ✓ (business services) | A, 4/4 |
| Multi-facility centralized management | ✓ ("add an unlimited number of facilities and lanes") | ✓ (17K+ locations claim) | ✓ (40+ car parks / 6 people testimonial) | ✓ (remote centralized terminal management) | A, 4/4 |

Key comparative findings:

1. **Three structures are jointly present in all four products** (A, 4/4): (1) parking held as managed, capacity-bearing space; (2) the vehicle's stay/permission as an identified, time-bounded record; (3) operator-configured rates/rules applied to stays with fee computation and payment collection. This is the candidate defining core.
2. **Gated access control is NOT definitional** (A, 3/4 + partial): the on-street pole (Flowbird) has no gates — the street cannot be gated; admission control there is realized as paid sessions/permits checked after the fact. Gated machinery is the off-street realization of the same underlying control.
3. **Enforcement/citations is NOT definitional** (A, 1/4): core for T2's campus/municipal posture, but absent from the fetched surfaces of Flash, SKIDATA, and Flowbird. It is the compliance leg of municipal/campus variants, not the Type's invariant.
4. **The plate is the emerging identity substrate** (A, 4/4): T2 digital permits "tied to license plates," Flash Express Pay "uses LPR," SKIDATA LPR-based access, Flowbird pay-by-plate. But ticket/RFID/app credentials coexist in all — plate is dominant-modern, not definitional (historical ticket-based operations satisfy the core without it).
5. **The driver-facing surface is a channel into the operator platform, not the platform** (A, 4/4): portals/apps write sessions/permits into the operator's system of record. The standalone driver app is the sibling Type (Parking Application).
6. **Validations are a distinct revenue-control mechanism** (A, 3/4): third parties (merchants, employers) partially or fully settle stays — present in T2, Flash, SKIDATA.
7. **Multi-facility centralized operation is standard-mature** (A, 4/4): every product sells centralized remote management across many locations.

## Canonical Model

### L0 — Defining Invariant (minimal)

The Parking Management Platform is the parking operator's system of record and control surface for parking as a managed, priced, capacity-bearing resource. Three jointly-held structures:

1. **The parking inventory of record** — parking held as managed, capacity-bearing space: facilities/lots/zones (and, where the operation manages at finer grain, individual spaces/bays), carrying capacity, rules, and rates. Remove → a payment terminal or access-control panel with no managed space; a bare occupancy counter.

2. **The parking stay/permission as the unit of record** — a vehicle's bounded right to occupy the inventory: a transient stay (opened at entry/issuance, closed at exit/payment) or a standing permission (permit/subscription valid for a period), identified by ticket/plate/credential, carrying time bounds and state. Remove → anonymous barrier actuation or an occupancy sensor feed; the operation loses its paper trail.

3. **The operator's revenue-control loop over stays** — the operator configures rates and rules (by facility/zone/user type/time), the system applies them to stays: computing fees, collecting and reconciling payments (transient, recurring/permit billing, validations), and deciding/verifying admission against the right held. Remove → a driver-side app (Parking Application territory) or a bare payment kiosk; the operator posture is gone.

Jointly-held is load-bearing:
- 1 alone = a space registry / parking-guidance system.
- 2 without 1 = a ticketing/payment flow with no managed space (driver-app or toll territory).
- 3 without 1+2 = a payment terminal / POS.
- 1+2 without 3 = occupancy tracking/guidance — sensing without revenue control.
- 1+3 without 2 = rates with nothing to apply them to.
- 2+3 without 1 = pay-by-phone app or permit billing detached from any managed inventory.

### L1 — Common Mature Structure

Very common in mature modern products; not required to recognize the Type:

- **Access-control machinery** (gates, barriers, entry/exit lanes, readers, kiosks) — the off-street realization of admission control.
- **LPR/plate recognition** as the dominant modern identity substrate (alongside tickets, RFID cards, apps).
- **Occupancy tracking** (sensors, cameras, counters; space-level where managed) and **guidance/signage**.
- **Permit/subscription administration** at depth: eligibility rules, waitlists, renewal windows, recurring billing, self-service portals.
- **Validations** (merchant/employer validation of stays, coupons).
- **Driver-facing self-service channel** (portal/app: purchase, pay, extend, receipts) — a channel into the platform.
- **Pay stations / kiosks / meters** as unattended payment surfaces (pay-on-foot, pay-and-display, pay-by-plate).
- **Reporting & analytics** (occupancy, revenue, utilization, enforcement metrics).
- **Multi-facility centralized management** (remote monitoring and control of many locations).
- **Enforcement/citations** (violations, evidence, appeals, collections) — dominant in municipal/campus variants; the compliance realization of the same control loop.
- **Reservations/pre-booking** and demand channels.
- **EV charging** integration as an amenity/revenue line.

### L2 — Variant / Optional Structure

Depends on segment, geography, deployment, business model:

- **Physical setting**: on-street (zones, meters, no gates) vs off-street (garages/lots, gates) vs valet vs curb/zone management vs mobility hubs.
- **Customer**: municipality vs commercial operator vs property owner/REIT vs campus/university vs airport vs healthcare vs events/venues.
- **Admission posture**: gated vs gateless/barrierless vs ungated (drive-in-register-drive-out).
- **Compliance depth**: none (pure revenue control) ↔ patrol/LPR enforcement with citations, appeals, scofflaw/boot/tow, collections.
- **Pricing sophistication**: flat/hourly tiers ↔ dynamic pricing/yield management.
- **Demand generation**: none ↔ marketplace/demand-network channels feeding the platform.
- **Hardware posture**: hardware-inclusive (vendor gates/terminals) vs software-only/hardware-agnostic vs camera-first.
- **Credential mix**: tickets, plates, RFID cards, smartphones, QR codes.
- **Deployment**: cloud-hosted vs on-premises server + offline-capable lane hardware.

### L3 — Vendor-specific Structure (Research Notes only)

- T2: Flex vs UPsafety two-platform split; Logan PARCS hardware line; FlexPort patron portal; FlexVal/FlexVal Mobile validations; SecurePay (PCI P2PE); PARCS Pay-on-Phone QR flow; "125 customers / 2,000+ PARCS lanes" claim; Verra Mobility parentage; Citation Collection Services (full-service collections team).
- Flash: FlashPARCS vs Parkonect product lines; Express Pay (powered by ParkWhiz; enroll via ParkMobile/ParkWhiz); Flash Vision (AI computer vision); Monthly Pools; Flash Admin Portal; Demand Network ("450M+ driver touchpoints", "17K+ locations", "1.5B+ transactions"); Waze partnership (30K locations); valet text-for-car; Denver airport "144 lanes in 22 days" claim.
- SKIDATA: SKIDATA Connect platform; sMove gates/mobile kit; Power.Gate; "6+ billion parking access transactions per year"; Pay-Per-Use (subscribers) / Pay-Later (unregistered) naming; mountain-destination and stadia adjacency (ski passes, event ticketing on the same access infrastructure); B+B "40 car parks / 6 people" testimonial; ASSA ABLOY parentage.
- Flowbird: Strada terminal family (EVOL/TPAL/S5/Compact/Access); ParkNYC, Monapass case studies; Park&Gaz fuel adjacency; transport fare collection (ABT, open payment, MaaS) as a sibling line; EasyPark Group/Arrive ownership.

## Vendor-specific Findings

See L3 above. Notable philosophy poles within the sample:

- **Permit/enforcement-first** (T2): the operation is defined by who may park and who complies; revenue control (PARCS) is an extension of the permit platform.
- **Access/revenue-control-first** (SKIDATA, Flash): the operation is defined by the entry/exit transaction and the money it captures; permits are "monthly" products inside the revenue system; enforcement is not the center.
- **Municipal-payments-first** (Flowbird): the operation is defined by payment capture at the curb and in garages, with terminals as the physical edge; enforcement not evidenced on fetched surfaces.
- **Demand-network-led** (Flash, distinctively): the platform actively routes drivers to assets (reservations, marketplace channels) — a growth layer on top of the same core.

## Boundary Findings

1. **vs Parking Application (§18 sibling, driver-side)** — sharpest seam. The driver app's world is find/park/pay from the driver's seat (search, availability, session start/stop, payment); the management platform's world is the operator's inventory, stays, rates, and revenue. They interlock: driver-app sessions/permits are records inside the operator platform (Flash Express Pay "powered by the ParkWhiz platform"; Flowbird's ParkNYC app feeds the city's program; T2 MobilePay "empowering you to own your customer relationship"). Remove the operator posture (inventory of record + revenue-control loop) and only a driver app remains → Parking Application.
2. **vs EV Charging Network Management (§19)** — charging platforms' unit of record is the energy-delivery session priced per kWh/time; parking platforms' unit is the stay priced per duration/flat. All three sampled products that mention EV treat chargers as an amenity/revenue line inside parking (Flash "Charge" step; SKIDATA EV-Charging; Flowbird EV Charging) — adjacent capability, not the core. Remove stays/rates over parking and keep charging sessions → EV Charging territory.
3. **vs Building Access & Visitor Management (§17)** — people through doors vs vehicles into parking. SKIDATA explicitly extends parking credentials to building/restricted-area access ("dedicate access rights based on employee cards, mobile phone, or license plate number") — evidence of adjacency via shared credential infrastructure, but the object of record differs (vehicle stay vs person entry). Remove vehicles/stays and keep people/doors → Building Access territory.
4. **vs Yard Management System (§10, processed)** — YMS's unit is the trailer/container moving between yard places and dock doors under directed yard-driver work, with no third-party driver revenue loop; parking's unit is the third-party driver's stay priced by the operator. Both model spaces + bounded unit presence, but the revenue-control loop over anonymous drivers is parking's, not YMS's.
5. **vs Space Management Platform / Workplace Management (§10/§17, processed)** — those passes held parking as one resource class inside workplace platforms (desks/rooms/parking bookable inventory). The standalone parking platform is vehicle-stay-and-revenue-centric, operates at lot/zone/space grain with gates/meters/enforcement, and serves parking operators rather than workplace teams. Remove the vehicle/stay/revenue semantics and keep bookable-space allocation → Space/Workplace territory.
6. **vs Marina Management (§18)** — berths are long-term space rentals (lease-like, vessel as resident); parking stays are short-turnover occupancy by anonymous drivers (transient) with permits as the long-term pole. Permit-heavy commercial parking approaches the marina shape at its long-tenure edge.
7. **vs Self-storage Management (§17)** — space rental with custody handoff and tenant identity; no vehicle turnover, no admission metering. Different unit of work.
8. **vs Tolling / road pricing (not a directory leaf here)** — per-passage charges on a route vs bounded occupancy of a space; a barrierless LPR garage is structurally close to tolling at its entry/exit poles but the stay (not the passage) is the record.

**"Remove what to become the other Type" judgments:**
- Remove the operator-side inventory + revenue-control loop → Parking Application (driver-side).
- Remove parking stays/rates, keep energy sessions → EV Charging Network Management.
- Remove vehicles, keep people/doors → Building Access & Visitor Management.
- Remove the third-party-driver revenue loop, keep trailer moves/docks → Yard Management System.
- Remove vehicle-stay semantics, keep bookable-space allocation for employees → Space/Workplace Management.

## Historical / Market-Sample Check (§24)

Would older, regional, platform-native products still fit the L0?

- **1950s–60s attended lot**: attendant issues paper ticket at entry, rate card on the booth wall, cash collected at exit, monthly parkers in a permit ledger, occupancy chalked on a board. Satisfies all three legs (inventory = the lot; stay = the ticket; revenue loop = rate card + cash + permit ledger). No digital, no LPR, no apps. ✓
- **Pay-and-display municipal scheme (paper era)**: driver buys a ticket from a mechanical meter, displays it on the dash; zones defined by signage; patrol checks compliance. Satisfies: inventory = zones; stay/permission = the displayed ticket (time-bounded right); revenue loop = meter tariffs + coin collection. No gates. ✓
- **Ticket-and-barrier garage (1970s–80s PARCS)**: machine-issued ticket, fee computed by duration, cashier/automatic pay station, gate release. Satisfies all three legs; no plate identity, no cloud. ✓
- **Modern gateless/camera-first operations** (Flash Digital Solutions, SKIDATA barrierless): no ticket, plate-as-identity, pay after or by account. Satisfies all three legs (stay = plate-identified session). ✓

The L0 therefore does not depend on gates, plates, apps, sensors, or cloud — only on managed capacity, the bounded stay/permission record, and the operator's revenue-control loop. Anti-overfit holds: LPR (4/4 in-sample) is held as dominant-modern implementation, not invariant, because the historical ticket-based poles satisfy the core without it.

## Uncertainties

1. **Passport unreachable** (HTTP 403 ×2): a major municipal pay-by-phone/permits/enforcement vendor is not directly evidenced. The municipal payments leg rests on Flowbird + T2 instead. Assertion strength for the municipal pole is calibrated accordingly.
2. **Genetec AutoVu unreachable** (404 ×2): the LPR-enforcement-centric security-platform pole is not directly evidenced; LPR enforcement rests on T2's pages.
3. **Enforcement absence in Flash/SKIDATA/Flowbird** is "not evidenced on fetched surfaces," not confirmed absence — these vendors may offer enforcement via partners or unlisted modules. The claim is kept at evidence strength.
4. **Fee-free parking administration** (e.g., workplace parking allocation with no charges): not sampled this pass. Whether such a pole belongs inside this Type or in Workplace/Space Management is recorded as a boundary uncertainty; the L0's revenue-control leg is asserted from 4/4 sampled products + historical paid-parking practice, not tested against a free-parking platform.
5. **Rate-engine precision** (grace periods, tier boundaries, per-minute vs per-hour rounding): deliberately not stated; not researched to precision on any fetched surface.
6. **Reservations depth** (T2, Flowbird): not evidenced on fetched surfaces; held as common-mature from Flash/SKIDATA only.

## Final Synthesis

A Parking Management Platform is the parking operator's system of record and control surface for parking as a managed, priced, capacity-bearing resource. Its defining core is three jointly-held structures: the parking inventory of record (facilities/lots/zones, spaces where managed at finer grain); the parking stay/permission as the unit of record (a bounded, identified right to occupy — transient stay or standing permit); and the operator's revenue-control loop (rates/rules configured operator-side, applied to stays: admission decided or verified, fees computed, payments collected and reconciled).

Around that core, mature products add: gated access machinery and LPR (off-street), meters/terminals and pay-by-plate (on-street), occupancy sensing and guidance, permit administration at depth (eligibility, waitlists, recurring billing), validations, driver-facing self-service channels, multi-facility centralized management, reporting/analytics, reservations, and EV charging. Enforcement/citations is the compliance realization of the same control loop, dominant in municipal/campus variants rather than definitional. The dominant modern identity substrate is the license plate, with tickets, RFID cards, and apps coexisting — held as implementation, not invariant, because ticket-era and paper-era operations satisfy the core without it.

The Type's sharpest boundary is with the driver-side Parking Application: the platform is the operator's world (inventory, stays, revenue); the app is the driver's window onto it. Secondary boundaries: EV charging (energy sessions vs parking stays), building access (people vs vehicles), yard management (trailer operations vs driver revenue), workplace space management (bookable-space allocation vs vehicle-stay revenue control).
