# Patient Flow Management

## Overview

A **Patient Flow Management** application is hospital operations software that manages the journey of each patient through the facility's acute episode — from arrival or admission, through unit stays and transfers, to discharge — as a live, coordinated process. Its defining core is small: every patient's progression is tracked in real time (where they are in the journey and where they are heading, with timing), progression that has stalled or is at risk is surfaced with its causes, and the teams responsible act from one shared house-wide picture.

The problem it exists to solve is compounding delay: patients boarding in the emergency department waiting for a bed, discharges happening late in the day, transfers waiting on phone calls, and handoffs between departments falling through the cracks. Each of these is a failure of coordination between teams that use different systems; a patient flow application makes the whole house's movement visible to everyone responsible for it and drives the actions that keep patients moving forward.

The type is deliberately person-centric. It is distinct from bed management software, which manages the physical bed as a resource (state, cleaning, placement, capacity) — although the market frequently bundles both layers into one suite and frequently names products across the seam. A patient flow application can exist with no bed machinery at all; what it cannot exist without is the tracked journey, the surfaced delays, and the shared picture.

## Users & Context

The work environment is a hospital's inpatient operation viewed as a whole: the emergency department, admission and intake, nursing units, care management and case management, ancillary services (therapy, imaging, laboratory), patient transport, environmental services, and increasingly a centralized operations, capacity, or command-center function.

Primary users:

- **patient flow / throughput coordinators and capacity managers** — own the house-wide movement picture; arbitrate when demand outstrips capacity; drive escalation when flow stalls
- **case managers and discharge planners** — own each patient's discharge readiness: expected discharge date, barriers (clinical, social, logistical), and the follow-up actions to remove them
- **charge nurses and unit teams** — see incoming admissions, patients awaiting transfer, and their unit's discharges; unblock tasks delaying their patients
- **admitting, transfer center, and intake staff** — process incoming demand from the ED, recovery, and other facilities, and pace admissions against discharges

Secondary users:

- **operations and nursing leadership** — watch length of stay, boarding, and discharge performance across the facility; run the daily coordination meetings; activate escalation protocols
- **ancillary and support teams** — receive sequenced or dispatched work (therapy, imaging, transport, cleaning) whose timing affects how soon patients can move or leave

The application is typically open continuously on shared displays and personal workstations; several products instead deliver their surfaces embedded inside the EHR itself. It consumes admission, discharge, and transfer events from the hospital's EHR or patient administration system rather than replacing clinical documentation.

## Core Model

### The Defining Core

```text
Live Tracked Patient Journey
└── Delay & Risk Surfacing   (stalled progression, barriers, boarding)
    └── Progression Coordination (actions across the teams involved)
        └── Shared House-Wide Picture (one view the coordinating roles act from)
```

Three structures. If any one is removed, the product stops being patient flow management:

- **Live tracked patient journey** — each patient in the acute episode is held in the system as a progression subject: current location and stage, where they are heading (anticipated moves and discharge), and the timing of both. The journey is the unit of record — not the appointment, not the bed, not the clinical note. Without it there is no flow subject to manage.
- **Delay and risk surfacing with progression coordination** — the system identifies the patients whose movement is stalled or endangered: barriers blocking discharge, patients boarding past reasonable waits, expected discharges that will not happen, transfers waiting on action. Surfacing alone is a report; the defining act is coordinating the corrective actions across the teams and units involved — assigning, prompting, escalating, and tracking that the unblocking actually happens. Without this, the product collapses into a passive tracking board or census report.
- **Shared house-wide operational picture** — one live view of all journeys that intake, units, flow coordination, and leadership jointly act from, whether delivered as a standalone board or embedded in the EHR's screens. The coordination failure this type exists to fix is precisely each department holding its own separate version of the truth; without the shared picture, that failure returns.

### Standard Capabilities

Mature products commonly add the following layers to that core:

- **Discharge coordination machinery** — expected or estimated discharge dates held per patient and revised as the stay progresses, likely-discharge identification ("who can go home today"), per-patient barrier lists spanning clinical, social, and logistical causes, and prioritized discharge worklists. Discharge is the pivotal event of the type: nearly every product's coordination effort concentrates on making it happen earlier and more predictably.
- **Admission and intake coordination** — a shared view of incoming demand (emergency department admissions, post-operative recoveries, inter-facility transfers), prioritization among waiting patients, and the pacing of admissions against discharges so that a bed vacated is met by a patient already waiting.
- **Coordination rituals in software** — the daily bed huddle and multidisciplinary rounds as supported workflows: prepared agendas from live data, captured decisions, assigned actions, and tracked follow-through, plus escalation paths for at-risk situations.
- **Throughput metrics and dashboards** — length of stay, excess days, boarding time, discharge counts by time of day, and related capacity measures, per unit and house-wide.
- **EHR / PAS integration** — admission, discharge, and transfer events flowing in as the data substrate; plan data (expected discharge dates, dispositions) flowing back.
- **Task layer** — flow-relevant tasks attached to the patient's journey (consults, paperwork, transport,equipment returns), triaged, prompted, and tracked to completion.
- **Handoff automation** — automatic triggering of the downstream actions a departure sets off: transport requests, cleaning notifications, order sequencing, notifications to receiving teams.

### One Structure, Many Implementations

The core is written conceptually. Implementations differ substantially:

```text
Concept:      The tracked journey
Realizations: standalone flow boards and patient lists;
              surfaces embedded inside the EHR;
              analytics views assembled from EHR data feeds

Concept:      Delay surfacing
Realizations: staff-identified barriers and task lists;
              rules and prompts on task completion;
              machine-learning prediction of discharge dates
              and care-plan gaps

Concept:      Coordination
Realizations: structured daily huddles and rounds with tracked actions;
              task triage and dispatch;
              automated triggers and escalations
```

A reader who encounters only one implementation should still recognize the others from the core above.

## How It Works

The application runs as three interlocking loops. Understanding them together is understanding the type.

### Loop 1 — The progression loop (patient by patient)

```text
Patient admitted (or awaiting a bed from ED / recovery / transfer)
→ journey record opens with location, stage, and care context
→ expected discharge date and disposition established early in the stay
→ progression monitored as care events land (consults, therapy, results)
→ barriers surface as they arise
→ actions assigned and completed to clear the barriers
→ patient moves (transfer, lower-acuity setting) or discharges
→ journey record closes; capacity is released for the next patient
```

The distinctive behavior of this loop is that discharge planning starts at admission, not on the day of discharge. In more automation-heavy products the expected discharge date is populated early in the stay and continuously pressure-tested against what is actually happening to the patient; in less automated products the care team sets and revises it. Either way the journey is managed prospectively — the system's question is not "what happened" but "what will stop this patient from moving on, and when."

### Loop 2 — The delay-removal loop (barriers and unblocking)

```text
Signal of stalled progression (barrier, overdue discharge, boarding wait)
→ surfaced on the shared picture with the patient and cause attached
→ routed to the team that can act (unit, case management, ancillary service)
→ action taken and recorded
→ progression resumes; if it does not, escalation paths engage
```

Barriers are heterogeneous by nature — a pending therapy assessment, a missing piece of discharge equipment, a post-acute placement decision, an order that was never sequenced. Mature products differ enormously in how much of this they detect automatically versus collect from staff, but they share the shape: the delay becomes a visible, owned, tracked object instead of a private frustration.

### Loop 3 — The daily coordination rhythm (the house as a system)

```text
Live data prepares the day's picture before the daily huddle
→ the meeting works the list: constraints, escalations, priorities
→ decisions and actions captured in the system
→ follow-through tracked against the day's goals
→ dashboards compare execution with targets (discharges by noon, boarding, LOS)
→ the picture carries into the next day's huddle
```

This loop runs on the hospital's daily operational rhythm and continuously in the background through dashboards and alerts. It is where individual patient coordination turns into capacity management: leadership acts on the aggregate (prioritize certain discharges, open alternate admission destinations, deploy staff) based on the same picture the frontline acts on.

### The combined picture

