# Shopping Cart Platform

## Overview

A **Shopping Cart Platform** is the product form of the buyer's pre-purchase accumulation object: a persistent, shopper-bound cart that collects priced, editable line items — products, quantities, chosen options — as *intended* purchases, and hands that accumulated intent to a completion stage (checkout and payment) when the buyer commits.

The defining core is small:

```text
Shopper-bound persistent cart
└── priced, editable accumulation of intended purchases
    │   (line items: product reference + quantity + options; computed totals)
    ├── pre-commitment character
    │   (totals are estimates; everything stays mutable until commitment)
    └── conversion handoff
        (the cart feeds the completion stage that turns intent into an order)
```

The Type has two realizations of one object model:

- **The standalone cart platform** — a hosted or script-embedded cart service attached to a website the merchant already has. The seller keeps the site and the product display; the platform hosts the cart, the checkout, and the order record. This is the form this leaf documents, and the form the market names: vendors in this space self-describe as "a shopping cart you can add to your existing website."
- **The platform-internal cart** — the same object realized inside every e-commerce platform and store builder as an owned internal structure. This is the dominant modern realization; standalone cart products have been largely absorbed into commerce platforms, and the standalone form survives as the attach-to-any-site niche (static sites, CMS sites, site builders without adequate commerce, email and social selling, embedded commerce in other products).

What a cart platform is not: it owns no catalog of record (item data is declared in the seller's own surfaces or referenced from the seller's systems), no storefront, and no fulfillment operation. It sits between the seller's site and the money rails — upstream of payment gateways, upstream of order management.

## Users & Context

**Buyers** are the primary actors on the cart: they add items while browsing a seller's site, adjust quantities and options, leave and return (the cart is supposed to survive that), and finally commit the accumulated intent at checkout.

**Sellers / merchants** are the primary actors *around* the cart:

- configure what can be bought and how (item definitions, options and price modifiers, quantity limits, tax and shipping behavior)
- operate the resulting orders (dashboard, notifications, refunds)
- run recovery on carts that never converted (abandoned-cart emails)

**Developers / integrators** are a first-class audience for the standalone form: attaching a cart platform to an existing site is an integration task (a script snippet, links or buttons with item parameters, or API calls), and the products document themselves accordingly.

