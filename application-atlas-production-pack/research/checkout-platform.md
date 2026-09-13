# Research Notes — Checkout Platform

Research date: 2026-09-07
Leaf: Checkout Platform (DIRECTORY §05.06 Commerce Checkout, sibling of Shopping Cart Platform)
Slug: checkout-platform

## Research Goal

Understand what a Checkout Platform actually is as an Application Type: what object model it runs on (how the purchase enters checkout, what the checkout session/order is, how it completes), what the buyer actually does in it, how the seller integrates and operates it, where it starts and ends relative to cart, payment rails, and order management, and where its boundary lies against neighboring Types (Payment Gateway, Payment Processing Platform, Payment Orchestration Platform, E-commerce Platform, Headless Commerce Platform, Shopping Cart Platform, Digital Wallet, Billing Platform, Fraud Detection Platform).

## Initial Boundary

- Hypothesis: a Checkout Platform is the buyer-facing completion stage of an online purchase — the stage that turns an initiated (priced) purchase into a completed transaction — as opposed to the storefront (discovery/browsing), the cart (pre-commitment accumulation), the payment rails (authorization/settlement), and the OMS (post-order management).
- Nearest neighbors per directory: Shopping Cart Platform (sibling leaf, §05.06); E-commerce Platform / Online Store Builder / Headless Commerce Platform (§05.01); Payment Gateway / Payment Processing Platform / Payment Orchestration Platform / Digital Wallet / Billing Platform (§08); Fraud Detection Platform (§08/§15); Order Management (§05.07).
- Prior Atlas passes already drew seams toward this leaf and are treated as cross-references:
  - research/payment-gateway.md: "checkout centers on the payer-facing conversion experience (cart→order UX); the gateway centers on authorization + transaction lifecycle."
  - research/payment-orchestration-platform.md: "The orchestrator's defining job is provider connectivity + routing + normalization; checkout is an optional acceptance surface. A checkout platform centers the payer-facing conversion experience."
  - research/headless-commerce-platform.md: "The checkout platform owns the checkout slice (often as an embeddable service); the headless commerce platform spans catalog → cart → checkout → order → fulfillment handoff. Headless platforms can even consume a standalone checkout component (observed as hosted-checkout products/modes inside two sampled platforms)."
  - research/payment-processing-platform.md: "A processing platform must own payer-facing checkout — rejected."
- Obvious unknowns at start: whether the Type is definable independently of commerce platforms (risk: checkout is "just a feature" of a storefront suite); whether "one-click/accelerated checkout" vendors (Bolt/Fast lineage) and regional full checkouts (Klarna Checkout lineage) share a structure with hosted payment pages (Stripe Checkout); how far checkout extends past the payment moment (post-purchase surfaces).

## Research Questions

1. How does a purchase enter checkout? What object is created (session/order token) and what does it carry?
2. What does the buyer-facing surface do — in what order do identity, contact, delivery, discount, payment, and confirmation appear, and which are optional?
3. Who executes the payment — the checkout platform, the merchant's processor, or both — and what flexibility exists?
4. What happens at completion: what state transitions occur, what record is produced, and how is it handed to the seller?
5. What identity models exist (guest, merchant account, cross-merchant shopper network)?
6. What merchant-side surfaces exist (configuration, branding, analytics, testing)?
7. Where does checkout end — does it own post-purchase surfaces (confirmation, order status) or stop at handoff?
8. What rules govern the flow (state rules, PCI/card-data placement, compliance machinery, idempotency)?
9. Where are the boundaries vs cart, payment rails, orchestration, storefront suites, and OMS?
10. Does the definition survive without modern specifics (accelerated checkout, AI, wallets)?

## Representative Products

Selection: market representativeness + documentation completeness + different product philosophies + different customer tiers. The four sampled products realize four distinct market poles of the same Type:

| Product | Pole | Customer tier | Rationale |
|---|---|---|---|
| Stripe Checkout | payment-led hosted checkout inside a payment-processing platform | developers/merchants, startup → enterprise | canonical "checkout as acceptance surface" docs; excellent documentation |
| Bolt | independent checkout-first vendor with cross-merchant shopper identity network | mid-market → enterprise retail, gaming/digital | pure-play "replace your checkout" positioning |
| Kustom Checkout (Klarna Checkout lineage) | regional full checkout (Europe/Nordics) wrapping payment methods | European merchants across platforms | the full-checkout pole; own consumer identity inside the checkout iframe |
| Shopify Checkout | commerce-suite-native checkout, sold with an extensibility product | SMB → enterprise commerce | the suite-owned realization; checkout as the platform's conversion surface + extension target |

