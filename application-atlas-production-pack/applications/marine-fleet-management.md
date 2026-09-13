# Marine Fleet Management

## Overview

A **Marine Fleet Management** application is the shipowner's or ship manager's fleet-side system of record: it holds the operator's vessels as individually identified, managed records, gives each vessel a living technical file organized around its equipment, and runs the ship–shore loop through which crews execute and record work onboard while shore-based technical teams plan, approve, and oversee the whole fleet.

It solves the problem that a shipping company's vessels are expensive, mobile, regulated, crewed by rotating people, and operated far from the office that is accountable for them. The owner or manager needs to know, per vessel: what maintenance is due or overdue, what has been done to it, which spares and certificates it has, who is crewing it, what it costs — and needs a place to act on that knowledge across dozens or hundreds of ships at once.

The defining structure is small:

```text
Fleet register (the operator's vessels as identified managed records)
└── Per-vessel technical record (organized on the vessel's equipment)
    └── Ship–shore management loop (crew executes onboard → shore oversees and acts)
```

Everything commonly associated with modern maritime software — live position tracking, sensor feeds, voyage optimization, fuel and emissions analytics, electronic logbooks, payroll — is widespread in current products or sold alongside them, but none of it is what makes the product a marine fleet management system. The paper-era ship management office (vessel files, maintenance schedules, survey and certificate registers, requisition books) and the on-premise software generation that replaced it both satisfy this definition without any of those specifics.

When the primary object becomes the voyage and its execution (routes, noon reporting, performance monitoring), the product is drifting toward a Vessel Operations Platform; when it becomes the cargo business (bookings, chartering, freight documents), toward Ocean Freight Management; when it becomes raw position data about other people's ships, toward a vessel-tracking service; when it becomes berthing spaces and the facility's rental business, that is Marina Management.

## Users & Context

The system is used by organizations that own or manage commercial vessels — shipowners, third-party technical (ship) managers, and operators of cargo fleets, ferries, offshore and workboat fleets, and increasingly yachts and cruise ships.

Primary users:

- **Technical superintendent / fleet manager (shore)** — the central role of the oversight side: monitors maintenance status, defects, and compliance across all vessels, plans work and dry docks, standardizes structures and procedures fleet-wide.
- **Chief engineer and crew (onboard)** — execute and record the work: work through job lists, report defects, record spare-part consumption, fill in forms and checklists, raise requisitions. The crew is both the workforce and the main data source.
- **Purchasing / procurement (shore)** — turns requisitions from vessels into approved purchase orders and manages vendors and deliveries to ships.
- **Safety / quality (HSEQ) team (shore)** — runs the safety-management side: incidents, non-conformities, audits, corrective actions, certificates.

Secondary users:

- **Crewing / HR (shore)** — maintains seafarer records, certifications, sign-on/sign-off, rotation planning, and commonly payroll.
- **Finance / management** — consumes per-vessel operating costs, budgets, and fleet-level reporting; in some products works directly in built-in accounting modules.

The work environment is inherently two-sided: a shore-side office application (the fleet oversight surface) and an onboard surface (job lists, forms, requisitions) that must keep working with intermittent, low-bandwidth connectivity and synchronize when a connection is available.

## Core Model

### The Defining Core

```text
Fleet register
└── Per-vessel technical record (organized on the vessel's equipment)
    └── Ship–shore management loop
```

Three properties. If any one is removed, the product is no longer recognizable as marine fleet management:

- **Fleet register** — the operator's vessels exist as individually identified, managed records (name and identity numbers, vessel type and attributes, fleet grouping) inside one organization-scoped system belonging to the owner or manager. Without it, there is no fleet — only disconnected per-vessel tools.
- **Per-vessel technical record** — each vessel carries a *living technical file* structured around its equipment: a hierarchy of components and systems to which planned-maintenance jobs, reported defects and corrective work, spare parts, certificates and documents, and costs are attached, accumulating over the vessel's service life. Without it, maintenance, spares, and certificates stop cohering, and the product degrades into a flat asset list or a generic maintenance tracker.
- **Ship–shore management loop** — work is executed and recorded onboard by the vessel's crew (tolerant of intermittent connectivity), synchronized to the shore office, where superintendents and technical managers monitor fleet-wide status, plan and approve work, standardize structures and procedures, and push actions back to vessels. Without it, the product is either a shore archive the crew never feeds or an onboard tool with no fleet-level management.

