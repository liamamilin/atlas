# News Application

## Overview

A **News Application** is a single news publisher's own reader-facing product: the application through which a newspaper, broadcaster, or news agency presents its own journalism directly to its audience.

The defining structure is small:

```text
First-party newsroom corpus
(the stories shown are the publisher's own journalism)
└── The publisher's standing editorial surface
    (front page, sections, editions — continuously updated by the
     publisher's own editorial judgment)
    └── The publisher's direct audience channel
        (the reader's relationship is with the publisher itself,
         under its brand and editorial voice)
```

Everything commonly associated with modern news products — native apps, paywalls and metering, personalization, push notifications, video and live coverage, games, newsletters, regional editions — is widespread in current products but is not part of the defining core. A free, ungated publisher website, a broadcaster's teletext-era text news service, and the printed daily newspaper itself all fit this definition without any of those specifics.

When the product instead assembles stories from many publishers, it is drifting toward a different Application Type (News Aggregator, Personalized News Feed). When the system described is the newsroom's production machinery rather than the audience-facing product, it is the publishing-side Types (News Publishing Platform, Newsroom Management System).

## Users & Context

The primary user is an **individual consuming news as a member of the publisher's audience**. They arrive to find out what is happening, as reported and framed by one news organization they have chosen to read, watch, or listen to.

Typical reasons to open the application:

- catch up on the day's reporting as the publisher has ordered and framed it
- follow a developing story as the publisher updates it through the day
- browse a section of interest (world, politics, business, sport, culture)
- watch live coverage or a news video, or listen to a news briefing or podcast

A secondary constituency is the **publisher's own editorial operation** — but only as the producer behind the product: reporters, editors, and homepage teams work in production-side systems and never in this one. Their output reaches the audience through this product.

The typical context is short, frequent sessions on a phone, with the web site as the other primary surface; print (for newspaper-pole publishers) and broadcast channels remain sibling artifacts of the same news operation rather than parts of this product.

## Core Model

### The Defining Core

Three structures, held together. If any one is removed, the product is no longer recognizable as a single publisher's news application:

- **First-party newsroom corpus** — the stories the product presents are the publisher's own journalism, produced by its own reporters and editors. The product is the publisher of what it shows; it authors the news, it does not feed on others' reporting. Without this, the product becomes an assembly of other publishers' work — an aggregator or a personalized feed.
- **The publisher's standing editorial surface** — a continuously updated consumption surface organized by the publisher's own editorial judgment: the front page, the section structure, the placement of breaking news, the edition rhythm. The ordering is itself an editorial product. Without this, the product is a raw stream or archive of the publisher's output — not a news application.
- **The publisher's direct audience channel** — the product is operated by the publisher as its own audience surface. The reader's relationship is with the publisher itself, under the publisher's brand and editorial voice — not mediated through a third party's assembly or licensed hosting. Without this, the surface is syndication or packaging.

### The Objects

- **Story** — the unit of news: a report produced by the publisher's newsroom, carrying headline, byline, media, and section placement. Stories arrive fully authored; the reader never sees them in draft.
- **Section** — the publisher's editorial organization of its own coverage: named subject spaces (world, politics, business, sport, culture, science, weather) that structure navigation and the public address space. Sections are the connective tissue between the front page and the corpus.
- **The front page** — the publisher's ordered presentation of what matters now: the editorially ranked assembly that changes through the day as news develops.
- **Editions** — regional or language variants of the same product (domestic vs international, per-market editions), carrying the publisher's corpus scoped and ordered for each audience.
- **The reader** — an audience member of this publisher: anonymous, registered, or paying, depending on the product's commercial posture. The reader consumes and reacts; they do not assemble the surface.

### Standard Capabilities

These are widespread in mature products. They make the product work well, but they are not what makes it a news application.

- **Section and topic navigation** — a taxonomy organizing the publisher's coverage; in one documented implementation a deep, stable section tree (domestic beats, world regions, politics, business, markets, health, entertainment, style, travel, sport, science, climate, weather) anchors the whole surface.
- **Breaking-news handling and continuous updates** — the surface changes through the day; developing stories are updated in place, and urgent coverage is promoted.
- **Video and live coverage** — news clips, live streams of the publisher's broadcast channels, and standing video products.
- **Audio** — podcasts and short daily news briefs as a listening channel.
- **Newsletters** — email editions of the publisher's journalism as a delivery channel beside the app and site.
- **A personalization layer** — following topics or sections inside the publisher's product, so the reader's preferred subjects surface more prominently. This layer sits beside the editorial surface; it does not replace it.
- **Accounts and notifications** — registration, saved preferences, push alerts for breaking news.
- **Search and archives** — finding the publisher's past reporting.
- **Engagement modules** — games, quizzes, and similar companions beside the news.
- **Regional and international editions** — the same product realized per market.

### One Structure, Many Implementations

The core model is written in conceptual terms. Implementations vary:

```text
Concept:   First-party corpus
Realized as:   a newspaper's reporting, a broadcaster's news operation,
               an agency's own consumer-facing reporting

Concept:   The standing editorial surface
Realized as:   a web front page, an app home screen, a print front page,
               teletext-era text pages — any surface the publisher
               orders itself and keeps current

Concept:   The direct audience channel
Realized as:   free anonymous access, registration, metered access,
               full subscription, public funding, reader contributions
```

A reader who only encounters one implementation (e.g. a subscription-gated app) should still be able to recognize a free broadcaster site or the printed newspaper itself from the core model.

## How It Works

### The editorial loop behind the surface

The product's defining loop is not operated by the reader. The publisher's newsroom produces stories continuously; its editors decide what leads, how sections are ordered, and what the front page carries; and the surface the reader opens is the current state of that editorial judgment:

```text
Newsroom produces and updates stories (in production-side systems)
→ the publisher's editorial judgment orders the surface
  (front page, sections, breaking placement)
→ the audience-facing product renders that order
→ the surface is re-ordered as the day develops
```

The reader experiences this as a surface that is always current but never theirs to assemble — the structural contrast with the aggregation and feed Types, where the product's machinery (or the user's own list) does the selecting across a multi-publisher corpus.

### Consume

```text
Open the product (app or site)
→ scan the front page as the publisher has ordered it
→ follow a section, a developing story, or a search
→ read / watch / listen
→ optionally follow topics, save, share, enable alerts
→ return later; the surface has been re-ordered in the meantime
```

### The personalization layer (where present)

Some products let the reader follow topics or sections so that preferred subjects appear more prominently. This is a tuning layer beside the editorial surface: the front page remains the publisher's shared editorial product, and the product remains a news application without the layer.

### Core vs Common vs Optional

**Defining core** — without these, not a news application:

- first-party newsroom corpus
- the publisher's standing editorial surface
- the publisher's direct audience channel

**Common mature structure** — present in most modern products:

- section/topic navigation; breaking-news and continuous updates
- video, live coverage, audio briefs, podcasts
- newsletters; accounts and push notifications; search and archives
- a personalization layer (follow topics); engagement modules
- regional/international editions

**Variant / optional** — depends on publisher, market, and era:

- commercial posture: subscription/metering, free + advertising, public funding, reader contributions
- modality emphasis: text-led, video-led, audio-brief-led
- platform packaging: web, native apps, print edition as sibling artifact
- bundled non-news products (games, cooking, shopping, weather)

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### The front page (home)

The product's primary surface.

- Purpose: present the publisher's current editorial order — what leads, what is developing.
- Typical information: ranked stories with headlines, imagery, section labels, recency; breaking-news placement; pointers into video and live coverage.
- Primary actions: open a story, enter a section, start watching/listening, share.

### Section pages

- Purpose: the publisher's ordered coverage of one subject space.
- Typical information: the section's current stories in editorial order, with sub-beats where the publisher maintains them.
- Primary actions: browse, open stories, follow the section (where personalization exists).

### Story page

- Purpose: consume one report fully.
- Typical information: the story as published — headline, byline, body, media, updates and corrections where the publisher appends them, related coverage from the same publisher.
- Primary actions: read/watch/listen, share, save, follow related topics.

### Live / video surface

- Purpose: follow unfolding coverage and the publisher's broadcast output.
- Typical information: the live stream or live report, clips, the publisher's video products.
- Primary actions: watch, follow the developing story.

### Audio surface

- Purpose: listen to the publisher's news output.
- Typical information: daily briefs, podcasts, the publisher's audio catalog.
- Primary actions: play, follow a show, download.

### Settings / account

- Purpose: manage the reader's relationship with the publisher.
- Typical information: profile, notification preferences, followed topics, subscription state (where the product is commercially gated).
- Primary actions: sign in, manage alerts and follows, manage subscription.

## Important Rules / Behaviors

### The surface is the publisher's editorial product

The front page and sections are ordered by the publisher's editorial judgment, not by the reader's signals and not by cross-publisher machinery. A personalization layer, where present, tunes prominence beside this order; it does not become the organizing principle.

### The corpus is the publisher's own

Every story traces to the publisher's own newsroom. Where a publisher's product also surfaces partners' or licensed content, that sits beside the first-party corpus as packaging — the product's identity rests on its own journalism.

### Publication is continuous, and corrections are ordinary

News develops through the day: stories are updated in place, urgent coverage is promoted, and corrections are a normal, visible operation on published reporting. The reader sees the current state of a living report, not a fixed artifact.

### The commercial posture varies but does not define

The same core supports a fully gated subscription product, a free ad-funded product, a publicly funded product, and a reader-contribution-funded product. Access state (anonymous / registered / paying) changes what the reader may consume, not what the product is.

### Provenance is the product's identity

