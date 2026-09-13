# Research Notes — Social Live Streaming Platform

## Research Goal

Understand what a Social Live Streaming Platform is as an Application Type: what the unit of experience is, who broadcasts and who watches, how the audience is assembled, what happens during a broadcast, what persists afterwards, and where the Type's boundaries lie against the dense cluster of neighboring social/live/video Types in §01.05, §01.08 and §27.

## Initial Boundary

Working hypothesis at start:

- Core use: individual users broadcast live video to an audience; viewers watch in real time and interact (chat, reactions, gifts); the platform provides discovery, follow relationships, and monetization.
- Primary users: individual creators (broadcasters), viewers, delegated moderators.
- Nearest neighbors: Video Streaming Platform (§27, media VOD), Live Video Chat Application (§01.08), Social Audio Platform (§01.08 — processed), Random Video Chat Application (§01.08 — processed), Short-form Video Social Platform (§01.05 — processed), Microblogging Platform (§01.05 — processed), Webinar Platform (§01.04), Internet Radio Platform (§27 — processed), Community Chat Platform / Chat Room Application (§01.06 — processed), General Social Network (§01.05 — processed).
- Obvious unknowns at start: whether gifting/monetization is definitional or common; whether the follow graph is definitional; how platform-embedded realizations (live inside social networks / short-video apps / video platforms) affect the definition; whether VOD/replays are part of the core.

## Research Questions

1. What is the unit of experience — the broadcast session? How is it created (go-live flow)?
2. Who can broadcast — any user, or gated? What are the eligibility mechanics (if discoverable)?
3. How do viewers discover live streams — browse, categories, follow feeds, recommendations?
4. What interaction happens during the broadcast — chat, reactions, gifts, co-hosts/guests?
5. How does broadcaster identity persist — channel/profile, followers, past broadcasts?
6. What roles exist — broadcaster, viewer, moderator, co-host/guest?
7. What rules matter — conduct policies, moderation, eligibility, monetization rules?
8. What happens after the broadcast — VOD, replays, clips, highlights?
9. Is monetization (gifts/subs/ads) definitional or variant?
10. Where are the boundaries against each neighboring Type?

## Representative Products

Selected for market representation, different product philosophies, and different realization postures:

- **Twitch** — gaming-rooted, desktop/web streaming culture, subscription/cheer economy; the Western archetype of the standalone dedicated platform.
- **BIGO Live** — mobile-first social live streaming with a gift economy; the pure "social live" pole.
- **TikTok LIVE** — live embedded inside a short-video social platform; the platform-embedded pole (symmetry with the social-audio-platform pass's finding about embedded realization).
- **YouTube Live** — live embedded inside a large video platform; creator + media mix.

Historical anchors for the market-sample check (conceptual, not fetched): Justin.tv (2007), Ustream (2007), Stickam, BlogTV, YouNow, Periscope/Meerkat (2015), and the Chinese live-streaming lineage (YY, Huya, Douyin live).

## Sources

### Attempted official sources — ALL UNREACHABLE

The research environment could not fetch any official documentation on 2026-09-09. Every attempt failed (timeouts or access blocks):

- help.twitch.tv — timeout
- twitch.tv (root, community guidelines) — timeout
- support.tiktok.com (two paths) — timeout
- support.google.com/youtube (Live getting-started article) — timeout
- bigo.tv — HTTP 403
- younow.com — returned an empty JavaScript shell
- help.instagram.com — timeout
- 17live.net — transport error
- en.wikipedia.org (two articles) — timeout

### Source-access Limitation

No Tier-1 or Tier-2 source was reachable for any sampled product. Consequences, applied strictly:

1. This pass states **no product-specific operational facts**: no eligibility thresholds, no gift/currency mechanics, no revenue shares, no numeric limits, no feature-by-product attributions.
2. All claims in the paired Application Document are held at **canonical-inference strength** (the Type's intrinsic structure) or at **cross-pass counterparty strength** (documented boundary rows of processed sibling passes), never at direct-observation strength.
3. Sampled products are named for **market orientation only**; no operational detail is attributed to them.
4. The historical market-sample check is passed **conceptually** (structural reasoning about the founding generation of the Type), not through fetched sources.
5. Nothing was filled in from model memory at precision; hedged structural claims ("commonly", "typically") are used only where the claim is a structural necessity of the Type or is corroborated by processed sibling passes.

### Internal cross-references (processed sibling passes, used as counterparty context)

- applications/social-audio-platform.md — characterizes this Type from the audio side: "video as the primary medium and a one-performer broadcast economy"; instructs sibling passes to treat platform-embedded realization symmetrically.
- applications/random-video-chat-application.md — "one broadcaster, many simultaneous viewers; asymmetric roles and a gifting/performance economy; here both sides are equal peers in a 1:1 session".
- applications/short-form-video-social-platform.md — "live real-time broadcast is the unit; here the unit is the persistent recorded short video. Live streaming is commonly bundled inside short-video products but remains an attached surface".
- applications/microblogging-platform.md — "ephemeral live broadcast with simultaneous viewers; here posts are persistent asynchronous artifacts".
- applications/internet-radio-platform.md — "live surfaces driven by individual creators with social interaction (chat, gifts), typically video-first, without a station-organized catalog of licensed broadcasts".
- applications/chat-room-application.md — "stream chat is a room-shaped surface subordinate to a broadcast; the primary object is the stream, and the audience relationship is viewer→streamer".
- applications/community-chat-platform.md — "room-shaped chat subordinate to a live broadcast; the primary object is the stream".
- applications/general-social-network.md — "ephemeral live broadcast with simultaneous viewers; here updates are persistent and attributed".
- applications/photo-centric-social-network.md — "live broadcast with simultaneous viewers vs a persistent photo stream".
- applications/interest-based-social-network.md — "live, ephemeral surfaces are primary; here content is persistent and recorded".
- applications/friend-discovery-application.md — "live rooms or anonymous random contact are the primary surface, without a persistent friend-seeking profile or a managed friendship outcome".
- applications/creator-tip-platform.md — "the broadcast venue; its native support economy is a monetization feature of that Type".
- applications/instant-messaging-application.md — "primary surface is a live broadcast with many simultaneous viewers".

## Product Observations

### Source-access situation

No sampled product's documentation was directly observed this pass (see Sources). The observations below are therefore of two kinds only:

- **(S) Structural observations** — properties intrinsic to the broadcast-audience model, defensible without vendor documentation.
- **(X) Cross-pass observations** — boundary characterizations documented by processed sibling passes (listed above), each of which researched real products from its own side.

### Structural observations (S)

- **(S1)** The unit of experience is the live broadcast: a real-time video stream that exists while it happens. Everything of value is produced during the live window. This is the only state in which the product's core experience occurs; recorded forms are derivatives.
- **(S2)** The broadcast is originated by an identified individual user of the platform, not by a programmed media channel. The broadcaster is a profile-carrying participant, not a station.
- **(S3)** The audience is many and simultaneous: one broadcaster, many concurrent viewers. The roles are asymmetric — the broadcaster holds the floor; viewers watch and participate through channels (chat, reactions), not as equal co-present participants.
- **(S4)** The audience is assembled by the platform: discovery surfaces (browse, categories, follow feeds, recommendations) gather strangers and followers into the same live room. A broadcast whose audience is privately invited has left the platform posture.
- **(S5)** Viewers act during the broadcast and those acts are visible to the broadcaster and commonly to each other within the live context: chat messages, reactions, and — where monetized — gifts. The interaction is part of the broadcast experience, not an accessory.
- **(S6)** Participation binds to persistent identities: chat and gifts attach to user accounts; the viewer→streamer relationship (following) carries across broadcasts, giving the broadcaster a returning audience.
- **(S7)** Because the medium is live public video before an assembled audience, conduct control (moderation, rules, enforcement) is a structural necessity of the Type, not an enterprise add-on.
- **(S8)** Public user-generated broadcast requires an eligibility gate of some kind (account standing, age, thresholds); the existence of a gate is structurally necessary, its mechanics are product-specific and unverified this pass.

### Cross-pass observations (X)

- **(X1)** From the social-audio side: this Type is the video-medium sibling — "one-performer broadcast economy" vs the audio Type's multi-speaker governed floor. The two Types share the live-room-before-an-audience structure and differ in medium and floor mode.
- **(X2)** From the random-video-chat side: this Type is asymmetric (one broadcaster, many viewers) where random chat is symmetric 1:1; both may carry gifting/performance economies.
- **(X3)** From the short-form-video side: live streaming is commonly bundled inside short-video products but remains an attached surface; the unit differs (live real-time broadcast vs persistent recorded short video).
- **(X4)** From the internet-radio side: this Type's live surfaces are driven by individual creators with social interaction; radio is station-organized scheduled programming without creator-driven social surfaces.
- **(X5)** From the chat-room/community-chat sides: stream chat is a room-shaped surface subordinate to the broadcast; the primary object is the stream, and the audience relationship is viewer→streamer.
- **(X6)** From the creator-tip side: the gifting/support economy is this Type's "native support economy" — a monetization feature of the Type, not its defining structure.
- **(X7)** From the microblogging/general-social-network/photo-centric sides: the seam is persistence — posts/photos/updates are persistent asynchronous artifacts; the live broadcast is ephemeral-first.
- **(X8)** From the social-audio pass's taxonomy note: the Type is realized substantially as a feature inside larger social/community/video platforms; sibling passes should treat platform-embedded live symmetrically.

## Cross-product Comparison

| Structure | Twitch (orientation) | BIGO Live (orientation) | TikTok LIVE (orientation) | YouTube Live (orientation) | Historical generation (conceptual) |
|---|---|---|---|---|---|
| User-originated live broadcast | yes (creators) | yes (mobile broadcasters) | yes (eligible users) | yes (creators + media mix) | yes (individual live channels) |
| Platform-assembled simultaneous audience | yes (categories, follow feeds) | yes (mobile discovery) | yes (feed + live surfaces) | yes (search/browse/notifications) | yes (channel directories) |
| In-broadcast participation loop | yes (chat, reactions, support mechanics) | yes (chat, gifts) | yes (chat, gifts) | yes (chat, reactions) | yes (chat; reactions/hearts in the mobile generation) |
| Persistent broadcaster identity + returning audience | yes (channel, followers) | yes (profile, fans) | yes (profile, followers) | yes (channel, subscribers) | yes (channels) |
| Recorded afterlife (VOD/clips) | characteristic | varies | varies | characteristic | partial/absent in early products |
| Monetization machinery | characteristic (subs/ads/support) | characteristic (gift economy) | characteristic (gifts) | characteristic (memberships/ads) | largely absent in the founding generation |
| Realization posture | standalone dedicated | standalone dedicated mobile | embedded in short-video platform | embedded in video platform | standalone web |

Reading: the first four rows are constant across every column — including the conceptual historical column — which is the signature of the defining core. The last three rows vary across columns, which marks them as common/variant structure, not definition.

## Canonical Model — Four Abstraction Layers

### L0 — Defining Invariant (three jointly-held structures)

1. **The user-originated live broadcast as the unit of experience.** A real-time video stream produced by an identified individual user of the platform — not a programmed media channel, not a recorded upload. Live is the primary state: the broadcast exists while it happens and its value is produced in real time. *Remove → Video Streaming Platform / recorded-content social platform territory.*
2. **The platform-assembled simultaneous audience in asymmetric roles.** Many viewers watch the same stream at the same time, in audience role — watching and participating through channels, not as equal co-present participants — and the audience is gathered through the platform's own discovery surfaces rather than private invitation. *Remove the asymmetry → Live Video Chat / video calling; remove platform assembly → private stream/embed.*
3. **The in-broadcast participation loop.** Viewers act during the broadcast — chat/messages, reactions, commonly gifting — and those acts are visible to and answered by the broadcaster within the live context; participation binds to persistent user identities, and the viewer→streamer audience relationship carries across broadcasts. *Remove → one-way live distribution (event stream / station-style broadcast); the "social" in the Type's name is this loop.*

Jointly-held load-bearing:

- 1 alone = live video distribution (event streams, media live channels)
- 1+2 without 3 = one-way live broadcast platform — streaming, but not social
- 1+3 without 2 = a stream with chat but no platform discovery — private/permalink streaming, drifting out of the platform posture
- 2+3 without 1 = audience-shaped chat rooms with no broadcast — Community Chat territory
- Remove video-primary (keep audio rooms with governed floor) → Social Audio Platform
- Remove liveness (recorded short videos) → Short-form Video Social Platform
- Remove one-to-many (platform-paired 1:1) → Random Video Chat Application

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Broadcaster channel/profile page accumulating streams, followers, and past broadcasts
- Follow relationship (viewer subscribes to the broadcaster; live notifications)
- Live discovery surfaces: category browse, featured/recommended rails, "following is live" feeds
- Chat moderation toolset: delegated moderators, participant removal, chat restrictions
- Virtual gifting / support economy — the monetized form of participation
- Recorded afterlife: VODs, replays, clips, highlights
- Co-streaming / guest invitations (multi-broadcaster formats)
- Broadcasting setup tooling (desktop encoder/stream-key culture; in-app camera on mobile)
- Categories/tags organizing content domains

### L2 — Variant / Optional Structure

- Monetization posture: gift economies vs subscriptions vs ad revenue share vs e-commerce integration
- Eligibility gating mechanics for going live (existence structural; mechanics product-specific)
- Mobile-first vs desktop/web-first culture
- Standalone dedicated product vs platform-embedded feature (substantial embedded share per X8)
- Regional market shapes (gift-economy-centric mobile markets vs subscription-centric Western markets vs Chinese-market platforms)
- Content-domain organization (gaming-rooted category ecosystems vs general entertainment)
- Private/unlisted broadcasts vs public-by-default
- Multi-host formats (talk-show style, co-host/battle formats)

### L3 — Vendor-specific Structure (research notes only)

Nothing asserted this pass — no vendor documentation was reachable. Vendor-specific machinery (specific gift currencies, subscription tiers, revenue shares, eligibility numbers, branded programs, category names) is deliberately absent from both files.

## Vendor-specific Findings

None recorded — see L3 above. The sampled products' well-known postures (gaming-rooted category ecosystems, gift economies, embedded realization) are used only as market orientation in the Representative Products sections, never as evidence for operational claims.

## Rejected Findings (anti-overfitting)

- **Virtual gifting is NOT definitional.** The founding generation of the Type ran on chat alone; the creator-tip sibling pass documents the support economy as "a monetization feature of that Type". The participation loop is definitional; gifting is its monetized form.
- **Algorithmic recommendation feed is NOT definitional.** Follow/browse discovery is the older and still-sufficient form (consistent with the short-form-video sibling's finding that the algorithmic feed is the modern dominant implementation of discovery, not the discovery itself).
- **VOD/clips are NOT definitional.** Live-first is the core; the recorded afterlife is a product posture (consistent with the social-audio sibling's persistence finding).
- **Mobile-first is NOT definitional.** Desktop/web streaming culture is a full realization of the Type.
- **Gaming categories are NOT definitional.** General-entertainment and mobile-social realizations exist without gaming-rooted category trees.
- **Co-streaming/multi-host is NOT definitional.** The solo broadcast is the base form; multi-broadcaster formats are variants.
- **Follower notifications are NOT definitional.** Discovery can run on browse alone; the follow graph is the common mature form of the returning-audience structure.

## Historical / Market-Sample Check (conceptual)

Question: would older, regional, platform-native, or differently positioned products still fit the L0?

- The founding generation (mid-2000s individual live channels with chat and channel directories) satisfies all three legs: user-originated live broadcast, directory-assembled audience, in-broadcast chat loop. No monetization, no algorithmic feeds, no mobile, no VOD required.
- The 2015 mobile generation (broadcast-from-your-phone with hearts/reactions and follower-based discovery) satisfies the same three legs with different machinery.
- Regional gift-economy markets and subscription-centric Western markets realize the same core with different monetization postures.
- Platform-embedded realizations (live inside social networks, short-video apps, video platforms) satisfy the three legs while inheriting identity and discovery from the parent product.

The L0 names no era machinery: no algorithmic feed, no gifting, no mobile form, no VOD, no subscriptions, no categories. **Historical check passed conceptually** (at the strength available given source limitations).

## Boundary Findings

| Neighboring Type | Remove what from this Type → becomes that Type |
|---|---|
| Video Streaming Platform (§27) | remove the user-originated broadcast (supply becomes licensed/produced catalog, on-demand primary) → media streaming |
| Live Video Chat Application (§01.08) | remove the assembled audience (make participants equal peers in a small group) → live video chat |
| Social Audio Platform (§01.08) | remove video-primary (audio rooms, multi-speaker governed floor) → social audio |
| Random Video Chat Application (§01.08) | remove the broadcast-audience structure (platform-paired 1:1 between equal peers) → random video chat |
| Short-form Video Social Platform (§01.05) | remove liveness (the unit becomes the persistent recorded short video) → short-form video |
| Microblogging Platform (§01.05) | remove liveness and the broadcast room (the unit becomes persistent asynchronous posts) → microblogging |
| Webinar Platform (§01.04) | remove the social/entertainment posture (organization-run, registration-based presentations to a defined business audience) → webinar |
| Internet Radio Platform (§27) | remove the individual creator and the participation loop (station-organized scheduled programming) → internet radio |
| Community Chat Platform / Chat Room Application (§01.06) | remove the broadcast (the room-shaped chat becomes the primary object) → community chat |
| General Social Network (§01.05) | remove liveness (persistent profile + feed of updates as the primary surface) → social network |

The three load-bearing boundaries, in order: **liveness** (vs every recorded-content Type), **asymmetry** (vs calling/chat Types), **participation** (vs one-way distribution Types). The medium seam (video vs audio) separates this Type from Social Audio; the supply seam (individual users vs programmed media) separates it from Video Streaming Platform and Internet Radio.

## Uncertainties

1. **No official documentation was reachable.** All product-specific operational facts (eligibility thresholds, gift mechanics, revenue shares, moderation tooling specifics, VOD retention) are unverified and deliberately absent from both files.
2. **Whether any market product realizes the Type without a follow mechanism** (browse-only discovery) — unverified; follow is held as common mature structure, not definitional.
3. **The exact seam against Live Video Chat Application** (§01.08 sibling, unprocessed at the time of this pass): multi-guest live rooms with a watching audience straddle the two labels; flagged for joint review in that pass.
4. **The embedded share of the market** — likely substantial (per X8) but unquantified this pass.
5. **The seam against Video Streaming Platform (§27, unprocessed)**: live-event and media live streaming vs user-originated live — the "who broadcasts" key should be ratified on that side; flagged.

## Final Synthesis

A Social Live Streaming Platform is a platform whose unit of experience is the **live video broadcast originated by an identified individual user**, before a **simultaneous audience assembled by the platform's own discovery surfaces**, with an **in-broadcast participation loop** (chat, reactions, commonly gifting) that binds viewers to the broadcaster and carries across broadcasts through persistent identity.

The defining core is three jointly-held structures: the user-originated live broadcast, the platform-assembled asymmetric audience, and the participation loop. Everything else the category is known for — gifting economies, subscriptions, algorithmic discovery, VODs and clips, co-streaming, mobile-first forms, gaming categories — is common mature or variant structure.

The Type sits at the intersection of three removal tests: remove liveness → recorded-content social Types; remove the assembled audience/asymmetry → calling and chat Types; remove participation → one-way distribution Types. The medium seam separates it from Social Audio; the supply seam (individual users, not programmed media) separates it from Video Streaming Platform and Internet Radio.
