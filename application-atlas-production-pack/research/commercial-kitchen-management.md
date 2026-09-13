# Research Notes — Commercial Kitchen Management

Research date: 2026-09-07
Slug: commercial-kitchen-management
Directory position: §20 Agriculture, Food & Natural Resources (line 1481)

## Research Goal

Understand what "Commercial Kitchen Management" software actually is in the real market: what objects it manages, what workflows it runs, who uses it, and where its boundaries lie against neighboring Types (KDS, Restaurant Inventory Management, HACCP Management, Food Manufacturing ERP, Institutional Foodservice Management, Restaurant Management System, Store Task Management).

## Initial Boundary

Initial hypothesis (before research):

- Commercial Kitchen Management = back-of-house production operations software for professional kitchens: recipes as structured production knowledge, production planning (prep lists / batches), food-safety execution (temperature logs, checklists), inventory/consumption linkage, food cost.
- Nearest neighbors suspected: Kitchen Display System (order tickets ≠ production planning), Restaurant Inventory Management (stock-centric), HACCP Management (food-safety-plan-centric), Food Manufacturing ERP (manufacturing business), Institutional Foodservice Management (meal-service programs).
- Known risk: the market term "kitchen management" is used loosely — at least one vendor (Crunchtime) markets its KDS under the name "Kitchen Management". The leaf must be defined so that it does not collapse into KDS.

## Research Questions

1. What are the core objects? (recipe, ingredient, sub-recipe, production plan, prep task, checklist, temperature log, stock record, waste record, supplier, purchase order)
2. What is the central workflow? (define recipes → plan production → execute prep → verify food safety → deduct stock → analyze cost)
3. How do recipes work as data? (ingredients, quantities, yields, sub-recipes, portions, scaling, allergens, nutrition, cost)
4. How does production planning work? (demand source → plan → prep tasks → assignee/workstation → completion)
5. How does food-safety execution work? (CCPs, checklists, temperature checks, corrective actions, labeling, audit reports)
6. How does inventory link to production? (depletion, counts, waste, stockable semi-finished output)
7. Who uses it, and on what surfaces? (chef/manager desktop, kitchen tablet, mobile, label printer)
8. Where are the boundaries against neighboring Types?

## Representative Products

Selected for market representativeness + documentation quality + different product philosophies + different customer tiers:

| Product | Philosophy / pole | Customer tier | Evidence quality |
|---|---|---|---|
| ApicBase | Recipe/food-cost data backbone + production planning + HACCP tasks (EU) | Multi-site groups, hotels, ghost kitchens, catering | Tier 1 help center (deep) |
| Kitchen CUT | F&B operations platform with compliance labelling + central production units (UK/global) | Hotels, restaurants, pubs, QSR, leisure; single-site (KC Lite) to groups | Tier 2 product pages (structured) |
| meez | Recipe-first "culinary system of record" (US) | Multi-unit restaurant groups; free tier for individual chefs | Tier 2 product pages + FAQ (deep) |
| Jolt | Frontline task/checklist + digital food-safety execution (US) | SMB restaurants, franchisees, multi-location | Tier 1 help center (deep) + Tier 2 pages |
| Crunchtime | Enterprise chain operations suite: inventory/food cost + ops execution + KDS + labor (US) | Enterprise restaurant chains (850+ brands claimed) | Tier 2 product pages + Zendesk help center |

Rejected / not researched:

- **Galley Solutions** ("culinary resource planning", institutional + commercial production planning) — identified as a market participant matching the production-planning pole, but all official surfaces were unreachable from the research environment (galley.co returned empty content ×2; help.galley.co transport error; docs.galley.co transport error; galley.solutions is a "Launching Soon" placeholder). Per source-access rules, no product claims are made about Galley; the production-planning pole is instead evidenced by ApicBase (production plans, menu cycles) and Kitchen CUT (CPU production lists).
- Restaurant365, MarketMan, MarginEdge — inventory/accounting-led back-office; appear in the sample only as integration partners of meez (documented on meez's site), not as primary samples. They anchor the boundary toward Restaurant Inventory Management / restaurant back-office accounting.

## Sources

Tier 1 (official operational documentation):

- ApicBase Help Center — https://support.apicbase.com/help (modules: Getting Started, Settings & Users, Menu Engineering, Allergens/Dietary/Nutritions, Procurement, Inventory, Sales, Planning, Traceability, Barcode Scanner App, Media, Insights Hub, API, AI, FAQ)
  - https://support.apicbase.com/help/planning (Tasks & HACCP / Production Plan / Menu Planning)
  - https://support.apicbase.com/help/guide-to-the-apicbase-production-module
  - https://support.apicbase.com/help/how-can-i-make-a-production-plan
  - https://support.apicbase.com/help/guide-to-the-tasks/haccp-module
  - https://support.apicbase.com/help/menu-engineering
  - https://support.apicbase.com/help/everything-you-need-to-know-about-stockable-recipes
- Jolt / SmartSense Help Center — https://help.smartsense.co/en/
  - https://help.smartsense.co/en/articles/9999196-getting-started-with-jolt-lists

Tier 2 (official product pages):

- Kitchen CUT — https://kitchencut.com/ (module pages: menu-engineering, allergen-nutrition-labelling, digital-menus, waste-management, procurement-purchasing-software, inventory-management, central-production-unit, business-intelligence-reporting, kc-lite; sector pages: hotels, restaurants, pubs-bars, quick-service-restaurants, leisure)
- meez — https://www.getmeez.com/ (feature pages: organization, costing, scaling, inventory-management, nutrition-labeling, kitchen-training, allergen-management, menu-engineering, analytics-dashboard, invoice-processing; FAQ)
- Crunchtime — https://www.crunchtime.com/ (suite-overview, inventory-management, food-cost-management, restaurant-forecasting, labor-and-scheduling, operations-execution, temp-monitoring, food-prep-labeling, kitchen, host, operational-intelligence, learning-and-development)
- Jolt — https://www.jolt.com/ (products: task-management-lists, remote-temperature-sensors, labeling-system, information-library, employee scheduling, time clock, communication manager)

Research limitations:

- ApicBase marketing site (apicbase.com / www.apicbase.com) returned HTTP 405; positioning evidence for ApicBase comes from its help center structure and the help-center link to get.apicbase.com.
- Galley Solutions unreachable (see above) — production-planning pole covered by other samples.
- meez Help Center (intercom.help/getmeez) timed out twice — meez evidence is from its official product pages and FAQ only.
- No pricing, numeric limits, or plan-gating details were asserted anywhere; none were needed for the canonical model.

## Product Observations

### ApicBase (evidence layer A — direct observation, Tier 1 help center)

Help-center module map: Getting Started · Settings & Users · **Menu Engineering** (Ingredients / Recipes / Menus / Advanced) · Allergens, Dietary and Nutritions · **Procurement** (Ordering / Receiving / Suppliers / Supplier Integrations) · **Inventory** (Counting / Stock Management) · **Sales** (Sales Management / PoS Integrations) · **Planning** (Tasks & HACCP / Production Plan / Menu Planning) · **Traceability** (NiceLabel) · Barcode Scanner App · Media (incl. APIC Studio) · Insights Hub · API · AI.

Menu Engineering (the knowledge base):

- Ingredients: package sizes, package & pricing information, price history, supplier per ingredient, weighted articles (sold by weight), custom fields/categories, import/export (Excel), verification & merging, archiving/deletion, "filling out ingredients for food cost".
- Recipes: create/delete/bulk-edit; **food cost calculation**; **Bill of Materials (BoM) generation** per recipe and per menu; **sub-recipes**; **stockable recipes** (semi-finished products held in stock); production time & costs per recipe; **preparation waste percentage**; auto-calculation of recipe weight/volume; recipe sheets export/print; QR-code sharing; kitchen utensils; translations; recipes produced by an **internal supplier**; accounting categories on stockable recipes.
- Menus: create; BoM for a menu; export; bulk edit.
- Advanced: stock variants; used-by/best-before dates + storage conditions on labels; ESG/footprints & "My Emissions"; cloning; Apicbase ID.

Planning (the production loop):

- **Tasks & HACCP**: start from the HACCP plan → define **Critical Control Points (CCPs)** → add HACCP tasks to CCPs → track task progress and **irregularities** → generate **reports from tasks and audit logs** for HACCP checks. Managed by library users or outlet users with the right permissions.
- **Production Plan**: create per **outlet** → name the plan → drag recipes/menus into "Planned Tasks" → per task enter **portions/units, assignee, workstation** → **sub-recipes are automatically added in the right amounts** (can be unchecked if already in stock) → optional **custom tasks** (e.g., cleaning stations, taking out trash) → save. Lifecycle: create → **activate/start** → manage → continue → **complete**. Production plan runs can be **scheduled**. A **BoM** can be used in the production module.
- **Menu Planning**: menu cycles; editing cycle instances; **ordering, selling and planning production from a menu plan**.
- **Internal ordering / production kitchen**: outlets order from production kitchens; production module works together with internal ordering; recipes can be produced by an internal supplier.

Inventory & linkage:

- Inventory: counting, stock management, transfers, waste registration, automatic stock tracking; barcode scanner app for counts and adding products.
- Sales: connect ePOS; link PLU items to Apicbase recipes; sales analytics per recipe.
- Traceability: "track every product's journey from purchase to sale"; labels with used-by/best-before and storage conditions (NiceLabel integration).
- Stockable recipes: register a **'create-event'** to add semi-finished product to stock.

### Kitchen CUT (evidence layer A — direct observation, Tier 2 product pages)

Self-positioning: "Hospitality Management Software" transforming "front- and back-of-house operations"; "Designed by hospitality operators, for hospitality operators"; sectors: hotels, restaurants, pubs & bars, QSR, leisure venues; a **KC Lite** edition for single-site businesses.

Module map: **Menu Engineering** · **Buffet Management** · **Allergen, Nutrition & CO² Emissions Labelling** · **Digital Menus** · **Waste Management** · **Procurement and Purchasing** · **Inventory Management** · **CPU and Warehouse Solutions** (central production unit) · **Business Intelligence Reporting** · Integrations (EPoS, accounts, purchasing; "200+ integrations", "3,000+ suppliers" claimed on marketing pages).

Key mechanics observed:

- Chefs get "live-costed menus, allowing them to change prices, ingredients, allergens or substitute products in real-time"; live pricing data re-calculates dishes and menus automatically; margin alerts.
- Purchasing workflow ranges "from basic order and receipt to Accounts Payable automation" with AI-driven invoice extraction matched to goods received.
- Inventory: PAR levels, live stock data, waste management.
- **CPU module**: central production units "prepare and plate meals to multiple outlets"; manage "internal stores, concessions, cellars, franchises and your central kitchen in one application"; "full traceability of ingredients and allergens per recipe for every outlet you supply"; "convert batch recipes to sales"; "create production lists to manage future deliveries"; "place orders with CPU and supplier in one order"; "automate stock replenishment"; "buy in bulk and despatch in single units using the same production profile".
- Compliance: allergen & nutrition labelling kept live; digital menus auto-update substitutions "guaranteeing compliance with allergen and nutrition laws"; CO² emissions labelling.

### meez (evidence layer A — direct observation, Tier 2 product pages + FAQ)

Self-positioning: "Recipe Management & Food Costing Software"; "Your recipes are your margins"; "a single source of truth for recipes, prep, training, and menu engineering"; "culinary system of record"; "designed by chefs, for chefs"; audience: culinary leaders, ops leaders, owners, training leaders, finance leaders; multi-unit restaurant groups.

Feature map: **Recipe Management/Organization** (searchable, version-controlled recipe hub replacing binders/PDFs/shared drives) · **Food Costing** ("laser accurate food costs by accounting for yields, UoM, prep loss") · **Recipe Scaling** ("one-click scaling with automatic unit conversions and precise yields"; "scale recipes for 5 covers or 500") · **Inventory Management** ("know what you have in your dry storage, freezer, or your walk-in") · **Nutrition Labeling** (built-in ingredient database; USDA-linked; FDA-formatted labels) · **Kitchen Training** (visual step-by-step recipe training; photos/videos per prep step) · **Allergen Management** (auto-tagging; updates disclosures when ingredients change; FOH access) · **Menu Costing & Engineering** (recipe data connected to sales; test portion/pricing/ingredient changes in real time) · **Menu Analytics** · **Invoice Scans & Processing** (vendor invoices sync ingredient costs).

Positioning vs back office: "meez is not accounting software… It acts as the missing culinary layer on top of systems like Restaurant365… Unlike ERPs that track what you *did* spend, meez shows you what you *should* have spent." Native integration with Restaurant365 (ingredient costs flow in; yield-adjusted, production-ready recipe data syncs back); other integrations: MarketMan, MarginEdge, Ottimate, Over Easy Office.

Workflow ("From recipe chaos to recipe clarity in 5 steps"): upload recipes (AI capture from docs/PDFs/handwritten notes) → attach training content (photos/videos per step) → connect vendors/invoices for real-time costs → engineer the menu (test changes against food cost %, margin, revenue) → roll out across locations (push recipe updates, menus, training; monitor per location).

### Jolt (evidence layer A — direct observation, Tier 1 help center + Tier 2 pages)

Self-positioning: "Operations Management Software for Restaurants & Business"; now part of SmartSense (Digi). Products: **Jolt Lists** (task management with accountability), **Jolt Sensors** (remote temperature monitoring with alerts), **Temperature Probes** (take and record food temperatures with digital logs), **Labeling System** (date-code labels), **Information Library** (training/content hub), **Employee Scheduling**, **Time Clock**, **Communication Manager**. Industries: food service (restaurants, K-12 nutrition), grocery, healthcare, retail, car washes, hotels.

Jolt Lists mechanics (help center, "Getting started with Jolt lists"):

- List templates built in the web portal, synced to the app; folders per **location** plus a **Content Group** (lists shared across all locations).
- **Item types** define how a task is completed: checkbox, photo, QR-code scan, measurement (probe/sensor), rating, yes/no variables.
- **Every completed item documents when it was completed and who completed it** (signed-in employee; personal mode or PIN).
- Item options: points (gamification), N/A / out-of-order options, **display criteria** (conditional follow-up tasks based on a previous answer), background colors, media attachments from the Information Library, labels attached from the Labeling subscription.
- Bulk import of items from spreadsheets/documents.
- **List scheduling**: start time (appears), **due time** (late after), **expiration time** (closes); repeat by day-of-week / day-of-month / intervals / date ranges; multiple display times per list.
- **Role-based access**: "Anyone can complete" vs role-restricted ("Assigned"); "Managed" column grants admin rights on the list (change due time, delete, manually enter measurements).
- **Notifications**: roles receive email/text/push on **overdue** items or **out-of-range** measurements/ratings.

Digital food safety: temperature probes and IoT sensors feed digital logs; alerts when conditions go out of range; date-code labeling reduces labeling errors.

### Crunchtime (evidence layer A — direct observation, Tier 2 product pages)

Self-positioning: "Restaurant Operations Management Suite"; "connects every part of the operations lifecycle"; targets multi-unit restaurants (claims 850+ brands, 150,000+ locations).

Suite map: **Inventory Management** (inventory lifecycle, counting, recipe management, reconciliation, purchasing from vendors, AI forecasting, **Food Cost Management (AvT)** — actual-vs-theoretical food cost) · **Labor & Scheduling** (AI scheduling, labor cost management, labor-law compliance) · **Operations Execution** (recurring and ad-hoc tasks: product rollouts, monthly quality audits, daily opening checklists; real-time completion visibility; automated alerts and follow-up tasks; **Temp Monitoring**; **Food Prep Labeling**) · **Kitchen Management** — *defined by Crunchtime as "Kitchen Display System (KDS) software that manages demand, directs order flow, and keeps every station in sync"* · **Guest Management** (host stand) · **Operational Intelligence** (Insights, Data Streaming) · **Learning & Development** (restaurant courses) · Integrations.

Boundary-relevant fact: Crunchtime's product named "Kitchen Management" is a **KDS**, not back-of-house production management. The market term is ambiguous; the directory keeps KDS as a separate leaf, so this leaf must be defined around production management, not order-ticket display.

## Cross-product Comparison

| Capability | ApicBase | Kitchen CUT | meez | Jolt | Crunchtime |
|---|---|---|---|---|---|
| Kitchen site as organizing unit (outlet/location/stations) | ✔ outlets, workstations | ✔ outlets, CPU, stores | ✔ locations | ✔ locations, content groups | ✔ locations/stores |
| Structured recipe library (ingredients × qty × yields, sub-recipes, portions) | ✔ deep (BoM, stockable, internal supplier) | ✔ live-costed recipes | ✔ deep (version-controlled, structured) | ✘ (no recipes; info library instead) | ✔ (recipe management inside inventory) |
| Food cost / costing | ✔ food cost calc, margin alerts | ✔ live costing, menu engineering | ✔ live costing, menu engineering | ✘ | ✔ AvT food cost |
| Production planning (plan → prep tasks) | ✔ production plans, menu cycles, scheduled runs | ✔ CPU production lists | ✔ scaling/daily production (prep) | ~ scheduled checklists | ~ forecasting → purchasing; prep labeling |
| Prep/task execution with attribution | ✔ assignee + workstation + progress | ✔ production lists | ✔ prep execution | ✔ item-level who/when | ✔ task completion visibility |
| Food-safety execution (temps, hygiene, corrective actions) | ✔ HACCP CCPs → tasks → irregularities → reports | ~ allergen compliance; food safety in CPU | ~ allergen tagging only | ✔ probes/sensors/logs/labels | ✔ temp monitoring, audits, labeling |
| Allergen / nutrition data | ✔ dedicated module | ✔ labelling module | ✔ auto-tagging + labels | ✘ | ✘ (not observed) |
| Inventory (counts, depletion, waste) | ✔ counting, transfers, waste, barcode app | ✔ PAR levels, waste | ✔ inventory + invoice scans | ✘ | ✔ counting, reconciliation |
| Procurement (suppliers, orders, receiving) | ✔ ordering/receiving/suppliers/integrations | ✔ purchasing + AP automation | ~ invoice processing, vendor price sync | ✘ | ✔ vendor purchasing, AI forecasting |
| Sales/demand linkage (POS → production) | ✔ ePOS → PLU → recipe | ✔ EPoS → menu engineering | ✔ sales → menu analytics | ✘ | ✔ sales forecasting |
| Traceability / labeling | ✔ purchase→sale traceability, date labels | ✔ per-recipe per-outlet traceability | ✘ | ~ date-code labels | ✔ food prep labeling |
| Labor / training | ✘ | ~ education services | ✔ kitchen training | ✔ scheduling, time clock, info library | ✔ labor & scheduling, L&D |
| Multi-site / central production | ✔ internal ordering, production kitchens | ✔ CPU module | ✔ multi-unit rollouts | ✔ content groups | ✔ enterprise chains |

Reading of the matrix:

- **Universal (5/5)**: kitchen site as organizing unit; some form of planned production work executed with attribution.
- **Near-universal (4/5)**: structured recipes; food cost; inventory linkage; allergen/nutrition data. Missing only at the execution pole (Jolt) — and Jolt is precisely the pole drifting toward Store Task Management / Food Safety.
- **Common (3–4/5)**: procurement; sales/demand linkage; traceability/labeling.
- **Pole-dependent**: labor, training, KDS, guest management — suite extensions, not definitional.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately small)

