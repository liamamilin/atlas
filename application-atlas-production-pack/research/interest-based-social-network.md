# Research Notes — Interest-based Social Network

Research date: 2026-09-07

## Research Goal

Understand the canonical structure of the Interest-based Social Network Application Type: what objects its world consists of, how the interest domain organizes identity, content, and discovery, how the social graph works, and where the boundary lies with the sibling Types of §01.05 (General Social Network, Microblogging, Photo-centric, Short-form Video, Professional, Neighborhood, Friend Discovery, Social Profile Network), with the community family of §01.06 (Interest Community Platform, Online Forum, Community Platform, Q&A), and with adjacent content Types (Content Curation Platform, Review Platform, Personalized Content Feed).

This pass is a sibling pass under the family boundary framework recorded by the processed `general-social-network` pass: the proposed §01.05 family discriminator is **the organizing key of the core consumption/distribution loop** (person graph [general] vs content-type [photo/short-form] vs broadcast-subscription ties [microblogging] vs audience/context [professional] vs verified locality [neighborhood] vs **interest/topic [interest-based]**). This pass should ratify or refine that framework from the interest-based side.

## Initial Boundary

- Core hypothesis: a social network where membership, content, and discovery are organized around a shared interest domain (film, books, music, sport, crafts, art, ideas) rather than around a pre-existing personal acquaintance graph.
- Likely confusions: General Social Network (same family surfaces), Interest Community Platform (§01.06, container vs network), Content Curation Platform (curation without social ties), Review Platform (reviews without the network), Photo-centric SNS (Pinterest straddle), Friend Discovery Application (person-match vs content loop), Dating Community Platform (the dating-community-platform pass flagged Hornet-class straddles against this leaf, root-page evidence only, unresolved).
- Known prior signals from other passes: `friend-discovery-application` ("organizes around interest containers where relationships are a byproduct"), `community-chat-platform` ("primary surface is profile, feed, and follow graph around an interest; chat is secondary"), `product-discovery-application` ("social graph/content feed is the core; shopping is a surface — Pinterest, TikTok"), `dating-community-platform` (Hornet-class straddle, unresolved).

## Research Questions

1. What is the organizing key of the consumption/distribution loop — the person graph or the interest domain? What exactly does "interest-keyed" mean operationally?
2. What objects exist: member profile, domain-anchored content object (review / diary entry / activity / creation / save), catalog entity (book / film / route / pattern), collection (shelf / board / list / watchlist), tag/topic/genre, follow graph, feed, groups/clubs?
3. How does each product build discovery: catalog browse, tags, similarity/taste matching, algorithmic interest feeds, member browse?
4. What social ties exist (symmetric friend vs asymmetric follow), and what flows through them (activity streams)?
5. What interactions, rules, states, and moderation apply to domain content?
6. What monetization postures exist and do they change the core?
7. Where are the removal-test boundaries to every neighboring Type?
8. Does the definition survive older/regional products (historical/market-sample check)?

## Representative Products

Selected for market representativeness across interest domains, product philosophy, era, geography, and scale; operational-document accessibility was the binding constraint (see Sources).

Directly researched (evidence layer A):

1. **Letterboxd** — film; catalog-anchored diary/review network; indie-scale, global, follow-first philosophy. Official FAQ fetched (rich).
2. **Strava** — running/cycling/outdoor sport; activity-anchored network; subscription-funded, competition-flavored. Official help center fetched (rich).
3. **Douban** — books/film/music; multi-domain interest network, China, founded 2005 — serves as the regional + historical sample. Official "About" page fetched (structural + philosophy; not operational help docs).
4. **Ravelry** — knitting/crochet/fiber arts; craft community-network hybrid, founded 2007. Official root positioning line only ("a free website for knitters, crocheters, and fiber artists"); help content login-walled. Thin evidence, used only for positioning and scope.

Market anchors commonly cited for this Type but **not directly researched** this pass (official surfaces unreachable — see Source-access Limitation): Pinterest, Goodreads, DeviantArt, Last.fm, Behance. None of their operational details are used as evidence anywhere in these notes; they are named only as market context and flagged as an uncertainty.

## Sources

Tier 1 (fetched successfully, 2026-09-07):

