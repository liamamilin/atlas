# Campus Housing Management

## Overview

A **Campus Housing Management** application is the institution-side system of record for running a college's or university's student housing: it holds the residential space inventory, manages how students apply for and are assigned to specific rooms for an academic period, tracks who is actually living where, and carries the surrounding operations — room changes, check-in and check-out, condition and damage records, housing charges, and the day-to-day work of residence-life staff.

The defining structure is small:

```text
Institution-held space inventory (rooms/beds organized by hall/building)
  + resident = identified member of the institution's population (normally a student)
  → assignment (specific resident × specific space × defined period)
  → occupancy state (who is assigned, who is in residence, what is vacant)
```

Everything else commonly associated with the category — self-service room selection, roommate matching, portals, meal-plan linkage, residence-life programming, conference housing — is standard capability layered around that core, and different products include different amounts of it. The Type is best understood as **administratively governed allocation of institution-owned rooms to institution-affiliated people**, which is what separates it from commercial rental property management (lease with a tenant) and from hotel management (transient stay with a folio).

When the resident population becomes an anonymous market of tenants with individually negotiated leases, the software has become property management; when stays become short, guest-centered, and folio-driven, it has become a hotel system (see Related Application Types).

## Users & Context

Primary users are the staff of the campus unit that runs housing — commonly a housing, residence life, or residential operations office:

- **Housing/assignment staff** run the occupancy machinery: publish the application, run room selection, make and adjust assignments, process room-change and swap requests, and answer "who is in which bed" questions. Occupancy is their central working object.
- **Residence-life staff** (area coordinators, hall directors, resident assistants) work inside the buildings: duty logs and rounds, programming and attendance, roommate conflict mediation, wellness check-ins, incident and concern reports, guest approvals.
- **Operations staff** handle the physical layer at scale: check-in/check-out of hundreds of residents, keys, room condition reports and inspections, maintenance handoff, and in some products package and front-desk services.

Secondary participants:

- **Students** are first-class actors through the resident portal: they apply, join roommate groups or search for roommates, pick rooms during selection windows, accept assignment offers, request room changes or break/holiday stays, submit maintenance requests, and complete room condition reports.
- **Campus partner offices** are structurally connected rather than seated: the registrar/student-records system (eligibility and student data), student billing (charges), campus card/dining (meal plans), and facilities or public safety (access control).

The context is fundamentally cyclical: the annual academic cycle (new-year applications and selection, summer turn-over and conference use, fall move-in, in-term changes, end-of-year move-out) drives most of the work, with continuous operations layered on top.

## Core Model

### The Defining Core

**Space inventory.** The institution's residential stock is modeled as individually assignable spaces — rooms or beds — organized in a hierarchy (building/hall → floor or wing → room → bed/space). Each space carries its capacity and attributes that selection and assignment rules read (room type, gender designation, rate class, and similar configuration). This inventory is the anchor: everything else refers to it.

**Resident.** The occupant record is a member of the institution's administered population, normally a student whose identity and eligibility can be matched against the student system. This is not an anonymous tenant: the person comes with institutional context (enrollment status, classification, and any housing-relevant accommodations), and eligibility to live in residence is typically derived from institutional standing rather than negotiated.

**Assignment.** The assignment is the central object: a binding of one resident to one space for a defined period — normally an academic year or term. It is created by a governed process (housing-office placement or student self-selection through a managed window), confirmed by an offer/acceptance step, and it is the administrative instrument of occupancy. Assignments can be changed (room changes, swaps, consolidations), which is a normal in-term workflow rather than an exception.

**Occupancy state.** The system continuously knows which spaces are filled or vacant and who is currently in residence — distinct from who is merely *assigned*. Check-in turns an assignment into physical presence; check-out (with condition inspection) closes it. Occupancy counts and bed fill are the numbers the office runs on.

### Standard Capabilities Around the Core

Mature products commonly add:

- **Housing applications** — configurable forms with questions that vary by applicant type (new vs. returning), collecting preferences, lifestyle and matching answers, emergency contacts, and required agreements.
- **Room selection** — a self-service window in which eligible students, in an ordered sequence (by selection time or similar mechanism), see real-time availability and pick their room, typically as part of a roommate group; housing offices can equally place students directly.
- **Roommate coordination** — matching questionnaires, roommate search and request mechanics (sometimes with a private social layer), roommate groups that pick rooms together, compatibility views for staff, and tracked roommate agreements that residence-life staff manage.
- **Offer/acceptance and contracts** — a placed student receives an offer to accept, which reduces no-shows; acceptance may involve signing a housing contract or license agreement.
- **Room changes and swaps** — student-initiated requests with staff approval, staff-side room-swap and comparison tooling, and direct assignment edits.
- **Check-in/check-out and period exceptions** — arrival processing (keys/access, identity confirmation), early-arrival and late-stay handling, break and holiday stays, move-out with room condition reports and damage recording.
- **Housing billing** — charge calculation and payment schedules per assignment, pro-rating and billing cycles, and handoff to the student account or ERP; financial-aid alignment in some implementations.
- **Residence-life operations** — staff role structures, duty logs and weekly reports, programming/event records with attendance, 1-on-1 interaction records, roommate conflict mediation, students-of-concern tracking, and guest/visitor logging.
- **Reporting** — occupancy, bed fill, retention/return rates, assignment activity, and financial views; user-definable reports and dashboards.
- **Integrations** — student information system (data in; assignments and charges out), payment processors, single sign-on, access control, and meal-plan linkage.
- **Resident portal and communications** — the student-facing surface for the whole lifecycle, plus targeted email/message tooling.

