# E-book Library Application

## Overview

An **E-book Library Application** manages a collection of e-books as a *library*: it keeps a persistent catalog of book entries, each entry holding the book's file(s), its metadata, and its cover; it organizes that catalog by book attributes (collections, tags, series, search); and it provides read access to every entry — through a reader built into the product, by handing the book off to another reading surface, or by delivering it to a device or reading client.

The defining structure is small:

```text
Acquisition (import / scan / purchase)
→ Library entry (book record: file(s) + metadata + cover)
    → organized by book attributes (collections / tags / series / search)
    → read access (built-in reader · external handoff · device or client delivery)
```

Everything else commonly associated with the category — format conversion, device syncing, reading-progress tracking, want-to-read lists, cloud sync, stores, multi-user sharing, DRM handling — is widespread in current products but is not part of what makes the application a library. Removing the collection yields a plain book viewer; removing the book-level organization yields a file manager; removing read access yields a mere catalog. The type lives between those three.

## Users & Context

The primary user is an individual reader who owns or assembles a collection of e-books — files sideloaded from various sources, purchases from one or more stores, downloaded classics, scanned personal archives — and needs one place where the whole collection is findable, described, and readable.

Typical situations:

- a reader with hundreds of files from different sources who wants a single organized shelf rather than a folder of files
- a purchaser inside a store ecosystem whose books, PDFs, and samples accumulate in one personal library
- a household or small group that keeps one shared collection on a home server, with each member reading their own way
- an owner of a dedicated e-reading device who wants to move books from the computer to the device

The work environment is personal. Unlike most business Application Types, there is no operator team, no transaction, no organizational workflow — the "work" is curation of one's own reading material. Server-based variants add a second role: the library administrator who configures storage, scanning, and user access.

## Core Model

### The Defining Core

```text
Library entry (book record)
├── file(s) — one or more formats of the same work
├── metadata — title, author, cover, and beyond
├── organization — collections / tags / series / search over book attributes
└── read access — built-in reader, external handoff, or delivery to a reading client
```

Three properties. If any one is removed, the product is no longer recognizable as an e-book library:

- **A persistent collection of book entries.** The unit inside the application is a *book* — one entry per work — not a file. An entry aggregates everything the application knows about that work and survives across sessions. Without the persistent collection, the product is just a viewer opened ad hoc on a file.
- **Book-level identity and organization.** Each entry is identified as a book (title and author are its face, the cover its thumbnail) and can be grouped, filtered, and located by book attributes — not by file attributes. Without this, the product is a file manager that happens to contain books.
- **Read access for every entry.** The library exists so the books can be read. Reading may happen inside the product's own reader, in another application the book is handed to, or on a device or client the book is delivered to. Without any path to reading, the product is a bibliographic catalog, not a working library.

### Book Entry

The book entry is the center of the model. A single entry commonly holds several things at once:

- **one or more format files** of the same work — the same book may exist as EPUB, PDF, or a proprietary format, and the entry groups them rather than treating them as separate books
- **metadata** — at minimum the title and author that identify the entry; mature libraries add series and reading order, publisher, description, tags, ratings, and identifiers such as ISBN
- **a cover image** — data in its own right: fetchable, replaceable, and the dominant visual element of browsing
- **the actions available on the work** — read, convert or transfer, edit, group, remove

### Metadata

Metadata is the searchable, browsable substance of the library, and every mature product automates parts of it: reading what is embedded in the book files, deriving it from file names when the files say nothing, fetching it from online sources, or receiving it from a store. Because automation is imperfect — file names mislead, embedded data is missing — libraries treat metadata as editable data, correctable entry by entry or in bulk. The entry, not the file, is what the user curates.

### Organization Structures

Mature products offer overlapping ways to organize the same collection, and most readers use several:

- **collections / shelves** — named groupings the reader creates or the product provides by default (by genre, author, project, or status such as want-to-read and finished)
- **tags** — free-form labels applied to entries, combinable with filters
- **series** — groupings of entries that belong to one work sequence, with reading order
- **larger partitions** — some products allow several separate libraries (for instance fiction and non-fiction) or saved searches that behave like virtual shelves over the full collection
- **search** — queries over metadata, and in several products over the full text of the books themselves

