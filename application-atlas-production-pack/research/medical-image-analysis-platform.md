# Research Notes — Medical Image Analysis Platform

Research date: 2026-09-08

## Research Goal

Understand what a Medical Image Analysis Platform actually is as an Application Type: what exists inside it, who uses it, how analysis flows from image acquisition to clinical action, what states and rules matter, and where its boundaries lie against PACS, RIS, Clinical Decision Support Systems, advanced visualization tools, and general ML platforms.

## Initial Boundary

Tentative understanding before research:

- Core use: software that computes findings, measurements, or quantifications from medical images and delivers them into clinical workflow.
- Users: radiologists, pathologists, cardiologists, other imaging specialists; downstream treating clinicians.
- Nearest neighbors: PACS (archive/distribute/display), Radiology Information System (workflow management), Clinical Decision Support System (knowledge→advice), advanced visualization workstations (display/processing), general ML/data-labeling platforms (training tooling).
- Likely confusions: "platform" marketing (multi-algorithm orchestration) vs single-analysis products; care-coordination add-ons (Viz.ai-style) drifting toward a different Type; report-mining follow-up modules drifting toward care-management territory.
- Unknowns: whether multi-algorithm orchestration is definitional; whether regulatory clearance is definitional; whether digital pathology (whole-slide imaging) belongs to this Type or a separate one; exact operational mechanics (alert acknowledgment, result states) — help centers mostly gated.

## Research Questions

1. What is the analytical input — how do images enter the platform, and in what form (DICOM studies, whole-slide scans)?
2. What does the platform compute — detections, segmentations, quantifications, derived physiological parameters?
3. How are results bound to the patient/exam, and what result states exist (flagged, negative, confirmed, refuted)?
4. How do results reach clinicians — worklist reprioritization, in-viewer overlays, mobile notifications, standalone consoles?
5. Who consumes results — radiologist at read time, or downstream specialists at care time?
6. How does the platform integrate with PACS / RIS / EHR, and is integration part of the Type or an implementation detail?
7. What role does regulatory clearance (FDA/CE) play — definitional or market posture?
8. Is multi-algorithm orchestration ("platform") definitional, or a common enterprise structure?
9. What monitoring/governance machinery exists (usage analytics, performance dashboards, model updates)?
10. Where does this Type end and PACS / CDSS / care coordination / research ML platforms begin?

## Representative Products

Selected for market representation, documentation reachability, different product philosophies, and different customer tiers:

| Product | Philosophy | Segment / Tier |
|---|---|---|
| Aidoc | enterprise multi-algorithm triage & notification platform (aiOS) | large hospitals / health systems, acute radiology |
| Viz.ai | detection + specialist care coordination (mobile-first) | stroke/vascular/cardiology networks |
| Lunit (INSIGHT) | screening & detection for high-volume imaging, partner-integrated | imaging centers / screening programs, international (Korea) |
| Heartflow | single deep quantification — image-derived physiological parameter (FFRCT) | cardiology, CCTA programs |
| PathAI (AISight) | digital pathology platform: image/case management + AI algorithms (own + partner) | anatomic pathology labs, academic centers; biopharma research pole |

Paige (paige.ai) was originally sampled for the pathology pole but returned HTTP 403; PathAI (which also hosts Paige algorithms as partner products) was substituted and fetched successfully.

## Sources

All fetched 2026-09-08 (Tier 2 official product surfaces; Tier 1 help centers mostly gated — see Sourcing Limitation):

- Aidoc — platform page: https://www.aidoc.com/platform/ ; radiology solution page: https://www.aidoc.com/solutions/radiology/
- Viz.ai — platform page: https://www.viz.ai/platform/ ; Viz LVO product page: https://www.viz.ai/neuro/large-vessel-occlusion
- Lunit — radiology/partner page: https://www.lunit.io/en/products/radiology (redirects to https://www.lunit.io/en/radiology-technology-partners/) ; INSIGHT CXR product page: https://www.lunit.io/en/ai-radiology-software/insight-cxr/
- Heartflow — homepage: https://www.heartflow.com/ ; FFRCT Analysis page: https://www.heartflow.com/heartflow-one/ffrct-analysis/
- PathAI — homepage: https://www.pathai.com/
- Sibling pass (boundary input): applications/clinical-decision-support-system.md (2026-09-07)

Not fetched (gated or not attempted within budget): Viz.ai Help Center (help.viz.ai), Lunit Product Documentation page, Aidoc product-information library, PathAI AISight subpages, FDA 510(k) database entries.

