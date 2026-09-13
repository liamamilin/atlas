# Headless Commerce Platform

## Overview

A **Headless Commerce Platform** is a transactional commerce engine — product catalog with prices, shopping cart, checkout, and order capture, with payment handled through integrated providers — that is consumed programmatically through APIs, while the customer-facing buying experience is deliberately built outside the platform as a separate frontend application.

The defining structure is small:

```text
Transactional Commerce Engine
└── consumed through APIs (buyer-facing + management)
    └── presentation decoupled: the buying experience is an external application
        └── merchant-side operation continues platform-side
```

Three properties. If any one is removed, the product is no longer recognizable as headless commerce:

- **Transactional commerce engine** — the platform's substance is selling: a sellable catalog with prices, carts that accumulate purchases, checkout that turns a cart into an order, and payment handled through connected providers. Without this, the product is content publishing (a headless CMS) or a product data feed (a PIM).
- **API as the primary consumption surface** — the engine is designed to be consumed and operated programmatically: a buyer-facing API for building shopping experiences and management APIs for operating the commerce. Without this, the product is a coupled, monolithic storefront platform.
- **Decoupled presentation** — the platform functions fully as a commerce backend with the storefront built elsewhere; any storefront tooling it ships is an optional accelerator, not the product. Without this, the product is again a monolithic e-commerce platform.

Everything else commonly associated with the category — GraphQL, cloud delivery, starter storefront frameworks, "composable commerce" architecture, hosted checkout components, channels, B2B structures — is widespread in current products but is not part of the defining core. The definition is era-neutral: an older self-hosted commerce system exposing programmatic APIs to a custom-built frontend fits it just as a modern cloud platform does.

When the platform's center of gravity shifts to shipping and owning the storefront itself (themes, page builders, bundled templates as the product), it has drifted toward a different Application Type — the monolithic E-commerce Platform.

## Users & Context

The primary users are **development teams** — frontend developers building the buying experience, backend/integration developers wiring the engine into the merchant's wider systems — typically at mid-market and enterprise retailers, or at brands whose digital experiences are built by **agencies** on their behalf.

Typical reasons to work with the platform:

- build a custom web storefront, mobile app, or other buying surface against the storefront API
- integrate commerce into an existing stack (an app, a game, a kiosk, a campaign page)
- connect orders to fulfillment, ERP, or order-management systems
- extend engine behavior (custom pricing logic, tax calculation, checkout steps) through server-side extension points

Secondary users are **merchant business users** — merchandisers, catalog managers, e-commerce managers — who continue to operate the commerce through the platform's admin: products, prices, promotions, orders, customers, settings. The decoupling concerns the buyer-facing surface only; the operations side remains a platform responsibility.

The work context is a composed stack: the commerce engine supplies transactions, while content (CMS), search, personalization, and payment providers are commonly supplied by separate systems the merchant assembles around it.

## Core Model

### The Commerce Engine's Objects

The engine's world is the standard commerce domain, exposed as API resources:

- **Product** — the sellable item, usually modeled with a type/schema of custom attributes and decomposed into **variants** (size/color/SKU-level combinations). Products are organized into **categories** or collections. Mature products commonly support staged-vs-published catalog states, per-market price books, and per-channel catalog subsets.
- **Price** — attached to products/variants, commonly contextualized by currency, region/market, customer group, or channel. A **promotion/discount engine** applies discounts inside cart totals rather than in the frontend.
- **Cart** — a persistent, engine-side object holding line items, quantities, addresses, shipping method, and computed totals (discounts and tax lines applied engine-side). The cart is the engine's working object between browsing and purchase; some engines treat carts as disposable and clean them up automatically.
- **Order** — the terminal transaction record created from a completed checkout. The order carries line items, amounts, payment and fulfillment state, and is the object downstream systems (fulfillment, OMS, ERP) consume. Order events are commonly published as webhooks.
- **Customer** — the buyer's account, with authentication commonly pluggable. Guest checkout is typically supported alongside identified customers.
- **Payment** — modeled as an integration seam: the engine orchestrates payment within checkout, while execution sits with connected payment providers (gateways/PSPs) behind connectors or provider integrations.
- **Inventory, fulfillment, tax, regions** — standard engine-adjacent structures: stock per location, shipping methods, tax configuration, multi-currency and multi-region support. Depth varies by product.
- **Channel / storefront scope** — several products model channels explicitly: named selling surfaces (a web store, a mobile app, a B2B portal, an in-store surface) that scope which products, prices, carts, and inventory belong to which surface. One engine can serve many channels.
- **Extension points** — custom fields on engine objects, plus server-side hooks (extensions, connectors, modules, functions) that run platform-side so the API contract stays intact.

