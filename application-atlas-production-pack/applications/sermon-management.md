# Sermon Management

## Overview

A **Sermon Management** application is a church's system for managing its sermons as records: each sermon — a specific message prepared and/or preached in the church's life — is held as an identified record carrying sermon-specific information (speaker, date and service occasion, the scripture passage, commonly the series it belongs to) together with the message's content (a recording, notes or manuscript, and commonly attached materials). Sermon records accumulate into the church's sermon library, and the message is carried beyond the live service — published through channels such as the church website, a podcast feed, or the church app, and in preparation-shaped products further worked into derivative content such as devotionals and group guides.

The problem it solves is the gap between the moment a message is preached and the rest of the week: most people a church wants to reach were not in the room, or want to revisit what they heard. The defining core is deliberately small:

```text
Sermon record (message identity + content)
└── Sermon library (the church's archive of record)
    └── The message carried beyond the service
        (made available beyond the live moment)
```

Everything else commonly associated with the category — podcast feeds, church-app integration, video hosting, live-stream capture, series organization, research libraries, AI repurposing — is widespread in current products but is not what makes the product a sermon-management application. A church cataloging sermon tapes in a labeled cabinet and mailing duplicates to shut-ins runs the same defining structure with none of the modern machinery.

## Users & Context

Primary users, on the church side:

- **The preacher / teaching pastor** — authors the message (in prep-shaped products), and is the recorded speaker on the record.
- **Church media or communications staff (often a volunteer)** — records or collects the service recording, trims it to the message, creates the sermon record, attaches content, and publishes it to the church's channels.
- **Church office administrator** — maintains the library, keeps metadata consistent, manages what is public.

Secondary users, on the congregation side:

- **Members** — watch or listen to past messages, download them for offline listening, sometimes keep their own notes against a sermon.
- **Visitors and seekers** — discover the church's teaching through the website sermon library or a podcast app.
- **Small group leaders** — use discussion guides or devotionals derived from the sermon, where the product generates them.

The context is the weekly rhythm of church life: the message is prepared during the week, preached at the weekend service, published early in the following week, and consumed by the congregation throughout the week. The work is recurring and cumulative — every service adds to a library that is expected to keep growing for years.

## Core Model

### The Defining Core

**The sermon as the unit of record.** A sermon record is a persistent, individually identified record of one message. Its identity is sermon-specific: a title, the speaker, the date and service occasion, typically the scripture passage, and commonly the series it belongs to. Its content is whatever form the message takes — an audio or video recording of the preaching, the speaker's notes or manuscript, a PDF, or several of these attached to the same record. Without the sermon shape — without speaker, occasion, passage, and message content — the system is just a media library or a folder of files.

**The sermon library as the church's archive of record.** Sermon records accumulate into an organized, retrievable collection — browsable by date, speaker, passage, or series — that becomes the church's preaching record over time. The library is why the record exists as a record rather than an upload: a sermon added this Sunday remains findable years later, and the library as a whole tells the story of what the church has taught.

**The message carried beyond the service.** The sermon record — or its content — is made available outside the live preaching moment: people who were not in the room, or who want to revisit the message, can reach it. The standard realization is publication — the record is distributed through channels the product operates or feeds: the church website's sermon library, a podcast feed, the church app, TV apps; in earlier eras, duplicated tapes and mailed copies. A further realization, documented in preparation-shaped products, is transformation — the message's content is worked into derivative material for the congregation (devotionals, small-group discussion questions, written recaps) that is then shared through the church's ordinary channels. Remove this leg and the product is a private archive or a writing tool with no afterlife; the reason churches adopt these products is precisely that the message should keep working after Sunday.

The three legs are jointly load-bearing:

- a sermon record without a library is a one-off upload;
- a library without sermon-shaped records is a folder of recordings;
- publication without records and a library is a podcast host or a generic publishing platform;
- records and a library without any availability path is a private archive nobody can reach.

### Standard Capabilities

Mature products commonly add the following. They make the Type practical; they do not define it.

- **Podcast feed generation** — the sermon library published as a feed that listeners subscribe to in podcast apps. The dominant modern realization of publication, but one channel among several.
- **Website sermon library and player** — an embeddable or hosted page where visitors browse and play messages.
- **Church app sermon surface** — live viewing of the service, catch-up on past messages, and offline downloads inside the church's own app.
- **Multiple content forms per record** — audio, video, PDF notes, and manuscript text coexisting on one record.
- **Search and browse** — finding messages by speaker, passage, date, or topic across the library.
- **Delivery support (prep-shaped products)** — a presenter mode for preaching from the notes, and slide export into worship presentation software.
- **Free consumer access** — sermons are typically available without an account, to members and strangers alike.

### One Structure, Many Implementations

The core model is conceptual; products realize each piece differently:

```text
Concept:            Sermon record content
Implementations:    audio recording, video recording, manuscript/notes, PDF, attached materials

Concept:            Library organization
Implementations:    date/service list, speaker index, scripture index, series collections

Concept:            Carried beyond the service
Implementations:    podcast feed, website library, church app, TV apps,
                    derivative content (devotionals, group guides, recaps, social posts),
                    historical: duplicated tapes / mailed copies / printed transcripts
```

A reader who has only seen podcast-style sermon libraries should still recognize a manuscript-first sermon workspace, or a tape-ministry-era archive, as the same Type.

## How It Works

The Type runs as a recurring weekly loop around one object — the sermon record. Different products emphasize different arcs of the loop.

### Prepare the message (prep-shaped products)

```text
Create a new sermon
→ structure it from blocks (scripture, points, illustrations, application)
→ research against built-in commentaries and references
→ refine and rehearse (presenter mode)
→ export slides for the service's presentation software
```

The sermon exists as a document before it exists as a recording. The record's library role starts here: past sermons are kept, reused, and turned into templates.

### Capture or collect the content (archive-shaped products)

```text
Record the service (live stream auto-archived, or a manual recording)
→ trim the recording to the message portion
→ or collect an already-produced file (audio, video, PDF)
```

### Catalog the sermon record

```text
Create the sermon record
→ enter the identity: title, speaker, date/service, scripture passage, series
→ attach the content (recording and/or notes and/or PDF)
→ save into the library
```

This is the hub step: everything else hangs off the record.

### Publish and distribute

```text
Publish the record
→ connected surfaces update: website sermon library, podcast feed,
  church app sermon tab, TV app
→ the audience streams, downloads, or reads
```

Publication is typically a single act that propagates: one published record appears on every channel the church has connected, rather than being re-uploaded per channel.

### Repurpose (where offered)

```text
Select a preached sermon
→ generate derivative content: small-group questions, daily devotionals,
  a written recap, social posts
→ hand the outputs to group leaders, the newsletter, or the church's social channels
```

### Core vs Common vs Optional

**Defining core** — without these, not sermon management:

- sermon as the unit of record (sermon-specific identity + message content)
- the accumulating sermon library
- the message carried beyond the service (made available beyond the live moment)

**Common mature structure** — present in most modern products:

- podcast feed generation
- website sermon library/player
- church app sermon surface with offline downloads
- multiple content forms per record
- search and browse by sermon metadata
- free accountless consumer access

**Variant / optional** — depends on product shape and era:

- live-stream capture feeding the archive, with trimming of captured full-service recordings down to the message
- prep-side machinery (research suite, templates, illustration libraries, presenter mode, slide export)
- derivative-content generation, AI assistance
- member notes per sermon, teaching aids attached to messages
- platform-level public directories of churches
- series organization depth, analytics

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Sermon library

The church-side home surface.

- lists the accumulated sermon records with their identity (title, speaker, date, passage, series)
- primary actions: add a sermon, edit a record, publish/unpublish, organize by series or speaker, search

### Sermon record editor

Where one sermon is assembled.

- identity fields (title, speaker, date/service, scripture passage, series)
- content attachment (audio/video files, PDF, manuscript text)
- in prep-shaped products, a block-based writing surface with research panels alongside

### Media player / sermon page

The consumption surface for one message.

- player for the recording, the passage reference, the speaker, download controls
- primary actions: play, download for offline, share, sometimes save personal notes

### Distribution settings

Where the channels are connected.

- podcast feed details, website embed configuration, app tab wiring, connected platforms
- primary actions: connect a channel, choose what publishes where, review feed status

### Prep workspace (prep-shaped products)

The writing environment.

- block editor, research/reference panel, template and illustration libraries, presenter mode

### Consumer surfaces

What the audience actually touches: the website sermon page, the podcast app, the church app's sermon tab, the TV app. These are operated by the product but experienced outside it.

## Important Rules / Behaviors

### One record, many surfaces

The sermon record is the hub: publishing a record updates every connected channel. Editing the record (a corrected title, a replaced file) propagates the same way. This is the behavior that distinguishes a sermon system from re-uploading files to each platform by hand.

### Content form is per-record, not per-product

A single record may carry an audio file, a video, a PDF, and a manuscript together. Products do not force one medium; the record is the unit that carries whatever the message produced.

### Captured services are reduced to the message

Sermon libraries are organized at message grain — by sermon, not by raw service recording. Where the content arrives as a captured full-service recording, it is typically trimmed to the message portion before it becomes the sermon record: the archive holds messages, not raw service footage.

### Availability follows the church's standing service

Published sermons are hosted by the product's service; if the church stops using the product, access to the published library follows the vendor's account-lifecycle policy. Churches treat the library as a long-term asset, and continuity of availability is part of the purchase decision — ownership and control of the content is a recurring posture theme across products.

### The audience is typically accountless

Sermons are public teaching: consumption typically requires no account — on the website, in podcast apps, or in the church app. Access control, where it exists at all, is the exception rather than the structure.

### The prep arc and the archive arc meet at the record

