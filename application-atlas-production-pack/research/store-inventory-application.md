# Research Notes — Store Inventory Application

## Research Goal

Understand the market referent of the directory leaf `Store Inventory Application` (§05.12 Retail Inventory, sibling of the processed `Retail Inventory Management`): what a store-scoped inventory application actually is, from real products — what objects exist inside it, who uses it, how stock work flows, which states and rules matter, and where its boundaries lie.

Two pending flags from prior passes await this pass (STATUS.md Boundary Issues):

1. **retail-inventory-management (processed) vs store-inventory-application (this leaf)** — scope-variant flag: the inventory pass's evidence (Square/Erply/NetSuite/Cin7) showed one Type operating at two scopes (store-scoped vs chain-scoped) with no structural difference found; joint review recommended. Candidate outcomes: keep-both with a store-vs-chain scope seam, or consolidate as one Type with scope variants.
2. **retail-store-management-system (processed) vs retail-inventory-management + store-inventory-application** — same-substrate consistency note: the same back-office products realize both Types, differing by center (item-level stock ledger vs store as operating unit).

This pass must resolve flag 1 from this side and confirm or amend flag 2.

## Initial Boundary

Working hypothesis before research:

- Core purpose: keep a single store's stock record true and usable — what is on the shelf and in the stockroom, what came in, what went out, what to reorder.
- Users: store owner/manager, stockroom clerk, counter staff (secondary).
- Nearest neighbors: Retail Inventory Management (processed sibling — the flagged joint review), Retail POS (transaction side), generic Inventory Management System (§10), WMS, PIM, Order Management (§05.07), Retail Store Management System (§05.11, processed).
- Likely confusion: with Retail Inventory Management (same machinery, different scope?) and with POS inventory screens (shared stock numbers, different job).

## Research Questions

1. What is the central object — item? stock record? location/folder/warehouse?
2. How does stock change: what movement primitives exist (receive, sell, adjust, transfer, check-out)?
3. How do counts work in store-scoped products — formal sessions or informal corrections?
4. How does receiving work — purchase orders, vendors, or direct registration?
5. How does replenishment work — alerts, reorder points, suggestions?
6. How does selling connect to the stock record (POS / sales orders / manual)?
7. What distinguishes the store-scoped pole from the chain/HQ pole?
8. Is there any structural difference from Retail Inventory Management that would justify a second Type? (the joint-review question)
9. Where exactly are the lines to Retail POS, generic IMS, WMS, PIM, OMS, and the Retail Store Management System?

## Representative Products

| Product | Pole | Customer tier | Why selected |
|---|---|---|---|
| Sortly | visual/mobile-first light pole: items + folders, transactions with reasons, alerts; no PO/COGS/formal count sessions observed | micro-SMB / SMB | the "inventory app for a small store" archetype; tests how light the store-scoped pole can be while staying in-Type |
| inFlow Inventory | SMB product-business ledger: full spine (POs, counts, adjustments, transfers, reorder, COGS) | SMB | strong documentation; shows the store-scoped pole with full ledger depth |
| Zoho Inventory | order-heavy SMB multichannel: warehouses, stock counts with approval, reason-coded adjustments, sales/purchase order machinery | SMB / mid-market | shows the seam where store inventory blends into order management; strong user guide |

Cross-reference (not re-sampled): the sibling pass's Square for Retail, Erply, NetSuite, Cin7 Core — POS-integrated, chain back-office, ERP, and multichannel poles of the same machinery. Their observations are cited from `research/retail-inventory-management.md` where needed for the joint review.

Rejected/abandoned candidates: Boxstorm (retail-specific inventory, by Fishbowl) — transport error on both www and apex URLs, abandoned per the network rule; Stockpile (free tier, thin documentation); Lightspeed Retail and Shopify help centers (unreachable in prior passes, not retried).

## Sources

All fetched 2026-09-08.

- Sortly Help Center — "Sortly Product Overview"; "Quantity Alerts"; "Low Stock Report"; "How to Update Your Inventory" (transactions, move reasons); "Getting started" section index; "FAQs" index — https://help.sortly.com/ ; product page https://www.sortly.com/
- inFlow Inventory Learning Center — "Managing products" section index (88 articles); "What is quantity reserved, on hand, available, etc?"; "How to create and complete a stock count (Web)" — https://www.inflowinventory.com/support/
- Zoho Inventory User Guide — Help index; "Stock Counts"; "Inventory Adjustments" — https://www.zoho.com/inventory/help/

