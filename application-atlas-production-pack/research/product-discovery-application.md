# Research Notes — Product Discovery Application

## Research Goal

Understand the consumer-facing shopping Application Type whose primary job is helping shoppers **discover products they did not set out to find** — through browse-oriented, curated, personalized, or social surfaces — as distinct from query-driven shopping search, offer comparison, and deal discovery.

Directory context: leaf `Product Discovery Application` sits in **05.05 Shopping Discovery** alongside `Shopping Search Engine`, `Shopping Comparison Platform`, and `Deal Discovery Platform`.

**Name-collision caution:** §12 Software Development contains a different leaf, `Product Discovery Platform` (product-management software, e.g. feedback → insight tools). That leaf is about software teams discovering what to build. This leaf is about consumers discovering products to buy. The two must not be conflated.

## Initial Boundary

- **What it probably is:** a consumer application that aggregates product (and/or brand) records from multiple sellers and surfaces them through feeds, collections, edits, trending lists, and similar browse surfaces, with a path to purchase attached to each product.
- **Who uses it:** individual shoppers in a leisure/intent-mixed shopping mode ("see what's out there", "find something for someone", "keep up with brands I like").
- **Nearest neighbors:** Shopping Search Engine, Shopping Comparison Platform, Deal Discovery Platform (siblings); E-commerce Platform / Online Marketplace / Digital Product Catalog (commerce family); Content Curation Platform, Review Platform, Interest-based Social Network, Personalized Content Feed (content/social family).
- **Likely confusion points:**
  - vs Shopping Search Engine: query-first vs browse-first.
  - vs Marketplace: who owns the transaction and the catalog.
  - vs Content Curation: is the unit a product record with commercial linkage, or a content item?
- **Unknowns going in:** how products enter the catalog; where checkout happens (in-app vs redirect); how personalization works; how monetization shapes behavior; whether identity/accounts are defining or merely common.

## Research Questions

1. What are the core objects (product, brand/store, feed, collection, review, offer)?
2. What does the user actually do, step by step, in the primary loop?
3. How do products enter the catalog (platform ecosystem, merchant feeds, affiliate links, user submissions)?
4. Where does the purchase happen — in-app checkout or redirect to the seller?
5. What drives what is surfaced (algorithmic personalization, editorial, creator, community, social graph)?
6. What role does search play relative to browse?
7. How does monetization (affiliate, ads, rewards) manifest in the product experience?
8. What state, rules, and exceptions matter (availability, location filtering, price-drop notifications, recommendation controls)?
9. Where exactly are the boundaries with the three sibling Types and with marketplace/curation/social Types?
10. Would older, regional, or platform-native discovery products still fit the definition?

## Representative Products

Selected for market representativeness, documentation accessibility, and distinct product philosophies:

| Product | Philosophy / posture | Role in sample |
|---|---|---|
| **Shop (Shopify)** | platform-ecosystem shopping destination app: discovery + in-app checkout (Shop Pay) + delivery tracking + rewards, over independent Shopify stores | primary sample, evidence A |
| **Thingtesting** | brand discovery + community review platform; brand pages, curated edits, outbound affiliate links, review rewards | primary sample, evidence A |
| **Klarna** | payments-first app whose shopping surface is organized around search/compare/brands/cashback | boundary sample, evidence A |
| **Wanelo, Polyvore, Kaboodle, ThisNext, Fancy** | historical social/visual shopping discovery products (2006–2018 era), now defunct | historical check (§24), qualitative only |
| **Xiaohongshu (RED), Musinsa/Kream, TikTok Shop, Instagram Shopping, Pinterest** | regional / platform-native / content-first discovery-commerce forms | historical & boundary check, qualitative only |

## Sources

Fetched 2026-09-06 (WebFetch):

