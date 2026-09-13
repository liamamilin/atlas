# Research Notes — PDF / Document Reader

## Research Goal

Understand the PDF / Document Reader as an Application Type: what the central object ("a document") is, how documents enter the reading environment, what "reading" means when the document has a fixed layout, what the interaction machinery around a rendered page is (navigation, zoom, search, selection), which in-document work actions (annotation, form filling, signing) are part of the reading experience versus a separate editing product, and where the Type is bounded against E-book Reader, Academic Paper Reader, E-book Library Application, Image Viewer, File Manager, Document Editor, and Read-it-later Application.

## Initial Boundary

Working hypothesis before research:

- The core purpose is **presenting an existing document file for human reading**, with the file's own layout preserved — as opposed to re-flowing content for comfort (E-book Reader) or authoring/changing the document's content (Document Editor).
- PDF is the canonical and near-universal format; the Type also historically covers sibling fixed-layout document formats (PostScript, DjVu, XPS).
- Suspected confusions: E-book Reader (processed sibling — book semantics), Academic Paper Reader (processed sibling — bibliographic library), Image Viewer (single raster images), File Manager (delegates rendering), Document Editor (authoring), web browsers (embed viewers), Read-it-later (clipped articles).
- Sibling passes pre-hung seams naming this leaf: e-book-reader ("fixed-layout page rendering of arbitrary documents is the center → PDF/Document Reader"), academic-paper-reader ("remove bibliographic identity + library → PDF / Document Reader"), e-book-library-application ("a PDF reader with no library semantics is the other type"), file-manager ("those render content of one file").
- Unknowns: whether annotation/form-filling is definitional or mature-common; how annotations persist (in-file vs sidecar vs copy); how the reader/editor product split is drawn in the market; format-breadth patterns.

## Research Questions

1. What is the unit of work — the document file, the page, or the reading session?
2. How do documents enter the application, and does the app hold any collection semantics?
3. What does faithful fixed-layout rendering imply for the interaction model (zoom, fit, view modes)?
4. What navigation machinery is standard: paging/scrolling, page jump, thumbnails, outline/TOC, links, bookmarks?
5. What content interaction exists: text selection/copy, search — and what happens when the text layer is absent?
6. Which document-work actions sit inside the reading experience: annotation, form filling, signing? How do they persist?
7. What protection semantics exist: open passwords, author-set permissions (print/copy restrictions)?
8. Where is the line between reading and editing/morganizing (page combine/reorder/delete, content editing, conversion)?
9. How do distribution models shape the product: platform-native bundled viewer, free incumbent with paid editor sibling, desktop-environment viewer, enterprise-deployed reader?
10. Does the definition survive historical samples (1990s-era viewers, platform-native viewers, minimal modern viewers)?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

| Product | Pole | Tier reached |
|---|---|---|
| Apple Preview | platform-native bundled document/image viewer | Tier-1 (official user guide, multiple pages fetched) |
| Evince (GNOME Document Viewer) | free-software desktop-environment document viewer, minimal philosophy | Tier-1 (official help, multiple pages fetched) |
| Okular (KDE) | free-software power-user "universal document viewer", annotation-rich | Tier-2 (official product site) |
| Foxit PDF Reader | cross-platform commercial reader with paid Editor sibling and enterprise deployment | Tier-2 (official product page + FAQ) |
| Adobe Acrobat Reader | the incumbent free reader from the PDF format's creator | **Unreachable** — market anchor only (see Sources) |

## Sources

Accessed 2026-09-08 (research date):

