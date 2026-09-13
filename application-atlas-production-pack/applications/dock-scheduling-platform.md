# Dock Scheduling Platform

## Overview

A **Dock Scheduling Platform** (also called a dock appointment scheduling system) is the facility-side scheduling system of record for freight arrivals and departures. It holds the facility's dock doors and their operating hours as bookable time capacity, manages appointments that bind loads and carriers to specific doors and time windows, and governs the request-and-confirmation loop between the facility and its carriers and suppliers under the facility's own scheduling rules.

The problem it solves is coordination: without a governed schedule, freight arrives when it arrives, dock workload piles into unpredictable waves, warehouse labor is staffed for the wrong hours, and carriers wait. A dock scheduling platform replaces "first come, first serve" and phone-and-email coordination with a capacity model, a rule set, and a shared appointment book that all parties work from.

Its defining boundary: it governs the plan **before the truck arrives** — when each carrier should show up, and at which door. Once a truck is on the property, execution (gate check-in, trailer tracking, yard moves, door sequencing) belongs to neighboring systems, most directly the Yard Management System.

## Users & Context

Primary users are on the facility side:

- **dock schedulers / transportation planners** — own the schedule of record: review and confirm appointment requests, resolve exceptions, adjust capacity, manage the day's dock plan
- **warehouse / receiving and shipping leads** — consume the schedule to plan labor and equipment; may book appointments on behalf of carriers
- **operations managers** — configure doors, load types, and scheduling rules; monitor compliance and performance

Secondary but essential users are **external**: carriers, suppliers, and their dispatchers and drivers, who request, book, change, and confirm appointments — in mature products through self-service portals available around the clock.

Typical context: distribution centers (retail, grocery, 3PL), manufacturing plants, and parcel operations with meaningful inbound supplier deliveries and often outbound shipping. The scheduling horizon is days to weeks ahead; the characteristic work is processing appointment requests against capacity, not managing trucks on the property.

## Core Model

The system's world consists of four structures and the loop that connects them.

### Facility and dock doors — the capacity of record

The facility is the container; its **dock doors** are the schedulable resources. Each door carries operating hours, capacity, and constraints — what kinds of loads it can handle (equipment type, load type restrictions), and when it is available. The facility-level calendar aggregates door capacity into bookable time slots. This is the schedule of record: the fixed frame against which every appointment is made.

### Load types and freight context

Loads are described in freight terms: **load types** (what kind of freight and handling the appointment involves), the orders or purchase orders being received or shipped, and the **direction** — receiving (inbound/unloading) or shipping (outbound/loading). Freight context determines what the appointment means operationally: how long it should take, which doors qualify, and what the warehouse should expect.

### The appointment — the unit of record

An **appointment** is a persistent binding of a load (with its freight context and its carrier or supplier) to a door and a time window at a facility. It is the system's central object and the unit everything else hangs on. An appointment carries:

- the freight context — load type, orders/POs, carrier/supplier, direction
- the resource binding — facility, door (in some implementations an appointment may be held at facility level before a door is assigned), start and end time
- a lifecycle state — requested, scheduled/confirmed, rescheduled, cancelled, and day-of states such as arrived, in-dock, completed, or no-show (exact labels vary by product)
- a confirmation reference given to the carrier
- often attached documents (bills of lading, packing slips) and load detail down to SKU/PO level where integrated

### Scheduling rules — the governing frame

The facility's rules determine what may be booked when: capacity limits per door and time slot, load-type-to-door restrictions, appointment durations (fixed, average, or computed from load characteristics), booking lead times and cutoffs, and priorities among carriers or vendors. Rules are what turn a shared calendar into a scheduling discipline: a request that fits the rules can be confirmed automatically; one that does not is declined or queued for a scheduler's decision.

### The loop

```text
Carrier / supplier requests an appointment
  → evaluated against the facility's rules and available capacity
  → confirmed (automatically or by a scheduler) / declined / queued as an exception
  → appointment holds door + time + freight context
  → changes: reschedule, cancel, reassign — re-evaluated and re-communicated
  → day of: arrival and completion may be recorded against the appointment
  → the record becomes the compliance history: who booked, whether they honored it
```

## How It Works

### Configure the facility

