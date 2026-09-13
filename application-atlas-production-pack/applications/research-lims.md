# Research LIMS

## Overview

A **Research LIMS** is a research laboratory's system of record for its specimen-based work: it registers each research sample as an identified record tied to its source, study or experiment, moves it through the lab's own protocol-defined stages of processing, captures the results and derived data with their full provenance, and retains the whole as a traceable record that feeds analysis, publication and collaboration.

The problem it solves is the one every research lab shares: physical samples — biological specimens, cell lines, constructs, extracts, environmental collections — accumulate over years, the people handling them change constantly, and the lab must always know what exists, where it is, what was done to it, by whom, and what was found, so that any result can be traced back to its material and method. Before such a system, labs ran this on sample registers, freezer box maps, notebook cross-references and spreadsheets; a Research LIMS replaces that with one connected, attributable record.

The defining core is small — a specimen tracked through a managed protocol workflow to provenance-tracked results, retained traceably. Everything else commonly associated with these products (lineage trees, freezer maps, reagent inventory, instrument connections, notebook integration, compliance support) is standard capability that mature products add, not what makes the product a Research LIMS.

A Research LIMS is the research-context form of the Laboratory Information Management System: the same sample-workflow core that testing and quality-control laboratories use, shaped by research practice — work configured to each lab's own science, results valued as evidence for reproducibility rather than certificates, and the record coupled to the experiment documentation and data-analysis layers. When the organizing subject shifts to the patient (clinical care) or to the experiment narrative itself (the lab notebook), the product is drifting toward a different Application Type.

## Users & Context

The primary users are the people who do and run research at the bench:

- **bench scientists / researchers** — register samples, record where material is stored and what has been done to it, link each sample to the experiment that produced or consumed it, and capture results
- **lab managers / lab operations staff** — configure sample types and workflows, manage storage and inventory, keep the lab's records audit-ready, and maintain continuity as students and postdocs rotate through
- **core facility and service-lab staff** — receive submitted samples, run them through standardized processing workflows, and return results and status to submitters

Secondary users:

- **principal investigators / research leads** — oversee the lab's sample estate and its results across projects and years
- **collaborators and external submitters** — in service and core-facility settings, submit samples, track progress and receive results through a portal
- **IT / research informatics staff** — configure integrations with instruments, analysis pipelines and institutional systems

