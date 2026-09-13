# Research Notes — ePRO / eCOA Platform

Research date: 2026-09-07
Slug: epro-ecoa-platform (DIRECTORY leaf: "ePRO / eCOA Platform", Domain 22 Healthcare & Life Sciences)

## Research Goal

Understand what an ePRO/eCOA platform actually is as an Application Type: what objects it manages, who uses it, how a study is configured and run, what compliance machinery it carries, and where its boundaries sit against Electronic Data Capture (EDC), survey platforms, remote patient monitoring, and patient engagement products. Produce a vendor-neutral Application Document whose defining core is minimal and historically robust.

## Initial Boundary

Working hypothesis before research:

- Core use: electronically administering clinical outcome assessments (validated questionnaires, rating scales, diaries) to trial subjects and raters, on a protocol-defined schedule, for a regulated study.
- Users: sponsor/CRO study teams (configure, monitor), site staff (oversee, support), clinicians/raters (ClinRO), patients/caregivers (PRO/ObsRO).
- Nearest neighbors: Electronic Data Capture (site staff enter CRF data — the "who enters" boundary), Survey/Questionnaire platforms (no protocol schedule, no regulatory record, no instrument licensing), Remote Patient Monitoring (care context, device-measurement-first), Patient Engagement Platform (broad communication), IRT/RTSM (randomization/supply), CTMS (operations).
- Unknowns: how scheduling/compliance is modeled (windows, reminders), whether ClinRO is first-class or peripheral, whether "platform" implies DCT-broad suites, what lifecycle states exist, degree of integration with EDC.

## Research Questions

1. What is the object model: study, subject, instrument, schedule, completion window, reminder, response record, alert, query, device?
2. How does a study get configured (instrument selection/licensing, branching/scoring logic, translations, validation)?
3. How does a subject complete an assessment (modalities: app, web, provisioned device, BYOD; offline; reminders)?
4. How do site/sponsor users monitor compliance and manage safety alerts and data review?
5. What regulatory machinery exists (audit trail, attribution, timestamps, Part 11/Annex 11/GCP, CSV, equivalence to paper)?
6. What is the lifecycle of an instrument assignment and of the study (amendments)?
7. Where are the boundaries vs EDC, survey tools, RPM, engagement platforms?

## Representative Products

Selected for market representation + different product philosophies + different customer tiers + documentation reachability:

| Product | Philosophy / position | Tier |
|---|---|---|
| **Signant Health** (SmartSignals eCOA) | science-and-services specialist; eCOA science teams, scale licensing, rater training, global helpdesk/logistics | enterprise sponsor/CRO |
| **Clario** (eCOA; now part of Thermo Fisher) | endpoint-technology breadth (eCOA + cardiac/imaging/respiratory/motion); device fleets, connected sensors, therapeutic-area specialization | large pharma / global |
| **THREAD** | no-code DCT platform; eCOA + eConsent + telehealth + eCRF/eSource in one configurable platform; strong services layer (licensing, translation, provisioning) | mid/large sponsor, CRO, DCT/hybrid |
| **Medable** | developer/platform-first DCT substrate (Cortex API); apps built on org/account/notification/audit infrastructure | enterprise, developer-led |

Considered and dropped:

- **Castor** (self-serve EDC suite with ePRO module; would have covered the academic/biotech self-service tier) — help center transport error + two product-page 404s on 2026-09-07; dropped per source-access rules. Its EDC positioning is documented in the same-day sibling EDC research, but no ePRO-specific claims are made here.
- **Veeva Vault ePRO, Medidata (Rave ePRO), YPrime, CRF Health/Exco (legacy)** — not fetched; noted as unverified market context only.
- **REDCap** — survey/EDC hybrid often used for simple PRO capture in academic settings; not fetched; relevant only as boundary context.

## Sources

All fetched 2026-09-07. Evidence layer per §23 notation: [A] = directly observed on that product's official page; [B] = cross-product commonality; [C] = canonical inference.

