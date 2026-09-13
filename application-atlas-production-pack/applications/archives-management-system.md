# Archives Management System

## Overview

An **Archives Management System** is the archival institution's system of record for describing and providing access to archival holdings — unique, unpublished materials of enduring value such as institutional records, personal papers, manuscripts, photographs, and audiovisual items.

Its defining core is small:

```text
Multi-level archival description (unit of record)
└── anchored to records creators (authority records)
    └── rendered as finding aids
        └── discovery and request of holdings
```

The system exists to solve a specific problem: archival materials are valuable less as individual objects than as bodies of material whose meaning depends on context — who created them, how they were organized, and how the parts relate. The system captures that context as structured description, and turns it into the finding aid, the instrument through which researchers discover and request materials.

Everything else commonly associated with modern products — accession modules, digital object attachments, storage and barcode tracking, standards-based export, public search websites — is standard furniture of mature products, not what makes the system an archives management system. A paper-era archives office with an accession register, typed finding aids, and a reading-room card catalog satisfies the same core.

## Users & Context

Primary users are the archives' own staff:

- **Processing archivists / cataloguers** — arrange materials and write the descriptions at every level of the hierarchy; the heaviest daily users of the staff interface.
- **Accessioning staff** — document the receipt and transfer of new materials, record donors and rights, and prepare accessions to become descriptions.
- **Archives administrators** — configure templates, controlled vocabularies, user accounts and permissions, publication defaults, and settings.

Secondary users:

- **Researchers and the public** — search and browse published descriptions, navigate hierarchies, download finding aids, and request access to materials; read-only.
- **Reference / reading-room staff** — use the descriptions to retrieve materials and manage researcher requests.

Typical institutions: university and college archives, national/state/provincial archives, municipal archives, historical societies, corporate and religious archives, special collections within libraries, and multi-institution union catalogs. The work is cataloguing work: long, careful, standards-driven data entry over months and years, punctuated by intake events (accessions) and public service (researcher requests).

## Core Model

### The Defining Core

**1. The multi-level archival description.** The unit of record is not the individual document but the *description* — a persistent, identified body of information about an archival unit. Archival units are aggregations: a whole body of materials sharing a common creator (a fonds or collection), its subdivisions (series, sub-series), and down through files to items. Description is hierarchical and progressive: describe the whole first, then its components, then components of components — not always reaching the individual item. The description emphasizes intellectual structure and content (creator, dates, scope, arrangement, conditions of access) rather than physical characteristics. Each description carries an identifier/reference code and a level of description.

**2. Provenance anchoring.** Every description is bound to the people and bodies that created or accumulated the materials. Creators — persons, families, corporate bodies — are held as **authority records**: identified, controlled descriptions of actors, with variant name forms, that link to the descriptions of the materials they created. The same authority record can link to many descriptions, and a description can link to many creators. The description hierarchy itself expresses arrangement by provenance: where a series sits inside a fonds, where a file sits inside a series. Custodial history (how materials reached the archives) is recorded on the description.

**3. Finding-aid production.** Descriptions are rendered into **finding aids** — the navigable representations of holdings. A finding aid may be the on-screen hierarchical view (the description tree a researcher browses), a generated document (a printable/downloadable inventory with cover page, table of contents, and container list), or exported description data published elsewhere. The finding aid is the bridge between the archives' internal intellectual control and the researcher's ability to discover and request materials.

### Standard Capabilities of Mature Products

These are widespread across the researched sample and expected in practice, but they are not what defines the Type:

- **Accession records** — the intake instrument. An accession documents the receipt of a body of material as a unit: provenance, contents, the legal and physical transfer, donor or transferring body, and rights or restrictions. Accessions carry events (typed, dated, attributed actions such as physical transfer or deed of gift signed) that form an audit trail. An accession can be converted into an archival description, with title, creator, custodial history, scope, and condition inherited so data is not re-entered. **Accruals** (additional material arriving for an existing accession) and **deaccessions** (documented removal from holdings) extend the accession lifecycle.
- **Digital object attachments** — descriptions can carry digital objects: scanned or born-digital files linked to the appropriate level of the hierarchy, with their own metadata and access states. Mature products are careful here: the system manages *metadata about* digital content and links to it; deep digital-asset management (bulk ingestion, derivatives, preservation processing) is neighboring territory.
- **Physical storage and location management** — shelving locations, boxes and containers, location records, container reporting, and movement tracking. This is container-level control ("which box on which shelf"), not per-object custody or circulation.
- **Controlled vocabularies and access points** — subject, place, and genre terms drawn from maintained taxonomies or external thesauri, attached to descriptions as access points; authority records play the same role for names.
- **Standards-based templates and exchange** — description templates aligned to archival description standards (international and national variants), and import/export in archival exchange formats (notably EAD for descriptions and EAC-CPF for authority records, alongside generic XML/CSV routes and harvesting interfaces).
- **Publication status** — descriptions live as drafts until deliberately published; publication is what makes a description visible to unauthenticated public users. Publication status can cascade down the hierarchy in some products, and publishing is commonly a distinct permission from editing.
- **Staff/public interface split** — a staff workbench for all record types and administration; a public interface (built in, or delivered through a companion product or export) for search, browse, and retrieval.
- **Search and navigation** — keyword and advanced search (commonly with date-range filters over controlled dates), browsing by collection/creator/subject, and hierarchical tree navigation of any description's position.
- **Reports** — file and item lists, container/location reports, cataloguing-progress and digitization statistics.
- **Rights records** — access restrictions (copyright, license, statute, policy) attached to accessions or descriptions, commonly inherited by lower levels.
- **Identifier machinery** — reference codes for descriptions and accessions (some products auto-generate numbers from configurable patterns), and alternative identifiers (legacy numbers, transfer IDs, barcodes).

### One Structure, Many Implementations

The core model is conceptual. Implementations differ:

```text
Concept:   Multi-level description
Realized as:  fonds → series → file → item trees (international practice),
              collection/series-centered structures (US, Australian series-system practice),
              configurable levels of description

Concept:   Records creators as authority records
Realized as:  agent records (persons, families, corporate bodies, sometimes software),
              ISAAR-style authority files linked through dated events,
              names linked to external thesauri / authority databases

Concept:   Finding aid
Realized as:  on-screen description tree, generated PDF/RTF finding-aid documents,
              uploaded finding-aid files, EAD export published on other platforms,
              companion public-access websites
```

## How It Works

### Intake: accession the materials

```text
Material arrives (transfer or donation)
→ create an accession record
→ record provenance, contents, transfer details
→ add donor, rights/restrictions, and dated events (audit trail)
→ assign a unique accession number
→ optionally link to physical storage containers
```

The accession establishes basic intellectual and physical control at the moment of receipt. It is an administrative record — not aimed at the public.

### Process: arrange and describe

```text
Open the accession (or start a description directly for legacy/backlog work)
→ spawn or create the top-level description
→ arrange the materials; build the hierarchy
→ add child descriptions level by level (series → file → item)
→ enrich each level: creator links, dates, scope and content,
   conditions of access, language, physical description
→ attach controlled-vocabulary access points
→ attach digital objects where they exist
→ link storage locations / containers
```

Some products let cataloguers sketch child descriptions as quick stubs while the skeleton is built and fill them in later, and can recalculate a parent's date range from the broadest dates among its descendants. The description remains editable indefinitely; accruals update the picture as more material arrives.

### Publish: make holdings discoverable

```text
Review the description
→ publish it (cascading to descendants if desired)
→ description becomes visible in public search and browse
→ generate or upload the finding aid for the hierarchy
→ researchers discover, navigate the tree, and request materials
```

Publication is the gate between internal work and public visibility. Draft descriptions are invisible to the public; publishing is a distinct permission so that editors can work without accidentally exposing unfinished description.

### Serve: reference and retrieval