- Apple — Preview User Guide for Mac: welcome/TOC (`https://support.apple.com/guide/preview/welcome/mac`), "View PDFs and images" (`.../view-pdfs-and-images-prvw11470/mac`), "If you can't select or copy text in a PDF" (`.../if-you-cant-select-or-copy-text-in-a-pdf-prvw1499/mac`). Directly fetched; evidence layer A.
- GNOME — Evince help: index (`https://help.gnome.org/users/evince/stable/`), "Moving around a document" (`.../movingaround.html`), "Supported formats" (`.../formats.html`). Directly fetched; evidence layer A. Additional page titles/subtitles (annotations save, forms saving, editing FAQ, reload behavior, print restrictions) recorded from the fetched index page.
- KDE — Okular product site (`https://okular.kde.org/`). Directly fetched; evidence layer A for positioning/features-at-a-glance, B for operational depth (docs.kde.org article URL returned 404; not retried).
- Foxit — PDF Reader product page (`https://www.foxit.com/pdf-reader/`) including the vendor's own reader/viewer FAQ. Directly fetched; evidence layer A for positioning/feature framing; FAQ is vendor marketing language, used only as market-terminology evidence.
- Adobe — `helpx.adobe.com/acrobat/using.html`, `www.adobe.com/acrobat/pdf-reader.html`, `helpx.adobe.com/acrobat/using/acrobat-user-guide.html`: **all three requests timed out (2026-09-08)**. Per source-access discipline the source was abandoned after repeated failures. Adobe Acrobat Reader is therefore held as a **market anchor** (the best-known free reader, published by the PDF format's creator) with **no product-specific capability claims** anywhere in this research or the final document.

Contextual (not fetched, not asserted as product fact): the historical lineage of the Type (early-1990s PDF viewers, PostScript previewers, platform-native viewers) is used only at the structural level for the historical check; no precise dates, version features, or defaults are asserted from memory.

## Product A — Apple Preview

### Key observations (layer A unless noted)

- Handles **PDFs and images in one application**; the user guide's top-level sections are "View PDFs or images", "Edit PDFs", "Edit images", "Manage PDFs or images", "Print PDFs and images". (Also the strongest boundary straddle evidence for the Image Viewer seam.)
- Opening: "Open PDFs and images" is its own guide section; multi-page PDFs show **thumbnails of all pages in the sidebar**.
- Viewing machinery: **Thumbnails / Contact Sheet** sidebar; **Table of Contents sidebar "if it has one"**; view modes **Continuous Scroll / Single Page / Two Pages**; swipe/scroll paging; **Go to Page**; previous/next page buttons (with pressure-accelerated paging on Force Touch trackpads — vendor detail).
- Zoom machinery: Zoom In/Out, **Actual Size**, **Zoom to Selection** (via rectangular selection), a **Scale percentage field** in the toolbar, and a **Magnifier** tool that magnifies an area under the pointer.
- Content interaction: "Find text in PDFs", "Select and copy text in a PDF", "Interact with text in a photo" (Live Text — OCR-adjacent), "Bookmark PDF pages", "View information about PDFs and images" (Inspector), "Display a PDF as a slideshow".
- Document work under "Edit PDFs": **Fill out and sign PDF forms** (with AutoFill), **Highlight, underline, and strike out text**, **Add notes and speech bubbles**, **Annotate a PDF** (markup toolbar), plus page-level organization: **Combine PDFs**, **Add, delete, or move PDF pages**, **Crop or rotate a PDF**, **Add effects**.
- Management: Save, Revert, Copy, Lock, Export, **Password-protect a PDF**, Reduce size; Share; Print.
- Troubleshooting evidence (high value): "If you can't select or copy text in a PDF" — causes documented: the Text Selection tool isn't active, **or the PDF requires a password before text can be selected/copied**. Confirms both the text-layer concept and author-set permission enforcement. Another troubleshooting page: "If Go to Page shows the wrong page of a PDF" (page-number vs physical-page mismatch).
- Image-side capabilities (background removal, conversion, color profiles) sit beside the PDF side — platform-native bundling of two sibling Types in one app.

## Product B — Evince (GNOME Document Viewer)

### Key observations (layer A unless noted)

- Self-label: **"Document Viewer"**. Supported formats documented explicitly: **Comic Book Archive (.cb7/.cbr/.cbt/.cbz), DVI, DjVu, OXPS/XPS, PDF, PostScript** — "Support for a format is called a backend", installable per format. (Format breadth + plugin/backend architecture directly documented.)
- Navigation ("Moving around a document"): mouse-wheel scrolling, **Autoscroll** mode, scrollbar, arrow keys, grab-and-drag; page flipping via Ctrl+PageUp/Down, **"Select Page" number entry**, Ctrl+Home/End for start/end, Shift+PageUp/Down to move ten pages; **Continuous mode** vs default one-page-at-a-time.
- Side pane: **preview of all pages**; **Outline** button shows the document's index/TOC — with the explicit note that **"Most documents don't use this feature"** (outline is optional document metadata, not a guaranteed structure).
- Zoom: percentage selector, Ctrl+scroll, **Fit Page**, **Fit Width**, fullscreen; **in-document links may change the zoom level** (blockable via the `allow-links-change-zoom` setting — vendor detail, layer A as a documented setting).
- Reading documents section: "Find text in a document", "Open a document", "Password-protected documents".
- Annotations section: adding, navigation, bookmarks, removing — and two structural facts: **"Annotations can only be added to PDF files"** and **"Save a copy of an annotated PDF — How to save your annotations"** (annotation persistence via explicit save-as-copy; PDF-specific annotation support).
- Interactive forms: "Forms — Working with fillable forms"; **"Saving a form — Make sure you save the form, otherwise all of the information you entered will be lost"** (form input is transient until saved).
- Printing section includes **"I can't print a document — The author may have put printing restrictions on the document"** (author-set permission enforcement) and booklet printing.
- FAQ (viewer/editor boundary, direct): **"Can I edit documents in Evince? — You can't use Evince to edit files."** Also: "Why didn't the text I selected copy properly?" (text-layer extraction imperfections) and **"Why does the document keep reloading? — Your document will be automatically reloaded if another program changes it while you're viewing it"** (the reader views a live file on disk).
- Tips: convert to PDF/PostScript/SVG **by "printing" to a file**; invert colors; command line can open files at specific pages in various modes.
- SyncTeX section: round-trip synchronization with LaTeX editors (scholarly adjacency — the same document-reading machinery serves the paper-reading world).

## Product C — Okular (KDE)

### Key observations

- Self-label: **"The Universal Document Viewer"**; "read PDF documents, comics and EPub books, browse images, visualize Markdown documents, and much more". Format table: **PDF, EPub, DjVu, MD for documents; JPEG, PNG, GIF, TIFF, WebP for images; CBR, CBZ for comics**. (Layer A for the list; layer B for operational depth — docs article 404'd, not retried.)
- Mode-based interaction model: **Annotation mode** (inline and popup notes, highlight, underline, own text), **Selection mode** (text, area, and **table** selection for copy/paste), **Magnifier mode**.
- Panels: **Thumbnails panel** ("browse graphically the part of the document you were looking for") and **Content panel** ("auto renders a table of contents for a document").
- Digital signatures: view and **verify** signatures embedded in PDFs, check validity, **detect modifications since signing**, and **sign PDFs** ("First-class Signature Support").
- Positioning extras: free software (GPLv2+), privacy policy, Blue Angel resource-efficiency ecolabel — product-philosophy framing, not Type structure.

## Product D — Foxit PDF Reader

### Key observations (layer A for positioning/framing)

- Self-positioning: **"View, annotate, form fill, and sign PDF across desktop, mobile, and web"**; product family blurb: "Read, annotate, and collaborate on PDFs with a fast, free PDF reader."
- Feature blocks: **Read and Print** ("Leverage existing forms and workflows with standard PDF (Acroforms) and XFA (XML Form Architecture) form filling"); **Read PDF Anywhere** (Windows, macOS, iOS, Android, web — "consistent reading experience"); **Collaborate and Share** (cloud storage and enterprise CMS integration, **shared reviews**, annotation tools, file attachments as comments); **Protect and Sign** (handwritten signatures, eSignature, digital-signature verification, Trust Manager/Safe Mode, ASLR & DEP, Disable JavaScript, Security Warning Dialogs); **AI Assistant** (ChatGPT integration); **Customize and Deploy** (Group Policy, SCUP catalog, XML configuration, MSI deployment).
- **The market's reader/editor split, directly evidenced**: Foxit ships a free **PDF Reader** whose scope is view/annotate/form/sign/collaborate, and sells **PDF Editor** as the separate product for "creating, editing, converting, signing, and securely managing PDFs". The reader's FAQ states the vendor's own terminology: a reader "usually offers extra features like editing, signing, and annotating, while a viewer mainly focuses on displaying the document" — marketing language, recorded as market-terminology evidence only (and internally inconsistent with the vendor's own reader/editor product split, which is the stronger structural fact).
- Enterprise packaging: "Enterprise Packaging" registration path; mass-deployment tooling — the enterprise-deployed-reader pole.

## Cross-product Comparison

| Dimension | Apple Preview | Evince | Okular | Foxit PDF Reader |
|---|---|---|---|---|
| Self-label | Preview (PDF+image viewer bundled with macOS) | "Document Viewer" | "The Universal Document Viewer" | "PDF Reader" |
| Open surface | Open dialog; part of platform (opens from Finder/mail) | Open dialog, command line | Open dialog | Desktop/mobile/web apps; enterprise deployment |
| Formats | PDF + images (HEIC/JPEG/PNG/TIFF/GIF...) | PDF, PostScript, DjVu, XPS/OXPS, DVI, comics (backend per format) | PDF, EPub, DjVu, MD, images, comics | PDF (AcroForms + XFA); cross-platform |
| Page navigation | Scroll/paging, Go to Page, prev/next | Scroll, page entry, start/end, ±10 pages, Continuous vs single-page | Thumbnails panel | Documented at feature level |
| Thumbnails | Thumbnails/Contact Sheet sidebar | Side pane page previews | Thumbnails panel | Feature-level |
| Outline/TOC | TOC sidebar "if it has one" | Outline side pane; "most documents don't use this feature" | Content panel auto-renders TOC | — |
| View modes | Continuous Scroll / Single Page / Two Pages | Continuous / Dual ("like in a book") | — (feature-level) | — |
| Zoom | Zoom in/out, Actual Size, Zoom to Selection, Scale %, Magnifier | Percentage, Fit Page, Fit Width, fullscreen | Magnifier mode | — |
| Search | Find text in PDFs | Find text in a document | — (selection/copy documented) | — |
| Text layer handling | Selection/copy; troubleshooting for missing text layer & password-gated copy | Selection/copy; "copies improperly" FAQ; annotations PDF-only | Text/area/table selection | AcroForm/XFA form filling |
| Annotations | Highlight/underline/strike, notes, speech bubbles, markup toolbar | Add/navigate/remove; **save a copy of an annotated PDF** | Annotation mode: inline/popup notes, highlight, underline, text | Highlight, sticky notes, attachments-as-comments, shared reviews |
| Forms | Fill out and sign (AutoFill) | Fill; **save or lose input** | — | AcroForms + XFA |
| Signatures | Sign forms (handwritten signature) | — | View/verify/detect-modification/sign digital signatures | Handwritten + eSignature + digital verification |
| Page organization | Combine, add/delete/move pages, crop/rotate | Explicitly **cannot edit documents** | — | In Editor product, not Reader |
| Print | Print PDFs and images | Print, booklet, **author print restrictions** | — | Read and Print |
| Protection | Password to open; password before copy | Password-protected documents; print restrictions | Signature validity/modification detection | Protected View, JS disable, trust tooling |
| Collection semantics | None (file-based; platform recents) | None | None | None |
| Distribution | Platform-native, bundled | Desktop-environment free software | Desktop-environment free software | Free reader; paid Editor sibling; enterprise packaging |

Cross-product commonalities (layer B, all four sampled products unless noted):

- The unit is always **an opened document file**; no sampled product imposes collection/curation semantics. (Files land in the app from the outside.)
- All render **fixed pages faithfully** and give **page-sequenced movement** plus **scale adjustment** (zoom/fit) as first-class machinery.
- Text-layer-dependent interaction (search, selection/copy) is present across the sample, with documented failure modes when the layer is absent or permission-gated.
- Annotation and form-filling are present in all four (layer B) but with materially different depth — from Evince's save-a-copy markup to Foxit's shared-review collaboration — supporting "common mature structure, not defining".
- The **reader/editor split** is structural in the market: Evince states it cannot edit; Foxit splits Reader from Editor as separate products; Preview's page-level organization is the exception that shows the seam is a packaging choice (layer A), not a Type law.
- Protection semantics are enforced, not granted: open passwords, author-set operation restrictions (print/copy), signature verification.

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

Three jointly-held structures; the Type is recognizable only with all three:

1. **The externally-obtained document as the unit of reading.** The app opens whole document files of arbitrary provenance and subject matter — contracts, manuals, statements, papers, forms, brochures — with no authoring relationship to the content and no collection/curation semantics of its own. Remove → the product is an authoring tool (content editing) or a content service (library/store/feed), not a reader.
2. **Faithful fixed-layout page rendering.** Pages are presented as fixed compositions — text, images, and vector graphics placed at exact positions with pagination determined by the file — preserved across devices and platforms. The app's obligation is fidelity to the file as authored, not re-presentation for comfort. Remove → the product re-lays-out content (e-book reader) or edits content (editor).
3. **Movement through the paginated document.** Page-sequenced navigation (scroll/paging between pages, jump to a page/position, page thumbnails) and viewing-scale adjustment (zoom, fit-to-window/page/width) — the machinery that fixed pagination makes necessary, since the layout does not adapt to the window. Remove → a static page image; a single-page snapshot view is not a document reader.

Jointly-held is load-bearing: rendering without movement = poster/image display; movement without fidelity = reflowing reading surface (sibling Type); all machinery without the document file = content web/app surface.

### L1 — Common Mature Structure

Present across the researched sample; expected in any modern product but not required to recognize the Type:

- text-layer search (find in document)
- thumbnails panel
- outline/table-of-contents navigation **when the document carries one** (optional document metadata)
- text selection and copy
- reading modes (single page / continuous / two-page spread)
- annotations: highlight/underline, notes, drawing — persisted into the file or saved as a copy (mechanics vary by product)
- form filling (interactive PDF forms)
- printing (page ranges; booklet printing in some)
- document information/metadata view
- user bookmarks within a document
- protected-document handling (open password; enforced author permissions)
- recent-documents recall

### L2 — Variant / Optional Structure

Depends on segment, platform, business model, deployment:

- format breadth beyond PDF (PostScript, DjVu, XPS/OXPS, DVI, comics archives, EPUB, images — backend architecture in some products)
- page-level organization (combine, add/delete/move, crop/rotate) — packaging choice; the pure-reader pole excludes it
- digital signatures: verification only, or also creation
- security hardening for untrusted documents (protected view, script disabling, trust management) — enterprise posture
- enterprise deployment machinery (MSI/GPO-class tooling)
- collaboration over annotations (shared reviews, comment attachments)
- OCR/text-recognition affordances for scanned documents
- conversion/export (save-as, export, print-to-file)
- presentation modes (slideshow/fullscreen), accessibility aids (magnifier, color inversion)
- round-trips with authoring tools (SyncTeX-class editor synchronization)
- embedded/browser viewing surfaces; mobile form factors
- AI assistance over document content (era-current)

### L3 — Vendor-specific (research notes only, not in final document)

- Apple Preview: Force Touch pressure-accelerated paging, AutoFill for forms, x-help-action deep links, Live Text in photos, HDR image display, window background color, slideshow mode.
- Evince: `allow-links-change-zoom` gsetting, backend-package error handling, autoscroll/grab-drag specifics, SyncTeX implementation.
- Okular: Blue Angel ecolabel, table-selection mode, privacy-policy framing.
- Foxit: Trust Manager/Safe Mode naming, ASLR/DEP, SCUP catalog, XML configuration, ChatGPT integration, Salesforce/Teams integration claims.
- Adobe: nothing asserted — unreachable this pass.

## Vendor-specific Findings

- The **reader-with-paid-editor-sibling** packaging (Foxit-documented; Adobe-class incumbents commonly cited at market level) is a business-model pattern, not Type structure. The pure-viewer pole (Evince's "you can't edit files") and the platform-bundled everything-viewer pole (Preview's page organization inside the same app) prove the packaging varies without changing the Type.
- Platform-native bundling can merge two sibling Types in one app (Preview: documents + images). The Type boundary lives at the capability level, not the app-icon level.
- Vendor terminology ("reader" vs "viewer") is inconsistent in the market — one vendor's own FAQ draws the line differently than its own product split. The Atlas documents the Type, not the label war.

## Boundary Findings

- **vs E-book Reader** (processed sibling; their flag discharged from this side): RATIFIED as recorded there — the seam is presentation semantics, not file formats. This Type centers faithful fixed-layout rendering of arbitrary documents; the sibling centers book-reading semantics (position life per book, comfort re-layout of reflowable text). Content breadth overlaps (sampled products on both sides open each other's formats: Okular opens EPUB; sibling readers open PDFs). Both documents keep the rule of thumb.
- **vs Academic Paper Reader** (processed sibling; their seam confirmed from this side): remove bibliographic identity and the persistent scholarly library → this Type remains. The paper reader embeds or delegates the rendering surface (their Zotero observation); this Type has no bibliographic object model. Machinery overlaps (annotation on long-form text; SyncTeX-class editor round-trips are this Type's optional layer).
- **vs E-book Library Application** (processed sibling; their seam confirmed): no acquisition/organization/curation semantics here; a PDF inside a book library is a format instance, a PDF reader is not a library.
- **vs Image Viewer**: single raster images vs multi-page paginated documents with text layers and document semantics (forms, permissions, print). Straddle documented: Preview bundles both poles in one app; Okular lists image browsing as content breadth. For a single-page scanned PDF the two Types nearly coincide — the seam is document semantics, not the raster/fixed-layout distinction alone.
- **vs File Manager** (processed sibling; their seam confirmed): the file manager presents metadata/structure and delegates content rendering to viewer capability; this Type is that rendering surface.
- **vs Document Editor / PDF Editor**: reading vs authoring. Direct evidence: Evince FAQ ("You can't use Evince to edit files"); Foxit's product split (Reader vs Editor). In-reading markup (annotation) is layering on the document, not changing its content; page-level organization is the gray zone — present in some readers (Preview), absent in the pure-reader pole, and owned by editor products in the commercial market. Held as optional/variant, never definitional.
- **vs Read-it-later Application**: clipped web articles in a reading queue vs whole document files; no collection/queue semantics here.
- **vs Web Browser**: browsers embed PDF viewing as a capability; the standalone Type's reason to exist is document-grade machinery (forms, signatures, annotation persistence, print fidelity, protection handling) beyond the embedded surface. No conflict with the browser leaf.
- **vs Desktop Publishing / Page Layout / Word Processing Types**: those produce documents; this Type consumes whatever it is given, author-agnostic.

### "Remove X → another Type" judgments

- Remove fixed-layout fidelity (re-layout for comfort) → E-book Reader.
- Remove the document file; keep a reading surface fed by clipped web content → Read-it-later Application.
- Remove content-agnosticism; add bibliographic identity + scholarly library → Academic Paper Reader.
- Remove multi-page document semantics (single image rendering) → Image Viewer (adjacent; Preview-class bundling straddles).
- Remove rendering delegation boundary; keep metadata/structure → File Manager.
- Add content authoring → Document Editor / PDF Editor (different Type; market splits products accordingly).

## Historical / Market-Sample Check

- The definition is deliberately free of annotation, form-filling, search-UI, signature, cloud, and AI requirements. The Type's own historical root — the read-only PDF viewer of the early 1990s and PostScript previewers before it — satisfies all three L0 legs (open file, render fixed pages, move and scale). A read-only viewer without markup remains fully inside the Type; therefore markup is mature-common, not definitional.
- Platform-native viewers (Preview-class), desktop-environment viewers (Evince/Okular-class), and regional/minimal viewers all satisfy the core without any specific format breadth, deployment, or business model.
- Scan-heavy (image-only) and text-heavy documents both sit inside the Type; the text layer is a property a given document may or may not have, not a property of the Type.
- No era-, region-, or vendor-specific capability was admitted to the defining core.

## Uncertainties

- **Adobe Acrobat Reader was unreachable** (three timeouts on official surfaces, 2026-09-08). The incumbent is held as a market anchor only; no Adobe-specific feature, packaging, or default is asserted anywhere. The freemium reader/editor pattern is anchored on Foxit's documented split instead.
- Okular operational depth rests on the product page (docs article 404; not retried) — its annotation/signature capabilities are asserted at feature-announcement strength, not workflow depth.
- Annotation persistence mechanics (written into the file vs sidecar vs explicit save-as-copy) are evidenced in Evince's explicit save-a-copy model; the full market spread of persistence mechanisms is not exhaustively mapped and is described conceptually in the final document.
- Numeric limits (file size, page count, form field counts) were not researched and are not asserted.
- Preview's exact image/PDF capability split by macOS version is version-dependent; only the documented guide structure is used.

## Final Synthesis

A PDF / Document Reader is the application that takes a document file someone else produced and makes it readable: it opens the whole file regardless of subject matter, renders its fixed pages faithfully (the layout, pagination, and composition travel with the file, not with the app), and moves the reader through the document — page by page or continuously, by thumbnails, outline, or page number, at whatever scale the page demands. Around that core, mature products add the text layer's affordances (search, selection/copy), in-document work (annotation, form filling, signatures), printing, protection handling, and — depending on packaging — page organization, format breadth beyond PDF, enterprise hardening, and collaboration.

The Type's identity is the fidelity obligation: the reader presents the document as it is; re-laying-out content for comfort belongs to the e-book reader, changing content belongs to the editor, organizing collections belongs to the library types, and discovering/holding documents belongs elsewhere entirely. The document reader begins where the file arrives and ends when the reading — and the markup, form, or signature it produced — is saved back out.
