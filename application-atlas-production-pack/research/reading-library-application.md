# Research Notes — Reading Library Application

Research date: 2026-09-08
Slug: reading-library-application
Directory position: §02.13 Personal Information Collection (sibling of Bookmark Manager)

## Research Goal

Understand what a Reading Library Application is as an Application Type: what the unit of record is, how a person's books are organized and tracked, what role reading status / reading activity / ownership / opinions play, and where the boundary sits against the heavily confusable neighbors (Bookmark Manager, Read-it-later Application, E-book Library Application, E-book Reader, and institutional library systems).

Context carried in from earlier passes (STATUS.md):

- The e-book-library-application pass left a joint-review note naming three confusable leaves and proposing working discriminators: E-book Library = holds book entries and makes them readable (collection management center of gravity); E-book Reader = the reading surface for one opened book; Reading Library Application = "reading record/wishlist without the files". That pass also observed reading-tracker functionality (want-to-read, finished detection, goals, progress) shipping as a standard capability inside e-book libraries, and raised "tracker-alone product" as a plausible distinct Type.
- The read-it-later-application pass defined its Type as a consumption queue (items enter unread, are consumed/archived; clearing is success) and explicitly named "reading library" as the retention-normal counterpart ("1+3 without 2 = reading library [retention normal]").

This pass must validate or correct both discriminators from its own evidence.

## Initial Boundary (working hypothesis before research)

- Core guess: the Type is the person's own organized collection of book records — books read, being read, wanted, or owned — with the record (bibliographic identity + personal relationship), not a readable book file, as the unit.
- Nearest neighbors: Bookmark Manager (links vs book identities), Read-it-later (queue vs permanent library), E-book Library (holds content vs holds records), E-book Reader (reading surface), Integrated Library System (institutional vs personal), Review Platform / Social Network (social layers that sit on top of the library).
- Unknowns: whether reading-status shelving is definitional or merely dominant; whether the private-library cataloging pole (e.g. home-library catalog apps) belongs to this Type or is a separate collection-catalog Type; how much social layer the Type carries.

## Research Questions

1. What is the unit of record — a book work, an edition/copy, a link, a reading session?
2. How do records enter the library (search, catalog import, barcode scan, manual entry)? Is there a shared book catalog behind the product?
3. What does the "shelf" structure mean: reading-status shelves, custom shelves, collections, tags? Mutually exclusive or overlapping?
4. What personal relationship data does a record carry: status, dates, progress, ownership, rating, review, notes?
5. Is reading content (files/text) held and presented? (Expected: no — this is the discriminator against e-book libraries.)
6. Is the social layer (feeds, followers, public profiles, review aggregation) definitional or optional?
7. What lifecycle does the library have — is it retention-normal (permanent) or consumption-oriented (cleared)?
8. Import/export: how do libraries move between products?
9. Does the org/institution pole (lending, patrons) stay inside this Type or drift toward ILS?

## Representative Products

Selected for different philosophies and customer layers; official-documentation reachability was the binding constraint, so two poles are documented from live sources and the market-dominant products could not be fetched (see Sources).

| Product | Pole / philosophy | Docs reachable |
|---|---|---|
| BookWyrm | open-source, federated, social-first reading tracker (anti-corporate community pole) | Yes — Tier-1 user documentation (docs.joinbookwyrm.com) |
| Libib | private-library / small-org cloud cataloging pole (books among other media; ownership-centered) | Yes — Tier-1 support site (support.libib.com) + product site |
| Hardcover | modern commercial tracker with social discovery ("serious book lovers" pole) | Partial — Tier-2 homepage only (FAQ/about pages JS-rendered) |
| Goodreads | dominant social reading platform (market anchor) | No — help center timeouts ×2 |
| The StoryGraph | independent stats-first tracker | No — transport error + 403 |
| Bookly | mobile session-based reading tracker | No — timeouts ×2 |
| LibraryThing | classic personal-library catalog (historical anchor, 2005-era) | No — 403 |
| Oku / Bookmory | minimal trackers | No — JS shell / empty |

Per network rules, unreachable sources were abandoned after 1–2 attempts; their structures are NOT asserted from memory in detail.

## Sources

