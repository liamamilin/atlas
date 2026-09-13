# Research Notes — Retail Inventory Management

## Research Goal

Understand what a Retail Inventory Management application actually is, from real products: what objects exist inside it, who uses it, how stock work flows, which states and rules matter, and where its boundaries lie against Retail POS, generic Inventory Management Systems, WMS, Merchandising, and PIM.

Directory context: leaf `Retail Inventory Management` under 05.12 Retail Inventory, sibling leaf `Store Inventory Application` (same family). Prior processed sibling: `retail-point-of-sale` (05.10), whose Related-Types table positions Retail Inventory Management as "back-office neighbor — plans, counts, receives, replenishes stock; the POS only decrements and displays it as a side effect of selling."

## Initial Boundary

Working hypothesis before research:

- Core purpose: keep the store's stock record true and usable — what is on hand where, what came in, what went out, what should be reordered.
- Users: store managers, stockroom/inventory clerks, retail buyers/merchandisers at HQ, loss-prevention roles.
- Nearest neighbors: Retail POS (transaction side), Inventory Management System (§10 generic), WMS (warehouse operations), Merchandising/Assortment Planning (what to buy), PIM (product data), Order Management (customer orders).
- Likely confusion: with generic Inventory Management System (shared machinery, different domain) and with POS inventory screens (shared stock numbers, different job).

## Research Questions

1. What is the central object — item? SKU? stock record? location?
2. How does stock change: what movement types exist (in, out, between, adjust)?
3. How does selling (POS / e-commerce) connect to the stock record?
4. How does receiving work — purchase orders, vendors, unit costs?
5. How do physical counts work — full vs cycle, approval, variance handling?
6. How does replenishment work — reorder points, alerts, suggestions, PO generation?
7. What cost/value machinery exists (unit cost, COGS, inventory value, costing methods)?
8. What rules matter — stock sufficiency, negative stock, permissions, audit?
9. What is retail-specific vs generic inventory machinery?
10. Where exactly is the line to WMS, Merchandising, PIM, and the §10 generic Inventory Management System?

## Representative Products

| Product | Pole | Customer tier | Why selected |
|---|---|---|---|
| Square for Retail | POS-integrated retail mode; inventory as back-office module of a payments-first POS | micro-SMB / SMB | dominant SMB retail pattern; strong help center |
| Erply | back-office-first retail suite; document-driven inventory; chain support | mid-market / enterprise, multi-store chains | European/chain heritage; explicit Inventory module vocabulary |
| NetSuite (Inventory Management) | enterprise ERP inventory; retail is one use of generic machinery | enterprise | shows the generic-ERP pole and the boundary to §10 |
| Cin7 Core | multichannel product-business IMS ("ERP-lite"); retail + wholesale + e-commerce | SMB / mid-market | shows the multichannel stock-hub pole and the WMS/forecasting adjacency |

Rejected/abandoned candidates: Lightspeed Retail (help center unreachable — transport errors ×2, abandoned per network rule), Shopify (help center 403, known from prior pass), Retail Pro (product URL 404; not retried).

## Sources

All fetched 2026-09-07.

- Square Help Center — "Items and inventory" topic page; "Track your inventory" (7746); "View, receive, and adjust inventory" (6110); "Conduct, review, and approve inventory counts" (8249); "Create and manage purchase orders" (8258) — https://squareup.com/help/us/en/
- Erply Wiki — "Upgrading from old to new inventory system" (579); "Erply Back Office Terminology" (662) — https://wiki.erply.com/
- NetSuite Applications Suite Help — SCM > Inventory Management book; "Basic Inventory Management" chapter — https://docs.oracle.com/en/cloud/saas/netsuite/
- Cin7 — "Multichannel inventory management software" product page (marketing, Tier-2); Cin7 Core Help Center — "Stock and replenishment" section; "Stocktake" article — https://www.cin7.com/ , https://help.core.cin7.com/

