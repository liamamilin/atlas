---
lint_errors: 0
lint_warnings: 0
slug: wip-draft-2
name: Novel Writing Application
name_zh: 小说创作应用
desc: 以结构化手稿树与故事设定库为核心的长篇虚构写作工具，覆盖构思、起草、修订到编译成稿，不承担排版与出版流程
link: 
name_source: model
source: human
status: draft
engine: opencode
created: 2026-09-13T01:19
---
# Novel Writing Application

## Overview

A **Novel Writing Application** is a long-form fiction authoring environment that holds a book-length narrative as a *structured manuscript* — an ordered, reorderable tree of parts, chapters, and scenes rather than one flat document — and binds it to a *project-attached body of story material* (characters, locations, world rules, plot threads, research) plus the tracking, revision, and assembly machinery needed to carry tens of thousands to hundreds of thousands of words from premise to submission-ready manuscript.

Its defining core is deliberately small:

```text
Novel project
├── Manuscript — the book as an ordered tree
│   ├── structural units (part / chapter / act)
│   │   └── prose units (scene or section documents — the editable leaves)
│   └── front & back matter (title page, dedication, epilogue …)
├── Story material — reference records beside the prose
│   └── characters, locations, items, lore, plot threads, research
├── Planning surfaces
│   └── synopses, index cards, scene grid, timeline, beat templates
├── Long-form state
│   └── per-unit word counts, targets, status, labels/POV, writing history
└── Assembly
    └── snapshots/versions → compile settings → exported manuscript
```

The Type exists because a novel is long enough that no single document stays workable: authors write out of order, restructure late, keep a large cast consistent over months, and finally produce one continuous manuscript. Corkboards, word-count goals, series bibles, AI co-writing, and e-book export are machinery layered on this core.

Canonical boundary: if the prose leaves disappear and only scene cards remain, it is a plot-outlining tool; if the story material and manuscript tree disappear and one continuous text remains, it is a word processor or a distraction-free writing application. This Type is the union of structure *and* prose.

## Users & Context

### Who uses it

The primary user is a novelist — a fiction author working at book length. The population splits into groups that shape which variation they choose:

- **genre fiction authors** — romance, fantasy, science fiction, mystery and thriller, historical, horror, LitRPG — often writing series and dependent on continuity across books
- **literary fiction authors** — lighter on world-building, heavier on revision and versioning
- **independent and self-publishing authors** — want drafting and a submission- or retail-ready export in one place
- **traditionally pursuing authors** — draft in the tool, then compile to a standard manuscript format for agents and editors

Secondary users appear in collaborative setups: co-authors sharing a project, developmental editors and beta readers invited to read or comment, and series authors sharing one story bible. Screenwriters and non-fiction authors are served by several products, but book-length fiction is the center.

### Working context and methods

A project is measured in months to years, and the work is not linear. Three activities interleave and products organize around them: **planning** (an outline, beat sheet, or scene list), **drafting** (prose scene by scene, often out of order, against daily targets), and **revising** (restructuring the whole, comparing drafts, reconciling continuity). The market openly divides writers into "plotters" who plan first and "pantsers" who draft and retrofit structure, and the strongest products serve both by making the same tree usable as a plan or a post-hoc map. A novel is private until the author shares a draft.

## Core Model

### The Defining Core

Four properties, jointly held. Remove any one and the product stops being recognizable as this Type:

- **The structured manuscript as the unit of work.** The novel is an ordered hierarchy of separately editable units — commonly part → chapter → scene — that the author can rename, reorder, merge, split, nest, and include or exclude, with prose in the leaf units. Without this it is a word processor; with it, "move this scene to chapter one" is a structural operation, not a cut-and-paste.
- **Project-attached story material (the continuity layer).** Characters, locations, items, world rules, plot threads, and research live in the same project as the manuscript but outside the prose, so the author can consult and maintain them while writing. Some products formalize typed records — a "codex," "story bible," or "worldbuilding" module with cross-links — while others provide only a research area, note pages, and reusable templates. The layer must exist; its formality is a product choice.
- **Long-form lifecycle machinery.** The project carries state across the whole book: word counts that aggregate up the tree, per-unit drafting status, targets, writing history, and a revision mechanism (snapshots, versions, comparison). This is what lets the Type survive a 120,000-word project instead of collapsing into one unwieldy file.
- **Assembly into one manuscript.** The structured units compile into a single continuous document — with front matter, chapter headings, and formatting presets — for submission, self-publishing, or proofing. The tree is thus two-faced: a working model while writing and the table of contents of the finished book. Without assembly, the structure is a private plan with no deliverable.

