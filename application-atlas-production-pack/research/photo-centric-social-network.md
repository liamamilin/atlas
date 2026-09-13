# Research Notes — Photo-centric Social Network

## Research Goal

Understand the canonical structure of the Photo-centric Social Network Application Type: what objects its world consists of, what the unit of publication and the unit of consumption are, how person-to-person ties distribute photos, what rules govern visibility and audience, and where the boundary lies with the sibling Types of the §01.05 Social Networking family (General Social Network, Microblogging Platform, Short-form Video Social Platform, Interest-based Social Network, Professional Social Network, Neighborhood Social Network, Social Profile Network, Friend Discovery Application) and with adjacent Types (photo editing tools, photo storage, community platforms, messaging).

This pass also carries two joint-review obligations from sibling passes:

1. **Ratify the Pinterest-class assignment** — the interest-based-social-network pass (2026-09-07) assigned Pinterest-class visual-interest products to Interest-based Social Network by organizing key and asked this pass to ratify from the photo-centric side.
2. **Ratify the §01.05 family framework from the content-type side** — the general-social-network pass (2026-09-07) proposed the family discriminator "organizing key of the core consumption/distribution loop" with photo-centric as a content-type-keyed sibling; the microblogging-platform pass (2026-09-08) ratified it with the refinement that the seam is the organizing key, not media presence (modern microblogging products ship heavy media as capabilities).

## Initial Boundary (pre-research hypothesis)

- Core hypothesis: a social network where the **photo** is the organizing object of both publication and consumption, distributed through a person-keyed social graph, with profiles that accumulate each member's photos.
- Likely confusions: General Social Network (untyped posts, photos as one capability among many); Interest-based Social Network (Pinterest-class photo-medium but interest-keyed; 500px-class photography-interest networks); Short-form Video Social Platform (video-first sibling); photo editing / photo workflow tools (creation without the social loop); photo storage/backup services (no consumption loop, no ties); community platforms / photo forums (topic-keyed containers); messaging (photo sharing inside private conversations).
- Unknowns going in: whether public discovery is definitional (vs friends-only); whether follow vs mutual-friend tie semantics is definitional; whether capture/editing tools are definitional; whether ephemeral (stories) and video surfaces break photo-centricity; how the web-era photo-community generation relates to the modern mobile form.

## Research Questions

1. What exactly is the unit of publication — how does the photo object relate to captions, multi-photo posts, albums, prompted capture?
2. What is the unit of consumption — personal feed vs discovery/explore surfaces; stream vs grid?
3. What tie semantics exist (mutual friend request vs one-way follow) and what do they gate?
4. What interactions attach to the photo post (reactions, comments, reshares, tags)?
5. How does the profile accumulate photos, and what archive/memory machinery exists?
6. What role do capture/editing tools play — definitional or capability?
7. How do ephemeral surfaces (stories-class) and other media (video, audio) fit without breaking the Type?
8. What audience/privacy machinery exists (private accounts, per-post audience, per-post interaction controls)?
9. Historical/market-sample check: would a web-era photo community (Flickr-class) satisfy the same definition?
10. Boundary: does the Pinterest-class product belong here or in Interest-based Social Network? Where do 500px-class and VSCO-class products sit?

## Representative Products

Selection logic: market representation + documentation accessibility + different product philosophies + different customer tiers. The canonical mass-market products (Instagram, Flickr, 500px, Glass, EyeEm, VSCO) were all unreachable from the research environment this pass (see Sources); the directly observed sample therefore spans the two reachable poles, with the unreachable products retained as market context only.

| Product | Role in sample | Philosophy / pole | Evidence |
|---|---|---|---|
| BeReal | friends-first consumer pole | daily prompted capture, no filters, no algorithmic discovery, anti-staging | A (Tier-1: root + 5 help articles) |
| Pixelfed | public federated creator pole | open-source, federated (ActivityPub), upload-any-photo, hashtag discovery, chronological | A (Tier-1: official docs + ActivityPub spec) |
| Instagram | canonical mass-market product | algorithmic photo/video feed at maximal scale | NOT observed — market context only |
| Flickr | web-era photo community | photostreams, contacts, groups, favorites/comments | NOT observed — historical context only |
| 500px | enthusiast/photographer showcase | photography community + licensing | NOT observed — market context only |

## Sources

Fetched 2026-09-08 (all REACHABLE):

