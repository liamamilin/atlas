# E-book Reader

## Overview

An **E-book Reader** is an application that turns a digital book into a reading experience: it opens one book at a time, presents the book's content for sustained reading on screen, keeps track of where the reader is in each book, and moves the reader through the book — page by page or scroll by scroll, with navigation back into any part of it.

The defining core is deliberately small:

```text
The opened book
└── Reading-oriented presentation (paginated or flowing, adapted to the screen)
    └── Persistent per-book reading position
        └── In-book movement (page turns / scrolling, resumed where you left off)
```

Everything else commonly associated with modern reading apps — typography panels, night themes, highlights and notes, dictionaries, read-aloud, bookshelves, store purchase, cloud sync, DRM handling — is widespread in current products but is machinery around the core, not the core. Older and simpler reading applications (desktop and PDA-era readers, plain-text book readers on early phones) satisfy the same core with none of those features.

When the center of gravity shifts from the reading session to the collection of books — acquiring, organizing, cataloging and delivering them — the product is drifting toward a different Application Type (E-book Library Application).

## Users & Context

The primary user is a person reading a long-form book over multiple sittings: on a commute, in the evening, across weeks. The defining situation of the Type is not "looking at a document once" but *living inside a book* — returning day after day to the same text and expecting to land exactly where the reading stopped.

Typical reasons to open the application:

- continue the book currently being read (the most common entry)
- open another book from a recent-books or bookshelf surface
- look something up inside the book (a passage, a term, a chapter)
- capture a highlight or note while reading
- adjust the page to the eyes and the environment (font size, night mode, brightness)

The work environment spans screens: dedicated e-ink reading devices, phones and tablets, and desktop computers. On device-bound products the reader also controls the reading hardware (frontlight, refresh behavior); on platform-native products it inherits the operating system's comforts (system voices, cloud accounts). Reading is overwhelmingly offline-capable — the book is present on the device.

## Core Model

### The Defining Core

```text
The opened book
└── Reading-oriented presentation
    └── Persistent per-book reading position
        └── In-book movement
```

Four properties. If any one is removed, the product is no longer recognizable as an e-book reader:

- **The opened book** — one digital book document is loaded into a reading surface at a time. The reading session is the unit of work; the reader's world is the book in hand, not the collection of books. Without this, the product is a library or catalog.
- **Reading-oriented presentation** — the book's content is laid out for sustained reading: paginated text, or continuously flowing text, adapted to the screen. It is never raw file contents, and it is not an editing surface. Without this, the product is a file viewer or text editor.
- **Persistent per-book reading position** — where the reader is in each book is first-class state that survives closing the application. Reopening resumes the book. Without this, long-form reading across sessions collapses, and the product degrades into a static renderer.
- **In-book movement** — the primary interaction is advancing through the book from that position: page turns or scrolling, plus the ability to move back and forth. Without movement, there is no reading flow.

### Capabilities Shared by Mature Products

These make the core practical. They are not what makes the product a reader, but mature products commonly carry most of them.

- **In-book navigation** — a table of contents (or page thumbnails), a progress indicator or slider, bookmarks for saved spots, jump-to-page/percentage, and a "back to where I jumped from" trail after multipage jumps or link follows.
- **Reading-comfort controls** — typography (font, size, weight, line spacing, margins, justification, sometimes columns and hyphenation), page themes (day/night/sepia-class), brightness or frontlight control, and page-turn versus continuous-scroll behavior.
- **Text interaction layer** — selecting text to highlight, annotate, copy, search the book for it, look it up in a dictionary or encyclopedia, translate it, or share it.
- **Search within the book** — finding words, phrases, or sometimes page numbers across the whole text.
- **Entry/bookshelf surface** — a "continue reading" shelf, recent-books list, history, or a small grid of books: the common entry layer into reading. This is an entry surface to books, not collection management.
- **Per-book settings memory** — appearance choices ride with the book, so a comfortable setup survives between sittings (some products also offer global defaults).
- **Read-aloud / synthetic speech** — having the page read aloud, in consumer-facing readers.

### One Structure, Many Implementations

The core model is written in conceptual terms; specific products realize each concept differently.

```text
Concept:            the book document
Implementations:    reflowable formats (EPUB-class), fixed-layout files (PDF, comics),
                    DRM-wrapped store titles, plain text files

Concept:            the page
Implementations:    screen-paginated page, continuous scroll position,
                    print-equivalent page mapping (publisher-embedded print page numbers)

Concept:            reading position
Implementations:    local per-book state, account/cloud-synced progress, device-ecosystem sync

Concept:            entry surface
Implementations:    continue-reading shelf, recents/history list, file browser, catalog grid
```

A reader who has only encountered one implementation (say, a store-based phone app) should still be able to recognize a file-based desktop reader or a device-embedded reader from the core model.

## How It Works

### The reading loop

The everyday lifecycle of the Type is a loop, not a pipeline:

