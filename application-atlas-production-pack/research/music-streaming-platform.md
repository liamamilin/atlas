# Research Notes — Music Streaming Platform

## Research Goal

Understand what a Music Streaming Platform actually is as an Application Type — from real products, not from marketing definitions:

- what the platform's "world" consists of (objects, relations);
- what the listener does around them;
- how playback, selection, and personal state work;
- what is definitional vs. merely common in today's market;
- where the boundary with Internet Radio Platform, Podcast Platform, and neighboring music-industry Types lies.

Cross-consistency requirement: the sibling leaf `internet-radio-platform` (processed 2026-09-08) already defined the seam: "the test is the organizing unit of the catalog: if the persistent, addressable things the user selects and saves are broadcast outlets whose output is a shared live flow, it is this Type [internet radio]; if they are tracks and albums the user owns and queues, it is music streaming." This pass must independently derive a definition that satisfies that test.

## Initial Boundary

Temporary hypothesis before research:

- Core use: on-demand listening to recorded music from a large platform-provided catalog; the user selects individual tracks/albums/playlists and builds persistent personal collections.
- Primary user: individual listener (consumer). Artists/labels are supply side but do not drive the core loop.
- Nearest Types: Internet Radio Platform (station/live flow), Podcast Platform (episodic shows), Video Streaming Platform (moving image), Digital Goods Store (purchase-and-own files), Music Distribution Platform (supply-side delivery of recordings into services), Music Publishing Management (composition-side rights), AI Music Generator (creation), local file players (no platform catalog).
- Most likely confusion: Internet Radio Platform, because modern music platforms embed "stations"/radio as features.

Unknowns at start: whether personal library/playlists are definitional or just universal practice; how monetization tiers interact with on-demand control; how regional licensing shapes the product; whether social layers (follow graphs, collaborative playlists) are variant or common.

## Research Questions

1. What are the core objects? (track / album / artist / playlist / queue / library / station / podcast…)
2. What exactly does "on-demand" mean operationally — what playback controls and selection rights does the listener have?
3. What personal state does the listener accumulate, and does it persist across sessions/devices?
4. What roles do playlists play — user-built, editorial, algorithmic?
5. How do discovery surfaces work (browse, charts, search, recommendations, stations)?
6. How is the service monetized, and what does the tier structure gate (on-demand control, offline, quality, ads)?
7. How does licensing shape the product (regional availability, catalog claims, catalog vs. owned files)?
8. Which adjacent content types (podcasts, radio, video, lyrics) live inside the platform without changing the Type?
9. Historical check: would 2000s-era subscription services, regional products, and platform-native players still fit the definition?
10. Where exactly is the boundary with Internet Radio Platform, Podcast Platform, Digital Goods Store, and Video Streaming Platform?

## Representative Products

Selection principles applied: market representation, reachable official surfaces, different product philosophies, different geographies/customer tiers. Four products with directly fetched official surfaces:

1. **Apple Music** — subscription-first, platform-ecosystem-native, global; official product page (www.apple.com/apple-music/).
2. **Amazon Music** — retail-ecosystem-bundled, freemium (Free tier + Unlimited), global; official product pages (www.amazon.com/music/).
3. **JioSaavn** — regional (India), web client with visible structural surfaces (library, queue, stations); official site (www.jiosaavn.com).
4. **NetEase Cloud Music (网易云音乐)** — regional (China), playlist-centric culture with a strong social layer and VIP membership; official site (music.163.com).

Attempted but inaccessible this pass (recorded per source-access rules; NOT used as evidence for any specific claim):

- Spotify — support.spotify.com and www.spotify.com both served a geo-block shell ("Spotify is currently not available in your country") after two attempts.
- YouTube Music — support.google.com and www.youtube.com timed out (multiple attempts).
- Deezer — www.deezer.com timed out (two attempts).
- Tidal — tidal.com returned HTTP 403.
- SoundCloud — help.soundcloud.com and artists.soundcloud.com timed out (two/three attempts).
- Pandora — www.pandora.com served a geo-block shell ("Pandora is unavailable in this country or region").
- Qobuz — www.qobuz.com timed out.

The Pandora and Spotify geo-block shells are themselves usable as **direct evidence of regional service restriction** (a platform-level behavior), though not of anything structural about catalogs or libraries.

## Sources

Fetched successfully (research date 2026-09-08):

