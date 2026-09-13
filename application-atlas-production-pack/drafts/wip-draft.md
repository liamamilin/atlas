---
slug: wip-draft
name: Book Writing Application
name_zh: 书籍写作应用
desc: 以书稿项目为核心、分层组织章节与素材并编译为ePub或印刷PDF的写作工具；非排版画布、非出版管理系统。
link: 
name_source: model
source: human
status: draft
engine: opencode
created: 2026-09-13T00:13
---
# Book Writing Application

## Overview

A **Book Writing Application** is an author-facing application whose unit of work is a book-length project: a persistent container holding a manuscript broken into movable structural units (parts, chapters, scenes, sections), the supporting material around a book (research, character and place profiles, the story bible), per-unit metadata (titles, synopses, statuses, labels, word targets), and the definitions of the finished artifact. The author drafts, reorders, splits, merges, and revises those units across a long project, then compiles the project into book-format output — EPUB, print-ready PDF, or submission DOCX — with front and back matter, a table of contents, and output styling assembled at generation time.

The defining structure is small:

```text
Book project (the author's unit of work — one book, or a series container)
├── Manuscript structure — the book's text as ordered, movable units
│   ├── front matter (half-title, title page, copyright, dedication …)
│   ├── body units (parts / chapters / scenes / sections)
│   └── back matter (afterword, acknowledgements, appendix, notes …)
├── Supporting material — research, notes, character/place profiles, story bible
├── Project and unit metadata — titles, synopses, statuses, labels, word targets
└── Output definitions — the artifacts the project compiles into
    (EPUB, print-ready PDF, submission DOCX, plain text …)
```

A book is assembled from hundreds of small pieces written out of order, repeatedly reordered, and finally shaped for a reading format. A word processor models one linear file with live pagination; this Type models a project of many units whose reading order is editable and whose formatting is decided at the end.

The canonical boundary is stated by subtraction. Remove the book-scale project and keep a single self-contained artifact with visible formatting and page output: a Document Editor. Keep only the attention-preserving drafting surface: a Distraction-free Writing Application. Replace the compile with a page canvas of freely placed frames: a Desktop Publishing Application. Replace the author with a publisher and add contracts, royalties, and metadata feeds: Book Publishing Management. This Type is none of these; it is the author's own workroom for a book.

### What the definition deliberately excludes

Everything the market associates with the category — plotting grids, character sheets, worldbuilding bibles, focus modes, word goals, AI drafting, cloud sync, collaboration, audiobook export — is common but not definitional. A 1990s binder-plus-compile program would satisfy the definition, as would a bare open-source outliner with an EPUB export. The book project and the compile-to-book step are the invariants.

## Users & Context

### Primary users

The primary user is an author producing a book-length work, and the application is built around that person's private, long-horizon drafting labor:

- **Novelists and fiction writers** — draft chapters and scenes, track plot threads and continuity across tens of thousands of words, and reorder the narrative often.
- **Non-fiction, memoir, and self-help authors** — combine narrative prose with research, interviews, and structured argument; footnotes and references often matter.
- **Academic and technical book authors** — produce a monograph or textbook whose chapters must move and whose output must satisfy a publisher's format.
- **Self-publishing authors** — own the production chain and need the manuscript to become store-ready EPUB and print PDF editions without a separate typesetting tool.

Secondary users enter at defined moments: **editors, proofreaders, and beta readers** (through comments, tracked changes, shared previews, or exports), **co-authors and ghostwriters** (in products that support shared projects), and **series authors and worldbuilders**.

### Context of use

The work is a long campaign: many months of short drafting sessions plus intense structural revisions, ending in a production push. Progress is measured against a whole book, so goal machinery attaches to manuscript units, and the project must survive over time — backed up, versioned, synced — because losing it destroys months of work. The environment ranges from offline-first desktop files to browser-based cloud projects; the Type is defined by the project, not by where it lives.

## Core Model

### The Defining Core

Three properties, jointly held. Remove any one and the product stops being recognizable as a Book Writing Application:

- **The book project as the unit of work.** The center is one persistent book-length project — not a single document, not a folder of unrelated notes — that gathers the manuscript, supporting material, and output definitions. This separates the Type from a Document Editor (one artifact) and a Note-taking Application (a library of fragments).
- **The manuscript as an ordered structure of movable units.** The text is held as discrete units (parts, chapters, scenes, sections) in a hierarchy that is directly editable: units can be created, split, merged, retitled, reordered, folded, and moved with their children. Reading order is held separately from formatting and pagination — unlike a word processor, where order is implied by one file's sequence.
- **Compilation into a book artifact.** A deliberate compile step assembles units in reading order, adds front and back matter, generates the table of contents, applies an output template, and emits a fixed artifact (EPUB, print-ready PDF, submission DOCX, plain text): the separation from a pure outliner or planning tool.

