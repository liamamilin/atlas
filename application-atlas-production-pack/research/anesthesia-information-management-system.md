# Research Notes — Anesthesia Information Management System

## Research Goal

Understand what an Anesthesia Information Management System (AIMS) actually is as an Application Type: its defining structure, its perioperative workflow, its interfaces, its rules, and its boundaries against neighboring Types (EHR, Operating Room Management, Emergency Department Information System, critical-care systems).

## Initial Boundary

Initial hypothesis (pre-research):

- AIMS is the anesthesia department's clinical system: it documents the anesthetic care of a patient around a procedure, replacing the paper anesthesia record.
- Its differentiator vs a generic EHR is (a) the anesthesia case as the organizing unit and (b) automatic capture of intraoperative physiologic data from connected devices (monitors, anesthesia machines, ventilators, infusion pumps).
- Nearest neighbors: EHR (longitudinal whole-patient record), Operating Room Management (OR as resource: scheduling/throughput), EDIS (departmental-system pattern, different department), ICU/critical-care PDMS (sibling structure, sometimes same platform).
- Main unknowns: whether pre-op assessment and PACU documentation are part of the defining core or common modules; whether device capture is invariant; how EHR-integrated modules (Epic OpTime, Cerner) relate to standalone AIMS.

## Research Questions

1. What objects exist in an AIMS? (case, anesthesia record, physiologic data stream, drug administrations, events, assessments, recovery records)
2. What is the canonical workflow from case listing to record completion?
3. Which devices feed the record, and how is capture described?
4. What rules govern the record (attribution, safety, offline behavior, compliance, billing)?
5. What interfaces do anesthesia providers actually work in?
6. How do products differ in packaging (standalone vs suite module vs EHR module) and does that change the Type?
7. Historical check: do paper-era and early automated anesthesia record keepers fit the same definition?

## Representative Products

Selected for market representativeness, different product philosophies, and different geographies/customer tiers:

| Product | Vendor | Philosophy | Evidence tier reached |
|---|---|---|---|
| MetaVision Anesthesia | iMDsoft (international) | standalone critical-care + anesthesia clinical information system | Tier 2 (official product pages) |
| Anesthesia Manager | Picis Clinical Solutions (US, part of Harris Computer) | module of a perioperative suite (Preop/OR/PACU/Anesthesia as sibling products) | Tier 2 (official product page + FAQ) |
| Diane Aims | Bow Medical (France) | European specialist AIMS, modular critical-care suite, offline-first | Tier 2 (official product pages) + Tier 3 (peer-reviewed implementation study) |
| Epic OpTime (anesthesia) | Epic (US) | EHR-integrated perioperative module | market anchor only — no public docs reachable; no product claims made |
| Oracle Health / Cerner (anesthesia/surgical) | Oracle Health (US) | EHR-integrated module | market anchor only — docs gated (wiki.cerner.com); no product claims made |

Rejected/abandoned samples:

- Dräger Innovian Anesthesia (device-vendor philosophy) — draeger.com timed out twice; abandoned per network rule; no claims made.
- Surgical Information Systems (SIS) — official site not reachable via available search; abandoned; no claims made.
- Veterinary anesthesia record systems (2026 Vet Anaesth Analg cloud-based electronic veterinary anesthesia record) — out of scope for this human-healthcare leaf; recorded as an observation only.

## Sources

