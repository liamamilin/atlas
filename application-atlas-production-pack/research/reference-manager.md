# Research Notes — Reference Manager

Research date: 2026-09-09

## Research Goal

Understand what a Reference Manager is as an Application Type: what the central object ("a reference") is, how references enter the library, how the library is organized, how the library feeds formatted citations and bibliographies into the user's written work, what role attachments/reading play, and how the Type is bounded against Academic Paper Reader, Academic Search Engine, PDF / Document Reader, Bookmark Manager, Note-taking/PKM, and Integrated Library System.

This pass also carries a pre-hung joint-review flag from the academic-paper-reader pass (2026-09-06): "the paper-reading surface is overwhelmingly implemented as a capability inside reference-management products… probable Capability/center-of-gravity relationship rather than two fully independent structures; the split is reading-and-annotation vs citation-database-and-bibliography; flagged for joint review when Reference Manager is processed." Discharged below (§Boundary Findings).

## Initial Boundary

Initial hypothesis (pre-research): the Type centers on a personal (or shared) database of bibliographic records plus the machinery that turns those records into correctly formatted citations and bibliographies inside a manuscript. The closest confusions:

- **Academic Paper Reader** — modern reference managers embed PDF readers; reading is one capability among several.
- **Academic Search Engine** — discovery over a corpus vs holding one's own library of records.
- **PDF / Document Reader** — rendering surface vs the surrounding bibliographic object model.
- **Bookmark Manager** — URL-based page saving without bibliographic identity or citation output.
- **Integrated Library System** — institutional holdings catalog vs a researcher's personal working library.

## Research Questions

