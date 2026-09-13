# Research Notes — Feed Reader

Research date: 2026-09-07

## Research Goal

Understand what a Feed Reader is as an Application Type — its defining structure, its standard capabilities, its variants — from real products, and hold clean boundaries against the §02.08 sibling leaves (Content Aggregator, Content Curation Platform, Personalized Content Feed) and adjacent Types (Bookmark Manager, Read-it-later, Email Client, News Aggregator, Podcast Platform). Two sibling passes (content-curation-platform, content-aggregator) left explicit joint-review flags that this pass must discharge from this side.

## Initial Boundary

- A Feed Reader (RSS reader; colloquially also "feed aggregator") is an application where a **user manages a subscription list of content sources** and consumes the **items those sources publish**, with per-item reading state.
- Nearest neighbors: Content Aggregator (product assembles the flow), Personalized Content Feed (per-user inference), Content Curation Platform (curated collection as artifact), Bookmark Manager (deliberate one-off capture), Read-it-later (deferred queue), Email Client (inbox resemblance), News Aggregator (news-scoped aggregation), Podcast Platform (enclosure-first), Social Network (follow graph), Web Browser (page-checking; subscription entry surface).
- Vocabulary trap: RSS readers are often colloquially called "feed aggregators"; the sibling pass documented vendors straddling the seam (Feedspot, elink).

## Research Questions

1. What objects exist in a feed reader's world? (source/feed, subscription, item, read state, folders, smart views)
2. Where do items come from — is the machine-readable feed (RSS/Atom/JSON) definitional or just the dominant implementation?
3. What is the subscribe → intake → triage → read → prune loop, end to end?
4. How is state kept (unread/read/starred) and synchronized (local store, cloud service, self-hosted server, sync protocols)?
5. Which rules/behaviors are load-bearing? (item identity/dedupe, item updates, stale-feed health, retention)
6. Which capabilities are common-not-definitional (full-text fetching, filters/rules, search, sharing out, enclosures/podcasts, newsletter intake)?
7. What are the architecture poles (native client / hosted service / self-hosted / multi-user instance)?
8. Boundaries: vs each sibling and adjacent Type — the "who assembles the flow" test, the "collection vs stream" test, the "capture vs standing intake" test.

## Representative Products

Selected for market representation, product-philosophy spread, and customer-tier spread:

| Product | Pole | Tier | Evidence reached |
|---|---|---|---|
| NetNewsWire | free open-source native Mac/iOS client; local store or sync-service client | consumer / enthusiast | Tier 1 — homepage, help index, "What is RSS?", "Get started", "Dinosaurs" article (all fetched) |
| Feedbin | paid hosted reader service; web UI + API for third-party client apps; multi-source intake | paying consumer | Tier 1 — homepage with feature descriptions (fetched) |
| Miniflux | self-hosted minimalist single-user server; unread-centric web app | technical / self-hoster | Tier 1 — homepage + features page (fetched) |
| FreshRSS | self-hosted multi-user aggregator; scraping + filter-generated feeds; WebSub push | technical / self-hoster / groups | Tier 1 — homepage (fetched) |
| (existence evidence only) Feedly, Inoreader, NewsBlur, BazQux, The Old Reader, Feedspot | large SaaS readers / sync services | consumer + business | named as sync services in NetNewsWire's own docs (Layer B); official docs unreachable this pass |

Philosophy spread achieved: native-client vs hosted-service vs self-hosted; minimal vs feature-rich; local vs cloud. The large-SaaS platform pole (Feedly/Inoreader) could not be directly documented (see Source-access Limitation).

## Sources

Tier 1 — official documentation (all fetched 2026-09-07):

