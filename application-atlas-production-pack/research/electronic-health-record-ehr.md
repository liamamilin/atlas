# Research Notes — Electronic Health Record / EHR

Research date: **2026-09-06**
Methodology: `WORKFLOW_v1.1.md` + `WRITING_GUIDE_v1.1.md` (v1.1)

---

## Research Goal

Understand what an Electronic Health Record / EHR actually is as an Application Type — its core objects, the workflows clinicians perform around them, the states and rules that govern the record, and where the boundary lies against adjacent Types (Practice Management, Patient Portal, LIS/RIS/PACS, Hospital Management System, HIE, Clinical Documentation Platform).

## Initial Boundary (pre-research hypothesis)

- Core use: clinicians maintain a longitudinal clinical record per patient and use it during care delivery (document, review, order, prescribe).
- Primary users: physicians, nurses, front-desk/registration staff; secondary: pharmacists, billing/coding staff, administrators.
- Likely confusions:
  - Practice Management System (scheduling/billing) — often bundled with EHR
  - Patient Portal (patient-facing companion)
  - LIS / RIS / PACS (departmental systems feeding results into the chart)
  - Hospital Management System (broader administrative suite; regional terminology)
  - Clinical Documentation Platform (documentation tooling vs system of record)
- Unknowns: is order entry (CPOE) definitional or common? Is the allergy list definitional? How do open-source / low-resource / historical products reshape the definition (§24 check)?

## Research Questions

1. What objects make up the patient chart, and which are present in *every* sampled product?
2. What role does the Encounter/Visit play in organizing documentation?
3. How does the order → result loop work, and is it definitional?
4. How is access controlled and how is documentation attributed (medico-legal character)?
5. How do products handle terminology/coding (ICD, SNOMED, LOINC, CPT, RxNorm)?
6. Where does scheduling / registration / billing sit — inside the EHR or adjacent?
7. How do open-source and low-resource products (OpenMRS, Bahmni) differ from US-certified suites (OpenEMR, Epic, Oracle Health)?
8. What is the EMR vs EHR terminology distinction, and does it imply two Types?

## Representative Products

Selected for market representativity + documentation accessibility + different product philosophies + different customer levels:

| Product | Segment | Philosophy | Docs access |
|---|---|---|---|
| OpenEMR | small/mid ambulatory practices, global | free open source, EHR+PM+billing integrated, ONC-certified | full (public wiki) |
| OpenMRS | global south, program care (HIV/TB/NCD), low-resource | open-source platform, implementer-configured, concept-dictionary driven | full (public wiki) |
| Bahmni | low-resource hospitals (500+ sites, 50+ countries) | open-source composite: OpenMRS + Odoo + OpenELIS + PACS | full (public site) |
| Oracle Health (Cerner Millennium) | large US/international health systems | commercial monolithic platform suite | index page only; detailed docs login-gated |
| Epic | large US health systems | commercial monolithic platform suite | not accessible (see Sources) |

Epic and Oracle Health are included as representative products because they define the acute-care market segment; however, **no product-specific operational claims about them are made in this research** because their operational documentation could not be fetched. They function as boundary/market anchors only.

## Sources

Fetched successfully (2026-09-06):

- OpenEMR Features — https://www.open-emr.org/wiki/index.php/OpenEMR_Features (Tier 1)
- OpenMRS Technical Overview — https://openmrs.atlassian.net/wiki/spaces/docs/pages/25476856/Technical+Overview (Tier 1)
- OpenMRS Data Model — https://openmrs.atlassian.net/wiki/spaces/docs/pages/25477157/Data+Model (Tier 1)
- OpenMRS EMR Features — https://openmrs.atlassian.net/wiki/spaces/docs/pages/26938068/OpenMRS+EMR+Features (Tier 1)
- OpenMRS home — https://openmrs.org/ (Tier 2)
- Bahmni home — https://bahmni.org/ (Tier 2)
- Bahmni Clinical Services — https://bahmni.org/clinical-services/ (Tier 1/2)
- Oracle Health documentation index — https://docs.oracle.com/en/industries/healthcare/index.html (Tier 2)
- ONC healthit.gov homepage (via failed FAQ redirect) — https://www.healthit.gov/faq/what-electronic-health-record-ehr → redirected to homepage; homepage context only (Tier 2)