### Supporting material, metadata, and capability tiers

The manuscript is not the whole project: a book-length project also accumulates material that stays beside the text without entering it — **research** (web pages, PDFs, images, transcripts, notes), a **story bible** of characters, places, items, timelines, and continuity facts often linked to the scenes where they appear, **plot scaffolding** (outlines, beat sheets, boards), and **working notes** excluded from output. Elaborate or minimal, this is a product philosophy, not a defining property.

Each unit also carries metadata — title, synopsis, status (drafting, revising, done), label, keywords, point-of-view tag, word target — while project metadata (title, author, series, total target) feeds the compile and progress views.

- **Defining core** — book project; editable structure of movable units; compile into book-format output.
- **Standard in mature products** — structural views, a drafting editor with styles and comments, per-unit metadata and statuses, word targets and history, a research/notes store, compile templates, autosave/backups, multi-device sync.
- **Optional / advanced** — plotting and worldbuilding databases, series bibles, real-time co-authoring, editor marketplaces, AI drafting and revision, audiobook or screenplay conversion, direct store publishing, LaTeX/technical pipelines.

### One structure, many implementations

```text
Concept:  book project       →  one project file on disk (binder document);
                                a cloud workspace; a series container;
                                a folder of plain-text files under version control
Concept:  manuscript units   →  binder sections/folders with synopses;
                                web chapters with drag-and-drop ordering;
                                scenes under chapters in a grid; local files
Concept:  compile / generate →  a compile dialog with per-format settings;
                                one-click EPUB and print-PDF export;
                                a template/theme picker; a CLI export pipeline
```

A reader who has only seen a desktop binder app should still recognize a browser-based editor or an open-source local tool as the same Type from the core alone.

## How It Works

### Start a book project

```text
Create a project (blank or from a template)
→ name the book; set the project's format and metadata
→ optionally choose a structure template (novel, non-fiction, thesis …)
→ the project opens with front matter, a first chapter, and a binder/sidebar
```

Templates are accelerators, not the Type: a blank project with a single unit is always available.

### Draft a unit

```text
Select a unit in the structure → the editor shows that unit's text
→ write; the unit's word count and status update
→ finish or leave the unit; the project remembers where you stopped
→ move to another unit and continue — writing order is free
```

The defining freedom: the author can write any scene at any time and leave gaps, because the project holds the structure rather than depending on the text's physical order.

### Work the structure

```text
Open the outline / corkboard / board view → see the whole book as units
→ drag units to reorder; rename, split, merge, or delete them
→ mark units to exclude from the compile (notes, cut scenes)
→ set statuses and labels to track progress and POV/threads
```

Structural work and drafting are deliberately separable: restructure without touching prose, revise prose without disturbing order.

### Compile the book

```text
Choose a target (EPUB, print-ready PDF, DOCX, plain text)
→ pick a template or theme; choose trim size and output options
→ select which units are included and how titles are handled
→ generate: units assemble in reading order, front/back matter added,
  table of contents built, styles applied
→ inspect the artifact and adjust; regenerate after edits
```

Compilation is the moment the project becomes a book, and it is repeatable: fixing a typo and regenerating produces new editions in seconds.

### Plan, track, and the parallel planning loop

```text
Before or during drafting: open the plot/planning surface
→ build a timeline, beat sheet, or board of scenes linked to units
→ set a target (total words, daily words, deadline)
→ the dashboard shows progress across the book; per-unit counts and
  statuses surface what is unfinished; history sustains the campaign
```

Some products fold planning into the project; others run a companion tool beside it. Either way, planning serves the book rather than replacing it.

## Interfaces

Exact layouts and names vary by product.

### The project / binder surface

The structural home of the book and often the first screen: a hierarchical tree of parts, chapters, scenes, and research items with icons, titles, synopses, statuses, and word counts. Primary actions: create/rename/reorder/delete units, open a unit in the editor, fold branches, drag to restructure.

### The writing editor

The drafting surface, opened on the selected unit: rich text or Markdown editing with formatting, styles, comments, highlights, and find/replace, plus an inline unit title, word count, and status and often an optional focus mode. Primary actions: type, format, comment, search, split or merge the unit, snapshot it.

### The outline / corkboard / board surface

