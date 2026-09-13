# Research Notes — Nutrition Analysis Application

## Research Goal

Understand what a Nutrition Analysis Application actually is from real products: what objects exist inside it, who uses it, how the analysis work flows, which structures are definitional vs. common vs. optional, and where its boundaries lie against the neighboring Types (Food Formulation Platform, Food Labeling Platform, Food/Calorie Tracking Application, Meal Planning Application, Nutrition Coaching Platform, Institutional Foodservice Management, Food Specification Management).

This pass also carries a JOINT REVIEW flag hung by the food-formulation-platform pass (2026-09-08): "sharpest seam — both compute nutrition from composition; discriminator = who holds the recipe and why: analysis of an existing recipe vs development of a product formula as governed versioned record; same-vendor split Trustwell Genesis Foods [formulation+labeling] vs Food Processor [dietitian nutrition analysis] supports two Types." This pass must independently ratify or refute that seam.

## Initial Boundary (hypothesis before research)

- Hypothesis: professional-facing software that computes the nutritional composition of recipes, menus, and diets from ingredient/food composition data, and delivers the results as nutrient reports, comparisons against reference standards, and label-ready values. Audiences: dietitians, foodservice, food producers, education, research.
- Likely confusions:
  - Food Formulation Platform (also computes nutrition from composition — but holds the formula as the manufacturer's product-development record of record)
  - Food Labeling Platform (also computes nutrition — but the compliant label of record is the terminal artifact)
  - Food/Calorie Tracking Application (also resolves food into nutrients — but person-facing daily consumption loop)
  - Meal Planning Application (plans future eating; analysis computes nutrition of compositions)
  - Nutrition Coaching Platform (coach-client relationship machinery)
  - Institutional Foodservice Management (menus bound to census, diet orders, production, money)
- Unknowns: whether the client/patient record is definitional or dietetics-pole-only; whether label generation is definitional or common; how the database substrate is realized across products; whether the education tier is a variant or a separate audience Type.

## Research Questions

1. What is the unit being analyzed (recipe, menu, diet recall, intake record)? What does it contain?
2. What is the nutrient reference substrate, and how is it realized (vendor-curated, public-source, user-added)?
3. What is computed, and what is delivered as output (reports, comparisons, labels, exports)?
4. What analysis frames exist (serving sizes, yields, portions, per-100g)?
5. What companion loops exist (client intake analysis, meal/menu planning, label generation, costing)?
6. Who uses it, per product and per tier?
7. Where is the seam against formulation, labeling, tracking, planning, coaching, institutional foodservice?
8. What variants exist (audience, deployment, database curation model)?

## Representative Products

Selected for market representativeness + documentation quality + different product philosophies + different customer tiers:

| Product | Vendor | Philosophy / pole | Customer tier |
|---|---|---|---|
| Food Processor | Trustwell (formerly ESHA Research) | dietetics/clinical/research pole — client-centered dietary analysis on a research-grade database; sold separately from the vendor's formulation product | professional dietitians, universities (dedicated education tier), healthcare |
| Nutritionist Pro | Axxya Systems | dietitian module family — Diet Analysis / Menu Creation / Food Labeling as separate modules; database also licensed raw | dietitians, hospitals, universities, food banks, restaurants, food companies |
| MenuSano | MenuSano (Konverge) | foodservice/producer cloud pole — label-output-led nutrition analysis for kitchens and small producers | restaurants, bakeries, caterers, SMB manufacturers, hospitals, schools |
| NutriCalc | TraceGains (UK origin) | manufacturer calculation pole — nutrition calculation inside an NPD suite; seam product vs formulation | SMB → mid-market food producers |

Rejected/considered: McGraw-Hill NutritionCalc Plus (education pole candidate) — vendor URLs 404 twice, abandoned per network rules; education tier instead evidenced via Food Processor for Education (dedicated vendor page) and Nutritionist Pro education testimonials. ProductVision considered and dropped by the formulation pass (unreachable) — not retried.

## Sources

Tier 2 (official product pages; no Tier-1 help centers were reachable this pass):

- Trustwell Food Processor: https://www.trustwell.com/products/food-processor-nutrition-analysis-software/ , education tier https://www.trustwell.com/products/food-processor-nutrition-analysis-software/education-purchase/ , vendor root https://www.trustwell.com/
- Nutritionist Pro: https://nutritionistpro.com/ , Diet Analysis module https://nutritionistpro.com/diet-nutrition-analysis/
- MenuSano: https://www.menusano.com/ (features, workflow, FAQ, industries, services)
- TraceGains NutriCalc: https://tracegains.com/product-development/nutricalc/

Research date: 2026-09-09.

Access limitations: McGraw-Hill NutritionCalc Plus unreachable (2× 404 on mheducation.com paths) — abandoned; no claims made about it. Vendor help centers / knowledge bases (menusano.zendesk.com, Trustwell KB, TraceGains enterprise support) not fetched this pass — operational detail rests on Tier-2 product pages; precise operational claims (exact nutrient field lists, exact rounding implementations, exact report counts beyond vendor-stated figures) are not made. Database-size figures (146,000 items; 90,000 ingredients; "tens of thousands") are vendor marketing claims recorded here as claims, not carried into the final document as facts.

## Product A — Trustwell Food Processor

### Key observations (evidence layer A unless noted)

Positioning: "Designed for dietitians, nutritionists, and healthcare professionals, Food Processor is a cloud-based software enabling comprehensive dietary tracking, exercise goal setting, and overall health monitoring for your patients." "Since 1984 nutritionists, dietitians, restaurants, and educational facilities have trusted the Food Processor for accurate recipe and nutrition analysis."

Five numbered capabilities (product page):

1. **Accurate Nutrition Analysis** — "Accurate nutritional information for each recipe, including calories, macronutrients, vitamins, and minerals. Adjust serving sizes and automatically recalculate nutritional information accordingly."
2. **Recipe Management** — "Easy and efficient data entry for recipes, including ingredients, quantities, and preparation steps."
3. **Comprehensive Database** — "An extensively researched food and nutrition database of more than 146,000 items including popular foods, restaurant items, ingredients, and recipes." (vendor figure)
4. **Dietary Filters & Organization** — "Categorize and tag recipes for easy retrieval and organization. Filter recipes based on specific dietary preferences or restrictions (e.g., vegetarian, gluten-free, vegan)."
5. **Robust Reporting** — "View, print, and share numerous professional reports and output for clients, diets, menus, and recipes."

Client work (dietetics pole):

- **Client Profiles** — "Record key individual traits such as age, weight, height, gender, activity levels, medical notes, and more."
- **Dietary Intake Analysis** — "Quickly see analysis results and accurately evaluate dietary intake for your clients. Instantly compare client dietary intake against recommended nutrient standards."
- **Tailored Recommendations** — "client-specific recommendations for weight modification and dietary requirements, with instant recalculations of caloric and nutrient intake based on recommendations entered."
- **Exercise Tracking** — "Design exercise regimens and calculate Metabolic Equivalent of Task (MET) for personalized fitness tracking" (references American College of Sports Medicine information).

Cycle menus & meal planning: "Create menu plans from frequently used foods and recipes"; "Quickly analyze menus and meals for nutritional value"; "Choose from generic DRI or specific client nutrient profiles for comparative analysis"; "Use the cycle option to see a week (or other range of days) at a glance."

Use cases named: Recipe Analysis, Dietary Intake Analysis, Cycle Menus (hospitals, cafeterias, healthcare facilities, schools), Nutrition Consulting (medical practitioners, dietitians, diabetes educators, athletic consultants, personal trainers, lifestyle coaches), Nutrition Research ("conduct research on dietary patterns"), Education ("Utilized by universities worldwide... training and educating students studying nutrition or aspiring to become registered dietitians").

Education tier (dedicated page): cloud-based; "up to 172 data fields, including proximates, vitamins, minerals, and other nutrient components" (vendor figure); students "analyze nutrient content quickly and accurately, learning to optimize recipes for nutrition goals, allergens, or specific dietary needs"; customizable reports; per-license annual pricing ($350/year — vendor figure, L3).

Boundary evidence from the vendor's own structure: Trustwell sells **Genesis Foods** (formulation + labeling) and **Food Processor** (nutrition analysis for dietitians/education) as separate products, plus a separate **Food Nutrition Database** product. Same vendor, three separable structures — the database is sold standalone, confirming it is a substrate, not the application.

## Product B — Axxya Nutritionist Pro

### Key observations (evidence layer A)

Positioning: "Your source for food nutrition labeling, diet analysis, and menu creation... a leading nutrition application designed and managed by registered dietitians. From food labels and menus to recipe calculations, it streamlines every aspect of your nutrition analysis workflow." "Since 1982, over 1,000,000 users..." (vendor figures). Compliance for USA, Canada, EU/UK, China/Hong Kong.

Three modules (product family structure):

1. **Food Labeling** — "Create and analyze unlimited recipes"; label formats for USA, Canada, UK/EU, China/Hong Kong; "Various label designs — Vertical, Aggregate, Dual Column, Horizontal, Front-of-package (FOP), Bilingual."
2. **Diet Analysis** — module features listed: "Diet recall, 24 hour, 3 day"; "Food Frequency Questionnaire (FFQ)"; "Meal Planning for patient and facility"; "Patient Nutrient, Exercise and Weight Goals"; "Recipe modifications to make them healthier"; "Latest Dietary Reference Goals"; "Over 55+ reports for education" (vendor figure).
3. **Menu Creation** — "Cycle Menus for conditions... High Protein, or Heart Healthy"; "Restaurant Menus made easier — Display calories on a menu board, comply with Menu Labeling"; "Compare menus against many nutrient goals—DRI goals or your own."

Diet Analysis module detail:

- "Monitor nutrient intake using the latest Dietary Reference Goals for each patient. Compare goals to keep patients on track."
- "Set Exercise Goals — Pick from a list of exercises to see calorie expenditure"; "Calculate Calorie Needs — Calculate using built in formulas... track weight over time."
- "24-hr or 3-day Diet Recall — Create recalls to see how your patient is eating, great for nutrition education"; "Food Frequency Questionnaire (FFQ) — To see how the patient is eating over time."
- Meal planning: "preset menus for various calorie levels or categories like Heart Healthy, High Protein"; "Use the DRI goals to see how the menu compares"; "Cycle Menu — Create weekly or monthly menus for hospital, schools or any other food service type facility."
- Reports: "over 55+ report options to help analyze diets, recipes, goals, menus and more"; named reports: MyPlate Analysis, Dietary Guidelines (2015/2020), Nutrient Deficiency, Nutrition Summary, Weight Management, Graphics Analysis, FFQ Form, Menu Report, Meals Report, Recipe Card, Recipe Yield, Shopping List, Food Profiling; PDF/CSV/RTF export; some Spanish-language reports.
- Audiences: "Dietitians, Hospitals, meals on wheels, non-profit programs, Universities, Colleges, Schools, Research, Wellness, Fitness, the Military and more."
- Deployment: PC install, individual and multi-user options (desktop-generation product with a new online label module).

Database: "Raw Nutrient Database of Foods and Beverages — use our database to calculate nutrition values for your mobile and web applications... a subset of the proven knowledge base that powers the Nutritionist Pro™ nutrition analysis software. Our staff of registered dietitians work continuously on the food database." Database licensing is a separate offering — again confirming the substrate is separable from the application.

Customer evidence (testimonials, layer A as vendor-published): Weight Watchers RDs "analyze thousands of recipes and menus"; Duke University Medical Center (large database, many nutrients); Loma Linda University graduate students evaluating 3-day food records; Greater Boston Food Bank (nutrition analysis + Nutrition Facts Labels + multi-day menus); Newk's Express Café (nutritional database for website); Fairmont Hotels (chefs evaluating recipes); Cengage Learning (database licensing).

## Product C — MenuSano

### Key observations (evidence layer A)

Positioning: "Easy-to-use software. USDA, CFIA, and FSA-compliant nutrition facts label generator. MenuSano includes nutrition analysis, recipe costing, experimentation features, and more." "MenuSano is an easy-to-use nutrition and supplement label generator. A cloud-based software that helps businesses in the food industry generate compliant labels."

Documented workflow (3 steps, product page):

1. **Build Your Recipe** — "Add ingredients manually or search our ingredient database to create your recipe."
2. **Customize Serving Details** — "Adjust serving sizes, yields, sugar levels, and portion settings."
3. **Generate Your Nutrition Label** — "Download a professional nutrition facts label with ingredients and allergen information."

FAQ-documented recipe flow: ingredient selection (database or custom) → quantity entry → serving size setting → yield adjustment/scaling → "The system handles all rounding rules automatically" → save recipe → select country and label type → specify allergens and dietary labels → export label in JPG or PDF → print. "Labels cannot be modified beyond CFIA, USDA, and FSA compliance requirements."

Key capabilities: "Instant Recalculations — Change one ingredient, and nutrition values update automatically"; recipe costing ("scale up or down recipes for accurate recipe amounts and costs"); recipe experimentation ("Experiment with new recipes and custom ingredients while being able to see the nutritional value of your dishes"); AI allergen detector ("scan recipes, identify potential allergens at the ingredient level"); cloud access ("Keep recipes, menus, and labels always up to date").

Industries served: restaurants, catering, meal kits, food manufacturers, food processors, cannabis edibles, bakeries, hospitals, retirement homes, public schools, school meal programs, culinary schools, pet food.

Services layer: "We Do It For You" (vendor generates labels), Lab Analysis Service (laboratory testing through lab partners), food service inspections partnership, MenuSano API.

Customer evidence (vendor-published testimonials): BonBon Collections — "Sending our recipes to a nutritionist, or out to a lab and having to wait three weeks for results is timely. Instead we use MenuSano, a web-based nutritional calculator"; Windmill Bakery — analysis revealed unexpected sodium, "which made us change some of our recipes" (analysis driving reformulation decisions); Bridgehead — "calculate our recipes with accuracy and instantly, it checks potential variations."

## Product D — TraceGains NutriCalc

### Key observations (evidence layer A)

Positioning: "Effortless and accurate nutritional calculation." "TraceGains NutriCalc allows simple management of recipes, including sub-recipes and compound ingredients. With tens of thousands of ingredients at your fingertips and the ability to add customer ingredients on the fly..."

Capabilities: "Compliant Label Formats — Global reach with USA, UK, and international labels"; "Insightful Reporting — Nutritional reporting across products and ingredients"; "Seamless Integration — enterprise integration and APIs"; "You can use TraceGains NutriCalc standalone or integrate it with TraceGains Formula Management and Supplier Management... calculate nutritional information as you create and modify recipes and track ingredient nutritional data with rich reporting."

Note: this product was sampled by the food-formulation-platform pass (2026-09-08) as its "calculation-led standalone" pole. This pass re-reads it from the analysis side: its center of gravity is nutrition calculation of recipes with label output — no evidenced versioning/trials/simulation/spec machinery on its own page. It is a seam product (see Boundary Findings).

## Cross-product Comparison

| Aspect | Food Processor | Nutritionist Pro | MenuSano | NutriCalc |
|---|---|---|---|---|
| Central analyzed object | recipe + client diet intake + menu | recipe + diet recall/FFQ + menu | recipe (+ menu context) | recipe (sub-recipes, compound ingredients) |
| Nutrient reference substrate | vendor research database (146k items claim; 172 fields claim) | vendor RD-maintained database (also licensed raw) | ingredient database + custom ingredients | tens of thousands of ingredients + customer ingredients |
| Computed output | nutrient profiles; intake vs standards; reports for clients/diets/menus/recipes | 55+ reports (MyPlate, Dietary Guidelines, deficiency, summary...); menu vs DRI | nutrition facts labels (USDA/CFIA/FSA), allergen info, reports | label formats (USA/UK/international), nutritional reporting |
| Analysis frame | serving sizes with auto-recalc; cycle-menu day ranges | calorie levels, DRI goals, custom goals | serving sizes, yields, sugar levels, portions, scaling | create & modify recipes |
| Client/patient layer | client profiles (age/weight/height/activity/medical notes) | patient nutrient/exercise/weight goals | none evidenced | none evidenced |
| Intake capture | dietary intake analysis vs standards | 24-hr/3-day recall, FFQ | none evidenced | none evidenced |
| Planning companion | cycle menus, menu plans from foods/recipes | meal planning, cycle menus for facilities | recipe experimentation | — |
| Label generation | not center (sibling Genesis does labels) | dedicated module, 4 jurisdictions | core output, 3 jurisdictions | core output |
| Allergens | recipe optimization for allergens (education page) | not evidenced on fetched pages | AI allergen detector at ingredient level; allergen info on labels | allergen labeling in positioning headline |
| Costing | not evidenced | not evidenced | recipe costing + scaling | not evidenced |
| Deployment | cloud | PC desktop + new online label module | cloud | enterprise/standalone |
| Audience center | dietitians, healthcare, universities, research | dietitians, hospitals, schools, food banks, restaurants | foodservice + small producers | food producers (NPD suite context) |

### Evidence-layer rollup

- A (directly observed, per product): all cells above as marked.
- B (cross-product commonality): recipe as central analyzed object (4/4); nutrient reference substrate (4/4); computed nutrition as the product's output (4/4); serving/portion/yield framing (3/4); report/output library (4/4); label generation (3/4 — absent-as-center in Food Processor, present as sibling); custom ingredients (3/4); planning companion (2/4); client/patient layer (2/4); intake capture (2/4); costing (1/4); allergen machinery (3/4).
- C (canonical inference): the Type is the professional nutrition-analysis loop over compositions — see L0 below.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately minimal)

