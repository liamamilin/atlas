# Research Notes — Read-it-later Application

Research date: 2026-09-08
Leaf: Read-it-later Application (§02.09 Reading) — slug `read-it-later-application`

## Research Goal

Understand what a Read-it-later Application is as an Application Type — its defining structure, its standard capabilities, its variants — from real products, and hold clean boundaries against the neighbors that previous passes already staked: Bookmark Manager, Feed Reader, E-book Reader, E-book Library / Reading Library, Academic Paper Reader, News Aggregator / Personalized Content Feed. This pass must also discharge the explicit joint-review flag the bookmark-manager pass left ("the most important boundary") from the read-it-later side.

Special situational awareness: the category itself is mid-contraction. Pocket (the archetype) shut down (verified via its shutdown page); other services have wound down or been absorbed (reported context, not verified in this pass — no operational claims rest on it). Survivorship and platform absorption (browser reading lists) are part of the evidence, not noise.

## Initial Boundary

- Hypothesis: an application where a user captures web content (articles above all) for later reading, the app holds a readable copy of the content, and the collection behaves as a consumption queue (unread → read → archived) rather than a permanent reference library.
- Nearest neighbors: Bookmark Manager (retrievable reference), Feed Reader (subscription intake), E-book Reader (opened book), Reading Library (durable collection), News Aggregator (machine-assembled flow), PDF/Document Reader, To-do-style task tools (queue resemblance).
- Vocabulary trap: "read-later", "reading list", "read-it-later", "save for later" are used loosely by vendors and platforms; several products straddle the bookmark seam deliberately.

## Research Questions

1. What objects exist? (saved item, reading state, archive, favorites, tags, highlights)
2. How does capture work, and is capture machinery definitional or common?
3. What is the working object of a saved item — the link, the extracted copy, or the media itself? What happens when extraction fails?
4. What is the consumption loop (unread → reading → done), and how do products express "cleared vs kept"?
5. Which capabilities are category-standard vs modern-pole additions vs vendor-specific?
6. What content types beyond articles do products hold, and where does breadth change the Type?
7. What do older / platform-native / open-source realizations look like (historical check)?
8. Where exactly do the boundaries with Bookmark Manager, Feed Reader, and the library Types bite — in objects, in loop, or in posture?

## Representative Products

| Product | Why sampled | Pole |
|---|---|---|
| Wallabag (+ wallabag.it hosted) | open-source since 2013, self-hostable; the richest accessible operational documentation | self-hosted / OSS, data-portability-first |
| Readwise Reader | self-described "first read-it-later app built for power readers"; premium subscription; extensive docs | modern premium power-user |
| Matter | self-described "modern read-later app for iPhone, iPad, and web"; consumer mobile-first | modern consumer, mobile-first |
| Instapaper | long-running commercial archetype; minimal philosophy | classic minimal commercial (degraded evidence — see Sources) |
| Pocket | the archetype (founded as "Read It Later", Inc.); shut down (year derived from "past 8 years" + 2017 acquisition on the shutdown page) | historical anchor + drift example |
| Safari Reading List | platform-native realization inside a browser | §24 platform-native check |

## Sources

Fetched 2026-09-08 (all Layer A unless noted):

