# General Social Network

## Overview

A **General Social Network** is a person-centered sharing network: every member owns a persistent personal profile representing them as a person, maintains their own connections to other members, and publishes general-purpose updates that are distributed along those personal connections to the people they are connected with.

The defining structure is small:

```text
Personal Profile
  (persistent, self-authored representation of one person)
└── Personal Connection Graph
    (each member maintains their own links to other members)
    └── User-Published Updates
        (posts attributed to the author's profile, distributed
         along the graph to connected members)
```

If any part is removed, the product stops being this Type: remove the **profile** and there is no personal identity home (an anonymous content surface or a topic forum remains); remove the **personal connection graph as the way content travels** and distribution becomes public broadcast or pure algorithmic discovery (a microblogging or content-feed product remains); remove the **shared update stream** and only a people directory remains; remove **person-attribution** of posts and a media site remains.

The Type is also defined by what it does *not* constrain: the audience is unrestricted personal life (not a professional context), the content is general-purpose (not one media format), and membership is not gated by locality or a topical interest. Those restricted forms are separate Application Types in the same family and are contrasted near the end of this document.

## Users & Context

The primary user is any individual who wants to keep up with the lives of people they know and share their own life with those people. Typical reasons to open the product:

- see what friends and family have posted lately
- share an update — text, photos, a life event, a link
- react to, comment on, or pass along a connection's post
- look up a person they know and visit their profile
- coordinate around an event or a shared interest group

Secondary users exist alongside the core: public figures and creators accumulate followers (a person-to-audience relationship layered on the personal graph), and organizations present themselves through pages and run groups. These are common capabilities of mature products rather than what makes the Type.

The dominant context today is the phone; web and desktop clients act as companion surfaces on the same account. Usage is long-term and habitual — the profile and the connection graph persist for years, which is what makes the product a durable home for a person's social presence rather than a transient app.

## Core Model

### The Defining Core

**Personal profile.** Each member owns one persistent page that represents them: identity attributes (name, photo, biographical details) plus the accumulation of the content they have published. The profile is the atom of the system — every post, comment, and connection is anchored to one. It is the member's self-authored representation, and it is what makes the network person-centered: content is organized by *who* posted it, not by where it was posted or what topic it belongs to.

**Personal connection graph.** Each member maintains their own links to other members — the set of specific people they are connected with. This graph is the primary distribution substrate: what a member posts travels to the people connected with them, and what a member sees is drawn from the people they are connected with. The graph is built and maintained by the members themselves (finding, inviting, confirming, following, removing), which distinguishes it from a follower base assembled by a broadcaster or an audience assembled by an algorithm.

**User-published updates.** The unit of shared content is the post: a general-purpose update — text, photos, video, links, life events — that is always attributed to its author's profile and is surfaced to the members connected with them. Updates persist and accumulate, both in the consumption stream and on the author's profile.

Two properties of this core are worth stating precisely:

- The connection graph does double duty. It is a **distribution mechanism** (content travels along it) and an **access-control surface** (who can reach you, see you, and interact with you is largely determined by it). Most products layer explicit audience settings on top, but the graph is the foundation.
- Consumption is constrained by the graph. What a member sees is, by default, a function of who they are connected with — a deliberate contrast with broadcast media and discovery-first feeds, where the operator or an algorithm assembles the audience's attention.

### Standard Capabilities

Mature products commonly carry most of the following. They are not what makes the product this Type, but they make the Type practical at modern scale:

- **Feed** — an aggregated, ordered stream of activity from the member's graph, serving as the home surface. Ordering philosophy varies: some products rank by predicted engagement, some present reverse-chronologically, some offer a choice.
- **Interaction machinery** — reactions or likes, comments, and shares/reposts attached to updates, with notifications for received activity.
- **Audience and privacy controls** — per-post audience selection (for example, connections only, or public) and standing visibility settings; blocking and reporting.
- **People discovery** — search by name, suggestions built from mutual connections, invitations to people not yet present.
- **Profile components** — photos, biographical fields, and the member's accumulated posts on their own profile.
- **Composition** — a composer surface for creating posts in multiple content forms (text, photos, video, links, life events).
- **Direct messaging** — private 1:1 and small-group conversation on the same account; in many modern products this lives in a separate companion app that shares the identity.
- **Person-adjacent containers** — groups (member-run topical communities), pages (an organization's or public figure's presence), and events — containers that exist beside the person-centered stream and carry their own membership and rules.
- **Account machinery** — registration, identity handling, age gates, multi-device clients.

### One Structure, Many Implementations

The core is written conceptually; realizations vary along a few stable axes:

```text
Concept:      Connection between members
Realizations: mutual friend ties (both sides confirm) · one-way follow ·
              both layered in one product

Concept:      Consumption surface
Realizations: aggregated feed (ranked or chronological) ·
              visiting connections' profiles (the earlier generation's mode) ·
              a mix of both

Concept:      Identity substrate
Realizations: email or username account · phone number ·
              platform/ecosystem account · real-name norms vs pseudonymity
```

