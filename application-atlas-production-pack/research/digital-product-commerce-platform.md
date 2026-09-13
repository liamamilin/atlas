# Research Notes — Digital Product Commerce Platform

Research date: **2026-09-07**

Directory location: §27 Media, Entertainment, Creator & Culture (siblings: Link-in-Bio Platform, Creator Storefront [processed], Paid Community Platform, Fan Membership Platform, Creator Subscription Platform [processed], Creator Tip Platform [processed], Creator Course Commerce Platform [processed], Coaching Commerce Platform [processed]; distant family: Digital Goods Store / Digital Download Commerce Platform §05.22, Online Store Builder / E-commerce Platform §05.01, Checkout Platform §05.06, Digital Product Catalog / PIM §05.04, Payment Gateway / Payment Processing §08)

---

## Research Goal

Understand what a Digital Product Commerce Platform actually is as an Application Type: what objects exist inside it, what the seller and buyer each do, how a purchase turns into a delivered product, which machinery is common, and where the Type's boundaries sit — especially against the already-processed creator-economy siblings (Creator Storefront, Creator Course Commerce, Creator Subscription, Coaching Commerce) and against the unprocessed commerce-section leaves with overlapping names (§05.22 Digital Goods Store / Digital Download Commerce Platform).

## Initial Boundary

Hypothesis before research:

1. Core use: a seller (creator, indie maker, small software vendor) sells digital products — files (ebooks, PDFs, audio, video, templates, presets, fonts, design assets, software) and/or codes/license keys — directly to buyers, with the platform automating purchase and delivery.
2. Primary users: the seller (dashboard side) and the buyer (product page / checkout / download side).
3. Nearest neighbors: Creator Storefront (spans physical + digital, storefront-centric), Creator Course Commerce (structured curriculum + consumption machinery), §05.22 Digital Goods Store (name overlap, unprocessed), Online Store Builder / E-commerce Platform (generic machinery), Link-in-Bio Platform (surface sibling).
4. Probable boundary test (inherited from the processed cluster): **what the purchase converts into** — discrete file delivery here, vs goods shipment (storefront), standing access entitlement (courses/memberships), tracked service engagement (coaching).
5. Unknowns: whether a storefront surface is definitional or optional (delivery-only products like SendOwl-class suggest optional); whether the money posture (merchant-of-record vs seller-connected gateway) varies; how much security machinery (stamping, limits, license keys) is common vs optional.

## Research Questions

- What is a "digital product" as an object in these systems? What hangs off it (files, variants, price, license keys)?
- What are the seller's setup steps from account to first sale?
- What exactly happens after payment? What does the buyer receive, through which channels, and with what durability?
- How do the security/anti-piracy mechanics work (download limits, stamping, expiring links, license keys)?
- What happens on refund — is access revoked?
- How do sellers get paid? Merchant-of-record vs connected-gateway postures?
- Which selling machinery is common (discounts, PWYW, bundles, upsells, affiliates, email)?
- Is a storefront required? What is the minimal sales surface (buy buttons/links/embeds)?
- Where do subscriptions/memberships/courses/physical goods sit — inside the core or as attached variants?
- How do the §27 cluster seams and the §05.22 name-space overlap resolve?

## Representative Products

Selection logic: market representativeness + documentation quality + different product philosophies + different customer tiers + one legacy/historical pole for the historical-sample check.

| Product | Philosophy / posture | Customer tier | Evidence this pass |
|---|---|---|---|
| **Lemon Squeezy** | digital-only, merchant-of-record, software/SaaS-leaning, developer-first (API/webhooks/licensing), hosted storefront + checkout overlays | indie software vendors, SaaS, digital creators | Tier 1+2 fetched (homepage, digital-products page, docs root) |
| **SendOwl** | delivery-first "no walled garden": embed checkout anywhere, connect your own gateway, flat monthly price, security machinery as differentiator | solopreneurs → businesses/teams | Tier 2 fetched (homepage, platform page) |
| **Payhip** | simple indie storefront, connect PayPal/Stripe, digital + courses + memberships + physical, free-tier friendly | individual creators/sellers | Tier 1 fetched (help center root, Products category, Add Digital Product, Protect Your Products, How Payhip Works) |
| **E-junkie** | legacy digital-goods cart: copy-paste buy buttons/links on any site, connect any processor, no real storefront required | long-tail sellers; 2005-era pattern still live | Tier 2 fetched (homepage) |
| **Gumroad** | market archetype for creator digital-product sales | creators | **not fetched** — gumroad.com/help.gumroad.com timed out ×3; kept as named market anchor only |

