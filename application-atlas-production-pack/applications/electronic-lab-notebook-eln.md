# Electronic Lab Notebook / ELN

## Overview

An **Electronic Lab Notebook (ELN)** is a research-side system of record for experimental work. Researchers document experiments as dated, attributed, tamper-evident records — entries that hold text together with the evidence of the work: tables, images, instrument output, and data files. Records accumulate in durable containers (notebooks, projects), remain retrievable for years, and can be attested (signed, witnessed, timestamped) so they stand up as evidence for research integrity, intellectual property, and regulatory inspection.

The defining core is deliberately small — it is the contract of the paper lab notebook made digital:

```text
Notebook / Project (durable container)
└── Experiment record (entry / experiment / page)
    └── Evidential content (text + tables + files + data)
    └── Attribution + timestamps + preserved change history
    └── Persistent, retrievable archive
```

Everything else commonly associated with modern ELNs — protocol templates, structured forms, sample inventory, integrations, publishing, AI assistance — is widespread capability, not definition. Remove the inventory or the AI and the product is still unmistakably an ELN; remove the experiment record, the evidential content, or the tamper-evident attribution and it becomes a generic notes tool, a wiki, or a document store.

## Users & Context

Primary users are bench scientists and researchers who perform and document experimental work:

- **Researcher / scientist**: writes experiment records as the work happens; attaches results, uploads data files, imports instrument output; returns later to complete or extend records.
- **Principal investigator / lab head**: oversees the lab's records — reviews and approves entries, checks that documentation standards are met, keeps oversight of the group's work.
- **Lab manager / technician**: maintains protocols, keeps records current, often manages the inventory items referenced in experiments.

Secondary users appear in organizational settings:

- **Quality / regulatory personnel** (regulated industry): witness or approve records, rely on audit trails and signature histories during inspections.
- **IT / research-data staff** (institutions): provision the system, manage permissions at scale, support export and archiving obligations.

Typical context: academic labs, biotech and pharma R&D, chemistry, materials, food and agricultural research — anywhere experimental work must be documented as it happens and defended later. The ELN is used continuously during experiments (at the bench, often via laptop or tablet) and episodically afterwards (writing up, repeating experiments, audits, patent work, onboarding new members who need to read past work).

## Core Model

### The Defining Core

Four structures. If any one is removed, the product is no longer recognizable as an ELN.

- **The experiment record inside a durable container.** The unit of record is a bounded piece of experimental work — an entry, experiment, or page — placed in a persistent organizational structure such as a notebook or project, usually with intermediate folders or groupings. The container outlives any individual; the record is the durable artifact.
- **Evidential content.** A record can hold the evidence of the work: free-form text plus embedded tables, images, and files. Mature products extend this with domain-specific objects (chemical structures, sequence files) and structured capture (typed tables, forms), but text-plus-evidence is the irreducible form.
- **Attributed, timestamped, tamper-evident records.** Each record carries who created or authored it and when. The system preserves the history of changes — version history, audit trail — so nothing can be silently altered. In mature products records can also be locked or sealed at a defined point, and signed (or, in regulated settings, witnessed) by a second party. This is what makes the record *evidence* rather than merely *notes*.
- **Durable accumulation with retrieval.** Records persist for years and can be found again — by browsing the container structure and, in modern products, by full-text search across content and metadata.

### Standard Capabilities of Mature Products

These capabilities are common across the market. They make the ELN practical, but they do not define it.

