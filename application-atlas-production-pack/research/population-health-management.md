# Research Notes — Population Health Management

## Research Goal

Understand what a Population Health Management (PHM) application really is from real products: what the managed object is, what structures it holds, what loop it runs, who uses it, and where its boundaries sit against the neighboring §22 healthcare leaves — especially the pre-hung flag from the payer-care-management pass: *"test whether PHM is the analytics Type and hold this as the operational loop"*.

## Initial Boundary

Working hypothesis at start:

- PHM = software that manages the health of a **defined population** (attributed patients / enrolled members) rather than individual encounters.
- Likely core: population data aggregation → risk stratification → care-gap identification → outreach/action → quality & cost measurement.
- Nearest neighbors: Payer Care Management (operational program loop), Care Coordination Platform (person-first loop), Chronic Care Management (program overlay), Value-based Care Platform (contract machinery), Public Health Surveillance Platform (jurisdiction level), Healthcare Quality Management (quality program governance), Business Intelligence / healthcare analytics (generic analytics), Patient Engagement Platform, EHR.
- Known risk: the category name is used both for pure analytics layers and for full management loops; the sample must resolve which is the Type.

## Research Questions

1. What is the central managed object — the population? the registry? the panel? the cohort?
2. How does a person enter the managed population (attribution, empanelment, enrollment, register inclusion)?
3. What data does the system aggregate, and is multi-source aggregation definitional or common?
4. What exactly is "stratification" and what is it used for?
5. What is a "care gap" and how does a gap become action (worklist, outreach, routing, visit planning)?
6. Is the action loop part of the Type, or is PHM only analytics with hand-off to care management?
7. What quality-measure machinery exists (HEDIS, Stars, eCQM, UDS, MIPS) and is it definitional or regime depth?
8. How do payer-side and provider-side deployments differ?
9. Where is the seam with payer care management, care coordination, and chronic care management?
10. Would older / regional / non-US products (paper disease registries, panel management, register-and-recall systems) still fit the definition?

## Representative Products

Selected for market representation, documentation quality, different product philosophies, and different customer levels:

| Product | Philosophy / position | Customer level |
|---|---|---|
| Arcadia | standalone PHM analytics platform (data platform + registry/stratification + care management applications); payer + provider | enterprise health systems, ACOs, payers, government |
| eClinicalWorks (Value-Based Care / Population Health suite) | EHR-embedded PHM suite sold as modules | ambulatory practices, health centers |
| Health Catalyst | healthcare data & analytics company; PHM as a solution family over a data platform | enterprise health systems |
| Azara Healthcare | PHM for the safety net (community health centers, PCAs, CINs); KLAS #1 Population Health Management | community health centers, small networks |
| ZeOmega (Jiva) | payer-side platform; PHM sold as a separate solution beside care management | health plans, Medicare/Medicaid, ACOs |

## Sources

All fetched 2026-09-09. Tier 1/2 official vendor pages (product and solution pages; no login-gated help centers reached):

- Arcadia — root: https://arcadia.io/ ; PHM use case: https://arcadia.io/population-health ; Patient Registry (Patient Stratification): https://arcadia.io/patient-registry ; Care Manager: https://arcadia.io/care-manager
- eClinicalWorks — Value-Based Care / Population Health suite: https://www.eclinicalworks.com/products-services/population-health-ccmr/ ; HEDIS module: https://www.eclinicalworks.com/products-services/population-health/hedis/
- Health Catalyst — PHM & VBC solution family: https://www.healthcatalyst.com/healthcare-analytics/population-health-value-based-care ; PHM solution: https://www.healthcatalyst.com/healthcare-analytics/population-health-value-based-care/population-health-management
- Azara Healthcare — root: https://www.azarahealthcare.com/ ; DRVS: https://www.azarahealthcare.com/solutions/drvs
- ZeOmega — root: https://www.zeomega.com/ ; PHM solution: https://www.zeomega.com/solutions/population-health-management-solution