## Product Observations

### Aidoc (evidence layer A unless noted)

From https://www.aidoc.com/platform/ and https://www.aidoc.com/solutions/radiology/:

- Positioning: "Enterprise Clinical AI Platform"; aiOS™ described as "a unified artificial intelligence operating system that fits within an existing IT stack, runs effectively in any clinical setting and orchestrates numerous AI applications at once."
- Radiology solution: "AI triage algorithms alert on suspected acute findings. Quantification algorithms automate repetitive tasks." "Detection algorithms increase disease awareness."
- Integration: "integrating deeply with your EHR, PACS, Scheduling and Reporting systems"; "custom configuration with minimal IT lift"; implementation time "two to three weeks" (vendor claim — L3).
- The Widget: "consolidating results from various algorithms, including those from our strategic partners, into a single, unified interface"; "Runs on any workstation"; "Provides key images and summary of AI medical imaging results"; "Tightly integrated with PACS, including AI triage results marked directly in worklist"; "Facilitates chat with downstream care team members' mobile devices."
- Result visibility: "View results of every algorithm run, both with and without AI findings"; "A quick glance of the Widget shows the Radiologist which pathologies to confirm" — negative results are surfaced, and the radiologist confirms.
- Algorithm catalog by pathology: intracranial hemorrhage, LVO, PE, rib fracture, pneumothorax, aortic dissection, appendicitis, etc. — mix of own and partner algorithms (Icometrix, Imbio, Riverain, Us2.ai, ScreenPoint, Gleamer, ChestView named on page).
- Care Coordination module: "multidisciplinary care teams always on, real-time notification of time-sensitive cases with image and data sharing capability between desktop and mobile workflows... integrates EHR data and scheduling systems."
- Patient Management module: "leverages the power of AI to mine radiology reports for confirmed findings and ensures they are routed to the appropriate teams for follow-up based on facility-specific protocol" — NOTE: this mines report text, not images; drift toward follow-up/care management territory (boundary observation).
- Regulatory: "Largest portfolio of FDA-cleared algorithms running on a single platform"; "FDA-cleared and CE/UKCA-marked algorithms."
- Clinical evidence posture: "More than 220 studies"; specific metrics (41% TAT reduction, 96.2% sensitivity) are vendor-claimed study results — kept out of canonical claims.

### Viz.ai (evidence layer A unless noted)

From https://www.viz.ai/platform/ and https://www.viz.ai/neuro/large-vessel-occlusion:

- Platform: "the Viz.ai platform delivers auto-detection of disease and critical insights to the entire care team"; "Trusted by more than 1,400 hospitals" (vendor claim).
- Viz Orchestrator: "Uses AI to automatically route the right algorithm on the right image at the right time"; "Helps to catch incidental findings and prioritize urgent patients."
- Integration: "Seamless integrations with PACS, worklist, and EHR"; "Vendor agnostic HL7 and FHIR integrations"; "Integrations with Epic, Cerner, Meditech"; cloud delivery ("no on-prem hardware or maintenance required").
- Viz LVO: "auto-detects suspected large vessel occlusions within seconds of image acquisition"; "90% of alerts are reviewed by the intended specialist within 5 minutes" (vendor claim).
- Specialist consumption (customer quotes): "makes imaging viewable right on my phone and allows me to not only confirm the occlusion, but simultaneously evaluate the rest of anatomy... I am planning the case and communicating that plan to my team well before the patient is on the table"; "Viz alerts my team to all potential LVOs in our network and allows me to quickly view them on my phone."
- Network coordination: "enables HIPAA-compliant image review, care plan discussions, and streamlined transfer decisions across primary and comprehensive stroke centers."
- Viz 3D CTA: "AI-Enhanced 3D Imaging — removing bone and venous noise"; "Automates 3D processing" — image processing/visualization extension.
- Suites span neuro, vascular, cardio, pulmonary, trauma, oncology, radiology; HCM detection extends to ECG (non-image physiological signal) — boundary observation: analysis substrate can extend beyond images.
- Regulatory: Viz LVO De Novo clearance DEN170073 cited on product page.
- Help Center exists (help.viz.ai) and EU user guides page — not fetched (budget).

### Lunit (evidence layer A unless noted)

From https://www.lunit.io/en/radiology-technology-partners/ and https://www.lunit.io/en/ai-radiology-software/insight-cxr/:

- Positioning: "AI Radiology Platform"; "we work with leading imaging manufacturers, PACS/RIS vendors, and digital health platforms to deliver AI-powered radiology solutions that fit seamlessly into real-world clinical workflows."
- Partner ecosystem: AGFA, Fujifilm, GE Healthcare, Philips, Samsung, Infinitt, Microsoft, Merative, etc. — distribution through imaging/PACS vendors (channel variant).
- Regulatory: "FDA-cleared, CE-certified under MDR, and deployed in more than 65 countries."
- INSIGHT CXR: "highlights 11 major thoracic abnormalities... compares priors, and supports earlier diagnosis"; "AI-integrated worklists"; "intelligent normal case reporting."
- DualScan System: "combines two chest AI engines—one for abnormality detection and one for flagging normal cases" — detection + normal flagging (triage in the negative direction: streamline normals).
- Normal Flagging: "identifies high confidence normal cases–streamlining workflow... allows radiologists to focus on abnormal and high-risk cases."
- Prior comparison: "Automatically surface changes in findings with current-prior comparison tools. Including automated nodule progression and tracking for pneumothorax, pleural effusion, and consolidation."
- Deployment FAQ: "On premise, where all data is analyzed on the client's infrastructure and servers, or on Cloud, with only a component of the software with the function to anonymize data and route to Lunit's AI Engine on Azure"; "a local DICOM Gateway strips identifying details before transmission."
- Model update posture: "No, the AI does not learn live. Our images are sourced from data providers based on clear collaboration agreements. Software versions are carefully monitored... Images from commercial sites are retained only for the period required for image analysis."
- INSIGHT Manager (monitoring console, "a non-medical device"): "Application Monitoring: task status, processing time, component uptime"; "Performance Lab: sensitivity, specificity... how thresholds impact AI analysis"; "Analysis Trends Monitoring: distributions and trends in AI outputs."
- Precision Oncology (Lunit SCOPE): pathology-slide AI for biomarker scoring (PD-L1, HER2, uIHC) — same vendor spanning radiology and pathology poles.
- Breast ecosystem extends beyond image analysis: density assessment, risk pathways, quality analytics, patient hub — drift toward screening-program management (boundary observation).

### Heartflow (evidence layer A unless noted)

From https://www.heartflow.com/ and https://www.heartflow.com/heartflow-one/ffrct-analysis/:

- Positioning: "Our first-of-its-kind AI analysis creates a detailed 3D model of the heart" from a coronary CTA (CCTA) scan.
- Heartflow One platform analyses: Roadmap Analysis ("Efficiently read every CCTA with consistent results across readers... early detection of CAD"), FFRCT Analysis ("Assess blood flow anywhere in the coronary tree"), Plaque Analysis ("Quantify and characterize plaque"), Plaque Staging, PCI Navigator (intervention planning).
- FFRCT substrate: "leveraging advanced computational fluid dynamics and deep learning algorithms... combines anatomy and lesion-specific physiology."
- How it works (product page): "1. Patient-specific, interactive, 3D anatomical and physiological reconstruction; 2. Rapid assessment of blood flow anywhere in the coronary tree, with color-coding to indicate values; 3. Evaluate multiple and sequential lesions... for a targeted interventional approach"; "Pins can be placed anywhere along the coronary tree; FFRCT values are specified distal to modeled stenoses."
- Turnaround: "90 minutes (median) from CCTA scan to guideline-directed pathway" (vendor claim) — asynchronous batch analysis, not real-time triage.
- Advisory posture (footer disclaimer): "The information provided by Heartflow Analysis is intended to be used in conjunction with the patient's clinical history, symptoms, and other diagnostic data, as well as the clinician's professional judgement."
- Delivery: cloud platform (login at app.heartflow.net); results consumed by cardiologists; >1,800 institutions (vendor claim).
- Commercial context: reimbursement resources, CPT category one codes — payer machinery attached (L2/L3).
- Regulatory: ISO 13485 marks; Indications for Use page; commercially available US/EU/UK/Japan/Canada (regional availability variant).

### PathAI (evidence layer A unless noted)

From https://www.pathai.com/:

- AISight® Digital Pathology Platform: "a cloud-native, open platform enterprise workflow solution used by the world's leading laboratories and research centers to power their digital pathology workflows and AI applications. It serves as a central hub for case management, image management, and best-in-class artificial intelligence tools to enable multiple histopathology use cases."
- Regulatory split: "AISight® Image Management System (RUO)" (research use only) vs "AISight® Dx Digital Pathology Platform (FDA 510(k) cleared)" for primary diagnosis; CE-IVDR marked variant for EU.
- Algorithm products: TumorDetect, ArtifactDetect, biomarker quantification panels (AIM-PDL1, AIM-HER, AIM-ER, AIM-PR, AIM-Ki67, AIM-MASH), PathAssistDerm, workflow optimization.
- Partner algorithm hosting: Deep Bio, Paige, Visiopharm, DoMore Diagnostics — platform hosts third-party algorithms (same pattern as Aidoc partners).
- Customer quotes/press: Labcorp deploying FDA-cleared platform nationwide; MedStar Health partnership — health-system and reference-lab tiers.
- BioPharma pole: translational research, clinical trial services, companion diagnostics, AISight Clinical Trials — research/analytics use of the same machinery (adjacent pole, weaker clinical-delivery leg).
- Pathologist contributor network: "450+ board-certified pathologists... 32.5M+ annotations" (vendor claims) — training-data machinery behind the product (L3).

## Cross-product Comparison

| Dimension | Aidoc | Viz.ai | Lunit INSIGHT | Heartflow | PathAI AISight |
|---|---|---|---|---|---|
| Image input | CT / XR (DICOM) | CT (DICOM); ECG for HCM (non-image extension) | CXR / MMG / DBT (DICOM) | CCTA (DICOM) | whole-slide pathology images |
| What is computed | triage flags on suspected acute findings + quantification | disease auto-detection + measurements + 3D processing | abnormality detection + normal-case flagging + prior comparison | 3D reconstruction + physiological values (FFRCT) + plaque quantification | tumor/biomarker detection & quantification; primary-diagnosis support |
| Result binding | per exam, per algorithm run ("results of every algorithm run, with and without findings") | per exam, per detection | per exam + prior comparison | per scan → patient-specific 3D model | per slide/case |
| Delivery surface | Widget on any workstation; AI triage results marked in PACS worklist; mobile chat | mobile/web specialist console; PACS/worklist/EHR integration | AI-integrated worklists; viewer overlay | cloud platform (app.heartflow.net) | platform hub: case/image management + viewer + AI tools |
| Primary recipient | radiologist + downstream care teams | radiologist + stroke/vascular/cardiology specialists | radiologist (screening) | cardiologist | pathologist |
| Integration machinery | EHR, PACS, scheduling, reporting | PACS, worklist, EHR; HL7/FHIR; Epic/Cerner/Meditech | PACS/RIS via partners; local DICOM gateway | scan ingestion into cloud | scanner/lab ecosystem; image management |
| Regulatory posture | FDA-cleared, CE/UKCA | FDA De Novo (DEN170073) + 510(k)s | FDA-cleared, CE MDR | FDA-cleared, CE; ISO 13485 | 510(k)-cleared Dx vs RUO split; CE-IVDR |
| Deployment | integrated into hospital IT (cloud/on-prem mix not detailed on page) | cloud only ("no on-prem hardware") | on-prem or cloud via anonymizing DICOM gateway | cloud | cloud-native |
| Multi-algorithm orchestration | yes (aiOS + partner algorithms) | yes (Orchestrator routes algorithms) | product-family level (INSIGHT suite) | single deep analysis family | yes (own + partner algorithms) |
| Monitoring/governance | platform-level (studies, customer success) | orchestrator-level | INSIGHT Manager (usage, performance, thresholds; non-device) | support/services program | platform-level |
| Notification/routing | care coordination to mobile; patient management follow-up routing | specialist alerts within seconds of acquisition | worklist prioritization (both directions) | asynchronous result delivery | case workflow within lab |
| Drift zones observed | report-mining follow-up (Patient Management) | care coordination/communication layer; ECG-based detection | screening-program ecosystem (risk, patient hub) | reimbursement machinery | biopharma research pole (RUO) |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (three jointly-held structures)

1. **Patient-bound medical images as the analytical input.** The platform ingests images of an identified patient's exam — radiology studies (DICOM) or digitized pathology slides — as the raw material it works on. Remove → generic computer-vision/ML platform (nothing medical to analyze).
2. **Algorithmic derivation of image-based findings and measurements.** The platform itself computes results from image content: suspected findings, segmentations, quantifications, classifications, derived clinical parameters. The algorithm substrate varies (classical CAD, physics-based/computational, deep learning) — the derivation is the invariant, not "AI" as a technology label. Remove → PACS/viewer (store and display without deriving) or RIS (workflow without analysis).
3. **Image-derived results delivered into clinical review.** The computed outputs are surfaced to healthcare professionals — flags on worklists, overlays in viewers, notifications to specialists, quantitative reports — to inform interpretation or care, with the clinician retaining the decision. Remove → offline research analytics (no clinical delivery leg).

