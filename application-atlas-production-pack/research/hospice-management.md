# Research Notes — Hospice Management

Research date: 2026-09-08
Slug: hospice-management
Directory leaf: "Hospice Management" (Section 22 Healthcare & Life Sciences)

---

## Research Goal

Understand, from real products, what a Hospice Management application is: the system of record used by a hospice provider (agency/organization) to deliver end-of-life, comfort-focused care to terminally ill patients — how the patient record, the admitted end-of-life episode, the interdisciplinary team and its plan-of-care loop, family/bereavement continuation, and the money/compliance machinery fit together, and how this Type is bounded against Home Health EHR, Home Care Agency Management, palliative care lines, facility-based post-acute Types, and generic EHRs.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: agency-side clinical + operational system for **hospice** (end-of-life comfort care for terminally ill patients, mostly delivered where the patient lives — home, nursing facility, or inpatient hospice unit), distinct from:
  - **Home Health EHR / Management** (already documented): skilled *restorative/maintenance* care with recertification cycles; no death-ending, no bereavement, no IDG machinery.
  - **Home Care Agency Management** (already documented): non-skilled personal/support care; service/attendance records, no clinical chart.
  - **Palliative care lines**: serious-illness comfort care that runs *alongside* treatment and is not bounded by terminal prognosis — sold as a sibling line by the same vendors.
  - **SNF / LTC systems**: facility-resident care; hospice manages patients *across* settings.
- Risk: US Medicare hospice-benefit vocabulary (election, benefit periods, levels of care, HIS/HOPE, CAHPS, PEPPER) could over-fit the definition to one regulatory regime. Historical/regional check required.
- Prior passes already recorded the seam from the other side:
  - home-health-ehr-management: "hospice is end-of-life comfort care with its own machinery (interdisciplinary group meetings, bereavement; Netsmart names IDG for hospice)... Remove the restorative/recertification frame and add end-of-life machinery → Hospice Management."
  - home-care-agency-management: "vs Hospice Management: terminal-illness interdisciplinary care under the hospice benefit, volunteer/bereavement machinery — different core objects and rules."

## Research Questions

1. What is the core object model: patient, referral, admission/election, plan of care, interdisciplinary team (IDG/IDT), visit/contact, level of care, death/discharge, family/bereavement record, volunteer?
2. How does a patient enter and leave hospice care in the software (admission → recertification → discharge; death discharge vs live discharge; readmission)?
3. How does interdisciplinary coordination work (IDG meetings, plan-of-care review, discipline-specific charting)?
4. How does care delivery get documented (point-of-care charting, mobile/offline, per-discipline forms, medications)?
5. How does the money loop work (per-diem/level-of-care billing, claims, eligibility, room & board for facility patients)?
6. What family machinery exists (caregiver contacts, family teaching, bereavement services after death)?
7. What volunteer machinery exists?
8. What quality/compliance machinery appears (HIS-class assessments, CAHPS, PEPPER-class payment-vulnerability monitoring, survey readiness) — definitional or regime-specific?
9. Where is the boundary vs Home Health EHR, Home Care Agency Management, palliative care, SNF/LTC, generic EHR?
10. Would older / non-US / paper-era hospice practice still fit the definition?

## Representative Products

Selected for market position + documentation reachability + different philosophies + different customer tiers:

| Product | Vendor | Why selected | Evidence depth this pass |
|---|---|---|---|
| Homecare Homebase (HCHB) | Homecare Homebase, LLC (Hearst Health) | Workflow-first home-based-care platform; FAQ states it serves "eight of the top ten Hospice Agencies" — enterprise pole | Strong (hospice analytics article, FAQ) |
| WellSky Hospice & Palliative | WellSky | Enterprise suite + services + analytics ("total agency solution"); ONC-CEHRT certified | Moderate (product page, certification news) |
| Netsmart (myUnity Hospice) | Netsmart | Post-acute continuum EHR family; hospice one community among home health/SNF/senior living/palliative | Thin (site nav descriptions only) |
| Hospice Tools | Hospice Tools | Hospice-only EMR built for independent agencies; SMB pole; flat per-user pricing; the only product with reachable Tier 1 operational docs | Strong (homepage, help-guide index, eDocs FAQ) |

