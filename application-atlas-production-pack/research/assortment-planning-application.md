# Research Notes — Assortment Planning Application

Research date: 2026-09-06
Slug: assortment-planning-application
Directory leaf: Assortment Planning Application (05.13 Merchandising)

## Research Goal

Understand what an Assortment Planning Application actually is as an Application Type: the core objects, the workflow retailers use to plan product offerings, the interfaces planners work in, the rules that govern the plan, and where the boundary lies against neighboring merchandising Types (Category Management, Space Planning, Merchandise Financial Planning, PIM, Replenishment/Allocation).

## Initial Boundary

Initial hypothesis (before research):

- Core use: decide which products (SKUs/style-colors) a retailer offers, in which stores/clusters/channels, in what depth (units), for which season/period — the "what to sell where" decision layer between category strategy and buying.
- Likely users: merchandisers, category managers, buyers, assortment/planning teams.
- Likely neighbors: Category Management Application (strategy), Retail Space Planning (shelf/planograms), Merchandise Financial Planning (budgets), PIM (product data), Replenishment/Allocation (in-season execution), Retail Merchandising Platform (umbrella).
- Unknowns: whether localization (store dimension) is definitional or optional; whether buy-quantity/receipt planning belongs to the Type or to a sibling; how ERP-embedded implementations differ from standalone suites.

## Research Questions

1. What are the core objects (assortment, option/choice/SKU, cluster, assortment period, plan measures)?
2. What is the canonical workflow from hindsight to approved assortment to execution handoff?
3. How is the plan localized (cluster vs store), and how do exceptions work?
4. How does the assortment plan connect to financial targets (MFP/OTB) and to buying/replenishment?
5. Which mechanisms are common (attributes, placeholders, curves, presentation minimums, line review) vs product-specific?
6. How do verticals differ (fashion vs grocery/FMCG)?
7. Where are the boundaries with Category Management, Space Planning, MFP, PIM, Replenishment?

## Representative Products

| Product | Philosophy / Tier | Why selected |
|---|---|---|
| Oracle Retail Assortment Planning Cloud Service (APCS) | Enterprise retail planning suite cloud service; process-structured workbooks | Public Tier-1 user guide; strong process and object vocabulary |
| RELEX Assortment Planning | Unified retail planning platform (European, grocery-heavy) | Marketing/solution documentation; localization and cross-platform integration emphasis |
| Toolio Assortment Planning | Modern standalone SaaS for mid-market/vertical (fashion) retailers | Public product pages + Help Center with operational articles |

Blue Yonder, o9 Solutions, Aptos and SAP were considered; public documentation could not be reached (see Uncertainties).

## Sources

Fetched 2026-09-06:

- Oracle Retail Assortment Planning Cloud Service 26.2.301.0 — Get Started: https://docs.oracle.com/en/industries/retail/retail-assortment-planning-cloud-service/26.2.301.0/
- Oracle Retail Assortment Planning Cloud Service — Use (guide listing): https://docs.oracle.com/en/industries/retail/retail-assortment-planning-cloud-service/26.2.301.0/use.html
- Oracle Retail AP Cloud Service User Guide — Introduction: https://docs.oracle.com/en/industries/retail/retail-assortment-planning-cloud-service/26.2.301.0/apcsu/to_2523introduction.htm
- Oracle Retail AP Cloud Service User Guide — Table of Contents (task/step/view structure): https://docs.oracle.com/en/industries/retail/retail-assortment-planning-cloud-service/26.2.301.0/apcsu/toc.htm
- RELEX Assortment planning solution page: https://www.relexsolutions.com/solutions/assortment-planning-software/
- Toolio homepage / platform overview: https://www.toolio.com/ , https://www.toolio.com/assortment-planning
- Toolio Help Center: https://help.toolio.com/en/ (collections: Assortment Planning, Next Generation Assortment Planning, Allocation)
- Toolio Help Center — Location Assortment: https://help.toolio.com/en/articles/16132784-location-assortment
- Toolio Help Center — Minimum Presentation Policies in Receipt Generation: https://help.toolio.com/en/articles/15702689-minimum-presentation-policies-in-receipt-generation

