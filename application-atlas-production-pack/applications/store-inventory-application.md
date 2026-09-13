# Store Inventory Application

## Overview

A **Store Inventory Application** is the store-scoped stock system of record: it holds item-level stock records for what a single location has on hand — on the sales floor and in the stockroom — changes those quantities only through recorded movements, reconciles the record against physical reality through counts, and turns the record into stocking action through low-stock alerts and reordering.

Its purpose is to answer, at any moment and trustworthily: *what do we have, where in the store, what happened to it, and what should we reorder.* The point of sale sells from this record; this application owns it.

Canonical boundary: a Store Inventory Application is not the selling surface (Retail POS), not the headquarters-level purchasing and distribution machinery that coordinates stock across a chain, not the warehouse's physical-handling system (WMS), not the product-data catalog (PIM), and not the customer-order pipeline (Order Management) — even though many products bundle adjacent pieces of these.

## Users & Context

**Primary users** — the people accountable for the store's stock being right:

- **Store owner / store manager**: oversees the stock record, approves counts and adjustments, decides what to reorder.
- **Stockroom / inventory clerk**: receives deliveries, puts stock away, performs counts with a scanner, records damaged or missing goods.

**Secondary users**:

- **Counter / sales staff**: sell from the record (directly at a register or by recording goods given out); they decrement stock but do not own it.
- **Bookkeeper / accountant** (in some businesses): read stock valuation and adjustment records.

The work context is back-of-store and on-the-floor: a web or desktop dashboard for the manager, plus phones, tablets, and handheld barcode scanners in the stockroom and on the shelf during receiving and counting. The rhythm is operational — deliveries arrive, goods sell or get used, counts happen on a schedule, reorders go out — rather than transactional at a counter.

## Core Model

### The Defining Core

```text
Item (merchandise or supplies, with variations such as size/color)
└── Stock record: quantity on hand, per location (sales floor, stockroom)
    └── changed only by recorded Movements
        ├── in:      receiving (from purchases, or direct registration)
        ├── out:     sales, consumption, give-outs, write-offs with reasons
        ├── between: moves and transfers (shelf ↔ stockroom, location ↔ location)
        └── correct: reason-coded adjustments
    └── reconciled by Counts
        (count actual → compare to record → write the difference back)
```

Three properties. If any one is removed, the product is no longer recognizable as store inventory management:

- **Item-level stock records at the store's locations** — for each item, the system holds a quantity on hand per location. This is the system of record for "how much we have, where." Without it, there is nothing to manage.
- **Recorded stock movements** — on-hand quantity is never edited in a vacuum; it changes through dated, attributable events: goods received in, goods sold or used out, stock moved between places, corrections. The movement history is what makes the record auditable and the shrinkage visible. Without movements, the record is a guess.
- **Count reconciliation** — the record is re-anchored to physical reality: a recorded count of what is actually there, compared against the record, with the difference written back. In mature products this is a formal count session with review and approval; in the lightest products it collapses into a reason-coded correction. Without any reconciliation, the record drifts away from reality with no way to recover.

### Standard Capabilities

Mature products commonly add these. They make the record actionable; they are not what makes the product a store inventory application.

- **Replenishment machinery** — low-stock thresholds and alerts per item (often per location), low-stock reports, and — in fuller products — reorder points, reorder suggestions, and purchase-order generation from them. Universal in the researched sample; the practical payoff of keeping the record.
- **Purchasing side** — vendors/suppliers, purchase orders (vendor, delivery location, expected date, item lines with quantities and unit costs), and receiving in full or partially. Present wherever purchasing matters; the lightest products operate on alerts and manual reordering alone.
- **Transfers and moves** — moving stock between places: shelf to stockroom, store to store, or — in visual, mobile-first products — between folders that represent locations or states (available, out to a job, rented out).
- **Cost and value layer** — unit costs captured at receiving, cost of goods sold, inventory valuation. Absent only at the lightest pole, where items carry a price but not a tracked cost.
- **Adjustment reasons** — damage, theft, loss, expiry, donation, recount, sold, consumed. Reason-coded corrections are the mechanism that turns stock loss from a silent number into manageable information.
- **Count discipline** — count sessions with assignment, review, and approval before adjustments take effect; full counts and partial/cycle counts; variance visibility.
- **Permissions and attribution** — stock actions gated by role; movements and adjustments attributed to the user who performed them; activity history.
- **Reporting** — stock levels, movements in and out, low stock, variance, and valuation reports; exportable for bookkeeping.
- **Identification** — SKUs, barcodes, QR codes; scanning as the dominant data-entry mode; label printing.
- **Sales linkage** — selling (at a register, through sales orders, or on e-commerce channels) decrements stock automatically; at the lightest pole, sales are posted by hand with a "sold" reason.

