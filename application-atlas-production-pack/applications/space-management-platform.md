# Space Management Platform

## Overview

A **Space Management Platform** is an organization-facing system of record for the organization's own physical space inventory. It maintains structured, individually identified records of the spaces an organization occupies — sites, buildings, floors, rooms, desks — anchored to floor plans; tracks the allocation and occupancy state of every space (who sits where, what is allocated to which department, what is bookable, what is vacant); and executes space-changing operations — seat assignments, moves, re-allocations, and bookings — as recorded changes against that inventory.

The problem it solves: as people, teams, and headcount constantly change, an organization's footprint drifts out of alignment with its actual structure. Facilities teams otherwise track this in disconnected spreadsheets, outdated drawings, and manual walkthrough audits. The platform gives space planners, corporate real estate, and facilities teams one maintained picture of what space exists, how it is categorized, who occupies it, and how it is actually used — so that reorganizations, growth, contraction, and portfolio decisions are made and executed against current facts.

The canonical boundary: the platform is **occupant-organization-side**. It serves the organization that occupies and manages space, not the landlord, not the hospitality operator, and not the design team that produces construction drawings. Its world is the occupied space inventory and the organization-to-space map — not financial lease records, not building maintenance, and not reservations alone.

## Users & Context

Primary users are the people whose job is the organization's space:

- **Space planners / space managers** — maintain the inventory and floor plans, allocate space to departments and teams, run block-and-stack and scenario planning, prepare and execute moves.
- **Facilities managers** — consume the same record for day-to-day operations, coordinate moves and seating changes, and answer "who and what is where" questions.
- **Corporate real estate / portfolio managers** — work at site, building, and portfolio level: capacity versus headcount, utilization, cost, consolidation and right-sizing decisions.

Secondary users interact with the same record through narrower surfaces:

- **Department managers and liaisons** — request space, review allocations for their teams, in some products make seating changes for their own groups.
- **Employees** — find and book desks or rooms, see who is in and where colleagues sit, submit move requests or location changes.
- **Move stakeholders** — IT, HR, movers, and employees receiving move instructions for a planned relocation.
- **Executives** — portfolio dashboards and reports for decisions about footprint and cost.

Typical context is any organization with a sizable multi-room, multi-floor, or multi-site footprint where allocation matters: corporate offices above all, and also government agencies, healthcare estates, and universities — anywhere a central team must govern how an organization occupies space.

## Core Model

The defining core is small: four structures that jointly make the application what it is.

```text
Space inventory of record
  (site → building → floor → spaces/seats, with types & attributes)
  └── anchored to floor plans
      └── carrying allocation & occupancy state per space
          (assigned / allocated / bookable / shared / vacant)
          └── changed by recorded space operations
              (assignments, moves, re-allocations, bookings)
```

### 1. The space inventory of record

A persistent registry of the organization's physical spaces. Every space is individually identified and carries a type (office, work point/desk, meeting room, kitchen, collaborative area, and so on) and attributes such as capacity, area, and category. The inventory is organized spatially and hierarchically — a site or campus contains buildings, a building contains floors, a floor contains spaces and seats. This is comprehensive: not just bookable rooms but every space the organization manages, down to individual seats. The registry is the anchor to which everything else in the platform refers.

### 2. The floor plan as the spatial anchor

The inventory is bound to a spatial representation of the physical layout. In modern products this is an interactive floor plan — spaces drawn on a building floor, browsable and editable in place. In older and CAD-integrated products the plan is a drawing maintained in external design tools and linked bi-directionally to the records; BIM building models play the same role in construction-heavy estates. The plan is not decoration: it is the primary surface through which the inventory is viewed, edited, and reported. The geometry and the records are two views of one thing — move a space on the plan and its record changes; change the record and the plan reflects it.

### 3. Allocation and occupancy state on every space

Each space carries managed state binding it to the organization — the maintained map between the organization and its space. The conceptual states:

- **Assigned** — bound to a specific person (a fixed seat).
- **Allocated** — bound to a group: a department, a team, a project team, or a named zone/neighborhood that aggregates seats for flexible use.
- **Bookable** — open for employees to reserve for a time (the hoteling/hot-desking end of the spectrum).
- **Shared / secondary** — bound to a person only part of the time or as a secondary seat.
- **Vacant / unallocated** — no current binding.

Products differ in the exact vocabulary and in how many distinct seat types they support, but the underlying idea — every seat sits somewhere on the assigned-to-bookable spectrum, and the current binding is recorded and editable — is what makes the platform a management system rather than a drawing.

