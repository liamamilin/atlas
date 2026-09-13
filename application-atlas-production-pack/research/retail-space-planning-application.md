# Research Notes — Retail Space Planning Application

Cross-references: research/retail-merchandising-platform.md §Boundary Findings (records a removal test for this leaf: "Replace merchandise lifecycle with shelf-layout objects → Space Planning"); research/assortment-planning-application.md §Boundary Findings ("Replace the offering decision with shelf-layout objects → Space Planning"); research/category-management-application.md §Boundary Findings ("Replace the category performance loop with shelf-layout objects → Space Planning"). This pass applies and discharges those tests.

## Research Goal

Understand, from real products, what a Retail Space Planning Application is: what objects it manages, what its workflow is, who uses it, and where its boundary lies against the three already-processed 05.13 siblings (merchandising platform, assortment planning, category management) and other neighbors.

## Initial Boundary (working hypothesis before research)

Hypothesis: software for planning how products occupy physical retail selling space — at store level (floor/category layout, "macro space") and shelf level (planograms, "micro space") — with distribution to stores and compliance checking. Neighbors to test: category management (space as one tactic), assortment planning (feeds planograms), merchandising platform (executes the offering), store operations (implements layouts), IWMS space management (workplace homonym), digital shelf (online homonym).

## Research Questions

1. What is a planogram as an object? What does it contain and bind?
2. What is macro space vs micro space, and how do the two relate?
3. What objects does the system manage (store, floor plan, fixture, shelf, planogram, product, facing/position)?
4. What is the workflow from planning to store implementation and verification?
5. How does performance data inform placement, and what analysis does the system run?
6. Who uses it — retailer HQ, stores, CPG suppliers?
7. How does it integrate with assortment/category data and ERP data?
8. What are the variants (standalone planogram tool vs integrated platform; retailer vs supplier side; manual vs automated generation)?
9. What flips the Type into a sibling (removal tests)?

## Representative Products

| Product | Pole | Evidence depth reached |
|---|---|---|
| NielsenIQ Spaceman | data-vendor heritage space-management suite; retailer + manufacturer (CPG) dual side; global | Tier-2 product pages (×2) |
| DotActiv | standalone category-management specialist incl. space planning; mid-market; AI-era tooling | Tier-2 product pages (×4: home, floor planning, Activ8, Nova) |
| Quant (Quant Retail) | European integrated space/category/planogram platform; SMB → multinational; supplier side included | Tier-1 manuals/KB (×2) + Tier-2 solution pages (×4) |
| Oracle Retail (legacy) | enterprise suite pole — naming/packaging evidence only | Tier-1 docs index (×2); product docs library JS-gated |

Rejected/unreachable: Blue Yonder (404, consistent with two prior passes), RELEX (404 + empty ×2), Aptos (404). No claims made about them.

## Sources

All fetched 2026-09-07:

- NIQ — Spaceman product page: https://nielseniq.com/global/en/solutions/spaceman/
- NIQ — Spaceman Suite landing page: https://nielseniq.com/global/en/landing-page/spaceman-suite/
- DotActiv — homepage: https://www.dotactiv.com/
- DotActiv — Floor Planning Software: https://dotactiv.com/floor-planning-software/
- DotActiv — Activ8 Planogram Communication Software: https://dotactiv.com/planogram-communication-software
- DotActiv — Nova Planogram Automation: https://dotactiv.com/nova-planogram-automation
- Quant — Overview: https://www.quantretail.com/en/overview
- Quant — Planogram Software: https://www.quantretail.com/en/planogram-software
- Quant — Retail Floor Planning: https://www.quantretail.com/en/retail-floor-planning
- Quant — Store Specific Planograms: https://www.quantretail.com/en/store-specific-planograms
- Quant — Planogram & Store Compliance: https://www.quantretail.com/en/planogram-store-compliance
- Quant — Manuals index (KB): https://www.quantretail.com/en/kb
- Quant — KB "Planograms Linked with Floor Plans": https://www.quantretail.com/en/kb/get-started/planograms-linked-with-floor-plans
- Oracle — Retail documentation index: https://docs.oracle.com/en/industries/retail/
- Oracle — Retail On-Premise Applications page: https://docs.oracle.com/en/industries/retail/onpremapps.html

## Product Observations

### Product A — NielsenIQ Spaceman (evidence layer A: direct observation of official pages)