### One Structure, Many Implementations

The core model is conceptual. Specific products realize each concept differently:

```text
Concept:              Book entry with files + metadata + cover
Implementations:      managed copy of imported files (desktop library manager),
                      store/cloud item record, database row generated by
                      scanning a folder tree

Concept:              Acquisition
Implementations:      file import / drag-drop, recursive folder scan with
                      auto-import on change, store purchase and re-download,
                      identifier-based lookup

Concept:              Organization
Implementations:      collections and shelves, tags, series, multiple named
                      libraries, saved searches / virtual shelves, custom filters

Concept:              Read access
Implementations:      built-in reader, open in the operating system's default
                      app, transfer to an e-reading device, send-to-device
                      service, networked library (web server, OPDS catalog,
                      cloud sync, email delivery)
```

A reader who has only seen one kind — say a store-backed shelf on a phone — should still recognize a desktop catalog-and-transfer manager, or a self-hosted family server, as the same type.

## How It Works

### Build the library

```text
Acquire books
→ (import files, scan a folder tree, buy in a store, re-download purchases)
→ an entry is created for each work
→ metadata is attached (read from the file, derived from the file name,
   supplied by the store, or fetched online)
→ the cover is attached
```

Acquisition is always an explicit step: the library does not silently absorb a disk. Some products import a chosen file; some scan a whole folder structure and keep watching it for new files; some acquire through a store. However the books arrive, the result is the same — entries in the catalog.

### Curate

```text
Select entries
→ correct metadata (fix titles, authors, series order; replace covers)
→ group (add to collections, apply tags, set series)
→ deduplicate / merge entries that describe the same work
```

Curation is the library's characteristic labor. Because books arrive from many sources with inconsistent or missing data, the recurring loop is: notice an entry that looks wrong → fix its metadata or cover → slot it into the right grouping. Mature products make this efficient with bulk editing, online metadata lookup, and entry merging.

### Locate

```text
Browse (cover grid / shelf / sortable list)
→ filter (by author, tag, series, collection, status)
→ or search (metadata query, full-text query)
→ open the entry
```

The browsing surface is dominated by covers and titles — the library is one of the few Application Types whose home screen is essentially a wall of book covers, optionally switchable to a data table with sortable columns.

### Read

```text
Open an entry
→ read in the product's own reader
   or hand off (open in another app · transfer to an e-reading device ·
   send via a delivery service)
→ in networked libraries: read in a browser or a connected reading client
```

This is the loop that completes the type. Every entry must have at least one working path to reading. Which path exists depends on the product and the format: a desktop library manager may offer its own viewer plus device transfer; a platform-integrated shelf reads in place and syncs position across devices through the cloud; a server library serves a web reader and exposes the collection to external reading apps. Handoff itself is a design decision — in some products certain formats are deliberately opened by another application rather than read in place.

### Track reading (common, not definitional)

Many libraries record reading state: want-to-read marking, progress through the book, and completion — sometimes detected automatically when the reader reaches the end. Server libraries keep this state per user. Tracking is a mature expectation in consumer products, but a library without it (a pure catalog-and-transfer manager) remains fully a library.

### Maintain and share

```text
Back up / export the collection (organized folders, portable structures)
→ optionally share it (network access with accounts, reading apps, email)
→ optionally move it (between machines, between libraries)
```

### Core vs Common vs Optional

**Defining core** — without these, not an e-book library:

- persistent collection of book entries (work-level, aggregating files)
- book-level identity and organization (metadata, collections/tags/search)
- read access for every entry (built-in reader, handoff, or delivery)
- acquisition/import that feeds the collection
- removal of entries

**Standard capabilities** — present in most current products:

- rich metadata machinery (auto-read, filename derivation, online lookup, bulk edit, merge)
- multiple formats per entry, with format management
- covers as first-class, replaceable data
- default and custom collections/shelves; tags; series grouping
- full-text search alongside metadata search
- a built-in reader for at least the core formats
- reading-state tracking (want-to-read, finished, progress)
- export/backup of the collection in organized form

**Common variants / optional** — depends on product philosophy and segment:

- format conversion (between formats, or automatic on transfer)
- e-reading-device transfer and send-to-device services
- cloud sync across a user's devices; networked access with accounts
- multi-user server operation (permissions, per-user state, age/rating restrictions)
- store integration (purchasing, re-download, recommendations)
- DRM-affected behavior (authorization, restricted formats)
- content-type breadth: audiobooks, PDFs, comic/manga image formats, samples, periodicals converted into e-books
- annotation support and annotation export to other tools
- programmatic access (APIs, OPDS catalogs)

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Library browsing surface

The home surface.

- shows the collection as a cover grid, a bookshelf-like arrangement, or a sortable list with metadata columns
- surfaces groupings (collections, libraries, filters) in a sidebar or top-level navigation
- primary actions: open an entry, filter or search, switch grouping, add books

### Book detail panel

The surface for one entry.

- cover, full metadata, the list of format files held by the entry, reading state where tracked
- primary actions: read, edit metadata, manage formats, add to collections, convert or transfer, remove

### Organization surface

The curation toolset.

- collection/shelf management, tag management, series handling, saved searches or filters
- bulk operations over selected entries (edit metadata, apply tags, merge)

### Import / acquisition surface

- file pickers and drag-drop targets, folder-scan configuration, watched-folder settings, or the store
- reports what was found or bought and what state the resulting entries are in

### Reader surface

The built-in reading experience where one exists.

- paginated or scrolled text with adjustable typography and layout
- navigation (contents, positions), and in many products highlights, notes, and dictionary or lookup aids

### Delivery / device surface

Where the library reaches outward.

- device views showing what is on a connected e-reader; send/transfer actions
- server settings and account views in networked libraries; catalogs exposed to external reading apps

### Settings

- storage location of the library, import behavior, format handling, reader defaults, and — in server products — users, permissions, and sharing

## Important Rules / Behaviors

### The library is a layer over the books, distinct from the raw files

A library's catalog is data about works, held separately from whatever files hold the text. Some desktop library managers make this explicit by keeping their own managed copies — the user's original files stay untouched while the library builds its catalog around copies — which makes the library safe to restructure (re-organize, re-format, re-export) without risking the source files. Where a library does hold the only copy (store purchases, server-scanned folders), the library's storage *is* the book's home, and backup behavior matters.

### One entry, many formats

The same work in several formats is commonly held as one entry carrying several files, not as several entries. This is where the distinction between books and files has teeth: the entry is the unit of meaning; formats are its contents. Library managers commonly allow the user to remove or add individual formats without touching the entry.

### Removal separates the catalog from the files — or doesn't

What "remove a book" means varies: deleting the entry and its files permanently, removing only one format, emptying the entry to metadata-only, or removing the entry while keeping the files. Whether a removal can be undone also varies by product. A reader should treat removal as the library's most destructive ordinary action.

### Rights management constrains what a library can do

For store-acquired or otherwise protected books, the library's abilities may be limited by rights management: conversion may be refused, transfer restricted, and some protected formats may be readable only in the vendor's designated application, with the library acting as the shelf and launcher rather than the reader. A library that handles only DRM-free files has no such constraints; the pattern, not the specifics, is the type-level rule.

### Automated metadata is a starting point, not a truth

Metadata arrives imperfect — derived from file names that mislead, embedded data that is missing, or store records that differ between editions. Every mature library therefore exposes metadata as editable, and correction is a normal, expected activity rather than an exception.

### Reading handoff is format- and product-dependent

Not every entry is read in the product's own reader. Some formats are deliberately opened by another application; some books travel to devices or remote clients. What must hold is that a path to reading exists; which path is used is a per-format, per-product decision.

### In shared libraries, state belongs to the reader

Where a library is served to multiple users, the collection is shared while the reading experience is not: each user brings their own progress, bookmarks, and restrictions, while the underlying entries are common. Access control operates at library and entry level, and age or content-rating restrictions may govern visibility per user.

## Variants

