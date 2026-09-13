# Research Notes — Care Coordination Platform

## Research Goal

Understand what a **Care Coordination Platform** is as an Application Type: its core objects, its coordination loop, who operates it, what rules constrain it, and where its boundaries sit against neighboring healthcare Types (Care Plan Management, Chronic Care Management, Referral Management, Population Health Management, Payer Care Management, Patient Engagement, Remote Patient Monitoring, Clinical Communication, HIE, Telehealth, Home Health EHR, Social Services Case Management).

Research date: 2026-09-06.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: software that organizes the delivery of care for an identified patient across a multi-participant care team (multiple roles, often multiple organizations), over an extended period (an ongoing program or an episodic transition), around a shared plan of care, with tracked care activities and communication.
- Likely confusion zones:
  1. **Chronic Care Management** (sibling leaf) — in the US market, "CCM software" and "care coordination software" appear to be nearly the same products, CCM being the Medicare-program-shaped variant.
  2. **Care Plan Management** (sibling leaf) — care plans are a central object here too; need to distinguish plan-as-document from plan-as-coordination-engine.
  3. **Population Health Management** — vendors bundle analytics registries with coordination workflows under one "population health" banner.
  4. **Payer Care Management** — same machinery, payer-owned deployment.
  5. **Referral Management / Patient Engagement / RPM / Clinical Communication / Telehealth** — each is one capability slice that care coordination platforms commonly include.
- Evidence posture anticipated: this category is heavily US/regulatory-shaped in its marketing; expect to abstract away from Medicare program specifics for the canonical definition.

## Research Questions

1. Who uses these platforms day-to-day, and in what organizations?
2. What are the core objects (patient record, team, plan, tasks, consent, time logs, assessments)?
3. How does a person enter coordination (identification, stratification, referral, discharge, consent/enrollment)?
4. What is the canonical coordination loop from identification to review/reporting?
5. How do platforms relate to the EHR (embedded module vs standalone with integration)?
6. What role do formal care programs (CCM/TCM/PCM/AWV etc.) and their billing machinery play?
7. What does the patient-facing side look like, and is it required?
8. What rules matter (consent, attribution, documentation of time, plan review/sign-off, role scope)?
9. How do variants differ by customer tier (practice vs health system vs payer vs post-acute vs community)?
10. Where are the hard boundaries with neighboring Types?

## Representative Products

Selected for market spread + product philosophy diversity + customer-tier diversity:

| Product | Positioning | Customer tier / philosophy |
|---|---|---|
| **ThoroughCare** | self-described "comprehensive care coordination platform"; pure-play, practice- and service-vendor-facing; organized around care programs (CCM, PCM, TCM, AWV, BHI, RPM) | mid-market practices, ACOs, outsourced care-coordination service providers, health plans |
| **eClinicalWorks (Population Health suite: Care Planning, CCM, TCM, APCM, Care Plan Oversight, RPM)** | EHR-suite-embedded care coordination modules | large ambulatory footprint; EHR-native pole |
| **Lumeon** (now part of Health Catalyst) | "Care Orchestration Platform" — automation-first, enterprise; care coordination tasks/events/workflow orchestrated automatically | large health systems (US + UK/Europe) |
| **Carium** | "virtual care management" platform; patient-experience-first; patient app + connected devices + care-team consoles | health systems, payers/payviders, healthcare innovators |
| **WellSky** (incl. CarePort lines) | full-care-continuum platform; "care coordination" deployed across acute discharge planning, post-acute placement, home care, payer post-acute coordination, social care coordination | post-acute/home/human-services + hospitals + payers |

Boundary-informing check: WellSky's product taxonomy itself demonstrates that "care coordination" is a market category used across settings (providers care coordination, payers care coordination, home care coordination, social care coordination, transitional care coordination) — evidence the Type is broader than the US chronic-program pole.

## Sources

All fetched 2026-09-06. All reachable sources are **Tier 2 (official product/solution pages)**. No Tier-1 help-center/user-guide articles were reachable from the research environment (attempted `help.healthsnap.io` → HTTP 403, abandoned after one attempt per the network-restriction rule). Operational details are therefore kept qualitative; no precise numeric limits, time windows, or default values are asserted.

