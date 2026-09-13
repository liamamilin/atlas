# Professional Typesetting Application

## Overview

A **Professional Typesetting Application** is a document-composition application in which the document is authored as a plain-text source annotated with markup, and a typesetting engine computes the composed, paginated output — line breaking, hyphenation, justification, pagination, and generated structures such as numbering and references — from that source. The deliverable (most commonly a PDF today) is regenerated from the source on demand, and the dominant working loop is *edit the source → compose → inspect the output → fix problems → repeat*.

The defining core is small:

```text
Marked-up plain-text source (the document of record)
└── Reusable design layer (classes / macro packages / styles / templates)
    └── Typesetting engine computes the composed pages
        └── Regenerated paginated deliverable (PDF, print, or other formats)
```

Everything else the market associates with the category — polished editing surfaces, instant preview, collaboration, math typesetting, package ecosystems, template galleries — is standard structure that mature products add around that core. The products of this family describe themselves as "typesetting systems" or "document preparation systems"; hosted products describe themselves as editors and collaboration platforms built over such engines. This application shares only its terminus — paginated output — with desktop publishing / page layout software; it differs fundamentally in how the pages come into being (see Related Application Types).

## Users & Context

Primary users are people who need documents whose length, structure, or precision exceeds what hand-layout or a word processor provides well:

- **academic and scientific authors** — journal articles, theses, conference papers; they concentrate on content and delegate page design to a document class or template
- **technical and engineering authors, and programmers** — reports, technical documentation, software manuals and manual pages, often produced inside toolchains and version control
- **publishers and long-form producers** — books and document series that share one design across many volumes or many authors
- **teams and institutions** — via hosted platforms where several authors work on the same sources with shared templates

The typical reason to choose this kind of application: the document (or document set) is long or highly structured; typographic consistency and reproducibility matter more than visual improvisation; or the content demands machinery that engines are built for — complex mathematical notation, automatic bibliographies, cross-references across hundreds of pages.

## Core Model

### The Defining Core

**The marked-up plain-text source is the document of record.** The user authors the document itself as text — usually plain text — annotated with markup that declares what things *are*: this is an article of a given class, this line is a title, this passage is a section, this is a citation. The source is the authoritative artifact. It can be edited in any text editor, compared and merged like code, stored in version control, and passed between people and systems. Nothing about the page exists in the source; the page exists only after composition.

**The reusable design layer.** Markup typically declares structure rather than appearance. Appearance lives in a reusable layer above the content: document classes, macro packages, style and template definitions. This division is stated outright in the family's own founding philosophy — the author should not have to worry about the appearance of the document, and design should be left to document designers. In practice this means a user selects or builds a design layer (or inherits an institutional one), and the same design governs every document that uses it.

**The typesetting engine's composition.** A typesetting engine reads the source and computes the composed pages. It decides where lines break, how words hyphenate, how paragraphs justify, where pages break, and how generated material — numbering, cross-references, tables of contents, bibliographies, indexes — is assembled. The user does not position content on a page; the user states content and rules, and the engine performs the composition. Composition parameters (line widths, spacing, hyphenation behavior, page geometry) are set in the source or the design layer, not by dragging.

**The regenerated paginated deliverable.** Producing output is an explicit step: a compile or format action turns the source into the deliverable. The output is always derived from the source — the same source regenerates the same output — and the deliverable is re-produced whenever the source or the design changes. Output formats vary by product: PDF is dominant today, while PostScript, DVI, HTML-class formats, and image formats are documented across the family, historically and currently.

### What Mature Products Add

These capabilities are not what makes the product a typesetting application, but essentially all current products provide them, and users expect them:

- **Editing surfaces** — a source editor with syntax highlighting, autocompletion, and as-you-type syntax checks; in hosted products, a rich-text "visual" mode that remains a view over the same source.
- **Preview of the composed output** — a PDF viewer beside the editor, instant preview that recomposes as the user types, or automatic recompilation on a short interval.
- **Generated apparatus** — automatic numbering, cross-references, footnotes, figures and floats placed by the engine, tables of contents, bibliographies and citations, and indexes, all assembled from the source rather than maintained by hand.
- **Math typesetting** — notation support of professional depth, flagship of the academic and technical pole though not required for non-mathematical documents.
- **Diagnostics** — errors and warnings reported as logs against the source; some products stop composition at the first error, others attempt to produce output anyway.
- **Package and template ecosystems** — libraries of document classes, macro packages, and ready-made templates, installed locally or browsed in hosted galleries.
- **Collaboration** — real-time co-editing, track changes, commenting, and sharing, on hosted platforms.
- **Organizational surfaces** — project dashboards, access administration, version-control and reference-manager synchronization.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:   Marked-up text source
Realized as:  semantic commands in a document language;
              general markup with embedded scripting;
              plain text with request/macro lines;
              a project of several source files plus assets

