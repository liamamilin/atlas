# Research Notes — Document Editor

Research date: 2026-09-07
Directory leaf: Document Editor (§03.01 Documents & Writing)
Slug: document-editor

---

## Research Goal

Understand what a Document Editor is as an Application Type: what the unit of work is, how the formatting model is presented during editing, what the page/print model contributes to the definition, which content objects and authoring aids are standard, how the review loop works in an author-owned file model, and where the boundary lies against the Collaborative Document Editor, Markdown Editor, Distraction-free Writing Application, Desktop Publishing / Page Layout, Note-taking, and Resume Builder.

## Initial Boundary (hypothesis before research)

- Core guess: a Document Editor is the classic word processor — an application for authoring persistent prose documents with direct inline editing, explicit user-controlled formatting visible while writing, and a page-oriented output model producing a finished artifact (print/PDF/interchange file).
- Most likely confusions:
  - Collaborative Document Editor (processed sibling): the shared live merged document is the primary object there; here the document is an author-owned artifact with collaboration layered on.
  - Markdown Editor (unprocessed sibling): formatting deferred to a rendering step vs explicit formatting on the editing surface.
  - Distraction-free Writing Application (processed sibling): formatting continuously visible here vs attention surface with deferred/hidden chrome there.
  - Desktop Publishing / Page Layout Application (processed): layout canvas with placed frames first vs body-text flow first.
  - Note-taking Application: fragment collections vs single finished artifact.
  - Resume Builder (processed): structured content model with tool-owned rendering vs free-form authoring.
- Unknown points at start: whether pagination belongs in the defining core; whether the review loop (track changes/comments) is core or mature-added; how cloud-storage/auto-save changes the file model; whether Pages' word-processing vs page-layout split inside one product is a variant or a Type problem.

## Research Questions

1. What is the unit of work and how is it persisted (file? cloud document record? format?)
2. What is the formatting model (direct formatting vs styles vs templates) and how is it presented during editing?
3. What is the page/print model (pagination, page setup, headers/footers, print, export) — definitional or standard?
4. What content objects can a document contain (tables, images, charts, hyperlinks, footnotes, TOC)?
5. What authoring aids are standard (spell check, autocorrect, find/replace, word count, dictation)?
6. How does the review loop work in the author-owned model (track changes, comments, accept/reject)?
7. How do cloud storage, AutoSave, versions, and protection modify the file model?
8. What variants exist (suite vs standalone vs platform-bundled; desktop/web/mobile; regional)?
9. Where are the boundaries vs the neighbor Types listed above?
10. Historical check: do keyboard-driven, formatting-code-era word processors still satisfy the definition? Do minimal rich-text editors fail it correctly?

## Representative Products

Selected for market representativeness + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy / tier | Evidence quality |
|---|---|---|
| Microsoft Word | dominant office-suite editor; richest mature implementation; desktop/web/mobile; consumer + enterprise | Tier-1 official support docs; 5 surfaces fetched (hub + 4 articles) |
| LibreOffice Writer | free open-source desktop editor; file-based, offline-first, ODF; individual/public-sector tier | Tier-1 official help: welcome page + Writer Features page fetched |
| Apple Pages | platform-native consumer editor bundled with the OS; document-first, design-forward | Tier-1 official user guide: full TOC + 2 deep articles fetched |
| Google Docs | cloud-native editor; the collaboration pole of the document-editor market | positioning anchor only — support page timed out (see Sources) |

Sibling-pass context: the Collaborative Document Editor pass (2026-09-06) documented this boundary from the other side and provides Word co-authoring evidence (real-time vs save-based legacy mode) used here only for boundary framing.

## Sources

Fetched 2026-09-07:

- Microsoft Support — Word help & learning hub: https://support.microsoft.com/en-us/word — fetched OK
- Microsoft Support — "Create a document in Word": https://support.microsoft.com/en-us/word/training/create-a-document-in-word — fetched OK
- Microsoft Support — "Add and edit text": https://support.microsoft.com/en-us/word/training/add-and-edit-text — fetched OK
- Microsoft Support — "Save a document": https://support.microsoft.com/en-us/word/training/save-a-document — fetched OK
- Microsoft Support — "Track changes in Word": https://support.microsoft.com/en-us/word/training/track-changes-in-word — fetched OK
- LibreOffice Help — Welcome to LibreOffice Writer Help: https://help.libreoffice.org/latest/en-US/text/swriter/main0000.html — fetched OK
- LibreOffice Help — LibreOffice Writer Features: https://help.libreoffice.org/latest/en-US/text/swriter/main0503.html — fetched OK
- Apple Support — Pages User Guide for Mac (welcome + full TOC): https://support.apple.com/guide/pages/welcome/mac — fetched OK
- Apple Support — "Intro to word-processing and page layout documents in Pages on Mac": https://support.apple.com/guide/pages/word-processing-or-page-layout-tan6129a1862/mac — fetched OK
- Apple Support — "Intro to paragraph styles in Pages on Mac": https://support.apple.com/guide/pages/intro-to-paragraph-styles-tanaa39b0aa3/mac — fetched OK

Failed / abandoned:

- Google Docs — https://support.google.com/docs/answer/6063498 — timed out ×1 this pass (and ×3 in the 2026-09-06 sibling pass across different Google URLs); source abandoned per retry discipline. Google Docs is used only as a market anchor; no operational claims about it are made anywhere.

Source-access limitations:

- No precise claims are made about Google Docs (edit windows, pageless mode, offline behavior, permission names, version mechanics — all unasserted).
- LibreOffice evidence is at features-page + help-TOC level; individual guide/menu subpages were not fetched. LibreOffice macro support is NOT asserted from fetched text.
- Zoho Writer / WPS Office not fetched this pass; no claims about them.
- Word online-templates catalog, version-history internals, .docx format internals: not fetched, not asserted.

---

## Product A — Microsoft Word

Evidence layer: A (directly observed in official support docs).

### Key observations

- **Document creation**: File → New → Blank document, or pick from templates ("Search for online templates"). Word's own summary of what it does: "Create a document from scratch or from a template. Add text, images, art, and videos. … Access your documents from a computer, tablet, or phone via OneDrive. Share your documents and collaborate with others. Track and review changes."
- **Formatting model**: type text, select, format from a pop-up toolbar or the **Home** tab — Font, Font Size, Font Color, bold/italics/underline, bullets/numbering. **Format Painter** copies formatting between selections. Formatting is applied inline during writing with immediate visible effect.
- **Content objects** (Insert tab): Tables, Pictures, Shapes, Icons, 3D Models, SmartArt, Chart, Screenshot. Help taxonomy also covers WordArt, watermarks, page borders, header/footer, page numbers, page breaks, newsletter columns, table of contents, text wrap around pictures, ruler.
- **File model**: File → Save a Copy → **OneDrive** or "another location, like your desktop"; name + **file type**; "When you save to OneDrive or SharePoint, all your changes are saved automatically" — AutoSave toggleable on the Quick Access Toolbar. Save as template supported. Save & print category also includes **Edit a PDF** and **Create and print labels** / mailing labels.
- **Review loop** (Track Changes, full article): Review tab → Track Changes on/off; scope **For Everyone vs Just Mine**; deletions struck through, additions underlined, per-author colors; markup views (Simple Markup margin line / All Markup with per-reviewer colors / No Markup / Original); balloons vs inline display; filter markup by type (insertions/deletions/formatting) and by reviewer; navigate Next/Previous; Accept/Reject per change, all shown, or all (each with "and Stop Tracking" variants); **Lock Tracking with a password** so others cannot turn it off; documents "shared for review" may prevent turning Track Changes off (save a copy or ask sender to re-share); Reviewing Pane lists remaining tracked changes and comments with counts; hiding markup when printing does not remove it — only Accept/Reject removes it; "Comments are no longer part of the Track Changes function" (separate feature). Documented across Windows, Web, macOS, iPad, iPhone.
- **Positioning**: share/collaborate and track/review changes are listed as capabilities of the product, not its identity — the hub's own structure separates "Collaborate" from Create/Format/Pages/Save.

