# Research Notes — E-book Library Application

Research date: 2026-09-07
Methodology: v1.1 (update-v1/)

## Research Goal

Understand what an E-book Library Application is as an Application Type: what objects it manages, how books enter the library, how the library is organized, how read access is delivered, what state is tracked, and where its boundaries run against the E-book Reader, PDF/Document Reader, Reading Library Application, Digital Library Platform, Reference Manager, and generic file managers.

## Initial Boundary (working hypothesis before research)

- Hypothesized core: a managed collection of e-book files organized as *books* (metadata, covers, groupings) rather than as generic files, with read access delivered by a built-in reader, external handoff, or device transfer.
- Suspected confusions: E-book Reader (reading surface), Reading Library Application (reading tracker, directory-adjacent in 02.13), Digital Library Platform (institutional lending), Reference Manager (academic PDFs), File Manager.

## Research Questions

1. What is the unit inside the library — a file, a work, or something else?
2. How do books enter the library (import, scan, purchase, download, borrow)?
3. What metadata machinery exists (auto-read, filename guessing, online fetch, manual edit)?
4. What organization structures exist (collections/shelves, tags, series, saved filters, multiple libraries)?
5. How is read access delivered (built-in reader, external app, device transfer, server/OPDS/email)?
6. What reading state is tracked (progress, want-to-read, finished)? Is it definitional or common?
7. What constraints exist around formats and DRM?
8. Do single-user and multi-user libraries differ structurally?
9. Where are the type boundaries (Reader vs Library vs Tracker vs institutional library)?

## Representative Products

| Product | Philosophy / pole | Why sampled |
|---|---|---|
| Calibre | Desktop power library manager (open source; catalog + conversion + device transfer + content server) | The archetypal dedicated library manager; deepest documentation in the category |
| Apple Books | Platform-native consumer integration (store + personal library + cloud sync + reader) | Consumer-integrated pole; shows library merged with store and OS |
| Kavita | Self-hosted multi-user server library (scan-based; EPUB/PDF/comics/manga; OPDS) | Server pole; shows the library as a shared service with users and permissions |

Coverage check: three philosophies (power tool / platform-native consumer / self-hosted server), three deployment surfaces (desktop file-based / OS-integrated cloud / web server), personal vs multi-user. Store-first cloud shelves and device-ecosystem companion apps (Google Play Books, Kobo, Kindle, Adobe Digital Editions) could not be reached — see Source-access Limitation.

## Sources

Fetched successfully (2026-09-07):

- Calibre — https://calibre-ebook.com/ (product page, Tier 2)
- Calibre — https://manual.calibre-ebook.com/ (User Manual, Tier 1)
- Calibre — https://manual.calibre-ebook.com/gui.html (The Graphical User Interface, Tier 1)
- Apple Books — https://support.apple.com/guide/books/welcome/mac (Apple Books User Guide for Mac — TOC + intro, Tier 1)
- Apple Books — https://support.apple.com/guide/books/organize-with-collections-ibks33867842/mac (Organize with collections, Tier 1)
- Apple Books — https://support.apple.com/guide/books/import-books-audiobooks-or-pdfs-ibkseed72068/mac (Import books, audiobooks, or PDFs, Tier 1)
- Kavita — https://www.kavitareader.com/ (product site, Tier 1/2)
- Kavita — https://wiki.kavitareader.com/getting-started/ (official wiki, Tier 1)

Unreachable (source-access limitation):

- Google Play Books — https://support.google.com/googleplay/answer/3096521 — timed out ×2
- Kobo help center — https://help.kobo.com/ and /hc/en-us — timed out ×2
- Adobe Digital Editions — https://helpx.adobe.com/digital-editions/... — timed out ×2

Consequence: no claims are made about the internal capabilities, upload limits, or behaviors of Google Play Books, Kobo, or Adobe Digital Editions. The sample is three products; cross-product claims below are calibrated to that sample.

## Product Observations

### Calibre (Evidence layer A — official manual, fetched)

