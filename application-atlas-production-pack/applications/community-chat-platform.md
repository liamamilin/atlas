# Community Chat Platform

## Overview

A **Community Chat Platform** is a chat application organized around joinable communities: people join a community first, and converse in named rooms that live inside it. The community — not the room and not a personal contact — is the top-level unit: it holds the members, owns the rooms, and carries the roles and rules that govern both.

The defining structure is small:

```text
Community — an identified community that people join
└── Membership held at community level (above and across
    all of the community's rooms)
    └── Rooms — named chat places owned by the community
        └── Shared real-time message stream per room
```

Everything else the market associates with this kind of product — role hierarchies, moderation tooling, invite links and public discovery, server-side history, voice rooms, bots, per-room notification controls — is standard capability layered onto that container, not what makes the product what it is.

The boundary that matters most: when the room itself is the top-level unit — a standalone addressable place that people join by its own address, with no membership above it — the product is a **Chat Room Application**. When membership derives from an organizational roster, it is **Team Messaging**. When the community's primary surface is asynchronous content (posts, topic threads, profiles) rather than live rooms, it is a **Community Platform**.

## Users & Context

The primary user is a **member**: someone who joins a community built around a shared interest, identity, or activity — gaming groups and guilds, study groups, hobby and interest communities, open-source project communities, creator and fan communities, or simply a friend group that wanted a place of its own. Typical reasons to open the application:

- take part in the ongoing conversation in one or more of the community's rooms
- follow specific topics by staying in the rooms dedicated to them
- ask questions or get help in a community's support or discussion room
- coordinate with the group — events, plans, announcements
- hang out: for many members the community's rooms are a place to be, not a task to complete

The second, equally defining role is **community staff** — the owner, admins, and moderators who created or inherited the community. They set up its rooms, define roles and who holds them, configure who may join and what newcomers see, and enforce the community's rules. Community-level governance is a feature of this Type, not an administrative afterthought: policy inside the community is set by its staff, separately from the platform's own rules.

A third, lighter role is the **bot or integration operator** — often a staff member — who connects bots and external services to extend what the community's rooms can do.

Context of use: desktop and mobile applications and web clients; hosted services, self-hosted servers, and federated open protocols all occur. Communities range from a handful of friends to large public communities with thousands of members; the same structures serve both.

## Core Model

### The Defining Core

**The community.** The central object is the community itself: an identified, joinable container with its own identity — a name, an icon or avatar, usually a description of its purpose — and an existence that does not depend on any particular member or conversation. Products call it a server or a space; the concept is the same. Joining it is the entry act, and membership is held at the community level: a member is a member of the community as a whole, above and across all of its rooms, and remains a member while offline.

**Rooms underneath.** Inside the container, conversation happens in **rooms** — named places owned by the community, each with its own stream. A community normally holds many rooms, organized by topic or purpose. Rooms are where the community's life actually happens; the container exists to hold them together under one membership, one identity, and one governance layer.

**The shared real-time message stream.** Within a room, participants post messages to one shared stream and see each other's messages live. Replies, mentions, and reactions layer onto the stream; files, links, and embedded content flow through it.

### Standard Capabilities

Around this core, mature products add a stable set of structures:

**Roles and permissions.** Communities carry a role hierarchy — typically owner, administrators, moderators, and regular members — with permissions configured per role or per action: who may send messages, invite others, manage rooms, change settings, or moderate. Role-based permission systems are the standard way community staff delegate governance.

**Moderation.** Community staff have tools to keep the community in order: removing members from a room or the whole community, banning, muting or timing out disruptive members, and deleting or restricting content. Many communities also run moderation bots that automate parts of this.

**Join machinery.** People join through invite links, community addresses, or public discovery. Many platforms maintain a **discovery surface** — a public directory of communities — with listing rules; being listed can come with expectations (active moderation, compliance with platform rules), and being unlisted or invite-only is equally normal.

**History.** A room's past conversation is the community's shared memory. In modern products history is kept server-side and survives every member's absence; what a newcomer may read — everything, or only what was sent after they joined — is a policy the community controls, and some products let outsiders preview a room before joining.

**Member roster and profiles.** The community holds a member list; members have profiles (display name, avatar) visible across the community's rooms.

**Notifications.** Because a member may belong to many rooms across several communities, per-room notification levels (muted, mentions only, all messages), name and keyword mentions, and unread indicators are structural, not extras.

**Voice alongside text.** Voice conversation is standard, realized either as dedicated voice rooms that exist alongside text rooms or as calls that happen inside a room.

**Extensions.** Bots, webhooks, and integrations connect the community's rooms to external services — games, feeds, tools — and are a standard part of running a community.

**Direct messages.** Members can usually message each other privately. Direct messages exist as a side surface of co-membership — not as the organizing structure.

### One Structure, Many Implementations

The Core Model is written in conceptual terms; implementations differ:

