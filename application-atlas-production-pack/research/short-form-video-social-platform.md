# Research Notes — Short-form Video Social Platform

## Research Goal

Establish what a Short-form Video Social Platform is as an Application Type: its minimal defining structure, its standard mature capabilities, its variant axes, and its boundaries against neighboring Types in §01.05 Social Networking (General Social Network, Photo-centric Social Network, Interest-based Social Network, Microblogging Platform) and against neighboring families (Video Streaming Platform, Social Live Streaming Platform, Personalized Content Feed, Video Editor).

Prior context from related passes (recorded in STATUS.md Boundary Issues): the §01.05 family discriminator is "the organizing key of the core consumption/distribution loop"; this leaf was flagged as a **content-type-keyed** member (photo-centric = photo key, short-form video = video key). This pass should ratify or refine that assignment.

## Initial Boundary

Working hypothesis before research:

- A platform where the primary published unit is a short video, circulated through a discovery feed, created with in-product tools, and wrapped in social interaction.
- Most likely confusions: General Social Network (untyped posts), Photo-centric Social Network (photo key), Video Streaming Platform (long-form catalog), Social Live Streaming Platform (live), Personalized Content Feed (selection without social/creation), Video Editor (creation without circulation).
- Open questions going in: Is the algorithmic "For You"-style feed definitional or only the modern dominant implementation? Is the follow graph definitional? Is in-product creation definitional or could a pure-consumption surface qualify?

## Research Questions

1. What is the unit of publication, and what metadata/attachments does it carry (sound, effects, caption, hashtags)?
2. How does content circulate: follow-graph feed, algorithmic recommendation, trending/editorial channels? Is circulation beyond the creator's own audience definitional?
3. What does the creation loop look like (capture → edit → publish)? Which creation capabilities are in-product (filters, stickers, music library, remixing/duet)?
4. What social structures exist (profile, follow graph, reactions, comments, private messages) and how do they attach to videos and creators?
5. What lifecycle and rules govern a video (privacy settings, review/moderation, deletion, recommendation eligibility)?
6. How do creators grow and monetize (creator programs, ad share, rewards, shopping/affiliate), and is monetization definitional or optional?
7. Where does this Type end and Video Streaming (long-form), Social Live Streaming, General/Photo SNS, and Personalized Content Feed begin?
8. Would older/regional/platform-native products (Vine-era follow-feed short video, lip-sync communities, regional GIF-community origins) still satisfy the definition?

## Representative Products

Chosen for market representativeness, documentation availability, distinct product philosophies, and distinct host-product situations:

| Product | Pole | Philosophy / situation |
|---|---|---|
| TikTok | pure-play archetype, algorithm-first | The category-defining standalone product. **Entirely unreachable this pass** (support.tiktok.com and newsroom.tiktok.com both timed out ×2). Kept as market anchor; no operational claims rest on it. |
| SnackVideo (Kuaishou family international product) | regional / social-first pole with heavy monetization machinery | Kuaishou Technology's international short-video community; "equal opportunity" distribution philosophy; rewards economy; live streaming. Rich reachable Help Center. |
| YouTube Shorts | annexed-to-long-form-video-platform pole | A short-video surface operated inside a long-form catalog platform; creators treat Shorts, long-form videos and livestreams as parallel monetizable formats. |
| Snapchat Spotlight | annexed-to-messaging-app pole | Public algorithmic recommendation surface operated inside a friend-first visual messaging app, with a formal eligibility regime for recommendation beyond friends/subscribers. |

## Sources

Fetched 2026-09-08.

Reachable (used):

