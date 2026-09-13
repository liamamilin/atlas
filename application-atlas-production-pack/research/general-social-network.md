# Research Notes — General Social Network

## Research Goal

Understand the canonical structure of the General Social Network Application Type: what objects its world consists of, how the personal connection graph works, how user-published content is distributed and consumed, what rules govern visibility and connection, and where the boundary lies with the sibling Types that §01.05 of the directory already separates (Professional Social Network, Microblogging Platform, Photo-centric Social Network, Short-form Video Social Platform, Interest-based Social Network, Neighborhood Social Network, Friend Discovery Application, Social Profile Network) and with adjacent Types (IM, Forum/Community, Dating, Live Social).

## Initial Boundary (pre-research hypothesis)

- Core hypothesis: profile + personal connection graph + user-published general-purpose updates + a consumption surface structured by that graph.
- Likely confusions: microblogging (public broadcast), interest-based networks (topic-keyed), friend discovery (stranger formation), social profile network (profile/directory without a shared stream), IM (private conversation).
- Unknowns: whether the aggregated feed is definitional or a common mature structure; whether symmetric friendship vs asymmetric follow is definitional; whether groups/pages/events belong to the Type.

## Research Questions

1. What are the core objects (profile, connection, post/update, feed)?
2. How do connections form (mutual confirmation vs one-way follow) and what do they control (visibility, distribution)?
3. Is the aggregated feed definitional, or common mature structure? What did the pre-feed generation look like?
4. What content forms do updates take?
5. What interaction machinery exists (react/comment/share) and is any of it definitional?
6. How do identity/registration, audience/privacy controls, and moderation behave?
7. Where is the boundary with each sibling Type — what, removed, turns this product into that Type?
8. How do person-adjacent containers (groups, pages/organizations, events) relate to the person-centered core?

## Representative Products

Selection logic: market representation + documentation accessibility + different product philosophies + different eras/regions.

| Product | Role in sample | Philosophy / era |
|---|---|---|
| Facebook | canonical general social network; the Type's center of gravity | unrestricted personal-life sharing at maximal scale; super-app surface (evidence LIMITED — see Sources) |
| VK | regional general social network (Russia/CIS), living product with reachable official support taxonomy | general SNS core bundled into a super-app |
| MySpace | historical #1 general social network (mid-2000s), living remnant | profile-centric, customization-era; today music-content-forward |
| Mixi | regional (Japan) historical general SNS | SNS now behind login; corporate parent diversified |

Historical/breadth check candidates (not directly verifiable this pass): Friendster, Orkut, Google+, Renren/QZone.

## Sources

Fetched 2026-09-07:

- VK Support portal — https://vk.com/support — REACHABLE. Full user-help taxonomy observed (see Product observations). Article bodies login-walled; dev.vk.com API docs are a JS shell (unreachable).
- MySpace — https://myspace.com/ — REACHABLE. Live product surface observed. /help timed out once (not retried).
- MIXI corporate site — https://mixi.co.jp/ — REACHABLE. Company-level positioning only; mixi.co.jp/service/ 404. The SNS product itself (mixi.jp) not examined.

Unreachable (limitations recorded; per evidence rules no precise claims drawn from memory for these):

- Facebook — facebook.com/help (transport error), help article URL (transport error), facebook.com/legal/terms (transport error) → abandoned after 3 attempts. No operational documentation observed for Facebook this pass.
- Wikipedia (Tier-3 fallback for dead products Friendster/Orkut/Google+) — timeouts ×2 → abandoned. Historical samples therefore NOT verified against any source this pass.
- help.instagram.com — timeout → photo-centric boundary evidence limited to positioning level.
- VK support article bodies, VK dev docs, mixi.jp service pages — login/JS walls.

Consequence: the direct observational base is narrower than ideal for a Type this large. All final-document claims are kept at conceptual level; no precise numbers, defaults, or feature lists attributable to unreachable products appear.

## Product A — VK (direct observation, evidence layer A)

Official support portal taxonomy (vk.com/support, fetched 2026-09-07). The user-help tree is organized as:

- **Profile management** — profile-oriented questions (observed section title; article bodies login-walled)
- **News** — feed questions ("News" section; article titles reference the news feed surface)
- **Friends** — friend-oriented questions
- **Communities** + **Communities for managers** — group/community surfaces with a distinct manager-facing track
- Separate super-app product surfaces, each with its own help tree: VK Messenger, Calls, VK Dating, VK Pay, VK Music, VK Clips, VK Video, VK Video Live, VK Donut (creator subscriptions), Gifts and stickers, Games, VK votes, VK ID (account system), Tickets, business/advertising surfaces.

