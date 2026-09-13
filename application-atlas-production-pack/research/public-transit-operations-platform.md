# Research Notes — Public Transit Operations Platform

## Research Goal

Understand what an operator-side public transit operations platform really is: the software a transit agency or operator uses to plan, resource, and run its scheduled passenger service (bus, metro, tram, light rail, passenger rail). The goal is a vendor-neutral model of the system's core objects, its plan-to-operations workflow, its real-time control loop, the rules that shape it, and its boundaries against neighboring Application Types (passenger apps, rail operations, generic fleet management, generic workforce scheduling, emergency CAD).

## Initial Boundary

Working hypothesis at start:

- The Type is the **operator/agency-facing** counterpart of the transit family. The rider-facing counterpart (journey planning, tickets, arrival info) is a different Type (Public Transit Passenger App).
- Expected core: the scheduled service (network + timetable), the assignment of vehicles and crew to that service, and the day-of-operations control loop.
- Likely confusions: Rail Operations Platform (rail-specific train running), Fleet Management System (generic vehicles), Employee Scheduling Platform (generic shifts), Computer-aided Dispatch (emergency, incident-driven), Transportation Management System (freight), School Transportation Management (student routing).

## Research Questions

1. What is the plan side? What objects make up the scheduled service (network, routes/patterns, stops, trips, timetables, service calendars)?
2. How does the plan become operable? What are vehicle schedules (blocks) and crew schedules (duties/runs/rosters), and how do they derive from the timetable?
3. What happens on the day of operations? How do dispatchers cover work, handle absences, breakdowns, and disruptions?
4. What does real-time control look like? What is monitored (vehicle position/status, adherence), what interventions exist, and how do they reach vehicles and crews?
5. How does crew work management work (bids, sign-on, timekeeping, payroll)?
6. What rules matter (union/collective agreements, service rules, connection protection, work-rule conflict checking)?
7. What surfaces exist (planning workbench, control center, dispatch desk, driver mobile, self-service, reports)?
8. Where are the boundaries — passenger app, rail ops, fleet management, employee scheduling, emergency CAD?
9. Historical check: would older, regional, paper-era, or differently positioned products still fit the definition?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Vendor | Philosophy / position |
|---|---|---|
| HASTUS | GIRO Inc. (Montreal) | Classic industry-standard scheduling & operations suite; deep optimization; 40+ years; large authorities/operators (MTA, RATP, SNCF, STM, De Lijn, Keolis, Transdev…) |
| IVU.suite | IVU Traffic Technologies (Berlin) | European integrated standard software for bus and rail; planning → dispatch → ticketing → passenger info → settlement; 50+ years; 500+ customers |
| Trapeze | Trapeze Software / Modaxo | North American incumbent agency suite: fixed-route scheduling, workforce management, EAM, paratransit, safety |
| Clever Devices (MAIOR + CleverCAD) | Clever Devices (now Hitachi Rail) | Real-time ITS specialist: CAD/AVL operations control + MAIOR planning/scheduling suite; agencies from ~30 to ~6000 vehicles |
| Swiftly | Swiftly, Inc. (San Francisco) | Modern cloud real-time data/operations layer: fleet visibility, OTP/headway management, RTPI — deliberately **without** scheduling/crew modules; 200+ agencies |

The sample deliberately spans: full-suite incumbents (HASTUS, IVU, Trapeze), a real-time specialist that also sells scheduling (Clever Devices), and a real-time-only data platform (Swiftly). This spread is what exposes which structures are definitional and which are packaging.

## Sources

Fetched 2026-09-09 (Tier 1/2 official vendor surfaces):