### The Two API Surfaces

The engine is exposed through two distinct API tiers with different trust levels:

- **Buyer-facing (storefront) API** — read catalog, search, build and read carts, initiate checkout. Consumed from browsers and mobile apps, so its credentials are often public or tokenless with limited scope; sensitive operations are excluded from this tier.
- **Management (admin) API** — full create/update/delete over catalog, orders, customers, promotions, settings. Authenticated with scoped credentials, consumed by the merchant's integrations and admin tooling.

### One Structure, Many Implementations

The Core Model is written in conceptual terms. Common implementations vary:

```text
Concept:            Buyer-facing API style
Implementations:    GraphQL-only, REST, REST + GraphQL mixes

Concept:            Payment execution
Implementations:    redirected hosted checkout, embedded hosted checkout UI,
                    build-your-own checkout over payment APIs with PSP connectors

Concept:            Presentation decoupling
Implementations:    custom SPA/server-rendered app, starter storefront framework,
                    native mobile app, embedded buy components, kiosk/campaign surfaces

Concept:            Channel scoping
Implementations:    channel objects binding catalog/prices/carts/inventory,
                    per-channel API tokens, per-storefront catalog subsets

Concept:            Delivery model
Implementations:    multi-tenant SaaS, open-source self-hosted install,
                    vendor-hosted cloud of an open-source engine
```

A reader who has only seen one implementation (e.g., a GraphQL cloud platform with a React starter storefront) should still be able to recognize a self-hosted REST-style engine or a hybrid platform with a bundled theme system from the Core Model.

## How It Works

### Model the catalog and configure the engine

```text
Define product types/attributes
→ create products and variants
→ organize into categories/collections
→ set prices per market/currency/channel
→ configure promotions, tax, regions, shipping, inventory locations
→ (optionally) define channels and scope the catalog to them
```

This work happens through the management API or the merchant admin; the result is immediately consumable through the buyer-facing API.

### Build the buying experience against the storefront API

```text
Choose a frontend stack (custom app, starter framework, mobile app)
→ fetch products/collections and render pages
→ implement search and product discovery
→ create a cart and add line items
→ display engine-computed totals (discounts, tax, shipping)
```

The frontend owns presentation only. Prices, discounts, and tax are computed by the engine; the frontend displays them. Mature products commonly ship starter storefront frameworks and SDKs to accelerate this step — using them is optional and the resulting storefront remains external to the platform.

### Take the buyer through checkout

```text
Collect/confirm addresses and shipping method (in the external frontend)
→ hand off payment
→ order is created from the cart
```

The characteristic behavior of the Type appears at payment: **card data does not flow through the custom frontend**. Mature products commonly realize this as a redirected or embedded hosted checkout component, or as a payment component that talks to the payment provider through the platform, keeping the merchant's custom code out of PCI scope. The checkout itself may be built by the merchant (over payment APIs) or consumed as a hosted component — both are headless-compatible realizations.

### Order creation and handoff

```text
Checkout completes
→ engine creates the order (cart is consumed)
→ order confirmation to the buyer
→ order event published (webhook/event)
→ downstream systems pick it up: fulfillment, OMS, ERP, notifications
```

The engine's order role is capture and lifecycle-light management; deep post-order orchestration belongs to order-management systems connected downstream.

### Operate the commerce

```text
Merchant admin / management API
→ catalog and price changes appear through the API to every channel
→ promotions configured once apply engine-side
→ orders monitored and managed
→ extension points adjust engine behavior (custom pricing, tax, checkout logic)
```

The operating loop is continuous: business users change the commerce in the admin; every external frontend reflects the change through the API without redeployment.

