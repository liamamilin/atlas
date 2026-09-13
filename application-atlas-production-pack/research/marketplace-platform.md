# Research Notes — Marketplace Platform

Research date: 2026-09-08

## Research Goal

Determine what a Marketplace Platform is as an Application Type, given that the directory already contains venue-type leaves under 05.02 (Online Marketplace, Multi-vendor Marketplace, Service Marketplace) and the already-produced Service Marketplace document explicitly distinguishes "Marketplace Platform" as *software used to build and run marketplace venues*.

Working hypothesis to verify or refute: a Marketplace Platform is **operator-side software for building and running a multi-seller commerce venue** — the software counterpart to the venue Types — as distinct from (a) single-merchant e-commerce platform software, (b) the marketplace venue itself, and (c) seller-side marketplace tools.

## Initial Boundary

Nearest neighbors identified before research:

- **E-commerce Platform / Online Store Builder (05.01)** — storefront software for ONE merchant. If the software only supports one seller's catalog, it is not a marketplace platform.
- **Online Marketplace / Multi-vendor Marketplace (05.02)** — the venue itself (the operated market with real participants), not the software used to operate it.
- **Service Marketplace (05.02, already documented)** — the venue Type for performed services; its Related-Types table already positions "Marketplace Platform" as the software.
- **Marketplace Seller Management / Seller Portal / Multi-marketplace Seller Platform (05.23)** — seller-side tools for operating across venues; the opposite side of the market from the platform.
- **Dropshipping Platform (05.20)** — supplier-network fulfillment for the operator's own sales, not a venue of independent sellers selling their own offers.
- **Classifieds Platform (05.03)** — listings without platform-mediated transaction/settlement.
- **Payment Orchestration / marketplace PSP rails** — a component, not the Type.

## Research Questions

1. What does this software provide that a single-merchant e-commerce platform does not? (the multi-seller seam)
2. What are the core objects? (operator, seller, listing/offer/product, order, commission, payout, storefront)
3. How does seller onboarding work, and who governs it?
4. How does the money flow work? (buyer payment → commission → seller settlement; which realizations exist)
5. How do orders work when a purchase spans multiple sellers?
6. What surfaces exist for operator, seller, buyer?
7. What is genuinely definitional vs. common-but-optional? (historical check needed: pre-SaaS marketplace software)

## Representative Products

Selection rationale: different product philosophies (no-code SaaS builder vs enterprise SaaS vs self-hosted ecosystem plugin), different customer tiers (self-serve SMB → mid-market → global enterprise), all with substantial official documentation.

- **Sharetribe** — hosted marketplace-building platform (SaaS, no-code configuration + code-extensible). Serves SMB/prosumer operators launching rental/service/product/gig marketplaces. Tier-1 developer docs + help center.
- **Mirakl** — enterprise marketplace SaaS ("Mirakl Marketplace Platform", MMP) for retailers, manufacturers, distributors; B2C and B2B. Tier-2 product page + Tier-1 developer portal (API structure).
- **Dokan (weDevs)** — WordPress/WooCommerce multi-vendor plugin (freemium, self-hosted ecosystem). Serves SMB operators building on WordPress. Tier-1 documentation tree.

Attempted and dropped (source-access limitation): **CS-Cart Multi-Vendor** (docs.cs-cart.com and cs-cart.com returned 403 on two attempts), **Arcadier** (developer portal transport error), **Yo!Kart** (helpdocs 500). The self-hosted-license deployment pole is therefore represented only indirectly (Dokan is self-hosted, though plugin-distributed).

## Sources

- Sharetribe Developer Docs — Introduction (architecture): https://www.sharetribe.com/docs/introduction/ (fetched 2026-09-08)
- Sharetribe Developer Docs — Transaction process: https://www.sharetribe.com/docs/concepts/transactions/transaction-process/ (fetched 2026-09-08)
- Sharetribe Developer Docs — Commissions: https://www.sharetribe.com/docs/concepts/pricing-and-commissions/commissions-and-monetizing-your-platform/ (fetched 2026-09-08)
- Sharetribe Developer Docs — Payments: https://www.sharetribe.com/docs/concepts/payments/payments-overview/ (fetched 2026-09-08)
- Sharetribe Help Center (collection structure: Monetization / Users / Listings / Transactions / Manage / Design / Content / Integrations): https://www.sharetribe.com/help/en/ (fetched 2026-09-08)
- Mirakl — Marketplace Platform product page: https://www.mirakl.com/products/marketplace-platform/ (fetched 2026-09-08)
- Mirakl Developer Portal — root + Mirakl Platform (MMP) page: https://developer.mirakl.com/ , https://developer.mirakl.com/content/product/mmp (fetched 2026-09-08)
- Dokan — Documentation hub and full docs tree (withdraw, dashboard, vendors, commission, sub-orders, modules): https://dokan.co/wordpress/dokan-documentation/ , https://dokan.co/docs/wordpress/ (fetched 2026-09-08)

