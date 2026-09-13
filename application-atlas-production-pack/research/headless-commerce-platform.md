# Research Notes — Headless Commerce Platform

## Research Goal

Understand what a Headless Commerce Platform actually is as an Application Type: what its commerce engine contains, how the decoupling between commerce backend and customer-facing frontend works in real products, what the purchase flow looks like when consumed over APIs, what merchant-facing operation continues to exist when the storefront is external, and where the boundary lies against monolithic e-commerce platforms, headless CMS, checkout platforms, PIM, and order management.

## Initial Boundary

Working hypothesis before research:

- Core use: run transactional commerce (catalog → cart → checkout → order → payment) behind programmatic APIs, with the merchant building and owning the customer-facing buying experience outside the platform.
- Likely users: frontend/backend development teams, digital agencies building storefronts for brands, plus merchant business users who still operate catalog/promotions/orders through an admin.
- Nearest neighbors: E-commerce Platform (monolithic, coupled storefront), Online Store Builder, Headless CMS (content only, no transactions), Checkout Platform (checkout slice), Shopping Cart Platform, PIM (product data master), Order Management System (post-order), Payment Orchestration/Gateway (money rails).
- Open questions going in: Is "API-first" definitional or merely common? Is payment execution part of the engine or an integration seam? Is a merchant admin UI required when the storefront is decoupled? Is the modern "composable/MACH" framing part of the Type or just the current market era?

## Research Questions

- RQ1: What commerce objects does a headless engine expose (product/variant/price, cart, order, customer, promotion, payment, inventory, channels)?
- RQ2: What is the end-to-end purchase flow when the storefront is external (catalog fetch → cart → checkout → order)?
- RQ3: How is payment modeled — platform-executed, connector-integrated, or redirected to hosted checkout? Where does card data live?
- RQ4: How do platforms model multiple channels/storefronts against one engine?
- RQ5: What merchant-side operation surfaces exist when the storefront is decoupled?
- RQ6: What is explicitly in and out of scope (content, search, fulfillment, tax, OMS)?
- RQ7: What delivery models exist (SaaS API-first, open-source self-hosted, hybrid "open SaaS", monolith-with-headless-option)?
- RQ8: What are the boundary tests against each neighboring Type?

## Representative Products

Selected for market representativeness, documentation quality, and deliberately different product philosophies and customer tiers:

| Product | Philosophy / pole | Customer tier | Docs used |
|---|---|---|---|
| commercetools | Pure-play API-first "composable commerce" SaaS; no default storefront, optional frontend tooling | Enterprise | docs.commercetools.com (root, API general concepts, Checkout overview) |
| Shopify (Storefront API + Hydrogen) | Dominant coupled-storefront platform exposing a first-class headless surface (Storefront API, Hydrogen framework, hosted web checkout kept) | SMB → enterprise | shopify.dev (Storefront API reference, Headless overview, Cart API migration) |
| Medusa | Open-source, self-hostable commerce platform with a customization framework; modular engine | Startups / developers → mid-market | docs.medusajs.com (root, Cart module, Sales Channel module) |
| BigCommerce | Mid-market SaaS "open SaaS": ships a bundled theme storefront AND a fully headless GraphQL API + composable storefront framework | Mid-market / retail | developer.bigcommerce.com (docs root, Catalyst overview) |

This sample spans: pure headless enterprise, dominant-platform headless add-on, open-source self-host, and SaaS hybrid. All four fetched 2026-09-07 (Tier 1 official documentation).

## Sources

Research date: 2026-09-07. All sources fetched live; no source-access limitations this pass.

- commercetools — Documentation root: https://docs.commercetools.com/ ; API General Concepts: https://docs.commercetools.com/api/general-concepts ; Checkout Overview: https://docs.commercetools.com/checkout/overview
- Shopify — Storefront API reference: https://shopify.dev/docs/api/storefront ; Headless overview: https://shopify.dev/docs/storefronts/headless ; Migrate to the Storefront Cart API: https://shopify.dev/docs/custom-storefronts/checkout
- Medusa — Documentation root: https://docs.medusajs.com/ ; Cart Module: https://docs.medusajs.com/resources/commerce-modules/cart ; Sales Channel Module: https://docs.medusajs.com/resources/commerce-modules/sales-channel
- BigCommerce — Developer docs root: https://developer.bigcommerce.com/docs ; Catalyst: https://developer.bigcommerce.com/developer/docs/storefront/catalyst