Deliberately not sampled: Fast (one-click checkout vendor, defunct 2022 — no operational docs exist); PayPal Express Checkout / wallet express lanes (treated below as a variant lane, not the Type's center); commercetools Checkout (already documented from the headless-commerce pass; reused as cross-product corroboration); BigCommerce/Medusa hosted-checkout patterns (same corroboration).

## Sources

Tier 1 (official operational documentation), fetched 2026-09-07:

- Stripe — Checkout overview: https://docs.stripe.com/payments/checkout (Layer A)
- Stripe — How Checkout works (index page; variants per UI mode): https://docs.stripe.com/payments/checkout/how-checkout-works (Layer A at index level)
- Stripe — Fulfill orders (full hosted page variant): https://docs.stripe.com/checkout/fulfillment.md?payment-ui=stripe-hosted (Layer A)
- Bolt — Documentation home / product suite: https://docs.bolt.com/ (Layer A)
- Bolt — Bolt Checkout product page: https://docs.bolt.com/products/checkout (Layer A)
- Kustom — Checkout overview ("Get started with Kustom"): https://docs.kustom.co/contents/checkout (Layer A)
- Kustom — Create Order guide: https://docs.kustom.co/contents/checkout/integrate-kco-in-your-ecommerce/create-order (Layer A)
- Shopify — Apps in checkout: https://shopify.dev/docs/apps/build/checkout (Layer A)

Unreachable / limitations (see Uncertainties):

- Shopify Help Center "Checkout settings" (https://help.shopify.com/en/manual/checkout-settings) — HTTP 403; shopify.dev used instead. Buyer-side operational detail (guest checkout toggles, exact address fields) not asserted.
- Klarna docs portal (https://docs.klarna.com/) — restructured 2026; classic Klarna Checkout path (docs.klarna.com/klarna-checkout/) returns 404. Kustom Checkout (the spun-off successor, kustom.co) used as the operational source; Klarna lineage corroborated by Kustom's own compatibility note ("Klarna's API endpoint will remain functional alongside Kustom's own API endpoint until the 31st of March 2026").
- Historical context (Fast, Amazon 1-Click patent era, early-2000s store-builder checkout pages, PayPal Express Checkout) — no fetchable operational docs; used only as era-anchoring reasoning, never as structural evidence.

No claim below relies on model memory for precise operational facts. All precise facts are Layer A and marked research-notes-only.

## Product Observations

### Stripe Checkout (Layer A)

- Self-description: "Build a payments page… prebuilt UIs using the Checkout Sessions API." Three payment UIs share one API: **Full page** (customers enter payment details in a fully-featured payment page, embedded on the merchant's site or via redirect to a Stripe-hosted page), **Embedded form** (embedded form on the merchant's site without redirection), **Elements** (fully customized payment page built from elements).
- Feature matrix (official): full page — "full order summary with subtotals (including tax and shipping costs), cross-sells & upsells, free trials, discounts and promo codes"; embedded form — "limited order summary… discounts and promo codes"; Elements — "no order summary". Built-in UI support for billing, tax, adaptive pricing, Link (vendor's accelerated checkout), dynamic payment methods, surcharging, split-tender.
- **Checkout Session** object: "represents your customer's session as they pay for one-time purchases or subscriptions through Checkout. After a successful payment, the Checkout Session contains a reference to the Customer, and either the successful PaymentIntent or an active Subscription." Created server-side by the merchant (`line_items`, `mode=payment|subscription|setup`, `success_url` with `{CHECKOUT_SESSION_ID}` placeholder).
- Completion lifecycle (official fulfillment guide): `checkout.session.completed` event fires on payment; `checkout.session.async_payment_succeeded` / `checkout.session.async_payment_failed` for delayed payment methods (ACH direct debit, bank transfers — "processing" until resolved). Merchant builds a `fulfill_checkout` function triggered by webhooks **and** optionally by the redirect landing page; "you can't rely on triggering fulfillment only from your checkout landing page, because it's not guaranteed customers visit that page"; fulfillment function must be idempotent ("might be called multiple times, possibly concurrently, for the same Checkout Session"); check `payment_status` before fulfilling; record fulfillment status per session.
- Fulfillment actions enumerated: provision access to services, trigger shipment, save payment details + line items in the merchant's own database, send custom receipts, reconcile line items/quantities, update inventory. — i.e., fulfillment is the seller's side; checkout hands off.
- Dynamic updates: "make updates while your customer checks out"; collect additional information (shipping details and other customer information); collect taxes; extend checkout with custom components; add trials, discounts, upsells.
- Post-purchase: "after the payment — customize the post-payment checkout process"; subscriptions and save-payment-for-future ("save your customers' payment details to charge them later"); save during payment; Managed Payments ("let Stripe handle sales tax and VAT compliance in more than 80 countries, including customer support, and help with fraud and disputes"); product catalog management; Payment Links "use Checkout".
- Customization gradient: hosted page "15 configurable settings via brand settings" vs embedded form "70 configurable settings via the Appearance API" vs Elements "full CSS customization".

### Bolt (Layer A)

- Self-description (product page): "Replace your storefront checkout with **Bolt Checkout**: a full checkout and account experience for supported eCommerce platforms." "Merchants who want Bolt to host checkout instead of building their own."
- How it works (official four steps): 1. Integrate your own cart (custom cart Direct API) or install the Bolt plugin for your platform (Shopify, BigCommerce, Adobe Commerce, SFCC, WooCommerce, Volusion). 2. "Shoppers complete checkout in Bolt's optimized modal or hosted flow." 3. "Bolt handles fraud review, payment routing, and shopper accounts." 4. "Orders sync to your platform; view transactions in the Merchant Dashboard."
- Integration objects: create order token (`POST /v1/merchant/orders`), authorize payment (Transactions API), checkout settings in the merchant dashboard; webhooks for transaction events; payment processor connection is a prerequisite ("Before platform setup, connect your payment processor") — merchant can also use Bolt Payments ("all-in-one payment processing") or Custom Payments ("processor choice and payment routing").
- Product suite around the checkout (official naming): **Bolt ID** (checkout-native identity and authentication), **Check-In** (one-click passwordless sign-in), **User Network** ("recognized shoppers for one-click checkout"), **Account Linking**, **SSO Commerce** (passwordless login with Bolt accounts), **Passkeys**; **Embeddable Checkout** ("payment fields and accounts inside your custom UI") and **Checkout Everywhere** ("Buy Now links and QR codes from any channel"); **Checkout OS** ("composable APIs for custom checkout"); **Connect** (marketplace payments and seller onboarding); **Subscriptions** (recurring billing and checkout links); **Fully Managed Fraud** (fraud review and chargeback indemnification) and **Risk Assessment Scoring**; add-ons: Order Tracking (confirmation, tracking, SMS updates), Abandoned Carts ("recover abandoned checkouts"), Shopper Assistant (floating cart and order widget), Checkout 2.0 ("AI-powered checkout orchestration"); Stablecoins; gaming vertical (payment links + SDKs for games).
- Environments: sandbox + production API hosts, merchant dashboard, shopper dashboard (accounts).
- Reading: the checkout is the product's center; identity (cross-merchant shopper network), fraud, and payments are attached services the vendor operates so the merchant doesn't build them; orders sync back to the merchant's platform.

### Kustom Checkout (KCO; Klarna Checkout lineage) (Layer A)

- Self-description: "This guide shows you how to integrate Kustom Checkout (KCO) to your e-commerce site… you can have a live checkout widget in minutes."
- Integration loop (official four steps): 1. **Create order** — API call returning an HTML snippet for rendering the KCO checkout iframe. 2. **Render checkout snippet** — merchant renders the KCO iframe on their site. 3. **Read order** — after the user completes checkout, the merchant reads the order, receiving an HTML snippet for confirmation. 4. **Render confirmation snippet** on the merchant's confirmation page. Alternative server-side-only pattern: **Hosted Payment Page**.
- Create Order payload (official example): `purchase_country`, `purchase_currency`, `locale`, `order_amount`, `order_tax_amount`, `order_lines[]` (type physical/digital, reference, name, quantity, quantity_unit, unit_price, tax_rate, total_amount, total_discount_amount, total_tax_amount), `merchant_urls` (terms, checkout, confirmation, push). Response: `order_id`, `status: checkout_incomplete`, billing/shipping address objects, `customer`, `html_snippet` (the iframe), `options` (allow_separate_shipping_address, date_of_birth_mandatory, require_validate_callback_success), `external_payment_methods`, `external_checkouts`.
- Structure around checkout (official docs nav): On-site Elements, Hosted Payment Page, Shipping Assistant, In-Person Payments, and a separate **Order Management** product ("Post Purchase"); partner plugins for Magento, WooCommerce, platforms.
- Reading: the checkout iframe is a full completion surface operated by the vendor — the vendor owns the buyer experience inside the iframe (identity, payment-method presentation, consents, market-specific requirements like date-of-birth collection), while the merchant keeps the storefront around it and reads back the completed order. Regional-market character: locale/purchase_country first-class, consumer-credit payment methods heritage, tax amounts per line.

### Shopify Checkout (Layer A, via shopify.dev)

- Self-description: "Merchants use Shopify checkout to accept orders and receive payments wherever they sell online." "After a customer adds products to a cart, they use Shopify checkout to enter their customer, shipping, and payment information before placing the order."
- Checkout is the platform's extension target: checkout UI extensions (blocks placed via the checkout editor), Shopify Functions (discount functions, payments functions — hide a payment option, delivery options functions — rename options, client/server-side cart-checkout validation, order routing/location rules, bundles, fulfillment constraints, local pickup options/charges/pickup points), web pixel extensions, payments extensions (custom payment processing).
- Post-purchase surfaces owned by checkout: "Thank you" and **Order status** pages are checkout surfaces with their own extensions ("Build a survey… after they made a purchase", thank-you/order-status extensions).
- Product features named in official text: **One-page checkout**, **Shop Pay** (vendor wallet/accelerated lane), checkout branding (GraphQL Admin API checkout branding types — header/footer customization).
- Legacy → extensibility migration: `checkout.liquid` deprecated/unsupported for Information/Shipping/Payment steps; sunset for Thank you/Order status pages (dates in research-notes-only list below). Extensions framed as "upgrade-safe".
- Corroboration from the headless-commerce pass (already in Atlas): Shopify's Storefront Cart API "redirects to Shopify's Web Checkout" — the headless surface deliberately keeps the hosted checkout.

### Cross-check: commercetools Checkout (reused from research/headless-commerce-platform.md, Layer A of that pass)

- Checkout sold as a separate product with two modes: **Complete Checkout** (entire hosted checkout UI: addresses, shipping method, payment method, terms, order summary) and **Payment Only** (merchant keeps existing checkout flow, uses hosted payment component that talks to PSPs and creates the order via Carts/Orders APIs); Browser SDK embeds the checkout as overlay or inline; PSP integration via Connectors; PCI DSS compliance claimed as handled. — Confirms the same product shape (checkout as an embeddable/hosted completion product, with a payment-only degradation mode) from an enterprise headless vendor.

## Cross-product Comparison

| Dimension | Stripe Checkout | Bolt | Kustom Checkout (KCO) | Shopify Checkout | Evidence |
|---|---|---|---|---|---|
| Positioning | payments page with prebuilt UIs (Checkout Sessions API) | "replace your checkout… full checkout and account experience" | full checkout widget (iframe) wrapping completion | checkout = where buyer enters customer, shipping, payment info "before placing the order" | A (each official) |
| Purchase entry object | Checkout Session (server-created; line_items, mode, success_url) | order token (POST /v1/merchant/orders) from custom cart or platform plugin | checkout order (POST /checkout/v3/orders; order_lines + merchant_urls) | platform cart (headless carts redirect to web checkout; Storefront cart carries checkoutUrl) | A |
| Buyer surface shape | hosted/embedded full page, embedded form, Elements; redirect or no-redirect | optimized modal or hosted flow; embeddable fields for custom UI | iframe html_snippet on merchant page; hosted payment page for server-only | platform-native pages (one-page checkout), merchant-branded | B (shape varies, "operated completion surface" constant) |
| What buyer provides | payment details; optionally shipping + customer info, taxes, discounts | identity via Bolt account/network; payment | identity, addresses, payment method, consents (inside iframe) | customer, shipping, payment information | A |
| Identity model | merchant-scoped customer + Link (accelerated) | cross-merchant shopper network (User Network, Bolt ID) | consumer identity inside checkout (vendor-operated) | merchant store accounts + Shop Pay | B (merchant-scoped vs network vs in-checkout identity all occur) |
| Payment execution | Stripe processing (PaymentIntent); dynamic methods, split-tender | Bolt Payments or merchant processor; payment routing | vendor processing inside iframe; external payment methods configurable | platform payments + payments extensions (custom PSPs) | B (checkout always in the money path; who runs rails varies) |
| Completion & handoff | checkout.session.completed events → merchant fulfillment (idempotent, webhook-required) | "orders sync to your platform"; transactions in Merchant Dashboard | read order → confirmation snippet; push callback URL | order placed in platform; thank-you/order status pages | B (completion event + seller-side handoff constant; mechanism varies) |
| Post-completion surfaces | "after the payment" customization | Order Tracking add-on (confirmation, tracking, SMS) | Order Management = separate product ("Post Purchase") | Thank you + Order status pages owned by checkout | B (ownership varies from none to full) |
| Fraud/authentication | Managed Payments incl. fraud + disputes | fraud review + chargeback indemnification in-flow | inside iframe (vendor-operated) | platform-level + payments functions | B (present in all, center varies) |
| Merchant config surface | Dashboard, Checkout studio, brand settings | Merchant Dashboard checkout settings | Kustom Portal | checkout editor + admin | B |
| Extensibility | custom components, Appearance API | Checkout OS composable APIs; add-ons | options object, external payment methods/checkouts, plugins | UI extensions + Functions (discounts, payments, delivery, validation, routing) | B |
| Segment emphasis | developer-led, all sizes | mid-market/enterprise, gaming/digital | European merchants | SMB → enterprise commerce | A |

Cross-product reading:

1. **Same transaction spine everywhere.** Every sampled product: an initiated, priced purchase (session/order token carrying line items and amounts) enters an operated completion surface; the buyer supplies what completion requires; payment is authorized inside that surface; completion produces a terminal record plus a seller-side handoff (event/callback/sync). This spine is constant while every other dimension varies. [B/C]
2. **The completion surface is always platform-operated, not merchant-HTML.** Hosted page, modal, iframe, or platform-native pages — even "embedded" options are platform components. Card/PII handling is deliberately taken off the merchant front end (Stripe hosted/embedded; Bolt; Kustom iframe; commercetools claims PCI handling; BigCommerce Catalyst in the headless pass). [B]
3. **Completion vs fulfillment is a hard seam.** Stripe's guide is explicit: completion events (webhooks) are required; the redirect landing page cannot be relied on; fulfillment must be idempotent and is the merchant's job. Bolt "orders sync to your platform"; Kustom's Order Management is a separate product; Shopify's order becomes the platform's order. [A+B]
4. **Completion ≠ paid.** Delayed payment methods create async success/failure states after checkout completes (Stripe async events; two-step patterns in gateway research). [A]
5. **Identity is the strategic variable.** Merchant-scoped identity (Stripe customer, Shopify store accounts), vendor-owned identity inside the completion surface (Kustom), and cross-merchant shopper networks (Bolt User Network; Shop Pay as platform wallet) are three distinct postures. [B]
6. **Checkout owns the conversion problem, not just the transaction.** Discounts/promo codes, cross-sells/upsells, abandoned-checkout recovery, funnel/transactions dashboards, A/B-able UX, accelerated lanes — all four products invest here. [B]
7. **Post-purchase ownership is a spectrum.** From none (handoff only: Stripe fulfillment guide, Kustom's separate Order Management product) to owned (Shopify's Thank you/Order status pages, Bolt's Order Tracking add-on). [B]

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the product is not a checkout platform:

```text
Initiated purchase (priced line items handed over from the seller's selling context)
└── Dedicated buyer-facing completion stage operated by the platform
    ├── capture of what the purchase requires to complete
    │   (buyer identity/contact; delivery details where the purchase needs them)
    ├── payment authorization executed inside the stage
    └── terminal completion → transaction record + handoff back to the seller's systems
```

Four properties. Remove any one and the Type stops being recognizable:

- **An initiated purchase as input** — checkout never starts from nothing; it receives a priced, seller-owned purchase context (cart/order intent). Without this it is a payment form or a wallet.
- **A dedicated buyer-facing completion stage operated by the platform** — a distinct surface (hosted page, modal, iframe, platform page) whose job is to end the purchase; not a storefront page, not a merchant-built HTML form. Without this it is a commerce engine or an orchestration API.
- **Payment authorization inside the stage** — the money path passes through the checkout (whoever ultimately runs the rails). Without this it is an address form or a preference collector.
- **Terminal completion with seller handoff** — the stage ends the purchase: a completed transaction record exists and is handed back to the seller (event, callback, sync, read-back). Without this it is a marketing page or an abandoned-cart tool.

Deliberately NOT in L0 (all are common modern structure or variants — see L1/L2): order summary layout, multi-step vs one-page, delivery options, discount codes, tax calculation, guest vs account, express lanes/wallets, one-click, saved instruments, fraud tooling, post-purchase pages, analytics, AI.

### L1 — Common Mature Structure

Present across the sampled products (or across the sample + prior Atlas passes), expected in mature products, not definitional:

- order summary (line items, totals, tax and shipping costs, discounts) [Stripe full page; KCO order object; Shopify]
- payment-method breadth and selection (cards, wallets, bank debits, BNPL; dynamic per-market methods) [Stripe dynamic payment methods; Kustom external_payment_methods; Bolt payments; Shopify payments functions]
- delivery options selection (shipping methods, local pickup) [Shopify delivery options/pickup functions; KCO shipping assistant; Stripe collect shipping]
- discount/promo codes and offers at checkout [Stripe promotions incl. trials; Shopify discount functions; KCO order_lines discounts]
- tax handling [Stripe collect taxes / Managed Payments; KCO per-line tax; Shopify tax via platform]
- guest checkout vs account login; accelerated/express lanes for recognized buyers [Bolt network; Shopify Shop Pay; Stripe Link; wallet lanes]
- saved instruments / vaulting for repeat purchase [Stripe save-and-reuse; Bolt accounts; gateway-research vault pillar]
- seller branding/customization of the completion surface [Stripe brand settings; Shopify checkout branding; Kustom iframe options; Bolt checkout settings]
- merchant-facing configuration surface (checkout settings/editor) [all four]
- completion-event machinery for seller handoff (webhooks, push/callbacks, order sync) [Stripe events; Bolt sync; KCO push/read-order; Shopify platform orders]
- post-completion surfaces (confirmation page; sometimes order status) [Stripe after-the-payment; KCO confirmation snippet; Shopify thank-you/order status; Bolt order tracking]
- conversion machinery: abandoned-checkout recovery, funnel/transactions reporting, in-checkout offers (cross-sell/upsell) [Stripe cross-sells; Bolt Abandoned Carts + Shopper Assistant; Shopify editor placements]
- fraud screening and buyer authentication (3DS/SCA-class) inside the flow [Stripe Managed Payments; Bolt fraud review; Kustom in-iframe; Shopify payments functions]
- localization (locale, currency presentation, market-specific payment methods) [KCO purchase_country/locale; Stripe adaptive pricing; Shopify markets]
- testing environments/sandbox + test purchases [Bolt sandbox + test order; Kustom playground; Stripe test data]

### L2 — Variant / Optional Structure

- **Ownership posture** (the packaging of the same Type): suite-native checkout (Shopify; commercetools inside a headless suite) vs payment-led checkout (Stripe Checkout) vs independent checkout-first vendor (Bolt; Fast historically) vs regional full checkout (Kustom/Klarna Checkout).
- **Surface shape**: hosted/redirected page; embedded page; embedded form/fields; iframe snippet; modal; platform-native pages; server-side-only hosted payment page (KCO alternative).
- **Identity posture**: merchant-scoped accounts; guest; vendor-operated in-checkout identity (Kustom); cross-merchant shopper network / one-click (Bolt; Shop Pay; wallet express lanes such as Apple Pay/Google Pay/PayPal-style buttons as payment lanes inside checkout).
- **Post-purchase ownership**: none (pure handoff) → confirmation-only → confirmation + order-status pages + tracking (Bolt add-on; Shopify surfaces).
- **Subscriptions/recurring**: checkout as the initiation point for recurring agreements (Stripe subscriptions/save-payment; Bolt Subscriptions; Shopify purchase options).
- **B2B shapes**: payment terms, purchase-order references, tax identifiers at checkout (observed in the B2B e-commerce pass as checkout-time application of account terms; not center of this sample).
- **Channel extension**: Buy Now links, QR codes, gaming SDKs, payment links (Bolt Checkout Everywhere/gaming; Stripe Payment Links "use Checkout").
- **Marketplace/split flows**: seller onboarding, split payouts (Bolt Connect; marketplace machinery observed in other Atlas passes).
- **Regulatory posture details**: SCA/3DS depth, date-of-birth/age verification options, terms acceptance URLs (KCO options; Stripe Managed Payments tax/VAT posture).
- **AI assistance**: AI checkout orchestration (Bolt Checkout 2.0); AI-assisted optimization — era-common, optional.
- **One-page vs multi-step** flow architecture (Shopify one-page checkout; platform checkouts historically multi-step).

### L3 — Vendor-specific (research notes only)

- Stripe: Checkout Sessions API, ui_mode hosted_page/embedded, Elements, Checkout studio, Link, Adaptive Pricing, Managed Payments, Payment Links, `{CHECKOUT_SESSION_ID}` success_url placeholder, `checkout.session.completed` / `async_payment_succeeded` / `async_payment_failed` events, checkout "waits up to 10 seconds" for the webhook response before redirect, 15 brand settings vs 70 Appearance API settings, cross-sells & upsells feature, split-tender, surcharging.
- Bolt: order token endpoint (`POST /v1/merchant/orders`), Transactions API, Bolt ID / Check-In / User Network / Account Linking / SSO Commerce / Passkeys, Checkout Everywhere (Buy Now links + QR), Checkout OS, Connect, Fully Managed Fraud / chargeback indemnification / Risk Assessment Scoring, Stablecoins, Checkout 2.0 ("AI-powered checkout orchestration"), Shopper Assistant floating widget, Order Tracking add-on, platform plugin list (Shopify/BigCommerce/Adobe/SFCC/Woo/Volusion), sandbox/production API hosts and shopper dashboard.
- Kustom: KCO v3 orders API (`/checkout/v3/orders`), `html_snippet` iframe, status `checkout_incomplete`, options (allow_separate_shipping_address, date_of_birth_mandatory, require_validate_callback_success), merchant_urls (terms/checkout/confirmation/push), order_lines with per-line tax fields, external_payment_methods/external_checkouts, Shipping Assistant, Hosted Payment Page, Playground portal, Klarna API compatibility until 2026-03-31.
- Shopify: checkout editor, checkout UI extensions, Shopify Functions (discount/payments/delivery/validation/order-routing/bundles/fulfillment-constraints/pickup), web pixel extensions, payments extensions, One-page checkout, Shop Pay, checkout branding API (header/footer), Thank you/Order status pages as checkout surfaces, checkout.liquid sunset dates (2025-08-28 Plus Thank-you/Order-status; 2026-08-26 non-Plus), design requirements for checkout apps, "upgrade-safe" framing.
- Cross-reference corroboration: commercetools Checkout Complete vs Payment-only modes, Connectors, Browser SDK overlay/inline; Shopify Storefront Cart API `checkoutUrl` redirect to Web Checkout; BigCommerce Catalyst "redirected headless checkout page… never collects or transmits PII such as credit card numbers" (from the headless-commerce pass).

## Rejected Findings

- **"A checkout platform is a hosted payment page."** Rejected: hosted page is one surface shape; Kustom/Bolt/Shopify operate full completion experiences (identity, delivery, consents) beyond payment; embedded/iframe/modal shapes are equally first-class.
- **"Checkout = payments, therefore it's a payment product."** Rejected: payment authorization is L0-adjacent but the completion stage (capture of delivery/identity, consents, handoff) is what distinguishes it from gateway/processing Types; the gateway research already recorded that gateways are not defined by their hosted pages.
- **"One-click/accelerated checkout is the definition."** Rejected: accelerated lanes are an identity realization (L2); Kustom and Shopify operate full checkouts without a cross-merchant one-click network; historical platform checkouts predate one-click networks entirely.
- **"Checkout owns order management."** Rejected: completion is terminal; fulfillment/order lifecycle belongs to the seller/platform downstream (Stripe's idempotent-fulfillment guidance; Kustom's separate Order Management product). Post-purchase page ownership is a spectrum, not a defining trait.
- **"Checkout requires guest checkout."** Not asserted as definitional; guest/login mix varies by product and merchant configuration; identity posture is L1/L2.
- **"Abandonment recovery is part of the Type."** Common (L1) but not definitional; a checkout without recovery emails is still a checkout.

## Boundary Findings

1. **vs Shopping Cart Platform (sibling leaf, §05.06).** The cart is the pre-commitment accumulation and editing of intended items (what am I buying?); checkout is the completion transaction of an initiated purchase (finalize what I'm buying into a paid order). The seam is the checkout button: the cart page ends where the checkout stage begins. Market observation: standalone cart products have largely been absorbed into commerce platforms, and cart↔checkout pairs are bundled everywhere — the sibling leaf's modern realization is mostly as a commerce-platform feature. Flag for joint review when Shopping Cart Platform is processed. Test: remove completion/payment → cart tooling; remove accumulation/editing → checkout.
2. **vs E-commerce Platform / Online Store Builder / Headless Commerce Platform (§05.01).** Those Types span catalog → cart → checkout → order (and the storefront). The checkout platform is the completion slice, pluggable into someone else's storefront/cart. Gradient is real: suite-native checkout (Shopify) is the same Type realized inside a platform, and headless platforms ship hosted-checkout products themselves (commercetools Checkout; Shopify Web Checkout redirect). The Atlas headless pass already drew this seam ("headless platforms can even consume a standalone checkout component"). Test: remove catalog/storefront/cart machinery → checkout remains; remove the completion stage → commerce platform remains.
3. **vs Payment Gateway / Payment Processing Platform (§08).** Gateway/processing center on acceptance + authorization + settlement lifecycle; checkout centers the buyer-facing completion experience. Overlap zone is explicit in the market: Stripe Checkout is a checkout product of a processing platform; hosted payment pages are checkout-shaped acceptance surfaces in every gateway (per the gateway pass). Structural test (consistent with research/payment-gateway.md): remove acceptance/authorization/settlement → checkout platform remains a conversion surface; remove the buying UX → gateway remains. Stripe Checkout is the acknowledged gradient case — its center is the payment session, with completion UX around it; recorded, not resolved.
4. **vs Payment Orchestration Platform (§08).** Orchestration = server-side provider connectivity, routing, normalization; checkout = payer-facing completion. Gradient: orchestrators ship full checkout UIs (Primer Universal Checkout, Gr4vy embed) while Bolt offers processor choice/routing (Custom Payments). Test (consistent with research/payment-orchestration-platform.md): remove routing → still a checkout; remove the buyer surface → orchestration.
5. **vs Digital Wallet (§08).** The wallet is payer-side instrument/identity storage; checkout is the stage where instruments/identities are used. Wallet express buttons are lanes inside checkout (L2). Test: a wallet without a completion stage (balance, P2P, card management) is not a checkout; a checkout without its own wallet is normal.
6. **vs Billing Platform (§08).** Billing decides what/when to charge for ongoing relationships (invoices, cycles, dunning); checkout is point-of-purchase. Subscriptions initiated at checkout (save payment + start plan) are the seam: initiation is checkout, the recurring machinery is billing/processing. Consistent with the payment-orchestration pass's framing ("billing decides what/when to charge; orchestration executes").
7. **vs Order Management (§05.07).** OMS begins at the completed order (editing, orchestration, fulfillment, returns); checkout ends at the completed order record + handoff. Post-purchase checkout surfaces (thank-you/order status) are communication surfaces, not lifecycle machinery. Test: remove completion → OMS has nothing to receive; remove fulfillment orchestration → checkout unaffected.
8. **vs Fraud Detection Platform (§08/§15).** Fraud decisioning is embedded in checkout flows (Bolt handles fraud review; Stripe Managed Payments) but standalone fraud platforms are services consumed during checkout, not the completion stage itself. Test: remove fraud tooling → checkout still completes purchases; remove completion → fraud scoring is just a scoring API.
9. **vs Retail POS (§05.10).** In-person transaction composition (staff-operated, physical hardware) is a different Type; checkout platforms occasionally bridge toward in-person (Kustom In-Person Payments; Bolt QR/Buy Now) but the POS's spine is store operations, not the online completion stage.

## §24 Historical / Market-Sample Check

Would older, regional, or differently positioned products still fit the L0?

- **Regional full checkout (Kustom/Klarna Checkout lineage)** — the Nordic full-checkout design predates the current "checkout optimization" category; its structure (merchant creates order → vendor-operated completion surface → read back completed order) fits L0 exactly. ✓
- **Suite-native checkout of 2010s store builders** — plain multi-step pages inside storefront platforms (cart → address → shipping → payment → confirm) fit L0: initiated cart, dedicated completion stage, payment inside, order handed to the platform. The extensibility/analytics layers are later additions. ✓
- **Hosted payment pages of early PSPs** — the 1990s–2000s hosted-pay page pattern (the payment-gateway pass anchored Authorize.Net 1996-era) satisfies a reduced form: initiated amount, buyer-facing stage, payment inside, completion notice. The full L0 (delivery capture, line-item purchase context) appears as these pages grew into order-bearing sessions; the payment-only form is the degraded mode still sold today (commercetools "Payment Only", KCO Hosted Payment Page). ✓ (with the gradient recorded)
- **One-click wallet lanes (PayPal Express Checkout era, ~2000s)** — an express payment lane inside a merchant's checkout: does not satisfy the full L0 (address/identity capture stays merchant-side) and is classified as a variant lane (L2), not the Type's center. The Type definition does not collapse into wallet express lanes. ✓
- **Amazon 1-Click (patent era)** — referenced only as era context that one-click completion predates current vendors; no structural claim is drawn from it (no operational docs fetched).

Conclusion: the L0 survives the historical check; the definition does not over-fit the modern accelerated-checkout pattern.

## Uncertainties

- **Shopify Help Center unreachable (403).** Buyer-side operational detail (guest checkout toggles, exact address/delivery form behavior) not verified from Shopify's own buyer-facing docs; all Shopify claims rest on shopify.dev's developer documentation (Layer A for developer-facing behavior, Tier-2-equivalent for buyer-flow description). Buyer-flow claims kept general and tied to shopify.dev's own sentence.
- **Klarna → Kustom restructure.** Classic Klarna Checkout docs are gone from docs.klarna.com (404 on the KCO path); Kustom docs are authoritative for the current product. Klarna-era history (launch markets, exact years) not asserted.
- **Bolt shopper-side mechanics** (account creation inside checkout, network mechanics) documented at product-naming level only ("User Network: recognized shoppers for one-click checkout"; shopper help section not fetched); no precise claims made about the shopper experience.
- **Gradient cases not fully resolvable** (Stripe Checkout as gateway product; Shopify Checkout as suite component): the Type boundary is drawn on structural center (what the product's defining job is), and the gradient is recorded rather than dissolved. Joint-review candidates: Shopping Cart Platform (sibling leaf, unprocessed); consistency checks with payment-gateway / payment-processing-platform / payment-orchestration-platform flags already recorded in the Atlas.
- **Precise numbers avoided** in the final document (no time windows, no conversion-rate claims, no numeric limits). Vendor-precise facts (e.g., Stripe's 10-second webhook wait, checkout.liquid sunset dates, KCO option names) are kept in these notes only.

## Final Synthesis

A Checkout Platform is the buyer-facing completion stage of a purchase, sold as a product. Its defining structure is small: an initiated, priced purchase handed over from the seller's selling context; a dedicated, platform-operated completion surface (hosted page, iframe, modal, embedded components, or platform-native pages); capture of what the purchase requires (buyer identity/contact, delivery where applicable) with payment authorization executed inside that surface; and a terminal completion that produces the transaction record and hands it back to the seller's systems. Everything else commonly associated with checkout — order summaries, discount codes, delivery options, tax, guest/account mix, express wallets, one-click networks, saved instruments, abandonment recovery, fraud tooling, post-purchase pages, analytics, AI — is mature-market structure layered on that spine, and the four sampled products realize the spine through four distinct packaging poles: payment-led (Stripe), independent checkout-first with a shopper identity network (Bolt), regional full checkout (Kustom/Klarna lineage), and suite-native with an extensibility product (Shopify). The Type's sharpest structural seams: it begins where the cart ends, it sits in the money path without being the rails, it ends at completion without owning fulfillment, and it is buyer-facing without being a storefront. The definition is validated against a Nordic regional full checkout and the plain platform checkouts of earlier eras, so it does not over-fit the current accelerated-checkout pattern.