- BeReal root — https://bereal.com/ — positioning ("Your daily dose of real life", front-back format, anti-filter/anti-staging, friends-focused, "no AIs allowed").
- BeReal Help Center home — https://help.bereal.com/hc/en-us — section taxonomy (Troubleshooting / The Guide / Safety; popular articles).
- BeReal The Guide (category index) — https://help.bereal.com/hc/en-us/categories/7209052114973-The-Guide — full section taxonomy (RealPeople & RealBrands / BeReal / Friends / Profile / Settings / Everything else).
- BeReal "Time to BeReal" — https://help.bereal.com/hc/en-us/articles/7350386715165 — daily notification, 2-minute window, front+back capture, retakes, late-post marking, posting gate, location, captions, audience choice.
- BeReal "Friends of Friends" — https://help.bereal.com/hc/en-us/articles/11773264475933 — FoF feed mechanics, mutual-friends display, friend invitation from feed, RealMoji-only (no comments) in FoF, audience changeable after posting, audience persistence, hidden users.
- BeReal "Friend Recommendations" — https://help.bereal.com/hc/en-us/articles/13270135622557 — mutual friends + contact-sync (phone matching) recommendations, limited profile info, phone numbers never shared, opt-outs.
- BeReal "Memories" — https://help.bereal.com/hc/en-us/articles/7531349180829 — private archive of past posts, share/download/delete, default-on, activation rules.
- BeReal "RealFans" — https://help.bereal.com/hc/en-us/articles/16280722573341 — RealPeople & RealBrands verified public accounts, engagement-earned RealFan status, exclusive content, comments on public accounts' BeReal.
- Pixelfed docs — https://docs.pixelfed.org/ and https://docs.pixelfed.org/project/introduction.html — "A fresh take on photo sharing. Get inspired with beautiful photos captured by people around the world."
- Pixelfed ActivityPub spec — https://docs.pixelfed.org/spec/ActivityPub.html — Person actor (following/followers collections, manuallyApprovesFollowers, indexable, avatar, summary), Note+Image-attachment statuses, hashtags, mentions, commentsEnabled + capabilities ACL (announce/like/reply), sensitive/content warnings, location geo-tagging, blurhash, Like/Announce/Follow/Accept/Reject/Undo activities, Story objects, federated Groups, Authorized Fetch.

Unreachable (limitations recorded; per evidence rules no precise claims drawn from memory for these):

- Instagram — about.instagram.com (timeout), www.instagram.com (timeout), developers.facebook.com Instagram platform docs (transport error ×2) → abandoned. Consistent with the general-social-network pass's recorded limitation (help.instagram.com timeout). No Instagram-specific operational claims anywhere in this pass.
- Flickr — www.flickr.com/help (timeout), help.flickr.com (timeout) → abandoned; Wikipedia fallback (timeout) → abandoned. Historical check therefore kept CONCEPTUAL.
- 500px — help.500px.com (transport error), 500px.com (transport error) → abandoned.
- Glass — glass.photo (403) → abandoned.
- EyeEm — www.eyeem.com (403) → abandoned.
- VSCO — vsco.co (403) → abandoned.

Consequence: the direct observational base is two products at opposite structural poles (friends-private daily-capture vs public federated upload). All final-document claims are calibrated to that base: cross-product commonalities are asserted only where both observed poles agree or where the structure is conceptually necessary; everything else is kept at variant/optional strength. No precise numbers, defaults, or feature lists attributable to unreachable products appear anywhere.

## Product A — BeReal (direct observation, evidence layer A)

Official positioning (bereal.com, fetched 2026-09-08):

1. Self-description: "Your daily dose of real life"; a daily ritual — "Every day, the world gets to be themselves for a random two-minute window"; "captures a spontaneous and unfiltered slice of daily life".
2. The signature format is the **front-back capture**: "We reject filters, staging, and uploads: our signature front-back format captures the scene and the individual behind it at the same time."
3. The social frame is **friends**: "the place where you get to see what your friends are actually doing"; "make real connections with those who really matter."
4. Explicit anti-posture: "no AIs allowed."

Help-center structure (The Guide category index): RealPeople & RealBrands / BeReal / Friends / Profile / Settings / Everything else — a friends-first photo network with a verified-public-accounts layer on top.

"Time to BeReal" article:

1. Daily notification at the same time for everyone in a time zone; a 2-minute window to capture; a BeReal "uses front and back cameras to capture your surroundings"; retakes allowed within the window.
2. **Posting gate**: "You can't view your friends' BeReal or the Friends of Friends feed until you've posted yours."
3. Late posting is allowed but visible ("your friends will know you posted late").
4. Optional location display; optional share to the Friends of Friends feed; captions added after posting.

