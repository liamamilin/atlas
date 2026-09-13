# Research Notes — Route Optimization Platform

## Research Goal

Understand what a Route Optimization Platform actually is as an Application Type: what the unit of record is, what the optimization act takes as input and produces, how plans are edited and re-optimized, how the plan is handed off for execution, and how the Type separates from the dense §18 delivery/logistics cluster (last-mile-delivery-platform, delivery-scheduling-platform, dispatch-management, transportation-management-system-tms, fleet-management-system) and from navigation/journey-planning tools.

## Prior-pass context (sibling seams to settle from this side)

- **last-mile-delivery-platform** (processed 2026-09-08): boundary recorded as "Route Optimization Platform | capability vs center | The optimization engine is a common capability here (and tier-gated in one product); when the engine and its solves are the defining object, that is Route Optimization." This pass must ratify from this side. Also: "route-optimization-platform side still pending that pass."
- **delivery-scheduling-platform** (processed 2026-09-07): "the operator pole straddles the Route Optimization seam (both sampled operator-side products [OptimoRoute/Routific-class] lead with route optimization while carrying full scheduling machinery) — JOINT REVIEW recommended when route-optimization-platform and last-mile-delivery-platform are processed."
- **transportation-management-system-tms** (processed 2026-09-08): "route-optimization-platform = algorithm capability vs management system (optimization depth in sampled TMS varies none→deep)."
- **courier-management-platform / §18 delivery family**: cluster-wide joint-review recommendation (courier pass) — partially discharged by the last-mile pass; this pass settles the route-optimization side of the remaining flags.

## Initial Boundary (working hypothesis before research)

Hypothesis: the defining object is the **route/plan** and the defining act is the **constrained optimization solve** — turning a pool of stops plus available resources into ordered, resource-bound routes. Execution (driver apps, POD, tracking) and customer communication are common adjacent layers, not the center. Confusion risks: last-mile delivery (execution orchestration), delivery scheduling (when-structure), dispatch (assignment act), TMS (freight management), fleet management (vehicle estate), consumer navigation (turn-by-turn for one trip).

## Research Questions

1. What is the unit of record — route, plan, stop, or order — and what does each carry?
2. What exactly does the solve consume (stops, resources, constraints, objectives) and produce?
3. Which constraints are configurable, and is any specific constraint definitional?
4. How are plans edited, overridden, and re-optimized when inputs change?
5. Is execution machinery (driver app, tracking, POD, notifications) part of the center or a common adjacent layer? (RouteSmart as the natural control case.)
6. What user populations exist (route planner vs dispatcher vs individual driver vs strategic planner vs developer)?
7. What flavors exist (delivery vs field service vs high-density industrial vs personal planner vs engine/API) and does the core change across them?
8. Does the single-driver case (no fleet) still satisfy the Type?
9. Where exactly do the sibling seams separate, by the remove-what test?
10. Historical check: do older/regional products (e.g., 1980s-era newspaper/waste route planning) fit the definition?

## Representative Products

| Product | Why sampled | Tier / philosophy | Sources reached |
|---|---|---|---|
| **Route4Me** | archetypal "route optimization platform"; API-first since 2009; SMB→enterprise; constraint marketplace; deep support portal | platform/engine posture; roles incl. dedicated "Route Planners" category | route4me.com, /platform/route-planning-software, support.route4me.com (route-planners category, multi-stop how-to) |
| **Routific** | SMB delivery-focused route optimization; explicit "route optimization" identity; sells its engine standalone (Engine API) | SMB, delivery; "practical routes / no spaghetti routes" philosophy | routific.com, routific.com/how-it-works |
| **OptimoRoute** | mid-market plan+optimize across delivery AND field service; weekly planning, replanning automation | plan/schedule breadth around one optimize act | optimoroute.com, /features/automated-planning/ |
| **Spoke (formerly Circuit)** | mobile-first individual-driver route planner + separate Dispatch product; the single-user pole | driver-simple, freemium | spoke.com, /route-planner (FAQ detail) |
| **RouteSmart** | 40+ years, FedEx-owned; enterprise high-density routing (waste, public works, postal, utilities, newspaper); GIS/OR-centered, execution-light | strategic/precision planning pole; safety/balance objectives | routesmart.com, /about-us/our-approach/ |

