# Feed Reader

## Overview

A **Feed Reader** is a personal application for following published content. The user assembles their own list of sources — blogs, news sites, journals, podcasts, video channels, newsletters — and the reader continuously brings in whatever those sources publish, presenting the arriving items in a single reading surface with per-item reading state.

The defining core is small:

```text
User-managed subscription list
  └── Source (an external publisher the user chose)
        └── Item (what the source publishes: article, post, episode, video)
              └── Reading state (unread / read / saved)
```

Three properties make the Type what it is. **The user's own list** decides what enters the application — the reader's job is faithful intake of the sources the user chose, not selection on the user's behalf. **Standing automated intake** — new items arrive on their own as sources publish; nothing depends on the user remembering to check, and nothing needs to be captured by hand. **A consumption surface with reading state** — the reader shows what has arrived, tracks what has been read, and lets the user read in place or continue at the source.

The reader solves a specific problem: keeping up with many publishing sources without visiting each site in turn, without relying on memory, and — in the philosophy most products state explicitly — without an algorithm deciding what is worth seeing.

When the product's own machinery rather than the user's list decides what enters the surface, it is a Content Aggregator or a Personalized Content Feed. When items only appear through deliberate one-off saving, it is a Bookmark Manager. Those seams are described under Related Application Types.

## Users & Context

The primary user is an individual who follows more sources than they can visit: a reader who tracks dozens of blogs and news sites, a developer following release notes and technical blogs, a researcher following journal tables of contents, a listener following podcasts, a professional monitoring a set of industry publications.

Typical sessions:

- open the reader and triage what arrived since last time (scan unread items, read some, skim others, mark the rest read)
- read an article in full inside the reader, or jump to the source site
- star or save an item worth keeping
- occasionally add a new source, reorganize the list, or prune sources that have gone quiet

The work environment is a mix of desktop reading sessions (where keyboard-driven triage shines) and mobile catch-up. How state travels between devices depends on the product's architecture: a hosted service or self-hosted server synchronizes it, while a local-only reader keeps it on one machine.

There is no team, audience, or organizational container anywhere in the core loop. The subscription list, the items, and the reading state belong to one person.

## Core Model

### The defining core

**Subscription list.** The central managed object: a durable, personal list of content sources. The user adds sources, organizes them (folders, categories, or tags in most mature products), and prunes them. The list persists across sessions and — in networked products — across devices. It is simultaneously the user interface and the selector: nothing appears on the reading surface that does not trace back to an entry on this list.

**Source.** An external publisher whose stream the user follows. Conceptually it is any entity that publishes a sequence of items. The common implementation is a machine-readable feed in RSS, Atom, or JSON Feed format, but the concept is wider: some products also accept sources implemented as scraped web pages that have no feed, email addresses (newsletters delivered to a per-user intake address), YouTube channels and playlists, or social accounts.

**Item.** The unit a source publishes — an article, blog post, news story, episode, or video. An item typically carries a title, a publication date, the content itself or a synopsis, and a link back to the source. Feed formats identify each item so the reader can recognize an item it has already seen and not show it twice. Items may carry attached media (enclosures), which is how audio and video publishing travels through the same machinery. The item is owned by the source, not the reader: the reader's copy is a reference plus (usually) a stored rendering, and items often remain readable in the reader even after the source page changes.

**Reading state.** The per-item state machine that makes triage possible: unread until consumed, then read (with "keep unread" as the escape hatch), and a separate long-term layer for items worth keeping (starred / bookmarked). Aggregate unread counts per source and overall are the reader's pulse. This state belongs to the reader and the user — the source site knows nothing of it.

### What mature products add

These capabilities are widespread and expected, but they are refinements rather than the definition:

- **Smart and dynamic views** — "all unread", "today", saved searches: queries over the item store rather than physical folders.
- **Full-content handling** — a reader view or readability extraction that renders the complete article when a source publishes only summaries, so reading can happen without leaving the application; opening the source site remains the alternative.
- **Search** over the accumulated item store.
- **OPML import/export** — the standard interchange for the subscription list, which makes the list portable between readers.
- **Sharing outward** — send an item to a read-it-later service, notes app, mail, or social target.
- **Synchronization** — a hosted service, a self-hosted server, or a platform sync service that carries subscriptions and reading state across devices and across third-party client applications.

### One structure, many implementations

The core is written conceptually. Implementations vary per concept:

```text
Concept:   Source
Implementations:   RSS/Atom/JSON Feed URL · scraped page (no feed available) ·
                   newsletter email address · YouTube channel or playlist · social account

Concept:   Standing intake
Implementations:   periodic checking by the reader or a server ·
                   real-time push (publish–subscribe protocols) · email-in delivery

Concept:   Storage and sync
Implementations:   local application store · hosted service · self-hosted server ·
                   service + third-party client apps speaking a sync protocol
```

A reader of any era fits the same core: a local desktop application with no account reading RSS feeds satisfies it exactly as a hosted web service does.

## How It Works

### Subscribe

```text
Choose a source
→ enter the site's address or its feed URL (the reader discovers the feed from the site)
→ or import an OPML file of subscriptions from another reader
→ or use a dedicated intake channel (a personal email address for newsletters, a browser extension button)
→ the source joins the list, optionally inside a folder or category
```

### Intake

The reader — or the server behind it — checks the subscribed sources continuously and pulls in new items as they are published. The user does nothing; this is the standing part of the loop. Items enter the store with their source, date, and unread state. Some hosted products also track sources that publish through email or through pages that must be scraped, and a few re-fetch items whose content changed at the source and show what changed.

### Triage and read

```text
Open the reader → see what is unread (per source, or in a combined view)
→ scan headlines → read in place (or in the reader view if the feed is summary-only)
→ or open the item at its source site
→ mark items read as you go (individually, or everything in view at once)
→ star or save the keepers → share the ones worth passing on
```

Keyboard-driven triage — next item, next source, mark read, star, without leaving the keyboard — is a hallmark of desktop readers; the sampled products document it on both the native and the web side.

### Organize and maintain

Subscriptions are living furniture: group them into folders or categories, build saved queries over the item store, and prune. Sources die — sites fold, feeds move, publishers stop — and the user is the maintainer of the list. Some products help by surfacing stale feeds with diagnostics (when a feed last delivered an item and how its server responds) so the user can decide what to delete.

### Carry state across devices and apps

In networked products, subscriptions and reading state live on a service (hosted or self-hosted) and synchronize to web and native clients. The ecosystem is unusually interoperable: the same account often serves several different client applications, and subscription lists move between entire products via OPML.

## Interfaces

Exact layouts differ, but the same surfaces recur:

**Subscription sidebar**
The list itself as an interface: sources grouped in folders or categories, each showing its unread count.
Primary actions: add, organize, and delete subscriptions; open a source's items.

**Timeline / item list**
The items of one source, a folder, or a smart view, in chronological order with read/unread marking.
Primary actions: open an item, mark read/unread, star, bulk mark-as-read.

**Article view**
The item's content: text, images, attached media where present, attribution and a link to the source.
Primary actions: read, open at source, star, share, save outward.

**Smart views and search**
"All unread", "today", saved searches — standing queries over the whole store rather than folders.
Primary actions: run, save, and refine queries; triage results like any list.

**Subscription management / settings**
Feed details, intake behavior, refresh settings, OPML import/export, sync account configuration.

## Important Rules / Behaviors

- **The list is the selector.** The reader shows what the user's subscriptions deliver — no editorial selection, no algorithmic insertion of unrequested items. Products differ in optional extras around this core, but the stream itself is the user's list made flesh. This is the structural line between a reader and an aggregator.
- **Reading state is the user's, and it is central.** Unread/read is a first-class, user-visible state on every item, with bulk "mark all read" and "keep unread" as standard escapes. The unread count is the primary signal that draws the user back.
- **Items are attributed references.** Content arrives with its source attached; reading in place and reading at the source are both normal, and the link back is never lost.
- **Items are recognized across fetches.** Feed formats carry per-item identifiers precisely so the reader can avoid re-showing an item it has already delivered; this is what makes repeated checking safe.
- **The stream persists independently of the source.** What the reader has received stays readable in the reader even if the source page later changes or the site disappears — within whatever retention the product offers.
- **Subscriptions require maintenance.** Sources go quiet or vanish. The user decides when a silent feed is finished; some products surface stale feeds and delivery errors to support that judgment, and deletion of dead subscriptions is a normal act, not an exceptional one.
- **Saved ≠ unread.** The starred/bookmarked layer deliberately separates "worth keeping" from "not yet consumed"; marking read and keeping are independent acts.

## Variants

Common shapes the Type takes:

- **Local native reader** — a desktop or mobile application that fetches feeds itself and keeps everything on the device; no account required.
- **Hosted service** — the provider's servers do the fetching and hold subscriptions and state; a web reader plus native client apps consume it. Hosted services often double as sync backends for third-party client apps.
- **Self-hosted reader** — the same server role, run by the user or a community instance; ranges from single-user minimalism to multi-user installations.
- **Minimalist reader** — deliberately reduced to the unread triage loop and clean typography.
- **Filtered / rules-driven reader** — intake rules (auto-mark-read, auto-star, notifications, include/exclude filters, scraper rules for feedless sites) to tame high-volume subscription lists.
- **Multi-source reader** — intake broadened beyond feeds: email newsletters via a personal intake address, YouTube channels and playlists, social accounts, scraped pages.
- **Enclosure-heavy usage** — readers used primarily for podcasts and video channels, where items carry playable media and playback position becomes part of the item state.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Content Aggregator | the product's own machinery (editors, scoring, clustering) selects and ranks items from a broad source base; in a reader, the user's subscription list is the only selector |
| Personalized Content Feed | the flow is assembled per user by interest inference; a reader's flow comes from an explicit list the user manages |
| Content Curation Platform | the managed artifact is a selectively built collection presented to an audience; the reader's artifact is a personal consumption stream |
| Bookmark Manager | holds deliberate one-off captures; the reader's items arrive automatically and continuously from subscriptions |
| Read-it-later Application | a deferred-reading queue built from deliberate saves; readers commonly hand items *to* it, but the standing stream is the reader's side |
| Email Client | an inbox-like list is superficial resemblance only: no addressing, no reply, no envelope; newsletters read through a reader have become sources, not correspondence |
| News Aggregator | same product-assembled machinery as the aggregator, scoped to news; the reader's scope is whatever the user subscribes to |
| Podcast Platform | an enclosure-first Type whose primary job is audio playback and show/episode discovery; text-oriented readers handle enclosures as a secondary capability |
| Social Network | the flow is ordered by a follow graph and product ranking; social accounts may serve as reader *sources* without the product becoming social |
| Web Browser | visits pages and may offer subscription entry points; it holds no standing item store, no subscription list, and no reading state |

The closest boundary inside the feeds-and-curation family is the one with the Content Aggregator, and the test is structural: **who assembles the item-level flow** — the user's own subscription list (reader) or the product's machinery (aggregator). Products in the market sometimes operate both models side by side, which is why the two Types are easily conflated in everyday vocabulary.

## Representative Products

- **NetNewsWire** — free open-source native reader for Mac/iOS; runs account-free on one device or synchronizes through a choice of services; documents the classic triage loop and feed-maintenance surfaces.
- **Feedbin** — paid hosted reader and sync service; documents broadened intake (newsletters via a personal address, YouTube, Mastodon), intake rules, and the service-plus-third-party-clients architecture.
- **Miniflux** — self-hosted minimalist reader; documents the unread-centric web surface, readability extraction, filters, and compatibility with established sync protocols.
- **FreshRSS** — self-hosted multi-user reader; documents scraped-page intake, filter-generated feeds, and real-time push updates.

The market also includes larger SaaS readers and sync services (e.g., Feedly, Inoreader); their documentation could not be reached during research for this document, so no claims in this document rest on them.

## Sources

Research date: **2026-09-07**

- NetNewsWire — homepage https://netnewswire.com/ ; "What is RSS? What are feeds?" https://netnewswire.com/help/what-is-rss.html ; "Get started with NetNewsWire 6 for Mac" https://netnewswire.com/help/mac/6.1/en/getting-started.html ; "How to Find Stale Feeds with the Dinosaurs Window" https://netnewswire.com/help/dinosaurs.html ; help index https://netnewswire.com/help/
- Feedbin — homepage (feature descriptions) https://feedbin.com/
- Miniflux — homepage https://miniflux.app/ ; features https://miniflux.app/features.html
- FreshRSS — homepage https://freshrss.org/
- RSS Advisory Board — RSS 2.0 Specification https://www.rssboard.org/rss-specification
- OPML — https://opml.org/ (canonical subscription-list example; spec body not retrievable)

> Sourcing limitation: the official sites of several large SaaS readers (Feedly, Inoreader, NewsBlur) were unreachable during research (repeated timeouts). Claims in this document are calibrated accordingly: the defining structure and standard capabilities rest on the four documented products above, product-specific depth is attributed to those products, and no operational details are asserted for the unreachable vendors. The OPML specification body was likewise not retrievable; OPML is evidenced through its implementation in the sampled readers.

Detailed evidence, product-by-product observations, the cross-product comparison, and the boundary analysis against the sibling Types are recorded in the paired Research Notes.