A prepared manuscript becomes the preached message becomes the archived record becomes the source for derivative content. Products may enter the loop at any point, but the record is the same object throughout — which is why prep tools and archive tools are one Type with different centers of gravity rather than two unrelated kinds of software.

## Variants

- **Standalone sermon broadcast/archive platform** — the whole product is sermon hosting and distribution: live capture, archive, podcast feeds, apps, TV channels, often with a public directory of churches (sermon-first media platforms).
- **Sermon preparation application** — the whole product is writing and delivering the message: block editors, research libraries, presenter mode, slide export, derivative-content generation; the library is the preacher's.
- **ChMS module** — the sermon archive as a named feature inside a church management system, storing messages alongside the church's people records and embedding them on the website; video hosting may be delegated to third-party platforms.
- **Church app / website surfaces** — sermon streaming, archives, and players delivered as capabilities of church app and church website products rather than as a standalone system.
- **CMS plugin realization** — the sermon archive implemented as a content type and templates inside a general website CMS (self-hosted church websites).
- **Streaming-platform adjacency** — live streaming products whose recorded broadcasts accumulate into an on-demand library; sermon-shaped only insofar as the church treats the archive as its sermon library.

A variant remains a variant while the defining core holds; when the center shifts to the live event (streaming), the show-and-subscriber relationship (podcasting), or the people records (ChMS), the product has drifted into a neighboring Type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Podcast Platform | centers the show/episode catalog and the listener's subscription; here the podcast feed is one output channel of the church's sermon record and library |
| Media Asset Management | holds generic media assets for media organizations; here records are sermon-shaped (speaker, passage, series, service occasion) for a church |
| Church Website Builder | the website's sermon library is a display object consuming the record; Sermon Management is the record workflow producing it |
| Worship Planning | organizes the service occasion (order of service, songs, people); here the object is the message as a record — they meet at the service plan's sermon slot |
| Worship Presentation Software | displays content live in the service (lyrics, scripture, slides); here the object is the record that outlives the service — they meet at slide export |
| Scripture Study Application | personal reference-keyed study of the canonical corpus; here the object is the church's sermon records — prep tools borrow study machinery as support |
| Church Management System / ChMS | centers the church's people records (members, households, giving, groups); the sermon archive ships as a module beside that core |
| Video Streaming Platform | centers the live broadcast event; here the center is the accumulating sermon library that captured services feed into |
| Content Management System | generic content management; the sermon archive can be realized as a CMS content type, but the sermon shape and distribution machinery are the Type |

The closest seams are Podcast Platform (feed as output vs show as center) and Church Website Builder (record workflow vs display object). The prep/archive duality is internal to the Type, not a boundary: both arcs hold the same sermon record.

## Representative Products

- **sermon.net** — standalone sermon broadcast/archive platform: live stream, archive, podcast feeds, network and custom-branded apps, TV channel, public directory
- **Sermonary (Ministry Pass)** — sermon preparation application: block editor, research suite, presenter mode, slide export, derivative-content generation
- **One Church Software** — church management system carrying a named Sermon Archive feature (store, organize, embed, member notes, YouTube/Vimeo hosting integration)
- **Tithe.ly (Church App / Sites)** — sermon streaming, archives, offline downloads, and site media players as surfaces of church app and website products
- **BoxCast** — live-streaming platform included as a boundary anchor (streaming-first, with recorded broadcasts as the byproduct)

The largest sermon-native platforms (SermonAudio, Subsplash, Faithlife/Logos Sermons) could not be reached during research; see Sources.

## Sources

Research date: **2026-09-09**

- sermon.net — https://www.sermon.net/ , https://www.sermon.net/outreach-tools-apps
- Sermonary — https://sermonary.com/ , https://sermonary.com/editor/ , https://sermonary.com/multiply/
- One Church Software — https://onechurchsoftware.com/features/ , https://onechurchsoftware.com/one-church-software-vs-subsplash/
- Tithe.ly — https://get.tithe.ly/product/church-app
- BoxCast — https://www.boxcast.com/
- Sharefaith — https://www.sharefaith.com/
- Elvanto — https://www.elvanto.com/ , https://help.elvanto.com/ (sermon search)
- WordPress.org — https://wordpress.org/plugins/sermon-manager-for-wordpress/ (plugin closed; existence/market-structure evidence only)

> Sourcing limitation: SermonAudio (403), Subsplash (timeouts), and Faithlife/Logos Sermons + Proclaim (timeouts/transport errors) were unreachable from the research environment on 2026-09-09; the media-platform pole is documented directly only through sermon.net, and second-hand through a competitor comparison page. All reachable sources were official product/marketing pages; no help-center article bodies were retrieved. Precise operational details (numeric limits, retention policies, pricing, analytics, series machinery) are therefore intentionally not asserted in this document; they remain recorded as uncertainties in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison, and the historical market-sample check are recorded in the paired Research Notes.