Deliberately not sampled after failure: Sellfy (403 ×2, abandoned per source-access rule).

## Sources

Fetched 2026-09-07 (all Layer A unless noted):

- Lemon Squeezy — https://www.lemonsqueezy.com/ ; https://www.lemonsqueezy.com/ecommerce/digital-products ; https://docs.lemonsqueezy.com/help
- SendOwl — https://sendowl.com/ ; https://sendowl.com/platform
- Payhip — https://help.payhip.com/ ; https://help.payhip.com/category/41-products ; https://help.payhip.com/article/59-adding-a-digital-product ; https://help.payhip.com/article/79-protecting-your-products ; https://help.payhip.com/article/132-how-payhip-works
- E-junkie — https://www.e-junkie.com/
- Sibling research (context, Layer B for cluster seams): research/creator-storefront.md, research/creator-course-commerce-platform.md, research/creator-subscription-platform.md, research/coaching-commerce-platform.md

**Source-access limitations:**
- Gumroad: all fetch attempts timed out (3). No operational detail for Gumroad is asserted anywhere; it appears only as a market-representative name and as a migration-source named by Lemon Squeezy's own docs ("Migrating from Gumroad").
- Sellfy: 403 twice; abandoned.
- No independent reviews or third-party sources were needed; official documentation was sufficient.

---

## Product Observations

### Lemon Squeezy (digital-only MoR, software-leaning)

**Positioning:** "Payments, tax & subscriptions for software companies… Selling digital downloads, subscriptions, and software licenses." Testimonial on the page: "refreshing to see Lemon Squeezy focusing solely on digital products." Product span: "SaaS subscriptions, software licenses, online courses, design assets, themes, templates, video content, fonts and more."

**Key observations:**