Source-access limitations: Boxstorm transport-failed twice (www + apex), abandoned. inFlow article pages are navigation-heavy; the two fetched article bodies were extracted from saved full output. Sortly's formal-count capability was not observed in any fetched page (see Uncertainties).

## Product A — Sortly (Help Center)

Evidence layer: A (direct observation, official help articles).

Key observations:

- **Items + folders as the world.** Items carry name, description, quantity, price, photos, custom fields, variants, units of measure (standard/custom/partial quantities), unique-item tracking (per-unit QR), consumable tracking by quantity or volume. Folders organize inventory — "typically arranged by location" — with nesting and sub-folders (e.g., per customer/job inside an "Out" folder). An item can be in multiple locations (FAQ).
- **Transactions are the movement record.** "A transaction is any recorded activity that affects the state of your inventory and appears in your Activity History or Reports": quantity updates, moves between folders/locations, create/delete, edits, merges, bulk edit, check-in/check-out workflows. Viewing/searching does not create transactions. Historical quantity on a specific date is answerable (FAQ).
- **Movement modeled as folder moves.** The documented pattern: folders like "Available Inventory" and "Out/Jobs/Rented Out"; moving an item (with quantity) between folders records the real-world movement; sub-folders track who/where it went; Quick Actions on mobile scan items in/out "similar to a check-out scanner at the grocery".
- **Reason-coded movements.** Move reasons: Consumed, Damaged, Donation, End of Life, Expired, Gift, **Inventory Count Adjustment**, Invoice Not Received, Item Recall, Other, Out of Season, Quality Control, Replenish, Return to Supplier, Signed In, Signed Out, **Sold**. Notes can be added but cannot be made mandatory.
- **Replenishment = alerts + report.** Quantity alerts on min levels (threshold conditions, per-item or bulk, recipients drawn from account users; plan-gated); Low Stock Report lists items at/below min level, filterable by location/tags, exportable; dashboard surfaces low-stock items.
- **No purchasing, costing, or formal count machinery observed.** No purchase-order, COGS, or count-session feature appeared in any fetched page; quantity changes happen through direct updates and folder moves; "Inventory Count Adjustment" exists as a move reason (the count happens in the real world; the correction is recorded). QuickBooks Online integration exists (help nav) but no COGS machinery was observed.
- **Roles and audit.** User access control (owners/admins/members, custom roles, limited-access role on Enterprise); activity/user histories; reports exportable CSV/PDF, schedulable.
- **Identification.** Sortly IDs (SID), QR/barcode label generation and printing, third-party barcode support, handheld scanners, offline mobile mode.
- Plan tiers Free → Enterprise; API on Enterprise; AI-powered bulk import (era-current).

## Product B — inFlow Inventory (Learning Center)

Evidence layer: A (direct observation, official help articles).

Key observations:

- **Products + locations + quantities.** Products with variants (sizes/colors), SKUs/barcodes (GS1 support, barcode shop), categories, images, cost/price/markup, product types (stocked vs service), units of measure (buy unit ≠ sell unit). Locations with sublocations (aisles, bins); stock transfers between locations.
- **Quantity model is explicit and multi-layer.** Named article "What is quantity reserved, on hand, available, etc?": on-hand (physically present minus picked), reserved (committed to open orders; includes expiring lot quantities), available (on-hand − reserved; negative available = not enough stock for open orders), unreserved, picked, committed, buildable (BOM), on order. Reorder logic formula: on-hand − reserved + on-order.
- **Purchase side.** Purchase orders (create/complete, partial receive, receiving one PO to multiple locations, PO approvals, backorder POs, dropship, returns to vendor, vendor product codes, lead times, tariffs/fees); starting stock via POs; vendors with product codes/currencies.
- **Sales side.** Sales orders fulfill and decrement stock; picking allocations; retail mode (POS-flavored); damaged-goods tracking; returns/credits.
- **Stock counts are formal.** Per location; count sheets — single sheet or split across team members with per-sheet status and assignment; "In review" status for double-checking; Finalize count; products can be added mid-count; the count produces stock adjustments; cancel/copy/print/email a count.
- **Adjustments and history.** Direct stock-level adjustment; reset stock levels; import stock levels/serials; per-product movement/transaction history; historical inventory report (quantity at a past date); "movement history inaccurate" troubleshooting exists — the history is a first-class, correctable record.
- **Replenishment.** Reorder points per product, low-stock email notifications, reorder suggestions from a vendor, recommended reorder point (inFlow suggests one).
- **Cost layer.** Product cost/COGS calculation article; cost/price/markup entry; inventory valuation and historical inventory reports.
- **Depth.** Serial numbers, lot numbers + expiry dates; bundles, bills of materials, manufacture orders, disassembly; consignment; asset-tracking and rental use cases; negative-inventory warnings ("why you should avoid negative inventory").
- **Integration.** QuickBooks Online/Xero (accounting), Shopify/WooCommerce/Amazon/Square (channels), shipping (EasyPost), API, Zapier.
- **Companion product.** inFlow Stockroom — a separate scan-first add-on ("quickly scan products in and out") with its own locations, labels, devices; plus hardware (smart scanner, portable label printer).
- Dashboard + report suite; PO approvals as governance.

