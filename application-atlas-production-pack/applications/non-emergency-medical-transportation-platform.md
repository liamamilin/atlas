# Non-emergency Medical Transportation Platform

## Overview

A **Non-emergency Medical Transportation (NEMT) Platform** is the system of record for scheduled, non-emergency transportation to and from healthcare services. It holds the passenger of record together with their transportation needs, manages **trips** as the unit of work, orchestrates a credentialed fulfillment network of vehicles, drivers, and transportation providers, and resolves completed trips into payment against the program or contract that funds them.

The defining core is small:

```text
Passenger of record (with recorded transportation needs)
└── Trip (scheduled, non-emergency journey — commonly home ↔ healthcare appointment)
    └── assigned to a managed fulfillment network (providers / vehicles / drivers)
        └── performed, verified, and resolved into payment
```

Everything else commonly associated with the category — Medicaid-style benefit administration, broker subcontractor networks, member mobile apps, GPS tracking, automated route optimization, mileage reimbursement — is widespread in current products but is a realization of one of these four structures, not the structure itself. A paper-era program office running phone intake, paper trip tickets, a roster of contracted cab companies, and invoices to the program satisfies the same core; so does a private-pay medical transport company or a transit agency running healthcare trips on demand-response machinery.

The "non-emergency" boundary matters: the Type has no emergency-response role and produces no clinical care documentation. When the dominant surface shifts to emergency response with clinical records, the product belongs to EMS operations territory; when transportation is open to the general public on demand, it belongs to ride-hailing or taxi dispatch.

## Users & Context

The platform sits between a funding program, a passenger population, and a fulfillment network. Typical roles:

**Program side (broker posture)**
- Program administrators run the transportation benefit on behalf of a payer — a government health program, a managed care organization, or another funding program. They own eligibility, program rules, provider networks, and program reporting.
- Call-center/intake agents take trip requests by phone, verify passengers, and enter trips — in many programs the phone remains the primary intake channel, with self-service portals alongside it.

**Fulfillment side (provider posture)**
- Transportation providers (fleet operators) receive trips, schedule them onto vehicles and drivers, and dispatch the day's work.
- Dispatchers manage the day of service: routes, manifests, real-time changes.
- Drivers execute trips from a mobile device: manifest, navigation, status updates, completion confirmation.

**Passengers and their caregivers**
- Members/patients request, review, track, and cancel their own rides in mature products; caregivers and family members often act on their behalf.

**Healthcare facilities**
- Hospital and clinic staff book trips for patients — recurring treatment schedules (dialysis, chemotherapy, physical therapy, behavioral health) and discharges are typical origins of facility-initiated requests.

**Payers and funders**
- Program staff consume performance data, trip records, and billing; in the broker posture the platform is also the payer's window into the benefit.

The work environment is operationally time-pressured: trips are bound to appointment times, the day's plan is built the night before or the morning of, and the operating loop is dominated by schedule building, dispatch, and exception handling.

## Core Model

### The defining core

**1. The passenger of record with transportation needs.**
A persistent, identified passenger — a program member, a patient, a private-pay client — carries the attributes that shape every trip: identity and contact details, eligibility context in the funding program where one exists, and above all their **transportation needs**: mobility level, assistance required, whether an attendant or caregiver rides along, and what kind of vehicle the trip requires. This record is what makes the passenger addressable across trips and what distinguishes the Type from anonymous ride booking. In program contexts the passenger's needs are commonly captured through a structured needs assessment completed with input from the passenger's healthcare provider.

**2. The trip as the unit of work.**
A trip is a scheduled, non-emergency journey for a specific passenger between a pickup location and a drop-off location at defined times — most commonly home to a healthcare appointment and back, but also facility-to-facility transfers, pharmacy trips, or health-related community destinations depending on the program. A trip binds together:

- the passenger (and any accompanying attendant)
- pickup and drop-off addresses and times, commonly with a pickup window built backward from the appointment time
- the required **mode** — the vehicle/service type implied by the passenger's needs (ambulatory sedan, wheelchair-accessible vehicle, stretcher-capable transport, and in some programs non-emergency ambulance)
- the fulfillment assignment (provider, vehicle, driver)
- frequently a **return leg**, either booked in advance or requested on demand when the passenger is ready to leave

