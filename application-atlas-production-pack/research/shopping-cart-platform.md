# Research Notes — Shopping Cart Platform

Research date: 2026-09-10
Leaf: Shopping Cart Platform (DIRECTORY §05.06 Commerce Checkout, sibling of Checkout Platform)
Slug: shopping-cart-platform

## Research Goal

Understand what a Shopping Cart Platform actually is as an Application Type: what the cart object is (what it holds, how it persists, whose it is), what buyers and sellers do with it, how a standalone cart product attaches to a website that has no commerce machinery of its own, where the cart ends and checkout begins, and — the pre-hung joint-review question from the checkout-platform pass — whether this leaf is a real Type or a capability slice absorbed by commerce platforms.

## Initial Boundary

- Hypothesis: the cart is the buyer's pre-commitment accumulation of intended purchases — a persistent, editable, priced working object bound to a shopper, handed off to a completion stage. A Shopping Cart Platform is a product whose defining job is to provide that object as a service, typically attached to a website that has no commerce machinery of its own.
- Nearest neighbors per directory: Checkout Platform (sibling leaf, §05.06); E-commerce Platform / Online Store Builder / Headless Commerce Platform (§05.01); Payment Gateway / Payment Processing (§08); Order Management (§05.07); PIM / Product Catalog (§05.04); Sales Order Capture (§07).
- Pre-hung joint-review flag (checkout-platform pass, 2026-09-07): "boundary defined structurally this pass (cart = pre-commitment accumulation/editing of intended items; checkout = completion transaction of an initiated purchase; seam = the checkout button), but the market observation is that standalone cart products have been almost entirely absorbed into commerce platforms, and cart↔checkout pairs are bundled everywhere; recommend joint review when shopping-cart-platform is processed — candidate outcomes: keep-both with accumulation-vs-completion seam (current framing), or re-scope the cart leaf as a capability slice absorbed by commerce platforms."
- Prior Atlas passes already drew seams toward this leaf (treated as cross-references):
  - research/e-commerce-platform.md: "from this side the cart and checkout are owned, internal structures of one system."
  - research/online-store-builder.md: "pre-purchase accumulation exists in every store builder as an internal structure; standalone cart products have been largely absorbed."
  - research/headless-commerce-platform.md: "cart as working object"; Shopify Storefront Cart API "redirects to Shopify's Web Checkout."
