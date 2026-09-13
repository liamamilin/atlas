# Research Notes — Amenity Booking Platform

## Research Goal

Understand what an Amenity Booking Platform actually is as an Application Type: what gets booked, by whom, under whose control, how a reservation lives and dies, what rules shape bookings, and where the Type's boundary sits against resident portals, appointment scheduling, resource/space booking, facility management, and hotel PMS.

## Initial Boundary

Initial hypothesis (pre-research):

- Core use: residents/tenants of a building or community reserve shared facilities (pool, gym, clubhouse, courts, guest suite, elevator/move slots) through a resident-facing surface; building staff/management configure amenities, enforce rules, and manage reservations.
- Likely users: residents/tenants (bookers); property managers, front-desk/concierge staff, HOA/community association managers, commercial property teams (operators).
- Nearest neighbor Types: Tenant / Resident Portal (booking as one function inside a broader portal), Appointment Scheduling Application (client↔provider service time), Resource Calendar / Space & Occupancy (desk/meeting-room booking), Facility Management System (maintaining the amenity, not scheduling its use), Hotel PMS (nightly stays of private units), Event Management/Registration (organized programs).
- Open questions: is this a real standalone Type or only a module of property-management suites? How universal are approvals, fees/deposits, guest limits? How does the office/CRE tenant-experience version differ from the residential version?

## Research Questions

1. What counts as an "amenity"? Is the inventory limited to physical shared spaces, or does it generalize (elevator moves, appointments, services)?
2. Who is eligible to book, and where does eligibility come from (lease, unit, association membership)?
3. What does a reservation contain, and what lifecycle/statuses does it move through?
4. How is availability structured (calendar, slots, capacity, overlap prevention)?
5. What rules does a building hang on bookings (approval, guest limits, max duration/occupancy, fees, deposits, documents, hours, blackouts)?
6. What does the operator side do (configure, approve, decline, cancel, notify, track)?
7. How is the capability delivered (standalone vs module of PM suite / resident portal / tenant-experience platform)?
8. Where are the boundaries with neighboring Types?

## Representative Products

Selected for market coverage across residential segments, HOA, and commercial CRE, plus differing product philosophies (suite module vs building-operations platform vs tenant-experience platform):

| Product | Segment | Product philosophy / packaging |
|---|---|---|
| BuildingLink | residential buildings (condo/co-op, HOA, multifamily, also commercial) | building-operations platform; amenity reservations as a staff-and-resident module among ~67 modules |
| CINC Systems (CINC Connect) | community association management (HOA) | management company-branded resident/board experience; amenity booking inside resident self-service |
| Entrata (ResidentPortal) | multifamily property management | PM suite with separate resident-experience portal; amenity booking surfaced in resident dashboard |
| HqO (Experience suite) | commercial office CRE | tenant-experience platform; amenity booking inside an experience/engagement suite |
| Vantaca (Vantaca Home) | HOA / community association | association management platform with resident app; booking of communal spaces |

## Sources

Fetched 2026-09-06 (WebFetch, markdown):

- BuildingLink root site — https://www.buildinglink.com/ (feature taxonomy; "Amenity Reservations" under Resident Experience and Record-Keeping & Administration; platform activity stats)
- BuildingLink Staff Help Site — Amenity Reservations article — https://help-staff.buildinglink.com/en/support/solutions/articles/42000098635-amenity-reservations (Tier-1 operational documentation; modified 2024-12-26)
- BuildingLink Staff Help Site — Manage Tab folder — https://help-staff.buildinglink.com/en/support/solutions/folders/42000105689 (module placement, related Amenity Settings / Product Update articles)
- CINC Systems — Boards + Residents — https://cincsystems.com/boards-residents (Amenity Booking section with resident steps and management-side capabilities)
- CINC Systems root — https://www.cincsystems.com/
- Entrata — ResidentPortal product page — https://www.entrata.com/products/residentportal (dashboard references "amenity booking" quick link)
- Entrata root — https://www.entrata.com/
- HqO — Experience product page — https://www.hqo.com/product/experience/ ("From access to amenity booking to service execution"; paid entry; waitlists; billing)
- HqO root — https://hqo.com/
- Vantaca — Vantaca Home — https://www.vantaca.com/home ("easy booking of communal spaces")
- Vantaca root — https://vantaca.com/