```text
Concept:     Community container
Realized as: servers, spaces, guilds — the product's top-level unit

Concept:     Membership
Realized as: platform accounts joined to the community; federated
             user IDs on open protocols

Concept:     Rooms
Realized as: text and voice channels under a server; rooms grouped
             under a space (rooms may belong to more than one
             container, and containers may nest)

Concept:     Governance
Realized as: role hierarchies with per-action permissions;
             platform-level rules enforced above the community
```

A reader who has only seen one kind of community chat product should still be able to recognize a self-hosted open-source community server or a federated protocol's public spaces as the same Type from this model.

## How It Works

### Create or join a community

```text
Create:  pick a name, icon, and description
         → choose the access mode (public / invite-only)
         → the community exists; its creator holds the top role

Join:    follow an invite link, enter a community address,
         or find the community in a public directory
         → the community's access mode decides who can join
         → become a member of the community as a whole
```

There is no organizational roster behind this: membership comes from the join act itself, and the community's staff govern who stays.

### Take part in rooms

```text
Open the community → see its room list
→ enter a room → read the stream (and, per the room's policy,
   the history before you arrived)
→ post; reply, mention, react; share files and links
→ switch between rooms freely — membership carries across all of them
→ join a voice room or start a call where voice is offered
```

### Govern the community

```text
Define roles (owner / admin / moderator / member, or finer)
→ attach permissions to roles or actions
→ create and organize rooms; set per-room access
→ set the community's rules
→ moderate: remove, ban, mute, delete content
→ connect bots and integrations to extend the rooms
```

### Stay current

```text
Keep many rooms and communities at once (sidebar with unread states)
→ rely on mentions and per-room notification levels
→ return later and read back through room history
```

### Capability tiers

**Defining core** — without these, not a Community Chat Platform:

- joinable community container with its own identity
- membership held at community level, persisting across rooms and while offline
- multiple named rooms owned by the community
- shared real-time message stream per room

**Standard capabilities** — present in essentially all mature products:

- roles and permission hierarchy; moderation tools
- invite links / addresses; discovery surfaces on the platform side
- server-side persistent history with visibility policy
- member roster and profiles
- per-room notification levels, mentions, unread indicators
- messaging machinery (replies, reactions, formatting, media)
- voice alongside text; bots/integrations; member-to-member direct messages

**Common variants** — depend on product philosophy and deployment:

- hosted consumer service vs open-source self-hosted vs federated protocol
- publicly discoverable vs unlisted/invite-only communities
- per-room or per-container end-to-end encryption
- how far the container extends beyond chat (events, forums, media)
- identity substrate (platform account vs federated ID)

## Interfaces

The surfaces below are described conceptually; exact layout and naming vary by product.

### Community sidebar / room list

The user's home surface: the communities they belong to, and inside each, its rooms — with unread indicators and notification states. Primary actions: switch community, open a room, join a new community, manage notifications.

### Room conversation view

The core surface: the live message stream, the room's name and topic, and the input line. Primary actions: send a message, reply/mention/react, share files, read and search history where policy allows.

### Voice room / call surface

Where voice exists as voice rooms, a surface showing who is currently speaking in each; where voice exists as calls, an in-room call surface with mute/camera/end controls.

### Member list

The community's roster (and, in some products, per-room presence), showing roles. Primary actions: inspect a member, mention them, start a direct message; for staff, moderate.

### Community settings and roles

The staff surface: community identity (name, icon, description), join configuration, rules, role definitions with their permissions, room creation and organization, integration/bot management.

### Moderation surfaces

Staff tools for acting on members and content: removal, bans, mutes/timeouts, and content deletion.

### Discovery surface

The platform's public directory of communities, showing name, description, and member activity. Primary actions: preview and join. Listing usually carries platform requirements (active moderation, rule compliance).

### Notification settings

Global and per-room levels (mute / mentions only / all messages), keyword configuration, and delivery channels (desktop, mobile push, email digests).

## Important Rules / Behaviors

**Governance is two-layered.** Community staff set and enforce the community's own rules; the platform sits above with rules that bind all communities, and can act at platform level — suspending accounts, removing a community from public listing, or removing it from the platform entirely. Publicly listed communities may carry explicit moderation obligations as a condition of listing. In federated deployments the "platform" role is played per server: each server's administrators set their own abuse policies above the communities they host.

**Membership is at community level; room access is a separate control.** Joining the community does not mean access to every room. Rooms can be open to all members, restricted by role, or private; a room's visibility and its joinability are controlled separately — a room can be listed so people know it exists while still restricting who may enter.

**Joining does not guarantee speaking.** Permission settings can restrict who may post in a room; moderation actions target individual members. Access denials and removals are the community staff's deliberate decisions, with the platform's rules as the backdrop — not errors to work around.

**History visibility is a policy, not a constant.** What a newcomer may read — the full past, only messages sent after they joined, or a preview before joining — is configured per room, and changing a room's access does not retroactively change what past messages are visible.