- Shop Help Center — root TOC: https://help.shop.app/hc/en-us
- Shop Help Center — Getting started: https://help.shop.app/en/shop/getting-started
- Shop Help Center — Discover stores and products: https://help.shop.app/en/shop/shopping/discover
- Shop Help Center — Make purchases: https://help.shop.app/en/shop/shopping/make-purchases-in-shop
- Shop Help Center — Save products and follow stores: https://help.shop.app/en/shop/shopping/discover/save-products-and-follow-stores
- Shop Help Center — Manage your Shop profile: https://help.shop.app/en/shop/getting-started/profile
- Thingtesting — About/FAQ: https://thingtesting.com/about
- Thingtesting — Discover (front page): https://thingtesting.com/
- Klarna — Shopping: https://www.klarna.com/us/shopping/
- Klarna — App: https://www.klarna.com/us/klarna-app/

Unreachable (1–2 attempts each, then abandoned per network rule):

- LTK (help.ltk.com, ltk.com) — transport errors ×2
- Pinterest Help (help.pinterest.com) — timeouts ×2
- Houzz Support — CSS error page
- shop.app root + help.shopify.com merchant docs — 403
- thingtesting.com/faq — 404 (FAQ answers not expanded; about-page FAQ questions + nav used instead)

Consequence: the sample rests on two deeply documented products (Shop, Thingtesting) plus one boundary product (Klarna). Historical and regional products were **not** re-verified in this pass; all claims about them are qualitative and marked evidence layer C.

## Product Observations

### Shop (Shopify) — evidence layer A (official help center, directly observed)

**Positioning:** "Shop is a shopping destination and delivery tracking app created by Shopify." Available as iOS/Android app and web at shop.app.

**Discovery surfaces (directly observed):**
- **Shop search** — keyword search (brand names, product names, categories) with filters; in US/Canada, conversational search ("describe what you're searching for in your own words", e.g. gift-for-hiker example) returning context-based results instead of filters. Results personalized by purchase history, shopping activity, personalization settings; filtered to stores that ship to the user's location.
- **Personalized home feed** — content from followed stores + recommended new stores; content types: product/store recommendations based on interests, new products/posts/videos from followed stores, recently viewed products, saved-item updates (price drops, back-in-stock), reorder suggestions, promotional offers. Sub-surfaces: Deals, Following, Minis, Saved.
- **Shop Minis** — "interactive shopping experiences" (vendor-specific surface).
- **Recommendation management** — press-and-hold a recommended product → "Not interested" or "Show similar".

**Personal shopping context (directly observed):**
- Save products (favorites, "unlimited number of items"), organize into **collections** (private or public; collaborators can be invited to add products; shareable view-only links; "Find more ideas" on collection page).
- **Follow stores**; notifications for: saved-product price drops, sold-out back-in-stock, collection activity, followed-store updates (products, collections, sales).
- **Profile** — photo, display name, bio, gender, birthday, personalization preferences (sizing, skin care, hair care), "others you shop for"; profile hidden until first public collection is created; display name appears alongside public collections and product reviews.
- Shopping-activity sync referenced as a personalization input (browsing activity).

**Acquisition path (directly observed):**
- Browse → product page → **Add to cart** → checkout. Cart can hold items from multiple stores but **checkout completes one store at a time**.
- Payment via **Shop Pay** (saved email/addresses/payment); Shop Pay Installments for eligible orders; **Shop Cash** rewards earned and redeemed on eligible purchases; **Shop offers** (limited-time special pricing or extra Shop Cash from participating stores).
- In-store pickup ("Available at" locations on product pages), subscription products (delivery frequency options), marketplace sales tax for US orders.
- Orders appear in **Orders** tab; delivery tracking with tracking numbers; post-purchase **product reviews**; contact store; report issue; store ratings and suspected-fraud guidance.
- **Agentic shopping**: "Shop App for ChatGPT" — discovery through agentic experiences, then "you're directed to the store's website to complete your purchase."

**Catalog substrate:** participating Shopify stores (platform-ecosystem catalog).

### Thingtesting — evidence layer A (official site, directly observed)

**Positioning:** "Your go-to brand discovery and review platform… Come here to research before you buy, discover, and try new things, and share your honest reviews to help others shop better." Origin story: began as an Instagram account reviewing brands; grew into "a community and platform where over 1 million shoppers research and review purchases every month."

