# Online Forum

## Overview

An **Online Forum** is a self-standing web venue where a community of members discusses topics organized into boards, accumulating a persistent, searchable archive of conversation.

It solves a specific problem: a group of people with a shared interest needs a place of its own on the web — a place with a name, an address, its own member population and its own rules — where conversations happen by subject rather than by moment, and where what is said stays findable instead of scrolling away.

The defining core is small:

```text
A self-standing venue of its own
└── Boards organizing member-opened topics
    └── Asynchronous replies accumulating into persistent threads
Members join the venue and carry identity, standing and history across it
```

Everything else commonly associated with forum software — member ranks and badges, moderation queues, notifications, search, private messaging, polls, chat channels — is standard equipment in mature products but is not what makes a forum a forum. Older and simpler forms (the classic self-hosted board of the 2000s, or a dial-up-era bulletin-board system) satisfy the same core without any of them.

## Users & Context

The primary user is a **member**: a person who has joined the venue because it hosts discussion they care about — the community around a product, an open-source project, a hobby, a game, a profession, a locality. Members read topics, open their own, reply to others, and return over months or years. The member's standing in the venue — profile, post history, recognition — is part of the experience and often part of the motivation.

Supporting roles shape the venue rather than the conversation:

- **Administrators** run the venue itself: install or configure the software, organize the boards, set who may see and post where, define the rules, and manage staff.
- **Moderators** keep discussion within the rules: reviewing flagged content, editing or removing posts, moving and merging topics, and steering disputes.
- **Trusted regulars** — in many mature venues, long-standing members are granted additional abilities that let them carry part of the moderation load themselves.

Typical settings: public interest communities, product and support communities, open-source project forums, game and hobby communities, and members-only venues for organizations or paid memberships.

## Core Model

### The Defining Core

Three structures, held together. If any one is removed, the product is no longer recognizable as an online forum.

- **A self-standing venue of its own.** The forum is a named, addressable place on the web with its own identity — its own site, its own member base, its own rules — that exists before and between conversations. The software's deployment unit is one such venue. Without this, the product is a discussion tool embedded in something else (a course, an organization, a product page), not a place people belong to.
- **Board-organized topic discussion.** The venue's world is organized into boards or areas — called forums, categories, nodes or tags depending on the product — each holding topics that members open with a subject and a seed post. Other members reply asynchronously over hours, days or years; a topic and its replies form a persistent thread, and the archive remains readable and searchable at the venue. Without the board organization, content organizes by author and time — that is a social network; without the asynchronous topic-with-replies structure, conversation is a live stream — that is chat; without persistence, the venue has no archive — that is an ephemeral surface.
- **A standing member base with venue-level identity.** The community is a persistent population of people who join the venue — by open registration, invitation, or approval — and carry identity, standing and history across all of its boards: a profile, a post history, often a visible rank or reputation. The membership belongs to the venue itself. Without it, posts are anonymous wall-writing; where joining and membership are managed by an operating organization's apparatus, the product is drifting toward community-platform territory.

The three are load-bearing together. A venue without boards is just a website; boards and topics without members are a tool; members without a venue of their own are an account list.

### Standard Capabilities of Mature Products

These are widespread in current forum products and expected by members, but they equip the core rather than define it:

- **Member profiles and user groups** — identity surfaces (avatar, history, statistics) and groupings used for both community structure and permissions.
- **Registration and authentication variety** — email/password, social login, single sign-on, two-factor authentication, invitation flows.
- **Topic lists with read state** — each board's home surface: topics ordered by latest activity or popularity, with unread indicators and filters.
- **Search** — because the archive is the venue's main asset, search across topics and posts is a first-class surface.
- **Notifications and subscriptions** — members watch topics or boards and are notified of replies; email digests and reply-by-email are common participation channels.
- **Moderation toolkit** — staff-only surfaces for reviewing flagged content, approving posts, and editing, moving, merging, splitting, closing, pinning, locking or removing topics and posts.
- **Reputation and recognition** — ranks, badges, points or trust systems that surface experienced members and, in some products, unlock abilities as members earn standing.
- **Rich posts** — formatting, images, attachments, quotes, reactions, post revision history.
- **Private messaging** — member-to-member exchanges kept separate from public topics.
- **Polls and special post types** — votes embedded in topics; collaboratively edited wiki-style posts; anonymous posting modes.
- **Administration surface** — site configuration, per-board permissions, appearance and theming, integrations, and an API.
- **Public-archive posture** — public venues are typically indexed and searchable from the wider web, which is part of how forums accumulate long-term value.

### One Structure, Many Implementations

The core model is conceptual; products realize each piece differently:

```text
Concept:                 Self-standing venue
Implementations:         self-hosted open-source software,
                         vendor-hosted commercial platform,
                         vendor cloud subscription

Concept:                 Board organization
Implementations:         category trees, forum/node hierarchies,
                         tag systems, hybrid

Concept:                 Member identity and standing
Implementations:         registered accounts with profiles,
                         ranks/badges, trust or reputation ladders,
                         user groups

Concept:                 Thread layout
Implementations:         flat reply streams with in-place context,
                         classic threaded trees, paged or scrolling
```