Source-access limitations: Lightspeed help center transport-failed twice (abandoned). Shopify help center 403. NetSuite marketing site 403 (Oracle docs used instead — these are Tier-1 operational docs, so no strength reduction for NetSuite). Cin7's multichannel claims rest partly on marketing pages; operational claims for Cin7 use its Core help center.

## Product A — Square for Retail (Square Help Center)

Evidence layer: A (direct observation, official help articles).

Key observations:

- **Inventory tracking is a per-item-variation, per-location toggle.** "Enable inventory tracking for new items" / enable for existing items; items that never had stock get count 0 when tracking is enabled. Tracking can be disabled (bulk disable via export/re-import with "N" quantity).
- **Sales decrement stock automatically**: "Square's inventory management software connects with your point of sale, so your stock levels are automatically adjusted every time you make a sale."
- **Stock alerts**: daily stock alert emails for low/out-of-stock items, framed as input to "prepare a purchase order for more stock in time."
- **Stock overview surface**: on-hand by item, filterable by multiple locations, category, inventory status, vendor; inline actions: adjust stock, receive stock, add to purchase order, add to transfer order, edit low-stock alert; actions: print labels, export library.
- **Stock actions with reasons**: "Stock received, Inventory recount, Damage, Theft, Loss, or Restock return"; custom adjustment reasons can be created. Reasons are attributed on the adjustment record.
- **Receiving**: bulk receive via barcode scanner (scan increments quantity), confirmation screen shows Unit Cost / Price / Profit Margin per item, cost-change indicator vs last receipt; work must be committed before exiting.
- **Inventory counts**: two modes — **full count** ("full accounting of your entire stock… any uncounted stock is set to zero" after approval) and **cycle count** (subset at intervals; uncounted items unaffected; recommendation to cycle-count each variation at least once every 90 days). Count lifecycle: In progress → Start review → Review results (sort by Variance (Count) / Variance (Cost) / alphabetical; override count; retract from review to add missed items) → Confirm (irreversible) → Completed. Multiple devices can contribute to one full count. Measurement units with automatic conversion to the item's stock-by unit.
- **Transfers**: "Transfer stock between locations" and "Create and manage transfer orders" (order-shaped transfer with receiving side).
- **Purchase orders**: vendor, delivery location, expected date, item lines with quantity / vendor code / unit cost; draft → send to vendor by email (preview, copy to self, PDF/CSV); receive All / None / partial per line; damaged/theft/loss on receipt excluded from COGS; "Add Fee" (shipping/handling) included in COGS but not in item unit cost; cancel → archived. POs can create items on the fly; creating a PO associates item variation with vendor and cost.
- **Cost/value**: unit costs, missing-unit-cost tracking, COGS report, inventory variance report (exportable), aging inventory report.
- **Permissions**: "item and inventory permissions" gate stock updates; inventory permissions article exists ("Set inventory permissions with Square for Retail").
- **Identification**: SKUs (auto-generate), GTINs, barcode label printing, barcode scanning for count/receive.
- **Stock conversion**: sell-by units with conversion (e.g., case ↔ unit) during counts.
- Plan gating: advanced inventory (counts, POs, transfers) tied to Square for Retail Plus/Premium tiers — plan-tiered capability (vendor-specific commercial fact, kept here).

## Product B — Erply (Erply Wiki)

Evidence layer: A (direct observation, official wiki).

Key observations:

- **Inventory is a named back-office module**, separate from PIM (product data) and Purchase (purchasing documents). Terminology article: "The Inventory module is where you can find stock levels for products across your retail chain. Set up semi-automated stock replenishment processes and take a physical stocktaking…"
- **Stock-keeping principles (documented)**: FIFO; all incoming goods registered as **batches**; each sold/written-off/transferred unit subtracted from the oldest batch; COGS = sum of costs of sold items; inventory value = total cost of batches in stock.
- **Inventory document types**: **Inventory Registration** (add stock in), **Inventory Write-Off** (remove stock, with reason codes such as expiration or breakage), **Inventory Transfer** (between locations), **Waybill** (document that pulls stock out), Purchase Invoice (receipt with cost). Documents must be **confirmed**; confirmation is the moment inventory transactions process ("items will come into stock and go out in the same order as the documents are confirmed… not possible to back date or post date"). Confirmed documents' lines are locked (copy + credit to change).
- **Stock sufficiency rule**: transfers require sufficient stock at confirm; insufficient → error / left unconfirmed.
- **Physical Stocktaking**: full or partial; pausable and resumable; count confirmed; **variances accounted via inventory registration and write-offs**; mobile stocktaking with Bluetooth/USB barcode scanners (Stocktake app).
- **Replenishment**: "Stock Replenishment — review and replenish stock levels… manage the restocking process across all locations"; "Restock and render points can be set up to enable inventory notifications when stock levels reach a predefined threshold." Central Purchasing and Distribution available on the new inventory system.
- **Purchasing side**: Purchase Orders, Receive PO in bulk, Late Deliveries Report (undelivered PO lines past supplier deadline), suppliers with groups and contact persons.
- **Product structure feeding inventory**: product catalog (stock vs non-stock items — "Non-stock products cannot hold inventory"), matrix products (size/color variations), **assembly products** (made/assembled/bundled; components may or may not sell separately), **bundle products** ("pull the products included in the recipe out of inventory every time the bundle is sold").
- **Locations**: "Locations in Erply represent a physical store where you will sell items out of"; registers are POS stations within a location. Chain/franchise module for multi-store setups.
- **Reports**: inventory summary, in/out of stock, purchases and sales by period, stock replenishment, central purchasing, inventory registrations / write-offs / transfers reports, COGS reports; "All stock (positive and negative)" report — negative stock is a first-class visible state.
- **Permissions**: user groups with permission levels over back office/POS/API and per-feature view/add/edit/delete.
- Historical migration note: an "old" vs "new" inventory system exists; upgrade re-registers all inventory from a transition date and locks prior documents — evidence that the document-confirmed ledger model is a deliberate design (and that older accounts ran a looser model).

## Product C — NetSuite Inventory Management (Oracle docs)

Evidence layer: A (direct observation, official help; generic-ERP pole).

Key observations:

- **Stock assessment**: quantities on item records, lists, inventory reports, saved searches; **negative inventory review** is a named workflow ("Run a report to view any negative inventory quantities that you can adjust or replenish").
- **Adjustment**: **Inventory Adjustment** and **Inventory Worksheet** forms adjust on-hand without a PO.
- **Counts**: **Inventory Count** feature — physical count; "an approved count automatically creates the necessary inventory adjustments to reconcile your inventory." (Smart Count and Item 360 Dashboard exist as named add-on surfaces.)
- **Movement between locations**: **Inventory Transfer** (increase one location, decrease another), **Transfer Order** ("schedule and track the movement"), Intercompany Transfer Order (between subsidiaries), **Inventory Distribution** form to allocate unallocated inventory right after multi-location setup.
- **Replenishment**: PO receipt auto-adjusts stock; **reorder points and preferred stock levels** per item per location; **Order Items** form determines what needs replenishing and submits POs in bulk; **Replenish Location By Inventory Transfer / By Transfer Order** worksheets move stock between locations based on those levels.
- **Sell/fulfill linkage**: "Selling and fulfilling items from your inventory affects your stock levels, accounting records, and item commitment"; backorder tracking; "underwater inventory" alerts.
- **Allocation machinery**: item commitment (allocate stock to open orders), Commit Order Schedule, **Reallocate Items** transaction (move received stock between open orders) — order-allocation depth beyond the retail-store pole.
- **Warehouse depth (advanced features)**: Bin Management (bins within location; bin transfers and putaway), Advanced Bin/Numbered Inventory (serialized/lot-numbered items), Inventory Status (status per stock record) — this is where NetSuite crosses toward WMS territory.
- Multi-location inventory, OneWorld subsidiaries, costing and inventory reporting (Inventory Reporting chapter, SuiteAnalytics workbooks).

