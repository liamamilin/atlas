# Research Notes — Food PLM

## Research Goal

Understand what a Food PLM actually is from real products: what objects exist inside it, who operates it, how the development-to-launch work flows, which structures are definitional vs common vs optional, and where its boundary lies against the neighboring Types — Product Lifecycle Management / PLM (§16), Food Formulation Platform, Food Specification Management, Food Labeling Platform, Food Manufacturing ERP, and PIM.

This pass also carries three pre-hung joint-review flags to discharge:

1. **food-formulation-platform** (§20, 2026-09-08): composition core vs lifecycle container; SpecPage splits SpecPDM from SpecPagePLM; TraceGains pitches Formula Management against "traditional PLM".
2. **food-specification-management** (§20, 2026-09-08): container-vs-core seam — test whether the food-plm core adds lifecycle machinery (projects, stage gates, artwork/critical path) beyond the spec record.
3. **product-lifecycle-management-plm** (§16, 2026-09-09): test whether sampled products hold the four-leg PLM core (product record + structured revision-controlled definition + controlled change + whole-life span) with food content, or whether they are composition/specification-centered tools adjacent to that Type.

## Initial Boundary

Initial hypothesis: Food PLM = the food & beverage manufacturer's product-lifecycle system of record — a product record holding formula + specifications + packaging + artwork, wrapped in NPD project/stage-gate machinery from concept to launch, handing off to ERP.

Nearest neighbors:
- Product Lifecycle Management / PLM (§16) — the generic four-leg core; risk of alias (industry variant).
- Food Formulation Platform — the composition core (formula of record).
- Food Specification Management — the formal statement of record.
- Food Labeling Platform — the regulated retail-facing label artifact.
- Food Manufacturing ERP — run-time production, consumes the released definition.
- PIM — commerce-facing product information.

## Research Questions

1. What is the unit of record — is there a product record to which everything attaches?
2. Is the product's definition held as structured, revision-controlled data (formula versions, spec versions, packaging/BOM versions, artwork versions)?
3. Is there controlled evolution — formal change processes, approval workflows, change propagation?
4. What is the lifecycle span — concept → launch → production handoff? Is NPD project machinery (stage gates, briefings, tasks, Gantt) definitional or common?
5. How do formulation, specification, labeling, packaging/artwork, and supplier data relate to the PLM center — inside it, beside it, or downstream of it?
6. What is the seam against generic/discrete PLM — is the record world (process manufacturing: formulas as ratios, allergen/claims rollups) the differentiator?
7. Do vendors split the lifecycle layer from the data core as separate products (SpecPage), bundle NPD on a spec core (Foods Connected), or brand the whole thing something else (TraceGains "NPD Suite")?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

| Product | Pole | Why sampled |
|---|---|---|
| Centric PLM (Centric Software) | multi-industry consumer-goods PLM with a dedicated F&B edition | the creative/lifecycle-led pole; fashion-PLM heritage extended to food |
| SpecPagePLM (SpecPage / Revalize) | food-native PLM explicitly split from SpecPDM | the vendor-split test case for container-vs-core |
| TraceGains NPD Suite | networked/formulation-led suite that does NOT brand as PLM | the anti-PLM-label pole that may still hold the core structurally |
| Foods Connected Specifications & NPD | spec core + bundled NPD stage-gate workflow (mid-market) | the "does bundling NPD workflow on a spec core make a PLM?" test case |
| Specright | spec-first PLM, multi-industry with F&B emphasis | the self-declared "spec-first PLM" pole; carries the Gartner F&B PLM market framing |

## Sources

Research date: 2026-09-10. All Tier 1/2 official vendor pages, fetched live.

- Centric Software — root: https://www.centricsoftware.com/ ; Food & Beverage industry page: https://www.centricsoftware.com/food-beverage ; Centric PLM product page: https://www.centricsoftware.com/what-is-centric-plm
- SpecPage (Revalize) — root: https://specpage.com/ ; SpecPagePLM product page: https://specpage.com/product-lifecycle-management/ ; SpecPDM product page: https://specpage.com/product-data-management/ ; Online Help portal: https://help.specpage.com/
- TraceGains — root: https://www.tracegains.com/ ; NPD Suite overview: https://tracegains.com/product-development/
- Foods Connected — Specifications & NPD solution page: https://www.foodsconnected.com/solutions/food-specifications-npd/
- Specright — root: https://www.specright.com/ ; spec-first PLM page: https://www.specright.com/spec-first-plm/ ; Food & Beverage PLM page: https://www.specright.com/food-and-beverage-plm/

