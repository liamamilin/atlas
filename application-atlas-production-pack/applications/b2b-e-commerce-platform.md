# B2B E-commerce Platform

## Overview

A **B2B E-commerce Platform** is a seller-operated online commerce platform on which the customers are companies rather than individual consumers. A manufacturer, brand, wholesaler, or distributor uses it to run a self-service ordering channel for its business customers: buyers log in on behalf of their company, order from a catalog whose products and prices are tailored to that company's account, and settle through the account — by purchase order, payment terms, or card.

Three structural properties define the type. First, the buying party is an **organization**: the seller maintains a registry of customer companies, and purchases are made by authenticated people acting on behalf of one of those companies — never by an anonymous visitor. Second, the ordinary commerce core (catalog → cart → order) runs inside that account relationship. Third, **pricing and product availability are mediated by the account**: what a buyer sees is determined by the seller–customer binding (trade pricing, contract prices, customer-specific catalogs), not by a single anonymous public retail price. Remove the organization-account layer and what remains is a consumer e-commerce store; that layer is what makes the platform B2B.

Everything else commonly associated with B2B online selling — quote negotiation, purchase-order approvals, credit management, buyer portals, requisition lists — is standard capability that mature products add on top of this core, not part of what makes the platform what it is.

## Users & Context

The platform has two sides, each with its own population and surfaces.

**Seller side (the operator of the platform):**

- commerce/e-commerce managers — own the channel: catalog publication, price structures, customer accounts, and the health of online ordering
- sales representatives — keep the relationship; mature products let them place or prepare orders on a customer's behalf and hand negotiated terms into the online channel
- customer service / back-office staff — work with the orders the channel produces (credit checks, order changes, invoicing) and often rely on the seller's ERP or order system for fulfillment
- administrators — configure which capabilities are available (quoting, purchase orders, payment methods) and manage the account registry

