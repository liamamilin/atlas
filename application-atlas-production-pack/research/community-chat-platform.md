# Research Notes — Community Chat Platform

## Research Goal

Understand the Application Type "Community Chat Platform" (DIRECTORY 01.01) from real products: what the community container is, how rooms relate to it, how people join, how governance works, and where the Type's boundaries sit against Chat Room Application, Team Messaging, Group Messaging, Instant Messaging, and the Community Platform family (01.06).

This leaf carries a prior joint-review flag from the processed sibling `chat-room-application` (2026-09-06): the boundary was held on the "place test" (room-first) vs "container test" (community-first), with joint review recommended once Group Messaging, Team Messaging, and Community Chat Platform were processed. This pass is the Community Chat Platform side of that review; Group Messaging and Team Messaging remain unprocessed.

## Initial Boundary

Working hypothesis before research:

- A Community Chat Platform is chat organized around a **joinable community container** (Discord-class "server"): users join the community first, then converse in rooms underneath it.
- Closest neighbors: Chat Room Application (room-first, no container), Team Messaging Application (org-roster membership behind room-shaped channels), Group Messaging Application (member-defined private threads), Community Platform family 01.06 (content/forum-centric communities).
- Expected defining difference from Chat Room: **what the user joins first** — the community (membership, roles, many rooms underneath) or the room itself (standalone addressable place).

## Research Questions

1. What is the top-level container called and what does it hold (identity, membership, rooms, roles, settings)?
2. What does joining mean — is membership at community level, above individual rooms?
3. How do people join (invite links, public discovery, addresses) and how is joining gated?
4. What roles and permission structures exist at community level vs room level?
5. How does moderation work — community-level vs platform-level (two-layer governance)?
6. What room types exist (text, voice, others) and how do rooms control access?
7. What history and notification machinery exists?
8. How do bots/integrations extend communities?
9. Where exactly is the seam vs Chat Room Application, Team Messaging, Group Messaging, and the 01.06 Community Platform family?
10. Historical check: would older or differently positioned products (IRC networks, portal-era rooms, voice-first community servers) fit the definition?

## Representative Products

| Product | Pole | Why selected |
|---|---|---|
| **Discord** | hosted consumer archetype | The category-defining hosted platform; market anchor |
| **Guilded** | hosted gaming-community competitor | Second hosted pole; market anchor |
| **Stoat (formerly Revolt)** | open-source, self-hostable | Open-source/self-host philosophy; community-run governance model |
| **Element (Matrix)** | federated protocol-native | Open protocol, federated deployment; Spaces as container layer over a room network |

Discord and Guilded were selected as market anchors but their documentation was unreachable (see Sources); they are used structurally, with no product-specific claims drawn from them. Stoat and Element provided the direct evidence base.

## Sources

Fetched 2026-09-07:

- Stoat (Revolt) product page — https://revolt.chat/ (serves the Stoat product; "Revolt Platforms Ltd")
- Stoat support KB index — https://support.stoat.chat/ (Account / Interface / Safety / Server Management / Troubleshooting)
- Stoat KB: Server Management — https://support.stoat.chat/kb/server-management ; Integrations & Bots — https://support.stoat.chat/kb/server-management/integrations-and-bots
- Stoat KB: Safety — https://support.stoat.chat/kb/safety ; Guidelines for servers on Discover — https://support.stoat.chat/kb/safety/discover-guidelines
- Stoat KB: Interface/Messaging — https://support.stoat.chat/kb/interface/messages ; Account — https://support.stoat.chat/kb/account
- Stoat Community Guidelines — https://stoat.chat/legal/community-guidelines
- Element help/FAQ — https://element.io/help
- Element user guide — https://element.io/user-guide
- Element docs — https://docs.element.io/latest/ ; Understanding Matrix Spaces — https://docs.element.io/latest/element-support/matrix-spaces/understanding-matrix-spaces/ ; Creating a Space — https://docs.element.io/latest/element-support/matrix-spaces/getting-started-creating-a-space/