- Signant Health — eCOA solution page: https://signanthealth.com/solutions/ecoa [A]
- Signant Health — Getting Started with eCOA (six how-to guides, in-house eCOA scientists): https://signanthealth.com/resources/getting-started-with-ecoa [A]
- Clario — eCOA Clinical Trials overview: https://clario.com/solutions/ecoa/ [A]
- THREAD — eCOA / Collect Data page: https://www.threadresearch.com/one-decentralized-platform/ecoa [A]
- THREAD — eCOA License Management: https://www.threadresearch.com/services/ecoa-license-management [A]
- THREAD — Study Configuration Enablement: https://www.threadresearch.com/services/study-configuration [A]
- THREAD — Compliance: https://www.threadresearch.com/one-decentralized-platform/compliance [A]
- Medable — Cortex docs (readme, features, llms.txt index): https://docs.medable.com/ [A — platform/API level only]
- Unreachable / dropped: help.castoredc.com (transport error), castoredc.com ePRO pages (404 ×2).

Sourcing limitation: no vendor's patient-app or site-portal user manual (Tier-1 operational help articles) was reachable in this pass; evidence is official product/FAQ/educational pages (Tier 2) plus developer documentation for Medable. Precise operational parameters (window lengths, reminder cadences, offline retention, export formats) are therefore not asserted. Strength of claims is calibrated accordingly.

## Product Observations

### Signant Health (SmartSignals eCOA)

Key observations (all [A]):

- eCOA/ePRO taxonomy stated directly in FAQ: "ePRO systems are a type of eCOA… Other types of COA include Electronic Performance Outcome ePerfO, Electronic Clinician-Reported Outcome (eClinRO), and Electronic Observer-Reported Outcome (eObsRO)." Patients "remotely send their ePRO symptoms and experience directly to site staff" via mobile devices.
- Data properties marketed for the platform: LOGICAL (built-in logic checks and rules keep data clean), LEGIBLE (no deciphering handwritten responses — paper heritage implied), ATTRIBUTABLE ("unique patient-specific credentials assign entries to each patient"), ACCURATE & TIMELY ("completion windows and time stamps guarantee data is collected at a specific time").
- Solution pillars: ePRO + complex ClinRO support; extensive eCOA library of scales (including PROMIS CAT computerized adaptive tests); scale licensing & management as a service; language management ("fully localized and linguistically validated"); device provisioning and global logistics; BYOD / web / provisioned devices; 24/7 patient-facing multilingual helpdesk; real-time study reporting dashboards (StudyIQ); rater training & qualification; faster study builds via automation.
- "Getting Started with eCOA" guides (in-house scientists): paper-vs-ePRO decision; choosing the right PRO measure; choosing electronic modality (app vs web; provisioned vs BYOD); special populations (elderly, pediatric); working with PROM license holders and authors (permissions, versions, contracts); designing and validating a study-specific patient diary.
- PRO data framed as primary or secondary endpoints feeding regulatory decision-making and HTA.

### Clario (eCOA)

Key observations (all [A]):

- eCOA positioned as one endpoint technology among cardiac safety, imaging, precision motion, respiratory — an endpoint-technology platform; 25 years of DCT/hybrid experience; studies in 120+ countries; 100+ languages.
- Study build described as: simplified design specification review, greater configuration, faster translations, pre-built validated standardized assessment libraries (eCOA Rapid Start assessment catalog of pre-validated, configured assessments).
- Flexible device modalities explicitly enumerated: provisioned devices, tablets, BYOD, home computer.
- Connected devices integrated with the eCOA device: CGM, blood glucose meters, home spirometry (Go Spiro), activity/wearable sensors (Opal, ActiGraph watch) — sensor/PerfO adjacency.
- Sub-offerings: eCOA Neuroscience (CNS trials); eCOA Swift (early phase, fast deployment); eCOA Science Services ("right participants at the right time, in clinic or at home"); Rater/Participant/Caregiver Training; Suicidal Ideation monitoring via self-reported eC-SSRS (+ telehealth visit service); eCOA Rescue Studies; eCOA Live (telehealth video calls and site assessments at home); eCOA Multimedia (image capture from home).
- Accessibility datasheet: zoom, dark mode; "science-led design that demonstrates equivalency" — direct evidence that modality/equivalence testing is a real practice discipline; features framed as reducing bias and caregiver assistance.
- Paper-cost calculator ("starting cost of using paper PROs") — paper is the marketed predecessor.

### THREAD

Key observations (all [A]):

