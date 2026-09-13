# Space & Occupancy Management

## Overview

A **Space & Occupancy Management** application is the occupying organization's system of record for its physical space inventory and for **who and what occupies each space** — maintained continuously as people are seated, teams are reallocated, departments expand and contract, and moves are executed.

The defining structure is small:

```text
Space inventory of record (site → building → floor → space)
└── Plan-anchored spatial representation (floor plans the inventory lives on)
    └── Occupancy state per space (organization allocations + person assignments)
        └── Recorded occupancy-changing operations (assignments, moves, reallocations)
```

Everything else commonly associated with the category — occupancy forecasting, block-and-stack scenario planning, utilization analytics, chargeback, employee "find my desk" services, sensor-fed measurement — is widespread in mature products but rides on top of this record; none of it defines the Type.

A note on naming: the market uses **"space & occupancy management"** and **"space management"** for the same systems. Vendors' own documentation treats occupancy as the managed content of space management — one leading suite describes its space module as providing "four areas of space and occupancy management" (inventory, chargeback, planning, occupancy), another titles its space management product as "complete visibility into space and occupancy," and a third defines space management as tracking allocations and "updating the occupancy" when people are assigned to spaces. No product was found that would satisfy one phrase and not the other. This document is written from the occupancy articulation of that single Type; the Space Management Platform record covers the same ground from the space-inventory articulation.

## Users & Context

The primary users are the people responsible for an organization's space as a managed resource:

- **Space planners and space managers** — maintain the inventory, allocate space to organizations, assign people to seats, and keep occupancy current. One enterprise product formalizes the split: the space manager tracks allocations, assignments, and utilization within a facility under space use agreements; the space planner monitors costs and utilization at the strategic portfolio level.
- **Department liaisons and business-unit administrators** — request space, confirm who sits where for their teams, and submit move requests.
- **Facilities and corporate real estate teams** — consume occupancy and utilization data for portfolio decisions: consolidate, expand, release, or reconfigure.

Secondary users:

- **Finance** — chargeback and occupancy-cost reporting (in organization-grain deployments).
- **HR and onboarding** — seating new hires, locating vacant seats, planning headcount against capacity.
- **Employees** — as consumers of the record: finding a person, a team, a bookable seat, or submitting a move request.

Typical contexts are organizations that occupy large, changing portfolios of space: corporate headquarters and campuses, government agencies, universities, healthcare systems. In these environments the space record is foundational — vendor documentation explicitly describes an accurate space inventory as the backbone that maintenance, reservations, and other facility applications build on.

## Core Model

### The defining core

**1. The space inventory of record.** The organization's occupiable spaces held as persistent, individually identified records — rooms, seats, workpoints — organized by location (site → building → floor → space) and carrying type, area, capacity, and classification. Non-occupiable areas (service areas, vertical penetrations) are commonly tracked as well, because area math depends on them. The inventory is durable and correcting: it outlives any single reorganization, and changes to it are recorded rather than overwritten.

**2. Plan-anchored spatial representation.** The inventory is bound to building and floor plans — through a native editor, linked CAD drawings, or BIM models — so that spaces are browsed, edited, highlighted, and reported *graphically*. Every sampled product manages space this way: the floor plan is the primary working surface, not a report illustration. Remove the spatial binding and what remains is a generic facilities database or a CAD viewer.

**3. Occupancy state per space.** The heart of the Type. Each space carries a managed occupancy state on two grains:

- **Organization grain** — the space is allocated to a department, division, or other organizational unit. This allocation is often the object of policy: who is accountable for the space, who is billed for it, and whether accountability persists when the space sits vacant.
- **Person grain** — individuals are assigned to spaces (a seat, an office), producing occupancy plans, headcounts, and person-to-seat ratios. One enterprise product treats the distinction explicitly, maintaining separate *occupancy allocations* (who actually occupies the space) from *chargeback allocations* (who pays for it), since the occupying and paying organizations can legitimately differ.

Beyond assigned and allocated, a space's occupancy state may be shared/team space, bookable/reservable, or vacant. The state answers the question the whole Type exists to answer: **who sits where, right now.**