A reader who knows only the current dominant form — a ranked feed over a mutual-friend graph with phone-based identity — should still be able to recognize older or differently positioned products of the same Type: a profile-browsing network with email registration and fully customized profile pages satisfies the same defining core.

## How It Works

### Join and establish the profile

```text
Register an account (identity substrate varies by product)
→ pass age/identity gates
→ set up the profile: name, photo, biographical details
```

### Build the personal connection graph

```text
Search for known people · receive suggestions (often mutual-connection-driven)
→ send an invitation or follow
→ the other side confirms (mutual tie) or the follow stands (one-way tie)
→ the graph grows; removal/unfriend/unfollow stays available
```

There is no operator who assembles a membership: the network is self-organizing, built entirely from members' own decisions about whom to connect with.

### Share an update

```text
Open the composer
→ create content (text / photos / video / link / life event)
→ choose the audience (default audience or per-post selection)
→ publish — the post is attributed to the profile
→ it is distributed along the graph to connected members' consumption surfaces
→ it persists on the profile
```

### Consume and interact

```text
Open the feed (or visit a connection's profile)
→ see updates from the graph
→ react, comment, share, or start a private conversation
→ posts you interact with may widen your own reach through the reactor's graph
```

### Maintain

```text
Adjust privacy and audience settings
→ review notifications
→ manage the graph (accept, remove, block)
→ edit or remove one's own posts (mechanics vary by product)
```

### Tiers

**Defining core** — profile · personal connection graph as the distribution substrate · attributed user-published update stream distributed along the graph · persistent content.

**Standard capabilities** — feed · interactions (react/comment/share) · audience and privacy controls · people discovery · notifications · composer with multiple content forms · messaging surface · groups/pages/events · account machinery.

**Optional / variant** — follow mechanics on top of friend ties · public-default posting · stories-style ephemeral formats · live surfaces · marketplace and commerce surfaces · creator monetization · deep profile customization · super-app bundling (payments, mini-apps, music, dating). Each of these, when it becomes the product's center of gravity, signals drift toward a different Type.

## Interfaces

The surfaces below are described conceptually; exact layouts and names vary by product.

### Feed (home surface)

- Purpose: the member's regular consumption loop over their graph's activity.
- Typical information: updates from connected members and subscribed pages/groups, ordered by the product's ranking or chronology.
- Primary actions: react, comment, share, open the author's profile, compose a new post.

### Profile

- Purpose: one member's persistent identity home — their own for curation, others' for visiting.
- Typical information: photo, name, biographical details, accumulated posts, mutual connections.
- Primary actions (own): edit details, curate visibility, review one's posts. Primary actions (others'): add as connection / follow, message, block, report.

### Composer

- Purpose: creating the update that will be attributed and distributed.
- Typical information: content area, audience selector, attached media.
- Primary actions: attach media, select audience, publish.

### Connections management

- Purpose: building and maintaining the personal graph.
- Typical information: incoming requests, current connections, suggestions, followers where the follow model exists.
- Primary actions: accept, decline, remove, search, invite.

### Notifications

- Purpose: surfacing activity that concerns the member — reactions, comments, connection requests, mentions.
- Primary actions: open the source item, adjust notification settings.

### Messaging surface

- Purpose: private conversation with a known member or small group on the same account.
- Primary actions: send messages and media, start calls (where offered).

### Group / page / event surfaces

- Purpose: the person-adjacent containers — topical communities, organizational presences, coordinated gatherings.
- Typical information: the container's content stream, membership, administrators.
- Primary actions: join/leave, post inside the container, manage (for admins).

### Settings and privacy

- Purpose: standing control over reach and data.
- Typical information: audience defaults, visibility of the profile and of the connection list, blocked accounts, notification rules.
- Primary actions: configure defaults, block/unblock, account maintenance.

## Important Rules / Behaviors

### The graph governs reach, audience settings refine it

Who can see a member's content and interact with them is determined first by the connection graph and second by the audience controls layered on each post and the standing privacy settings. Removing a connection and blocking an account are the two hard levers that sever reach.

### Connection semantics define reciprocity

In the mutual-friend implementation, a tie exists only when both sides confirm, and each side's content flows to the other. In the follow implementation, the tie is one-directional and needs no consent. Products differ on which they use as the base and whether both coexist; within one product the semantics are explicit and visible to members.

### Content is attributed and persistent

A post always remains bound to its author's profile; it persists unless the author removes it or the product applies a specific lifecycle (edit windows and removal mechanics vary by product). Attribution is what makes the network person-centered: the same content surfaces in the feed, on the profile, and in search under the same author.

### Consumption is graph-bounded

The default consumption surface shows the graph's activity, not the whole network. A member who connects with nobody and follows nothing sees almost nothing — a structural difference from broadcast or discovery-first products, where the operator's or algorithm's choices fill the stream regardless of personal connections.

### Identity and admission are gated

