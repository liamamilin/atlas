# Research Notes — Digital Goods Store

## Research Goal

Determine what a "Digital Goods Store" is as an Application Type, given two prior passes in the same name-space:

- `digital-product-commerce-platform` (§27, processed 2026-09-07) — seller-side commerce platform for selling digital products
- `digital-download-commerce-platform` (§05.22 sibling, processed 2026-09-08) — same seller-side Type; alias pair confirmed; left a FORWARD FLAG: "the three-leaf name-space (digital goods store / digital download commerce platform / §27 digital product commerce platform) likely reduces to two structures — the buyer-facing VENUE (store/marketplace for digital goods) vs the seller-side operating platform (this Type); the digital-goods-store pass should test the venue reading (first-party retail storefront or multi-vendor marketplace for digital goods) against the seller-tooling reading before assuming a third distinct Type"

Task of this pass: test the venue reading against the seller-tooling reading; if the venue reading holds, define it with a minimal core and hold all adjacent boundaries.

## Initial Boundary Hypothesis

- Core use hypothesis: a buyer-facing store where people browse, discover, and purchase digital goods (games, apps, music, e-books, video, software, creative assets), with purchases converting into account-held entitlements delivered digitally.
- Users hypothesis: buyers as primary users; sellers (publishers/authors/developers) and the operator's staff as a secondary population.
- Nearest neighbors: Digital Download Commerce Platform / Digital Product Commerce Platform (seller-side tooling — duplication risk), Online Marketplace / Multi-vendor Marketplace (generic goods venue — subsumption risk), E-commerce Platform / Online Store Builder (§05.01 store-building tools), Video/Music Streaming Platforms (§27 — subscription access, not per-item purchase), Creator Storefront (§27).
- Unknowns: whether the market realizes a distinct buyer-facing venue population; whether "purchase → entitlement" is the defining transaction; where the line to streaming subscription sits; whether app stores belong in this Type.

## Research Questions

1. What does a purchase convert into — a shipped good, a subscription, or an entitlement/license? How is that recorded and held?
2. What does the storefront surface look like (browse, search, curation, product pages)?
3. How is delivery performed (download, key, client/launcher, streaming access)? Is there standing re-access?
4. What seller models exist (operator-as-retailer, multi-vendor marketplace, platform-native store)? Who is merchant of record?
5. What rules govern the transaction (refunds, regional pricing, licenses, review gates)?
6. Where is the boundary to the seller-side operating platform (sibling Type), to generic marketplaces, and to streaming platforms?

## Representative Products

| Product | Store model | Why sampled | Evidence status |
|---|---|---|---|
| Steam (Valve) | operator retail storefront, third-party publishers, client-based delivery | largest PC game store; explicit entitlement model | Tier 1: Refund Policy + Subscriber Agreement (fetched); store surface directly observed |
| Envato Market | multi-vendor marketplace for digital creative assets | author-gated asset marketplace; license/support machinery | Tier 1: Author Help Center + Market Support Help Center (both fetched) |
| Apple App Store | platform-native ecosystem store | OS-owner store; review gate; in-app purchase commerce | Tier 2: developer-facing App Store page (fetched); consumer side not fetched |
| itch.io | open indie marketplace; pay-what-you-want | different philosophy (openness) | UNREACHABLE ×3 — named anchor only |
| GOG.com | curated DRM-free game store | different philosophy (DRM-free retail) | UNREACHABLE ×1 — named anchor only |
| Bandcamp | artist-storefront music store | music domain; artist-first economics | UNREACHABLE ×2 — named anchor only |

Sample spans three store models (retail storefront / asset marketplace / platform-native store), three goods domains (games, creative assets, apps), three seller levels (game publishers, professional asset authors, solo-to-enterprise developers), different philosophies (open retail, gated marketplace, curated ecosystem).

## Sources

Fetched 2026-09-08:

- Steam Refund Policy — https://store.steampowered.com/steam_refunds/ (Tier 1; page states "Last updated 23 April, 2024")
- Steam Subscriber Agreement — https://store.steampowered.com/subscriber_agreement/ (Tier 1)
- Steam store homepage — https://store.steampowered.com/ (Tier 2 surface observation; nav: Store Home, Discovery Queue, Wishlist, Points Shop, News, Charts, Community, Support; "Recommended Based on the Games You Play"; "Your Wishlist"; "DLC for Your Games"; specials/deals; gift cards; "Install Steam")
- Envato Author Support Help Center — https://help.author.envato.com/hc/en-us (Tier 1: Becoming an Author, Uploading Items, Pricing Items, Quality requirements, Understanding Licenses, Earnings, Tax)
- Envato Market Support Help Center — https://help.market.envato.com/hc/en-us (Tier 1: Buying, Item Support, Your Statement & Documents, purchase code, invoice, Tax & Compliance; linked policy pages: customer refunds, author refunds, item support, licenses, Market API, affiliate program)
- Apple App Store developer page — https://developer.apple.com/app-store/ (Tier 2: distribution, discovery, commerce, analytics, trust sections)

Unreachable (network limitation; used only as named market anchors, no claims from them):

- itch.io — docs/creators/pricing, docs/general/faq, /about all timed out (3 attempts, then dropped)
- Bandcamp — bandcamp.com/about timed out; get.bandcamp.help/hc/en-us returned 404
- GOG — support.gog.com/hc/en-us timed out
- Google Play refunds article — support.google.com timed out

