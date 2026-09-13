# Research Notes — Dock Scheduling Platform

## Research Goal

Understand what a Dock Scheduling Platform (dock appointment scheduling system / DSS) actually is in the real market: what objects it manages (appointments? doors? capacity? loads? carriers?), how the scheduling loop between a facility and its carriers/suppliers works, what rules govern what can be booked when, where the appointment lifecycle begins and ends, and where the boundaries lie with neighboring Types (Yard Management System, WMS, TMS, generic Appointment Scheduling). Determine which structures are definitional vs common vs variant — and discharge the three seams pre-hung by the yard-management-system, warehouse-management-system-wms, and transportation-management-system-tms passes.

## Initial Boundary

Initial hypothesis (pre-research): a Dock Scheduling Platform is the facility-side system of record for planning freight arrivals and departures — it holds the dock/door-time capacity of record, manages appointments binding loads and carriers to doors and time windows, and governs the request/confirm/change loop between the facility and its external freight partners under facility-defined rules. Its center of gravity is plan-before-arrival.

Pre-hung seams to discharge (from STATUS.md, first-hand from those passes):
- **yard-management-system** (§10, processed 2026-09-08): keep-both proposed with the arrival-gate seam — dock scheduling = plan-before-arrival (unit of work = the appointment; vendor-drawn "Dock scheduling's job effectively ends at the gate"), yard management = execute-after-arrival (unit of work = the trailer and the move, gate-in to gate-out). C3 sells both as separate products; YardView bundles dock scheduling in its YMS suite; kaleris ships dock appointments inside YMS. This pass should ratify from its side.
- **warehouse-management-system-wms** (§10, processed 2026-09-08): seam recorded — "dock-scheduling-platform (dock time-slot appointments vs WMS receiving once goods arrive) — no merge, that pass should ratify."
- **transportation-management-system-tms** (§10, processed 2026-09-08): seam (8) — "dock-scheduling/yard-management = facility-level machinery shipped as TMS modules (Shipwell Dock Scheduling), standalone forms are their own Types." The dock-scheduling half of this seam is ratified from this side (the yard half was discharged by the YMS pass).

## Research Questions

1. What is the core object model — appointment, dock door, facility, time slot/capacity, load type, carrier/supplier, load/shipment/order?
2. Who schedules — facility planners only, or carriers/suppliers self-service? What does the multi-party loop look like?
3. What rules govern scheduling — capacity per door/slot, load-type restrictions, durations, lead times, priorities, exceptions?
4. What is the appointment lifecycle — request → confirm → change/cancel → day-of → completion? Which statuses exist and do they extend past the gate?
5. What happens day-of — does the scheduling system track arrival/check-in/unload, or does its responsibility end at the gate?
6. What is the relationship to YMS, WMS, TMS — module, sibling product, integration?
7. Which roles use the system, on which surfaces?
8. What variants exist: standalone vs YMS/TMS-embedded, inbound-only vs inbound+outbound, by-appointment vs open scheduling, automation posture, industries?
9. Historical check: what did docks run on before dock scheduling software, and would those forms satisfy the definition?

## Representative Products

| Product | Segment / philosophy | Why sampled | Evidence depth |
|---|---|---|---|
| C3 Reservations (C3 Solutions) | Standalone dedicated dock scheduling product (since 2000, Montreal); also sells a YMS sibling (C3 Yard) | Dedicated standalone pole; the vendor that draws the dock-vs-yard boundary itself; rich product/tour/FAQ/blog content | Tier-2 (product page, tour, FAQ, boundary blog fetched) |
| Shipwell Dock Scheduling | Dock scheduling as a module of a TMS platform; API-first | TMS-embedded pole; the only Tier-1 source in the sample (developer/API documentation with full object model and status enum) | Tier-1 (developer docs, API reference, MCP tool docs fetched) |
| YardView | Dedicated YMS suite (since 1998) with a dock scheduling module; also sells a stand-alone dock scheduling option | YMS-embedded pole from a dedicated vendor; explicit vendor FAQ on dock-vs-yard distinction | Tier-2 (dock-appointments page, features, FAQ fetched) |
| kaleris (YMS) | Enterprise dedicated YMS (ex-PINC lineage) with dock appointments inside | Enterprise YMS-embedded pole; "intelligent dock scheduling" positioning; retail inbound-load-planning framing | Tier-2 (solution pages, blog, press release fetched) |
| Turvo Appointment Scheduling | Appointment scheduling as an application inside a collaborative TMS cloud | Collaboration-first pole; driver/carrier self-service emphasis; cross-tenant data sharing | Tier-2 (product page, solution brief, press release fetched) |

The sample spans four packaging philosophies (standalone / TMS-embedded / YMS-embedded dedicated / collaboration-TMS application) and three customer postures (dedicated mid-market, enterprise, TMS-suite customers).

## Sources

Fetched 2026-09-10:

C3 Solutions (c3solutions.com, Tier-2):
- Dock Scheduling Software product page — https://www.c3solutions.com/dock-scheduling/
- C3 Reservations Product Tour — https://www.c3solutions.com/dock-scheduling/tour/
- Dock scheduling FAQ — https://www.c3solutions.com/dock-scheduling/faq/
- "Dock Scheduling vs. Yard Management: What You Actually Need at Scale" (blog, 2026-09-02) — https://www.c3solutions.com/blog-c3/dock-scheduling-vs-yard-management/

Shipwell (docs.shipwell.com, Tier-1):
- "What is dock scheduling?" — https://docs.shipwell.com/docs/dock-scheduling/what-is-dock-scheduling/
- Dock Scheduling API overview — https://docs.shipwell.com/openapi_pages/dock-scheduling/overview/
- Create Dock Appointment (API reference) — https://docs.shipwell.com/openapi_pages/dock-scheduling/operation/create_dock_appointment_facilities__facility_id__docks__dock_id__appointments_post/
- Schedule Appointment (API reference) — https://docs.shipwell.com/openapi_pages/dock-scheduling/operation/schedule_appointment_facilities_appointments__appointment_id__schedule_post/
- Facilities & Dock Scheduling (MCP tools) — https://docs.shipwell.com/docs/mcp/tools/facilities/

YardView (yardview.com, Tier-2):
- Dock scheduling product page — https://www.yardview.com/dock-appointments
- YMS features page — https://www.yardview.com/features
- FAQ — https://www.yardview.com/faq
- Why we lead — https://www.yardview.com/why-we-lead

kaleris (kaleris.com, Tier-2):
- Yard Management Solutions — https://kaleris.com/solutions/yard-management/
- "Why a Purpose-Built YMS Outperforms WMS Yard Modules" (blog, 2026-05-28) — https://kaleris.com/why-a-purpose-built-yms-outperforms-wms/
- Advance Your Yard Operations — https://kaleris.com/advance-your-yard-operations/
- MODEX 2024 press release (Appointment Scheduling feature) — https://kaleris.com/news/kaleris-launches-yard-management-innovations-at-modex-2024/
- Retail page — https://kaleris.com/who-we-serve/retail/

Turvo (turvo.com, Tier-2):
- Appointment Scheduling product page — https://turvo.com/scheduling/
- Solution brief — https://turvo.com/solution-briefs/turvo-appointment-scheduling/
- Launch press release (2021-04-06) — https://www.prnewswire.com/news-releases/turvo-announces-new-appointment-scheduling-application-to-drive-yard-efficiency-and-contribute-to-supply-chain-sustainability-301263106.html

Prior-pass evidence reused (recorded in STATUS.md, first-hand from those passes):
- TMS pass: Shipwell Dock Scheduling as a TMS module; no sampled TMS help center was reachable in that pass.
- WMS pass: D365 driver check-in + staging/loading locations as the WMS-side edge.
- YMS pass: full YardView/kaleris/C3 Yard observations (yard-side), reused here only where dock-relevant.

Source-access limitation: no UI help-center articles were reachable for C3 Reservations, YardView, kaleris, or Turvo (their operational documentation is marketing-hosted product/tour/FAQ pages, Tier-2). Shipwell's developer documentation is the only Tier-1 source. Operational depth (exact UI state machines, default lead times, permission models, numeric limits) is therefore not asserted beyond what vendors publish; precise vendor facts stay in these notes.

## Product A — C3 Reservations (standalone dedicated dock scheduling)

### Key observations (A = direct observation of this product)

