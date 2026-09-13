# Electronic Trial Master File / eTMF

## Overview

An **Electronic Trial Master File (eTMF)** is the system of record for a clinical trial's document file: the organized collection of documents — identified in GCP practice as the trial's essential documents — that demonstrates how the trial was planned, run, and overseen. Where a CTMS manages the conduct of the trial and an EDC manages its data, the eTMF manages its documentary record: every essential document is held as a record anchored to the trial, filed into a defined trial-document structure, tracked against what is expected, and kept inspection-ready until the trial is closed and archived.

The defining core is small:

```text
Clinical trial (study anchor, commonly scoped to countries and sites)
└── Trial-document index (where each document belongs)
    └── Expected-vs-filed completeness tracking (what should exist vs what has been filed)
        └── Document records with version state (current vs superseded, attributed and dated)
```

Everything else commonly associated with eTMF products — reference-model pre-configuration, email-based document intake, quality-control workflows, completeness dashboards, electronic-signature and audit-trail machinery, inspector access, and long-term archiving — is standard capability that mature products carry, not what makes them eTMFs. The same discipline existed for decades as paper files with index tabs, and later as shared drives with index trackers; those satisfy the same core without any of the modern machinery.

## Users & Context

Primary users:

- **Sponsor study teams / clinical operations** — own the trial and its file; review completeness and health, decide what "expected" means for their study, and answer for inspection readiness.
- **TMF / document managers** — run the file day to day: intake, indexing, filing, quality control, chasing gaps.
- **CRO teams** — in outsourced trials the CRO often operates the file on the sponsor's behalf; sponsor oversight of a CRO-held file is a first-class concern.
- **Sites (investigator sites)** — contribute site-generated documents (approvals, training records, logs); in many products they contribute without holding full system accounts.
- **Quality / audit and regulatory staff** — run periodic file reviews and prepare for inspections.
- **Inspectors and auditors** — read-only users during health-authority inspections or sponsor audits; several products provide dedicated, access-scoped inspector modes.

The context is a regulated, multi-party workflow: documents originate at sites, CROs, vendors, and the sponsor's own departments; the file spans the whole trial lifecycle from startup through closeout and, in many deployments, many years of post-trial retention.

## Core Model

### The defining structures

**Trial-scoped document record.** The unit of record is a document with metadata, belonging to one specific trial. Records anchor to the study, and in practice scope downward to country and site — because most trial documents exist per country (regulatory approvals) or per site (investigator credentials, site logs). A record carries identity (what it is), attribution (who filed it, when), and version state.

**Trial-document index.** Documents are filed into a defined structure — the "master file" organization. In current practice the structure commonly aligns with the industry-standard TMF Reference Model (now maintained by CDISC as the TMF Standard Model), which organizes content into zones, sections, and numbered artifacts; a trial's specific filing expectations are typically recorded in a TMF plan or document index. The index is what turns a pile of trial documents into a *file*: every document has a place where it belongs.

**Expected-vs-filed completeness.** The index is not just a folder tree — it expresses which documents the trial *should* have. Products operationalize this as placeholders or required-document lists created at study setup, then track received versus expected in real time. Completeness is the file's central managed property: dashboards and views surface missing documents at trial, country, site, and document level, and work is organized around closing gaps.

**Document-of-record integrity.** A filed document is the record, not a working copy. Current and superseded versions are distinguished and retained; changes and activity are attributable; the file must remain retrievable and trustworthy into the archive phase. Modern products implement this with electronic audit trails and e-signatures aligned to 21 CFR Part 11 / EU Annex 11; the underlying expectation — an attributable, versioned record — predates any of that machinery.

### Standard capabilities of mature products

- **Reference-model structures** — pre-configured document inventories aligned to the TMF Reference Model, auto-generated per study, adaptable to study-specific needs.
- **Intake machinery** — upload (commonly drag-and-drop), email-to-TMF inboxes where site documents land in a staging area for indexing, scanner integration for paper, and auto-filing based on document naming conventions.
- **Filing and QC workflow** — documents move from intake through indexing/metadata capture to quality review and filed status; rejections carry reasons; issues are tracked as queries to remediation. Configurable workflows route a document "from upload to inspection readiness."
- **TMF health metrics** — the industry frames file health in three dimensions: completeness, quality, and timeliness. Dashboards trend all three, with drill-down to root causes and configurable thresholds; heatmap-style risk views appear in some products.
- **Amendment and event awareness** — study changes such as protocol amendments update what documents are expected; reviews can be regular, risk-based, or milestone-driven.
- **GxP access and security** — role-based access for internal teams, CROs, and external partners; audit trails over all document activity; Part 11-capable electronic signatures; validated deployment with vendor validation packages.
- **Inspection support** — dedicated or scoped inspector access, navigation inspectors can learn quickly, and export/reporting that documents the file's state.
- **Closeout and archive** — long-term retention (often measured in years to decades), searchable archived file with metadata and audit trail preserved, and structured TMF transfer between organizations (an industry Exchange Mechanism Standard exists for moving a TMF with its metadata and audit-trail information).

### One structure, many implementations

