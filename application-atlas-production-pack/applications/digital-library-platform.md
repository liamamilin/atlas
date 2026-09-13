# Digital Library Platform

## Overview

A **Digital Library Platform** is institution-operated software for building and operating a curated collection of digital items: it stores identified digital objects (descriptive metadata bound to content files), organizes them into named collections, gives staff the machinery to add, describe, review, and maintain those objects over time, and makes the collection discoverable and accessible to an audience through search, browse, and content delivery.

It answers a specific institutional problem: a library, archive, museum, or university holds digitized or born-digital material — manuscripts, photographs, maps, audio, video, theses, reports, datasets — that must be described consistently, grouped meaningfully, kept under curatorial control, and put in front of researchers, students, or the public. Generic file storage cannot describe or organize; a website cannot manage items at scale; a library system built around physical circulation does not host digital content. The digital library platform is the system of record for the institution's digital collections and their public delivery.

The defining core is deliberately small:

```text
Digital item (metadata + content files)
└── Collection-level organization
    └── Staff curation machinery (add / describe / review / maintain)
        └── Discovery (search / browse)
            └── Delivery to an audience (view / download)
```

Everything else commonly associated with these products — OCR and full-text search, IIIF viewers, OAI-PMH harvesting, submission workflows, preservation programs, exhibit builders, persistent identifiers — is widespread in current products but is not what makes the product a digital library platform. Older, regional, and offline-delivery systems (collections distributed on removable media, early thesis repositories) satisfy the same core without any of those specifics.

## Users & Context

**Primary operators** are the institution's collection staff:

- **digital collections librarians / archivists / curators** — create and describe items, apply controlled vocabularies, curate collections, decide what is published and how it is presented
- **collection administrators** — configure metadata fields and vocabularies, manage user accounts and rights, configure the public site, run reports
- **contributing staff or depositors** — in some deployments, scholars, students, or partner institutions submit material that staff then review and publish

**Primary end users** are the audiences the institution serves:

- **researchers and students** — search and browse the collection, view items, download files for study
- **the general public** — discover and view cultural heritage material
- **external systems** — in many deployments, library discovery layers, catalogs, and aggregators consume the collection's metadata

The work context is an institution's ongoing digitization and digital-publishing program: material arrives from scanning projects, born-digital deposits, or migrations from legacy systems; staff process it in batches; published items serve scholarship and public engagement for years.

## Core Model

### The Defining Core

**Digital item.** The unit of record. An item is an identified object that binds descriptive metadata to one or more content files (images, documents, audio, video) or media references. The metadata describes the item for discovery and interpretation; the files are what the audience ultimately sees or downloads. Items may be simple (one file) or compound (many files with an internal order — the pages of a book, the parts of a multi-part object). In some products an item can also be a pure descriptive node — a person, place, or event — linked to other items rather than holding content itself.

**Collection.** The organizing container. Items are grouped into named, curated collections that give the corpus its structure: by source archive, subject, format, provenance, or exhibition theme. Implementations differ in topology — a strict tree of departments containing collections, a flat list of collections, or many-to-many sets an item can join freely — but every product in this Type organizes items into collections, and collection pages are a primary public entry point.

**Staff curation machinery.** The platform is operated, not merely installed. Staff add items (one at a time or in batches), enter and edit metadata against configured fields, apply controlled vocabularies, generate access copies (thumbnails, display images), review contributions before publication, correct records, and maintain the collection as material and standards change. This machinery is what distinguishes a managed library from a static file drop.

**Discovery.** The collection is searchable and browsable: keyword search over metadata (commonly over extracted document text as well), browse indexes such as title / date / creator / subject, and filters or facets over descriptive fields. Discovery operates across the whole collection and within single collections.

**Delivery.** The audience-facing half. Each item has a public page presenting its metadata and its content; users view images or documents in a viewer, play media, and download files where rights allow. Delivery is the point of the exercise: without it the system is a back-office store; without discovery it is an unfindable archive.

### Capabilities Mature Products Commonly Add

These are standard capabilities across the researched sample. They make the platform practical; they do not define the Type.

- **Metadata workbenches** — per-item-type field templates, controlled vocabularies (sometimes shared across collections), batch editing, per-field configuration of search behavior
- **Batch ingest** — importing many items at once from folders or spreadsheets, with automatic generation of display images and thumbnails from high-resolution originals
- **Review and approval** — contributed or batch-loaded items held in a pending state until a staff member approves and indexes them for publication
- **Full-text search and OCR** — extracting searchable text from scanned documents so content inside files is findable, not just the metadata
- **Access restriction** — public versus restricted items, institution-network or authenticated access, item-level rights and license statements
- **Persistent identifiers** — stable, citable identifiers for items (and often collections) that survive reorganization
- **Usage statistics** — views and downloads per item and collection
- **Metadata exposure** — publishing the collection's metadata for harvesting by catalogs, aggregators, and discovery layers; rich-media delivery interfaces for image viewers
- **Structural metadata** — ordering and grouping of an item's constituent files (page order, part hierarchy)

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:   Digital item
Realized as:   metadata record + attached files; compound object with
               internal page structure; vocabulary-driven resource with
               linked media; archival information entity with representations