- **File hosting**: upload and host any type of digital file; "attach and store an unlimited number of files to each of your products"; file types listed: zip, photos, audio, video, apps, ebooks, software licenses. Platform handles "file storage and secure delivery to customers after purchase."
- **Secure download links**: "Your download links are securely signed, throttled, and more" (security against link sharing/abuse).
- **License keys**: automatically issue license keys after each sale; deactivate, re-issue, full control; docs section "Licensing" includes "License keys and subscriptions" (keys tied to subscription state).
- **Variants**: "attach new files and pricing to each variation" — variants are file+price bundles around one core product.
- **File versioning**: dedicated help doc "Managing file versions" — updating deliverables for a product is first-class.
- **Purchase surfaces**: hosted product pages / online store (template, customizable, custom domain), hosted checkout, **checkout overlays** (embed on any site via Lemon.js), checkout links, WordPress plugin for checkout buttons.
- **Payments posture: merchant of record.** "We handle payments, merchant fees, fraud and sales tax"; 135+ countries, 20+ payment methods, multi-currency; docs: sales tax & VAT, refunds & chargebacks, W-8/W-9 tax forms for sellers. Platform resolves money to the seller as payouts (docs "Getting paid").
- **Attached commerce modes**: subscriptions (trials, dunning/failed-payment recovery, upgrades/downgrades), usage-based billing, lead magnets (free products to grow email list), PWYW, single payment.
- **Marketing machinery**: discount codes, bundles + upsells, affiliates (full merchant+affiliate program with payouts and fees docs), built-in email marketing (broadcasts, subscribers, segments), abandoned cart emails, customer segmentation.
- **Buyer side**: "My orders" docs + **Customer Portal** (self-service for the store's customers).
- **Operations**: order refund, resend receipt, generate invoice, export orders, discount codes, **test mode**, 2FA, teams (multi-user), multiple stores per account, webhooks + full REST API, Zapier/ConvertKit/Mailchimp integrations.
- **Marketplace**: a discovery marketplace exists (docs "Marketplace — Guidelines, Categories").
- **Migration docs** exist for Gumroad, Stripe, Paddle — evidence these are the same market category.
- 2026 banner: "Lemon Squeezy + Stripe Managed Payments" (acquired-by-Stripe era update).

### SendOwl (delivery-first, embed-anywhere, own-gateway)

**Positioning:** "Sell anything digital — simply, securely, reliably. Sell directly to your customers — no marketplace, no middleman." "SendOwl plugs into your existing website, social presence, or platform. No walled gardens, no ecosystem lock-in… modular by design."

**Key observations:**

- **Setup loop (as marketed)**: 1) Create & upload products; 2) **Connect your payment gateway** (Stripe/PayPal/Square), "list your product anywhere," start delivering orders securely; 3) Collect payments ("get paid instantly").
- **Sales surface is NOT a storefront-first model**: "Embed checkout anywhere. Your website, Shopify, WordPress, Notion, Linktree, or link directly from social." Buy-button/checkout-embed posture ("copy and paste the code we provide"). A storefront page exists but is deliberately minimal ("showcasing up to 10 digital products").
- **Delivery machinery**: automatic file delivery; large files, unlimited storage; **audio & video streaming at any size** (with or without download allowed); **license key generation & delivery**; **drip content over time** ("set and sell digital files over any duration"); **automatic access management on refunds** (refund revokes delivery access).
- **Security machinery (the product's flagship differentiator)**: PDF stamping ("each download is uniquely stamped with the buyer's information"), download limits ("control the number of download attempts"), time-limited/expiring download links, document locking (prevent copy/print), IP and email blocking.
- **Product types**: digital media assets (music, videos, images, PDFs, "virtually all digital file types"), subscriptions (with management/reporting), bundles (collections incl. gaming codes), streaming, courses & drip files (file-based courseware), software downloads & license keys. Physical goods supported (testimonials mention "downloads and physical goods") but not the positioning center.
- **Checkout machinery**: three cart templates (overlay → two-page flow), custom checkout fields, upsells & cross-sells, cart abandonment recovery emails, discount codes, PWYW (seller sets minimum), pre-orders (sell before release, auto-deliver on launch), gifting (scheduled delivery windows + messages).
- **Marketing**: affiliate programs with per-affiliate links and commission tracking; email-platform integrations (Mailchimp, Kit) including "automatically send update emails to existing customers as you upload new products"; order tagging, URL redirects, custom CSS/JS, tracking codes; webhooks + API.
- **Money posture: seller owns the rails.** "Keep more of what you earn with flat monthly pricing — no percentage cuts… Handle taxes and accounting your way." Sales tax & EU VAT support = calculation assistance and tax-rule configuration ("complying with EU VAT rules simply by checking one additional box") — not MoR.
- **Teams/scale**: multi-user accounts with permission levels, 2FA; "enterprise scale" positioning.
- **Membership integrations**: WordPress membership plugins (Wishlist Member, MemberMouse, s2Member Pro) — delivery engine feeding external membership systems.
- Vendor-competitive framing on the page (treat as marketing): "SamCart optimizes checkout but delivery is basic. Gumroad focuses on simplicity but lacks security. SendOwl delivers both."
- Help center exists at help.sendowl.com with per-feature articles (pdf-stamping, license-codes, digital-file, api-introduction, selling options…); "10+ years helping creators" claimed.

### Payhip (indie storefront, connected gateways, multi product types)

**Positioning (help center "How Payhip Works"):** "an e-commerce platform that enables anyone to sell their work directly to their fans and followers… your own unique storefront where you can showcase your products — from ebooks, software, clothing, art, music, you name it."

**Product types (Products category):** digital, courses, coaching, memberships, physical; plus bundles, collections, free products, PWYW, custom digital orders.

**Digital product setup (Add Digital Products article):**

1. Products page → Add new product → select **Digital Product**
2. Upload product files (multiple files: ebooks, PDFs, audio, video, other types)
3. Title, price, cover image
4. Optionally embed audio/video content via external platform links (YouTube, Vimeo, SoundCloud)
5. Description

Advanced product options: **variants** ("different versions… different formats, tiers, or bundles"), tax exempt flag, **"Product is an ebook" flag → reduced EU VAT rates in certain countries**, preview/sample file for buyers, **limit the number of copies sold** (scarcity cap), auto-subscribe buyers to mailing list, **generate unique license keys for each sale** (software).

**Digital buyer flow (How Payhip Works):**

1. Customer visits the product page and purchases
2. Redirected to the **download page**, instant download
3. **Email receipt includes the download-page link for future access** (durability beyond the session)
4. Payment **deposited to your PayPal/Stripe account**; sale notification email to seller

**Security (Protect Your Products):** download limits (default value documented in the article; seller-adjustable; seller can reset per customer) and **PDF stamping** (buyer's email + purchase date stamped on each PDF page; portrait-mode PDFs under a size threshold; product-specific mechanics).

**Other mechanics:** product visibility states (Visible / Invisible / Unlisted-direct-link-only); editable after publish; test purchase via 100% coupon; file-type restrictions for executables (specific list in article); per-file size cap (article states 5GB — vendor-specific, not generalized); pre-orders via workaround only (no dedicated feature); store customization + custom domains (Domain Providers category); buyers have accounts (Buyers help category); sales-tax category; developer/API + integrations + analytics categories.

**Money posture:** payments deposit directly to the seller's PayPal/Stripe (connected-gateway, not MoR). EU VAT handled at the product/tax-setting layer (ebook rates, tax-exempt), not as full merchant-of-record on the homepage positioning.

### E-junkie (legacy digital-goods cart — historical pole)

**Positioning:** "We help you sell downloads. Copy-paste a link to sell downloads, or physical goods on any website. Or, create a simple shop in 5 minutes. Sell art, ebooks, comics, game codes, merchandise, and more!"

**Setup loop:** 1) **Link your payment processor** (PayPal, Stripe, Braintree, Authorize.Net, 2Checkout, Razorpay, Instamojo, Paytm — including regional Indian processors); 2) Add product details ("sell file downloads, codes, tickets, tangible items!"); 3) **Copy-paste button codes or links** into website/blog/social networks/WhatsApp/Messenger.

