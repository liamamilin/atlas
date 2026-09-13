# Research Notes — Pathology Information System

Research date: 2026-09-08 · Methodology: update-v1 v1.1 · Evidence layers: A = directly observed on official source, B = cross-product commonality, C = canonical inference.

## Research Goal

Understand what a Pathology Information System (PIS / AP-LIS / pathology LIS) really is as an Application Type: its core objects, the workflow it runs, who uses it, its lifecycle and rules, and — critically this pass — how it separates from the Laboratory Information System (LIS, processed 2026-09-08, joint-review flag aimed at this leaf), PACS (processed), and the Medical Image Analysis Platform (processed), all three of which left boundary watchpoints.

## Initial Boundary

Hypothesis entering research:

1. Core use: manage a pathology department's diagnostic work on tissue and cell specimens — from specimen accessioning through specimen preparation (grossing, blocks, slides) to pathologist diagnosis and signed-out report.
2. Users: pathologists, residents/fellows, pathologists' assistants, histotechnologists, cytotechnologists, lab managers, IT.
3. Nearest Types: LIS (flagged seam), PACS (digital-pathology images), Medical Image Analysis Platform (WSI AI pole held inside that Type), RIS (unprocessed radiology sibling), EHR (care record), Biobank Management (specimen annotation).
4. Likely confusion: "pathology information system" is also market vocabulary for the LIS of a pathology lab; AP-LIS is the anatomic-pathology-specific product class. Molecular/genomics is the known overlap zone (LIS pass flag).
5. Unknowns: whether the case (vs order/test) and the diagnosis/sign-out act (vs validated result) are load-bearing enough to hold the Type separate from LIS; whether digital pathology (whole-slide imaging) belongs here or in PACS/analysis-platform territory; whether billing depth is definitional.

## Research Questions

1. What is the unit of work — case? order? specimen? How does a case relate to parts, blocks, slides?
2. What workflow does the system orchestrate, stage by stage, and which roles own which stages?
3. What completes a case — what exactly is "sign-out" and why is it the terminal state?
4. What does the system hold as the record (report, images, blocks/slides, audit)?
5. How do orders arrive and reports leave (EMR/clients)?
6. Where do whole-slide images, viewers, and AI sit relative to this system?
7. What differs from a clinical-pathology LIS in structure, not just vocabulary?
8. What is the paper-era ancestor (historical check)?

## Representative Products

| Product | Class / pole | Why sampled |
|---|---|---|
| NovoPath | pathology-dedicated LIS (anatomic, molecular, veterinary, digital) — workflow-first | self-described "built specifically for pathology labs… not a module bolted onto a general-purpose LIS"; 4 official pages fetched (home, AP, histology, digital pathology) |
| Proscia Concentriq | digital-pathology platform (image-first; AP-Dx cleared for primary diagnosis) | the digital pole; boundary work vs this Type and vs Medical Image Analysis Platform |
| PathAI AISight | digital pathology platform (case/image management + AI hub) | reuse of Tier-1 evidence captured in the medical-image-analysis-platform pass |
| Clinisys (Clinisys™ Anatomic Pathology Laboratory) | enterprise platform vendor; AP as separate discipline package | joint-review evidence from the LIS side: even the #1 global LIS provider ships AP as its own product |
| OpenELIS Global (cross-pass) | open-source LIS with pathology stages | blur-zone evidence: an LIS carrying "grossing-to-sign-out" stages |

Rejected/abandoned samples: Xifin (AP-LIS + RCM vendor — site returned empty JS shells on three URLs; abandoned per network rule). Epic Beaker AP — EHR-embedded class, previously unreachable (403 ×2, recorded in LIS pass).

## Sources

