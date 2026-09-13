# Personalized News Feed

## Overview

A **Personalized News Feed** is a news-consumption application that assembles, for each individual user, a personal flow of news stories drawn from many publishers — selecting the stories through the product's own machinery, weighted by signals about that user (the topics, publications, and teams they follow, the reading behavior they generate, their location, and their explicit more/fewer feedback), and re-assembling the flow as those signals accumulate.

Its purpose is news without a curated front page made just for everyone: the user opens the feed to catch up on what matters *to them*, and the product does the choosing — differently for every user. Two people opening the same product see two different flows, and the same person's flow changes as their reading and declared interests change.

The defining structure is small:

```text
Sourced news corpus — journalistic stories from multiple identifiable
  publishers (each item carries its source)
└── Per-user selection
    (the product's machinery weighs stories by signals about the
     individual user, so each user's flow is their own)
    └── The personal news flow
        (a standing consumption surface, re-assembled as signals accumulate)
```

Everything else commonly associated with modern news apps — editor-picked top stories beside the feed, local news sections, sports scores, "show fewer like this" buttons, notifications, subscriptions, advertising — is widespread but not part of the defining core. A personal newspaper service that cuts each subscriber a daily digest according to a stated interest profile satisfies the same structure with no software at all.

When the product assembles one news flow shared by everyone, it is a **News Aggregator**. When the stories all come from the product's own newsroom, it is a **News Application**. When the user's own list of sources is delivered faithfully, it is a **Feed Reader**. These seams are described under Related Application Types.

## Users & Context

The primary user is an **individual consuming news as an audience member**. No connections to other people are needed: the flow works from the first session. The user's role is to read and react — open, save, share, follow, ask for more or less — and every reaction is also an input to the next assembly of their flow.

Typical reasons to open the application:

- catch up on current events filtered to personal interests, without scanning a full front page;
- follow specific topics, publications, sports teams, or local news without managing a subscription list;
- return after an absence and find the flow updated to match recent reading.

A secondary constituency is **publishers** whose stories fill the corpus — being selected into feeds is distribution for them — and, in products that run one, an editorial staff that selects the shared top-stories layer beside the personal flow.

The typical context is short, frequent sessions on a phone, with desktop, tablet, and companion surfaces (car, watch, lock screen) common in mature products.

## Core Model

### The Defining Core

Three structures. If any one is removed, the product is no longer recognizable as a personalized news feed:

- **A sourced news corpus** — journalistic stories about current events drawn from multiple identifiable publishers. The product feeds the news; it does not have to be the publisher. Each item carries its source: provenance is part of what makes it news consumption rather than a content stream. Without a multi-publisher news corpus there is nothing to select from — a single publisher's surface is a publisher app, and an unattributed rehost of news is not a news feed at all.
- **Per-user selection** — the product's selection machinery weighs corpus stories by signals about the individual user: **interests the user declares** (following topics, publications, teams), **behavior the user generates** (what they open, read, save, hide), **location** where local relevance is supported, and **explicit feedback** ("show more/fewer like this"). Selection happens *between stories across the corpus* — the product decides which stories this user sees, and the user did not enumerate the candidates. Following a publication here does not mean receiving everything it publishes; it means the machinery treats it as a strong signal. Without per-user selection, the flow is shared by everyone (an aggregator) or a faithful delivery of the user's own list (a reader).
- **The personal news flow as a standing, updating surface** — each user's flow persists between sessions and is re-assembled as signals accumulate. Without this, personalization degrades into a one-shot personal newspaper edition; the *feed* is gone.

### The Objects

- **Story (the flowing unit)** — a news item with its headline, its publisher, usually imagery and recency, and topic labels. Stories are not authored in the feed surface; they arrive from the corpus.
- **Publisher (channel)** — the source publication, elevated to a first-class object in the model: in a documented implementation the publisher can be followed, blocked, and subscribed to individually, and a story links back to its channel. Provenance is therefore navigable, not just a byline.
- **Topic** — a subject space (science, travel, politics…) that organizes both the corpus and the user's declarations.
- **Signals** — the user's trace: declarations (follows), behavior, location, explicit feedback. Signals accumulate on a persistent per-user identity, which is why the flow improves over time.
- **Selection machinery** — whatever weighs corpus stories against signals to produce the flow: learned models, simpler rules over followed topics, or hybrid editorial-plus-algorithm assembly. The Type requires that the *product* selects *for this user* from *that user's signals* — not any particular technique.
- **The flow** — the assembled artifact each user sees: standing, personal, and never complete. Stories outside the selection are simply not seen.
- **The editorial layer (standard, not core)** — a shared surface of editor-selected top stories and trending coverage that mature news products commonly run beside the personal flow, sometimes inside it.

