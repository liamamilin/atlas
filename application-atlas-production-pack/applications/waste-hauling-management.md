# Waste Hauling Management

## Overview

A **Waste Hauling Management** application is the operator-side business system of record for organizations that collect waste and haul it away — residential and commercial collection routes, roll-off and skip container services, municipal collection fleets, and per-job removal work. It holds every served customer and location with the collection services configured and priced for it, turns each pickup into a service event dispatched to a truck crew, records what the crew actually collected in the field, and converts those recorded events into the operation's billing and service record.

The work it manages has a characteristic shape: the cargo is unwanted material **leaving** a customer's site toward disposal, transfer, or recovery, and the mobile unit is a **truck and its crew**. That shape — collecting and carrying away, rather than repairing, delivering, or relocating — is what makes this a distinct Application Type rather than generic field service or freight trucking.

The market realizes the Type in two connected realizations: **route-based waste hauling** (recurring collection rounds and container services — the center of gravity of the dedicated products) and **per-job removal** (quoted one-off cleanouts, frequently run on generic field-service platforms). A closely related leaf, Junk Removal / Waste Hauling Management, covers the same software from the local-service-business angle; the two name one Type (see Related Application Types).

## Users & Context

The operation runs on trucks; the software mirrors that.

Primary users:

- **owner / general manager** — owns pricing, service configuration, contracts, and profitability (per route, per job, per customer)
- **office staff / dispatcher** — books work, builds the day's routes or job schedule, assigns trucks and drivers, handles exceptions and customer calls
- **driver / crew** — executes the collections, records completions and problems at each stop, captures signatures or photos

Secondary users:

- **customer service / billing staff** — invoices, payment cycles, missed-service and complaint handling
- **scale-house or yard operator** (dedicated hauling operations) — weighs loads and issues disposal tickets
- **the customer or resident** — through self-service surfaces: online booking, payment, service history, service notifications

Typical context: independent haulers serving residential, commercial, and construction customers; larger haulers under municipal contracts; municipalities operating their own collection fleets; waste brokers subcontracting haulage. The office plans, bills, and answers; the road performs and reports back.

## Core Model

The application's world is organized around four connected things: the served customer, the service event, the truck that performs it, and the money and accountability that result from it.

### Customer service accounts

Every served customer or location is a standing record: who they are, where the truck goes, what the operation collects for them, and at what terms — a recurring weekly collection, an on-call removal, a container of a given size placed on site, or a quoted one-off job. Prices are configured per customer or per service: base collection, extra items, container rental, disposal-related charges, overweight charges. At the enterprise end this extends into contract management and per-customer pricing hierarchies. The account accumulates service history, which is what the office answers questions from and what billing is built on.

### The haul service event

The unit of work is the **service event** — a stop on a route, an order, a job: material to be collected at a location at a defined time or on demand. Every event belongs to a customer account, is scheduled (recurring round slot, booked appointment) or taken on demand, and is assigned to a **truck / driver / crew**. The event carries its execution record: completed or not, what was actually collected, exceptions ("no material out", "container blocked", "access denied"), and evidence the crew captures (photos, signatures, notes). Completed events become billable; exceptions become follow-ups, credits, or service-level records.

### Trucks, crews, routes

Trucks (with their drivers and helpers) are the performing resources. Work is organized for them as **routes** — an ordered day of stops — or as dispatched **jobs** — individual assignments sent to a truck. Route order can be planned in the office and adjusted by how the driver actually ran it; truck position and stop progress are commonly visible to the dispatcher in real time. Some products also hold each truck's service capability — weight class, lift type, container types — so dispatch does not send a truck that cannot handle the container.

### Billing from recorded service

Revenue follows the recorded work. Each completed event, with its attached charges, is priced to the customer's account and flows into invoices — per pickup or per job in the removal pole; per collection cycle, per container service, or by weight/volume measures in the route pole. Cash- and check-paying customers are handled in batches; billing cycles group who is billed when. In contracted municipal work, the same recorded service drives contract billing and chargeable-service income; where a municipality self-operates its fleet, the money loop narrows to chargeable extras and the service-accountability record, and some government-focused products ship without a full billing module at all.

### The disposal side

What was collected has to go somewhere. Dedicated hauling products track the outbound leg: weights captured at a scale or weighbridge, disposal or "tip" tickets, charges paid at the dump, and the destinations materials went to. In markets that require it, the system also produces the disposition paperwork — duty-of-care notes, transfer/consignment records, digital waste-tracking data. The per-job removal pole frequently leaves this leg outside the software; it is a standard capability of dedicated products rather than a requirement of the Type.

```text
Customer / Location (services + prices configured)
        ↓
Haul service event  (stop / order / job — material to collect)
        ↓ assigned to
Truck / Driver / Crew  (route or dispatched job)
        ↓ executed & recorded
Completion + exceptions + evidence
        ↓ priced from
Invoice / Payment   →   (disposal side: scale, tip tickets, destinations, paperwork)
```

## How It Works

