# Research Notes — Chronic Care Management

## Research Goal

Understand **Chronic Care Management (CCM) software** as an Application Type: its core objects, its program operating loop, who operates it, what rules constrain it, and where its boundaries sit against neighboring healthcare Types — especially the two processed sibling leaves **Care Coordination Platform** and **Care Plan Management** (both of which left joint-review flags pointing at this leaf), plus Remote Patient Monitoring, Population Health Management, Payer Care Management, Patient Engagement, and the wider family of US care-management programs (PCM, TCM, APCM, AWV, BHI).

Research date: 2026-09-06.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: CCM software is software for **operating a longitudinal care-management program for patients with chronic conditions** — identifying eligible patients, enrolling them (with consent), building and maintaining condition-oriented care plans, driving a recurring cycle of non-face-to-face care activities by care staff, documenting the service (including clinical staff time), and producing program billing and compliance outputs.
- Likely confusion zones:
  1. **Care Coordination Platform** (processed sibling) — its pass recorded a joint-review flag: "market evidence shows chronic-care-management software and care coordination software are the same products under a program overlay (ThoroughCare sells both as functions of one platform; eClinicalWorks ships CCM as one module of its care-coordination suite)"; recorded working split: "chronic-care-management = care coordination Type carrying a specific chronic-care program's eligibility/consent/time/billing rules."
  2. **Care Plan Management** (processed sibling) — care plans are central here too; split recorded as plan-as-authored-document vs plan-as-execution-engine; its pass noted "chronic-care-management sibling remains unprocessed — its flag stands for its own pass."
  3. **Remote Patient Monitoring** — many CCM platforms bundle RPM; device loop vs program loop must be separated.
  4. **Population Health Management** — panel analytics vs person-level program delivery.
  5. **Payer Care Management** — same machinery, payer-owned deployment.
- Evidence posture anticipated: the category name and its dominant implementation are US-Medicare-shaped (a 2015-introduced fee-for-service program); the canonical definition must be tested against older and non-fee-for-service chronic-care program forms (payer disease-management programs, international chronic disease management) so that the definition does not collapse into "Medicare CCM billing software."

## Research Questions

1. What is a "CCM program" as the products define it (eligibility, consent, care plan, service pattern, billing)?
2. What core objects exist in CCM software (eligible-patient identification, consent record, care plan, time log, billing report, dashboard)?
3. What is the canonical program loop from panel identification to monthly billing and plan review?
4. Who operates it (in-house practice staff vs vendor-employed care managers under physician supervision)?
5. How does CCM software relate to the EHR (embedded module vs standalone with bi-directional integration)?
6. Is the billing machinery definitional, or is it the dominant regime overlay? (Test: does chronic-care program software exist without claims machinery?)
7. How do the sibling Types differ (care coordination, care plan management, RPM, PHM)?
8. What variants exist (software-only vs tech-enabled services vs full-service; single-program vs multi-program stacking; practice tiers; FQHC/RHC)?
9. Does the definition survive the historical/market-sample check (non-US, payer-funded, pre-2015 chronic disease management forms)?
10. What is the answer to the joint-review flag recorded by care-coordination-platform's pass?

## Representative Products

Selected for market spread + product philosophy diversity + customer-tier diversity. All are official vendor surfaces fetched 2026-09-06.

| Product | Positioning | Philosophy / tier |
|---|---|---|
| **ChartSpan** | self-described CCM leader; explicitly **not** "a CCM software" but "a full-service program" delivered with proprietary software | full-service software+service pole; practices, health systems, FQHCs, RHCs |
| **Prevounce** | "AI-powered" **software-first** platform for RPM/CCM/APCM/AWV + optional care-management services and cellular devices | software-only platform pole; practices of all sizes, health systems, payors, ACOs |
| **TimeDoc Health** | "chronic care management company" — **tech-enabled services** with enterprise platform | managed-service pole; community health centers, medical groups, health systems, health plans |
| **ThoroughCare** | care-coordination platform selling CCM as one program among many (CCM, PCM, RPM, TCM, AWV, BHI) | multi-program coordination platform (the direct joint-review evidence product); ACOs, service providers, health plans, home health, pharmacies, physician groups |
| **HealthArc** | CCM **software and services** with an unusually documentation-grade product page enumerating every platform capability | platform + managed-services pole; primary care, cardiology, endocrinology, multi-specialty, FQHC/RHC |