The publisher's brand and editorial voice organize everything the reader sees. This is the inverse of the aggregation Types, where provenance must be displayed because the corpus is others' work; here the provenance is singular and structural.

## Variants

- **Subscription-first national newspaper** — the metering/paywall pole; the news product is the front door of a wider subscription brand (market anchor: The New York Times).
- **Public-broadcaster news** — free at the point of use, publicly funded, with domestic and international editions (market anchor: BBC News).
- **Reader-funded open journalism** — free at the point of use, supported by reader contributions (market anchor: The Guardian).
- **Ad-funded commercial broadcaster** — app-first, video-led, advertising-supported with an optional subscription tier (documented this pass: CNN).
- **Agency direct-to-consumer** — a wire agency operating its own consumer surface beside its syndication business (market anchor: AP News).
- **Regional / local newspaper products** — the same core at local scale, often with strong local-coverage identity.
- **Print-era and teletext-era forms** — the printed daily newspaper and broadcaster text-news services satisfy the same core; the digital product is this Type's current realization.

A variant remains a variant unless it changes users, core objects, or rules so much that the core model no longer applies — as when the corpus becomes multi-publisher (aggregation/feed Types) or the system described becomes the newsroom's production machinery (publishing-side Types).

## Related Application Types

| Application Type | Distinction |
|---|---|
| News Aggregator | assembles a shared flow from many identifiable publishers — the product feeds the news; here the product is the publisher of everything it shows |
| Personalized News Feed | assembles a personal flow per user from signals, across a multi-publisher corpus; here the corpus is the publisher's own output and per-user selection is at most an optional layer |
| News Publishing Platform | the newsroom-side production system of record (story records, gated publication, curated assemblies, delivery); this Type is the audience-facing product it serves — different users and objects |
| Newsroom Management System | plans and assigns the editorial work (pitches, tasks, rundowns); this Type consumes the output |
| Financial News & Research Platform | finance-vertical news products anchored to instruments, with attached market data and investment-decision purpose; a general news product carrying business/markets sections stays here |
| Media Monitoring Platform | an organization's standing watch over its own media presence; the consumer news product is explicitly outside that Type |
| Information Portal | a whole entry surface of content, services, and routing; a portal may host a news surface as one module — packaging, not identity |
| Blogging Platform | an author-owned dated post stream without an editorial gate, front-page assemblies, or correction semantics |
| Video Streaming Platform | the catalog of shows/films is the artifact; video is one channel of the news surface here |
| Podcast Platform | audio shows as the artifact; audio is one channel of the news surface here |
| Social Network / social feed Types | the connection graph is the distribution substrate and the user is a member; here the user is an audience member of one publisher |

The most important boundary inside the news section of the directory is with the **News Aggregator**: one product can host both surfaces (a publisher's app may carry partner coverage beside its own reporting), and the structural test is whether the product publishes what it shows (this Type) or feeds and assembles others' journalism (aggregator).

## Representative Products

- **CNN** — ad-funded commercial broadcaster; directly documented for this research (app product page): section taxonomy, Watch/Listen/Games modules, newsletters, topic following, subscription offering.
- **The New York Times** — market anchor for the subscription-first national-newspaper pole. Not directly verifiable during this research; listed for orientation only.
- **BBC News** — market anchor for the public-broadcaster, free-at-the-point-of-use pole. Not directly verifiable during this research; listed for orientation only.
- **The Guardian** — market anchor for the reader-funded open-journalism pole. Not directly verifiable during this research; listed for orientation only.
- **AP News** — market anchor for the agency-as-publisher boundary probe. Not directly verifiable during this research; listed for orientation only.

The core model was checked against the printed newspaper, teletext-era text news, and early free web editions to avoid over-fitting to the modern app-and-paywall pattern.

## Sources

Research date: **2026-09-10**

Fetched directly:

- CNN — App product page: https://www.cnn.com/app

Family and boundary evidence recorded at first-hand in the processed sibling passes (News Aggregator 2026-09-10; Personalized News Feed 2026-09-08; News Publishing Platform 2026-09-08; Newsroom Management System 2026-09-08; Media Monitoring Platform 2026-09-08; Financial News & Research Platform §08), including vendor positioning that defines each pole against the others.

> Sourcing limitation: only CNN's product page could be fetched this pass. The New York Times help center and site, both BBC surfaces, both Guardian surfaces, Le Monde, and AP News were unreachable from the research environment (repeated timeouts; AP returned an access denial; each source abandoned after the standard retry limit). No feature-level claims are made about those products; they are listed as market anchors for orientation. Precise operational details (metering thresholds, notification defaults, offline behavior, app-internal layouts) are intentionally not stated anywhere in this document. The historical argument (print newspaper, teletext) is structural, as no archival sources were reachable.

Detailed evidence, product-by-product observations, the cross-product comparison, the abstraction hierarchy, and the full boundary analysis — including the dispositions of the flags forwarded from the sibling passes — are recorded in the paired Research Notes.