A reader who has only seen one realization — say, a modern hosted community platform — should still be able to recognize a classic self-hosted board from the core model alone.

## How It Works

### Establish the venue

An administrator sets up the venue: install or configure the software, name the site, organize the board structure, define who may see and post in each board, and write the venue's rules. Access configuration is structural — visibility of a board decides whether a member or visitor can even see the topics inside it. A staff-only administration surface, separate from the member-facing front-end, is where this configuration lives in every mature product.

### Join the venue

```text
Visitor arrives at the venue
→ reads topics (in open venues, without an account)
→ registers (or is invited / approved)
→ becomes a member with a profile
→ can now open topics and reply where permissions allow
```

Joining is a one-time act with venue-wide effect: membership applies to the whole venue, not to individual boards (board-level permissions gate *what* a member may do where, not *whether* they belong).

### Discuss

```text
Member opens a topic (subject + seed post) in a board
→ the topic appears in the board's topic lists
→ other members reply over time — minutes or months
→ the thread accumulates; late readers get the full exchange
→ activity moves the topic up the lists; interested members subscribe
→ the thread remains readable and searchable indefinitely
```

This loop is asynchronous by design: nobody must be present at the same moment, and the value of the archive compounds as threads accumulate. In several modern products, informal chat exists as a side surface, with the explicit expectation that anything worth keeping gets continued in a topic — the topic is where durable conversation lives.

### Govern

Moderators watch flagged or problematic content, then edit, move, merge, split, close, pin or remove it — usually softly, keeping the record intact. Venue rules are typically published to members. In many venues, reputation or trust systems let experienced members carry part of this load: flagging, approving, or editing, with abilities earned through accumulated standing rather than appointment.

### Capability tiers

- **Defining core** — a self-standing venue; board-organized member-opened topics with asynchronous replies; persistent readable threads; a standing member base with venue-level identity.
- **Standard equipment** — profiles and groups; registration variety; topic lists with read state; search; notifications and email participation; moderation toolkit; reputation and recognition; rich posts; private messaging; polls; administration surface; public-archive posture.
- **Variant / optional** — chat channels as a side surface; question-and-solution thread types; wiki posts; anonymous posting; invite-only or private spaces; mailing-list-style email participation; AI assistance; mobile apps; add-on surfaces such as media galleries or resource libraries.

## Interfaces

Exact layouts and names vary by product; the surfaces below are described conceptually.

### Board index (venue home)

The front door of the venue.

- lists the boards/areas, often grouped, with topic counts and latest activity
- shows venue-level state (new topics, unread activity, who is online in some products)
- primary actions: browse into a board, search, log in / register

### Topic list (per board)

The surface where a board presents its conversations.

- topics with subject, author, reply count, latest activity, unread state
- ordering (latest activity, popularity) and filters
- primary actions: open a topic, start a topic, filter, subscribe

### Thread view

The surface where one discussion lives.

- seed post first, replies after — sequentially or nested where threading is supported
- per-post authorship, timestamps, quotes, reactions, revision history
- primary actions: reply, quote, react, share; for staff: edit, move, close, pin, delete

### Composer / reply editor

- formatting, attachments, images, previews, drafts
- primary actions: submit, preview, attach

### Member profile

The member's identity surface within the venue.

- display name, avatar, post history, statistics, recognition (ranks/badges)
- primary actions: message the member, view their topics and posts, adjust own settings

### Search

- query across topics and posts; results link into threads
- often the main way returning members relocate a past discussion

### Notifications / subscriptions

- watched topics and boards, reply notifications, digests; email as a common channel

### Moderation / administration surfaces

- staff-only: flagged-content queues, member management, board structure and permissions, site configuration, appearance, rules
- separate from the member-facing front-end by design

## Important Rules / Behaviors

### Asynchrony and persistence are the point

The forum is deliberately not real-time. Threads are expected to span days or years; the persistent archive is the venue's main asset and the reason conversations are held there rather than in chat. Products in this family articulate the contrast themselves: discussion that matters goes in topics precisely because it persists.

### Topics have managed states

A topic can typically be closed to further replies, pinned for visibility, or archived; closed topics usually remain readable — the record survives even when the discussion ends. Exact state names vary by product.

### Access is structural

Who may see and post in each board is configured per board (and per group). In tree-organized products visibility behaves hierarchically: no access to a parent means no access to what is inside it. Open public venues, invite-only venues, and private members-only boards inside an open venue are all common postures; the mechanism — board-level permission — is the same.

### Membership carries standing

A member's identity, history and recognition are visible in the conversation (on posts and profiles). In products with reputation or trust systems, accumulated standing can change what a member is allowed to do — an unusual rule structure in which the community's own history gates capabilities.