- https://doc.wallabag.org/en/ (project documentation index) — self-definition: "wallabag is a read-it-later application: it saves a web page by keeping content only. Elements like navigation or ads are deleted."
- https://doc.wallabag.org/en/user/interface/ — homepage (grid/list of saved articles), left menu (unread, starred, archived, tags), toolbar (save URL, search, random entry, filters incl. unread/starred/archived/annotations/language/reading time/domain/date-saved, download current view)
- https://doc.wallabag.org/en/user/articles/save/ — capture: bookmarklet "bag it!", paste-URL form, Wallabagger browser extension (save, edit title, tags, starred/archived, delete; duplicate-save detection note), mobile apps
- https://doc.wallabag.org/en/user/errors_during_fetching/ — fetch-failure handling: Re-fetch content; graby + php-readability parsers; per-domain site config files (XPath title/body/strip); Wallabagger can send already-rendered page content instead of the link
- https://doc.wallabag.org/en/user/faq/ — account/FAQ (no queue-behavior content; confirms docs reachability)
- https://www.wallabag.it/en — hosted service positioning: "Save articles now, read them later on every device"; "keeps the readable text of your articles, not just a link"; "Read anywhere, even offline"; tags/search/favourites/annotations/exports; subscriptions from 11€/year; "export your data anytime"; apps for web/Android/iPhone/e-reader
- https://readwise.io/read — positioning: "The first read-it-later app built for power readers"; "Save everything to one place"; content types: web articles (reader mode), RSS, PDFs, YouTube transcripts, Twitter threads, EPUBs, newsletters; highlighting first-class; Ghostreader (GPT); TTS; keyboard reading; full-text search offline; local-first sync; export CSV/OPML/zip/Markdown; import from Instapaper/Pocket/CSV/OPML; "Pocket shut down. How do I know Reader won't?"; FAQ: pricing $9.99/mo annual; MCP server; CLI; changelog
- https://docs.readwise.io/reader/docs — "What is Reader?": all-in-one reading app; library sections; getting started
- https://docs.readwise.io/reader/docs/saving-content — extension saves "a clean, readable version of the document to your Reader inbox"; extension gets rendered content "as opposed to just a URL"; paywalled content via iOS Safari only, otherwise "naked URL … partial parsing"; share-sheet actions (Read Now / Delete / tags / document note / Move to Later / Move to Archive); Library sections "Inbox or Later, depending on your configuration"; "move it straight to the archive if you read it on-site"; Archive described as for items "you've read in your browser and simply want to save for posterity"
- https://docs.readwise.io/reader/docs/organizing-content — document tags vs highlight tags; filtered views (query syntax: date saved, reading length, number of highlights…); RSS folders
- https://docs.readwise.io/reader/docs/faqs — cross-platform surfaces; offline full-text caching + selective per-section caching (Feed off by default); unseen dots (dark blue = unseen, teal = unseen RSS, green = saved more than once; dot disappears on open); reading progress vs last location (pace-based, never moves backward); return-to-position; undo; delete → Trash (device-specific) with restore/restore-all; command palette; keyboard-driven
- https://getmatter.app/ — "Matter is the modern read-later app for iPhone, iPad, and web"; "Welcome Pocket Readers"; "Save anything for later. Save articles, threads, and PDFs… advanced parsing technology so you can read without distraction"; newsletters via Gmail connect or unique Matter address; follow writers/feeds; YouTube/podcast transcription to time-synced text; TTS playlist; highlighting; Power Queuing ("Reorder, triage, filter, shuffle"); offline search; tagging; "Sync highlights to your second brain"; quoteshots (positioning-level only; no operational docs fetched)
- https://getpocket.com/ — shutdown notice: "our read-it-later and content discovery app"; "What began as a read-it-later app evolved into something much bigger" (curation/recommendations after Mozilla's 2017 acquisition); successors named as Firefox Tab Groups and "enhanced bookmarks … built-in ways to manage reading lists"; "© 2026 Read It Later, Inc."
- https://support.apple.com/guide/safari/keep-a-reading-list-sfri35905/mac — "To quickly save webpages to read later, add them to your Reading List"; save offline (per page or automatic "Save articles for offline reading automatically"); Unread/All toggle; Mark as Read/Unread; delete; search; iCloud continuity; separate doc page exists for "Bookmark webpages to revisit" — reading list and bookmarks are distinct Safari features
- https://support.apple.com/guide/safari/welcome/mac — TOC confirming bookmarks-vs-reading-list separation in Safari's own documentation

Degraded / unreachable (recorded per the source-access rules):

- https://www.instapaper.com/ and https://www.instapaper.com/about — both returned empty page bodies (title only) on 2026-09-08; two attempts, then abandoned. No operational Instapaper claims are drawn anywhere in these notes or the final document; Instapaper's role in the sample is historical anchor and category positioning, corroborated indirectly by Wallabag's and Reader's import documentation.
- getpocket.com operational docs no longer exist (service shut down); only the shutdown page itself was used.
- Matter help-center / operational docs not fetched (positioning page only); no operational Matter claims drawn.
- docs.readwise.io/reader/docs/faqs/basics → 404 (FAQ index at /faqs used instead).

