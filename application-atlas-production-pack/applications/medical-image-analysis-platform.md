# Medical Image Analysis Platform

## Overview

A **Medical Image Analysis Platform** is clinical software that computes findings, measurements, and derived parameters from a patient's medical images, and delivers those image-derived results into clinical review — flagging suspected findings on worklists, annotating them in viewers, notifying specialists, or producing quantitative reports — while the clinician retains the interpretation and the decision.

Its defining structure is small:

```text
Patient-bound Medical Images (exam / study / slide)
└── Algorithmic Derivation
    (detection · segmentation · quantification · derived clinical parameters)
    └── Image-derived Results Bound to the Patient's Exam
        └── Delivery into Clinical Review
            └── Clinician Retains the Decision
```

Everything else commonly associated with the category — the "AI" label, cloud or mobile delivery, multi-algorithm orchestration, regulatory clearances, care-coordination messaging, monitoring dashboards — is widespread in current products but is not what makes the software an image analysis platform. Older computer-aided detection and quantification packages, built before deep learning, satisfy the same defining structure.

The platform is not the image archive (PACS), not the workflow system (RIS), and not the record (EHR): its distinctive act is computing new clinical information out of the image itself and routing it to the right human at the right moment.

## Users & Context

Primary users are the clinicians who read images or act on image findings:

- **radiologists** — the dominant readers; they receive triage flags and detection results on their worklists, confirm or refute AI findings during interpretation, and benefit from quantification that automates repetitive measurement
- **pathologists** — in the digital pathology pole, they review whole-slide images with AI-derived detections and biomarker quantifications, up to primary-diagnosis support
- **treating specialists** — stroke neurologists, interventionalists, cardiologists, pulmonologists; they receive notifications of suspected acute findings with the images attached, and review them on mobile or web surfaces to plan care

Secondary users operate the system rather than consume its results:

- **imaging/IT administrators** — configure integrations, deployment mode, and which algorithms run on which study types
- **quality and operations teams** — monitor usage, performance, and output trends through analytics consoles

The work environment is the hospital or imaging network's existing radiology and clinical IT stack. The platform is deliberately not a standalone island: it ingests studies from modalities and archives, and it writes its results back into the worklists, viewers, and record systems clinicians already use. Deployment ranges from hospital-integrated to cloud services reached through anonymizing gateways.

## Core Model

### The Defining Core

Three properties, each necessary for the software to be recognizable as a medical image analysis platform:

- **Patient-bound medical images as the analytical input.** The platform works on images of an identified patient's exam — radiology studies (CT, X-ray, mammography, MRI) or digitized pathology slides. The exam is the unit the analysis belongs to. Remove this and the product becomes a generic computer-vision or machine-learning platform with nothing medical to analyze.
- **Algorithmic derivation of image-based results.** The platform itself computes new information from the image content: suspected findings, lesion segmentations, measurements, classifications, and derived clinical parameters (for example, a physiological value computed from a reconstructed anatomy). The algorithm substrate varies — classical detection rules, physics-based computation, deep learning models — but the derivation is the point. Remove this and the product is an archive or a viewer: it stores and shows images without producing anything new from them.
- **Delivery of image-derived results into clinical review.** The computed results are surfaced to healthcare professionals — marked on worklists, overlaid in viewers, pushed as notifications, rendered as quantitative reports — to inform interpretation or care. The clinician reviews, confirms or refutes, and decides. Remove this and the product is offline research analytics: computation with no clinical destination.

The three are jointly held. Images without derivation are an archive; derivation without images is a generic AI platform; derivation without clinical delivery is a research tool.

### Standard Capabilities

Mature products commonly add the following. They make the platform practical and trustworthy, but a product relying only on the core would still be an image analysis platform.