## Product B — LibreOffice Writer

Evidence layer: A (directly observed on the official Features page and help welcome page).

### Key observations

- **Self-definition**: "LibreOffice Writer lets you design and produce text documents that can include graphics, tables, or charts. You can then save the documents in a variety of formats, including the standardized OpenDocument format (ODF), Microsoft Word .doc format, or HTML. And you can easily export your document to the Portable Document Format (PDF)."
- **Writing scope**: "basic documents, such as memos, faxes, letters, resumes and merge documents, as well as long and complex or multi-part documents, complete with bibliographies, reference tables and indexes."
- **Authoring aids**: spellchecker, thesaurus, AutoCorrect, hyphenation; "a variety of templates for almost every purpose"; own templates via wizards.
- **Formatting model — styles**: "Use the Styles deck to create, assign and modify styles for paragraphs, individual characters, frames and pages." **Navigator** "helps you to quickly move around inside your documents, lets you look at your document in an outline view, and keeps track of the objects that you have inserted."
- **Long-document machinery**: "create various indexes and tables… define the structure and appearance"; live hyperlinks and bookmarks jump to items.
- **DTP-adjacent capabilities inside the word processor**: "LibreOffice Writer contains numerous desktop publishing and drawing tools to assist you in creating professionally styled documents, such as brochures, newsletters and invitations… multi-column layouts, frames, graphics, tables, and other objects." (Evidence that layout breadth is a capability layer of this Type, with dedicated DTP apps as the canvas-first pole.)
- **Extras**: integrated calculation function (tables with calculations); drawing tool; picture insertion (JPG/GIF etc.); Gallery clipart; Fontwork; configurable UI; drag & drop between documents.
- **Interchange posture**: native ODF position + saving to Word .doc + HTML + PDF export — the document artifact leaves the application in standard formats.

## Product C — Apple Pages

Evidence layer: A (directly observed in the official user guide TOC and two deep articles).

### Key observations

- **Template-first creation**: "All documents begin with a template—a model you can use as a starting point. You can create word-processing documents, like reports and letters, and page layout documents, like posters and newsletters."
- **THE vendor-side Type boundary, stated inside one product** ("Intro to word-processing and page layout documents"):
  - *Word-processing* documents "have a *body text* area where you type, the text flows from one page to the next, with new pages created automatically when you reach the end of the page. When you open a word-processing document (or template), you can just start typing, though you can also add images, charts, and other objects."
  - *Page layout* documents "is like a canvas that you add text boxes, images, and other objects to, then arrange the objects on the page however you like… there is no body text area; to add text you need to add a text box and type in it. New pages must be added manually."
  - The mode is a per-document setting (Document Body checkbox) and documents can be converted between the two. → The word-processor model (body-text flow with automatic pagination) vs the page-layout model (canvas + placed frames + manual pages) is a real, vendor-documented structural distinction, and the word-processing model is the Type's center.
