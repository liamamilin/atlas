# Research Notes — Dispatch Management

Research date: 2026-09-07
Slug: dispatch-management
Directory leaf: Dispatch Management (§18 Transportation, Mobility & Logistics)

---

## Research Goal

Understand what "Dispatch Management" software actually is as an Application Type: the core objects it manages, the dispatch workflow it supports, the surfaces its users operate, the states and rules that govern assignment, and — critically — its boundary against the densest seam family in the directory (§18: Taxi/Towing Dispatch, Courier Management, Trucking/TMS, Route Optimization, Last-mile Delivery, Driver Management, FMS) and against §24 Computer-aided Dispatch.

## Prior-pass context (sibling seams already recorded)

Three earlier passes constrain this one:

- **computer-aided-dispatch-cad** (processed): L0 = incident + unit real-time status + assignment + live picture, emergency semantics definitional. Its Boundary Findings table lists "Dispatch Management (§18, freight) | structural sibling, logistics | Load/freight assignment over commercial logistics; no incident, priority, or response semantics."
- **courier-management-platform** (processed): L0 = courier order + dispatch to own courier workforce + recorded execution ending in POD + courier-business frame (customer accounts, contracted rates, billing). Its notes characterize this leaf as "Dispatch Management — generic field-workforce dispatch across industries." Its STATUS note flags the §18 delivery cluster as "the densest seam family" and holds the seam on tenant identity (operator business frame vs shipper-side orchestration), recommending joint review when last-mile-delivery-platform is processed.
- **fleet-management-system** (processed): dispatch appears in sampled FMS products only as an optional module (Samsara Dispatch menu; Motive driver-app dispatch; absent in Fleetio); "Job-dispatch-to-field-workers is its own Type; its presence in an FMS is a bundle." Flags a joint pass with this leaf.
- **delivery-scheduling-platform** (processed): L0 = scheduled delivery + delivery schedule (time-grid of commitments) + availability structure; execution hand-off to routing/driver apps is NOT definitional there.
- **construction-materials-management** (processed): watch-item — the bulk-hauling pole (dispatch boards, loads, GPS cycle tracking, e-ticketing) is documented there because the object of record is material quantity against orders/jobs; "when trucks and carriers become the object of record, it is a TMS/dispatch." Joint seam review requested for this pass.

Reconciliation needed: CAD's pass read this leaf as "(freight)"; the courier pass read it as "generic field-workforce dispatch." This pass decides.

## Initial Boundary (pre-research hypothesis)