Unreachable (recorded as source-access limitations):

- Blue Yonder assortment/category solutions (URL 404; no further guesses spent)
- o9 Solutions category management page (URL 404)
- Aptos assortment planning (URL 404)
- SAP Help Portal (no reachable standalone "Assortment Planning" doc library found via URL pattern)
- Oracle AP Functional Overview Guide (KB695860) — behind My Oracle Support login
- RELEX customer support portal (login-gated); only public solution page used

## Product Observations

### Oracle Retail Assortment Planning Cloud Service (Tier 1 — official user guide; Evidence Layer A)

Definition observed on the product's Get Started page:

> "The Assortment Planning Cloud Service process establishes the breadth and depth of the product offering (including the color/fragrance/flavor and size level), for Points-of-Commerce and for a given period of time. The analysis of past performance ... are key inputs into revising a currently planned/executed assortment or building a new assortment."

User Guide Introduction (directly observed):

- "Assortment Planning is the strategic process retailers use to define the optimal product mix by balancing assortment breadth, depth, and product attributes to meet customer demand across channels and locations."
- Planning container: **Assortment Group = Assortment Period (planning timeframe) + assigned Cluster version (groups of stores with similar assortment needs)**. "Together, they establish the time and location framework that drives localized assortment decisions across stores, channels, and product categories."
- Two product lifecycle classes: **Long Life Cycle (LLC)** — replenishment-driven/evergreen, "flow into external replenishment or allocation systems after assortment approval"; **Short Life Cycle (SLC)** — seasonal/fashion/trend-driven, "require pre-season inventory flow planning and external purchase order execution".
- Three core capabilities: **Assortment Strategy** (breadth: option counts, attribute mix targets, sales expectations aligned to financial objectives), **Assortment Fit** (selection: "which style-colors assort to which store clusters while aligning to assortment strategy and financial targets"), **Item Flow** (SLC only: "weekly sales and receipt plans ... to support downstream purchase order creation").
- 12-step process: Planning Administration (week mapping, product attributes, base unit/price/cost, location attributes, cluster strategy weights, exceptions) → Validate Loaded Data (actuals, MFP plan, location plan) → Location Clustering (attribute analysis, sales performance groups, space groups, approval, cluster versions) → Assortment Period Maintenance (periods, calendars, bell/trend/slow item curves) → Curve Maintenance → Hindsight (item and attribute views, thresholds) → Assortment Strategy (attribute type/values, strategy parameters, strategy by subclass, **Reconcile to MFP**) → Assortment Fit (item eligibility, **generate placeholders**, refine shopping list, create assortment fit, visual fit, **Line Review**, reconcile to strategy, reconcile to MFP, store assortment exceptions) → Cross-Category Line Review (visual + table) → Item Flow (adjust buy quantity, adjust weekly flow, reconcile to MFP, approve, sales curve review) → Store Exception Item Flow → In-Season Item Flow (trend analysis, adjust weekly flow, reconcile to MFP, approve).
- Objects visible in the guide TOC: product attributes (define/select/assign, images, placeholder positions), location attributes, department/location exclusions, cluster strategy weights, assortment periods, sales curves (by assortment, with approval), item eligibility (define, attribute-store exceptions, item-store exceptions), placeholders, buy quantity, weekly flow, receipts by size (SPO size profile), option eligibility, rollups (product/location), dashboards (tiles, charts, recent plans), real-time alerts, special filters, glossary of measures.
- Interfaces: RPAS "workbook" model — planning Segments → Steps → Tabs → Views; dashboard with tiles/charts/recent plans; line review in visual and table modes; approval views for clustering, curves, item flow.

### RELEX Assortment Planning (Tier 2 — official solution page; Evidence Layer A for this product, marketing-depth)

