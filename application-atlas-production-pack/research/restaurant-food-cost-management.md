# Research Notes — Restaurant Food Cost Management

Research date: 2026-09-09

## Research Goal

Understand what "Restaurant Food Cost Management" applications actually are as a Type: their defining core structure, standard capabilities, variants, and boundaries against neighboring Types (Restaurant Inventory Management, Restaurant Procurement, Restaurant Menu Management, Restaurant Management System, Nutrition Analysis, Food Formulation Platform, Accounting Software).

## Initial Boundary

Initial hypothesis before research:

- Core use: control the money cost of food in a restaurant — cost recipes/plates, track actual food spend, compare theoretical vs actual, act on variance.
- Users: owner/GM, chef/kitchen manager, cost controller/bookkeeper.
- Nearest types: Restaurant Inventory Management (stock-centered), Restaurant Procurement (ordering-centered), Restaurant Menu Management (menu-content-centered), Restaurant Management System (broader suite).
- Key unknowns: (1) Is the theoretical-vs-actual variance loop definitional, or merely common? (2) Do pure recipe-costing calculators belong to this Type? (3) How do products compute the "actual" side (invoice-based vs inventory-depletion-based)? (4) Is this leaf a distinct Type or a capability of Restaurant Inventory Management?

## Research Questions

1. What is the central object — recipe, invoice, inventory, or cost report?
2. How is a recipe costed (ingredients, package sizes, units, yields, sub-recipes, waste factors)?
3. How is actual food cost computed (invoice line items, inventory counts/depletion, waste records)?
4. What is theoretical vs actual food cost and how is the comparison surfaced?
5. What actions follow from variance (portion control, re-pricing, waste reduction, supplier negotiation)?
6. What interfaces exist (dashboards, costing screens, invoice processing, count sheets, reports)?
7. What rules matter (unit conversions, yield factors, price-basis choice, recalculation triggers, sales-mix dependency)?
8. Where are the boundaries vs inventory / procurement / menu management / accounting?

## Representative Products

Selected for market representativeness + documentation quality + different product philosophies + different customer levels:

| Product | Philosophy / position | Customer level | Evidence quality |
|---|---|---|---|
| MarketMan | inventory-first cloud platform, food costing as profit layer | SMB independents → small chains | Tier 2 (product + solution pages, FAQ) |
| Craftable | hospitality back-office platform (restaurants + hotels) | mid-market / multi-unit | Tier 2 (product pages, case studies) |
| xtraCHEF by Toast | invoice-first cost analytics inside a POS platform | SMB → mid-market, Toast ecosystem | Tier 2 (product pages) |
| Apicbase | recipe-driven enterprise F&B management | enterprise / multi-unit / international | Tier 1 (help center articles) |
| Restaurant365 | broader restaurant management suite (accounting + inventory + workforce) | SMB → franchise/multi-location | Tier 2 (product pages, FAQ) |
| meez | recipe-first culinary layer ("your recipes are your margins") | chef-led groups, multi-unit | Tier 2 (product pages, FAQ) |

MarginEdge (a major invoice-first player) was selected but unreachable (transport errors on www.getmag.com and help.getmag.com) — limitation recorded below.

## Sources

Fetched 2026-09-09:

- MarketMan — https://www.marketman.com/ ; https://www.marketman.com/platform/recipe-costing-software
- Craftable — https://www.craftable.com/
- xtraCHEF by Toast — https://www.xtrachef.com/ ; https://xtrachef.com/features/food-cost-management/ (redirects to Toast product page)
- Apicbase Help Center — https://support.apicbase.com/ ; https://support.apicbase.com/help/menu-engineering ; https://support.apicbase.com/help/food-cost-calculation ; https://support.apicbase.com/help/insights-hub
- Restaurant365 — https://www.restaurant365.com/ ; https://www.restaurant365.com/inventory/recipes/
- meez — https://www.getmeez.com/
- MenuCalc — https://www.menucalc.com/ (boundary datum: pivoted to nutrition/allergen analysis)