## Product D — Cin7 Core (help center + product page)

Evidence layer: A for help-center articles; B/marketing for product-page claims.

Key observations (help center, Tier-1):

- **Stock quantity model**: named article "Calculation of Available, On Hand and Allocated Stock quantity" — on-hand vs allocated vs available is an explicit user-facing distinction.
- **Stocktake** (full article): per-location; **location locked while stocktake in progress** ("inventory cannot be used, sold, or moved"; e-commerce sales still load but stay Pending until stocktake completes); effective date used for the journal entries the stocktake triggers; expense account selected; filters (stock locators, categories, brands, tags, bins, bin groups, pick zones) define the counted product set; two sections — non-zero and zero stock on hand (zero section catches items present physically but not in the system); entry by manual input, barcode scan (scan increments), or CSV export/import; Save (draft) vs Complete (unlocks location); **Undo** reverses transactions back to draft; stocktake generates accounting transactions (synced to accounting; can be skipped for "fake" stocktakes correcting data-entry errors); Financials tab, Activity log (username + timestamp), attachments, print; only **Stock**-type products stocktake (services, fixed assets, non-inventory, gift cards excluded); batch/serial numbers on lines.
- **Stock transfers**, **location supply rules and transfer planning** (rule-based replenishment between locations), **low stock reorder**, **reorder parameters**, **generate reorder suggestions**.
- **Inventory write-off** as a named document; **stock adjustment and revaluation**; costs allocable to transfers and adjustments.
- **Costing**: FIFO (batch) costing method named; "Calculate current and historical inventory value."
- **Stock receipt and put away** section (purchasing side); suppliers, purchase orders/invoices, supplier credit notes.
- **Inventory reports** and **audit reports** categories; roles and permissions (stocktake permissions named).
- **POS module**: "POS products and stock" — POS sales draw on the same stock.
- Product page (marketing, Tier-2): source → store → sell → bill → report → restock loop; on-hand/committed/in-transit visibility; bins and batches; multichannel sync (Shopify/Amazon/POS) to prevent overselling; AI forecasting (ForesightAI) with automated reordering; 700+ integrations; "full IMS, sometimes called ERP Lite."

## Cross-product Comparison

