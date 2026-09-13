# Taxi Dispatch Platform

## Overview

A **Taxi Dispatch Platform** is the operator-side system a taxi (and private-hire or livery) company runs its dispatch operation on. It captures fare-bearing passenger transport bookings from the operator's channels, holds a live picture of which drivers and vehicles are available to work, allocates each booking to a specific driver-and-vehicle, tracks the job through pickup and completion, and closes it into the operator's commercial records — the fare, the payment, and the driver's share.

The defining core is deliberately small:

```text
Fare-bearing passenger transport job (booking)
  ↓ allocated against
Live availability of the operator's own driver-and-vehicle fleet
  ↓ tracked through
Job lifecycle → completion → payment + driver settlement
```

Everything else commonly associated with modern taxi technology — passenger apps, GPS maps, automatic allocation, caller ID, card payments, inter-fleet networks — is widespread in current products but is not what makes the system a dispatch platform. Radio-era dispatch offices running on voice, zone boards, and paper dockets satisfied the same core, and the modern products are best understood as that operation carried into software.

The boundary that matters most: a taxi dispatch platform is the **fleet operator's** system. The passenger does not create a request in a shared marketplace; bookings arrive through channels the operator manages, and the operator's own fleet is the supply being allocated. When the passenger creates the request in a marketplace that aggregates supply across many providers, the product is a ride-hailing platform instead.

## Users & Context

Primary users, all on the operator's side:

- **Call-takers / dispatchers** — the operational heart. They take bookings by phone (often with caller-ID assistance), create and edit jobs, watch the live board and map, and assign jobs to drivers — manually or with system assistance.
- **Fleet managers / owners** — configure dispatch rules, zones, tariffs, shifts; manage driver and vehicle records; monitor performance and revenue.
- **Drivers** — receive job offers, progress their status, navigate, record fares and payments, and manage their documents through a driver app (historically a mobile data terminal or voice radio).

Secondary users:

- **Passengers** — book through the operator's channels (phone, app, web, reception) and receive confirmations, tracking, and receipts; they do not work in the system.
- **Account customers** — companies, hotels, and institutions with booking portals or standing arrangements, billed on invoice rather than per-ride.
- **Back-office staff** — handle billing, driver settlement, and compliance records.

The work environment is a dispatch office under time pressure: bookings arrive continuously, allocation decisions are made in seconds, and demand spikes must be absorbed without stranding customers. The system is the operational system of record for the whole fleet business — the jobs, the availability, the money, and the compliance records all live here.

## Core Model

### The Defining Core

Four structures, jointly held. Remove any one and the product stops being a taxi dispatch platform:

**1. The fare-bearing passenger transport job.** The unit of work is a booking: a passenger ride with a pickup (address and time), a destination, service requirements (vehicle type, accessibility, extras), and a pricing basis — a metered tariff, a fixed rate or quote, or an account rate. The job carries its own fare semantics; this is what makes the work taxi work rather than generic dispatched labor. Jobs may be immediate ("as soon as possible") or booked in advance, simple point-to-point or multi-stop, one-off or recurring.

**2. The operator's own fleet as live dispatchable capacity.** Drivers and vehicles are held as the supply. Each driver carries identity, licensing and compliance documents, and an availability state; each vehicle carries its attributes (accessible, executive, standard) and compliance status. Availability is organized along two axes: **time** (shifts and schedules — when a driver is working) and **space** (zones and queues — where a driver is posted and waiting). Allocation consumes this state; performing a job changes it.

**3. The allocation act.** An incoming job starts unassigned. The central managed transition is binding it to a specific driver-and-vehicle — by a dispatcher's hand, by system recommendation, or automatically under configured rules. The act is visible, governed, and reversible (jobs can be reassigned).

**4. The tracked lifecycle closing into the commercial record.** Every job is tracked from capture through allocation and performance to a terminal state — completed, cancelled, or no-show. Completion produces the commercial record: the fare, the payment (cash, card, app, or account invoice), and the driver's share for settlement. The job history is the operator's business record.

```text
Booking (fare basis, pickup, destination, requirements)
  → unassigned queue
  → ALLOCATION (manual / assisted / automatic)
  → driver-and-vehicle bound
  → en route → on board → completed
  → fare + payment + driver settlement recorded
terminal exceptions: cancelled / no-show / uncovered (overflow)
```

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:  Booking intake
Realizations:  call-taking console (with caller ID), passenger app,
               web booking widget, corporate account portal, partner/API feed

Concept:  Availability state
Realizations:  shift/schedule sign-on, zone queues with waiting order,
               posted-available status, GPS-verified zone book-in

Concept:  Allocation
Realizations:  manual dispatcher assignment, closest-vehicle rule,
               traffic-aware fastest-ETA rule, zone-queue first-in-first-out,
               broadcast to drivers with bidding

