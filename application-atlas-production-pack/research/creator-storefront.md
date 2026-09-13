# Research Notes — Creator Storefront

Directory location: §27 Media, Entertainment, Creator & Culture (siblings: Link-in-Bio Platform, Digital Product Commerce Platform, Paid Community Platform, Fan Membership Platform, Creator Subscription Platform, Creator Tip Platform, Creator Course Commerce Platform [processed], Coaching Commerce Platform [processed], Creator Affiliate Dashboard [processed], Creator Revenue Management [processed]; distant family: E-commerce Platform / Online Store Builder §05.01, Marketplace §05.02, Print-on-demand Commerce Platform §05.21, Digital Goods Store §05.22)

Research date: 2026-09-07

## Research Goal

Understand what a "Creator Storefront" really is in the market: what the storefront object is, what goods are sold, who operates which part of the commerce machinery (production, payments, taxes, support, fulfillment), how buyers arrive, how earnings reach the seller, and where the boundary sits against the §27 creator-economy siblings and the §05 commerce Types (store builder, marketplace, POD, digital goods).

## Initial Boundary (hypothesis before research)

- Working hypothesis: a Creator Storefront is a selling surface bound to an individual creator's public identity, where fans buy goods the creator offers (typically merchandise + digital products), with the platform operating most of the commerce machinery.
- Expected confusions:
  - Online Store Builder / E-commerce Platform (§05.01) — same commerce loop, different seller and machinery posture
  - Marketplace (§05.02) — platform-owned catalog vs seller-branded shop
  - Digital Product Commerce Platform (§27 sibling, unprocessed) — file-only specialization?
  - Link-in-Bio Platform (§27) — link aggregation vs commerce
  - Print-on-demand Commerce Platform (§05.21) — production machinery vs selling surface
  - Creator Affiliate Dashboard (§27, processed) — own goods vs commissions on others' goods
  - Creator Subscription / Fan Membership / Tip (§27) — purchase converts into access or support, not goods
  - Creator Revenue Management (§27, processed) — earning mechanism vs money layer above it
- Known cluster seam test from prior passes: **what a purchase converts into** (coaching → tracked human-service engagement; course → curriculum access; storefront → goods/downloads; community/membership → venue access). Feature presence is explicitly NOT the seam.

## Research Questions

1. What do products in this space call themselves, and what is the storefront object in each?
2. What product/goods types can be sold (POD merch, self-sourced physical, digital files, memberships)?
3. Who does what: platform vs seller division of labor for production, payment processing, taxes, shipping, customer support?
4. How does the purchase flow work and what does a purchase convert into?
5. How do buyers arrive at the storefront (link-in-bio, social channels, YouTube/TikTok integrations, marketplace)?
6. What does the seller's dashboard contain (products, orders, payouts, analytics, promotions)?
7. What rules matter (payout thresholds/methods, verification, content/IP guidelines, account constraints)?
8. Where is the boundary vs store builder, marketplace, POD platform, digital-product commerce, link-in-bio, affiliate storefronts?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

