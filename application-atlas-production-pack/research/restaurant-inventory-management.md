# Research Notes — Restaurant Inventory Management

Research date: 2026-09-09

## Research Goal

Understand what "Restaurant Inventory Management" applications actually are as a Type: their defining core structure, standard capabilities, variants, and boundaries against neighboring Types — Restaurant Food Cost Management (joint review obligation from the sibling pass), Restaurant Procurement, the generic Inventory Management System (family calibration obligation), Retail Inventory Management (sibling instantiation), Restaurant POS, Restaurant Management System, KDS, and WMS.

Two prior-pass obligations must be discharged in this pass:

1. **Family calibration note** (inventory-management-system, 2026-09-07): the generic Type's defining core is written smaller (stock records + recorded events, 2 properties) than the retail instantiation's (which includes count reconciliation as core, 3 properties), because the generic sample included a count-less minimal pole. This pass must decide per-domain whether count discipline is core or standard for the restaurant instantiation and cross-reference the note.
2. **Joint review** (restaurant-food-cost-management, 2026-09-09): the two leaves share ONE product population (most products self-label "inventory management" with food costing as the profit layer); keep-both was provisionally ratified with removal tests running both directions. This pass must discharge the joint review from the inventory side.

## Initial Boundary

Working hypothesis before research:

- Core use: track what food, beverage, and supply stock the restaurant has on hand (ingredients, disposables, cleaning supplies), where it sits (walk-ins, dry storage, bar), how it changes (deliveries in, kitchen consumption out, waste, transfers), and what to reorder.
- Users: kitchen manager / chef (counts, usage), owner/GM (stock value, ordering), bar manager, inventory clerks; not the POS cashier.
- Nearest types: Restaurant Food Cost Management (money-centered sibling), Restaurant Procurement (order-centered), generic Inventory Management System (family parent), Retail Inventory Management (retail sibling), Restaurant POS (sales side), Restaurant Management System (suite).
- Key unknowns: (1) Is count reconciliation definitional for the restaurant instantiation (family calibration question)? (2) Is recipe/sales-depletion linkage (stock depleted from POS sales × recipes) definitional or common? (3) What is restaurant-specific in the core vs generic stock machinery? (4) How does reorder machinery work (par levels)? (5) Discharge the food-cost joint review.

## Research Questions

1. What is the central object — ingredient/item, stock package, storage location, count, or purchase?
2. How does stock change: what event types exist (receiving, consumption/depletion, waste, transfers, adjustments)?
3. How do counts work (full/partial, mobile, parallel, snapshot vs delta semantics), and are they definitional for this domain?
4. How does the system know what was consumed — counts only, or recipe/sales-depletion computation?
5. How does reorder work — par levels, min quantities, order guides, suggested/generated purchase orders?
6. What unit machinery exists (purchase packages, cases, base packages, weight counting, purchase-vs-recipe units)?
7. What is restaurant-specific in the objects (perishables, storage areas, waste reasons, commissary) vs generic machinery?
8. What rules matter (count-event exclusivity, event-before-count discipline, overwrite semantics, permissions)?
9. Where are the boundaries vs food cost management (joint review), procurement, the generic family, retail inventory, POS, and the suite?

## Representative Products

Selected for market representativeness + documentation quality + different product philosophies + different customer levels:

| Product | Philosophy / position | Customer level | Evidence quality |
|---|---|---|---|
| MarketMan | self-labels "Restaurant Inventory Management Software"; inventory-first cloud platform | SMB independents → small chains → multi-unit | Tier 2 (product + FAQ pages; help center unreachable) |
| Apicbase | recipe-driven enterprise F&B management with a full Inventory module | enterprise / multi-unit / international (European vendor) | Tier 1 (help center articles) |
| Restaurant365 | restaurant management suite; inventory as a pillar beside accounting/payroll/workforce | SMB → franchise/multi-location | Tier 2 (product pages; help center is ticket-portal) |
| Toast Inventory (xtraCHEF by Toast) | inventory product inside a POS platform ecosystem, invoice-first heritage | SMB → mid-market, Toast ecosystem | Tier 2 (product page) |
| Craftable | hospitality back-office platform (restaurants + hotels) | mid-market / multi-unit | cross-pass context (food-cost pass 2026-09-09, Tier 2; fresh fetch of guessed inventory URL 404) |

