# Retail Inventory Management

## Overview

A **Retail Inventory Management** application is the back-office stock system of record for a retail business: it holds item-level stock records for merchandise at named locations (stores, stockrooms, warehouses), changes those quantities only through recorded stock movements, reconciles the records against physical reality through counts, and turns the record into stocking action through replenishment.

Its purpose is to answer, at any moment and trustworthily: *what do we have, where, what happened to it, and what should we buy or move next.* The point-of-sale sells from this record; this application owns it.

Canonical boundary: a Retail Inventory Management application is not the selling surface (Retail POS), not the warehouse's physical-handling system (WMS), not the planning layer that decides what a retailer should carry (Merchandising), not the product-data catalog (PIM), and not the customer-order pipeline (Order Management) — even though modern products increasingly bundle adjacent pieces of all of these.

## Users & Context

**Primary users** — the people accountable for stock being right:

- **Store manager / inventory controller**: oversees the location's stock record, approves counts and adjustments, decides replenishment.
- **Stockroom / inventory clerk**: receives deliveries, puts stock away, performs counts with a scanner, records damaged or missing goods.

**Secondary users**:

- **Buyer / merchandiser / HQ inventory manager** (in chain and multichannel operations): works the aggregate picture — what to reorder from vendors, how to distribute stock across stores and channels.
- **Loss-prevention / finance roles**: read shrinkage-relevant adjustment records (damage, theft, loss) and inventory valuation.

The work context is back-office and back-of-store: a web dashboard for managers and HQ, plus handheld devices with barcode scanners on the stockroom floor and the sales floor during counts and receiving. The rhythm is operational — deliveries arrive, goods sell, counts happen on a schedule, reorders go out — rather than transactional at a counter.

## Core Model

### The Defining Core

```text
Item (merchandise, with variations such as size/color)
└── Stock record: quantity on hand, per location
    └── changed only by recorded Stock Movements
        ├── in:      receiving (from purchase orders, or direct registration)
        ├── out:     sales (POS / orders), write-offs with reasons
        ├── between: transfers (store ↔ store, store ↔ warehouse)
        └── correct: adjustments (reason-coded)
    └── reconciled by Physical Counts
        (count actual → compare to record → adjust the record)
```

Three properties. If any one is removed, the product is no longer recognizable as inventory management:

- **Item-level stock records at named locations** — for each sellable item and its variations, the system holds a quantity on hand per location. This is the system of record for "how much we have, where." Without it, there is nothing to manage.
- **Recorded stock movements** — on-hand quantity is never edited in a vacuum; it changes through dated, attributable events: goods received in, goods sold or written off out, stock moved between locations, corrections. The movement history is what makes the record auditable and the shrinkage visible. Without movements, the record is a guess.
- **Physical count reconciliation** — a recorded count of what is actually on the shelf, compared against the record, with the difference written back as adjustments. Without counts, the record drifts away from reality with no way to recover.

### Standard Capabilities

Mature products commonly add these. They make the record actionable; they are not what makes the product an inventory manager.

- **Replenishment machinery** — low-stock thresholds and alerts, reorder points and preferred stock levels per item per location, reorder suggestions, and purchase-order generation from them. Universal in the researched sample; the practical payoff of keeping the record.
- **Purchasing side** — vendors/suppliers, purchase orders (vendor, delivery location, expected date, item lines with quantities and unit costs), receiving in full or partially, and supplier signals such as late-delivery reports.
- **Transfers between locations** — moving stock between stores or between store and warehouse, either as direct transfers or as order-shaped transfer documents that schedule and track the movement.
- **Cost and value layer** — unit costs captured at receiving, cost of goods sold, inventory valuation, and costing methods (FIFO with batch tracking is a common pattern); revaluation when costs change.
- **Adjustment reasons** — damage, theft, loss, expiry, recount, restock-return. Reason-coded adjustments are the mechanism that makes shrinkage visible instead of silent.
- **Count discipline** — full counts and partial/cycle counts, count sessions with review and approval before they take effect, and variance reporting by quantity and by cost.
- **Permissions and attribution** — stock actions gated by role; adjustments, counts, and write-offs attributed to the user who performed them; activity/audit logs.
- **Reporting** — stock levels, movements in and out, variance, aging, and valuation reports as a first-class category.
- **Identification** — SKU / barcode / GTIN; scanning as the dominant data-entry mode for receiving and counting; label printing in retail-facing products.
- **Sales-channel linkage** — selling (at the POS, through sales orders, or on e-commerce channels) decrements stock automatically, and the stock record feeds availability back to the selling surfaces.

