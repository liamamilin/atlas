# Interest-based Social Network

## Overview

An **Interest-based Social Network** is a social network whose entire world is organized around a shared interest domain — film, books, music, a sport, a craft, a creative field. Members keep profiles that are persistent records of their engagement with that domain, contribute content that is anchored in it, and find both content and people through the domain's own structures rather than through a pre-existing circle of acquaintances.

The defining core is deliberately small:

```text
Shared Interest Domain
└── Member Identity as Interest Record
    └── Domain-anchored Content Objects
        └── Interest-keyed Discovery & Distribution
            └── Person-to-person Social Ties (follow / friend) with persistent activity streams
```

Everything else commonly associated with modern social products — entity databases, curated collections, ratings, recommendation engines, rich feeds, moderation machinery, mobile apps, paid tiers — is widespread in mature products but is not what makes the product an interest-based social network. The Type is also not defined by any one content form: a review of a film, a logged run, a saved idea, and a hand-made project can all be the same structural object in different implementations.

## Users & Context

The primary user is an enthusiast, hobbyist, or practitioner of the interest domain — someone who watches films, runs and rides, reads books, knits, or makes things, and who treats the domain as a sustained part of their life rather than a passing curiosity.

What brings them to the application:

- **record** their engagement — log what they watched or read, capture the workout they completed, save the work they made or the things they want to do next
- **express taste** — rate, review, tag, and curate their record into something that represents them
- **discover** new content within the domain — what to watch, read, do, or make next
- **connect** with people who share the interest — follow other members, react to their activity, and find like-minded members through the things they love

Secondary participants include highly active contributors (prolific reviewers, creators, club or group organizers) and moderators who apply the community standards. Consumption without contribution is a fully supported mode: browsing, searching, and discovery work for members who never post. Usage is mobile-first in current products, with web clients serving as the deeper authoring and browsing surface; scale can range from global mass-market products to small niche communities of a single craft.

## Core Model

### The Defining Core

```text
Shared Interest Domain
└── Member Identity as Interest Record
    └── Domain-anchored Content Objects
        └── Interest-keyed Discovery & Distribution
            └── Person-to-person Social Ties (follow / friend) with persistent activity streams
```

Five properties held together. If any one is removed, the product stops being recognizable as this Type:

- **Shared interest domain** — the network exists for one named interest area (or one coherent cluster of them). The domain bounds the world: it decides what content can exist and what the profile means. One product is a film diary network, another is an athletic network, another spans books, film, and music.
- **Member identity as interest record** — the profile is not a generic personal page; its persistent meaning is the member's accumulated engagement with the domain: what they have watched, read, done, made, collected, and how they rated it. The profile answers "who is this person as an enthusiast of X", not "who are this person's friends" and not "what does this person do for work".
- **Domain-anchored content objects** — everything a member contributes is bound to the interest: attached to one of the domain's objects (a film, a book, a route, a pattern), or produced as the domain's native artifact (a recorded activity, a completed project). Untyped personal updates are not the currency of the network; the domain is what makes each post meaningful.
- **Interest-keyed discovery & distribution** — content is surfaced through the domain's structures: pages that aggregate everything members have said or done around one object, tags and classifications, member-curated collections, similarity and taste matching, member-driven rankings. Follow streams also distribute content, but the interest structures do the organizing work that a personal acquaintance graph does in a general-purpose social network.
- **Person-to-person social ties with persistent activity streams** — members connect to (follow or befriend) other members, their activity flows into durable feeds, and interactions (reactions, comments, ratings) attach to content and profiles. Remove the ties and the product is a content catalog or curation site; the ties are what make it a social network.

### How the Concepts Are Implemented

The core is written conceptually; mature products realize each concept differently:

```text
Concept:        Domain-anchored content object
Implementations: review / diary entry bound to a catalog entity (film, book)
                 recorded activity as a native artifact (a run, a ride)
                 member-created work (artwork, project)
                 saved item bound to an idea or topic

Concept:        Interest-keyed discovery
Implementations: entity pages aggregating member content
                 tags / genres / site-wide classifications
                 member-curated lists and collections
                 similarity ("if you liked these…") and taste matching
                 member-driven rankings and votes

Concept:        Social tie
Implementations: asymmetric follow, symmetric friendship
                 contact import from other networks or address book
                 member browsing and search
```

A reader who has only seen one implementation — for example a film-review network — should still be able to recognize an athletic-activity network or a craft network as the same Type from the core model.

### Capabilities Shared by Mature Products

These are common in current products across the sampled market; they make the Type practical but do not define it:

- **Domain catalog pages** — a persistent page per object of the interest (a film, a book) that aggregates member content and anchors discovery; activity-flavored products use domain constructs (segments, routes) in the same role
- **Member collections** — curated, shareable, public-or-private sets: lists, shelves, boards, watchlists
- **Tags and classifications** — member-contributed or system-provided genres and topics that organize content site-wide
- **Ratings, reviews, reactions** — expressive primitives attached to content objects, with comment threads and owner-controlled comment gates
- **Activity feed** — a persistent stream combining followed members' activity with interest items; notification machinery around it
- **Similarity and recommendation surfaces** — interest-filtered discovery, similar-object suggestions, taste-adjacent members
- **Search** over the domain's objects, members, and content
- **Privacy controls** — per-entry visibility (public, followers, close circles, private), with private entries excluded from public stats in products that keep public records
- **Moderation machinery** — community standards, reporting, blocking, content removal with recourse
- **Profile statistics and recaps** — aggregated views of the member's record (totals, year-in-review summaries, personal bests where the domain has them)
- **Mobile apps** sharing one identity with the web surface

