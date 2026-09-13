# Research Notes — Sheet Music Reader

Research date: 2026-09-08
Leaf: Sheet Music Reader (§04.11 Music Notation)
Slug: sheet-music-reader

## Research Goal

Understand what a Sheet Music Reader really is from real products: what the central object is, how the reading surface presents notated music, how scores are collected and organized, what performance- and practice-oriented machinery surrounds the document, and where the Type's boundaries lie (vs Music Notation Editor — the sibling leaf with a flagged forward seam — vs PDF/Document Reader, vs sheet-music stores/catalogs, vs streaming and learning products).

## Initial Boundary

- Hypothesis: the Type centers on **consuming** existing notated music — displaying scores for reading while practicing or performing, plus organizing them in a performer's library. This is the opposite relationship to the notation editor's **authoring** center (same rendered artifact, opposite relationship to it — the seam flagged by the music-notation-editor pass, to be held from this side).
- Nearest neighbors: Music Notation Editor (sibling; authoring vs consumption), PDF / Document Reader (generic document consumption vs music-specialized), E-book Reader (book-reading analog), Music Streaming Platform (audio vs notation), online sheet-music stores (acquisition vs reading), Music Production / DAW (audio deliverable).
- Unknowns at start: Is the library definitional or common? Is playback definitional? Is annotation definitional? Is page-turn machinery definitional? How do catalog-attached readers (subscription libraries) change the model? Does the interactive-practice pole stay in-type?

## Research Questions

1. What is the central persistent object, and what document forms does it take (PDF, scans, native/interactive scores)?
2. How does the reading surface present the score (display modes, page turns, zoom/crop, reading-state control)?
3. How is the score library organized (metadata, categories, search/filter, multiple libraries, setlists)?
4. How does annotation work, and how does it relate to the underlying score document?
5. Is playback (audio/MIDI/AI rendering) definitional or common, and how is it realized?
6. How do scores enter the library (import, scan, catalog download, purchase)?
7. What performance machinery exists (hands-free page turns, device sync, ensemble collaboration)?
8. What practice machinery exists (metronome, pitch tools, practice tracking, transposition)?
9. What variants exist (catalog-attached, interactive converted scores, education, cross-platform)?
10. Where are the boundaries vs Music Notation Editor, PDF reader, sheet-music stores, streaming, learning apps?

## Representative Products

| Product | Why sampled | Evidence tier reached |
|---|---|---|
| forScore | Dominant dedicated iOS/iPadOS music-stand reader; performer-centric; mature documentation (full online user guide) | Tier 1 (official site + user-guide TOC + two user-guide chapters) |
| MobileSheets | Cross-platform (Android/Windows/iOS/Mac) library-organization pole for gigging musicians; detailed feature documentation | Tier 1 (official site + features pages) |
| Newzik | Cloud/collaboration pole (app + web); ensembles, orchestras, education; interactive converted scores | Tier 1 (official site incl. FAQ; knowledge base not fetched) |
| nkoda | Catalog/subscription pole — scores licensed from publishers on subscription, individual + institutional | Tier 2 (official marketing site only; Help Centre unreachable ×2) |
| Tomplay | Intended interactive-practice sample (play-along backing tracks) | FAILED — tomplay.com returned empty ×2. No claims made. |

## Sources

- forScore — forscore.co (product overview), forscore.co/user-guides/ (guide index), forscore.co/documentation/ (forScore 15.0 user-guide table of contents), forscore.co/documentation/scores/ (Scores chapter) — fetched 2026-09-08
- MobileSheets — zubersoft.com/mobilesheets/ (product overview), zubersoft.com/mobilesheets/features/ (library features page) — fetched 2026-09-08
- Newzik — newzik.com/en (product overview incl. FAQ section) — fetched 2026-09-08; support.newzik.com knowledge base not fetched
- nkoda — nkoda.com (subscription/institution overview) — fetched 2026-09-08; intercom.help/nkoda Help Centre timed out ×2 — abandoned
- Tomplay — tomplay.com returned empty content ×2 — abandoned, product dropped from sampled set
- Sibling context: research/music-notation-editor.md (2026-09-08) — forward seam definition

## Product Observations

### forScore (evidence layer A — direct, official site + user guide)

