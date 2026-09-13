# Research Notes — Delivery Scheduling Platform

## Research Goal

Understand what a "Delivery Scheduling Platform" actually is in the market: what gets scheduled, who fixes the "when" of a delivery, what machinery governs schedulable times, and how the schedule connects to routing/execution — so that this §18 leaf can be defined independently of its dense neighbor cluster (courier management, last-mile delivery, on-demand delivery, route optimization, proof of delivery, dispatch management).

## Initial Boundary

Hypothesis before research: the Type is about **when deliveries happen** — booking/fixing/managing delivery dates and time windows and organizing delivery work around that schedule.

Nearest neighbors (from DIRECTORY §18 and the courier-management-platform pass):

- Courier Management Platform — courier order lifecycle + billing (operator business frame)
- Last-mile Delivery Platform — shipper-side delivery orchestration with customer-experience focus
- On-demand Delivery Platform — instant/near-now consumer delivery
- Route Optimization Platform — stop-sequencing engines
- Delivery Experience Platform (§05.08) — post-purchase tracking/communication
- Dock Scheduling Platform (§10) — warehouse dock appointment scheduling
- Appointment Scheduling Application (§03.09) — generic person-appointment booking

Prior family handoff (STATUS.md, courier-management-platform, 2026-09-07): the §18 delivery cluster is the densest seam family in the directory; the courier pass held the seam on tenant identity and predicted this leaf = "scheduling of deliveries/routes is embedded; the standalone Type is narrower."

## Research Questions

1. What is the scheduled object: the order, the delivery, a slot, a route, a round?
2. Who sets the "when": the customer (self-booking) or the operator (dispatcher planning)? Both?
3. What machinery governs which times can be promised: slots/windows, capacity per slot/day, cutoff/lead times, blackout dates, zones?
4. How does the schedule propagate into execution (routes, dispatch, prep, notifications)? Is propagation definitional?
5. How do changes work: reschedule, move to another day, unschedule, cancel; what happens when a commitment and a route conflict?
6. Do recurring/standing schedules exist as first-class objects?
7. What separates this Type from Route Optimization Platform, Last-mile Delivery Platform, Courier Management Platform, and generic appointment scheduling?

## Representative Products

Selection rationale: different poles of the "when" question, different customer tiers, different packaging.

| Product | Pole | Customer tier | Packaging |
|---|---|---|---|
| Zapiet — Pickup + Delivery | customer self-booking of delivery/pickup slots (checkout side) | SMB merchants → Shopify Plus | storefront app (Shopify) |
| OptimoRoute | operator multi-day scheduling for delivery + field-service fleets | SMB → enterprise | standalone SaaS |
| Routific | operator delivery-day planning for scheduled-delivery businesses | SMB delivery operators | standalone SaaS |
| Orderable | delivery/pickup timeslots inside an online-ordering product (slot-machinery cross-check; adjacent Type: restaurant online ordering) | SMB food merchants | WordPress/WooCommerce plugin |

Examined and rejected as core samples: Dispatch (dispatchit.com) — official site positions it as a "delivery orchestration platform" / last-mile network for enterprise industrial distribution; center of gravity sits with Last-mile Delivery Platform, not scheduling. Onfleet (403 ×2, timeout ×1), Bringg (403), Webkul store (403), Iconic WP (403) — unreachable; not used.

## Sources

All fetched 2026-09-07. Official sources only (Tier 1/2).

- Zapiet: https://zapiet.com/ ; product page https://zapiet.com/shopify/store-pickup-delivery ; help center https://support.zapiet.com/en/articles/6279887-delivery-setup-overview ; https://support.zapiet.com/en/articles/6279892-configuring-delivery-slots (Intercom help center, sidebar collection tree also observed)
- OptimoRoute: https://optimoroute.com/ ; https://optimoroute.com/order-and-task/ ; https://optimoroute.com/weekly-planning/
- Routific: https://www.routific.com/ ; help center root https://help.routific.com/en/ ; https://help.routific.com/en/articles/9-what-are-route-templates ; https://help.routific.com/en/articles/52-use-delivery-dates-when-scheduling-your-orders
- Orderable: https://orderable.com/
- Dispatch (positioning only): https://www.dispatchit.com/