Note: the earlier food-plm attempts (batch-D 2026-09-08, sweep 2026-09-10) failed before producing files; this pass is the first completed research.

## Product Observations

### Centric PLM (Centric Software) — multi-industry consumer-goods PLM, F&B edition

Evidence layer: A (direct observation of official pages).

- Positioning: "End-to-End Product Platform From Concept to Commercialization"; Centric PLM is one product in a suite (Planning & Pricing, Market Intelligence, Visual Boards, PXM, AI Studio). Industries include Fashion & Apparel and Food & Beverage as siblings — the multi-industry consumer-goods PLM pole.
- F&B edition content (from the F&B industry page): "Optimize recipes, manage ingredients and drive innovation while reducing costs... ensure compliance with Centric PLM's centralized data and automated workflows."
- Product-definition estate: "KEEP TRACK OF PRODUCT SPECS — Easily update and manage data and documentation for product formulation, ingredients, packaging and more. Centralize all product data connected directly to each product to track changes over time." — product record + attached definition data + change tracking over time.
- Packaging/artwork: "SYNCHRONIZE PRODUCT & PACKAGING DATA — Quickly develop, source and update labels using templates populated with formulation, allergen, nutrition and regulatory data from PLM and connected databases." "Automatically update changes from formulation to artwork to marketing."
- Formulation inside the platform: "Automate formulations. Optimize nutrient targets to ingredient constraints." (R&D Food Scientists role)
- Lifecycle/workflow: "Manage tasks efficiently with built-in workflows. See the impact of R&D, design, packaging and supply decisions on cost, delivery and more." PLM FAQ: "PLM software makes every part of the product lifecycle simpler to manage, from concept to replenishment... streamlining design, sourcing, sampling and quality and compliance testing."
- Roles served: R&D Food Scientists, Quality & Compliance, Procurement & Buying, Marketing, Brand Managers, Project Management, Packaging & Artwork, Master Data Management — the whole-organization span.
- Customer types: ingredient providers, F&B companies, food service companies. Food case studies: Teway Food ("100% Compliance Calculation Accuracy and Cuts Formula Updates to Minutes with Centric PLM"), Great Kitchens, MeEat, NHCO Nutrition.
- Compliance integrations: FoodChain ID (regulatory content).

### SpecPagePLM (SpecPage / Revalize) — food-native PLM split from SpecPDM

Evidence layer: A (direct observation of official product pages).

- The vendor ships SpecPagePLM, SpecPDM, and SpecPIM as three separately named products — direct confirmation of the data-core vs lifecycle split inside one vendor.
- SpecPagePLM page: "PLM is the crucial differentiator to drive product and process innovations... a single source of truth, transparency and traceability." "PLM innovative process solutions are global project and portfolio management frameworks, they support new product innovations..." — the PLM product's own self-description centers project and portfolio management.
- PLM pillars named: supplier management (raw-ingredient source, processing date, expiration, allergen information for procurement decisions); "materials and recipe specifications management throughout the entire product structure and lifecycle"; global project and portfolio management; regulatory compliance adaptability.
- SpecPDM page (the data core): master data management (raw materials, semi-finished and finished products, prices, nutritional values, allergens, certifications, packaging; suppliers; nutrient databases BLS/Ciqual/USDA); formula management (recipe ingredients, trials, simulations, versions, cost calculations); formula optimization & simulation (linear optimization to nutritional targets); specifications (automated product specification + ingredients/declarations lists, templates, generated reports, ISO/IFS certification-based workflows, audit trails); labeling & calculations (nutrition facts, QUID, allergen status, RDA); processing instructions; risk management; complaint management; reporting.
- The SpecPDM page contains a "PLM – Project Management" section: "Briefing and requirements; Activities and indicators can be linked to automated workflows; Checklists, product and vendor questionnaires...; Resource planning and management; Integrated document management support." — i.e., the project/briefing/workflow layer is what the PLM side contributes on top of the PDM data core.

