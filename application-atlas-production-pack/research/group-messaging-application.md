# Research Notes — Group Messaging Application

## Research Goal

Understand the Application Type "Group Messaging Application" (DIRECTORY 01.01 Messaging & Chat) from real products: what the group is as an object, how membership is assembled and governed, how the conversation works, and where the Type's boundaries sit against Instant Messaging (whose group chat may subsume this Type), Chat Room Application, Community Chat Platform, and Team Messaging Application.

This leaf carries two open joint-review questions from already-processed siblings:

1. **Instant Messaging pass (2026-09-05):** "Group Messaging is largely a focused variant of IM Group Chat. It does not currently present a structurally distinct model; the boundary may deserve review in a later pass." — this pass must answer whether the leaf is a distinct Type, a Variant, or an Alias.
2. **Chat Room pass (2026-09-06) + Community Chat pass (2026-09-07):** group messaging characterized as "member-defined private thread among known people (invitation-flow, no self-service discovery by address)" — boundary held structurally; the group-messaging side of the joint-review flag is to be discharged here.

## Initial Boundary (hypothesis before research)

- Core use: ongoing shared conversation among a known set of people — family, friends, teammates, a class, a club.
- Nearest neighbors: Instant Messaging (1:1 threads + group chat as a capability), Chat Room (addressable place joined by anyone with the address), Community Chat Platform (community container above rooms), Team Messaging (org-roster channels).
- Main risk: the leaf collapses into "IM group chat" and is not a distinct Type.
- Unknowns: whether a dedicated group-first product family actually exists in the market (vs groups only inside IM); what state a group carries beyond the stream; how join/roles work at the low end; where discovery/size drift begins.

## Research Questions

1. What is the top-level object users create or join first — a group, a person thread, a room, a container?
2. What state does a group carry? (name/avatar/topic, roster, roles, settings, shared content)
3. How is membership assembled and changed? (invite flow, share links, approvals, join codes)
4. How do messages relate to the group? (one shared stream? sender attribution? addressing?)
5. What group-level rules matter? (roles and permissions, visibility, join approval, lifecycle)
6. How does 1:1 messaging relate to the group world in group-first products?
7. Where are the boundaries vs IM group chat / chat rooms / community chat / team messaging?
8. Do older, regional, carrier-era forms (MMS group texts, SMS-based class groups, QQ-style numbered groups) satisfy the same core?
9. Where does the Type start drifting into neighbor Types (discovery, scale, announcement modes, org containers)?

## Representative Products

| Product | Pole / role | Evidence status |
|---|---|---|
| GroupMe (Microsoft) | group-first consumer messaging | Tier-1 help articles fetched (start-a-group, join/rejoin, group settings) + Tier-2 root page — direct evidence |
| Apple Messages (group iMessage / MMS) | person-graph IM group-chat pole + carrier-era forms | Tier-1 Apple support article fetched — direct evidence |
| Remind | education-tier group messaging (class as group) | Tier-1 help-center root fetched (article summaries visible); article pages 403 — partial evidence |
| WhatsApp / Telegram / Signal / BAND | IM-pole and group-first anchors | vendor help docs unreachable this pass (timeouts ×2 each; WhatsApp FAQ unreachable in the prior IM pass as well) — structural anchors only, claims limited to what the processed IM pass already recorded |

## Sources

Fetched 2026-09-07:

- GroupMe product page — https://groupme.com/ (root; features URL 404)
- GroupMe Help & Learning (Microsoft Support) — https://help.groupme.com/hc/en-us (root)
- GroupMe — How do I start a group? — https://support.microsoft.com/en-us/groupme/how-do-i-start-a-group-in-groupme
- GroupMe — How do I join or rejoin an existing group? — https://support.microsoft.com/en-us/groupme/how-do-i-join-or-rejoin-an-existing-group-in-groupme
- GroupMe — Manage group settings — https://support.microsoft.com/en-us/groupme/manage-group-settings-in-groupme
- Apple — Send a group text message on your iPhone or iPad — https://support.apple.com/en-us/HT202724
- Remind Help Center root — https://help.remind.com/hc/en-us (article summaries; article pages 403)

Unreachable (1–2 failures each, then abandoned per source-access rules): band.us and help.band.us (timeouts ×2), telegram.org/tour/groups + telegram.org/faq (timeouts ×2), faq.whatsapp.com (timeout ×1 this pass; also unreachable in the 2026-09-05 IM pass), help.viber.com (timeout ×1). Recorded as a Source-access Limitation: no numeric limits, default values, or group-size figures are asserted from memory for these products.

