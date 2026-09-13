# Research Notes — Novel Writing Application

Research date: **2026-09-13**

Methods: direct reading of existing corpus leaves in `applications/`, the `DIRECTORY.md`
category index, and official product/vendor pages fetched during this pass. The
`application-atlas` MCP server (`search_similar` / `get_leaf`) was not exposed as a tool
in this environment, so nearest-neighbor discovery was done by listing and reading the
corpus directly (see Uncertainties).

Evidence grades used below:

- **A** — multiple official vendor pages plus product documentation fetched and read
- **B** — official product/feature pages fetched and read (marketing/overview level)
- **C** — direct corpus inspection plus reasoned inference from at least two products
- **D** — single-source or inference not confirmed elsewhere

## Boundary Findings

### 1. Novel Writing Application vs. Distraction-free Writing Application

- Pair: `novel-writing-application` (proposed) ↔ `distraction-free-writing-application` (existing leaf).
- Distinguishing test: remove the manuscript tree, the continuity layer, and compile
  settings from a novel writer and leave only the editor; if the product's promise is
  still intact, it was a distraction-free writer. Remove the attention surface from a
  distraction-free writer and you get a plain editor, not a novel writer.
- Evidence: the distraction-free leaf defines its core as a persistent text document +
  a distraction-free composition surface + drafting primacy, and explicitly subordinates
  organization to the writing surface; Scrivener's overview documents a binder, research
  area, corkboard/outliner, targets, snapshots, and compile as the center, with
  full-screen composition as one optional mode among them. **Grade A.**
- Result: distinct Type. The centers of gravity are opposite (surface vs. project).

### 2. Novel Writing Application vs. Outliner

- Pair: proposed ↔ `outliner` (existing leaf).
- Distinguishing test: in an outliner the item tree *is* the content; delete the prose
  and the story material and a novel writer's remaining tree is a plot outline, which is
  outliner territory. In an outliner, adding long prose to items is an overlay, not the
  product's reason to exist.
- Evidence: the outliner leaf defines the item as the atomic unit and subtree operations
  as the defining act; Scrivener's binder is an ordered tree whose leaves are separately
  authored prose documents, and whose tree is the compiled book's table of contents.
  Manuskript documents both a hierarchical outliner and a separate writing editor with
  characters/plots/world. **Grade A (two products) → B overall.**
- Result: distinct Type; shared surface (a nested list), different unit of meaning.

### 3. Novel Writing Application vs. Document Editor / Word Processor

- Pair: proposed ↔ `document-editor` (existing leaf).
- Distinguishing test: remove the structured tree and the continuity layer — if one
  continuous formatted document remains and that is still a complete product, it is a
  document editor. A novel writer with those removed has no manuscript anymore, only
  text fragments.
- Evidence: the b2b/2d exemplars and the category index place Document Editor in
  Documents & Writing as a flat-document Type; Dabble's own comparison positions Google
  Docs and Word as editors that "struggle with large manuscripts", while it organizes
  chapters/scenes/plot separately. **Grade B.**
- Result: distinct Type; the document editor is the generalist ancestor.

### 4. Novel Writing Application vs. Note-taking / Personal Knowledge Management

- Pair: proposed ↔ `note-taking-application`, `personal-knowledge-management` (existing leaves).
- Distinguishing test: remove the manuscript and keep the continuity layer — if the
  product still stands on its own as a linked note/wiki product, it was PKM. Remove the
  continuity records from a novel writer and the manuscript still stands; the reverse is
  not true for a PKM tool.
- Evidence: the outliner leaf's boundary discussion distinguishes library-level
  organization from in-content trees; Novelcrafter's Codex is explicitly a supporting
  wiki for one narrative ("for a true insight into your world"), not a general note
  network. Campfire's worldbuilding modules serve stories. **Grade B.**
- Result: distinct Type with a shared wiki-like surface.

### 5. Novel Writing Application vs. Storyboard Application

- Pair: proposed ↔ `storyboard-application` (existing leaf).
- Distinguishing test: if the unit of planning carries an image (a drawn frame) as its
  primary content, it is storyboarding; if it carries prose and a synopsis, it is a
  novel writer's planning surface. Remove the prose and the story bible and Plottr-like
  scene cards remain — but without images they are still outline cards, not storyboards.
- Evidence: the corpus's Storyboard Application is classified under 04.19 Storyboarding;
  the 2D-animation leaf describes storyboarding as static planning panels with no
  animation. **Grade C** (corpus structure plus definitional contrast; no storyboard
  vendor fetched this pass).
- Result: distinct Type; adjacent only through "planning before production".

### 6. Novel Writing Application vs. Script Breakdown Application

- Pair: proposed ↔ `script-breakdown-application` (existing leaf, read in full).
- Distinguishing test: a breakdown app requires a screenplay as source of record and
  produces per-scene element inventories and category reports; a novel writer neither
  parses scenes into production categories nor emits breakdown sheets.
