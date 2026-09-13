# PDF / Document Reader

## Overview

A **PDF / Document Reader** is an application for reading document files produced elsewhere: it opens a whole document — regardless of subject matter or origin — renders its pages faithfully in the layout the file defines, and lets the reader move through the document and interact with its content without changing what the document *is*.

The defining core is small:

```text
Document file from an external source
└── Faithful fixed-layout page rendering
    └── Movement through the paginated document
        (paging, jumping, scale adjustment)
```

Everything else commonly associated with PDF applications — annotation, form filling, digital signatures, text search, page reorganization, enterprise security tooling, AI assistance — is widespread in current products but is not what makes the product a document reader. The Type's historical root is the plain read-only viewer, and a viewer with none of the modern machinery remains fully inside the Type.

When the center of gravity shifts — re-laying-out content for reading comfort, authoring or editing the document's content, curating a collection of books or papers — the product has drifted toward a different Application Type (E-book Reader, Document Editor, E-book Library, Academic Paper Reader).

## Users & Context

The user is, in principle, anyone — this is one of the most universally installed application categories. What all uses share is the situation: **a document file arrives from elsewhere** (a download, an email attachment, a scan, an enterprise repository, a colleague) and must be read, checked, filled in, or marked up.

Typical situations:

- a consumer reading a statement, manual, ticket, or contract they were sent
- an employee reviewing a report, specification, or policy and commenting on it
- a form-filer completing a tax, application, or administrative form
- a reviewer marking up a draft or returning a signed document
- a student or researcher reading papers distributed as PDFs

The reader is deliberately uninvolved in where documents come from and where they belong: it has no store, no feed, no library. Its job starts when the file exists and ends when the reading — and any markup, form data, or signature it produced — is saved back out.

## Core Model

### The Defining Core

```text
Document file from an external source
└── Faithful fixed-layout page rendering
    └── Movement through the paginated document
        (paging, jumping, scale adjustment)
```

Three properties. If any one is removed, the product is no longer recognizable as a document reader:

- **The externally-obtained document as the unit of reading.** The application opens whole document files of arbitrary provenance and content — invoices, manuals, papers, forms, brochures. It holds no authoring relationship to the content and no collection semantics of its own. Without this, the product is an authoring tool or a content service, not a reader.
- **Faithful fixed-layout page rendering.** Pages are presented as fixed compositions — text, images, and graphics placed at exact positions, with pagination determined by the file itself. The same file looks the same everywhere; the application's obligation is fidelity to the file as authored, not re-presentation for comfort. Without this, the product re-lays-out content (e-book reader) or changes content (editor).
- **Movement through the paginated document.** Because the layout is fixed and does not adapt to the window, reading requires machinery to move: scrolling and paging between pages, jumping to a page or position, and adjusting viewing scale (zoom, fit-to-window/page/width). Without this, the product is a static page image.

### Capabilities Shared by Mature Products

A typical modern document reader carries most of the following. They are not what makes the product a reader, but they make reading documents practical:

- **Text-layer interaction** — search across the document, and selection and copying of text. These depend on the document carrying a machine-readable text layer (see Important Rules).
- **Page thumbnails** — a sidebar of miniature pages for graphical navigation.
- **Outline / table of contents** — navigable chapter structure *when the document carries one*; the outline is optional metadata inside the file, not something the reader invents.
- **Reading modes** — single page, continuous scroll, or two-page spread.
- **Annotations** — highlights, underlines, notes, drawings layered on the page and persisted with the document (written into the file, or saved as a marked-up copy, depending on the product).
- **Form filling** — completing interactive form fields embedded in the document; input is transient until saved.
- **Signatures** — from adding a handwritten signature to form fields up to verifying cryptographic digital signatures, depending on the product.
- **Printing** — the paper counterpart of the rendered page, with page-range and layout options.
- **Document information** — metadata and properties of the opened file.
- **Protected-document handling** — opening password-protected files and enforcing author-set restrictions.
- **Recall** — a list of recently opened documents, so yesterday's file is one click away.

### One Structure, Many Implementations

The Core Model is conceptual. Products realize it differently:

```text
Concept:      Externally-obtained document
Realizations: opened via file dialog, e-mail attachment, download,
              platform integration, or enterprise repository;
              some products bundle it with sibling viewing (images)

Concept:      Faithful fixed rendering
Realizations: PDF as the near-universal format; format breadth varies
              (PostScript, DjVu, XPS, comics archives, EPUB, images)

Concept:      Movement & scale
Realizations: continuous vs single-page modes, thumbnails, outline panel,
              zoom percentages, fit-page/fit-width, magnifiers
```