Unreachable (abandoned per network-restriction rule):

- Discord: https://discord.com/developers/docs/intro (timeout), https://support.discord.com/hc/en-us (timeout), https://discord.com/moderation (timeout) — 3 failures, vendor abandoned
- Guilded: https://www.guilded.gg/ (timeout), https://www.guilded.gg/about (timeout) — 2 failures, vendor abandoned
- Rocket.Chat docs: https://docs.rocket.chat/ (timeout), https://rocket.chat/docs (timeout) — 2 failures, abandoned (was a drift-test candidate)
- matrix.org / spec.matrix.org: unreachable in the prior sibling pass (2026-09-06) and not retried here; Matrix-side evidence rests on Element's own Tier-1 surfaces

## Product Observations

### Stoat (formerly Revolt) — open-source community group chat

Evidence layer: A (direct observation from official product page, support KB, community guidelines).

- Positioning: "the open-source group chat app for friends and communities"; explicitly serves "your community, raid guild, study group, and anything in-between" (product page; community guidelines).
- Top-level container: **servers**. Product page: "Servers, channels, voice chat, file sharing, markdown support, and all the rest." Scale framing: "Whether you're chatting with a handful of friends or running a bustling community, Stoat scales with you. The tools work the same, no matter how big you get."
- Governance: "Manage your community with an intuitive role-based permissions system, powerful moderation tools, and the best moderation bots in class."
- Membership metrics are a governed concept: community guidelines prohibit "Selling, purchasing, or providing means to artificially grow servers" (botting, artificial inflation of server membership or engagement) and prohibit "Selling and purchasing of servers" (with an exception for servers sold as part of a larger brand/company sale, subject to approval). This implies servers are persistent, ownable community units with membership counts that matter.
- Two-layer governance, platform side: Community Guidelines "apply to all users, communities, and content on Stoat"; violations bring strikes/suspensions at platform level; ban evasion prohibited. Platform sits above communities.
- Two-layer governance, community side: servers listed on the platform's **Discover** surface must "ensure users follow our Acceptable Usage Policy", ensure associated off-platform communities abide by the rules, and "report and delete violating content within a reasonable timeframe"; poorly moderated servers "may be removed from Discover" or "temporarily removed from the platform". Discover-listed servers are automatically enrolled in analytics (activity ranking) and (in testing) automatic moderation.
- Discovery: a platform-level directory ("Discover") of servers, with listing guidelines and anti-manipulation rules ("not intentionally manipulate their own position on Discovery"; not listed "for the sole purpose of promoting an external service").
- Extensions: "Integrations & Bots — All you need to know before connecting external services and bots to spice up your server"; webhooks documented.
- Messaging surface: message formatting and replying documented in the Interface KB.
- Identity/account: accounts with badges, deletion, partial PII deletion; minimum age requirements; spam-block policy.
- Deployment: hosted service plus self-hosting ("You don't have to worry about hosting your own server if you don't want to, but if you do, we've got you covered. It's free, it's open, and it's yours"); public API ("Our public API is so powerful that we use it ourselves for the official apps"); multi-platform clients (Windows/macOS/Linux/Android/iOS/web).
- Product-specific details (L3, not for final doc): group DMs support up to 50 members; 20 MB file upload limit free; custom emojis free; CSS theming; EU data-storage jurisdictions (UK operator; data in Germany/Finland/Netherlands; media in Netherlands); Revolt→Stoat rebrand (site now brands the product "Stoat", operator "Revolt Platforms Ltd").

### Element (Matrix) — federated rooms with a container layer

Evidence layer: A (direct observation from Element help FAQ and official docs).