## Product C — Zoho Inventory (User Guide)

Evidence layer: A (direct observation, official user guide).

Key observations:

- **Items + warehouses.** Items (inventory-tracked vs non-tracked), composite items, assemblies/bundles, item categories, price lists, QR/barcode generation. Multi-warehouse with locations and bin locations; transfer orders between warehouses.
- **Stock counts are formal and governed.** Warehouse-scoped; assigned to a user; counted on the mobile app (scan for batch/serial-tracked items); statuses: Yet To Start → Counting in Progress → Pending Approval → Completed / Cancelled; approval on the web with per-item Matched/Unmatched; unmatched items take an adjustment reason (default "Stock taking results", customizable) and post a quantity adjustment to a chosen account (default COGS); approvers can see suspected transactions that occurred during the count (variation badge); recurring/scheduled counts with reminders; plan-gated (Premium/Enterprise or Advanced Warehouse Operations add-on); requires multi-warehouse enabled.
- **Inventory adjustments are reason-coded documents.** Quantity Adjustment: reasons such as theft, damaged goods, data entry error, write-off, donation; custom reason list manageable (add/deactivate; used reasons cannot be deleted); GL account selection per adjustment; cost price captured; draft → convert to adjusted; serial/batch-aware adjustments. Value Adjustment: revaluation of item value (supply/demand-driven cost changes). Adjustments viewable per item and searchable by type/reason/date.
- **Purchase side.** Purchase orders, purchase receives, bills, vendor credits, purchase returns, dropshipment.
- **Sales side is heavy.** Sales orders, packages, shipments, picklists, invoices, payments received, sales returns, backorders — the order-fulfillment cycle is a first-class half of the product (the OMS seam).
- **Replenishment.** Replenishments module; low-stock notifications.
- **Depth.** Batch/serial tracking with batch price management; stock allocation setting; approval workflows; record locking; users & roles.
- **Reports.** Inventory, advanced inventory, valuation, warehouse, activity reports.
- **Integration.** QuickBooks/Xero/Zoho Books, Shopify/Amazon/WooCommerce/marketplaces, shipping carriers, online payments, Zoho ecosystem.

## Cross-product Comparison

