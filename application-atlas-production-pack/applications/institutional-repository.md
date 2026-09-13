# Institutional Repository

## Overview

An **Institutional Repository** is a research institution's public system of record for its own scholarly output. It holds a persistent, individually identified record for each work the institution's researchers and students produce — bibliographic metadata bound to the deposited files — captures those works through a managed intake process, and delivers them on the open web as openly accessible, citable items.

It answers a specific institutional problem: a university or research institute produces a steady stream of articles, theses, datasets, conference papers, and reports that are scattered across publisher sites, personal drives, and department servers. The institution wants a durable, openly accessible home for this output — one that satisfies open-access policies and funder mandates, showcases the institution's research, and gives each work a stable address that outlives website redesigns. A website cannot manage deposits at scale; an internal records system does not deliver content to the world; a library system built around physical circulation does not hold scholarly files. The institutional repository is the system of record for the institution's own output and its open delivery.

The defining core is deliberately small:

```text
The institution's own research output
└── Item of record (bibliographic metadata + held content files)
    └── Managed intake (deposit / ingest, commonly gated by review)
        └── Open-access public delivery (item pages, persistent citation)
```

Everything else commonly associated with these products — metadata harvesting interfaces, search-engine optimization, ORCID integration, funder-policy checks, preservation programs, usage dashboards — is widespread in current products but is not what makes the product an institutional repository. The founding generation of repository software (early 2000s) already exhibits the full defining core without any of those specifics.

## Users & Context

**Primary operators** are the institution's repository and library staff:

- **repository staff / scholarly-communications librarians** — review and approve deposits, correct and enrich metadata, mediate deposits on behalf of researchers, manage embargoes and restrictions
- **repository administrators** — configure work types and metadata fields, manage user accounts and permissions, configure the public site, run reports

**Primary contributors** are the people whose works fill the record:

- **researchers / faculty** — deposit their own outputs (or claim records harvested on their behalf), respond to review feedback, receive usage reports for their works
- **students** — deposit theses and dissertations, often through a dedicated form, sometimes with advisor involvement

**Primary end users** are outside the institution:

- **researchers worldwide** — discover and read the institution's output without a subscription
- **funders, practitioners, journalists, prospective students** — access works and evidence of the institution's research
- **external systems** — library catalogs, discovery layers, and aggregators that harvest the repository's metadata

The work context is the institution's open-access and research-management program: deposits arrive continuously from authors and automated feeds; staff keep the record accurate; published works serve readers for years and are expected to remain accessible indefinitely.

## Core Model

### The Defining Core

**The work of record.** The unit of the repository is a persistent, individually identified record for one scholarly work — a journal article, conference paper, thesis or dissertation, dataset, report, book chapter, or similar output of the institution's own research. Each record binds descriptive bibliographic metadata (title, creators, date, publication reference, subject, abstract) to the content files the institution holds for that work. The record — not the file — is the preserved unit: files may be supplemented or reformatted over time, while the record's identity and citation stay stable. Work types are configurable per institution, and the type chosen drives which metadata fields apply.

**Managed intake.** Works enter the record through the repository's deposit and ingest machinery, never by hand-editing a public page. Three intake paths coexist in mature products: authors deposit their own works through a submission form; staff create or complete deposits on a researcher's behalf; and automated feeds import records (and sometimes files) from external bibliographic sources. Intake captures metadata against the work type's fields, uploads files, records the depositor, and commonly passes a review or approval step before the work is published into the archive. The review gate's depth is an institution-level policy choice — some repositories review every item, others publish deposits directly — but the intake machinery itself is what makes the repository a managed record rather than a static showcase.

**Open-access delivery.** The repository's public face presents each work as a web page carrying its metadata and its files, where any visitor can discover, read, and download the deposited content. Open access is the default posture of the Type — the repository exists to make the institution's output publicly available — with restriction as the deliberately managed exception: embargoes with future release dates and institution-only or staff-only files; some products add a request path through which restricted files can be requested. Each published work is citable: repositories assign persistent identifiers (handles, DOIs, or equivalent stable addresses) so references survive reorganization and redesign.

### Capabilities Mature Products Commonly Add

These are standard capabilities across the researched sample. They make the repository practical; they do not define the Type.