### TraceGains NPD Suite — networked/formulation-led, not branded PLM

Evidence layer: A (direct observation of official pages).

- The vendor does NOT use "PLM" as a product name. The suite is the "NPD Suite": "Digitize and centralize sourcing, formulation, specs, and compliance—all on one integrated platform." "Accelerate innovation from source to shelf."
- Named products: Formula Management, Specification Management, Packaging Spec Management, WebCenter Go (artwork; Esko integration), Finished Goods, Regulatory Global (SGS Digicomply partnership), NutriCalc.
- The data thread: "Every formula, package, artwork file, and finished good is linked in one seamless data thread, eliminating gaps and guesswork." — the linked-definition estate.
- Lifecycle: "streamline change management across the entire development cycle"; "research ingredients, manage specifications, develop formulas, align packaging and artwork, and ensure ongoing compliance—accelerating speed to market."
- Finished Goods product: "Manage complex supplier and co-man/co-pack relationships, and get an instant, audit-ready view of all documentation." — finished-goods records as the product center.
- Marketing posture: blog "Why Networked Product Development Is Replacing Traditional NPD" — the network pole pitches against traditional NPD/PLM tooling while structurally covering the same span.
- Prior pass evidence (food-formulation, 2026-09-08): TraceGains pitches Formula Management against "traditional PLM" — consistent.

### Foods Connected Specifications & NPD — spec core + bundled NPD stage-gate

Evidence layer: A (direct observation of the official solution page).

- One solution bundling specification management and NPD: "Take control of your product development lifecycle... Empower your technical and NPD teams with automation, collaboration, and full visibility from concept to launch."
- NPD machinery: "Use our Workflow Manager for real-time collaboration across different functional departments. Create a single path for PLM and NPD to manage the end-to-end process from concept to launch." Features: Stage Gate Process Control; Collaborate Internally & With Customers; Fully Configurable Process & Format; Deadline Tracking & Gantt Charts; Recipe Development; QUID & Nutritional Data Management.
- Spec kinds: Retail Pack, Raw Material, Packaging, Complex Ingredients, Manufacturing Process specifications — with version control and change tracking (Manufacturing Process Specs: "Change Tracking & Version Control").
- FAQ: "The NPD workflow enables you to manage the entire product development lifecycle – from initial concept to launch. It includes task assignments, milestone tracking, collaboration tools, and document version control."
- The vendor also markets a "Product Lifecycle Management Guide" (CTA on the page) — PLM vocabulary used for the spec+NPD bundle.
- Suite context: integrates with Quality Management, Supplier Management, Traceability modules.

### Specright — spec-first PLM

Evidence layer: A (direct observation of official pages).

