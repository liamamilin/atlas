# Research Notes — Mobile Commerce Application

## Research Goal

Understand what a Mobile Commerce Application is as an Application Type: the core objects a shopper manipulates in the app, what the app is bound to, what is app-specific structure versus shared commerce structure, who produces these apps and how, which flows are distinctive, which rules matter, and where the boundary lies against the §05.01 siblings (E-commerce Platform, Online Store Builder, Headless Commerce Platform) and the wider commerce cluster (Marketplace, Checkout, Mobile POS, Shopping Discovery).

This pass also carries two pre-hung ratification duties from sibling passes:

1. **e-commerce-platform (processed)**: "expected seam = buyer-side mobile surface vs seller-side platform (mobile storefronts and admin companions appear in this sample as channel variants without changing the core); to be ratified from that side."
2. **online-store-builder (processed)**: "mobile appears in this sample as (a) responsive storefronts the builder produces, and (b) merchant-side mobile admin/POS companion apps. Both are channel/companion surfaces; the seller-side platform is the Type. Ratified from this side as expected."

## Initial Boundary

- The leaf sits in §05.01 E-commerce Storefront beside three seller-side platform leaves. The natural reading is the **buyer-side mobile shopping application** — the dedicated app a consumer installs to shop a specific seller's venue.
- "Mobile commerce" (m-commerce) is also an industry channel term (commerce via mobile devices generally). That reading is context, not the Type; the Type is the application object.
- Nearest neighbors: E-commerce Platform (seller-side system), Online Store Builder (web-store production), Headless Commerce Platform (decoupled backend+APIs), Marketplace Platform (multi-seller venue), Shopping/Product Discovery Application (cross-seller), Mobile POS (seller-carried in-person surface), Checkout Platform (checkout slice), Digital Wallet (payment instruments).
- Precedent inside this atlas: surface-defined sibling leaves are kept as separate Types when the surface is load-bearing — Mobile Banking Application vs Online Banking Portal (ratified keep-all-three 2026-09-10), Mobile POS vs Retail POS (ratified keep-both 2026-09-06).

## Research Questions

1. What objects does the shopper manipulate inside the app (catalog, product, cart, checkout, order, account, saved items)?
2. What is the app bound to — is the seller's commerce backend the system of record, or does the app own commerce state?
3. What structure is app-specific (push, device capabilities, app-store lifecycle, app-only benefits) versus shared with the web storefront?
4. Who produces these apps and how — retailer in-house vs merchant app-builder platforms? What does an app-builder product actually provide?
5. Which flows are distinctive: browse→buy, re-engagement (push→deep link→buy), post-purchase servicing, marketplace sell-side?
6. Which rules matter: account continuity across surfaces, guest vs logged-in, permission-gated push, app-store review, purchases routed through the operator's servers?
7. Boundary: buyer-side app vs seller-side platform; app vs discovery/aggregation apps; app vs mobile POS; app vs checkout slice.

## Representative Products

Selected to cover both production models and multiple tiers/philosophies:

| Product | Pole | Why sampled |
|---|---|---|
| Amazon Shopping App | retailer-operated consumer app (largest western e-commerce) | the canonical "store's own app"; official App Store listing + help pages + corporate newsroom |
| eBay App | marketplace-operated consumer app with in-app sell side | marketplace semantics (auctions, live) inside the app; official help center articles |
| Tapcart | merchant app-builder (Shopify ecosystem, DTC/SMB) | the production-platform pole with exceptionally deep official help docs |
| Vajro (rebranded Superfans) | merchant app-builder, loyalty/live-selling philosophy | a different product philosophy for the same object; product-page level evidence |

Enterprise-tier mobile commerce platform vendors (Poq class) were attempted and are recorded as a sourcing limitation below.

## Sources