How much capability is layered on the core is a packaging decision, not a Type boundary: one product ships page reorganization inside the same reading app, another explicitly refuses to edit anything, a third splits the free reader from a paid editor product — all three remain the same Type.

## How It Works

### Open a document

```text
The file arrives (download, attachment, scan, shared drive)
→ open it in the reader
→ if the document is protected, provide the password
→ the document renders at fit-to-window scale, page 1
```

There is no setup, no account, no content selection. The reader's world begins at the file.

### Read and move through the document

```text
Scroll or page through
→ jump: click a thumbnail, follow the outline, type a page number
→ adjust scale: zoom, fit page/width, magnify a region
→ switch reading mode (single page / continuous / spread) if wanted
→ follow links embedded in the document
```

Movement is the daily loop. On long documents the thumbnails panel and outline serve as the map; the page number and search serve as the address.

### Interact with the content

```text
Search for a word or phrase
→ select and copy text (when a text layer exists)
→ optionally annotate: highlight, underline, add notes or drawings
→ optionally fill form fields embedded in the document
→ optionally sign
```

These interactions layer *on* the document; they do not rewrite it.

### Persist and output

```text
Save — annotations and form data go back into the file,
       or into a marked-up copy (product-dependent)
→ or export / convert to another format
→ or print
→ or share the document onward
```

Unsaved form input and unsaved markup are transient: products that persist annotations via an explicit "save a copy" step lose nothing until that step, but also keep nothing before it.

### Capability tiers

**Defining core** — without these, not a document reader:

- externally-obtained document file as the unit
- faithful fixed-layout page rendering
- movement through the paginated document (paging, jumping, scale adjustment)

**Standard capabilities** — present in most modern products:

- text search, text selection/copy
- thumbnails, outline navigation
- reading modes
- annotation, form filling, signature support (depth varies widely)
- printing, document info, protected-file handling, recent documents

**Common variants / optional** — depend on segment and packaging:

- format breadth beyond PDF
- page-level organization (combine, reorder, delete, rotate, crop)
- digital-signature creation and verification; security hardening for untrusted files
- enterprise deployment and configuration machinery
- collaboration over annotations (shared review rounds)
- conversion/export, presentation modes, accessibility aids
- authoring-tool round-trips, AI assistance over document content

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Document canvas

The page surface — the reason the application exists.

- the current page rendered at the chosen scale, centered in the window
- primary actions: scroll, page forward/back, select text, follow links, place annotations, click form fields

### Navigation sidebar

The document's map.

- page thumbnails (and/or an outline / table-of-contents tab when the document has one)
- primary actions: jump to a page or section, see the document's structure at a glance

### Toolbar / view controls

Scale and mode machinery.

- zoom in/out, zoom percentage, fit page / fit width, actual size, magnifier
- reading-mode switches (single page / continuous / two-page)
- page-number entry to jump directly

### Find bar

Search across the document's text layer.

- query entry, result count and navigation, on-page highlighting

### Markup / annotation tools

The in-document work surface.

- highlight, underline, strike-through, notes, drawing tools; form-field highlighting; signature placement

### Document info / protection

The file's own facts and constraints.

- metadata, encryption status, signature validity where supported; password entry for protected files

### Output surfaces

- print dialog (page ranges, layout options), export/save-as, share

## Important Rules / Behaviors

### Fidelity is the obligation

The reader renders what the file says. It does not re-flow text to fit the window, does not re-typeface for comfort, does not "improve" the layout. Everything that changes presentation rather than scale belongs to other Types. This is the structural contrast with e-book reading, where the presentation is the app's to optimize.

### The text layer is not guaranteed

A PDF's pages may be true text or may be scanned images. When there is no text layer, search, selection, and copy do not work — a failure mode documented in mainstream products' own troubleshooting guides. Text recognition features in some products exist precisely to bridge this gap; the base behavior is: **no text layer, no text interaction**.

### Documents carry permissions; readers enforce them

An author can protect a document: a password to open it, and restrictions on printing or copying content. The reader enforces these — it can refuse to print a restricted document or require a password before text can be copied. The reader never grants rights the file does not carry.

### Markup and form data are changes to a copy

Annotation and form input modify the opened document (or a copy of it). Persistence mechanics differ — some products write back into the file, some require an explicit save-as-copy step — but in all cases unsaved work is transient. A filled form that is not saved is lost.

### The outline is the document's, not the app's

A table of contents exists only if the authoring tool put one in the file. Most documents carry none; the reader must remain fully usable through thumbnails, page numbers, and search alone.