**Source-access Limitations (recorded per §23):**

- Epic: `open.epic.com` timed out twice; `www.epic.com` returned 403. Epic UserWeb/help is login-gated. → No Epic-specific claims.
- athenahealth: `docs.athenahealth.com` and `www.athenahealth.com` returned 403 twice. → Dropped from sample.
- Practice Fusion: `help.practicefusion.com` transport error twice. → Dropped from sample.
- ONC EHR definition pages: FAQ URL 404; topic URL 404. → No ONC definition quoted; the EMR/EHR terminology discussion below is framed as terminology observation, not as an ONC definition.
- Oracle Health: only the documentation index was reachable; product-level wiki links (wiki.cerner.com) were not fetched (login-gated expected). → Oracle Health observations are limited to its own product taxonomy as listed on the index.

No precise operational facts (limits, defaults, timings) were filled from model memory.

---

## Product Observations

### OpenEMR (evidence layer A — directly observed)

Source: OpenEMR Features wiki page (retrieved 2026-09-06).

- Self-description: "a Free and Open Source **electronic health records and medical practice management** application… fully integrated electronic health records, practice management, scheduling, electronic billing, internationalization".
- ONC **Ambulatory EHR Certification** for version 8.0.0 (self-reported on the features page).
- **Patient Demographics**: name, DOB, sex, identification, marital status, contact info of patient and employer, primary provider, HIPAA information, language and ethnicity, insurance coverage, deceased tracking; customizable.
- **Patient Scheduling**: appointment calendar (open slots, appointment categories, repeating appointments), Patient Flow Board (tracking/reporting), recall board, multi-facility, email/SMS notifications.
- **Electronic Medical Records** section: Encounters; Medical Issues; Medications; Immunizations; Forms and clinical notes (Vitals incl. growth charts, SOAP note, Review of systems, template-driven forms, WYSIWYG notes); Group Therapy; Graphical Charting; Labs; Procedures; Patient Reports; Referrals; Patient Notes; Disclosures; electronic digital document management; Paper Chart Tracking; Clinic Messaging; Direct messaging (send/receive records); Dated Reminders; DICOM medical image viewer; syndrome surveillance reporting.
- **Prescriptions**: online drug search; track patient prescriptions and medications; create and send prescriptions via E-Prescribe / print / fax / email; customizable layout (DEA, NPI, state license fields); in-house pharmacy dispensary module.
- **Medical Billing**: CPT, HCPCS, ICD9, ICD10, SNOMED coding; clearinghouse electronic billing (ANSI X12); institutional billing (UB-04); eligibility queries; accounts receivable; EOB entry.
- **Clinical Decision Rules**: physician reminders, patient reminders, clinical quality measure calculations, customizable.
- **Patient Portal**: scheduling, secure messaging/chat, online payments, records via Direct, customized forms, new-patient registration, CCDA support, labs, medical problems, medications, allergies, appointments; secure API for third-party portals.
- **Reports**: appointments, encounters, patient lists, prescriptions/dispensing, referrals, immunizations, CQM/AMC calculations, syndromic surveillance, pending procedure orders, billing/collections reports.
- **Security**: role-based menus, fine-grained per-user access controls, Active Directory support, document encryption.
- **Interoperability**: CCDA; FHIR (ONC US Core IG 4.0.0) incl. SMART on FHIR.
- Multilanguage support (30+ languages, RTL support).

### OpenMRS (evidence layer A — directly observed)

Sources: Technical Overview, Data Model, EMR Features wiki pages; openmrs.org (retrieved 2026-09-06).

