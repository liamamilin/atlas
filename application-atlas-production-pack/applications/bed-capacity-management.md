# Bed & Capacity Management

## Overview

A **Bed & Capacity Management** application is hospital operations software that maintains a live picture of a facility's inpatient beds — which are occupied, which have just been vacated, which are being cleaned, and which are ready — and coordinates the placement of patients into those beds across departments, together with the planning view that compares incoming patient demand against available capacity.

Its purpose is operational, not clinical: patients are admitted, discharged, and transferred continuously throughout the day, and every one of those events changes the usability of a physical bed. A bed is not usable the moment a patient leaves it; it must be cleaned, checked, and released back into the pool before the next patient can occupy it. This application makes that cycle visible and actionable, so that the moment a bed becomes ready, someone is waiting to fill it — and so that when demand rises, the hospital sees the constraint coming instead of discovering it at the emergency department door.

The defining core is deliberately small: a managed registry of beds, a live state on each bed, placement decisions binding patients to beds, and a shared real-time view that multiple departments work from. Everything else widely associated with the category — housekeeping task dispatch, transport, discharge prediction, forecasting, escalation protocols, staffing linkage — is mature capability layered on that core, not what makes the product this type.

## Users & Context

The work environment is a hospital's inpatient operation — normally spanning every nursing unit, the emergency department, post-anesthesia recovery, admitting, environmental services (housekeeping), patient transport, and increasingly a centralized operations or command function.

Primary users:

- **bed manager / patient flow coordinator / capacity manager** — owns the facility-wide bed picture; makes or arbitrates placement decisions when demand exceeds comfortable supply
- **admitting and transfer center staff** — process incoming demand (ED admissions, recoveries, direct and inter-facility transfers) and reserve or assign beds
- **charge nurses and unit staff** — see and affect the state of beds on their own unit; receive incoming patients
- **environmental services (EVS) teams** — receive and perform cleaning/turnaround tasks that return beds to a usable state
- **patient transport teams** — move patients to and from beds, feeding status changes into the same picture

Secondary users:

- **operations and nursing leadership** — watch occupancy, boarding, length of stay, and turnaround across the facility; run capacity huddles; activate escalation protocols
- **staffing offices** — consume census and workload forecasts to align staffing with predicted demand

The application is typically open continuously on large shared displays and personal workstations, with companion mobile surfaces for EVS and transport staff who are not at desks. It consumes admission/discharge/transfer events from the hospital's EHR or health information system rather than replacing them.

## Core Model

### The Defining Core

```text
Managed Bed Inventory
└── Per-Bed Operational State  (occupied ↔ usable, advanced by care events)
    └── Placement Decisions    (patient bound to a specific bed)
        └── Shared Real-Time Operational View  (one picture for many departments)
```

Four elements. Each is required for the product to function as bed and capacity management:

- **Managed bed inventory** — the facility's inpatient beds exist in the system as individually identified physical resources, organized into rooms and units. The bed, not the appointment and not the patient record, is the managed asset. Without the inventory there is nothing for this type to manage.
- **Per-bed operational state** — each bed carries a live state that distinguishes occupied from available-for-use, and that changes as care events happen: a patient is admitted into it, leaves it at discharge, it is cleaned and readied, it may be held or blocked. State is driven by events in the care process, not by pre-booked time. Without live state the concept collapses into ordinary scheduling.
- **Placement decisions** — the system records which patient is in, or will occupy, which bed: assignment at admission, movement at transfer, release at discharge. Placement is a decision made against demand and bed suitability, and it is the act that turns bed state into patient flow. All researched products expose this under one name or another (bed assignment, bed selection, placement prioritization).
- **Shared real-time operational view** — one live picture of beds, states, and incoming demand that admissions, the ED, bed management, nursing units, EVS, and transport all work from. The shared view is what distinguishes a management application from an internal EHR field: the bed state exists to be seen and acted on collectively, in real time.

### Standard Capabilities

Mature products commonly add the following layers to that core:

- **Housekeeping/EVS turnaround** — a discharge generates a cleaning task; the bed does not rejoin the available pool until cleaning completes and readiness is confirmed. This occupied→vacated→cleaning→ready cycle is the rhythm the whole application runs on.
- **Patient transport coordination** — requests to move patients between departments or to and from beds, often zoned and dispatched to mobile staff.
- **Discharge machinery** — expected/estimated discharge dates tracked per patient, likely-discharge identification, surfacing of clinical, social, and logistical discharge barriers, and prioritized discharge lists to free beds where they are needed.
- **Intake and boarding visibility** — queues of patients waiting for beds (ED boarders, recovery holds, waiting transfers) shown against the bed picture.
- **Reservations and holds** — beds held for patients who have not yet physically arrived, including pre-arrival reservations for inter-facility transfers.
- **Capacity dashboards and metrics** — occupancy, length of stay, boarding time, discharge counts, and bed turnaround time, per unit and facility-wide.
- **Demand forecasting and prediction** — projections of census and demand, predicted discharges, and early warning of capacity constraints.
- **Escalation machinery** — structured capacity huddles, capacity protocols that can be activated early, and bottleneck alerts.
- **Staffing-demand linkage** — census and workload forecasts used to identify staffing gaps or excess and guide staff allocation.
- **EHR integration** — admission, discharge, and transfer events from the hospital information system as the primary data substrate; placement actions commonly flow back into the EHR.

