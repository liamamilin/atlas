# Research Notes — Academic Paper Reader

Research date: 2026-09-06

## Research Goal

Understand what an Academic Paper Reader is as an Application Type: what the central object ("a paper") is, how papers enter the reading environment, what the reading surface provides beyond page rendering, how reading side-effects (annotations, notes) persist and flow onward, and how this Type is bounded against PDF / Document Reader, Reference Manager, Read-it-later Application, E-book Reader, and Academic Search Engine.

## Initial Boundary

Initial hypothesis (pre-research): the Type centers on reading scholarly articles on screen with support for paper-specific reading work — annotation, navigation by scholarly structure (figures, references, sections), and a durable library of papers. The closest confusions:

- **PDF / Document Reader** — papers are usually distributed as PDFs; a generic reader can render them. The paper-specific part must be more than rendering.
- **Reference Manager** — the dominant products researchers use to read papers (Zotero, Mendeley, ReadCube Papers, Paperpile, EndNote) are marketed as reference managers; reading is one capability inside them.
- **Read-it-later Application** — both hold documents to read later.
- **Academic Search Engine / AI Research Assistant** — discovery and Q&A vs. reading a held document.

## Research Questions

1. What is "a paper" as an object — is it more than a PDF file (bibliographic identity, identifiers, versions, supplements)?
2. How do papers enter the reading environment (import paths, acquisition machinery)?
3. What does the reading surface add beyond page rendering (navigation, annotation, citation navigation, figure/table handling)?
4. How do annotations and notes persist, and how do they flow onward (export, notes, citations)?
5. How is the collection of papers organized (collections, tags, search, sync, sharing)?
6. Where does AI augmentation fit (summaries, chat, explain, skimming), and does it change the core model?
7. What is the boundary against Reference Manager, PDF Reader, Read-it-later, E-book Reader, Academic Search Engine?
8. Would older / platform-native products (early desktop reference managers, publisher-hosted viewers, OS PDF viewers) still fit the definition?

## Representative Products

Selection logic: market representation + documentation quality + different product philosophies + different customer layers.

| Product | Philosophy | Customer layer | Evidence level reached |
|---|---|---|---|
| **Zotero** (Digital Scholar, nonprofit, open source) | Library-first reference manager with a first-class built-in reader and notes | Individual researchers/students; free + paid storage | A — full Tier-1 documentation pages fetched |
| **ReadCube Papers / ReadCube** (Digital Science) | Dedicated "literature management" platform grown out of a paper-reading product; enhanced reading + AI | Individual researchers through institutions/enterprises | A− — full product page + Help Center structure fetched; individual help articles not fetched |
| **Semantic Reader** (Semantic Scholar / Ai2) | AI-augmented scientific reading surface over a search corpus | Individual researchers; free public platform | A — full product page fetched |
| **Readwise Reader** | General "everything reader" (articles, PDFs, EPUBs, RSS, newsletters) used heavily by academics; boundary probe | Consumer power readers, incl. academics | A — full product page fetched |
| **Paperpile** | Web-native, Google-coupled reference manager with PDF annotator | Individual academics, Chrome/Google Docs users | B — product page + feature-page titles fetched |
| **Mendeley** (Elsevier) | Publisher-suite reference manager with reader | Individual academics (free) / institutions | C — positioning only; guide pages are JS-rendered and returned no content (3 attempts on different URLs, then abandoned) |

SciSpace (an AI-first paper reader) was planned as a sample but both fetch attempts failed (empty response, then timeout); it was abandoned per the source-retry rule and is NOT described from memory.

## Sources

- Zotero — PDF Reader and Note Editor: https://www.zotero.org/support/pdf_reader (fetched 2026-09-06; last updated 2026-05-05)
- Zotero — Adding Items to Zotero: https://www.zotero.org/support/adding_items_to_zotero (fetched 2026-09-06; last updated 2026-02-11)
- ReadCube — product page: https://www.papersapp.com/ → about.readcube.com (fetched 2026-09-06)
- ReadCube — Help Center: https://about.readcube.com/help-center/ (fetched 2026-09-06)
- Semantic Reader — product page: https://www.semanticscholar.org/product/semantic-reader (fetched 2026-09-06)
- Readwise Reader — product page: https://readwise.io/read (fetched 2026-09-06)
- Paperpile — product page: https://paperpile.com/ (fetched 2026-09-06)
- Mendeley — https://www.mendeley.com/guides/mendeley-reference-manager/ and /02 and /download-reference-manager/ (fetched 2026-09-06; content body not renderable — nav/footer only)

