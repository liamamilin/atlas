# Tower Management Platform

## Overview

A **Tower Management Platform** is the system of record a tower infrastructure owner uses to run a distributed portfolio of passive-infrastructure sites — the towers, rooftops, poles, and shelters on which mobile operators rent space and power for their equipment.

It exists because the tower business is, at its core, a leasing business run over physical structures: the owner acquires or builds sites, secures the land under them, rents space and power on them to multiple tenant operators, collects that rent, pays the land rent beneath, and keeps the structures maintained and safe — across hundreds to hundreds of thousands of sites. The platform holds the portfolio as persistent records and runs that commercial and operational life from a single source of truth.

Its boundary: it manages **passive** infrastructure and the business built on it. It does not run the active network (that is the domain of telecom network/OSS systems), and it is more than an asset register — the tenancy and lease structures are what make it a tower management platform rather than a site inventory.

## Users & Context

Primary users sit inside a tower company (towerco) or an operator's tower/infrastructure division:

- **Site / portfolio managers** — own the accuracy of the site records: what exists, where, what is mounted, what capacity remains.
- **Leasing / colocation managers** — run the tenant pipeline: inquiries, feasibility checks, contracts, equipment rights, onboarding.
- **Finance / billing teams** — generate tenant invoices from lease terms, pay ground landlords, track escalations, renewals, and receivables.
- **Operations & maintenance (O&M) / network operations staff** — schedule preventive maintenance, dispatch and track trouble tickets, manage inspections and audits.
- **Site acquisition and rollout teams** — find candidates, run surveys and permits, deliver new builds and portfolio acquisitions.
- **Field crews and contractors** — execute the work orders and record what they did on site.

Secondary external parties interact through portals or constrained views: **tenant operators** (submit requests, view their sites and equipment), **landowners** (view contracts and payments), and **contractors** (receive and close work orders).

The context is a capital-intensive, long-lived asset business: sites stay in the portfolio for decades, change owners through M&A, and accumulate tenants, contracts, permits, and equipment across that life. The platform is therefore built for permanence and auditability, not for short transactions.

## Core Model

### The Defining Core

The platform's world rests on three structures that only make sense together:

```text
Site Portfolio of Record
└── Site (identified location + structure + capacity)
    ├── Occupancy (tenants and/or equipment on the site, against capacity)
    └── Leases & Agreements
        ├── Ground lease(s) — the owner rents the land (money out)
        └── Tenant lease(s) — tenants rent space/power (money in)
```

- **Site** — the anchor object. A persistent, individually identified record for each piece of passive infrastructure: its location (geographic and postal), its structure type (ground-based tower, rooftop installation, pole, shelter), its physical characteristics, and its capacity — usable space, structural load, and power. Everything else in the system attaches to a site.
- **Occupancy** — who and what is on each site. A tenant's presence is recorded as an occupancy of defined space and power; the equipment a tenant is entitled to install (and actually installs) is recorded against the site. Occupancy is tracked against the site's finite capacity, because the number of tenants a tower can carry is limited by structure, space, and power.
- **Leases & agreements** — the commercial instruments, running in two directions. Inward: **ground leases** with landowners, under which the tower owner rents the land beneath its structures — a major recurring cost. Outward: **tenant leases** (often under master agreements with each operator), under which tenants rent space and power — the portfolio's revenue. Leases carry terms, rents, escalations, renewal and termination provisions, and critical dates; tenant billing is derived from them.

These three are jointly load-bearing. Sites without occupancy and leases are just a map. Leases without sites are lease administration. Occupancy without leases has no commercial basis. The platform exists to hold all three as one reconciled record.

### Standard Capabilities

Mature products commonly add the following around that core. They make the platform practical, but they do not define it:

- **Colocation order management** — a managed pipeline from tenant inquiry through feasibility/capacity check, reservation, contract, equipment-rights recording, installation, and billing start.
- **Rollout and acquisition projects** — candidate identification, surveys, permits, construction milestones, acceptance for new sites; due-diligence and lease novation workflows for acquired portfolios.
- **Operations & maintenance** — preventive maintenance schedules, inspections and audits, trouble tickets, and fault tracking against sites and equipment.
- **Field and contractor work management** — work orders dispatched to internal crews and contractors, with completion evidence (photos, checklists, scanned identifiers) captured at the site.
- **Site access control** — planning, approving, and logging site visits; verifying visitor certifications; integrating with electronic locks in some implementations.
- **Billing and revenue management** — a billing engine that turns lease terms into tenant invoices (rental, energy and other pass-through costs, discounts, taxes, multi-currency), plus the rent roll payable to landlords.
- **Per-site document dossier** — leases, permits, drawings, photos, and correspondence attached to the site record and searchable.
- **Portfolio map / GIS view** — the portfolio on a map with drill-down into any site.
- **Vendor and contractor management** — onboarding, contracts, insurance, and performance tracking for the companies that build and maintain the sites.
- **Reporting and role-based dashboards** — portfolio health, tenancy, revenue, maintenance backlog, lease expiries.
- **External self-service portals** — constrained views and actions for tenants, landowners, and contractors.
- **Platform configuration** — configurable workflows, forms, roles, and permissions, because every towerco's processes and contracts differ.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:  Site of record
Implementations:  site/tower/location records with GIS coordinates; hierarchical
                  site→asset structures; rooftop vs greenfield vs special-structure types

Concept:  Occupancy
Implementations:  tenancy records with space/power allocation; equipment rights
                  derived from contracts; physical equipment holdings captured from
                  rollout, colocation, and field processes

Concept:  Lease / agreement
Implementations:  ground leases with landowners; tenant leases under master
                  agreements (MLAs) and individual site agreements; infrastructure
                  sharing agreements (ISAs); permits tracked alongside

Concept:  Capacity
Implementations:  space/aperture on the structure; structural load (weight, wind,
                  ice); power allocation and measured consumption
```

## How It Works

### Build or acquire the portfolio

```text
Identify candidate location
→ survey and validate
→ secure permits and the ground lease with the landowner
→ build the structure (project with milestones and acceptance)
→ site enters the portfolio as a managed record
```

Acquired portfolios follow a parallel path: due diligence, data capture, and novation of existing leases into the platform so the incoming sites, tenants, and land obligations become managed records.

### Onboard a tenant (the colocation loop)

```text
Tenant inquiry / request for a site
→ feasibility check against the site's remaining space, load, and power
→ reservation of the capacity
→ contract executed (under a master agreement where one exists)
→ equipment rights recorded on the site
→ installation performed and confirmed
→ billing starts against the lease terms
```

This loop is the revenue engine of the tower business: each additional tenant on an existing site adds revenue at marginal cost, so the platform's job is to make capacity visible and the path from inquiry to billed tenancy short and controlled.

### Operate the leases in both directions

```text
Tenant side:  lease terms → periodic invoices (rent, energy/pass-through, discounts, tax)
              → escalations on schedule → renewals and terminations on critical dates
Landlord side: ground-lease terms → periodic rent payable
              → renewals and renegotiations on critical dates