- BookWyrm — https://joinbookwyrm.com/ (product page, 2026-09-08); https://docs.joinbookwyrm.com/ (documentation index, 2026-09-08); https://docs.joinbookwyrm.com/shelves.html (Shelves & Reading Status, 2026-09-08); https://docs.joinbookwyrm.com/adding-books.html (Adding Books, 2026-09-08)
- Libib — https://libib.com/ (product site, 2026-09-08); https://support.libib.com/faqs.html (FAQs, 2026-09-08); support site section index observed (collections, items, tags, search, add items, lending, patrons, publish, dashboards, reports)
- Hardcover — https://hardcover.app/ (homepage, 2026-09-08); /pages/faq and /pages/about returned JS-only shells (content not retrieved)
- Goodreads — https://help.goodreads.com/s/article/What-are-shelves and https://www.goodreads.com/about/how_it_works — timed out (2026-09-08)
- The StoryGraph — https://help.thestorygraph.com/ (transport error), https://www.thestorygraph.com/ and https://app.thestorygraph.com/ (403)
- Bookly — https://booklyapp.com/ and https://booklyapp.com/help (timeouts)
- LibraryThing — https://www.librarything.com/ (403)
- Oku — https://oku.club/ (JS-only shell); Bookmory — https://bookmory.com/ (empty response)

## Product Observations

### BookWyrm (evidence layer A — official documentation, directly observed)

Self-positioning: "a social network for tracking your reading, talking about books, writing reviews, and discovering what to read next", decentralized via ActivityPub.

Unit of record and structure:

- The unit is the book. Books are organized on **shelves** on a "Your Books" page whose tabs are the shelves plus an "All books" view ("displays any book that is on at least one of your shelves").
- **Four default reading-status shelves: To Read, Currently Reading, Read, Stopped Reading** — "used to track the reading status of each of your books". A "Stopped Reading" shelf exists for DNF (did-not-finish) books.
- Expected reading flow: `Not shelved → To read → Currently reading → Read`; the default button moves a book to the next stage; a dropdown allows skipping steps or selecting any status manually.
- **A book can be on only one of the four status shelves at a time** — updating status moves it. Re-reading puts the book on Currently Reading even though it was read before.
- **Custom shelves are completely separate from status shelves**: a book can be on multiple custom shelves simultaneously, and on a custom shelf plus a status shelf, or only a custom shelf. Shelf descriptions editable; filter by keyword (title/author); per-shelf privacy (default public; can be followers-only or private).
- **Reading activity**: start/finish dates prompted when starting/finishing; visible on the book page under "Your reading activity"; "Store started/stopped/finished reading dates, as well as progress updates along the way". Manually added read dates do not auto-shelve the book.
- Reader contributions attach to the book page: reviews with or without ratings (aggregated on the book page, including across connected instances), comments, quotes/excerpts, replies; posting status updates to feeds with granular privacy.
- Reading goal: "set an annual reading goal" (product page).
- Lists: books lists open to submissions, curated, or creator-edited; groups with group-owned lists.

Getting records in:

- Search local instance; if no results, external catalogs (OpenLibrary, Inventaire, other BookWyrm instances) are automatically queried with an "Import book" button; "Load results from other catalogues" for more.
- Works and editions are modeled: "add another edition to the work" — the work is the anchor, editions hang off it.
- Manual creation of a completely new book as last resort; the docs explicitly order the options: import before create.
- Bulk import of an existing library: CSV/TSV import from Calibre, Goodreads, LibraryThing, OpenLibrary, Storygraph, OpenReads; import matches against "the local database, connected BookWyrm servers, and selected public data sources" and may not match everything.
- Federation: book metadata is shared between instances to form "a networked database of metadata"; shared books identified across instances and related content aggregated.

Boundary-relevant: no book content is delivered or presented — every documented object is about books (records, statuses, reviews, dates), never the text of reading.

### Libib (evidence layer A — official support site + product site, directly observed)

Self-positioning: "Cloud Cataloging. Your library has never looked so good. Books, Board Games, Movies, Music and Video Games." — "caters to libraries, schools, organizations, and home catalogs".

Unit of record and structure:

- The unit is the **item** — a catalog record of a physical thing (a specific book/game/movie copy), created by scanning its ISBN/UPC barcode ("Just scan your ISBN/UPC barcode using a physical scanner or our free mobile apps and we take care of the rest" — automatic data from barcode) or added via the Add Items page.
- **Collections** are the organizing structure — "a logical or physical separation of items" (home library vs office library; media types; classrooms), up to 100 per account. **Tags are recommended for categorization such as genres** — an explicit two-axis organization guidance (collections = logical/physical groupings; tags = categories).
- Item records carry covers, titles, descriptions, creators — all user-editable; a "flag" option routes bad records to staff review ("within 48 business hours"); Pro/Ultimate can edit all data including LCCN/DDC/OCLC/LCC classification fields (books only).
- Library surfaces: Library view, Search, Item Overview, Batch Edit; mobile app mirrors collections/items/tags/search; cloud sync across devices.
- Sharing: "share your collections"; import/export; Pro tier adds a published interactive online library site.
- Pro/Ultimate (organization pole): **lending, patrons, patron holds, checkouts, managers, custom fields, barcode management, dashboards, reports**, REST API, SSO.
- Media scope is deliberately multi-media (books, board games, movies, music, video games) — "keep them together or separate".
- Account-scale facts (vendor-specific): 5,000 items Basic, 100,000 Pro/Ultimate; 100 collections.

Boundary-relevant: ownership-centered, not reading-status-centered. No reading-status shelves, reading dates, progress, or goals appear anywhere in the documented front door; the personal relationship the record carries is possession + notes (+ tags), plus lending in the org pole. No content is delivered.

### Hardcover (evidence layer B/C — product homepage only; limited depth)

Homepage (Tier-2 marketing, directly observed):

- Self-positioning: "Social discovery for serious book lovers".
- Four named verbs: Find ("Search and browse for new books – or find inspiration in other reader's libraries"), **Track ("Track every book by want to read, currently reading, read and did not finish")**, Connect ("Explore others reader's bookshelves and follow for their next reads"), Discover ("Uncover new books and authors based on your reading history and preferences").
- Status vocabulary independently matches the tracker pole: want to read / currently reading / read / did not finish.
- The person's collection is called a "library" with "bookshelves"; libraries of others are browsable; following exists.
- FAQ/About pages are JS-rendered shells — no operational detail retrieved. All deeper Hardcover claims are withheld.

### Goodreads / The StoryGraph / Bookly / LibraryThing (no live evidence — limitations)

- Unreachable (timeouts / 403 / JS shells). These are market anchors (Goodreads the dominant social reading platform; StoryGraph the stats-first alternative; LibraryThing the classic cataloger) and are listed as representative products, but no structural claims about them are asserted from memory in this research. Their known shapes are consistent with the two poles documented above (tracker/social shelf model; cataloging model), which is used only as background, not as evidence.

## Cross-product Comparison

| Dimension | BookWyrm (A) | Hardcover (B, homepage) | Libib (A) |
|---|---|---|---|
| Unit of record | the book (work with editions) | "every book" (unspecified depth) | the item (specific copy, ISBN/UPC-scanned) |
| Organizing structure | 4 default status shelves + custom shelves + lists | statuses + "library/bookshelves" | collections (logical/physical) + tags |
| Reading status | To Read / Currently Reading / Read / Stopped Reading, one at a time | want to read / currently reading / read / did not finish | none documented (possession + tags instead) |
| Reading dates / progress | start/finish dates + progress updates | not documented (homepage level) | none documented |
| Rating / review / notes | reviews ± ratings, comments, quotes; aggregated on book page | not documented | notes (plus user-editable metadata) |
| Ownership semantics | incidental (not the point) | not documented | the point (catalog what you own; lending in Pro) |
| Getting records in | search → external catalogs (OpenLibrary/Inventaire/instances) → manual create; CSV/TSV import | search/find | barcode scan → automatic data; add items |
| Shared catalog behind product | yes — federated metadata network + public sources | implied ("find new books") | yes — automatic data from barcode; staff-reviewed records |
| Content delivery | none | none | none |
| Social layer | core to positioning (feeds, followers, federation) | core to positioning (share, follow) | absent (sharing of collections, not social) |
| Privacy controls | granular (public/followers/private per shelf/list/post) | not documented | public sharing via published site (opt-in, Pro) |
| Import/export | CSV/TSV import from 6 named sources | not documented | import/export |
| Goals / stats | annual reading goal | not documented ("reading history" implied) | none documented (dashboards/reports are org-side) |
| Deployment | self-hosted open-source, federated | hosted commercial | hosted commercial (tiered) |