- Tapcart Help Center (index + articles): https://help.tapcart.com/ — "Welcome to Tapcart!" (https://help.tapcart.com/en/articles/11120041-welcome-to-tapcart), "Cart Sync: Keep Carts in Sync Between Web and App" (https://help.tapcart.com/en/articles/16075704-cart-sync-keep-carts-in-sync-between-web-and-app)
- Vajro / Superfans product site: https://www.vajro.com/ (fetched 2026-09-10; brand mid-rebrand to Superfans.io)
- Amazon Shopping App — App Store listing: https://apps.apple.com/us/app/amazon-shopping/id297606951 ; Amazon Customer Service help "Shopping on the Amazon Shopping App": https://www.amazon.com/gp/help/customer/display.html?nodeId=GEF4J8BNR2WA8BB9 ; About Amazon newsroom "10 cool features to try in the Amazon Shopping app": https://www.aboutamazon.com/news/retail/amazon-shopping-app
- eBay — help "Using the eBay app": https://www.ebay.com/help/buying/getting-started-ebay/using-ebay-app?id=4032 ; help "Selling with the eBay app": https://www.ebay.com/help/selling/ebay-tools/ebay-app-sellers?id=4100 ; Google Play listing: https://play.google.com/store/apps/details?id=com.ebay.mobile ; eBay app marketing page: http://pages.ebay.com/mobile-app and https://pages.ebay.com/gp/en-us/ebay-app-mobile
- Poq (enterprise mobile commerce platform): https://www.poqcommerce.com/ — **403 on both attempts (www and apex), abandoned per network rules.**

Research date: **2026-09-10**

## Product A — Amazon Shopping App (retailer-operated consumer app)

### Key observations (evidence layer A unless noted)

- **Bound to the existing account and the same commerce system as the web**: App Store listing (official): "Sign in with your existing Amazon account to access your basket, payment and shipping options. No need to create a new account to manage your 1-Click settings and wish lists, track your orders and use your Prime membership benefits. Shop just as you do on the web." And: "All purchases are routed through Amazon's secure servers."
- **The complete buying flow in-app**: "Browse, view product details, read reviews, and purchase millions of products." Multi-country store switching inside one app ("shop Amazon.ca, Amazon.co.uk, Amazon.de … from a single app").
- **App-only benefits as a stated category**: "Amazon Shopping offers app-only benefits to help make shopping on Amazon faster and easier than shopping on your desktop."
- **Device capabilities as first-class shopping tools**: scan a barcode or photograph an item to find it ("Just tap the scan icon in the search bar, take a picture of the item or its barcode, and we'll find it for you"); visual search (Amazon Lens); voice shopping; AR — View in 3D, View in Your Room, Virtual Try-On (camera/TrueDepth); biometric sign-in ("use facial or fingerprint identification to sign back in").
- **Push/alert machinery**: real-time tracking and delivery notifications; price-drop alerts on saved items ("tap the heart icon to save items to Your Lists and we'll alert you of price drops"); widgets on home/lock screens for order tracking, deals, and Lens search.
- **AI-era discovery** (newsroom, official): Shopping Guides (gen-AI research + recommendations), Interests (continuously scanning inventory, proactive notifications on restocks/deals), Rufus AI assistant, See It On Your Model, Skincare Quiz.
- **Servicing in-app**: help page documents "Cancel an Order in the Amazon Shopping App" and "Logging Out of a Lost Device"; live chat support 24/7 with a 24-hour session persistence.
- **Permission surface**: the app requests contacts, camera, microphone, notifications, touch ID, photos, Bluetooth "to enable features such as voice shopping, notifications, visual search, customer reviews, and authentication."

Reading: the app is Amazon's commerce system experienced as an installed mobile surface, with app-only incentives and device-native capabilities layered on top. No separate "mobile commerce product" exists — the app is the surface of the same system.

## Product B — eBay App (marketplace-operated consumer app with sell side)

### Key observations (evidence layer A)

- **Same system as the site**: help center: "You can shop for items on the eBay app the same as you would on the site." Search, sort/filter, Add to cart, "tap the shopping cart icon and proceed to checkout", purchases in "Purchases", watchlist in "My eBay → Watching".
- **Buy AND sell in one app**: "Download the eBay app to buy, sell, or browse straight from your phone." Selling help: create/edit/monitor listings, relist, add tracking; "Scan your item's barcode to automatically add product details from our catalog"; "Snap photos and add them directly to your listing"; "Listings will sync across your devices, so you can start a listing on the app and finish it on your laptop or desktop, or vice versa."
- **Marketplace semantics in-app**: auctions/bidding ("live auctions, live bidding"), eBay Live livestream shopping ("exclusive drops, live auctions, case breaks"), Best Offer-class negotiation implied by marketplace mechanics (not asserted beyond listing text).
- **App-only incentives**: marketing page: "App-only discounts… higher discounts and one-of-a-kind offers only for eBay app users"; price notifications ("we'll tell you when the price has dropped"); daily deals.
- **Push**: "real-time alerts about Daily Deals, order updates and more… personalised push notifications"; notification enablement documented per OS plus in-app notification settings.
- **Trust machinery surfaced in-app**: Authenticity Guarantee, Money Back Guarantee.
- **AI-era listing tools**: "AI Snap… let AI instantly generate descriptions and key details for your listing."