Considered and rejected / unreachable:

- **Axxess Hospice** — axxess.com unreachable (transport errors on 2 attempts this pass; 3 attempts in the prior home-health pass). Abandoned per network rules; not sampled.
- **Brightree** — current site positions HME/DME + pharmacy only (established in the home-health pass); not a current hospice representative.
- **Muse Healthcare** — predictive-analytics partner of HCHB, not a full hospice management system; cited only as an attachable capability.

## Sources

Fetched 2026-09-08:

- HCHB hospice page (redirect target) — "Hospice Agency Analytics: Best Metrics to Track Staffing Utilization, Productivity and Patient/Family Satisfaction", June 21, 2021 — https://hchb.com/who-we-serve/hospice/ (A)
- HCHB FAQ — https://hchb.com/resources/faqs/ (A)
- WellSky Hospice & Palliative product page — https://wellsky.com/hospice (A)
- WellSky ONC certification news — https://www.wellsky.com/hospice/ (redirect target; A)
- Netsmart site (404 page rendering full nav incl. hospice community description) — https://www.ntst.com/communities/post-acute-care/hospice (A)
- Hospice Tools homepage — https://www.hospicetools.com/ (A)
- Hospice Tools Help Guide index — https://www.hospicetools.com/hospice-tools-help-guide/ (A)
- Hospice Tools eDocs FAQ — https://www.hospicetools.com/edocs-faq/ (A)

Unreachable / failed:

- https://axxess.com/products/hospice, https://www.axxess.com/ — transport errors (abandoned)
- https://www.netsmarthealth.com/ — transport error (ntst.com used instead)
- https://www.hospicetools.com/hospice-tools-edocs-faq/ — 404 (correct URL is /edocs-faq/)
- Hospice Tools PDF manuals (e.g. IDG-Dashboard-R1.pdf) — fetch returned raw PDF binary, not readable text; only titles/index used as evidence
- CMS.gov not attempted this pass (403 in prior home-health pass); US regulatory details calibrated to what vendor pages themselves state

**Source-access limitation:** No vendor help-center *screens* (Tier 1 UI walkthroughs) beyond Hospice Tools' FAQ were readable; Hospice Tools' PDF manuals exist but returned binary. All product evidence is Tier 2 official pages plus one Tier 1 FAQ. Consequently: no precise operational facts (benefit-period lengths, visit frequencies, exact form fields, rate values) are asserted in the final document; US-regime machinery is named only where vendor pages name it, and workflow claims are calibrated to fetched evidence plus cross-product structure.

---

## Product Observations

### Product A — Homecare Homebase (HCHB)

Evidence layer: A (directly observed on official pages).

Positioning: serves Home Health, Hospice, Personal Care as three "Who We Serve" lines; FAQ: "Field staff in the Home Health and Hospice industry utilize PointCare [Android app]"; "market leader for Home Health and Hospice care, serving all ten of the top ten largest Home Health Agencies and eight of the top ten Hospice Agencies"; in business since 1999; offline-capable field apps; customizable for all 50 states with EVV-related state constraints.

Hospice-specific structure observed (from the hospice analytics article):

