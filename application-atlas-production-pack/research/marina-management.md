# Research Notes — Marina Management

Research date: 2026-09-09
Leaf: Marina Management (§18 Transportation, Mobility & Logistics) → slug `marina-management`

## Research Goal

Understand what marina management software actually is as an Application Type: what objects exist inside it, what marina staff do with them, how berthing work flows, what states and rules matter, and where its boundary lies against neighboring Types (campground/RV park management, hotel PMS, boat/yacht charter platform, port terminal operating system, self-storage management).

## Initial Boundary (hypothesis before research)

- Hypothesis: operator-side system of record for a marina — the facility that rents berths (wet slips, moorings) and commonly dry storage to boat owners. Core guess: berth inventory + berthing agreements (long-term lease + transient dockage) + occupancy operations + billing (recurring rent, utilities, fuel, services).
- Likely confusions:
  - Campground/RV Park Management — structurally the closest analog (site inventory + reservations + stay lifecycle + billing). The campground pass itself recorded marina as an adjacent bundled property type and flagged "same shape over water".
  - Hotel PMS — reservation/stay/folio shape.
  - Boat/Yacht Charter Platform — demand-side vessel time-use; the charter pass explicitly recorded a boundary row against Marina Management.
  - Port Terminal Operating System — commercial cargo, not recreational berthing.
  - Self-storage Management — dry-stack racks resemble storage units.

## Research Questions

1. What is the core inventory object (slip/berth/mooring/dry-stack rack) and its attributes (size, location, power/water)?
2. What agreement types exist (annual/seasonal lease, transient reservation, dry storage, mooring)?
3. What is the berthing lifecycle and what occupancy states drive daily operations?
4. How does billing work (recurring rent cycles, renewals, transient fees, metered utilities, fuel, services)?
5. What vessel record is kept (dimensions, registration, insurance) and how does it constrain assignment?
6. What service/yard capabilities exist (work orders, haul-out, launch scheduling)?
7. What interfaces do staff actually work from (dock map, occupancy board, reservation calendar)?
8. What assignment/waitlist rules exist?
9. Where is the boundary against campground management, hotel PMS, charter platforms, port TOS?

## Representative Products

| Product | Position | Why sampled | Evidence layer |
|---|---|---|---|
| **DockMaster** (dockmaster.com) | Enterprise marine ERP, 40+ years, 1,000+ marinas/boatyards/dealerships; desktop+web+mobile; marina + service + inventory + boat sales + POS + accounting | Full-service-yard pole; deepest marina-module documentation | A — root + dedicated Marina Management solution page |
| **Storable Molo** (storablemarine.com, product "Molo") | Modern cloud-native marina management SaaS (Storable Marine; app at app.getmolo.com); marinas, yacht clubs, boatyards, rental fleets | Modern cloud pole; multi-location enterprise; online booking/portal | A — marine root + Molo product page + Slips/Mooring/Storage feature page |
| **Jonas Club — Marina Management** (jonasclub.com) | Marina module inside a private-club management suite; members with permanent slips + transient reservations for members | Club-marina audience pole; member-billing integration | A — dedicated marina module page (thin but direct) |

Attempted and unreachable (recorded as sourcing limitation, not silently substituted):
- **Dockwa** (dockwa.com, knowledge.dockwa.com, help.dockwa.com) — 403 / transport errors; transient-boater reservation pole not directly observed.
- **Molo standalone site** (moloapp.com) — transport errors; superseded by reachable storablemarine.com pages.
- **Harbour Assist** (harbourassist.com) — 403 ×2; UK harbour-authority pole not directly observed.
- **SNS MarinaMaster** (snsmarine.com) — timeouts ×2.
- **MarinaOffice** (marinaoffice.com) — empty responses ×2.
- **HarborMaster** (harbormaster.com) — transport error + 403.
- **MarinaCloud** (marinacloud.com) — empty ×2.
- **TotalDock** (totaldock.com) — empty ×2.
- **web.archive.org** fallback — timeouts ×2.
- **RMS Cloud** (rmscloud.com) — reachable, but its current site has no dedicated marina solution page; marina appears only as a reconfiguration (Twin Creeks marina testimonial). Used as boundary evidence only (a hospitality PMS pole that can run marinas), cross-referenced from the campground pass.

## Sources

