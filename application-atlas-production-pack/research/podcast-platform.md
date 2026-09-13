# Research Notes — Podcast Platform

## Research Goal

Understand the real structure of the products the market calls "podcast platforms" — the listener-facing consumption side (apps, directories, players), the creator-facing publishing side (hosting, distribution), and the two-sided products that span both — and produce a vendor-neutral Application Document that explains what this Type is, what exists inside it, how work flows, and where its boundaries lie.

This pass also carries five pre-hung joint-review flags to discharge (from podcast-editing-application, music-streaming-platform, internet-radio-platform, social-audio-platform, feed-reader).

## Initial Boundary

Working hypothesis before research:

- A Podcast Platform is the listening/distribution side of podcasting: shows, episodes, subscription/follow, playback, discovery — not the production side (Podcast Editing Application territory).
- Nearest neighbors: Music Streaming Platform (on-demand audio, but tracks not episodic shows), Internet Radio Platform (audio flow, but live not on-demand), Social Audio Platform (audio, but live rooms), Feed Reader (subscription-to-source + arriving items, but text-first), Podcast Editing Application (same subject matter, production side).
- Known ambiguity: the market uses "podcast platform" for both listener apps and hosting platforms. The directory has one leaf (§27) and no separate hosting leaf (unlike music, which has both Music Streaming Platform and Music Distribution Platform).
- Unknowns: whether the canonical core must include the publishing/hosting side; how closed-delivery platforms (Spotify exclusives) affect the feed-centric model; where private/paid feeds sit.

## Research Questions

1. What is a show? What is an episode? What identity/metadata do they carry?
2. How do shows enter a platform? (RSS submission, hosting, directory review)
3. What exactly is the listener's "follow/subscribe" relationship, and what does it trigger?
4. What is the playback model? (on-demand selection, queue, position memory, downloads, offline)
5. What is the delivery substrate? (RSS feeds; open federation vs platform-internal delivery)
6. How do private and paid feeds work?
7. What does the supply side look like? (hosting, distribution, analytics, monetization)
8. Where are the boundaries vs music streaming, radio, social audio, feed readers, editing applications, and bare directories/search engines?
9. Would older/regional/platform-native products still fit the definition? (historical check)

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer levels — deliberately spanning the three product shapes the market realizes:

1. **Apple Podcasts** — platform-native consumption platform + catalog + creator console (Apple Podcasts Connect). Free core + paid creator subscriptions. The catalog that third-party apps reference.
2. **Spotify** — music-bundled two-sided platform; closed-delivery variant (exclusives); free + Premium; Spotify for Creators on the supply side.
3. **Pocket Casts** — independent dedicated podcatcher (open-RSS consumption platform); freemium (Plus); no hosting.
4. **Transistor** — publishing-platform pole: hosting + distribution + analytics for creators/organizations; no listener app; paid SaaS.