- Self-description: "clinical research platform… design, operate, and scale next-generation research studies and electronic clinical outcome assessments (eCOA) programs for participants, sites, and study teams."
- eCOA library: "545+ eCOAs… pre-vetted, tested, and streamlined for licensing procurement"; visual no-code editor to customize eCOA; "select and schedule any eCOA as needed for your study."
- eCOA License Management service: manages the entire process from licensing through validation with copyright holders/instrument authors — securing license agreements, confirming approved modes of administration, obtaining authorized translations; ~800 unique licensed instruments deployed. Instruments configured to meet protocol-specific requirements "including scheduling, branching logic, scoring, localization, and participant workflows before undergoing comprehensive validation against the licensed source." Risk-based CSV (Computer System Validation) framework; content accuracy, functional performance, cross-device compatibility.
- Study Configuration (100% no-code): study workflows and participant pathways; forms and complex eCOA assessments; visit schedules and schedules of events; alerts, reminders, and automated notifications; branching and skip logic; scoring algorithms and calculations; protocol amendments and study updates — in a "validated configuration environment."
- Operate layer: eCOA and eDiaries; offline data capture "ensures protocol compliance regardless of connectivity interruptions"; compliance engine (study health dashboards & KPIs → direct-to-patient notifications → adapt); omni-channel experience; eCRFs and eSource (EDC adjacency); telehealth virtual visits; voice/image/video capture; sensors/DHT.
- Enroll layer: eConsent, recruitment/onboarding, telehealth screening.
- Services: device provisioning, translation, training, support.
- Compliance page: GDPR, HIPAA/HITECH, SOC 2, ICH GCP E6(R2), EU Annex 11, FDA 21 CFR Part 11, CCPA, CDISC membership.
- Fit-for-purpose offerings include registries and phase 3b/4 post-approval studies — non-interventional contexts run on the same machinery.

### Medable (Cortex platform)

Key observations (all [A], developer-doc level; ePRO-specific surfaces not documented publicly):

- Platform substrate for patient-facing study apps: organizations, accounts, roles/permissions (ACLs), SSO/SAML, two-factor authentication.
- Notifications: SMS, email, push; localized templates; attachments — the reminder/notification machinery at platform level.
- Audit Logs: "Some event logs, such as tracking invalid login attempts, are explicitly required by 21 CFR 11… Events that affect or are required to document compliance of 21 CFR 11, Good Clinical Practice (GCP), and other regulatory requirements are logged and visible in human-readable format in the Admin Portal."
- Localization via localized string properties; custom data models; scripting/triggers; televisit (secure video); PDF/CSV generation; environment export/import of org configuration.
- Confirms the "platform-first" pole: the eCOA workflow objects are built by the vendor/implementation teams on top of this API substrate rather than exposed as turnkey screens in public docs.

## Cross-product Comparison

