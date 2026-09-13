# Research Notes — Inventory Management System

## Research Goal

Understand what a generic Inventory Management System actually is, from real products: what objects exist inside it, who uses it, how stock work flows, which states and rules matter, and where its boundaries lie against Retail Inventory Management, WMS, ERP, Order Management, Purchase Order Management, asset-management Types, and planning Types.

Directory context: leaf `Inventory Management System` under §10 Enterprise Operations & Administration, listed between Purchase Order Management and Warehouse Management System. Domain siblings elsewhere in the directory: Retail Inventory Management / Store Inventory Application (§05.12, retail-inventory-management already processed 2026-09-07), Restaurant Inventory Management (§26), Telecom Inventory Management (§19). The already-processed retail pass explicitly positions this leaf as the "domain sibling — same machinery (records, movements, counts, replenishment) applied to any stock-holding operation."

## Initial Boundary

Working hypothesis before research:

- Core purpose: keep a trustworthy record of what stock a business has, where, and how it changed — and turn that record into stocking action.
- Users: inventory controllers, warehouse/stockroom staff, operations managers, buyers; not cashiers (that is POS territory).
- Nearest neighbors: Retail Inventory Management (domain sibling), WMS (physical handling), ERP (suite embedding), Order Management (customer orders), Purchase Order Management (buying commitments), IT Asset Management / Enterprise Asset Registry / CMMS parts (identified-item custody vs stock quantities), Demand/Supply Planning (forecast vs record).
- Likely confusion: with ERP inventory modules (packaging, not Type), with WMS (depth blur at bin level), with asset tracking (identified items vs quantities).

## Research Questions

1. What is the central object — item, SKU, stock record, location, warehouse?
2. How does stock change: what event/movement types exist (in, out, between, adjust, manufacture)?
3. How do orders (sales/purchase) connect to the stock record, and is order linkage definitional?
4. How do counts/reconciliation work, and are they definitional or common?
5. How does replenishment work — reorder points, alerts, suggestions, order generation?
6. What cost/valuation machinery exists (unit cost, COGS, valuation methods, GL integration)?
7. How do multi-location and transfers work (transfer documents, in-transit states)?
8. What identification machinery exists (SKU/barcode/serial/lot, scanning, labels)?
9. What rules matter — negative stock, sufficiency checks, permissions, approval, audit?
10. What is the minimal structure that survives across the simplest and most complex products (and across eras)?
11. Where exactly are the lines to Retail Inventory Management, WMS, ERP, OMS, PO Management, asset Types, and planning Types?

## Representative Products

| Product | Pole | Customer tier | Why selected |
|---|---|---|---|
| Zoho Inventory | order-centric multichannel inventory for online sellers; full document set (SO/PO/TO/adjustments/counts/assemblies) | SMB / mid-market | dominant SMB multichannel pattern; extensive Tier-1 help docs |
| inFlow Inventory | standalone inventory-first software for product businesses; deep quantity-state model | SMB | the inventory-first standalone pole; strong Tier-1 learning center |
| ERPNext (Stock module) | ERP-integrated open-source stock ledger; movement documents with purposes; perpetual inventory | mid-market / self-hosted | shows the ERP-module pole and the ledger/document philosophy |
| Sortly | simple visual item-and-folder tracking for any business; no order machinery | micro-SMB / any-business (facilities, field service, contractors) | the minimal pole — calibrates what is definitional vs common |

Rejected/abandoned candidates: Odoo (docs 403 — also 403 in the purchase-order-management pass), Fishbowl (/help and /support 404 ×2), Katana (help transport error + 404), Unleashed (support portal requires sign-in), Cin7 Omni / DEAR Systems (help.dear.systems transport error), Microsoft Dynamics 365 (learn.microsoft.com inventory URLs 404 ×2), Linnworks (support center reachable but order-management-first and channel-integration-focused; sampling stopped per stop conditions). NetSuite Inventory Management was directly observed in the retail-inventory-management pass (2026-09-07) and is used here only as cross-pass context, not as fresh evidence.