- **Hospice Weekly Agency Audit Report (WAAR)** KPIs: referral conversion percentages; **revenue per day** totals; gross margin percentage; visits last week percentages **including missed visits**; **length of stay** totals. Color-coding linked to budget goals per branch/region.
- **PEPPER monitoring** (CMS payment-vulnerability reports): metrics include **life discharges**, **routine homecare**, **continuous homecare and GIP** (general inpatient), **long LOS & single Dx** — the US level-of-care vocabulary (RHC/CHC/GIP) appears as the agency's own operating categories.
- **Caregiver Optimization workbook**: visits by specialty, cost of non-optimized visits ("are your schedulers sending out an RN for visits that an LPN could handle for a lower cost?").
- **Field Productivity workbook**: documentation time inside/outside the home, sync timing and success, drive time, visit time; time and/or points systems.
- **Continuity of Care workbook**: number of caregivers patients see, by job code, by month — framed around end-of-life trust relationships and **family caregiver satisfaction contributing to CAHPS scores**.
- **Hospice Quality workbook**: nine outcomes/quality measures tied to National Quality Forum-endorsed measures plus one non-NQF measure; includes **treatment preferences**, **beliefs/values addressed**, composite measures; drill-down to patient/month; customizable by agency/branch.
- **Predictive decline**: exclusive partnership with Muse Healthcare — "examines more than 800 assessment points from visits to identify which hospice patients are more likely to decline in their disease within 7-10 days"; framed as improving "quality and coordination of care during a patient's final days"; customer reports "service intensity visits and revenue doubled" (service-intensity add-on appears as a revenue concept).
- Compliance posture: "How Analytics Can Strengthen Home Health and Hospice Compliance"; "QAPI Checklist for Home Health and Hospice"; "Home Health and Hospice Audit and Survey Readiness Checklist".
- Blog taxonomy places Hospice as a first-class audience alongside Home Health and Personal Care.

### Product B — WellSky Hospice & Palliative

Evidence layer: A (directly observed on official pages).

- Product page: "WellSky Hospice & Palliative is the **total agency solution** that brings together **software, analytics, and services** to transform end-of-life care. Combining the ease-of-use clinicians love with the sophistication that growth minded organizations need."
- Named deliverables: "Advanced predictive insights to improve clinical decision making and provide better end-of-life care"; "**Care-centric scheduling** and efficient documentation to streamline workflows"; "2015 Certified EHR Technology (CEHRT) designation to meet the requirements of advanced payment models"; "Expert services that reduce administrative burdens and support growth."
- ONC certification news (2021): WellSky Hospice & Palliative V.500 certified as CEHRT; "customizable and web-based software suite that supports compliance and high-quality clinical care"; solutions "deliver a **portal for both patients and caregivers**, a reconciliation application, access to WellSky's API, service line-specific workflows, direct secure messaging."
- Site structure: Hospice and Palliative Care are **separate solution lines** in the home & post-acute family (alongside Home Health, Personal Care, Home Health Therapy, DDE & Payer Connection).
- Revenue Cycle Management webinar listed on the product page; "home health and hospice franchises" named in the client base.

### Product C — Netsmart (myUnity / Hospice community)

Evidence layer: A (directly observed on official site nav; thin).

- Hospice community description: "Our **hospice EMR software** is easy to learn and use, streamlining **documentation, IDG meetings and compliance**." — IDG (interdisciplinary group) named as the hospice-specific machinery.
- myUnity: "a single EHR for home health, hospice, senior living, skilled nursing, palliative, adult day and personal care" — one EHR family across the post-acute continuum; hospice is one community.
- Palliative Care is a **separate community** ("ONC-Certified palliative care EHR software... serious and advanced illness care") — palliative ≠ hospice in the vendor's own taxonomy.
- Post-acute platform framing: "one integrated platform built for the full post-acute continuum... across home health, hospice, palliative care and senior living settings."
- News feed tracks CMS hospice final rules — payment regulation as a standing concern.

### Product D — Hospice Tools

Evidence layer: A (directly observed; the only product with reachable Tier 1 operational documentation).

Positioning (homepage): "The Hospice EMR Built for Teams Like Yours! Hospice Tools delivers the powerful **hospice EMR & billing tools** built from the ground up for **independent hospice agencies**." "Hospice is our DNA — built exclusively for hospice by a team of hospice pros... From our **super-fast IDG** & smart care planning to hassle-free **SNF room & board**." CHAP Verified seal — "deliver personalized **comfort care**, to meet the CHAP standards of best practices and compliance."

