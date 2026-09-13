# Research Notes — Microblogging Platform

Research date: 2026-09-08

## Research Goal

Understand the canonical structure of the Microblogging Platform Application Type: what the unit of publication is, what the follow tie means and how content is distributed, what the primary consumption surface is, how public conversation works, what discovery and control machinery exists, and where the boundary lies with the sibling Types of §01.05 (General Social Network, Photo-centric, Short-form Video, Professional, Neighborhood, Interest-based, Friend Discovery, Social Profile Network) and with adjacent Types (Blogging Platform, Online Forum/Community, Feed Reader, IM, Social Live Streaming).

This pass is a sibling pass under the §01.05 family boundary framework recorded by the processed `general-social-network` pass (discriminator: the organizing key of the core consumption/distribution loop; microblogging provisionally = **broadcast-subscription tie semantics**) and refined by the processed `interest-based-social-network` pass (domain-binding refinement). This pass ratifies or refines the framework from the microblogging side. The processed `blogging-platform` pass already drew the blogging↔microblogging seam from its side ("microblogging posts are short status updates consumed in a social follow-feed aggregating many authors; there is no author-owned publication container with its own address and archive") — this pass should confirm it from the microblogging side.

## Initial Boundary (pre-research hypothesis)

- Core hypothesis: public, short-form status posts; asymmetric follow = subscription to a person's broadcast stream; a merged multi-author feed as the home surface; public conversation (replies/mentions/reposts) attached to posts.
- Likely confusions: General Social Network (same surfaces, different tie semantics), Blogging Platform (publication vs status stream), Short-form Video (content-type key), Online Forum (topic containers), Feed Reader / Personalized Content Feed (aggregation without social authorship), IM (private conversation), Social Live Streaming (ephemerality).
- Unknowns going in: is a strict character limit definitional? is public-by-default definitional? is the chronological feed definitional? are reposts/hashtags/trends definitional? does federation change the core?

## Research Questions

1. What exactly is the unit of publication (post/status)? What forms does it take? Is brevity definitional, and how do long-form add-ons relate to it?
2. What does the follow tie mean operationally, and how does content reach an audience (subscription vs addressing vs acquaintance)?
3. What is the primary consumption surface? Is the aggregated multi-author feed definitional? Chronological vs algorithmic ordering?
4. How does public conversation work (replies, mentions, quotes/reposts)? Are conversation artifacts posts in the same space?
5. What visibility postures exist (public default, per-post visibility, protected accounts)? Is public-first definitional?
6. What discovery machinery exists (hashtags, trends, search, live/public timelines, algorithmic or user-built feeds)?
7. What control/moderation machinery exists (mute, block, filters, reply gating, quote consent, reporting)?
8. What identity substrates and deployment models exist (centralized vs federated/protocol-based)? Do they change the core?
9. Where are the removal-test boundaries to every neighboring Type?
10. Does the definition survive older/regional products (historical/market-sample check)?

## Representative Products

Selection logic: market representation + documentation accessibility + different product philosophies + different eras/regions. Documentation accessibility was the binding constraint (see Sources).

| Product | Role in sample | Philosophy / era | Evidence |
|---|---|---|---|
| Mastodon | decentralized, open-source, non-profit-instance microblogging (2016–) | federation-first, anti-centralization; user docs rich | A (rich) |
| Bluesky | protocol-based public-benefit microblogging (2023–) | open-protocol-first (AT Protocol), custom algorithmic feeds | A (rich, developer docs describing the app model) |
| Weibo | regional (China) centralized super-app microblogging (2009–) | ad-funded, celebrity/media-centric, super-app bundle | A (API-level model; user help unreachable) |
| X (Twitter) | canonical centralized microblogging; the Type's center of gravity and namesake era (2006–) | ad-funded, trend/media-centric | NOT OBSERVED — all official surfaces unreachable |

Historical/breadth check candidates (not source-verifiable this pass): SMS-era Twitter (140-char origin), Jaiku, Plurk, Tumblr (straddler: blogging platform with microblogging mechanics).

## Sources

Fetched 2026-09-08. The research environment could not reach any social-product web surface directly (timeouts/transport errors); official documentation was obtained through the vendors' own public source repositories and open-platform wiki, which serve the same official content.

Tier 1 — official operational documentation (all REACHABLE, evidence layer A):

