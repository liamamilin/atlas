# Reading Library Application

## Overview

A **Reading Library Application** maintains a person's own library of book records: persistent entries for books the person has read, is reading, wants to read, or owns, organized on shelves or collections the person controls, with each record carrying that reader's relationship to the book — reading state, dates and progress, ownership, ratings, reviews, notes.

The defining core is small:

```text
Book record (bibliographic identity)
└── held in the person's own organized, retained library
    └── carrying that reader's personal relationship to the book
```

What it does **not** hold is the books themselves. A reading library keeps records *about* books — the actual reading happens elsewhere: a physical copy, an e-reader, an audiobook app, a borrowed library book. If the product holds book content and presents it for reading, it has drifted into E-book Library territory; if its entries are links to web pages held for later consumption, it is a Read-it-later or Bookmark Manager.

The type appears in the market under two dominant shapes — the **reading tracker** (organized by reading status: want to read, currently reading, read, did not finish) and the **private library catalog** (organized by possession: what is on my shelves) — both built on the same core.

## Users & Context

The primary user is an individual reader — from the casual reader who wants a list of books to read next, to the heavy reader who logs every session and reviews every book, to the collector cataloging a home library. Some products also serve small organizations (classrooms, schools, community groups) cataloging and lending a shared collection.

Typical reasons to open the application:

- record a book as something to read, being read, finished, or abandoned
- check what a book was about, when it was read, what rating or notes it received
- decide what to read next by browsing the want-to-read shelf or a discovery surface
- keep a durable account of one's reading life — volumes finished this year, all-time totals, milestones
- catalog owned books (often by scanning their barcodes) so the physical library has a virtual mirror

The context is personal and long-lived. A reading library is measured in years and decades; its value grows with accumulation. Secondary concerns are privacy (how much of the library is visible to others) and portability (moving the library between products).

## Core Model

### The Defining Core

**The book record.** The unit of everything is a persistent, individually identified record of a book — anchored on bibliographic identity: title and author at minimum, commonly cover image, edition, publication details, and description. Records are deliberately added by the person: by searching the product's book catalog, importing a file exported from another service, scanning an ISBN barcode, or creating an entry manually. The record is what is kept; it is neither a link to a web page nor a book file.

**The personal library.** Records live in the person's own library — a whole that is searchable and browsable, organized into user-managed groupings. The canonical groupings are *shelves* or *collections*: named sets the person controls. The library is retained, not consumed — a book that has been read stays on the record, often for life. This is the structural opposite of a to-read queue, where handled items are cleared away.

**The personal relationship layer.** What turns a book catalog into *my* library is the data that records that reader's relationship with each book. The layer is a personal layer, not a fixed checklist — products compose it differently, drawing on:

- **reading status** — where the book stands in the reading life: want to read / currently reading / read, with a did-not-finish or stopped state common alongside;
- **reading dates and progress** — when it was started and finished, how far along it is;
- **ownership** — whether the book is in the person's physical (or digital) possession;
- **reader contributions** — a rating, a review, quotes, notes, comments.

A tracker-shaped product carries the reading-life half (status, dates, opinions); a catalog-shaped product carries the possession half (ownership, tags, notes). Both are the same personal layer weighted differently.

Remove any leg and the type collapses into a neighbor: no book records → nothing; no personal relationship layer → a neutral public book database; no organized retained library → a flat reading log or a link queue.

### Standard Capabilities of Mature Products

These capabilities are widespread and expected, but they are not what makes the product a reading library:

- **Reading-status shelves as the primary axis** — most tracker-shaped products build the whole library around a small set of statuses (want to read, currently reading, read, and usually a stopped/did-not-finish state), each a shelf of its own.
- **Custom shelves, collections, and tags** — user-created groupings beyond status: genres, moods, years, challenges, physical locations.
- **Search and filtering** across the whole library, typically by title and author keyword.
- **Import and export** of the entire library — CSV-class files are the common currency for moving between products.
- **Ratings, reviews, and notes** on records; in social products these can be aggregated on the book's page for all readers.
- **Reading goals and statistics** — some products support targets such as an annual books-read goal, and summaries of reading activity over time.
- **Discovery** — recommendations drawn from community activity or from the reader's own history.
- **Privacy and sharing controls** — from a fully private library to public shelves and profiles.
- **A shared book catalog underneath** — records usually come from a catalog maintained by the product (sometimes with user corrections and review), so the same book added by two people resolves to the same record.