- NetNewsWire — https://netnewswire.com/ ; help index https://netnewswire.com/help/ ; "What is RSS? What are feeds?" https://netnewswire.com/help/what-is-rss.html ; "Get started with NetNewsWire 6 for Mac" https://netnewswire.com/help/mac/6.1/en/getting-started.html ; "How to Find Stale Feeds with the Dinosaurs Window" https://netnewswire.com/help/dinosaurs.html
- Feedbin — https://feedbin.com/ (homepage feature descriptions)
- Miniflux — https://miniflux.app/ ; https://miniflux.app/features.html
- FreshRSS — https://freshrss.org/
- RSS Advisory Board — RSS 2.0 Specification https://www.rssboard.org/rss-specification (channel/item model, guid dedupe, enclosure, pubDate, source, ttl/cloud)
- OPML — https://opml.org/ (spec site; "subscriptionList.opml" canonical example; the OPML 2.0 spec page itself returned an unrendered shell — see limitations)

Sibling-pass carry-over (boundary consistency, Layer B):

- research/content-aggregator.md + applications/content-aggregator.md (Feedspot reader pole beside catalogs; elink sells "RSS Feed Reader" as a separate solution page of one product)
- research/content-curation-platform.md + applications/content-curation-platform.md (stream vs collection)
- applications/email-client.md (vs Feed Reader: subscriptions to published content; no addressing, no reply, no envelope)
- applications/bookmark-manager.md (stream intake vs deliberate one-off capture)

Unreachable this pass (1–2 timeouts each, then abandoned): https://feedly.com/ and https://blog.feedly.com/ ; https://www.inoreader.com/ ; https://newsblur.com/ ; https://opml.org/spec2.opml (dynamic shell, no spec body).

## Product Observations

### NetNewsWire (Layer A — directly observed)

Positioning (homepage + help): "free and open source RSS reader for Mac, iPhone, and iPad. It shows you articles from your favorite blogs and news sites and keeps track of what you've read." Tagline: "It's like podcasts — but for *reading*." Anti-model stated explicitly: "Instead of going from site to site in your browser looking for new articles — or relying on big tech social media and their algorithms — let NetNewsWire bring you the news you actually want."

The reader's job, in the vendor's own words ("What is RSS?"): a feed is "a specially-formatted text file that readers like NetNewsWire can read"; "it's NetNewsWire's job to know how to read the feed. And it's NetNewsWire's job to remember which articles you've read and to show you the ones you haven't read. You don't have to go to the websites and check to see if there's something new. You can let NetNewsWire do it." RSS, Atom, and JSON Feed are all handled as equivalent feed formats.

Accounts and sync ("Get started"): single-Mac use needs no account ("On My Mac"); otherwise a "syncing feed account" — the account-type chooser lists iCloud, BazQux, Feedbin, Feedly, Inoreader, NewsBlur, The Old Reader, FreshRSS. Multiple accounts supported; direct feed downloading also supported (no sync at all).