**What can be sold:** file downloads (comics, ebooks, art, music, video, software), **codes** (game codes, gift cards), tickets, tangible items (with shipping calculation: UPS/USPS/flat rate/custom).

**Features:** "Secure digital delivery — instant download of your files and codes after a successful payment"; PWYW; donations; free checkout; discounts; **PDF stamping**; affiliate network; product bundles; product variations; eBay **digital delivery** integration; Patreon digital-delivery integration; Buy Now Button; Shopping Cart; Product Page; hosted shop; **self-hosted shop** (open-source on GitHub); marketplace (market.e-junkie.com).

**Historical significance:** this is the older-generation realization of the Type (button-code cart era). It demonstrates the minimal core needs **no storefront, no MoR, no buyer accounts** — product+file, buy button, own processor, instant delivery already constitute the Type.

### Gumroad (unfetched — market anchor only)

All fetch attempts timed out. Included as representative because it is the market archetype of creator digital-product sales and because Lemon Squeezy's own docs name it as a migration source ("Migrating from Gumroad"). **No operational claims about Gumroad are made from this pass.**

---

## Cross-product Comparison

| Structure | Lemon Squeezy | SendOwl | Payhip | E-junkie | Strength |
|---|---|---|---|---|---|
| Seller-defined product catalog anchored to files/codes | ✓ (unlimited files/product) | ✓ (unlimited storage) | ✓ (multi-file, size cap) | ✓ (file downloads, codes) | **Core, 4/4** |
| Platform-operated purchase surface (page and/or button/link/embed) | ✓ (store + overlays + links + WP plugin) | ✓ (embed anywhere + minimal storefront) | ✓ (storefront + product pages) | ✓ (buttons/links/cart; optional shop) | **Core, 4/4** |
| Automated delivery on payment (instant download page/link/email) | ✓ (secure signed links) | ✓ (automatic delivery; streaming; drip) | ✓ (download page + emailed link) | ✓ ("instant download after successful payment") | **Core, 4/4** |
| License keys / codes delivery | ✓ (+ subscription-tied) | ✓ (+ gaming codes) | ✓ (per-sale keys for software) | ✓ (codes, gift cards, tickets) | Common (4/4 present, but software-segment-weighted — Common, not Core) |
| Seller earnings path to seller's own rails OR MoR payout | MoR payouts | deposits to seller Stripe/PayPal | deposits to seller PayPal/Stripe | deposits to seller processor | **Core (one of two realizations, 4/4)** |
| Tax handling posture | MoR (full) | seller-side + VAT tooling | seller-side + VAT product flags | seller-side (processor) | Variant axis (both postures mature) |
| Storefront as primary surface | ✓ hosted store | ✗ embed-first (10-item page) | ✓ | optional simple shop | Variant axis — NOT definitional |
| Product variants (files+price) | ✓ | (tailored pages by type) | ✓ | ✓ (variations) | Common |
| Bundles | ✓ | ✓ | ✓ | ✓ | Common |
| Discount codes | ✓ | ✓ | ✓ (implied by test-coupon doc) | ✓ | Common |
| PWYW | ✓ | ✓ (minimum) | ✓ ("+" syntax) | ✓ | Common (4/4) |
| Free products / lead magnets | ✓ | (drip/preorder adjacent) | ✓ (free products) | ✓ (free checkout) | Common |
| Download limits | (signed/throttled links) | ✓ | ✓ (default documented) | — | Common (delivery-security machinery, form varies) |
| PDF stamping / buyer-marked files | — | ✓ | ✓ | ✓ | Common (3/4; LS uses signed links instead — mechanism varies) |
| Expiring/time-limited links | (signed/throttled) | ✓ | — | — | Optional / product-specific form |
| File updates & versioning | ✓ (doc) | ✓ (+ buyer update emails) | ✓ (article) | — | Common |
| Refund → access handling | ✓ (MoR refunds/chargebacks) | ✓ (auto access revoke) | ✓ (refund docs; buyers category) | — | Common (3/4 direct) |
| Streaming delivery | — | ✓ (audio/video, any size) | ✓ (external embeds) | — | Optional (form varies strongly) |
| Subscriptions attached | ✓ (+dunning) | ✓ | ✓ (+memberships) | — | Common attached mode |
| Courses / drip | (courses as products) | ✓ (drip files) | ✓ (structured course product) | — | Attached mode; structured-course pole → sibling Type |
| Physical goods | ✗ (digital-only) | ✓ (secondary) | ✓ | ✓ (+shipping calc) | Optional; center-shift marker → Creator Storefront |
| Affiliates | ✓ | ✓ | ✓ (marketing category) | ✓ | Common |
| Upsells / abandonment | ✓ | ✓ | (marketing category) | — | Common |
| Email marketing | ✓ built-in suite | integration | mailing lists | Mailchimp/Zapier | Common (depth varies) |
| API/webhooks | ✓ full | ✓ | ✓ (developer category) | (integration ecosystem) | Common |
| Buyer accounts / portal | ✓ (Customer Portal, My orders) | (delivery-link based) | ✓ (Buyers category) | — | Common |
| Marketplace/discovery layer | ✓ | ✗ ("no marketplace" positioning) | ✗ | ✓ | Optional, polarizing |
| Teams / multi-user + 2FA | ✓ | ✓ | (account settings category) | — | Common at business tier |
| Test purchase mode | ✓ (test mode) | — | ✓ (100% coupon) | — | Common (form varies) |
| Pre-orders | — | ✓ built-in | workaround only | — | Optional |

