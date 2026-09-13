# Research Notes — E-book Reader

Research date: 2026-09-07
Methodology: v1.1 (update-v1/)

## Research Goal

Understand what an E-book Reader is as an Application Type: what the unit of work is, how book content is presented, what reading-position state exists, what navigation and reading-comfort machinery is standard, what in-reading interaction looks like, where position/annotation state lives, and where the boundaries run against the E-book Library Application (processed sibling), PDF / Document Reader, Read-it-later Application, Reading Library Application, and generic file/text viewers.

This pass must also discharge the reader-side half of the boundary flag raised by the e-book-library-application pass (§Boundary Issues in STATUS.md), using the working discriminators that pass adopted: E-book Library = collection management is the center of gravity; E-book Reader = the reading surface for one opened book.

## Initial Boundary (working hypothesis before research)

- Hypothesized core: an application that opens one digital book and presents it for sustained reading — paginated or flowing — while remembering the reader's position in each book.
- Suspected confusions: E-book Library Application (collection management around the reader), PDF / Document Reader (fixed-layout documents of any kind), Read-it-later (articles, not books), Reading Library Application (tracker without files), plain text/file viewers.
- Open question: which of {typography controls, annotations, store acquisition, cloud sync, DRM, TOC} are definitional vs merely common. Initial assumption: none of store/cloud/DRM/annotations are definitional; typography and TOC likely common-but-maybe-not-definitional.

## Research Questions

1. What is the unit of the reader's world — the file, the book, the reading session?
2. How is book content presented (pagination vs scroll; reflowable vs fixed layout)?
3. What reading-position state exists (per-book resume, continue-reading surfaces, progress indicators)?
4. What navigation machinery exists (page turns, TOC, progress jumps, bookmarks, back trails)?
5. What reading-comfort controls exist (typography, themes, brightness, layout)?
6. What in-reading interactions exist (select → highlight/note/lookup/translate/search/share)?
7. What is the structural role of the reflowable-vs-fixed-layout distinction?
8. Where does the entry/bookshelf surface sit in reader products, and is it definitional?
9. Where does position/annotation state live (local, cloud, device)?
10. What does the reader deliberately NOT do (acquisition, cataloging, curation)?
11. Do older/regional/platform-native readers satisfy the candidate core (historical check)?
12. Where exactly is the reader/library seam, and can it be discharged from this side?

## Representative Products

| Product | Philosophy / pole | Why sampled |
|---|---|---|
| Apple Books | Platform-native consumer reader (store + cloud sync + reader in one OS-integrated app) | The consumer-integrated pole; deepest Tier-1 reading-surface documentation reachable |
| KOReader | Open-source power-user reader for E Ink devices (file-based, highly configurable, device-controlling) | The enthusiast/device-embedded pole; explicit reflowable-vs-fixed machinery; runs on Kindle/Kobo/PocketBook/Android |
| Thorium Reader | Open-source accessibility-first desktop reader (EDRLab; reader-first positioning, library catalogs, LCP) | The accessibility/education pole; file-based desktop reader for heavy readers and students |

Coverage check: three philosophies (platform-native consumer / device-embedded power tool / accessibility-first desktop), three customer tiers (mainstream consumer / enthusiast / accessibility-education), three deployment surfaces (OS-integrated app / e-ink device software / desktop app). The store-first cloud-shelf pole (Google Play Books) and the device-companion retail pole (Kobo, Adobe Digital Editions) could not be reached — see Source-access Limitation. The sibling pass (e-book-library-application) provides additional cross-product context from calibre / Apple Books / Kavita documentation.

## Sources

Fetched successfully (2026-09-07):

- Apple Books User Guide for Mac (macOS Tahoe 26) — https://support.apple.com/guide/books/welcome/mac (TOC/structure, Tier 1)
- Apple Books — Read books in Books on Mac — https://support.apple.com/guide/books/read-books-ibks5f526382/mac (Tier 1)
- Apple Books — Change a book's appearance in Books on Mac — https://support.apple.com/guide/books/change-a-books-appearance-ibks8923126d/mac (Tier 1)
- KOReader — https://koreader.rocks/ (product page, Tier 1/2)
- KOReader User Guide (last update 2025-03-25) — https://koreader.rocks/user_guide (Tier 1)
- Thorium Reader — https://thorium.edrlab.org/en/ (product page, Tier 2; EDRLab, v3.4.0)

