# Book Writing Application — Boundary Findings & Uncertainties

Research date: 2026-09-13

Identity settled during research: **Book Writing Application** (书籍写作应用). The
submitted thesis ("我想要开发一个写小书的辅助工具") described a book-writing aid
without naming a type; research against the corpus and the live product market
established the category as the author-facing, book-project-structured,
compile-to-edition tools (Scrivener, Atticus, Dabble, Reedsy Studio, Vellum,
Manuskript and peers), and no existing leaf covers it.

## Boundary Findings

Evidence grades: **A** = operational/feature documentation reachable and directly
observed; **B** = official product/landing page confirmed; **C** = inference from
adjacent documented types, not directly demonstrated for this pair.

### 1. Book Writing Application vs Document Editor

- **Pair**: this Type vs `document-editor`.
- **Distinguishing test**: Does the user own a *project of many movable manuscript
  units* whose reading order is editable and whose pages are produced by a compile
  step, or a *single self-contained artifact* with explicit formatting applied while
  writing and a page-shaped finish (print/PDF)? Remove the multi-unit project and the
  compile from a Book Writing Application and the remaining object is exactly a
  Document Editor.
- **Evidence grade**: A for both sides — document-editor.md (fetched corpus leaf) and
  the product pages of Scrivener (binder + compile) and Atticus (chapter reorder +
  export) document the structure directly. The load-bearing difference is the object:
  project-of-units vs single document; formatting timing is a secondary tell.

### 2. Book Writing Application vs Distraction-free Writing Application

- **Pair**: this Type vs `distraction-free-writing-application`.
- **Distinguishing test**: Is the product's *promise* the attention-preserving
  composition surface (chrome hidden, formatting deferred to protect focus), or the
  book project and its compiled output? A minimal distraction-free app with only a
  persistent text document and a hide-away editor becomes a Distraction-free Writing
  Application; the book structure and compile are what keep it here. Both can coexist
  in one product (Scrivener has a full-screen composition mode; Dabble has Focus Mode),
  so the test is center of gravity, not feature presence.
- **Evidence grade**: A — distraction-free-writing-application.md defines the Type by
  the attention surface and explicitly treats library/project machinery as the
  "studio pole" of that Type; the representative products here (Scrivener, Dabble,
  Reedsy Studio, Novlr) all present drafting as one stage inside a book project.

### 3. Book Writing Application vs Desktop Publishing / Page Layout Application

- **Pair**: this Type vs `desktop-publishing-application`.
- **Distinguishing test**: Is the output assembled from a structured linear manuscript
  by a compile step, or by placing freely positioned frames on a page canvas and
  threading text stories through them? Remove the compile and substitute a page canvas
  with free frames → Desktop Publishing. Vellum is the closest market case and was the
  hardest call: it imports a manuscript and concentrates on producing editions, but it
  still operates on a linear manuscript with automatic chapter/TOC building rather than
  a free-placement layout canvas, so it is documented here as the
  production-emphasis variant rather than as DTP.
- **Evidence grade**: A for desktop-publishing-application.md and for Vellum's
  documented import→build→style→generate flow (B); the Vellum classification is the
  single most contestable boundary in this leaf (see Uncertainties).

### 4. Book Writing Application vs Book Publishing Management / Publishing Editorial Workflow / Author Management Platform

- **Pair**: this Type vs the publisher-side family (`book-publishing-management`,
  `publishing-editorial-workflow`, `author-management-platform`).
- **Distinguishing test**: Who is the user and what is the managed object? Replace the
  author's private workroom with a publisher's system of record over titles,
  contributors, contracts, rights, royalties, and metadata feeds → Book Publishing
  Management. Replace it with a staged, gate-and-assignment editorial process over
  submissions and manuscripts → Publishing Editorial Workflow. Center it on the
  creator registry and the settlement loop → Author Management Platform. None of these
  contains the author's drafting environment; they manage the book as a commercial or
  process object.
- **Evidence grade**: A — all three sibling leaves are in the corpus and were read
  directly; they document no manuscript-composition surface.

### 5. Book Writing Application vs eLearning Authoring Tool