Subscribe flow: "New Web Feed" → "enter the URL for your favorite site or its feed" (a site URL is accepted — feed discovery/normalization is the reader's job); subscribe to Micro.blog feeds; import an OPML file of subscriptions from another reader; Safari-toolbar extension as a subscription entry path.

Reading loop: sidebar of sites; click a site to see its articles or use "Today" to see the latest; click an article to read. Keyboard-first: space (scroll, then next unread), n (next article), z (next subscription), Enter (open in browser), s (mark starred), u (mark unread), k ("mark everything here as read"). Reader View shows "the full article. No need to open it in your browser."

Feed health ("Dinosaurs" window, added in 7.1, June 2026): lists feeds that have not updated in a user-chosen number of months (default six), with feed name, feed URL, account, date of the last article in the app's database, and the last HTTP response code (200 fine; 304 no changes since last check; 404 not found — "A feed can respond with a 404 and not actually be gone"; 410 — "gone for real… a very deliberate choice on the part of a publisher (and super rare)"). "A feed can respond with 200 or 304 and still be finished… It's up to you to judge whether or not these feeds are likely to be finished." Feeds can be deleted from the same window; the Error Log lists download errors (timeouts, DNS failures).

Feature set (homepage): Safari extension for adding feeds; direct feed downloading; syncing via the service list; customizable article themes; Reader view; sharing to Mail, MarsEdit, Micro.blog, Notes, Messages; keyboard navigation; single-key shortcuts; starred articles; "All Unread" and "Today" smart feeds; hiding read articles and read feeds; folders; background refreshing; OPML import/export; searching; multiple accounts.

### Feedbin (Layer A — directly observed, marketing-tier homepage)

Positioning: "A nice place to read on the web. Follow your passions with RSS, email newsletters, podcasts, and YouTube." Paid hosted service (monthly/yearly price stated on homepage).

Multi-source intake (intake substrate broader than RSS): Websites; YouTube (channels and playlists) — "There's no algorithm or confusion about what you have already watched, just the videos from your favorite creators in chronological order"; Newsletters — "Every pro account gets a unique email address to subscribe to and follow newsletters" (email-in intake); Mastodon.

Reading: "clean interface with customizable themes and typography"; fullscreen mode; full-text extraction — "Feedbin can extract the full content of an article for feeds that only offer partial-content. This way you can keep reading without leaving."

Sync-service role: "Feedbin syncs with your favorite iOS, Mac, & Android Apps so you always have something great to read" — third-party clients (Reeder, NetNewsWire, Unread, ReadKit, Airshow) connect to the same account. Feedbin is simultaneously a reader and the synchronization backend for other readers.

Item management: **Actions** — "Using actions, you can automatically star, mark as read or send a push notification on the articles you want" (user rules over incoming items). **Updated Articles** — "Articles are updated whenever the original changes so you don't miss any important changes. You can even see the differences to know what changed." Search — "a powerful and expressive search syntax", with saved searches. Sharing — "Configurable sharing and read-it-later services." Podcasts with playback position ("remembers your place"), plus a native listening app.

### Miniflux (Layer A — directly observed)

Positioning: "Minimalist and Opinionated Feed Reader"; free open-source, self-hosted (single Go binary + PostgreSQL) or paid hosted instance. The overview screenshot is the **unread page** — triage-centric design. "The content is the most important thing. Everything else is just noise."

Formats: Atom 0.3/1.0, RSS 1.0/2.0, JSON Feed 1.0/1.1. OPML import/export and URL import. Multiple attachments supported (podcasts, videos, music, images enclosures); YouTube playable inside. Organization: categories and bookmarks. Public sharing of individual articles. Favicons. Save-to-third-party services. Full-text search (Postgres). 20 languages.

Content handling: fetches the original article and extracts content with a local Readability parser for summary-only feeds; custom scraper rules (CSS selectors); custom rewriting rules; regex filters to include/exclude articles. Privacy machinery: removes pixel trackers, strips tracking parameters from URLs, media proxy, no referrer, blocks external JavaScript.

Integrations: 25+ third-party services (Instapaper, Wallabag, Pinboard, Notion, Slack, Telegram, Discord, Matrix…); bookmarklet "for subscribing to websites directly from any web browser"; webhooks; **compatibility with existing mobile applications using the Fever or Google Reader API** (sync-protocol compatibility layer); REST API with Go/Python clients. Background feed updates via internal scheduler or cron. Authentication: local, passkeys (WebAuthn), OAuth2, OIDC, reverse-proxy.

### FreshRSS (Layer A — directly observed)

Positioning: "A free, self-hostable feed aggregator" (RSS and Atom). Community-hosted instances and cloud providers offered; multi-user capable.

Capability framing (homepage): Syndication — "Follow websites, podcasts and video channels in a single place." Reader — "Read your articles directly in FreshRSS." Search — "Search and save queries for quick access." **Web scraping** — "Generate feeds by scraping external websites" (intake beyond machine-readable feeds). **Feeds generation** — "Generate new feeds based on your filters" (filtered views materialized as feeds). OPML — "Import and export your feeds with OPML." **WebSub** — "Stay connected to your feeds in real-time" (push updates, not only polling). Mobile — with or without third-party apps (APIs). Scale claims: "1M+ articles and 50k+ feeds." Themes & extensions; 15+ languages.

### RSS 2.0 Specification (Layer A — upstream data model)

A feed document = `<channel>` (metadata: title, link, description) + any number of `<item>`s. An item "may represent a 'story' — much like a story in a newspaper or magazine; if so its description is a synopsis of the story, and the link points to the full story. An item may also be complete in itself." Key item elements: title; link (URL of the item); description (synopsis or entity-encoded full content); author; category; comments; **enclosure** (media object with url/length/type — the podcast origin); **guid** ("an aggregator may choose to use this string to determine if an item is new" — item identity/dedupe); **pubDate** ("If it's a date in the future, aggregators may choose to not display the item until that date"); **source** ("The RSS channel that the item came from… Its purpose is to propagate credit for links"). Channel-level `ttl` / `skipHours` / `skipDays` are caching/polling hints; the `cloud` element defines "a lightweight publish-subscribe protocol for RSS feeds" (historical push option). The spec's own term for consuming software is "aggregators" — the vocabulary overlap with the sibling Type is historical, not structural.

### OPML (Layer A on the reader side; spec body not rendered)

opml.org's own example set names **subscriptionList.opml** as the canonical example (alongside directory.opml, category.opml) — OPML is the interchange format for the subscription list. Reader-side confirmation: NetNewsWire (import/export OPML feed lists; "If you use another feed reader… you can import an OPML file of your subscriptions"), Miniflux (OPML import/export and URL import), FreshRSS (import/export feeds with OPML). OPML is the glue that makes the subscription list portable between readers.

## Cross-product Comparison

| Structure | NetNewsWire | Feedbin | Miniflux | FreshRSS | Reading |
|---|---|---|---|---|---|
| User-managed subscription list | yes (sidebar, folders, multiple accounts) | yes (web UI) | yes (categories) | yes (+ saved queries) | **defining** |
| Standing automated intake | background refreshing; direct feed download | server-side (service) | scheduler/cron | scheduler + WebSub push | **defining** (substrate varies) |
| Consumption surface with attribution | sidebar → timeline → article; Reader View; open in browser | web UI; full-text in place; open at source | unread page → article; original fetch | "read directly in FreshRSS"; web apps | **defining** |
| Per-item reading state (unread/read) | central ("remember which articles you've read"; All Unread; k = mark all read) | Actions auto-mark-read; unread machinery implied | unread page is the product's center | unread machinery; scale framing | universal in sample → standard capability; see Uncertainties |
| Starred / saved layer | starred articles | star + share/read-later | bookmarks | bookmarks | standard |
| Folders / categories / tags | folders | (not detailed on fetched page) | categories | categories | standard |
| Smart views (Today / All Unread / saved queries) | Today, All Unread | saved searches | unread page | saved queries | standard |
| Full-content fetching (reader view / readability) | Reader View | full-text extraction | Readability parser | reader surfaces | standard |
| Search over items | searching | expressive syntax + saved searches | full-text (Postgres) | search + saved queries | standard |
| Non-RSS intake (newsletters / YouTube / social / scraping) | Micro.blog feeds; Safari-toolbar add | newsletters (email-in), YouTube, Mastodon | scraper rules; bookmarklet add | web scraping; filter-generated feeds | variant (substrate) |
| Enclosures / podcasts | (not detailed) | podcasts with playback position | enclosures incl. YouTube play | podcasts | variant |
| Rules / filters on intake | (not detailed) | Actions (auto-star / auto-mark-read / notify) | regex include/exclude; scraper/rewrite rules | filter-generated feeds | variant |
| Sync architecture | local (On My Mac) OR client of a sync service (iCloud, Feedbin, Feedly, Inoreader, NewsBlur, BazQux, The Old Reader, FreshRSS) | hosted service + API for third-party apps | self-hosted server + Fever/Google Reader API compatibility | self-hosted multi-user + APIs + WebSub | variant (architecture) |
| OPML in/out | yes | (page silent; ecosystem assumes) | yes | yes | standard (ecosystem glue) |
| Feed-health / pruning surfaces | Dinosaurs window (stale months, HTTP codes, delete); Error Log | (not on fetched page) | (not on fetched page) | (not on fetched page) | deep surface observed in one product; generic need recorded cautiously |
| Anti-algorithm posture | explicit (homepage) | explicit (YouTube copy) | minimalist / no-telemetry framing | community framing | philosophy, not structure |

Anti-overfitting notes:

- Unread state is universal in the sample, but the sample cannot test a stream-without-unread pole; kept out of the defining core.
- Folders/categories are near-universal, but a flat list is still recognizable; standard, not defining.
- RSS/Atom is the dominant intake substrate, but FreshRSS documents web-scraping intake and Feedbin documents email-in / YouTube / Mastodon intake — the machine-readable feed format is an implementation, not the invariant. The invariant is *standing automated intake from the user's chosen sources*.
- Cloud sync is dominant in consumer products, but NetNewsWire runs with no account ("On My Mac") and Miniflux/FreshRSS are self-hosted — sync is not definitional.
- The term "aggregator" appears in the RSS spec itself for consuming software; do not let vocabulary collapse this Type into the Content Aggregator sibling.

## Canonical Model (abstraction layers)

### L0 — Defining Invariant

Three structures. Remove any one and the product stops being a feed reader:

1. **User-managed subscription list** — a durable list of content sources the user personally chooses and maintains (adds, organizes, prunes). The list — not product machinery, not an algorithm, not a curator — decides what enters the surface. Remove → the product assembles the flow for the user (Content Aggregator / Personalized Content Feed territory).
2. **Standing automated intake** — new items arrive from the subscribed sources automatically as the sources publish; no per-item user action and no deliberate capture step. Remove → deliberate one-off saving of links (Bookmark Manager territory).
3. **Consumption surface for arriving items** — the app presents the arriving items, attributed to their sources, for reading in place (full or synopsis) or opening at the source. Remove → subscription plumbing (a feed-to-email/chat forwarder), not a reader.

Minimal statement: *a personal application that holds the user's own list of content sources, continuously pulls in what those sources publish, and gives the user a surface on which to read it.*

### L1 — Common Mature Structure (standard capabilities)

- Per-item reading state: unread / read; per-source and aggregate unread counts; "mark all as read"; keep-unread. Universal in the sampled products and central to their UX.
- Saved layer: starred articles / bookmarks, kept independently of the unread flow.
- Organization: folders, categories, or tags over the subscription list; smart/dynamic views ("All Unread", "Today") and saved searches.
- Full-content handling: reader view / readability extraction so summary-only feeds can be read without leaving; open-at-source as the alternative.
- Search over accumulated items.
- OPML import/export — the subscription list is portable.
- Sharing outward: to read-later services, notes, mail, social targets.
- Sync across devices: cloud service, self-hosted server, or platform sync; compatibility sync protocols (Google Reader API, Fever) exist as ecosystem glue.
- Multi-format feed parsing (RSS, Atom, JSON Feed) and feed-URL discovery from a site URL.

### L2 — Variant / Optional Structure

- Intake substrate beyond RSS/Atom/JSON: email newsletters via a personal email-in address; YouTube channels/playlists; social accounts (Mastodon; Twitter-era integrations attested in community copy); web-page scraping where no feed exists (FreshRSS web scraping, Miniflux scraper rules); filter-generated feeds.
- Architecture poles: local-only native app; client of a hosted sync service; hosted service with its own web reader (Feedbin also acts as sync backend for third-party apps); self-hosted server (single-user minimalist vs multi-user instance).
- Rules/filters over intake: auto-star / auto-mark-read / notification actions; regex include/exclude; scraper and rewrite rules.
- Enclosure-first usage: podcasts and video channels inside a reader; playback with position memory.
- Item-update tracking: some services re-fetch changed articles and show diffs (Feedbin documents this explicitly).
- Business/team layer: shared collections, newsletters out, AI assistance — attested for large-SaaS readers only at Layer B this pass; not directly researched.
- Monetization/deployment: free OSS, paid hosted service, paid hosting of OSS, self-hosted free.

### L3 — Vendor-specific Detail (research notes only)

- NetNewsWire: Dinosaurs window semantics (default six months; 404 vs 410 interpretation; per-feed last-response-code display); keyboard map (space/n/z/Enter/s/u/k); iCloud as a sync backend; AppleScript support; Micro.blog subscription path; © 2002 lineage (historical depth of the native-client pole).
- Feedbin: unique per-account email address for newsletter intake; Actions feature; updated-article diffs; Airshow companion podcast app; homepage price points.
- Miniflux: Go/Postgres stack; Fever + Google Reader API compatibility; Readability parser + CSS-selector scraper rules; tracker removal and media proxy; 20 languages; single-binary deployment posture.
- FreshRSS: WebSub real-time; filter-generated feeds; claimed 1M+ article / 50k+ feed scale; AGPL; extensions ecosystem.
- RSS 2.0: element-level details (guid isPermaLink default true; ttl/skipHours/skipDays; rssCloud interface; source element for credit propagation) — upstream format facts, useful as evidence but not canonical reader behavior.

## Vendor-specific / Rejected Findings

- "Anti-algorithm" is a marketing posture (NetNewsWire, Feedbin), not a structural rule; some products pair the subscription core with optional suggestion/discovery layers (attested for large-SaaS readers via sibling-pass evidence only). Not definitional either way.
- Feedbin's newsletter email-in, Miniflux's regex filters, FreshRSS's feed generation from filters, NetNewsWire's Dinosaurs: each is product-specific depth; none promoted to canonical.
- Precise scale numbers (FreshRSS "1M+ articles", Miniflux "25+ integrations", Feedbin price) are marketing claims recorded here, not in the final document.
- Rejected: defining the Type as "RSS reader" (RSS is one intake implementation; scraping and email-in are documented alternatives). Rejected: defining it by cloud sync or mobile apps (local-only and self-hosted poles pass). Rejected: defining it by unread state (universal in sample but untested against a stream-without-unread pole; placed at standard-capability level).

## Boundary Findings

1. **vs Content Aggregator (§02.08 sibling) — joint-review flag DISCHARGED from this side.** The test is *who assembles the item-level flow*. Reader: the user's own subscription list decides what enters; the reader's job is faithful intake + triage. Aggregator: the product's machinery (editors, scoring, clustering) selects and ranks from a broad source base; the user at most tunes inputs. Evidence: sibling pass documented Feedspot running a subscription reader beside product-assembled catalogs in one company, and elink selling "RSS Feed Reader" and "Content Curation" as separate solutions — the market itself keeps the categories apart. Removal test: replace the user's subscription list with product-side selection → aggregator. Family test now confirmed on all four §02.08 siblings: collection+curator (Curation) / stream+product-machinery (Aggregator) / user-assembled subscription list (Reader) / per-user inference (Personalized Feed).
2. **vs Personalized Content Feed (§02.08 sibling, unprocessed)** — same seam on the inference side: per-user interest inference selects the flow; no explicit user-managed source list is required. Flag remains open for that leaf's pass.
3. **vs Content Curation Platform (§02.08 sibling) — their flag discharged here.** Reader's managed artifact is the *stream* (consumption loop for one person); curation's artifact is a *selectively built collection presented to others*. A reader's saved/starred layer is a personal state, not an audience-facing collection.
4. **vs Bookmark Manager (§02.13)** — consistent with their pass: items arrive automatically and continuously from subscriptions vs deliberate one-off captures. The handoff seam (save an item out of the stream) is standard sharing, not capture-into-reading.
5. **vs Read-it-later Application (§02.09)** — reader = standing intake stream; read-later = deferred-reading queue built from deliberate saves. Products integrate (reader's share/save-to actions) but the primary artifacts differ (stream vs queue).
6. **vs Email Client (§01.02)** — consistent with their pass: inbox-like list is superficial resemblance; no addressing, no reply, no envelope. The interesting seam is newsletter intake: Feedbin turns newsletters into sources (email-in address), which moves mail *into* the reader model rather than the reader becoming email.
7. **vs News Aggregator (§02.04, unprocessed)** — same machinery question as #1 plus scope (news-only). No new evidence this pass; flag stands for that leaf.
8. **vs Podcast Platform (§27, separate leaf)** — readers commonly handle enclosures/podcasts (Miniflux, Feedbin, FreshRSS), and a reader specialized to enclosures shifts the primary job to audio playback, discovery, and show/episode semantics — the market treats that as a distinct Type. Recorded as a substrate-variant at the text/article core; joint review recommended when Podcast Platform is processed.
9. **vs Social Network (§01.05)** — follow graph + product-ordered feed vs user-curated source list + chronological/stateful triage. Social accounts can serve as *sources* (variant intake) without becoming a social network.
10. **vs Web Browser (§02.01)** — browsers check pages and have historically embedded feed-subscription entry points (NetNewsWire's Safari extension is the subscription entry path); the browser holds no standing item store or reading state. The reader, not the browser, owns the subscription list and its state.
11. **Historical check (older / platform-native / regional products)** — the three-part L0 holds for: local desktop readers with no account (NetNewsWire's own "On My Mac" mode); platform-synced clients (iCloud account in NetNewsWire); self-hosted multi-user servers (FreshRSS); pre-modern readers of the RSS/Atom era (the RSS spec itself, frozen, describes channel/item/guid semantics that early aggregators implemented). What would *not* qualify: a hand-edited "what's new" page checked manually (no standing intake — pre-feed era, correctly excluded), and product-assembled headline pages (aggregator sibling). The L0 deliberately does not require: RSS as format, cloud sync, unread tracking, mobile apps, or AI — so regional/minimal/historical readers fit.

## Uncertainties

- **Large-SaaS pole unreached**: Feedly, Inoreader, NewsBlur official docs timed out (2 attempts each domain, abandoned). Their existence and reader/sync-service role are Layer B (named in NetNewsWire's docs; Feedspot reader documented in the sibling pass). Business/team and AI features of that pole are NOT asserted anywhere in the final document. If a later pass reaches them, re-check whether "team/business sharing" deserves a variant entry with stronger wording.
- **Unread-state placement**: universal in the sample (4/4) and central to every fetched UX, but the sample could not test a "river of news" style reader without unread tracking (no official doc reachable for such a pole this pass). Placed at standard-capability level, not defining. A future pass could re-test.
- **OPML spec body** not rendered (dynamic page); OPML evidence is reader-side (A layer: three products document import/export) plus the spec site's canonical example name. Format-internal details not asserted.
- **Newsletter/YouTube/social intake breadth**: Feedbin documents newsletters/YouTube/Mastodon; FreshRSS documents scraping; Miniflux documents scraper rules + Fever/GReader API. Whether *most* modern readers accept non-feed sources is unknown; written as variant, not standard.
- **Feed-health surfaces** (stale-feed listing) observed deeply in one product only; the *generic* need (subscriptions die; user prunes) is cross-product plausible but only NetNewsWire documents a dedicated surface. Kept cautious in the final document ("some products surface stale feeds").
- **Podcast Platform joint review** pending on that leaf's pass (see Boundary Finding 8).

## Final Synthesis

The Feed Reader is the *user-assembled* member of the feeds-and-curation family: its center is the user's own subscription list, its engine is standing automated intake from those sources, and its purpose is a personal reading surface over the arriving items with per-item state. Everything else — folders, unread counts, stars, full-text fetching, search, OPML, sync architectures, rules, enclosures, newsletter intake — is mature standard structure or variant implementation. The Type is distinguished from the Content Aggregator by who assembles the flow (user's list vs product machinery), from the Bookmark Manager by standing intake vs deliberate capture, from the Curation Platform by stream-for-self vs collection-for-others, and from the Email Client by the absence of envelope semantics. Its minimal historical form (local desktop reader, RSS/Atom only, no account) satisfies the same definition as its modern cloud form, which is the strongest sign the abstraction is not over-fit to the current market.