- Apple — Apple Music product page: https://www.apple.com/apple-music/ (plans, FAQ, feature sections, footnotes).
- Amazon — Amazon Music product page: https://www.amazon.com/music/ (Unlimited + Free tier framing).
- JioSaavn — official web client home: https://www.jiosaavn.com/ (browse taxonomy, library, queue, stations).
- NetEase Cloud Music — official web client home: https://music.163.com/ (navigation, player/queue structure, login, VIP surfaces).

Unreachable (attempted, abandoned per 1–2 attempt rule): Spotify, YouTube Music, Deezer, Tidal, SoundCloud, Pandora, Qobuz — see Representative Products for detail.

Evidence layers used in observations: **A = directly observed** on the fetched official surface; **B = cross-product commonality** across the fetched sample; **C = canonical inference** from comparison + Type-boundary reasoning.

---

## Product 1 — Apple Music (Layer A)

Source: official product page (apple.com/apple-music).

Key observations:

- Self-definition (FAQ): "Apple Music is a streaming service that allows you to listen to over 100 million songs" — catalog-scale claim of ~100M tracks, on a **subscription** model (no free tier in the offered plans; "Apple Music has zero ads").
- Plans: Individual / Family / Student / Apple One bundle; Family gives "each person their own library, recommendations, and playlists" — direct evidence that **library + playlists + recommendations are per-person state**.
- On-demand + offline: "download your favorite tracks and play them offline" — offline download is a subscription capability; playback is of catalog content without file purchase.
- Library continuity with owned files: "Your iTunes library is still yours. You can access your entire collection from Apple Music or from iTunes" — direct evidence that the platform **coexists with a personal owned-file library** (streaming catalog ≠ owned files; two different layers in one product).
- Playlists: user-facing playlist creation ("Create instant playlists… with Playlist Playground"), **collaborative playlists** ("invite them to add, remove, reorder, and react to songs"), curated/editorial playlists ("curated playlists from our editors").
- Discovery: "personalized artist and album suggestions based on your listening history"; "Explore a world of genres".
- Live radio inside the platform: "live local, global, and artist-led radio shows and stations"; footnote 10 lists named stations (Apple Music 1 / Hits / Country / Música Uno / Club / Chill) that are "available without an Apple Music subscription" — radio is an embedded content class, partly free-standing of the subscription.
- Audio quality tiering: Lossless / Hi-Res Lossless / Spatial Audio (Dolby Atmos) as subscription features with device dependencies.
- Lyrics: "lyrics in real time"; Apple Music Sing (animated lyrics, adjustable vocals) — karaoke-grade lyric surface.
- Multi-surface: iPhone/iPad/Watch/Mac/Vision Pro/HomePod/Apple TV/CarPlay/Android/Windows/Sonos/TVs/consoles — cross-surface delivery is a headline capability.
- Companion/adjacent: Apple Music Classical (separate classical-focused app, shared library — "classical tracks, albums, and playlists added in either app are instantly available in the other"); Shazam integration ("identify and add songs"); Concerts Near You; Apple Music Live exclusives.
- Supply side: "Apple Music for Artists" portal (artists.apple.com) — artist-facing tools ("create, release, promote, and measure").
- Regional/legal texture: footnote 14 — collaborative playlists unavailable in a named list of countries/regions and for under-13 accounts — direct evidence that features are region-gated.

## Product 2 — Amazon Music (Layer A)

Source: official product page (amazon.com/music).

Key observations:

- Tier structure is the page's organizing frame: **Amazon Music Unlimited** ("Unlimited access to 100 million songs… 100 million songs ad-free and on demand") vs **Amazon Music Free** ("Free streaming music — no credit card required").
- The page explicitly positions **on-demand as the paid differentiator**: free tier = "Discover new music and podcasts based on your likes", "Thousands of stations and top playlists"; then "Want on-demand music + HD and spatial audio? Try Amazon Music Unlimited." Direct evidence that **on-demand control, HD/Spatial quality are gated by tier**, while free tier leans on stations/curated playlists and personalization.
- Podcasts bundled: "The most ad-free top podcasts", "Millions of podcast episodes" — podcasts are a first-class content class inside the same product.
- Audiobooks bundled (Audible catalog claim) — adjacent audio content inside the umbrella service.
- Catalog-scale claim ~100M songs (matches Apple's claim order of magnitude).
- Web player as a surface ("Open Web Player"); app promoted ("Get the most out of Amazon Music wherever you go with the mobile app").
- No structural detail on personal library on this page — **library existence in this product is NOT directly evidenced by this fetch** (flagged for evidence calibration; not used for any L0 claim on its own).

## Product 3 — JioSaavn (Layer A)

Source: official web client (jiosaavn.com home).

Key observations:

- Structural surfaces visible in the shell itself:
  - **Library** with named sections: History, Liked Songs, Albums, Podcasts, Artists + **"New Playlist"** action — direct evidence of personal listening state: liked/saved songs, saved albums, saved artists, listening history, user playlist creation.
  - **Queue** with **Save / Clear** actions and a "Drop Here to Add to Queue" target — direct evidence of an explicit, manipulable, saveable playback queue.
  - Global player bar with prev/play/next and time display.
- Browse taxonomy: New Releases, Top Charts, Top Playlists, Podcasts, Top Artists, Radio — the platform's catalog organization made visible.
- Editorial/featured playlists as catalog objects with social counts ("Fans", "Followers" — e.g. "2.5M Followers") — playlists are addressable, followable objects.
- **Radio stations inside the product**: a "Radio Stations" rail of named algorithmic stations ("Party Karlo", "Desi Hip Hop", "90s Nostalgia"…) all labeled "Hindi Radio" — stations as playback features derived from the catalog, not broadcast outlets.
- Charts: region-specific chart playlists ("Hindi: India Superhits Top 50", decade playlists "Hindi 1970s…1990s") — charts and era organization.
- Top Artists rail — artist pages are first-class catalog objects.
- Podcasts bundled as a top-level section.
- Title tag claims: "Download & Play Latest Music for Free" — free access posture with download claims (tier details not visible on this surface).
- Content base: film-soundtrack-heavy regional catalog (Bollywood/regional cinema naming throughout) — regional catalog economics visible.

## Product 4 — NetEase Cloud Music (Layer A)

Source: official web client (music.163.com home).

Key observations:

- Navigation frame: 发现音乐 (Discover) / 我的音乐 (My Music) / 关注 (Following — a social follow graph) / 商城 (Store) / 音乐人 (Musicians) / 云推歌 (song promotion service) / 创作者中心 (Creator Center); search spans 音乐/视频/电台/用户 (music/video/radio/users).
- Discover taxonomy: 推荐 (Recommendations), 排行榜 (Charts), **歌单 (Playlists)**, 播客 (Podcasts), 歌手 (Artists), 新碟上架 (New Albums) — playlists elevated to a top-level discovery dimension (playlist-centric culture).
- Player/queue: persistent bottom player (prev/play/next, shuffle, time); **播放列表 (play queue) panel** with per-item actions 删除 (remove) / 下载 (download) / 分享 (share) / 收藏 (favorite/collect), plus 收藏全部 (collect all) and clear; queue items can be radio programs ([电台节目]) or songs; **lyrics panel** with scrolling lyrics, translation upload, and error reporting (报错) — community-maintained lyrics metadata.
- Login: phone-number login, QR-code login (via mobile app), WeChat/QQ/Weibo third-party login, email login — multi-identity login typical of the regional market.
- Membership: VIP 会员 center in user menu; 黑胶VIP ("Vinyl VIP") branding surfaced in UI bubbles; quality claim "打开客户端播放，享受高清音质" (open the client for HD audio quality) — quality features tied to client + membership tier.
- Native client emphasis: desktop/mobile client download promoted; web is a secondary surface.
- Social/community texture: 关注 (follow) as top-level nav; playlist pages with fans/followers (visible in playlist culture); user homepages (user/home), messages, user level (我的等级), real-name verification (实名认证) — the platform is also a social product around music.
- MV (music video) support: search includes MVs; queue items link to MV pages.
- Creator/supply side: 音乐人 (musician) portal, 云推歌 (paid song promotion), creator center — supply-side surfaces inside the consumer product's frame.

## Cross-product Comparison

| Dimension | Apple Music | Amazon Music | JioSaavn | NetEase Cloud Music |
|---|---|---|---|---|
| Catalog of recordings (tracks/albums/artists) | yes, "100M songs" claim | yes, "100M songs" claim | yes (regional/film-heavy) | yes (charts/new albums/artists) |
| On-demand selection & playback | yes (subscription) | yes in paid tier ("ad-free and on demand"); free tier leans on stations/playlists | yes (visible player/queue) | yes (visible player/queue) |
| Personal library / saved state | yes ("own library… playlists"; per-person in Family) | not evidenced on fetched page | yes (Library: Liked Songs/Albums/Artists/History) | yes (我的音乐 + 收藏 in queue) |
| User-created playlists | yes (incl. collaborative) | not evidenced on fetched page | yes ("New Playlist") | yes (歌单 as top-level culture) |
| Editorial/curated playlists | yes | yes ("top playlists") | yes (featured playlists w/ follower counts) | yes (歌单 discovery) |
| Search | not detailed on page | store-level search only | yes | yes (multi-type search) |
| Charts / new releases / genres browse | genres + personalized suggestions | playlists/stations framing | New Releases / Top Charts / Top Artists | 排行榜 / 新碟上架 / 推荐 |
| Algorithmic stations / personal radio | personalized suggestions; named live stations | "thousands of stations" (free tier) | named algorithmic stations rail | radio-program content; 推荐 |
| Queue as manipulable object | not detailed on page | not evidenced | yes (save/clear, drop-to-queue) | yes (panel w/ per-item actions) |
| Offline/download | yes ("download… play offline") | implied by paid positioning, not stated | claimed in title tag | yes (下载 in queue actions) |
| Audio-quality tiers | Lossless / Hi-Res / Spatial | HD & Spatial (paid) | not evidenced | HD via client; VIP |
| Lyrics | real-time lyrics; Sing | not evidenced | not evidenced | scrolling lyrics + translation + community reporting |
| Podcasts bundled | not on this page (Apple Podcasts separate) | yes | yes (top-level) | yes (播客 top-level) |
| Music videos | not evidenced | not evidenced | not evidenced | yes (MV in search & queue) |
| Social layer | collaborative playlists, SharePlay | not evidenced | playlist fans/followers | follow graph, user pages, sharing, community lyrics |
| Free tier | no (subscription-only; zero ads) | yes (ad-supported posture) | "free" in title claims | free with VIP membership tier |
| Regional restriction | features region-gated (footnote) | geo-steered storefront | India-focused catalog | China-focused; phone+ID login |
| Live radio programming | yes (named live stations, free-standing) | algorithmic stations | algorithmic stations | radio-program content (djradio) |
| Supply-side surfaces | Apple Music for Artists | not evidenced | not evidenced | 音乐人 portal, 云推歌, creator center |
| Owned-file coexistence | yes (iTunes library access) | not evidenced | not evidenced | not evidenced |

Convergent findings (Layer B):

1. All four organize the world around **recordings as catalog objects** — tracks, albums, artists — regardless of geography or monetization.
2. All four offer **on-demand playback of individually selected recordings** (Apple: stated; Amazon: paid tier stated; JioSaavn/NetEase: player+queue surfaces directly observed).
3. Three of four directly evidence **persistent personal listening state** (library/liked/saved + user playlists + history). Apple additionally evidences per-person state inside a family plan.
4. All four carry **stations/radio as features inside the platform** (live, algorithmic, or both) — without the station being the organizing object. Consistent with the internet-radio sibling's boundary test.
5. Three of four bundle **podcasts** as a separate content class; the fourth (Apple) keeps podcasts in a separate product — podcast presence is a packaging variable, not the music core.
6. Monetization spans both poles: subscription-only (Apple) vs free+premium (Amazon, NetEase; JioSaavn claims free) — **tiering commonly gates on-demand control, offline, and quality** (Amazon explicit; NetEase quality+VIP; Apple offline as subscriber capability).
7. Regional restriction is real and user-visible: geo-block shells (Spotify, Pandora shells observed) and feature-level region gating (Apple footnote); regional catalogs dominate regional products (JioSaavn, NetEase).
8. Quality tiers (lossless/spatial/HD) appear in 3 of 4 as premium features.
9. Social features vary widely — from collaborative playlists (Apple) to follower-counted playlists (JioSaavn) to a full follow graph with community metadata (NetEase) — a spectrum, not a fixed structure.

## Canonical Model (abstraction hierarchy)

### Level 0 — Defining Invariant

Three structures, jointly held. Remove any one and the product stops being a Music Streaming Platform:

1. **A platform-operated catalog of recorded music** — identified recordings organized as tracks within albums within artist discographies, provided by the platform under an access model (not sold as files the buyer owns).
   - remove → a local file player over user-owned files (no catalog = no streaming platform).
2. **On-demand selection and playback of individual recordings** — the listener picks a specific track, album, or playlist and controls playback directly (play/pause, skip, sequence/queue, seek within a recording).
   - remove → the listening object becomes a shared flow chosen by someone else (Internet Radio) or episodic shows (Podcast Platform).
3. **Persistent personal listening state under the listener's identity** — the listener's selections accumulate into durable personal collections (saved/liked tracks, albums, artists; user-built playlists; listening history/queue state) that outlive a session and travel across the listener's devices.
   - remove → an anonymous jukebox; the "your music, anywhere" value proposition of the Type collapses.

Jointly load-bearing:

- catalog without on-demand → station-flow listening (internet radio) or a promo catalog;
- on-demand without a platform catalog → file player;
- catalog + on-demand without personal state → anonymous kiosk, not an account-based platform;
- personal state without on-demand → favorites over a live-flow service (radio favorites).

### Level 1 — Common Mature Structure

Present across the sampled products; not definitional:

- search across catalog (multi-type search where the platform has adjacent content);
- browse/discovery organization: new releases, charts, genres/moods, editorial playlists, artist pages;
- personalized recommendations and auto-generated sequences (personalized suggestions, algorithmic stations/mixes);
- an explicit playback queue as a manipulable object (reorder, save, clear);
- editorial/curated playlists as addressable catalog objects (often with follower counts);
- offline download of catalog content (commonly tier-gated);
- audio-quality tiers (lossless/spatial/HD as premium features);
- multi-surface delivery (mobile app, web player, desktop client, speakers/TVs/car);
- lyrics display;
- account-based identity with the personal state following the listener across surfaces;
- social features in some form (sharing at minimum; collaborative playlists, playlist followers, or follow graphs at the upper end);
- bundled adjacent audio content — podcasts most commonly;
- supply-side artist portals.

### Level 2 — Variant / Optional Structure

- Monetization posture: subscription-only vs freemium (ad-supported free tier with gated on-demand) vs membership tiers with regional billing (VIP).
- Live human-programmed radio inside the platform vs purely algorithmic stations.
- Coexistence with a personal owned-file library (purchased/ripped music living alongside the streaming catalog).
- Music video support; karaoke/sing-along lyric features.
- Regionally-shaped catalogs and social conventions (film-soundtrack-centric catalogs; community-maintained metadata).
- Regional identity/login conventions (phone-first, QR, third-party social login, real-name verification where regulation requires).
- Bundling context: standalone music service vs music inside a retail/telecom/ecosystem umbrella.
- Classical/specialized companion experiences; e-commerce/merchandising attachments; concert discovery; artist-promotion marketplaces.

### Level 3 — Vendor-specific (Research Notes only)

- Apple: Apple Music Sing, AutoMix beat-matched transitions, Music Haptics, Shazam integration, Apple Music Classical companion app with shared library, Apple One bundling, SharePlay/CarPlay DJ sharing, named free-standing live stations (Apple Music 1/Hits/Country/…).
- Amazon: Audible audiobook bundling claims, Alexa-device ecosystem positioning, Free-vs-Unlimited gating copy.
- NetEase: 黑胶VIP (Vinyl VIP) branding, 云推歌 paid promotion service, 商城 store, 我的等级 user levels, 实名认证 real-name verification, community lyrics translation/reporting, 主播/djradio anchor program surfaces.
- JioSaavn: drop-to-queue interaction, "Hindi Radio" station naming, film-soundtrack chart structure.

## Boundary Findings

**vs Internet Radio Platform** (the critical seam — cross-checked against the sibling leaf):
- Both may contain "stations" and both stream audio. The organizing unit decides: internet radio's persistent selectable objects are **broadcast outlets whose output is a shared live flow**; a music streaming platform's persistent selectable objects are **individual recordings the listener selects, sequences, and saves**.
- Music streaming platforms embed stations as *features* (algorithmic stations, live programming) — observed in all four sampled products — but the station never becomes the catalog's organizing object, and nothing is lost if the listener never touches one.
- Conversely, the on-demand legs (individual selection, queue, personal track library) are exactly what an internet radio platform lacks.
- Historical check favors the abstraction: Pandora-style station-first products sit on the radio side even when they stream music; this is the same test the sibling leaf froze.

**vs Podcast Platform**: the organizing unit is episodic shows (subscribe/download/play episodes) vs recordings-as-music. Podcast bundling inside a music streaming platform is common (3 of 4 sampled) but packaging: the platform's music core — catalog, on-demand tracks, personal library — is untouched by whether podcasts ride along. Apple's separation (podcasts in a distinct app) shows the bundling is optional in both directions.

**vs Digital Goods Store (music purchase/download stores)**: a store's loop ends in acquiring files the buyer owns; a streaming platform's loop is playback from the catalog under an access model, with personal collections made of *references* (saved items), not files. The two can coexist in one product (Apple evidences owned-file library access alongside the streaming catalog), but the streaming Type is defined by the access-model loop.

**vs Video Streaming Platform**: media type and organizing unit (moving-image titles/episodes vs audio recordings as tracks/albums). Music videos inside a music platform (NetEase evidences MV search/links) are content variants, not a Type change.

**vs Music Distribution Platform / Music Publishing Management / Royalty Management**: supply-side and rights-side industry systems. Distribution delivers recordings *into* streaming platforms; publishing/royalty systems manage compositions and money *out of* exploitation. The streaming platform is the listener-facing consumption surface; these Types never share the listener's loop.

**vs AI Music Generator / Music Production / DJ software**: creation-side Types. They produce or manipulate recordings; the streaming platform catalogs and delivers finished recordings to listeners. (Generated tracks may *enter* streaming catalogs; the platform stays a catalog.)

**vs Personal Cloud Drive / local file players**: no platform catalog of recordings; content is user-owned files. The personal *library* concept overlaps superficially, but the library of a streaming platform points at platform-catalog recordings under licensing, not at user files.

**Degenerate cases**: a search-and-play demo with no persistent personal state is a jukebox, not this Type; a catalog without playback is a listings site. Both boundary conditions are enforced by the jointly-held L0.

## Uncertainties

1. **Amazon Music's personal library** was not directly evidenced on the fetched page (the page is acquisition-focused). The L0 leg "persistent personal listening state" rests on three directly-observed products (Apple, JioSaavn, NetEase); for Amazon the leg is neither asserted nor denied from evidence.
2. **Free-tier mechanics beyond Amazon** (e.g., shuffle-only mobile free tiers, skip limits, time caps) are widely discussed in the market but were not documentable this pass — no such precise mechanics appear in the final document.
3. **Catalog dynamics** (titles being added/removed from catalogs, "greyed-out" unavailable tracks) are strongly implied by the licensing model and by regional geo-blocks, but no sampled surface stated a catalog-change policy; the final document phrases this qualitatively.
4. **Offline-download rules** (device limits, DRM posture, expiry on lapsed subscription) were not documentable from fetched surfaces; kept qualitative ("download… offline" capability only).
5. **Spotify/YouTube Music/Deezer/Tidal/SoundCloud** are canonical market members; their absence from the direct-evidence set lowers sample breadth on the freemium-market-leader pole and on the creator-upload (UGC) catalog pole. The SoundCloud question — whether a creator-uploaded catalog product still satisfies the L0 — remains formally untested this pass, though conceptually its structure (catalog of recordings + on-demand + personal collections) fits.
6. **Precise catalog sizes** ("100 million songs") are vendor claims from two product pages, reproduced as claims, not verified counts.

## Final Synthesis

A Music Streaming Platform is a listener-facing platform whose world is organized around a **platform-operated catalog of recorded music** — tracks within albums within artist discographies — that the listener accesses rather than owns. Its defining activity is **on-demand**: the listener selects individual recordings (tracks, albums, playlists), sequences them in a queue, and controls playback directly. Its defining accumulation is **personal listening state**: saved and liked recordings, user-built playlists, history — durable state tied to the listener's identity that follows them across devices and sessions.

Around this core, mature products add search, browse/discovery organization, personalized recommendation, offline downloads, quality tiers, lyrics, multi-surface delivery, social features, podcast bundling, and artist portals — none of which define the Type. Monetization spans subscription-only and freemium poles, and the tier structure commonly gates exactly the defining capabilities (degree of on-demand control, offline, quality). The catalog is licensed, so service availability is regional and feature gating by geography is normal.

The boundary with Internet Radio Platform is the organizing-unit test: stations and live flows belong to radio; individually selectable recordings and personal collections belong to streaming. A music platform may embed radio; a radio platform may embed podcasts; neither embedding changes either Type. The boundary with purchase/download stores is the access model: references under a catalog vs files under ownership.

Historical check: 2000s subscription jukebox services, regional platforms (film-catalog-centric, social-heavy, membership-tiered), and platform-ecosystem-native services all satisfy the three-leg definition; nothing in it names an era-specific implementation (no freemium requirement, no mobile-app requirement, no algorithmic-recommendation requirement, no specific billing or identity scheme).