Cross-pass boundary obligations (from earlier passes):

- bookmark-manager: "Read-it-later's center of gravity is the consumption queue… the extracted readable copy is the working object, and the queue's health is measured by items being consumed and cleared… Distinguishing test: remove the organized persistent library and keep only the reading queue → read-it-later; remove the reading-experience machinery and keep the organized library → bookmark manager." — discharge from this side below.
- e-book-reader: "read-it-later captures web articles and presents them in a reader-mode surface; unit = clipped article, acquisition = clipping, no book structure."
- academic-paper-reader: "Read-later holds a triage queue of heterogeneous web content intended to be processed/cleared; paper reader holds a durable, identity-bearing scholarly collection… the identity+library model vs the inbox model."
- feed-reader: "Sharing outward — send an item to a read-it-later service, notes app, mail, or social target."
- content-aggregator: saved items and reading lists hand off to personal retention.
- note-taking-application: "2 without 1 (records that point at external resources rather than hold authored content) = bookmark manager / read-it-later."

## Product observations

### Wallabag / wallabag.it (Layer A — operational docs + hosted positioning)

- Self-definition (project docs): "a read-it-later application: it saves a web page by keeping content only. Elements like navigation or ads are deleted." — extraction IS the product's own first sentence.
- Save page: "The main purpose of wallabag is to save web articles." Four capture paths: bookmarklet ("bag it!"), paste-URL form, browser extension (Wallabagger), mobile apps.
- Wallabagger extension: save current page, edit title, add/remove tags, set starred and archived, delete. Duplicate-save behavior documented: saving an already-saved URL reopens the existing entry with its tags/title/flags.
- Interface: homepage lists saved articles (grid or list); left menu = unread, starred, archived, tags; toolbar = save new URL, search, random entry ("open a random saved entry"), filter modal (unread/starred/archived/annotations, language, reading time, domain, date saved), download current view, account menu (API clients, themes).
- Failure handling is a first-class documented topic ("Fetch errors"): network/server/site-structure failures; "Re-fetch content" button; parser = graby + php-readability; per-domain site configs (XPath) maintained in a shared community repository; the extension can send the already-interpreted page content instead of only the link.
- Hosted service: readable text "not just a link that can change or disappear"; offline reading on web/Android/iPhone/tablet/e-reader; tags, search, favourites, annotations, exports; "export your data anytime"; subscription-funded, no ads.
- Tagging rules (config doc nav) = automatic tag application rules; RSS output of the library (config doc nav); import from Pocket, Instapaper, Readability, Pinboard, elCurator, wallabag v1/v2.

### Readwise Reader (Layer A — marketing site + docs)

- Positioning: "The first read-it-later app built for power readers"; "Save everything to one place"; "All your reading in one place."
- Content types enumerated: articles (read-it-later), RSS, PDFs, YouTube (transcript highlighting), Twitter threads ("compiled into proper long-form articles"), EPUBs, newsletters. Reader is the sample's maximal-breadth pole.
- Saving: browser extension saves "a clean, readable version of the document to your Reader inbox"; extension prefers rendered content over naked URL; mobile share sheet with Read Now / Move to Later / Move to Archive; document note ("why you're saving this").
- Library sections: Inbox or Later (configurable first section), Archive, plus content-type sections (Feed, PDFs, EPUBs…), Pinned, Trash. Archive explicitly framed for items "you've read in your browser and simply want to save for posterity" — i.e., archive = post-consumption retention.
- Triage language throughout: the marketing page frames queue-clearing as a designed loop — "game-like triage for clearing our email inboxes of clutter… Weed your digital garden with delight"; a testimonial: "the first reading app that helps you process information rather than hoard it."
- Reading state: unseen dots (dark blue unseen; teal unseen-from-feed; green saved-more-than-once), dot disappears on open; reading progress vs last location, pace-differentiated, never backward; return-to-position affordance.
- Organization: document tags + highlight tags, saved filtered views (query syntax: date saved, reading length, highlight count), RSS folders.
- Offline: full-text caching, selective per-section caching, offline full-text search.
- Annotation/knowledge flow: first-class highlighting (images/tables/rich text), auto-sync to the Readwise highlights product, exports to note apps (Obsidian/Notion/Roam/Evernote/Logseq), Markdown export, MCP server, public API, CLI.
- Migration: import from Instapaper, Pocket export file, generic CSV of URLs, OPML; export "anytime, in full" (CSV/OPML/zip/Markdown). The FAQ treats "Pocket shut down" as a first-class customer question — the category's mortality is part of its market discourse.
- Pricing: subscription ($9.99/mo annual), 30-day trial; bootstrapped-sustainability pitch as a response to category shutdowns.