- Self-description: "Electronic medical records built by a global community"; "the world's leading open-source EMR system"; 8000+ facilities, 70+ countries, 15M+ patient records (self-reported).
- Positioning: adaptable to local clinical needs — "Primary Care, NCD, MCH/ANC, HIV, TB, Malaria, COVID, and more in your language"; REST and FHIR APIs.
- **Data model domains** (Data Model page): Concept; Encounter ("meta-data regarding health care providers interventions with a patient"); Visits; Location; Form ("user interface description"); Observation ("where the actual health care information is stored… many observations per Encounter"); Conditions; Diagnosis; Order ("things/actions that have been requested to occur"); Patient; User; Person; Groups/Workflow.
- **EAV storage**: Entity = Patient or Encounter; Attribute = Concept (the question, e.g. "Temperature"); Value = Obs (the answer, e.g. "37.5").
- **Concept dictionary** at the heart of the system: defines all concepts (questions and answers); datatypes (Numeric, Coded, Text, Date, Boolean); classes (Diagnosis, Test, Drug, Finding); multi-language names; mappings to external terminologies (CIEL, SNOMED, ICD, LOINC, RxNorm).
- **Medico-legal data handling**: metadata is *retired*; clinical data is *voided* ("marked as voided when it has been deleted or otherwise invalidated by a user") — i.e., clinical data is invalidated, not hard-deleted. Many tables carry `created_by`, `retired_by`, `voided_by` columns referencing users — attribution is built into the schema.
- **Authorization**: "very granulated permissions system. Every action is associated with a Privilege" (e.g. "Add Patient", "Update Patient"); Roles contain privileges and can inherit from other roles; Users hold roles; service methods are annotated with required privileges.
- **EMR features (O3)**: registration (with address hierarchy); patient search incl. advanced filters and comparison of similar patients (duplicate avoidance); clinic queue dashboards / service queues; patient lists; appointments & calendar; active-visits widget; patient chart widgets — vitals (with alert/warning thresholds), test results viewer (trends, filtering, custom sets), medication ordering (order basket), order history, patient forms, patient conditions, program enrollment, allergies, immunizations, attachments (photos/PDF), bulk retrospective data entry (from paper charts); lab orders & status; lab results; manual lab result entry; medication history; medication dispensing ("pharmacy-lite"); offline mode for community health workers / tablet use.
- Notable maturity signals: lab orders app "IN DESIGN" and order history "IN DESIGN" in the O3 reference app at time of writing; immunizations widget had been removed from the reference app for rework — i.e., even core-adjacent modules ship at different maturity stages without the product ceasing to be an EMR.

### Bahmni (evidence layer A — directly observed)

Sources: bahmni.org home + Clinical Services page (retrieved 2026-09-06).

- Self-description: "an easy-to-use **EMR & hospital system**… combines and enhances existing open source products into a single solution"; "Hospital System For Low Resource Settings".
- Composition: **OpenMRS** "for electronic medical records and patient management"; **OpenERP/Odoo** "for inventory, billing, financial accounting"; **OpenELIS** "for laboratory management"; **DICOM and PACS** integration.
- Scope statement: "Manage patient information across **registration, point of care, investigations, and billing**."
- Deployment: "Host and operate at the hospital site, requiring no dependence on the Internet"; runs on tablets/laptops; modular ("choose parts of Bahmni").
- **Clinical Services**:
  - Clinical Observations and Notes: a configurable forms platform; forms for general patients, emergency, surgery, vitals, intake-output, delivery, gynaecology, disease-specific; observation types numeric, textual, coded options, true-false, date, date-time, duration; forms grouped and shown on patient and visit dashboards; previously filled data can be recalled.
  - Diagnosis: clinicians capture and manage diagnoses; mapped to ICD-10 for reporting.
  - Drug Order: create new drug orders, stop or refill active ones; choose route, frequency, dosage, instructions; regimen templates auto-populate common orders for review and save.
  - Patient Dashboards: configurable widget platform — diagnosis, observations, tabular/graphical views, drug orders, patient profile, lab results, visits, radiology results, disposition, in-patient summary.
  - Visit Dashboards: single-visit data; printable view optimized for paper (e.g., discharge summary without code).