## Canonical Model

### Level 0 — Defining Invariant (deliberately small)

1. **The book record as the unit of the library.** A persistent, individually identified record of a book — anchored on bibliographic identity (title/author, commonly cover and edition information) — deliberately added by the person (search against a book catalog, import, barcode scan, or manual entry). Remove → no library exists; only browsing history or a link list.
2. **The personal library as an organized, retained collection.** The records are organized in user-managed groupings (status shelves, custom shelves, collections, tags) and searchable/browsable as one whole; entries persist indefinitely — the accumulated library is the product's value, not a queue to be emptied. Remove → a flat book list / triage queue, not a library.
3. **The personal relationship layer on each record.** The record documents *that reader's* relationship with the book — reading state (want/current/read/stopped), reading dates and progress, and/or ownership, plus reader contributions (rating, review, notes). Remove → a neutral bibliographic catalog (a public book database), not a personal reading library.

Jointly-held load-bearing tests:

- 1 alone → public book-metadata database (OpenLibrary-class).
- 1+2 without 3 → an organized copy of a bibliographic catalog with no personal layer — a book database in folders, not a reading library.
- 1+3 without 2 → a flat reading log/list — the library structure is gone.
- 2+3 without 1 → empty groupings; nothing anchored.

### Level 1 — Common Mature Structure (very common, not definitional)

- **Reading-status shelving as the primary organizing axis** — want-to-read / currently-reading / read, almost always with a did-not-finish/stopped state; documented in both sampled tracker products and the market anchor vocabulary. Held at L1 because the cataloging pole (Libib) runs on possession+tags and still belongs to the Type; and because e-book libraries embed the same status machinery without being this Type.
- Search/browse across the library (keyword/title/author filtering).
- Import/export of the whole library (CSV-class) between products — the market assumes library portability.
- Ratings/reviews/notes on records; reading dates and progress updates.
- Reading goals and reading statistics (annual target documented in one product; stats-heavy trackers are a market staple).
- Privacy/sharing controls over the library and its parts.
- Discovery — recommendations from community activity or from one's own reading history.
- Records drawn from a shared product-maintained book catalog, with user corrections/flagging possible.

### Level 2 — Variant / Optional Structure

- Social layer depth: none → follow/feed/review aggregation → fully federated social network.
- Record anchoring: work-centric with multiple editions (tracker/social pole) vs item/copy-centric (cataloging pole).
- Emphasis: reading-life (tracker) vs possession (private home library).
- Media scope: books-only vs mixed-media cataloging.
- Deployment: hosted SaaS vs self-hosted open-source.
- Organization axes: named shelves/collections vs free-form tags (products guidance differs; both exist).

### Level 3 — Vendor-specific (kept here, not in the final document)

- BookWyrm: ActivityPub federation; instance-to-instance book-metadata sharing and cross-instance review aggregation; import source list (Calibre/Goodreads/LibraryThing/OpenLibrary/Storygraph/OpenReads); status types (comment/quote besides review); BookWyrm Vocabulary document; `/create-book` path; manual-read-dates-do-not-shelve behavior; "Flag/issue" contribution flow.
- Libib: 5,000/100,000 item limits; 100-collection cap; Pro lending/patron/hold/checkout machinery; published interactive library site; kiosk; LCCN/DDC/OCLC/LCC fields; 48-business-hour flag review; barcode-manager; mixed-media types (board games etc.); REST API/SSO (Ultimate).
- Hardcover: Discord role linking; roadmap board; community channels.

## Vendor-specific Findings (summary)

- Federation (BookWyrm) is a deployment/social architecture, not a Type property.
- Lending/patron management (Libib Pro) pulls the product toward a mini Integrated Library System for organizations — a boundary-drift example retained as a variant pole, not core.
- The "collections vs tags" guidance (Libib) and the "status shelves vs custom shelves" split (BookWyrm) are two realizations of the same conceptual need: separating *where a book is in its reading life* from *how the reader groups books*.

## Boundary Findings