- Positioned under "Space & Assortment" within RELEX Unified Merchandising, sibling to Planogram optimization and Retail floor planning; "connects assortment and space decisions to pricing, promotions, and inventory plans."
- Key features as stated: set **category goals (sales, margin, volume targets)** aligned to merchandise strategies; "discover how planned assortments are forecast to perform against category goals and adjust"; use data to "identify slow-moving SKUs and instances of item duplication ... free up space"; "plan their product offerings, ensuring that the right products are stocked in the right stores."
- **Store-cluster and store-specific assortment changes** "visible across your business ... simultaneously available for forecasting, replenishment, planograms, and inventory planning."
- Attribute-based forecasting: new items get reference products "based on attributes such as category, brand, pack size, and price."
- Forward-looking data: adapt assortments using "store- and channel-specific forecasts", not only historical sales.
- Store collaboration: mobile access to assortment and planogram information; "two-way communication between central teams and stores"; associates can suggest changes.
- Named personas: VP of Merchandising / Chief Merchandising Officer; Category Manager / Assortment Manager. Decisions described: which products to "retain and discontinue", minimizing capital in slow movers, increasing category gross margin.
- MFP/OTB exists as a separate RELEX solution (not claimed as part of assortment planning).

### Toolio (Tier 1 help center articles + Tier 2 product pages; Evidence Layer A)

Product page (official):

- Module chain: **Merchandise Planning (MFP) → Assortment Planning ("Assortment Item Plan — visualize and refine buying for the perfect item mix") → Allocation**.
- "Toolio manages the full assortment workflow: width and depth planning, option counts, cluster-level localization, and buy quantities. All connected to your merchandise financial plan so assortment decisions stay within OTB."
- "Planning happens at the **choice** level (style/color) **by cluster** (group of locations), and clusters are built from your actual location attributes: geography, store size, historical sales behavior."
- **Placeholders**: "plan for new styles before they're finalized in your ERP or PLM. When the real style is adopted, it maps to the placeholder automatically."
- Hindsighting: "analyze past seasons and assortments to identify the winners, losers ... data-driven buy decisions"; attribute analysis to develop new assortments.
- Gallery view: "product imagery front and center ... filter, group, and sort"; line sheets are visual + numeric.
- Reconciliation: "Top-down to bottom-up reconciliation — connect your assortment plan to your merchandise plan to spot gaps."
- Smart Start: AI "automatically generating cluster-appropriate placeholders."
- PO Manager: consolidate ideal receipts into purchase orders (MOQs, freight); "Review and approve POs"; creating NetSuite inventory items & POs from the assortment plan (Help Center).
- Snapshots ("filter and analyze your assortment by time, product, or location attributes ... how it evolves"), pre-season vs in-season shift monitoring, what-if scenarios with financial impact.

Help Center (operational detail, directly observed):

- **Location Assortment** view: "translates your cluster-level assortment into a location-level picture — showing you which choices are present at each location"; "Manage Exclusions" to add/remove locations per choice; distinct-count metrics (choices per location, locations per choice); "financial and unit metrics are planned at the cluster level."
- **Minimum Presentation Policy**: presentation minimum/profile acts as an inventory floor combined with forecasted demand when generating receipts (policies Additive/Balanced/Inclusive; reorder point and order-up-to levels; per-choice, assortment-default, or org-default). "Receipt Order Multiple ... rounds final receipts up to the configured increment"; MOQ applies; Target Sell Through applies "for seasonal choices with a defined end date or phase out date"; "After the Phase Out Date, presentation minimums drop to 0."
- Other collections: Sell-Down Curves, ABCXYZ Analysis, Forecast Confidence Score for new choices, Forward Inventory Position View, In-Season Business Review, Retrend views, Ordering in Packs (Prepacks), Multi-currency planning, Similar Choices tab, Exporting Deleted Choices (deleted choices remain retrievable), Lock Receipts Through a Date.

