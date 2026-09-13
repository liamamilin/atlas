# CMMS / Maintenance Management

## Overview

A **CMMS** (Computerized Maintenance Management System) is maintenance operations software: it keeps a register of the physical assets an organization must maintain, manages maintenance work as **work orders** bound to those assets, and accumulates every completed job into a persistent **maintenance history** on each asset.

The defining core is small:

```text
Maintainable Asset Register
└── Work Order bound to an Asset
    (created → assigned → executed → closed with a record)
    └── Persistent Maintenance History
        (what was done, by whom, how long, at what cost)
```

Everything else the market associates with the category — preventive maintenance scheduling, request portals, spare-parts inventory, mobile apps, dashboards — is a standard capability layered on this core, not part of the definition. A reactive-only deployment with no PM schedules, no inventory, and no mobile app is still recognizably a CMMS; a system with asset records but no managed work orders is not (it is an asset registry); a system with work items but no asset register is a generic ticketing tool.

The Type's purpose is to move a maintenance operation from informal tracking (paper, spreadsheets, email, radio calls) to a managed system of record: work is captured, prioritized, assigned, executed, documented, and measured, and each asset's service life is managed against that record.

## Users & Context

The CMMS serves an internal maintenance organization — the people responsible for keeping an organization's own equipment, facilities, vehicles, or infrastructure running. Typical settings include manufacturing plants, food and beverage production, facilities and campuses, healthcare and biomedical equipment, fleets, utilities, government public works, and property operations.

Primary users:

- **Maintenance manager / supervisor** — owns the operation: triages incoming work, sets priorities, assigns technicians, plans the schedule, watches backlog and completion metrics, answers for downtime and cost.
- **Maintenance technician** — executes the work: receives assignments, follows procedures and checklists, records labor time and parts used, documents what was done, closes the work order. Increasingly works from a mobile device at the asset itself.
- **Requester** — anyone outside the maintenance team who reports a problem or needs service (production operators, facility occupants, other departments). Requesters typically submit through a portal or form and do not hold a full license; some products make requester seats free or account-free by design.

Secondary users:

- **Maintenance planner / scheduler** (larger organizations) — prepares planned work in advance: builds procedures, checks parts availability, schedules work when assets and labor are free.
- **Reliability / maintenance engineer** — analyzes failure and downtime data, tunes preventive maintenance programs.
- **Administrator** — configures the asset register, PM schedules, users, roles, and permissions.
- **Vendors / contractors** — external service providers who may receive assigned work or access a limited portal.

The work environment is dual: an office-side web application for managers and planners, and a mobile application for technicians on the floor, in the field, or in dead zones with offline capture and later sync.

## Core Model

### The Defining Core

**Asset (equipment record).** The central object of the register: a maintainable physical thing — a machine, production line, HVAC unit, vehicle, pump, elevator, medical device — identified by name/number and described by fields such as location, model, serial number, criticality, and warranty. Assets are organized by **location** (site → building → area) and often by **hierarchy** (a production line containing machines containing components), so that work can be recorded at the right level and rolled up. Assets can be moved between locations and eventually retired; the register is a living map of "what exists and what must be maintained."

**Work order.** The managed unit of maintenance work, always anchored to one or more assets (and usually a location). A work order carries: a description of the problem or task, priority, requested/due dates, assigned technician(s), status, planned procedures or checklists, logged labor hours, parts consumed, costs, and closing documentation (what was done, findings, photos, signatures). It has a lifecycle — created, assigned, scheduled, in progress, closed — and closed work orders can typically be reopened for corrections. Work orders are created from requests, from PM schedules, or directly by maintenance staff.

**Maintenance history.** The cumulative record: every closed work order remains attached to its asset, forming a queryable service history — what failed, what was done, when, by whom, how long it took, what it cost. This history is what makes the system a *management* system rather than a dispatch tool: it supports troubleshooting ("how was this fixed last time?"), warranty claims, audits, and decisions about repair-versus-replace.

### Standard Capabilities

Mature products commonly add the following around the core. They are what make a CMMS practical, but a product lacking any one of them can still be a CMMS.