Concept:   Collection
Realized as:   department → collection tree; flat collection list;
               many-to-many item sets; curated publication sites over a
               shared item pool

Concept:   Delivery
Realized as:   public web portal with image viewers and downloads;
               integration into the library catalog or discovery layer;
               offline distribution on removable media (historical form)
```

A reader who has only seen one hosted collection website should still be able to recognize a self-hosted repository or an offline-distributed collection as the same Type from this model.

## How It Works

### Building a collection

```text
Plan the collection
→ configure its metadata fields and controlled vocabularies
→ acquire or digitize material
→ add items (individually, or in batches from folders/spreadsheets)
→ enter or import descriptive metadata
→ generate access copies (thumbnails, display images, searchable text)
→ review and approve
→ publish to the public site
```

In batch-oriented products, staff work in staging projects: items and their metadata are prepared, checked, and uploaded together, then held in a pending queue until an administrator approves them and rebuilds the search index. In submission-oriented deployments, external depositors submit through a form, and the item passes through configurable review steps — with rejection returning the item to the submitter for correction — before it is installed in the archive and indexed.

### The recurring curation loop

```text
Monitor the collection
→ correct or enrich metadata
→ move, group, or reclassify items
→ restrict or release access where rights require
→ withdraw items that must no longer be shown (commonly leaving a
  visible placeholder rather than silently breaking citations)
