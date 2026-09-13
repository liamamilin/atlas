# Research Data Management

## Overview

A **Research Data Management application** is a research institution's system of record for governing its research data across the data lifecycle. It holds research **datasets** as persistent, identified, described records, and operates a stewardship loop over each dataset — planning how data will be managed, preparing and describing it, preserving it, and making it available to others under defined terms (or holding it under control when it cannot yet be shared).

The defining structure is small:

```text
Research dataset (unit of record)
  = data files + documentation + metadata, bound to a research context
    (project / study / depositor / funder), persistent beyond the project
+
Stewardship governance over the dataset's availability lifecycle
  = plan → prepare & describe → review → preserve
    → make available under terms / hold under control
    → reuse & report
    with access rules, versioning, and accountable closure
```

Everything else commonly associated with the category — DOIs, data management plans, domain metadata schemas, usage metrics, open-access compliance — is standard machinery built on this core, not the core itself. The category's ancestor, the scholarly data archive, ran the same two structures for decades with accession numbers and membership contracts instead of DOIs and funder mandates.

When the center of gravity shifts to the institution's scholarly *outputs* as a whole (papers, theses, media) with an open-access delivery posture, the product is an Institutional Repository. When it shifts to lab- and instrument-scale data files with capture machinery, it is a Scientific Data Management System. When it manages only the plan document, it is a planning fragment, not the full Type.

## Users & Context

Primary users:

- **Researchers / depositors** — produce data in a project and deposit it, describe it, choose licenses and access terms, version it, and cite it. They interact with the system at deposit time and at publication milestones.
- **Data stewards, curators, and data librarians** — review deposits, check metadata quality, manage embargoes and restricted access, and advise on data management plans. In institutions this role typically sits in the library or research office.

Secondary users:

- **Institutional administrators** — configure metadata schemas and submission policies, manage users, groups, storage allocations, and approval workflows.
- **Reusers** — other researchers who discover, evaluate, download, and cite datasets; their access may be open, gated by terms, or granted through request workflows.
- **Funders and publishers** — not operators, but the source of the policy pressure (data management plan requirements, open-data mandates, repository characteristics) that shapes what the system must enforce and evidence.

The work context is the research institution: universities, research institutes, funders, consortia, and publishers. The system is typically operated by a library, research office, or IT department, either as a hosted service or as self-installed open-source software.

## Core Model

### The Defining Core

**The research dataset as the managed unit of record.** A dataset is a persistent, identified bundle of research data: the data files themselves, the documentation that gives them context (readmes, codebooks, protocols), and the metadata that describes them (title, creators, description, dates, subjects, license, funding sources). The dataset is bound to a research context — a project, study, grant, or depositor — and it outlives the project: it remains addressable, citable, and governed after the research team moves on. Stable identity is part of the record; the DOI is today's common implementation, but the invariant is a durable identifier by which the dataset can be cited and retrieved.

**Stewardship governance over the dataset's availability lifecycle.** The dataset is not a static file drop; it moves through managed states. It is prepared and described, optionally reviewed by a curator, preserved under explicit commitments, and made available under defined terms — open, licensed, embargoed until a date, restricted to approved requesters, or held entirely under institutional control. Changes to published data are versioned rather than silently overwritten, and removal is an accountable act (a recorded reason; a citation-bearing tombstone rather than a silent deletion).

Remove the dataset of record and only a policy framework or a catalog remains. Remove the stewardship loop and only a file store remains. The two together are what make the system a system of record for research data.

### Standard Capabilities

Mature products commonly add:

- **Data management planning** — templates aligned to funder requirements, guidance and example answers, plan documents that state what data will exist, how it will be stored, documented, licensed, shared, and preserved, and when. Plans connect the grant stage to the deposit stage.
- **Persistent identifiers and data citation** — a DOI (or handle) per dataset, citation text generated by the system, version-specific citation where versioning exists.
- **Structured metadata with domain depth** — required citation fields plus optional domain-specific schemas (social science, life sciences, geospatial, astronomy), and export/harvesting of metadata into standard formats so discovery services can index the holdings.
- **Versioning** — published datasets are revised as new versions (major/minor, or new version records), with version history and differences visible; citations can point at the exact version used.
- **Access machinery** — embargoes that expire automatically at a set date, restricted files with terms of access, request-access workflows routed to the owner and administrators, download terms and guestbooks that record who took what.
- **Licensing** — standard open licenses (the Creative Commons suite is typical) and custom terms for data that cannot use standardized licenses.
- **Review workflow** — contributor submits; curator or administrator reviews and publishes or returns to author.
- **Discovery and metrics** — search and browse surfaces, indexing into scholarly discovery layers, and usage statistics (views, downloads, citations).
- **Preservation commitments** — bit-level preservation, backups, no-deletion posture, stated retention minimums.
- **Administration and integration** — user/group/storage management, bulk upload channels (FTP, API), and connections to ORCID, code repositories, research information systems, and lab systems.

### One Structure, Many Implementations

```text
Concept:            Dataset identity
Implementations:    DOI (DataCite), handle, accession number (archive era)

Concept:            Planning artifact
Implementations:    funder-specific DMP templates, generic checklists,
                    plan guidance embedded in repository help

Concept:            Availability posture
Implementations:    open by default with managed exceptions;
                    restricted-archive with contractual access

Concept:            Domain metadata
Implementations:    configurable metadata blocks, fixed schemas,
                    institution-customized fields

Concept:            Deployment
Implementations:    hosted SaaS, self-installed open source,
                    consortium-operated archive
```

A reader who has only seen a modern DOI-minting repository should still be able to recognize a 1970s social-science data archive as the same Type: identified holdings, curated deposits, governed access, long-term preservation.

## How It Works

### Plan

Before or during a project, the researcher (often with a data librarian) produces a data management plan: what data the project will produce, how it will be organized and documented, what will be shared and when, under what license, where it will be preserved, and for how long. Planning tools provide funder-specific templates and guidance; repositories provide compliance guidance that names themselves as the sharing destination. The plan is a commitment that the rest of the lifecycle executes.

### Prepare, deposit, and describe

```text
Create dataset record
→ upload data files (single files, folders, or bulk via FTP/API)
→ add documentation (readme, codebook, code)
→ fill required metadata (title, creators, description, subjects, dates)
→ choose a license and funding attribution
→ save as draft
```

The draft is private to the depositor and invited collaborators. Files may receive checksums; some systems extract technical metadata from known formats (tabular, geospatial, astronomical).

### Review and publish

```text
Submit for review (where institutional review applies)
→ curator checks metadata quality and policy fit
→ publish (or return to author with changes requested)
```

Publication is the system's commitment point: the dataset becomes findable, its identifier is registered, and — the defining rule — published content becomes immutable. Files can no longer be modified or deleted; corrections happen as new versions. In several products publication is explicitly irreversible.

### Make available under terms

The published dataset's metadata is public and findable; the files' availability is governed:

- **Open** — anyone downloads under the stated license.
- **Embargoed** — files are inaccessible until a set date, then open automatically; the metadata and identifier are visible now. Embargoes serve journal and funder agreements ("data becomes available when the paper publishes").
- **Restricted** — files require terms of access; requesters ask, the owner and administrators approve; some systems track every download through guestbooks.
- **Held** — permanently restricted or institution-controlled content, with the record still asserting the data's existence and terms.

### Preserve and version

After publication, edits create a new draft version; publishing it produces a new version (major for file changes, minor for metadata-only changes in the common scheme). Version history and differences are visible; each version remains citable. Preservation runs underneath: fixity checks, redundant storage, backup replication, and a no-deletion posture. Where a product permits removal at all, it is a deliberate, reasoned act that leaves a tombstone page with the citation so prior citations still resolve.