Sibling research consulted (not re-fetched): research/payer-care-management.md (pre-hung PHM flag), research/care-coordination-platform.md (eCW suite framing).

Source-access limitation: all fetched pages are official product/solution marketing-documentation pages; no vendor help-center / user-guide articles were reachable in this pass. Precise operational parameters (attribution logic details, measure-update cadences, exact tier thresholds, numeric limits) are therefore NOT asserted anywhere. Assertion strength is calibrated accordingly.

## Product Observations

### Arcadia (evidence layer A — directly observed)

- Positions itself as a "healthcare data platform"; PHM is one use case (/population-health). Platform loop stated as **Aggregate → Analyze → Activate → Automate**.
- Data: "unifying EHRs, claims, SDoH information, and other critical sources" into one foundation.
- **Patient Registry** (product named "Patient Stratification"): "Build cohorts, stratify patients, and close more gaps… Identify high-risk patients for screenings, and instantly reach out with a text-message campaign all from one tool." "Build a comprehensive list of patients with gaps, instantly reach out via text-message, and generate custom reports. Zero in on individual patients, or get a comprehensive view of your population." "Understand risk profiles for specific conditions alongside demographic information, costs, and more for patients in your population."
- PHM use-case page: "identify risk and quality gaps, so you can work to close them"; "hone in on patients in need of care management or healthcare interventions"; "set data-backed goals, then track them with more data, a positive feedback loop".
- **Care Manager** is a *separate application*: "identify patients for care management programs and efficiently manage the tasks and events of the patient's care plan"; care programs, caseloads, shared care plans/tasks, program routing decision trees, automated task execution.
- Customers: providers (systems, ACOs, IDNs), payers (Stars/HEDIS, risk adjustment), government (state/local population health programs), life sciences.
- Other named applications (L3): Vista dashboards, Benchmark Reporting, Contract IQ, Network Modeler, Patient Engagement (Engage), Point-of-Care Insights (EHR integration), Provider-Payer Collaboration, Referral Management, Report Distribution, Risk Suspecting, SDoH Package.

### eClinicalWorks — Value-Based Care / Population Health suite (A)

- The pop-health suite is branded "Value-Based Care" and organized as modules: APCM, Care Planning, CCM, TCM, Care Plan Oversight, RPM, HCC (coding gaps), HEDIS Measures, Disease Explorer, Cost and Utilization Explorer, PCMH.
- **Disease Explorer**: "Gain better visibility and sharper insight into your patient population to target high-risk patients and prioritize care for those who need immediate attention."
- **HEDIS Measures**: "more than 100 clinical quality measures designed to improve healthcare delivery, measure compliance, and evaluate provider performance."
- **HEDIS Analytics** page: "Standard HEDIS Quality Measures are available through the Clinical Quality Measure Dashboard… track compliance across your patient population with integrated point-of-care alerts and patient reminders." Key features: track compliance at the point of care; view/query/measure with customizable filters; set thresholds for group performance; engage non-compliant patients; view care opportunities; **"Enroll patients in registry groups"**; integration with eClinicalMessenger (outreach).
- **HCC**: "Identify coding gaps based on historical coding data… update RAF scores at the point of care."
- Suite framing confirms sibling research: CCM/care planning are modules *inside* the pop-health suite (bundling pole).

### Health Catalyst (A)

- PHM is one solution inside the "Population Health & Value-Based Care" family (beside Care Transformation, VBC Performance, Patient Engagement Efficiency, Network Management).
- PHM solution page — six capability blocks:
  1. **Identify the right populations** — "flexible cohort-building tools… Combine clinical, claims, and SDoH data… customizable logic or prebuilt value sets."
  2. **Stratify risk** — "explainable, adaptable" models; "predict risk across domains (clinical, utilization, cost)."
  3. **Target interventions** — "Prioritize patients for outreach, care, and prevention… Track impact on quality scores, admissions, and utilization."
  4. **Deliver insights to every team member** — role-specific dashboards; "real-time tracking by population, provider, or contract."
  5. **Continuously improve** — "Reassess data sources and **attribution models** regularly. Tune risk models."
  6. **Simplify reporting** — "Automate metrics for CMS, HEDIS… submission-ready reports with full audit trails."