- **Deposit licenses and agreements** — the depositor grants the institution a distribution license at submission; open-content licenses (such as Creative Commons) can be attached to works
- **Embargoes with automatic expiry** — a file restricted until a set date becomes available without staff intervention; the metadata page typically shows the future availability date
- **File security tiers** — public, institution-only, and staff-only access levels per file, with the metadata page remaining public even when the file is restricted
- **Version semantics** — describing which form of the work is deposited (submitted manuscript, accepted manuscript, published version), because publisher policy usually permits only specific versions to be self-archived
- **Metadata harvesting exposure** — publishing the repository's metadata in a standard harvesting protocol so catalogs, discovery layers, and aggregators can index it
- **Search-engine optimization** — structured metadata in item pages so search engines and Google Scholar index the works correctly
- **Full-text search and browse indexes** — search across metadata and extracted document text; browse lists organized by year, author, subject, or organizational unit
- **Batch ingest and duplicate detection** — importing many records at once and flagging likely duplicates against existing holdings
- **Persistent identifiers** — handles, DOIs, or equivalent stable addresses, assigned to works
- **Usage statistics** — views and downloads per work, reported to administrators and, in some products, to authors
- **Withdrawal with tombstone** — a removed work stays addressable with a visible notice rather than silently disappearing
- **Controlled vocabularies** — subject schemes and the institution's organizational hierarchy (schools, departments, centers) as metadata fields

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:   Work of record
Realized as:   item with metadata and files in named bundles;
               publication record with attached documents;
               research asset with attachments and history

Concept:   Managed intake
Realized as:   author submission form with workflow steps and
               gatekeeper groups; editor review queue; staff-mediated
               deposit wizard; automated harvesting from bibliographic
               databases with author-claim steps

Concept:   Organization of the corpus
Realized as:   hierarchy of communities and collections; flat archive
               browsed by metadata fields; named publication series
               and communities; organizational units

Concept:   Open-access delivery
Realized as:   public item pages optimized for search engines;
               public portal with researcher profiles; metadata
               harvesting into catalogs and discovery layers
```

A reader who has only seen one hosted repository site should still be able to recognize a self-hosted community platform, a flat browse-organized archive, or a repository embedded in a research-information suite as the same Type from this model.

## How It Works

### Capturing a work

```text
A work is identified for the record
→ (author self-deposit | staff-mediated deposit | automated feed)
→ metadata entered against the work type's fields
→ files uploaded — commonly the version publisher policy permits
→ deposit license / submission agreement accepted
→ review and approval (or return to the depositor with a reason)
→ work installed in the archive: indexed, given its persistent identifier
→ publicly discoverable and downloadable
```

The review step is where the institution exercises quality and policy control: reviewers can accept, correct metadata, or return the deposit to its author with an explanation for correction and resubmission. Once approved, the work becomes part of the archive — findable through search and browse, exposed to harvesting, and addressable by its persistent identifier.

### The recurring curation loop

```text
Monitor the record
→ correct or enrich metadata
→ flag suspected duplicates for staff resolution
→ restrict or release file access as publisher terms require
→ lift embargoes automatically at their expiry dates
→ withdraw works that must no longer be shown (leaving a visible
  tombstone rather than breaking citations)
```

Records are treated as durable: identifiers stay stable, edits accumulate in a revision history, and removal is deliberate and visible.

### The audience loop

```text
Arrive from a search engine, scholarly search service, catalog, or
discovery layer (or browse the repository directly)
→ search or browse (keyword, facet, year, author, subject, unit)
→ open the work's public page
→ read the metadata (creators, publication reference, abstract, license)
→ download the deposited file — or see an embargo notice (and, in some
  products, a request path) where access is restricted