## Product Observations

### commercetools

Evidence layer: A (direct observation of official docs).

- Self-presentation as API-first commerce: docs root is organized around APIs (API Reference, Concepts, Carts/Orders/Payments/Customers/Products APIs as "popular pages"), SDKs, Merchant Center, Checkout, Connect, Frontend, InStore.
- **Project** is the top-level container; all resources belong to a Project, isolated between projects. Per-region SaaS deployment (multiple isolated cloud regions).
- Engine resource model observed in API docs: **Products** (Product Types with attribute definitions, variants, staged/current masterData, categories, tax categories), **Carts**, **Orders**, **Payments**, **Customers**, **Shopping Lists**, **Inventory** (InventoryEntry with availability; inventory modes incl. reserve-on-order/track-only/reserve-on-cart), **Channels** and **Stores** (multi-channel/multi-store modeling), **Business Units** (B2B structures), **Product Selections** (per-store catalog subsets), standalone prices with discounts, **Custom Types/Custom Fields** (extensible fields on resources), Custom Objects (arbitrary JSON key-value storage).
- API mechanics: OAuth 2.0 bearer tokens with scopes (project-management scope grants all); resources are **versioned with optimistic concurrency** (update requires expected version; ConcurrentModification error); typed **update actions** per resource; reference expansion; query predicates; pagination; bulk **Import API**; Change History (audit) API; Messages; **API Extensions** (server-side callouts into API flows, e.g., external tax calculation service shown in the correlation-ID example).
- **Merchant Center** = the merchant-facing web admin (accounts, product types, import/export, checkout configuration, connector management, customizations). Admin continues to exist although the storefront is external.
- **Checkout** is a separate product with two modes: **Complete Checkout** (entire checkout UI, hosted: addresses, shipping method, payment method, terms, order summary) and **Payment Only** (keep existing checkout flow, use hosted payment component that talks to PSPs and creates the order via Carts/Orders APIs). Integration through **Connectors** (marketplace PSP integrations: Adyen, PayPal, Stripe; custom "Organization Connectors"); Browser SDK embeds the checkout UI as overlay or inline; applications configured per brand/country in Merchant Center; PCI DSS compliance claimed as handled.
- Frontend tooling exists but is optional: "Frontend Development" docs area, Frontend SDKs, Store Launchpads, Frontend Studio (storefront builder). Also InStore (in-store selling surface), MCP servers and an "Agentic Commerce" area (AI Hub, AgenticLift).
- Precise operational facts observed (NOT to be promoted to the final doc): default cart retention 90 days (configurable); request URL+headers limit ~15 KB; pagination offset max 10 000; background-update JSON doc size limit 16 MB; refresh-token validity 200 days default; minimum TLS 1.2; isolated regions list (GCP/AWS US/EU/AU); "reduce 50 API calls to 3" checkout marketing claim.

### Shopify (headless surface: Storefront API + Hydrogen)

Evidence layer: A.

