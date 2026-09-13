# Research Core Facility Management

## Overview

A **Research Core Facility Management** application is the operating system of a shared research facility — a "core facility" or "shared resource" that offers expensive instruments and specialized services to a population of researchers drawn from many labs, and recovers its operating costs through usage-based charging.

It solves a specific operational problem: an institution buys instruments (sequencers, microscopes, flow cytometers, mass spectrometers, NMR) that no single lab can afford or fully utilize, staffs them with experts, and opens them to a researcher community. The facility must control who may use what, schedule time on instruments, accept and fulfill service requests, record who used what for how long, and turn that recorded usage into charges billed to the labs' grants, departmental accounts, or external organizations.

The defining structure is small:

```text
Shared instrument/service catalog (rate-bearing, presented as the facility's storefront)
└── Identified researcher (member of a lab/group with funding sources)
    └── Reservation (instrument time) or Service Request (facility-performed work)
        └── Recorded usage
        └── Charge (priced at facility rates, internal/external tiers, subsidies)
            └── Recharge to funding source → invoice/statement → utilization & revenue reporting
```

Everything else commonly associated with these systems — training and certification tracking, kiosks and hardware interlocks, maintenance management, sample manifests, publication tracking — is standard or optional machinery that makes the operation practical. It is not what makes the product this type.

When the facility-service economics disappear (no rates, no funding-source charging, no financial approval), the product drifts toward a plain resource calendar. When sample and assay workflows become the center of gravity, it drifts toward a LIMS.

## Users & Context

Primary users:

- **Facility manager / core administrator** — configures the catalog, schedules, booking rules and rates; approves reservations and requests; runs the billing cycle; reports utilization and revenue. This role owns the system.
- **Facility staff / core members** — perform services, validate and process requests, maintain instruments, run day-to-day operations.
- **Researcher (core customer)** — a lab member who reserves instrument time, submits service requests, selects the payment source, and tracks their own requests and reservations.
- **Principal Investigator (PI) / lab manager** — the financial authority over a lab/group: assigns payment sources (funds) to lab members, approves spending above thresholds, and sees what the lab is being charged.

Secondary users:

- **Institutional administrators** — cross-facility oversight, user and group management, institution-level reporting.
- **Finance / accounting** — receives invoices and journals; the system typically integrates with the institution's ERP or financial system.
- **External users** — researchers from other institutions or commercial customers, who order with purchase orders or other external payment methods.

Typical context: universities, research institutes, teaching hospitals, pharmaceutical and biotech companies, and shared/incubator laboratories. Facility types include genomics, sequencing, proteomics, flow cytometry, light and electron microscopy, histology, mass spectrometry, metabolomics, NMR, structural biology, vector cores, and bioinformatics. A single institution commonly operates many such facilities on one deployment of the system.

## Core Model

### The Defining Core

Three structures held together. Each one is load-bearing: remove it and what remains is a different kind of software.

**1. The shared instrument/service catalog.** The facility's offerings are held as managed objects: instruments that can be reserved as time on a schedule, and services that can be ordered as requests. Each offering carries a description, visibility controls (who may see and book it), and pricing. Presented together, the catalog is the facility's storefront — the place where researchers discover what the facility offers and on what terms. Without the catalog there is no facility being operated, only a list of assets or a rate sheet.

**2. Identified-user reservations and service requests with usage attribution.** Researchers act as identified members of labs/groups. They reserve time slots on an instrument's schedule, or submit a service request for work the facility will perform. Every reservation and request is attributed to the identified user and their group, and carries a payment source chosen from the sources assigned to that group. This attribution is the join key for everything downstream: access control, usage records, charges, and reporting. Without it, the system is an anonymous booking board.

**3. The usage-to-recharge loop.** Recorded usage and completed work are priced at facility rates — with different tiers for internal and external customers, and subsidies where institutional policy provides them — accumulated as charges, and billed on a recurring cycle (commonly monthly) to funding sources: grant numbers, departmental accounts, project IDs, or purchase orders. The loop produces invoices or statements for the paying parties, and utilization/revenue reporting for the facility and institution. Without this loop, the product is a resource calendar.

### The Objects