**4. Recorded occupancy-changing operations.** Occupancy is kept *current* by recorded changes: seat assignments, employee moves, department claims and reallocations ("moves, adds, and changes"), and physical surveys/audits that reconcile the record with reality. In mature implementations these changes are stored as transactions — who changed what, when — so occupancy history is reconstructable and audits are answerable. Remove this leg and the system is a static snapshot of a reorganization rather than a living record.

```text
Organization                     Person
   │ allocated to                    │ assigned to
   ▼                                 ▼
Space record ── carried on ──► Floor plan (site → building → floor)
   │  occupancy state: allocated / assigned / shared / bookable / vacant
   ▼
Move / add / change recorded  ──►  occupancy updated, history kept
```

### What mature products add

The following are standard in the category's mature products but are capabilities over the record, not the record itself:

- **Occupancy planning** — building and comparing scenarios for future space needs: block-and-stack plans that place departmental requirements on floors, headcount forecasts, and the promotion of an approved scenario into executed moves.
- **Occupancy and utilization analytics** — occupancy rate, vacancy rate, density, seat ratios, utilization trends; benchmarking across buildings and over time; increasingly fed by booking, badge, and sensor data.
- **Chargeback** — internally billing departments for the space they occupy, including shares of common area; in organization-grain deployments (government, higher education) this is often the financial point of the whole record.
- **Employee-facing location services** — self-service "where is my desk / where is my team," people and room search on floor plans, move requests.
- **Field survey tooling** — mobile survey and audit apps used to verify the inventory and occupancy against physical walkthrough.

## How It Works

### Establish the record

```text
Import or draw floor plans
→ define the space hierarchy (site / building / floor)
→ create space records with type, area, capacity, classification
→ survey or audit against the physical building
```

In CAD-anchored deployments, floor-plan polylines are connected to database records; in native-editor deployments the plan is drawn directly in the product. Either way the result is the same object: a space inventory whose graphical and tabular views are the same data.

### Put the space into occupancy

```text
Allocate spaces to departments/organizations (organization grain)
→ assign people to seats (person grain)
→ mark shared / bookable / vacant states
→ record the assignment as a transaction
```

This is the routine maintenance loop of the Type. A new hire arrives (often pushed from HR data), is assigned to a seat, and the space's occupancy — headcount, ratio, vacancy figures — updates. A department claims rooms; the allocation record changes; chargeback targets move with it.

### Keep it current: moves, adds, changes

```text
Move request submitted (self-service or planner-initiated)
→ planner designs the move against the floor plan
→ move scheduled and executed
→ occupancy updated at both origin and destination
→ history retained
```

Move management is the operational engine that keeps the record honest: large relocations ("box moves" and team relocations alike) are planned on the same floor plans that hold the record, and execution updates occupancy at both ends. Without this loop, the occupancy state decays into fiction — which is why surveys and audits exist as a reconciliation backstop.

### Plan and decide

```text
Current occupancy + headcount forecast
→ build scenarios (block & stack; reconfigure floors; new/removed space)
→ compare scenarios (capacity, cost)
→ approved scenario promoted into the live plan
→ executed as moves
```

The planning loop is where occupancy becomes forward-looking: visualizing what the space and occupancy might look like months or years out, testing reorganizations before moving a single desk, and converting decisions into the move work that updates the record.

### Report and account

Occupancy rate, vacancy, density, assignment by occupant and by department, utilization trends — reported from the record for benchmarking, portfolio decisions, and (where chargeback exists) internal billing.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Floor-plan workspace (space console)

The primary working surface: interactive floor plans of every building and floor, with spaces color-coded or highlighted by department, occupancy state, space type, or vacancy.

- Typical information: space boundaries and areas, occupancy state, assignments, space types, capacity
- Primary actions: browse and search space and people, edit space records and boundaries, place or move assignments, highlight by department/occupancy, export and print plans

### Space record / allocation views

The record view for a single space (or a person): area, type, classification, allocations, assignments, occupancy status, transaction history.

