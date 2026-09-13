# Research Notes — Emergency Department Information System (EDIS)

Research date: **2026-09-07**
Methodology: update-v1 WORKFLOW/WRITING_GUIDE v1.1

---

## Research Goal

Understand, from real products and the supporting literature, what an Emergency Department Information System is, what objects and state it manages, how work flows through it, which rules and behaviors define it, and where its boundaries lie against the hospital EHR, patient flow / bed management, and prehospital EMS systems.

---

## Initial Boundary (pre-research hypothesis)

- Core hypothesis: EDIS = department-scoped clinical information system for hospital emergency departments; heart = real-time patient tracking (digital whiteboard) + triage/acuity + visit-anchored documentation/orders/results + disposition.
- Neighbors to differentiate: EHR (hospital-wide longitudinal record), Patient Flow Management (hospital-wide movement), Bed & Capacity Management (enterprise bed allocation), Patient Registration & Intake, EMS Operations Platform / ePCR (prehospital), Patient Portal, CPOE, Clinical Documentation Platform.
- Known unknowns: exact board semantics per product; how admission/boarding handoff is modeled; regional triage scale realizations; whether "tracking board" is definitional or merely common (early/regional systems sometimes lacked live tracking — see Product C).

---

## Research Questions

1. What is the unit of record? Is the ED visit distinct from the longitudinal patient chart?
2. What does the patient tracker/board show; what state changes does it reflect?
3. What does the triage step record; how is acuity used?
4. Which clinical content is native vs provided through integration with a host EHR/HIS?
5. How does disposition work; how is the admission/boarding handoff handled?
6. Which time-stamped milestones and throughput metrics exist (door-to-provider, LOS, LWBS)?
7. What rules matter: unknown identity, re-triage, documentation→level-of-care billing, access control?
8. What interfaces exist beyond the board?
9. What variants exist: standalone vs EHR-module vs HIS-subsystem; tracking-first vs comprehensive; regional scales?
10. Would older / regional / partial-function products still fit the definition?

---

## Representative Products (research sample)

| Product | Realization | Evidence strength | Access |
|---|---|---|---|
| MEDITECH Expanse Emergency Department Management | ED module of mid-market enterprise EHR (North America incl. Canada) | A — official product page + official blog | Fetched |
| Academic medical center EDIS (large US academic ED, ~101k visits/yr; vendor not named in study) | Comprehensive standalone EDIS with heavy HIS integration | A via peer-reviewed usability study | Fetched (PMC) |
| Regional EDIS deployments — Kowsar, Pouya Samaneh Diba, Hamedan Sayan Rayan Ekbatan, Rayavaran Toseeh (11 teaching hospitals, Iran) | Standalone or HIS-subsystem EDIS, partial EDIS-FP conformance | A via peer-reviewed conformance study (regional sample — useful §24 check) | Fetched (PMC) |
| HL7 EDIS Functional Profile (Emergency Care SIG, 2007) | Neutral functional standard for the Type | Standard-based anchor | Accessed via secondary literature |
| Epic ED module / Oracle Health (Cerner) FirstNet / MEDHOST EDIS / PulseCheck | Large-enterprise and specialist realizations | Not directly researched — see Source-access Limitations | Not accessible |

Sampling rationale: one modern suite ED module (official docs), one comprehensive historical standalone EDIS (US academic), one regional cluster of standalone/subsystem products (Middle East) — deliberately spanning eras, geographies, and deployment postures to avoid over-fitting to the current North-American EHR-module pattern (§24 check).

---

## Sources

Fetched successfully:

1. MEDITECH — "Expanse Emergency Department Management" product page — https://ehr.meditech.com/ehr-solutions/meditech-ed (researched 2026-09-07)
2. MEDITECH blog — "MEDITECH customers create efficiencies to address emergency department utilization" (Feb 2025; ED MAPP pre-booking pathway; CTAS five-level acuity; low-acuity diversion) — https://blog.meditech.com/meditech-customers-create-efficiencies-to-address-ed-utilization
3. Saghaeiannejad-Isfahani S, Hazhir F, Jalali R. "An assessment of emergency department information systems based on the HL7 functional profile." J Educ Health Promot. 2019;8:26. PMC6432815 — EDIS-FP structure (direct care / supportive / information infrastructure), full function inventory, conformance results for 4 regional EDIS products. — https://pmc.ncbi.nlm.nih.gov/articles/PMC6432815/
4. Kim MS, Shapiro JS, Genes N, et al. "A pilot study on usability analysis of emergency department information system by nurses." Appl Clin Inform. 2012;3(1):135–53. PMC3613014 — Mount Sinai EDIS system description, role differentiation, full nurse task workflow entry→disposition. — https://pmc.ncbi.nlm.nih.gov/articles/PMC3613014/
5. Bienzeisler J, et al. "The Effects of Displaying the Time Targets of the Manchester Triage System to Emergency Department Personnel." J Med Internet Res. 2024;26:e45593 (PMC11134237) — title-level confirmation that MTS time targets operate in ED IT contexts (used only to evidence regional triage scales / time targets).

