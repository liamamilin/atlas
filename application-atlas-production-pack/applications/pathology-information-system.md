# Pathology Information System

## Overview

A **Pathology Information System** is the pathology department's system of record for its diagnostic work on tissue and cell specimens. It accessions each submitted specimen as a **case** bound to an identified patient and the requesting context, drives the preparation of that case's diagnostic material — the gross examination, the tissue blocks, the microscopic slides — and completes the case when a pathologist examines the prepared material and signs out a diagnosis that becomes the patient's pathology report of record.

The problem it solves is one no general laboratory system handles well: pathology is not machine measurement. A specimen arrives as a piece of tissue with a request attached; days of technical work transform it into labeled glass slides; and the outcome is a narrative diagnosis authored by a physician who examined that material. Every step must keep the right name attached to the right piece of tissue, and the case is not finished until a pathologist puts their signature on it. Before such systems, departments ran this on an accession ledger, hand-written grossing sheets, hand-labeled cassettes and slides, dictation and typed reports — a workflow this software digitizes stage for stage.

The defining core is small: a case of record, the specimen-to-slide preparation workflow, and the pathologist's diagnosis made final at sign-out. Everything else commonly associated with modern products — barcode labeling, synoptic cancer protocols, whole-slide imaging, EMR interfacing, workload dashboards — is standard capability that mature products add, not what makes the product a pathology information system.

When the organizing unit shifts from the case to the ordered test and the outcome shifts from a signed-out diagnosis to a validated instrument result, the product is operating as a different Application Type — the Laboratory Information System (LIS).

## Users & Context

Primary users — the department's production line and its readers:

- **pathologists** — the medical core: they receive assigned cases, examine the prepared slides (through a microscope or on-screen), author the diagnosis, and sign cases out; sub-specialists handle cases routed to them by subspecialty
- **pathologists' assistants and pathologists at the grossing bench** — receive and verify specimens against requests, describe the gross specimens, and submit tissue into blocks
- **histotechnologists** — process, embed, cut and stain the tissue; the slides they produce are what the diagnosis reads from
- **cytotechnologists** — where cytology is performed, prepare and screen cell-based cases for pathologist review
- **residents and fellows** — in teaching departments, draft or preliminary-read cases under supervision

Secondary users:

- **accessioning staff** — receive incoming specimens, verify patient and requisition match, create the case and labels
- **lab managers / medical directors** — monitor turnaround, case distribution, workload balance and the department's compliance posture
- **system administrators / IT** — configure workflows, report templates, codes, users and interfaces
- **ordering clinicians** — receive the signed-out report; in hospital settings it lands in the patient's medical record, and client offices receive reports directly
- **billing staff** — in laboratories that bill for professional and technical pathology services

Typical contexts: hospital pathology departments; independent pathology groups and dermatopathology laboratories serving clinics; large reference laboratories; veterinary pathology laboratories (where the subject is an animal); and multi-site pathology networks. The work is regulated and the record is confidential patient data — clinical-laboratory quality regimes and patient-privacy discipline shape what the system must enforce and document.

## Core Model

### The Defining Core

```text
Patient / subject of record
└── Pathology case of record (accessioned; requesting context attached)
    └── Specimens / parts received and verified
        └── Prepared diagnostic material
            (gross description → blocks → slides/stains, identity carried at every step)
        └── Pathologist's interpretation of the material
            └── Diagnosis & report, final on sign-out
                └── Retained case record + retained material (blocks, slides, images)
```

Three properties. If any one is removed, the product is no longer recognizable as this Type:

- **The case of record.** Every unit of work is a persistent, individually accessioned case that binds the patient, the submitted specimen or specimens (often several parts under one case), and the requesting context. Everything the department does — every block cut, every stain run, every word dictated — attaches to the case, and the case is retained as an attributed, auditable, confidential record. Without the case, there is only a loose collection of specimens and paperwork.
- **The specimen-to-material preparation workflow.** The system exists to manage the transformation of raw tissue into diagnostic material: the gross examination is described, tissue is submitted into blocks, blocks are cut and stained into slides (or, for cell-based cases, prepared and stained). Specimen identity travels with the material at every step — labels, barcodes, chain of custody — and mismatches are intercepted rather than discovered at sign-out. This is the workflow that manufactures what the diagnosis reads from. Without it, the system is a case registry with nothing happening, or a separate tissue tracker.
- **Pathologist diagnosis authoring and sign-out.** The case completes when a pathologist examines the prepared material and authors the diagnosis. Sign-out is the act that makes the report final — a professional medical act of record, performed by name, with the case's remaining work (pending stains, recuts, special studies) resolved first. The signed-out report is the patient's pathology result; changes afterwards happen as tracked amended reports. Without this, the system is a specimen log with no medical outcome.

