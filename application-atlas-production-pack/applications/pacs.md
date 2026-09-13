# PACS

## Overview

A **PACS** (Picture Archiving and Communication System) is a medical-imaging facility's system of record for its images. It receives images directly from the imaging devices that produce them — CT, MRI, ultrasound, X-ray, mammography, PET and similar modalities — holds every patient's exams as a persistent, structured archive, and serves those studies to the people who use them: radiologists reading at diagnostic workstations, referring clinicians viewing results through lighter viewers, and increasingly patients through portals and share links.

Three properties define the Type:

```text
Imaging modality (CT, MR, US, CR/DX, PET …)
  └─ pushes each study as it is acquired, carrying patient/exam metadata
      └─ Study archive of record (patient → study → series → image)
          └─ Diagnostic-grade delivery (reading worklist + diagnostic viewer)
              └─ Clinical distribution (web viewers, portals, share/export)
```

- **Acquisition-device ingest** — images enter the system straight from the modalities at acquisition time, not by later import. Each device is configured with the PACS as its send destination.
- **The study archive of record** — the archive is the facility's authoritative, retained copy of what was acquired, bound to identified patients and organized per exam. The "A" in the name is load-bearing: without persistent archiving, the product is a viewer or a relay, not this Type.
- **Diagnostic-grade delivery** — the archive exists to be read: radiologists open studies from a reading worklist in full diagnostic viewers, and studies flow onward to clinicians and patients through accessible viewing surfaces. An archive nobody reads from is storage, not a communication system.

If the system receives only imported or exchanged files (no device link), it is an archive/VNA-style store. If it streams images without retaining them, it is a relay. If it stores and serves but nothing diagnostic reads from it, it is an appliance. The defining core is the three together.

DICOM — the medical imaging interchange standard — is the universal current realization of both the device link and the study format in today's market, but the Type is defined by the function (device-fed, patient-bound, archived, delivered), not by the protocol. The definition also does not assume radiology: cardiology, breast imaging, digital pathology and ophthalmology all run the same core, and veterinary imaging products satisfy it as well.

## Users & Context

**Primary users:**

- **Radiologist** — the main reader: works through a reading worklist, opens studies in a diagnostic viewer, compares with prior exams, and produces (or triggers) the report. Remote and after-hours reading is a normal mode in many deployments.
- **Radiographer / technologist** — performs the exam on the modality and hands the study into the system; commonly performs the first image quality and completeness check before the study enters the record.
- **Referring clinician** — consumes results: opens the patient's studies and reports from a portal, a web viewer, or an embedded view inside the medical record system.

**Secondary users:**

- **PACS / imaging IT administrator** — registers devices, maintains routing rules and user access, monitors storage and integrations, handles anonymization/export requests.
- **Patient** — an increasingly common direct consumer of images and reports through portals or share links.
- **Specialist readers** — cardiologists, pathologists, orthopaedic surgeons and others where the deployment covers multiple specialties.

Typical contexts: hospital radiology departments (the origin and still the dominant context), freestanding imaging centers, teleradiology groups reading for many facilities, and small clinics with one or two devices. The system is clinical infrastructure relied on around the clock — uninterrupted availability is a primary product concern, with vendors committing to continuous technical support and high-uptime guarantees.

## Core Model

### The study hierarchy

The PACS world is organized around a four-level hierarchy — the structure the DICOM standard itself calls its "model of the real world," and which every sampled product preserves:

```text
Patient
  └─ Study (one imaging exam / order context)
      └─ Series (one acquisition: a single X-ray image, a CT volume, an ultrasound cine loop, a derived reconstruction …)
          └─ Image / instance (one file: pixel data plus its embedded metadata)
```

- **Patient** — the person (or animal, in veterinary deployments) whose exams accumulate over years. The patient record carries identity and demographics.
- **Study** — the unit of clinical work and of reading: one exam, typically performed against one order or visit context. Studies are indexed by attributes such as patient, date, modality type, description, and an exam identifier (the accession number).
- **Series** — one coherent acquisition or reconstruction inside the exam. A CT study contains several series (scout, axial slices, reconstructions); a PET-CT study contains at least the PET and CT series. A series may be a single 2D image, a 3D volume, a cine loop, or even a stored report document.
- **Image/instance** — the smallest stored unit: pixel data plus embedded metadata (patient name/ID, study and series identifiers, acquisition parameters, modality type). The metadata travels inside every image file, which is what lets studies be verified, routed, and safely matched to patients wherever they move.