Concept:  Fare basis
Realizations:  metered tariff tables, fixed rates and quotes,
               account rates, regulated council tariffs

Concept:  Commercial record
Realizations:  cash, in-car card, app payment, account invoicing;
               driver commission/lease accounting and payouts
```

A reader who has only seen one implementation — say, an app-centric operation — should still be able to recognize a radio-and-pegboard dispatch office as the same Type from this core.

### Standard Capabilities of Mature Products

These are common in current products and expected by the market, but they are additions to the core, not the definition:

- **Live map and vehicle tracking** — real-time positions and statuses of the fleet on a map, alongside the job board.
- **Configurable dispatch rules** — operators translate local knowledge into allocation behavior (prioritize speed, fairness, zone coverage, driver earnings equity) and schedule different rule profiles for different times or zones.
- **Caller ID and telephony integration** — the booking form auto-populates when a known customer calls.
- **Driver app** — job offers, acceptance, navigation, status progression, messaging, in-app metering, document access.
- **Pricing engines** — tariff tables, fixed fares, surcharges (holidays, zones), discount codes, quotes and estimates before booking.
- **Payment capture and driver settlement** — multi-channel payments plus automatic driver accounting.
- **Corporate account management** — account users, travel rules, invoicing, reporting.
- **Driver and vehicle records** — licenses, insurance, disclosures, plate and inspection compliance, vehicle attributes.
- **Passenger records** — history, preferences, saved addresses, and flags (priority treatment or blocking).
- **Exception machinery** — cancellation, no-show handling, reassignment, overbooking protection, overflow routing to partner fleets.
- **Notifications and tracking** — confirmations, arrival alerts, live trip tracking links, receipts.
- **Reporting and analytics** — trip volumes, channel mix, driver performance, revenue by zone or account.
- **Inter-fleet work exchange** — sending uncovered bookings to partner fleets and accepting inbound work; app roaming networks.

## How It Works

### The dispatch loop

The daily operation is a continuous loop over a stream of jobs:

```text
1. CAPTURE   A booking arrives — by phone (call-taker with caller ID),
             passenger app, web booking, account portal, or partner feed.
             The system records pickup, destination, time, requirements,
             and the pricing basis; duplicates and account rules are applied.

2. PRICE     The job is priced under the applicable basis — tariff,
             fixed rate, quote, or account rate. Estimates can be given
             to the passenger before confirming.

3. QUEUE     The job enters the unassigned queue, visible on the
             dispatch board with its pickup time, location, and any
             special-requirement flags.

4. ALLOCATE  The job is bound to a driver-and-vehicle:
             - manually, by a dispatcher reading the live board and map;
             - by recommendation, with the system proposing candidates;
             - automatically, under configured rules — closest vehicle,
               fastest traffic-aware ETA, zone-queue order, or broadcast
               to drivers who accept/bid.
             The driver receives the job on the driver app — in some
             products, accepting or bidding before the assignment is final.

5. PERFORM   The driver progresses the job: en route to pickup, passenger
             on board, completion. Position updates flow to the live map;
             dispatchers can message the driver; passengers may see
             tracking and arrival alerts.

6. CLOSE     The job completes: the fare is finalized (meter, fixed, or
             account), payment is captured or routed to invoicing, and the
             driver's share is recorded for settlement. The job becomes
             part of the operator's history and reporting.
```

Steps 1–4 run continuously and concurrently across dozens or thousands of jobs; the dispatch board is the shared working surface where the whole operation is visible at once.

### The availability loop

Allocation is only as good as the availability picture behind it:

```text
Driver starts a shift (sign-on, often from the driver app)
  → vehicle associated
  → driver posts available — in a zone queue or on the general board
  → allocation assigns a job; availability changes
  → job performed; driver returns to available (or ends shift)
