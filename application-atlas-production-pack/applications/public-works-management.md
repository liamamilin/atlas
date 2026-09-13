# Public Works Management

## Overview

A **Public Works Management** application is a public-works department's operational system for its service delivery: it receives and triages requests for service from the public and staff, turns them into crew-executed work orders, and records that work — with its labor, equipment, materials, and costs — against the public estate the department maintains.

The defining structure is small:

```text
Service request (recorded, located demand for service)
  ↓ triage / convert
Crew work order (assigned, scheduled, executed, closed with costs)
  ↓ attached to
Maintained public estate (streets, signs, lights, storm drains,
grounds, facilities, fleet — the department's domains of work)
  ↓ reported as
Service performance and cost visible to the public and the budget process
```

Everything else commonly associated with these products — GIS mapping, citizen self-service portals, capital-planning analytics, FEMA cost reporting, seasonal snow programs — is widespread in current products or standard in certain regions, but is not what makes the application what it is. A department running the loop above on paper or on a 1990s work-order system was still doing public works management.

When the center shifts to the estate's own stewardship record (condition, renewal outlook, long-term plans), the product is drifting toward Public Asset Management. When it stays at the intake venue with a complaint lifecycle and no work execution, it is a citizen-request (311) platform.

## Users & Context

The operator is a public agency — typically a municipal department of public works (DPW), a county road/operations department, or a combined municipal operations unit. The department's defining condition is that it performs work **in public space, on behalf of the public**: potholes, broken street lights, clogged storm drains, damaged signs, downed trees, snow, fleet upkeep, and public building maintenance all arrive as requests from residents or staff and are resolved by the department's own crews.

Primary users:

- **operations coordinator / dispatcher / clerk** — receives and triages requests, creates and assigns work orders, answers "what's the status of my pothole," runs reports
- **crew members and crew leaders** — see their assigned work, navigate to locations, perform and close work in the field, record time, equipment, and materials used
- **field supervisor / superintendent** — schedules crews, balances workload and backlog, handles exceptions and emergencies
- **department director** — watches performance and costs, justifies budgets and staffing to council

Secondary users:

- **residents** — report issues and follow their request's status through a portal or by phone
- **finance / administration** — consume cost and activity data for budgeting, grants, and (in the US) disaster-cost recovery

The work environment is split between an office (triage, assignment, reporting) and the field (crews in vehicles, at locations across the jurisdiction), with the mobile connection between them being one of the application's most important affordances.

## Core Model

### The defining core

**Service request.** A request for public-works service is the unit of demand. It records what was reported (a pothole, a dead street light, a missed collection, a damaged sign), where it is (an address, a map pin, or coordinates), who reported it (citizen contact details, or an internal requester), and commonly a photo. Requests arrive through a public portal, by phone taken down by staff, or are raised by employees who spot issues in the field. A request is triaged and prioritized; its status is visible back to the requester, because "is it fixed yet" is the department's most-asked public question. A request does not itself cause work to happen — it becomes work.

**Crew work order.** The work order is the unit of execution. It binds a work type to an asset or location, an assigned crew or worker, and a schedule; it advances through a life of open → assigned/scheduled → in progress → completed/closed (conceptual states; exact labels vary by product). On completion it records what the work cost: labor hours and cost, equipment time, and materials or supplies used. Work orders arise two ways — from converted service requests, and from the department's own planned and recurring work (preventive maintenance, inspections, seasonal programs). Work-order templates for repeated job types are a common efficiency mechanism.

**The maintained public estate.** Work attaches to the public-domain assets and locations the agency stewards: street segments and pavement, signs, street lights and signals, storm and drainage infrastructure, trees and grounds, public buildings, and the vehicle fleet. These may be held as asset records in the system (with location, class, and condition) or referenced more lightly as locations — but work orders and requests resolve onto them, and completed work accumulates as history on each object. A department runs many service domains under one roof; the system spans them rather than serving one asset class.

**The public-agency posture.** The records exist to be shown: response performance to residents, costs and activity to council and the budget process, and documentation to insurers, grantors, or disaster-recovery programs where the regime provides for it. This is not an add-on reporting layer — it is why the department keeps the records at all.

### How the pieces connect

```text
Resident / staff report
  ↓
Service request  ─── status visible to requester
  ↓ triage; duplicates considered
Work order  ← also created from planned/recurring programs
  ↓ crew / worker + schedule assigned
Field execution (mobile: view, navigate, photo, complete)
  ↓ labor + equipment + materials + cost recorded
Closed work, attached to the asset/location
  ↓ accumulates
Work and cost history per object; performance and cost reports outward
```

### Standard capabilities around the core

Mature products commonly add, around the defining loop:

- asset/inventory records for the estate (location, class, condition, accumulated history), often visualized on a map
- a citizen request portal with notifications and live status; staff-side intake for phone and walk-in reports
- automatic assignment notifications (email/text) and personal "my assigned work" views
- planned and preventive maintenance schedules alongside demand-driven work
- inspections and checklists tied to assets or work orders
- cost accounting per work order and per asset, with exportable and scheduled reports
- a mobile field app: assigned work list, location and navigation, photos, completion, barcode/QR asset lookup
- dashboards for open/in-progress/completed work, backlog aging, and the reactive-versus-planned mix
- parts and supply inventory feeding work orders; document and photo attachments

Capabilities that depend on segment, region, or product line — capital-planning and predictive analytics, disaster cost-recovery reporting, community event bookings, utility-domain modules, sensor-triggered work — are covered under Variants.

## How It Works

### The demand loop (the department's daily rhythm)

```text
Request arrives (portal / phone / staff observation)
→ recorded with issue, location, requester, photo
→ triaged: duplicate check, priority, correct domain/crew
→ converted into a work order
→ crew assigned; notification sent
→ work scheduled and dispatched
→ crew performs the work in the field, records time/equipment/materials
→ work order closed
→ requester sees the outcome; asset gains a work-history entry
→ costs roll up into activity and budget reporting
```

This loop is the application's center of gravity. Two details of it matter structurally:

- **The request→work conversion is the operational pivot.** Intake alone is a complaint log; the conversion is where demand becomes the department's work.
- **Completion is a costing event, not just a status change.** Closing work records labor, equipment, and materials — the raw material of every report the department owes the public.

### The planned loop

```text
Recurring/planned programs (preventive maintenance, inspections,
seasonal preparations)
→ scheduled work orders generated against assets or locations
→ same execution and costing path as demand work
```

### The accountability loop

```text
Work and cost history
→ dashboards (open work, backlog, reactive vs planned)
→ reports to management and council (activity, costs, service levels)
→ external documentation where the regime provides for it
  (insurer claim packs, grant and disaster-cost reports)
```

### Exceptions that shape the design

- **Duplicate reports of the same issue** (ten residents report one pothole) — triage must detect and merge rather than multiply work.
- **Requests that belong to another department** — routing or transferring a request outside the public-works scope.
- **Emergency work displacing planned work** — storm or main-break response interrupts the day's schedule; work orders get created and executed under time pressure and reconciled afterward.
- **Work on unmapped or new assets** — a location not yet in the inventory still needs work done and recorded.
- **Reopened work** — a closed request comes back as "still broken," reopening or spawning a new work order.
- **Crew unavailability** — assignments must be re-balanced when crews are out.

## Interfaces

### Operations dashboard (office)

The coordinator's home surface: lists of open service requests and work orders, charts and counts of the day's work, aging and backlog indicators. Primary actions: triage requests, create and assign work orders, check status, run reports.

### Service request triage

A request's detail view: what was reported, map location, requester contact, photos, request history in the area. Primary actions: set priority, assign to a domain or crew, convert to a work order, merge duplicates, correspond with the requester.

### Work order detail

The execution record: work type, asset/location, assignee, schedule, status, and — after completion — labor, equipment, materials, cost, photos, and notes. Primary actions: assign, reschedule, record completion, attach documents, reopen.

### Map view