- NovoPath — home (https://www.novopath.com/), Anatomic Pathology LIS (…/solutions/anatomic-pathology-lis-software/), Histology LIS (…/solutions/histology-lis-software/), Digital Pathology LIS (…/solutions/digital-pathology-lis-software/) — all fetched 2026-09-08 (A)
- Proscia — home (https://proscia.com/) and Concentriq platform page (https://proscia.com/platform/concentriq-digital-pathology-platform) — fetched 2026-09-08 (A)
- Clinisys — Laboratory Solution overview (https://www.clinisys.com/int/en/clinisys-laboratory-solution/) — fetched 2026-09-08 (A)
- PathAI — homepage + AISight positioning, captured in research/medical-image-analysis-platform.md lines 54–131 (A, that pass)
- OpenELIS Global — home + Capabilities, captured in research/laboratory-information-system-lis.md lines 55–56 (A, that pass)

Source-access limitations: Xifin official pages unreachable in usable form (three URLs returned JavaScript-empty shells). Vendor help centers / user manuals not reachable for any sampled product this pass (NovoPath support portal exists but was not fetched; no operator-level documentation captured). No numeric limits, default values, or exhaustive state lists asserted anywhere. The EHR-embedded AP-LIS packaging shape (e.g., Beaker AP class) is market-known but not directly evidenced this or the LIS pass — held as adjacent-market context only.

## Product Observations

### NovoPath (evidence layer A unless noted)

Positioning: "Most laboratory information system software was designed for high-volume, routine testing like chemistry panels, hematology, and microbiology. Pathology is a different discipline. NovoPath was built specifically for pathology labs. Anatomic. Molecular. Veterinary." — "Not a side market. Not a module bolted onto a general-purpose laboratory information system software. Pathology is the entire focus, and it has been from the beginning" (since 1993; 300+ lab implementations). This is first-hand vendor evidence for the discipline split the LIS pass predicted.

- **Case as unit of work**: "29M+ cases processed"; auto case distribution "reads each case against your rules, subspecialty, client, location, and workload, then routes it to the right pathologist's worklist the moment it's ready"; "no related cases split across three people"; workload-by-pathologist dashboards.
- **Preparation workflow** (histology page): "keeps each specimen connected to its case from accessioning through sign-out"; "Every tissue sample gets a unique code at collection that follows it through preservation, cutting, staining, examination, and storage"; implementation validates "accessioning, grossing, embedding, cutting, staining, and sign-out"; bottlenecks named "in embedding, in cutting, in staining"; label generation/printing (right label, right specimen, right time); role-based permissions per station — "Grossing stations, embedding techs, cutting stations, pathologists: each with their own access".
- **Specimen identity machinery**: specimen tracking "full chain-of-custody from accessioning to reporting"; discrepancy module — "Data and specimen mismatches flagged and resolved early, before they turn into reporting errors"; quality behavior — "When something doesn't match, NovoPath stops the case, routes it to the right person, and won't let it move until it's resolved. Mistakes get caught at the bench, not at sign-out."
- **Diagnosis authoring & sign-out**: case-study headline "Faster sign-out, focus on diagnosis"; combination codes — "pathologists combine two diagnosis codes in one action, reducing search time and clicks at sign-out"; synoptic reporting — "Structured reporting for cancer and other diagnoses that require standardized data elements. Compliance documented as you work."; customizable result reports — "Add gross and slide images, lab logos, and client-specific templates… by test, by client, or by pathologist."
- **Orders in / reports out**: electronic requisitions, patient verification, batch scanning; 100+ prebuilt EMR/instrument interfaces ("DXE connections"); interface monitoring.
- **Digital pathology pole** (as LIS-side integration): "Open digital slides directly from the case inside NovoPath… The slide and the case are the same view"; platform-agnostic viewer integrations named: PathAI AISight, Paige.ai, Hamamatsu NanoZoomer, Leica Aperio, Motic, Philips; "Every slide tied to its case from scan to sign-out"; remote case review/telepathology; "AI-Assisted Diagnosis Foundation"; secure WSI archiving indexed by case; instant subspecialty consults ("No shipping, no waiting"); workflow "slide scanning, image retrieval, case review, and results delivery"; "from slide scanning through case sign-out".
- **Physical-slide reality**: "Archive rooms fill up. Slides break. Cases get lost." — slide archival as a managed concern.
- **Money**: molecular page — "TC/PC billing splits handled natively" (technical/professional component billing, a US reference-lab/pattern-variant concern).
- **Paper ancestor (vendor-quoted customer)**: "I would hand write onto a sheet of paper, check everything against the req in the bottle, and then manually apply a sticker, manually print slides and cassettes. If I wrote down the wrong number or I forgot to send the recut at the end of the day, that would be an error." — the accessioning-to-material pipeline, identity stickers, cassette/slide labeling, recuts, all pre-software.
- **Poles beyond AP on one platform**: cytology ("GYN, Bethesda, and CLIA"), hemepath ("comprehensive reporting, flow and beyond"), clinical pathology (chemistry/hematology/urinalysis), veterinary ("species, breed, owner, and lineage data structured for vet workflows"), molecular (NGS/PCR/LDT; instrument results from Panther/Cobas post to the case; reflex triggers).

### Proscia Concentriq (A)

- AP-Dx intended-use language: "an aid to the pathologist for viewing, managing, reviewing, and interpreting digital images of scanned surgical pathology slides prepared from FFPE tissue, for the purpose of pathology primary diagnosis when used with specified interoperable components. … not intended for use with frozen sections, cytology, or non-FFPE hematopathology specimens." FDA 510(k) cleared, CE-IVDR marked.
- Pathologist work inside: "navigating tissue, orienting slides, and assembling reports"; 81% of pathologists prefer Concentriq to the microscope (vendor-claimed KLAS quote); one-day case turnaround improvement claims (vendor-claimed).
- Scope: supports "45+ scanners and every major format, including DICOM"; "native bi-directional LIS and LIMS integrations keep workflows moving and data in sync" — the platform positions itself as the image/AI layer that integrates with the LIS, not as the accessioning/reporting spine.
- Scale: customers "manage 6,000 cases an hour"; 12M cases managed annually; 230+ AI applications in its ecosystem; life-sciences pole (biomarker discovery, clinical trials, CDX deployment) — research-use realizations of the same machinery.
- Regulatory posture: AP (research) vs AP-Dx (diagnostic) split mirrors PathAI's RUO/Dx split.

### PathAI AISight (A, reused from medical-image-analysis-platform pass)

- "AISight® Digital Pathology Platform: a cloud-native, open platform enterprise workflow solution … serves as a central hub for case management, image management, and best-in-class artificial intelligence tools to enable multiple histopathology use cases."
- Regulatory split: AISight Image Management System (RUO) vs AISight Dx (FDA 510(k) cleared) for primary diagnosis.
- Boundary note from that pass: the WSI/digital-pathology pole was held INSIDE the analysis-platform Type as a specialty variant; watchpoint for this pass to apply its own remove-tests.

### Clinisys (A)

- Platform family page lists discipline content packages: Contract Services, Crop Sciences, Environmental, Food & Beverage, Public Health, Toxicology, Water Quality (LIMS side); **Clinical Pathology Laboratory** and **Genomics Laboratory** (healthcare side, available) and **Anatomic Pathology Laboratory — marked "Coming soon"** as a separate package.
- Positioning: "our single-platform solution for all pathology disciplines, including genetics"; healthcare LIS described as managing "patient data related to laboratory processes and testing for patient-specific specimens" (the LIS core per the LIS pass).
- Joint-review meaning: even a consolidated vendor selling "all pathology disciplines" from one platform structures Anatomic Pathology as its own discipline product, separate from Clinical Pathology. Confirms the LIS pass's forward flag from the vendor side.

### OpenELIS Global (A, cross-pass from LIS research)

- Capabilities page includes "stage-based pathology screens" and home page describes "pathology grossing-to-sign-out" — an open-source LIS that carries anatomic-pathology stages inside its workflow engine. Blur zone: discipline modules inside LIS products exist; classification rests on the product's center of gravity, not on the presence of AP vocabulary.

## Cross-product Comparison

| Dimension | NovoPath | Clinisys AP package | Concentriq (Proscia) | AISight (PathAI) | OpenELIS (cross-pass) |
|---|---|---|---|---|---|
| Organizing unit | case → pathologist worklist | discipline package for AP labs | "cases" managed for review (6k/hour claim) | case management hub | patient+order LIS with AP stages |
| Specimen→material preparation | accessioning→grossing→embedding→cutting→staining→sign-out (native) | implied discipline content (page not yet live) | out of scope — starts from scanned slides | out of scope — image/case hub | grossing-to-sign-out stages |
| Diagnosis & sign-out | sign-out as terminal gate; combination diagnosis codes; synoptic reporting | discipline workflow (vendor's own AP category) | report assembly inside AP-Dx review | diagnosis via AI-assisted review (Dx variant) | sign-out stage present |
| Image layer | integrated viewer access from case; 6+ WSI partners | not evidenced this pass | the product's core (45+ scanners, DICOM) | the product's core | not evidenced |
| Identity/discipline machinery | unique code per specimen; chain of custody; discrepancy stops; labels/barcodes | platform-level traceability | slide-case binding ("from scan to sign-out") | image management | patient/sample management core |
| Orders in / reports out | eRequisitions; 100+ EMR/instrument interfaces; reports by client/test/pathologist | healthcare LIS interfacing (per LIS pass) | bi-directional LIS/LIMS integration | integration into case-management environments | EMR/interfacing per LIS pass |
| Money | TC/PC billing (molecular); recovered-revenue case studies | vendor family spans outreach/RCM heritage | not positioned here | not positioned here | public-health pole |
| Regulatory posture | CLIA-class compliance documentation, audit trail | national/international regulation claims | FDA 510(k) Dx / RUO split | RUO vs Dx split | CLIA-class |
| Poles | vet, cytology, molecular, hemepath, clinical-pathology co-resident | all-pathology-disciplines platform | life-sciences research pole | biopharma research pole | national networks, One Health |

Reading: the **case-centric workflow products** (NovoPath; Clinisys's AP discipline package class; the LIS-with-AP-stages class) run the full specimen→preparation→diagnosis→report lifecycle. The **image-first digital platforms** (Concentriq, AISight) run case review and image/AI operations over scanned slides, integrate bi-directionally with LIS/LIMS, and explicitly scope themselves for "viewing, managing, reviewing, interpreting" for primary diagnosis — they do not run accessioning/grossing/block-slide manufacture. The market itself draws this seam (Proscia names LIS/LIMS as the systems it integrates with; NovoPath names viewers/ scanners as the systems it integrates with).

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately small)

Three jointly-held structures plus the record posture folded into leg 1:

1. **The pathology case of record** — a persistent, individually accessioned case binding an identified patient (or veterinary subject), the submitted specimen(s) (commonly several parts), and the requesting context; everything else in the system attaches to it; retained as an attributed, auditable, confidential record. Remove → an order tracker or an EMR note store, not a pathology department system.
2. **The specimen-to-diagnostic-material preparation workflow** — the system tracks the case's material through technical preparation into what the diagnosis reads from: gross examination descriptions, blocks, slides/sections with stains (or cytology-class preparations), with specimen identity carried at every step (labels/barcodes/chain of custody) and a technical workforce organized by station. Remove → a case registry with no material workflow, or a standalone histology tracker.
3. **Pathologist diagnosis authoring and sign-out** — the case completes when a pathologist interprets the prepared material and authors the diagnosis/report, made final by sign-out: a professional medical act of record (amendable only through tracked amended reports), not an instrument-validated result. Remove → a specimen tracker with no diagnosis, or a lab-result feed.

Joint-hold is load-bearing:
- 1 alone = case log / accession register
- 2 without 1 = histology-lab task tracker (blocks and slides unanchored to cases)
- 3 without 1+2 = dictation/template reporting tool
- 1+2 without 3 = tissue logistics with no diagnosis — the "information system" loses its medical outcome
- 1+3 without 2 = consult-note reporting over material the system never managed

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Case worklists by role and station; case distribution to pathologists by rules (subspecialty, client, location, workload)
- Accessioning with patient/order verification; electronic requisitions; batch scanning
- Label/barcode printing for cassettes and slides; discrepancy/mismatch interception before sign-out
- Gross image capture; dictation/transcription support; report templates (client/test/pathologist-specific); synoptic reporting protocols for standardized cancer data elements
- Coded diagnoses (ICD/SNOMED-class) and combination-code shortcuts
- EMR interfacing (orders in, reports out); instrument interfaces (molecular analyzers posting results to cases)
- Turnaround-time, workload and bottleneck dashboards; audit trail; role-based permissions per station
- Consult/second-opinion handling; physical block/slide storage and retrieval; recuts/deeper levels as material-level operations
- Case charges/billing linkage (incl. TC/PC splits in US reference-lab variants)

### L2 — Variant / Optional Structure

- Whole-slide imaging integration: viewer access from the case, WSI archives, remote/telepathology reads (image-centric realization of the reading step; the paper era satisfies L0 without it)
- AI-assisted analysis present as "foundation"/integration, not core (era machinery)
- Image layer ownership: integrated viewer vs platform-agnostic multi-viewer integration vs external digital platforms (Concentriq/AISight class) reached through bi-directional integration
- Clinical-pathology co-residency (pathology-dedicated vendors spanning CP), molecular/genomics modules (the LIS-flagged overlap zone), cytology/hemepath/dermatopathology/veterinary subspecialty packages
- Billing/RCM depth (unified AP-LIS+RCM products), outreach client portals, multi-site pathology networks
- Cancer-registry reporting interfaces; specimen retention policy machinery

### L3 — Vendor-specific (research notes only)

NovoPath Insights (Looker Studio dashboards), DXE "100+ connections", NovoU unified UX, "combination codes" as named feature, specific uptime/price marketing; Concentriq Fifth Generation AI layer/Compute/MCP/Aperture, "6,000 cases an hour" claims; AISight RUO/Dx naming; Clinisys content-package naming and CLS CARE assistant.

## Vendor-specific Findings

- NovoPath's own before-quote documents the paper workflow it digitized (hand-written sheets, req-in-bottle verification, stickers, manual cassette/slide printing, recuts) — rare vendor-documented ancestry, used for the historical check.
- Proscia's AP-Dx intended-use language explicitly EXCLUDES frozen sections, cytology, and non-FFPE hemepath — the cleared digital pole is narrower than the Type; the Type's canonical core must not be frozen to the FFPE-surgical slide.
- Both digital platforms split research-use vs diagnostic use of the same machinery — evidence that "diagnosis-of-record" posture, not the machinery, is what defines the clinical side.

## Boundary Findings

### vs Laboratory Information System (LIS) — JOINT REVIEW DISCHARGED (flag from LIS pass)

Keep-both RATIFIED. The two Types share the accessioned-specimen skeleton but differ in organizing structure and medical outcome, and vendors themselves hold the seam:

- **Unit of record**: LIS organizes ordered tests on specimens (order → specimen → result); PIS organizes cases (case → parts → blocks → slides → diagnosis). NovoPath's whole vocabulary is cases routed to pathologists; the LIS pass's vocabulary was orders, specimens, results.
- **Outcome**: the LIS result is captured/validated (ranges, QC gates, autoverification); the PIS outcome is a pathologist-authored diagnosis made final by sign-out — a medical professional's interpretive act, not a validated measurement.
- **Workflow center**: LIS centers the analyzer/instrument workflow; PIS centers material preparation (gross → blocks → slides) and interpretation.
- **Vendor evidence both directions**: Clinisys ships Anatomic Pathology as a separate discipline package beside Clinical Pathology (A); NovoPath explicitly claims pathology products are "not a module bolted onto a general-purpose LIS" and calls out that most LIS software was designed for routine high-volume testing (A). NovoPath itself carries a clinical-pathology solution — the co-residency is packaging on a pathology-centered platform, the reverse blur of OpenELIS carrying AP stages inside a patient/order LIS. Structural test holds: re-center on cases + diagnosis/sign-out → PIS; re-center on ordered tests + validated results returned to care → LIS. Molecular/genomics remains the overlap zone (flagged by LIS pass; NovoPath molecular module posts instrument results to cases — order-result machinery inside a case system).
- Recorded as discharged; no Boundary Issues conflict remains against the LIS pass.

### vs PACS (processed)

PACS is the imaging facility's image system of record (device-fed archive + diagnostic delivery + distribution). In digital pathology the scanner is the "modality" and WSI files can flow into PACS/enterprise imaging (PACS pass itself covers digital pathology modules). But the PIS holds the case narrative and the diagnosis-of-record machinery — parts, blocks, stains, gross descriptions, sign-out — which PACS does not; PACS stores and serves images without running the case. Remove-tests: strip the images from a PIS and it is still a PIS (paper era); strip the case/diagnosis from an image archive and it is PACS/VNA territory. Hold: keep-both; digital pathology image archives are adjacent, integration-level neighbors.

### vs Medical Image Analysis Platform (processed)

That pass holds the WSI-AI pole inside its Type and flagged this leaf. Confirmed from this side: analysis platforms DERIVE findings from image content (algorithmic derivation is their L0 leg); the PIS runs the case lifecycle and produces the report of record (case + preparation + sign-out are its legs). Where a product is primarily an image/AI hub (Concentriq, AISight), it belongs to that Type's digital pole — both vendors also present themselves as "platforms" integrating with LIS/LIMS rather than replacing the accessioning/sign-out spine. Where a product runs accessioning→sign-out and the patient's pathology report of record, it is this Type. AI in the PIS is an integration ("AI-Assisted Diagnosis Foundation"), not defining. Keep-both holds; the natural split candidate named by that pass (a standalone pathology-AI leaf) does not exist in the directory, so nothing to merge.

### vs Radiology Information System / RIS (unprocessed sibling)

Same product family shape (departmental workflow + report of record) applied to a different discipline: RIS runs imaging-exam workflows (scheduling → performance → reading → report) against DICOM-producing modalities; PIS runs tissue-case workflows (accession → preparation → interpretation → sign-out) against specimens. Distinct discipline workflow Type; low confusion risk; RIS unprocessed — no flag needed from this side beyond the note.

### vs Electronic Health Record / EHR

The signed-out pathology report flows into the patient's chart; the EHR holds the care record, the PIS holds the pathology operation of record. Same relation as LIS↔EHR per the LIS pass.

### vs Biobank Management (processed)

Biobanks annotate specimens with pathology data (e.g., tumor banks with anatomopathology/TNM annotation per that pass) — specimen-protocol custody, not case diagnosis. Adjacent; no conflict.

## Historical / Market-Sample Check (§24-style)

Ask: would older, regional, platform-native products still fit?

- **Paper era**: surgical pathology ran on an accession ledger/case log, hand-written grossing sheets, container-requirement matching ("check everything against the req in the bottle" — vendor-quoted), cassette/slide labeling by hand, worksheet trays, dictation, typed reports signed by the pathologist, and a stored block/slide archive. Case of record ✓, preparation tracking ✓, diagnosis/sign-out ✓. The L0 names none of: WSI, barcodes (L1), synoptic protocols (L1/era), billing, dashboards.
- **Platform-native variants**: AP stages inside an LIS (OpenELIS), AP as a discipline package in a platform (Clinisys), image-first digital platforms — all recognizably carrying the same three structures in whole or in the review subset.
- **Regional/animal poles**: veterinary pathology products (NovoPath vet: species/breed/owner) satisfy the core with the subject extended to animals — the subject leg is "identified patient/subject", not "human patient" (same resolution as LIS pass).
- Check passed: the L0 is era-, region-, and substrate-agnostic (FFPE tissue and cytology-class preparations both satisfy; Proscia's own FFPE-only cleared scope proves the market's digital pole is NARROWER than the Type, which is safe).

## Uncertainties

- No operator-level documentation (help centers/manuals) captured for any product; staging/state lists are inferred from vendor workflow language, not user manuals — state names deliberately not asserted in the final document.
- Xifin (AP-LIS + RCM class) not evidenced — the unified AP-LIS+RCM packaging pole is held at variant strength from market knowledge only, and is NOT asserted in the final document.
- Clinisys AP package content is "coming soon" — its workflow depth is not directly evidenced; used only as separation evidence, not as workflow evidence.
- EHR-embedded AP-LIS packaging (Epic Beaker AP class) unverified (403 ×2 in LIS pass) — mentioned as adjacent-market context only, not in the final document's claims.
- Exact consult/second-opinion and amended-report mechanics observed only at marketing granularity (NovoPath consults "no shipping"; report customization) — kept qualitative.
- Whether autopsy workflows (a third AP case class besides surgical and cytology) are first-class in sampled products is unverified — the L0's "case + material + diagnosis" frame accommodates them; no claim made.

## Final Synthesis

A Pathology Information System is the pathology department's case system of record: it accessions each submitted specimen as a case bound to patient and requesting context, drives the preparation of that case's diagnostic material (gross examination, blocks, slides/preparations — identity carried at every step), and completes the case when a pathologist examines the prepared material and signs out the diagnosis/report that flows to the requesting care context — the whole retained as an attributed, auditable record, with the material itself (blocks, slides, or their digital images) retained as retrievable evidence. Its separateness from the LIS rests on the unit (case vs ordered test), the outcome (diagnosis signed out vs result validated), and the workflow center (material preparation + interpretation vs analyzer workflow) — a seam the market itself maintains in both directions. Digital pathology does not redefine the Type: it re-implements the reading step (whole-slide images, remote reads, AI assistance) on the same case spine, while the image/AI hub products that center on scanned slides belong to the medical-image-analysis Type with which this Type integrates.