Boundary/width anchors from sibling research (not re-fetched this pass): **eClinicalWorks** ships CCM as a module of its EHR-embedded care-coordination/population-health suite (EHR-embedded pole; evidence recorded in research/care-coordination-platform.md).

## Sources

All fetched 2026-09-06. All reachable sources are **Tier 2 (official product/solution/program-guide pages)**. No Tier-1 help-center articles and no regulator pages were reachable: `https://www.cms.gov/chronic-care-management` returned HTTP 403 (abandoned after one attempt per the network-restriction rule); no vendor help centers were attempted because the sampled products expose their operational descriptions on product pages. CPT-code figures (dollar rates) below are vendor-stated national averages — treat as vendor claims, not verified fee-schedule facts.

- ChartSpan — root: https://chartspan.com/ ; CCM program page: https://www.chartspan.com/chronic-care-management/
- Prevounce — root: https://prevounce.com/ ; CCM software page: https://www.prevounce.com/software/chronic-care-management
- TimeDoc Health — root: https://timedochealth.com/
- ThoroughCare — CCM guide: https://www.thoroughcare.net/chronic-care-management ; (root + care-coordination pages were fetched in the sibling pass, research/care-coordination-platform.md)
- HealthArc — CCM software & services page: https://healtharc.io/chronic-care-management/

## Product Observations

### ChartSpan (Evidence layer: A — directly observed on official pages)

- Program portfolio: CCM (primary care / specialties / RHCs / FQHCs), Advanced Primary Care Management, Annual Wellness Visits, RPM Enrollment Service, Quality Improvement (MIPS) services.
- Explicit software-vs-service self-positioning (FAQ): "Is ChartSpan a CCM software? No, we're a full-service program with a highly-trained team of clinicians and nurses… But we also use our proprietary CCM software to deliver a streamlined, fully-managed CCM service."
- Program process (as published): **Onboard → Identify & Enroll** ("We identify eligible patients, you approve the eligibility list, and we enroll them in the program") **→ Engage** ("We reach out monthly to your enrolled patients") **→ Intervene → Measure** ("track quality, measure performance, support compliance") **→ Bill** ("RapidBill™ technology allows you to review and bill under general supervision").
- Workflow statement: "Our team identifies CCM-eligible patients from your practice's EMR and calls those patients to get their consent to participate in the program. Once the patient is enrolled, we reach out each month to work on care coordination activities… All work is documented in a comprehensive care plan, which is then shared with the provider through the EMR."
- Practice obligations: "Ensure ChartSpan has access to your EHR; approve the eligible patient lists; manage clinical notifications."
- Patient-facing services: 24/7 care line, dedicated clinician, medication refills, appointment scheduling, test-result access, comprehensive care plans, transportation/mobility support, SDOH assistance, caregiver/family support. Vendor claims "20 minutes of care from ChartSpan for each patient every month".
- Program rules cited: CPT 99490 / G0511 billing; "Medicare patients with two or more chronic conditions"; billing "under general supervision"; MIPS/ACO compliance angle; 10 years record archiving; SOC 2 Type 2.
- Vendor-specific (L3): RapidBill™; $2,457 per-patient annual cost-reduction claim; 3M+ monthly encounters; 175+ practices; enrollment-rate averages (45% primary care / 35% specialty); 75.75 NPS; Validic acquisition for device/data infrastructure.

### Prevounce (Evidence layer: A)