## Product Observations

### Zotero — key observations (Evidence: A, official docs)

- **Two-object structure: item (bibliographic record) + attachment (file).** A PDF added directly becomes a "standalone attachment"; Zotero "automatically attempt[s] to retrieve metadata … and create a parent item". "Standalone attachments can't have bibliographic metadata or child notes, so in most cases you'll want to convert them to child items under regular parent items." This is direct documentary evidence that the paper object = content + bibliographic identity, and that identity is treated as the primary organizing entity.
- **Import machinery is a first-class subsystem**: browser connector saves from publisher pages with "high-quality bibliographic metadata" and downloads the PDF; "Add Item by Identifier" accepts ISBN, DOI, PubMed ID, arXiv ID, ADS Bibcode, resolved via CrossRef/PubMed/arXiv/ADS registries; direct PDF import triggers automatic metadata retrieval; batch import via BibTeX/RIS; manual entry as last resort.
- **Reader surface**: highlights and underlines (two modes: popup per selection; "locked mode" for batch highlighting), annotation toolbar, annotations tab in sidebar.
- **Annotations → notes flow**: "Add Item Note from Annotations", drag individual annotations into notes; added annotations "automatically include links back to the PDF page as well as citations that you can later add to a Word, LibreOffice, or Google Docs document". "Show on Page" re-opens the PDF at the annotation's page. Note templates customizable.
- **Annotation storage semantics**: "annotations created in the built-in PDF reader are stored in the Zotero database, so they won't be visible in external PDF readers unless you export a PDF with embedded annotations." Annotations are page-anchored records in the product's data model, not just ink in a file.
- **External reader support**: a preferred external PDF reader can be configured; page-level structural changes (delete/reorder/rotate) in external tools can break annotation anchoring — confirms annotations are anchored to the document layout.
- **Library organization** (nav-observed, doc titles): Collections and Tags, Searching, Sorting, Related Items, Duplicate Detection, Feeds, Syncing, Groups.

### ReadCube Papers — key observations (Evidence: A− positioning + help-center taxonomy)

- Positioning: "Discover, read, organize, and cite scientific literature, all in one platform."
- Reading: "Annotate directly on the PDF — Highlight, underline, draw, and add notes and sticky comments."
- Acquisition: "Import with full metadata — Every reference arrives with citations, supplemental data, and full text." Discovery backed by a scholarly index (Dimensions, "123M+ indexed papers").
- Organization: "Tags, custom fields, and Smart Lists keep growing libraries sorted and easy to share"; shared libraries for teams.
- AI augmentation: ask in plain language, answers "from your library and trusted databases, each linked to the exact passage in the source"; chat with one paper or up to 20 papers at once; per-paper "AI Access Indicator" flags whether publisher terms permit AI use.
- Monitoring: saved recurring searches auto-add new papers to the library, with email alerts.
- Adjacent capabilities in the same platform: SmartCite (cite in Word/Google Docs), document delivery, systematic review (PRISMA, dual-reviewer screening, extraction forms).
- Help Center topics: Getting Started, Search & Discover, **Read & Annotate** (13 docs), Organize, SmartCite, Collaboration, Library & Device Sync, Browser Extension, Mobile — confirms the functional anatomy (acquire → organize → read/annotate → cite → share/sync).

### Semantic Reader — key observations (Evidence: A, official product page)