- SnackVideo Help Center root: https://www.snackvideo.com/support
- SnackVideo Help Center — Video category (privacy settings, review of uploaded videos, views guidance referencing filters/stickers, download, duet, delete, add music in editing page): https://www.snackvideo.com/support/video
- SnackVideo Help Center — Social category (follow/unfollow, removing followers, like/cancel like, daily like limit exists, recommendation steering per category, private messages/comments and violation restrictions, followers/traffic growth): https://www.snackvideo.com/support/social
- SnackVideo Help Center — Creator Center (Creator Tasks rewards; Partner Program = ads placed in videos with daily earnings visible in Creator Center; gradual quality-gated admission and exit): https://www.snackvideo.com/support/creator-center
- SnackVideo product page ("We are a place to record and share life stories"; "Record moments in life with fun props and easy editing"; "Share photos, videos, and messages to keep in touch"; "Stay connected with live streaming"; "Have equal opportunity to express their minds"; Ads Solutions): https://www.snackvideo.com/about (and root https://www.snackvideo.com)
- SnackVideo Help Center categories list (Live Streaming 11 questions; Rewards 13; Withdrawal 10; Payment 7; Phone Number Binding 5; Mini Games 3): https://www.snackvideo.com/support
- Snap "Content Guidelines for Recommendation Eligibility" (defines Recommended Content as content eligible for "algorithmic recommendation beyond the creator's friends or subscribers… for example, on Stories, Spotlight, or the Map"; stricter standards; moderation via technology and human review; enforcement incl. removing, limiting distribution, limiting promotion, age-gating; sensitive-content personalization; viewers "may see content without actively choosing to do so"): https://values.snap.com/policy/content-guidelines-recommendation-eligibility
- Snap Safety & Privacy hub (Snap self-description: "visual messaging app… opens directly to the camera, not a content feed… without the pressure to grow a following or compete for likes"; "We don't allow unvetted content to go viral"; Creator Monetization Policy exists): https://values.snap.com
- YouTube Official Blog (Shorts as a named creator surface; creators tag products "in their Shorts, long-form videos, and livestreams" under the Shopping Affiliate Program; "How to Get Started on YouTube Shorts" creator guidance exists): https://blog.youtube

Unreachable (limitation recorded, assertions degraded, no memory-fill):

- TikTok: support.tiktok.com (timeout ×2), newsroom.tiktok.com (timeout ×2). TikTok retained as representative product but contributes no direct evidence.
- YouTube operational docs: support.google.com/youtube (timeout ×2); youtube.com/howyoutubeworks product-features page (timeout). Only the official blog was reachable.
- Kuaishou (Chinese product) corporate site: JS shell, no readable content. SnackVideo stands in as the reachable Kuaishou-family pole.
- Snapchat: help.snapchat.com (transport error); values.snap.com Spotlight-specific guidelines URL guessed → 404 (the recommendation-eligibility page above was reached instead and covers Spotlight explicitly).

## Product Observations

### SnackVideo (Kuaishou family) — evidence layer A unless noted

- Positioning: "a place to record and share life stories"; "Have equal opportunity to express their minds, share their stories"; "Discover and watch exciting videos you like". The "equal opportunity" framing is the Kuaishou-family philosophy: distribution aims to give ordinary creators reach, not only established ones.
- Creation loop: "Record moments in life with fun props and easy editing". Help center documents an editing page reached at publish time with a **Music** button ("click the third button [Music] in the lower left corner of the [video editing] page") — sound added from inside the product at editing time; a "My video has no views" article advises using "filters, stickers, and other features on SnackVideo when publishing high-quality videos" — in-app editing tooling is tied to visibility advice.
- **Duet**: documented ("Choose the videos you want shoot with others… click 'Duet'") — remixing-with-others is a first-class creation format.
- Publication: per-video privacy settings ("Share button → Privacy Settings" → private or public); published videos deletable; downloadable.
- Review gate: "we will review the uploaded videos according to our community rules. If…" — uploaded videos are reviewed against community rules before being visible (pre-visibility review documented for this product).
- Circulation: main page has category/search-based browsing and a recommendation feed; a user can "increase or decrease video recommendations in a certain category" — the recommendation stream is steerable per category. Distribution is discovery-first with a follow layer.
- Social layer: profile page with Follow button; follow/unfollow; follower lists; removing followers; likes (heart, cancellable); daily like-limit exists (number not recorded — precision rule); comments; private messages; violating rules in private messages leads to reported/restricted messaging or commenting.
- Monetization/creator machinery: Creator Center with **Creator Tasks** (earn rewards by completing assessments) and **Partner Program** ("users earn money by randomly placing ads in the videos you create"; daily earnings visible in Creator Center; "gradually opened for high-quality creators"; exit notifications with re-join rules). Help center also has large categories for Rewards (13), Withdrawal (10), Payment (7), Referral (3) — a full user-side value/earnings economy beyond creator ads.
- Bundled surfaces: **Live Streaming** (11-question help category; product page: "Stay connected with live streaming… Watch live streaming anytime anywhere"); private messaging ("Share photos, videos, and messages to keep in touch"); **Mini Games** (help category).
- Identity substrate: **Phone Number Binding** is a dedicated help category (5 questions) — phone-anchored account identity.

### Snapchat Spotlight — evidence layer A