```text
Concept:   Trial-document index
Realized as:  TMF Reference Model zone/section/artifact inventory, TMF plan + document index, trial-defined file plan

Concept:   Expected documents
Realized as:  placeholders, required-document lists, auto-planned document inventories from study setup

Concept:   Intake
Realized as:  direct upload, email-to-TMF inbox with staging, site-system exchange, scanner capture

Concept:   Record integrity
Realized as:  Part 11 audit trail + e-signatures, versioning with superseded retention, validated archive
```

## How It Works

### Set up the trial's file

```text
Create the study in the system
→ scope it to countries and sites
→ establish the filing structure (reference-model inventory and/or trial-specific TMF plan)
→ set templates and naming conventions
→ generate the expected-document inventory (placeholders / required-document lists)
→ assign roles and permissions for sponsor, CRO, and site participants
```

Setup captures what is unique about the trial — its parameters and document requirements — while enforcing filing standards. The generated inventory is the yardstick against which the whole file is thereafter measured.

### Move documents into the file

```text
Documents arrive (upload, email to a study inbox, site systems, scanners)
→ land in a staging/intake area if unfiled
→ team or automation indexes them: document type, metadata, trial/country/site placement
→ quality review (risk-based, sampled, or full)
→ filed at the correct index position, or rejected with a reason back to the sender
→ issues tracked as queries until remediated
```

Sites frequently participate without system accounts: they email documents to study-specific inboxes, or upload against placeholders created for them. Naming conventions can drive auto-filing; AI-assisted filing suggestions exist at one pole of the market.

### Keep the file complete and inspection-ready

```text
Completeness views compare received vs expected, continuously
→ missing documents surface at trial / country / site / document level
→ owners are assigned and chased; queries track remediation
→ quality metrics (rejections, misfiles, timeliness) accumulate
→ study events (amendments, milestones) update what is expected
→ periodic reviews confirm the file's readiness posture
```

This loop is the application's working heartbeat. The output — a file that can be shown to an inspector at any time — is the product's core promise, and inspection-readiness reporting is a standard deliverable.

### Hand over the record

```text
Trial closes
→ file is completed/reconciled
→ retained in long-term archive (searchable, access-controlled, audit trail preserved)
→ and/or transferred between organizations in a structured exchange format
→ inspectors and auditors retrieve documents from the archive years later
```

In outsourced models the CRO typically hands the completed file to the sponsor at closeout; sponsor-side archive products exist precisely for this retention phase.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Completeness / health dashboard

- **Purpose:** the file's live status — the surface managers check daily.
- **Typical information:** completeness percentages and gaps, QC queues, timeliness trends, quality metrics, drill-down by study, country, site, and document type; heatmap-style risk views at the mature pole.
- **Primary actions:** drill into a gap, assign ownership, open the underlying documents, export a report.

### File navigator (index tree + search)