| Dimension | Signant | Clario | THREAD | Medable | Layer |
|---|---|---|---|---|---|
| Instrument library of validated scales | yes (50+ library instruments; pre-validated/pre-approved versions; PROMIS CAT) | yes (pre-built validated standardized assessment libraries; Rapid Start catalog) | yes (545+ pre-vetted; ~800 licensed instruments deployed) | not documented at this level | B |
| Licensing/rights management as explicit machinery | yes (Scale & License Management service; author review step) | implied via libraries; science services | yes (dedicated service: agreements, approved modes of administration, authorized translations) | not documented | B |
| Configuration: branching/skip logic, scoring, logic checks | yes ("built-in logic checks and rules"; automation accelerates builds) | yes ("greater configuration"; design specification review) | yes (no-code: branching/skip logic, scoring algorithms, calculations) | yes at platform level (expressions, scripting, custom objects) | B |
| Protocol schedule / schedules of events | yes (completion windows; "collected at a specific time") | yes ("right participants at the right time") | yes (visit schedules & schedules of events configurable; "select and schedule any eCOA") | platform notifications/scheduled jobs | B |
| Reminders / direct-to-participant notifications | 24/7 helpdesk implies engagement; not explicit as notification engine | engagement emphasized; not itemized | yes (alerts, reminders, automated notifications; compliance engine "Respond") | yes (SMS/email/push, localized templates) | B |
| Attribution & timestamps | explicit ("unique patient-specific credentials"; time stamps) | implied by regulated posture; not itemized | implied by compliance posture | audit logging infrastructure explicit | A+B (attribution/timestamps [A] on Signant; machinery [A] on Medable) |
| Modalities: BYOD / web / provisioned device | yes (explicit three-way choice; guide on modality selection) | yes (provisioned, tablets, BYOD, home computer) | yes (omni-channel; device provisioning service) | device strategy not publicly documented | B |
| Translation / linguistic validation | yes (Language Management; "linguistically validated") | yes ("faster translations"; 100+ languages) | yes (Translation service; authorized translations) | platform localization primitives | B |
| Validation of electronic implementation | instrument library "pre-validated, do not require additional testing" | "science-led design that demonstrates equivalency"; pre-validated assessments | "comprehensive validation against the licensed source"; risk-based CSV; cross-device compatibility | platform audit/CSV posture | B |
| ClinRO support | yes, first-class ("complex ClinRO"; Electronic Clinician Ratings; rater training & qualification) | yes (rater training; eC-SSRS self-report variant; CNS specialization) | forms/assessments generic; raters not separately surfaced | not documented | A (product-specific depth on Signant/Clario; ClinRO as part of eCOA family [A] per Signant FAQ) |
| Safety alerting (e.g., suicidality) | framed via science/monitoring; not itemized | yes (Suicidal Ideation monitoring, eC-SSRS + telehealth) | compliance engine alerts (study-health oriented) | not documented | A (single-product itemization; common pattern inferred but not cross-confirmed) |
| Reporting/compliance dashboards | yes (StudyIQ real-time metrics) | yes (Reporting & Analytics) | yes (study health dashboards & KPIs) | admin dashboards (platform) | B |
| Offline capture | not stated | not stated | yes (explicit) | not stated | A (single-product; keep qualified) |
| EDC/eCRF adjacency | yes (separate EDC product in suite) | not in-scope for eCOA offering | yes (eCRFs and eSource in same platform) | data model supports it | B (suite/DCT bundling, not core) |
| eConsent / telehealth / sensors adjacency | yes (eConsent, telemedicine, DHT in suite) | yes (eCOA Live telehealth; connected CGM/spiro/wearables; multimedia capture) | yes (eConsent, virtual visits, sensors, voice/image/video) | televisit; platform | B (adjacent capabilities, not definitional) |
| Regulated posture (Part 11 / GCP / Annex 11 / SOC 2 / HIPAA / GDPR) | implied by positioning ("regulatory submissions") | yes (Part 11 named on imaging; posture throughout) | yes (explicit badge set) | yes (Part 11 logging explicit) | B |
| Multi-language global operation | yes | yes (120+ countries, 100+ languages) | yes (global cloud, translations) | localization primitives | B |
| Service layer (licensing, provisioning, helpdesk, training) | yes, extensive (24/7 patient helpdesk, logistics) | yes (science services, training, rescue studies) | yes (licensing, translation, provisioning, training, support) | n/a (platform sells through implementations) | B (packaging varies) |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant (minimal)

Four structures; remove any one and the software is no longer an ePRO/eCOA platform:

1. **The outcome instrument as the configured capture unit.** A defined assessment — validated questionnaire, rating scale, or diary — with items, response options, branching, and scoring, deployed into a study as an administrable object. Without it: a generic form/survey builder.
2. **Direct reporting by the subject-adjacent reporter.** The person whose report the assessment IS — the patient/participant (PRO), or a clinician rater or observer (ClinRO/ObsRO) for the specific subject — completes the instrument themselves, rather than site staff transcribing trial observations. Without it: EDC (site-based CRF entry).
3. **Protocol-scheduled administration with compliance machinery.** Instruments become due according to the study's protocol-driven schedule (visits, events, daily windows), with reminders and completion/compliance tracking. Without it: an ad-hoc survey tool.
4. **The regulated study record.** Responses are captured as attributable, time-stamped, auditable records in a validated system, feeding the study's dataset (endpoint/safety/HTA use). Without it: a consumer survey or wellness app.

Evidence: [C] canonical inference built on [B] cross-product commonality; item 2's attribution semantics directly observed [A] on Signant ("unique patient-specific credentials assign entries to each patient"); scheduling+windows [A] on Signant/THREAD.

### L1 — Common Mature Structure (expected in modern products, not definitional)

- Pre-validated instrument libraries with licensing/rights management (instrument authors, permissions, approved modes of administration).
- Translation and linguistic validation workflows; multi-language, multi-country operation.
- Modality machinery: BYOD app, web, provisioned devices/tablets (and device logistics/tracking as a service).
- Reminders/notifications to participants (push/SMS/email, localized).
- Compliance reporting: completion/compliance dashboards, study-health KPIs, real-time data review.
- Safety-oriented alerting tied to instrument answers (e.g., suicidality monitoring instruments) — observed [A] on one product, pattern widely claimed; keep as common-not-core.
- Rater/observer training and qualification (especially CNS).
- Study configuration environments with validated change control; protocol amendments/versioned updates.
- Audit trails, role-based access, e-signature-class record machinery, regulatory-posture certifications.
- Integration/export to the wider trial data stack (EDC, CTMS, analysis pipelines); APIs.