### One Structure, Many Implementations

The core model is conceptual. Implementations vary, and none of them is the definition:

```text
Concept:   Stock record            Implementations: per-variation stock levels, batch/lot quantities,
                                   bin quantities (warehouse depth)
Concept:   Movement                Implementations: confirmed inventory documents (registration,
                                   write-off, transfer, waybill), POS sale postings, order
                                   fulfillments, adjustment forms
Concept:   Count                   Implementations: full/cycle count sessions with approval,
                                   stocktake documents with effective dates, scanner-driven
                                   counting apps
Concept:   Replenishment trigger   Implementations: low-stock alerts, reorder points, reorder
                                   suggestions, AI demand forecasts
Concept:   Cost basis              Implementations: unit cost per receipt, FIFO batches, average cost
```

A reader who has only seen a small shop's scanner-driven stock app should still recognize a chain's document-driven back office and an ERP inventory module as the same Type from the defining core.

## How It Works

### Set up the record

Items are defined (or imported) with their variations, SKUs/barcodes, and stock-tracking enabled; locations are defined (stores, stockrooms, warehouses). Initial quantities are entered by count or by receiving. From then on, the record lives by movements.

### The receiving loop (stock comes in)

```text
Raise purchase order      vendor, delivery location, expected date, item lines + quantities + unit costs
→ Send to vendor          email/PDF; order sits as an open commitment
→ Receive                 full or partial, against the PO lines; scanning typical
→ Stock lands             on-hand rises at the receiving location; unit cost captured;
                          discrepancies (damaged/missing) recorded with reasons
```

Receiving can also happen without a PO (direct stock registration), but the PO path is the standard one wherever purchasing matters.

### The selling linkage (stock goes out)

Sales at the POS, order fulfillments, and e-commerce sales decrement on-hand automatically and continuously — the inventory system does not execute the sale, it records its stock consequence. Bundles and assemblies may pull their components out of stock when sold. This linkage is what keeps the record current between counts.

### The correction loop (record meets reality)

```text
Discover a discrepancy    (damaged unit, missing unit, miscount, expired goods)
→ Record an adjustment    with a reason: damage / theft / loss / expiry / recount / return-to-stock
→ On-hand changes         the reason and the user are kept on the record
```

Reason-coded adjustments accumulate into the shrinkage picture that loss-prevention and finance read.

### The count cycle (the record is re-anchored)

```text
Schedule a count          full count (everything at a location) or cycle count (a subset,
                          e.g. one category at a time)
→ Count                   scan or key in actual quantities, often across several devices
→ Review                  compare counted vs recorded; variances by quantity and by cost;
                          override or recount lines as needed
→ Approve / complete      the count takes effect: the record is adjusted to match reality
```

Products differ in strictness: some treat an approved full count as a complete accounting (uncounted items go to zero), some lock the location against stock changes while the count runs, some date the resulting adjustments with an effective date for accounting. The cycle repeats — full counts periodically, cycle counts continuously — so the record never drifts far.

### The replenishment loop (the record drives buying)

```text
Stock falls               through sales, write-offs, transfers
→ Threshold crossed       low-stock alert fires, or item hits its reorder point
→ Replenishment proposal  reorder suggestion / suggested quantities per location
→ Purchase order raised   to the vendor (or transfer raised from another location)
→ back to receiving
```

In chain operations the same loop runs at headquarters: aggregate demand across stores, buy centrally, distribute to locations by transfer.

### Core vs Common vs Optional

**Defining core** — without these, not inventory management:

- item-level stock records at named locations
- recorded stock movements (in / out / between / corrections)
- physical count reconciliation

**Standard capabilities** — present in most mature products:

- replenishment machinery, purchasing side (vendors, POs, receiving), transfers, cost/COGS/valuation, reason-coded adjustments, count discipline with approval, permissions and audit, reporting, barcode identification, sales-channel linkage

**Variant / optional** — depends on segment, scale, and deployment:

- chain/HQ central purchasing and distribution, multichannel stock sync, warehouse depth (bins, serial/lot, pick zones), order-allocation depth (on-hand vs allocated vs available), unit conversions (case ↔ unit, weighed goods), forecasting/AI reordering, consignment stock, bundle/assembly recipes, accounting-integration depth, plan-tiered packaging

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Stock overview

The manager's primary surface.

- on-hand quantities by item and variation, per location; filterable by location, category, vendor, stock status
- primary actions: adjust stock, receive stock, add item to a purchase order or transfer, set low-stock alert, print labels, export

### Receiving surface

Where deliveries become stock.

- open purchase orders with expected deliveries; line-by-line or scan-driven receiving; unit cost and cost-change indicators
- primary actions: receive in full / partially, record damaged or missing quantities, add receiving fees

### Count surface (often on handheld devices)

Where the record is re-anchored.

- count sessions (full / cycle) with progress state; scan-driven or keyed quantity entry; counted-vs-recorded comparison with variances by quantity and cost
- primary actions: start count, enter/scan quantities, submit for review, override a line, approve the count

### Purchase orders

- order list by state (draft / sent / receiving / received / closed or archived); order detail with vendor, delivery location, expected date, lines
- primary actions: create, edit, send to vendor, receive, cancel

### Transfers

- transfer list and detail (origin, destination, lines, state)
- primary actions: create transfer, ship/send, receive at destination

### Adjustment / write-off surface

- reason-coded stock corrections, individually or in bulk; history of adjustments with user attribution

### Reports

- stock levels, movements in/out, variance, aging, valuation, purchase and supplier reports; exportable for finance

### Admin / settings

- locations, units of measure, adjustment reasons, reorder parameters, user roles and inventory permissions

## Important Rules / Behaviors

### On-hand changes only through movements

The stock quantity is not a free-editable field; it moves because something happened — a receipt, a sale, a transfer, a reason-coded adjustment, or an approved count. This discipline is what makes the movement history an audit trail and the record trustworthy.

### Counts take effect on approval, not on counting

A count session is a draft until it is reviewed and approved/completed; only then do adjustments post. Some products make approval irreversible, lock the location while counting, or treat an approved full count as a complete accounting. Exact strictness is product-dependent.

### Transfers conserve stock

Moving stock between locations decreases the origin and increases the destination. Stricter implementations check that the origin actually holds the quantity before the transfer can take effect; insufficient stock blocks or leaves the transfer pending.

### Adjustments carry reasons, and reasons carry meaning

Damage, theft, loss, expiry, recount — the reason on an adjustment is what turns stock loss from a silent number into manageable information (shrinkage by cause, by location, by item).

### Negative stock is a visible anomaly

Several products surface negative on-hand quantities as a reportable, correctable state rather than silently clamping to zero — a signal that movements and records have diverged.

### Cost follows the stock

Receiving captures unit cost; sales consume cost (COGS) by the product's costing method; adjustments and transfers can carry or allocate cost. Inventory value on the books is derived from the stock record — which is why finance cares about count discipline.

### Permissions match money and trust

Stock actions are permission-gated (receive, adjust, write off, approve counts, edit costs) and attributed to users, because the stock record underpins both the shrinkage picture and the financial valuation.

## Variants