Three jointly-held structures, held in an **analysis posture** (the composition is brought to be analyzed and reported on — it is not a governed product-development record being iterated toward manufacture, and not a person's own daily consumption log):

1. **The analyzed composition** — a user-defined recipe, menu, or diet/intake record (foods + quantities) held as the analysis subject. Remove → a nutrient database browser or calculator with nothing to analyze.
2. **The nutrient reference substrate** — a food/ingredient composition dataset the analysis resolves against (vendor-curated, public-source, or user-supplied). Remove → a recipe/menu manager with no nutritional meaning.
3. **The computed nutrition result as the product's output** — nutrient quantities derived from composition × reference data, delivered as nutrient profiles, comparisons against reference standards, reports, and/or label-ready values. Remove → storage without analysis; the "analysis" is gone.

Jointly-held is load-bearing: 1 alone = a recipe book/menu list; 2 alone = a nutrient database (a real adjacent product — two sampled vendors sell the database standalone); 3 without 1+2 = a bare calculator; 1+2 without 3 = recipe storage with nutrient data but no analysis; 2+3 without 1 = ad-hoc calculation below the Type.

The analysis posture is the load-bearing discriminator against the formulation platform (whose composition is the manufacturer's product-development record of record) — see Boundary Findings.

### L1 — Common Mature Structure (standard in current products, not definitional)

- persistent recipe/menu library with organization (tags, dietary filters, search)
- serving-size / yield / portion framing with automatic recalculation when composition changes
- comparison against nutrient reference standards (DRI-class goals, dietary guidelines, custom targets)
- professional report library with export/share (PDF/CSV-class formats)
- custom foods/ingredients added by the user
- allergen identification/declaration
- label generation (nutrition facts panels per jurisdiction) — dominant in producer/foodservice poles
- meal/menu planning companion (cycle menus, meal plans, templates)
- client/patient profiles with intake analysis (dietetics pole)
- diet recall / intake capture (24-hr, multi-day, FFQ) (dietetics pole)
- recipe costing (foodservice pole)
- database/API licensing (some vendors)

### L2 — Variant / Optional Structure

- audience packaging: dietetics/clinical, foodservice, producer/labeling-led, education, research
- database curation model: vendor-maintained research-grade (RD-staffed) vs public-source-derived vs user-supplied
- exercise/energy-expenditure tracking (MET-class) and weight-management goals
- multi-jurisdiction label formats (US/CA/UK-EU/CN-HK observed)
- services layer: done-for-you analysis, lab-testing partnerships
- AI features (allergen detection, ingredient matching)
- deployment: cloud vs desktop install
- edge realizations: pet-food analysis, cannabis edibles (observed industry pages)

### L3 — Vendor-specific (kept out of the final document)

- Food Processor: 146,000-item / 172-field database claims, MET exercise calculation, ACSM referencing, $350/yr education license, ESHA trademark lineage, eshacloud login
- Nutritionist Pro: "55+ reports", "since 1982 / 1,000,000 users" claims, three-module family split, raw-database licensing program, named client roster
- MenuSano: AI Allergen Detector branding, "We Do It For You" service, lab-analysis partnership, free tool suite (HFSS score calculator, IU converter, shelf-life calculator), compliance-constraint wording ("labels cannot be modified beyond...")
- NutriCalc: TraceGains suite integration framing, Gather® network, competitive-comparison marketing

## Anti-overfitting checks

- **Client/patient records are NOT definitional**: present in the two dietetics-pole products, absent in the producer/foodservice poles. Held in L1 (pole capability).
- **Label generation is NOT definitional**: 3/4 generate labels, but Food Processor — the archetype dietetics product — does not center labels (its vendor sells a separate labeling product). Held in L1 as common, pole-dominant.
- **Intake capture (recalls/FFQ) is NOT definitional**: dietetics-pole only. Held in L1.
- **Planning is NOT definitional**: companion capability in 2/4. Held in L1.
- **Cloud is NOT definitional**: Nutritionist Pro's core is PC-desktop generation. Held in L2.
- **Database curation model is NOT definitional**: vendor-curated vs public-source vs user-added all observed. Held in L2.
- **Database scale figures are vendor marketing** — not carried into the final document.
- **§24 historical check**: paper-era diet office — recipe/diet records on forms + printed food-composition tables (USDA Handbook-class) + hand-computed nutrient sums compared against recommended allowances — satisfies all three L0 legs at analog level; no software, no labels, no cloud required. The Type is also old as software: two sampled vendors trace their products to 1982/1984 (vendor claims), i.e., the software generation predates the modern web. L0 holds across eras.

## Vendor-specific Findings

See L3. Additional structural evidence: Trustwell's own catalog separates **Food Processor** (this Type), **Genesis Foods** (formulation + labeling), and **Food Nutrition Database** (substrate) — a same-vendor three-way split confirming analysis / formulation / substrate as separable structures. Axxya similarly licenses its raw database separately from the application.

## Boundary Findings

- **vs Food Formulation Platform** (JOINT REVIEW FLAG DISCHARGED — seam RATIFIED): both compute nutrition from composition, and both hold persistent recipes. The discriminator is who holds the composition and why: the analysis application treats it as an **analysis subject** — an existing recipe/menu/diet brought to be computed against and reported on (dietetics, foodservice, education, producer-calculation audiences); the formulation platform holds it as the **manufacturer's product-development record of record** — iterated through versions/variants/trials toward specifications, production, and labels. Same-vendor split (Trustwell: Genesis Foods vs Food Processor) supports two Types. The seam product NutriCalc sits on the seam: marketed inside an NPD suite, but its own evidenced center is nutrition calculation + labels with no versioning/trials/simulation — closer to the analysis pole; recorded as a boundary issue, not resolved as a Type split.
- **vs Food Labeling Platform**: analysis products end at nutrient values, comparisons, and reports; labels are one output among several (and absent-as-center in the dietetics pole). The labeling platform's defining output is the compliant label of record maintained through reformulation and regulation change. The labeling pass already recorded this seam from its side; this pass ratifies it.
- **vs Food/Calorie Tracking Application**: the tracker centers the person's self-serve daily consumption loop (log → nutrients → personal targets). The analysis application is professional-facing: the professional analyzes compositions (recipes, menus, client intakes) for reporting, planning, and labeling purposes. A client's intake record inside an analysis product belongs to the professional's analysis workflow, not the person's daily loop. The tracking pass recorded the same seam from its side ("§20 industry formulation/labeling vs personal consumption"); ratified.
- **vs Meal Planning Application**: planners center the future plan artifact (what to eat, plan → shopping list); analysis products center computed nutrition of compositions. Analysis products include planning companions (cycle menus, meal plans) — planning without the analysis loop is the planner; analysis without plan-first record-keeping is this Type.
- **vs Nutrition Coaching Platform**: coaching centers the managed coach-client relationship (roster, prescription delivery, adherence review). Analysis products center computation; client profiles exist as analysis context, with no coaching-relationship machinery observed.
- **vs Institutional Foodservice Management**: that Type binds menus to census, diet orders, production quantities, and money (operations system of record). Analysis products compute nutrition of menus/recipes for facilities without production/census/money machinery. Cycle-menu features here are analysis+planning surfaces, not foodservice operations.
- **vs Food Specification Management**: the spec is the product's formal statement of record exchanged with partners; analysis output is computed nutritional knowledge. No spec-authoring/approval/exchange machinery observed in this sample.
- **vs Restaurant Menu/Recipe Management (foodservice)**: menu management serves preparation consistency and menu operations; analysis products serve nutritional computation. Menu-calorie display (menu labeling compliance) is an output of the analysis, not menu operations.
- **"去掉什么就变成另一个 Type" 判据**: remove the nutrient reference substrate → recipe/menu manager; remove the computed result → recipe storage; make the composition a governed product-development record → Food Formulation Platform; make the compliant label the terminal artifact of record → Food Labeling Platform; make the composition the person's own daily log → Food/Calorie Tracking; make the future plan the record → Meal Planning; center the coach-client relationship → Nutrition Coaching; bind menus to census/production/money → Institutional Foodservice Management.

## Uncertainties

- Education-pole product coverage: McGraw-Hill NutritionCalc Plus unreachable (2× 404) — the education tier is evidenced via Food Processor's dedicated education page and Nutritionist Pro's education testimonials; a dedicated education-only product's structure is unverified. No claims made about NutritionCalc Plus.
- Operational depth rests on Tier-2 product pages this pass (no Tier-1 help centers fetched): exact report contents, exact nutrient field lists, exact recalculation mechanics, and database update cadence are unverified. No precise operational claims made in the final document beyond vendor-stated page content.
- NutriCalc's classification is seam-ambiguous (formulation pass claimed it as a pole; this pass reads its center of gravity as nutrition calculation). Recorded in STATUS Boundary Issues; not resolved as a Type split.
- Whether a research-grade pole product exists as a standalone (beyond Food Processor's research use case) was not sampled; no claims made.
- Market-size/share claims deliberately not researched; none made.

## Final Synthesis

A Nutrition Analysis Application is the professional-facing software that computes the nutritional composition of recipes, menus, and diets from a food/ingredient composition dataset, and delivers the results as the product's output — nutrient profiles, comparisons against reference standards, professional reports, and label-ready values. Its defining core is three jointly-held structures in an analysis posture: the analyzed composition (analysis subject), the nutrient reference substrate, and the computed nutrition result. Around that core, mature products add the recipe/menu library with recalculation, standards comparison, report libraries, label generation, allergen machinery, planning companions, and — on the dietetics pole — client profiles and intake capture. The market realizes the Type in several poles — dietetics/clinical (Food Processor), dietitian module family (Nutritionist Pro), foodservice/producer cloud label-led (MenuSano), and manufacturer calculation inside an NPD suite (NutriCalc, a seam product) — all sharing the same analysis loop. The sharpest boundaries are against the Food Formulation Platform (analysis subject vs product-development record of record — joint-review seam ratified), the Food Labeling Platform (analysis ends at values/reports vs label of record), the Food/Calorie Tracking Application (professional analysis vs personal consumption loop), and the Meal Planning Application (computed nutrition vs future plan artifact).