Referenced but not fetched (cited within sources above):

6. Rothenhaus T, et al. "Emergency Department Information Systems: primer for Emergency Physicians, Nurses and IT Professionals." ACEP/AMIA/AAEM/HIMSS 2009 — original URL (acep.org workarea) returns 404; cited as evidence the professional community defines EDIS as a distinct system category.
7. Landman AB, et al. "Emergency department information system adoption in the United States." Acad Emerg Med. 2010;17:536–44.
8. Callen J, et al. "Does an integrated emergency department information system change the sequence of clinical work?" Int J Med Inform. 2014.

Source-access Limitations (failed attempts, per network-restriction rule — 1–2 attempts each then abandoned):

- medhost.com / www.medhost.com — transport errors (×2) → MEDHOST EDIS not directly researched.
- www.epic.com/software — 403 → Epic ED module not directly researched.
- www.oracle.com/health/emergency-department/ — 404; Oracle Health root page contains no ED-specific operational content → Cerner FirstNet not directly researched.
- www.intersystems.com (TrakCare) — request timeout.
- www.alterahealth.com (Sunrise) — 503.
- www.tido.com (tracking-first vendor) — transport error.
- acep.org — 404 on both attempted EDIS URLs.
- DuckDuckGo HTML — timeout; Bing — results polluted/unusable for these queries (search engines abandoned after 2 attempts).
- PubMed/PMC E-utilities — worked (used to locate sources 3–5).

Consequence: all statements about large-enterprise ED modules (Epic, Oracle Health FirstNet) and specialist vendors (MEDHOST, PulseCheck) are drawn only from general market knowledge for identification purposes; **no operational, workflow, or rule claims in this research or the final document are based on those vendors**. Assertion strength is calibrated accordingly.

---

## Product A — MEDITECH Expanse Emergency Department Management (official, Tier 2)

Key observations (evidence layer A — direct from vendor page):

- **Patient tracker is the operational center**: "Quickly see patient location, triage, chief complaint, alerts, and more in the tracker, and launch order routines with one click." Screenshots include a "patient tracker" and a separate "waiting room" view.
- **Triage documentation**: "Streamline triage process for quick documentation of patient details — like location, complaints, screenings, allergies, home meds and more."
- **Nurse role views**: "Customize views for nurses … instantly allowing them to see pending tasks, medications, and assessments"; AI-generated handoffs at care transitions.
- **Leadership/department view**: "Monitor a timely, comprehensive … overview of the department, maximizing throughput"; "Assess patient volume and acuity, optimize resources, and manage wait lists to reduce overcrowding."
- **One record across settings**: "one complete patient record across ED, acute, and ambulatory environments."
- **Care-coordination flow**: nurses collect/enter info → stored for discharge; physicians place orders/referrals/instructions before next care transition; generative AI hospital-course summary at discharge; discharge instructions/education auto-available on patient portal; documentation pushed to connected network providers.
- **Reporting**: "Measure ED throughput, volumes, and much more, using our Business and Clinical Analytics tools … ability to directly drill down into patient details."
- Mobile technology positioning ("intuitive mobile technology").
- Official blog adds (Canada): ED "Minor Ailment Patient Pathway" — patients self-book same/next-day ED slots online and are rerouted into a designated treatment area (pre-arrival booking variant); CTAS described as "a five-level system used to prioritize patients based on the severity of their condition" (regional triage scale evidence).

---

## Product B — Academic medical center EDIS (Mount Sinai; vendor unnamed in study)

Key observations (evidence layer A via peer-reviewed study):