- **Formatting model — styles**: "A paragraph style is a set of attributes—like a font size and color—that determines how the text in a paragraph looks." Uses: consistent look (Title/Body), global restyling ("change the color of the Heading style itself, and all the headings update automatically"), and **TOC generation from paragraph styles**. Preset styles + user-created styles; **overrides tracked** (asterisk + Update button next to the style name); character styles, object styles, copy/paste text styles exist; paragraph styles cannot apply inside table cells. Guide also covers font/size/color, bold/italic/underline/strikethrough, ligatures, drop caps, hyphens/dashes/quotes, capitalization.
- **Page model** (TOC): paper size and orientation, document margins, facing pages, page templates, add/rearrange/duplicate/delete **pages and sections**, table of contents, bibliography, footnotes and endnotes, headers and footers, page numbers, page background, border around a page, watermarks, custom templates.
- **Objects** (TOC): images, image galleries, shapes (draw/combine), 3D objects, lines/arrows, video and audio, record audio, tables (with cell formats, conditional highlighting, sorting, **formulas and functions in table cells**), charts, equations, bookmarks and links; object positioning (align, layer/group/lock, alignment guides, wrap, captions, shadows).
- **Writing and editing tools** (TOC): check spelling, look up words, find and replace, replace text automatically, word count/statistics, annotations view, author name and comment color, highlight text, add and print comments, **track changes**.
- **File model** (TOC): save and name a document, iCloud Drive, find/open/close, **export to Word, PDF, or another file format**, reduce file size, package files for large documents, **restore an earlier version**, move/delete, **lock a document, password-protect a document**, AirDrop/Handoff/Finder transfer, create/manage custom templates.
- **Distribution** (TOC): send a document, print a document or envelope, publish a book to Apple Books (EPUB book templates).
- **Collaboration exists but is a section, not the spine**: invite others, shared document activity, stop sharing, shared folders, **Use Box to collaborate** — Pages (the platform-native pole) has added the same collaboration layer the sibling pass recorded across the market.
- **Mail merge present** (TOC): merge fields, source files, populate and create customized documents.

## Product D — Google Docs (market anchor only)

Evidence layer: none beyond market position (official docs unreachable this pass and in the 2026-09-06 sibling pass).

- The cloud-native pole of the document-editor market; its defining structure (shared live merged document with sharing/permission machinery) is already canonicalized under the sibling Collaborative Document Editor leaf. Because official documentation was unreachable, no Google Docs claims are recorded here.

---

## Cross-product Comparison

| Structure | Word | LibreOffice Writer | Pages | Strength |
|---|---|---|---|---|
| Persistent self-contained document as unit of work | ✓ (file/document saved to desktop or OneDrive) | ✓ ("design and produce text documents", saved in file formats) | ✓ (save/name, iCloud Drive, lock, password) | B — all three |
| Direct inline editing (cursor/type/select/replace) | ✓ (documented as the basic act) | ✓ (implied by "design and produce"; menus/toolbars) | ✓ ("you can just start typing"; add and replace text) | B — all three |
| Explicit user-applied character + paragraph formatting visible while writing | ✓ (Home tab / pop-up toolbar, Format Painter) | ✓ (Styles deck + direct styling; formatting documented as part of writing) | ✓ (Format controls, sidebars, pop-up style menus) | B — all three |
| Styles system packaging formatting | ✓ (implied by hub/formatting docs; Save as template) | ✓ (paragraph/character/frame/page styles) | ✓ (paragraph/character/object styles, overrides, TOC from styles) | B — all three |
| Page-oriented document model (page setup, margins, headers/footers, page numbers, breaks) | ✓ (Pages & layouts help category) | ✓ (page styles; multi-part documents) | ✓ (paper size/margins/sections/headers-footers/page numbers/breaks) | B — all three |
| Finished-artifact output: print + fixed export | ✓ (Save & print; Edit a PDF; labels) | ✓ (PDF export; save to ODF/Word/HTML) | ✓ (print, export to Word/PDF/EPUB, Apple Books) | B — all three |
| Content objects: tables, images, shapes/charts | ✓ (Insert tab list) | ✓ (graphics, tables, charts, drawings, gallery) | ✓ (full object palette incl. 3D, audio/video) | B — all three |
| TOC / long-document machinery | ✓ (TOC learning guide; multi-part docs implied) | ✓ (indexes and tables, bibliographies, reference tables) | ✓ (TOC from styles, bibliography, footnotes) | B — all three |
| Writing aids: spell check, autocorrect, find/replace, word count | ✓ (documented across hub) | ✓ (spellchecker, AutoCorrect, thesaurus, hyphenation) | ✓ (TOC of writing/editing tools) | B — all three |
| Comments + track changes review loop | ✓ (deep documentation) | present (Writer help structure; not article-fetched this pass) | ✓ (TOC: track changes, comments, author colors) | B — Word deep; Pages present via TOC; LibreOffice present via help structure |
| Templates | ✓ (blank or template creation) | ✓ (templates + wizards) | ✓ (template chooser; custom templates) | B — all three |
| File machinery: autosave/cloud, versions, protection | ✓ (OneDrive AutoSave; toggleable) | file-based (ODF; local-first posture) | ✓ (iCloud Drive, restore earlier version, lock, password) | B — varies by storage posture |
| Mail merge / labels | ✓ (mail merge hub link; labels) | ✓ ("merge documents" in scope statement) | ✓ (mail merge TOC section) | B — all three |
| DTP-adjacent layout (columns, frames, wrap) | ✓ (newsletter columns, text wrap, page borders) | ✓ (explicit "Desktop Publishing with LibreOffice Writer" section) | ✓ (columns, linked text boxes, wrap, facing pages) | B — all three |
| Real-time co-editing | ✓ (documented; legacy clients fall back to save-merge) | not in fetched scope | ✓ (collaboration section; Box support) | B — layer added on the artifact, not the artifact itself |
| AI assistance | ✓ (Copilot in help hub) | not in fetched scope | ✓ (Apple Creator Studio AI features surfaced in guide) | Optional |
| Suite membership | office suite (Word/Excel/PowerPoint) | office suite (Writer/Calc/Impress…) | iWork family | Variant |
| Business model | subscription / perpetual heritage | free open-source | bundled with OS | Variant |

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

