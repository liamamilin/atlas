# Research Notes — International Commerce Management

## Research Goal

Understand what "International Commerce Management" refers to in the real market: what a merchant-side system for managing cross-border / multi-country commerce actually consists of, what its core objects and workflows are, how its realizations differ (platform-native module vs dedicated cross-border layer vs international-first platform), and where its boundaries lie vs neighboring Types (E-commerce Platform, Global Trade Management, Order Management, Cross-border Commerce Platform sibling leaf).

## Initial Boundary

Working hypothesis at start:

- The leaf sits under §05.24 "Cross-border Commerce", sibling of "Cross-border Commerce Platform" (unprocessed) and adjacent to Global Trade Management (§10, processed 2026-09-07).
- Hypothesis: this is merchant-side management of selling into multiple countries — market segmentation, localized proposition (currency/pricing/language/catalog/payments/delivery), cross-border obligations (tax/duty/import), settlement and per-market performance — NOT the ERP/SCM-side trade-compliance discipline covered by Global Trade Management.
- Risk: the two sibling leaves (this one and Cross-border Commerce Platform) may be the same market family under two names. Market labels observed in the sample ("cross-border ecommerce platform", "global ecommerce platform", "international selling") do not cleanly separate into two categories under these two directory names. Recorded for joint review.

## Research Questions

1. What is the core object around which international commerce is managed? (Answer: the "market" — a seller-defined grouping of buyers, typically by geography.)
2. What does a market carry as configuration? (currency/pricing, language/content, catalog, payments, delivery/fulfillment, domains, taxes/duties.)
3. How do cross-border obligations (duties, import taxes, local taxes, product restrictions) enter the model?
4. Who bears the compliance/liability burden — merchant or provider (Merchant-of-Record model)? Is MoR definitional or variant?
5. How is the international operation managed centrally (one back end? portal?) and reviewed (per-market performance)?
6. What are the distinct packaging philosophies in the market?
7. Where are the boundaries vs E-commerce Platform, Global Trade Management, OMS, and the sibling leaf?

## Representative Products

Selected for market representativeness + distinct product philosophy + distinct customer tier:

1. **Global-e** — dedicated cross-border e-commerce layer ("Global E-Commerce Platform") that localizes the brand's own site and runs international operations on the brand's behalf; enterprise + emerging-brand (PRO) tiers. Philosophy: "we run your global trade for you" (Merchant of Record).
2. **ESW** — enterprise global-ecommerce platform/orchestration layer (Global Checkout, Global Returns, Global Supply Chain, Omnichannel Order Management, Growth/Customer Services); philosophy: "absorb complexity", additive control layer over existing commerce platforms; Merchant of Record.
3. **Shopify Markets / Shopify international selling** — platform-native international layer inside the dominant SMB/mid-market commerce platform; philosophy: merchant configures and maintains markets themselves; optional managed MoR service ("Shopify Managed Markets"). Provides the clearest explicit definition of the "market" object.
4. **Centra** — international-first DTC+wholesale commerce platform for fashion/lifestyle brands; philosophy: multi-market/multi-store as the native structure of the platform itself ("built for global sales, out-of-the-box"), merchant retains full commerce ownership.

Rejected/abandoned: **Zonos** (landed-cost/compliance infrastructure pole) — all three attempted hosts (zonos.com, docs.zonos.com, developer.zonos.com) timed out on 2026-09-07; abandoned per network rules. The compliance-infrastructure pole is therefore under-evidenced and is described structurally only.

## Sources

| # | Source | Tier | Result |
|---|---|---|---|
| 1 | https://www.global-e.com/ (root) | 2 | Fetched 2026-09-07 |
| 2 | https://www.global-e.com/platform/ | 2 | Fetched 2026-09-07 (rich: enablement/intelligence/demand pillars, MoR, merchant portal) |
| 3 | https://globale-b2b.zendesk.com/hc/en-us | 1 | Sign-in wall — NOT accessible (limitation recorded) |
| 4 | https://esw.com/ (root) | 2 | Fetched 2026-09-07 |
| 5 | https://esw.com/platform-overview/ | 2 | Fetched 2026-09-07 (orchestration/data layer/connectors/compliance) |
| 6 | https://esw.com/product/global-checkout/ | 2 | Fetched 2026-09-07 (localized checkout, MoR, settlement/FX) |
| 7 | https://help.shopify.com/en/manual/markets | 1 | 403 — NOT accessible (limitation recorded) |
| 8 | https://www.shopify.com/markets | 2 | Fetched 2026-09-07 (Market object definition, per-market customization) |
| 9 | https://www.shopify.com/international | 2 | Fetched 2026-09-07 (localization surfaces, Managed Markets MoR, FAQ defining market) |
| 10 | https://centra.com/ (root) | 2 | Fetched 2026-09-07 (one store all markets, 100% localized claim) |
| 11 | https://centra.com/cross-border-ecommerce | 2 | Fetched 2026-09-07 (multi-market setup, price lists, PSP routing, taxes, warehouses) |
| 12 | https://zonos.com/, https://docs.zonos.com/, https://developer.zonos.com/ | 1/2 | Timeout ×3 — abandoned |

