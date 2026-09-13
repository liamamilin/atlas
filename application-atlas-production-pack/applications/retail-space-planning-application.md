# Retail Space Planning Application

## Overview

A **Retail Space Planning Application** is the merchandising application whose object of record is the physical selling space itself: it models a store's fixtures and shelves as measured structures, composes **planograms** — explicit arrangements that assign specific products to specific positions on that space — informed by product performance data, and carries those layouts to stores for implementation and verification.

The defining structure is small:

```text
Store selling space (modeled, measured)
└── Fixtures / shelves (real dimensions)
    └── Planogram (product-to-position arrangement)
        └── Placement decisions informed by performance data
```

Everything else commonly associated with the category — store-level floor planning, automated per-store planogram generation, distribution portals, photo-based compliance checking, 3D visualization — is widespread in current products but is not what makes the product a space planning application. A planner working from measured shelf sketches, a product list, and sales figures satisfies the same core.

The Type sits in the retail merchandising family between decision disciplines and execution: assortment planning decides *what* is offered in each store, category management steers the *commercial strategy* of each category, and space planning decides *how the offered products physically sit on the shelf* — then hands the layout to stores to implement.

## Users & Context

Primary users work at retailer head office:

- **space planners / space management teams** — own the store layout and shelf standards; titles such as "Space Planning Manager" and "Head of Space Management" are common in the market
- **category managers** — compose and maintain the planograms for their categories, usually against an agreed assortment and category strategy
- **merchandising analysts** — run the performance analysis that drives space reallocation

A second major user group works supplier-side: **CPG manufacturer account teams** build planograms for their categories as pitch and compliance artifacts aimed at retailer customers. Most established products serve both sides.

Store staff are downstream users rather than planners: they receive published planograms, implement them on the floor, confirm implementation, and often photograph the result. Field or audit teams may verify compliance across store regions.

The work context is head-office planning cycles (seasonal resets, range changes, reconstructions) connected to a continuous in-season loop of updates, store feedback, and compliance monitoring.

## Core Model

### The Defining Core

**Modeled selling space.** The application represents the store's selling space as a structure of fixtures — shelving units, gondolas, freezers, tables, pallets, hanging systems — each carrying real dimensions: width, depth, number of shelves, shelf heights. This measured space is the canvas on which everything else is composed. Without it there is no space planning, only product lists or freehand drawings.

**The planogram.** The central object of record: a defined arrangement that assigns specific products to specific positions on a fixture — which shelf, which horizontal segment, how many facings (side-by-side copies of a product). A planogram is typically visualized with product images drawn to scale on the fixture, so a reader can see exactly what the shelf should look like. Planograms are the artifact the application produces, exchanges, evaluates, and versions.

**Performance-informed placement.** Space is treated as a scarce, allocatable resource. Placement decisions are informed by product performance data — sales history and related measures — and evaluated against it: fast-moving products earn space, slow movers give it up, and the layout is revised as performance changes. This binding between placement and performance is what separates the Type from generic drawing tools.

### Standard Capabilities

Mature products commonly add the following around the core. They make the application practical at chain scale but do not define it:

- **Macro space / floor planning** — the store-level layer: dividing the sales area into sections, laying out categories across them, and placing fixtures; heatmap overlays of category performance, floor and gondola reports, and cross-category optimizers that recommend space allocation. Floor plans link downward to planograms (fixtures on the plan carry the planograms attached to them).
- **Store-specific planogram generation** — templates and rules from which the system generates a tailored planogram per store, fitted to that store's fixture dimensions and local sales, replacing or augmenting the older practice of sharing one cluster-level planogram for many different stores.
- **Distribution to stores** — publishing planograms to a store-facing web or mobile surface, with notifications, implementation dates, and visualizations of what changed versus the previous version.
- **Compliance verification** — store confirmation of implementation, photo documentation of the shelf, increasingly automated image recognition that scores compliance, and follow-up tasks when shelves do not match the plan.
- **Planogram performance analysis** — sales-per-space views across planograms, before/after comparisons of layout changes, floor-level reports.
- **Product and fixture data foundation** — product records with images and physical dimensions; a category hierarchy as the organizing structure; a reusable library of fixture types.
- **Integration** — sales, stock, and price data flowing in from ERP/BI systems; product-placement data flowing back out; linkage to assortment and category planning outputs.
- **Sharing of finished planograms** — planograms leave the system as reviewable, printable, or exportable artifacts for stores and supplier pitches (exact mechanisms vary by product).

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:   Modeled selling space
Realized as:  floor-plan editors with layers, fixture libraries,
              CAD/DWG imports of store technical plans, 3D store models

