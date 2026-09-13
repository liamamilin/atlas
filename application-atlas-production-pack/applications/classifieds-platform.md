# Classifieds Platform

## Overview

A **Classifieds Platform** is a self-publishing advertisement board for trade between private parties and businesses. Posters publish short, time-bound ads, each describing one specific offer or want; ads are filed in categories and tied to a locality; interested parties browse, search, and contact the poster through the platform; and the exchange itself — negotiation, payment, handover or shipping — is completed between the parties as the default.

The defining core is small:

```text
Poster (private individual or business)
  └── Self-published ad (one offer or want, transient, not a catalog entry)
      └── Filed by category × location
          └── Contact from interested party to poster
              └── Exchange arranged between the parties
```

Everything else commonly associated with modern classifieds — in-platform messaging, saved-search alerts, paid visibility boosts, escrow payment and shipping services, professional seller tooling, user reviews — is widespread in current products but is not what makes the product a classifieds platform. Print-newspaper classifieds and the earliest web classifieds satisfy the defining core without any of those additions, and today's products still support the pure form: meeting in person and paying privately remains a normal, supported outcome.

The boundary against marketplaces follows directly: a marketplace intermediates the transaction (order, payment, protection, dispute handling inside the platform, with off-platform completion treated as a violation). A classifieds platform's defining role ends at publishing the ad and connecting the parties. Where a classifieds product does offer payment and shipping, these are optional services attached to eligible ads — and the ad-contact model remains the center.

## Users & Context

**Posters** — the supply side:

- private individuals selling used goods, giving items away, renting out rooms or apartments, offering services (tutoring, repairs, moving, pet care), rehoming animals, or posting "wanted" ads seeking items
- professional sellers posting at volume under business identities: vehicle dealers, real-estate agencies and landlords, employers posting job offers, retailers and workshops with recurring stock, service businesses

**Responders** — the demand side: buyers, renters, job seekers, and clients who browse categories, search, save searches, and contact posters.

**Operators** — moderation and trust-and-safety functions that review ads and reports, remove violating content, and restrict accounts.

The work context is local trade between strangers who cannot trust each other by default: a seller and a buyer for a used car, a landlord and a tenant, an employer and a candidate. The platform surfaces supply and provides the contact channel; the high-trust part of the exchange happens in person or, where offered, through an optional protected-payment service. Web and mobile apps are both primary surfaces; posting and replying are mobile-heavy, while browsing larger purchases (cars, real estate) often happens on larger screens.

## Core Model

### The Ad

The ad (listing) is the central object of the system. It is authored by the poster, describes exactly one offer or want, and is composed of:

- a title and description that must describe the actual item or service
- photos or other media representing the item
- a price — where a price makes sense; some categories (give-aways, many services, job offers) legitimately have no price field
- category-specific attributes (brand, model, mileage and registration status for vehicles; surface, energy-performance data for real estate; condition for goods)
- a category placement and a location
- the poster's identity behind it

Two structural properties distinguish the ad from a marketplace product page:

- **One ad = one offer.** An ad describes a single item or service. Multi-item "everything in our shop" ads are rejected by posting rules. There is no inventory depth behind an ad: when the item is gone, the ad is marked sold or deleted, not decremented from stock.
- **Ads are transient.** An ad runs for a defined period and then expires unless renewed. It can be paused, edited, deleted, or restored within limits. The board is a flow of current offers, not a persistent catalog.

### Category and Location

Ads are filed in a category vocabulary that spans the whole local-trade space: goods and furniture, electronics, clothing, vehicles, real estate (sales and rentals), vacation rentals, jobs, services, animals, professional equipment, and a general "other". Mature products maintain deep category trees with per-category attribute filters. Alongside the category, every ad carries a location — a city or region — and discovery is organized around both axes together: browse vehicles in a region, apartments in a city, jobs near a locality. Radius search and map views extend the location axis.

### Poster and Responder

Every ad sits on a poster identity. The private/professional distinction is structural: professional posters are identified as businesses (posting rules typically require business registration to be declared), get different tooling and limits, and are restricted from or charged for categories reserved for private individuals. Responders are typically light-identity users: they browse, favorite, save searches, and contact posters without ever creating supply.

### Conversation

Contact between responder and poster happens through a messaging channel bound to the ad. This conversation is where negotiation happens — price offers, questions, appointment arranging. Posting rules commonly prohibit contact information (phone numbers, email addresses) inside the ad text precisely to keep the exchange on the platform channel, where moderation and scam protection operate.

### Optional Transaction Service

Where a product offers payment and shipping, the service attaches to an eligible ad as an optional layer: the responder pays through the platform, funds are held until the item is received or the parties otherwise settle, and a shipping label flow covers distant trade. An order-like object exists only inside this optional service — it is not the platform's default structure, and ads that are not eligible (or parties who prefer it) simply transact outside it.