- **Definition published by vendor (A):** "a system designed to optimize operational efficiency for facilities that manage inbound and outbound shipments. It allows for the configuration of facility specifics, including load types and dock doors, to facilitate online scheduling of dock appointments by carriers and suppliers. This software provides notifications and real-time updates on appointment statuses, dwell times, and more."
- **Key features as marketed (A):** Carrier and Supplier Web Portal; Capacity and Rule-Based Durations; Automated Notifications; Reports and Dashboards; Audit and Compliance.
- **Scheduler surface (A):** "An intuitive calendar view, drag'n'drop functionality and real-time updates allow your schedulers to be the most productive." All dock door schedules "managed with the click of a button."
- **Carrier/supplier self-serve portal (A):** carriers and vendors manage their appointment requests to all locations; step-by-step flow "first-time users grasp without training"; user management tools so carriers manage their own logins; available 24/7.
- **Capacity model (A):** "C3 Reservations' capacity model balances your dock workload so you can accurately plan your labor and equipment needs." Plan per warehouse dictating "who can deliver which product, at which facility and in what time period."
- **Rule-based durations (A):** "a natural-language based rule system that allows you to compute accurate unloading times by including all the subtleties of shipments" — for when "fixed or average appointment times don't fit"; result: better labor forecasting and scheduling accuracy.
- **Rules engine (A):** "Most companies' scheduling rules & policies are either found in a disorganized binder or the scheduler's head. C3 Reservations allows you to translate all your constraints and exceptions into clear and concise rules. It can be as simple as the number of pallets per shift to complex logic tying load types, PO's, product descriptions and more." Rules "automatically enforced eliminating the need to manually process special appointments and exceptions."
- **Reserved capacity semantics (A):** "allows you to reserve physical capacity and restrict the load content of the allocated time. Your carrier or supplier doesn't use its reserved slot? No problem! Configurable expiration dates can free up the reserved slot."
- **Automation posture (A):** "every request that fits within your schedule and constraints can be automatically processed without any user intervention. The level of automation, however, is customizable… automate your top tier carriers and vendors while keeping a hands-on control over your lower tier." Exceptions "channelled into a prioritized task queue."
- **Compliance/scorecarding (A):** "compliance and scorecarding ensure they respect the standards of your operations"; "vendor report cards"; "an auditable record of who booked what, when, and whether they honored it" (blog).
- **Documents (A):** carriers/vendors can attach electronic documents (packing slips, bills of lading) to each appointment.
- **Multi-site (A):** "supports an unlimited number of sites and warehouses across multiple time zones… distinct capacity management and user access… centralize or decentralize your scheduling."
- **Inbound/outbound (A, FAQ):** "handles outbound appointments. Any specific site can be setup to handle inbound and/or outbound appointments."
- **Independence (A, FAQ):** "can function independently without the need for integration with warehouse, transportation, or yard management systems. However, for those that require integration, APIs are available to connect with such systems" (TMS, WMS, RTV).
- **Kiosk (A):** self-serve kiosk giving carriers/vendors 24/7 access to real-time availability at each facility.
- **Boundary, vendor-drawn (A) — the same vendor sells both products:** dock scheduling "governs everything that happens before the truck arrives… answers a planning question: given the doors, labor, and equipment I have available, when should each carrier and supplier show up, and at which door?… Dock scheduling's job effectively ends at the gate." Time horizon: days to weeks ahead. Unit of work: the appointment. Primary users: planners, schedulers, carriers, suppliers. Main question: "When should they come?" Executive metrics: on-time arrival, labor smoothing, carrier compliance. "Fails when volume exceeds door and labor capacity." Yard management = after arrival, gate-in to gate-out, unit of work = the trailer and the move. Coupling at scale: "one continuous record per shipment, running from the moment a carrier books through gate-in, yard moves, door assignment, unload, and gate-out."
- **Pre-history named by vendor (A):** "your warehouse can no longer operate on a 'first come, first serve' basis"; rules "found in a disorganized binder or the scheduler's head"; (blog) the phone-and-email traffic planners drown in.

## Product B — Shipwell Dock Scheduling (TMS-embedded; Tier-1 API docs)

### Key observations

- **Definition published by vendor (A, Tier-1):** "Shipwell Dock Scheduling is a fast, easy, low-touch, and API accessible solution for optimizing shipment pickup and delivery at facilities." Capabilities listed: "Shippers and carriers may schedule pickups and deliveries for one or more facilities; Manage shared calendars for facilities and docks; Schedule and reschedule appointments; Optimize facility capacity and dock staffing needs; Reduce the chance of shipments incurring detention fees; …Get data-driven insights on facility and carrier performance." (Early-access status noted.)
- **Object model (A, Tier-1):** Facility → Dock → Appointment. Docks carry "equipment type, capacity, and hours" and "load type restrictions or operating hours." Load types are first-class objects (list/create/update/delete). Availability is queryable (`list_facility_availability` — "What appointment slots are open at our Memphis facility tomorrow?").
- **Appointment fields (A, Tier-1):** name, reason (enum: PRE_LOAD / MAINTENANCE / FREIGHT / STAGING / OTHER), reference_id, start/end, is_all_day, matched_load_type_id, stop_id, carrier_name / carrier_contact / carrier_tenant_id, driver_id, appointment_type (enum: BY_APPOINTMENT_ONLY / FIRST_COME_FIRST_SERVE), delivery_type (enum: RECEIVING / SHIPPING), scheduled_resource_type (enum: FREIGHT_GENERAL / SHIPMENT / SERVICE / LEG) + scheduled_resource_metadata (e.g. ShipmentAppointmentScheduledResource or FreightAppointmentScheduledResource for off-platform freight), appointment_orders, notes, references.
- **Status enum (A, Tier-1):** UNSCHEDULED, SCHEDULED, RESCHEDULED, CANCELLED, ARRIVED, ARRIVED_LATE, DELAYED, DOCK_IN_USE, REJECTED, REQUESTED, NO_SHOW, COMPLETED, DOCK_IS_READY. Plus is_closed, rejected_reasons, declined_at/reasons/by_user_id, requested_at/by_user_id.
- **Confirmation number (A, Tier-1):** "Customer-facing confirmation number assigned once at creation and immutable for the life of the Appointment" ('SCH' + 6 alphanumerics).
- **Override semantics (A, Tier-1):** `override_availability_restrictions` — "Bypass any restrictions on appointment scheduling that would normally apply… facility hours of operation, holidays, max appointment capacity… will fail if the user does not have override permissions."
- **Scheduling model duality (A, Tier-1):** appointment_type documents both BY_APPOINTMENT_ONLY (default) and FIRST_COME_FIRST_SERVE — open scheduling is a supported mode, not just the absence of scheduling.
- **Appointment may exist unscheduled or dock-less (A, Tier-1):** status UNSCHEDULED exists; dock_id nullable ("or null if the appointment is not scheduled for any specific dock") — an appointment can be at the facility level without a specific door.
- **Day-of statuses (A, Tier-1):** the appointment lifecycle extends past confirmation into arrival (ARRIVED, ARRIVED_LATE), dock state (DOCK_IN_USE, DOCK_IS_READY), and completion (COMPLETED, NO_SHOW) — the appointment record bookends the visit even though the execution machinery is not this module's object world.