Registration is required, products commonly enforce a minimum age, and identity norms vary from real-name enforcement to pseudonymity. The gates exist because the graph is built from identified persons — the network's value rests on members being real, findable people.

### Moderation applies at two levels

Network-wide rules (prohibited content, abuse, impersonation) are enforced by the operator across the whole service, while containers (groups, pages) carry their own membership rules and administrators on top. Reporting flows from members to the operator's review machinery.

## Variants

- **Mutual-friend-first** — the graph is built from confirmed reciprocal ties; the classic personal-contact model.
- **Follow-layered** — follow mechanics added beside friend ties, letting members subscribe to people they do not know personally without granting them reciprocity.
- **Private-graph-first vs public-default** — products differ in whether the default audience of a post is the personal graph or the public; the graph remains the organizing structure either way.
- **Feed philosophy** — ranked-by-engagement as the default, reverse-chronological as the default, or a member-facing choice between them.
- **Focused vs super-app** — some products remain focused on the sharing core; others wrap the core in a large bundle (messaging, calls, payments, music, short video, dating as separate product surfaces under one account). The core profile/graph/feed structure survives bundling intact — observed in a regional super-app whose own user help splits exactly this way: Profile / News / Friends / Communities, with everything else as separate surfaces.
- **Identity norms** — real-name policies versus pseudonymous handles; phone-, email-, username-, or platform-account-based identity.
- **Era styles** — the earlier generation centered consumption on visiting profiles and emphasized deep profile customization; the current generation centers the aggregated feed with standardized profiles. Both satisfy the defining core.
- **Content-type drift** — products that let one media format or one audience definition become the organizing principle are drifting toward the sibling Types (photo-centric, short-form video, professional, neighborhood); the general Type is the unrestricted form.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Microblogging Platform | the sharpest structural overlap; the tie means a subscription to a person's public broadcasts rather than a personal acquaintance, posts are public-first, and discovery-first consumption dominates |
| Photo-centric Social Network / Short-form Video Social Platform | one content format (photos / short video) is the organizing object and creation surface; here content is general-purpose and the person is the organizing key |
| Professional Social Network | identity and sharing are framed by career and professional context; here the frame is unrestricted personal life |
| Neighborhood Social Network | membership is gated by verified locality; here membership is not geographically bounded |
| Interest-based Social Network | interests or topics, rather than the personal connection graph, key what is distributed and consumed |
| Friend Discovery Application | forming new relationships with strangers is the primary job (discovery → contact formation is the core loop); here the graph starts from people already known and discovery is an auxiliary loop |
| Social Profile Network | profiles and connections exist without a shared update stream — a people directory rather than a sharing network; removing the update stream from this Type yields that form |
| Online Forum / Community Platform | content is organized in topic containers and threads (often under a community operator); here content is organized by who posted it, in a self-organizing member graph |
| Instant Messaging Application | private direct conversation between specific participants; messaging inside a social network is a bundled capability on the same account, not the organizing structure |
| Dating Application | romantic-partner intent with a mediated contact gate; here relationships are unrestricted and unmediated |
| Social Live Streaming Platform | ephemeral live broadcast with simultaneous viewers; here updates are persistent and attributed |

The load-bearing boundary inside the family is the one with microblogging: both Types have profiles, follows, and posts. The difference is what the connection *means* and what the feed *is for* — acquaintance and personal-life sharing in one, subscription and public discourse in the other. Modern products blur the edge by shipping both mechanics, so the assignment follows the product's center of gravity.

## Representative Products

- Facebook — the canonical general social network and the Type's center of gravity
- VK — a regional general social network whose core (profile / news / friends / communities) ships inside a super-app bundle
- MySpace — the dominant general social network of the mid-2000s generation; today a music-forward remnant that still retains the profile-and-connection skeleton
- Mixi — a major regional (Japan) general social network of the same era

The definition was written to be checkable against older and regional forms: the profile-browsing-era generation (customization-heavy profiles, email/username identity, no feed as home surface) and the regional super-app form both satisfy the defining core without any of the modern specifics.

## Sources

Research date: **2026-09-07**

- VK — Support portal section taxonomy (Profile management / News / Friends / Communities and super-app surfaces): https://vk.com/support (retrieved 2026-09-07)
- MySpace — live product surface (role-typed profiles, people connection framing, Discover > People): https://myspace.com/ (retrieved 2026-09-07)
- MIXI — corporate site (company positioning; consumer-sharing lineage): https://mixi.co.jp/ (retrieved 2026-09-07)

> Sourcing limitation: the canonical product's (Facebook) help center and terms pages were not reachable from the research environment on 2026-09-07 (repeated transport errors), VK support article bodies and developer documentation are login- or JavaScript-walled, and the service surfaces of Mixi and of the historical generation were not directly examinable. The document therefore keeps all claims at the structural and conceptual level: no numeric limits, defaults, or product-specific feature claims are asserted, and single-sample observations are stated as such where they appear. Detailed product-by-product observations and the cross-product comparison are recorded in the paired Research Notes.