MarginEdge (invoice-first leader) was unreachable in the food-cost pass and was not retried here (same domain, same transport failures expected). meez (recipe-first pole) was sampled by the food-cost pass and is used only as boundary context, not as a primary sample of this Type.

## Sources

Fetched 2026-09-09:

- Apicbase Help Center (Tier 1) — https://support.apicbase.com/help/inventory (module index); https://support.apicbase.com/help/counting-your-inventory ; https://support.apicbase.com/help/register_waste ; https://support.apicbase.com/help/transfer-stock ; https://support.apicbase.com/help/inventory-3.0-the-new-way-of-counting
- MarketMan — https://www.marketman.com/platform/ (platform index); https://www.marketman.com/platform/restaurant-inventory-management-software (self-labeled inventory page + FAQ)
- Restaurant365 — https://www.restaurant365.com/inventory/ (pillar hub); https://www.restaurant365.com/inventory/inventory-management/ ; support portal index https://help.restaurant365.net/support/home (ticket portal; KB articles not fetched)
- Toast — https://www.toasttab.com/inventory-management ("Restaurant Inventory Management Software" product page; xtraCHEF-based)
- Craftable — https://www.craftable.com/ (recorded in the food-cost pass 2026-09-09; used as cross-pass context)

Unreachable / abandoned (per network rules): help.marketman.com (transport error ×1), marketman.com/support/ (404), marketman.com/faq/ (404), marketman.com/platform/inventory-management (404 — correct URL found via platform index), craftable.com/inventory-management/ (404, guessed URL; not retried further). R365 knowledge-base articles sit behind a Freshdesk search portal and were not individually fetched.

## Product Observations

### Apicbase (evidence layer A — Tier 1 help center)

- **Module map**: Inventory module = Counting + Stock Management (waste registration, transfers, past events, stock-item deletion). Neighbors: Menu Engineering (ingredients/recipes/menus), Procurement (ordering/receiving/suppliers), Sales (POS integrations), Planning (production plans, HACCP), Insights Hub (CoGS/inventory dashboards).
- **Counting** (Counting your inventory):
  - Count events with **sub-counts**: several people count simultaneously in parallel sub-counts; a Count Total column aggregates everyone's quantities per item.
  - **Counting happens in packages** (stock items = packages with units): "When you count stock, you count packages… 2 for the bourbon = two bottles of 750ml."
  - **Partial-package counting**: a "Part" button counts by unit instead of package (1,250 g of mushrooms → recalculated to 2.5 packages of 500 g).
  - **Snapshot-overwrite semantics**: "the final quantity you have counted when you save a main count **overwrites** the previous stock, it does not add to the existing stock."
  - **Not mandatory to count everything**: uncounted items keep their current stock; "if you wish to deplete an item's stock, you must explicitly count it to zero."
  - **Count-event exclusivity**: "strongly recommended that you do not start any other inventory events (waste, create, transfer, sales) while a count event is open."
  - **POS interaction**: "Never do a stock count when your POS is active and generating sales tickets, your stock will **not** be updated at night!" — i.e., sales tickets deplete stock in a nightly update; counting mid-service conflicts with it.
  - **Count overview with variance**: Theoretical Stock, Counted Stock, Stock Variance, Theoretical Stock Value, Counted Stock Value, Stock Value Variances. Variance filtering before save "to spot any mistakes."
  - Count history, count reports, exports; Excel-file counting; aggregated-package counting (crate of beer 24×33 cl); storage-location filter; notification if a stock count has not been saved.
- **Waste** (register_waste): waste events for **stock items AND recipes**; quantity (+part), event description (shows in waste report), remarks; waste overview shows "the stock change in value" per event; tip: "Registering waste consistently is very important to have a precise stock… Determine a regular moment… a certain employee is responsible."
- **Transfers** (transfer-stock): transfer events between outlets; "items will now be depleted in the stock of the first outlet… and added to the stock of the outlet you selected afterward"; transferable types include **stockable recipes** (prep items held in stock); tip: "all transfer events that have actually happened before a stock count must be registered before this count. Otherwise, your stock will not be correct."
- **Inventory 3.0** (multiple related packages): inventory tracked at the **base package** (wine tracked at bottle level); larger packages (pallet/box) are "unpacked" to base units (1 pallet + 2 boxes + 5 bottles → 41 bottles); counting any branch overwrites the total across related packages; unrelated packages of the same ingredient (5 kg vs 10 kg flour) stay separate; **Min. Qty, PAR, and Storage Location are set directly on the inventory list page**.

