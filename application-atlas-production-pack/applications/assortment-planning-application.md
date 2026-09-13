# Assortment Planning Application

## Overview

An **Assortment Planning Application** is the planner-facing application in which a retailer decides its product offering for a coming period: which products — at style/color/SKU level — to offer, in which stores or store groups and channels, and in what quantities. The output is a reviewable, financially sized plan that is handed downstream to buying (purchase orders) or to replenishment and allocation systems.

The defining core is small:

```text
Merchandise category
└── Assortment plan for a defined period (season)
    ├── Offering set — which options are offered (breadth)
    ├── Points-of-commerce assignment — which store groups carry them (localization)
    └── Planned depth — units to buy/carry, in units and value
```

Everything else commonly associated with these products — AI recommendations, planogram linkage, in-tool purchase orders, store collaboration apps, prepack logic, scenario tooling — is widespread in current products but is not what makes the product an assortment planner. A spreadsheet over last season's sell-through, a store grading, and an open-to-buy cap satisfies the same core; so do AI-heavy cloud suites.

When the object of record shifts — to category-level strategy (Category Management), to physical shelf layout (Space Planning), to money budgets without SKUs (Merchandise Financial Planning), or to continuous in-season stock movement (Replenishment/Allocation) — the product is drifting toward a different Application Type.

## Users & Context

Primary users sit in the retailer's merchandising organization:

- **Merchandisers / buyers** — own the product decision: which styles, brands, and items make the offering, and how deep to buy.
- **Category managers / assortment managers** — own a category's plan: its goals, its option counts, its performance, and the balance of the offering across the category.
- **Planners** — own the numbers: translating the offering into buy quantities, receipt timing, and financial reconciliation.

Secondary users:

- **Merchandising leadership** — reviews plans against targets and approves them.
- **Allocation and replenishment teams** — consume the approved plan as the basis for in-season execution.
- In some implementations, **store teams** — suggest local assortment changes through companion surfaces.

The working context is the retail planning calendar: most of the work happens pre-season, months before goods arrive, against last season's data and this season's financial targets. The plan is a decision object — nothing in the application sells, ships, or stocks anything; it decides what will be sold, where, and how much.

## Core Model

### The Defining Core

Four properties. If any one is removed, the product is no longer recognizable as an assortment planner:

- **Planned offering set (breadth)** — the retailer's decision, per category, about which product options are offered: added, kept, or dropped. The option is the offering unit: a style-color, an article, a SKU. Without the item-level offering decision, the product becomes a financial plan or a product data catalog.
- **Points-of-commerce assignment (localization)** — the offering is defined against the retailer's selling locations, grouped for planning (store clusters, grades, banners, channels). Even a uniform chain is planned through its location groups; the plan resolves to which locations carry which options. Without this, the product is a product list, not a retail assortment plan.
- **Period bound** — the plan is made for a defined timeframe on the retail calendar: a season, a quarter, an assortment period. Offerings carry over between periods, but every plan has a window. Without this, the product is catalog maintenance.
- **Planned depth in units and value** — the offering is sized: planned units to buy or carry per option per location group, measured in units, cost, retail value, and margin, and sized against the retailer's financial targets. Without quantities, the product is a listing exercise.

The application holds the plan as a **persistent, reviewable, versioned object** that passes through review and approval and is then handed to execution. The plan — not a transaction — is the center of the world.

### Standard Capabilities

Mature products commonly add these capabilities. They make assortment planning practical; they do not define it.

