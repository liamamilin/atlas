# Research Notes — E-commerce Platform

## Research Goal

Understand what an E-commerce Platform actually is as an Application Type: the core objects it maintains, the buying flow it operates for shoppers, the merchant-side operation it runs, which interfaces each side uses, which states and rules matter, and where its boundary lies against the neighboring Types in §05.01 (Online Store Builder, Headless Commerce Platform, Mobile Commerce Application) and the wider commerce cluster (Marketplace Platform, Checkout Platform, Shopping Cart Platform, B2B E-commerce Platform, Cross-border Commerce Platform, Subscription/Digital-goods/Dropshipping platforms, OMS/PIM/Inventory siblings).

## Initial Boundary

Working hypothesis before research:

- The E-commerce Platform is the merchant-side software platform for running an online store: product catalog + customer-facing storefront + cart/checkout + payment + order management, operated from one system.
- Closest neighbors and expected seams:
  - Online Store Builder — probably template-first packaging of the same Type (alias/variant risk).
  - Headless Commerce Platform — API-first engine posture; prior pass (§05.01, processed 2026-09-07) pre-hung a joint-review flag naming this leaf.
  - Marketplace Platform (§05.02, processed) — multi-seller venue vs single-merchant selling operation; its L0 remove-test already names "single-merchant e-commerce platform software".
  - Checkout Platform (§05.06, processed) — stand-alone buyer-facing completion stage vs owned checkout inside a full selling operation.
  - B2B E-commerce Platform (§05.17, processed) — account-mediated selling vs anonymous public retail.
  - Cross-border Commerce Platform (§05.24, processed) — border-machinery test pre-recorded for this pass to apply.
  - Mobile Commerce Application (§05.01, unprocessed) — buyer-side mobile surface; expected variant.
- Unknowns: whether "platform" implies hosting/SaaS (open-source products may falsify), whether customer accounts/inventory/promotions belong in the definition, and the exact shape of the merchant-side order lifecycle across products.

## Research Questions

1. What objects must exist before a merchant can sell? (products, categories, prices, variants…)
2. What does the shopper-facing side look like, and who operates it — the platform or a third-party frontend the merchant composes?
3. How does a purchase flow: browse → cart → checkout → payment → order? Which steps are owned by the platform?
4. What happens to an order after purchase? What lifecycle states exist, and what do they drive (stock, emails, fulfillment)?
5. What does the merchant work in day-to-day (admin surface) and what roles exist?
6. Which capabilities are universal vs plan/segment/extension-dependent (payments, inventory, accounts, promotions, tax, shipping, analytics)?
7. Where do storefront posture (coupled themes vs headless APIs), deployment posture (SaaS vs self-hosted vs plugin) and channel breadth (POS, social, mobile, B2B, multi-market) fit — defining structure or variant?
8. Historical/market check: would pre-SaaS shopping-cart platforms and regional/open-source shop systems still fit the definition?

## Representative Products

Selected for market representation, documentation quality, distinct product philosophy, and distinct customer tiers:

| Product | Philosophy / posture | Customer tier |
|---|---|---|
| Shopify | Hosted SaaS, storefront-first, platform-operated checkout, app/theme ecosystems | SMB → enterprise |
| BigCommerce | Open SaaS; bundled storefront + control panel with first-class APIs and storefront-option matrix | Mid-market → enterprise |
| WooCommerce | Free open-source plugin on WordPress; merchant assembles hosting, design, extensions | SMB → mid-market (self-managed) |
| Adobe Commerce / Magento Open Source | Enterprise commerce application; on-premises, cloud PaaS, and SaaS deployment poles; deep admin | Enterprise (and open-source self-hosters via Magento Open Source) |

Rejected as primary samples: Wix/Squarespace (template-first, better anchors for the online-store-builder sibling; docs script-rendered risk), PrestaShop/OpenCart/osCommerce (used for the historical check conceptually, not fetched), commercetools/Medusa (already sampled by the headless pass).

## Sources

All fetched 2026-09-08 (Layer A = direct observation of official operational documentation; Layer B = cross-product commonality; Layer C = canonical inference):