- iMDsoft — MetaVision Anesthesia product page: https://imd-soft.com/metavision/anesthesia/ (fetched 2026-09-06)
- iMDsoft — corporate/product overview: https://www.imd-soft.com/ (fetched 2026-09-06)
- Picis — Anesthesia Manager product page + FAQ: https://picis.com/solution/anesthesia-manager/ (fetched 2026-09-06)
- Picis — root/suite navigation (Preop Manager, OR Manager, PACU Manager, Device Hub, SmarTrack, Envision Analytics): https://www.picis.com/ (fetched 2026-09-06)
- Bow Medical — Diane Aims product page: https://bowmedical.com/en/intuitive-anaesthetic-records-for-operating-theatres/ (fetched 2026-09-06)
- Bow Medical — company/suite overview: https://www.bowmedical.com/ (fetched 2026-09-06)
- Prpic N, et al. "Adoption and Efficiency of an Anesthesia Information Management System: Evaluation of Workflow Integration in Perioperative Care." Healthcare (Basel) 2026;14:1520. PMC13256662 (full text via Europe PMC REST, fetched 2026-09-06) — describes AIMS as specialized PDMS; Diane system (Bow Medical) implementation at Clinical Hospital Merkur, Zagreb.
- Oracle Health documentation index: https://docs.oracle.com/en/industries/healthcare/index.html (fetched 2026-09-06) — no public anesthesia-specific operational docs; wiki.cerner.com links gated.
- Referenced (not fetched, pointer only): Tewfik G, et al. "Narrative Review of Electronic Health Record Systems in Anesthesia: Benefits, Risks, and Medico-Legal Considerations in the United States of America." J Med Syst 2025;49:87 — cited by PMC13256662; supports the medico-legal framing of anesthesia records.

### Source-access Limitations

- No Tier-1 help center / user manual / training documentation was reachable for any sampled product. Evidence base is Tier-2 official product pages (marketing-adjacent but operationally descriptive) plus one Tier-3 peer-reviewed implementation study.
- Epic (open.epic.com / epic.com), Dräger, SIS, and Cerner wiki documentation were unreachable or gated.
- Consequence: no precise operational facts are asserted anywhere (no sample rates, no numeric limits, no exact field lists, no exact state names, no default settings). Vendor-marketed numbers (e.g., "420/450+ device drivers", "500+ drivers", "80% of entries in one click", ROI percentages) are recorded here as vendor claims only and are excluded from the final document except where explicitly attributed as vendor claims.

## Product A — iMDsoft MetaVision Anesthesia

### Key observations (Evidence layer A unless noted)

- Positioned as "Anesthesia Information Management System & Perioperative Care"; "aids every step of the complex perioperative workflow, spanning pre-op to intra-op and post-anesthesia care units".
- "Generating complete and accurate anesthesia records" is the central deliverable claim.
- Workflow phases explicitly marketed: Pre-Op (review planned anesthesia protocol, pre-op scores, access pre-op data in intra-op and post-op, print pre-op visit reports and patient instructions) / Intra-Op ("complete view of critical system & device data", "smart alerts on changes in the patient's condition", "record events & medications with one click or a barcode scan", "pre-set dosing templates", "plan & document the transfer to the PACU") / Post-Op (access entire anesthesia records, review and validate medication orders, pain management view with pain scores and medications, discharge reports auto-populated).
- Continuum of care: "from the pre-op assessment, through intra-op, to discharge from the PACU and extending to ICU and general wards."
- Interoperability: "Integrates seamlessly with all major hospital information systems and hundreds of medical devices" (vendor claim).
- Pediatrics-specific section: pediatrics-tailored scores and documentation, pediatric BMI charts, early warning table.
- Key capability list: patient management, continuum of care, clinical documentation, medication management, patient monitoring & decision support.
- Customer quotes (Hadassah): adherence to PONV treatment protocols (drug choice, dose, time), "anesthesia records don't get lost anymore", data retrieval for quality assurance and research. Sydney Adventist: "coding and billing processes are much easier"; records visible at any workstation by multiple caregivers simultaneously.
- Marketing ROI numbers (20% LOS reduction, 72% billing-error reduction, 90 min saved/shift) — vendor claims, excluded from final doc.
- Platform context: MetaVision is one suite with ICU, Anesthesia, Clinical EMR, MobileVision products — anesthesia shares a platform with critical care.

## Product B — Picis Anesthesia Manager

### Key observations