The marine context is carried inside these objects rather than stated as a feature: the equipment structure is the ship's own systems, the certificates are the vessel's class and statutory documents, the executing party is a certified crew, and the connectivity is that of a ship at sea.

### Capabilities Shared by Mature Products

A typical modern product carries most of these. They are not what makes the product a marine fleet management system, but they make it work in practice.

- **Planned maintenance machinery** — recurring jobs generated from calendar time, running hours, or condition-based triggers; job relations and sequencing; critical-equipment analysis; full maintenance history per component.
- **Defect and corrective work** — defects reported onboard become tracked corrective jobs linked to the component, with responsibility and resolution recorded.
- **Spares and inventory** — spare-part records per component and per vessel; stock levels onboard and ashore; job-linked consumption; low-stock requisitions; spares movable between sister vessels.
- **Procurement** — requisitions (often raised onboard) flowing through multi-level approvals into purchase orders, vendor management, and goods receipt.
- **Crewing** — seafarer records with certifications and documents, sign-on/sign-off, rotation and manpower planning, commonly payroll; some products add work/rest-hour compliance machinery.
- **HSQE / safety management** — incident and non-conformity reporting, audits and inspections, corrective actions, permits to work and structured forms; support for the operator's safety-management system.
- **Certificates and surveys** — statutory and class certificates tracked with expiry timelines and reminders; survey records attached to the vessel.
- **Dry dock management** — docking events planned as projects: specification, tendering, budgets, execution, and final reporting, feeding the next docking cycle.
- **Document management** — ship–shore distribution of manuals, procedures, and job instructions; changes pushed to many vessels at once.
- **Fleet-wide dashboards and analytics** — overdue jobs, open defects, KPIs, budgets, and dry-dock analysis across all vessels from one point of control.
- **Master data standardization** — shared component structures and job templates across sister vessels, so crews see the same structure wherever they are assigned.
- **Mobile and offline onboard apps** — crews execute, record, and close tasks on mobile devices and keep working offline; some products add equipment-code scanning to open a component's record.
- **Roles and approvals** — office-versus-onboard permissions and approval chains, especially in procurement and safety workflows.
- **Class-approved records** — the maintenance system itself is commonly certified or approved by classification societies, because its records are what the operator shows at surveys and inspections.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:                    Fleet register
Implementations:            vessel records with identity numbers, types, groups;
                            fleet-wide lists and dashboards; archived vessels

Concept:                    Per-vessel technical record
Implementations:            component/equipment tree mirroring the vessel;
                            job lists with history; data libraries of equipment,
                            spares, and jobs; certificate and document stores

Concept:                    Ship–shore loop
Implementations:            scheduled data exchange, replication modules that
                            sync when connectivity returns, near-real-time
                            dashboards; onboard apps that work offline
```

A reader who has only seen a cloud dashboard product should still recognize an on-premise, sync-based, or even paper-heritage system from the core model.

## How It Works

### Set up the fleet

```text
Register each vessel (identity, type, attributes, grouping)
→ build the vessel's equipment/component structure
→ load planned-maintenance schedules, spares, certificates, documents
→ add users ashore and crews onboard, assign roles
→ standardize structures across sister vessels
```

The register and the per-vessel structure come first; modules and data sources attach to them. Products differ in how much is bundled, but the sequence is the same.

### Run the ship–shore maintenance loop

```text
System generates due jobs (calendar time / running hours / condition)
→ crew works the job list onboard (often offline), records completion,
  spare-part consumption, and measurements
→ records synchronize to the shore office
→ superintendents monitor fleet-wide status (overdue jobs, defects, costs)
→ shore plans, approves, adjusts schedules, and pushes updates back
→ history accumulates on the component, driving the next round of jobs
```

This loop is the daily work of the chief engineer and the superintendent, and it is what turns the accumulated record into management. Defects reported at sea enter the same loop as corrective jobs.

### Run the procurement loop

```text
Requisition raised (commonly onboard, against a component or stock level)
→ multi-level approval ashore (budgets, company policy)
→ purchase order to vendor → goods delivered to the vessel
→ receipt and consumption recorded against the vessel's record
```

### Keep the vessel legal

```text
Certificates and survey records held per vessel with expiry timelines
→ reminders fire before expiry
→ surveys and inspections completed; records updated
→ the system's maintenance and safety records are what the operator
  produces at class and port-state inspections