- Positioning (direct): "turbocharge your sheet music" — "Go paperless. Get organized." "everything you can do with paper and so much more"; #1 paid music app claims (marketing tier).
- Score menu = the sheet music library (direct, Scores chapter): list sorted in multiple ways; browse by categories (Composers, Genres) **generated automatically from each score's metadata**; a single score may appear in several category lists; menu reopens to last submenu.
- Separate **Libraries** (direct): create and work with entirely separate collections of music, e.g. for different bands.
- Find & Filter (direct): search bar; filter by cross-referencing categories with include/exclude rules against categories and setlists.
- Metadata (direct): per-score metadata editor (circled info button); dedicated Metadata guide chapter.
- File management (direct): swipe to delete/share; preview; import from other apps and cloud storage; **Merging** pages from multiple PDFs into one new PDF; **Cloning** — duplicate a score without extra storage, annotate each copy uniquely, add each to its own setlist.
- Setlists, Bookmarks, Rearrange (pages), Crop, Annotation, Links & Buttons (jump-to-page), Audio, Metronome, Search, Tools, Scan, Cue, Dashboard, Page Turners & Shortcuts, Accessibility, iCloud Syncing, Backups — all present as user-guide chapters (TOC, direct).
- Annotation (direct): with Apple Pencil "annotating is as simple as drawing… just like paper, but with an undo button"; no mode activation needed.
- Playback (direct): "play along to an audio track"; Audio chapter in guide. Metronome, pitch pipe, piano keyboard tool, practice-time tracking with goals (direct, "And So Much More").
- Page turning (direct): page turning devices, MIDI signals, built-in remote control system to **wirelessly synchronize page turns with nearby devices**; adaptive caching so page turns are "virtually instantaneous".
- Reflow (direct): transforms standard PDF pages into easily readable content on small screens ("a horizontal teleprompter for sheet music") — iPhone experience.
- Acquisition (direct): save PDFs from the web, import from cloud storage providers, **download purchases from popular retailers** (Musicnotes integration page), iCloud sync across devices.
- Platforms (direct): iOS/iPadOS/macOS/visionOS, universal purchase; forScore Pro subscription exists; education page; sheet-music providers and page-turner accessory listings.

### MobileSheets (evidence layer A — direct, official site + features page)

- Positioning (direct): "Get rid of your books and binders and experience the freedom of going digital" — "designed to meet the needs of performing musicians and hobbyists alike, with a focus on reliability and functionality."
- Library management (direct): "at the core of MobileSheets is a SQLite database that allows for libraries to grow to any size"; data cached for fast viewing/editing/searching; **over 20 fields** (artists, albums, composers, genres + renamable custom field); multiple sorting algorithms; configurable formatting; fast filtering; voice search; "Find and load any song in seconds".
- Multiple libraries (direct): "Create separate libraries per band or event"; switching in a few taps.
- Setlists (direct): "Build a list of scores and page through them seamlessly… perform with seamless transitions between files"; setlist editor to add/remove/rearrange; merge/delete setlists.
- Bookmarks (direct): bookmark pages for quicker access; window shows in-app bookmarks **and native PDF bookmarks**; library-wide bookmark tab.
- Display (direct): switch display modes — horizontal scrolling, vertical scrolling, half pages in portrait, two pages at a time; select how pages stretch to fill the screen.
- Annotation (direct): multiple layers, accurate stylus drawing, highlight passages, place stamps, add lyrics or notes.
- Hands-free (direct): Bluetooth pedal page turns and actions; automatic scrolling through scores and setlists.
- Pairing/collaboration (direct): connect multiple tablets over WiFi/Bluetooth with one controlling the others; **synchronize libraries over WiFi or cloud** distributing changes "without overwriting each musician's annotations"; book mode pairs two tablets for two-page display (turn one page, two pages, or alternate).
- MIDI (direct): connect MIDI instruments to synchronize loading of keyboard registrations and scores; trigger actions with MIDI messages.
- Import (direct): integrated file browser for Dropbox/Google Drive/OneDrive; standard file picker for other services.
- Utilities (direct): audio player, metronome, configurable buttons, **link points** to jump to pages.
- Platforms (direct): Android, iOS/macOS, Windows; trial version; store installs vs license-key-per-device channel; e-Ink Android variant; manual, FAQ, forums, tutorial videos.