| Structure | Sortly | inFlow | Zoho Inventory | Square/Erply/NetSuite/Cin7 (sibling pass) | Layer |
|---|---|---|---|---|---|
| Item-level stock records at named locations | ✓ (items × folders-as-locations) | ✓ (products × locations/sublocations) | ✓ (items × warehouses) | ✓ all four | B |
| Recorded movements (dated, attributable) | ✓ (transactions + activity history + quantity-on-date) | ✓ (movement history; orders/adjustments/transfers) | ✓ (transactions; adjustments; receives; shipments) | ✓ all four | B |
| Count reconciliation | ✓ as reason-coded "Inventory Count Adjustment" (no formal count session observed) | ✓ formal (count sheets → review → finalize → adjustments) | ✓ formal (statuses, approval, matched/unmatched, reason) | ✓ all four formal | B (form varies) |
| Replenishment machinery | ✓ (min-level alerts + low-stock report) | ✓ (reorder points + suggestions + notifications) | ✓ (replenishments + notifications) | ✓ all four | B |
| Purchasing side (vendors, POs, receiving) | not observed | ✓ | ✓ | ✓ all four | B (absent at light pole) |
| Cost/COGS/valuation | price only; no COGS observed | ✓ | ✓ (FIFO lots; value adjustment) | ✓ all four | B (absent at light pole) |
| Reason-coded adjustments | ✓ (move reasons incl. Sold/Damaged/Donation/Count Adjustment) | ✓ (damaged goods; adjustments) | ✓ (customizable reason list) | ✓ | B |
| Transfers between locations | ✓ (folder moves) | ✓ | ✓ (transfer orders) | ✓ | B |
| Sales linkage decrements stock | manual ("Sold" reason; no POS integration observed) | ✓ (sales orders; Square/Shopify sync) | ✓ (sales orders/channels) | ✓ | B (mechanism varies) |
| Permissions / roles / attribution | ✓ | ✓ (+ PO approvals) | ✓ (+ approval workflows, record locking) | ✓ | B |
| Reporting on stock | ✓ | ✓ (incl. historical inventory) | ✓ (incl. valuation) | ✓ | B |
| Barcode/SKU identification + labels | ✓ (QR/barcode labels, scanners) | ✓ (GS1, label printers) | ✓ (QR/barcode generation) | ✓ | B |
| Multi-location as first-class | ✓ (folders) | ✓ | ✓ (warehouses) | ✓ | B |
| Order-allocation depth (reserved/available/on-order) | ✗ | ✓ | ✓ (stock allocation) | NetSuite/Cin7 ✓ | C-variant |
| Serial/lot/batch tracking | ✓ (unique items) | ✓ (serials, lots + expiry) | ✓ (batches, serials, batch pricing) | Erply batches; NetSuite/Cin7 ✓ | C-variant |
| Bins / sublocations | sub-folders | ✓ (aisles/bins) | ✓ (bin locations) | NetSuite/Cin7 ✓ | C-variant |
| BOM / bundles / manufacturing | ✗ (BOM FAQ: not supported) | ✓ | ✓ (composites, assemblies) | Cin7/NetSuite ✓ | C-variant |
| Accounting integration | QuickBooks integration (nav only; no COGS observed) | ✓ (QBO/Xero) | ✓ (QBO/Xero/Zoho Books) | ✓ | B (depth varies) |
| Formal count session absent | ✓ (this product) | — | — | — | product-specific (light pole) |
| Purchase orders absent | ✓ (this product) | — | — | — | product-specific (light pole) |
| Visual/photo-first item identity | ✓ (photos as first-class) | ✓ (images) | — | — | C-variant |
| Scan-first companion app | — | ✓ (inFlow Stockroom add-on) | ✓ (mobile counting) | — | C-variant |
| Chain/HQ central purchasing & distribution | — | — | — | Erply ✓ (sibling pass) | C-variant (chain pole) |

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which a store inventory application stops being recognizable:

1. **Item-level stock records at the store's locations** — for each sellable/usable item, a quantity on hand per location (sales floor, stockroom, back room). The system of record for "how much we have, where."
2. **Recorded stock movements** — dated, attributable events that change on-hand: goods in, goods out (sold, consumed, given out), corrections, movements between locations. On-hand is never edited in a vacuum.
3. **Count reconciliation** — the record is re-anchored to physical reality: a recorded count compared against the record with the difference written back. In mature products this is a formal count session with review/approval; in the lightest products it collapses into a reason-coded correction ("Inventory Count Adjustment") — the reconciliation act survives even where the session does not.

Historical check (§24): a paper stock ledger/bin card updated from invoices and sales slips, with a periodic shelf count and correction, satisfies all three properties — no cloud, no scanner, no POS integration, no purchase orders in the core. PLU-based stock tracking in electronic cash registers satisfies it. Sortly-class light apps satisfy it (records + transactions + count-adjustment reason). L0 holds.

Deliberately NOT in L0 (tested against the sample): purchase orders/purchasing (absent at the light pole), cost/COGS machinery (absent at the light pole), formal count sessions (absent at the light pole; the reconciliation act is the invariant, the session is its mature form), replenishment alerts, POS integration as a mechanism (historically stock-out was posted by hand), permissions, barcode identification, multi-store/chain machinery.

### L1 — Common Mature Structure

Present across the researched sample (Layer B):

- **Replenishment machinery** — low-stock thresholds/alerts (universal in sample), reorder points and reorder suggestions (common), notifications.
- **Purchasing side** — vendors, purchase orders, receiving (full/partial) — present wherever purchasing matters; absent only at the lightest pole.
- **Transfers between locations** — folder moves, transfers, or transfer orders.
- **Cost and value layer** — unit costs, COGS, inventory valuation (absent only at the lightest pole).
- **Reason-coded adjustments** — damage, theft, loss, expiry, donation, recount; the shrinkage-visibility mechanism.
- **Count discipline** — count sessions with assignment, review, and approval before adjustments post (formal in mature products).
- **Permissions and attribution** — roles gating stock actions; user attribution on transactions; audit/activity history.
- **Reporting** — stock levels, movements, low stock, valuation; exportable.
- **Identification** — SKU/barcode/QR; scanning as the dominant data-entry mode; label printing.
- **Sales-channel linkage** — selling decrements stock automatically (via POS, sales orders, or channel sync); manual "Sold" posting at the light pole.