| Structure | Square for Retail | Erply | NetSuite | Cin7 Core | Layer |
|---|---|---|---|---|---|
| Stock record: item(+variation) × location, quantity on hand | ✓ | ✓ | ✓ | ✓ | B |
| Selling auto-decrements stock (POS / sales docs / orders) | ✓ | ✓ | ✓ | ✓ | B |
| Receiving from purchase orders brings stock in | ✓ | ✓ | ✓ | ✓ | B |
| Manual adjustment without a PO | ✓ (reasons) | ✓ (Registration / Write-Off) | ✓ (Adjustment / Worksheet) | ✓ (adjustment / write-off) | B |
| Adjustment reasons (damage/theft/loss/expiry…) | ✓ explicit list + custom | ✓ reason codes | (adjustment forms; reasons not fetched) | ✓ write-off doc | B (form varies) |
| Physical count reconciles record to actual | ✓ (full + cycle; review/approve) | ✓ (full/partial, pausable) | ✓ (approved count auto-adjusts) | ✓ (stocktake; location lock) | B |
| Count produces variance visibility | ✓ (variance by count & cost) | ✓ (variances via registration/write-off) | ✓ (auto adjustments) | ✓ (financials + activity log) | B |
| Transfers between locations | ✓ (+ transfer orders) | ✓ (sufficiency check at confirm) | ✓ (transfer + transfer order + intercompany) | ✓ (+ supply rules/planning) | B |
| Replenishment machinery | ✓ (alerts → PO) | ✓ (restock/render points; stock replenishment) | ✓ (reorder points, preferred levels, bulk PO) | ✓ (reorder params, suggestions, AI forecast) | B |
| Vendors + purchase orders + expected dates | ✓ | ✓ (+ late deliveries report) | ✓ | ✓ | B |
| Cost tracking: unit cost, COGS, inventory value | ✓ | ✓ (FIFO batches) | ✓ | ✓ (FIFO batch; revaluation) | B |
| Accounting linkage | ✓ (COGS report) | ✓ (export to accounting) | ✓ (native GL) | ✓ (journal sync per stocktake) | B (depth varies) |
| Permissions on stock actions | ✓ | ✓ (user groups) | ✓ (roles) | ✓ (stocktake permissions) | B |
| Audit trail / adjustment history | ✓ | ✓ (document reports; deletion logs) | ✓ | ✓ (activity log) | B |
| Multi-location as first-class structure | ✓ | ✓ (locations = stores; chain module) | ✓ (multi-location; subsidiaries) | ✓ (locations/warehouses) | B |
| Negative stock as visible, correctable state | not observed | ✓ | ✓ | ✓ (error cases) | B (3/4) |
| Barcode/SKU/GTIN identification + labels | ✓ (labels) | ✓ (scanners) | (bar coding named) | ✓ (scan in stocktake) | B |
| Bins / serial / lot tracking | not in retail docs | (separate WMS) | ✓ (advanced features) | ✓ (bins, batch/serial) | C-variant |
| Unit conversions (case/unit, weighed) | ✓ (stock conversion) | — | — | ✓ (pack/carton quantities) | C-variant |
| Order allocation / commitment to customer orders | — | (layaway/order docs book stock) | ✓ (commit/reallocate) | ✓ (allocated vs available) | C-variant |
| Location locked during count | — | — | — | ✓ | product-specific |
| Full count sets uncounted items to zero | ✓ | — | — | — | product-specific |
| Document-confirm ledger semantics (no backdating) | — | ✓ | — | — | product-specific |
| AI demand forecasting / automated reordering | — | — | — | ✓ (ForesightAI) | product-specific (era-common trend) |
| Central purchasing & distribution (HQ→stores) | — | ✓ | (intercompany analog) | (supply rules analog) | C-variant |

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the product stops being recognizable as retail inventory management:

1. **Item-level stock records at named locations** — for each sellable item (and its variations), the system holds a quantity on hand per location (store, stockroom, warehouse). The stock record is the system of record for "how much we have, where."
2. **Recorded stock movements** — dated, attributable events that change on-hand: goods received in, goods sold or otherwise removed out, corrections, and movements between locations. On-hand is never edited in a vacuum; it changes through movements.
3. **Physical count reconciliation** — a recorded count of actual stock, compared against the record, with the difference reconciled back into the record as adjustments.

Historical check: paper stock ledgers / stock cards (perpetual inventory), PLU-based stock tracking in electronic cash registers, and batch-upload stocktaking terminals all satisfy these three properties. Modern implementations (cloud sync, omnichannel, AI reorder) are not required. L0 holds.

Deliberately NOT in L0 (tested against the sample): replenishment machinery (a bare perpetual-inventory ledger with counts is still this Type), purchase orders, cost/COGS machinery, permissions, POS integration as a mechanism (historically stock-out was posted by hand from sales slips), omnichannel sync, bins/serials.

### L1 — Common Mature Structure

Present across the researched sample (Layer B):

- **Replenishment machinery** — low-stock thresholds/alerts, reorder points / preferred stock levels, reorder suggestions, and generation of purchase orders from them. Universal in the sample; the practical purpose of the record.
- **Purchasing side** — vendors/suppliers, purchase orders (vendor, expected date, lines with quantities and unit costs), receiving (full/partial), supplier performance signals (late deliveries).
- **Transfers between locations** — direct transfers and/or order-shaped transfer documents; sufficiency checks in stricter implementations.
- **Cost and value layer** — unit costs, COGS, inventory value, costing methods (FIFO/batch named in two products), revaluation.
- **Adjustment reasons** — damage, theft, loss, expiry, recount, returns-to-stock; reason-coded adjustments are the shrinkage-visibility mechanism.
- **Count discipline** — full vs partial/cycle counts, count sessions with review/approval, variance reporting (by quantity and by cost).
- **Permissions and attribution** — stock actions gated by role; adjustments and counts attributed to users; audit/activity logs.
- **Reporting** — stock levels, movements in/out, variance, aging, valuation; inventory reports as a first-class category.
- **Identification** — SKU/barcode/GTIN; scanning as the dominant data-entry mode; label printing in retail-facing products.
- **Sales-channel linkage** — selling (POS, sales orders, e-commerce) decrements stock automatically; the stock record feeds availability back.