Jointly-held is load-bearing:
- 1 alone = a medical data platform / imaging corpus
- 2 alone = a generic AI/vision platform
- 3 without 1+2 = PACS/viewing territory
- 1+2 without 3 = batch research analytics (the RUO/biopharma pole)
- 1+3 without 2 = an image distribution/viewing system

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Integration machinery: DICOM routing/gateway, PACS/RIS/EHR integration, HL7/FHIR; results marked into existing worklists and viewers rather than replacing them.
- Worklist prioritization / triage: positive flags move urgent exams up; normal flagging streamlines high-confidence normals (both directions observed).
- In-viewer presentation: marks, contours, key images, result summaries; results of every algorithm run surfaced "with and without findings."
- Notification/routing beyond radiology: mobile alerts to specialists (stroke, PE, vascular teams) with image sharing.
- Prior comparison / progression tracking.
- Reader confirmation loop: the radiologist/pathologist confirms or refutes AI findings; the platform shows "which pathologies to confirm."
- Monitoring & analytics console: task status, processing time, uptime, sensitivity/specificity views, threshold exploration, output trends (Lunit names its console a non-medical device — governance tooling is often regulated separately from the analysis itself).
- Regulatory clearance posture: FDA 510(k)/De Novo, CE/MDR marks, clinical validation studies — universal across the clinical pole of the sample.
- Multi-algorithm orchestration: route the right algorithm to the right study; host partner/third-party algorithms (Aidoc, Viz.ai, PathAI all exhibit this; Heartflow is the single-family counterexample).
- Deployment variants: cloud, on-prem, hybrid with anonymizing gateway.

### L2 — Variant / Optional Structure

- Specialty domain: radiology (chest/neuro/abdomen), cardiology, mammography screening, digital pathology, (ophthalmology known in market but not sampled).
- Analysis posture: acute triage & notification vs screening detection vs deep quantification vs comprehensive multi-finding panels vs primary-diagnosis support (pathology Dx).
- Care-coordination extension: communication/mobilization layers around detection (Viz-style) — when coordination becomes the center of gravity, the product drifts toward a care-coordination Type.
- Report-mining follow-up management (Aidoc Patient Management) — drifts toward care-management/follow-up territory; input is report text, not images.
- Research-use-only (RUO) vs diagnostic (Dx) regulatory posture (PathAI splits its platform this way).
- Screening-program ecosystem: risk modeling, quality analytics, patient-facing hubs (Lunit/Volpara ecosystem).
- Modality-embedded analysis (scanner-embedded quantification) — adjacent realization not directly sampled; held as market-known variant.
- Reimbursement machinery (CPT codes, payer coverage) — commercial context layer.

### L3 — Vendor-specific (kept out of canonical document)

- Named platforms/modules: aiOS™, Viz Orchestrator, Viz 3D CTA, DualScan System, INSIGHT Manager, AISight®, Roadmap™, PCI Navigator, The Widget.
- Specific pathology catalogs (11 thoracic abnormalities; specific abdomen list).
- Vendor-claimed performance numbers (sensitivity/specificity percentages, turnaround minutes, hospital counts, ROI multiples).
- Implementation-time claims ("two to three weeks").
- Training-data machinery (PathAI contributor network, annotation counts).
- Named integration partners (Epic, Cerner, Meditech, Redox, Azure).

## Vendor-specific Findings

- Aidoc's "Patient Management" mines radiology *reports* (text) for confirmed findings and routes follow-up — an extension whose input is not images. Held as vendor extension / drift zone, not part of the Type's core.
- Viz.ai's HCM detection runs on ECG signals — analysis substrate extending beyond images. Held as vendor extension; the Type's invariant remains image-anchored.
- Lunit's deployment FAQ is the clearest public statement of the data-flow pattern (local DICOM gateway strips identifiers before cloud analysis) — used as evidence for the integration/anonymization pattern, generalized cautiously.
- Lunit explicitly states the AI "does not learn live" from customer cases — evidence for the vendor-controlled model-update posture; generalized as common posture with single-product caution.
- Lunit's INSIGHT Manager is explicitly "a non-medical device" — evidence that monitoring/governance tooling is often regulated separately from the analysis engine.
- Heartflow's footer disclaimer ("used in conjunction with the patient's clinical history... clinician's professional judgement") — evidence for the advisory posture shared with CDSS.
- PathAI's RUO/Dx split — evidence that the same machinery exists in research-only posture; the clinical-delivery leg is what makes it the clinical Type.

