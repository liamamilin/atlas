# Research Notes — Radiology Information System / RIS

Research date: 2026-09-09
Slug: `radiology-information-system-ris`
Directory leaf: Radiology Information System / RIS (Section 22 Healthcare & Life Sciences)

---

## Research Goal

Understand what a Radiology Information System (RIS) actually is as an Application Type — its defining core, its exam/order lifecycle, its division of labor with PACS / EHR / billing systems, who uses it and on what surfaces, which rules and states matter, and where its boundaries with neighboring Types run — based on official product documentation of representative vendors, not on generic industry descriptions.

## Initial Boundary (working hypothesis before research)

- RIS = the radiology department's administrative-clinical workflow system of record: imaging exams are ordered, scheduled on imaging resources, performed and tracked, reported, and (region-dependent) billed.
- Nearest neighbors: PACS (image store/viewing), LIS (same pattern for laboratory), EHR (hospital-wide record and orders), Practice Management System (generic visit scheduling + billing), Patient Scheduling (generic appointment booking), Medical Image Analysis Platform (AI on images).
- Expected boundary seam: RIS holds the *exam workflow and report state*; PACS holds the *images*; the EHR holds the *patient's whole record* and often the *order entry*.

## Research Questions

1. What is the central object (exam/order/study) and what does it carry (patient, procedure code, modality, status)?
2. What is the exam lifecycle, and are statuses fixed or configurable?
3. How does imaging scheduling differ from generic appointment scheduling (resources = modality/room/technologist/radiologist; exam-type durations; double-booking guards)?
4. How do RIS, PACS, modality devices, and the EHR/HIS divide the work (order intake, modality worklist, image/exam linkage, report distribution)?
5. Who uses the RIS and on which surfaces (scheduler/front desk, technologist, radiologist worklist, manager/BI, portals)?
6. Which rules matter (insurance verification/prior auth, AUC/decision support, safety/prep, report status discipline, quality feedback)?
7. Which capabilities are definitional vs common vs variant (billing, patient portal, dose monitoring, mammography tracking, teleradiology, AI)?

## Representative Products

Selected for market representativeness, different product philosophies, and different customer tiers:

| Product | Vendor | Pole in the sample |
|---|---|---|
| PowerServer RIS/PACS + OmegaAI (RIS/PACS/VNA) + Blume + Stana | RamSoft | Cloud/cloud-native mid-market RIS/PACS; imaging centers + teleradiology groups |
| Exa RIS (+ Exa PACS, Exa Billing, Exa Clear) | Konica Minolta Healthcare | Standalone-capable RIS lineage for imaging centers; scheduling/registration/billing depth |
| Radiology imaging (IDS7 worklists, Reporting, DoseTrack) | Sectra | Enterprise-imaging PACS-centric pole (Europe/US hospitals); reading workflow + reporting |

Rejected/abandoned samples: Novarad (site unreachable ×2), GE HealthCare Centricity RIS (404), Siemens syngo Workflow (404 ×2), Infinitt (403), Epic Radiology (403). See Sources → access limitations.

## Sources

Fetched 2026-09-09 (Tier 2 official product pages unless noted):

- RamSoft — https://www.ramsoft.com/ (root: product family, who-we-serve)
- RamSoft — https://www.ramsoft.com/solutions/products/powerserver (PowerServer RIS/PACS)
- RamSoft — https://www.ramsoft.com/solutions/products/omegaai (OmegaAI RIS/PACS/VNA)
- RamSoft — https://www.ramsoft.com/who-we-serve/by-industry/teleradiology (teleradiology variant)
- RamSoft — https://www.ramsoft.com/conformance (conformance statements index: DICOM/HL7/IHE PDFs listed)
- Konica Minolta Healthcare — https://healthcare.konicaminolta.us/healthcare-it/exa-ris (Exa RIS)
- Konica Minolta Healthcare — https://healthcare.konicaminolta.us/healthcare-it/exa-pacsris (Exa PACS|RIS)
- Sectra — https://medical.sectra.com/ (root)
- Sectra — https://medical.sectra.com/solutionarea/radiology-imaging/ (Radiology imaging solution)

### Source-access limitations