### Matter (Layer A positioning only — no operational docs fetched)

- Self-positioning: "the modern read-later app for iPhone, iPad, and web"; "Save. Read. Grow."
- Explicit Pocket-migration capture: "Welcome Pocket Readers."
- Capture breadth: "Save articles, threads, and PDFs"; newsletters (Gmail connect or a unique Matter email address); "follow writers and feeds"; YouTube/podcast saving with time-synced transcription.
- Queue posture: "Save anything for later"; Power Queuing ("Reorder, triage, filter, shuffle"); parsing ("advanced parsing technology so you can read without distraction").
- Reading: TTS playlist ("switch between audio and text… seamlessly"), friction-free highlighting, audio highlights, quoteshots, offline search, tagging, highlights-to-second-brain integrations.
- No operational docs sampled → all Matter findings stay at positioning strength; nothing operational asserted.

### Pocket (Layer A — shutdown page only; historical anchor)

- Self-describes at shutdown as "our read-it-later and content discovery app"; origin: "What began as a read-it-later app evolved into something much bigger" — curation/recommendation machinery after Mozilla's 2017 acquisition.
- The pivot to discovery/recommendations is named as the reason resources moved elsewhere ("the way people save and consume content on the web has evolved"); reading-list management is delegated to Firefox's built-in Tab Groups and "enhanced bookmarks."
- Corporate vestige: footer still "© 2026 Read It Later, Inc." — the Type's founding name.
- Drift lesson: recommendations/discovery growth moved the product away from its Type center; the queue core is what users had to migrate away from (Reader/Matter both advertise Pocket import).

### Safari Reading List (Layer A — official guide; §24 platform-native check)

