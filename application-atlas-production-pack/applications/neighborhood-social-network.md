# Neighborhood Social Network

## Overview

A **Neighborhood Social Network** is a social network organized by **verified locality**: people join by verifying where they live, are placed into a geographically demarcated neighborhood that becomes their default audience, and exchange practical local-life content with co-residents — recommendations, help, items, safety, events, local issues — while local institutions (businesses, public agencies, organizations) participate as constrained guests.

The defining structure is small:

```text
Verified-locality membership
└── The neighborhood as container and default audience
    └── Resident-to-resident practical exchange
```

Everything else commonly associated with these products — real-name display, marketplaces, business pages, agency alerts, events, groups, moderation programs — is widespread in current products but is not part of the defining core. A members-only email list for one residential area, exchanging practical neighborhood messages, would satisfy the same core.

## Users & Context

The primary user is a **resident** — someone who lives in a defined local area and uses the network as a member of that area, not as a follower of people or topics. Their standing in the network derives from where they live.

Typical reasons to open the application:

- ask neighbors for a recommendation (plumber, babysitter, doctor)
- offer or seek help
- give away, sell, or borrow items
- share or receive safety alerts and lost-and-found notices
- learn about and organize local events
- discuss local issues (roadworks, traffic, construction)

Secondary participants are **local institutions** — businesses, public agencies, nonprofits — which maintain pages or profiles and post into localities, but (in the products researched) cannot read the conversations residents have with each other. The work environment is dominated by mobile apps with a companion web surface sharing one identity.

## Core Model

### The Defining Core

Three structures, jointly held. If any one is removed, the product stops being recognizable as a Neighborhood Social Network:

1. **Verified-locality membership** — membership is established through a real-world residence claim (an address) that the product verifies, and the member's standing derives from where they live. Remove the gate → a social network anyone can join from anywhere.
2. **The neighborhood as container and default audience** — a geographically demarcated local area holds the membership; content is scoped to it (with controlled extension to surrounding areas); the neighborhood is the attribution frame of ordinary posts. Remove the container → a topic-keyed community or a person-graph feed.
3. **Resident-to-resident practical exchange as the content loop** — the currency of the network is posts between resident-members about local practical life, attributed to identified residents, with persistent history and private channels. Remove the exchange → a resident directory or bulletin board; remove the resident-to-resident direction → a local news/information service.

The three are load-bearing together: verification alone is a verified-address directory; a demarcated container without the gate is an open local topic forum; practical exchange without the locality gate is a general social network with a location interest.

### Capabilities Shared by Mature Products

These make the Type practical; they do not define it.

- **Resident profile** — a real-identity posture is the strong market norm (verification against a real address implies a real person); display is often abbreviated (e.g. first name + last-name initial), with street-level visibility as a user toggle and personal attributes (hobbies, pets, profession) on the profile.
- **Practical post taxonomy** — recommendations and asks, help offered/sought, item exchange (sell / free / borrow), safety alerts and lost-and-found, events, local civic discussion.
- **Replies and private messaging** between members; group chats within the locality.
- **Nearby reach extension** — per-post or per-surface scoping beyond the immediate neighborhood (surrounding neighborhoods, city, jurisdiction).
- **Constrained institution layer** — business pages, public-agency pages, nonprofit pages that post into localities but cannot read neighbor conversations. Documented directly in two researched products and structurally present in all four.
- **Moderation machinery** — community guidelines, tone rules, volunteer moderator/admin roles, and flagging that reduces a post's distribution rather than deleting it.
- **Events and groups** — a neighborhood calendar and member-formed activity groups inside the locality.
- **Mobile app + web** sharing one identity, with notifications.

### One Structure, Many Implementations

The core is written conceptually; implementations vary:

```text
Concept:            Verified-locality membership
Implementations:    address entry at signup with verification,
                    real name + address registration,
                    in-app neighborhood verification tied to trading

Concept:            The neighborhood container
Implementations:    system-drawn geographies, member-founded neighborhoods,
                    administrative units, public browsable directories

Concept:            Practical exchange
Implementations:    a general feed with sections (ask / items / alerts / events),
                    a commerce-first app with a community feed riding on it,
                    a closed network with borrow/give and a calendar
```

## How It Works

### Join and be placed

```text
Sign up with a real identity
→ provide a home address
→ the product verifies the residence claim
→ the member is assigned (or confirms assignment) to a demarcated neighborhood
→ set a resident profile
```

There is no follow graph to build and no topics to pick. Membership and default audience both come from the address. Some products let members found or choose among neighborhood definitions; most assign automatically.

### Post into the neighborhood

```text
Compose a post (recommendation, ask, offer, alert, event, local issue)
→ choose the audience scope (the neighborhood, or neighborhood + surrounding area)
→ post; it is attributed to the named resident and visible to co-residents
→ receive replies; continue in comments or move to private messages
```

The neighborhood feed is the default consumption surface: what a member sees is primarily what co-residents post, not a merged stream of followed accounts.

### Exchange items or services

```text
List or request an item / service
→ neighbors respond
→ arrange handover or delivery directly
→ (in commerce-first products: complete payment in-app with trade-safety mechanics)
```

Item exchange appears in every researched product, but in different depths — from borrow/give-away boards to full secondhand-commerce verticals.

### Institutions post in

```text
A business / agency / nonprofit maintains a page or profile
→ it posts messages targeted to specific localities
→ residents see them in the neighborhood context
→ residents generally cannot be read by institution staff;
  in agency surfaces, residents often cannot start conversations with the agency either
```

The institution layer is one-directional by design: institutions broadcast into localities; the resident loop stays private to residents.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Neighborhood feed

The primary surface.

- posts from co-residents, attributed to named residents and their neighborhood
- sections or filters for asks/recommendations, items, alerts, events
- primary actions: post, reply, react, message the author, adjust audience scope

### Neighborhood / member directory

The locality's people surface.

- list of co-residents with profiles; neighborhood identity and boundaries
- primary actions: view a profile, message a neighbor, see who lives nearby

### Item exchange / marketplace surface

- listings or posts for sale/free/borrow (in commerce-first products, full trade flows with chat, payment, and reputation)
- primary actions: list, respond, arrange exchange

### Institution pages

- business, agency, or organization profiles posting into localities
- primary actions: follow/see posts, view reviews or contact details (businesses); receive alerts (agencies)

### Events and groups

- neighborhood calendar and member-formed groups
- primary actions: create/join an event or group, RSVP, discuss

### Settings / privacy

- controls over identity display (name form, street visibility), notification preferences, and audience scopes

## Important Rules / Behaviors

### Membership is gated, and the gate is the audience

The address is both an entry requirement and the scoping mechanism: what a member posts is by default visible to co-residents of the demarcated area, not to a self-curated graph or the public. Extending reach beyond the neighborhood is an explicit, controlled act.

### Institutions are guests with one-way rights

In the researched products, public agencies and local governments can post into neighborhoods but **cannot view the conversations residents have with each other**; businesses participate through pages rather than the resident identity. This privacy wall is a structural feature, not an incidental setting.

### Real-identity posture, implementation-flexible display

Verification against a real address implies real identity; products differ on display (full name vs abbreviated name vs profile attributes). The load-bearing structure is verified locality, not any particular display form.

### Moderation shapes distribution

Community guidelines and tone rules are prominent; in at least one researched product, flagged posts remain published but lose distribution. Volunteer neighborhood-level moderator roles exist in several products.

### The exchange loop stays resident-to-resident

Commerce, help, and recommendations flow between identified residents. When the transaction — not the neighbor loop — becomes the unit of record, the product belongs to marketplace territory (see Related Types).

## Variants

