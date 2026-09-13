# Public Transit Operations Platform

## Overview

A **Public Transit Operations Platform** is the operator-side system a transit agency or transport operator uses to plan, resource, and run its scheduled passenger service — buses, metros, trams, light rail, and commonly passenger rail as well.

The defining structure is small:

```text
The scheduled service (plan of record)
└── network: routes/patterns + stops
    └── timetabled trips + operating calendar
        └── run in real time against that plan
            └── vehicles & crews tracked, deviations surfaced,
                control interventions executed and recorded
```

Everything else the market associates with this software — vehicle blocking, crew scheduling and rosters, bid processes, depot management, timekeeping and payroll, disruption management, real-time passenger information, performance analytics — is standard capability that mature products carry, not what makes the product an operations platform. A product that only plans the service is scheduling software; a product that only tracks vehicles is a fleet tracker. The operations platform is defined by holding both: the plan, and the live operation of that plan.

## Users & Context

The primary users are the transit agency's or operator's own staff, organized around the life of the service plan:

- **Service planners** — design the network: routes, stop patterns, running times, trip frequencies, and the timetables that define what service is promised.
- **Schedulers** — turn the timetable into assignable work: vehicle schedules (blocks) and crew schedules (duties/runs), then assemble them into rosters under the applicable work rules.
- **Control-center dispatchers / operations managers** — run the day of operations: monitor vehicles against the plan, cover uncovered work, manage disruptions and incidents, direct vehicles and crews.
- **Depot / yard supervisors** — manage vehicle parking, assignments, and the hand-off between maintenance and service.
- **Drivers / operators** — the executing role: receive their duty, sign on, run their vehicle work, report status; interact through mobile or depot-kiosk surfaces.
- **Roster/bid administrators and payroll staff** — run bid processes, administer leaves and swaps, and consume timekeeping records.

The work environment is an agency back office and control center, with mobile and depot surfaces reaching the field. The rhythm is layered: seasonal and annual timetable versions, weekly rosters, and the daily operating cycle that begins with sign-on and ends with timekeeping.

## Core Model

### The Defining Core

**1. The scheduled service as the plan of record.** The system holds the agency's timetabled service as the authoritative reference for what should run:

- the **network** — routes or lines, their patterns, and the stops they serve;
- **trips** — individual service runs with times, organized into timetables per service level (weekday, weekend, holiday) and operating-calendar **versions** (seasonal schedules, construction timetables);
- the plan is the frame against which everything downstream is measured. In the dominant product shape the plan is authored in the platform itself; in the real-time-layer shape it is imported from a scheduling system — either way, the running service is measured against it.

**2. The real-time operations loop.** On the day of operations the system tracks vehicles — and the crews operating them — against the plan: position, status, and adherence. It surfaces deviations (late or early running, bunching and gaps, breakdowns, uncovered work) and executes control interventions: communicating with vehicles and crews, reassigning work, managing incidents, and adjusting service. Interventions are recorded against the operation.

Remove the plan and the system is blind tracking; remove the loop and the system is a planning tool. The two together are the Type.

### The Resource Layer: How the Plan Becomes Assignable Work

Mature products standardly derive assignable work from the timetable in a fixed dependency chain:

```text
Timetable (trips)
  → Vehicle schedule (blocks): trips chained to vehicles
      → Crew schedule (duties/runs): covering the vehicle work
          → Rosters: duties assembled into weekly biddable work
              → Day-of-operations assignments: named people on named work
```

- A **vehicle block** chains timetabled trips — plus pull-outs, layovers, and returns — into one vehicle's day, maximizing time in revenue service.
- A **duty (run)** covers a portion of vehicle work for one crew member, built under the applicable union and business rules.
- **Rosters** combine duties into weekly patterns of biddable work; bid processes allocate them to employees under role and quota rules.

A change to the timetable propagates down this chain — vendors describe the system keeping trips, vehicle schedules, and duties consistent when plans change.

### Standard Capabilities Around the Core

Mature products commonly carry most of the following:

- **Day-of-operations crew dispatch** — covering open work when operators are absent or late, applying agency rules, with sign-in/sign-out visibility.
- **Timekeeping → payroll** — continuous per-employee timekeeping with rule enforcement, transaction audits, and export to payroll systems.
- **Depot / yard management** — vehicle parking and depot assignments, coupled to maintenance; charging planning for electric fleets.
- **Disruption / incident management** — event-driven incident records, disruption handling, and updates pushed to passenger information.
- **Passenger information production** — real-time arrival and prediction feeds consumed by rider-facing apps, signage, and announcements.
- **Performance analytics** — on-time performance, headway adherence, and historical run-times that feed back into planning.
- **Integration spine** — connections to AVL (automatic vehicle location), automatic passenger counters, ticketing, maintenance/EAM, and payroll systems.