- Primary actions: allocate to an organization, assign or unassign a person, adjust shared allocations, view occupancy details and history

### Move / MAC management

The queue and planning surface for moves, adds, and changes.

- Typical information: move requests, affected people and assets, origin and destination, dates, status
- Primary actions: submit/approve requests, design moves on the floor plan, schedule, execute, confirm occupancy updates

### Scenario / stack planning workspace

The planning surface for future states.

- Typical information: current floor stacks and head/seat counts, departmental requirements, draft scenarios
- Primary actions: create scenarios, block and stack requirements onto floors, compare, merge an approved scenario into the live plan

### Reports and dashboards

Occupancy rate, vacancy, utilization, headcounts, space by department and type, benchmarks by building; chargeback reports where applicable.

### Employee self-service

Search for a person, team, or room on a floor plan; "where is my desk/team"; move requests; desk/room booking in hybrid deployments.

### Field survey apps

Mobile tools for walking a floor and reconciling the physical space and its occupancy against the record.

## Important Rules / Behaviors

### Occupancy and financial responsibility are separable

A space's occupying organization and its paying organization can differ, and mature products model the two separately (occupancy allocations vs chargeback allocations). Departments may remain accountable — and chargeable — for space they have vacated. Treating "who occupies" and "who pays" as one field is a common implementation shortcut, not the model the category is built on.

### The inventory is the prerequisite

Occupancy, chargeback, maintenance, and reservations all read the same space inventory. Vendor documentation describes the room-level inventory as the backbone on which other facility applications depend; products therefore treat inventory accuracy (surveys, audits, transaction histories) as a governance concern, not housekeeping.

### Occupancy is two-grained

Organization-grain allocation and person-grain assignment are both first-class and must stay consistent with each other (a person's assignment typically infers their department's occupancy, by configurable policy). Reports that look similar (occupancy rate, headcount) can be computed at either grain; which grain is authoritative is a deployment decision.

### Changes are recorded, not overwritten

Assignments, moves, and claims are recorded as transactions with attribution, so occupancy has a history: who sat where, when, on whose authority. Field audits reconcile drift between record and reality.

### Space standards govern placement

Mature deployments configure space standards and placement policies (ratios, room types per function, fair-placement rules) that constrain what can be assigned where, making allocation a policy-governed act rather than free drawing.

## Variants

- **Suite module vs pure-play** — the most common packaging is as the space/occupancy domain of an integrated workplace management suite (alongside lease administration, maintenance, and capital projects); standalone space-and-occupancy products form the pure-play pole. The core record is the same in both.
- **Organization-grain estates** — government agencies and universities run the Type at department/fund grain with chargeback and formal space classification as central concerns.
- **Corporate hybrid estates** — free-address and neighborhood seating shift emphasis toward bookable states, employee self-service, and measured (sensor/badge) occupancy feeding utilization analytics; the allocation record remains the spine.
- **CAD-anchored vs native editing** — deployments anchored to CAD/BIM integrations vs products with built-in floor-plan editors (some adding 3D walkthroughs); a packaging axis, not a structural one.
- **Measurement-fed vs survey-fed** — occupancy data refreshed by walkthrough surveys and audits vs continuously fed by booking, badge, WiFi, and sensor signals.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Space Management Platform | same population (alias) | The market uses "space management" and "space & occupancy management" interchangeably for these systems; vendor documentation itself titles space-management modules as providing "space and occupancy management." One Type, two names. |
| Integrated Workplace Management System (IWMS) | module within a broader Type | Space & occupancy is one domain inside an IWMS, whose differentiator is the integrated multi-domain span (lease administration + space + facility operations) over one portfolio spine. |
| Facility Management System | adjacent | Centers on keeping the estate operating — service requests and planned maintenance work. It consumes the space inventory (which it treats as a prerequisite), rather than owning the occupancy record. |
| Workplace Management Platform / Office Operations Platform | adjacent | Centers on the employee-facing reservation and coordination surface and the workplace team's request/operations loop; here the center is the managed inventory and its occupancy record. A pure booking suite satisfies neither this Type's inventory-allocation legs nor its recorded-operations leg. |
| Amenity Booking Platform | adjacent | Time-bound reservations of shared amenities by a closed population vs the durable allocation and occupancy record of the whole estate. |
| Coworking / Flexible Workspace Management | opposite side of the wall | Operator-side management of a space-as-a-service business (memberships, billable units) vs the occupier organization's internal record of its own space. |
| Hotel PMS | different domain | Transient guest stays with folios and payments vs durable organizational allocation of owned/leased space. |
| Lease Administration | adjacent | Lease obligations, terms, and financials; reads space context from the estate but its record of record is the lease, not the space or its occupants. |
| Building Management System | different layer | Operates building plant (sensors, controllers, setpoints); this Type records places and the people and organizations occupying them. |
| Occupancy sensing / analytics products | upstream measurement layer | Sensor/analytics platforms measure how space is used and feed planning; they hold no inventory, no allocations, no move records. They are a data source for this Type, not a competing Type. |
| Architecture / CAD tools | different lifecycle stage | Authoring construction documents vs operating the occupied-space record built from them. |

