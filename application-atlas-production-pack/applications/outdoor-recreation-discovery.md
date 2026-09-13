# Outdoor Recreation Discovery

## Overview

An **Outdoor Recreation Discovery** application helps a person **find and choose outdoor recreation opportunities** — places and things to do outdoors such as campsites, trails, peaks, parks, put-ins, huts, facilities, permits, and journey services — through a persistent, map-anchored catalog in which every opportunity is an addressable record carrying the attributes that matter for an outdoor decision: where it is, what it is, how demanding or suitable it is, when it is possible, and what it takes to do it.

The defining structure is small:

```text
Opportunity catalog of record
└── Map-anchored discovery browsing (the map as the working surface)
    └── Decision surface per opportunity (the detail view that informs the go/no-go choice)
```

Everything else commonly associated with these products — community reviews and photos, curated collections and editorial guides, offline maps, favorites and trip builders, freemium subscriptions, navigation, even reservations — is widespread in current products but is not what makes the product a discovery application. Older and non-digital ancestors (regional guidebooks with fold-out maps, printed campground directories, agency park brochures) satisfy the same core without any of it.

The product's center of gravity is the **find-and-choose loop**. Field wayfinding, activity recording, and booking transactions may appear as layers or extensions — but when one of them becomes the center, the product belongs to a neighboring type: a hiking/trail application, a sport tracker, or a booking platform.

## Users & Context

The primary user is an **individual planning outdoor recreation** — a day-tripper choosing a trail, a weekend family picking a campground, a road-tripper or RVer looking for tonight's stop, an overlander provisioning a remote crossing, a cyclist or hiker looking for routes in an unfamiliar region. Two moments dominate:

- **At home, before the trip** — browsing regions, comparing options, saving favorites, building a plan.
- **En route, between stops** — "where can I camp / eat / refuel / hike from here?", often where connectivity is poor.

Secondary participants shape the content rather than the choice:

- **Community contributors** — travelers who add places, write reviews, upload photos and tracks, and file corrections (in community-content products this is the supply side).
- **Official content partners** — agencies and organizations that publish facility and opportunity information (in official-portal products this is the supply side).
- **Moderators** — in community products, experienced contributors who enforce published content criteria.
- **Place owners** — some products let owners add or update their own listing under strict identification rules.

## Core Model

### The Defining Core

```text
Opportunity catalog of record
└── Map-anchored discovery browsing
    └── Decision surface per opportunity
```

Three structures. If any one is removed, the product is no longer recognizable as outdoor recreation discovery:

- **The opportunity catalog of record** — persistent, individually addressable records of outdoor opportunities. A record is a place or a thing-to-do outdoors: a campsite or campground, a trail, a mountain peak, a hut, a lake or put-in, a park facility or individual site, a tour, a permit, or — in journey-oriented products — a service point such as a mechanic, fuel stop, border crossing, or consulate. Each record carries outdoor-relevant attributes: location; activity or category; difficulty, effort, or suitability (including vehicle/rig fit where relevant); season or availability; and practicalities such as access, fees, amenities, and rules. The record outlives any single trip — it is the product's memory of the opportunity, updated over time. Without the catalog there is only a map or a search box.
- **Map-anchored discovery browsing** — the catalog is presented and browsed spatially. The map is a primary working surface, not a decoration: users browse around a destination, along a route, or within a region, and narrow with search and filters across place, activity, and attributes. In paper ancestors this leg is the guidebook's regional map sheet with numbered entries. Without the spatial presentation the product is a text directory.
- **The decision surface per opportunity** — each record renders as a detail view whose job is to inform the go/no-go choice: what it is and how to do it, what it requires or costs, and — where the product's content model provides it — what others experienced (photos, reports, ratings) and what conditions are like. Without this layer the product degrades into bare pins on a map — a map feature, not a discovery application.

### Capabilities Shared by Mature Products

These make discovery practical; they are not what defines the type:

- **Search and filter machinery** — by activity, geography, and outdoor attributes (difficulty, length, amenities, suitability, cell coverage).
- **Curated and editorial layer** — collections, guides, "best of" lists, and inspiration articles that convert a catalog into inspiration.
- **Community knowledge layer** — reviews, photos, tips, check-ins, and condition or correction reports contributed by users, usually under published content criteria and moderation.
- **Personal organization** — favorites, saved lists, trip builders, and a history of contributions.
- **Offline support** — offline maps and downloadable places or routes, because discovery targets places where signal fails.
- **Mobile app as the primary surface**, with web as companion or portal.
- **Freemium subscription commerce** — users pay for tools and coverage (offline maps, planning, alerts), not for the opportunity itself.
- **Contribution machinery** — add a place, upload a track, write a review, report a problem.
- **Hand-off integrations** — send a route to a GPS device, open external navigation, or follow a booking link.