### Moderation is usually soft

Removed posts and topics often remain in the record (hidden or anonymized) rather than vanishing, preserving thread integrity and accountability. Venue rules are typically published, and moderation actions are expected to be defensible against them.

## Variants

- **Classic self-hosted board** — software installed on the operator's own server; board tree, member ranks, moderator roles; the long-dominant shape.
- **Modern hosted platform** — the vendor hosts and operates the software as a service; flat scrolling layouts, integrated chat, trust systems, analytics; common for organization-run communities.
- **Minimal extension-driven board** — a small core with everything else added through extensions; demonstrates how little the defining core actually is.
- **Forum-first commercial suite** — the forum as the core product with paid add-on surfaces (media galleries, resource libraries, enhanced search).
- **Support communities** — venues organized around getting answers; question-and-solution thread types layered onto the discussion core.
- **Org-run forums** — companies and projects running their customer or user communities on forum software; the overlap zone with the Community Platform type.
- **Members-only venues** — access gated by invitation, approval or paid membership; the venue core is unchanged.
- **Older forms** — dial-up-era bulletin-board systems (one system = one venue, message areas = boards, user accounts = members) satisfy the same core; Usenet newsgroups and mailing lists do not (no venue of its own, no member base) and belong to the discussion-surface lineage rather than the forum lineage.

A variant remains a variant unless it changes the core: if member profiles, feeds and events become the primary surface, it is a community platform; if the primary object becomes live chat rooms, it is a community chat platform.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Discussion Board | nearest neighbor; the two overlap so heavily in everyday usage that they share one product family. A defensible line: the discussion board is the discussion *tool/surface* (topic + reply machinery), which also exists embedded without any public venue — course boards, organizational boards; the online forum is the *standing venue of its own* built on that machinery — site identity, member base, governance. Every standalone forum product instantiates both; the two types answer different questions |
| Community Platform | an operated container: an organization manages membership and offers multiple surface families (discussions, groups, events, content, directory) with operator measurement; the forum is the venue itself, organized around boards, with membership belonging to the venue. A forum can be one surface inside an operated container; organizations running their communities on forum software form the documented overlap zone |
| Interest Community Platform | hosts many joinable communities as first-class units under one account; in a forum, boards are sections of one venue — they do not carry their own joinable membership or scope |
| Q&A Community | question + answer + accepted-answer structure is the primary organizing principle of the whole venue; in a forum, that machinery is a thread-type capability |
| Community Chat Platform | primary surface is live chat rooms under a container; the forum is asynchronous, topic-structured and persistent by design; chat appears in forums only as a side surface |
| Social Network / Microblogging | content organized by who posted it (profiles, follow graphs, feeds); forum content is organized by topic containers with a standing venue membership |
| Blogging Platform | centers one author's publication with readers reacting; a forum is a venue where members themselves open the topics. Comments do not make a blog a forum |
| Comment System | comments attach to a content item; a forum is a standing venue independent of any single item |

**Note on the Discussion Board boundary:** the standalone products that embody this type are the same market family the Discussion Board type describes, and "forum", "discussion board" and "message board" are near-synonyms in everyday usage. This document treats the online forum as the venue type — defined by the standing place, its member base and its governance — while the Discussion Board document treats the surface type, defined by the topic-and-reply machinery itself; each document points at the other's pole, and the shared product family is acknowledged on both sides.

## Representative Products

- **Discourse** — modern open-source discussion platform with commercial hosting; flat scrolling topics, categories and tags, trust system, badges, bundled chat as a side surface
- **XenForo** — classic commercial self-hosted forum software with a cloud option; node tree of forums, thread/post model, per-board permissions, optional add-on surfaces
- **Flarum** — minimal open-source forum, extension-driven; tags as the organizing layer

The defining core was checked against older and simpler forms (the classic self-hosted board lineage, dial-up-era bulletin-board systems) and against the neighboring multi-community and operated-container product shapes, to avoid defining the type by today's hosted-community implementation.

## Sources

Research date: **2026-09-08**

- Discourse — official about and features pages: https://www.discourse.org/about , https://www.discourse.org/features
- XenForo — official Administrator's Manual (index and structure): https://xenforo.com/docs/xf2/manual/
- Flarum — official documentation (About): https://docs.flarum.org/

> Sourcing limitation: several candidate sources could not be reached during research (phpBB userguide and Invision Community returned access errors; ProBoards serves a JavaScript-only shell; XenForo manual section pages redirected to the manual index from the research environment). The classic-forum pole is therefore evidenced through XenForo's manual and Flarum's documented lineage, and product-specific capability details for unreachable products are not asserted. Precise operational details (numeric limits, rate limits, exact state names) are intentionally not stated in this document.

Detailed evidence, product-by-product observations, cross-product comparison, and the historical / market-sample breadth check are recorded in the paired Research Notes.