Uniqueness of identifiers is part of the safety model: study and series identifiers are globally unique so that images from different devices and hospitals can never be confused; patient identifiers are unique within a facility.

### The archive of record

The archive holds studies as the facility's authoritative copy: recent work sits on fast storage for immediate reading, and studies move to long-term archive behind it as they age, remaining retrievable for years. Archives are kept redundant, and migrations between storage generations are a routine administrative operation. The archive is also the source of **priors** — the earlier studies of the same patient that a radiologist compares against the current exam.

### Moving images

Studies move through configured routes: modalities send to the PACS; the PACS forwards, pre-fetches, and exchanges studies with other systems and facilities according to rules (by modality, destination, facility, or reading group) and on request (query/retrieve). In today's market these movements are almost universally carried by DICOM services (store, query, retrieve) or their web-age equivalent (DICOMweb), with a device-connector component bridging older devices to cloud deployments.

### One structure, many implementations

```text
Concept:              device → archive ingest
Implementations:      DICOM store services from the modality directly; a connector component bridging devices to a cloud archive; DICOMweb uploads

Concept:              persistent archive
Implementations:      on-premises server storage; cloud object storage; hybrid (local short-term storage archiving into cloud long-term storage)

Concept:              diagnostic viewer
Implementations:      dedicated workstation application; zero-footprint browser viewer; embedded viewer inside the medical record system
```

A reader who has only seen one shape (for example, a hospital on-premises PACS) should still recognize a small clinic's browser-based cloud PACS, or an open-source image server, from this model.

## How It Works

### From acquisition to archive

```text
Exam scheduled (where a scheduling system exists)
→ modality pulls its scheduled-patient worklist
→ technologist performs the exam on the modality
→ modality stamps each image with patient/exam metadata and sends the study to the PACS
→ study received, verified for completeness and image quality (technologist QC)
→ routing rules distribute it (reading groups, locations, backup destinations)
→ study enters the archive of record
```

The device link is configured once per device: the administrator registers the PACS address on the modality (and the device on the PACS), tests the connection, and from then on the modality sends studies automatically after every acquisition. No manual export, no removable media.

A well-documented exception path: in emergency imaging the patient may be imaged before any registration exists. The study is still acquired and archived under a temporary/exam identifier, and the patient identity is reconciled into the study afterwards once administrative information is available — the metadata, not the pixels, is what gets corrected.

### The reading loop

```text
Radiologist opens the reading worklist (prioritized; status indicators)
→ opens the next study in the diagnostic viewer
→ a display protocol arranges the series into a layout suited to the exam type
→ window/level adjustment, zoom, measurement, annotation while reading
→ pulls prior studies of the same patient for comparison
→ report is created (in the integrated reporting tool or the department's reporting/RIS system) and linked to the study
→ study status advances; the report becomes available to referrers
```

The viewer's adjustment tools are presentation-layer: windowing, zooming and annotating change how the image is displayed and what measurements are recorded, not what was acquired. Display protocols (layout presets per modality, exam type, role) are configured system-wide so every reader starts from a consistent arrangement.

### Distribution to the point of care

```text
Study completes reading; report linked
→ referring clinician opens the study from the medical record system link, portal, or web viewer
→ sees images (often with prior comparisons) and the report
→ optionally shares onward: secure links, exports, or media that replace burned CDs
→ patient accesses own images/reports where a portal or share-link feature exists
```

### The archive over time

Studies age from fast short-term storage into long-term archive. Old studies are not dead data: the reading loop retrieves them as priors, and the archive satisfies retention obligations. Retrieval from long-term tiers happens on demand; how quickly differs by product and deployment.

### Capabilities by tier

**Defining core** — without these, not a PACS:

- direct ingest from acquisition devices with patient/exam metadata
- persistent per-patient study archive (patient → study → series → image) as the record
- diagnostic-grade delivery to readers (worklist + viewer) and onward distribution

**Standard capabilities** — present in nearly all mature products:

- reading worklist with prioritization; display/hanging protocols
- routing rules, pre-fetching, query/retrieve between systems
- prior-study retrieval for comparison
- ingest-time image quality and completeness checks
- web/zero-footprint clinical viewers; report linkage; EMR/scheduling integration
- archive tiering with redundancy; role-based access with audit trails
- DICOM (and increasingly DICOMweb) as the interchange layer; non-DICOM content (photos, videos, PDFs) attached alongside

**Optional / variant** — depends on segment and deployment:

- patient portals, teleradiology packaging, integrated reporting/dictation, AI applications, 3D advanced visualization, teaching/research libraries, multi-specialty enterprise scope, cloud vs on-premises deployment

## Interfaces

### Reading worklist

The reader's entry surface. Typically shows: patient, exam type, modality, arrival time, status, priority/turnaround indicators, and assignment. Primary actions: open a study, filter/sort, prioritize, assign or reassign (in group reading).

### Diagnostic viewer

The core clinical workspace. Shows the study's series arranged by a display protocol, with tools to window/level, zoom, rotate, measure, annotate, navigate series side-by-side, compare with priors, and (where provided) launch MPR/3D or third-party/AI tools. Usually paired with an information panel holding the worklist, patient data, orders and report views, so reading and reporting happen in one place.

### Image quality check surface

A simplified view used by technologists (or in the reading flow) to verify that a study is complete and technically acceptable before it enters the record — focused review of single images or short series.

### Clinical / referrer viewer

A lighter viewing surface for referring clinicians: open current (and earlier) studies and reports from a browser or an embedded view in the medical record system; share or export where permitted. Often zero-footprint (browser-based, nothing to install).

### Patient-facing surface (where offered)

Portal or share-link access letting patients open their own images and reports, commonly as part of the facility's patient engagement features rather than the PACS core.

### Administration console

The operator's surface: registered devices (each with its network identity), routing rules and destinations, user accounts and roles, storage/archive status, integrations, and audit logs. Device registration and connection testing happen here — the step that binds modalities to the archive.

### Sharing / export

Mechanisms for moving studies out of the facility's control deliberately: secure share links, export to media or files (the modern replacement for burned patient CDs), and interfaces for exchange with other institutions.

## Important Rules / Behaviors

- **The archived study is a medical record.** What the modality produced is retained as acquired; the archive — not a workstation's local copy — is the authoritative version. Display adjustments never alter stored pixel data, and products strongly prefer lossless handling of image data to avoid any loss of diagnostic information.
- **Metadata correctness is a safety property.** Every image carries the patient/exam identity it was acquired with; mismatched metadata means the wrong study read on the wrong patient. Hence device-side stamping, completeness checks at ingest, and a reconciliation path for studies acquired before the patient was registered.
- **Access is identity-controlled and audited.** Viewing patient imaging is restricted to authorized roles; access is logged (often to a defined audit standard); emergency access is handled through controlled override mechanisms ("break the glass") that are themselves recorded. Privacy-regime compliance (HIPAA/GDPR-class postures) is a standing product concern, including where data physically resides in cloud deployments.
- **Reports and images are linked but not necessarily co-owned.** The report text may be created in the PACS, in a separate reporting/RIS system, or by dictation — but the association between study and report is maintained and surfaced together at the point of reading.
- **Distribution follows rules, not habit.** Where studies are sent, pre-fetched, or exposed is governed by configured routing rules and role-based visibility — a deliberate control surface, since a misrouted study is a privacy event.
- **The archive serves the past, continuously.** Priors comparison is a normal part of reading, which is why retention, integrity and retrieval — not just capacity — are the archive's core obligations. Deletion is a governed, exceptional act; some cloud products explicitly warn that user-initiated deletion is unrecoverable and recommend an independent backup.

## Variants