- Host-product situation: Snap's own policy copy states "Snapchat is primarily a visual messaging app built to help people communicate with their family and friends. But there are parts of the app where public content may reach a wider audience via algorithmic recommendations; such content is defined as Recommended Content." Examples given: Stories tab (recommended content from professional media partners and popular creators), **Spotlight** ("Snapchatters can watch content created and submitted by our community"), and the Map.
- **The recommendation-vs-ties boundary is explicit**: recommendation eligibility applies to "algorithmic recommendation **beyond the creator's friends or subscribers**". This is official documentation of the structural seam between social distribution (friends/subscribers) and public discovery circulation.
- Eligibility regime: content must meet "additional, stricter standards" than the base Community Guidelines to be recommended publicly. Moderation via "a blend of technology and human review"; in-app reporting; enforcement includes "removing, limiting distribution, suspending, limiting promotion or age-gating your content."
- Feed consumption posture: "Recognizing that many Snapchatters may see content without actively choosing to do so…" — the recommended feed is a surface where the viewer encounters content they did not select. "Sensitive" content may be recommended with personalization restrictions by age, location, preferences.
- Company posture: "Opens to a Camera, Not a Feed of Content… without the pressure to grow a following or compete for likes" — the messaging-first host positions the public recommendation surface as an annex, not the core identity. Safety hub: "We don't allow unvetted content to go viral" (review-before-amplification posture).
- Monetization: a **Creator Monetization Policy** exists ("Content must adhere to the policies to be eligible for monetization") — monetization is eligibility-gated here too.

### YouTube Shorts — evidence layer A (thin), limitation noted

- Shorts exists as a named, first-class creator surface in the YouTube family. Official blog copy: creators "tag Amazon products in their **Shorts, long-form videos, and livestreams**" — Shorts is one of three parallel creator content formats in the same platform, with its own monetization path (shopping affiliate tagging; eligibility documented in the support ecosystem).
- The blog also lists creator guidance for getting started on Shorts.
- Operational detail (creation tools, feed mechanics, monetization thresholds) was **not reachable** this pass: support.google.com timed out ×2. Assertions about Shorts are kept structural and minimal; nothing precise is claimed.

### TikTok — no direct evidence (limitation)

- Both official surfaces timed out twice. TikTok is retained as the category's pure-play archetype and market anchor. Per the sourcing rules, no operational claim in this research rests on TikTok. The canonical model below is built from the three reachable poles and is expected to cover TikTok; this expectation is recorded as an uncertainty, not a fact.

## Cross-product Comparison

| Dimension | SnackVideo (Kuaishou family) | Snapchat Spotlight | YouTube Shorts | TikTok (no direct evidence) |
|---|---|---|---|---|
| Unit of publication | short video post on a personal profile, privacy-settable | submitted public video content eligible for Spotlight | named short-video format alongside long-form uploads | — |
| Primary consumption surface | recommendation feed + category/search browsing; follow layer | full-feed algorithmic recommendation ("may see content without actively choosing") | Shorts feed inside the YouTube app | — |
| Circulation beyond ties | yes — discovery feed is the front door; "equal opportunity" philosophy | yes — definitionally "beyond the creator's friends or subscribers" | yes — Shorts feed distributes beyond subscriptions | — |
| In-product creation | record + edit page (filters, stickers, music), duet | content "created and submitted by our community" (host opens to camera) | in-app Shorts creation (detail unreachable) | — |
| Sound/music as creation material | Music button in editing page (A) | not directly evidenced this pass | not directly evidenced this pass (market-common) | — |
| Remixing formats | Duet (A) | not directly evidenced | not directly evidenced | — |
| Follow graph | follow/unfollow, followers, remove follower (A) | "friends or subscribers" — subscriber concept explicit (A) | channel subscriptions (host-native) | — |
| Reactions/comments | like, comment, daily like limit, PMs (A) | report tools; reaction detail not fetched | (host-native) | — |
| Moderation posture | review of uploaded videos against community rules before visibility (A) | stricter recommendation-eligibility standards; tech + human review; age-gating; "unvetted content" not allowed to "go viral" (A) | host community guidelines (not fetched) | — |
| Creator monetization | Partner Program (in-video ads), Creator Tasks rewards, withdrawal/payment machinery (A) | Creator Monetization Policy, eligibility-gated (A) | Shorts monetization + shopping affiliate tagging (A, blog) | — |
| Bundled live streaming | yes, help category + product page (A) | (host has no live this pass evidenced) | livestreams as sibling format (A, blog) | — |
| Bundled private messaging | yes (A) | host core is messaging (A) | (host has DMs, not evidenced) | — |
| Reward/growth economies | Rewards/Referral/Withdrawal categories (A) | — | — | — |
| Identity substrate | phone-number binding category (A) | host Snapchat account (friends-graph) | host Google/YouTube account | — |
| Distribution philosophy | "equal opportunity" discovery + social layer (social-first heritage) | eligibility-gated public annex of a messaging app | annex of long-form creator platform | algorithm-first (market position, no evidence this pass) |