Concept:   Planogram
Realized as:  scaled shelf diagrams with product images, printable PDFs,
              web previews for stores, versioned planogram records

Concept:   Performance-informed placement
Realized as:  sales history, demand forecasts, days-of-supply targets,
              per-store availability checks, margin and priority rules
```

A reader who has only seen one implementation — say, an AI planogram generator — should still be able to recognize a spreadsheet-era planner or a manually drawn planogram process as the same Type.

## How It Works

### Build the data foundation

```text
Import products (records with images and physical dimensions)
→ organize them into a category hierarchy
→ register stores
→ define fixture types with real measurements
```

Product images and dimensions matter because the planogram must look like the shelf and fit the shelf.

### Plan the macro space

```text
Draw or import the store floor plan
→ divide the sales area into sections
→ allocate categories to sections (informed by performance heatmaps)
→ place fixtures in each section
→ attach planograms to fixtures
```

Not every deployment uses this layer — planogram-only tooling exists — but in integrated products the floor plan is where category-level space decisions are made and where planograms find their physical home.

### Compose planograms

```text
Select a fixture
→ place products on shelves (manually, or by rules/templates)
→ set facings and positions
→ check fit against the fixture's real dimensions
→ review and approve
```

Composition ranges from manual drag-and-drop drawing to rule-driven generation: instead of placing every product by hand, the planner expresses intent — a shopper's decision-tree order, priority for high-margin or high-velocity items, days-of-supply targets — and the system arranges products accordingly, always within the physical dimensions of the fixture.

### Tailor planograms to stores

```text
Start from a template or cluster-level planogram
→ generate a store-specific version
   (fitted to that store's fixture dimensions,
    adjusted to that store's sales and availability)
→ substitute locally unavailable products where needed
```

This step exists because stores differ. A planogram drawn for an 80 cm shelf cannot be implemented on a 76 cm shelf — one product's documentation states the rule concretely, warning that a planned product may then simply not fit. Store-specific tailoring turns the planogram from an ideal into an implementable instruction.

### Distribute, implement, verify

```text
Publish planograms to stores (web/mobile; no local install needed)
→ stores are notified; implementation dates are set
→ store implements the shelf and confirms
→ store (or field team) photographs the implemented shelf
→ compliance is checked — manually or by image recognition
→ discrepancies create follow-up tasks
```

The loop closes at the shelf. Verification distinguishes an empty position caused by out-of-stock from one caused by non-implementation — two different problems with different owners.

### Analyze and re-plan

```text
Measure performance of the laid-out space
→ compare before/after layout changes
→ reallocate space toward what sells
→ revise planograms and floor plans
```

Space planning is cyclical: layouts are revised as assortments, seasons, and performance change.

### Capability tiers

**Defining core** — without these, not space planning:

- modeled, measured selling space (fixtures/shelves)
- planogram: explicit product-to-position arrangement
- placement informed and evaluated by performance data

**Standard capabilities** — present in most mature products:

- macro space / floor planning
- store-specific planogram generation
- distribution to stores
- compliance verification
- planogram performance analysis
- product/fixture data foundation and integration
- sharing of finished planograms (print/export)

**Optional / variant** — depends on product and deployment:

- 3D store models and digital twins; CAD/DWG interoperability
- AI-generated planograms from natural-language intent
- image-recognition compliance
- structured approval workflows with dedicated reviewer roles
- adjacent machinery in the same platform: shelf labels, POS printing, store communication forms, task management, replenishment linkage

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Planogram editor

The primary authoring surface: a scaled drawing of a fixture with shelves, product images placed in positions, dimension controls, and fit checking against the fixture's real measurements. Primary actions: place/move/remove products, set facings, apply rules or templates, validate fit, save versions.

### Floor plan editor

The store-level surface: the sales area drawn to scale (sometimes over an imported technical plan), sections and fixtures placed on layers, category allocations shown and colored by performance. Primary actions: draw/arrange sections and fixtures, attach planograms, overlay heatmaps, run space-allocation optimization.

### Planogram library

The managed collection: planograms organized by category, store or cluster, and version, with status (draft, approved, published) and history. Primary actions: search, open, duplicate, version, approve, publish.

### Store portal

The store-facing surface, typically web or mobile with no local installation: current planograms for that store, visual diffs against the previous version, implementation dates, confirmation, and photo upload. Primary actions: view, confirm implementation, photograph the shelf, respond to tasks or questionnaires.

### Compliance dashboard

The head-office verification surface: implementation status across regions, stores, and categories; submitted shelf photos; compliance scores where image recognition is used; ranked lists focusing attention on the worst gaps. Primary actions: review, root-cause an empty position, create follow-up tasks.

### Analysis and reporting views

Performance of space: planogram-level and floor-level reports, before/after comparisons, category performance across the estate. Primary actions: run analyses, compare versions, export.

### Product and fixture libraries

Reference data surfaces: product records with images and dimensions; fixture types with measurements. Primary actions: import, edit, organize into hierarchies and libraries.

## Important Rules / Behaviors

### Physical fit is a hard constraint

A planogram must fit the fixture it is sent to. Products are pre-validated against real fixture dimensions; a layout that ignores the shelf's actual width produces shelves where planned products do not fit. This constraint is why the space model carries real measurements rather than schematic boxes.

### The planogram is a store-targeted instruction, not a suggestion

A planogram published to a store is an instruction to be implemented by a date. Sharing one generic planogram for stores with different fixtures forces store staff to improvise — a recognized failure mode that store-specific generation exists to remove.

### Space follows performance — and performance follows space

Placement decisions are expected to be justified by product performance, and layout changes are expected to move performance. The analysis layer exists to keep this loop honest: reallocation without measurement is treated as guesswork.

### Compliance is measured against the planogram, with causes distinguished

A shelf that differs from the planogram is a compliance gap, but an empty position has two distinct causes — the store lacks stock, or the store did not implement. Mature verification separates the two, because they route to different fixes.

### Planograms are versioned and changes are made visible

Stores see what changed versus the previous version; implementation dates control when the switch happens. The planogram is a living, versioned record of the shelf, not a one-off drawing.

## Variants

- **micro-only planogram tooling** — shelf-level planning without a floor-plan layer; common as an entry tier and for supplier-side users
- **integrated micro + macro space planning** — floor plans and planograms in one model; the typical retailer HQ configuration
- **retailer-side vs supplier-side operation** — the same objects serve retailer space teams and CPG account teams building category pitches; some deployments are joint
- **generation philosophy** — manual drawing; rules/template-driven automation; AI generation (including zero-base rebuilds, maintenance inserts, and re-spacing modes, sometimes driven by natural-language instructions)
- **store-estate posture** — unified chains served by cluster planograms vs non-unified store estates requiring per-store planograms
- **packaging** — standalone specialist products; modules of category-management suites; modules of retail planning platforms. Notably, some large enterprise retail suites do not sell a space planning product at all — the specialist market carries the Type
- **visualization depth** — 2D planograms only vs 3D store models and digital twins, the latter associated with reconstruction projects
- **adjacent machinery** — some platforms extend into shelf-label generation, POS label printing, store communication forms, and task management around planogram work

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Category Management Application | adjacent, heavily bundled | category management owns the category's ongoing commercial performance and strategy loop (roles, scorecards, reviews); space planning owns the physical shelf representation. Category strategy is an input to space planning; space is one tactic category management directs |
| Assortment Planning Application | upstream, feeds planograms | assortment decides what is offered, in which stores, at what depth, for a period; space planning decides how the offered products sit on the shelf. Assortment output is a key planogram input; shelf constraints can bound assortment |
| Retail Merchandising Platform | sibling (planning → execution handoff) | the merchandising system is the back-office system of record for items, acquisition, and stock; space planning owns shelf-layout objects. Planning decides the offering; merchandising creates items, cuts POs, and records actuals |
| Retail Inventory Management | different discipline | inventory management owns stock quantities and movements; space planning owns where products sit on the shelf. They share product data, not objects |
| Store Operations / Store Task Management | downstream consumer | store operations runs daily store work; implementing a published planogram becomes a store task, and compliance results feed back — but the layout objects belong to space planning |
| Space & Occupancy Management (workplace) | homonym only | workplace/facility space planning manages occupancy of offices and buildings; retail space planning manages product placement on selling fixtures. Same words, different universe |
| Diagramming / floor-plan drawing tools | capability overlap only | generic drawing tools can draw floor plans but carry no product records, no performance data, and no planogram object of record |
| Digital shelf / e-commerce merchandising | homonym risk | online ranking and presentation vs the physical shelf; the researched products are physical-space systems |

The closest boundaries are the two planning siblings above. The discriminator is the object of record: category management holds a category's performance/strategy view, assortment planning holds a period-bound offering plan, and space planning holds shelf-layout objects. Vendors frequently bundle all three, which creates product-level overlap without collapsing the Types.

## Representative Products

- **NielsenIQ Spaceman** — long-established space-management suite serving retailers and manufacturers globally; planogramming, automation, and compliance modules
- **DotActiv** — standalone category-management specialist with planogram automation, floor planning, planogram distribution, and image-recognition compliance
- **Quant** — integrated European space/category/planogram platform with documented end-to-end workflow from floor plans to store compliance

Market-structure note: enterprise retail-suite vendors have historically packaged macro space optimization with category management (one major suite's legacy planning product was literally named for both), and at least one such suite's current cloud portfolio lists no space planning product — the Type is carried primarily by specialists and category-management suites.

## Sources

Research date: **2026-09-07**

- NielsenIQ — Spaceman product page: https://nielseniq.com/global/en/solutions/spaceman/
- NielsenIQ — Spaceman Suite: https://nielseniq.com/global/en/landing-page/spaceman-suite/
- DotActiv — homepage: https://www.dotactiv.com/
- DotActiv — Floor Planning Software: https://dotactiv.com/floor-planning-software/
- DotActiv — Activ8 (planogram communication): https://dotactiv.com/planogram-communication-software
- DotActiv — Nova (planogram automation): https://dotactiv.com/nova-planogram-automation
- Quant — Overview: https://www.quantretail.com/en/overview
- Quant — Planogram Software: https://www.quantretail.com/en/planogram-software
- Quant — Retail Floor Planning: https://www.quantretail.com/en/retail-floor-planning
- Quant — Store Specific Planograms: https://www.quantretail.com/en/store-specific-planograms
- Quant — Planogram & Store Compliance: https://www.quantretail.com/en/planogram-store-compliance
- Quant — Manuals (KB): https://www.quantretail.com/en/kb and https://www.quantretail.com/en/kb/get-started/planograms-linked-with-floor-plans
- Oracle — Retail documentation index and On-Premise Applications page: https://docs.oracle.com/en/industries/retail/ , https://docs.oracle.com/en/industries/retail/onpremapps.html

> Sourcing limitations: Blue Yonder, RELEX, and Aptos product documentation could not be reached from the research environment (repeated 404/empty responses); no claims about them are made. One enterprise suite's legacy space/category product documentation is login/script-gated — only its name and packaging were observed. Most sampled evidence is official product-page depth; operational workflow detail is strongest for one product's published manuals. Vendor-published benefit percentages are marketing claims and are not asserted in this document. Precise numeric limits are stated only where a vendor's own documentation states them (the shelf-fit example).