- **Ad-funded network with institution programs** — deep local-news publisher integration, agency alert partnerships, paid lead routing to businesses (the large global product pattern).
- **Social-startup / civic posture** — real-name + address registration, voluntary user contributions plus clearly labeled local ads, tone governance as a stated mission.
- **Public-sector-licensed, ad-free** — municipalities buy a communication/participation dashboard; consumer side free and closed; only non-commercial external parties admitted.
- **Commerce-first hyperlocal super-app** — verified-locality secondhand trade as the founding loop, with a community feed, neighborhood store profiles, and adjacent verticals (jobs, cars, realty, payments) riding on the same verified locality.
- **Civic-circle boundary case** — locality used to *suggest* topic circles rather than gate a neighborhood feed; sits on the seam toward Community Platforms.

A variant remains a variant unless it changes the users, core objects, or loop so much that the defining core no longer applies.

## Related Application Types

| Application Type | Distinction |
|---|---|
| General Social Network | membership is open and the graph is self-curated; here membership is address-gated and the default audience is co-residency |
| Interest-based Social Network | identity and content are keyed to an interest domain; here to a residence domain |
| Microblogging Platform | ties are public broadcast subscriptions consumed in a merged stream; here the audience is co-residency, not subscriptions |
| Professional Social Network | career/professional context keys identity and sharing; here residential context does |
| Community Platform / Online Forum | containers are topic-keyed and membership open to anyone interested; here containers are geographic and membership verified |
| Classifieds Platform / Service Marketplace | the transaction is the unit of record and the venue serves it; here the neighbor exchange loop is the spine and commerce is one post type |
| Tenant / Resident Portal, HOA Management | operator-side residential systems: membership follows tenancy of a specific property and the operator's business processes are the core; here membership follows residence in a demarcated area and peer exchange is the core |
| Civic Engagement Platform / 311 | government operates the surface for constituent engagement; here agencies are guests posting into a resident-owned loop |
| Local News Application / News Aggregator | editorial news consumption is the product; here news is a bundled capability feeding the neighbor loop |
| Instant Messaging Application | private addressed conversation is the product; here DMs are a side channel of the neighborhood loop |
| Friend Discovery Application | forming new relationships is the primary loop; here meeting neighbors is a byproduct of the exchange loop |

The sharpest boundary is with the General Social Network: both share surface vocabulary (profiles, feeds, posts, comments), but the organizing key differs structurally — verified residence keys both membership and the default audience here, versus a self-curated person graph there.

## Representative Products

- Nextdoor (global, ad-funded, institution-heavy)
- nebenan.de (Germany, social-startup posture, real-name + address verification)
- Hoplr (Belgium/Netherlands, public-sector-licensed, ad-free)
- Karrot / Danggeun (Korea, commerce-first hyperlocal super-app)

LocalCircles (India) was examined as a boundary case: locality suggests topic circles rather than gating a neighborhood feed — evidence for the Community Platform seam, not a core sample.

## Sources

Research date: **2026-09-08**

- Nextdoor — About: https://about.nextdoor.com/ ; neighborhood directory: https://nextdoor.com/find-neighborhood ; product updates and self-promotion policy: https://blog.nextdoor.com/ ; public agencies: https://about.nextdoor.com/public-agency
- nebenan.de — root: https://nebenan.de/ ; FAQ: https://nebenan.de/ueber-uns/fragen
- Hoplr — root: https://www.hoplr.com/ ; about: https://www.hoplr.com/about
- Karrot / Danggeun — about: https://about.daangn.com/ ; service: https://about.daangn.com/service/
- LocalCircles — root: https://www.localcircles.com/

> Sourcing limitation: the help centers of all four core products were unreachable during research (transport errors, timeouts, or access restrictions), as were the consumer app surface of the commerce-first product and several older/regional neighborhood-network sites. The model therefore rests on official about/FAQ/landing/blog pages rather than help-center-grade operational detail. Verification methods, exact neighborhood granularity rules, and moderator-program details are intentionally not stated precisely in this document; the historical check (pre-smartphone email-list neighborhood networks) is reasoned from the defining core rather than sourced from fetched documents.