### 4. Space-changing operations recorded against the inventory

The platform is not a snapshot; it is where space changes happen. Operations change the allocation state and are recorded:

- **Seat assignment changes** — placing, moving, or unseating people directly on the plan.
- **Moves** — planned relocations of people or whole teams (the "moves, adds, and changes" discipline), from request through execution to history.
- **Re-allocations** — redistributing blocks of space between departments, floors, or buildings.
- **Bookings** — temporal claims on bookable spaces, layered over the standing allocation.

### One structure, many implementations

The core model is conceptual; products realize each part differently:

```text
Concept:              Spatial anchor
Implementations:      interactive floor-plan editor, linked CAD drawings,
                      BIM building models

Concept:              Allocation target
Implementations:      person, department, team, project team, neighborhood/zone,
                      workplace group

Concept:              Usage state of a seat
Implementations:      reserved/fixed, shared, secondary, hot desk, hoteling
                      (exact vocabularies vary by product)

Concept:              Org data feeding allocation
Implementations:      HRIS sync (headcount, new hires, terminations), directory
                      sync, bulk imports, manual assignment

Concept:              Occupancy signal for reporting
Implementations:      bookings, check-ins, badge/access data, workplace sensors
```

### Standard capabilities of mature products

These are widespread in current products but are not what makes the platform a space management platform — older and simpler products in the lineage operate without them:

- **Scenario and stack planning** — visual "block and stack" views of how departments occupy floors and buildings, drag-and-drop re-stacking, unlimited what-if scenarios, headcount projections by department, floor, or building.
- **Move management machinery** — move plans distinct from executed moves, alternative plans, approval workflows, automated move-day communications, move instructions for IT/HR/facilities/movers, move history and reports.
- **Employee booking surfaces** — desk and room reservation for employees, recurring bookings, booking on behalf of others, check-in, kiosk and mobile access.
- **Utilization and occupancy analytics** — dashboards and reports combining bookings, check-ins, badge data, and (in some deployments) sensor data; under-used-space identification; attendance trends.
- **Cost and portfolio surfaces** — space cost and chargeback views, lease and portfolio reporting in some products.
- **Roles and permissions** — planner/admin vs. employee vs. department-liaison capabilities, with single sign-on typical.
- **Org-system integrations** — HRIS, calendars, directories, and access-control systems as data sources and booking surfaces.

## How It Works

The platform's life runs through several loops, of which the first three are the defining workflow.

### Build and maintain the inventory

```text
Obtain the floor plan (draw in the editor, import CAD/BIM drawings,
or link to external design tools)
→ define spaces and seats on the plan
→ set space types, codes/numbers, and attributes (capacity, area)
→ keep in step with the physical world as spaces change
```

The plan and the records stay synchronized: space types, seat counts, and labels live on the geometry itself, and space-type tags drive later behavior (what can be assigned, what can be booked).

### Allocate space to the organization

```text
Assign people to seats (individually or in bulk; often drag-and-drop on the plan)
→ allocate blocks of seats to departments, teams, or neighborhoods
→ mark remaining seats bookable, shared, or vacant
→ keep the map current as the organization changes
```

Allocation accuracy depends on organization data: HR-system syncs feed new hires and terminations into seating queues, and directory records attach people to seats. This is why the platform sits next to HR and directory systems rather than replacing them.

### Plan and execute change

```text
Plan:     build stack plans and scenarios against current occupancy and
          projected headcount — which teams go where, on which floor, in which building
→ compare alternatives, share with stakeholders, decide
Execute:  turn the decision into move plans
→ route move requests for approval
→ issue move instructions (dates, schedules, to-do steps) to IT, HR,
  facilities, movers, and affected employees
→ apply the committed moves: seats and allocations update on the plan
→ retain move history as part of the record
```

Moves range from one-off seat changes ("this person moves next week") to whole-floor relocations. The mature pattern separates the *plan* (draftable, comparable, duplicable) from the *executed change* (committed, applied, historicized) — so the inventory reflects what is true, while plans hold what is proposed.

### Operate day to day

Employees book bookable desks and rooms for specific times, check in on arrival, and find colleagues — all as temporal claims layered over the standing allocation. A booking consumes a space for a window; it does not change its allocation.

### Observe and report

Utilization and occupancy are computed from the record and its signals — bookings and check-ins, badge/access events, and in some deployments sensor data — and reported at seat, floor, building, and portfolio level: headcount versus capacity, under-used areas, attendance trends, space cost. These reports close the loop back into planning.

### Capability tiers