### Stability findings (evidence layer B unless noted)

Present across all reachable products (B, with A anchors listed):

- short video post bound to an identified creator (A: all three)
- a platform-assembled discovery/circulation surface reaching beyond the viewer's own ties (A: SnackVideo recommendation + steering; A: Snap's explicit "beyond friends or subscribers"; A: Shorts feed inside host app)
- in-product creation producing content for the same product's feed (A: all three)
- social participation: identifiable creators, an audience mechanism (followers/subscribers), reactions and comments or equivalents (A: SnackVideo explicit; A: Snap subscribers; A: YouTube channels)
- moderation/governance machinery on the public circulation surface, with eligibility rules stricter than private sharing rules (A: SnackVideo review-before-visibility; A: Snap recommendation-eligibility regime)
- creator-side surfaces: profile, audience metrics, monetization or reward machinery (A: SnackVideo Creator Center; A: Snap monetization policy; A: YouTube blog monetization formats)

Not universal (therefore not definitional; variant or vendor layers):

- licensed/commercial music library inside editing (A for SnackVideo; market-common for the archetype family but not evidenced across the whole reachable sample; historically absent in the Vine era)
- duet-style remixing (A: SnackVideo only this pass)
- live streaming, private messaging, mini games, reward/referral economies (A: SnackVideo; absent or unevidenced elsewhere — bundling, not Type)
- pre-publication review (SnackVideo) vs eligibility-gating at recommendation time (Snap) vs host-level moderation (YouTube, not fetched) — the review posture varies; governance existence is common, its position in the lifecycle is a variant
- duration ceilings, format norms (vertical vs square), identity substrate (phone vs host account)

## Canonical Model

### Level 0 — Defining Invariant (minimal)

Four jointly-held structures:

1. **The short video post as the unit of publication** — a persistent, self-contained brief video published under an identified creator's profile and retained as that creator's content record. Other media (captions, sounds, effects) attach to it; it is video-shaped, not text-shaped or photo-shaped.
2. **Public circulation through a discovery surface beyond the viewer's ties** — the platform assembles a continuously consumed feed from the platform-wide pool of short videos, surfacing content the viewer did not explicitly follow or select (by algorithmic recommendation, trending, or editorial channels). Distribution is not confined to the creator's own audience; creators become discoverable by strangers.
3. **The in-product creation loop** — capture and editing tools native to the product produce the videos for the same product's feed. Production and consumption are two ends of one loop inside one product.
4. **The social participation loop** — viewers act on videos and creators (react, comment, share, follow/subscribe); interaction attaches to videos and accumulates on creator profiles and feeds back into circulation signals.

Jointly-held load-bearing:

- 1 alone → video hosting/gallery application
- 2 alone → personalized content feed / content aggregator territory (no creation, no social layer)
- 3 alone → camera/video editor territory (no circulation, no social)
- 4 alone → generic social features without a content-type center
- 1+2 without 3 → consumption-only short-video portal (aggregator-like; the production culture that defines the Type is missing)
- 1+3 without 2 → profile-feed video sharing without public circulation (drifts toward photo-centric/general SNS shape)
- 2+3 without 4 → anonymous content feed, not a social platform
- 1+4 without 2 → a general/personal social network that happens to carry videos

### Level 1 — Common Mature Structure

Standard capabilities of mature modern products (cross-product commonality; not definitional):