**Discovery surfaces (directly observed):**
- **Discover front page** — curated collection rails: "Trending", "New Launches", "The Oral Care Edit", "Wearables Everywhere", "For the Modern Mother", "Editor Picks"; "Browse all brands"; **Categories**; **Best of Thingtesting**; **Gift guides**; **Stories** (community content).
- **Brand cards** — brand image, one-line description, aggregate rating with review count (e.g. "4.5 • 641 reviews"), "View brand" + "Shop" external link (affiliate redirect via click.thingtesting.com).
- **All brands** directory; **Submit a brand** (community intake).

**Community/review layer (directly observed):**
- Reviews with ratings on brand pages; "Write a review"; latest-reviews stream; **Thingtesting Rewards** — "cash-based commission in exchange for writing thoughtful reviews" (per-brand reward percentages displayed, e.g. 20% reward).
- Business side: "Claim your brand" (brand self-service page management), contact sales.

**Acquisition path (directly observed):** outbound "Shop" links to retailers; affiliate disclosure: "Things you buy through retailers after clicking an external link on Thingtesting may earn us a commission." No in-app checkout observed.

**Catalog substrate:** brand pages for (mostly DTC) brands; community submissions + brand claims.

### Klarna — evidence layer A (official pages, directly observed; boundary sample)

**Positioning:** "Your everyday money app" — flexible payments, cashback, money management. The shopping surface is one layer of a payments app.

**Shopping surface (directly observed):**
- "Search, compare, save: Find your next deal today" — category tiles (Health, Clothing, Toys, Home, …), **Popular brands** (Walmart, eBay, Target, Nike…), **price comparison** "across thousands of stores", **cashback** offers ("Earn cashback when you shop at hundreds of stores in the Klarna app"), delivery tracking, gift cards, loyalty cards.
- FAQ: "browse stores and offers in the app and choose how you pay at checkout"; "find deals and cashback offers only available to Klarna users, compare prices, and keep track of orders and deliveries."

**Boundary reading:** Klarna's shopping layer is organized around **search + comparison + offers/cashback** — structurally closer to the Shopping Search / Comparison / Deal siblings than to a browse-feed discovery app. Its "discovery" is store/offer-led, not product-feed-led. Included to sharpen the boundary of this Type.

### Historical / regional / platform-native samples — evidence layer C (qualitative, not re-verified)

Used for the historical check only. No operational details asserted.

- **Wanelo** ("want–need–love") — user-saved products from any store into a shared social shopping feed; defunct.
- **Polyvore** — visual collage/mood-board discovery over fashion products with outbound shopping links; shut down after 2018 acquisition.
- **Kaboodle, ThisNext, Fancy** — 2006–2014-era social shopping discovery (user picks, curated feeds); defunct or marginal.
- **Xiaohongshu (RED)** — content-first community where product discovery happens through user posts with embedded commerce; regional (China).
- **Musinsa / Kream** (Korea) — fashion discovery layered with commerce/resale.
- **TikTok Shop / Instagram Shopping** — content platforms with commerce layers; discovery is a byproduct of the content feed.
- **Pinterest** — visual discovery engine; shopping is a surface on an interest-graph platform (help center unreachable in this pass).

## Cross-product Comparison

| Dimension | Shop | Thingtesting | Klarna | Historical social shopping (Wanelo/Polyvore/Kaboodle/ThisNext) |
|---|---|---|---|---|
| Core unit | product + store record | brand record (+ reviews) | product/offer + store | product record (user-saved or collage item) |
| Catalog source | Shopify store ecosystem | community submissions + brand claims | merchant feeds/price data | user-saved links from any store |
| Primary surface | personalized home feed, Deals/Following/Minis/Saved | curated edits, trending, categories, brand directory | search + categories + brands + offers | social feed / collages |
| Query role | supporting (keyword + conversational) | minimal (directory browse) | primary ("search, compare") | minimal |
| Personalization | activity-driven feed + explicit prefs + controls | editorial + trending + community | offer/cashback-led | social-graph/user-saved-driven |
| Acquisition path | in-app cart → Shop Pay checkout (one store at a time); agentic path redirects to store | outbound affiliate link to retailer | price-compare → store; cashback activation | outbound link to store |
| Social layer | follows, public collections, reviews, collaborators | reviews, rewards, stories | reviews of Klarna itself (not products) | core (saves, boards, community) |
| Monetization | platform commission/ads implied, Shop offers, Shop Cash | affiliate commissions, brand services, review rewards | interchange/BNPL economics, cashback program | affiliate (era-typical) |
| Trust surfaces | store ratings, report issue, fraud guidance | review community, honest-review positioning | buyer protection, app-store ratings | community reputation |