- **Templates and protocols.** Reusable entry templates, versioned protocol documents, and admin-governed template libraries so experiments are recorded consistently; some products import protocols from external protocol repositories and let users check off protocol steps during execution.
- **Structured capture.** Tables with typed columns and formulas; form-based data entry; metadata fields and classification schemas on records.
- **Sign-off and review.** A record can be sent for review, routed through one or more reviewer stages (self, parallel, or sequential), and closed with recorded approval — often with re-authentication at signing and a preserved signature history. Two-person witnessing is the regulated-industry form of this.
- **Team permissions.** Notebook- or project-scoped roles (own records, edit the group's records, view only), external collaborators, and section-level access restrictions.
- **Search.** Corpus-wide search over text, metadata, and files; some products add domain-specific search (e.g., chemical structures).
- **Inventory linkage.** Samples, reagents, and equipment recorded in an inventory (built in, bundled, or as a companion product) and referenced from experiment records, so a record shows which materials produced which results.
- **Export and archiving.** PDF and office-format exports, data exports, read-only share links, offline copies; institutional products add repository publishing (DOIs, data repositories) and portable export formats.
- **Collaboration mechanics.** Comments, mentions, notifications, activity feeds; simultaneous co-editing in some products.
- **APIs and integrations.** Connections to desktop editors, analysis tools, institutional storage, and instruments.

### One Structure, Many Implementations

The core is conceptual; products realize it differently.

```text
Concept:   Experiment record
Realizations:  notebook entry · experiment with tasks · notebook page with entries · research document

Concept:   Tamper-evidence
Realizations:  version history with restore · audit trail · record locking · trusted/blockchain timestamps · signature with re-authentication

Concept:   Attestation
Realizations:  author sign-off · multi-stage review · electronic witnessing · notarization-grade timestamping

Concept:   Evidence content
Realizations:  rich text + attachments · tables with formulas · embedded office documents · chemical sketches · sequence files · forms
```

## How It Works

### Document an experiment

```text
Open or create a record in the notebook/project
→ write the procedure and observations (or start from a template/protocol)
→ embed the evidence: tables, images, instrument files, data exports
→ the system timestamps the work and attributes it to its author(s)
→ keep working; every change is captured in the record's history
```

The record grows during the work and remains open for extension. Attribution and timestamps accumulate automatically; the researcher does not manage them.

### Close and attest a record

```text
Finish the record
→ send it for review / apply a signature (re-authenticating at the moment of signing)
→ reviewers approve or witness; the record may lock against further edits
→ the record's completion, signatures, and any later exceptions are all preserved
```

Not every lab uses formal review; in academic settings records are often simply kept, while regulated environments require signature chains. Both operate on the same underlying property: the record's history is preserved and its state changes are attributable.

### Find and reuse past work

```text
Search (text, metadata, sometimes domain-specific queries) or browse the container tree
→ open the record; read the full history and original evidence
→ repeat or adapt: clone the record or its template for the next experiment
```

This retrieval loop is the practical payoff: the notebook becomes the lab's long-term memory, and newcomers read how work was actually done.

### Share and hand off

```text
Share records or read-only links with collaborators
→ export records (PDF, office or data formats) for reports, theses, or filings
→ in institutional settings: publish selected records to repositories with persistent identifiers
```

## Interfaces

Exact layouts and names vary by product; these are the surfaces an ELN reader should expect.

### Notebook / project browser

The entry surface. Lists the user's notebooks or projects, usually as a tree of containers with folders below.

- typical information: container names, recent activity, record counts or dates
- primary actions: create notebook/project, create a record, navigate, search

### Experiment record editor

The central surface — the digital page.

- typical information: title, author(s), dates, the body (text, sections, tables), attachments, embedded objects, comments
- primary actions: write and format text, insert tables/files/images, link other records or inventory items, insert dates/sections, comment, share

### Record metadata / info panel

The evidence posture of a single record.

- typical information: authors, created/modified timestamps, status, schema/classification fields, links
- primary actions: add or change authors, apply classification fields, move the record, export

### History / audit view

The tamper-evidence surface.

- typical information: version list with timestamps and editors, audit events, signature history where present
- primary actions: preview a version, restore or clone from a version, inspect who changed what

### Review / signature surface

Where attestation happens.

- typical information: pending reviews, signature requests, reviewer stages, completed signatures with comments
- primary actions: send for review, approve / witness / reject, sign with re-authentication, cancel or reopen

### Search

Corpus-wide retrieval over records, attachments, and metadata.

- primary actions: keyword search, filter by container/author/date, sometimes structure-based queries

### Administration

- typical information: users, roles, template libraries, audit configuration
- primary actions: manage members and permissions, configure templates and review processes, oversee compliance settings

## Important Rules / Behaviors

- **Attribution is structural, not optional.** Every record has authors and timestamps that the system manages; authors cannot be silently detached from their work, and the initial date of a record is typically fixed as audit metadata.
- **History is preserved, not replaced.** Editing a record adds to its history rather than overwriting it; earlier versions remain inspectable and often restorable. Deleting or retracting content is itself a recorded event.
- **Sealed records resist change.** Where records are signed or sent for review, editing is typically blocked while the record sits in its review state; reopening it (when permitted) is itself logged, and existing signatures may have to be formally revoked.
- **Signing re-proves identity.** Applying a signature generally requires fresh authentication rather than relying on the open session — the signature must mean "this person, at this moment".
- **Permissions shape visibility and edit rights.** A researcher normally controls their own records; group edit rights, view-only roles, and section-level restrictions are governed by the notebook/project's permission model. Reviewers usually need at least read access.
- **The archive is expected to outlive projects.** Records remain readable long after work ends; export and archiving exist precisely because labs, people, and funding move on.
- **Compliance behavior is segment-dependent.** In regulated settings the same machinery becomes formal: witnessing requirements, validated environments, inspection-ready audit trails. In academic settings the same properties serve integrity and IP without the formal apparatus.

## Variants

- **Notebook-first standalone ELN** — the notebook is the product; academic labs and mid-size organizations are the natural home.
- **Platform-embedded notebook** — the notebook is one module of a wider R&D data platform (alongside registries, inventory, results, analytics); common in enterprise life sciences.
- **Institutional / RDM-oriented ELN** — emphasis on institutional deployment, data management policy, persistent identifiers, repository hand-off; often open source or institution-hosted.
- **Regulated-industry ELN** — signature/witness machinery, validated environments, audit posture as first-class selling points.
- **Education ELN** — the same notebook machinery wrapped in courses, assignments, and student roles.
- **Self-hosted / open-source ELN** — institute-level installations hosting many teams; attestation often leans on timestamping mechanisms.
- **Deployment axes** — cloud SaaS vs self-hosted; single lab vs whole-institution; single discipline vs generalist.

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| Laboratory Information Management System / LIMS | adjacent, most-confusable | LIMS is operation-centered: samples flow through lab processes (accessioning, workflows, results, chain of custody). ELN is documentation-centered: the experiment record is the spine, and samples are *referenced* from records. Remove the experiment record → sample operations software; remove sample workflow management → still an ELN. |
| Research LIMS | adjacent | research-context LIMS; same documentation-vs-operations seam; boundary deserves joint refinement |
| Scientific Data Management System | adjacent | manages scientific datasets and their curation; the ELN's unit is the ongoing experiment record; publishing exports are the hand-off seam |
| Research Data Management | adjacent | institution-scale preservation, sharing, and publication of data; an ELN records work in progress; some products straddle both |
| Note-taking Application | adjacent | records personal notes; lacks experiment-record semantics, tamper-evidence, attestation, and regulatory posture |
| Wiki Application | adjacent | team knowledge base; version history serves collaboration, not evidential integrity; no record-of-experiment shape |
| Collaborative Document Editor | adjacent | prose authoring; no container→experiment record hierarchy, no sign-off/audit posture for evidence |
| Electronic Trial Master File / eTMF | adjacent in regulated research | holds trial-governance document collections; different unit of record and lifecycle owner |
| Project Management Application | weak adjacency | ELNs carry project containers to organize records, not to plan/schedule/track work as a managed workflow |

The load-bearing boundary is with LIMS: both live in the lab and both mention samples, but one documents experiments and the other operates the flow of samples and work. The second-most-important boundary is with notes/wikis: tamper-evidence plus the experiment record is what separates a system of record from a system of collaboration.

## Representative Products

- Benchling — structure-aware life-sciences R&D platform with the Notebook at its center
- SciNote — structured projects/experiments/tasks ELN with protocols, inventory, and compliance add-ons
- LabArchives — notebook-first ELN with strong university, education, and government editions
- RSpace — institutional, FAIR-oriented research notebook with integrated sample and file management
- eLabFTW — open-source, self-hosted ELN for research teams

The defining core was checked against the paper-notebook ancestor and against early-generation and self-hosted institutional products, so it does not depend on current cloud, AI, or inventory features.

## Sources

Research date: **2026-09-07**

- Benchling Help Center — Product Documentation → Data Capture → Notebook; "Plan experiments and collect data in the Notebook"; "Create and use review processes" — https://help.benchling.com/
- SciNote — product site (https://www.scinote.net/); Knowledge Base: "How to sign a task using an electronic signature and move a task to 'In review' status", "Is SciNote 21 CFR Part 11 compliant?" — https://knowledgebase.scinote.net/en/knowledge
- LabArchives — product site (https://www.labarchives.com/); Help Center ELN category (sections incl. Creating and Organizing Notebooks, Revision History and Timestamps, Search/Track/Apply Electronic Signatures, Publishing and Exporting) — https://help.labarchives.com/hc/en-us
- RSpace — product site and ELN page — https://www.researchspace.com/ , https://www.researchspace.com/eln
- eLabFTW — official repository README — https://github.com/elabftw/elabftw

> Sourcing limitations: the eLabFTW official user guide (doc.elabftw.net) was unreachable during research; eLabFTW claims are limited to its official README and asserted conservatively. RSpace evidence is product-page level; its operational documentation was not fetched. LabArchives feature existence is observed at help-index level; article-level mechanics are not asserted. Accordingly, this document avoids precise numeric limits, exact status names, and plan-specific behaviors; conceptual wording ("typically", "mature products commonly") reflects the available evidence.

Detailed product-by-product observations, the cross-product comparison, and the boundary analysis are recorded in the paired Research Notes.