```text
Persistent Prose Document (self-contained artifact the author keeps)
└── Direct Inline Editing (compose & revise in place on the document surface)
    └── Explicit Text & Paragraph Formatting applied while writing
        (user-controlled, visible on the editing surface, not deferred
         to a separate rendering step)
        └── Page-shaped Finished Output
            (print-oriented pagination + print/export of a fixed artifact)
```

Four properties. Remove any one and the Type collapses into a neighbor:

- Remove the **persistent self-contained document** → an ephemeral or fragment surface (notes, scratchpads, whiteboards). The document holds both content and formatting and travels as a unit.
- Remove **direct inline editing** (the user composes/edits on the document itself) → a form/generator that produces documents from inputs (resume-builder-style rendering, document automation) — authoring, not editing.
- Remove **explicit formatting applied while writing** → a plain-text or markup-source editor (Markdown editor) or an attention-first drafting surface (distraction-free writing application), where formatting is deferred, hidden, or rendered separately.
- Remove the **page-shaped finished output** → a generic rich-text editor or note surface: no print semantics, no finished artifact leaving the application. (Rich-text components inside other applications fail this test; the artifact must be completable and portable.)

Notes on what was deliberately kept OUT of L0:

- **Single-authorship / local files** — out. The canonical form is an author-owned artifact, but cloud-stored documents with AutoSave (Word) and platform-bundled cloud documents (Pages) satisfy the core; what matters is the document-as-artifact model, not where bytes live. Collaboration is layered on top of the artifact in this Type (see Boundary 1).
- **WYSIWYG screen fidelity** — out as a requirement. The invariant is the explicit, user-controlled formatting model present on the editing surface; historically this was satisfied by visible formatting codes/commands before full on-screen fidelity existed (historical check below).
- **Styles** — out. Formatting is definitional; styles are the standard packaging of it (L1). Direct formatting remains always available in all sampled products.
- **Specific content objects (tables/images/charts), templates, spell check, track changes, comments, mail merge, macros, AI** — all standard or optional capabilities, not definitional.
- **Office-suite membership, DOCX/ODF formats, desktop deployment** — out; variants.

§24 historical / market-sample check:

- **Formatting-code-era word processors** (keyboard-driven, late-1970s/1980s class): prose document artifact ✓, inline editing ✓, explicit formatting applied via commands/codes visible in the editing surface ✓, pagination/print output ✓. Passes without WYSIWYG.
- **Regional / platform-native products** (platform-bundled editors, regional office suites): same core — pass.
- **Plain rich-text editors (TextEdit-class)**: fail L0 #4 (no page/print model, no finished-artifact production) — correctly excluded from the Type.
- **Cloud-native collaborative editors (Google Docs class)**: fail the L0 framing in its canonical form — the primary object there is a shared live merged document with sharing/permission machinery (already canonicalized as the sibling Type). Products in this family that retain a document-file model for the author (desktop Word with AutoSave, Pages before sharing) satisfy this Type's core; the drift is recorded under Boundary 1.
- The definition is not an artifact of the modern desktop-suite era.

### L1 — Common Mature Structure

Capabilities found across all sampled products (and expected by the market) that are not definitional:

- **Styles system**: paragraph styles, character styles (LibreOffice adds frame/page styles; Pages adds object styles); presets, custom styles, style updates restyling everything that uses a style, override tracking; TOC generated from styles
- **Templates**: creation from templates; saving custom templates; template choosers/galleries; wizards (LibreOffice)
- **Content objects**: tables (with formatting, and cell formulas in some products), images, shapes, charts, media, text boxes, hyperlinks, bookmarks, footnotes/endnotes, watermarks, WordArt/display text
- **Page machinery**: page setup (paper size, orientation, margins), headers/footers, page numbers, page/section breaks, multi-column text, facing pages
- **Long-document machinery**: table of contents, indexes, bibliographies, navigation/outline panes, ruler, formatting symbols
- **Writing aids**: spell check, AutoCorrect/replace-text-automatically, find & replace, thesaurus/lookup, hyphenation, word count, dictation
- **File machinery**: save/open with named file formats, import/export (PDF; DOCX/ODF/HTML/EPUB interchange), AutoSave/cloud storage, restore earlier version, document lock/password protection, package files
- **Review loop**: comments/annotations with authorship; track changes capturing proposed edits with per-author attribution; accept/reject individually, in bulk, or all; markup display controls; navigate between changes; review summaries
- **Print machinery**: print dialog with page setup, print options, labels/envelopes
- **Undo/redo, clipboard, format copying** (Format Painter / copy-paste styles)

### L2 — Variant / Optional Structure

- **Suite membership**: member of an office suite vs standalone vs OS-bundled
- **Surface strategy**: desktop-first with web/mobile companions (Word), desktop-only OSS (LibreOffice), platform-native multi-device (Pages)
- **Storage posture**: local files vs cloud drive with AutoSave vs platform cloud; per-product mixes
- **Layout breadth**: text-stream purist vs DTP-adjacent (multi-column, frames, text wrap, linked text boxes) — Pages even offers a full page-layout document mode as a per-document switch
- **Document-class machinery**: mail merge, labels/envelopes, macros/automation, equations, bibliographies/citations, master/long documents
- **Typography breadth**: bidirectional text, vertical text, CJK formatting, phonetic guides
- **Collaboration depth**: review-only → full real-time co-editing (the drift seam toward the Collaborative Document Editor; every sampled product has some form)
- **AI assistance** embedded in authoring (Copilot, platform AI features)
- **Business model**: subscription, perpetual, free open-source, OS-bundled
- **Regional/regulatory posture**: regional office suites, standardized ODF posture

### L3 — Vendor-specific Structure (research notes only)

- **Word**: ribbon tab organization (File/Home/Insert/Review); Quick Access Toolbar AutoSave toggle; OneDrive/SharePoint AutoSave coupling; Track Changes scope selector (For Everyone / Just Mine); Lock Tracking with password; markup view names (Simple/All/No/Original); balloons vs inline; Reviewing Pane; review-mode sharing that prevents disabling tracking; Format Painter; SmartArt/WordArt/3D Models/Icons; Edit a PDF; Create and print labels; Copilot; .docm macro check-out/check-in (recorded in the 2026-09-06 sibling pass)
- **Pages**: word-processing vs page-layout document types with Document Body checkbox and conversion; template chooser; paragraph-style override asterisk/Update button; TOC enabled per style; mail-merge source files; EPUB book templates and Apple Books publishing; Use Box to collaborate; AirDrop/Handoff transfer; package files for large documents; object styles; Apple Creator Studio AI features; iCloud Drive integration
- **LibreOffice**: Styles deck; Navigator (outline view + object tracking); ODF standardization posture; saving to Word .doc/HTML; Gallery clipart; Fontwork; wizards; integrated table calculations; configurable/dockable UI; multi-column/frames under "Desktop Publishing with LibreOffice Writer"

