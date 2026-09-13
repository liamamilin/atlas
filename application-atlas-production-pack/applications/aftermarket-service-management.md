# Aftermarket Service Management

## Overview

An **Aftermarket Service Management** application is the system a product manufacturer — or the authorized service network acting for it — uses to run the in-service life of the products it has sold: tracking the installed units at customer sites, recording what service each unit is entitled to, and driving every service demand on those units through a tracked fulfillment lifecycle to completion and settlement.

The defining core is small:

```text
Installed base (identified in-service units, per-unit service history)
└── Service entitlement (warranty / contract / SLA coverage per unit)
    └── Service demand (work object attached to a specific unit)
        └── Tracked fulfillment lifecycle → completion → settlement
```

Everything else commonly associated with this software — dispatch boards, technician mobile apps, depot repair queues, spare-parts logistics, customer self-service portals, partner networks, IoT-based remote service, analytics — is standard equipment in mature products but is not what makes the application what it is. A product that manages service work without anchoring it to identified sold units and their coverage is a different kind of application (generic customer service or generic field-service scheduling), no matter how similar the screens look.

## Users & Context

The organization behind the application is a service business attached to a product business: the manufacturer's after-sales organization, an authorized dealer or service partner, or a dedicated service division. Its revenue depends on keeping customer-owned equipment running — under warranty, under paid contracts, or through billed repairs.

Primary users:

- **Service representatives / support agents** — receive service demands, identify the unit and its coverage, create and progress the service work object.
- **Dispatchers / service planners** — schedule and assign work to field technicians or depot workstations, balancing skills, location, availability, and priority.
- **Field service technicians** — execute work at customer sites; consult the unit's history and entitlement, record parts used and time spent, close the job.
- **Depot / repair-center staff** — receive units sent in for repair, triage them into work queues, execute repairs, inspect quality, ship units back.

Secondary users:

- **Service managers** — monitor turnaround, SLA compliance, cost to serve, and service profitability.
- **Service parts planners** — keep spare parts available where service will need them.
- **Contract / warranty administrators** — create, amend, and renew service contracts and warranty terms.
- **Customers** — through self-service surfaces: registering products, requesting service, tracking progress, viewing their own asset records.
- **Partners / contractors** — through portals that assign them work and collect results back.

The work environment spans a back-office console, a dispatcher's scheduling surface, technicians' mobile devices (often offline-capable, since equipment sites frequently lack connectivity), repair-center workstations, and customer- and partner-facing portals.

## Core Model

### The defining core

Three structures carry the whole application. If any one is removed, what remains is no longer aftermarket service management.

**1. Installed base.** A managed registry of the product units the organization has sold and that are now in service at customer locations. Each unit is an identified record — commonly serialized — attributed to a customer account, carrying its installation details and configuration, and accumulating its service history: every visit, every repair, every replaced part, for the unit's whole life. This registry is the anchor of everything else; mature products describe their model as "asset-centric" for exactly this reason. The population is typically created and maintained as products are sold, delivered, and commissioned, and it changes over time as units are upgraded, reconfigured, moved, or retired.

**2. Service entitlement.** The recorded coverage that defines what service a unit is owed, on what terms, and until when: the base warranty that came with the sale, purchased extended warranties, service contracts and level agreements, and included response or resolution commitments. Entitlement is the commercial bridge between the original sale and today's service demand. When a service demand arrives, the application determines which coverage applies to the unit and surfaces that coverage to everyone involved in fulfilling the work — this is what separates a warranty repair from a billable one, and what the service organization uses to prevent revenue leakage.

**3. Service demand as a tracked work object.** A service request, work order, or return authorization attached to one specific unit in the installed base. It records what was demanded, what coverage applies, what work was performed, which parts and how much labor were consumed, and how it resolved. The work object moves through a lifecycle — intake, coverage determination, fulfillment, completion, and commonly invoicing — and its record joins the unit's permanent service history.

```text
Customer account
└── Installed base unit (identified, configured, history-bearing)
    ├── Service entitlement(s): warranty / contract / SLA coverage
    └── Service demand (work order / return authorization)
        └── Fulfillment: field visit · depot repair · parts · remote resolution
            └── Completion → parts/labor/billing → service history
```