Fetched in the sibling pass (cited here as corroborating evidence):

- Apple Books — Import books, audiobooks, or PDFs ("PDFs open in Preview (or your default PDF reader), rather than in Books") — via research/e-book-library-application.md
- Calibre user manual — built-in E-book viewer described inside the library ("navigation, highlighting, read-aloud, dictionary, look & feel") — via research/e-book-library-application.md
- Kavita — built-in web readers per format (EPUB/PDF/comic) — via research/e-book-library-application.md

Unreachable (source-access limitation; abandoned after repeated failures):

- Google Play Books help — timed out ×2 in this pass (plus ×2 in the sibling pass on 2026-09-07)
- Kobo help center — not re-attempted (timed out ×2 in the sibling pass)
- Adobe Digital Editions — not re-attempted (timed out ×2 in the sibling pass)
- Thorium Reader documentation — https://thorium-web.pages.dev/... transport error, https://support.thoriumreader.com/ timed out ×2, archived GitHub doc listing timed out ×1

Consequence: Thorium evidence stays at product-page level (positioning + feature bullets; no operational procedures). Google Play Books / Kobo / Adobe Digital Editions get no product-level claims anywhere. The store-first cloud pole is covered only indirectly (Apple Books covers store + cloud sync in-sample). Cross-product claims are calibrated to three directly documented products.

## Product Observations

### Apple Books (Evidence layer A — official user guide, fetched)

Reading surface and position:

- Home surface: "Home is the place to pick up where you left off, or to start reading a new book"; "Books you're currently reading appear in the Continue section."
- Open a book by double-click from a collection; iCloud-backed items download on open ("you can double-click the book to download it from iCloud").
- Progress sync: "To sync your progress in a book across all your Apple devices … you need to set up iCloud" — position is syncable state, not just local.
- Moving around: table-of-contents button or page thumbnails at the top of the book; next/previous page by edge arrows, trackpad swipe, or keyboard arrow keys.
- Search in the book (word, phrase, or page number); "See the last page you viewed" Go Back control after a multipage jump (TOC, search results) — an explicit back-trail for jumps.
- Bookmarks: save multiple spots; bookmark toggle per page; "see all the bookmarks in a book."
- Read Aloud for books that include the feature (with page-turning options); system Speech (Edit > Speech > Start Speaking) for any book.
- Translate a text selection (Control-click > Translate).
- "Delay the display sleep settings while reading" — reading holds the screen.
- Book-internal rich content: "Interact with video, audio, and more" page exists; glossaries/definitions; study cards; highlights and notes (Learn with Books section).