### Newzik (evidence layer A — direct, official site incl. FAQ)

- Positioning (direct): "The score management and playback app that revolutionizes your musical practice, whether alone or with others." Users: musicians, ensembles, schools; institutional logos (opera houses, orchestras) displayed; vendor-stated scale figures (450k users, 14M scores) — marketing tier.
- Manage your parts (direct): centralize digital sheet music (**PDFs, scans, sets**); "Classification, setlists, and versions give you complete control over your library."
- Cloud library (direct): "All your music, everywhere. Setlists and versions always synchronized."
- Annotate & turn pages (direct): highlight, add **fingerings and markers**; turn pages hands-free using **facial movements** or a Bluetooth pedal.
- Playback (direct): "musical AI that reads it for you" — listen to your sheet music; MIDI accompaniment with a mixer to isolate instruments; playback bar with **cursor following the score** (guided reading).
- LiveScore (direct): OMR conversion of PDFs/scans into **interactive scores**; after conversion: follow along with cursor, navigate by section, **transpose** (key/clef), **export MusicXML/MIDI** "to continue editing wherever you want".
- Projects / collaboration (direct): create project, add scores, invite musicians/students; content **and annotations sync in real time** for all members "depending on access rights"; aimed at students/teachers, chamber musicians, orchestras.
- Formats (direct): PDF, MusicXML, MIDI accepted; transposition linked to LiveScores.
- Offline (direct): downloaded sheet music works offline; cloud library, LiveScores, and synchronization require connection.
- Tiers (direct): free version (3 scores import, 10 LiveScore pages); Essentials (1,000-song cloud storage, 1 collaborative project, web access); Premium (unlimited, MusicXML/MIDI export, transposition, facial page turns); monthly/annual/lifetime options.
- Surfaces (direct): iOS app, web platform (library, annotations, LiveScore in browser).

### nkoda (evidence layer B — official marketing site only; help center unreachable)

- Positioning (direct): "Digital sheet music app. Licensed from publishers. All on subscription." 7-day free trial.
- Catalog (direct): publisher logos displayed (Bärenreiter, Boosey & Hawkes, Breitkopf & Härtel, Chester, Doblinger, Faber, Novello, Ricordi, Schott); "Simple access to 100k+ titles. Scores, performance and education materials." (vendor-stated figure)
- Institutional plans (direct): "Plans for conservatoires, universities, schools and performing institutions"; institution logos (conservatoires, orchestras incl. London Symphony Orchestra, La Phil, Boston Symphony).
- Developer ecosystem (direct): "Our app is open to developers… Build the tools that musicians need."
- Operational reader behavior (import, annotation, page-turn, display modes) could NOT be verified — Help Centre unreachable. No operational claims are made for nkoda anywhere in this research. Its evidentiary role is the catalog-acquisition posture: scores acquired from a licensed subscription catalog rather than imported by the user.

### Tomplay — unreachable

- tomplay.com returned empty content twice. No claims made. The interactive-practice orientation (play-along backing tracks) is represented in the sample only indirectly, via Newzik's playback/MIDI-accompaniment features.

## Cross-product Comparison