- Element's center of gravity is messaging ("an end-to-end encrypted secure messenger and collaboration app"); its community container is **Spaces**: "Matrix Spaces are a way to group multiple rooms together. Rooms can be in multiple spaces at once, and spaces themselves can also be included within other spaces."
- Container semantics: spaces can be public or private; a public space has an **address** users can link to with `#`; creation flow asks for avatar, name, address, description ("a description of the space and its purpose will help inform others of why the space exists and help them decide whether it's a space they'd like to join").
- Container-level membership gates rooms: room access can be set to "Space members" — "By adding the room to a Space, you can also select 'Space members' to only allow anyone that is a member of the Space to join."
- Room access modes (room-level control distinct from container membership): "Private (invite only)", "anyone who knows the room link", "Space members", and public directory listing ("Publish this room to the public in example.com's room directory?").
- Listed ≠ joinable: "If your room is listed in the directory, people will know it exists but they will only be able to join it if you allowed the access to it to anyone knowing the link."
- History visibility is room policy: "Members (full history)" vs "Members since invited"; changing access does not change history visibility; "peek" before joining is possible when history is visible to anyone (and the room is not encrypted). In E2EE rooms, history for new members only via explicit invite.
- Room-level roles and permissions: "In the roles and permissions section of the room's settings, you'll be able to configure the privilege levels required to perform various actions in the room, e.g. send a message, ban / kick members, redact messages, update the room's settings, invite new members."
- Notifications: two levels (app-wide and per room); per-room options mute / mentions only / all messages / all messages (noisy); keyword notifications; email notification digests.
- Messaging machinery: mentions by name (autocomplete), read receipts (avatars with reading time), file sending, search (room-scoped or across conversations), favourites/low-priority/historical room-list sections, threads (beta; homeserver support required).
- Encryption posture: per-room optional E2EE; key storage/recovery machinery; identity pinning/verification.
- Federation and two-layer governance: "Element is a client that allows you to access any homeserver in the Matrix network... Each homeserver has different approaches to Abuse Management and Privacy, which are out of Element's control." Abuse reporting splits between the client vendor, the matrix.org homeserver, and other homeservers' administrators. Room addresses are linked to homeservers; a room can have addresses on multiple homeservers.
- Platform ecosystem: bridges exist for Discord, Slack, Telegram, IRC, XMPP, WhatsApp, Teams, Signal (Element cloud docs) — evidence that the room/container model interconnects with neighboring Types' products.
- Deployment: Element app (hosted matrix.org or other homeservers), Element Server Suite (self-hosted), EMS (managed cloud).
- Straddle note: Element is a room-first product (rooms exist and are addressable apart from any space) that grew a container layer (Spaces) with space-members access gating — exactly the drift case the sibling chat-room pass observed. It is retained in the sample deliberately as the boundary-straddler.

### Discord — unreachable market anchor

Evidence layer: none (docs unreachable). Structural anchor only.

- All three official surfaces (developer docs, support center, moderation curriculum) timed out. No product-specific claims are made about Discord anywhere in this research or the final document. Discord is retained as the market anchor for the hosted consumer pole of the Type; the hosted pole's structure is argued from the sampled products plus the sibling pass's structural reasoning.

### Guilded — unreachable market anchor

Evidence layer: none (docs unreachable). Market anchor only; no claims.

### Rocket.Chat — abandoned drift-test candidate

Docs timed out twice; abandoned. Rocket.Chat was considered as a test of "team-messaging product used as community platform" drift; the drift is instead argued structurally (see Boundary Findings).

## Cross-product Comparison

