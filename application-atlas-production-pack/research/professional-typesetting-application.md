# Research Notes — Professional Typesetting Application

Directory leaf: §04.17 Publishing & Layout — "Professional Typesetting Application"
Research date: 2026-09-08
Status of adjacent flags: this pass is responsible for the pending mechanism-test flag from the desktop-publishing-application pass (interactive WYSIWYG frame layout vs markup/batch-driven composition) and for re-checking the resolved DTP↔page-layout alias finding against this Type.

---

## Research Goal

Establish what the "professional typesetting" family of software actually is, as realized in real products: what its input of record is, what its composition engine does, what its working loop is, what its interfaces are, and — critically — whether it is the same Application Type as the already-documented Desktop Publishing / Page Layout Application (which also produces paginated output) or a distinct Type.

## Initial Boundary (hypothesis before research)

- Working hypothesis: this leaf names the markup-driven typesetting family (TeX/LaTeX, troff/groff, ConTeXt, Typst, …) — systems where the user authors a plain-text source annotated with markup, and a typesetting engine computes the pages (line breaking, hyphenation, justification, pagination, generated apparatus).
- Nearest neighbors: Desktop Publishing Application / Page Layout Application (interactive frame layout, already documented as one Type under two labels); Document Editor / Word Processor (WYSIWYG stream editing); Markdown Editor (light markup, shallow composition); XML/structured publishing pipelines (unexamined here).
- The DTP pass left an explicit open question: "apply the mechanism test (interactive frame manipulation vs markup-driven batch composition) and decide the Type boundary here." This pass must answer it.
- Unknowns at start: whether the market self-labels as "professional typesetting application"; whether the compile loop and error surface are as central as suspected; whether output formats other than PDF are definitional; how much of the family survives a pre-GUI historical check.

## Research Questions

1. What do the products call themselves, and what is their stated purpose and audience?
2. What is the input of record — what does the user actually author and edit?
3. What does the engine compute at composition time, and how is document design delegated (document classes, macro packages, templates, styles)?
4. What is the dominant working loop, and what states/errors matter (compile errors, logs, helper state, recompiles)?
5. What interfaces does the user face (source editor, preview, log console, project/package management, collaboration)?
6. What deployment/surface variants exist (CLI formatter, distribution-bundled editor, hosted web app, scripting-first engine)?
7. **Mechanism test (owed to the DTP pass):** do the two families differ in what the user manipulates, who decides layout, where the artifact's authority lives, and the dominant loop — or only in packaging?

## Representative Products

Selection rationale: market representativeness + documentation completeness + different product philosophies + different customer tiers + historical breadth.

| Product | Pole represented |
|---|---|
| **LaTeX** (LaTeX Project) | the dominant markup typesetting system; academic/scientific/technical authoring; the "content vs design" philosophy stated by the project itself |
| **Typst** (Typst GmbH) | the modern scripting-first engine + editor; language + compiler + web app as one product; alternative to both word processors and LaTeX |
| **Overleaf** (Digital Science) | the dominant hosted collaborative surface for LaTeX; browser-based, real-time co-editing, organizational plans |
| **groff** (GNU) | the Unix troff lineage; CLI batch formatter; programmer/systems documentation (man pages); historical/platform-native pole |

Not sampled (recorded as uncertainty): ConTeXt, SILE, LyX (WYSIWYM hybrid), commercial XML/structured publishing tools (FrameMaker, Arbortext, XSL-FO formatters).

## Sources

All fetched 2026-09-08, all Tier-1 official:

- LaTeX Project — "An introduction to LaTeX" (About page): https://www.latex-project.org/about/
- LaTeX Project — "Get LaTeX" (distributions/CTAN/online services): https://www.latex-project.org/get/
- Typst — Documentation Overview: https://typst.app/docs/
- Typst — Tutorial ("When to use Typst"): https://typst.app/docs/tutorial/
- Overleaf — Documentation index: https://docs.overleaf.com/
- Overleaf — "Recompiling your project": https://docs.overleaf.com/getting-started/recompiling-your-project.md
- Overleaf — documentation query (workflow definition: project / source editor / recompile / PDF preview / error logs / collaboration / templates) answered from official GitBook docs pages: https://docs.overleaf.com/readme.md
- GNU — "GNU roff (groff)" project page: https://www.gnu.org/software/groff/
- GNU — "GNU roff (groff) Manuals Online": https://www.gnu.org/software/groff/manual/

