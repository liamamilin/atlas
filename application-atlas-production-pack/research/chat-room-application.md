# Research Notes — Chat Room Application

Research date: 2026-09-06
Directory position: 01.01 Messaging & Chat, sibling of Instant Messaging, Group Messaging, Team Messaging, Community Chat Platform, Business Messaging, Customer-to-Business Messaging.
Processed siblings at time of research: Instant Messaging Application (2026-09-05), Business Messaging Application (2026-09-06). Group Messaging / Team Messaging / Community Chat Platform not yet processed — joint-review flags recorded below.

---

## Research Goal

Understand what a Chat Room Application is as an Application Type: what the "room" structure is, how participation works, how it differs structurally from instant messaging (personal contact graph), team messaging (organizational workspace), and community chat platforms (community containers with many rooms), and what the stable cross-product model is across eras (1988 IRC → 1990s portal chat rooms → modern room platforms).

## Initial Boundary (hypothesis before research)

A chat room is a **place-based** conversation: a named, addressable room that people join and leave, in which current participants exchange messages in real time. Contrast with IM, where conversation is **person-based**: threads bound to known individuals drawn from a personal contact graph.

Potential confusions to resolve:

- Is a chat room just "group chat" (IM variant)? (Group Messaging Application leaf is unprocessed)
- Is a chat room just a "channel" inside a team workspace? (Team Messaging leaf is unprocessed)
- Where does a "community server with many rooms" (Discord-class) end and a plain chat room begin? (Community Chat Platform leaf is unprocessed)
- Does stream chat (Twitch-class) belong here? (Social Live Streaming Platform leaf exists separately)

## Research Questions

1. What is a room/channel as an object: how is it named, addressed, discovered (directory, alias, link, invite)?
2. What does joining/leaving mean? Is membership presence-based (you are in the room only while connected) or persistent (you remain a member while offline)?
3. How are participants identified? Anonymous/pseudonymous nicknames vs registered accounts — which is defining, which is variant?
4. How does the live message stream work, and where does history live (client scrollback vs server-side persistence)?
5. What governance exists inside a room (operators, kick/ban, speak restrictions, topic)?
6. What access models exist (public/listed, link-known, invite-only)? Does being listed imply joinability?
7. What is the typical user loop for a newcomer (connect → find room → join → read → speak)?
8. What delivery forms exist (desktop client, web client, hosted service, self-hosted, embedded widget)?
9. Where are the hard boundaries against IM / Group Messaging / Team Messaging / Community Chat Platform / live-stream chat?

## Representative Products

Selection rationale: the room-centric chat space is dominated by two structures — the IRC tradition (1988, still the largest native room-chat ecosystem) and modern room platforms built on the Matrix protocol. The sample deliberately spans hosted/self-hosted/embedded delivery, presence-based vs account-based identity, and client-side vs server-side history.

| Product | What it is | Why sampled |
|---|---|---|
| **IRCCloud** | Hosted IRC client service ("IRC client with a future") | Commercial hosted room chat; always-on bouncer; server-side history; invites at scale |
| **Element** | Client for the Matrix room-network | Modern account-based room platform; explicit room access/history/permission settings; non-IRC counterweight |
| **The Lounge** | Self-hosted web IRC client | Self-hosted delivery; private-mode (bouncer-like) vs public-mode (no registration) postures |
| **Kiwi IRC** | Web IRC client + embeddable widget | Embedded-chat delivery surface (website visitor chat); open-access posture |
| **Libera.Chat** (network-side context) | Large public IRC network with official guides | Network-side evidence: channel creation, modes, operator model, discovery, accounts vs nicks |

Sample-bias note: 4 of 5 samples are IRC-adjacent by lineage. Element/Matrix is the deliberate structural counterweight (accounts, persistent membership, server history, per-room settings). Where IRC-specific mechanics appear (channel-name `#` prefixes, operator `@` symbols, voice flags), they are treated as implementation, not canon; the abstraction used is "room", not "channel".

Boundary anchors (not sampled as representatives, used only for boundary reasoning): Discord-class community platforms (rooms nested inside a community container → Community Chat Platform territory), stream chat (chat subordinate to a broadcast → Social Live Streaming), workspace channels (org-roster membership → Team Messaging), portal-era chat rooms (AOL/Yahoo-class; historical check).

## Sources

All fetched 2026-09-06.

