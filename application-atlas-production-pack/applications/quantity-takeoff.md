# Quantity Takeoff

## Overview

A **Quantity Takeoff** application is the document-measurement system of preconstruction: it organizes a project's construction drawings (or models), lets an estimator measure the work directly on them — counts, lengths, areas, volumes — as traceable objects placed at their location on the document, and accumulates those measurements into a per-item schedule of quantities.

The defining structure is small:

```text
Project's construction documents (drawings / model)
└── On-document measurement objects (count / linear / area / volume)
    └── Running quantities accumulated per identified item
        └── The takeoff results — "how much of what" — handed to estimating
```

Everything else the category is known for — scale calibration, item and assembly catalogs, bid areas and zones, typical-repetition shortcuts, revision comparison, multi-user collaboration, AI-assisted measuring, even an estimate worksheet — is widespread in mature products but is an accretion around this loop, not what makes a product a takeoff application. A markup tool with no per-item quantity accumulation is not a takeoff application; a pricing tool that never measures from documents is an estimating application, not a takeoff application.

## Users & Context

The primary user is the person who must quantify a building or structure from its design documents before it is priced:

- **estimators** at general contractors and specialty subcontractors — measure their scope from bid documents to produce quantities for pricing; specialty trades (drywall, electrical, painting, roofing, concrete, plumbing, mechanical, flooring and others) each measure their own scope from the same plan set
- **quantity surveyors** in international practice — measure and present quantities in formal bills of quantities, often working directly from BIM models

Secondary users:

- **BIM managers / VDC staff** who set up model-based quantity extraction
- **chief estimators / preconstruction leads** who consume takeoff results across multiple bids; in the market's current shape they commonly review AI-produced first-pass measurements rather than perform every measurement themselves
- **collaborators and reviewers** — colleagues with view access, other estimators working the same takeoff concurrently

The work environment is deadline-driven bid work: a plan set arrives, the scope must be quantified before the bid date, and revisions can land at any time. This is why measurement speed, reuse of saved setups, and revision comparison are recurring themes across products — and why the takeoff is organized around a *project or bid*, not a standalone drawing.

## Core Model

### The Defining Core

Three structures, jointly held. Remove any one and the software stops being a takeoff application:

- **The project's construction documents as the dimensional source.** A takeoff project is, first, an organized set of the project's drawings — sheets and pages arranged, named, and grouped by discipline — or a project model. Quantities are *derived from* these documents, not typed in from memory. Without this, the software is a spreadsheet or a material calculator.
- **On-document measurement objects.** The act of measuring leaves a visible, selectable, editable object at its location on the document: a count marker on a fixture symbol, a traced run for pipe, a filled region for floor area, a volume with depth for a slab. This is the audit trail of the takeoff — every quantity in the results can be traced back to where and what was measured, and editing the object updates the quantity. Without this, quantities are just typed numbers.
- **Per-item quantity accumulation.** Measurements roll up into running totals organized by identified item or condition — the takeoff results, grouped by whatever structure the user works in. This schedule of "how much of what" is the deliverable. Without it, the tool measures but does not take off.

### What Gets Measured

Across the researched products, measurements fall into a stable set of quantity types:

- **counts** of repeated elements (fixtures, devices, doors)
- **linear quantities** — straight runs, segmented polylines, perimeters
- **area quantities** — floor and wall areas, with openings subtracted
- **volume quantities** — areas with a depth or height applied (concrete, excavation)

The item being measured — the takeoff item, condition, or markup subject — carries the measurement method, units, and any conversion factors (heights, depths, waste multipliers) so that what is traced on the sheet converts into the quantity the trade needs.

### Standard Capabilities of Mature Products

These are what make the core loop practical at bid volume; they are common across mature products without being the definition:

- **Scale calibration** — the 2D drawing is a scaled representation, so dimensional measurement requires setting (and verifying) each sheet's scale, commonly by calibrating against a known dimension; some products handle detail sheets at a different scale with separately scaled views of the same page. In model-based takeoff, dimensions come from the model geometry instead.
- **Item and assembly libraries** — saved catalogs of takeoff items with their measurement behavior, reused across projects; in the markup-tool pole, item identity lives in named markups with custom columns instead of a catalog.
- **Results surfaces** — a summary of accumulated quantities per item, sortable and groupable (by code, zone, floor).
- **Location segmentation** — bid areas or zones that partition quantities by room, floor, or building.
- **Typical repetition** — measure a typical room or floor once and multiply it across repeating instances and pages.
- **Revision handling** — overlay or compare drawing versions, identify what changed, and update affected quantities.
- **Annotations alongside takeoff** — dimension lines, text, highlighter, and clouds mark up the plan but deliberately do not feed quantities; products keep the two separate.
- **Export and reporting** — printed plans with takeoff shown, quantity reports, and export of quantities (commonly to spreadsheets) into estimating.
- **Concurrent collaboration** — shared takeoffs with per-user permissions and view-only seats for reviewers; changes tracked for accountability in some products.