1. What is a reference record — which fields, which item types, what does it hold beyond metadata?
2. How do references enter the library (capture paths, identifier lookup, file import, manual entry)?
3. How is the library organized (collections/folders, tags, search, duplicates)?
4. How does the cite-and-format loop work (word-processor integration, citation insertion, bibliography generation, style switching, refresh/unlink semantics)?
5. What are citation styles and how are they handled (style sets, custom styles, CSL vs vendor formats)?
6. What role do attachments (PDFs), reading, notes, and knowledge-organization features play — definitional or capability?
7. What about sync, sharing, groups?
8. What is the boundary against Academic Paper Reader (joint review), Academic Search Engine, Bookmark Manager, PDF Reader, ILS?
9. Would older products (1980s–2000s bibliography tools: EndNote's early generations, RefWorks, ProCite, the product literally named "Reference Manager") still fit the definition?

## Representative Products

Selection logic: market representation + documentation quality + different product philosophies + different customer layers.

| Product | Philosophy | Customer layer | Evidence level reached |
|---|---|---|---|
| **Zotero** (Digital Scholar, nonprofit, open source) | Free, library-first, community-developed; local app + optional sync | Individual researchers/students; free + paid storage | A — full Tier-1 documentation pages fetched (Quick Start Guide; Word plugin usage) |
| **EndNote** (Clarivate) | Commercial incumbent, desktop-first, institutional site licenses; 30+ year lineage | Individuals, universities/libraries, enterprise/government | A− — product page + product-details + official Help Guide title page fetched; feature-level evidence |
| **Paperpile** | Web-native, Google-ecosystem-coupled (Chrome sign-up, Drive storage, Google Docs citation) | Individual academics; institutional plans exist | A− — features overview + Google Docs citation feature page fetched |
| **Citavi** (Lumivero) | Project-based reference + knowledge organization (quotations, categories, tasks); European heritage, 30+ years | Individuals/small teams; universities; on-premise DBServer for institutions | A− — product page with detailed FAQ fetched |
| **Mendeley** (Elsevier) | Free publisher-suite reference manager | Individual academics (free) / institutions | C — positioning/nav only; guide body JS-rendered, fetch failed (consistent with academic-paper-reader pass's 3 failures); no operational claims drawn |

## Sources

- Zotero — Quick Start Guide: https://www.zotero.org/support/quick_start_guide (fetched 2026-09-09; last updated 2024-08-16)
- Zotero — Using the Zotero Word Plugin: https://www.zotero.org/support/word_processor_plugin_usage (fetched 2026-09-09; last updated 2026-05-14)
- EndNote — product page: https://endnote.com/ (fetched 2026-09-09)
- EndNote — product details: https://endnote.com/product-details/ (fetched 2026-09-09)
- EndNote — official Help Guide (title page): https://docs.endnote.com/docs/endnote/2025/v1/windows/en/content/01intro/title_page.htm (fetched 2026-09-09; title page only)
- Paperpile — Features overview: https://paperpile.com/features/ (fetched 2026-09-09)
- Paperpile — Citations and bibliographies for Google Docs: https://paperpile.com/features/google-docs-citations-bibliography/ (fetched 2026-09-09)
- Citavi (Lumivero) — product page incl. FAQ: https://www.citavi.com/en (fetched 2026-09-09)
- Mendeley — https://www.mendeley.com/guides/mendeley-reference-manager/ (fetched 2026-09-09; body not renderable — nav/footer only; degraded to positioning)
- Prior-pass context: research/academic-paper-reader.md (2026-09-06) — Zotero/ReadCube/Paperpile/Mendeley reader observations, reused only as cross-pass corroboration, not as new claims

## Product Observations

### Zotero — key observations (Evidence: A, official docs)

- **Self-definition**: "Zotero is, at the most basic level, a reference manager. It is designed to store, manage, and cite bibliographic references, such as books and articles. In Zotero, each of these references constitutes an item."
- **Item = typed metadata record**: "Every item contains different metadata, depending on what type it is. Items can be everything from books, articles, and reports to web pages, artwork, films, letters, manuscripts, sound recordings, bills, cases, or statutes." Right pane shows "titles, creators, publishers, dates, page numbers, and any other data needed to cite the item."
- **Library organization**: left pane = My Library + collections. Collections are aliases, not moves: "Think of collections like playlists in a music player: items in collections are aliases (or 'links') to a single copy of the item in your library. The same item can belong to many collections at one time." Tags (colored tags supported), quick/advanced search, saved searches that "update with new matching items automatically."
- **Attachments & notes as children**: "Items can have notes, files, and links attached to them"; any file type; web pages as links or local snapshots; standalone notes also possible.
- **Acquisition paths**: browser Connector with site "translators" ("automatically create an item of the appropriate type and populate the metadata fields, download a full-text PDF if available, and attach useful links… or Supplemental Data files"); single or multiple capture; Add Item by Identifier (ISBN, DOI, PubMed ID; batch paste supported); RSS feeds; manual entry as last resort ("While you should generally not add items manually").
- **Cite loop (Word plugin)**: Zotero tab in Word with Add/Edit Citation, Add/Edit Bibliography, Document Preferences, Refresh, Unlink Citations. Citation dialog searches the library ("Start typing part of a title, the last names of one or more authors, and/or a year"); cited items listed under "Cited"; multiple items per citation; locators (page default; volume etc.); prefix/suffix; "Omit Author" for narrative citations; automatic sort per style. Bibliography auto-updates from cited items; manual bibliography edits are overwritten on refresh; uncited items can be added via the bibliography editor. Document Preferences set the citation style per document (plus language, footnote/endnote choice for note styles, Fields vs Bookmarks storage). **Unlink Citations is irreversible** and "should usually only be done in a final copy of your document" — converts citations/bibliography to plain text. Orphaned citations: "Items that are orphaned (not connected to any items in your Zotero database) will not have an 'Open in My Library' button. Orphaned items can exist if… deleted from your Zotero library."
- **Styles**: "Zotero uses Citation Style Language (CSL) to properly format citations in many different bibliographic styles. Zotero supports all the major styles (Chicago, MLA, APA, Vancouver, etc.) as well as the specific styles for over 8,000 journals and publishers."
- **Non-plugin output path**: "Zotero can also insert citations and bibliographies into any text field or program. Simply drag-and-drop items, use Quick Copy to send citations to the clipboard, or export them directly to a file." LaTeX/Scrivener via community plugins.
- **Sync & collaboration**: data sync via Zotero servers, file sync via Zotero servers or user WebDAV; online library access; Groups ("Shared group libraries make it possible to collaboratively manage research sources"); My Publications.
- **Duplicate Detection** exists as a documented top-level topic.

### EndNote — key observations (Evidence: A−, official product pages)

- Self-label: "reference manager" / "citation & reference management tool"; "Millions of researchers at the world's top universities and organizations trust their work to EndNote."
- **Cite While You Write** is the named flagship: "Insert properly formatted references and generate bibliographies as you write"; Find a Journal is "available directly in the industry-leading Cite While You Write plugin."
- **Styles**: "Access over 7,000 citation styles including APA, MLA, Chicago, and more. Switch between styles instantly." Downloads page offers "more styles, templates, filters, and connection files" (vendor-specific style/filter/connection file machinery).
- **Library organization**: "Use smart groups, tags, and custom folders to organize thousands of references effortlessly."
- **Capture**: "Import references from databases, PDFs, and websites with a single click using our browser extension"; "Automatically export your references and full-text PDFs into EndNote" (Kopernio one-click PDF access).
- **Metadata maintenance**: "Find Reference Updates and Find Full-Text improvements… retrieving full-text articles and updating your reference details, ensuring references are correct and complete." Web of Science integration: "Trusted and verified data from Web of Science™ to populate and update your EndNote libraries"; citing articles/related records views.
- **Sharing**: "Share entire libraries or subsets of references with up to 1,000 people and set permissions for access and editing. View activity logs."
- **Platform**: desktop (Windows/Mac) + EndNote Web + iOS; cloud sync; unlimited storage claims.
- **2025 additions (variant-era features)**: AI Research Assistant (chat with document, Key Takeaways summaries, translation), Cite from PDF ("insert a highlighted quote from a PDF and its corresponding citation… with a click"), retraction alerts, Find a Journal.
- Official Help Guide exists at docs.endnote.com (title page fetched; deeper pages not fetched — feature-level evidence only).

### Paperpile — key observations (Evidence: A−, official feature pages)

- Self-label: "Reference management. Clean and simple." / "The no-fuss reference manager for the web" (prior pass).
- **Feature anatomy** (top-level nav): Manage References, Find & Collect, Download & Sync, Annotate, Share, Cite in Google Docs.
- **Library**: "Organize your papers with folders, labels and stars. Search your library in real-time… Automatically fix references with incomplete data and clean up duplicates."
- **Capture**: Chrome extension; "Import data directly from Google Scholar, PubMed, ArXiv and thousands of supported publisher sites. Use the Paperpile button to save a reference, PDF or a supplementary data file."
- **PDFs in Google Drive**: "Download PDFs with one click and sync them directly to your Google Drive… No arbitrary storage size limitations."
- **Cite in Google Docs**: citation dialog ("Look up references from your library or online databases. Compile in-text citations with one or multiple references. Tweak your citations with additional options like page or chapter numbers."); styles ("any major citation style like APA, MLA, Chicago or in one of thousands of journal-specific styles"; "Upload and use your own customized citation style"); typographic detail handling (italics for species names, superscripts, footnote citations, 'ibid.' and 'et al.'); collaborative citation editing via a free Google Docs sidebar add-on ("It's free, no Paperpile account or subscription is required").
- **Platform coupling**: Chrome-only sign-up at research date (Safari/Firefox in beta); Google sign-in; Google Drive storage; Word plugin also offered; iOS/Android apps.

### Citavi — key observations (Evidence: A−, official product page + FAQ)

- Self-label: "reference management software that combines knowledge organization and AI-powered insights into one intelligent workflow"; "Your research writing and knowledge engine." "Trusted by researchers for 30+ years."
- **Gather references**: "import articles, books, PDFs, and webpages in seconds, or search library catalogs and academic databases directly from Citavi"; "automatic metadata extraction, a built-in browser picker, and over 11,000+ citation styles."
- **FAQ — acquisition paths enumerated**: search academic databases from within Citavi; "Enter an ISBN, DOI, or PubMed ID to automatically retrieve complete bibliographic details"; manual entry "using structured entry forms tailored to different source types"; import files (PDFs, RIS, BibTeX) "Citavi can extract metadata and link full texts automatically"; attach multimedia; Citavi Picker browser extension ("grab references, quotations, and images from websites or PDFs as you browse"). Plus: "avoid duplicates, check local library availability, and find full texts."
- **Knowledge-organization layer (variant emphasis)**: "Highlight important passages and instantly save quotations, summaries, comments, or images — all automatically linked to their reference information"; task planner with deadlines; "flexible categories for structuring your ideas. Drag and drop quotations, compare perspectives across sources, and watch your paper take shape"; export to Word "automatically formatted using Citavi's library of 11,000+ citation styles."
- **Cite loop**: Word Add-In ("insert citations and build your bibliography as you write"); Google Docs via "copying formatted citations and bibliography entries from your Citavi project and pasting them into your document" — a non-plugin realization of the same loop.
- **Styles**: "over 11,000 citation styles for journals, institutions, and publishers… You can easily switch styles at any time, upload your own, or customize an existing style."
- **Deployment**: cloud projects; local drive; "Citavi DBServer, which allows teams to work together securely within their own IT infrastructure" (on-premise); collaboration with roles/tasks; NVivo integration (categories → codes, quotations → annotations).
- **PDF annotation**: "You can highlight text, add comments, extract quotations, and create tasks directly within the PDF viewer. These annotations are saved in your project."

### Mendeley — key observations (Evidence: C, positioning/nav only; degraded)

- Product family structure from navigation: Mendeley Reference Manager (desktop download), Mendeley for Microsoft Word (Office store add-in), Mendeley Importer (Chrome extension), Mendeley Data (companion dataset service), Pricing, Support Center, Release Notes.
- Guide body (operational detail) not renderable — JS-rendered SPA; 1 fetch attempt this pass (prior pass failed 3× on different URLs). Per evidence rules: no reader/citation mechanics claims for Mendeley. The academic-paper-reader pass's positioning-level observations (reference manager with reader; importer extension) are carried as context only.

## Cross-product Comparison

| Dimension | Zotero | EndNote | Paperpile | Citavi | Mendeley |
|---|---|---|---|---|---|
| Self-label | "reference manager" | "reference manager" / "citation & reference management" | "reference management. Clean and simple." | "reference management software" | "Reference Manager" (product name) |
| Reference record = typed structured metadata | yes (item types; fields "needed to cite") | yes (references; summary panel; reference updates) | yes (references with metadata; fix incomplete data) | yes (structured entry forms per source type) | yes (positioning) |
| Persistent organized library | yes (collections-as-aliases, tags, saved searches) | yes (groups, smart groups, tags, custom folders) | yes (folders, labels, stars, real-time search) | yes (projects, categories, tags) | yes (positioning) |
| Cite-and-format loop into a manuscript | yes (Word/LibreOffice/Google Docs plugins; drag-and-drop/Quick Copy/export path; LaTeX via community plugins) | yes (Cite While You Write — named flagship; Word, Google Docs) | yes (Google Docs citation dialog + sidebar add-on; Word plugin) | yes (Word Add-In; Google Docs via copy-paste of formatted citations) | yes (Mendeley for Microsoft Word add-in) |
| Citation styles + switching | yes (CSL; major styles + 8,000+ journal styles; per-document style) | yes (7,000+ styles; "switch between styles instantly") | yes (major + thousands of journal styles; custom style upload) | yes (11,000+ styles; switch anytime; custom upload) | unverified (positioning) |
| Bibliography auto-generated from cited items | yes (explicit; auto-update; uncited-item editor) | yes ("generate bibliographies as you write") | yes (citations + bibliographies in Docs) | yes ("build your bibliography as you write") | unverified |
| Acquisition: browser capture | yes (Connector + translators) | yes (browser extension) | yes (Chrome extension) | yes (Citavi Picker) | yes (Importer extension, nav-level) |
| Acquisition: identifier lookup (ISBN/DOI/PMID) | yes (Add Item by Identifier, batch) | not observed at fetched level | not observed at fetched level | yes (FAQ explicit) | unverified |
| Acquisition: in-product database/catalog search | feeds only observed | not observed at fetched level | yes ("look up… online databases"; Scholar/PubMed/arXiv import) | yes (library catalogs + academic databases) | unverified |
| Acquisition: file import (RIS/BibTeX/PDF) | yes (importing from other tools documented) | yes (import from databases/PDFs) | yes (reference/PDF save) | yes (PDF/RIS/BibTeX with metadata extraction) | unverified |
| Manual entry | yes (last resort) | not observed | not observed | yes (structured forms) | unverified |
| Duplicate detection | yes (documented topic) | not observed | yes ("clean up duplicates") | yes ("avoid duplicates") | unverified |
| Metadata repair loop | yes (retrieve PDF metadata; refresh updates) | yes (Find Reference Updates) | yes ("automatically fix references with incomplete data") | yes (automatic metadata extraction) | unverified |
| Attachments (PDFs) | yes (child attachments; any file) | yes (PDFs; unlimited storage claims) | yes (PDFs in Google Drive) | yes (PDFs + multimedia) | yes (positioning) |
| Built-in reading/annotation | yes (PDF Reader documented; prior pass A) | yes (PDF viewing; Cite from PDF; AI chat) | yes (PDF annotator) | yes (PDF viewer with quotation extraction) | yes (prior pass, positioning) |
| Notes/knowledge layer | yes (notes; note-from-annotations per prior pass) | not observed at fetched level | not observed | yes (quotations/comments/images linked to references; categories; tasks) | unverified |
| Sync | yes (data + file sync, WebDAV option) | yes (cloud sync; desktop/web/iOS) | yes (Google Drive; apps) | yes (cloud projects; local; DBServer) | unverified |
| Sharing/groups | yes (group libraries) | yes (share up to 1,000 people; permissions; activity logs) | yes (shared folders; private links) | yes (cloud project collaboration; roles/tasks) | unverified |
| AI features | not in fetched docs | yes (Research Assistant 2025) | not observed | yes (AI assistant: key insights, passage summaries, paper search) | AI statement page exists (prior pass) |
| Deployment substrate | desktop app + sync service | desktop + web + iOS | web app (Chrome-coupled) | desktop + web + on-premise server | desktop + web |

## Canonical Model (abstraction layers)

### L0 — Defining Invariant

The smallest structure without which the product stops being recognizable as a Reference Manager — three jointly-held structures:

```text
Bibliographic Reference Record (typed structured metadata identifying a published source)
└── held in a Persistent Reference Library (accumulating, organized collection)
    └── Cite-and-Format Loop (the library feeds formatted citations + a bibliography
        into the user's manuscript, under a chosen citation style)
```

1. **The bibliographic reference record as the unit of record** — a persistent structured record describing a published source: item type (journal article, book, chapter, webpage, report, case…), creators, title, container/venue, date, pages, identifiers (DOI/ISBN/PMID/URL), plus cite-relevant fields. The record is the atom; attachments and notes hang off it. Evidence: Zotero item model (A); Citavi structured forms per source type (A−); EndNote/Paperpile reference libraries (A−). Remove it → a document/file library or bookmark collection (no bibliographic identity, nothing to cite).
2. **The persistent reference library** — records accumulate across projects and years as an organized, searchable collection (folders/collections, tags, search, duplicate handling). Evidence: all five products (A/A−/C). Remove it → a one-shot citation formatter with no memory.
3. **The cite-and-format loop** — while writing, the user pulls records from the library into a manuscript as formatted citations (in-text, footnote, or numeric) and the product generates/updates a bibliography from the cited records, formatted to a selected citation style; the whole document can be re-styled and refreshed when library data changes. Evidence: Zotero Word plugin mechanics (A); EndNote Cite While You Write (A−); Paperpile Google Docs citation dialog (A−); Citavi Word Add-In + copy-paste path (A−); Mendeley Word add-in (C, nav). Remove it → a bibliographic database or a literature library with no writing output (Academic Paper Reader / saved-items territory).

Jointly-held load-bearing tests:

- 1 alone = a bibliographic catalog/database (records nobody cites from)
- 2 without 1 = a PDF/document library (files without bibliographic identity)
- 3 without 1+2 = a form-based one-shot citation generator (no library, no accumulation)
- 1+2 without 3 = a literature collection with no writing output (academic-paper-reader / search-engine-library territory)
- 1+3 without 2 = a transient citation list — not a "manager" of anything

### L1 — Common Mature Structure

Present in essentially all mature modern products (Evidence: B across ≥4 products unless noted):

- **Acquisition machinery** — browser extension capture from publisher/database pages with metadata + PDF (Zotero A, EndNote A−, Paperpile A−, Citavi A−, Mendeley C-nav); identifier lookup by ISBN/DOI/PMID (Zotero A, Citavi A−); in-product search of databases/catalogs (Citavi A−, Paperpile A−); file import (RIS/BibTeX/PDF with metadata extraction) (Zotero A, Citavi A−); manual entry as fallback (Zotero A, Citavi A−).
- **Metadata retrieval and repair** — automatic metadata from identifiers/pages/PDF content; explicit repair/update loops (Zotero retrieve-PDF-metadata A; EndNote Find Reference Updates A−; Paperpile auto-fix A−; Citavi extraction A−).
- **Organization surfaces** — folders/collections (often alias semantics), tags/labels, quick + advanced search, saved/dynamic searches, duplicate detection (Zotero A; Paperpile A−; Citavi A−; EndNote A−).
- **Citation style sets** — the major generic styles plus large journal-specific style catalogs (Zotero 8,000+ A; EndNote 7,000+ A−; Citavi 11,000+ A−; Paperpile "thousands" A−); custom style upload (Paperpile A−, Citavi A−).
- **Word-processor integration** — a citation dialog over the library inside the writer's environment; locators (pages/chapters), prefix/suffix, omit-author, multiple items per citation, footnote support (Zotero A; Paperpile A−; EndNote A−; Citavi A−).
- **Bibliography generation and document restyling** — bibliography auto-built from cited records; style switch re-formats the document (Zotero A; EndNote A− "switch between styles instantly"; Citavi A−).
- **Attachments** — PDFs (and other files) attached to records; full-text retrieval helpers (all five; depth varies).
- **Sync across devices** — desktop/web/mobile continuity (all five at some level).
- **Sharing** — group/shared libraries with permissions (Zotero groups A; EndNote sharing A−; Paperpile shared folders A−; Citavi cloud projects A−).

### L2 — Variant / Optional Structure

Depends on segment, era, ecosystem, or workflow posture:

- **Reading/annotation depth** — from simple PDF viewing to full annotation surfaces with quotation extraction (Citavi) or DB-stored page-anchored annotations (Zotero, per prior pass); external-reader support (Zotero). NOT definitional — see joint review.
- **Knowledge-organization layer** — quotations, comments, images linked to references; outline/category structures; task planning (Citavi A− as its differentiator; Zotero notes/related items A; others thinner).
- **Citation-output mechanism** — word-processor plugin (dominant), copy-paste of formatted citations (Citavi's Google Docs path A−), drag-and-drop/clipboard/export (Zotero A), LaTeX/BibTeX export via community plugins (Zotero A). The mechanism varies; the formatted output into written work is the invariant.
- **Style technology** — CSL (Zotero) vs vendor style formats (EndNote style files/filters/connection files); custom style authoring/upload.
- **Ecosystem coupling** — Google account/Drive/Docs (Paperpile), Microsoft Office (EndNote/Citavi/Mendeley Word add-ins), Web of Science data (EndNote), NVivo (Citavi).
- **Deployment substrate** — local desktop, cloud sync service, web app, on-premise server (Citavi DBServer), institutional site licensing.
- **Discovery/monitoring adjuncts** — in-product database search, RSS feeds (Zotero A), saved-search alerts, Web of Science citing-article views (EndNote A−).
- **AI augmentation (2025-era)** — chat with documents, summaries, translation, AI search, journal finders (EndNote A−, Citavi A−); absent in older generations.
- **Companion outputs** — CV/publication lists (Zotero My Publications A), reports, data sharing (Mendeley Data, nav-level).

### L3 — Vendor-specific Structure (research notes only)

- Zotero: translators architecture; collections-as-aliases ("playlists"); Fields-vs-Bookmarks citation storage; irreversible Unlink Citations; orphaned-citation semantics; colored tags; WebDAV file sync; My Publications; CSL 8,000+ journal styles.
- EndNote: "Cite While You Write" branding; style/filter/connection file downloads; Web of Science integration; Find a Journal; retraction alerts; 1,000-person sharing with activity logs; Kopernio PDF access; Research Assistant AI suite.
- Paperpile: Chrome-only sign-up posture; Google Drive as the file store; free collaborative Docs sidebar add-on (works without a Paperpile account); BibTeX Guides/BibGuru companion properties.
- Citavi: project-based model (references + quotations + categories + tasks in one project); DBServer on-premise; local-library availability check; NVivo interplay (categories→codes); 11,000+ styles; Lumivero suite membership.
- Mendeley: Elsevier support hub; Mendeley Data companion; Importer extension (nav-level only).

## Vendor-specific Findings

See L3. Market-structure observations:

- **The cite-and-format loop is the named flagship everywhere it can be named**: Zotero's docs give "Citations & Bibliographies" its own top-level section; EndNote brands it "Cite While You Write"; Paperpile's nav has "Cite in Google Docs"; Citavi's FAQ leads with the Word Add-In. This is the Type's center of gravity.
- **Reading is packaged in, but never the headline**: every modern product ships a PDF surface, yet none of the five self-defines by reading; Zotero files its PDF Reader under "Organizing & Taking Notes", not under "Citations & Bibliographies".
- **Style catalogs are a competitive surface** (7,000–11,000+ styles claimed across vendors) — a common mature structure with vendor-specific counts.
- **The market spans four business models**: free open-source + paid storage (Zotero), commercial license/site license (EndNote, Citavi), freemium publisher suite (Mendeley), subscription SaaS (Paperpile) — the Type is business-model agnostic.

## Boundary Findings

| Compared Type | Structural test | Result |
|---|---|---|
| **Academic Paper Reader** | Remove the reading/annotation surface → citation database + cite-and-format loop remains (fully in-type); remove the cite-and-format loop → reading surface remains (fully reader) | **JOINT REVIEW DISCHARGED — keep-both RATIFIED from this side.** The two Types are fused in today's market packaging (modern reference managers embed readers) but have different centers of gravity: Reference Manager centers the citation database + formatted-citation output into manuscripts; Academic Paper Reader centers the reading surface. Fresh evidence this pass: (a) the historical generation of this Type (1980s–2000s EndNote/RefWorks/ProCite era) is a full Reference Manager with no reading surface at all — reading is demonstrably not definitional; (b) Zotero's own documentation taxonomy separates "Citations & Bibliographies" (top-level) from "PDF Reader" (nested under Organizing & Taking Notes); (c) Citavi's product anatomy separates "Gather references" from "Capture insights as you read"; (d) EndNote's flagship brand is Cite While You Write, with PDF reading/AI arriving as later additions. The reader inside a reference manager is a standard capability, not the Type's identity. |
| **Academic Search Engine** | Discovery/answering over a corpus vs holding and citing from one's own library | Distinct but coupled: the handoff is export/import (RIS/BibTeX) or in-product database search (Citavi searches catalogs/databases; Paperpile imports from Scholar/PubMed/arXiv). A saved-items list without the cite-and-format loop stays search-engine-side. |
| **PDF / Document Reader** | Rendering surface vs the bibliographic object model around it | Distinct; the renderer may be embedded or external (Zotero explicitly supports external readers). The boundary is the surrounding record/library/citation model, not the renderer. |
| **Bookmark Manager** | URL-based page saving vs bibliographic identity + citation output | Distinct: a bookmark has a URL and a title, not a typed bibliographic record; bookmarks do not generate bibliographies. Overlap zone: Zotero saves web pages as items with snapshots — but inside a bibliographic item model with citation output. |
| **Note-taking / Personal Knowledge Management** | Notes about sources vs records of sources | Distinct; Citavi's quotation/category/task layer straddles toward knowledge organization but stays anchored on reference records (every quotation is "automatically linked to their reference information"). A PKM product without the citation loop is not a Reference Manager. |
| **Integrated Library System** | Institutional holdings catalog (acquisitions/circulation/cataloging for an institution's patrons) vs a researcher's personal working library feeding their own writing | Distinct: different users, objects (holdings/items/loans vs personal reference records), and workflows. Shared vocabulary ("library", "catalog search") only. |
| **Professional Typesetting / LaTeX tooling** | Consumes bibliographic data vs manages the library | Distinct but interoperable: the BibTeX file is a reference database a typesetting chain consumes; Zotero documents LaTeX use via export/community plugins. The Reference Manager owns the records and the style formatting; the typesetting tool owns the page. |
| **Form-based citation generators (no directory leaf)** | One-shot formatting without a persistent library | The 3-without-1+2 removal test: a citation machine is not a Reference Manager. Recorded as the boundary's outer edge. |

### The "remove what" tests

- Remove the bibliographic identity (records become files/URLs) → **PDF/Document library or Bookmark Manager**.
- Remove the cite-and-format loop → **Academic Paper Reader** (if reading remains) or a **literature collection** (if not).
- Remove the persistent library → **one-shot citation generator**.
- Remove the manuscript output (records + library only) → **Academic Search Engine saved-list / bibliographic database**.

### Historical / market-sample check (older / regional / platform-native)

- **1980s–2000s bibliography-tool generation** (EndNote's early desktop generations, ProCite, RefWorks, and the product literally named "Reference Manager" by Research Information Systems): a local reference database + formatted bibliography output into Word/word processors via add-ins — satisfies all three L0 legs with no PDFs, no cloud, no browser capture, no AI. The Type's own name-giving product is metadata + citation output only.
- **LaTeX/BibTeX command-line workflow**: the .bib file is a structured reference database; \cite + style files produce formatted citations/bibliographies; no GUI library surface — fits the conceptual core (the loop and the records are present; the GUI is not definitional).
- **Paper card-file / index-card bibliography practice** (analog lineage): one card per source (the record), an organized box (the library), a bibliography typed to a style sheet (the output) — satisfies the structure at the analog level.
- **Regional products** (Citavi's DACH-strong heritage; 30+ years; multiple languages): same core with a knowledge-organization emphasis — fits.
- **Institutional deployments** (site licenses, on-premise DBServer): same core, different licensing — fits.

The L0 survives the historical check. PDFs/reading, cloud sync, browser capture, identifier lookup, style-catalog breadth, and AI are all correctly held OUT of the definition.

## Uncertainties

1. **Mendeley operational mechanics unverified** (guide body JS-rendered; 1 attempt this pass + 3 in the prior pass). No Mendeley-specific operational claims are made; its product-family structure (desktop RM + Word add-in + Importer) is nav-level evidence only.
2. **EndNote deep documentation not fetched** (Help Guide title page only; deeper docs.endnote.com pages not reached). EndNote claims are feature-level (product pages), not workflow-level; the CWYW mechanics are corroborated by pattern across Zotero (A) and Paperpile (A−) rather than by EndNote's own workflow docs.
3. **Citation-storage mechanics** (how citations persist inside the manuscript document — Zotero's Fields/Bookmarks is documented; equivalent mechanics for EndNote/Paperpile/Citavi not verified at storage level). Final document states the live-link behavior generally, not storage mechanics.
4. **Style-count figures** (8,000+ / 7,000+ / 11,000+) are vendor claims at positioning level — recorded as claims, not verified counts.
5. **Non-academic professional use** (law, medicine, corporate research writing) is evidenced only indirectly (EndNote's organizations/government segment page; Citavi's Marinomed/Roche testimonials). The Type is treated as research/writing-centric with professional spillover; no separate professional variant is asserted.

## Final Synthesis

A Reference Manager is the researcher's **citation system of record**: a persistent, organized library of bibliographic reference records — each a typed, structured description of a published source — plus the machinery that feeds those records into the user's manuscript as correctly formatted citations and an automatically generated bibliography under a chosen citation style. Acquisition (browser capture, identifier lookup, database search, file import, manual entry), organization (collections, tags, search, duplicate handling), attachments and reading, notes, sync, and sharing are standard or optional structure layered on that core. The defining test is the loop: records → library → formatted citations + bibliography in the written work. Remove the loop and the product drifts to the paper-reader/literature-collection side; remove the records' bibliographic identity and it drifts to file/bookmark management; remove the library and it collapses into a one-shot citation formatter.

Joint-review outcome (vs Academic Paper Reader): keep-both ratified from this side — the reading surface is a standard capability inside modern reference managers, not the defining core; the two Types are fused by market packaging but separated by center of gravity (citation database + cite-while-writing vs reading-and-annotation).