### MarketMan (evidence layer A for the fetched pages; Tier 2 product/FAQ)

- Self-labels: nav solution "Inventory Management" → page titled "Restaurant Inventory Management Software"; platform pitch: "Eliminate spreadsheets and automate inventory management, purchasing, invoicing."
- Positioning: "MarketMan keeps track of everything that comes in the back door and is served to your guests."
- FAQ — tracking model: "MarketMan tracks inventory in real time using a combination of purchase orders, sales data from your POS, and manual stock counts completed through the mobile app. Every item received, used, or wasted is logged automatically to give you an accurate live stock picture."
- FAQ — mobile counts: "storage rooms, walk-in fridges, or the bar. Counts sync instantly to the cloud so managers see results in real time."
- FAQ — count schedules: "daily, weekly, or custom count schedules… The system supports partial counts so you don't have to count everything at once."
- FAQ — variance: "variance reports that compare theoretical usage (based on sales) against actual usage (based on counts). Unusually high variance on a specific item flags potential theft, spoilage, or portioning issues."
- FAQ — ordering: "automatically generate purchase orders based on par levels you set. When stock drops below a threshold, the system flags items for reorder. You can review and send orders directly to suppliers."
- "Real-time Ordering Intelligence": "Manage purchasing budgets, par levels, deliveries, cut-off times, & purchasing limits from one app."
- Invoices: "snap a photo or upload a copy of your delivery invoices… automatically update items and quantities received without any manual entry."
- Multi-unit (Enterprise): "centralized reporting, inter-location inventory transfers, commissary kitchen management, standardized recipe libraries, and comparative performance dashboards."
- Cross-pass context (food-cost pass): tier gating of costing/COGS/waste features; actual-vs-theoretical named report; POS/accounting/distributor integrations.

### Restaurant365 (evidence layer A for the fetched pages; Tier 2 product)

- Suite structure: "Inventory & Purchasing" pillar with sub-products — Inventory Management, Recipes, Prep, Purchasing and Receiving, Cash Management, Commissary, AI Dashboards — beside Accounting, Workforce, Payroll & HR pillars.
- Inventory Management page: "Automate recipe costing, speed up inventory counts, and track transfers to close the actual vs. theoretical gap"; "Save hours with faster, easier inventory counts via mobile app"; "Control inventory with accurate transfer tracking"; "Protect margins by spotting and reducing waste."
- "Complex Inventory Processes Made Simple": "Verify deliveries and seek credit memos for shorted or incorrect items"; "Simplify payments with automated invoice capture & coding"; "Count smarter to drive more accurate purchasing decisions"; "Connect your counts to real-time food cost and P&L reporting."
- Counts: "multiple team members count in real time via mobile app."
- Purchasing: "Generate AI-driven purchase orders based on actual demand"; "Order smarter with shopping lists"; "Sync received items directly to inventory."
- Commissary: "standardizing catalogs, recipes, and portioning… simplified transfers and production… sell items to third parties."
- Hub page: "Track ingredients in real time"; "See real-time COGS and variance by location or concept"; "Cut food waste with real-time inventory counts."

### Toast Inventory (xtraCHEF by Toast) (evidence layer A for the fetched page; Tier 2 product)

- Page title: "Restaurant Inventory Management Software"; "xtraCHEF by Toast offers modern inventory management tools."
- Scope: "a restaurant inventory tool that combines invoice automation, recipe costing, vendor management, ordering, product catalogs, and Toast POS sales data."
- Financial layer: "Monitor real-time inventory values with automated ingredient price changes"; "Transform beginning and ending inventory details into insights for COGS reports"; "Integrate with Toast POS data to fuel reporting, such as actual vs theoretical (AvT), depleting inventory, and more."
- Counting: "Get counts done quicker on your phone or mobile device by mapping count lists to your unique kitchen setup — with or without connection to wifi"; "Assign inventory counts to staff members so it never gets skipped or forgotten"; "Track patterns of missing value to identify waste, shrinkage, and theft."
- Ordering: "Take inventory once, and we'll create an order guide for you based on what's on hand and what's required to maintain par"; "Schedule recurring orders to ensure you're maintaining par levels"; "Send orders directly to your suppliers."
- Positioning: inventory that "goes beyond counting cans" — value-based inventory insights.
- Cross-pass context: Toast ships "xtraCHEF cost analytics" and "Inventory management" as separately purchasable products in the Supplier & Accounting Suite.

