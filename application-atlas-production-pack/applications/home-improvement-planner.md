# Home Improvement Planner

## Overview

A **Home Improvement Planner** is a homeowner-side planning application: it holds the user's own home as the anchored subject, lets the homeowner compose improvement work as a defined, revisable project (which spaces, what work), and attaches a money plan to that work (estimates, budgets, contractor bids). Its job is to turn an intention — "redo the kitchen," "finish the basement," "add a deck" — into a plan the household can decide on, hire for, and carry through.

The defining core is small:

```text
The user's own home (anchored, persistent subject)
└── Improvement project (defined, revisable plan of work: spaces + work items)
    └── Money plan (planned cost: estimates / budget / bids)
```

Everything else commonly associated with this software — mood boards and idea collections, contractor matching and competitive bids, 3D design, home-value and ROI analytics, maintenance schedules, document storage — is standard capability that mature products add around this core. A paper-era homeowner with a sketch of the room, a clippings folder, a budget worksheet, and a folder of contractor bids satisfies the same core.

The Type is defined by whose plan it is. This is the homeowner's own planning surface — not the contractor's business system (Home Improvement Contractor Management), not the recurring-upkeep app (Home Maintenance Application), and not the whole-home information binder (Home Management Application).

## Users & Context

The primary user is a homeowner — often a couple or household — planning change-work on the home they live in, have just bought, or are preparing to sell. Three situations dominate:

- **Deciding** whether and what to improve: what a project would cost, what it might return, which of several ideas to pursue.
- **Hiring**: defining the work well enough to collect and compare contractor bids.
- **Doing it themselves (or a mix)**: organizing the work they will perform, tracking what gets done and what it cost.

Secondary users are co-owners and partners who share the plan, and family members in household-shared products. The context is long-lived: a project spans weekends to months, money is the binding constraint, and decisions are made from pictures, prices, and bids. Phones and web are both first-class surfaces; the plan is revisited repeatedly over its life.

## Core Model

### The Defining Core

Three structures, jointly held. Remove any one and the application stops being this Type:

- **The user's own home as the anchored subject.** A persistent, personalized record of the home — the property, its spaces and details, its records — that all planning hangs from. The plan belongs to *this* home. Without it, the product is a generic remodeling calculator, a content site, or a marketplace with nothing of the user's to plan on.
- **The improvement project as a defined, revisable plan of work.** The intended change-work — a renovation, remodel, addition, or upgrade — held as a scope: which spaces, which work items. The homeowner composes it, revises it, and carries it from idea toward execution. Without it, the product is a home journal or photo album of past work.
- **The money plan attached to the work.** Planned cost held against the scope: estimates (often per work item, sometimes with finish tiers), a budget, contractor bids, scenario comparisons. Money is the decision variable the planner exists to inform. Without it, the product is an idea board or a design toy.

These three are load-bearing together: a home record without projects and costs is a home binder; a project and budget without a home of record is a spreadsheet; a scope with pictures but no money is a mood board; a value dashboard with cost guides but no project is a data surface.

### Standard Capabilities

Mature products commonly add the following. They make the planner useful but do not define it:

- **Idea and inspiration collection** — mood boards, ideabooks, saved photos and products that feed the project's scope.
- **Hiring machinery** — pro directories and matching, request-for-bid flows, and bid-comparison support; sometimes vetting and expert guidance during the renovation.
- **Progress and completion logging** — photos, receipts, and completed-work records; completed projects can feed the home's record and sometimes its estimated value.
- **Document storage** — contracts, permits, manuals, and warranties kept with the home or project.
- **Work-plan layer** — task lists and schedules for the improvement work; strongest where the homeowner self-executes or tracks the job. When the work is hired out, the schedule usually lives with the contractor.
- **Sharing** — co-owner or partner access to the plan; household members in family-shared products.
- **Home-value linkage** — value estimates that respond to completed improvements; ROI framing for candidate projects.
- **Maintenance adjacency** — a maintenance planner or task list in the same product, held separate from improvement projects.

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:  the money plan
Implementations:  data-driven cost estimates with ROI and scenarios;
                  a priced shopping list generated from a design;
                  competitive contractor bids against a posted scope;
                  a project budget tracked inside a home binder

Concept:  the project scope
Implementations:  composition from a catalog of project types (kitchen, bath, deck…);
                  a posted project description written for bidding;
                  a spatial design of the space being changed;
                  a tracked project record on the home