## Product C — YardView (dedicated YMS suite; dock scheduling module)

### Key observations

- **Dock scheduling module definition (A):** "Dock scheduling software is the essential tool for optimizing arrivals and departures… Our appointment scheduling module supports open dock scheduling and provides full control over appointments and dock capacity planning. Our system runs on proven, rule-based automation."
- **Key features of the module (A):** Flexible Scheduling for Inbound and Outbound Loads ("customizable time slots and capacity controls"); Post-Arrival Tracking ("goes beyond check-in… track trailers and containers after check-in… dwell time, milestones, and live driver detention"); Quick Schedule Adjustments ("add, change, or remove schedules, and adjust operating days or capacity as needed"); Real-Time API Integration ("keep schedules synced across your TMS, WMS, or ERP"); Third-Party and Carrier Self-Scheduling ("partners… book and edit appointments and receive automatic email confirmations… predefined rules to safeguard the system and control who can access what"); Appointment Compliance Tracking ("track on-time performance"); QR Code Access for Secure Check-In.
- **FAQ on scope (A):** "Supports manual entry or self-service carrier access; Integrates down to SKU-level load data, if needed; Allows custom schedules by building, dock, shipping, and receiving side; Adds post-arrival tracking…; Offers blind seal verification."
- **Vendor-drawn dock-vs-yard distinction (A, FAQ):** "Dock scheduling manages appointments and dock utilization. Yard management covers all yard activities. This includes everything from gate entry to trailer tracking and dock moves. YardView's YMS handles scheduling and yard actions in one platform."
- **Stand-alone option (A, pricing FAQ):** "Flexible options, including asset billing yards or a stand-alone appointment or dock scheduling solution."
- **Late/early arrivals (A, FAQ):** "lets teams adjust schedules and reassign docks to keep yard operations moving."
- **Reporting (A, FAQ):** "Dashboards and reports cover dock utilization, appointment compliance, dwell times, throughput, and more."
- **Pre-history named by vendor (A):** manual processes, phone calls and emails (carrier booking "reduces time spent on phone calls and emails").

## Product D — kaleris (enterprise YMS; dock appointments inside)

### Key observations

- **Dock appointments inside YMS (A):** "Automated dock management + appointment scheduling: Yard managers, warehouse teams, carriers, and suppliers can self-schedule inbound+outbound appointments. Balance loads, and decrease detention fees."
- **Intelligent Dock Scheduling positioning (A, blog):** "Go beyond simple 'door assignments.' Kaleris provides dock scheduling based on real-time door capability, capacity, and current labor availability."
- **Retail framing (A):** "Dock Scheduling capabilities, which are used as an inbound load planning tool by yard managers or trading partners."
- **Press-release definition of Appointment Scheduling (A):** "assigns a specific time for trucks or carriers to arrive for shipment loading or unloading. Facilities can use this feature to better manage resources, plan labor and equipment availability, and prevent long waiting times for drivers. The scheduling system also optimizes the flow of inbound and outbound shipments, reducing congestion."
- **Check-in coupling (A):** "As the YMS processes driver check-ins, it queues appointments to reduce gate congestion" — in the YMS-embedded packaging, the appointment feeds the gate/check-in machinery.

## Product E — Turvo Appointment Scheduling (collaborative TMS application)

### Key observations

- **Definition (A):** "Reduce the hassle of handling the dock — regardless of the number of bays, facilities, or warehouses in your network — with a single solution to automate appointment scheduling."
- **Full-context scheduling (A):** "See the schedule in the context of your network and shipment status, including order, shipment, customer, and carrier data synced to the appointment slot." — the appointment slot carries synchronized freight context from the surrounding TMS.
- **Truck status / arrival-departure (A):** "Capture truck status in real-time… See when drivers arrive and depart."
- **Self-service booking (A):** "Give your partners control over booking and appointment scheduling… allowing drivers and carriers to schedule appointments directly into warehouse calendars."
- **Custom appointment rules (A); collaborative scheduling for warehouse appointments (A); cross-tenant data sharing (A); identification of equipment needed for loading/unloading (A).**
- **Driver Fast-Pass (A, press release):** "automating the scheduling processes between carrier, driver, guard house and the dock door… provides drivers a Fast-Pass lane using the Turvo Driver Application."
- **Pre-history named by vendor (A, press release):** "Managers today use spreadsheets, phone calls, and emails for scheduling… Without visibility into truck ETAs or self-service booking capabilities for carriers, schedules can quickly become chaotic."