**Stable across the sample (candidates for the defining core):**
1. Product/brand records aggregated from **multiple sources** (never a single seller's own catalog).
2. **Browse-oriented discovery surfaces** that surface products without a user query (feeds, edits, trending, collections, directories).
3. An **acquisition path** attached to each product record (in-app checkout or outbound link to a seller) — shopping intent is structural.

**Common but not defining:** personal accounts, saves/favorites, follows, personalized feeds, price-drop/back-in-stock notifications, recommendation controls, reviews/ratings, supporting search, collections.

**Variant:** where checkout happens; what drives curation (algorithm/editorial/creator/community/social); catalog substrate; monetization; vertical focus; bundled services (payments, tracking).

## Canonical Abstraction

### L0 — Defining Invariant

A Product Discovery Application is a consumer-facing application built on three properties. Remove any one and it stops being this Type:

1. **Multi-source product catalog** — product (and/or brand) records aggregated from multiple sellers/merchants/brands. (Single-source → the operator's own storefront, i.e. e-commerce.)
2. **Query-independent discovery surfaces** — the primary interaction is browsing surfaces (feed, collections, edits, trending, directory) that surface products the user did not explicitly ask for. (Query-first → Shopping Search Engine.)
3. **Acquisition path per product record** — every product record carries a route to obtain it (in-app checkout or outbound link to a seller), carrying price/seller/availability context. (No acquisition path → content curation / bookmarking.)

### L1 — Common Mature Structure

Very common in mature modern products, not required for the definition:

- personal shopping context: account/profile, saved products (favorites/wishlists), followed brands/stores/creators, browsing & purchase history
- personalized feed(s) driven by activity, with explicit preference inputs (sizing, categories, "others you shop for")
- recommendation management ("not interested", "show similar")
- supporting search (keyword; increasingly conversational/AI-assisted)
- curation structures: user collections (private/public, sometimes collaborative), editorial edits/guides, trending/best-of lists, categories
- notification loop: price drops, back-in-stock, followed-source updates
- reviews/ratings and community content
- trust surfaces (store ratings, reporting)

### L2 — Variant / Optional Structure

- **Acquisition locus:** in-app checkout (Shop) vs outbound redirect (Thingtesting, historical social shopping) vs compare-then-redirect (Klarna)
- **Curation source:** algorithmic personalization vs editorial vs creator-led vs community/user-saved vs social-graph
- **Catalog substrate:** platform-ecosystem (Shopify stores) vs open-web affiliate vs merchant feeds vs user submissions
- **Monetization:** affiliate commissions, sponsored placements, platform commission, rewards programs (cashback, review rewards, platform cash)
- **Vertical focus:** general vs fashion vs home vs beauty vs regional content-commerce
- **Bundled services:** payments/wallet, installments, delivery tracking, subscriptions, in-store pickup, agentic shopping assistants
- **Delivery form:** mobile app vs web; standalone vs layer inside a payments app or content platform

### L3 — Vendor-specific (research notes only)

- Shop: Shop Minis, Shop Cash, Shop Pay Installments, Shop offers, conversational search limited to US/Canada, one-store-per-checkout rule, marketplace sales tax handling, "Shop App for ChatGPT" agentic path, profile-hidden-until-first-public-collection rule
- Thingtesting: Thingtesting Rewards (per-brand cash commission percentages), click.thingtesting.com affiliate redirect, "Claim your brand" self-service
- Klarna: Klarna Membership, WebBank-issued financing, balance account, buyer protection terms

## Historical / Market-Sample Check (§24)

- Older social shopping discovery (Wanelo, Kaboodle, ThisNext) had **no personalization engine and no in-app checkout** — user-saved feeds + outbound links. They fit L0 (multi-source catalog, browse surfaces, acquisition path) without any L1 personalization machinery. → personalization and in-app checkout stay out of L0.
- Polyvore was collage-first (creation tool) with shopping links — still fits L0; suggests creation/collage tools over product records are a variant posture, not a separate core.
- Regional content-first discovery (Xiaohongshu) makes the **content/social layer** clearly a variant, not the core.
- Platform-native commerce layers (TikTok Shop, Instagram Shopping) show the discovery surface can be a byproduct of a content feed — boundary case, recorded below.
- Klarna shows a payments app can host a shopping surface — but its surface is search/compare/offer-led, which is exactly why it reads as the sibling Types rather than this one.

## Vendor-specific Findings

See L3 above. None promoted to the canonical model.

## Boundary Findings

| Neighbor Type | Test that separates them |
|---|---|
| **Shopping Search Engine** | query-first retrieval vs browse-first surfacing. Remove query-independent surfaces (everything is query-driven) → Shopping Search Engine. |
| **Shopping Comparison Platform** | unit is the offer set for a chosen item (price comparison) vs the product record surfaced for inspiration. Klarna's price-comparison layer sits here. |
| **Deal Discovery Platform** | unit is the deal/offer (discount, coupon, cashback event) vs the product record. |
| **E-commerce Platform / Online Store Builder** | operator's own single-seller storefront tooling vs multi-source aggregation. Single catalog source → e-commerce. |
| **Online Marketplace** | marketplace = platform is the transaction venue with unified catalog/fulfillment/seller management; discovery app = discovery layer over independent sellers, transaction thin (redirect) or delegated per-seller (Shop checks out one store at a time; each store remains merchant of record). |
| **Digital Product Catalog (05.04)** | B2B/internal product data management vs consumer-facing discovery. |
| **Content Curation Platform / Bookmark Manager** | unit is a content item/link without structural acquisition path vs product record with commercial linkage. |
| **Review Platform** | reviews are the organizing unit vs product/brand records with acquisition path. Thingtesting is genuinely hybrid (brand discovery + reviews) — recorded as a boundary case, not a misclassification. |
| **Interest-based Social Network / Personalized Content Feed** | social graph/content feed is the core; shopping is a surface (Pinterest, TikTok). When the product record + acquisition path stops being structural, it's the other Type. |

**"Remove what to become the neighbor" summary:** remove browse-first surfacing → Shopping Search Engine; remove multi-source aggregation → e-commerce storefront; remove acquisition path → content curation; make offers/deals the unit → Deal Discovery; make offer-comparison the unit → Comparison Platform; make the transaction venue + unified fulfillment the core → Marketplace.

## Uncertainties

1. **Sample depth:** only two products were documented in depth (Shop, Thingtesting); LTK, Pinterest, and Houzz were unreachable. L1 claims about personalization/social features rest mainly on Shop + qualitative knowledge of the category; they are phrased as common-structure claims, not universals.
2. **Catalog intake mechanics:** how merchant feeds/affiliate integrations work on the supply side was not directly observed (Shopify merchant docs 403). Intake is described conceptually only.
3. **Monetization internals:** commission/ad mechanics are inferred from public disclosures (affiliate note, rewards pages); no rate structures asserted.
4. **Historical products:** not re-verified; used only for the §24 qualitative check.
5. **Type strength:** this leaf could be argued to be a family-level node whose instances (visual discovery, creator-led, brand-review-led) are quite different from each other. Kept as one Type because L0 holds across all sampled instances; flagged for joint review if future siblings (Shopping Search Engine, Deal Discovery) show heavy overlap.

## Final Synthesis

The Product Discovery Application is the **browse-first member of the Shopping Discovery family**: a consumer application whose world is a multi-source catalog of product/brand records, surfaced through query-independent discovery surfaces (feeds, collections, edits, trending, directories), where every product record carries an acquisition path to a seller — in-app checkout or outbound link. Personal accounts, saves, follows, personalized feeds, notifications, reviews, and supporting search are the common mature layer that makes the loop sticky, but none of them is required to recognize the Type. The purchase itself may happen inside the app or after leaving it; what is defining is that discovery, not search, not comparison, not deals, and not the transaction venue itself, is the organizing job.