Appearance controls (Change a book's appearance):

- One or two pages depending on window width (desktop layout adapts).
- Font size (A buttons, with reset), font choice, bold text.
- Page themes (Original, Quiet, Paper), theme customization, page background Light/Dark/Automatic.
- Spacing sliders (page layout and accessibility options), justify text on/off, single vs multiple columns, auto-hyphenation setting.
- Full screen for larger reading.

Library-side context (from sibling pass, same product): library sidebar with collections; Want to Read / Finished (auto-added "when you reach their end"); "PDFs open in Preview (or your default PDF reader), rather than in Books" — the reader surface is for books; PDFs are deliberately handed off. DRM: "Authorize your Mac" for protected content; some formats "can only be opened in the associated third-party app."

### KOReader (Evidence layer A — official site + user guide, fetched)

Positioning: "a document viewer for E Ink devices. Supported fileformats include EPUB, PDF, DjVu, XPS, CBT, CBZ, FB2, PDB, TXT, HTML, RTF, CHM, DOC, MOBI and ZIP"; runs on "Kindle, Kobo, PocketBook, Android and desktop Linux" (guide's name-history note adds Remarkable, Cervantes, Sony, macOS).

Getting books in (all variant machinery, no store): USB mass storage, cloud storage (Dropbox/FTP/WebDAV), built-in SSH/SFTP server, Calibre plugin, News downloader (RSS/Atom → HTML), Wallabag (read-it-later retrieval).

Entry surfaces to books (present but not the center): File Browser (with file management: copy/move/rename/delete, bulk operations, mosaic/detailed views), Favorites, History ("List of books you opened"), Collections ("Personalized book lists", filterable by book status: new / reading / finished / on hold); search History by filename or metadata; "open the last document with a gesture"; Book information popup with editable metadata fields (long-press in File Browser).

The reading screen (the center):

- Two menus: TOP MENU (Navigation: TOC, bookmarks, book map; Typesetting: fonts, style tweaks; Settings; Tools; Search) and BOTTOM MENU (document formatting: font size, contrast/weight, line spacing, margins, word spacing/expansion for justification, columns, view mode page vs continuous, render mode, zoom dpi, embedded styles/fonts on-off).
- Tap zones: predefined screen areas for page turns and menu activation; 200+-action gesture system; keyboard shortcuts; Quick Menu; Profiles (book-open state machinery: "Profiles to control every aspect").
- Status bar: highly configurable (page numbers, progress bar for book or current chapter, time, battery…); alternative top status bar.
- Reading statistics: "reading progress, time range and calendar views."

The reflowable vs fixed-layout rule (explicitly documented):

- "Document types like epub, mobi, html naturally don't have fixed page numbers because they are reflowable documents… If you increase the font size of a reflowable document, your page count will increase… this sometimes causes a problem because a highlight which you made on page 38 might be on page 42 after the font adjustment."
- "Font selection is available only on reflowable documents (EPUB, HTML, DOCX, RTF, TXT…). Fixed-layout documents like PDF/DJVU are not supported."
- Reference page numbers: publishers can embed print-edition page numbers; the reader can display those instead of computed screen pages ("matches the print version of the book").
- Partial rendering: EPUB described as "basically .zip archives that contain .html files"; chapter-level re-render for fast typography preview.
- PDF machinery (fixed-layout pole): margin crop, reflow mode, OCR for scanned books, zoom types and page-flow for multi-column documents, auto-straighten, save highlights into the PDF itself, panel zoom for manga, refresh-interval tuning.
- View mode: page mode vs "continuous mode — you can scroll the document like a web page" (with page-overlap option).

Navigation machinery: Skim widget (tap progress bar; enter page number or percentage; chapter/bookmark hopping; long-press returns to where you opened it), Book map ("bird's eye map of your book including all your notes and highlights"), Page browser ("move through pages like a film reel"), TOC tools (create an alternative TOC if the book's is poor), hidden flows (exclude appendix/index/references "for more accurate page counts"), "Go back to previous location" (browser-like back/forward across jumps and links).

Annotations: highlight styles/colors (long multi-page highlight mode), notes with customizable keyboard, export to text/markdown/HTML/JSON/Kindle clippings, sync to Joplin/Readwise/Memos/Flomo/XMNote; dictionary lookup (EPUB and scanned PDF/DJVU), Wikipedia lookup, whole-page translation (130+ languages), regex document search, search inside bookmarks/notes.

E-ink/device integration: frontlight + warmth control (auto schedules or sun-position calculation), night mode (color inversion), e-ink refresh settings, screensaver (book cover option), battery charge alarms, device self-update. Embedded styles/fonts of the book can be honored or ignored.

### Thorium Reader (Evidence layer A− — official product page; docs unreachable)

Positioning (product page, EDRLab): "Read, Select, Annotate, Classify — Perfect for heavy readers, library-goers, and students alike!" Free & open source; Windows/macOS/Linux; 20+ languages.

"Reader first" feature list:

- "Read ebooks, comics & audiobooks"
- "Adjust display to your needs"
- "Screen reader support"
- "Move through print-equivalent pages"
- "Listen via synthetic voices"
- "Add library catalogs"
- Annotations block: "Bookmark reading locations; Highlight & annotate text in EPUB; Select annotation styles; Select annotation mode; Export/import of annotations."

Version 3.4.0 notes: filtering and sorting in the library grid view and catalogs; MathML support; LCP passphrase display option; improved note handling. (LCP = EDRLab's content-protection schema for library-loan content; the passphrase mention confirms license-gated content exists in this product without further operational detail being asserted.)

Community positioning corroborates the accessibility pole (user quotes on the page: visually-impaired readers, university students).

### Cross-checks from the sibling library pass (reader embedded inside libraries)

- Calibre's built-in E-book viewer: navigation, highlighting, read-aloud, dictionary, look & feel — a reader surface inside a library product (Tier 1, sibling fetch).
- Kavita ships built-in web readers per format (EPUB reader, PDF reader, comic reader with webtoon/single/double-page modes) — same pattern.
- Apple Books reads books directly but hands PDFs to Preview.

This confirms: in the live market the reading surface usually ships *inside* a product that also carries library/store machinery — the Type question is which surface is the center of gravity, not which features exist.

## Cross-product Comparison

| Aspect | Apple Books | KOReader | Thorium Reader |
|---|---|---|---|
| Unit of work | One opened book (Home "Continue" surfaces it) | One opened document (book status: new/reading/finished/on hold) | One opened book ("Read, Select, Annotate") |
| Entry surface to books | Library sidebar + Home Continue | File Browser / History / Favorites / Collections | Library grid view + added library catalogs |
| Presentation model | Reflowable book pages; one/two-page desktop layout; themes | Page mode or continuous scroll; reflowable vs fixed-layout machinery explicit | "Reader first — adjust display to your needs"; print-equivalent pages |
| Reading position | Per-book; iCloud-syncable; Continue section | Per-book resume; status-bar progress (book/chapter); reading statistics | Bookmarks as "reading locations" |
| Navigation | TOC/thumbnails, page arrows/swipe/keys, search, Go-Back trail, bookmarks | Skim widget, Book map, Page browser, TOC tools, hidden flows, back/forward trail, bookmarks | Bookmarks (detail level not fetched) |
| Appearance controls | Font size/choice, bold, themes, light/dark, spacing, justify, columns, hyphenation | Font/size/weight/contrast, kerning, word spacing/expansion, margins, columns, view mode, embedded styles on-off, night mode, own CSS-style tweaks | "Adjust display to your needs" (detail not fetched) |
| Text interaction | Select → highlight/note/study cards, lookup (glossaries), translate, share | Select → highlight styles/notes, dictionary, Wikipedia, translate, regex search, export/sync annotations | Highlight & annotate (EPUB), styles, export/import |
| Read-aloud | Read Aloud (feature books) + system Speech | (TTS exists in product but not captured in fetched guide portion — not asserted) | "Listen via synthetic voices" |
| Position sync | iCloud across devices | Local (device); annotation sync to external note services | (not asserted) |
| Content breadth | Books + audiobooks + PDFs handed to Preview + samples | EPUB/PDF/DjVu/comics/manga/plain text/DOC/HTML… | Ebooks, comics & audiobooks |
| Acquisition | Book Store + import (embedded) | File transfer + plugins (USB/cloud/SSH/Calibre/Wallabag/news) | Library catalogs + LCP-licensed content |
| DRM/license | Authorize your Mac; third-party-app-only formats | None asserted (user's own files) | LCP passphrase flow exists |
| Device integration | Platform-native (iCloud, system Speech, display-sleep hold) | Deep e-ink control (frontlight/warmth, refresh, screensaver, battery alarms) | Desktop app; screen-reader support |
| Accessibility | Platform accessibility (detail in guide not fetched) | E-ink UI simplicity; DPI scaling; gestures | Explicit first-class pole (screen reader support; conformance program referenced) |

### Stable commonalities across the sample (B-layer)

1. The unit of work is one opened book document in a reading surface; every product's center is the reading session, even when bookshelf/store/catalog machinery surrounds it.
2. Book content is presented for sustained reading — paginated or continuously flowing — never as raw file contents or an editing surface.
3. Reading position is first-class per-book state: it survives the session (Apple: Home "Continue" + iCloud sync; KOReader: per-book resume + progress bar; Thorium: bookmarkable "reading locations").
4. Movement through the book is the primary interaction: page turns / scrolling everywhere, plus structural navigation (TOC/thumbnails, progress jumps, bookmarks) and jump-back trails.
5. Reading-comfort controls adjust the presentation (typography, themes/light-dark, spacing; brightness/frontlight on device-bound products).
6. Text interaction layer: select text → highlight/note, lookup (dictionary/Wikipedia/glossary), translate, search-in-book, share (Apple, KOReader direct; Thorium annotates with styles).
7. Every product carries some entry/bookshelf-like surface (Continue shelf, file browser/history, library grid) — but in each it is an entry layer to books, not the managed center.
8. Annotation state attaches to book locations, not absolute page numbers (KOReader documents page-number instability under reflow directly).

### Divergences (not definitional)

- Acquisition: embedded store (Apple) vs file-transfer machinery (KOReader) vs library catalogs + LCP (Thorium).
- Position/annotation sync: iCloud (Apple) vs external note-service sync (KOReader) vs not asserted (Thorium).
- Device control depth: e-ink hardware control only in the device-embedded pole.
- Accessibility depth: first-class positioning (Thorium) vs platform-inherited (Apple).
- Format breadth and fixed-layout handling depth varies (KOReader deepest: PDF reflow/OCR/crop).

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

1. **The opened book** — one digital book document loaded into a reading surface at a time; the reading session is the unit of work. The reader's world is the book being read, not the collection of books. Remove this and the product is a library/catalog (sibling Type) or a generic file surface.
2. **Reading-oriented presentation** — the book's content is laid out for sustained reading: paginated or continuously flowing text adapted to the screen (and, in fixed-layout content, scaled/cropped to it). Remove this (raw file bytes, or an editing surface) and the product is a file viewer or text editor.
3. **Persistent per-book reading position with in-book movement** — where the reader is in each book survives the session, and the primary interaction is advancing through the book (page turns / scrolling) from that position. Remove position/movement and the product is a static document renderer, not a reading application.

Notes on the L0 boundary:

- No typography controls, no TOC, no bookmarks, no annotations, no store, no cloud sync, no DRM, no TTS, no bookshelf is required. A 2000s-era desktop/PDA reader or a feature-phone TXT reader — open file, paginated presentation, remembered position, key-driven page turns — satisfies the core. Historical check passes (historical products named from general knowledge as context only; no precise claims relied on).
- "Reading position" is deliberately one concept with two faces: persistence (resume) and movement (navigation). Sequential page movement is the timeless floor; structural navigation (TOC) is common wherever the book has structure and is therefore L1.
- The entry/bookshelf surface is NOT definitional: remove it (open books purely by file/system entry) and a reader remains; this matches the sibling pass's discriminator (remove the collection → reader; remove the reading surface while keeping catalog + handoff → library).

### L1 — Common Mature Structure

- **In-book navigation machinery**: table of contents / page thumbnails, progress indicator or slider (book- and sometimes chapter-level), bookmarks (multiple, listable), jump-to-page/percentage, back-to-previous-location trails across jumps.
- **Reading-comfort controls**: typography (font family/size, weight, line spacing, margins, justification, sometimes columns and hyphenation), page themes (day/night/sepia-class), brightness/frontlight control, page-turn vs continuous scroll behavior. (Nearly universal across the type's history, but conceptually the requirement is "presentation for reading"; the control surface is its mature implementation — kept out of L0 deliberately.)
- **Text interaction layer**: select text → highlight / note / copy / search-in-book / dictionary or encyclopedia lookup / translate / share.
- **Search within the book** (words, phrases; sometimes page numbers).
- **Entry/bookshelf surface**: continue-reading shelf, recents/history, favorites, or a small grid — the common entry layer to books. Common in mature products; not defining.
- **Per-book settings memory** (appearance settings ride with the book) — documented directly at KOReader (per-book defaults mechanism) and Apple (appearance applied per opened book).
- **Read-aloud / synthetic speech** in consumer-facing readers (Apple Read Aloud/Speech; Thorium synthetic voices; KOReader TTS not asserted from fetched portion).

### L2 — Variant / Optional Structure

- **Sync of position and annotations across devices** (account/cloud-backed: iCloud-style; or device-ecosystem sync).
- **Store acquisition embedded** (buy/download in-app — store-first products).
- **DRM/license handling** (account authorization; license-gated opening; library-loan expiry; LCP-class license flows).
- **Fixed-layout content support** (PDF, comics/manga with panel zoom and webtoon-style modes; fixed-layout EPUB) — with the accompanying machinery (zoom/crop/reflow/OCR) being the fixed-layout pole's specialty.
- **Content breadth**: audiobooks bundled, plain-text/markdown, papers.
- **Device integration depth**: e-ink frontlight/warmth/refresh control, screensaver from book cover, hardware-button/tap-zone bindings.
- **Accessibility depth**: screen-reader support, dyslexia-friendly options, keyboard-driven navigation, conformance programs (accessibility-first pole).
- **Annotation portability**: export (text/markdown/HTML/JSON/clippings), sync to external note systems, write-back into documents (KOReader's save-into-PDF).
- **Reading statistics and status** (progress, time, calendar views; book status new/reading/finished/on hold).
- **Print-equivalent page mapping** (publisher-embedded print page numbers displayed instead of computed pages).
- **Power-user extensibility**: custom fonts/CSS style tweaks, alternative TOC construction, hidden content flows, gesture/shortcut systems, plugin ecosystems.
- **OCR** for scanned books (fixed-layout pole).

### L3 — Vendor-specific (research notes only)

- Apple Books: Home/Continue surface; page themes Original/Quiet/Paper with per-theme customization; study cards; book glossaries; Read Aloud with page-turning options; "Extend by 10 minutes while reading" display-sleep setting; x-help-action deep links; Authorize-your-Mac DRM flow; PDFs deliberately open in Preview instead.
- KOReader: name/heritage (Kindle/Kobo Open Reader); tap zones with tri-segmented top-edge behavior; 200+-action gesture manager; Quick Menu; Profiles with auto-execution; partial rendering pipeline (EPUB = zip of HTML fragments; idle-triggered full re-render); Book map; Skim widget; Page browser; hidden flows; reference page numbers with margin labels; style tweaks; user patches (core behavior changes); SSH/SFTP server; Calibre plugin; Wallabag/News plugins; ChatGPT discussion plugin; frontlight auto-warmth by sun position/coordinates/altitude; screensaver options; battery charge alarms; regex search; whole-page translation 130+ languages; highlights-into-PDF write-back; book-status filter vocabulary (new/reading/finished/on hold).
- Thorium: EDRLab provenance; LCP passphrase display option; annotation export/import; library catalogs added to the reader; conformance/VPAT program (repo-archived docs note); documentation distributed as EPUB read in Thorium itself.

## Vendor-specific Findings

- Auto-detection of "finished" reading state (auto-shelving on reaching the end) is documented in the library-side sample (Apple Books default Finished collection) — a library/tracker capability, not a reader capability. KOReader exposes book status as manual/filter metadata.
- The reader↔device coupling (frontlight, refresh tuning, screensaver) is a device-embedded-pole specialty (KOReader direct). Platform-native products inherit platform behaviors instead (display-sleep hold documented at Apple).
- Print-equivalent page numbers appear in two independent products (KOReader "reference page numbers"; Thorium "print-equivalent pages") — a real cross-product concept, but maturity varies; kept at L2.
- Annotation sync targets differ structurally (device cloud vs external note services); no universal mechanism exists.

## Boundary Findings

- **vs E-book Library Application** (processed sibling): the reader's center of gravity is the reading session for one opened book; the library's is the collection (acquire, organize, locate, maintain, deliver). Products straddle — all sampled readers carry entry/bookshelf surfaces, and the sibling sample shows every sampled library embedding a reader. Discharge from this side using the sibling's adopted removal tests: remove the collection → a reader remains (KOReader opens by file browser/history; a single-book reader is still a reader); remove the reading surface while keeping catalog + handoff → still a library (calibre's view/handoff floor). **The reader/library pair stands as two Types with a declared straddle zone.** The remaining unresolved leaf in the three-leaf flag is Reading Library Application (tracker without files) — left to its own pass.
- **vs PDF / Document Reader**: the document reader renders fixed-layout pages of arbitrary documents faithfully; the e-book reader treats the file as a book — book-semantic position (resume, chapters), reading-comfort re-layout of reflowable text, print-page mapping. The boundary is the presentation semantics, not file formats: sampled readers DO open PDFs (KOReader's PDF machinery is deep; Apple hands PDFs to Preview instead — both poles documented). Rule of thumb: when fixed-layout page rendering of arbitrary documents is the center → PDF/Document Reader; when book-reading semantics (position life + comfort re-layout of long-form text) is the center → this Type. Readers commonly support PDF as a content-breadth variant.
- **vs Read-it-later Application**: read-it-later captures web articles and presents them in a reader-mode surface; unit = clipped article, acquisition = clipping, no book structure. KOReader's Wallabag plugin shows the systems interlock (read-it-later delivers articles INTO a reader surface) — delivery relationship, not identity.
- **vs Reading Library Application** (§02.13, unprocessed): tracker products record reading activity/wishlists and may hold no book files and no reading surface. Reader-side reading statistics (KOReader) and status labels are book-level byproducts of reading, not the managed object; the tracker's object is the reading record itself. Flag maintained for the sibling pass's joint review.
- **vs Academic Paper Reader**: papers-not-books as the unit, paper-centric annotation/organization; overlap only in machinery (highlights on long-form text).
- **vs Digital Library Platform** (§23): institutional lending/circulation platform; the reader is the consumer-facing consumption surface that licensed content eventually reaches (Thorium's library catalogs + LCP illustrate the interlock).
- **vs Text editors / file viewers**: editors hold an editing surface and file semantics; readers hold a reading surface and book-reading semantics (position life, comfort presentation). The same plain-text file straddles both worlds; KOReader's file browser + reading screen split shows the seam inside one product.
- **Audiobooks**: bundled as content breadth in several readers (Apple, Thorium); an audiobook-first product is a different surface (audio timeline, not pages) — no directory leaf; noted, not escalated.

### "Remove X → another Type" judgments

- Remove the opened-book session (world = collection) → E-book Library Application.
- Remove reading-oriented presentation (raw bytes / editing) → file viewer / text editor.
- Remove position persistence + movement → static document renderer (drifts toward PDF/Document Reader pole).
- Remove the book unit but keep the reading surface + clipping acquisition → Read-it-later Application.
- Remove files AND the reading surface, keep the reading record → Reading Library Application.

## Uncertainties

- Google Play Books, Kobo, Adobe Digital Editions unreachable — the store-first cloud-shelf pole and the retail device-companion pole are evidenced only indirectly (Apple Books carries store + cloud in-sample). No claims about those products' internals are made anywhere.
- Thorium documentation unreachable — Thorium evidence is product-page level; its operational details (catalog mechanics, annotation model, display options) are not asserted.
- KOReader TTS exists in the product historically but was not captured in the fetched guide portion; not asserted.
- Whether every reader in the market persists position per book: the sample says yes and the historical floor assumes it, but a pathological counter-product cannot be excluded; the definition treats position as the defining state regardless.
- Historical samples (2000s-era readers, feature-phone readers) were not directly documented due to fetch constraints; the historical check rests on the L0 being deliberately free of store/cloud/annotation/DRM/typography requirements plus coarse, well-established product knowledge (used as context only, no precise claims).

## Taxonomy Flag (for Boundary Issues)

Discharge (from this side) of the e-book-library-application pass's reader/library flag: the adopted working discriminators hold with direct reader-side evidence; E-book Reader and E-book Library Application stand as separate Types with a declared straddle zone (store-first products embed both; entry surfaces exist on both sides). The three-leaf joint review remains open only for Reading Library Application (tracker leaf, §02.13, unprocessed).

## Final Synthesis

An E-book Reader is the application that turns a digital book file into a reading experience: it opens one book at a time, presents its content for sustained reading (paginated or flowing, adapted to the screen), keeps the reading position per book across sessions, and moves the reader through the book — with in-book navigation, reading-comfort controls, and a text-interaction layer as the mature machinery around that core.

The defining core is the triad: **opened book + reading-oriented presentation + persistent per-book reading position with in-book movement**. Typography controls, TOC, bookmarks, annotations, search, read-aloud, and the continue-reading shelf are standard capabilities that make the core practical; store acquisition, cloud sync, DRM handling, device integration, fixed-layout/comics machinery, reading statistics, annotation portability, and print-page mapping are variants that depend on segment and business model. Collection management belongs to the sibling E-book Library Application Type; the reader's world is the book in hand.
