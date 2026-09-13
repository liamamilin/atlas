# Research Notes — Remote Patient Monitoring

Research date: 2026-09-09

## Research Goal

Understand what a Remote Patient Monitoring (RPM) platform actually is as an Application Type: its core objects, data flow, clinical loop, roles, rules, and boundaries against neighboring Types (Telehealth, Chronic Care Management, Patient Portal, Population Health, Home Health EHR, consumer wearables, in-facility telemetry).

## Initial Boundary

Working hypothesis before research:

- RPM = software through which care organizations monitor patients' physiological data outside the care facility (usually the home), using connected medical devices, with a clinical team reviewing the data and intervening.
- Likely confused with: Telehealth Platform (visits), Chronic Care Management (coordination), Patient Portal (patient-facing records), consumer health/wearable apps (no clinical loop), in-facility bedside telemetry.
- Unknowns: exact object model, alert/threshold machinery, device logistics depth, billing structures, EHR integration depth, staffing models.

## Research Questions

1. What are the core "things" in the system? (patient, device, reading, threshold, alert, care team, care plan, billing time)
2. How does data flow from the patient's body to the care team?
3. What does the clinical surveillance loop look like (review → alert → intervene → record)?
4. How are patients enrolled and how do devices reach them?
5. What roles exist and what does each do?
6. How does US reimbursement machinery (CPT codes) shape the product?
7. Where is the boundary vs Telehealth / CCM / Portal / wearables / in-facility monitoring?
8. What exceptions matter (missed readings, device failure, urgent escalation)?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer levels:

| Product | Philosophy | Customer level | Evidence quality |
|---|---|---|---|
| Tenovi | Hardware + API first; device data infrastructure for other RPM platforms and care orgs | RPM software vendors, care management orgs, health systems | Strong (vendor guide pages + official API docs) |
| CoachCare | Software platform + optional outsourced clinical staff; multi-program remote care (RPM/CCM/RTM/PCM) | Physician practices | Good (product/program pages) |
| CareSimple | End-to-end enterprise: cellular devices + logistics + platform + EHR-native integration + billing + optional staff | Health systems, physician groups, payers | Strong (platform pages with concrete workflow detail) |
| Biofourmis | AI-driven acute/post-acute pole: hospital-at-home, deterioration prediction, dynamic care pathways | Health systems, payers | Good (platform page) |
| Vivify Health | Enterprise RPM pioneer (Care Team Portal is an FDA 510(k)-cleared device) | Health systems | Structural evidence only — product is decommissioning (site announces platform discontinuation Aug 31, 2026; no new customers) |

## Sources

All fetched 2026-09-09.

- Tenovi — https://tenovi.com/remote-patient-monitoring-software/ ; https://www.tenovi.com/remote-patient-monitoring-dashboard/ ; https://docs.tenovi.com/ ; https://docs.tenovi.com/hwi-api/typical-dataflow/
- CoachCare — https://coachcare.com/ ; https://www.coachcare.com/programs/remote-patient-monitoring/
- CareSimple — https://caresimple.com/ ; https://caresimple.com/platform/
- Biofourmis — https://www.biofourmis.com/ ; https://www.biofourmis.com/platform
- Vivify Health — https://vivifyhealth.com/ (transition/decommission notice; footer system description)
- Attempted but failed: https://telehealth.hhs.gov/providers/best-practice-guides/telehealth-and-remote-patient-monitoring (HTTP 403). Not retried further per network-limitation rule.

## Product Observations

### Tenovi (Layer A — directly observed)

