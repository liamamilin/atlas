# Destination Discovery Application

## Overview

A **Destination Discovery Application** is a traveler-facing application that answers the question "where should I go?". Its world is organized around **destination records**: persistent, identified entries for places a traveler might go — countries, regions, cities, islands, national parks, coastal areas — each carrying visiting-oriented content about what the place is like and what a visitor can see and do there. These records are held together in a **multi-destination catalog** organized so that candidates can be found across destinations, and the whole structure exists to move the user from inspiration to an evaluated choice or shortlist.

The defining structure is small:

```text
Destination (a place a traveler might go)
└── Visiting-oriented record content
    └── Multi-destination catalog
        └── Organized for finding candidates across destinations
            └── Used to reach a where-to-go decision / shortlist
```

Everything else commonly present in current products — map exploration, places-of-interest records, photo galleries, curated best-of lists, seasonal and interest collections, personal save lists, editorial articles, hand-off links to planning and booking — is standard equipment, not part of the definition. The core survives even in non-software form: printed destination guidebooks organized by the same destination taxonomy carry the same structure without an app, a map, or personalization.

When the primary record shifts — to a day-by-day trip itinerary, to reviews of specific hotels and attractions, or to priced bookable inventory — the product has crossed into a different Application Type (Travel Itinerary Planner, Travel Review Platform, or a booking Type).

## Users & Context

The primary user is an individual traveler (occasionally a couple or group deciding together) in the **pre-trip phase**: they hold an open or partly formed travel goal — a free week, a general region, an interest — and are deciding where to go and what is there.

Typical reasons to open the application:

- browse for inspiration ("where should we go this season?")
- compare candidate destinations against each other
- evaluate a specific place: what it is like, what there is to see and do
- collect candidates into a shortlist for a timeframe or an interest

A second usage context is mid-planning: users who have already chosen a destination consult its record — and the places within it — as reference material while building an itinerary, often inside the same product that plans the trip.

Users read the catalog; they do not author it. Records are produced by editors, aggregated from open data sources, contributed by other travelers, or maintained by communities — the reader's own acts are evaluating, saving, and discarding candidates. Products that add a user-contributed guide layer on top are a variant, not the base model.

## Core Model

### The Defining Core

Three properties. Remove any one and the product stops being recognizable as this Type:

- **Destination as the primary record.** A persistent, identified entry for a place a traveler might go. The granularity is *travel-scale*, not administrative: mature catalogs mix countries and cities with regions, islands, national parks, and coastal areas, because those are the shapes in which people actually choose where to go.
- **Visiting-oriented content.** The record exists to help someone evaluate the place as a travel candidate: what it is like, its highlights, what can be seen and done there, supported by media and practical visiting information. This is what separates a destination record from a business-directory entry, which exists for contact and routing.
- **A multi-destination catalog organized for decision-making.** Many such records held together and organized for finding candidates *across* destinations — browse by geography, search, curated collections. And the orientation is a decision: the loop ends in a choice, a shortlist, or a hand-off — not in a booking transaction, and not in a day-by-day plan.

The removal tests, in natural terms:

- strip the catalog down to one destination → a single-destination tourism or marketing site
- replace visiting orientation with contact/reach information → a directory
- end the loop in priced inventory and transaction → a booking platform
- replace destination records with free-form articles as the record → travel media

### Standard Capabilities

Mature products commonly add, on top of the core:

- **Geographic hierarchy browse** — continent/region → country → city as the catalog spine.
- **Search** over destinations and places.
- **Map presence** — map-based exploration, or at least each record's location on a map; map-first in app-style products.
- **Places-of-interest layer** — attractions, museums, parks, viewpoints, neighborhoods, restaurants carried as records within (or alongside) their destination; commonly the catalog's second record layer.
- **Media** — photo galleries as part of record content.
- **Practical visiting information** — addresses, opening hours, official website links on place records.
- **Curated collections** — editors' picks, trending/popular selections, sometimes an annual best-of list.
- **Seasonal axis** — "where to go this season" / destination-by-month framing.
- **Interest axis** — collections by travel style or theme (beaches, adventure, food and culture).
- **Save / shortlist** — capturing candidates into personal lists (favorites, bucket lists) for later.
- **Hand-off seam** — links or flows onward to trip planning and/or booking, sometimes native to the same product, sometimes external.
- **Editorial layer** — articles and guides attached to destinations ("best places to visit…", "when to visit…").