- Mastodon user documentation (official repo `mastodon/documentation`, source of docs.joinmastodon.org):
  - `content/en/user/posting.md` — composing status updates, character limit, mentions/hashtags/links, attachments, polls, the four visibility levels, content warnings, reply-distribution rule
  - `content/en/user/network.md` — live feeds (local/federated public timelines), post actions (reply/boost/quote/favourite/bookmark), notifications, following, search (incl. full-text search limits), private mentions, list timelines, RSS syndication, translation
  - `content/en/user/discoverability.md` — featured hashtags, pinned posts, profile directory
  - `content/en/user/quote-posts.md` — quote consent machinery (Anyone / Followers only / Just me), revocation, quote-vs-reply context
  - `content/en/user/moderating.md` — keyword filters, hide boosts, mute, block, domain block, reporting
  - `content/en/user/profile.md` — profile fields, locked account, bot flag, profile metadata, rel=me link verification, author attribution
  - `content/en/user/signup.md` — server choice, signup modes (open/invite/approval), username@domain addressing
- Bluesky app documentation (official repo `bluesky-social/bsky-docs`, source of docs.bsky.app):
  - `docs/tutorials/creating-a-post.mdx` — post record structure (text/createdAt/facets), replies (root+parent strong refs), quote posts, image/external embeds
  - `docs/tutorials/following.mdx` — follow/unfollow as records
  - `docs/tutorials/like-repost.mdx` — like/repost as records; quote repost
  - `docs/tutorials/viewing-feeds.mdx` — timelines ("the default chronological feed of posts from users the authenticated user follows"), feed generators (custom feeds), author feeds
  - `docs/tutorials/thread-gates.mdx` — reply-gating rules (mention/following/follower/list; empty = nobody; absent = anybody)
- Weibo open platform (official Sina wiki, open.weibo.com):
  - `/wiki/微博API` — API index: statuses (home_timeline, user_timeline, repost_timeline, mentions, show, count, share), comments (show/mentions/create/reply), users (show, domain_show), OAuth
  - `/wiki/2/statuses/home_timeline` — home timeline definition ("获取当前登录用户及其所关注（授权）用户的最新微博"), weibo object fields (text, retweeted_status, reposts_count, comments_count, attitudes_count, visible types, ad array), user object fields (verified, followers_count, friends_count, statuses_count, domain)
  - `/wiki/2/statuses/update` — post creation ("发布一条新微博"): 140-Chinese-character native limit, is_longtext flag, visible (0 everyone / 1 self), geo, duplicate-post rule, non-member group-post limit

Unreachable / abandoned per network rules (limitations recorded; no claims drawn from memory for these):

- X: x.com (timeout ×2), about.x.com (timeout ×2), help.x.com (transport error), docs.x.com (transport error ×2) → abandoned. **No X-specific operational claim is made anywhere in this research.**
- Weibo user-facing surfaces: weibo.com (visitor-login wall, no content), help.weibo.com (timeout ×2) → abandoned; Weibo evidence is API-level only.
- Mastodon/Bluesky web surfaces: docs.joinmastodon.org, joinmastodon.org, mastodon.social, bsky.app, bsky.social/about/faq, docs.bluesky.xyz — all timeout/transport errors → abandoned; replaced by the official source repositories above (same content, different transport).
- Wikipedia (historical check for SMS-era Twitter/Jaiku/Plurk/Tumblr): en.wikipedia.org timeout ×2 → abandoned. Historical samples are therefore NOT source-verified this pass; the historical check is done structurally (see below).
- Tumblr, Plurk: timeout ×2 each → abandoned.

Consequence: the direct observational base is two decentralized products (rich) + one centralized regional product (API-level). The canonical centralized Western product (X) contributes no direct evidence. All final-document claims are kept at conceptual level; no precise numbers, defaults, or feature lists attributable to X appear anywhere.

## Product Observations

### Product A — Mastodon (evidence layer A — official user docs, rich)

