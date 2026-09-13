# News Aggregator

## Overview

A **News Aggregator** is a consumption application that assembles a shared, continuously refilled flow of news stories drawn from many identifiable publishers, using the product's own assembly machinery — human editors, ranking algorithms, clustering, crawling, or a combination — so that every reader sees the same assembled flow.

The defining structure is small:

```text
Sourced news corpus (stories from multiple identifiable publishers,
each carrying its source)
└── Shared product-side assembly (editors / ranking / clustering /
    crawling — the flow is the same for every reader)
    └── The standing news flow (a continuously refilled surface)
```

Everything commonly associated with modern news aggregation — machine-learned ranking, story clustering with source counts, personal feeds, apps, accounts — is widespread in current products but is not part of the defining core. A single-editor headline site, a machinery-only automated feed, and the edited wire-service digest all fit this definition without any of those specifics.

When the flow becomes assembled *per user* from that user's signals, the product is drifting toward a different Application Type (Personalized News Feed). When the user's own subscription list becomes the sole selector, it is a Feed Reader. When the product is the publisher of what it shows, it is a News Application.

## Users & Context

The primary user is an individual who wants to keep up with what is happening — a reader scanning a standing flow of current stories rather than searching for a specific fact or following a personal interest profile.

Typical reasons to open the application:

- scan what is rising across many publishers right now
- see one story's coverage from multiple outlets
- check a topic section of interest (tech, politics, sports, business)
- follow a link out to the originating publisher for the full report

The user is an audience member of an editorially or algorithmically assembled flow — not a member of a social graph, not a subscriber curating a personal list. The work environment is dominated by the web and mobile apps; newsletter delivery is a common companion channel.

## Core Model

### The Defining Core

```text
Sourced news corpus
└── Shared product-side assembly
    └── The standing news flow
```

Three properties, held together. If any one is removed, the product is no longer recognizable as a news aggregator:

- **Sourced news corpus** — journalistic stories about current events drawn from multiple identifiable publishers. The product feeds the news; it does not have to be the publisher. Each story carries its source — provenance is structural, not decorative. Without the multi-publisher corpus, the product is a single publisher's application; without visible provenance, it is not aggregation at all.
- **Shared product-side assembly** — the product's machinery selects, merges, and orders the flow: editors making final calls, scoring models ranking candidates, clustering merging duplicate coverage, crawlers collecting raw articles. The assembled flow is the same for every reader. Per-user selection may exist as an optional tuning layer beside it, but it is not what assembles the flow. Without shared assembly, the product is a personalized feed (per-user selection) or a feed reader (the user's list).
- **The standing news flow** — a continuously refilled consumption surface, not a one-shot digest or a per-query result. The flow updates as new coverage arrives.

### The Story as the Unit

The unit of the flow is the **story** — typically a cluster of publisher articles about the same event, presented as one entry with its sources attached. Mature products commonly make the cluster explicit: one headline with a count of covering outlets and links to each. The source is a first-class object in the model — visible on every story, and in some products ranked and surfaced in its own right.

### One Structure, Many Implementations

The core model is written in conceptual terms. Implementations vary:

```text
Concept:          Shared assembly machinery
Implementations:  editors making final calls, ranking/scoring models,
                  meaning-based clustering, crawlers — in any combination

Concept:          Sourced corpus
Implementations:  crawled publisher articles, feeds, licensed content

Concept:          The flow's surface
Implementations:  ranked front page, reverse-chronological river,
                  topic sections, newsletter editions
```

A reader who only encounters one implementation (e.g. an algorithmic news app) should still be able to recognize an editor-led headline site or a machinery-only automated feed from the core model.

## How It Works

### Collect and assemble

```text
Crawl / collect articles from many publishers
→ group coverage of the same event into one story
→ score stories (freshness, breadth of coverage, source authority, velocity)
→ editors make final calls on what leads and how headlines read
→ the assembled flow renders, the same for every reader
→ re-assemble continuously as new coverage arrives
```

The machinery composition varies: some products put editors at the top of the loop with software beneath; some run entirely on software; most combine both. The invariant is that the product — not the reader — assembles the flow, and assembles it once for everyone.

### Consume

```text
Open the flow (front page / topic section / river)
→ scan assembled stories with their sources visible
→ open a story's coverage from one or several outlets
→ follow links out to the originating publishers
→ return to the flow; it has refilled in the meantime
```

### Optional personal layer

Some products offer a companion personal surface beside the shared flow — follow topics and sources, save stories, keep a reading list. This layer sits beside the shared flow; it does not replace it, and the product remains an aggregator without it.

### Core vs Common vs Optional

**Defining core** — without these, not a news aggregator:

- sourced multi-publisher news corpus with visible provenance
- shared product-side assembly of the flow
- the standing, continuously refilled flow

**Common mature structure** — present in most modern products:

- clustering of duplicate coverage into one story with multiple sources
- an editorial layer making final calls on prominence and headlines
- ranking/scoring machinery with stability safeguards
- alternative renderings (ranked page, reverse-chronological river, topic sections)
- link-out to the originating publishers
- search and topic navigation