### Craftable (cross-pass context from the food-cost pass; Tier 2)

- "Hospitality's most intelligent back-office platform" for restaurants AND hotels. Modules: Intelligent Ordering, AP Automation, Inventory & Recipe Management, Daily Actionable Insights.
- Inventory & Recipe: "Know exactly what you have, what it costs, and where your variance is — in real time. Craftable connects physical counts to recipes and theoretical usage so you can spot margin loss before it hits the P&L."
- Case-study framing: bartaco "50% reduction in food cost variance"; Sugarfire "spot actual vs. theoretical variance."

## Cross-product Comparison

| Structure / capability | MarketMan | Apicbase | R365 | Toast/xtraCHEF | Craftable (cross-pass) |
|---|---|---|---|---|---|
| Item-level stock records (ingredients/supplies, quantities) | ✓ ("accurate live stock picture") | ✓ (ingredients + stockable recipes, packages) | ✓ ("track ingredients in real time") | ✓ (product catalogs, inventory values) | ✓ ("know exactly what you have") |
| Storage locations / areas as structure | ✓ (storage rooms, walk-ins, bar as count venues) | ✓ (Storage Location per outlet; storage-location filter) | ✓ (locations/concepts) | ✓ (count lists mapped to kitchen setup) | ✓ |
| Recorded stock events | ✓ (received/used/wasted "logged automatically") | ✓ (count/waste/transfer/create events; sales tickets deplete nightly) | ✓ (receiving syncs to inventory; transfers tracked) | ✓ (depleting inventory from POS; invoice receipt) | ✓ (counts connected to usage) |
| Physical count reconciliation | ✓ (mobile counts, partial counts, schedules) | ✓ (count events, sub-counts, variance review, overwrite semantics) | ✓ (mobile counts, multiple counters, real time) | ✓ (mobile/offline counts, assigned to staff) | ✓ (physical counts) |
| Count variance visibility (theoretical vs counted) | ✓ (variance reports) | ✓ (Theoretical/Counted/Variance in qty + value) | ✓ (actual vs theoretical gap) | ✓ (missing-value patterns → waste/shrinkage/theft) | ✓ (variance in real time) |
| Recipe/sales-depletion linkage | ✓ (POS sales data in tracking; theoretical usage from sales) | ✓ (sales tickets deplete stock at night; PLU→recipe linking) | ✓ (recipes + purchasing + inventory connected) | ✓ (AvT, depleting inventory from Toast POS) | ✓ (counts ↔ recipes ↔ theoretical usage) |
| Waste tracking as first-class event | ✓ (wasted items logged; waste sources) | ✓ (waste events for items and recipes, with value) | ✓ (spotting and reducing waste) | ✓ (waste, shrinkage, theft patterns) | ✓ (variance attribution) |
| Transfers (between outlets/locations) | ✓ (inter-location transfers) | ✓ (outlet-to-outlet transfer events) | ✓ (accurate transfer tracking; commissary) | — (not on fetched page) | — |
| Receiving / delivery verification | ✓ (invoice photo → quantities received) | ✓ (Procurement module: receiving) | ✓ (verify deliveries; credit memos; sync received to inventory) | ✓ (invoice automation feeds stock) | ✓ (AP automation, 3-way match) |
| Par levels / reorder machinery | ✓ (par levels → auto POs; budgets, cut-off times) | ✓ (Min. Qty, PAR on inventory list) | ✓ (shopping lists, AI-driven POs) | ✓ (order guide from par; recurring orders) | ✓ (Intelligent Ordering) |
| Package/unit machinery | (not detailed on fetched pages) | ✓ (packages, base-package unpacking, part/weight counting, aggregated packages) | (not detailed) | (not detailed) | (not detailed) |
| Multi-outlet / commissary | ✓ (Enterprise: commissary management) | ✓ (outlets; transfers) | ✓ (commissary pillar; third-party sales) | ✓ (across locations) | ✓ (hotels + restaurants) |
| Stock valuation / COGS contribution | ✓ (real-time inventory value) | ✓ (stock value variances; Inventory Evolution dashboards) | ✓ (counts → food cost and P&L) | ✓ (beginning/ending inventory → COGS) | ✓ (variance before it hits the P&L) |
| POS integration | ✓ (Toast, Square, Lightspeed…) | ✓ (ePOS, PLU→recipe) | ✓ (POS, invoices, recipes connected) | ✓ (native Toast) | ✓ (POS integrations) |
| Accounting integration | ✓ (QuickBooks, Xero) | (via Insights Hub/reports) | ✓ (native accounting pillar) | ✓ (accounting suite) | ✓ (GL coding) |
| AI layers | ✓ (AI ordering, Cookbook) | ✓ (AI module) | ✓ (R365 AI, AI POs, AI dashboards) | (Toast IQ adjacent) | ✓ (Operator AI/Crafti) |
| Suite packaging | standalone platform (+purchasing/AP modules) | suite with separate Procurement module | suite pillar | POS-ecosystem product | back-office suite |

