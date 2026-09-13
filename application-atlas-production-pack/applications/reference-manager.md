# Reference Manager

## Overview

A **Reference Manager** is a researcher's citation system of record: it maintains a persistent, organized library of bibliographic reference records, and it feeds those records into the user's manuscript as correctly formatted citations and an automatically generated bibliography.

The defining core is small — three structures that only work together:

```text
Bibliographic reference record (a typed, structured description of one published source)
└── Persistent reference library (accumulating, organized, searchable)
    └── Cite-and-format loop (records → formatted citations + bibliography
        in the written work, under a chosen citation style)
```

Everything commonly associated with modern products — browser capture, PDF attachments and built-in reading, notes, cloud sync, shared libraries, AI assistants — is standard or optional capability layered on this core. Older generations of this software (desktop bibliography tools with no PDF support at all) satisfy the definition completely, which is why none of those capabilities belong in it.

## Users & Context

The primary user is anyone who writes documents that cite published sources: graduate students, academic researchers and faculty, scientists, scholars, and — in spillover usage — professionals in research-bearing roles who produce cited reports and publications.

The product lives between two other environments:

- **the sources** — bibliographic databases, publisher websites, library catalogs, and PDFs already on disk, where references are discovered;
- **the word processor** — where the manuscript is written.

The reference manager collects from the former and feeds the latter. A secondary circle of usage is collaborative: co-authors drawing on a shared library while writing together, and — in institutionally licensed deployments — librarians who train and support researchers.

## Core Model

### The defining core

**1. The reference record.** The atom of the system: a typed, structured record describing one published source. It carries an item type — journal article, book, book chapter, conference paper, report, thesis, webpage, case, statute, and others — and the fields that type requires: creators, title, container (journal, book, publisher), date, pages, and identifiers such as DOI, ISBN, PubMed ID, or URL. The item type determines which fields exist and how the record can be cited. Files, notes, and links attach to the record as children; the record, not the file, is the primary object — a PDF is an attachment to a citable source, not a citable source in itself.

**2. The reference library.** The record population, accumulating across projects and years as durable working capital — not an inbox to clear. It is organized with folders or collections, tags or labels, quick and advanced search, saved searches, and duplicate handling. In some products a collection is an alias rather than a move: the same record can sit in many collections while existing once in the library.

**3. The citation style.** The formatting rule set that turns records into citations: author-date styles, note-based styles, numeric styles, and large catalogs of journal-specific styles (vendors claim catalogs in the thousands). The style is applied at output time, not stored in the record — the same record renders correctly in any style.

**4. The cite-and-format loop.** The defining workflow that binds the other three: while writing, the user pulls records from the library into the manuscript as formatted citations; the product generates and maintains a bibliography from the cited records; the whole document can be re-styled and refreshed against the library at any time.

### Standard capabilities

Mature products commonly add:

- **Acquisition machinery** — browser-extension capture from publisher and database pages (metadata plus PDF), lookup by identifier (ISBN, DOI, PubMed ID), search of databases and library catalogs from inside the product, file import (RIS, BibTeX, PDF) with automatic metadata extraction, and manual entry as the fallback.
- **Metadata repair** — automatic retrieval of missing details, explicit update/fix loops, and duplicate cleanup, because retrieved metadata is imperfect.
- **Attachments** — PDFs and other files attached to records, with full-text retrieval helpers.
- **Reading and annotation** — a built-in PDF reader with highlighting and notes in most current products (a capability, not the identity — see Related Application Types).
- **Notes and knowledge layers** — per-record notes; in some products a fuller layer of quotations, comments, and images linked to references, outline categories, and task planning.
- **Sync and sharing** — multi-device continuity; shared or group libraries with permissions for collaborative writing.

### One structure, many implementations

```text
Concept:          Citation output into the manuscript
Implementations:  word-processor plugin (dominant), copy-paste of formatted citations,
                  drag-and-drop / clipboard export, LaTeX/BibTeX export

Concept:          Style technology
Implementations:  an open citation style language, vendor style files,
                  custom style upload

Concept:          Library substrate
Implementations:  local desktop database, cloud-synced service, web app,
                  on-premise server
```

A reader who has only seen one implementation — say, a plugin inside a desktop word processor — should still be able to recognize a copy-paste or BibTeX-based workflow as the same Type.

## How It Works

### Build the library

```text
Discover a source (database, publisher site, catalog, or a PDF on disk)
→ capture it: browser button, identifier lookup, file import, or manual entry
→ the product creates a typed record and fills the metadata (automatically where possible)
→ attach the PDF / supplementary files if available
→ file it into collections, tag it
→ resolve duplicates and repair incomplete metadata
```

Automatic capture is the documented primary path; manual entry is consistently positioned as the last resort for sources that cannot be found online.

### Cite while writing

```text
Open the manuscript in the word processor
→ place the cursor and invoke the citation control
→ search the library (author / title / year) and pick the record(s)
→ add cite-specific details: page locators, prefix/suffix text,
  omit-author for narrative citations, multiple records in one citation
→ insert: the citation appears, formatted to the document's style
→ repeat as the text grows
→ insert the bibliography: generated from the cited records,
  kept up to date automatically as citations come and go
```

### Restyle and finalize

```text
Change the document's citation style → every citation and the bibliography re-format
→ refresh pulls metadata corrections made in the library since insertion
→ at submission, a final "unlink" step (where offered) converts citations
  and the bibliography to plain text — documented as irreversible,
  so it belongs in a final copy only
```

### Collaborate (optional)

A shared library or shared document lets co-authors insert citations from the same pool; permissions govern who may edit the library; some products log activity for large team libraries.