- Titled "Anesthesia EMR Software & Management System"; "Advanced EMR, Record, and Charting Solution"; "Integrated into the Perioperative and Clinical Suite for OR Efficiency".
- Positioning: "Anesthesia software just like a paper record, without the risk" — explicitly frames the product as the electronic successor of the paper anesthesia record.
- "automate the anesthesia documentation process from preoperative assessments through intraoperative monitoring to postoperative care" (FAQ).
- Device integration: "Automatically capture device data from multiple systems helping to provide near real-time data"; "charting device integration allows quick reference to accurate historical data". Driver library vendor claim: "over 420 device drivers" in one place, "over 450+" in the FAQ (inconsistent on the same page — treat as "hundreds", vendor claim), "including ventilator, infusion pumps, anesthesia machines, monitors"; "No third-party device integration needed".
- Forms builder for customizable clinical printouts (demographic, medication, vitals, labs, IV fluids); configurable templates reflecting institutional requirements.
- Preoperative assessment: "quickly build concise and completed anesthetic assessments", multi-disciplinary preoperative documentation and chart review.
- Compliance: "captures and reports core measures to regulatory and accrediting agencies and meets Joint Commission mandates for each patient encounter"; "audit readiness".
- Customer testimonial: "the most complete, legible, defendable record that you'll ever document" (medico-legal framing); "the machine is doing all the documentation".
- Suite decomposition (navigation): Preop Manager, OR Manager, PACU Manager, Anesthesia Manager, SmarTrack Next (patient tracking), Device Hub, Envision Analytics, Critical Care Manager — anesthesia is one sibling product in a perioperative suite; pre-op and PACU have their own products.

## Product C — Diane Aims (Bow Medical)

### Key observations

- Named explicitly "Anaesthesia Information Management System"; "The essential electronic anaesthetic record module for secure monitoring in operating theatres"; "digitizes anaesthesia records for use in operating theatres".
- Retrieves all data collected during preoperative assessment (Diane Poa — a separate module) so patients are tracked "throughout the anaesthesia experience".
- Manages anesthesia protocols (configurable by users, teams, departments); one-click selection of anaesthesia, surgical, and injection events from protocols.
- "Retrieve vital signs from biomedical devices and integrate data"; driver library vendor claim "over 500 drivers"; "interfaces with all the medical devices at a healthcare facility during the perioperative period".
- Decision support engine ("rules engines and decision support tools" at company level; "prescription-assistance software").
- Recovery room: "facilitates post-intervention recovery room monitoring"; "Patient discharge can be contingent on the Aldrete score or VAS score"; "Automated discharge validation and Aldrete score calculation"; real-time graphical visualization of bed availability.
- Offline-first architecture: "designed with an offline-first architecture that allows it to function even when there is no internet connection" — direct evidence that network resilience is a design requirement in this Type.
- Shared database between anesthesia and ICU departments, updated in real time; multi-workstation simultaneous access/editing.
- Print engine automating generation of reports and prescriptions; documentation written to patients' records; query engine for statistical analyses and pre-/postoperative reports.
- Deployment breadth: "operating theatres, recovery rooms, delivery rooms, and in outpatient settings".
- Regulatory: Diane platform is a class IIb digital medical device, CE-certified by notified body GMED (0459) under EU MDR 2017/745 — direct evidence that AIMS are regulated medical devices in the EU.
- Vendor claim "80% of entries are simplified down to a single click" — excluded from final doc.

## Product D — Peer-reviewed implementation study (Diane at Clinical Hospital Merkur, Zagreb)

### Key observations (Evidence layer A for the study, layer B when generalized)

- Definition sentence (literature): "Within perioperative medicine, the complexity and temporal density of anesthesia care have necessitated the development of specialized PDMSs, namely Anesthesia Information Management Systems (AIMSs). These systems extend beyond conventional documentation by enabling real-time integration of physiological data, automated recording of intraoperative events, and support for clinical decision-making, including drug dosing and event awareness."
- Paper vs electronic: paper records "characterized by limited temporal resolution and reduced clarity during periods of intensive documentation"; AIMS enable "structured, high-resolution data capture and improved accessibility of perioperative information".
- Simulated case dataset used to test documentation: induction and maintenance medication, performed procedures (endotracheal intubation, central venous catheter placement, arterial catheter placement), and physiological parameters — a concrete picture of what an anesthesia record contains.
- Decision-support usage measured for: automatic tidal volume calculator for mechanical ventilation setup, drug-dosing calculators, guidelines summary — embedded-in-workflow decision support used more than features requiring extra navigation.
- Survey dimensions: recording intraoperative events, recording administered medications, reviewing the record during and after anesthesia, documentation errors, safer anesthesia management.
- Electronic documentation significantly faster than paper in the simulation (median 540 vs 1140 s) — study-specific result; not generalized into the final document.
- Reference list points to a 2025 narrative review on EHR systems in anesthesia with "Medico-Legal Considerations" in the title — supports treating the anesthesia record as medico-legal documentation (pointer only; review not fetched).