### Standard capabilities around the core

Mature products add a consistent layer of machinery that makes the core operational at scale:

- **Scheduling and dispatch** — matching work to field technicians by skills, location, availability, and priority; dispatcher boards with real-time status; optimization of routes and schedules.
- **Mobile technician execution** — work orders, the unit's history and entitlement, service procedures and checklists, parts and time capture, and job closure, usable offline.
- **Depot repair and returns processing** — when a unit must come to a repair center: a return authorization is issued, the inbound shipment is received and matched against it, the unit is triaged into queues, repaired or replaced or exchanged under task-level work plans, inspected for quality, and shipped back.
- **Spare parts logistics** — checking parts availability, assigning parts to work orders, tracking shipments, and feeding consumption back to inventory and finance systems.
- **Preventive and planned service** — service plans and maintenance schedules generated from usage, thresholds, or regulatory requirements, so work is created proactively rather than only after failures.
- **Customer self-service** — product registration, service requests, appointment scheduling, progress tracking, and visibility into the customer's own asset data.
- **Partner and contractor channels** — portals through which dealers, service partners, and subcontractors receive work, manage their own technicians, and report results.
- **Commercial settlement** — parts consumption, labor, and billing events flowing to ERP/finance systems; service contracts quoted, fulfilled, and invoiced; service profitability measured.
- **Analytics** — technician productivity, resolution times, first-time-fix and SLA performance, cost to serve, service revenue.
- **Remote service** — in connected deployments, product telemetry used to investigate issues remotely and resolve without a site visit where possible.

### One structure, many implementations

The core is conceptual; products implement it differently, and the differences are philosophical rather than structural:

```text
Concept:   Installed base
Implementations:  installed products / assets (field-service-rooted products),
                  physical asset configurations with as-built records (PLM-rooted),
                  equipment + customer contract & warranty data (ERP-rooted)

Concept:   Service entitlement
Implementations:  a rules-driven entitlements engine (field-service-rooted),
                  contract and warranty objects inside the ERP service module,
                  coverage embedded in service plans and contracts (PLM-rooted)

Concept:   Service demand
Implementations:  work order (field), depot work order + return authorization,
                  service order / case in an ERP service module
```

A reader who has only seen one implementation — say, a dispatch-centric field-service product — should still be able to recognize an ERP-embedded service module or a PLM-rooted service engineering environment as the same Type from the core model.

## How It Works

### Sell → install → entitle

The application's world begins where the product sale ends. Sold units enter the installed base as identified records attributed to the buying customer, with their configuration and coverage: the base warranty that follows from the sale, plus any purchased service contracts. From this point on, the unit — not the sales order — is the object that service works on.

### Demand → coverage → fulfillment → settlement

The recurring operational loop:

```text
Service demand arrives (customer call, self-service request, contract-triggered
  plan, connected-product alert)
→ identify the specific unit in the installed base
→ determine applicable coverage (warranty / contract / SLA) and required response
→ decide fulfillment mode: field visit, depot repair / return, parts shipment,
  or remote resolution
→ schedule and assign the work (technician, depot queue, or partner)
→ execute: perform tasks, consume parts, record labor and observations
→ complete and confirm quality
→ settle: bill what is chargeable, feed parts/labor/billing events to ERP
→ the record joins the unit's service history
```

Two fulfillment modes deserve detail because they structure the work differently:

**Field service.** Work stays at the unit's site. Dispatchers schedule visits against technician skills, location, and availability; technicians arrive with mobile access to the unit's history, entitlement, procedures, and required parts; they record parts used and time spent and close the job on site — often without network connectivity.

**Depot repair / returns.** The unit travels to a repair center. A return authorization is created from the service demand; receiving matches the arriving unit against it; triage assigns the unit to a workstation and technician by skill, workload, and priority; task-level work plans drive repair, replacement, exchange, or simple return; quality inspection gates release; and the unit ships back to the customer or field location. The return authorization stays linked to the unit through the whole passage, giving one traceable record from request to release.

### Planned service