```text
Researcher searches or browses published descriptions
→ navigates the hierarchy to the relevant series/file
→ consults the finding aid (on screen or downloaded)
→ requests access (reading room or reproduction)
→ staff use storage/location data to retrieve the materials
```

### The recurring loop

Accession → arrange → describe → publish → serve → (accrual → describe again). The system of record grows monotonically: descriptions are revised, never silently discarded; removal from holdings is itself documented (deaccession).

## Interfaces

### Staff: description edit page

The primary staff surface. A standards-aligned template organized into information areas (identity, context, content and structure, conditions of access and use, allied materials, notes). Typical information: title, identifier, level of description, dates (display date plus controlled start/end), creator links, scope and content, arrangement, custodial history, access restrictions. Primary actions: create/edit/save, add child descriptions, link authority records and terms, attach digital objects, link storage, duplicate, move within the hierarchy.

### Staff: accession record

The intake surface. Typical information: accession number, title, dates, transferring body/donor, extent, contents, rights, events. Primary actions: create accession, add donor, add events, add rights, add accrual, create description from accession, link storage containers, record deaccession.

### Staff: authority record

The creator-control surface. Typical information: authorized form of name, type of entity (person/family/corporate body), variant names, dates, biographical/administrative history. Primary actions: create/edit, link to descriptions as creator or subject, record relationships between agents.

### Staff: administration

User accounts and groups with granular permissions (edit, publish, administer), controlled vocabularies/taxonomies, description templates and defaults, publication defaults, visible-element toggles, import/export jobs, settings.

### Public: search and browse

The researcher's entry surface. Keyword search plus advanced filters (creator, subject, place, date range, level, availability of digital content); browse by collection, creator, or subject. Primary actions: search, refine, open a description.

### Public: description view with hierarchy tree

The finding-aid surface. The description's full content, with a tree showing its position in the hierarchy (fonds → series → file → item) for navigation up and down; links to creators, subjects, digital objects, and the downloadable finding aid where one exists. Primary actions: navigate the tree, view linked records, download the finding aid, request access where the institution offers it.

## Important Rules / Behaviors

- **Description is hierarchical by provenance.** A child description belongs inside its parent; the tree is the arrangement. Moving a description re-positions it and its descendants.
- **Publication is deliberate and permission-gated.** Descriptions remain in draft until deliberately published; only published descriptions are publicly visible. Publishing is commonly a distinct permission from editing — in products that separate the two powers, an edit by a user who cannot publish may send the record back to draft until someone with publish rights releases it. Publishing can cascade to all descendants.
- **The finding aid is a rendered artifact, not a live view.** Where the system generates finding-aid documents, they are snapshots: typically one document attaches per descriptive hierarchy, and it is not automatically regenerated when descriptions change — staff re-generate or re-upload after edits.
- **Accessions are administrative; descriptions are public-facing.** Accession records (with donors, events, internal notes) are staff-only; the public sees descriptions. The link between them is visible to staff as the provenance of the description.
- **Rights and restrictions commonly inherit downward.** A restriction recorded at the top level of a hierarchy applies to the material described beneath it unless overridden — several products implement this inheritance explicitly, mirroring how archival access control actually works.
- **Removal is documented, not silent.** Materials leave the holdings through deaccession records that preserve the audit trail — the archives' own records are part of its accountability chain.
- **Controlled dates vs display dates.** Descriptions carry both a free-text display date (preserving archival conventions like "circa" and uncertainty) and controlled machine-readable dates used for range search, sorting, and parent-date calculation.
- **No circulation.** Materials are unique and non-circulating; the system tracks where materials are stored, not who has borrowed them. Retrieval happens through reference/reading-room workflows, not loans.

## Variants

