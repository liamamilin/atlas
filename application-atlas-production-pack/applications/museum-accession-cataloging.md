# Museum Accession / Cataloging

## Overview

A **Museum Accession / Cataloging** application is the record-creating system of museum collection stewardship. It handles two connected jobs:

- **Accessioning** — the formal, recorded intake of objects into a museum's permanent collection: who the objects came from, how they were acquired (gift, purchase, bequest, transfer), the evidence that title passed to the museum, and the commitment to care for them long term. Each accessioned object receives a unique number that ties the physical object, its record, and its acquisition paperwork together.
- **Cataloging** — creating and continually enriching the authoritative record for each object: what it is, who made it and when, what it is made of, how large it is, what it looked like, where it came from, and what the museum knows about it over time.

The defining structure is small:

```text
Acquisition of objects
  → Accession (recorded intake: source, method, title evidence, permanent-collection commitment)
    → unique numbers assigned and marked on objects
      → Object catalogue record (one authoritative record per object or object group)
        → Enrichment over time (description, terminology, media, provenance, links)
```

Everything else commonly bundled with this software — configurable fields, image libraries, thesaurus vocabularies, reports, public web publishing, locations and loans — either supports these two jobs or consumes their output. Downstream custody work (movement, loans, exhibitions, conservation) operates *on* the records this system creates; the public presentation of the collection is a separate publishing surface.

A second boundary matters inside the workflow itself: not everything a museum acquires is accessioned. Objects kept as teaching props, handling specimens, or property to be disposed of are tracked as acquisitions without accessioning, because accessioning carries an ethical commitment to preserve the object for the long term.

## Users & Context

Primary users are the museum professionals who own the documentation:

- **Registrar** — the traditional owner of the accessioning workflow: records acquisitions, creates accession and object records, generates acquisition paperwork (deeds of gift, receipts), maintains numbering discipline, and manages the formal exit of objects (deaccession).
- **Collections manager / cataloger** — creates and enriches object records: identification, classification terms, measurements, images, provenance notes; often runs backlog cataloging projects.
- **Curator** — the content authority for what objects mean: attribution, significance, scholarship that feeds the record over time.

Secondary users include volunteers and interns (especially in small museums and historical societies, where bulk photography and data entry are common), conservators and educators who read the records, and — at the edge of the category — private collectors and family historians who keep the same kind of records for personal collections without the institutional governance.

The work environment alternates between a desk (data entry, research, paperwork) and the storage room or receiving dock (photographing, measuring, labeling objects). The work is paced in two rhythms: event-driven intake when acquisitions arrive, and slow backlog projects that may run for years.

## Core Model

### The defining core

Three structures carry the whole system. Remove any one and what remains is no longer this application.

**1. The accession — a recorded, numbered intake.** Objects enter the collection through a recorded acquisition event: the source (donor, seller, estate, originating institution), the method of acquisition (gift, purchase, bequest, transfer), the date, and evidence that ownership legally transferred — a signed deed of gift, an invoice, a transfer memo. The intake that is formally accessioned is a commitment by the institution to hold and care for the objects in perpetuity, made under its collecting policy. Each accessioned object is given a unique number, and the object is physically labeled or marked with it. This number is the connective tissue of the entire system: it links the physical object to its record and to the acquisition documents behind it.

**2. The object catalogue record.** One persistent, individually identified record per object (or per defined group of objects, such as a set). It is the authoritative documentation of what the institution holds. It starts with identification — object name, classification, maker or origin, date, materials, dimensions — and is designed to grow: provenance and ownership history, associations with people and places, credit lines naming the source, images and files, and the research accumulated about the object. The record exists regardless of where the object physically is; it is the object's permanent institutional memory.

**3. The ongoing cataloging loop.** Cataloging is explicitly open-ended. Records are enriched as knowledge grows — through research, exhibitions, new attributions, contributions from communities and previous owners — and corrected when knowledge changes. The corpus is kept searchable, changes are attributable, and the accession record itself is treated as a formal register: tamper-resistant and backed up. No museum finishes cataloging; the system is built for continuous improvement, not for a final product.

### Standard capabilities

Mature products commonly add, around that core:

- **Configurable record structure** — fields, forms, and screens adapted to the institution and to the collecting discipline (a natural-history specimen record and a painting record need different fields); record depth is a policy decision, not a fixed standard.
- **Terminology control** — authority lists and thesauri (such as the Getty Art & Architecture Thesaurus or library subject headings) so object names, classifications, and place names stay consistent across catalogers and decades.
- **Person and organization records** — donors, makers, artists, previous owners, and contacts held as their own records, linked to objects (as creator, source, or subject) and reused across the catalogue.
- **Images and files on the record** — photographs, scans, and documents attached to objects; image-first browsing of the collection.
- **Numbering scheme configuration** — support for the institution's numbering convention (commonly a year-and-lot accession number extended with a per-object sequence, and separate prefixes for loans, acquisitions, found-in-collection items, or deaccessions), with some products enforcing the scheme automatically.
- **Acquisition paperwork from records** — deeds of gift, receipts, and credit-line documents generated from the accession record rather than typed separately.
- **The exit counterpart** — deaccessioning recorded in the same system with its own formal process, so the register of what the institution holds stays truthful in both directions.
- **Search, import, and batch work** — retrieval across the whole catalogue, bulk data import for migration and backlog projects, batch editing, and consistency checks.
- **Roles and change history** — permission to create and edit records restricted to authorized roles; edits recorded so the register remains trustworthy.
- **Registers and reports** — printed-style accession registers, catalogue reports, and object lists: the digital descendants of the ledger and the card catalogue.

### One structure, many implementations

The core is conceptual, and products realize it differently:

```text
Concept:   Accession with unique numbering
Implementations:  year.lot.object numbers (common in US practice),
                  institution-specific schemes, prefixed series for
                  loans / acquisitions / deaccessions, paper registers

Concept:   Object catalogue record
Implementations:  "object records", "entries", catalogue cards (paper era)

Concept:   Terminology control
Implementations:  bundled thesauri, linked external vocabularies,
                  institution-built classifications

Concept:   The cataloging loop
Implementations:  direct data entry, photo-first mobile capture,
                  AI-assisted description, backlog batch projects
```

A reader who has only seen one implementation — say, a cloud product where each object is an "entry" with a photo — should still be able to recognize the same structure in an enterprise system configured for a national museum, or in the paper accession register and card file it replaced.

## How It Works

The canonical flow is the life of an object's documentation:

```text
Acquire under collecting policy
  → record the acquisition (source, method, title evidence)
  → accession: create the accession record; assign the accession number
  → number and mark each object in the lot
  → create the object catalogue record, linked to its accession
  → catalog: identification, classification terms, images, provenance, credit line
  → enrich over time (research, exhibitions, corrections, contributions)
  → maintain: search, correct, report; feed downstream workflows
```

**Intake and accessioning.** An acquisition arrives — a donation, a purchase, a bequest, a transfer from another institution. The registrar records the source and method, and the system holds the title evidence: the signed deed of gift, the invoice, the transfer document. If the objects are accepted into the permanent collection, an accession record is created for the lot — objects acquired at the same time from the same source — and a unique accession number is assigned. Each object in the lot receives its own number derived from the accession, and is labeled or marked with it. Acquisitions that the museum does *not* intend to accession (teaching props, property held for disposal) are tracked through a parallel, non-accessioned path so they never contaminate the formal register.

**Record creation and cataloging.** For each accessioned object, the cataloger creates the object record and fills the identification fields: name, classification, maker or origin, date, materials, dimensions. Photographs are attached. Terminology is drawn from the institution's authorities so that "vase", "amphora", or the regional equivalent is used consistently. Provenance and credit line are recorded — who gave or sold the object, and how the museum may acknowledge them. The record may begin sparse and deepen over years.

**Enrichment and maintenance.** The catalogue is a living corpus. Research adds attributions; exhibitions add display history; communities and previous owners contribute knowledge; corrections replace earlier mistakes. Catalogers run backlog projects (photographing and documenting stored collections), often with batch tools and data imports. Changes are attributable, and the register of accessioned objects is preserved against loss or tampering — it is the museum's proof of what it holds and how it came to hold it.

**Handoff to downstream work.** Once records exist, other workflows consume them: locations and movement track where objects are; loans and exhibitions borrow their content; conservation attaches condition and treatment history. This application's job ends at the authoritative record; the record is what everything else points at.

### Core vs common vs optional