### L2 — Variant / Optional Structure

- **Scope posture**: single-store back office ↔ chain/HQ central purchasing & distribution ↔ multichannel stock hub (stores + warehouses + e-commerce channels).
- **Warehouse depth**: bins, serial/lot tracking, pick zones, putaway — the WMS-flavored extension (present in the ERP and IMS poles; separate WMS products in the retail-suite pole).
- **Order-allocation depth**: on-hand vs allocated vs available; commit/reallocate stock to customer orders (stronger in order-management-heavy poles).
- **Unit handling**: stock conversion (case ↔ sell-by unit), weighed goods, pack/carton quantities.
- **Count posture**: lock-location strictness, uncounted-items policy, effective dating, count via dedicated mobile apps.
- **Ledger strictness**: document-confirm semantics with no backdating (one product) vs looser editable records; negative stock tolerated vs blocked.
- **Forecasting/AI**: demand forecasting and automated reordering (era-common trend, one product in sample).
- **Consignment stock, assembly/bundle recipes** (bundle sale pulls components), intercompany transfers.
- **Accounting integration depth**: native GL ↔ journal sync ↔ report/export.
- **Commercial packaging**: advanced inventory gated behind plan tiers (one product).

### L3 — Vendor-specific (research notes only)

- Square: adjustment-reason list (Stock received / Inventory recount / Damage / Theft / Loss / Restock return) + custom reasons; 500-item PO limit; PO decimal-quantity restriction; "retail mode" in the POS app; Plus/Premium plan gating; daily alert emails; profit-margin display at receiving; aging report.
- Erply: document set (Inventory Registration / Write-Off / Transfer / Waybill / Purchase Invoice); confirm-to-post semantics with locked confirmed lines; FIFO batch as the stock-keeping principle; "restock and render points"; old→new inventory system migration with transition-date re-registration; Central Purchasing and Distribution; bundle-recipe stock pull; Stocktake mobile app.
- NetSuite: Inventory Adjustment vs Inventory Worksheet forms; Inventory Distribution (unallocated stock at setup); Replenish Location By Transfer worksheets; item commitment / Commit Order Schedule / Reallocate Items; Bin Management + Advanced Bin/Numbered Inventory + Inventory Status feature ladder; Smart Count; Item 360 Dashboard; intercompany transfer orders; "underwater inventory" alerts.
- Cin7 Core: location lock during stocktake with e-commerce sales held Pending; effective date + expense account on stocktake; zero-stock-on-hand section catching unregistered physical items; skip-sync for "fake" stocktakes; Available/On-Hand/Allocated calculation article; ForesightAI; "ERP Lite" self-positioning.

## Rejected Findings

- "Retail inventory management = ERP inventory module" — rejected: the SMB POS-integrated pole (Square) carries the same core without ERP machinery; the ERP is a packaging pole, not the definition.
- "Replenishment/forecasting is the defining core" — rejected: a perpetual-inventory ledger with counts (historical and minimal modern forms) is still this Type; forecasting is an L2 trend.
- "Bins/serial/lot tracking is core" — rejected: absent from the retail-suite pole's inventory module (delivered by separate WMS products); it is warehouse depth, not retail inventory definition.
- "Omnichannel sync is core" — rejected: single-store retail inventory predates and exists without e-commerce sync; it is a channel-depth variant.
- "Inventory management includes merchandising decisions (what to buy, assortment)" — rejected: sampled products track and replenish what the business already sells; assortment/category planning is a different Type (05.13).

