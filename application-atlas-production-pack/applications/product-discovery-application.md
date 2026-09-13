# Product Discovery Application

## Overview

A **Product Discovery Application** is a consumer-facing shopping application whose primary job is to help shoppers find products they did not set out to look for. It aggregates product and brand records from many sellers, surfaces them through browse-oriented surfaces — personalized feeds, curated collections, trending lists, brand directories — and attaches a route to acquisition to every product record, either an in-app checkout or a link out to the seller.

The defining core is small:

```text
Multi-source product catalog
└── Query-independent discovery surfaces (feed / collections / edits / trending)
    └── Product record with an acquisition path (in-app checkout or outbound link to a seller)
```

Remove any one property and the product becomes a different kind of application: make everything query-driven and it becomes a shopping search engine; keep only one seller's catalog and it becomes a storefront; drop the acquisition path and it becomes content curation.

Everything else commonly associated with this category — personal accounts, wishlists, followed brands, personalized recommendations, price-drop alerts, reviews, in-app payment — is widespread in current products but is not what makes the application a discovery application. Older social shopping products and regional content-commerce products fit the definition without most of those specifics.

## Users & Context

The primary user is an individual shopper in a browsing or mixed-intent mode: killing time and open to inspiration, looking for a gift without a specific item in mind, keeping up with brands they like, or researching a category before buying. The session typically starts without a query — the user opens the app to see what is there.

Secondary participants shape the catalog and the curation:

- **sellers and brands** — supply the product records, and in some products manage their own presence (claim pages, post new arrivals)
- **community members and creators** — write reviews, save products into shared collections, or curate picks that other shoppers browse
- **editors** — in some products, maintain curated edits, gift guides, and best-of lists

The dominant surface is the mobile app; web clients usually mirror the same catalog and surfaces.

## Core Model

### The Defining Core

Three structures. If any one is missing, the application is no longer recognizable as a product discovery application:

- **Multi-source product catalog** — the application's world is a catalog of product (and/or brand) records drawn from many sellers, merchants, or brands. The application is not any single seller's storefront; it aggregates. The catalog is the raw material everything else operates on.
- **Query-independent discovery surfaces** — the primary interaction is browsing surfaces that decide what to show without being asked: a personalized home feed, curated collections and edits, trending and best-of lists, category and brand directories. Products reach the user even when the user has not expressed a specific want. Search may exist, but as a supporting surface, not the organizing principle.
- **Acquisition path on every product record** — each product record carries the commercial context needed to act on it (price, seller or brand, availability) and a route to obtain it: an in-app cart and checkout, or an outbound link to the seller's own site. The application may or may not host the transaction itself, but shopping intent is structural, not incidental.

### Standard Capabilities

Mature products commonly add a personal layer and a curation layer on top of the core. These make the discovery loop sticky, but they are not what defines the Type:

- **Personal shopping context** — an account with saved products (favorites or wishlists), followed brands or stores, and accumulated browsing and purchase history. This context is both a convenience (find things again) and the fuel for personalization.
- **Personalized feed** — a home feed that mixes recommendations based on activity, new arrivals and posts from followed sources, recently viewed items, updates on saved items (price drops, back-in-stock), reorder suggestions, and promotional offers.
- **Recommendation controls** — user-visible ways to tune what is surfaced, such as marking an item as not interested or asking for similar items, plus explicit preference inputs (sizes, categories, people you shop for).
- **Supporting search** — keyword search over the catalog with filters; some products add conversational or assistant-style search where the user describes what they want in natural language.
- **Curation structures** — groupings of product records: user-created collections (private or public, sometimes with invited collaborators), editorial edits and gift guides, trending and best-of lists, category trees.
- **Notification loop** — alerts that pull the user back: price drops on saved items, back-in-stock, updates from followed sources.
- **Reviews and community signals** — ratings, written reviews, and community content that help shoppers judge what they discover.
- **Trust surfaces** — seller ratings, reporting mechanisms, and buyer-protection information where the application hosts or intermediates the transaction.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:            Multi-source catalog
Implementations:    platform-ecosystem stores, merchant data feeds,
                    open-web affiliate links, community-submitted brands

Concept:            Discovery surface
Implementations:    activity-personalized feed, editorial edits,
                    creator picks, community-saved boards, trending lists

Concept:            Acquisition path
Implementations:    in-app cart + checkout, outbound link to the seller,
                    compare-then-redirect to a store