### One Structure, Many Implementations

The core is written conceptually. Products realize each concept differently:

```text
Concept:   Opportunity record
Realized as:  campground listing · trail · peak · park facility/site ·
              tour or ticket · permit · journey service point · community GPS track

Concept:   Content authority
Realized as:  official agency publications · moderated community contributions ·
              curated editorial · in-house data · mixtures of these

Concept:   Map-anchored browsing
Realized as:  interactive web/app maps · category map layers · 3D terrain maps ·
              (paper ancestor: regional map sheet)
```

A reader who has only seen one implementation — say, a community campground-review map — should still be able to recognize an official public-lands portal or a 3D mountain explorer as the same type of application.

## How It Works

### The discovery loop

```text
Frame the search
→ (by region on the map, by country/state browse, by current location, or by activity)
Narrow
→ (filters: activity, difficulty, amenities, suitability, cost, coverage)
Evaluate
→ (open the decision surface: description, parameters, photos, reviews, conditions)
Decide and organize
→ (save to favorites/lists, add to a trip plan)
Hand off
→ (navigate there, book if needed, go do the activity — often in other products or surfaces)
```

The loop's center is the choice. What happens after the choice — walking the trail with turn-by-turn guidance, recording the activity, paying for the campsite — is either left to the user, delegated to another product, or offered by the discovery product as an extension layer.

### The contribution loop (community-content products)

```text
Visit a place or complete an outing
→ contribute: add a place, write a review, upload photos or a GPS track, check in
→ moderators (or published criteria) govern what enters the catalog
→ other users discover through the enriched record
→ places change; users file corrections
```

In community-content products this loop is the supply engine: the catalog exists because travelers keep feeding it. Corrections deserve emphasis — places close, prices change, roads wash out — so "report a problem" and update flows are first-class contributions, not afterthoughts.

### Core vs common vs optional

**Defining core** — without these, not outdoor recreation discovery:

- opportunity catalog of record
- map-anchored discovery browsing
- decision surface per opportunity

**Common mature structure** — present in most modern products:

- search/filter machinery · curated editorial · community knowledge · personal organization · offline support · mobile-first surface · freemium subscriptions · contribution machinery · hand-off integrations

**Variant / optional** — depends on positioning:

- transaction layer (reservations, permits, lotteries) · turn-by-turn navigation · live activity tracking · star ratings · 3D maps · B2B/open-data surfaces

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Map browse surface

The primary entry for spatial discovery.

- pan/zoom map with opportunity markers, often organized in toggleable category layers (e.g., campgrounds, dump stations, peaks, huts)
- cluster or density rendering at low zoom
- primary actions: browse an area, switch categories, open a record, recenter on a location

### Search and filter panel

The structured entry for known criteria.

- location or region input; activity or category selection; attribute filters (difficulty, length, amenities, suitability, price)
- primary actions: apply filters, sort results, switch between map and list views

### Result list / cards

The catalog rendered as scannable entries alongside or instead of the map.

- photo, name, distance, key attributes, rating or community signal where the product has one
- primary actions: open detail, save, compare

### Opportunity detail (the decision surface)

The heart of the product.

- photos, description, attribute summary (difficulty, season, fees, access, amenities), map context
- experiential knowledge where present: reviews, ratings or detailed reports, recent condition notes, community tips
- primary actions: save/favorite, share, navigate, book or follow booking link (where offered), contribute a review or correction

### Curated collections / editorial

Guides, themed collections, and articles that package the catalog into inspiration.

- authored lists of opportunities with narrative context
- primary actions: browse collection, open member records, save the collection

### Personal space

The user's own layer over the catalog.

- favorites and lists, trip plans, contribution history (places added, reviews written, tracks uploaded)
- primary actions: organize, revisit, publish contributions

### Contribution surfaces

Forms and flows for feeding the catalog.

- add a place, write a review with structured fields, upload photos or GPS tracks, report a problem or correction
- governed by published content criteria in community products

## Important Rules / Behaviors

### Content authority is governed, not assumed

Every product of this type runs an explicit content-authority model. Community products publish criteria and moderate: a place typically must have been physically visited by its contributor, must not promote illegal activity (for example, illegal camping or fee-dodging routes), must not carry paid placement, and owners who list their own place must identify themselves as owners. Official portals publish agency-authored content and onboard facilities through a supply-side process. The authority model is a structural choice, not a feature.

### The catalog decays; corrections are first-class

Outdoor opportunities change constantly — closures, price changes, damaged access. Mature products treat corrections and condition reports as core contributions, and some surface freshness signals (recent reviews, check-in dates) prominently. A discovery product that cannot age its content fails at its one job.

### Ratings are a philosophy, not a given

Products differ structurally on whether a place is summarized by star ratings or by read-the-details reports. Both exist and both work; no single rating model is definitional.