### One Structure, Many Realizations

The core model is written in conceptual terms. Products realize it differently:

```text
Concept:      Destination record
Realizations: structured database entry, editorial destination page, printed guidebook section

Concept:      Catalog organization
Realizations: geographic hierarchy, search index, interactive map, curated collections

Concept:      Content supply
Realizations: professional editors, aggregated open data with in-house curation,
              user-contributed guides, community maintenance

Concept:      Places of interest
Realizations: place database entries, sections inside guides, mentions inside articles
```

A reader who has only seen one realization — say a map-first app over a structured place database — should still recognize a magazine-style destination site, or a print guidebook series, as the same Type.

## How It Works

### The discovery loop

```text
Enter the catalog
→ surface candidates (browse / search / map / curated collections)
→ open a destination record and evaluate
→ narrow: save candidates, drop the rest
→ hand off to planning or booking
```

**Surface candidates.** The user enters the catalog through one of its doors: browsing the geographic hierarchy, searching by name, exploring a map, or following a curated surface — trending picks, a seasonal collection, an interest collection, an annual best-of list.

**Evaluate.** Opening a destination record presents the visiting-oriented content: an overview of the place, its highlights, things to see and do, photos, and practical visiting information. Places of interest within the destination — attractions, museums, parks, neighborhoods — are typically listed and individually viewable, giving evaluation a second level: not only "is this place for me?" but "is there enough there for my trip?".

**Narrow.** The user captures promising candidates — saving them to a shortlist, favorites, or a bucket list — while discarding the rest. The saved set is the loop's working output.

**Hand off.** The loop closes on a decision. The application then hands off: to trip planning (turning saved candidates into an itinerary — natively, when the same product plans trips, or by link), to booking (tours, hotels, transport — again natively or via external links), or simply to the user's own next steps. When a product also prices inventory or builds itineraries, those are adjacent structures; the destination-discovery part of the product ends at the decision.

### How the catalog exists

The catalog is read-mostly for the end user. Records come into being and stay current through a content regime chosen by the operator: professional editorial production, aggregation of open data sources with in-house curation, user-contributed guides, or community maintenance. The regime is a variant; what does not vary is that the user of the catalog is not its author.

## Interfaces

The surfaces below are described conceptually; exact layouts and names vary by product.

### Destinations hub / catalog browser

The entry surface of the catalog.

- Typical information: the geographic hierarchy (regions → countries → cities), curated collections, seasonal and interest rails, search.
- Primary actions: browse by region or country, search, open a collection, open a destination.

### Destination page

The record surface for one place.

- Typical information: overview content, highlights, things to see and do, photos, practical visiting information, places of interest within the destination, related editorial.
- Primary actions: read and evaluate, open a place of interest, save to a list, follow a hand-off link (plan a trip, book something).

### Place-of-interest record

The second record layer: one attraction, museum, park, viewpoint, or neighborhood.

- Typical information: description, photos, location on a map, practical visiting information, its destination context.
- Primary actions: read, save, view on map, add to a plan where planning is native.

### Curated collection / list surface

The editorial rails of the catalog.

- Typical information: a themed or seasonal selection of destinations with short evaluative blurbs.
- Primary actions: browse, open a destination.

### Map exploration

A spatial door into the catalog; the primary surface in map-first products.

- Typical information: places and destinations positioned geographically.
- Primary actions: pan and zoom, inspect a place, save it.

### Saved lists / shortlist

The user's capture surface.

- Typical information: the destinations and places the user has saved.
- Primary actions: review, remove, move a saved item into planning.

## Important Rules / Behaviors

- **The loop closes on a decision, not a transaction.** Booking links and planning hand-offs are seams out of the catalog, not the record. A product whose center of gravity is priced inventory or a day-by-day plan is a different Type with a discovery layer, not this Type with a booking layer.
- **The destination is a travel-scale place.** Catalogs mix administrative and non-administrative destinations freely; "destination" means a place people choose to go, not a census unit.
- **Places of interest are subordinated to destinations.** Attractions and things-to-do are commonly carried as a second record layer, presented within the destination's context rather than as the catalog's primary axis.
- **Users capture; they don't author.** The normal user action on records is saving and discarding. Products that let users author guides add a contribution layer on top; the catalog itself remains operator-maintained.
- **Content currency is part of the product.** Records describe a changing world (places open and close, practical information drifts), so catalogs are maintained over time under their content regime.
- **The shortlist is the working output.** The personal saved set is the artifact the discovery loop produces, and it is what feeds the hand-off to planning.