## Product Observations

### Sharetribe

Evidence layer: A (directly observed in official developer docs and help center).

- Positioned as "a complete solution for building a powerful online marketplace for rentals, services, events or experiences"; template configurable as rental / service / product / messaging (no payments) / gig (regular or reverse, price negotiation) marketplaces. The unit of exchange is configurable per venue.
- Architecture: buyer/seller-facing UI (operator-branded front end, own domain, template or fully custom via Marketplace API) + **Console** — the operator's admin interface ("manage all your marketplace data, such as users, listings and transactions"; email template editor; transaction-process visualizer) + Integration API + Asset Delivery API + CLI. Multiple UIs (web + native mobile) over one marketplace.
- Role model: **customer**, **provider**, **operator** (plus "system"/time as automatic actor). The operator is a first-class transition actor in transaction processes (e.g. operator cancel).
- **Listings** are provider-authored; provider search; extended data; inventory/seat management for bookable/digital items.
- **Transaction process** is a configurable state machine: states, transitions (triggered by customer/provider/operator/time), actions (payment/refund/payout/booking actions), email notifications. Multiple processes can coexist (buying vs renting vs negotiation). Regular flow (provider lists, customer buys) and reverse flow (customer posts, provider offers) both exist; a negotiation process with counter-offers exists. Reviews are a terminal phase of the process.
- **Payments**: built on Stripe Connect (custom accounts, destination charges, application fees). Provider onboarding/KYC via Stripe is a hard gate — "A provider cannot create listings (i.e. receive money from customers) unless they have verified their identity with Stripe — this ensures that the platform is always KYC compliant." Payment flow: customer preauthorization → provider acceptance → capture → payout to provider's bank on completion; operator can refund; payout timing controlled by the transaction process (manual payout schedule).
- **Commissions**: line-item machinery with provider commission (negative) and/or customer commission (positive); percentage, fixed, or dynamic; minimum commission; configurable in Console (hosted) or in code. Monetization alternatives (e.g. subscriptions via third-party billing) supported through the Integration API.
- Environments (Test/Dev/Live); content management and marketplace texts; user access control; referral links.
- A marketplace can run **without payments at all** (messaging marketplace type) — payments are detachable in this product.

### Mirakl

Evidence layer: A for product/API structure (developer portal); capability claims from the product page are treated as vendor claims (A for "the product page claims X", not verified operationally).

- Product literally named "Marketplace Platform" (MMP), part of Mirakl Platform suite (MMP + Dropship MDP + 1 Creditor M1C); a separate "Platform for Services" (MPS) exists. Positioned for retailers, manufacturers, distributors; B2C and B2B (bulk pricing, customer-specific pricing, payment on terms, quote management per product page).
- Developer portal structures the whole product around **three API audiences**: **Front APIs** (machine-to-machine buyer-facing integration with e-commerce platforms/CMS), **Operator APIs** (operator back-office systems, OPERATOR role), **Seller APIs** (seller-specific operations). GraphQL endpoint covers "orders, offers, threads, and shops"; webhooks/cloud events are operator-side only.
- Domain vocabulary: **shops** (sellers), **offers** (seller-authored sellable items against the catalog), **orders**, **threads** (messaging), **incidents** (order issues), ratings — "From creating offers and placing orders to rating transactions and managing incidents."
- Product-page capability claims: seller onboarding via self-service seller portals with real-time validation; intake via API/CSV/XML/EDI; AI mapping/categorization into the operator's taxonomy; catalog QC (enrichment, validation, moderation, translation); automated **order routing that "splits and routes multi-vendor orders"**; seller scorecarding, real-time alerts, automated suspensions; incident management; **commission engine with rates by seller and category, automated per-order calculation**; seller KYC + configurable payout schedules + multi-currency (via Mirakl Payout); dropship and marketplace runnable from one instance with per-vendor relationship choice; retail media (Ads) as commission-adjacent monetization.
- Positioning claim (useful for boundary, treat as claim): with marketplace, "third-party sellers are visible to the customer and set their own pricing; you earn a commission," while with dropship "you resell products under your own brand with full price control; the vendor fulfills directly."