What is deliberately *not* required: AI, cloud sync, real-time collaboration, deep world-building, a specific file format, or a dedicated plotting view. Desktop tools, cloud products, AI-native platforms, and open-source projects all satisfy the same core.

### The Continuity Layer and the Manuscript

The two halves of a project are different kinds of object:

```text
Manuscript                          Story material
─────────                           ──────────────
ordered, hierarchical               unordered (or loosely categorized)
prose that will be published        reference that will not
included/excluded at compile        never appears in the book text
measured in words                   measured in facts and links
```

A character record holds what the author needs to stay consistent — appearance, voice, backstory, goal, arc — and may link to the scenes where the character appears, but it never prints. A scene's *synopsis* is a third thing: a one-paragraph description attached to a structural unit, used on planning surfaces and excluded from output. Confusing these three — prose, reference, synopsis — is a common beginner error the core model prevents. Some products automate the link (a codex highlighting recognized names, an AI assistant retrieving records), but automation is an accelerator, not the definition.

### Standard Capabilities of Mature Products

Widespread and expected, but not definitional:

- **Structural tree** with drag-and-drop reordering, grouping, and per-unit include/exclude flags for compile
- **A prose editor** (rich text or Markdown) with split panes, full-screen mode, comments, and footnotes
- **Planning surfaces** — index cards or corkboard, a scene grid (scenes × storylines/POV), a timeline or beat template, and an outline view; moving a card reorders the manuscript
- **Per-unit metadata** — synopsis, status, label or color, point of view, keywords
- **Word counts and goals**, live per scene and for the book, with session targets and history
- **Revision support** — snapshots or version history, diff and compare, global find-and-replace
- **A story-bible module** — typed character, location, and item records, sometimes shared across a series
- **Compile and export** to Markdown, RTF, DOCX, PDF, or EPUB, with import from Word and plain text
- **Search, optional collaboration, optional AI assistance, and cross-platform sync**

### One Structure, Many Implementations

The core model is conceptual; products realize each piece differently:

```text
Concept:  manuscript as an ordered tree
Impl.:    binder tree (Scrivener), chapter/scene list (Dabble, bibisco),
          book → act → chapter → scene tree (Novelcrafter), outline (Manuskript)

Concept:  prose unit
Impl.:    rich-text sub-document; Markdown scene file;
          card with attached text; chapter-sized document

Concept:  continuity layer
Impl.:    research folder with templates; story-notes area;
          linked codex wiki with typed records; character/plot/world tabs

Concept:  planning surface
Impl.:    corkboard of cards; scene grid; timeline lanes; snowflake prompts

Concept:  revision
Impl.:    per-document snapshots with compare; version history; duplicated drafts

Concept:  assembly
Impl.:    compile dialog with presets and front matter; one-click export;
          project folder of Markdown files
```

A reader who has only seen one realization — say, a binder-based desktop tool — should recognize the same core in a cloud scene-list product or an AI codex-centric platform.

## How It Works

### Create the project

```text
New project (blank or from a template)
→ name it, choose a format or method (novel, series, screenplay, snowflake)
→ optionally set a total word-count target and a daily goal
→ a starter structure appears: front matter, chapters, a first scene
```

Templates encode method: a blank novel, a three-act structure, a beat-sheet skeleton, a snowflake scaffold, or a genre-specific plot template. The author can ignore all of it and start with one empty scene.

### Plan the story (plotter path)

```text
Add structural units (acts, chapters, scenes) without prose
→ write a one-line and a paragraph synopsis on each unit
→ open the planning surface (cards, grid, or timeline)
→ arrange and tag units by storyline, POV, or tension
→ reach an outline the author trusts enough to draft from
```

The same objects serve the plan: a scene card in the grid *is* the scene in the manuscript, so planning and restructuring are the same acts. This is why a corkboard move reorders the book.

### Draft the manuscript

```text
Pick a scene — often out of order, often a blank unit created on the fly
→ write prose in the editor
→ consult the continuity layer in a side pane and update it as facts emerge
→ leave inline comments for later
→ move to the next scene; the tree grows and reshapes as the story does
```

Authors routinely write the ending first, insert a scene between two existing ones, or split an overlong chapter. The tree absorbs this without a linear rewrite, and word counts roll up automatically. A daily or session target with a live count and history keeps progress visible even while the book is out of order, substituting for the deadlines an external editor would otherwise impose.

### Revise

```text
Take a snapshot of a unit before a rewrite
→ restructure: move, merge, split, or cut units in the tree
→ rework prose; compare against the snapshot when needed
→ run project-wide find-and-replace for names and terminology
→ reconcile continuity: update the story bible as facts change
```