### Capability tiers

**Defining core** — without these, not a headless commerce platform:

- transactional engine: catalog with prices, cart, checkout-to-order, payment through integrated providers
- buyer-facing API and management API as the primary surfaces
- decoupled presentation: the platform works fully with an external buying experience
- merchant-side operation (management APIs; in practice an admin dashboard)

**Standard capabilities** — present in most mature products:

- product/variant modeling with custom attributes; categories
- promotion/discount engine; customer accounts with pluggable auth
- inventory with locations; shipping methods; tax and multi-currency/regions
- channel/storefront scoping (several products model channels explicitly)
- webhooks/event subscriptions; server-side extension points; extensible custom fields
- merchant admin dashboard; SDKs in multiple languages; API explorers; sandbox/mock environments
- starter storefront frameworks and optional hosting; product search/discovery surfaces
- order lifecycle APIs and integration seams to fulfillment/OMS/ERP

**Optional / advanced** — depends on segment and product:

- B2B structures (company accounts, quotes, customer-specific pricing) in enterprise-class products
- hosted checkout as a packaged product with PSP connector marketplaces
- multi-vendor marketplace capability; subscriptions/selling plans; digital goods
- in-store selling surfaces; agentic-commerce surfaces (AI assistants, agent-facing API access)
- bulk import/export tooling; audit/change-history APIs

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Buyer-facing API

The Type's defining interface — a programmatic surface, not a page.

- Purpose: let external applications render catalogs, build carts, and initiate checkout.
- Typical shape: documented schema (GraphQL or REST), versioned, with query/filter/pagination conventions.
- Primary consumers: the merchant's storefront frontend, mobile apps, other channels.

### Management API

- Purpose: programmatic operation of the engine — catalog, orders, customers, promotions, settings.
- Typical shape: authenticated, scoped credentials; full CRUD; often bulk/import endpoints.
- Primary consumers: merchant integrations, ERP/PIM sync, admin tooling.

### Merchant admin dashboard

- Purpose: business-user operation of the commerce.
- Typical information: products and variants, prices, promotions, orders and their states, customers, channel/store settings.
- Primary actions: create/edit products, configure promotions and shipping/tax, inspect and manage orders, manage users and API credentials.

### Checkout components (optional)

- Purpose: consume checkout without building it.
- Typical shape: hosted checkout page reached by redirect, or an embeddable payment/checkout UI (browser SDK) placed inside the external frontend.
- Primary actions: enter address/shipping, select and enter payment method, complete the order.

### Developer tooling

- Purpose: make the API surface productive.
- Typical shape: SDKs/client libraries, API explorers/playgrounds, sandbox or mock stores, CLI tooling, documentation portals.

## Important Rules / Behaviors

### Card data stays off the custom frontend

The decoupled storefront is merchant-written code; mature products deliberately keep payment card data out of it — via redirected/embedded hosted checkout or platform-mediated payment components. This is a structural behavior of the Type, not a feature toggle.

### Two trust tiers on the API surface

Buyer-facing API credentials are commonly public or tokenless and carry limited scope; management credentials are secret and scoped. Sensitive operations (customer data, order management) are excluded from the buyer-facing tier. Integrations must respect this split.

### The engine computes commerce truth

Totals, discounts, and tax are computed engine-side; the frontend displays but does not decide. A frontend that computed its own prices would break the model — promotions and price books must apply uniformly across channels.

### Carts are working objects; orders are the record

Carts are mutable and in some engines automatically cleaned up if abandoned; the order is the durable transaction record created at checkout completion. Order information commonly reaches integrations through webhooks/events rather than by polling carts.

### The decoupling contract

Platform changes reach external frontends only through the versioned API. Mature products therefore version their APIs and publish changes deliberately; merchants upgrade on their own schedule. Server-side extension points exist precisely so custom behavior can run platform-side without breaking the contract.

### Channel scoping governs visibility

Where channels are modeled, product availability, prices, carts, and inventory can be scoped per channel — one engine serving a web store, an app, and a B2B portal with different assortments. Exact channel semantics vary by product.

## Variants

Common shapes of the Type:

- **Pure-play API-first SaaS ("composable commerce")** — enterprise-oriented; no default storefront; optional frontend tooling; deep B2B and multi-brand structures.
- **Open-source self-hosted engine** — installable application the merchant runs and customizes; optionally with vendor-hosted cloud; customization framework as a first-class part.
- **"Open SaaS" hybrid** — SaaS platform that ships both a coupled theme storefront and a fully headless API surface plus a composable storefront framework.
- **Monolith-with-headless-option** — a dominant storefront-first platform exposing a storefront API and headless framework as an additional mode; checkout typically remains platform-hosted.
- **B2B headless** — company accounts, buyer hierarchies, quotes, customer-specific pricing layered on the same engine.
- **Composable-ecosystem pole** — the engine deliberately narrow (transactions only), with content, search, and personalization composed from separate best-of-breed systems.

A variant remains a variant as long as the defining core holds: engine + API-primacy + external presentation. If a product's storefront becomes required and primary, it has crossed into the monolithic E-commerce Platform Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| E-commerce Platform | adjacent (sharpest boundary) | centers on shipping/owning the coupled storefront; headless capability may exist but is not the product's center. Market reality is a spectrum — dominant platforms ship both postures |
| Online Store Builder | adjacent | no-code storefront creation for merchants; the storefront is the product, APIs secondary |
| Headless CMS | complementary | delivers content items via APIs with no transactional semantics; commonly composed alongside a commerce engine in the same storefront |
| Checkout Platform | narrower | owns the checkout slice as a standalone service; a headless commerce platform spans catalog → order and may itself consume a checkout component |
| Shopping Cart Platform | narrower | cart/checkout mechanics without the full catalog-to-fulfillment span |
| Product Information Management / PIM | complementary | master-data system for product content and enrichment; the commerce engine prices and sells, and integrates PIM for data |
| Order Management System / OMS | downstream | orchestrates post-order lifecycle across sources/locations; the commerce engine captures the order and hands it off |
| Payment Orchestration / Payment Gateway | complementary | PSP connectivity and money movement; the commerce platform orchestrates the transaction and delegates execution via connectors |
| API Management Platform | different domain | manages API infrastructure in general; here the APIs are the product's delivery mechanism, not the managed subject |

## Representative Products

- **commercetools** — pure-play API-first "composable commerce" SaaS; enterprise tier; no default storefront, optional frontend tooling.
- **Shopify (Storefront API + Hydrogen)** — the dominant storefront-first platform's headless surface: GraphQL storefront API, official headless framework, checkout kept platform-hosted.
- **Medusa** — open-source, self-hostable commerce platform with a customization framework; developer/startup tier, managed cloud available.
- **BigCommerce** — mid-market "open SaaS": bundled theme storefront plus a fully headless GraphQL API and a composable storefront framework.

The defining core was checked across these four deliberately different philosophies (pure headless enterprise, dominant-platform headless add-on, open-source self-host, SaaS hybrid) to avoid over-fitting to any one delivery model or API style.

## Sources

Research date: **2026-09-07**

- commercetools — Documentation root: https://docs.commercetools.com/ ; API General Concepts: https://docs.commercetools.com/api/general-concepts ; Checkout Overview: https://docs.commercetools.com/checkout/overview
- Shopify — Storefront API reference: https://shopify.dev/docs/api/storefront ; Headless overview: https://shopify.dev/docs/storefronts/headless ; Migrate to the Storefront Cart API: https://shopify.dev/docs/custom-storefronts/checkout
- Medusa — Documentation root: https://docs.medusajs.com/ ; Cart Module: https://docs.medusajs.com/resources/commerce-modules/cart ; Sales Channel Module: https://docs.medusajs.com/resources/commerce-modules/sales-channel
- BigCommerce — Developer docs root: https://developer.bigcommerce.com/docs ; Catalyst: https://developer.bigcommerce.com/developer/docs/storefront/catalyst

> Assertion calibration: findings rest on official documentation observed 2026-09-07 (one to three key pages per product). Cross-product commonalities are stated as common; single-product behaviors (e.g., specific channel semantics, specific checkout realizations) are stated as product-dependent. Precise operational limits, version dates, and vendor-specific tooling names are intentionally omitted from this document and recorded in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