```

Money flows in from tenants and out to landowners, and the two are linked: in some markets, ground-rent costs above agreed thresholds and measured energy consumption are passed through to the tenants on the site.

### Keep the sites serving

```text
Preventive maintenance schedule → planned work orders
Fault / alarm / inspection finding → trouble ticket
→ dispatch to crew or contractor (with site access arranged)
→ on-site execution with completion evidence
→ closure recorded against the site and its equipment
```

Some implementations add remote monitoring of site power, fuel, security, and environmental conditions, feeding the same ticket flow.

### Reconcile occupancy against contracts

The behavior that binds the whole model together: the platform continuously reconciles **what is physically on each site** against **what the contracts say should be there and what is being paid**. Equipment installed without a matching right is unbilled occupancy; rights billed but not installed are disputes waiting to happen; land occupied without a current ground lease is a legal exposure. This reconciliation — in both the tenant and landlord directions — is the reason the site, occupancy, and lease structures live in one system rather than three.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Portfolio map / list

The entry surface. The portfolio on a map or as a searchable list, filterable by region, status, structure type, or availability.

- typical information: site identity, location, structure type, tenant count, capacity availability, status
- primary actions: search, open a site, start a rollout or acquisition activity

### Site record (the dossier)

The center of gravity. One site with everything attached.

- typical information: location and structure details, capacity and remaining availability, tenants and their equipment rights, installed equipment, leases (ground and tenant), permits, documents and photos, open work orders, revenue and cost
- primary actions: update site data, record equipment changes, open work orders, attach documents, evaluate colocation feasibility

### Colocation pipeline

The tenant-onboarding surface.

- typical information: inquiries and requests, feasibility results, reservations, contracts in progress, installations pending, activations
- primary actions: run feasibility, reserve capacity, progress contract, record equipment rights, activate billing

### Lease records

The commercial surface, in both directions.

- typical information: parties, term, rent and escalation schedule, critical dates (renewal, termination, notice), payment history, linked sites and equipment rights
- primary actions: abstract and update lease data, generate invoices or payment runs, action renewals and terminations, reconcile payments

### Billing workbench

- typical information: billing cycles, invoice runs by tenant and contract, pass-through cost inputs (energy, ground rent), discounts and taxes, receivables status
- primary actions: generate and adjust invoices, handle disputes, track revenue by customer, region, and site type

### Work management

- typical information: preventive schedules, trouble tickets, work orders by site, assignee (crew or contractor), status, completion evidence
- primary actions: create and dispatch work orders, approve site access, verify and close work

### Administration / configuration

- typical information: workflow definitions, forms and fields, roles and permissions, notification rules
- primary actions: configure processes, manage users and access, bulk-import data

### External portals

Constrained surfaces for tenants (submit requests, view own sites and equipment), landowners (view contracts and payments), and contractors (receive and close work orders).

## Important Rules / Behaviors

- **Capacity is finite and shared.** A site can carry only so much space, structural load, and power. Colocation feasibility is evaluated against remaining capacity, and reservations hold capacity against pending contracts.
- **Billing follows contracts; contracts follow the site record.** Tenant invoices are derived from lease terms and the equipment rights recorded on the site — not from free-form entry. Escalations, discounts, pass-through costs, and taxes are applied as the contract defines.
- **Money runs in two directions and the directions are linked.** Tenant rent is revenue; ground rent is cost. Pass-through arrangements (energy consumption, ground-rent thresholds) make one side's cost the other side's charge, so both lease populations must be accurate in the same system.
- **Occupancy truth is reconciled against contract truth.** Installed equipment is checked against contracted rights; discrepancies are revenue leakage or dispute risk. Products commonly treat this reconciliation as a first-class control, not a report.
- **Site access is controlled and attributed.** Visits are planned and approved against work, personnel certifications are tracked, and entries may be logged — because towers are critical infrastructure with safety and security obligations.
- **Records outlive projects and tenants.** Sites persist beyond the rollout project that built them and beyond any tenant's occupancy; leases, permits, and equipment history accumulate across decades and ownership changes.
- **State names vary.** Lifecycle labels for sites, tenancies, work orders, and leases differ per product and per customer configuration; the conceptual states (candidate → built → serving; requested → contracted → installed → billed; open → closed) are stable even where labels are not.

## Variants

- **Towerco pole vs operator-owned pole.** The classic user is an independent tower company whose tenants are operators. Operators that still own towers use the same structures with the tenancy layer thinned to their own equipment; the ground-lease and site-operations layers remain central.
- **Energy-heavy emerging-market variant.** Where grid power is unreliable, site power becomes a first-class concern: generators, batteries, fuel logistics, pilferage control, and energy pass-through billing push energy management and remote monitoring deeper into the platform.
- **Regulatory-heavy markets.** Some markets layer strict permitting, structural-safety, insurance, and regulator-reporting obligations onto the portfolio; permit tracking and compliance checklists grow from a supporting feature into a major surface.
- **Adjacent infrastructure on the same platform.** Fiber routes, transmission links, small cells, and DAS are managed by some products with the same site-and-agreement grammar, turning the tower platform into a broader passive-infrastructure platform.
- **Scale tiers.** Products range from small regional towercos (hundreds of sites, often replacing spreadsheets) to tier-1 portfolios (tens of thousands to hundreds of thousands of sites), with configuration, bulk operations, and multi-country reporting scaling accordingly.
- **Deployment shape.** SaaS and on-premises deployments both exist; licensing is commonly sized by site count rather than user count.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Telecom OSS | adjacent | OSS runs the active network — services and the resources carrying them, fulfillment and assurance; tower management runs the passive-infrastructure leasing business. A towerco has no service to activate or assure; its product is space and power on structures. |
| Enterprise Asset Management / EAM | overlapping capability | EAM maintains an asset base (lifecycle, maintenance, work orders). Tower management runs a leasing business on top of the asset base; strip the tenancy and lease structures and what remains is EAM territory. |
| Property Management | neighboring grammar | Shares landlord/tenant/lease vocabulary, but the object differs: human occupancy of buildings vs equipment occupancy of infrastructure sites, plus structural capacity, colocation fulfillment, and site power/O&M. |
| Lease Administration | narrower | The lease layer alone, at administration/accounting depth. Tower management binds leases to physical sites and drives colocation fulfillment and site operations from them. |
| Telecom Inventory Management | different axis | Holds the estate of telecom services and equipment consumed or delivered (circuits, lines, network elements) reconciled to carrier/network reality; tower management holds passive sites and their occupancy reconciled to contracts. |
| Telecom Field Service | consumer relationship | The field-workforce system of record (work orders, crews, dispatch-to-closure). Tower management dispatches work into it; its own core is the site/tenancy/lease record, not workforce capacity. |
| Construction Project Management | module relationship | Rollout projects are one workflow inside tower management; the site portfolio persists beyond any project, and construction tools carry no tenancy or lease estate. |
| Site monitoring / IoT products | label collision | Products that only monitor tower equipment (power, fuel, lights, security) and raise faults sometimes use the "tower management" label; they lack the tenancy/lease layer entirely and are monitoring tools, not portfolio systems of record. |
| TowerCo BSS / lead-to-cash | commercial pole | Catalog-, order-, and billing-grade commercial chains for towercos; tower management holds the estate those transactions act upon. Depth of billing beyond lease-derived invoicing belongs to the BSS side. |

The most important boundary is against **Telecom OSS**: the two meet at "the network's physical infrastructure" but from opposite sides — OSS from the services the network delivers, tower management from the structures that host it and the leases that monetize them.

## Representative Products

- **Tarantula Red Cube** — vertical telecom site management suite used by large towercos; modules spanning location, site inventory, rollout, colocation, lease, billing, O&M, field force, site access, and acquisition.
- **NEXSYS-ONE** — modular infrastructure-management platform with a dedicated towerco configuration covering site acquisition through built-to-suit to tenant billing, plus field, vendor, monitoring, and access modules.
- **Accruent Siterra** — site-centric telecom site management from a real-estate/facilities software house; sites, assets, projects, and leases in one system of record.
- **OneVizion TowerVizion** — platform built on a native tower/tenant/lease data model; leases, tenants, billing, permits, colocation pipeline, and maintenance for mid-market to enterprise portfolios.
- **Xolas TMS** — small regional tower management system (Malaysia) with role-based views for telcos, tower suppliers, contractors, and landlords.

## Sources

Research date: **2026-09-10**

- Tarantula — Red Cube product page: https://www.tarantula.net/red-cube-telecom-site-management-software
- Tarantula — "Tower billing complexity — an opportunity in disguise": https://www.tarantula.net/blog/towerco-billing
- NEXSYS-ONE — Telecom Tower Companies: https://www.nexsysone.com/telecom-tower-companies/
- NEXSYS-ONE — Modules: https://www.nexsysone.com/modules/
- Accruent — Siterra product page and FAQ: https://www.accruent.com/products/siterra
- OneVizion — TowerVizion: https://onevizion.com/towervizion/
- Xolas — TMS product page (via search index; live fetch unavailable): https://xolas.io/

> Sourcing limitation: no public help-center or user-guide documentation was reachable for the sampled products on 2026-09-10; evidence comes from official product pages and vendor-published domain material. Precise operational details (numeric limits, default settings, exact state names, contract-form specifics) are intentionally not asserted in this document; they remain in the paired Research Notes.

Detailed product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
