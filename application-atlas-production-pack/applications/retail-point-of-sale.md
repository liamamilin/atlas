# Retail Point of Sale

## Overview

A **Retail Point of Sale (POS)** is an operator-facing transaction application that executes item-level retail sales in person: it composes a sale from a store-defined priced catalog, collects payment, and records the completed transaction with a receipt.

Its purpose is to be the store's system of record for selling: every exchange of goods for money at the counter (or at a handheld, or a self-service kiosk) becomes a priced, tendered, recorded transaction. Everything around that spine — barcode scanning, discounts, returns, customer records, cash management, reporting — exists to make that spine fast, correct, and accountable.

Canonical boundary: a Retail POS is not the payment rails it calls (payment processing), not the customer's remote self-service surface (e-commerce checkout), not the back-office planning systems (inventory, merchandising), and not the restaurant service workflow (Restaurant POS) — even though modern products increasingly bundle adjacent pieces of all of these.

## Users & Context

**Primary users** — store staff executing sales:

- **Cashier / sales associate**: composes the sale (scan or select items, adjust quantities, apply approved discounts), collects payment, issues the receipt.
- **Return desk / any associate handling reversals**: processes refunds, returns, and exchanges against prior transactions.

**Secondary users** — oversight and configuration:

- **Shift manager / supervisor**: performs or approves permission-gated actions (refunds, voids, overrides, unlinked refunds), opens and closes cash sessions, counts drawers.
- **Owner / administrator** (usually in a back-office companion, not at the register): maintains the item catalog and prices, tax settings, employee accounts and permissions, and reads sales reports.

The work context is a live selling floor: interruptions are normal (customer waits), hardware is peripheral (scanner, receipt printer, cash drawer, card terminal), and the operator is usually not the person who configured the system. Speed and error-resistance of the checkout loop matter more than feature breadth.

## Core Model

### The Defining Core

```text
Store-defined priced item catalog
└── Sale (operator-composed basket of catalog items + quantities; system-priced, tax applied)
    └── Payment (one or more tenders settle the basket)
        └── Completed transaction record + receipt
```

Executed **live, in person, at the point of exchange, on a store-operated surface** (a staffed register, a handheld device, or a store-controlled self-service kiosk).

Five properties. If any one is removed, the product is no longer recognizable as a Retail POS:

- **Store-defined priced item catalog** — the sale's content comes from items the store has defined, with prices and tax treatment the system applies. Without this, the product is an amount-entry payment terminal, not a POS.
- **Sale construction** — an operator composes a basket by adding catalog items and quantities; the system, not the operator, computes the total. Without this, a card charge is just a payment, not a sale.
- **Payment collection** — at least one tender settles the basket; cash requires change computation, electronic tenders are authorized and captured. Without this, it is a quote or a wish list.
- **Completed transaction record + receipt** — the sale closes into a durable record (with a receipt for the buyer) that reporting, reversals, and audits refer back to. Without this, there is no system of record.
- **Live in-person execution at the point of exchange** — the sale is executed in real time, on a surface the store operates. Without this, the product is a remote customer-self-service checkout, a different Application Type.

### Capabilities Shared by Mature Products

A typical modern retail POS carries most of these. They make the Type practical; they do not define it.

- **Item lookup surfaces** — barcode scan, visual item grid / favorites, search, and manual or custom-amount entry for non-catalog charges.
- **Item structure** — variations/variants of an item, modifiers or add-ons, categories for navigation; unit types including weighed goods.
- **Price adjustment at sale time** — line and sale-level discounts, price overrides, promotions; service charges or tips where the vertical calls for them.
- **Sale-reversal flows** — refunds (money back), returns (money back + item restocked), exchanges (return + replacement, priced by difference); voids before completion; refunds not linked to a prior POS payment as a risk-gated exception.
- **Multi-tender payment** — split payment across tenders; cash tender with change; gift cards and store credit as tender.
- **Receipt** — printed, emailed, or sent by SMS; reprintable from the transaction record.
- **Customer association** — optionally attach a customer to the sale; store credit, house accounts, and loyalty points may act as tender or discount sources.
- **Cash and shift management** — cash drawer sessions, cash tender recording, drawer counts, shift open/close.
- **Held / parked sales** — a basket can be set aside and recalled later (open tickets, saved carts).
- **Employee accounts and permission gating** — sensitive actions (refund, void, discount beyond limits, unlinked refunds) require elevated rights or a manager override; actions are attributed to the employee who performed them.
- **Inventory decrement on sale** — selling reduces stock and surfaces availability; deeper stock control lives in back-office tools.
- **Tax computation** — sales tax or VAT applied from catalog/tax configuration at line or sale level.
- **Sales reporting + back-office companion** — a web dashboard for catalog, employees, taxes, and reports; end-of-day summaries.

### One Structure, Many Implementations

The Core Model is conceptual. Implementations vary and none of them is the definition:

```text
Concept:            Item identification
Implementations:    barcode/SKU scan, GTIN lookup, visual grid, search, manual entry, scale barcodes

Concept:            Sale container
Implementations:    cart, current sale, ticket, order, sales document/invoice

Concept:            Tender
Implementations:    cash, card (chip/contactless/swipe), mobile wallet, gift card, store credit,
                    check, recorded external tender, BNPL, government benefits

Concept:            Receipt
Implementations:    printed, emailed, SMS, fiscal-certified receipt

Concept:            Transaction record
Implementations:    cloud-synced order, local receipt log, fiscal document in a certified format
```

A reader who has only seen a tablet-and-card-reader POS should still recognize an electronic cash register, a fiscal POS, and a self-checkout kiosk as the same Type from the defining core.

## How It Works

### The checkout loop (defining workflow)

```text
Identify items        scan barcode / tap item grid / search / manual amount
→ Adjust lines        quantity, variation, modifier, note, price override, discount
→ Charge              system computes subtotal, tax, total
→ Collect tender      card / wallet / cash (compute change) / gift card / split across tenders
→ Complete            transaction recorded, receipt issued (print / digital)
```

The loop is optimized for seconds per iteration. After completion, the transaction feeds the rest of the system silently: inventory decrements, the customer record (if attached) accumulates the purchase, and reporting totals update.

### Reversal flow (returns, refunds, exchanges)

```text
Locate original transaction   (receipt number, card lookup, or customer history)
→ Choose action               refund / return / exchange
→ Select items                restock returned goods (or skip)
→ Settle the difference       refund to original tender or store credit;
                              exchange may add a further charge or even out
→ Record                      reversal linked to the original transaction and employee
```

Returns restock the item; exchanges net the price difference into a new charge or refund; refunds without a linked prior payment exist as an explicitly risk-gated exception.

### Cash and shift cycle

```text
Open shift / assign drawer
→ sell (cash tenders open the drawer; change computed)
→ count / reconcile drawer (mid-shift or close)
→ close shift; cash session reported
```

### Configuration loop (back office)

Catalog items, prices, taxes, discounts, employees, and permissions are maintained in a companion back-office surface and pushed to the register. The operator at the register consumes this configuration; only within-permission adjustments happen live.

### Core vs Common vs Optional

**Defining core** — without these, not a Retail POS:

- store-defined priced item catalog
- sale construction from catalog items
- payment collection
- completed transaction record + receipt
- live in-person execution on a store-operated surface

**Common mature structure** — present in most modern products:

- item lookup (scan/grid/search), variations/modifiers, discounts, multi-tender, receipts, returns/exchanges, customer association, cash/shift management, held sales, permissions, inventory decrement, tax, reporting + back office

**Variant / optional** — depends on segment, region, deployment:

- surface form factor, omnichannel depth, offline posture, payments stack, vertical adaptations, fiscal/regional layers, chain scale, attached loyalty/gift-card modules

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Sale screen (item selection)

The operator's primary surface.

- item grid organized by category, favorites, search field, scan input
- availability/sold-out indicators where stock is tracked
- primary actions: add item to sale, scan barcode, enter custom amount, open held sales

### Cart / line detail

The in-progress sale.

- lines with item, variation, quantity, unit price, line total; running subtotal, tax, total
- primary actions: change quantity, select variation/modifier, apply discount or override, add note, remove line, attach customer, hold/park sale

### Charge / tender screen

Where the sale becomes payment.

- total due, tender buttons (card, cash, wallet, gift card, split), cash-change computation, tip/service-charge prompts where enabled
- primary actions: take tender, split payment, cancel back to cart

### Completion / receipt

- confirmation state, receipt routing (print, email, SMS), reprint
- signals the transaction is recorded and the loop can restart

### Transactions / receipts list

The store's sale history at the register.

- searchable list of completed transactions with amounts, tenders, employee attribution
- primary actions: look up a transaction, reprint receipt, start a return/exchange/refund from it

### Shift / cash surface

- open/close shift, drawer counts, cash in/out, expected vs counted

### Back-office dashboard (companion surface)

- catalog and price management, tax configuration, employee and permission management, sales reports, reversal audit
- usually web-based; the register consumes its output

### Customer-facing display (optional)

- mirrors the running total and hosts the payment interaction on some hardware configurations

## Important Rules / Behaviors

### The system prices the sale, not the operator

Prices, taxes, and promotion effects come from catalog and tax configuration. Operator adjustments (discounts, overrides) are deliberate, permission-gated exceptions — this is what makes the transaction record trustworthy.

### Completion is the state boundary

Before payment, the sale is freely modifiable (add, remove, discount, hold, void). After completion, the record is immutable; corrections happen only through reversal flows (refund, return, exchange) that reference the original transaction. This asymmetry is the core state rule of the Type.

### Sensitive actions are permission-gated and attributed

Refunds, voids, unlinked refunds, and large discounts typically require elevated rights or manager approval, and the acting employee is recorded on the reversal. The permission model exists because the register handles money and is operated by rotating staff.

### Returns restock; exchanges net out

A return returns money *and* goods to stock; an exchange prices the difference between returned and replacement items (the new basket may even out or leave a balance); refunds follow the original tender where possible, with store credit as a common alternative. The researched sample documents the exchange-difference mechanics in detail for one product; treat exact exchange settlement as product-dependent.