## How It Works

### Join and start the interest record

```text
Create an account (a username or member name in the sampled products)
→ set a profile (name, avatar, a few favorites to seed the record)
→ the record grows as the member engages
```

There is no workspace, no team, no locality gate, and no pre-existing acquaintance requirement — joining is an individual decision driven by the interest.

### Contribute domain-anchored content

The primary authoring loop, in one of the sampled shapes:

```text
Pick an object of the domain (a film, a book)         ← catalog-anchored shape
→ log it (mark watched/read, add a date)
→ attach a rating, a review, and tags
→ choose visibility (public / circle / private)
→ it appears on the object's page, the profile, and followers' activity

or:

Record the domain-native artifact (an activity)       ← artifact-anchored shape
→ it uploads from the app or a device
→ attach details (type, notes, gear, route)
→ it appears on the profile and in followers' feeds
```

The content object is durable and attributable: it accumulates on the member's profile and on the object it anchors to, and it can typically be edited or removed later (products differ on whether earlier revisions are kept). Content that references something not yet released or not yet experienced is commonly disallowed as a review — some products explicitly restrict reviews to things the member has actually watched, read, or done.

### Discover through the interest structures

```text
Browse the domain's objects / classifications / collections
→ open an object page → see what members said or did around it
→ follow similar objects (genres, tags, similarity)
→ find members whose taste aligns and follow them
→ their future activity enters the feed
```

This loop is the Type's signature: members and content are reached through what they are about, not primarily through who one already knows. Products differ in which structure leads — some are follow-first, some are browse-and-tag-first, some lean on similarity matching — but all sampled products run discovery through domain structures.

### Connect and interact

```text
Follow / befriend members (found via objects, member browse, or imported contacts)
→ their logs, activities, and reviews flow into the activity feed
→ react, comment, rate; build collections
→ block or report members who violate the standards
```

Ties are personal and persist until changed; feeds aggregate followed members' activity over time rather than disappearing with the session.

### Capabilities by tier

- **Defining core** — the five properties of the Core Model
- **Standard capabilities** — catalog pages, collections, tags, ratings/reactions, feeds, similarity surfaces, search, privacy, moderation, apps, stats/recaps
- **Optional / variant** — groups, clubs, and forum containers; challenges and goals; commerce (shops, rentals, marketplaces); regional super-network surfaces (city events, audio, marketplaces); cross-posting and export; paid tiers

## Interfaces

Described conceptually; exact layout and naming vary by product.

### Activity feed

The member's running view of the network.

- shows followed members' new content (logs, activities, reviews, list publications) and interest items
- primary actions: react, comment, open the content and its object, adjust what appears (ordering, favorites, muting in some products)

### Object page

The page for one object of the domain — the organizing surface of discovery.

- the object's identity (title, key attributes, artwork) and everything members attached to it: ratings, reviews, tags, related lists, similar objects
- primary actions: record one's own engagement (log, rate, review, save), browse member content around it, navigate to similar objects

### Member profile

The interest record of one member.

- their accumulated record (what they watched/read/did/made, favorites, collections, stats), their activity stream
- primary actions: follow, browse their content and collections, interact

### Collection / list surface

Member-curated sets.

- ordered or unordered sets of domain objects, public or private, shareable
- primary actions: create, add and reorder objects, publish or keep private, clone or compare with other members' collections (in some products)

### Browse / explore / search

The discovery surface of the domain.

- classifications, tags, curated editorial or community selections, filters; search across objects, members, and content

### Settings / privacy

- account identity, per-entry default visibility, blocked members, notification preferences, data export

## Important Rules / Behaviors

### Content must anchor to the domain

The network does not accept untyped personal updates: a post is a log, a review, an activity, a creation, or a save — something bound to the interest. This single rule is what keeps the profile an interest record and the discovery loop interest-keyed.

### The interest record is durable and cumulative

Entries persist on the profile and on the object they anchor to. In products that keep public records, aggregate stats are derived from entries, and entries hidden by privacy settings may be excluded from those stats. Deleting content does not always remove it from a member's own export archive; earlier revisions of edited content may or may not be retained.

### Visibility is layered

Per-entry privacy (public / restricted circles / private) is a structural surface, not an afterthought, because the record mixes public expression with personal bookkeeping. Blocking terminates the tie in both directions and hides content asymmetrically; some products have no fully private accounts, so blocking limits interaction rather than guaranteeing invisibility.

### Moderation applies to the domain's expression