- Scale (self-reported): 500+ sites, 50+ countries, 20M+ patient records; SNOMED CT support via Snowstorm terminology server.

### Oracle Health / Cerner Millennium (evidence layer B — product taxonomy only)

Source: Oracle Health documentation index on docs.oracle.com (retrieved 2026-09-06).

- The vendor's own documentation taxonomy lists as sibling products: **Oracle Health EHR**; **Oracle Health Patient Administration**; **Oracle Health Patient Portal**; Clinical Data Exchange; Claims, Prior Authorizations, and Payments; CareAware and Revenue Cycle Millennium Platform; Population Health; Quality Management; Millennium Platform APIs.
- Observation: the vendor separates EHR from patient administration (front-office/registration operations) and from the patient portal at the product level — supporting the boundary that the EHR Type is the clinical record core, with front-office and patient-facing surfaces as adjacent products.
- Detailed operational documentation (wiki.cerner.com) was not fetched (login-gated expected); no operational claims are made.

### Epic (no evidence layer — market anchor only)

- Public surfaces (`open.epic.com`, `www.epic.com`) were not reachable during research (timeouts / 403); operational documentation is login-gated (UserWeb).
- Included in the sample as a widely referenced acute-care EHR vendor for market representativity. **No product-specific claims** are made anywhere in this research or the final document.

### ONC / healthit.gov (context only)

- The EHR FAQ and topic pages returned 404; only the homepage was reachable. Usable context from the homepage: ONC describes its mission around "access, exchange, and use of data"; homepage cites adoption/exchange statistics (e.g., 96% of US non-federal acute care hospitals electronically sending care records; 65% of individuals offered and accessing online medical records or patient portals in 2024). These are context statistics only; no definition was quoted.

---

## Cross-product Comparison

| Dimension | OpenEMR | OpenMRS | Bahmni | Oracle Health | Epic |
|---|---|---|---|---|---|
| Patient identity & registration | Demographics incl. insurance, deceased tracking | Patient/Person domains; registration app; duplicate-aware search | Registration module (OpenMRS-based) | Patient Administration is a sibling product | not observed |
| Longitudinal chart | Patient summary screen; medical issues, meds, immunizations, vitals, notes, documents | Patient chart dashboard; conditions, meds, allergies, immunizations, attachments, obs | Patient dashboard widgets (diagnosis, obs, drug orders, lab/radiology results, profile) | EHR product | not observed |
| Encounter/visit as documentation unit | Encounters; SOAP note; flow board | Encounter + Visit domains; "many observations per Encounter"; visit dashboards | Visit dashboards; disposition widget | EHR product | not observed |
| Problems/diagnoses | Medical Issues | Conditions + Diagnosis domains | Diagnosis with ICD-10 mapping | EHR product | not observed |
| Medications | Medications + prescriptions (e-prescribe/print/fax/email) | Medication ordering (order basket), history, dispensing | Drug orders (start/stop/refill; route/frequency/dosage; regimen templates) | EHR product | not observed |
| Allergies | Portal lists allergies; chart module | Allergies widget (IN DEV at time of writing) | not observed on fetched pages | EHR product | not observed |
| Immunizations | Immunizations section | Widget removed from O3 refapp for rework | not observed | EHR product | not observed |
| Orders (lab/imaging/procedure) | Procedure orders; labs; referrals | Order domain in core; lab orders app IN DESIGN; order history IN DESIGN | via OpenELIS (lab) and PACS (radiology) as separate components | EHR product | not observed |
| Results review | Labs; DICOM viewer; patient reports | Test results viewer (trends, filters); manual lab result entry | Lab results + radiology results widgets | EHR product | not observed |
| Decision support | Clinical decision rules (reminders, CQM) | Vitals alert/warning thresholds | not observed | EHR product | not observed |
| Scheduling | Calendar, flow board, recalls | Appointments & calendar (IN DEV); service queues | Registration + visit flow | Patient Administration sibling | not observed |
| Billing | Integrated (CPT/ICD/X12 clearinghouse) | not core | separate Odoo component | Claims/Prior Auth/Payments sibling | not observed |
| Patient portal | Integrated module | not observed | not observed | separate sibling product | not observed |
| Access control | Role-based menus; per-user access controls; AD | Privilege/Role/User; privilege-annotated services | inherited from OpenMRS | EHR product | not observed |
| Attribution / record integrity | (not directly observed on fetched page) | created_by/voided_by columns; void vs retire semantics | inherited from OpenMRS | EHR product | not observed |
| Terminology | CPT, HCPCS, ICD9/10, SNOMED | Concept dictionary mapped to CIEL/SNOMED/ICD/LOINC/RxNorm | SNOMED CT via Snowstorm; ICD-10 | EHR product | not observed |
| Interoperability | CCDA, FHIR US Core, SMART on FHIR, Direct | REST + FHIR APIs | PACS/DICOM; SNOMED | Clinical Data Exchange sibling; Millennium APIs | not observed |
| Deployment | self-hosted web (Win/Linux/Mac) | self-hosted; offline mode for CHWs | on-site, no internet dependence | vendor-hosted/platform | not observed |
| Certification/regulatory | ONC Ambulatory EHR certified | none claimed | Digital Public Good recognition | (US certified suites; not observed) | not observed |