- **Facility (core / shared resource)** — the operating unit: one imaging facility, one genomics core. An institution typically runs many; the system supports both single-facility and multi-facility deployments.
- **Instrument / resource** — a bookable shared asset. The concept is deliberately broad: usually a piece of equipment, but also rooms, or time with a specialist.
- **Schedule / calendar** — the collection of available and reserved time slots for one instrument. The calendar is the operational heart of every product in this space.
- **Reservation** — a claim on a specific time slot, made by an identified user under a specific lab/group and payment source.
- **Service and service request** — work the facility performs for a researcher (e.g., run samples, prepare libraries, image specimens). A request carries forms/questionnaires, a quote where cost is not fixed, an approval, staff assignment, and progress phases.
- **User, lab/group, PI** — the researcher population is organized into groups led by PIs; the group is the financial responsibility unit.
- **Fund / payment source** — the vehicle a charge is billed to. The same concept appears under many institutional names: grant number, chart-field string, speed code, account number, project ID — or, for external customers, a purchase order.
- **Rate and subsidy** — the price rules of the facility: hourly or per-service rates, internal/academic/commercial tiers, subsidies and rebates applied automatically by eligibility.
- **Charge** — an individual line item corresponding to a specific product or service provided: a reserved hour, an assisted session, a processed sample, a consumable.
- **Billing cycle / invoice** — the periodic compilation of charges into invoices or journals delivered to funding sources and finance systems.
- **Training / qualification record** — the record that a user is qualified to use an instrument; in mature products it gates access.
- **Usage record** — the actual time or quantity consumed. Mature products distinguish booked time from actual time and may bill on either.

### One Structure, Many Implementations

The core model is conceptual. Common implementations vary:

```text
Concept:            payment source (fund)
Implementations:    grant number, chart-field string, speed code, account number,
                    project ID, purchase order, credit card, wire transfer

Concept:            usage capture
Implementations:    booking-based billing, kiosk check-in sessions, workstation
                    usage apps, card readers / door controllers, hardware
                    interlocks on instrument power

Concept:            catalog
Implementations:    storefront page per facility, searchable asset directory,
                    categorized service price list
```

A reader who has only seen one implementation (e.g., a university genomics core billing grant numbers monthly) should still be able to recognize the others (a commercial shared lab invoicing POs; a subsidized core where charges resolve to zero) from the core model.

## How It Works

### Onboarding: from researcher to qualified user

```text
Researcher registers (often with institutional credentials via SSO)
→ joins a lab/group (or requests membership)
→ PI or lab manager assigns payment sources (funds) to the group's members
→ researcher completes training for the instruments they need
→ access to those instruments is granted
```

There is no procurement and no negotiation at this stage: the facility's catalog is already configured; onboarding only connects a person to a group, a payment source, and a qualification.

### The instrument self-service loop

```text
Browse the facility catalog (descriptions, pricing, rules)
→ open the instrument's calendar
→ drag-select a time slot
→ choose lab/group + payment source
→ complete required forms (if any)
→ submit (auto-confirmed, or pending core approval)
→ arrive at the instrument; start the session (kiosk / interlock / card reader where deployed)
→ usage is recorded (booked time, and actual time where captured)
→ charge is computed at the instrument's rate for the usage type
→ charge accumulates for the billing cycle
```

The reservation carries its economics with it: the cost estimate is visible at booking time, the usage type (e.g., assisted vs unassisted) can change the rate, and additional service charges (consumables, staff help) can be attached to the same reservation.

### The service request loop

```text
Browse the facility's services
→ initiate a request; complete its forms/questionnaires
→ select payment (internal fund, or PO for external customers)
→ submit
→ facility reviews; issues a quote where cost is not fixed
→ customer accepts the quote
→ financial approval by the PI / lab manager (auto-approved below a threshold)
→ facility staff perform the work through defined phases
→ charges are recorded against the request
→ status is visible to the customer throughout
```

The quote-approval step is typically bypassed when the price is fixed at submission or the work is free of charge.

### The billing cycle

```text
Charges accumulate from reservations, sessions, and completed requests
→ facility admin reviews and generates the billing run
→ invoices/statements produced per funding source (and per external customer)
→ financial journals exported / uploaded to the institution's ERP or billing system
→ PIs see what their labs consumed; finance reconciles
```

Subsidies are applied as separate line items; split charges can allocate a single consumption across several funds by percentage.

### The facility administration loop

```text
Configure instruments, schedules, booking rules, rates, and visibility
→ monitor bookings, incidents, and downtime
→ maintain instruments (maintenance schedules, work orders)
→ run billing
→ report utilization, revenue, and outcomes to institution leadership
```