Assets and work plotted geographically — the natural view of work that happens across a jurisdiction. Depth varies from a full GIS integration (where the agency's GIS is the authoritative asset inventory and the work system reads from it) to a lighter map layer. Primary actions: locate assets, see nearby or clustered work, select objects to start work or inspection.

### Citizen request portal

The public face: residents report issues (with photo and map pin) and follow their request's status. Primary actions: submit a request, view status, receive notifications. Many departments also take phone reports, entered by staff into the same request queue.

### Crew mobile app

The field surface: the worker's assigned work list, work order details, maps and navigation, photo capture, and completion recording — often with barcode/QR lookup to pull up an asset on site.

### Reports and dashboards

Activity, backlog aging, cost summaries, and planned-versus-reactive mix — the surfaces directors and finance use to answer council, justify budgets, and document work for external programs.

## Important Rules / Behaviors

- **A request is not work.** Nothing happens to the estate until a request is triaged and converted into a work order; conversely, planned work enters without any request.
- **Assignment gates execution.** Work orders sit in an unassigned queue until a crew or worker owns them; notifications and personal dashboards make ownership explicit.
- **Completion carries cost.** A work order closed without its labor/equipment/material record is incomplete for the department's reporting purposes; the cost record is what turns work into accountability data.
- **Work accrues to objects.** Completed work attaches to the asset or location, so each object carries its own history — the basis for condition judgments, repeat-failure spotting, and future planning.
- **Requester visibility is a commitment.** Status flows back to the resident who reported the issue; response-time performance is part of the department's public standing.
- **Location discipline.** Requests and work orders are locatable (address, pin, coordinates, or asset reference) — unmapped work is the exception, not the rule.
- **Domain routing.** The department's domains (streets, fleet, facilities, grounds, utilities where applicable) route work to the right crews; one system spans them.

## Variants

- **Department size and tier** — from small-town deployments (lightweight SaaS, quick implementation) to county and state-level estates (enterprise platforms with heavy analytics).
- **GIS posture** — GIS-centric products treat the agency's GIS as the authoritative asset inventory and work against it; others integrate map layers or map work locations only.
- **Estate scope** — departments differ in which domains they run: some include water/storm utilities, some include sanitation collection, some are facilities-heavy; the system's module set follows.
- **Region and regime** — some US deployments add disaster-cost-recovery reporting (FEMA) and claim documentation for insurers; UK highways practice and Australian/NZ council works-and-assets practice organize the same loop under different vocabulary and reporting obligations.
- **Capital-planning depth** — some products extend from operations into lifespan forecasting, risk scoring, and what-if funding scenarios that feed capital budgets; at other poles this lives in a separate asset-management product.
- **Seasonal and emergency programs** — snow and storm response as structured seasonal work; dedicated program machinery (routes, storm events) exists in some products, though it was not directly evidenced in the sources researched for this document and should be treated as product-dependent.
- **Adjacent services in the same platform** — community event and facility reservations, and payment processing, appear in some products as the department's public-facing services extend beyond maintenance.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Public Asset Management | centers the estate's stewardship record — register, condition, renewal outlook, multi-year plans; this Type centers the department's demand→dispatch→completion operation. Suite products often carry both faces; asset management is one system public-works teams use |
| 311 / Citizen Service Request Platform | centers the intake venue and complaint lifecycle; here the request record exists to become crew work, and work outcomes flow back. Products pair naturally ("save money on 311 services") |
| CMMS / Maintenance Management | same work-order machinery, but for a private owner's equipment and facilities; no public demand loop, no public-space estate, no public accountability outputs |
| Government Inspection Management | inspection program as regulatory managed unit (examinations against criteria, outcomes/violations); here inspections are common work attachments, not the managed unit |
| Facility Management System | facility-centered maintenance and space operations; facilities are one domain among many here |
| Fleet Management System | vehicle-centered; fleet appears here as one service-domain module |
| Government GIS | spatial data platform for the jurisdiction; the GIS-centric pole integrates with it, but GIS is not work management |
| Capital Improvement Planning | multi-year capital project and funding decisions; here capital planning (where present) consumes operations data as an optional extension |
| Utility Asset Management / Utility Field Service | utility network estate and utility customer operations (meters, service orders on accounts); this Type serves the agency's mixed civil estate and public requests |
| Smart City Operations Platform | senses and events (IoT monitoring, dashboards of the city); here sensors at most auto-trigger work orders — execution stays with crews |
| Parks & Recreation Administration | venue booking and program administration; parks crews appear here in their maintenance role |

## Representative Products

- **Trimble Unity Maintain** (the Cityworks lineage, now under Trimble) — the GIS-centric enterprise pole for cities, counties, and state DOTs
- **FMX** (Public Works) — lightweight modern SaaS serving counties and municipalities across infrastructure, facilities, fleet, and grounds
- **iWorQ** — module suite built for small-city public works and community development departments

## Sources

Research date: **2026-09-09**

- Trimble Unity Maintain (Cityworks lineage) — product page and FAQ: https://www.trimble.com/en/products/trimble-unity-maintain (reached via https://www.cityworks.com/)
- FMX Public Works — https://www.gofmx.com/public-works-software/ ; FMX — https://www.gofmx.com/
- iWorQ — https://iworq.com/ ; Work Management — https://iworq.com/systems/work-management-software/ ; Citizen Engagement — https://iworq.com/systems/citizen-engagement-software/
- Boundary context from the paired research of Public Asset Management (this repository)

> Sourcing limitation: vendor help centers for the major public-works products (Cityworks, Cartegraph, Lucity) were not reachable from the research environment on 2026-09-09 (403 / timeout). Claims in this document are therefore calibrated to official product pages and support-page-level evidence; precise operational details (status vocabularies, SLA timers, permission models, numeric limits) are intentionally not stated. Seasonal snow/storm program machinery is acknowledged as domain practice but was not directly documented in the fetched sources.

Detailed evidence, product-by-product observations, the cross-product comparison, and the historical/market-sample check are recorded in the paired Research Notes.