### L2 — Variant / Optional Structure

- **Scope posture** — single store ↔ small chain ↔ multichannel hub (stores + warehouses + e-commerce channels). The store-vs-chain axis is the flagged joint-review seam (see Boundary Findings).
- **Depth posture** — light pole (records + movements + alerts; no POs/COGS/formal counts) ↔ full ledger pole (POs, counts, COGS) ↔ order-heavy pole (sales orders, pick/pack/ship, invoices).
- **Order-allocation depth** — on-hand vs reserved vs available vs on-order; committing stock to open orders.
- **Warehouse depth** — bins, serial/lot tracking, batch pricing.
- **BOM/bundle/manufacturing** — assemblies, kits, manufacture orders.
- **Visual/scan-first interaction** — photo-first item identity, QR labels, scan-driven check-in/check-out, dedicated companion apps.
- **Unit handling** — buy-vs-sell units, partial quantities, weighed goods.
- **Count strictness** — location locking, effective dating, recurring/scheduled counts, per-item matched/unmatched approval.
- **Forecasting/AI** — demand forecasting, automated reordering, AI bulk import (era-current).
- **Accounting integration depth** — native GL ↔ journal sync ↔ export.
- **Commercial packaging** — plan-tiered capabilities (alerts, counts, API gated by tier in sampled products).

### L3 — Vendor-specific (research notes only)

- Sortly: move-reason list (Consumed…Sold); Sortly IDs (SID); folders-as-locations with sub-folder check-out patterns; Quick Actions scan workflows; Return to Origin; Sortly Labs; AI-powered bulk import; plan tiers Free/Advanced/Premium/Ultra/Enterprise; API on Enterprise; notes/reasons cannot be made mandatory.
- inFlow: quantity-breakdown vocabulary (on-hand/reserved/available/unreserved/picked/committed/buildable/on-order); reorder formula (on-hand − reserved + on-order); count sheets split across team members with per-sheet status; "In review" → Finalize; inFlow Stockroom scan-first add-on; Smart Scanner hardware; Showroom B2B portal; retail mode (Windows); recommended reorder point; GS1 barcode shop.
- Zoho Inventory: stock-count statuses (Yet To Start/Counting in Progress/Pending Approval/Completed/Cancelled); default adjustment reason "Stock taking results" posting to COGS account; variation badge showing suspected transactions during count; recurring counts with reminders; plan gating (Premium/Enterprise or Warehouse add-on); multi-warehouse prerequisite; organization model; value adjustments; batch price management.

## Vendor-specific Findings

(See L3; none promoted to the canonical model.)

## Rejected Findings