### Standard Capabilities

These are widespread in mature products. They make the feed work well, but they are not what makes a feed personalized.

- **Editorial surfaces beside the flow** — editor-picked top stories, trending coverage, spotlight event coverage. In one documented implementation the home feed literally mixes editor-selected top stories with stories from followed channels, and an option exists to restrict the feed to followed channels only — which also removes the editorial items.
- **Declared-interest inputs** — following topics, publications, and teams/leagues; the documented causal effect is that followed sources' stories "appear more often" in the feed, and following helps the product "better understand your interests."
- **Per-story feedback** — "show more stories like this" / "show fewer stories like this," recorded visibly against the story in the feed and reading history.
- **Negative controls** — blocking publications or topics; stopping a surfaced suggestion from appearing again.
- **Suggestions and cold-start handling** — suggested publications/topics seeded from platform signals or the user's own actions; default and onboarding content until signals accumulate.
- **Local news** — curated and personalized local stories selected by location, typically region-gated.
- **Retention handoff** — save stories for later; share stories (and surfaces for stories shared with you); notifications for breaking or followed news.
- **Reading history** — a user-visible, clearable record of what was read (which doubles as a signal-management surface).
- **Search** — finding publications, topics, or specific stories beside the standing flow.
- **Multi-surface delivery** — phone, tablet, desktop, and companion surfaces with the flow synced across devices.

### One Structure, Many Implementations

The core is written conceptually; the Variants section enumerates how products realize it.

```text
Concept:   Selection machinery
Implementations:  learned ranking models, rules over followed topics,
                  hybrid editorial+algorithm assembly

Concept:   Signals
Implementations:  followed topics/publishers/teams (declaration),
                  opens/reads/saves/hides (behavior), location,
                  explicit more/fewer feedback

Concept:   Provenance
Implementations:  hosted in-app with publisher branding,
                  link-out to the publisher's site, hybrid

Concept:   Packaging
Implementations:  standalone news feed apps, platform-native preinstalled
                  apps, personalized feed surfaces inside portals/start pages
```

## How It Works

### Signal accumulation and the personal flow

The defining loop runs continuously and is invisible as a "workflow" — the user just reads:

```text
First session: no signals yet
→ the feed falls back to defaults (top stories, suggested topics,
  onboarding picks)
→ the user reads, follows, saves, hides, gives more/fewer feedback
→ signals accumulate on the user's identity
→ the next assembly of the flow weighs corpus stories against those signals
→ the flow the user returns to is different from the one they left
```

Two properties follow. First, the flow is **never complete** — the product promises relevance to this user, not coverage; stories outside the selection are absent. Second, the flow is **re-computed, not fixed** — what the user saw this morning is not what they see tonight, and no other user sees the same sequence.

### Declaring interests

Following topics, publications, or teams shapes selection across the whole corpus — it does not guarantee delivery of everything under that topic. The contrast with a subscription list is visible inside one documented product: an optional mode restricts the home feed to followed channels only, and when the user exercises it, the shared editorial items (top stories, trending) disappear — the feed drifts toward reader behavior. Default mode remains selection.

### Steering the model

The user steers what the machinery sees: follow or unfollow, block publications or topics, stop a suggestion, ask for more or fewer stories like the current one, and clear reading history. Consuming *is* configuring — reading a story is itself a signal, whether or not the product makes that visible. The same mechanism creates a privacy surface: where signals are processed (on the device vs in the cloud) is a product posture, and mature products expose controls over signal use.

### The editorial layer's role

Mature news products commonly run a shared editorial surface — top stories, trending — beside, or inside, the personal flow. The shared layer serves the "what's happening now" job; the personal flow serves the "what matters to me" job. Products differ in how much the two interleave; the coexistence is standard news-product structure, not a requirement of the Type.

### Core vs Common vs Optional

**Defining core** — without these, not a personalized news feed:

- sourced news corpus from multiple identifiable publishers (items carry their source)
- per-user selection from that user's signals
- the personal news flow: standing, updating, individual

**Common mature structure** — present in most modern products:

- editorial surfaces beside the flow (top stories / trending)
- declared-interest inputs (follow topics/publications/teams)
- per-story feedback and negative controls (more/fewer, block, stop suggesting)
- suggestions and cold-start defaults
- local news with location relevance
- retention handoff (save, share, notifications)
- reading history; search; multi-surface delivery with sync