- **Hindsight analysis** — past-performance review at item and attribute level (winners, losers, slow movers, duplicated items) as the factual basis for the next plan.
- **Product attribute model** — category/department hierarchy plus descriptive attributes (brand, size, pack, color); attribute mix targets (e.g., how many options per attribute) are a common way to express breadth.
- **Option-count targets** — explicit breadth targets (number of options per category/subclass) and per-option sales expectations.
- **Store clustering** — grouping locations by sales performance, attributes, or space so assortments can be planned once and localized many times; cluster versions track changes across seasons.
- **Placeholders** — plan slots for new items that do not yet exist in product systems; real SKUs are mapped to them when development or ERP adoption completes.
- **Line review** — side-by-side review of the proposed offering, typically both as a visual gallery with product imagery and as an editable numeric grid; some products extend the review across categories to check the overall balance of the offer.
- **Financial reconciliation** — the assortment is checked against the merchandise financial plan / open-to-buy; plans that exceed budgets must be adjusted before approval.
- **Sales curves and receipt timing** — season sell-through/sell-down curves that phase the planned sales and receipts across weeks for seasonal items; size profiles distribute depth across size runs.
- **Presentation minimums** — floor quantities an option must present in stores, which can drive buys above forecast demand in some products.
- **Exceptions and exclusions** — store-level adjustments on top of cluster-level plans: an item excluded from specific stores, or a store-specific addition.
- **Snapshots, versions, and scenarios** — the plan's state is preserved at points in time; alternative plans (what-if) are compared on financial impact.
- **In-season adjustment** — monitoring sell-through as the season runs and revising the remaining plan (re-orders, re-phasing, exits).
- **Approval and handoff** — review gates before the plan is released; handoff to purchase-order creation for seasonal goods, or to replenishment/allocation systems for evergreen goods.
- **Administration** — retail calendar mapping, product and location attribute setup, data loading and validation, dashboards, and alerts.

### One Structure, Many Implementations

The core is written conceptually. Implementations differ on every axis:

```text
Concept:            Offering unit (breadth)
Implementations:    style-color option (fashion), choice, article/SKU (grocery/hardlines)

Concept:            Points-of-commerce grouping
Implementations:    performance-based clusters, attribute-based clusters, store grades,
                    banners/chains, sales-performance and space groups

Concept:            Period structure
Implementations:    seasons, assortment periods on a mapped retail calendar,
                    launch/end/phase-out dates per option

Concept:            Depth expression
Implementations:    buy quantities, weekly receipt flows, presentation minimums,
                    size-curve splits, prepack/pack multiples
```

A reader who has only seen one implementation — say, fashion line planning in a SaaS tool — should still be able to recognize a grocery banner-level assortment plan, or a spreadsheet-era process, as the same Type.

## How It Works

The canonical cycle runs pre-season, with an in-season extension. Exact steps and names vary by product; the sequence below is the common structure across the researched sample.

### 1. Set up the planning frame

Administrators map the retail calendar to planning weeks, define product and location attributes, load or connect historical sales and financial plans, and configure base data (costs, prices, images). This frame rarely changes between seasons.

### 2. Cluster locations

Locations are grouped into clusters so a plan can be authored once per group: by sales performance, by attributes (region, store size, format), or by space capacity. Clusters are reviewed, versioned, and approved. This step is what makes localization scalable — a plan is written for a cluster, then resolved to hundreds of stores.

### 3. Review the past

Planners analyze last season's (and longer-history) performance at item and attribute level: which options sold, which stalled, which attribute values outperformed, where the assortment duplicated itself or left demand unserved. Thresholds flag outliers. This hindsight becomes the evidence base for the next plan.

### 4. Set the strategy

For each category and assortment period, planners set breadth targets (option counts, attribute mix) and sales expectations, aligned to financial objectives. In mature products this happens against — and reconciled to — the merchandise financial plan, so the strategy starts inside the budget.

### 5. Build the assortment

The planner composes the offering per category and cluster:

```text
Determine eligible items
→ generate placeholders for new items
→ select / adopt options into the assortment
→ assign options to clusters (with exclusions for specific stores)
→ review the line visually and numerically
→ reconcile against strategy and financial plan
```

Item eligibility rules determine which items may go to which stores; placeholders hold space for styles still in development and are mapped to real SKUs later. The offering is refined until the line reviews well and the numbers fit.

### 6. Size the buy

For each selected option and location group, the planner sets planned quantities: units per cluster, spread across size runs where relevant, and phased across receipt weeks using sales curves for seasonal items. Depth is expressed in units, cost, and retail value, and stays within the financial envelope.

### 7. Review and approve