- **Defining core** — recorded accession with unique numbering and title evidence; per-object catalogue record as the system of record; continuous enrichment, searchable and attributable.
- **Common mature structure** — configurable fields, thesauri, person records, media, numbering schemes, paperwork generation, deaccession process, search/import/batch, roles and change history, registers and reports.
- **Optional / variant** — multilingual data entry, AI-assisted description, public web publishing, discipline-specific extensions (archival finding aids, bibliographic modules), private-collector editions without institutional governance.

## Interfaces

Exact layouts vary by product; these are the working surfaces the category is built around.

### Object record editor

The single most-used surface.

- Purpose: create and edit one object's authoritative record.
- Typical information: identification fields (name, classification, maker, date, materials, dimensions), description and provenance text, credit line, accession number, linked images and files, links to related people, places, and objects.
- Primary actions: create record, edit fields, attach media, add authority terms, link related records, save with recorded attribution.

### Accession register / intake view

The register of acquisition events — the digital ledger.

- Purpose: record and retrieve acquisitions and their paperwork.
- Typical information: accession number, date, source, method of acquisition, objects in the lot, attached documents (deed of gift, invoice), status.
- Primary actions: create accession, assign numbers, attach title evidence, open the object records created from the lot, generate acquisition paperwork.

### Search and browse

- Purpose: find records across the whole catalogue.
- Typical information: result lists and image-centric grids, saved queries, structured filters by classification, source, date, or missing fields (useful for backlog targeting).
- Primary actions: search, refine, open records, bulk-select for batch edit or export.

### Person / organization profiles

- Purpose: hold donors, makers, artists, and contacts as reusable records.
- Typical information: biography, roles relative to objects (creator, source, previous owner), linked object lists.
- Primary actions: create profile, link to objects, trace everything connected to one person.

### Forms and reports

- Purpose: produce the paperwork and registers the workflow owes the institution.
- Typical information: deeds of gift, receipts, catalogue reports, accession registers, object lists.
- Primary actions: generate from records, print or export, adapt templates.

### Administration and configuration

- Purpose: adapt the system to institutional policy.
- Typical information: field and form definitions, numbering schemes, authority lists, user roles.
- Primary actions: configure fields, set or enforce numbering, manage vocabularies and users.

A public web-publishing surface (online collections) is commonly available as a companion; it presents records governed here but is its own application type.

## Important Rules / Behaviors

- **Accessioning is a commitment, not a filing act.** Because accessioned objects are held in trust for the long term, what gets accessioned is governed by the institution's collecting policy; acquisitions made for other uses follow a separate, non-accessioned path. Some products distinguish the two at the record level with different record types and number series.
- **Numbers are permanent connective tissue.** Each accessioned object gets a unique number, the object is marked with it, and the number links object, record, and acquisition documentation. Numbering discipline is treated as critical: some products assign numbers automatically and refuse deviations from the configured scheme.
- **The accession record is a formal register.** It must be tamper-resistant and backed up — the institution's proof of ownership and of what it holds. Mature products support this with change history (who changed what, old and new values) and permission control over record creation and editing.
- **There is no "complete" catalogue.** Records deepen indefinitely and are corrected as knowledge changes; the system is designed for continuous enrichment rather than a finished product. Record depth itself is policy-driven — there is no single ideal record.
- **Credit and provenance travel with the object.** The source of the object (and the credit line owed) is part of the record, not an external footnote.
- **Exit is as formal as entry.** Removing an object from the collection (deaccession) is its own governed process recorded in the same system — the register must stay truthful in both directions.
- **Paper and software are equivalent in kind.** The defining records — accession register, object catalogue, title evidence — predate software and can legally be kept on paper; the software's contribution is search, scale, images, linkage, and change tracking, not a new kind of record.

## Variants