## Product E — Epic OpTime / Oracle Health (market anchors)

### Key observations

- No public operational documentation reachable (Epic closed; Cerner wiki gated). Included only as market anchors demonstrating that the EHR-integrated module is a dominant deployment pattern in large US health systems. No product-specific claims made anywhere.

## Cross-product Comparison

| Dimension | MetaVision (iMDsoft) | Anesthesia Manager (Picis) | Diane Aims (Bow) | EHR modules (Epic/Cerner) |
|---|---|---|---|---|
| Core deliverable | complete/accurate anesthesia records | anesthesia EMR/record/charting | electronic anaesthetic record | (anchor only) |
| Organizing span | pre-op → intra-op → PACU → ICU/wards | preop → intraop → postop | pre-op (Poa) → intra-op → recovery room | perioperative module inside EHR |
| Device data capture | "hundreds of medical devices" (claim) | automatic capture, near real-time; hundreds of drivers (claim) | vital signs from biomedical devices; 500+ drivers (claim) | assumed, unverified |
| Drug documentation | one click or barcode scan; dosing templates | medication printouts/forms | one-click injection events; prescription assistance; dosing calculators (study) | unverified |
| Decision support | smart alerts on patient condition | best-practice guidelines in charting (testimonial) | rules engine; tidal-volume & dosing calculators (study) | unverified |
| PACU/recovery | post-op phase incl. pain management | sibling product (PACU Manager) | recovery-room monitoring; Aldrete/VAS discharge validation | unverified |
| Packaging | standalone platform shared with ICU | perioperative suite module | modular suite (Poa/Aims/Icu/Resus/Nicu/Pnc), modules usable independently | EHR module |
| Offline resilience | not stated | not stated | offline-first architecture (explicit) | unverified |
| Compliance/billing | billing/coding easier (quotes); reimbursement capture | core measures, Joint Commission, audit readiness | statistical reports; (French coding per iMDsoft quote for MetaVision) | unverified |
| Regulatory posture | hospital software | hospital software | CE class IIb medical device (EU MDR) | unverified |

### Cross-product commonalities (Evidence layer B)

All three evidence-bearing products, plus the peer-reviewed literature definition, converge on:

1. The anesthesia record as the central deliverable (electronic successor of the paper anesthesia record).
2. Organization around the patient's anesthetic care for a procedure, spanning pre-op → intra-op → post-anesthesia recovery.
3. Automatic capture of physiologic data from connected patient-care devices during the case (monitors, anesthesia machines, ventilators, infusion pumps).
4. Rapid provider documentation of administered drugs and clinical events (one-click/barcode/protocol-driven entry) — because documentation happens live during care.
5. Protocol/template-driven documentation, configurable per institution/team.
6. Decision support embedded in the documentation workflow (alerts, dosing aids, guideline prompts).
7. Post-anesthesia recovery (PACU) monitoring and discharge-readiness scoring.
8. Record outputs: printable/structured reports for the medical record, coding/billing, and quality/compliance reporting.
9. Multi-workstation, multi-user concurrent access to the live record.
10. Configurability as a first-class need (forms, protocols, printouts differ per institution and country).

### Divergences (candidate L2/L3)

- Packaging: standalone platform vs perioperative-suite sibling vs EHR module (L2).
- Pre-op assessment and PACU documentation: in-product phases (MetaVision, Diane) vs separate sibling products (Picis Preop Manager / PACU Manager; Diane Poa as separate module) (L2).
- Shared platform with ICU/critical care on one database (MetaVision, Diane) vs standalone (L2).
- Offline-first architecture (Diane explicit; others unstated) (L2, product-specific evidence).
- Regulatory regime: EU MDR class IIb (Diane) vs US accreditation/core-measure reporting (Picis) (L2).
- Setting breadth: delivery rooms, outpatient/office-based settings (Diane) (L2).
- Pediatrics-specific tooling (MetaVision) (L2/L3).
- Secondary use: data lake/AI, research retrieval (Bow, Hadassah quote) (L2).

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