**Defining core** — without these the product is not a space management platform:

- structured, individually identified space inventory
- floor-plan anchoring of the inventory
- allocation/occupancy state per space
- recorded space-changing operations

**Standard in mature products:**

- scenario/stack planning and projections
- move-plan vs. executed-move machinery with approvals and communications
- employee booking and check-in surfaces
- utilization/occupancy analytics
- roles and permissions; HRIS/calendar/directory integrations

**Optional / dependent on segment and scale:**

- sensor-based real-time occupancy
- CAD/BIM bi-directional integration
- chargeback and lease/portfolio cost depth
- government-grade compliance postures
- AI layout suggestions and forecasting assistance

## Interfaces

Described conceptually; layouts and names vary by product.

### Floor plan / map view

The platform's center of gravity.

- Purpose: see and edit the space inventory and its occupancy in place.
- Typical information: spaces and seats drawn on the floor, color-coded by allocation, department, or usage state; search across people, spaces, and floors; filters by location, department, or space type.
- Primary actions: select seats, assign/unseat/move people, change a space's type or usage state, add or edit spaces and icons (rooms, points of interest, furniture), drill between buildings and floors.

### Stack / scenario planning view

- Purpose: plan space at department-to-floor-to-building granularity.
- Typical information: departments stacked by floor and building with seat counts, occupancy, and capacity; headcount projections.
- Primary actions: drag departments between floors/buildings, adjust seat allocations, create and compare alternative scenarios, export or share a plan.

### Move console

- Purpose: turn space decisions into executed relocations.
- Typical information: move plans and their status, move requests awaiting approval, affected people and their from/to seats, dates and schedules, instruction recipients.
- Primary actions: create/duplicate/compare plans, approve requests, schedule or reschedule, send move communications, complete moves, review move history.

### Employee booking surface (web, mobile, kiosk)

- Purpose: let employees occupy bookable space.
- Typical information: floor maps with availability, who is in and where, desk and room details, one's own upcoming bookings.
- Primary actions: search and filter bookable spaces, book/edit/cancel, check in, find a colleague, submit a location-change or facility request in some products.

### Portfolio dashboard and reports

- Purpose: management-level view of the estate.
- Typical information: portfolio/map overview of sites, occupancy and utilization trends, capacity versus headcount, space cost.
- Primary actions: filter, drill down, generate and share reports, export data.

### Administration and settings

- Purpose: govern the system.
- Typical information: roles and permissions, space types and usage-type vocabularies, booking policies, integration configuration (HRIS, calendars, directories, CAD/BIM sources).
- Primary actions: manage users and roles, configure space types and policies, set up data syncs and imports.

## Important Rules / Behaviors

### Allocation and booking are different layers

Allocation is the standing state of a space (who or what it belongs to, or that it is bookable). Booking is a temporal claim on a bookable space that leaves the standing allocation untouched. A desk can be allocated to a team's neighborhood yet booked by an individual for Tuesday. Conflating the two is the most common conceptual error when approaching this software.

### The inventory is the record of truth

Every operation — a seat assignment, a committed move, a booking — updates the same underlying record. This is deliberate: the alternative, spreadsheets and drawings edited separately, is what the category exists to replace. Move history, assignment history, and (in some products) plan versions are retained, so past states of "who sat where" remain answerable.

### Moves are planned, approved, and batched

A move is typically a planned, reviewable change rather than a silent edit: plans are drafted, alternatives compared, requests approved, instructions issued, and only then is the change applied to the record. Conflict detection (target seats already occupied, overlapping moves) belongs at planning time.

### Organization data drives allocation currency

New hires, terminations, and department changes flow in from HR and directory systems and become work queues (seat someone, unseat someone). An allocation layer fed by stale organization data loses trust quickly; the HRIS/directory integration is therefore structural, not incidental.

### Space types determine behavior

Whether a space can be assigned, booked, or both; what booking rules and limits apply; how it is colored and reported — all follow from the space's type and usage-state classification. Space-type taxonomies are product-specific and organization-configurable.

### Roles gate the geometry

Editing floor plans and allocations is planner/admin capability; employees book and view; department liaisons may hold intermediate rights over their own areas. Viewing "who sits where" is a privacy-relevant capability and is commonly permissioned.

### Geometry and records must not drift

Where the plan lives in external design tools (CAD/BIM), the platform maintains a deliberate link — in some products bi-directional — because a plan that disagrees with the inventory silently invalidates both. Native plan editors remove the boundary problem by making drawing and recording one act.

## Variants