## Variants

- **Content regime** — structured place databases (aggregated open data plus editors), professional editorial production, user-contributed guides, community-maintained wiki-style catalogs.
- **Surface philosophy** — map-first mobile apps, catalog-first websites, article-first media sites in which the destination record structure is lighter.
- **Coverage scope** — global catalogs spanning the world's destinations vs regional or niche catalogs (a single city, one country, one travel style).
- **Planning attachment** — some products natively include a trip planner; the discovery layer then serves the planner's explore phase. When the trip becomes the primary record, the product has drifted toward the Travel Itinerary Planner Type.
- **Booking attachment** — bookable tours, tickets, or hotels in-plan, or affiliate/external booking links. When priced inventory dominates, the product drifts toward marketplace and booking Types.
- **Reviews layer** — some products integrate ratings and reviews into destination and place records; in review-first platforms, reviews are the record and destination pages are context.
- **Personalization / AI** — matching destination ideas to the user, AI-generated trip ideas, AI-assisted place research.
- **Language breadth** — record content in one language vs many.
- **Business model and operator** — freemium app subscriptions, advertising-funded media, commerce (guidebooks, bookable trips), affiliate income. Commercial vendors, publishers, and in principle tourism bodies all operate such catalogs — a single-destination official tourism site is the degenerate one-record case, not the Type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Travel Itinerary Planner | the planner's primary record is the trip/itinerary (days, routes, bookings); this Type's primary record is the destination in a catalog. The closest seam — discovery commonly ships as the explore layer of a planner |
| Travel Review Platform | the primary record is reviews/ratings of specific supply (hotels, restaurants, attractions); destination pages there are aggregation context |
| Online Travel Agency / Flight Search / Hotel Search / Vacation Rental | priced inventory and transaction; destination discovery holds unpriced place records and ends in a decision |
| Tour & Activity Marketplace | bookable experiences are the record; places of interest here are unpriced candidates |
| Travel content publishing (travel blogs, travel media) | the article is the record and the corpus is the product; here the destination is the record and articles are a supporting layer. Hybrid products blend both; the destination-organized catalog layer is the distinguishing structure |
| Directory Application | structured place/entity entries exist for contact and routing; destination records exist for the where-to-go decision, and the catalog is travel-scale and cross-geography |
| Map / Navigation application | geography- and route-first (get to a known target); destination discovery is decision-first (choose the target) |
| Destination Management Company Platform | operator-side B2B systems for running ground-operation businesses; traveler-side discovery here — name similarity only |

The boundary with the Travel Itinerary Planner is the most important one, because the two overlap heavily in today's market. The structural test is the primary record: remove the trip/itinerary machinery and a destination catalog still stands (still this Type); remove the destination catalog and only a trip workspace remains (a planner).

## Representative Products

- Tripomatic (formerly Sygic Travel) — structured global place database with map-first exploration, attached to a trip planner
- Wanderlog — trip planner whose explore layer combines destination browsing with user-shared guides
- Lonely Planet — publisher-heritage destination catalog with curated collections; the same destination taxonomy also organizes its printed guidebooks
- Touropia — editorial travel-content site at the light end of the Type: destination listicles over a geographic taxonomy

In the current market this Type most often appears as the explore layer of broader travel products (planners, review platforms) and in standalone destination-guide media; the sample covers both shapes.

## Sources

Research date: **2026-09-07**

- Tripomatic — https://www.tripomatic.com/en/destinations , https://www.tripomatic.com/en/features/places-to-visit , https://support.tripomatic.com/
- Wanderlog — https://www.wanderlog.com/ , https://wanderlog.com/guides
- Lonely Planet — https://www.lonelyplanet.com/destinations
- Touropia — https://www.touropia.com/

> Sourcing limitation: several additional products representing the review-platform pole and the community-wiki / local-guide poles were not reachable during research (Tripadvisor, Culture Trip, Wikivoyage, Visit A City, Spotted by Locals). No claims are made about those products; their structures are covered only indirectly through the reachable sample. Help-center-level operational detail (catalog sizes, save-semantics internals, personalization mechanics) was not reachable for most sampled products, so no precise numbers, limits, or default values are asserted in this document. Detailed product-by-product observations and the cross-product comparison are recorded in the paired Research Notes.