### L2 — Variant / Optional Structure

- Packaging: standalone eCOA specialist vs eClinical suite member vs DCT platform module vs endpoint-technology portfolio (sensors/imaging/cardiac) vs API substrate.
- Study context: interventional trials (all phases), registries, post-approval/observational studies, decentralized/hybrid/site-based delivery models.
- ClinRO depth: generic form machinery vs dedicated clinician-rater surfaces, rater training/qualification programs, CNS therapeutic specialization.
- Sensor/PerfO integration: connected CGM, spirometry, wearables, voice/image/video capture as part of assessment.
- Adjacent modules riding the same platform: eConsent, telehealth visits, eCRF/eSource capture, engagement/retention content.
- Special-population tuning: pediatric caregiver proxy reporting, elderly accessibility, accessibility features (zoom, dark mode).
- Offline capture and sync behavior (explicit in one sampled product; others not documented).
- Service depth: full-service (helpdesk, logistics, licensing done-for-you) vs self-serve configuration.

### L3 — Vendor-specific Structure (research notes only)

- Signant: SmartSignals branding; StudyIQ dashboards; "four S's" framing; library "50+ instruments"; claimed 33% faster builds; PROMIS CAT brochure positioning.
- Clario: eCOA Swift / Rapid Start / Live / Multimedia / Rescue Studies sub-branding; eC-SSRS "exclusive self-reported" claim; Opal/ActiGraph/Ametris device names; paper-cost calculator; "25% of novel drug approvals" style marketing stats; Thermo Fisher acquisition (2025/2026).
- THREAD: "545+ eCOA library", "~800 unique licensed instruments deployed" counts; 100%-no-code philosophy; Definitive Media corporate name; DiMe Seal.
- Medable: Cortex object model (Account/Organization/Room), scripting/triggers, service accounts, mdctl tooling, Twilio-based televisit.
- These counts/claims are vendor-marketing figures; not independently verifiable; excluded from the canonical document.

## Rejected Findings (anti-overfitting)

- **"eCOA = smartphone app with push reminders"** — rejected. Clario explicitly supports home computers/tablets; modality choice (app vs web vs provisioned) is a documented decision point; historical paper and device-era precedents exist. Canonical form: subject-facing digital administration surface.
- **"eCOA = PRO only"** — rejected. Signant's own FAQ: ePRO is a subset of eCOA; ClinRO, ObsRO, PerfO are siblings. The Type covers the whole COA family; the patient is the modal reporter, not the only one.
- **"Equivalence studies / linguistic validation are optional extras"** — rejected as part of the value proposition but NOT promoted to L0: they are how mature vendors de-risk implementation, not what makes the Type recognizable. Kept in L1/L2 with [A] evidence on two products.
- **"Includes eConsent/telehealth/eCRF"** — rejected as definitional. Adjacent modules bundled at the suite/DCT pole; standalone eCOA specialists exist without them.
- **"eCOA requires a randomised controlled trial context"** — rejected. Registries and post-approval studies run on the same machinery [A] THREAD; the canonical anchor is "regulated study," not "trial phase."
- **"Compliance dashboards are core"** — demoted to L1: monitoring is universal in mature products but an early/minimal system still qualifies via windows+records; the dashboard is the mature expression.
- Precise numbers (library sizes, country counts, build-speed percentages, approval percentages) — rejected from the canonical document; vendor-marketing only.

## Historical / Market-Sample Check

- Paper diaries and paper rating scales are the acknowledged predecessor (Signant markets a paper-vs-ePRO decision guide and a paper-cost calculator; "no longer decipher handwritten responses" implies the paper baseline). Paper satisfies none of the "digital" machinery but defines the outcome-assessment discipline itself; the electronic Type is defined by digitizing administration + schedule compliance + regulated records, not by any specific device.
- Device-heritage era (provisioned handsets/tablets, before BYOD) and telephone/IVR-era remote PRO administration are part of industry history; a definition requiring BYOD smartphones would exclude them. Canonical: "digital administration surface," modality in L2.
- Non-trial regulated research (registries, post-approval) must fit: yes — same objects (instruments, schedules, subjects, records), weaker/randomization-free protocols; no L0 element mentions randomization, arms, or drug supply.
- Pediatric/caregiver proxy completion and clinician-rater completion must fit: yes — L0 item 2 is written as "the person whose report the assessment is" (subject, caregiver-observer, or clinician rater), not "the patient."
- Non-English/global operation must fit: yes — no L0 element is language- or geography-specific; translation machinery sits in L1.

