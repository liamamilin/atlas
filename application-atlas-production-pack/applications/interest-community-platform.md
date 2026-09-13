# Interest Community Platform

## Overview

An **Interest Community Platform** is a venue that hosts many member communities as first-class units. Each community is a named container scoped by a shared interest or topic — a game, a craft, a city's hiking scene, a fandom, a profession's hobbyists — that people discover, join, and participate in under a single account. Each community holds its own members, its own rules, and its own persistent body of member-contributed content, and the platform's home surface for a user is assembled from the communities that user has joined.

The defining structure is small:

```text
Venue (the platform)
└── Interest community (named, joinable, scoped by a shared interest)
    ├── Community membership (per community, under one account)
    └── Persistent member contributions organized inside the community
```

Everything else the market associates with these products — voting, threaded replies, media, events, chat, feeds, moderation dashboards, mobile apps, subscriptions — is common capability layered onto that skeleton, not what makes the product an interest community platform.

The boundary that matters most inside the family: when the software is organized around **one operated container** that an organization owns and manages, it is a **Community Platform**; when it is organized around a **person's interest record and follow graph**, it is an **Interest-based Social Network**; when the primary object is **live rooms** under a joinable container, it is a **Community Chat Platform**; when it is a **single standing venue** organized around boards, it is an **Online Forum**. When the unit users discover and join is itself a community scoped by an interest — and the venue hosts many of them — it is this Type.

## Users & Context

Three structurally different populations use these products.

**Participants** — people who hold an interest and want others around it. Typical reasons to open the application:

- find communities that match an interest (and often a location)
- join and keep up with several communities at once
- post, reply, vote, or react inside a community
- attend what the community organizes, or see what's new without posting

Participation is commonly pseudonymous: members are typically identified by chosen handles rather than legal identity, though the posture varies by product.

**Community organizers and moderators** — members who take responsibility for one community: writing its description and rules, approving or removing members, starting and sustaining activity, and keeping content within the community's scope. In the sampled products this role is exercised by members themselves — the person who created the group, volunteer moderators — rather than by the platform's staff, and a community can outlive a particular organizer.

**The platform operator** — the side that runs the venue as a whole: platform-wide rules, review of new communities, enforcement above the community level, and the discovery machinery that surfaces communities to potential members.

Context of use is mixed web and mobile; the venue's defining loop (find a community → join it → follow what happens in it) works on both. Communities range from a handful of members to mass scale, and one person's participation typically spans several communities of unrelated interests.

## Core Model

### The Defining Core

```text
Venue (the platform)
└── Interest community (named, joinable, scoped by a shared interest)
    ├── Community membership (per community, under one account)
    └── Persistent member contributions organized inside the community
```

Three properties held together. If any one is removed, the product stops being recognizable as this Type:

- **The interest community as a first-class unit.** A community is a named container with an identity of its own — description, scope, rules — that exists independent of any single member. Its scope is explicit: the community is *about* something, and that something decides what belongs inside. Remove the interest scoping and the product becomes a social platform with arbitrary personal groups; remove the container and it becomes a profile-centric network.
- **A multi-community venue under one account.** The platform hosts many such communities in parallel and makes them discoverable — through listings, search, and announcements — so that members can find and join them. One user account holds memberships across several communities simultaneously, and the user's home surface is assembled from those memberships. Remove the many-community hosting and what remains is a single community site (an online forum or one operated community); remove member-side discoverability and it collapses into private groups with no venue.
- **Persistent member contributions inside the community.** Members — not only the venue's operators — create the content: discussion posts that accumulate replies, shared links and media, event records, photos. Content organizes within the community's space and persists as its readable archive. Remove member participation and the product is a directory of communities; make the live stream the primary object and it becomes a chat venue.

The three are load-bearing together: a single interest-scoped community with persistent discussion is a forum or a community platform instance; a venue of communities without member contributions is a directory; a platform of persistent group content without interest-scoped, joinable units is a social network's group feature.