Reading: a marketplace's consumer app carries both sides of the marketplace (buy + casual sell) on the mobile surface, bound to the marketplace's backend; app-only deals and push are the retention layer.

## Product C — Tapcart (merchant app-builder, Shopify)

### Key observations (evidence layer A)

- **The product is the merchant's own branded app, produced from the store**: "Tapcart is the premier mobile app provider on Shopify! With Tapcart you can launch a mobile app that seamlessly integrates with your Shopify store to increase retention, build brand loyalty and boost customer lifetime value." "No-code required platform… create a professional-looking app within hours." "Tapcart is a white-label solution, there will be no Tapcart branding in your app!"
- **App-store lifecycle owned by the merchant**: merchant registers their own Apple Developer ($99/yr) and Google Play ($25 one-time) accounts; app listing creation, privacy policy generation, account-deletion compliance, submission & review timelines, Release Manager, TestFlight beta management; "live in the App and Google Play Stores in 1-3 weeks"; business must be a legal entity.
- **The binding to the backend is explicit and load-bearing**:
  - Products/collections sync from the Shopify store ("Adding Products & Collections to Tapcart").
  - Cart Sync article: "Cart Sync keeps a logged-in shopper's cart consistent between your online store and your Tapcart app. Add an item on web, and it appears in the app. Add in the app, and it appears on web." "Native Shopify checkout. Checkout stays 100% native Shopify on both surfaces. Tapcart does not intercept checkout." Cart record "keyed to their Shopify customer account"; "Logged-in only. Guests are untouched."
  - Account screens tie to Shopify customer accounts ("Classic vs. New Customer Accounts in Shopify"); order history & subscription management in-app.
  - Checkout configuration mirrors the store: Shopify Markets, multi-currency, payment gateways, selling plans (subscriptions), bundles.
- **The app as an owned marketing channel** (merchant-side machinery): push notifications with segments, personalization tokens, automated push (abandoned cart, browse abandonment, winback, back-in-stock, checkout recovery), in-app Inbox; deep linking (universal links, ad deep links); "Capture Kit" QR codes to drive app installs; app-exclusive discounts and in-app exclusives; pre-launch/post-launch campaign guides.
- **App-native merchandising**: screens/blocks/theme editor (bottom navigation, headers, custom blocks via CLI), drafts & scheduled content updates, A/B testing of app layouts, "For You Feed" personalization, barcode/QR scanner integration, wishlist sync across web and app.
- **Measurement**: app analytics (Insights dashboard, conversion reporting, session timeout), integration event tracking (Firebase, Meta SDK), app-store analytics; attribution integrations (AppsFlyer, Branch).
- **Ecosystem integrations**: loyalty (Smile, LoyaltyLion, Yotpo), reviews (Judge.me, Okendo, …), search & merchandising (Algolia, Constructor, …), subscriptions (Recharge, Loop, …), live selling & video commerce (LyveCom, Tolstoy, LiveMeUp), support (Gorgias), shipping/protect (AfterShip, Narvar, Route).

Reading: an app-builder product does not operate commerce; it produces and operates the merchant's mobile shopping surface over the merchant's commerce backend, and sells the app-native layer (push, exclusives, analytics, app-store lifecycle) as its value.

## Product D — Vajro / Superfans (merchant app-builder, loyalty & live-selling philosophy)

### Key observations (evidence layer A for positioning; product-page level only — help docs not fetched)