Unreachable (abandoned after repeated failures per network rules): MarginEdge (www.getmag.com, help.getmag.com — transport errors ×3); Apicbase marketing site (www.apicbase.com / apicbase.com — HTTP 405 ×2; help center reachable instead); meez.com / www.meez.com (wrong domain; getmeez.com reachable); galley.co and restaurantcosting.com (empty responses).

## Product Observations

### MarketMan (evidence layer A unless noted)

- Self-labels "Restaurant Inventory Management Software"; nav solution pages include "Menu Costing" (/platform/recipe-costing-software). Positioning: "Manage Inventory, Invoicing, Purchasing, Recipe Costing, and COGS, All from One Easy-to-Use Platform."
- Recipe costing page: "calculates the profitability of each menu item based on your fluctuating distributor ingredient costs"; "ingredient-level cost breakdowns dynamically updated in real-time".
- **Actual vs Theoretical**: "Actual vs. Theoretical reports identify variances between inventory usage & theoretical usage to reduce theft, waste, & over-portioning." Case study: sports bar saved $600/month on unlogged soda usage (theft).
- FAQ: "pulls live ingredient prices from your purchase orders and inventory records, then calculates the cost per portion for each recipe. You can set target food cost percentages and instantly see which dishes are most and least profitable."
- FAQ: "When you receive a new invoice or update ingredient prices in MarketMan, all linked recipes recalculate automatically. You get instant alerts when a price change affects your menu profitability beyond a threshold you set."
- FAQ: sub-recipes ("prep recipes used inside other recipes"), modifiers, portion-level tracking supported; multi-location: "compare actual versus theoretical food costs per location."
- Pricing tiers: Starter (inventory/ordering/receiving, price tracking & alerts), Growth (+ waste tracking, AI recipe creation, real-time recipe costing, **automatic COGS**), Enterprise (+ AI ordering, order by recipe). Food-cost features are tier-gated.
- Integrations: POS (Toast, Square, Lightspeed, TouchBistro), accounting (QuickBooks, Xero), distributors (US Foods, Sysco, PFG).
- Customer quotes evidence the practice: COGS reviewed monthly; price-fluctuation flags used to challenge vendor price increases; waste/theft control.

### Craftable (evidence layer A)

- Self-labels "Hospitality's most intelligent back-office platform" for restaurants AND hotels. Modules: Intelligent Ordering, AP Automation, Inventory & Recipe Management, Daily Actionable Insights.
- Inventory & Recipe: "Know exactly what you have, what it costs, and where your variance is — in real time. Craftable connects physical counts to recipes and theoretical usage so you can spot margin loss before it hits the P&L."
- Daily Actionable Insights: "Food cost, labor, and purchasing data in one dashboard — not three different systems. Craftable surfaces the variances and trends that matter most."
- Case studies framed in food-cost terms: bartaco "50% reduction in food cost variance" ($30K/week saved); Sugarfire "spot actual vs. theoretical variance"; Jim's Steakout "$500K in food costs" in one year.
- AP automation: AI invoice scanning with line-item extraction and 3-way match to POs; "flag any price that drifts past your threshold."
- Claims: 5% lower cost of goods, 50% inventory-time reduction; 1,000+ POS/EDI/API integrations.

### xtraCHEF by Toast (evidence layer A)

- Old homepage: "Our suite of automated financial and operational management tools make it easy for any operator to better control food costs and maximize margins." Features list included a named **"Food Cost Management"** capability (direct vendor use of the leaf name).
- Toast product page: "restaurant back-office software for invoice automation, recipe costing, inventory management, and cost reporting… built for US restaurants and hospitality groups that need to track ingredient costs, monitor margins, reduce manual data entry, and connect purchasing data with accounting."
- "Monitor costs across all recipes — Gain insight into **plate costs and gross margins** by factoring fluctuating ingredient prices, labor and how product was sold (on/off premises)."
- Invoice automation unlocks line-item detail: "drill down into how fluctuating costs are impacting your financial performance"; ingredient price fluctuation alerts; gross margin variances per menu item.
- Positioned inside Toast's "Supplier & Accounting Suite" as "xtraCHEF cost analytics" beside "Inventory management" (separate Toast product) — vendor itself splits cost analytics from inventory.
- Roles: Culinary Management ("real-time food cost reporting"), Financial Management (back office), Operations, Outsourced Accountants.

