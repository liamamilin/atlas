# Mobile POS

## Overview

A **Mobile POS** is an operator-facing transaction application that executes item-level in-person sales from a portable device — a smartphone, tablet, or purpose-built handheld — carried to wherever the exchange happens: a counter, the sales floor, a checkout queue, a market stall, a pop-up event, or the customer's door. It composes a sale from a seller-defined priced catalog, collects payment in person through payment capture attached to or built into the device, and records the completed transaction with a receipt.

The Type exists because the traditional point of sale anchors the sale to a place: a fixed register wired to a counter, a drawer, and a printer. A Mobile POS detaches the sale surface from the place. The selling machinery is the same as any in-person point of sale — catalog, basket, tender, receipt — but it travels with the seller, which makes selling possible where no counter exists at all (markets, pop-ups, mobile services, delivery) and faster where a counter does (line busting, floor selling).

Canonical boundary: a Mobile POS is not the payment rails it calls (payment processing), not the customer's own remote shopping surface (e-commerce checkout), and not a bare card reader that only enters amounts. Its closest sibling is **Retail Point of Sale**, the fixed-counter form of the same sale execution — the two share the entire sale machinery and differ in surface class and selling context; some vendors ship them as configurations of one product, while other vendors build products that are mobile-only from the ground up.

## Users & Context

**Primary users — sellers who take the sale to the customer:**

- **Micro-merchants and mobile sellers without fixed premises** — market traders, pop-up and event sellers, food trucks, craft fair vendors, mobile service providers (grooming, cleaning, repair, personal training), delivery and field sellers. For this population the portable device plus a card reader (or just the phone itself) is the entire point of sale; there is no counter, and often no cash drawer or receipt printer.
- **Store staff selling away from the register** — sales associates checking customers out on the floor or in the queue (line busting), doing curbside handoff, or carrying inventory visibility with them while helping customers.

**Secondary users — oversight and configuration:**

- **Owner / administrator**: maintains the catalog, taxes, employees, and payment settings, usually in a companion web or desktop back office rather than on the selling device itself.
- **Shift lead / manager**: handles permission-gated actions such as refunds, mirroring the counter form's supervision model.

The work context differs from the counter form in three practical ways. First, connectivity is often unreliable — markets, basements, rural routes — so how the product behaves offline matters more than in a wired store. Second, the hardware is consumer-grade and personal: the device may be the seller's own phone, and peripherals (readers, docks, printers) attach and detach. Third, the sale is completed in the customer's presence at the moment of exchange, and the receipt is usually digital — sent by email or SMS rather than printed.

## Core Model

### The Defining Core

```text
Seller-defined priced item catalog (carried on the mobile device)
└── Sale (operator composes the basket from catalog items; system prices it, incl. tax)
    └── Payment (in-person tender collected at the point of exchange)
        └── Completed transaction record + receipt
```

Executed on a **portable, seller-carried sale surface** — with payment capture either paired to the device, attached to it, or built into it — so the checkout can move to wherever the exchange happens.

Five properties. If any one is removed, the product is no longer recognizable as a Mobile POS:

- **Seller-defined priced item catalog carried on the device** — the sale's content comes from items the seller has defined, with prices and tax treatment the system applies. Without this, the product is an amount-entry card reader or payment terminal, not a point of sale.
- **Sale construction on the device** — the seller composes a basket by adding items and quantities, and the system — not the seller — computes the total. Without this, a charge is just a payment, not a sale.
- **In-person payment collection at the point of exchange** — at least one tender settles the basket, in the customer's presence, on or through the portable device. Without this, the product is remote checkout, a payment link, or an invoice — different Types.
- **Completed transaction record + receipt** — the sale closes into a durable record with a receipt for the buyer, which reporting, refunds, and disputes refer back to. Without this, there is no system of record, only ephemeral acceptance hardware.
- **Portable seller-carried surface** — the device can be carried to the exchange, and the product is built around that ability. This is the property that distinguishes the Type from its fixed-counter sibling, Retail Point of Sale: remove it, and the same machinery is simply a counter POS.

### Standard Capabilities

A typical modern product carries most of the following. They make the Type practical; they do not define it.