- "Embedded workflows and intervention tracking to close the loop."
- Implementation phases: define/discover (populations, contracts, measures, cohort definitions, risk models, baselines) → act/align (dashboards, outreach programs, embedded workflows) → expand/sustain.

### Azara Healthcare — DRVS (A)

- Self-description: "The leading provider of data-driven analytics, quality measurement and reporting for the community health and physician practice market." KLAS "#1 in Population Health Management" four consecutive years (vendor-published).
- DRVS = "centralized data reporting and analytics solution which facilitates care transformation, drives quality improvement, aids in cost reduction, and simplifies mandated reporting."
- Data: "seamless combination of Clinical, Claims, Practice Management and ADT information"; multi-EHR normalization; "single source of truth."
- Drill: "from an aggregated enterprise view to individual practices, providers and locations, down to individual patient detail."
- Features: Centralized Reporting & Analytics (UDS+, 100+ reports, 600+ measures); Dashboard & Performance Trending (UDS, HEDIS, managed-care contracts); **Cohort Management** ("track both static and dynamic patient groups for care/disease management, grants, research or payer based programs"); **Registry Reports** ("track specific populations of patients by chronic disease, age/gender or advanced filter preferences, such as payer, co-morbidities or health disparities"); **Patient Visit Planning** ("prepares clinical team for patient encounters by identifying care gaps and providing critical data at the point of care"); Risk Stratification module; Transitions of Care reporting; Referral Management reporting ("close the loop"); Care Management & Care Coordination (Care Connect application).
- Applications: Patient Outreach (automated outreach), Cost & Utilization, Benefit Screening, Care Connect.
- Own FAQ definition of the category: "Population health tools help organizations **identify care gaps, stratify risk, and prioritize outreach across entire patient populations**. By combining clinical, claims, and demographic data, these tools allow care teams to proactively find patients who are overdue for screenings, chronic disease management, or follow-up care." / "Effective population health tools include **risk stratification, care gap identification, quality dashboards, and actionable patient lists**."
- Loop stated as: Aggregate & Activate → Simplify & Streamline → Engage & Improve ("close care gaps, improve outcomes, track performance in real time").

### ZeOmega — Jiva PHM solution (A)

- PHM is a **separate solution** on the Jiva platform, beside Care Management, Quality Improvement, Risk Adjustment, SDOH, UM, Member Engagement.
- PHM page: "Leveraging claims, SDOH, and other data sources, Jiva **identifies drivers of disease, stratifies populations based on risk scores, and intelligently routes members to the care management workflows** designed to address their specific needs."
- "A robust set of dashboards and reporting tools provide insight into KPIs and enterprise metrics such as productivity, cost, disease status, and utilization… pre-built visualizations for CMS Star ratings, CMS ACO Quality Measures, and NCQA HEDIS® measures."
- ACO page: "From risk-stratification to gap identification and closure strategies… built in SDOH criteria helps you reach at-risk communities."
- Confirms the payer-side seam: PHM identifies/stratifies/routes; care management executes programs (separate solution).

## Cross-product Comparison