Administrators define sites, dock doors, operating hours and calendars, load types, and the scheduling rules — capacity per slot, which loads go to which doors, durations, lead times. In mature products this configuration is explicit and rule-driven rather than held in a scheduler's head; vendors consistently position against rules that live "in a binder."

### Book and confirm appointments

Carriers and suppliers request appointments — through a self-service portal (the common modern form), or by phone/email with a scheduler entering the appointment manually (a fully supported mode). Each request is evaluated against the rules: fitting requests are confirmed — often automatically, with the automation level typically configurable per carrier tier — and non-fitting requests are declined with reasons or routed to an exception queue for human handling. Confirmations and notifications go out to all parties on every action.

### Live with the schedule

Schedulers work from a calendar view of doors and time slots: reviewing the day and week, dragging appointments to rebalance, handling early or late arrivals by adjusting slots or reassigning doors, and working the exception queue. Capacity views show where the day is overloaded so labor and equipment can be planned to the appointment book rather than to a guess.

### Close the loop

As appointments complete, the record accumulates into compliance history: on-time performance per carrier, dock utilization, dwell exposure. This feeds carrier scorecards and capacity planning — actual unload durations informing future slot sizing.

### What it does not do

The appointment record may carry day-of statuses (arrived, in-dock, completed), but the scheduling system does not manage what happens on the property: it does not track where trailers are parked, direct yard moves, or operate the gate. That execution layer belongs to the Yard Management System. The scheduling system's responsibility is the plan and its governance; the yard lives with the consequences.

## Interfaces

### Scheduler calendar

The facility side's primary surface: a calendar/grid of dock doors and time slots showing booked appointments with their freight context.

- typical information: door, time window, carrier/supplier, load type, direction, status, attached documents
- primary actions: confirm/decline requests, create or enter appointments on behalf of carriers, drag-and-drop rescheduling, reassign doors, work the exception queue

### Carrier / supplier self-service portal

The external party's surface: real-time availability at each facility, booking and editing of appointments, confirmation history, and account management.

- primary actions: request/book an appointment, reschedule, cancel, view confirmations, attach documents

### Exception queue

A prioritized worklist of requests and situations that rules could not resolve — non-fitting requests, conflicts, late or missing arrivals — awaiting a scheduler's decision.

### Configuration / administration

Door and facility setup, calendars and capacity, load types, scheduling rules, notification templates, user and carrier access management.

### Dashboards and reports

Dock utilization, appointment compliance and on-time performance, dwell exposure, throughput — the reporting layer over the appointment record.

## Important Rules / Behaviors

### Capacity is the constraint everything answers to

Appointments exist only where door-time capacity exists. Facility hours, holidays, and per-slot capacity limits are enforced on every booking; overriding them requires explicit permission in products that allow overrides at all.

### Rules decide, humans handle exceptions

The characteristic behavior: requests that fit the configured rules are confirmed without human touch; requests that do not are declined with reasons or queued. The degree of automation is a dial — some facilities auto-confirm top-tier carriers while keeping hands-on control over others; others confirm everything manually. The rule set, not the scheduler's memory, is the governing frame.

### The appointment is durable and auditable

Appointments persist through changes; reschedules and cancellations are tracked states, not overwrites. The accumulated record — who booked what, when, and whether they honored it — is the basis for carrier compliance and scorecarding.

### Confirmation is a commitment with consequences

A confirmed appointment is a reservation of physical capacity. Some products free unused reserved slots after a configurable expiration; no-shows and late arrivals are recorded states that feed compliance scoring.

### The gate is the handoff, not the end

The appointment's lifecycle may extend to arrival and completion statuses, but responsibility for the visit itself transfers at the gate — to gate/check-in processes and, where present, the yard management system. The scheduling system holds the plan and its history; it does not hold the trailer.

## Variants