Observations:

1. The general-SNS core is exactly four user-facing sections: Profile / News (feed) / Friends / Communities. This is direct evidence for the person-centered core structure (profile + graph + feed) with communities as a person-adjacent container layer.
2. Everything that is NOT the general-SNS core (messaging, calls, payments, music, short video, dating, live) is packaged as separate product surfaces with separate help trees — direct evidence that the SNS core remains structurally distinct from the super-app bundle wrapped around it, and direct evidence for the super-app bundling variant.
3. VK ID as a separate account-system section shows identity/account machinery as a distinct layer under the SNS.
4. Evidence layer: A (directly observed) for the taxonomy itself; the article contents were not accessible, so no operational detail (limits, defaults, workflows) is claimed.

## Product B — MySpace (direct observation of the live remnant, evidence layer A)

myspace.com root (fetched 2026-09-07):

1. The site today is a music-culture content site, but the social-network skeleton is still visible and reachable: profiles typed by role ("Member", "Musician", "Artist, Actor", "DJ / Producer", ...), a sign-up framing "Date, Network, and Connect with People", and a Discover section with a "People" tab alongside Featured/Music/Videos.
2. Profiles remain the atom: every listed user (member or musician) resolves to a profile URL (myspace.com/<handle>).
3. Role-typed profiles (Musician vs Member) are a directly observed variant: the profile distinguishes person vs public-figure/creator classes — consistent with the person-adjacent "page" concept inside a general SNS.
4. Evidence layer: A for the current surface; nothing operational about friends/feed mechanics was reachable this pass.

## Product C — Mixi (corporate positioning only, evidence layer A-limited)

mixi.co.jp (fetched 2026-09-07): the corporate parent is now diversified (games, sports, the FamilyAlbum photo-sharing service); the mixi SNS itself was not documentable (service pages 404/login). The company's consumer portfolio still includes person-to-person sharing products (FamilyAlbum: family/friend-scoped photo sharing with comments/reactions), evidencing the regional lineage but NOT usable as operational evidence for the mixi SNS. Evidence layer: A for corporate positioning only.

## Product D — Facebook (no direct observation this pass)

All official documentation attempts failed (see Sources). Facebook is retained as the canonical representative product because the market position is uncontested and the Type name describes exactly this product family; but per evidence rules, NOTHING precise about Facebook's current features, defaults, or limits is asserted anywhere in the research or the final document. The final document's model stands on the observed samples (VK, MySpace) plus cross-era conceptual reasoning.

## Historical / regional breadth check (§24 check)

Question: would older, regional, platform-native products still fit the definition?

- The pre-feed generation (Friendster-class, mid-2000s profile-centric networks): consumption centered on visiting connections' profiles; the aggregated feed arrived later. **Not verifiable via sources this pass** (Wikipedia unreachable) — recorded as an uncertainty. Consequence applied anyway: the defining core is written so that a feed is NOT required ("surfaced to connected users" covers profile-browsing consumption). If the pre-feed generation actually lacked a user-published update stream (pure directory+testimonials), the L0 would still hold for the modern Type but the historical claim would need revision.
- Regional products: VK (observed) fits the core (profile/news/friends) wrapped in a super-app. Mixi (not directly examined) — treated as lineage evidence only.
- MySpace today (observed) retains profile + people connection framing — fits the core; its content-type drift toward music media is a business-model drift, not a structure change.
- Platform-native case (e.g., a social layer inside a device ecosystem) was not sampled this pass; the definition is written identity-substrate-neutral (email/username/phone/platform account all satisfy).

## Cross-product Comparison

| Dimension | VK (observed) | MySpace (observed) | Facebook (not observed) | Mixi (not examined) |
|---|---|---|---|---|
| Personal profile | yes — "Profile management" section | yes — role-typed profiles are the site's atom | canonical (not verified) | lineage evidence only |
| Personal connection concept | yes — "Friends" section | yes — "Connect with People" framing | canonical (not verified) | — |
| Feed as named surface | yes — "News" section | not observed today | canonical (not verified) | — |
| Communities/groups as containers | yes — dedicated + manager sections | not observed today | canonical (not verified) | — |
| Super-app bundling | extreme (messenger/calls/pay/music/dating/clips/live all separate surfaces) | drifted to music media | (not verified) | (not examined) |
| Identity/account layer | VK ID as separate machinery | handle-based profiles | (not verified) | (not examined) |

Cross-product commonalities (evidence layer B where ≥2 observed, C where inferred):