### One Structure, Many Implementations

The core model is conceptual. Implementations vary, and none of them is the definition:

```text
Concept:   Stock record            Implementations: per-variation quantities, per-location
                                   quantities, folder-held quantities (visual apps)
Concept:   Location                Implementations: named store locations, stockrooms,
                                   warehouses, folders organized by place or state
Concept:   Movement                Implementations: receiving documents, sales postings,
                                   folder moves with reasons, adjustment forms,
                                   check-in/check-out workflows
Concept:   Count                   Implementations: count sessions with approval,
                                   count sheets split across staff, scanner-driven
                                   counting, reason-coded corrections
Concept:   Replenishment trigger   Implementations: min-level alerts, low-stock reports,
                                   reorder points, reorder suggestions
```

A reader who has only seen a small shop's photo-and-folder stock app should still recognize a scanner-driven back office with purchase orders and count sessions as the same Type from the defining core.

## How It Works

### Set up the record

Items are defined (or imported) with their variations, SKUs or barcodes, and stock tracking enabled; locations are defined (sales floor, stockroom, back room). Initial quantities are entered by count or by receiving. From then on, the record lives by movements.

### The receiving loop (stock comes in)

```text
Delivery arrives            expected against a purchase order, or unannounced
→ Receive                   full or partial, line by line or scan-driven
→ Stock lands               on-hand rises at the receiving location;
                            unit cost captured where costing is tracked;
                            damaged or missing quantities recorded with reasons
```

In products without purchase orders, receiving is a direct stock addition — still a recorded movement, just without the purchasing paperwork.

### The selling linkage (stock goes out)

Sales at the register, sales-order fulfillments, e-commerce orders, and — in stores that use the app directly — goods handed out or consumed all decrement on-hand. The inventory application does not execute the sale; it records the stock consequence. This linkage is what keeps the record current between counts. Where no selling system is connected, staff post goods-out by hand with a reason.

### The correction loop (record meets reality)

```text
Discover a discrepancy    (damaged unit, missing unit, miscount, expired goods)
→ Record a correction     with a reason: damage / theft / loss / expiry / recount / donation
→ On-hand changes         the reason and the user are kept on the record
```

Reason-coded corrections accumulate into the shrinkage picture that the owner and the bookkeeper read.

### The count cycle (the record is re-anchored)

```text
Schedule a count          full count (everything) or partial/cycle count (a subset)
→ Count                   scan or key in actual quantities, often across several devices
→ Review                  compare counted vs recorded; variances by quantity (and by
                          cost where costing is tracked); recount lines as needed
→ Approve / finalize      the count takes effect: the record is adjusted to match reality
```

Products differ in strictness: some assign count sheets to individual staff and track progress per sheet, some lock the location against stock changes while the count runs, some let approvers see which transactions occurred during the count, and some treat an approved full count as a complete accounting. The cycle repeats — full counts periodically, cycle counts continuously — so the record never drifts far.

### The replenishment loop (the record drives buying)

```text
Stock falls               through sales, use, write-offs
→ Threshold crossed       low-stock alert fires, or item hits its reorder point
→ Replenishment action    reorder suggestion accepted, purchase order raised
                          to the vendor — or a manual order placed
→ back to receiving
```

### Core vs Common vs Optional

**Defining core** — without these, not store inventory:

- item-level stock records at the store's locations
- recorded stock movements (in / out / between / corrections)
- count reconciliation

**Standard capabilities** — present in most mature products:

- replenishment machinery, purchasing side (vendors, POs, receiving), transfers and moves, cost/valuation, reason-coded adjustments, count discipline with approval, permissions and audit, reporting, barcode identification, sales linkage