- Software-first: "comprehensive, cloud-based platform… Manage your RPM, CCM, APCM, and AWV programs in one place," plus optional care-management staff ("our clinically trained care managers serve as an extension of your practice") and cellular devices/kits.
- CCM capability page enumerates the machinery step by step:
  - **Identify chronic conditions** — "Receive automatic notifications if a patient is eligible for CCM. Quickly identify qualified patients from your EMR or a Medicare annual wellness visit (AWV), and easily register patients with efficient guided workflows."
  - **Ensure compliance** — "We even flag required steps that are easily overlooked, like getting informed patient consent. This process ensures that all your CCM work is billable."
  - **Create a care plan** — "editable templates that allow practitioners to choose the right items for each patient quickly."
  - **AI-powered insights** — embedded AI analyzing patient data for "customized care summaries and recommendations."
  - **Time tracking** — "Get credit for your 20 minutes a month… simple to be compliant with Medicare and get paid for time spent supporting patients."
  - **Billing output** — "Collect and record calls and other interactions, document them, and generate a single billing report (superbill). Simply review the report and send it to your biller or billing software."
- CCM billing guide resource (2026 coding/billing); AWV machinery ("intelligent eligibility verification, automated patient outreach, checklists, billing support") confirms eligibility/outreach/billing as generic program machinery reused across programs.
- Vendor-specific (L3): Pylo device line; $66/month-per-enrolled-Medicare-patient revenue claim; CCM Toolkit; AI insight screenshot branding.

### TimeDoc Health (Evidence layer: A)

- Self-identifies as "a chronic care management company" delivering "care management programs at scale… supported by proven technology" — tech-enabled-services pole.
- Program portfolio: Virtual Care Management, CCM, RPM, APCM, Behavioral Health Monitoring, AWV.
- CCM described as "Enterprise platform and care management services to effectively deliver holistic care, from medication adherence and appointment scheduling to durable medical equipment (DME) assistance."
- Integration framing: solutions "designed by doctors to seamlessly integrate into your EHR and workflow. From pushing vitals directly into your flow chart to automating the billing process."
- Dedicated "Care Coordination Services" and "EHR Integration" pages exist (not fetched).
- Testimonials name the operating roles: "Chronic Care Management Coordinator," care coordinators refilling medications, arranging appointments, changing and monitoring the plan of care; rural/community health center deployments.
- Vendor-specific (L3): animated revenue-per-patient figures; Piedmont Care Connect partnership; HITRUST i1 certification.

### ThoroughCare (Evidence layer: A — CCM program guide page)

- Direct joint-review evidence: the same vendor sells **Care Coordination** and **Chronic Care Management** as sibling items in one platform nav ("By Function: … Care Coordination, Chronic Care Management, … Principal Care Management, RPM, TCM…"), and its CCM page says "ThoroughCare gives providers the tools and support to make Chronic Care Management effective" while its dashboard screenshot is labeled "ThoroughCare's care management software platform."
- Program definition: "CCM is a Medicare Part-B program for patients with two or more chronic conditions. Clinical staff engage patients for at least 20 minutes per month to coordinate care activities… Providers are also reimbursed per patient."
- Eligibility rules: 2+ chronic conditions; "expected to last at least 12 months or until end-of-life"; "pose a risk of death, acute decompensation or functional decline"; "noted by the provider 12 months prior to enrollment."
- Enrollment: "completed at an in-person evaluation or Annual Wellness Visit. Written or oral consent must be documented." Patient must be told benefits, Part-B cost-sharing, and the right to opt out at any time.
- Service content: "a monthly clinical review, telephone check-ins, physician reviews, referrals, prescription refills, chart reviews and scheduling appointments or services."
- Workforce: "Care managers… conduct a majority of patient engagement and execute nearly all program services"; billing must be directed by a provider with an NPI; diverse licenses can deliver the service (physicians, PAs, NPs, CNMs, CNSs, pharmacists).
- Billing structure (guide): non-complex codes 99490 (20 min) + 99439 add-ons (40/60 min); physician-driven 99491 (30 min) + 99437 (60 min); complex 99487 (60 min) + 99489 (90 min); "Two ICD-10s must be presented when billing."
- Program-start checklist: build a care team → identify and enroll patients → "Use digital tools — Acquire a digital platform to streamline workflow, support documentation, enable patient care planning, track and report outcomes, and automate claims preparation."
- Multi-program stacking: "CCM and RPM can be billed together when each program independently meets the requirements"; BHI and TCM companions named.
- Vendor-specific (L3): TC Compass AI; NCQA prevalidation; case-study retention/engagement figures (23.4 months, 36%); West Virginia program outcomes.