### Evidence-layer summary

- **Layer A (directly observed)**: every cell above for the four fetched products.
- **Layer B (cross-product)**: catalog+purchase+instant-delivery+earnings as the shared spine (4/4); security machinery (limits/stamping/keys) as standard delivery hygiene; marketing machinery (discounts/PWYW/bundles/affiliates) as standard.
- **Layer C (canonical inference)**: the Type = "the purchase converts into automated delivery of the product's own digital content"; storefront and MoR are realizations, not requirements; the file (not the shop, not the curriculum, not the membership) is the center of gravity.

---

## Abstraction Levels

### L0 — Defining Invariant (minimal)

```text
Seller-defined catalog of digital products
└── each product anchored to its own deliverable digital content
    (uploaded files and/or codes/license keys)
└── platform-operated purchase machinery
    (product page, storefront, buy button/link/overlay/embed — any surface)
    resolving a payment transaction
└── automated digital fulfillment
    (the platform itself delivers the deliverable — download, key, stream —
     with no per-order seller labor)
└── seller earnings path
    (transaction resolves into seller compensation recorded by the platform:
     deposit to seller-connected gateway, or platform-collected payout)
```

Remove the deliverable-anchored catalog → generic store builder. Remove purchase machinery → file hosting. Remove automated delivery → generic e-commerce (manual/shipped fulfillment). Remove earnings path → not commerce. Storefront, MoR, license keys, buyer accounts, subscriptions, marketing machinery, physical goods — all removable while the Type remains recognizable (E-junkie-era products prove it).