- **Pure-play platform vs. named module.** Space management exists both as standalone products and as a clearly named product line inside broader workplace platforms and IWMS suites. The core discipline is the same; packaging differs.
- **CAD/BIM-integrated vs. native-editor.** Estates whose plans are authoritative in external design tools integrate those sources; products with native editors treat the plan as authored in-product. Both postures occur in the same market, sometimes in the same vendor family.
- **Fully-assigned estates vs. hybrid/free-address.** Traditional deployments assign nearly every seat; hybrid-work deployments keep a smaller assigned core and push most seats into bookable/neighborhood modes. The platform supports both; the allocation-state vocabulary absorbs the difference.
- **Segment scoping.** Corporate offices dominate, but the same structure serves government portfolios (with chargeback and compliance emphasis), healthcare estates, and universities — differing in space-type vocabularies and cost machinery, not in the core model.
- **Planner-first vs. booking-first packaging.** Some products lead with planning and moves (facilities/CRE posture); newer workplace-experience products lead with employee booking and analytics while carrying the same inventory/allocation spine underneath.
- **Deployment.** Cloud SaaS is the current default; on-premise and government-authorized deployments persist for regulated organizations.

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| Space & Occupancy Management | likely the same Type under another label | market vendors use "space and occupancy" and "space management" interchangeably for this discipline; the directory keeps both leaves — joint review recommended |
| Integrated Workplace Management System / IWMS | broader suite | bundles this Type with facility maintenance, asset management, lease, projects, and sustainability; space management is the space-domain module inside it |
| Workplace Management Platform | adjacent sibling | centers employee experience and workplace operations (booking, visitors, service requests, announcements); the space inventory/allocation discipline is this Type's center |
| Facility Management System | adjacent | centers building operations and maintenance (work orders, PM); space management centers the inventory and allocation record; commonly co-exist as product lines |
| Resource Calendar / Desk & Room Booking | narrower, contained | manages temporal reservations of bookable resources; lacks the comprehensive inventory, allocation layer, planning, and moves; in mature platforms booking is a surface over this Type's inventory |
| Enterprise Asset Registry | distinct object | records movable assets with custody flows; spaces are places; asset modules attach to space platforms but the space record is the anchor |
| Coworking / Flexible Workspace Management | different side of the desk | operator-side commercial business (memberships, billing, member CRM) vs. occupant-organization-side planning and allocation |
| Hotel PMS | different domain | transient hospitality stays (reservation/stay/folio) vs. organizational space allocation |
| Architecture Design / CAD applications | upstream | author building designs and construction documents; this Type imports and operates on the resulting geometry for an occupied building |
| Lease Administration | adjacent financial record | centers the lease obligation; space platforms carry lease/portfolio-cost surfaces but their defining record is the space |

## Representative Products

- OfficeSpace Software
- SpaceIQ / SiQ (now part of Eptura)
- FM:Systems (FM:Interact, now part of Johnson Controls)
- Archibus (now Eptura Archibus)
- Robin

The core model was checked against the older CAD-integrated lineage (Archibus, FM:Interact) and against pre-software practice (paper floor plans with manual allocation registers and walkthrough audits) to avoid defining the Type by the current hybrid-work-era packaging.

## Sources

Research date: **2026-09-08**

- OfficeSpace Software — home, Block & Stack Planning, and Move Management pages: https://www.officespacesoftware.com/ , https://www.officespacesoftware.com/features/stack-plans/ , https://www.officespacesoftware.com/features/move-management/
- SpaceIQ (Eptura) — Knowledge Center (admin, employee, planning, move-order, floor-map documentation): https://knowledge.eptura.com/SiQ ; migration page: https://spaceiq.com/
- FM:Systems — home and Space Management product page: https://fmsystems.com/ , https://fmsystems.com/products/workplace-management-solutions/space-management/
- Eptura / Archibus — platform and Archibus product pages: https://eptura.com/ , https://eptura.com/our-platform/archibus/
- Robin — home and Space Management page: https://robinpowered.com/ , https://robinpowered.com/platform/space-management

> Sourcing limitation: the help centers of OfficeSpace and Robin could not be fetched from the research environment (one failed render and one transport error respectively), and Archibus's own documentation site was not reachable (404 on the legacy domain). Observations for those products rest on their official product pages; only the SpaceIQ knowledge center provided Tier-1 operational documentation. Accordingly, this document states no precise numeric limits, default settings, or time windows for any product, and cross-product claims are calibrated to what the reachable sources jointly support. Detailed product-by-product evidence is in the paired Research Notes.