```text
Open a book
→ read: advance page by page (or scroll); position advances and is saved continuously
→ adjust the page when needed (typography, theme, brightness)
→ navigate when needed (table of contents, progress slider, bookmarks, search)
→ interact when needed (select text → highlight / note / lookup / translate / share)
→ close
→ return later: the book resumes exactly where the reading stopped
```

There is no checkout, no assignment, no pipeline stage. The reader's "workflow" is the rhythm of a reading life: open, read, return.

### Opening a book

Books arrive at the reading surface in different ways depending on the product family: from a continue-reading shelf or library grid, from a file browser over the device's files, as a download from an embedded store, or synced from an account. For store-licensed titles, opening may pass through a license step (account authorization); for the user's own files, opening is immediate. These acquisition and licensing layers are variant machinery — the reading surface itself starts when a book is open.

### Reading and adjusting

Reading advances the position continuously; the position is saved as it moves, not at exit. When the default presentation doesn't suit — small text on a big screen, daylight versus darkness, a dense justification — the reader adjusts the page. For reflowable books this re-lays-out and re-paginates the text; for fixed-layout content it scales or crops instead. The adjusted presentation is remembered (per book, or as the reader's default).

### Navigating

Movement is continuous (page turns, scrolling) and structural (table of contents, progress jumps, bookmarks). A distinctive mature behavior is the jump trail: after leaping to a search result or a chapter, the reader can return to where the reading was, in one step.

### Interacting with the text

Selecting a passage opens the interaction layer: highlight or annotate it, look it up, translate it, search for other occurrences, copy or share it. Annotations attach to locations *in the text*, not to visual page numbers — see the reflow rule below. In mature products annotations accumulate into reviewable lists, and some products export them or sync them to external note systems.

### Core vs standard vs optional

**Defining core** — without these, not an e-book reader:

- the opened book as the unit of work
- reading-oriented presentation (paginated or flowing)
- persistent per-book reading position
- in-book movement

**Standard capabilities** — present in most modern products:

- in-book navigation (contents, progress, bookmarks, back trail)
- reading-comfort controls (typography, themes, brightness)
- text interaction (highlight, note, lookup, translate, search-in-book)
- search within the book
- entry/bookshelf surface (continue reading, recents)
- per-book settings memory
- read-aloud / synthetic speech

**Common variants / optional** — depends on product family and market:

- sync of position and annotations across devices
- embedded store acquisition and DRM/license handling
- fixed-layout content support (PDF, comics and manga with panel-aware modes)
- audiobook playback bundled
- reading statistics and book-status labels
- annotation export/sync to external systems
- print-equivalent page mapping
- deep device integration (e-ink frontlight/refresh control) and power-user extensibility (custom fonts and styles, gestures, plugins, OCR for scanned books)

## Interfaces

The following surfaces are described conceptually. Exact layouts and names vary by product.

### The reading page

The main surface, and the only defining one.

- the book's content laid out for reading; one page or a two-page spread on large screens, continuous flow on others
- primary actions: turn pages (tap zones, edges, keys, swipes, hardware buttons), scroll, open the reading menu

### Reading menu / controls overlay

A transient surface over the page.

- typography and appearance controls (font, size, weight, spacing, themes, light/dark), brightness/frontlight
- navigation entries: table of contents, progress bar, bookmarks, search
- primary actions: adjust presentation, jump within the book

### Contents / progress / bookmarks panel

The structural map of the book.

- chapter list (or thumbnails), position slider with percentage or page entry, list of bookmarks and annotations
- primary actions: jump to a chapter, page, or saved spot; return from a jump

### Text-selection popup

The interaction layer for a selected passage.

- primary actions: highlight, note, copy, define/lookup (dictionary, encyclopedia, glossary), translate, search-in-book, share

### Entry/bookshelf surface

The doorway into reading — common but not defining.

- continue-reading items with progress indicators, recent/history list, favorites, or a grid of covers
- primary actions: open (and in collection-oriented products, organize) books

### Settings

Reader-level preferences: default appearance, page-turn behavior, reading-aid toggles, and — on device-bound products — hardware behaviors (light, refresh, screensaver).

## Important Rules / Behaviors

### Position persistence is the defining behavior

The reader's central state is the per-book position. It advances while reading, survives closing the application, and is the anchor that "continue reading" surfaces restore. Products that sync extend this state across devices; products that don't keep it local. Either way, the position belongs to the book, not to the device session.

### The reflow rule

This is the load-bearing structural rule of the Type. For **reflowable** books, the reader's typographic choices re-lay-out and re-paginate the text: enlarging the font increases the page count, and a highlight made "on page 38" may land on a different screen page after an adjustment. Visual page numbers in a reflowable book are therefore unstable — which is why position state must be text-anchored, and why products offer **print-equivalent page numbers** (publisher-embedded print pagination) when citations must match the paper edition. For **fixed-layout** content (PDF, comics, fixed-layout epubs), the text cannot re-flow: comfort controls degrade to zoom, crop, and theme, and page numbers are stable by construction. Mature readers handle both poles, but the two poles behave differently under every control.

