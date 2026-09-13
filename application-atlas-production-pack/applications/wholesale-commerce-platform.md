# Wholesale Commerce Platform

## Overview

A **Wholesale Commerce Platform** is a seller-operated commerce system through which a wholesaler, brand, distributor, or manufacturer sells goods to business buyers — retailers, dealers, and other businesses — over digital ordering surfaces.

Its defining structure has three parts:

```text
Gated business-buyer accounts
└── Wholesale offer presented per account (catalog + account-specific pricing/terms)
    └── Orders against the account, managed through a B2B order lifecycle
        (order → fulfillment → invoicing → payment)
```

Buyers are not anonymous shoppers: they participate as identified business customer accounts whose access and commercial terms the seller controls. Orders are not simple checkout transactions: they move through a trade lifecycle that accommodates partial shipments, backorders, invoicing, and payment on terms. Remove the gated accounts and per-account terms and the product becomes an ordinary consumer storefront; remove the buyer-facing ordering surface and it becomes a back-office order processor; remove the order lifecycle and it becomes a price-list catalog.

## Users & Context

The platform serves two sides of a wholesale relationship.

**Seller side (the operator):**

- **Wholesale/sales staff** — enter and manage orders that arrive by phone or email, manage customer accounts
- **Sales reps / agents** — write orders on behalf of their customers, often in the field or at trade shows, sometimes offline
- **Order processing / fulfillment staff** — work the order queue, produce pick lists, record shipments
- **Accounting / AR staff** — manage invoices, payments, credit memos, statements
- **Administrator** — configures catalog, price lists, customer accounts, permissions, integrations

**Buyer side:**

- **Retail buyers / purchasing staff** — browse the offer, place and reorder against their account, track order status
- Larger buyer organizations may have multiple users under one business account

Typical context: ongoing replenishment and seasonal buying relationships between a seller and a base of known trade customers, replacing phone/email/fax ordering and paper price lists with a digital channel — while still absorbing orders that continue to arrive by phone, email, or in person.

## Core Model

### The Defining Core

**Business-buyer account.** The unit of participation on the buyer side. An account represents a company (a store, a dealer, a restaurant group), typically with one or more user logins attached. Accounts are created by the seller or requested by buyers and approved; access to the offer is gated — a visitor without an account sees little or nothing. The account is the anchor for pricing, order history, and money.

**Wholesale catalog.** The seller's product offer: products with variants (size, color, pack configurations), inventory status, and wholesale (not retail) pricing. Catalog visibility can be restricted — some products are shown only to certain customers or groups.

**Account-specific commercial terms.** The commercial presentation of the catalog is configured per account or account group: price lists, customer-specific discounts, payment terms, shipping options, and tax treatment. Two buyers can see different prices for the same product. This is what makes the offer "wholesale" rather than a public price tag.

**Order.** A purchase placed against an account, entering from any capture channel (see How It Works). The order is the workflow-driving object: it carries the ordered items and quantities and progresses through fulfillment and settlement.

**Order documents.** In mature implementations the order separates into distinct documents that mirror accounting practice: the **sales order** (what was agreed), the **invoice** (what is owed), the **shipment** (what was sent), and the **payment** (what was received). They are related but independently managed — an order can be partially shipped and partially invoiced; a payment can settle an invoice later.

**Money posture.** Payment happens either at order/invoice time (prepay, card) or later under **net terms**, tracked as receivables on the account, with credit memos and statements as the standard adjustment and communication instruments.

### Standard Capabilities of Mature Products

These are widespread in current products but are additions to, not parts of, the defining core:

- **Reordering** — buyers rebuild past orders from their history in a few clicks; order history is a primary buyer surface
- **Quotes** — negotiated quotations that convert into orders
- **Sales rep layer** — rep accounts with permissions, order-on-behalf (frequently a mobile app, sometimes offline-capable), and rep performance reporting
- **ERP / accounting / shipping integrations** — product, inventory, and order data synchronized with the seller's back-office systems; the platform is typically not the books of record
- **Reporting** — orders, customer activity, product sales, inventory, rep performance
- **PDF / digital catalogs** — generated per customer for offline and presentation use