## Representative Products

- IBM TRIRIGA (space & occupancy as a domain of the TRIRIGA suite)
- Archibus, an Eptura company (Space module — inventory, occupancy, chargeback, planning, moves)
- FM:Systems FM:Interact (space management, scenario planning, move management modules)
- OfficeSpace (pure-play space planning, MAC, and utilization platform)
- SpaceIQ / SiQ (pure-play space management, now part of Eptura)

The category has consolidated considerably (several named space-management vendors now sit under one workplace-technology group), but space & occupancy management remains a named product line within each consolidated portfolio.

## Sources

Research date: **2026-09-09**

- IBM TRIRIGA — Space and Move Management User Guide (v11.6): https://www.ibm.com/docs/en/SSFCZ3_11.6/pdf/pdf_tri_space_move_mng.pdf ; "Planning facilities, spaces, and moves": https://www.ibm.com/docs/en/tririga/11.6.0?topic=planning-facilities-spaces-moves ; "Occupancy Rate (%) metric": https://www.ibm.com/docs/en/tririga/11.5.0?topic=metrics-occupancy-rate-metric
- Archibus (Eptura) — Space Domain, Space Inventory, and Space module documentation: https://help.archibus.com/user_en/Content/sp_results/space_business_functions.htm , https://help.archibus.com/user_en/Subsystems/webc/Content/sp_results/space_inv_web.htm , https://help.archibus.com/user_en/Subsystems/webc/Content/sp_results/space_module.htm ; product pages: https://archibus.com/products/space-management
- FM:Systems — Space Management and Strategic Scenario Planning product pages; space-management best-practices guide: https://fmsystems.com/products/workplace-management-solutions/space-management , https://fmsystems.com/products/workplace-management-solutions/strategic-scenario-planning
- OfficeSpace — Space Management and Scenario Planning product pages: https://www.officespacesoftware.com/solutions/space-management , https://www.officespacesoftware.com/features/scenario-planning
- SpaceIQ (Eptura) — product/transition pages and feature syntheses: http://spaceiq.com/
- VergeSense — Occupancy Intelligence Platform pages (boundary comparison only): https://www.vergesense.com/occupancy-intelligence
- Customer operational documents (corroboration): State of Arizona GAO TRIRIGA Space Management manual; University of Queensland Archibus Space Management Manual; CFTC TRIRIGA privacy impact assessment.

> Sourcing limitation: OfficeSpace and SpaceIQ official help/knowledge centers were not reachable from the research environment on 2026-09-09; evidence for those two products is limited to official product pages and third-party feature listings, and claims involving them are calibrated accordingly. The alias determination between "space & occupancy management" and "space management" rests on the fully documented products (TRIRIGA, Archibus, FM:Systems). Detailed product-by-product evidence, the cross-product comparison matrix, and vendor-specific details are recorded in the paired Research Notes.