- **System composition**: "combines triage, patient tracking, physician and nursing documentation, risk management, charge management, integrated voice recognition, prescription writing"; includes "physician and nursing documentation, computerized provider order entry (CPOE), results retrieval, a print-on-demand electronic prescribing solution, various modules of clinical decision support".
- **Integration posture**: "through the creation of 14 electronic interfaces, comprehensive integration with hospital systems including registration, laboratory, and hospital electronic data repository"; browser-based.
- **Workflow span**: tasks "spanned from the entry of the patient through door to final disposition decision (i.e. discharge or hospital admission)."
- **Role differentiation**: "only expert nurses perform triage, and were therefore allowed to complete 'triage nurse tasks', while both expert and novice nurses complete 'primary nurse tasks'."
- **Nurse documentation tasks** (complete task lists): allergy/current meds; past medical/surgical/social history; structured nursing assessments by body system (abdomen, upper extremity — pain site/quality/scale, nausea/vomiting, tenderness, etc.); procedure documentation with time (pelvic exam, wound care incl. anesthesia/irrigation/suture details); diagnostic test ordering (bedside tests, labs, radiology with ordering physician); result documentation (bedside testing results, imaging results); medication follow-up (adverse-effect documentation); **admission pathway** (admission time, procedure, transportation) and **discharge pathway** (discharge instructions, prescriptions, return instructions).
- **Documentation → billing**: "Accurate emergency nursing documentation is essential for continuity of care, patient safety and for hospital ED reimbursement by determining the ED level of care."
- Consult pathway (surgery consult → admitted to service → OR) handled inside the workflow.
- Implementation preceded by clinical workflow/process redesign; sustained customization.

---

## Product C — Regional EDIS deployments (4 systems, 11 Iranian teaching hospitals)

Key observations (evidence layer A via conformance study; systems are regional and partially conformant — valuable historical/regional check):

- Deployment forms: standalone EDIS or subsystem of the hospital information system.
- Supported (across the studied systems): quick ED patient registration; **"Creating an individual record for all the patients even for those whose identity is unknown"**; demographic capture/edit; structured + unstructured clinical documentation; viewing previous patient records; drug orders + diagnostic test orders with details; **tracking order status and retrieving results**; vital signs capture; allergy capture; **recording patient status (admission, discharge, or transfer)**; comprehensive triage assessment data; discharge instructions; emergency diagnoses; ED-patient-transfer legal documentation; CDS (patient-identification display, waiting-list display for physician examination, allergy/contraindication warnings, templates); task lists; communication recording; user/access management; **recording the exact time of ED admission; identifying and updating the patient's current real-time location; displaying/updating triage time, admission time, in-room time, discharge time; managing ED rooms; displaying empty beds ready for admitted patients**; reports (patient records; **key ED reports: admissions count, bed occupancy rate, length of stay, number of patients who left without physician examination or before completing treatment**); financial/administrative data exchange; per-visit data organization; coding support.
- Weaknesses observed (deployment realities, not type definition): no accurate live tracking monitor in these deployments (only room/bed number display); incomplete clinical decision support; no external health-center exchange; paper records used alongside.
- The study also cites the US NHAMCS 2011 survey of ED electronic-system functions (order entry, drug-interaction warnings, demographics, problem lists, medication/allergy lists, guideline reminders, visit summaries, electronic exchange) — EDIS functionality is measured against a common federal-standard function set.

---

## Standard anchor — HL7 EDIS Functional Profile (Emergency Care SIG, 2007)