- **Catalog layer synced from a companion** — items with prices, tax treatment, and often variants and categories are maintained in a web dashboard or back-office app and pushed to the selling device; one catalog is shared across all the seller's devices and selling surfaces.
- **Item lookup adapted to small screens** — a visual item grid or favorites, search, barcode scanning with the device's camera or an attachable scanner, and a keypad for custom amounts when nothing in the catalog fits.
- **Sale adjustment** — quantity, notes, discounts, and tax shown on the running basket; the ability to set a sale aside and return to it (saved carts) when serving more than one customer.
- **Tender set** — contactless tap, chip insert, and (where the capture hardware supports it) magstripe swipe; mobile wallets; cash with change computation; card on file; gift cards; regional QR and wallet schemes; tipping prompts where the trade calls for them.
- **Digital-first receipts** — email or SMS by default, reprintable from the transaction record; printed receipts only where optional printer hardware exists.
- **Transaction history on the device** — the seller's recent sales, with refund flows against prior transactions; dispute and chargeback handling provided by the surrounding payment service.
- **Inventory decrement and stock visibility** — selling reduces stock counts and surfaces availability; deeper stock control lives in the back office.
- **Staff accounts and permission gating** — taking payment and issuing refunds are permission-scoped actions, attributed to the staff member who performed them.
- **Offline posture** — some products keep selling (fully or payments-only) through connectivity loss and reconcile later; others require a connection. The posture interacts with the acceptance method (see Rules below).
- **Multi-device operation** — several phones, tablets, or handhelds on one account, sharing catalog, history, and settings.

### One Structure, Many Implementations

The Core Model is conceptual. Each concept has several common implementations, and none of them is the definition:

```text
Concept:             Payment capture
Implementations:     paired card reader (Bluetooth or cable) · built-in NFC on the seller's
                     phone (software-only "Tap to Pay") · all-in-one portable terminal with
                     the POS app built in

Concept:             Item identification
Implementations:     camera barcode scan · attachable scanner · visual grid / favorites ·
                     search · keypad custom amount

Concept:             Receipt
Implementations:     email / SMS / QR digital receipt (default) · printed receipt (optional
                     printer hardware)

Concept:             Catalog housing
Implementations:     on-device item library synced from a web dashboard · unified commerce
                     back office · standalone terminal with the catalog on it

Concept:             Cash handling
Implementations:     recorded cash tender with manual change · optional physical drawer as an
                     accessory
```

A reader who has only seen a phone-and-dongle kit should still recognize a purpose-built handheld, a portable terminal, and a software-only phone setup as the same Type from the defining core.

## How It Works

### Set up the selling kit

```text
Install the POS app on a phone or tablet
→ define the catalog (or sync it from the back office)
→ pair a card reader, or enable built-in contactless acceptance on the device
→ optionally add peripherals: dock or stand, cash drawer, receipt printer, scanner
```

Setup is quick, because the hardware is consumer-grade and the catalog can start small — which is what allows selling to begin at a weekend market with nothing but a phone and a reader.

### The portable checkout loop (defining workflow)

```text
Go to the customer      carry the device to the exchange (floor, queue, table, stall, doorstep)
→ Compose the sale      scan with camera or scanner, or select from grid / search;
                        adjust quantity, notes, discount
→ Charge                the system computes subtotal, tax, total
→ Collect payment       customer taps card or phone on the reader or the device,
                        or inserts / swipes; or pays cash and the seller computes change
→ Complete              transaction recorded; digital receipt sent (email / SMS) or printed
```

The loop is the counter checkout loop relocated. Two things stay constant: the sale surface remains in the seller's hands, and the customer's participation is presenting a payment instrument (and, on reader hardware, completing the payment action on the reader).

### Selling where no counter exists

For a seller without premises, the kit is the whole store: the catalog lives on the device, cash is optional and change is made by hand, receipts are digital, and the product's offline behavior determines whether a market stall in a dead zone can still trade. Connectivity-aware products buffer card payments offline and settle them when a connection returns; software-only acceptance typically requires a live connection, so sellers who need offline trade carry a reader.

### Selling inside a store