- GIRO — HASTUS software overview: https://www.giro.ca/en-ca/our-solutions/hastus-software/
- GIRO — HASTUS for schedulers: https://www.giro.ca/en-ca/our-solutions/hastus-software/hastus-for-schedulers/
- GIRO — HASTUS for operations managers: https://www.giro.ca/en-ca/our-solutions/hastus-software/hastus-for-operations-managers/
- IVU — IVU.suite home: https://www.ivu.com/en/
- IVU — Dispatching: https://www.ivu.com/en/solutions/dispatching
- IVU — Service Planning: https://www.ivu.com/en/solutions/service-planning
- Trapeze — home / suite: https://trapezegroup.com/
- Trapeze — Operations Management (Workforce Management): https://trapezegroup.com/operations-management/
- Clever Devices — home / solutions: https://www.cleverdevices.com/
- Clever Devices — CleverCAD: https://www.cleverdevices.com/products/clevercad/
- Clever Devices — Resource Scheduling (MAIOR): https://www.cleverdevices.com/solutions/resource-scheduling/
- Clever Devices — Operations Management (MAIOR): https://www.cleverdevices.com/solutions/operations-management/
- Swiftly — home / platform: https://goswift.ly/

**Source-access limitation:** www.optibus.com (root and /platform/) returned HTTP 403 on 2026-09-09, and help.optibus.com failed with a transport error — three attempts across two hosts, then abandoned per the network-restriction rule. Optibus is retained in the market picture as a known modern cloud scheduling/operations platform, but **no Optibus-specific observation below carries an A-layer claim**; nothing in the synthesis depends on it. Precise operational details (numeric limits, exact rule sets, module pricing/packaging) were not researched and are not asserted anywhere.

## Product Observations

Evidence layers: **A** = directly observed on the cited official page; **B** = cross-product commonality; **C** = canonical inference. All observations below are A-layer unless marked otherwise.

### HASTUS (GIRO)

- Self-description: "a complete software solution for bus, metro, tram and passenger rail operations, trusted by authorities and operators around the world." Suite organized as **Planning / Scheduling / Operations / On-demand transport / Customer info / Integration tools**. The Integration layer explicitly names integration with **AVL, APC and ticketing systems** (Connect module ships with every installation). [A]
- Scheduling side (HASTUS-Vehicle): manage **routes, run times, layovers, dwell times, and distances**; define **trips and timetables** according to service levels; create optimized **vehicle blocks** considering capacities, vehicle movement restrictions, unit availability; what-if scenarios. [A]
- Crew side (HASTUS-Crew): build **duties** for crew members "to cover vehicle schedules"; immediate validation feedback; cost and quality attributes; what-if; optimization "while considering the quality of resulting solutions". Rail variant: timetabling + track access + rolling stock + on-board crew + station staff in one system. [A]
- Operations side: **BidWeb** (employee bid process; roles and quotas respected; centralized real-time information; off-site bidding); **HASTUS-DailyCrew** (day-to-day operations, assignment changes, "quickly identify impacts of service disruptions and last-minute changes", continuous timekeeping calculations per employee for payroll accuracy, leaves/absences "while respecting rules and quotas"); **DispatchAssistant** ("ensure all service is covered and runs smoothly on the day of operations"; highlights tasks requiring immediate action; shows available employees and assignment details **with sign-in/sign-out information**; manages last-minute changes "such as vehicle breakdowns or operators being late"); **YardAssistant** (depot vehicle management: locations, assignments, maintenance activities, parking spots incl. electric buses); **HASTUS-SelfService** (absence/vacation requests, overtime volunteering, work/vacation exchanges "while ensuring respect of applicable rules", assignment-change communication). [A]
- Customer-information modules exist as a suite pillar ("provide, receive and process information" between agency and customers). [A]
- Longevity: "more than 40 years of international experience" — the Type predates modern cloud/mobile delivery. [A]

### IVU.suite (IVU Traffic Technologies)