- "To quickly save webpages to read later, add them to your Reading List. To read webpages in your Reading List even when you're not connected to the internet, you can save them offline."
- Capture: Share button → Add to Reading List; Shift-click a link.
- State model: Unread/All toggle; Mark as Read / Mark as Unread; remove/delete entries; search over the list; continuous reading ("keep scrolling when you reach the end of a Reading List webpage").
- Offline: per-page Save Offline or automatic "Save articles for offline reading automatically."
- Sync via iCloud across devices.
- What it lacks: no tags, no folders, no archive, no favorites, no highlights, no reading-time estimates, no extraction at save time (the saved object is the webpage itself, viewable with Safari's separate Reader mode). No separate account needed beyond the platform.
- Key structural fact: Safari's own documentation separates "Bookmark webpages to revisit" and "Keep a Reading List" as two distinct features — the browser platform itself draws the bookmark-vs-read-later seam.

### Instapaper (degraded evidence — positioning only, via corroboration)

- Direct site unreachable from the research environment on 2026-09-08 (two attempts, empty bodies). No operational claims drawn.
- Corroborated existence and category membership: Wallabag docs provide a dedicated Instapaper import path; Reader advertises direct Instapaper import; wallabag.it markets itself as an alternative to Pocket, Instapaper & Pinboard; Pocket-era testimonials reference "ex-Pocket / Instapaper power user."
- Role in sample: a long-running commercial archetype (age asserted from common knowledge and corroborated only indirectly — every sampled vendor treats it as an established import source; no fetched source states its founding year); survivor of the category contraction.

## Cross-product Comparison

| Dimension | Wallabag | Reader | Matter | Safari Reading List | Pocket (historical) | Instapaper |
|---|---|---|---|---|---|---|
| Deliberate save-elsewhere capture | ✔ bookmarklet/form/extension/apps | ✔ extension/share sheet/upload | ✔ extension/newsletters/follows | ✔ share/shift-click | ✔ (save button) | ✔ (corroborated) |
| Working object = held content | ✔ "keeping content only" | ✔ "clean, readable version" | ✔ "advanced parsing" | ✔ saved webpage copy (no extraction) | ✔ (per shutdown framing) | (unverified) |
| Source link kept with item | ✔ (domain opens source article) | ✔ (partial parsing when link-only) | (positioning-level) | ✔ (webpage) | ✔ | (unverified) |
| Unread/read state | ✔ menu + filters | ✔ unseen dots | ✔ (implied by triage) | ✔ Unread toggle + mark read | ✔ | (unverified) |
| Archive/clear as distinct from delete | ✔ archived ≠ deleted | ✔ Archive ≠ Trash | ✔ (triage/queue framing) | ✖ (delete only) | ✔ | (unverified) |
| Favorites/starred exception | ✔ starred | ✔ Pinned/Shortlist variants | (positioning-level) | ✖ | ✔ | (unverified) |
| Tags | ✔ | ✔ doc + highlight tags | ✔ | ✖ | ✔ (historical) | (unverified) |
| Extraction failure handling documented | ✔ dedicated doc page | ✔ partial-parsing FAQ | (not sampled) | n/a (no extraction) | n/a | n/a |
| Offline holding | ✔ | ✔ cached full text | ✔ offline search | ✔ Save Offline | ✔ | (unverified) |
| Cross-device continuity | ✔ web/mobile/e-reader | ✔ local-first sync everywhere | ✔ iPhone/iPad/web | ✔ iCloud | ✔ | (unverified) |
| Reading-comfort controls | ✔ (display settings) | ✔ typography/themes/paged scroll | ✔ (reader design) | ✔ Reader mode (separate) | ✔ | (unverified) |
| Reading progress/position | ✔ (filters by reading time; progress implied) | ✔ pace-based progress + return | (positioning-level) | ✖ documented | ✔ | (unverified) |
| Highlights/annotations | ✔ annotations | ✔ first-class → knowledge flow | ✔ highlights | ✖ | ✔ (historical) | (corroborated historically) |
| TTS | (not evidenced) | ✔ | ✔ | ✖ documented | ✔ (historical) | (unverified) |
| Ingestion beyond manual save | RSS output only | ✔ RSS + newsletters + files | ✔ newsletters + follows + media | ✖ | ✔ (recommendations era) | (unverified) |
| Import/export as migration convention | ✔ multi-service import, export anytime | ✔ Instapaper/Pocket/CSV/OPML in; CSV/OPML/zip/MD out | Pocket migration advertised | n/a (platform) | export-at-shutdown | export (corroborated via importers) |
| Business model | OSS + paid hosted | premium subscription | consumer mobile-first (model not verified) | platform feature | shut down; was free+premium | (unverified) |

Reading of the table:

- Universal across every sampled realization (including the platform-native pole): deliberate capture, held content for in-app reading, unread/read state, source link retained, offline holding, cross-device continuity (Safari's via iCloud).
- Near-universal in dedicated products (absent only in Safari): archive/favorites distinction, tags, highlights. These are maturity layers, not the Type's spine.
- Era-pole features (TTS, transcription, AI assistance, ingestion breadth) appear only at the modern poles → variant/optional.
- The extraction step is *nearly* universal but is explicitly absent at the platform pole (Safari holds the webpage itself) and is a *documented failure mode* everywhere it exists → extraction is the dominant implementation of "content held for reading", not the invariant itself.

## L0 / L1 / L2 / L3 abstraction

### L0 — Defining Invariant (minimal)

```text
Deliberate capture of content from elsewhere (save act)
└── the saved reading item as the unit of record
    │   (source link + title, plus the content itself held in a form
    │    the product can present: extracted clean copy / archived page /
    │    uploaded document / media with transcript — not merely an address)
    └── the deferred-reading queue posture
        │   (enters unread, surfaces organized around reading state,
        │    consumed: marked read and set aside — archive/remove —
        │    retention the deliberate exception)
        └── the in-app reading surface as the product's main act
            (the product presents the content itself for reading)
```

Three jointly-held structures. If any one is removed, the product stops being recognizable as this Type:

1. **Saved reading item as unit of record** — a persistent, individually addressable entry created by a deliberate save act performed elsewhere (usually while browsing), carrying at minimum its source (title + origin link) and its content in a presentable form. Remove → browsing history / a link log. Keep the record but hold only the organized address → Bookmark Manager.
2. **Deferred-reading queue posture** — the collection is lived in as a queue of things to read *later*: items enter unread, the primary surfaces sort/filter by reading state, and items are consumed — archived, removed, or otherwise retired once handled. Favorites are the deliberate retention exception. Remove → a permanent reference library or a feed: nothing is "later", nothing is cleared.
3. **In-app reading surface as the main act** — the product itself presents the saved content for reading (reader-mode text, archived page, document viewer, media/transcript player), rather than handing the user back out to the web. Remove → a link triage list; the "reading" in the Type's name is gone.

Jointly-held load-bearing tests:

- 1 alone (records without queue posture or reading surface) = Bookmark Manager
- 2 without 1+3 = a to-do list of links
- 3 without 1+2 = browser reader mode / a bare document viewer
- 1+3 without 2 = a general reading library (retention normal, nothing cleared) — E-book Library / paper-reader territory
- 1+2 without 3 = a link triage queue (unread-flag bookmark lists that never present content)
- 2+3 without 1 = ephemeral reading with nothing held (an ordinary browsing session)

Deliberately NOT in L0 (each fails the historical/platform check):

- **Reader-mode extraction at save time** — the platform pole (Safari Reading List) holds the webpage itself and leaves cleanup to a separate Reader mode; extraction is the dominant modern implementation of "content held presentable", not the invariant. Its failure mode is a documented, designed-for event (Wallabag fetch errors; Reader partial parsing).
- **Archive as a distinct retention zone** — Safari marks read and lets entries be deleted; no archive object exists. Unread/read + removal is the invariant; archive/favorites layering is maturity.
- **Tags / folders** — absent in Safari Reading List entirely.
- **Highlights/annotations** — absent at the platform pole; maturity layer.
- **Accounts / cloud sync** — Safari Reading List is platform-local with iCloud as an option; the queue exists on one device.
- **Offline caching** — near-universal in dedicated products, but it is the *reason* the content is held, not a separate invariant; the holding leg already covers it.
- **Reading-time estimates, TTS, transcription, AI, ingestion breadth (RSS/newsletters), recommendations** — era/variant machinery.

### L1 — Common Mature Structure

- **Capture machinery**: browser extension, mobile share-sheet target, bookmarklet, paste-URL form, mobile apps; import as bulk capture.
- **Extraction/clean-copy as the working object** with the original link kept on the item (Wallabag: domain opens source article; Reader: partial parsing when link-only) — plus designed failure handling: re-fetch, per-site parser configs, rendered-content fallback from the extension.
- **State model**: unread → read; starred/favorites; archived as the post-consumption zone distinct from deletion; delete + (in one product) trash/restore.
- **Reading experience**: typography/themes, distraction-free layout, reading progress/position with return-to-position (modern pole), estimated reading time, full-text search over the library, offline availability.
- **Organization**: tags as the standard organization axis; filtered/saved views at the power pole.
- **Annotation layer**: highlights and notes on the held copy (modern dedicated products); export of highlights toward note-taking systems.
- **Continuity**: multi-device sync of library, states, and (where present) progress/annotations.
- **Portability**: import from sibling services (Pocket/Instapaper/CSV/OPML) and export of the library — the category's interchange convention, forced by repeated category deaths.

### L2 — Variant / Optional Structure

- **Content-type breadth**: articles-only minimalism (classic pole) vs all-media reading (PDFs, EPUBs, video with transcript, podcasts) (modern pole).
- **Ingestion breadth**: manual save only vs subscription/newsletter intake absorbed into the same library (Reader, Matter) — the seam toward Feed Reader, held as variant.
- **Knowledge-flow orientation**: reading as input to note systems (highlight export/integration) vs reading as closed loop (clear the queue).
- **Delivery form**: hosted SaaS vs self-hosted open source vs platform-native feature inside a browser/OS.
- **Business model**: free, freemium, flat subscription, subscription-funded hosted OSS; the sustainability pitch as a market response to category mortality.
- **Power-user posture**: keyboard-driven operation, command palettes, query-syntax filtered views, APIs.

### L3 — Vendor-specific (research notes only)

- Wallabag: graby/php-readability parser stack with community XPath site-config repository (ftr-site-config); "bag it!" bookmarklet; random-entry button; tagging rules (auto-tagging); RSS output of one's own library; elCurator/Readability import sources; wallabag.it hosted arm with e-reader export and 11€/year pricing; SQLite-dropped/MySQL-default history.
- Reader: Ghostreader (GPT copilot); Readwise integration (Daily Review, spaced repetition); green "saved more than once" dot; pace-differentiated reading progress vs last location; device-specific Trash; Shortlist vs Inbox/Later configurable library; MCP server; CLI; e-ink viewing mode; Unreal Speech TTS; student/discount pricing program.
- Matter: time-synced transcription of YouTube/podcasts; quoteshots; audio highlights; "follow writers" writer graph; Gmail newsletter ingestion; Apple "App of the Day" positioning.
- Pocket: Mozilla ownership; "algotorial" recommendation engine on Firefox New Tab; 2017 acquisition (stated on shutdown page); shutdown (2025 derived from the page's "past 8 years" + 2017 acquisition); corporate entity "Read It Later, Inc."
- Safari: iCloud Reading List sync; Reader mode as the separate cleanup feature; Shift-click save gesture.

## Vendor-specific / Rejected Findings

Rejected from the canonical model:

- **"Read-it-later = reader-mode extraction"** — rejected as invariant on Safari's platform-native form plus the documented failure modes; held as dominant implementation.
- **"The Type includes content discovery/recommendations"** — rejected: Pocket's own shutdown page frames discovery as the drift away from the Type center ("evolved into something much bigger"), and the successor reading-list machinery lives in bookmarks/tab groups. Discovery = adjacent Type territory (News Aggregator / Personalized Content Feed).
- **"Library sections are named Inbox/Later/Archive"** — Reader-specific naming, configurable even within Reader; canonical statement kept at conceptual-state level (unread / read-archived / favorites).
- **"Duplicate saves are detected and merged"** — Wallabag documents re-open-on-duplicate; Reader shows a green "saved more than once" dot implying coexistence. Handling varies → kept generic.
- **"Trash is device-specific"** — Reader operational quirk; not canonical.
- **"TTS is standard"** — evidenced only at modern poles; Safari lacks it; Wallabag not evidenced. Optional/variant.
- **Instapaper-specific claims of any operational kind** — no reachable source; excluded entirely rather than filled from memory.

## Boundary Findings

1. **vs Bookmark Manager** (discharges the bookmark-manager pass's flag — keep-both ratified from this side). This pass's evidence lands exactly on the proposed seam: Wallabag's first sentence is that it keeps *content*, "not just a link that can change or disappear" (their hosted-site copy) — the extracted readable copy is the working object; the state model (unread/starred/archived + filters on reading state + reading time) is organized around *consumption*; Reader's own marketing centers on "triage for clearing… not hoard it". Safari ships bookmarks ("to revisit") and Reading List ("to read later") as two distinct features with separate guide pages — the platform-native proof that the market treats these as different jobs. Removal tests both ways recorded in the L0 section (remove reading-experience machinery → bookmark manager; remove organized-reference posture and live in the queue → read-it-later). Hybrid products exist at the seam (Pinboard's unread flag with Instapaper sync; Raindrop's reader view) and are held as overlaps, not Type mergers.
2. **vs Feed Reader** — feed readers intake by subscription (items arrive automatically, continuously, from sources); read-it-later intake is the deliberate one-off save. Reader and Matter both absorb feed/newsletter intake as a variant capability while keeping the held-library center; the e-book-reader pass already documented the handoff direction (feed reader → read-later via save/share).
3. **vs E-book Reader** — unit and acquisition differ: clipped article vs opened book; clipping vs file/store acquisition; no book structure (TOC/chapters/print mapping) in the clipped-article world. Interlock documented by the e-book-reader pass (Wallabag/KOReader plugin delivering articles into a reader surface).
4. **vs E-book Library / Reading Library Application** — the library Types hold durable content objects where retention is the normal case; read-it-later's posture is consumption and clearing, with retention the deliberate exception (favorites). The academic-paper-reader pass's phrasing (identity+library model vs inbox model) is adopted and corroborated.
5. **vs Academic Paper Reader** — the scholarly collection carries scholarly identity (venue/authors/citation machinery); a read-it-later item is a generic document. Reader straddles functionally (PDF support) without the identity layer, exactly as that pass recorded.
6. **vs News Aggregator / Personalized Content Feed** — machine-assembled, source- or interest-driven flow vs the user's own saved queue; Pocket's recommendation-era pivot documents the drift path and its endpoint (the reading-list core got shut down; discovery was folded into the browser).
7. **vs PDF / Document Reader** — document-centric work (annotation on the document as the object of record) vs the queue item as unit; one product (Reader) does both by making the PDF a document type inside the queue.
8. **vs To-do/task tools** — superficial resemblance of the queue posture; items are content to consume, not work to complete; no assignment/delegation/scheduling machinery. Not a boundary flag — recorded to preempt confusion.

Taxonomy note: the leaf is a coherent standalone Type. The category is contracting (Pocket, Omnivore shut down; Mozilla redirected reading lists into browser features), but the market still sustains dedicated products across the hosted/self-hosted/premium/consumer spectrum plus platform-native realizations, and its defining structure differs from every neighbor's.

## Uncertainties

1. **Instapaper operational behavior unverifiable** — site unreachable twice on 2026-09-08; nothing operational asserted about it anywhere. Its role is archetype/history; import paths in other vendors' docs corroborate category membership only.
2. **Pocket operational details** — only the shutdown page was reachable; historical features (save button mechanics, offline, tags) are NOT asserted from memory.
3. **Matter operational depth** — positioning page only; no operational claims drawn.
4. **Universality of reading-time estimates** — Wallabag (filter by reading time) and Reader (reading length in filtered views) evidence existence at two poles; TTS universality unknown; written as common-at-modern-pole, hedged.
5. **Whether favorites-vs-archive layering is universal in dedicated products** — evidenced in Wallabag (starred/archived), Reader (Pinned/Shortlist/Archive); Matter positioning-level; Safari lacks it. Held L1 with Safari as the recorded exception.
6. **Instapaper/Pinboard as hybrid seam products** — corroborated only via other vendors' import docs; treated as overlap evidence, not behavior evidence.

## Final Synthesis

A Read-it-later Application is, at minimum: **an application that captures content from elsewhere by deliberate save acts, holds each saved item together with its content in a presentable form on a personal queue organized around deferred reading (unread → read, archive/remove after consumption, favorites as the retention exception), and presents that content itself for in-app reading.** Save now, read later, clear when done is the defining loop; the queue's health is measured by items consumed, not accumulated.

Around that core, mature dedicated products add: frictionless capture machinery (extensions, share sheets, bookmarklets, paste, import), reader-mode extraction with the original link kept and designed failure handling, the unread/starred/archive state layer, reading-comfort controls, reading progress, offline availability, multi-device continuity, tags and filtered views, an annotation layer feeding knowledge tools, full-text search, text-to-speech, and standardized import/export. Variants divide along content breadth (articles-only vs all-media), ingestion breadth (manual saves vs absorbed RSS/newsletters), knowledge-flow orientation, delivery form (hosted / self-hosted / platform-native), and business model. The platform-native form (browser reading lists) satisfies the core with none of the maturity layers — the strongest evidence that the definition is the queue-plus-reading structure and nothing more.