### Dokan

Evidence layer: A (official documentation tree; node titles and named features directly observed; article bodies not individually fetched, so operational parameters are not asserted).

- WordPress/WooCommerce plugin converting a WooCommerce store into a multivendor marketplace. Admin = marketplace operator (WP admin + Dokan admin dashboard + multi-step setup wizard). Terminology: **admin / vendor / customer**.
- **Vendor side**: signup form + multi-step seller wizard; vendor dashboard (products, orders, coupons, reports, reviews, store settings incl. store SEO); vendor **store pages** inside the marketplace site (store listing page, single store page, store opening hours); vendor staff manager (sub-accounts); vendor vacation mode; vendor verification module (incl. company verification); subscription packs (vendor pays to sell) as a module.
- **Admin side**: managing vendors (add vendor from backend, manage selling capabilities, vendor switching — admin can act as a vendor); **product approval system** ("create products on your marketplace with approval system", "pending product rejection"); **vendor commission setup** (tutorial-level feature; per-vendor commission); **earning reports** (admin earnings, all logs); seller announcements; refund request handling (admin-side refund approval flow).
- **Money**: dedicated **withdraw system** — vendor withdrawal requests, automatic withdraw disbursement, withdrawal thresholds, withdraw charges, **reverse withdrawal** (claw-back), statements; excludes COD payments from withdraw; payment realized through marketplace-capable gateways (Stripe Connect / Stripe Express, PayPal Marketplace, Mangopay, Razorpay, Paystack) and an "escrow feature" FAQ entry.
- **Orders**: **sub-orders** — a parent order split into per-vendor sub-orders (dedicated FAQ "What is Sub Order?"); manual order creation (admin/vendor); per-vendor shipping (zone-wise shipping, table rate, delivery time slots); delivery driver app.
- Venue: unified storefront on one WordPress site; seller-attributed product pages; single product multiple vendor module; follow store; live chat (Tawk.to/WhatsApp/Facebook Messenger); store support; product Q&A; report abuse; RMA/warranty requests; auctions, bookings, RFQ modules; geolocation; EU compliance fields; seller badges.
- Distribution: self-hosted plugin (free + paid modules), REST API, hooks/filters, WP-CLI, n8n integration, MCP; separate customer mobile app, vendor app, delivery driver app.
- Boundary knob directly documented: a **"single seller mode"** setting exists — the same software can be configured down to a single-vendor store.

## Cross-product Comparison

| Dimension | Sharetribe | Mirakl | Dokan |
|---|---|---|---|
| What it is | hosted marketplace-building SaaS | enterprise marketplace SaaS | self-hosted WP/WooCommerce plugin |
| Operator role | named actor (operator) with Console | OPERATOR role, Operator APIs, back office | admin with Dokan admin dashboard |
| Seller entity | provider (user) | shop | vendor (store) |
| Seller-authored supply | listings (products/services/rentals) | offers against catalog | products (WooCommerce) |
| Seller onboarding gate | Stripe KYC gates listing creation | self-service portals + validation + pre-vetted network (claim) | signup wizard + admin product approval + optional verification module |
| Catalog governance | operator config via Console | moderation/validation/enrichment (claim) | product approval system |
| Buyer venue | operator-branded UI via API/template | Front APIs into operator's e-commerce storefront | unified WP storefront |
| Order ↔ seller attribution | transaction binds customer ↔ provider (one provider per transaction) | per-seller orders; multi-vendor orders split/routed (claim) | sub-orders per vendor |
| Commission machinery | line-item provider/customer commissions, %/fixed/dynamic, Console-configurable | commission engine by seller/category, per-order (claim) | per-vendor commission setup |
| Seller settlement | automatic payout via Stripe on completion; platform-controlled schedule | payouts, KYC, schedules, multi-currency (claim) | withdraw system: requests, auto-disbursement, thresholds, reverse withdrawal |
| Buyer–seller interaction | messages within transaction; reviews | threads | live chat, store support, Q&A, reviews |
| Payments substrate | Stripe Connect (built-in, detachable) | Mirakl Payout / PSP integrations (claim) | marketplace-capable gateway plugins |
| Extension surface | Marketplace/Integration APIs, CLI, webhooks | REST/GraphQL, webhooks, SDKs, operator+seller connectors | REST API, hooks, WP-CLI, modules |
| Venue subject | goods, services, rentals, gigs, negotiation | goods (MMP) + services (MPS) | goods (+ modules for auction/booking) |
| Deployment | SaaS | SaaS | self-hosted plugin |
| Distinctive extras | reverse/negotiation flows as first-class processes; paymentless venues | dropship dual-mode, retail media, pre-vetted seller network (claims) | staff accounts, vacation mode, driver app, single-seller mode |