- Self-description: "End-to-end solution for bus and rail… from planning, dispatch, fleet management, ticketing, and passenger information through to the settlement of transport contracts." Suite pillars: **Service Planning / Resource Planning / Dispatching / Fleet Management / Ticketing / Passenger Information / Controlling**. [A]
- Service planning (IVU.timetable / IVU.pool): "Planning your services **creates the framework for your operational tasks**." Route networks, headways, trips; conflict warnings when designated connections are not met; line-graph timetable display; timetable **versions** (e.g., construction/summer timetables); network-wide timetable aggregation from multiple operators; and the explicit cascade: "If you reschedule planned timetable deviations, the system ensures consistent planning information — **from trips and vehicle schedules through to duties**." Timetables are published and "suppl[ied] [to] operation control and passenger information systems". [A]
- Dispatching (IVU.vehicle): vehicle dispatch + depot management; plan "deployments, workshop visits and downtimes"; suggestion system for allocating vehicles to schedules; **automatic conflict checker** ("ensures that you adhere to all the relevant rules"); "**The system monitors all journeys in real time and alerts you to any disruptions**"; workshop orders created directly from dispatch; depot parking and (e-bus) charging planning; rail variant adds track-occupancy planning and shunting. [A]
- Personnel dispatch (IVU.crew + IVU.pad): "from roster layout and holiday planning to dispatch and precise settlement and evaluation"; configurable **rule system** checks job allocations and reports conflicts; real-time alerts when employees are absent; "Overtime, sickness, covering duties: IVU.crew registers every change immediately" with integrated payroll accounting; IVU.pad gives mobile staff duty schedules, duty swaps, manuals/forms. [A]
- Day-of-operations posture (homepage): "The system monitors all aspects of a trip, from the vehicle status and the timetable situation through to the current deployment of vehicles and staff. If any irregularities occur, it offers the right measures immediately." [A]
- Longevity: "developing integrated IT systems… for over 50 years"; "more than 500 customers worldwide". [A]

### Trapeze (Modaxo)

- Suite: **Enterprise Asset Management / Fixed Route Scheduling (route planning, optimization) / Fixed Route Traveler Experience / Mobility on Demand / RISC (Risk, Incident & Safety Compliance) / Workforce Management (Operations Management + Employee Empowerment)**. [A]
- Workforce Management / Operations Management ("Modern mission control"): **Efficient Daily Dispatch** ("applies agency rules consistently with tools to aid covering open work"); **Accurate Timekeeping and Payroll** ("automatically enforces timekeeping rules, audits transactions, and exports to payroll"); **Streamlined Bidding** ("automates bid configuration and bidding process, enables employees to bid off-site"); **Better Employee Management** (performance monitoring "customized to your policies"); **Safer and Optimized Vehicle Management** ("automates vehicle assignment tasks, matching vehicle type and driver skills to work requirements"). [A]
- Fixed Route Scheduling positioned as "planning and scheduling software… tailored to your unique fixed-route planning and scheduling needs" (route planning, optimization). [A]
- Traveler experience pillar sells "access to scheduled and real-time bus information" — the rider-facing edge of the same data. [A]

### Clever Devices (MAIOR suite + CleverCAD)

- Positioning: "Intelligent Transportation Systems… for transit agencies"; "From operations control to real-time passenger information. From safety and security to planning and scheduling." Customers "from the largest public transport agency in the United States with over 6000 vehicles to a small city agency with just 30". [A]
- MAIOR **Service Planning**: "define and manage your network in detail, plan your trips, optimize timetables". [A]
- MAIOR **Resource Scheduling**: "Simultaneous **blocking and run cutting** generates schedules that optimize vehicles and drivers and reduces the total number of **blocks and duties** required to perform your service"; Vehicle Scheduling = "create vehicle **blocks** that maximize the time each of your vehicles are in **revenue service**"; Operator Scheduling = "generate the fewest driver **duties** necessary to operate your planned services… without fear of breaking **union or business rules**"; Rostering = "assemble operator work, combining it into weekly **rosters of biddable work** while adhering to all union and business rules". [A]
- MAIOR **Operations Management**: "manage the unpredictable changes that occur every day"; Assignment ("optimize driver assignments while balancing the workload, following time-off requests, **labor rules, and agency regulations**"); Daily Management ("quickly react to unplanned changes to your service"); Operator Portal ("self-serve web-based personnel kiosk… view and manage schedules and connect with management"); WFM module (centralized driver data: performance, activities, incidents, attendance; payroll integration; training, certifications, random drug/alcohol testing). [A]
- **CleverCAD** (CAD/AVL): "a clear, **real-time picture of the location and status of every in-service vehicle** and the ability to quickly react to service disruptions in real time"; situational awareness = "real-time vehicle location, voice communications, and **on-time performance**"; text messaging between dispatchers and vehicles; "**Event-driven incident management**: auto-generated, user-defined incident reports for critical events"; "**Mobile route supervision**" app for road supervisors; "**Disruption management**: react to unavoidable service disruptions and update your passengers in real time". [A]
- Adjacent pillars: SmartYard (depot management), BusTime (real-time arrival information), AVM (vehicle health monitoring), CleverCloud (hosted ITS). [A]