### One Structure, Many Implementations

The core is written conceptually; products realize it differently:

```text
Concept:   Assignable space unit
Implementations:  bed, room, suite/apartment space; configurable per hall

Concept:   Governed allocation of a space
Implementations:  housing-office placement, ordered self-selection,
                  application-based matching by staff

Concept:   Confirmation instrument
Implementations:  offer acceptance, signed housing contract/license agreement

Concept:   Period of occupancy
Implementations:  academic year, single term, custom session
                  (summer/conference sessions as variants)
```

## How It Works

### The annual assignment cycle

```text
Configure the year's inventory and rates
→ open housing applications (eligibility checked against student standing)
→ roommate groups form (matching questions, requests, social search)
→ room selection runs in ordered windows (students pick real-time-available rooms)
   and/or staff place applicants
→ assignments confirmed via offer/acceptance and contract signing
→ charges scheduled to the student account
→ move-in: check-in, keys/access, condition baseline
```

This cycle is the system's defining rhythm. Everything before move-in exists to produce a full, conflict-free set of assignments against the inventory.

### In-residence operations

```text
Resident or staff event occurs
  (room change request, maintenance issue, program, incident, concern, guest)
→ recorded against the resident and/or the space
→ routed to the responsible staff role
→ resolved and kept on the resident's and building's record
```

Residence-life staff work from the live occupancy picture: who is in which room, what interactions and incidents are on record, which programs ran and who attended, which concerns are open.

### Continuous adjustment

```text
Assignment pressure appears (no-show, cancellation, room conflict, capacity gap)
→ room changes, swaps, consolidations, or waitlist-style reallocation
→ inventory and occupancy state updated in real time
→ billing adjusted where the assignment changed
```

### Core vs Common vs Optional

**Defining core** — without these, not campus housing management:

- space inventory with assignable units
- resident as institution-population member
- assignment of resident × space × period
- occupancy state

**Standard capabilities** — present in most modern products:

- applications, room selection, roommate matching, offers/contracts
- room changes, check-in/out, break/early/late housing
- room condition reports and damage records
- housing billing and student-account handoff
- residence-life operations (staff duty, programming, concerns, guests)
- SIS/billing/payment/SSO integrations, reporting, resident portal

**Variant / optional** — depends on institution and packaging:

- deep meal-plan administration, conference/summer event housing
- student-staff (RA) recruitment and hiring
- front desk, packages/mailroom, key inventory, access-control hardware integration
- living-learning communities and residential-curriculum tooling
- operator/PBSA lease-flavored deployments, boarding schools, staff housing

## Interfaces

### Assignments / occupancy console (staff)

The operations center.

- information: building → room → bed tree, current assignments, real-time availability, applicant queues
- primary actions: place or reassign a student, run or monitor selection, process room changes and swaps, check residents in or out

### Student portal (resident)

The self-service surface across the whole lifecycle.

- information: application status, current assignment and roommates, offers, charges, requests
- primary actions: apply, form/join a roommate group or search roommates, pick a room in a selection window, accept an offer, request a change or break stay, submit a maintenance request, complete a room condition report

### Residence-life workspace (staff in the buildings)

- information: roster by floor/hall, duty schedules, interaction and incident history per resident, open concerns, program calendar and attendance
- primary actions: log an interaction, incident, or concern; record duty rounds; track programs; approve guests; manage roommate agreements

### Condition and inspection surfaces

- information: room condition reports per space, inspection checklists, damage records, work-order status
- primary actions: conduct check-in/check-out inspections, record damage, open and track maintenance items

### Reporting and dashboards

- information: occupancy and bed-fill views, application/selection progress, retention, financial summaries
- primary actions: configure reports, monitor selection windows, export to campus systems

## Important Rules / Behaviors

### An assignment governs occupancy, not a lease

The resident's right to occupy flows from an institutional assignment (application → selection/placement → acceptance), not from a commercially negotiated lease. Changing occupancy is an administrative act inside the system, which is why room changes are a routine workflow rather than a contract renegotiation.

### Eligibility derives from institutional standing

Who may apply and hold an assignment is determined by institutional criteria (enrollment and standing, and policy rules such as live-on requirements or room- and hall-eligibility policies). The housing system applies these rules at application and selection time.

### One resident per assignable unit

Inventory capacity is enforced: a bed holds one assignment at a time. Selection shows only genuinely available spaces, and staff-side assignment tools respect the same constraint. Exact modeling (bed-level vs room-level units) varies by product and configuration.

### Assignment and physical presence are distinct states