- Vendor help centers / user manuals (Tier 1) were not publicly reachable for any sampled product (RamSoft support portal requires login; Konica Minolta "Product Manuals" resource area not fetched; Sectra customer login required). All evidence below is from official marketing/product pages (Tier 2) plus one conformance-statement index page.
- The RamSoft "IHE Statement — PowerServer RIS-PACS" PDF exists at a public URL but returned unparseable binary; its *existence and title* are used as evidence that the vendor publishes IHE conformance statements for the RIS/PACS product; its *content* was not read.
- No hospital-incumbent RIS (GE/Siemens/Epic-class) official page could be fetched. Claims about the hospital-enterprise pole are therefore weakened and mostly rest on RamSoft's own hospital-segment page ("integrates with your HIS, EMR, and billing systems") plus general cross-product reasoning. Precise hospital-RIS workflow details (order entry from CPOE, HIS-driven scheduling) are NOT asserted in the final document.
- No numeric limits, default settings, or exact status names are asserted anywhere in the final document; exact status labels are explicitly described as configurable per product/facility.

---

## Product A — RamSoft (PowerServer / OmegaAI / Blume / Stana)

### Key observations (evidence layer A = directly observed on official pages)

- **Positioning**: "AI-powered cloud-based RIS/PACS solutions for imaging centers, hospitals, and teleradiology groups worldwide since 1994." PowerServer described as "A cloud-based radiology platform… from intake to final report"; "unifies scheduling, image management, reporting, and workflow automation."
- **Product family as packaging**: PowerServer RIS/PACS / PowerServer PACS / PowerServer TELE PLUS (teleradiology) / PowerServer LITE PACS; OmegaAI = cloud-native RIS/PACS/VNA; Blume = patient engagement portal; Stana = mammography tracking; DICOM routing products. RIS, PACS, VNA, patient portal, and specialty tracking are separately named modules of one platform.
- **Unified worklist**: "a singular worklist that consolidates patient data from multiple sources, customizable to suit the workflow needs of any imaging environment"; "Access all imaging studies across multiple facilities from one consolidated, single-login interface"; "real-time updates and intelligent auto-routing." OmegaAI "True Universal Worklist": "One worklist for every role — filter, assign, merge, and act on studies in real time… smart routing, prior auth indicators, and one-click report access built in."
- **Study lifecycle automation**: OmegaAI Workflow Designer & Automation (WFA): "scriptable, trigger-based automation that eliminates manual routing, escalations, and status updates across the entire study lifecycle"; "Auto-route studies, escalate findings, and update statuses — hands-free"; "Trigger workflows from any event, at any stage of the study lifecycle."
- **Order intake**: OmegaAI AI-driven OCR: "Turn inbound faxes into orders automatically, removing a persistent front desk bottleneck." Blume: "automated intake forms, SMS notifications, self-scheduling, and AI Order Processor."
- **Reporting**: OmegaAI AI-Powered Reporting: "integrated voice dictation and AI-generated report drafts… Move from read to signed report with fewer interruptions." (Report lifecycle endpoint = signed report.)
- **Patient-facing**: Blume gives "patients secure, on-demand access to their imaging studies, reports, and health records"; "Automated intake, reminders, and notifications reduce no-shows."
- **Referrer-facing**: RapidResults "provides physicians with easy access to studies… Securely access current and prior reports"; secure study sharing via QR codes/links "keeping patients, referring physicians, and care teams aligned."
- **Integration**: "Connects effortlessly to EMR/HIS and third-party systems via HL7®, DICOM, and IHE profiles" (PowerServer); OmegaAI "built on HL7® FHIR® R4, DICOMweb, and open APIs"; OmegaAI LINK: "Bidirectional image routing and worklist support" (worklist connectivity toward sites/modalities without VPN).
- **Hospital segment**: "Enterprise RIS/PACS/VNA that integrates with your HIS, EMR, and billing systems from day one."
- **Teleradiology variant**: "orchestrates your distributed radiologist workforce — automating workflows and integrating AI so you hit turnaround targets across every client and location"; "Automated workflows triage and prioritize readings and reports"; collaboration (chats/screen-share/alerts triggered by "critical findings or study status changes"); per-study pricing.
- **Mammography tracking (Stana)**: "Automatically captures BI-RADS™ scores, breast density, and follow-up recommendations"; "Automates patient reminders, outcome tracking, and next-order creation"; "embedding FDA MQSA compliance directly into your PowerServer workflow."
- **Operational analytics**: Essence BI "Built-in turnaround time, referrer, and study analysis"; OmegaAI Root BI "Prebuilt turnaround metrics… TAT, throughput, and operational performance."
- **Standards**: conformance page lists DICOM Conformance, HL7 Conformance, IHE Statement — PowerServer RIS/PACS, FHIR Capability Statement, FDA 510(k) clearances, HIPAA/SOC 2/ISO 13485.