- DockMaster — https://www.dockmaster.com/ (fetched 2026-09-09) — positioning, module map, FAQ
- DockMaster — https://www.dockmaster.com/solutions/marina-management (fetched 2026-09-09) — slip/reservation/billing/launch/waitlist/utility detail
- Storable Marine — https://www.storablemarine.com/ (fetched 2026-09-09) — positioning, feature map, case studies
- Storable Marine (Molo) — https://www.storablemarine.com/marina-management-software/ (fetched 2026-09-09) — marina operations, reporting, integrations, FAQ
- Storable Marine — https://www.storablemarine.com/services/slips-mooring-storage/ (fetched 2026-09-09) — slip assignment, contracts, portal, meter readings, rent rolls
- Jonas Club — https://www.jonasclub.com/marina-management/ (fetched 2026-09-09) — club marina module
- RMS Cloud — https://www.rmscloud.com/ (fetched 2026-09-09) — boundary evidence (marina as PMS reconfiguration)
- Prior passes (cross-reference only): research/campground-rv-park-management.md (RMS "Boat size" field renaming, marina bundling), research/boat-yacht-charter-platform.md (boundary row vs Marina Management), research/golf-course-management.md (Jonas suite marina module), research/hotel-property-management-system-pms.md (WebRezPro marinas/kennels verticals)

## Product A — DockMaster

### Key observations (Layer A unless noted)

Positioning (root): "all-in-one marina management software trusted by 1,000+ marinas, boatyards, and marine dealerships… combines slip and storage management, service operations, boat sales, inventory, point of sale, payments, and a full accounting suite". Desktop = "complete marine ERP"; Web = cloud CRM/portal/eSignature/payments; Mobile = offline-first field app.

Marina Management solution page:
- **Visual marina map**: "Interactive marina interface with drag-and-drop slip assignments and real-time occupancy tracking"; "Locate customer boats instantly on the visual marina map"; "Manage partially occupied slips for linear dockage (e.g., fuel docks)".
- **Vessel data**: "Track vessel dimensions, LOA (Length Overall), and LWL (Length Waterline)".
- **Reservations & billing**: "Efficient transient reservation management"; "Deferred revenue management for seasonal contracts"; "Create storage proposals as PDFs or printed documents"; "Integrated billing, payment processing, and rent roll reporting".
- **Launch Master** (dedicated dry-stack/launch module): launch scheduling with queue and priority, real-time tracking, automated customer notifications, weather-based scheduling adjustments, integration with marina billing.
- **Customer & vessel management**: "Store detailed customer profiles with billing balances"; "Review and track boat information associated with each customer"; "Manage insurance details and documentation"; link accounts to reservations and payments.
- **Wait list & security deposits**: "Wait list management with priority tracking"; "Security deposit collection & distribution"; "Automated position notifications"; "Deposit refund processing".
- **Utility billing**: "Import electric meter readings and phone charges for automated usage-based tenant billing"; usage-based charge calculation integrated with A/R.
- **Integrations**: fuel (FuelCloud — real-time fuel inventory, automated pricing), vessel monitoring, meter readings (MarineSync — automated meter readings, usage analytics, unusual-usage alerts).
- FAQ: "It runs the daily operations of a marina from one system: slip assignments and reservations, storage and lease billing, customer and vessel records, launch and dry stack scheduling, utility metering, and integrated invoicing." Reservations module: "slip bookings on a calendar with wait-list management, customer holds, seasonal rates, and multi-month or multi-vessel bookings." Storage billing: "Recurring storage charges generate automatically from your rate cards and billing cycles, with proposals, deferral accounting, surcharges, and meter-based utility billing."

## Product B — Storable Molo (Storable Marine)

### Key observations (Layer A unless noted)

Positioning (marine root): "one system to run slip management, service workflows and boat rentals"; "software solutions designed specifically for marinas, service yards, boat clubs, and rental fleets". Case study: Pine Knot Marina ran "400 slips, 20+ rentals, service, and retail sales" on paper before switching; Harbourgate switched from a legacy system for cloud access, automated invoicing, online payments.

Molo product page:
- "Real-Time Visibility & Marina Map Views — See your property at a glance, drag-and-drop boats into slips, and manage transient or long-term dockage."
- "Slip Booking Flexibility — schedule transient or long-term stays with real-time pricing and instant customer data capture."
- "Support for Enterprise & Multi-Location Marinas — manage multi-location marina operations from a single login, standardize workflows, consolidate reporting."
- "Boat Service Workflow Management — track work orders, parts and technician schedules."
- Reporting: "80+ built in reports… slip occupancy and reservation revenue to service activity, GL exports and inventory usage"; report groups: financial/revenue (accruals, AR, GL exports), invoicing/payments (invoice aging, unallocated payments), service/work-order (volume, job status, technician hours, parts usage), "Reservation & Slip Performance — Occupancy %, linear footage usage, slip revenue", "Contact & Vessel Reporting — Vessel insurance, activity history, stored cards", operational oversight.
- Integrations: QuickBooks, Xero, NetSuite, Sage Intacct, Slack, SpeedyDock.