## Abstraction Hierarchy

### L0 — Defining Invariant (minimal)

A Marketplace Platform is operator-side software for building and running a commerce venue in which many independent third-party sellers transact with buyers under one operator. Four jointly-held structures:

1. **The operator-run multi-seller venue as the product's purpose.** The software exists so that ONE operator can run a venue where the selling population is many independent external sellers, not the operator's own single catalog. Remove → single-merchant e-commerce platform software.
2. **Seller-side administration.** Sellers onboard into the platform and self-administer a persistent presence (shop/store/provider profile) and their own sellable catalog (listings/offers/products) inside it. Remove → operator-only catalog with staff accounts (plain e-commerce; or 1P/consignment retail).
3. **Operator governance and marketplace economics.** The operator admits and governs sellers and their catalog, and the platform carries the operator's commercial terms for sellers — commission/fee configuration with per-order/per-sale computation, plus per-seller settlement machinery (payouts/withdrawals, or per-seller split payment routing). Remove → a hosting surface or seller-management back office with no marketplace business loop.
4. **A unified buyer venue with per-seller attribution.** Buyers face one venue — one catalog/search/purchase surface spanning all sellers — while every listing and resulting order remains attributed to its seller for fulfillment and settlement. Remove → separate storefronts per merchant (multi-store builder) or anonymous aggregation.

Jointly-held checks:
- 1+2 without 3 = sellers self-publish into a venue with no operator economics/governance → an open listing board / hosting surface, not an operated marketplace.
- 1+3 without 2 = the operator holds the catalog and merely pays out third parties → 1P/consignment retail, not a marketplace.
- 2+3 without 4 = seller portals and fee machinery with no shared buyer venue → seller management software.
- 4 without 2+3 = buyers see "sellers" but nothing seller-side exists → attribution cosmetics on a 1P store.

Notes on minimality:
- "Commission" as the specific fee form is NOT invariant (seller subscription/listing-fee models exist — Dokan Subscription packs; Sharetribe documents subscription monetization via integration); the invariant is operator-configured seller economics + per-seller settlement machinery.
- "Built-in payment processing" is NOT invariant: Sharetribe supports paymentless venues and removable Stripe; Dokan realizes payments through gateway plugins. What is invariant is that the platform resolves money per seller (commission computation + payout/withdraw or split routing), however it is implemented.
- "Cart splitting across vendors" is NOT invariant: explicit in goods-oriented products (Mirakl claim, Dokan sub-orders) but absent in Sharetribe's one-provider-per-transaction model → per-seller attribution is the invariant; cart splitting is a common goods-marketplace implementation.

### L1 — Common Mature Structure (standard capabilities, cross-product B evidence unless noted)

- Operator back office: dashboards/reports (orders, sellers, earnings/commission), seller management, catalog moderation, order oversight, configuration of commissions/fees, settings, content/design.
- Seller portal: onboarding + verification, catalog/listing management, order/booking queue and fulfillment status, earnings balance and payout/withdraw views, ratings, messaging, store/profile settings.
- Buyer storefront: catalog with search/filters, seller-level pages, listing/product detail with seller attribution, cart/checkout, order tracking, reviews, buyer–seller messaging.
- Reviews/ratings between buyer and seller (A in all three sampled products).
- Notifications/emails tied to order/transaction events.
- Extension surface: APIs (REST/GraphQL), webhooks, storefront theming/templates.
- Multi-seller cart splitting with per-seller fulfillment (goods marketplaces; A for Dokan sub-orders, vendor claim for Mirakl).
- Refund/dispute handling with operator adjudication (A for Sharetribe operator refund; A for Dokan refund requests; incident management claim for Mirakl).