### HealthArc (Evidence layer: A — documentation-grade product page)

- One-sentence product definition: "HealthArc helps physician practices and health systems launch, run, and bill compliant CCM programs, with care plans, automated outreach, time tracking, and billing support built into one platform."
- Program definition: "CCM is a Medicare and Medicare Advantage program that reimburses eligible providers for **non-face-to-face care coordination** delivered to patients with two or more chronic conditions… reviewing care plans, coordinating referrals, managing medications, and following up on results."
- Platform machinery enumerated:
  - **Patient Identification & Eligibility** — "Filter the panel by condition, payer and enrollment status, then flag everyone who qualifies today and isn't being billed for."
  - **Digital Consent & Enrollment** — "Consent, captured electronically. Every record is timestamped and auditable."
  - **Condition-Specific Care Plans** — "Editable CMS-compliant templates, by condition. Everyone works from the current version and every revision is dated."
  - **Monthly Outreach Tracking** — "Log calls, secure messages and check-ins. Each one lands on the monthly record with a timestamp and a running total toward the threshold."
  - **Automated Time Tracking** — "In-platform time captures itself. Off-platform work goes in by hand, and at month end the totals map to whichever CPT code the minutes actually support."
  - **Billing Report Generation** — "Minutes map to 99490, 99439, 99487 or 99491, and the export lands in your clearinghouse format."
  - **Population-Level Dashboard** — "Who's enrolled. Who's hit the threshold. Who's about to miss the minimum with four days left in the month."
- Care-team model: internal staff or vendor-managed coordinators "under physician supervision… under the supervising physician's NPI. Physicians set parameters and approve care plans. That satisfies CMS general supervision."
- Five documentation requirements for a CCM claim: documented consent (verbal allowed but recorded, with right to stop); initiating visit within previous 12 months; a comprehensive, current, revised care plan; monthly clinical-staff time logs meeting the threshold "and never counted toward a second program"; evidence of the coordination work.
- EHR integration: bi-directional (HL7/FHIR), diagnosis-code import for eligibility screening, care-plan documentation written back to the chart, structured import fallback.
- Implementation timeline: panel analysis → platform/EHR setup → training → consent & enrollment → first billing cycle (60–90 days to first billed patient) → ongoing program management with quarterly reviews.
- Program family in nav: RPM, CCM, PCM, TCM, RTM, BHI, APCM, PIN, MTM — same platform, different program overlays.
- Vendor-specific (L3): revenue calculator; $62–64 (99490) / $47–49 (99439) / $130–135 (99487) / $82–85 (99491) vendor-stated rates; "40–60% of a typical primary care panel eligible" claim; 100K+ patients served; panel-revenue estimates.

## Cross-product Comparison