- Positioning: "The mobile app tailored for your superfans… Your best customers always show up for you, now give them a mobile app that shows up for them. Early access, personal attention, push-powered journeys, and a home they'll keep coming back to." The app framed as the "VIP lounge" for the merchant's best customers — a loyalty/retention channel beside email and SMS ("a third, high-ROI channel — one that's fully owned… No deliverability. No opt-ins. No send costs.").
- Production speed claims: "Build in 60 minutes. Test drive for 30 days."; "Go live in weeks, not months"; "Built by the team behind 5,000+ mobile apps."
- Shopify-ecosystem binding implied by "the perfect solution for Shopify merchants" (customer testimonial) and the Shopify app store trial link.
- Integration inventory: BNPL (Sezzle, Clearpay), loyalty (Smile.io, LoyaltyLion), reviews (Judge.me, Loox, Stamped), search (Algolia, Searchanise), live chat (Tidio), stories (Storifyme), account page (Flits).
- Heritage: Vajro known for live video selling; comparison pages vs CommentSold (live-selling commerce) and vs Tapcart/Shopney/Appbrew (app builders).

Reading: same object as Tapcart (merchant's branded shopping app over the store's backend), different philosophy — the app positioned primarily as a loyalty/retention and live-selling channel rather than a conversion surface.

## Cross-product Comparison

| Dimension | Amazon app | eBay app | Tapcart-built apps | Vajro/Superfans-built apps |
|---|---|---|---|---|
| Surface | installed app (iOS/Android), widgets | installed app (iOS/Android) | installed app, white-label, merchant's store accounts | installed app, white-label |
| Backend binding | Amazon's own commerce system; same account as web; purchases through Amazon servers | eBay marketplace backend; "same as you would on the site" | Shopify store = system of record; catalog/cart/accounts/checkout native Shopify; "Tapcart does not intercept checkout" | merchant's Shopify store (implied by ecosystem + trial link) |
| Buying flow in-app | browse→PDP→cart→checkout→orders; multi-country switching | browse→cart→checkout; plus bidding/auctions/live | full flow via synced catalog + native checkout | full flow (product-page level) |
| Account continuity | existing Amazon account; biometric re-sign-in | eBay account; reinstall keeps data | Shopify customer account keyed cart sync; logged-in only | store accounts (implied) |
| App-only incentives | "app-only benefits" (stated category) | app-only discounts/offers (stated) | app-exclusive discounts, in-app exclusives (productized) | early access, app as VIP channel |
| Push | delivery tracking, price drops, deal alerts | deals, order updates, price notifications | full campaign machinery + automated flows + inbox | "push-powered journeys" (positioning) |
| Device capabilities | scan/vision search, voice, AR try-on/3D, biometrics | barcode scan (listing), photo search, shake-to-report | barcode/QR scanner block, camera capture | (not directly observed) |
| Sell side | none in consumer app | yes — listing creation, AI Snap, sync across devices | n/a (merchant operates via dashboard) | n/a |
| Production model | retailer in-house | marketplace in-house | no-code dashboard + app-store submission service | no-code builder, speed-positioned |
| Philosophy | everything-store in one app | marketplace + casual selling + live | retention/LTV app for DTC brands | loyalty/superfan channel + live selling |

**Cross-product commonalities (evidence layer B):** the app is a dedicated mobile buying surface bound to the seller's commerce backend; the complete buying flow runs in-app; the shopper's account is continuous with the seller's web presence; app-only incentives are a named, deliberate category in every sample; push notifications are the retention engine; device capabilities (camera scan, biometrics) are first-class; order tracking/servicing lives in-app.

**Vendor-specific (layer D, stays here):** Tapcart's Capture Kit/Release Manager/AI Notification Agent/For You Feed/Insights API and Shopify-only binding; Amazon's Rufus/Interests/Shopping Guides/See It On Your Model/Skincare Quiz/1-Click/Prime/multi-country switching; eBay's eBay Live/AI Snap/My Garage/Authenticity Guarantee/PSA Vault/Simple Delivery; Vajro's 60-minute build claim and 5x/2x marketing stats; Superfans rebrand.

## Canonical Model (abstraction)

### L0 — Defining Invariant (minimal, jointly-held)

1. **The seller's dedicated mobile shopping application on the shopper's device** — an installed app (app-store distributed; PWA-class and embedded mini-program surfaces as variant realizations) operated for one seller's venue, encountered and used on the shopper's personal mobile device. Remove → the seller's web storefront (e-commerce platform territory).
2. **Binding to the seller's commerce backend as the system of record** — the app's catalog, pricing, cart, customer accounts, checkout and orders are bound to / synchronized with the operator's commerce system; the app presents and extends that system rather than replacing it. Remove → a standalone app with no commerce semantics, or a generic app-builder product.
3. **The complete buying flow executed on the mobile surface** — browse/search → product detail → cart → checkout/payment → order confirmation, carried out within the app. Remove → a marketing/content app or store locator.