## Product B — Konica Minolta Exa RIS (+ Exa PACS|RIS, Exa Clear)

### Key observations (layer A)

- **Positioning/packaging**: "Exa® RIS is available as an integrated solution with Exa PACS and Exa Billing or standalone." Exa PACS|RIS = "integrated, single database solution designed natively together with a single source of truth that eliminates data duplication, status changes are updated instantly and an improved user experience with single login and single workflow."
- **Resource-based scheduling**: "Intelligent, resource based scheduling"; "Input appointments by patient, calendar or resource (modality, physician, procedure) and view the first available time slot." "Resource scheduling is based on availability of Technologist to perform or Radiologist to interpret specific exams." "With Secure Scheduling the RIS software will notify if a resource is double booked and not allow a patient to double book on multiple resources at the same time." "Easily reschedule patients without re-entering exam and CPT information." Multi-facility: "Schedule appointments by region and market… centralized scheduling."
- **Scheduler color-coding tied to insurance verification time**: "The color-coded scheduler is designed to alert schedulers of time concerns for insurance verification."
- **Registration**: "Intuitive Patient Registration notifies and suggests a merge when registering duplicate patient fields."
- **Configurable status workflow**: Custom Workflow Design Engine: "The order of operations for an imaging study varies drastically from business to business. Build your workflow based on your facility needs. Choose from the drag and drop status options to design your preferred imaging workflow. The ability to define the entire process step-by-step…" — statuses are facility-configurable; the exam advances through them.
- **Insurance/financial machinery at scheduling (Exa Clear)**: "Real-time pre-authorization, eligibility verification and patient payment estimation built into the scheduling process"; "Automated prior-authorization built into the pre-authorization process"; "Real-time health plan eligibility verification at the point-of-care"; "Calculate patients' charges against contracted rates with national and regional payers."
- **Patient kiosk**: self check-in; "view and update demographic and insurance information as well as complete and sign electronic forms."
- **Portals**: referring physician portal (zero-footprint images+reports, no VPN); patient portal (pre-appointment forms, images, reports); attorney portal with scoped access to "Study/order status, Exams, Schedules, Reports, DICOM Studies."
- **Order appropriateness (AUC)**: LogicNets partnership: "Realtime evaluation of patient scenario either validating that an order is appropriate or recommending appropriate alternatives"; "AUC code provided with order"; "integrated with your scheduling workflow"; ordering physicians access AUC tools from the physician portal.
- **Exam + code vocabulary**: rescheduling "without re-entering exam and CPT information" implies the order/exam carries procedure and billing codes.

## Product C — Sectra (Radiology imaging / IDS7 / Reporting / DoseTrack)

### Key observations (layer A, with a scope limitation)

- **Positioning**: enterprise imaging platform; radiology solution "Built on a reliable PACS, VNA, and strong interoperability, it streamlines daily radiology work." Vendor claims "170 million annual imaging exams" managed; "250,000+ daily users."
- **Users named**: "Radiologists, technologists, and administrators—we've got you covered"; referrers get "universal viewer embedded in the EMR… access to images and reports."
- **Reading worklist machinery (IDS7)**: "built-in workflow orchestration to keep cases organized, highlight what is most important"; worklists carry "Seat-based case distribution, Color indicators and sortable columns, SLA information and reading physician, Quick filters and worklist groups; Dynamic, static, or meeting specific content."
- **Reporting**: Sectra Reporting add-on — "native, structured reporting… Through the same interface as the images"; report links from lesion-tracking tools ("Insert lesion measurements into reports with a single click").
- **Quality feedback loop**: "a closed communication loop mechanism that allows feedback from supervisor to technologist. Ensuring diagnostic quality over time." (Radiologist→technologist feedback on image quality.)
- **Dose monitoring**: Sectra DoseTrack — "keeping track of radiation doses and collect data for future improvements" (add-on module).
- **Modality breadth**: "Vendor-neutral modality interfaces; CT, MRI, ultrasound—you name it, we support it."
- **Scope limitation**: Sectra's public site does not expose RIS-side scheduling/ordering/registration pages (the vendor positions everything as "enterprise imaging"). Sectra is therefore used as evidence for the reading-worklist/reporting/quality side of the Type, not for the scheduling side. This is recorded as a research limitation, not as evidence that Sectra lacks those functions.