- **Deployment shape** — on-premises (traditional hospital), cloud (storage and viewing hosted by the vendor), and hybrid (local short-term storage archiving into cloud long-term storage). The cloud shape is now a mainstream offering for imaging centers and hospitals alike.
- **Scale ladder** — single-device or small-practice PACS → imaging-center PACS → full RIS/PACS suites → enterprise imaging platforms. Vendors commonly sell an explicit upgrade path between these.
- **Department scope** — radiology-first deployments vs multi-specialty enterprise imaging on one platform (cardiology, breast imaging, digital pathology, ophthalmology, orthopaedic planning), including capture of non-DICOM media into the same archive.
- **Teleradiology packaging** — editions and features aimed at distributed reading workforces: cloud-based reading worklists, remote full-performance viewing, cross-site image exchange.
- **Archive pairing** — the archive embedded in the PACS vs a standalone vendor-neutral archive product alongside it (the enterprise-imaging convergence; see Related Types).
- **Reading audience** — radiologist-centric vs clinically broad deployments where most users are referrers.
- **Subject breadth** — human patients dominant; veterinary and dental/CBCT deployments run the same core.
- **Regulatory posture** — products are regulated medical devices in most markets (e.g., diagnostic viewers carrying medical-device certification), with certification specifics varying by product and market.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Radiology Information System / RIS | interlocking sibling | the department's administrative/workflow system of record — scheduling, orders, registration, report text; the PACS is the image system of record. "RIS/PACS" suites bundle both; the seam is images vs workflow |
| Medical Image Analysis Platform | adjacent (computation) | computes on images (detection, quantification, planning) and returns derived results; integrates into PACS viewers but holds no acquisition link or archive of record |
| Electronic Health Record / EHR | adjacent (care record) | holds the longitudinal care record; imaging is custodied in the PACS and surfaced through EMR-embedded viewers and links |
| Health Information Exchange / HIE | adjacent (cross-organization) | moves records and images between organizations; the PACS is the intra-facility archive that feeds such exchange |
| Vendor Neutral Archive / enterprise imaging archive | boundary-blur neighbor | holds multi-department, multi-vendor archives without owning device ingest or diagnostic reading; modern enterprise platforms bundle both, but the functions remain distinct |
| Media Asset Management / MAM | different world | archives media assets for creative/broadcast work; lacks the patient/exam binding, medical metadata and clinical custody of diagnostic studies |
| Standalone DICOM viewer | below the Type | a delivery surface with no archive of record and no device ingest |

## Representative Products

- **Orthanc** — open-source standalone DICOM server: the minimal realization of the core (device ingest, indexed archive, query/retrieve, web viewing) with none of the department machinery; also the best-documented window into how the device interface and study hierarchy actually work.
- **RamSoft PowerServer** — cloud-based RIS/PACS suite for imaging centers and teleradiology groups, with an edition ladder from small-practice PACS to full RIS/PACS.
- **Intelerad IntelePACS** — reading-workflow-focused PACS for radiology groups and hospitals, sold alongside separate worklist-orchestration and archive products.
- **Sectra IDS7 / Sectra Enterprise Imaging** — security-focused enterprise platform whose radiology PACS extends across imaging specialties; documented three-window viewer and hybrid STS/LTS archive.
- **PostDICOM** — browser-based cloud PACS for small practices and clinics: device connector, zero-footprint diagnostic viewer, share links.

The defining core was checked against the minimal open-source shape and the historical film-less department pattern (device-fed archive + diagnostic reading, no cloud/AI/VNA machinery) so that the definition does not over-fit the current enterprise-cloud market.

## Sources

Research date: **2026-09-08**

- Orthanc Book — official documentation (https://book.orthanc-server.com/), incl. "Connect your modality to Orthanc" and "Understanding DICOM with Orthanc"
- RamSoft — https://www.ramsoft.com/ and PowerServer product page (https://www.ramsoft.com/solutions/products/powerserver)
- Intelerad — https://www.intelerad.com/ and IntelePACS product page (https://www.intelerad.com/en/all-products/intelepacs/)
- Sectra Medical — https://medical.sectra.com/ , IDS7 product page (https://medical.sectra.com/product/sectra-ids7/), One Cloud Storage page (https://medical.sectra.com/product/sectra-one-cloud-storage/)
- PostDICOM — https://www.postdicom.com/ (product pages and public operational FAQ)

> Sourcing limitation: no commercial product's operator manual / help center was reachable from the research environment on 2026-09-08; evidence comes from official product pages, technical documentation (Orthanc), and public operational FAQs (PostDICOM). Precise operational facts (retention periods, exact status lists, retrieval latencies, certification numbers, vendor performance figures) are intentionally not stated in this document; where relevant they remain in the Research Notes.