- ThoroughCare — root page: https://www.thoroughcare.net/ ; care-coordination solution page: https://www.thoroughcare.net/care-coordination
- eClinicalWorks — root: https://www.eclinicalworks.com/ ; Value-Based Care / Population Health suite: https://www.eclinicalworks.com/products-services/population-health-ccmr/ ; CCM module: https://www.eclinicalworks.com/products-services/population-health/chronic-care-management-software/ ; Care Planning module: https://www.eclinicalworks.com/products-services/population-health/care-planning/
- Lumeon — root / Care Orchestration Platform: https://www.lumeon.com/
- Carium — root: https://www.carium.com/
- WellSky — root / connected platform + care coordination lines: https://wellsky.com/ (links observed: /care-coordination-software/, /payers-care-coordination/, /home-care-coordination/, /social-care-coordination/, /transitional-care-coordination/, /transitional-care-management/, CarePort discharge planning / referral intake / PAC network management)

## Product Observations

### ThoroughCare (Evidence layer: A — directly observed on official pages)

- Self-identifies as "a comprehensive care coordination platform", "an end-to-end solution" for CCM, RPM, Advanced Primary Care Management, Behavioral Health Integration, Principal Care Management, TCM, Annual Wellness Visits, Advance Care Planning.
- Care coordination function page: care plans with evidence-based interventions; interactive assessments; personalized measurable goals to monitor progress; patient education content (Healthwise / WebMD Ignite) tracked for engagement; SDOH screening → "plan of care to address gaps and barriers".
- Explicit workflow statement: "Enroll patients in care management … ThoroughCare supports end-to-end workflow for care management, including program enrollment, service documentation, and automated billing reports."
- Task machinery: "Prioritize and track clinical tasks — Assign patient care tasks to clinical team members. Clinicians can use task lists … Management can monitor care performance."
- Communication: secure two-way texting, HIPAA-compliant, "messages can be shared and read between the patient's entire assigned care team", single conversation thread per patient; opt-in required for texting.
- Data: bi-directional interoperability capturing data from EHRs, HIEs, remote monitoring devices, advance care directives, and a mobile app; analytics aggregated across clinical sites (engagement/performance, risk stratification reports, claims details, encounters and call metrics).
- Customer proof points are notably **care-management service vendors** (e.g., companies delivering outsourced CCM/RPM for practices), physician groups, ACOs, health plans, home health, pharmacies, long-term care — confirming the multi-organization operating model.
- Billing-integration evidence: athenahealth integration with "auto eligibility checks and care plan uploads" and elimination of "manual claim entry".
- Vendor-specific (L3): TC Compass AI "Smart Summary"; NCQA prevalidation; 1M+ patients figure; WebMD Ignite content in 17 languages.

### eClinicalWorks — Population Health suite (Evidence layer: A)

- The EHR vendor's "Value-Based Care" suite groups the care-coordination-relevant modules: Care Planning, Chronic Care Management, Transition Care Management, Care Plan Oversight, Remote Patient Monitoring, plus risk/coding (HCC, HEDIS), claims analytics (Disease Explorer, Cost & Utilization Explorer), PCMH.
- **Population Care Planning module** (closest to a coordination core): "Member Management — member enrollment, care team assignment, program management"; "Identify and Manage Risk — health assessment, risk stratification, gaps in care"; "Care Plans — customizable care plans to monitor progress and patient action plans"; "Productivity Tools — dashboards for tasks, reminders, referrals, messaging, and reports"; goal tracking; automated care plan review reminders; patient and care team sign-offs; group visit scheduling/documentation. Collaborative planning "with all care team members, the patient, and their family or caregivers".
- **CCM module**: identify eligible patients and alert the clinician during (or non-face-to-face) visits; manage enrollments and program activities; promote program awareness/increase enrollment; care plan templates for chronic conditions; integrated time tracker; batch billing automation for claims. Explicitly framed around Medicare's CCM program for patients with multiple chronic conditions.
- **APCM module**: "Streamline eligibility verification, consent capture, care plan creation, and batch claim generation."
- **TCM module**: continuity of care for patients moving between acute and ambulatory settings; understanding "who is being hospitalized and why".
- **Care Plan Oversight**: post-acute care management, home health supervision (certifications/recertifications), time-based services.
- **RPM module**: gathers physiological data from wearables, captures "time-based activities".
- L3: module names (Disease Explorer, healow Genie etc.), "27 chronic conditions" template count, customer stories (HealthTexas, Long Island Select Healthcare).