- **Scope posture** — single-store back office; chain operation with headquarters-level central purchasing and distribution to stores; multichannel stock hub synchronizing stores, warehouses, and e-commerce channels against overselling.
- **Warehouse depth** — bins, serial/lot tracking, pick zones, putaway: the warehouse-flavored extension, present in ERP/IMS poles and delivered by companion WMS products in retail suites.
- **Allocation depth** — distinguishing on-hand from allocated/committed stock and available-to-sell; committing received stock to open customer orders.
- **Unit handling** — stock conversion between purchase and selling units (case ↔ each), weighed goods, pack/carton quantities.
- **Count posture** — full vs cycle emphasis, location locking, effective-dated adjustments, dedicated counting apps.
- **Ledger strictness** — document-confirmed inventory ledgers where confirmation posts movements in real time and backdating is impossible, vs looser editable records.
- **Forecasting** — demand forecasting and automated reordering riding on the movement history (an era-common extension).
- **Vertical tuning** — grocery (weighed goods, case quantities), fashion (size/color matrices), food service (ingredient/recipe-level stock as an adjacent module).
- **Commercial packaging** — advanced inventory (counts, POs, transfers) gated behind plan tiers in some products; inventory as a module of a POS suite, of an ERP, or of a standalone IMS.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Retail POS | transaction-side sibling | the POS executes sales and decrements stock as a side effect; this Type owns the stock record, receiving, counts, and replenishment. Remove the stock ledger from a POS and it is still a POS; remove selling from this Type and it is still inventory management |
| Inventory Management System (generic) | domain sibling | same machinery (records, movements, counts, replenishment) applied to any stock-holding operation; the retail instantiation anchors it to merchandise, stores, POS-driven stock-out, and shrinkage |
| Warehouse Management System (WMS) | adjacent, deeper on handling | WMS manages how stock is physically handled inside a warehouse (bins, picking, putaway); this Type manages what/how much exists and how it changes. Bin/serial depth is the blur zone |
| Merchandising / Assortment Planning | planning-side neighbor | decides what to carry and how to present it (forward-looking); this Type records and maintains what is actually there (operational truth) |
| Product Information Management (PIM) | data-side neighbor | PIM owns product data (descriptions, images, attributes); this Type owns quantities. A stock record references a product; it does not describe it |
| Order Management System | downstream consumer | orchestrates customer orders to fulfillment; draws on this Type's stock. Allocation/commitment features are the shared seam |
| Demand Planning | analytical neighbor | forecasts what will sell; this Type records what is and what moved. Forecasting features ride on this Type's movement history |
| Store Operations / Store Task Management | operational neighbor | manages store work and tasks; stock counts may appear as tasks, but the stock record itself lives here |

The most important boundary is with **Retail POS**: the two share the item catalog and the stock numbers, and vendors ship them as one product's front and back halves. The structural difference is ownership of the record — the POS is the system of record for *selling*; inventory management is the system of record for *stock*.

## Representative Products

- **Square for Retail** — payments-first SMB POS with inventory management as its retail back-office mode (stock overview, counts with approval, POs, transfers)
- **Erply** — back-office-first retail suite with a document-driven inventory ledger, chain support, and physical stocktaking
- **NetSuite Inventory Management** — enterprise ERP inventory: multi-location stock, counts, transfers, reorder points, allocation, warehouse-depth extensions
- **Cin7 Core** — multichannel inventory platform for product businesses: stock across locations and channels, stocktakes, reorder suggestions, forecasting

The defining core was checked against older and non-cloud patterns (paper stock ledgers, register-based PLU stock tracking, batch-upload stocktaking) to avoid over-fitting the definition to the current cloud/SaaS era.

## Sources

Research date: **2026-09-07**

- Square Help Center — "Items and inventory" topic; "Track your inventory"; "View, receive, and adjust inventory"; "Conduct, review, and approve inventory counts"; "Create and manage purchase orders" — https://squareup.com/help/us/en/
- Erply Wiki — "Upgrading from old to new inventory system"; "Erply Back Office Terminology" — https://wiki.erply.com/
- Oracle NetSuite Applications Suite Help — SCM: Inventory Management; "Basic Inventory Management" — https://docs.oracle.com/en/cloud/saas/netsuite/
- Cin7 — product page (multichannel inventory management) and Cin7 Core Help Center — "Stock and replenishment" section; "Stocktake" — https://www.cin7.com/ , https://help.core.cin7.com/

> Sourcing limitations: the Lightspeed Retail help center could not be reached (repeated transport errors) and the Shopify Help Center returned access-denied; the retail-suite pole beyond Square is therefore evidenced by Erply. Cin7's multichannel positioning rests partly on marketing pages; its operational claims here use the Core help center. Precise vendor facts (plan gating, item limits, exact adjustment-reason lists, costing-method defaults) are kept in the Research Notes only.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