| Structure | Arcadia | eCW | Health Catalyst | Azara | ZeOmega | Verdict |
|---|---|---|---|---|---|---|
| Defined population as managed unit (attributed panel / member base / empaneled patients) | ✓ (population, cohorts) | ✓ (patient population) | ✓ (populations, attribution models) | ✓ (patient populations, cohorts) | ✓ (populations, members) | **Core — all 5** |
| Person-level records inside the population (registry/registry groups/cohort membership) | ✓ (Patient Registry) | ✓ ("enroll patients in registry groups") | ✓ (cohort-building) | ✓ (Cohort Management, Registry Reports) | ✓ (stratified member pictures) | **Core — all 5** |
| Risk stratification / segmentation | ✓ | ✓ (Disease Explorer, HCC RAF) | ✓ (explainable models) | ✓ (Risk Stratification module) | ✓ (risk scores) | Common mature (mechanism varies; simple tiering counts) |
| Care-gap identification | ✓ ("list of patients with gaps") | ✓ (HEDIS gaps, care opportunities) | ✓ (close care gaps) | ✓ (care-gap identification) | ✓ (gap identification & closure) | **Core — all 5** |
| Action loop: outreach / worklists / routing / visit planning | ✓ (text campaigns; Care Manager routing) | ✓ (point-of-care alerts, reminders, eClinicalMessenger) | ✓ (prioritize for outreach; embedded workflows) | ✓ (Patient Outreach, Visit Planning, Care Connect) | ✓ (routes members to care-management workflows) | **Core — all 5** (depth varies) |
| Quality measure computation & reporting | ✓ (HEDIS-certified, benchmarks) | ✓ (HEDIS Analytics, 100+ measures) | ✓ (CMS/HEDIS automation, audit trails) | ✓ (UDS/HEDIS/600+ measures) | ✓ (Stars/HEDIS/ACQ visualizations) | Common mature (existence); regime specifics = variant |
| Multi-source aggregation (EHR+claims+SDoH+ADT) | ✓ | partial (claims via Cost/Utilization Explorer; EHR-native) | ✓ | ✓ | ✓ | Common mature — NOT definitional (single-EHR and paper-registry poles exist) |
| Multi-level drill-down (enterprise→provider→patient) | ✓ | ✓ (practice/provider/patient levels) | ✓ (by population/provider/contract) | ✓ (explicit feature) | ✓ (enterprise KPIs) | Common mature |
| Benchmarking | ✓ (product) | — | — | — | — | Optional |
| Risk adjustment / coding gaps (HCC) | ✓ (Risk Suspecting) | ✓ (HCC module) | ✓ (VBC solution) | — | ✓ (Risk Adjustment solution) | Variant (US payer/MA regime) |
| Care management/coordination execution bundled | ✓ (separate app) | ✓ (CCM/care-planning modules) | ✓ (care transformation family) | ✓ (Care Connect) | ✓ (separate solution PHM routes to) | Variant — bundling common, execution layer is neighboring Types |
| Outreach campaign machinery | ✓ | ✓ | ✓ | ✓ (APO) | ✓ (member engagement solution) | Common mature |
| SDoH / health equity | ✓ (SDoH Package) | — | ✓ (data input) | ✓ (SDOH data) | ✓ (SDOH solution) | Variant |
| Cost & utilization analytics | — | ✓ (module) | — | ✓ (application) | ✓ (KPIs) | Variant |
| Referral / transitions tracking | ✓ (Referral Mgmt app) | ✓ (TCM module) | — | ✓ (modules) | ✓ (Social Care Connect) | Variant |
| Payer↔provider data exchange / VBC reporting | ✓ (Provider-Payer Collaboration) | — | ✓ (VBC Performance) | ✓ (VBC Reporting solution) | ✓ (VBC reporting) | Variant |

## Canonical Model (abstraction hierarchy)

### Level 0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being a Population Health Management application:

1. **The defined population as the managed unit of record.** A persistent, identified population — an attributed patient panel, an enrolled member base, an empaneled or registered patient set — that the organization manages as a whole. Membership is *assigned* (attribution, empanelment, enrollment, register inclusion), not created by encounters. This population is the object to which everything else attaches. Remove → healthcare analytics / BI over encounter data.
2. **Person-level registry records within the population.** Each person in the population carries an assembled picture — conditions, services, measures, risk indicators, status — that makes them individually addressable *from the population view*. The population view is built up from person-level records, not from aggregate statistics alone. Remove → aggregate statistics dashboard.
3. **The stratify → gap → act → measure loop.** The population is continuously segmented by risk and need; person-level care gaps / needs are identified against defined standards (quality measures, disease standards, program criteria); the gaps become tracked work — outreach, visit planning, worklists, routing to care teams or programs; completion rolls back up into population-level measures that are tracked over time. Remove → a static registry or a reporting tool; the "management" is gone.