### Reuse and report

Reusers discover datasets through search and through scholarly discovery services that harvest the system's metadata. They download under terms, cite with the provided citation, and their usage accumulates into metrics (views, downloads, citations) that depositors and institutions report — increasingly a currency in funder reviews alongside the publications the data supports.

## Interfaces

### Deposit / dataset editing form

The researcher's primary working surface: metadata fields (required and domain-specific), file upload with folder structure, license selection, funding attribution, access settings (embargo, restriction), and collaborator invitations. Draft state is always visible.

### Dataset page (public)

The canonical address of the record: citation with identifier, metadata, file list with sizes and formats, license and terms, version history, metrics, and download/request controls. Restricted and embargoed files show their state and the route to request access.

### Collection / community browse

The organizational layer above datasets: an institution's groups, a project's community, a funder's collection. Provides curated browsing, submission-to-community review in some products, and the institutional "front door" for discovery.

### Search

Faceted search over metadata (subject, creator, date, license, file type, domain). The system's own search is complemented by metadata export/harvesting that feeds external discovery services.

### Data management plan editor (where present)

Template-driven plan authoring: funder requirement templates, question-by-question guidance, example answers, institutional customization, plan export for grant submission. In planning-only products this is the entire product; in repository products it appears as guidance and compliance support.

### Administration console

User and group management, storage quotas, submission/approval queues, metadata schema configuration, embargo and restriction policy settings, integration credentials, and usage reporting.

## Important Rules / Behaviors

- **Published data is immutable.** Once published, files and the persistent identifier cannot be modified; metadata may be corrected in some products, but the archival principle is that anyone who cited a dataset must find it unchanged. Corrections arrive as new versions.
- **Publication is treated as a one-way door.** Products either forbid unpublishing outright or treat it as an exceptional, advised-against correction; the normal route for change is versioning.
- **Removal, where a product allows it at all, is accountable, not silent.** A recorded reason is required, and a public tombstone with the citation remains so prior citations still resolve; products that forbid deletion simply never reach this state.
- **Embargoes are time-locked and automatic.** Access opens at the set date without further action; embargoes typically cannot be altered by the depositor after publication.
- **Restriction is a managed exception, not a hiding place.** Restricted files remain visible as records (metadata, terms, request route); the system records who accessed what — guestbooks and request logs are part of the accountability.
- **Licensing is mandatory metadata.** A machine-readable license (or explicit custom terms) is required at publication; reuse rights are part of the record, not an afterthought.
- **Versioning has semantics.** File changes force major versions; metadata-only changes can be minor; version-specific citations keep analyses reproducible.
- **Preservation is a stated commitment.** Bit-level preservation, backups, and retention minimums are product-level promises that institutions rely on for funder compliance.
- **The plan binds the lifecycle.** Where data management planning is present, the plan's commitments (what to share, when, where, how long) are the standard against which the deposit and availability decisions are checked.

## Variants