1. **Profile as the atom** — A×2 (VK, MySpace), C for the rest.
2. **A personal connection concept as a first-class section/feature** — A×2 (VK Friends, MySpace Connect-with-People).
3. **A named feed/news surface as primary consumption** — A×1 (VK News only). Kept at L1 (common mature structure), not L0 — also motivated by the pre-feed historical check.
4. **Communities/groups as a person-adjacent container layer** — A×1 (VK). L1/L2.
5. **Super-app bundling around the SNS core** — A×1 (VK) + MySpace's content drift suggests the SNS core survives bundling; L2 variant.
6. **Audience/privacy controls, interactions (react/comment/share), notifications, people discovery, messaging surface** — C (conceptually necessary for the modern form; no precise claims made).

## Canonical Model (four layers)

### L0 — Defining Invariant (deliberately minimal)

```text
Personal Profile
  (persistent, self-authored representation of one person)
└── Personal Connection Graph
    (each user maintains their own links to other users;
     symmetric friend ties or asymmetric follow ties both satisfy)
    └── User-Published Update Stream
        (posts attributed to the author's profile, distributed
         along the graph to connected users' consumption surfaces)
```

Three structures. Removal tests:

- Remove the **profile** → anonymous content surface or topic forum; no personal identity home → not this Type.
- Remove the **personal connection graph as the primary distribution substrate** (content distributed by public topic or pure algorithmic discovery) → broadcast/microblogging or content-feed product → not this Type.
- Remove the **user-published update stream** (profiles + connections but nothing shared through them) → people directory / social profile network → not this Type.
- Remove **person-attribution** of updates → media/publication site → not this Type.

Note on the feed: the aggregated feed is the modern canonical FORM of "surfaced to connected users", but L0 does not require a feed UI — profile-browsing consumption (the pre-feed generation) satisfies the same invariant. The feed therefore sits at L1.

Note on symmetry: L0 is deliberately written graph-neutrally. What the tie MEANS is the sibling discriminator (see Boundary Findings), not whether it is bidirectional.

### L1 — Common Mature Structure

- **News feed** — aggregated, ordered stream of the graph's activity as the home surface; ordering philosophy varies (reverse-chronological vs engagement-ranked; some products offer both).
- **Interaction machinery** — reactions/likes, comments, shares/reposts attached to updates.
- **Audience / privacy controls** — per-post audience selection and standing visibility settings; the graph plus audience rules jointly determine reach.
- **People discovery** — search, suggestions (mutual-connection-driven "people you may know" class), invitations.
- **Notifications** — alerts for graph activity.
- **Profile components** — photos, about/biography fields, the accumulation of one's own posts on the profile (timeline/wall forms).
- **Content forms** — text, photos, video, links, life events; composition via a composer surface.
- **Direct messaging surface** — in-product 1:1/small-group messaging (in many modern products a separate app sharing the identity).
- **Person-adjacent containers** — groups/communities, pages/organizations, events: containers that exist beside the person-centered stream.
- **Account machinery** — registration, identity substrate (varies), age gates, block/report, multi-device clients.

### L2 — Variant / Optional Structure

- Connection semantics: symmetric friendship vs asymmetric follow vs both layered in one product.
- Audience posture: private-graph-first vs public-default.
- Feed ordering: chronological vs algorithmic vs user-selectable.
- Identity substrate: email, username, phone, platform account; real-name norms vs pseudonymity.
- Super-app bundling: messaging, payments, mini-apps/games, music, dating, short-video, live, creator subscriptions shipped inside the SNS container (VK observed extreme form).
- Profile customization depth (themes/layouts era vs standardized profiles).
- Regional norms (verified identity, age gating, moderation regimes).
- Monetization surfaces: ads, creator tools, marketplace/classifieds — business-model drift, not structure.
- Ephemeral formats (stories-class), live surfaces — adjacent Types shipped as capabilities.

### L3 — Vendor-specific (research notes only)

- VK: VK ID account system; VK Donut creator subscriptions; VK votes; gifts/stickers; the observed 20+ section super-app help taxonomy.
- MySpace: role-typed profiles (Member/Musician/...); music-content-forward remnant positioning.
- Facebook: News Feed/Pages/Groups branding, Marketplace, Reactions etc. — NOT verified this pass; deliberately excluded from all claims.
- Mixi: pre-transformation SNS features — not examined; excluded from all claims.

## Rejected Findings