### L1 — Common Mature Structure

- Product page / hosted store with customization, custom domains (some products); minimal storefront in embed-first products
- Product variants (file+price bundles), bundles, discount codes, PWYW (4/4), free products/lead magnets
- Delivery-security machinery: download limits, buyer-stamped files (PDF stamping) or signed/throttled links, license keys, refund-triggered access revocation
- Email receipt with durable download link; buyer-side surfaces (emailed link, buyer accounts/customer portal)
- File update/versioning with buyer notification in mature products
- Order operations (refund, resend receipt, invoices, export), test-purchase mode
- Marketing machinery: affiliates, upsells/cross-sells, cart abandonment, mailing-list/email integration
- Analytics; API/webhooks; teams + 2FA at business tier

### L2 — Variant / Optional

- **Sales-surface posture**: hosted-storefront-first ↔ embed/link-anywhere ("headless") ↔ both
- **Money posture**: merchant-of-record (platform is seller of record; handles tax/VAT/fraud/chargebacks; pays out) ↔ seller-connected gateway (deposits go straight to seller's processor; seller handles taxes with platform tooling)
- **Seller segment**: creators/indie makers ↔ software vendors (licensing, usage-based billing) ↔ educators
- **Attached commerce modes**: subscriptions, memberships, structured courses, coaching, physical goods — present in some products, each shifting weight toward a sibling Type when centered
- **Delivery form for media**: plain files ↔ streaming (hosted or external-embed)
- **Discovery layer**: marketplace/directory ↔ strictly direct ("no marketplace, no middleman")
- **Product-type breadth**: pure files ↔ files + codes/keys/tickets/gift cards
- **Scale posture**: solo/free-tier ↔ business teams/enterprise

### L3 — Vendor-specific (research notes only, excluded from final doc)

- Payhip: PWYW "+" price syntax; 5GB per-file cap; blocked executable file-type list; portrait-only PDF stamping below a size threshold; default download-limit value; Visible/Invisible/Unlisted visibility states; copy-sales cap; custom (manual) digital orders; pre-orders only via workaround
- Lemon Squeezy: Lemon.js overlay API; checkout overlay vs hosted checkout distinction; marketplace guidelines/categories; W-8/W-9 tax forms; license-keys×subscriptions interplay; test mode; multiple stores per account; Stripe acquisition-era update; migration docs (Gumroad/Stripe/Paddle)
- SendOwl: storefront limited to 10 showcased products; WordPress membership-plugin integrations (Wishlist Member, MemberMouse, s2Member Pro); flat monthly pricing stance; competitive framing vs SamCart/Gumroad; gifting with scheduled delivery windows; Parli (sibling AI product)
- E-junkie: eBay digital delivery; self-hosted shop on GitHub; regional processors (Razorpay, Instamojo, Paytm); Patreon delivery integration; tickets as product type
- Gumroad: none asserted (unfetched)

---

## Vendor-specific vs Rejected Findings

- **Rejected as definitional: storefront.** SendOwl is explicitly embed-first with a minimal storefront page; E-junkie's canonical surface is a copy-paste button. A storefront is a common (L1) realization of the purchase machinery, not the Type.
- **Rejected as definitional: merchant-of-record.** Two mature postures coexist (LS MoR vs Payhip/SendOwl/E-junkie gateway-connected). MoR is a money-posture variant, not the Type.
- **Rejected as definitional: license keys.** 4/4 sampled products have codes/keys, but the mechanism is software-segment-weighted and the file-download pole stands alone (ebooks, templates). Classified Common.
- **Rejected: "creator-only" scoping.** The sampled seller population includes software companies (LS positioning, ITFactory via SendOwl, theme/plugin vendors) and educators. The Type's user is "a seller of digital products," of which creators are the largest but not the defining segment — despite the §27 placement.
- **Anti-overfitting note:** all four sampled products support PWYW and discounts; that is market maturity (L1), not definition. The historical pole (E-junkie) and the delivery-first pole (SendOwl) both remain the Type without most L1 machinery.

## Historical / Market-Sample Check (per §24)

- **Older-generation products**: E-junkie (button-code cart era, still operating) satisfies the L0 exactly — file/code catalog, buy buttons on any site, own processor, instant delivery, PDF stamping. No storefront, no MoR, no buyer accounts required.
- **Regional variation**: E-junkie's regional processor list (Razorpay, Instamojo, Paytm) shows the same core under non-US payment rails; the money posture (deposit to seller's processor) is region-independent.
- **Platform-native / differently-positioned**: SendOwl's embed-anywhere posture shows the Type works as a delivery engine attached to *someone else's* web surface; Payhip's free-tier indie posture shows it at minimal scale. Both satisfy L0.
- Conclusion: the definition survives the historical and posture spread; nothing era-specific or region-specific entered L0.