- Positioning: "A complete suite of applications that helps you to unlock your potential across all the steps of the Space management process"; "an integrated, automated planogramming process with diverse modules… analyzing performance and opportunities across planograms".
- Named capability clusters: powerful space planning and analysis; automatically generated planograms; cost-effective data management; planogram compliance.
- Benefits framing: define a space strategy based on shopper behavior to optimize product placement and store layout; a "synchronized environment that integrates data to create the perfect shelf"; automatically manage and update planograms; a "Smart placement algorithm" generating localized planograms adapted to each store's specific situation; a digital environment to update and distribute planograms across stores "with real-time HQ-store communication for tracking and monitoring planogram performance and quality".
- Users: "retailers, manufacturers, and organizations across industries"; claim of 2,000+ clients in 79 countries.
- Testimonials evidence: store-specific planogram creation using "the current assortment and financial data of each store" to avoid "free interpretation of the cluster level planogram" (French retailer); Spaceman Automation + Automation Server named (Grupo Ramos); user titles "Space Management Leader" (Grupo Ramos), "Space Planning Manager" (Sigma Healthcare).
- Vendor claims (kept as claims): revenue +10–20%, margin +5–15%, inventory −5–10%, efficiency ×3; Gartner analyst quote cited.

### Product B — DotActiv (evidence layer A: direct observation of official pages)

- Positioning: "Helping retailers and suppliers optimise shelf space. It creates planograms and improves in-store execution." Product family: Planograms (space planning automation), Floor Planning, Assortment Planning, Clustering, Retail Analytics, Unified Data Engine, DotActiv Viewer, Nova/LUNA (planogram automation), TrueView (planogram compliance & image recognition), Activ8 (planogram distribution), LOLA (AI assistant).
- Nova (AI planogram generation): generates planograms "from the ground up" on zero-base logic using shopper decision trees, merchandising rules, and store format needs; can generate planograms for multiple store sizes in one step. Three modes: Maintenance (insert new lines, remove delisted items with minimal disruption), Re-Space (rebalance facings on updated sales data and Days-of-Supply targets), Zero-Base (rebuild the category from scratch with an optimal flow and blocking strategy). Natural-language intent ("prioritize high-margin items on the top shelf") translated into a compliant planogram; every product pre-validated against specific fixture dimensions before generation ("a planogram that fits the shelf, every single time").
- TrueView (compliance): image recognition verifies planogram compliance at store level; upload shelf photos; automatic execution check; implementation status tracked in real time; drill down by region, store, or category; dashboards and execution metrics with feedback to Head Office.
- Floor Planning: data-driven floor plans; "Floor Plan Highlights" presets to see category performance across the store; heatmapping; floor performance and gondola reports; floor cluster grid (compare clusters on the plan against the live database); clustered gondolas ("pull planograms as drop counts onto your floor plan"); Floor Optimizer (cross-category analysis recommending ideal space allocation); goals include reducing congestion and improving shopper flow.
- Activ8 (distribution/implementation): automatically sends new and updated planograms to store users; web browser + Android/iOS; custom questionnaires to stores; implementation tracking; self-hosted or vendor-hosted; designed for stores with slow internet.
- DotActiv Viewer: approval workflow for planograms/reports ("cut out unnecessary steps in your approval workflow").
- Legacy migration: onboarding includes "conversion of existing PSAs and ICPs into DotActiv planograms" (legacy planogram file conversion — semantics of the formats not verified).
- Pricing tiers include "Enterprise — Best for Retail Teams & Floor Planners" ($4,500/license/year) and Enterprise AI ($7,500); Free/Lite/Pro below (claims from pricing page).
- Testimonial title: "Head of Assortment and Micro Space Planning" (Pick n Pay) — "micro space planning" as practitioner vocabulary.

### Product C — Quant (evidence layer A: official manuals + solution pages; strongest operational depth in sample)