- **Desktop power library manager** — a local application centered on catalog depth: heavy metadata tooling, format conversion, device transfer, export; the archetypal form of the type and the one with the deepest curation tools (e.g. Calibre)
- **Platform- / store-integrated personal shelf** — the library embedded in an operating-system or store ecosystem: purchases accumulate automatically, reading syncs across the user's devices through the cloud, organization is collections-and-status oriented (e.g. Apple Books)
- **Self-hosted server library** — the library as a service on the user's own hardware: it scans folders for content, serves a web reader and external reading apps, supports multiple users with permissions and per-user state (e.g. Kavita)
- **Reading-device companion library** — libraries shipped by e-reader vendors to hold and organize the device's books and move them to the device; the collection is anchored to the device ecosystem rather than to open file import (market-observed family; not separately documented in this research — see Sources)
- **Content-specialized libraries** — the same structure tuned to a content class: comic and manga servers with page-oriented readers, audiobook-inclusive libraries, document-and-PDF collections
- **Store-first cloud shelf** — a thin personal library in the cloud whose books arrive almost entirely by purchase; local file import is minimal or secondary (market-observed family; not separately documented in this research — see Sources)

A variant remains a variant while the defining triad — collection of book entries, book-level organization, read access — is intact. If the product stops holding books and only records reading activity, it has crossed into a different type (see Related Application Types).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| E-book Reader | adjacent; heavily bundled | the reader's center of gravity is the reading experience for one opened book; the library's is the collection. Libraries commonly embed readers; a product that only reads (no persistent collection, no organization) is the other type |
| PDF / Document Reader | adjacent | documents are read ad hoc without book-entry curation; a PDF can live *inside* a book library as a format, but a PDF reader is not a library |
| Reading Library Application | adjacent; confusable name | the reading-tracker type records what is being read or wanted (possibly with no book files at all); the e-book library holds the files and makes them readable. Want-to-read lists inside libraries are the overlap zone |
| Digital Library Platform | distinct scale | institutional collections with patrons, lending/circulation, and licensed content; the e-book library has no circulation workflow — sharing is access, not lending |
| Reference Manager | adjacent, scholarly | organizes academic papers around citation and bibliography workflows; the book library organizes works around reading |
| File Manager | different Type entirely | operates on files by file attributes; no book identity, metadata layer, or reading intent |
| Read-it-later Application | different unit | captures web articles for later reading; unit is a clipped article, not a book in a persistent collection |
| Bookmark Manager | different unit | stores references to web locations; nothing to read inside the application itself |

The most important boundary is with the **E-book Reader**: the two types bundle each other so routinely that the market rarely sells them apart. The working discriminator is the primary job — organizing and making a collection readable versus rendering one book well — and the remove-one-thing test: strip the collection management and what remains is a reader; strip the reading surface while keeping catalog and handoff, and what remains is still a library.

## Representative Products

- **Calibre** — desktop open-source e-book library manager; the deepest documentation of catalog-and-transfer library management
- **Apple Books** — platform-integrated personal library combining store purchases, imported files, collections, and cloud-synced reading
- **Kavita** — self-hosted, multi-user server library for e-books, PDFs, comics, and manga, with web readers and OPDS

Together these span the three main philosophies of the type: the power catalog-and-transfer manager, the store-and-cloud personal shelf, and the shared server library.

## Sources

Research date: **2026-09-07**

- Calibre — product site: https://calibre-ebook.com/ · User Manual: https://manual.calibre-ebook.com/ · The Graphical User Interface: https://manual.calibre-ebook.com/gui.html
- Apple Books — Apple Books User Guide for Mac: https://support.apple.com/guide/books/welcome/mac · Organize with collections: https://support.apple.com/guide/books/organize-with-collections-ibks33867842/mac · Import books, audiobooks, or PDFs: https://support.apple.com/guide/books/import-books-audiobooks-or-pdfs-ibkseed72068/mac
- Kavita — official site: https://www.kavitareader.com/ · official wiki, Getting Started: https://wiki.kavitareader.com/getting-started/

> Sourcing limitation: official documentation for Google Play Books, Kobo, and Adobe Digital Editions could not be fetched from the research environment on 2026-09-07 (repeated request timeouts). These products are therefore not used as evidence anywhere in this document, and no claim is made about their internal behavior. The store-first cloud shelf and reading-device companion forms described under Variants are described only as market-observed families at low precision, without product-specific assertions. Claims in this document are calibrated to the three documented products; where only one sampled product exhibits a structure (for example automatic conversion on device transfer, or automatic finished-marking), it is stated as something some products do.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