## Cross-product Comparison

| Dimension | Oracle APCS | RELEX | Toolio |
|---|---|---|---|
| Defining act | breadth + depth of offering per point-of-commerce per period | right products in right stores against category goals | width/depth (option counts, buy quantities) by choice × cluster |
| Plan container | Assortment Group = Assortment Period + Cluster version | category/store-cluster assortments on one platform | assortment plan per season/channel; datasets + views |
| Product unit | style-color "option" (color/fragrance/flavor + size) | SKU | "choice" (style/color) |
| Location unit | store clusters (sales performance groups, space groups); versions | store clusters and store-specific assortments | clusters from location attributes; per-choice exclusions |
| Time | assortment periods, retail week mapping, curves | season goals; forecasts | seasonal timelines, launch/end/phase-out dates, sell-down curves |
| Depth expression | buy quantity, weekly flow, receipts by size | forecast-driven performance vs goals | buy quantities, receipts, presentation minimums |
| Past data | hindsight item/attribute views, thresholds, loaded actuals | identify slow movers/duplication; forecasts | hindsighting winners/losers, attribute analysis |
| Financial coupling | Reconcile to MFP (repeated gates) | category goals (sales/margin/volume) | reconcile to MFP / OTB guardrails |
| New items | placeholders (generate placeholder view) | attribute-based reference products | placeholders + auto-mapping on adoption |
| Review | Line Review (visual/table), Cross-Category Line Review | plan/adjust loop vs goals | Gallery line sheets, snapshots, scenarios |
| Localization mechanics | cluster assignment + item/attribute store exceptions | cluster + store-specific changes; store suggestions | cluster planning + per-choice exclusions; Location Assortment view |
| Execution handoff | LLC → replenishment/allocation; SLC → external POs | forecasting/replenishment/planograms get updates | allocation module; NetSuite POs |
| In-season | In-Season Item Flow (trend, adjust, approve) | adapt assortments to changing demand | In-Season Business Review, retrend |
| Packaging | module of Oracle Retail Analytics & Planning (RPAS workbooks) | module of RELEX unified platform | standalone SaaS; separate modules MFP/AP/Allocation |

Cross-product commonalities (Layer B): option/SKU-level offering decision; cluster/localization; season/period bound; quantified plan (units/value); hindsight; attribute analysis; placeholders for new items; line review; exceptions; approval before handoff; in-season adjustment; downstream handoff to buying or replenishment; coupling to financial targets.

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

Minimal structure; removing any element stops the product from being recognizable as an Assortment Planning Application:

1. **Planned offering set (breadth)** — the retailer's merchandise decision at product-option level (style/color/SKU) within a category: which items are offered, added, kept, or dropped.
2. **Points-of-commerce assignment (localization)** — the offering is defined against the retailer's selling locations, grouped for planning (clusters/grades/banners/channels); the plan resolves to which locations carry which options.
3. **Period bound (season)** — the plan is made for a defined planning timeframe on the retailer's calendar (season/period), including carryover structure.
4. **Planned depth in quantity/value** — the offering is sized: planned units to carry/buy per option per location group for the period, expressed in units and value, sized against the retailer's financial targets.

The application itself is a planner-facing decision surface that holds this plan as a persistent, reviewable, versioned object and hands the approved plan to execution (buying/POs or replenishment/allocation).