- EDIS-FP organizes EDIS functions into: **Direct care** (Care management; Clinical decision support; Operations' management and communications) + **Supportive** (Clinical support; Measurement, analysis, research and reports; Administrative and financial) + **Information infrastructure** (security, terminologies, interoperability).
- The profile contains hundreds of "shall" (essential) conformance criteria — i.e., the emergency-care informatics community treats EDIS as a well-bounded Type with a known function set.
- The profile itself confirms as essential: unknown-identity individual records, location tracking, milestone time stamps (triage/admission/in-room/discharge), room management, order/result status tracking, triage assessment, disposition status recording, waiting-list display, key throughput reports (incl. left-without-being-seen-class outcomes), coding/accounting support.
- Canonical definition circulating in this literature: "an electronic health record system specially developed for the management of information and workflow, supporting the patient care in the ED and emergency operations"; "can be implemented either as a subsystem of the hospital information system or a standalone system."

---

## Cross-product Comparison

| Structure / capability | MEDITECH Expanse ED | Academic EDIS (B) | Regional systems (C) | EDIS-FP standard | Judgment |
|---|---|---|---|---|---|
| ED visit record from arrival, per-visit organization | Y | Y | Y | essential | **L0** |
| Time-stamped milestones (arrival/triage/in-room/discharge) | implied (throughput, wait lists) | Y (admission time etc.) | Y (triage/admission/in-room/discharge times) | essential | **L0** (concept), exact milestone set = L1 |
| Per-patient tracking state (location/room/bed + status) | Y (tracker: location, triage, complaint, alerts) | Y (patient tracking) | Y-minimal (room/bed display only) | essential | **L0** (concept: tracked location+state); full live board = L1 |
| Department-level aggregate view / wait list | Y (tracker, waiting room, leadership overview, wait lists) | Y (waiting list via CDS) | Y (waiting-list display) | essential | **L0** (department-level coordination surface) — minimal forms vary |
| Triage step + acuity assessment | Y | Y (triage nurse role) | Y (comprehensive triage data) | essential | **L0** |
| Structured nursing + provider documentation | Y | Y | Y (partial) | essential | L0-clinical-content / L1 depth |
| Orders (CPOE) + results retrieval/status | Y (order routines, one click) | Y | Y | essential | L0-clinical-content |
| Disposition recorded (discharge/admission/transfer) | Y (care transitions) | Y (admission/discharge pathways) | Y | essential | **L0** |
| Discharge instructions (patient-facing) | Y (portal push) | Y | Y | essential | L1 (common mature) |
| Bed/room management + empty-bed views | Y (resources optimization) | not stated | Y | essential | L1 (common) |
| CDS (allergy/interaction warnings, templates) | Y (predictive analytics, alerts) | Y | partial | essential | L1 |
| Throughput/volume/LOS/LWBS reporting | Y (throughput, volumes, drill-down) | implied (operational efficiency) | Y (incl. LWBS-class report) | essential | L1 (common; metric names vary) |
| Charge management / coding support | Y (revenue cycle suite around it) | Y (charge management) | Y | essential | L1 (common) |
| Integration with HIS (registration/lab/radiology/billing/data repository) | Y (one record across ED/acute/ambulatory; portal; network providers) | Y (14 interfaces) | Y (subsystems) | essential (infrastructure) | L1 mechanism, L0 prerequisite when documentation is not native |
| One longitudinal record across ED/inpatient/ambulatory | Y | partial (data repository) | partial (viewing previous records) | — | L1 (maturity continuum) |
| Pre-arrival booking / minor-ailment pathways | Y (customer deployment) | — | — | — | L2 workflow variant (regional) |
| Voice recognition / scribe support | Y (ambient/AI positioning) | Y (integrated voice recognition) | — | — | L2 optional |
| Board-specific: admission-decision patients retained on board ("boarding") | implied (care transitions) | Y (admission pathway incl. transportation) | implied (status = admitted, empty beds for admitted) | — | L1 (common; hospital-ED contexts only) |
| Regional five-level triage scales (CTAS Canada, MTS Europe; ESI in US) | Y (CTAS evidence) | — | — | — | L2 (regional realization) |

Stop conditions reached: core model, main workflows, stable commonalities, and boundaries are clear; further products would mostly repeat evidence (large-enterprise modules are additionally inaccessible — recorded limitation, not hidden uncertainty).

---

## Canonical Model

### L0 — Defining Invariant (minimal)

The EDIS is a **department-scoped system of record for unscheduled emergency care**. Four structures; remove any one and it stops being an EDIS:

1. **The ED visit as the unit of record** — a record created at the patient's arrival that carries that single unscheduled visit through time-stamped milestones to a recorded terminal disposition (discharge, admission, transfer, or departure without completing care). Remove → scheduling/clinic-management software (planned encounters) or a generic longitudinal chart.
2. **Department-level tracking state** — each visit holds current, updateable location/room/bed, care stage, acuity, and staff assignments as shared departmental state used by the whole team to coordinate; surfaced at minimum as location + status (the digital descendant of the ED whiteboard; mature form = live department board). Remove → generic charting with no departmental coordination surface.
3. **Triage-driven prioritization** — a managed triage step producing a structured acuity assessment that orders who is seen/worked next, with a visible waiting population. Remove → first-come-first-served clinic model.
4. **Visit-anchored clinical content** — documentation, orders, and results retrieval attached to the visit (native modules or provided via host EHR/HIS integration), supporting coding of the visit's level of care. Remove → a pure tracking display / whiteboard-replacement utility (a component, not the information system).

### L1 — Common Mature Structure (common, not definitional)

- Live department board with configurable columns, acuity color-coding, elapsed-time indicators; waiting-room view.
- Full milestone timer set (door-to-triage, door-to-provider, door-to-disposition) and throughput analytics (volumes, LOS, LWBS-class outcomes) with drill-down.
- Bed/room management with availability views; assignment workflows; wait-list management.
- Structured nursing flowsheets by body system; provider notes/templates; procedure documentation; medication administration records with follow-up.
- CDS: allergy/contraindication/interaction warnings, order sets/routines, templates, guideline prompts.
- Discharge instructions with patient-portal delivery; care-transition handoffs; documentation pushed to network providers.
- Charge capture / coding support for ED level of care.
- Integration spine: registration, laboratory, radiology, billing, enterprise data repository, patient portal; identity continuity into the longitudinal record.
- Role-scoped views (triage nurse / primary nurse / provider / charge nurse / leadership).
- Boarding view: patients with an admission decision remaining on the ED board until physical handoff.

### L2 — Variant / Optional Structure

- Deployment posture: standalone EDIS vs module of an enterprise EHR (dominant modern North-American pattern) vs HIS subsystem (regional pattern).
- Regional triage scale realizations (CTAS, MTS, ESI and others; five-level scales common — the scale itself is regional, not definitional).
- Pre-arrival machinery: online self-booking for minor ailments; pre-arrival EMS notification.
- Voice recognition, scribe integration, ambient/AI documentation.
- Freestanding / urgent-care ED contexts (no boarding).
- Mass-casualty/incident support modes (literature documents MCI stress scenarios; not researched in depth here).

### L3 — Vendor-specific Structure (kept out of the final document)

- Branded module names and positioning ("Emergency Department Management", "FirstNet", "ED Floor"-style whiteboard products).
- Specific AI offerings (ambient documentation, AI hospital-course summaries), specific analytics suites, specific portal brands.
- Customer-specific pathways (a named hospital's online minor-ailment booking portal).
- Precise conformance percentages from the regional study (49.72%/75.25%/53.15%) — study-specific numbers, not type facts.

---

## Vendor-specific Findings

- MEDITECH: "order routines with one click" from the tracker; AI-generated handoff text; generative-AI hospital-course summary at discharge; ED MAPP customer pathway (Royal Victoria Regional Health Centre); MaaS/AI positioning.
- Mount Sinai EDIS: 14-interface integration architecture; print-on-demand e-prescribing; integrated voice recognition; risk-management module; implementation preceded by formal process redesign; macro-based documentation templates (documented usability friction).
- Regional systems: individual product names (Kowsar, Pouya Samaneh Diba, Hamedan Sayan Rayan Ekbatan, Rayavaran Toseeh); conformance percentages; missing live tracking in those specific deployments.
- MEDITECH blog: customer-specific virtual-care numbers (visit reductions, booking counts) — marketing/customer data, not type structure.

---

## Boundary Findings

| Neighbor | Relationship | Distinction | "Remove …" criterion |
|---|---|---|---|
| Electronic Health Record (EHR) | overlapping / hosting | EHR = enterprise-wide longitudinal record across all care settings. EDIS = the ED department's visit-scoped operational system; the tracker and visit lifecycle are its center. Modern EDIS are frequently EHR modules — the relationship is containment, not equivalence. | Remove the ED department scoping and the visit lifecycle → generic EHR charting. Remove the longitudinal/enterprise record and keep only the ED visit → EDIS. |
| Patient Flow Management | adjacent downstream | Patient flow platforms manage movement across the whole hospital (transfer centers, enterprise bed assignment, EVS/transport orchestration). EDIS ends (or hands off) at the admission decision + physical bed handoff; its tracking is within-ED. | Widen the tracked geography from the department to the enterprise → Patient Flow Management. |
| Bed & Capacity Management | adjacent | Enterprise bed allocation/housekeeping is upstream of the ED handoff; EDIS needs only room/treatment-space state inside the department (empty-bed visibility is a common integration, not the EDIS's core). | Remove the visit-lifecycle/clinical center and keep enterprise beds → Bed & Capacity Management. |
| Patient Registration & Intake | overlapping capability | Enterprise registration/admission is a capability EDIS consumes or embeds ("quick registration" is ED-specific: unscheduled, speed-critical, provisional identity). | Standalone pre-arrival/registration scope → Patient Registration & Intake. |
| EMS Operations Platform / ePCR | adjacent upstream | Prehospital systems record care before arrival and hand off to the ED. EDIS begins at arrival (optionally consuming pre-arrival data). | Move the unit of record to the prehospital scene response → EMS operations Type. |
| Patient Portal | adjacent output | Portal is the patient-facing output surface (instructions, education); no departmental operations. | — |
| CPOE / Clinical Documentation Platform | capability vs system | Ordering and documentation are capabilities EDIS must offer natively or via the host EHR; standalone CPOE/documentation products are not departmental operating systems. | Remove the visit/tracking/triage frame → generic CPOE/documentation. |
| Telehealth Platform / virtual triage | adjacent | Pre-ED digital navigation (symptom triage, redirection) sits outside the EDIS; the MEDITECH blog examples are customer additions, not the EDIS core. | — |

Taxonomy note: "Emergency Department Information System" in the directory sits among hospital department systems (OR management, anesthesia, nursing systems). No evidence was found that the leaf is an alias or mere variant of EHR: the type has its own functional standard (HL7 EDIS-FP), its own adoption literature, and its own vendor categories. It is a legitimate Type; the EHR-module relationship should be reflected as a realization variant, not a merge.

---

## Historical / Market-Sample Check (§24)

- Would the definition still hold for older / regional / partial-function products? **Yes**: the 2003–2004 academic EDIS (tracking + documentation + CPOE + charging, pre-smartphone, browser-based), and 2010s regional standalone/subsystem systems with only room/bed-number tracking and paper coexistence, all satisfy the four L0 structures in minimal form. The L0 deliberately abstracts "live board" to "department-level tracking state" precisely because full live boards were not universal.
- Paper-era EDs (whiteboard + paper chart) are the pre-digital predecessor: the whiteboard's columns (name, complaint, acuity, room, doctor, status, times) map one-to-one onto the L0 tracking state — strong evidence the abstraction is not an artifact of current products.
- The five-level acuity scale is common (CTAS/MTS/ESI) but treated as a regional realization; triage-with-prioritization remains the invariant, not any specific scale.

---

## Uncertainties

1. **Large-enterprise module semantics** (Epic, Oracle Health FirstNet): official operational documentation was not accessible; whether they model e.g. boarding, result-status, or assignment state exactly as inferred is unverified. Mitigated by not making claims about them.
2. **Boarding state modeling**: the admission-decision-patient-still-on-board pattern is directly evidenced only in Product B's admission pathway and implied in C and A; treated as common (L1), not definitional.
3. **Exact milestone metric sets** (which timers are standard): the full door-to-X timer set is industry-typical but was directly evidenced only in the regional sample (triage/admission/in-room/discharge times) and implied by throughput reporting elsewhere; final document keeps milestone names illustrative.
4. **PulseCheck/MEDHOST lineage** (acquisition history): could not be verified without search engines; excluded entirely from claims.
5. **Freestanding ED / urgent-care EDIS depth**: not directly researched; variant claims kept generic.
6. **Re-triage on deterioration**: clinically expected and plausibly supported everywhere, but no direct evidence captured — omitted from the final document's rules rather than asserted.

---

## Final Synthesis

An EDIS is the emergency department's own system of record: a visit-scoped clinical and operational application whose defining core is (1) the ED visit record carried from arrival through time-stamped milestones to a recorded disposition, (2) shared department-level tracking state per visit (location, stage, acuity, assignments) surfaced for whole-team coordination, (3) triage-driven prioritization of the waiting population, and (4) visit-anchored clinical content (documentation, orders, results, discharge instructions) supplied natively or through host-EHR integration, supporting level-of-care coding. Everything else — live boards with timers, bed/room management, CDS, charge machinery, analytics, portals, AI — is common mature structure or optional/variant machinery layered on this core. The type is distinct from, and usually hosted by, the hospital EHR; it hands off to patient flow/bed management at the admission decision and receives from EMS at arrival.