### Apicbase (evidence layer A — Tier 1 help center)

- Help-center module map: Menu Engineering (ingredients, recipes, menus), Allergens/Dietary/Nutritions, Procurement (ordering/receiving/suppliers), Inventory (counting, stock management, waste registration, transfers), Sales (ePOS connection, PLU→recipe linking), Planning (production plans, HACCP tasks), Traceability, Insights Hub, API, AI.
- **Food cost calculation article** (recipe-level "Financial" tab; also available at menu level):
  - Food cost = ingredient cost + waste percentage (waste % per recipe or library default).
  - Personnel cost = labour time × cost per hour, with up to three hour prices (prepping / cooking / plating); optional (can be zeroed).
  - **Prime cost = food cost + personnel cost.**
  - Cost always expressed **for 1 portion/serving** even when the recipe yields multiple portions.
  - Required inputs: ingredient costs, ingredient weights/volumes; for margins: selling price (VAT-inclusive; VAT deducted), VAT %, target profit margin (library-wide default, per-recipe override).
  - Price basis selectable: **cheapest supplier package (default) vs last ordered package price**; per-outlet calculation.
  - Ingredients overview table: quantity, pricing, ingredient cost per serving and per recipe, waste cost, cost % of total; sortable to find the most expensive/most-used ingredient.
  - Target calculations: target prime cost (given actual sell price) and target sell price (given actual prime cost).
  - POS sync: recipes linked to POS PLUs can have prices updated automatically from the POS.
- Ingredients: package sizes, pricing, pricing history ("Check the pricing history of ingredients", "Keep track of the price evolution of your products"), preparation waste percentage on recipes, sub-recipes, **stockable recipes** (prep items held in stock), BoM generation for recipes and menus, weighted articles.
- Insights Hub: CoGS Dashboard, Inventory Evolution/Snapshot dashboards, Goods Receipt Dashboard, Management Figures Dashboard, procurement reports, inventory reports.

### Restaurant365 (evidence layer A)

- Broader suite: Accounting, Inventory & Purchasing, Workforce, Payroll & HR; self-labels "Restaurant Management Software" / "restaurant back office".
- Inventory product: "R365 AI integrates your recipes, purchasing, and inventory counts to surface waste, catch cost variances, and drive smarter purchasing decisions in real time, not at month end."
- Recipes page: "Uncover usage gaps by comparing **actual vs. theoretical food costs**"; "Track ingredient yield to account for trim, cut, and prep loss"; "Create 'batch' recipes that can be used across multiple other dishes"; "Link recipes to purchasing data to control ingredient spend"; "Keep menu items profitable by adjusting portions or pricing as soon as cost shifts happen"; "Pinpoint your top menu performers and underperformers."
- FAQ: "By linking recipes to purchasing and inventory data, the software ensures every ingredient is costed accurately, portions are standardized, and waste is minimized." Recipes connected in real time with inventory and sales.
- Webinar title evidences the operating rhythm: "Know Your Food Cost Before Count Day."
- Franchise benchmarking: franchisees "see immediately how their results compare" on "prime costs of food and labor."

### meez (evidence layer A)