Typical contexts: a seller with a website that has no commerce machinery (a static site, a CMS site, a site-builder site whose built-in commerce is inadequate) who wants to sell without rebuilding the site on a commerce platform; a seller who wants to accept orders from email campaigns or social posts; a product team embedding checkout into a larger application (an LMS, an ERP, a service business's site).

## Core Model

### The Defining Core

**The cart.** A persistent working object belonging to one shopper, holding line items. Each line item carries a product reference, a quantity, and the chosen options or variants (size, color, engraving, gift note — with per-option price modifiers where offered). The cart computes totals from its contents: subtotal, applied discounts, and commonly estimated tax and shipping.

**Shopper binding.** The cart is bound to a shopper identity — at minimum an anonymous session that survives page views, at most a known customer account that survives devices and visits. The binding is what makes the cart *the shopper's* cart rather than a form: the shopper can close the browser, come back tomorrow, and find the accumulation intact.

**Pre-commitment character.** Everything in the cart is intent, not transaction. Totals are estimates — the completion stage, not the cart, is where terms become final. The shopper can edit anything — add, change quantity, swap options, remove — until the moment of commitment. One platform's API states the estimate character directly: cart costs are "estimated… subject to change and changes will be reflected at checkout."

**The conversion handoff.** The cart exists to become a purchase. Its terminal act is the handoff: the accumulated, priced intent is passed to a completion stage — a checkout operated by the cart platform itself, or an external one — which captures what the purchase requires, executes payment, and produces the order record. Without the handoff the object is a wishlist (save-for-later), not a cart (commitment-track).

**The order record.** On completion, the cart's contents become an order: the seller's record of what was bought, by whom, for how much. The cart platform provides a merchant-side surface for these orders — deliberately lightweight; sellers with real fulfillment operations push orders onward to dedicated systems.

### One Structure, Many Implementations

The core model is conceptual. Common implementations:

```text
Concept:  Priced, editable accumulation
          Implementations:
          - line items defined as HTML attributes on the seller's buy buttons
          - line items declared as (signed) parameters in add-to-cart links
          - line items created through API mutations against a platform catalog

Concept:  Shopper binding
          Implementations:
          - anonymous session (cookie/token) on the hosted or embedded cart
          - customer account, optionally synced with the seller's own user base
          - B2B buyer identity (company location) in platform-internal carts

Concept:  Conversion handoff
          Implementations:
          - built-in checkout operated by the cart platform (hosted page or embedded flow)
          - redirect to a connected checkout (the platform-internal pattern's checkoutUrl)
```

A reader who has only seen the platform-internal cart (a commerce platform's cart page) should still be able to recognize the standalone form from the core model — and vice versa.

## How It Works

### The seller's attach loop (standalone form)

```text
Sign up with the cart platform
→ define what can be bought (item data in the seller's own surfaces:
   HTML attributes on buy buttons, or add-to-cart links carrying
   item name/price/options — commonly signed so they cannot be tampered with)
→ place add-to-cart affordances anywhere on the site
   (buttons, links, forms — the site keeps its design and its CMS)
→ connect a payment gateway (or use the platform's partner processing)
→ configure cart behavior (taxes, shipping, discounts, quantity limits, notifications)
→ take the cart live
```

The seller never migrates the site. Item data lives with the seller; the platform hosts the cart, the checkout, and the order record. Because item data is declared in surfaces the seller controls (or arrives as parameters), the platform needs a way to trust it — see Important Rules below.

### The buyer's accumulate loop

```text
Browse the seller's site
→ add items to the cart (a mini-cart or floating cart confirms each add
   without leaving the page)
→ open the cart (a cart page or slide-out) and edit freely:
   change quantities, swap options, remove lines, apply a discount code
→ leave — the cart persists (session or account)
→ return — the accumulation is intact
→ commit: proceed to checkout
→ the completion stage captures buyer/contact/delivery details,
   executes payment, and produces the order
→ the cart's work is done; its contents are now an order record
```

### The seller's operate loop

```text
Receive the order (dashboard, email notification, webhook, or push to
   the seller's own ERP/CRM/order system)
→ work the order (view, refund, invoice, tracking — lightweight by design)
→ watch for carts that never converted (abandoned-cart reports)
→ run recovery (abandoned-cart emails, follow-ups)
→ adjust configuration (prices, options, stock limits) as the assortment changes
```

### Capability tiers

**Defining core** — without these, not a shopping cart platform:

- the cart as a persistent, shopper-bound, priced, editable accumulation
- pre-commitment mutability with estimate-side totals
- the conversion handoff to a completion stage

**Standard capabilities** — present in essentially all mature products:

- cart surfaces (mini-cart / floating cart, cart page, count and total badges)
- line editing with stacking rules for repeated adds
- cart-level promotions (discount codes, gift cards)
- estimated totals (subtotal, discounts, tax, shipping)
- persistent and saved carts across sessions and devices
- abandoned-cart tracking and recovery emails
- cart notes and attributes (gift messages, instructions)
- bundled checkout and payment-gateway connections
- merchant dashboard (orders, customers, configuration, test environments)
- quantity/stock limits and mixed cart contents (physical, digital, subscriptions, donations)
- webhooks/API access for the seller's own systems

**Common variants** — depend on segment and posture:

- standalone embeddable service vs platform-internal object
- item-definition substrate (HTML attributes / signed links / API mutations)
- integrity posture (server-side re-validation / signed parameters / platform-authoritative pricing)
- anonymous session vs account-bound carts; customer sync and SSO
- cart entry from email and social posts; marketplace listing integration
- donations, tickets, bookings as first-class cart contents
- offline / purchase-order payment lanes for B2B
- hosted storefront option (a gradient toward store builders)

## Interfaces

### Add-to-cart affordances (on the seller's site)

The seller-side entry points. Buttons, links, or forms carrying item data (name, price, options), placed anywhere on the site — including pages that are not "product pages" at all (a blog post, a landing page, an email). Primary action: add the declared item to the cart.

### Cart surface (mini-cart / floating cart / cart page)

The buyer's working surface for the accumulation.

- typical information: line items with product reference, quantity, chosen options, per-line and total amounts, applied discounts
- primary actions: change quantity, edit options, remove lines, apply a discount or gift card, add a note, proceed to checkout
- shapes vary: a floating widget that follows the shopper, a slide-out panel, a dedicated page — the object behind them is the same

### Checkout

The completion stage the cart hands off to. In the standalone form it is commonly operated by the cart platform itself (a hosted checkout page or embedded flow, branded within constraints); in the platform-internal form it is the platform's own checkout, reached via the cart's checkout URL. Payment details are collected under the platform's security posture; the money rails are the connected gateway's.

### Merchant dashboard

The seller's operations surface, hosted by the platform.

- typical information: orders, customers, abandoned carts, discount configuration, tax and shipping rules, payment-gateway status, test/live environment state
- primary actions: inspect and refund orders, configure items and cart behavior, set up recovery emails, manage environments, integrate (webhooks, API keys)

## Important Rules / Behaviors

### Everything is pre-commitment

The cart's contents are intent. Totals shown in the cart are estimates; the completion stage is where terms become final (a platform API says exactly this: estimated costs, "subject to change and changes will be reflected at checkout"). Checkout-time choices — delivery method, address, payment method — can change the final amounts, and in the platform-internal pattern such checkout preferences deliberately do not write back into the cart.

### The cart persists, the session may not

The cart is designed to survive page views, navigation, and — in mature products — visits and devices. Anonymous session carts are the base pattern; account-bound carts extend persistence across devices. Abandonment (a cart that never converts) is a first-class state, not an error: platforms track it and commonly provide recovery machinery.

### Client-declared item data must be re-validated

In the standalone form, item data is declared in surfaces the seller controls — or arrives as parameters from the buyer's browser. Either way the platform cannot naively trust it. The observed integrity mechanisms:

- **server-side re-validation**: before processing an order, the platform re-reads the seller's site at the item's declared URL and cross-references the declared price/options/quantity against the order; a mismatch blocks the transaction (documented verbatim by one vendor as the answer to "how do you prevent bad actors from changing product pricing with their DevTools before checking out?")
- **signed parameters**: add-to-cart links carry per-parameter signatures so they cannot be forged
- **platform-authoritative pricing**: in the platform-internal pattern, the cart references the platform's own catalog, so the cart cannot disagree with the price of record

### Quantity and stacking rules are cart semantics

Repeated adds of the same item normally merge into one line with an increased quantity; products can override this (each add stays a separate line — for personalized items where every occurrence carries different information). Minimum and maximum quantities per item bound the accumulation; a line reduced below its minimum is removed.

### Mixed contents share one cart

Physical goods, digital downloads, subscriptions, services, donations, and tickets can share a single cart. Shipping options drop out when nothing in the cart is shippable; digital delivery is arranged per item; recurring items initiate subscription terms at completion.

### The order handoff is terminal for the cart

Once the completion stage produces the order, the cart's job is done. Post-order life (fulfillment, edits, returns) belongs to the seller's order systems; cart platforms keep their order handling deliberately lightweight and provide push/webhook integration for sellers who run dedicated operations.

## Variants

- **Standalone embeddable cart platform** — the form documented here: hosted or script-embedded cart attached to an arbitrary site; item data declared in the seller's surfaces; developer-first or merchant-first packaging. The market niche that keeps the Type independent.
- **Platform-internal cart** — the same object inside an e-commerce platform or store builder, exposed through the platform's storefront and (in headless patterns) through a cart API with a checkout-URL handoff. The dominant modern realization; documented here as the absorbed-side variant of the same core model.
- **Classic hosted cart (legacy pattern, still operating)** — buy-now links on any page → a cart page hosted on the vendor's servers → amend and checkout there → payment → email notification. The 2000s form of the same Type; its survival demonstrates the definition is not an artifact of the modern embeddable pattern.
- **Developer-first vs merchant-first packaging** — HTML-attribute item definition and SDKs (developer-first) vs link/button generators and hosted storefronts (merchant-first).
- **Entry-channel breadth** — website-only carts vs carts reachable from email campaigns, social posts, and marketplace listings.
- **Content-scope variants** — donations, tickets, accommodation bookings, digital downloads as first-class cart contents (nonprofit, events, hospitality uses).
- **B2B posture** — offline and purchase-order payment lanes; quote/proforma uses of the same accumulator.
- **Storefront gradient** — a hosted storefront option turns the cart platform toward the store-builder pole; recorded as a gradient, not a separate Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Checkout Platform | sibling | the cart accumulates and edits intended items before commitment; checkout turns an initiated purchase into a completed transaction. The seam is the checkout button — the cart is estimate-side, checkout is authoritative. Modern carts are mostly features of commerce platforms, and standalone cart products bundle checkout, so the two leaves are usually bundled in one product |
| E-commerce Platform | broader | owns catalog → storefront → cart → checkout → order as one system; the cart platform owns only the accumulation slice and attaches to a site the merchant already has |
| Online Store Builder | broader | builds the whole store (site + catalog + cart + checkout); the cart platform explicitly positions against it — "add a cart to the site you already have" |
| Headless Commerce Platform | adjacent | spans catalog → cart → checkout → order consumed through APIs; its cart is an internal working object, not the product's center |
| Payment Gateway / Processing Platform | downstream | the money rails the cart platform connects to; the cart platform sits upstream and never owns authorization/settlement |
| Order Management System | downstream | owns the post-order lifecycle (fulfillment orchestration, edits, returns); the cart platform's order handling is deliberately lightweight and pushes orders onward |
| Product Information Management / Catalog | adjacent | owns the rich product record; the cart platform owns no catalog of record — item data is declared at the point of sale or referenced from the seller's systems |
| Sales Order Capture | adjacent | seller-side intake of committed orders; the cart is buyer-side accumulation of uncommitted intent — the cart becomes an order at the handoff |

The boundary with the Checkout Platform is the most important one, and it was jointly reviewed from both sides: the cart is the pre-commitment accumulation and editing of intended items; checkout is the completion transaction of an initiated purchase; the seam is the checkout button. The market bundles them everywhere — every standalone cart product bundles checkout, every commerce platform bundles the cart — which is packaging, not identity.

## Representative Products

- **Snipcart** — developer-first embeddable cart: item data as HTML attributes on the seller's buy buttons, script-embedded cart, server-side crawler re-validation, hosted merchant dashboard.
- **Foxy** — hosted cart & checkout platform attached to any site, CMS, or framework; signed add-to-cart links; broad gateway connectivity; API-first with customer sync and SSO; operating since 2007.
- **Mal's e-commerce** — the classic hosted-cart pattern in its purest surviving form: buy-now links → vendor-hosted cart page → amend and checkout → email notification; free tier.
- **RomanCart** — classic hosted cart with buy buttons, floating drop-cart, optional hosted storefront, stock/price push, and marketing machinery.

The platform-internal realization of the same object model was checked against a major commerce platform's public cart API (cart object with estimated costs and a checkout-URL handoff), and against the Atlas's prior e-commerce-platform, online-store-builder, headless-commerce-platform, and checkout-platform passes, which independently recorded the cart as an owned internal structure of those Types.

## Sources

Research date: **2026-09-10**

Primary vendor surfaces:

- Snipcart — Documentation (Basics, Products, Cart summary, Security): https://docs.snipcart.com/v3/ , https://docs.snipcart.com/v3/setup/products , https://docs.snipcart.com/v3/setup/cart-summary , https://docs.snipcart.com/v3/security
- Foxy — How Foxy Works / Home: https://foxy.io/how-foxy-works , https://foxy.io/
- Mal's e-commerce — Home / How it works: https://www.mals-e.com/
- RomanCart — Home / How it works: https://www.romancart.com/
- Shopify — Storefront API Cart object (platform-internal cross-check): https://shopify.dev/docs/api/storefront/latest/objects/Cart

> Sourcing limitation: the vendor's developer wiki for one sampled product (Foxy) was not reachable from the research environment (repeated empty fetches); claims for that product rest on its product and how-it-works pages plus its own demo cart URL, and its operational API detail is intentionally not asserted. Detailed help documentation for the two legacy hosted carts was not fetched; their claims are kept at the level observed on their how-it-works surfaces. Precise vendor figures (gateway counts, account counts, request-size limits) are recorded in the Research Notes only, not asserted as Type facts.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, the joint-review disposition with the Checkout Platform pass, and the historical hosted-cart check are recorded in the paired Research Notes.