**Buyer side (the seller's business customers):**

- company account administrator — a person appointed inside the customer organization who manages its account: structure, buyer users, and what each user may do
- buyers / purchasers — order for the company in daily work: procurement staff, branch managers, technicians ordering spare parts
- approvers — in organized purchasing processes, review and approve orders placed by other users before they become binding

Typical sellers: manufacturers and industrial suppliers, distributors and wholesalers, brands with trade or dealer programs, medical and construction suppliers. Typical buyers: businesses that reorder repeatedly against negotiated terms — retail chains, contractors, workshops, service companies, branch networks of larger corporations.

The work context differs from consumer shopping in one practical way: purchases are recurring and consequential. Buyers usually know what they need (SKU, part number, previous order), order repeatedly, and buy under terms negotiated between the two companies. The platform's job is to make that repetitive, rule-bound purchasing self-service without losing the account-specific terms.

## Core Model

The world of a B2B e-commerce platform is organized around one central object — the **buying organization** — and a set of structures that hang from it.

```text
Seller
 └── Customer company account
      ├── buyer users (people, with roles and permissions)
      ├── structure (branches / divisions, billing & shipping locations)
      ├── account-scoped catalog & prices
      ├── payment terms / credit line / tax exemption
      └── history: quotes, purchase orders, orders, invoices
```

### Customer company account

The account represents the buying company as a managed record under the seller. It is created and governed by the seller (or applied for by the company and approved), and it carries everything the two companies have agreed: which products the company may buy, at which prices, on which payment terms, with which tax exemptions. Orders, quotes, and invoices all belong to this account. In many products the account also models internal structure — branches or divisions, each with its own shipping and billing addresses — and larger enterprises may group related companies under a parent account.

### Buyer users

A buyer user is a person who acts on behalf of the company. Each user belongs to exactly one company account and carries a role inside it, with permissions that determine what they may do: browse and order, request quotes, approve other users' orders, or administer the account itself. This internal role model is what allows a company with many purchasers and several approvers to work in one shared account while keeping purchasing control inside the customer organization.

### Seller catalog and account-scoped pricing

The seller publishes a catalog of products as in any commerce platform. What is specific to B2B is that the catalog a buyer actually sees, and the prices on it, are derived from the account. The standard mechanisms are:

- **price lists / pricing levels** — sets of prices that the seller assigns to a company account or to a customer group, so different companies see different prices for the same product
- **account-scoped catalogs** — product selections scoped to an account (or a branch of it), so the assortment itself can differ per customer
- **negotiated contract prices** — where an account has a specific agreed price for a product, that price governs over any general level

The result is a platform on which there is no single "the price" of a product in the consumer sense: there is the public or base price, and there is the price this account is entitled to. For many sellers, the base price is not even shown to logged-in trade buyers at all.

### Ordering objects

Between catalog and order, mature products offer a set of buying tools shaped by how businesses actually purchase:

- **cart** — the ordinary accumulation of items before submission
- **quick order / SKU entry** — a form for entering product numbers and quantities directly, for buyers who already know what they need
- **requisition or shopping lists** — saved selections (per team, per project, per branch) that can be reordered or converted into a cart; repeat ordering of the same basket is a primary daily action
- **quote (RFQ)** — when a price must be negotiated, the buyer requests a quote from a cart or list; buyer and seller exchange the quote — adjusting items, quantities, and discounts — until they reach an agreement, and the agreed quote can then be converted into an order
- **purchase order and approval** — in organized accounts, a submitted cart becomes a purchase order first; it routes through the buyer-side approval rules (for example, approvers review orders placed by other users) before it becomes a binding order

### Order and settlement

An order is the binding record of a purchase. It is attributed to the company account — typically to the account, the ordering user, and the branch or location it ships to — and it enters the seller's order processing. Settlement runs through the account: many companies buy **on payment terms** (goods are invoiced and paid later, under terms the account defines) against a **credit line** the seller maintains for the account; card payment also exists, especially for lighter-weight wholesale shops. Invoices, order history, shipment status, and account balances are visible to the buyer as self-service views of the account.

### Seller-side management

Running the platform is itself a substantial job, so the seller works in an administration surface of comparable weight: managing company accounts and their users, assigning price lists and catalogs, handling incoming quotes, monitoring orders and credit exposure, and configuring which B2B capabilities are switched on. In many products the seller's back office — most commonly the ERP — remains the system of record for prices, stock, customer master data, and sometimes the buying rules themselves; the platform then presents those rules to the buyer rather than keeping its own independent copy.

## How It Works

The life of the platform has two loops: a seller loop that establishes and maintains the account relationship, and a buyer loop that executes purchasing inside it.

### Establishing the account

```text
Seller creates the customer company account
  (or the company applies for one, and the seller approves)
→ define structure: branches/divisions, addresses
→ invite or create buyer users; assign roles
→ attach the account's terms: price list / catalog, payment terms, tax exemption
→ buyer begins ordering
```

A company account is rarely self-serve in the consumer sense: access is granted by the seller (or through an application the seller accepts), because the account *is* the commercial contract surface between the two firms.

### The buyer's daily loop

```text
Sign in under the company account
→ see the catalog and prices scoped to the account
→ build the order: browse / search, quick-order by SKU,
   or convert a saved requisition list (or a past order) into the cart
→ either check out directly
   or request a quote → negotiate with the seller → convert the agreed quote
→ submit — as a purchase order first if the account uses approvals,
   routed through the account's approvers
→ order becomes binding
→ settle: on account under the account's payment terms, or by card
→ track: order status, shipments, invoices, balances in the account view
```

Two things in this loop distinguish it from consumer checkout. The order passes through the **buyer organization's own purchasing control** (roles and approval rules), and the settlement is settled **against the account** rather than against an anonymous payment.

### The seller's operating loop

```text
Maintain the account registry (onboard companies, users, roles)
→ maintain price structures (price lists, account catalogs, contract prices)
→ handle quotes: respond, adjust, agree
→ monitor orders and credit exposure
→ orders flow into the seller's fulfillment (directly, or through the ERP)
→ sales reps use the same data to serve accounts
   (preparing orders or draft orders on a customer's behalf)
```

### How products differ in where the data lives

The same core works in noticeably different architectures. Some platforms keep their own pricing and catalog data and manage it in the platform admin. Others — most explicitly the ERP-integrated products — keep no independent copy: prices, stock, and customer terms are read live from the seller's ERP at the moment a buyer loads a page, and buying rules such as approval workflows apply "where they exist in the ERP configuration." This is a packaging and data-ownership difference between products, not a difference in the core model: in both cases the buyer experiences an account-scoped catalog, and the account is the carrier of terms.

## Interfaces

### Buyer storefront

The commerce surface, scoped to the signed-in buyer's account.

- typical information: account-specific product listing, account prices (often replacing public prices entirely), stock availability, product data sized for large technical catalogs
- primary actions: search and browse, add to cart, quick order by SKU, manage requisition lists, reorder past purchases, request a quote, proceed to checkout / PO submission

### Buyer account dashboard

The company's self-service cockpit — the surface that makes the account tangible to the buyer.

- typical information: recent and historical orders, quotes and their status, invoices and account balance, payment terms, credit visibility (where permissions allow), saved lists, the company's user list (for administrators)
- primary actions: track orders and shipments, download invoices, manage users and roles (administrator), reorder, open quotes

### Quote workspace

The negotiation surface shared by buyer and seller.

- typical information: quoted items, quantities, negotiated prices/discounts, message history between the two parties
- primary actions: request a quote, add or remove items, propose or apply prices, accept and convert to order

### Purchase-order / approval view

The buyer-side control surface used where the account enforces approvals.

- typical information: submitted purchase orders, their approval state, orders awaiting a given approver
- primary actions: approve, reject, or adjust a purchase order; view who must act

### Seller admin console

The operator surface for the whole customer base.

- typical information: company accounts and their users/roles, price lists and account catalogs, incoming quotes, orders, credit lines and payment terms, platform capability configuration
- primary actions: create and configure company accounts, assign pricing/catalogs, respond to quotes, manage orders and credit, enable or disable B2B features

### Sales-rep tooling

Support for assisted selling, present in mature products in different forms.

- typical information: the same account data the buyer sees (prices, history, credit)
- primary actions: place or prepare an order on behalf of a customer (for example as a draft order the buyer then confirms), start quotes from the seller side

## Important Rules / Behaviors

- **What you see depends on who you are.** The account binding governs assortment and price. The same product page can show different prices to different companies, and some products may not be offered to some accounts at all. This is the platform's most basic behavior.
- **Buying authority is internal to the customer organization.** Permissions inside the account decide who may order, quote, approve, or administer. An order placed by a junior purchaser may remain non-binding until the account's approver accepts it. Where the platform offers purchase-order mode and the account enables it, a submitted cart typically becomes a purchase order first — so purchases route through the account's approval machinery rather than going straight to a binding order.
- **The account carries the settlement relationship.** Payment terms and any credit line belong to the account, not to the individual buyer. A purchase on terms increases the account's exposure; sellers manage that exposure, and ordering may be tied to the account's credit limit.
- **The negotiated price wins.** Where a contract or account-specific price exists, it overrides general price levels; quotes, once agreed, convert into orders under the agreed terms.
- **Orders are attributed to the organization, not just the person.** An order records the company account, typically the ordering user and the branch/location it concerns — necessary because a company account may span many locations with different shipping addresses, catalogs, and sometimes tax exemptions.
- **Tax exemptions and legal attributes attach to the account** (or its locations), not to individual purchases: business buyers are routinely exempt from particular taxes, and the platform applies this automatically at order time.
- **The back office is the anchor of truth.** In mature deployments the platform hands orders into the seller's fulfillment and usually draws prices, stock, and customer terms from the seller's ERP or equivalent systems. When the back office is the system of record, ordering rules (approvals, terms) may be enforced by surfacing ERP configuration rather than by independent platform settings.
- **Access is a seller decision.** A visitor cannot shop anonymously as a company: until the seller grants or accepts an account (with users and terms), there is nothing to buy with.

## Variants

The core model is stable; products differ mainly in packaging, coexistence with consumer commerce, and market focus.

- **B2B module on a consumer platform** — a mainstream commerce platform that adds the organization-account layer (companies, account-scoped catalogs and prices, payment terms) on top of a consumer store core; B2B features may be plan-gated at the high end.
- **Integrated B2B suite module** — an enterprise commerce suite in which the B2B feature set (company accounts, shared catalogs, negotiable quotes, purchase orders, credit) is an installable/activatable layer that can coexist with consumer selling in the same store.
- **Add-on B2B edition** — a dedicated B2B product layered onto a SaaS store, often with its own buyer-facing portal and sales-rep tooling, and with the option to run B2B and B2C as separate storefronts.
- **ERP-integrated platform** — a B2B-first product with no independent pricing/stock/customer master: the seller's ERP is the system of record and the platform reads it live. Common among manufacturing and distribution sellers.
- **B2B-first vs dual-model** — some deployments sell only to business accounts; others run both consumer and business customers, either in one store or in separate storefronts.
- **Lightweight wholesale shops** — smaller sellers may run the organization-account layer with card-only checkout and no quotes or approvals; the defining core is intact, the standard kit is simply thinner.
- **Industry overlays** — vertical catalogs and rules: automotive parts filtered by make/model, regulated goods with compliance data, deep technical catalogs for machinery and electronics, construction-material ordering with pickup logistics.
- **Order-channel variants** — alongside the web storefront, the same account relationships may feed sibling channels such as EDI ordering or rep-entered orders.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| E-commerce Platform (consumer) | sibling / same continuum | buying party is an individual (optionally anonymous), single public price, anonymous card checkout; here the buying party is an organization account with account-mediated pricing — vendors often ship both modes in one product line |
| Online Store Builder | adjacent | tooling to build and run a store; when aimed at business customers it gains this Type's account layer; when aimed at consumers it lacks it |
| Wholesale Commerce Platform | probable overlap (sibling leaf) | wholesale is the commercial relationship (bulk selling to trade buyers); it is typically executed *on* a platform of this Type — org accounts, trade pricing, catalog ordering — and lacks an independent structural core; flagged for joint review |
| Dealer / Distributor Commerce Portal | probable variant (sibling leaf) | the same structure applied to the manufacturer→dealer channel: contract pricing, account-bound catalogs, ordering; differs in channel relationship, not in core objects |
| Online Marketplace / Multi-vendor Marketplace | different structure | a plurality of third-party sellers mediates; here one seller operates its own channel to its own business customers |
| Configure Price Quote (CPQ) | adjacent | CPQ centers on configuring complex products into a priced quote; this platform treats the quote as one workflow object in an ordering flow, not as the centerpiece of product configuration |
| Procurement Platform (buyer side) | counterpart | procurement tooling belongs to the buying organization's sourcing process; this platform is the seller's selling channel; the two interconnect at order time |
| Order Management System | downstream | OMS orchestrates fulfillment after capture; this platform's primary flow ends at the order plus settlement record |
| Customer Portal | overlapping surface | self-service views (orders, invoices, balances) exist in both; here they are secondary surfaces of the commerce flow, there they are the whole |
| Product Information Management | upstream | PIM feeds product data into the catalog; it does not manage accounts, pricing bindings, or ordering |

The boundary with consumer e-commerce is the structural dividing line of the whole category: the organization-account layer. Because the same vendors frequently ship consumer and business selling as one product, the practical distinction is a mode of the platform, but the mode changes the users, the core objects, the rules, and the settlement model enough to constitute a distinct Application Type.

## Representative Products

- Adobe Commerce B2B (integrated B2B module in an enterprise commerce suite)
- Shopify Plus B2B (organization-account layer on a mainstream consumer platform)
- BigCommerce B2B Edition (add-on B2B edition with dedicated buyer portal)
- Sana Commerce Cloud (ERP-integrated B2B-first platform)

These were selected to span the main packaging philosophies and customer tiers of the category. The core model was checked across all four; product-specific mechanisms (for example, a particular platform's shared-catalog or draft-order design) are intentionally not generalized here.

## Sources

Research date: **2026-09-06**

- Adobe — "Introduction to Adobe Commerce B2B", Adobe Experience League commerce-admin documentation — https://experienceleague.adobe.com/en/docs/commerce-admin/b2b/introduction
- Shopify — "Apps and B2B", Shopify Dev documentation — https://shopify.dev/docs/apps/build/b2b
- BigCommerce — "B2B Edition for Stencil Themes (Legacy Experience)", BigCommerce developer documentation — https://docs.bigcommerce.com/developer/docs/b2b-edition/storefront/stencil.md
- Sana Commerce — official product site, platform pages and FAQ — https://www.sana-commerce.com/

> Sourcing limitation: several official help centers could not be retrieved from the research environment on 2026-09-06 (a vendor help center returned HTTP 403; a B2B-native platform's documentation site failed with transport errors twice and was dropped as an evidence source; a help center rendered as script-only). Evidence therefore rests on the four sources above; assertions are kept at the strength these sources support. No precise numeric limits (credit amounts, approval thresholds, price-list counts, plan entitlements) are asserted anywhere in this document, and no unverified platform (including the unreachable B2B-native product) is relied on for any claim.