For staffed retail, the same app becomes a second, mobile register: associates take the checkout to the queue (line busting), check stock without leaving the customer, set a basket aside and retrieve it later, and complete the sale curbside. The device shares the store's catalog, inventory, and transaction history with the fixed registers.

### After the sale

Completion feeds the same downstream machinery as any point of sale: inventory decrements, the sale appears in history and reports, refunds are issued from the device against prior transactions, and settlement and payouts are tracked in the companion back office (or by the bundled payment service, in products where selling and payment processing come from the same vendor).

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Sale screen (on the device)

The seller's primary surface — a touchscreen sized for one hand or a small tablet.

- item grid organized by category, favorites, search field, scan input
- running basket with per-line quantities and totals
- primary actions: add item (tap or scan), adjust line, apply discount, enter custom amount, charge

### Payment surface

Where the sale becomes money.

- total due; prompt to tap, insert, or swipe — rendered on the device itself, on the paired reader's screen, or as an on-screen contactless prompt when the phone is the terminal
- cash path with change computation; tipping prompt where enabled
- primary actions: take payment, cancel back to the basket

### Item management (on device or in companion)

- create and edit items, prices, tax treatment; organize by category
- typically mirrored in the web back office and synced to the device

### Sales history / transactions

- recent completed sales with amounts, tenders, and timestamps
- primary actions: look up a sale, resend or reprint receipt, start a refund

### Settings & device security

- reader pairing and acceptance-method setup (including enabling software-only contactless where offered)
- passcode / lock options for the payment screen; staff sign-in; receipt destinations

### Companion back office (web or desktop)

- catalog and employee management, tax settings, sales and payout reports, dispute handling
- the selling device consumes this configuration; only within-permission adjustments happen live

## Important Rules / Behaviors

### The device stays with the seller

The sale surface is operated by the seller; the customer presents a payment instrument rather than taking over the device. Products that support software-only contactless acceptance document this explicitly as a security practice, often paired with a device passcode that prevents a customer from navigating away from the payment screen. This is the inverse of e-commerce, where the customer operates their own device.

### The acceptance method shapes capability

Whether payment capture is a paired reader, built into the phone, or an all-in-one terminal determines parts of the sale: sampled products document that software-only contactless acceptance requires a live connection (so offline selling needs a reader), and a failed contactless authorization may require the customer to tap again rather than being retried automatically. The sale model does not change; the tender mechanics do.

### Completion is the state boundary

As in any point of sale, a sale is freely modifiable before payment and becomes a durable record at completion; corrections afterwards happen only through refund flows that reference the original transaction. Attribution to the staff member who performed the sale — and the refund — carries over from the counter form.

### Permissions gate money actions

Taking payment and issuing refunds are permission-scoped. In a solo micro-merchant operation the seller holds all permissions; in a store, associates hold the checkout permission while refunds and other sensitive actions escalate — the same supervision model as the counter form, on portable hardware.

### Cash is optional and peripheral

Cash is supported — tender recorded, change computed by the seller — but nothing in the Type requires a drawer. A physical cash drawer is an accessory that reappears only when the mobile device is used at a staffed counter.

### The system prices the sale, not the seller

Prices and taxes come from the catalog configuration; seller adjustments are deliberate, permission-gated exceptions. This is what keeps the transaction record trustworthy when many sellers, devices, and locations feed one history.

## Variants

- **Micro-merchant kit** — a phone, a reader, and an app as the seller's entire point of sale; digital receipts; minimal or no peripherals; the typical market-stall, pop-up, and mobile-service shape.
- **In-store mobile POS** — additional portable devices inside a staffed store, sharing catalog and history with fixed registers; used for line busting, floor selling, and curbside checkout.
- **Purpose-built handheld** — a dedicated pocketable POS device with integrated scanner, screen, and card capture, used where durability and one-handed scanning matter.
- **All-in-one portable terminal** — acceptance hardware with the POS software built in; the seller may not need a separate phone at all.
- **Software-only acceptance** — the seller's phone itself is the payment terminal (built-in contactless); zero external hardware, with the connectivity and security constraints that follow.
- **Vertical adaptations** — appointments and services, food trucks and street food (often touching restaurant semantics), delivery and field service; regional variants follow local payment mixes and fiscal receipt requirements.
- **Scale** — from a single device as one merchant's whole system, up to fleets of handhelds in a store or chain alongside counter registers.