- **Generalist research-output repositories** — datasets alongside papers, theses, software, media; the dataset is one item type among many (common in publisher- and funder-facing services).
- **Data-centric repositories** — the dataset is the primary object, with domain-aware metadata and tabular/geospatial handling.
- **Discipline data archives** — curated archives for a field (classic social-science data archives), often consortium-operated, with deep curation and restricted-use handling.
- **Institutional repositories with data services** — the institution's own repository operated as its RDM infrastructure, often paired with research information systems.
- **Planning-only tools** — standalone data management plan authoring platforms; the planning fragment of the lifecycle without a data of record.
- **Open-by-default vs restricted-archive postures** — the same core under opposite defaults; sensitive-data institutions run the restricted pole with request/access machinery doing the heavy lifting.
- **Deployment shapes** — hosted SaaS, self-installed open-source platforms run by universities or national infrastructures, and consortium-operated membership archives.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Institutional Repository | adjacent, heavily overlapping in products | IR's center of gravity is the institution's scholarly output collection (papers, theses, media) with an open-access delivery posture; datasets are one work type. RDM's center is the dataset lifecycle with data-specific machinery (domain schemas, DMP linkage, embargo/licensing/retention depth). Products span both; the Types remain distinct. |
| Scientific Data Management System | adjacent | SDMS operates lab/instrument-scale data files with capture machinery (instrument outputs, adaptors); RDM governs institution-scale datasets, plans, and repositories under funder policy. |
| Research LIMS | adjacent | LIMS manages physical specimens and lab workflows; it feeds data toward RDM but does not govern institutional data compliance or availability. |
| Data Management Planning tools | fragment of this Type | Planning tools manage plan documents only — no dataset of record, no availability lifecycle. A capability of RDM sold standalone, not a separate Type. |
| Data Catalog / data portals | different Type | Catalogs describe data that lives elsewhere as catalog entries for discovery; RDM holds and governs the data of record with lifecycle stewardship, preservation, and citation semantics. Generic open-data portals share the word "dataset" but not the stewardship loop. |
| Electronic Data Capture / Clinical Data Management | upstream | EDC captures trial data at sites; CDM cleans and locks it. RDM takes custody afterward for stewardship, sharing, and preservation across the institution's research. |
| Research Information Management / CRIS | ecosystem partner | CRIS aggregates research information (publications, grants, datasets as metadata); RDM holds and governs the data itself. Integrations hand metadata and context between them. |
| Research Grant Management | planning linkage only | DMPs attach to grants and funder requirements, but grants manage money and milestones; RDM manages the data. |
| File storage / sync | substrate | Storage is a configurable substrate beneath every RDM product; the record plus governance is the product. Metadata-only records that link to externally held data are legitimate. |

## Representative Products

- **Figshare** — commercial institutional repository/data repository service; strong embargo/restriction machinery, funder-policy compliance framing, and DMP guidance.
- **Dataverse** — open-source dataset-centric repository software (Harvard-origin); deep versioning, citation, and access-control semantics; self-hosted by universities and archives worldwide.
- **Zenodo** — generalist open repository (CERN, built on InvenioRDM); community curation, NIH and Horizon Europe data-sharing guidance.
- **DMPonline** (Digital Curation Centre) — planning-only platform; included as the boundary probe for the planning fragment.
- **ICPSR** — consortium social-science data archive; included as the historical anchor demonstrating the Type's pre-web form.

## Sources

Research date: **2026-09-10**

- Figshare — product site and user guides: https://info.figshare.com/ , https://info.figshare.com/academic-institutions/ , https://info.figshare.com/user-guides/ , https://info.figshare.com/user-guide/embargoes-and-restricted-access-publishing/ , https://info.figshare.com/user-guide/how-to-write-a-data-management-plan-dmp-and-include-figshare-in-your-data-sharing-plans/
- Dataverse — official guides: https://guides.dataverse.org/en/latest/quickstart/what-is-dataverse.html , https://guides.dataverse.org/en/latest/user/dataset-management.html
- Zenodo — official help and docs: https://help.zenodo.org/ , https://help.zenodo.org/docs/deposit/about-records/
- DMPonline (Digital Curation Centre) — https://dmponline.dcc.ac.uk/ , https://dmponline.dcc.ac.uk/help
- CKAN — https://ckan.org/ (counter-sample for the data-portal boundary)
- ICPSR — https://www.icpsr.umich.edu/web/pages/about/index.html (historical anchor)

> Sourcing limitations: the figshare.com application root and the Figshare support site were not reachable from the research environment (HTTP 403 / 404); official product-site pages and user guides were used instead, and Figshare's institutional approval-queue mechanics are asserted only at the level its official pages state. Precise numeric limits, pricing, and vendor-specific defaults are intentionally omitted from this document; they remain in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