| Dimension | forScore | MobileSheets | Newzik | nkoda |
|---|---|---|---|---|
| Score as persistent displayable unit | Yes (PDF-based files) | Yes (files) | Yes (PDF, MusicXML, MIDI; scans) | Yes (catalog editions; form not verified) |
| Score-reading surface with page control | Yes (page turns, Rearrange, Crop, Reflow) | Yes (display modes, scrolling, two-page, book mode) | Yes (page turns incl. gestures, cursor-guided reading) | Unverified |
| Organized personal/ensemble library | Yes (auto-categories, metadata editor, filters, separate libraries) | Yes (20+ fields, sorting, filtering, multiple libraries, SQLite core) | Yes (cloud library, classification, versions, projects) | Yes (catalog as the library; mechanics unverified) |
| Setlists | Yes (dedicated chapter; clone-to-setlist) | Yes (setlist editor, seamless paging) | Yes (shared setlists) | Not observed |
| Annotation | Yes (Pencil ink, undo) | Yes (layers, stylus, highlight, stamps, text) | Yes (highlight, fingerings, markers, synced) | Unverified |
| Hands-free page turning | Yes (pedals, MIDI, device-to-device remote sync) | Yes (pedals, auto-scroll, tablet pairing) | Yes (pedal, facial movements) | Unverified |
| Bookmarks / link points | Yes (Bookmarks, Links & Buttons chapters) | Yes (in-app + native PDF bookmarks, link points) | Yes (bookmarks to jump pages — testimonial-tier; sections in LiveScore) | Not observed |
| Import from files/cloud/web | Yes (cloud providers, web, retailer downloads) | Yes (Dropbox/Drive/OneDrive, file picker) | Yes (Files app, share sheet, built-in scanner) | No (catalog-sourced) |
| OMR scan conversion | Yes (Scan chapter) | Not observed on fetched pages | Yes (OMR → LiveScore) | Not observed |
| Playback adjunct | Yes (audio-track play-along) | Yes (audio player, metronome) | Yes (AI audio rendering, MIDI accompaniment + mixer, cursor) | Not observed |
| Transposition / notation-aware operations | Not observed | Not observed | Yes (LiveScore transposition; MusicXML/MIDI export) | Not observed |
| Ensemble collaboration | Yes (wireless page-turn sync between devices) | Yes (multi-tablet control, library sync preserving annotations) | Yes (real-time shared projects, annotation sync, access rights) | Not observed |
| Cloud/account sync | Yes (iCloud) | Yes (cloud library sync) | Yes (account-based cloud, cross-device) | Yes (subscription account; details unverified) |
| Catalog acquisition | Retailer download integration (purchase elsewhere, import) | No | No | Yes (subscription catalog licensed from publishers) |
| Education packaging | Yes (education page) | Not observed | Yes (Education product line) | Yes (schools/institutions) |
| Platform posture | Apple-only (iOS/iPadOS/macOS/visionOS) | Cross-platform (Android/iOS/Mac/Windows, e-Ink) | iOS app + web | App; platforms not verified |

## Abstraction Hierarchy

### L0 — Defining Invariant (deliberately minimal)

Three jointly-held structures. Remove any one and the product stops being recognizable as a Sheet Music Reader:

1. **The score as the unit of record** — a persistent, identified, displayable document of one piece of notated music held in the application (imported file, scanned set, converted/interactive score, or catalog edition), carrying identity and typically metadata. Remove → a folder of files, no artifact for the reader to operate on.
2. **The score-reading presentation surface** — the score displayed for human music-reading, organized around the music's own pagination/structure, with direct control of reading state: page position and turning, display arrangement (single page, spread, scrolling, zoom), reading optimized for use while playing or practicing. Remove → a metadata catalog or file manager that lists music but doesn't present it for reading.
3. **The performer's score library** — the collected scores of a person or ensemble stored, organized, and retrieved for use (metadata organization, search/filter, and in performance contexts ordered programs of pieces), under a user or shared-group identity. Remove → a one-off viewer with no collection.

Plus the consumption posture that defines the Type's relationship to its artifact: the application **operates on existing scores** — presenting, marking up, playing, and organizing them. Authoring the notation itself (creating/changing musical semantics) is not its center; where notation-aware operations appear (conversion, transposition), they act on the stored document or a derived copy, not as in-place music-semantic authoring.

Jointly-held load-bearing checks:

- (1) alone = a score file collection (a folder of PDFs).
- (2) without (1) = a generic document viewer.
- (3) without (2) = a music-file/metadata manager with no reading surface.
- (1)+(3) without (2) = a sheet-music catalog or download manager.
- (2)+(3) without (1) = nothing to read — incoherent.
- Add authoring as the center → Music Notation Editor territory.

Historical / market-sample check: a **music folder or binder of paper scores on a stand, with a pencil and a setlist sheet** satisfies all three structures with zero software features; a 2000s laptop PDF reader driven by a foot pedal satisfies them with no annotation layers, no playback, no cloud, no catalog, and no native formats. Therefore the definition names no tablet, no PDF, no annotation, no playback, no page-turn hardware, no cloud, no setlist object, no catalog. All of these are realizations or common capabilities layered on the core.

### L1 — Common Mature Structure (standard capabilities, not definitional)