These properties are jointly held. A case log without preparation and diagnosis is a filing system. A preparation tracker without cases is block-and-slide logistics. A dictation tool without the case and material underneath is just word processing. The joint hold is the Type.

### Standard Capabilities of Mature Products

A typical modern product carries most of the following, with depth and packaging varying by product and market. They make the department practical; they are not what makes the product a pathology information system:

- **Case routing and worklists** — cases distributed to pathologists and stations by configurable rules (subspecialty, client, workload); role-based worklists for every stage
- **Accessioning machinery** — order/requisition receipt (electronic or scanned), patient verification, case creation, label and barcode printing for cassettes and slides
- **Identity interception** — discrepancy handling that stops a case when data and specimen do not match, before errors reach the report
- **Synoptic reporting** — structured, protocol-driven data elements for cancer and other diagnoses requiring standardized reporting
- **Coded diagnoses** — diagnosis terminology with code selection built into authoring
- **Report composition** — templates per test, client or pathologist; gross and slide images embedded; distribution to the requesting context and into the medical record
- **Interfacing** — orders received from EMRs and reports returned to them; interfaces to instruments for accompanying studies (for example molecular results posting onto the case)
- **Material retention** — tracking of stored blocks and slides so old material can be found for recuts, additional studies and prior-case comparison
- **Consultation handling** — sending slides or cases to colleagues or external specialists for second opinions
- **Operational visibility** — turnaround times, workload per pathologist, bottlenecks by stage, volume trends
- **Audit trail and roles** — every action attributed; permissions that follow the stations (grossing, histology, reading, sign-out)

One structure, many implementations:

```text
Concept:            The case
Implementations:    accession ledger entries (paper era), electronic case numbers
                    with requisition capture, cases created from EMR orders

Concept:            Specimen identity
Implementations:    hand-written labels and initials (paper era), printed
                    cassette/slide labels, barcodes scanned at each move

Concept:            Preparation tracking
Implementations:    bench worksheets and trays (paper era), electronic stage
                    worklists, station-specific queues with batch processing

Concept:            The pathologist's reading
Implementations:    microscope over glass slides (still the norm in many
                    departments), whole-slide images opened from the case
                    on screen, remote reading

Concept:            Diagnosis authoring
Implementations:    dictation and transcription (paper era), direct text entry
                    with diagnosis-code picking, structured synoptic forms

Concept:            Sign-out
Implementations:    ink signature on the typed report (paper era), electronic
                    sign-out by the named pathologist
```

A reader who has only seen a whole-slide-imaging department should still recognize a paper-hybrid laboratory running accession sheets, cassettes and a signature book from the same core.

## How It Works

The typical life of a case, as the application supports it:

### Receive and accession the specimen

```text
Specimen container arrives with a requisition (or an electronic order)
→ container verified against the request; patient identity confirmed
→ case accessioned: numbered, bound to patient and requesting context
→ parts recorded; labels/barcodes printed for container, cassettes and slides
→ mismatch (unlabeled, wrong patient, wrong container) stopped here
```

### Describe the specimen and submit tissue

```text
Grossing bench: specimen described in the record (the gross examination)
→ representative tissue submitted into cassettes → blocks
→ block labels printed and applied under the case's identity
```

### Prepare the diagnostic material

```text
Blocks processed, embedded, cut, stained
→ slide labels printed; slides matched back to the case
→ additional work (recuts, deeper levels, special stains, ancillary studies)
   requested as the case develops and tracked to completion
→ every physical move tracked; the case cannot advance with unresolved material
```

### Read and author the diagnosis

```text
Completed case appears on the pathologist's worklist
→ pathologist examines the slides (microscope, or whole-slide images
   opened directly from the case) and any prior material
→ diagnosis dictated or entered; synoptic elements completed where required
→ preliminary reads and supervised drafts possible in teaching settings
→ remaining add-on work resolved before the case can finish
```

### Sign out, distribute, retain

```text
Pathologist signs out the case — the report becomes final of record
→ report distributed to the ordering clinician / EMR / client office
→ amendments after sign-out issued as tracked amended reports
→ case, report and material (blocks, slides, or their digital images)
   retained and retrievable — the archive future cases are compared against
```

### Core vs standard vs optional

**Defining core** — without these, not this Type:

- case of record binding patient, specimens and requesting context
- preparation of the case's diagnostic material with identity carried throughout
- pathologist-authored diagnosis made final at sign-out
- retained, attributable record of the whole