## Sources

All fetched 2026-09-07.

- Zoho Inventory Help (User Guide) — "Access Zoho Inventory" (getting-started); "Items"; "Stock Counts"; "Replenishment"; "Inventory Adjustments"; "Warehouses – Overview"; "Transfer Orders"; "Assemblies" — https://www.zoho.com/inventory/help/
- inFlow Inventory Learning Center — "What is quantity reserved, on hand, available, etc?"; "How to create and complete a stock count (Web)"; "How to set up product reordering in inFlow"; "Managing products" article index — https://www.inflowinventory.com/support/
- ERPNext Documentation — "Introduction to Stock Module"; "Stock Entry"; "Stock Reconciliation" — https://docs.frappe.io/erpnext/
- Sortly Help Center — "Sortly Product Overview"; "Quantity Alerts"; "Reports Overview"; "Getting Started with Sortly: A Quick Start Guide" — https://help.sortly.com/

Source-access limitations: Odoo, Fishbowl, Katana, Unleashed, Cin7 Omni/DEAR, and Dynamics 365 could not be reached (see Representative Products). The enterprise-suite pole is therefore evidenced only indirectly (ERPNext as the ERP-module pole; NetSuite via the prior retail pass). ERPNext's auto-reorder documentation page could not be fetched (404), so ERPNext replenishment claims are omitted rather than filled from memory. Sortly's feature set is evidenced by its help center; absence claims (no order machinery, no documented count workflow) are absence-in-documentation observations, not certified product limits.

## Product A — Zoho Inventory (help docs)

Evidence layer: A (direct observation, official user guide).

Key observations:

- **Items are the stock carriers.** Item types: Goods vs Service — "Inventory tracking is available only for goods, not for services." Track Inventory is a per-item toggle. Items carry SKU plus additional identifiers (UPC, EAN, MPN, ISBN); variants managed under a parent item with attribute-based SKU generation; opening stock entered per variant per warehouse.
- **Costing is a per-item choice with an accounting account**: FIFO or WAC (weighted average cost), with an Inventory Account; COGS and inventory value derive from it. Value Adjustment exists as a separate document (revaluation when unit cost changes).
- **Reorder point per item** triggers in-app notifications; a dedicated **Replenishments** module holds per-item/per-warehouse replenishment configs: order type (Purchase Order or Transfer Order), preferred vendor or source location, reorder level, maximum stock level, min/max order quantity, unit multiple, check frequency. Falling below the reorder level lists the item under **Pending Replenishments**, from which the user creates the PO/TO (manually or in bulk); replenishments can be dismissed; history is kept.
- **Stock Counts** (Premium/Enterprise plans or warehouse-operations add-on; requires multi-warehouse): count created per warehouse, assigned to a user, optionally recurring (periodic or custom schedule with reminders); counting happens in the mobile app (scan or key entry; serial/batch items require tracking details); statuses: Yet To Start → Counting in Progress → Pending Approval → Completed / Cancelled; approval is web-side and permission-gated (only users with access can see system quantity); per-item approve/reject — unmatched items get an adjustment reason or a recount; approvers see a "Variation" badge listing suspected transactions that occurred during the count; approval creates a Quantity Adjustment posted to a COGS-linked account with default reason "Stock taking results" (customizable).
- **Inventory Adjustments** module: **Quantity Adjustment** (reason-coded — theft, damage, data-entry error, write-off, donation; custom reasons manageable; warehouse-scoped; cost price captured; Save as Draft → Convert to Adjusted) and **Value Adjustment** (revaluation of in-stock items). Adjustments appear on the item's Adjustments tab and in FIFO cost-lot tracking.
- **Warehouses/Locations**: multi-warehouse toggle; first warehouse is Primary (default stock target for transactions); deactivating a warehouse freezes its stock; **warehouse restrictions** map users to permitted warehouses (restricted users see only permitted-warehouse stock and transactions; a transaction is openable only if all its warehouses are permitted); bin locations tracked per item; Business Locations vs Warehouse-Only Locations distinction.
- **Transfer Orders**: numbered document with source/destination warehouse, reason, and source/destination stock shown; **Initiate Transfer** (status In Transit; manual receive later) vs **Transfer and Receive** (instant); Mark as Received with receive date; serial/batch quantities transfer with explicit serial/batch selection; optional approval workflow (submit → approver → Approve and Initiate Transfer → Mark as Transferred); carrier tracking of in-transit transfers via AfterShip integration.
- **Assemblies**: composite items combine component items (and services) into a finished item; assembling consumes components and increases composite stock; can assemble on the fly from a sales order/invoice when ordered quantity exceeds available; deleting an assembly restores component stock; serial/batch details carried into assemblies.
- **Order machinery around the stock record**: Sales Orders → Packages → Shipments; picklists; backorders; dropshipment; sales returns. Purchase Orders → Purchase Receives → Bills; purchase returns; vendor credits. **Material Request / Material Issue / Material Return** documents for internal material movements.
- **Governance**: transaction approval workflows (custom approvals), record locking, validation rules, users & roles.
- **Integrations**: sales channels (Shopify, Amazon, marketplaces), shipping carriers, accounting (QuickBooks Online, Xero, Zoho Books), CRM.
- **Reports**: inventory reports, advanced inventory reports, inventory valuation reports, warehouse reports, activity reports.
- Plan gating is explicit in docs (Stock Counts on Premium/Enterprise; advanced tracking plan-gated) — vendor commercial facts, kept here.