Jointly-held load-bearing tests:

- 1 alone = member/patient analytics dashboard (BI territory)
- 2 without 1 = disconnected patient records / EHR chart review
- 3 without 1+2 = generic outreach/campaign tool
- 1+2 without 3 = static registry archive
- 1+3 without 2 = aggregate program management with no person-level addressability
- 2+3 without 1 = person-first care coordination territory (no population container)

### Level 1 — Common Mature Structure

- Multi-source data aggregation (EHR/clinical + claims + SDoH + ADT/HIE) normalized into a per-person "single source of truth"
- Risk stratification machinery (tiering, scoring, predictive models — mechanism varies widely)
- Cohort/registry building (static and dynamic groups; condition registries)
- Care-gap identification against measure/disease logic
- Gap worklists and point-of-care delivery (visit planning, EHR plug-ins, alerts)
- Outreach machinery (campaigns, reminders, text/email/phone task generation)
- Quality measure computation and reporting (measure libraries, dashboards, submission support, audit trails)
- Multi-level drill-down (enterprise/network → site/provider → patient)
- Benchmarking and performance trending

### Level 2 — Variant / Optional Structure

- Regime machinery: HEDIS / CMS Stars / eCQM / MIPS (US), UDS (US CHCs), QOF-class register-and-indicator regimes (UK-shaped, inferred), other regional programs
- Risk-adjustment support (HCC-class coding-gap identification, RAF updates)
- Bundled care-management / care-coordination execution modules (the neighboring Types, co-deployed)
- Patient engagement modules (campaigns, portals, reminders as product line)
- Referral management, transitions-of-care tracking
- Cost & utilization analytics
- SDoH / health equity packages
- Payer↔provider data exchange / VBC reporting
- Deployment poles: standalone platform vs EHR-embedded suite vs module inside a payer platform
- Owner poles: provider/ACO vs payer vs government programs

### Level 3 — Vendor-specific Structure

- Arcadia: Vista dashboards, Contract IQ, Network Modeler, Risk Suspecting (Epic-integrated), Engage, Aggregate→Analyze→Activate→Automate framing, Customer Insights Team
- eClinicalWorks: Disease Explorer, Cost and Utilization Explorer, eClinicalMessenger, APCM module, "Value-Based Care" suite branding, PCMH module
- Health Catalyst: DOS platform framing, Ambulatory Intelligence (Suite), six-capability PHM solution packaging, 90-day implementation framing
- Azara: DRVS name, Patient Visit Planning (PVP), Automated Patient Outreach (APO), Care Connect, Benefit Screening, UDS+ reporting emphasis
- ZeOmega: Jiva platform, Care Quality (CQ) Navigator, "intelligently routes members" framing, KLAS payer-care-management awards

## Vendor-specific Findings

- Arcadia sells registry/stratification (Patient Registry) and care-program execution (Care Manager) as **separate applications** on one platform — the cleanest in-sample documentation of the PHM↔care-management seam.
- ZeOmega documents the same seam from the payer side: its PHM solution "routes members to the care management workflows" (a separate solution).
- eCW brands its entire pop-health suite "Value-Based Care" — category naming drift at the vendor level; the module set is PHM-shaped (registries, measures, gaps, explorers) plus program modules.
- Azara's own FAQ is the sample's best vendor-written definition of the category ("identify care gaps, stratify risk, and prioritize outreach across entire patient populations").
- Health Catalyst makes "attribution models" an explicit recurring-configuration object — the clearest vendor naming of the population-definition mechanism.