- **Standards flavor** — international ICA-standard practice, US practice, Canadian practice, and series-system practice all implement the same core with different templates, vocabularies, and hierarchy conventions; products typically support or can be adapted to several.
- **Public-access posture** — built-in public web interface; optional public interface; companion publishing product; add-on public site; or export-only (descriptions published on other platforms).
- **Single repository vs union catalog** — one institution's system, or a multi-repository deployment accepting descriptions from many contributing institutions.
- **Archives-dedicated vs combined collections suite** — dedicated archives products, versus broader collections-management products in which archives is one catalog beside objects, photographs, and library materials (common in small museums and historical societies).
- **Scale and deployment** — solo-archivist small shops on desktop or hosted instances; large archives with many concurrent cataloguers; self-hosted open source vs commercially hosted.
- **Reference machinery depth** — from simple public discovery to managed reading-room request workflows.
- **Adjacent extensions** — condition assessment and conservation documentation, digitization statistics, retention-schedule machinery (appearing where the product also serves records-management duties), multilingual content and interface.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Institutional Repository | holds the institution's **own scholarly output** through deposit, with an open-access delivery posture; the AMS describes **archival materials** the institution has transferred or acquired, delivered through finding aids |
| Digital Library Platform | curates **digital items** (metadata bound to content files) for delivery to an audience; the AMS's unit is the **description of holdings**, often physical, with digital objects as optional attachments — one sampled product states plainly that it is not a digital asset management system |
| Museum Collections Management | organized around **object-level custody accountability** — each object's location, loans, exhibitions, condition; the AMS works at **aggregation level**, describing bodies of material by provenance, with container-level (not per-object) location tracking |
| Enterprise / Government Records Management | governs **active and semi-active business records** under retention and disposition schedules; the AMS manages **permanent holdings of enduring value** — the records program's "transfer to archives" disposition is the AMS's intake |
| Integrated Library System | catalogs **published** materials as item-level bibliographic records and **circulates** them; the AMS describes **unique, unpublished** materials as aggregations, with no circulation |
| Library Discovery Platform | a **search layer over** a library's resource universe (catalog, indexes, repositories); the AMS is the archives' **own system of record**, whose public face may feed such a layer |
| Cultural Heritage Asset Management | registers **place-based heritage resources** (monuments, buildings, sites) with spatial anchoring; the AMS describes **held archival materials** |

The closest boundary is with the Institutional Repository, because both live in libraries and archives and both produce public description. The structural test: whose materials are they, and what is the access instrument? Self-deposited scholarly works delivered as open access → repository; transferred/acquired records of enduring value delivered through finding aids → archives management system.

## Representative Products

- ArchivesSpace — open-source, community-governed; dominant in US academic and special collections
- AtoM (Access to Memory) — open-source, ICA-standards-native, multilingual, multi-repository capable
- Axiell CALM — commercial, UK/European heritage sector, with a companion public-access product
- PastPerfect — commercial, small institutions; archives as one catalog within a broader collections tool

The core model was checked against the paper-era archives office (accession register, typed finding aids, card catalog) and against regional standards variants to avoid defining the Type by any one era, region, or product pattern.

## Sources

Research date: **2026-09-10**

- ArchivesSpace — https://archivesspace.org/ , https://archivesspace.org/features , https://archivesspace.org/application/specifications , https://archivesspace.org/resources/user-resources/getting-started , https://archivesspace.atlassian.net/wiki/spaces/ADC/overview
- AtoM — https://www.accesstomemory.org/en/docs/2.10/ (user manual: overview/entity types, archival descriptions, accessions, finding-aid generation)
- Axiell — https://www.axiell.com/uk/solutions/product/calm/ , https://www.axiell.com/solutions/product/axiell-collections/axiell-collections-packages/
- PastPerfect — https://museumsoftware.com/ , https://museumsoftware.com/pp5.html , https://museumsoftware.com/webedition.html

> Sourcing limitation: detailed per-field user documentation for the commercial products sits behind support portals; claims for those products rest on official product pages, and assertion strength was calibrated accordingly. Precise numeric limits and product-specific defaults are intentionally not stated in this document; they remain in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/regional check are recorded in the paired Research Notes.