Jointly-held load-bearing:
- 1 alone = a generic mobile app (or the mobile web, which is not an application).
- 2 alone = an integration/API, not an application.
- 3 alone = a checkout widget / payment link.
- 1+2 without 3 = showroom/catalog app (drifts toward marketing-app territory).
- 1+3 without 2 = the app IS the commerce system — better described as an e-commerce platform in a mobile-first form (app-first drift; recorded as a boundary note, not this Type's center).
- 2+3 without 1 = the web storefront — the same buying flow on a different surface.

### L1 — Common Mature Structure

- Shopper account continuous with the seller's web customer account (sign-in, order history, saved items/wishlist); biometric/device sign-in.
- Push notifications & alerts (order/delivery status, price drops, back-in-stock, abandoned cart, campaigns) + in-app inbox/notification settings.
- App-only benefits as a deliberate channel incentive (exclusive discounts, early access, app-only products/offers).
- Device capabilities as shopping tools: camera (barcode/image scan search, AR view-in-room/try-on), voice search, location.
- Order tracking and self-service servicing in-app (order history, cancel where offered, support chat).
- Personalization (recommendations, "For You"-class feeds), wishlist with price-drop alerts.
- Deep linking (ads/email/web → in-app product/cart surfaces).
- Merchant-side: app analytics & attribution; content scheduling/drafts; A/B testing of app layouts.
- Loyalty/rewards integration; live video shopping (in a subset); home/lock-screen widgets.

### L2 — Variant / Optional Structure

- Production model: retailer/marketplace in-house build vs merchant app-builder platform (white-label, merchant-owned developer accounts, submission service) vs PWA-class vs embedded mini-program surface.
- Seller kind: single-seller brand/retailer vs marketplace (multi-seller venue, auctions, in-app casual sell side).
- Geography/market features: multi-country store switching in one app; market payment rails (BNPL integrations etc.).
- Philosophy poles: conversion-first vs loyalty/superfan-first vs live-selling-first.
- AI-era discovery layers (shopping assistants, generative guides, visual search depth).

### L3 — Vendor-specific

See Vendor-specific Findings above; none of it enters the canonical core.

## Historical / Market-Sample Check (§24)

- Would older products fit? Early mobile commerce — WAP shopping portals, i-mode shopping (Japan), Java ME shopping apps, SMS/IVR ordering — were mobile surfaces bound to a commerce backend carrying a buying flow, without app stores, push, AR, or AI. They satisfy the three-leg core; app-store distribution, push, and device capabilities are era-current implementations, not invariants. The definition does not over-fit to the modern app-store era.
- Regional: super-app embedded commerce surfaces (mini-program stores) satisfy the binding + buying-flow legs with the "dedicated mobile surface" realized inside a host app — recorded as a variant realization, not excluded.
- Platform-native: a mobile-first commerce system that exists ONLY as an app (no web storefront) still satisfies the core; the seam note below records that such a product drifts toward the e-commerce-platform reading.

## Boundary Findings

### vs E-commerce Platform (§05.01 sibling) — RATIFIED from this side

The platform is the seller-side system of record operating the whole buying flow across surfaces (web storefront, mobile web, apps, admin); the mobile commerce application is the buyer-side dedicated mobile surface bound to that system. Removal tests: remove the dedicated mobile-app surface from this Type → the seller's e-commerce platform/storefront; remove the backend binding (the app becomes the whole commerce system) → an e-commerce platform in mobile-first form. The seam is **surface vs system-of-record**. The e-commerce-platform pass's observation ("mobile storefronts, dedicated shopper apps, mobile admin companions appear in-sample as channel variants; the Type's center is unchanged on a phone") is consistent: those are channel variants OF THE PLATFORM; the dedicated shopper app is THIS leaf's object. **Keep-both ratified** (mobile-banking/online-banking and mobile-pos/retail-pos precedents: surface-defined siblings stay separate when the surface is load-bearing — here the installed surface carries push, device capabilities, app-only incentives, app-store lifecycle, and home-screen persistence that the web surface does not have in the same form).

### vs Online Store Builder (§05.01 sibling) — RATIFIED from this side

The builder's product is the web store it assembles (venue = web store, no-code assembly the defining act); the app-builder products sampled here (Tapcart, Vajro) are the production tooling for THIS Type — their venue is the installed app bound to an existing backend, and they explicitly do not create the store (they require one). The online-store-builder pass's observation that "mobile" appears in its sample only as responsive storefronts and admin companions is confirmed: those are not this leaf's object. **Keep-both; seam = which surface is the product.**

### vs Headless Commerce Platform (§05.01 sibling)

Headless decouples the storefront from the backend via APIs — the mobile app is one "head" among several. The headless platform is backend+API machinery (seller-side); the mobile commerce application is the consumer head (buyer-side). Adjacent; a headless backend can feed this Type's app (Tapcart documents "Cart Sync for Headless Storefronts" and a "Wishlist SDK for Headless Storefronts").

### vs Marketplace Platform (§05.02)

Marketplace = multi-seller venue operated by an intermediary (seller-side). A marketplace's consumer app is an instance of this Type whose backend happens to be a marketplace (eBay sample). The app is the surface; the marketplace is one kind of backend.

### vs Shopping Discovery / Product Discovery / Deal Discovery (§05.05)

Discovery applications operate across sellers (aggregation, comparison, deals across stores). The mobile commerce application is bound to ONE seller's venue. Multi-seller aggregation apps (e.g., the "shop many stores" class) are a different Type; noted as adjacent without deep research.

### vs Mobile POS (§05.10)

The Mobile POS sale runs on the seller's device, in person, at the exchange; the mobile commerce purchase runs on the buyer's device, remotely. Consistent with the mobile-pos pass's recorded seam.

### vs Checkout Platform (§05.06)

Checkout platform = the checkout slice. The mobile commerce application carries the whole shopping surface (discovery→buy→servicing); checkout is one stage inside it (and in the app-builder sample, checkout is not even owned by the app layer — it stays native to the commerce platform).

### vs Digital Wallet / Mobile Wallet (§08)

Wallets hold payment instruments/value; the commerce app sells goods and services. Wallet checkout appears inside the app as a payment method.

### Drift note (app-first)

If the operator's entire commerce presence lives only inside the app (no web storefront), the product is better described as an e-commerce platform in a mobile-first form. This Type's center assumes the app is a dedicated surface over a commerce backend, not the backend itself.

## Uncertainties

1. **Enterprise-tier production model (Poq class)**: poqcommerce.com returned 403 on both attempts; no enterprise mobile-commerce-platform vendor was directly observed. The enterprise pole is asserted only from the app-builder side's existence and general market structure — no enterprise-specific structural claims are made in the final document.
2. **Vajro/Superfans depth**: evidence is product-page level (positioning, integrations, testimonials); help docs (help.superfans.io) not fetched. No workflow claims asserted from this product; used for philosophy-pole diversity only.
3. **Guest checkout behavior in app-builder apps**: Tapcart cart sync is explicitly logged-in only; whether in-app guest checkout is available varies by the underlying platform's checkout and was not directly verified. The final document avoids precise guest-checkout claims.
4. **PWA-class products**: no PWA-builder product directly sampled; PWA recorded as a variant realization without product-specific claims.
5. **Consumer-app operational rules**: Amazon/eBay evidence comes from store listings, help articles, and the corporate newsroom; deep operational parameters (notification defaults, session behavior, exact cancellation windows) were not researched and are not stated.
6. **Mini-program surfaces**: treated as a variant realization on conceptual grounds; no mini-program product directly sampled this pass.

## Final Synthesis

The Mobile Commerce Application is the **buyer-side dedicated mobile shopping application bound to a seller's commerce backend**: an installed app on the shopper's device through which the complete buying flow runs, with the seller's commerce system as the system of record and the app layer adding what the mobile surface uniquely carries — push re-engagement, device capabilities (camera scan, AR, biometrics), app-only incentives, home-screen persistence, and app-store lifecycle. It is a surface-defined sibling of the E-commerce Platform (same commerce spine, different surface, surface load-bearing), produced either in-house by retailers/marketplaces or via merchant app-builder platforms that generate and operate white-label apps over an existing store. The two pre-hung sibling seams are ratified from this side; keep-both with E-commerce Platform and Online Store Builder; no directory change.