## Interfaces

The surfaces below are described conceptually; exact layouts and names vary by product.

### Library pane

The home surface: a navigation tree of collections/folders, an item list, and a record-detail pane showing the metadata fields, attachments, tags, and notes.

- primary actions: add or capture a record, edit metadata, attach files, organize, search

### Capture surface

A browser-extension button on publisher, database, and catalog pages.

- typical information: detected source metadata, PDF availability
- primary actions: save the record (often with the PDF) into a chosen collection

### Citation dialog

The loop's working surface, inside the word processor: search-as-you-type over the library, multi-record citations, and per-citation options (locators, prefix/suffix, omit-author).

### Document preferences / style picker

Sets the document's citation style, language, and (for note-based styles) footnote vs endnote placement.

### Bibliography control

Inserts and updates the bibliography; allows deliberately including uncited records.

### Search and duplicate resolution

Quick, advanced, and saved search over the library; a merge surface for duplicate records.

### Sharing administration

Create shared libraries or group spaces, set member permissions (in products that support collaboration).

## Important Rules / Behaviors

- **Citations in the document are live links to library records.** The manuscript stores references to records, not formatted text: a refresh updates citations when library metadata changes, and deleting a record can orphan the citations that pointed to it — a failure mode some products document explicitly.
- **Manual edits to citations or the bibliography are overwritten** by the next refresh. The sanctioned path for final, hand-tuned changes is to unlink citations into plain text in a final copy of the document.
- **Style is a document-level setting.** Switching styles re-formats every citation and the bibliography at once; the records themselves stay style-neutral.
- **Item type determines the field set.** A book record carries publisher and place; an article carries journal, volume, issue, and pages. Choosing the wrong type produces wrong citations.
- **Metadata quality is the user's responsibility.** Automatic retrieval is imperfect, so products provide repair loops — update from registries, fix incomplete data, merge duplicates — because a wrong record silently produces a wrong citation.
- **The bibliography follows the citations.** By default it contains exactly the cited records; uncited records can be included deliberately.

## Variants

- **Desktop-first commercial** — a local database with optional cloud sync, sold per license or site license; the longest-lived form of the Type.
- **Open-source local + optional sync** — a free client with paid storage; community-maintained style catalogs and capture translators.
- **Web-native, office-ecosystem-coupled** — a browser-first library with files in a cloud drive and citation inside an online document suite.
- **Publisher-suite freemium** — a free tier tied to a publisher's wider ecosystem of research services.
- **Project-based knowledge-organization emphasis** — references combined with structured quotations, outline categories, and task planning inside one project; a regional-strength variant.
- **LaTeX/BibTeX text workflow** — the library exports to a bibliographic database file; citations are written as keys and formatted by the typesetting chain rather than a plugin.
- **Individual vs institutional deployment** — personal libraries vs site-licensed institutional access, with on-premise server options for organizations that require it.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Academic Paper Reader | Fused by market packaging — modern reference managers embed PDF readers — but the centers of gravity differ: the reader centers the reading-and-annotation surface; the reference manager centers the citation database and formatted-citation output. Remove the reading surface and a full reference manager remains (historically the norm); remove the cite-and-format loop and a paper reader remains. |
| Academic Search Engine | Discovery and answering over a corpus vs holding and citing from one's own library; the handoff between them is export/import or in-product database search. |
| PDF / Document Reader | A rendering surface, which a reference manager may embed or delegate to. The boundary is the surrounding record/library/citation model, not the renderer. |
| Bookmark Manager | Saves pages by URL without typed bibliographic identity and without citation output. |
| Note-taking / Personal Knowledge Management | Notes about sources vs records of sources; a knowledge layer can straddle (quotations linked to references), but here it stays anchored on reference records. |
| Integrated Library System | The institution's holdings catalog — acquisitions, circulation, cataloging for a patron population — vs a researcher's personal working library feeding their own writing. |
| Professional Typesetting / LaTeX tooling | Consumes bibliographic data (e.g., BibTeX files) but does not manage the library or own the citation-style machinery. |

## Representative Products

- Zotero (open-source, nonprofit)
- EndNote (Clarivate)
- Mendeley (Elsevier)
- Paperpile
- Citavi (Lumivero)

The definition was checked against older and differently positioned realizations — the 1980s–2000s desktop bibliography-tool generation, the LaTeX/BibTeX workflow, and the analog card-file practice — to avoid over-fitting to the modern PDF-and-cloud implementation.

## Sources

Research date: **2026-09-09**

- Zotero — Quick Start Guide: https://www.zotero.org/support/quick_start_guide
- Zotero — Using the Zotero Word Plugin: https://www.zotero.org/support/word_processor_plugin_usage
- EndNote — product page and product details: https://endnote.com/ , https://endnote.com/product-details/
- Paperpile — Features overview and Google Docs citations: https://paperpile.com/features/ , https://paperpile.com/features/google-docs-citations-bibliography/
- Citavi (Lumivero) — product page including FAQ: https://www.citavi.com/en
- Mendeley — https://www.mendeley.com/guides/mendeley-reference-manager/ (navigation/positioning only)

> Sourcing limitation: Mendeley's guide body is JS-rendered and could not be fetched (consistent with a prior research pass's three failed attempts on the same site), so Mendeley is described at positioning level only. EndNote's deep help-guide pages were not reachable at workflow level; EndNote-based claims are feature-level. Vendor-claimed figures (style-catalog sizes, sharing limits) are reported as claims, not verified facts, and no precise operational limits are asserted anywhere in this document.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical / market-sample check are recorded in the paired Research Notes.