1. **Identified patient undergoing an anesthetic for a procedure** — the anesthesia case is the organizing object (bound to a scheduled or in-progress procedure).
2. **Time-anchored anesthesia record of that case** — the electronic successor of the paper anesthesia record; the record is the deliverable.
3. **Automatic capture of intraoperative physiologic data from connected patient-care devices** (monitors, anesthesia machines, ventilators, infusion pumps), timestamped into the record during care (manual entry exists as fallback/complement).
4. **Provider-documented anesthesia actions** — administered drugs with doses, airway/procedure and clinical events — attributed to authenticated anesthesia providers.

Justification for minimality:

- Pre-op assessment and PACU documentation are NOT L0: Picis ships them as separate sibling products (Preop Manager, PACU Manager) and Bow ships pre-op as a separate module (Diane Poa); a product can be unambiguously an AIMS while pre-op/PACU live in sibling modules. The intraoperative record is the invariant center; the perioperative span is common structure.
- Billing/coding is NOT L0: it is a major adoption driver but a downstream consumer of the record.
- Decision support is NOT L0: present in all sampled products but a capability layer over documentation.
- Device capture IS L0: it is what distinguishes an AIMS from generic EHR anesthesia note templates; the literature definition centers on "real-time integration of physiological data"; every sampled product leads with device integration. Historical check: the earliest automated anesthesia record keepers were defined by exactly this automation replacing manual plotting of vitals.

### L1 — Common Mature Structure

- Pre-anesthesia assessment/evaluation documentation and anesthesia plan/protocol management.
- Medication administration documentation with dosing support (dose calculation aids, dosing templates, barcode scanning).
- One-click/rapid event documentation (induction, intubation, procedures, clinical events).
- Intraoperative alerts and embedded decision support.
- PACU/post-anesthesia recovery documentation with discharge-readiness scoring (e.g., Aldrete-style scores; VAS pain scores).
- Handoff/transfer documentation between phases (OR → PACU → ward/ICU).
- Record outputs: printable/structured anesthesia record, reports, prescriptions.
- Coding/billing support derived from the record; compliance/quality measure reporting.
- Case lists / status boards / live dashboards of patients and room/bed state.
- Multi-workstation concurrent access to the live record.
- Configuration surfaces: forms, protocols, printouts, device mappings.

### L2 — Variant / Optional Structure

- Packaging: standalone specialty platform / perioperative-suite module / EHR-integrated module / device-vendor bundle.
- Shared platform and database with ICU/critical care.
- Offline-first / network-resilience architecture.
- Device-interface breadth (vendor driver libraries; hundreds of drivers per vendor claims).
- Segment tooling: pediatrics scores/charts; obstetric settings (delivery rooms); outpatient/office-based settings.
- Regional regulatory regimes: EU MDR class IIb CE-marking; US accreditation/core-measure reporting; country-specific coding schemes.
- Secondary use: research data extraction, data lakes, AI/analytics programs, quality registries.

### L3 — Vendor-specific (Research Notes only)

- Diane: offline-first architecture; automated Aldrete/VAS discharge validation; shared anesthesia-ICU database; Posos multilingual drug database partnership; certified health hosting.
- Picis: SmarTrack Next patient tracking; Device Hub; Envision Analytics; Experior ASC suite; VA government suite; driver-library counts.
- MetaVision: MobileVision companion; pediatrics BMI charts and early-warning table; smart alerts; marketing ROI statistics.
- Vendor driver counts (420/450+/500+) and efficiency claims (80% single-click, ROI percentages) — marketing claims, excluded from the final document.

## Historical / Market-Sample Check