Research date: 2026-09-07.

## Product Observations

### Global-e (dedicated cross-border layer; MoR philosophy)

Evidence: A (direct observation of official product pages), layers noted inline.

- Positions as "The Global E-Commerce Platform"; three pillars: Global Enablement (localized shopper journey on the brand's own website), Global Intelligence (benchmarks, recommendations from platform-wide data), Global Demand (multi-country B2C portal "borderfree" + marketing services). [A]
- Localised Shopper Experience surfaces listed by the vendor: messaging (location-specific notifications), price & currencies (browse/buy in local currency; pricing-strategy insights), localized checkout, shipping (variety of methods at competitive rates), tax & duty ("guaranteed final cost… prevent unexpected add-on fees upon delivery" — i.e., DDP-style presentation), payment options (local/alternative methods, wallets, BNPL), returns (pre-paid and local returns), customer support (order-tracking dashboard for international shoppers). [A]
- Streamlined Merchant Experience: Merchant of Record — "Global-e takes on the responsibilities of global online trade. We handle payment processing, tax filing and local regulations compliance in every market". [A]
- End-to-end operations: international logistics via ecosystem of global/local carriers, fulfilment services, PSPs. [A]
- Regulations & tax compliance: "manage country restrictions and import processing". [A]
- Risk management: currency-fluctuation protection, international payments fraud prevention. [A]
- Self-Management Tools: "merchant portal provides full visibility and control of global e-commerce activity… track performance and manage your proposition in over 200 markets from one place". [A — vendor-claimed count, not independently verified]
- Tiers: PRO (emerging brands, simple/fast integration) vs ENTERPRISE (high-volume, dedicated team). [A]

### ESW (enterprise orchestration layer; "absorb complexity" philosophy)

- Root: "ESW manages the complexity behind global commerce across payments, compliance, shipping and returns. We localize each market, absorb the risk and stay accountable". Products: Global Checkout, Global Returns, Omnichannel Order Management, Global Supply Chain, Growth Services, Customer Services (+ Agentic Commerce). [A]
- Platform overview: "control layer that orchestrates global commerce operations"; orchestration (payments/compliance/logistics/service coordinate centrally), data layer (one consistent view across checkout/payments/fulfillment/delivery/service), security, compliance ("financial, regulatory and operational compliance controls built into how the platform operates"), commerce-platform connectors & APIs ("global capability without replacing what you already operate"; "additive, not replacement architecture"; "not a domestic platform extended for cross-border"). [A]
- Workflows coordinated: "checkout, payments, fulfillment, delivery, returns and settlement… from payment processing and fraud evaluation at checkout through to carrier selection, customs execution and post-purchase service". [A]
- Global Checkout page: per-market localized branded UX (local currencies, languages, payment methods, pricing); international payments (vendor-claimed 35+ local/alternative methods, smart routing, local acquiring); ML fraud detection; Merchant of record — "ESW collects your revenue and pays customs authorities directly, with tax, duties, foreign exchange and regulatory responsibility transferred to us"; global financial settlement and FX ("settlement, reporting and reconciliation centralize across your international markets"). Deployment: hosted, embedded or composable; compatible with major commerce platforms and custom environments. [A — vendor-claimed counts unverified]
- Solutions menu confirms the buyer jobs: launch & scale new markets, mitigate tariff and import duty exposure, reduce cross-border compliance risk, improve international margins, consolidate fragmented commerce infrastructure. [A]

### Shopify Markets (platform-native module; self-managed philosophy)

- Explicit definition of the core object (FAQ): "A market is a group of customers you define—often by country, region, or customer type. With Shopify Markets, you can create markets for both retail and B2B buyers, set local currencies and pricing, choose which products are available, and adapt your storefront experience for each market. All of these settings are configured and maintained by you." [A]
- Markets page: "Sell to multiple markets, all from a single store"; holistic overview of all markets, zoom in, make updates in one place; create markets in minutes; markets can "inherit" settings from similar markets; per-market local languages and currencies (payments so people pay in own currency), optimized fulfillment (ship from closest fulfillment center), unique domains/subfolders per market, per-market theme/look, per-market catalog & pricing ("curate your catalog… keeping your different taxes straight"). [A]
- International page: localization surfaces — translations & SEO (Translate & Adapt), international themes, unique URLs (.ca/.eu), secure local checkout (vendor-claimed 130+ currencies; "sell in local currency and get paid in yours"), regional address forms, market-specific products ("avoid product and shipping restrictions with unique product catalogues"); "Currency conversion, duties, and import taxes don't have to come out of your payout". [A]
- Shopify Managed Markets (optional MoR service): "automates much of the work and risk of cross-border selling with a merchant-of-record service (which handles foreign taxes and import fees), provides protection on eligible chargebacks, and offers automatic price adjustments"; "hand off the taxes, duties, and import fees". Without it, merchants configure currencies, pricing, translations, duties and import taxes themselves. [A]
- Market definition axis extends beyond geography: retail customers, B2B wholesale buyers, in-person retail locations (POS). [A]

### Centra (international-first commerce platform)

- Root: "The fashion brand commerce platform… serve all markets with the right products, prices, and campaigns"; "One online store, all markets — Win new markets easily with a single store localized to every country, language, currency and more"; "100% localized: One global site localized with local payments, deliveries, local warehouses, languages, prices, taxes and more"; vendor-claimed 120+ countries supported; "the only commerce platform that was built for global sales, out-of-the-box". [A — counts unverified]
- Cross-border page: multi-market setup — "manage multiple storefronts from one back end"; tailor storefronts with "local pricing, languages, content, currencies and size charts, based on consumers' location"; "Sell in 100+ local currencies"; "Use local PSP agreements for the best auth rates and lowest costs"; "Build a checkout with local payment methods, delivery options and price lists based on the customer's location. Create separate price lists per territory or currency. Route to the best PSP depending on location"; "Handle international taxes: Manage taxes natively… Validate and calculate EU VAT and US Sales tax"; "Add any number of warehouses, globally"; ship-from-store support with uncertain inventory and dual reservation; one back end for all countries ("Filter data by country or market and export it to your favorite BI tool"); per-country discounts; localized domains; GeoIP-based dynamic adaptation; checkout PSP fallbacks; per-market analytics. [A]
- Notably ABSENT at this pole: no Merchant-of-Record claim, no duty/landed-cost presentation claim (taxes = VAT/sales tax natively). Confirms MoR and duty/DDP handling are common-but-not-universal. [A]

## Cross-product Comparison

| Dimension | Global-e | ESW | Shopify Markets | Centra |
|---|---|---|---|---|
| Packaging | dedicated cross-border layer on brand's own site | dedicated orchestration layer + services via connectors | module inside the commerce platform | international-first commerce platform |
| Core unit managed | market/proposition, brand-wide | market/transaction workflow | "market" object in store admin | market/storefront from one back end |
| Market carries | currency/pricing, language, checkout, payments, shipping, tax&duty, returns, messaging | currency/language/payment/pricing per market | currency/pricing, language, catalog, payments, fulfillment, domains, theme, taxes | currency/pricing (price lists per territory), language, payments (PSP routing), delivery, warehouses, taxes, discounts |
| Buyer-location based adaptation | yes | yes | yes | yes (GeoIP + location-based checkout) |
| Duty/import fees at checkout | yes (guaranteed final cost) | yes (MoR pays customs authorities) | yes (merchant-configured or Managed Markets) | not evidenced (taxes only) |
| Tax handling per market | MoR files taxes | MoR transfers responsibility | merchant-configured or MoR | native VAT/US sales tax calculation |
| MoR model | yes (core posture) | yes (core posture) | optional ("Managed Markets") | no (not evidenced) |
| Central management surface | merchant portal (200+ markets claim) | platform data layer/orchestration | markets overview in admin | one back end, filter by market |
| Per-market performance review | benchmarks + insights | consolidated settlement/reporting | overview + zoom-in + updates | per-market reports/BI export |
| International returns | pre-paid/local returns | Global Returns product | (not detailed on fetched pages) | (case-study level evidence) |
| Catalog scoping per market | (implied via proposition) | (not detailed) | market-specific catalogs | product allocation to markets |
| Demand generation | Global Demand pillar (portal + marketing) | Growth Services | sales channels | (out of scope for product) |
| Customer tier | enterprise + emerging brands | enterprise brands | SMB→enterprise | mid-market/enterprise fashion brands |

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

The smallest structure without which the Type stops being recognizable:

1. **Buyer-jurisdiction segmentation** — the system distinguishes buyers by seller-defined markets (groupings typically by country/region, extendable to customer type or channel).
2. **Market-scoped proposition configuration** — per-market settings (at minimum pricing/currency, language/content, catalog availability, payment and delivery options) are centrally defined and automatically applied according to the buyer's market.
3. **Per-market commerce obligations** — the tax (and, where goods physically cross borders, duty/import-fee) treatment of a sale is carried as explicit per-market rules or handoff, honored at checkout.
4. **Central management with per-market oversight** — one system surface through which all markets are managed and per-market performance is observed.

Remove #1 → single-jurisdiction commerce. Remove #2 → disconnected per-country sites. Remove #3 → localized but compliance-blind store. Remove #4 → international selling without "management" (the leaf's own discriminator).

### L1 — Common Mature Structure

Very common in mature products, not definitional:

- currency conversion + per-market price lists / pricing rules (incl. automatic price adjustment)
- language/content localization, localized domains/subfolders, per-market SEO
- local payment methods, PSP routing / local acquiring, PSP fallback
- localized checkout flows and regional address forms
- duty & import-fee handling presented at checkout (landed-cost / DDP presentation)
- international shipping methods; multi-warehouse / closest-fulfillment routing; market-specific catalogs honoring product restrictions
- international returns (prepaid / local returns)
- market inheritance / duplication / templating of settings
- consolidated settlement, FX handling, per-market reporting/analytics
- international shopper order-tracking / support surfaces

### L2 — Variant / Optional Structure

- Responsibility model: Merchant-of-Record handoff (liability + filing transferred) vs merchant-retained obligations (self-configured) — both fully valid realizations; MoR is a packaging/posture, not the definition.
- Packaging: platform-native module / dedicated cross-border layer in front of the domestic platform / international-first platform / (adjacent pole) compliance & landed-cost infrastructure APIs — the last pole under-evidenced in this pass (source unreachable).
- Market definition axis: geography-dominant; customer-type (B2B vs retail) and channel (in-person locations) extensions.
- Segment emphasis: DTC fashion/lifestyle heartland (Centra, and largely Global-e/ESW brand lists) vs general merchandise.
- Scale/coverage claims (markets supported, currencies, payment methods) — vendor marketing figures, vary and are not independently verified.
- Demand-generation add-ons (multi-country B2C portals, marketing services) — present at the dedicated-layer pole, absent at the platform-native pole.
- Agentic/AI commerce surfaces (one vendor) — frontier, single-product.

### L3 — Vendor-specific (research notes only)

- Global-e: borderfree.com multi-country B2C portal; PRO/ENTERPRISE tier names; merchant support via zendesk (sign-in gated); "billions of interactions / 51123123 transactions" style dashboard claims; 200+ markets claim.
- ESW: Client Hub (esp.eshopworld.com); product names Global Checkout / Global Returns / Global Supply Chain / Omnichannel Order Management / Agentic Commerce; MACH certification; 35+ payment methods, 8M+ orders, 200+ markets, 241,559.42 DSA monthly-recipients figure; Microsoft Copilot agentic-commerce launch.
- Shopify: "Shopify Managed Markets" service name; Translate & Adapt app; 130+ currencies claim; markets-for-POS-locations capability; help-center 403.
- Centra: GraphQL API / headless posture; dual reservation & uncertain inventory concepts; PIM out-of-the-box; 120+ countries / 100+ currencies claims; support.centra.com (not fetched).

## Vendor-specific Findings

Summarized above under L3. None promoted to the final document beyond neutral capability descriptions.

## Boundary Findings

1. **vs Cross-border Commerce Platform (§05.24 sibling, unprocessed)** — the sampled market does not maintain two distinct product categories matching the two leaf names; products self-label variously ("cross-border ecommerce platform", "global ecommerce platform", "international selling"). The management discipline documented here (market as managed unit) appears across all packaging poles, including inside general commerce platforms. Likely outcome: same market family; the two leaves are either aliases or a packaging-angle split (enabling-infrastructure/MoR layer vs management discipline). Escalated for joint review; not unilaterally merged.
2. **vs E-commerce Platform (§05.01)** — the e-commerce platform's center is store/product/order machinery regardless of geography; this Type's center is the market as the managed unit with per-market proposition and obligations. Remove market scoping and obligations → an e-commerce platform (Shopify Markets is exactly such a layer; Centra is an e-commerce platform whose distinguishing claim is the multi-market structure).
3. **vs Global Trade Management (§10, processed)** — GTM is the importer/exporter-side compliance-and-fiscal system of record for goods trade (classification, screening, licensing, customs declarations, trade programs), fed by ERP/order/TMS streams. This Type is consumer-commerce-side: localized selling experience + checkout-time obligation handling + per-market management. Complementary rather than overlapping; a merchant running international DTC may use both, with different operators and objects. Consistent with the GTM pass's own boundary notes.
4. **vs Order Management System (§05.07)** — OMS is order-centric (orchestration across inventory/channels); this Type is market-centric (proposition + obligations per market). International order/returns oversight appears here as per-market visibility, not as order orchestration. (ESW sells an OMS as a sibling product — the market itself separates the two.)
5. **vs Tax/duty compliance platforms (§08/§10)** — obligation determination as a standalone discipline vs embedded per-market selling rules here. Duty/landed-cost infrastructure products (pole not directly evidenced this pass) would sit adjacent, supplying the landed-cost capability into checkout.
6. **vs Marketplace seller / multi-marketplace platforms (§05.23)** — channel axis (many marketplaces) vs geography axis (many countries) — different managed unit.
7. **vs Localization/translation tooling** — language is one localized dimension among many; the Type spans pricing, catalog, payments, delivery, and obligations.

## Uncertainties

1. The compliance/landed-cost infrastructure pole (Zonos-class) could not be examined (all hosts timed out). The final document therefore describes that pole only structurally, with no product claims.
2. Tier-1 operational docs largely unreachable (Global-e merchant help sign-in gated; Shopify help 403; Centra support center not fetched). All evidence is product-page tier. No precise operational facts (numeric limits, fees, windows, default settings) are asserted in the final document; all numeric counts quoted above are vendor claims kept in these notes.
3. Whether the directory intends this leaf and Cross-border Commerce Platform as alias or split — requires joint review (recorded in STATUS Boundary Issues).
4. Per-market catalog/product-restriction handling was evidenced directly only at the platform-native pole (Shopify) and partially at Centra (allocation); its universality is assumed moderate, not proven.

## Historical / Market-Sample Check

Question: would older, regional, or differently-positioned products still fit the L0?

- Pre-SaaS and suite-era international selling was commonly realized as per-locale/per-country store scopes (website → store → view scoping carrying currency, language, tax class and payment config) inside self-hosted commerce suites. These satisfy all four L0 structures: seller-defined market scopes, per-scope proposition, per-scope tax rules, central admin with per-scope results. They lack MoR, demand portals and dedicated-layer packaging — confirming those are variants, not invariants.
- Regional/older practice: a domestic shop that merely ships internationally with manual export paperwork (no market-scoped configuration, obligations handled per-shipment by hand) fails the L0 — correctly excluded as plain cross-border shipping, not management of international commerce.
- The definition therefore survives the historical check: no dependency on the modern MoR posture, on dedicated-layer packaging, on checkout-side landed-cost presentation, or on any vendor's market-count scale.

## Final Synthesis

International Commerce Management is the merchant-side management layer for selling across borders: the seller defines markets (groupings of buyers, typically geographic), configures each market's proposition (pricing/currency, language, catalog, payments, delivery), carries each market's commerce obligations (taxes; duties/import fees where goods cross borders) explicitly, manages all markets from one system surface, and reviews performance per market to drive pricing, catalog, and expansion decisions.

The Type's realization poles: (a) platform-native module inside a commerce platform (self-managed; optional MoR handoff), (b) dedicated cross-border layer / orchestration platform that localizes the brand's own storefront and can absorb the whole operating burden (MoR posture), (c) international-first commerce platform where multi-market structure is native. The defining core is shared across all poles; MoR, demand generation, agentic surfaces, and specific counts are variants or vendor specifics.