- Evidence: the breakdown leaf's defining core is the script + scene records + element
  tags + breakdown outputs. Nothing in the novel-writing product set (Scrivener, Dabble,
  Novelcrafter, Campfire, bibisco, Manuskript) produces production-element inventories.
  **Grade A (breakdown leaf) → B.**
- Result: distinct Type, adjacent through the shared idea of a scene as a unit.

### 7. Novel Writing Application vs. Publishing Editorial Workflow / Book Publishing Management

- Pair: proposed ↔ `publishing-editorial-workflow`, `book-publishing-management` (existing leaves).
- Distinguishing test: if the system's unit of record is a publishing work moving through
  role-assigned editorial gates with deadlines, it is an editorial workflow; if it centers
  title P&L, contracts, royalties, and metadata, it is publishing management. A novel
  writer's unit is the author's manuscript, and its users are authors, not publishers.
- Evidence: the publishing-editorial-workflow leaf states the workflow "tracks the
  process; it does not do the editing", and that writing/revising happen in editors
  outside it. **Grade A.**
- Result: distinct Types; they meet at submission/handoff, not in structure.

### 8. Novel Writing Application vs. Desktop Publishing / E-book Production

- Pair: proposed ↔ `desktop-publishing-application` (existing leaf).
- Distinguishing test: if the product's center is page layout and typesetting for print
  or retail, it is DTP. Novel writers' compile produces a manuscript or a basic
  DOCX/PDF/EPUB export, not designed pages; Scrivener's own compile description is
  "prepare your manuscript for sharing", with EPUB generation as one format among many.
- Evidence: Scrivener overview (compile/export) and Campfire's separate publishing
  pathway. **Grade B.**
- Result: distinct Types; compile is a bridge out, not layout authoring.

### 9. Novel Writing Application vs. plot-outlining companion (Plottr)

- Pair: proposed ↔ a possible "Plot Outlining Application" (no existing leaf found).
- Distinguishing test: does the product author prose? Plottr documents visual timelines,
  templates, character sheets, a series bible, and export "to either MS Word & Scrivener"
  so the author writes elsewhere; it deliberately positions itself as the planning
  companion rather than the writing surface.
- Evidence: Plottr product page, fetched. **Grade B.**
- Result: Plottr is treated as adjacent/boundary context, not as a representative member,
  because in-product prose drafting is part of the L0 core. Flagged: if a future leaf for
  "Plot Outlining Application" is created, the two must be cross-linked.

### 10. Story bible formality (internal boundary)

- Test within the Type: Scrivener's continuity layer is a research folder plus reusable
  templates rather than typed entity records; bibisco exposes characters, locations, and
  storylines as structured areas; Novelcrafter's Codex is typed and link-aware; Campfire
  ships discrete worldbuilding modules.
- Evidence: all six representative product sites fetched. **Grade B.**
- Result: the formality of the continuity layer is a variant axis, not a definitional
  requirement — recorded so the Type is not overfit to codex-style products.

## Uncertainties

1. **yWriter not verified.** `https://www.spacejock.com/yWriter7.html` returned HTTP 500
   during this pass. yWriter is absent from Representative Products and Sources entirely;
   no claim rests on it. (Grade: verified failure.)
2. **Documentation depth.** For all six representative products, only product, features,
   and overview pages were readable; full user guides/help centers were not fetched. All
   capability statements are therefore calibrated to overview level, and no numeric
   limits, default settings, feature counts, or exact stage vocabularies are asserted.
   (Grade B.)
3. **Planning-only tools.** It is genuinely arguable whether a prose-less outliner such as
   Plottr is a sub-variant or a separate Type. This pass decided *separate/adjacent*
   because in-product prose authoring is part of the settled L0 core. Reasonable reviewers
   could place the seam elsewhere. (Grade C, flagged for joint review.)
4. **AI centrality.** Whether AI-native fiction platforms are the same Type or an emerging
   sub-Type is unresolved. This pass treats AI as an optional accelerator layered on the
   same core, since Novelcrafter documents that its interface is usable without AI. No
   separate AI-native Type is claimed. (Grade C.)
5. **No screenwriting leaf exists in the corpus.** Screenwriting applications share
   scene/outline structure with novel tools and several products serve both. Because no
   `screenwriting-application` leaf was found in `applications/` or `DIRECTORY.md`, the
   screenwriting relationship is described only inside Variants/Related, and a future leaf
   would need a boundary pass. (Grade C.)
6. **MCP search unavailable.** The `search_similar` / `get_leaf` MCP tools named in the
   brief were not available in this environment. Nearest neighbors were found by listing
   the 1806 application files, reading `DIRECTORY.md`, and grepping for `novel|fiction|
   manuscript|screenplay|story bible` across the corpus. It is possible a newly created
   leaf outside the indexed set was missed; the four nearest existing leaves read in full
   were `distraction-free-writing-application`, `outliner`, `script-breakdown-application`,
   and `publishing-editorial-workflow`. (Grade: process limitation.)
7. **Chinese display layer.** The Chinese name and thesis in the identity file are the
   authoring hint; per corpus policy the translated display layer is generated separately,
   so no Chinese text appears in the body.
