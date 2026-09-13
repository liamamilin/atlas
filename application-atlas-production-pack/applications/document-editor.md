# Document Editor

## Overview

A **Document Editor** is an application for authoring persistent prose documents: the user creates a self-contained document, writes and revises it directly on the page, applies explicit text and paragraph formatting while writing, and finishes it as a page-shaped artifact that is printed or exported (typically to PDF and interchange formats for other editors).

The defining structure is small:

```text
Persistent prose document (self-contained artifact the author keeps)
└── Direct inline editing (compose & revise in place)
    └── Explicit text & paragraph formatting applied while writing
        └── Page-shaped finished output (print / export)
```

Everything else commonly associated with this category — styles, templates, tables and images, spell check, comments and tracked changes, mail merge, cloud AutoSave, collaboration — is widely standard in mature products but is not what makes the product a Document Editor. Older, keyboard-driven word processors from before on-screen formatting fidelity, platform-bundled editors, and file-based open-source editors all satisfy the definition without any of those specifics.

When the dominant object shifts to a shared document that several people edit concurrently as one live version, the product is drifting toward a different Application Type (Collaborative Document Editor). When formatting is reduced to plain-text markup rendered in a separate step, that is a Markdown Editor; when the application's promise is hiding everything except the text, that is a Distraction-free Writing Application.

## Users & Context

The primary user is an individual author producing a document artifact that will be read, printed, or sent elsewhere: a report, letter, memo, essay, contract, flyer, newsletter, resume, or manuscript. The author works alone in a private editing session for most of the work; other people typically enter the process only at review time, as commentators or reviewers of a draft the author still owns.

Typical reasons to open the application:

- start a new document from scratch or from a template
- write and revise text with formatting applied as you go
- shape the pages (margins, headers and footers, page numbers, table of contents)
- run a review cycle: collect comments and proposed edits, then accept or reject them
- produce the finished artifact: print it, export it to PDF, or save it in a format another editor or recipient can open

Secondary contexts include households and students (letters, essays, personal documents), organizations of every size (reports, contracts, documentation), and specialist authors of long or multi-part documents (theses, manuals, books). The work environment is traditionally a desktop application over files; web and mobile companions are now common, and documents may live on the local disk or in a cloud drive without changing the model.

## Core Model

### The Defining Core

```text
Persistent prose document (self-contained artifact the author keeps)
└── Direct inline editing (compose & revise in place)
    └── Explicit text & paragraph formatting applied while writing
        └── Page-shaped finished output (print / export)
```

Four properties. If any one is removed, the product is no longer recognizable as a Document Editor:

- **A persistent prose document** — the unit of work is a single, self-contained document the author creates, names, keeps, and revisits over time. The document carries both its content and its formatting, and it travels as a unit (as a file or a cloud-stored document record). Without this, the surface is ephemeral or fragment-based — notes and scratchpads, not documents.
- **Direct inline editing** — the author works on the document itself: place the cursor, type, select, replace, delete. The application is an editor, not a form that generates documents from inputs.
- **Explicit formatting applied while writing** — the application carries a formatting model the author controls directly: character-level (font, size, color, emphasis) and paragraph-level (alignment, spacing, indentation, lists), presented on the editing surface with immediate visible effect, not deferred to a later rendering step. Styles exist to package this formatting; direct formatting remains always available.
- **Page-shaped finished output** — the document is modeled as printed pages: page size, orientation, margins, headers and footers, page numbers, page breaks. The document is completed by leaving the application as a fixed artifact — printed on paper or exported to a portable format.

### Standard Capabilities of Mature Products

Mature products carry a stable set of capabilities beyond the core. They are not what makes the product a Document Editor, but they make it practical.