### Stable commonalities (present across all fully-observed products)

1. Patient identity + registration as the entry point to a per-patient record.
2. A longitudinal chart holding problems/diagnoses, medications, and clinical notes/observations.
3. Encounter/visit as the unit that organizes documentation.
4. Authenticated users with role-based access; attributed entries.
5. Coded clinical data bound to standard terminologies.
6. Medication ordering/recording as the most universal order form.
7. Results (lab/radiology) visible in the chart, whether discrete or as documents/images.
8. Reporting over the recorded data.

### Common but not universal (L1 candidates)

- Allergies as a first-class chart domain (absent/immature in OpenMRS O3 reference app at time of writing).
- Immunizations (removed from OpenMRS O3 reference app for rework).
- Discrete lab-order entry inside the EHR (IN DESIGN in OpenMRS O3; handled by OpenELIS in Bahmni).
- Decision-support rules (OpenEMR yes; OpenMRS limited to vitals alerts; Bahmni not observed).
- Scheduling (present in OpenEMR/OpenMRS; separate product at Oracle Health).
- Patient portal (OpenEMR integrated; Oracle Health separate product).

### Variant-level (L2 candidates)

- Billing/revenue-cycle bundling (US-centric; OpenEMR integrated; Bahmni via Odoo; Oracle Health separate product line).
- E-prescribing network transmission (OpenEMR e-prescribe; OpenMRS/Bahmni record orders without external transmission evidence).
- Interoperability posture (FHIR/CCDA/Direct vs PACS/DICOM vs closed).
- Deployment (on-prem vs hosted; offline operation).
- Regulatory certification (ONC; program-oriented global-south deployments).
- Care-setting specialization (ambulatory vs hospital vs program care).

---

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

```text
Identified Patient
└── Longitudinal clinical chart (the record of care over time)
    ├── Problems / diagnoses
    ├── Medications
    └── Clinical notes / observations
└── Encounter/visit as the organizing unit of documentation
└── Authenticated, attributed documentation by authorized care providers
    (role-restricted access)
```

Four invariants. Removal tests:

- Remove the identified patient anchor → it is no longer a medical record system.
- Remove the longitudinal chart with problems/meds/notes → it is a scheduling or billing tool, not an EHR.
- Remove encounter-based documentation → it is a data warehouse or registry, not a working clinical record.
- Remove authenticated/attributed access → it is not a deployable medico-legal record.