- The paper anesthesia record is the explicit predecessor: Picis positions itself as "just like a paper record, without the risk"; the Zagreb study compares paper vs electronic records and describes paper's limited temporal resolution. The Type's identity is "the anesthesia record, made electronic and automatic" — this holds for early automated record keepers (1980s–90s era) through current cloud-era products.
- Regional check: the sample spans US (Picis), international (iMDsoft deployments across EU/AU/IL), and French/European (Bow) products; the Zagreb study shows the same structure in a Croatian tertiary hospital. The definition does not depend on US certification regimes or on any single billing model.
- Packaging-era check: standalone AIMS (older pattern) and EHR-integrated modules (current dominant US pattern) both satisfy L0; the definition is packaging-agnostic.
- Veterinary analog exists (electronic veterinary anesthesia record, 2026) — same structural pattern, different patient domain; out of scope for this human-healthcare leaf but confirms the pattern's generality.

## Boundary Findings

- **vs Electronic Health Record (EHR)**: the EHR holds the longitudinal whole-patient chart; the AIMS holds the anesthesia dimension of care with device-integrated high-resolution capture, organized by anesthesia case. In large US deployments the AIMS is a module inside the EHR platform (Epic OpTime, Cerner) — the boundary is center of gravity, not deployment. Test: remove device capture and the anesthesia-case focus → generic EHR documentation remains; remove the longitudinal whole-patient chart → AIMS remains.
- **vs Operating Room Management**: OR management centers the operating room as a resource (scheduling, block time, staffing, turnover, supplies); AIMS centers the anesthetic care of the patient. Picis ships OR Manager and Anesthesia Manager as separate products in one suite — vendor-confirmed structural separation. Test: remove the anesthesia record → OR management remains; remove OR scheduling/throughput → AIMS remains. Flag for joint review when Operating Room Management is processed (perioperative suites bundle both).
- **vs Emergency Department Information System**: same "departmental clinical system" pattern, different department and care semantics (EDIS: triage/acuity/ED-visit lifecycle; AIMS: anesthetic care for procedures). Bow ships Diane Resus (ED) as a sibling module — same-vendor evidence of separation.
- **vs ICU/critical-care systems (no dedicated directory leaf)**: shared platforms exist (MetaVision ICU+Anesthesia; Diane Aims+Icu on one database). Sibling structure; recorded as observation, no leaf conflict.
- **vs Medication Management Platform / Electronic Prescribing**: AIMS documents intraoperative drug administration as part of the record; it does not run the pharmacy-side medication lifecycle.
- **vs Patient Scheduling / OR scheduling**: the schedule feeds the case list into the AIMS; scheduling is not the record.
- **vs Remote Patient Monitoring**: no overlap — intraoperative device capture is point-of-care documentation during an encounter, not ambulatory monitoring of patients at home.
- **vs Clinical Documentation Platform**: documentation-content tooling (templates/scribes); the AIMS is the system of record that holds and governs the anesthesia record.

## Uncertainties

- Exact record-finalization mechanics (sign-off/locking/amendment rules) could not be verified from public sources for any sampled product; the final document only asserts attribution/timestamping and the medico-legal character of the record (supported by literature pointer and vendor testimonial), with weak wording.
- Whether EHR-integrated modules (Epic/Cerner) implement device capture with the same depth as standalone AIMS could not be verified; no claims made.
- Offline behavior is directly evidenced only for Diane (product-specific); the final document marks it as a design concern that at least one product addresses explicitly, not a universal property.
- Device sample rates, exact vital-parameter sets, exact scoring implementations (Aldrete variants), and numeric limits are unverified; none are asserted.
- The relative market share of standalone vs EHR-integrated AIMS is unknown; the final document describes both as common deployment patterns without ranking them.

## Final Synthesis

An AIMS is the anesthesia department's clinical record system: it maintains the time-anchored electronic anesthesia record for each identified patient's anesthetic care for a procedure, combining physiologic data captured automatically from connected patient-care devices with provider-documented drug administrations and clinical events, attributed to authenticated providers. Around this core, mature products add pre-anesthesia assessment, protocol/plan management, dosing and decision support, PACU recovery documentation with discharge scoring, handoffs, record outputs, coding/billing and compliance reporting, and live case/status boards. The Type is packaging-agnostic (standalone platform, perioperative-suite module, or EHR module) and regulated as medical-device software in at least the EU. Its sharpest boundaries: EHR (longitudinal whole-patient chart vs anesthesia-dimension record), Operating Room Management (OR-as-resource vs anesthesia record of care), and EDIS (different departmental semantics).
