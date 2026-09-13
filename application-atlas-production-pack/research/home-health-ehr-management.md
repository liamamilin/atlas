# Research Notes — Home Health EHR / Management

Research date: 2026-09-08
Slug: home-health-ehr-management
Directory leaf: "Home Health EHR / Management" (Section 22 Healthcare & Life Sciences)

---

## Research Goal

Understand, from real products, what a Home Health EHR / Management application is: the system of record used by a home health agency to deliver skilled clinical care (nursing, therapy, aide services) in patients' homes — how the clinical record, the episode/visit structure, field documentation, agency operations (scheduling, billing, quality/compliance) fit together, and how this Type is bounded against Home Care Agency Management, Hospice Management, generic EHR, and facility-based post-acute Types.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: agency-side clinical + operational system for **skilled** home care (physician-directed, licensed clinicians), distinct from non-skilled personal/support home care (already documented as home-care-agency-management), from hospice (end-of-life), from facility-based SNF/LTC systems, and from office/hospital EHRs.
- The leaf name itself ("EHR / Management") suggests the Type always bundles the clinical record with agency operations — to be verified.
- Risk: US-centric market vocabulary (OASIS, PDGM, LUPA, EVV) could over-fit the definition to one regulatory regime. Historical/regional check required.

## Research Questions

1. What is the core object model: patient, referral, admission, episode/certification period, plan of care, visit, discipline, documentation, claim?
2. How does field (point-of-care) documentation work — device, offline behavior, sync, review?
3. What agency operations are fused into the product: intake, scheduling, QA review, billing/claims, analytics?
4. What regulatory/quality machinery appears (assessment instruments, quality reporting, EVV, survey readiness) — and is it definitional or regime-specific?
5. Who are the users and roles (intake, scheduler, clinician by discipline, clinical supervisor/QA, biller, administrator, executive)?
6. Where is the boundary vs Home Care Agency Management (non-skilled), Hospice, generic EHR, SNF/LTC?
7. Would older / non-US / paper-era home health practice still fit the definition?

## Representative Products

Selected for market position + documentation reachability + different philosophies:

| Product | Vendor | Why selected | Evidence depth this pass |
|---|---|---|---|
| Homecare Homebase (HCHB) | Homecare Homebase, LLC (Hearst Health) | Workflow-first home-based-care EHR; claims market leadership; rich public pages | Strong (homepage, FAQ, analytics article) |
| Netsmart Home Health (myUnity) | Netsmart | Post-acute continuum platform; home health + hospice + personal care + SNF in one EHR family | Moderate (root site, nav descriptions, data-solutions pages) |
| WellSky Home Health | WellSky | Enterprise post-acute suite (Kinnser lineage); broad home & post-acute catalog | Thin (root site only; product page unfetchable) |

Considered and rejected / unreachable:

- **Brightree** — current brightree.com positions only HME/DME + pharmacy/home infusion; home health line no longer presented as a market. Product mismatch for the current market.
- **Casamba** — casamba.net now serves Net Health's rehab/RTM products (Limber, Optima, ReDoc); home health line not presented. Product mismatch.
- **PlayMaker Health** — acquired by Trella Health; now a referral-growth CRM / market-intelligence product, not a home health EHR. Product mismatch (adjacent Type: referral/marketing side of home health).
- **Axxess Home Health** — axxess.com unreachable (transport errors on 3 attempts). Abandoned per network rules; not sampled.
- **CMS.gov** (regulatory context for OASIS/quality) — HTTP 403. Regulatory details not independently verified this pass; regulatory claims below are calibrated to what vendor pages themselves state.

## Sources

Fetched 2026-09-08:

- HCHB homepage — https://hchb.com/ (A)
- HCHB FAQ — https://hchb.com/resources/faqs/ (A)
- HCHB analytics article (redirect target of /who-we-serve/home-health/ and /home-health/) — "Home Health Agency Analytics: Best Metrics to Track Staffing Utilization, Productivity and Patient Satisfaction", May 25, 2021 (A)
- Netsmart root — https://www.ntst.com/ (A)
- WellSky root — https://www.wellsky.com/ (A)
- Brightree root — https://www.brightree.com/ (A; used only to establish mismatch)
- Casamba/Net Health root — https://www.casamba.net/ (A; mismatch)
- PlayMaker/Trella root — https://www.playmakerhealth.com/ (A; mismatch)

Unreachable / failed:

- https://www.wellsky.com/home-health/ — returned image-only payload on repeated attempts (text + html)
- https://www.axxess.com/, https://axxess.com/, https://www.axxess.com/products/home-health — transport errors
- https://www.cms.gov/medicare/quality/home-health — 403
- https://www.ntst.com/solutions/homecare, https://www.ntst.com/communities/post-acute-care/home-health — 404 (nav-only shell)
- https://hchb.com/back-office/, https://hchb.com/pointcare-mobile-app/, https://hchb.com/solutions/ — 404
- https://www.wellsky.com/wellsky-home-health-available-ehr/, https://www.wellsky.com/blog/category/home-health/ — 404

**Source-access limitation:** No vendor help-center / user-guide pages (Tier 1 operational documentation) were reachable this pass. All product evidence is Tier 2 (official product/marketing/support pages). Consequently: no precise operational facts (field counts, time windows, exact state names, claim formats) are asserted in the final document; workflow claims are calibrated to what the fetched pages state plus cross-product structure.

---

## Product Observations

### Product A — Homecare Homebase (HCHB)

Evidence layer: A (directly observed on official pages).

Positioning: "A modern EHR platform built to simplify workflows" for home-based care; "From documentation to billing to analytics, HCHB brings your entire operation into one secure, integrated system"; "Integrated technology designed specifically for home health agencies"; "Streamlined documentation, scheduling, and billing in one intuitive system."

Structure observed:

- **Core platform split**: Back Office (office web software) + PointCare Mobile App (field). FAQ: office workers/management run the software from computers; field staff in Home Health and Hospice use PointCare on Android devices; Personal Care field staff use a separate app (CareManager, iOS/Android).
- **Offline field work**: "PointCare and CareManager both allow for offline work in areas with mobile service difficulties." Field productivity metrics include "sync timing and success" — sync is a monitored operation.
- **State/regulatory fit**: "highly customizable and can be utilized in all 50 states. Some state rules and regulations (i.e. closed EVV states) may limit the use of some potential integrations" — EVV appears as a state-rule-driven integration surface.
- **Services layer**: Revenue Cycle Services (HCHB RCS) and Authorizations — outsourced billing and payer-authorization services around the platform.
- **Extensions**: Analytics; Intake Central (referral/intake); Curate: Scribe (AI documentation); Predict: Hospitalization Risk; Smart Scheduling.
- **Interoperability**: HCHB Connect — "seamless sharing of complex data... across every touch point."
- **Agency operating vocabulary (from the analytics article)** — the domain's own KPIs:
  - Financial: revenue per period and per visit; Medicare vs non-Medicare patient totals; estimated gross margin; **unbilled episode percentages**.
  - Patient metrics: average daily census; **admissions / recerts / discharges**; **referral conversion**; LUPA and non-LUPA data on FTE periods.
  - Productivity: **Medicare days to admit**; **open packets**; visits per period; points met percentages.
  - Quality: **Home Health Quality Reports (HHQR)** drawn from CMS + agency data, outcomes in three categories — Improvement (ambulatory/locomotion, bathing, transferring), Prevention (diabetic foot care, flu immunization, pain management), Utilization (emergent care with/without hospital admission, discharge to community, timely initiation of care); drill-down to patient and Case Manager; results by branch, payor type, month.
  - Field productivity: time in-home, drive time, documentation time, sync timing/success; measured per clinician.
  - Office productivity: backlog ratio and age, hours to close, hours allotted — "Office productivity directly affects patient intake, billing, and payment."
  - Staffing: Caregiver Optimization — visits that could be done by a higher/lower-cost caregiver, utilization by specialty/job code; Continuity of Care — how many different RNs see a patient.
  - Structure: agency branches and regions; case managers own patients.
- **Compliance posture (blog titles)**: "How Analytics Can Strengthen Home Health and Hospice Compliance"; "QAPI Checklist for Home Health and Hospice"; "Home Health and Hospice Audit and Survey Readiness Checklist" — QAPI (quality assurance & performance improvement) and survey readiness are agency concerns the product addresses.
- **Scale claims (marketing, use only as positioning)**: serves all ten of the top ten largest home health agencies; 750,000+ patients served; in business since 1999.

### Product B — Netsmart (Home Health / myUnity)

Evidence layer: A (directly observed on official root site).