### Lumeon (Evidence layer: A)

- Self-describes as "the enterprise platform for automating care coordination tasks, events, activities and workflow" — the **care orchestration** pole: coordination driven by automated, event-based workflows fed by real-time data from existing systems, with clinical intelligence deciding the next step per patient ("full automation for lower-risk engaged patients, higher-touch for those who need it").
- Deployment is once per enterprise across multiple use cases: ambulatory/routine care, diagnostics, perioperative preparation, rehabilitation; acute (admission avoidance, discharge optimization, hospital-at-home); post-acute (follow-up optimization, post-discharge monitoring).
- Customers are large health systems (US and UK/Europe — NHS, Nuffield Health among logos).
- Observation: Lumeon demonstrates that the same Type can be realized as an **automation layer over existing systems** (EHR, scheduling) rather than a standalone patient-record; the coordination objects (patients, steps, tasks, handoffs, events) still exist, but the system's center of gravity is executing and advancing them automatically.
- L3: Lumeon Conductor product name; perioperative capacity claims; Health Catalyst acquisition.

### Carium (Evidence layer: A)

- Self-describes as a "care management platform delivering the next generation of advanced virtual care technology" with "bi-directional EHR integration and intelligent automations … the engine to drive an end-to-end care journey".
- Philosophy: experience-led; "A Portal Is Not A Care Experience" — patient app as first-class surface (education, coaching, connection with care team), connected-device store for monitoring kits, private-label option.
- Audiences: health systems, healthcare innovators, physician & wellness organizations, payors & payviders — i.e., also embedded in payer-side deployments.
- Personnel named in customer outcomes: nurses and "care navigators"; workflow-efficiency framing for care teams.
- L3: customer statistics (93% engagement, 44% readmission reduction, $3,700 cost reduction per patient), Healthmap Solutions ownership.

### WellSky (Evidence layer: A — portfolio-level)

- Full-continuum platform ("Intelligent Health Record … every setting, every transition"); care coordination appears as distinct lines by setting/audience: providers care coordination, payers care coordination, home care coordination, **social care coordination**, transitional care coordination/management, readmission prevention, PAC Advance (payer post-acute coordination), and CarePort (acute-side discharge planning, utilization management, patient event notifications, post-acute network management, referral intake, ED optimization).
- Confirms: (a) coordination machinery extends to non-clinical/community care (SDoH, community-based organizations); (b) transitions of care (hospital → post-acute → home) are a major coordination deployment pattern, including payer-funded coordination networks; (c) "care coordination" is used as a market category independent of chronic-care billing programs.
- L3: product line names (CarePort, PAC Advance), SkySense AI, 20,000+ provider organizations figure.

## Cross-product Comparison