### The file is live

The reader views a file that other programs may change while it is open; products commonly reload the document when the file changes underneath. The reader is a window onto the file, not a container that owns it.

### Reading is not editing

The line the market itself maintains: readers present, mark up, fill, and sign; they do not rewrite the document's content. Products that do both split the capability into a separate editor product or explicitly disclaim editing. Page-level organization (combining, reordering, deleting pages) is the gray zone — offered by some readers as a convenience, owned by editors as a job — and is treated here as optional, never defining.

## Variants

Common forms the Type takes in the market:

- **platform-native bundled viewer** — shipped with the operating system, often bundling the neighboring image-viewing capability, deeply integrated with platform services (e.g. Preview on macOS)
- **free incumbent reader with a paid editor sibling** — the commercial pattern in which the reader is free and broad, while content creation and heavy manipulation are sold as a separate editor product (e.g. Foxit PDF Reader beside Foxit PDF Editor)
- **desktop-environment document viewer** — free-software, minimalist reading-first products ("document viewer", "universal document viewer"), often with unusually broad format breadth via per-format support modules (e.g. Evince, Okular)
- **enterprise-deployed reader** — hardened against untrusted documents (protected view, script disabling), centrally deployable and configurable across an organization
- **mobile-first readers** — phone/tablet surfaces with touch navigation and stylus markup
- **embedded viewers** — PDF viewing built into browsers and other applications; document-grade machinery (forms, signatures, annotation persistence, print fidelity) is what standalone readers add beyond the embedded surface
- **premium consumer readers** — paid consumer products competing on annotation depth, smoothness, and cross-device continuity

A variant remains a **Variant** as long as the defining core applies. When a product's center moves to content creation or collection management, it belongs to a different Type regardless of the "PDF" in its name.

## Related Application Types

| Application Type | Distinction |
|---|---|
| E-book Reader | re-lays-out content for reading comfort and treats the file as a book (position life, chapters, print-page mapping); this Type renders fixed pages of arbitrary documents faithfully — the seam is presentation semantics, not file format (each side commonly opens the other's formats as content breadth) |
| Academic Paper Reader | adds bibliographic identity and a persistent scholarly library around paper reading; remove those and this Type remains. A paper reader may embed or delegate to a document reader as its rendering surface |
| E-book Library Application | acquires, organizes, and curates a book collection; this Type holds no collection semantics — a PDF inside a library is a format, not a reading environment |
| Image Viewer | renders single raster images; this Type renders multi-page paginated documents with text layers, forms, and document semantics. Some platform apps bundle both (documents and images in one window) — the boundary lives at the capability level |
| File Manager | presents file metadata and structure and delegates content rendering to viewer capability; this Type *is* that rendering surface for documents |
| Document Editor / PDF Editor | authors and modifies document content; this Type presents, marks up, fills, and signs. The market itself splits these into separate products |
| Read-it-later Application | captures web articles into a reading queue; this Type opens whole document files with no queue or capture semantics |
| Web Browser | embeds basic PDF viewing; the standalone Type exists for document-grade machinery beyond the embedded surface |
| Word Processing / Page Layout Types | produce the documents this Type consumes; author-agnostic on the reading side |

## Representative Products

- Apple Preview — platform-native document and image viewer
- Evince (GNOME Document Viewer) — desktop-environment document viewer
- Okular (KDE) — annotation-rich universal document viewer
- Foxit PDF Reader — cross-platform commercial reader with a paid editor sibling

Adobe Acrobat Reader — the best-known reader, published by the PDF format's creator — is recognized as the category's market anchor, but its official documentation could not be reached during research, so no product-specific claims about it are made in this document.

## Sources

Research date: **2026-09-08**

- Apple — Preview User Guide for Mac (welcome, "View PDFs and images", "If you can't select or copy text in a PDF"): https://support.apple.com/guide/preview/welcome/mac
- GNOME — Evince help (index, "Moving around a document", "Supported formats"): https://help.gnome.org/users/evince/stable/
- KDE — Okular product site: https://okular.kde.org/
- Foxit — PDF Reader product page and FAQ: https://www.foxit.com/pdf-reader/

> Sourcing limitation: Adobe's official documentation surfaces (helpx.adobe.com, adobe.com) timed out repeatedly on the research date and were abandoned per source-access discipline. Adobe Acrobat Reader is therefore used only as a named market anchor; no capability, packaging, or default is asserted for it. Product operational details for Okular and Foxit rest on official product-page-level sources; precise numeric limits and defaults are intentionally not stated anywhere in this document.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
