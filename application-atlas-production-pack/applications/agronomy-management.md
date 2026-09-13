# Agronomy Management

## Overview

An **Agronomy Management** application is the working system of the agronomy practice: it holds each client grower's **fields as identified records**, attaches the **agronomic evidence** gathered about each field (soil and tissue test results, scouting observations, yield and planting history), and turns that evidence into recorded **agronomic recommendations and crop plans** — which seed, fertilizer and crop-protection products to apply, at what rate, and when. Those recommendations are handed to execution as work orders, blend or application tickets, or operator tasks, and the completed applications are recorded back, building a season-over-season **field history** that becomes the basis for the next decision.

The defining structure is small:

```text
Grower / client registry
└── Identified field (per season and crop)
    ├── Agronomic observations & test data
    ├── Agronomic recommendation / crop plan (products, rates, timing)
    ├── Execution record (what was actually applied)
    └── Field-level history across seasons
```

The recommendation artifact is what makes this a distinct Application Type: remove it and the remainder is field or crop record-keeping. Remove the field-and-evidence layer and it is merely a recommendation generator. Everything the market commonly bundles — product catalogs, soil-sampling job machinery, variable-rate outputs, maps, compliance reporting, retail blending and dispatch — is standard capability or segment-specific extension, not the definition.

## Users & Context

Agronomy management is operated by organizations that make or support crop-input decisions for specific fields:

- **Agronomists / crop advisors** — the primary users. They review field evidence, record observations, and write recommendations and crop plans. They may work for an agricultural retailer or cooperative, for an independent consulting firm, or inside a larger farming operation.
- **Ag-retail operations staff** — sales staff confirm plans; dispatchers schedule application jobs; applicators and drivers carry out and complete them (in the retail operating model).
- **Growers** — the recipients of recommendations. In some collaborative products they review and approve recommendations or convert them into work for their own crews; they receive reports and records.
- **Operators / contractors** — execute field activities from assigned work orders using mobile tools.

The work context is seasonal and field-bound: recommendations are drafted before and during the season, soil samples are pulled from specific points in specific fields, scouting happens in the crop, and application jobs run on tight weather windows. Mobile field capture — often with offline support — is standard; office desks hold the planning, catalog and reporting work.

## Core Model

### The defining core

**Field.** The field is the unit of record. Every field belongs to a grower or operation, is identified (name, and in most products a boundary), and carries a crop and season context. All agronomic data — observations, test results, recommendations, applications — attaches to a specific field. Fields accumulate a history across seasons, which is the substrate every new recommendation starts from.

**Agronomic observations and test data.** The evidence base: scouting notes and photos taken in the crop, soil sample results, plant tissue results, planting and yield data, and imported precision layers (imagery, management zones). Test data typically arrives as structured results — sampled points or zones within a field — and is commonly rendered as map layers over the field.

**Recommendation / crop plan.** The professional judgment artifact and the center of the model. A recommendation is a recorded specification for one field: which products (seed variety, fertilizer materials, crop-protection products), at what rates, at what timing, with instructions for application. A crop plan is the season-level container — from a simple rotation up to field-by-field production plans — from which individual field recommendations are drawn. Recommendations may be written by hand from professional judgment or produced with algorithmic assistance from the field's test data, yield history, rotation, production goals and input budget; they may be flat (single rate) or variable-rate (rates that vary across zones within the field). The recommendation is also a record: it states what was *advised*, distinguished from what was *applied*.

**Execution record.** The recommendation becomes work — a work order, a blend or application ticket, or an assigned field activity — and the completed application is recorded back: product, rate, timing, who applied it. In retail products the execution chain is deep (blend tickets flow to application jobs and into invoicing); in advisory products the grower or a contractor performs the work and the record closes the loop. Either way, the system maintains the distinction and the linkage between what was advised and what was done.

**Grower/client registry.** Because recommendation-writing is a service performed across many clients, the system carries the client organizations and their farms/fields as the operating population. This holds for the retail and consulting variants; a grower-operated deployment inverts it (own fields, agronomist as invited advisor).

### Standard capabilities of mature products

These are widespread in current products and make the practice practical; they are not what makes the product an agronomy-management application:

- product catalog — seed varieties, fertilizer materials, crop-protection products with lot and variety detail
- recommendation builder with blanket and variable-rate modes, manual and equation/algorithm-driven
- soil-sampling machinery — sample jobs (zone, grid, composite), sample labels or numbering, lab-result import (files or integrated labs), results shown as data layers
- mobile scouting and observation capture with photos, usually working offline and syncing later
- maps and layers as a presentation surface, with boundary import/export
- planned-versus-actual tracking: input usage, per-acre costs, plan comparison
- compliance-oriented application records and standardized, exportable reports — often branded and shared with the grower
- role-scoped surfaces: agronomist/advisor, sales, dispatcher, applicator, grower each see their slice
- integrations with equipment data platforms and file interchange (machine data, shapefiles)