1. **Unit of publication**: the "status update" — composed in a text field with a default character limit (500 by default; product-specific number), links counted at a fixed length, mentions addressed `@user@domain`, hashtags make posts "discoverable to anyone searching for that hashtag". Attachments: images, animated GIFs, video, audio; polls with expiry. Content warnings collapse the body ("similar to an email subject line or a read-more break"); media can be marked sensitive.
2. **Visibility**: four per-post levels — Public (default: anyone at the permalink, public timelines, profile, followers' home feeds, boostable), Quiet public/unlisted (same minus public feeds/explore/search), Followers (followers + mentioned only; not boostable except by self), Private mention (mentioned only; not boostable). Docs state explicitly: "post privacy on Mastodon is per-post, rather than account-wide. There is no way to make past public posts private." A default posting visibility can be set.
3. **Distribution semantics**: followers receive the post in their home feeds; mentions notify; boosts carry the post into other home feeds ("The post will be reshared on your profile"). Reply-distribution rule: "Your replies will only appear on your followers' Home feeds if they follow both you and the person you are replying to" — the subscription graph gates even conversation distribution. A post starting with an @mention is NOT a reply (it broadcasts to all followers).
4. **Consumption surfaces**: Home feed (followed authors); Live Feeds — browse all public posts on your server or "from across the fediverse" ("There is no global shared state between all servers, so there is no way to browse all public posts"); list timelines (user-defined subsets of the home timeline); profile streams; hashtag pages. Every account and tag page has an RSS feed.
5. **Public conversation**: replies thread under the post; boosts reshare; quotes reference another post with added commentary (consent machinery: author sets per-post and default quote policy — Anyone / Followers only / Just me; quotes can be revoked; quotes create a new context, not replies; blocked users cannot quote). Favourites notify the author; bookmarks are private with no notification.
6. **Discovery**: hashtags (searchable, autosuggested with usage frequency), live/public timelines, profile directory (opt-in; sortable by recent activity/new arrivals; filterable local/all), featured hashtags on profile, pinned posts (up to 5 of one's own public posts), search (hashtags, users, status URLs; full-text search deliberately limited to one's own posts/favourites/bookmarks/mentions — "You can't search for any text across the entire database. This prevents people from searching for controversial terms to find and harass others").
7. **Control/moderation**: keyword filters (per-context: home/lists, notifications, public timelines, conversations, profiles; with expiry, whole-word option, hide-completely server-side option); hide boosts from a followed user; mute (undetectable, optional duration, optional notification muting); block (forced unfollow both directions, hides from public timelines); domain block (entire server; loses its followers); reporting to local moderators with note + attached statuses + optional forwarding to the remote server's moderators.
8. **Identity/profile**: account on a chosen server ("like you would choose an email provider"); address = `@username@domain`; same username can exist on different servers; signup modes per server (open / invite / approval); profile = display name, bio, avatar, header, metadata fields, flags (locked account = manual follower approval; bot flag; directory opt-in); verification = rel=me link cross-reference (no central authority); author attribution for external articles.
9. **Notifications**: mentions, favourites, boosts, poll ends, follows, plus per-followed-user opt-in "bell" notifications for every post.
10. **Private messaging edge**: private mentions are posts with mention-only visibility; the DM column lists conversations containing them; docs warn "Mastodon is not an encrypted messaging app like Signal or Matrix" — the IM-shaped capability is a visibility level of the post, not a separate messaging system.
11. **Product-specific (L3)**: 500-char default; 23-char link counting; 4-row metadata fields; 30-char display name; FEP-044f quote-consent protocol; server-level signup modes; authorized-fetch / reply-fetching mechanics; translation button (server-configured); RSS per account/tag.

### Product B — Bluesky (evidence layer A — official developer docs describing the app model, rich)

1. **Unit of publication**: the post — a repository record (`app.bsky.feed.post`) whose required fields are `text` and `createdAt`; rich-text "facets" annotate mentions and links into the text; grapheme-based length counting implies a composition limit (number not stated in fetched pages). Embeds: images (up to 4, each with alt text), external website cards, record embeds (quote posts; also lists and feed generators).
2. **Distribution semantics**: following is a record the follower creates (`agent.follow(did)`); the timeline is defined as "the default chronological feed of posts from users the authenticated user follows" — subscription-defined consumption, chronological by default.
3. **Consumption surfaces**: timelines (following-based), **feed generators** — "custom feeds made by users and organizations" (algorithmic feeds as user-created objects, e.g. the official "Discover" feed), author feeds (single author; filterable: posts_with_replies / posts_no_replies / posts_with_media / posts_and_author_threads).
4. **Public conversation**: replies are posts carrying strong references to both the immediate parent and the thread root ("threads of replies can get pretty long"); quote posts embed a reference to another post with one's own text. Like and repost are records (create/delete); un-reposting deletes the repost record.
5. **Conversation control**: thread gates — the post author constrains who can reply (mention rule / following rule / follower rule / list rule; up to 5 rules; empty allow-list = nobody can reply; absent gate = anybody). Thread-owner moderation: "hide reply for everyone" (threadgate hiddenReplies) and "detach quote" (postgate detachedEmbeddingUris) — the author can remove others' contributions from their own thread's public rendering.
6. **Identity**: decentralized identity — handle (domain-shaped, e.g. `handle.example.com`) + DID; posts live in the user's repository on a PDS (Personal Data Server); self-hosting documented.
7. **Product-specific (L3)**: AT Protocol record/lexicon architecture; strong refs (URI+CID); 4-image/2MB limits; feed-generator marketplace mechanics; app-password auth; DID-based URLs recommended for reliability.

### Product C — Weibo (evidence layer A — official open-platform API docs; user-facing help unreachable)

1. **Unit of publication**: the weibo (微博) — "发布一条新微博" via `statuses/update`; the native `status` parameter is capped at **140 Chinese characters**; a separate `is_longtext` flag switches to long-form ("是否发送超过140字的长文") — direct evidence that the short post is the native unit and long-form is an add-on mode. Geo (lat/long) attachable; third-party metadata (annotations) attachable.
2. **Distribution semantics**: `statuses/home_timeline` = "获取当前登录用户及其所关注（授权）用户的最新微博" — the latest weibo of the logged-in user **and the users they follow (关注)**. The home timeline is subscription-defined. `statuses/mentions` = the stream of weibo that @-mention the user.
3. **Post object**: text, created_at, source (posting client), favorited, truncated, in_reply_to_* fields, image fields (thumbnail/middle/original), geo, author (user object), **retweeted_status** ("被转发的原微博" — the original weibo carried by a repost), **reposts_count** (转发数), **comments_count** (评论数), **attitudes_count** (表态数 — likes), **visible** object (type: 0 normal / 1 private / 3 specified-group / 4 close-friends, with group id), pic_ids, and an **ad** array (promoted weibo injected in the stream).
4. **Public conversation**: two distinct conversation artifacts — **comments** (评论: comments/show, comments/create, comments/reply, comments/mentions) and **reposts** (转发: repost_timeline = "返回一条原创微博的最新转发微博"; the repost is itself a weibo carrying retweeted_status). Both are counted on the post.
5. **Visibility postures**: per-post visible types (normal / private / group / close-friends); anti-spam rule ("连续两次发布的微博不可以重复" — consecutive posts cannot be duplicate); membership-gated limit ("非会员发表定向微博，分组成员数最多200" — non-members' group-targeted posts cap at 200 group members).
6. **Identity/profile**: user object with screen_name, description, profile_image_url, **domain** (个性域名 — personal domain), location (province/city), followers_count, friends_count (following), statuses_count, favourites_count, **verified** + verified_type + verified_reason (authentication), badges, level, online_status; `users/domain_show` resolves a personal domain to a user.
7. **Ecosystem bundling (L2/L3 context)**: the open platform's own taxonomy shows the super-app wrapper around the microblogging core — 粉丝服务平台 (fans service platform: receive/send messages, custom menus, user management for accounts), 电商接入 (e-commerce seller/service-provider APIs), 商业接口 (commercial data APIs), 微博龙虾 (assistant/community), advertising surfaces. The microblogging core (statuses/comments/users) is a distinct API family from all of these.
8. **Product-specific (L3)**: 140-Chinese-char native limit + is_longtext; visible types 0/1/3/4; attitudes_count; verified_type taxonomy; badges/level; weihao; ad array; fans-service messaging machinery; e-commerce APIs.

### Product D — X (no direct observation this pass)

All official surfaces unreachable (see Sources). X is retained in the sample as the canonical market anchor — the Type's namesake era and largest product — but per evidence rules, NOTHING about X's current features, limits, or defaults is asserted in this research or the final document. The model stands on the three observed products.

## Historical / Market-Sample Check

Question: would older, regional, platform-native products still fit the definition?

- **Regional (directly evidenced)**: Weibo (2009, China) satisfies the core on official API evidence — and its API still documents the **140-Chinese-character native limit with long-form as a flag**, which is the SMS-era lineage preserved in a living product. This anchors the historical form with direct evidence rather than memory.
- **SMS-era generation (not source-verifiable this pass)**: the founding generation of microblogging (SMS-era Twitter, Jaiku, Plurk) is structurally covered by the definition as written: short status posts + follow-as-subscription + merged feed + public conversation. The definition deliberately requires none of: specific length numbers, hashtags, reposts, trends, algorithmic feeds, ads, DMs, media attachments, verification, or federation — every one of those is documented as common/variant structure, so the older generation fits even if it lacked all of them. (Wikipedia unreachable; recorded as an uncertainty, not silently filled from memory.)
- **Platform-native / differently positioned**: the definition is identity-substrate-neutral (username@domain, domain handle + DID, UID + personal domain all observed; phone/email not observed but not excluded) and deployment-neutral (centralized Weibo and federated Mastodon/Bluesky both satisfy).
- **Straddler noted**: Tumblr-class products (blogging platform with microblogging mechanics — reblog, follow feed) sit on the blogging boundary; the blogging-platform pass drew the seam from its side (no author-owned publication container in microblogging). Not directly examined this pass (tumblr.com unreachable); the seam is held conceptually.

## Cross-product Comparison

| Dimension | Mastodon (observed, user docs) | Bluesky (observed, app-model docs) | Weibo (observed, API docs) | X (not observed) |
|---|---|---|---|---|
| Unit of publication | status update, default 500-char limit | post record (text + createdAt), grapheme-counted limit | weibo, native 140-Chinese-char limit + long-text flag | (not verified) |
| Follow tie | follow across servers; home feed of followed authors | follow record; "default chronological feed of posts from users the authenticated user follows" | home_timeline = self + 关注 (followed) users | (not verified) |
| Aggregated feed | home feed; live feeds (local/federated public); lists | timeline; feed generators (custom algos); author feeds | home_timeline; mentions stream; repost_timeline | (not verified) |
| Public conversation | replies (threaded, subscription-gated), boosts, quotes (consent machinery), favourites, bookmarks | replies (root+parent refs), reposts (records), quotes (record embeds), likes | comments (separate object) + reposts (weibo carrying original) + attitudes (likes) | (not verified) |
| Visibility posture | per-post: public (default) / quiet public / followers / private mention | public posts; thread gates control replies | per-post visible types: normal / private / group / close-friends | (not verified) |
| Discovery | hashtags, live feeds, profile directory, pinned posts, search (self-scoped full-text) | feed generators (Discover), search (not fetched), author feeds | mentions stream; feature filters (original/image/video/music) | (not verified) |
| Control/moderation | filters, mute, block, domain block, reporting | thread gates, hide-reply-for-everyone, detach-quote, block/mute (docs exist) | duplicate-post rule, group-post limits | (not verified) |
| Identity substrate | username@domain on a chosen server | domain handle + DID on a PDS | UID + screen_name + personal domain; verified status | (not verified) |
| Deployment | federated (ActivityPub instances) | protocol-based (AT Protocol; self-hostable PDS) | centralized | (not verified) |
| Monetization observed | none in docs (non-profit instance model) | none in fetched docs | ad array in timeline; commercial/fans/e-commerce API families | (not verified) |
| Era / region | 2016, global | 2023, global | 2009, China | 2006–, global |

### Stable cross-product commonalities (evidence B where ≥2 observed, C where inferred)

1. **The short status-shaped post as the native unit** — B×3 (all observed products), with composition limits that vary by product and long-form existing only as an add-on mode (Weibo's is_longtext flag is direct evidence of the add-on pattern).
2. **Follow-as-subscription distribution** — B×3: the home surface is defined by "posts from users the authenticated user follows" (Bluesky verbatim; Weibo verbatim; Mastodon structurally).
3. **The aggregated multi-author feed as the primary consumption surface** — B×3 (home feed/timeline in all three), supplemented by public timelines, lists, author streams, and (Bluesky) user-built algorithmic feeds.
4. **Posts form a public conversation space** — B×3: replies, mentions, and reposts/quotes are posts or post-attached artifacts in the same public space; conversation accumulates around posts (Mastodon and Bluesky: replies/quotes ARE posts; Weibo: comments + reposts as the two conversation artifacts, both counted on the post).
5. **Mentions as an addressing primitive inside posts** — B×3 (@user@domain; DID mentions via facets; @-mentions with a dedicated mentions stream).
6. **Hashtags as discovery keys** — B×2 directly (Mastodon; Weibo feature filters imply content-type keys but hashtag evidence is market-context for Weibo — kept B×1 direct + market context). Trends/trending surfaces: A×1 (Mastodon's public-feeds definition mentions trending); kept at L1.
7. **Author profile as the person's stream home** — B×3 (profile with posts tab/stream; Weibo user_timeline; Bluesky author feed).
8. **Interaction primitives: like/favourite + countable engagement on the post** — B×3 (favourites; like records; attitudes_count).
9. **Control machinery over what one sees and who interacts** — B×3 (mute/block at minimum; filters, domain blocks, thread gates, quote consent as richer forms).
10. **Media attachments and link cards** — B×3 (images/video/audio; external card embeds; Weibo image fields).
11. **Notifications for conversation events** — B×3 (mentions/favourites/boosts/follows; Weibo mentions stream; Bluesky reply/quote notifications implied by thread machinery — kept B×2 direct + structural for Bluesky).

### Cross-product differences (variants, not core)

- Deployment: centralized (Weibo) vs federated (Mastodon) vs protocol-based with self-hostable data (Bluesky).
- Feed ordering: chronological default (Bluesky timeline verbatim; Mastodon lists/home) vs user-selectable algorithmic feeds (Bluesky feed generators) vs engagement-ranked (market context for X/Weibo — not directly evidenced).
- Visibility granularity: per-post visibility levels (Mastodon 4 levels; Weibo 4 types) vs post-level reply gating (Bluesky thread gates) vs account-level protected posture (market context; not directly evidenced).
- Conversation artifact structure: replies-as-posts + quotes-as-posts (Mastodon, Bluesky) vs comments-as-separate-object + reposts-as-posts (Weibo).
- Quote governance: consent + revocation (Mastodon) vs detach/hide (Bluesky) vs (Weibo: not evidenced).
- Identity substrate: username@domain vs handle+DID vs UID+personal domain.
- Monetization: ads in feed (Weibo) vs none observed (Mastodon/Bluesky docs) vs (X: not evidenced).
- Super-app bundling: Weibo wraps commerce/fans-service/commercial APIs around the core; Mastodon/Bluesky stay focused.

## Canonical Model — Four Abstraction Levels

### L0 — Defining Invariant (deliberately minimal; jointly-held)

```text
Broadcast-Subscription Post Network

Short status-shaped post (the native unit of publication)
└── Follow-as-subscription tie
    (follow = subscribe to a person's broadcast stream;
     the audience of a post is whoever subscribes, plus
     platform visibility rules — never a named recipient set)
    └── Aggregated multi-author feed
        (the home surface merges the streams of all subscribed
         authors into one scrolling timeline)
    └── Public conversation attached to posts
        (replies, mentions, and reposts/quotes are posts or
         post-attached artifacts in the same space; discourse
         accumulates around posts)
```

Four properties, jointly held. Removal tests:

- Remove the **short status-shaped post** (the native unit becomes the long-form article in an author-owned publication with its own address and archive) → Blogging Platform with social features → not this Type.
- Remove **follow-as-subscription** (ties become acquaintance links and audiences are curated per post, or content is addressed to specific recipients) → General Social Network or Instant Messaging → not this Type.
- Remove the **aggregated multi-author feed** (consumption happens by visiting author streams/publications; no merged home surface) → syndication/subscription reading (Feed Reader territory) or profile-browsing publication network → not this Type.
- Remove the **public conversation space** (posts are pure broadcast items with no replies/mentions/reposts accumulating around them) → a syndication wire / broadcast channel → not this Type.

Notes:

- **"Public" is a default, not the invariant.** Per-post visibility levels (Mastodon: public/quiet-public/followers/private-mention; Weibo: normal/private/group/close-friends) and reply gating (Bluesky thread gates) are observed postures. The invariant is the *addressing model*: even a restricted post is delivered to a subscriber/visibility class — broadcast-subscription — not addressed to named recipients. The IM-shaped edge (private mentions) exists in products but is explicitly not the messaging system (Mastodon: "not an encrypted messaging app").
- **"Short" is a design posture, not a number.** Composition limits exist in all observed products and vary (140 Chinese characters native in Weibo; 500-character default in Mastodon; Bluesky counts graphemes against a limit). Long-form exists only as an add-on mode (Weibo's is_longtext flag), never as the native unit.
- **No requirement of**: hashtags, reposts, trends, algorithmic feeds, ads, DMs, media, verification, federation, or any specific length number — all of those sit at L1/L2, which is what makes the historical check pass.

### L1 — Common Mature Structure

- **Author profile** — display identity (name, avatar, bio) plus the author's own post stream; the person's home inside the product.
- **Repost / boost (amplification)** — re-sharing another's post into one's own stream; quote variant adds commentary (observed in all three; consent/revocation and detach machinery in newer products).
- **Likes / favourites** — one-click endorsement, usually notifying the author and counted on the post.
- **Hashtags and topic/trend discovery** — hashtag search and pages; trending surfaces; live/public timelines for browsing all public posts.
- **Search** — over posts, authors, hashtags; scope varies (Mastodon deliberately limits full-text search to one's own interactions).
- **Notifications** — mentions, likes, reposts, replies, follows; per-author opt-in bells.
- **Media attachments** — images, video, audio, GIFs; link/website cards; polls; location.
- **Content warnings / sensitive-media flags** — collapse-with-consent presentation.
- **Lists of authors** — user-defined subsets of the follow graph rendered as dedicated timelines.
- **Control machinery** — keyword filters with contexts, mute (undetectable), block (severs the tie both ways), reporting to moderators; richer forms: domain/server blocks (Mastodon), thread gates and hide-reply/detach-quote (Bluesky).
- **Verification signals** — platform authentication marks (Weibo verified fields), link-based self-verification (Mastodon rel=me), domain-handle identity (Bluesky).
- **Direct/private messaging edge** — private mentions / DM surfaces exist beside the public space (Mastodon private mentions; Weibo私信 per market context) but are not the Type's center.
- **Syndication/export** — RSS/Atom feeds for accounts and tags (Mastodon); API access (all three).
- **Ads/promoted posts in the feed** — observed (Weibo ad array); monetization posture varies.

### L2 — Variant / Optional Structure

- Deployment model: centralized service vs federated instances vs protocol-based network with self-hostable personal data servers.
- Identity substrate: username@domain, domain handle + decentralized ID, UID + personal domain, phone/email (market context).
- Feed ordering philosophy: chronological vs algorithmic vs user-selectable custom feeds (feed generators).
- Visibility posture: public-default with per-post levels vs account-level protected posture; reply gating; quote consent.
- Conversation artifact structure: replies/quotes as posts vs comments as a separate object class.
- Composition limits and long-form add-ons (numbers and mechanics vary by product).
- Discovery posture: follow-first vs discovery/trend-first vs custom-algorithm-first.
- Monetization: ad-funded, subscription/premium tiers, none/donation-funded.
- Regional super-app bundling: commerce, fans-service/creator messaging, live, vertical media wrapped around the microblogging core.
- Moderation regime: per-server rules (federated), platform-wide rules (centralized), jurisdictional compliance.

### L3 — Vendor-specific (research notes only; not in final document)

- Mastodon: 500-char default limit; 23-char link counting; 4-row profile metadata; 30-char display names; FEP-044f quote-consent protocol; per-server signup modes (open/invite/approval); authorized-fetch; reply-fetching across servers; translation service integration; RSS per account/tag; pinned-post limit (5); bot flag; locked-account mechanics; full-text search scoping rationale.
- Bluesky: app.bsky.feed.post record schema; strong refs (AT URI + CID); root+parent reply references; 4-image/2MB embed limits; feed generators as user-created records; threadgate rule set (mention/following/follower/list, max 5); postgate detach mechanics; DID/handle identity; PDS self-hosting; app passwords.
- Weibo: 140-Chinese-char native limit + is_longtext flag; visible types 0/1/3/4 with group ids; attitudes_count; verified_type/verified_reason; badges and level; weihao; personal domain (个性域名) lookup; duplicate-post rule; non-member 200-member group-post cap; ad array in timeline; 粉丝服务平台 messaging machinery; 电商/商业 API families.
- X: nothing recorded (unreachable this pass).

## Rejected Findings

- "A strict character limit is definitional" — REJECTED as a specific number: limits vary (140 Chinese chars native in Weibo; 500-char default in Mastodon) and have loosened over time; the invariant is the brief status-shaped unit, with long-form as an add-on mode (Weibo is_longtext is direct evidence).
- "Microblogging is public-only" — REJECTED: per-post visibility levels (Mastodon, Weibo) and reply gating (Bluesky) are observed; the invariant is broadcast-subscription addressing, not universal publicity.
- "The chronological reverse-chron feed is definitional" — REJECTED: Bluesky ships user-built algorithmic feed generators as first-class surfaces; ordering is a variant axis.
- "Reposts/retweets are definitional" — REJECTED: amplification is common mature structure (all three observed products have it), but the distribution substrate is the follow tie itself; a subscription feed without reposts is still recognizable microblogging (and the historical generation predates the mechanic — not source-verified this pass, but the L0 does not depend on it).
- "Hashtags/trends are definitional" — REJECTED: discovery machinery, not the distribution substrate.
- "DMs are part of the Type" — REJECTED: private mentions are a visibility edge of the post (Mastodon explicitly disclaims being a messaging app); IM is a separate Type.
- "Federation/decentralization is definitional" — REJECTED: centralized (Weibo) and federated/protocol-based (Mastodon, Bluesky) both satisfy the core.
- "Microblogging = Twitter-clone features" — REJECTED: over-fit to one product family and era; the sample spans three deployment models, two conversation-artifact structures, and three identity substrates.
- "The aggregated feed must be algorithmic" — REJECTED: chronological defaults are directly documented (Bluesky, Mastodon); ranking is a variant.

## Boundary Findings

### Family framework ratification (§01.05)

The general-social-network pass's family framework is **RATIFIED from this side with one refinement**. The organizing key of the microblogging core loop is indeed **broadcast-subscription tie semantics**. The refinement: the tie semantics are inseparable from the consumption surface — "follow = subscribe to a person's broadcast stream" only constitutes microblogging when those subscriptions are consumed in a **merged multi-author feed**. Stated as the family test: *ties are public broadcast subscriptions, posts are general/untyped status-shaped broadcasts, and consumption is the merged stream of one's subscriptions.* This is consistent with the interest-based pass's phrasing ("ties become public broadcast subscriptions and posts become general/untyped") and with the general-social-network pass's ("follow = subscribe to broadcasts, posts public-first, discovery-first consumption").

### Removal tests against neighbors

| Neighbor Type | Relationship | Removal test (what removed → becomes that Type) |
|---|---|---|
| General Social Network (§01.05) | sharpest structural overlap | ties become personal-acquaintance links with per-post audience curation and profile-centered consumption → General SNS; the follow tie's MEANING (subscription vs acquaintance) is the seam |
| Professional Social Network (§01.05) | audience/context sibling | career/professional context becomes the organizing key of identity and sharing → professional |
| Photo-centric / Short-form Video (§01.05) | content-type siblings | the medium (photo/video) becomes the organizing key with creation-first or discovery-first loops → those Types |
| Neighborhood Social Network (§01.05) | locality sibling | verified locality becomes the membership key → neighborhood |
| Interest-based Social Network (§01.05, processed) | organizing-key sibling | a shared interest domain bounds content and identity (domain-anchored objects, interest-keyed discovery) → interest-based; microblogging posts are general/untyped |
| Friend Discovery Application (§01.05, processed) | formation-loop sibling | forming new relationships with strangers becomes the primary loop → friend discovery; here ties are consumption subscriptions, not formation goals |
| Social Profile Network (§01.05) | substrate sibling | remove the post stream and feed → profiles + connections directory |
| Blogging Platform (§02.07, processed) | publication sibling | the native unit becomes the article in an author-owned publication with its own address/archive; consumption by visiting publications → blogging; here the unit is the status-shaped post consumed in the social feed — confirms the blogging pass's seam from this side |
| Online Forum / Community Platform (§01.06) | container sibling | content organized by topic containers (boards/threads under communities) with membership, not by author subscription → forum/community |
| Feed Reader / Personalized Content Feed (§02.08) | aggregation siblings | remove social authorship (content is third-party, not user-published) and the public conversation space → aggregation/reading |
| Instant Messaging Application (§01.01) | conversation sibling | private, addressed, small-party conversation with persistent threads → IM; the DM/private-mention edge here is a visibility posture of public-space posts, not a conversation graph of its own |
| Social Live Streaming Platform (§01.08) | temporality sibling | ephemeral live broadcast with simultaneous viewers → live social; here posts are persistent, asynchronous broadcast items |
| News Application / News Aggregator (§02.04) | media sibling | editorially produced or aggregated third-party content without user authorship → news |

Boundary blur zones recorded honestly: modern products ship stories, live, long-form, audio spaces, and commerce as capabilities; assignment follows the core loop (broadcast-subscription post network), not feature presence.

## Uncertainties

1. **X contributes no direct evidence** — the canonical centralized product was entirely unreachable (all four official domains failed). The model rests on two decentralized products (rich) + one centralized regional product (API-level). Prevalence claims about the market's largest product are deliberately absent; the final document's claims are calibrated to the observed sample.
2. **Historical generation not source-verified** — SMS-era Twitter, Jaiku, Plurk could not be checked against any source (Wikipedia unreachable). The L0 is written so none of them is required to have anything beyond the four core properties; the Weibo 140-char native limit (directly documented today) serves as the living anchor for the SMS-era lineage.
3. **Weibo evidence is API-level** — user-facing help (help.weibo.com) was unreachable; user-facing workflows (compose UI, trends UI, hot-search) are inferred only as far as the API objects imply. No user-UI claims are made.
4. **Bluesky evidence is developer-doc-level** — it describes the app model authoritatively (records, feeds, gates) but not end-user help prose; user-UI claims kept generic.
5. **Trends/trending surfaces** — directly evidenced only in Mastodon's public-feeds definition; prevalence across the market not measured.
6. **Account-level protected/private account posture** (as opposed to per-post visibility) — market-known for X-class products but not directly observed this pass; kept out of all claims.
7. **DM prevalence** — directly observed only as Mastodon private mentions; Weibo私信 and Bluesky DMs are market context, not evidence.

## Final Synthesis

The Microblogging Platform is a **broadcast-subscription post network**: the native unit of publication is a short, status-shaped post; the follow tie is a subscription to a person's broadcast stream (the audience of a post is whoever subscribes, plus visibility rules — never a named recipient set); the primary consumption surface is an aggregated multi-author feed merging all subscribed streams; and posts form a public conversation space where replies, mentions, and reposts/quotes accumulate around posts as posts or post-attached artifacts. The defining core is exactly these four jointly-held structures. Everything else — profiles, reposts, likes, hashtags, trends, search, notifications, media, lists, filters, moderation, verification, DMs, ads, syndication — is common mature structure; deployment model, identity substrate, feed ordering, visibility granularity, conversation-artifact structure, monetization, and bundling are variants. The Type is assigned by the organizing key of the core loop: broadcast-subscription tie semantics over general/untyped status posts — not a person-acquaintance graph (General SNS), not a content type (photo/short-form), not an interest domain (interest-based), not an audience context (professional), not a locality (neighborhood), not topic containers (forums), not author-owned publications (blogging), and not private addressed conversation (IM).