Not all work starts from a failure. Service plans and preventive maintenance schedules create work proactively — from usage counters, time intervals, thresholds, or regulatory requirements — so the same demand→coverage→fulfillment loop runs ahead of breakdowns. In connected deployments, product telemetry can trigger the loop automatically.

### The feedback loop upstream

Service history is also product knowledge. What fails, which parts wear, what repairs cost — mature deployments feed this back toward engineering and product management, closing a loop from in-service experience to future product design and service planning. In PLM-integrated environments this is explicit: the serviceable structure of the product (the service bill of materials) is derived from engineering data, and the as-maintained configuration of each fielded unit is tracked against it.

## Interfaces

The surfaces below are described conceptually; exact layouts and names vary by product.

### Service console (back office)

The service representative's and manager's primary surface.

- lists service demands, units, customers, and coverage
- typical information: unit identification, customer, entitlement status, demand details, status, SLA clock
- primary actions: create a service demand, verify coverage, progress status, escalate, close

### Scheduling / dispatch board

The dispatcher's surface for field work.

- typical information: open work, technician skills/locations/availability, priorities, travel
- primary actions: assign, reschedule, rebalance, handle exceptions

### Technician mobile application

The field execution surface, designed to work offline.

- typical information: assigned jobs, unit history and entitlement, procedures/checklists, parts required
- primary actions: start/complete tasks, record parts and time, capture signatures/photos, close the job

### Depot repair workbench

The repair-center surface.

- typical information: inbound units, return authorizations, queues, workstation status, inspection results
- primary actions: receive, triage, assign, execute work plans, inspect, ship

### Customer self-service portal

- typical information: the customer's registered units, coverage, open requests, progress
- primary actions: register a product, request service, schedule appointments, track status

### Partner / contractor portal

- typical information: assigned work, partner technicians, job status
- primary actions: accept and manage work, update status, provide feedback

### Analytics / dashboards

- typical information: SLA and turnaround performance, first-time-fix, technician productivity, cost to serve, service revenue and profitability

## Important Rules / Behaviors

### Coverage gates the work

The single most consequential rule: service delivery is checked against the unit's entitlement. What the application does next — free warranty repair, contract-covered visit with response commitments, or billable work — follows from that determination. Mature products surface coverage to every participant in the fulfillment chain and treat untracked coverage as a revenue-leakage risk.

### The unit anchors everything

Every service interaction is tied to a specific identified unit. Work, parts, labor, and billing all attach to the unit's record; the unit's history is the authoritative account of what has been done to it. This is what makes recalls, repeat-failure analysis, and audit-ready traceability possible — and it is why regulated industries (medical devices, aerospace) lean on this structure heavily.

### Work objects have lifecycles

A service demand is not a note; it is a stateful object that must progress through defined stages to completion, with the stages and their rules configured per organization. Depot work adds its own passage — authorization, receipt, triage, repair, inspection, shipment — and a unit should not re-enter service without passing the quality gate.

### Fulfillment consumes resources that must settle

Parts and labor consumed in fulfillment are not free text; they flow to inventory and financial systems. The service organization's economics — what a contract costs to serve, whether a repair is profitable — are computed from this linkage.

### Planned work competes with reactive work

Preventive and contract-driven work enters the same queues as breakdowns; scheduling has to balance them against capacity. SLA commitments on contract work typically outrank discretionary work.

### The service network is partly external

Dealers, service partners, and contractors fulfill a meaningful share of work in many deployments. The application must govern what external parties can see and do — their portals expose assigned work and unit context, not the whole installed base.

## Variants

Common shapes of the same Type:

- **Field-service-centric platforms** — dispatch, mobile execution, and entitlement management as the heart; depot repair and parts logistics as adjacent pillars. Typical of OEM/dealer service in industrial equipment, medical devices, high-tech.
- **ERP-embedded service modules** — contracts, service orders, returns and repairs, billing inside the ERP landscape; customer-service case management and field dispatch as connected satellite products. Typical of large enterprises standardizing finance and service on one vendor.
- **PLM-rooted service engineering** — the serviceable product structure, as-built/as-maintained configuration, and service planning as the heart; execution delegated to connected field-service or asset-management systems. Typical of complex engineered products and aerospace & defense.
- **Service-centric ERP suites** — field service, parts logistics, depot repair, and warranty handled as modules of one suite. Typical of service-heavy industries (field-dense equipment, energy).
- **Industry overlays** — medical-device traceability and compliance documentation; aerospace/defense product-support data exchange; multi-brand equipment dealers servicing products they did not manufacture; high-volume consumer-electronics depot repair; remanufacturing and circular-economy dispositions.