- Shopify — https://www.shopify.com/ (product page, Tier 2 — scope/posture only); https://shopify.dev/docs (Tier 1 — apps/themes/storefronts/checkout surfaces, CLI, App Store & Theme Store); help.shopify.com not fetched (prior passes recorded HTTP 403).
- BigCommerce — https://developer.bigcommerce.com/docs (Tier 1); https://docs.bigcommerce.com/developer/docs/storefront/getting-started.md (Tier 1 — Stencil/Catalyst/headless matrix, multi-storefront, cart & checkout APIs).
- WooCommerce — https://woocommerce.com/documentation/woocommerce/getting-started/ (Tier 1); https://woocommerce.com/document/managing-products/ (Tier 1); https://woocommerce.com/document/managing-orders/ (Tier 1); https://woocommerce.com/document/managing-orders/order-statuses/ (Tier 1).
- Adobe Commerce / Magento Open Source — https://experienceleague.adobe.com/en/docs/commerce (Tier 1 landing — merchant guide map); https://experienceleague.adobe.com/en/docs/commerce-admin/stores-sales/guide-overview (Tier 1 — purchase experience, order management, store structure).

Sourcing limitations: Shopify's merchant manual (help.shopify.com) unreachable this pass (403 recorded in prior passes); Shopify evidence rests on the product page (Tier 2) plus shopify.dev (Tier 1). No precise plan entitlements, numeric limits, or pricing asserted anywhere. Marketing figures on vendor homepages (conversion uplift, shopper counts) deliberately not used as operational facts.

## Product Observations

### Shopify — hosted storefront-first platform (Layer A, Tier 1 shopify.dev + Tier 2 shopify.com)

- Self-positioning: "The All-in-One Commerce Platform for Businesses"; "Sell everywhere people shop. Online and in person. Across AI and on social."
- Merchant build loop presented as three steps: "01 Add your first product, 02 Customize your store, 03 Set up payments" — product catalog → storefront design → payment as the onboarding spine.
- The merchant works in the **Shopify admin** ("Sidekick… Built right into your Shopify admin"); the platform operates the online store and checkout for the merchant.
- Storefronts: themes (Theme Store) or custom builds; developer docs organized around **apps** (extend "Shopify's core functionality with apps that integrate into Shopify's admin, online store, checkout"), **storefronts** ("build a custom theme or Hydrogen storefront"), and agents/checkout surfaces. Headless toolkit (Hydrogen) exists alongside the platform-hosted online store — headless is an option, not the product's identity.
- Scope breadth (product page nav): website builder, domains, customer accounts; sell online / POS / Shop app / social & marketplaces / international ("Shopify Markets") / B2B; email & chat, discounts, analytics; orders & inventory, shipping, finance; checkout, payments, taxes.
- App Store and Theme Store as distribution ecosystems; CLI for apps/themes/headless storefronts.

### BigCommerce — open SaaS with bundled storefront + API surface (Layer A, Tier 1)

- Self-description: "a commerce-centric company, platform, and set of retailer-facing SaaS products"; "Our hosted control panel and bundled storefront are how most brands interact with BigCommerce. They have access to their BigCommerce stores from day one."
- Platform split the docs themselves make: "store-level APIs that handle product catalogs, orders, and customers" vs "shopper-focused APIs" for storefront experiences; REST Management APIs "manage products, orders, customers, and store settings programmatically".
- Storefront option matrix (documented explicitly): **Stencil** — "traditional storefront option… integrated, template-based design system… Fully Hosted – Runs directly on the BigCommerce platform… Integrated with BigCommerce's Backend – Handles checkout, cart, and product rendering without needing API calls", default theme Cornerstone; **Catalyst** — headless Next.js composable storefront over the GraphQL Storefront API, merchant hosts it; **Custom headless** — "BigCommerce powers commerce operations" behind any frontend. Their own comparison table labels Stencil "Monolithic" and Catalyst/custom "Headless".
- Multi-storefront: "Maintain multiple sites while centrally configuring a distinct look, feel, and pricing configuration for each shopping experience."
- Cart/checkout: storefront cart and checkout APIs to "build a custom checkout experience… move shoppers through their journey, from cart to checkout" — i.e., the platform ships a standard cart+checkout and exposes it for replacement/customization.
- Store data objects named at API level: products, orders, customers, store settings; customer login API; webhooks; sandbox stores; B2B Edition ("company accounts, quotes, and custom pricing"); PCI/ISO/SOC certifications mentioned on the overview page.
- Apps marketplace ("single-click apps… enrich their control panels") and agency ecosystem.