**Variant / optional** — depends on product philosophy, scope, and packaging:

- vertical scope (tech, politics, media, finance) vs general news
- editors-in-the-loop vs machinery-only vs hybrid
- link-out vs in-app hosting of content
- personal feeds / follows / saved stories as a companion layer
- attached context modules (market data, scores, weather)
- newsletter delivery, commercial models, portal or platform embedding

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### The main flow (front page)

The product's primary surface.

- assembled stories ranked by the machinery, each with headline, source(s), recency
- primary actions: open a story, open its coverage from a specific outlet, share

### Topic sections

Narrower renderings of the same machinery over a topic-scoped corpus.

- the same story-with-sources presentation, filtered to one topic
- primary actions: browse the section, open stories

### River / chronological view

An alternative rendering of the same shared flow in pure reverse-chronological order, offered by some products for readers who want the raw stream rather than the ranked page.

### Story / cluster view

The coverage picture for one story.

- the headline as framed by the product, the list of outlets covering it, links to each
- primary actions: open an outlet's report, see related coverage

### Personal layer (where present)

A companion surface for following topics/sources and saving stories — separate from the shared flow.

## Important Rules / Behaviors

### The flow is shared

The defining behavior: the assembled flow is the same for every reader. Personalization may exist as an optional layer, but the product's main surface is assembled once, not per reader. This is the structural contrast with personalized feeds.

### Provenance is visible on every story

Each story shows where it came from — the originating outlet, and commonly the full set of outlets covering the same event. Aggregation without visible sourcing is not recognizable as aggregation.

### The flow refills continuously

The surface updates as new coverage arrives; stories rise and fall as the machinery re-scores. Mature products add stability safeguards so the page does not thrash between near-tied stories, and some hold back single-outlet stories until corroborated.

### The product feeds, it does not (normally) author

The aggregator's job is assembly and presentation of others' journalism. Some products add first-party editorial content, but the defining job is feeding the multi-publisher corpus.

## Variants

- **general-news aggregator** — the whole news corpus across topics
- **vertical news aggregator** — the same machinery over a narrower corpus (technology, media industry, politics, celebrity); the machinery is identical, only the scope differs
- **editor-led aggregators** — editors as the top assembly layer, software beneath
- **machinery-only aggregators** — fully automated assembly with no human editors
- **platform-native news products** — the aggregator surface hosted inside a platform's news app, commonly beside a per-user personalized flow in the same product
- **portal-embedded news modules** — the aggregator surface hosted inside a larger information portal; the nesting is packaging, not identity

## Related Application Types

| Application Type | Distinction |
|---|---|
| Content Aggregator | same assembly machinery, but the corpus spans all content kinds, not just news/journalism |
| Personalized News Feed | the flow is assembled *per user* from that user's signals; here the flow is assembled once and shared |
| Feed Reader | the user's own subscription list is the sole selector, with faithful complete delivery; here the product's machinery selects across a corpus the user never enumerated |
| News Application | a single publisher's own product — its editors, editions, and reporting; here the corpus is multi-publisher and the job is assembly, not authoring |
| Information Portal | the portal's artifact is the whole entry surface (content + services + routing); the aggregator's artifact is the assembled article stream |
| General Web Search Engine | per-query transient results vs a query-free standing shared flow |
| Social Networking / social feed Types | the connection graph is the distribution substrate and the user is a member; here the user is an audience member of an assembled publisher flow |
| Financial News & Research Platform | instrument anchoring, attached market data, and investment-decision purpose; a plain vertical news aggregator stays in this Type |

The most important boundary is with the **Personalized News Feed**: the two are commonly hosted in one product (a shared editorial front page beside a per-user flow), and the seam is whether per-user selection is the core or an optional layer.

## Representative Products

- Techmeme — editor-led vertical news aggregation (technology)
- AllTop — editor + ranking-model + clustering hybrid with topic sections
- Google News — algorithmic news aggregation at general scale
- Apple News — platform-native news product hosting the aggregator surface beside a personalized flow

The core model was checked against machinery-only (editor-free automated feeds), single-editor web-era, and analog edited-digest forms to avoid over-fitting to the modern algorithmic pattern.

## Sources

Research date: **2026-09-10**

- Techmeme — About page: https://techmeme.com/about
- AllTop — homepage: https://www.alltop.com/ ; About page: https://www.alltop.com/about
- Apple News — User Guide pages (fetched 2026-09-08 in the paired sibling research; see research notes)
- Google News — product blog index: https://blog.google/products/news/ (positioning sentence only)

> Sourcing limitation: live fetch of Google News, SmartNews, and Flipboard documentation was not possible from the research environment (repeated timeouts; abandoned per the failure limit). Claims about those products are limited to what prior research passes recorded; precise operational details (ranking formulas, update frequencies, coverage limits) are intentionally not stated in this document. Detailed evidence, cross-product comparison, and the historical check are recorded in the paired Research Notes.