### One structure, many implementations

```text
Concept:            field as unit of record
Implementations:    named field, drawn boundary + field file, farm→field hierarchy

Concept:            recommendation artifact
Implementations:    field recommendation with products/rates/timing, nutrient prescription,
                    seed placement prescription, fertilizer blend request

Concept:            execution handoff
Implementations:    work order / field activity (advisory), blend ticket + dispatch job (retail),
                    application card or map handed to an operator (consulting)

Concept:            test data
Implementations:    structured lab results (uploaded files or integrated labs),
                    sampling points/zones drawn on the field, imported precision layers
```

A reader who has only seen one variant — for example an ag-retail product where recommendations become blend tickets — should still be able to recognize a consultant's prescription tool or a collaborative advisory platform as the same Application Type.

## How It Works

### The seasonal loop

The canonical loop runs per field, per season:

```text
Establish the field record (grower, field, crop, season)
→ gather evidence (soil/tissue sampling jobs, lab results, scouting visits,
   prior-year yield and application history)
→ write the plan and field recommendations (products, rates, timing)
→ hand the recommendation to execution
   (work order / blend ticket / application job / operator assignment)
→ record what was actually applied
→ accumulate it into the field's history
→ the next decision starts from the updated record
```

### Building the evidence base

Soil sampling is the archetypal evidence workflow. The agronomist creates a sampling job on a field — grid, zone or composite — which defines where samples are pulled and generates the labeling (bag labels or sequential numbering) that keeps each sample traceable to its point on the field. Samples go to a laboratory; results return as structured data, either uploaded from files or delivered through lab integrations, and are attached to the field as layers or tables. Scouting observations and photos are captured in the field on mobile devices, typically with offline support, and join the same field record.

### From plan to recommendation

A crop plan (season scope) is progressively detailed into field-level recommendations. Each recommendation names products from the catalog with rates and timing. Variable-rate recommendations are derived from analysis layers — for example productivity or yield layers — computed by equation or authored manually, or imported from third-party prescription sources. In products with algorithmic assistance, the system formulates the prescription from the field's chemistry, history, goals and budget, and the agronomist adjusts parameters and compares outcomes before committing.

### From recommendation to execution

The retail model: pre-season plans are converted, when timing is right, into blend and delivery tickets; tickets become scheduled application jobs assigned to applicators; applicators see their jobs on mobile apps, navigate to the field, and start and complete them; completed jobs flow back as application records and, where the retail suite is integrated with accounting, into invoicing. Dispatch surfaces show job lists and schedules, applicator locations, priorities and statuses.

The advisory/collaborative model: the grower receives the recommendation, approves it or has it converted into a work order, and assigns it to staff or contractors; completion is recorded from mobile devices, and in some products a completed activity automatically becomes the compliant application record.

The consulting model: the prescription itself — application cards or maps — is the deliverable handed to whoever operates the equipment; the consultant's system keeps the evidence and the prescription, and may not capture the application.

### Reporting and the next season

Standardized records support reports for growers and for compliance programs — application reports, soil tests, crop planning summaries, yield maps — often assembled into shareable report sets. Planned-versus-actual views compare what was recommended against what was applied and what it cost. Because every element was attached to the field, the accumulated multi-year history — what was grown, what was tested, what was recommended, what was applied — is the starting evidence for the following season's plan.

## Interfaces

### Field map / fields view

The home surface for field-centric work.

- fields under a farm or client, with boundaries and a layer or status rendering
- typical information: crop, acres, current season, recent activity, layers available
- primary actions: open a field, create a sampling job, record an observation, view or build a recommendation

### Field record / field history

The longitudinal record of one field.

- typical information: crop and season context, soil and tissue results, scouting entries and photos, recommendations issued, applications recorded, prior-season layers
- primary actions: add an observation or event, review a season, compare layers, start a new plan

### Recommendation / plan builder

Where professional judgment is recorded.

- typical information: field and crop, product list from the catalog, rates (flat or by zone), timing, instructions, plan-versus-budget figures
- primary actions: create recommendation, apply rates, set timing, submit for approval, convert to work

### Execution surfaces

Job and activity machinery, varying by operating model.

- job list and schedule (status, priority, customer, field, products, dates); map-based scheduling in retail dispatch; applicator mobile views (assigned jobs, details, start/complete); grower approval views in collaborative products
- primary actions: create ticket/work order, assign, update status, record completion

### Sampling and lab data

- typical information: sampling jobs by type, sample points or zones, labels, lab results per point/zone, result layers
- primary actions: create sampling job, print/track labels, upload lab results, view as layers

### Reporting

- typical information: application reports, soil test reports, plan summaries, yield maps
- primary actions: assemble report sets, brand and share with the grower (PDF/print/email/portal)