Origin story (boundary evidence): "After struggling to make other frustrating **tweaked home health EMR systems** work for our needs we finally said, 'let's do it ourselves'. We built Hospice Tools from the ground up using our decades of expertise in how clinicians, management, and agencies actually deliver and document hospice care." — a hospice-only vendor exists because home health EMRs had to be "tweaked" for hospice; the market itself treats the two as distinct needs.

Modules:

- **eDocs EMR** ("Point-of-Care EMR"): "Built for hospice & palliative agencies; customizable forms & reports; fast and seamless charting, **smart care plans**, **super-fast IDG**, **automatic compliance**, mobile apps and more."
- **eBilling**: "Medicare real-time claim status; built-in appeals tracking; fast and accurate billing with all payers including **Medicaid room & board**."
- **TimeKeeper**: "Timesheets, mileage, & payroll; 3 layers of built-in document validation & compliance; auto-calculate mileage, visits, on-call & more."
- Web + native mobile apps, real-time sync; dashboard e-signing ("review & sign off individual or bulk documents"); mobile scan & upload auto-filed into the right chart section.

Help Guide index (Tier 1 structure of the product):

- **User Management**: new user setup/permissions; Mentor Mode; **Volunteer Management Setup**; HR tab for hospice professional qualifications.
- **Patient Intake**: enter a new patient; patient face sheet; patient location & contact details; **contact tab: capture important caregiver info**; **hospice patient discharge & readmission**; **facilities master list** (add/edit).
- **Hospice Charting**: quick patient summary; amend/correct completed form; **start a new care plan**; **create & export HIS forms**; **IDG dashboard / IDG updates**; medications form.
- **360° Reports**: **recertification & face-to-face report**; admission audit report.
- **Palliative Charting & Coding**: palliative charting & CPT coding as a separate mode.
- Discipline charting checklists (PDF titles): **Nurse start of care**, **nurse ongoing care**, **compliance**, **social worker**, **spiritual counselor**, **bereavement**, **volunteer**.

eDocs FAQ (Tier 1 operational detail):

- Offline/mobile: native apps on cellular & WiFi; auto-save/save/save-&-close; forms or entire chart downloadable as PDF for offline viewing; pre-printed patient-specific blank forms can be filled on paper and scanned/uploaded, auto-filed under the right chart section (assessment → assessments, RN visit note → nurses).
- **Medicare DDE screen** ("black screen") included in the subscription to check **patient eligibility & claim status** with a button — direct payer-system connection.
- **Amend/correct completed forms**: per-field edit with a mandatory **REASON FOR CHANGE** free-text; document re-saves showing changes and reason at the bottom — correction with audit trail, not silent overwrite.
- Form customization: forms "built to be customized to how your agency operates"; defaults "weighted to free text long form narrative boxes" for "regulatory safe" posture; admin requests changes.
- Comprehensive Assessment: most fields optional, skip irrelevant (cancer vs dementia patients); required fields marked; after sign+submit the chart shows only completed fields.
- **DATE/TIME IN/OUT**: the date & time of the activity (patient visit, call), not charting time; no overlapping/split docs — example shows multiple patients seen in one facility with per-patient time attribution (Patient A 10:00–10:30, Patient B 10:30–12:00, Patient C 12:00–13:00) — confirms facility-based patients and per-patient visit-time discipline.
- Unfinished forms: save & close, appear on dashboard as unfinished documents, resumable on any device.
- Web and app views "virtually identical", real-time sync.

User roles visible in testimonials: Director of Finance ("palliative care billing tool — clinical visits automatically generate into claims and can be billed with the click of a button"), Director of Clinical Services, Palliative Nurse Practitioner, Hospice Administrator, **Referral Coordinator**, Corporate Director of Program Development ("I also love the **volunteer access**"), HR Manager, Director of Support Services ("I can comment on the intern documents I **reject**" — document review/rejection), **Chaplain / Bereavement coordinator**, **Social Worker**, Hospice RN.

Pricing: flat per-user ($85/mo per user), "not census-based" — SMB/independent-agency tier.

---

## Cross-product Comparison