- **Styles** — named, reusable formatting packages (paragraph styles, character styles, and in some products frame, page, or object styles). Applying a style keeps text consistent; updating a style restyles everything that uses it; the system tracks manual deviations from a style. Generated tables of contents are typically built from styles.
- **Templates** — prebuilt starting documents for common document classes (letters, reports, flyers), with the ability to save custom templates.
- **Content objects** — tables (with formatting, and in some products in-cell formulas), images, shapes, charts, media, text boxes, hyperlinks, bookmarks, footnotes and endnotes, watermarks and decorative display text.
- **Page machinery** — page setup (paper size, orientation, margins), headers and footers, page numbers, page and section breaks, multi-column text, facing-page layouts.
- **Long-document machinery** — generated table of contents, indexes, bibliographies, outline/navigation panes for moving through large documents.
- **Writing aids** — spell check, automatic text replacement, find and replace, word lookup/thesaurus, hyphenation, word count, dictation.
- **File machinery** — saving documents under named formats; importing and exporting interchange formats (office formats, HTML, e-book formats) and PDF; automatic saving to cloud storage; restoring earlier versions; locking or password-protecting documents.
- **Review loop** — comments attached to the text with author attribution, and tracked changes that record proposed edits per author, with accept/reject decisions and display controls for the markup.
- **Print machinery** — a print path with page setup, plus label and envelope printing in many products.

### One Structure, Many Implementations

The core is written in conceptual terms; products realize it differently:

```text
Concept:            Persistent prose document
Implementations:    local file in a working format (.docx / .odt / other),
                    cloud-stored document with automatic saving

Concept:            Formatting model
Implementations:    ribbon/toolbar commands + pop-up formatting bars,
                    style galleries and sidebars/inspector panels,
                    style decks over direct formatting

Concept:            Page model
Implementations:    print-layout view with live pagination, rulers and
                    formatting marks, print dialogs, PDF/office-format/
                    e-book export

Concept:            Review loop
Implementations:    tracked changes with per-author colors and
                    accept/reject controls, comments/annotations
                    in margins or cards
```

A reader who has only seen one implementation (say, a subscription desktop suite) should still recognize a file-based open-source editor or a platform-bundled editor as the same Type from the core alone.

## How It Works

### Start a document

```text
Open the application
→ create a blank document or pick a template
→ the document artifact exists (named, saved, kept)
```

Templates are the common starting point in modern products, but a blank document is always available; the artifact, not the template, is the invariant.

### Compose and format

```text
Type text into the body
→ select text → apply character formatting (font, size, color, emphasis)
→ apply paragraph formatting (alignment, spacing, lists, indentation)
→ optionally apply styles instead of, or on top of, direct formatting
→ insert objects where needed (tables, images, charts, links)
```

Formatting takes effect immediately on the editing surface — this is the visible difference between a Document Editor and markup-source editors. Styles are the scalable form of the same formatting: apply once, restyle everywhere.

### Shape the pages

```text
Set page size, orientation, margins
→ add headers, footers, page numbers
→ control page breaks and sections
→ insert a generated table of contents
```

The document's pagination is live: as text flows past the end of a page, new pages are created automatically (in the word-processing document model that defines the Type).

### Revise

```text
Run spell check / look up words
→ find and replace across the document
→ check word count and statistics
→ move around via outline or navigation panes
```

### Run a review cycle

```text
Send the document to reviewers (as a copy or via sharing)
→ reviewers add comments and tracked-change edits
→ the author reviews each proposed change
→ accept or reject individually, in bulk, or all
→ the document remains the author's artifact throughout
```

The review loop passes the artifact between people; it does not turn the document into a shared live surface. Even when the same product also offers real-time co-editing, the author-owned document with tracked proposals remains this Type's native pattern.

### Finish

```text
Print, or
→ export to PDF (the fixed, appearance-preserving artifact), or
→ save in an interchange format for another editor or recipient
→ optionally: merge the document with a data source for bulk versions
```

### Core vs Standard vs Optional

**Defining core** — without these, not a Document Editor:

- persistent self-contained prose document
- direct inline editing
- explicit text/paragraph formatting applied while writing
- page-shaped finished output (print/export)

**Standard in mature products**:

- styles; templates
- tables, images, shapes, charts, hyperlinks, footnotes, headers/footers, generated tables of contents
- spell check, autocorrect, find & replace, word count
- save/open in named formats, PDF and interchange export, AutoSave/cloud storage, version restore, document lock/password
- comments and tracked changes with accept/reject
- print machinery
- navigation panes, undo/redo, format copying

**Optional / variant**:

- mail merge, labels and envelopes
- macros and automation
- bibliographies, citation management, indexes, master documents
- equations, in-table calculations
- DTP-adjacent layout (multi-column, frames, text wrap, linked text boxes)
- bidirectional / vertical / CJK typography
- real-time co-editing (the drift seam toward the Collaborative Document Editor)
- AI assistance in authoring
- book/e-book production

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Document window (page view)

The primary surface: the document rendered as pages, with a body-text area carrying the cursor.

- shows live pagination, margins, and the text with its formatting
- primary actions: type, select, edit, insert, scroll through pages

### Formatting surfaces

The controls through which the formatting model is exercised.

- a command ribbon or toolbar with font and paragraph controls, plus a pop-up formatting bar on text selection
- style galleries/panels listing paragraph and character styles, with style creation, update, and override handling
- inspector sidebars or panels for document, section, and object settings
- primary actions: apply character/paragraph formatting, apply/create/update styles

### Insert surface

- a menu or tab for placing content objects: tables, pictures, shapes, charts, links, page elements (breaks, headers/footers, page numbers, tables of contents)
- primary actions: insert, size, position, and format objects

### Review surface

- track-changes controls (on/off, scope, display of markup), comment placement and navigation, accept/reject controls, review summaries
- markup shown per author; comments collected as a navigable set
- primary actions: toggle tracking, add/reply to comments, accept/reject changes

### Document management surface

- open/save dialogs or a document browser; recent documents; template chooser; cloud-drive locations where applicable
- primary actions: create, open, rename, duplicate, move, delete, lock/protect, restore earlier versions

### Print and export surface

- print dialog with page setup and print options; export dialog for PDF and interchange formats
- primary actions: print, export, save-as-format

### Navigation aids

- outline or navigator panes, page thumbnails, rulers, optional formatting marks
- primary actions: jump between headings/pages, find text

## Important Rules / Behaviors

### The document is the container of truth

Content and formatting live inside the artifact and travel with it. What other people receive — a copy, an export, a print — is a rendering of that artifact. Documents are saved in the application's working format, and interchange formats exist to carry the document to other editors; when appearance must be preserved exactly, the fixed export (PDF) is used.

### Formatting is immediate and layered

Formatting applied to text takes effect on screen at once. Styles sit on top of direct formatting: changing a style restyles everything that uses it, and manual deviations are tracked as overrides that can be kept or folded back into the style.

### The body-text area flows