### Discovery is not transaction

Most products of this type do not take payment for the opportunity itself; their commerce is a subscription for tools (offline maps, planning, alerts). Where transactions exist — as in public-lands portals that take reservations and permit fees — they sit on top of the discovery frame. The discovery loop, not the checkout, is what the product is organized around.

### Offline is an engineering commitment

Because discovery targets places beyond signal, mature products engineer for offline use: downloadable maps, downloadable place or route sets, and offline-capable filtering. The depth of this commitment varies; the intent is common.

## Variants

- **Official public-lands portal** — agency-run catalog over a nation's public recreation estate, official content, with a reservation/permit/lottery layer on top (e.g., a federal recreation portal).
- **Community-moderated place catalog** — traveler-contributed records under published criteria and moderation; often journey-scoped (camping plus the services a road journey needs) and offline-first.
- **Community review catalog** — structured traveler reviews and photos as the decision content, frequently with niche vehicle or lifestyle filters.
- **Route and highlight discovery** — routes and points of interest as the records, community tips as the content, with planning and navigation as adjacent layers.
- **Trail-sharing community** — members publish their own GPS tracks; the catalog is the community's shared output; navigation and device hand-off adjacent.
- **3D / immersive map exploration** — the map itself (3D terrain, peak identification) is the discovery experience.
- **Single-domain vs multi-activity** — some products span many outdoor activities; others bind deeply to one journey style (camping/RV, overlanding) and grow the surrounding service catalog instead.

A variant remains a variant unless it changes the core: a product whose center becomes the booking transaction, the field navigation, or the activity record has crossed into a neighboring type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Hiking / Trail Application | closest sibling | the trail app holds the trail as an operational object and supports walking it (field wayfinding, offline, recording); here discovery is the center and wayfinding is absent or an extension |
| Running / Cycling / Workout Tracking Applications | adjacent | those center the activity record loop (record → analyze); here there is no record loop at the center |
| Campground Booking Platform | adjacent, transaction-centered | that type is defined by the payment-confirmed booking transaction over bookable inventory; here discovery is the center and a transaction layer, where present, serves it |
| Tour & Activity Marketplace / Sports Marketplace | adjacent, transaction-centered | those end in transacted engagements; discovery content here does not |
| Ski Resort Recreation Application | adjacent | finding and choosing destinations vs being the guest's companion at the destination (live operating state, the mountain day) |
| Recreational Fishing Application | adjacent | places and inspiration vs the catch record and operational water-bound knowledge |
| Directory Application / Review Platform | family resemblance | generic directories list businesses for general purposes; this type is domain-bound to outdoor recreation with outdoor attributes and a plan-an-outing loop |
| Map / Navigation Application | adjacent | generic routing and wayfinding vs catalog plus decision content; navigation here is absent or an extension |
| Destination Discovery Application (travel) | adjacent | travel destinations broadly (cities, stays, attractions) vs outdoor recreation opportunities specifically |
| Parks & Recreation Administration | opposite side | operator-side administration of programs and facilities vs end-user discovery of opportunities |

The boundary with the Hiking / Trail Application is the most important one, because the two types share subject matter and often share discovery surfaces — the discovery layer inside a trail app is a standard capability of that type, not this one. The structural test is the center of gravity: does the product exist to help someone choose an outing, or to carry them through it?

## Representative Products

- **Recreation.gov** — official US public-lands portal; multi-activity catalog with reservations, permits, and lotteries on a discovery frame
- **Komoot** — multi-activity route and highlight discovery with curated collections, planning, and navigation
- **iOverlander** — community-moderated place catalog for overland journeys; offline-first; no commerce in the opportunity
- **Campendium** — camping/RV discovery with structured community reviews and map-first browsing
- **Wikiloc** — community trail-sharing catalog with navigation and device hand-off

(Also observed during research: PeakVisor, a 3D-map-led mountain discovery product.)

## Sources

Research date: **2026-09-10**

- Recreation.gov — https://www.recreation.gov/
- Komoot — https://www.komoot.com/ , https://support.komoot.com/hc/en-us
- iOverlander — https://www.ioverlander.com/ , https://ioverlander.com/features , https://ioverlander.com/general_criteria
- Campendium — https://www.campendium.com/
- Wikiloc — https://www.wikiloc.com/
- PeakVisor — https://peakvisor.com/

> Sourcing limitations: The Dyrt (HTTP 406) and AllTrails (timeout) could not be fetched; no claims in this document rest on them. Recreation.gov's help center is script-rendered and unreadable, so its reservation and permit mechanics are intentionally not characterized. Precise vendor figures (user counts, catalog sizes) appear in the paired Research Notes and are not asserted as operational facts here.

Detailed evidence, product-by-product observations, the cross-product comparison, and the boundary analysis are recorded in the paired Research Notes.