- **Preventive maintenance (PM) scheduling** — recurring maintenance defined per asset (or asset group) and triggered automatically: by calendar/time intervals (weekly, monthly, seasonal) or by usage (meter readings, runtime hours, mileage). A PM template holds the task list and instructions; the scheduling engine generates work orders when each cycle comes due, and the next cycle may be scheduled from the completion date rather than the original calendar date (behavior varies by product). PM calendars and planners give a forward view of scheduled work.
- **Work request intake** — a form or portal (link, QR code, email, sometimes phone intake) through which non-maintenance staff report problems. Requests are triaged by the maintenance team: duplicates are detected and merged, some requests require review or approval, and accepted requests convert into work orders. Requesters usually see the status of their own submissions.
- **Task templates, procedures, and checklists** — reusable, standardized instructions for recurring jobs, with step-by-step tasks and time estimates, so PM work is performed consistently regardless of who does it.
- **MRO spare-parts inventory** — a parts catalog with stock levels per storeroom/location, minimum thresholds and reorder points, reservations of parts against planned work, issue of parts to work orders, part movement logs, and cycle counts. Parts are associated with the assets that use them.
- **Vendors and contractors** — supplier records, parts sourced per vendor, and mechanisms to share work with external service providers, sometimes with approval gates for contractor work.
- **Labor and cost tracking** — technician hours logged against work orders (often with rates), parts cost, and computed work order cost; asset-level cost accumulation over time.
- **Planning surfaces** — backlog views, work order calendars, technician workload views, search by asset/priority/due date.
- **Metrics and dashboards** — work order completion and overdue counts, backlog, PM completion/compliance, asset downtime; KPI tracking is a standard reporting frame across the researched products.
- **Mobile technician app** — the work queue, asset lookup (often via QR/barcode scan on the equipment), checklists, photo capture, time and parts entry, and closure — with offline operation and later sync.
- **Multi-location support** — multiple sites/storerooms with location-scoped assets, parts, and reporting.
- **Audit trail** — timestamps, user attribution, and change history on records; deepest in compliance-oriented deployments.
- **Roles and permissions** — at minimum a distinction between administrators/managers (configure, assign, approve, see everything), technicians (execute assigned work), and requesters (submit and view own requests).

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:  Maintainable Asset Register
Realized as:  equipment records with location hierarchies, functional-location
              trees, asset maps, parent/child component structures

Concept:  Work Order
Realized as:  work orders, maintenance tickets, tasks (some products model PMs,
              work orders, and work requests as distinct task types under one engine)

Concept:  PM Trigger
Realized as:  calendar schedules, meter/runtime readings, conditional schedules,
              sensor-threshold events

Concept:  Request Intake
Realized as:  web portals, QR-code forms, email intake, phone/voice intake
```

Exact status names, field sets, and limits vary by product; the conceptual lifecycle above is the stable part.

## How It Works

### The reactive loop (unplanned work)

```text
Something breaks or needs service
→ requester submits a work request (portal / QR / email / phone)
   or a technician creates a work order directly
→ maintenance team triages: deduplicate, prioritize, approve if required
→ request converts into a work order on the affected asset
→ work order is assigned and scheduled (parts availability checked)
→ technician executes: follows procedure/checklist, logs time, consumes parts,
   attaches photos/notes