---

## Boundary Findings

### vs Creator Storefront (§27, processed) — the flagged joint review, now executed from this side

Cluster-established fulfillment-structure test: what the purchase converts into.

- **Creator Storefront**: purchase → **goods** (manufactured via platform production network, self-sourced shipped goods, or downloads) centered on a **seller-owned branded storefront**; physical fulfillment machinery (POD, shipping, support for physical orders) is a standard capability.
- **Digital Product Commerce Platform**: purchase → **delivery of the product's own digital content** (file download / license key / stream); storefront optional and often minimal; **physical fulfillment is outside the defining core** (appears only as an attached option in some products, absent entirely in the digital-only pole).
- Diagnostic (confirmed bidirectionally): remove physical fulfillment AND demote the branded storefront to optional → this Type; re-center on owned branded shop + physical goods → Creator Storefront.
- **Honest spectrum note**: market products straddle (Gumroad-class sells both; Payhip/SendOwl/E-junkie all support physical as a secondary type). The Types are kept independent because the market sustains a distinct "sell digital products" category (LS: "focusing solely on digital products"; SendOwl/E-junkie digital-first positioning) and because the machinery center of gravity differs (delivery security + file versioning + license keys vs POD/shipping/storefront design). Flag stands as a documented near-seam, not a merge.

### vs Creator Course Commerce Platform (§27, processed)

- Course platform: purchase → **standing access entitlement to structured curriculum** (units/lessons) consumed in a **course player with progress tracking**; offers/pricing plans bound to the course.
- This Type: purchase → **discrete delivered content** (files as-is). SendOwl's "Courses & Drip Files" and LS "online courses" as product types are file-delivery shaped (drip of files over time, no player/progress machinery) — evidence of absorption at the edges, not of a boundary failure. The seam test (player+progress+curriculum structure = course Type; delivered file = this Type) holds.

### vs Creator Subscription Platform / Fan Membership (§27, processed)

- Subscription/membership: purchase → **standing entitlement maintained across billing cycles**; cancellation ends access.
- This Type: discrete one-time conversion (even when subscriptions are an attached mode selling files periodically, the defining transaction remains file delivery). Memberful's downloads seam (documented in that pass) is consistent from this side.

### vs Coaching Commerce Platform (§27, processed)

- Coaching: purchase → tracked human-service engagement (session credits, milestones). Payhip sells coaching as an attached product type with a milestone dashboard — attached mode, not this Type's core; this Type's core conversion has no service-fulfillment structure.

### vs §05.22 Digital Goods Store / Digital Download Commerce Platform (unprocessed) — taxonomy flag

The directory carries both this §27 leaf and §05.22 leaves whose names cover the same activity ("digital goods store", "digital download commerce platform"). Possible resolutions when §05.22 is processed: (a) §05.22 = the generic/non-creator digital-goods selling Type and this §27 leaf = creator-economy positioning (fragile — the researched market does not split by seller type: the same platforms serve creators and software vendors), or (b) genuine duplicate/alias pair. The evidence here (seller population spans creators ↔ software companies within single products) suggests the seller-type split is NOT a real market seam. Recommend joint review; do not resolve unilaterally.