### One Structure, Many Implementations

```text
Concept:                    Gated business-buyer account
Implementations:            seller-created accounts, buyer registration with approval,
                            vetted network membership

Concept:                    Account-specific terms
Implementations:            price lists, customer discounts, privacy groups,
                            per-customer payment/shipping/tax configuration

Concept:                    Order capture channels
Implementations:            buyer self-service portal, rep mobile app,
                            staff entry of phone/email orders, quote conversion

Concept:                    Order lifecycle documents
Implementations:            multi-document OMS (order/invoice/shipment/payment),
                            simpler order-status models in lighter products
```

## How It Works

### Establish the trade relationship

```text
Buyer requests access (or seller creates the account)
→ seller approves and configures the account
→ price list, discounts, payment terms, shipping options, visible catalog assigned
→ buyer logs in and sees "their" wholesale offer
```

The account configuration is the foundation: everything the buyer subsequently sees and pays is derived from it.

### Capture an order

Orders enter through several channels that converge on the same order record:

```text
Buyer self-service:   browse catalog → add variants to cart → submit order
Sales rep:            rep opens the customer's account (often on mobile, sometimes offline)
                      → builds the order → submits on the customer's behalf
Staff entry:          phone/email order arrives → staff keys it into the system
Quote path:           quote negotiated → converted to an order
```

Inventory availability is visible during capture; items can be ordered as backorders when out of stock.

### Work the order through fulfillment and settlement

```text
Order received
→ (optional) approval / custom status workflow
→ fulfillment: pick lists generated, shipments recorded — partial shipments supported
→ invoicing: invoice issued for shipped quantities, with adjustments
   (substitutions, price/shipping/tax corrections, deposits vs balance)
→ payment: captured at order/invoice time, or later under net terms
→ credit memos / statements where needed
→ order complete; history retained for reordering
```

The lifecycle is deliberately document-separated: shipping what is available, invoicing what was shipped, and settling what was invoiced are independent steps. This is the structural difference from consumer checkout, where order, fulfillment, and payment collapse into one transaction.

### Keep the back office in sync

Product, inventory, pricing, and order data flow between the platform and the seller's ERP/accounting/shipping systems; invoices and payments hand off to accounting. The platform is the commerce layer of the wholesale business, not its general ledger.

## Interfaces

### Buyer portal (storefront)

The buyer's primary surface.

- gated access behind login; branded to the seller
- catalog with variants, inventory status, and the account's own pricing
- cart, order submission, order history, order status, reordering
- primary actions: browse, order, reorder, track, (where offered) pay invoices

### Seller admin / back office

The operator's control surface.

- order queue with statuses; order editing, invoicing, shipment recording, payment capture
- customer accounts: approval, price lists, terms, visibility, user logins
- product and price-list management, imports/exports
- primary actions: approve, fulfill, invoice, take payment, adjust, configure

### Sales rep app

The field-selling surface.

- customer accounts and their pricing in the rep's pocket
- order writing (sometimes offline), barcode scanning, on-the-spot payment capture
- primary actions: open customer, build order, submit, check status

### AR / money views

Invoice lists, receivables, statements, credit memos — used by accounting staff and, in buyer-facing form, to let buyers view and settle what they owe.

## Important Rules / Behaviors

- **Access is gated.** The catalog and ordering are closed to anonymous visitors; the seller decides who gets in and what they see. Catalog visibility can differ between customer groups.
- **Price is per account, not per product.** The same product can carry different prices, discounts, and terms for different buyers; the buyer always sees their own configuration.
- **Order, shipment, invoice, and payment are separate steps.** Partial shipments and partial invoices are normal; an order is complete only when fulfillment and settlement both close out. Backorders carry unfilled quantities forward rather than canceling them.
- **Payment posture is a customer attribute.** Some accounts prepay; others buy on terms. Terms accounts generate receivables that the seller tracks and pursues; credit memos adjust what is owed.
- **The account's order history is durable.** Reordering from history is a first-class flow, and history is shared context between buyer, rep, and seller staff.
- **The platform is not the books of record.** Accounting and inventory truth typically live in the ERP/accounting system; the platform synchronizes with it.