### One Structure, Many Implementations

The core model is conceptual. Products implement each piece differently:

```text
Concept:          Construction documents as source
Implementations:  2D sheets (PDF, scanned, CAD) · 3D BIM models · both in one product

Concept:          Dimensional basis of measurement
Implementations:  calibrated sheet scale (2D) · model geometry (BIM)

Concept:          Item identity
Implementations:  named conditions with properties · catalog items and assemblies ·
                  named measurement markups with custom columns · model element types via mapping

Concept:          Quantity results
Implementations:  summary tabs · markups lists with legends · live-linked estimating
                  workbooks · exported spreadsheets
```

A reader who has only seen one shape — say, cloud 2D takeoff feeding a live estimate — should still be able to recognize a desktop tool, a markup-based takeoff, or a model-based takeoff as the same Type.

## How It Works

### Set up the takeoff project

```text
Create a project (the bid)
→ add the plan set: upload/import drawings or model files
→ organize sheets: name pages, group by discipline, collate revisions
→ set or verify the scale on each sheet (2D) / map model data (BIM)
```

The project is the container for both the documents and everything measured on them. Some products handle alternates and change orders as variations of the same takeoff.

### Measure the work

```text
Pick or create a takeoff item (condition) — "what am I measuring?"
→ choose the matching tool: count / linear / area / volume
→ trace, click, or fill on the sheet — a measurement object is placed at the location
→ the quantity accumulates on that item's running total
→ repeat across pages until the scope is covered
```

Measurement objects stay on the sheets, visually distinguished (commonly color-coded per item), and remain editable: stretching a traced area, splitting a linear run, or adding a vertex recomputes the quantity. Repeated symbols can be counted automatically by searching for them; enclosed regions can be filled to generate area measurements; in AI-assisted products, a first pass of measurements is generated automatically for the estimator to review, reassign, and correct — vendors position this as a head start to review, not a finished takeoff.

### Structure and refine the results

```text
Assign measurements to bid areas / zones (rooms, floors, buildings)
→ apply typical-area multiplication where layouts repeat
→ review the results summary: quantities per item, per location
→ handle revisions: overlay the new issue, find the changes, update affected takeoff
```

### Hand off to pricing

```text
Export the takeoff results (report / spreadsheet / live link)
→ estimating attaches rates and produces the price
```

Where takeoff and estimating are bundled, the same quantities flow directly into the estimate worksheet or live-linked workbooks. Where they are separate, the handoff is an export or a synchronization link. Either way, the takeoff's own deliverable is quantities — pricing is the next Type's job.

## Interfaces

The following surfaces are described conceptually; exact names and layouts vary by product.

### Project / bid list

The entry surface. Lists the takeoff projects with their status and basic details.

- primary actions: open a project, create a project, filter by status

### Plan / document organizer

The document substrate of the takeoff.

- typical information: sheets and pages, page names/numbers, discipline folders, revision issues
- primary actions: upload or import documents, organize and rename pages, compare or overlay revisions

### Takeoff surface (the main workbench)

The drawing window with the measurement toolset.

- typical information: the current sheet, page navigation, the takeoff item list with colors and running quantities, layers, the image legend of what has been taken off, measurement tool controls
- primary actions: set scale, select a takeoff item, place measurements, edit measurement objects, place annotations (non-quantifying), navigate pages

### Results summary

The quantity deliverable.

- typical information: accumulated quantities per item, grouped by zone/code/location; subtotals
- primary actions: review and regroup, drill into a quantity back to its measurement objects, export or print

### Estimate / handoff surface (in bundled products)

Where quantities meet pricing inside the same product.

- typical information: items with quantities, rates, extended costs
- primary actions: push takeoff quantities into the estimate, export quantities to estimating tools or spreadsheets

### Collaboration and administration

Project sharing with roles and permissions; item/library management; audit trails of changes — present in cloud products and mature desktop ones alike.

## Important Rules / Behaviors

### Scale governs dimensional accuracy

In 2D takeoff, every length, area, and volume is only as correct as the sheet's calibration, so products treat scale as a first-class setup step — including verification against a known dimension and separately scaled views for detail sheets. Counts are immune to scale; dimensional quantities are not.

### Measurements are objects, not annotations

Takeoff objects and plan annotations are kept distinct by design: annotations (text, clouds, dimension lines, highlighter) communicate but never feed quantities; takeoff objects always do. Deleting or editing a takeoff object changes the results; deleting an annotation does not.

### Quantities are live-linked to their measurements

Results are computed from the measurement objects, not entered beside them. Editing geometry, moving an object to another bid area, or applying a typical multiplication updates the totals — and a drawing revision, once compared and processed, updates the affected quantities in the same way.

### AI output is reviewed, not trusted