### One Structure, Many Implementations

The core is written conceptually; products realize it differently:

```text
Concept:  Plan of record
Realizations:  authored in-product (full suites) · imported schedule
               consumed from a scheduling system (real-time layers)

Concept:  Real-time vehicle state
Realizations:  onboard AVL hardware feeding the control center ·
               third-party AVL feeds ingested by a data platform

Concept:  Work-rule enforcement
Realizations:  configurable rule engines checking duties and
               assignments · conflict checkers on vehicle dispatch ·
               rule-gated absence and swap workflows
```

## How It Works

### Plan: build the service

```text
Define/adjust the network (routes, patterns, stops, running times)
→ create trips and timetables per service level
→ check connections and resolve conflicts
→ publish the timetable version
→ the plan becomes the framework for all operational tasks
```

### Resource: turn the plan into work

```text
Chain trips into vehicle blocks
→ cut blocks into crew duties under work rules
→ validate duties (rules, cost, quality)
→ assemble duties into rosters
→ run the bid process / allocate work to employees
```

### Operate: run the day

```text
Sign on (depot/kiosk/mobile) → vehicle and crew take up their block/duty
→ control center tracks every in-service vehicle against the plan
→ deviations surface (late/early, bunching, breakdown, absence)
→ dispatcher intervenes: instruct vehicle/crew, cover open work,
   reassign, log the incident
→ service changes flow to passenger information
→ sign off → timekeeping records feed payroll
```

### Learn: close the loop

```text
Actual run-times, speeds, dwell times, adherence accumulate
→ performance analytics (OTP, headway, route-level diagnosis)
→ insights feed the next planning cycle
```

The defining loop is the middle one: **plan → operate against the plan → intervene → record**. The resource layer and the analytics loop are the standard machinery that makes it work at agency scale.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Planning / scheduling workbench

The planner's and scheduler's primary surface.

- network maps, timetable graphs (lines against time), trip tables
- primary actions: edit routes/patterns/trips, adjust running times, build and validate blocks and duties, run what-if scenarios and optimizations

### Control center / operations dashboard

The dispatcher's real-time surface.

- live map and list of in-service vehicles with schedule adherence, status, and communication state
- primary actions: monitor adherence, contact vehicle/crew (voice or text), cover open work, reassign, log incidents, trigger passenger-information updates

### Dispatch / crew desk

The day-of-operations workforce surface.

- today's duties and assignments, available employees, uncovered work flagged for action, sign-in/sign-out state
- primary actions: assign and reassign duties, record absences, manage swaps and overtime, note events against employees

### Driver / operator surfaces

Mobile app or depot kiosk for the executing role.

- duty schedule, documents and manuals, swap and absence requests, sign-on
- primary actions: view duty, request changes, communicate with dispatch

### Depot / yard view

- vehicle locations and statuses in the depot, parking assignments, maintenance coupling
- primary actions: assign vehicles to blocks, plan parking, hand off to/from maintenance

### Analytics / reporting

- on-time performance, headway adherence, historical run-time and ridership views
- primary actions: query by route/time/stop, compare periods, export for planning

### Employee self-service

- bids, absence and vacation requests, overtime volunteering, work exchanges — all validated against applicable rules

## Important Rules / Behaviors

### The plan is the measure

Adherence — on-time performance, headway management — is defined against the held timetable. Real-time data has no operational meaning in this Type without the plan to measure it against.

### Work rules are first-class

Crew scheduling and daily dispatch run under explicit rule systems: union and collective-agreement rules shape which duties are legal, agency rules shape how open work is covered, and quotas govern bids, absences, and swaps. Products expose conflict checking and validation as core behavior, not add-ons — an illegal duty or assignment is flagged before it reaches the field.

### Changes cascade

A timetable change propagates through vehicle schedules and duties; a day-of-operations change (breakdown, absence) propagates through assignments and passenger information. The system's value is keeping these layers consistent; vendors describe this consistency explicitly.

### The day is recorded

Sign-ons, assignments, interventions, incidents, and timekeeping entries accumulate against the operation. This record is what feeds payroll, incident review, and performance analytics — and what distinguishes an operations system from a passive tracking feed.

### Coverage is the dispatcher's binding constraint

On the day of operations, every piece of scheduled work must be covered. Absences, breakdowns, and late operators create open work that the dispatch surface highlights for immediate action; leaving it uncovered means service that was promised does not run.

## Variants