- **Integration machinery** — DICOM routing or gateways that move studies in, and connections to PACS, worklists, RIS, and EHR (commonly through HL7/FHIR-style interfaces) that carry results back out. Some cloud deployments route analysis through a local gateway that strips patient-identifying details before transmission.
- **Worklist prioritization** — suspected-positive exams are flagged and moved up the reading queue; conversely, high-confidence normal cases can be flagged to streamline high-volume reading. Both directions appear in mature products.
- **In-viewer presentation** — marks, contours, key images, and result summaries placed in the reading surface; results of every analysis run are available, including studies where nothing was found.
- **Notification and routing beyond radiology** — time-sensitive findings pushed to specialists' mobile devices with images attached, so care teams mobilize before the formal report exists.
- **Prior comparison and progression tracking** — current studies compared automatically against earlier exams, with changes in findings surfaced.
- **Reader confirmation loop** — the reading clinician confirms or refutes AI findings; the interface is built around showing which findings need human confirmation.
- **Monitoring and analytics** — consoles tracking task status, processing time, uptime, output distributions, and performance against thresholds; in at least one sampled product this tooling is explicitly regulated as a non-medical device, separate from the analysis engine itself.
- **Regulatory clearance posture** — analysis intended for clinical use is typically cleared or certified as medical device software (FDA clearances, CE marks), backed by validation studies. This posture is universal in the clinical pole of the market but is a market property, not the defining structure: research-use-only deployments of the same machinery exist.
- **Multi-algorithm orchestration** — enterprise platforms route the right algorithm to the right study automatically and may host third-party algorithms alongside their own; single-analysis-family products are equally valid members of the Type.
- **Deployment variants** — cloud, on-premises, or hybrid (local anonymization gateway feeding a cloud analysis engine).

### One Structure, Many Implementations

The core is conceptual; products realize each part differently:

```text
Image input          →  DICOM radiology studies, mammography/tomosynthesis,
                        chest radiographs, coronary CT, whole-slide pathology scans

Derivation           →  deep-learning detection, classical CAD rules,
                        computational-fluid-dynamics physiology, biomarker
                        quantification, 3D anatomical reconstruction

Delivery surface     →  PACS worklist marking, in-viewer overlays, mobile
                        specialist alerts, cloud analysis consoles,
                        pathology case-management hubs

Recipient            →  radiologist at read time, pathologist at diagnosis
                        time, treating specialist at care time
```

A reader who has only seen one implementation — for instance, a stroke-detection alert on a phone — should still recognize a mammography screening aid or a cloud FFR-CT service as the same Type.

## How It Works

The Type runs one fast loop around each exam, plus a slower operations loop around the analysis machinery itself.

### 1. Images enter the platform

Studies flow in from the imaging environment — modalities, archives, or the PACS — through integration the vendor configures at deployment. In cloud deployments a local gateway typically anonymizes the data before it leaves the facility. The binding to the patient and exam travels with the images; every result the platform produces will be attached to that same exam.

### 2. Analysis runs against the exam

In triage-style deployments, analysis runs automatically and continuously on incoming studies of the covered types — no one queues a job per case. Enterprise platforms route each study to the algorithms that apply to it. Deep quantification analyses are typically performed on indicated studies and take longer, producing their results asynchronously after acquisition. The output is a set of image-derived results: suspected findings with locations, measurements, quantified values, or a reconstructed model — and, just as importantly, a recorded negative result when nothing suspicious is detected.

### 3. Results are delivered into clinical surfaces

Delivery follows the exam's clinical urgency:

- **triage path** — suspected acute findings are flagged on the reading worklist (the exam moves up the queue) and, in parallel, pushed as notifications with images to the responsible specialists' mobile devices, so treatment planning can begin before the formal report
- **reading path** — detection results appear as marks and summaries in the reading workflow; the radiologist sees at a glance which findings need confirmation, and studies with no findings are also accounted for
- **quantification path** — measurements, physiological values, and 3D reconstructions are delivered through the platform's own console or written back into the clinical systems, for the interpreting or treating clinician to use alongside the rest of the diagnostic picture
- **pathology path** — detections and biomarker scores appear in the lab's case-management and viewing environment, supporting the pathologist's diagnosis

### 4. Clinicians review and act

The recipient confirms or refutes the AI findings, incorporates quantifications into interpretation, or mobilizes care around a notification. The platform's outputs inform these actions but never execute them: no analysis result changes a patient's care by itself. Products differ in how much coordination machinery wraps this step — from a simple flag on a worklist to structured communication between transferring and receiving teams.

### 5. The operations loop keeps the machinery trustworthy