Alternative structural views over the same project: an outline of units as rows with synopsis and metadata columns; a corkboard of index cards, freely arranged and reorderable; a board/grid of scene cards or cells with POV, status, and custom columns. Primary actions: drag to restructure, edit synopses and metadata in bulk, filter by label/status.

### The planning, story-bible, and research surfaces

Where continuity and support material live (present in most mature products, absent in minimal ones): profiles for characters, places, and items; timeline views; relations between records; "appears in" links showing which scenes reference a record; and imported files plus notes viewable beside the draft. Primary actions: create/edit records, link them to scenes, organize references, open beside the text.

### The compile / export surface

The bridge from project to artifact: target format, template/theme, trim size and page settings, inclusion and title-handling options, and front/back-matter configuration. Primary actions: configure, preview, generate, update editions, save settings as a reusable format.

### The progress and collaboration surfaces

The long-campaign instruments and the points where others enter a private project: total and per-unit word counts, goal progress, session statistics, writing history, and streak calendars; comments anchored to text, tracked changes, shared read-only previews, role-based access, and version compare/restore. Primary actions: set targets and deadlines, jump to unfinished units, invite a collaborator, comment, accept/reject edits, share a preview, restore a version.

## Important Rules / Behaviors

### The project, not a file, is the unit of work

The author names, backs up, syncs, and compiles a project; the manuscript units are internal structure, not files the user must manage, and in many products the project is one opaque document. Where a product exposes files (an open-source folder-based tool), the project is still the organizing concept.

### Structure is decoupled from pagination and formatting

Unlike a word processor, the application does not force the manuscript to look like pages while drafting: reading order is explicit, and a page-like appearance, if shown, previews a chosen output. Writers can thus rearrange chapters without the layout churn a page-based word processor produces.

### Compile is a transformation, and writing order is not reading order

The finished artifact is generated from the project through output settings; it is a rendered result, not the source, so editing an exported EPUB or PDF does not change the project and regenerating overwrites the artifact. Relatedly, authors draft out of sequence: the project separates the order units were written from the order they are read, and cut or research units can remain while being excluded from the compile.

### Progress attaches to manuscript units, and storage sets the rules

Word counts, statuses, and targets are computed over the structured manuscript, per unit and for the whole book; a daily goal is a slice of a book-length target. Where the project lives then determines sync, backup, and lock-in: a local-file product relies on a cloud drive or manual transfer for multi-device work, while a cloud-workspace product syncs automatically and ties the work to an account.

### AI assistance, where present, is advisory and author-owned

Products that add generative drafting, outlining, or revision keep the author as owner: generated material enters as suggestions the author reviews, and the workflow (project → units → compile) is unchanged. The book outlives any single format — one project yields several editions, and the project, not any artifact, is the durable asset.

## Variants

Common forms of the Type; the core model holds across all of them.

- **File-based desktop studio** — a single application over a local project file, offline-first, with rich structural views and compile settings; the historical center of the category (Scrivener being the archetype).
- **Cloud subscription workspace** — browser-and-app project synced to an account, with community, goal, and plotting features.
- **All-in-one write-and-format tool** — drafting and book formatting combined, so one project exports store-ready EPUB and print PDF without a second tool.
- **Formatting/production-emphasis tool** — imports a finished manuscript and concentrates on building beautiful editions; drafting is minimal and structure derives from the import.
- **Open-source local tool** — free software over local files, often with a planning method and a distraction-free editor.
- **Planning-first companion** — a plot/story-bible tool whose output is an outline exported into a writing application; when it stops producing book-format output of its own, it drifts toward Outliner/Timeline territory.
- **AI-forward workspace** — a cloud studio where generative drafting, rewriting, and analysis sit alongside the structural and export machinery.

A variant stops being a variant when it changes the core object: a single page-layout file with manually placed frames is Desktop Publishing; a publisher managing titles and contracts is Book Publishing Management.

## Related Application Types