## Cross-product Comparison

| Structure | C3 Reservations | Shipwell | YardView | kaleris | Turvo | Evidence |
|---|---|---|---|---|---|---|
| Facility + dock doors held as schedulable capacity (hours, capacity, restrictions) | ✓ (capacity model, doors, per-site) | ✓ (facility→dock, equipment type, capacity, hours, load-type restrictions) | ✓ (custom schedules by building/dock/side, capacity controls) | ✓ (door capability, capacity, labor availability) | ✓ (bays, facilities, warehouses) | A, 5/5 |
| Appointment binding freight context to door + time window | ✓ (load types, POs, product descriptions in rules; reserved capacity + load content restriction) | ✓ (load type, orders, shipment/freight resource, carrier, driver, receiving/shipping) | ✓ (SKU-level load data; inbound/outbound) | ✓ (inbound load planning; trucks/carriers for loading/unloading) | ✓ (order/shipment/customer/carrier data synced to slot) | A, 5/5 |
| Appointment lifecycle with request/confirm/change states | ✓ (requests, auto-processing, exceptions queue, statuses) | ✓ (REQUESTED→SCHEDULED→RESCHEDULED/CANCELLED→…→COMPLETED enum) | ✓ (book/edit/confirm, email confirmations) | ✓ (self-schedule inbound+outbound) | ✓ (booking, confirmations, rescheduling) | A, 5/5 (status vocabulary verified only at Shipwell) |
| Facility-defined scheduling rules governing bookings | ✓ (rules engine: pallets/shift → load types/POs/product logic; auto-enforced) | ✓ (availability restrictions: hours, holidays, max capacity; override permission) | ✓ (predefined rules safeguarding self-scheduling; capacity controls) | ✓ (door capability/capacity/labor-based scheduling) | ✓ (custom appointment rules) | A, 5/5 |
| Carrier/supplier/driver self-service portal | ✓ (24/7 portal, own logins, kiosk) | ✓ ("shippers and carriers may schedule") | ✓ (third-party/carrier self-scheduling) | ✓ (carriers and suppliers self-schedule) | ✓ (partners book; driver app Fast-Pass) | A, 5/5 → common |
| Automated notifications/confirmations | ✓ (every action triggers email; customizable content/language) | ✓ (implied by API + "low-touch") | ✓ (automatic email confirmations) | not observed explicitly | ✓ (appointment confirmations in real time) | A, 4/5 → common |
| Scheduler calendar UI (drag-and-drop) | ✓ | (API-first; UI not documented) | ✓ (implied: adjust schedules/reassign docks) | ✓ (Whiteboard hub; graphical dock view) | ✓ (visual schedule in network context) | A, 4/5 → common |
| Compliance tracking / carrier scorecards | ✓ (vendor report cards, audit) | ✓ (facility and carrier performance insights) | ✓ (appointment compliance tracking) | not observed | not observed | A, 3/5 → common |
| Exception handling (queue for non-fitting requests) | ✓ (prioritized task queue) | ✓ (REJECTED status + declined reasons; override) | ✓ (late/early adjustment flows) | not observed | not observed | A, 3/5 → common |
| Multi-site / network scheduling | ✓ (unlimited sites, time zones, central/decentral) | ✓ (one or more facilities) | ✓ (single warehouse → enterprise networks) | ✓ (multi-facility) | ✓ (network-wide, cross-tenant) | A, 5/5 → common |
| Documents attached to appointments | ✓ (packing slips, BOLs) | ✓ (references; appointment_orders) | ✓ (SKU-level load data) | not observed | ✓ (mobile document sharing) | A, 4/5 → common |
| Integration with WMS/TMS/ERP | ✓ (APIs; but works standalone) | ✓ (native TMS context; stop_id) | ✓ (TMS/WMS/ERP sync) | ✓ (web API to WMS) | ✓ (third-party systems; native TMS) | A, 5/5 → common |
| Rule-based duration computation (unload-time estimation) | ✓ (natural-language rule system) | not observed (load types exist; duration logic not documented) | not observed | implied (labor planning) | ✓ (equipment identification; not duration rules) | A, C3-led → optional |
| Day-of statuses on the appointment (arrived/dock/completed) | statuses mentioned ("appointment statuses, dwell times") | ✓ (ARRIVED, DOCK_IN_USE, COMPLETED, NO_SHOW…) | ✓ (post-arrival tracking, milestones) | ✓ (check-in queues appointments) | ✓ (truck status, arrival/departure updates) | A, 5/5 — depth varies; execution machinery NOT in-type |
| Outbound scheduling supported | ✓ (FAQ) | ✓ (SHIPPING enum) | ✓ (inbound and outbound) | ✓ (inbound+outbound) | ✓ (inbound and outbound visibility) | A, 5/5 → common |
| Open / first-come-first-serve mode | not observed (anti-FIFO positioning) | ✓ (appointment_type enum) | ✓ ("open dock scheduling") | not observed | not observed | A, 2/5 → variant |