## Variants

- **Brand wholesale (fashion/lifestyle pole)** — emphasis on seasonal collections, linesheets, virtual showrooms, and network discovery of new retail buyers; buying-side assortment planning for larger retailers
- **Distributor / wholesaler pole** — emphasis on high-volume replenishment ordering, AR automation, and ERP/accounting integration
- **SMB out-of-the-box pole** — lightweight storefront + order management for smaller wholesalers, often with file-based imports and standard accounting integrations
- **Network/marketplace layer** — some products add a multi-brand discovery marketplace on top of the seller-operated core; the marketplace layer is an addition, not the core
- **Industry packaging** — food & beverage, building materials, jewelry, medical supplies, and others differ mainly in catalog conventions and integrations, not in structure

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| E-commerce Platform / Online Store Builder | adjacent (B2C) | anonymous or consumer shoppers, one public price, single checkout transaction; no gated trade accounts or per-account terms |
| B2B E-commerce Platform | sibling | broader B2B selling (services, SaaS-style checkout); the wholesale leaf is the trade-goods pole with wholesale trade semantics |
| Dealer / Distributor Commerce Portal | sibling (relationship variant) | manufacturer→authorized-dealer networks with authorization/franchise semantics; wholesale commerce is the broader trade pattern |
| Online Marketplace | different operator model | multi-seller venue where the operator is not the seller of record; a marketplace layer can sit on top of a wholesale platform but is not its core |
| Order Management System / OMS | contained capability | back-office order processing without a buyer-facing commerce surface; wholesale platforms bundle OMS-like machinery inside a commerce product |
| Sales-order Capture / CPQ / Sales Rep Apps | single-channel tools | one order-capture channel; the wholesale platform is the whole seller-side commerce system including the buyer portal and account/price machinery |
| Product Information Management / Catalog | upstream data | manages product data with no buyer accounts, pricing per account, or transactions |

The most important boundary is with B2C e-commerce: the surfaces look similar, but the gated business account, per-account commercial terms, and the document-separated order lifecycle are what make this a wholesale Type.

## Representative Products

- NuORDER by Lightspeed — brand-side wholesale commerce with retailer buying/assortment tools and a brand network
- JOOR — fashion wholesale platform with virtual showrooms, linesheets, embedded payments, and digital tradeshows
- Zoey — B2B ordering platform for wholesale distributors with a multi-document OMS, buyer portal, and rep mobile app
- B2B Wave — out-of-the-box B2B ecommerce for wholesalers, distributors, and brands

## Sources

Research date: **2026-09-10**

- NuORDER — https://www.nuorder.com/ (Wholesale, Order Management, Integrated Payments product pages); Knowledge Base: https://helpdesk.nuorder.com/hc/en-us/
- JOOR — https://www.joor.com/ (Brands, Retailers, Wholesale Management, Order Management, JOOR Pay pages); Help Center: https://help.jooraccess.com/hc
- Zoey — https://www.zoey.com/ (homepage; Order Management feature page: https://www.zoey.com/features/order-management/); Support Documentation: https://support.zoey.com/
- B2B Wave — https://www.b2bwave.com/ (homepage and feature sections); Knowledge Base: https://docs.b2bwave.com/

> Sourcing note: official product pages were fetched for all four products; deep help-center articles were consulted for Zoey and B2B Wave only. Operational specifics for NuORDER and JOOR (order-editing rules, approval flows, exact limits) are therefore stated conservatively in this document; precise vendor facts are not asserted.