- Self-labels "Recipe Management & Food Costing Software"; tagline "Your recipes are your margins."
- Food Costing: "Get laser accurate food costs by accounting for **yields, UoM, prep loss**, and more." Costs update automatically from vendor pricing/invoice scans.
- Menu Costing & Engineering: "See the impact of recipe and menu changes in real-time"; "Connect recipe data to sales to see the true profit contribution of every dish. Analyze food cost %, profit margins, and revenue impact. Plus, test changes in portion sizes, pricing, and ingredients in real-time before reprinting a single menu."
- **Boundary quote (vendor's own positioning)**: "meez is not accounting software… It acts as the missing culinary layer on top of systems like Restaurant365… **Unlike ERPs that track what you *did* spend, meez shows you what you *should* have spent.**"
- Native R365 integration: "ingredient costs flow from R365 into meez automatically, and yield-adjusted, production-ready recipe data syncs back into R365 for accurate inventory and cost reporting." Other integrations: MarketMan, MarginEdge, Ottimate, Over Easy Office.
- Also ships: recipe organization (version-controlled hub), scaling & conversions, kitchen training, allergen management, nutrition labeling, inventory management, invoice scans, analytics dashboard.
- FAQ: "eliminating unexplained food cost variance"; customers report 4–5% COGS reduction claims (self-reported).

### MenuCalc (boundary datum, evidence layer A)

- Now positions as "Nutrition Analysis Software" / "The Modern Nutrition & Allergen Analysis Software" — FDA-compliant nutrition/allergen analysis, not food costing. Demonstrates that nutrition analysis is a separate neighboring Type even though it shares recipe-decomposition mechanics.

## Cross-product Comparison

| Structure / capability | MarketMan | Craftable | xtraCHEF/Toast | Apicbase | R365 | meez |
|---|---|---|---|---|---|---|
| Costed recipe (ingredients → per-serving cost) | ✓ | ✓ | ✓ ("plate costs") | ✓ (Tier-1 detail) | ✓ | ✓ (core) |
| Yield / prep-loss / unit-conversion factors | ✓ (sub-recipes, portions) | ✓ | ✓ | ✓ (waste %, yields, stockable recipes) | ✓ (yield for trim/cut/prep loss) | ✓ (core: yields, UoM, prep loss) |
| Price feed from invoices/purchasing | ✓ (POs + invoices) | ✓ (AP automation, 3-way match) | ✓ (invoice automation, line items) | ✓ (packages/pricing, price history) | ✓ (purchasing link) | ✓ (invoice scans, vendor pricing) |
| Automatic recipe recalculation on price change | ✓ (+ threshold alerts) | ✓ (price-drift flags) | ✓ (price fluctuation alerts) | ✓ (price evolution tracking) | ✓ ("as soon as cost shifts happen") | ✓ (real-time) |
| Actual consumption side (counts / waste / depletion) | ✓ (counts, waste tracking) | ✓ (physical counts) | ✓ (inventory mgmt product) | ✓ (counting, waste, transfers) | ✓ (inventory counts) | partial (inventory mgmt; actual-side often via integrations) |
| Sales-mix link (POS → recipes) | ✓ | ✓ (POS integrations) | ✓ (Toast sales data) | ✓ (PLU→recipe linking) | ✓ (sales data) | ✓ (menu analytics via sales) |
| Actual vs theoretical variance reporting | ✓ (named report) | ✓ (core pitch) | ✓ (gross margin variances) | ✓ (CoGS dashboard) | ✓ (named capability) | ✓ ("should have spent" framing; variance via stack) |
| Food cost % / COGS reporting | ✓ (automatic COGS, tier-gated) | ✓ (dashboard) | ✓ (cost reporting) | ✓ (CoGS dashboard) | ✓ | ✓ (food cost %) |
| Target food cost % / target price / margin targets | ✓ (target food cost %) | ✓ (thresholds) | ✓ | ✓ (target margin, target sell/prime cost) | ✓ | ✓ (scenario modeling) |
| Per-item profitability / menu engineering | ✓ (most/least profitable dishes) | ✓ | ✓ | ✓ | ✓ (top performers/underperformers) | ✓ (core) |
| Waste tracking | ✓ (tier-gated) | ✓ | ✓ | ✓ (waste registration) | ✓ | (via inventory) |
| Multi-location comparison | ✓ | ✓ | ✓ (across locations) | ✓ (outlets) | ✓ (franchise benchmarking) | ✓ (rollouts) |
| Labor in plate cost (prime cost incl. labor) | — | ✓ (labor in dashboard) | ✓ ("factoring… labor") | ✓ (personnel cost, optional) | ✓ (prime cost of food and labor) | — |
| Purchasing/ordering bundled | ✓ | ✓ | ✓ (procurement) | ✓ (procurement module) | ✓ | — (partner feeds) |
| AP automation / invoice payment | ✓ (AP automation) | ✓ | ✓ (core) | — | ✓ (AP automation) | — (scans only) |
| Nutrition/allergen | — | — | — | ✓ (module) | — | ✓ (module) |
| Recipe training/sharing | — | — | — | ✓ (QR share, recipe sheets) | — | ✓ (core: kitchen training) |

Reading of the table (evidence layer B — cross-product commonality):

- The **costed recipe** with per-serving cost is universal (6/6).
- The **price feed** (invoices/purchasing → ingredient prices → automatic recalculation) is universal (6/6).
- **Actual vs theoretical variance** is named or structurally present in 6/6 (meez realizes the theoretical half natively and the actual half via integrations — its own positioning states the split).
- **Food cost % / COGS reporting** and **per-item profitability** are universal.
- Inventory counting, waste tracking, POS sales-mix linking are near-universal substrates for the actual side.
- Labor-inclusive prime cost is a variant (present in 4/6, absent/explicitly-optional in others).
- AP automation, purchasing, nutrition, training are bundled adjacent capabilities, unevenly present.

## Canonical Model

### L0 — Defining Invariant (deliberately small)

The Type is the restaurant's **food-cost control loop**. Three jointly-held structures:

1. **The costed recipe** — a menu item (or prep item) decomposed into costed ingredients with quantities, converted through package sizes/units and yield/prep-loss factors into a **per-serving cost**, held as a persistent record and **maintained as ingredient prices change**. Remove → inventory management (stock without costed dishes) or menu management (menu without cost).
2. **The actual food-cost record** — what the operation actually spent and consumed on food over a period, assembled from purchase prices (invoices/receipts), inventory depletion (counts), and recorded waste. Remove → a costing calculator with no operational record; the "actual" half of the loop gone.
3. **The theoretical-vs-actual comparison loop** — the expected cost of what was sold (recipes × sales mix) computed against the actual cost, with the **variance surfaced, attributed, and acted on** (portion control, re-costing, re-pricing, waste reduction, supplier negotiation). Remove → cost data without the management loop; the "management" in the Type name gone.

Jointly-held load-bearing checks:

- 1 alone = recipe-costing calculator (the outer edge of the Type; see Boundary Findings).
- 2 alone = spend tracking / accounting territory.
- 3 without 1+2 = nothing to compare.
- 1+2 without 3 = cost data without management.
- 2+3 without 1 = variance with no standard to vary from.

Note on realization: the loop is the Type's invariant, but a single product need not realize both halves natively — the meez pole realizes the theoretical half in-product and the actual half through integrations (its own positioning: "shows you what you *should* have spent" vs ERPs that track "what you *did* spend"). The Type survives as a stack; the loop must close across the stack.

### L1 — Common Mature Structure (standard, not definitional)

- Invoice processing / price capture (line-item extraction, coding, price updates) — universal in-sample
- Inventory counting & depletion as the actual-usage substrate
- Waste tracking with cost
- POS sales-mix integration (PLU→recipe linking)
- Food cost % / COGS reporting by period, location, category
- Price-change alerts / price-evolution history
- Per-item profitability / menu engineering views
- Target food cost % / target sell price / margin targets
- Sub-recipes / batch recipes; unit conversions; yield factors
- Multi-location standardization and per-location comparison
- Accounting-system integration (GL coding of costs)

### L2 — Variant / Optional Structure

- Labor included in plate cost (prime cost framing) vs food-only costing — Apicbase documents it as optional (hour prices can be zeroed); xtraCHEF/R365 factor labor; MarketMan/meez food-only in observed surfaces
- Price-basis choice (cheapest supplier package vs last ordered price — Apicbase documents both)
- Purchasing/ordering bundled (suggested orders, POs)
- AP automation / vendor payments bundled
- Beverage/alcohol cost programs (bar-specific costing)
- Commissary / production-kitchen transfers (multi-unit)
- Nutrition/allergen modules; recipe training/sharing; scaling/production planning
- AI layers (recipe creation, anomaly detection, assistants)
- Benchmarking across franchisees/locations
- VAT handling in margin math (Apicbase documents VAT-inclusive sell price with VAT deducted)

### L3 — Vendor-specific (research notes only)

- Apicbase: "Menu Engineering" module name, library-wide settings (VAT, target margin, hour prices), "stockable recipes", outlet prices, My Emissions/ESG footprints, APIC Studio media
- MarketMan: "Cookbook" AI recipe management; Starter/Growth/Enterprise tier gating of costing/COGS/waste features
- Craftable: "Operator AI", "Crafti" assistant, "One Cart" purchasing, hotel positioning
- Toast/xtraCHEF: "cost analytics" naming inside "Supplier & Accounting Suite"; separate Toast "Inventory management" product
- meez: "Recipe Upload Service", 3-day onboarding claim, free tier for individual chefs
- R365: "R365 AI", Chef's Table early access, franchise benchmarking framing

## Rejected Findings

- **"Food cost management = inventory management"** — rejected as a definition. The product population overlaps heavily, but the centers differ: stock/quantities/reorder vs money/cost/variance. meez's existence (recipe/costing layer without full inventory) and Toast's split ("cost analytics" vs "inventory management" as separate products) show the market itself distinguishes the two centers.
- **"Actual vs theoretical requires inventory counts"** — rejected as definitional. The actual side can be assembled from invoices + counts + waste in different proportions; the invariant is that an actual record exists, not any specific capture mechanism.
- **"Prime cost (food + labor) is the defining metric"** — rejected. Labor-inclusive prime cost is a variant framing (optional in Apicbase's own docs); food-only costing is fully in-type.
- **"Menu engineering quadrant analysis is definitional"** — rejected. Per-item profitability is common; the specific quadrant/popularity-classification machinery is vendor-level detail not verified across the sample.
- **Precise numeric claims** (e.g., "5% COGS reduction", "$600/month theft", "3-day onboarding") — vendor marketing/case-study claims, recorded as claims, not promoted to the canonical document.

## Boundary Findings

- **vs Restaurant Inventory Management**: closest neighbor; shares the substrate (items, counts, purchases). Distinction: inventory's center is stock (what you have, what to reorder); food cost's center is money (what each dish should cost, what food actually cost, why they differ). Test: remove costed recipes + variance loop → inventory management remains. Remove stock counting/reordering → food cost management survives (invoice-price feed + theoretical costing; meez pole). **Taxonomy note**: the two directory leaves share one product population; most products market themselves as "inventory management" with food cost as the profit layer. Joint review recommended when restaurant-inventory-management is processed.
- **vs Restaurant Procurement Platform**: procurement's center is the order (POs, suppliers, receiving); food cost consumes purchase data as its price feed. Bundled in many products but separable.
- **vs Restaurant Menu Management**: menu management's center is the guest-facing menu (items, descriptions, pricing presentation, publishing); food cost's center is the costed recipe behind it. Menu pricing decisions may be informed by food cost but menu management is not the costing system.
- **vs Restaurant Management System**: broader suite (POS, labor, payroll, accounting, marketing); food cost management is one pillar (R365, Toast suites show the pillar structure explicitly).
- **vs Accounting Software / Bookkeeping**: accounting is the financial system of record; food cost management is operational cost control that feeds accounting (GL coding) but is not the books. meez's own line: "meez is not accounting software."
- **vs Nutrition Analysis Application**: shares recipe-decomposition mechanics; different output (nutrition/allergen vs cost). MenuCalc's pivot to nutrition-only positioning demonstrates the split.
- **vs Food Formulation Platform / Food Manufacturing ERP**: similar recipe/BOM-costing mechanics, different industry context (manufacturing specs/compliance vs restaurant cost control) and different users.
- **vs Restaurant POS**: POS captures what was sold (sales mix input) and menu prices; it does not cost recipes or track actual food cost.
- **Outer edge of the Type**: a pure recipe-costing calculator with no actual-side record and no variance loop sits below the Type (costing tool, not management). No verified pure-calculator product was reachable in this pass (meez is the closest verified pole but connects to actual-side systems); held with uncertainty.

## Historical / Market-Sample Check

Would older, regional, platform-native products fit the three-leg definition?

- Paper-era practice (conceptual lineage, medium confidence — not directly source-verified in this pass): standard recipe cards with costs updated when prices changed (leg 1); weekly/monthly food-cost calculation from purchases and inventory (opening inventory + purchases − closing inventory, divided by sales = food cost %) (leg 2); potential/theoretical food cost compared against actual in standard food-cost-control doctrine (leg 3). The sample's own educational materials (R365's "Know Your Food Cost Before Count Day", "The Profit Illusion" guide) and case studies (unlogged soda usage at a sports bar) describe the practice and its failure modes in pre-software terms.
- Regional/non-US operations: Apicbase (European vendor) documents VAT-inclusive pricing and outlet-level costing — no US-specific machinery in the core.
- Definition names no era machinery: no invoice OCR, no AI, no cloud, no POS-integration requirement, no specific metric set beyond the loop.

Check passes: the three-leg core is era-agnostic; all era machinery (OCR, AI, cloud, tier packaging) is held outside the core.

## Uncertainties

1. **MarginEdge unverified** — a leading invoice-first product was unreachable; the invoice-first philosophy is evidenced via xtraCHEF/Craftable instead. MarginEdge-specific claims are NOT made in the final document.
2. **Pure recipe-costing calculators** — whether a standalone costing tool with no actual-side connection is marketed as "food cost management" could not be verified (meez, MenuCalc, galley.co, restaurantcosting.com fetch issues). Held as the Type's outer edge with uncertainty; the final document treats costing-only as below the Type.
3. **Exact variance formulas** — how each product computes theoretical usage (sales mix × recipe quantities vs inventory depletion models) is documented only in part (Apicbase Tier-1; others marketing-level). The final document describes the loop conceptually without asserting a single formula.
4. **Waste-percentage vs waste-record semantics** — Apicbase uses a preparation waste *percentage* in costing; MarketMan/Apicbase also support waste *records* in inventory. Both exist; relationship varies by product; held as variant.
5. **Beverage costing depth** — bar-specific programs exist in the market but were not sampled; beverage held as a variant mention only.
6. **Historical paper-era check** — medium confidence, conceptual lineage only (see above).

## Final Synthesis

Restaurant Food Cost Management is the restaurant-side **food-cost control loop**: the costed recipe as the standard (what each dish *should* cost, maintained against changing ingredient prices), the actual food-cost record (what food *did* cost and was consumed, from purchases, depletion, and waste), and the comparison loop that turns the gap between the two into attributed, acted-on variance. Everything else — invoice OCR, inventory counting, POS sales-mix feeds, COGS dashboards, menu-engineering views, AI — is substrate and standard capability serving that loop. The Type's center is money, not stock: it is distinguished from Restaurant Inventory Management (stock-centered), Restaurant Procurement (order-centered), and Menu Management (menu-content-centered) by that center, and from accounting by being operational rather than the financial system of record. The market realizes the Type as inventory-first platforms with a costing layer, invoice-first cost-analytics products, recipe-first culinary layers, and suite pillars — one loop, several postures.