Concept:   Reusable design layer
Realized as:  document classes + packages;
              style and template definitions;
              macro packages + user-defined macros;
              hosted template galleries

Concept:   Engine composition
Realized as:  a standalone typesetting engine invoked on the source;
              a compiler producing PDF/HTML directly;
              server-side compilation in a hosted platform;
              an instant-preview rendering loop

Concept:   Deliverable
Realized as:  PDF; PostScript; DVI; HTML; PNG/SVG;
              print-ready output; slide decks
```

A reader who has only seen one product should be able to recognize any other product of this type from the core: a marked-up source, an engine that composes it, a design layer between them, and output regenerated from source.

## How It Works

The canonical workflow runs from empty project to delivered document:

**1. Choose or build the design layer.**

```text
Start a document or project
→ select a document class / template / macro package
→ (or build one, when a whole series must share a design)
→ set page geometry and composition parameters
```

**2. Write the source.**

```text
Type content into the markup language
→ declare structure: title, sections, figures, tables, citations
→ insert notation (mathematics, code, data-loaded tables)
→ let markup reference other parts of the document
```

**3. Compose.**

```text
Run the compile/format step
→ the engine computes line breaks, hyphenation, justification, pagination
→ the engine assembles generated material (numbering, references, contents)
→ composition reports errors or completes
```

**4. Inspect and fix.**

```text
View the composed output (preview pane, PDF viewer)
→ read the error/warning log against the source
→ correct the source (or the design layer)
→ compose again
```

**5. Produce the deliverable.**

```text
Compose the final output
→ export/produce in the target format (PDF, other formats)
→ deliver: submission, printing, publication, or hand-off
```

The interaction loop that dominates daily work is steps 2–4: write, compose, inspect, fix. In modern hosted products this loop can run nearly continuously — automatic recomposition while the user types — but it remains the same loop: the pages are always computed from the source, never positioned by hand. A second, distinct workflow exists at the design-layer level: building and refining a class, template, or macro package so that a whole series of documents typesets consistently — work done once, inherited by every document that uses the layer.

## Interfaces

The following surfaces are described in conceptual terms; exact layouts and names vary by product.

### Source editor

The primary working surface: the document's source text with markup.

- shows the marked-up source (often split across multiple files in a project), with syntax highlighting and, commonly, autocompletion and on-the-fly syntax checks
- primary actions: write and edit markup, insert structural elements, navigate files

### Compose / produce control

The action that turns source into output — a button in hosted and desktop products, a command-line invocation in toolchains.

- typical options: compile mode (fast draft vs complete), error handling (stop at first error vs continue), automatic recomposition
- primary actions: compose, recompose, configure how composition proceeds

### Output preview

The composed document as the engine produced it.

- shows the paginated result (commonly PDF), usually beside the source and kept in step with the latest composition
- primary actions: scroll/inspect pages, move between source and output locations, export/produce the final file

### Diagnostics / log console

The engine's report against the source.

- typical information: errors, warnings, composition log
- primary actions: jump from a message to the offending source location, fix, recompose

### Project / package management

The surfaces that organize sources and reusable machinery.

- typical information: project file tree, assets (images, bibliographies), installed or available packages/classes, templates
- primary actions: add/remove files, manage packages, start from a template

### Collaboration surfaces (hosted pole)

On hosted platforms: sharing and permission controls, real-time co-editing, track changes, comments, and version-history or version-control integration.

## Important Rules / Behaviors

- **The source is the authority.** What the user edits is the document; the composed output is always a derived artifact. Hand edits made directly to output (for example, in a PDF) are lost at the next composition — changes happen in the source or the design layer.
- **The engine owns the composition.** Line breaks, hyphenation, pagination, and placement of generated material are computed. The user influences them through markup and design-layer parameters, not by moving objects. Fighting the engine's decisions is done by changing the rules, not the result.
- **Design is delegated, then inherited.** Changing the design of a document normally means changing its class, template, or macro package — one change updates every page and every document that shares the layer.
- **Errors are composition-time and user-facing.** A markup mistake surfaces as an error or warning in the log rather than as a silent visual defect. Products differ: some stop at the first error, others attempt to complete the output anyway; as-you-type syntax checks catch a first tier of problems early.
- **Generated material can need further composition.** Structures that depend on the whole document — cross-references, bibliographies, tables of contents — may require additional passes to settle, depending on the engine. Hosted products manage this machinery (including cached intermediate state) for the user.
- **Regeneration is reproducible.** The same source with the same design layer yields the same output. This is what makes the source, not the artifact, the thing stored, versioned, and shared.

## Variants

- **Local engine + editor distributions** — a typesetting engine bundled with editors and maintenance tools, installed on the user's machine; the classic desktop realization.
- **Command-line formatter in toolchains** — the engine as a batch program inside Unix-style systems, composing manual pages and technical documents as part of software workflows; the oldest continuously-alive realization.
- **Hosted collaborative platforms** — the engine plus editor running as a browser service: projects on a dashboard, server-side composition, real-time collaboration, template galleries, organizational administration.
- **Modern scripting-first engines** — newer languages that combine markup with scripting and deliver instant preview, positioning themselves as alternatives to both word processors and the older typesetting systems.
- **Rich-text hybrids** — visual editing modes over the same source, so users who never learn the markup can still edit it; the source remains the record.
- **Document-series production** — the same core used to run a design across a book series or institutional template: the design-layer workflow above becomes the main event.
- **Slide and web output** — some engines produce presentation decks and HTML-class output from the same source system, alongside print-oriented formats.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Desktop Publishing Application / Page Layout Application | adjacent, same terminus, different mechanism | there the user assembles pages by placing and adjusting frames on a page canvas, and the publication file itself is the document; here the user writes marked-up text, the engine computes the pages, and the source is the document. Both produce paginated output; the authoring mechanism is mutually exclusive |
| Document Editor / Word Processor | adjacent | a word processor is a live WYSIWYG page: layout is applied through menus and formatting, there is no markup source of record, and no separate composition step. The typesetting family's own self-descriptions explicitly draw this line ("not a word processor") |
| Markdown Editor | adjacent, mechanism overlap | markdown tools also author marked-up text, but lack the professional composition machinery — typographic depth, macro/class design layer, generated apparatus — that defines this Type; the boundary is the composition engine, not markup itself |
| Presentation Application | capability overlap | typesetting systems can emit slide decks from the same sources; the presentation Type centers on screen-deck delivery, not document composition |
| Academic Paper Reader | downstream | reads and annotates the typeset output; does not author or compose it |
| Font Editor / Typeface Design Application | supply chain | produces the fonts this family consumes; composes no documents |
| Collaborative Document Editor | adjacent | collaboration over a shared visual document; here collaboration (on hosted surfaces) is over shared sources that recompose into output |

## Representative Products

- **LaTeX** — the dominant document-preparation system for technical and scientific publishing, running on the TeX typesetting engine; distributed through TeX distributions and the CTAN package network.
- **Typst** — a modern markup-based typesetting system combining language, compiler, and collaborative web app; positions itself as an alternative to both word processors and LaTeX.
- **Overleaf** — the leading hosted LaTeX editor and collaboration platform: browser projects, server-side compilation, real-time co-editing.
- **groff (GNU roff)** — the GNU reimplementation of the AT&T troff lineage: a typesetting system that reads plain text with formatting commands and produces PostScript, PDF, HTML, or DVI; long associated with Unix manual pages.

## Sources

Research date: **2026-09-08**

- LaTeX Project — "An introduction to LaTeX": https://www.latex-project.org/about/
- LaTeX Project — "Get LaTeX" (distributions, CTAN, online services): https://www.latex-project.org/get/
- Typst — Documentation Overview: https://typst.app/docs/
- Typst — Tutorial: https://typst.app/docs/tutorial/
- Overleaf — Documentation: https://docs.overleaf.com/ (including "Recompiling your project": https://docs.overleaf.com/getting-started/recompiling-your-project.md)
- GNU — "GNU roff (groff)": https://www.gnu.org/software/groff/
- GNU — "GNU roff (groff) Manuals Online": https://www.gnu.org/software/groff/manual/

> Sourcing limitation: other systems of the same family (ConTeXt, SILE, LyX, and commercial XML/structured publishing tools) were not sampled this pass; their fit with the described core is assumed from family self-identification but not directly evidenced. Whether generated material such as cross-references requires additional composition passes was not directly evidenced either; the document uses qualified wording for that behavior. Precise operational facts (compile-time limits, project-size limits, version-specific defaults) are deliberately not stated.

Detailed evidence, product-by-product observations, the cross-product comparison, and the boundary analysis against desktop publishing / page layout are recorded in the paired Research Notes.