- Defines RPM software as "the platform that receives, stores, displays, and acts on patient-generated health data from connected medical devices… sits between the device in the patient's home and the clinician reviewing the reading."
- Enumerates the platform's jobs: ingest readings (BP monitors, glucometers, scales, pulse oximeters, etc.); apply thresholds and generate alerts when a reading falls outside a set range; present trends in a clinical dashboard; track time spent on care management for billing documentation; manage device inventory, shipping, replacement supplies; pass data to EHR/third-party platforms via API.
- Data flow (official API docs): device → (Bluetooth) Tenovi Gateway → cellular → Tenovi Cloud → webhook/API → customer's application (EHR, RPM platform, custom app). Cellular-enabled devices skip the gateway. Near-real-time push via webhooks.
- Fulfillment lifecycle statuses (official docs): Shipped → In Transit → Out for Delivery → Delivery Issue → Available for Pickup → Delivered → Connected (patient's first measurement) → Replaced → Unlinked (data stops, billing halted).
- Cellular Gateway model: patient plugs gateway into power; "no app to download, no account to create, no Wi-Fi to configure"; devices arrive pre-paired; LED ring reminds patient each morning (red → green once data sent).
- Self-managed vs full-service spectrum table: device procurement, storage/shipping, patient tech support, consumable replenishment, upfront cost, staff time — vendor vs in-house.
- Billing: Medicare CPT codes 99453 (initial setup/education, once), 99454 (device supply + transmission, 16+ days in 30), 99457 (first 20 min monthly care management), 99458 (each additional 20 min); vendor blog adds 99445 (2–15 days) and 99470 (10–20 min) effective Jan 1, 2026 per CY 2026 Physician Fee Schedule. Software "surfaces this eligibility automatically… which patients crossed which threshold."
- API object model: patient records (attach devices, fulfillment requests, address validation), devices/gateways, measurement data streams, webhooks, bulk orders, Automated Supply Replenishment (lancets, test strips, batteries, cuffs).
- Dashboard guidance: "shows exceptions first"; configurable thresholds; sortable patient lists; escalation paths; trend analytics; order devices and ship directly to patients.

### CoachCare (Layer A)

- Defines RPM: "collecting vital health data remotely… digital devices such as blood pressure cuffs, weight scales, pulse oximeters… securely transmitted to a central platform, enabling providers to monitor chronic conditions like diabetes, heart failure, and COPD."
- Runs multiple remote-care programs on one platform: RPM, CCM, Diabetes Care Management, RTM, PCM, BHI, AWV, VBC, APCM — "built to manage any remote care program including Medicare covered programs."
- Platform (RevCare): "one unified view of alerts, tasks, messaging, and patient activity"; consolidated patient list "prioritizes the next right task or action"; review readings, alerts, manage escalations; bulk actions; streamline billing.
- Patient side: connected devices + white-labeled patient app; reminders and text messages; patients "track vitals through our connected remote monitoring devices and intuitive app."
- RPM program features: ID qualified patients (enroll in practice or outreach services); customizable vitals at patient level + graphing; equipment distribution (ordering in the EHR, turnkey provisioning/distribution); education & engagement (multi-channel); "Clinical Monitoring & Triage — real-time vitals monitoring and escalations based on provider-defined protocols."
- CPT codes enabled: 99453, 99454, 99457, 99458 (descriptions as above).
- CareExtend: vendor's US-based clinical care team handles "every aspect of your remote care from enrollment through delivery" as an extension of the practice.
- EHR integration (Epic): service ordering, health history exchange, discrete vitals, documentation, claims.
- Explicitly recommends RPM + CCM combined ("telephonic coaching calls from staff that have access to the same condition monitoring data").

### CareSimple (Layer A)

- Positions as "one accountable vendor for devices, connectivity, logistics, software, billing, and the clinical team to run it," with "a fully controlled, end-to-end data path from the patient's home to your EHR."
- Device logistics loop (platform page): Order (clinician enrolls patient, selects device in portal) → Fulfill (Amazon-powered fulfillment, pre-activated cellular, branded kit, two-day delivery) → Track (real-time shipment tracking, delivery confirmation, automatic enrollment status update) → Monitor (patient opens box, takes reading; data transmits over cellular automatically; "no app download, no WiFi pairing").
- Inventory management: real-time visibility, automated reorder triggers, device lifecycle tracking "from deployment through retirement"; devices that go quiet "reconnect automatically."
- Clinical workflow: "condition-specific care plans, calibrated alert thresholds, and an alert triage queue — staffed by your team, ours, or any split in between."
- Alert queue examples: "BP 182/98 — sustained hypertensive episode"; "+3.2 lbs / 48h — CHF weight gain pattern"; "Glucose 248 mg/dL — trending elevation (3rd reading)"; "No reading — patient gone silent."
- Pattern-aware alerting: "Alerts detect clinical patterns — not just single out-of-range readings… Configurable by condition, cohort, and individual patient."
- Caseload framing: "When a care manager is responsible for 200 or more RPM patients, reviewing raw vitals is not sustainable… surfaces a prioritized queue."
- TriCheck: automates three sequential BP measurements and averages them per clinical guidelines.
- Condition care plans: hypertension, heart failure, diabetes, maternity, COPD, CKD; each with "calibrated alert thresholds, measurement frequency, questionnaire cadence, and escalation rules." Dexcom CGM integration (patient authorizes via SMS link).
- EHR-native: vitals as discrete structured data in Epic Flowsheets; alerts route to Epic In Basket; patients engage via MyChart; charges flow into revenue cycle. Also Oracle Health, Meditech, athenahealth, NextGen, eClinicalWorks; standalone portal and API-first deployment modes.
- Billing: "logs every clinical interaction — alert reviews, messages, care plan adjustments, data review sessions — and maps time to the appropriate CPT code automatically"; threshold compliance indicators; charges on rolling 30-day/monthly cycles; six codes tracked: 99453, 99454, 99457, 99458, 99091, 99490.
- Patient engagement: automated reminders (push for app users, SMS for non-app users); education library (videos, quizzes, articles); secure messaging and video; white-label, multilingual. "Approximately half of CareSimple patients participate successfully without downloading the app."
- Service model spectrum: Devices & Connectivity (your team runs everything) ↔ Partial managed ↔ Fully managed (CareSimple provides monitoring staff; physicians stay in the loop through the EHR).

### Biofourmis (Layer A)

- Platform loop: Collect & Aggregate (biosensor data → "unique and aggregate biomarkers that continuously represent the clinical status of the patient") → Detect & Predict (FDA-cleared algorithms generate "a personalized baseline for each patient and detect clinical deviation… predict deterioration early") → Treat & Track ("personalized interventions through a user-friendly dashboard and communication interface. Dynamic care pathways… manage, escalate, and track care") → Care & Connect (technology-enabled remote and in-home support: care coordination, nursing, diagnostics).
- Solutions: Hospital at Home, Timely Discharge, SNF at Home, Remote Patient Management — "making home the site of care."
- Device connectivity: "connects medical-grade clinical devices and sensors for physiology monitoring in homes, hospitals, and clinics"; continuous monitoring; device-agnostic; cellular.
- Patient app: "tracks daily care plan, vital signs, symptoms, and medications; facilitates virtual visits and communications with clinical teams; offers education and guidance."
- Clinician dashboard: "view notifications, communicate with patients, conduct triage, and manage medications."
- Care pathways: "70+ remote dynamic care pathways with intervention protocols such as care team outreach, vital sign checks, and symptom specific feedback."
- Clinical/in-home services: Health Navigators, RNs, advanced practitioners "evaluate and manage clinical escalations; available 24/7/365"; EMR integration includes "patient monitoring questionnaires, notifications, in-home support, and reference billing documentation."

### Vivify Health (Layer A — structural only)

- Footer system description: "Vivify Health's solution is a Remote Patient Monitoring system that consists of the Care Team Portal, patient portals, and OEM/third-party accessory devices. The Care Team Portal is an FDA 510(k) cleared medical device."
- Site announces decommissioning (platform access permanently discontinued Aug 31, 2026; no new customers). Used only to corroborate structure (care-team portal + patient portals + devices), not as a live-market sample.

## Cross-product Comparison

| Dimension | Tenovi | CoachCare | CareSimple | Biofourmis |
|---|---|---|---|---|
| Enrolled patient as anchor | Patient records anchor devices/fulfillment/data | Patient list with multi-program enrollment | Patient enrollment → device order → status tracking | Patient with personalized baseline + care pathway |
| Device-originated data stream | Core (gateway/cellular → cloud → webhook) | Connected devices → central platform | Cellular devices, automatic transmission | Biosensors → biomarkers, continuous |
| Clinical review loop | Dashboard "exceptions first", thresholds, alerts | Unified alerts/tasks view, escalations per provider-defined protocols | Alert triage queue, pattern-aware alerting, caseload mgmt | Triage dashboard, dynamic care pathways, escalation mgmt |
| Intervention | Via partner platforms (data infrastructure) | Messaging, tasks, coaching calls | Alert review, documentation, care plan adjustments | Outreach, vital sign checks, symptom feedback, 24/7 nurse escalation |
| Device logistics | Fulfillment lifecycle statuses, ASR supplies | Turnkey provisioning/distribution, ordering in EHR | Order→Fulfill→Track→Monitor, inventory lifecycle | Device inventory tools (care coordination) |
| Patient app | Not required (gateway model) | White-label app, reminders, texts | App optional (~half participate without it), SMS reminders | App: care plan, vitals, symptoms, meds, virtual visits, education |
| Symptom/questionnaire data | Not emphasized | Patient-logged vitals alongside device data | Wellness questionnaire in care plan | Symptoms + monitoring questionnaires |
| EHR integration | API/webhook delivery (FHIR discussed) | Epic: ordering, vitals, documentation, claims | Epic Flowsheets/In Basket/MyChart, charge capture | EMR integration incl. questionnaires, notifications, billing docs |
| Billing machinery | CPT eligibility surfacing | CPT 99453/54/57/58 | 6 CPT codes, automatic time logging, charge generation | Reference billing documentation |
| Staffing model | Vendor = infrastructure; org runs care | Optional vendor clinical team (CareExtend) | Your team ↔ partial ↔ fully managed | Vendor clinical network (navigators, RNs) 24/7 |
| Acuity range | Chronic (device catalog) | Chronic multi-program | Chronic + maternity + post-discharge patterns | Chronic → post-acute → acute (hospital-at-home) |
| AI | Not claimed | AI models via integration ecosystem | Pattern-aware alerting rules | FDA-cleared algorithms, personalized baselines, deterioration prediction |

Cross-product commonalities (Layer B):

1. Every product binds devices to an enrolled patient and streams device-originated readings to a clinician-side surface.
2. Every product has a clinical review surface organized around exceptions (alerts/queues), not raw feeds.
3. Every product supports configurable thresholds/parameters (per patient and/or per condition/protocol).
4. Every product treats missing readings as a first-class signal (Tenovi LED adherence nudge; CareSimple "patient gone silent"; adherence framing throughout).
5. Every product carries device logistics (provisioning, shipping, activation, replacement) as a major operational layer.
6. Every product integrates toward the EHR and/or exposes APIs.
7. Every product (where US-market) supports the RPM CPT billing loop with time capture.
8. Every product offers a patient-facing engagement surface (app/portal/reminders/education), with varying necessity (cellular models make the app optional).
9. Every product offers some form of staffing flexibility (in-house vs vendor-operated monitoring).

## Canonical Model

### L0 — Defining Invariant (three jointly-held structures)

1. **The enrolled monitored patient as anchor of record** — a patient formally enrolled in a monitoring program, located outside the care facility, with an assigned responsible care team; devices, readings, thresholds, alerts, and clinical actions all attach to this patient. Remove → anonymous device telemetry / data pipeline.
2. **Device-originated physiological data transmitted from the patient's environment** — connected medical devices capture physiological measurements (BP, glucose, weight, SpO2, heart rate, temperature, peak flow…) at the patient's location and transmit them to the care side without a clinical encounter. Remove → Telehealth (encounter-based) or CCM (coordination-based) territory.
3. **The clinical surveillance-and-intervention loop** — the care team reviews the incoming data stream against defined parameters, is alerted to exceptions (out-of-range, trending, missing readings), and intervenes with recorded clinical actions (contact, adjust, escalate). Remove → passive data logger / consumer tracker.

Jointly-held load-bearing analysis:

- 1 alone = patient roster with device telemetry (device logistics platform)
- 2 without 1+3 = device data pipeline/API (a real market role — Tenovi's HWI API alone is exactly this — but not the RPM application)
- 3 without 1+2 = generic alerting/workflow
- 1+2 without 3 = data collection program with no clinical consequence (consumer tracker with medical devices)
- 1+3 without 2 = remote care without device data (Telehealth/CCM territory)
- 2+3 without 1 = anonymous monitoring infrastructure

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Device logistics/fulfillment machinery (order, ship, activate, track, replace, unlink, supplies replenishment)
- Cellular connectivity removing patient-side setup (no app/Wi-Fi/pairing) — dominant modern realization, not required (Bluetooth+app and phone-line historical models also satisfy L0)
- Clinical dashboard/worklist organized as prioritized exception queues; caseload management for large panels
- Threshold/parameter configuration (per patient, per condition protocol); pattern-aware alerting (trends, sustained episodes, weight-gain patterns)
- Patient engagement surface (app/portal, reminders, education, secure messaging, sometimes video)
- Symptom surveys/questionnaires alongside device vitals
- Condition-specific care plans/protocols
- Time capture and billing support (US CPT machinery)
- EHR integration (vitals into flowsheets, alerts into clinician inbox, charges into revenue cycle) and/or APIs
- Adherence monitoring (missed-reading alerts, reminder escalation)
- Multi-role model: care manager/RN (primary reviewer), physician (escalation/oversight), ops/admin (logistics), billing staff

### L2 — Variant / Optional Structure

- Program scope: chronic disease management (HTN, diabetes, CHF, COPD, CKD) vs maternity vs post-acute/post-discharge vs acute hospital-at-home vs SNF-at-home
- Service model: self-managed ↔ partial ↔ fully managed monitoring (who staffs the surveillance loop)
- Hardware model: vendor-issued cellular kits vs Bluetooth+gateway vs BYOD/patient-owned (CGM authorization) vs historical phone-line transmission
- Payer context: US fee-for-service CPT billing vs value-based/payer programs vs non-US systems without RPM-specific billing
- Data breadth: vitals only vs vitals + symptoms + medications + education + virtual visits
- Acuity: stable chronic vs post-discharge vs acute (continuous monitoring, deterioration prediction)

### L3 — Vendor-specific (research notes only)

- Tenovi: Cellular Gateway hardware with LED adherence ring; HWI API object model (patients, devices, gateways, measurement streams, webhooks, bulk orders); ASR (Automated Supply Replenishment) API; fulfillment status vocabulary (Shipped→…→Connected→Replaced→Unlinked).
- CareSimple: TriCheck (three sequential BP measurements averaged per clinical guidelines); Epic Toolbox designation; Amazon-powered fulfillment; six-code billing automation (99453/54/57/58/99091/99490).
- Biofourmis: FDA-cleared AI algorithms; personalized vitals baselines; digital biomarkers; 70+ dynamic care pathways; 24/7 vendor-staffed clinical escalation network; hospital-at-home/SNF-at-home program shapes.
- CoachCare: RevCare/RevConnect/RevUp product branding; 400+ managed conditions; multi-program engine (RPM/CCM/RTM/PCM/BHI/AWV/APCM on one platform).
- Vivify: Care Team Portal as FDA 510(k)-cleared medical device.

## Vendor-specific Findings

See L3 above. None of these enter the canonical core. Notably, Tenovi's own materials show the market separates the device-data infrastructure role (API-first) from the clinical RPM application role — the same Type is realized as a layered stack, with some vendors selling only a layer.

## Boundary Findings

| Neighboring Type | Relationship | Distinction (what to remove from RPM to become the other) |
|---|---|---|
| Telehealth Platform | adjacent, commonly bundled | Remove the device-originated physiological data stream and the continuous surveillance loop; keep the synchronous encounter → Telehealth. RPM products commonly bundle video visits; telehealth products commonly add device data. The seam is encounter vs continuous device data. |
| Chronic Care Management | sibling program, same platforms | Remove the physiological device data; keep care-plan-driven coordination and time-based services → CCM. CoachCare documents both as separate programs on one platform and explicitly bundles them; the data object (device vitals vs coordination time) is the seam. |
| Patient Portal | different primary user | The portal's primary surface is patient-facing access to records/messages; RPM's primary surface is clinician-side surveillance. RPM patient apps are engagement surfaces of the program, not the defining surface. |
| Consumer wearable / fitness tracker | adjacent, often confused | Remove enrollment, the responsible care team, clinical thresholds, and intervention accountability → consumer tracker. Medical-grade devices + clinical loop are the seam. |
| In-facility telemetry / bedside monitoring | different setting | Remove the distance (patient outside the facility) → in-facility monitoring. RPM is defined by the patient's own environment. |
| Home Health EHR / agency management | different unit of work | Home health organizes episodic visits/assessments per agency operations; RPM organizes continuous data surveillance per enrolled patient. |
| Population Health Management | consumer of RPM data | Population health works at registry/panel level with attribution and gap closure; RPM works at person level with a continuous data stream. |
| ePRO / eCOA | different context | Trial/protocol-driven patient-reported data capture vs clinical-care device surveillance. |
| RTM (Remote Therapeutic Monitoring) | sibling US billing category | RTM targets therapy/adherence data (non-physiological); appears in-sample as a separate program on the same platform (CoachCare). Recorded as adjacent category, not merged. |

Historical / market-sample check: early home-telemonitoring programs (phone-line transmission of home BP/weight/glucose to a nurse station; nurse-led heart-failure telemonitoring in European systems; VA-style home telehealth) satisfy all three L0 legs with no cellular, no apps, no AI, no CPT codes. The definition therefore does not over-fit the current US cellular-kit + CPT implementation.

## Uncertainties

- CPT code details (including the claimed 2026 additions 99445/99470) come from vendor pages citing CMS; the HHS/CMS primary pages were not reachable (403). Billing specifics are therefore recorded as US-market machinery with vendor-sourced descriptions, not verified against primary regulation. The final document deliberately keeps billing at the conceptual level (time capture, eligibility thresholds, charge capture) without asserting exact code values as canonical.
- Non-US RPM products were not directly sampled; the sample is US-heavy. The clinical loop is assumed universal (supported by the historical check), but non-US product naming/structure is unverified.
- Vivify Health is decommissioning; used only as structural corroboration.
- Whether "RPM" and "Remote Patient Management" (Biofourmis's term) represent one market or two subtly different categories was not resolved; treated as one Type with an acuity variant axis.
- RTM's exact boundary (therapy data vs physiological data) is described from one vendor's program taxonomy; recorded as adjacent, not fully researched.

## Final Synthesis

A Remote Patient Monitoring platform is the clinician-side system of record for monitoring enrolled patients outside the care facility through device-originated physiological data. Its defining core is three jointly-held structures: the enrolled monitored patient (anchor to which everything attaches), the device-originated physiological data stream transmitted from the patient's environment, and the clinical surveillance-and-intervention loop (review against parameters → alert on exceptions → intervene and record). Everything else — cellular kits, patient apps, fulfillment logistics, condition protocols, EHR-native integration, CPT billing automation, AI deterioration prediction — is common mature structure, variant machinery, or vendor-specific detail layered on that core. The Type sits between Telehealth (encounter-based, no continuous data) and Chronic Care Management (coordination-based, no physiological data), and is distinct from consumer wearables (no clinical loop) and in-facility monitoring (no distance).