Reading of the table (evidence layer B — cross-product commonality):

- **Item-level stock records + recorded events + count reconciliation** are present in 5/5. Counts are a first-class workflow in every product (mobile counting, count schedules, count assignment, variance review) — the restaurant instantiation is count-anchored.
- **Recipe/sales-depletion linkage** is present in 5/5 as the theoretical-usage substrate — but it always rides on recipes and POS data, and bars/count-only practices exist without it; held as common mature structure, not definitional.
- **Waste as a first-class event type** (not just an adjustment reason) is restaurant-typical: 5/5.
- **Par-level reorder machinery** is 5/5 (order guides, suggested/auto POs, min quantities).
- **Receiving** is 5/5 (delivery verification, quantities received into stock, credit memos for shortages).
- **Transfers** are documented in 3/5 fetched pages (4th/5th not verified on fetched surfaces) — common mature structure.
- **Package/unit machinery** is documented in Tier-1 depth only at Apicbase; universally implied (food is bought in cases and counted in bottles/weights) but held at L1 with the Tier-1 pole as the documented example.
- **Multi-outlet/commissary, valuation, POS/accounting integration, AI** — common to variant layers depending on segment.

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

The Type is the restaurant's **stock system of record for food, beverage, and operating supplies**. Three jointly-held structures:

1. **Item-level stock records at storage locations** — for each stocked item (ingredient, beverage, supply), the system holds quantity on hand in its stock-keeping unit (package, bottle, weight) at named storage places (walk-in, dry storage, bar) and outlets. The record is the system of record for "what do we have, where, in what unit." Remove → a pantry list / spreadsheet, not a managed system.
2. **Recorded stock events as the way the record changes** — deliveries received in; consumption out (recorded directly as waste/production/transfer events, or computed as depletion from sales through recipes); transfers between storage areas and outlets; reason-coded corrections. On-hand is never silently edited; every change is a dated, attributable event. Remove → a static quantity list.
3. **Physical count reconciliation** — periodic counts (full or partial, commonly mobile, often by multiple people) that reconcile the record to physical reality, with the variance between theoretical and counted stock surfaced in quantity and value. Remove → an unanchored depletion ledger that drifts without bound; the restaurant's only direct observation of stock is the count.

Jointly-held load-bearing checks:

- 1 alone = pantry list / stock spreadsheet.
- 2 without 1 = event log with no stock picture.
- 3 without 1+2 = a count sheet with no system (the digitized clipboard).
- 1+2 without 3 = depletion ledger with no physical anchor — conceivable but unsampled; every sampled product anchors the record with counts, and the domain's structural reason (consumption is invisible at item level) makes the count the truth-anchor.
- 1+3 without 2 = count snapshots without event memory — variance between counts would be unattributable.