- "Store Inventory Application is a different Type from Retail Inventory Management" — rejected on the joint-review evidence: the store-scoped sample (Sortly/inFlow/Zoho) carries the same three-part core (records at locations, movements, count reconciliation) as the sibling pass's sample (Square/Erply/NetSuite/Cin7). The differences are scope (single location vs chain/HQ) and depth (light vs full ledger), not structure.
- "A store inventory app is just a stock list" — rejected: the movement record and count reconciliation are present in every sampled product, including the lightest (Sortly's transactions, activity history, and count-adjustment reason). A bare stock list without movements/history would not be this Type.
- "Purchase orders are definitional" — rejected: Sortly operates without them (alerts + manual reordering); purchasing is common mature structure, not the definition.
- "Formal count sessions are definitional" — rejected as stated: the *reconciliation* is definitional; the formal session is its mature implementation (Sortly reconciles through a reason-coded correction without a session feature).
- "Store inventory = asset/equipment tracking" — rejected as the definition: Sortly carries a supplies/equipment flavor (its retail use is one industry among many), but the store-inventory referent centers merchandise stock with sell/consume/replenish semantics; the asset flavor is a use-case variant and a boundary note toward generic IMS/asset tracking.
- "POS integration is definitional" — rejected: Sortly posts sales manually; historical stores ran stock ledgers by hand. Linkage mechanism is variant.

## Boundary Findings

1. **vs Retail Inventory Management (§05.12 sibling, processed) — JOINT REVIEW RESOLVED FROM THIS SIDE.** The flagged question was whether the two leaves are one Type at two scopes or two Types. Evidence from this pass: the store-scoped products carry the identical three-part core; no structural difference was found. The seam is **scope + depth**: this leaf's market referent is the store-scoped pole — the single location's stock operations (shelf, stockroom, receiving door, counts, reorder alerts) as the working center, with the light small-business pole as its most common realization; the sibling leaf documents the same machinery with the full chain/HQ span (central purchasing, distribution, cross-store transfers) as part of its scope posture. **Recommendation: keep-both with a store-vs-chain scope seam** — the two documents are readable as scope-slices over one machinery; consolidation as one Type with scope variants is the defensible alternative if the directory is ever revised. This document is written as the store-scoped pole and cross-references the sibling.
2. **vs Retail POS (§05.10, processed)** — the POS executes sales and decrements stock as a side effect; this Type owns the stock record, receiving, counts, and reorder. Remove the stock ledger from a POS and it is still a POS; remove selling from this Type and it is still store inventory. Consistent with the processed Retail POS document's own boundary statement.
3. **vs Retail Store Management System (§05.11, processed)** — confirms the same-substrate note from this side: the store's stock domain is one slice of the store record base. The store-management pass centers the store as an operating unit (offering, customers, staff, cash, performance); this pass centers the stock domain. The same back-office products realize both; the two documents are span-slices over shared machinery.
4. **vs generic Inventory Management System (§10)** — same machinery, different domain instantiation. The store instantiation: items are merchandise/supplies for a selling location, stock-out is dominated by sales, replenishment serves the shelf, shrinkage reasons appear. Sortly sits nearest this seam (supplies/equipment flavor, industry-generic marketing) but its store-shaped structure (locations, sold/consumed/replenish reasons, low-stock reorder loop) keeps it in-family; a purely asset-tracking deployment would drift toward asset tracking.
5. **vs WMS (§10)** — warehouse handling depth (bins, picking, putaway) is the blur zone; Zoho/inFlow carry bin/serial depth as extensions. When physical handling becomes the center, the product drifts to WMS.
6. **vs Order Management System (§05.07)** — Zoho Inventory and inFlow show the seam: when customer-order orchestration (sales orders, pick/pack/ship, invoices, backorders) becomes the center and stock is the constraint feeding it, the product is drifting toward OMS. The store-inventory center is the stock record, not the order pipeline.
7. **vs PIM (§05.04)** — PIM owns product data; this Type owns quantities. Item records here reference products (name, SKU, photo) but do not manage catalog data.
8. **vs Merchandising / Assortment Planning (§05.13)** — planning decides what to carry; this Type records and maintains what is actually there. Reorder suggestions touch planning but the record-keeping spine is here.

## Uncertainties

- Boxstorm (retail-specific free-tier inventory) could not be fetched (transport error ×2); the retail-specific free pole is therefore not directly sampled. Its expected structure (stock + counts + POs at retail flavor) is inferred from category positioning only and was not used as evidence.
- Sortly's formal-count capability: no count-session feature was observed in any fetched page; this is evidence-of-absence in documentation, not proof the feature does not exist. The light-pole characterization is calibrated to this limitation.
- Sortly's retail depth (POS integration, sales-channel sync) was not observed; its QuickBooks integration was seen in navigation only. Claims about Sortly's accounting linkage are kept weak.
- inFlow's Windows-app count flow was not fetched (web app used); minor interface differences between Windows/web/mobile clients are unverified.
- Whether market usage of "store inventory application" ever refers to a store's fixture/equipment inventory (rather than merchandise stock) was not resolved; the supplies/asset flavor exists in Sortly and is recorded as a use-case variant and boundary note.
- The exact plan-tier gating of features differs per product and changes over time; tier facts are kept in these notes only, not in the final document.

## Final Synthesis

A Store Inventory Application is the store-scoped stock system of record: it holds item-level stock records at the store's locations (sales floor, stockroom), changes them only through recorded movements (goods in, goods out, corrections, moves), re-anchors the record to physical reality through counts (formal sessions in mature products; reason-coded corrections at the light pole), and turns the record into stocking action through low-stock alerts and reordering. Mature products wrap this spine with purchasing (vendors, POs, receiving), cost/valuation, permissions and audit, reporting, barcode identification, and sales linkage; the small-business pole runs the same spine lighter (no POs, no COGS, informal counts), and the order-heavy pole extends it toward order management. The joint review with Retail Inventory Management resolves as: same machinery, two scopes — keep-both with a store-vs-chain scope seam, this leaf documenting the store-scoped pole.