```

## How It Works

### The discovery loop

The application's central cycle runs continuously:

```text
Products enter the catalog from connected sources
→ discovery surfaces select and arrange what to show
→ the shopper browses, saves, follows, reacts
→ activity feeds back into what the surfaces show next
→ the shopper acts on a product (checkout in-app, or tap out to the seller)
→ post-purchase, the record returns as history, review material, or reorder suggestion
```

### Catalog intake

Products enter from the sources the product is built on: stores connected through a commerce platform, structured merchant feeds, affiliate-linked listings from across the web, or community-submitted and brand-claimed pages. The intake mechanism determines what the catalog covers — an ecosystem catalog covers its platform's stores; an affiliate catalog covers whatever the web offers.

### Browsing and engaging

The shopper opens the app and lands on a discovery surface — typically a personalized feed or a set of curated rails. From there:

```text
Browse feed / collections / trending / categories
→ open a product or brand record
→ save it (optionally into a collection), follow its source, or share it
→ keep browsing; the feed adapts
```

Saves and follows are not just bookmarks: they subscribe the shopper to a notification loop (price drops, back-in-stock, new arrivals from followed sources) and tune future recommendations.

### Acting on a product

When the shopper decides to buy, the acquisition path takes over. In some products the path stays inside the application: the product goes into a cart, checkout collects payment and shipping, and the order appears in an orders area with tracking. In others the path leaves the application: the shopper taps through to the seller's own site and completes the purchase there. Both are first-class patterns; neither is more defining than the other.

### After the purchase

Where the application hosts checkout, it commonly keeps the post-purchase thread: order status, delivery tracking, and the option to review the product. Reviews then feed back into the discovery surfaces as community signals. Where the path leaves the application, the post-purchase relationship usually stays with the seller.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Home feed

The primary entry surface.

- a personalized stream of product and brand cards, mixed with curated rails (trending, new launches, edits) and updates from followed sources
- primary actions: open a record, save, follow, hide or refine recommendations

### Product record

The unit the whole application exists to surface.

- imagery, price, seller or brand, availability, description, reviews where present
- primary actions: save, add to cart or tap out to the seller, share, review after purchase

### Brand / store record

The source-side record, one level up from products.

- brand presentation, product listing, rating where reviews exist, follow control
- primary actions: follow, browse its products, contact or report where supported

### Collections / saved

The shopper's personal organization layer.

- saved products grouped into named collections, private or public, sometimes collaborative
- primary actions: create and manage collections, invite collaborators, share, find more ideas

### Search

A supporting surface over the catalog.

- keyword input with filters (category, brand, price where present); some products offer conversational search
- primary actions: search, refine, open a record

### Orders / account (where checkout is hosted)

The post-purchase surface.

- order list, delivery tracking, payment and address settings, personalization preferences, notification settings

## Important Rules / Behaviors

### Discovery is query-independent by design

The organizing behavior of this Type is that products are surfaced without a query. A user can open the app cold and receive a useful stream. Search complements this but does not replace it; if search became the only way to reach products, the application would be a shopping search engine.

### The application is not necessarily the seller

The acquisition path may lead out of the application. Where it does, the application's responsibility typically ends at the handoff — the seller owns fulfillment, payment, and support. Where checkout is hosted in-app, the application (or its platform) takes on transaction responsibilities, but the underlying seller usually remains the merchant of record. Cart and checkout rules vary: for example, some products restrict a single checkout to one seller's items even when the cart spans sellers.

### Personalization is activity-driven and user-manageable

What the feed shows is derived from the shopper's own activity — browsing, saves, follows, purchases — plus explicit preferences. Mature products expose control over this: marking items as not interested, asking for similar items, editing preference settings. Personalization inputs and their visibility to the user differ by product.

### Commercial placement shapes what is surfaced

Discovery surfaces are commercially mediated. Sponsored placements, affiliate links, and rewarded placements are common; some products disclose them (for example, a note that purchases through outbound links may earn the platform a commission). The presence of commercial mediation is structural; its exact form varies.

### Availability and location constrain the catalog

What is surfaced is commonly filtered by practical constraints — whether a store ships to the shopper's location, whether an item is in stock. Saved items commonly carry a monitored state: the application watches for price drops and restocks and notifies the shopper.

## Variants

Common forms of the Type:

- **platform-ecosystem discovery app** — the catalog is drawn from one commerce platform's connected stores; checkout is hosted in-app through the platform's payment layer; delivery tracking and rewards are bundled (e.g. Shop)
- **brand-discovery and review community** — the catalog is brand pages built from community submissions and brand claims; discovery is editorial and community-driven; acquisition is by outbound link; reviews and reviewer rewards are central (e.g. Thingtesting)
- **creator-led shopping app** — curation is supplied by creators/influencers whose picks form the browsable surface; acquisition is typically affiliate-linked
- **visual / collage discovery** — the shopper assembles or browses visual boards of products; acquisition is by outbound link (historical form, e.g. Polyvore)
- **social shopping feed** — products enter the catalog through user saves from across the web; the feed is socially driven (historical form, e.g. Wanelo, Kaboodle)
- **content-first discovery commerce** — discovery happens inside a community content feed with embedded product links; commerce is a layer on content (regional form, e.g. Xiaohongshu)
- **payments-app shopping layer** — discovery is one surface inside a broader money app, organized around stores, offers, and cashback rather than a product feed (e.g. Klarna's shopping surface)

A variant remains a variant as long as the defining core holds. When the transaction venue, the seller's own catalog, or the content feed becomes the organizing structure, the product belongs to a neighboring Type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Shopping Search Engine | query-first retrieval across sellers is the primary interaction; a discovery application surfaces products without a query and treats search as support |
| Shopping Comparison Platform | organized around comparing offers for an item the shopper has already chosen; the discovery application's unit is the product record surfaced for inspiration |
| Deal Discovery Platform | the deal or offer (discount, coupon, cashback event) is the unit; here the product record is the unit and offers are a feed ingredient |
| E-commerce Platform / Online Store Builder | tooling for a seller's own storefront with a single-seller catalog; a discovery application aggregates multiple sellers and does not own the catalog it presents |
| Online Marketplace | the platform is the transaction venue with unified catalog, fulfillment, and seller management; a discovery application is a discovery layer over independent sellers, with the transaction hosted thinly or delegated to each seller |
| Digital Product Catalog | business-side management of product data (PIM-style), not a consumer-facing discovery surface |
| Content Curation Platform / Bookmark Manager | the unit is a content item or link without a structural acquisition path; here every record carries commercial linkage |
| Review Platform | reviews are the organizing unit; here reviews are one signal attached to product records (some products sit genuinely between the two) |
| Interest-based Social Network / Personalized Content Feed | the social graph or content feed is the core and shopping is a surface; here the product record and its acquisition path are structural |

The closest boundaries are the three siblings in the shopping discovery family — search, comparison, deals — and the marketplace. The sibling test is what the user's session is organized around: a query (search), a chosen item's offers (comparison), a discount event (deals), or an open-ended stream of products (discovery). The marketplace test is who owns the transaction: a marketplace is the venue; a discovery application is the path to it.

## Representative Products

- **Shop (Shopify)** — platform-ecosystem shopping destination: personalized feed, follows, collections, in-app checkout via Shop Pay, delivery tracking, rewards
- **Thingtesting** — brand discovery and review community: curated edits, brand pages, community reviews, outbound affiliate links, reviewer rewards
- **Klarna** — payments app whose shopping surface (search, compare, brands, cashback) illustrates the boundary with the search/comparison siblings

Historical and regional forms checked against the definition (qualitatively): Wanelo, Polyvore, Kaboodle, ThisNext (social/visual discovery, 2006–2018 era), Xiaohongshu (content-first discovery commerce), TikTok Shop and Instagram Shopping (content-platform commerce layers), Pinterest (visual discovery with a shopping surface).

## Sources

Research date: **2026-09-06**

- Shop Help Center — Getting started; Discover stores and products; Make purchases in Shop; Save products and follow stores; Manage your Shop profile — https://help.shop.app/en/shop/getting-started , https://help.shop.app/en/shop/shopping/discover , https://help.shop.app/en/shop/shopping/make-purchases-in-shop , https://help.shop.app/en/shop/shopping/discover/save-products-and-follow-stores , https://help.shop.app/en/shop/getting-started/profile
- Thingtesting — About/FAQ and Discover front page — https://thingtesting.com/about , https://thingtesting.com/
- Klarna — Shopping and App pages — https://www.klarna.com/us/shopping/ , https://www.klarna.com/us/klarna-app/

> Sourcing limitation: official documentation for LTK, Pinterest, Houzz, and Shopify's merchant-side Shop channel docs could not be fetched from the research environment (transport errors, timeouts, or access blocks). The documented sample therefore rests on Shop, Thingtesting, and Klarna. Claims about historical and regional products (Wanelo, Polyvore, Kaboodle, ThisNext, Xiaohongshu, TikTok Shop, Instagram Shopping, Pinterest) are qualitative and were not re-verified against live sources; no precise operational details are asserted for them. Precise vendor specifics (reward percentages, regional availability of features, checkout restrictions) are kept out of this document and recorded in the paired Research Notes.