| Dimension | ThoroughCare | eCW (PH suite) | Lumeon | Carium | WellSky |
|---|---|---|---|---|---|
| Identified person under coordination | yes (enrolled patients) | yes (member management) | yes (patients across use cases) | yes (patients/members) | yes (patients/clients) |
| Multi-participant care team w/ shared view | yes (whole assigned care team, one thread; task assignment) | yes (care team assignment, collaborative planning incl. family/caregivers) | yes (care teams across processes) | yes (care-team consoles) | yes (cross-setting, cross-org) |
| Coordinated plan/program organizing execution | yes (care plans w/ goals & interventions; program enrollment) | yes (care plans, patient action plans, program management) | yes (orchestrated care pathways/workflows) | yes (end-to-end care journeys) | yes (discharge plans, care coordination plans) |
| Tracked care activities w/ status | yes (tasks, outreach documentation) | yes (tasks, reminders, sign-offs) | yes (automated task/event orchestration) | yes (workflow automation, journeys) | yes (referral intake, transition events) |
| Entry by enrollment/consent | yes (program enrollment; opt-in texting) | yes (enrollment + consent capture) | not emphasized (event-triggered episodes) | program-shaped deployments | payer/agency program-shaped |
| Risk/eligibility identification | yes (risk stratification reports; eligibility checks) | yes (risk stratification, gaps, eligibility) | real-time data-driven identification | automations-driven | predictive analytics |
| Assessments (incl. SDOH) | yes (interactive assessments, SDOH screens) | yes (health assessment) | clinical intake per pathway | patient-reported + devices | SDoH focus in social line |
| Outreach communication w/ patient | yes (secure two-way texting, education content) | yes (messaging) | automated patient engagement per risk | yes (app-first experience) | patient engagement line |
| Time tracking / billing machinery | yes (service documentation, automated billing reports) | yes (time tracker, batch claims) | not observed | not emphasized | not emphasized at root level |
| EHR integration | bi-directional (EHR/HIE/devices/app) | EHR-native (same platform) | integrates existing systems in real time | bi-directional EHR integration | native record + interoperability (Carequality etc.) |
| Analytics/reporting | yes (cross-site analytics) | yes (HEDIS/HCC/claims explorers) | process/variation analytics | results metrics | analytics suite |
| Patient-facing surface | mobile app + texting | patient engagement suite (healow) | automated engagement (channel per risk) | app-first, private-label | patient engagement / family line |
| Automation depth | workflows + AI assist | module workflows + batch claims | full event-driven orchestration | intelligent automations | agentic AI workflows |

Reading: every product realizes the same four-part structure — person under coordination, multi-participant team with a shared view, a coordinating plan/program, and tracked care activities that feed status back. Everything else varies by segment and philosophy.

## Canonical Abstraction

### L0 — Defining Invariant

A Care Coordination Platform exists to coordinate the delivery of care for an identified person across the people responsible for that care. Minimal structure:

```text
Identified person under coordination
└── Multi-participant care team sharing one coordinated view of that person
    └── Coordinated care plan / program organizing intended care (goals, interventions, steps)
        └── Tracked care activities (tasks / outreach / handoffs) assigned to and
            performed by team members, with status feeding back into the shared record
```

- Remove the shared multi-participant team view → it becomes a single-clinician documentation or task tool, not coordination.
- Remove the plan/program organizing the work → it becomes unstructured messaging or a generic task tracker.
- Remove tracked, status-bearing activities (the closed loop) → it becomes a care-plan document system (adjacent Type), not coordination.
- Remove the identified person as the anchor of the record → it becomes process workflow software or analytics, not patient-centered coordination.

Deliberately **not** in L0 (checked against §24-style historical/market-sample reasoning): chronic-condition eligibility (payer case management, post-acute and social coordination do not require it), enrollment/consent (hospital discharge coordination is event-triggered), billing machinery (social/international coordination has none), patient mobile app, risk-stratification dashboards, automation, EHR embedding. Older/regional forms — hospital case management and discharge planning, payer disease-management programs, community/social care coordination — all still fit the L0 structure without any of these.

### L1 — Common Mature Structure