### Swiftly

- Positioning: "the industry's leading data platform for knowing where your vehicles **were, are, and will be next**… This platform powers operations and performance insights." [A]
- Products: **Proactive operations** ("dynamic real-time fleet visibility and management"); **Metronome** ("real-time vehicle operations"); **Transitime** (real-time passenger information); **Insights** (historical performance); **Integrations and APIs** ("real-time data quality monitoring across existing systems, plus APIs and open data standards"). [A]
- Operations solution: "boost **on-time performance and headway adherence** with real-time adjustments for your operators and historical insights for operations staff." [A]
- Scheduling solution is data-for-scheduling, not scheduling: "optimize your schedule using actual run-times, vehicle speeds, and dwell times" — Swiftly consumes the agency's schedule and AVL data; it does **not** build blocks, duties, or rosters, and has no crew dispatch/timekeeping. [A]
- Marketing outcome claims (OTP +40%, prediction accuracy +50%) are vendor claims — recorded here as claims only, not treated as evidence of mechanism. [A, claim-only]

## Cross-product Comparison

| Structure | HASTUS | IVU | Trapeze | Clever Devices | Swiftly | Reading |
|---|---|---|---|---|---|---|
| Scheduled service plan held as reference (network/trips/timetable/calendar) | ✓ (Vehicle: trips, timetables, service levels) | ✓ (IVU.timetable; "framework for your operational tasks") | ✓ (Fixed Route Scheduling) | ✓ (MAIOR Service Planning) | ✓ (consumed; "were, are, will be next") | **5/5 — definitional** |
| Real-time monitoring of running service vs plan | ✓ (AVL integration + DailyCrew/DailyVehicle day-of-ops) | ✓ ("monitors all journeys in real time") | ✓ (daily dispatch mission control) | ✓ (CleverCAD CAD/AVL) | ✓ (native; Proactive operations) | **5/5 — definitional** |
| Deviation → intervention loop (disruptions, incidents, reassignment) | ✓ (DispatchAssistant last-minute changes; disruption impacts) | ✓ (disruption alerts + "right measures immediately") | ✓ (covering open work; responding to operational changes) | ✓ (disruption management; event-driven incident management) | ✓ (real-time adjustments for operators) | **5/5 — definitional** |
| Vehicle scheduling into blocks | ✓ | ✓ | ✓ (fixed-route optimization) | ✓ (blocking) | ✗ | 4/5 — common mature |
| Crew scheduling into duties/runs under work rules | ✓ (duties cover vehicle schedules) | ✓ (IVU.crew rule system) | ✓ (agency rules) | ✓ (union/business rules) | ✗ | 4/5 — common mature |
| Rosters / biddable work / bid process | ✓ (BidWeb) | ✓ (roster layout) | ✓ (streamlined bidding) | ✓ (rosters of biddable work) | ✗ | 4/5 — common mature |
| Day-of-ops crew dispatch (cover open work, absences) | ✓ | ✓ | ✓ | ✓ | ✗ | 4/5 — common mature |
| Sign-on/sign-out + timekeeping → payroll | ✓ (DailyCrew timekeeping) | ✓ (settlement + payroll) | ✓ (timekeeping/payroll export) | ✓ (payroll integration) | ✗ | 4/5 — common mature |
| Depot / yard management (parking, maintenance coupling) | ✓ (YardAssistant) | ✓ (depot mgmt, workshop orders) | ✓ (vehicle assignment) | ✓ (SmartYard) | ✗ | 4/5 — common mature |
| Driver self-service / mobile surface | ✓ (SelfService) | ✓ (IVU.pad) | ✓ (Employee Empowerment) | ✓ (Operator Portal) | ✗ (operator-facing adjustments only) | 4/5 — common mature |
| Passenger information production (RTPI) | ✓ (customer info modules) | ✓ (passenger information pillar) | ✓ (traveler experience) | ✓ (BusTime/AVA) | ✓ (Transitime) | 5/5 — common mature, not definitional |
| Performance analytics (OTP, headway, historical) | ✓ (scheduling quality attributes; BI via integrations) | ✓ (Controlling pillar) | ✓ (Insight reporting) | ✓ (CleverMetrix/Reports) | ✓ (Insights) | 5/5 — common mature |
| Integration spine (AVL/APC/ticketing/EAM/payroll) | ✓ (Connect: AVL, APC, ticketing) | ✓ (fleet mgmt, ticketing) | ✓ (EAM) | ✓ (AVM, APC, payroll) | ✓ (APIs, data quality across existing systems) | 5/5 — common mature |
| E-bus charging management | ✓ (recharging planning) | ✓ (charging mgmt) | ✓ (EV module) | ✓ (EV management) | ✗ | 4/5 — era-current, optional |
| Rail packaging (train paths, track occupancy) | ✓ (rail modules) | ✓ (IVU.rail) | ✓ (EAM for Rail; rail solutions) | ✓ (CleverCAD for Rail, MAIOR for Rail) | ✗ | 3/5 — variant axis |
| Paratransit / on-demand modules | ✓ (on-demand pillar) | (via partners/products) | ✓ (Mobility on Demand) | ✓ (GreyHawk) | ✗ | variant axis |