Cutting a subplot means cutting its scenes, not hunting through one enormous file; renaming a character is a project-wide replace plus a bible edit; a snapshot preserves the version the author no longer trusts.

### Compile and deliver

```text
Select which units are included (prose yes; research, synopsis, notes no)
→ choose an output format and a formatting preset
   (submission manuscript, print, EPUB, or editor/beta-reader copy)
→ assemble: front matter, chapter headings, spacing, styles
→ export a single continuous manuscript
```

Compile is a separate pass: authors draft in one font and submit in another, and the settings bridge the two without forcing the draft to look like the deliverable.

## Interfaces

Described conceptually; names and layouts vary by product.

### Project binder / manuscript tree

The spine of the application and the author's map of the book.

- purpose: show the whole novel as ordered structural units
- typical information: parts, chapters and folders, scene titles, per-unit word counts, status and label marks, include/exclude state
- primary actions: create, rename, drag to reorder, nest, merge, split, duplicate, set status, exclude from compile

### Writing editor

Where prose is produced.

- purpose: draft and edit the current unit's text
- typical information: the prose, comments, highlights, and inline notes; often a side pane showing synopsis, metadata, or another document
- primary actions: type, format, insert comments, split the view, open a continuity record or reference beside the text, enter full-screen mode

### Planning board / scene grid / timeline

The surfaces that let the author see the story rather than the text.

- purpose: arrange and diagnose the narrative at a glance
- typical information: scene cards with short synopses; rows or columns for storylines, POV, or characters; a beat or template skeleton; a timeline
- primary actions: add, move, and reorder scenes; edit synopses in place; tag by storyline or POV; apply a beat template

### Story bible / codex

The continuity layer's working surface.

- purpose: keep the cast, world, and rules consistent across a long project
- typical information: character, location, item, and lore records; plot threads; research notes, images, and clippings; in series projects, shared records
- primary actions: create and edit records, link records to scenes, search and filter, and in some products auto-highlight and retrieve records while typing

### Snapshot / version view

- purpose: make rewriting safe
- typical information: stored versions of a unit, timestamps, differences against the current text
- primary actions: take a snapshot, compare, restore an earlier version

### Compile / export surface

- purpose: turn the project into a deliverable manuscript
- typical information: included units and their order, output format, formatting presets, front-matter and heading options
- primary actions: choose format and preset, select included units, export or print, save compile settings

## Important Rules / Behaviors

- **Moving a structural unit moves the book.** Dragging a scene card or tree row reorders the manuscript itself; planning surface and manuscript are views of one structure.
- **Synopsis, notes, and research never print unless explicitly included.** Compile includes prose units by default and excludes reference material, synopses, and comments.
- **Word counts are hierarchical.** A scene's words count toward its chapter and the book; excluding a unit removes it from both. Drafting order is not narrative order — the tree defines reading order, not writing order.
- **The continuity layer is user-maintained unless automation is present.** A character record is only as accurate as the author keeps it; auto-link or AI retrieval changes convenience, not ownership of the truth.
- **Snapshot and version behavior is per unit and product-specific** — on-demand snapshots, automatic history, or duplicated drafts; authors are expected to snapshot before major rewrites.
- **Series projects share the bible, not the prose.** Characters, locations, and lore are defined once and shared while each book keeps its own manuscript tree.
- **AI output is a draft, not canon.** Where AI features exist they propose text or critique from the continuity layer, and authorship remains the writer's.

## Variants

- **Desktop power tool** — local, file- or project-package-based; deep structure, snapshots, and compile control; a steeper learning curve (Scrivener, bibisco, Manuskript).
- **Cloud, ease-first writer** — browser and mobile clients, automatic sync, a simplified plot/write/edit flow for less tool-tolerant authors (Dabble).
- **AI-native / codex-centric platform** — the continuity layer is a linked wiki and AI assistance is integrated but optional; strong for discovery writers and series (Novelcrafter).
- **World-building-first suite** — the story bible and world modules are the center, with a word processor attached (Campfire Writing).
- **Method-guided tool** — the product teaches a method (snowflake, beat sheets, guided character questions) as its organizing metaphor (Manuskript, bibisco).
- **Local-first / open-source** — plain files the author owns, community development, no subscription (Manuskript).