| Dimension | HCHB | WellSky | Netsmart | Hospice Tools | Reading |
|---|---|---|---|---|---|
| Self-description | hospice line of home-based-care platform; "eight of the top ten Hospice Agencies" | "total agency solution... transform end-of-life care" | "hospice EMR software... documentation, IDG meetings and compliance" | "hospice EMR & billing tools... for independent hospice agencies" | All four self-identify as hospice-class agency systems |
| IDG/interdisciplinary machinery | (continuity-of-care framing) | (not named this pass) | **IDG meetings** named | **Super-fast IDG**, IDG dashboard/updates | IDG is the named hospice-specific coordination structure |
| Plan of care | (implied by care workflows) | care-centric workflows | (implied) | **Smart care plans**, start-a-new-care-plan guide | Plan of care is a shared object |
| Discipline set | caregiver optimization by specialty (RN/LPN) | clinicians | (not detailed) | nurse (SOC/ongoing), social worker, spiritual counselor, bereavement, volunteer checklists; chaplain/bereavement coordinator user | Multi-discipline team incl. non-clinical/spiritual roles is the shared grammar |
| Family/caregiver | family caregiver satisfaction → CAHPS | **portal for both patients and caregivers** | (not detailed) | contact tab: caregiver info | Family/caregiver is a first-class record side |
| Bereavement | (not named this pass) | (not named this pass) | (not named this pass) | **Bereavement charting checklist**, chaplain/bereavement coordinator | Bereavement directly evidenced at one product; treated as common structure with single-product depth (marked below) |
| Volunteers | (not named this pass) | (not named this pass) | (not named this pass) | **Volunteer management setup**, volunteer charting checklist, volunteer access | Same single-product depth |
| Death/discharge | **life discharges** (PEPPER metric) | (not named) | (not named) | **Hospice patient discharge & readmission** guide | Discharge incl. death is a managed lifecycle event |
| Episode/recertification | length-of-stay totals | (not named) | (not named) | **Recertification & face-to-face report**, admission audit report | Bounded episode with periodic re-authorization |
| Settings | home + facility (PEPPER RHC/CHC/GIP) | agency-wide | (not detailed) | facilities master list; SNF room & board; per-patient time in one facility | Care across home + facility + inpatient settings |
| Money loop | revenue per day, gross margin, PEPPER payment-vulnerability, service-intensity revenue | RCM webinar + expert services | (not detailed) | eBilling: Medicare real-time claim status, appeals, Medicaid room & board; DDE eligibility/claim status | Per-diem/claims money loop fused to the record |
| Quality/compliance | Hospice Quality workbook (NQF measures, treatment preferences, beliefs/values), QAPI, survey readiness, CAHPS | CEHRT certification, compliance support | compliance named | HIS forms create/export, "automatic compliance", compliance checklist, document validation layers | Quality/compliance reporting is a standing layer |
| Field charting | PointCare Android, offline, sync metrics | efficient documentation | (not detailed) | native apps, offline PDF fallback, scan & upload | Point-of-care mobile charting is the norm |
| Predictive analytics | Muse partnership (decline in 7-10 days) | advanced predictive insights | (not detailed) | (not observed) | Decline prediction is an emerging common layer |
| Palliative sibling | Personal Care/Hospice/Home Health lines | Hospice & Palliative in one suite name, separate lines | Palliative Care separate community | Palliative charting & coding separate mode | Palliative is a sibling line, not this Type |
| Packaging | multi-line platform | multi-line suite + services | multi-line continuum EHR | hospice-only standalone | Multi-line platform is the market norm; hospice-only exists at the SMB pole |

## Canonical Model (abstraction ladder)

### L0 — Defining Invariant (deliberately small)

A Hospice Management application is a hospice provider's system of record whose defining core is exactly five jointly-held structures:

1. **The terminally ill patient of record under comfort-focused care** — a persistent, identified clinical record for a person receiving end-of-life care whose goal is comfort and quality of remaining life (symptom/pain management, psychosocial and spiritual support), not cure or restoration. The comfort orientation is what separates the record from restorative-care records. (Remove the comfort orientation → Home Health EHR territory.)