- Dispatch Management = the dispatcher's operational application: incoming work (loads/jobs/orders/service calls) + dispatchable mobile resources (drivers/vehicles/crews/technicians) with live availability + the assignment act + a live board, worked to completion.
- NOT definitional: emergency incident semantics (CAD), courier order/rating/billing frame (Courier Management), route optimization (its own leaf), vehicle health/telematics (FMS), freight settlement/EDI/compliance (TMS/Trucking), POD as contractual closure (courier/delivery leaves), customer-facing delivery orchestration (Last-mile/On-demand).
- Directory placement in §18 (between Route Optimization Platform and Driver Management) suggests transportation center of gravity, but market evidence shows the same machinery across field services → treat industries as variants, hold "generic machinery" as the Type.
- Historical check required: radio-and-paper dispatch era (check calls, whiteboards) must satisfy the definition (Truckbase's own blog documents the pre-software baseline).

## Research Questions

1. What enters the dispatch queue, and what is the unit of work called/structured per industry (load / job / order / stop)?
2. How are dispatchable resources modeled — people, vehicles, or person+vehicle pairs? What availability state is maintained?
3. How does assignment happen — manual, assisted (recommendation), automated? What is the human's role?
4. What statuses do work items and resources carry, and who updates them (office vs field)?
5. What surfaces exist (board/calendar/whiteboard/map/list, field mobile, customer notifications, reporting)?
6. Which machinery is adjacent-but-not-defining: route optimization, GPS/ELD tracking, customer notifications, POD, billing/settlement, EDI?
7. How are exceptions handled (last-minute changes, breakdowns, delays, reassignment)?
8. What packaging exists (standalone dispatch product vs module of TMS/FSM/fleet platform)? What scale range?
9. What are the boundaries vs CAD, courier management, TMS/trucking, route optimization, FMS, delivery scheduling, employee scheduling, last-mile platforms?

## Representative Products

Selected for market representation + different product philosophy + different customer tier + spanning the industry poles of the Type:

| Product | Pole | Tier | Philosophy |
|---|---|---|---|
| Truckbase | trucking dispatch (asset-based carriers) | SMB–mid ("turnkey at 5 trucks... powerful enough for 50") | dispatch-centric TMS; text-first, app-optional; optimization NOT shipped |
| Elite EXTRA Routing & Dispatch | cross-industry last-mile dispatch & routing (auto parts, distributors, couriers) | mid-market | dispatch+routing core with optimization engine, driver app, customer notifications; suite modules (Delivery Network, Returns) |
| Samsara (Fleet Telematics → Routing & Dispatch) | dispatch as module of a fleet/telematics platform | enterprise | dispatch fused with telematics: route planning + execution + navigation on one data platform |
| Workiz | home-services field dispatch (HVAC/plumbing/locksmith/junk removal) | SMB | FSM suite where dispatch is a stage of the lead-to-payment engine; AI auto-dispatch marketed |

Rejected/considered: ServiceTitan and Verizon Connect Dispatch (intended poles: enterprise FSM dispatch board; fleet-carrier module) — unreachable (404/403 twice each; see Source-access Limitations). Jobber — 403 once, abandoned. Towbook/CXT/e-Courier excluded: they belong to the Towing Dispatch / Courier Management leaves.

## Sources

Fetched 2026-09-07 (all official vendor surfaces):

1. Truckbase homepage — https://truckbase.com/
2. Truckbase "Trucking Dispatch Software" product page — https://truckbase.com/trucking-dispatch-software
3. Truckbase blog articles on the dispatch page ("Truck Dispatchers: The Vital Role for Carriers", "How to eliminate check calls...", "Top 10 Truck Dispatcher KPIs") — fetched as part of page 2
4. Elite EXTRA homepage — https://www.eliteextra.com/
5. Elite EXTRA "Routing & Dispatch" product page — https://eliteextra.com/routing-and-dispatch/
6. Samsara Fleet Telematics (fleet) page — https://www.samsara.com/fleet
7. Samsara "Routing & Dispatch" product page — https://www.samsara.com/products/telematics/routing
8. Samsara guide "7 Key Things to Look For When Selecting Your Dispatch Software" — https://www.samsara.com/guides/dispatch-software (only the key-takeaways line rendered; body not reachable)
9. Workiz homepage — https://www.workiz.com/
10. Workiz "Job Scheduling Software" feature page (incl. scheduling/dispatch FAQ) — https://www.workiz.com/features/job-scheduling/

### Source-access Limitations

- ServiceTitan — https://www.servicetitan.com/software/dispatch-software and /features/dispatch → 404 ×2; abandoned. Enterprise-FSM dispatch board unverified this pass.
- Verizon Connect — /solutions/dispatch-software/ and /products/dispatch/ → 404 ×2; abandoned.
- Jobber — https://www.getjobber.com/ → 403; abandoned.
- Samsara guide article body did not render (nav chrome only); only the takeaway sentence usable.
- Vendor help centers (Truckbase, Elite EXTRA, Workiz help.workiz.com, Samsara kb.samsara.com) not drilled this pass; observations rest on Tier-2 official product/marketing pages. Consequence: exact status vocabularies, numeric limits, timing windows, and plan gating are NOT asserted anywhere; claims are calibrated to the fetched pages.

---

## Product A — Truckbase

Source: truckbase.com homepage + /trucking-dispatch-software (Tier 2). Evidence layer: A.

### Key observations

- Self-labeling: "Trucking dispatch software"; "Truckbase is a dispatch-centric TMS for small to mid-sized carriers." Dispatch is the flagship module of a TMS suite (dispatch, ELD/truck tracking, invoicing, customer portal, driver settlement, intelligence/reporting).
- Unit of work: the **load** ("organize load, documents, and invoices"; "load history"; "Track all load information within a single calendar").
- Intake: "Automate load-building and dispatch with our AI-powered PDF importer" (rate confirmations imported from PDF).
- Board: "Get an overview of your calendar, and schedule loads in one single screen"; "Has all load and driver schedules on one calendar for easy access"; "complete visibility over your drivers' schedules."
- Assignment + transmission: "Send your drivers dispatch details via text or email all with a single click"; "text-based dispatch" — drivers need no app ("text-based dispatch makes it easy to instantly communicate with your drivers"); optional driver logins/mobile app to "view all their loads in one place... update information or attach documents"; integrated mobile BOL scanning.
- Status loop: "Keep track of a load's progress with status updates between driver & dispatcher."
- Resource availability: FAQ — "Truckbase's truck dispatch software uses driver availability, ELD integrations, and intuitive load planning tools to improve route planning and efficiency."
- Tracking: 30+ ELD integrations; "real-time load and truck visibility"; "eliminate check calls"; automated customer updates; "if they need to rest to remain compliant, they can be alerted automatically" (HOS-aware alerting). Live tracking links shareable to customers; customer portal.
- Broker/customer side: "Email your broker updates & BOLs instantly"; EDI to customer TMS ("automated data flows... load acceptance, tracking, and invoicing").
- Dispatcher role (vendor blog): route planning, driver communication, load management, compliance/safety monitoring (hours, rest), problem-solving ("vehicle breakdowns, traffic delays, or unexpected route changes"). Dispatcher KPIs: load acceptance rate, on-time delivery, driver utilization, load turnaround.
- Check-call era as the documented pre-software baseline: "Twenty years ago, this would all have to be done manually... the only way to solve it would be to add dispatchers." Historical anchor for L0-without-GPS.
- Routing/optimization: listed as "COMING SOON" (PC*Miler/Google Maps options) — a dispatch-centric product WITHOUT native optimization. Boundary evidence vs Route Optimization Platform.
- Scale/segment: "turnkey at 5 trucks and powerful enough for 50 trucks"; long haul, regional, heavy haul & specialized, LTL & partial, intermodal.

## Product B — Elite EXTRA (Routing & Dispatch)

Source: eliteextra.com homepage + /routing-and-dispatch (Tier 2). Evidence layer: A.

### Key observations

- Self-labeling: "Last Mile Logistics Software"; suite = Routing & Dispatch + Delivery Network (third-party dispatch) + Returns Automation (an Epicor company).
- Documented dispatch workflow, six named stages: **Integrate** ("orders are automatically and efficiently passed into the dispatch workflow" from ERP/POS/eCommerce) → **Route** ("optimization engine that works according to your rules... efficiency, time windows, customer priority") → **Dispatch** ("Dispatch routes and orders to drivers within your fleet or... drivers from crowdsourced and courier fleets") → **Inform** ("email and text notifications complete with a tracking page... ETAs and order updates") → **Fulfill** ("EXTRA Driver mobile app, guiding them through each task from dispatch to completion... signatures, photos, and time stamps") → **Manage** ("manager's dashboard, route whiteboard, and... robust reporting engine").
- Feature list: automated routing & dispatching, real-time GPS tracking, customer ETA notifications, photo & signature capture, driver mobile app, route scheduling, robust reporting suite.
- Work items: orders and routes (stops); customers are the shipper/distributor's customers (auto-parts dealers, supply houses).
- Resource model: "drivers within your fleet" OR third-party/couriersourced fleets via Delivery Network — resource roster can span internal + external fleets; "Compare delivery times and rates of crowdsourced and courier fleets... and dispatch to the fleet that works best."
- Returns Automation integration: "automatically dispatch a driver to a pickup request right within one platform" — same dispatch machinery applied to reverse logistics.
- Fleet Telematics integration (separate product): "communicate vehicle alerts, maintenance schedules and driver management data between Routing & Dispatch and our Fleet Telematics solution" — telematics lives outside the dispatch product.
- Industries (nav): courier, pharmacy, auto parts, water, building materials, appliance/electronics distribution — cross-industry evidence for the same machinery.
- "325,000+ users since 2008"; updates every 8 weeks; SaaS.

## Product C — Samsara (Routing & Dispatch within Fleet Telematics)

Source: samsara.com /fleet + /products/telematics/routing + /guides/dispatch-software (Tier 2). Evidence layer: A.

### Key observations

- Vendor's generic definition (FAQ): "Routing and dispatch software is used to plan, optimize, and manage vehicle routes and **driver assignments**, particularly for last-mile deliveries and other logistics operations. It helps streamline operations by providing tools for automated and optimized routes, **driver dispatch**, and real-time tracking of deliveries or service tasks."
- Guide takeaway: "Dispatch software is one of the primary tools that fleet managers and dispatchers rely on to ensure that drivers are running efficient routes to keep your customers happy."
- Product structure: **Route Planning** ("Generate smarter, optimized routes—built for your operation's real-world constraints") + **Route Execution** ("Dispatch drivers, monitor route performance, and manage exceptions in real time") + Commercial Navigation (in-cab, truck-restriction-aware turn-by-turn).
- Dispatch-and-operations role: "Give dispatch and operations full visibility into driver location, route, performance, and fuel usage."
- Driver↔dispatch sync: "Keep drivers and dispatch in sync with consistent ground truth, ETAs, and navigation paths"; Driver App unifies navigation + customer notifications + HOS.
- Platform context: dispatch sits inside the telematics platform — same data spine as GPS tracking, diagnostics, fuel, maintenance; integrations with TMS/ERP (App Marketplace, 300+ integrations). Confirms the "dispatch as module of fleet platform" realization and the FMS seam.
- Customer proof: Harris Ranch Beef route planners "3-4 hours a day planning routes. Now... 20-30 minutes"; Mohawk route planning savings.
- Optimization-forward philosophy: optimization and planning lead the page; dispatch is the execution stage of the route lifecycle.

## Product D — Workiz

Source: workiz.com homepage + /features/job-scheduling (Tier 2). Evidence layer: A.

### Key observations

- Self-labeling: "AI software for home service pros"; growth-engine framing names **Dispatch** as a stage: "Dispatch — The right tech on every job, automatically."
- Board: "Dispatch the right tech to every job with a simple drag-and-drop calendar. See each tech's route and easily rearrange appointment times to minimize windshield time."
- Work item: the **job** / appointment (created from calls/leads; "Job created" event shown in the hero flow).
- Assignment inputs: "Assign jobs to the most suitable technicians based on **skills, location, and availability**" (FAQ); AI: "Jessica, Workiz's smart AI assistant, automates job assignments by analyzing technician availability, location, and skill set to ensure the right person is dispatched for each job"; "Genius Answering... talks to clients, books jobs, and **dispatches the right tech without any human intervention**."
- Live awareness: "When you get a call, your dispatcher can easily see **which tech is nearby** and alert them about the last minute change" — proximity-aware, real-time reassignment; "Easily set up automations that let your pre-scheduled clients know you'll be late."
- Field side: mobile app (schedules, job details, customer info; iOS/Android); "real-time updates on job progress, technician location."
- Customer side: automated notifications — confirmations, reminders, running-late alerts via SMS/email.
- Resource: the technician (person); vehicles implicit (routes, windshield time); integration with telematics provider (Linxup) for vehicle tracking.
- Business frame around dispatch: estimates, pricebook, invoicing, payments, phone system, marketing — the FSM frame; dispatch is one stage.
- Segment: SMB home services, 50+ industries (HVAC, plumbing, electrical, locksmith, appliance repair, garage doors, junk removal...).

---

## Cross-product Comparison

| Dimension | Truckbase (trucking) | Elite EXTRA (cross-industry last mile) | Samsara (fleet platform module) | Workiz (home services) |
|---|---|---|---|---|
| Unit of work | load (with stops, BOL) | order / route (stops) | route + deliveries/service tasks | job / appointment |
| Resource | driver (+ truck via ELD) | driver within fleet OR crowdsourced/courier fleet | driver (+ vehicle from telematics) | technician (+ vehicle implicit) |
| Availability state | "driver availability" feeds dispatch | fleet assignment + third-party capacity comparison | "driver availability" in optimization inputs | "technician availability, location, skill set" |
| Assignment | dispatcher builds/schedules loads; text/email/app transmission | automated routing & dispatching; dispatch to chosen fleet | "Dispatch drivers" as route-execution stage; optimization-assisted | drag-drop manual; AI-assisted; auto-dispatch marketed |
| Work status loop | "status updates between driver & dispatcher" | driver app "from dispatch to completion"; signatures/photos/time stamps | monitor route performance, manage exceptions in real time | "real-time updates on job progress, technician location" |
| Live board | single calendar (loads × drivers) | manager's dashboard + route whiteboard | map/telematics dashboard | drag-drop calendar + map/routes |
| Location feed | 30+ ELD integrations; truck tracking | real-time GPS tracking | native telematics (per-second GPS) | technician location in app; Linxup integration |
| Route optimization | NOT shipped ("COMING SOON") | optimization engine by rules | route planning/optimization is the lead capability | route-planning feature; "minimize windshield time"; AI time-finding |
| Customer notifications | automated updates, live tracking links, customer portal, EDI status | email/text notifications + branded tracking page + ETAs | Driver App sends customer notifications; live order tracking | confirmations/reminders/running-late via SMS/email |
| Field surface | text/email + optional mobile-friendly driver app | EXTRA Driver mobile app | Samsara Driver App (nav + HOS + tasks) | Workiz mobile app |
| Exceptions | dispatcher problem-solver: breakdowns, delays, route changes; HOS alerts | exceptions managed in real time (route execution) | "manage exceptions in real time" | emergency calls; see nearby tech; alert + notify customer |
| Business frame around dispatch | TMS frame: invoicing, driver settlement, EDI, factoring | last-mile suite: Delivery Network (3rd-party), Returns | telematics platform: safety, maintenance, fuel, compliance | FSM frame: estimates, payments, marketing, phone |
| Packaging | dispatch-centric TMS (standalone suite) | standalone dispatch product + optional suite modules | module of fleet-telematics platform | stage/module of FSM suite |
| Tier | SMB–mid carriers (5–50+ trucks) | mid-market, multi-warehouse | enterprise | SMB (120K+ pros claimed) |

### Layer-B findings (cross-product commonality, 4/4 unless noted)

1. Work exists as discrete, assignable items — each with location(s)/destination and time expectations — awaiting or undergoing assignment (loads / orders+routes / routes+tasks / jobs).
2. A roster of dispatchable resources is maintained with an availability state; assignment consumes availability (drivers with trucks, technicians, mixed internal/external fleets).
3. The assignment act is the managed transition — unassigned work becomes assigned work — executed manually, with assistance (availability/proximity/skill/optimization), or automatically; a dispatcher role exists in all four framings.
4. Assignment is transmitted to the field (text/email, mobile app), and field-side progress flows back (status updates, arrival/en-route events, photos/signatures/time stamps in the delivery flavor).
5. A live operational surface (calendar / whiteboard / dashboard / map) presents work × resources × progress as current state.
6. Real-time location awareness of resources is common (ELD/GPS/telematics/native app), but implementation varies from native (Samsara) to integration (Truckbase, Elite EXTRA, Workiz).
7. Exceptions are a designed concern: last-minute/emergency changes, delays, breakdowns, reassignment to nearby/available resources.
8. Customer-facing notification/tracking is common (3/4 strongly: Elite EXTRA, Samsara, Workiz, Truckbase) but intensity varies by industry.
9. Dispatch is packaged three ways: standalone dispatch-centric suite, module of a fleet/telematics platform, stage/module of a field-service business suite — the machinery is the same; the surrounding business frame differs.
10. Route optimization is common but NOT universal (Truckbase ships none) — dispatch-first and optimization-first are both viable philosophies.
11. Reporting/KPIs (utilization, on-time performance) appear in mature products.

### Layer-C canonical inference

The Type is best modeled as: **the real-time management of the assignment relationship between a queue of work and a roster of available mobile resources — assignment, transmission, status return, and exception handling — worked on a live operational picture until each item completes.** The work item's industry semantics (freight, delivery, service, ride) and the surrounding business frame (settlement, billing, compliance, telematics) are variant layers, not the Type.

---

## Abstraction Hierarchy

### L0 — Defining Invariant (minimal)

1. **A queue of dispatchable work** — discrete units of service work (load / order / job / route), each carrying where it must happen and when, held in unassigned state and tracked to completion.
2. **A roster of dispatchable resources with live availability** — the mobile workers (with their vehicles/equipment where applicable) who execute the work; the system maintains who/what is available now.
3. **The assignment act** — binding work item(s) to resource(s); unassigned → assigned is the managed transition; manual, assisted, or automated.
4. **The live dispatch picture** — work × resources × progress maintained and presented as current state (board/calendar/map/whiteboard), the shared surface the dispatcher works from.

Real-time posture is definitional (consistent with the CAD sibling pass): dispatch answers "who is available now, what is unassigned now."

Removal tests: remove the work queue → vehicle/asset tracking (FMS/telematics territory); remove resource availability → an order/job log, not dispatch; remove the assignment act → a schedule or tracking board, not dispatch (scheduling owns commitment-before-execution); remove the live picture → after-the-fact records. All four are required.

Historical check: the radio-and-paper era satisfies all four without any modern implementation — the dispatcher knew availability personally, assigned by voice, and kept the board (paper/whiteboard/magnetic) as the live picture; Truckbase's own marketing documents the check-call era as the manual baseline ("Twenty years ago, this would all have to be done manually"). Pre-GPS, pre-app, pre-optimization dispatch software (and non-US equivalents) fits the definition. GPS, mobile apps, optimization, customer notifications, EDI, cloud are later additions → L1/L2.

### L1 — Common Mature Structure

- Real-time location feeds for resources (ELD/GPS/telematics integration or native; technician location in apps)
- Field-side surface (mobile app or message-based dispatch: assignments in, status/documents back)
- Route building / sequencing support and stop-level detail (transport/delivery flavors)
- Recommendation/assistance for assignment (proximity, skills, availability; optimization engine where present)
- Customer-facing notifications and tracking (ETAs, tracking links/pages, reminder/running-late messages)
- Exception machinery (reassignment, delays, breakdown alerts, emergency/urgent insertions)
- Reporting/KPIs (utilization, on-time rate, load/job turnaround) and manager dashboards
- Integration spine for work intake (ERP/POS/eCommerce/TMS/lead sources) and outward to settlement/records
- Scheduling/calendar layer feeding the dispatch day (work arrives already scheduled or as same-day demand)

### L2 — Variant / Optional Structure

- Industry work semantics: freight loads (trucks/brokers), delivery orders/stops (distribution), service jobs (trades), and the industry-specific leaves that specialize them (taxi, towing, courier)
- Workforce model: own employees/owner-operators vs mixed internal + third-party/crowdsourced fleets
- Optimization depth: none (calendar-first, text-first) → rules-based engine → optimization-led planning suite
- Automation depth: manual drag-drop → assisted recommendation → AI auto-dispatch (auto-assignment marketed without human intervention is single-product in this sample; kept variant)
- Packaging: standalone dispatch product vs module of fleet/telematics platform vs stage of an FSM/TMS business suite
- Scale: single-dispatcher SMB (a handful of trucks/techs) to multi-warehouse enterprise
- Customer-facing depth: internal-only dispatch vs customer-visible tracking/portal/EDI status
- Regional/deployment shape: cloud SaaS dominant in sample; legacy on-prem dispatch exists in the installed base

### L3 — Vendor-specific (research notes only)

- Truckbase: AI-powered PDF rate-con load importer; text-based dispatch without driver app; 30+ ELD integrations; one-click broker update emails + BOL scanning; driver settlement module; customer portal; factoring/EDI integrations; "COMING SOON" routing (PC*Miler/Google Maps); 5–50 truck positioning.
- Elite EXTRA: six-stage named workflow (Integrate→Route→Dispatch→Inform→Fulfill→Manage); route whiteboard; Delivery Network with provider price/time comparison (DoorDash/Uber/Roadie class); Returns Automation pickup dispatch; Fleet Telematics as separate Epicor sibling product; auto-parts/distributor testimonial base; 8-week release cycle.
- Samsara: Route Planning / Route Execution / Commercial Navigation three-part structure; telematics-native data spine (GPS, diagnostics, fuel, HOS in one platform); Driver App unifying navigation + customer notifications + HOS; 99.99% uptime SLA claim; Harris Ranch/Mohawk case studies; marketplace of 300+ integrations.
- Workiz: growth-engine framing (Lead Capture→Book→Dispatch→Estimates→Pay→Remarket); Genius Answering AI that "books jobs and dispatches the right tech without any human intervention"; "Jessica" AI assistant; Genius Phone dispatcher insights; drag-drop calendar with per-tech routes; Linxup telematics integration; Dispatch.me integration.

---

## Boundary Findings

| Neighbor Type | Relationship | Boundary criterion ("remove/add X → becomes the other") |
|---|---|---|
| Computer-aided Dispatch / CAD (§24, processed) | structural sibling, emergency | Add emergency incident semantics — incidents with nature/priority, response rules, public-safety governance, emergency-line intake — over the same assignment mechanics → CAD. Dispatch Management has no incident/priority/response machinery; its work is commercial service work. (CAD pass itself recorded this leaf as its commercial sibling.) |
| Taxi Dispatch Platform / Towing Dispatch Platform (§18) | industry-specialized siblings | Specialize the work item to passenger rides / tows with industry settlement → those leaves. Same generic machinery underneath; directory already separates them. |
| Courier Management Platform (§18, processed) | sibling with business frame | Add the courier operator's business frame — courier orders for external customer accounts, contracted-rate rating, billing on completed work, POD as contractual closure — → Courier Management. Remove that frame and only the dispatch loop remains → this Type. (Held consistently with the courier pass's own seam.) |
| Transportation Management System / Trucking Management System (§18) | host/adjacent business frame | Add the freight business system — order-to-cash, carrier settlement, EDI tendering, compliance — → TMS/TMS-for-carriers. Dispatch is the operational core inside such suites (Truckbase self-labels "dispatch-centric TMS"), but the dispatch machinery does not require the freight frame. |
| Route Optimization Platform (§18) | machinery sibling | Make the optimization engine the defining object (solve routes; dispatch is output) → Route Optimization Platform. Dispatch Management can be manual-first — a sampled dispatch-centric product ships no optimization at all. |
| Fleet Management System (§18, processed) | estate vs assignment | Make vehicles/telematics/maintenance/fuel the system of record → FMS; dispatch appears there only as an optional module. Here the work item is the object of record and the vehicle is the executing resource. Confirms the FMS pass's finding. |
| Delivery Scheduling Platform (§18, processed) | plan vs mobilize | Scheduling owns the time-grid of commitments before execution (days/windows/slots); dispatch owns mobilizing work to resources in/for execution. Work arrives from scheduling already time-placed; dispatch answers "who does it," not "when is it offered." |
| Last-mile Delivery Platform / On-demand Delivery Platform (§18, unprocessed) | seam pending | These own shipper-side delivery orchestration/customer experience; a dispatch core may sit inside them. This pass holds the dispatch machinery seam; final placement should be settled in those passes (joint review already recommended by the courier pass). |
| Driver Management / ELD-HOS (§18) | resource-record siblings | Driver records, compliance, licenses, hours = the resource dimension; dispatch consumes availability but does not own the records. |
| Employee Scheduling Platform (§09) | time vs work | Scheduling assigns people to time slots (shifts); dispatch assigns work items to people. Products blur this at the calendar surface, but the managed object differs. |
| Field Service Management (generic category; Small Business FSM leaf §29) | suite vs core | FSM suites run the full customer→job→invoice→payment spine with dispatch as one stage; this Type is the dispatch stage as such. The directory has no generic-FSM leaf; trades dispatch is documented in the §29 trade leaves as part of their spine. |