A variant remains a variant while the structured manuscript, the continuity layer, the long-form lifecycle, and assembly all hold. A tool that keeps the structure but drops the prose, or keeps the prose but drops the structure, has crossed into a neighboring Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Distraction-free Writing Application | sibling, opposite weight | centers the attention surface; here the editor is one view inside structure, continuity, and compile |
| Document Editor / Word Processor | generalist ancestor | one continuous formatted document; here the book is a tree and the compiled document is an output |
| Outliner | adjacent structure tool | the tree *is* the content; here it is the book's structure and prose lives in leaf documents |
| Note-taking Application | adjacent reference tool | capturing fragments is the point; here notes serve a manuscript that is the point |
| Personal Knowledge Management / Wiki | adjacent continuity tool | a linked page network is the product; a codex here supports one narrative |
| Storyboard Application | adjacent visual planning | an image per unit for screen production; here units are prose scenes |
| Script Breakdown Application | different production stage | inventories a screenplay's shooting elements; this Type has no such model |
| Publishing Editorial Workflow | publisher-side counterpart | a publisher's staged process with roles and gates; this Type is author-side |
| Book Publishing Management | downstream business system | centers the title as a commercial product; this Type stops at the manuscript |
| Desktop Publishing / E-book Production | downstream formatting | performs page layout and typesetting; compile here produces a manuscript |
| Collaborative Document Editor | collaboration contrast | multi-user co-editing of one document is the center; novel tools are single-author |
| AI Writing Assistant | adjacent generator | generates text as its product; here AI is an optional accelerator |

The most important boundaries are with the Distraction-free Writing Application and the Outliner. Both share surface area with the Type — the first shares prose drafting, the second the tree — and the test is which machinery is the center: the attention surface, the tree as content, or the structured book plus continuity and assembly.

## Representative Products

- **Scrivener (Literature & Latte)** — the canonical desktop studio: binder tree, research area, corkboard/outliner, snapshots with compare, targets, and compile to Word/PDF/EPUB. The *desktop power-tool* pole. https://www.literatureandlatte.com/scrivener/overview
- **Dabble** — a cloud, browser-and-mobile novel writer built for ease: plot grid, character profiles, worldbuilding bible, drag-and-drop chapters and scenes, daily word-count tracking, comments, and export. The *cloud, ease-first* pole. https://www.dabblewriter.com/
- **Novelcrafter** — a cloud platform whose linked "Codex" bible tracks characters, places, and lore across a series, with planning grids and optional AI assistance. The *AI-native, codex-centric* pole. https://www.novelcrafter.com/
- **Campfire Writing** — a writing-and-worldbuilding suite (characters, maps, species, timelines, lore) with an integrated word processor and mobile app. The *world-building-first* pole. https://www.campfirewriting.com/
- **bibisco** — desktop novel-writing software (Windows, macOS, Linux, mobile) centered on chapters, scenes, storylines, locations, and guided character development. The *method-guided, structured-analysis* pole. https://www.bibisco.com/
- **Manuskript** — a free, open-source, cross-platform tool combining hierarchical outlining, goals, characters, plots, world notes, and a snowflake-method assistant. The *open-source, local-first, method-guided* pole. https://www.theologeek.ch/manuskript/

Adjacent for boundary context: **Plottr** — visual outlining and series-bible software that exports outlines to Word and Scrivener rather than drafting prose in-product — sits just outside the Type as a planning-only companion. https://plottr.com/

## Sources

Research date: **2026-09-13**

- Literature & Latte — Scrivener overview (binder, research, corkboard, outliner, targets, snapshots, compile): https://www.literatureandlatte.com/scrivener/overview
- Dabble Writer — product site and feature pages (plot grid, character profiles, worldbuilding bible, goals, editing): https://www.dabblewriter.com/
- Novelcrafter — product site and Codex page: https://www.novelcrafter.com/ , https://www.novelcrafter.com/features/codex
- Campfire Technology — product site and worldbuilding pages: https://www.campfirewriting.com/ , https://www.campfirewriting.com/worldbuilding-tools
- bibisco — product site and features/overview pages: https://www.bibisco.com/ , https://bibisco.com/writer-software-bibisco-features/
- Manuskript — project site (outliner, distraction-free mode, snowflake assistant, characters, plots, world): https://www.theologeek.ch/manuskript/
- Plottr — product site (visual timeline, templates, series bible, exports): https://plottr.com/

> Sourcing limitations: written from official product and vendor pages fetched on 2026-09-13; full user guides were not retrieved, so capability claims are stated at the level the overview pages support, and no numeric limits or default settings are asserted. The yWriter page returned HTTP 500 and is not cited. Plottr is boundary context only: its documented output is an outline exported to drafting tools, not prose authored in-product, so no product-specific mechanism is generalized into the Type definition.

Detailed boundary tests and evidence grades are recorded in the paired Research Notes.