## Canonical Model

### L0 — Defining Invariant (deliberately minimal; jointly held)

1. **The dock/door-time capacity of record.** The facility and its dock doors — with operating hours, capacity, and load-type/equipment constraints — held as bookable time capacity: the schedule of record against which freight arrivals and departures are planned. Remove → a generic appointment calendar with no dock semantics, or a freight plan with nothing to book against.
2. **The appointment as unit of record.** A persistent, lifecycle-managed binding of a load/shipment (freight context: load type, orders/POs, carrier/supplier, direction receiving/shipping) to a door and a time window at a facility — requested, confirmed, rescheduled, cancelled, and completed as tracked states. Remove → an empty door calendar, or a freight plan with no reservations.
3. **Facility-defined scheduling rules governing the loop with external freight parties.** Appointments are made for external carriers/suppliers arriving at (or departing from) the facility, evaluated against the facility's own rules — capacity limits, load-type/door restrictions, lead times, priorities — with confirmations, declines, and change notifications keeping the parties synchronized. Remove → an open parking lot with no scheduling discipline (the "first come, first serve" state the products position against), or an internal calendar with no external freight semantics.

Jointly-held is load-bearing:
- 1 alone = a facility hours page / empty door grid.
- 2 without 1 = a visit list with nothing to book against.
- 3 without 1+2 = a portal with no schedule.
- 1+2 without 3 = a bare calendar that accepts anything (loses the scheduling discipline that defines the Type).
- 2+3 without 1 = rule-governed requests with no capacity of record.
- 1+3 without 2 = capacity model nobody books.

### L1 — Common Mature Structure (very common in mature products; not definitional)

- Carrier/supplier/driver self-service portals (book/edit/cancel, own logins, 24/7 availability views; kiosks in some products).
- Automated event-triggered notifications and confirmations (email; customizable content and language).
- Scheduler calendar surfaces (drag-and-drop, real-time updates, availability views).
- Appointment compliance tracking and carrier scorecards / vendor report cards; auditable record of who booked what and whether they honored it.
- Exception queues for requests that do not fit rules; late/no-show handling; dock reassignment for early/late arrivals.
- Multi-site/network scheduling with per-site capacity, time zones, and access control; centralized or decentralized operation.
- Documents attached to appointments (BOLs, packing slips); SKU/PO-level load data.
- Integration with WMS/TMS/ERP so appointments carry shipment/order context (or function standalone, product-dependent).
- Load-type-aware duration estimation (rule-based unload-time computation) for labor forecasting.
- Detention/dwell exposure tied to appointment adherence.
- Outbound (shipping) as well as inbound (receiving) scheduling.

### L2 — Variant / Optional Structure

- Packaging: standalone product (C3 Reservations) ↔ YMS module (YardView, kaleris) ↔ TMS module/application (Shipwell, Turvo) ↔ WMS-embedded (per vendor commentary; suite pole under-observed).
- Direction scope: inbound-only (the retail/supplier-delivery classic; kaleris frames dock scheduling as "an inbound load planning tool") ↔ inbound + outbound.
- Scheduling model: by-appointment-only ↔ open/first-come-first-serve windows (documented in Shipwell's appointment_type enum and YardView's "open dock scheduling").
- Automation posture: fully automated self-service ↔ clerk-mediated manual entry ↔ tiered automation (C3: top-tier carriers auto-processed, lower tier hands-on).
- Day-of depth: appointment record ends at confirmation vs carries arrival/dock/completion statuses (Shipwell enum; YardView post-arrival tracking; Turvo truck status) — packaging-dependent; the execution machinery (trailer location of record, yard moves, gate operation) is out-of-type in all packagings.
- Industry tuning: retail/grocery DCs, 3PL, manufacturing plants, parcel/post, temperature-controlled freight.

### L3 — Vendor-specific (research notes only)