Prior sibling-pass records used (as recorded cross-product evidence, not new fetches): research/instant-messaging-application.md, research/chat-room-application.md, research/community-chat-platform.md.

---

## Product Observations

### GroupMe (group-first consumer messaging)

Evidence layer A unless noted. Sources: Microsoft Support articles listed above.

**Identity / account layer**
- Personal identity includes phone number and email (dedicated help articles: change phone number, change email, forgot password, PIN by SMS). Tier-2 positioning: consumer app, use-case pages for Campus, High School, Non-Profit, Friends.
- Personal profile: profile picture + nickname (editable per member).

**Group as object**
- Creating a group: Chats tab → New conversation → **Start Group** → enter **group name** and add a **group avatar** → add members by name, email, phone number, or from GroupMe contacts → confirm. The group is created as a named object before any message exists.
- Group identity surface: avatar, name, topic, theme, like-icon emoji (owner/admin only).
- Group-scoped member identity: each member can set their own nickname/avatar *for this group* ("Edit your profile (all members): change your profile picture or edit your nickname").

**Membership machinery**
- "You must be invited into a group. Anyone who is a member of the group can add you to the group from the app, or they can send you a share link."
- Join controls (owner/admin): **Who can join? — Anyone / Approved members only** (admin approval), optionally with a **join question** the candidate answers.
- Share link enablement is an owner/admin capability; anyone with the link can join.
- Member-management permission: **Everyone can edit** (all members add/remove) vs **Admins only**.
- Roles: **owner** and **admin(s)**; ownership transferable ("Change owner" — owner/admin only).
- Rejoin semantics: left groups appear in Archive → "Groups You Left" → Rejoin. If removed by others, only current members can add you back.

**Visibility / discovery (drift surface)**
- Visibility setting (owner/admin): **Hidden** (default posture — open only to invited members) / **Visible to everyone** (findable by name or location) / **Visible only to your school name** (Campus Connect, a school-scoped listing surface).

**Group lifecycle**
- Leave group (any member); **End group** (owner/admin) — "will also delete the group and cannot be undone"; Clone group (creates a new group); Clear chat history (member action on their view).

**Conversation**
- Shared stream per group; per-message sender; "like" reactions with a configurable emoji; media & sharing is a top-level help section; Copilot AI assistance (era-typical); block/unblock contacts.
- 1:1 messaging exists (contacts, blocking) but the product's organizing surface is groups; marketing headline is "group chat app".

### Apple Messages — group texts (person-graph IM pole + carrier forms)

Evidence layer A. Source: Apple support article.

- A group text is started by composing a message and entering multiple recipients from **contacts** — the thread comes into existence when a message is sent; there is no separate group-creation step.
- Transport variants of one structure: **Group iMessage** (Apple transport, end-to-end encrypted), **Group MMS** (carrier, green bubbles, shared stream with media), **Group RCS** (carrier, receipts/typing), **Group SMS**.
- **Group SMS is the degenerate form**: "All responses in a group SMS are sent as individual text messages and the recipients can't see the other responses from the group" — i.e. no shared stream. Apple documents it as the limited fallback, not the normal group form.
- Group iMessage capabilities: send/receive media, see all responses, effects, share location, collaborate; **give the group a name, add or remove people, mute notifications, leave the group**. Related articles: add/remove someone, name a group iMessage, group FaceTime from Messages, polls in a group message (iOS 26).
- The group surface is attached to the person-thread world: threads are listed among personal conversations; reachability is the address book. This is the pole where groups are a thread type inside a person-first IM.

### Remind (education tier)

Evidence layer A for the visible help-center summaries; details unverified (article pages 403).

- The group container is a **class**: classes have **owners** ("Add another owner to your class — you can add an owner from two places: class settings and the people list"), a people list, and settings.
- Join machinery: "The fastest way to join a class is by text (US & Canada). Participants text a class **@code**…" — owner-controlled join code, functioning as an address-like join aid.
- Leave/opt out: "To leave a specific class, text **@LEAVE**. To leave all classes, text @LEAVEALL" — membership exit is member-controlled, even via SMS.
- Communication: send messages; "Get message history" exists. Add people / remove people are documented member-management operations.
- Organization layer (Remind Hub: schools & districts, rostering, SSO) sits above classes — drift toward an org container.
- Audience tier: teachers, students, families; phone-number/SMS-backed reachability.

### WhatsApp / Telegram / Signal / BAND (structural anchors only)

No new product claims. What the processed sibling pass already recorded (research/instant-messaging-application.md):