Intake demand feeds Loop 1; Loop 1's stalled patients feed Loop 2; both feed Loop 3, whose decisions push discharges earlier and reshape the day. The application's value is keeping all three loops turning on one shared, real-time picture of every patient's journey.

## Interfaces

Described in conceptual terms; exact layouts and names vary by product, and some products deliver these surfaces inside the EHR rather than as standalone screens.

### House-wide flow board / patient list

The central surface: the facility's inpatients as a live list or board.

- typical information: patient, current location and stage, length of stay, expected discharge date, destination or disposition, flags for risk or delay
- primary actions: open a patient's journey, update stage or location, flag a barrier, prioritize, drill into the unit view

### Discharge planning / barrier worklist

The workbench of the type's pivotal event.

- typical information: expected discharges for the day, per-patient barriers and their owners, likely-discharge candidates, completed and outstanding actions
- primary actions: set or revise the expected discharge, record and assign barrier removal, mark discharge readiness, escalate an at-risk plan

### Intake / demand view

The demand side of the same picture.

- typical information: patients awaiting beds by origin (ED, recovery, transfer), wait time, prioritization, incoming transfer requests
- primary actions: prioritize, coordinate placement options, accept transfers, pace admissions against pending discharges

### Huddle / rounds support

The coordination-meeting surface.

- typical information: prepared agenda of constraints and escalations, the patient-level evidence behind each item, prior decisions and their follow-through status
- primary actions: capture decisions, assign actions, track completion

### Throughput dashboard

The leadership surface.

- typical information: census and occupancy trends, length of stay and excess days, boarding measures, discharge performance against goals, bottleneck indicators
- primary actions: drill down to the patients behind a number, activate escalation, adjust priorities

### Task views and mobile surfaces

- typical information: assigned flow tasks by patient, priority, and due state
- primary actions: claim, complete, hand off — often delivered on mobile devices for roving staff

## Important Rules / Behaviors

### Progression is event-driven, not appointment-driven

Nothing in the flow picture is pre-booked into fixed future slots. A patient's position advances as care events actually happen; the expected discharge date is a live plan, not a reservation. This is the structural difference from scheduling software, and it is why the flow picture must be continuously reconciled with reality rather than consulted occasionally.

### The expected discharge date is a revisable plan under pressure

Mature products treat the expected discharge date as the journey's load-bearing attribute — set early, revised as evidence accumulates, and checked against actual progression. A plan that silently goes stale is treated as a failure state: the system's job is to notice the gap between planned and actual before the patient's last day.

### A stalled patient is visible as a patient, not just a slow average

Delay is surfaced at the level of the individual journey — this patient, this barrier, this owner — before it is aggregated into metrics. The metrics exist to direct attention back to patients; products that only aggregate lose the coordination function.

### Boarding is a shared problem by design

Emergency-department boarding sits at the seam between departments, and the type treats it as a house-level concern: the waiting patient is displayed on the shared picture where the units, intake, and flow coordination can act on it, rather than remaining an ED-local wait.

### The system coordinates; people decide

Escalation pathways, prioritization suggestions, and automated triggers route work to the accountable humans; placement decisions, discharge decisions, and clinical judgments remain with staff. The most automation-heavy products automate administrative actions below the clinical decision line, and keep interventions on at-risk plans in human hands.

### The EHR remains the record; flow is the action layer

Admission, discharge, and transfer events originate in the hospital's EHR or patient administration system, and clinical documentation stays there. The flow application consumes those events, adds the progression and coordination layer, and writes plan data back. It supplements the record system; it does not replace it.

## Variants

Common forms of the same type:

- **insight-first coordination** — analytics over EHR data feeding a daily plan: predicted discharges, barrier surfacing, huddle support, and tracked follow-through, with little or no task-execution machinery
- **AI-automation pole** — machine-learning models embedded in the EHR that populate expected discharge dates, predict care-plan gaps, sequence ancillary orders, and automate administrative actions; the depth pole of the type
- **operational task platform** — the journey coordinated primarily through attached tasks: triage, prompts, and automations replacing paper lists, phone calls, and whiteboards (common in UK NHS deployments)
- **integrated operations suite** — the flow layer bundled inside a platform that also carries the bed-state, placement, environmental-services, and transport machinery of bed & capacity management; the most common enterprise packaging and the source of the market's naming confusion
- **command-center / transfer-center delivery** — the same software operated from a centralized coordination function, often across multiple facilities, with inter-facility transfer management folded into the intake picture
- **sensor-automated deployments** — real-time location systems detect departures and trigger downstream flow actions automatically
- **regional vocabulary variants** — the same software is marketed as "patient flow", "throughput", "inpatient flow", or "patient journey" depending on market; the underlying structure is the same

A variant should remain a variant unless it changes users, core objects, workflow, or rules so much that the defining core no longer applies — as when the tracked subject becomes the physical bed rather than the patient, which is the sibling type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Bed & Capacity Management | closest adjacent; market naming is porous across the seam | patient flow is person-centric — the journey, its timing, and its coordination; bed & capacity management is resource-centric — per-bed state, cleaning/readiness cycle, placement decisions, and capacity planning. Products frequently bundle both layers, and some products marketed under flow-like names are bed-centric at the core; the test is the managed object |
| Hospital Management System / EHR | upstream foundation | the EHR documents care and produces the admission/discharge/transfer events; patient flow consumes them and adds the operational progression layer. In an HMS the flow board is one surface among many; here it is the centered object |
| Emergency Department Information System | adjacent upstream | EDIS is the ED's own visit-scoped clinical and operational system of record; its tracking ends at the admission decision and bed handoff. From there the patient becomes flow's subject, and ED boarding reappears in flow as an intake queue and a house-level metric |
| Patient Scheduling | adjacent | scheduling books patients into future time slots in advance; flow manages live, event-driven progression with no appointment book |
| Operating Room Management | adjacent, same pattern over a different resource | the same live-coordination structure applied to operating rooms as scheduled capacity; the two meet at post-operative destination planning, where the surgical case's outcome becomes a patient journey in flow |
| Care Coordination Platform | adjacent | care coordination spans care settings and the longitudinal care plan (clinical and social); patient flow is the operational progression of the acute episode inside the facility |
| Clinical Communication Platform | adjacent, complementary | communication platforms route messages and forward events from flow systems; flow systems coordinate progression. Message exchange is their center, not flow's |

## Representative Products

- **TeleTracking** (Operations IQ platform, Throughput module) — integrated enterprise platform coordinating the acute journey end to end, with the full bed-operations machinery bundled alongside journey coordination
- **LeanTaaS iQueue for Inpatient Flow** — insight-first coordination: the daily capacity plan, care-progression signals, huddle and rounds support, staffing alignment
- **Qventus (Inpatient Capacity)** — AI-automation pole: EHR-embedded discharge planning, barrier prediction, and action automation with no bed machinery
- **Liaison Assist (Infinity Health)** — UK NHS operational pole: task-based journey coordination and discharge forward-views replacing paper and whiteboard processes

The defining core was checked against the market's naming seam (products named "patient flow" that are bed-centric at the core, and vice versa) and against non-AI and paper-lineage practice, to avoid defining the type by its most automated current implementations.

## Sources

Research date: **2026-09-08**

Official vendor surfaces (product/solution pages):

- TeleTracking — https://www.teletracking.com/ ; https://www.teletracking.com/healthcare-operations-iq-platform/throughput/
- LeanTaaS — https://leantaas.com/products/inpatient-flow/
- Qventus — https://qventus.com/ ; https://qventus.com/solutions/discharge-planning/
- Liaison Assist (Infinity Health) — https://infinityhealth.io/ ; https://infinityhealth.io/patient-flow/

> Sourcing limitation: the vendors researched do not publish public operational documentation (help centers, user guides) for their flow modules; customer documentation portals are login-gated. All statements in this document are calibrated to official product/solution pages, and precise operational parameters (state vocabularies, thresholds, timers, defaults, numeric limits) are intentionally not stated. Vendor-published outcome figures are marketing claims and were not relied on. Detailed product-by-product evidence, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