### Core vs standard vs optional capabilities

**Defining core** — without these, not this type:

- shared instrument/service catalog with pricing and visibility
- identified-user reservation/request with lab/group and payment-source attribution
- usage-to-recharge loop: rates → charges → funding sources → invoices/reporting

**Standard capabilities** — present in most mature products:

- training/qualification management gating access
- service request workflows (forms, quotes, phases, staff assignment)
- actual-usage capture (kiosk, workstation app, card readers, interlocks, walk-up sessions)
- maintenance and incident management
- reporting and analytics (utilization, revenue)
- SSO with institutional identity; ERP/finance integration
- multi-facility institutional deployment
- notifications to users (confirmations, cancellations, downtime)

**Optional / variant** — depends on segment and funding model:

- external/commercial commerce (POs, standing POs, credit card, wire)
- subsidy models (automatic subsidies, centrally-assigned funds, split charges)
- publication/research-output tracking linked to facility usage
- scientific project management with milestones
- sample manifests and sample/run lifecycle tracking
- consumables/inventory management
- cloud vs self-hosted deployment

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Facility catalog / storefront

The researcher's entry surface.

- lists the facility's instruments and services with descriptions, policies, and pricing
- primary actions: open an instrument schedule, initiate a service request, read facility information

### Instrument calendar

The schedule of one bookable resource.

- time slots in day/week/month views; color-coded entries distinguish the user's own reservations, other users' bookings, unavailable/maintenance time, and reservations pending approval
- primary actions: create a reservation (drag-select a slot), move/resize it, cancel it, view pricing and rules

### Reservation form

The transaction surface of the self-service loop.

- lab/group selection, payment source, usage type, cost estimate, required forms, linked resources, repeating options, notes
- primary actions: save, cancel (with fee acceptance where configured)

### Service request workspace

The request lifecycle surface.

- request list with statuses; request detail with forms, quote, payment, approval state, phases, and staff notes
- primary actions: initiate, submit, accept a quote, track status, communicate with staff

### My reservations / my requests

The researcher's personal history.

- upcoming and past reservations; request statuses; primary actions: start a session (where kiosk-based), modify, cancel, review charges

### Session / kiosk surface

The physical-usage surface, where deployed.

- login with credentials; start a scheduled session or a walk-up session; elapsed-time clock; extend; finish; add-on charges; payment selection
- often coupled to instrument power or access control (interlock, card reader)

### Administration console

The facility staff's working surface.

- resource and schedule configuration; booking rules; rate and subsidy configuration; request queues (validation, assignment, phases); user and training administration; billing runs; report builders
- primary actions: configure, approve, assign, bill, report

### Finance surfaces

- invoices and statements per funding source; financial journals; exports/uploads to ERP systems

## Important Rules / Behaviors

### Financial approval gates the work

A reservation or request is not merely "booked" — it carries a payment source, and spending typically requires approval by the group's financial authority (PI or lab manager) before the facility starts work or the reservation is confirmed. Amounts below a configurable threshold are commonly auto-approved. This makes the PI structure an access-control structure, not just an org chart.

### Reservations have states and economics

A reservation may be auto-confirmed or pending core approval; approved reservations are commonly locked against casual change. Cancellation is rule-governed: deleting far enough ahead of the slot is free, late cancellation becomes a cancellation (often with a fee that must be accepted), and no-shows may be charged. These rules protect instrument utilization — the facility's scarcest resource.

### Booked time is not always billed time

Where actual-usage capture exists (kiosk sessions, workstation apps, interlocks), the system distinguishes booked time from actual time, and billing may follow the actual usage. Walk-up sessions on open instruments are a first-class flow, not an exception.

### Access is qualification-gated

Instruments are commonly locked — procedurally and sometimes physically — until the user is trained: training records, verification steps, and progressive access levels determine who can book or operate what. Hardware interlocks and card readers enforce the same rule physically.

### Rate tiers and subsidies are structural

The same instrument hour can carry different prices for internal academic users, external academic users, and commercial customers; subsidies can be applied automatically by eligibility; a single consumption can be split across several funds by percentage. The pricing model is part of the facility's policy, configured in the system.

### Payment sources have lifecycles

Funds expire (grants end); the system warns users when a chosen fund is near expiry. External customers may need formally approved standing purchase orders before they can pay at all.

### The catalog is a visibility surface

Instruments and services can be made visible or hidden to specific user groups; the same facility can present different offerings to internal and external populations.