## Vendor-specific Findings (summary)

See L3. None of these enter the final document except as neutral, genericized illustrations.

## Rejected Findings

- **"WYSIWYG editing" as definitional** — rejected: the historical formatting-code era satisfies the Type without on-screen final-form fidelity; the invariant is the explicit formatting model on the editing surface, kept conceptual.
- **"Desktop application with local files" as definitional** — rejected: cloud-stored documents with AutoSave and platform cloud documents satisfy the core; the artifact model, not storage location, is what matters.
- **"Office suite membership" as definitional** — rejected: standalone and OS-bundled editors exist (Pages, LibreOffice).
- **"DOCX" (or any single format) as definitional** — rejected: ODF/DOCX/HTML/EPUB/PDF interchange documented across products; format is implementation.
- **"Templates" as definitional** — rejected: blank-document creation exists in all sampled products (Pages is template-first but supports both; Word documents both paths).
- **"Comments + track changes" as definitional** — rejected: review machinery is mature-standard (L1), not required to recognize the Type; historical single-author products pass without it. The review loop is also structurally different from CDE co-editing: the document remains the author's artifact.
- **"Collaboration" as definitional** — rejected: it is the sibling Type's defining core. Here it is a layer added to the artifact (documented in all three sampled products, but the artifact model survives its absence — historical check).
- **"Rich DTP-grade layout (frames/canvas placement)" as definitional** — rejected: text-stream-first is the Type's center; layout breadth is capability depth (Apple's own word-processing vs page-layout split is the cleanest evidence).
- **Treating Pages' page-layout mode as a second Type inside Pages** — rejected: it is a per-document mode switch inside a document-editor product; the word-processing model is the product's default and the Type's center.

## Boundary Findings

1. **vs Collaborative Document Editor (processed sibling)** — the sharpest boundary. From this side: the unit of work is an author-owned document artifact; collaboration (comments, tracked changes, even real-time co-editing) arrives as machinery layered on the artifact, and the artifact model (save/keep/export as a file) remains the spine. In the sibling Type the primary object is the shared live merged document with sharing/permission machinery as the defining structure. Microsoft's own documentation marks the seam from inside: real-time co-authoring for current clients vs "you'll have to save the document from time to time" save-merge mode for older ones (recorded in the 2026-09-06 sibling pass). The seam is porous in one direction — every sampled single-author editor has added collaboration (Word co-authoring, Pages collaboration section, Google Docs as the full pole) — but the leaf remains structurally distinct because the defining machinery (sharing model, role ladder, presence, live merge) is the sibling's core, not this Type's. **Test: remove shared access + live merge → Document Editor; make the shared live document the primary object → Collaborative Document Editor.** Consistent with the sibling pass's recorded seam ("Remove shared access → a single-user Document Editor (even if the file is in the cloud)").
2. **vs Markdown Editor (unprocessed sibling)** — the formatting model is the discriminator. In a Document Editor, character/paragraph formatting is explicit, user-controlled, and visible during writing (with styles as packaging). In a Markdown editor, the source is plain text with markup and rendering is deferred to a separate step. Remove the explicit formatting model → Markdown editor; add it back → Document Editor. Flag for the markdown-editor pass to hold this seam from its side.
3. **vs Distraction-free Writing Application (processed sibling)** — consistent with that pass's recorded boundary: a Document Editor keeps formatting and page layout continuously visible/editable during writing; the distraction-free Type defers formatting and hides chrome to preserve attention. The full-screen mode of a word processor is auxiliary; it is not the product's promise.
4. **vs Desktop Publishing / Page Layout Application (processed sibling)** — the flow model is the discriminator. Word-processing documents have a body-text area where text flows page to page with automatic pagination; page-layout documents are canvases with manually placed text boxes/frames and manual pages. Apple documents this distinction inside Pages itself; LibreOffice markets DTP tools as a capability layer of the word processor. Remove body-text flow, add frame-based canvas → Page Layout / DTP.
5. **vs Note-taking Application** — notes are fragment records in a container, optimized for capture and retrieval; a document editor produces a single, self-contained, print-shaped artifact. No page model in the note sense → notes.
6. **vs Resume Builder (processed sibling)** — the resume builder owns a structured career-document model and the rendering (the user never lays out pages); the Document Editor gives free-form authoring where the user owns content and layout. Microsoft's separate purpose-built resume-builder surface confirms the seam.
7. **vs Code Editor (processed sibling)** — program source with syntax/tooling vs prose documents with formatting/print model; a Markdown file can be edited in either, but the Types are defined by their content model and tooling.
8. **vs generic rich-text editing surfaces** — embedded rich-text fields lack the self-contained artifact, the page model, and the finished-artifact production; they are capabilities of other applications, not this Type.
9. **Directory-adjacency note** — this leaf sits next to Collaborative Document Editor, Markdown Editor, and Distraction-free Writing Application under 03.01. The research supports keeping all four separate: artifact+formatting+pages (this leaf), shared-live-merge (CDE), markup-source (Markdown), attention surface (distraction-free) are genuinely different structures, not audience variants. The CDE seam is porous toward this leaf (collaboration added to editors), so the markdown-editor and any future word-processor-alias questions should cite the formatting-model discriminator as the load-bearing test.