Slips/Mooring/Storage feature page:
- "Assign, renew, and bill accurately by dock, LOA, and season."
- "Slip Assignments & Reservations — Manage seasonal, annual, and transient contracts from one dashboard."
- "Mobile-Friendly for Dockside Service — View occupancy, perform meter readings, upload photos… from your mobile device."
- "Online Transient Bookings — Accept short-term slip reservations online with full payment processing."
- "Customer Portal — Let boaters pay bills, upload documents & manage reservations themselves."
- "Easy Billing & Payments — bill customers for fuel, services, or retail purchases."
- "Interactive Marina Map — real-time visual layout of all your slips and reservations."
- Reports: "From simple occupancy to slip utilization to full rent rolls with revenue recognition"; "Contact, vessel & insurance reporting"; "Staff activity logs & audit trails".
- Tagline: "Fill more slips, auto-renew moorage, & get paid on time."

## Product C — Jonas Club Marina Management

### Key observations (Layer A unless noted)

- Dedicated module page: "Easily Process Transient Reservations — Reservations can be taken and processed for members who don't have permanent slips — through the marina views screen and directly through the processing menu."
- "A graphical display of your wet and/or dry storage areas provides an effective overview of your facilities for club staff."
- "Provides a wide variety of real-time inquiries and reports."
- "The Marina Management system integrates to your Jonas Club Software system" — i.e., billing flows into the club's member accounting; the berthed population is club members.
- Reveals the club-marina shape: permanent slips held by members (long-term berthing) + transient reservations for member guests; wet and dry storage both displayed graphically.

## Cross-product Comparison

| Dimension | DockMaster | Storable Molo | Jonas Marina | Strength |
|---|---|---|---|---|
| Berth/space inventory as managed record | Visual marina map, drag-drop assignment, real-time occupancy, linear dockage | Interactive marina map, real-time slip assignments, custom harbor maps | Graphical wet/dry storage display | **Core (B, 3/3)** |
| Berthing agreements: long-term + transient | Transient reservations + seasonal contracts + multi-month bookings; deferred revenue | Seasonal, annual, transient contracts; auto-renew | Permanent member slips + transient reservations for members | **Core (B, 3/3)** |
| Vessel as berthed subject | LOA/LWL tracking, boat info per customer, insurance docs | Vessel details, vessel insurance reporting; assign "by dock, LOA, and season" | (implied: member boats; not detailed) | **Core (B, 2/3 direct)** |
| Occupancy/assignment operations | Real-time occupancy tracking, drag-drop, availability check | Real-time availability, drag-and-drop, occupancy views | Marina views screen | **Core (B, 3/3)** |
| Billing loop (recurring rent + transient + usage) | Rate cards, billing cycles, rent roll, deferred revenue, meter imports, A/R | Automated invoicing, rent rolls with revenue recognition, fuel/services/retail billing | Member-account billing integration | **Core (B, 3/3)** |
| Customer/boater profiles | Profiles with billing balances | Boater profiles, stored cards, comms | Club member records | Common (B) |
| Waitlist | Explicit: priority tracking, position notifications | Not directly evidenced | Not evidenced | Product-specific (A, 1/3) |
| Security deposits | Explicit: collection→distribution→refund | Not directly evidenced | Not evidenced | Product-specific (A, 1/3) |
| Utility metering | Electric meter reading imports, phone charges | Meter readings on mobile | Not evidenced | Common (B, 2/3) |
| Fuel dock | FuelCloud integration, fuel sales reporting | Fuel billing, pay-at-pump options | Not evidenced | Common (B, 2/3) |
| Service/yard work orders | Service Management module (work orders, estimates, time tracking) | Work orders, parts, technician schedules | Not evidenced (club pole) | Common (B, 2/3) |
| Dry stack / launch scheduling | Launch Master module (queue, priority, notifications) | "yard" workflows; storage areas | Dry storage display | Common (B, 3/3 existence; depth varies) |
| Online booking / customer portal | Payment links, customer portal (Web) | Online transient bookings, customer portal | Not evidenced | Common (B, 2/3) |
| Renewals | Seasonal contracts, deferral | Auto-renew moorage | Not evidenced | Common (B, 2/3) |
| Accounting | Built-in full accounting (A/R, A/P, G/L, bank rec) | Integrations: QuickBooks/Xero/NetSuite/Sage Intacct | Club accounting integration | Common (B; built-in vs integrated is a variant) |
| Multi-location | Not directly evidenced | Explicit enterprise multi-location | Not evidenced | Product-specific (A, 1/3) |
| Boat sales/dealership | Sales Management (leads, contracts, F&I, trade-ins) | Not evidenced | Not evidenced | Product-specific (A, 1/3) — segment variant |
| Boat rental fleet / boat clubs | Not evidenced | Storable Rentals (rentals, waivers, fleet) | Not evidenced | Product-specific (A, 1/3) — segment variant |
| Dynamic pricing | Not evidenced | "real-time pricing", "dynamic pricing" | Not evidenced | Product-specific (A, 1/3) |
| POS / retail | Touchscreen POS integrated | POS & billing, retail purchases | Club POS (separate module) | Common (B) |
| eSignature / documents | eSignature workflows, marine document templates | Document upload in portal | Not evidenced | Optional (B) |
| AI features | AI scheduling assistant, voice agent | AI blog guidance (feature-level not evidenced) | Not evidenced | Optional/emerging |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant (deliberately small)