The context is any research organization whose work is anchored in physical specimens: academic life-science labs, biotech and biopharma R&D, genomics and sequencing facilities, biobanks and biorepositories, government research institutes, agricultural and industrial research labs, and histology or analytical research services. Two conditions shape the whole: research runs for years with frequent contributor turnover (so the record must outlive any individual's memory), and the record's audience includes future reviewers — collaborators, auditors, journals — which is why provenance, not just storage, is the point.

## Core Model

### The Defining Core

```text
Research specimen of record
└── Origin and lineage context (source, study/experiment, aliquots and derivatives)
    └── Managed protocol workflow
        └── Provenance-tracked result of record
            └── Traceable, attributable retention
```

Four properties. If any one is removed, the product is no longer recognizable as a Research LIMS:

- **Research specimen of record** — every physical sample in the lab's custody becomes a persistent, individually identified record: a unique identifier plus its type, metadata and status. Samples are the unit the whole system hangs from; work, results and documentation all attach to them. Without this, the product is a spreadsheet or a task tracker with no laboratory subject.
- **Origin and lineage context** — a research specimen carries where it came from (source, subject, parent sample, the experiment that generated it) and, in mature products, an explicit lineage of aliquots and derivatives with parent–child relationships preserved. This is what makes a result interpretable years later: the material's history travels with it. Without it, the system holds anonymous tubes.
- **Managed protocol workflow** — the lab's work is organized as defined stages the specimen moves through — registration, processing, assay, disposition — orchestrated by the system through statuses and worklists. Critically, these stages are configured to each lab's own protocols and methods, and they change as the science changes. Without this, the product is a static registry that never moves anything.
- **Provenance-tracked result of record** — results and derived data are captured per assay or experiment — manually or from instruments — attributed to the specimens and methods that produced them, and retained as the lab's evidence-bearing record. The value of a research result lies in being able to trace it back to its material, method, instrument and operator; that linkage is the product. Without it, the system tracks material but produces nothing defensible.

Binding these is the **traceability posture**: the record is attributable and auditable. Every action — registration, movement, storage change, modification, with user and timestamp — is logged. In a research setting this posture is provenance and reproducibility: the record exists so that results can be defended in collaboration, review, audit and publication, and so that work survives contributor turnover.

These properties are jointly held. A sample list without workflow is a freezer spreadsheet. A workflow engine without specimens has nothing to work on. Results without the specimen-and-method chain are just numbers. The joint hold is the Type.

### Standard Capabilities of Mature Products

A typical modern Research LIMS carries most of the following. They make the product practical, but they are not what makes it a Research LIMS:

- **Lineage and aliquot modeling** — parent–child relationships between originals, aliquots and derivatives, with genealogy views; the signature capability of the research form of this Type
- **Storage depth** — freezers, cold rooms and other storage units mapped as racks, boxes and positions, with capacity, movement history, checkout tracking and freeze/thaw history
- **Reagent and consumable inventory** — stock levels, low-stock alerts, shopping lists and order tracking from request to fulfillment
- **Instrument integration** — results imported from connected instruments, commonly transformed on ingest; instrument registration with maintenance and calibration scheduling
- **Experiment documentation coupling** — an integrated or connected electronic lab notebook whose entries reference the actual samples, results and workflows they document
- **Configuration without code** — sample types, custom metadata fields, status workflows and storage hierarchies defined by the lab itself, adapting as the science evolves
- **Roles, permissions and audit trail** — role-based access and a timestamped log of every change and access
- **Search** — advanced search over the specimen and result corpus, with saved and shareable queries in mature products
- **Barcode and label identification** — printed labels and scanned identification at bench and storage points
- **Reporting and export** — report generation and audit-ready exports assembled for papers, tech transfer or inspection
- **Submitter portals** — in service and core-facility deployments, external submitters create requests, track status and receive results
- **Analysis handoff** — connection to downstream analysis: sequencing run setup and secondary analysis in genomics, bioinformatics workspaces in data-platform products

One structure, many implementations:

```text
Concept:            Specimen identification
Implementations:    handwritten accession numbers (paper era), sequential IDs,
                    barcode/RFID labels

Concept:            Origin and lineage context
Implementations:    notebook cross-references (paper era), source/subject fields,
                    parent–child aliquot trees, genealogy views

Concept:            Work orchestration
Implementations:    protocol binders and bench sheets (paper era), configured
                    status workflows, preconfigured protocol libraries,
                    protocol/experiment structures

Concept:            Results with provenance
Implementations:    signed results in a bound register (paper era), assay data
                    linked to samples and experiments, instrument imports with
                    transformation, version-controlled records

Concept:            Traceability
Implementations:    register + box map + notebook (paper era), audit trail with
                    user/timestamp on every action, chain-of-custody timelines
```

A reader who has only seen a modern cloud product should still be able to recognize a small academic lab running a shared database, or a sequencing core facility running a genomics LIMS, from the same core.

## How It Works

The typical loop of a research laboratory, as the application supports it:

### Register the specimen

```text
Sample enters the lab (collected, received, or created by an experiment)
→ registered with a unique identifier and its type
→ origin captured: source or subject, parent sample, generating experiment
→ custom metadata recorded per the lab's sample type
→ storage location assigned (freezer, rack, box, position)
→ status: in custody / awaiting work
```

### Process under the lab's protocols

```text
Work requested or scheduled against the specimen
→ system moves it through the lab's configured stages
→ bench scientist performs each step per the lab's protocol
→ aliquots or derivatives created where the material is split or transformed,
   linked back to the parent
→ status advances with each completed step
```

### Capture results with provenance

```text
Results recorded manually or imported from instruments
→ each result linked to its specimen, method and operator
→ derived data associated with the experiment that produced it
→ review or sign-off where the lab requires it
→ notebook entries, where used, reference the same records
```

### Use the record

```text
Search the specimen and result corpus
→ assemble reports or audit-ready exports for papers, tech transfer, inspection
→ hand material or protocols to collaborators with history intact
→ feed results onward to analysis pipelines where connected
→ the complete history — every movement, change and attribution — retained
```

### Core vs standard vs optional

**Defining core** — without these, not a Research LIMS:

- research specimen of record with identification and metadata
- origin and lineage context for the material
- managed protocol workflow configured to the lab's own methods
- provenance-tracked results of record
- traceable, attributable retention of the whole

**Standard capabilities** — present in most mature products:

- lineage/aliquot trees, freezer-depth storage, inventory and ordering, instrument integration, notebook coupling, no-code configuration, roles and audit trail, search, labels, reporting/export, submitter portals, analysis handoff

**Optional / variant** — depends on domain, scale and regulatory posture:

- preconfigured protocol libraries for a specific science, specification/QC enforcement for regulated research, biobanking depth, clinical/translational data capture, AI assistance, industry-specific editions

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Sample registration / catalog

The entry surface where material becomes records.

- fields for type, origin (source/subject/parent/experiment), custom metadata, storage assignment
- primary actions: register, import batches, print labels, define new sample types

### Storage browser

The lab's freezer estate as a navigable map.

- storage units rendered as racks, boxes and positions with occupancy and capacity
- primary actions: locate a sample, move material, record checkout/check-in, inspect storage history

### Worklist / workflow view

The bench worker's daily surface.

- work due per specimen or protocol stage, with status and priority
- primary actions: open a work item, record results, advance status, create aliquots

### Specimen detail

The record of one sample's life in the lab.

- identification, origin and lineage tree, storage history, linked experiments and results, audit timeline
- primary actions: update status, split/aliquot, link records, inspect full history

### Result and experiment linkage

The surface where data connects back to material.

- results per assay with their specimen, method and operator attribution
- primary actions: import/enter results, link to experiments, review and sign where required

### Search

A primary surface, because the corpus is the lab's memory.

- advanced filters over types, metadata, status, location and lineage; saved and shared queries in mature products

### Configuration and administration

The lab manager's surface — a defining interface of this Type, since each lab configures its own science.

- sample types and fields, workflow stages, storage hierarchies, roles, instrument registrations, integrations

### Submitter portal (service deployments)

The external submitter's window.

- submit requests, track progress, receive results; visibility restricted to the submitter's own material

## Important Rules / Behaviors

### The record outlives the people

Research work spans years with constant contributor turnover; the system's purpose is continuity — a new student can find what exists, where it is and what was done without asking anyone. Records are organized so that history is attached to the material, not to individuals' memories.

### Provenance is the product

A result without its specimen-and-method chain is not usable evidence. Mature products make the linkage automatic: results attach to samples and experiments at capture time, and every modification is logged with user and timestamp, including the reason for the change.

### Work follows the lab's own defined stages

The workflow a specimen follows is the lab's configured process, not a fixed external menu — and it changes as the science changes. In regulated research settings the same machinery enforces step adherence and captures deviations automatically rather than after the fact.

### Lineage must be preserved

When material is split, aliquoted or transformed, the parent–child relationship is recorded and preserved; downstream results remain traceable to the original source through the chain.

### Storage is part of the record

Where a sample sits — which freezer, which rack, which box, which position — is tracked with its movement history; material that cannot be found is material that was never recorded.

### Access follows roles

What a user can see and do follows their role: bench scientists see their work, external submitters see only their own material, managers configure and oversee. In collaborative research, fine-grained permissions and data partitioning control what is shared with whom.

## Variants

Common shapes of the Type:

- **genomics / sequencing LIMS** — specimen and workflow management built around sequencing pipelines: preconfigured protocol workflows, sample sheets, pooling controls, run setup and secondary-analysis handoff
- **biologics / R&D LIMS** — construct and cell-line registries with lineage from design through assay, coupled to notebooks and workflow managers
- **biobank-oriented deployments** — the same core weighted toward long-term specimen custody and storage depth (the storage-first pole borders Biobank Management territory)
- **lightweight academic lab systems** — sample tracking, storage and inventory with notebook coupling, priced and simplified for academic labs and startups
- **ELN+LIMS hybrid platforms** — experiment documentation, sample management and often safety management sold as one connected platform
- **data-platform LIMS** — the specimen workflow embedded in a wider scientific data platform with bioinformatics, study data and analytics
- **service / core-facility deployments** — submitter portals, request intake and status return for labs that process other researchers' material
- **regulated research deployments** — specification/QC enforcement, electronic signatures and validation support where the research lab operates under Part 11-class or clinical-laboratory expectations

A variant should remain a variant, not a separate Type, unless it changes the organizing subject — as the clinical LIS and the experiment-record ELN Types do.

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| Laboratory Information Management System / LIMS | parent Type | the generic Type serves testing-service and production-QC laboratories; the research form is the same sample-workflow core shaped by research practice — protocol-configurable work, provenance-bearing results feeding analysis and publication, freezer-depth storage |
| Electronic Lab Notebook / ELN | documentation twin | the ELN's spine is the experiment record — notes, protocols, observations; the Research LIMS spine is the specimen workflow. Hybrid platforms bundle both; bundling does not merge them |
| Laboratory Information System / LIS | clinical sibling | LIS is patient-centric clinical diagnostic testing in a care context; the Research LIMS is specimen-centric research work. Clinical/translational research deployments keep the specimen-and-study frame |
| Biobank Management | storage-centric neighbor | long-term specimen banking and custody is the spine there; the Research LIMS spine is the processing workflow. Biobanking modules appear inside research LIMS products — the storage-first pole is the boundary zone |
| Research Data Management | institutional neighbor | RDM governs an institution's research data — datasets, plans, repositories, funder mandates; the Research LIMS operates the lab's physical specimens and their processing. One feeds the other |
| Scientific Data Management System / SDMS | data-file layer | SDMS manages instrument data files and lab documents; some vendors ship LIMS and SDMS as separate products of one platform |
| Scientific Instrument Management | instrument-centric neighbor | booking, maintenance and usage of shared instruments is the spine there; equipment management appears as a module inside Research LIMS products |
| Research Core Facility Management | service neighbor | scheduling and billing for shared research facilities; a core facility may run both — one books its instruments, the other runs its samples |
| Chromatography Data System / CDS | instrument-data neighbor | CDS acquires and processes instrument data locally; the Research LIMS orchestrates the lab-wide specimen workflow around it |

The generic-LIMS boundary is the most consequential one: the two share the same structural core, and the difference is context, posture and emphasis — research practice (configurable protocols, provenance for reproducibility, analysis/publication as the destination) versus testing-service practice (accredited test menus, specification-validated results, reports and certificates as the destination).

## Representative Products

- LabKey (Sample Manager / LabKey LIMS)
- Illumina Clarity LIMS
- SciSure LIMS (eLabNext)
- Genemod

The core model was checked across a research-native platform pole, a genomics-workflow pole, an ELN+LIMS hybrid platform pole and a lightweight academic-SaaS pole, and against academic, government-research, biotech and service-lab deployments, to avoid defining the Type by one market segment.

## Sources

Research date: **2026-09-09**

- LabKey — home, LIMS product page, Sample Manager product page, Academic Research industry page — https://www.labkey.com/ , https://www.labkey.com/products-services/lims-software/ , https://www.labkey.com/products-services/sample-management-software/ , https://www.labkey.com/industry/academic-research-software/
- Illumina — Clarity LIMS product page, Lab management software page — https://www.illumina.com/products/by-type/informatics-products/clarity-lims.html , https://www.illumina.com/products/by-type/informatics-products/lab-management-software.html
- SciSure (eLabNext) — home and LIMS page — https://www.elabnext.com/ , https://www.elabnext.com/lims
- Genemod — home page — https://www.genemod.com/

> Sourcing limitation: product help centers and user manuals were not fetched from the research environment on 2026-09-09 (documentation hosts not reached; two candidate vendors unreachable after repeated attempts and excluded from the sample). All evidence is official but drawn from product, feature and industry pages. Operational detail in this document is therefore stated only at the granularity those sources support — no numeric limits, default values or exhaustive state lists are asserted, and vendor-stated figures are excluded. Product-by-product observations and the cross-product comparison are recorded in the paired Research Notes.