### One Structure, Many Implementations

The core is conceptual; implementations differ on stable axes:

```text
Concept:          Book record
Implementations:  work-anchored record with multiple editions (tracker/social pole)
                  item-anchored record of a specific copy (cataloging pole)

Concept:          Relationship layer
Implementations:  reading-life emphasis (status, dates, progress, opinions)
                  possession emphasis (ownership, location, tags, condition)

Concept:          Library organization
Implementations:  fixed status shelves + free custom shelves
                  free-form collections + tags
```

A reader who has only seen the tracker form should still recognize the cataloging form as the same type: both hold book records in a personal, organized, retained library with a relationship layer — they merely weight different relationships.

## How It Works

### Add a book to the library

```text
Search the product's book catalog by title/author (or scan a barcode, or import a file)
→ pick the matching book record
→ the record is added to the person's library
```

The person almost never types bibliographic data from scratch; the shared catalog supplies identity, cover, and description. Manual creation is the last resort for books the catalog does not know. Imported libraries (from another reading service or a spreadsheet) are matched against the catalog, with unmatched entries flagged or created as needed.

### Work a book through its reading life

```text
Add as "want to read"
→ start reading → status becomes "currently reading" (optionally: log start date, progress updates)
→ finish → "read" (finish date recorded) — or abandon → "stopped reading" / "did not finish"
→ optionally: rate, review, take notes, quote
```

The status flow is the heartbeat of the tracker form. A book moves between statuses rather than accumulating them — a book is currently being read or has been read, not both (custom shelves are different: a book can sit in any number of user-created groupings at once). Re-reading a book simply runs it through the same statuses again — supported explicitly in at least the sampled open-source tracker, where the re-read moves the book back onto the currently-reading shelf.

In the cataloging form the analogous loop is possession-centered: scan or add the copy, assign it to a collection, tag and annotate it; reading state, if present at all, is a secondary field.

### Maintain and use the library over time

```text
Browse shelves and collections; search across the whole library
→ open a book record to see its story: status, dates, rating, notes, review
→ revisit discovery surfaces for what to read next
→ periodically: import new acquisitions, export for backup or migration
→ optionally: share shelves or the whole library publicly
```

There is no completion state for the library itself. Unlike a queue, the goal is accumulation: the record of books read this year, the growing want-to-read shelf, the mirrored home library.

### Core vs common vs optional, in one view

- **Defining:** book records; the personal organized retained library; the relationship layer on each record.
- **Common:** status shelves; custom shelves/collections/tags; search; import/export; ratings/notes; privacy controls; a shared catalog beneath.
- **Optional:** reading goals and statistics; recommendations; social layers (feeds, followers, public profiles); lending for small organizations; federated or self-hosted deployment.

## Interfaces

The surfaces below are described conceptually; names and layouts vary by product.

### My books / shelves view

The home of the library.

- shows the shelves (status shelves and custom shelves) and/or collections, commonly as cover grids or lists, plus an "all books" view of everything on any shelf
- primary actions: browse a shelf, search/filter the library, open a book record, change a book's status or grouping

### Book page

The surface for one book record.

- bibliographic information (title, author, cover, description, editions), the person's own relationship data (status, dates, rating, notes), and — in social products — aggregated community reviews
- primary actions: update reading status, log dates/progress, rate, write review or notes, assign to shelves/collections

### Search / discovery

- catalog search for adding new records; discovery surfaces (recommendations, popular books, community activity) for deciding what to read next
- primary actions: find a book, add it to the library

### Add / import

- barcode scanning (mobile), manual entry, and library import from exported files
- primary actions: scan or search to add, choose import source, review matched entries

### Profile / sharing

- the reader's public face where sharing is offered: profile, public shelves, reviews, reading goal progress; privacy settings for who sees what