In the defining document model, text flows from page to page and new pages are created automatically as content grows. (Some products additionally offer a canvas-style page-layout document mode in which pages are added manually — a vendor-documented alternative mode, not the Type's center.)

### Tracked changes persist until decided

Proposed edits remain visible markup — attributed to their authors — until accepted or rejected; hiding markup for display or printing does not remove it, only the accept/reject decisions do. Some products let an author lock tracking on, and documents shared specifically for review may not allow tracking to be turned off at all.

### Saving is tied to where the document lives

A document stored locally is saved explicitly by the author; a document stored in a connected cloud location is commonly saved automatically, with the automatic behavior toggleable. Version history and restore exist alongside, letting the author return to earlier states of the artifact.

### The finished artifact is fixed

Print and PDF capture the document's layout at a point in time. The artifact that leaves the application is read-only by nature; editing it again means bringing it back into the editor (some products can open and convert fixed exports for editing).

## Variants

The Type is implemented in several recognizable forms:

- **Office-suite editor** — the document editor as one application in a suite (word processor, spreadsheet, presentation) with shared command structure and interchange (the dominant enterprise/consumer form)
- **File-based open-source editor** — desktop application over standard document formats, offline-first, with strong interchange posture (the sovereignty/public-sector form)
- **Platform-bundled editor** — shipped with a device platform's operating system, cloud-connected, design-forward, consumer tier
- **Cloud-native editor** — browser-first editing of cloud-stored documents (today usually carrying the collaborative machinery of the sibling Type)
- **Long-document/professional variant** — emphasis on indexes, bibliographies, master documents, citation workflows
- **DTP-adjacent variant** — deeper layout capabilities (columns, frames, wrap) marketed inside the word processor; the dedicated canvas-first pole remains a separate Type
- **Regional suites** — office editors dominant in specific regional markets, same core structure

A variant remains a **Variant** unless it changes the core object: once the primary object becomes the shared live merged document, the product belongs to the Collaborative Document Editor Type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Collaborative Document Editor | the shared live merged document is the primary object, with sharing/permission machinery as the defining structure; here the author-owned artifact is primary and collaboration is layered on |
| Markdown Editor | formatting is plain-text markup rendered in a separate step; here formatting is explicit and visible during writing |
| Distraction-free Writing Application | formatting deferred and chrome hidden to preserve attention during drafting; here formatting and page layout are continuously visible and editable |
| Desktop Publishing / Page Layout Application | a layout canvas with manually placed text frames and manual pages; here a body-text area flows across automatically created pages |
| Note-taking Application | fragment notes in a container for capture and retrieval; here a single self-contained print-shaped artifact |
| Resume Builder | owns a structured career-document model and re-renders it from templates; here the user owns both content and layout, free-form |
| Code Editor | program source with syntax tooling; here prose documents with a formatting/print model |
| Text editor / generic rich-text fields | no self-contained artifact, page model, or finished-artifact production |

The two most important boundaries: against the **Collaborative Document Editor** (is the primary object a shared live merged document, or an author-owned artifact with collaboration layered on?) and against the **Markdown Editor** (is formatting explicit and visible during writing, or deferred to a rendering step?).

## Representative Products

- Microsoft Word
- LibreOffice Writer
- Apple Pages

The core model was checked against older keyboard-driven word processors (formatting-code era), platform-bundled editors, and file-based open-source editors to avoid over-fitting to the modern desktop-suite pattern. Cloud-native collaborative editors (the Google Docs class) are documented under Collaborative Document Editor.

## Sources

Research date: **2026-09-07**

- Microsoft Support — Word help & learning hub: https://support.microsoft.com/en-us/word
- Microsoft Support — "Create a document in Word": https://support.microsoft.com/en-us/word/training/create-a-document-in-word
- Microsoft Support — "Add and edit text": https://support.microsoft.com/en-us/word/training/add-and-edit-text
- Microsoft Support — "Save a document": https://support.microsoft.com/en-us/word/training/save-a-document
- Microsoft Support — "Track changes in Word": https://support.microsoft.com/en-us/word/training/track-changes-in-word
- LibreOffice Help — "Welcome to the LibreOffice Writer Help" and "LibreOffice Writer Features": https://help.libreoffice.org/latest/en-US/text/swriter/main0000.html , https://help.libreoffice.org/latest/en-US/text/swriter/main0503.html
- Apple Support — Pages User Guide for Mac (guide TOC; "Intro to word-processing and page layout documents"; "Intro to paragraph styles"): https://support.apple.com/guide/pages/welcome/mac , https://support.apple.com/guide/pages/word-processing-or-page-layout-tan6129a1862/mac , https://support.apple.com/guide/pages/intro-to-paragraph-styles-tanaa39b0aa3/mac

> Sourcing limitation: official documentation for the cloud-native pole of this market (Google Docs) could not be fetched (request timeouts, consistent with a prior sibling-leaf pass); no operational claims about that product are made here, and cloud-native editing is treated through the sibling Collaborative Document Editor documentation. LibreOffice evidence is at the features-page and help-contents level; no claims are made about features not confirmed there. Precise vendor specifics (menu names, exact default settings, format internals) are intentionally not asserted in this document.

Detailed product-by-product observations, the cross-product comparison matrix, and the historical market-sample check are recorded in the paired Research Notes.