### L2 — Variant / Optional Structure

- Traded subject: products (Mirakl, Dokan), services/bookings/rentals/gigs (Sharetribe; Mirakl MPS variant), digital goods, auction/booking/RFQ modes (Dokan modules).
- Deployment: SaaS vs self-hosted plugin vs (reported elsewhere) self-hosted license.
- Money realization: split-at-charge via marketplace PSP rails (Sharetribe/Stripe destination charges + application fees) vs collect-then-withdraw operator cycles (Dokan withdraw system) vs dedicated payout product (Mirakl Payout claim); paymentless venues (Sharetribe messaging type); seller subscription monetization.
- Operator business model: commission per sale (dominant), customer-side fees (Sharetribe supports), seller subscription/listing packs (Dokan), retail media (Mirakl claim).
- B2C vs B2B (Mirakl B2B pricing/terms/quotes claims).
- Marketplace vs dropship dual operation per vendor (Mirakl claim).
- Buyer-facing realization: standalone venue site (Sharetribe/Dokan) vs embedded into the operator's existing e-commerce storefront via Front APIs (Mirakl).
- Geography/multi-currency/multi-language; EU compliance fields (Dokan module); geolocation (Dokan).
- Mobile apps for buyer/seller/courier (Dokan; Sharetribe custom UI).

### L3 — Vendor-specific (kept out of the final document)

- Sharetribe: transaction processes in edn/CLI, privileged transitions, Console hosted configurations, Asset Delivery API, environments Test/Dev/Live.
- Mirakl: Connect (seller-side network), pre-vetted seller network, Ads, Nexus, MMP/MDP/M1C/MPS naming, SDK languages.
- Dokan: named modules (Vacation, Follow Store, RMA, Seller Badge, wePOS), WP-CLI/MCP/n8n specifics, store listing page numbering.

## Vendor-specific Findings

(see L3; plus) Sharetribe is the only sampled product that treats a *paymentless venue* as a first-class configuration and that models the operator as an explicit transition actor inside a customizable transaction process. Dokan is the only sampled product that documents an explicit *single-seller mode* switch and *reverse withdrawal*. Mirakl is the only sampled product documented as running marketplace and dropship in one instance with per-vendor model choice.

## Rejected Findings