- Self-definition: "Specright's modern product lifecycle management software puts specifications — ingredients, packaging, formulas, and BOMs — at the core of your product lifecycle." "PLM That Starts With the Spec — Purpose-built to manage what Food & Consumer Goods products are made of—formulas, ingredients, packaging, and BOMs. From concept to commercialization, every spec stays aligned."
- F&B PLM definition (vendor's own words): "'Food & beverage PLM' means software that manages the full product lifecycle. It covers everything from ingredient and formula through packaging and label to finished product."
- The food-vs-discrete seam (vendor FAQ, verbatim structure): "Food-specific PLM is designed for process manufacturing. General PLM is designed mainly for discrete manufacturing... In food and beverage, ingredients are mixed, cooked, or blended into something new. They're also managed in batches using weights, volumes, and percentages instead of units. That means a formula is not a static parts list, but a flexible set of ratios that must scale, allow substitutions, and roll up allergen and claims data through every level. Food-specific PLM must therefore natively handle formulas and recipes, allergen and claims rollups, supplier ingredient data, and compliant label generation for each market."
- Anti-legacy framing: "Legacy PLM wasn't built for what food is made of. It was built for part numbers and assemblies, rather than formulas, ingredients, and packaging."
- Five-step lifecycle: Ideation & Concept → Design & Development → Manufacturing → Service & Support → End-of-Life ("Even after a product is retired, its specs stay in the system with full history and version tracking").
- Project Management module: "Track a product from ideation through formulation, finished good, and commercialization in one system. You gain a spec-first PLM with stage-gate workflows, tasks, and Gantt charts."
- Change propagation: "When one spec changes, Specright's patented SpecGraph shows every product it affects and updates them together."
- ERP handoff: "Specright does not replace your ERP. ERPs run the business; Specright runs the product and packaging data that powers it. Specright feeds spec data, item and material masters, and multi-level BOMs into the ERP, and pulls cost, supplier, and inventory data back."
- Modules: Product Data Management (formulas, ingredients, recipes, labeling as structured data), R&D Workbench (AI formulation), Project Management, Supplier Collaboration, Packaging Management.
- Market framing: hosts the Gartner "Market Overview for PLM Software in Food and Beverage Manufacturing" (2026) — "the market is shifting from fragmented point solutions toward connected, AI-enabled product platforms... purpose-built PLM has become essential." Bob Evans Farms case: SDM platform "powers a strong, efficient Product Lifecycle Management (PLM) process."

## Cross-product Comparison

| Structure | Centric | SpecPagePLM | TraceGains NPD | Foods Connected | Specright |
|---|---|---|---|---|---|
| Product record as center (product/finished-good/SKU to which all attaches) | Y ("all product data connected directly to each product") | Y (product master data in PDM core) | Y (Finished Goods records; data thread) | Y (specs per product/material) | Y (specs anchored to products; SpecGraph) |
| Definition as structured revision-controlled data (formula/spec/packaging versions) | Y ("track changes over time") | Y (formula versions, spec versions, histories) | Y (formula + spec + packaging spec products) | Y ("Change Tracking & Version Control") | Y ("full history and version tracking") |
| Controlled change / propagation through links | Y ("automatically update changes from formulation to artwork to marketing") | Y (traceability when components/formulations change) | Y ("streamline change management across the entire development cycle") | Y (workflow approvals, sign-off tracking) | Y (SpecGraph updates every affected product) |
| Development-to-launch lifecycle span (concept → launch → production handoff) | Y (concept to commercialization; design/sourcing/testing/launch) | Y (project & portfolio framework; ideation to finished product) | Y (source to shelf; development cycle) | Y ("single path for PLM and NPD... concept to launch") | Y (five-step lifecycle incl. manufacturing + end-of-life) |
| NPD project machinery (stage gates, briefings, tasks, Gantt) | Y (built-in workflows, project management role) | Y (the PLM product's differentiator: briefings, activities, resource planning) | Y (workflows; configurable) | Y (Stage Gate Process Control, Gantt) | Y (stage-gate workflows, tasks, Gantt) |
| Formulation/composition tools inside | Y (automate formulations, nutrient targets) | Y (in the PDM core: recipes, trials, optimization) | Y (Formula Management, NutriCalc) | Y (Recipe Development, QUID) | Y (R&D Workbench) |
| Specification management inside | Y (product specs tracked) | Y (in PDM core) | Y (separate product) | Y (the core of the bundle) | Y (the foundation) |
| Packaging specs + artwork workflow | Y (packaging & artwork role; label templates) | partial (packaging master data; label services separate) | Y (Packaging Spec Mgmt + WebCenter Go) | Y (Packaging Specifications kind) | Y (Packaging Management; label generation) |
| Supplier collaboration | Y (sourcing, supplier delays) | Y (supplier management pillar) | Y (Gather network; supplier data) | Y (supplier-invited spec editing) | Y (suppliers enter spec data directly) |
| ERP handoff | Y (implied; PXM/PIM separate) | Y (SAP GTIN connector; GDSN) | Y (integrations) | Y (module integrations) | Y (explicit: feeds item/material masters + multi-level BOMs to ERP) |
| Brands itself "PLM" | Y | Y | N ("NPD Suite") | partial (PLM guide; "single path for PLM and NPD") | Y ("spec-first PLM") |
| Industry scope | multi-industry (fashion→F&B) | food-native | food & beverage native | food-native, mid-market | multi-industry, F&B-emphasized |

Key readings:

- All five hold the four-leg generic-PLM core with food content. The record world is process-manufacturing: formulas/recipes as versioned ratio structures, allergen/claims rollups, packaging specs, artwork, supplier ingredient data, label outputs — not part numbers, CAD files, and assemblies.
- The NPD project machinery (stage gates, briefings, tasks, Gantt) appears in all five — but its weight varies from "the product's differentiator" (SpecPage: the PLM product IS the project layer) to "one module among four" (Specright). It is best classified as common mature structure, not definitional: a food PLM with lightweight change workflows but the full record + versioning + lifecycle span would still be recognizable.
- The vendor label varies: two brand as PLM, one explicitly refuses the label while holding the structure (TraceGains), one uses PLM vocabulary for a spec+NPD bundle (Foods Connected). The Type is structural, not label-defined.
- The data core (formulas, specs, master data) can live inside the PLM product or in a sibling product: SpecPage splits PDM from PLM; TraceGains sells Formula Management and Specification Management as separate products inside the NPD suite; Specright builds PLM modules on the SDM foundation; Foods Connected bundles NPD on the spec core; Centric embeds formulation in PLM. Packaging posture of the composition/spec layers varies — this is packaging, not identity.

## Canonical Abstraction

### L0 — Defining Invariant

The food & beverage manufacturer's system of record for the product's definition across its development-to-market life. Three jointly-held structures:

1. **The food product record as the unit of record** — a persistent, identified record of the product (and its SKU/packaging variants) to which the whole definition attaches: formula/recipe, specifications, packaging components, artwork, supplier/ingredient data, compliance status. Remove → a product registry, or disconnected formula/spec tools with no product center.
2. **The definition held as structured, revision-controlled data** — the product's definition exists as versioned structured records (formula versions, specification versions, packaging/BOM versions, artwork versions), so "which version is released/current" is always answerable, and a change propagates through links to everything affected. Remove → a document store or uncontrolled file share.
3. **The governed development-to-launch lifecycle** — the definition moves through a managed process (NPD projects with stage gates/briefings, or formal change workflows) from concept through release, with the released definition handed off to production/ERP and the history retained. Remove → product data management (data without the lifecycle) or project management over uncontrolled data.

Jointly-held load-bearing:

- 1 alone = product/master-data registry (PIM/PDM territory)
- 2 without 1+3 = versioned files with no product center or lifecycle
- 3 without 1+2 = generic project management over uncontrolled data
- 1+2 without 3 = product data management — exactly the SpecPDM pole that SpecPage sells as a separate product
- 1+3 without 2 = project tracking over spreadsheets (the state all vendors market against)
- 2+3 without 1 = change control over orphaned records

The food content of the record world is part of the invariant as this directory realizes the Type: formulas as scalable ratios (not static part lists), allergen/claims rollup through every level, packaging and artwork as first-class definition objects, supplier ingredient data flowing in. Remove the food record world and keep the four-leg container → generic PLM (§16).

### L1 — Common Mature Structure

Present across the sampled market; expected but not definitional:

- NPD stage-gate project machinery: briefings, tasks, milestones, Gantt/deadline tracking, configurable gate processes
- formulation/composition tooling inside the platform: recipe development, trials, simulations, optimization to nutrient/cost targets
- specification management and generated specification documents
- packaging specification management and artwork/label workflow
- nutrition/allergen/claims computation and compliant label generation outputs
- supplier collaboration: supplier-entered ingredient/spec data, certifications, questionnaires
- regulatory/compliance content and integrations (restricted-substance and market-regulation data)
- ERP handoff: item/material masters, multi-level BOMs, spec data fed to production systems
- portfolio/assortment and cost visibility

### L2 — Variant / Optional Structure

- Industry scope: food-native suites vs multi-industry consumer-goods PLM with an F&B edition
- Composition/spec packaging: embedded in the PLM (Centric), split as sibling products (SpecPage, TraceGains), or the foundation the PLM is built on (Specright, Foods Connected)
- Network posture: supplier-data networks as the differentiator (TraceGains Gather)
- Suite placement: PLM as one product beside planning/PIM/PXM products (Centric, SpecPage)
- Sustainability/EPR reporting, plastic-tax reporting, carbon data
- AI assistance (formulation workbenches, spec-grounded answer engines)
- Regulated-industry posture (21 CFR Part 11 support for life- sciences-adjacent F&B)
- Deployment: cloud/SaaS dominant; on-premises available in the European pole
- Customer scale: enterprise (Nestlé-class) to mid-market (Foods Connected) to startup (MeEat)

### L3 — Vendor-specific (Research Notes only)

- Specright: patented SpecGraph data model; Specification Data Management (SDM) trademark; named connector ecosystem (TOPS, Lorax, Trayak COMPASS, 1WorldSync, How2Recycle, PageProof); customer-reported metrics (19% duplicate-SKU cut, 21→11 days spec approval) — vendor-stated, not independently verified.
- TraceGains: Gather® supplier network; WebCenter Go (Esko artwork integration); NutriCalc; Regulatory Global (SGS Digicomply partnership).
- Centric: FoodChain ID integration; Visual Boards/PXM/AI Studio suite siblings; customer-quoted ROI figures (marketing).
- SpecPage: BLS/Ciqual/USDA nutrient databases; GDSN connectivity; SAP GTIN connector; ISO/IFS certification-based workflow framing; "90 percent less implementation effort" (marketing).
- Foods Connected: Workflow Manager branding; module suite (HACCP, traceability, procurement, CSR).

## Rejected Findings

- **"Food PLM = generic PLM with a food skin"** — rejected as an alias disposition. The record world differs structurally (process vs discrete manufacturing; formulas as ratios vs part lists; allergen/claims rollups; packaging/artwork as definition objects), the vendors themselves draw the seam, and Gartner treats "PLM Software in Food and Beverage Manufacturing" as its own market overview. Keep-both with a documented seam.
- **"Food PLM = Food Formulation Platform + projects"** — rejected. The formulation platform's core is the composition of record and its computed properties; the food PLM's center is the product record and the lifecycle over the whole definition estate (formula + spec + packaging + artwork + supplier data). Formulation is one leg of the definition, commonly embedded or sibling-sold. The SpecPage split (PDM vs PLM) shows the seam is vendor-real.
- **"Food PLM = Food Specification Management + stage gates"** — rejected as alias, confirmed as gradient. Spec management's core is the statement of record + approval/version lifecycle + trading-partner exchange; the food PLM adds the development lifecycle machinery around the whole estate. Foods Connected's spec+NPD bundle is the boundary case — it holds all three L0 legs and is therefore in-type, but its center of gravity is the spec core (posture gradient, recorded).
- **"The PLM label is definitional"** — rejected. TraceGains holds the full structure without using the label; Foods Connected uses the vocabulary for a spec-led bundle. Structure, not branding, defines the Type.
- **"NPD stage gates are definitional"** — rejected as L0; classified L1. All sampled products have them, but the load-bearing test (would the product still be a food PLM without configurable stage gates, using simpler change workflows?) passes — the record + versioning + governed span is what carries the identity.

## Boundary Findings

**vs Product Lifecycle Management / PLM (§16)** — industry-variant seam, keep-both. The sampled food products hold the generic four-leg core (product record + structured revision-controlled definition + controlled change + whole-life span) with food content. The seam is the record world: process manufacturing (formulas as scalable ratios, allergen/claims rollups, batch/weight/volume/percentage measures) vs discrete manufacturing (part numbers, assemblies, CAD). Vendor-drawn: Specright's own FAQ ("Food-specific PLM is designed for process manufacturing. General PLM is designed mainly for discrete manufacturing"); Centric ships the same PLM product across fashion and food with industry record content. Gartner maintains a distinct "PLM Software in Food and Beverage Manufacturing" market overview. Test: remove the food record world (formulas/specs/packaging/allergens) and keep the container → generic PLM; remove the lifecycle container and keep the composition → Food Formulation Platform.

**vs Food Formulation Platform** — composition core vs lifecycle container, keep-both (discharges flag 1). The formulation platform owns the formula of record + ingredient substrate + composition-driven evaluation; the food PLM owns the product record + the governed lifecycle over the whole definition estate. Composition flows into the PLM's product record. Vendor-real: SpecPage sells SpecPDM (data core incl. formulas) and SpecPagePLM (project/lifecycle layer) as separate products; TraceGains sells Formula Management as one product inside the NPD suite. "去掉什么就变成另一个 Type": remove the lifecycle container from a food PLM → the formulation/spec data core; bind the formula into the lifecycle container with the product record at center → Food PLM.

**vs Food Specification Management** — statement core vs lifecycle container, keep-both (discharges flag 2). Spec management owns the formal statement of record + approval/version lifecycle + trading-partner exchange; the food PLM adds NPD lifecycle machinery (projects, stage gates, artwork/critical path, launch) around the whole estate. The tested question — does the food-plm core add lifecycle machinery beyond the spec record? — answers YES, with vendor-split evidence (SpecPage) and module evidence (Specright Project Management as a PLM module). Foods Connected's spec+NPD bundle is the confirmed posture gradient: in-type, spec-centered emphasis.

**vs Food Labeling Platform** — label generation is one compliance output inside the food PLM (Centric: labels from PLM-populated templates; Specright: approved formulas → compliant labels); the labeling platform owns the jurisdiction rule sets and the label artifact as its core. Downstream sibling.

**vs Food Manufacturing ERP** — design-time vs run-time. The ERP consumes the released definition (Specright: "ERPs run the business; Specright runs the product and packaging data that powers it"); the food PLM governs the definition up to release. ERP-embedded recipe management (Aptean F&B ERP, Foodware 365 — per the formulation pass) is a variant placement of the composition core, not a food PLM.

**vs PIM** — commerce-facing product information vs development-side definition. SpecPage splits SpecPIM from both PDM and PLM; Centric ships PXM as a separate suite product.

## Uncertainties

- Deep help-center documentation was reachable only indirectly (SpecPage's Online Help portal exists at help.specpage.com but was not crawled module-by-module this pass; the sibling spec pass used the SpecPDM manual as its Tier-1 anchor). Claims about SpecPagePLM rest on the vendor's product pages.
- Exact stage-gate counts, gate names, and workflow defaults vary by product and are vendor-configured; no precise defaults are asserted.
- TraceGains' NPD Suite is treated as in-type on structural evidence (data thread + change management across the development cycle + finished-goods records); the vendor's own category vocabulary ("NPD", "networked product development") differs from "PLM" — the possibility that TraceGains positions a distinct-but-adjacent category is noted, not resolved.
- Gartner's F&B PLM market overview is known only through Specright's syndication of it; the report itself was not accessed.
- Historical samples (pre-cloud food NPD systems, desktop formulation/PDM tools of the 1990s–2000s) were checked by reasoning from the vendors' own "before" descriptions (spreadsheets, email, paper spec binders) rather than by direct documentation of those older products.

## Final Synthesis

A Food PLM is the food & beverage manufacturer's system of record for the product's definition across its development-to-market life. Its defining core is three jointly-held structures: the food product record (the persistent identified product to which formula, specifications, packaging, artwork, and supplier data attach), the definition held as structured revision-controlled data (versioned formula/spec/packaging/artwork records with change propagation through links), and the governed development-to-launch lifecycle (NPD projects/stage gates or formal change workflows moving the definition from concept through release, with the released definition handed to production/ERP).

The record world is food-specific: process-manufacturing content — formulas as scalable ratios rather than static part lists, allergen/claims rollups through every level, packaging and artwork as first-class definition objects, supplier ingredient data flowing in, compliant label generation as an output. This is the seam against generic/discrete PLM (keep-both, vendor-drawn, Gartner-recognized as a separate market), against the Food Formulation Platform (composition core vs lifecycle container), and against Food Specification Management (statement core vs lifecycle container).

The market realizes the Type in poles: multi-industry consumer-goods PLM with an F&B edition (Centric), food-native PLM split from a PDM data core (SpecPage), networked NPD suites that hold the structure without the PLM label (TraceGains), spec-core + NPD bundles (Foods Connected), and spec-first PLM (Specright). The NPD stage-gate machinery is the common mature structure; the PLM label itself is not definitional. All three pre-hung sibling flags discharge as keep-both with documented seams.