- **Purpose:** browse the trial-document structure and locate any filed document.
- **Typical information:** the index (zones/sections/artifacts or the trial's plan) populated with filed documents and empty placeholder positions; per-document metadata and version state.
- **Primary actions:** open a document, file a document onto a placeholder, replace/supersede a version, inspect a document's audit trail.

### Document workspace (record view)

- **Purpose:** work on one document record.
- **Typical information:** metadata (type, dates, owner, country/site scope), version list (current/superseded), workflow state, review history, linked queries.
- **Primary actions:** upload new version, route for review/signature, reject with reason, raise a query, view audit trail.

### Intake / staging queue

- **Purpose:** process incoming documents that are not yet filed.
- **Typical information:** batch of emailed or uploaded documents, suggested filing targets, sender.
- **Primary actions:** index and file, auto-file by naming convention, return to sender.

### Inspector view

- **Purpose:** give inspectors scoped, usable access during an inspection.
- **Typical information:** the same index and documents, filtered to the inspection scope; read-only.
- **Primary actions:** navigate, search, open and export documents; access is itself traced.

### Archive

- **Purpose:** retain and retrieve the closed trial's file.
- **Typical information:** archived structure with metadata, retention schedule, access history.
- **Primary actions:** search/retrieve, grant scoped access, export.

## Important Rules / Behaviors

### Completeness is a standing property, not a report

The expected-document inventory makes "what is missing" always computable. Trial documents do not merely accumulate; they are tracked against expectations that are themselves updated by study events. A file that simply holds documents — without expected-vs-filed tracking — is not functioning as a TMF system.

### The current version is the file; prior versions are retained

Filing a new version supersedes, and does not silently overwrite. Superseded versions remain retrievable with their attribution, because the file may need to show what was true at any point in the trial's history.

### Access is party- and scope-aware

Sponsors, CROs, vendors, and sites see scoped slices of the same file; permissions distinguish internal and external participants, and inspector access is granted and traced per inspection. In outsourced trials, sponsor oversight of a CRO-operated file is a supported posture rather than an exception.

### Records are attributable and traceable

All document activity is logged (filed, changed, viewed, signed), electronic signatures are uniquely attributable to records, and validation of the system is an expected deployment artifact. This is the vendor-documented norm across the sampled market, aligned to 21 CFR Part 11 and EU Annex 11.

### The file has a long tail

Retention obligations commonly run years to decades after closeout, and archiving is a distinct phase with its own requirements — integrity preservation, controlled retrieval, and inspection support long after active work has stopped.

## Variants

- **Purpose-built eTMF specialists** — vendors dedicated wholly to TMF practice, with embedded industry best practices and TMF-professional services around the software.
- **Clinical-suite modules** — eTMF as one product inside a life-sciences suite alongside CTMS, EDC, RTSM, RIM, and QMS; deeper cross-module integration, lighter standalone identity.
- **Trial-operations platform members** — eTMF as the sponsor-side document core of a platform that also carries site-side eISF/eBinder products and site–sponsor document exchange.
- **Site-side file products (eISF/eBinders)** — the same file-management machinery applied to the investigator site's own file; a closely adjacent surface with its own industry reference model, often integrated with sponsor TMFs.
- **Archive-only deployments** — products purpose-built for the post-closeout retention phase, used when a sponsor receives a completed file from a CRO and needs decades of secure, searchable, inspection-ready retention rather than active filing machinery.
- **CRO-held file with sponsor oversight** — the file operated by the CRO, observed by the sponsor; read-only "viewing" archive products exist for the handover of CRO-run files.
- **Deployment and regional spread** — cloud SaaS and on-premises; US Part 11 and EU Annex 11 postures; regional regulator guidance contexts (e.g., EMA and MHRA TMF guidance); medical-device flavor oriented to approval pathways.

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| Clinical Trial Management System / CTMS | adjacent, integrated | manages the conduct of the trial (sites, milestones, monitoring, budgets); eTMF manages its document file; vendors ship both separately, and one suite vendor embeds only basic trial-entity registers in its eTMF while pointing to its CTMS for operations |
| Electronic Data Capture / EDC | adjacent, integrated | holds the trial's captured data values; eTMF holds its documents — same trial, different unit of record |
| Regulatory Information Management / RIM | sibling regulated-document system | RIM manages submission dossiers, registrations, and health-authority correspondence at product level; eTMF manages trial-conduct documents at trial level |
| Life Sciences QMS | sibling regulated-document system | QMS holds the organization's quality-system records (SOPs, CAPA, training); eTMF holds one trial's essential documents |
| Enterprise Content Management | structural look-alike | generic, organization-wide content management; lacks the trial anchor, the trial-document index, and expected-vs-filed completeness — the eTMF market explicitly defines itself against this |
| Enterprise Records Management | adjacent | generic retention/records schedules; eTMF's retention and archive machinery is specific to the trial file and its inspection lifecycle |
| Clinical Trial Site Management | adjacent, site operations | site business operations (payments, visits, recruitment); the site's document file (eISF) is the eTMF-like record, commonly a separate product |

The sharpest seam is with CTMS, because both are trial-scoped systems used by the same study teams and are increasingly integrated or co-purchased. The structural test: CTMS's objects are the trial's operations (who, where, when, how much); the eTMF's object is the document record filed in the trial's index with completeness machinery. Removing the index and completeness tracking from an eTMF leaves a document store; removing the document unit from an eTMF and keeping the operations leaves a CTMS.

## Representative Products

- Montrium eTMF Connect — TMF-specialist pole for scaling sponsors and CROs
- Phlexglobal PhlexTMF (Enterprise / Express / Viewing / CROs / MedTech) — purpose-built TMF specialist with TMF services arm
- Ennov eTMF and Ennov eTMF Archive — clinical-suite module pole; archive as a distinct product
- Florence eTMF (with eBinders/eISF and SiteLink) — site-first platform pole

The core model was checked across these four poles and against the pre-digital practice the industry itself documents (paper TMFs and the CDISC TMF Standard Model's explicit paper adaptation), so the definition does not depend on any single era, vendor pattern, or regulatory regime.

## Sources

Research date: **2026-09-07**

- Montrium — eTMF Connect product and FAQ pages: https://montrium.com/etmf-connect , https://montrium.com/
- Phlexglobal — PhlexTMF software pages: https://www.phlexglobal.com/etmf-software , https://www.phlexglobal.com/
- Ennov — eTMF and eTMF Archive product pages and FAQs: https://en.ennov.com/solutions/clinical/ennov-etmf/ , https://en.ennov.com/solutions/clinical/ennov-tmf-archive/
- Florence Healthcare — platform and eTMF product pages: https://www.florencehc.com/products/etmf/ , https://florencehc.com/
- CDISC — Trial Master File Standard (TMF Standard Model, formerly TMF Reference Model): https://www.cdisc.org/tmf ; community forum site: https://tmfrefmodel.com/

> Sourcing limitation: vendor help-center/support documentation was not reachable (login-gated support portals; the widely used enterprise product Veeva Vault eTMF could not be fetched from the research environment at all). Observations are therefore drawn from official product and FAQ pages, and the industry-standard body's own site. Precise operational details (exact state names, numeric limits, default settings, workflow step counts) are intentionally not stated here; finer product-specific detail is retained in the Research Notes.