2. **The admitted end-of-life episode under an authorizing admission** — care is organized as a bounded stay in the program: formal admission gated by eligibility and consent (in the US: terminal-prognosis certification and benefit-period election), periodic re-authorization/recertification, and a recorded discharge — most often a **death discharge**, sometimes a live discharge (revocation/transfer), with readmission as a first-class path back. (Remove the bounded episode → unbounded caseload; remove the death-ending frame → home health.)

3. **The interdisciplinary team loop around a shared plan of care** — care is planned, delivered, and reviewed by a multi-discipline team (nursing, aide, social work, spiritual care, volunteer, physician) working from one shared plan of care that the team formally reviews and updates on a recurring cycle (the IDG/IDT meeting in US vocabulary). (Remove → discipline-siloed charting with no coordination structure.)

4. **The family as part of the care unit, with support continuing after death** — family members/caregivers are recorded as part of the care unit (caregiver contacts, family teaching, caregiver burden), and after the patient's death the family remains a service recipient (bereavement support) while the patient record closes. The record's care unit outlives the patient. (Remove → patient-only clinical record; no other clinical Type holds this structure.)

5. **The revenue-and-compliance loop** — the admitted episode and its documented care convert into payer-facing money (per-diem/level-of-care billing, claims, eligibility checks) and into quality/compliance artifacts (assessment-based quality reporting, survey/audit readiness). (Remove → documentation tool with no business loop.)

Jointly-held is load-bearing:
- 1+2 without 3–5 = a terminal-diagnosis registry.
- 3+5 without 1–2 = generic team charting + billing.
- 1+3 without 2+4 = clinic-style multidisciplinary notes with no program admission and no family unit.
- 1+4 without 2+3+5 = a family-support caseload tool.
- 2+5 without 1+3+4 = a per-diem billing engine with no care record.
- 1+2+3 without 4 = home-health-shaped record (the "tweaked home health EMR" the market complains about).
- 1+2+3+4 without 5 = a care-coordination/documentation tool with no agency business.

### L1 — Common Mature Structure (very common, not definitional)

- Referral intake funnel (referral coordinator role; referral conversion tracking).
- Scheduling and assignment across disciplines with continuity-of-care management (number of caregivers per patient as a tracked metric).
- Mobile point-of-care charting (native apps, offline fallbacks, scan-and-upload, real-time sync, e-signing incl. bulk sign-off).
- Discipline-specific charting templates and checklists (nurse start-of-care/ongoing, aide, social worker, spiritual counselor, bereavement, volunteer).
- Medication management oriented to palliative/symptom-control meds related to the terminal diagnosis.
- Physician-order and face-to-face/recertification tracking with signature workflows.
- Facilities master list (nursing homes, assisted living, inpatient hospice units) with per-facility patient placement and room-and-board handling.
- Document review/QA: supervisor review, document rejection with comments, amend/correct with recorded reason.
- Death/discharge processing with readmission; on-call management.
- Analytics: census, length of stay, visits/missed visits, revenue per day, caregiver optimization (right-skill/right-cost discipline per visit), continuity of care, payment-vulnerability monitoring.
- Quality reporting: assessment-based quality measures (incl. treatment preferences, beliefs/values addressed), CAHPS-class family/caregiver experience surveying, QAPI/survey readiness.
- Volunteer program management (recruitment/qualification/hours/charting).
- Timesheets, mileage, payroll for field staff.
- Patient/caregiver portals; predictive decline analytics; AI documentation assistance (era-current).

### L2 — Variant / Optional Structure (regime-, segment-, deployment-dependent)