Taxonomy verdict: Dispatch Management is a legitimate standalone Type — the transversal dispatch machinery that industry-specialized dispatch leaves and business-suite dispatch modules all instantiate. The CAD pass's "(freight)" gloss is too narrow; the courier pass's "generic field-workforce dispatch" is confirmed, with transportation/mobility as the directory's center of gravity. No alias/duplicate problem; no directory change proposed.

## Watch-items discharged / carried

- Construction Materials Management watch-item (bulk-hauling pole): discharged from this side — the seam holds on the object of record (material quantity vs orders/jobs → that Type; work item assigned to trucks/drivers with trucks as resources → this Type / TMS). Recorded in STATUS.md.
- Courier pass's §18 delivery-cluster joint review: this pass documents the dispatch machinery seam; last-mile-delivery-platform and on-demand-delivery-platform remain unprocessed and should inherit this boundary when processed.

## Uncertainties

1. **Status vocabularies**: no fetched source documents a canonical status ladder for work items (unassigned → assigned → en route/in progress → complete) or resources; described conceptually only. Exact per-product status sets are unverified.
2. **Enterprise-FSM dispatch board** (ServiceTitan) and **fleet-carrier dispatch module** (Verizon Connect) unreachable — the field-service pole is carried by Workiz alone; the enterprise trades dispatch surface is unverified this pass.
3. **Samsara dispatch-software guide body** did not render; only the takeaway sentence was usable from that page.
4. **Automation-forward claims**: "dispatch without any human intervention" is a single-product marketing claim (Workiz); not generalized. The practical checkpoint behavior of auto-dispatch was not observable from marketing pages.
5. **Regional coverage**: all sampled vendors are North America-centric; the historical/regional check rests on the structural argument (radio/paper era + Truckbase's documented manual baseline), not on direct non-US vendor evidence.
6. **POD depth**: signature/photo capture observed in the delivery-flavored products; whether POD is definitional for generic dispatch was deliberately NOT decided — it is treated as a delivery-flavor capability, since the courier pass owns POD as its own L0 element.

## Final Synthesis

Dispatch Management is the dispatcher's operational application: it holds the work that needs doing as assignable items, keeps the roster of mobile resources with live availability, manages the binding of work to resources (by hand, with help, or automatically), transmits assignments to the field, receives progress back, and works exceptions — all on a live board that shows the operation's current state. Everything else that modern dispatch products carry — GPS feeds, driver apps, optimization engines, customer tracking pages, settlement hooks — is maturity and industry layering. The Type's identity is transversal: the same machinery underlies freight dispatch inside a TMS, route dispatch inside a telematics platform, job dispatch inside a field-service suite, and the industry dispatch leaves (taxi, towing, courier) that specialize the work item's semantics.