Rejected/deferred: Circuit-branded pages (redirected to Spoke — brand migration documented); OptimoRoute support center (transport error ×2, dropped per network rule — feature pages substituted); Routific help center (empty response — limitation recorded); Bringg-class (unreachable in prior sibling passes; not re-attempted); consumer navigation apps (different Type, boundary only).

## Sources

Fetched 2026-09-09:

- Route4Me — https://www.route4me.com/ (homepage: platform map, claims); https://www.route4me.com/platform/route-planning-software (constraint catalog, adjust-instantly, capabilities, recurring); https://support.route4me.com/category/route-planners/ (documentation taxonomy: Dynamic/Strategic/Recurring/Commercial routing, Business Rules & Constraints, Routes & Destinations Management); https://support.route4me.com/faq/plan-routes-guide/how-to-plan-a-route-with-multiple-stops/ (6-step flow, named business rules, geocoding, dispatch, tracking)
- Routific — https://routific.com/ (positioning, Engine API, industries); https://routific.com/how-it-works (7-step day flow)
- OptimoRoute — https://www.optimoroute.com/ (feature set, industries, review corpus); https://www.optimoroute.com/features/automated-planning/ (constraint enumeration, replanning automation, weekly planning)
- Spoke — https://spoke.com/ (product family: Route Planner / Dispatch / Connect); https://spoke.com/route-planner (features, plans, FAQ incl. manual ordering, mid-route reoptimization, offline)
- RouteSmart — https://www.routesmart.com/ (industries, case-study economics, Route Health Score); https://www.routesmart.com/about-us/our-approach/ (operations research framing, safety constraints, balance, open architecture, 40 years)

Source-access limitations:

- support.optimoroute.com returned transport errors on two attempts (root + /help-topics/); dropped per the retry rule. OptimoRoute evidence rests on its marketing/feature pages (Tier 2) — operational click-path detail not independently verified; no precise mechanics claimed beyond feature-page statements.
- help.routific.com returned an empty response; Routific evidence rests on product pages (Tier 2). The 7-step flow quoted is from the vendor's own "how it works" page.
- onfleet.com/bringg.com class enterprise platforms not re-attempted (403 recorded in two prior sibling passes); enterprise promise/orchestration pole characterized only via last-mile pass notes.
- No numeric limits, prices, or algorithm names from memory; all specifics below are quoted or closely paraphrased from fetched pages.

## Product Observations

### Route4Me (Evidence layer A — directly observed)