## Rejected Findings

- **"PHM is purely the analytics/segmentation layer"** — rejected as the full definition: all five sampled products include an action loop (outreach, worklists, visit planning, routing, gap closure) inside their PHM offering. The analytics layer is the engine, not the whole. (This answers the payer pass's test — see Boundary Findings #1.)
- **"PHM = payer care management"** — rejected: the centers differ (population-first loop vs program-first loop); ZeOmega sells them as separate solutions; Arcadia ships registry and care management as separate applications.
- **"Multi-source aggregation is definitional"** — rejected: single-EHR products (eCW Disease Explorer operates on the EHR's own data) and the paper-registry pole satisfy the Type without claims/HIE aggregation.
- **"HEDIS/Stars machinery is definitional"** — rejected: US regime depth; UDS is CHC-specific; register-and-indicator regimes exist elsewhere; the paper-era registry pole has none.
- **"Risk scores / predictive models are definitional"** — rejected: mechanism varies from simple tiering to ML models; the loop only needs segmentation that directs attention.
- **"PHM owns the care plan"** — rejected: care plans belong to care management/coordination Types; PHM products either route to them or bundle them as modules.
- **"PHM is a BI platform for healthcare"** — rejected: the data-platform layer is substrate; the Type's center is the population-care loop, which generic BI lacks.

## Boundary Findings

1. **vs Payer Care Management (§22 sibling, processed — pre-hung flag DISCHARGED).** The payer pass hypothesized "PHM = analytics/segmentation layer; payer care management = operational program loop" and asked this pass to test it. Test result: **the split holds but must be restated** — PHM is not purely analytics (the gap→outreach→closure loop is in-type, present in all five samples), but PHM's loop is **population-first**: aggregate → stratify → identify gaps → route/act → measure at population scope. Payer care management's loop is **program-first**: defined clinical programs (case/disease/UM/transitions) into which members are enrolled and run through documented care-management cycles. Evidence for the seam: ZeOmega sells PHM and Care Management as separate solutions with PHM "routing members to the care management workflows"; Arcadia ships Patient Registry and Care Manager as separate applications; Azara splits DRVS from Care Connect; eCW ships CCM as a module inside the pop-health suite. Bundling is common in both directions; the centers of gravity differ. Keep both leaves; cross-reference.
2. **vs Care Coordination Platform (processed sibling).** Coordination is person-first (person + team + plan + tracked-activity loop); PHM is population-first (the population container is the defining object; persons are addressed through the population lens — cohorts, gaps, worklists). eCW bundles both in one suite (documented in sibling research). Remove the population container and PHM's person-level work becomes care coordination.
3. **vs Chronic Care Management (processed sibling).** CCM = coordination machinery bound to a defined chronic-care program's rules (eligibility, consent, service time, billing). PHM supplies the population view (registries, gap lists) that feeds such programs; the program machinery itself is CCM's center.
4. **vs Value-based Care Platform (§22 sibling, unprocessed).** VBC machinery = payer↔provider contract/payment/quality-reporting layer. PHM produces the population performance that VBC contracts reward, and PHM vendors sell VBC reporting as separate solutions/products (Azara VBC Reporting; Arcadia Contract IQ; Health Catalyst VBC Performance). Proposed discriminator for that pass: contract/payment machinery vs population management loop.
5. **vs Public Health Surveillance Platform (§22 sibling, unprocessed).** Surveillance = jurisdiction/community-level notifiable-condition monitoring and outbreak detection; PHM = management of an attributed/enrolled care population (chronic disease, quality, cost). Arcadia's government use case (state Medicaid/population programs) still operates on enrolled populations, not jurisdiction-wide surveillance. Flag for that pass.
6. **vs Healthcare Quality Management (§22 sibling, unprocessed).** Quality management = the organization's quality-program governance (accreditation, incidents, measure governance); PHM = population-level gap closure. Both touch quality measures; the center differs (program governance vs population care loop). Flag for that pass.
7. **vs Business Intelligence / healthcare analytics.** Generic BI lacks registries, attribution, care-gap logic, and the outreach loop. The data-platform layer of PHM vendors (Arcadia Data Platform, Health Catalyst DOS) is BI-class substrate; the PHM application layer is the Type.
8. **vs Patient Engagement Platform.** Outreach campaigns and reminders are capabilities inside PHM (or bundled modules), not the center; engagement platforms center on the patient-facing relationship surface.
9. **vs EHR.** The EHR holds the encounter/clinical record of record; PHM aggregates across sources (including EHRs) and manages the population as a unit. EHR-embedded PHM (eCW) is a deployment pole, not a different Type.

## Historical / Market-Sample Check

- **Paper-era disease registry + panel management** (group practice keeps a diabetes register: a card per patient with condition status and last services; staff generate recall lists of patients due for checks; outreach by phone/letter; completions marked off; annual register-level audit of control measures): satisfies all three L0 structures — defined population (the register), person-level records (cards), stratify→gap→act→measure (recall + closure + audit) — with no software, claims data, risk scores, or HEDIS. The definition names none of those.
- **Register-and-recall systems in register-based primary care regimes** (UK-shaped QOF-era disease registers and recall systems; held as conceptual lineage, low confidence — no vendor documentation fetched in this pass): register + recall + indicator reporting fits the same three structures; confirms the Type is not US-machinery-shaped.
- **1990s managed-care disease-management registries** (claims-triggered enrollment lists, nurse outreach, program tracking): conceptual lineage; the program-execution half of that world became payer care management, the population-analytics half became PHM.
- **Single-EHR registry products** (eCW Disease Explorer on the EHR's own data) prove multi-source aggregation is common-mature, not invariant.
- The definition therefore holds across eras and regimes; HEDIS/Stars/UDS/risk-score machinery is regime and era depth, not the Type.

## Uncertainties

- All fetched sources are official product/solution pages; no help-center/user-guide articles were reachable. Precise operational parameters (attribution logic, measure-update cadences, tier thresholds, numeric limits) are deliberately not asserted.
- Regional (non-US) PHM products were not fetched; register-and-recall regimes held as conceptual lineage only.
- The exact hand-off behavior when care management is bundled (does a closed gap automatically update the care program? does routing create the enrollment?) — evidenced only as "routing" (ZeOmega) and "program routing decision tree" (Arcadia Care Manager); held product-specific.
- KLAS category naming ("Population Health Management") is vendor-published; treated as market-category evidence, not independent verification.
- Whether government PHM deployments (state Medicaid programs) constitute a distinct variant or the payer pole — held as variant; not separately researched.

## Final Synthesis

Population Health Management is the care organization's **population-facing management system**: it holds a defined, attributed population as the managed unit of record; builds the population view from person-level registry records assembled out of aggregated clinical/claims/social data; and runs a continuous stratify → gap → act → measure loop — segmenting the population by risk and need, identifying person-level care gaps against defined standards, turning gaps into tracked work (outreach, visit planning, worklists, routing to care teams or programs), and rolling completion back up into population-level quality and cost measures that are tracked and reported over time. Around that core, mature products add multi-source aggregation, risk-scoring machinery, cohort/registry tooling, point-of-care delivery, outreach campaigns, quality-measure libraries and submission support, benchmarking, and drill-down from enterprise to patient. The market realizes the Type across deployment poles (standalone platform / EHR-embedded suite / payer-platform module), owner poles (provider & ACO / payer / government / safety-net networks), and bundling poles (care-management execution bundled vs separate). The boundaries that matter: population-first loop vs program-first loop (payer care management), population container vs person-first coordination (care coordination), population management vs contract machinery (value-based care), attributed care population vs jurisdiction surveillance (public health surveillance), and the population-care loop vs generic analytics (BI).