```

Zone queues preserve fairness and coverage: drivers wait in order within a zone, and jobs in that zone go to the head of the queue. Some products verify with GPS that a driver is actually inside the zone before allowing the book-in. Shift schedules bound the whole structure — a driver works within their shift, and some products can block overtime by configuration.

### Demand protection

When demand outruns supply, the operation must act before customers are stranded. Modern products commonly watch live capacity against incoming demand, and some can enforce it as overbooking protection — holding new bookings, alerting the dispatch team, or automatically routing them to partner fleets through a networking arrangement. The same overflow logic, run in reverse, lets an operator accept inbound work from partners during quiet periods.

### Exceptions

Real operations are defined by their exceptions, and the platform is built to absorb them:

- **Cancellation** — by passenger or operator, before or after allocation; fees may apply under the fare rules.
- **No-show** — the driver at pickup with no passenger; recorded against the job and often against the passenger's history.
- **Reassignment** — a job moved to another driver (breakdown, delay, fairness correction); the availability state updates both ways.
- **Uncovered bookings** — no capacity to serve; held, escalated, or overflowed to partner fleets.
- **Failed payment** — card declined in-vehicle; recorded against the job and the driver's settlement until resolved.

## Interfaces

### Dispatch console

The dispatcher's primary working surface, typically multi-monitor.

- **Purpose:** capture bookings, watch the operation, allocate jobs.
- **Typical information:** job list (unassigned / assigned / active) with pickup time, addresses, requirements and flags; live map with vehicle positions and statuses; zone queues with waiting order; caller-ID pop-ups with customer history.
- **Primary actions:** create/edit a booking, check price and time, assign or reassign a job, message a driver, invoke a dispatch profile, handle exceptions.

### Live map

- **Purpose:** the spatial picture of supply and demand.
- **Typical information:** vehicle positions and statuses, job pickup points, zone boundaries.
- **Primary actions:** locate a vehicle or job, judge coverage, support allocation decisions.

### Driver app

- **Purpose:** the driver's side of the loop.
- **Typical information:** job offers with pickup, destination, distance, estimated time and price; current job details; zone queue position; shift and earnings summary; documents.
- **Primary actions:** start/end shift, accept or decline an offer, progress job status, navigate, record fare and payment, message dispatch, upload documents.

### Passenger channels

- **Purpose:** bring demand into the operator's system.
- **Typical surfaces:** phone (call-taker or automated IVR), passenger app (book now or later, track, pay), web booking widget, corporate account portal.
- **Primary actions:** request a ride or schedule one, receive confirmation and tracking, pay or attach to an account.

### Back office

- **Purpose:** run the business around the operation.
- **Typical surfaces:** tariff and zone configuration, dispatch rule profiles, driver and vehicle record screens with compliance documents, account management, billing and driver settlement, reporting dashboards.
- **Primary actions:** configure rules and tariffs, maintain records, invoice accounts, settle drivers, review performance.

## Important Rules / Behaviors

### Availability gates allocation

A job is allocated only to a driver-and-vehicle that is actually available — on shift, posted in a compatible zone or queue, with a vehicle type matching the job's requirements. The availability state is both a working picture and an access rule: it is what prevents double-assignment and phantom capacity.

### The allocation act is governed, not automatic by default

Even where auto-dispatch exists, operators keep control over the rules: which priority wins (speed, fairness, earnings equity, zone coverage), which zones get which profiles, and when profiles change. Scheduled profiles let the same system behave differently at a stadium event than at 3 a.m. The dispatcher can always override.

### The job carries its fare basis

Pricing is not an afterthought: the booking records whether the ride is metered, fixed, quoted, or on account, and the applicable tariff (including regulated rates, holiday and zone surcharges). Completion resolves the fare under that basis — the same job record drives the passenger charge and the driver's settlement share.

### Overbooking protection is a capacity rule, where present

Some products watch live capacity against incoming demand and stop silently accepting work they cannot serve — holding, alerting, or rerouting bookings. Where it exists, it changes how the dispatch office experiences demand spikes; where it does not, the same judgment happens in the dispatcher's head.

### Compliance records gate the fleet

Driver licenses, insurance, disclosures, vehicle plates and inspections are maintained in the system because the fleet's legal right to work depends on them. An expired document is an operational problem, not just paperwork.

### Passenger standing shapes service

Passenger records accumulate history and, in some products, can carry flags — priority treatment for good accounts, or blocking for abusive customers. The booking channel is therefore also a gatekeeping surface.

### Terminal states are recorded, not silent

Cancelled, no-show, and uncovered jobs remain in the record with reasons. They feed reporting, driver disputes, passenger flags, and network settlement with partner fleets.

## Variants

- **Service mix.** The same platform commonly serves taxi, private-hire, executive/chauffeur work, paratransit/NEMT contracts, school runs, and corporate shuttles — each adding its own requirements (accessibility, safeguarding, program rules) on top of the same dispatch core.
- **Demand posture.** On-demand-dominant operations (street-rail plus app demand, seconds-level allocation) versus prebook-dominant operations (chauffeur and livery work: quotes, scheduled dispatch grids over future reservations, payroll-style settlement).
- **Scale and structure.** Single-fleet SME deployments; multi-site operators running several fleets or brands in one system with shared overflow; bureaus aggregating multiple companies; inter-fleet networks and exchanges that trade uncovered work.
- **Call handling.** Own dispatch office; outsourced call-center services (automation, live agents, dispatcher tiers); IVR and voice-AI automation reducing live call-taking.
- **Meter posture.** Hardware taximeter integration; in-app meters; bring-your-own-device driver apps with built-in metering — shaped by local weights-and-measures regulation.
- **Regulatory regime.** Council-regulated tariffs and licensing (driver badges, plate expiry, fare tables) versus market-rate regimes where pricing is the operator's own.
- **Demand aggregation.** None; e-hail demand feeds from third-party apps; inter-fleet exchange; passenger-app roaming networks.
- **Deployment.** Cloud SaaS is dominant; legacy on-premises computer-dispatch systems (mobile-data-terminal era) still run the same core.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Ride-hailing Platform | adjacent, most confusable | passenger creates the request in a shared marketplace and the platform matches aggregated supply under platform pricing; a dispatch platform is the operator's own system — bookings arrive via operator channels and the operator's fleet is allocated. Operator passenger apps, inter-fleet exchanges, and taxi supply inside ride-hail apps are overlap zones, not Type collapses |
| Dispatch Management | generic sibling | shares the dispatch spine (work queue + resource availability + assignment + live picture) but without passenger-transport semantics, fare machinery, licensed fleet pairing, or regulated tariffs |
| Computer-aided Dispatch (CAD) | structural cousin | emergency incidents and unit status under response-priority rules, worked by public-safety telecommunicators — not commercial rides under tariff and fairness rules |
| Courier Management Platform | adjacent | goods pickup→delivery with proof of delivery and shipment custody; both have account rate engines, but the work unit and execution differ |
| Towing Dispatch Platform | sibling | same dispatch spine applied to vehicle recovery rather than passenger transport |
| Non-emergency Medical Transportation Platform | adjacent | scheduled medical transport centered on passenger needs/eligibility and payer/broker settlement; taxi dispatch products serve NEMT contracts as a service-mix variant |
| Fleet Management System | adjacent | vehicle register, in-service record, and oversight loop; job allocation is secondary there, central here |
| Public Transit / School / Employee Transportation | adjacent | scheduled route-and-run plans for defined populations; taxi dispatch allocates discrete jobs for open public demand |
| Hotel PMS / Reservation Systems | false friend | "dispatch" appears in both vocabularies, but a reservation system books capacity against a schedule; a dispatch platform allocates work against live availability |

## Representative Products

- **iCabbi** (Coolnagour Ltd, ex-Autocab) — enterprise taxi and private-hire dispatch platform, UK/Ireland/global; strong dispatch-rule configuration, zone profiling, multi-fleet sites, inter-fleet Exchange.
- **TaxiCaller** (TaxiCaller Nordic AB) — self-serve cloud dispatch for small and mid-size fleets, global; dispatch console with zone queues, closest-car / FIFO / broadcast-bid allocation, multi-service solutions.
- **Limo Anywhere** — chauffeur and livery pole (US/global): reservation-centric booking, scheduling, dispatch grid, driver payroll, affiliate network.
- **Curb Fleet Systems (Way2Cloud / e-Fleet / Call Center)** — US taxi-fleet systems with meter and payments heritage, outsourced call-center tiers, NEMT dispatch, and the Curb Flow demand network.

The defining core was checked against the radio-dispatch and mobile-data-terminal eras (zone pegboards, paper dockets, computerized dispatch of the 1980s–90s) to avoid defining the Type by today's app-and-cloud implementation.

## Sources

Research date: **2026-09-10**

- iCabbi — product site and Dispatch product page: https://icabbi.com/ , https://icabbi.com/platform/dispatch/
- TaxiCaller — product site, dispatch and driver-app feature pages, knowledge base (automatic assignment; booking channels): https://www.taxicaller.com/ , https://www.taxicaller.com/en/features/dispatch-system , https://www.taxicaller.com/en/features/driver-app , https://www.taxicaller.com/en/help/kb/741220 , https://www.taxicaller.com/en/help/kb/579405
- Limo Anywhere — product site, dispatch software page, knowledge center (New Dispatch Grid): https://www.limoanywhere.com/ , https://www.limoanywhere.com/dispatch-software/ , https://kb.limoanywhere.com/docs/new-dispatch-grid/
- Curb — rider/fleet site and Dispatch & Management page: https://www.gocurb.com/ , https://www.gocurb.com/fleet/dispatch-management
- Historical context (industry and trade sources): "Taxi – Dispatching" overview (primidi.com); D. McCurdy, "Taxi Dispatch Technology" (taxi-library.org); Gandalf mobile-data dispatch brochure (Anaheim Yellow Cab); The Independent, "Taxis on the super highway" (1994); TaxiPoint, "ComCab's Journey" (2024); TaxiCom '95 report (FTA).

> Sourcing limitations: iCabbi's support centre is login-walled, so its operational detail rests on official product pages and FAQ; Curb's fleet-system detail is product-page tier only. Exact state vocabularies, numeric limits, and settlement figures are intentionally not asserted in this document; product-specific claims (configuration counts, uptime figures, market statistics) were treated as vendor statements and excluded from the canonical description.