### Standard Capabilities

Mature products commonly add the following around the core. They make the venue practical; they do not define the Type.

- **Community discovery** — a browsable, searchable surface of communities, filtered by interest and often by location; recommendations and interest-targeted announcements of new or newly-approved communities.
- **Discussion machinery** — posts with attached comments, threaded replies, reactions; voting on posts and comments is common in discussion-anchored products but is not universal across the Type.
- **Community rules as a visible surface** — each community's description and rules are shown where people decide whether to join.
- **Two-layer governance machinery** — community-level powers (approve members, remove content, mute or ban problem members) nested under platform-level rules and enforcement; some products expose a log of moderation actions.
- **Member profiles** — a page per member carrying identity and participation (handle, bio, avatar; joined communities; attendance or contribution history where the product tracks it).
- **A personal home feed** — an aggregation of recent content from the communities a member has joined, alongside notifications and per-community notification settings.
- **Member-to-member messaging** — private messages between members, and in some products real-time chat or event chats as side surfaces.
- **Blocking and muting** — of other members, and in some products of entire communities.
- **Content classification** — media uploads, link sharing, and (where relevant) adult-content marking at the post and community level.

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:     Interest community unit
Realized as: a discussion community holding post threads, a local group
             holding real-life events, a fandom community holding media
             and polls, a topic "bar" in a regional platform

Concept:     Membership
Realized as: one-click join, subscribe, or a join request awaiting
             organizer approval — the membership act always exists,
             its friction varies

Concept:     Persistent contributions
Realized as: post threads with replies, event listings with attendee
             records and photos, shared media collections

Concept:     Two-layer governance
Realized as: member moderators under site-wide rules and review,
             with platform staff enforcing above the community
```

A reader who has only seen a discussion-anchored venue should still be able to recognize an event-anchored one as the same Type from the core model.

## How It Works

### The member loop

```text
Discover communities (browse / search / recommendations / announcements)
→ inspect a community (description, rules, current content)
→ join or subscribe (immediately, or by request)
→ the community's new content enters the personal home feed
→ participate: post, reply, vote or react, attend, upload
→ manage: adjust per-community notifications, mute, block, leave
```

Joining is the pivotal act. It converts a visitor into a member of that specific community and, in the products researched, membership — not posting permission — is what membership primarily configures: the personal feed is assembled from joined communities, and the community appears in the member's own list. Depending on the product and the community, participation in a visible community may require membership or may be open to any signed-in member of the venue; membership always organizes the reading experience.

Membership is multi-community by design. A single account collects many unrelated communities — this is the structural difference between a venue of communities and a single community site — and the leave, mute, and block controls operate per community.

### The community lifecycle

```text
A member (or operator) creates the community:
    name, description of purpose and ideal members, rules
→ platform-level review against site-wide guidelines (in some products)
→ approved: the community becomes discoverable and is announced,
    often targeted at members with similar interests
→ governed: join requests approved or declined, content moderated
    within community rules under platform rules
→ sustained: recurring contributions — threads, events, media
→ succession: in some products the organizer role can pass to a new
    member rather than the community ending
```

Creation is member-initiated in the products researched; the vetting a new community passes before it becomes discoverable varies — from none to a formal platform review — and is a product decision, not a Type property. The community's scope statement (purpose, ideal members, rules) is created at birth and is the reference point for all later moderation inside the community.

### The governance loop

```text
Platform-wide rules published by the venue
→ each community states its own rules on top
→ community-level moderators/organizers act on content and members
→ platform-level staff enforce above the community: reviewing new
   communities, handling reports and appeals, removing communities
   or accounts that break platform rules
→ moderation actions are recorded (in some products in a publicly
   visible log)