Commercial Kitchen Management is recognizable as this Type only if all three hold:

1. **The kitchen production site is the managed unit** — a physical kitchen (outlet/location) with workstations/stations is the container around which everything else is organized.
2. **Structured food-production knowledge** — what the kitchen makes and how, held as structured data: recipes composed of ingredients with quantities, yields, and portions; sub-recipes composing into parent recipes; cost derivable from ingredient data.
3. **The production loop: plan → prep → record** — the system turns production knowledge into planned production work (production plans / prep lists: recipe × quantity × assignee × workstation × time), the work is executed and completed with attribution (who did what, when), and completion is recorded.

Historical check (§24): older and simpler kitchen software (recipe-costing tools with prep lists; hotel kitchen systems; regional products) satisfies all three without any of the modern additions (POS integration, IoT sensors, AI forecasting, carbon labelling). A product with only #1 + #2 and no production loop is a recipe/costing tool (drifting toward a Recipe Management Type); a product with only #1 + #3 and no structured recipes is kitchen task execution (drifting toward Store Task Management / Food Safety Management). Both poles exist in the market (meez pole, Jolt pole) and are recorded as boundary findings, not as the definition.

### L1 — Common Mature Structure (very common, not definitional)

- **Food cost layer** — per-recipe/per-portion cost computed from ingredient packages & prices; live re-costing when prices change; margin views; menu engineering (sales-linked profitability).
- **Food-safety execution** — temperature checks (manual probe or IoT sensor), hygiene/cleaning checklists, corrective actions on out-of-range values, date-code labeling, audit-ready reports (HACCP-shaped: CCPs → tasks → irregularities → reports).
- **Inventory linkage** — ingredient stock records; counts; depletion driven by production and/or sales; waste registration; stockable semi-finished recipes (production output becomes stock via a create-event).
- **Allergen & nutrition data on recipes** — auto-propagated through sub-recipes and menus; disclosures for guests/FOH.
- **Multi-site structure** — outlets/locations; central production kitchens supplying outlets; internal ordering between sites.
- **Sales/demand linkage** — POS/EPoS integration; PLU→recipe mapping; sales mix informing production planning and menu engineering.
- **Procurement** — suppliers, purchase orders, receiving; supplier price feeds.
- **Insights/reporting** — food-cost variance (actual vs theoretical), task-completion rates, waste, per-site performance.