**Domain calibration decision (cross-reference to the inventory-management-system family note, 2026-09-07):** count reconciliation is written into the restaurant instantiation's core (3 properties), matching the retail instantiation, NOT the smaller generic core (2 properties). Reasons: (a) 5/5 sampled products make counting a first-class workflow (count events, schedules, assignment, variance review); (b) the domain-structural reason is stronger than in generic stock-keeping — restaurant consumption is largely invisible at the item level (no per-unit scan at sale; the POS sells a "burger", not 0.1 lb of beef), so the periodic count is the only direct observation of stock; (c) the historical paper-era practice IS the count (clipboard count sheets + par lists). The generic family keeps its smaller core because of its count-less minimal pole (Sortly); no count-less pole was found in the restaurant sample. This is sample-driven calibration, consistent with the family note's expectation that "domain instantiations may carry stricter cores."

Deliberately NOT in L0 (checked against the sample): recipe/sales-depletion computation (a bar counting kegs and bottles without recipes is still this Type), par levels/reorder machinery (a count-and-record system is still recognizable), waste tracking as a separate event type (foldable into adjustments), transfers, package-conversion machinery, mobile apps, cloud, AI, invoice OCR, POS integration as a mechanism (historically counts and deliveries were written by hand).

### L1 — Common Mature Structure

Present across the researched sample; not required to recognize the Type:

- **Recipe/sales-depletion linkage** — POS sales × recipes deplete ingredient stock (or compute theoretical usage); the bridge between "what was sold" and "what left the storeroom" (5/5)
- **Par levels / min quantities → reorder machinery** — order guides from what's on hand vs par, suggested or auto-generated purchase orders, purchasing budgets and cut-off times (5/5)
- **Receiving** — delivery verification against orders, quantities received posted into stock, credit memos for shorted/incorrect items (5/5)
- **Waste tracking as a first-class event type** — dated, attributed, reason-coded waste with its stock-value impact; waste reports (5/5)
- **Transfers** — between storage areas and between outlets, with event records registered before counts (3/5 fetched; Apicbase/MarketMan/R365 documented)
- **Package and unit machinery** — stock kept in purchase packages (cases, bottles, sacks), counting by package or by partial unit/weight, conversion between purchase, stock, and recipe units; base-package normalization (Apicbase Tier-1 documented; universally implied)
- **Mobile counting** — phone/tablet count sheets organized by storage area, offline-capable, counts assigned to staff, parallel counting (4/5 documented on fetched surfaces)
- **Variance reporting** — theoretical vs counted/actual stock in quantity and value; variance as the theft/spoilage/portioning signal (5/5)
- **Stock valuation** — inventory value in dollars; beginning/ending inventory feeding COGS (5/5)
- **Multi-outlet structure** — outlets/locations with standardized item libraries; inter-location transfers; commissary at the multi-unit pole (4/5)
- **Integration spine** — POS (sales/depletion input), accounting (stock value → books), supplier/distributor connections (5/5)

### L2 — Variant / Optional Structure

Depends on segment, scale, deployment:

- **Commissary / central production kitchen** — production plans, transfers to outlets, selling to third parties (R365 pillar; MarketMan Enterprise; Apicbase stockable recipes + production plans)
- **Beverage/bar-specific programs** — bottle/keg-level tracking, bar count practices (guides exist in-sample; depth not sampled)
- **AI layers** — AI-driven purchase orders, demand forecasting, AI dashboards/assistants (era-current trend; 4/5 name some AI)
- **Franchise/multi-group benchmarking** — comparative performance across locations
- **HACCP / traceability adjacency** — production planning, task and HACCP modules beside inventory (Apicbase)
- **Barcode scanning apps**; Excel-import counting; aggregated-package handling
- **Suite vs standalone packaging**; plan-tier gating of features (waste tracking, costing behind tiers)
- **Hotel/institutional anchoring** (Craftable's hospitality positioning)

### L3 — Vendor-specific (research notes only)

- Apicbase: base-package "unpacking" of related packages; sub-count naming; count-overwrite warnings; "stockable recipes"; outlet model; Library settings; storage-location filter; Excel counting; stock-count-unsaved notifications; nightly sales-ticket depletion
- MarketMan: Starter/Growth/Enterprise tier gating; "Cookbook" AI recipe management; buyer portal; purchasing budgets/cut-off times/purch limits; 55-countries claim
- R365: commissary third-party sales; "R365 AI"; AI Dashboards ("ask a question, get a dashboard"); cash-management pillar; franchise benchmarking framing
- Toast: xtraCHEF branding inside "Supplier & Accounting Suite"; offline count app; order guide generated from a single count; "beyond counting cans" positioning
- Craftable: hotel positioning; "Crafti"/"Operator AI"; "One Cart" purchasing

## Rejected Findings

- **"Restaurant inventory management = food cost management"** — rejected as a merge. One product population, two centers: stock (quantities, counts, par, reorder) vs money (plate cost, spend, cost variance). The removal tests run both directions (documented in the food-cost pass and re-confirmed here): remove costed recipes + the money-variance loop → inventory management remains; remove counting/reordering → food cost management survives on invoice prices + theoretical costing. The market itself splits the centers (Toast sells "cost analytics" and "inventory management" as separate products; meez positions as a costing layer on top of inventory systems). Keep-both ratified — joint review discharged (see Boundary Findings).
- **"Depletion from recipes is definitional"** — rejected. A bar or counter-service operation can run this Type on counts + deliveries + waste without any recipe linkage; the depletion link requires recipes and POS data and is the food-cost loop's substrate. Common mature structure, not invariant.
- **"Reorder automation is definitional"** — rejected. A count-and-record system with human ordering decisions is still this Type (and was the historical norm); par-driven order generation is the common mature expression.
- **"Mobile offline counting is definitional"** — rejected: era-typical implementation of the count, not the count itself.
- **"Waste tracking is a separate Type"** — rejected: waste is a stock event type inside this Type (with a value dimension that feeds the food-cost sibling).
- Precise numeric claims (e.g., "4% food-cost reduction", "15,000+ customers", "$400M food waste cut") — vendor marketing claims, recorded as claims, not promoted.

## Boundary Findings

- **vs Restaurant Food Cost Management (§26 sibling) — JOINT REVIEW DISCHARGED**: the two leaves share one product population; most products self-label "inventory management" with food costing as the profit layer. The centers differ: inventory's center is the **stock record and its physical truth** (what's on hand, counts, par, reorder); food cost's center is **money** (what each dish should cost, what food actually cost, why they differ). Removal tests hold in both directions (re-confirmed from this side): strip the costed recipes and the money-variance loop from a sampled product → a stock system remains; strip counting/receiving/reorder → a costing system on invoice prices remains. The shared seam is the **variance**: inventory computes usage variance in *quantities* (theoretical vs counted stock), food cost computes cost variance in *money* (theoretical vs actual food cost) — same underlying data, different center. Keep-both ratified from both sides. The final documents cross-reference each other.
- **vs generic Inventory Management System (§10)**: domain instantiation of the family parent. Same machinery (stock records, events, counts, replenishment); restaurant color in the objects' content: ingredients/perishables, storage areas (walk-ins, dry storage, bar), purchase packages/cases/weights, par levels, waste as a first-class event, recipe-depletion linkage, commissary transfers. The generic Type's core is smaller (no count reconciliation — its Sortly-class minimal pole corrects by editing quantities); the restaurant instantiation carries the stricter 3-property core. Family calibration note cross-referenced.
- **vs Retail Inventory Management (§05.12)**: sibling instantiation. Both carry count reconciliation in their cores. Structural difference in how stock leaves: retail sells *identifiable units* scanned at the POS (sales auto-decrement the record); restaurants sell *prepared dishes* whose ingredient consumption is invisible at item level (depletion must be computed from recipes, and the count anchors the record). Retail color: merchandise, stores, shrinkage reasons, price labels; restaurant color: ingredients, storage areas, perishables, par levels, waste events, commissary.
- **vs Restaurant Procurement Platform**: procurement's center is the order (POs, suppliers, ordering workflows, receiving as order fulfillment); inventory's center is the stock record (receiving as stock-in, par levels generating *suggestions*). Bundled in most sampled products (MarketMan purchasing module, R365 Purchasing & Receiving, Toast ordering) but structurally separable (Apicbase ships Procurement as a separate module; a count-first operation can order by phone). Remove the order lifecycle → inventory management remains.
- **vs Restaurant POS**: the POS captures what was sold (the depletion input) and menu prices; it does not own the stock record, counts, par, or receiving. The POS is this Type's most consequential integration, not the same Type.
- **vs Restaurant Management System**: suite packaging. R365 and Toast show the pillar structure explicitly — inventory is one pillar beside accounting/payroll/workforce/POS. Remove the suite neighbors → this Type remains.
- **vs KDS / Restaurant Menu Management / recipe management**: KDS is kitchen production display; menu management is the guest-facing menu; recipe management (meez pole) is the recipe-content layer. Depletion rides on recipes but recipe authoring is not stock-keeping.
- **vs WMS**: warehouse physical-handling depth (bins, picking, putaway) has no restaurant counterpart at store level; the blur zone is the commissary/central kitchen (R365 commissary with production and transfers). Restaurant inventory stays at storage-area grain, not bin grain.