The plan goes through line review — often category by category, sometimes across categories to check the overall offer — and through financial reconciliation. Planners and leadership approve the plan; store-level exceptions are resolved here.

### 8. Hand off to execution

The approved plan leaves the application in two typical paths, matching two item lifecycles:

- **Seasonal / short-life items** → weekly sales and receipt plans become purchase orders (created in the tool in some products, exported to ERP or purchasing systems in others).
- **Evergreen / replenished items** → the approved assortment feeds replenishment and allocation systems, which then manage in-season stock store by store.

### 9. Adjust in season

Once the season runs, planners monitor actual sell-through against plan, retrend forecasts, adjust remaining receipts, re-balance the assortment across locations, and — for some segments — add or exit items. The adjusted plan is re-approved like the original.

## Interfaces

The following surfaces appear, in conceptual form, across the researched products. Exact layouts and names vary.

### Planning grid / workbook

The working surface where the plan lives.

- rows are options (or attribute groups), columns are periods and measures; data is grouped by category and cluster
- plan values (option presence, quantities, targets) are edited here
- primary actions: add/remove options, set quantities, filter, group, roll up, reconcile

### Hindsight / analysis views

The evidence surface for decisions.

- item-level and attribute-level historical performance, with thresholds and filters
- primary actions: analyze, flag winners/losers, compare seasons, identify duplication

### Strategy view

Where breadth and targets are set.

- option counts and attribute mix per category/subclass, sales expectations, target indicators
- primary actions: set targets, compare against last year, reconcile to financial plan

### Line review (visual + tabular)

The review surface for the proposed offering.

- visual gallery with product imagery, filterable and groupable; numeric grid alongside
- primary actions: adopt/drop options, compare, present, annotate

### Localization / location assortment views

Where the cluster-level plan is inspected and adjusted at location level.

- which options are present at which locations, filterable and groupable by location attributes
- primary actions: add/remove exclusions, inspect a store's assortment, review exceptions

### Receipt / flow views

Where depth is phased over time (prominent for seasonal businesses).

- weekly sales and receipt plans per option, sales curves, size-level splits
- primary actions: adjust buy quantity, adjust weekly flow, apply curves, approve

### Dashboard

Management surface with KPI tiles, charts, and quick access to recent planning work; some products add real-time alerts on plan conditions.

### Scenarios / snapshots

Alternative-plan comparison (what-if) and preserved plan states for pre-season vs in-season comparison.

### Administration

Calendar mapping, attribute definition, data import/validation, cluster strategy setup.

## Important Rules / Behaviors

### Plans are authored at group level, resolved at store level

The plan is written against clusters, then localized: every store in a cluster inherits the cluster assortment, minus exclusions plus store exceptions. This two-level structure — group authoring, location resolution — is the standard localization mechanism.

### The plan must fit the money

Assortment decisions are checked against the financial plan / open-to-buy. Products surface this as explicit reconciliation steps; a plan that exceeds its budget is not release-ready. The invariant behind it: depth is always quantified and sized against targets.

### Not every item may go to every store

Eligibility rules and exceptions constrain option-to-store assignment — by format, region, capacity, or regulation. The plan's cluster assignment is the default, not the absolute.

### Two item lifecycles, two post-plan paths

Evergreen, replenished items and seasonal, finite-life items follow different paths after approval: the former flow into replenishment/allocation; the latter into purchase orders and a sell-down to an end date. In several products, seasonal options carry launch and phase-out dates, and once an option is past its phase-out date it stops driving buys.

### New items are planned before they exist

Placeholders (or attribute-based reference items) let planners size and position new offerings ahead of product-system data. When the real item arrives, it is mapped to the placeholder; planning does not wait for master data.

### Approval gates precede handoff

Cluster definitions, curves, and the plan itself pass explicit review/approval steps in mature products. The plan handed downstream is an approved version, not a live draft.

### The application decides; it does not execute

No sales, no inventory movements, no payments happen in an assortment planner. Its output is a plan. If a product's primary surface is executing stock movement per store, it is a replenishment/allocation product, not this Type.

## Variants

Common forms of the Type:

- **Fashion / softlines assortment planning** — style-color depth planning, size curves and prepacks, visual line sheets, integration with product development (PLM), pre-season receipt planning by week; the strongest fit with the "line review" model.
- **Grocery / FMCG assortment planning** — banner- and cluster-level localization at large store counts, space pressure and item duplication analysis, listing/delisting of items, tight coupling to space planning and replenishment; supplier-driven item introductions.
- **Hardlines / electronics** — longer item lifecycles, more evergreen than seasonal, localization by store format and capacity.
- **Suite module vs standalone** — the capability ships as a module of a retail planning suite (alongside merchandise financial planning, pricing, promotion, space), as a standalone SaaS focused on the merchandise→assortment→allocation chain, or, in ERP-centric retailers, as listing administration close to merchandising master data.
- **Planning granularity** — cluster-level planning with location resolution (common) vs store-specific assortments (deeper localization, higher effort).
- **AI posture** — AI-generated recommendations for width/depth, automatic cluster assignment, auto-generated starting assortments vs planner-driven work with lighter assistance. The Type predates AI and does not depend on it.

A variant stays a variant as long as the defining core — offering set × points-of-commerce × period × depth — still describes its center. When the center moves (to money, to shelves, to strategy, to execution), it has become a different Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Category Management Application | adjacent, often bundled | owns ongoing category strategy and performance (category role, goals, supplier view); assortment planning produces the period-bound SKU offering plan that realizes that strategy |
| Merchandise Financial Planning / Demand Planning | upstream | plans money (sales, inventory, margin budgets by category × month, top-down); assortment planning is the SKU-level, location-resolved realization that reconciles to it |
| Retail Space Planning | adjacent, consumes output | owns physical shelf representation (planograms, facings, floor plans); assortment planning owns the offering. Space constraints can bound the assortment; assortment output feeds planograms |
| Replenishment / Allocation / Retail Inventory Management | downstream | execute continuous in-season stock movement per store; assortment planning makes the periodic offering decision that those systems then execute |
| Product Information Management / Product Catalog | orthogonal data layer | manages product master data and content; assortment planning decides the offering using that data |
| Retail Merchandising Platform | umbrella | suites marketed as "merchandising" span pricing, promotion, space, and assortment; assortment planning is one discipline inside them |
| Purchase Order Management | downstream execution | assortment planning decides what to buy and when; purchasing executes vendor transactions. Some products bundle PO creation; others hand off |

The closest boundary is with Category Management: vendors often sell them together, and users overlap heavily. The structural difference is the object of record — a category strategy and performance view versus a period-bound plan of which items are offered where and in what depth.

## Representative Products

- Oracle Retail Assortment Planning Cloud Service
- RELEX Assortment Planning (RELEX Unified Merchandising)
- Toolio Assortment Planning

The core model was checked across an enterprise planning-suite module, a unified retail platform's solution line, and a standalone SaaS product, spanning fashion, grocery, and mixed verticals.

## Sources

Research date: **2026-09-06**

- Oracle Retail Assortment Planning Cloud Service 26.2.301.0 — Get Started, Use listing, and User Guide (Introduction; Table of Contents) — https://docs.oracle.com/en/industries/retail/retail-assortment-planning-cloud-service/26.2.301.0/
- RELEX Solutions — Assortment planning solution page — https://www.relexsolutions.com/solutions/assortment-planning-software/
- Toolio — Assortment Planning product page and Help Center (Location Assortment; Minimum Presentation Policies in Receipt Generation; Assortment Planning collections) — https://www.toolio.com/assortment-planning , https://help.toolio.com/en/

> Sourcing limitation: Blue Yonder, o9 Solutions, Aptos, and SAP documentation could not be reached from the research environment (unreachable URLs or no public documentation library); no claims about those products are made. Oracle's functional overview paper is login-gated, so Oracle evidence rests on the public user guide. RELEX evidence is official but marketing-depth, so operational mechanics are not asserted for it. Precise vendor parameters (numeric limits, default values, exact state names) are intentionally avoided in this document; product-specific mechanics observed at that precision remain in the Research Notes.

Detailed product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