| Structure | Stoat/Revolt | Element (Matrix) | Discord-class (structural, no product claims) |
|---|---|---|---|
| Top-level container | Server | Space | Community container ("server"-class unit) |
| Container identity | name, icon, customization | name, avatar, address, description | name/icon-class identity surface |
| Membership unit | community (server) | community (space); rooms can additionally gate by space membership | community-level membership |
| Rooms underneath | channels (text + voice) | rooms grouped by the space; rooms can belong to multiple spaces and spaces to spaces | multiple rooms under the container |
| Shared live stream per room | yes (chat with formatting, replies) | yes (timeline, mentions, read receipts, threads) | yes |
| Roles/permissions | role-based permissions system (community-level framing) | privilege levels per action at room level; space-level governance implied by space membership gating | role hierarchy expected |
| Moderation | community moderation tools + moderation bots; platform strikes/suspensions above | room-level kick/ban/redact privileges; homeserver abuse management above | community moderation + platform enforcement expected |
| Join mechanisms | invite/join via server address; platform Discover directory | invite; space address (#); room link; public room directory per homeserver | invite links + discovery expected |
| Discovery surface | platform-level Discover with listing guidelines and anti-manipulation rules | per-homeserver public room directory; public spaces with addresses | platform discovery expected |
| History | server-side (implied by always-on hosted/self-host model; not explicitly detailed in fetched pages) | server-side with explicit visibility policies (full vs since-invited; peek) | server-side expected |
| Notifications | (documented at messaging level; per-room levels not confirmed in fetched pages) | per-room levels (mute/mentions/all), keywords, email digests | per-room levels expected |
| Voice | voice chat listed as core feature | calls in rooms (Element Call); no voice-channel room type evidenced | voice rooms expected |
| Extensions | bots, webhooks, integrations | bridges (Discord/Slack/Telegram/IRC/XMPP/WhatsApp/Teams/Signal), bots/integrations | bots/integrations expected |
| Deployment | hosted + self-host + public API | hosted (matrix.org/EMS) + self-host (ESS) + federated | hosted |
| E2EE | not evidenced in fetched pages | optional per-room E2EE with key management | varies |

Cross-product commonalities (evidence layer B): container-with-rooms structure; community-level membership; roles/permissions; two-layer governance (community staff + platform above); join mechanisms (invite + discovery); per-room notification control; extensions/bots; persistent server-side history.

## Abstraction Levels

### L0 — Defining Invariant (minimal)

```text
Community container — an identified community that people join
└── Membership at community level (join/leave; held above and
    across all of the community's rooms)
    └── Rooms — named chat places owned by the community,
        living underneath the container
        └── Shared real-time message stream per room
```

- **Community container**: an identified, joinable community with its own identity (name/icon/description-class surface), which exists and holds its membership regardless of any particular room or conversation.
- **Community-level membership**: joining is the entry act; a member is a member of the community as a whole, not merely of individual conversations. Membership persists while offline.
- **Rooms underneath**: the community holds a set of named rooms; conversation happens in rooms, not in one member-defined thread.
- **Shared real-time message stream per room**: participants post to the room's stream and see each other's messages live.

Remove the container → standalone rooms → Chat Room Application. Collapse to a single member-defined conversation → Group Messaging. Replace open community membership with an organizational roster → Team Messaging. Replace live rooms with asynchronous topic content → Community Platform (01.06).

Deliberately NOT in L0 (tested against the historical/market-sample check): accounts (identity substrate is L2), server-side history (all sampled products have it, but a container+rooms product without server history is still recognizable; consistent with the sibling chat-room treatment), roles/moderation (near-universal but a tiny unmoderated community still fits), public discovery (private invite-only communities are fully valid), voice rooms, bots, large scale (Stoat explicitly serves "a handful of friends" upward).

### L1 — Common Mature Structure

- Community-level roles and permission hierarchy (owner/admin/moderator/member; role-based permission systems; per-action privilege levels)
- Community-level moderation machinery (removal, bans, timeouts; moderation bots in some products)
- Two-layer governance split: community staff set and enforce local rules; the platform retains platform-level rules and enforcement (strikes/suspensions; removal from discovery or the platform; per-homeserver abuse management in federated deployments)
- Join machinery: invite links/addresses; platform-level discovery surfaces (directories) with listing rules
- Server-side persistent history per room, with visibility policy (what newcomers may read; peek-before-joining in some products)
- Member roster/directory at community level; member profiles
- Per-room notification levels (mute / mentions only / all messages), mentions, keyword alerts
- Messaging machinery in rooms: replies, reactions-class responses, formatting, media/file sharing
- Voice conversation alongside text (as dedicated voice rooms in some products; as in-room calls in others)
- Extensions: bots, webhooks, integrations bridging external services
- Direct messages between members as a side surface (not the organizing structure)
- Community presentation and join configuration (name, icon/avatar, description, access mode)

### L2 — Variant / Optional Structure

- Deployment posture: hosted consumer service vs open-source self-hosted vs federated protocol network (rooms/spaces addressable across servers; bridges to other chat systems)
- Identity substrate: platform account (email/username) vs federated ID (@user:homeserver)
- Discovery posture: publicly listed/discoverable vs unlisted/invite-only; anti-manipulation and moderation requirements attached to public listing
- Encryption posture: optional per-room E2EE with key management (some products) vs none evidenced
- Container depth: rooms exclusive to one container vs rooms belonging to multiple containers and containers nested in containers (Element Spaces)
- Non-chat module depth: how far the container extends beyond chat (voice, events, forums, media) — varies by product; only voice is directly evidenced in this sample
- Audience/segment variants: gaming guilds and raid groups, study groups, interest/hobby communities, open-source project communities, creator/fan communities, friend groups
- Monetization posture: freemium hosted vs free open-source (not deeply evidenced in this sample)

### L3 — Vendor-specific (research notes only)

- Stoat: group DM limit of 50 members; 20 MB free file upload; free custom emojis; CSS theming; badges; Discover auto-moderation enrollment (in testing); strikes system; EU jurisdiction/data-storage map; Revolt→Stoat rebrand; "servers" as sellable property prohibited with brand-sale exception.
- Element: threads require homeserver support (MSC3440); recovery-key/key-storage machinery and tables; matrix.org registration policies; bridge catalog; ESS/EMS product suite; space mapping/provisioning in ESS Pro; room address aliasing across homeservers.
- Discord/Guilded: nothing recorded (docs unreachable).

## Rejected Findings

- **"Server-side persistent history is definitional"** — rejected. Universal in the sample but not required for recognition; consistent with the sibling chat-room leaf's treatment of history models.
- **"Voice channels are definitional"** — rejected. Voice is common but implemented differently (voice rooms vs in-room calls); a text-only community chat platform is still clearly the Type.
- **"Public discovery is definitional"** — rejected. Private invite-only communities are fully valid instances; discovery is a join mechanism, not the structure.
- **"Bots/integrations are definitional"** — rejected. Extension layer, not structure.
- **"Large scale is definitional"** — rejected. The same tools serve friend-group communities and bustling communities (Stoat's own framing); scale is a variant, not a definition.
- **"Accounts are definitional"** — rejected at L0. All sampled products require accounts, but identity substrate is an implementation choice (L2); the sibling pass showed room-based systems operating without accounts historically.
- **"Community Chat Platform = Community Platform with chat"** — rejected as a collapse. The 01.06 family centers on asynchronous content (posts/threads/profiles); this Type centers on live rooms. See Boundary Findings.

## Boundary Findings

**vs Chat Room Application (sharpest seam; discharges this leaf's side of the joint-review flag).** Both are full of rooms and both use join/leave participation. The structural test is **what the user joins first**:
- Chat Room: the room is the top-level unit — a standalone addressable place; entry is by room address/link/directory; there is no membership above the room.
- Community Chat Platform: the community is the top-level unit — membership is held at the container, rooms live underneath it, and community-wide roles/rules govern across rooms.
Drift is real and observed: Element is a room-first product that grew Spaces (container layer with space-members gating); the sibling pass observed the same straddle from the room side. The two Types form a gradient, and products exist at every point; the container test remains the discriminator. Joint review with the still-unprocessed Group Messaging and Team Messaging siblings remains open.

**vs Team Messaging Application.** Team messaging channels are room-shaped, but membership derives from an organizational roster (employment/org identity), and the workspace is closed to outsiders by default. Community chat membership is self-service join around a shared interest/identity, strangers are expected, and governance is community-volunteer rather than organizational. Drift case: communities sometimes run on team-messaging products (org-roster product repurposed as a community home) — a deployment choice, not a Type collapse. Rocket.Chat was to be the drift test but was unreachable; argued structurally.

**vs Group Messaging Application.** A group is a member-defined private thread among known people with invitation flow and no self-service discovery by address. A community is a container holding many rooms with governed membership and (often) public discoverability. The gradient at private link-known rooms mirrors the sibling pass's observation.

**vs Community Platform family (01.06: Online Forum, Community Platform, Interest/Private/Member Community Platform).** Those center on asynchronous content objects (posts, topic threads, profiles, feeds) browsed over days; chat is at most one feature. Community Chat Platform centers on live rooms under a container. The seam is the primary object: async content vs live conversation places. Note: 01.06 leaves are unprocessed; if research there shows chat-centric community products, a joint review may be needed.

**vs Instant Messaging Application.** IM threads are person-addressed from a personal contact graph; community chat is place/container-addressed with self-service join. IM products adding community-container layers (or community products adding DMs) create gradient cases; DMs in community products are a side surface of co-membership, not the organizing structure.

**vs Social Live Streaming / Social Audio.** In those, chat is a room-shaped surface subordinate to a broadcast or voice stage; here the rooms and their streams are the primary object.

**Voice-first community servers (TeamSpeak-class).** A voice server with channels and membership satisfies container+membership but its primary medium is voice; treated as a boundary case toward voice communication Types rather than a core instance. Voice rooms inside a text-first community platform are normal (L1), not a separate Type.

**Historical / market-sample check.** Older chat systems (IRC networks, portal-era chat rooms) had no user-joinable container: the network or portal was the backdrop, and rooms were the top-level unit — those are Chat Room Applications, and the sibling pass documented them. The user-created, user-owned, joinable community container holding many rooms is the structural innovation that defines this Type; the Type is therefore modern, and the definition was checked to not depend on any single era's implementation (no accounts, no server history, no discovery, no voice in L0). Regional/regional-variant products were not directly sampled (evidence limitation recorded below).

## Uncertainties

- Discord and Guilded documentation unreachable: the hosted consumer pole's community-specific machinery (onboarding flows, verification levels, discovery tiers, monetization, boosts-class mechanics) is unverified. No claims made; the hosted pole is described structurally from the sampled products.
- Stoat's history and notification documentation was only partially reachable (KB sections are sparse); server-side history is inferred from the always-on hosted/self-host model rather than an explicit statement — treated as L1 with moderate confidence.
- Whether the 01.06 Community Platform family will claim chat-centric community products — joint review may be needed when those leaves are processed.
- Group Messaging and Team Messaging siblings unprocessed — boundaries argued structurally; the chat-room sibling's joint-review flag stays partially open.
- Element's center of gravity (messenger with a container layer vs community platform) is genuinely gradient; treated as the deliberate straddler.
- Stoat/Revolt naming is in flux (rebrand); product references use "Stoat (formerly Revolt)".

## Final Synthesis

The Community Chat Platform is defined by a small structure: **a joinable community container holding membership above its rooms, with named rooms underneath carrying shared real-time message streams.** Everything else the market associates with the Type — role hierarchies, moderation tooling, invite links and discovery directories, server-side history, voice rooms, bots, notification levels — is common mature structure layered onto that container, not the definition. The two-layer governance split (community staff govern locally; the platform governs the platform) is the Type's characteristic governance shape. Deployment (hosted / self-hosted / federated), identity substrate, discovery posture, and encryption posture are variants. The Type sits in a deliberate gradient between Chat Room Application (room-first) and Team Messaging (org-roster-first), with the container test as the discriminator.