Key comparative findings:

1. **Every sampled product, including the real-time-only one, works against the agency's scheduled service.** Even Swiftly, which builds no schedules, describes itself entirely in terms of the timetable-bound question "where vehicles were, are, and will be next". The scheduled service is the Type's reference frame. [B→C]
2. **Every sampled product operates the service in real time on the day of operations** — monitoring against the plan, surfacing deviations, intervening. Products without this leg are scheduling/planning tools, not operations platforms. [B→C]
3. **Resource scheduling (vehicle blocks + crew duties) is near-universal but not universal**: 4/5. The real-time-layer product shape (Swiftly) proves a market-real product can carry the operations loop without owning resource scheduling — it consumes schedules produced elsewhere. Therefore resource scheduling is common mature structure, not definitional. [B→C]
4. **The plan→ops cascade is explicit in vendor language**: IVU states planning "creates the framework for your operational tasks" and that changes propagate "from trips and vehicle schedules through to duties"; HASTUS crew duties exist "to cover vehicle schedules"; MAIOR generates "the fewest driver duties necessary to operate your planned services". The dependency chain timetable → vehicle schedule → duty → day-of-ops assignment is the Type's backbone. [B]
5. **Work rules are a first-class system feature**, not configuration trivia: union/business rules in crew scheduling (MAIOR, HASTUS, IVU), agency rules in daily dispatch (Trapeze), rules and quotas in absence management (HASTUS), conflict checkers in vehicle dispatch (IVU). [B]
6. **The same vendor families span into rail and into rider-facing surfaces** — the Type's edges are bundling boundaries, not product-family boundaries. [B]

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (minimal)