- "Marketplace software = goods e-commerce + vendor accounts." Rejected: Sharetribe's venues trade services, rentals, bookings, and negotiated gigs without product catalogs or stock; the goods substrate (SKU/stock/warehouse) is variant, not definitional.
- "The platform processes payments itself." Rejected: payment processing is realizable via external PSP rails or gateway plugins; the invariant is per-seller money resolution, not in-product processing.
- "Marketplace platforms always split multi-seller carts." Rejected: service/booking venues transact one provider at a time; attribution, not cart splitting, is the invariant.
- "Reviews/verification/AI catalog tools are definitional." Rejected as L1/L2-era machinery; older venues satisfied the Type without them.
- "Marketplace Platform is the same Type as Online Marketplace." Rejected: one is software for operating; the other is the operated venue (consistent with the Service Marketplace document's positioning).

## Boundary Findings

- **vs E-commerce Platform (05.01):** e-commerce platform software runs one merchant's own store. The marketplace platform runs a venue of many independent sellers with seller-side administration and per-seller economics. Sharpest proof from the sample: the same product ships a *single-seller mode* (Dokan) — flip the knob and it degrades into a plain store; remove seller administration and seller economics from any marketplace platform and what remains is e-commerce platform software.
- **vs Online Marketplace / Multi-vendor Marketplace (05.02):** those leaves name the venue (the operated market with its real participants); Marketplace Platform names the software used to build and run such a venue. The platform is to the venue what store-builder software is to a store.
- **vs Service Marketplace (05.02, documented):** the venue Type for performed services; a marketplace platform can be configured to run one (Sharetribe service/rental types; Mirakl MPS). Venue vs software again.
- **vs Marketplace Seller Management / Seller Portal / Multi-marketplace Seller Platform (05.23):** those serve a SELLER operating across multiple venues; the marketplace platform serves the OPERATOR running one venue. Same market, opposite side.
- **vs Dropshipping Platform (05.20):** in dropship the operator sells its own catalog under its own brand and vendors merely fulfill; in a marketplace sellers sell their own offers under their own names and the operator takes commission. One sampled vendor ships both modes in one instance and frames them exactly this way (vendor claim) — which confirms the boundary while showing the products can converge at implementation level.
- **vs Classifieds Platform (05.03):** no platform-mediated transaction/settlement → not a marketplace platform's defining loop (consistent with the corpus-wide leakage/settlement seam).
- **vs Auction Platform (05.18) / Payment Orchestration / OMS / PIM:** auction is a pricing mode (module in sampled platform); payment processing and order/inventory infrastructure are components the platform orchestrates or integrates.

"Remove what → becomes another Type" summary: remove seller-side administration + seller economics → E-commerce Platform; remove the software framing (keep the operated market) → the venue Types; move to the seller's side of the market → 05.23 seller tools; remove platform settlement → Classifieds; replace seller-offers with operator-owned catalog fulfilled by vendors → Dropshipping.

## Historical / Market-Sample Check

Ask: would older, regional, platform-native marketplace software still fit the L0?

- Pre-SaaS multi-vendor software (late-1990s/2000s-era shopping-mall scripts, B2B trading-exchange platforms, self-hosted auction-site scripts of the eBay-clone wave, marketplace extensions for open-source stores): all held operator venue + seller accounts with self-managed catalogs + operator fee machinery (commission/transaction/booth/listing fees) + a shared venue with per-seller attribution, without cloud delivery, no-code editors, AI catalog tools, or built-in payouts (payouts often manual/offline). All satisfy the L0; nothing modern is definitional. (Reasoned from well-known category history; these older products were not directly examined in this pass — assertion strength kept at structural level, no product-specific claims.)
- Paper-era analog (craft-market/flea-market operator): admission of vendors, vendor-brought goods, booth fees, shared venue with per-vendor attribution — the four structures exist socially, supporting the abstraction above software-era features.
- Platform-native present: a WordPress site with the sampled plugin realizes the same core inside a CMS; a headless realization (Mirakl Front APIs) realizes the buyer venue inside an existing e-commerce storefront. Both fit.
- The check also forces "commission" out of the L0 in favor of "operator-configured seller economics + per-seller settlement": booth-fee and subscription models historically preceded per-sale commissions in several venue lineages.

## Uncertainties

1. Mirakl operational detail (exact onboarding flow, commission configuration surface, payout mechanics) sits behind login/enterprise sales; claims rest on the product page and the API-portal structure. All Mirakl-specific capability statements in the final document are marked as product-page claims or kept generic.
2. The self-hosted-license pole (CS-Cart class) and API-first mid-market pole (Arcadier) could not be examined (403/transport errors); the sample's deployment spread rests on SaaS (×2) + self-hosted plugin (×1). Structure-level conclusions are unlikely to be affected (the plugin sample already realizes self-hosting), but per-product claims about those vendors were avoided.
3. Whether "operator charges sellers" is definitional in degenerate cases (a free venue): resolved by holding the *machinery* (fee configuration + settlement) as invariant and its usage as the operator's choice; a platform lacking the machinery entirely would not be recognizable as marketplace software.
4. Dokan article bodies were not individually fetched; Dokan observations rest on the documentation tree's named features and dedicated articles (titles are self-describing) — operational parameters (fee formulas, thresholds) intentionally not asserted.
5. Older marketplace software lineages (mall scripts, exchange platforms, auction clones) were reasoned about, not fetched; they are used only for the historical-structure check, never as cited evidence for specific behaviors.

## Final Synthesis

The sample confirms the working hypothesis and the corpus precedent: **Marketplace Platform = operator-side software for building and running a multi-seller commerce venue.** Its defining core is four jointly-held structures (multi-seller venue under one operator; seller-side administration of presence and catalog; operator governance + marketplace economics with per-seller settlement; unified buyer venue with per-seller attribution). Everything else — reviews, cart splitting, built-in payments, catalog QC, mobile apps, AI machinery, retail media — is standard or variant machinery around that core. The Type sits between E-commerce Platform (single-merchant substrate it is often built on) and the venue Types it brings into existence (Online/Multi-vendor/Service Marketplace), and is the operator-side counterpart of the seller-side 05.23 tools.

Taxonomy note (for STATUS.md Boundary Issues): within 05.02, "Online Marketplace" and "Multi-vendor Marketplace" appear to be near-duplicate venue leaves, while "Marketplace Platform" is the software leaf; a joint review of the 05.02 cluster is recommended.