- Positioning: "Route Optimization Platform"; schema.org self-classification "Route4Me Route Optimization Platform"; claims 3B+ miles optimized, 30M+ routes planned, 40K+ customers, since 2009. Own slogan: "It's Not The Route, It's The Optimization!"
- Support-portal taxonomy defines the object world: **Route Planning & Optimization** (Dynamic Routing, Strategic Routing [Strategic Routing System, Strategic Route Planning], Recurring Routing, Commercial Truck Routing, **Business Rules & Constraints**, Advanced Optimization Types, Business Database Routing [Orders/Locations/Address Book], **Routes & Destinations Management** [Route Management, Route Editing & Adjustments, Destinations Management]), plus Dispatch & Tracking, Driver Mobile App, Business Operations (Orders System, Business Database [Customers/Locations/Regions/Facilities/Address Book], Team & Equipment [Users, Vehicle & Fleet, Assets], Workflows & In-Field Tasks, Regions & Zones), Customer Experience, Analytics.
- **Roles**: dedicated documentation categories for Route Planners, Dispatchers, Drivers, Developers, Admins — the route planner is a distinct first-class role from the dispatcher.
- Canonical 6-step flow (official how-to): (1) choose planner, (2) **input customers' delivery addresses** (import thousands from spreadsheets, cloud storage, eCommerce/CRM integrations; geocode + autocorrect), (3) **plan and optimize** ("select the addresses you need to deliver to. If you have multiple drivers, the software can balance workload automatically... instantly optimize routes, giving you the fastest, shortest path"), (4) **set routing rules and optimization constraints** (delivery time windows, vehicle loading capacity, traffic, weather; "fine-tune delivery routes... prioritizing the distance, travel time, and wait time"), (5) **dispatch planned routes to drivers** (iOS/Android apps: turn-by-turn voice navigation, ePOD, real-time stop updates), (6) **track driver progress** in real time; review route history.
- Named business rules (from the how-to's own schema): Multiple Depot, Pieces Constraint, Max Route Distance, Priority, Weight Constraint, Revenue Constraint, Predictive Weather, Cube Constraint, Time Windows.
- Platform page constraint catalog: Time Windows, Max Stops, Max Distance, Max Time, Vehicle Capacity, Mixed Fleets, Max Drivers & Vehicles, Avoidance Zones, Turn Avoidance, Stop Priority, Curbside. Capability list: "Add and Visualize Destinations", "Plan Routes Using a Map", "Dispatch Routes and Track Progress", "Optimize Routes", "Plan Routes from Orders", "Combine Multiple Stops", "Optimize Across Drivers, Vehicles and Depots", "Apply Business Rules and Priorities", "Plan Unlimited Routes".
- **Dynamic reoptimization**: "Extra stop? New address? Unexpected delay?... Just add changes to your route planning software settings and Route4Me's dynamic route optimization engine will reoptimize your routes instantly." Multi-route overview: "Re-assign drivers and vehicles, move an address from one route to another, and track route progress in real-time."
- Distinct solve modes: Dynamic (daily, in-flight), Strategic (long-range master planning), Recurring (repeating route templates — packaged as a paid add-on), Commercial Truck (vehicle-specific routing). Special capabilities: Smartzone Routing ("Let Route4Me create optimized territories"), Curbside ("set exact locations for unusual stops"), Pickup-and-Dropoff ("pair stops for item receipt and delivery"), Mixed-fleet routing.
- Plan-scoped limits exist ("Routes Saved for 7 Days" in one feature list — plan-specific, L3). Execution layer (driver app, POD, notifications, telematics integrations, invoicing from field data) documented as a separate platform pillar, not the planning core.

### Routific (Evidence layer A)

- Positioning: "Delivery Management & Route Optimization Software For Growing Businesses"; "Smart route optimization... Easily create optimized routes based on traffic patterns, driver preferences, and business priorities. Routes are easy to edit."
- 7-step day flow (vendor's own how-it-works): (1) **upload delivery orders** ("Just upload a spreadsheet! Or use our API integration to sync orders from your e-commerce system"), (2) **optimize routes with one click** ("We don't just optimize mathematically. We consider driver happiness, historical traffic patterns, and avoid messy 'spaghetti routes'"), (3) **easy route adjustments** ("comprehensive route planning and editing tools... drag 'n drop, add last-minute deliveries, assign drivers to the territories they are most familiar with"), (4) **dispatch to the driver app** ("Replace paper manifests"), (5) **track drivers** (live GPS; "We respect your drivers' privacy and only track their locations when they are working"), (6) **customer notifications** (tracker links with ETAs), (7) **capture proof of delivery**.
- **Engine API as a standalone product**: "Need just our algo? Routific's AI-powered route optimization algorithm is blazing fast, scalable, and easy to integrate. Leverage 179 machine learning models across the globe for the most accurate ETAs." — the solve sold separately from the delivery platform.
- Industries: food & beverage, couriers, farms, groceries, florists. Claim: 191M+ deliveries optimized.

### OptimoRoute (Evidence layer A; Tier-2 pages)

- Positioning: "Delivery Route Planning & Field Service Scheduling"; "Automated Planning... Maximize the number of orders performed, while reducing costs"; "Once you hit 'plan routes,' any changes are automated too. OptimoRoute will automatically replan and reschedule your routes if things change in the moment." — **"Automated planning is central to the OptimoRoute experience and is available in all three price plans."**
- Constraint enumeration (feature page): driver skills and availability; delivery/service time windows, date ranges, day-of-week constraints; flexible scheduling (start/end from home, working-hour limits, overtime/labor costs, miles); location-based planning (service areas, clustering); automated break planning; task/order variations (backhauling, reverse logistics, multiple depot returns, variable durations, wait times); vehicle capacity/features; coordinated orders (multiple drivers per task); multi-day long-haul routes (beta); weekly planning ("Produce schedules 5 weeks ahead and let the software suggest optimal dates").
- Feature family around the plan: Realtime Route Modification ("Intelligent Drag & Drop"), Live Tracking & ETA, Realtime Order Tracking (customer notifications), Mobile App for Drivers, POD (signatures/photos/custom forms), barcode scanning, customer feedback, analytics, workload balancing, truck & hazmat routing, commercial truck navigation, breadcrumbs, SSO, API.
- Audience spread: 16 industries, delivery AND field service (technicians, inspections, sales) — "Equally efficient at fleet management or planning delivery operations for a single driver."

### Spoke / formerly Circuit (Evidence layer A)

- Two-pole product family: **Route Planner** ("For delivery drivers — our free driver app. Upload stops, optimize delivery routes, navigate easily, and finish your route faster") and **Dispatch** ("For courier companies — our delivery management platform. Plan multi-driver routes, track progress, and collect proof of delivery"), plus Connect (retailer→courier marketplace, out of scope here).
- Route Planner mechanics: input stops by scan (route manifest), voice, search, or spreadsheet; "In 1 click the most efficient route is instantly mapped"; turn-by-turn navigation powered by Google Maps (alternatives: Apple Maps, Waze, HERE WeGo, Sygic); custom stop properties (delivery/pickup type, arrival window, notes, **vehicle load order**, stop ID); mid-route add/edit with re-optimization; offline mode for saved routes.
- **Manual override is first-class**: FAQ — "you can also customize your route stop order before and during your route": cluster stops, make urgent stops next, pin stops to start/end, edit mid-route and reoptimize, or "**Skip route optimization altogether, and attempt stops in the order you added them**."
- Pricing confirms scale positioning: Free ≤10 stops/route; Lite $9.99; Standard $19.99. The unit is the route on the driver's phone — no fleet roster, no dispatcher UI. Claims: 10M+ downloads, 1.5B+ deliveries/year, 2M+ hours saved daily.
- Legal name "Circuit Routing Limited"; brand migration Circuit→Spoke documented in structured data.

### RouteSmart (Evidence layer A)

- Positioning: "Route Planning & Optimization Software"; "Optimize service and delivery routes. Our routing technology cuts planning hours, maximizes fleet efficiency, and enforces street-level safety constraints." A FedEx company; "more than 40 years"; focus: "vehicle routing and scheduling" within operations research.
- Industries: waste collection, public works, postal & local delivery, utilities & field service (meter reading, "balance cycle days"), newspaper delivery — high-density residential and medium-density commercial routing. Case-study economics: route-count reduction (Gannett −48% routes, −16% mileage), meters-per-route increase (PSE&G −12% routes), overtime elimination.
- **Plan-quality objectives beyond time/distance**: "We know good routes when we see them. Keep your routes balanced, compact, and efficient. Measure the results of your route optimization efforts... with the **Route Health Score**." Safety as a solve input: "planning every service to be on the correct side of the street, making sure turns across busy traffic lanes are minimized, planning routes that reduce driver frustration and fatigue."
- **No execution-layer center**: no driver-app/POD/notification emphasis in fetched pages; deployment is planning-day-oriented ("Before a single truck leaves your facilities, you need to build the foundation for a successful, efficient day"). Open architecture stance: "your data is your data... make sure you're not locked into a platform." Services-led model: onboarding, Routing University training, certification, INTERSECT user conference; also "RouteSmart Online" SaaS form (Gannett).

## Cross-product Comparison

| Structure / capability | Route4Me | Routific | OptimoRoute | Spoke | RouteSmart | Assessment |
|---|---|---|---|---|---|---|
| Stops/visits as planning input (geocoded, with visit attributes) | addresses/destinations, orders, address book; geocode+autocorrect | uploaded orders (spreadsheet/API) | orders/tasks w/ windows, durations, skills | scanned/voice/spreadsheet stops w/ windows, load order, stop ID | subscriber/service addresses from client data (GIS) | **Core** (5/5; intake varies) |
| Optimization solve (assignment + sequencing under constraints/objectives) | patented engine; constraint marketplace; multi-depot, mixed fleet | one-click optimize; traffic/historical patterns; "not just mathematically" | automated planning central to product; replan on change | 1-click optimize (skippable); single route | OR-based vehicle routing; balance, safety, cycle days | **Core** (5/5) |
| Route/plan as held record, editable & re-solvable | Routes & Destinations Management; Route Editing; move address between routes; reoptimize instantly | drag'n'drop editing; last-minute additions | Intelligent Drag & Drop; realtime route modification | edit/reorder mid-route; offline saved routes | balanced route plans; Route Health Score as plan-quality measure | **Core** (5/5) |
| Multi-resource assignment (fleet) | yes ("Optimize Across Drivers, Vehicles and Depots") | drivers w/ territories | multi-driver, workload balancing, skills | no (single-driver pole; Dispatch product adds fleet) | fleet-level balance, route count reduction | Common, **not definitional** (single-driver pole in-type) |
| Constraint catalog: time windows | Time Windows | yes (windows on orders) | windows, date ranges, day-of-week | arrival windows | service constraints (safety, side-of-street) | Common (5/5) — catalog varies; **no specific constraint definitional** |
| Constraint catalog: capacity/load | weight/cube/pieces, vehicle capacity | (not emphasized on fetched pages) | vehicle capacity/features | vehicle load order (packing aid) | density/landfill/commercial constraints implied by industry cases | Common in delivery/fleet flavors; absent in simple pole |
| Objective plurality (not just shortest) | fine-tune distance/travel/wait; priority | driver happiness, practical routes | maximize orders performed | urgent-next, pin start/end | balance, compactness, safety, fatigue | Common (5/5) — "optimality" is multi-dimensional |
| Manual override of the solve | route editing; reassign; move address | "You're in control" | Intelligent Drag & Drop | skip optimization; reorder anytime | planner-driven; professionals-in-the-loop (certification) | **Core behavior** (5/5) |
| Re-optimization loop on change | dynamic reoptimization "instantly" | easy adjustments | automatic replan/reschedule | mid-route reoptimize | (re-planning cycle: daily/cycle-day planning) | Common-leaning Core behavior (4/5 direct) |
| Dispatch to driver mobile app | yes | yes | yes | (driver IS the user) | not observed | Common (4/5), execution-layer — **not definitional** (RouteSmart center survives without it) |
| Live tracking / GPS | yes | yes | yes | (navigation only in Route Planner) | not observed | Common (delivery-flavored); **not definitional** |
| POD capture | yes (incl. "Proof of Visit") | yes | yes | Dispatch product | not observed | Common (delivery flavor); **not definitional** |
| Customer notifications/ETAs | yes | yes | yes | Dispatch product | not observed | Common; **not definitional** |
| Recurring/strategic/master planning | Strategic + Recurring routing (recurring = add-on) | (recurring implied by verticals) | weekly planning, 5 weeks ahead | no | cycle-day balancing; 40 years of master planning | Common/variant; **not definitional** |
| Engine as standalone API | yes (API-first, GitHub, integrate portal) | yes (Engine API product) | yes (Web Service API) | no | services/embedded form | Variant posture |
| Territories/zones | Smartzone Routing, Regions & Zones | driver territories | service areas, clustering | no | GIS-based territory/route balancing | Common/advanced |
| Commercial truck/hazmat routing | Route4Trucks, commercial routing | no | truck & hazmat, truck navigation | no | industry-specific vehicle classes | Variant |
| Analytics on plan quality/execution | planned-vs-actual, business insights | end-of-day stats | analytics from route data | route completion stats | **Route Health Score** (plan quality) | Common; formulation varies |
| Marketplace/consumer demand generation | no | no | no | Connect product (separate) | no | Absent from the Type |

## Canonical Abstraction Hierarchy

### L0 — Defining Invariant (deliberately minimal)

Three jointly-held structures. Remove any one and the product stops being recognizable as a Route Optimization Platform:

1. **The stop/visit as the unit of demand** — a record of a place to be served (a location, commonly geocoded from an address), carrying the planning attributes of the visit (service duration, time window, load/quantity, priority, pickup/delivery pairing where applicable). Stops may come from an order system, a spreadsheet, an address database, or ad-hoc entry — the intake is not the invariant; the stop-as-planned-demand is. Remove it → a navigation app or an address book: nothing to plan.
2. **The optimization solve as the defining act** — the system's central computation: assigning stops to routes and sequencing each route (which stop in which order) under the configured stop- and resource-side constraints, against stated objectives (travel time/distance as default; balance, safety, priority, driver practicality where configured), and re-solvable when inputs change. With one resource the solve degenerates to pure sequencing — still in-type. Remove it → a manual route-drawing tool or a dispatch board where humans sequence; the Type's namesake dies.
3. **The route plan as the produced and held record** — the solve's output persists as route plans (ordered stop sequences bound to a resource or crew and to an operating day/period) that are inspected on a map/list, edited, re-optimized, and handed off for execution — dispatched to a driver app, sent to navigation, printed/exported as manifests, or returned as the structured output of an engine API. Remove it → a one-shot route calculator with no working artifact; nothing to dispatch, manage, or measure.

Jointly-held load-bearing checks: stops alone = geocoder/address book; solve alone = an algorithm/calculator (a library, not an operating application); plan alone = manual map-pinning; stops + solve without a held plan = one-shot calculator; stops + plan without solve = manual route planning (the pre-software baseline); solve + plan without stops-as-demand = territory drawing with nobody to visit.

Deliberately NOT in L0 (tested and rejected): multi-vehicle/fleet optimization (single-driver pole in-type — Spoke Route Planner); any specific constraint (windows/capacity are common, the *catalog* is not invariant); driver apps/POD/live GPS/customer notifications (execution layer — RouteSmart's center survives without them; delivery-flavored products carry them); map/navigation substrate (Google/Waze/HERE swap-able at Spoke); recurring/strategic planning (add-on at one sampled vendor); traffic/weather/ML-ETA data (era-current); cloud/SaaS form (RouteSmart's 40-year form includes non-SaaS lineages); demand generation (absent everywhere).

### L1 — Common Mature Structure

- Stop intake machinery: spreadsheet/CSV import, API sync, order-system integrations (e-commerce, CRM, ERP), address/customer databases, geocoding with correction
- Constraint catalogs: time windows, service durations, vehicle capacity (weight/cube/pieces), driver skills, priorities, pickup-delivery pairing, depot/start/end locations, avoidance zones and turn restrictions, truck/commercial restrictions
- Objective profiles / fine-tuning (distance vs time vs wait vs balance vs priority)
- Route editing surfaces: drag-and-drop reorder, move stops between routes, reassign drivers/vehicles, manual override, skip-optimization ordering
- The re-optimization loop: add/edit stops (including mid-route) → replan → updated ETAs
- Multi-route oversight map: all routes and drivers, progress, stop-level status
- Dispatch of routes to driver mobile apps; turn-by-turn navigation handoff (built-in or external nav apps)
- Delivery-flavor execution: live GPS tracking, POD capture, customer notifications/tracking links, ETAs
- Analytics: planned vs actual, route completion, driver performance, plan-quality measures
- Recurring route templates / weekly or cycle-day planning; territory/zone support

### L2 — Variant / Optional Structure

- Segment poles: personal driver planner (mobile, freemium, single user) ↔ team delivery routing ↔ mid-market plan+optimize ↔ enterprise strategic/high-density planning (GIS-led, services-led) ↔ engine/API-only consumption
- Work flavor: delivery routing vs field-service routing (visits, skills, appointments) vs high-density industrial service routing (waste, newspaper, meters, postal) vs sales routing
- Solve horizon: daily dynamic vs weekly/strategic master planning vs recurring templates
- Vehicle specialization: commercial truck/hazmat routing, EV considerations (era-current)
- Data enrichment: traffic patterns, predictive weather, historical/ML ETAs
- Deployment posture: self-serve SaaS vs services-led enterprise vs API platform

### L3 — Vendor-specific (kept out of the final document)

- Route4Me: "Route Optimization Platform" self-branding, patented-engine claim, constraint add-on marketplace packaging ("Business Rule - Predictive Weather" etc.), Routes-Saved-for-7-Days plan limit, Route4Trucks, Smartzone Routing, "It's Not The Route, It's The Optimization!", AI scenario-planning branding, 30M+ routes planned claim
- Routific: "spaghetti routes" framing, driver-happiness philosophy, Engine API product name, 179 ML models claim, driver-privacy tracking stance, 191M deliveries claim
- OptimoRoute: "Intelligent Drag & Drop" naming, 5-week-ahead weekly planning, multi-day long-haul + coordinated orders as beta features, breadcrumbs feature
- Spoke: Circuit→Spoke rebrand, scan/voice stop input, vehicle load order, Android Auto/CarPlay, 10-stop free limit, Google-Maps substrate, 1.5B deliveries/year claim
- RouteSmart: Route Health Score™, street-level safety constraints (right-side servicing, turn minimization), Routing University / Certified Routing Professional, FedEx ownership, INTERSECT conference, RouteSmart Online, 40-year lineage

## Vendor-specific Findings

See L3. Single-product findings that must not generalize:

- Plan-quality scoring as a named, branded measure (RouteSmart Route Health Score)
- Constraint marketplace packaging of individual business rules (Route4Me)
- Engine sold as a standalone named product (Routific Engine API; Route4Me's API-first posture is the broader analog)
- Safety objectives as first-class solve inputs (right-side servicing, turn minimization — RouteSmart)
- Voice/scan stop entry and vehicle load-order packing (Spoke)
- Retailer→courier marketplace attached to a routing vendor (Spoke Connect — separate product)

## Rejected Findings (considered and rejected as core)

- **Execution orchestration (dispatch, driver apps, POD, tracking, notifications) as definitional**: present in 4/5 sampled products but absent from RouteSmart's center; where present it is the dispatch/last-mile layer attached to a planning core. Consistent with the last-mile pass's ratified "engine as capability, not center" — the complement holds: execution is not the engine's center either.
- **Fleet/multi-vehicle optimization as definitional**: fails the single-driver pole (Spoke Route Planner is squarely the Type with no fleet roster).
- **Time-window servicing as definitional**: windows are the most common constraint (5/5 in some form) but Spoke's free tier and RouteSmart's safety-driven solves show the Type without window-centric machinery.
- **"Platform" as multi-module suite as definitional**: the Type includes single-purpose planners and API engines; the suite is packaging.
- **Traffic/ML/predictive data as definitional**: era-current; RouteSmart's 40-year OR core and offline-capable mobile planners satisfy the Type without them.
- **Route optimization as "just an algorithm" (not a Type)**: rejected — the market sustains multiple standalone products whose entire center is the solve-plus-plan; the TMS pass's framing ("algorithm capability vs management system") is resolved as: capability inside TMS/last-mile, standalone Type when stops+solve+plan are the product's own record system.

## Boundary Findings

| Neighboring Type | Relationship | Distinction (the "remove-what" test) |
|---|---|---|
| Last-mile Delivery Platform | closest sibling; RATIFIED from this side | Last-mile's unit of record is the delivery task (recipient, window, status lifecycle, POD closure) and its center is executing the day. Here the unit of record is the route plan and the center is the solve. Remove the optimization center → last-mile/dispatch. Remove the delivery-task execution record (POD, recipient comms, delivery networks) → this Type. Delivery-flavored routing products carry execution layers, but stripping them leaves the Type intact (RouteSmart proves it); a last-mile platform stripped of optimization remains last-mile (Detrack base tier proves the complement). |
| Delivery Scheduling Platform | upstream/parallel neighbor; joint-review flag DISCHARGED | Scheduling owns the when-structure (availability, offered slots, promised times as the worked object). Here timing exists as stop attributes feeding the solve; there is no availability structure and no consumer-facing promise machinery in the center. The OptimoRoute/Routific-class products the scheduling pass flagged at its operator pole are route-optimization-centered products with scheduling machinery attached — their center of gravity sits here. Remove the solve → scheduling; remove the when-structure center → this Type. |
| Dispatch Management | machinery inside delivery-flavored members | Dispatch owns the transversal assignment loop (queue × roster × assignment act × live picture). Here assignment is one output of the solve and is plan-shaped; sequencing is the essence. Remove sequencing/optimization → dispatch. |
| Transportation Management System | business-frame + unit-of-work seam (TMS pass) | TMS runs freight: loads, carriers, tendering, audit/pay. Here the unit is the stop-level route for own-resource field operations. Optimization depth inside TMS varies none→deep (TMS pass); routing engines attach to TMS as integrations (Route4Me lists "OMS & TMS" as an integration category). Remove freight management → this Type; remove the solve → TMS without optimization. |
| Fleet Management System | estate vs plan | FMS owns vehicles/telematics/maintenance as the system of record. Here vehicles appear as solving resources; telematics is an optional input (Route4Me telematics integrations). Remove the plan/solve → fleet management. |
| Navigation Application (consumer) | output surface, different Type | Navigation plans one traveler's single trip turn-by-turn, no multi-stop constrained solving, no persistent plan record, no resources. Route platforms produce plans and hand off to navigation (Spoke: built-in Google Maps / Waze / HERE). Remove the multi-stop constrained solve + held plan → navigation. |
| Field/agent scheduling (Agent Scheduling, Enterprise Resource Scheduling) | parallel machinery, different objective center | Those schedule people against work/appointments over time; the geography is secondary. Here the solve's objective is geometry/travel: who covers which stops in what order. Remove the travel-sequencing center → appointment scheduling. |
| Public Transit Journey Planner / passenger trip planning | different subject entirely | Plans a passenger's journey over published transit networks; no fleet, no stop pool owned by the operator. |
| School Transportation Management / other domain systems | engine-consumer relationship | Domain systems run their own frame (students, runs, guardians); routing engines serve them (RouteSmart's postal/utility/waste industries are engine-as-service to domain operations). Domain frame ≠ this Type. |

## Uncertainties

1. OptimoRoute operational click-paths unverified (support center unreachable ×2); constraint claims rest on vendor feature pages. No precise mechanics asserted beyond those pages' own statements.
2. Routific help center empty; its constraint depth (windows/capacity specifics) unverified — held generic.
3. Enterprise platform pole (Bringg-class) unreachable in prior sibling passes; this pass makes no claims about enterprise promise/orchestration mechanics.
4. RouteSmart's product internals (screens, workflow) behind sales-led pages; its role as the execution-light control case rests on what its public pages center (plan quality, safety, balance) — inference recorded as such, not as exhaustive product knowledge.
5. Exact feasibility/unassigned-stop behavior (what a solve does with impossible stops) observed nowhere at document depth; final doc avoids claiming specific infeasibility mechanics.
6. Algorithmic lineage (VRP/TSP class) is industry-common knowledge but not user-facing product structure; final doc names it only conceptually, without product-specific algorithm claims.
7. Regional planners (EU/JP) not sampled beyond Spoke's UK base and RouteSmart's global distributor network; assertions kept conceptual.

## Final Synthesis

A Route Optimization Platform is the planning-side system whose defining core is three jointly-held structures: (1) stops/visits as the unit of demand — records of places to be served carrying their planning attributes; (2) the optimization solve as the defining act — assigning stops to routes and sequencing each route under configurable constraints and objectives, re-solvable on change; (3) the route plan as the produced and held record — ordered, resource-bound, time-scoped sequences that are inspected, edited, overridden, re-optimized, and handed off for execution (driver app, navigation, print/export, or structured API output). Around this core sits the mature stack: intake machinery, constraint catalogs, objective fine-tuning, multi-route oversight, dispatch/tracking/POD/notifications (delivery flavor), recurring and strategic planning, and plan-quality analytics. The Type spans a personal driver planner and an enterprise high-density planning house without the core changing — multi-vehicle scope, execution machinery, and any specific constraint are common or variant, not definitional. All inherited seams settle from this side: vs last-mile (solve+plan center vs execution-orchestration center — ratified both directions), vs delivery scheduling (when-structure vs sequence-structure; the flagged operator-pole products' center of gravity is here), vs TMS (stop-level routing vs freight management), vs dispatch (plan-shaped assignment vs transversal assignment loop), vs fleet (plan vs estate), vs navigation (produced plan vs single-trip guidance). Taxonomy verdict: confirmed standalone Type; the delivery-scheduling pass's joint-review flag and the last-mile pass's pending route-optimization side are discharged.