- Home Health community page description: "home health EHR software that **streamlines scheduling, documentation and billing** processes." — vendor-named triad.
- **myUnity**: "a single EHR for home health, hospice, senior living, skilled nursing, palliative, adult day and personal care" — one EHR family across the post-acute continuum; home health is one community of it.
- Post-acute platform framing: "one integrated platform built for the full post-acute continuum, streamlining care delivery, simplifying reimbursement and enabling data-driven decisions across home health, hospice, palliative care and senior living settings."
- **Data Solutions**: "OASIS Scrubbing and Analytics — **OASIS compliance and PDGM reimbursement analytics for Home Health**" — the OASIS assessment instrument and PDGM payment model appear as a distinct data/analytics layer around the EHR.
- **Workforce Management**: Mobile Dispatch (CareRouter — "streamlined scheduling and operational efficiency") and **Electronic Visit Verification (EVV)** (Mobile Caregiver+) — EVV packaged as a workforce module adjacent to the EHR.
- Hospice sibling description: "streamlining documentation, IDG meetings and compliance" — hospice-specific machinery (interdisciplinary group) distinct from home health.
- News feed references CMS home health proposed rules and hospice final rules — the products track CMS payment regulation as a standing concern.

### Product C — WellSky (Home Health)

Evidence layer: A (directly observed on official root site; product page unreachable).

- Home & post-acute solution family includes: **Home Health**, Hospice, Palliative Care, **Personal Care**, **Home Health Therapy**, **DDE & Payer Connection**, WellSky Services.
- "Home Health Therapy" as a named solution — therapy disciplines (PT/OT/SLP) are a distinct concern inside home health.
- "DDE & Payer Connection" — direct connection to payer systems for claims (DDE = direct data entry into Medicare systems; the page names the capability without detail).
- Platform framing: "Intelligent Health Record"; "A longitudinal record that follows the patient across care transitions... structured, standardized data across every care setting"; analytics and AI (SkySense) positioned around documentation time reduction and referrals processing.
- Same sibling structure as HCHB/Netsmart: home health / hospice / palliative / personal care as adjacent lines.

### Rejected / mismatch products (recorded for the boundary record)

- **Brightree**: current site = HME/DME + pharmacy/home infusion only. Historically associated with home health & hospice software; today not presented in that market. Do not cite as a current representative.
- **Casamba**: absorbed into Net Health's rehab-therapy/RTM portfolio; home health line not presented.
- **PlayMaker Health**: now Trella Health referral-growth CRM (market intelligence, referral attribution, CRM for liaison teams) — this is the *marketing/referral* side of home health, a different Type.

---

## Cross-product Comparison

| Dimension | HCHB | Netsmart | WellSky | Reading |
|---|---|---|---|---|
| Self-description | "modern EHR platform" for home-based care | "home health EHR software" | part of "Intelligent Health Record" platform | All three self-identify as EHR-class systems for home health |
| Core triad | documentation + scheduling + billing in one system | "streamlines scheduling, documentation and billing" | Home Health + Therapy + DDE & Payer Connection (clinical + payer) | Triad is cross-product stable |
| Field documentation | PointCare Android app, offline-capable, sync monitored | mobile workforce modules (CareRouter, Mobile Caregiver+) | not directly evidenced this pass | Field/mobile point-of-care is the norm; offline capability directly evidenced at HCHB only |
| Patient/episode vocabulary | census, admissions/recerts/discharges, unbilled episodes, LUPA periods, days to admit, open packets | OASIS, PDGM reimbursement analytics | Home Health Therapy, DDE & Payer Connection | Episode/certification + assessment + payer machinery is the shared domain grammar (US-flavored) |
| Quality/compliance | HHQR dashboards, QAPI, survey readiness | OASIS scrubbing/compliance | (not directly evidenced) | Quality reporting tied to CMS is a standing layer |
| Sibling lines | Home Health / Hospice / Personal Care | home health / hospice / SNF / senior living / palliative / personal care | Home Health / Hospice / Palliative / Personal Care | Multi-line post-acute platforms are the market norm; home health is one line |
| Payer connection | RCS + Authorizations services | PDGM claims analytics | DDE & Payer Connection | Claims/payer connectivity is fused or tightly attached |
| Intake/referral | Intake Central; referral conversion KPI | (referral analytics in data solutions) | referrals processing in AI claims | Referral→admission is a managed funnel |
| Branch structure | branches/regions, case managers | (not observed) | (not observed) | Multi-branch agency structure evidenced at HCHB |

## Canonical Model (abstraction ladder)

### L0 — Defining Invariant (deliberately small)

A Home Health EHR / Management application is an agency-side system of record whose defining core is exactly four jointly-held structures:

1. **The home-based patient of record** — a persistent, identified clinical record for a person receiving skilled care **in their own home**, held by the agency delivering the care. The patient's residence is the care site; the agency is the record holder. (Remove → generic office/facility EHR or a CRM.)

2. **The ordered episode of skilled care under an authorizing plan of care** — care is organized as a bounded episode (admission → periodic re-authorization/recertification → discharge) governed by a plan of care that authorizes which skilled services (nursing / physical therapy / occupational therapy / speech therapy / aide) are delivered and at what frequency. (Remove → unbounded task list or generic home-care service plan.)