```

The two layers are structurally distinct: community moderators govern *inside* a scope they did not set, and the venue governs the venue. Both layers were observed directly in the research, and their nesting is what distinguishes governance in this Type from single-layer moderation on a standalone forum.

### The event loop (event-anchored variant)

In products where real-life gatherings are the participation anchor, the community's recurring cycle runs through its events:

```text
Organizer schedules an event for the community
→ members RSVP (with waitlists where capacity is limited)
→ attendance is recorded; tickets or fees where applicable
→ the event happens; photos and feedback are added afterward
→ the event's record persists in the community's archive
```

Everything else in the model — discovery, joining, rules, two-layer governance — is unchanged; only the dominant content object differs from discussion threads to event records.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Community discovery page

The venue's storefront.

- purpose: find communities worth joining
- typical information: community names and descriptions, interest categories, location scoping, member counts, activity signals
- primary actions: browse by category, search, open a community, respond to an announcement

### Community home

The unit's identity surface.

- purpose: show what this community is about and what is happening in it
- typical information: description and scope, rules, member list, recent posts or upcoming events, join button
- primary actions: join (or request to join), post, browse content and members, read rules

### Discussion view

The reading-and-participation surface for one community's content.

- typical information: posts with authorship, threaded replies, votes or reactions, timestamps
- primary actions: reply, vote or react, share media or links, report

### Composition surface

Where contributions enter a community.

- typical information: target community selector, title and body, links/images, content classifications
- primary actions: publish post, create event (where events exist), attach media

### Personal home feed

The member's assembled view of the venue.

- purpose: keep up with several joined communities in one stream
- typical information: recent content from joined communities, notifications, announcements
- primary actions: filter or sort (subscribed vs all), open content, adjust notification settings

### Member profile

A member's identity and participation record.

- typical information: handle, avatar, bio, joined communities, contribution or attendance history
- primary actions: follow or message (where supported), view their content

### Organizer and moderation surfaces

The community-governance side.

- purpose: run one community and enforce its rules
- typical information: join requests, reported or flagged content, member list with standing, community settings, moderation log
- primary actions: approve/decline members, remove or lock content, mute/ban members, edit rules, transfer the organizer role

## Important Rules / Behaviors

**The community's scope is enforced.** Content that falls outside what a community is about is removable under its rules. This is the interest anchoring operating as a daily rule: the scope statement created at the community's birth is the reference for moderation, and cross-posting the same content into many communities is constrained by each community's rules.

**Rules stack.** A community's rules sit on top of the venue's platform-wide rules; a member can satisfy the community and still violate the venue. Venue-level enforcement (reviewing new communities, removing communities or accounts) operates above community-level moderation and cannot be overridden from inside a community.

**Membership configures the experience, not always participation.** Joining assembles the personal feed and attaches the member to the community's roster; whether non-members may post into a visible community varies by product. Approval-gated joining exists in the sampled products alongside one-click joining.

**Content persists.** Contributions remain readable in the community's space — the archive is the community's accumulated value, and search over it is a standard expectation. This is the deliberate contrast with live-chat venues, where conversation is transient.

**Governance is largely member-run.** Community organizers and moderators are typically members of the venue, not platform staff; the platform's role is the outer layer — rules, review, and enforcement. Moderation transparency practices vary; some products expose a log of moderation actions.

**Blocking is layered.** Members can block other members and, in some products, entire communities, removing them from the personal experience without affecting the venue at large.

## Variants

- **Discussion-anchored venues** — communities hold post threads with replies and voting; the archive of discussion is the asset (the canonical consumer shape).
- **Event-anchored venues** — communities organize real-life gatherings; the event record (RSVPs, attendance, photos, feedback) is the asset, and the organizer role carries a stronger operational burden, often under a paid organizer model.
- **Fandom and mobile-first venues** — communities built around media franchises or niches with heavier media, chat, and poll usage.
- **Regional mega-platforms** — topic-scoped communities at national scale under one account, often with long histories predating modern social networks.
- **Federated and self-hosted venues** — the venue is a network of independently operated servers; communities remain joinable units, and accounts span communities across servers; commonly non-commercial.
- **Creation and gating postures** — open member-created communities vs review-gated creation; one-click vs approval-gated joining; open signup vs application-gated venue accounts.
- **Monetization postures** — advertising-funded venues, paid organizer subscriptions, member dues and ticketed events, premium member tiers, donation-funded non-commercial venues.
- **Historical realizations** — newsgroup hierarchies and email-based interest groups satisfy the same core (named topic communities, subscription membership, persistent member content, layered governance) with none of the modern machinery, which is the check that the core is not an artifact of current implementations.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Community Platform | adjacent (sharpest seam in the family) | an organization operates **one** container it owns, sold to the operator and instrumented for operator management; here the venue hosts **many** communities discovered and joined by members, and monetization targets participants or organizers, not a container license. Interest communities run on community-platform software are instances of that Type |
| Interest-based Social Network | adjacent (container-vs-network seam) | there the member's profile-as-interest-record is the spine and content binds to a domain's objects; groups are optional containers. Here the community unit is the spine, profiles are thin participation records, and the home feed aggregates joined communities rather than followed people |
| Community Chat Platform | adjacent | live rooms with real-time message streams are the primary object there; here persistent asynchronous content (threads, events) is the community's asset and chat is a side surface |
| Online Forum | adjacent (same family) | a single standing venue organized around boards/topics; a board is a section of the venue, not itself a joinable community with its own membership and scope |
| Q&A Community | adjacent (same family) | participation organized around question/answer pairs with accepted answers; Q&A machinery can exist inside communities without being the Type |
| Discussion Board | nested surface | the topic-and-reply tool; a community platform typically hosts such surfaces inside its communities |
| Neighborhood Social Network | adjacent | the community container is keyed by verified locality rather than interest |
| Dating Community Platform | adjacent | the container is keyed by partner discovery |
| Member Community Platform / AMS | segment sibling | the container is keyed by organizational membership; the AMS owns the member registry |
| General Social Network | adjacent (different family) | profiles, follow graphs, and untyped personal updates organize the loop there; here the joinable interest community organizes it |

## Representative Products

- **Reddit** — the canonical ad-funded venue of discussion communities; product documentation consulted at positioning level only (see Sources)
- **Meetup** — event-anchored interest groups with a paid organizer model; extensively documented help center
- **Lemmy** — federated, self-hostable, non-commercial venue of topic communities; official open-source documentation

Widely cited members of this family such as Amino and Baidu Tieba could not be directly researched (see Sources) and are not relied on for any claim; the definition was additionally checked by reasoning against historical newsgroup and email-group realizations.

## Sources

Research date: **2026-09-08**

- Reddit — corporate site and product explanation ("How does Reddit work", post/comment/vote, communities organized around interests): https://www.redditinc.com/
- Meetup — Help Center: https://help.meetup.com/hc/en-us — including "What is a Meetup group?", "Joining a Meetup group", "Starting a Meetup group and publishing your first event", the Groups and Communications and Events categories
- Lemmy — official site and documentation (Introduction, Getting Started): https://join-lemmy.org/ , https://join-lemmy.org/docs/index.html , https://join-lemmy.org/docs/users/01-getting-started.html

> Sourcing limitation: official operational documentation for Reddit (help center 403; wiki FAQ timed out), Amino (support and main sites timed out), and Baidu Tieba (403) could not be retrieved from the research environment on 2026-09-08 and was abandoned rather than substituted from memory. Reddit's contribution rests on its official product-positioning pages; Amino and Baidu Tieba are used as market anchors only, with no product-specific claims anywhere in this document. The abstraction rests on the two products with full operational documentation (Meetup, Lemmy) plus Reddit positioning; claims that could not be checked across products are phrased as product-specific or common-variant statements, and no precise numeric limits or defaults are asserted beyond figures stated on fetched pages.

Detailed evidence, per-product observations, cross-product comparison, and the historical / regional sample check are recorded in the paired Research Notes.