- **US regulatory machinery**: election statements and benefit periods, levels of care (routine home care, continuous home care, general inpatient, inpatient respite) with per-diem rates, HIS/HOPE-class item sets, CAHPS Hospice Survey, PEPPER-class payment-vulnerability reports, Medicare DDE connectivity, service-intensity add-on billing. All are US-regime implementations of L0 legs 2 and 5 — not definitional. (Historical check below.)
- **Palliative care sibling line**: several vendors sell palliative care as a separate line/mode (serious-illness care alongside treatment, CPT-coded visits rather than per-diem episodes); a hospice product may carry a palliative mode.
- **Multi-line platform packaging**: hospice sold alone vs bundled with home health/personal care/SNF on one platform (three of four sampled vendors bundle; the fourth exists precisely because bundled platforms under-serve hospice).
- **Setting mix**: home-dominant agencies vs agencies with large facility/inpatient-unit censuses.
- **Non-US hospice/palliative services**: same abstract core (admitted dying patient, interdisciplinary plan, family/bereavement, funder reporting) under different regimes and funding models.
- **Customer tier**: enterprise chains vs independent agencies (flat per-user pricing pole).
- **Pediatric hospice** and other population variants.

### L3 — Vendor-specific (kept out of the final document)

- HCHB: WAAR, PEPPER workbook, Caregiver Optimization/Field Productivity/Continuity of Care/Hospice Quality workbooks, Muse Healthcare partnership, PointCare, Intake Central, Curate: Scribe, RCS.
- WellSky: CEHRT reconciliation application, SkySense AI, DDE & Payer Connection packaging, expert services layer.
- Netsmart: myUnity communities structure, CareRouter, Mobile Caregiver+, Bells AI.
- Hospice Tools: eDocs/eBilling/TimeKeeper module split, Mentor Mode, CHAP Verified seal, flat per-user pricing, DDE "black screen" inclusion.

## Vendor-specific Findings

- Hospice Tools is the only sampled product whose origin story explicitly names the boundary: hospice agencies historically ran on "tweaked home health EMR systems" and a hospice-only EMR exists because that tweaking under-served hospice workflows. Strong market-side evidence that the two Types are distinct.
- HCHB exposes the US level-of-care vocabulary (RHC/CHC/GIP) through its PEPPER analytics; Hospice Tools exposes room-and-board billing; both confirm that level-of-care/setting economics are operating concerns, but the specific US level set is regime machinery (L2).
- Bereavement and volunteer machinery are directly evidenced only at Hospice Tools this pass (checklists, setup guides, user roles). Cross-product depth is thin; these are kept in the defining core only at the conceptual level (family continuation after death), with volunteer program management held at L1.
- WellSky names a patient *and* caregiver portal; the others evidence caregiver records without portals. Portals are common structure, not core.
- Predictive decline analytics appear at two products (HCHB/Muse, WellSky) — emerging common layer, not core.

## Boundary Findings

1. **vs Home Health EHR / Management (sharpest seam; sibling leaf documented from the other side)** — home health organizes *restorative/maintenance* skilled care in bounded episodes with recertification; hospice organizes *comfort-focused* care for the dying, admitted under terminal-prognosis eligibility, normally ending in death discharge, with interdisciplinary team review (IDG) and family/bereavement continuation. Remove the comfort/death/bereavement/IDG machinery from this Type → Home Health EHR. Add them to that Type → this Type. Shared platform families (HCHB, WellSky, Netsmart all sell both lines) confirm sibling status, not identity. The market's own testimony (a hospice-only vendor born from "tweaked home health EMR systems") supports the split.
2. **vs Home Care Agency Management** — home care delivers non-skilled personal/support services with service/attendance records and no clinical chart; hospice holds a clinical record with plan of care, assessments, medications, and quality reporting, and adds the death/bereavement frame. Remove the clinical layer → home care territory.
3. **vs Palliative care lines** — palliative care is comfort-focused care for serious illness *alongside* curative treatment, not bounded by terminal prognosis or a death-ending episode; vendors sell it as a sibling line/mode (Netsmart separate community; WellSky separate line; Hospice Tools separate charting/coding mode). Palliative is adjacent, not this leaf.
4. **vs Skilled Nursing Facility Management / Long-term Care EHR** — SNF/LTC systems run facility-resident care (24-hour on-site operations, resident assessment regimes); hospice manages patients *across* settings (their own homes, facilities, inpatient hospice units) with the facility as a placement record (facilities master list, room & board), not as the resident's operating system.
5. **vs Electronic Health Record (generic)** — a generic EHR records encounter-based care; it does not run a hospice program's admission-to-death operations (IDG cycles, per-diem billing, bereavement caseload, survey readiness).
6. **vs Healthcare Revenue Cycle Management** — RCM is the money layer across settings; here the revenue loop is one leg of the agency system fused to the clinical record.
7. **vs Care Coordination Platform** — coordination tools manage handoffs/tasks between parties; they do not hold the hospice program's clinical record or its money loop.
8. **vs Pastoral Care Management (religious-org leaf)** — chaplains appear inside hospice teams as disciplined staff; pastoral care management is congregation-facing ministry administration, a different world.