Trips advance through a lifecycle: requested → authorized/eligible → scheduled → assigned → dispatched → performed → completed (or cancelled / no-show). Exact state names vary by product; the progression is the stable part.

**3. The managed fulfillment network.**
The capacity that performs trips is held inside the system as schedulable, credentialed resources. Two postures dominate, and both are the same Type:

- **Provider posture** — the operator owns or leases vehicles, employs or contracts drivers, and schedules its own fleet. Trips arrive from brokers, facilities, or direct customers.
- **Broker posture** — the operator administers a program and subcontracts fulfillment to a network of transportation providers, independent drivers, and sometimes volunteer drivers. The broker's platform assigns trips to subcontractors, manages their credentials, and settles what they are owed.

In both postures the network is governed by credentialing: driver qualifications, training, background checks, vehicle standards, insurance, and program-specific requirements are recorded, monitored for expiry, and gate whether a resource may take trips.

**4. The completion-to-payment loop.**
A trip is not finished when the passenger is dropped off. Completion is **verified and recorded** — timestamps, GPS traces, driver confirmations, and in mature products electronic trip verification — because the record is what payment rests on. Completed trips then resolve into money along the path the funding takes:

- claims submitted to a payer (electronic claim files with the codes each payer requires)
- billing files formatted to each broker's specifications (providers billing brokers)
- invoices to facilities or private-pay clients
- reimbursement calculations and settlements owed to subcontractors
- in some programs, mileage reimbursement paid to members who drive themselves or are driven by a companion

No-shows, cancellations, and partial completions are documented with the same care, because they determine what may — and may not — be billed.

### One structure, many implementations

The core model is conceptual. Current products realize each structure differently:

```text
Passenger eligibility context:
  program benefit enrollment, facility contract, private pay, membership program

Fulfillment network:
  own fleet, contracted provider network, subcontracted brokers-of-providers,
  rideshare driver augmentation, volunteer driver programs

Payment path:
  payer claims, broker billing templates, facility/private-pay invoices,
  subcontractor reimbursement, member mileage reimbursement
```

A reader who has only seen one realization — for example a Medicaid broker platform — should still be able to recognize a private-pay fleet operator's system or a transit agency's healthcare-trip operation from the same core.

## How It Works

### Request intake

```text
Trip request arrives
→ from the passenger (portal/app/phone), a facility (portal/phone),
   a broker feed (into a provider's system), or a program call center
→ passenger identified against the passenger of record
→ needs and mode requirement attached
```

Mature products support all of these channels; which dominates is a property of the program, not the Type. Phone intake with agent-entered trips remains widespread alongside self-service portals.

### Eligibility and needs

```text
Passenger checked against the funding program's rules
→ eligibility confirmed (enrollment status, benefit terms, trip-level authorizations where required)
→ needs assessment determines the mode/accommodation the trip must have
→ recurring treatment schedules can be established as standing orders
   that generate trips for each treatment date
```

Eligibility is the gate that makes the trip bookable at all in program contexts; in facility-contracted and private-pay contexts the contract or the payment method plays the same role.

### Scheduling and assignment

```text
Trips for the day assembled into a schedule
→ mode-appropriate vehicle and driver chosen for each trip
→ routes built to minimize vehicles and drivers while honoring pickup windows
→ shared-ride loading (multiple passengers in one vehicle) where the program allows it
→ schedule published to drivers and providers
```