### L2 — Variant / Optional Structure

- Segment shape: full-service restaurants, hotel F&B, QSR chains, pubs/bars, catering/banquets, institutional foodservice, ghost/cloud kitchens, central production units.
- Pole emphasis: recipe/cost-data-led (ApicBase, Kitchen CUT, meez) vs execution/compliance-led (Jolt, Crunchtime Ops Execution).
- Scale packaging: single-site lite editions (KC Lite; meez free tier) vs multi-unit vs enterprise suites.
- Suite extensions that drift toward other Types: labor scheduling, time clocks, training/L&D, KDS, guest/host management, digital customer-facing menus, buffet management.
- Traceability depth: lot-level purchase→sale traceability, label printing integrations.
- Sustainability: CO²/emissions labelling, ESG footprints.
- Menu planning cycles (institutional/catering shape).
- AI assistance: recipe capture from documents, invoice extraction, forecasting, insights assistants.

### L3 — Vendor-specific (research notes only)

- ApicBase: Library vs Outlet user model; APIC Studio media production; Insights Hub; NiceLabel integration; barcode scanner app; "My Emissions"; Apicbase ID; weighted articles.
- Kitchen CUT: KC Lite edition; buffet management module; digital customer-facing menus; CO² labelling; hospitality consultancy/data services.
- meez: Recipe Upload Service (concierge import); native Restaurant365 two-way sync; "what you should have spent" positioning; 3,000+ ingredient database claim.
- Jolt: points gamification; Content Group vs Location list folders; SmartSense IoT sensor line; date-code label printers; communication manager.
- Crunchtime: AvT (actual-vs-theoretical) food cost framing; Zenput-derived Ops Execution; Squadle (temp monitoring); Teamworx (scheduling); its "Kitchen Management" product is a KDS (naming collision).