A confirmed assignment is not yet occupancy. Check-in (with keys/access and condition baseline) establishes presence; no-shows are a managed outcome — hence the offer/acceptance step that mature products use to reduce them. Early arrivals, late stays, and break-period occupancy are tracked as exceptions to the normal period.

### Room changes are mediated

Students typically request changes; staff approve and execute them through swap and comparison tooling. Roommate relationships, gender/policy designations of spaces, and capacity are the constraints the mediation respects.

### Charges follow the assignment lifecycle

Housing charges, pro-rating, and adjustments are driven by the assignment (its space's rate class, its period, and its changes), and are handed to the student account rather than collected as standalone rent in most institution deployments.

### The occupancy picture must be true at all times

The live roster ("who is on campus right now") is a working requirement — used for duty coverage, guest policy, emergencies and duty-of-care situations, and is why real-time check-in state is treated as an operational fact, not a report.

### Incident logging lives here; adjudication usually does not

Residence-life staff record incidents, concerns, and conflicts inside the housing system, but the formal conduct case process (hearings, sanctions) is commonly a separate system fed by those records.

## Variants

- **Large research university (housing + residence life at scale)** — full inventory across many halls, multi-window selection, large RA staff structures, deep reporting; often the fullest platform deployments.
- **Small college / small institution packaging** — same lifecycle with lighter configuration; vendors commonly package by bed count and staff structure.
- **Suite-module deployments** — housing selection and assignment handled by a focused module inside a broader student-affairs suite, with residence-life breadth reduced and conduct handled by sibling products.
- **Conference / summer housing** — the same inventory let to non-student populations for short sessions; inquiry-to-billing guest workflows layered onto the core.
- **Purpose-built student accommodation (PBSA) / commercial operator** — the same structures operated lease-flavored by a housing provider rather than the institution; contract and payment mechanics resemble tenancy, while inventory/assignment/occupancy logic is retained.
- **Boarding schools and staff housing** — population and period rules change (school terms, employees), the assignment core does not.
- **Policy-flavored configurations** — gender-inclusive housing, living-learning communities, and accommodation-driven placement are policy layers over selection and assignment rather than separate structures.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Residential Property Management | commercial landlord software: lease negotiation with a tenant, market rent, no institutional population or residence-life layer |
| Student Housing Management | same object world from the housing-operator vantage; treated as a sibling leaf — the boundary (institution housing office vs commercial operator) deserves joint review |
| Hotel Property Management System | transient guests with folio-and-payment at the center and housekeeping-driven room state; campus housing is term-length assignment of institution members billed to the student account |
| Student Information System | owns the student record and academic standing; housing consumes eligibility and returns assignment/billing data |
| Student Billing System | collects the charges the housing system schedules; it does not manage space or assignment |
| Campus Card Management | owns credentials and entitlements (card, meal-plan accounting, door access); housing links to meal plans and access but does not run the credential lifecycle |
| Student Behavior / Conduct Management | adjudicates conduct cases; the housing system logs incidents and concerns from residence-life staff and feeds them |
| Student Services Portal | student-facing portal surfaces are interfaces of this system, not a separate housing Type |
| Affordable Housing Management | also eligibility-governed occupancy, but governed by housing-program rules (income/certification) rather than institutional enrollment and housing contracts |
| Event / Conference housing tools | short-stay guest management over borrowed inventory; a variant module here, a standalone Type only when events are the primary business |

The most consequential boundary is with **Residential Property Management**: both manage rooms and money, but in campus housing the occupancy instrument is a governed assignment for an institution-population member on an academic cycle — remove that and the software collapses into generic property management.

## Representative Products

- StarRez
- eRezLife
- Symplicity Residence
- The Housing Director (Adirondack Solutions, now part of StarRez) — included as the historical-generation sample

The core model was checked against the historical sample (a 1998-generation housing product) and against lighter suite-module deployments to avoid over-fitting the definition to the modern portal-and-selection experience.

## Sources

Research date: **2026-09-06**

- StarRez — platform overview: https://www.starrez.com/
- StarRez — Higher Education solution: https://www.starrez.com/solutions/higher-education
- StarRez — Room & Roommate Solution: https://www.starrez.com/solutions/room-and-roommate-solution
- StarRez — The Housing Director hub: https://www.starrez.com/company/the-housing-director
- Adirondack Solutions — home: https://www.adirondacksolutions.com/
- eRezLife — home: https://erezlife.com/
- eRezLife — Assignments: https://erezlife.com/assignments/
- eRezLife — Residence Life: https://erezlife.com/residence-life/
- Symplicity — Residence: https://www.symplicity.com/higher-ed/solutions/residence

> Sourcing limitation: evidence rests on official product and solution pages. Vendor help-center depth was not reachable from the research environment on 2026-09-06 (Roompact blocked after repeated attempts; The Housing Director knowledge base and StarRez support portal require login). Operational specifics — exact unit modeling, selection-ordering defaults, state names, numeric limits, pricing — are therefore intentionally not asserted; behavioral descriptions are calibrated to the product-page evidence, and claims supported by fewer than two products are kept qualified. Detailed observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