Two jointly-held structures:

1. **The scheduled service as the plan of record.** The system holds the agency's timetabled service — its network (routes/patterns and stops), its trips with times, and its operating calendar (service levels/versions) — as the authoritative reference for what should run. The plan may be authored in-product (dominant shape) or imported from a scheduling system (real-time-layer shape); either way the running service is measured against it.
   - Remove → generic fleet tracking (vehicles without a service to deliver) or a generic workforce scheduler (shifts without service semantics). The transit semantics die.

2. **The real-time operations loop over the running service.** During the operating day, the system tracks vehicles (and the crews operating them) against the plan — position, status, adherence — surfaces deviations (late/early, bunching/gapping, breakdowns, uncovered work), and executes control interventions (communicate with vehicles/crews, reassign, manage incidents, adjust service) that are recorded against the operation.
   - Remove → a planning/scheduling tool or a passive data feed. The "operations" in the Type name dies.

Jointly-held load-bearing analysis:

- 1 alone = timetable/scheduling software (GTFS-style plan authoring, runcutting) — planning territory, not an operations platform.
- 2 without 1 = blind real-time tracking with nothing to adhere to — generic AVL/fleet-tracker territory.
- 1+2 = the operations platform core; everything else in the market is depth, packaging, or adjacent bundling.

### L1 — Common Mature Structure

Present in most mature products (4–5 of 5 in the sample) but not required to recognize the Type:

- **Vehicle scheduling (blocking)** — chaining timetabled trips into vehicle assignments that maximize revenue-service time (HASTUS-Vehicle, MAIOR blocking, IVU resource planning, Trapeze fixed-route optimization).
- **Crew scheduling (run cutting / duties)** — covering vehicle work with driver duties under union/business rules; simultaneous blocking+run-cutting optimization (MAIOR), duty validation with cost/quality attributes (HASTUS-Crew).
- **Rosters and bids** — assembling duties into weekly rosters of biddable work; bid processes with role/quotas and off-site bidding (BidWeb, Trapeze bidding, MAIOR rostering).
- **Day-of-operations crew dispatch** — covering open work from absences, applying agency rules, sign-in/sign-out visibility (DispatchAssistant, IVU.crew, Trapeze daily dispatch, MAIOR daily management).
- **Timekeeping → payroll** — continuous per-employee timekeeping with rule enforcement, audits, payroll export (HASTUS-DailyCrew, IVU.crew settlement, Trapeze timekeeping/payroll, MAIOR WFM).
- **Depot / yard management** — vehicle parking, depot assignments, maintenance coupling, charging for e-fleets (YardAssistant, IVU.vehicle depot, SmartYard).
- **Disruption / incident management** — event-driven incident records, disruption handling, passenger-information updates (CleverCAD, IVU disruption alerts, DispatchAssistant).
- **Passenger information production (RTPI)** — feeding real-time arrival/prediction data to rider surfaces (BusTime, Transitime, IVU passenger information, HASTUS customer info, Trapeze traveler experience).
- **Performance analytics** — OTP, headway adherence, historical run-times feeding back into planning (Swiftly Insights, CleverMetrix, IVU Controlling, Trapeze Insight).
- **Integration spine** — AVL, APC, ticketing, EAM/maintenance, payroll interfaces (HASTUS Connect, IVU fleet/ticketing, Clever AVM/APC, Trapeze EAM, Swiftly APIs).
- **Driver self-service / mobile** — duty schedules, swaps, absence requests, documents on a mobile/kiosk surface (IVU.pad, HASTUS-SelfService, MAIOR Operator Portal, Trapeze Employee Empowerment).

### L2 — Variant / Optional Structure