- **Mode packaging** — bus-only agencies; multi-modal bus/metro/tram operators; products extended into passenger rail, where rail-specific machinery (train paths, track occupancy, rolling-stock formations) appears beside the service-delivery core.
- **Product shape** — the full suite (plan authored and operated in one system) versus the real-time layer (operations, prediction, and analytics run over a schedule imported from elsewhere and third-party AVL feeds).
- **Deployment** — on-premises control-center installations (the legacy norm for large authorities) versus vendor-hosted cloud delivery.
- **Regional work-rule regimes** — bid-based work allocation in some markets, duty-roster allocation in others; rule engines are configured per jurisdiction and collective agreement.
- **Electric fleet machinery** — charging management, range prediction, and charge-aware scheduling as an increasingly standard layer for e-bus fleets.
- **Adjacent bundling** — ticketing/fare back office, paratransit and on-demand service modules, safety and incident compliance, and enterprise asset management are commonly bundled by suite vendors; they are adjacent capabilities, not the defining core.
- **Customer scale** — the same Type spans small-city agencies with dozens of vehicles and metropolitan authorities with thousands.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Public Transit Passenger App | rider-facing counterpart | journey planning, tickets, and arrival info for the rider; it *consumes* the real-time data this platform *produces* |
| Rail Operations Platform | adjacent, shared vendor families | rail ops centers on train running over railway infrastructure (train paths, track occupancy, signaling-adjacent work); this Type centers on delivering the scheduled passenger service across road/mixed modes |
| Fleet Management System | adjacent | generic vehicles as assets (maintenance, fuel, generic dispatch) with no timetabled service; here vehicles are bound to trips and measured against the timetable |
| Employee Scheduling Platform | adjacent | generic shift scheduling against demand; here crew schedules are derived from vehicle work under transit work rules — a crew-only product without the service plan and real-time loop belongs there |
| Computer-aided Dispatch / CAD (police, EMS) | name-adjacent | emergency CAD is incident-driven (units respond to calls); transit CAD/AVL is timetable-driven (service adherence is the center); incident management exists here as a capability inside the operations loop |
| Transportation Management System / TMS | different domain | freight and shipping logistics, no passenger service semantics |
| School Transportation Management | adjacent domain | student-to-stop routing and school-run specifics rather than public scheduled service |
| Mobility-as-a-Service Platform | rider-side aggregation | multi-provider journey planning, booking, and payment for the traveler; operator-side service running is this Type |
| Taxi Dispatch Platform | adjacent | on-demand ride assignment with no timetable as reference frame |

The most important boundary is the rider/operator split: the same real-time data feeds both, but the passenger app plans a journey while the operations platform runs the service. The second most important is the rail seam: several vendors ship both products, and the dividing object is infrastructure-centric train running versus service-centric transit delivery.

## Representative Products

- **HASTUS** (GIRO) — classic industry-standard scheduling and operations suite for bus, metro, tram, and passenger rail; used by large authorities and operators worldwide.
- **IVU.suite** (IVU Traffic Technologies) — integrated European standard software spanning service planning, dispatch, fleet management, ticketing, and passenger information for bus and rail.
- **Trapeze** (Modaxo) — North American agency suite: fixed-route scheduling, workforce/operations management, asset management, paratransit.
- **Clever Devices** — real-time ITS specialist combining the MAIOR planning/scheduling suite with CleverCAD CAD/AVL operations control; serves agencies from small city systems to the largest US agencies.
- **Swiftly** — modern cloud real-time data and operations layer (fleet visibility, on-time performance, passenger information) running over agencies' existing schedules and systems.

The definition was checked against the real-time-layer shape (Swiftly) and against the vendors' own 40–50 year histories so that the core does not over-fit to today's full-suite, cloud-era packaging.

## Sources

Research date: **2026-09-09**

- GIRO — HASTUS software overview, for schedulers, for operations managers: https://www.giro.ca/en-ca/our-solutions/hastus-software/ (and linked role pages)
- IVU Traffic Technologies — IVU.suite overview, Dispatching, Service Planning: https://www.ivu.com/en/ , https://www.ivu.com/en/solutions/dispatching , https://www.ivu.com/en/solutions/service-planning
- Trapeze — suite overview and Operations Management: https://trapezegroup.com/ , https://trapezegroup.com/operations-management/
- Clever Devices — solutions overview, CleverCAD, MAIOR Resource Scheduling, MAIOR Operations Management: https://www.cleverdevices.com/ , https://www.cleverdevices.com/products/clevercad/ , https://www.cleverdevices.com/solutions/resource-scheduling/ , https://www.cleverdevices.com/solutions/operations-management/
- Swiftly — platform overview: https://goswift.ly/

> Sourcing limitation: Optibus, a prominent modern cloud scheduling/operations platform, could not be fetched from the research environment (repeated access failures on 2026-09-09) and is therefore not used as evidence; no product-specific claims about it are made. Precise operational details (numeric limits, exact rule sets, packaging tiers) were not researched and are intentionally not stated. Detailed product-by-product observations, the cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