---

## Cross-product Comparison

| Dimension | RamSoft | Konica Minolta Exa | Sectra | Evidence layer |
|---|---|---|---|---|
| Exam/order as central record with status | "entire study lifecycle" statuses; attorney-visible "study/order status" (via RamSoft-class portals) | exam record with configurable drag-and-drop statuses; "study/order status" in attorney portal | worklist cases with SLA info and reading physician | B (all three) |
| Statuses configurable per facility | WFA: trigger-based status updates, configurable workflows | explicit "choose from drag and drop status options" | worklist groups/filters configurable | B |
| Resource-based scheduling (modality/technologist/radiologist) | AI Scheduling product; Blume self-scheduling | explicit: resources = modality, physician, procedure; double-booking guard | not publicly documented | A (Exa) + A (RamSoft partial) |
| Patient registration / intake | Blume automated intake forms | registration with duplicate-merge suggestion; kiosk self check-in | not publicly documented | B (2 of 3) |
| Order intake from referrers | fax→order via AI OCR; AI Order Processor | AUC evaluation attached to order; physician portal | not publicly documented | A (RamSoft), A (Exa) |
| Insurance verification / prior auth at scheduling | "prior auth indicators" on worklist | Exa Clear: real-time eligibility + prior auth + payment estimation | not documented | B (2 of 3, US-market products) |
| Reading worklist per radiologist | True Universal Worklist (filter/assign/merge) | — (PACS-side worklist implied) | seat-based distribution, SLA, reading physician | B (all three) |
| Report lifecycle to signed/final report | "read to signed report", dictation + AI drafts | reports in portals (final artifacts) | native structured reporting in same interface | B (all three) |
| Report/image distribution to referrers & patients | RapidResults, QR/link sharing, Blume | physician/patient/attorney portals | universal viewer embedded in EMR | B (all three) |
| HL7/DICOM/IHE integration spine | HL7, DICOM, IHE, FHIR R4, DICOMweb; conformance statements published | single-database PACS|RIS; portals; (integration pages exist) | vendor-neutral modality interfaces; EMR embedding | B (all three) |
| Billing/charge machinery | hospital page: integrates with billing systems; AI coding claims | Exa Billing separate product; CPT codes on exam; payment estimation | not documented | B (2 of 3; region-dependent) |
| Teleradiology mode | TELE PLUS; distributed workforce orchestration; per-study pricing | — | — | A (RamSoft only) → variant |
| Mammography outcome tracking | Stana (BI-RADS, MQSA) | Exa RIS(MG) video exists (depth not fetched) | breast imaging PACS (viewing-side) | A (RamSoft) → specialty variant |
| Dose monitoring | — | — | DoseTrack add-on | A (Sectra only) → optional |
| Quality feedback loop (radiologist→technologist) | chats/alerts on status changes | — | explicit closed feedback loop | A (Sectra), A (RamSoft partial) |
| Operational BI (TAT, referrer analysis) | Essence BI / Root BI | Quinsite analytics partnership (press release) | — | B (2 of 3) |

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

Three jointly-held structures. Remove any one and the product stops being a RIS:

1. **The imaging exam as the unit of record.** A persistent, individually identified record of one requested imaging procedure for a specific patient, carrying the department's procedure vocabulary (exam type, modality, and where applicable billing codes) and a workflow status. The exam record is the anchor to which scheduling, performance documentation, images, report, and charges attach. *Remove → generic appointment scheduling or a plain image archive (PACS).*
2. **The department's exam-status workflow machinery.** The exam advances through a sequence of statuses (requested/ordered → scheduled → arrived/performed → reported → distributed) that is the department's shared coordination state; each status transition is driven by a role-specific work surface (scheduler's book, technologist's exam screen, radiologist's reading worklist). Statuses are facility-configurable, but the existence of a status-tracked exam lifecycle is invariant. *Remove → order-entry tool or a bare worklist with no memory.*
3. **The report lifecycle of record.** The exam's interpretation is tracked through drafting/dictation to a signed/final report, and the report (with its status) is distributed to referrers and made visible to stakeholders. *Remove → image management without results; the "I" in RIS collapses.*

Jointly load-bearing: (1 alone = scheduling/billing tool; 2 without 1 = status board over nothing; 3 without 1+2 = dictation system; 1+2 without 3 = exam logistics without results; 1+3 without 2 = archive with no live workflow).

### L1 — Common Mature Structure (very common, not definitional)

- Resource-based scheduling of exams on imaging capacity (modality/room/technologist/radiologist slots, exam-type durations, double-booking guards, rescheduling) — the canonical intake surface in patient-facing deployments.
- Patient registration/demographics with duplicate detection/merge; patient check-in (desk or kiosk).
- Role worklists: reading worklist for radiologists (prioritization, assignment, SLA/turnaround indicators); technologist exam lists.
- Modality connectivity: worklist delivery to devices and image/exam linkage (DICOM/HL7/IHE integration spine; conformance statements).
- Referrer and patient access to images/reports (portals, zero-footprint viewers, EMR embedding).
- Operational analytics: turnaround time, referrer, study-volume analysis.
- Order intake machinery from referring physicians (electronic orders, fax-to-order conversion).
- Quality feedback loops between readers and technologists.

### L2 — Variant / Optional Structure

- Billing/charge capture and revenue-cycle linkage (separate product in some vendors; region-dependent — in single-payer or provincial-billing regimes the loop runs without US claim machinery).
- Insurance eligibility / prior authorization / patient cost estimation at scheduling (US-market-specific).
- Order-appropriateness decision support (AUC) attached to the ordering workflow.
- Teleradiology operation: distributed reading workforce, multi-client study intake, per-study economics; patient scheduling may be replaced by reading-work orchestration.
- Specialty tracking: mammography outcome tracking (BI-RADS-class scoring, recall/follow-up loops, regulatory compliance reporting).
- Radiation dose monitoring.
- Patient self-scheduling, reminders, kiosk check-in.
- AI overlays: AI report drafting, triage/prioritization, coding automation.
- Deployment: on-premises vs cloud-hosted vs cloud-native SaaS; standalone RIS vs integrated RIS/PACS single-database vs EHR-embedded radiology module.

### L3 — Vendor-specific (research notes only)

- Named modules: Blume, Stana, OmegaAI LINK, WFA, Root BI, Essence BI, RapidResults, Gateway Router/Viewer (RamSoft); Exa Clear, Exa Patient Kiosk, Exa Billing, RIS(MG) (Konica Minolta); IDS7, UniView, Amplifier, DoseTrack (Sectra).
- Vendor marketing metrics (uptime %, coding accuracy %, benchmark speedups, exam volumes managed).
- Per-study pricing model (RamSoft teleradiology page).
- LogicNets AUC partnership (Konica Minolta).

## Vendor-specific / Rejected Findings

- **Rejected as definitional**: billing/charge capture (Exa ships it as a separate product; region-dependent), insurance verification (US-specific), AI anything (all vendor-specific overlays), dose monitoring (single-vendor add-on in sample), mammography tracking (specialty variant), patient portal (common but not defining — a RIS without a portal is still a RIS), cloud delivery (on-prem poles exist).
- **Rejected as definitional**: "single database RIS/PACS" (Exa's architecture claim) — an integration architecture, not a property of the Type; standalone RIS with separate PACS remains in-type.
- **Rejected**: exact status-name sequences as industry standard — Exa explicitly documents that the order of operations "varies drastically from business to business" and statuses are drag-and-drop configurable; therefore the final document describes conceptual lifecycle phases, not canonical labels.

## Boundary Findings

- **vs PACS**: PACS acquires, stores, and displays images; RIS runs the exam workflow and report state. In integrated RIS/PACS products the seam is internal (single database, "status changes updated instantly"), but conceptually: remove exam workflow/report tracking from an integrated suite → PACS + viewer; remove image storage/viewing → standalone RIS (still a RIS — Exa RIS is sold standalone). The reading worklist and report status belong to the RIS side even when the PACS vendor ships them.
- **vs LIS**: same structural pattern (order → scheduled/collected → performed → resulted → distributed) applied to specimens instead of imaging exams; different vocabulary (tests vs procedures), different resources (bench/instruments vs modality rooms), different result object (lab result vs imaging report). Separate Types.
- **vs EHR / Hospital Management System**: the EHR holds the whole-patient record and (in hospital deployments) often originates the imaging order and receives the final report. A hospital RIS is a department-level system that exchanges orders/results with the EHR/HIS (HL7-class integration). When the EHR vendor ships a radiology module that performs scheduling + exam tracking + report workflow inside the EHR, the standalone RIS is absorbed — an EHR-embedded variant of the same functions, not a new Type. (Taxonomy observation recorded below.)
- **vs Practice Management System**: PM runs generic visit scheduling + billing for an ambulatory practice; RIS carries imaging-procedure semantics — modality resources, procedure/protocol vocabulary, exam-status machinery, report lifecycle. The Exa RIS + Exa Billing split shows the seam: scheduling/registration/workflow = RIS; money movement = billing product.
- **vs Patient Scheduling (generic)**: generic appointment booking lacks modality-resource semantics, exam-type durations/preparation, and the downstream exam lifecycle. Remove the imaging-resource and procedure vocabulary → generic scheduling territory.
- **vs Medical Image Analysis Platform**: that Type's object is the image (AI analysis of image content); RIS's object is the exam workflow. AI triage inside a RIS reorders worklists; it does not become an analysis platform.
- **"去掉什么就变成另一个 Type" 判据**: remove the exam-status workflow + report lifecycle → PACS/image archive; remove imaging procedure/modality semantics → generic scheduling/PM; remove the department scope (whole-patient record) → EHR; remove patient-facing scheduling entirely and keep multi-client reading orchestration → teleradiology workflow platform (variant, not separate Type — same exam/report objects).

## Taxonomy observation (for STATUS Boundary Issues)

- The market increasingly sells RIS only as part of "RIS/PACS" bundles or "enterprise imaging" platforms; standalone RIS persists mainly in imaging-center/teleradiology segments. The directory's separate leaves (RIS, PACS, Medical Image Analysis Platform) remain justified, but the RIS document should explicitly describe the integrated-suite packaging as the dominant market form so readers do not imagine RIS as always-standalone.
- EHR-embedded radiology (Epic-class) is a real deployment form that the sampled sources could not document directly (Epic 403). Recorded as an uncertainty, not resolved here.

## Uncertainties

1. Hospital-incumbent RIS behavior (CPOE-originated orders, HIS-driven scheduling, bed/transport coordination) could not be verified from official sources; the final document deliberately avoids precise claims about hospital-order entry mechanics.
2. Whether technologist-side documentation (tech notes, contrast/safety screening, protocol selection) is universally structured in modern RIS could not be confirmed from fetched pages (no sampled page detailed the technologist exam screen's fields). The final document mentions technologist exam documentation only generically.
3. Exact report-status vocabularies (preliminary/addendum/corrected) are industry-familiar but were not directly evidenced in fetched pages; the final document says report states "vary by product" and only asserts the signed/final endpoint (evidenced by RamSoft "read to signed report").
4. Sectra's RIS-side scheduling/ordering functions: not publicly documented; no claim made either way.
5. DICOM Modality Worklist as a named standard service: supported indirectly (RamSoft LINK "worklist support", IHE conformance statement existence, Sectra "vendor-neutral modality interfaces") but the specific DICOM service name was not read from a primary standard document; the final document describes the capability, not the standard's internals.

## Final Synthesis

A RIS is the radiology department's system of record for its exam workflow. Its defining core is three jointly-held structures: the imaging exam as a persistent identified unit of record (patient + procedure/modality vocabulary + status); the exam-status workflow machinery that coordinates the department's roles through configurable statuses; and the report lifecycle of record that carries each exam's interpretation to a signed result distributed to referrers. Around that core, mature products add resource-based scheduling, registration/check-in, role worklists, modality connectivity, referrer/patient access, and operational analytics; billing, insurance machinery, AUC decision support, teleradiology operation, specialty tracking, dose monitoring, and AI are variant/optional layers that depend on segment, geography, and regulation. The Type's identity survives both the standalone-RIS form (Exa) and the integrated RIS/PACS or enterprise-imaging form (RamSoft, Sectra); what kills the identity is removing the exam workflow or the report lifecycle (→ PACS/viewer) or the imaging-procedure semantics (→ generic scheduling/PM).