Sourcing limitations: Onfleet, Bringg, Webkul, Iconic unreachable (403/timeout) — the enterprise checkout-window-orchestration pole (Bringg-class) and additional storefront slot plugins are evidenced indirectly only; no claims made about them. Help-center-level numeric defaults (cutoff lengths, slot limits) observed only where explicitly documented (e.g., Zapiet's "10-minute intervals" granularity) — all other numbers deliberately omitted.

## Product A — Zapiet — Pickup + Delivery

### Key observations (evidence layer A unless noted)

Positioning: "Add scheduled store pickup, click & collect and local delivery to Shopify. Time slots, delivery zones, multi-location and POS sync."

- **Order scheduling as the flagship feature**: "Reliable time slots for customers. Predictable prep for your team. Set slot capacity per location, define cut-off times so late orders roll to the next window, and block out the dates you're closed. Customers pick a real time you can actually honour."
- **Delivery slots** (help center): "the delivery times your customers can choose after selecting a date"; slots can be the same every day or differ by weekday; configured **per location**; each slot has from/until times; "the slot will be blocked out when it starts" (a single 9–5 slot makes same-day delivery unavailable after 9am; multiple shorter slots recommended for same-day).
- **Date and time pickers**: date picker usable without time picker; time picker requires date picker; product page claims availability "down to 10-minute intervals" (vendor-stated granularity).
- **Delivery order limits** (capacity): choose how many orders each date or time slot takes (plan-gated to higher tiers per FAQ).
- **Blackout dates**: block out dates the business is closed.
- **Preparation time**: lead time before an order can be scheduled.
- **Restrict future orders**: control how far ahead orders can be booked.
- **Zone/product-scoped schedules**: "Creating zone-based delivery schedule and pricing" (different schedules for different areas); "Creating product-based delivery schedule and pricing"; product date restrictions (products available only on certain dates).
- **Delivery validation/eligibility**: postal-code/radius/driving-distance validation, custom-drawn zones, delivery validator widget on every page.
- **Staff-side schedule work**: dashboard lists all pickup/delivery orders sorted by pickup/delivery date or creation date, filterable by date/location/checkout method/status; Google Calendar view; CSV export; draft orders let staff set location + date/time manually; staff edit order details, customers cannot; production reports "plan the day".
- **Notifications**: pickup-ready and delivery-status emails/SMS fire automatically.
- **Execution hand-off is integrative, not native**: "Last Mile Delivery" help collection documents on-demand driver-network integrations (DoorDash Drive, Uber Direct, Roadie, Gophr, Stuart, etc.); "Fleet Management" collection documents routing integrations (Onfleet, Shipday, AntsRoute, Zippykind); route optimization is a partner page, not a native module.
- Merchant workflow (FAQ + setup overview): enable delivery → configure days/slots/limits/blackouts/prep time per location → widget on storefront → customer validates address → books date/slot → order carries date/time attributes into Shopify → staff work the dashboard by date.

## Product B — OptimoRoute

### Key observations (evidence layer A)

Positioning: "Delivery Route Planning & Field Service Scheduling"; "Plan your day instantly. Optimize for top productivity."

- **Orders with time constraints**: orders/tasks carry "priorities, time windows, job durations, skills"; example given: "delivering between 9am–11am".
- **Recurring schedules**: "Recurring appointments or deliveries" listed as routing constraints; "repeating the same service every week"; recurring orders managed as a workflow.
- **Weekly Planning** (dedicated feature): plan across a date range "up to five weeks at a time" considering "date range (e.g. service needs to be done between May 2nd and May 6th), available days (…either on Monday or Thursday), time windows (…customer is at home only after 5pm), order type, vehicle and driver constraints"; schedules updated with cancellations/last-minute orders "without compromising existing orders".
- **Constraint-driven scheduling with explanations**: "If an order cannot be scheduled, OptimoRoute explains why"; dispatchers drag-and-drop orders, use best-fit insertion, review constraint warnings before committing.
- **Case use-cases** (vendor-stated): inspection business books inspections initially with a 2-hour window, then narrows the start time 1–2 days before and notifies the customer; vending business schedules stocking 5–7 days ahead and slots urgent orders into days when drivers are already in the area; food distribution plans Mon–Fri weeks ahead around loading hours.
- **Execution stack**: automated route optimization, driver app, live tracking/ETA, customer notifications, proof of delivery — the planner sits upstream of routing/execution.
- Scale of scheduling decision: dispatcher (operator) sets the when, within customer-imposed windows.

## Product C — Routific

### Key observations (evidence layer A)

Positioning: "Delivery management & route optimization software for growing businesses… designed for last-mile delivery businesses."

- **Delivery dates on orders** (help center): "Assign delivery dates to your orders so you can plan your routes more easily in advance… upload all your orders at once and indicate delivery dates so Routific knows exactly when each order should go out"; benefits: plan routes in advance, "stay aligned with your delivery schedule", "meet customer expectations — fulfill orders on the dates your customers requested"; orders without a delivery date "appear on every date" and can be scheduled any day.
- **Changing the delivery date**: unscheduled orders move to the new date; already-scheduled orders get a mismatch warning (route planned for a date that no longer matches) — the system does not silently re-schedule.
- **Scheduling machinery in help tree**: "How to optimize and schedule routes", "Moving orders and routes to another day", "How to unschedule orders", "Reuse a day's route setup", "How to insert last-minute orders", "Use delivery dates when scheduling your orders", "What are time windows?".
- **Route templates**: reusable route shapes — shift times, standard start/end locations, vehicle load capacity, number of routes — applied when scheduling future routes; editing a template "will not adjust any current scheduled routes… will affect any new routes to be scheduled".
- **Customer base** (vendor case studies): scheduled-delivery programs — meat subscription (Walden Local), farm-to-home grocery (~3,500 weekly deliveries, 4P Foods), flower subscription (Bear's Blooms), bakery (Flourist) — i.e., standing delivery rounds are the typical workload.
- Customer notifications include a "scheduled 3–5pm delivery window" SMS with tracker link (marketing imagery).
- Scale of scheduling decision: dispatcher plans; delivery date often reflects a customer-requested or subscription-driven commitment.

## Product D — Orderable (slot-machinery cross-check; adjacent Type)

### Key observations (evidence layer A)

Positioning: online ordering system for restaurants/bakeries/florists (WordPress/WooCommerce). Primary Type adjacency: Restaurant Online Ordering (§26 family). Included because its delivery-scheduling machinery is directly documented and independent of Zapiet.

- **Delivery and Pickup Timeslots**: "Allow customers to select the time and date they'll receive/pick up their order at the checkout. Tailor this to your schedule with maximum orders, holidays, ASAP delivery, lead time, and more."
- Storefront sets "food delivery/pickup schedule"; per-location customization of "opening hours, delivery services, delivery zones, order screen, delivery times, and dates".
- Order notifications to customers (order on the way / ready).
- Confirms the slot machinery (timeslots, max orders per slot, holidays, lead time, ASAP) as a cross-product pattern independent of Shopify.

## Product E — Dispatch (examined, rejected as core sample)

### Key observations (evidence layer A, positioning-level only)

Official site: "Delivery Orchestration Platform for Enterprise Industrial Distribution"; national driver network; fleet management includes "route planning, vehicle capacity, driver assignments, and delivery schedules"; comparison table positions it against "route planning / TMS software" and on-demand couriers. Center of gravity = last-mile orchestration/execution network. Scheduling is one input among many. Classed as Last-mile Delivery Platform territory and excluded from the sample; boundary evidence only.

## Cross-product Comparison

| Dimension | Zapiet | OptimoRoute | Routific | Orderable |
|---|---|---|---|---|
| Who fixes the when | customer books at checkout | dispatcher plans within constraints | dispatcher plans; date often customer-requested | customer books at checkout |
| Scheduled unit | order → date + time slot (per location/zone/product) | order/task → day(s) within date range + time window | order → delivery date → route | order → date + timeslot |
| Availability structure | delivery days, slots per weekday, blackout dates, prep time, restrict-future | date ranges, available days, time windows, driver/vehicle constraints | delivery dates; route templates (shifts, depots, capacities) | timeslots, holidays, lead time, max orders |
| Capacity control | order limits per date/slot (plan-gated) | via driver/vehicle constraints, workload balancing | route capacity/number of routes in templates | max orders per slot |
| Recurring patterns | via subscription apps (date incrementation documented for Appstle/Recharge/Awtomic) | recurring orders/weekly services | standing delivery rounds typical of customer base; reuse day's setup | — (not documented) |
| Change management | staff edit date/time; customers cannot self-edit | reschedule; cancellations; constraint warnings; explains unschedulable | move orders/routes to another day; unschedule; mismatch warning | — (not documented) |
| Schedule surface | dashboard by date/slot; calendar sync; production reports | planner grid; weekly plan; drag & drop | scheduled tray; timeline; order page by date | — (checkout + order management) |
| Propagation to execution | integrations (last-mile networks, fleet/routing tools); prep via production reports | native: route optimization → driver app → POD | native: route optimization → driver app → tracking | native ordering/kitchen flow |
| Customer comms | order-ready/delivery-status emails/SMS | ETA notifications, tracking | window SMS + tracker link | order status notifications |

### Stable commonalities (B layer — cross-product)

1. The scheduled delivery (order fixed to a date; commonly a window/slot) is the unit.
2. An availability structure defines which times can be scheduled (days/slots/windows + admission rules: capacity, cutoff/lead time, blackouts).
3. A schedule surface where staff work by date/slot (dashboards, calendars, planners, trays).
4. Change management against the schedule (move/reschedule/unschedule; warnings on mismatch).
5. Notification of the committed when to customers.
6. Recurring/standing patterns in at least 3 of 4 (recurring orders, subscription date increments, standing rounds, weekly plans).
7. Hand-off to execution (native routing or integrations) — present everywhere but implemented natively in only 2 of 4.
8. Scoping of schedules by location/zone/resource (per-location slots; per-driver/vehicle constraints; per-zone schedules).

### Divergences (implementation-level)

- Who sets the when: customer pole (Zapiet, Orderable) vs dispatcher pole (OptimoRoute, Routific).
- Granularity: timed slots vs date-only vs date-range "somewhere this week".
- Whether routing is native or external.
- Whether customer self-service editing exists (Zapiet explicitly denies customers date/time edits).

## Canonical Model

### L0 — Defining Invariant (deliberately small)

1. **The scheduled delivery** — a delivery commitment for goods to a destination, fixed to a date (and commonly a time window) and held as a managed record before execution. Without it there is no scheduling at all — just order records.
2. **The delivery schedule** — a maintained time-grid view (days, and where offered slots/windows) of those commitments that staff and/or customers work from; the schedule is the organizing object of the application. Without it the product is an order list or a route engine, not a scheduler.
3. **The availability structure** — the application (not the customer or driver ad hoc) defines the set of schedulable times: offered delivery days, time windows/slots, date ranges, or recurring patterns, qualified by admission rules (lead times, closures, capacity). Without it, a date stamp on an order would suffice and there would be nothing to "schedule".

Historical check: pre-software delivery scheduling satisfies all three — furniture/appliance deliveries were booked into an appointment book with offered windows (slot structure), milk/newspaper rounds ran on standing weekly schedules (recurring pattern), and the round/appointment book was the schedule surface. No checkout widget, GPS, or optimization engine is required; all three are modern implementations.

### L1 — Common Mature Structure

- Capacity/limits per slot or day; cutoff/lead times; blackout dates; restrict-future-order windows
- Per-location/per-zone/per-product scoping of schedules; eligibility validation (zones, postal codes, distance)
- Customer self-service booking surface (checkout widget/picker) at the storefront pole
- Staff schedule surfaces: dashboards/calendars/planners by date and slot; production/prep reports
- Change management: reschedule, move to another day, unschedule, cancel; mismatch warnings when commitments and routes diverge
- Recurring/standing schedules (recurring orders, weekly plans, route templates, subscription date increments)
- Notifications tied to the committed when (order-ready, window reminders, ETA)
- Hand-off to execution: native route optimization/dispatch (operator pole) or last-mile network integrations (storefront pole); CSV/API exports
- Time windows as order attributes

### L2 — Variant / Optional Structure

- Pole: customer-self-booking vs operator-planning (the main market split)
- Granularity: date-only, date + timed slot, date range, window narrowed late (book wide, narrow before service)
- Scope: local delivery/pickup for a merchant vs fleet-wide delivery + field-service planning
- Recurring programs: subscription/standing rounds vs one-off orders
- Packaging: storefront app/plugin vs standalone SaaS planner vs scheduling module inside a broader delivery platform
- Industry tuning: food/bakery (prep-time driven), grocery/meal subscription rounds, florists, inspection/field service, big & bulky/industrial distribution
- ASAP/near-now scheduling as a mode alongside future-dated scheduling

### L3 — Vendor-specific (kept out of the final document)

- Zapiet: ZapietId order attribute; plan-gated per-slot order limits (Advanced plan); 10-minute picker granularity; Google Calendar sync; specific last-mile integration names (DoorDash Drive, Uber Direct, Roadie…); routing partner names (Onfleet, Shipday…)
- OptimoRoute: "up to five weeks" planning horizon; "explains why" unschedulable orders; skill/certification matching; coordinated multi-driver jobs; truck/hazmat routing; branding as "#1 rated route optimization"
- Routific: route-template fields (shift time, depots, route capacity, number of routes); delivery-date CSV formats (YYYYMMDD etc.); mismatch warning behavior; workspace model; ETA ML claims
- Orderable: table ordering, WhatsApp notifications, tipping/order bumps (ordering-product features outside scheduling)
- Dispatch: orchestration branding, national driver network metrics, National Delivery Guarantee terms

## Vendor-specific Findings

See L3. Single-product findings that must not generalize: customer self-booking with staff-only edits (Zapiet); "explains why an order cannot be scheduled" (OptimoRoute); delivery-date mismatch warnings (Routific); plan-gated capacity features (Zapiet).

## Rejected Findings (considered and rejected as core)

- **Route optimization as definitional**: both operator-pole products lead with route optimization, but the storefront pole schedules without any native routing (Zapiet works entirely through Shopify + integrations); historic scheduling predates optimization. Optimization is a common execution complement, not the defining structure.
- **GPS/live tracking as definitional**: absent from the storefront pole entirely; fails the historical check.
- **Checkout widget as definitional**: the operator pole schedules without any storefront surface; fails cross-product test.
- **Capacity limits per slot as definitional**: near-universal in modern products but the abstract availability structure (offered days/windows) is the invariant; capacity is its strongest modern realization. Kept common-not-core.
- **Notifications as definitional**: common; pre-software scheduling communicated the when verbally/paper.
- **"Platform = network/marketplace" reading**: no sampled scheduling product is a demand marketplace; the scheduling machinery, not network effects, is the Type.
- **Dispatch as a sample**: self-positioning places it in last-mile orchestration, not scheduling-centric software.

## Boundary Findings

| Neighboring Type | Relationship | Distinction (the "remove-what" test) |
|---|---|---|
| Route Optimization Platform | closest pole overlap (operator side) | Route optimization sequences stops; delivery scheduling owns the when-structure: offered times, admission rules, commitments, and the schedule as the worked object. Remove slots/windows/cutoffs/commitment management from OptimoRoute/Routific and what remains is a route optimizer; add a scheduling center to it and it enters this Type. Both sampled operator-side products straddle the seam — joint review recommended. |
| Last-mile Delivery Platform | adjacent, frequent packaging overlap | Last-mile platforms orchestrate execution of deliveries (carriers, tracking, customer experience); scheduling is one input. Dispatch (examined) self-labels "delivery orchestration" — its delivery schedules are an input to orchestration, not the center. Remove the schedule-centric machinery (when-structure + schedule surfaces) and a scheduling product becomes a last-mile platform. |
| Courier Management Platform | family neighbor, capability slice both ways | Courier management runs the operator's order lifecycle end-to-end (dispatch, POD, rating/billing); scheduling is embedded there. The courier pass predicted this leaf is "narrower" — confirmed: this Type carries the when-commitment machinery but not the courier business frame (rates, billing, driver pay, courier order identity). |
| On-demand Delivery Platform | adjacent | On-demand delivery dispatches near-now work driven by consumer demand; scheduling recedes to ASAP modes. A scheduling product is organized around future commitments. ASAP scheduling exists here only as a mode (documented in the storefront pole). |
| Delivery Experience Platform (§05.08) | different focus | Delivery experience owns the customer-facing post-purchase surface (tracking pages, comms). Scheduling owns the when-structure upstream. Notifications about the committed window overlap, but the experience platform does not define schedulable times or manage the schedule. |
| Dock Scheduling Platform (§10) | sibling name, different object | Dock scheduling books carrier appointments at warehouse docks (facility logistics). Delivery scheduling commits last-mile deliveries to customers. Different scheduled objects, different users. |
| Appointment Scheduling Application (§03.09) | structural cousin, different domain | Generic appointment booking schedules person-services (meetings, salons). Delivery scheduling adds logistics semantics: goods, addresses, zones, route/day capacity, prep/cutoff rules. The slot/window/availability machinery is shared; the domain objects are not. |
| E-commerce Fulfillment / Order Management (§05) | upstream consumers | Order management records the order; delivery scheduling structures when it will be delivered and manages that promise. Storefront pole sits inside e-commerce stacks as the scheduling layer. |

## Uncertainties

1. **Market self-labeling**: no sampled product markets itself primarily as a "delivery scheduling platform"; the population is realized as storefront slot schedulers, schedule-first planners, and scheduling modules of delivery platforms. The directory label is a category name, not a vendor label — Type cohesion is supported by the shared machinery, but the label↔population mapping is moderate confidence.
2. **Enterprise checkout-window orchestration** (Bringg-class, delivery windows at scale with promise engines): sources unreachable; the customer-promise pole at enterprise scale is characterized only via the SMB storefront samples. No claims made about enterprise promise-engine mechanics.
3. **Customer-side rescheduling**: Zapiet documents staff-only edits; other samples don't document customer self-rescheduling. Whether customers can reschedule their own deliveries is implementation-dependent — kept out of the core.
4. **Cross-pole notification detail** (what exactly is sent when the window narrows): vendor-stated for OptimoRoute's case study, not verified at help-center level elsewhere.
5. **Regional products** (e.g., EU slot-based grocery delivery engines, Japanese time-slot commerce): not sampled; assertions kept at the conceptual level.

## Final Synthesis

A Delivery Scheduling Platform is the system that owns **when deliveries happen**. Its defining core is three structures: (1) the scheduled delivery — a delivery commitment fixed to a date (commonly with a window) held as a managed record; (2) the delivery schedule — a maintained time-grid of those commitments that staff and/or customers work from, the application's organizing object; (3) the availability structure — the application-defined set of schedulable times (days, windows/slots, date ranges, recurring patterns) qualified by admission rules. Everything else — capacity limits, cutoffs, blackout dates, zone scoping, checkout widgets, planner grids, recurring programs, notifications, and the hand-off into routing/dispatch/last-mile execution — is the mature capability stack that makes the core operational, realized across two market poles (customer self-booking at the storefront; operator planning for delivery fleets) that share the same machinery. The Type sits deliberately between Route Optimization Platform (which sequences the how) and Last-mile Delivery Platform (which orchestrates the execution): remove the when-structure and it becomes one of those; remove routing/orchestration and it remains a scheduler.