### Moderation State

Every ad carries a moderation state: pending or scheduled before appearing, active, hidden or removed for rule violations, expired, or marked sold by the poster. Accounts themselves can be restricted, which blocks posting or replying.

```text
Poster (private / professional)
  ↓ authors
Ad (one offer or want; title, description, photos, price, attributes)
  ↓ filed in
Category × Location
  ↓ discovered by
Responder (browse / search / saved-search alerts / favorites)
  ↓ contacts through
Conversation bound to the ad
  ↓ arrangement between the parties
Exchange (meet-up & private payment — or optional platform payment + shipping)
  ↓ outcome
Ad marked sold / renewed / expired / removed
```

## How It Works

### Post an ad

```text
Choose the category that matches the offer
→ describe the item (title, description, photos, attributes)
→ set price (where applicable) and location
→ publish (free for most private categories; some categories or options are paid)
→ moderation check → ad goes live
→ manage over time: edit, renew before expiry, boost visibility,
  pause while away, mark as sold, delete
```

Posting is a guided multi-step flow, and the category choice drives everything downstream: which fields appear, which rules apply, whether posting costs money, and whether the ad can use transaction services.

### Find an ad

```text
Browse by category and location (or search directly)
→ filter by attributes, price, radius
→ save the search → receive alerts when new matching ads appear
→ favorite candidates
→ open the ad detail page
```

Discovery is organized around the category × location axes; search and saved-search alerts sit on top. Because ads are transient and new supply arrives continuously, saved-search alerts are a first-class mechanism rather than an add-on.

### Contact and arrange

```text
Contact the poster through the platform messaging
→ ask questions, negotiate price, propose an appointment
→ complete the exchange:
   · meet in person and pay privately (the default model), or
   · use the platform's optional payment + shipping service where the ad is eligible
→ poster marks the ad as sold (or deletes it)
```

The platform's job ends at the connection. What happens next — inspection at the meet-up, cash payment, handover — is the parties' affair. This is why trust-and-safety guidance (meet in safe public exchange zones, verify the item before paying, never send deposits to strangers) is a standard part of these products rather than an afterthought.

### Keep the marketplace safe

```text
See a suspicious ad or message → report it
→ moderation reviews → ad removed / account restricted
→ scam-education content and warnings circulate continuously
```

Because the platform connects strangers for high-value exchanges it does not control, moderation, reporting, account restrictions, and continuous scam-alert communication are core operating behavior, not optional features.

### Operate as a professional

```text
Register a business account (identified as professional)
→ post at higher volume / via feeds from external systems
→ buy visibility products (highlights, boosts, top placements)
→ manage a storefront or subscription
→ in some products: use the protected transaction service at pro terms
```

Professional posters are the commercial engine of the category: dealers, agencies, employers, and shops pay for visibility and tooling while private posting stays predominantly free.

### Capability tiers

**Defining core** — without these, not a classifieds platform:

- self-published ad describing one offer or want
- category-and-locality filing with browse/search discovery
- contact channel from interested party to poster
- exchange completed between the parties as the default

**Standard capabilities** — present across mature products:

- time-bound ad lifecycle (renewal, pause, mark-sold, deletion, drafts)
- ad-bound messaging as the sanctioned contact channel
- saved searches with new-result alerts; favorites
- search filters over category attributes, price, and radius
- reporting/moderation with prohibited-item rules and account restrictions
- paid visibility products (highlight/boost)
- private vs professional account distinction
- photos and per-category attributes; price field with defined no-price categories

**Optional capabilities** — product- and market-dependent:

- platform-operated escrow payment, shipping, and buyer protection for eligible ads
- identity verification services
- paid posting for select categories
- professional storefronts, subscriptions, feed integrations, resume databases
- user reviews/ratings of counterparties
- value-added services (vehicle valuation, financing referral, tenant dossiers, booking for vacation rentals)
- AI assistance (ad-description drafting, moderation automation)

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Category / location browse (home)

The entry surface: top-level categories (goods, vehicles, real estate, jobs, services…) crossed with a location selector (region → city). Purpose: orient the user in the local supply space. Primary actions: pick a category × location, or enter a search.

### Search results list

The main consumption surface: a scrollable list of ad cards (photo, title, price, location, age) with filters (attributes, price range, radius) and sorting. Primary actions: refine, save the search, favorite an ad, open one.

### Ad detail page

The decision surface for one offer: full photo set, description, attributes, price, location, posting date, and the poster's identity (private/professional, profile, reviews where present). Primary actions: contact the poster, favorite, share, report the ad; where eligible, buy with the protected payment service.