Deliberately **not** in L0 (checked against §24 historical/regional samples): allergies list, immunizations, discrete lab orders, CPOE breadth, e-prescribing transmission, decision support, scheduling, billing, patient portal, cloud deployment, FHIR APIs, certification status. Evidence: OpenMRS O3 reference app ships with lab orders "IN DESIGN", order history "IN DESIGN", and its immunizations widget removed for rework — yet it is unambiguously an EMR. Bahmni runs lab and radiology through separate components (OpenELIS, PACS) while remaining an EMR+hospital system.

### L1 — Common Mature Structure

- Allergy/intolerance list (near-universal; immature in one sampled reference app)
- Immunization record
- Vitals & measurements as structured data (flowsheets, trends)
- Order entry beyond medications (labs, imaging, referrals, procedures) + results review loop
- Basic clinical decision support (reminders, alerts, quality-measure calculation)
- Structured note tooling: templates, forms, configurable observation forms
- Patient search with duplicate-record awareness
- Work lists / queues / flow boards for visit management
- Reporting & quality measurement
- Audit trail of record access (regulation-driven in many markets; not directly observed in every sampled product)
- Patient registration/demographics management (identity maintenance of the chart anchor)

### L2 — Variant / Optional Structure

- Scheduling & front-office operations (bundled or separate; boundary with Practice Management)
- Billing / revenue cycle (bundled in US-style products; separate component or product elsewhere)
- Patient portal (bundled module or separate product)
- E-prescribing network transmission; controlled-substance workflow
- Interoperability posture: FHIR APIs, CCDA, Direct messaging, HIE connectivity, PACS/DICOM integration
- Deployment: self-hosted vs vendor-hosted; offline/low-connectivity operation
- Regulatory/certification context: ONC certification (US), program-oriented deployments (global south), national systems
- Care-setting specialization: ambulatory, acute inpatient, emergency, behavioral health, long-term care, home health
- Specialty/program modules (e.g., ophthalmology module; disease-program enrollment)

### L3 — Vendor-specific (research notes only)

- OpenEMR: CAMOS module, Nation Notes, Eye (Ophthalmology/Optometry) module, Chart Tracker, specific clearinghouse integrations (Office Ally, ZirMED, ClaimRev), USPS address verification.
- OpenMRS: EAV storage implementation, CIEL concept dictionary, O3/React microfrontend architecture, service queues naming, "pharmacy-lite" dispensing.
- Bahmni: specific composition (OpenMRS + Odoo + OpenELIS + PACS), implementer widget platform, printable visit dashboards.
- Oracle Health: Millennium Platform, CareAware, product-line naming (Patient Administration, Clinical Data Exchange).
- Epic: none (no accessible evidence).

---

## Vendor-specific / Rejected Findings

Rejected from the canonical core (with reasons):

- **"EHR = EHR + PM + billing suite"** — rejected: Bahmni and Oracle Health separate billing/patient administration from the EMR; OpenEMR's bundling is a packaging choice.
- **"EHR requires integrated e-prescribing transmission"** — rejected: OpenMRS/Bahmni record medication orders without observed external transmission; e-prescribing networks are regional (US) infrastructure.
- **"EHR requires a patient portal"** — rejected: Oracle Health ships the portal as a separate product; portal is a companion surface with its own Atlas leaf.
- **"EHR requires ONC certification"** — rejected: certification is a US regulatory context (L2); OpenMRS/Bahmni make no certification claim.
- **"EHR requires cloud deployment"** — rejected: Bahmni explicitly targets on-site hosting without internet dependence.
- **"Allergy list is definitional"** — rejected: allergies widget was still IN DEV in the OpenMRS O3 reference app at time of writing; moved to L1.
- **"Lab order entry inside the EHR is definitional"** — rejected: IN DESIGN in OpenMRS O3; handled by a separate LIS component in Bahmni; moved to L1.
- **"Immunizations are definitional"** — rejected: removed from OpenMRS O3 reference app for rework; moved to L1.