**Standard capabilities** — present in most mature products:

- case routing/worklists, accessioning and label machinery, discrepancy interception, synoptic reporting, coded diagnoses, report templates and distribution, EMR/instrument interfacing, material retention and retrieval, consult handling, turnaround and workload visibility, audit trail and station-level roles

**Optional / variant** — depends on segment, region, era and digital posture:

- whole-slide imaging and remote reading, AI-assisted image analysis, integrated billing for professional/technical services, outreach client portals, multi-site networking, subspecialty packages (dermatopathology, cytology, molecular, veterinary), cancer-registry reporting interfaces

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Case worklist

The pathologist's and each station's daily surface.

- cases due by stage, priority, subspecialty and assigning rules; status of pending material
- primary actions: open a case, claim/read, return for more work, sign out

### Accessioning

Where work enters the department.

- incoming requisitions/orders, patient verification, case creation
- primary actions: accept case, verify identity, record parts, print labels, reject with reason

### Grossing station surface

The bench-side record of the specimen.

- container/requisition verification, gross description entry, cassette/submission records, block assignments
- primary actions: describe specimen, submit tissue, print cassettes, photograph specimen

### Histology tracking

The material pipeline.

- blocks and slides in process — processing, embedding, cutting, staining queues; bottleneck visibility
- primary actions: advance stage, print slide labels, record recuts/special stains, flag discrepancies

### Case view and slide viewing

The reading surface.

- the case's full history — clinical information, gross description, blocks, slides, prior cases, add-on requests; whole-slide images opened from the case where digital
- primary actions: view slides, compare priors, request additional studies, send for consult

### Diagnosis and reporting surface

Where the diagnosis becomes the report.

- dictated or typed diagnosis, diagnosis-code selection, synoptic forms for standardized reporting, report template with gross and slide images
- primary actions: author/edit diagnosis, complete synoptic elements, generate report

### Sign-out queue

The completion gate.

- cases pending signature, with unresolved work visible
- primary actions: review and sign out, hold with reason, amend a signed-out case

### Administration

- workflow and stage configuration, report templates, code and protocol libraries, users/roles per station, interface configuration

## Important Rules / Behaviors

### Sign-out completes the case

The case is not finished when the slides are cut; it is finished when the pathologist signs it out. Work blocks between material completion and sign-out — pending stains, unresolved add-on studies — keep the case open. This gate, not the technology, is what makes the report defensible.

### Specimen identity is a safety discipline

The material's identity must never detach from the case. Labels and barcodes attach identity at the bench; mismatches stop the case and route it to a person for resolution. The department's own operating rule — catch the mistake at the bench, not at sign-out — is built into the workflow.

### The material is retained evidence

Blocks and slides (or their digital images) are kept as the physical basis of the diagnosis, retrievable for recuts, additional studies, second opinions and comparison with later cases. Losing the link between a case and its material is treated as a patient-safety event, not a filing problem.

### Signed-out reports change only as amended reports

A diagnosis of record is not overwritten. Post-sign-out changes are issued as tracked amendments that preserve the prior version — the paper era's equivalent being the reissued report over the signed original.

### The report is a physician's product

Authoring and sign-out belong to named medical professionals; system users around them prepare, track and distribute. Teaching settings may route preliminary reads through trainees, but the signing pathologist carries the accountability.

### Everything that changes is logged

Case creation, part and block records, stage movements, add-on requests, diagnosis edits and sign-outs are attributed and retained. The audit trail is what inspectors and accreditors examine.

### Access follows the station

Permissions are organized around the production line — what a histotechnologist, a grossing assistant, a resident and a signing pathologist can see and do differ — and the record itself is confidential patient data governed by the applicable privacy regime.

## Variants

Common shapes of the Type:

- **private pathology group / dermatopathology LIS** — case-centric systems for physician-owned laboratories serving clinics; strong client-facing reporting and turnaround focus
- **hospital departmental pathology system** — the department inside a hospital's laboratory environment; orders and reports flow to and from the EMR; teaching workflows with resident drafts
- **pathology-dedicated multi-specialty platform** — one product family covering anatomic, cytology, hematopathology, molecular and veterinary pathology, where anatomic workflow is the anchor discipline
- **enterprise platform discipline package** — laboratory informatics vendors delivering anatomic pathology as its own discipline product alongside (not inside) their clinical-pathology product
- **digital-first department** — reading performed on whole-slide images opened from the case, with remote reading and AI-assisted analysis integrated into the case workflow; the case spine is unchanged
- **image-layer platform (adjacent)** — digital pathology platforms that manage cases, images and AI for slide review, integrating with the department's system rather than replacing the accessioning-through-sign-out spine
- **AP stages inside an LIS** — some laboratory systems carry anatomic-pathology stages as a module; classification follows the product's center of gravity
- **unified with billing** — packaging that adds professional/technical component billing to the case workflow in markets where pathology bills both sides

