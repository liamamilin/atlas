# Research Notes — Food Formulation Platform

## Research Goal

Understand what a Food Formulation Platform actually is from real products: what objects exist inside it, who uses it, how the formulation work flows, which structures are definitional vs. common vs. optional, and where its boundaries lie against the neighboring food-industry Types (Food PLM, Food Specification Management, Nutrition Analysis Application, Food Labeling Platform, Food Manufacturing ERP).

## Initial Boundary (hypothesis before research)

- Hypothesis: software for food & beverage R&D teams to compose product formulas (recipes) from ingredients with quantities, compute derived product properties (nutrition, cost, allergens, yield), iterate versions, and hand results off to specifications/labels/production.
- Likely confusions:
  - Nutrition Analysis Application (computes nutrition for a recipe — but does it hold the formula as the product's record of record?)
  - Food Specification Management (the spec is the product's formal statement — formula is upstream)
  - Food PLM (lifecycle wrapper — projects, packaging, workflow)
  - Food Manufacturing ERP (executes production — batching, lots)
  - Restaurant recipe/menu management (foodservice preparation consistency, not product development for manufacture)
- Unknowns: exact formula object structure per product; whether versioning is definitional; how deep supplier data goes; whether spec generation is part of the Type or a boundary.

## Research Questions

1. What is the formula/recipe object? What does it contain (ingredients, quantities, phases, yield, versions)?
2. What is the ingredient substrate, and what data does it carry (nutrients, cost, allergens, supplier specs)?
3. How does iteration work — versions, variants, trials, comparisons, what-if?
4. What is computed from composition vs. entered by hand (nutrition, cost, allergens, yield, declarations)?
5. What outputs does the system produce (labels, declarations, specs, production instructions)?
6. Who uses it, and what roles/permissions matter?
7. How does it connect to specs, PLM, ERP, and supplier data?
8. What variants exist (segment, region, deployment, packaging inside a suite)?

## Representative Products

Selected for market representativeness + documentation quality + different product philosophies + different customer tiers:

| Product | Vendor | Philosophy / pole | Customer tier |
|---|---|---|---|
| Genesis Foods (formerly Genesis R&D Foods) | Trustwell (formerly ESHA Research) | nutrition/label-led formulation built on a large nutrient database | SMB → enterprise, US-centric, also restaurants/foodservice |
| Formula Management | TraceGains | networked enterprise formulation connected to supplier/ingredient data | mid-market → enterprise CPG |
| SpecPDM | SpecPage (Revalize) | spec/product-data-led formulation for formula-based manufacturing, European certification workflows | mid-market → enterprise, EU-strong |
| NutriCalc (TraceGains NutriCalc) | TraceGains (UK origin) | standalone nutrition-calculation-led recipe tool, mid-market | SMB → mid-market |

Rejected/considered: ProductVision (PLM pole) — vendor site unreachable after 2 attempts (transport errors), abandoned per network rules. Aptean Food & Beverage ERP and Foodware 365 — fetched; both are ERP-pole products (traceability, production, QC) where formulation is not the center; used as boundary evidence, not representative products. innovate.com returned empty content; dropped.

## Sources

Tier 1 (official operational documentation):

- SpecPage Online Help — SpecPDM Manual (TOC, Recipe/Definition, Recipe/Recipe, Commit Recipe to Master Data): https://help.specpage.com/SpecPDM/en/ , https://help.specpage.com/SpecPDM/en/recipe_definition.htm , https://help.specpage.com/SpecPDM/en/rezeptur.htm , https://help.specpage.com/SpecPDM/en/rezeptdaten_an_material_ueberg.htm
- Genesis R&D Foods Knowledge Base (Trustwell/ESHA): https://genesisrdfoods.zendesk.com/hc/en-us , yield-adjustment article https://genesisrdfoods.zendesk.com/hc/en-us/articles/21197547183245-How-to-Best-Apply-Yield-Adjustments

Tier 2 (official product pages):

- Trustwell Genesis Foods: https://www.trustwell.com/products/genesis/food-formulation-and-labeling/ , https://www.trustwell.com/ , https://www.trustwell.com/support/
- TraceGains Formula Management: https://tracegains.com/product-development/formula-management/
- TraceGains NutriCalc: https://tracegains.com/product-development/nutricalc/
- TraceGains root (product line nav): https://www.tracegains.com/
- SpecPage root + SpecPDM page: https://specpage.com/ , https://specpage.com/product-data-management/

Research date: 2026-09-08.

Access limitations: TraceGains enterprise support help center (enterprise-support.tracegains.com) — transport error, abandoned after 1 attempt; TraceGains operational detail therefore rests on product pages (Tier 2). Genesis Foods (new generation) help center exists (genesisfoods.zendesk.com) but was not fetched; Genesis evidence combines the new-generation product page with the retired Genesis R&D Classic KB (Tier 1, product retired June 2026 — structure assumed continuous per vendor's own migration framing, flagged as an uncertainty). ProductVision unreachable — no claims made about it.

## Product A — Trustwell Genesis Foods (formerly ESHA Genesis R&D)

### Key observations (evidence layer A unless noted)

Positioning: "Formulate foods, analyze nutrients, and create government-compliant labels with a streamlined, all-in-one solution." "Start with a recipe and end with a label." R&D use case: "Access a database of over 90,000 ingredients to formulate, reformulate, and analyze with ease."

Documented workflow (product page, 5 steps):

1. Input ingredients — "adding your own or using our database of over 90,000 raw ingredients, whole foods, and proprietary and government-provided ingredients."
2. Adjust yields and ingredient amounts — "see automated nutrient calculations populate based on regulatory requirements."
3. Develop a label "with a click" — serving sizes, footnotes, nutrient content claims, ingredient and allergen statements.
4. Choose customizations — label formats for Mexico, Canada, Australia/New Zealand, EU.
5. Track formula changes "and different versions with audit tracking, save and re-use your favorite formulas, and monitor and manage all your recipes in one place."
6. Run custom nutrient reports — "analyze formulas and recipes, track costs and yields, and recalculate nutrient amounts based on yield changes."

Other directly observed:

- Nutrition analysis via database positioned as replacing analytical testing ("Eliminate the time and cost of analytical testing").
- Regulatory computation built in: "built-in calculations based on government regulations for nutrient rounding rules, RACC, and more"; nutrient content claims assessed as the label updates.
- API: distributes final product data (nutrient analysis, labels, allergen statements) to websites, POS, ERP; pulls data in to "automatically create ingredient and recipe records."
- Access rights to database records; verified users across stations.
- Genesis NutriLive: extends recipes/ingredients/nutrition data into restaurant digital menus (foodservice extension pole).
- Sibling product split (boundary evidence): Trustwell sells "Food Processor" separately as nutrition analysis software for dietitians/education, while Genesis Foods is formulation + labeling for product development. Same vendor, two Types.

Tier-1 KB (Genesis R&D Classic):

- Sub-recipes: a recipe can be added as the ingredient of another recipe (cookie example: Cookie Dough recipe → Cookie Base recipe → final Apple Filled Cookies recipe combining Cookie Base + Filling recipes). Spreadsheet Report verifies "the subrecipe's total contribution to the final recipe."
- Yield adjustments: Processing Loss and Moisture Loss (or Target) yield adjustments applied per recipe stage, "emulate the stages of the recipe in the same manner you would within the kitchen."
- Search and Replace: "replace an ingredient with another ingredient in all my recipes."
- Nutrients to View: configurable nutrient display in reports.

## Product B — TraceGains Formula Management

### Key observations (evidence layer A)

Positioning: "Networked Formula Management connects recipes to your specs, ingredients, and claims data, so you can experiment and create new products faster." Positioned against "traditional PLM and/or ERP systems" for NPD speed. Anti-pattern named: "critical formulations stuck on some desktop."

Four capability blocks (product page):

1. Centralize & digitize recipes — "store recipes, product concepts, and more for cross-team collaboration."
2. Research & reformulate — "Digitally model formula variations in minutes with access to real-time ingredient and supply data... unlimited variants."
3. Simplify reporting — "Create cost estimates, allergen reports, nutrition profiles, and more. Advanced calculations automate processes in R&D and beyond."
4. Audit & innovate — "a digital audit trail and roll-back capabilities"; "next-level version control."

Customer quote (Chief R&D Officer): "I can go in and look at the formulas and see their trials, see where they've been."

NPD suite context: Formula Management, Specification Management, Packaging Spec Management, Finished Goods, Regulatory Global, NutriCalc — formulation is one module of a suite; specification management is a separate product (boundary evidence).

## Product C — SpecPage SpecPDM (Revalize)

### Key observations (evidence layer A; Tier-1 manual)

Positioning: product data management for "formula-based food and beverage manufacturing... from concept to marketplace." "Formulation histories may be recalled on-demand." "Centralized product data repository."

Module map (manual TOC): Administration, Project, Master Data, Recipe, Calculation, Simulation, Search, Declaration, Production, Inspection Plan, Costing, Customs, Reporting.

Master Data module (tabs): Definition, Supplier, Attributes, Ingredients, Allergens, Minerals, Nutritional Values, Vitamins, Recipe Parameters, Laboratory Data, Status, Customs Info, Declaration, Recipe (a master-data object can itself be a recipe), Change Info. Functions: insert ingredient, assign supplier, assign nutrient database (BLS, Ciqual, USDA per product page), allergen cross-contamination indication, alternative materials, parent-child relationships, "Change Released Master Data", "Using Master Data Status in Calculation."

Recipe module — the deepest formulation evidence in the sample:

- Three identification levels: **Recipe** (recipe number) → **Variant** (variety number) → **Release version** (release number; "A recipe must have been released previously, before you can create a new version").
- Components: "raw materials, additives, pseudo items, components, semi-finished goods, weight loss/gain components, and packaging aids (with quantities and prices)."
- Sub-recipes: "A recipe normally consists of various components such as materials, additives, and sub-recipes"; right-click "Add recipe: Insert a sub-recipe into a recipe"; "Move to sub-recipe"; "Create sub-recipe" from selected components.
- Parameter auto-accept: "All parameters stored for the material or ingredient, such as calculations, allergens, nutritional values, vitamins... are automatically accepted into the recipe, when the components are assigned."
- Composition mechanics: mixing sequence (cooking instructions), preset quantity, overdosage %, quantity with unit, % content ("% out"), weigh-in/weigh-out, predefined/water/production losses, surplus %, density/volume, dry matter, Brix, Baker's percentage (GME%), special calculations (milk DS, cocoa content).
- Reconciliation rule: "Re-calculate to 100%... adjusts the base quantity to correspond with the sum of the components"; saving with sum ≠ base quantity triggers a confirmation; difference must be resolved by adjusting base amount or component quantities.
- Calculation base: weigh-in vs weigh-out (losses deducted from or added to 100%).
- Targeting (Dosi mode): dosage targeting "aims to achieve the defined target for the lowest price possible"; Carrier checkbox treats one component as the cheapest filler; linear optimization (GIPALS); rounding mode for manual quantity adjustment.
- "Added by consumer" components: included in the recipe but excluded from calculation and declaration (e.g., powdered drink mixed with milk at home).
- Alternatives: alternative materials ("in the case there is a shortage of the main material") and alternative recipes replaceable 1:1.
- Control & governance: processing status + control status (draft → released), special release, lock project, encrypt recipe, protect recipe (grant access), unreleased components displayed in a distinguishing color.
- Impact analysis: "Objects with which the recipe is used"; "List of related recipes" (parent recipes using this recipe as a sub-recipe).
- Project linkage: recipes linked to projects; "Generate Targeting Recipe" from a project briefing.
- Commit Recipe to Master Data: "Committing means transforming a recipe into a new Master data object. This is usually done when creating a finished or semi-finished product." Selective transfer of base data, prices, ingredients, allergens, minerals, nutritional values, vitamins, laboratory data, status; "Values... are a sum of all the values collected from the recipe's components"; unspecified (N.A.) component values can be highlighted.
- Batch conversion (filling), portion sizes, production specification (PL sheet / manufacturing instructions).

Calculation module: recipe parameters, allergens, minerals, nutritional values, vitamins, status, GDAs, maximum dosage; linked to recipes; targeting; pie chart.

Simulation module: selection, comparison, ingredients, targeting, variation, simulation plan, assessment; create simulation, comparison varieties, "Save Simulation Data into Recipe", "Create a New Recipe Variant from Simulation", price simulation, cost simulation, sub-recipe in simulation.

Declaration module: ingredient lists per declaration rules, semi-automatic declaration, tolerance ranges, allergen declaration, GDAs, maximum dosage. Product page: QUID in ingredient lists, allergen status (kosher, halal, vegetarian, vegan, organic), critical alarm functions, pre/post calculations.

Specifications (product page): "Automated management of product specification, ingredients and declarations list... Automatic generation of reports; product data sheets, allergen lists... Certification-based management in accordance with ISO and IFS standards... Audit workflows."

## Product D — TraceGains NutriCalc

### Key observations (evidence layer A)

Positioning: "Effortless and accurate nutritional calculation." "simple management of recipes, including sub-recipes and compound ingredients." "tens of thousands of ingredients at your fingertips and the ability to add customer ingredients on the fly." Compliant label formats "USA, UK, and international labels." "Nutritional reporting across products and ingredients." "You can use TraceGains NutriCalc standalone or integrate it with TraceGains Formula Management and Supplier Management." "calculate nutritional information as you create and modify recipes and track ingredient nutritional data."

Note: same vendor family as Product B but a distinct standalone product (UK-origin, mid-market pole). Evidence used to test whether the core structure holds in a thinner, calculation-led product.

## Cross-product Comparison

| Aspect | Genesis Foods | TraceGains Formula Mgmt | SpecPDM | NutriCalc |
|---|---|---|---|---|
| Central object | Recipe (with sub-recipes) | Formula (with variants, trials) | Recipe → Variant → Release version | Recipe (sub-recipes, compound ingredients) |
| Ingredient substrate | 90k+ ingredient database + user ingredients | networked ingredient/supplier data | Master data: materials w/ supplier, nutrients, allergens, certifications, status; nutrient DBs (BLS/Ciqual/USDA) | tens of thousands of ingredients + customer ingredients |
| Computed from composition | nutrients (regulatory rounding, RACC), allergen statements, cost & yield tracking | cost estimates, allergen reports, nutrition profiles | nutrients, allergens, minerals, vitamins, GDAs, max dosage, costing | nutrition (label-grade) |
| Iteration structure | formula versions + audit tracking; save & reuse | unlimited variants, version control, roll-back | variants + release versions; Simulation module | create & modify recipes |
| What-if / optimization | adjust & recalc | digitally model variations | Simulation (comparison, price simulation), targeting/linear optimization | — |
| Regulatory outputs | labels (US/CA/MX/EU/ANZ), ingredient & allergen statements, claims | allergen reports, nutrition profiles | Declaration (ingredient lists, QUID, allergen status), specifications, data sheets | label formats (USA/UK/international) |
| Yield / loss handling | yield adjustments (processing loss, moisture loss/target) | not evidenced on page | weigh-in/weigh-out, predefined/water/production losses, overdosage | not evidenced |
| Sub-recipes / nesting | yes (KB) | not evidenced on page | yes (Tier 1) | yes |
| Supplier linkage | via API/database; NutriLive for foodservice | core ("real-time ingredient and supply data") | core (supplier per material, multiple specs) | via suite integration |
| Audit / governance | audit tracking, access rights | audit trail, roll-back | control status, release, permissions, encrypt/protect, audit workflows | not evidenced |
| Handoff outward | API to ERP/POS/web | to specs, supplier docs, claims | commit recipe → master data; specifications; production instructions | integrate with Formula/Supplier Management |
| Projects / NPD workflow | not evidenced on page | product concepts stored | Project module (briefing, stages, activities, Gantt) | not evidenced |

### Evidence-layer rollup

- A (directly observed, per product): all cells above as marked.
- B (cross-product commonality): formula as central persistent object (4/4); ingredient data substrate (4/4); composition-computed nutrition (4/4); allergen determination (4/4); versioning/variants (3/4); cost computation (3/4); sub-recipe nesting (3/4); label/declaration outputs (4/4); audit trail (3/4); supplier linkage (2/4); yield/loss machinery (2/4); search & replace across formulas (2/4); project linkage (2/4).
- C (canonical inference): the Type is the manufacturer-side formulation system of record — see L0 below.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately minimal)

Three jointly-held structures:

1. **The formula of record** — a persistent, individually identified composition of ingredients with quantities (the product's recipe held as structured data, not as a document). Remove → recipe documents/listings with no system of record.
2. **The ingredient substrate** — ingredients held as records carrying the data (nutrients, cost, allergens, etc.) that formulas reference by identity. Remove → free-text recipes; nothing to compute from.
3. **Composition-driven evaluation** — product-level properties (nutrition, cost, allergen status, yield) computed from formula × ingredient data rather than hand-entered. Remove → a recipe archive/cookbook; the "formulation" work is gone.

Jointly-held is load-bearing: 1 alone = a recipe list; 2 alone = an ingredient database; 3 without 1+2 = a calculator; 1+2 without 3 = a recipe database with no computed properties; 2+3 without 1 = nutrition analysis of ad-hoc recipes (Nutrition Analysis Application territory).

### L1 — Common Mature Structure (standard in current products, not definitional)

- versioning / variants of formulas (iterations, trials) — near-universal in the sample but a development-loop affordance, not the definition
- sub-recipes / compound ingredients (nesting)
- yield & loss handling (moisture loss, processing loss, weigh-in/weigh-out)
- cost calculation
- allergen determination and allergen reports/statements
- nutrition computation per regulatory rules (rounding, serving sizes, reference values)
- label / declaration generation (nutrition panel, ingredient list, allergen statement)
- formula library: search, reuse, favorites
- audit trail / change history
- multi-user collaboration with access rights
- ingredient search & replace across formulas
- supplier/specification linkage per ingredient
- NPD project linkage

### L2 — Variant / Optional Structure

- optimization / targeting (linear optimization to nutritional or cost targets)
- simulation & price-simulation modules
- specification generation & management (boundary with Food Specification Management)
- supplier document collection (specs, COAs) — networked pole
- production instructions / PL sheets, batch scaling/conversion
- ERP/POS/web APIs and integrations
- multi-language declarations, multi-market label formats
- supplement-specific formulation
- foodservice/menu extension surfaces
- AI assistance (extraction, formulation suggestions)

### L3 — Vendor-specific (kept out of the final document)

- TraceGains: Gather® network, "Networked Formula Management" branding, AI Formulation landing positioning
- SpecPDM: GIPALS optimizer, Baker's percentage (GME%), VAL-I-PAC, Swissness, customs module, DS/Brix calculation modes, pseudo items
- Genesis: NutriLive, AskReg, ESHA Security/Port workflow utilities, Genesis Classic vs Genesis Foods generation split
- NutriCalc: competitive-comparison marketing claims

## Anti-overfitting checks

- Versioning is NOT definitional: NutriCalc (standalone pole) evidences recipe management and calculation without evidenced version machinery; the paper-era check below also satisfies the core without versioning. Held in L1.
- Supplier networking is NOT definitional: only the TraceGains pole makes it central; Genesis works from a static nutrient database; held in L2 (supplier linkage per ingredient is L1-adjacent but the live network is L2).
- Label generation is NOT definitional: it is the dominant output but a formulation system without label rendering (e.g., SpecPDM's declaration lists feeding separate spec documents) still is one; held in L1 as common, with labeling-first products being a different center of gravity.
- The database scale ("90,000 ingredients") is vendor-specific marketing precision — not carried into the final document.

## §24 Historical / Market-Sample Check

- Paper-era R&D kitchen (conceptual): recipe card with ingredient percentages + ingredient file with nutrient/cost data + hand-computed nutrition/cost per batch + trial sheets kept in a binder — satisfies all three L0 legs at analog level. No versioning software, no supplier network, no label rendering required.
- Spreadsheet era (conceptual): recipe workbook + ingredient data sheet + computed columns (nutrition, cost) — satisfies.
- Hobbyist brewing recipe software (conceptual, evidence layer C): formula (malts/hops/yeast with quantities) + ingredient data (potential, alpha acid, color) + computed ABV/IBU/color — structurally satisfies the three legs at hobbyist level; noted as an edge realization, not a representative product.
- Conclusion: L0 holds across eras and market positions; the modern sample's versioning/networks/labels are era features, not invariants.

## Vendor-specific Findings

See L3 above. Also: TraceGains positions Formula Management explicitly against "traditional PLM and/or ERP" — useful boundary evidence from a vendor's own framing. SpecPage splits SpecPDM (product data management) from SpecPagePLM (project/lifecycle) — same vendor separating formulation-data from lifecycle. Trustwell splits Genesis Foods (formulation+labeling) from Food Processor (dietitian nutrition analysis) — same vendor separating formulation from consumption-side analysis.

## Boundary Findings

- **vs Nutrition Analysis Application**: nutrition analysis computes nutrition for a recipe (dietetics, foodservice, education audiences — e.g., Trustwell's own Food Processor for dietitians); the formulation platform holds the formula as the manufacturer's product-development record of record and drives iteration. Seam test: who holds the recipe and why — analysis of an existing recipe vs. development of a product formula. Same-vendor product splits (Genesis Foods vs Food Processor) support the seam. Joint-review flag recommended (sibling unprocessed).
- **vs Food Specification Management**: the spec is the product's formal statement (attributes, declarations, data sheets) shared with customers/regulators; the formula is the internal composition that feeds it. TraceGains sells Formula Management and Specification Management as separate products; SpecPDM contains both with the formula upstream of the spec. Seam: composition of record vs. formal statement of record. Joint-review flag recommended (sibling unprocessed).
- **vs Food PLM**: PLM wraps the lifecycle (projects, workflow, packaging, artwork); formulation is the composition core. SpecPage separates SpecPDM from SpecPagePLM; TraceGains pitches Formula Management as faster than "traditional PLM." A formulation platform can be a component inside a PLM. Seam: composition of record vs. lifecycle container.
- **vs Food Manufacturing ERP**: ERP executes production (batching, lots, traceability); formulation designs the product. ERP-embedded recipe management (Aptean/Foodware pole, observed) is a variant placement of the same composition core. SpecPDM's production tab remains subordinate to the recipe. Seam: design-time composition vs. run-time production execution.
- **vs Food Labeling Platform**: labeling-first products start from compliance output; formulation platforms start from composition and generate labels as an output stage (Genesis: "start with a recipe and end with a label"). Seam: direction of the record.
- **vs Restaurant Menu/Recipe Management (foodservice)**: foodservice recipe tools serve preparation consistency and menu costing for kitchens; formulation platforms serve product development for manufacture. Genesis NutriLive shows the formulation system extending into foodservice, not the reverse.
- **"去掉什么就变成另一个 Type" 判据**: remove the formula of record → ingredient/nutrient database or analysis tool; remove composition-driven evaluation → recipe/document store; bind the formula into a lifecycle container with projects/packaging as the center → Food PLM; make the formal statement (spec) the center → Food Specification Management; bind composition to production execution → Food Manufacturing ERP.

## Uncertainties

- TraceGains operational detail (exact formula object fields, versioning mechanics) rests on Tier-2 product pages; the enterprise help center was unreachable. No precise operational claims made about TraceGains internals.
- Genesis Foods (new generation) help center not fetched; Genesis evidence combines the new product page with the retired Genesis R&D Classic KB. The vendor's own migration framing ("Genesis Foods builds on more than 30 years...") supports structural continuity, but exact new-generation mechanics are unverified.
- NutriCalc's cost handling and versioning were not evidenced; treated as unknown, not assumed absent.
- Whether "product concepts" in TraceGains constitute a first-class object (vs. marketing phrasing) is unverified.
- Market-size / share claims deliberately not researched; none made.

## Final Synthesis

A Food Formulation Platform is the food & beverage manufacturer's R&D-side system of record for product composition. Its defining core is three jointly-held structures: the formula of record (persistent identified ingredient composition with quantities), the ingredient substrate (ingredient records carrying the nutrient/cost/allergen data formulas reference), and composition-driven evaluation (product properties computed from formula × ingredient data). Around that core, mature products add the development loop (versions/variants, sub-recipes, yield/loss handling, simulation), the compliance outputs (nutrition per regulatory rules, allergens, labels/declarations), and the handoffs (specs, production, ERP). The market realizes the Type in several poles — nutrition/label-led (Genesis), networked/supplier-led (TraceGains), spec/data-led (SpecPDM), calculation-led standalone (NutriCalc), and ERP-embedded — all sharing the same composition core. The sharpest boundaries are against Nutrition Analysis Application (analysis of a recipe vs. development of a product formula), Food Specification Management (composition vs. formal statement), Food PLM (composition core vs. lifecycle container), and Food Manufacturing ERP (design-time vs. run-time).