- Self-description: "An AI-Powered Augmented Scientific Reading Application."
- **Explicit canonical frictions of paper reading** (the vendor's own research framing): "Frequently paging back and forth looking for the details of cited papers; Challenges recognizing the same work across multiple papers; Losing track of reading history and notes; Contending with a PDF format that is not well suited to mobile reading or assistive technologies."
- Mechanism: "uses artificial intelligence to understand a document's structure and merge it with the Semantic Scholar's academic corpus, providing detailed information in context via tooltips and other overlays."
- Features: in-line citation cards with TLDR summaries; table of contents; "Save to Library to conveniently track your reading list"; personalized in-line citations (colored by relation to the reader's library, e.g. "cited by a paper saved to your library"); AI skimming highlights labeled Goal / Method / Result; definitions on demand for terms/symbols; annotation via Hypothesis integration (highlight + notes, "review your annotations anytime, and share them with others").
- Availability scoped to "most arXiv papers" in English-language CS fields — augmentation is corpus-dependent, not universal.

### Readwise Reader — key observations (Evidence: A, official product page)

- Positioning: "The first read-it-later app built for power readers"; "All your reading in one place."
- Content model is type-agnostic: web articles, PDFs, EPUBs, RSS, newsletters, YouTube transcripts, Twitter threads. PDFs enter by upload ("Everyone has a forgotten folder of PDFs").
- Reading surface: "highlight images, tables, rich text" on any device; document notes; keyboard-first navigation; full-text search; text-to-speech; AI copilot (Ghostreader: ask questions, define terms, simplify language).
- Workflow: inbox/triage ("weed your digital garden"), then annotate; highlights flow to the companion Readwise product (spaced-repetition resurfacing) and export to note apps (Obsidian, Notion, Logseq, Evernote, Roam) and via API/MCP.
- Note: the content model has no bibliographic identity layer — documents are saved items, not scholarly records with DOI/venue metadata. Academic papers are one content type among many.

### Paperpile — key observations (Evidence: B, positioning-level)

- Self-description: "The no-fuss reference manager for the web… Manage your research library right in your browser."
- Feature-page anatomy: Manage References, Find and Collect, **Organize PDFs**, **Highlight and annotate** (PDF annotator), Share and Collaborate, Cite in Google Docs; iOS/Android apps; Word plugin.
- Chrome/Google-account/Google Docs coupling (sign-up Chrome-only at research date; blog posts confirm PDF night mode, bulk downloads).
- No operational detail on annotation storage/anchoring verified.

### Mendeley — key observations (Evidence: C, positioning-only; degraded)

- Product family confirmed from navigation: Reference Manager (desktop download), Mendeley for Microsoft Word, Mendeley Importer (browser extension), guides, release notes, support hub, Mendeley Data.
- Guide content body (reading/annotating specifics) could not be fetched (JS-rendered SPA; 3 attempts on different URLs). Per evidence rules, no reader-mechanics claims are made for Mendeley; historical market knowledge (Mendeley as a widely used reader inside a reference manager) is recorded only as context, not as sourced evidence.

## Cross-product Comparison

| Dimension | Zotero | ReadCube Papers | Semantic Reader | Readwise Reader | Paperpile | Mendeley |
|---|---|---|---|---|---|---|
| Paper = bibliographic record + content | yes (item/parent + attachment; explicit) | yes ("full metadata", citations, supplements) | yes (corpus-linked paper identity; citations cards) | no — generic saved document | yes (reference manager) | yes (positioning) |
| Persistent library of papers | yes (collections, tags, sync, groups) | yes (smart lists, custom fields, shared libraries) | yes ("Save to Library"; personalized citations from library) | partial — saved-items list, no scholarly identity | yes | yes (positioning) |
| Full-text reading surface | yes (built-in reader; external reader optional) | yes ("read… directly on the PDF") | yes (reader over arXiv papers) | yes (PDF/article/EPUB reader) | yes (web PDF annotator) | yes (positioning) |
| Annotation on the paper | yes (highlight/underline, colors, page-anchored, DB-stored) | yes (highlight/underline/draw/notes/sticky) | yes (via Hypothesis: highlight + notes, shareable) | yes (highlight images/tables/text; doc notes) | yes (feature page) | unverified |
| Annotation → onward flow | yes (notes with page links + citations; export to word processors) | yes (AI answers linked to passages; cite via SmartCite) | yes (notes reviewable anytime; share) | yes (highlight export to note apps/API) | unverified | unverified |
| Acquisition machinery | connector save, DOI/arXiv/PubMed lookup, PDF metadata retrieval, RIS/BibTeX | import with metadata + supplements; Dimensions discovery | corpus-side (papers come from the search engine) | upload/save (type-agnostic) | browser save, Scholar/DOI | importer extension (positioning) |
| Organization of collection | collections/tags/search/related/duplicates | tags/custom fields/smart lists/sharing | save-to-library | inbox triage + labels | folders/labels (positioning) | positioning |
| AI augmentation | not in core reader (none observed in fetched docs) | chat with paper(s)/library; AI access flags | citation TLDRs, skimming highlights, definitions | Ghostreader Q&A/define/simplify; TTS | none observed | AI statement page exists |
| Social/shared reading | groups (library sharing) | shared libraries; dual-reviewer workflows | shared public annotations (Hypothesis) | no | share/collaborate pages | positioning |

## Canonical Model (abstraction layers)

### L0 — Defining Invariant

The smallest structure without which the product stops being recognizable as an Academic Paper Reader:

```text
Scholarly Paper Record (content + bibliographic identity)
└── held in a Persistent Personal/Shared Library
    └── Reading Surface presenting the paper's full published content
```

Three properties; the test for each is "if removed, is it still this Type?":

1. **Scholarly paper as an identified record** — the document is held together with its bibliographic identity (authors/venue/year or a scholarly identifier such as DOI/arXiv ID), not as an anonymous file. Evidence: Zotero's explicit item→attachment model and parent-item metadata retrieval (A); ReadCube's "import with full metadata… citations, supplemental data" (A−); Semantic Reader's corpus-linked paper identity (A). Remove it → generic PDF/Document Reader.
2. **Persistent library of papers** — papers accumulate across sessions as an organized collection the reader returns to; it is a working collection, not an inbox to clear. Evidence: all sampled reference-manager products (A/A−/B) and Semantic Reader's save-to-library (A). Remove it → a viewer or a one-shot chat-with-PDF tool (different Type).
3. **Reading surface for the paper's full published content** — the primary interaction is reading the document itself (layout-preserving full text, typically paginated; figures/tables/references in place), not a summary, snippet, or transcript. Evidence: every sampled product (A). Remove it → Academic Search Engine / Answer Engine.

Note: annotation is NOT in L0. Annotation is present in every sampled modern reader but is also present in generic PDF readers, so it does not distinguish the Type; it belongs to standard capabilities (L1). Historical check (below) supports this: early paper-reading products were library + reading first, with annotation depth varying.

### L1 — Common Mature Structure

Present in essentially all mature modern products (Evidence: B across ≥4 products unless noted):

- **Import/acquisition machinery** — browser connector saving from publisher pages with metadata + PDF; identifier lookup (DOI, arXiv, PubMed, ISBN); direct-PDF import with automatic metadata retrieval; file-format exchange (BibTeX/RIS). (Zotero A; ReadCube A−; Paperpile B)
- **Metadata retrieval and correction** — automatic metadata from content or registries; verification/repair loops (Zotero documents the failure modes and manual repair explicitly).
- **Organization surfaces** — collections/folders, tags/labels, search, sorting; sometimes smart/dynamic lists, related-item links, duplicate detection.
- **Annotation on the reading surface** — highlights (usually colored), notes; in some products underlines, drawings, sticky comments, area/figure snapshots. (Zotero A; ReadCube A−; Semantic Reader A; Readwise A; Paperpile B)
- **Annotations as durable data** — annotations persist in the product's data model (page-anchored), survive sessions, and can be exported or flowed into notes/other tools. (Zotero A: "stored in the Zotero database… links back to the PDF page"; Readwise A: Markdown export; ReadCube A−; Semantic Reader A: "review your annotations anytime")
- **Note-taking attached to papers** — per-item notes; note construction from annotations is a mature pattern (Zotero's note-from-annotations with auto citations; Readwise document notes).
- **Onward flow to writing** — annotations/records flow toward writing tools: citations insertable into word processors (Zotero plugins, ReadCube SmartCite, Paperpile Google Docs); exports to note apps (Readwise). Depth varies; presence is common.
- **Multi-device sync** — library + annotations available across desktop/web/mobile. (ReadCube "Library & Device Sync"; Paperpile iOS/Android; Readwise cross-platform; Zotero sync)
- **Document navigation** — table of contents / page navigation; full-text search within papers and across the library.

### L2 — Variant / Optional Structure

Depends on segment, era, business model, or workflow posture:

- **AI augmentation of reading** — in-context citation summaries, skimming highlights (rhetorical facets), on-demand definitions, chat with a paper or the whole library, AI answers "linked to the exact passage" (Semantic Reader A; ReadCube A−; Readwise A). Absent in older products; posture and depth vary strongly; corpus- or licensing-dependent (Semantic Reader: arXiv CS papers only; ReadCube flags per-paper AI permission).
- **Social / collaborative reading** — shared libraries, group annotation, public annotation layers (Zotero groups; ReadCube shared libraries + dual-reviewer screening; Semantic Reader/Hypothesis public annotation).
- **Acquisition modes** — publisher-integrated discovery (Dimensions index), saved-search monitoring with automatic library additions and alerts (ReadCube A−), feeds (Zotero), corpus-side acquisition (Semantic Reader: papers arrive from the search engine).
- **Citation-writing depth** — full bibliography generation and styles (shared with Reference Manager; varies from absent to deep).
- **Reading comfort variants** — dark/night mode (Paperpile blog-confirmed), text-to-speech (Readwise A), mobile/reflowed reading (Semantic Reader names PDF's mobile/assistive weakness as a problem it addresses).
- **Open-access / document delivery** — helping readers reach accessible copies (ReadCube document delivery; Zotero's open-access PDF lookup from the connector — observed as "an open-access PDF that can be found for the saved item").
- **Platform substrate** — desktop app vs web-first vs corpus-hosted web; identity substrate varies (local account, Google account, institutional/publisher account).

### L3 — Vendor-specific Structure (research notes only)

- Zotero: locked-vs-popup highlighting modes; note templates; annotations stored in the product database with export-to-embedded-annotations; external-reader page-anchoring constraints; specific identifier registries (CrossRef, PubMed, ADS Bibcode).
- ReadCube: SmartCite branding; Dimensions-backed discovery ("123M+ indexed papers"); AI Access Indicator; PRISMA/systematic-review module; up-to-20-paper chat; Essentials/Plus/Team/Enterprise packaging.
- Semantic Reader: TLDR citation cards; Goal/Method/Result skimming overlays; definitions via dotted-underline terms; Hypothesis annotation integration; personalized in-line citation coloring from the user's library; PaperMage/PaperCraft open libraries.
- Readwise: Ghostreader AI; Daily Review (spaced repetition); MCP server/CLI/API-first posture; Kindle send; e-ink mode.
- Paperpile: Chrome/Google-account sign-up posture; Google Docs citation integration; Google Drive file storage.
- Mendeley: Elsevier support hub; Mendeley Data companion.

## Vendor-specific Findings

See L3. Additional market-structure observations:

- **The dominant commercial implementation of paper reading is embedded in reference managers.** Four of six sampled products self-identify as reference/literature managers; reading/annotating is a named capability layer in each ("Read & Annotate" help category; "Highlight and annotate" feature page). The Type as an independent product manifests in: (a) AI-augmented reading surfaces attached to discovery platforms (Semantic Reader), and (b) general reading apps with PDF support (Readwise Reader).
- **Augmented-reading research lineage** is unusually visible in this Type: Semantic Reader ships research prototypes (ScholarPhi, CiteRead, Scim) as product features and publishes open tooling — the Type's frontier is partly academic HCI research.

## Boundary Findings

| Compared Type | Structural test | Result |
|---|---|---|
| **PDF / Document Reader** | Remove the bibliographic identity and the persistent scholarly library → content-agnostic file viewing remains | Distinct Type; PDF Reader is a rendering surface this Type may embed or delegate to (Zotero explicitly supports external readers). The boundary is the surrounding object model, not the renderer. |
| **Reference Manager** | Remove the reading/annotating surface → citation database + bibliography writing remains; remove citation writing → reader remains | The two Types are fused in today's market: the paper-reading surface is the standard embedded reader of reference-manager products. Reading is the center of gravity of THIS Type; the citation database + cite-while-writing is the center of gravity of Reference Manager. Flag for joint review. |
| **Read-it-later Application** | Read-later holds a triage queue of heterogeneous web content intended to be processed/cleared; paper reader holds a durable, identity-bearing scholarly collection | Readwise Reader straddles: it is a read-it-later app whose PDF support lets it do paper-reading work, but its content model has no scholarly identity layer — papers are "documents" like any other. The boundary is the identity+library model vs the inbox model. |
| **E-book Reader** | Books: long-form, chapter-based, often reflowable, DRM; papers: short-form, fixed-layout, figures/equations/references, bibliographic identity | Distinct; both can share a general "everything reader" shell (Readwise reads both EPUBs and PDFs) without the Types merging. |
| **Academic Search Engine** | Discovery/answering over a corpus vs reading a held paper | Distinct but coupled: Semantic Reader is the reading surface of a search engine's corpus; "save to library" is the hand-off between the two Types. |
| **AI Research Assistant** | Q&A across sources vs reading one identified paper with annotation | Chat-with-paper/library features cross the line; the line is whether the reading surface + library or the Q&A loop is the center of gravity. |

### The "remove what" tests

- Remove bibliographic identity + library → **PDF / Document Reader**.
- Remove the reading surface (keep identity + library + citations) → **Reference Manager** proper.
- Remove persistence (inbox instead of library) → **Read-it-later Application**.
- Remove the held document (corpus-side snippets only) → **Academic Search Engine**.

### Historical / market-sample check (older / regional / platform-native)

- Early desktop reference/reading products (the Papers / Mendeley Desktop era, late 2000s): local library of PDFs with metadata + embedded reading + basic highlighting — satisfies the L0 exactly (identity + library + reading surface), with annotation depth below today's norm. Consistent.
- OS-native PDF viewers (macOS Preview etc.) reading a downloaded paper: no identity, no library → correctly excluded as PDF Reader usage.
- Publisher-hosted article viewers (HTML/PDF on journal sites): reading surface + paper identity, but no persistent reader-owned library → belongs to the publishing/subscription platform, not this Type (matches Semantic Reader's contrast: it adds "your library" to the reading surface).
- arXiv listing + in-browser PDF: discovery + viewing → Academic Search Engine + PDF Reader, correctly excluded.

The L0 survives the historical check; annotation (L1) and AI (L2) are correctly excluded from the definition.

## Uncertainties

1. **Mendeley reader mechanics unverified** (guide pages JS-rendered; degraded to positioning). The canonical model does not depend on it, but Mendeley-specific claims are absent by design.
2. **SciSpace not researched** (two fetch failures). The AI-first reader wave is covered indirectly via Semantic Reader, ReadCube AI, and Readwise Ghostreader; no SciSpace-specific claims are made.
3. **Annotation anchoring depth** — Zotero documents page-anchored DB storage explicitly; anchoring semantics for ReadCube/Paperpile/Semantic Reader (via Hypothesis) are observed only at feature level, not storage level. Final document states persistence generally, not storage mechanics.
4. **Semantic Reader's library model** is thinner than reference-manager libraries (save-to-library + reading list); its classification as a (corpus-hosted) implementation of this Type rather than an adjacent Type is a judgment call — recorded, treated as a variant of this Type because reading is its center of gravity.
5. **E-reader/tablet paper-reading devices and apps** (reMarkable-class, iPad stylus apps) were not sampled; handwriting annotation is treated as an L2 variant based on partial evidence only (ReadCube "draw").

## Final Synthesis

An Academic Paper Reader is an application whose world is a **persistent library of identified scholarly papers** and whose primary interaction is **reading a paper's full published content on a dedicated reading surface**. The paper is a record — content bound to bibliographic identity — not an anonymous file; the library is a durable working collection, not an inbox; the reading surface is augmented for scholarly work (annotation, structure navigation, citation context). Everything else — acquisition machinery, organization, sync, AI augmentation, sharing, citation writing — is standard or optional structure layered on this core.

Market structure: the Type is usually *realized inside* reference-management products (as their embedded reader), and re-appears independently where reading is the product's center of gravity — AI-augmented reading surfaces over scholarly corpora and general reading apps with scholarly PDF support. The definition is written to cover both without collapsing into Reference Manager or PDF Reader.