3. **Field-captured visit documentation feeding the clinical record** — each scheduled visit produces a clinical record entry captured at the point of care (in the home, commonly on a mobile device, commonly offline-capable with sync), including discipline-specific assessment and intervention content; completed documentation passes clinical review before the record is closed. (Remove → scheduling/billing system with no clinical chart — home-care territory.)

4. **The agency revenue and compliance loop** — delivered, documented care converts into payer-facing money and quality artifacts: claims/billing derived from the episode and visits, and quality/compliance reporting derived from the same clinical record (assessment-based outcome measures, survey/audit readiness). (Remove → clinical documentation tool with no business loop.)

Jointly-held is load-bearing:
- 1+2 without 3+4 = a referral/episode registry with no clinical content and no money.
- 3+4 without 1+2 = generic clinical notes + billing (any outpatient practice).
- 1+3 without 2+4 = a clinical documentation tool with no episode governance or revenue.
- 1+4 without 2+3 = a billing system with a patient list.
- 2+3 without 1+4 = clinical workflow without the agency business context.

### L1 — Common Mature Structure (very common, not definitional)

- Referral intake and admission workflow (referral funnel with conversion tracking; admission "packets").
- Visit scheduling and assignment (clinician/discipline matching, routes, continuity-of-care preferences, smart-scheduling assistance).
- Offline-capable mobile point-of-care app with sync (directly evidenced at HCHB; market norm).
- Discipline-specific charting templates and assessment instruments (nursing, PT/OT/SLP, aide).
- Plan-of-care / physician-order management with signature and communication routing.
- Clinical QA/review queues (supervisor review before documentation closes; correction workflows).
- Billing/claims generation with payer/clearinghouse connectivity (incl. direct payer-system connection), plus revenue-cycle services as an attachable layer.
- Analytics: census, productivity (field + office), unbilled/AR, quality dashboards, caregiver optimization.
- Multi-branch / multi-agency structure with role-based access.
- Patient/family engagement surfaces; medication list management; interoperability connections to hospitals/physician systems.
- HR/compliance tracking of clinician credentials.

### L2 — Variant / Optional Structure (regime-, segment-, deployment-dependent)

- **US regulatory machinery**: OASIS assessments, PDGM payment analytics, LUPA handling, EVV integrations, Medicare DDE, HHQR/CASPER-class reporting, QAPI/survey readiness. All are US-regime implementations of L0 legs 2 and 4 — not definitional. (Historical check: paper-era agencies ran episodes, plans of care, visit notes, and claims without any of these electronics.)
- **Payor mix**: Medicare-certified agency pole vs mixed commercial/Medicaid/private-duty poles.
- **Multi-line platform packaging**: home health sold alone vs bundled with hospice/personal care/SNF on one platform (all three sampled vendors bundle).
- **International equivalents**: community/district nursing systems organize the same abstract core (referred patient, care plan, visit records, funder reporting) under different regimes and names.
- **Adjacent attachable modules**: telehealth/RPM ingestion, hospital-at-home programs, AI scribe/documentation, hospitalization-risk prediction, family portals.

### L3 — Vendor-specific (kept out of the final document)

- HCHB: PointCare, CareManager, Intake Central, Curate: Scribe, Predict: Hospitalization Risk, Smart Scheduling, HCHB Connect, WAAR workbook, RCS.
- Netsmart: myUnity, CareRouter, Mobile Caregiver+, OASIS Scrubbing and Analytics, Bells AI.
- WellSky: SkySense AI, DDE & Payer Connection, Home Health Therapy packaging.

## Vendor-specific Findings

- HCHB's platform split (office web + Android field app) and its offline-first field posture are the most explicit in the sample; do not generalize offline capability to all products.
- Netsmart packages EVV as a separate workforce product (Mobile Caregiver+) rather than inside the home health EHR narrative; HCHB treats EVV as a state-rule integration constraint. Same regulatory force, different packaging.
- WellSky names a payer-connection capability (DDE & Payer Connection) as a first-class solution; the others express payer connectivity via services/analytics.
- Caregiver-optimization economics (right-skill caregiver per visit) surfaced only at HCHB this pass — treat as product-specific analytics emphasis.

## Boundary Findings