**Variant / optional** — depends on product, packaging, and market:

- hosting model (in-app licensed vs link-out)
- signal-processing posture (on-device vs cloud)
- commercial packaging (premium tiers, channel subscriptions, ads)
- vertical modules (sports scores, weather, audio briefings, newsletters, puzzles)
- portal or platform embedding; regional editions

## Interfaces

The following surfaces are described conceptually. Exact layouts and names vary by product.

### The personal feed (home)

The primary surface.

- Purpose: present this user's assembled news flow.
- Typical information: an ordered stream of story cards — headline, publisher mark, imagery, recency, topic labels — sometimes interleaved with editor-selected items and module rows (local, sports).
- Primary actions: open the story, give more/fewer feedback, save, share, follow or block the publisher, go to the publisher's channel.

### Editorial surface (top stories)

- Purpose: the shared, editor-selected view of the day.
- Typical information: ranked top stories, trending coverage, spotlight event coverage.
- Primary actions: read, save, share, follow the underlying topics.

### Story view

- Purpose: consume one story fully.
- Typical information: the story (hosted in the app or handed off to the publisher), its publication, related stories, feedback controls.
- Primary actions: read/watch, suggest more or fewer like this, save, share, report a concern, open the publisher.

### Following / interests management

- Purpose: declare and adjust what the machinery treats as signals.
- Typical information: followed publications, topics, teams; suggested additions; blocked items.
- Primary actions: follow/unfollow, favorite, block/unblock, stop suggesting, rearrange.

### Local news

- Purpose: surface coverage of the user's area.
- Typical information: local stories selected by location, often with weather.
- Primary actions: read, follow local publications, adjust location.

### Search

- Purpose: find publications, topics, or specific stories on demand.
- Typical information: results for the entered query, browsable topic spaces.
- Primary actions: search, open results, follow what is found.

### Settings / privacy

- Purpose: control how the flow behaves and how signals are used.
- Typical information: feed restriction options (e.g., show only followed channels), explicit-content filtering, notification controls, reading-history management, signal/privacy posture.
- Primary actions: toggle options, clear history, manage notifications.

## Important Rules / Behaviors

### Selection replaces completeness

The flow never promises to show everything from anywhere. What it promises is relevance to this user, and it keeps that promise by omitting. This is a defining behavioral contrast with the subscription reader, which delivers everything its list publishes.

### Declaration is a strong signal, not a subscription

Following a publication or topic raises the presence of that publisher's or subject's stories in the flow; it does not transfer the publication's full output. The user who wants faithful delivery restricts the feed to followed channels (where the option exists) and accepts the loss of editorial items — the documented trade-off of the one deeply researched implementation.

### Feedback is recorded and visible

More/fewer requests, blocks, and stops are recorded against the user's identity and visibly marked in the feed and history in the documented implementation. Reactions work in both directions: they change future assemblies of the flow.

### Provenance travels with the story

Every story shows its publisher, and the publisher is a navigable object (go to channel, follow, block, subscribe). Whether the story text lives in the app or on the publisher's site varies by product; the visible source does not.

### The editorial layer and the personal flow are distinct selections

Editor-picked items are chosen for everyone; personal items are chosen per user. Products that interleave them still separate the mechanisms — and some expose the difference by letting the user strip the editorial layer from the personal feed.

### Signals persist and are manageable

Reading behavior accumulates on the user's identity across sessions and devices. Mature products expose a reading history that can be viewed and cleared, and posture statements about where personalization happens (on-device vs server-side) differ by product.

### Availability is regional

News feed products commonly gate content and features by country/region (local news, publishers, licensing) — the same product can offer different corpora and capabilities in different markets.

## Variants

- **Platform-native feed apps** — preinstalled news surfaces bound to a device platform's account and ecosystem, with editor-plus-algorithm assembly and strong privacy posture (e.g. Apple News).
- **Search-giant algorithmic feeds** — feeds run by search engines beside their headline surfaces, personalization-led (e.g. Google News — positioning verified this research; feature detail not directly examined).
- **Lightweight download-first apps** — small, fast, algorithm-led news apps (e.g. SmartNews — market anchor; not directly examined this research).
- **Magazine-hybrid products** — feeds interleaved with user-assembled "magazines" or collections, shading toward curation (e.g. Flipboard — market anchor; not directly examined this research).
- **Portal-embedded feed surfaces** — personalized news streams inside portals and start pages; the feed is one module of a wider entry surface (shades toward Information Portal unless the stream is the primary artifact).
- **Regional superapp feeds** — news flows embedded in larger content or superapp ecosystems; regional poles exist beyond the samples examined here.