On a slower cycle, the organization monitors the platform: usage and uptime, output distributions, performance against thresholds, and the rate at which clinicians confirm or refute findings. Thresholds and routing rules are tuned with this data. Model improvements arrive as vendor-controlled software updates — the platform does not learn live from the local site's cases — and updates are validated before deployment. In clinical use, the analysis engines themselves sit inside a medical-device regulatory posture, while monitoring tooling may be regulated separately or not at all.

## Interfaces

The surfaces below are described conceptually; exact layouts and names vary by product.

### AI worklist / triage surface

The reading team's entry point when analysis is integrated into workflow.

- typical information: exams with AI flags and finding summaries, prioritization indicators, negative-result status
- primary actions: open the exam in the viewer, review flagged findings, confirm or refute, proceed to reporting

### In-viewer results overlay

The reading surface where image-derived results meet the images.

- typical information: marks/contours on lesions, key images, per-algorithm result summaries, prior-comparison views
- primary actions: inspect a finding, adjust or measure, accept into the report, dismiss

### Specialist notification surface

A mobile or web surface for treating specialists receiving time-sensitive findings.

- typical information: patient and exam context, the suspected finding, images and reconstructions, care-team communication
- primary actions: review images, confirm the finding, communicate with the care team, plan the intervention

### Quantitative analysis console

The platform surface for deep quantification products.

- typical information: patient-specific 3D reconstructions, color-coded physiological values, measurements at user-selected locations, comparison across studies
- primary actions: place measurement points, inspect values along structures, export or share the analysis

### Pathology case and image management hub

The digital pathology pole's working environment.

- typical information: cases and slides, AI detections and biomarker scores, workflow state
- primary actions: open slides, review AI results, sign out diagnosis

### Monitoring and analytics console

The operations team's surface, separate from clinical use.

- typical information: task status, processing time, uptime, output trends, performance metrics against thresholds
- primary actions: filter, compare, tune thresholds, feed deployment decisions

### Configuration and administration

- typical information: connected systems, enabled algorithms per study type, routing and notification rules, deployment mode
- primary actions: configure integrations, enable/disable algorithms, manage users and roles

## Important Rules / Behaviors

### The clinician decides

Analysis results inform interpretation and care but never execute it. Confirming, refuting, and acting on a finding is the clinician's act; products are built around this — the interface asks "which findings do you confirm," not "what should the system do." A system that acted on findings autonomously would no longer be this Type.

### Results are bound to the exam

Every result — positive or negative — attaches to the identified patient's exam and persists with it. The analysis does not float free of its images; later readers encounter the AI results in the exam's context.

### Negative results are part of the output

The platform's answer to "nothing found" is itself a delivered result: it can streamline normal cases out of the urgent path and it is visible to the reader. Mature products surface the results of every analysis run, not only the positive ones.

### Analysis is continuous, results may be asynchronous

Triage analysis runs automatically on incoming studies; deep quantification may complete minutes to hours after acquisition and is delivered asynchronously. The platform's value in acute care depends on the fast path; its value in quantification depends on the reliable asynchronous path.

### Model behavior is vendor-controlled

Improvements to the analysis arrive as validated vendor updates rather than live adaptation; at least one sampled product states explicitly that its models do not learn from a site's own cases in real time. Sites tune thresholds and routing, not the model itself.

### The platform depends on its host environment

The Type is defined by integration: without connections to modalities, archives, worklists, and record systems, the derived results have no path to a clinician. Products therefore compete on integration depth as much as on algorithm quality, and they deliberately write results into existing surfaces rather than demanding clinicians come to a new one.

## Variants

Common forms the Type takes in the market:

- **acute triage & notification** — automatic detection of time-sensitive findings with worklist reprioritization and specialist alerts (stroke, hemorrhage, pulmonary embolism, aortic dissection)
- **screening & detection panels** — high-volume reading support (mammography, chest X-ray), including normal-case flagging and prior comparison
- **deep quantification** — single-family products that derive physiological parameters or detailed measurements from a scan (coronary physiology, plaque quantification)
- **comprehensive multi-finding panels** — one product analyzing many pathologies per study
- **digital pathology** — whole-slide image analysis for detection and biomarker quantification, up to cleared primary-diagnosis support
- **research-use-only deployments** — the same machinery without the clinical-delivery regulatory posture, used in trials and translational research
- **care-coordination-extended products** — detection wrapped in communication, mobilization, and transfer management; when coordination becomes the center of gravity, the product is drifting toward a care-coordination Type
- **report-mining follow-up extensions** — modules that mine radiology reports (text, not images) to route confirmed findings for follow-up; an adjacent extension rather than the core Type
- **deployment variants** — cloud-only, on-premises, or hybrid with an anonymizing local gateway; distribution through imaging/PACS vendor partnerships is a common channel shape

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| PACS | host environment | PACS acquires, archives, distributes, and displays images; the analysis platform derives new results from them. Remove the derivation and what remains is a PACS. Analysis products deliberately write results into PACS surfaces — integration is not identity |
| Radiology Information System / RIS | adjacent workflow system | RIS manages orders, scheduling, and reporting workflow; the analysis platform consumes studies and returns results into that workflow |
| Clinical Decision Support System | adjacent advisor | CDS applies clinical knowledge to the patient's overall context to advise on decisions; the image analysis platform computes findings from image data. An image finding can feed CDS as input. Both share an advisory posture, but the knowledge source differs |
| Advanced visualization workstation | adjacent tool | visualization tools process and display images (3D rendering, reconstructions) without deriving findings; adding detection or quantification crosses into this Type |
| Care Coordination Platform | drift boundary | coordination products mobilize teams and manage transfers; image analysis products compute findings. Detection-triggered coordination is a variant; coordination as the center of gravity is a different Type |
| Machine Learning Platform / Data Labeling | upstream | training tooling and annotation platforms build models; this Type runs validated analysis in clinical delivery. Research-use deployments sit between the two |
| Electronic Health Record | record system | the EHR holds the patient's record; image-derived results may be posted into it or referenced from it, but the computation happens in this Type |
| Pathology Information System / LIS | lab workflow system | the LIS manages specimens and lab workflow; whole-slide analysis complements it with image-derived results |

The sharpest boundary is with PACS, because the two are commercially entangled — analysis results are delivered through PACS surfaces, and some archives now embed analysis. The structural test: if the software only stored, moved, and displayed images, it would be a PACS; the moment it computes new clinical information from the image content and routes it to a clinician, it is this Type.

## Representative Products

- **Aidoc** — enterprise multi-algorithm triage and notification platform for radiology and acute care, with partner algorithms and care-coordination extensions
- **Viz.ai** — detection plus specialist care coordination (stroke, vascular, cardiology), mobile-first
- **Lunit (INSIGHT)** — screening and detection for high-volume imaging (mammography, chest X-ray), distributed through imaging and PACS partners; also spans digital pathology biomarker analysis
- **Heartflow** — single deep quantification family deriving coronary physiology and plaque measures from coronary CT
- **PathAI (AISight)** — digital pathology platform combining image/case management with own and partner AI algorithms, in cleared diagnostic and research-use postures

## Sources

Research date: **2026-09-08**

- Aidoc — platform overview: https://www.aidoc.com/platform/ ; radiology solution: https://www.aidoc.com/solutions/radiology/
- Viz.ai — platform overview: https://www.viz.ai/platform/ ; Viz LVO product page: https://www.viz.ai/neuro/large-vessel-occlusion
- Lunit — partner/radiology overview: https://www.lunit.io/en/radiology-technology-partners/ ; INSIGHT CXR product page: https://www.lunit.io/en/ai-radiology-software/insight-cxr/
- Heartflow — overview: https://www.heartflow.com/ ; FFRCT Analysis: https://www.heartflow.com/heartflow-one/ffrct-analysis/
- PathAI — overview: https://www.pathai.com/

> Sourcing limitation: official product and solution pages were the reachable layer on 2026-09-08; detailed operational documentation (help centers, user guides) is gated or was not fetched, and step-level mechanics (alert acknowledgment flows, result state machines, default thresholds) are therefore not stated in this document. Vendor-published performance figures (sensitivity/specificity percentages, turnaround times, deployment counts) are treated as vendor claims and intentionally omitted. The interaction-loop description is grounded in the sampled products' own product-page descriptions; the historical check (pre-deep-learning CAD and quantification packages) is conceptual, with no named historical product directly sourced.
