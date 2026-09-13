# Research Notes — Content Aggregator

Research date: **2026-09-07**

## Research Goal

Understand what a Content Aggregator is as an Application Type: what its world consists of, who/what performs the selection and assembly of content, how the consumption loop works, and where it separates from its four §02.08 siblings (Feed Reader, Content Curation Platform, Personalized Content Feed) and from adjacent Types (News Aggregator, Information Portal, Directory, Search, Community Platform).

## Initial Boundary (hypothesis before research)

Working hypothesis: a Content Aggregator collects content from multiple external sources and assembles it into a unified, continuously updated surface for consumption, where the application (not a per-item human curator, not the user's own subscription list) performs the assembly.

Expected confusions:

- Feed Reader (§02.08 sibling) — RSS readers are colloquially called "feed aggregators"; the vocabulary overlaps
- News Aggregator (§02.04 sibling) — the most common real-world aggregators are news-scoped
- Content Curation Platform (§02.08 sibling, processed) — human selection vs system assembly
- Personalized Content Feed (§02.08 sibling, unprocessed) — algorithmic per-user streams
- Information Portal (§02.11), Directory Application (§02.11) — pages full of links
- Search Engine / Metasearch (§02.02) — pull vs push
- Community Platform / social news (Reddit/HN-class) — member-voted aggregation

## Research Questions

1. What are the core objects (item, source, topic, stream, assembly machinery)?
2. Who or what selects: editors, algorithms, fixed editorial configuration, or the user's own subscriptions? Which of these is definitional?
3. How is multi-source origin made visible (attribution, source counts, link-out)?
4. What does the user tune (topics, sources, follows) vs what the system decides (ranking, clustering, framing)?
5. How does the production loop work (ingestion → dedup/cluster → ranking → editorial → publication) and how continuous is it?
6. What lifecycle do aggregated items and surfaces have (front-page churn, archives, snapshots)?
7. What derived artifacts exist (newsletters, leaderboards, data products, widgets)?
8. Boundaries: vs Feed Reader, News Aggregator, Curation Platform, Personalized Content Feed, Portal/Directory, Search, Community.

## Representative Products

Selected for different selection philosophies, audiences, and eras:

| Product | Pole | Evidence tier |
|---|---|---|
| Techmeme | crawler + algorithm + human-editor "editorial pyramid"; professional audience; domain-scoped | Tier 1 (homepage, About, Leaderboards — fetched) |
| AllTop | ranking model + editors + clustering; broad multi-topic scan; personal-feed layer | Tier 1 (homepage, About — fetched) |
| Drudge Report | pure human-edited single page, no accounts/algorithms; minimal historical pole (since 1997) | Tier 1 (homepage — fetched) |
| Feedspot | subscription RSS reader + niche discovery catalogs (Feed Reader straddle pole) | Tier 1 (homepage — fetched) |
| Flipboard / Feedly / Popurls / Mix / Digg / Refind / SmartNews | consumer-magazine, reader-mainstream, single-page, interest, relaunch, links-of-the-web, news-app poles | **unreachable** (timeouts; see Sources) |
| elink / Curata / Paper.li | family evidence from the processed Content Curation Platform pass | Tier 1 (sibling research notes) |

## Sources

Fetched successfully (2026-09-07):

- Techmeme — https://www.techmeme.com/ (live front page), https://www.techmeme.com/about, https://www.techmeme.com/lb
- AllTop — https://alltop.com/ (live front page), https://www.alltop.com/about
- Drudge Report — https://www.drudgereport.com/ (live front page)
- Feedspot — https://feedspot.com/ (product homepage)
- Sibling pass: research/content-curation-platform.md (elink three-solution-pages evidence; Curata human-review centering; Paper.li defunct-market observation)

Source-access limitations:

- **Flipboard** (flipboard.com, about.flipboard.com/help-center) — timeout ×3 → abandoned. No claims made about Flipboard anywhere in this pass.
- **Feedly** (feedly.com, feedly.com/i/discover) — timeout ×2 → abandoned. No claims made.
- **Popurls** (popurls.com) — transport error ×2 → abandoned. No claims made.
- **Mix** (mix.com) — timeout ×2 → abandoned. No claims made.
- **Digg** (digg.com) — timeout ×2 → abandoned.
- **Refind** (refind.com) — timeout ×2 → abandoned.
- **SmartNews** (smartnews.com) — timeout ×2 → abandoned.
- AllTop support page /support/news-clustering → 404 (footer link exists; page not published). Machinery documented instead on AllTop's own /about page.
- Techmeme /faq → 404; machinery documented on /about instead.

Consequence: the consumer-magazine pole (Flipboard-class) and the mainstream reader pole (Feedly-class) rest on structural reasoning and the sibling pass's elink market evidence, not on direct product documentation. Assertion strength is reduced accordingly; no precise operational claims are made for those poles.

## Product Observations

### Techmeme (evidence layer A — fetched 2026-09-07)

- Self-positioning: "the only tech news aggregator" — "By sourcing news from thousands of outlets, we're uniquely able to highlight the best and earliest reports on important industry events. And by highlighting notable social media commentary around that news, we're uniquely able to round out coverage." (about page)
- Assembly machinery (about page, "How it works"): "people and software forming a sort of editorial *pyramid*. At the top, editors make final calls on what we feature, and write descriptive, straightforward headlines for that news. Below that are news filtering and discovery tools that our editors rely on and which automatically re-sort our front page. And underlying both is our state-of-the-art crawling technology."
- Editors: "A team of editors across five continents work around the clock" — final call on what is featured; editors write the headlines shown (the aggregator writes its own headline text for featured stories).
- Pure-algorithmic variant in the same family: "Techmeme software foundations also underly political news aggregator memeorandum, and celeb site WeSmirch, both of which run *without* human editors." Also Mediagazer (media industry) runs on Techmeme editors.
- Front-page structure (homepage): ranked story blocks; lead item = author / publication attribution + aggregator-written headline + summary phrase; "More:" lists of related coverage from many other publications; social commentary sections (X, Bluesky, Mastodon, LinkedIn, forums — attributed per author/platform); "Expand More For Next 4" controls.
- Alternative view: "River — Techmeme in pure reverse chronological order" (unranked fallback).
- Archives: date+time snapshot selection ("Enter Techmeme snapshot date and time") — past front pages remain addressable.
- Leaderboards (lb page): "lists that identify the most influential and prolific writers in technology today"; General Leaderboards "determined by the stories featured on Techmeme's homepage over the past 180 days"; Topic Leaderboards: "Techmeme's crawler has sorted through thousands of news publications to find the authors and publications that are most influential and prolific on a variety of key news topics over the past 120 days"; sold as data (one-time purchase, HTML or PDF). Confirms crawler spans "thousands of news publications".
- Distribution: RSS feed of the aggregator itself (feed.xml), daily newsletter, mobile view; social channels.
- Business: self-funded since 2005; advertising (sponsor posts, featured podcast players, paid event listings), "data sales including author-ranking Leaderboards, and news-filtering services."
- Domain scope: tech (sister sites cover media/politics/celebrity) — news-scoped.

### AllTop (evidence layer A — fetched 2026-09-07)

- Self-positioning: "AllTop ranks the stories moving across the web" — "keep the classic AllTop scan of what matters right now, then add market prices when traders are actively assigning odds to the same story." Broad topic coverage: "news, tech, business, politics, sports, crypto, culture, and the source-level context behind each story."
- Assembly machinery (about page, "The three layers that make AllTop what it is"):
  1. "Editors decide the top stories — The ranking model surfaces candidates and sorts the feed, but a human makes the final call on what leads the homepage and how the headline is framed."
  2. "The ranking model scores every story continuously — Each story gets a score built from how fresh it is, how many separate outlets are covering it, the authority of those outlets, and how fast new coverage is arriving. Stories sort by that score, and it updates every few minutes… Two safeguards keep it steady: a story only one outlet is running gets held back until others corroborate it, and a story already leading holds its place unless a challenger clearly outscores it."
  3. "Clustering and ingestion do the groundwork — Incoming articles are grouped by meaning, so twenty versions of the same headline become one story with twenty sources attached rather than twenty separate entries. That source count is what feeds the ranking above it, and it's why a story on AllTop shows how many outlets are behind it."
- Front-page structure (homepage): "Story of the day" block (lead article with author/source attribution, timestamp, source count, "Why it matters" line, "More:" list of other outlets' coverage); "Across every topic" section grids per topic (Tech ×5, Business ×5, AI ×3, Crypto ×3, Culture ×3, Startups ×3, Trump ×3, Weather) with per-item source attribution and ages ("13h ago", "30h ago"); secondary signal layer: live prediction markets (Kalshi, Polymarket) ranked by volume, kept distinct from stories ("stories remain stories, market prices remain market prices").
- Topic pages: /tech, /business, /politics, /sports, /crypto, /ai, /world, /culture, etc.
- Personal layer: "MyAllTop preserves the personal feed workflow: follow topics and sources, save stories, and keep a reading list that is separate from market browsing." Also "My personal feeds" listed as a product pillar.
- Story-page philosophy (about page quote): "A story page should answer what happened, who is covering it, and what markets are implying — only when a relevant market exists."
- Editorial staff named on about page (director of content, reporters/editors); editorial guidelines published.
- Scope: multi-topic general scan (news-dominant but spans sports, culture, entertainment, crypto markets).

### Drudge Report (evidence layer A — fetched 2026-09-07)

- Form: a single hand-edited page of headline links to stories at external outlets (AP, NYT, WaPo, Yahoo News, CNBC, WSJ, Guardian, NPR, NY Post, Guardian, AccuWeather, futurism, local TV, …). All-caps editorialized headlines written by the editor; links go to the original article.
- Structure: top lead story + "UPDATES..." link; flowing headline list separated by rules; standing outlet directories in columns (US outlets A–Z; international newspapers; wire services: AFP, AP Top, Bloomberg, Reuters, Xinhua, KYODO…); utility links (Google Trends LIVE, world newspaper front pages, box office, TV ratings, poll trackers); own archives site (drudgereportArchives.com, "RECENT HEADLINES" timeline); quake/weather side sheets.
- Explicit human-selection pole: app store slogans on page — "FIRST ALERTS, SPEED, CLASSIC VIEW… ALWAYS EDITED BY HUMAN BEING."
- No accounts, no personalization, no visible algorithm; the editor IS the selection mechanism. Since 1997 (site self-presents "DRUDGE REPORT® 2027" branding era; heritage well known — no claims beyond what the page shows).
- News/politics/entertainment headline scope.

### Feedspot (evidence layer A — fetched 2026-09-07; boundary/straddle product)

- Self-positioning: "Read All Your Favorite Websites in one place"; RSS Reader product: "Read content from different sources in one place. e.g. Blogs, RSS, Youtube channels, Podcast, Magazines, etc."
- The reader pole: user subscribes to sources ("Discover and subscribe to popular blogs, podcasts, influencers, magazines and news websites from across the web on FeedSpot Reader") — the user assembles their own list; the reader delivers items from those sources.
- The aggregation/catalog pole: niche discovery catalogs ("Discover" homepage sections — food blogs, woodworking blogs, podcasts by niche, magazines by niche, news websites by region, influencer lists), i.e., human-maintained ranked directories of sources by category; "750K blogs, podcasts and influencers listed"; "120+ Million users visited FeedSpot lists".
- Adjacent products shipped by the same company: Media Contact Database (250K PR contacts in 1,500+ niche categories — a directory product), RSS Combiner, Embeddable RSS Widgets, Brand Monitoring, Combined Newsletters, Social Media Scheduler.
- Demonstrates in one company: (a) the user-subscription reader (Feed Reader seam), (b) source catalogs (Directory seam), (c) content-into-one-place framing that both Types share in marketing language.

### Family evidence from the processed Content Curation Platform pass (evidence layer B — sibling research)

- elink sells "Bookmark Manager", "RSS Feed Reader", and "Content Curation" as three separate solution pages of one product — direct market evidence that reader / curation / (and by extension aggregation) are distinct recognized categories.
- Curata centers human review/selection over automated discovery — curation, not aggregation.
- Paper.li-class fully automated curation products have exited the market (domain repurposed) — the fully-automated *curation* pole died; automated *aggregation* (Techmeme/AllTop machinery) is alive and staffed differently: the artifact is the stream, not a collection.

## Cross-product Comparison

| Dimension | Techmeme | AllTop | Drudge Report | Feedspot |
|---|---|---|---|---|
| What the user gets | ranked tech-news stream w/ cluster "More:" coverage | ranked multi-topic story stream + topic pages + market signals | one hand-edited headline-link page | unified reader of user-subscribed sources |
| Who selects between items | editors atop auto re-sorting tools + crawler | ranking model (freshness × outlet count × authority × velocity) + editors' final call | the human editor, alone | **the user** (subscriptions); catalogs only recommend sources |
| Clustering of same-story coverage | yes ("More:" lists) | yes (semantic clustering, visible source counts) | no | no (per-feed items) |
| Personalization/tuning | none on the surface | MyAllTop: follow topics/sources, save, reading list | none | subscription list is the personalization |
| Attribution to sources | explicit (author / publication) | explicit (source name, source count) | implicit (link-out to outlet) | per-feed item origin |
| Accounts required | no | for My personal feeds | no | yes (reader) |
| Ingestion machinery | crawler over thousands of publications | ingestion + semantic clustering + scoring | none visible (editor reads the web) | feeds/RSS ingestion |
| Archives/history | date-time front-page snapshots; 180-day leaderboard basis | story ages; (archive depth not observed) | separate archives site | reader history (not observed in docs) |
| Derived data products | Leaderboards (author/source influence), news-filtering services | source authority as ranking input; (no data product observed) | visit counters | media contact database (separate product) |
| Scope | tech news (sister sites: media/politics/celeb) | broad multi-topic, news-dominant | news/politics/entertainment | general (blogs/podcasts/video/news) |
| Audience | industry professionals, execs | general scanners + market-curious | general consumers | individual readers; PR/marketers |
| Business model | ads + data sales + filtering services | (ads implied; market-data layer) | ads | freemium reader + B2B products |

Stable across all four: many external sources → one surface; the surface is continuously refreshed; items carry source attribution/links; users consume rather than author the flow; the product's own machinery (human, algorithmic, or both) decides what appears and in what order — with Feedspot deliberately showing the sibling pole where the user's subscription list decides.

## Abstraction Levels

### L0 — Defining Invariant (deliberately small)

A Content Aggregator is recognizable by exactly this structure:

```text
Content items drawn from many external sources
  (publications/sites/channels the application hosts none of as its primary job)
  └── Product-side assembly: the application's own machinery — editorial judgment,
        algorithmic ranking, or a fixed configured mix — decides which items
        from which sources enter the surface and in what order
        (not the user's own subscription list; not per-item human curation
        into organized collections)
        └── One unified, continuously refreshed consumption surface,
              presenting items with attribution/links back to their sources
```

Three properties. Remove any one and the Type collapses into a neighbor:

- Remove multi-source inflow → the product is a single publication (blog/news site), not an aggregator.
- Remove product-side assembly → if the user's subscription list does the selecting it is a Feed Reader; if a query does the selecting it is Search; if a curator selects items into persistent named collections with added context it is a Content Curation Platform; if members' votes/discussion select it is a Community Platform.
- Remove the unified, current, attributed surface (e.g., static organized set, or unattributed rehosting) → a curation collection (not current), a links directory (no flowing items), or a republishing pirate (not aggregation).

Notes on the L0 boundary:

- "Attribution/links to sources" is definitional: every sampled product points back to origin (explicit source names, or link-out). Without it the artifact is stolen/rehosted content, not aggregation.
- The assembly can include human editors (Techmeme, AllTop, Drudge) — what makes it aggregation rather than curation is that the deliverable is the standing stream/page itself, continuously refilled, not a persistent organized collection built item-by-item with added context. Editors in aggregators make final calls on a flow; curators build sets.
- The user may tune inputs (follow topics/sources — AllTop's MyAllTop layer) without the L0 changing: the application still assembles the item-level flow.
- Accounts, personalization, clustering, topics, apps, RSS ingestion, archives: all absent in at least one live product (Drudge lacks accounts/personalization/clustering/apps/RSS; AllTop's default view needs no account) → none is definitional.

### L1 — Common Mature Structure (standard capabilities)

- Topic/category organization: sections or topic pages beyond the single main stream (AllTop topic network; Techmeme Topic Leaderboards as topic axis; Feedspot niche categories).
- Follow/subscribe tuning: the user follows topics and/or sources to shape a personal variant of the stream, plus save/reading list (AllTop MyAllTop — direct; consumer pole expected — structural).
- Story clustering with visible coverage breadth: same-story articles merged, source counts or related-coverage lists shown (AllTop direct; Techmeme "More:" lists direct). Common in machine-assembled aggregators; absent in hand-edited pole → common, not definitional.
- Chronological fallback view alongside the ranked view (Techmeme River) — common pattern: an "everything, unranked" alternative.
- Archives/history: addressable past states of the surface (Techmeme snapshots; Drudge archives site) or per-item history.
- Distribution surfaces beyond the page: daily newsletter, RSS feed of the aggregator itself, mobile app (Techmeme, Drudge).
- Derived influence data: source/author rankings as a first-class artifact (Techmeme Leaderboards, free + paid; AllTop source-authority input) — common at the professional pole.
- Save-for-later integration point: reading lists (AllTop) and the natural handoff to read-it-later services — common.

### L2 — Variant / Optional Structure

- Selection-philosophy poles: pure human editing (Drudge) · human+machine pyramid (Techmeme, AllTop) · pure algorithmic (Techmeme's sister sites documented as running without editors) · user-subscription-driven (Feedspot reader pole — the Feed Reader sibling). NOT definitional which pole; that a product-side mechanism assembles is the invariant.
- Scope axis: domain-scoped (tech/media/politics/celebrity — the Techmeme family pattern), broad multi-topic (AllTop), niche catalogs (Feedspot). News-scoped variants shade toward the News Aggregator sibling (§02.04).
- Secondary signal layers stacked on the stream: notable social commentary around stories (Techmeme), prediction-market odds beside stories (AllTop), bias/stance ratings (Ground News-class — structural, unreachable).
- Reading surface: link-out headlines (Drudge, Techmeme) vs in-app article rendering (consumer apps — structural; not directly verified in this pass).
- Audience packaging: professional/executive current-awareness (Techmeme), general consumer scanning (Drudge, AllTop), reader-tool users (Feedspot).
- Business models: advertising/sponsorship (Drudge, Techmeme), data sales and services (Techmeme leaderboards, filtering services), freemium reader (Feedspot), B2B monitoring.
- Regional/language-scoped aggregators (structural; not sampled).

### L3 — Vendor-specific (research notes only)

- Techmeme: "editorial pyramid" phrasing; General Leaderboards based on 180 days of homepage features; Topic Leaderboards from 120 days of crawler data, $100 one-time, HTML/PDF, ~40 topics; sponsor posts priced $7k–$21k/month; paid event listings $2.9k/month; "news-filtering services" business line; editors across five continents; launched 2005 (Gabe Rivera; Omer Horvitz co-lead); sister sites Mediagazer (with editors) and memeorandum/WeSmirch (without editors); aggregator's own RSS feed + newsletter.
- AllTop: scoring inputs (freshness, separate-outlet count, outlet authority, coverage velocity; updates every few minutes); safeguards (single-outlet stories held back until corroborated; leading story holds its place unless clearly outscored); prediction-market partners Kalshi/Polymarket/Polymarket US; "24/7 story ranking · 3 market venues · Live market context · My personal feeds" pillar strip; "As seen in NYT/BBC/CNET/Amazon/Mayo Clinic/Harvard/Smithsonian"; named editorial team; about-page updated July 27, 2026; support/footer pages for News Clustering/Best Price (clustering page 404 at fetch time).
- Drudge Report: displayed visit counters (31,385,557 past 24h / 550,093,391 past 31 days / 6,110,720,834 past year as of 2026-09-07); "ALWAYS EDITED BY HUMAN BEING" app slogan; separate archives domain (drudgereportArchives.com + headline timeline); quake sheet and weather action side pages; all-caps editorialized headline style; standing A–Z outlet columns + wire-services column.
- Feedspot: claimed scale (750K listed blogs/podcasts/influencers; 120M+ visitors; 250K media contacts in 1,500+ niches); product set (RSS Reader, Media Contact Database, RSS Combiner, RSS Builder, Widgets, Brand Monitoring, Combined Newsletters, Social Scheduler, Publisher listing program); mobile apps.

## Rejected Findings (considered, not promoted)

- **"Aggregator = news"** — rejected: Techmeme/Drudge are news-scoped, but AllTop spans sports/culture/crypto/entertainment topics, and the consumer-magazine pole aggregates non-news content structurally. Scope is a variant axis; news-scoped products shade into the News Aggregator sibling.
- **"Clustering is definitional"** — rejected: Drudge does not cluster; clustering is machinery of the machine-assembled pole (2/4 direct).
- **"RSS/feeds are definitional"** — rejected: only Feedspot depends on feeds; Techmeme crawls; Drudge's editor reads; AllTop ingests. Ingestion mechanism is an implementation.
- **"Personalization/algorithmic ranking is definitional"** — rejected: Drudge has no algorithm and no personalization; AllTop's default view is shared. Per-user machinery belongs to the Personalized Content Feed sibling.
- **"Accounts are definitional"** — rejected: Drudge/Techmeme front pages need none.
- **"Human editors are definitional"** — rejected: Techmeme's own About documents sister aggregators of the same software family running without editors. Editorial review is one pole of the assembly mechanism.
- **"Editor-written headlines are definitional"** — product-level detail (Techmeme/Drudge write headlines; AllTop frames leads editorially; machine pole inherits source headlines). Common, not definitional.

## Boundary Findings

1. **vs Feed Reader (§02.08 sibling, unprocessed)** — sharpest intra-family seam. Reader's center: the user manages a subscription list of sources and consumes their streams with per-source/per-item reading state (unread, read, saved). Aggregator's center: the product assembles the item-level flow from a broad source base; the user tunes at most (follow topics/sources). Evidence: Feedspot in one company runs the reader (user subscribes) beside ranked niche catalogs (system-recommended sources); elink sells "RSS Feed Reader" and curation as separate solutions (sibling pass). Market straddle: mainstream readers brand themselves "news/content aggregators" (vocabulary overlap) — Feedly-class unreached in this pass. Removal test: replace product-side assembly with the user's own subscription list → Feed Reader. **Flag for joint review when feed-reader is processed.**
2. **vs News Aggregator (§02.04 sibling, unprocessed)** — same machinery, narrower scope. Techmeme self-describes as a "tech news aggregator"; Drudge and AllTop are news-dominant. The 02.04 sibling is the news-specialized expression; Content Aggregator spans content kinds (articles, blogs, links, video, posts) and topic breadth beyond news. Boundary = content scope, not structure. **Flag for joint review; likely the same family realized twice in the directory.**
3. **vs Content Curation Platform (§02.08, processed)** — confirmed from this side. Curation: a curator selects items into persistent named collections, adds context, presents the collection to an audience (collection = artifact). Aggregation: product-side machinery assembles a standing, continuously refilled stream (stream = artifact; no per-item human selection into sets; no collection object). Removal test consistent with the sibling's ("remove human selection → aggregator"). Techmeme/AllTop editors make final calls on a flow — they do not build collections. **Joint review recommended (flagged by the sibling pass; this pass confirms).**
4. **vs Personalized Content Feed (§02.08 sibling, unprocessed)** — the sibling's defining machinery is per-user personalization (inferred interests drive each user's stream). The aggregator's default surface is shared (same-for-everyone: Drudge, Techmeme, AllTop default pages); personal feeds are an optional tuning layer (AllTop MyAllTop). Removal test: remove per-user inference → still an aggregator; remove the shared assembled surface → not an aggregator. Structural (sibling unprocessed); **flag for joint review.**
5. **vs Information Portal (§02.11) and Directory Application (§02.11)** — portal artifact = navigational hub (entry points, sections, services, links out); directory artifact = standing entries per entity with reach attributes. Aggregator artifact = flowing content items presented for consumption. Drudge's A–Z outlet columns and Feedspot's niche catalogs are directory-like furniture; Feedspot ships a literal media-contact database as a separate product — the market separates the artifacts. Structural.
6. **vs Search Engine / Metasearch (§02.02)** — pull vs push: search assembles results per query, transient; aggregator maintains a standing assembled surface between queries. Metasearch aggregates query results across engines; aggregation here runs without a user query. Structural.
7. **vs Community Platform / social news (§01.06/§01.01)** — Reddit/HN-class products select via member submission + voting + discussion; the community's participatory selection is their center. Aggregators in this pass select via the product's own editorial/algorithmic machinery; readers do not vote items in. Products can drift across this seam. Structural.
8. **vs Bookmark Manager / Read-it-later (§02.13/§02.09)** — personal retention artifacts vs a public/shared standing stream. The aggregator is the discovery/consumption surface; read-later/bookmarking is the personal downstream (save actions, reading lists mark the handoff). Structural.
9. **Historical / market-sample check** — Drudge Report (1997, still live) passes the full L0 with zero accounts, zero algorithms, zero apps, zero RSS: a hand-edited page of attributed links from many outlets, continuously refreshed through the day. Techmeme's 2005 crawler+editor hybrid passes. Techmeme's own sister sites run without editors — so even the human editor is not required. Print-era practice (condensed-articles digests such as Reader's Digest since 1922; news-clipping services) satisfies the same structure off-software, indicating the Type predates its implementations. The definition therefore does not depend on RSS, apps, accounts, personalization, clustering, or any single selection philosophy.

## Uncertainties

- **Consumer-magazine pole unverified** — Flipboard unreachable; whether magazine-style consumer aggregators expose different first-class objects (user-created magazines as collections) is unresolved. If a product centers user-built collections for an audience, it may straddle toward Curation Platform. Structural handling; no claims made.
- **Reader-mainstream pole (Feedly-class) unverified** — how strongly mainstream readers position as "aggregators" and how their discovery features blur the reader/aggregator seam is unresolved; joint review flagged.
- **In-app reading prevalence** — link-out is direct evidence (Techmeme, Drudge, AllTop); in-app article rendering in consumer aggregators is structural reasoning only.
- **Personalization depth in current products** — sampled products rank mostly without per-user inference; consumer pole may differ; not verified.
- **AllTop's own history** — the current product explicitly references "the classic AllTop scan" and a 2026 build; the feed-directory era (2008) was not independently verified in this pass (site has pivoted).
- **Scope drift risk** — with news-heavy reachable evidence, there is residual risk that the synthesis over-weights news machinery; mitigated by AllTop's multi-topic breadth and Feedspot's general-content framing, but the consumer pole remains unobserved.
- Whether "attribution/link-back" can degrade (e.g., in-app rendering with canonical attribution) without leaving the Type: assumed yes (attribution preserved, hosting changes); not directly tested.

## Final Synthesis

A Content Aggregator is a content-consumption application that continuously collects content items from many external sources and assembles them — through its own machinery, which may combine editors, algorithms, or a fixed editorial configuration — into one unified, continuously refreshed consumption surface on which items are presented with attribution and links to their sources.

The defining core is small: **multi-source inflow + product-side assembly into a standing flow + one current, attributed surface.** Everything else commonly seen — topic pages, follows and personal feeds, clustering, chronological fallbacks, archives, newsletters, apps, leaderboards/data products, market or social signal layers — is standard or variant capability layered on that core. The market's own poles prove the invariant does not depend on any single mechanism: a lone human editor with a static page (Drudge), a crawler-driven editorial pyramid (Techmeme), a scoring model with editors and semantic clustering (AllTop), and a user-subscription reader beside niche catalogs (Feedspot) all sit in the same family neighborhood, separated by *who assembles* — and the sibling passes prove the market itself (elink's three solution pages; Paper.li's exit vs Techmeme's persistence) treats stream-assembly, collection-curation, and subscription-reading as distinct product categories.