- **Mode packaging**: bus-only, bus+metro+tram, or including passenger rail (rail packaging adds train paths, track occupancy, formations — see Boundary Findings).
- **Product shape**: full-suite (plan + resource + ops in one system) vs real-time-layer (ops + analytics over imported schedules and third-party AVL).
- **Deployment**: on-premises control-center installations (legacy norm) vs vendor-hosted cloud (IVU.cloud, CleverCloud, Swiftly SaaS).
- **Regional work-rule regimes**: union/collective-agreement rule engines differ by jurisdiction; bid/roster practices are regionally shaped (e.g., North American bid processes vs European duty rosters).
- **E-fleet machinery**: charging management, range prediction, depot/opportunity charging planning (era-current).
- **Adjacent bundling**: ticketing/fare back office, paratransit/on-demand modules, safety/incident compliance (Trapeze RISC), EAM/maintenance depth.
- **Customer scale**: from ~30-vehicle city agencies to 6000+ vehicle metropolitan authorities (Clever Devices' own customer framing).

### L3 — Vendor-specific Structure (Research Notes only)

- HASTUS: BidWeb, DailyCrew, DailyVehicle, YardAssistant, DispatchAssistant, SelfService, MinBus (e-bus scheduling), Connect integration module.
- IVU: IVU.timetable, IVU.trainpath, IVU.pool, IVU.vehicle, IVU.crew, IVU.pad, IVU.rail, IVU.cloud.
- Trapeze: RISC (safety/event compliance), Insight (reporting), Advisor (scheduling toolkit), FX bus-stop integration.
- Clever Devices: CleverCAD, SmartYard, BusTime, AVA, Celrado, IVN (vehicle logic unit), CleverWorks, CleverCloud, MAIOR suite naming.
- Swiftly: Metronome, Transitime, Insights, Connected Transit Platform branding; marketing outcome statistics (OTP/prediction improvements) — claims, not mechanisms.

## Boundary Findings

- **Public Transit Passenger App** (rider-facing): journey planning, ticket purchase, arrival info for the rider. The ops platform *produces* the real-time data the passenger app *consumes*; the feed (e.g., GTFS-RT-class standards) is the seam. Remove the operator-side plan/control and only the rider surface remains → passenger app territory.
- **Rail Operations Platform**: the sampled vendor families span both (IVU.rail, HASTUS rail modules, CleverCAD for Rail). The seam is the object of work: rail operations centers on train running over railway infrastructure — train paths, track occupancy, shunting, signaling-adjacent concerns (IVU.rail's own rail features) — while transit operations centers on delivering the agency's scheduled passenger service across road/mixed modes. A rail product whose center is path/occupancy/interlocking is Rail Operations; the same vendor's bus/metro service-delivery system is this Type. **Taxonomy note recorded for STATUS**: the two leaves share vendor families; the seam holds but is packaging-adjacent and worth a future joint review.
- **Fleet Management System**: generic vehicles as assets (maintenance, fuel, generic dispatch) with no timetabled service. Transit ops binds vehicles to trips and measures them against the timetable. The maintenance leg of transit ops platforms (workshop orders, EAM integration) is exactly the seam — integration, not identity.
- **Employee Scheduling Platform**: generic shift scheduling against demand. Transit crew scheduling is bound to vehicle work derived from the timetable (duties cover blocks) under transit work rules. A product with only the crew leg (no service plan, no real-time loop) is employee-scheduling territory; the crew leg inside this Type is common mature structure, not the definition.
- **Computer-aided Dispatch / CAD (police/EMS)**: incident-driven emergency dispatch with units responding to calls. Transit "CAD/AVL" (CleverCAD) borrows the name but the center is the timetable and service adherence, not emergency incidents; incident management exists as a capability inside the operations loop. Emergency CAD's record is the call/incident; transit ops' record is the scheduled service and its operation.
- **Transportation Management System / TMS**: freight/shipping logistics — different domain, no passenger service semantics.
- **School Transportation Management**: student-to-stop routing and school-run specifics; public scheduled service is not the object.
- **Mobility-as-a-Service Platform**: rider-side multi-provider aggregation and payment (sibling pass already documented); operator-side service running is this Type.
- **Taxi Dispatch Platform**: on-demand ride assignment; no timetable as reference frame.
- **Airport Operations Platform**: airport-specific resource/flight operations; different domain object.

"Remove-what" test summary: remove the timetable-bound service semantics → fleet management / employee scheduling / generic AVL; remove the real-time loop → scheduling/planning software; remove the operator side entirely → passenger app / MaaS.

## Historical / Market-Sample Check

- Longevity evidence: GIRO states "more than 40 years of international experience"; IVU "over 50 years" — the Type long predates cloud, mobile apps, and modern AVL. [A]
- Paper-era thought experiment: a mid-20th-century bus company ran on a timetable book (the plan of record), run boards / paddle sheets (vehicle and crew assignment derived from the timetable), and a control room with radio and a wall map (real-time monitoring and intervention), plus punch clocks feeding payroll. Both L0 legs are satisfied with no software-era machinery — the definition does not over-fit to AVL, cloud, or optimization engines. [C]
- The optimization engine is **not** definitional: manual runcutting and hand-built rosters satisfy the core; optimizers (HASTUS, MAIOR, IVU) are the mature implementation of the same structures. [C]
- The real-time-layer product shape (Swiftly) is itself a historical pattern: schedule-consuming, prediction-centric operations systems (the Transitime lineage) existed before the current full-suite consolidation. [A]

## Uncertainties

- **Optibus**: unreachable (403 ×2, transport error ×1). Its exact module boundaries (scheduling vs operations vs passenger experience) could not be verified; excluded from all evidence claims. If later reachable, it would most likely reinforce L1 (cloud-native scheduling+ops) — but this is expectation, not evidence.
- **Exact rule semantics**: the sample shows work-rule engines exist everywhere (conflict checkers, rule systems, quotas) but the precise rule sets (spread penalties, break rules, overtime triggers) are jurisdiction- and product-specific; no precise rule asserted in the final document.
- **Paratransit/on-demand**: present as modules in 3/5 sampled vendors; whether demand-responsive operations deserves its own Type or is a variant was not fully resolved here — recorded as a possible future boundary question (the directory has no dedicated DRT leaf; Trapeze MOD and HASTUS on-demand pillars treat it as a sibling service inside the agency suite).
- **Fare/ticketing back office**: bundled in IVU's suite pillar and integrated elsewhere; the boundary with fare-system products was not deeply researched (no dedicated leaf conflict identified in this pass).
- **Trapeze AVL/real-time depth**: the fetched pages evidence workforce/dispatch and scheduling; real-time monitoring is implied by the "mission control" positioning and the traveler-experience real-time data but was not observed at CleverCAD-level detail. Assertions about Trapeze's real-time leg are held at common-structure strength via the category, not A-layer detail.

## Final Synthesis

A Public Transit Operations Platform is the operator-side system of record for a scheduled passenger transit service. Its defining core is two jointly-held structures: **the scheduled service as the plan of record** (network, timetabled trips, operating calendar — the authoritative reference for what should run) and **the real-time operations loop** (vehicles and crews tracked against that plan on the day of operations, deviations surfaced, control interventions executed and recorded). Around that core, mature products standardly add the resource layer that turns the plan into assignable work (vehicle blocks, crew duties, rosters and bids), the day-of-operations crew machinery (dispatch, sign-on, timekeeping → payroll), depot management, disruption/incident handling, passenger-information production, performance analytics, and an integration spine to AVL, APC, ticketing, maintenance, and payroll systems. The market realizes the Type in two shapes — the full suite that authors the plan and runs the operation in one system, and the real-time layer that runs the operation over an imported plan — plus mode variants (bus, metro, tram, passenger rail) and regional work-rule regimes. The Type is bounded from rider-facing transit apps (consumes, not operates), from rail operations (infrastructure-centric train running), from generic fleet and workforce scheduling (no service semantics), and from emergency CAD (incident-driven, not timetable-driven).