| Dimension | ChartSpan | Prevounce | TimeDoc | ThoroughCare | HealthArc |
|---|---|---|---|---|---|
| Chronic-condition eligibility machinery | yes — team identifies CCM-eligible patients from the EMR; practice approves list | yes — automatic eligibility notifications from EMR/AWV; guided registration | yes (program population framing; EHR-integrated) | yes — eligibility rules published; panel identification step | yes — panel filtering by condition/payer/enrollment, flagging qualifiers |
| Consented enrollment | yes — enrollment calls obtain patient consent; "fully compliant patient enrollment services" | yes — informed-patient-consent flagged as required step | yes (enrollment within services) | yes — written or oral consent documented; opt-out explained | yes — digital consent, timestamped, auditable |
| Condition-oriented care plan | yes — "comprehensive care plans for each patient," documented and shared via EMR | yes — editable care-plan templates per patient | yes — plan-of-care changes/monitoring named | yes — "patient-centered care plan" central | yes — condition-specific CMS-compliant templates, dated revisions |
| Recurring (monthly) service cycle | yes — "reach out monthly… 20 minutes of care… every month" | yes — "20 minutes a month" framing; time tracking | yes — recurring engagement ("consistent engagement," coordinator cadence) | yes — "at least 20 minutes per month" | yes — monthly outreach record with running total toward threshold |
| Time tracking | yes (service framed in minutes; billing support via RapidBill) | yes — time tracking as named feature | implied (billing automation) | yes — service documentation workflow | yes — automated capture + manual entry, mapped to codes |
| Billing/claims output | yes — "review and bill under general supervision with ease" | yes — single billing report/superbill to biller | yes — "automating the billing process" | yes — "automate claims preparation"; billing guide | yes — clearinghouse-format export, CPT mapping, pre-submission review |
| Multi-program stacking | yes — CCM + APCM + AWV + RPM enrollment + QI | yes — RPM/CCM/APCM/AWV one platform | yes — CCM/RPM/APCM/BHI/AWV | yes — CCM/PCM/RPM/TCM/AWV/BHI | yes — RPM/CCM/PCM/TCM/RTM/BHI/APCM/PIN/MTM |
| EHR relationship | EHR access required; care plan written back | EMR identification + integrations | "seamlessly integrate into your EHR and workflow" | bi-directional EHR/HIE/device integration | bi-directional HL7/FHIR; write-back to chart |
| Service delivery model | full-service program (vendor staff) | software-only optional + managed services | tech-enabled services | software platform (+ clinical advisory) | software + optional managed coordinators |
| Patient-facing surface | 24/7 care line, dedicated clinician | patient engagement via platform/devices | engagement emphasis in testimonials | mobile patient app; secure two-way texting | secure messages logged in outreach record |
| Quality/analytics | MIPS/QI services; measure step | AI insights; program metrics | outcome claims (gaps closed, retention) | analytics across sites; NCQA angle | population dashboard; compliance monitoring |

Reading: every product realizes the same five-part structure — chronic-condition eligibility, consented enrollment, condition-oriented care plan, recurring documented care service (monthly in the dominant form), and program billing/compliance outputs — delivered over an EHR-connected platform, and nearly all of them bundle sibling Medicare care-management programs on the same machinery. What varies is who performs the service (practice staff vs vendor coordinators), how much is software vs people, and which programs share the platform.

## Canonical Abstraction

### L0 — Defining Invariant

Chronic Care Management software exists to **operate a recurring, documented care-management service for a consent-enrolled population defined by chronic conditions**. Minimal structure:

```text
Chronic-condition-defined patient population
  (eligibility record: qualifying conditions drawn from the patient panel / EHR)
└── Consented program enrollment
    (patient bound to a defined ongoing program; consent recorded)
    └── Condition-oriented care plan maintained per enrolled patient
        └── Recurring non-face-to-face care service cycle
            (care staff perform and document care activities per patient
             per service period — the monthly service record)
```

- Remove the chronic-condition anchor (eligibility/profile) → the product is a generic care-coordination or outreach tool, not chronic care management.
- Remove program enrollment (the patient-membership record) → anonymous outreach; the program's accountable population disappears.
- Remove the care plan → a call center or reminder service; the program no longer manages care.
- Remove the recurring documented service cycle → a care-plan authoring system (adjacent Type) or a one-off visit tool; the program's heartbeat is the per-period service record.

Deliberately **not** in L0 (tested against the historical/market-sample check): CPT/claims billing (payer-funded, internal, and international chronic-care programs operate without fee-for-service claims), time thresholds (regime-specific rules of the dominant US program), RPM devices (several programs run phone-only), patient mobile apps, AI features, risk stratification dashboards, multi-program stacking. Older and non-US forms — payer disease-management programs (enrolled chronic patients, nurse outreach, documented care, payer-funded), GP-register chronic disease review programs, internally funded clinic programs — fit the L0 structure without any of these.

### L1 — Common Mature Structure

Present in most mature products; not definitional:

- **Eligibility identification machinery over the panel** — automatic notifications, panel filtering by condition/payer/enrollment status, flagging patients who qualify but are not enrolled (Prevounce, HealthArc, ChartSpan, ThoroughCare).
- **Consent capture as a compliance gate** — flagged required steps, digital/timestamped/auditable consent records (Prevounce, HealthArc; ThoroughCare guide documents the consent rules; ChartSpan enrollment services).
- **Time documentation per patient per period** — capturing clinical-staff time against the service period, with running totals toward the program's threshold (Prevounce, HealthArc; the framing recurs across products because the dominant program pays on documented time).
- **Program billing outputs** — billing reports/superbills, CPT mapping, claims preparation, denial/compliance review (all five; regime-dependent in principle, near-universal in the US market).
- **EHR integration or embedding** — bi-directional sync (demographics/diagnoses in; care-plan documentation out), structured-import fallback; or module-inside-EHR delivery (eCW pole from sibling research).
- **Multi-program stacking** — CCM delivered on platforms shared with RPM, PCM, APCM, AWV, TCM, BHI, and related programs; the same objects (eligibility, consent, plan, time, billing) are reused per program.
- **Care-team role model** — care coordinators/managers execute; supervising physician/NPP directs and approves (general supervision); billing and compliance staff consume outputs (HealthArc roles list; ThoroughCare workforce description; ChartSpan practice obligations).
- **Patient communication and engagement** — phone outreach as the default medium; secure messaging/texting; 24/7 care lines; education and SDOH support (ChartSpan, HealthArc, ThoroughCare, TimeDoc).
- **Dashboards/analytics** — enrollment state, threshold proximity, care gaps, quality-program performance (MIPS/Star/ACO angle), revenue reporting (all five).
- **Compliance/audit machinery** — timestamped records, audit-ready documentation, security certifications (HIPAA, SOC 2/HITRUST) (HealthArc, ChartSpan, TimeDoc).
- **Patient-facing surfaces** — apps/portals where offered; commonly secondary to staff-mediated outreach.

### L2 — Variant / Optional Structure

- **Delivery model**: software-only (Prevounce) ↔ software + managed coordinators (HealthArc, Prevounce services) ↔ tech-enabled services company (TimeDoc) ↔ full-service program vendor (ChartSpan). The same program machinery is sold as tool, staffing extension, or turnkey service.
- **Program regime**: US fee-for-service Medicare/Medicare Advantage CCM (dominant), with sibling Medicare programs (PCM for single high-risk conditions, TCM transitional episodes, APCM, AWV, BHI) on shared machinery; vs payer-funded disease management, internal programs, and international chronic disease management without claims machinery.
- **Program breadth**: single-program vs multi-program platforms; the CCM category is the anchor of a wider "care management program software" market.
- **EHR posture**: standalone platform with bi-directional integration vs EHR-embedded module (eCW).
- **Customer tier**: solo/small primary care, multi-specialty groups, FQHCs/RHCs (distinct billing rules), hospitals/health systems, ACOs, health plans, pharmacies as delivery partners.
- **Condition scope**: multi-condition general programs vs condition-flavored templates (condition-specific care-plan libraries) vs specialty deployments (cardiology, endocrinology, nephrology).
- **RPM integration**: phone-only vs device-fed vitals flowing into the program record; RPM as a separate billable program stacked with CCM.
- **Geography/regulation**: the sampled market is US-shaped; international chronic-care program software was not directly sampled (see Uncertainties).

### L3 — Vendor-specific (kept out of the final document)

- ChartSpan: RapidBill™; 24/7 care line branding; 10-year record archiving; Validic acquisition; enrollment-rate/NPS/cost-reduction claims.
- Prevounce: Pylo device line and Connect API; AI insight branding; $66/month revenue claim; CCM Toolkit.
- TimeDoc: Piedmont Care Connect; HITRUST i1; animated revenue figures.
- ThoroughCare: TC Compass AI; NCQA prevalidation; case-study figures (23.4-month retention, 36% engagement).
- HealthArc: revenue calculator; vendor-stated CPT dollar rates ($62–64 etc.); panel-eligibility percentage claims; implementation-day counts.
- eCW: module names and suite structure (recorded in sibling research).