- Positioning: "Intelligent Retail Platform" (since 2003); "an integrated solution for Space Planning, Category Management, planograms, ranging, Shelf Labels and POS printing, communication with stores and In-store Marketing". Pricing plans for "a small retailer, a multinational chain or a supplier" (supplier = CPG side included).
- Explicit micro/macro terminology: "Quant Desktop allows you to solve not only micro space in the form of creating planograms but also macro space within one integrated, multi-user application thanks to the built-in management of store floor plans."
- Macro space definition (Floor Planning page): "Macro space planning is the process of optimizing the sales area in order to increase the customer experience and sales. The result is the division of the sales area into individual sections, the layout of product categories within these sections and the selection of suitable fixture for the placement and presentation of products."
- KB workflow "Planograms Linked with Floor Plans" (ordered steps): import products → import product images ("so that planograms look professional") → create a category hierarchy (auto-generable from product attributes) → set up a standalone planogram → set a fixture for the planogram ("define the measurements of the fixture, number of shelves and other important attributes") → fill the planogram with products → create a store → upload a technical plan (DWG) to facilitate floor-plan drawing → create a layer version → insert and set fixtures in the floor plan → link planograms with store floor plans ("the planogram is tailored to each store according to the dimensions of the fixtures and, if necessary, according to sales") → publish the planogram on the web for the store.
- Fixtures: "classic shelving systems, atypical gondolas, freezers, hanging systems, display on tables or pallets"; floor-plan editor includes a fixture library for reuse; floor-plan layers; CAD/DWG import; advanced 3D (upload external 3D models — "digital twins of your stores").
- Store-specific planograms: "enhance the traditional concept of sharing planograms within clusters by automatically generating optimized planograms for each store based on a template composed of planogram rules." Planogram rules: "Instead of placing individual products on shelves, users express their intention reflecting the customer's decision tree by inserting planogram rules. Artificial intelligence takes care of the rest." Optimization inputs: sales history, demand forecast, logistical parameters (days a product's allocated capacity should last within the display), promotions/events and new products, product priorities, per-store product availability; automatic substitution of an unavailable product with the most similar available one.
- Publishing & compliance loop: "a well-managed process starting with the creation of a planogram at the headquarters, through its implementation in the store to the retrospective control and evaluation of the quality and results of implementation." Publishing "hundreds or thousands of new planograms to stores… is a matter of seconds"; stores notified by e-mail; previews include automatic visualization of changes vs old planograms; implementation dates and automatic notifications settable. Store confirms implementation and uploads a photo; built-in AI product recognition evaluates compliance; empty positions root-caused ("distinguishes whether the store has the corresponding product in stock or not"); HQ gets a list of implementation images ranked by quality; non-compliance can create follow-up tasks in Task Management.
- Physical-fit rule (concrete): "If the shelf is 76 cm wide, the store cannot receive a planogram for 80 cm, otherwise we risk that an important product will not be placed, simply because it did not fit."
- Data integration: automatic transfers of product, sales, stock, and price data into Quant; Quant "will enrich your ERP / BI systems with detailed information about product placement on store planograms"; CSV/FTPS, REST API, or SQL replication.
- User titles in testimonials: "Head of Space Management" (Sportisimo), "Assistant Manager – Space Management" (Keells), Category Managers (Dr.Max, Iceland, BioCompany).
- Vendor claims (kept as claims): 5–15% sales increase, 20–30% overstock reduction, 40–60% operations time saving; live in under 12 weeks.
- Heritage evidence: page references users transitioning "from Excel" floor plans and from "CAD tools" — direct evidence of pre-dedicated-software practice.

### Product D — Oracle Retail (evidence layer A: docs index pages; naming/packaging evidence only)

- Current cloud portfolio (Retail Analytics and Planning): AI Foundation, Retail Insights, Assortment Planning, Inventory Planning Optimization, Lifecycle Pricing Optimization, Merchandise Financial Planning, RPAS. Merchandising: Allocation, Fiscal Management, Integration, Invoice Matching, Merchandising Foundation, Pricing, Supply Chain Collaboration. **No space planning product is listed.**
- Legacy on-prem planning suite lists: "Category Management Planning and Optimization and Macro Space Optimization" (docs library at /cd/E75765_01/catman/, JS-gated — contents not readable). The product name is direct evidence that (a) macro space optimization existed as a distinct Oracle planning capability, and (b) the enterprise-suite pole packaged space with category management.
- Implication for the market-structure picture: the enterprise retail-suite pole does not currently lead with a standalone space planning product; the standalone/specialist market (NIQ, DotActiv, Quant, and unreachable Blue Yonder) carries the Type.

## Cross-product Comparison

| Structure | NIQ Spaceman | DotActiv | Quant | Oracle (legacy) | Verdict |
|---|---|---|---|---|---|
| Planogram as central object | yes ("build-out and analysis of planograms") | yes (core product) | yes (KB-documented) | implied (category planning suite) | Core (all) |
| Fixture/shelf as measured physical object | implied | explicit (fixture-dimension pre-validation) | explicit (measurements, shelves, fixture types) | unverified | Core (all full products) |
| Product placement informed by performance data | yes ("analyzing performance… across planograms"; assortment+financial data per store) | yes (sales data, Days of Supply) | yes (sales history, forecast, availability) | unverified | Core (all) |
| Store as target; store-specific tailoring | yes (localized planograms per store situation) | yes (multiple store sizes in one step) | yes (store-specific planograms; 76cm/80cm rule) | unverified | Core (all) |
| Macro space / floor planning | mentioned (store layout) | yes (dedicated product) | yes (dedicated editor + KB) | yes (named "Macro Space Optimization") | Common (not universal: standalone planogram tools exist) |
| HQ→store distribution | yes (digital environment, HQ-store communication) | yes (Activ8) | yes (Quant Web publishing) | unverified | Common |
| Compliance verification | yes (named module) | yes (TrueView image recognition) | yes (photo + AI + task follow-up) | unverified | Common |
| Automated/AI planogram generation | yes (automation, "Smart placement algorithm") | yes (Nova modes) | yes (template + rules + AI) | unverified | Common (era-current; not definitional) |
| Category/assortment linkage | yes (assortment refinement) | yes (integrated suite) | yes (category management module, ranging) | yes (packaged with category mgmt) | Common |
| Supplier/CPG side | yes (manufacturers) | yes (suppliers) | yes (suppliers) | n/a | Common |
| Analysis/reporting | yes (performance across planograms) | yes (floor/gondola reports, dashboards) | yes (analyses KB section) | unverified | Common |
| 3D / CAD import | not observed | not observed | yes (DWG, 3D models) | unverified | Optional |
| Approval workflow | not observed | yes (Viewer) | not observed directly (projects/roles exist) | unverified | Optional |
| Shelf labels / POS printing | not observed | not observed | yes | unverified | Optional |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

Minimal structure; removing any element stops the product from being recognizable as a Retail Space Planning Application:

1. **Physical selling space modeled as measured structure** — the store's selling space is represented as fixtures/shelves carrying real dimensions (widths, shelf counts, heights). This modeled space is the canvas everything else works on. Without it there is no space planning — only product lists or drawings.
2. **Planogram: explicit product-to-position arrangement** — the central object of record: a defined arrangement that assigns specific products to specific positions (shelves/segments/facings) on the modeled space. The planogram is the artifact the whole Type produces, exchanges, and evaluates.
3. **Performance-informed placement** — placement decisions are informed by product performance data (sales and related measures) and evaluated against it; space is treated as a scarce, allocatable resource whose allocation follows and feeds back into performance. This is what separates the Type from generic drawing/CAD tools.

The application is the digitized home of this structure: it holds the space model, composes and edits planograms against it, binds performance data to placement, and produces the planogram artifacts that flow to stores.

§24 historical check: the discipline predates dedicated software — planograms were drawn on paper and in spreadsheets, floor plans in CAD (direct evidence: Quant's page references users coming "from Excel" and from "CAD tools"; DotActiv onboards by converting legacy PSA/ICP planogram files; Spaceman is a decades-old product lineage). A spreadsheet-era planner with measured fixtures, explicit product placement, and sales-informed allocation satisfies all three invariants. Therefore: AI generation, image-recognition compliance, cloud publishing, 3D/digital twins, DWG import, and even dedicated software are NOT definitional.

### L1 — Common Mature Structure

Present across the researched sample; expected in mature products but not definitional:

- **Macro space / floor planning** — the store-level layer: dividing the sales area into sections, laying out categories across them, placing fixtures; heatmaps, floor-performance and gondola reports, cross-category space optimizers; linked to the micro layer (planograms pulled onto floor plans as "drop counts").
- **Store-specific planogram generation** — templates/rules plus automation producing per-store planograms tailored to fixture dimensions and local sales (replacing or augmenting cluster-level planogram sharing); substitution of locally unavailable products.
- **Distribution to stores** — publishing planograms to a store-facing web/mobile surface, with notifications, implementation dates, and change visualization vs the previous version.
- **Compliance verification** — store confirmation of implementation, photo documentation, increasingly AI image recognition scoring compliance, root-causing empty positions (out-of-stock vs not implemented), and follow-up tasks.
- **Planogram performance analysis** — sales/space productivity views across planograms, before/after comparisons, floor and gondola reports.
- **Product data foundation** — product records with images and physical dimensions; category hierarchy as the organizing structure; fixture library of reusable fixture types.
- **Integration** — sales/stock/price data in from ERP/BI; planogram placement data out to ERP/BI; linkage to assortment/category planning outputs.
- **Collaboration/approval** — review/approval surfaces for planograms (viewer roles, sign-off).
- **Export/printing** — PDF planograms and printouts for stores and supplier pitches.

### L2 — Variant / Optional Structure

Depends on operator, scope, generation philosophy, packaging, segment:

- operator side: retailer HQ space/category teams vs CPG/supplier account teams (planograms as pitch and compliance artifacts) vs joint work
- scope: micro-only planogram tooling vs micro+macro integrated space planning
- generation philosophy: manual drawing vs rules/template-driven automation vs AI generation (zero-base / maintenance / re-space modes; natural-language intent)
- compliance mechanism: manual photo review vs AI image recognition vs store self-confirmation only
- packaging: standalone specialist vs category-management suite module vs retail planning platform module; enterprise suites may not sell it at all (Oracle current portfolio)
- store estate posture: unified chains (cluster planograms) vs non-unified stores (per-store planograms)
- 3D visualization / digital twins; CAD/DWG interoperability
- adjacent machinery in the same platform: shelf labels, POS printing, store communication/forms, task management, replenishment linkage
- segment/pricing: SMB self-serve tiers vs enterprise licensing

### L3 — Vendor-specific (research notes only)

- NIQ: Spaceman suite module names (Automation, Automation Server); "Smart placement algorithm"; 2,000+ clients / 79 countries claim; Gartner-quoted benefit ranges (+10–20% revenue etc.)
- DotActiv: Nova/LUNA/LOLA/TrueView/Activ8 product names; Maintenance/Re-Space/Zero-Base modes; "model-agnostic" AI routing claim; PSA/ICP legacy conversion; pricing ladder ($0/$800/$2,000/$4,500/$7,500 per license/year); PowerBase knowledge base; DotActiv Academy; 2,000+ retailers / 500+ consultants claims
- Quant: Quant Desktop vs Quant Web split; "planogram rules" concept; layer versions; DWG import; 3D digital twins; shelf labels + POS printing; Forms & Surveys; Task Management integration; Planogramming vs Retail Planning pricing plans (unlimited users on the latter); 2003 heritage; claims (5–15% sales, 20–30% overstock, 40–60% time saving, <12 weeks to live); G2 satisfaction claims
- Oracle: legacy product name "Category Management Planning and Optimization and Macro Space Optimization"; current cloud portfolio contains no space planning product

## Rejected Findings (considered, not promoted)

- **"Space planning = workplace/facility space planning"** — rejected: same words, different universe. IWMS Space & Occupancy Management (§17) plans workplace occupancy; this Type plans product placement on retail selling fixtures. Homonym only.
- **"Planogram software = digital shelf / e-commerce merchandising"** — rejected: different surface (physical shelf vs online ranking); no acquisition/stock machinery here; the digital homonym was already rejected in the merchandising pass.
- **"Floor planning = architecture/CAD tooling"** — rejected: CAD is a data source (DWG import) and a heritage tool, not the Type; the Type binds categories/products/performance to the layout.
- **"Macro space is definitional"** — rejected: standalone planogram tools exist (Quant "Standalone Planograms" KB track; DotActiv planogram-only tiers); macro is the common second layer. → L1.
- **"Distribution to stores is definitional"** — rejected: supplier-side and standalone planogramming (e.g., a pitch planogram exported as PDF) satisfies the core without store distribution. → L1.
- **"Compliance (image recognition) is definitional"** — rejected: compliance existed as manual store confirmation and photo review before AI; mechanism is variant. → L1/L2.
- **"AI generation is definitional"** — rejected: manual planogramming was the norm for decades (historical check). → L2.
- **"3D / digital twins are definitional"** — rejected: single-product emphasis in sample. → L2.

## Boundary Findings

| Neighbor | Relationship | Distinction | Removal test (what flips the Type) |
|---|---|---|---|
| Category Management Application (05.13, processed) | adjacent, heavily bundled | category management owns the category's ongoing commercial performance/strategy loop (roles, scorecards, reviews); space planning owns the physical shelf representation. Category management consumes space as one tactic; space planning consumes category strategy/assortment as input. | Replace shelf-layout objects with the category performance/strategy loop → Category Management |
| Assortment Planning Application (05.13, processed) | upstream, feeds planograms | assortment decides WHAT is offered, in which stores/clusters, at what depth, for a period; space planning decides HOW the offered products sit on the physical shelf. Assortment output (range per store/cluster) is a key planogram input; space constraints can bound assortment. | Replace shelf-layout objects with the period-bound offering plan → Assortment Planning |
| Retail Merchandising Platform (05.13, processed) | sibling; planning→execution handoff | merchandising is the item/stock/PO operations system of record; space planning owns shelf-layout objects. (Test recorded there: "Replace merchandise lifecycle with shelf-layout objects → Space Planning" — confirmed from this side.) | Replace shelf-layout objects with item lifecycle + stock ledger → Merchandising Platform |
| Store Operations / retail execution (05.11) | downstream consumer | store operations runs daily store work (tasks, inventory, POS); space planning produces the layout that store execution implements; the compliance loop feeds results back but the objects differ (work vs layout). | Replace layout objects with daily store work objects → Store Operations |
| Space & Occupancy Management (§17 IWMS) | homonym | workplace occupancy vs retail product placement; different users, objects, data. | n/a — different Type |
| Digital shelf / e-commerce merchandising (no leaf; §06 neighbors) | homonym risk | online ranking/presentation vs physical shelf; "planogram" language occasionally borrowed online but the sampled products are physical-space systems. | n/a — different Type |
| Diagramming / floor-plan drawing tools (§03.05) | capability overlap only | generic drawing lacks product/performance semantics and the planogram object of record. | Remove product/performance binding → generic diagramming |
| Visual merchandising (discipline, no leaf) | adjacent discipline | visual merchandising covers display/presentation aesthetics; space planning is the quantified layout system of record. Some vendors use "visual merchandising" language for planogram work (Quant). | n/a — discipline vs system |

Joint-review discharge: the removal tests recorded by the three processed 05.13 siblings are applied and confirmed — the object-of-record discriminator (shelf-layout objects) separates this leaf from all three. Vendors bundle space with category/assortment (DotActiv, Quant, Oracle legacy packaging), matching the predicted heavy product-level overlap; the leaves remain distinct Types.

## Uncertainties

- Blue Yonder, RELEX, Aptos unreachable (404/empty); their space planning positioning is unverified and no claims are made about them. The enterprise-suite pole is therefore evidenced only by Oracle's legacy packaging name and current-portfolio absence.
- Oracle's legacy catman docs library is JS-gated; operational mechanics of the legacy Oracle product are not verified — only the product name and its packaging beside category management.
- NIQ Spaceman module-level mechanics (Automation Server, data management module) are marketing-depth only; no operational workflow documented.
- DotActiv evidence is product-page depth; the semantics of legacy "PSA/ICP" planogram formats are unverified.
- Planogram performance metric vocabulary (e.g., sales per linear/meter of shelf) is industry canon but was not documented at operational precision in any fetched source; kept generic in the final document.
- Supplier-side (CPG) workflows are evidenced by positioning ("retailers, manufacturers", "suppliers") and testimonials; no operational-depth supplier workflow (e.g., retailer-specific planogram submission) documented in the sample.
- Exact planogram interchange standards and file formats were not researched; the final document makes no claims about them.
- Approval workflow evidence is thin (DotActiv Viewer only); state names for planogram lifecycle (draft → approved → published) are not asserted.

## Final Synthesis

A Retail Space Planning Application is the retail merchandising application whose object of record is the physical selling space itself. Its defining core is threefold: the store's selling space modeled as measured fixture/shelf structures; the planogram — an explicit arrangement assigning specific products to specific positions on that space — as the central produced/exchanged artifact; and performance-informed placement, where sales and related data drive and evaluate how space is allocated to products. Around this core, mature products add the store-level macro layer (floor plans, category sections, fixture placement, heatmaps, space optimizers), store-specific planogram generation from templates and rules, distribution of planograms to stores through web/mobile surfaces with implementation dates, compliance verification through store confirmation and photo/image-recognition checks, planogram performance analysis, and integration with assortment/category planning and ERP data. The Type is realized by standalone specialists, category-management suites, and integrated retail platforms; enterprise retail suites may not sell it at all. It is distinct from category management (commercial loop vs shelf representation), assortment planning (offering decision vs shelf arrangement), the merchandising platform (merchandise lifecycle vs shelf-layout objects), store operations (execution vs layout), and the workplace "space planning" homonym. The spreadsheet/CAD/paper-era practice satisfies the defining core, so AI, cloud publishing, 3D, and image recognition are variants, not definitions.