| Source | Tier | Status |
|---|---|---|
| IRCCloud — https://www.irccloud.com/ (product page) | Tier 2 | ✅ |
| IRCCloud — https://www.irccloud.com/faq (FAQ) | Tier 1–2 | ✅ (rich: persistence, history, invites, kick policy, highlights, files, teams) |
| Element — https://element.io/help (FAQ/help center) | Tier 1 | ✅ (rich: room access modes, room address, history visibility, roles & permissions, notifications, threads, E2EE) |
| The Lounge — https://thelounge.chat/docs (getting started) | Tier 1 | ✅ (private vs public mode, bouncer posture) |
| The Lounge — https://thelounge.chat/docs/usage | Tier 1 | ✅ (mostly CLI/config; marginal) |
| Kiwi IRC — https://kiwiirc.com/ (product page) | Tier 2 | ✅ (widget embedding, network tools) |
| Libera.Chat — https://libera.chat/guides/registration | Tier 1 | ✅ (account vs nickname, identify, +r/+R modes, nick expiry) |
| Libera.Chat — https://libera.chat/guides/channels | Tier 1 | ✅ (join blockers +i/+k/+r/+j, bans; speak restrictions +m/+R/quiet; local operator policy) |
| Libera.Chat — https://libera.chat/guides/creatingchannels | Tier 1 | ✅ (/join, temporary op, ChanServ REGISTER, +s discovery mode, +t topic, FLAGS, GUARD, MLOCK) |
| matrix.org (docs / concepts) | Tier 1 | ❌ timeout ×2 — abandoned per network rules |
| spec.matrix.org (specification) | Tier 1 | ❌ timeout ×1 — abandoned (matrix.org family degraded) |
| Discord support (Intro to Servers) | Tier 1 | ❌ timeout ×1 — abandoned; boundary argued structurally, no Discord-specific claims made |
| help.element.io | Tier 1 | ❌ transport error ×1 → succeeded via https://element.io/help |

Consequence of access limitations: Matrix protocol-level claims are made only through Element's own help docs (client-level, Tier 1 for Element). No claims are made about Discord's product behavior. IRC history-absence is evidenced via the positioning of IRCCloud/The Lounge (products whose value proposition is storing history/keeping the connection alive), not via protocol documentation.

---

## Product A — IRCCloud (hosted IRC client)

Evidence layer: A (directly observed from irccloud.com and /faq, 2026-09-06).

Key observations:

- Positioning: "Group chat for teams, friends, and communities." "An IRC client — we connect to IRC servers for you, keep your connection alive, and store your chat history." (The value-add framing implies the underlying IRC room model lacks persistence by default — Layer A for the product, Layer C inference about IRC.)
- Core surfaces: public or private **channels**, plus one-to-one conversations. Channels are the primary conversation container.
- **Always-on / bouncer model**: "you will stay connected to IRC even if you shutdown your computer or sign out… when you come back, you'll be able to see what happened on IRC whilst you were away." Participation (presence) can be decoupled from the user's local session.
- **History**: server-side backlog; "scroll to the top of the conversation, more history will automatically be loaded. We keep all your message history forever (until you delete it)." Search currently browser-based (planned server-side search).
- **Invites at scale**: customizable "badge creator" — share a link or embed a form on a website so people can "easily join your channel just by providing an email address… Great for open communities and projects."
- **Highlights/mentions**: highlight words configurable; lines mentioning the user are highlighted; desktop notifications and mobile push.
- **Moderation semantics**: "Is there an option to auto-rejoin on kick — No, we deliberately respect the wishes of channel ops. Kicks are designed to remove people from a channel… we'd rather optimise for legitimate moderation concerns." → kick is an operator action that removes a participant from a room; the client deliberately does not circumvent it.
- **Files/media**: drag-and-drop upload, inline display, text snippets with syntax highlighting, embeds for images/videos/social links; integrations via IRC bots and service hooks.
- **Identity**: per-network nicknames; NickServ/SASL authentication supported on free accounts; avatars are network-scoped and only on servers supporting IRCv3 metadata (implementation detail).
- **Team variant**: team accounts can get a private IRCCloud-hosted server "for team messaging" with threading, message editing, reactions, typing indicators — modern chat features layered onto the room model in a private-server variant.
- **Interoperability**: connects to "any IRC server out there", plus Slack workspaces; can act as a bouncer for other IRC clients; supports connecting to user-run ZNC bouncers.
- Misc operational facts (L3): trial accounts disconnected if not visited "for a couple of hours"; free upload cap 100MB; NickServ verification email must be confirmed or account dropped (~24h per Libera, not IRCCloud); these numbers stay here.