## Rejected Findings (considered, not promoted)

- "CCM software = Medicare billing software" — **rejected**: billing is the dominant regime's output, not the invariant; payer-funded and international chronic-care program forms lack claims machinery but realize the same core (enrollment, plan, recurring documented service). Billing is mature structure in the US market.
- "The 20-minute monthly threshold is definitional" — **rejected** as an L0 element: it is the base code's rule in the dominant US program (documented by three sampled products); the invariant is *documented service time per period against whatever the program requires*, which is regime machinery, not the Type.
- "RPM devices are part of CCM" — **rejected**: RPM is a sibling program stacked on the same platform; several programs run phone-only. Device data feeding the program is optional integration.
- "Care must be delivered by vendor-employed staff" — **rejected**: all four delivery postures (in-house, software-only, managed, full-service) appear in the sample; the service is performed "under physician supervision" either way.
- "A patient mobile app is defining" — **rejected**: the dominant interaction medium is staff-initiated phone/message outreach; apps are common but secondary.
- "CCM is only for primary care" — **rejected**: specialties, FQHCs/RHCs, health systems, ACOs, health plans, and pharmacy delivery partnerships all appear in the sample.
- "Eligibility requires 2+ chronic conditions" — **rejected as universal**: that is the US CCM program's rule; sibling programs extend to single high-risk conditions (PCM) or whole populations (APCM). The invariant is eligibility defined by chronic conditions, with the count set by the regime.

## Boundary Findings

- **vs Care Coordination Platform (processed sibling — joint-review flag answered)** — the sharpest seam, and the flag is **confirmed**: the same products sell both (ThoroughCare's nav carries Care Coordination and Chronic Care Management as sibling functions of one platform; HealthArc names CCM "non-face-to-face care coordination" and ships a /care-coordination/ solution; eCW ships CCM as a module of its care-coordination suite; ChartSpan's FAQ frames CCM as "care coordination activities" delivered as a program). Resolution consistent with the sibling pass's recorded split: **CCM software is the care-coordination machinery bound to a defined chronic-care program** — the program's objects (chronic-condition eligibility, consented enrollment, per-period service documentation, time thresholds, billing) are first-class and load-bearing here, while general coordination treats programs as one deployment shape. Test: remove the chronic-program machinery (eligibility rules, consent gate, per-period time/service documentation, billing outputs) and what remains is a care coordination platform; add a different program overlay (payer utilization program, discharge episode) and it becomes the other deployment. The two leaves therefore document one family from two centers of gravity; both documents cross-reference, and neither subsumes the other in the directory. Not unilaterally merged — recorded as a probable variant-relationship for joint review.
- **vs Care Plan Management (processed sibling)** — the care plan appears in all five products, but only as an element of the program loop: condition-specific templates, dated revisions, write-back to the EHR. Care Plan Management centers the plan as an authored, controlled record; CCM centers the recurring service cycle that the plan organizes. Test: remove the recurring documented service and billing machinery → plan management; keep them and the plan is one program object among five.
- **vs Remote Patient Monitoring** — RPM's defining loop is device-data collection; CCM's is the program service cycle. They co-bill and co-deploy, and RPM readings can feed CCM plans, but removing devices leaves CCM intact (phone-only programs are the norm in the sample). RPM leaf owns the device loop.
- **vs Population Health Management** — PHM is panel-level analytics/registry; CCM is person-level program delivery for the patients PHM would flag. Vendors bundle both (ThoroughCare sells "population health management software" as an analytics function; sibling research records the same bundling from the coordination side).
- **vs Payer Care Management** — the same program machinery owned and operated by health plans over members (TimeDoc and Prevounce sell to health plans as customers; sibling research records payer-side deployments). Organizational ownership and purpose (utilization/cost oversight vs provider-side program delivery) is the boundary; the payer leaf owns it.
- **vs Patient Engagement Platform** — outreach/education machinery appears here, but as the delivery medium of the program record (engagement must be documented against the service period). Engagement platforms have no eligibility/enrollment/time/billing program record.
- **vs sibling Medicare programs (PCM, TCM, APCM, AWV, BHI) — same Type, different program overlays**: the products themselves run these as sibling programs on one platform. TCM is the most divergent (episode-based, discharge-triggered rather than monthly-recurring) and sits closest to the transitions variant of care coordination. The directory has no separate leaves for these; they are Variants here, not Types.
- **vs Telehealth Platform / Patient Scheduling / Practice Management** — visits, bookings, and practice administration are not program records; CCM software arranges visits and consumes EHR context but its defining loop is the between-visit program service.
- "Remove what, and it becomes another Type" summary: remove the chronic-condition eligibility anchor → care coordination; remove the recurring documented service cycle → care plan management; remove the program record entirely (enrollment/documentation/billing) → patient outreach or panel analytics; remove the devices → still this Type (so RPM is not definitional); remove the claims machinery → still this Type (so fee-for-service billing is not definitional).