## Uncertainties

- Google Docs: official documentation unreachable this pass (timeout) and in the 2026-09-06 sibling pass. Treated as market anchor only; no Google-specific claims anywhere in this pass.
- LibreOffice: evidence is features-page + help-TOC level; article-level mechanics (e.g., exact style dialogs, macro support) not verified this pass — no LibreOffice macro claims made.
- Whether any major document editor ships a "pageless"/non-paginated viewing mode as a first-class alternative: not researched; no claims made. The L0 page-oriented claim rests on the three deep products' document models.
- Word version-history internals, online-template catalog scope, .docx internals: not fetched; unasserted.
- Zoho Writer / WPS Office: not fetched; market-structure mentions only (no claims).
- Exact interchange-fidelity behavior between formats (what breaks in translation): not researched; kept qualitative in the final document.

## Final Synthesis

A Document Editor is an application for authoring persistent prose documents whose defining core is: a self-contained document artifact the author creates, keeps, and revisits; direct inline editing on the document surface; an explicit, user-controlled text-and-paragraph formatting model applied while writing and visible on the editing surface; and a page-oriented document model completed by printing or exporting a fixed finished artifact. Around that core, mature products add a stable standard structure: styles and templates; content objects (tables, images, shapes, charts, hyperlinks, footnotes, headers/footers, generated tables of contents); writing aids (spell check, autocorrect, find/replace, word count, dictation); file machinery (named formats, PDF/interchange export, cloud AutoSave, version restore, protection); a review loop (comments and tracked changes with accept/reject) that passes the author-owned artifact between authors and reviewers; and print machinery. Products vary by suite membership, surface (desktop/web/mobile), storage posture (local vs cloud), layout breadth (text-stream purist vs DTP-adjacent), long-document machinery, typography breadth, collaboration depth, and business model. The type is not defined by the modern desktop-suite era: a keyboard-driven formatting-code word processor satisfies the core without WYSIWYG, and a file-based open-source editor satisfies it without cloud or suite. The sharpest boundary is against the Collaborative Document Editor — whose defining structure (shared live merged document) appears here only as an added layer on the author-owned artifact — and against the Markdown Editor, whose formatting is deferred to a rendering step rather than explicit and visible during writing.