A variant remains a variant while the defining core holds. When work is no longer anchored to sold units and their coverage — a cleaning company scheduling house visits, an IT help desk resolving software inquiries — the same screens belong to a different Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| CMMS / Enterprise Asset Management | adjacent, same machinery | EAM maintains the operator's **own** production assets; aftermarket service manages **sold** units at customer sites. Asset ownership is the test. Vendors ship both in one product line, and integrations connect them. |
| Field Service Management (generic) | fulfillment-layer overlap | Generic FSM schedules jobs for any customer with equipment as incidental detail; this Type anchors work to an installed base with entitlement. All sampled products market themselves as FSM/SLM — the aftermarket Type is the asset-centric superset. |
| Product Lifecycle Management (PLM) | upstream neighbor | PLM governs as-designed/as-built product data; this Type governs the in-service/as-maintained phase. The service bill of materials and the service→design feedback loop are the bridge. |
| Customer Service Platform / Help Desk | adjacent | Case management for inquiries without unit anchoring or coverage semantics. In ERP-rooted stacks both exist side by side: cases for general contact, unit-anchored work objects for product service. |
| Returns Management Platform (e-commerce) | name-similar, structurally different | E-commerce returns refund or replace an **order line**; service returns (RMAs) restore the function of a **serialized unit**. Different object, different purpose. |
| Warranty Management | embedded capability | Warranty registration and claims adjudication without work-order fulfillment is a narrower capability that mature products embed here, not the Type itself. |
| Maintenance, Repair & Overhaul (MRO) | industry variant | Aviation/defense MRO implements the same core with deeper as-maintained configuration and regulatory data exchange. |

## Representative Products

- **PTC ServiceMax** — asset-centric field service management platform; installed base, entitlements engine, work execution, depot repair and service logistics.
- **Siemens Teamcenter Service Lifecycle Management** — PLM-rooted service engineering: service BOM, as-built/as-maintained configuration, service plans, closed-loop integration with execution systems.
- **SAP service portfolio (S/4HANA Cloud for Service, SAP Service Cloud, SAP Field Service and Asset Management)** — ERP-rooted service: contracts, returns and repair services connected to warranty data, spare-parts planning, scheduling and mobile execution, billing.
- **IFS Cloud (Service Management / Field Service Management, Service Logistics & Depot Repair)** — service-centric ERP suite: field service, contractor management, parts logistics, depot repair and warranty claims in one platform.

## Sources

Research date: **2026-09-06**

- PTC — ServiceMax product overview (asset-centric field service management): https://www.servicemax.com/
- PTC — ServiceMax Depot Repair & Service Logistics: https://www.ptc.com/en/products/servicemax/core/depot-repair
- Siemens — Teamcenter Service Lifecycle Management: https://www.siemens.com/en-us/products/teamcenter/solutions/service-lifecycle-management/
- SAP — Service Management (portfolio overview): https://www.sap.com/products/service-management.html
- SAP — Field Service and Asset Management: https://www.sap.com/products/scm/field-service-and-asset-management.html
- SAP — Service Cloud: https://www.sap.com/products/crm/service-cloud.html
- IFS — Field Service Management: https://www.ifs.com/en/products/fsm
- IFS — Service Logistics and Depot Repair: https://www.ifs.com/en/products/fsm/service-logistics-and-repair

> Sourcing limitation: vendor help-center and operational documentation portals (SAP Help Portal, IFS documentation, ServiceMax documentation) were not reachable from the research environment on 2026-09-06; all evidence comes from official product pages. Consequently this document deliberately avoids precise operational details — exact status names, numeric limits, default settings, and timing rules — and describes structures and flows at the level the sources support. Detailed observations and evidence calibration are recorded in the paired Research Notes.
