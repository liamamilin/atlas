# Research Notes — Digital Download Commerce Platform

Research date: **2026-09-08**

Directory location: §05.22 Digital Goods (siblings: Digital Goods Store [unprocessed]; the §27 leaf Digital Product Commerce Platform [processed 2026-09-07] is the counterparty for this pass's central taxonomy question; other nearby: E-commerce Platform / Online Store Builder / Headless Commerce Platform §05.01, Checkout Platform §05.06, Online Marketplace §05.02, Payment Gateway / Payment Processing §08)

---

## Research Goal

Understand what a Digital Download Commerce Platform is as an Application Type — and resolve the taxonomy question the §27 pass pre-hung: the directory carries both this §05.22 leaf and the §27 leaf "Digital Product Commerce Platform", whose names appear to cover the same activity. This pass samples products that brand themselves around the "digital download" vernacular and tests whether their structure differs from the already-documented Type, or whether the two leaves are name variants of one Type.

## Initial Boundary

Hypothesis before research:

1. Core use: a seller sells digital downloads — files (ebooks, PDFs, music, video, templates, software) and/or codes/license keys — with the platform automating purchase and delivery.
2. Primary users: the seller (management side) and the buyer (product page / checkout / download side).
3. Nearest neighbors: Digital Product Commerce Platform §27 (name overlap — the flagged question), Digital Goods Store §05.22 (sibling leaf, unprocessed), Online Store Builder / E-commerce Platform (generic machinery), Checkout Platform (payment machinery only), Online Marketplace (venue vs seller tooling).
4. Probable boundary test (inherited from the processed cluster): **what the purchase converts into** — a delivered file/key here, vs goods shipment, standing curriculum access, or cycle-maintained entitlement elsewhere.
5. Unknowns: does the "digital download" naming denote a structurally distinct category (e.g., delivery-only infrastructure, or a buyer-side download store), or is it the vernacular for the same seller-side category the §27 pass documented? Does a WordPress-plugin deployment posture (platform inside the seller's own CMS) constitute a new sales-surface variant? How deep does license-key machinery go in download-branded products?

## Research Questions

- What is a "download" as an object in these systems — and do the products themselves distinguish "download" from "product"?
- What are the seller's setup steps from account to first sale?
- What exactly happens after payment — through which channels does the buyer receive the content, and with what durability?
- How do the delivery-security mechanics work (download limits, stamping, expiring links, license keys, activation control)?
- How do sellers get paid — merchant-of-record vs seller-connected postures?
- Which selling machinery is common (discounts, bundles, upsells, affiliates, product updates)?
- What sales-surface postures exist (hosted storefront, embed-anywhere, plugin-inside-own-CMS)?
- Do the "digital download"-branded products form the same population as the "digital product"-branded products sampled by the §27 pass?

## Representative Products

Selection logic: products that brand themselves in the "digital download" register (the leaf's own vocabulary), spanning deployment postures and customer tiers; plus the §27 pass's fetched products as documented cross-pass evidence.

| Product | Philosophy / posture | Customer tier | Evidence this pass |
|---|---|---|---|
| **Easy Digital Downloads (EDD)** | WordPress plugin: the store runs inside the seller's own site; digital-only by design; software-licensing emphasis; no platform fees | solo creators → plugin/theme/software vendors → stores at six-seven figures | Tier 1 deep (homepage, Introduction doc, Getting Started doc, Software Licensing feature page) |
| **DPD (Digital Product Delivery)** | hosted delivery-first service: upload files, copy-paste buttons anywhere, money straight to the vendor's merchant account; flat monthly, no per-sale fees | indie authors/artists/teachers → small stores | Tier 2 (homepage, features page, checkout-domain page) |
| **Payhip** | hosted indie storefront, seller-connected PayPal/Stripe | individual creators | Layer A, prior pass 2026-09-07 (help center articles) |
| **SendOwl** | embed-anywhere delivery engine, seller-owned rails, security machinery emphasis | solopreneurs → teams | Layer A, prior pass 2026-09-07 (homepage, platform page) |
| **E-junkie** | legacy button-code digital-goods cart (historical pole) | long-tail sellers | Layer A, prior pass 2026-09-07 (homepage) |
| **Lemon Squeezy** | digital-only merchant-of-record, software/SaaS-leaning | indie software vendors, SaaS | Layer A, prior pass 2026-09-07 (homepage, docs root) |
| **Gumroad** | market archetype for creator digital-product sales | creators | **not fetched** — gumroad.com timed out again this pass (2nd failure across passes); named anchor only |

## Sources

Fetched 2026-09-08 (Layer A unless noted):

- Easy Digital Downloads — https://easydigitaldownloads.com/ ; https://easydigitaldownloads.com/docs/easy-digital-downloads-introduction/ ; https://easydigitaldownloads.com/docs/getting-started/ ; https://easydigitaldownloads.com/features/software-licensing/
- DPD — https://getdpd.com/ ; https://getdpd.com/features ; https://dpdcart.com/ (checkout-domain notice page)
- Prior pass 2026-09-07 (Layer A, documented in research/digital-product-commerce-platform.md): Lemon Squeezy (homepage, digital-products page, docs root), SendOwl (homepage, platform page), Payhip (help center: How Payhip Works, Add Digital Products, Protect Your Products, Products category), E-junkie (homepage)
- Sibling research (context, Layer B for cluster seams): research/digital-product-commerce-platform.md and its published application document

**Source-access limitations:**

- Gumroad: fetch timed out again this pass (second consecutive failure across passes). No operational claims about Gumroad are made; it appears only as a market-representative name and as a comparison target named in EDD's own materials.
- Sellfy: 403 in the prior pass; not retried.
- No independent third-party sources were needed; official documentation was sufficient.

---

## Product Observations

### Easy Digital Downloads (WordPress-plugin posture — Tier 1, deep)

**Positioning:** "#1 Digital Ecommerce Plugin for WordPress… Easy Digital Downloads helps creators sell digital products securely with automated delivery, subscriptions, and licensing." "Built from the ground up to sell digital products: software, ebooks, music, courses, templates, and any other downloadable file." FAQ: "If it can be delivered as a file or a license key, you can sell it with Easy Digital Downloads."

**Terminology (the Introduction doc — decisive for the taxonomy question):**

- "**Download (or Product)**: these terms are used interchangeably. A download is a product. It's the 'thing' available for sale."
- **Order**: a record of a purchase; every purchase creates an order, even failed or incomplete ones; one order can contain multiple downloads. (Older docs called these "payments.")
- **Sale**: recorded per product whenever an order contains that product.
- **Customer**: a profile created when an order completes; collects all of one person's orders, email addresses, name, notes.
- **User**: a WordPress account attached to a customer — what lets them log in to view their account. "Users have a username and password; customers do not."
- **File Download**: logged each time a customer downloads a file (reportable).
- **Gateway**: the payment service processing transactions (Stripe default, PayPal, Square; Authorize.net and Braintree available).
- **Test Mode**: simulate orders without moving real money.

**Product options:** title, description, featured image; single or variable pricing; file uploads in the Download Details metabox; custom receipt notes; single or bundled products; categories and tags; **download limits** (how many times a buyer may download); per-product sales and earnings data.

**Delivery (Introduction doc):** on purchase completion the customer lands on a **purchase confirmation page** showing order details and download links for immediate download; two emails are sent automatically — the **customer receipt** (financial details + download links) and the **seller sale notification**; both customizable. FAQ adds: the receipt email carries a "secure, time-limited download link," and "customers can also access their purchases any time through their account page."

**Store surfaces (Blocks doc summary):** EDD ships WordPress blocks — Products (list/grid), Buy Button, Cart, Checkout, Order History, User Downloads (logged-in customers see orders and download files), Receipt, Login/Registration/Profile Editor. Shortcodes supported. The storefront is composed inside the seller's own WordPress site.

**Setup loop (Getting Started doc, 6 steps):** install/activate plugin → Setup Wizard (business info & currency, payment methods, receipt email, recommended tools, first product) → create first product (Downloads » Add Download: name, description, image, product type, price, files) → connect payments → configure store emails → test mode purchase, verify checkout/receipt/download, go live. "Most stores can be up and selling the same day."

**Discounts:** percentage or flat; product-requirement conditions; expiration dates; total-use limits; one use per customer.

**Reports:** earnings overview, top-selling products, refunds, gateway usage, taxes, file downloads, discount usage, customer metrics; CSV export of reports and logs (earnings, orders, customers, products, API request logs, file download logs). Import/export tools move orders, products, settings between sites.

**Software Licensing (Pro feature page — the deep form of license machinery):**

- unique license keys generated per purchase, delivered immediately
- **activation limits per license tier** (e.g., one site basic, five or unlimited agency) with real-time validation when the customer enters the key; at-limit customers see an upgrade message; a site can be deactivated to free a slot — self-service, no support ticket
- **activation logs**: dates, registered URLs, IP addresses per key
- **JSON licensing API** for any software type (desktop, SaaS, mobile), enforcing activation limits and validating requests
- **1-click updates** delivered through the WordPress update mechanism to licensed customers; **staged rollouts** to a portion of the user base
- **renewal automation**: reminder emails, targeted renewal discounts, one-click renewal links; with Recurring Payments, fully automatic subscription renewals
- **prorated upgrade paths** between product tiers, price calculated automatically
- **beta releases** to opted-in customers before full rollout
- license management dashboard: statuses, bulk activations, customer access control

**Money posture:** no platform fees — "you only pay the standard payment processing rates charged by your chosen payment provider"; deposits go to the seller's own Stripe/PayPal/Square account (seller-connected posture).

**Physical goods:** only via the Simple Shipping add-on; the docs explicitly warn: "If physical products with complex shipping needs are your main business, a general ecommerce solution may be a better fit."

**Market framing:** compares itself against WooCommerce, Shopify, BigCommerce, Etsy, Envato, Gumroad, SureCart, FluentCart; blog resources include "What Are Digital Downloads? A Beginner's Guide to Selling Online" and marketplace-vs-own-store guidance. Claims 50,000+ businesses, 187 countries, 30M+ processed orders, 13+ years.

### DPD — Digital Product Delivery (hosted delivery-first posture)

**Positioning:** "Digital Publishing for E-books and Digital Downloads… self-publish your e-books and sell digital downloadable products quickly and conveniently." Footer self-description: "an all-in-one shopping cart and digital fulfillment service to sell downloads, keycodes, and tangible goods."

**Setup loop (homepage):** 1) create products and store files on DPD's cloud servers; 2) copy-paste DPD's add-to-cart buttons or links onto your website, blog, social media — anywhere; 3) when customers buy, "the money goes straight to you and DPD delivers your products."

**Money posture:** 100% of the sale goes directly to the vendor's merchant account or payment provider (PayPal, Stripe, Authorize.net); no per-sale fees, bandwidth fees, or commissions — flat monthly pricing. The checkout-domain notice page states the platform's role explicitly: "DPD is not the vendor of your product and we can not provide product support" — the platform operates checkout infrastructure (each store gets a PCI-compliant SSL subdomain at dpdcart.com), it is not the seller of record.

**Delivery and security machinery (features page):**

- product hosting and delivery: any size, any type, no bandwidth charges
- **PDF stamping and encryption**: stamp buyer info onto PDF ebooks and encrypt to prevent copying/printing
- **advanced download controls**: "limit download sessions to prevent sharing"
- **automatic product updates**: new version → updated files sent to a subset or all previous buyers via download link
- key codes, services, and tangible goods supported beside downloads

**Selling machinery:** coupons/discount codes (fixed or percentage, cart conditions); upsells and cross-sells during checkout; multiple price points (special prices for a group/list vs public price); bundles — music-specific form: MP3 snippet creation, preview player embedded on the seller's site, per-track products, albums as bundles with their own price; built-in shipping and tax calculation (table rate and imported shipping; VAT/GST and sales tax); multi-language checkout (25+ languages); custom checkout domain on qualifying plans.

**Operations:** multiple stores under one account; sub-user/staff accounts with limited access; Google Analytics support; 500+ integrations via Zapier plus automatic payment notifications for custom integrations; knowledgebase and learning portal.

### Cross-pass evidence (Layer A, 2026-09-07 — summarized from the documented prior research)

- **Payhip**: hosted storefront; digital product = uploaded files + title/price/cover; buyer redirected to a download page, receipt email carries the download link for future access; deposits to seller's PayPal/Stripe; download limits and PDF stamping documented; license keys per sale for software; ebook VAT flag; variants, bundles, PWYW, free products.
- **SendOwl**: embed checkout anywhere (website, Shopify, WordPress, Notion, Linktree); connect own gateway (Stripe/PayPal/Square); automatic delivery incl. streaming and drip files; license keys; PDF stamping, download limits, expiring links, document locking, IP/email blocking; refund auto-revokes access; minimal storefront (about ten showcased products).
- **E-junkie**: copy-paste button codes/links on any site; connect any processor (incl. regional Indian processors); file downloads, codes, tickets, tangible items; instant download after successful payment; PDF stamping; the minimal historical form — no storefront, no MoR, no buyer accounts required.
- **Lemon Squeezy**: digital-only merchant of record; unlimited files per product; signed/throttled download links; license keys incl. subscription-tied; variants as file+price bundles; file versioning; hosted store + checkout overlays/links; subscriptions, PWYW, lead magnets; affiliates, email marketing; customer portal; test mode; teams; API/webhooks; marketplace layer.

---

## Cross-product Comparison

| Structure | EDD | DPD | Payhip | SendOwl | E-junkie | Lemon Squeezy | Strength |
|---|---|---|---|---|---|---|---|
| Seller-defined product catalog anchored to files/codes | ✓ (Download = Product; files in product metabox) | ✓ (files on DPD cloud) | ✓ | ✓ | ✓ | ✓ | **Core, 6/6** |
| Platform-operated purchase surface | ✓ (blocks/checkout inside seller's WP site) | ✓ (copy-paste buttons; hosted PCI checkout) | ✓ (storefront + product pages) | ✓ (embed anywhere) | ✓ (buttons/links/cart) | ✓ (store + overlays + links) | **Core, 6/6** |
| Automated delivery on payment (instant page/link + emailed durable link) | ✓ (confirmation page + receipt email w/ links) | ✓ ("DPD delivers your products") | ✓ (download page + emailed link) | ✓ (automatic delivery) | ✓ ("instant download after successful payment") | ✓ (signed links) | **Core, 6/6** |
| Seller earnings path | ✓ (deposit to seller's gateway; no platform fees) | ✓ (straight to merchant account) | ✓ (PayPal/Stripe deposit) | ✓ (own gateway) | ✓ (own processor) | MoR payout | **Core, 6/6 (both postures)** |
| Download limits / session controls | ✓ | ✓ | ✓ | ✓ | — | (signed/throttled) | Common |
| PDF stamping / buyer-marked files | — | ✓ (+ encryption) | ✓ | ✓ | ✓ | — | Common (4/6; mechanism varies elsewhere) |
| License keys | ✓ (deep: activation limits, logs, JSON API, updates, renewals) | ✓ (keycodes) | ✓ (per-sale keys) | ✓ | ✓ (codes, gift cards) | ✓ (+ subscription-tied) | Common (6/6 present; deep form software-weighted) |
| Product updates to past buyers | (via licensing updates; version delivery) | ✓ (subset or all previous buyers) | ✓ (article) | ✓ (+ buyer update emails) | — | ✓ (file versioning doc) | Common |
| Bundles | ✓ | ✓ (incl. album bundles) | ✓ | ✓ | ✓ | ✓ | Common (6/6) |
| Discount codes | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Common (6/6) |
| PWYW | ✓ (feature listed) | — | ✓ | ✓ | ✓ | ✓ | Common (5/6) |
| Buyer accounts / durable re-access | ✓ (WP user account; Order History/User Downloads blocks) | (delivery-link based) | ✓ (Buyers) | (delivery-link based) | — | ✓ (Customer Portal) | Common (form varies: account vs emailed link) |
| Test purchase mode | ✓ (Test Mode) | — | ✓ (100% coupon) | — | — | ✓ (test mode) | Common (form varies) |
| Order records incl. failed/incomplete | ✓ (explicit) | — | — | — | — | — | Product-specific detail (EDD) |
| File-download logging | ✓ (File Download records + report) | — | — | — | — | — | Product-specific detail (EDD) |
| Refund → access revocation | (refund reports; policy docs) | — | ✓ | ✓ (automatic) | — | ✓ | Common (3/6 direct) |
| Physical goods | ✓ (Simple Shipping add-on; explicitly de-emphasized) | ✓ (tangible goods) | ✓ | ✓ (secondary) | ✓ (+shipping calc) | ✗ (digital-only) | Optional; center-shift marker |
| Subscriptions | ✓ (Pro: Recurring Payments) | ✓ | ✓ (+memberships) | ✓ | — | ✓ (+dunning) | Common attached mode |
| Affiliates | ✓ (feature listed) | (via Zapier/integrations) | ✓ | ✓ | ✓ | ✓ | Common |
| Upsells / abandonment | ✓ (cart recommendations; abandoned cart recovery doc) | ✓ | (marketing category) | ✓ | — | ✓ | Common |
| Multi-store / multi-user | (WP multisite ecosystem) | ✓ (multiple stores; sub-users) | (account settings) | ✓ (teams, permissions) | — | ✓ (multiple stores; teams) | Common at scale |
| Marketplace/discovery layer | ✗ (anti-marketplace positioning) | ✗ | ✗ | ✗ ("no marketplace") | ✓ | ✓ | Optional, polarizing |
| API / webhooks / integrations | ✓ (REST API, hooks; 100+ integrations) | ✓ (Zapier, payment notifications) | ✓ | ✓ | ✓ (integration ecosystem) | ✓ (full REST) | Common |

### Evidence-layer summary

- **Layer A (directly observed)**: every cell for EDD and DPD this pass; the prior-pass cells as documented 2026-09-07.
- **Layer B (cross-product)**: catalog + purchase surface + automated delivery + earnings path as the shared spine (6/6 across both passes); delivery-security machinery, bundles/discounts, license keys, product updates, marketing machinery as standard hygiene.
- **Layer C (canonical inference)**: identical to the §27 pass's conclusion — the Type is "the purchase converts into automated delivery of the product's own digital content"; the download-branded sample and the product-branded sample are one population.

---

## Abstraction Levels

### L0 — Defining Invariant (minimal)

```text
Seller-defined catalog of digital products
└── each product anchored to its own deliverable digital content
    (uploaded files and/or codes/license keys)
└── platform-operated purchase machinery
    (product page, storefront, buy button/link/embed, or store blocks
     inside the seller's own CMS — any surface)
    resolving a payment transaction
└── automated digital fulfillment
    (the platform itself delivers the deliverable — download, key, stream —
     with no per-order seller labor)
└── seller earnings path
    (deposit to seller-connected payment account, or platform-collected payout)
```

Remove the deliverable-anchored catalog → generic store builder. Remove purchase machinery → file hosting. Remove automated delivery → generic e-commerce. Remove earnings path → not commerce. Storefront, MoR, buyer accounts, subscriptions, marketing machinery, physical goods — all removable while the Type remains recognizable (E-junkie and DPD's button-only posture prove it).

### L1 — Common Mature Structure

- Product page / hosted store; or store blocks/buttons composed into the seller's own site
- Variants (file+price), bundles, discount codes, PWYW, free lead-magnet products
- Delivery security: download limits/session controls, buyer-stamped or encrypted files, signed/expiring links, license keys, refund-triggered revocation
- Durable buyer access: emailed receipt link (universal baseline); buyer accounts/portals common
- File updates with past-buyer notification
- Order operations (refund, resend receipt, invoices, export), test-purchase mode, analytics/reports
- Marketing machinery: affiliates, upsells/cross-sells, cart abandonment, mailing-list/email integration
- API/webhooks; multi-store and staff accounts at scale

### L2 — Variant / Optional

- **Deployment posture**: hosted service ↔ plugin inside the seller's own CMS/site ↔ embed-anywhere buttons
- **Money posture**: merchant-of-record ↔ seller-connected gateway (both mature; DPD states the non-MoR role explicitly)
- **Seller segment**: authors/teachers/artists ↔ software vendors (licensing depth) ↔ educators
- **Attached commerce modes**: subscriptions, memberships, structured courses, coaching, physical goods, tickets
- **Delivery form**: files ↔ streaming (hosted or external embeds) ↔ drip-released files
- **Discovery layer**: marketplace ↔ strictly direct
- **Product-type breadth**: pure files ↔ files + keycodes + tickets + tangible goods

### L3 — Vendor-specific (research notes only)

- EDD: Download/Product terminology equivalence (used here as taxonomy evidence); Order records created even for failed/incomplete purchases; Customer-vs-User separation (customer profile has no credentials; WordPress user attached for login); File Download logging/report; Pass pricing tiers; Simple Shipping add-on with the "general ecommerce may be a better fit" warning; blocks/shortcodes duality; setup wizard steps; staging-site update advice; claims (50k businesses, 187 countries, 30M orders, 13 years); Sandhills Development / Awesome Motive ownership; comparison set (WooCommerce, Shopify, BigCommerce, Etsy, Envato, Gumroad, SureCart, FluentCart)
- DPD: dpdcart.com PCI checkout subdomain per store; "DPD is not the vendor of your product" support notice; Portal Labs ownership; MP3 snippet/preview-player music machinery; 25+ checkout languages; table-rate/imported shipping; VAT/GST + sales tax; 500+ Zapier integrations framing; 40,000 vendors / $150M sales claims
- Prior-pass vendor specifics (Payhip PWYW syntax, file caps, visibility states; Lemon Squeezy Lemon.js, marketplace guidelines, W-8/W-9; SendOwl 10-item storefront cap, membership-plugin integrations; E-junkie eBay/Patreon delivery, self-hosted shop) — recorded in research/digital-product-commerce-platform.md

---

## Vendor-specific vs Rejected Findings

- **Rejected: "digital download" denotes a structurally distinct category.** The download-branded sample (EDD, DPD) has the same four-part spine, the same standard capabilities, and the same variant axes as the product-branded sample (Payhip, SendOwl, E-junkie, Lemon Squeezy). EDD's own documentation states the equivalence verbatim ("Download (or Product): these terms are used interchangeably"). DPD's brand expansion is literally "Digital Product Delivery" while its homepage sells "digital downloads." The two leaf names are register variants of one Type.
- **Rejected: buyer-side download store reading.** Every "digital download"-branded product sampled is seller-side selling infrastructure. A consumer-facing store for digital goods is a different structure (venue vs seller tooling) — that reading belongs to the sibling Digital Goods Store leaf, to be tested in its own pass.
- **Rejected as definitional: storefront.** DPD's canonical surface is a copy-paste button; EDD's store is composed from blocks inside the seller's own site; SendOwl is embed-first. Storefront is a common realization, not the Type.
- **Rejected as definitional: merchant-of-record.** EDD and DPD both route money straight to the seller's own account and disclaim platform fees; Lemon Squeezy is MoR. Both postures mature.
- **Rejected as definitional: license keys.** Present in 6/6 sampled products but the deep form (activation limits, validation API, update delivery, renewals) is software-segment-weighted (EDD Software Licensing, Lemon Squeezy); the file-download pole (ebooks, templates) stands without it. Common, with a software-weighted deep form.
- **Anti-overfitting note:** bundles and discount codes appear in 6/6 — market maturity, not definition. The historical pole (E-junkie) and the button-only pole (DPD) remain the Type without most L1 machinery.

## Historical / Market-Sample Check

- **Older-generation products**: E-junkie (button-code cart era, still operating) satisfies the core exactly — file/code catalog, buy buttons on any site, own processor, instant delivery. No storefront, no MoR, no buyer accounts.
- **Long-lived current products**: EDD claims 13+ years and 30M+ processed orders; DPD claims tens of thousands of vendors over a long life. Both are download-era products whose current form still reduces to the same spine.
- **Regional variation**: E-junkie's regional processor list (Razorpay, Instamojo, Paytm) and DPD's VAT/GST + multi-language checkout show the same core under non-US rails and languages.
- **Deployment spread**: hosted service (DPD, Payhip), plugin inside the seller's own CMS (EDD), embed-anywhere (SendOwl), MoR suite (Lemon Squeezy) — all satisfy the core.
- Conclusion: nothing era-specific, region-specific, or deployment-specific entered the defining core.

---

## Boundary Findings

### vs Digital Product Commerce Platform (§27, processed 2026-09-07) — the central finding of this pass

**The two leaves name the same Application Type.** Evidence:

1. **The products say so.** EDD's terminology doc: "Download (or Product): these terms are used interchangeably. A download is a product." DPD's brand expansion is "Digital Product Delivery" while its marketing leads with "digital downloads."
2. **The populations coincide.** Payhip, SendOwl, and E-junkie were sampled by both passes as representatives of their respective names. EDD's comparison set (Gumroad, WooCommerce, Shopify, Etsy, Envato) is the §27 pass's market.
3. **The structure coincides.** The four-part defining core, the standard-capability set, and the variant axes derived independently from the download-branded sample match the §27 pass's model point for point.
4. **The §27 pass pre-flagged it**: "the seller-type split is NOT a real market seam… Recommend joint review; do not resolve unilaterally."

Resolution recorded: **probable duplicate/alias pair** — "digital download commerce platform" is the download-centric vernacular; "digital product commerce platform" is the product-centric framing of the same seller-side category. No directory change made; joint review recommended. This document is written as a full standalone record of the Type from this leaf's own evidence, cross-referencing the §27 document.

### vs Digital Goods Store (§05.22 sibling, unprocessed)

The sibling leaf's most plausible distinct reading is the **venue** — a store where buyers browse and purchase digital goods (whether first-party retail or multi-vendor marketplace). That is a different structure from the seller-side operating platform documented here (the platform is the seller's tooling, not the buyer's shopping destination). The Digital Goods Store pass should test this seam; the name-space of §05.22 + §27 (three leaves) may reduce to two Types (venue + seller platform) or fewer.

### vs Online Store Builder / E-commerce Platform / Headless Commerce (§05.01, processed)

- Store builders: generic catalog + cart + shipping machinery; fulfillment is whatever the seller configures; no delivery engine as center. EDD's own docs draw this line from the product side: physical-products-first businesses should use a general ecommerce solution.
- Headless commerce: engine consumed through APIs with the buying experience built outside; no deliverable-anchored digital fulfillment as the defining act.
- This Type: the product-with-deliverable + automated delivery is the managed unit.

### vs Checkout Platform (§05.06, unprocessed)

Checkout machinery without the product/delivery catalog as the managed unit. DPD's checkout-domain page shows the seam from inside: the checkout is infrastructure the platform operates, but the platform's identity is delivery of the vendor's products, not the payment transaction itself.

### vs Online Marketplace (§05.02, unprocessed)

Marketplace = the venue where discovery and multi-vendor transaction happen; this Type = the seller's own direct-sales infrastructure. Several sampled products position explicitly against marketplaces ("no marketplace, no middleman"; EDD's marketplace-alternatives content); where a marketplace layer exists (Lemon Squeezy, E-junkie), it is an optional overlay.

### vs the §27 creator-cluster siblings (processed)

Inherited seams, confirmed from this side: purchase → delivered file/key (here) vs goods (Creator Storefront), standing curriculum access (Course Commerce), cycle-maintained entitlement (Subscription/Membership), tracked service (Coaching), nothing-owed (Tip Platform). EDD sells courses as file deliverables (course materials, workbooks, video lessons as downloads) — the file-delivery form, not a curriculum player.

### "去掉什么就变成另一个 Type" summary

- Remove automated digital delivery (fulfillment becomes shipping/manual) → generic e-commerce / store builder
- Remove the purchasable product catalog (keep only buttons/links) → checkout tool / link surface
- Remove discrete file conversion (purchase → standing structured access) → course commerce
- Remove discrete file conversion (purchase → cycle-maintained entitlement) → subscription/membership
- Re-center on the buyer's shopping venue → Digital Goods Store / Marketplace territory
- Same Type under the other name → Digital Product Commerce Platform (alias pair, flagged)

## Uncertainties

1. **Gumroad** unverified across two passes (repeated timeouts). Archetype status safe (named in EDD's comparison set and the §27 pass's evidence); no operational claims drawn.
2. **Sellfy** unverified (403 in prior pass).
3. **Whether the directory will keep both leaves or merge them** — recorded for joint review; this pass does not resolve the directory.
4. **Digital Goods Store's intended reading** (venue vs seller tooling vs something else) — unresolved until its own pass; this pass only records that the seller-platform reading is taken by this leaf.
5. Refund→access-revocation universality: directly observed in 3/6 (SendOwl explicit, Lemon Squeezy refunds docs, Payhip refund docs); EDD documents refunds and refund reports but the automatic-revocation behavior was not confirmed on the fetched pages. Stated as common, not universal.
6. EDD's PWYW: listed as a homepage feature bullet ("pay-what-you-want pricing") but no dedicated doc page fetched; treated as present-but-shallow evidence.

## Final Synthesis

A **Digital Download Commerce Platform** is the seller-side commerce application whose defining loop is: a seller defines a catalog of digital products — each anchored to its own deliverable content (uploaded files and/or license codes) — exposes them for purchase through platform-operated surfaces (a hosted page or storefront, buy buttons/links placed anywhere, or store blocks composed inside the seller's own site), and the platform itself converts each successful payment into automated delivery of that content (instant download page, emailed durable link, license key, or stream) with no per-order seller labor, resolving the money to the seller either as a deposit into the seller's own payment account or as a merchant-of-record payout.

Around this spine, mature products add: variants and bundles, discount codes and pay-what-you-want, delivery-security machinery (download limits, buyer-stamped/encrypted files, signed or expiring links, license-key management with activation control, refund-triggered revocation), file updates with past-buyer notification, order operations and test modes, durable buyer access (emailed link or buyer account), marketing machinery (affiliates, upsells, abandonment recovery, email), analytics, APIs, and multi-store/staff accounts at scale.

The Type varies along: deployment posture (hosted service ↔ plugin inside the seller's own CMS ↔ embed-anywhere), money posture (merchant-of-record ↔ seller-connected), seller segment (authors/teachers/artists ↔ software vendors ↔ educators), attached commerce modes, delivery form (files ↔ streaming ↔ drip), and discovery posture (marketplace ↔ direct-only). Its historical pole (button-code carts) and its button-only present pole satisfy the same spine without storefront, MoR, or buyer accounts.

**Taxonomy conclusion:** this leaf and the §27 leaf Digital Product Commerce Platform name **one Application Type** — "digital downloads" and "digital products" are the market's interchangeable terms for the same seller-side category (the products themselves state the equivalence). Recorded as a probable duplicate/alias pair for joint review; no directory change made unilaterally.