- sound/music as creation material: sound library and sound reuse in the editing page (A-evidenced in one sample; market-common in the archetype family)
- remixing formats (duet-style creation on top of another's video) (A: one sample)
- follow/subscribe audience graph with follower management (A: all reachable)
- engagement/visibility metrics as creator-facing feedback (views advice, earnings dashboards) (A: SnackVideo; B)
- user-steerable recommendation controls (category up/down weighting) (A: SnackVideo; B)
- moderation + community governance on the public surface, including reporting (A: two samples)
- creator monetization machinery (ad revenue share, creator programs, eligibility-gated monetization) (A: all three reachable)
- profile as the creator's video archive and audience hub (A/B)

### Level 2 — Variant / Optional Structure

- Distribution philosophy: algorithmic-first single-feed (archetype pole) vs social/discovery blend with "equal opportunity" framing (regional pole) vs eligibility-gated public annex inside a messaging app vs annexed shelf inside a long-form platform
- Review posture: pre-visibility review of uploads vs recommendation-time eligibility gating vs host-level moderation (varies by product)
- Identity substrate: phone-number binding vs host-platform account (messaging account, Google account)
- Sound-library depth and licensing model
- Duration ceilings and format norms (vary by product and era; no precise limits asserted)
- Bundled adjacent surfaces: live streaming, private messaging, mini games, rewards/referral economies, shopping/affiliate, map/location surfaces
- Monetization models: in-video ad share, creator funds/reward tasks, gifting, shopping affiliate tagging

### Level 3 — Vendor-specific (kept here, not in the final document)

- SnackVideo: "Partner Program" (ads randomly placed in videos, daily earnings in Creator Center, quality-gated gradual admission), "Creator Tasks", Rewards/Withdrawal/Payment/Referral categories, Mini Games, Phone Number Binding category, "fun props" framing
- Snapchat: "Spotlight", "Recommended Content" definition, Stories tab and Map as sibling recommendation surfaces, "Sensitive" content personalization classes, "don't allow unvetted content to go viral" posture, camera-first company identity
- YouTube: "Shorts" naming inside channel/Studio architecture; Shopping Affiliate tagging across Shorts/long-form/livestreams; YouTube Partner Program ecosystem
- TikTok: "For You" feed naming and the full algorithm-first feature set (unreachable this pass — no detail asserted)

## Rejected Findings (anti-overfitting)

- **"Algorithmic recommendation feed" is NOT definitional.** Vine (2013–2016) is universally recognized as the origin archetype of this Type and circulated short videos through follow feeds plus editorial Explore/Popular channels, years before the modern recommendation feed. The invariant is public circulation beyond ties; the mechanism (algorithmic, trending, editorial) is a variant. The modern algorithmic feed is the dominant implementation, not the definition.
- **Vertical video is NOT definitional.** The Vine-era archetype was square; regional products have shipped mixed orientations. Vertical is the current dominant format norm.
- **A licensed in-app music library is NOT definitional.** Sound-as-creation-material is market-defining for the modern era but the Vine-era core had no licensed library; treat as common mature structure.
- **Precise duration limits are NOT definitional.** Duration ceilings vary by product and have repeatedly changed within single products. The invariant is "brief, self-contained videos sized for rapid in-feed consumption"; numbers stay in product documentation, not the Type definition.
- **Monetization is NOT definitional.** All reachable products operate monetization machinery, but a short-video social platform without monetization (the early archetype generation) is still fully in-type.
- **Phone-number identity is NOT definitional** (same anti-overfit as the IM pass): identity substrate varies by host product (phone binding, messaging account, Google account, username).
- **Live streaming / private messaging / mini games / rewards are NOT definitional** — bundled adjacent surfaces at particular products.
- **A standalone app is NOT definitional** — two of the sampled products are surfaces annexed into larger platforms.

## Boundary Findings

| Neighboring Type | Relationship | Distinction (and the removal test) |
|---|---|---|
| General Social Network | family sibling (§01.05) | General SNS organizes around the person and untyped posts; here the video-shaped unit, the video-shaped consumption loop, and in-product video creation organize everything. Untype the post and generalize the feed → general SNS. |
| Photo-centric Social Network | family sibling, nearest content-type neighbor | Same content-type-key logic, different key: photo post vs short video post; photo-centric streams draw from ties and/or discovery while the defining short-video circulation surface reaches beyond ties by design. Re-key video→photo → photo-centric SNS. Instagram-class products (photo-centric networks shipping a Reels-style annex) are the straddling poles — assign by center of gravity. |
| Interest-based Social Network | family sibling, watch-item | Modern short-video platforms rank by an implicit, behavioral interest graph. Distinction: there is no declared interest/topic container organizing membership; the interest signal is a ranking input inside a video-keyed loop, not the organizing key. A product whose whole membership is organized around declared interest topics belongs to the sibling. Flagged for joint review (see below). |
| Microblogging Platform | family sibling | Text-unit key with broadcast-subscription tie semantics consumed in a merged stream; media rides on posts. Here the media (video) IS the post and the loop is watch→react→create. |
| Video Streaming Platform | adjacent family (long-form) | Catalog/series/lean-back consumption of long-form content, click-to-choose navigation. The Shorts annex inside such a platform is the documented seam: same host carries both loops; the Type here is the short-video loop, assigned by center of gravity. |
| Social Live Streaming Platform | adjacent | Live real-time broadcast as the primary unit vs persistent recorded short-video posts. Live streaming is commonly bundled inside short-video platforms (A-evidenced) but the recorded-feed loop is this Type's center. |
| Personalized Content Feed | machinery overlap | Per-user selection machinery overlaps, but that Type has no creation loop, no social participation, and no member-published short-video requirement. Remove creation+social from this Type → personalized content feed. |
| Video Editor | creation-side neighbor | Dedicated editing depth without circulation or a social loop. The short-video platform's creation tools are deliberately lightweight and feed-optimized. |
| Music Streaming Platform | sound-economy overlap | Music as consumable catalog (listener licenses tracks) vs sound as creation material inside videos. Bundled licensed sound libraries must not be confused with the streaming Type. |
| Instant Messaging / private messaging | capability overlap | Private messaging exists inside several sampled products (A) but is secondary; conversation threads are not the organizing unit here. |

**Removal test summary**: remove the video-shaped unit → general/photo SNS or microblogging; remove public beyond-ties circulation → profile-feed social app or consumption portal; remove in-product creation → personalized content feed/streaming annex; remove social participation → anonymous feed service. Remove any two and the product is clearly some other Type.

**Family discriminator ratification**: this pass **ratifies** the §01.05 family framework (organizing key of the core consumption/distribution loop) and confirms the leaf as the **short-video content-type-keyed** member, with one refinement: the defining consumption loop is not merely video-shaped but **discovery-circulation-shaped** — public distribution beyond the creator's own audience is what historically (Vine) and structurally (Snap's own eligibility boundary) separates this Type from the tie-graph social networks. Products where video exists but circulation is tie-confined belong to the general/photo siblings.