## Product B — Element (Matrix client)

Evidence layer: A (directly observed from element.io/help, 2026-09-06).

Key observations:

- Architecture posture: "Element is a client that allows you to access any homeserver in the Matrix network, just like a browser allows you to access any website." Client/server separation mirrors IRC client/network separation.
- **The room is the central object**: per-room settings exist for every behavior below.
- **Room access modes** (three-tier, user-selectable per room):
  1. "Private (invite only)" — only invited people can access, even if they know the link;
  2. "anyone who knows the room link" — link-known but not publicly visible;
  3. published to the server's **room directory** — "discoverable to anyone searching for a room on the server."
  - Crucially: "If your room is listed in the directory, people will know it exists but they will only be able to join it if you allowed the access" — **listing ≠ joinability**. Discovery and access are separate controls.
- **Room address (alias)**: rooms get human-readable addresses bound to a homeserver; "A room can have different addresses on the same homeserver and addresses on different homeservers… required the moment you want to make the room accessible in other ways than by inviting users." Rooms are independently addressable places.
- **History visibility** (per-room policy): "Members (full history)" — new members read messages sent before they were invited; "Members since invited" — only from their invite onward; "anyone" — non-members can "peek" at a public room's history before joining. Visibility is bound to the setting at send time. So **room history visibility is a configurable property of the room**, not a fixed Type property.
- **Roles & permissions per room**: "As a room admin, can I decide what members can do? … configure the privilege levels required to perform various actions in the room, e.g. send a message, ban / kick members, redact messages, update the room's settings, invite new members." → room-level permission model, parallel to IRC ops but settings-based.
- **Membership model**: joining is the act of entering the room; invitations by Matrix ID or email; outsiders without an ID may be able to preview the room. Left rooms persist in a "historical" section where the user can still read past history but sees no new activity — **membership ending ≠ history eviction**.
- **Notifications**: two-level config (global + per-room): Mute / Mentions only / All messages / All messages (noisy); keyword ("nicknames") notifications; email notification of missed activity.
- **Read state**: read receipts shown as avatars next to the last-read message (product-specific UX; not generalized).
- **Threads**: threaded replies exist (beta, dependent on homeserver support) — sub-conversations inside a room (optional/variant capability).
- **E2EE**: per-room opt-in ("messages are only encrypted in rooms with encryption enabled"); identity verification machinery exists at account level (implementation detail).
- **Spaces**: rooms can be grouped into Spaces, and room access can be restricted to "Space members" — a container layer above rooms (drift toward community/organizational structuring; see Boundary Findings).
- **Identity**: Matrix ID (username@homeserver); email optional (up to the homeserver administrator); phone-number registration explicitly retired ("Not anymore. Sorry!") — confirms identity substrate is variant, not defining.

## Product C — The Lounge (self-hosted web IRC client)

Evidence layer: A (directly observed from thelounge.chat/docs, 2026-09-06).

Key observations:

- "The Lounge, a web-based IRC client for the modern world… must be installed on a server that runs 24/7… users can access it from their browser or mobile device." PWA delivery.
- **Two postures**:
  - **Private mode**: "acts like a bouncer and a client combined, in order to offer an experience similar to other modern chat applications outside the IRC world. Users can then access and resume their session without being disconnected from their channels." → always-on intermediary gives modern continuity (persistent presence + backlog).
  - **Public mode**: "acts as an open chat available to anyone without registration." → the zero-registration open room posture persists as a real deployment mode.
- Server/operator vs user split: an administrator installs the server, creates user accounts (`thelounge add <name>`); users log in from browsers. Self-hosted delivery form of the same room model.
- Plugins/themes ecosystem (npm), push notifications (L3 detail).

## Product D — Kiwi IRC (web client + embeddable widget)

Evidence layer: A (Tier-2 product page, 2026-09-06).

Key observations:

- "KiwiIRC makes Web IRC easy… Designed to be used easily and freely." Trusted-by list of IRC networks (freenode-era, EFnet, DALnet, Snoonet, Rizon…). (Note: freenode reference is dated marketing content; networks named are L3.)
- **Embedded widget**: "Embed an IRC client widget into your website for an instant, free live chat… No downloads or plugins required meaning your users can start engaging in your community easily." → the room as an open, zero-install surface for a website's visitors. This is the direct modern descendant of the 1990s website chat room.
- **Network-side tools**: WEBIRC (proper hostmask handling for web users), real-time connection stats, server allowlists ("It's your network").
- Privacy posture: heavy privacy focus; does not pass user connection info to networks unless requested (L3).

## Network-side context — Libera.Chat (public IRC network)

Evidence layer: A (official guides, 2026-09-06). The network guides document the room ("channel") structure independent of any client.

Key observations:

- **Identity vocabulary**: "an 'account' is your persistent identity; a 'nickname' is your current display name and can be owned by an account; to 'identify' means to log into your account." → pseudonymous display identity, optionally anchored to a registered account. Unregistered use is possible; some channels require registration (+r to join, +R to speak). Nicknames expire if unused.
- **Channel creation** (the canonical "create a room" flow): pick a name ("descriptive of the channel's purpose, no spaces or commas"; namespace conventions with `#` prefixes); `/join` it — "A person who joins an empty and unregistered channel is granted temporary operator status"; then register with ChanServ to gain ownership. So: **rooms come into existence by being joined; ownership is claimed by registration; unregistered rooms may vanish (temporary op, no services protection); registered rooms persist and can be guarded** (ChanServ GUARD keeps the channel present), with mode locks (MLOCK) and expiry rules.
- **Join restrictions**: `+i` invite-only, `+k` password-known, `+r` registered/identified users only, `+j` join throttle, plus ban lists with wildcard/extended masks. "The server will tell you the reason" — join denial is explained to the user. A banned user should "talk to one of the channel operators to see about having it removed."
- **Speak restrictions**: `+m` moderated (only voiced users may speak), `+R` identified users only, quiet masks (`+q`). → joining a room does not imply an unconditional right to speak; rooms may be run in moderated mode (used for announcements/Q&A-style channels).
- **Room-local governance**: "local policy and rules for each channel are set by that channel's operators" — the operator model is the room's governance layer, distinct from network staff.
- **Discovery**: channels are findable via network channel lists/search ("Finding Channels" guide); a new channel defaults to `+s` (secret — "will not appear in searches") until the owner removes it and makes it public. Topic changes can be restricted to operators (`+t`); `+n` prevents people outside the channel from sending messages to it (default) — i.e., **only current participants can address the room**.
- **Permissions machinery**: ChanServ FLAGS grants per-account permissions (voice/op/full control `F`), templates, temporary OP/DEOP, SECURE flag to bind op status to registered permissions.
- Historical reach: these guides are themselves derived from freenode-era documentation (2016–2021), documenting a structure that has operated since 1988 — the same join/operate/listen model.

---

## Cross-product Comparison

| Dimension | IRCCloud | Element | The Lounge | Kiwi IRC | Libera.Chat (network) |
|---|---|---|---|---|---|
| Primary object | channel | room | channel | channel | channel |
| Addressing | channel names on networks | room address/alias (multiple per room, cross-server), room ID | channel names | channel names | channel names, namespace conventions |
| Discovery | network channel lists; invite badges/links for public channels | room directory listing (publish), search; link-known mode; invite | (client of networks) | network lists; website widget entry | channel list/search; +s hides until published |
| Access models | public / private channels | private-invite-only / link-known / directory-public; listing ≠ joinable | private-mode (accounts) vs public-mode (no registration) | open widget access | +i / +k / +r / open; bans |
| Participation | join; presence kept alive by hosted service (bouncer) | join; membership persists offline; left rooms keep history accessible | private mode = resumed session; public mode = session-scoped | session-scoped web sessions | /join and /part; presence = connected |
| Identity | nickname per network + NickServ/SASL account | Matrix ID account (email optional; no phone) | server-local user accounts (private mode) or none (public mode) | nick per session/network | nickname (display) owned by account (persistent identity); expiry |
| History | server-side, "forever (until you delete)", scroll-load | server-side; per-room visibility policy (full / since-invited / peekable) | backlog via always-on client | client-side only (plain web client) | none server-side (implied by client/bouncer value props) |
| Governance | channel ops; kick respected (no auto-rejoin) | per-room roles & permissions (send/ban/kick/redact/settings/invite) | (delegates to network ops) | (delegates to network ops) | operators set local policy; kick/ban/quiet; FLAGS; temporary op on empty unregistered channels |
| Speak control | (via network modes) | privilege level required to send configurable | (via network modes) | (via network modes) | +m moderated, +R identified-only, quiet masks |
| Mentions/notifications | highlight words, push, desktop | global + per-room levels, keywords, email digests | push notifications | — | — |
| Threads/reactions/editing | team servers only | threads (beta), reactions | — | — | — |
| E2EE | no | per-room opt-in | no | no | no |
| Delivery | hosted service (web/iOS/Android) | apps + web, any homeserver | self-hosted server + browser PWA | web client + embeddable widget | network of servers + webchat |