## Historical / Market-Sample Check

- **Pre-2015 forms**: payer disease-management programs (1990s–2000s) enrolled members with diabetes/asthma/CAD, ran nurse outreach on recurring cycles against care plans, and documented services — payer-funded, no CPT claims. They fit the L0 structure.
- **International forms**: GP-register chronic disease review programs (UK-style) and statutory disease-management programs (German DMP-style) enroll chronic patients, maintain documented disease-management plans, and run recurring reviews — again without US claims machinery. These were not directly sampled (language/availability); the fit is reasoned from the program structure, not observed — flagged in Uncertainties.
- **Platform-native / older tooling**: spreadsheet-and-timer CCM operation (the state HealthArc's "No spreadsheets, no manual timers" framing targets) shows the Type pre-dating specialized software; the software exists to industrialize the program record.
- Conclusion: the canonical definition survives without the current dominant implementation (US Medicare CCM billing). The dominant implementation is recorded as the leading Variant, not the definition.

## Uncertainties

- **No Tier-1 operational documentation and no regulator pages reached** (CMS.gov HTTP 403; no vendor help centers attempted — the sampled products document their machinery on product pages, HealthArc's being documentation-grade). All evidence is Tier-2 official vendor pages. Dollar figures for CPT codes are vendor-claimed national averages and vary by geography/year; they are kept out of the final document.
- **US-centric sample**: all five directly sampled products are US-market. The definition was stress-tested against non-US/payer-funded forms by reasoning, not by direct sampling; a non-US chronic-care program product was not fetched.
- **Consent mechanics per payer** (Medicare Advantage vs original Medicare vs commercial) were not verified beyond the ThoroughCare guide's original-Medicare description.
- **Exact state machines** (enrollment → active → graduated/discharged/opted-out) are not uniformly documented; the final document describes the lifecycle qualitatively.
- The joint-review question with care-coordination-platform is answered as a documented working split (see Boundary Findings), but the ultimate directory consolidation decision belongs to a joint review; recorded in STATUS.md.

## Final Synthesis

Chronic Care Management software is the operational system for running **care-management programs for people with chronic conditions**: it defines and finds the eligible population (chronic-condition records drawn from the patient panel), enrolls patients into the program with documented consent, maintains a condition-oriented care plan for each enrollee, and drives a recurring cycle of non-face-to-face care — outreach calls, medication work, referrals, scheduling, chart review — performed by care staff under clinician supervision and documented per patient per service period, with time tracking and billing/compliance outputs where the regime pays for documented service. Mature products add panel-level eligibility machinery, audit-ready documentation, EHR bi-directional integration, patient communication surfaces, dashboards, and multi-program stacking (CCM alongside RPM, PCM, TCM, APCM, AWV, BHI) on the same objects. The market realizes the Type across delivery poles — software-only platforms, platform+managed coordinators, tech-enabled services companies, and full-service program vendors — and one EHR-embedded pole. The Type is the chronic-care-program member of the care-coordination family: what distinguishes it from general care coordination is the program's own machinery (eligibility, consent, per-period service documentation, billing) as first-class, load-bearing structure.