## Product B — inFlow Inventory (learning center)

Evidence layer: A (direct observation, official support articles).

Key observations:

- **The quantity model is the product's spine** ("What is quantity reserved, on hand, available, etc?"): per product per location, the record distinguishes **on hand** (physically present minus picked), **available** (what remains if all open sales and manufacture orders fulfill), **reserved** (open unpicked sales orders + outgoing transfers + MO components + anticipated builds; expiring lots listed within reserved), **unreserved** (on hand − reserved), **picked** (awaiting shipment), **buildable** (how many bundles/BOM products could be built from components), **on order** (waiting on vendor / manufacturing / transfer / stock), **in transit** (sent transfers not yet received), **quantity owned** (on hand + picked), and a **negative stock** badge (oversold or transferred-before-restocked).
- **Stock counts (Web)**: created per location; product selection by "all products at this location" (zero-quantity products excluded), by category (zero included), or manual; **snapshot semantics** — "Stock counts provide a snapshot of your inventory… the System quantity will not update if back-dated orders are added after the count has been completed"; guidance to stop processing orders and movements during the count; **multiple count sheets** split across team members with per-sheet status and visibility of who is working; review status to double-check counts.
- **Reordering**: per product per location — reorder point ("minimum stock level before you need to reorder") and reorder quantity; **reorder method selectable: purchase order, stock transfer, or manufacture order**; a Reorder Stock screen lists what is low per location and generates the orders in bulk; low-stock email notifications; inFlow can recommend a reorder point from history.
- **Manufacturing**: bill of materials, manufacture orders (consume components → produce finished goods), disassembly, production management, manufacturing operations (labor/operations), MO components blocked from going negative.
- **Locations**: main locations plus **sublocations** (aisles, bins) — WMS-adjacent depth.
- **Tracking**: serial numbers; **lot numbers with expiry dates** (expiring quantity surfaced inside reserved); units of measure (buy in one unit, sell in another).
- **Adjacent uses marketed by the same product**: consignment tracking, asset tracking, rental services, items out for repair — the identified-item blur zone.
- **Purchasing**: POs with partial receiving, receiving to multiple locations on one PO, PO approvals, backorder POs, dropship orders, returns to vendor, product lead times, tariff/fee handling.
- **Sales**: partial fulfillment, picking allocations, backorders, dropship, pick/pack/ship.
- **Cost**: product cost/COGS calculation articles; cost correction flows.
- **History**: per-product movement/transaction history; historical inventory report (point-in-time levels); movement-history-vs-report reconciliation guidance.
- **Integrations**: Shopify, Amazon, WooCommerce, Squarespace, Square, QuickBooks Online, Xero, Zapier, EasyPost, API; Stockroom add-on (scan in/out); B2B portal (Showroom).
- Negative inventory is explicitly framed as a state to avoid and correct, not silently clamp.