- Letterboxd — About / Frequent questions (official FAQ): https://letterboxd.com/about/ (includes /about/faq/ content). Rich: product definition, diary/watched/logging semantics, ratings/likes/tags, lists/watchlist, follow semantics ("works like X/Twitter"), activity timeline, blocking, community policy, privacy modes, TMDB film data, Pro/Patron subscriptions, Video Store.
- Strava — Help Center root: https://support.strava.com/hc/en-us (collection taxonomy: About Strava; Recording and Uploading Activities; Setting Up Your Account; Profile Customization; Stats and Metrics; Your Feed and Community; Maps; Glossaries). Rich structural evidence.
- Strava — About Strava article: https://support.strava.com/en-us/articles/15402118-about-strava ("community of athletes", "social fitness").
- Strava — Following Athletes on Strava: https://support.strava.com/en-us/articles/15402056-following-athletes-on-strava (follow = subscribe to activities; activity feed; favorites; mute; per-athlete notifications; privacy controls everyone/followers/just you).
- Douban — 关于豆瓣 (About Douban): https://www.douban.com/about (philosophy: find like-minded people through the things you love; no editors; member-produced content/classification/ordering; tags enter site-wide tag classification; review "useful" votes raise ranking; member pages with collections/reviews called the most important content; site structure: 读书/电影/音乐/播客/同城/小组/发现/话题广场). Structural + philosophy evidence; operational help (help.douban.com) not fetched.
- Ravelry — root page: https://www.ravelry.com/help → "Ravelry is a free website for knitters, crocheters, and fiber artists." Positioning only.

Unreachable / abandoned per network rules (1–2 fetch failures each):

- Pinterest — help.pinterest.com/en/guide/all-about-pinterest (timeout), www.pinterest.com (timeout).
- Goodreads — goodreads.com/about/how_it_works (timeout), www.goodreads.com (timeout).
- DeviantArt — deviantart.com/about (timeout), welcome.deviantart.com (timeout).
- Last.fm — last.fm/about (HTTP 403).
- Behance — help.behance.net/hc/en-us (timeout); (no further attempts per network rule).

## Product Observations

### Letterboxd (evidence: A — official FAQ, rich)

Key observations:

- Self-definition: "a global social network for grass-roots film discussion and discovery"; "described as like Goodreads for movies".
- **Interest domain**: film. **Identity**: member profile showcasing favorites; username-based; profile = the member's film record (watched, diary, ratings, reviews, lists, likes).
- **Content object**: the diary entry / review / rating, always **bound to a film entity**; distinct "marked watched" vs "logged (dated diary entry)" states; logging builds "the Recent Activity section of your Profile". Reviews have editing/deletion; old revisions not stored. Tags attach to diary entries/reviews/lists (personal taxonomies, e.g. `with:mom` nested tags).
- **Interest structures for discovery**: film pages (catalog entities, data sourced from TMDB), genres, "Similar Films" with "themes and nanogenres", member-curated lists on any topic, tag aggregation (own/friends'/community-wide), an interest-based film page ("films you haven't seen, based on your watched and liked films"), advanced search triggers (film:, member:, cast:), Official Lists, Showdown topics.
- **Social graph**: follow is asymmetric, explicitly "works like X/Twitter"; followed members appear in the Activity timeline; members are colloquially "friends"; discovery of members via the Members section, review pages, followers pages, or X/Twitter & Facebook connection; no private accounts (blocking hides content one-way).
- **Feed**: Activity timeline aggregates followed members' logs, reviews, likes, comments, list publications; back-dated diary entries are throttled (max one item per hour) to avoid saturating followers' feeds.
- **Collections**: watchlist (single toggle, auto-removal on watch) and unlimited curated lists (public/private, ranked or not, drafting before publication); no list collaboration (crew-maintained exception).
- **Interactions**: rate, like, comment (owner-controlled comment gates: anyone / people-you-follow / none, per-thread override), tag.
- **Rules/states**: community policy with zero-tolerance moderation (hate speech), report + block machinery, review removal with recourse; no reviews of unwatched content ("not for reviews of films you want to see"); spoiler flags; privacy mode per diary entry (public / close friends / private) — private/close-friends ratings excluded from stats; drafts.
- **Monetization**: Pro/Patron subscriptions (ad-free, stats pages, filters, cloning, custom posters), Video Store (curated digital rentals since Dec 2025).
- **Product-specific (L3)**: TMDB/Posteritati poster sourcing; per-film custom poster modes (Any/Theirs/Yours/None); "Stan Lee Rule" (cameo credits excluded from most-watched stats); Year in Review requires ≥10 diary entries/year; 30-day deleted-content retention in export bundles; username cooling-off after change; list title limit 256 chars; boxd.it short URLs; RSS/IFTTT auto-publish; film-vs-diary count semantics; patron HQ accounts.

### Strava (evidence: A — official help center, rich)

Key observations:

- Self-definition: "a community of athletes from all over the world… what we call social fitness — connecting and competing with each other via mobile and online apps."
- **Interest domain**: athletic activity (many supported sport types). **Identity**: athlete profile (display name, bio, photo, displayed team, stats; Year in Sport recap).
- **Content object**: the **recorded activity** (uploaded from app/GPS devices/manual entry/file upload; editable afterwards; gear attached; route files). The activity is the domain-native artifact — the post is the workout.
- **Interest structures for discovery**: supported sport types; segments (competed course constructs — Live Segments integration evidenced), routes, maps/map layers, clubs (club joins appear in feed), training glossaries, stats/metrics semantics.
- **Social graph**: "Following athletes is a way to subscribe to other athletes' activities"; following shows their activities, challenge progress, and created routes in the activity feed; favorites (star) pin an athlete's new activities to the top of the feed; muting hides without unfollowing (app-only); follower lists visible; managing followers + blocking.
- **Feed**: activity feed with ordering controls; per-athlete upload notifications; privacy controls per activity (everyone / followers / just you).
- **Interactions observed in help**: feed items, notifications, challenge progress; reporting content for community-standards violations; verified athlete badges.
- **Monetization**: freemium — "Is Strava free?" article exists; shop; partner integrations (device ecosystem, MCP connector listed under Connectivity); acquiring Runna (training-app acquisition).
- **Product-specific (L3)**: segments/leaderboard culture and Live Segments partner integrations; gear; Year in Sport; athlete intelligence; supported-language and country-availability articles; Pro badge; maps layers/glossary.

### Douban (evidence: A — official About page, structural/philosophical)

Key observations:

- **Interest domain**: cultural consumption — books, film, music (site sections 读书/电影/音乐/播客), plus city/local (同城) and groups (小组) and topic square (话题广场).
- Founding philosophy (verbatim paraphrase): the most effective recommendations come from people with similar tastes, but "the people with the most similar tastes are usually strangers"; Douban helps you **find like-minded people through the things you love, and then find more good things through them** — the interest-first inversion of the acquaintance graph, stated by the vendor itself.
- **No editors**: "all content, classification, filtering, and ordering here is produced and decided by members like you" — classification and ordering are member-produced.
- **Interest structures**: tagging a book makes it appear in the site-wide tag classification; a "useful" vote on a review raises its ranking; member pages (via name/avatar) holding collections and reviews are called "the most important and beneficial content".
- **Social**: member-to-member profile visiting encouraged; like-minded discovery through shared objects; groups (小组) exist as a major section (community straddle); follow/friend mechanics not directly observed in fetched text.
- **Historical**: © 2005–2026 — a 20-year-old regional (Chinese) implementation; satisfies the historical/market-sample check together with Letterboxd's "like Goodreads for movies" self-description (Goodreads itself founded 2007).

### Ravelry (evidence: A — root positioning line only, thin)

- "Ravelry is a free website for knitters, crocheters, and fiber artists." — scope = craft interest domain; free; invitation-style signup path visible (Sign Up → /invitations). All operational mechanics (projects, patterns, forums, groups) are login-walled and were **not observed**; nothing beyond positioning and scope is used as evidence. Market context only.

## Cross-product Comparison

| Dimension | Letterboxd | Strava | Douban | Ravelry |
|---|---|---|---|---|
| Interest domain | film | sport/athletic activity | books + film + music (+ groups/topics) | knitting/crochet/fiber arts |
| Profile meaning | member's film record (diary/ratings/favorites/lists) | athlete's activity record (stats/gear/recap) | member page of collections & reviews ("most important content") | member profile (unobserved detail) |
| Primary content object | diary entry / review / rating bound to a film entity | recorded activity (sport-native artifact) | review / collection bound to a book/movie/music entity; topic posts | (unobserved; craft projects per market context) |
| Content anchoring | required: every entry binds to a film | required: every post is an activity | strong: collections/reviews bind to catalog entities; topics free-form | (unobserved) |
| Discovery structures | film pages, genres, similar films, tags, lists, interest-filtered films, member browse | sport types, segments, routes, maps, clubs, challenges | site-wide tag classification, review rankings, explore, topic square | (unobserved) |
| Social tie | asymmetric follow ("works like X/Twitter") | follow = subscribe to athletes' activities | like-minded discovery through objects; visiting profiles; (tie mechanics unobserved) | (unobserved) |
| Feed | Activity timeline of follows; back-dating throttled | activity feed with ordering, favorites pinning, mute | member-produced ordering; explore surfaces | (unobserved) |
| Collections | lists + watchlist (public/private, ranked) | routes; (no generic collections observed) | collections attached to catalog entities | (unobserved) |
| Interactions | rate / like / comment (owner-gated) / tag | feed actions, notifications, challenge progress (kudos not directly observed in fetched docs) | "useful" votes on reviews | (unobserved) |
| Moderation | community policy, zero-tolerance removals, report + block | community standards, reporting, verified badges | 社区指导原则 community guideline link | (unobserved) |
| Monetization | Pro/Patron subscriptions; Video Store rentals | freemium subscription; shop | market section (豆品); premium tiers (context) | free |
| Era / region | 2011, global | 2009, global | 2005, China | 2007, global (niche) |

### Stable cross-product commonalities (evidence B where 2+ products)

1. Every product is organized around a **named interest domain** that bounds the content (film / sport / books-movies-music / fiber arts).
2. **Member profile = accumulated interest record** (what you watched/logged/made/c collected), not a personal-acquaintance representation.
3. **User-contributed content objects are anchored to the domain** — bound to domain objects (film, book, route) or produced as the domain's native artifact (an activity).
4. **Interest structures do the organizing/discovery work**: domain object pages, tags/classifications, collections, similarity, member-produced ordering and rankings.
5. **Person-to-person ties with activity streams exist** (follow/friends), though their primacy varies (Letterboxd follow-first; Douban browse-first; Strava follow-led feed but domain-bound content).
6. **Moderation + community standards + blocking/reporting** appear wherever content is open.
7. **A free core with optional paid tiers** (subscriptions/rentals/shop) appears in 3 of 4; monetization never changes the core loop.

### Cross-product differences (variants, not core)

- Catalog provision: site-maintained entity catalogs (film/book data partners) vs self-recorded artifacts (activities) vs user-generated objects.
- Discovery posture: follow-first vs browse/tag-first vs interest-similarity-first.
- Community-container depth: none (Letterboxd) vs clubs (Strava) vs groups + local + topics (Douban, Ravelry — straddling toward Interest Community Platform).
- Content typology: reviews/diary vs activities vs creations vs saves.

## Canonical Model — Four Abstraction Levels

### Level 0 — Defining Invariant (minimal; jointly-held)

```text
Shared Interest Domain
└── Member Identity as Interest Record (profile accumulating the member's domain engagement)
    └── Domain-anchored Content Objects (user-contributed content bound to the domain)
        └── Interest-keyed Discovery & Distribution (domain objects / tags / collections / similarity organize the loop)
            └── Person-to-person Social Ties (follow/friend) with persistent activity streams
```

- **Shared interest domain** — the whole network exists for one named interest area (or one coherent cluster of them). Remove → no Type; the domain is the boundary of the world.
- **Member identity as interest record** — the profile's persistent meaning is the member's accumulated engagement with the domain (their watching/reading/doing/making/taste). Remove → anonymous content site or people directory.
- **Domain-anchored content objects** — user contributions are bound to the interest (attached to the domain's objects — a film, a book, a route — or produced as the domain's native artifact — an activity, a project). Remove → content site with no member contribution, or (if content becomes untyped personal updates) the General Social Network.
- **Interest-keyed discovery & distribution** — content is surfaced through the domain's structures: object pages, tags/topics/classifications, member collections, similarity/taste matching, member-produced rankings — alongside follow streams. Remove interest-keying (only a personal graph distributes untyped updates) → General Social Network.
- **Person-to-person social ties with persistent activity streams** — members connect to (follow/friend) other members and their activity flows into durable streams. Remove → content catalog / curation / aggregation platform with no social network.

All five properties are jointly held. Historical check: Douban (2005, regional) satisfies the core on direct evidence; Letterboxd's own "like Goodreads for movies" analogy anchors the 2007 generation; the core is substrate-neutral (no assumption of phones, algorithms, or catalogs).

### Level 1 — Common Mature Structure

- Domain catalog entity pages where content aggregates (film pages, book pages; segments/routes as domain constructs in activity products)
- Member collections (boards / shelves / lists / watchlists) — curated, shareable, public-or-private sets
- Tags / genres / topics as user- or system-level classification members contribute to
- Ratings / reviews / reactions as content primitives; comment interactions with owner controls
- Activity feed combining followed people and interest items; notification machinery
- Interest-based recommendation / similarity surfaces (similar films, taste-like members, interest-filtered listings)
- Search over the domain (objects, members, content)
- Privacy controls over content visibility (public / followers / close circles / private) and per-entry granularity
- Moderation: community standards, reporting, blocking, review removal
- Mobile apps; profile stats / year-in-recap surfaces; challenges/goals (domain-flavored)
- Free core + paid tiers (ad-free, analytics, filters, custom presentation)

### Level 2 — Variant / Optional Structure

- Content typology: catalog-referenced entries (reviews/diary/logs) vs self-recorded artifacts (activities) vs user-created objects (artworks/projects) vs saves/collections of found content
- Catalog provision: platform-maintained entity database (data partners) vs member-produced objects vs no catalog
- Discovery posture: follow-first vs browse/tag-first vs algorithmic-interest-first
- Tie semantics: asymmetric follow vs symmetric friend (varies; not measured for prevalence this pass)
- Community-container depth: none vs clubs vs full groups/forums/events (straddle zone with Interest Community Platform §01.06)
- Multi-domain vs single-domain scope (one interest vs a cluster under one roof)
- Monetization packaging: subscriptions, rentals, shops, marketplaces, advertising
- Regional super-network packaging (interest network absorbing city/local, market, audio surfaces)
- Cross-posting / export surfaces (RSS, IFTTT-class automation, share to external networks)

### Level 3 — Vendor-specific (research notes only; not in final document)

- Letterboxd: custom poster modes (Any/Theirs/Yours/None), TMDB/Posteritati sourcing, "Stan Lee Rule", Year in Review ≥10-entry threshold, 30-day deleted-content bundle retention, username cooling-off, list title 256-char limit, boxd.it URLs, per-hour back-dated-activity feed throttling, Video Store rental "drops", HQ/crew-maintained list exception.
- Strava: segments/leaderboard constructs + Live Segments partner integrations, gear attachment, per-athlete notification opt-in, mute app-only restriction, favorites pinning, maps layers/glossary, athlete intelligence, MCP connector, Runna acquisition, supported-country articles.
- Douban: no-editors manifesto, review "useful"-vote ranking mechanics, site-wide tag classification entry, 小组 groups scale, 同城 city/local section, 豆品 market, FM/podcast surfaces.
- Ravelry: invitation-path signup, free positioning (mechanics unobserved).

## Rejected Findings

- "Interest-based SNS = visual pin-board products" — REJECTED: over-fit to one content typology; the sample spans diary/review, activity, and craft forms.
- "Reviews are definitional" — REJECTED: activity-anchored products have no reviews; the invariant is domain-anchored content, not the review form.
- "A platform-maintained catalog database is definitional" — REJECTED as L0: catalogs are the common realization of "domain objects" in catalog-anchored variants, but self-recorded/user-generated variants satisfy the Type without one.
- "Follow must be the primary distribution substrate" — REJECTED: Douban states the loop as object/taste-first; Letterboxd states follow-first; Strava is follow-led with domain-bound content. The invariant is that interest structures organize discovery, not that the follow graph leads.
- "Interest-based SNS is merely a niche General SNS" — REJECTED: the organizing key differs structurally (identity is an interest record; content is domain-anchored; discovery runs through domain structures), not just in topic breadth.
- "Private messaging is part of the Type" — REJECTED: not observed as definitional in any fetched documentation; messaging belongs to IM Types.

## Boundary Findings

The §01.05 family framework (from the general-social-network pass) is **ratified from this side with one refinement**: the discriminator "interests/topics key the distribution" holds, but operationally the stronger invariant is **domain-binding of identity and content** — distribution may be follow-led (activity products) while the Type still reads interest-based, because every post is a domain object and every profile is an interest record. Stated as the family test: *interests key the consumption/distribution loop, and the domain bounds what content and identity even are.*

Removal tests against neighbors:

| Neighbor Type | Relationship | Removal test (what removed → becomes that Type) |
|---|---|---|
| General Social Network (§01.05) | family sibling, sharpest | unbind content from the domain (untyped personal updates) and let the self-curated personal graph key distribution → General SNS |
| Microblogging Platform (§01.05) | tie-semantics sibling | ties become public broadcast subscriptions and posts become general/untyped → microblogging |
| Photo-centric SNS / Short-form Video (§01.05) | content-type siblings | the medium (photo/video) becomes the organizing key rather than the interest; visual-interest products straddle this seam |
| Professional SNS (§01.05) | audience sibling | career/professional context becomes the organizing key → professional |
| Neighborhood SNS (§01.05) | locality sibling | verified locality becomes the membership key → neighborhood |
| Friend Discovery Application (§01.05) | formation-loop sibling | forming new relationships becomes the primary loop (person-match); in this Type relationships are a byproduct of the content loop |
| Social Profile Network (§01.05) | substrate sibling | remove the content/loop → profiles + connections directory |
| Interest Community Platform (§01.05→§01.06 family) / Online Forum / Community Platform | container siblings | shared containers (groups/forums/events/threads) become the primary organizing structure and participation replaces the profile+stream loop → community Types; Douban/Ravelry-class products straddle |
| Content Curation Platform (§02.08) / Personalized Content Feed (§02.08) | capability siblings | remove member social ties and the network loop → curation/aggregation |
| Review Platform (§02.10) | object overlap | review-of-record for purchase decisions becomes the core product; network is absent → Review Platform |
| Q&A Community (§01.06) | container sibling | question/thread containers become primary → Q&A |
| Dating Application / Dating Community Platform (§01.07) | intent siblings | partner-discovery intent organizes the loop → dating Types; identity-niche interest networks straddle (see flag below) |
| Activity/fitness tracker tools (outside §01.05) | capability overlap | tracking without the network; in this Type the network is the Type and tracking is domain-native content generation |

Unresolved straddles for joint review:

1. **Hornet-class identity-niche networks** (flagged by the dating-community-platform pass, root-page evidence only): products organized around an identity-linked interest where the partner/community discovery weight is unclear. This pass adds no direct evidence; the seam test proposed is whether partner discovery or the interest content loop organizes the product.
2. **Pinterest-class visual-interest products**: interest-keyed (organizing key = the interest/idea) but visually object-heavy; assigned here by organizing key per the family framework, flagged for the photo-centric pass to ratify from that side.
3. **Douban/Ravelry-class community-heavy interest networks**: network core + major group/forum containers; kept in this Type by center of gravity (profile + domain-keyed loop remains the spine); the Interest Community Platform pass should confirm the seam.

## Uncertainties

1. Pinterest, Goodreads, DeviantArt, Last.fm, and Behance documentation was unreachable this pass (timeouts/403). These are commonly cited as flagship members of this Type, so the abstracted core rests on three products with direct evidence (two rich, one structural) and one thin positioning line. Prevalence claims are deliberately avoided; wording in the final document is calibrated accordingly.
2. Douban's follow/friend mechanics were not directly observed (About page is philosophical/structural); its feed/tie details are inferred only as far as the page states.
3. Ravelry's operational mechanics are login-walled; only positioning was used.
4. The balance between follow-first and discovery-first feed postures across the market was not measurable.
5. Algorithmic interest feeds (visual-discovery class) were not directly observed; Level 1 wording stays generic.
6. Kudos-style reactions in activity products are market-known but were not in the fetched Strava pages; not used as evidence.

## Final Synthesis

The Interest-based Social Network is a social network whose world is bounded by a shared interest domain: members keep profiles that are persistent records of their engagement with that domain, contribute content objects anchored to it (bound to the domain's objects or produced as the domain's native artifact), and find both content and people through the domain's own structures — object pages, tags and classifications, member collections, taste similarity, and member-produced rankings — alongside person-to-person follow ties whose activity flows into persistent streams. The defining core is the jointly-held five-part structure above. The organizing key of the consumption/distribution loop is the interest: remove the domain-binding of identity, content, and discovery and the product collapses into a General Social Network; remove the social ties and it collapses into a content catalog/curation platform; strengthen shared containers until participation replaces the profile-and-stream loop and it drifts to the Interest Community Platform. Catalog databases, collections, ratings, feeds, recommendations, moderation, privacy controls, apps, and paid tiers are common mature structure; content typology, discovery posture, tie semantics, container depth, scope, and monetization are variants.