A variant remains a variant unless it changes users, core objects, or rules so much that the core model no longer applies — as when the corpus collapses to a single publisher (News Application) or selection becomes shared for everyone (News Aggregator).

## Related Application Types

| Application Type | Distinction |
|---|---|
| News Aggregator | the product's machinery assembles one news flow shared by everyone (per-user feeds at most an optional tuning layer); here per-user assembly is the core, and the product must fall back to defaults when a user has no signals |
| News Application | a single publisher's own product — the newsroom's editorial output, editions, and subscriptions; here the corpus is multi-publisher and the product's job is feeding, not authoring |
| Personalized Content Feed | the same selection machinery across all content kinds, with origin display as standard structure; here the corpus is restricted to publisher journalism and provenance is part of the recognizable core |
| Feed Reader | the user's subscription list is the sole selector, delivering what those sources publish completely and in order; here follows are inputs to selection across a corpus the user never enumerated |
| Content Aggregator | same shared-flow distinction as the news aggregator, for general content; attribution is its essence while per-user selection is absent |
| Information Portal | the whole entry surface — content, services, routing, start-page role; keep only the personalized article stream and it becomes this Type |
| General Social Network (and short-form video social) | the connection graph is the distribution substrate and the user joins as a member; here the user is an audience member whose signals select from a publisher corpus |
| General Web Search Engine | per-query transient results vs query-free standing personal flow; search may live beside the flow as a separate surface |
| Content Curation Platform | a curator selects items into persistent named collections; here there is no curator and no collection artifact — a standing per-user flow |
| Bookmark Manager / Read-it-later | personal retention of deliberately saved items; the feed's save actions are the handoff toward those tools |

The most important boundary inside the news section of the directory is with the **News Aggregator**, because one product commonly hosts both surfaces: a shared editor/machine-selected front page *and* a per-user flow. The structural test is whether the primary flow is assembled per user from that user's signals (this Type) or assembled once for everyone (aggregator).

## Representative Products

- **Apple News** — directly documented for this research (User Guide + product page): the Today feed mixing editor-selected top stories with followed-channel stories, channel/topic/team following, per-story more/fewer feedback, block and stop-suggesting controls, restrict-to-followed mode, local news, My Sports, on-device personalization posture.
- **Google News** — the search-giant pole: officially positioned as "organizing what's happening in the world to help you learn about the stories that matter." Feature documentation was not reachable during this research; no feature claims are made.
- **SmartNews, Flipboard, Microsoft Start** — market anchors for the lightweight-algorithmic, magazine-hybrid, and portal-descendant poles respectively. Not directly verifiable during this research; listed for orientation only.

## Sources

Research date: **2026-09-08**

Fetched directly:

- Apple — Apple News User Guide (macOS): Welcome — https://support.apple.com/guide/news/welcome (channels/topics structure; Today feed; saved stories; reading history)
- Apple — Follow and unfollow channels and topics — https://support.apple.com/guide/news/follow-and-unfollow-channels-and-topics-iph776e48d55/mac
- Apple — See more or fewer stories like the current one — https://support.apple.com/guide/news/stories-current-iph1ddb4a8aa/mac
- Apple — Explore channels, topics, and stories — https://support.apple.com/guide/news/explore-channels-topics-and-stories-iph523395af1/mac
- Apple — Change settings — https://support.apple.com/guide/news/change-settings-iphca74e7adb/mac
- Apple — Apple News product page — https://www.apple.com/apple-news/
- Google — Google News product blog index — https://blog.google/products/news/ (positioning sentence)

Family and boundary evidence recorded at first-hand in the processed sibling passes for the feeds-and-curation family (Personalized Content Feed, Content Aggregator, Feed Reader, Content Curation Platform, Information Portal), including vendor positioning that defines each pole against the others.

> Sourcing limitation: only Apple News could be documented first-hand this pass. Google's support surfaces, the Google News product site, SmartNews, Flipboard, Microsoft Start, and all encyclopedic/historical references (Wikipedia, web archives) were unreachable from the research environment (repeated timeouts; abandoned after the standard retry limit). No operational claims are made about those products; claims resting on the single deeply documented product are qualified in place ("documented implementation", "one product"), and market-level statements are drawn from the sibling passes' first-hand evidence. The historical argument (personal newspaper/clipping services) is conceptual for the same reason.

Detailed evidence, product-by-product observations, the cross-product comparison, and the full boundary analysis — including the joint-review conclusions for the feeds-and-curation family — are recorded in the paired Research Notes.