→ work order is closed with required documentation
→ the record lands in the asset's maintenance history
```

### The planned loop (preventive maintenance)

```text
Define a PM schedule on an asset (or asset group)
→ choose the trigger: calendar interval, meter/runtime reading, or both
→ attach a task template / checklist with instructions and time estimates
→ the engine generates a work order when the cycle comes due
→ planner/manager reviews the PM calendar, adjusts or reassigns as needed
→ technician executes and closes
→ the next cycle is scheduled (in some products, from the completion date)
→ PM completion feeds compliance and reliability metrics
```

### The supporting loops

- **Parts replenishment**: stock falls below a threshold → reorder point alert → purchase order (in products with purchasing) → receipt → stock available for reservation against planned work.
- **Planning**: the manager works the backlog — reviewing open work, balancing technician workload, pulling planned work forward when assets and labor are free, escalating overdue work.
- **Condition-based extension** (optional): sensor readings or meter values cross a threshold → the system generates a prioritized work order automatically, with asset history and parts availability attached for the technician.
- **Measurement**: dashboards and reports aggregate work order data into completion rates, backlog, PM compliance, downtime, and cost per asset — closing the loop back into planning and PM tuning.

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Asset list / asset detail

The register. Lists assets with locations, status, and criticality; the detail page holds identity fields, location/hierarchy placement, associated parts and documents, open work orders, and the full maintenance history. Primary actions: create/import assets, edit fields, move location, open a work order, view history, retire.

### Work order list / work order detail

The operational heart. The list shows open work by status, priority, assignee, and due date, with backlog and overdue visible. The detail page carries the problem description, asset and location, priority, assignee, schedule dates, procedure/checklist, labor and parts entries, attachments, and the audit trail. Primary actions: create, assign, prioritize, update status, log time/parts, attach documentation, close (or reopen).

### PM planner / maintenance calendar

The forward-looking schedule of preventive work: upcoming and overdue PMs by asset, technician, and date, commonly presented as a calendar view (color-coding in some products); primary actions: create/edit PM schedules, reschedule or reassign generated work orders, review PM compliance.

### Request portal

The requester-facing surface: a simple form (often reachable by link or QR code, sometimes without requiring an account) to report a problem, plus a "my requests" view showing status. Maintenance-side, a request queue supports triage: merge duplicates, approve, convert to work order.

### Parts / inventory screens

The storeroom view: parts with on-hand/allocated quantities per location, thresholds and reorder points, part logs, cycle counts, and links from parts to the assets and work orders that use them. Primary actions: adjust stock, transfer, reserve, reorder.

### Dashboards / reports

Management view: completion and overdue work, backlog, PM compliance, downtime, and cost metrics, filterable by site, asset, or time period; exportable reports for audits and stakeholder summaries.

### Mobile technician app

The point-of-work surface: assigned work queue, QR/barcode asset scan pulling up the asset and its history, checklist execution, time and parts entry, photo capture, and closure — usable offline with later sync.

### Administration / settings

Asset and PM configuration, custom fields, users/teams, roles and permissions, locations, notification and escalation rules, integrations.

## Important Rules / Behaviors

- **Closure is gated by documentation.** Products commonly require defined fields to be completed before a work order can be closed — what was done, time spent, who performed it — and some prevent technicians from closing without proper documentation. This is what keeps the maintenance history trustworthy.
- **Closed work is history, not trash.** Closed work orders remain attached to the asset and may be reopenable for corrections (product-dependent); editing completed records is controlled, and compliance-oriented products timestamp and attribute every change.
- **Requests and work orders are different objects.** A request is a report from outside the team; it becomes a work order only after triage. Duplicate detection (by asset, location, and description) with merge/link options is a common triage behavior, because the same broken asset often gets reported several times.
- **In some products, PM cycles reschedule from completion.** A recurring PM's next due date may be computed from when the work was actually completed rather than from the original calendar date — so late completions shift the whole cycle. Meter-based PMs depend on recorded readings; missed readings stall the trigger.
- **Approval gates sit before work, not after.** Where configured, manager sign-off is required before work starts — typically for high-cost repairs or contractor work — rather than as an after-the-fact review.
- **Parts availability shapes planning.** Planned work is scheduled when parts and labor are available; parts are reserved against planned work orders, and stock thresholds trigger replenishment. Consuming a part on a work order decrements inventory and records the movement.
- **Requesters are not technicians.** The requester population is broad and license-free in many products; their surface is deliberately limited to submitting and tracking their own requests, while assignment, prioritization, and closure remain maintenance-team actions.
- **The asset is the anchor of accountability.** Costs, downtime, and compliance accumulate on assets; assets can be moved between locations and eventually retired, and retirement closes the record rather than erasing it.

## Variants

- **Deployment**: cloud SaaS (dominant today) vs on-premise installation; subscription vs perpetual license. On-premise and perpetual-license editions remain a real segment.
- **Scale**: single-site small teams (work orders + assets is the entry floor) through multi-site enterprises (multi-site governance, SSO, custom roles, APIs, cross-site reporting).
- **Capability poles**: mobile-first CMMS built around technician adoption vs enterprise CMMS/EAM platforms built around governance, compliance, and integration depth.
- **Industry tuning**: manufacturing (downtime, OEE context), food & beverage (sanitation and audit readiness), facilities and campuses, healthcare/biomedical equipment, fleet (service by mileage/hours), government/public works, wastewater, pharma (validated, compliance-grade records).
- **Maintenance strategy emphasis**: reactive/corrective-only deployments; preventive (calendar/meter) programs; condition-based and predictive extensions driven by sensor or meter data.
- **Compliance depth**: regulated-industry editions with validation, e-signatures, and audit-grade trails (life sciences, pharma).
- **Requester scope**: internal-only requesters vs portals that also serve external customers (common in facility/property service contexts).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Enterprise Asset Management / EAM | superset / converging | EAM adds the asset's full financial and lifecycle governance — procurement, accounting, depreciation, capital planning, disposal — on top of the CMMS work-management core; vendor positioning treats EAM as the superset of the CMMS. The seam is whether asset financial lifecycle is a first-class structure or an extension. |
| Enterprise Asset Registry | adjacent | Asset records without managed work orders; the "remove the work order" test separates them. |
| Reliability Management | consumer / sibling | Reliability engineering (failure analysis, RCM/FMEA, condition-monitoring programs) analyzes and optimizes the strategy; the CMMS captures the operational data and executes the work. Predictive triggers inside a CMMS are an extension, not the whole discipline. |
| Facility Management System / IWMS | adjacent | FM/IWMS centers on buildings, space, leases, occupancy, and contracted services; building maintenance within FM is typically served by a CMMS-like module. |
| Property Maintenance Management | adjacent | Tenant/lease/unit orientation with rent-side workflows; request intake overlaps, but the organizing spine is tenancy, not maintenance operations. |
| Fleet Management System | domain cousin | Vehicles with telematics, routing, and compliance as the spine; CMMS principles apply to vehicle service, but fleet operations are a distinct Type. |
| Aircraft Maintenance Management | domain cousin | Airworthiness and regulatory MRO with its own compliance spine; a specialized relative of maintenance management. |
| IT Service Management / ITSM | structural analog | Manages tickets and assets for IT services rather than physical maintenance; no PM recurrence or MRO parts semantics at the core. |
| Tool Management / Calibration Management | narrow siblings | Single-domain specializations (tools, calibrated instruments) that commonly ride inside a CMMS as modules. |
| Field Service Management | adjacent | Dispatches technicians to external customers' sites; a CMMS maintains the organization's own operations, though some products add external request intake. |
| Aftermarket Service Management | adjacent | Service delivered on products sold to customers (warranty, service contracts); the maintained object belongs to the customer, not the operator. |

The most important boundary is the **EAM** one, because the market itself is convergent: CMMS vendors add lifecycle and purchasing depth while EAM platforms embed CMMS cores. The working discriminator: a CMMS is defined by maintenance work management (assets + work orders + history); an EAM is defined by the asset's whole-of-life governance, of which maintenance is one phase.

## Representative Products

- **Limble CMMS** — SMB/mid-market cloud CMMS; explicit task model separating PMs, work orders, and work requests.
- **UpKeep** — mobile-first CMMS spanning SMB to enterprise; pricing tiers illustrate the capability layering (work orders + assets at entry; PM, parts, request portal, lifecycle above).
- **eMaint (Fluke)** — mid-market to enterprise CMMS/EAM with compliance-grade audit trails and condition-monitoring integration.
- **FTMaintenance (FasTrak SoftWorks)** — SMB/mid-market CMMS available both cloud-hosted and on-premise (perpetual license), with a canonical feature taxonomy.

The definition was checked against deployment and era variety (cloud vs on-premise/perpetual, mobile-first vs office-first) rather than a single market moment. Enterprise EAM-heritage and open-source products could not be directly documented in this research pass (see Sources); their fit with the definition is supported by vendor boundary articulations rather than direct observation.

## Sources

Research date: **2026-09-07**

- Limble CMMS Help Center (Tier 1): https://help.limblecmms.com/en/ — including "Types of Tasks in Limble", the "Tasks (PMs, WOs & WRs)", "Assets, Parts & Vendors", and "PM Schedule Options & Configuration" collections
- UpKeep (Tier 2): https://upkeep.com/ (root + FAQ), https://upkeep.com/product/cmms-software/
- eMaint (Tier 2): https://www.emaint.com/ , https://www.emaint.com/work-order-management , https://www.emaint.com/customer-support-center
- FTMaintenance (Tier 2): https://ftmaintenance.com/ , https://ftmaintenance.com/cmms-features/preventive-maintenance/ , https://ftmaintenance.com/cmms-features/work-order-management/

> Sourcing limitation: official help-center documentation for Fiix (help.fiix.io), IBM Maximo (ibm.com/docs), and Odoo Maintenance (odoo.com/documentation) was not reachable from the research environment on 2026-09-07 (transport errors / access denied). The enterprise EAM-heritage and open-source poles are therefore evidenced indirectly through vendor boundary articulations rather than direct observation. Precise operational details (exact status names, numeric limits, default settings, specific KPI definitions) are intentionally not asserted in this document; vendor performance claims (e.g., completion-rate percentages) were observed but are not reproduced as facts.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/deployment-variety check are recorded in the paired Research Notes.