Source-access limitations:

- Yardi RentCafe (major multifamily PM suite with resident amenity reservations) — https://www.yardi.com/products/rentcafe/ returned HTTP 403; abandoned after one attempt per network rules. Multifamily PM-suite evidence therefore rests on Entrata.
- BuildingLink resident-side help site and the separate "Amenity Reservations Settings" article (hosted on a different doc domain) were not fetched; resident-facing booking flow is inferred from the staff article's description of resident submissions and from CINC's resident-side description.
- CINC/Entrata/Vantaca/HqO pages are Tier-2 product marketing; only BuildingLink provided Tier-1 operational documentation. Claims below are calibrated accordingly.

## Product A — BuildingLink

Evidence layer: A (Tier-1 staff help article + official site).

Key observations:

- The Reservations module "allows you to track and coordinate amenity reservations at your building." Bookable items: "physical amenities (theater, club room, etc.), appointment times, elevator reservations, or even massages and restaurant tables" — i.e., the inventory is whatever the building defines, not only physical shared rooms.
- Module can be "Internal Only": residents cannot request or view the amenity calendar; staff use it purely as internal scheduling. Otherwise residents submit requests from web or Resident App.
- Permission split: settings decide whether non-management employees may enter reservations for residents; only Management / Security Officer level users can approve/decline. Reservation requests entered by non-management automatically get Status = Requested, with no Approve/Decline options visible.
- Reservation record: amenity (selected from building's amenity list) + requester (resident/unit; contact person selectable when a unit has multiple occupants) + date/time (or "All Day" — used e.g. to close an amenity for a day) + details. Recurring reservations supported (e.g., book club every Monday; board meetings every second Tuesday), editable per occurrence or per series.
- Status lifecycle: Requested → Approved / Declined; Cancel also available. Per-amenity-type setting for automatic approval. Overlap prevention: amenities can be set to prohibit overlapping reservations (error message on conflicting request).
- Operator actions: approve/decline/cancel/edit; add notes to the reservation log (examples given: "Payment Received"; for an elevator reservation, "Certificate of Insurance Received") with private-note option; send email reminders to the resident about outstanding paperwork/payment; edit date/time.
- Notifications: staff notified on new requests and reservation changes; residents notified automatically when reservation status changes to approved/declined (not on cancellation).
- Views: list (filter/sort by amenity type, status, date range) and Calendar View (used to check availability before requesting); reservations calendar is separate from the building's event Calendar; QuickSearch shows upcoming reservations per unit.
- Placement: "Amenity Reservations" appears both under Resident Experience and under Record-Keeping & Administration; a separate Amenity Reservations Settings topic covers "the amenities available for your property and their constraints" (constraints not detailed in the fetched article).
- Site-level: platform claims 195K+ amenity reservations booked; "Residents book amenities directly, reducing manual coordination and freeing up staff."

## Product B — CINC Systems (CINC Connect)

Evidence layer: A (product page with specific Amenity Booking capability description), partially B.

Key observations:

- CINC Connect (branded web + mobile resident/board experience) explicitly includes "amenities" in resident self-service. Amenity Booking section ("Court booked. Game on."):
  - Schedule: "Browse amenities and open times"
  - Rules and Requirements: "Review rules, guest limits, fees, deposits, or other requirements"
  - Reservations: "Complete the reservation steps required by the community"
  - Reservations visible in the branded experience ("My reservations")
- Management side: "Teams can manage availability, rules, fees, and reservations without handling every request by phone or email."
- Amenity cards show per-amenity state: e.g. "Pickleball Court — Free — Max 4 — Max 2h — Today's next available time-slots 9:00 AM / 10:00 AM / 11:00 AM"; "Community Pool — Free — Max 12 — Max 3h" (mock data on the marketing page, but confirms the displayed attributes: availability, max occupancy, max duration, time slots).
- The platform positions resident activity (payments, requests, amenities) as "connected to the management work in CINC" — booking lives inside a community-management suite, not standalone.

## Product C — Entrata (ResidentPortal)

Evidence layer: A- (product page + product screenshot text).

Key observations:

- ResidentPortal is Entrata's resident-facing portal within a large multifamily PM suite (OXP operations platform + RXP resident experience platform).
- The dashboard screenshot's quick links include "amenity booking" alongside balance/payment, late-rent alert, package pickup — i.e., amenity booking is a standard resident-portal tile.
- Page copy itself emphasizes rent payment, work orders, documents, events, community wall; amenity booking appears only in the UI mock — no operational detail published on the fetched page. Breadth of the booking capability is therefore not independently verifiable from this source.

## Product D — HqO (Experience suite)

Evidence layer: A- (product page, marketing depth).

Key observations:

- HqO REX is a commercial-real-estate experience platform; the Experience Suite covers "From access to amenity booking to service execution" — amenity booking is listed as one pillar of building experience operations, next to building access and service delivery.
- Events & Services: tenant events with admin/self check-in, "Paid Entry options for premium, revenue-generating experiences", "Automated waitlists" (described for events, not confirmed for amenity slots).
- Billing & Operational Finance: "amenity passes, vendor services, or event bookings" with transaction logging, payment reporting, and "integration with tenant billing platforms" — commercial buildings monetize amenity usage through the same suite.
- Audience & Profile: user/tenant profiles tied to engagement — booking activity feeds tenant-experience analytics.
- No operational booking-flow detail published on the fetched pages.

## Product E — Vantaca (Vantaca Home)

Evidence layer: B (single short claim on official product page).

Key observations:

- Vantaca Home (resident/board app for community associations): "personalized content, exclusive offers from top brands, and easy booking of communal spaces" — amenity/communal-space booking confirmed as a resident capability.
- No further operational detail on the fetched page; management-side booking administration not documented on fetched surfaces.

## Cross-product Comparison

| Dimension | BuildingLink | CINC Connect | Entrata ResidentPortal | HqO Experience | Vantaca Home |
|---|---|---|---|---|---|
| Amenity inventory operator-defined | Yes (per-property amenity list + constraints) | Yes ("manage availability, rules, fees") | implied (portal tile) | Yes (experience operations) | Yes (communal spaces) |
| Booker population closed to building | Yes (residents/units; staff book on behalf) | Yes (association residents) | Yes (residents) | Yes (tenants/employees of building) | Yes (association homeowners) |
| Reservation = amenity × time × booker | Yes | Yes (slots; "Max 2h") | implied | implied | implied |
| Availability calendar/slots | Yes (Calendar View; list filters) | Yes (open times; today's slots) | implied | implied | not observed |
| Request → approval workflow | Yes (Requested/Approved/Declined/Cancelled; auto-approve option; role-gated approval) | Steps "required by the community" (approval not explicit) | not observed | not observed | not observed |
| Overlap/conflict prevention | Yes (optional prohibit-overlap with error) | implied by slot display | not observed | not observed | not observed |
| Per-amenity rules surface | Yes (constraints; notes e.g. insurance cert, payment) | Yes (rules, guest limits, fees, deposits) | not observed | not observed (billing for amenity passes) | not observed |
| Fees/deposits handling | tracked via notes/emails in doc; payments module separate | requirements incl. fees/deposits | not observed | transaction logging + tenant billing integration | not observed |
| Recurring reservations | Yes | not observed | not observed | not observed | not observed |
| Staff book on behalf of resident | Yes (role-gated) | not observed | not observed | not observed | not observed |
| Internal-only mode | Yes (module switch) | not observed | not observed | not observed | not observed |
| Resident notifications on status | Yes (approved/declined, not cancellation) | "see reservations"/status in app | not observed | not observed | not observed |
| Delivered as | module of building-operations platform | module of association-management suite | module of PM suite portal | suite pillar in tenant-experience platform | module of association platform |

Stable commonalities (Layer B): operator-defined amenity inventory; closed resident/tenant booker population; time-bound reservation against availability; building-defined usage rules attached to amenities; operator-side configuration and reservation management; resident-facing "my reservations" visibility; capability almost always shipped inside a broader property/resident platform.

Asymmetric evidence: approval workflow, overlap prevention, recurring reservations, staff-on-behalf booking, internal-only mode are documented only in BuildingLink's Tier-1 doc. Treat as common mature structure with single-source depth, not as canonical requirements.

## Canonical Model

Four-level abstraction.

### L0 — Defining Invariant

1. **Operator-defined amenity inventory** — the building/community's shared amenities exist as bookable resources, each configured (existence, time structure, constraints) by the building's operator.
2. **Closed booker population** — booking eligibility derives from occupancy/membership: residents, tenants, unit holders of that specific building/association (plus operator staff acting for them). Not a public marketplace.
3. **Time-bound reservation** — a reservation binds one amenity to a time window and an eligible booker, with the system tracking availability so the same amenity-time is not double-consumed.
4. **Building-side control surface** — an operator-facing side that configures amenities/rules and manages reservations over their lifecycle (create/approve/change/cancel/release).

Remove any one: no amenity inventory → generic appointment scheduling; open population → public facility/event booking marketplace; no time-bound reservation → bulletin board/announcement; no operator control → a self-service widget, not a platform the building runs.

### L1 — Common Mature Structure

Very common in mature products, not definitional:

- availability presentation as calendar or next-available time slots; per-amenity capacity and duration limits
- request → approval workflow with per-amenity auto-approval; role-gated approval rights
- per-amenity rules surfaced to bookers: guest limits, hours, fees, deposits, required documents (e.g., insurance certificates for moves)
- fee/deposit recording and payment linkage (in-suite payments or notes/accounting handoff)
- cancellation and modification by either side; recurring reservations
- notifications to bookers on status change; staff notification of new requests
- staff booking on behalf of residents; internal-only scheduling mode
- booking history per unit/person; list + calendar operator views

### L2 — Variant / Optional Structure

- packaging: module of a multifamily PM suite (resident portal tile), module of an association-management platform (branded resident app), pillar of a CRE tenant-experience platform, or standalone booking tool
- segment flavor: residential condo/co-op vs HOA (volunteer boards, no on-site staff) vs commercial office (tenant companies as the booker's employer; monetized amenity passes; engagement analytics)
- adjacent capabilities that share the booking surface: guest-suite overnight stays; move/elevator reservations; bookable appointments and services; event creation/paid entry/waitlists
- integration posture: access-control linkage (booking grants entry), payments stack, calendar export, PM-suite accounting sync
- monetization: free-to-resident (membership entitlement) vs fee-based vs deposit-guaranteed

### L3 — Vendor-specific Structure (Research Notes only)

- BuildingLink: Management/Security Officer role split; "notify residents on status change (not cancellation)" checkbox; private notes; occurrence-vs-series recurring editing; reservations calendar separate from Building Calendar; QuickSearch by unit; Internal Only module switch set via support; amenity types generalizing to massages and restaurant tables
- CINC: management-company-branded app store presence; amenity card attributes (Free / Max N / Max 2h / today's slots); Community Intelligence/AI skills elsewhere in platform
- HqO: REX framing; paid entry events; automated waitlists (events); Leesman experience assessment; tenant-billing-platform integration
- Entrata: agentic-OS positioning; 3,000+ settings claim; amenity booking tile in ResidentPortal dashboard
- Vantaca: HOAi AI workforce; member-benefits marketplace framing around booking

### Rejected Findings

- "Amenity booking = payment for amenities" — several sampled deployments are entitlement-based (membership-included); payments/deposits are rule variants, not the core.
- "Booking grants door access" — plausible and marketed via integration categories, but not operationally documented in the fetched sample; kept as optional integration, not asserted as behavior.
- "Waitlists are standard for amenity slots" — observed at HqO only and for events; not generalized.
- "Amenities are always physical spaces" — falsified by BuildingLink (elevator reservations, appointments, services); the canonical concept is an operator-defined bookable resource.
- "Residents always self-book" — falsified by BuildingLink's internal-only mode and staff-on-behalf workflow; self-service is the common default, not the invariant.

## Boundary Findings

- **vs Tenant / Resident Portal**: the portal is the aggregation surface (payments, requests, documents, communication); booking is one capability inside it in most market deliveries. A portal without booking is still a portal; the booking core (inventory × eligibility × reservation × operator control) stands alone. Distinct Types with heavy delivery overlap — booking is usually delivered as a module. Recorded as a packaging reality, not a merge.
- **vs Appointment Scheduling Application**: appointment scheduling mediates a client ↔ provider service time with provider availability; amenity booking mediates a resident ↔ building shared-asset use under building rules. The building is not a service provider and the booker is not an external client. Removal test: strip building-defined amenity rules and occupancy-based eligibility → appointment scheduling.
- **vs Resource Calendar / desk & meeting-room booking (Space & Occupancy)**: generic resource scheduling serves an employee population booking workspaces; no building-amenity rule semantics (guest limits, deposits, lease-based eligibility, operating hours as community rules). Segment overlap exists for office buildings; the amenity-specific rule/eligibility layer is the boundary.
- **vs Facility Management System**: FM maintains the amenity (work orders, inspections, preventive maintenance); booking schedules its use. In BuildingLink both coexist as separate modules; a booked amenity with a broken pump generates a work order in the other system.
- **vs Hotel PMS / Short-term Rental Management**: PMS books exclusive overnight occupancy of private units with folio/payment and stays; amenity booking allocates short shared-asset use windows to people who already belong to the property. Guest suites blur the edge (overnight stay of an amenity) — treated as an L2 adjacency.
- **vs Event Management / Registration**: events are organized programs with attendee registration; amenity reservations are self-directed use of a facility. Platforms like HqO run events inside amenity spaces and share the booking substrate, but the attendee/program objects differ.
- **Removal test summary**: strip the closed resident population → public facility-booking; strip the building rule layer and amenity semantics → generic resource scheduling; strip time-bound reservations → announcement/bulletin board. The Type holds.

## Uncertainties

- Whether fee/deposit collection is executed in-platform or recorded and settled via the suite's payments/accounting is documented only partially (CINC lists fees/deposits as requirements; HqO logs transactions; BuildingLink's doc records payment via notes). Final doc uses moderate wording.
- Resident-side booking flow detail (what the resident sees step by step) comes from marketing descriptions plus the staff-side doc; BuildingLink's resident help and amenity-settings pages were not fetched.
- Waitlists for amenity slots, per-amenity blackouts, and access-control unlock behavior: not verified; not asserted.
- Market size of truly standalone amenity-booking vendors vs suite modules: not measured; packaging claim ("usually a module") rests on the sampled products being all suite/platform-bundled.

## Final Synthesis

An Amenity Booking Platform is the building's own reservation system for its shared amenities: an operator (property manager, association, building staff) defines a bookable inventory of shared resources with time structures and rules; a closed population of residents/tenants (or staff acting for them) binds amenities to time windows via reservations that are checked against availability; and the operator side configures, oversees, and moves those reservations through their lifecycle. Usage rules the building hangs on amenities — approvals, guest limits, hours, capacity, duration, fees, deposits — are the recognizable texture of the Type, but they are calibrated extensions, not the definition. The Type survives across condo towers, HOA pool decks, and office towers, and across delivery as a portal tile, an association app section, or a suite pillar; what does not vary is the amenity × resident × time reservation under building control.