- Self-description: "calibre is an e-book library manager. It can view, convert and catalog e-books in most of the major e-book formats. It can also talk to many e-book reader devices. It can go out to the Internet and fetch metadata for your books." (manual index)
- **Unit**: a book record in an internal database; "calibre will automatically try to read metadata from the books and add them to its internal database." "Note that calibre creates copies of the files you add to it. Your original files are left untouched." The library is a managed copy of the user's files, organized as book records. One record can hold multiple format files ("Add files to selected book records"; "Remove files of a specific format").
- **Acquisition**: Add books from single folder / folders and sub-folders (recursive scan; folder = one book with multiple formats) / from archives (ZIP/RAR/7z) / **Add empty book (book entry with no formats)** / **Add from ISBN** / add files to existing records / add extra data files. Also **Fetch news**: downloads news sites via recipes and converts them into e-books added to the library.
- **Metadata machinery**: reads metadata from book files; configurable guessing from file names (default regex `title - author`); Edit metadata individually (with online metadata + cover fetch) / in bulk / Download metadata and covers; merge book records; copy/paste metadata; custom columns; notes attached to authors/series; metadata stored in `metadata.db` with per-book OPF backups.
- **Organization**: multiple named Libraries ("Libraries are the highest organizational structure within calibre. Each library has its own set of books, tags, categories and base storage location"); Virtual libraries (saved-search-defined partitions — "a way to pretend that your calibre library has only a few books"); Tag browser (browse by Author/Tags/Series, hierarchical items, sub-categories, click-to-filter); saved searches; temporarily marking books (pins, text labels); sort by columns; powerful search language (field:value, boolean, regex, dates, relational, identifiers incl. ISBN/DOI, virtual-library scoping, template searches); optional full-text indexing of all books.
- **Browsing surfaces**: book list with configurable columns; Cover grid; Bookshelf view; Cover browser; Book details panel (cover + all metadata; clickable author links to Wikipedia/retailer pages; drag-drop cover replacement; per-format actions).
- **Read access**: built-in E-book viewer (navigation, highlighting, read-aloud, dictionary, look & feel, paper-edition sync) — or open with the OS default application ("For other formats it uses the default operating system application"); **Send to device** (main memory/card A/card B; auto-converts to the device's format if needed; send-and-delete-from-library; fetch annotations from device into book comments); **Save to disk** (organized Author/Title folder structure with OPF metadata, re-importable without loss); **Connect/share**: connect-to-folder as device, built-in Content server (library accessible via web browser, with user accounts), email-based sharing.
- **Conversion**: individual / bulk; extensive conversion options (look & feel, page setup, heuristics, structure detection, TOC); auto-convert on send-to-device. DRM rule: "Many e-books available for purchase will be protected by DRM technology. calibre will not convert these e-books."
- **Catalogs**: generate a listing of the library (with all metadata) as XML/CSV/BiBTeX or as an e-book (EPUB/MOBI/AZW3) that can be sent to a device.
- **Removal**: Remove books is permanent (book record + files), with a trash/restore-recently-deleted mechanism; per-format removal possible; remove covers.
- **Other**: e-book editor, e-book comparison tool, CLI, plugins, template language, jobs queue. (Editor/comparison are authoring tools, not library semantics — vendor extensions.)

### Apple Books (Evidence layer A — official user guide, fetched)

- Positioning: "Build your library — Choose from millions of books and audiobooks — classics, bestsellers, and more — to create your personal library." "Your library, your way. Organize your library any way you like. With collections, every one of your books is right where you want it. Use default collections or create your own for your favorite authors, genre, or book club picks."
- **Units**: library items are books, audiobooks, PDFs, and samples ("All: Shows all of the books, audiobooks, PDFs, and samples in your library").
- **Acquisition**: find and buy in Book Store / Audiobook Store; get books in a series; **Import** (File > Import; drag-and-drop; "PDFs, mp3 audiobooks, Audible audiobooks, and many EPUB books"); download purchased and updated items; redeem gift cards; iCloud carries imported books/purchases/PDFs across devices.
- **Format/DRM rules**: "Some content (such as ACSM, AZW, and ODM files) can only be opened in the associated third-party app. If you're not sure which app you need to open your book or audiobook, check with the library or eBook store that provided the content." "PDFs open in Preview (or your default PDF reader), rather than in Books." "Authorize your Mac" (DRM authorization step for protected content).
- **Organization**: collections in the sidebar; default collections: All, **Want to Read** (user-added, also addable from the store), **Finished** ("Books and audiobooks are automatically added to this collection when you reach their end. You can also add books to this collection manually — even if you read them outside Apple Books"), Books / Audiobooks / PDFs / My Samples (by item type); custom collections; sorting.
- **Reading state**: Finished with editable finished date and a timeline view; Want to Read; reading goals ("Set reading goals").
- **Read access**: built-in reader (read books, change a book's appearance); audiobook listening; multi-device via iCloud ("Use iCloud to read and listen on all your devices"); PDF handoff to external Preview.
- **Other surfaces**: highlights and notes, study cards, glossaries/definitions, share, rate and review, recommendations improvement, explicit-content restriction, notifications.

### Kavita (Evidence layer A — official site + wiki, fetched)

- Self-description: "Kavita is an open-source, self-hosted digital library management system primarily designed for managing and reading comics, manga, and ebooks." Site tagline: "self-hosted digital library for EPUB, PDF, comics and manga — with built-in readers (single, double page, and webtoon mode), OPDS, and rich metadata."
- **Acquisition**: Library Scanner (wiki has per-format scanner guides: Manga, Comic, EPUB, PDF, Images; "Managing Files"); **Folder Watching** ("Automatically import new files from watched folders for painless library updates").
- **Metadata machinery**: "Kavita scans and parses metadata from filenames and ComicInfo.xml. Enhance your library with external cover art, descriptions, ratings, and reviews through Kavita+"; external metadata tools documented (ComicTagger, Komf); per-format metadata guides (Comics/Epubs/PDFs).
- **Organization**: multiple Libraries (admin setting; libraries typed by content); custom tags and filters; **Custom Filters** ("Create custom filters ... then bind them to your Homepage or Side nav"); Collections; **Reading Lists** ("Create curated lists, share them with friends, and pin reading queues"); Relationships (series/edition linkage); full-text search & indexing.
- **Multi-user**: "User Management: Use OIDC or built-in logins to manage your users. Restrict access based on library or age restrictions. Full control over who sees what, with granular permission settings." "Create multiple users with different permissions to access your library, each with their own progress tracking and age restrictions."
- **Read access**: built-in web readers per format (EPUB reader, PDF reader, Comic/Manga reader with webtoon mode, single/double page); **OPDS** ("Expose your library to OPDS-enabled readers and third-party apps"); **Send to Kindle** ("One-click send to Kindle or other devices so you can read offline"); third-party client apps (KOReader, Panels, Paperback, Mihon, etc.); REST API + OPDS feeds.
- **Reading state**: per-user progress tracking; bookmarks; annotations (highlight/notes, shareable within the server, export to Obsidian); Kavita+ premium: progress sync with external sites (AniList/MAL/Mangabaka/Hardcover), want-to-read sync, smart collections, external ratings/reviews, recommendations; scrobbling.
- **Content-rating governance**: rating/age restrictions on visibility.

## Cross-product Comparison

| Aspect | Calibre | Apple Books | Kavita |
|---|---|---|---|
| Self-description | "e-book library manager" — view, convert, catalog | "create your personal library" from store + import | "self-hosted digital library management system" |
| Unit in library | Book record: internal DB entry aggregating multiple format files + metadata + cover; managed copy of originals | Item: book / audiobook / PDF / sample, from store or import | Series/book entry produced by scanning files (filename/ComicInfo.xml/EPUB/PDF metadata) |
| Acquisition | Add from disk (folders/recursive/archives/ISBN/empty record), fetch news | Store purchase, File > Import, drag-drop, re-download purchases via iCloud | Folder scan, watched-folder auto-import |
| Metadata machinery | Read from file; guess from filename; edit single/bulk; download metadata+covers online; merge records; custom columns | Automatic for store items (import detail not fetched — not asserted) | Scan/parse from filenames, ComicInfo.xml, format internals; external metadata (Kavita+/tools) |
| Organization | Multiple libraries; virtual libraries; tag browser; saved searches; marks | Default + custom collections (sidebar); sort | Multiple typed libraries; collections; reading lists; custom filters bound to home/nav |
| Reading state | Marks (temporary); device annotations pulled into book record; no progress model asserted | Want to Read; Finished (auto on reaching end; manual; finished date; timeline); reading goals | Per-user progress; bookmarks; annotations; want-to-read sync (Kavita+) |
| Read access | Built-in viewer OR OS default app; send to device (auto-convert); save to disk; email; content server (web) | Built-in reader; audiobook player; PDF opens in external Preview; iCloud multi-device | Built-in web readers (EPUB/PDF/comic); OPDS to external apps; Send to Kindle; API/clients |
| Format conversion | Deep (individual/bulk/auto on transfer) — signature capability | None evidenced | None evidenced |
| DRM posture | Will not convert DRM books (documented) | Authorize Mac; some formats open only in third-party apps | Not applicable/not evidenced (own files) |
| Users | Personal; content server adds user accounts for remote access | Personal, single user; iCloud sync | Multi-user with permissions, age/rating restrictions, OIDC |
| Content breadth | E-books + news-as-e-books | Books + audiobooks + PDFs + samples | E-books + comics/manga + PDF (image formats) |
| Storage model | Local managed copy (metadata.db + files + OPF backups) | Cloud/store-backed + local imports (iCloud) | Self-hosted server over user-provided folders |

### Stable commonalities across the sample (B-layer)

1. A persistent catalog of book entries — each entry is a *work* aggregating file(s), metadata, and cover; not a raw file listing.
2. Books enter through an explicit acquisition/import step (file import, folder scan, or store purchase/download).
3. Book-level metadata exists and is the basis of browsing; metadata can be automated (file-internal, filename, or store-supplied) and corrected manually.
4. Organization into named groupings: collections/shelves (Apple), libraries/virtual libraries/tags (calibre), collections/reading lists (Kavita).
5. A browsing surface dominated by covers + titles (cover grid, bookshelf, sidebar shelves).
6. Search/locate over the collection (metadata search everywhere in the sample; full-text indexing in calibre and Kavita).
7. Read access to every entry, delivered by built-in reader, external handoff (OS app, device transfer, OPDS client), or networked delivery (content server, email, iCloud).
8. Removal/retirement of entries from the library.

### Divergences (not definitional)

- Conversion engine: only calibre (power-manager pole).
- Reading-status tracking: strong in Apple Books and Kavita; minimal/pull-based in calibre.
- Multi-user sharing: only Kavita (server pole); calibre's content server adds accounts; Apple Books is single-user.
- Content-type breadth varies (audiobooks, PDFs, comics, samples).
- DRM posture varies with business model.

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

1. **Persistent library collection of book entries** — the application keeps a durable, enumerable collection in which the unit is a book entry (a work) aggregating the book's readable file(s), its metadata, and its cover. Remove this and the product is an ad-hoc file viewer (E-book Reader / PDF viewer) or a generic file manager.
2. **Book-level identity and organization** — entries are identified and browsable as books (title/author-level identity visible on the entry; groupings, tags or search that operate on book attributes rather than file attributes). Remove this and the product is a file manager / folder of files.
3. **Read access for every entry** — the collection exists to be read: each entry can be opened through a reader built into the product, handed off to an external reading surface (OS application, e-reader device), or delivered over the network to a reading client. Remove this and the product is a bibliographic catalog/database, not a working library.

Notes on the L0 boundary:
- No cloud, no store, no conversion, no annotations, no reading-progress tracking, no device sync, no multi-user, no server is required. Older desktop library managers (calibre's own 2006-era core; the pre-cloud era of e-book management) satisfy the L0 — the historical check passes. File-import + metadata + shelves + reader/handoff is the timeless floor.
- "Read access" is deliberately defined as *built-in reader OR handoff OR delivery*: calibre's View action explicitly includes "uses the default operating system application", and Apple's PDFs open in Preview. A library with only handoff is still a library.
- Metadata floor is deliberately thin: title/author-level identity + browsable organization. Rich metadata (series indices, ratings, custom columns, identifiers) is L1/L2.

### L1 — Common Mature Structure

- **Import/acquisition machinery**: add from disk (files, folders, recursive scan, archives), drag-drop, watched folders, store purchase + re-download of purchases.
- **Metadata management**: auto-read from book files, guessing from filenames, single/bulk editing, online metadata + cover download, merging duplicate entries.
- **Organization structures**: default + custom collections/shelves; tags; series grouping; multiple libraries; saved searches/filters.
- **Browsing surfaces**: cover grid / bookshelf / list with sortable columns; book detail panel (cover, metadata, formats, actions).
- **Search**: metadata search; full-text search of book contents (calibre optional indexing; Kavita indexed; Apple not asserted).
- **Built-in reader** for at least the core format(s), with appearance/typography options.
- **Export/save back out** of the library in organized form (calibre Save-to-disk with OPF; store re-download equivalent).
- **Removal** with per-entry and per-format granularity.
- **Covers as first-class data** (fetchable, replaceable, the browsing face).

### L2 — Variant / Optional Structure

- **Conversion engine**: convert between formats (individually/bulk), auto-convert on device transfer — power-manager variant.
- **Device handoff**: USB e-reader transfer with format/profile matching, send-to-Kindle-style delivery, email delivery.
- **Networked library**: content server with accounts (calibre), OPDS exposure, REST API, third-party reader clients (Kavita), iCloud-style cloud sync (Apple).
- **Multi-user server posture**: users, permissions, library- and age-rating restrictions, OIDC, per-user progress.
- **Reading-state tracking**: want-to-read, finished (auto-detect on reaching the end — Apple; manual marking), progress, bookmarks, annotations, scrobbling/external progress sync.
- **Content-type breadth**: audiobooks, PDFs, comic/manga image formats (webtoon/panel modes), samples, news-as-e-books.
- **DRM posture**: DRM-conversion refusal, DRM authorization, formats locked to designated third-party apps.
- **Store/editorial integration**: purchasing, recommendations, ratings/reviews, reading goals.
- **Ecosystem metadata exchange**: ComicInfo.xml, external tagging tools, annotation export to other apps.

### L3 — Vendor-specific (research notes only)

- Calibre: Virtual libraries / Tag browser / Quickview terminology; template language; news recipes; plugins; metadata.db + per-book OPF storage; e-book editor; e-book comparison tool; calibre:// URL scheme; catalogs generated as e-books; "fetch annotations" from device.
- Apple Books: Want to Read / Finished default collections with auto-finish detection and editable finished date; My Samples; Reading Goals; Study Cards; Top Picks; explicit-content restriction; Authorize your Mac; x-help-action deep links.
- Kavita: Kavita+ (AniList/MAL/Mangabaka/Hardcover progress sync, smart collections, external ratings/reviews); scrobbling; CBL import; Relationships; Media Issues report; webtoon mode; bindable smart filters to homepage/side nav; SSE4.2 requirement.

## Vendor-specific Findings

- Conversion depth is effectively a single-product signature in this sample (calibre). It must not enter the defining core: nothing in being a *library* requires conversion.
- Reading-state auto-detection (auto-add to Finished on reaching the end) is documented for Apple Books; Kavita tracks progress per user; calibre has no asserted reading-progress model. Treat auto-finish as product-specific, reading-state tracking generally as common-but-not-universal.
- Multi-user permission models are documented only in the server-pole product (Kavita); calibre's content server has user accounts for remote access. Treat multi-user as a deployment variant, not a Type property.
- DRM-specific rules are ecosystem-dependent (calibre refuses conversion; Apple documents third-party-app-only formats). No universal DRM rule can be stated.

## Boundary Findings

- **vs E-book Reader**: the reader's center of gravity is the reading experience for one opened book (typography, pagination, annotation-while-reading). The library's center of gravity is the collection (acquire, organize, locate, maintain, deliver). Products straddle: all three sampled products embed readers. The discriminator is the primary job, not feature presence. Test: remove the collection management → E-book Reader / viewer; remove the reading surface but keep catalog + handoff → still recognizably a library.
- **vs PDF / Document Reader**: documents are read ad hoc without curation as a book collection. A PDF *format inside* a book library is normal (Apple treats PDFs as library items; Kavita scans PDFs); a PDF reader with no library semantics is the other type.
- **vs Reading Library Application** (directory 02.13, Personal Information Collection): the tracker-type records what one reads/wants to read and may hold no book files at all. The e-book library holds the files and makes them readable. Overlap zone is real and documented: Apple Books ships Want to Read/Finished; Kavita+ syncs want-to-read lists. Taxonomy flag raised (see below).
- **vs Digital Library Platform** (directory 23): institutional platform = patrons, loans/circulation, licensed collections, discovery for an organization. Personal/server e-book library = no circulation or lending workflows evidenced in the sample; Kavita's sharing is access control, not lending.
- **vs Reference Manager**: reference managers organize scholarly records around citation/bibliography workflows; the book library organizes works around reading. PDF storage overlaps; semantics differ.
- **vs File Manager**: file managers operate on files; the library operates on books. Calibre's "managed copy + metadata.db" model makes the distinction crisp: the user's original files are deliberately left untouched while the library builds a book-semantic layer over copies.
- **vs Read-it-later**: web-article capture vs book-file curation; different acquisition channel and unit.
- **Audiobooks**: present inside sampled libraries as items; an audiobook-first product would likely be its own type (no nearby directory leaf; noted, not escalated).

### "Remove X → another Type" judgments

- Remove the persistent collection → E-book Reader / PDF-Document Reader (open-and-read viewer).
- Remove book semantics (identity/metadata/organization) → File Manager.
- Remove read access (no reader, no handoff, no delivery) → bibliographic catalog / database, not a working library.
- Remove local-file reality and keep only tracking (no files) → Reading Library Application (tracker).

## Uncertainties

- Apple Books metadata editing, dedup, and storage details were not fetched (pages not visited); no claims made.
- Google Play Books, Kobo, Adobe Digital Editions unreachable — the store-first cloud shelf and device-companion poles are covered only indirectly (Apple covers store+cloud; calibre covers device transfer). Details of those poles are NOT asserted anywhere.
- Whether single-format consumer apps (e.g. pure e-reader companion apps) always carry a library layer — plausible but unverified; the Type definition does not depend on it.
- Historical samples (2000s-era library managers, e-reader companion suites) were not directly documented due to fetch failures; the historical check is supported by calibre's own long-documented file-import/metadata/shelves/transfer core being the product's original design, and by the fact that no L0 element depends on cloud/store/server/conversion.

## Taxonomy Flag (for Boundary Issues)

**E-book Library Application vs Reading Library Application vs E-book Reader**: the three leaves sit in adjacent sections (02.09 Reading vs 02.13 Personal Information Collection) with confusable names, and sampled evidence shows reading-tracker functionality (want-to-read, finished, goals, progress) shipping as a standard capability *inside* e-book libraries. Recommendation: joint review of the three leaves to confirm the tracker-alone product is the distinct Type and that E-book Reader vs E-book Library splits on center of gravity (reading surface vs collection management).

## Final Synthesis

An E-book Library Application manages a personal (optionally shared) collection of e-books as a *library*: a persistent catalog of book entries — each entry aggregating the work's file(s), metadata, and cover — organized and locatable by book attributes (collections/shelves, tags, series, search), fed by explicit acquisition (file import, folder scan, store purchase), maintained with metadata tools, and completed by read access to every entry through a built-in reader, external handoff (OS app, e-reader device), or networked delivery (server, OPDS, email, cloud sync).

The defining core is the triad: **collection of book entries + book-level organization + read access**. Conversion engines, reading-progress tracking, multi-user sharing, stores, cloud sync, DRM machinery, and content-type breadth (audiobooks, comics, PDFs) are mature or variant capabilities, not the definition. Removing the collection yields a reader; removing book semantics yields a file manager; removing read access yields a mere catalog.