## Important Rules / Behaviors

- **Advised versus applied are distinct records.** The system maintains the recommendation as a statement of intent and the application record as a statement of fact; planned-versus-actual comparison depends on this separation.
- **Every data element belongs to a field.** Sampling points, observations, recommendations and applications are attached to a specific identified field — this is what makes the history usable for the next decision.
- **Samples must stay traceable.** A soil or tissue result is only usable if it maps back to where the sample was taken; products therefore bind sample labels/numbering to field points or zones.
- **Recommendations are versioned or statused through their lifecycle.** Drafted, approved, converted to work, executed, or revised — some collaborative products expose approval explicitly; retail products expose conversion (plan → blend ticket) and job status explicitly.
- **Execution data flows back automatically where possible.** Completed jobs or activities become application records without re-entry; in integrated retail products the same records continue into invoicing.
- **Role-scoped visibility.** Agronomists, sales, dispatch, applicators and growers each see a different slice of the same underlying record; the grower's view is a deliberate subset of the advisor's.

## Variants

- **Ag-retail / cooperative agronomy** — the recommendation flows into the retailer's own fulfillment: fertilizer blending and formulation, blend tickets, applicator dispatch, and invoicing handoff. Execution machinery is deepest here.
- **Independent crop consulting** — the consultant serves many grower clients; the prescription (cards, maps, budgets) is the deliverable; formulation/dispatch machinery is typically absent.
- **Collaborative advisory platforms** — grower and advisor share one system; recommendations carry explicit approval loops and convert directly into the grower's operational records.
- **Grower-internal agronomy** — a large farming operation runs the same practice on its own fields, with its own agronomy staff.
- **Precision-forward deployments** — variable-rate prescription building from analysis layers and machine-data exchange dominates the usage; the underlying recommendation core is unchanged.
- **Deployment-era variants** — cloud suites dominate today's market, but the defining loop is older: paper recommendation slips backed by soil-test reports, and later desktop recommendation writers, satisfy the same structure without any of the modern machinery.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Farm Management Platform | adjacent, overlapping | centers whole-farm operations — finance, inventory, labor, equipment; agronomy management centers the input-decision practice on the field record. Many vendors ship both under one product family. |
| Precision Agriculture Platform | adjacent, gradient | centers the variable-rate execution loop (prescription → machine → as-applied verification) with equipment data as a first-class citizen; agronomy management centers the professional recommendation practice, of which VRT prescriptions are one output form. |
| Agricultural GIS | adjacent | centers the spatial land base, layers and spatial analysis; map-layer analytics without a recommendation lifecycle is GIS, not agronomy management. |
| Crop Management | adjacent, gradient | centers the crop cycle — planting, growth, harvest operations per field; agronomy management centers what to plant and apply, at what rate and when. Both sit on the same field record. |
| Nutrient / Crop Protection / Soil Management | narrower siblings | each centers a single input domain; agronomy management integrates across domains in one field-level recommendation. |
| Agribusiness ERP | adjacent (retail segment) | in ag retail, agronomy operations are sold as modules of an integrated ERP with books, inventory and invoicing at the center; agronomy management is the practice without the financial core. |
| Farm Equipment Telematics | upstream data source | captures machine operations; contributes as-applied and field-operation data, does not manage recommendations. |

## Representative Products

- Agvance Agronomy (SSI) — ag-retail agronomy suite: planning, mapping, blending, dispatch, invoicing handoff
- Agworld (Semios Group) — collaborative platform with a dedicated agronomist solution: plans, recommendations, approvals, automatic application records
- E4 Crop Intelligence Software — consulting-suite modules: field data, scouting, fertility and seed prescriptions, planning and budgeting

## Sources

Research date: **2026-09-06**

- Agvance — https://agvance.net/ , https://agvance.net/products/agronomy , https://agvance.net/products/agronomy/blending , https://agvance.net/products/agronomy/dispatch , https://agvance.net/products/agronomy/mapping
- Agworld — https://www.agworld.com/ , https://www.agworld.com/solutions/agronomists , https://www.agworld.com/products/activity-management/ , https://help.agworld.com/en/collections/1474249-soil-sampling
- E4 Crop Intelligence — https://e4cropintelligence.com/ , https://www.e4cropintelligence.com/agronomy-services/e4-software/fertility-rx/
- Boundary reference — https://www.myfarmweb.com/

> Sourcing limitation: Agvance and E4 had no reachable Tier-1 help centers during research (support subdomains empty or absent); their mechanics are asserted at official product-page level, and precise operational details (status names, numeric limits, defaults) are intentionally not stated. One additional candidate vendor (Agrian) was unreachable and was dropped rather than filled from memory. Detailed evidence, the cross-product comparison, and the boundary analysis are recorded in the paired Research Notes.