**Variant / optional** — depends on segment, scale, and deployment:

- purchase-order depth, order-allocation depth (on-hand vs reserved vs available), warehouse depth (bins, serial/lot tracking), unit conversions (case ↔ unit, weighed goods), bundles/assemblies, forecasting and automated reordering, accounting integration depth, plan-tiered packaging, photo-first and scan-first interaction styles

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Stock overview

The manager's primary surface.

- on-hand quantities by item and variation, per location; filterable by location, category, stock status; in visual products, items appear as photo cards organized in folders
- primary actions: adjust stock, receive stock, move stock, set a low-stock alert, print labels, export

### Receiving surface

Where deliveries become stock.

- open purchase orders with expected deliveries (where purchasing is tracked); line-by-line or scan-driven receiving; unit cost and cost-change indicators
- primary actions: receive in full / partially, record damaged or missing quantities

### Count surface (often on handheld devices)

Where the record is re-anchored.

- count sessions (full / partial) with progress state and, in fuller products, per-staff count sheets; scan-driven or keyed quantity entry; counted-vs-recorded comparison with variances
- primary actions: start count, enter/scan quantities, submit for review, override a line, approve/finalize the count

### Adjustment / correction surface

- reason-coded stock corrections, individually or in bulk; history of corrections with user attribution

### Reorder / purchasing surface

- low-stock lists and alerts; reorder suggestions; purchase-order list and detail (vendor, delivery location, expected date, lines) where purchasing is tracked
- primary actions: create order, send to vendor, receive, cancel

### Reports

- stock levels, movements in/out, low stock, variance, valuation; exportable for bookkeeping

### Settings

- locations, units of measure, adjustment reasons, alert thresholds and reorder parameters, user roles and permissions

## Important Rules / Behaviors

### On-hand changes only through movements

The stock quantity is not a free-editable field; it moves because something happened — a receipt, a sale, a move, a reason-coded correction, or an approved count. This discipline is what makes the movement history an audit trail and the record trustworthy. Even the lightest sampled products follow it: every quantity change is a recorded transaction with an optional reason, visible in an activity history.

### Counts take effect on approval, not on counting

A count session is a draft until it is reviewed and approved/finalized; only then do adjustments post. Some products lock the location while counting, surface transactions that happened mid-count, or treat an approved full count as a complete accounting. Exact strictness is product-dependent.

### Adjustments carry reasons, and reasons carry meaning

Damage, theft, loss, expiry, donation, recount — the reason on a correction is what turns stock loss from a silent number into manageable information (shrinkage by cause, by location, by item).

### Negative stock is a visible anomaly

Products surface negative on-hand quantities as a reportable, correctable state — or warn against it — rather than silently clamping to zero. A negative quantity is a signal that movements and records have diverged.

### Permissions match money and trust

Stock actions are permission-gated (receive, adjust, write off, approve counts) and attributed to users, because the stock record underpins both the shrinkage picture and — where costing is tracked — the financial valuation.

### The light pole trades depth for simplicity, not structure

Small-store products may omit purchase orders, costing, and formal count sessions. What they do not omit is the spine: records at locations, recorded movements, and a way to reconcile the record with reality. A product without that spine is a stock list or an asset register, not store inventory management.

## Variants