```

Items are treated as durable records: identifiers stay stable, removal is deliberate and visible, and edits accumulate as the collection's history.

### The audience loop

```text
Arrive at the collection site (or a catalog/discovery layer)
→ search or browse (by keyword, facet, collection, index)
→ open an item page
→ view the content (image viewer, document reader, media player)
→ read the metadata (creator, date, provenance, rights)
→ download files where permitted
```

### Core vs common vs optional

**Defining core** — without these, not a digital library platform:

- digital item (metadata + content)
- collection-level organization
- staff curation machinery
- discovery (search / browse)
- delivery to an audience

**Standard capabilities** — present in most mature products:

- metadata templates and controlled vocabularies
- batch ingest with derivative generation
- review/approval before publication
- full-text search / OCR
- access restriction and rights statements
- persistent identifiers
- usage statistics
- metadata harvesting exposure and rich-media interfaces
- compound items with internal ordering

**Variant / optional** — depends on segment, scale, and philosophy:

- preservation programs (fixity checking, format registries, retention policies)
- exhibit and storytelling layers (curated sites, timelines)
- crowdsourced transcription and public contribution
- researcher profiles, ORCID integration, request-a-copy
- offline distribution media
- linked-data modeling of items as interconnected nodes

## Interfaces

### Staff administration

The operator's console. Purpose: configure and run the collection program.

- typical information: collections and their settings, metadata field definitions, controlled vocabularies, user accounts and rights, pending items, reports
- primary actions: create/configure collections, define fields and vocabularies, manage users, approve pending items, run imports, view usage reports

### Item and metadata workbench

Where description happens. Purpose: create and maintain item records.

- typical information: item list with thumbnails and status, item detail with metadata fields and attached files
- primary actions: add/edit/delete items, enter metadata, attach or replace files, reorder pages, batch-edit, move items between collections

### Ingest / staging surface

For batch work. Purpose: prepare many items safely before publication.

- typical information: staging projects, item batches, upload status, error and warning summaries
- primary actions: import from folders or spreadsheets, apply templates, upload for approval

### Public collection portal

The audience surface. Purpose: make the collection discoverable and usable.

- typical information: collection listings with descriptions and representative images, search and filter results, item pages with metadata and content
- primary actions: search, browse by collection/index/facet, view content, download, cite or share

### Item page

The workhorse of public delivery. Purpose: present one item completely.

- typical information: title and descriptive metadata, rendered content (image viewer, document, media player), download options, rights statement, persistent identifier, related items
- primary actions: navigate pages/parts, zoom or read, download, request a copy where access is restricted

## Important Rules / Behaviors

### Publication is a controlled transition

Items typically exist in non-public states (staging, pending, private) until explicitly approved or made public. Approval commonly triggers indexing — an item is findable only after the collection's index is updated. This gate is the institution's quality and rights control.

### Access is governed per item

A collection can mix open and restricted material. Restrictions are enforced at delivery: items may be hidden from anonymous users, limited to on-campus networks or authenticated groups, or downloadable only on request. Whether an item's metadata stays visible while its content is restricted varies by product — some keep records discoverable with content gated, others hide restricted items entirely.

### Items are durable, removal is deliberate

Because items acquire persistent identifiers and citations, platforms distinguish between withdrawing an item (hidden from view, replaced by a tombstone that explains its absence) and fully deleting it. Silent disappearance is avoided.

### Metadata quality is structural, not cosmetic

Controlled vocabularies, field types, and required fields exist so the collection stays coherent as many staff contribute over time. Search facets and browse indexes are only as good as the vocabulary discipline behind them.

### The collection outlives any single rendering

Files may be re-encoded or supplemented with derivatives over time, but the item — its identity and metadata — is the preserved unit. Delivery mechanisms (viewers, formats) are expected to change; the record is not.

## Variants

- **Repository / submission-centered** — the platform's center of gravity is accepting deposits from scholars and students, with submission workflows, embargoes, and open-access policy machinery (institutional repositories of papers and theses)
- **Hosted collection management** — turnkey hosted service where the institution configures collections and the vendor runs everything; common in small and mid-sized libraries and archives
- **Publication / exhibition-centered** — the item pool is shared infrastructure while the visible products are independently curated sites and exhibits; strong in museums and digital-humanities teaching
- **Preservation-centered** — long-term stewardship is the discipline: validated ingest, fixity checking, format registries, retention rules, preservation reporting; typical of national libraries and large heritage institutions
- **Cultural-heritage / GLAM flavor** vs **academic flavor** — museum and archive deployments emphasize visual presentation, exhibits, and community engagement; academic deployments emphasize scholarly metadata, citation, and integration with the library ecosystem
- **Deployment posture** — self-hosted open source, vendor-hosted SaaS, or enterprise hosted/on-premise installations
- **Delivery medium** — web portal (dominant today) versus offline distribution on removable media, a form still relevant where connectivity is limited

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Integrated Library System / ILS | adjacent, ecosystem partner | ILS runs the physical collection's operations — cataloging, circulation, acquisitions, patrons. The digital library platform hosts and delivers digital content. They integrate (catalog records link to digital items) but neither replaces the other. |
| Library Discovery Platform | adjacent, complementary | A discovery layer searches across many external sources (catalog, subscriptions, digital collections). The digital library platform is the host of the collection such layers index. Remove the hosted item store and search external indexes instead → discovery platform. |
| Institutional Repository | subtype / variant | An institutional repository is this Type applied to an institution's scholarly output, with submission workflows and open-access machinery at the center. The same products often serve both roles; see the note in Sources. |
| Archives Management System | adjacent | An archives system manages archival description and finding aids — the intellectual control of archives (often including material not yet digitized). The digital library platform publishes digitized content to audiences. Remove public delivery and center finding-aid description → archives system. |
| E-book Library Application | different actor | A consumer's personal reading library: the user's own books, reading experience first. Remove institutional curation and multi-user collection management → personal e-book library. |
| Digital Asset Management (DAM) | adjacent | Enterprise DAM centers on an organization's brand and marketing assets and their rights. A digital library platform centers on curated collections described for scholarship and public access, with library metadata and harvesting semantics DAMs lack. |
| Content Management System / CMS | adjacent | A CMS publishes web pages. It has no item-level collection semantics — no descriptive metadata models, controlled vocabularies, content viewers, or metadata harvesting. A digital library platform can sit behind or beside a CMS, but is not one. |

## Representative Products

- **DSpace** — open-source repository platform; the dominant system for institutional scholarly collections, widely used for digital collections of all kinds
- **CONTENTdm (OCLC)** — hosted digital collection management for libraries, archives, and museums
- **Omeka S (Omeka / Digital Scholar)** — open-source web publication system for galleries, libraries, archives, and museums; exhibit-oriented
- **AM Quartex (Adam Matthew Digital)** — fully hosted digital collections platform combining asset management and site creation
- **Rosetta (Ex Libris)** — enterprise preservation-and-delivery system for digital heritage collections

The defining core was checked against an older, regional, offline-capable system (Greenstone, developed with UNESCO for institutions including those in developing regions) to avoid defining the Type by today's hosted, web-only, standards-rich implementations.

## Sources

Research date: **2026-09-07**

- DSpace — DSpace 7.x Documentation, Functional Overview (LYRASIS wiki): https://wiki.lyrasis.org/display/DSDOC7x/Functional+Overview
- CONTENTdm — CONTENTdm Overview and Collection building overview (OCLC Support): https://help.oclc.org/Metadata_Services/CONTENTdm
- Omeka S — User Manual: Items, Item Sets (omeka.org): https://omeka.org/s/docs/user-manual/
- AM Quartex — product pages (Adam Matthew Digital): https://www.amdigital.co.uk/products/quartex
- Rosetta — Introducing the Rosetta System (Ex Libris Knowledge Center): https://knowledge.exlibrisgroup.com/Rosetta/Product_Documentation/Rosetta_Overview_Guide/001_Introducing_the_Rosetta_System
- Greenstone — About Greenstone: https://www.greenstone.org/

> Sourcing limitations: operational help documentation for AM Quartex was not reachable from the research environment; claims about that product are limited to its official product-page positioning. Deep Rosetta configuration guides were not individually fetched; its model is described at the level its overview documentation supports. Precise operational limits, default settings, and numeric caps observed during research were intentionally not stated in this document.

> Taxonomy note: the market does not cleanly separate "digital library platform" from "institutional repository" — the same leading products serve both roles. This relationship is recorded for joint review in the project status notes.

Detailed evidence, product-by-product observations, cross-product comparison, and the historical sample check are recorded in the paired Research Notes.