### WooCommerce — open-source plugin on WordPress (Layer A, Tier 1)

- Posture: "WooCommerce is built on top of WordPress" — a plugin that turns a WordPress site into a store; hosting/design/updates are the merchant's assembly; free core plugin + paid extensions marketplace.
- Documentation taxonomy itself enumerates the Type's object set: **Products, Taxes, Shipping, Payments, Orders, Data and reporting, Customers, Marketing, Site administration, Store design**, plus setup wizard ("Onboarding Wizard and Setup Checklist… set up your store and get it ready to start selling").
- Products: "you can add a product with just a name and a price"; product types — **Simple, Grouped, External/Affiliate, Variable** (each variation with "its own price, SKU, stock level"), **Virtual** ("don't require shipping"), **Downloadable** ("digital files… customers can access immediately after payment"); categories "for organizing and displaying"; attributes; reviews; bulk editing; featured/filter/sort.
- Orders: "Orders are the center of activity in your store"; "Orders are usually created when a customer on your site completes the checkout process, though you can manually add orders"; also created via REST API by external systems; visible to **Admin / Shop Manager** roles.
- Order status lifecycle (documented, product-exact): **Draft** (temporary block-checkout record) → **Pending payment** → **Processing** ("Payment has been received (paid), and the stock has been reduced. The order is awaiting fulfillment") → **Completed**; side states **On hold** (offline/delayed payment confirmation; auth/capture split), **Failed** (stock returned to inventory), **Cancelled** (stock returned "if inventory management is enabled"; auto-cancel of pending-payment orders under the Hold Stock setting), **Refunded**. Status changes trigger customer/merchant emails. Virtual+downloadable-only orders skip the fulfillment leg.
- Payments: "A payment gateway, in WooCommerce terms, is a WordPress plugin…" — payment is an extension seam, not built-in processing (WooPayments available in selected locations).
- Abandoned-cart recovery emails; test orders; order notes to communicate with customers.

### Adobe Commerce / Magento Open Source — enterprise commerce application (Layer A, Tier 1)