Secondary/structure-only: LaTeX historic versions note (LaTeX 2.0 for TeX 1.0, released 11 December 1983, per latex-project.org/get "Historic LaTeX"); groff manuals page (328-page manual, 58 man pages) as ecosystem context.

---

## Product A — LaTeX

### Key observations (evidence layer A unless noted)

- Self-description: "LaTeX … is a document preparation system for high-quality typesetting. It is most often used for medium-to-large technical or scientific documents but it can be used for almost any form of publishing." (latex-project.org/about)
- Explicit boundary sentence: "**LaTeX is not a word processor!**" — "LaTeX encourages authors not to worry too much about the appearance of their documents but to concentrate on getting the right content." And: "it is better to leave document design to document designers, and to let authors get on with writing documents."
- Input of record shown by the project's own example: a plain-text markup source — `\documentclass{article} \title{…} \author{…} \begin{document} \maketitle Hello world! \end{document}` — glossed by the project as "This document is an article. Its title is … Its author is … The document consists of a title followed by the text." The markup is **semantic** (declares what things are, not how they look).
- Stated feature set: "Typesetting journal articles, technical reports, books, and slide presentations. Control over large documents containing sectioning, cross-references, tables and figures. Typesetting of complex mathematical formulas. Advanced typesetting of mathematics with AMS-LaTeX. Automatic generation of bibliographies and indexes. Multi-lingual typesetting. Inclusion of artwork, and process or spot colour."
- Architecture (Get page): "LaTeX is not a stand-alone typesetting program in itself, but document preparation software that runs on top of Donald E. Knuth's TeX typesetting system." TeX **distributions** (MacTeX, TeX Live, MiKTeX) "bundle together all the parts needed for a working TeX system … contain a complete TeX system with LaTeX itself and editors to write documents." Packages come from **CTAN**.
- Online services named by the project itself: "LaTeX online services like Overleaf, Papeeria, or CoCalc offer the ability to edit, view and download LaTeX files and resulting PDFs."
- Historical anchor (same page): "LaTeX 2.0 for TeX 1.0 (released on 11 December 1983)" — the family predates every GUI layout canvas.

## Product B — Typst

### Key observations (evidence layer A)

- Self-description: "Typst is a markup-based typesetting system that combines powerful automation and high-quality typography with speed and ease of use. This makes it suitable for documents of any complexity. Typst is a great alternative to both word processors and LaTeX." (typst.app/docs overview)
- Three-part architecture, in the docs' own words: "The term Typst refers to three concepts: The Typst language, the Typst compiler, and the Typst web app. The language is what you write, the compiler translates files in the Typst language into PDFs, HTML pages, and other formats, and the Typst web app lets you work collaboratively on Typst projects in your browser."
- Input of record, from the tutorial: "Typst takes text files with markup in them and outputs PDFs." "This tutorial does not assume prior knowledge of Typst, other markup languages, or programming. We do assume that you know how to edit a text file."
- Use cases named: "any long form text such as essays, articles, scientific papers, books, reports, and homework assignments… any documents containing mathematical notation… [and] any set of documents that share a common style, such as a book series" (styling/automation emphasis).
- Working surfaces: "The app gives you instant preview, syntax highlighting and helpful autocompletions. Alternatively, you can follow along in your local text editor with the open-source CLI."
- Reference structure of the language/library (documented capability map): Model layer — Bibliography, Cite, Document, Figure, Footnote, Heading, Numbered List, Outline, Quote, Reference, Table, Title; Layout layer — Align, Columns, Grid, Page, Page Break, Place, Stack, Rotate/Scale/Move; **Introspection** layer — Counter, Here, Locate, Location, Metadata, Query, State; Data loading — CSV/JSON/YAML/TOML/XML; Export — PDF, HTML, PNG, SVG, and PDF-specific machinery (Artifact, Attach, Data Cell, Header Cell, Table Summary); Guides include "Guide for LaTeX Users", Page Setup, Table, Accessibility.
- Tutorial arc: Writing → Formatting → Advanced Styling (build "a complex page layout for a scientific paper… author list and run-in headings") → Making a Template ("Build a reusable template from the paper").
- Web app concepts documented: Creating a Project, Folders, Export and Preview, Comments, Private Packages, Reference Sync, Git Sync, Presentation Mode, Invite by Email, Search, Single Sign-On.

## Product C — Overleaf