## Boundary Findings

| Neighbor | Load-bearing test ("remove X → becomes Y") | Distinction |
|---|---|---|
| Electronic Data Capture / EDC | Move completion from the subject/rater to site staff filling protocol CRFs → EDC. Reverse: give EDC a subject-facing instrument schedule → it grows an ePRO module. | Who reports (subject/rater assessment vs site data entry) and the record semantics (assessment responses on licensed instruments with administration windows vs protocol CRFs). Closest sibling; constantly bundled; suite vendors ship both. |
| Survey Platform / Online Form Builder | Remove the protocol schedule, instrument licensing/rights, and regulated-study record posture → a survey tool. | eCOA instruments are licensed, versioned, linguistically validated, scheduled by protocol, and captured as regulatory records; surveys are ad-hoc, anonymous-tolerant, non-regulated. |
| Remote Patient Monitoring | Shift from instruments reporting how the patient feels/functions to continuous device-derived physiological measurements in a care/management context → RPM. | Assessment-first (episodic instrument completion on a schedule) vs measurement-first (continuous sensor streams); trial record vs care workflow. They meet in DCT sensor integration (L2). |
| Patient Engagement Platform | Remove the instrument/assessment unit and keep reminders, education, communication → engagement platform. | Engagement machinery (reminders, content, retention) is L1/L2 inside eCOA platforms; the assessment response record is what makes eCOA. |
| IRT / RTSM | Replace assessments with randomization strata and drug-supply logistics → IRT/RTSM. Different managed object entirely. | Adjacent trial-technology Type; integrated in suites. |
| Clinical Trial Management System / CTMS | Shift from outcome data to trial operations (sites, visits as operations, budgets, monitoring) → CTMS. | Data-capture vs operations; visit schedule here is a data-administration schedule, not a costed operational plan. |
| eConsent | Consent is a one-time(ish) regulatory document event, not a scheduled outcome instrument. | Adjacent module; frequently co-deployed. |
| Patient Portal / EHR | Care relationship vs study relationship; care record vs study record. | ePRO data can flow into care contexts (RWD/HTA), but the platform's center of gravity is the regulated study. |
| Clinical Data Management | eCOA is a data *origin*; CDM is the cleaning/coding/discipline over collected data (sibling EDC research, same date). | Instrument vs discipline seam, same as EDC↔CDM. |

## Uncertainties

- No Tier-1 patient-app or site-portal user manuals were reachable; the subject-side interaction loop is reconstructed from vendor descriptions (reminders, windows, timestamps, offline capture) and not from step-by-step documentation. Assertion strength kept moderate accordingly.
- Whether safety-alert routing (e.g., suicidality flags to sites) is universal machinery: directly observed [A] on one product only; kept common-not-core.
- Offline capture: explicit on one product; likely widespread but unverified; kept qualified.
- e-Signature usage on eCOA records (vs audit-trail-only): not directly evidenced; not asserted in the final document.
- Castor/ePRO self-service pole: unverified this pass (fetch failures); the final document's variants mention self-serve packaging generically without Castor-specific claims.
- Medable's patient-facing eCOA feature set: only platform/API level documented; product-specific claims avoided.

## Final Synthesis

An ePRO/eCOA platform is the subject-facing outcome-measurement system of regulated studies: it takes defined, licensed/validated outcome instruments (questionnaires, rating scales, diaries — patient-, clinician-, or observer-reported), deploys them digitally to the people whose report they are (BYOD app, web, or provisioned device), schedules them against the protocol (visits, daily windows, reminders), and captures the responses as attributable, time-stamped, auditable records that feed the study's dataset. Around that defining core, mature products add instrument libraries and rights management, linguistic validation, compliance dashboards and alerts, rater training, device logistics, and integration into the wider trial data stack; packaging ranges from standalone eCOA specialists to DCT platforms and eClinical suites. Remove the subject/rater as reporter and it becomes EDC; remove the protocol schedule and regulated record and it becomes a survey tool; remove the instruments and it becomes a patient-engagement app.