- **By institution scale**: national and large museums (deeply configured enterprise systems, dedicated registrar departments), mid-size museums, small museums and historical societies (lighter cloud products where volunteers do the cataloging), and private collectors (the same record-keeping core without institutional governance or formal accession policy).
- **By deployment**: cloud subscription products; on-premises or vendor-hosted enterprise systems; self-hosted open-source platforms.
- **By collecting discipline**: art museums, history and natural-history collections, archives and library hybrids — the record structure is shared, while fields, classifications, and attached modules differ.
- **By standards regime**: institutions align record content with different national and disciplinary documentation standards; the software adapts rather than imposing one.
- **Era layering**: current products increasingly add AI-assisted description and mobile-first capture; these change the pace of cataloging, not its structure.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Museum Collections Management | containing system | the full stewardship suite; accessioning and cataloging are its record-creating core, sitting beside movement, loans, exhibitions, conservation, and rights modules |
| Archaeological Collection Management | discipline variant with an added layer | adds excavation context (site → stratum → object) as first-class documentation; strip the context layer and the accession/catalog structure remains |
| Digital Collection Portal | publication surface | presents records publicly; it owns no records and no cataloging machinery — the complement of this Type |
| Provenance Research Platform | investigation over the same records | builds evidence chains about an object's ownership history; cataloging records provenance fields but provides no research apparatus |
| Museum Object Movement / Location Management | downstream custody workflow | tracks where objects physically are; operates on the records this Type creates |
| Museum Loan Management | downstream agreement layer | the legal structure of borrowing and lending; attaches to existing object records |
| Museum Conservation / Condition Reporting | downstream care workflow | documents condition and treatment; attaches to existing object records |
| Integrated Library System | different object world | bibliographic records for works held in copies, with circulation; museum records describe unique objects under permanent custody, with accession numbers, provenance, and credit lines |
| Auction Management System | different disposition | catalogs lots as units of sale ending in a commercial close; museum accessioning ends in permanent custody, with disposal as a governed exception |
| Enterprise Asset Registry | generic inventory | tracks what an organization owns and where; lacks acquisition-event semantics, provenance, credit lines, and the permanent-custody commitment |

The densest boundary is with Museum Collections Management, because in the current market this workflow is always sold as the core of such a system rather than as a standalone product. The structural test runs both ways: strip the downstream custody and operations modules and the accession/catalog system of record still stands on its own; strip the record-creating core and the remaining modules manage records that no longer exist. This document therefore describes the record-creating workflow itself, as it exists inside every product that realizes it.

## Representative Products

- **TMS Collections** (Gallery Systems) — enterprise museum incumbent; Spectrum-compliant, with the accessioning and cataloging procedures verified alongside the full stewardship family
- **MuseumPlus** (Zetcom) — European museum incumbent; cataloging and registration of all collection objects as its core function
- **CatalogIt** — cloud-native product for small museums, historical societies, and private collectors; documented through its public help center
- **CollectiveAccess (Providence)** — open-source collections platform; its cataloging application is deliberately separate from its public-publishing tool, illustrating the record-creation boundary

These span enterprise, regional, small-institution, and open-source poles; the structure described here is common to all of them.

## Sources

Research date: **2026-09-08**

- Collections Trust — Spectrum 5.1, primary procedures: *Acquisition and accessioning* and *Cataloguing*, with scope and standard pages — https://collectionstrust.org.uk/spectrum/
- Collections Trust — Spectrum appendix, Object information groups — https://collectionstrust.org.uk/spectrum/information-requirements/object-information-groups/
- Collections Trust — software directory entry for TMS Collections and eMuseum — https://collectionstrust.org.uk/software/tms/
- Gallery Systems — Collections Management (TMS Collections) and Software for Registrars — https://www.gallerysystems.com/solutions/collections-management/
- Zetcom — MuseumPlus product page — https://www.zetcom.com/en/museumplus-en/
- CatalogIt — product page, help center (*What is an Entry?*, *Using the Museum Accession Profile*, *Creating The First Entry in Your Museum Account*, Museum Features) and the article *Acquisition v. Accession* — https://www.catalogit.app/ , https://support.catalogit.app/
- CollectiveAccess — official documentation — https://manual.collectiveaccess.org/

> Sourcing limitation: detailed help documentation for the enterprise incumbents (Gallery Systems client community, Zetcom help center) is login-gated, so their observations here rest on official product pages and the Collections Trust software directory entry at module level; no screen-level workflow details are asserted for them. The CollectiveAccess documentation wiki was unreachable, so its evidence is positioning-level only. PastPerfect and Lucidea Argus were not reachable. The claim that a specific three-part numbering pattern is widespread in US museum practice rests on vendor-authored guidance and is presented as common practice, not as a rule of the category. Precise field lists, state names, and configuration limits are intentionally kept qualitative.