## Boundary Findings

| Neighboring Type | Relationship | Distinction (what makes them different Types) |
|---|---|---|
| Kitchen Display System / KDS | adjacent, **naming collision** | KDS manages live order tickets from the POS during service (demand-driven, minute-scale, station routing). CKM manages production knowledge, planning, and compliance (plan-driven, day-scale). Evidence: Crunchtime markets its KDS as "Kitchen Management" — the market term is ambiguous; the directory keeps them separate. Remove the production-knowledge/planning loop and only order display remains → that is KDS, not CKM. |
| Restaurant Inventory Management | capability overlap | Inventory-centric products manage stock as the primary object (counts, PAR, purchasing). In CKM, inventory is one loop serving production (recipes → prep → consumption). Inventory-led products (e.g., MarketMan-class) are a different center of gravity. |
| Restaurant Food Cost Management | specialization | Food-cost analytics is one L1 capability of CKM; a standalone food-cost product lacks the production loop and food-safety execution. |
| HACCP Management / Food Safety Management | adjacent | Food-safety-plan-centric products manage hazards, CCPs, monitoring schedules, and compliance documentation as the primary object. CKM embeds food-safety execution as one loop inside production management (ApicBase's Tasks & HACCP is a module, not the product). |
| Food Manufacturing ERP | adjacent | ERP serves a manufacturing business: financials, MRP, lot compliance, BOM-driven production orders, distribution. CKM serves foodservice kitchens with culinary semantics (menus, portions, POS linkage, guest-facing allergen data). ApicBase's BoM/internal-supplier features approach the seam but stay kitchen-shaped. |
| Institutional Foodservice Management | adjacent | Institutional products manage meal-service programs (resident/patient menus, nutrition care, tray service, cycles). CKM is the kitchen production layer beneath such programs; menu cycles appear in both (ApicBase Menu Planning), which is the overlap zone. |
| Restaurant Management System | broader | RMS includes front-of-house (POS, reservations, payments). CKM is back-of-house only; it integrates to POS rather than operating it. |
| Catering Management / Banquet Management | adjacent | Event-driven production for booked functions vs ongoing kitchen production. CKM supplies the production machinery; catering adds event/order context. |
| Store Task Management (§05.11) | cousin (execution pole) | Retail-store checklist/task execution. Jolt-shaped products sit between CKM's execution loop and Store Task Management; without structured recipes/production planning they are not CKM. |
| Recipe Management (no directory leaf) | pole drift | A recipe+costing system without production planning or food-safety execution (meez pole taken strictly) is drifting toward a Recipe Management Type. Recorded as a taxonomy observation, not silently merged. |

"去掉什么就变成另一个 Type" 判据：

- 去掉生产知识库与生产计划，只留订单工单展示 → KDS。
- 去掉配方/生产，只留库存与采购 → Restaurant Inventory Management。
- 去掉生产循环，只留食安计划与监控 → HACCP/Food Safety Management。
- 去掉厨房现场与烹饪语义，加上财务/MRP/批次合规 → Food Manufacturing ERP。
- 去掉生产循环，只留任务清单 → Store Task Management。

## Uncertainties

- Galley Solutions unreachable; the institutional/production-planning pole is inferred from ApicBase Menu Planning + Kitchen CUT CPU rather than from Galley itself. If Galley were researched, the L1 list might gain "culinary resource planning" (demand→ingredients→prep aggregation) as a named capability.
- meez Help Center timed out; meez's prep-execution depth (whether it has assignable production plans comparable to ApicBase's) is evidenced only at the level of its marketing pages ("prep execution", scaling, daily production). L0 #3 is still supported by 4/5 products directly.
- Exact plan-tier gating of modules (which capabilities are add-ons at which vendor) was not researched; no pricing claims are made.
- The exact shape of institutional foodservice overlap (menu cycles, nutrition care) is inferred from ApicBase's Menu Planning module and the directory's separate leaf; no institutional-only vendor was sampled.