## Product C — ERPNext Stock module (docs)

Evidence layer: A (direct observation, official docs; ERP-module pole).

Key observations:

- **Stock module scope** (module intro): inventory tracking, item management, stock transactions, stock reconciliation, reports/analytics.
- **Stock Entry is the universal movement document**, typed by purpose: Material Issue (outgoing), Material Receipt (incoming), Material Transfer (between internal warehouses), Material Transfer for Manufacturing (against Work Order/Job Card), Material Consumption for Manufacture, Manufacture (receipt from production), Repack (items into new items), Send to Subcontractor. Source and Target warehouses per line; rate and valuation fetched/calculated; "Allow Zero Valuation Rate" for samples; **quality inspection can be required before submission**; scrap items with valuation; **process loss** accounting (unproduced quantity's cost absorbed into finished goods); **additional costs** (shipping, customs, operating costs) distributed proportionally into receiving items' valuation rate; accounting dimensions (projects); **perpetual inventory** — stock entries post to the general ledger; **Add to Transit** — two-step transfer through a Transit-type warehouse (issue to transit → End Transit / receive at destination); submitted entries are changed by cancel-and-amend.
- **Stock Reconciliation**: two purposes — **Opening Stock** (posting initial quantities with valuation rate; difference account "Temporary Opening") and **Stock Reconciliation** (count actual → set quantity/valuation → difference account "Stock Adjustment"); CSV template upload for large counts; fetch current balance and valuation as of a specific date/time; **barcode scan mode** (incremental scanning builds the counted quantity); serial/batch bundles with "reconcile all" or "reconcile selected" serials/batches.
- Items have a "Maintain Stock" toggle; warehouses are the location units; serial/batch tracking with auto-generation options.
- Valuation rate is a first-class field on every movement; inventory value and stock ledger reports derive from it. (Auto-reorder docs page unreachable — replenishment machinery not directly verified for this product.)

## Product D — Sortly (help center)

Evidence layer: A (direct observation, official help center; minimal pole).

Key observations:

- **Items and folders are the whole world**: items carry name, description, quantity, price, photos, variants, custom fields (text/number/checkbox/date), tags; folders (nestable) organize by location, category, or job — "if managing inventory for specific jobs, you'd create folders for Available Inventory and separate ones for each job… for items moving between locations or warehouses, set up folders for each location."
- **Two movement idioms, both recorded**: (1) **move items between folders** — "this mimics real-life inventory management"; Move Summary report shows origins, destinations, moved quantities and values over time; (2) **update quantities with reasons** — "for asset or consumption tracking, instead of moving items between folders, you update quantities and specify reasons for changes (e.g., consumed, sold, restocked). Adding Transaction Notes captures additional details."
- **Transactions report** tracks "all quantity-changing actions such as Create, Clone, Update Quantity, Merge, Restore, Delete, and Move," showing item data at the moment of each transaction; **Transaction Reason and Transaction Note are editable** on transactions; **Item Flow** report aggregates increases/decreases by item and folder over a date range; **Activity History** tracks all user changes (Moved, Edited, Deleted, Created, Restored, Quantity Changed, Merged).
- **No order machinery**: no purchase orders, sales orders, manufacturing, or BOM anywhere in the documented feature set. **No formal count/reconciliation workflow** documented — reconciliation happens by editing quantities (with reasons); Inventory Summary is real-time only, with a separate **Inventory Snapshot** (automated monthly point-in-time snapshot, ~13 months of history) for historical views.
- **Alerts**: quantity alerts per item or in bulk (conditions like "at or below Min Level," recipient selection — owners/admins/members/specific people), date-based reminders (expiry, maintenance) driven by custom date fields; Manage Alerts console; alerts not available on the Free plan.
- **Identification**: QR code and barcode label creation/printing (thermal printers supported); mobile scanning to add items and auto-populate details; Sortly ID (SID) as native identifier.
- **Team**: roles (Owner/Admin/Member), folder-level permissions, user seats; User Activity Summary report for admins.
- **Reports**: Inventory Summary (real-time), Low Stock, Transactions, Item Flow, Move Summary, Activity History, User Activity Summary; custom reports and scheduled/subscribed reports on higher plans; CSV/XLSX export.
- **Integrations**: QuickBooks Online, AppFolio; API.

## Cross-product Comparison

| Dimension | Zoho Inventory | inFlow | ERPNext (Stock) | Sortly |
|---|---|---|---|---|
| Item-level stock records at locations | ✓ (items/variants × warehouses; track-inventory toggle; goods only) | ✓ (products × locations/sublocations) | ✓ (items with Maintain Stock × warehouses) | ✓ (items × folders; quantity + price) |
| Recorded stock events | ✓ (documents: receipts, shipments, transfers, adjustments, assemblies; draft→converted) | ✓ (movement history; every order/transfer/adjustment posts) | ✓ (Stock Entries typed by purpose; stock ledger; cancel-and-amend) | ✓ (transactions with editable reason + note; moves between folders) |
| Physical count/reconciliation | ✓ (Stock Counts: assign → mobile count → review/approve → adjustment; recurring) | ✓ (stock counts: location snapshot, multi-sheet, review) | ✓ (Stock Reconciliation: opening stock + reconcile; CSV; scan mode) | ✗ (no documented count workflow; correct by editing quantities with reasons) |
| Replenishment machinery | ✓ (reorder levels → Pending Replenishments → PO/TO; frequency; min/max; unit multiples) | ✓ (reorder point + quantity per location → PO/transfer/MO; email alerts; recommended reorder point) | (auto-reorder docs unreachable — unverified) | partial (low-stock alerts only; no order generation) |
| Sales/purchase order linkage | ✓ (SO→package→shipment; PO→receive→bill; backorder; dropship) | ✓ (SO fulfillment/reserved; PO receiving; backorders; dropship) | ✓ (SO/PO + Stock Entry purposes; subcontracting) | ✗ |
| Allocation depth (on-hand vs reserved vs available) | ✓ (stock allocation settings; backorders) | ✓ (explicit reserved/available/unreserved/buildable model) | partial (implied via ordered/delivered quantities) | ✗ |
| Cost & valuation | ✓ (FIFO or WAC per item; COGS; value adjustments; valuation reports) | ✓ (cost/COGS; cost correction) | ✓ (valuation rate on every movement; additional costs into valuation; perpetual GL) | partial (price/value fields; no costing methods) |
| Transfers between locations | ✓ (Transfer Orders: in-transit vs instant; approval; carrier tracking) | ✓ (stock transfers; in-transit; reserved while outgoing) | ✓ (Material Transfer; Add to Transit two-step) | ✓ (move between folders; Move Summary) |
| Serial/lot/batch | ✓ (serial OR batch per item; expiry; serial/batch on transfers/adjustments/counts) | ✓ (serial; lot + expiry) | ✓ (serial/batch bundles; auto-generation) | ✗ (custom fields only) |
| Manufacturing/assembly | ✓ (composite items + assemblies; assemble from SO) | ✓ (BOM, MOs, disassembly, operations) | ✓ (Manufacture/Repack/consumption purposes; BOM; work orders; subcontracting; process loss) | ✗ |
| Bin/sublocation depth | ✓ (bin locations) | ✓ (sublocations: aisles, bins) | (warehouse hierarchy; bins not verified) | ✗ (folders only) |
| Identification & scanning | ✓ (SKU/UPC/EAN/MPN/ISBN; barcode scan; QR generation) | ✓ (SKUs, GS1 barcodes, scanners, label printing) | ✓ (barcodes; scan mode in reconciliation) | ✓ (QR/barcode labels; mobile scan) |
| Permissions & audit | ✓ (roles; warehouse restrictions; record locking; approvals) | ✓ (roles; PO approvals) | ✓ (roles; permission-scoped entry types) | ✓ (Owner/Admin/Member; folder permissions; activity history) |
| Reporting | ✓ (inventory, valuation, warehouse, activity) | ✓ (stock levels, historical inventory, movement) | ✓ (stock ledger, valuation) | ✓ (summary, low stock, transactions, item flow, moves, snapshots) |
| Accounting integration | ✓ (QuickBooks/Xero/Zoho Books) | ✓ (QuickBooks/Xero) | ✓ (native GL; perpetual inventory) | ✓ (QuickBooks) |
| E-commerce channel sync | ✓ (Shopify, Amazon, marketplaces) | ✓ (Shopify, Amazon, WooCommerce, Square) | (via integrations; not verified) | ✗ |
| Negative stock posture | (not directly observed) | flagged as state to avoid; badge visible | (not directly observed) | (not directly observed) |
| Deployment | cloud SaaS | cloud (+ legacy Windows desktop) | self-hosted open-source / cloud | cloud SaaS + mobile |

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

```text
Item-level stock records (what / how much, organized by location)
└── changed only through recorded, attributable stock events
    (receipts in, issues/shipments out, transfers between,
     reason-coded adjustments)
```

Two properties:

1. **Item-level stock records organized by location** — for each stocked item, the system holds quantity on hand per location. This is the system of record for "what do we have, where."
2. **Recorded stock events as the way the record changes** — every quantity change is a dated, attributable event (a movement document, an order posting, or a logged quantity edit with reason). The event history is what makes the record auditable and the stock picture trustworthy.

Test: remove #1 → there is no stock to manage (not an inventory system). Remove #2 → a static quantity list (a spreadsheet), not a managed system. Both properties hold for all four sampled products — including Sortly, whose quantity edits are recorded as transactions with reasons and whose folder moves are recorded as moves — and for paper stock cards and perpetual-inventory ledgers.

Deliberately NOT in L0 (checked against the sample): counts (absent in Sortly), replenishment (absent as order-generation in Sortly), orders (absent in Sortly), costing methods (absent in Sortly), serial/lot (absent in Sortly), barcodes (present in all four but not definitional — paper era), cloud/mobile, AI.

### L1 — Common Mature Structure

Present in most mature products; not required to recognize the Type:

- **Physical count/reconciliation workflows** — count sessions (full/cycle), review/approval before adjustments post, variance handling (3/4 sampled; absent in the minimal pole)
- **Replenishment machinery** — reorder points/levels, low-stock alerts, reorder suggestions, generation of purchase or transfer orders (2/4 full machinery; alerts-only in the minimal pole; unverified in ERPNext)
- **Order linkage** — sales orders/shipments decrement stock, purchase orders/receipts increment it; allocation states (on-hand vs reserved vs available) (3/4)
- **Cost & valuation layer** — unit cost at receipt, COGS, inventory valuation, costing methods (FIFO/weighted average), value revaluation (3/4 full; price-only in the minimal pole)
- **Multi-location transfers** — transfer documents with in-transit states and receive-at-destination steps (4/4)
- **Identification & scanning** — SKU/barcode identifiers, scanning as data entry, label printing (4/4)
- **Permissions, attribution, audit** — roles, user-attributed events, activity logs, approval workflows on sensitive transactions (4/4)
- **Reporting** — stock levels, movements in/out, valuation, low stock, activity (4/4)
- **Integration spine** — accounting (QuickBooks/Xero/native GL) and, where relevant, e-commerce channel sync (4/4 accounting; 2/4 channels)

### L2 — Variant / Optional Structure

Depends on segment, industry, scale, deployment:

- serial / lot / batch tracking with expiry (electronics, pharma, food)
- manufacturing/assembly machinery (BOM, work/manufacture orders, kits, disassembly, subcontracting, process loss)
- bin/sublocation depth (WMS-adjacent)
- negative-stock posture (flagged-and-correctable vs blocked)
- consignment, asset-tracking use, rentals, items-out-for-repair
- dropshipping, backorders
- demand forecasting / AI reorder suggestions
- plan-tier packaging of advanced features
- deployment: standalone SaaS vs ERP module vs open-source self-hosted; desktop heritage vs cloud
- domain anchoring: retail (POS linkage, shrinkage), restaurant (recipe/ingredient), telecom (network equipment), IT (asset register) — same machinery, different vocabulary and integrations

### L3 — Vendor-specific (research notes only)

- Zoho: Stock Counts gated to Premium/Enterprise plans; default adjustment reason "Stock taking results" posted to a COGS-linked account; "Variation" badge listing suspected transactions during counts; Business vs Warehouse-Only Locations; AfterShip transfer tracking; opening-stock caps (200 serials / 100 batches); replenishment fields (unit multiple, frequency, min/max order quantity)
- inFlow: quantity-owned metric (on hand + picked); "combine quantities" setting including buildable in available; auto-selected single count sheet at ≤15 products; Stockroom add-on; Showroom B2B portal; smart-scanner hardware line; reorder method choice including manufacture order
- ERPNext: Stock Entry purpose vocabulary; Transit-type warehouses with End Transit; process-loss cost absorption; cancel-and-amend change model; serial/batch bundles (v15); "Temporary Opening" vs "Stock Adjustment" difference accounts
- Sortly: Sortly ID (SID); ~13-month snapshot history; folder-level alerts; AppFolio integration; alerts absent on Free plan

## Vendor-specific Findings

See L3 above. Additionally: plan gating is a recurring commercial pattern (Zoho Stock Counts on higher plans; Sortly alerts not on Free; inFlow advanced features tiered) — recorded as vendor commercial facts, excluded from the canonical document.

## Boundary Findings

- **vs Retail Inventory Management (§05.12)** — domain sibling, same machinery. The retail instantiation anchors the record to merchandise, stores, POS-driven stock-out, and shrinkage; the generic Type is domain-neutral (distribution, manufacturing, e-commerce, services, facilities). Remove the retail anchoring (POS linkage, store network, shrinkage framing) → generic IMS. The retail pass recorded this exact relationship from its side. Calibration note: the retail pass's defining core includes count reconciliation (all four of its sampled products had counts); this pass's broader sample includes a count-less minimal pole (Sortly), so the generic core is written smaller (records + events) with counts as common mature structure. Both are defensible; the difference is sample-driven calibration, not conflict.
- **vs WMS (§10)** — WMS manages how stock is physically handled inside a warehouse (bins, picking, putaway, waves); IMS manages what/how much exists and how it changes. The blur zone is bin/sublocation depth (inFlow sublocations, Zoho bin locations) and pick/pack surfaces. Remove physical-handling direction → IMS.
- **vs ERP (§10)** — packaging variant, not a different Type. ERPNext shows inventory as a module of a suite with native GL (perpetual inventory); Zoho/inFlow show it standalone with accounting integrations. The machinery is the same; the ERP pole adds ledger postings and suite neighbors.
- **vs Order Management System (§05.07)** — OMS orchestrates customer orders to fulfillment; IMS owns the stock record orders draw on. The shared seam is allocation (reserved/available). Remove order orchestration → IMS.
- **vs Purchase Order Management (§10)** — IMS products embed POs as the stock-in path; the dedicated PO Type centers on the commitment lifecycle (approval, acknowledgment, receiving, invoice matching). PO-as-stock-source vs PO-as-managed-commitment.
- **vs IT Asset Management / Enterprise Asset Registry / CMMS (§14/§10/§16)** — asset Types track identified individual items for custody, maintenance, and lifecycle; IMS tracks quantities of stock items for consumption and sale. The blur zone is identified-item stock (serial-tracked inventory, inFlow's asset-tracking use case, Sortly's asset/consumption framing). Custody-and-maintenance purpose → asset Types; consumption-and-sale purpose → IMS.
- **vs Demand Planning / Supply Planning / Supply Chain Planning (§10)** — planning decides what will be needed (forward-looking); IMS records what is and what moved (operational truth). Reorder suggestions ride on IMS movement history; remove the forecast machinery and the planning Types collapse into IMS.
- **vs Telecom Inventory Management (§19) / Restaurant Inventory Management (§26)** — domain instantiations of the same family; the generic Type is the family's domain-neutral form.

## Historical / Market-Sample Check

Would older, regional, platform-native products still fit the L0?

- **Paper stock cards / perpetual inventory ledgers** (pre-software): one card per item, quantities updated by recorded entries (received/issued), periodic physical counts — satisfies both L0 properties. ✓
- **Early desktop inventory software** (1990s standalone packages): item records, movement entry screens, count sheets — satisfies. ✓
- **ERP inventory modules** (mainframe/mini era through today): stock ledgers, movement documents, reconciliation — satisfies. ✓
- **Simple modern trackers** (Sortly pole): item records, logged quantity changes with reasons — satisfies. ✓

Therefore the L0 (records + recorded events) is era-independent. Barcode scanning, cloud delivery, channel sync, AI suggestions are era-typical implementations, not definitional. The check passed.

## Uncertainties

- ERPNext replenishment machinery (auto-reorder) could not be verified (docs 404) — replenishment claims rest on Zoho + inFlow (+ NetSuite via the prior retail pass).
- Negative-stock posture: directly observed only in inFlow (flagged state to avoid/correct) and Erply/NetSuite (prior retail pass: visible/reportable). Generalized cautiously in the final document.
- Sortly absence claims (no orders, no count workflow) are absence-in-documentation, not certified product limits; Sortly may add features beyond the researched pages.
- The enterprise-suite pole (SAP/Dynamics/Oracle-style inventory) was not directly reachable in this pass; its shape is inferred from ERPNext (same machinery, deeper) and the prior NetSuite observations. Assertion strength kept moderate accordingly.
- Exact numeric limits, plan gates, and default settings are kept here (L3), not in the final document.

## Final Synthesis

The Inventory Management System is the domain-neutral stock system of record: it holds item-level stock records organized by location, and it changes those quantities only through recorded, attributable stock events — receipts in, issues and shipments out, transfers between locations, and reason-coded adjustments. Around that core, mature products add the machinery that makes the record actionable: count reconciliation, replenishment (reorder points → purchase/transfer orders), order linkage with allocation states, cost and valuation, serial/lot tracking, scanning and labels, permissions and audit, reporting, and accounting/channel integrations. Products range from order-centric multichannel suites (Zoho), through inventory-first standalone tools (inFlow), ERP-embedded ledgers (ERPNext), to minimal visual trackers (Sortly) — all recognizable as the same Type from the two-property core. The Type is the family parent of domain instantiations (retail, restaurant, telecom) and is bounded against WMS (physical handling), OMS (order orchestration), PO Management (commitment lifecycle), asset Types (custody vs consumption), and planning Types (forecast vs record).