## Important Rules / Behaviors

- **Records, not content.** The product never presents the text of the book. Every object in the system is about the book (identity, status, opinion); the reading itself is done elsewhere. This is the type's clearest structural signature.
- **Retention is normal.** Finished books are not cleared; they accumulate. The library's health is measured by its completeness and growth, not by an empty queue.
- **Status is usually exclusive.** In tracker-form products a book typically occupies exactly one reading status at a time — moving forward moves it out of the previous shelf — while custom shelves/collections hold books independently of status. (Documented explicitly in the sampled open-source tracker; treat the exact mechanics as product-dependent.)
- **One shared identity per book.** Because records resolve against a shared catalog, two readers referencing the same book are referencing the same record — which is what makes community reviews and comparisons possible. Users can usually correct catalog data; some products route corrections to staff review.
- **The library is portable.** Export/import is an expected property; the person's library is their data, movable between products (with the caveat that matching old records to a new catalog is approximate).
- **Privacy is graduated.** A library can be entirely private, per-shelf visible, or public; products differ in the default.

## Variants

- **Reading tracker (dominant modern form)** — status shelves, reading dates/progress, goals and stats; social layer optional (e.g. the large social reading platforms and their independent alternatives).
- **Social reading network** — the tracker with feeds, followers, and review aggregation as a first-class surface; the library remains the spine.
- **Private library catalog** — possession-centered: barcode-scanned copies, collections mirroring physical shelves, notes and tags; reading status secondary or absent; media scope may extend beyond books (movies, music, games).
- **Small-organization catalog** — the catalog plus lending, patrons, and a published catalog site for classrooms, schools, and community libraries (this variant grazes institutional library systems).
- **Self-hosted / federated** — open-source deployments where the library lives on infrastructure the reader (or a small community) controls, sometimes exchanging book metadata across servers.

## Related Application Types

| Application Type | Distinction |
|---|---|
| E-book Library Application | holds the books themselves (files/purchased titles) and presents them for reading; a reading library holds records *about* books — remove the content and reading surface from an e-book library and a reading library remains |
| E-book Reader | the reading surface for one opened book; no library organization of the person's reading life |
| Read-it-later Application | a consumption queue of saved articles/documents — items enter unread and are archived once handled, clearing is success; a reading library retains permanently and its unit is a book identity, not a saved copy of a document |
| Bookmark Manager | organizes web addresses/resources; no bibliographic identity, no reading-status lifecycle, no edition semantics |
| PDF / Document Reader, Academic Paper Reader | content-presenting surfaces for held documents, not personal book libraries |
| Integrated Library System / Library Discovery Platform | institutional catalogs and circulation serving patrons; a reading library serves one person or household; the small-org lending variant grazes this boundary |
| Social Network / Review Platform | feed/follow/review mechanics may sit on top; remove the social layer and the reading library stands; remove the library and it becomes a social network |
| Book databases (public catalogs) | the metadata substrate products search and import from; no personal relationship layer |

## Representative Products

- Goodreads — the dominant social reading platform (tracker + community)
- The StoryGraph — independent, statistics-oriented reading tracker
- BookWyrm — open-source, federated social reading tracker
- Hardcover — modern tracker with social discovery for heavy readers
- Libib — private/small-organization library cataloging (possession-centered pole)

## Sources

Research date: **2026-09-08**

Directly researched (official documentation/product pages):

- BookWyrm — https://joinbookwyrm.com/ ; https://docs.joinbookwyrm.com/ (documentation index, Shelves & Reading Status, Adding Books)
- Libib — https://libib.com/ ; https://support.libib.com/faqs.html (support site: collections, items, tags, lending, publish)
- Hardcover — https://hardcover.app/ (homepage)

Representative products whose official documentation could not be fetched during this research (timeouts or access restrictions): Goodreads, The StoryGraph, Bookly, LibraryThing, Oku, Bookmory. No operational details for these products are asserted in this document; claims about "typical" behavior rest on the directly researched sample and are worded accordingly. Precise vendor facts (item limits, import source lists, plan-gated features) are kept in the paired Research Notes.

Detailed observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