§24 historical check: pre-AI assortment planning (spreadsheets over last season's sell-through, store grades, size curves, OTB caps) satisfies all four invariants; ERP-embedded "listing" systems satisfy the offering+location+period core but lack the planning surface — they are execution of listing decisions, a different (adjacent) structure. AI/optimization is not required.

### L1 — Common Mature Structure

Present across the researched sample; expected in mature products but not definitional:

- hindsight / past-performance analysis at item and attribute level
- product attribute model (category/brand/size/pack etc.) and attribute mix targets
- option-count (breadth) targets and per-option sales expectations
- store clustering machinery (performance/attribute/space-based), cluster versions
- placeholders for planned-but-not-yet-final items, mapped to real SKUs later
- line review surfaces (visual gallery + tabular grid), cross-category review
- reconciliation to the merchandise financial plan / open-to-buy
- sales/sell-through/sell-down curves; time-phased receipts (weekly flow) for seasonal items
- size profiles / packs / prepacks / order multiples; presentation minimums as inventory floors
- store × item exceptions / exclusions on top of cluster-level plans
- snapshots / versions / what-if scenarios
- in-season monitoring and adjustment (trend analysis, retrend, re-buy)
- approval gates before handoff; handoff to PO creation or replenishment/allocation
- dashboards, KPI tiles, alerts; admin setup (calendar mapping, attributes, data validation)

### L2 — Variant / Optional Structure

Depends on segment, geography, workflow, packaging:

- vertical emphasis: fashion/softlines (style-color-depth, PLM integration, visual line sheets, prepacks) vs grocery/FMCG (banner localization, duplication/space pressure, delisting, supplier-driven items) vs hardlines/electronics (longer cycles)
- planning granularity: cluster-level planning with location resolution vs store-specific assortments
- receipt-planning depth: full weekly item-flow planning inside the tool vs leaving receipts to replenishment systems
- suite module vs standalone SaaS vs ERP-adjacent execution of listing decisions
- channel scope: stores-only vs including e-commerce/points-of-commerce
- AI posture: recommendations and auto-generation vs planner-driven with lighter assistance
- store collaboration (associate suggestions via mobile) — observed in one product, plausible variant
- PO creation inside the tool vs external PO execution

### L3 — Vendor-specific (research notes only)

- Oracle: "Assortment Group", "option", LLC/SLC terminology, RPAS workbook segments/steps/tabs, Reconcile-to-MFP views, Receipts by Size (SPO size profile), Cross-Category Line Review as a named task, legacy separate SKUs for fashion vs grocery/hardlines editions
- Toolio: "choice", Minimum Presentation Policy (Additive/Balanced/Inclusive), Smart Start, Gallery View, Style Bank, Tooli AI agent, MCP server, Assortment Plan Defaults, exporting deleted choices
- RELEX: Unified Merchandising framing, mobile two-way store collaboration, attribute-based reference-product forecasting, planogram/floor-planning siblings on one platform

## Vendor-specific Findings

- Oracle's approval gates appear at multiple points (clustering, curves, item flow) — an approval-gated process is cross-product, but Oracle's named views are vendor detail.
- Toolio's three named Minimum Presentation Policies and their formulas are product-specific; the *concept* of a presentation floor is broader but only evidenced in Toolio at this precision.
- RELEX's store-associate mobile suggestions are product-specific.
- Toolio's MCP server / AI agent surfaces are product-specific modern packaging.

## Rejected Findings

- **"Option counts / attribute mix targets" as invariant** — very common target mechanism, but an assortment plan can exist as an explicit SKU set without formal breadth targets. → L1.
- **"AI-driven recommendations" as invariant** — modern packaging; pre-AI assortment planning is the same Type. → L2.
- **"Planogram/space linkage" as invariant** — common in grocery (space groups; planogram integration) but assortment planning exists without space data. → L1/L2.
- **"Formal MFP/OTB reconciliation" as invariant** — all sampled products couple to financial targets; but the invariant is captured more abstractly in L0 as "depth sized against financial targets". The named MFP interface is L1.
- **"Purchase order creation inside the tool" as invariant** — Toolio does POs in-tool; Oracle explicitly hands off to external PO execution. → L2.
- **"Weekly item-flow planning" as invariant** — Oracle scopes it to SLC; RELEX evidence does not center it. → L1.
- **"Store-level (not cluster-level) planning" as invariant** — sampled products plan at cluster level and resolve to stores; store-specific is a variant depth. → L2.

## Boundary Findings

| Neighbor | Relationship | Distinction | What removal flips the Type |
|---|---|---|---|
| Category Management Application | adjacent, often bundled | category management owns ongoing category strategy and performance management (category role, goals, supplier view); assortment planning produces the period-bound SKU offering plan. Users overlap; the object of record differs (category strategy vs assortment plan). | Replace the SKU-offering plan with category-level strategy/performance management → Category Management |
| Merchandise Financial Planning / Demand Planning | upstream | MFP plans money (sales/inventory/margin budgets by category × month, top-down); assortment is the SKU-level bottom-up realization that reconciles to it. | Remove SKU/option level and locations, keep category budgets → MFP |
| Retail Space Planning | adjacent, feeds into | space planning owns physical shelf (planograms, facings, floor plans); assortment owns the offering. Space constraints (space groups, capacity) can bound assortment; assortment output feeds planograms. | Replace the offering decision with shelf-layout objects → Space Planning |
| Replenishment / Allocation / Retail Inventory Management | downstream | those systems execute in-season stock movement per store continuously; assortment makes the periodic offering decision. LLC assortments flow into them after approval. | Replace the planned offering with continuous automated per-store stock decisions → Replenishment/Allocation |
| PIM / Product Catalog | orthogonal data layer | PIM manages product master data/content; assortment planning decides the offering using that data. | Remove the offering decision and quantities, keep product data → PIM |
| Retail Merchandising Platform | umbrella | suites market "merchandising" across pricing/promos/space/assortment; assortment planning is one discipline inside it. | n/a (umbrella term) |
| Buying / PO management | downstream execution | assortment decides what to buy and when; purchasing executes vendor transactions. PO management may be bundled (Toolio) or external (Oracle). | Replace planning with transaction execution → Purchase Order Management |

Alias/variant risks observed: some vendors sell assortment planning and category management as one module ("category & assortment planning"); the directory keeps them separate, which matches the object-level difference found. Retail Merchandising Platform (sibling leaf) risks overlapping with suite-level products — noted as a taxonomy observation, not changed here.

## Uncertainties

- Blue Yonder, o9, Aptos, SAP documentation could not be reached; their inclusion would likely confirm the same core but could add variants (e.g., optimization-first positioning). No claims about them are made.
- Oracle's Functional Overview (business concepts, AI recommendations) is login-gated; Oracle observations rest on the Get Started page and User Guide (Introduction + TOC + task structure).
- RELEX evidence is marketing-depth (official solution page); operational mechanics (statuses, editability, exact views) not verified.
- Exact lifecycle states (draft → review → approved → published) were not documented identically across products; approval gates are evidenced (Oracle approve views, Toolio PO review) but universal state names are not asserted.
- ERP-embedded "assortment maintenance / listing" semantics (e.g., whether ERP suites implement assortment as site-group master data rather than analytical planning) could not be verified from primary sources in this pass; kept as a hypothesis to verify, not a finding.
- SMB segment: no dedicated SMB-native assortment planning product surfaced in the sample; the low end of the market appears to run on spreadsheets. Unverified beyond the sample.

## Final Synthesis

An Assortment Planning Application is a planner-facing retail decision surface in which merchandising teams compose, size, localize, review and approve the retailer's product offering for a coming period: which options (style/color/SKU) are offered (breadth), which store groups and channels carry them (localization), and how many units are bought/carried per option and location group (depth), with the plan quantified in units and value and sized against financial targets. Plans are built on hindsight analysis of past performance at item and attribute level, organized through store clusters and assortment periods, use placeholders for not-yet-final new items, pass through line reviews and approvals, and hand off downstream to purchase-order creation (seasonal items) or replenishment/allocation (evergreen items), with an in-season loop for adjusting the plan as real demand emerges.

The defining core is deliberately small: offering set × points-of-commerce × period × depth. Everything else — AI recommendations, planogram coupling, in-tool purchase orders, store collaboration, prepacks, scenario tooling — is common mature structure or variant, not definition.