- "A general social network requires an algorithmic ranked feed" — REJECTED as definitional: single-era pattern; chronological and profile-browsing forms satisfy the core (anti-overfitting rule; historical check).
- "Friendship must be mutual/confirmed" — REJECTED as definitional: follow-style asymmetric graphs are widespread in the family; symmetry is a variant axis.
- "Groups/Pages/Events are part of the definition" — REJECTED: person-adjacent containers are common but the observed core sections split them from profile/news/friends; removing them leaves the Type intact.
- "Messaging is part of the definition" — REJECTED: in-product messaging is a bundled surface (observed as a separate help tree in VK); the IM Type already exists as its own leaf.
- "Real-name/phone identity is definitional" — REJECTED: identity substrate varies across eras and regions.
- "General-purpose content means 'anything goes'" — REJECTED as phrasing: the Type's scope is defined by what it does NOT constrain (audience, content type, locality), not by an absence of rules; moderation and audience rules still apply.

## Boundary Findings

The organizing discriminator across the §01.05 family: **what the consumption/distribution substrate is organized around**.

| Neighbor Type | Relationship | Discriminator (what removed → becomes that Type) |
|---|---|---|
| Microblogging Platform | sharpest structural overlap | ties become public-content subscriptions (follow = subscribe to broadcasts), posts public-first, discovery-first consumption; remove the personal-acquaintance meaning of the graph → microblogging |
| Photo-centric Social Network | content-type sibling | content-type-first organization (photo objects primary); restrict the stream to one content class → photo-centric |
| Short-form Video Social Platform | content-type + discovery sibling | discovery/algorithm-first consumption with video-first creation → short-form |
| Professional Social Network | audience/context sibling | identity and sharing framed by career/professional semantics → professional |
| Neighborhood Social Network | locality sibling | membership gated by verified locality → neighborhood |
| Interest-based Social Network | organizing-key sibling | interests/topics, not the person graph, key the distribution → interest-based |
| Friend Discovery Application | formation-loop sibling (processed 2026-09-07) | forming NEW relationships with strangers is the primary job (discovery → contact formation); in this Type the graph starts from known people and discovery is auxiliary — the friend-discovery pass's own discriminators (friend-seeking profile + stranger-candidate discovery as primary) invert here |
| Social Profile Network | substrate sibling | remove the update stream → profiles + connections with no shared content loop → profile/directory network |
| Online Forum / Community Platform | container sibling (community-platform pass processed) | content organized by topic containers and threads rather than by who posted; community-operator container vs person-centered self-organizing graph |
| Instant Messaging Application | conversation sibling | private direct conversation vs shared attributed updates; messaging inside the SNS is a bundled capability, not the Type |
| Dating Application | intent sibling | romantic-partner intent + mediated contact gate vs unrestricted personal sharing |
| Social Live Streaming Platform | temporality sibling | ephemeral live broadcast with simultaneous viewers vs persistent attributed stream |

Boundary blur zones recorded honestly: modern general SNS products ship follow mechanics, public posts, stories, live, marketplace — each is a capability overlap, not a Type merge; the Type is assigned by what the product's core consumption loop is organized around.

## Uncertainties

1. Facebook operational documentation unreachable this pass — the canonical product contributes no direct evidence; all Facebook-specific detail excluded.
2. Pre-feed historical generation (Friendster-class) unverified — the claim that earliest-generation consumption was profile-browsing-based rests on general market history, not sources; the L0 is nevertheless written feed-neutral so the definition is robust either way.
3. VK article bodies (operational detail on friends/feed/privacy) login-walled — the VK evidence is structural (section taxonomy), not operational.
4. MySpace's current friends/feed mechanics not directly observed (root page only; /help timed out).
5. The exact balance between symmetric-friend and asymmetric-follow implementations in the current market was not measurable this pass — kept as a variant axis without prevalence claims.
6. Platform-native social layers (device-ecosystem social networks) not sampled.

## Final Synthesis

The General Social Network is the **person-centered sharing network**: each member owns a persistent profile representing them, maintains their own connections to other members (the personal graph), and publishes general-purpose updates attributed to their profile that are distributed along that graph to the people connected to them. Consumption surfaces (feed today, profile-browsing in earlier generations) are structured by that graph. The defining core is exactly three structures — profile, personal connection graph as the primary distribution substrate, attributed user-published update stream distributed along the graph. The feed, interactions, privacy controls, discovery, messaging, and person-adjacent containers (groups/pages/events) are common mature structure; bundling posture, connection semantics, audience posture, and identity substrate are variants. The Type is assigned by the organizing key of the core loop: the person and their self-curated graph — not a content type, an audience, a locality, an interest, or a stranger-formation loop.