- C3 Reservations: natural-language rule engine; configurable expiration freeing unused reserved slots; reserved physical capacity + load-content restriction; prioritized exception task queue; self-serve kiosk; multi-timezone unlimited sites; vendor report cards; "10+ dock doors and 100+ appointments/day" marketing threshold; ROI calculator.
- Shipwell: immutable 'SCH'-prefixed confirmation numbers; MCP tool surface; early-access status; appointment reasons enum (PRE_LOAD/MAINTENANCE/FREIGHT/STAGING/OTHER); scheduled_resource polymorphism (SHIPMENT/SERVICE/LEG/off-platform freight); override_availability_restrictions permission gate.
- YardView: blind seal verification; QR-code check-in; "up to 95% reduction in detention fees" and "50% faster spotting" marketing claims; 25+ years positioning; stand-alone dock scheduling pricing option.
- kaleris: "Intelligent Dock Scheduling" branding (real-time door capability/capacity/labor); Whiteboard central hub; driver precheck-in app queuing appointments at the gate; 12-week implementation claim.
- Turvo: Fast-Pass driver lane; cross-tenant data sharing; visual yard maps; messenger; customer outcome claims ($62M overtime savings, 90% email reduction — marketing, research notes only).

### Rejected Findings (candidates examined and not promoted)

- **Carrier self-service portal as definitional** — rejected: the analog form (carrier phones, clerk enters the appointment) satisfies the core; vendors name the phone/email/spreadsheet pre-history themselves (Turvo, C3). The portal is the modern channel, not the Type.
- **Automation/auto-confirmation as definitional** — rejected: C3 explicitly documents automation level as customizable from fully manual to fully automatic.
- **Rule-based duration computation as definitional** — rejected: fixed/average durations are the simpler documented alternative (C3's own framing).
- **Day-of arrival tracking as definitional** — rejected: depth varies by packaging; the appointment record may bookend the visit, but the execution machinery (trailer location, yard moves, gate) is the YMS's object world in every sampled product.
- **Multi-site as definitional** — rejected: single-site operation is explicitly in-type (C3 FAQ: "from a single warehouse with just a few docks").
- **Detention machinery as definitional** — rejected: it is an economics layer on appointment adherence and dwell; present as module/insight, not structure.
- **Scorecarding as definitional** — rejected: common (3/5) but a reporting layer on the compliance record.
- **"Dock management" (door master data, door assignment/sequencing) as the center** — rejected: door configuration exists in all products, but door *assignment/sequencing at execution time* is the YMS's job (C3's own boundary analysis); the scheduling system's center is the appointment against capacity.

## Boundary Findings

1. **vs Yard Management System — DISCHARGES the YMS pass's pre-hung flag; RATIFIED keep-both with the arrival-gate seam.** From this side, the sampled products confirm the seam independently: C3 (sells both) — dock scheduling "governs everything that happens before the truck arrives… Dock scheduling's job effectively ends at the gate"; unit of work = the appointment; horizon = days to weeks. YardView's own FAQ — "Dock scheduling manages appointments and dock utilization. Yard management covers all yard activities… from gate entry to trailer tracking and dock moves." kaleris ships dock appointments inside the YMS but as a distinct capability ("assigns a specific time for trucks or carriers to arrive"). Nuance recorded: the appointment record may carry day-of statuses (Shipwell: ARRIVED/DOCK_IN_USE/COMPLETED; YardView: post-arrival tracking; Turvo: truck status) — the record bookends the visit, but the execution machinery (trailer location of record, directed yard moves, gate operation) is the YMS's object world, not this Type's. Neither subsumes the other: a scheduling system has no execution picture of the yard (C3: "the plan on the screen no longer resembles what is happening outside the fence"), and a YMS "can execute brilliantly against a bad plan." Frequently bundled (YardView, kaleris) or sold as siblings (C3 Reservations / C3 Yard); drop-and-hook breaks the appointment-trailer coupling (C3), which is why the two Types cannot merge.
2. **vs Warehouse Management System — DISCHARGES the WMS pass's seam; RATIFIED no merge.** WMS = goods handling inside the building (receiving, putaway, picking); dock scheduling = the arrival/departure plan for the doors. The handoff is concrete: the appointment tells the warehouse when freight will arrive and what it contains (SKU/PO-level data syncs are documented); once goods are received inside, WMS territory begins. WMS dock-appointment modules exist as packaging (vendor commentary), not as a different structure.
3. **vs Transportation Management System — DISCHARGES the TMS pass's seam (8, dock half); RATIFIED no merge.** Dock scheduling ships as TMS modules (Shipwell Dock Scheduling; Turvo Appointment Scheduling inside the TMS cloud) and as standalone products (C3 Reservations); the TMS plans and executes transportation between locations, while dock scheduling governs the facility-side arrival/departure schedule against door capacity. Turvo's own positioning — appointment scheduling as an application within the collaboration cloud, with shipment context synced in — shows the module relationship without subsumption.
4. **vs generic Appointment Scheduling Application (§03.09)** — same abstract shape (resource + time slot + booking) but a different object world: freight logistics (loads/shipments/POs, load types, carriers/suppliers, receiving/shipping directions, dock doors) vs personal/service appointments; B2B multi-party coordination under facility rules vs consumer/service booking. Different users, rules, and integrations. Keep-both; record for that pass's awareness.
5. **vs Delivery Scheduling Platform (§18)** — delivery scheduling is carrier/shipper-side scheduling of deliveries to recipients; dock scheduling is facility-side scheduling of arrivals at the facility's own docks. A delivery appointment at a DC is the meeting point of both; the object worlds differ (route/stop vs door/slot). Adjacent, keep-both.
6. **vs Resource Calendar (§03.08)** — a resource calendar allocates shared resources over time generically; dock scheduling is the freight-specific realization with load semantics, external multi-party loop, and facility rules. The dock scheduling platform is best understood as a domain-specific scheduling system, not an instance of the generic Type.
7. **vs Port Terminal Operating System (§18)** — cross-mode analog (berth windows/vessel calls vs dock doors/truck appointments), already noted by the YMS pass; convergence only at intermodal container yards.
8. **vs Employee Scheduling / Agent Scheduling** — different resource world (people/shifts vs freight/doors); no overlap beyond the shared word "scheduling."