Scheduling is the intellectual center of the provider's day: the system's value is building a feasible, efficient plan from trips whose times are fixed by appointments. In the broker posture, the same act happens one level up — trips are assigned to subcontractor providers, by standing rules (this passenger's trips always to this provider), by standing order, or case by case for efficiency.

### Day-of dispatch

```text
Day begins → drivers receive manifests on mobile devices
→ status updates flow back (en route, arrived, passenger on board, dropped off)
→ GPS keeps the dispatch picture current
→ exceptions handled in real time:
   no-shows, last-minute "ready now" return requests (will-calls),
   add-on trips, cancellations, driver absences, vehicle breakdowns, traffic
→ dispatch re-optimizes: reassign, re-route, or hand the trip to another resource
```

The exception vocabulary is stable across the sampled products — no-shows, will-calls, add-ons, cancellations, breakdowns, driver call-offs — because these are the failure modes of appointment-bound shared transportation.

### Completion, verification, and payment

```text
Trip completed → timestamps and route recorded; driver confirms
→ verification evidence retained (GPS, timestamps, confirmations)
→ completed trips batched into the payment path:
   payer claims / broker billing files / invoices / subcontractor reimbursement
→ claim and payment status tracked back onto the trip
→ disputed or unverified trips held out of billing
```

The loop closes on money: the platform's record of what actually happened is what the funder pays for, which is why verification machinery (and fraud-and-abuse monitoring built on it) is standard in mature products.

## Interfaces

### Operations console (broker or provider)

The dispatcher's and program staff's primary surface: the day's trip schedule, trip search and filtering, assignment and reassignment, exception queues, and — on the broker side — subcontractor management and credential review. Typical information: passenger, addresses and times, mode, assigned provider/vehicle/driver, trip status, billing status. Primary actions: enter/edit trips, assign, dispatch, turn trips back, document exceptions.

### Driver app / mobile data terminal

The driver's working surface: the day's manifest in order, navigation, per-trip status actions, completion confirmation, and sometimes payment collection and vehicle checklists. Primary actions: start trip, arrive, load passenger, complete, report exception.

### Member / passenger portal and app

The passenger's self-service surface: request a ride (date, pickup, drop-off, return), view upcoming and past trips with status and provider information, track the assigned vehicle in real time, cancel, request accommodations (attendant, accessible vehicle), and in some products submit mileage reimbursement for self-driven trips. Primary actions: request, review, track, cancel.

### Facility portal

The healthcare facility's surface for booking trips on behalf of patients: register the patient's trip needs, book routine and recurring appointment transport, and track trip status. Primary actions: register patient, book trip, view status.

### Phone / IVR channel

A first-class channel rather than a legacy fallback: passengers book and check trips by phone through agents or automated voice systems, and automated outbound calls deliver trip reminders and pickup-time notifications.

## Important Rules / Behaviors

- **Eligibility gates the trip.** In program contexts a trip cannot be scheduled for a passenger the program does not cover; eligibility is checked at intake, commonly against enrollment data exchanged with the payer, and some trip types require documented medical justification (for example a physician certification for higher-acuity modes).
- **Needs determine the mode.** The passenger's recorded needs — not preference or availability — decide what vehicle and service level the trip requires; dispatching a mode-inappropriate vehicle is a compliance failure, not just a service failure.
- **Completion must be verified before payment.** The verified record (timestamps, GPS, confirmations) is the basis of billing; unfulfilled or unverifiable trips must not be billed, and no-shows must be documented to defend against disputes.
- **Credentials gate assignment.** Drivers and vehicles whose certifications, insurance, or training have lapsed are excluded from assignment — in mature products automatically, with expiry reminders to the provider and the program.
- **The appointment time anchors the schedule.** Pickup times are computed backward from appointment times within program punctuality rules; on-time performance against those windows is the headline operational metric.
- **Exceptions are documented, not just handled.** No-shows, cancellations, and breakdowns all leave records because they carry program, payment, and dispute consequences. In broker networks, a subcontractor that cannot perform its trips can hand them back to the program, and that hand-back is itself recorded.
- **Program rules vary and are local.** Covered destinations, mode menus, attendant rules, reimbursement rates, and required forms differ by program and jurisdiction; the platform encodes them as configurable rules rather than assuming one regime.

## Variants

- **Broker-operated program platform** — the operator administers a transportation benefit end to end: eligibility, intake, network management, subcontractor settlement, program reporting. Fulfillment is subcontracted.
- **Provider-operated fleet platform** — the operator runs its own vehicles and drivers, receives trips from brokers/facilities/direct customers, and lives on scheduling efficiency and clean billing.
- **Transit / paratransit heritage operation** — public or nonprofit transit agencies running healthcare trips on demand-response machinery; the scheduling core is shared with paratransit, wrapped in healthcare program rules.
- **Facility-contracted transport** — hospitals and health systems contracting transport directly, with hospital discharge (freeing beds) as a distinctive urgent-but-not-emergency workload.
- **Program-specific populations** — elderly comprehensive-care programs, senior living communities, and social-services programs extend destinations beyond clinical appointments.
- **Mileage reimbursement operation** — in some programs, part or all of the benefit is paid as reimbursement for self-arranged drives, with the platform verifying trips and processing claims rather than dispatching vehicles.
- **Rideshare-augmented networks** — credentialed rideshare drivers layered onto contracted provider networks for capacity and short-notice coverage.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| EMS Operations Platform | adjacent sibling | emergency response incidents + clinical care documentation (patient care reports) are the core there; NEMT is scheduled, non-emergency, and clinically undocumented. Non-emergency ambulance transport is a mode inside NEMT, not EMS response |
| Ride-hailing Platform | adjacent | open public, on-demand, consumer-paid, no eligibility or appointment binding; rideshare fleets may fulfill NEMT trips, but the closed eligible population and program billing are the boundary |
| Taxi Dispatch Platform | adjacent | public on-demand hailing without eligibility/program structure; some NEMT operators are cab companies, but the program wrapper defines this Type |
| Paratransit / demand-response transit | adjacent, shared machinery | serves the transit agency's eligible public under transit rules; NEMT serves healthcare access under health-program rules — same scheduling machinery, different program wrapper |
| Employee Transportation Platform | sibling structure | employer-admitted workforce moved for commuting; NEMT moves a patient/member population for healthcare access |
| School Transportation Management | sibling structure | student population on school-calendar routes; different population, purpose, and rules |
| Fleet Management System | component relationship | vehicles as assets (maintenance, telematics); in NEMT the trip is the unit of work and fleet upkeep is a module |
| Dispatch Management | component relationship | generic assignment/status/routing machinery is one layer inside NEMT, which adds passenger needs, eligibility, modes, and program billing |
| Patient Scheduling | adjacent | owns the clinical appointment; the NEMT trip references the appointment time but does not manage the appointment |
| Prior Authorization Platform | adjacent | payer-side coverage-approval machinery for medical services; trip-level medical justification inside NEMT is a rule of the trip lifecycle, not that Type |
| Transportation Management System / TMS | different domain | freight movements, not passenger journeys |

The most important boundary is with **EMS operations**: both move patients, but EMS is organized around unscheduled emergency response and clinical documentation, while NEMT is organized around scheduled access to care. The second most important is with **ride-hailing/paratransit**: all three schedule vehicles for passengers, and the machinery overlaps; the population (eligible members vs public), the purpose (healthcare access vs any trip), and the money (program-funded vs consumer-paid/fare-funded) are what separate them.

## Representative Products

- **MTM Link (MTM Health)** — broker-operated program platform: member portal/app, facility portal, provider access, driver app, program analytics.
- **RouteGenie** — provider all-in-one (scheduling, dispatch, routing, billing, fleet, driver and passenger apps) with a separate broker edition for subcontractor, credentialing, and eligibility management.
- **TripMaster (CTS Software / Transit Technologies)** — established provider suite with demand-response and paratransit heritage, deep broker-integration orientation, and IVR/rider-portal channels.

The core model was checked against the paratransit/transit heritage of the sample (the same scheduling machinery serving public transit) and against private-pay and facility-contracted operations, to avoid defining the Type by the Medicaid broker pattern alone.

## Sources

Research date: **2026-09-09**

- MTM Health — MTM Link member portal/app overview: https://www.mtm-inc.net/mtm-link/
- MTM Health — NEMT service and platform description: https://www.mtm-inc.net/healthcare/nemt/
- MTM Health — Transportation provider network: https://www.mtm-inc.net/service-providers/
- MTM Health — Healthcare facility trip intake and forms: https://www.mtm-inc.net/healthcare-providers/
- RouteGenie — provider platform overview: https://routegenie.com/
- RouteGenie — Broker Edition: https://routegenie.com/nemt-broker-software/
- RouteGenie — billing: https://routegenie.com/nemt-billing-software/
- RouteGenie — scheduling: https://routegenie.com/nemt-scheduling-software/
- TripMaster (CTS Software) — suite overview: https://www.cts-software.com/

> Sourcing limitations: two additional candidate products (RoutingBox, WellRyde) could not be reached from the research environment (repeated failures / access denied) and were excluded; the provider-side sample therefore rests on two products plus the broker-side sample. The fetched sample is US-centric in vocabulary; the definition above is deliberately written without US program machinery in its core, and non-US patient-transport software was not directly sampled. Precise vendor-claimed metrics (call volumes, performance percentages) and product-specific rules observed on single products are intentionally not stated as general facts in this document; they are recorded in the paired Research Notes.