```

### Plan and run a dry dock

```text
Docking due (class interval or condition)
→ specification built from the vessel's job history and defects
→ tendering and budget approval
→ execution tracked as a project; final reporting closes the dock
→ the next docking cycle is prepared from the outcome
```

### Prove and report

```text
Accumulated fleet record → dashboards and reports
→ maintenance status, defects, spares, crew, certificates, budgets
→ used for technical management decisions, audits, and owner reporting
```

### Core vs Common vs Optional

**Defining core** — without these, not marine fleet management:

- fleet register of identified vessels
- per-vessel technical record organized on the vessel's equipment
- ship–shore management loop with crew-executed, offline-tolerant onboard work

**Common mature structure** — present in most modern products:

- planned-maintenance machinery · defects and corrective work · spares/inventory · procurement · crewing · HSQE/safety management · certificates and surveys · dry dock management · document management · fleet dashboards · master-data standardization · mobile/offline onboard apps · roles and approvals · class-approved records

**Variant / optional** — depends on segment, operator, and packaging:

- voyage/fuel/performance layers (noon reporting, emissions, voyage optimization)
- electronic logbooks · commercial/chartering modules · built-in accounting suites · insurance/claims · catering/provisions · CRM
- onboard sensor integration and predictive maintenance depth
- deployment shape (on-premise, cloud, hybrid) · AI assistance
- segment editions (cargo, ferry, offshore, cruise, yacht)

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Fleet dashboard (shore)

The oversight entry surface.

- maintenance status, overdue jobs, open defects, and KPIs across all vessels
- primary actions: drill into a vessel, acknowledge or assign work, jump to procurement or safety views

### Vessel record / component tree

The register surface and the vessel's living technical file.

- the vessel's equipment hierarchy mirroring its real layout; per component: jobs, history, documents, spares, certificates
- primary actions: plan or complete jobs, report defects, attach documents, move spares, update certificates

### Job list (onboard)

The crew's working surface.

- due and planned jobs with instructions, defect reports, forms and checklists, permit-to-work documents
- primary actions: start and complete jobs, record consumption and measurements, report a defect, raise a requisition — usable offline; some products let crews scan a code on the equipment to open its record

### Procurement workbench (shore)

- requisitions awaiting approval, purchase orders, vendors, deliveries to vessels
- primary actions: approve or reject at defined levels, create POs, track receipts

### Crewing views (shore)

- crew pool per vessel, certifications and document expiry, sign-on/sign-off, rotation planning
- primary actions: assign crew to a vessel, plan rotation, track certification renewal

### Safety / quality views (shore and onboard)

- incidents, non-conformities, audits, corrective actions; structured forms and checklists
- primary actions: report an event, assign follow-up, verify closure, prepare for audits

### Dry dock project views (shore)

- docking specification, budgets, tendering status, execution progress, final reports

### Reports and settings

- fleet-level analytics (maintenance, costs, compliance); administration of users, roles, master data, and integrations

## Important Rules / Behaviors

### The loop tolerates disconnection

Vessels work with intermittent, low-bandwidth connectivity. Onboard work continues offline and synchronizes when a link returns; products differ in cadence (scheduled exchange, replication on reconnect, near-real-time), but the two-sided record must reconcile. This is a structural behavior, not an add-on.

### Maintenance is triggered by the vessel's own usage

Jobs fire on calendar time, running hours, or condition — not on fixed dates alone. This is why the usage and measurement stream in the technical record matters even without live telemetry.

### Defects become tracked work

A defect reported onboard is converted into a corrective job linked to the component, with responsibility and resolution recorded — it is not a free-floating note.

### Certificates expire, and expiry is managed

Statutory and class certificates carry expiry timelines with reminders; the system's records are what the operator presents at surveys and inspections. The maintenance system itself is commonly class-approved for this reason.

### The fleet shares one structure

Mature operators standardize component structures, job templates, and procedures across sister vessels, so a crew moving between ships sees the same picture; vessel-specific variation is retained where needed.

### Procurement is approval-gated

Requisitions — often raised onboard — pass through defined approval levels and budget checks before becoming purchase orders; spending is attributed to the vessel.

### Permissions split shore and onboard

Office roles oversee and approve; onboard roles execute and record. Access to safety data, costs, and documents follows role and commonly licensing.

## Variants

Common forms of the Type:

- **deep-sea cargo fleets** — tankers, bulk carriers, container ships; the classic ship-management deployment with full technical, crewing, and compliance depth
- **ferry and RoRo operators** — passenger-ship compliance emphasis, standardized fleets
- **offshore and workboat fleets** — tugs, offshore support vessels; project- and charter-adjacent operations
- **cruise fleets** — vessel technical management alongside (not replaced by) guest/hotel operations systems
- **yacht management** — the single-vessel pole: owner-side management with crew, procurement, and compliance for one ship
- **third-party technical managers** — one system run across many owners' fleets by a professional ship manager
- **maintenance-led entry tiers** — growing fleets starting with the register + maintenance + spares core, adding modules as they scale
- **performance-attached deployments** — the fleet record used as the data foundation for separate voyage/fuel/emissions optimization products
- **deployment shapes** — on-premise installations with scheduled exchange, cloud SaaS, and hybrids

A variant remains a **Variant** unless it changes users, core objects, workflow, or rules so much that the core model no longer applies — the cases that do are listed under Related Application Types.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Fleet Management System (road vehicles) | family sibling | shares the register + per-unit record + oversight pattern, but centers on drivers and live road telemetry; the marine Type is defined by the equipment-structured technical record, the crew-executed ship–shore loop, and class/statutory machinery the road core does not capture |
| Vessel Operations Platform | adjacent sibling | centers on voyage execution and operations (voyage lifecycle, operational reporting, performance monitoring) over the fleet record; the fleet record and workflow management stay with this Type |
| Ocean Freight Management | adjacent business system | manages the cargo business (bookings, chartering, freight documents); this Type manages the vessels as assets; suites may bundle both |
| Vehicle Telematics / vessel tracking services | data layer | acquire and publish position and sensor data; this Type is the management application of record over its own fleet |
| Fisheries Management | different record world | there the vessel is an authorized participant in a fishery's catch/entitlement records; here it is the owner's logistics/crew/maintenance asset; a fishing company may run both |
| Marina Management | facility side | manages berths, spaces, and the marina's rental business; this Type manages the owner's fleet |
| Boat / Yacht Charter Platform | demand side | sells vessel time-use to customers; yacht *management* (owner-side) is a single-vessel variant of this Type |
| Aircraft Maintenance Management | parallel domain | same register + usage-driven maintenance program + airworthiness/survey-record structure in aviation; different domain machinery |
| CMMS / Enterprise Asset Management | generic substrate | the maintenance module is a maritime CMMS; generic CMMS/EAM lack the vessel register, ship–shore loop, and class machinery |
| Mining / Robot Fleet Management | domain siblings | same oversight family pattern over production-cycle-centric (mining) or task-execution-centric (robots) fleets |

The most important boundary is with the **Vessel Operations Platform**: the test is the object of work. Remove the voyage-execution and performance-monitoring layer and a marine fleet management system remains; remove the fleet's technical/crew/compliance record and only an operations surface remains. They are different Types that frequently ship together or integrate.

## Representative Products

- SpecTec AMOS (maritime asset management suite; class-approved planned maintenance)
- SERTICA by RINA (modular ship management: maintenance, procurement, HSQE, crewing, performance, reporting)
- MariApps smartPAL (multi-module ship management platform with segment editions)
- ZeroNorth ShipPalm (fleet-management ERP within a voyage/performance optimization platform)

The sample deliberately spans different philosophies: a maintenance-led incumbent, a class-society modular system, an ERP-style suite, and a performance-first vendor's fleet record. Several other established vendors in this market (including class-society software suites and long-standing ship-management ERPs) could not be reached during research and are not characterized here (see Sources).

## Sources

Research date: **2026-09-09**

- SpecTec — AMOS (maritime asset management) — https://spectec.net/ ; AMOS Maintenance — https://spectec.net/amos-software/amos-maintenance/
- SERTICA by RINA — Ship Management Software — https://www.sertica.com/ ; Maintenance (incl. PMS FAQ) — https://www.sertica.com/maintenance/
- MariApps — smartPAL — https://www.mariapps.com/smartpal/ ; company/product overview — https://www.mariapps.com/
- ZeroNorth — ShipPalm — https://zeronorth.com/shippalm ; platform overview — https://zeronorth.com/

> Sourcing limitation: several other representative vendors' official sites were unreachable from the research environment on 2026-09-09 (transport errors, 403/404/429 responses). No claims are made about those products. Precise operational details (exact status label sets, numeric limits, plan packaging, specific regulation configurations) are intentionally not stated in this document; such details remain in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison, and the historical / market-sample check are recorded in the paired Research Notes.