A variant should remain a variant, not a separate Type, unless it abandons the case spine or the sign-out act.

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| Laboratory Information System / LIS | closest sibling | the LIS organizes ordered tests on specimens and produces instrument- or method-generated results validated against ranges and returned to care; this Type organizes cases into prepared material and a signed-out physician diagnosis. Vendors hold the seam themselves — anatomic pathology ships as a separate product beside clinical pathology, and pathology-dedicated vendors distinguish themselves from general LIS products |
| Radiology Information System / RIS | family sibling | same shape (departmental workflow + report of record) for a different discipline: RIS runs imaging exams against image-producing modalities; this Type runs tissue cases against specimens |
| PACS | adjacent image layer | PACS is the image system of record — device-fed archive and diagnostic delivery. Whole-slide scanners can feed images into enterprise archives, but the case narrative, blocks/stains and sign-out live here, not there; a pathology department without digital slides still runs entirely on this Type |
| Medical Image Analysis Platform | adjacent analytical layer | those platforms derive findings from image content (algorithmic derivation is their defining act); this Type runs the case lifecycle and produces the report of record. AI-assisted analysis enters the case as evidence for the pathologist, never as the signed-out diagnosis |
| Electronic Health Record / EHR | adjacent container | the EHR holds the care record and receives the signed-out report; it does not run the case |
| Biobank Management | specimen-protocol neighbor | biobanks store specimens under protocols and may annotate them with pathology data; they do not diagnose or sign out cases |
| Hospital Management System | institutional neighbor | admissions and hospital administration; the pathology department's diagnostic operation is this Type's domain |
| Clinical Documentation Platform | note-taking neighbor | clinical notes record care encounters; the pathology report records an interpretation of prepared material under a case workflow with its own completion act |

The LIS boundary is the most consequential one, because the two share vocabulary ("laboratory", "specimen", "sign-out") and can share vendors. The structural test: re-center the record on cases with prepared material and a signed-out physician diagnosis → this Type; re-center on ordered tests with validated results returned to care → LIS.

## Representative Products

- NovoPath — pathology-dedicated LIS (anatomic, histology, digital, molecular, veterinary poles)
- Clinisys Anatomic Pathology Laboratory — anatomic pathology as a separate discipline package within an enterprise laboratory informatics platform

The digital pathology platform pole (whole-slide case review and AI hubs, e.g. products from Proscia and PathAI) was researched for boundary purposes and belongs primarily to the Medical Image Analysis Platform Type; it integrates with — rather than replaces — the case spine documented here.

The core model was checked against paper-era practice (accession ledger, hand-labeled cassettes, dictation and signed typed reports), against an open-source laboratory system carrying pathology stages, and against veterinary and cytology poles, to avoid defining the Type by one market segment or one era's technology.

## Sources

Research date: **2026-09-08**

- NovoPath — home page; Anatomic Pathology LIS; Histology LIS; Digital Pathology LIS product pages — https://www.novopath.com/ , https://www.novopath.com/solutions/anatomic-pathology-lis-software/ , https://www.novopath.com/solutions/histology-lis-software/ , https://www.novopath.com/solutions/digital-pathology-lis-software/
- Proscia — home page and Concentriq platform page — https://proscia.com/ , https://proscia.com/platform/concentriq-digital-pathology-platform
- Clinisys — Laboratory Solution overview (Anatomic Pathology Laboratory as separate discipline package) — https://www.clinisys.com/int/en/clinisys-laboratory-solution/
- PathAI — AISight positioning, as captured in the Medical Image Analysis Platform research (https://www.pathai.com/)
- OpenELIS Global — pathology workflow stages, as captured in the Laboratory Information System research (https://openelis-global.org/)

> Sourcing limitation: vendor help centers and user manuals were not reachable from the research environment on 2026-09-08; one major AP-LIS vendor's site (Xifin) returned unusable empty pages across three attempts and was abandoned. All evidence is official but drawn from product and positioning pages, not operator documentation. Operational detail in this document is therefore stated only at the granularity those sources support — no numeric limits, default values, exhaustive stage lists or exact turnaround figures are asserted. Product-by-product observations, the cross-product comparison, and the joint-review record against the Laboratory Information System research are in the paired Research Notes.