"Friends of Friends" article:

1. The FoF feed extends distribution one hop: "your post is shared with your BeReal friends and their BeReal friends."
2. Reciprocity gate repeated: "you need to post to the Friends of Friends feed to view the feed."
3. Mutual friends are displayed above each BeReal; tapping a username opens the profile and offers a friend invitation — **the discovery surface feeds the tie graph**.
4. In the FoF feed, reactions (RealMoji) are allowed but comments are not ("can react… but can't leave or view comments").
5. Audience is a per-post choice ("My friends" vs "My friends + their friends"), changeable after posting, and "your chosen audience is saved for future posts unless you modify it."
6. A hidden-users list removes a person from the FoF feed and friend suggestions.

"Friend Recommendations" article:

1. Recommendations come from mutual friends and from **contact syncing** (uploaded contacts matched to users).
2. Recommended users show only selected profile information; their BeReals and Memories are not viewable pre-tie.
3. Phone numbers are never shared with other users; opt-outs exist (don't share phone number, disable contact syncing). Identity substrate is phone-number-based.

"Memories" article:

1. Memories are "a collection of your past BeReal posts" displayed on the profile — **the profile is the photo archive**.
2. Private by default: "No one but you can view your Memories, not even your BeReal friends."
3. Per-memory share/download/delete; activation rules (cannot deactivate once activated).

"RealFans" article:

1. **RealPeople & RealBrands** are a distinct account class (verified public figures/brands) added by users.
2. **RealFans** status is earned through engagement (tagging, reacting, sharing) with those accounts; RealFans get comments on the public accounts' BeReal, exclusive content, and higher reshare chances.
3. This is a public-creator layer grafted onto a friends-first core — evidence that public creator accounts are an extension, not the base graph.

Evidence layer: A throughout (official help articles, directly observed). Product-specific mechanics (2-minute window, posting gate, RealMoji, RealFans, front-back format) are L3.

## Product B — Pixelfed (direct observation, evidence layer A)

Official positioning (docs.pixelfed.org introduction): "A fresh take on photo sharing. Get inspired with beautiful photos captured by people around the world." — photo sharing with public discovery as the frame; open-source and federated (ActivityPub), self-hostable.

ActivityPub spec page (protocol-level documentation of the product's own data model):

1. **Person actor** with `following` and `followers` collections (one-way follow semantics at protocol level), `manuallyApprovesFollowers` (private accounts — "If the account is private, this value is set to `true`"), `indexable` (crawl permission), avatar, summary/bio, account aliases.
2. **The photo post is a Note with Image attachments** — statuses carry one or more `Image` attachment objects with mediaType and optional per-image name; content is caption-level text with hashtags and mentions.
3. **Interactions attach to the status**: Like, Announce ("boosting"), replies; per-post **capabilities ACL** lets the author disable Announce/Like/reply (`commentsEnabled`, `canAnnounce`, `canLike`, `canReply`).
4. **Follow lifecycle**: Follow → Accept/Reject (follow requests can be denied) → Undo.Follow.
5. **Discovery metadata**: hashtags (`#pixelfed`-style tag objects with discover URLs), location geo-tagging (Place with name/lat/long/country), sensitive-content flags (media concealed by default with content warnings), blurhash previews.
6. **Ephemeral surface exists**: Story objects (Add.Story / Delete.Story / Story:Reaction / Story:Reply / View), federated only to known Pixelfed instances.
7. **Containers exist**: federated Groups (Group actor, group walls) — communities beside the person graph.
8. Federation with other Pixelfed instances and fediverse software (Mastodon) via signed Authorized Fetch.

Evidence layer: A (official protocol documentation, directly observed). ActivityPub/federation mechanics are L2/L3 (variant substrate, vendor-specific detail).

## Historical / market-sample check (§24 check)

Question: would older, regional, platform-native, or differently positioned products still fit the definition?

- **Web-era photo community (Flickr-class, mid-2000s)**: photos published as photostream items, contacts-based feeds, profiles accumulating photos, favorites/comments on photos, groups beside the graph. Conceptually satisfies all three L0 legs. **Not verifiable via sources this pass** (Flickr and Wikipedia both unreachable) — recorded as an uncertainty; the L0 is nevertheless written so that this generation fits (no mobile-first, no filters, no algorithmic feed required).
- **Regional/platform-native forms**: photo-heavy personal homepage networks (Cyworld-class minihompy) and device-ecosystem photo sharing fit conceptually; not sampled this pass.
- **Modern mobile poles (observed)**: BeReal (friends-first, prompted capture) and Pixelfed (public, federated, free upload) both satisfy the L0 despite opposite postures — the definition holds across the poles.
- The definition is deliberately written identity-substrate-neutral (phone number, username, federated handle all satisfy) and capture-neutral (prompted in-app capture and free upload both satisfy).

## Cross-product Comparison

| Dimension | BeReal (observed) | Pixelfed (observed) | Instagram / Flickr / 500px (not observed) |
|---|---|---|---|
| Unit of publication | the BeReal post — front+back photo pair, caption added after | the status — one or more Image attachments with caption text | canonical (not verified) |
| Unit of consumption | friends feed + Friends of Friends feed | home feed (follow graph) + discover/tags | canonical (not verified) |
| Tie semantics | mutual friend request (friends); "add" for public accounts | one-way follow with accept/reject for private accounts | canonical (not verified) |
| Profile | profile + private Memories archive + pins | profile + outbox (public statuses) | canonical (not verified) |
| Interactions on the photo | RealMoji reactions; comments in friends context (not in FoF); reshares | Like, Announce (boost), replies; per-post ACL | canonical (not verified) |
| Discovery beyond ties | Friends of Friends feed (one-hop, gated on posting) | hashtags, discover, federation-wide | canonical (not verified) |
| Audience/privacy | per-post audience (friends vs +their friends), hidden users, private Memories | private accounts (manuallyApprovesFollowers), per-post interaction ACL, sensitive flags, indexable | canonical (not verified) |
| Capture/editing | prompted daily in-app capture; filters/staging/uploads rejected | free upload; no capture machinery documented | canonical (not verified) |
| Other media | BeReal Audio, Behind The Scenes surface, stories-class extensions | Story objects, federated Groups | canonical (not verified) |
| Identity substrate | phone number + contact sync | federated username handle | canonical (not verified) |
| Ephemeral surface | late-post marking; (BTS surface) | Story objects with reactions/views | canonical (not verified) |

Cross-product commonalities (evidence layer B where both observed poles agree, C where inferred):

1. **Photo post as the unit of publication** — B (both poles; the photo object is primary, text is caption-level).
2. **Photo stream as the unit of consumption** — B (both poles; the home surface is a stream of others' photos).
3. **Person-keyed ties distributing photos between photo-accumulating profiles** — B (both poles).
4. **Interactions attaching to the photo post** — B (reactions/comments/likes/boosts all bind to the post object).
5. **Audience/privacy machinery over the graph** — B (both poles; forms differ).
6. **Discovery beyond the tie graph as a secondary surface** — B (FoF feed; hashtags/discover).
7. **Profile as the person's photo archive** — B (Memories; outbox/profile grid).
8. **Ephemeral/other-media surfaces as extensions** — B (both poles ship them; neither organizes the core loop around them).
9. **Notifications, search, account machinery** — C (conceptually necessary; no precise claims).

## Canonical Model (four layers)

### L0 — Defining Invariant (deliberately minimal)

```text
Photo Post
  (the unit of publication: a photo object with caption-level text;
   other media ride on it as extensions)
└── Photo Stream
    (the unit of consumption: a stream/grid of other members' photos —
     from personal ties and/or a discovery surface)
└── Person-keyed Photo Graph
    (ties — friend or follow — between personal profiles that
     accumulate each member's published photos; distribution and
     interaction run through these ties and attach to the photo post)
```

Three jointly-held structures. Removal tests:

- Remove the **photo post as organizing unit** (posts become untyped text-plus-anything) → General Social Network — not this Type.
- Remove the **photo stream as consumption unit** (photos stored/shared but nothing to browse) → photo storage/backup or a bare gallery — not this Type.
- Remove the **person-keyed graph** (distribution keyed by interest/topic/board instead of person ties) → Interest-based Social Network or a photo community/forum — not this Type.
- Remove the **social graph entirely** (browse-only gallery) → stock-photo/wallpaper site — not this Type.

Jointly-held is load-bearing:

- 1 alone = photo hosting/gallery (storage-first product).
- 2 alone = photo discovery/curation surface (no ties, no personal distribution).
- 3 alone = General Social Network (untyped posts).
- 1+2 without 3 = interest-keyed visual discovery (Pinterest-class) — the interest-based sibling.
- 1+3 without 2 = photo sharing with no consumption loop (messaging-adjacent or storage).

Note on the feed: L0 requires a consumption surface structured as a stream of photos; it does NOT require any particular ordering (chronological, algorithmic), a grid layout, or a discovery/explore surface — those are L1/L2.

Note on ties: L0 is deliberately tie-semantics-neutral (mutual friend request and one-way follow both satisfy); the tie MEANING is a variant axis.

Note on capture: L0 requires publishing photos; it does NOT require in-app capture, filters, or editing — the prompted-capture pole and the free-upload pole both satisfy.

### L1 — Common Mature Structure

- **Interactions on the photo post** — reactions/likes, comments, reshares/reposts; per-post interaction controls in mature products.
- **Profile as photo archive** — the member's published photos accumulate on their profile (grid/photostream/memories forms).
- **Discovery beyond ties** — explore/discover surfaces, hashtag streams, suggestions (mutual-connection-driven), one-hop expansion (friends-of-friends class).
- **Audience/privacy controls** — private accounts, per-post audience selection, hidden/blocked users.
- **Notifications** — alerts for tie and interaction activity.
- **People/location/hashtag tagging** — metadata attaching photos to people, places, topics.
- **Ephemeral surfaces (stories-class)** — 24h-style photo surfaces beside the persistent stream.
- **Other media riding on the loop** — short video, audio, multi-photo posts as extensions of the photo post.
- **Photo editing tools** — common in many products but NOT universal (the anti-filter pole explicitly rejects them).
- **Messaging surface** — private photo/message exchange beside the public loop (often a separate app sharing the identity).
- **Account machinery** — registration, identity substrate, block/report, multi-device clients.

### L2 — Variant / Optional Structure

- Tie semantics: mutual friend request vs one-way follow vs layered.
- Audience posture: friends-private default vs public-by-default.
- Capture discipline: prompted daily capture vs free upload vs camera-first creation.
- Identity substrate: phone number + contact sync vs username vs federated handle.
- Federation/self-hosting (protocol-level distribution across independent servers).
- Creator/public-account layers (verified public figures/brands beside the personal graph).
- Monetization: ads, subscriptions, licensing/marketplace (business-model drift, not structure).
- Regional/era forms: web-era desktop communities vs mobile-first apps.
- Video/short-video surfaces — capability drift toward the short-form sibling; presence does not reassign the Type (organizing-key test).

### L3 — Vendor-specific (research notes only)

- BeReal: the 2-minute daily window and time-zone-synchronized notification; the posting gate (cannot view friends'/FoF feeds until posting); front-back dual capture; late-post marking; RealMoji (selfie reaction); RealFans engagement-earned status; RealPeople & RealBrands account class; Memories activation rules; hidden-users list; "no AIs allowed" positioning; streaks; pins.
- Pixelfed: ActivityPub actor/status model; manuallyApprovesFollowers; capabilities ACL (canAnnounce/canLike/canReply); blurhash previews; bearcaps for stories; federated Groups (FEP-400e); Authorized Fetch; indexable flag; Story objects federated only to known Pixelfed instances.

## Rejected Findings

- "Photo-centric social networks require filters/editing tools" — REJECTED as definitional: the anti-filter pole explicitly rejects them; the upload pole ships none as core. Editing is a common capability at best.
- "Public accounts and algorithmic discovery are definitional" — REJECTED: the friends-first pole has neither as its base loop; discovery is a secondary surface in both poles.
- "One-way follow is the definitional tie" — REJECTED: mutual friend request and one-way follow both observed; tie semantics is a variant axis.
- "Phone-number identity is definitional" — REJECTED: federated username pole observed; identity substrate varies (same anti-overfitting pattern as the IM pass's phone-number precedent).
- "In-app capture is definitional" — REJECTED: prompted capture and free upload both observed.
- "Stories/video presence breaks photo-centricity" — REJECTED: both observed poles ship ephemeral and other-media surfaces as extensions; the organizing key of the core loop remains the photo (consistent with the microblogging pass's refinement that the seam is the organizing key, not media presence).
- "Multi-photo posts/albums are definitional" — REJECTED as L0: multi-image posts observed in one pole, dual-photo framing is product-specific; single-photo posts satisfy the core.

## Boundary Findings

The §01.05 family discriminator (ratified by the general-social-network and microblogging-platform passes): **the organizing key of the core consumption/distribution loop**. For this Type the organizing key is the **content type — the photo object**.

| Neighbor Type | Relationship | Discriminator (what removed/changed → becomes that Type) |
|---|---|---|
| General Social Network | family parent | untype the post (photo becomes one capability among many) → general SNS; the photo-centric Type is the stream restricted to one content class |
| Interest-based Social Network | organizing-key sibling | re-key distribution by interest/topic/board rather than person ties → interest-based. **Pinterest-class ratification: stays interest-based** — the photo is the medium, but consumption is organized by interest (boards/search/ideas), profiles are idea collections, and person-to-person ties are not the distribution spine |
| Short-form Video Social Platform | content-type sibling | re-key the loop to video-first creation/discovery → short-form video; video surfaces inside a photo-centric product are capabilities, not a re-keying |
| Microblogging Platform | content-type sibling | re-key to broadcast-subscription status updates consumed as a merged stream → microblogging; heavy media presence does not move a product here |
| Professional Social Network | audience sibling | re-key identity/content by career/professional semantics → professional |
| Neighborhood Social Network | locality sibling | gate membership by verified locality → neighborhood |
| Social Profile Network | substrate sibling | remove the photo stream → profiles + connections directory |
| Friend Discovery Application | formation-loop sibling | making the formation of NEW ties with strangers the primary job → friend discovery; here the graph starts from known people and discovery is auxiliary |
| Photo Editor / Photo Workflow / RAW Editor (§04.04) | creation-tool sibling | remove the social loop (publish/stream/ties) → a creation tool; creation-first products with a community layer (VSCO-class) straddle — unresolved, see Uncertainties |
| Personal Cloud Drive / photo storage | storage sibling | remove consumption stream and ties → storage/backup |
| Community Platform / Online Forum | container sibling | re-key content by topic containers and threads rather than who posted → community/forum |
| Instant Messaging Application | conversation sibling | photo exchange inside private conversations keyed to a thread, not a stream → IM |
| Social Live Streaming Platform | temporality sibling | live broadcast with simultaneous viewers vs persistent photo stream |

Boundary blur zones recorded honestly: modern photo-centric products ship stories, short video, messaging, creator accounts, and shopping surfaces — each is a capability overlap, not a Type merge; assignment follows the organizing key of the core loop.

## Uncertainties

1. Instagram, Flickr, 500px, Glass, EyeEm, VSCO all unreachable this pass — the canonical mass-market product contributes no direct evidence; the model rests on two opposite-pole products. All claims about unreachable products are excluded; they appear as market context only.
2. Historical check kept CONCEPTUAL — the web-era photo community's fit is argued from structure, not from reachable sources (Flickr + Wikipedia both timed out).
3. VSCO-class creation-first products (editing-first with a community layer) straddle §04.04 Photo Editor and this Type — unresolved; flagged for joint review if that pass processes.
4. 500px-class photography-interest networks: held in this Type on the organizing-key test (the photo object still organizes the loop; the interest defines the audience), but without direct evidence this pass. If a product re-keys the loop around structured domain objects (films, routes, books — Letterboxd/Strava-class), it belongs to interest-based per that pass's domain-binding refinement.
5. Prevalence claims (how common each tie semantics, audience posture, or monetization form is in the market) were not measurable with two observed products — kept as variant axes without prevalence assertions.
6. Whether the aggregated multi-author feed is definitional was resolved the same way as the general-SNS pass: the L0 requires a photo stream as consumption surface but not any particular feed implementation; profile-browsing consumption (photostream visiting) satisfies the same invariant.

## Final Synthesis

The Photo-centric Social Network is the **content-type-keyed member of the social-network family**: a network whose core loop is organized around the photo object. Members publish photos as posts (caption-level text; other media as extensions), consume a stream of other members' photos (from personal ties and/or discovery surfaces), and connect through person-to-person ties between personal profiles that accumulate each member's photos; interactions attach to the photo post. The defining core is exactly three jointly-held structures — photo post as unit of publication, photo stream as unit of consumption, person-keyed photo graph as the distribution substrate. Interactions, profile archives, discovery, audience controls, tagging, stories, editing tools, and messaging are common mature structure; tie semantics, audience posture, capture discipline, identity substrate, federation, and creator layers are variants. The Type is assigned by the organizing key: the photo object — not the untyped post (general SNS), the interest/board (interest-based), the video (short-form), the broadcast status (microblogging), or the topic container (community platform). Pinterest-class products are ratified as interest-based from this side: the photo is their medium, not their organizing key.