## Final Synthesis

Commercial Kitchen Management is the back-of-house production management application for professional foodservice kitchens. Its world model is the kitchen as a production unit:

```text
Kitchen site (outlet/location, workstations)
└── Recipe library (structured production knowledge)
    ├── Ingredients (packages, prices, yields, allergens, nutrition)
    ├── Sub-recipes → parent recipes → menus
    └── Cost per recipe / portion
└── Production loop
    ├── Demand input (forecast / sales mix / menu cycle / internal orders)
    ├── Production plan / prep list (recipe × qty × assignee × workstation × time)
    ├── Prep execution with attribution (who, when, evidence)
    └── Completion
└── Food-safety loop
    ├── Temperature checks (probe / sensor) & hygiene checklists
    ├── Corrective actions on out-of-range values
    └── Date-code labeling + audit-ready records
└── Resource loops serving production
    ├── Inventory (counts, depletion, waste, stockable output)
    ├── Procurement (suppliers, orders, receiving)
    └── Insights (food-cost variance, completion, waste)
```

The defining core is small: kitchen site + structured production knowledge + the plan→prep→record production loop. Everything else — costing, food-safety execution, inventory, procurement, sales linkage, multi-site, insights — is common mature structure that makes the Type commercially valuable but does not define it. The market splits into a recipe/cost-data pole and an execution/compliance pole; products at either pole that lose the other loop drift toward neighboring Types (Recipe Management / Store Task Management / Food Safety Management). The sharpest naming hazard is KDS: at least one enterprise vendor sells a KDS under the name "Kitchen Management"; order-ticket display is a different Type.