## Historical / Market-Sample Check

- Vendors name the pre-history themselves: "spreadsheets, phone calls, and emails" (Turvo), "first come, first serve" operations (C3's positioning), rules "found in a disorganized binder or the scheduler's head" (C3), "phone calls and emails" for booking (YardView). The analog dock office — an appointment book / whiteboard grid of doors and time slots, carrier requests arriving by phone/fax/email, a clerk who confirms against rules held in their head or a binder, confirmation given by phone — satisfies all three L0 legs at analog level: capacity of record (the book/grid), appointments (entries binding carrier+load to door+time), rule-governed loop (clerk evaluates requests against the facility's rules and confirms). The category digitized this office; the definition should not require its digital replacements (portals, kiosks, rule engines, automated notifications).
- The dedicated market dates to around 2000 (C3 incorporated June 2000, "focused on providing yard management and dock scheduling solutions"; YardView since 1998 per vendor statements), with earlier dock-appointment functions living inside WMS/ERP and the phone/fax era before that. Nothing in the L0 depends on that era's implementation: no cloud, no portals, no automation, no APIs.
- Regional check: C3 documents UK/EU operations (British retailers program; bilingual platform); the L0 is vocabulary-neutral ("carrier/supplier", "door", "appointment"). Single-site, multi-site, inbound-only, and inbound+outbound realizations all satisfy the core.
- Mode check: the Type generalizes beyond road freight docks in principle (any facility receiving/sending freight by appointment), but the sampled market is road-freight DC-centric; the L0 is written mode-neutrally (facility + doors + freight appointments).

## Uncertainties

1. **No Tier-1 UI help-center reached for C3, YardView, kaleris, or Turvo.** All non-Shipwell observations are Tier-2 vendor documentation (product/tour/FAQ/blog). Exact UI state machines, default lead-time/cutoff values, permission models, and numeric limits are not asserted anywhere in the final document.
2. **Status vocabulary generalized only from Shipwell** (the sole Tier-1 source). Other products' exact status sets are not documented at reachable depth; the final document describes the lifecycle conceptually and notes that exact labels vary.
3. **Suite-embedded pole (SAP TM dock appointments, Blue Yonder, Manhattan, Oracle TM) under-observed** — the WMS/TMS-embedded claim rests on vendor commentary and the two prior passes, not on fetched suite documentation.
4. **Whether detention-fee invoicing (vs tracking/exposure) is in-Type** is unclear — held as optional machinery.
5. **Open/first-come-first-serve mode** documented at only two products (Shipwell enum, YardView "open dock scheduling"); held as variant, not common.
6. **Whether an appointment without a specific door (facility-level only, Shipwell's nullable dock_id) is common** across products is unknown — held as a documented possibility at one product.

## Final Synthesis

A Dock Scheduling Platform is the facility-side scheduling system of record for freight arrivals and departures. Its defining core is three jointly-held structures: (1) the dock/door-time capacity of record — the facility and its dock doors with operating hours, capacity, and load-type constraints held as bookable schedule; (2) the appointment — a persistent, lifecycle-managed binding of a load/shipment (with carrier/supplier and receiving/shipping direction) to a door and time window; (3) facility-defined scheduling rules governing the loop with external freight parties — requests evaluated against capacity, load-type, and lead-time rules, confirmed or declined, with notifications keeping facility and partners synchronized.

Around that core, mature products add carrier self-service portals, automated notifications, scheduler calendars, compliance tracking and scorecards, exception queues, multi-site operation, document attachment, WMS/TMS/ERP integration, and rule-based duration estimation. Packaging (standalone vs YMS/TMS-embedded), direction scope, scheduling model, and automation posture are variants.

The Type's identity comes from its slice of the flow: it governs the plan before the truck arrives — "when should each carrier show up, and at which door?" — and its job effectively ends at the gate, where the Yard Management System takes over execution. That arrival-gate seam, drawn independently by the vendors on both sides of it, is what keeps Dock Scheduling and Yard Management separate Types that are frequently bundled but never subsume each other.