### What is constant across all five (Layer B commonality)

1. A named, addressable conversation **place** that exists independently of any one participant.
2. **Join/leave participation**: the room's participant set is determined by the room (who is in it / joined it), not by personal contact relationships. Users find rooms by name, directory, list, link, or invite — the room is the thing you enter.
3. A **shared real-time message stream**: participants see each other's messages as they are sent; any permitted participant addresses the whole room; only current participants can post (default).
4. A visible **participant roster** and room-scoped **governance** (operators/moderators; kick/ban; speak restrictions) — room-local policy is set inside the room, separate from the platform operator.
5. Room-level **access control** distinguishing public/discoverable from private/invited, with join denial explainable to the user.
6. **Direct/private messages between participants exist as an adjacent surface** in every sampled system.
7. Identity is a **nickname/handle in a room namespace**, optionally anchored to a registered account — not a mutual-contact graph.

### What varies (implementation space)

- History: none server-side (IRC) ↔ always-on intermediary backlog (hosted/self-hosted IRC clients) ↔ full server-side with configurable newcomer visibility (Element).
- Membership persistence: presence-only (IRC; simulated by bouncers) ↔ persistent membership (Matrix).
- Identity anchoring: session nickname ↔ registered account (nick-account or homeserver ID).
- Delivery: desktop/web client ↔ hosted service ↔ self-hosted server ↔ embedded website widget.
- Container: standalone rooms ↔ rooms grouped in Spaces/community containers/team servers (drift cases).
- Richness: plain text ↔ media/files/embeds/threads/reactions/E2EE.

---

## Abstraction Levels

### L0 — Defining Invariant

```text
L0
Room — a named, addressable conversation place that exists
        independently of any participant
└── Join/leave participation — the room, not a personal contact
    relationship, defines who is in the conversation
    └── Shared real-time message stream — participants converse
        with the whole room, live, and see each other's messages
        as they are sent
```

Three properties. Removal tests:

- Remove the durable addressable place (conversation exists only between known individuals, unaddressable beyond its members) → IM group chat, not a chat room.
- Remove join/leave participation (participants bound by mutual contact/invitation from a personal graph, no self-service entry by address/discovery) → personal messaging, not a room.
- Remove the shared live stream (delayed/queue-based exchange, or broadcast where the audience cannot converse with each other and the speaker) → not a chat room.

Not in L0 (checked against the historical sample): server-side history (IRC rooms have none and remain chat rooms), persistent offline membership (IRC presence-only), registered accounts (public-mode rooms run without registration), E2EE, media, threads, moderators per se (an unmoderated small room is still a room), community containers, voice/video, phone numbers/emails.

### L1 — Common Mature Structure

- Participant roster (user/member list per room, with roles surfaced)
- Room discovery surface: directory / channel list / search / topic line
- Public vs private access modes (listed, link-known, invite-only) with listing ≠ joinability
- Room-scoped governance: operators/moderators; kick/ban/quiet; configurable permissions (who may send, invite, change settings)
- Message history / scrollback, with modern products persisting server-side and making it searchable
- Mentions/highlights and per-room notification levels
- Media/file sharing, embeds, snippets
- Bots/integrations feeding the room stream
- Direct 1:1 messages between participants (adjacent surface inside the same product)
- Multi-room membership with a room-list navigation surface; unread state
- Persistent registered identity (account) with display-name layer

### L2 — Variant / Optional Structure