Prior passes used only for the name-space seam (not for this Type's structure): STATUS.md entries for `digital-product-commerce-platform` (2026-09-07) and `digital-download-commerce-platform` (2026-09-08).

## Product Observations

### Steam — evidence layer A unless noted

Storefront surface (direct observation of store homepage):

- Standing buyer-facing surface: Store Home, Discovery Queue, Wishlist, Points Shop, News, Charts; tag/category browsing; deal surfaces ("Discounts & Events", "Specials", publisher sales with percent-off pricing); personalized recommendations ("Recommended Based on the Games You Play"); "Your Wishlist"; "DLC for Your Games"; gift cards; "Install Steam" client call-to-action.
- Community is a sibling surface (Discussions, Workshop, Market, Broadcasts) including a user-to-user item market (Community Market).

Purchase = entitlement ("Subscription"), not goods (Subscriber Agreement, Tier 1):

- The buyer is a "Subscriber"; the account holds "contact information, billing information, Account history and Subscriptions".
- "'Subscriptions' … the rights to access and/or use any Content and Services accessible through Steam. Each Subscription allows you to access particular Content and Services."
- "The Content and Services are licensed, not sold. Your license confers no title or ownership in the Content and Services."
- Contract formation distinguishes digital from physical inside one document: for Content and Services the contract is concluded "by confirming the transaction and making the Content and Services available to you"; for Hardware only "when we dispatch the Hardware … Dispatch Confirmation … separate contract of sale". Direct in-document evidence that the digital transaction's fulfillment obligation is making the goods accessible, not shipping.
- Operator as merchant of record: "any transactions for Subscriptions you make on Steam are being made from Valve" (except subscriber-to-subscriber trades in Subscription Marketplaces).
- Access may be tied to the client: "you must have a Steam Account and you may be required to be running the Steam client and maintaining a connection to the Internet."
- Personal, non-commercial license; account and Subscriptions non-transferable except as expressly permitted.

Payment machinery:

- Steam Wallet: prepaid account balance ("neither a bank account nor any kind of payment instrument") used to order Subscriptions; non-refundable, no cash value; limits set by Valve (a US$2,000-per-24h aggregate cap and a 6-month expiry for Japanese subscribers are stated — product-specific, L3).
- Recurring Payment Subscriptions exist (recurring access billing).
- Regional pricing/geography: buyers agree not to use IP proxying "to circumvent geographical restrictions on game content, to order or purchase at pricing not applicable to your geography".

Key/activation path (Tier 1):

- Retail boxed product and authorized resellers: "The 'CD-Key' or 'Product Key' accompanying such versions is used to activate your Subscription." Keys from third parties outside Steam sit outside Valve's refund obligations (Refund Policy: "Valve cannot provide refunds for purchases made outside of Steam (for example, CD keys …)").

Refund policy (Tier 1; product-specific terms):

- Refunds "for nearly any purchase … for any reason" within a return period (two weeks) and, for games, under two hours of playtime; refund to wallet or original payment method within a week of approval.
- Scope: DLC under same windows with "not consumed, modified or transferred" conditions; in-game purchases 48h for Valve-developed games, opt-in for third-party; pre-purchases (window starts at release); wallet funds; renewable subscriptions if unused; hardware under separate policy; bundles if aggregate playtime under the limit; unredeemed gifts (redeemed via recipient); video content NOT refundable; VAC-banned games lose refund right; EU right of withdrawal; anti-abuse clause.
- The numbers are Steam's own; the transferable structure is "self-service, policy-governed refund loop with usage-conditioned eligibility".

Marketplace-internal machinery:

- "Subscription Marketplaces" (Steam Community Market, Steam Trading): subscribers trade license rights to virtual items; Valve may charge transaction fees, collects transaction taxes, transfers Subscriptions between accounts; transfers outside Steam are not recognized.
- Steam Workshop: user-generated content attached to store products; in some categories users "may be able to interact with, download or purchase the Workshop Contribution"; revenue sharing defined per-app ("App-Specific Terms").
- User reviews are part of pre-purchase information the agreement points buyers to ("Subscription description, minimum technical requirements, and user reviews").
- Age gating: no Subscribers under 13; regional age restrictions.

### Envato Market — evidence layer A unless noted

Marketplace structure (two official help centers, author side + buyer side):

- Author help center framed as "selling your work on Envato's network of sites"; market help center framed as buyer support. The venue is a multi-vendor marketplace of independent authors.
- Author lifecycle categories: "What is Envato Author?", "Becoming an Author" (admission), "Uploading Items" (upload methods), "Manage and Update Items", "Pricing Items" (author-set pricing), "Quality requirements" (named category), "Understanding Licenses" (named category), "Earning with Envato" (earnings — commission mechanics), "Tax Information & Requirements", "Tax Forms".
  - Evidences: seller-authored supply, admission + quality gates, author pricing, per-item licensing, commission-based earnings, seller tax handling — all venue-provided machinery.
- Buyer side categories: "Buying", "Item Support", "Your Statement & Documents", "Account Settings", "Tax & Compliance".
  - "Purchase code" is a named common topic — each purchase yields an identifiable code (entitlement proof used for registration/support).
  - "Item Support" — author-provided support for items (policy page linked); buyer protection machinery beyond the file itself.
  - "Your Statement & Documents" + invoice topics — purchase history/invoices held per buyer account.
  - Refunds: separate "Customer refunds" and "Author refunds" policy pages exist (existence confirmed; terms not fetched — do not state their conditions).
  - Licenses: licenses page linked (Standard/Extended are market knowledge; terms not fetched — phrase generically).
- Market API and affiliate program exist (distribution/affiliate machinery).

Storefront surface: not directly fetched; help centers confirm a browse/buy venue structure. Storefront UI details (search, collections) not directly observed — venue-side browsing claims are evidence layer B (cross-venue structure), not a fetched storefront observation.

### Apple App Store — evidence layer A (developer-facing page, Tier 2)

Platform-native store:

- Distribution channel owned by the platform: "Distribute your apps and games on the App Store … whether you're a solo developer, or a part of an enterprise team", "availability in 175 regions and 50 languages".
- Admission gate: "every app, update, Apple In-App Purchase, and In-App Event on the App Store reviewed for safety, security, and privacy" — review-gated listing (contrast with open self-publish).
- Discovery/editorial: Featuring Nominations + editorial team; "charts and lists, and even personalized recommendations"; App Store search surfacing "In-App Events, developer stories, categories, collections, custom product pages"; app tags; custom product pages; product page optimization; marketing tools/badges.
- Commerce: Apple In-App Purchases — "from one-time purchases, to subscriptions"; "Purchases through the App Store use a customer's payment method on file"; "end-to-end payment processing handled" by the platform; "Support for more than 200 payment methods"; "international pricing tools"; auto-renewable subscriptions with "billing retry, grace periods, and retention messages"; offer types (introductory, promotional, win-back, offer codes).
- Seller side: App Store Connect analytics ("sales, subscription performance, referral sources, engagement"), benchmarks; App Review Guidelines + submission; App Store Small Business Program (commission-tier program).
- Trust/family: age ratings, Ask to Buy, Screen Time; "AppleCare is available to provide people with support related to their purchases, billing issues" — the platform handles buyer purchase support.
- Embedded in an ecosystem: OS-level surfaces (a Games app as destination), platform account as payment/identity substrate.

### Named anchors (no fetch — existence and general market position only)

- itch.io — open indie marketplace with self-publishing and pay-what-you-want pricing (no claims from its docs).
- GOG.com — curated DRM-free game store.
- Bandcamp — artist-operated storefronts inside a music store; per-item digital music purchases.
- Google Play — platform-native Android app store.

## Cross-product Comparison

| Dimension | Steam | Envato Market | Apple App Store |
|---|---|---|---|
| Primary user | consumers buying games/software | businesses/creators buying design assets | end users buying/installing apps + IAP |
| Store model | operator retail storefront; publishers list | multi-vendor marketplace; independent authors | platform-native store; sole app channel |
| Merchant of record | operator ("transactions ... made from Valve") | operator (authors earn via commission) | platform (end-to-end payment processing) |
| Catalog of digital goods | games, software, DLC, in-game items, video | templates, themes, code, media, assets | apps, games, in-app content |
| Product page | store page: description, technical requirements, reviews (per SSA) | item page with license + support terms | product page; custom product pages; optimization |
| Discovery | home, discovery queue, charts, tags, recommendations, wishlist | category/browse structure (help-center consistent; UI not observed) | editorial featuring, charts, personalized recommendations, search, events |
| Purchase to entitlement | "Subscription" = right to access/use; "licensed, not sold"; held on account | purchase + purchase code + per-item license; statements per account | payment-on-file purchase; IAP machinery; subscriptions |
| Delivery/access | client download/install; client may be required to run | file download; purchase code as proof | install via OS; IAP delivered in-app |
| Refund posture | explicit self-service policy with usage/time conditions | customer/author refund policy pages exist (terms not fetched) | platform purchase/billing support via AppleCare (terms not fetched) |
| Seller admission | listing with store-presence requirements (docs not fetched) | admission + quality gates | review gate for every app/update/IAP |
| Seller earnings | publisher revenue share; Workshop revenue share per-app terms | commission-based author earnings | App Store commerce + analytics; small business program |
| Extras | wallet, gifting, bundles, community market, workshop UGC, age gate | item support, invoices, affiliates, API | age ratings, family controls, offer types, grace periods |

Evidence-layer summary of transferable findings:

- Layer A (directly observed, product-specific): the quoted mechanics above.
- Layer B (cross-product commonality across the 3-product sample): storefront as a standing browse/discover surface with product pages; purchase converting into an account-held entitlement (license/access right); digital delivery (download / key / install / in-app); buyer account accumulating purchase records; a seller/partner side with listing, pricing, earnings and (in 2 of 3) admission gates; published refund/customer-protection policies.
- Layer C (canonical inference): the store's defining transaction is payment → recorded entitlement → digital access, and the store's defining surface is a multi-item buyer-facing venue. This is more abstract than any product's implementation (Subscription vs purchase code vs platform-account entitlement).

## L0 — Defining Invariant (minimal)

A Digital Goods Store is a buyer-facing venue whose defining core is four jointly-held structures:

1. **The storefront** — a standing, operator-run, buyer-facing surface presenting a catalog of many items for sale (browse, search, curation, product pages). Remove → a payment page or single-product checkout (sibling seller-tooling territory), or a plain file listing.
2. **Digital goods as the inventory** — every item is software or content whose delivery and use are digital; the store carries no physical-logistics leg for its goods. Remove → generic e-commerce storefront/marketplace.
3. **The purchase-to-entitlement conversion** — payment produces a recorded access/license right to the specific item, held on the buyer's account; the operator's fulfillment obligation is making the goods available/accessible, not shipping. Remove → free download directory (no purchase) or payment machinery with no venue (no store).
4. **Digital fulfillment and access** — the purchased entitlement is exercised digitally (download, key activation, client/launcher, in-app or streaming access) granted to the buyer's account. Remove → ordering goods by mail = physical commerce; remove access → payment-only conduit.

Jointly-held is load-bearing:

- 1 alone = generic storefront (physical e-commerce)
- 2 alone = a catalog/listing site
- 3 alone = checkout/payment machinery
- 4 alone = file hosting
- 1+2 without 3+4 = free download directory / portal
- 1+3 without 4 = voucher shop that never delivers the goods digitally
- 2+3 without 1 = single-seller checkout — the sibling seller-tooling pole
- 3+4 without 1 = a paywalled file host, not a store

## L1 — Common Mature Structure (standard capabilities, not definitional)

- Buyer account as entitlement container: purchase history/statements, and typically standing re-access (library/collection/downloads page). (B: Steam "Account history and Subscriptions"; Envato statements; Apple payment-on-file account; Steam homepage shows the library filter "Include items in my library".)
- Discovery machinery: search, categories/tags, curated and editorial surfaces, personalized recommendations, charts, wishlists, deal/sale events. (A: Steam homepage; Apple discovery section. B across sample.)
- Product pages with media, descriptions, technical requirements, and (commonly) ratings/reviews. (A: SSA cites reviews + minimum technical requirements; Apple product-page machinery.)
- Purchase forms beyond the base item: DLC/add-ons, in-app/consumable purchases, pre-orders, bundles, gifting, stored balance/wallet, free items. (A: Steam refund-policy scope table; Apple IAP section.)
- Subscriptions as a purchase form (recurring access). (A: Steam "Recurring Payment Subscriptions"; Apple auto-renewable subscriptions.)
- Refund/customer-protection policies with condition-based eligibility; buyer purchase support. (A: Steam policy terms; Envato policy pages exist; Apple AppleCare billing support.)
- Regional pricing/availability, currency handling, sales. (A: SSA geo-pricing clause; Apple international pricing tools; Steam observed sales.)
- Seller/partner side of the venue: listing management, pricing control, earnings/revenue-share dashboards, admission/quality gates, marketing/featuring surfaces. (A: Envato author hub; Apple App Store Connect; Steam Workshop revenue share + publisher sale surfaces.)
- Community/commerce extensions: reviews, discussions, user-generated content markets attached to the store. (A: Steam Community/Workshop/Market.)
- Key/activation pathway: keys sold through retail/reseller channels that activate entitlements in the store's account system. (A: Steam CD-Key/Product Key activation.)

## L2 — Variant / Optional Structure

- Store model: operator retail storefront (Steam; GOG anchor) / multi-vendor marketplace (Envato; itch.io anchor) / platform-native ecosystem store (Apple App Store; Google Play anchor; console and carrier stores). Platform-native stores may be the sole distribution channel for their goods class.
- Goods domain: games, apps, music, e-books, video, professional software, creative assets, in-game/in-app content.
- Delivery substrate: dedicated client/launcher, plain web download, key activation, in-app delivery, streaming access.
- Access/DRM posture: client-tethered access vs DRM-free files vs key-locked activation (Steam client-conditional language; GOG anchor's DRM-free positioning).
- Monetization: per-item purchase, pay-what-you-want (itch.io anchor), bundles, all-you-can-eat subscription catalogs, rental.
- Curation posture: open self-serve listing vs admission/quality-gated (Envato, Apple) vs editorial curation.
- Supply: operator may sell its own goods and/or third parties' goods.

## L3 — Vendor-specific (Research Notes only)

- Steam: "Subscription" terminology for purchases; Subscriber Agreement framing; Steam Wallet caps and Japan expiry; VAC-ban refund forfeiture; Discovery Queue/Points Shop; Subscription Marketplaces (Community Market); Workshop App-Specific Terms; 13+ age floor; in-document digital-vs-hardware contract-formation contrast.
- Envato: purchase codes; item support policy (author-provided); separate customer vs author refund policies; author exclusivity economics (market knowledge, not fetched); Market API; affiliate program.
- Apple: In-App Purchase machinery details (offer types, billing retry, grace periods, retention messages); featuring nominations; custom product pages; product page optimization; 175 regions / 50 languages; 200+ payment methods; Small Business Program; AppleCare purchase support; ecosystem embedding (Games app).

## Anti-overfitting Notes

- "Purchase = subscription/license, not ownership" is Steam's explicit legal framing. Apple and Envato evidence account-held purchases plus license/support machinery without that exact wording. Canonical form: "recorded access/license entitlement held on the buyer's account" — the license vocabulary is not definitional, the account-held entitlement structure is.
- Client/launcher delivery must NOT be definitional: Envato is a plain download venue; keys and streaming exist as alternative substrates. The invariant is digital access granted to the account, not a particular client.
- Reviews/wishlists/recommendations are market-standard but era-current; early stores (2003-era music/game stores) operated without several of them.
- The merchant-of-record pole is consistent in-sample (operator collects payment in all 3), but pay-what-you-want/direct-to-seller models (itch.io anchor) suggest the canonical phrasing should be "the venue operates the purchase machinery", not "the venue is always the merchant of record". Kept at L1 level of abstraction: the venue runs purchase and fulfillment machinery; who economically receives what (commission vs retail margin) varies.

## Boundary Findings

1. **vs Digital Download Commerce Platform / Digital Product Commerce Platform (§05.22 sibling + §27)** — the seam both prior passes anticipated. The sibling Types are SELLER-side operating platforms: the seller's catalog, the seller's checkout (hosted page, buy button, embed, CMS blocks), per-order automated delivery, seller earnings path. This Type is the BUYER-facing venue: the operator runs the store, buyers browse many items from one surface, purchases convert into account-held entitlements inside the store's account system. Test question: whose direct user is the software for? Store = the buyer; platform = the seller. A seller using the sibling Type can embed one buy button on their own site (no venue); a store's buyer never configures anything. DISCHARGES the forward flag: keep-both with the venue-vs-tooling seam; the two populations interlock (a store often exposes a partner side, but that partner side is a portal into the venue, not a standalone store builder).
2. **vs Online Marketplace / Multi-vendor Marketplace (§05.02)** — the marketplace-form digital goods store (Envato) satisfies the generic marketplace core (operated venue + seller-authored supply + mediated attributed transaction + operator economics). The specialization is real: goods are digital, so fulfillment is entitlement/delivery rather than logistics, and the retail-form store (Steam's own-sale pole; Apple) falls outside the multi-vendor marketplace core entirely. Recorded as a boundary issue for joint review: the marketplace form of this Type is a digital-goods specialization of the generic marketplace core; this pass does not merge or rewrite the directory.
3. **vs E-commerce Platform / Online Store Builder (§05.01)** — those are tools a merchant uses to BUILD and run their own storefront; this Type is the storefront/venue itself that buyers visit. Keep both.
4. **vs Video/Music Streaming Platform (§27)** — streaming sells ongoing access to a catalog (subscription posture); the store's defining transaction is the per-item purchase producing an entitlement. Rental and all-you-can-eat catalogs are variant postures inside some stores; a pure streaming service without per-item purchase falls outside.
5. **vs Creator Storefront (§27)** — goods-centered storefront with physical fulfillment machinery standard (per that pass's boundary note); this Type is all-digital delivery. The two passes' fulfillment test separates them consistently.
6. **App stores** — no separate directory leaf exists; platform-native app stores are documented here as a store-model variant, not a separate Type.
7. **vs consumption applications (E-book Reader, E-book Library, media players, game launchers without store)** — consumption surfaces are not venues; a launcher with no store is outside this Type.

## Historical / Market-Sample Check

- 2003-era stores (iTunes Music Store; Steam's launch): storefront, per-item purchase, account-held entitlement, download delivery — fit the four-part core without wishlists, reviews, recommendations, or modern refund policies. Passes.
- Mid-2000s console stores (Xbox Live Marketplace, PSN Store, Wii Shop) and feature-phone carrier decks selling ringtones/games: storefront on device, per-item purchase, entitlement delivered to handset/account. Passes — supports abstracting away the client/launcher and web surfaces.
- Shareware registration and key-by-email purchasing (pre-storefront e-commerce): purchase → key entitlement with minimal browsing surface. The thin ancestor; fits if a multi-item catalog surface existed, otherwise sits below the Type (checkout without venue).
- Regional forms (DLsite/DMM in Japan, regional Android app stores) match the core; nothing in the core assumes a Western consumer web pattern.
- Conclusion: the core does not depend on client ecosystems, reviews, refunds, wishlists, recommendations, or any specific era's discovery machinery.

## Uncertainties

- Envato's storefront UI details (search, collections, browsing) were not directly observed; buyer-side browsing evidence is structural (help centers), not surface-level. Assertions about marketplace storefront UI are kept at B level.
- Apple's consumer-side purchase/refund behavior was not fetched; only the developer-facing page. No claims made about Apple refund terms.
- itch.io, GOG, Bandcamp, Google Play: unreachable; their positioning is used only as named anchors for variant breadth, never as evidence for structure.
- Whether the market increasingly blurs store vs subscription catalog (store-run all-you-can-eat catalogs) was not deeply researched; held as a variant posture, not resolved.
- Steam's seller-side store-presence requirements (Steamworks docs) were not fetched; Steam's admission posture is stated cautiously.

## Final Synthesis

The venue reading holds. The market realizes a distinct buyer-facing population — operator-run stores where buyers browse and purchase digital goods and receive account-held entitlements — structurally different from the seller-side operating platforms documented by the two sibling passes. Digital Goods Store is defined as the venue: a storefront presenting a catalog of digital goods, purchase machinery operated by the venue, purchase-to-entitlement conversion, and digital fulfillment/access. Three store models (retail storefront, multi-vendor marketplace, platform-native ecosystem store) are variants of one Type; seller-side tooling, generic physical-goods marketplaces, store builders, and streaming platforms are neighboring Types. The four-leg core is minimal and passes the historical check.