| Type | Distinction (remove X → becomes Y) |
|---|---|
| Document Editor | Remove the multi-unit project and the compile, leaving one self-contained artifact with visible formatting and page output: a Document Editor. |
| Distraction-free Writing Application | Remove the manuscript structure and compile so the promise becomes hiding everything but the text: a Distraction-free Writing Application; here focus mode is at most a capability. |
| Collaborative Document Editor | Make a shared live merged document the primary object with co-editing as the defining structure: a Collaborative Document Editor; here collaboration is a layered feedback loop. |
| Desktop Publishing / Page Layout Application | Replace the structured manuscript with a page canvas of freely placed frames and threaded stories: a Desktop Publishing Application. |
| Professional Typesetting Application | Replace interactive drafting with markup/batch composition rules: a typesetting system; some tools export to such a pipeline, but composition is not their surface. |
| Book Publishing Management | Remove the author's writing environment; add title records, contracts, royalties, rights, and metadata feeds run by a publisher: Book Publishing Management. |
| Publishing Editorial Workflow | Move the center to a publisher's staged content process (submissions, review rounds, gates, assigned roles) with the author external: Publishing Editorial Workflow. |
| eLearning Authoring Tool | Add learner-facing interactivity and an LMS delivery package: an eLearning Authoring Tool; remove them and compiled reading content remains this Type. |
| Outliner | Strip the manuscript prose and the compile, leaving the hierarchy itself as the product: an Outliner; here the tree serves a book. |
| Personal Knowledge Management Application | Diffuse the single book project into a network of linked notes across many topics: a PKM application; here all material serves one book-shaped output. |

The two most consequential boundaries are the Distraction-free Writing Application (is the promise the attention surface or the book project?) and the Document Editor (a project of movable units versus one page-shaped artifact).

## Representative Products

- **Scrivener (Literature & Latte)** — file-based desktop studio built on a ring-binder of sections with outlining, corkboard, research, snapshots, and compile to EPUB/PDF/DOCX; the structural file-based pole and the Type's archetype. https://www.literatureandlatte.com/scrivener
- **Atticus** — cross-platform (PWA) all-in-one tool that drafts and formats the book, with drag-and-drop chapters, goals, and EPUB/PDF/DOCX export; the write-and-format-in-one variation. https://www.atticus.io/
- **Dabble** — cloud subscription studio for fiction with plot grid, character profiles, worldbuilding notes, focus mode, and sync; the cloud-workspace, planning-rich variation. https://www.dabblewriter.com/
- **Reedsy Studio** — free browser app that plans, drafts, edits, and typesets with Boards, real-time collaboration, and one-click EPUB/print-PDF export; the free/collaborative ecosystem variation. https://reedsy.com/studio
- **Vellum (180g)** — macOS tool that imports a manuscript and produces store-ready editions (EPUB 3/2, print-ready PDF/X-1a) across trim sizes; the formatting/production-emphasis variation. https://vellum.pub/
- **Manuskript** — open-source local tool with outliner, snowflake assistant, story records, and a distraction-free mode; the open-source, local-file, methodology-led variation. https://www.theologeek.ch/manuskript/

These six cover the main poles (file-based vs cloud; drafting-first vs formatting-first vs planning-first) and commercial models (one-time, subscription, free ecosystem).

## Sources

Research date: **2026-09-13**

Product sources (fetched on the research date):

- Scrivener — https://www.literatureandlatte.com/scrivener (binder, Scrivenings, corkboard, outliner, targets, snapshots, compile)
- Atticus — https://www.atticus.io/ (writing editor, templates, EPUB/PDF/DOCX export, one-time pricing)
- Dabble — https://www.dabblewriter.com/ (plot grid, character profiles, worldbuilding bible, goals, focus mode)
- Reedsy Studio — https://reedsy.com/studio (Write/Plan/Format, Boards, collaboration, EPUB and print-PDF export)
- Vellum (180g) — https://vellum.pub/ (EPUB 3/2, print-ready PDF/X-1a, trim sizes, styles, update flow)
- Manuskript — https://www.theologeek.ch/manuskript/ (outliner, snowflake assistant, story records, distraction-free mode)

Boundary-context surfaces consulted (not primary core-model evidence): Plottr — https://plottr.com/; Novlr — https://www.novlr.org/; Campfire Writing — https://www.campfirewriting.com/; LivingWriter — https://livingwriter.com/. Sibling corpus leaves read for boundaries: document-editor, distraction-free-writing-application, desktop-publishing-application, book-publishing-management, publishing-editorial-workflow, author-management-platform, elearning-authoring-tool, outliner.

Could not verify:

- **yWriter** (spacejock.com/yWriter7.html) returned HTTP 500; it was dropped rather than cited from memory.
- No vendor help-centre or user manual was accessed for any representative product; all statements rest on official product/landing pages, so exact numeric limits, defaults, full export-option inventories, and pricing are deliberately not asserted. Feature coverage varies by edition, platform, and plan (Vellum is macOS-only; Atticus is a one-time-purchase PWA) — observations, not properties of the Type.
- The `application-atlas` MCP tools (search_similar / get_leaf) were not exposed in this environment; nearest-neighbor work was done by reading the corpus leaves listed above.