1. **Fourthwall** — storefront-first creator commerce platform; POD catalog + self-sourced + digital + memberships; Merchant-of-Record posture; serves individual creators up to media brands/companies. (Primary; deep help center.)
2. **Bonfire** — campaign/cause-flavored merch storefront; limited-edition batch campaigns + always-on on-demand stores + fundraising; strong nonprofit posture. (Primary; help center reachable.)
3. **Big Cartel** — artist/maker shop builder; seller-operated payments/shipping/support; POD via third-party apps; the low-machinery boundary pole. (Primary; help center reachable.)
4. **Spring (Teespring)** — legacy creator merch platform. (Secondary; official docs not directly reachable this pass — evidence via Fourthwall's official comparison page, Tier 2.)
5. **Stan Store** — link-in-bio-posture creator store. (Tertiary; JS-gated site — only the page title "Stan - Your Creator Store" directly observed.)

Unreachable this pass (recorded as limitations, not silently substituted from memory): Gumroad (timeouts ×2), Ko-fi (403 + help-center timeout), Sellfy (403), Payhip (403), Bandcamp (transport error), Stan help center (transport error).

## Sources

Tier 1 (official operational documentation):

- Fourthwall Help Center: https://help.fourthwall.com/ (root; /category/setting-up-your-shop; /category/design-my-storefront; /category/get-started; /category/payments-and-pricing; /category/getting-started-with-memberships; articles: *Create new product listings*, *How you get paid*, *Handle support inquiries*)
- Bonfire Help Center: https://help.bonfire.com/en/ (root; Sellers collection; articles: *Create a Store*, *How Payouts Work*)
- Big Cartel Help Center: https://www.bigcartel.com/resources/help (topic index)

Tier 2 (official product/positioning pages):

- Fourthwall: https://fourthwall.com/ (homepage), https://fourthwall.com/compare/fourthwall-vs-shopify, https://fourthwall.com/compare/fourthwall-vs-spring-teespring, https://fourthwall.com/features/digital-products
- Bonfire: https://bonfire.com/ (homepage)
- Big Cartel: https://www.bigcartel.com/ (homepage), https://www.bigcartel.com/product/how-it-works
- Stan Store: https://www.stan.store/ (page title only — JS-gated)

Evidence layers used below: **A** = directly observed on an official source for a specific product; **B** = cross-product commonality across the researched sample; **C** = canonical inference from comparison + boundary reasoning.

## Product A — Fourthwall

### Key observations (evidence layer A unless noted)

- Self-description: "One platform for custom products and branded shops"; "Trusted by 500,000+ creators and companies"; example shops span individual creators (MKBHD, Harry Mack) to companies/media brands (SanDisk, Vox, NY Magazine, Smithsonian). Positioning: "You bring the ideas. We'll handle the rest."
- **Three product listing types** (help center, *Create new product listings*):
  1. *Design something new* — print-on-demand from the Fourthwall catalog (hundreds of blanks: apparel, accessories, home goods); creator applies artwork in a design editor; Fourthwall handles manufacturing, fulfillment, shipping.
  2. *Sell something I have* (self-sourced) — creator enters title/description/price/images/variants manually; Fourthwall collects payment and passes orders to the creator for fulfillment.
  3. *Sell digital product* — downloadable file (PDFs, ebooks, digital art, presets, templates, audio); customers download instantly after purchase; no shipping.
- **Storefront = a full branded website**: site designer with themes, global colors/fonts, header/footer/menus, homepage layout sections (image banners, collection lists, video/YouTube feed sections), custom pages (About, press kit, FAQ), custom HTML/CSS/Liquid, product/collection page templates, checkout page customization (customer messages, donations, email consent), password-protected shops, QR code generation, preview-before-publish, custom domain connection.
- **Merchant of Record**: Fourthwall operates as MoR — handles payment processing (cards, PayPal, Apple/Google Pay, Amazon Pay, local methods), sales tax (nexus registration, collecting, remitting to US states and other countries). (Compare-vs-Shopify page FAQ.)
- **Payouts** (*How you get paid*): automatic monthly payouts via Stripe Connect (ACH/wire/debit card); balance over $25 paid by the 3rd business day of the following month; payout history with Pending/Paid/Failed statuses; manual payout requests for balances under $25 (one per month, Stripe only); unclaimed balances never expire; account closure blocked while balance outstanding; payout invoices downloadable; team members may lack permission to payout settings (account owner vs team roles exist).
- **Support division** (*Handle support inquiries*): every shop gets an automatic support email (routes through Fourthwall's system; updates to match custom domain). Fourthwall handles support for catalog-fulfilled products (quality, sizing, order status, changes/cancellations, refunds/replacements under a quality guarantee, processed through the shop balance). Creator handles: self-fulfilled products, digital-product refunds (processed by creator in Orders), and orders from external channels (TikTok Shop — support must start in TikTok's seller dashboard).
- **Memberships** as a sibling module: tiers, tier permissions over posts/pages/perks, members-only locked pages, posts (text/image/video/audio/poll/livestream), DMs, locked (PPV) messages, free tiers, trials/promos, Twitch gifting integration, Spotify members-only audio, branded mobile app, cancellation flows/exit surveys, Patreon migration tooling. (Category listing observed; article bodies not individually fetched.)
- **Sales channels**: own site; TikTok Shop integration; YouTube Shopping product shelf; Instagram/Facebook shops; stream alerts (purchase events on Twitch/YouTube); integrations (Streamlabs, Discord, Mailchimp, Klaviyo, Zapier, Linktree, beehiiv…); "Don't need a storefront? Skip it and order your products immediately" (shop optional).
- **Pricing posture** (FAQ): no monthly fees; catalog products carry a publicly listed flat production cost deducted from the seller-set price; self-sourced 0% fee; digital 5%; memberships 5%; card processing ~2.9% + $0.30 (US). (Product-specific numbers — L3.)
- **Data ownership positioning**: "your fans and your data belongs to you, not the marketplace" — anti-marketplace framing; APIs/webhooks; full data ownership claim.
- **Site verification before first payout**: Fourthwall reviews every new shop before the first payout (help-topic title observed).
- AI assistant ("Eli") for shop/product/promotion tasks; MCP server; docs.fourthwall.com for developers. (Era-current extras — L3.)

## Product B — Bonfire

### Key observations (evidence layer A unless noted)

- Self-description: "The easy way to sell merch online"; "Let Bonfire take care of printing, shipping, and customer support"; "100% risk-free • No inventory"; since 2012; trusted by "artists, creators, schools, political movements, fundraisers, small businesses, churches, nonprofits".
- **Campaign is the core selling object**: sellers design products on Bonfire's catalog blanks and sell through *campaigns* — either limited-edition **batch campaigns** (orders print after the batch end date) or **print-on-demand campaigns** (orders print the next business day). Campaign lifecycle: draft → scheduled launch → live → ended; duplicate/revert/delete; promotions; product groups; samples; campaign page customization; connect a campaign to an event.
- **Store = container of campaigns**: one store per account; campaigns added manually ("full control over which ones you want to show"); store must contain ≥1 campaign to publish; store customization + settings; "Add a Store to Linktree" article (link-in-bio distribution). (Tier 1, *Create a Store*.)
- **Pro tier**: "Open a fully branded custom merch store in minutes. No inventory or integrations needed" — subscription-based commerce solution (Bonfire vs Bonfire Pro collection).
- **Payouts** (*How Payouts Work*): typically PayPal; request-based (seller requests from dashboard Payouts page, "Available" tab); available 1–3 business days after orders are sent to print; $5 minimum for PayPal; single payouts over $10,000 cannot go via PayPal; check ($100 min) and ACH ($1,000 min) as restricted alternatives; tips/donations included in payout; Bonfire covers payout fees. Nonprofits paid via donation-processing partner (Change); Giving Campaigns route payouts to beneficiary organizations; "Send Payouts to a Beneficiary".
- **Money objects**: base cost per product, seller-set profit margins, additional contributions (tips/donations) with a processing fee, sales tax handled by Bonfire, seller pays income tax on earnings.
- **Supporter machinery**: supporter lists, supporter contact information, group shipping, shipping options.
- **Distribution/integrations**: YouTube Merch Shelf, Instagram, Tiltify, GoFundMe integrations; Bonfire marketplace ("Shop the marketplace") exists alongside seller stores.
- **Governance**: Community Guidelines, Content Guidelines, Verified Creator Guidelines, Ownership of Artwork, reporting violations, DMCA/trademark takedown. (Footer + help-topic titles.)

## Product C — Big Cartel

### Key observations (evidence layer A unless noted)

- Self-description: "Free, Easy Online Stores for Artists & Small Businesses"; "HUSTLE WITHOUT THE HASSLE"; audience: entrepreneurs, bands, printmakers, jewelry makers, designers, ceramicists, painters, illustrators, photographers, publishers; "WHERE DIY GOES PRO"; compares itself against Etsy, Shopify, Wix, Squarespace.
- **Four-step setup**: choose a template → add products (or import from Shopify/Etsy/Squarespace) → set up the store (shipping, payments, design) → promote ("Tell the world!").
- **Seller-operated machinery**: seller connects their own online payment processors (help topic *Accept Online Payments* / *Set up Checkout*; homepage: "Cards, wallets, Venmo, PayPal & more"); seller configures shipping (manual rates via shipping profiles, or automatic rates for US-based sellers); seller manages and ships orders (order notifications, order details, packing slips, bulk edit); automatic taxes available for US/PR USD orders as a feature; EU order-cancellation-request handling article (compliance surface).
- **Goods types**: physical goods, digital goods (*Selling Digital Products on Big Cartel*), print-on-demand via apps (Printful, Printify articles), in-person selling via the mobile app (scan-and-pay, hardware/tap-to-pay), scheduled product drops, product variants/variant groups, discounts, abandoned-cart recovery, shareable carts.
- **Storefront**: template-based shop designer (themes with preset colors/fonts or bespoke customization), custom pages, custom domain, maintenance mode, integration code.
- **Dashboard**: order & visitor stats, conversion rates & trends, product & category stats.
- **Plans**: free plan to start; paid tiers (Platinum $15/mo, Diamond $30/mo per homepage pricing block). (Product-specific — L3.)
- FAQ "Does Big Cartel make the products I sell?" — implies the seller makes/sources products (platform does not manufacture). (Title-level evidence.)

## Product D — Spring (Teespring) — Tier 2 only

### Key observations (evidence layer A for the comparison page, vendor-claimed)

- Evidence limited to Fourthwall's official comparison page (Fourthwall-vs-Spring). Vendor-claimed contrasts: Spring POD catalog ~180+ products (vs Fourthwall 330+); fulfillment centers US/EU/AUS/IN; no digital products; no memberships; no custom domain (per the comparison table); no self-sourced products; YouTube merch shelf heritage.
- Spring's own docs were not reachable this pass; no Spring-specific workflow claims are made beyond this comparison table.

## Product E — Stan Store — title only

- Page title "Stan - Your Creator Store" directly observed (JS-gated SPA; no content rendered). Confirms the market uses "creator store" language for a link-in-bio-posture commerce product. No structural claims.

## Cross-product Comparison

| Dimension | Fourthwall | Bonfire | Big Cartel | Spring (T2) | Stan (title only) |
|---|---|---|---|---|---|
| Self-description | platform for custom products + branded shops | easy way to sell merch online (campaign/cause) | online stores for artists & small businesses | creator merch platform (per comparison) | "Your Creator Store" |
| Storefront object | branded shop website (site designer, themes, pages, checkout customization) | store = container of campaigns; campaign pages | template-based shop | store page | store |
| Goods types | POD catalog + self-sourced physical + digital files + memberships | POD merch (batch or on-demand campaigns) | physical + digital + POD via apps | POD merch | (unverified) |
| Production/fulfillment | platform (POD) / seller (self-sourced) | platform | seller / POD provider via app | platform | n/a |
| Payment processing | platform as Merchant of Record | platform | seller connects own processors; platform hosts checkout | platform | n/a |
| Taxes | platform handles sales tax (MoR) | platform handles sales tax; seller pays income tax | seller-level (automatic US taxes as a feature) | platform (per comparison posture) | n/a |
| Customer support | platform handles catalog-fulfilled; seller handles self-fulfilled/digital/external-channel | platform ("printing, shipping, and customer support") | seller | platform | n/a |
| Payout model | automatic monthly via Stripe Connect; minimum threshold; payout history statuses | request-based via PayPal; minimum threshold; batch-gated availability | payments go directly to seller's connected processors | platform payouts | n/a |
| Sales channels | own site + TikTok Shop + YouTube shelf + IG/FB + stream alerts | store + campaign pages + YouTube Merch Shelf + Instagram + marketplace | shop + in-person app + social channels | store page + YouTube shelf | link-in-bio |
| Buyer arrival | link in bio / social / video-platform integrations | campaign sharing + marketplace + YouTube | social, SEO, in-person, imports | social | social bio |
| Distinct flavor | full machinery bundle + memberships + data ownership | campaign/batch drops + fundraising/cause + nonprofit rails | artist shop builder, seller-operated | legacy creator merch | bio-first store |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

The smallest structure without which the product stops being recognizable as a Creator Storefront:

```text
Seller-owned branded storefront surface
  (the shop is the seller's own branded property — own name/URL/branding —
   not a listing inside a platform-owned catalog)
└── Seller-defined product catalog
    (the seller decides what goods exist — designs on platform blanks,
     self-made/self-sourced goods, digital files — and sets prices)
    └── Platform-hosted purchase flow
        (browse → cart → checkout → payment happens on the platform's
         storefront/checkout, however payment processing is wired)
        └── Seller earnings
            (the platform tracks sales and delivers the money to the
             seller — payout to the seller's account, or pass-through
             to the seller's connected processors)
```

Four invariants. Remove any one and it becomes a different Type:

- Remove the seller-owned branded surface (buyers browse a platform catalog) → Marketplace.
- Remove the seller-defined catalog (the seller curates other parties' products for commission) → affiliate storefront (Creator Affiliate Dashboard territory).
- Remove the platform-hosted purchase flow (links out to elsewhere) → Link-in-Bio Platform.
- Remove seller earnings (support/donation without a goods transaction) → tip/support platforms.

Deliberately NOT in L0 (modern common, not definitional — historical check below): print-on-demand production networks, Merchant-of-Record payment processing, memberships, social-channel sales integrations, AI assistants, mobile apps, custom domains, analytics.

### L1 — Common Mature Structure

Present across the researched sample (evidence layer B):

- **Design-on-blank product creation** — a catalog of blank products the seller applies artwork to (Fourthwall catalog; Bonfire catalog; Big Cartel via Printful/Printify apps). The dominant goods model for merch.
- **Digital product delivery** — file upload, instant download after purchase (Fourthwall direct; Big Cartel digital products; the digital-only specialization is the Digital Product Commerce Platform sibling).
- **Order management dashboard** — order list with statuses, refunds, order-level actions (Fourthwall Orders + refund split by product type; Bonfire dashboard; Big Cartel order management).
- **Earnings/payout machinery** — balance, payout method, minimum thresholds, payout history/status, tax documentation (all sampled products; mechanics differ — see L2/L3).
- **Storefront design surface** — themes/templates, branding, custom pages, custom domain (all sampled).
- **Promotions** — discount/promo codes, limited-time drops (all sampled; Bonfire's batch campaign is the drop mechanism itself).
- **Analytics** — sales, top products, visitors/conversion (all sampled).
- **Off-storefront sales channels** — YouTube product shelves, TikTok Shop, Instagram/Facebook shops, stream alerts, link-in-bio placement (Fourthwall, Bonfire; Big Cartel social selling + in-person).
- **Platform-handled customer support for platform-fulfilled goods** (Fourthwall explicit split; Bonfire claims support handling; Big Cartel is the seller-support pole).
- **Content/IP governance** — community/content guidelines, artwork ownership, takedown (Bonfire explicit; Fourthwall acceptable-use policy).

### L2 — Variant / Optional Structure

- **Machinery posture spectrum** — platform-operated machinery (production + MoR payments + taxes + support: Fourthwall, Bonfire, Spring) ↔ seller-operated machinery (seller connects processors, sets shipping, does support: Big Cartel). The seller-operated pole shades into Online Store Builder; the platform-operated pole is the distinct creator-commerce species.
- **Selling cadence** — always-on on-demand store (Fourthwall, Big Cartel, Bonfire Pro stores) vs limited-time batch campaigns/drops (Bonfire campaigns; Big Cartel scheduled drops).
- **Cause/fundraising posture** — fundraiser campaigns, beneficiary payouts, nonprofit donation rails (Bonfire; absent in the others sampled).
- **Memberships/community attached to the shop** (Fourthwall; sibling Types own this structure elsewhere).
- **In-person selling** (Big Cartel app + hardware).
- **Link-in-bio acquisition posture** (Stan; Bonfire's Linktree article; Fourthwall Linktree integration) — the storefront as the destination of a bio link.
- **Audience scale posture** — individual creators ↔ media brands/companies running merch shops on the same machinery (Fourthwall's example shops).
- **Curated/affiliate storefronts** — shop surfaces whose catalog is other parties' products (LTK, Amazon Influencer) — assigned to the Creator Affiliate Dashboard Type by that pass; recorded here as a naming overlap, not part of this Type's core.

### L3 — Vendor-specific (research notes only)

- Fourthwall: Stripe Connect monthly payouts with $25 minimum (3rd business day); bill.com BRL $35 minimum; site verification before first payout; automatic per-shop support email; quality guarantee with refunds through shop balance; 5% digital/membership fee, 0% self-sourced, catalog flat cost; Eli AI assistant; MCP; branded mobile apps; thank-you videos; Patreon migration; password-protected shops; team roles/permissions.
- Bonfire: one store per account; campaign batches with print-after-batch-end; PayPal payouts $5 minimum, >$10,000 single payouts not via PayPal; check $100 / ACH $1,000 minimums; Change for nonprofit donation processing; Giving Campaigns; Tiltify/GoFundMe integrations; Bonfire Pro subscription tier.
- Big Cartel: Gold free plan / Platinum $15 / Diamond $30; seller-connected processors (Stripe/PayPal/Venmo); automatic US taxes; EU cancellation-request tooling; maintenance mode; in-person tap-to-pay hardware; Printful/Printify apps; import from Shopify/Etsy/Squarespace.
- Spring: ~180+ product catalog; fulfillment US/EU/AUS/IN; no digital/memberships/custom domain (per Fourthwall's comparison table — vendor-claimed).

## Rejected Findings (considered and not promoted)

- **"Creator Storefront = POD merch shop"** — rejected: digital files are a first-class listing type in multiple products (Fourthwall direct; Big Cartel), and self-sourced physical goods exist (Fourthwall). POD is the dominant goods model, not the definition.
- **"The platform must be Merchant of Record"** — rejected: Big Cartel sellers connect their own processors while the checkout remains platform-hosted. MoR is the dominant modern posture (L1/L2), not the invariant.
- **"Memberships are part of the Type"** — rejected: only some products ship them (Fourthwall yes; Bonfire/Big Cartel no in the sampled evidence). Feature presence is not the seam (consistent with the cluster's established test).
- **"The storefront must be a full website"** — rejected: Bonfire's store is a campaign container; Stan's is a bio-embedded store. Surface depth varies; the branded-seller-owned-surface invariant is what holds.
- **"Buyers must come from the creator's audience"** — rejected as definitional: Big Cartel sellers use SEO and in-person sales; Bonfire has a marketplace surface. Audience-native traffic is the typical posture (positioning), not an invariant.
- **"Creator Storefront includes affiliate storefronts (Amazon Influencer/LTK-style)"** — rejected: those surfaces' defining objects are commission records (per the Creator Affiliate Dashboard pass); the name overlap is recorded as a boundary note.

## Boundary Findings

- **vs Online Store Builder / E-commerce Platform (§05.01)** — the sharpest seam. Shared: product → cart → checkout → payment → fulfillment → earnings loop; themes; custom domains; discounts; analytics. Different: (a) who the seller is and what the goods are — a creator/artist monetizing an audience with design/IP-driven goods vs a business selling inventory; (b) machinery posture — creator platforms bundle production (POD), payment processing (often MoR), taxes, and support so the seller's job reduces to design/price/promote, while store builders hand the seller raw machinery; (c) traffic model — audience-native (bio links, video-platform shelves) vs the store's own marketing/SEO. Big Cartel is the boundary pole: artist-focused store builder with seller-operated machinery — structurally a store builder, rhetorically a creator shop. Diagnostic: remove the bundled machinery and audience-native posture → Online Store Builder; add them → Creator Storefront.
- **vs Marketplace (§05.02)** — marketplace owns the catalog, the brand, and discovery; sellers hold listings. Here the shop is seller-branded property. Bonfire and Redbubble-style platforms have marketplace surfaces alongside stores; the store remains the seller's branded surface. Diagnostic: platform brand fronts the shopping experience and owns the catalog → Marketplace.
- **vs Digital Product Commerce Platform (§27 sibling, unprocessed)** — fulfillment-structure test (cluster-established): a storefront purchase converts into goods (manufactured merch, shipped self-sourced goods, or a file download) with no curriculum structure, no service engagement, no venue access. The digital-product platform is the file-only specialization of the same loop. This Type spans physical + digital; the sibling is digital-only. Flag for joint review when that leaf is processed.
- **vs Link-in-Bio Platform (§27, unprocessed)** — link aggregation vs commerce. Stan straddles (a "creator store" delivered in a bio-link posture). Diagnostic: remove products/checkout → link-in-bio; keep them → storefront with a bio-link acquisition surface.
- **vs Print-on-demand Commerce Platform (§05.21, unprocessed)** — POD platform = the production/fulfillment machinery and its supply network; creator storefront = the seller-facing selling surface that consumes that machinery (natively in Fourthwall/Bonfire, via apps in Big Cartel). One product can span both (Bonfire prints its own catalog). Diagnostic: remove the seller-facing branded shop → POD platform; remove the production network → pure storefront.
- **vs Creator Affiliate Dashboard (§27, processed)** — storefront sells the seller's own goods; the dashboard earns commissions on other parties' goods. That pass's own test: "remove the commission ledger and it becomes a storefront." Curated storefronts (LTK, Amazon Influencer) sit on the affiliate side of the seam.
- **vs Creator Subscription / Fan Membership / Paid Community (§27)** — purchase converts into access to a venue/stream/relationship, not goods. Fourthwall ships memberships as a sibling module inside a storefront account — feature presence is not the seam (cluster-established test confirmed from this side).
- **vs Creator Tip Platform (§27)** — tips/donations are support, not a goods transaction; Bonfire's "additional contributions" ride on top of goods sales rather than defining the Type.
- **vs Creator Revenue Management (§27, processed)** — the storefront is an earning mechanism (fan-facing transaction machinery); revenue management is the money layer above mechanisms (source-attributed income records, consolidated payouts). One product can span both; objects differ (product/order vs income record).
- **"去掉什么就变成另一个 Type" tests**:
  - Remove the seller-branded surface (platform catalog fronts) → Marketplace.
  - Remove the seller-defined catalog (curate others' goods) → affiliate storefront / Creator Affiliate Dashboard.
  - Remove the platform-hosted checkout → Link-in-Bio Platform.
  - Remove goods fulfillment entirely (access instead of goods) → Membership/Subscription/Community Types.
  - Remove the bundled machinery + audience posture → Online Store Builder.
  - Remove the selling surface, keep production → Print-on-demand Commerce Platform.

### Taxonomy observation (for STATUS.md Boundary Issues)

The Type is real and distinct at the platform-machinery pole (Fourthwall/Bonfire/Spring/Stan: bundled production + payments + support + audience-native distribution), but the market shows a continuum into Online Store Builder at the seller-ops pole (Big Cartel: artist-focused store builder). The leaf is documented as an independent Type on the four-invariant core; the store-builder seam is recorded as a spectrum with a named diagnostic, for joint review when §05.01 leaves are processed. Secondary naming overlap: "creator storefront" in market language also covers affiliate-curated shop surfaces (assigned to Creator Affiliate Dashboard by that pass).

## Historical / Market-Sample Check

- Older/regional equivalents fit the four-invariant core: artist shops on Big Cartel (seller-era, 2000s/2010s), campaign merch on Spring/Teespring (2010s), Bandcamp-style musician storefronts (artist-branded pages selling music/merch — not directly fetchable this pass, checked conceptually), Bonfire (2012, cause merch). None of these require MoR payments, POD networks, memberships, TikTok/YouTube integrations, or AI assistants to qualify.
- The L0 therefore does not over-fit the current dominant implementation (MoR + POD + social integrations); those sit in L1/L2.
- Counter-pole check: Etsy (marketplace) and Shopify (store builder) fail the L0 on the intended reading (platform-owned catalog; raw machinery without the creator-commerce bundle) — consistent with the boundary findings.

## Uncertainties

1. **Digital-products-first pole under-sampled** — Gumroad, Ko-fi, Sellfy, Payhip all unreachable (timeouts/403). Digital-goods mechanics are evidenced via Fourthwall (help + feature page) and Big Cartel's digital-products documentation; the checkout/product-centric digital pole is inferred from the cluster's prior passes (course commerce) rather than directly observed here.
2. **Stan Store** — title-only evidence (JS-gated); the link-in-bio store posture is weakly evidenced. No structural claims made.
3. **Spring** — official docs not directly reachable; all Spring observations come from Fourthwall's comparison page (vendor-claimed, Tier 2). No Spring workflow claims.
4. **Bandcamp** — transport error; the historical musician-storefront check is conceptual, not source-backed.
5. **Memberships depth** — Fourthwall membership article bodies not individually fetched; membership structure recorded from category/article listings only.
6. **Precise numbers are product-specific** — payout minimums, fees, and plan prices observed for specific products are kept in L3/research notes and are not asserted as Type-wide behavior.
7. **Buyer-side experience** — research focused on the seller-facing application (consistent with the leaf's position as a seller-side Type); buyer checkout surfaces were observed only indirectly (checkout customization, buyer help collections exist).

## Final Synthesis

The Creator Storefront is the seller-side commerce application of the creator economy: an individual creator or small brand operates a **branded selling surface they own** (not a listing in a shared catalog), fills it with a **catalog they define** — designs applied to platform blanks, self-made/self-sourced goods, and digital files — and lets a **platform-hosted purchase flow** turn fan demand into **seller earnings**. Around this four-part core, mature products bundle the machinery the seller would otherwise operate: print-on-demand production networks, payment processing (often as Merchant of Record) with sales-tax handling, split customer support, payout machinery with thresholds and tax documentation, order dashboards, promotions/drops, analytics, and off-storefront sales channels (video-platform shelves, social shops, stream alerts, bio links). The market realizes the Type on a spectrum of machinery posture — from fully bundled creator-commerce platforms (Fourthwall, Bonfire, Spring, Stan) to artist-operated shop builders (Big Cartel) — and on a spectrum of cadence — always-on stores vs limited-time campaign drops — with cause/fundraising and memberships as common attached postures. The Type is distinct from Marketplace (platform-owned catalog), from Online Store Builder (raw machinery, business sellers), from Digital Product Commerce (file-only specialization), and from the affiliate/membership/tip/revenue siblings by the established cluster test: what a purchase converts into, and whose goods are being sold.