The marina operator's berthing system of record. Four jointly-held structures:

1. **The berth/space inventory of record** — the facility's mooring spaces (wet slips, moorings, dry-stack racks, commonly yard/storage spaces too) held as individually identified, size-typed inventory with location on the docks; the inventory truth against which occupancy is managed. Remove → a customer list or billing tool with nothing to fill.
2. **The berthing agreement as the unit of work** — a persistent commitment binding a specific vessel (owned by a specific customer) to a specific space for a defined term: a long-term contract (seasonal/annual lease) or a transient stay (reservation or walk-in). The hub to which occupancy, charges, and services attach. Remove → an anonymous dock log.
3. **Occupancy state of the spaces** — which spaces are occupied, vacant, or reserved, driving the daily dock board and assignment decisions under the size-fit constraint (vessel dimensions vs space capacity). Remove → a lease ledger with no live operations.
4. **The berthing-to-money loop** — recurring rent billing on contracts (billing cycles, renewals), transient fees on stays, and usage charges (metered utilities, fuel, services) resolving into invoices/payments on the customer account. Remove → a free roster; the business loop is gone.

Jointly-held load-bearing:
- 1 alone = space registry/map with no business
- 2 without 1 = booking tool with no inventory truth (double-booking possible)
- 3 without 1+2 = occupancy board over nothing
- 4 without 1–3 = invoicing shell
- 1+2 without 3 = contract archive, not operations
- 1+3 without 2 = map with no commitments
- 2+4 without 1 = billing without inventory truth

Historical check (§24): the paper-era marina office — wall dock plan/slip chart, lease files, rent ledger, transient log book, meter-reading sheets, fuel tickets, yard work tickets — satisfies all four legs with no software, no cloud, no online booking. Older desktop marina systems and regional products fit. Therefore nothing era-specific (cloud, online booking, dynamic pricing, mobile) may enter the definition.

### L1 — Common Mature Structure

- Interactive marina/dock map as the signature surface (3/3 sampled — strongest common structure)
- Vessel records with dimensions (LOA/LWL) and insurance/documents
- Customer/boater profiles with balances and stored payments
- Utility metering (electric meter readings → usage-based charges)
- Fuel dock sales and POS
- Service/yard work orders (parts, labor, technicians)
- Dry-stack storage and launch scheduling
- Online transient booking and customer portal
- Renewal machinery for seasonal/annual contracts
- Occupancy / rent-roll / revenue reporting
- Accounting: built-in suite or integrations (variant of realization)

### L2 — Variant / Optional Structure

- Segment variants: full-service boatyard (deep service), marine dealership (boat sales, F&I), boat rental fleet / boat clubs, club marina (member population), municipal/harbour-authority operation (not directly observed), dry-stack-dominant operation
- Multi-location enterprise management
- Dynamic/real-time pricing
- Waitlists and security deposits (directly evidenced at one product; likely common in market but unverified breadth)
- Vessel monitoring/security integrations, eSignature, digital waivers
- AI assistance (scheduling, voice agents)

### L3 — Vendor-specific (Research Notes only)