- Storefront API framed as "commerce primitives to build custom, scalable, and performant shopping experiences" on any platform "including the web, apps, and games": view products/collections, add to cart, check out. **GraphQL-only** for storefronts ("There's no REST API for storefronts"); versioned API with periodic releases; single endpoint per store.
- Trust-tiered storefront access: **tokenless access** (limited feature set: products/collections, selling plans, search, pages/blogs/articles, cart read/write; query-complexity limited) vs **public token** (browser/mobile, buyer-visible) vs **private token** (server-side, secret; requires buyer-IP header for bot protection/fraud). A "Headless channel" in the Shopify admin provisions storefronts and tokens.
- Storefront-facing objects observed: products, collections, selling plans (subscriptions), search, pages/blogs/articles, menus, metaobjects/metafields, **cart** (read/write), customers. `@inContext` directive contextualizes queries by country, language, buyer identity (incl. B2B: customer access token + company location), and visitor consent.
- **Checkout seam**: the cart object carries a `checkoutUrl`; the documented pattern is that headless carts **redirect to Shopify's Web Checkout** (framed as a benefit: "Unified functionality — The Storefront Cart API redirects to Shopify's Web Checkout"). REST Checkout APIs are deprecated (2024-04) and sunset (2025-04) in favor of the Cart API + **Checkout Kit** mobile SDKs. Completed carts are deleted on order creation; order information arrives via **webhooks**.
- Frameworks/tooling: **Hydrogen** ("Shopify's official React-based framework for building headless commerce"), **Oxygen** (free edge hosting for Hydrogen), "Bring your own stack" (any language/framework/host), Storefront Web Components (embeddable HTML buy surfaces), custom-storefront apps (search, personalization, content management), GraphiQL explorer, mock.shop (mock data store for building without a store).
- Traffic rules: buyer traffic scales (no fixed requests-per-minute for legitimate buyers); automated/bot traffic rate-limited; security rejections for malicious-looking requests.
- Terms-level rule observed: "You can't use Storefront API to duplicate existing Shopify functionality" (headless mode must not replace the platform's admin/checkout wholesale).
- Precise operational facts observed (notes only): tokenless complexity limit 1000; max 100 active storefront tokens per shop; quarterly API versioning; specific sunset dates; HTTP 430 security rejection; buyer-IP header name.

### Medusa

Evidence layer: A.

- Self-description: "a digital commerce platform with a built-in Framework for customization. When you install Medusa, you get a fully fledged commerce platform…" Installable application; self-hosted or **Medusa Cloud** (deploy from GitHub, preview environments). Delivery model pole: open-source self-host.
- **Commerce modules** (the engine decomposed): Cart (line items, addresses, shipping methods; promotion adjustments as adjustment lines; tax lines; carts scoped to sales channel + region + customer), Payment ("process any payment type"), Customer (+ groups), Product (variants, categories, bulk edits), Pricing ("configurable pricing engine"), Promotion, Order ("omnichannel order management"), Inventory (multi-warehouse, reservations), Fulfillment, Stock Location, Region (cross-border), **Sales Channel** (online or offline channel; product availability per channel; carts and orders scoped to channels; inventory availability per channel via stock-location links), Tax, Currency, API Keys (store and admin access), User (admin users), Auth (pluggable authentication).
- Customization framework: custom API routes (REST-style), **Workflows** (composed steps with rollback/compensation guarantees), Data Model Language (custom data models), custom modules, module links, event subscribers (e.g., order.placed → send notification).
- **Storefront development** is an explicit external activity: Next.js storefront starter template; "Build custom storefront" guides; AI-agent storefront best practices. The storefront is not part of the core install.
- **Admin dashboard** exists for merchants and is extensible (widgets in predefined zones, custom UI routes, admin user guide). Recipes document marketplace (multi-vendor), ERP integration, bundles, subscriptions, restaurant-delivery, digital-products use cases.
- Precise operational facts observed (notes only): code-level workflow/DML mechanics; Bloom AI assistant; docs MCP server.

### BigCommerce

Evidence layer: A.

- Self-description: "open SaaS" — "blending the flexibility of open source with the usability and security of SaaS… without the constraints of a SaaS monolith." SaaS-delivered platform with compliance certifications (PCI, ISO, SOC, etc.).
- **Two storefront postures shipped by one platform**: Stencil themes (coupled theme storefront) OR "go fully headless with the GraphQL Storefront API". **Catalyst** = "the composable, fully customizable headless ecommerce storefront framework" (Next.js + React components over the GraphQL Storefront API; MIT-licensed; deployable to any Node.js host; demo hosted on Vercel).
- Catalyst's B2C funnel (evidence of what a headless storefront must build itself): home page, PLPs with faceted search per category/brand, full-text search, PDPs "published to the Catalyst storefront channel", shopping cart, "secure **redirected headless checkout** page… on our hosted SaaS environment to simplify PCI compliance. By default, your headless storefront never collects or transmits personally identifiable information (PII) such as credit card numbers", customer accounts.
- API surface split: **REST Management APIs** (catalog products, orders, customers, store settings — the admin-side engine), **REST Storefront Cart & Checkout APIs** (custom checkouts), **GraphQL Storefront API** (site/products/prices; storefront tokens carrying `channel_id`, CORS origins, expiry), Customer Login API, **Webhooks** ("real-time store event notifications").
- Operation: sandbox/trial stores for development; API accounts with scopes; in-browser Request Runner; OpenAPI specs for Postman. Control panel = merchant admin; "Our hosted control panel and bundled storefront are how most brands interact with BigCommerce."
- **B2B Edition**: company accounts, quotes, custom pricing for wholesale/enterprise buyers.
- Precise operational facts observed (notes only): storefront token constraints (single channel ID accepted, single CORS origin in example), expiry timestamps.

## Cross-product Comparison

| Dimension | commercetools | Shopify (headless) | Medusa | BigCommerce | Strength |
|---|---|---|---|---|---|
| Delivery model | Multi-region SaaS, project-isolated | Multi-tenant SaaS | Open-source install / managed cloud | Multi-tenant SaaS ("open SaaS") | B: varies by design |
| Default coupled storefront | None shipped (optional Frontend tooling) | Yes (themes) + headless surface | None shipped (starter template only) | Yes (Stencil themes) + headless surface | B: the axis itself varies |
| Buyer-facing API | HTTP API (+ SDKs) | GraphQL-only storefront API | REST-style API routes (+ SDKs) | GraphQL Storefront API + REST storefront cart/checkout | B: API style varies, API-primacy constant |
| Management/admin API | Yes (full engine APIs, OAuth scopes) | Yes (Admin API) | Yes (admin API + API keys) | Yes (REST Management APIs) | B: constant |
| Merchant admin UI | Merchant Center | Shopify admin (+ Headless channel) | Admin dashboard (extensible) | Control panel | B: constant |
| Catalog modeling | Product types/attributes, variants, staged/current, categories, product selections | Products/collections, metafields/metaobjects | Product module (variants, categories) | Catalog products (REST) | B: common with different depth |
| Cart | First-class API resource (persistent, retention-managed) | Cart object in storefront API | Cart module (scoped to channel/region/customer) | Storefront cart APIs | B: constant |
| Payment | Payments API + hosted Checkout product + PSP Connectors | Redirect to hosted web checkout; Checkout Kit SDKs | Payment module "process any payment type" (provider integrations) | Redirected hosted checkout; payment via platform/PSP | B: implementation varies, card-data-off-storefront constant |
| Order creation | Order from cart via API (typed flows) | On hosted checkout completion (cart deleted; order via webhook) | Complete-cart → order (workflow) | Checkout completion creates order | B: constant pattern |
| Channels / multi-store | Channels + Stores + Product Selections | Not directly observed in fetched pages | Sales Channel module (products/carts/orders/inventory per channel) | channel_id in storefront tokens; Catalyst storefront channel | B (3/4 observed) |
| Promotions/discounts | Discounts/standalone prices | Discounts in cart (stackable codes) | Promotion module | Discounting in management APIs | B: constant |
| Inventory | InventoryEntry, reservations modes | Not detailed in fetched pages | Inventory module (multi-warehouse, reservations) | Inventory via catalog APIs | B: common |
| Fulfillment | Order fulfillment state machine (API docs area) | Shipping/fulfillment platform-side; not detailed here | Fulfillment + Stock Location modules | Shipping via management APIs | B: common, depth varies |
| B2B structures | Business Units, B2B learning path | Buyer context incl. company location | Recipe-level (customer groups) | B2B Edition (company accounts, quotes, custom pricing) | B: segment-dependent |
| Webhooks/events | Subscriptions (notifications) | Webhooks for orders | Subscribers (events) | Webhooks | B: constant |
| Extension points | API Extensions (server-side callouts), Custom Fields, Connect runtime | Apps, Functions, metafields | Modules/workflows/routes/subscribers | Apps, checkout extension | B: constant in kind |
| Starter storefronts | Launchpads/Frontend Studio (optional) | Hydrogen (+ Oxygen hosting) | Next.js starter | Catalyst | B: common as optional accelerator |
| Content/CMS | Not in engine (compose externally) | Pages/blogs in API; CMS via apps | Not in engine | Not in engine | B: commerce engine does not own marketing content |
| Search/discovery | Product Search / Projection Search | Storefront search | Not observed in fetched pages | Faceted search in Catalyst; search APIs | B: common |
| AI/agentic era additions | MCP servers, AI Hub, AgenticLift | (mock.shop; not prominent in fetched pages) | Bloom assistant, docs MCP | MCP server, AI search/chat in docs | B: era-common |

## Canonical Abstraction

### Level 0 — Defining Invariant

The smallest structure without which the product stops being a Headless Commerce Platform:

1. **Transactional commerce engine** — the platform runs catalog-with-pricing, cart, checkout-to-order, and payment handling through integrated providers as its substance. Remove this and the product is content publishing (headless CMS) or a data feed (PIM).
2. **API as the primary consumption surface** — the engine is consumed programmatically through a buyer-facing API and management APIs; the platform is designed to be operated and sold-through via these interfaces, not via a bundled page system. Remove this and the product is a coupled (monolithic) e-commerce platform.
3. **Deliberately decoupled presentation** — the platform functions fully as a commerce backend with the buying experience built outside it; any storefront tooling it ships is optional and disposable. Remove this (presentation becomes platform-owned and required) and it is again a monolithic storefront platform, not headless commerce.

Structural implication of "platform": merchant-side operation must remain possible platform-side (management APIs; in practice a merchant admin UI). Without any operation surface it would be a commerce library, not a platform. The admin UI is the common implementation of this, not the invariant itself.

### Level 1 — Common Mature Structure

Present across the sampled products, expected in the market, but not definitional:

- product/variant catalog modeling with custom attributes/types and categories
- promotion/discount engine applied inside cart totals
- customer accounts with pluggable authentication
- inventory with locations/reservations (depth varies)
- shipping methods and fulfillment configuration/handoff
- tax configuration, regions and multi-currency
- channel/storefront scoping (catalog, prices, carts, inventory per channel) — observed in 3/4 products
- webhooks / event subscriptions for order and catalog events
- server-side extension points (extensions, connectors, modules, functions) and extensible custom fields
- merchant admin web dashboard
- SDKs/client libraries in multiple languages; API explorers/playgrounds; sandbox or mock environments
- starter storefront frameworks and optional hosting (accelerators, never required)
- product search/discovery surfaces
- order lifecycle API and integration seams to OMS/ERP/fulfillment systems
- B2B structures (company accounts/business units, quotes, customer-specific pricing) in enterprise-class products

### Level 2 — Variant / Optional Structure

Depends on segment, era, deployment, business model:

- delivery model: multi-tenant SaaS vs open-source self-hosted (optionally with vendor cloud) vs "open SaaS" hybrid
- API style: GraphQL-only storefront vs REST vs REST+GraphQL mixes
- storefront tooling depth: pure API only vs starter frameworks vs embedded buy components vs (in hybrids) a still-shipped theme system
- checkout realization: redirected hosted checkout vs embeddable hosted checkout UI vs build-your-own over payment APIs
- B2B depth; multi-vendor marketplace capability (recipe/module level in some products)
- subscriptions/selling plans; digital goods; in-store selling adjacency
- compliance posture (PCI offloading claims), regional data isolation
- agentic-commerce surfaces (MCP servers, AI assistants) — era-common, not definitional

### Level 3 — Vendor-specific Structure

Research-notes only: Merchant Center, Checkout Applications/Connectors, Frontend Studio/Launchpads, InStore, AI Hub/AgenticLift (commercetools); Hydrogen/Oxygen, Headless channel, mock.shop, Storefront Web Components, Checkout Kit, @inContext directives, token tiers, 430 rejection code (Shopify); module list, Bloom, DML/workflow mechanics, Next.js starter (Medusa); Catalyst, Stencil, B2B Edition, Request Runner, storefront-token constraints (BigCommerce); all precise limits and dates (cart retention 90d, URL size ~15 KB, tokenless complexity 1000, quarterly API versions, sunset dates, token counts, TLS floors, region lists, CORS/channel-token constraints).

## Rejected Findings

Candidate "core" claims investigated and rejected:

- "Headless commerce = GraphQL" — rejected. GraphQL-only is a Shopify storefront trait; Medusa exposes REST-style routes; commercetools documents an HTTP API. API style is implementation, not structure.
- "Headless commerce = SaaS/cloud-native" — rejected. Medusa is self-hostable by design; delivery model varies.
- "Headless commerce = JAMstack/static storefronts" — rejected. Storefront technology is the merchant's choice; the platform does not define it.
- "Headless = no admin UI" — rejected. All four products ship merchant admin surfaces; decoupling concerns the buyer-facing presentation only.
- "MACH/microservices architecture is definitional" — rejected. Architecture posture varies (Medusa ships a modular application; BigCommerce brands itself anti-monolith but SaaS). What is definitional is the API contract, not the internal architecture.
- "One engine = one storefront" — rejected. Channel/multi-storefront modeling is common (3/4 products observed).
- "The platform processes payments itself" — rejected. Payment execution sits with PSPs behind connectors/gateways/hosted components; the platform orchestrates payment within checkout and keeps card data off the custom frontend.

## Boundary Findings

- **vs E-commerce Platform (§05.01 sibling)**: The sharpest and least clean boundary. A monolithic e-commerce platform centers on shipping/owning the storefront (themes/pages as the product); a headless commerce platform centers on exposing the engine. Market reality is a **spectrum**: dominant platforms (Shopify, BigCommerce) now ship first-class headless surfaces alongside their storefronts, and pure-play headless vendors ship optional storefront tooling. Working seam: **primary posture** — is the coupled storefront the product's center (monolith) or a disposable convenience while the engine+API is the product (headless)? Removal test: "can the product be used with no storefront from the platform at all, by design?" — yes for headless, no (or off-product) for monolith. Recommend joint review with the e-commerce-platform leaf when processed.
- **vs Headless CMS (§02.07)**: Headless CMS delivers content items/entries via APIs with no transactional semantics (no cart/order/payment). The two are complementary and commonly composed: the external storefront fetches content from a headless CMS and commerce from the commerce engine. Removal test: remove transactional commerce → headless CMS territory.
- **vs Checkout Platform (§05.06) / Shopping Cart Platform (§05.06)**: The checkout platform owns the checkout slice (often as an embeddable service); the headless commerce platform spans catalog → cart → checkout → order → fulfillment handoff. Headless platforms can even *consume* a standalone checkout component (observed as hosted-checkout products/modes inside two sampled platforms).
- **vs Product Information Management / PIM (§05.04)**: PIM is the master-data system for product content (enrichment, syndication); the commerce engine is the transactional system that prices and sells. Headless engines carry a sellable catalog and integrate PIM for enrichment (observed as ERP/PIM integration recipes).
- **vs Order Management System / OMS (§05.07)**: OMS orchestrates post-order lifecycle across sources/locations; headless commerce captures the order and hands it off (webhooks/integrations). Order objects inside headless engines are capture/lifecycle-light compared to OMS orchestration.
- **vs Payment Orchestration / Payment Gateway (§08)**: PSP connectivity and money movement are delegated to connected providers via connectors; the commerce platform owns the commerce transaction, not the rails.
- **vs API Management Platform (§14)**: The APIs are the product's delivery mechanism, not the product; an API-management platform manages any API. Boundary holds trivially.

## Historical / Market-Sample Check

The sampled products are all current-generation. Structural check against older/regional/differently-positioned commerce systems:

- The three defining properties (transactional engine + API-primary consumption + external presentation) are era-neutral. Nothing in the definition requires GraphQL, cloud SaaS, JAMstack, or the "composable/MACH" framing — all of those are current-era implementations (Level 2/3).
- Older self-hosted commerce systems that exposed programmatic APIs to custom frontends fit the definition structurally; the "headless" label is the market's recent naming of the posture. (This historical fit is reasoned structurally; no pre-headless-era product documentation was fetched this pass, so the claim is kept low-strength and generically phrased.)
- Conversely, a theme-and-page store builder with weak/no commerce APIs does not fit, regardless of era — supporting that API-primacy (not modernity) is the invariant.

Conclusion: the abstraction survives the historical check; no re-abstraction needed.

## Uncertainties

- One to three documentation pages observed per product; catalog modeling depth (e.g., staged-vs-published semantics, price books) verified directly only at commercetools; treated as common-with-variance elsewhere.
- Channel modeling observed at 3/4 products; Shopify's channel semantics were not directly observed in fetched pages, so the channel claim is deliberately capped at "several products model channels explicitly".
- Medusa payment-provider integration mechanics ("process any payment type") not deep-verified below module level.
- commercetools' GraphQL API surface was not directly verified in fetched pages (HTTP API documented); GraphQL presence at commercetools left unstated.
- Pricing/packaging, marketplace app ecosystems, and SLA details were out of scope.
- Historical fit (pre-"headless"-era products) is a structural inference, not documented from archived sources.

## Final Synthesis

A Headless Commerce Platform is a transactional commerce engine — product catalog with prices, cart, checkout-to-order, and payment handling through integrated providers — that is consumed programmatically through APIs as the primary surface, with the customer-facing buying experience deliberately built outside the platform. The merchant operates the commerce (catalog, promotions, orders, configuration) through the platform's admin/management side while frontends, apps, and other channels are composed on top of the buyer-facing API. Mature products add catalog modeling depth, promotions, customers, inventory, fulfillment and tax configuration, channel scoping, webhooks, server-side extension points, admin dashboards, SDKs, sandboxes, and optional starter storefronts — none of which are required to recognize the Type. The defining contrast is with the monolithic e-commerce platform, where the storefront is the product; in headless commerce the storefront is by design somebody else's application. The boundary is a posture spectrum in the current market (dominant platforms ship both), which is recorded as a taxonomy flag for joint review with the E-commerce Platform leaf.