- **Metadata-driven library organization** — composer/genre/instrument-style fields, auto-generated category browsing, search/filter, multiple named libraries (forScore, MobileSheets strongly; Newzik classification).
- **Setlists** — ordered programs of scores for a performance, paged through seamlessly; all three operationally-sampled products document them.
- **Annotation on the score** — ink/stylus drawing, highlighting, stamps, text/fingerings; held as a layer over the document distinct from the score itself (undo; per-copy independence: forScore cloning, MobileSheets sync "without overwriting each musician's annotations").
- **Hands-free page turning** — Bluetooth pedals, MIDI triggers, automatic scrolling, and device-to-device page-turn synchronization (forScore remote sync, MobileSheets pairing/control, Newzik pedal + facial gestures).
- **Display-mode control** — two-page spread, half-page, horizontal/vertical scrolling, page stretching (MobileSheets explicit; forScore crop/rearrange/Reflow adjacent evidence).
- **Bookmarks and jump points** — in-app bookmarks, native PDF bookmarks, link points/buttons to jump within or between scores (forScore, MobileSheets; Newzik sections/bookmarks).
- **Acquisition machinery** — import from cloud storage/file system/web, built-in scanning of paper scores (forScore, Newzik, MobileSheets).
- **Playback adjuncts** — attaching or playing audio alongside the score (forScore play-along, MobileSheets audio player) or rendering the score audibly (Newzik AI reading, MIDI accompaniment); metronome (forScore, MobileSheets).
- **Practice utilities** — metronome, pitch pipe/tuning reference, practice-time tracking with goals (forScore documents these directly).

### L2 — Variant / Optional Structure

- **Catalog-attached subscription reader** — the library is populated from a publisher-licensed catalog rather than user imports (nkoda; also the retail-download integration in forScore points the same direction from the opposite side). Individual vs institutional licensing (nkoda conservatoire/orchestra plans).
- **Interactive/converted scores** — OMR conversion of PDFs/scans into notation-aware documents enabling cursor-guided reading, section navigation, transposition, and MusicXML/MIDI export (Newzik LiveScore). This is a bridge capability toward the notation-editor territory, executed on converted copies.
- **Ensemble/orchestral collaboration** — shared projects with real-time annotation sync and access rights (Newzik), multi-tablet control and annotation-preserving library distribution (MobileSheets), wireless page-turn sync for duos (forScore).
- **Cross-platform vs single-platform posture** — Apple-only polish pole (forScore) vs cross-platform/e-Ink pole (MobileSheets) vs app+web cloud pole (Newzik).
- **Education packaging** — dedicated education programs/pages (forScore education, Newzik Education, nkoda school grants).
- **Chord/lyrics-oriented documents** — lyrics-and-chords support appears in sampled products (Newzik tiers); chord-chart-first gigging products exist as an adjacent orientation (not sampled).
- **Practice-time gamification** (forScore Dashboard/goals) — practice-support variant.

### L3 — Vendor-specific (research notes only)

- forScore: Reflow teleprompter technology, adaptive caching, cloning (storage-sharing duplicates), Cue, Dashboard, pitch pipe + piano keyboard tools, forScore Pro subscription, Musicnotes retailer integration, universal Apple purchase, visionOS support.
- MobileSheets: SQLite-core library claim, e-Ink device variant, license-key-per-device sales channel + trial version, companion app, configurable buttons, MIDI keyboard-registration syncing.
- Newzik: LiveScore AI/OMR conversion, facial-movement page turns, version system ("versions give you complete control"), transposition-after-conversion model, project access rights, lifetime/annual/monthly tiering, vendor-stated scale figures (450k users / 14M scores — marketing tier).
- nkoda: publisher roster, "Made, not born" school grant fund, developer partnership program, 7-day trial, institution trials; reader mechanics unverified.
- Tomplay: no claims (unreachable).

## Vendor-specific Findings

All L3 items above stay out of the canonical document. The only marketing figures encountered (user counts, score counts, title counts) are vendor-stated and unverified; they are never used as structural evidence.

## Boundary Findings