- Obvious unknowns at start: do standalone cart products still exist as a live product category (or only as history)? What exactly does a standalone cart platform provide beyond the cart UI? Where does item data live (the merchant's site or the cart platform)? What integrity machinery keeps client-side cart data honest?

## Research Questions

1. What is the cart object — what does it hold (line items, quantities, options, totals), and what is its state character (estimate vs committed)?
2. How does the cart persist — session, cookie, account? Across page views, visits, devices?
3. How do items get into the cart — where is item data defined (merchant HTML, links, API, dashboard)?
4. How does a standalone cart platform attach to a website that has none — what does the merchant install, what does the platform host?
5. What keeps client-side cart data honest (price tampering, stale prices)?
6. What does the handoff to completion look like — who provides checkout/payment, what crosses the seam?
7. What does the merchant get — dashboard, orders, abandoned carts, configuration?
8. What cart-adjacent structures exist (promotions, notes, stock limits, digital goods, subscriptions, donations)?
9. Is the standalone form a live Type or an absorbed capability? What is the modern realization split?
10. Does the definition survive the historical hosted-cart era (2000s) and the platform-internal present?

## Representative Products

Selection: market representativeness + documentation completeness + different product philosophies + different eras. Four standalone products realizing distinct poles, plus one platform-internal API as the absorbed-side cross-check:

| Product | Pole | Era | Customer tier | Rationale |
|---|---|---|---|---|
| Snipcart | developer-first, client-side HTML-attribute cart embedded in any site | modern | developers + small merchants | canonical "add a cart to any website" docs; excellent documentation |
| Foxy | hosted cart & checkout platform, API-first, attach to any site/CMS | modern (since 2007) | one-person businesses → Fortune 500 | self-describes as focusing "exclusively on a shopping cart platform" |
| Mal's e-commerce | classic hosted cart page driven by buy-now links | legacy pattern, still operating | micro/small merchants, free tier | the 2000s hosted-cart pattern in its purest surviving form |
| RomanCart | classic hosted cart + buy buttons + optional hosted storefront | legacy pattern, still operating | micro/small merchants, UK-centric | same pattern with storefront/marketing extensions |
| Shopify Storefront Cart API | platform-internal cart object of a commerce platform | current | SMB → enterprise commerce | the absorbed-side realization, documented at API level |

Deliberately not sampled: Cart32 (legacy hosted cart; sample already sufficient), WooCommerce cart (plugin-internal; same absorbed pattern as Shopify), cart-recovery/abandonment tools (adjacent capability, not the cart itself).

## Sources

Tier 1 (official operational documentation), fetched 2026-09-10:

- Snipcart — Basics: https://docs.snipcart.com/v3/ (Layer A)
- Snipcart — Products: https://docs.snipcart.com/v3/setup/products (Layer A)
- Snipcart — Cart summary: https://docs.snipcart.com/v3/setup/cart-summary (Layer A)
- Snipcart — Security: https://docs.snipcart.com/v3/security (Layer A)
- Foxy — How Foxy Works: https://foxy.io/how-foxy-works (Layer A)
- Foxy — Home: https://foxy.io/ (Layer A at product-positioning level)
- Mal's e-commerce — Home / How it works: https://www.mals-e.com/ (Layer A at how-it-works level)
- RomanCart — Home / How it works: https://www.romancart.com/ (Layer A at how-it-works level)
- Shopify — Storefront API Cart object: https://shopify.dev/docs/api/storefront/latest/objects/Cart (Layer A)

Unreachable / limitations (see Uncertainties):

- Foxy wiki (wiki.foxycart.com, /v/2.0/overview and root) — two fetch attempts returned empty; abandoned per the network-limitation rule. Foxy claims rest on foxy.io product/how-it-works pages plus the vendor's own demo cart URL; operational API detail not asserted.
- foxy.com — wrong company (a produce brand); the cart platform's domain is foxy.io.
- Mal's detailed help docs (getting-started PDF) and RomanCart screencasts/help pages not fetched; claims for these two kept at the level observed on their how-it-works surfaces.
- Historical hosted-cart context (Cart32, 1ShoppingCart era) — no fetch attempted; used only as era-anchoring reasoning, never as structural evidence.

No claim below relies on model memory for precise operational facts. All precise facts are Layer A and marked research-notes-only.

## Product Observations

### Snipcart (Layer A)

- Self-description: "Snipcart is a shopping cart developers can easily integrate into any website in minutes." "Unlike many e-commerce solutions, Snipcart lives *on* your site, in its HTML client-side code."
- Attachment model: "You add the **shopping cart** to your site with a simple JavaScript snippet inclusion. It's similar to adding a third party script like Google Analytics."
- Item definition: "You create **products** by adding simple HTML attributes—product name, price, description, etc.—to elements on your site. Usually, developers add these attributes to a 'buy' `<button>`." Any HTML element with class `snipcart-add-item` plus `data-item-id`, `data-item-price`, `data-item-name` (required), `data-item-description`, `data-item-image`, `data-item-url` becomes a purchasable item.
- Item options ("custom fields"): dropdown with per-option price modifiers (`Black|Brown[+100.00]|Gold[+300.00]`), text, checkbox, textarea, readonly, hidden; multiple fields per item; required/placeholder/default-value controls.
- Quantity machinery: default quantity, max quantity ("Handy if you have limited stocks"), min quantity, quantity step, and a `stackable` enum (`auto`/`never`/`always`) controlling whether repeated adds merge into one line or stay separate ("useful when you have a product with specific custom fields requiring different information for each occurrence").
- Per-item commerce attributes: weight/dimensions (for shipping providers), shippable flag ("All shipping options will be removed from the cart if you only have non-shippable items"), taxable/taxes/has-taxes-included, digital-good file GUID (file uploaded in the vendor's dashboard), categories, JSON metadata, alternate-price lists (`data-item-price-vip`).
- Cart surfaces: `snipcart-checkout` class opens the cart; `snipcart-items-count` and `snipcart-total-price` classes display count/total anywhere on the site.
- **Integrity machinery (the security page, verbatim)**: "Since Snipcart relies on HTML markup for product information, people often ask: How do you prevent bad actors from changing product pricing with their DevTools before checking out? The short answer: before processing an order, we double check product data using a crawl back method. Once an order is placed, Snipcart initiates a server-side validation: First, we crawl the URL specified in your data-item-url property. Then, we cross-reference the product information stored in the DOM with the one displayed in the order. If these don't match, we block the transaction." Also: "If you have more than one product with the same ID, they must all have the same price, otherwise validation will fail."
- Merchant side: hosted merchant dashboard ("Unlike the cart, this dashboard doesn't live on your site—it's hosted on our own servers") for orders, customers, discounts, abandoned carts, payment-gateway configuration, test/live environments; email templates (invoices, refunds, abandoned carts, order shipped, digital download); webhooks (order/subscription/shipping/tax events); JavaScript SDK; full API (orders, customers, discounts, products, abandoned carts, user sessions); subscriptions "currently under development" at research date; e-invoicing; MCP server docs (era artifact).
- Reading: the cart platform's item data lives in the merchant's own HTML; the platform hosts the cart, the checkout, the order record, and a validation loop that re-reads the merchant's site to confirm the order matches the site's declared prices.

### Foxy (Layer A)

- Self-description (how-it-works page): "Most e-commerce systems *also* are website builders. Most website builders have some shopping cart functionality. And mostly… one side or the other is limited and frustrating. But Foxy is somewhat unique. We focus *exclusively* on a shopping cart platform you can **add to your existing website**."
- Attachment model: "Foxy *can* be **as simple as an 'add-to-cart' link** on a static HTML site. But it can also power e-commerce in custom sites built in any framework, CMS, or language." The vendor's own demo link is a hosted cart URL carrying signed product parameters (`.../cart?name=Simple+Product||<hash>&price=10USD||<hash>&code=simple_product||<hash>`).
- "And if you don't have a website? You can even use Foxy directly from emails or social posts!"
- Product scope in one cart: "Sell **physical products**, services, **donations**, digital **downloads**, **recurring billing** and **auto-ship**, memberships, **custom products** (with near-unlimited options), and more, all in the same cart."
- Cart-adjacent machinery: "Live shipping and rates, with native or external providers? Yup. Coupons, discounts, and gift cards? Yup. Customer syncing (with password hashes!)? Single Sign-on? APIs and webhooks? Of course!"
- Completion: "Foxy makes it easy to add a persistent **cart**, a secure **one-page checkout**, a **customer portal**, and more." Payment: "We support about 100 different payment gateways and platforms around the world, and you can even configure different payment accounts within a single store… Or use Foxy with offline or purchase order payments."
- Post-order: "Our admin provides lightweight order management, or push orders to Airtable, your own ERP or CRM, or our friends over at OrderDesk.com."
- Positioning claims: users "range **from one-person businesses** on Wix or Squarespace, all the way **to Fortune 500** implementations with custom CMS and ERP back-ends"; "We've been around since 2007"; integrations page lists Webflow, Framer, Squarespace, Wix, WordPress, Carrd, Unbounce, Weebly, Drupal, ClickFunnels, Leadpages; PCI Level 1 Service Provider claim; customer quote: "completely custom checkout page while still handling all the critical security components… even after being redirected to the Foxy secure payment page."
- Reading: the hosted-cart pole — the platform hosts cart and checkout as services; item data arrives as (signed) parameters from the merchant's site; the merchant keeps the site and the product display entirely.

### Mal's e-commerce (Layer A)

- Self-description: "We make it simple to add a shopping cart to your website. Escape from the limitations of traditional store builder software."
- Attachment model: "All you have to do is add simple Buy Now links or buttons on any page on your website, made from a form button, a text hyperlink or your own image."
- The hosted cart: "When customers click on one of these links they are taken to a cart page hosted on our servers, here they can amend their order, or checkout. Credit card and check details are collected using an SSL secured server."
- Notification: "Once a customer completes an order you will be notified immediately by e-mail."
- Feature claims: responsive cart design, credit cards directly on the website, "Sell in any currency and in 30 different languages", unlimited products, PayPal/Braintree/Nochex/Skrill payments, "Nothing to install or technical setup required"; "145,000 accounts online across 120 countries"; free tier + premium tier.
- Reading: the purest hosted-cart form — buy-now links on any site → vendor-hosted cart page (amend + checkout) → payment → email notification. No catalog of record on the platform side beyond what the links declare.

### RomanCart (Layer A)

- Self-description: "Paste Shopping Cart 'Add To Basket' and 'Buy Now' Buttons onto your Existing Website, Twitter, Facebook, Insta or Anywhere! With the RomanCart Shopping Cart any Website can Become a Shop in Minutes." "You can add the RomanCart Shopping Cart to any website: .html, Wordpress, Wix, Muse, Weebly, Serif, Anything!"
- Cart surfaces: "Your customers stay on your site as they add items to their carts via a drop-down floating cart fixed in the top-right corner of their screens" (drop-cart); "Shopping Cart Templates: Choose exactly how your cart looks to your customers"; responsive templates.
- Button widgets: "Create Shopping Cart Buttons With Multiple Options, Variations, Modifiers and Social Media Links."
- Storefront option: "Easily add an entire shop on to Wordpress, Facebook or your own website and manage your products and sales on RomanCart" — a gradient toward the store-builder pole.
- Stock management (gradient case): "Show Real time stock and prices on your website. RomanCart Lets you change the price, stock and availability of products on your website without changing any code! It doesn't even matter who your website is hosted with or how it was created!"
- Payment gateways: PayPal, SagePay, Stripe, Braintree, Authorize.net, WorldPay, Nochex, Global Payments, ePDQ, Netbanx, Secure Trading, Cardsave.
- Use cases enumerated: "Websites, Telephone Sales, Mail Orders, Invoices, Proformas, Accounting, Quotes" — the cart as a general priced-intent instrument beyond web retail; digital downloads ("Digital Vault… delivered automatically after purchase"), barcoded tickets, accommodation booking.
- Marketing machinery: email marketing, autoresponders, coupons, cross-sell/up-sell, eBay listing from the control panel; order fulfilment service; sister website-builder product (Sellr).
- Reading: the hosted-cart pattern extended with storefront, stock-push, and marketing machinery; the "telephone sales / mail order / invoice / quote" use list shows the cart platform serving as a general priced-line-item accumulator for a small business.

### Cross-check: Shopify Storefront Cart API (Layer A — the absorbed-side realization)

- Object definition (verbatim): "A cart represents the merchandise that a buyer intends to purchase, and the estimated cost associated with the cart, throughout a customer's session. Use the checkoutUrl field to direct buyers to Shopify's web checkout to complete their purchase."
- Cart fields: `lines` (merchandise lines with quantity, selling plan, custom attributes, parent relationships "for nested line items such as warranties or add-ons"), `cost` ("The estimated costs that the buyer will pay at checkout. **The costs are subject to change and changes will be reflected at checkout**"), `discountCodes`, `appliedGiftCards`, `buyerIdentity` (customer access token, B2B company location, checkout preferences — "Preferences prefill checkout fields but don't sync back to the cart if overwritten at checkout"), `delivery`/`deliveryGroups` (carrier-calculated rates available), `note`, `attributes` (key-value, e.g. gift messages), `totalQuantity`, `createdAt`/`updatedAt`.
- Mutations: `cartCreate`, `cartLinesAdd/Update/Remove`, `cartDiscountCodesUpdate`, `cartGiftCardCodesAdd/Remove/Update`, `cartNoteUpdate`, `cartAttributesUpdate`, `cartBuyerIdentityUpdate`, `cartSelectedDeliveryOptionsUpdate`, `cartDeliveryAddressesAdd/Remove/Update/Replace`. Request-size limits (250 lines/values) documented.
- Reading: the same cart object model — intended merchandise + estimated cost + shopper binding + edit operations + checkoutUrl handoff — realized as an internal structure of a commerce platform. The API's own wording marks the cart/checkout seam: cart costs are estimates; checkout is where they become final.

## Cross-product Comparison

| Dimension | Snipcart | Foxy | Mal's | RomanCart | Shopify Cart API | Evidence |
|---|---|---|---|---|---|---|
| Positioning | "a shopping cart developers can easily integrate into any website" | "focus exclusively on a shopping cart platform you can add to your existing website" | "add a shopping cart to your website… escape from traditional store builder software" | "any Website can Become a Shop in Minutes" | internal object: "merchandise that a buyer intends to purchase… throughout a customer's session" | A (each official) |
| Where item data lives | merchant's HTML (`data-item-*` attributes) | merchant's links/forms (signed parameters) | merchant's buy-now links | merchant's buttons/links or RomanCart-managed stock push | platform's own catalog (variants) referenced by API | A |
| Cart hosting | JS-embedded cart on the merchant's page; dashboard hosted by vendor | hosted cart & checkout pages | cart page hosted on vendor's servers | hosted cart page + floating drop-cart on merchant's site | platform-native object + web checkout | A/B (hosted-or-embedded platform-operated cart constant) |
| Accumulation & editing | add items, quantities, options; stackable rules | "persistent cart"; multi-product add, bundles | "amend their order" on the hosted cart page | floating cart while browsing; amend before checkout | cartLinesAdd/Update/Remove; quantity, attributes, selling plans | A |
| Totals character | cart total displayed; server re-validates against site prices | real-time price calculation (configurator) | cart page shows order to amend | cart shows order; stock/price push keeps site current | "estimated costs… subject to change and changes will be reflected at checkout" | A (estimate-side character explicit at Shopify; operationalized at Snipcart via validation) |
| Shopper binding | user sessions API; customer dashboard | customer syncing, SSO, customer portal | cart session on hosted page | cart session | buyerIdentity (customer token, B2B location); session-scoped | A/B (session-or-account binding constant; mechanism varies) |
| Handoff to completion | built-in checkout steps (customizable) | built-in one-page checkout | checkout on the hosted cart page | checkout on the hosted cart page | `checkoutUrl` → web checkout | A |
| Payment | gateway configuration in dashboard; custom payment gateway option | ~100 gateways claim; offline/PO | PayPal, Braintree, Nochex, Skrill | PayPal, Stripe, SagePay, Braintree, WorldPay, etc. | platform payments | A/B (gateway-external money rails constant) |
| Merchant dashboard | hosted dashboard: orders, customers, discounts, abandoned carts, test/live | admin with "lightweight order management"; push to ERP/OrderDesk | email notification of orders; premium features | control panel: products, sales, eBay, marketing | platform admin (outside this API) | A/B |
| Abandoned-cart machinery | abandoned-cart email templates + API resource | (not observed this pass) | (not observed this pass) | follow-up emails / autoresponders | (not in Cart object; platform feature) | A (Snipcart) / B |
| Cart content scope | physical, digital (file GUID), subscriptions (in development) | physical, services, donations, downloads, recurring, memberships, custom products | products, digital | products, downloads, tickets, accommodation | merchandise lines incl. warranties/add-ons, selling plans (subscriptions) | A/B (mixed-content cart common) |
| Entry channels | merchant website | website, emails, social posts | any website page | website, Twitter/Facebook, eBay | storefront/headless storefront | A/B |

Cross-product reading:

1. **One object model everywhere.** Every sample — standalone or platform-internal — holds the same structure: a shopper-bound, persistent, editable collection of priced line items (product reference, quantity, options) with computed totals, feeding a completion stage. [B/C]
2. **The cart is estimate-side by nature.** Shopify's API says it in one sentence ("estimated costs… subject to change and changes will be reflected at checkout"); Snipcart operationalizes it from the other side (server re-validates the order against the site's declared prices before processing). The cart holds intent; the checkout produces the authoritative transaction. [A+B]
3. **Item data lives with the seller, not the cart.** Standalone cart platforms define items in the merchant's own surfaces (HTML attributes, links, buttons) or accept them as parameters; the cart platform hosts the accumulation, not the catalog of record. RomanCart's stock-push is the observed gradient (platform-managed price/stock pushed to the site). [A+B]
4. **The attachment pattern is the standalone form's defining posture.** All four standalone products attach to a site the merchant already has — via script snippet, link, button, or form — and explicitly position against store builders ("escape from the limitations of traditional store builder software"). [A]
5. **Completion is always bundled or connected.** No sampled cart product stops at accumulation: each provides or connects checkout and payment. A cart that cannot complete is not a sellable product. [B]
6. **The merchant gets an order record and light operations.** Hosted dashboards, email notifications, abandoned-cart machinery, webhooks — the cart platform is also the seller's first order-management surface, deliberately lightweight (Foxy: "lightweight order management… push orders to your own ERP or CRM"). [A/B]
7. **Cart identity spans anonymous-to-known.** Session carts are the base; account binding, customer sync, SSO appear in the modern products; Shopify's buyerIdentity shows the same span inside a platform. [A/B]

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the product is not a shopping cart platform:

```text
Shopper-bound persistent cart
└── priced, editable accumulation of intended purchases
    │   (line items: product reference + quantity + chosen options; computed totals)
    ├── pre-commitment character
    │   (totals are estimates; everything mutable until the handoff)
    └── conversion handoff
        (the cart feeds a completion stage — checkout/payment — that consumes it)
```

Three jointly-held structures. Remove any one and the Type stops being recognizable:

- **The priced, editable accumulation** — line items with product reference, quantity, and chosen options, held as a working object with computed totals. Without accumulation there are no carts — only isolated buy buttons and one-item purchase forms.
- **Shopper-bound persistence** — the cart belongs to a shopper (anonymous session or identified account) and survives page views and returns. Without persistence it is a stateless order form.
- **The conversion handoff** — the cart exists to become a purchase: it feeds a completion stage that consumes the accumulated intent and produces the order. Without it the object is a wishlist / saved-items list (save-for-later, not commitment-track).

Defining behavior across the seam: everything in the cart is pre-commitment intent — totals are estimates subject to change at completion, and the shopper can edit freely until the handoff. (Shopify's API states the estimate character verbatim; Snipcart's server-side validation enforces the integrity side.)

Deliberately NOT in L0 (all common modern structure or variants — see L1/L2): mini-cart vs cart-page shape, floating cart widgets, coupon codes, gift cards, tax/shipping estimates, saved carts across devices, abandoned-cart recovery, stock limits, digital goods, subscriptions, donations, merchant dashboards, webhooks, multi-currency, AI.

### L1 — Common Mature Structure

Present across the sampled products (or across the sample + prior Atlas passes), expected in mature products, not definitional:

- cart surfaces: mini-cart / floating cart, dedicated cart page, item-count and total badges on the merchant's site [Snipcart classes; RomanCart drop-cart; Foxy persistent cart]
- line-item editing: quantity +/-, remove, option changes; stacking/merge rules for repeated adds [Snipcart stackable; Shopify cartLinesUpdate]
- cart-level promotions: coupon/discount codes, gift cards [Snipcart discounts; Foxy coupons/gift cards; Shopify discountCodes/appliedGiftCards]
- estimated totals: subtotal, discounts, estimated tax and shipping [all samples]
- persistent/saved carts across sessions and devices; account-bound carts [Foxy customer sync; Shopify buyerIdentity]
- abandoned-cart tracking and recovery emails [Snipcart abandoned-carts templates + API; RomanCart follow-up emails]
- cart notes/attributes (gift messages, special instructions) [Shopify note/attributes; Snipcart custom fields]
- bundled checkout + payment-gateway connections [all four standalone products]
- merchant dashboard: orders, customers, discounts, environments, notifications [Snipcart; Foxy admin; RomanCart control panel; Mal's email notification]
- stock/quantity limits: max/min quantity, real-time stock display [Snipcart max-quantity; RomanCart stock management]
- mixed cart contents: physical + digital + subscriptions + donations in one cart [Foxy; Snipcart; Shopify selling plans]
- webhooks/events and API access for the seller's own systems [Snipcart; Foxy; Shopify]

### L2 — Variant / Optional Structure

- **Realization posture** (the primary variant axis): standalone embeddable service attached to an arbitrary site (Snipcart, Foxy, Mal's, RomanCart) vs platform-internal object of a commerce platform (Shopify Cart API; WooCommerce cart; every §05.01 platform's internal cart).
- **Item-definition substrate**: HTML attributes on buy buttons (Snipcart); signed links/URL parameters (Foxy demo link; Mal's/RomanCart buy-now links); API mutations against a platform catalog (Shopify); dashboard-defined products with optional hosted storefront (RomanCart storefront pole).
- **Integrity posture**: server-side crawler re-validation of the order against the merchant's declared prices (Snipcart); signed parameters (Foxy); platform-authoritative pricing (Shopify — the platform owns the catalog, so the cart cannot disagree with it).
- **Cart identity posture**: anonymous session cart; account-bound cart; customer-sync/SSO (Foxy); B2B company-location binding (Shopify buyerIdentity).
- **Entry-channel breadth**: website only; email and social posts as cart entry (Foxy, RomanCart); marketplace listing integration (RomanCart eBay).
- **Cart content scope**: standard retail; donations, tickets, bookings, digital downloads, memberships as first-class cart contents (Foxy, RomanCart).
- **B2B shapes**: offline/purchase-order payment lanes (Foxy); quotes/proformas as cart uses (RomanCart's use list).
- **Storefront gradient**: hosted storefront option (RomanCart) — a gradient toward the Online Store Builder pole, recorded, not dissolved.
- **Non-web accumulation**: telephone sales / mail order / invoice / quote uses of the same priced-line-item accumulator (RomanCart).

### L3 — Vendor-specific (research notes only)

- Snipcart: `data-item-*` attribute vocabulary; custom-field types (dropdown/checkbox/textarea/readonly/hidden) with per-option price modifiers; `stackable` enum (`auto`/`never`/`always`); quantity step/min/max; crawler-based order validation against `data-item-url`; same-ID-same-price rule; test/live environments; merchant dashboard at app.snipcart.com; email template set (invoices, refunds, abandoned carts, order shipped, digital download, payment expired); webhooks (order/subscription/shipping/tax); JS SDK; API resources (orders, customers, discounts, products, abandoned carts, user sessions, domains, custom shipping methods); e-invoicing; withdrawal requests; MCP server documentation (era artifact); subscriptions "under development" at research date.
- Foxy: signed cart URLs (`||`-separated parameters with per-parameter hashes in the vendor's demo link); "about 100 different payment gateways and platforms"; multiple payment accounts per store with currency routing (CAD→Canadian PayPal example); offline/purchase-order payments; customer syncing "with password hashes"; SSO; Foxy Automations (beta Q1 2025); push to Airtable/ERP/CRM/OrderDesk; PCI Level 1 Service Provider claim; operating since 2007; integration catalog (Webflow, Framer, Webstudio, Squarespace, Wix, WordPress, Carrd, Unbounce, Weebly, Drupal, ClickFunnels, Leadpages).
- Mal's: free/premium tier split; "145,000 accounts online across 120 countries" (vendor claim); 30 languages; buy-now link/button/hyperlink/image attachment; hosted cart page with amend + checkout; SSL collection of card/check details; immediate email order notification; PayPal/Braintree/Nochex/Skrill processors.
- RomanCart: drop-cart floating widget; button widgets with options/variations/modifiers; hosted storefront (WordPress/Facebook); real-time stock/price push to the merchant's site without code changes; cart templates; eBay listing from the control panel; barcoded tickets; accommodation booking; digital vault; autoresponder/follow-up email machinery; order fulfilment service; sister website-builder product Sellr; gateway list (PayPal, SagePay, Stripe, Braintree, Authorize.net, WorldPay, Nochex, Global Payments, ePDQ, Netbanx, Secure Trading, Cardsave).
- Shopify: Cart object fields (lines with selling plans and parent relationships for warranties/add-ons; cost with estimate wording; buyerIdentity incl. B2B company location; delivery groups with carrier-calculated rates via `@defer`; note; attributes; totalQuantity); mutation set (cartCreate, cartLinesAdd/Update/Remove, cartDiscountCodesUpdate, cartGiftCardCodes*, cartNoteUpdate, cartAttributesUpdate, cartBuyerIdentityUpdate, cartSelectedDeliveryOptionsUpdate, cartDeliveryAddresses*); 250-item request limits; `checkoutUrl` handoff to web checkout; "preferences prefill checkout fields but don't sync back to the cart if overwritten at checkout."

## Rejected Findings

- **"A shopping cart platform is a commerce platform."** Rejected: the standalone cart platform owns no catalog of record, no storefront, no fulfillment operation — item data lives in the merchant's own surfaces, and orders are pushed outward (Foxy: "lightweight order management… push orders to your own ERP or CRM"). The commerce platform owns the whole span; the cart platform owns the accumulation slice.
- **"The cart is just a UI widget."** Rejected: the cart is a persistent, shopper-bound server-side object with identity, totals, promotions, and lifecycle (abandonment, recovery, conversion); UI is one surface of it. Shopify's API object model makes the object-ness explicit.
- **"Cart = checkout."** Rejected: the seam is structural. The cart is estimate-side, pre-commitment, freely editable; checkout is the completion transaction that fixes the terms and takes payment. Shopify's own wording ("estimated costs… subject to change and changes will be reflected at checkout") and the `checkoutUrl` field mark the seam from the inside.
- **"Cart platforms own the pricing of record."** Rejected as a general claim: cart totals are estimates; integrity is maintained by re-validation against the seller's declared prices (Snipcart crawler), signed parameters (Foxy), or platform-authoritative catalogs (Shopify). RomanCart's stock/price push is the observed gradient — recorded, not generalized.
- **"Abandonment recovery defines the cart."** Common (L1), not definitional: a cart without recovery emails is still a cart.
- **"One-click buy buttons are carts."** Rejected: no accumulation, no persistence, no editing — a buy button is an entry affordance, not the cart object.
- **"The cart requires an account."** Rejected: anonymous session carts are the base pattern; account binding is a variant posture.

## Boundary Findings

1. **vs Checkout Platform (sibling leaf, §05.06) — JOINT REVIEW DISCHARGED: keep-both RATIFIED.** The checkout pass's structural seam is confirmed from this side with new inside-the-API evidence: the cart is the pre-commitment accumulation and editing of intended items; checkout is the completion transaction of an initiated purchase; the seam is the checkout button (Shopify: the cart object carries `checkoutUrl`; cart costs are "estimated… subject to change and changes will be reflected at checkout"). The joint-review question — real Type vs absorbed capability — resolves as **keep-both**: standalone cart platforms exist as a live, self-identifying product category (Foxy: "We focus *exclusively* on a shopping cart platform you can add to your existing website"; Mal's: "Escape from the limitations of traditional store builder software"; RomanCart: "any Website can Become a Shop in Minutes"; Snipcart: "a shopping cart developers can easily integrate into any website"), with a continuous lineage from the 2000s hosted carts to today's embeddable carts. The absorption observation is CONFIRMED and recorded as market structure, not as a taxonomy verdict: the dominant modern realization of the cart is platform-internal (every §05.01 platform ships one; Shopify exposes it as an API object), while the standalone form persists in the attach-to-any-site niche (static sites, CMS sites, site builders without adequate commerce, email/social selling, LMS/ERP embeds). Removal tests: remove completion/payment from a cart platform → accumulation/editing remains (cart tooling); remove accumulation/editing from a checkout → completion remains. Bundling is universal (every standalone cart product bundles checkout; every commerce platform bundles the cart) — packaging, not identity.
2. **vs E-commerce Platform / Online Store Builder / Headless Commerce Platform (§05.01).** Those Types own catalog → storefront → cart → checkout → order (and the site itself). The cart platform owns the accumulation slice and attaches to a site the merchant already has; it has no catalog of record (item data lives in the merchant's HTML/links or arrives as parameters) and deliberately positions against store builders (Mal's verbatim). Gradient cases recorded: RomanCart's hosted storefront pole; commerce platforms exposing cart APIs for headless storefronts (Shopify) — the same object model realized inside the platform. Test: remove the cart accumulation → the commerce platform remains a store; remove catalog/storefront/order machinery → the cart platform remains.
3. **vs Payment Gateway / Payment Processing Platform (§08).** The cart platform sits upstream of the money rails: it connects to gateways (Foxy's ~100-gateway claim; Mal's and RomanCart's gateway lists; Snipcart's gateway configuration + custom-gateway option) but authorization/settlement is external. Test: remove the accumulation → the gateway still processes; remove the gateway → the cart still accumulates (with offline/PO lanes as observed variants).
4. **vs Order Management (§05.07).** The cart platform's merchant dashboard is deliberately lightweight order handling (Foxy's own wording); the order lifecycle (fulfillment orchestration, edits, returns) belongs to the seller's OMS/platform, to which cart platforms push orders (Foxy → OrderDesk/ERP/CRM). Test: remove fulfillment orchestration → the cart platform is unaffected; remove the cart → the OMS still manages orders it receives from elsewhere.
5. **vs PIM / Product Catalog Management (§05.04).** The cart platform does not own the catalog of record; item data is declared at the point of sale (HTML attributes, links) or referenced from the seller's own catalog (Shopify variants). RomanCart's stock/price push is the gradient: platform-held item data pushed to the site — still item-level selling data, not a PIM's rich-product-record discipline. Test: remove the cart → a PIM still manages product records; remove the PIM → the cart platform still accumulates what the seller declares.
6. **vs Sales Order Capture (§07).** Sales-order capture is seller-side intake of committed orders; the cart is buyer-side accumulation of uncommitted intent. The cart becomes an order at the completion handoff — different actor, different object state. RomanCart's "telephone sales / mail order / invoice / quote" uses sit on this seam (the same accumulator serving seller-side entry) — recorded as a variant use, not a Type merge.
7. **vs Wishlist / saved-items behavior (no directory leaf).** The wishlist accumulates but is save-for-later: no commitment track, commonly no totals discipline, no handoff. The cart's conversion handoff is the discriminator. Recorded for completeness; no directory action.

## §24 Historical / Market-Sample Check

Would older, regional, or differently positioned products still fit the L0?

- **2000s hosted carts (Mal's, RomanCart, the Cart32 era)** — buy-now links on any site → vendor-hosted cart page → amend → checkout → payment → notification. Satisfies the L0 exactly: priced editable accumulation, shopper-bound session on the hosted page, conversion handoff. The modern embeddable carts are the same structure with better attachment mechanics. ✓
- **Platform-internal carts (Shopify Cart API; WooCommerce cart; every store builder's cart)** — the same object model realized inside a commerce platform: intended merchandise, estimated costs, shopper binding, edit mutations, checkoutUrl handoff. ✓
- **The physical-world metaphor** — the cart/basket predates software; the L0's accumulation-persistence-editing-handoff structure is the software formalization of the shopping basket, not of any vendor era. ✓
- **One-click / express purchase flows** — deliberately excluded: no accumulation, no persistence, no editing; they are entry affordances (or checkout-side accelerators per the checkout pass), not carts. ✓
- **Quote/estimate instruments (RomanCart's proforma/quote uses)** — the same accumulator serving pre-commitment priced intent in non-web-retail flows; fits the L0's pre-commitment character. ✓

Conclusion: the L0 survives the historical check; the definition does not over-fit the modern embeddable-cart pattern, the platform-internal pattern, or any single vendor era.

## Uncertainties

- **Foxy wiki unreachable** (wiki.foxycart.com — two empty fetches, abandoned per the network-limitation rule). Foxy claims rest on foxy.io product/how-it-works pages (Tier 2) plus the vendor's own demo cart URL; operational API detail (cart session mechanics, API object model) not asserted.
- **Mal's and RomanCart depth**: how-it-works surfaces fetched; detailed help docs/screencasts not fetched. Claims for these two kept at the observed level; no precise limits, session durations, or template mechanics asserted.
- **Cart32 not sampled** (legacy hosted cart; the sample already spans the pattern's era range).
- **Abandonment-recovery breadth**: directly observed at Snipcart (email templates + API resource) and RomanCart (follow-up emails); treated as common (L1) on cross-product reasoning plus prior passes, not asserted for every product.
- **Precise numbers avoided** in the final document. Vendor-claimed figures (Foxy "~100 gateways", "since 2007"; Mal's "145,000 accounts", "30 languages"; Shopify "250 lines/values" request limits) are kept in these notes only.
- **Gradient cases recorded, not dissolved**: RomanCart's storefront/stock-push pole (toward store builder / catalog territory); Foxy's bundled one-page checkout (toward the checkout sibling); Shopify's platform-internal cart (the absorbed realization). The Type boundary is drawn on structural center; the gradients are market packaging.

## Final Synthesis

A Shopping Cart Platform is the product form of the buyer's pre-purchase accumulation object. Its defining structure is small and jointly-held: a shopper-bound persistent cart holding a priced, editable accumulation of intended purchases (line items with product reference, quantity, options, computed totals); the pre-commitment character of everything in it (totals are estimates, everything mutable until commitment); and the conversion handoff that feeds the accumulated intent to a completion stage. The Type has two realizations of one object model: the standalone embeddable cart platform — a hosted or script-embedded cart service attached to a website the merchant already has, with item data declared in the merchant's own surfaces and integrity maintained by re-validation or signed parameters, completion bundled because a cart that cannot complete is unsellable — and the platform-internal cart, the same object realized inside every commerce platform, where the API wording itself marks the seam (estimated costs, checkoutUrl). The joint review with the checkout sibling resolves as keep-both: the accumulation-vs-completion seam is ratified from this side with inside-the-API evidence, the standalone category is confirmed live and self-identifying, and the absorption observation is recorded as market structure — the standalone form is the niche realization (attach-to-any-site), the platform-internal form the dominant one. The definition is validated against the 2000s hosted-cart era and the platform-internal present, so it does not over-fit any single implementation pattern.