## Boundary Findings

- **vs PACS**: PACS acquires, archives, distributes, and displays images; the analysis platform derives new results from them. Remove the derivation → PACS. Integration is the seam: analysis products deliberately write results INTO PACS worklists and viewers (Aidoc: "AI triage results marked directly in worklist") — integration is not identity. Many analysis products are PACS-agnostic and reach the radiologist through the PACS surface.
- **vs Radiology Information System / RIS**: RIS manages orders, scheduling, reporting workflow; the analysis platform consumes studies and returns results. An analysis platform that adds worklist management is extending, not becoming, an RIS.
- **vs Clinical Decision Support System** (sibling pass, 2026-09-07): CDS applies clinical knowledge to the patient's overall context to advise on decisions; the image analysis platform computes findings from image data. An image finding can feed CDS as input. Heartflow's disclaimer shows the advisory posture is shared, but the knowledge source differs: image-derived computation vs clinical knowledge evaluation. The sibling CDSS document already records this boundary from its side.
- **vs Advanced visualization workstation**: visualization tools process and display (MPR, 3D rendering); analysis platforms compute findings/quantifications. Viz 3D CTA (bone removal, 3D processing) shows the hybrid zone: image processing without finding derivation stays visualization; adding detection/quantification crosses into analysis.
- **vs General ML / data-labeling platforms**: training tooling, annotation platforms, and model-development infrastructure are upstream of this Type. PathAI's biopharma research pole (translational research, clinical trials) is the adjacent research realization; the clinical Type requires the delivery-to-clinicians leg.
- **vs Care Coordination Platform**: Viz.ai/Aidoc care-coordination modules add communication, mobilization, and transfer management around detections. When coordination becomes the center of gravity and image analysis shrinks to a trigger, the product drifts toward care coordination.
- **"去掉什么就变成另一个 Type" 判据**: remove algorithmic derivation → PACS/viewer; remove image input (analyze reports/signals instead) → CDSS-adjacent or care-management territory; remove clinical delivery (results never reach clinicians) → research analytics; remove patient binding → generic computer vision.

## Historical / Market-Sample Check (conceptual)

The L0 is phrased to admit older and differently-positioned products:

- Pre-deep-learning computer-aided detection (mammography CAD of the late 1990s/2000s) satisfies all three legs: mammography images in, algorithmic detection of suspicious regions, marks delivered to the radiologist for review. No direct source fetched for a named historical product — the historical leg is kept conceptual per evidence rules.
- Physics/quantification packages on modality workstations (e.g., cardiac quantification, calcium scoring) satisfy the same structure with deterministic algorithms.
- The invariant is therefore "algorithmic derivation," NOT "deep learning/AI," and "delivered into clinical review," NOT "mobile app/cloud." Modern cloud/mobile machinery is L1/L2, not definitional.

## Uncertainties

- Exact operational mechanics (alert acknowledgment flows, result state machines, timeout behavior, threshold defaults) were not directly observed — help centers and user guides are gated or were not fetched. All workflow descriptions are grounded in product-page descriptions, not step-level documentation.
- Whether every product surfaces negative results (Aidoc explicitly does; others not confirmed) — held as common-with-variation, not invariant.
- Whether modality-embedded analysis (scanner-embedded quantification) should count as the same Type — not directly researched; held as adjacent realization.
- Ophthalmology and other specialty poles not sampled; assumed to fit by structure, not verified.
- The exact regulatory classification boundaries (what makes a monitoring console a "non-medical device") not researched beyond Lunit's statement.

## Final Synthesis

A Medical Image Analysis Platform is defined by three jointly-held structures: it takes patient-bound medical images as input, derives findings/measurements from the image content algorithmically, and delivers those image-derived results into clinical review where professionals retain the decision. Everything else — the AI label, cloud/mobile delivery, multi-algorithm orchestration, regulatory clearance, care coordination, monitoring consoles — is common mature structure or variant posture, not the definition. The Type sits between PACS (which stores and shows images) and CDSS (which applies clinical knowledge to patient context): its distinctive act is computing new clinical information out of the image itself and routing it to the right human at the right moment.