### Key observations (evidence layer A)

- Self-description (official docs): "Overleaf is a LaTeX editor and collaboration platform you can use in your browser—no install required. It supports both direct LaTeX editing and automatic server-side compilation into a PDF preview."
- Unit of work: a **project** — "Your work lives in a project with a project-level menu (rename, copy, download source, submit, etc.)"; a dashboard lists projects.
- Documented main workflow (docs' own numbered steps):
  1. Create/open a project
  2. Edit the source ("Use the Code editor (or switch to Visual editor if you prefer)")
  3. **Recompile** — "Click Recompile to compile your .tex sources into the latest PDF. Compilation errors/warnings show up in the error logs."
  4. Preview the PDF ("The PDF viewer shows the compiled output produced by your latest recompile")
  5. Read error logs and fix issues
- Recompiling page (direct fetch): "A key part of working with LaTeX is compiling your source (`.tex`, `.bib`, images, and other files) into a PDF." "You should compile frequently, and always fix any errors that you encounter as soon as they arise."
- Compile options documented: **Auto compile** ("Overleaf automatically compiles your document for you every few seconds"); **Compile mode** Fast [draft] ("skip over image file processing… all images will be replaced with empty boxes"); **Syntax checks** as you type (unmatched braces, undefined commands, missing/extra `\begin \end`); **Compile error handling** (default attempts to produce a PDF even with errors; "Stop on first error" mode stops and reports immediately); **Recompile from scratch** ("The LaTeX compiler generates temporary helper files when it compiles your project. These files are preserved when possible between compiles" — cache clearing documented).
- Collaboration documented: "multiple authors can edit in real time, with sharing, track changes, commenting, and collaborator chat."
- Templates documented: "start from pre-loaded templates and examples."
- Organizational tier documented in docs structure: "Admins, groups, and organizations" section (groups, SSO).
- Note: the Visual editor is an alternate **view** over the same LaTeX source — the docs describe "direct LaTeX editing" as the primary mode and the source (downloadable via the project menu) as the portable artifact. (Evidence A for surface; the "view over source" characterization is an A+B inference from the same pages.)

## Product D — groff

### Key observations (evidence layer A)

- Self-description (GNU project page): "groff (GNU roff) is a typesetting system that reads plain text input that includes formatting commands to produce output in PostScript, PDF, HTML, or DVI formats or for display to a terminal."
- Command vocabulary layering, in the project's own words: "Formatting commands can be low-level typesetting primitives, macros from a supplied package, or user-defined macros. All three approaches can be combined."
- Heritage and niche: "A reimplementation and extension of troff and other programs from AT&T Unix, groff is widely available on POSIX and other systems owing to its long association with Unix manuals, including man pages. It and its predecessor have produced several best-selling software engineering texts. groff can create typographically sophisticated documents while consuming minimal system resources."
- Macro packages as the design layer: the page showcases the **mom** macro package ("Examples of groff usage with the mom macro package… which were used to generate the PDF version" of the project's own mission statement — the project typesets its own documents with it).
- Documentation surface: "groff installs about five dozen man pages"; "info groff presents a book-length manual documenting the language of the formatter in detail" — i.e., the formatter has a *language* to learn, per official framing.
- Surface: a command-line formatter inside Unix toolchains — no canvas, no GUI of its own; the "application" realization here is the formatter + macro packages + surrounding Unix tooling.
- Manuals page: the manual is 328 letter pages; 58 collected man pages — deep, official, and stable.

---

## Cross-product Comparison

| Dimension | LaTeX | Typst | Overleaf | groff |
|---|---|---|---|---|
| Self-label | "document preparation system for high-quality typesetting" | "markup-based typesetting system" | "LaTeX editor and collaboration platform" | "typesetting system" |
| Input of record | `.tex` semantic markup source | Typst text files with markup | project of `.tex`/`.bib`/asset sources | plain text + formatting commands |
| Design delegated to | document classes + packages (CTAN) | styling + templates (built via tutorial arc) | templates/examples + the underlying LaTeX classes | macro packages (mom, man, …) + user-defined macros |
| Engine role | TeX typesetting engine underneath | own compiler → PDF/HTML/… | server-side LaTeX compilation | own formatter → PS/PDF/HTML/DVI/terminal |
| Output | PDF-class paginated output (via TeX engines) | PDF, HTML, PNG, SVG | PDF preview; project/source download | PostScript, PDF, HTML, DVI, terminal |
| Dominant loop | edit source → run engine → view → fix | edit → instant preview → fix | edit → Recompile → PDF preview → error logs | write source → run formatter → view/ship output |
| Error surface | compile errors/warnings | compile errors; syntax check | error logs pane; syntax checks as you type; stop-on-first-error option | formatter diagnostics (manual-documented language) |
| Collaboration | not of the system itself | web app: collaborative projects | real-time co-editing, track changes, comments, chat | none (Unix toolchain) |
| Surface variant | distribution-bundled editors; online services | web app + open-source CLI | hosted web app | CLI in Unix toolchains |
| Audience pole | technical/scientific authors | long-form + math + shared-style document sets | academic teams, institutions | programmers/systems docs (man pages) |

Cross-product commonalities (evidence layer B):

1. **Plain-text markup source as the input of record** — 4/4. All four docs describe the user authoring text files containing markup/commands.
2. **Engine-performed composition** — 4/4. All four name an engine (TeX, Typst compiler, Overleaf's server-side LaTeX, groff formatter) that computes the output from the source; none describes the user positioning content on a page canvas.
3. **Design delegated to a reusable layer** — 4/4. Document classes/packages; styles/templates; macro packages. The LaTeX project states the philosophy outright ("leave document design to document designers"); groff and Typst document the macro/template layering as the standard way to work.
4. **Generated paginated output as the terminus** — 4/4, with multiple output formats across products (PDF dominant today; PostScript/DVI/HTML documented by groff and Typst; HTML/PNG/SVG by Typst).
5. **A compile/produce step in the working loop, with an error surface** — 4/4 (Overleaf documents it most explicitly; Typst calls it the compiler; groff is batch by design; LaTeX runs on the TeX engine).
6. **Generated apparatus machinery** — cross-references, bibliographies, indexes/tables of contents, numbering (LaTeX features list; Typst Model + Introspection layers; groff man-page machinery). Strength: B (documented across all sampled, with different mechanisms).
7. **"Typesetting system" family self-identification** — 3/3 engines self-label with "typesetting"; Overleaf labels as the editor/collaboration surface over one. The market's term for this family is "typesetting system"; the directory's "professional typesetting application" is the catalog label for the same referent (inference layer C, anchored in A).

---

## Canonical Model

### L0 — Defining Invariant (minimal)

Three jointly-held structures. Remove any one and the product stops being this Type:

1. **Marked-up plain-text source as the document of record.** The user authors the document itself as text annotated with markup that declares structure/semantics (and, optionally, formatting intent). The source is the authoritative artifact — editable, diffable, portable, regenerable. *(Remove → WYSIWYG editing surface: word processor or DTP canvas.)*
2. **Engine-performed typographic composition.** A typesetting engine computes the composed pages from the source — line breaking, hyphenation, justification, pagination, placement of content — under rules defined by a reusable design layer (classes/macros/styles/templates). The user does not hand-position content. *(Remove → plain text editor or code editor: no composition happens.)*
3. **Regenerated paginated deliverable via an explicit produce step.** The composed output (classically PDF; historically PostScript/DVI; also HTML-class formats in current products) is generated *from* the source by a compile/format action, reproducible from the same source; the dominant working loop is edit → compose → inspect → revise. *(Remove → interactive canvas editor where the edited artifact itself is the deliverable.)*

Jointly-held is load-bearing:

- 1 alone = marked-up text with no composition (a text/code editor's territory)
- 2 without 1+3 = a composition computation with no authorable source or artifact (absent as a product)
- 3 without 1+2 = generic print-to-PDF of anything
- 1+2 without 3 = a formatter that never yields a deliverable (absent as a product)
- 1+3 without 2 = text-to-output conversion without typographic composition machinery (lightweight converters below the Type)
- 2+3 without 1 = a composing application whose artifact is the edited object itself — that is the DTP/word-processor side of the mechanism boundary

### L1 — Common Mature Structure (expected in mature products, not definitional)

- Source editing surface with syntax highlighting, autocompletion, syntax checks (editor-bundled or companion)
- Preview of composed output — split view, instant preview, or auto-compile loops
- The reusable design layer made concrete: document classes, macro packages, style/template systems
- Generated apparatus: numbering, cross-references, footnotes, figures/floats, tables of contents, bibliographies/citations, indexes
- Math typesetting (flagship in the academic/technical pole; present in all sampled products' capability sets — but absent from real non-math use of the same products, so common-not-definitional)
- Compile diagnostics: errors, warnings, logs as a first-class user surface
- Multi-format output options
- Package/module ecosystems and distribution vehicles (CTAN-class repositories, bundled distributions)
- Font handling and typographic parameter control (kerning/hyphenation/justification settings exposed at the language level)

### L2 — Variant / Optional Structure

- Surface: bare CLI formatter inside toolchains (groff) ↔ distribution-bundled desktop editors ↔ hosted web apps (Overleaf, Typst app)
- Real-time collaboration, track changes, commenting, chat (hosted pole)
- Visual/rich-text editing modes over the same source (Overleaf Visual editor; LyX-class WYSIWYM hybrids — hybrid not sampled)
- Git/version-control sync, reference managers sync, organizational administration (SSO, groups)
- Template galleries as the starting point
- Presentation/slide output from the same source system (LaTeX "slide presentations" in its feature list; Typst Presentation Mode)
- Publish targets beyond print (HTML, PNG/SVG, web)

### L3 — Vendor-specific (research notes only)

- Typst's introspection machinery (Counter/Locate/Query/State) and its scripting language; PDF/Artifact-specific reference machinery names.
- Overleaf's specific compile options (Fast [draft] skipping image processing; stop-on-first-error; cache clearing), project menu items, Learn platform.
- groff's mom macro package; "five dozen man pages"; mission-statement self-typesetting.
- LaTeX's LPPL licensing, LaTeX3 project structure, CTAN as the package network, AMS-LaTeX naming.
- Overleaf/Papeeria/CoCalc named by the LaTeX Project as online services (vendor naming is evidence, not canonical structure).

## Rejected Findings

- **"Typesetting = math typesetting."** Rejected: math is pole-dependent; groff/man pages and the family's book/report use cases have no math requirement. L1 at most.
- **"Typesetting = LaTeX."** Rejected: groff, Typst (and, unsampled, ConTeXt/SILE) realize the same structure with different languages and engines; LaTeX itself is "document preparation software … on top of" TeX.
- **"A GUI editor is part of the definition."** Rejected: groff is a CLI formatter; the pre-GUI generations (troff, TeX, LaTeX 1983) satisfy the core; editors are wrappers/distributions added around engines.
- **"PDF is the definitional output."** Rejected: groff documents PostScript/PDF/HTML/DVI/terminal; Typst documents PDF/HTML/PNG/SVG. The invariant is *regenerated paginated deliverable*, not a specific format.
- **"Collaboration is definitional."** Rejected: single-author batch lineage; collaboration is the hosted pole's structure (L2).
- **"Must run on the TeX engine."** Rejected: Typst compiles with its own engine; groff has its own formatter.
- **"This Type is really XML publishing pipelines (XSL-FO etc.)."** Not established: those were not sampled; recorded as adjacent/unexamined rather than merged.
- **"The market calls this 'Professional Typesetting Application'."** Adjusted: products self-label "typesetting system" / "document preparation system"; Overleaf self-labels as editor/platform. The catalog label is retained as the leaf name with the market vocabulary documented.

## Boundary Findings

| Neighboring Type | Verdict | Mechanism-test detail / removal test |
|---|---|---|
| **Desktop Publishing Application / Page Layout Application** (siblings §04.17, already documented as one Type under two labels) | **Distinct Type — keep both.** The DTP pass's adjacent-mechanism flag is hereby answered: the families share only the terminus (paginated output), not the authoring model. | What the user manipulates: markup source text vs frames on a page canvas. Who decides layout: the engine computes composition from declared rules vs the user hand-positions/resizes elements. Artifact authority: the source file *is* the document and output is always derived/regenerated vs the publication file is the document and output is an export. Dominant loop: edit→compile→inspect→fix-errors vs place→flow→adjust→reflow. Remove markup authoring + engine composition → you get DTP. Remove interactive frame placement → you get this Type. Hybrid straddlers exist (WYSIWYM front-ends; structured/long-document DTP workflows) and sit on the seam, not in either core. |
| Document Editor / Word Processor (incl. Collaborative Document Editor) | Distinct. | Direct evidence from the family's own self-descriptions ("LaTeX is not a word processor!"; Typst as "a great alternative to both word processors and LaTeX"). Word processor: live WYSIWYG page, layout-by-formatting-commands-in-menus, no markup source of record. Remove the markup source + explicit produce step → word processor. |
| Markdown Editor | Adjacent, mechanism overlaps, composition depth differs. | Markdown editors author marked-up text (leg 1) but the mature typesetting engine machinery (professional line/page-breaking depth, macro/class design layer, generated apparatus) is what makes this Type; not sampled this pass, so asserted at moderate strength: the boundary is the professional composition engine and typographic quality bar, not markup itself. |
| XML/structured publishing pipelines (XSL-FO formatters, publishing houses' batch composition) | Same mechanism family, unexamined here. | Recorded as candidate realization of the same L0 (markup source + engine composition + regenerated output) — flagged for any future pass; not merged into this document's claims. |
| Presentation Application | Capability overlap, distinct Type. | Typesetting systems can *emit* slide decks (LaTeX feature list; Typst Presentation Mode); the presentation Type's center is deck delivery, not document composition. |
| Academic Paper Reader | Downstream consumer. | Reads the typeset output; does not author or compose it. |
| Font Editor / Typeface Design Application | Supply-chain adjacency. | Produces the fonts this Type consumes; no composition of documents. |

## Historical / Market-Sample Check

- The pre-GUI generations satisfy all three legs with zero GUI: AT&T troff (1970s Unix lineage per GNU's own framing) and TeX-era LaTeX (project-documented release of LaTeX 2.0 for TeX 1.0, 11 December 1983) — plain text + formatting commands/macros → engine composition → device output (DVI/PostScript). The definition therefore does not over-fit to modern hosted/editor-bundled realizations.
- The platform-native pole (groff in Unix systems; man pages) fits unchanged.
- The hosted/collaborative pole (Overleaf, Typst app) fits: same three legs, newer surface.
- No analog (pre-digital) ancestor is claimed: automated composition machinery is inherently computational; phototypesetting command codes are recorded here only as conceptual pre-history, not as evidence.

## Taxonomy Issues (for STATUS.md Boundary Issues)

1. **Mechanism test verdict (discharges the DTP pass flag):** Professional Typesetting Application and Desktop Publishing/Page Layout Application are **distinct Types** — keep both. Evidence basis: 4/4 sampled products document markup-source authoring + engine composition + compile-to-output, and none documents interactive frame placement; the DTP document's core (canvas/frames/stories) has no counterpart in any sampled typesetting product. The two are mutually exclusive on the authoring mechanism while sharing the output terminus.
2. Secondary note: the market self-label is "typesetting system" (engines) / "editor and collaboration platform" (hosted surface); the directory label "Professional Typesetting Application" is a catalog name for the same referent — retained, no directory change proposed.
3. Unexamined same-mechanism family (XML/XSL-FO batch publishing) flagged for any future pass that touches it.

## Uncertainties

- ConTeXt, SILE, LyX not sampled; assumed consistent with the derived core (same self-labeling family) but not directly evidenced this pass.
- Multi-pass compile behavior (references/bibliographies settling across runs) was **not** directly evidenced this pass; Overleaf's "helper files preserved between compiles" indirectly evidences stateful compilation. Final document uses qualified wording only.
- Commercial XML/structured-publishing products not fetched; their classification stays unexamined.
- Exact numeric facts (compile timeouts, project-size limits, version numbers) deliberately excluded from the final document; the one dated fact kept (LaTeX 2.0, 1983) is project-documented.
- Overleaf Visual editor's exact rendering behavior (what it shows for arbitrary LaTeX) not researched; kept as "alternate view over the same source" at moderate strength.

## Final Synthesis

The Professional Typesetting Application is the markup-driven composition Type of the publishing family: the user authors the document as plain-text source annotated with semantic/structural markup, a reusable design layer (document classes, macro packages, templates) carries the design decisions, and a typesetting engine computes the composed pages — line breaking, hyphenation, justification, pagination, and the generated apparatus — producing a regenerated, reproducible deliverable (PDF today; PostScript/DVI/HTML-class formats across products). The dominant loop is edit → compile → inspect → fix-errors, making the error log a first-class surface. The mechanism test demanded by the desktop-publishing pass is answered: **distinct Type, keep both** — the two families differ in what the user manipulates (source vs canvas), who decides layout (engine vs hand), where artifact authority lives (source-of-record vs publication-file-as-document), and the dominant loop, sharing only the paginated-output terminus. The definition survives the pre-GUI historical check untouched; collaboration, GUI editors, math, and PDF are common structure or variants, not the core.