**Joint-review flag for interest-based-social-network**: modern archetype products' ranking is behaviorally interest-keyed; if that sibling's L0 turns out to hinge on implicit behavioral interest rather than declared interests/topics, a consolidation review is warranted. This pass holds the seam at: declared interest containers = sibling; implicit behavioral ranking inside a video-keyed creation-consumption loop = this Type.

## Uncertainties

- TikTok contributed no direct evidence (all official surfaces unreachable). The canonical model is derived from three poles; TikTok is assumed to satisfy it (market consensus) but nothing TikTok-specific is asserted.
- YouTube Shorts operational mechanics (creation tool depth, feed mechanics, monetization thresholds) unreached; only its structural role as an annexed creator surface is evidenced (official blog).
- Snapchat Spotlight's creation tooling detail (in-app capture/edit for Spotlight specifically) was not directly documented in the fetched pages; "content created and submitted by our community" evidences the loop without tool detail.
- Kuaishou proper (Chinese product) was not directly documented; SnackVideo stands in for the Kuaishou-family philosophy. Chinese-market features (e.g., e-commerce integration) are not asserted.
- Whether historical Vine/Musical.ly satisfy the final L0 was checked conceptually against well-known product structure, not against fetched primary sources (those products are discontinued; vendor documentation is gone). The historical check is therefore marked conceptual.
- The exact position of review/moderation in the upload lifecycle varies and was only directly evidenced at two products with different postures; the final document states governance existence, not lifecycle position.

## Final Synthesis

A Short-form Video Social Platform is a social platform whose unit of publication is the brief, self-contained video post under an identified creator; whose defining consumption surface is a platform-assembled discovery feed circulating videos beyond the viewer's own ties; whose production happens with the product's own lightweight capture-and-edit tools feeding the same pool; and whose social loop (reactions, comments, shares, follows) attaches to videos and accumulates on creators. The algorithmic recommendation feed is the dominant modern implementation of the discovery surface, not the definition; vertical format, sound libraries, remix formats, monetization, live streaming, messaging, and rewards economies are standard or optional capabilities; and the Type's boundary is content-type + circulation-keyed: tie-graph video sharing is the general/photo sibling's territory, long-form catalogs are streaming territory, and selection-without-creation-or-social is the personalized-feed territory.