In AI-assisted takeoff, the generated measurements are presented as a first pass attached to the project's items, which the estimator reassigns, corrects, or rejects. The measurement objects remain the underlying record either way.

### The takeoff stops at quantities

No matter how deep the bundle, the takeoff's own output is "how much of what". Rates, markups, taxes, and bid prices belong to estimating; pursuit and award belong to preconstruction management.

## Variants

Common shapes of the Type in the current market:

- **dedicated desktop takeoff** — the classic shape: a licensed desktop tool organized around projects, conditions, and summary results, with estimating either internal-basic or in a sibling product
- **cloud takeoff + estimating bundle** — takeoff and live-linked estimating in one browser product with view-only collaboration seats; currently the most common packaging for specialty contractors
- **takeoff inside a markup platform** — a general PDF markup tool whose measurement and markups-list machinery doubles as a takeoff when measurements are accumulated per item and exported for pricing
- **model-based (BIM) takeoff** — quantities extracted from the model's geometry and data via mapping, alongside or instead of 2D sheets; common in quantity-surveying practice
- **AI-first takeoff** — automatic detection and measurement as the entry point, with the estimator as reviewer
- **regional practice variants** — US subcontractor bid culture vs international QS/BOQ practice, which shapes how results are grouped and presented (codes, zones, formal bills of quantities)

A variant remains a variant while the core loop — measure on the document, accumulate per item — is intact.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Construction Estimating | closest sibling | takeoff produces quantities; estimating attaches rates and produces money. Strip pricing from a bundle and a takeoff tool remains; remove measuring entirely from an estimator (template-driven tools) and it remains an estimator |
| Preconstruction Management | containing phase | the pursuit pipeline (find work, qualify, solicit, level quotes, award) consumes takeoff as one workstream; takeoff has no pursuit record, no solicitation loop, no award |
| Construction Cost Management / Project Controls | downstream governance | controls manage a cost/schedule baseline and variances during delivery; takeoff builds the pre-award quantity basis and holds no baseline |
| PDF Markup / Review Tools | capability overlap | review markup with occasional dimension queries is not takeoff; the Type begins when measurements systematically accumulate per item as the deliverable (the markup-platform pole legitimately straddles) |
| BIM Authoring / BIM Coordination | upstream | authoring creates the model geometry; coordination manages model information exchange; model-based takeoff only consumes model data for quantities |
| Construction Materials Management | downstream, post-award | materials management consumes required quantities and tracks purchased/delivered actuals; takeoff exists before award |
| Architecture / Civil / MEP Design | upstream authors | design tools may report volumes or schedules as a byproduct of authoring; the design loop, not measurement, is their center of gravity |

The sharpest seam is with Construction Estimating, because the market bundles the two constantly — the same vendor often sells them as one product. The discriminator runs in both directions: a measuring tool that produces only quantities and no price is still takeoff; a pricing tool that never measures from documents is still estimating. Bundling is packaging, not type identity.

## Representative Products

- **On-Screen Takeoff** (On Center / ConstructConnect) — classic dedicated takeoff tool; the shape whose vocabulary (conditions, bid areas, typical areas, summary tab) much of the market shares
- **STACK** — cloud takeoff + estimating bundle with AI-assisted measuring
- **Bluebeam Revu** — markup platform whose takeoff workflow represents the capability pole
- **RIB CostX** — quantity-surveyor-oriented 2D + BIM takeoff with live-linked estimating workbooks
- **PlanSwift** — desktop takeoff-and-estimate tool with formula- and template-driven trade extensions

## Sources

Research date: **2026-09-09**

- STACK Construction Technologies — product site: https://www.stackct.com/ ; Help Center (Takeoff & Estimate, incl. Plans & Takeoffs): https://support.stackct.com/hc/en-us
- On Center Software / ConstructConnect — product site and takeoff FAQ: https://www.oncenter.com/ ; On-Screen Takeoff User Guide: https://help.constructconnect.com/on-screen-takeoff-user-guide-68 (also hosting ConstructConnect Takeoff, PlanSwift, and Quick Bid user guides)
- Bluebeam — Takeoffs & Estimation workflow page: https://www.bluebeam.com/workflows/takeoffs-and-estimation/ ; Markups & Data: https://www.bluebeam.com/product/markups-and-data/ ; Technical Support portal: https://support.bluebeam.com/
- RIB Software — CostX product page (2D & BIM takeoff, model maps, auto-revisioning): https://www.rib-software.com/en/rib-costx

> Sourcing limitation: Autodesk Takeoff product documentation was not reachable from the research environment (multiple failed attempts on 2026-09-09); the model-based (BIM) pole is evidenced through RIB CostX's own 2D/BIM takeoff documentation instead. Parameter-level details (exact unit lists, per-project limits, pricing) are not stated in this document beyond what the reachable vendor pages assert; the estimate-side of bundled products is described only as far as the takeoff boundary.