### Posting flow

A multi-step form: category → description → photos → attributes → price → location → (optional paid options) → review → publish. Primary actions: save draft, preview, publish.

### My ads dashboard

The poster's management surface: all own ads with their states (active, scheduled, paused, expired, sold), expiry dates, and per-ad actions (edit, renew, boost, mark sold, delete, restore where supported).

### Messages

The conversation surface: threads bound to ads, negotiation, appointment arranging, and — where the product offers it — the entry point for protected payment and shipping actions. Primary actions: reply, make an offer, report the counterpart.

### Account / profile

Identity and settings: private vs professional account type, personal data, notification preferences, blocked users.

### Business surfaces

Professional posters get additional surfaces: bulk ad management, storefront/shop pages, subscription and billing management, and in some products recruiting or listing-feed tools.

### Transaction surfaces (where offered)

Checkout for an eligible ad, shipping-label flow, wallet or payout view, and a dispute/cancellation surface — the order-like layer that exists only inside the optional transaction service.

## Important Rules / Behaviors

### One ad, one item, no duplicates

Posting rules require each ad to describe a single item or service, and prohibit running duplicate ads for the same offer: to repost, the poster must first delete the existing ad. This keeps the board a flow of distinct current offers rather than an accumulation of stale entries.

### Ads are time-bound

An ad runs for a defined period and then expires, dropping out of search. Renewal (sometimes paid) extends the run; some products allow restoring recently deleted ads, while expired ads generally cannot be reactivated. Pausing for absence is a standard poster control.

### Contact stays on the platform

Contact information (phone numbers, email addresses) inside ad text is commonly prohibited; the ad-bound messaging channel is the sanctioned contact route. The reason is safety: off-platform contact is where payment scams live. Products warn continuously about off-platform payment offers — typically framed as "outside our protection" rather than as a rule violation, because the parties completing the exchange privately is the model, not an abuse of it.

### The exchange is the parties' responsibility — by default

The platform publishes the ad and carries the conversation; it does not guarantee the item, hold the money, or ship the goods unless an optional transaction service is used. Where such a service exists, it applies only to eligible ads and categories, has a defined geographic scope, and adds buyer protection (funds held until receipt; dispute handling for non-conforming items). In-person sale with payment settled at the meeting remains a supported, first-class mode.

### Category-specific rule layers

Categories carry their own rule sets, often reflecting legal requirements: job offers restricted to identified employers with anti-discrimination language rules; used vehicles requiring registration documents and mileage disclosure; real-estate ads carrying energy-performance and rent-regulation disclosures and restricted to owners or licensed intermediaries; animal ads governed by welfare policies. Professionals are excluded from some categories entirely.

### Professional identification

Ads posted on behalf of a business must be identified as professional (business registration declared). The private/professional split also drives limits: private posters face per-category caps on concurrent ads; professionals post at volume under business accounts.

### Moderation has teeth

Prohibited-item lists (weapons, drugs, counterfeits, protected species, and more), content rules (language, links, keyword stuffing), and automated plus human moderation enforce the board's integrity. Violating ads are removed or dereferenced; repeat offenders face account restrictions that block posting or replying. Users can report ads and counterparts directly from the ad page and the conversation.

### Visibility is purchasable; ranking is rule-governed

Organic ranking follows published rules (recency, category fit, completeness), and posters can buy visibility — highlights, boosts, top placements. Paid visibility is a primary revenue mechanism alongside paid categories and professional subscriptions.

### Location is bound at posting

The ad's location is set when posting and is not freely editable afterwards; posting in the wrong location is a known, supported-issue class rather than a casual setting.

## Variants

- **Newspaper-heritage minimalism** — the pure board: categories, ads, contact, nothing else; the exchange is entirely off-platform. The founding shape of the Type, still visible in the simplest products.
- **Transaction-service-heavy hybrids** — mature products that productize escrow payment, shipping, and buyer protection for eligible ads, moving part of the exchange on-platform while keeping the ad-contact model primary.
- **Free-posting C2C boards vs paid-category models** — the free/paid boundary varies by market: predominantly free private posting with paid options and select paid categories is the common pattern; some markets charge for high-value categories (vehicles, real estate, jobs).
- **Private-only vs strong professional ecosystem** — products range from consumer-only boards to platforms where dealers, agencies, and employers are the economic center with dedicated tooling and storefronts.
- **Horizontal generalist vs verticalized groups** — the generalist carries all categories in one product; operator groups frequently spin high-value verticals (cars, real estate) out into standalone brands while keeping the horizontal generalist.
- **Regional regulatory depth** — posting rules embed local law to varying degrees: business-registration identification, energy-performance disclosures, rent regulation, vehicle documents, media age ratings.
- **Mobile-first local-trade apps** — the same core model delivered as a phone-native experience with chat-first contact and meet-up orientation.