- **Light / visual pole** — photo-first item cards organized in folders-as-locations, scan-driven check-in/check-out, min-level alerts and low-stock reports; no purchase orders, no costing, no formal count sessions. The small-store and supplies-tracking realization.
- **Full ledger pole** — the complete spine at small-business scale: purchase orders with receiving, formal count sessions with approval, cost of goods sold, reorder points and suggestions, accounting sync.
- **Order-heavy pole** — the same stock spine wrapped in a sales-order/purchase-order cycle (pick, pack, ship, invoices, backorders); stock serves the order pipeline. The seam toward order management.
- **POS-integrated** — inventory as the back-office half of a point-of-sale product; sales decrement stock automatically and the stock record feeds availability back to the register.
- **Single store vs small chain** — one location's stock operations vs a few locations with transfers between them; headquarters-level central purchasing and distribution belongs to the broader retail inventory management span.
- **Vertical tuning** — grocery (weighed goods, case quantities), fashion (size/color matrices), supplies and equipment (check-out to jobs, rentals), food service (ingredient-level stock as an adjacent module).
- **Companion apps** — dedicated scan-first mobile companions for counting and check-in/check-out, sharing the same record.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Retail Inventory Management | same machinery, broader span | the closest neighbor. Both Types hold item-level stock records, movements, counts, and replenishment. The seam is scope: this Type centers a single store's stock operations (shelf, stockroom, receiving door); Retail Inventory Management spans the whole retail business including headquarters-level central purchasing, distribution, and cross-store transfers. The two documents are readable as scope-slices over one machinery |
| Retail POS | transaction-side sibling | the POS executes sales and decrements stock as a side effect; this Type owns the stock record, receiving, counts, and reorder. Remove the stock ledger from a POS and it is still a POS; remove selling from this Type and it is still store inventory |
| Retail Store Management System | same substrate, different center | the store management system centers the store as an operating unit (offering, prices, customers, staff, cash, performance), of which stock is one managed domain; this Type centers the stock domain itself. The same back-office products often realize both |
| Inventory Management System (generic) | domain sibling | the same machinery applied to any stock-holding operation (materials, assets, equipment); the store instantiation anchors it to merchandise, a selling location, sales-driven stock-out, and shrinkage. Supplies/equipment-flavored deployments drift toward the generic Type and asset tracking |
| Warehouse Management System (WMS) | adjacent, deeper on handling | WMS manages how stock is physically handled inside a warehouse (bins, picking, putaway); this Type manages what/how much exists and how it changes. Bin/serial depth is the blur zone |
| Product Information Management (PIM) | data-side neighbor | PIM owns product data (descriptions, images, attributes); this Type owns quantities. A stock record references a product; it does not describe it |
| Order Management System | downstream consumer | orchestrates customer orders to fulfillment; draws on this Type's stock. When order orchestration becomes the center, the product is drifting toward OMS |
| Merchandising / Assortment Planning | planning-side neighbor | decides what to carry and how to present it (forward-looking); this Type records and maintains what is actually there (operational truth) |

The most important boundary is with **Retail Inventory Management**: the two Types share the item catalog, the stock numbers, and the entire stock spine. The structural difference is none — the difference is scope and depth. This document describes the store-scoped pole; the sibling document describes the same machinery across the full retail span.

## Representative Products

- **Sortly** — visual, mobile-first inventory app: items as photo cards in folders-as-locations, scan-driven check-in/check-out, min-level alerts and low-stock reports; the light pole
- **inFlow Inventory** — small-business inventory software with the full spine: purchase orders and receiving, count sheets with review and finalize, adjustments, transfers, reorder points and suggestions, cost of goods sold
- **Zoho Inventory** — order-heavy small-business inventory: warehouses, governed stock counts with approval, reason-coded adjustments, purchase and sales order machinery, replenishments

The defining core was additionally checked against the processed sibling pass's sample (a POS-integrated retail mode, a chain back office, an ERP inventory module, and a multichannel inventory platform) and against older, non-cloud patterns (paper stock ledgers with count sheets, register-based stock tracking) to avoid over-fitting the definition to the current cloud/SaaS era.

## Sources

Research date: **2026-09-08**

- Sortly Help Center — "Sortly Product Overview"; "Quantity Alerts"; "Low Stock Report"; "How to Update Your Inventory"; "Getting started"; "FAQs" — https://help.sortly.com/ (product page: https://www.sortly.com/)
- inFlow Inventory Learning Center — "Managing products" section; "What is quantity reserved, on hand, available, etc?"; "How to create and complete a stock count (Web)" — https://www.inflowinventory.com/support/
- Zoho Inventory User Guide — "Stock Counts"; "Inventory Adjustments"; help index — https://www.zoho.com/inventory/help/

> Sourcing limitations: Boxstorm (retail-specific inventory) could not be reached (repeated transport errors) and is not sampled. No formal count-session feature was observed in Sortly's documentation; the light-pole characterization rests on that documented absence. Precise vendor facts (plan-tier gating, exact reason lists, quantity-model vocabulary) are kept in the paired Research Notes only.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the joint-review resolution with Retail Inventory Management are recorded in the paired Research Notes.