### Cash is a managed inventory

Cash tenders typically open the drawer and accumulate into a shift session that is counted and reconciled; the POS records cash and other non-electronic tenders it never processes itself.

### Tax is configuration-driven

Sales tax or VAT is computed from catalog/tax setup at line or sale level; regional fiscal variants add certified receipt requirements on top.

### Offline posture varies

Some products keep selling (fully or payments-only) through connectivity loss and reconcile later; others require connectivity. This is a deployment/reliability variant, not a defining property.

## Variants

- **Surface form factor** — fixed counter register; tablet/handheld mobile POS (line-busting, pop-ups, markets); self-checkout kiosk (store-controlled, customer-operated). Same core model on different hardware.
- **Channel integration depth** — standalone in-store POS ↔ omnichannel POS sharing catalog, inventory, customers, and orders with e-commerce (buy-online-pickup-in-store, ship-from-store).
- **Deployment and reliability posture** — cloud-first vs local-server; offline modes from none to full.
- **Payments stack** — integrated processor (POS and processing from one vendor) vs bring-your-own processor / external terminal; settlement and closeout semantics follow the processor.
- **Vertical adaptations** — restaurant/quick-service modes (tables, checks, kitchen routing), appointments/services, grocery (scale barcodes, age-restricted goods), benefits programs.
- **Regional / fiscal** — fiscal printers and certified receipts, VAT vs sales-tax models, cash rounding rules, country-specific editions.
- **Scale** — single register → multi-store chains and franchises with headquarters synchronization.
- **Attached commerce modules** — loyalty, gift cards, marketing, payroll: modules around the sale engine, not part of its definition.

A variant remains a Variant unless it changes the core users, objects, workflow, or rules so much that the defining core no longer applies — as happens when table/check service semantics become primary (see Restaurant POS below).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Restaurant POS | adjacent sibling; shared transaction spine | sale semantics differ: table/check lifecycle, service period, production routing, and tips are primary; retail's immediate paid sale and returns flow are not |
| Mobile POS | variant (surface) | same core model on handheld hardware; a form factor, not a separate Type |
| Omnichannel POS | variant (channel depth) | same core model plus unified e-commerce data; an integration posture, not a separate Type |
| Checkout Platform | adjacent | customer self-service, remote, no store-operated live surface; remove in-person execution from POS and you get checkout |
| Payment Processing Platform / Gateway | underlying layer | moves the money (authorize, capture, settle); the POS composes the sale and orchestrates tender, delegating card processing to it |
| Retail Inventory Management | back-office neighbor | plans, counts, receives, replenishes stock; the POS only decrements and displays it as a side effect of selling |
| Loyalty / Gift Card Management | attached module | supplies tender and discount sources to the sale; absent them, the POS is still a POS |
| Self-checkout / kiosk systems | surface variant | store-controlled customer-operated execution of the same sale model |

The most important boundary is with **Restaurant POS**: the two Types share the entire transaction spine, and vendors ship both as modes of single products — the boundary is what a sale *means while it is alive* (a priced basket completed at exchange vs a check living across a service period), not the underlying machinery.

## Representative Products

- **Square Point of Sale / Square for Retail** — payments-first, micro-SMB; retail mode of a mode-based POS app
- **Shopify POS** — commerce-platform-first; POS as a surface of a unified online+offline back office
- **Clover** — hardware-first, app-market platform on Android POS devices
- **Loyverse** — global, mobile-first SMB POS with add-on modules
- **Erply** — mid-market/enterprise cloud POS with back office, chain support, and fiscal editions

The Core Model was checked against older and regional samples (electronic cash registers with PLU tables, fiscal POS editions, market-stall mobile POS, self-checkout kiosks) to avoid over-fitting the definition to the current cloud/tablet era.

## Sources

Research date: **2026-09-06**

- Square Help Center — Payments topic; Items & inventory topic; "Accept payments with Square Register"; "Process a return, exchange, or unlinked refund"; "Accept cash and checks with Square"; "Settle payments and manage tips" — https://squareup.com/help/us/en
- Shopify — POS product page and FAQ — https://www.shopify.com/pos
- Clover developer documentation — data model; "Create an atomic order"; "Transaction types" — https://docs.clover.com/
- Loyverse Help Center — Sales topic (article inventory) — https://loyverse.com/help
- Erply Wiki — section inventory; "Which user rights are required to make a sale in Brazil POS" — https://wiki.erply.com/

> Sourcing limitations: the Shopify Help Center (HTTP 403) and Loyverse article bodies (404) could not be fetched; Clover's merchant help center is a JavaScript app with no fetchable content. Claims specific to those products are calibrated accordingly (Shopify at product-page level; Loyverse at capability-inventory level; Clover at data-model level). Precise vendor facts (settlement windows, plan limits, hardware names) are kept in the Research Notes only.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, the abstraction-layer rationale, and the historical/market-sample check are recorded in the paired Research Notes.