Rejected/considered: Overcast, Podcast Addict, AntennaPod (listener-only, would duplicate Pocket Casts' shape); Podbean, Spreaker, Castbox, Acast, Buzzsprout (two-sided/hosting candidates — fetches failed, see Sources); Libsyn (legacy hosting pole, not fetched).

## Sources

Fetched 2026-09-09 (Tier 1 unless noted):

- Apple Podcasts product page: https://www.apple.com/apple-podcasts/
- Apple Podcasts for Creators: https://podcasters.apple.com/ ; support index: https://podcasters.apple.com/support/
- Apple — "How Apple Podcasts distributes your shows to listeners": https://podcasters.apple.com/support/5108-how-apple-podcasts-distributes-your-shows-to-listeners
- Apple — "Follow on Apple Podcasts": https://podcasters.apple.com/support/3298-follow-on-apple-podcasts
- Spotify — "Podcasts and shows": https://support.spotify.com/us/article/podcasts/
- Spotify — "Podcast paid subscriptions": https://support.spotify.com/us/article/podcast-paid-subscriptions/
- Pocket Casts Help Center: https://support.pocketcasts.com/
- Pocket Casts — "Following / Subscribing to Podcasts": https://support.pocketcasts.com/knowledge-base/subscribing-to-podcasts/
- Pocket Casts — "Submitting Podcasts": https://support.pocketcasts.com/knowledge-base/submitting-podcasts/
- Pocket Casts — "Auto Downloading Episodes": https://support.pocketcasts.com/knowledge-base/auto-downloading-episodes/
- Transistor homepage: https://transistor.fm/
- Transistor — "Distribution": https://transistor.fm/features/distribution/

Failed fetches (abandoned per network rules; recorded as sourcing limitations):
- Podbean (www.podbean.com, help.podbean.com — timeout ×2), Buzzsprout (www.buzzsprout.com — timeout; help center not attempted after), Spreaker (timeout), Castbox (timeout), Acast (timeout), Apple Podcasts User Guide (support.apple.com/guide/podcasts — 404), Apple "Submit a new show" article (404), Apple "serial vs episodic ordering" article (timeout), pocketcasts.com/podcast-producers (empty response).

Consequence: the two-sided product shape is evidenced through Spotify's own structure (listener app + Spotify for Creators + private-RSS fulfillment) rather than through a dedicated two-sided vendor (Podbean/Spreaker class). Claims about that shape are held at moderate strength.

## Product Observations

### Apple Podcasts (evidence layer: A — direct, official docs)

**Listener side (product page):**
- Self-description: "the app built just for podcasts… finding, following, and listening to millions of the world's most popular podcasts."
- Discovery: expert curation, Channels (all shows from a creator in one place), Top Charts, personalized recommendations ("You Might Like"), editorial collections.
- Playback: video podcasts (full screen, PiP, adaptive quality), transcripts (read along, search, tap-to-jump, chapters), Enhance Dialogue, variable speed with per-podcast saved settings, skip controls.
- Follow + downloads: "You can download any podcast episode and listen to it offline. New episodes from shows you follow will be automatically downloaded."
- Paid: Apple Podcasts Subscriptions — "unlock ad-free listening, bonus content, unreleased episodes… from your favorite shows and creators"; can also connect App Store / Apple News+ / Apple Music subscriptions; Family Sharing.
- Multi-surface: iPhone, Mac, iPad, Watch, TV, Vision Pro, CarPlay, HomePod, web (podcasts.apple.com), smart speakers, cars.

**Distribution model (support 5108 — the load-bearing document):**
- "There are two ways to distribute your shows to listeners through Apple Podcasts."
  1. **Publish to the Apple Podcasts catalog** — submit via Apple Podcasts Connect (RSS feed hosted by a third-party provider) or via a hosting provider dashboard. Catalog shows are "public, searchable, and shareable," available in 170+ countries "as well as third-party podcasting services that reference the Apple Podcasts catalog."
  2. **Publish an RSS feed URL that listeners can add to their Libraries directly** — "listeners can input an RSS feed URL to add a show directly to their own Library… they will follow the show directly from the hosting provider, not the Apple Podcasts catalog."
- Feed URL types: public; **private** — "personalized, so that each user has access to their own specific feed; password-protected…; and authenticated, so that only active paying subscribers can continue to access new content." Private feeds must use the `<itunes:block>` tag so the public directory cannot process them.
- Catalog as industry spine: "Some popular third-party podcasting services that reference the Apple Podcasts catalog include… Podcast apps or 'podcatchers,' including Overcast and Pocket Casts." Third parties integrate via the iTunes Search API.
- Shows followed via raw RSS URL lose catalog benefits: no discovery/recommendations/charts/featuring/ratings/reviews/subscriptions/channels/analytics.
- Subscriber episodes distributed via Apple Podcasts Subscriptions are DRM-protected and only available on Apple Podcasts; free episodes distributed by RSS "remain free and available everywhere."
- Availability configuration: shows default to all countries + third-party services referencing the catalog; creators can opt out of third-party distribution.
- Creator console (Apple Podcasts Connect): submit new show / claim existing show; review process before availability; statuses; RSS feed refresh; change feed URL; archive/restore channel/show/episode; transfer ownership; channels (multiple shows in one place); users and access roles; hosting-provider partner search ("Find a hosting provider. Experts that can help get your show on Apple Podcasts"); Apple Creator Studio (production essentials).

**Follow model (support 3298):**
- "Listeners can follow shows to automatically download and receive notifications for new episodes and, with Apple Podcasts Subscriptions, subscribe to shows and channels to support creators and unlock premium experiences."
- Followers vs subscribers distinction: followers follow free; subscribers purchase.
- "When a user decides to follow your show, they'll automatically download and be notified of all new episodes, which appear in the Listen Now and Library tabs."
- **Playback sync:** "When users follow a show or save an episode to their Library, playback position for each episode is preserved and synced across all of their devices."
- **Up Next queue:** "Apple Podcasts presents the best episode to your followers in their Up Next queue. When users follow episodic shows, the most recent episode is automatically downloaded and added to Up Next. For serial shows, the first three episodes of the most recent season are downloaded and added to Up Next." (Shows carry an episodic-vs-serial ordering mode.)
- Charts update with follows/engagement. Subscribing from a show page implies following; subscribing from a channel lets the user choose shows.
- Creator analytics: followers per show, net new followers over time, time listened split following vs not following; "downloads versus followers" divergence explained (play-without-following adds downloads; multi-device plays; auto-download paused for disengaged followers; inactive followers not counted).

### Spotify (evidence layer: A — direct, official docs)

**Listener side ("Podcasts and shows"):**
- Podcasts are a content class inside the music app: "Listen to your favorite podcasts, and discover many more including shows with music."
- "Get recommended and featured podcasts and shows. **Save the podcasts and shows you like. New episodes then automatically save.** Download to listen offline. Some episodes feature videos too."
- Flow: Search → Browse All → Podcasts → featured episodes / categories → show page → all available episodes → play. Playback speed control; skip forward/back 15s; Now Playing actions: info, download, share, add to Play Queue.
- **Follow:** "Select FOLLOW on a page to save it to Your Library under Podcasts." Episodes can be saved to "Your Episodes" playlist or other playlists. Home → Podcasts → Following shows latest episodes of saved shows.
- Downloads: per-episode; "You may need Premium to download some shows."
- Ads: tier-dependent. "Spotify ads are promotional messages… inserted dynamically into podcast episodes by Spotify." Plus "creator sponsorships" (baked-in host reads, branded editorial segments, product placement). Premium removes Spotify ads on video podcasts but creator sponsorships remain.
- Supply side: "Get a podcast on Spotify → Spotify for Creators."

**Paid subscriptions ("Podcast paid subscriptions"):**
- "Support your favorite podcasters and get exclusive content in return by subscribing to their shows, with Spotify for Creators and Spotify." Subscription-only shows carry a lock icon.
- "Podcast paid subscriptions are independent from Spotify Premium subscriptions."
- **Fulfillment is feed-based:** "To unlock the podcast and listen, either: Tap Activate on Spotify, or copy the **Private RSS Link** and paste it into **any podcast app**."
- Auto-renewal; cancel via monthly email link; access continues until renewal date, then locked again.

### Pocket Casts (evidence layer: A — direct, official docs)

**Discovery and follow ("Following / Subscribing to Podcasts"):**
- "The Pocket Casts podcast database includes over a million shows."
- Discover tab: dynamically generated sections (Featured, Trending/Top 100, Popular, You Might Like, Loved by listeners of, If you like) plus human-curated sections (Guest Lists, Network Highlights).
- Search by podcast name, network, author, **or feed URL/RSS feed**.
- "Once you've found the show you'd like to follow, tap the + or follow icon to add it to your podcast collections."
- **"You can play episodes without following a podcast"** — stream or download straight from Discover; played episodes land in Profile > Listening History, downloads in Profile > Downloads.

**Ingestion and the feed ("Submitting Podcasts"):**
- "Anyone can submit podcasts to our platform" via the in-app search bar or the submission form; accepted inputs: **podcast RSS feed URL** or Apple Podcasts link.
- Feed validity checking (own form errors; W3C feed validator; third-party validators suggested).
- **Private feeds:** a feed containing `<itunes:block>Yes</itunes:block>` "is classified as 'private,' so it will not show up in our public search database. Private podcasts cannot be shared…; to let someone listen, give them the podcast's RSS feed URL so they can add it to Pocket Casts themselves."
- Password-protected feeds supported (dedicated article "Private and paid podcast feeds").
- **Direct-URL consumption:** the web player accepts `https://pocketcasts.com/follow/<feed_url>` — "opens that podcast's page in the web player. It works whether or not the podcast appears in our public directory."
- Publishing frequency shown on a show page is **computed automatically from the feed's recent episode cadence** — no frequency field exists in the feed.
- Duplicate-listing safety check on title/author/website/thumbnail (free vs members-only feeds).

**Playback machinery ("Auto Downloading Episodes"):**
- Auto-download scopes: Up Next episodes; all new episodes (per-podcast selection, with quantity limits); On Follow (latest episodes of any newly followed show); per-playlist.
- Guards: Only-on-WiFi restriction; Android "Only when enough storage" (default on); download management (stop all, clear errors, auto-delete via archiving).
- Other documented machinery: sync account (cross-device), OPML export, starring episodes, sleep timer, skip controls, YouTube channels as followable sources, family sharing, Plus paid tier.

### Transistor (evidence layer: A — direct, official product pages; help center not fetched)

**Positioning:** "Transistor.fm provides podcast hosting and analytics for thousands of organizations, brands, and creatives." Publishing-platform pole: no listener app; the product is the show/episode system of record and the distribution machinery.

**Hosting:** unlimited shows per account; video podcast hosting; private podcasts ("Host a members-only podcast for your company or online community"); team collaborators; AI transcription; website builder per show; network websites; embeddable player; dynamic ad insertion (pre/mid/post-roll); API.

**Distribution (features/distribution — the load-bearing document):**
- The supply chain, verbatim: "1. Upload your audio and publish your podcast episode. 2. Transistor will update your podcast's RSS feed. 3. **Podcasting apps & aggregators detect a new episode in your feed and download it from Transistor's servers.**"
- Submission targets, one click: directories (Spotify Podcasts — "We'll submit your show for inclusion in the Spotify Podcast directory… and pull in analytics every morning"; Apple Podcasts — "Add a podcast to the Apple Podcasts directory using your Apple ID. **Many podcasting apps also pull information from Apple**"), search indexes (The Podcast Index — "An alternative to Apple's podcast directory"; Listen Notes — "a popular podcast search engine"), and apps/aggregators (Player FM, Podcast Addict, Deezer, Amazon Music, Podchaser, Overcast, Pocket Casts, Castro, Castbox, Goodpods, TuneIn, Anghami, Fountain, RadioPublic, Pandora, iHeartRadio, SoundCloud).
- FAQ: "Do I need to upload my podcast to each platform separately? No, you only need to upload your audio to your hosting provider. Platforms like Apple and Spotify will read your RSS feed and update their directories." Apple still requires manual feed submission.
- Video: "Upload your video once, and we'll distribute it to YouTube, Apple Podcasts, Spotify, and your podcast's RSS feed (in any podcast app that supports video)." Same feed carries audio+video.
- Analytics: "average downloads per episode, popular podcast apps, number of subscribers, trends."
- Pricing tiers meter private podcast subscribers and monthly downloads (plan-specific numbers kept out of the final document).

## Cross-product Comparison

| Dimension | Apple Podcasts | Spotify | Pocket Casts | Transistor |
|---|---|---|---|---|
| Product shape | consumption platform + creator console (platform-native) | two-sided, music-bundled | consumption platform (independent) | publishing platform (hosting/distribution) |
| Unit of record | show → episodes; channels group shows | show ("podcasts and shows") → episodes | show ("podcast") → episodes | show → episodes (unlimited shows per account) |
| Delivery substrate | RSS from third-party host; catalog submission OR direct URL follow; DRM for subscriber episodes | platform-internal delivery; **private RSS link fulfillment for paid shows** | RSS ingestion (search bar/form); direct feed-URL consumption | RSS feed of record; apps pull from it |
| Follow semantics | follow = auto-download + notifications; appears in Listen Now/Library | follow = saved to Library; "new episodes then automatically save" | follow = added to podcast collections; auto-download configurable (incl. On Follow) | n/a (no listener side) |
| Playback | on-demand; position synced across devices; Up Next queue (episodic vs serial behavior) | on-demand; speed; skip; Play Queue | on-demand; queue; speed/skip/sleep timer; streaming or download | n/a (embeddable player for websites) |
| Discovery | editorial curation, channels, charts, recommendations, Search/Siri | featured, categories, recommendations, search | Discover sections (dynamic + human-curated), search incl. feed URL | n/a (directories are the discovery layer) |
| Episode state | played/unplayed/downloaded/saved filters (iOS 15.4+ noted in news) | saved episodes (Your Episodes playlist), downloads | new/played, downloaded, starred, archived | n/a |
| Offline | downloads; auto-download of followed shows' new episodes | downloads (Premium-gated for some shows) | downloads; auto-download with WiFi/storage guards | n/a |
| Private/paid feeds | private/personalized/password/authenticated feeds; `<itunes:block>`; DRM subscriber episodes | paid shows fulfilled via private RSS link usable in any app | `<itunes:block>` private feeds; password-protected feeds; direct URL | private podcasts with per-subscriber provisioning; paid tiers meter subscribers |
| Monetization | Apple Podcasters Program subscriptions (creator-set prices; platform revenue share) | podcast paid subscriptions (independent of Premium); dynamic ads + creator sponsorships | Plus consumer tier (app features) | SaaS plans; dynamic ads insertion |
| Supply-side analytics | followers, time listened, downloads vs followers, listening reports | via Spotify for Creators | featuring/analytics for podcasters (page not fetched) | downloads per episode, popular apps, subscribers, trends |
| Catalog role | the reference catalog third-party apps query (iTunes Search API) | own closed catalog + exclusives | own public directory over ingested feeds | submits into others' directories |

**Cross-product commonalities (evidence layer B):**
- Show → episode hierarchy as the universal unit structure; episodes arrive over time under a persistent show.
- A standing listener→show relationship (follow/subscribe) that makes new episodes arrive automatically (auto-download / auto-save / notifications) — present in all three listener-side products.
- On-demand episode selection and playback with per-episode position memory (Apple explicit; Pocket Casts via sync machinery; Spotify implicit in product behavior — held B).
- The feed as the delivery substrate in every sampled product (Apple's two distribution paths are both RSS; Pocket Casts ingests feeds; Transistor's product IS the feed; Spotify's paid fulfillment is a private RSS link) — with platform-internal delivery coexisting for exclusive content.
- Discovery machinery (search + browse + charts/editorial/recommendations in some combination).
- Downloads/offline as a first-class episode state.
- Supply-side machinery: directory submission, creator analytics, monetization.

## Canonical Model

### L0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being recognizable as a Podcast Platform:

1. **The show as the unit of record.** A persistent, identified episodic series — title, artwork, publisher/author, description — under which episodes accumulate over time. The show is the addressable object of the whole system: platforms list it, listeners follow it, creators publish into it. Remove → a music catalog (recorded works, not episodic series) or a loose audio file store.

2. **The standing follow relationship between listener and show.** The listener holds a personal list of followed shows; new episodes of followed shows arrive automatically (auto-download, auto-save, notifications). Subscription is show-level: follow once, future episodes come to you. Remove → an audio search engine / directory / one-off player (lookup without a standing relationship or arrival).

3. **On-demand episodic playback under the listener's control.** The listener chooses specific episodes and controls playback directly — play, queue, skip, resume. Consumption is listener-scheduled, not flow-scheduled; long episodes are consumed across sessions (position remembered per episode in mature products). Remove → a live flow (Internet Radio) or a live room (Social Audio).

Jointly-held load-bearing tests:
- 1 alone = show database/directory (Podchaser/Listen Notes-class metadata corpus)
- 2 alone = subscription plumbing with nothing to play
- 3 alone = bare audio player
- 1+2 without 3 = an audio feed reader (arrival without playback-centered consumption)
- 2+3 without 1 = a playlist of loose episodes, no shows
- 1+3 without 2 = an on-demand catalog without the standing relationship (one-off listening surface)

### L1 — Common Mature Structure

- **The feed as delivery substrate.** The show's publication stream — universally realized as RSS in the sample. Open federation: any app can consume any public feed; directories are views over ingested feeds; direct-URL follow bypasses directories; private/password/authenticated feeds serve internal and paid audiences. Platform-internal closed delivery (exclusives) coexists as a variant. (Universal in sample; held L1, not L0, because a closed-delivery platform remains recognizable — see Spotify.)
- Discovery machinery: search, browse categories, charts, editorial curation/collections, personalized recommendations.
- Episode state machinery: new/unplayed/played, downloaded, saved/starred, archived.
- Auto-download + new-episode notifications (configurable, pausable).
- The queue (Up Next) as an explicit manipulable object; show-ordering modes (episodic vs serial) shape what enters it.
- Playback controls: speed, skip forward/back, sleep timer; per-show settings.
- Offline downloads as a first-class episode state.
- Show page + episode list as the primary browsing surface; personal library (followed shows, downloads, history).
- Cross-device sync under a listener account.
- Ratings & reviews; sharing (links, embeddable players).
- Supply side: directory submission, creator analytics (downloads, followers, apps), monetization (paid subscriptions, dynamic ad insertion, sponsorships).
- Current-generation layers: transcripts, video podcasts, chapters.

### L2 — Variant / Optional Structure

- Product shape: consumption-only / publishing-only / two-sided.
- Delivery posture: open-RSS federation vs platform-internal closed delivery (exclusives) vs hybrid.
- Monetization model: free / freemium app tiers / paid creator subscriptions / ad-supported / SaaS hosting fees.
- Private-podcast deployments (companies, communities, paid subscriber feeds, personalized per-user feeds).
- Video podcasts (same show/episode structure, video media).
- Live integration (live rooms attached to a podcast platform — social-audio seam).
- Bundling: music (Spotify), radio (TuneIn/iHeart class), video platforms (YouTube as a podcast surface).
- Regional/language scope; platform-native vs cross-platform apps.

### L3 — Vendor-specific (research notes only)

- Apple: Apple Podcasters Program; channels; Apple Creator Studio; DRM on subscriber episodes; iTunes Search API; `<itunes:block>` tag; holiday delivery deadlines; 70%/85% creator revenue share; Enhance Dialogue; serial shows' first-three-episodes Up Next rule; CarPlay/HomePod/Vision Pro surfaces; Family Sharing.
- Pocket Casts: Plus tier; getrssfeed.com extraction tool; `pocketcasts.com/follow/<url>` scheme; "Only when enough storage" Android default; publishing-frequency computation from feed cadence; duplicate-listing check fields (title/author/website/thumbnail).
- Spotify: dynamic ad insertion formats (baked-in host reads, branded editorial segments, product placement); "Your Episodes" playlist; Premium gating of some downloads; private-RSS-link fulfillment flow; cancel-via-monthly-email flow.
- Transistor: plan-metered downloads/private subscribers; HLS video partnership with Apple; MCP server; podcaststandards.org involvement; network websites.

## Vendor-specific Findings

- The Apple Podcasts catalog functions as the industry's reference directory: third-party podcatchers (Overcast, Pocket Casts — named by Apple itself) query it via the iTunes Search API; Transistor tells creators "many podcasting apps also pull information from Apple." A single-vendor artifact with industry-wide structural role — documented, but not generalized into the Type's definition.
- Spotify's paid-subscription fulfillment via a private RSS link consumable in any app shows the open-feed architecture surviving inside a closed platform — strong evidence that the feed is the medium's substrate even where delivery is platform-internal.
- Pocket Casts computes a show's publishing frequency from observed feed cadence — a directory-side derived attribute, not feed metadata.
- Apple's follower analytics explicitly reconcile downloads (host-reported) vs followers (platform-side) — evidence that the platform's follow graph and the host's download counts are distinct measurement planes.

## Rejected Findings

- "Podcast Platform = RSS reader for audio." Rejected: the playback-centered consumption loop (queue, position, downloads, show pages) and show/episode semantics, not feed parsing, are the center. Feed handling is the substrate, not the job. (Symmetric to the feed-reader pass's finding.)
- "Subscription requires payment." Rejected: follow (free, automatic arrival) is the base relationship in all sampled products; paid subscriptions are a distinct layer on top (Apple: followers vs subscribers; Spotify: paid subscriptions independent of Premium).
- "Podcasts are audio-only." Rejected: video podcasts are documented in three of four samples (Apple, Spotify, Transistor) inside the same show/episode structure; audio-primary, not audio-exclusive.
- "The platform must host the audio." Rejected: consumption platforms consume feeds they don't host; hosting platforms host feeds they don't play. The Type spans the delivery chain; hosting is a shape, not the invariant.
- "Charts/editorial curation are definitional." Rejected: discovery machinery varies widely (Transistor has none; Pocket Casts' is dynamic+curated; Apple's is editorial-heavy). It is L1.

## Boundary Findings

1. **vs Podcast Editing Application** — DISCHARGES the pre-hung flag from the podcast-editing pass. Seam: **production vs distribution/listening.** Test ratified from this side: remove production tools → the product remains on the platform side (the publishing-platform shape: feed hosting, distribution, analytics — Transistor-class); remove hosting/distribution → the product remains a Podcast Editing Application (export-only editors). Products attaching both (editing products with built-in hosting) straddle by packaging; the center of gravity (making episodes vs delivering/consuming them) decides. Keep-both ratified.

2. **vs Music Streaming Platform** — DISCHARGES the music pass's adopted seam ("episodic shows = Podcast Platform"). Seam: **unit of consumption.** Music: individual selectable recordings (tracks/albums/playlists) pulled from a catalog; Podcast: episodic shows whose new episodes arrive to a standing follower. Bundling is packaging in both directions (Spotify bundles podcasts into the music app; podcast platforms don't become music services by adding music). Consistent with the music pass's own related-types row.

3. **vs Internet Radio Platform** — consistent with the radio pass's adopted seam. Seam: **live continuous flow vs on-demand episodes.** The station (broadcast outlet) is the radio unit; the show (episodic series) is the podcast unit. Radio platforms commonly bundle podcasts and vice versa without merging the Types.

4. **vs Social Audio Platform** — DISCHARGES the social-audio pass's flag. Seam adopted from that side and ratified: **the live participatory room as primary surface = Social Audio Platform; the distributable recording as primary object = Podcast Platform.** A podcast platform may carry recorded replays of live rooms as episodes; a social-audio product may distribute episodes; the primary object decides.

5. **vs Feed Reader** — DISCHARGES the feed-reader pass's flag. Seam: **primary job.** Shared substrate (subscription-to-source + arriving items) but different centers: the reader's job is text-oriented reading with per-item reading state; the podcast platform's job is audio playback with show/episode semantics (queue, position, downloads). Enclosure handling is secondary in readers; text (show notes, transcripts) is secondary in podcast platforms. An enclosure-first reader whose primary job has shifted to audio playback belongs to this Type — consistent with the reader pass's own formulation.

6. **vs audio search engines / podcast directories (Listen Notes, Podchaser class)** — no directory leaf exists for these. A metadata corpus + search without the standing follow/playback loop is search/directory territory (Vertical Search Engine / Directory Application family). The follow+playback loop is what makes a platform a platform rather than a lookup surface. Recorded as a boundary note, not a Type split.

7. **Taxonomy gap (recorded, not resolved):** podcast hosting/distribution platforms (Transistor, Libsyn, Buzzsprout, RSS.com class) have no dedicated directory leaf — unlike music, which has both Music Streaming Platform and Music Distribution Platform. This pass documents them as the publishing-platform shape of the Podcast Platform's territory (consistent with the podcast-editing pass's seam test). If the taxonomy is later refined, a "Podcast Hosting/Distribution Platform" leaf sibling to Music Distribution Platform would be the natural home; until then they are covered here.

## Historical / Market-Sample Check

- **2005 founding generation** (podcatcher clients + iTunes Podcast Directory 4.9): shows as RSS feeds, subscribe-to-show, on-demand playback in a media player, a browsable directory. Satisfies all three L0 legs with no charts, recommendations, apps-ecosystem, video, transcripts, or monetization machinery. The definition holds.
- **Pre-RSS conceptual lineage:** serial audio distributed as physical media on subscription (cassette-of-the-month style audio magazines; radio programs distributed as recordings) satisfies the conceptual core — show, episodic arrival, standing relationship, on-demand playback — with entirely different delivery machinery. Held as conceptual lineage (not directly evidenced from fetched sources), consistent with the medium's own self-descriptions.
- **Regional/platform-native products:** regional podcast apps and platform-native apps (device-bundled) satisfy the core without any specific discovery or monetization machinery.
- **Closed-delivery platforms:** Spotify-exclusive shows (platform-internal delivery, no public feed for those shows) still satisfy the consumption core — confirming the feed is the common architecture, not the invariant.

Conclusion: the L0 is not an artifact of the current app generation. The definition names no RSS version, no app form, no monetization model, no discovery mechanism.

## Uncertainties

- **Two-sided products (Podbean/Spreaker/Acast/Castbox class):** none could be fetched. The two-sided shape is evidenced structurally through Spotify (listener app + Spotify for Creators + private-RSS fulfillment) and through Apple's creator console, but a dedicated two-sided vendor's documentation was not observed. Claims about that shape are held at moderate strength; no precise claims made.
- **Position memory on Spotify:** universal product behavior but not explicitly documented in the fetched articles; held as cross-product commonality (B), with Apple as the explicit Tier-1 source (A).
- **Paid-subscription mechanics depth** (grace periods, billing retry, pricing changes): Apple documents these; the final document deliberately stays conceptual.
- **Whether every consumption platform maintains its own directory:** Pocket Casts and Apple do; some apps rely entirely on the Apple catalog (per Apple's own description of third-party podcatchers). The directory-maintenance role is held as common, not invariant.
- **Live-room integration inside podcast platforms** (e.g., platforms attaching live broadcasting): observed in market (Spreaker-class) but not fetched; held as a variant with low confidence, no claims made in the final document beyond the social-audio seam.

## Final Synthesis

A Podcast Platform is the venue where episodic audio shows live as records and reach listeners. Its defining core is three structures held jointly: the show as the persistent unit of record (episodes accumulating under it), the standing follow relationship that makes new episodes arrive into the listener's library automatically, and on-demand episodic playback under the listener's control with remembered position. The feed — universally RSS — is the delivery substrate that lets shows publish once and reach every app and directory; platforms occupy different stations of that delivery chain (consuming feeds, operating them, or both), which is why the market realizes the Type as consumption platforms, publishing platforms, and two-sided platforms. Discovery, downloads, queues, transcripts, video, monetization, and creator analytics are the mature capability set around this core. The Type is bounded from production (Podcast Editing Application), from recorded-music consumption (Music Streaming Platform), from live flows (Internet Radio), from live rooms (Social Audio), and from text-first subscription reading (Feed Reader) by the unit-of-record / primary-object / primary-job tests ratified with each counterparty pass.