## Historical / Market-Sample Check

Would older, regional, platform-native products still fit the three-leg definition?

- **Paper-era restaurant practice** (conceptual lineage, medium-high confidence): clipboard count sheets by storage area (leg 3 + leg 1's quantities), par lists and order sheets sent to vendors (leg 1's records + reorder), delivery check-ins and waste noted on the sheet (leg 2's events). The sampled products' own guidance describes exactly this practice in pre-software terms (Apicbase's "register waste consistently… a regular moment… a certain employee is responsible"; Toast's "ditch the sheets and clipboards"; MarketMan's "eliminate spreadsheets"). ✓
- **Bar inventory practice**: periodic bottle counts (and weighing practices) against par — count-anchored, no recipes required. ✓ (conceptual, medium confidence)
- **Regional**: Apicbase is a European vendor (outlets, multi-language); no US-specific machinery appears in the inventory core. ✓
- **Era machinery kept outside the core**: mobile apps, offline counting, cloud sync, invoice OCR, AI ordering/forecasting, tier packaging — none required by the definition. ✓

Check passes: the three-leg core is era-agnostic.

## Uncertainties

1. **MarketMan help center unverified** — help.marketman.com unreachable (transport error); /support, /faq, /platform/inventory-management 404 (correct URL found via platform index). MarketMan evidence is Tier-2 product/FAQ pages plus cross-pass context; FAQ statements (e.g., "every item received, used, or wasted is logged automatically") are vendor FAQ claims, not help-doc verification.
2. **Craftable fresh fetch failed** — guessed inventory URL 404; Craftable evidence is cross-pass context from the food-cost pass (recorded, Tier-2 product pages). Not retried further per network rules.
3. **R365 knowledge base not article-fetched** — the support portal is a ticket/search portal; R365 evidence is Tier-2 product pages. Count mechanics (snapshot vs delta semantics) verified only at Apicbase (Tier 1).
4. **Depletion-without-counts posture** — conceivable (a pure depletion ledger) but unsampled; not asserted in the final document. The L0's third leg rests on 5/5 sampled products plus the domain-structural argument, not on an exhaustive market census.
5. **Package/unit machinery depth** — documented at Tier-1 depth only at Apicbase; other products' unit handling is implied by domain practice but not help-doc verified.
6. **Beverage/bar programs** — guides exist in-sample (R365 bar inventory guide) but no bar-specific product was sampled; held as variant mention.
7. **MarginEdge** — unreachable (also in the food-cost pass); no MarginEdge claims made.

## Final Synthesis

Restaurant Inventory Management is the restaurant's stock system of record: item-level stock records for food, beverage, and supplies at storage locations, changed only through recorded stock events (deliveries in, consumption out — recorded or recipe-depleted — waste, transfers, corrections), and reconciled to physical reality by periodic counts whose variance is surfaced in quantity and value. Around that core, mature products add the machinery that makes the record actionable: recipe/sales-depletion linkage, par-level reorder machinery, receiving with shortage credit memos, waste tracking as a first-class event, transfers, package/unit conversions, mobile counting, valuation, multi-outlet structure, and POS/accounting integrations. The Type's center is stock, not money — the money layer (plate costs, cost variance, COGS analysis) is the food-cost sibling's center, and the market sells both centers separately and together. The restaurant instantiation carries the family's stricter core (count reconciliation included) because restaurant consumption is invisible at the item level: the count is the only direct observation of stock. Products realize the Type as standalone inventory platforms, suite pillars, POS-ecosystem products, and hospitality back-offices — one stock system, several postures.