A variant remains a variant as long as the ad-contact model holds. When the mediated transaction becomes mandatory — every sale must flow through platform order, payment, and dispute machinery — the product has become a marketplace, not a variant of this Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Online Marketplace / Multi-vendor Marketplace | closest boundary | marketplaces intermediate the transaction (catalog, cart, order, payment, fulfillment) and run merchant inventory; classifieds publish transient self-published ads and leave the exchange to the parties |
| Resale Marketplace | adjacent (second-hand focus) | resale marketplaces center the in-platform order + payment + dispute machinery for pre-owned goods; off-platform completion is a violation there, while it is a normal outcome here |
| Listing Marketplace | sibling leaf | same family; the observed market spans a pure ad-contact pole and a transaction-service-heavy pole — the division of labor between the two leaves deserves joint review |
| Directory Application / Listings Platform | adjacent | directories hold persistent reference listings for lookup; classifieds hold transient trade offers with contact-to-transact intent |
| Job Board | vertical relative | jobs are historically a classifieds category; the dedicated job board adds candidate-side machinery (profiles, resumes, applications, employer tooling) that classifieds lack |
| Property Listing Platform | vertical relative | real estate is a classifieds category; dedicated property platforms add agent tooling, listing depth, and transaction support |
| Service Marketplace | adjacent | service marketplaces center persistent, profiled provider supply with booking and review machinery; in classifieds the ad itself is the supply |
| Review Platform | adjacent | reviews are the object of a review platform; in classifieds, reviews (where present) are a trust layer over the ad-contact model |
| Online Auction Platform | adjacent | auctions center price discovery through bidding; classifieds center the ad with fixed or negotiable pricing |

The boundary with the marketplace family is the most important one, because modern classifieds increasingly offer payment and shipping. The structural test: if completing the exchange off-platform (meet-up, private payment) is a normal supported outcome, the product is a classifieds platform; if it is a rule violation because every transaction must flow through the platform, the product is a marketplace.

## Representative Products

- **Leboncoin** (France) — mature hybrid: free private classifieds core, escrow transaction service with delivery for eligible ads, deep professional ecosystem, extensive published posting/ranking rules
- **Kleinanzeigen** (Germany) — classic free C2C board with optional escrow payment ("Sicher bezahlen"), rich ad-lifecycle management, separate commercial tier
- **Subito** (Italy) — generalist with a platform shipping service, business storefronts, and premium/gamification layers
- **Kijiji** (Canada) — North American classifieds with paid ad promotion, user reviews, and community-based safety education
- **OLX** (global, emerging-markets core) — multi-country local classifieds brands with large paid-lister populations and spun-off vertical brands

The defining core was checked for era, region, and positioning spread: the print-newspaper classifieds model and the early web city-board archetype satisfy it without any modern capability, and the researched products span free-posting, paid-category, transaction-service, and professional-ecosystem poles.

## Sources

Research date: **2026-09-07**

- Leboncoin — homepage: https://www.leboncoin.fr/
- Leboncoin — Help Centre (consumer & professional): https://assistance.leboncoin.info/hc/fr
- Leboncoin — Règles de référencement, de déréférencement et de classement des annonces: https://www.leboncoin.fr/dc/rules
- Kleinanzeigen — Help Center: https://hilfe.kleinanzeigen.de/hc/de
- Kleinanzeigen — "Anzeigen" help category: https://hilfe.kleinanzeigen.de/hc/de/categories/17006957523740-Anzeigen
- Kleinanzeigen — "Was ist „Sicher bezahlen"": https://hilfe.kleinanzeigen.de/hc/de/articles/17211553583388
- Kleinanzeigen — "Wie lange ist meine Anzeige online?": https://hilfe.kleinanzeigen.de/hc/de/articles/17082474526236
- Subito — homepage and service structure: https://www.subito.it/
- Kijiji — Community Connect help (Getting Started, My Account): https://help.kijiji.ca/
- OLX Group — corporate site: https://www.olxgroup.com/

> Sourcing limitation: several major classifieds products could not be reached from the research environment on 2026-09-07 (Craigslist and Locanto returned access-denied responses; Gumtree and Marktplaats help desks are JavaScript applications that do not render; OfferUp timed out; OLX country help sites and Avito were unreachable or rate-limited). The researched sample therefore skews toward European products plus one North American and one global group. Claims about the unreachable archetype and mobile-first products are kept at structural-inference strength; precise operational details (ad durations, fees, limits) are stated only where directly evidenced, and exact figures remain in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