### Recurring collection (route-based hauling)

```text
Customer account holds a recurring service (e.g., weekly collection, container on site)
→ recurring events generate on the calendar
→ dispatcher assembles / adjusts each truck's route for the day
→ driver runs the route in the in-cab or mobile app, completing stops
→ misses and problems reported at the stop (with photo, reason)
→ completions sync back to the office
→ billing cycle invoices the period's recorded services
```

### Container services (roll-off / skip)

```text
Customer orders a container (drop) or a pickup (pull / exchange)
→ dispatcher assigns a capable truck to the container job
→ crew delivers, exchanges, or pulls the container; placement recorded
→ rental period and service charges accumulate on the account
→ load hauled to disposal; weight and destination recorded
```

### Per-job removal

```text
Customer requests a pickup (call, web booking, lead source)
→ office books a job (or sends an estimate / quote first)
→ job assigned to a truck and time window
→ crew arrives, confirms scope, loads the material
→ job completed on the mobile app; invoice issued; payment taken on the spot or billed
→ load taken to disposal; costs recorded
```

### The daily dispatcher loop

Across all realizations, the office works a continuous loop: see today's schedule and route progress → assign and reassign work between trucks → work field exceptions (skipped stops, delays, complaints) → keep customers and residents informed → make sure completed work got billed and unresolved service got followed up.

## Interfaces

### Dispatch / scheduling board (office)

The dispatcher's primary surface: today's jobs and routes, trucks and drivers, drag-and-drop assignment, route progress on a map.

- typical information: stops or jobs, assigned truck/driver, status, exceptions, customer history at hand
- primary actions: assign, reassign, reroute, schedule, cancel, contact driver or customer

### Customer account screen (office)

Single view per customer: services and prices configured, containers or equipment on site, contact and location details, service history, invoices and payments.

- primary actions: configure services, set pricing, book work, log issues, review history, take payment

### Driver / in-cab application (in the truck)

The crew's surface: the day's route or job list on a map, stop details, completion actions. At the dedicated end this runs on in-cab tablets with sensors and cameras; at the light end, on the driver's own phone.

- typical information: next stop, location, access notes, container or material details
- primary actions: complete stop, report exception with reason and photo, capture signature, record extra work, navigate; works through dead zones and syncs later

### Billing workspace (office)

Invoice assembly and payment handling: billing cycles that group who is billed when, batch entry of cash/check payments, edge-case invoices separated from bulk runs, adjustments and billing audits, online payment processing.

### Customer / resident self-service

Online booking (quote → book → pay), account portal with invoices, e-tickets, service history, and — where the market requires it — recycling and disposition reports; service-change notifications that reduce inbound calls.

### Scale / disposal capture (dedicated hauling operations)

Scale-house or disposal-event recording: weigh-in/weigh-out, material and destination, ticket issuance, charges assigned to the right account; compliance paperwork generated from information already held in the system.

## Important Rules / Behaviors

- **Billing follows recorded execution.** What a customer is charged is derived from what the system recorded as done — completed stops, extra items noted by the crew, overfilled containers. Unrecorded work does not get billed; exceptions become credits or follow-ups rather than silent omissions.
- **The route as planned is not the route as run.** Drivers work around access problems, blocked containers, and no-shows; the system keeps the as-run order and reports, and dispatchers see both plan and reality.
- **Exceptions are first-class.** A skipped or failed pickup ("no material out", "container blocked", "site inaccessible") is captured at the stop with a reason — it must reach the office as a follow-up, affect service-level commitments, and be communicated to the customer or resident.
- **Containers are assets with placement state.** In container-based work, the software tracks which container sits at which customer, its size and service state, and keeps billing attached to the placed service rather than the specific physical unit, so swapping a container does not disrupt the account.
- **Truck capability can gate assignment.** Some products hold each truck's service capability (weight class, lift type, container types) and match container jobs to trucks that can actually perform them.
- **Cash and edge cases live beside bulk billing.** Haulers serve many pay-on-account customers and many cash/check customers; mature products separate edge cases from bulk invoice runs and support batch payment posting.
- **A confirmed schedule is not a completed service.** Completion depends on the crew's field capture; office records show scheduled vs completed, and missed-service handling is a permanent workflow.

## Variants