## Historical / Market-Sample Check

- Paper-era hospice (founding-generation programs, 1960s–70s UK; US hospices before and after the 1980s Medicare benefit): patient chart opened at admission with terminal diagnosis/prognosis; interdisciplinary team (nurse, social worker, chaplain, physician, volunteer) notes; written plan of care reviewed in team meetings; family supported through death and followed up with bereavement contact; funding/claims records. Satisfies all five L0 legs on paper. No software, no US benefit machinery, no cloud — none of those are definitional. ✔
- Non-US hospice/palliative services (UK, and community palliative services elsewhere): admitted dying patient, interdisciplinary plan, family/bereavement support, funder reporting — fits the abstract core with different regime vocabulary. ✔ (Structural reasoning; no non-US vendor fetched this pass — recorded as an uncertainty.)
- US-regime artifacts (election/benefit periods, RHC/CHC/GIP/IR levels, HIS/HOPE, CAHPS, PEPPER, DDE, SIP) are all regulatory layers on legs 2 and 5 → L2, not L0. ✔

## Uncertainties

1. Bereavement and volunteer machinery have single-product direct evidence (Hospice Tools). The L0 leg-4 phrasing ("family as part of the care unit, with support continuing after death") is kept at the conceptual level where cross-product evidence (caregiver portals/records at WellSky, caregiver-satisfaction metrics at HCHB) supports the family-inclusive care unit; the *post-death continuation* specifically rests on one product plus the universal hospice-care philosophy. If challenged, the fallback is to hold bereavement at L1 and keep only "family as part of the care unit" in L0.
2. Election/benefit-period mechanics are US-specific and were not directly documented by any fetched page (only implied via "recertification & face-to-face" and PEPPER/LOS metrics); the final document describes the admission gate conceptually without asserting US mechanics.
3. Netsmart evidence is nav-description depth only; no hospice workflow claims rest on it.
4. Axxess (a major vendor) unsampled — domain unreachable across two passes.
5. Exact US regulatory mechanics (HIS/HOPE timepoints, level-of-care definitions, CAHPS administration) intentionally not stated — CMS.gov unreachable in the prior pass and vendor pages name but do not detail them.
6. Non-US products not fetched; international fit of the L0 is structural reasoning, not observation.

## Final Synthesis

The Type is a **hospice provider's system of record for end-of-life care**. Its identity comes from holding five things in one system: the terminally ill patient's comfort-focused clinical record; the admitted end-of-life episode that begins with an authorizing admission and normally ends in a recorded death discharge; the interdisciplinary team loop that plans and reviews care around one shared plan of care; the family as part of the care unit with support continuing after death; and the revenue-and-compliance loop that converts documented care into per-diem/claims money and quality artifacts. Everything US-specific (election, benefit periods, levels of care, HIS/HOPE, CAHPS, PEPPER, DDE) is regime machinery layered on legs 2 and 5; everything operational-modern (mobile offline charting, predictive decline analytics, portals, AI scribes) is mature structure layered on legs 3–5. The Type sits beside Home Health EHR (restorative frame, same platform families) and Home Care Agency Management (non-skilled frame), with palliative care as a sibling line sold by the same vendors — the market itself testifies to the seam through hospice-only vendors built because "tweaked home health EMR systems" could not serve hospice.