- Group conversation in IM is "a thread whose participant set is defined by its members, of bounded size, addressable per member" — recorded as cross-product common structure (Layer B), not the IM defining core.
- The IM defining core is personal identity + person-addressed threads; groups are common mature structure layered on that core.
- Telegram recorded as cloud-first IM with "very large public groups, optional E2EE only in special modes" (IM-pass record; product's own tour/FAQ unreachable both passes).
- BAND was intended as the second direct group-first sample but its docs were unreachable; it is retained as a market anchor only, with no claims.

---

## Cross-product Comparison

| Dimension | GroupMe | Apple Messages (groups) | Remind (class) | IM-pole record (WhatsApp/Telegram/Signal class) |
|---|---|---|---|---|
| Top-level object users create first | Group (named + avatar, before any message) | Thread (created by sending to multiple recipients) | Class (created by teacher/owner; joinable by code) | Person thread (groups are a thread type) |
| Participant set defined by | Members (invite/share link) | Initial recipients + add/remove | Owner + join code + member self-exit | Members |
| Shared stream | Yes | Yes (iMessage/MMS/RCS); No in Group SMS (documented degenerate form) | Yes (class message stream) | Yes |
| Persistent history | Yes (retained; clear/leave/end semantics) | Yes (thread persists on device/cloud) | Yes ("message history") | Yes |
| Group identity surface | Name, avatar, topic, theme | Optional group name | Class name (code-based) | Name (common) |
| Roles | Owner/admin; member-management permission toggle | None documented (peer members) | Owner(s); members | Admin roles common (unverified this pass) |
| Join controls | Invite, share link, request-to-join approval + join question | Add/remove by members | @code join by text; @LEAVE exit | Invite/link (unverified this pass) |
| Discovery posture | Hidden default; optional visible-by-name/location; school-scoped listing | None | Code-based; org-layer context | — |
| 1:1 messaging | Present but secondary | Primary (groups attached to person-thread world) | Present (chat) vs announcements | Primary |
| Transport/substrate | App identity (phone/email) | iMessage vs carrier MMS/RCS/SMS | App + SMS | App-specific |
| Scale | Small-to-medium groups; no figures asserted | Thread-scale; no figures asserted | Class-scale | Large-group drift recorded for Telegram |

**Reading.** All directly-sampled products agree on: member-shaped participation, one shared message stream with sender attribution, persistent shared history, and a group surface carrying at least a name/identity. They diverge on: whether the group is an object created before messaging (GroupMe, Remind) or a thread that exists because someone messaged several people (Apple); whether roles/governance exist (GroupMe, Remind vs Apple peers); and whether discovery machinery exists (GroupMe's optional listing, Remind's codes — both owner-controlled).

The Group SMS counter-form is valuable boundary evidence: when responses are NOT visible to the whole group (individual copies), the product stops being a shared-stream group conversation and becomes a broadcast-to-many — Apple itself documents this as the limited fallback.

## Canonical Model (with historical sample check)

### Level 0 — Defining Invariant (deliberately minimal)

```text
Group Messaging Application
└── Member-defined participant set
    (a group of known people assembled and changed by its own members)
    └── Shared message stream addressed to the group
        (all members see the same stream; per-message sender attribution)
        └── Persistent shared history
            (retained and available to members over time)
```

Three structures. Tests:

- Remove the member-defined participant set (self-service join by address) → Chat Room Application.
- Remove the member-defined participant set (org roster) → Team Messaging Application.
- Remove the shared stream (recipients get individual copies) → broadcast messaging, not a group conversation (the Group SMS form; also the seam toward SMS Marketing / Business Messaging).
- Remove persistent history → ephemeral live chat (drifts toward room / live surfaces).
- Remove the group as the organizing object (person-addressed threads primary, groups as one thread type) → Instant Messaging with group chat.

Historical / market-sample check (§24 of the workflow methodology):

- **Carrier-era group MMS** (no dedicated app): member-defined thread among address-book contacts + shared stream + persistence on device — satisfies the three invariants. ✓
- **Group SMS** (individual copies): fails the shared-stream invariant — Apple documents it as the degraded fallback. (Boundary counter-example, not a Type member.)
- **SMS-backed class groups** (Remind's SMS join/leave): membership and history machinery over carrier transport — satisfies the invariants with a non-app substrate. ✓
- **Numbered-owner groups in regional platforms (QQ-class)**: owner/admin hierarchy, join by number, group files/albums — structurally group messaging with address-like join; docs unreachable, described structurally only, no claims. (Plausible ✓, unverified.)
- **Email mailing lists (Listserv / Google Groups)**: subscription-based list address over email transport — belongs to the Email family, not this Type. ✗ (boundary, not core)

The three invariants do not depend on phone numbers, app accounts, avatars, roles, or any specific join mechanism.

### Level 1 — Common Mature Structure

Observed in most directly-sampled products / recorded across the IM market:

- Named group with an identity surface (name, photo/avatar; topic in some)
- Visible member roster; per-member group-scoped identity (nickname)
- Owner/admin roles governing member management and group settings
- Join machinery beyond raw invites: share links, request-to-join with approval, join questions, (in one sample) join codes
- Group settings surface (a management screen for identity, membership, notifications)
- Group lifecycle operations: leave, end/delete (irreversible), ownership transfer; rejoin/archive semantics
- Media in the stream (photos/video/files); reactions/likes; mentions; per-group mute/notification levels
- Message-level operations (reply, edit/delete depth varies by product — unverified this pass)

### Level 2 — Variant / Optional Structure

- Group enrichment beyond the stream: shared photo albums/galleries, events/calendar, polls (polls directly observed only in one sampled product's iOS 26 release; enrichment breadth unverified for the group-first family this pass)
- Discovery posture: hidden-by-default is the observed default; optional visible-listing (by name/location), school-scoped listing, owner-issued join codes — drift toward room/community when discovery becomes the primary way groups are found
- Very large groups (recorded in the IM pass for one product; the Type itself carries no scale bound)
- Announcement-first modes (education/family poles; drift toward broadcast/business messaging)
- Org containers above groups (school/district Hub in one sample) — drift toward Team Messaging / organization-scoped products
- Transport substrate: app identity (phone/email/username), carrier MMS/RCS, SMS bridging, school rosters
- Encryption posture (E2EE observed in one sampled product's group iMessage; varies by product)
- AI assistance (era-typical; one sampled product ships a Copilot in-group assistant)

### Level 3 — Vendor-specific (kept out of the final document)

- GroupMe: Campus Connect, clone-group, configurable like-emoji, group themes, "Groups You Left" archive tab, Copilot branding
- Apple: the iMessage/MMS/RCS/SMS bubble-color transport ladder, Shared-with-You behavior, group FaceTime from Messages
- Remind: @code/@LEAVE texting commands, Remind Hub rostering integrations (Clever/ClassLink/OneRoster)

## Vendor-specific Findings

See Level 3. Additionally: GroupMe's "Everyone can edit vs Admins only" member-management toggle and join questions are directly observed but treated as common-pattern instances, not universal rules; the settings taxonomy (Hidden/Visible/School) is product-specific naming over the general drift surface.

## Rejected Findings

- **"Group messaging = IM group chat, not a distinct Type" (the IM-pass review question).** Partially rejected: the conversation machinery is indeed shared, but the market contains products whose organizing object is the group — created before any message, carrying managed identity/roster/roles/join controls, with 1:1 messaging absent or secondary. That is a different center of gravity from person-thread IM, and the sibling leaves already separate Type boundaries by center-of-gravity tests. The boundary is a gradient, not a wall (documented in Boundary Findings), and is recorded for taxonomy-owner review rather than as a silent merge.
- **"Groups require a named group object created before messaging."** Rejected: Apple's group threads come into existence by messaging multiple recipients; the minimal form is the member-defined thread itself. Named group objects with identity/roster are the mature group-first realization, not the invariant.
- **"Groups require roles/admins."** Rejected for the invariant: peer groups without documented roles exist (Apple group texts). Roles are Level 1.
- **"Group messaging is consumer-only / small-scale."** Rejected: education tier (Remind) uses the same structure for classes; large-group drift is recorded for one IM-pole product. No scale claims.
- **"SMS/phone-number reachability is definitional."** Rejected: carrier-era MMS groups and app-identity products both satisfy the invariants; phone numbers are one substrate (Level 2).

## Boundary Findings

**vs Instant Messaging Application (the carried review question).** The two Types share the same conversation substrate (member-defined thread, shared stream, persistence). The discriminator is the **organizing center**:

- IM: the primary object is the *person-addressed thread* built on a personal reachability graph; groups are one thread type beside 1:1 threads; the home surface is personal conversations.
- Group Messaging: the primary object is the *group*; users create/join groups first; groups carry managed state (name/avatar, roster, roles, join controls, lifecycle); 1:1 messaging is absent or secondary.
- Test: remove 1:1 person threads — a group-first product (GroupMe) remains a working product of this Type; a person-first IM (Apple Messages / WhatsApp-class) loses its defining surface and only groups remain (i.e., it becomes this Type). Conversely, remove groups from an IM and the IM survives; remove groups from this Type and nothing remains.
- Consequence: person-first products with rich group chat are documented as IM (as the IM pass did); group-first products are this Type. Products straddle (GroupMe keeps contacts/DMs; Apple groups can be named/managed) — the gradient is real, the test is the center of gravity.

**vs Chat Room Application.** The chat-room pass held the boundary on the "place test": a room is an addressable conversation place existing apart from its members, entered self-service by directory/link/invite, with pseudonymous stranger co-presence and room-local operator governance. Group messaging assembles conversations from known people with member-shaped membership. **Discharge:** this pass confirms the seam with direct evidence of the group side — invitation-flow is documented as the norm ("You must be invited into a group"), the default visibility posture is Hidden, and the drift surfaces (visible-by-name/location listing, join codes) are owner-controlled join aids, not discovery directories, in the sampled products. Flag's group-messaging side: **discharged**; team-messaging side remains open.

**vs Community Chat Platform.** Community = joinable container above many rooms, membership held at community level; group messaging = the conversation itself is the unit (or a set of independent ones), with no container layer. GroupMe's school-scope (Campus Connect) is a listing context, not a container holding multiple rooms — a group still exists independently. Boundary held (consistent with the community-chat pass's "member-defined thread vs container" formulation).

**vs Team Messaging Application (unprocessed sibling).** Working boundary from the chat-room pass: org-roster membership and organizational identity behind room-shaped channels. Group messaging assembles private groups from personal reachability; no org identity. Remind's school Hub (rostering, SSO, admin oversight) shows the drift surface where a group-messaging product grows an org layer — that pole belongs with Team Messaging when it is processed. Flag stands for the team-messaging pass.

**vs Business Messaging / Customer-to-Business Messaging / SMS Marketing.** Those Types center on an organization as a conversation participant or campaign-first broadcast. The Group SMS degenerate form (individual copies) shows the seam: without a shared stream among members there is no group conversation — broadcast sends individual copies. Boundary held.

**vs Email-family group forms (mailing lists / Google Groups).** Subscription-based list addresses over email transport; the medium and the address model belong to Email. Recorded as a boundary, not a variant.

**Taxonomy note for review.** The Group Messaging / IM seam is a center-of-gravity gradient over one shared substrate, like the room/container gradient the sibling passes recorded. Two options are defensible for taxonomy owners: keep both leaves with the center-of-gravity boundary statement (current state, both documents cross-reference), or consolidate Group Messaging as the group-first realization of IM. Recorded in STATUS Boundary Issues; nothing silently merged.

## Uncertainties

1. **BAND unreachable** — the group-first family beyond GroupMe is not directly sampled; the group-first pole rests on GroupMe + Remind (different tier) + the market's existence of this product family. Enrichment features (albums/events/polls as *standard* group capabilities) are unverified — kept optional, and the single polls observation is marked product-specific.
2. **WhatsApp/Telegram/Signal group documentation unreachable** (both passes) — IM-pole group details (admin controls, size limits, invite mechanics) rest on the IM pass's recorded Layer-B findings; no numeric claims anywhere.
3. **QQ-class regional groups** — structurally described from general knowledge of the family; no direct documentation this pass; kept out of all product-specific claims.
4. **Group-size limits, edit/delete windows, retention defaults** — no direct evidence; not asserted.
5. Whether GroupMe still delivers messages to members by SMS (its historical signature) — not verified this pass; not asserted.
6. Remind details beyond the help-root summaries (announcement vs chat modes, class settings depth) — 403 on article pages; claims limited to the visible summaries.

## Final Synthesis

A Group Messaging Application is a messaging application whose organizing object is the **group**: a conversation among a set of known people that the members themselves assemble and manage, exchanging messages in one shared, persistent stream. The defining core is exactly three structures — member-defined participant set, shared message stream addressed to the group, persistent shared history. Everything else commonly present — named group identity, roster with nicknames, owner/admin roles, share links and join approvals, group settings and lifecycle, media/reactions/mentions, mute — is mature structure that makes the Type practical but does not define it. The Type is distinct from Instant Messaging by center of gravity (group-first vs person-first over the same conversation substrate), from Chat Room by the member-shaped membership vs addressable-place test, from Community Chat by the absent container layer, and from Team Messaging by the absence of an org roster. Drift surfaces (discovery listing, join codes, very large groups, announcement modes, org containers) mark the seams and are documented as variants, not definition.