### Annotations attach to text, not to visual pages

Because of the reflow rule, highlights and notes bind to locations in the book's text so they survive re-layout and device changes. Some products can additionally write annotations into the document itself (a fixed-layout specialty) or export them in standard formats.

### License can gate the book

For store-licensed content, the license — not the file — determines readability: opening may require account authorization, and borrowed titles can expire and remove access. The reader surface itself is indifferent to where the file came from; the license layer sits in front of it in store-based families.

### Reading aids overlay the page

Menus, dictionaries, translation pop-ups, and statistics are overlays and side panels. The reading page remains the durable surface; aids appear over it and disappear, and the reading position is never disturbed by using them.

### Settings follow the book

Appearance choices are remembered per book (with global defaults in many products), so a re-opened book returns in the shape the reader left it — an application of the same persistence logic that governs position.

## Variants

Common forms of the Type:

- **Platform-native consumer readers** — integrated into a device operating system, bundling store, cloud sync, and system services (voices, accessibility) around the reading core.
- **Store-first cloud readers** — reading surface embedded in a retail ecosystem: a cloud bookshelf, in-app purchase, account-synced progress and annotations.
- **Device-companion and device-embedded readers** — the reader inside (or beside) a dedicated e-ink device ecosystem; adds hardware behaviors such as frontlight and warmth control, refresh tuning, and cover screensavers.
- **Open file-based readers** — the user's own files, opened from a file browser or history list; no store, no accounts; common on desktop and in open-source projects.
- **Accessibility-first readers** — screen-reader support, keyboard-driven navigation, conformance programs, and display adjustment positioned as the primary value (education and assistive segments).
- **Power-user readers** — deep format and appearance control, configurable gestures and tap zones, custom styles, alternative contents, plugin ecosystems, reading statistics.
- **Content-breadth variants** — the same reading core extended to comics and manga (panel-aware zoom, strip-style scrolling), plain text and markdown, papers, or bundled audiobook playback.

A variant remains a **variant** as long as the reading loop above still describes its center. When the product's center shifts to managing many books (acquisition, organization, metadata, delivery), it is the sibling library Type with a reader embedded.

## Related Application Types

| Application Type | Distinction |
|---|---|
| E-book Library Application | center of gravity is the collection: acquiring, organizing, locating, and delivering books; the reader is embedded. Remove the collection from a reader and a reader remains; remove the reading surface from a library (keeping catalog + handoff) and it is still a library |
| PDF / Document Reader | renders fixed-layout pages of arbitrary documents faithfully; the e-book reader treats the file as a book — reading-position life, comfort re-layout of reflowable text, print-page mapping. Readers commonly open PDFs as content breadth, but fixed-layout rendering of any document is the other Type's center |
| Read-it-later Application | captures web articles and presents them in a reading view; the unit is the clipped article (no book structure), and acquisition is clipping rather than book files |
| Reading Library Application | records what one reads and wants to read (reading record/wishlist); may hold no book files and no reading surface at all |
| Academic Paper Reader | papers, not books, are the unit; annotation and organization are paper- and citation-centric |
| Digital Library Platform | institutional lending and circulation of licensed collections; the e-book reader is the consumer-facing consumption surface that such content eventually reaches |
| Text editor / file viewer | holds an editing surface and file semantics; the reader holds a reading surface and book-reading semantics (position life, comfort presentation) |

The boundary with the E-book Library Application is the closest one, because nearly every consumer reading product bundles both. The structural test is the center of gravity: the reading session for one opened book versus the managed collection of many books.

## Representative Products

- Apple Books
- KOReader
- Thorium Reader

These were chosen to span the Type's market poles: platform-native consumer, open-source device-embedded power tool, and open-source accessibility-first desktop reader. The Core Model was checked against the file-based and device-embedded poles to avoid over-fitting to the store-and-cloud pattern of mainstream phone apps.

## Sources

Research date: **2026-09-07**

- Apple Books User Guide for Mac — Read books — https://support.apple.com/guide/books/read-books-ibks5f526382/mac
- Apple Books User Guide for Mac — Change a book's appearance — https://support.apple.com/guide/books/change-a-books-appearance-ibks8923126d/mac
- Apple Books User Guide for Mac — overview/TOC — https://support.apple.com/guide/books/welcome/mac
- KOReader — product page — https://koreader.rocks/
- KOReader User Guide — https://koreader.rocks/user_guide
- Thorium Reader — product page (EDRLab) — https://thorium.edrlab.org/en/
- Corroborating context from the paired sibling research: calibre user manual, Apple Books import page, Kavita wiki (reader surfaces inside library products) — see research/e-book-library-application.md

> Sourcing limitation: Google Play Books and Kobo help centers (the store-first cloud and retail device-companion poles) could not be reached on 2026-09-07, and Thorium's documentation sites were unreachable, leaving Thorium at product-page level. The store-first cloud pole is therefore described generically from the in-sample store-based product rather than from a dedicated sample, and no operational details (limits, defaults, exact behaviors) are asserted for the unreachable products.