## Variants

- **Instrument-based (self-service) cores** — the researcher operates the instrument; the system's center is scheduling, access, and time-based charging.
- **Service-based cores** — the facility performs the work; the system's center is request intake, quoting, phases, and per-service charging. Most real facilities mix both shapes.
- **Internal-only vs externally-facing facilities** — some serve only their institution; others actively sell to external academic and commercial customers, with PO-based commerce and commercial rate tiers.
- **Subsidized / free-at-point-of-use facilities** — the recharge machinery runs, but subsidies or institutional funding absorb the charges; reporting, not invoicing, carries the value.
- **Single facility vs institution-wide deployments** — one core adopting a tool vs an institution standardizing many cores on one system with cross-facility oversight and consolidated reporting.
- **Non-university operators** — pharma internal facilities, biotech, CROs, and incubator shared laboratories run the same model with commercial payment mechanics.
- **Deployment** — vendor-hosted cloud is dominant; self-hosted installation persists where data must remain inside institutional infrastructure.

A variant remains a variant unless it changes the users, core objects, workflow, or rules so much that the defining core no longer applies.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Laboratory Information Management System / LIMS (incl. Research LIMS) | adjacent, frequently integrated | LIMS is sample/assay-centric (samples, test runs, results, chain of custody); core facility management is access/usage/economics-centric. Sample data may travel through service requests in both, but the centers differ. |
| Scientific Instrument Management | overlapping module | Instrument registry, maintenance, calibration and lifecycle are one operational ring here; the center of this type is the facility's service operation to a researcher population, not the asset lifecycle itself. |
| Resource Calendar | downstream sibling if economics are removed | A resource calendar books time on shared things but has no rate-bearing catalog, no funding-source charging, no financial approval, no recharge reporting. Remove the recharge loop from this type and a resource calendar is what remains. |
| Research Animal Facility Management | sibling shared-facility type | Same family — a shared institutional facility with per-user attribution and recharge-style billing — but the managed subject is animal colonies and husbandry, not instruments and services. |
| Research Administration Platform / Research Grant Management | adjacent domain | Grants administration manages the grant lifecycle (application, award, reporting). Here the fund is only a payment vehicle to be charged; facility reporting may support grant renewals but is not grants administration. |
| Enterprise Resource Scheduling Platform | generic neighbor | Generic resource scheduling lacks the research-facility semantics: qualification-gated instrument access, grant-funded payment, internal/external rate tiers. |
| Calibration Management / CMMS | overlapping module | Maintenance and calibration appear here as one ring of facility operations; the standalone types center on the asset/maintenance program itself. |

The most important boundary is with the Resource Calendar: both put calendars at the center of the user experience, and scheduling-first products of this type can look like resource calendars. The difference is the economic spine — rates, funding sources, financial approval, and recharge reporting exist here because the facility is a service operation that must recover its costs.

## Representative Products

- Agilent iLab Operations Software — the widely deployed academic core facility platform; storefront-and-fund model
- BookitLab (Prog4biz) — modular platform spanning scheduling, access control, requests, assets, and billing
- Stratocore PPMS — European-led platform with a price/subsidy-rule and project-centric spine
- Calpendo (Exprodo Software) — scheduling-first configurable system showing the calendar pole of the type

The defining core was checked against non-university operators (pharma, CROs, incubator shared labs) and against the paper-era practice (sign-up sheets, usage logbooks, recharge invoices) to avoid over-fitting the definition to the current university recharge implementation.

## Sources

Research date: **2026-09-09**

Primary official sources:

- Agilent iLab Help Site — https://help.ilab.agilent.com/ (Key iLab Terms glossary; Using a Core: Request Services, Schedule Equipment, Using Kiosk, Payment Methods)
- BookitLab — https://www.bookitlab.com/ (product and module pages)
- Stratocore PPMS — https://www.stratocore.com/ (home and features pages)
- Calpendo / Exprodo Software — https://calpendo.com/ (home and features pages)

> Sourcing limitations: the vendor's main marketing page for the leading product was not retrievable (HTTP 403); its official help site was used instead, which is the stronger source for operational structure. A fifth candidate product could not be reached and was dropped; no statement in this document depends on it. Precise vendor-specific figures (licence-tier limits, warning windows, approval thresholds) are intentionally not stated here; they remain in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-breadth check are recorded in the paired Research Notes.