### vs Online Store Builder / E-commerce Platform / Checkout Platform (§05.01/§05.06, unprocessed)

- Store builders: generic catalog + cart + shipping/tax machinery; fulfillment is whatever the seller configures; no delivery engine as center.
- Checkout platforms: payment-transaction machinery without the product/delivery catalog as the managed unit.
- This Type: the **product-with-deliverable + automated delivery** is the managed unit. E-junkie/SendOwl embed-buttons overlap with checkout-tool surfaces, but the delivery engine + file catalog distinguish them.

### vs Link-in-Bio Platform (§27 sibling, unprocessed)

- Link-in-bio's defining object is the aggregated link profile; commerce may be attached. Here the defining object is the product-with-deliverable and its purchase→delivery loop. SendOwl listing Linktree as an integration surface confirms the two compose rather than compete.

### vs Digital Product Catalog / PIM (§05.04, unprocessed)

- Catalog/PIM: manages product information, no selling/delivery loop. Here the catalog exists to be sold and auto-delivered.

### "去掉什么就变成另一个 Type" summary

- Remove automated digital delivery (fulfillment becomes shipping/manual) → generic e-commerce / store builder
- Remove the purchasable product catalog (keep only the link surface) → Link-in-Bio / landing-page surface
- Remove discrete file conversion (purchase → standing structured content access) → Creator Course Commerce
- Remove discrete file conversion (purchase → standing entitlement across cycles) → Creator Subscription / Fan Membership
- Remove discrete file conversion (purchase → tracked service) → Coaching Commerce
- Re-center on branded storefront + physical goods → Creator Storefront

## Uncertainties

1. **Gumroad's current structure** unverified this pass (fetch failures). The archetype status is safe (named as migration source by LS docs; universally present in the sibling passes' evidence), but any Gumroad-specific mechanics are deliberately absent.
2. **Sellfy** unverified (403). Its inclusion in the market set is likely but unconfirmed from primary sources this pass.
3. **Where the §05.22/§27 name-space resolves** — flagged, not resolved (see Boundary Findings).
4. Whether buyer accounts (vs pure emailed-link access) should be L1-Common or L2 — evidence is 2/4 explicit (LS Customer Portal/My orders, Payhip Buyers category); classified L1-Common with the emailed durable link as the near-universal baseline.
5. Refund→access-revocation universality: directly observed in 3/4 (SendOwl explicit "automatic access management on refunds"; LS refunds docs; Payhip refund/buyer docs); E-junkie not confirmed on-page. Stated as common, not universal.

## Final Synthesis

A **Digital Product Commerce Platform** is the seller-side commerce application whose defining loop is: a seller defines a catalog of digital products — each anchored to its own deliverable content (uploaded files and/or license codes) — exposes them for purchase through platform-operated surfaces (product page, storefront, or embeddable buttons/links), and the platform itself converts each successful payment into automated delivery of that content (instant download page/link, emailed durable link, license key, or stream) with no per-order seller labor, resolving the money to the seller either by deposit to the seller's connected payment account or by platform-collected payout as merchant of record.

Around this spine, mature products add: product variants and bundles, discount codes and PWYW, delivery-security machinery (download limits, buyer-stamped files, signed/expiring links, license-key management, refund-triggered revocation), file versioning with buyer updates, order operations and test modes, buyer accounts/portals, marketing machinery (affiliates, upsells, abandonment recovery, email integration), analytics, APIs/webhooks, and teams.

The Type varies along: sales-surface posture (storefront-first ↔ embed-anywhere), money posture (MoR ↔ connected gateway), seller segment (creators ↔ software vendors ↔ educators), attached commerce modes (subscriptions, memberships, courses, coaching, physical), media delivery form (files ↔ streaming), and discovery posture (marketplace ↔ direct-only). Its historical pole (button-code digital-goods carts) satisfies the same spine without storefront, MoR, or buyer accounts — the defining core is small by design.

The center of gravity — what the purchase converts into — is a **delivered file/key**, which separates it from every sibling: goods (Creator Storefront), structured standing access (Course Commerce), cycle-maintained entitlement (Subscription/Membership), tracked service (Coaching), venue access (Paid Community), nothing-owed (Tip Platform).