A variant remains a Variant unless it changes the core users, objects, workflow, or rules so much that the defining core no longer applies — as happens when the sale becomes a check living across a service period (see Restaurant POS below).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Retail Point of Sale | closest sibling; shared sale machinery | the fixed-counter form: purpose-built register surface, counter hardware, store-anchored context; Mobile POS adds the portable seller-carried surface and the no-counter contexts. Vendors ship both as configurations of one product in some families; other products are mobile-only |
| Restaurant POS | adjacent; different sale semantics | an open check tied to a table across a service period, kitchen routing, and tips — even when executed on a tableside handheld; Mobile POS keeps the immediate paid sale |
| Payment Processing Platform / Gateway | underlying layer | moves the money (authorize, capture, settle, disputes); the Mobile POS composes the sale and orchestrates tender, sometimes from the same vendor |
| E-commerce Platform / Mobile Commerce Application | customer-side adjacent | the purchase runs on the customer's own device, remotely; remove the in-person seller-carried surface from Mobile POS and you drift into checkout territory |
| Payment Terminal / amount-only card machines | below the Type | tender capture without a catalog or sale construction is a payment terminal, however portable |
| Digital Wallet / Peer-to-peer Payment Application | consumer-side | personal money movement between people; a Mobile POS is seller-side business sale execution with catalog, taxes, and records |
| Retail Store Management System | back-office neighbor | governs the store behind the sale surface (staffing, tasks, inventory planning); the Mobile POS is the sale-execution surface |

The most important boundary is with **Retail Point of Sale**: the two Types share the entire transaction spine, and the boundary is the sale surface class and the selling context it enables — not the underlying machinery. The most instructive boundary is with the amount-only card reader: the catalog and sale construction are what turn portable payment capture into a point of sale.

## Representative Products

- **Square Point of Sale** (mobile surfaces: phone/tablet app with attachable Readers, purpose-built Handheld, software-only Tap to Pay) — payments-first; the archetypal phone-and-reader lineage
- **Shopify POS** (mobile use) — commerce-platform-first; publishes its own mPOS definition and treats mobile as one selling surface of a unified back office
- **SumUp** — portable-first merchant kit (paired readers, terminal, software-only acceptance) for micro-merchants
- **PayPal Point of Sale (Zettle by PayPal)** — the original European phone-and-reader mPOS lineage, now under PayPal; segments its customers by on-the-go selling

The defining core was checked against older and differently-shaped samples (dongle-era smartphone mPOS, purpose-built portable terminals and handhelds from before the smartphone era, and current software-only acceptance) to avoid defining the Type by the current dominant hardware pattern.

## Sources

Research date: **2026-09-08**

- Shopify — POS product page and POS-types FAQ — https://www.shopify.com/pos
- Shopify — "How To Choose a Mobile POS (mPOS) System" guide — https://www.shopify.com/blog/mobile-pos-system
- Square Support Center — Payments topic (article inventory) — https://squareup.com/help/us/en/topic/payments
- Square — "Accept payments with Tap to Pay on iPhone" — https://squareup.com/help/us/en/article/7786-get-started-with-tap-to-pay-on-iphone
- Square — "Accept payments with Square Handheld" — https://squareup.com/help/us/en/article/8499-accept-payments-with-square-handheld
- SumUp — Support Centre (product and section inventory) — https://help.sumup.com/
- PayPal Point of Sale (Zettle by PayPal) — product and POS systems pages — https://www.zettle.com/gb , https://www.zettle.com/gb/pos-systems

> Sourcing limitations: SumUp's individual help articles render only navigation in the research environment (JavaScript app), so SumUp evidence is at product-structure level. PayPal Point of Sale's help centre timed out, so its evidence is at product-page level. The Shopify Help Center returned HTTP 403 in the earlier retail-POS pass and was not retried; Shopify evidence rests on its product page and vendor guide, both fetched successfully. Claims for those products are calibrated to those evidence levels, and precise vendor facts (device limits, pricing, feature availability) are recorded only in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the sibling-boundary review with Retail Point of Sale are recorded in the paired Research Notes.