```

### Core vs standard vs optional

**Defining core** — without these, not an institutional repository:

- the institution's own research output as the collection of record
- the work of record: persistent identified item with metadata + held files
- managed intake (deposit/ingest machinery)
- open-access public delivery with persistent citation

**Standard capabilities** — present in most mature products:

- deposit licenses and agreements
- review/approval gates with return-to-depositor loops
- embargoes with automatic expiry; file security tiers
- version semantics for deposited files
- metadata harvesting exposure; search-engine optimization
- full-text search and browse indexes
- batch ingest and duplicate detection
- persistent identifiers (handles, DOIs)
- usage statistics
- withdrawal with tombstone

**Optional / variant** — depends on segment, scale, and philosophy:

- automated harvesting from bibliographic databases with author-claim workflows
- researcher profiles and public portals
- funder/journal permission checking and open-access compliance machinery
- preservation programs (fixity checking, archival packages)
- journal and conference publishing add-ons
- exhibits and showcase layers
- metadata-only records (records without deposited files, linking out instead)

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Deposit form

The contributor's entry surface. Purpose: capture a work into the record.

- typical information: work type selection, metadata fields (title, creators, date, publication reference, abstract, subjects, organizational unit), file upload, license/agreement acceptance, embargo or access options where offered
- primary actions: choose work type, enter metadata, upload files, accept the agreement, submit for review

### Review / approval queue

The staff gate. Purpose: control what enters the public archive.

- typical information: pending deposits with depositor, work type, completeness indicators, duplicate warnings
- primary actions: open a deposit, edit metadata, approve and publish, return to depositor with a reason, assign to another staff member

### Item / metadata workbench

Where the record is maintained. Purpose: keep the archive accurate over time.

- typical information: record list with status, record detail with all metadata fields, attached files and their security settings, revision history
- primary actions: edit metadata, replace or add files, change access settings, move or reclassify, withdraw, resolve flagged duplicates

### Public work page

The workhorse of delivery. Purpose: present one work completely to any visitor.

- typical information: title, creators, publication reference, abstract, subjects, license, download options, persistent identifier, embargo notice where applicable
- primary actions: download files, view alternative versions, request a copy (where the product offers one), share or cite

### Public browse and search

The discovery surface. Purpose: make the corpus navigable.

- typical information: search box, browse lists by year / author / subject / organizational unit, collection or series listings, recent additions
- primary actions: search, filter, browse to a work page

### Administration and configuration

The operator's console. Purpose: configure and run the repository program.

- typical information: work types and metadata field definitions, vocabularies, user accounts and roles, workflow settings, harvest configuration, reports
- primary actions: configure types and fields, manage users and permissions, adjust workflows, run imports, view usage reports

### Researcher-facing surfaces (in many products)

Author account pages listing one's own deposits and their statuses (with revise/withdraw actions before publication), usage reports for one's works, and — in suite-integrated products — public researcher profiles gathering a person's outputs.

## Important Rules / Behaviors

### Publication is a controlled transition

A deposit exists in a non-public state until it is approved and installed into the archive; approval typically triggers indexing and identifier assignment. This gate is the institution's quality and policy control, and its depth (formal review vs direct publication) is an explicit institutional choice.

### Open by default, restricted by exception

The repository's posture is open access; restrictions are deliberate, per-work exceptions with defined mechanics. An embargo expires automatically on its date. When a file is restricted, its metadata page normally remains public and discoverable — the record stays findable even while the file is gated — and some products add a request path for restricted files.

### The record is durable; removal is deliberate

Because works acquire persistent identifiers and citations, repositories distinguish withdrawing a work (hidden, replaced by a visible tombstone) from fully deleting it. Silent disappearance is avoided.

### Version discipline matters

Publisher agreements usually permit only specific versions of a work to be self-archived (commonly the accepted manuscript rather than the published PDF). Mature repositories let records state which version is held, and staff manage files accordingly.

### Metadata stays harvestable

The repository publishes its metadata for harvesting by catalogs, discovery layers, and aggregators. The record is designed to outlive any single interface: files may be re-encoded, viewers replaced, sites redesigned — the work's identity and metadata persist.

### Duplicate control is structural

Works can enter twice (author deposit plus automated feed, multiple versions, name variants). Mature products detect likely duplicates at intake and surface them to staff for resolution, because a credible institutional record must not double-count its own output.

## Variants

- **Corpus scope** — publications and theses only; extended to datasets; extended to creative and performance works; extended to teaching materials; extended to patents. The broader the scope, the more the repository resembles a general institutional archive.
- **Intake mix** — author self-deposit-first (the classic open-access form); staff-mediated-first (library-run deposit services); automated-harvest-first (records flow in from bibliographic sources and researchers claim them). Most mature products support all three; the mix is an institutional choice.
- **Metadata-only vs full-text posture** — some repositories hold metadata-only records that link out to publisher copies; others require a deposited file per record. Both postures are documented in current products.
- **Standalone vs suite-integrated** — a dedicated repository platform versus a repository embedded in a research-information or library-services suite with profiles, portals, and analytics around it.
- **Hosting posture** — self-hosted open source, vendor-hosted SaaS, or services-backed hosting.
- **Publishing add-ons** — some platforms also run institutional journals and conference proceedings alongside the repository.
- **Policy environment** — funder open-access mandates, national assessment exercises, and journal permission checking shape workflows differently by country and institution type.

A variant remains a **Variant** unless it changes the defining core: a system that manages research information without openly delivering the institution's output content has moved to a different Type (research information management); a system that curates acquired heritage material has moved to another (digital library platform).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Digital Library Platform | closest sibling | The digital library platform curates collections of material the institution **acquires or digitizes** (heritage, archives, exhibits), with collection curation at its center. The institutional repository holds works the institution's own people **produced**, with intake at its center and an open-access posture. The same product can serve both roles — which is why the market blurs the labels — but the centers of gravity differ. |
| Research Information Management / CRIS | adjacent, upstream | A CRIS manages the institution's research **information** — people, grants, projects, outputs — for reporting and assessment. The repository holds and openly delivers the output **content**. Remove open content delivery and add people/grants/projects → CRIS. Suite products increasingly span both. |
| Integrated Library System / ILS | adjacent, ecosystem partner | The ILS runs the physical collection's operations — cataloging, circulation, acquisitions. The repository hosts the institution's scholarly output. They integrate (catalog and discovery layers index repository metadata) but neither replaces the other. |
| Library Discovery Platform | adjacent, complementary | A discovery layer searches across external sources. The repository is the **host** that discovery layers index. Remove the hosted item store and intake → discovery platform. |
| Archives Management System | adjacent | An archives system manages archival description and finding aids — intellectual control over archival holdings, often undigitized. The repository self-archives the institution's output for open delivery. |
| Academic Journal Management / Peer Review Platform | different stage | Journals run editorial decision workflows that produce publications. The repository captures and delivers works **after** the editorial fact — published articles, accepted manuscripts, theses. Vendors ship both as separate products in one suite, evidence of the structural difference. |
| Research Data Management | overlapping scope | Datasets are one work type within repository scope. Dedicated research data management adds data-specific machinery (domain metadata schemas, data management plans). Boundary to be confirmed in that Type's own documentation. |
| ePortfolio Platform | different subject | An ePortfolio is a person's learning/evidence record. The repository is the institution's published scholarly record. |

## Representative Products

- **DSpace** — open-source repository platform; the dominant system for institutional scholarly collections, equally used for digital collections of all kinds
- **EPrints** — open-source repository platform from the University of Southampton; the founding-generation institutional repository software, widely used for open-access journals and theses as well
- **Digital Commons (bepress / Elsevier)** — turnkey hosted institutional repository service, spanning small colleges to large universities, with journal and data add-ons
- **Esploro (Ex Libris)** — research-services platform whose repository function is integrated with researcher profiles, a public portal, and the library ecosystem

The defining core was checked against the founding generation of repository software (EPrints, begun in 2000; DSpace from the same founding era) to avoid defining the Type by today's hosted, harvesting-rich implementations.

## Sources

Research date: **2026-09-08**

- DSpace — Functional Overview, DSpace 7.x Documentation (LYRASIS wiki): https://wiki.lyrasis.org/display/DSDOC7x/Functional+Overview
- EPrints — What is EPrints? and The EPrints Platform (eprints.org): https://www.eprints.org/what-is-eprints/ , https://www.eprints.org/the-eprints-platform/
- EPrints Documentation wiki — EPrints Glossary and Introduction: https://wiki.eprints.org/w/EPrints_Glossary , https://wiki.eprints.org/w/Introduction
- Digital Commons Help Center — Digital Commons IR; Author Submission Steps; Access Control and Embargoes; Harvesting Tool: https://digitalcommons.elsevier.com/en_US/digital-commons-ir and linked articles
- Esploro Online Help (English) — Adding and Working with Research Deposits; product documentation index (Ex Libris Knowledge Center): https://knowledge.exlibrisgroup.com/Esploro/Product_Documentation/Esploro_Online_Help_(English)

> Sourcing limitations: operational documentation for Pure (Elsevier) was not fetched this pass; Pure is discussed only as a boundary reference in Related Application Types, at the level its official product page supports. The DSpace documentation fetched is the 7.x documentation tree; version-specific details were not re-verified against the current release. Precise operational limits, default settings, and numeric figures observed during research are intentionally not stated in this document.

Detailed evidence, product-by-product observations, cross-product comparison, and the historical sample check are recorded in the paired Research Notes.