- DockMaster: "Launch Master" module name; "Visual Marina Map"; MarineSync/FuelCloud integrations; Blu Voice Agent; desktop/web/mobile packaging; 40+ years framing
- Molo: "80+ built-in reports"; SpeedyDock/Slack integrations; app.getmolo.com; Storable Marine packaging; "Fill more slips, auto-renew moorage" tagline
- Jonas: "marina views screen"; ClubHouse Online ecosystem; member-billing integration shape

## Vendor-specific Findings

- DockMaster is the only sampled product with explicit waitlist machinery, security-deposit lifecycle, and linear-dockage partial occupancy — treat as product-specific until broader evidence.
- Molo is the only sampled product with explicit multi-location enterprise support and dynamic pricing claims.
- Jonas is the only sampled product whose berthed population is club members with billing into club accounting — audience variant, not a definitional difference.

## Boundary Findings

1. **vs Campground/RV Park Management** — same structural shape (rentable-space inventory + dated commitments + occupancy lifecycle + billing). The campground pass itself recorded: "same shape over water (slips as sites, transient docking + long-term leases, size-fit constraints)… Distinct Type because watercraft operations (berthing, haul-out, dockside services) differ; products straddle." Test: strip the vessel/berthing semantics (vessel records, size-fit, wet/dry, dockside utilities, fuel dock, yard) and what remains is campground management; a marina without vessels is a parking lot. Sibling Types under rentable-space operations; the marina's defining difference is the vessel as berthed subject plus marine service context, and long-term-lease dominance (vs campground transient dominance).
2. **vs Hotel PMS** — hotel PMS binds guests to rooms for short stays with folios; marina binds vessels to berths, dominantly on long-term contracts, with vessel/yard/fuel semantics. Boundary evidence: a hospitality PMS (RMS Cloud) can be reconfigured to run marinas (its own case-study testimonial shows a marina property; the campground pass documented "Boat size" field renaming) — the shape is portable, but the marina Type carries marine-specific objects the hotel PMS does not define.
3. **vs Boat/Yacht Charter Platform** — charter sells time-use of vessels to the public (demand side, vessel-centric); marina manages berths for the operator (supply side, space-centric). The charter pass's own boundary row: "manages berths, dockage, and marina operations for the marina operator; a charter platform sells time-use of vessels to the public; marinas host charter bases but the systems do not merge."
4. **vs Port Terminal Operating System** — TOS serves commercial cargo terminals (container moves, gate/yard/crane operations); marina serves recreational vessels and long-term berthing. Different users, objects, and economics.
5. **vs Self-storage Management** — dry-stack racks resemble storage units and some vendors straddle (Storable spans both), but the marina's core is wet berthing + vessel + marine services; a dry-stack-only operation is a marina variant, not self-storage.
6. **vs transient-dockage marketplaces (boater-facing booking venues)** — operator-side system of record vs consumer-side listing/booking venue. Not directly observed in this pass (Dockwa unreachable); recorded as a weak, directory-level boundary only.
7. **vs Marine Fleet Management / Vessel Operations** — those manage the vessel owner's fleet; marina manages the facility operator's spaces and berthing business.

## Uncertainties

- Sample breadth: only 3 products directly observed; the transient-boater-marketplace pole (Dockwa) and the harbour-authority pole (Harbour Assist) could not be fetched. Claims about those poles are not made in the final document.
- Exact berthing lifecycle state names (reserved → arrived → moored → departed) were not directly evidenced per product; the final document keeps lifecycle states conceptual.
- Waitlist and security deposits: direct evidence at DockMaster only; breadth in the market unverified.
- Meter-reading mechanics vary (file import vs mobile capture); exact mechanics not generalized.
- Whether every marina product includes yard/service: the club pole (Jonas) shows a marina module without evidenced service work orders — service depth treated as common-mature, not definitional.

## Final Synthesis

Marina Management is the marina operator's berthing system of record. Its defining core is four jointly-held structures: the berth/space inventory of record (wet slips, moorings, dry-stack racks as identified, size-typed spaces on the docks), the berthing agreement as the unit of work (long-term lease or transient stay binding vessel × customer × space × term), the occupancy state of the spaces driving daily dock operations under size-fit constraints, and the berthing-to-money loop (recurring rent + transient fees + usage charges → invoices/payments). Everything else — dock maps, meter readings, fuel, work orders, online booking, portals, renewals, dynamic pricing, multi-location — is standard or optional machinery that mature products add. The Type is the water sibling of campground/RV park management, distinguished by the vessel as berthed subject and marine service context; it is not a hotel PMS, not a charter platform, not a port TOS, and not self-storage.