### One Structure, Many Implementations

The core is written conceptually. Implementations differ substantially:

```text
Concept:      Bed inventory & state
Realizations: dedicated standalone platform integrated with the EHR;
              modules inside the EHR vendor's suite;
              analytics overlays consuming EHR data feeds

Concept:      State transitions
Realizations: manual staff updates; semi-automated task flows;
              sensor-based (RTLS) detection of patient departure
              triggering downstream tasks automatically

Concept:      Shared view
Realizations: electronic bed boards; unit whiteboards; command-center
              dashboards; room-side displays at the physical bed
```

## How It Works

The application runs as three interlocking loops. Understanding them together is understanding the type.

### Loop 1 — Bed turnaround (the state loop)

```text
Patient discharge executed
→ bed becomes vacated (and not yet usable)
→ cleaning task issued to environmental services
→ cleaning performed and confirmed
→ bed becomes ready and rejoins the available pool
```

The point of this loop is elapsed time: every minute between a patient leaving and a bed being ready is a minute the bed cannot serve the next patient. Mature products compress it — automatically issuing the cleaning request at discharge, timing the turnaround, and in some implementations detecting the patient's physical departure with location sensors so the downstream tasks start on their own.

### Loop 2 — Placement (the demand loop)

```text
Demand arrives (ED admission, recovery, transfer, inter-facility referral)
→ placement decision: match patient requirements against available beds
→ bed reserved or assigned
→ transport requested / patient moves
→ bed becomes occupied; queue shrinks
```

The placement decision weighs where the patient should go (unit and level of care, isolation precautions, and other care requirements, depending on the product) against what is actually free or about to become free. Products keep admissions pacing with discharges: the aim is that a bed becoming available is met by a patient already waiting for it, not discovered idle.

### Loop 3 — Capacity management (the planning loop)

```text
Forecast census and demand
→ compare against available capacity; surface constraints early
→ capacity huddle: decide actions (prioritize discharges, open surge beds,
   adjust staffing, activate escalation protocols)
→ track that decisions are executed
→ re-forecast
```

This loop runs on a daily rhythm (daily bed huddles are a common institution) and continuously in the background via dashboards and alerts. It is where "capacity" in the type's name is earned: prediction and escalation, not just board-keeping.

### The combined picture

Discharges feed Loop 1, which feeds Loop 2's supply; demand feeds Loop 2; both feed Loop 3, whose decisions push discharges earlier and adjust supply and staffing. The application's core value is keeping all three loops turning on one shared, real-time picture.

## Interfaces

Described in conceptual terms; exact layouts and names vary by product.

### Bed board / census board

The central surface: the facility or unit as a grid or list of beds.

- typical information: bed identity, room, unit, per-bed state (occupied / being cleaned / ready / held / blocked), current patient, expected discharge where known
- primary actions: assign a patient to a bed, change bed state, place a hold or reservation, transfer, drill into a patient's stay

### Intake / boarding view

The demand side of the same picture.

- typical information: patients awaiting beds by origin (ED, recovery, transfer), wait time, boarding status, pre-arrival reservations
- primary actions: prioritize, assign a bed, accept a transfer, flag constraints

### Housekeeping / EVS view

The turnaround worklist for cleaning teams.

- typical information: pending cleaning tasks by room, discharge events just occurred, task status, turnaround timers
- primary actions: claim/complete tasks, confirm room readiness; often delivered on mobile devices

### Transport view

- typical information: pending transport requests, origin and destination, priority, assignment
- primary actions: dispatch, assign, complete; mobile-oriented

### Capacity dashboard / command center view

The leadership and coordination surface.

- typical information: census and occupancy trends, forecast demand, boarding and length-of-stay metrics, bottleneck alerts, predicted discharges
- primary actions: run and record huddle decisions, activate escalation protocols, prioritize discharges, adjust staffing plans

### Unit whiteboards / room-side displays

Peripheral surfaces that push the state back to the point of care: auto-populated status of each room or bed — in some products including discharge status among the shared indicators — visible to staff walking the unit.

### Mobile surfaces

Companion apps for EVS, transport, and roving coordinators: receive tasks, update state from the corridor rather than the desk.

## Important Rules / Behaviors

### State advances with events, not time slots

Unlike scheduling software, nothing here is pre-booked into the future in fixed slots. A bed's usability is determined by what has physically happened to it — occupied, vacated, cleaned, ready — and the application's job is to keep that state truthful in real time.

### A vacated bed is not an available bed