1. **vs E-book Library Application** — the content boundary. An e-book library holds the books themselves (files/purchased titles, stored or store-served) and presents them for reading; a reading library holds *records about* books and never presents the text — reading happens elsewhere (physical copy, e-reader, audiobook app). Remove content-holding + the reading surface from an e-book library → a reading library; make content the center of gravity → e-book library. This pass **ratifies the e-book-library pass's discriminator** and **resolves its open question**: the tracker-alone product (records reading activity, may hold no book files) fits THIS Type — tracker vs cataloger are two variants of the same L0 (relationship layer = reading-life vs possession emphasis), so no separate tracker Type is created.
2. **vs Read-it-later Application** — the queue boundary. Read-it-later is consumption-oriented: items enter unread, the primary surfaces sort by reading state, and handled items are archived/removed — clearing is success; its unit is a specific saved article/document instance carrying its source content. The reading library is retention-oriented: the record of a book stays (a finished book stays on Read), the unit is a book identity (edition-independent), and the content is not held. Queue-removal semantics vs permanent retention is the sharpest test.
3. **vs Bookmark Manager** — the unit boundary. A bookmark manager organizes web addresses/resources; a reading library organizes book identities. A bookmark may carry read/unread, but there is no bibliographic catalog behind it, no reading-status lifecycle, no edition/work semantics.
4. **vs E-book Reader / PDF-Document Reader / Academic Paper Reader** — the surface boundary. Those Types present content for reading; this Type records. A reading library at most links out to acquisition/reading venues.
5. **vs Integrated Library System / Library Discovery Platform** — the institutional boundary. ILS/Discovery serve an institution's catalog and its patrons (acquisition, circulation, cataloging standards); the reading library serves one person (or a household). Libib's Pro lending layer is the in-sample drift example: an org variant that grazes the ILS boundary but keeps the personal-catalog core.
6. **vs Social Network / Review Platform** — the layer boundary. Tracker products commonly add feeds, followers, and public reviews aggregated on book pages. Remove the social layer → still fully a reading library; remove the library → a social network. The library is the spine; sociality is optional tissue.
7. **vs Book databases (OpenLibrary-class)** — the data-source relationship, not a Type boundary: public bibliographic catalogs are the substrate the products search/import from. No personal layer → not this Type.

**Historical / market-sample check**: a paper-era personal book log (notebook of books read with dates and opinions) plus a home-library card catalog (ownership, location) satisfies all three L0 legs — records, organized retention, personal relationship layer. LibraryThing (2005-era cataloger), spreadsheet reading lists, platform-native "Want to Read" mini-features, and regional reading communities all fit without any modern machinery. The definition below names no social graph, no ISBN, no cloud, no mobile app, no stats engine, no monetization.

## Uncertainties

- **Dominant products unreachable**: Goodreads, The StoryGraph, Bookly, LibraryThing, Oku, Bookmory could not be fetched (timeouts/403/JS shells). Their structural details are NOT asserted; the canonical model rests on the three documented products, with the unreachable anchors treated as background. The final document's claims about "typical products" are calibrated accordingly.
- **Cataloging-pole status support**: whether Libib-class products optionally carry reading-status fields is unconfirmed from fetched pages (absent from all fetched front-door docs); treated as "not part of their documented center".
- **Hardcover depth**: FAQ/About pages are JS-rendered; Hardcover evidence stays at homepage vocabulary (statuses, libraries, follow, discover).
- **Record-anchoring spread**: work-with-editions (BookWyrm, documented) vs item/copy (Libib, documented) are two poles; where the market median sits was not measured.
- **Acquisition links**: whether products typically deep-link to retailers/libraries for acquisition was not directly evidenced in fetched docs (Hardcover "Find new books" implies discovery-to-acquisition but the mechanism is undocumented).

## Final Synthesis

A Reading Library Application is the reader-facing application that maintains a person's own library of book records: persistent records of books — read, being read, wanted, or owned — organized on shelves/collections the person controls, each record carrying that reader's relationship with the book (status, dates, progress, ownership, opinions). It holds records about books, not the books themselves; reading happens outside it. It retains rather than consumes; it is personal rather than institutional; its social layer, however prominent in the market, is optional tissue on a private spine. The dominant modern form is the reading tracker with status shelves (want/current/read + DNF); the cataloging form (private home library) is the possession-centered variant of the same core.