**Communities persist apart from their members.** A community outlives any member's presence or absence; ownership and roles are meant to survive turnover. Membership counts are a meaningful, even governed, quantity — some platforms explicitly prohibit artificially inflating a community's membership.

**Notification control is structural.** Members typically belong to many rooms across several communities; without per-room mute levels and mention triggers, participation at this shape is impractical.

**Pseudonymity and identity vary.** A member is known by a display handle; how durable the underlying identity is — platform account, federated ID — depends on the product. The community's rooms, not personal contact relationships, define who converses with whom.

## Variants

- **Hosted consumer platforms** — the category's public image: large hosted services with free access, public discovery, and rich community tooling; communities range from friend groups to very large public ones.
- **Open-source, self-hostable platforms** — the same container structure as installable software; a community can be hosted by its own operators, with public APIs and bot ecosystems around it.
- **Federated protocol networks** — communities and rooms on an open protocol, spread across cooperating servers; rooms and containers can be reachable across servers, and bridges connect them to other chat systems.
- **Gaming-origin and content-rich communities** — products that extend the container with non-chat modules (events, forums, media, scheduling) so the community's whole life lives in one place; depth varies widely by product.
- **Private / invite-only communities** — unlisted communities joined by invitation; fully valid instances of the Type, differing only in discovery posture.
- **Voice-heavy communities** — communities whose rooms are primarily voice; a matter of emphasis within the Type rather than a separate one.
- **Audience variants** — gaming guilds, study groups, interest and hobby communities, open-source projects, creator and fan communities, friend groups; the structures are the same, the norms differ.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Chat Room Application | the room is the top-level unit — a standalone addressable place joined by its own address, with no membership above it; here the community is the top-level unit and rooms live underneath |
| Team Messaging Application | channels are room-shaped but membership derives from an organizational roster and org identity; communities are joined by self-service around a shared interest, and strangers are expected |
| Group Messaging Application | a member-defined private thread among known people, invitation-flow, no container holding many rooms |
| Instant Messaging Application | person-addressed threads bound to a personal contact graph; here conversation is place- and container-addressed |
| Community Platform (forum-style) | the community's primary surface is asynchronous content — posts, topic threads, profiles; here the primary surface is live rooms |
| Interest-based Social Network | the primary surface is profile, feed, and follow graph around an interest; chat is secondary |
| Social Live Streaming Platform | room-shaped chat subordinate to a live broadcast; the primary object is the stream |
| Social Audio Platform | voice-first stages rather than text-first rooms under a community container |
| Member Community Platform (associations) | membership is a managed organizational relationship with benefits and dues; chat rooms are at most one member benefit |

The most important boundary is the one against **Chat Room Application**: both are full of rooms with join/leave participation. The structural test is what the user joins first — the community (membership, roles, many rooms underneath) or the room itself (standalone place). The boundary against **Team Messaging** is the second key seam: whether membership comes from an organizational roster or from the join act itself.

## Representative Products

- **Discord** — the category-defining hosted consumer platform (market anchor; its documentation was unreachable during research, so no product-specific claims are drawn from it)
- **Guilded** — hosted gaming-community competitor (market anchor; documentation likewise unreachable)
- **Stoat (formerly Revolt)** — open-source, self-hostable community group chat with a platform-level community directory
- **Element** — client for the Matrix federated room network; its Spaces provide the community-container layer over room-based messaging

The definition was checked against room-first systems (IRC-tradition networks and portal-era rooms, documented in the paired Chat Room Application research) to confirm that the community container — not rooms, not accounts, not server-side history — is what distinguishes this Type.

## Sources

Research date: **2026-09-07**

- Stoat (Revolt) — product page https://revolt.chat/ ; support KB https://support.stoat.chat/ (Server Management, Safety incl. "Guidelines for servers on Discover", Interface/Messaging, Account) ; Community Guidelines https://stoat.chat/legal/community-guidelines
- Element — help/FAQ https://element.io/help ; user guide https://element.io/user-guide ; docs https://docs.element.io/latest/ (Understanding Matrix Spaces; Creating a Space)
- Discord — https://discord.com/developers/docs/intro , https://support.discord.com/hc/en-us , https://discord.com/moderation (all unreachable; market anchor only)
- Guilded — https://www.guilded.gg/ , https://www.guilded.gg/about (unreachable; market anchor only)

> Sourcing limitation: Discord's and Guilded's official documentation could not be fetched from the research environment (repeated timeouts), and Rocket.Chat's docs (a drift-test candidate) were likewise unreachable. The hosted consumer pole of this Type is therefore described structurally, from the reachable products and cross-product reasoning, and no precise operational details (numeric limits, default settings, discovery-tier mechanics, monetization structures) are asserted for any product in this document. Product-specific details are recorded in the paired Research Notes.

Detailed product-by-product observations, the cross-product comparison matrix, and the historical / market-sample breadth check are recorded in the paired Research Notes.