The readiness cycle is the load-bearing rule of the type: discharge does not make a bed usable; cleaning and confirmation do. Systems that skip this distinction are census reports, not bed management.

### Reservation is not occupancy

Beds can be held or reserved for patients who have not yet arrived (including pre-arrival holds for transfers). The shared view must distinguish held beds from genuinely free ones, or the picture breaks trust with its users.

### Placement is constrained

Placement decisions are not free choice: care requirements, unit functions, isolation status, and house rules constrain which patient may go in which bed. Mature products encode these constraints to varying degrees; public documentation of the rule engines is limited, so their exact mechanics vary by product.

### One shared picture, many actors

The view is deliberately shared across departments that report to different leaders. Coordination failures (each department holding its own version of the truth) are precisely the problem the type exists to solve; products therefore treat the shared board as a single real-time source of truth for every department acting on beds.

### Data flows in from the EHR

Admission, discharge, and transfer events originate in the hospital information system; the bed application reacts to them and feeds placement actions back. It supplements the EHR's operational layer rather than replacing clinical documentation.

## Variants

Common forms of the same type:

- **standalone operational platform** — a dedicated vendor product integrated with the hospital's EHR, strongest at the operational loops: placement consoles, EVS and transport dispatch, mobile task execution, enterprise visibility
- **EHR-embedded module family** — the EHR vendor's own suite modules (patient flow, command center, transfer center, digital whiteboards), benefiting from native data and distribution
- **analytics / decision-support overlay** — a cloud layer over EHR data focused on the planning loop: demand prediction, discharge prediction, huddle support, staffing forecasts, prescriptive recommendations
- **sensor-automated deployments** — real-time location systems detect patient movement and trigger status transitions and downstream tasks automatically, reducing manual updates
- **command-center delivery model** — the software operated from a centralized coordination center that manages capacity for a whole facility or multi-hospital network
- **single facility vs network scope** — from one hospital's bed pool to multi-facility visibility of beds, referrals, and patient demand across a health system
- **regional vocabulary variants** — the same software is marketed as "bed management" or "electronic bed management" (common in the UK), "throughput" or "capacity management" (common in the US); the underlying structure is the same

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Patient Flow Management | closest adjacent; boundaries are porous in the market | patient flow is person-centric — the patient's journey through care stages and its timing; bed & capacity management is resource-centric — the bed's state, readiness, placement, and capacity. Vendors frequently bundle both, and some market one product under both names; the bed-state/placement core is the distinguishing slice |
| Hospital Management System / EHR | upstream foundation | the EHR documents clinical care and produces the admission/discharge/transfer events; bed & capacity management consumes those events and adds the operational bed-state and placement layer. EHR suites increasingly bundle this layer as modules |
| Patient Scheduling | adjacent | scheduling books patients into future time slots in advance; bed placement binds patients to physical beds in the present, driven by live care events |
| Emergency Department Information System | adjacent | manages ED-side care and tracking; ED boarding appears in bed & capacity management as an intake queue and a metric |
| Space Management (IWMS / facilities) | adjacent, different rhythm | facilities software plans and manages the physical space portfolio over long cycles; bed & capacity management operates the live, care-event-driven state of beds inside that space |
| Capacity Management (IT domain) | same term, different domain | in IT, capacity management plans compute and infrastructure resources; shares nothing with the healthcare type beyond the name |

## Representative Products

- **TeleTracking** (Operations IQ platform; in the UK marketed explicitly as Electronic Bed and Capacity Management) — dedicated operational platform: placement, EVS management, transport, discharge automation, enterprise visibility
- **LeanTaaS iQueue for Inpatient Flow** — analytics-first capacity management: demand and discharge prediction, huddle support, escalation protocols, staffing forecasts
- **Oracle Health Clinical Operations (Patient Flow, Command Center Dashboard, Transfer Center, Clinical Operations Whiteboard)** — EHR-suite-embedded modules for bed utilization, placement, EVS/transport automation, and capacity forecasting

Real-time location system vendors (for example CenTrak) appear in this space as the sensing layer that automates status transitions and feeds bed systems; they are enablers rather than bed & capacity management products themselves.

## Sources

Research date: **2026-09-06**

Official vendor surfaces (solution/product pages):

- TeleTracking — https://www.teletracking.com/ ; https://www.teletracking.com/healthcare-operations-iq-platform/throughput/ ; https://teletracking.uk/
- LeanTaaS — https://leantaas.com/ ; https://leantaas.com/products/inpatient-flow/
- Oracle Health — https://www.oracle.com/health/clinical-operations/
- CenTrak (boundary reference only) — https://www.centrak.com/

> Sourcing limitation: the sampled vendors do not publish public operational documentation (help centers, user guides) for their bed and capacity modules; customer documentation portals are login-gated. All statements in this document are therefore calibrated to official product/solution pages, and precise operational parameters (state vocabularies, numeric thresholds, timers, defaults) are intentionally not stated. Detailed product-by-product evidence and comparison are recorded in the paired Research Notes.