- **Packaging** — the same core ships as a standalone dedicated product, as a module inside a Yard Management System, as a module or application inside a TMS, and inside broader warehouse/supply-chain suites. Frequently bundled with yard management; the bundle does not dissolve the boundary.
- **Direction scope** — inbound-only (the classic supplier-delivery/receiving program, often run as a vendor-compliance discipline) through inbound-plus-outbound scheduling at the same site.
- **Scheduling model** — strictly by-appointment-only versus open scheduling with first-come-first-serve windows alongside booked slots.
- **Automation posture** — fully self-service automated booking; clerk-mediated manual entry; tiered automation mixing both.
- **Industry tuning** — retail and grocery DCs (high-volume supplier deliveries), 3PL multi-client operations, manufacturing plants (inbound materials), parcel and post, temperature-controlled freight.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Yard Management System | adjacent, frequently bundled | YMS executes after arrival — gate-in to gate-out, trailer location of record, directed yard moves; dock scheduling plans before arrival — the appointment is the unit of work, and its job effectively ends at the gate |
| Warehouse Management System / WMS | downstream neighbor | WMS handles goods inside the building (receiving, putaway, picking); dock scheduling governs the arrival plan for the doors and hands freight context to the warehouse |
| Transportation Management System / TMS | upstream neighbor / common host | TMS plans and executes transportation between locations; dock scheduling governs the facility-side arrival/departure schedule — often shipped as a TMS module, but a distinct object world |
| Appointment Scheduling Application (generic) | same abstract shape, different world | generic appointment scheduling books people/services against resources; dock scheduling binds freight loads, carriers, and load types to dock doors under facility rules in a B2B multi-party loop |
| Delivery Scheduling Platform | adjacent | delivery scheduling is carrier/shipper-side scheduling of deliveries to recipients; dock scheduling is facility-side scheduling of arrivals at its own docks — a delivery appointment at a DC is where the two meet |
| Resource Calendar | generic substrate | a resource calendar allocates shared resources over time; dock scheduling is the freight-specific realization with load semantics, external partners, and facility rules |
| Port Terminal Operating System | cross-mode analog | berth windows and vessel calls at a marine terminal vs dock doors and truck appointments at a DC; they converge only at intermodal container yards |

## Representative Products

- **C3 Reservations (C3 Solutions)** — standalone dedicated dock scheduling; rule-based durations and capacity model; the vendor also sells a YMS sibling and draws the dock-vs-yard boundary itself
- **Shipwell Dock Scheduling** — dock scheduling as an API-accessible module of a TMS platform
- **YardView** — dock scheduling module of a dedicated YMS suite (stand-alone option also offered)
- **kaleris** — dock appointment scheduling inside an enterprise YMS
- **Turvo Appointment Scheduling** — appointment scheduling as a collaborative application within a TMS cloud, with shipment context synced to each slot

## Sources

Research date: **2026-09-10**

- C3 Solutions — Dock Scheduling Software product page, Product Tour, Dock scheduling FAQ, and "Dock Scheduling vs. Yard Management: What You Actually Need at Scale" (blog): https://www.c3solutions.com/dock-scheduling/ , https://www.c3solutions.com/dock-scheduling/tour/ , https://www.c3solutions.com/dock-scheduling/faq/ , https://www.c3solutions.com/blog-c3/dock-scheduling-vs-yard-management/
- Shipwell — "What is dock scheduling?" and Dock Scheduling API documentation (developer portal): https://docs.shipwell.com/docs/dock-scheduling/what-is-dock-scheduling/ , https://docs.shipwell.com/openapi_pages/dock-scheduling/overview/
- YardView — Dock scheduling page, YMS features, FAQ: https://www.yardview.com/dock-appointments , https://www.yardview.com/features , https://www.yardview.com/faq
- kaleris — Yard Management Solutions, "Why a Purpose-Built YMS Outperforms WMS Yard Modules", MODEX 2024 announcement, Retail page: https://kaleris.com/solutions/yard-management/ , https://kaleris.com/why-a-purpose-built-yms-outperforms-wms/ , https://kaleris.com/news/kaleris-launches-yard-management-innovations-at-modex-2024/ , https://kaleris.com/who-we-serve/retail/
- Turvo — Appointment Scheduling product page and launch announcement: https://turvo.com/scheduling/ , https://www.prnewswire.com/news-releases/turvo-announces-new-appointment-scheduling-application-to-drive-yard-efficiency-and-contribute-to-supply-chain-sustainability-301263106.html

> Sourcing limitation: UI help-center documentation was reachable only for Shipwell (developer/API docs). Observations for the other products come from vendor product, tour, and FAQ pages. Precise operational parameters (default lead times, numeric capacity limits, exact status vocabularies, permission details) are intentionally not stated; the appointment lifecycle is described conceptually, and exact state labels vary by product.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis against Yard Management, WMS, and TMS are recorded in the paired Research Notes.