- **Residential / commercial route hauler** — recurring rounds, billing cycles, missed-pickup handling; the classic dedicated-product population.
- **Roll-off / skip container operator** — container drop, exchange, and pull cycle; rental periods; per-container and disposal charges.
- **Per-job removal business** — quoted cleanouts, bulky items, estate and construction debris; jobs over rounds; often run on generic field-service platforms (see the related Junk Removal / Waste Hauling Management leaf).
- **Municipal / government operation** — collection fleets run under contract (billing the municipality per recorded service) or self-operated by a city (service-level accountability, chargeable extras, resident communication); the same machinery commonly extends to street cleansing, winter maintenance, and street sweeping as additional configured services.
- **Waste broker** — subcontracted haulage with subcontractor portals, self-billing, and margin-per-job tracking.
- **Liquid waste operator** — septic, grease, and portable-toilet servicing running the same spine with liquid cargo.
- **Regulatory-context variants** — markets that require disposition documentation (duty-of-care notes, consignment records, digital waste tracking) add compliance paperwork machinery on top of the same core.
- **Era/deployment variants** — legacy desktop module suites (billing-led) through modern cloud SaaS (dispatch- and driver-app-led); the same spine persists across both.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Junk Removal / Waste Hauling Management | same Type, second directory leaf | Covers the identical software population from the local-service-business angle (per-job junk removal + dedicated hauling). Joint review held: one Application Type, two directory entries; merge recommended. |
| Small Business Field Service Management | adjacent / overlapping | Same job-book → dispatch → complete → invoice spine, but no haul-domain structures (containers as placed assets, recurring rounds, disposal legs, weight/volume billing). Per-job removal businesses are substantially served by generic field-service products. |
| Waste Management Platform | broader / program-side | Organization- or municipality-side waste program management (contracts, compliance, reporting across sites and contractors), not the hauler's own operating system of record. |
| Recycling Operations Management | facility-side | The material-recovery ledger at processing facilities (classification to stock, commodity-out) vs the collection business. Scale/weighbridge and ticket machinery is shared substrate; the recovery loop belongs to the recycling side. |
| Hazardous Waste Management | generator-side counterpart | The waste generator's compliance record for waste it ships out (profiles, accumulation, manifests) vs the hauler's service business. Hauler-side products treat disposition paperwork as documentation, not as the managed object. |
| Moving Company Management | adjacent | Same truck-and-crew shape, but cargo moves between two customer-controlled points (origin → destination); hauling cargo leaves the site toward disposal. Different pricing semantics. |
| Trucking Management System | adjacent | Both are truck-fleet business systems, but trucking centers freight loads hauled between points under the carrier's operating identity; hauling centers recurring collection service at served locations with disposal-side semantics. |
| Route Optimization Platform / Dispatch Management | capability vs system | Algorithmic routing/dispatch is one surface inside this Type; those Types are the capability alone, with no service accounts, service events, or billing. |
| Fleet Management / Vehicle Telematics | capability vs system | Connected-vehicle data and fleet reporting integrate into this Type but carry no collection business records. |
| Home Services Marketplace | consumer-facing counterpart | Two-sided venue matching customers with providers (removal is one trade among many); this Type is the operator's internal system, not the venue. |

## Representative Products

- **AMCS Platform** — enterprise-grade waste and recycling platform (commercial & industrial, municipal, construction & demolition, recycling): customer management with pricing hierarchies, route planning and dispatch, mobile workforce, scale operations, financial automation, business intelligence; municipal configuration extends to street cleansing and winter maintenance
- **Routeware (Elements / SmartCity)** — cloud, hardware-light suite for haulers and governments: dispatch, in-cab tools, CRM, billing and payments, compliance publishing; SmartCity serves municipal collection fleets and adjacent public-works services
- **CRO Software** — ERP for waste businesses from owner-operators to multinationals: solid waste, roll-off & dumpster, liquid waste, scrap & recycling; drag-and-drop dispatch, asset tracking, recurring services, invoicing
- **Waste Logics** — UK cloud waste-business automation (skip hire, trade waste, MRFs, brokers): orders, rounds, driver apps, weighbridge, duty-of-care and consignment paperwork, digital waste tracking, customer portal

The defining model was also checked against the dedicated hauler products documented in the related Junk Removal / Waste Hauling Management leaf (Trash Flow, Hauler Hero), a generic field-service platform serving the per-job pole (Workiz), a non-US regulatory market (UK trade waste/skip hire), a legacy desktop generation, and paper-era analog operations, so the definition does not depend on any single era, region, or vendor pattern.

## Sources

Research date: **2026-09-10**

- AMCS — https://www.amcsgroup.com/ ; platform (https://www.amcsgroup.com/solutions/amcs-platform/) ; municipal (https://www.amcsgroup.com/solutions/amcs-platform-for-municipalities/)
- Routeware — https://routeware.com/ ; Elements (https://routeware.com/products/routeware-elements/) ; SmartCity (https://routeware.com/products/routeware-smartcity/)
- CRO Software — https://www.crosoftware.net/
- Waste Logics — https://wastelogics.com/ (home incl. features, plugins, FAQ)
- Cross-referenced prior passes: research/junk-removal-waste-hauling-management.md (2026-09-08), research/recycling-operations-management.md (2026-09-09), research/hazardous-waste-management.md (2026-09-08)

> Sourcing limitation: vendor help-center / user-manual articles were not reachable from the research environment (consistent with prior passes); all observations above come from official vendor product pages, which document feature existence and positioning but not detailed screen-level workflows. Accordingly, this document deliberately states no numeric limits, exact status names, default settings, or precise workflow sequences, and keeps workflow descriptions conceptual. Detailed evidence, single-product observations, and rejected marketing claims are recorded in the paired Research Notes.