- Enrollment / consent machinery for formal coordination programs (evidence: ThoroughCare, eCW APCM/CCM; program-shaped deployments in Carium/WellSky lines).
- Identification machinery: risk stratification, eligibility checks, gap-in-care flags, admission/discharge event notifications (eCW, ThoroughCare, WellSky; Lumeon's real-time identification).
- Structured assessments feeding the plan, including SDOH screening (ThoroughCare, eCW, WellSky).
- Task assignment and worklists with attributable completion (ThoroughCare, eCW, Lumeon, Carium).
- Outreach and communication with the person under coordination (secure messaging/texting, education content with engagement tracking) — visible across the assigned team (ThoroughCare, eCW, Carium, WellSky).
- Time/service documentation, and where fee-for-service programs apply, billing-support outputs (ThoroughCare, eCW; time-based services language in eCW CPO/RPM).
- Care plan review cycles and sign-offs (eCW; ThoroughCare goal tracking).
- Referrals to external providers/services as one coordination activity (eCW dashboards include referrals; WellSky referral intake/PAC networks).
- EHR integration or embedding (all five).
- Dashboards/analytics over the coordinated population (all five).
- Patient-facing surface (app/portal/texting) — common but of varying depth (staff-facing-only operation is possible; e.g., Lumeon's engagement is largely automated outreach).

### L2 — Variant / Optional Structure

- **Program/billing overlay**: US Medicare/Medicaid fee-for-service care-management programs (CCM, PCM, TCM, AWV/APCM, BHI) with eligibility, consent, time thresholds and claims generation — a dominant variant that shapes many products but is not the Type itself.
- **Customer pole / ownership**: provider practice & outsourced service vendor (ThoroughCare), EHR-suite module (eCW), enterprise health system (Lumeon, WellSky acute), payer/payvider (Carium, WellSky payer lines), post-acute/home agency, community-based organization (WellSky social).
- **Automation depth**: human worklists → batch automation → event-driven orchestration (Lumeon) → agentic AI (WellSky positioning).
- **Patient-experience depth**: portal/texting → app-first experience-led design (Carium).
- **Setting scope**: ambulatory chronic care vs transitions of care (discharge → post-acute → home) vs community/social care coordination.
- **Regulatory geography**: the market category as marketed is US-shaped; international deployments exist (Lumeon/NHS) where the program/billing overlay drops out.
- **Business model**: software only vs software + outsourced clinical/consulting services (ThoroughCare clinical advisory; embedded nurse services in the market).

### L3 — Vendor-specific (kept out of the final document)

- ThoroughCare: TC Compass AI Smart Summary; WebMD Ignite/Healthwise content; athenahealth auto-eligibility; NCQA prevalidation; scale figures.
- eCW: module names (Disease Explorer, Cost & Utilization Explorer, Care Plan Oversight, healow RPM, healow Genie); "27 chronic conditions" template count; HCC/HEDIS tooling.
- Lumeon: Conductor; perioperative capacity claims; Health Catalyst ownership.
- Carium: private-label option; device store; customer outcome statistics; Healthmap Solutions ownership.
- WellSky: CarePort, PAC Advance, SkySense AI; portfolio-scale figures.

## Rejected Findings (considered, not promoted)

- "Care coordination = software for Medicare CCM billing" — rejected: WellSky's payer/social/transitions lines and Lumeon's perioperative/discharge use cases realize the Type without US chronic-program billing; billing is L2 overlay.
- "Risk stratification dashboards are defining" — rejected: event-triggered coordination (discharge, referral, perioperative pathway) works without population-level stratification; L1.
- "Patient mobile app is defining" — rejected: multiple sampled products operate staff-first with automated outreach; L1/L2.
- "Automated orchestration is defining" — rejected: it is one vendor philosophy (Lumeon, and partially Carium/WellSky); the majority pattern remains human-executed worklists; L2.
- "Care plans as full clinical documents are defining" — rejected: the coordination record needs enough plan structure to organize execution (goals, interventions, steps), not the document-control depth of Care Plan Management; the plan's *executive* role is what is invariant.
- "Multiple organizations must be involved" — considered as L0 candidate; rejected in absolute form because a coordination program can run inside one practice; kept as "multi-participant team, typically spanning roles and often spanning organizations".

## Boundary Findings

- **vs Chronic Care Management (sibling leaf, unprocessed)** — sharpest seam. Market evidence: ThoroughCare sells "care coordination software" and "chronic care management software" as functions of the same platform; eCW ships CCM as one module of its care-coordination/population-health suite. Conclusion: CCM software is the care coordination Type under a program-specific overlay (chronic-condition eligibility, consent, monthly service time, claims). Recorded as a **probable overlap / variant — joint review recommended**; the other leaf is unprocessed so this cannot be unilaterally resolved.
- **vs Care Plan Management (sibling leaf, unprocessed)** — care plans exist in both. Distinction: plan-as-authored-document (structure, versioning, clinical detail) vs coordination platform where the plan organizes team execution and accumulates task/status/communication evidence. Test: remove team-execution loop → care plan management; remove document depth but keep the loop → still care coordination.
- **vs Population Health Management** — PHM is panel-level analytics/registry (identify cohorts, gaps, risk); care coordination is person-level execution for the people PHM flags. Vendors bundle both (eCW names the suite "Value-Based Care/Population Health"; ThoroughCare's analytics is "population health management software") — real bundling zone, distinct centers of gravity.
- **vs Payer Care Management** — same coordination machinery; boundary is organizational owner and purpose (payer-side utilization/cost oversight of members vs provider-side delivery of coordinated care). Products deploy on both sides (WellSky payer lines; Carium payviders), so treat as deployment pole, not separate Type — boundary belongs to the payer leaf when processed.
- **vs Referral Management** — referral management runs the single request→routing→appointment→result loop; care coordination runs a longitudinal record in which a referral is one activity type. Referral platforms lack the shared plan/team/longitudinal record.
- **vs Patient Engagement Platform** — engagement centers patient-facing outreach/education/content as the primary surface; coordination centers staff-side orchestration, with patient surfaces as one channel. Carium shows the two can be bundled with an engagement-first philosophy, but the coordination record/team/tasks are what make it coordination.
- **vs Remote Patient Monitoring** — RPM's defining loop is device-data collection/monitoring; coordination consumes RPM data (observations on both ThoroughCare and eCW) but the device loop is not coordination.
- **vs Clinical Communication Platform** — secure clinician messaging is a mechanism inside coordination (team-visible patient thread); communication platforms have no plan/program/record anchor.
- **vs Health Information Exchange** — transport of records between parties; no team, plan, or task loop.
- **vs Telehealth Platform / Patient Scheduling / Patient Intake** — single-surface operational tools (visit, booking, registration); no longitudinal coordination record.
- **vs Home Health EHR / Home Care Agency Management / Hospice Management** — agency-side delivery systems of record for visit-based care; coordination platforms hand off to them (transitions) but do not run the agency's care delivery.
- **vs Social Services Case Management** — CBO-side case files; social **care coordination** (WellSky line) sits between the two: health-originated coordination extended to community services via closed-loop referral machinery. Flagged as a fuzzy edge for the sibling leaf.
- "Remove what, and it becomes another Type" summary: remove the shared team + tracked execution loop → care plan document tool or task tracker; remove the person anchor → workflow/process orchestration; remove the longitudinal record → referral/engagement tools; remove program overlay → still this Type (hence overlay is only L2).

## Uncertainties

- **No Tier-1 operational documentation reached** (help centers login-gated or unreachable; one help-center attempt returned HTTP 403). All observations are from official product/solution pages. Consequently the final document deliberately avoids precise operational claims (time thresholds, numeric limits, state-machine labels, default settings).
- **US-centric sample**: all five sampled products are US-market-rooted (one deploys internationally). The canonical definition was abstracted to survive non-US and non-CCM forms (discharge coordination, payer case management, social care coordination) based on portfolio evidence within those products, but a non-US pure-play was not directly sampled.
- **Epic / Oracle Health / Athena care-coordination modules** were not fetched (documentation login-gated); they are referenced in market reasoning only, and no claims about them are made.
- The exact boundary with the unprocessed sibling leaves **chronic-care-management** and **care-plan-management** cannot be finalized unilaterally; flagged for joint review.

## Final Synthesis

A Care Coordination Platform is the operational software for **coordinated longitudinal care**: it holds an identified person under coordination as the anchor record, organizes a multi-participant care team (roles, often organizations) around a shared view of that person, structures the intended care as a coordinated plan or program, and tracks the team's care activities — tasks, outreach, handoffs, referrals, documentation — through attributable states that feed back into the shared record until the person's goals are met or the episode closes. Around this core, mature products add identification (risk/eligibility/events), enrollment and consent, assessments (including SDOH), patient-facing communication and education, time/service documentation and program billing support, EHR interoperability, and analytics. The Type is realized across distinct market poles — program-billing-centric practice/service-vendor tools, EHR-embedded suite modules, enterprise automation/orchestration layers, patient-experience-first virtual care platforms, and cross-setting transitions/social coordination — all of which preserve the same defining structure.