- **Pair**: this Type vs `elearning-authoring-tool`.
- **Distinguishing test**: Add learner-facing interactivity (questions, branching,
  scoring) and a delivery package for an LMS/xAPI consumer; the deliverable becomes a
  course → eLearning Authoring Tool. The shared shape is "authoring tool with a
  publishable deliverable"; the differentiator is the consumer (a learner who operates
  the content vs a reader who reads it) and the output semantics.
- **Evidence grade**: A for elearning-authoring-tool.md; B for this side. Both are
  documented as authoring tools that produce a deliverable, which is why the boundary
  needs the consumer test rather than the "authoring" label.

### 6. Book Writing Application vs Outliner / Note-taking / PKM

- **Pair**: this Type vs `outliner`, `note-taking-application`,
  `personal-knowledge-management-application`.
- **Distinguishing test**: Strip the manuscript prose and the book-format compile and
  keep only a hierarchy whose main operation is subtree restructure → Outliner. Replace
  the single book with a library of fragments → Note-taking. Replace it with a growing
  network of linked notes across many topics → PKM. Book Writing Applications contain
  an outliner-like structure and a notes store, but both serve one book-shaped output.
- **Evidence grade**: A — outliner.md and the product pages (Scrivener outliner,
  Dabble notes, Reedsy Boards) document the components; the boundary is by purpose
  (means to a book vs the tree/network as the product).

### 7. Book Writing Application vs planning-first tools (Plottr and peers)

- **Pair**: this Type vs planning/outlining products such as Plottr (no leaf exists;
  Plottr was fetched as market context).
- **Distinguishing test**: Remove the manuscript-composition surface and the
  book-format output, keeping only visual outlining and a story bible whose export is
  an outline handed to another app → an outlining/planning tool, not this Type. Plottr
  itself states the author goes on to "write the book in your favorite writing app",
  which makes its position explicit.
- **Evidence grade**: B — Plottr's official page was fetched directly and states the
  handoff; no corpus leaf covers this neighbor yet, so this boundary is recorded but
  not cross-checked against an existing Type.

## Uncertainties

- **Vellum's placement.** Vellum is the strongest alternative classification. Its
  official page describes import, build, style, preview, and generate, with minimal
  emphasis on drafting. It is included as a representative product for the
  formatting/production-emphasis variation, but a future reviewer could reasonably
  reclassify it as a book-formatting/production tool adjacent to this Type. Grade: B.
- **No primary operational documentation.** For every representative product only the
  official product/landing page was reachable; no help centre or user manual was
  fetched. Exact compile-option inventories, numeric limits, default settings, and
  pricing details are therefore not asserted. Grade: A (that this limitation exists).
- **Market naming is unstable.** Vendors use "book writing software", "novel writing
  software", "writing app", "writing studio", and "authoring" interchangeably, and the
  same products are marketed to novelists, non-fiction authors, and screenwriters. The
  Type name was chosen as the clearest category label, not because the market agrees on
  it. Grade: B.
- **AI is a moving layer.** LivingWriter and several peers now embed generative
  drafting/rewriting/analysis. It is treated as an optional capability; whether
  AI-forward products drift into a distinct Type (or toward a general AI writing
  assistant) is left open. Grade: B.
- **Series containers and multi-book projects.** Some products hold a whole series in
  one container sharing characters and lore. It is treated here as a variant of the
  same Type rather than a separate one; the threshold at which a series bible product
  becomes a distinct knowledge-base Type is not settled. Grade: C.
- **yWriter unverifiable.** https://www.spacejock.com/yWriter7.html returned HTTP 500
  on the research date; the product was dropped rather than cited from memory.
- **Collision-check tooling unavailable.** The `application-atlas` MCP tools
  (search_similar / get_leaf) were not exposed in this environment; boundary work was
  done by directly reading the nearest corpus leaves (`document-editor.md`,
  `distraction-free-writing-application.md`, `desktop-publishing-application.md`,
  `book-publishing-management.md`, `publishing-editorial-workflow.md`,
  `author-management-platform.md`, `elearning-authoring-tool.md`, `outliner.md`) and
  by fetching the live product sites. No corpus leaf was found that documents this
  Type; the nearest neighbors are all documented above.