1. **vs Home Care Agency Management (sharpest seam; sibling leaf already documented)** — Home care delivers **non-skilled** personal/support services; its visit record is a service/attendance record (tasks performed, time on site, EVV), its authorization is a payer/service authorization, and it holds no clinical chart, no physician plan of care, no clinical assessment instruments, no clinical quality reporting. Home health delivers **skilled** clinical care; its visit record is a clinical note/assessment tied to an episode plan of care, and its quality layer is clinical outcome measurement. Remove the clinical/physician/assessment layer from this Type → Home Care Agency Management. Add it to that Type → this Type. The two share: agency + caregivers + scheduled home visits + visit-level records + service-to-money translation. Market note: vendors sell both lines (HCHB PointCare vs CareManager; Netsmart myUnity communities; WellSky lines) — same platform family, distinct Types.
2. **vs Hospice Management** — hospice is end-of-life comfort care with its own machinery (interdisciplinary group meetings, bereavement; Netsmart names IDG for hospice); home health is restorative/maintenance skilled care with recertification cycles. Same platform families, different workflow objects and rules. Remove the restorative/recertification frame and add end-of-life machinery → Hospice Management.
3. **vs Electronic Health Record (generic)** — a generic EHR records encounter-based care delivered in offices/facilities by the patient's care team; it does not run an agency's in-home episode operations (field scheduling, offline field charting, per-episode payer billing, agency quality reporting). Remove the in-home agency operations layer → generic EHR territory.
4. **vs Skilled Nursing Facility Management / Long-term Care EHR** — facility-resident care (24-hour on-site operations, MDS-class resident assessment in the US) vs home-based patient care (visit-based field operations). Different care site, different unit of operations.
5. **vs Healthcare Revenue Cycle Management** — RCM is the money layer across healthcare settings; here the revenue loop is one leg of an agency system fused to the clinical record, not a standalone claims factory.
6. **vs Remote Patient Monitoring** — RPM collects physiologic data between visits; the home health record of care delivery is the visit. RPM may attach as a module; it is not the record core.
7. **vs Referral/marketing CRM for home health (PlayMaker/Trella-class)** — manages the referral funnel and referral-source relationships on the market side; it is not the agency's clinical/operational record. Intake Central-class modules inside EHRs touch the same funnel but terminate at admission.

## Historical / Market-Sample Check

- Paper-era home health (mid-20th-century visiting nurse associations): referral slip → admission assessment form → physician-signed plan of care → visit notes written in the home → supervisor review → billing ledger/claims to Medicare/Medicaid. Satisfies all four L0 legs with paper. No mobile app, no OASIS electronics, no cloud — so none of those are definitional. ✔
- Non-US equivalents (community/district nursing under national health systems): referred patient, authorizing care plan, visit records, funder/commissioner reporting — fits the abstract core with different regime vocabulary. ✔ (Structural reasoning; no non-US vendor fetched this pass — recorded as an uncertainty.)
- US-regime artifacts (OASIS/PDGM/LUPA/EVV/DDE) are all post-1990s regulatory layers → L2, not L0. ✔

## Uncertainties

1. No Tier 1 help-center documentation was reachable; the plan-of-care/physician-order workflow (orders, signatures, verbal orders, order tracking) is asserted at canonical-inference strength, supported indirectly by the episode/recertification/assessment machinery all sampled vendors build for — not by a fetched operational page.
2. WellSky evidence is root-site only; its home health product page never fetched. WellSky-specific workflow claims are avoided in the final document.
3. Axxess (a major vendor) unsampled — domain unreachable. Cross-product claims rest on three products, two with substantial depth.
4. Non-US products not fetched; the international fit of the L0 is structural reasoning, not observation.
5. Exact US regulatory mechanics (OASIS timepoints, PDGM parameters, EVV state rules) intentionally not stated — CMS.gov was unreachable and vendor pages name but do not detail them.
6. The precise split of EVV responsibility between home health (where it applies mainly to Medicaid-funded personal-care/homemaker services) vs home care could not be verified from fetched sources; EVV is kept out of the defining core entirely.

## Final Synthesis

The Type is an **agency-side system of record for skilled care delivered in patients' homes**. Its identity comes from holding four things in one system: the home-based patient's clinical record; the ordered episode of skilled care under an authorizing plan of care; field-captured visit documentation that feeds that record; and the agency's revenue-and-compliance loop that converts documented care into claims and quality artifacts. Everything US-specific (OASIS, PDGM, LUPA, EVV, DDE, HHQR) is regime machinery layered on legs 2 and 4; everything operational-modern (offline mobile charting, smart scheduling, AI scribes, analytics) is mature structure layered on legs 3 and 4. The Type sits between Home Care Agency Management (non-skilled, service-record world) and facility-based post-acute Types (SNF/LTC), sharing platform families with both in the current market while remaining a distinct Type.