- Identity substrate: anonymous session nickname / registered nick-account (NickServ-style) / platform account ID (homeserver ID); email optional; phone registration absent in modern samples
- History model: no server history / client-side scrollback / always-on intermediary backlog / server-side with newcomer-visibility policy (full vs since-join vs peekable)
- Membership persistence: presence-only vs persistent-while-offline
- Delivery form: desktop client / web client / hosted service / self-hosted server / embedded website widget
- Deployment: standalone rooms / federated networks (IRC multi-server; Matrix homeserver federation) / single private server for a team
- E2EE posture: none (IRC tradition) / per-room opt-in (Matrix-style)
- Richness: threads, reactions, editing, typing indicators (modern room platforms; partial in IRC-family variants)
- Room lifecycle: long-lived registered rooms (with expiry policies) / temporary event or site-widget rooms / unregistered rooms that vanish when empty
- Voice/video in rooms (drifts toward Social Audio / calling when primary)
- Community/team containers around rooms (drift toward Community Chat Platform / Team Messaging when primary)

### L3 — Vendor-specific Structure (stays here)

- IRCCloud: badge creator; bouncer interface for third-party clients; ZNC support; Slack-workspace bridging; team servers with threading/editing/reactions/typing; avatars via IRCv3 metadata; zombie-detection trial disconnects; free-account upload cap (100MB); deliberate no-auto-rejoin-on-kick policy
- Element: Spaces; recovery key (48-character), key storage, identity pinning/verification machinery; threads beta and homeserver-version dependency (MSC3440); matrix.to invite links; message-provenance decorations in E2EE rooms; per-room read receipts (avatars)
- Libera.Chat: ChanServ/NickServ/GroupContact/ProjectServ (CLAIM); namespace policy (`#` vs `##`); cloaks; memos; GUARD/MLOCK; nick and channel expiry thresholds; SASL/CertFP login
- The Lounge: private/public mode as server config; npm theme/plugin ecosystem; PWA install
- Kiwi IRC: WEBIRC hostmask handling; network connection stats; server allowlists; widget embedding service
- All numeric details, brand names, protocol extension names: evidence only, none promoted.

---

## Boundary Findings

### vs Instant Messaging Application (processed sibling)