Community standards govern written and uploaded content, with reporting, blocking, and removal machinery; removal typically has a stated recourse path. Membership is generally open to anyone with the interest — some products state explicitly that no invitation by an existing member is required, while others gate or queue new signups; the gate is an access rule of the product, not a structural element of the Type.

### Discovery is member-shaped

Rankings, classifications, and similarity are produced from member actions (votes, tags, watches) — the network's ordering is an emergent product of its members rather than an editorial layer, in the products that state this philosophy explicitly. Commercial placement and platform curation vary by product and are variant, not core.

## Variants

- **Catalog-anchored networks** — content binds to a platform-maintained catalog of the domain's objects (films, books, music); the diary/review is the signature object (film and reading networks)
- **Artifact-anchored networks** — the content is the member's own recorded activity or creation (athletic activities, artworks, craft projects); the domain supplies structures (segments, routes, patterns) instead of an object catalog
- **Save-and-curate networks** — content is largely found-and-saved material organized by interest and topic; visual-discovery products sit on this pole and straddle toward content-type networks when the medium dominates
- **Community-heavy hybrids** — the network core is joined by first-class groups, forums, or local events; kept in this Type while the profile-and-stream loop remains the spine, drifting to the Interest Community Platform when containers take over
- **Follow-first vs discovery-first** — feed led by personal ties vs led by tags, similarity, and algorithmic interest surfaces
- **Single-domain vs multi-domain** — one deep interest vs a cluster of cultural-consumption interests under one roof; regional multi-domain networks may bundle city events, audio, and marketplaces
- **Monetization postures** — free community, freemium with paid tiers (ad-free, analytics, filters, custom presentation), commerce extensions (shops, rentals); none of these change the core loop

## Related Application Types

| Application Type | Distinction |
|---|---|
| General Social Network | the profile is a person-representation and untyped personal updates distribute along a self-curated personal graph; here identity is an interest record, content is domain-anchored, and interest structures key discovery |
| Microblogging Platform | ties are public broadcast subscriptions and posts are general-purpose; here content is bound to the domain |
| Photo-centric Social Network / Short-form Video Platform | the medium is the organizing key; visual-interest products straddle this seam and are assigned by what keys the loop |
| Professional Social Network | career/professional context keys identity and sharing; audience differs structurally, not just in topic |
| Neighborhood Social Network | verified locality gates membership and keys the loop; no locality gate exists here |
| Friend Discovery Application | forming new relationships is the primary loop with a person-match at the center; here relationships are a byproduct of the content loop |
| Social Profile Network | profiles and connections without the domain-anchored content loop — a people directory |
| Interest Community Platform / Online Forum / Q&A Community | shared containers (groups, threads, events) organize participation; here the profile + stream + interest-keyed discovery is the spine and containers are optional additions |
| Content Curation Platform / Personalized Content Feed | curating and aggregating content without member social ties; here the social network is structural |
| Review Platform | the review of record for purchase decisions is the product; here reviews are one expressive content object inside a network |
| Dating Application / Dating Community Platform | partner discovery organizes the loop; identity-niche interest networks straddle this seam when community or partner weight is unclear |
| Social Audio Platform / Social Live Streaming Platform | live, ephemeral surfaces are primary; here content is persistent and recorded |

The sharpest boundary is with the General Social Network, its own family sibling: the surface vocabulary (profiles, follows, feeds, reactions) is shared, but the organizing key differs. In a general social network the person and their self-curated graph organize the loop; in an interest-based network the domain does — the profile is an interest record, the content is domain-anchored, and discovery runs through the domain's structures.

## Representative Products

- Letterboxd — film; catalog-anchored diary/review network
- Strava — running, cycling, and outdoor sport; activity-anchored network
- Douban — books, film, and music; multi-domain interest network (China, founded 2005 — the historical/regional anchor of the sample)
- Ravelry — knitting, crochet, and fiber arts; craft network (positioning consulted; operational detail login-walled)

Widely cited members of this family such as Pinterest and Goodreads were not directly researched for this document (see Sources).

## Sources

Research date: **2026-09-07**

- Letterboxd — About & Frequent Questions (official): https://letterboxd.com/about/
- Strava — Help Center (official): https://support.strava.com/hc/en-us
- Strava — About Strava (official): https://support.strava.com/en-us/articles/15402118-about-strava
- Strava — Following Athletes on Strava (official): https://support.strava.com/en-us/articles/15402056-following-athletes-on-strava
- Douban — 关于豆瓣 / About (official): https://www.douban.com/about
- Ravelry — root page (official): https://www.ravelry.com/help

> Sourcing limitation: official documentation for Pinterest, Goodreads, DeviantArt, Last.fm, and Behance could not be retrieved from the research environment on 2026-09-07 (request timeouts / access denial) despite repeated attempts, and was abandoned rather than substituted from memory. The abstraction therefore rests on the four products listed above — two with rich official documentation, one with an official structural/philosophical statement, one with positioning only. Claims that could not be checked across several products are phrased as product-specific or common-variant statements rather than universal rules, and no precise numeric limits, defaults, or feature specifics from unresearched products are stated anywhere in this document.

Detailed evidence, per-product observations, cross-product comparison, and the historical / market-sample check are recorded in the paired Research Notes.