```

A reader who has only seen one kind of product — say, a cost-estimator dashboard — should still be able to recognize the design-led and marketplace-led products as the same Type from the core model.

## How It Works

The canonical loop runs from intention to settled outcome:

```text
Anchor the home (claim/address the property; spaces and details)
→ collect ideas (photos, products, designs)
→ compose the project (spaces + work items)
→ attach the money plan (estimate/budget; scenarios; finish tiers)
→ decide and hire (match/contact pros; collect and compare bids)
   — or plan the do-it-yourself work
→ execute and track (photos, receipts, completed items; documents)
→ settle (final costs against the plan; value impact recorded)
```

**Deciding.** The homeowner starts from the anchored home. Ideas accumulate — saved photos, products, designs. Candidate work is composed as project scope, and the money plan is attached: data-driven estimators price project types (often with finish-tier options and ROI against the home's value); a design prices out as a shopping list; scenarios re-price the plan as choices change.

**Hiring.** When the work will be contracted, the scope and budget become the brief: the homeowner posts the project or contacts matched professionals, collects competing bids, and compares them — line by line where support exists. The accepted bid becomes the project's committed cost. Guidance during the renovation is a marketplace-pole service; the schedule and production themselves live with the contractor.

**Doing.** Where the household does the work, the planner may carry the task layer — steps, timing, materials — and tracks progress as items complete.

**Recording.** However the work happens, the record returns to the home: photos, receipts, documents, and completed projects. In products with value linkage, completed improvements update the home's estimated value; in binder-style products the whole record can be shared or transferred — for example to a buyer when the home is sold.

## Interfaces

The surfaces below are described conceptually; names and layouts vary by product.

### Home dashboard

The anchor surface.

- the property and its details, value context where offered, the project list, maintenance items
- primary actions: claim or edit the home, open or start a project, review value and condition

### Project workspace

Where one project lives.

- scope (spaces, work items), budget or bids, photos, documents, status
- primary actions: edit scope, attach estimate or bid, add photos and documents, mark progress

### Estimator / budget builder

Where the money plan is built.

- project-type catalogs, inputs (dimensions, finish tiers), cost and ROI output, scenario switching
- primary actions: select project type, adjust inputs, compare scenarios, save the estimate to the project

### Idea board / gallery

Where inspiration collects.

- saved images, products, designs, often grouped per project or room
- primary actions: save items, attach to a project, note preferences

### Hiring surface

Where pros and bids are managed.

- matched or searched professionals, bid requests, received bids, comparisons, messages
- primary actions: request bids, compare bids, contact a pro, record the accepted bid

### Design canvas (design-led products)

Where the scope is drawn.

- floor plan in 2D, furnished 3D view, item library, priced shopping list
- primary actions: draw or import the space, place items, price the design, render or share it

### Documents and records

The home's paper trail.

- contracts, permits, receipts, manuals, warranties; completed-project history
- primary actions: upload, attach to home or project, share

### Sharing and settings

- co-owner or viewer access, household members, transfer of the record (for example on sale)

## Important Rules / Behaviors

- **The plan is personal and persistent.** It belongs to the homeowner, survives across sessions and months, and outlives any single contractor relationship. Some products let the record transfer with the home when it is sold.
- **Money is the decision variable.** Estimates and bids exist to be compared; scenarios and finish tiers re-price the plan; products commonly advise a contingency reserve within the budget. The plan is revised as real prices arrive.
- **The plan precedes and survives execution.** Projects can be scoped and priced long before any commitment; completed work logs back onto the home and can feed its estimated value.
- **Improvement and maintenance are held apart but adjacent.** Products that carry both keep planned change-work separate from recurring upkeep tasks; the same home anchors both.
- **Hired work shifts the schedule to the pro.** The homeowner's plan holds scope, money, and choices; the production schedule typically lives with the contractor — in the contractor's own system, whose client portal the homeowner visits, rather than in the homeowner's planner.
- **Value and ROI figures are model-based guidance, not appraisals.** Products present them as estimates that respond to the data the homeowner maintains.
- **No standardized states.** Project statuses, bid stages, and labels vary by product and are usually product-defined.

## Variants

- **Estimation-led planner** — data-driven cost and ROI estimation against the home's value is the engine; hiring and maintenance attach to it.
- **Design-led planner** — the scope is expressed as a spatial design (floor plans, 3D, renders) with a priced shopping list; hiring is light (often a designer marketplace).
- **Marketplace-led planner** — the money plan is realized as competitive bids from vetted contractors, with expert guidance through the renovation.
- **Suite-embedded projects** — planning as a Projects module inside a whole-home management binder (documents, appliances, inventory, value).
- **Prep-to-sell framing** — light improvements selected and priced for sale speed and price.
- **Maintenance-adjacent packaging** — improvement planning bundled with a maintenance planner in one product.
- **Embedded distribution** — the planner white-labeled or bundled into banks', realtors', or inspectors' homeowner surfaces.

A variant remains a variant while the defining core holds. When the center of gravity shifts — to the contractor's business (Home Improvement Contractor Management), to recurring upkeep (Home Maintenance Application), to the whole-home binder (Home Management Application), or to pure space design — the product belongs to the neighboring Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Home Improvement Contractor Management | consumer/professional twins | the contractor's business system (leads → sale → production → money) vs the homeowner's own plan; a contractor system's client portal shows one job inside the contractor's record, while the planner holds the homeowner's plan across projects and contractors |
| Home Maintenance Application | adjacent sibling | recurring preservation of existing systems vs bounded, discretionary change-work; products bundle both, with separate machinery |
| Home Management Application | adjacent sibling | the whole-home binder/hub (documents, appliances, inventory, finance) vs the project-and-money plan; planning may be embedded as one module |
| Home Services Marketplace | hiring leg | discovery, matching, and booking of pros vs the homeowner's persistent planning record; marketplaces feed the planner's hiring machinery |
| Project Management Application | shared vocabulary | generic team project machinery (tasks, resources, schedule) vs a household's decisions about change-work on a home, with the money plan first-class |
| Budgeting Application | money overlap | whole-finances budgeting vs a money plan scoped to one project's work items |
| Travel Itinerary Planner | same pattern, other domain | a consumer planner of a bounded real-world effort; the subject differs (a home vs a trip) |
| Architecture / interior design tools | capability overlap | tools that plan the space (layout, furniture, visuals) vs this Type's plan of work and money; design-led products straddle the seam |
| Construction Estimating / Quantity Takeoff | capability supplier | trade-facing takeoff from plans vs consumer-facing cost guidance by project type |

## Representative Products

- Kukun (iHomeManager) — estimation-led planner: renovation cost and ROI estimation on the anchored home, with maintenance planner and contractor matching
- HomeBinder — suite-embedded planner: a home-management binder whose Projects tab plans, scopes, and tracks renovations, with value linkage
- Planner 5D — design-led planner: 2D/3D space design with mood boards and a priced shopping list
- Sweeten — marketplace-led planner: posted projects matched to vetted contractors with competitive bids and bid-comparison guidance
- Dwellin — boundary anchor: a maintenance-centered home-care log where improvements are recorded, not planned

The defining core was checked against the market's other known poles — dedicated renovation planners and inspiration platforms (HomeZada, Houzz, Block Renovation class) — which could not be reached during research; see Sources.

## Sources

Research date: **2026-09-08**

- Kukun — root, iHomeManager, and Remodel Cost Estimator pages — https://www.mykukun.com/ , https://mykukun.com/ihomemanager , https://mykukun.com/Home-Renovation-Costs
- HomeBinder — root page, Knowledge Base, and Homeowner Help Center (homeowner dashboard documentation) — https://www.homebinder.com/ , https://pages.homebinder.com/knowledge-base , https://pages.homebinder.com/homeowner-help-center-0
- Planner 5D — root page — https://www.planner5d.com/
- Sweeten — root page — https://www.sweeten.com/
- Dwellin — root and How It Works pages — https://www.dwellin.com/ , https://dwellin.com/app/how-it-works/

> Sourcing limitation: several major products in this category could not be accessed on 2026-09-08 — HomeZada (site blocked; archived snapshot unavailable), Houzz (site blocked), and Block Renovation (site defunct or moved). Claims in this document are calibrated to the five reachable products; no details of the unreachable products are asserted. Precise operational parameters (exact fields, statuses, limits, defaults) are not stated, since only one product's Tier-1 operational documentation was reachable. Detailed evidence, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