1. **vs Music Notation Editor (sibling leaf, processed 2026-09-08)** — the sharpest seam, held from this side as that pass requested: same rendered artifact, opposite relationship to it. The editor's defining act is *changing* the score (music-semantic editing, re-rendering as content changes); the reader's defining act is *consuming* it (display, page-turning, annotation, playback, organization of existing scores). The seam is center-of-gravity, not feature presence: sampled notation editors include playback and reading of scores, and sampled readers include notation-adjacent operations (Newzik transposes and exports MusicXML after OMR conversion; forScore merges/rearranges pages). The discriminator: do notation-aware changes happen as **authoring of musical semantics on the score**, or as **operations on the stored document or a converted copy** while the score remains an artifact to be read? Remove consumption posture and put editing at the center → Music Notation Editor.
2. **vs PDF / Document Reader (§02.09)** — a generic document reader can display a score PDF; that does not make it this Type. The sheet-music reader is specialized for music-reading: a library organized for performing (composers/genres/setlists rather than folders), page-turn machinery designed for hands-busy musicians, annotation shaped like pencil marks on music, score-aware playback. Remove the music-specialized machinery → generic document reader.
3. **vs E-book Reader (§02.09)** — the same consumption-vs-consumption boundary by domain: book-reading machinery (chapters, reading progress, typography for text) vs score-reading machinery (measures/pagination of music, page turns for performance, musical annotation). The domain specializations are the Type's substance.
4. **vs online sheet-music stores / catalogs** — acquisition vs reading. Stores (e.g., the retailers forScore integrates with) sell and deliver files; the reader's unit of record is the score held for use. nkoda shows the two can be fused (catalog + reader in one subscription app) — with the reader core still present; a catalog without a reading surface is a store, not this Type.
5. **vs Music Streaming Platform (§27)** — recorded-audio catalog playback vs notated-music documents for reading. Even when a reader renders audio (Newzik), the audio is derived from/aligned to the held score, not a licensed recording catalog.
6. **vs music-learning applications** — where the score becomes subservient to a lesson/curriculum (progression, exercises, feedback), the product drifts to learning territory. Tomplay (unreachable) anchors this orientation in the market; no claims are made. Newzik stays in-type because the score and its library remain the center.
7. **Historical/genere note** — chord-chart/lead-sheet readers (gigging orientation) keep the same core with a different document genre; held as variant, with Newzik's lyrics-and-chords support as in-sample corroboration.

## Uncertainties

- nkoda's operational reader behavior (import, annotation, page turns, display) is unverified — Help Centre timed out twice; all nkoda observations are marketing-tier (positioning, catalog, institutions). Its role in the sample is the catalog-acquisition posture only.
- Tomplay unreachable (×2) — the interactive-practice pole is under-sampled; that orientation is described only as a market variant without product claims.
- forScore display modes (two-page/half-page) were not directly documented in the fetched pages (MobileSheets was); forScore's display claims are limited to what its guide TOC/chapters show (page turns, crop, rearrange, Reflow).
- Whether score-rendered playback with a synchronized cursor is common across the market cannot be confirmed beyond Newzik (and notation-editor evidence from the sibling pass); it is held as common-to-optional, never definitional.
- Newzik bookmark behavior is partially testimonial-tier (user review) alongside direct FAQ evidence; kept calibrated.
- Vendor-stated figures (450k users, 14M scores, 100k+ titles) are marketing claims, not verified.

## Final Synthesis

A Sheet Music Reader is a performer-facing **consumption** application for notated music whose defining core is exactly three jointly-held structures: the **score as the unit of record** (a persistent, identified, displayable document of one piece of notated music — imported, scanned, converted, or catalog-acquired), the **score-reading presentation surface** (the music displayed for human reading, organized around its own pagination, with direct control of reading state — page position, turning, display arrangement), and the **performer's score library** (the person's or ensemble's collected scores stored, organized, and retrieved for practice and performance, commonly through metadata, search, and setlists). The Type's posture is operating on existing scores rather than authoring notation — that posture is the seam with the Music Notation Editor. Everything commonly associated — annotation layers, hands-free page turns, playback, metronome/practice tools, cloud sync, ensemble collaboration, OMR conversion, subscription catalogs, education packaging — is standard capability or variant, not definition. A music binder on a stand with a pencil and a setlist sheet satisfies the core with no software; a laptop PDF reader with a foot pedal satisfies it with none of the modern machinery.