## Boundary Findings

- **vs Practice Management System**: PM owns scheduling, registration front-office operations, and billing/claims. Evidence: OpenEMR self-describes as EHR **and** practice management (bundled); Bahmni splits EMR (OpenMRS) from billing/accounting (Odoo); Oracle Health lists EHR and Patient Administration as separate products. Test: remove clinical documentation → PM; remove scheduling/billing → still an EHR.
- **vs Patient Portal**: clinician-facing system of record vs patient-facing companion surface. Oracle Health ships them as separate products; OpenEMR bundles a portal module. The portal reads from / writes into the record but is not the record.
- **vs LIS / RIS / PACS**: departmental systems run lab/imaging workflows; their results and reports flow into the chart. Bahmni integrates OpenELIS and PACS as separate components; OpenEMR adds a DICOM viewer; OpenMRS keeps lab orders in a separate app. The EHR holds results; it does not run the modality or the lab.
- **vs Hospital Management System**: HMS (regional term, especially in Asia) spans registration, billing, inventory, pharmacy stock, and more. Bahmni brands itself "EMR & hospital system" and is exactly this composition. The EHR is the clinical record core inside such suites.
- **vs Health Information Exchange / HIE**: HIE moves records between organizations; the EHR is where the record lives and is used. Interoperability posture is L2.
- **vs Clinical Documentation Platform**: documentation tooling (templates, scribes) produces content for the chart; the EHR is the system of record that holds and governs it.
- **vs CPOE / Clinical Decision Support / Electronic Prescribing / Medication Management (directory siblings)**: in the researched sample these are capabilities (L1) of the EHR; standalone products exist in some markets. Taxonomy observation recorded for STATUS.md.
- **EMR vs EHR terminology**: OpenMRS and OpenEMR self-identify as "electronic medical records"; OpenEMR is simultaneously ONC **Ambulatory EHR** certified. The historical distinction (EMR = single-organization record; EHR = interoperable, cross-organization longitudinal record) describes an interoperability posture (L2), not two structures. Treated here as **one Type**; the directory leaf name ("Electronic Health Record / EHR") already carries both terms.
- **vs Telehealth Platform**: telehealth is a visit modality; the EHR remains the record in which the visit is documented.

## Uncertainties

- Inpatient/acute-care workflow depth (admission/discharge/transfer, medication administration records, nursing flowsheets) could not be verified from primary sources in this sample (Epic/Oracle Health inaccessible; OpenMRS/Bahmni inpatient pages not fetched). The final document keeps inpatient-specific claims generic.
- Audit-trail universality: OpenMRS evidence shows schema-level attribution; OpenEMR's fetched page shows access controls but not audit-log specifics. Audit trail is placed in L1 with moderate wording.
- Note sign-off / attestation steps: not directly evidenced in fetched pages; deliberately not asserted as a universal workflow step.
- Exact regulatory scope of "EHR" vs "EMR" in non-US markets was not researched; the terminology discussion is kept at the level of market usage observed in the sample.

## Final Synthesis

An EHR is best modeled as:

```text
Identified Patient
  → longitudinal chart (problems, medications, notes/observations; plus common domains)
  → documented through encounters by authorized, attributed care providers
  → supporting an order → result → review loop (common mature structure)
  → under role-based access control and medico-legal record discipline
  → with front-office (scheduling/registration), billing, portal, and
    departmental systems (LIS/RIS/PACS) as adjacent, often-bundled surfaces
```

The defining core is small and stable across a 1990s-style open-source ambulatory EMR, a global-south program EMR, a low-resource hospital composite, and (as far as product taxonomy shows) the largest US acute-care platforms. Everything that feels "essential" in a modern US deployment — portal, e-prescribing network, billing, certification, FHIR — is L1/L2 market maturity, not the Type.