- Deployment poles documented side by side: on-premises installation, Adobe Commerce on Cloud (PaaS), Adobe Commerce as a Cloud Service (SaaS); Magento Open Source named as the open-source sibling in developer docs.
- Merchant guide map (the Type's object set at enterprise depth): **Catalog Management** ("Create and manage products and the category structure that drives your store's navigation"), **Inventory Management** ("Manage stock in multiple locations so that your store accurately reflects physical inventory"), **Merchandising and promotions** ("targeted promotions"), **Content and Design** ("Manage the text and images on your storefront pages"), **Customer Management** ("accounts… customer segments, and… B2B company accounts"), **Stores and Purchase Experience** ("Set up the point of purchase and the supporting functions that turn shopping cart items into completed orders"), **Admin Systems** ("users, security settings, and data transfers"), Analytics/BI, B2B Commerce.
- Store structure: "multiple websites with a different domain, and within each website… multiple stores, and within each store, separate store views" (locales/branding) — multi-site hierarchy for multi-brand/multi-locale selling.
- Purchase experience: shopping cart configuration, **checkout process** ("gather the information necessary to complete a transaction"), instant purchase from saved account data, wish lists, gift card accounts, native payment methods, taxes per locale, currency per store view.
- Order management: "Track order progress and status through the workflow, where an order becomes an invoice and an invoice becomes a shipment" — order → invoice → shipment document chain (product-exact granularity; canonical reading is payment+fulfillment states on the order).
- Optional commerce services layered on: Live Search, Product Recommendations, Catalog Service, Payment Services — explicitly separate services, not core.

## Cross-product Comparison

| Structure | Shopify | BigCommerce | WooCommerce | Adobe Commerce | Evidence |
|---|---|---|---|---|---|
| Merchant-defined product catalog (price-bearing records, categories, variants) | Yes ("add your first product") | Yes (catalog APIs: products) | Yes (Simple/Variable/Virtual/Downloadable; "name and a price") | Yes (Catalog Management: products + category structure) | A×4 → B |
| Platform-operated shopper buying surface (storefront + cart + checkout owned by the product) | Yes (hosted online store + operated checkout; themes) | Yes (Stencil "fully hosted… handles checkout, cart, and product rendering"; bundled storefront "from day one") | Yes (storefront pages + checkout blocks inside the merchant's WordPress site) | Yes (storefront + point of purchase configured in Admin) | A×4 → B |
| Headless/custom storefront as an option alongside the coupled one | Yes (Hydrogen) | Yes (Catalyst/custom headless documented as storefront options) | Via WordPress theming/decoupling (REST API documented) | Yes (web APIs for headless applications) | A×4 → B (posture continuum) |
| Cart → checkout → payment → persistent order | Yes | Yes ("from cart to checkout"; cart/checkout APIs) | Yes ("orders are usually created when a customer… completes the checkout process") | Yes ("turn shopping cart items into completed orders") | A×4 → B |
| Order lifecycle with payment/fulfillment/cancellation/refund states | Order + fulfillment machinery in admin (status names not fetched) | Orders object + workflows | Documented status set: Draft/Pending payment/Processing/Completed/On hold/Failed/Cancelled/Refunded | "order becomes an invoice and an invoice becomes a shipment"; order workflow | B (Woo/Adobe status detail = A, product-exact) |
| Stock/inventory linkage to selling | Orders & inventory in scope | Inventory in settings/data | Documented: stock reduced on payment, returned on cancel/fail; "if inventory management is enabled" | Inventory Management guide ("multiple locations") | B — linkage common, depth varies |
| Customer accounts / shopper login | Customer Accounts product | customers object + Customer Login API | Customers documentation area | Customer Management (accounts, segments, B2B company accounts) | B; guest checkout exists (variant) |
| Promotions/discounts | Discounts in scope | promotions machinery | Marketing area; "targeted promotions" (Adobe) | Merchandising and promotions | B |
| Shipping & tax configuration | Shipping, Taxes in scope | settings/APIs | Taxes + Shipping doc areas | Taxes per locale, currency, shipping & delivery | B |
| Storefront design layer (themes/page editing) | Theme Store, "customize your store" | Stencil themes + widgets for non-technical edits | Store design area, WordPress themes | Content and Design, Page Builder | B |
| Extensions/apps ecosystem + APIs | App Store, CLI, APIs | Apps marketplace, webhooks, APIs | Extensions marketplace, REST API | App Builder, API mesh, web APIs, SDKs | B |
| Admin roles/staff permissions | admin (Sidekick "in your Shopify admin") | control panel + API scopes | Admin / Shop Manager roles (documented) | Admin Systems (users, security) | B |
| Sales analytics/reporting | Analytics in scope | Data and reporting (Woo) / reporting APIs | Data and reporting | Analytics and reporting (MBI) | B |
| Hosted-SaaS-only? | SaaS | SaaS ("open SaaS") | Self-hosted plugin (free core) | On-prem / PaaS / SaaS | B — falsifies SaaS as defining |
| Built-in payment processing? | platform-operated payments + gateways | gateway integrations | gateway plugins ("a WordPress plugin") | native payment methods + Payment Services add-on | B — payment as integration seam; processing not defining |

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

An E-commerce Platform is the merchant's own online selling operation realized as one integrated software platform. Three jointly-held structures:

1. **The merchant's sellable catalog of record** — the merchant defines, as structured records, the products it sells (name and price at minimum; variants, options, categories, media, virtual/downloadable forms as common depth). The catalog is the merchant's, not other sellers'. *(Remove → a product database/PIM; the platform would have nothing to sell.)*
2. **The platform-operated buying surface over that catalog** — the platform itself presents the catalog to shoppers (browse/discover, product pages, cart) and carries the purchase through its own checkout. The coupled storefront is the product's center of gravity; themes/page design make it the merchant's branded surface; headless/custom storefronts exist as options without changing the product's identity. *(Remove → a CMS/website with no selling surface, or an API-only commerce engine = Headless Commerce Platform.)*
3. **Checkout-to-order conversion operated from the same system** — completing checkout with payment converts the cart into a persistent order of record that the merchant manages inside the same system through its lifecycle (payment confirmation, fulfillment, cancellation, refund), with stock and customer effects recorded there. *(Remove → a brochure site with third-party buy buttons, or a handed-off completion stage = Checkout Platform; the "management" leg is what the checkout sibling explicitly does not hold.)*

Jointly-held is load-bearing:
- 1 alone = product database / PIM territory
- 2 alone = website builder / CMS
- 3 alone = Checkout Platform (§05.06)
- 1+2 without 3 = browsable catalog site with no transaction
- 1+3 without 2 = engine + embedded buy buttons (headless-adjacent substrate)
- 2+3 without 1 = shell storefront with nothing to sell (incoherent)

### L1 — Common Mature Structure

Present in all/most sampled products; expected by the market but not definitional:

- product depth: variants/options per-variation price/stock, categories/collections, attributes, media, reviews
- customer accounts with saved details; guest checkout as the common alternative
- promotions/discounts; sales pricing
- shipping/delivery configuration (rates, carriers) and tax configuration
- inventory/stock tracking with selling-side decrement and cancellation restock
- storefront design layer: themes/templates, page/layout editing usable by non-developers, navigation
- order-lifecycle tooling: fulfillment actions, refunds, status-triggered customer/merchant emails, order notes
- analytics/reporting on sales
- extensibility: apps/plugins/extensions marketplace, public APIs, webhooks
- staff/admin roles and permissions
- storefront search (native or service)

### L2 — Variant / Optional Structure

- deployment posture: hosted SaaS ↔ self-hosted open source ↔ plugin-on-CMS ↔ enterprise on-prem/PaaS/SaaS
- storefront posture: coupled theme storefront as center ↔ headless-first (the sibling Type); same products often span both
- channel breadth: POS/in-person, mobile app storefront, social/marketplace channel sync, multi-storefront/multi-site hierarchies
- B2B mode: company accounts, quotes, trade pricing (§05.17 sibling when account-mediated selling is the center)
- multi-market/cross-border: markets, currencies, languages, localized payment; border obligations distinguish the §05.24 sibling
- subscription selling, digital-goods emphasis, gift cards, wish lists, abandoned-cart recovery
- region-specific payment methods and compliance
- AI assistance (era-current)

### L3 — Vendor-specific (kept in Research Notes only)

- Shopify: Hydrogen/Oxygen, Shop app, Shop Pay, Sidekick, Shopify Markets, Universal Commerce Protocol/agents surface, Editions, Capital; homepage marketing figures (conversion %, shopper counts) not used as facts.
- BigCommerce: Stencil/Cornerstone, Catalyst + Makeswift visual builder, BigCommerce for WordPress (BC4WP), B2B Edition, multi-storefront, storefront-token channel scoping, certification list.
- WooCommerce: product-type taxonomy names (Simple/Grouped/External-Affiliate/Variable/Virtual/Downloadable), block-based checkout Draft machinery + daily draft cleanup, Hold Stock setting + auto-cancel window, exact status names, WP Admin menu structure, WooPayments regional availability, gateway-as-plugin definition.
- Adobe Commerce: websites→stores→store-views hierarchy, order→invoice→shipment document chain, Page Builder, Commerce Admin systems, Live Search/Product Recommendations/Catalog Service/Payment Services as separate SaaS services, three deployment programs, HIPAA-readiness add-on, Edge Delivery Services storefront tooling.

### Rejected Findings (anti-overfitting)

- "E-commerce platform = hosted SaaS subscription product" — **rejected**: WooCommerce (free plugin) and Magento Open Source/on-premises falsify; deployment is L2.
- "E-commerce platform = themes + app store" — **rejected** as definitional: early-2000s cart scripts had neither; ecosystems are L1/L2 maturity markers.
- "Built-in payment processing defines it" — **rejected**: payment is an integration seam (gateway plugins/modules documented; certifications are product posture). The owned **checkout** is definitional; the payment processor is not.
- "Multi-currency/multi-language defines it" — **rejected**: single-market stores satisfy the L0 (cross-border border-machinery test applied, see Boundary Findings).
- "Inventory module defines it" — **rejected**: WooCommerce documents orders/checkout working with inventory management disabled ("if inventory management is enabled"); linkage is common, not invariant.
- "Customer accounts define it" — **rejected**: guest checkout and anonymous purchasing are documented modes; accounts are L1.
- "B2B structures define it" — **rejected**: the consumer-retail pole satisfies L0 without accounts/quotes (B2B = §05.17 sibling).

## Boundary Findings

1. **vs Headless Commerce Platform (§05.01, processed) — pre-hung joint-review flag DISCHARGED from this side.** The headless pass's center-of-gravity test and by-design test are adopted and confirmed from the storefront side: all four sampled storefront-first products document headless surfaces as *options* (Shopify Hydrogen; BigCommerce Catalyst/custom headless with Stencil labeled "monolithic"; Adobe web APIs; WooCommerce REST API/WordPress theming), while the coupled storefront + operated checkout remains each product's center ("our hosted control panel and bundled storefront are how most brands interact"). Conversely the headless pass's population (commercetools, Medusa…) treats the storefront as disposable. Verdict: **keep both Types; seam = center of gravity** (is the platform-operated buying surface the product, or a convenience over the engine?). The posture is a continuum, not a hard wall — recorded, no directory change.
2. **vs Online Store Builder (§05.01, unprocessed) — NEW flag.** The market uses "e-commerce platform" and "online store builder" almost interchangeably for hosted template-first products (Wix/Squarespace/Shopify self-descriptions blend the two), and the sampled population here already includes a strong template-first pole. Candidate outcomes for joint review when that leaf is processed: alias of this Type; or a DIY-store-creation emphasis variant; or a packaging split (builder = store-creation-first packaging of the same core). Recorded from this side; no directory change.
3. **vs Mobile Commerce Application (§05.01, unprocessed)** — mobile storefronts (responsive storefronts, dedicated shopper apps, mobile admin companions) appear in-sample as channel variants; the Type's center is unchanged on a phone. Sibling pass should confirm the buyer-facing-app vs seller-platform seam.
4. **vs Marketplace Platform (§05.02, processed)** — that pass's own remove-test ("remove multi-seller venue → single-merchant e-commerce platform software") is confirmed from this side: the sampled platforms sell the **merchant's own** catalog under the merchant's brand; per-seller attribution, seller onboarding, commission/settlement economics are absent from every sampled L0. Keep-both; the multi-seller venue is the marketplace's center, not a feature of this Type.
5. **vs Checkout Platform (§05.06, processed) / Shopping Cart Platform (§05.06)** — from this side the cart and checkout are **owned, internal structures** of one system (Adobe: "supporting functions that turn shopping cart items into completed orders"; BigCommerce: standard cart/checkout that APIs may replace). The checkout sibling's defining posture is the stand-alone completion stage handed an initiated purchase from outside, with fulfillment explicitly seller-side and idempotent handoff — i.e., exactly what this Type does *not* do (it keeps the order and the operation). Seam: ownership of the purchase record and the operation around it. Consistent with that pass's note that standalone cart products have been absorbed into commerce platforms.
6. **vs B2B E-commerce Platform (§05.17, processed)** — that pass centers account-mediated selling (trade pricing, buyer roles, PO/approvals); this pass's consumer-retail pole (anonymous public retail) satisfies the L0 without any of it, and B2B structures appear here as L2 mode/edition (BigCommerce B2B Edition, Adobe B2B, Shopify B2B). Seam: is selling account-mediated by design, or a mode? Keep-both.
7. **vs Cross-border Commerce Platform (§05.24, processed) — border-machinery test applied, as that pass requested.** Multi-currency, localization, and multi-storefront are documented as standard capabilities/structures (BigCommerce multi-storefront; Adobe store views; Shopify Markets as an *add-on posture*). Without a foreign-market model + border obligations carried by the order, a multi-storefront platform remains this Type. Keep-both; the border-machinery test stands.
8. **vs Subscription Commerce / Digital Goods / Dropshipping platforms (§05.16/§05.20/§05.22, processed)** — all three passes define themselves by what a purchase *converts into* (recurring commitment schedule; deliverable-anchored digital fulfillment; supplier-direct fulfillment without inventory). On this side those are L2 sellable-goods/selling-model variants of the same platform substrate; the siblings' defining conversions are absent from this pass's L0. Consistent remove-tests already recorded by those passes.
9. **vs PIM / Product Catalog Management (§05.04), OMS (§05.07), Inventory Management (§10)** — the catalog leg of this Type holds *sellable* records for *this merchant's storefront*, not syndication/normalization across channels (PIM); order management here is the store's own order book, not cross-channel sourcing/orchestration (OMS); stock here is storefront-attached selling state, not the domain-neutral stock ledger. Keep-both, seams at the operation's center of gravity.
10. **vs CMS (§02.07, processed)** — a CMS's published site presents content; adding checkout machinery to a CMS site produces exactly this Type (WooCommerce is the existence proof: a WordPress plugin whose core adds products/cart/checkout/orders). Presentation-only → CMS; transactional selling → this Type.

## Historical / Market-Sample Check (§24 discipline)

- **Early-2000s shopping-cart-script generation** (osCommerce-class and its Zen Cart/OpenCart/PrestaShop lineage, conceptually): merchant installs on a host, defines products in a catalog, gets a template-based storefront with cart and checkout calling a payment module, and an order admin with statuses. Satisfies all three L0 legs **without** SaaS, app stores, theme marketplaces, headless APIs, or AI. Historical check **passed**.
- **Paper-era analog (thin ancestor)**: a mail-order retailer's catalog + order form + payment by mail + order ledger satisfies the pattern structurally (catalog of record, buying surface = the catalog/form, order book), but has no platform-operated digital buying surface — recorded as the pre-history the storefront digitized, not a member.
- **Regional/platform-native products**: regional European shop systems and platform-native storefronts satisfy the L0 with region-specific payment/compliance — supporting the decision to keep payment methods and localization out of the definition.
- **Enterprise vs SMB poles**: Magento-class enterprise depth (multi-site hierarchies, invoice/shipment chains) and plugin-class minimalism (name + price product, checkout, order status) both satisfy — supporting depth items as L1/L2, not L0.

## Uncertainties

- Shopify's merchant-side order-status vocabulary was not directly observed (help center unreachable); lifecycle claims for Shopify rest on scope evidence (orders/inventory/shipping/refunds in product scope) and are written at B-strength.
- Exact feature packaging (which capabilities are plan-gated per product) deliberately not asserted; pricing/plan entitlements out of scope.
- WooCommerce store-frontend theming depth (block vs classic themes) not separately verified; presentation evidence accepted at doc-taxonomy level ("Store design").
- The online-store-builder boundary (Finding 2) is recorded as a hypothesis for that sibling's own pass, not a settled verdict.

## Final Synthesis

An E-commerce Platform is the merchant-side software platform that runs the merchant's own online store as one system: the merchant defines a sellable catalog; the platform operates the shopper-facing buying surface (storefront → cart → checkout) over that catalog as its center; and completed checkouts become persistent orders the merchant manages to fulfillment inside the same system. Everything else commonly present — variants, accounts, promotions, shipping/tax configuration, inventory linkage, themes, analytics, apps/APIs, staff roles, SaaS packaging, headless options, B2B/cross-border/multi-channel breadth — is mature-market structure or variant, not definition. The Type is bounded on one side by surfaces that present without transacting (CMS, site builder) and on the other by machinery that transacts or orchestrates without owning the selling operation (checkout platform, headless engine, OMS, marketplace).