## Boundary Findings

- **vs Retail POS**: the POS executes sales and decrements stock as a side effect; it does not own receiving, counts, replenishment, or the stock ledger. Remove the stock ledger/receiving/counting from a POS and it remains a POS; remove sale execution from RIM and it remains RIM. The two share the stock numbers and the item catalog; the boundary is which system is the record of record for stock and which job owns it. (Consistent with the processed Retail POS document.)
- **vs generic Inventory Management System (§10)**: same machinery (stock records, movements, counts, replenishment), different domain instantiation. Retail instantiation: items are merchandise for sale, locations are stores/stockrooms, stock-out is dominated by POS sales, replenishment serves selling locations, shrinkage reasons and price labels appear, counts happen on the sales floor. The generic Type serves any stock-holding operation (materials, assets, equipment). Domain siblings, like Nonprofit CRM vs CRM. NetSuite sits exactly on this seam: one inventory engine, retail as one use.
- **vs WMS**: WMS manages how stock is physically handled inside a warehouse (bins, picking, putaway, waves); RIM manages what/how much stock exists and how it changes. Bin/serial depth is the blur zone (NetSuite/Cin7 carry both; Erply ships a separate WMS).
- **vs Merchandising / Assortment Planning (05.13)**: merchandising decides what to buy and how to present it (forward-looking planning); RIM records and maintains what is actually there (operational truth). Replenishment quantity suggestions touch planning, but the record-keeping spine is RIM.
- **vs PIM (05.04)**: PIM owns product data (descriptions, images, attributes, categories); RIM owns quantities. Erply separates the two modules explicitly; a stock record references a product but does not describe it.
- **vs Order Management (05.07)**: OMS orchestrates customer orders to fulfillment; RIM holds the stock those orders draw against. Allocation/commitment features (NetSuite, Cin7) are the shared seam.
- **vs Demand Planning (§10)**: forecasting what will sell is planning; recording what is and what moved is RIM. AI forecasting in one sampled product is an adjacent capability riding on RIM data.
- **Sibling leaf "Store Inventory Application"**: the researched evidence shows one Type operating at two scopes — store-scoped (single location's stock, counts, receiving) and chain-scoped (HQ central purchasing, distribution, cross-store transfers). No structural difference was found that would make a second Type; scope looks like a variant axis. Flag for joint review.

## Uncertainties

- Lightspeed Retail and Shopify could not be fetched; the SMB/mid retail-suite pole beyond Square is evidenced by Erply instead. Claims about "most retail suites" are calibrated to the four-product sample.
- NetSuite's count reasons and retail-specific behaviors were only partially fetched (Basic chapter + book TOC); its retail depth (e.g., retail-specific count flows) is unverified.
- Whether "full count sets uncounted items to zero" is a widespread convention is unknown (single-product observation) — kept product-dependent.
- The exact relationship between RIM and financial inventory accounting (periodic vs perpetual, GL subledger status) varies by product; the sample shows journal-sync and COGS-report postures but a full accounting treatment was not researched.
- Restaurant/grocery ingredient-level inventory (recipe/ingredient tracking) was observed only as a named adjacent module in one product; not researched here.

## Final Synthesis

Retail Inventory Management is the back-office stock system of record for a retail business: it holds item-level stock records at named locations, changes them only through recorded movements (receiving in, selling out, reason-coded adjustments, transfers), reconciles them to physical reality through counts, and turns the record into stocking action through replenishment machinery (thresholds, reorder points, suggestions, purchase orders). Mature products wrap this spine with cost/valuation layers, permissions and audit, reporting, barcode identification, and sales-channel linkage; variants extend it along scope (store ↔ chain ↔ multichannel hub), warehouse depth (bins/serials), allocation depth, and forecasting. Its neighbors are separated by ownership of the record: the POS sells from the stock record, the WMS handles stock physically, merchandising plans it, PIM describes it, the OMS draws it down against orders — RIM is the place where the stock truth lives.