IM L0 (per the sibling's research): personal addressable identity + reachability between known participants + member-defined thread + message + persistent history.

- IM conversation is **person-addressed** (you open a thread with a known contact); a chat room is **place-addressed** (you enter a room; co-participants may be strangers).
- IM reachability is the personal contact graph; room reachability is the room's address/directory/invite — no contact relationship required.
- IM threads are created by and die with their members' relationships; rooms exist independent of any member and outlive individual membership.
- Group conversation in IM is member-defined and invitation-flow; a room is entered via join, often by self-service discovery.
- Convergence case: pseudonymous room-chat with no discovery (private room, all members know each other) looks like group IM — the boundary is a gradient at that corner. Discriminating test: **is the room an addressable place that exists apart from its members?** If yes, room; if the conversation exists only as a thread among specific people, IM.

### vs Group Messaging Application (unprocessed sibling)

Structurally, group messaging ≈ IM group chat (member-defined, invitation-flow, person-graph identity). Chat rooms differ on: self-service entry by address/discovery, room-independence from members, pseudonymous/stranger co-presence, roster+operator governance, and public listing. Flagged for joint review when Group Messaging is processed: probable "member-defined small private group" vs "addressable place" split, with a real gradient in the middle (private link-known rooms).

### vs Team Messaging Application (unprocessed sibling)

Team messaging channels are rooms in shape, but: membership derives from the **organizational container** (workspace roster/identity), rooms are not open-addressable by outsiders, and the channel set belongs to the org. In a chat room the participant assembles themselves (join) under a personal/pseudonymous identity. Sampled drift cases: IRCCloud team servers ("private server for team messaging") and Element's enterprise positioning — products of this Type extending into team territory. Discriminating test: remove the organizational container and org-roster identity — if a self-joinable room system remains, the room core was a chat room capability inside a team product.

### vs Community Chat Platform (unprocessed sibling)

A community platform adds a **community container above rooms**: community-level membership, community-wide roles/moderation, many rooms organized under one discoverable community entity, plus community machinery (onboarding, rules, events). In a chat room application, the room itself is the top-level addressable unit. Sampled drift case: Element Spaces adds exactly such a container layer (room access restrictable to "Space members"). Discriminating test: **what do users join — the community, or rooms directly?** Community-first = Community Chat Platform; room-first (community container optional/absent) = Chat Room Application. Discord-class products were not directly researched (source unreachable); boundary stated structurally, no product-specific claims made.

### vs Social Live Streaming Platform / Social Audio Platform

Stream chat has a room-shaped text surface, but the primary object is the broadcast; the chat is subordinate and the audience relationship is viewer→streamer. In a chat room, the conversation is the primary surface and participants address each other. Audio rooms (voice-first) drift to Social Audio. Discriminating test: remove the broadcast/audio stage — if a standalone conversational room remains and is still the product's core, the room was a capability of the live surface, not the Type itself.

### vs Customer Support Chat / website live chat

Website widgets (Ki IRC-class embedding, "instant free live chat" for visitors) deliver open visitor rooms — a delivery form of this Type when the surface is a shared room. Visitor-to-agent 1:1 conversations are Customer Support Chat. The widget is L2 delivery, not a different Type by itself.

### Removal-test summary (canonical)

```text
Remove the room as an addressable place  → IM / Group Messaging
Remove self-join/open participation      → personal messaging
Add an org roster as membership source   → Team Messaging
Add a community container as primary unit→ Community Chat Platform
Make the room subordinate to a broadcast → live-stream chat
```

## Historical / Market-Sample Check

- **1988 IRC** (channel model, operator model, presence-based membership, no server history): satisfies the L0 fully — the L0 deliberately excludes history persistence and registered accounts so it does.
- **1990s portal chat rooms** (AOL/Yahoo-class, directory-listed public rooms, pseudonymous handles, join/leave, live text): satisfies the L0 (evidence: market-historical common knowledge, kept qualitative; no specific product claims).
- **Modern room platforms** (Element): satisfies the L0 with persistent membership, server history, and per-room settings — all L1/L2.
- **Website visitor chat** (Kiwi-class widget): satisfies the L0 in embedded form.
- Conclusion: the L0 is era-stable. The 1990s consumer "chat room" largely migrated into community platforms and died as a standalone consumer category, while the IRC/Matrix ecosystems keep the room structure alive — the Type is structurally alive even where the *consumer marketing label* has faded.

## Uncertainties

- matrix.org / spec.matrix.org could not be fetched; Matrix-side evidence rests entirely on Element's help center (client-level). Protocol-level claims were deliberately avoided.
- Discord-class community platforms were not directly evidenced (source unreachable); the Community Chat Platform boundary is argued structurally and must be re-checked when that leaf is processed.
- Group Messaging and Team Messaging leaves are unprocessed; the boundaries here are one-sided tests pending joint review.
- The "history lives in the client" property of IRC is evidenced via the value propositions of IRCCloud/The Lounge (Layer C inference from Layer A product claims), not via protocol documentation; kept qualitative.
- Consumer "chat room" products beyond the IRC/Matrix families (portal-era survivors, regional products) were not sampled due to documentation weakness; the sample is weighted toward IRC lineage (4/5) with Element as the structural counterweight.
- Whether voice-rooms (audio spaces) deserve their own Type vs a Variant of this one is deferred to the Social Audio Platform leaf.

## Final Synthesis

Canonical Chat Room Application:

```text
L0 (defining invariant)
- Room: a named, addressable conversation place existing independently of any participant
- Join/leave participation: the room, not a personal contact graph, defines who is conversing
- Shared real-time message stream among room participants

L1 (common mature structure)
- participant roster; room discovery (directory/list/search/topic);
  public vs private access modes; room-scoped governance (operators,
  kick/ban, speak restrictions, permissions); message history/scrollback;
  mentions & notification levels; media/files; bots/integrations;
  adjacent 1:1 DMs; multi-room navigation; registered persistent identity

L2 (variant / optional)
- identity substrate (session nick / registered nick-account / platform ID)
- history model (none / client / always-on intermediary / server-side with visibility policy)
- membership persistence (presence-only vs persistent)
- delivery (client / hosted / self-hosted / embedded widget)
- deployment (standalone / federated network / private team server)
- E2EE posture; threads/reactions/editing; room lifecycle (registered vs temporary)
- voice/video rooms; community/team containers (drift surfaces)

L3 — vendor specifics: see Vendor-specific Structure
```

The Application Document will present the L0 as the defining core and L1 as standard capabilities, with L2 named in Variants. L3 stays in these notes.
