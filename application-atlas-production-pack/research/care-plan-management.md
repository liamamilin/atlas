# Research Notes — Care Plan Management

## Research Goal

Understand what **Care Plan Management** is as an Application Type: what a "care plan" is inside these systems, what structure it carries, who authors and approves it, how it is kept current, how it connects to care delivery, what rules constrain it, and where its boundaries sit against neighboring healthcare Types — especially **Care Coordination Platform** (which recorded a working split with this leaf in its own pass), EHR, Home Care Agency Management, Home Health EHR, Hospice Management, Skilled Nursing Facility Management, and Chronic Care Management.

Research date: 2026-09-06.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: software whose central managed object is the **care plan as an authored, structured, controlled record** for an identified person — assessed needs → goals → interventions/services — maintained under review/revision cycles and (commonly) operationalized into tasks for care delivery.
- Prior sibling evidence to respect: the care-coordination-platform pass recorded a working split — "care-plan-management = plan-as-authored-document system vs coordination's plan-as-execution-engine (remove the team-execution loop and it becomes plan management; remove document depth and keep the loop and it stays coordination)". This pass tests that split against care-plan-centric products.
- Likely confusion zones:
  1. **Care Coordination Platform** — plans exist in both; the seam is document-control depth vs team-execution loop.
  2. **EHR** — care plans are one document type inside EHRs; here the plan is the central object.
  3. **Home Care Agency Management / Home Health EHR / Hospice / SNF Management** — setting delivery systems that bundle care planning as one module.
  4. **Chronic Care Management** — program overlay on coordination; care plans appear as program artifacts.
- Market reality anticipated: "care plan management" is rarely sold standalone; it ships as the care-planning module of agency platforms, social-care platforms, behavioral-health EHRs, and LTC EHRs. The Type is the plan-record layer, not the surrounding platform.

## Research Questions

1. What exactly is a care plan in these systems — what sections/structure does it carry?
2. Who authors it, under what authority, and how is approval/sign-off handled?
3. What is the plan's lifecycle (draft → active → review → revision → archive; versions)?
4. What inputs feed it (assessments, risk screening, templates, libraries, standardized scores)?
5. How does the plan connect to delivery (task generation, visit schedules, point-of-care documentation, progress notes)?
6. What rules matter (review cadence, consent, audit trail, regulatory evidence, version history)?
7. How do variants differ by setting (home care, residential care, behavioral health, IDD, skilled nursing, senior living, children's services)?
8. Where are the hard boundaries with neighboring Types — especially the recorded coordination split?

## Representative Products

Selected for market spread + product philosophy diversity + customer-tier/segment diversity:

| Product | Positioning | Segment / philosophy |
|---|---|---|
| **AxisCare** | all-in-one home care platform with a dedicated Care Planning feature (home care, skilled care, IDD) | US home-care agency pole; plan → goals → daily activities → outcomes |
| **Birdie** | UK homecare platform; care management module with digital care plans, assessments, SmartPlans AI | UK domiciliary care pole; person-centred plan + inspection evidence |
| **Nourish** | UK social care platform (residential, home care, children's services; formerly CarePlanner) | UK multi-setting social care pole; contextual person-centred plans |
| **Qualifacts** | behavioral health EHR family (CareLogic/Credible/InSync) with a dedicated Treatment Planning module | US behavioral health pole; regulatory treatment plan as clinical document |
| **PointClickCare** | senior living / skilled nursing EHR; Care and Service Delivery package (service plans) | North American LTC EHR pole; EHR-embedded service plans |

Boundary-informing checks: AxisCare's separate "Plan of Care" (skilled care, certification-tracked) vs its "Care Plans" (home/IDD) feature demonstrates the plan-of-care variant inside one product. PointClickCare's SNF Clinical Documentation ("capturing care plans accurately") vs its Senior Living service plans demonstrates the EHR-embedded pole.

## Sources

All fetched 2026-09-06. All reachable sources are **Tier 2 (official product/solution/feature pages)**. No Tier-1 help-center/user-guide articles were reachable from the research environment (see Uncertainties). Operational details are kept qualitative; no precise numeric limits, cadences, or default values are asserted.

- AxisCare — root: https://axiscare.com/ ; Care Plans feature: https://axiscare.com/features/care-plans/ ; Plan of Care feature: https://axiscare.com/features/plan-of-care/ (referenced from root navigation)
- Birdie — root: https://www.birdie.care/ ; Care management: https://www.birdie.care/care-management ; SmartPlans: https://www.birdie.care/smartplans (referenced)
- Nourish — root: https://nourishcare.com/ ; Better Care (residential): https://nourishcare.com/product/better-care/ ; Better Care at Home: https://nourishcare.com/product/better-care-at-home/
- Qualifacts — root: https://www.qualifacts.com/ ; Treatment Plan Management: https://www.qualifacts.com/behavioral-health-software/mental-health-treatment-planning-software/
- PointClickCare — root: https://pointclickcare.com/ ; SNF EHR: https://pointclickcare.com/products/skilled-nursing-platform/ ; Care and Service Delivery package: https://pointclickcare.com/software-packages/care-and-service-delivery-package/

Unreachable (abandoned per network rules after repeated failures): AlayaCare (403 ×2), Log my Care (timeout ×2), Netsmart (transport error ×2).

## Product Observations

### AxisCare (Evidence layer: A — directly observed on official pages)

- Care Plans feature: "Build comprehensive care plans that outline **objectives, goals, and interventions** tailored to each client's specific needs. Across all types of care needs, staff can track progress and align **daily activities** with client goals and preferences to improve outcomes and accountability."
- Real-time monitoring: "Give care team members instant visibility into each client's progress with real time data. Teams can identify trends, **adjust care plans**, and strengthen care coordination across staff. Built in reporting helps support regulatory compliance for billing, state programs, and internal audits."
- Mobile documentation: "Field staff can document care activities, interventions, and **progress toward goals** directly from their mobile device, even when internet access is unreliable."
- Customizable Care Plan Libraries: "Build, manage, and reuse individualized, high-quality care plans more efficiently using **standardized, customizable libraries** that support compliance and accuracy, while streamlining care plan updates and promoting person-centered care."
- Skilled-care variant — Plan of Care: "Track each Plan of Care through **certification** with accurate records, real-time visibility, and secure storage." (a physician-ordered, certification-cycled plan-of-care variant distinct from the agency care plan)
- IDD variant: "Create and manage individualized plans while tracking goals, services, and outcomes"; IDD positioning: "Support person-centered care with tools designed for the unique needs of IDD organizations."
- Surrounding platform (not the plan layer): scheduling, caregiver app, EVV, billing, custom forms, care analytics (AI), RCM.
- L3: Axi AI chat assistant; "350K users" scale figures; Best-in-KLAS badges.

### Birdie (Evidence layer: A)

- Care management: "Digital care plans keep every detail organised from medication schedules to personal preferences"; "Person-centred care aligned to unique client needs and goals."
- Unified client records: "Care plans, visit notes, and eMAR in a single client profile"; "Care plans automatically connect to schedules, visits flow seamlessly to invoices."
- Assessments: "Structured assessments are best-in-class, up-to-date, and fully regulatory compliant"; "Over 25 specialised assessment areas cover all care and risk requirements"; "Smart recommendations suggest further assessments based on what you've recorded"; "Easily audit assessment completion rates and dates."
- SmartPlans (AI drafting): "turns your client conversations into completed care plans in minutes"; "every suggestion cited to what the client said, **ready to review**" — AI drafts are human-reviewed before becoming the plan.
- Responsiveness: customer quote — "Before Birdie, we may have considered a 48hr update to a care plan quite responsive, but now we can do the same in five minutes." (customer-reported, not a product spec)
- Review machinery: "Assessment reviews — Makes it easy to review and deliver responsive care"; risk-level change tracking: "Clear reporting shows when and why a client's risk level has changed."
- Evidence/compliance: "Complete audit trail from assessment through to care delivery"; Q-Score CQC benchmarking; "Essential tasks — Clearly labelled for carer priority and safety."
- Person/family involvement: Family App ("keeps relatives informed and involved"); GP Connect; third-party access with sharing codes; consent forms and care-delivery terms stored as client documents.
- L3: SmartPlans, Q-Score, "60M+ visits annually", "57% average time saved on care planning", 0.6MB-per-report claim.

### Nourish (Evidence layer: A)

- Better Care (residential): "Contextual care plans — Care plans give care workers information on the **everyday needs and preferences** of the people they support. This helps them to understand **why** they are delivering care in a certain way, creating a deeper understanding and enhancing the quality of care being delivered."
- Assessments: "From preventing ulcers to screening for malnutrition, our digital assessments can be easily completed to support your vital work."
- Templates: "Make use of **templates for care plans and assessments**, in line with industry best practices and tailored for the type of care you deliver."
- Handover: "a handover screen, where important information is displayed at the touch of a button… The whole care team will be able to see the latest handover notes."
- Point-of-care app: staff get "instant access to care plans, assessments and daily records"; offline mode; GP Connect integration.
- Family Portal: "secure, real-time access to appointment details, the timeline, assessments, and the care plan. It offers peace of mind and encourages **greater involvement in care planning**."
- Compliance framing: "Evidence care quickly and easily to improve your rating from regulators (CQC, Ofsted, Care Inspectorate etc)."
- Home variant (Better Care at Home): mobile care delivery — "Access client details, care plans, medication, and record unregulated care in the moment"; critical information ("allergies, risks, and protocols, at a glance"); rostering/invoicing integrated (Empower).
- L3: product names (Better Care, Empower, Transparency, Confidence, Insights); CarePlanner acquisition; scale stats.

### Qualifacts (Evidence layer: A)

- Treatment Plan Management: "Our highly configurable treatment plan module streamlines the entire process— providing easy, seamless ways to document **problems, goals, objectives, interventions, and activities**."
- Assessment linkage: "Problems and goals are **tied to scores displayed from standardized assessments**, to facilitate the ease of tracking progress."
- Golden Thread: "Recommendations Module **pulls presenting problems into the Treatment Plan** to maintain the Golden Thread"; "Treatment Plan data is **incorporated into the progress note**, supporting the Golden Thread allowing you to track progress throughout treatment." (The plan is the connective document between assessment and ongoing progress notes.)
- Plan types: "Integrated treatment plans, **program-specific plans**, and service document groups are available."
- Configurability: "Simplified and configurable workflows support your clinical practice and requirements."
- Surrounding EHR (not the plan layer): assessments, progress notes, e-prescribing, measurement-based care, billing, analytics.
- L3: platform names (CareLogic, Credible, InSync); Qualifacts iQ AI suite; "2,200+ agencies" figure.

### PointClickCare (Evidence layer: A)

- Senior living Care and Service Delivery package: "Connect **assessments, service plans, tasks, point-of-care documentation, and medication records** within the senior living EHR."
- Service plans: "Create **individualized service plans that evolve** with resident preferences and changing conditions, **connecting assessments directly to care planning**."
- Task operationalization: "Provide frontline staff with visibility into each resident's **service plan, preferences, and scheduled tasks** directly within the mobile app"; unscheduled task frequency "support[s] accurate billing."
- Progress notes: "Capture progress notes at the point of service to maintain continuity across shifts and support clear communication with families and providers."
- Real-time service coordination (their term): "a workflow that helps senior living teams **assess resident needs, create service plans, document scheduled and unscheduled services**, and use that information to quickly identify and proactively respond when a resident's needs are changing."
- SNF pole: Clinical Documentation — "Improve point of care documentation and manage resident health proactively by **capturing care plans accurately** and viewing clinical data easily"; MDS submission automation (regulatory assessment instrument).
- L3: Companion app; "ADLs in 30 seconds or less" claim; eMAR "five rights"; Best-in-KLAS award.

## Cross-product Comparison

| Dimension | AxisCare | Birdie | Nourish | Qualifacts | PointClickCare |
|---|---|---|---|---|---|
| Identified care recipient as plan subject | yes (client) | yes (client) | yes (person supported / resident / child) | yes (client) | yes (resident) |
| Structured plan: needs/problems → goals → interventions/services | yes (objectives, goals, interventions) | yes (needs and goals; medication schedules; preferences) | yes (everyday needs and preferences; contextual sections) | yes (problems, goals, objectives, interventions, activities) | yes (service plans from assessments; scheduled services) |
| Assessments feed the plan | yes (visit forms/assessments; custom forms) | yes (25+ structured assessments; smart recommendations) | yes (ulcer/malnutrition etc.; templates) | yes (standardized assessment scores tied to problems/goals) | yes (assessments connected directly to care planning) |
| Authored/edited by authorized staff with attribution | yes (agency staff; timestamps on mobile documentation) | yes (audit trail assessment → delivery) | yes (configured platform; staff app) | yes (clinical workflows; configurable) | yes (EHR documentation; point-of-care attribution) |
| Living record — review/revision as needs change | yes ("adjust care plans"; real-time monitoring) | yes (assessment reviews; risk-level change tracking; rapid updates) | yes (up-to-date records; handover of latest state) | yes (progress tracked throughout treatment) | yes ("service plans that evolve with… changing conditions") |
| Plan → tasks/services operationalization | yes (daily activities aligned to goals) | yes (plans connect to schedules; essential tasks) | yes (care workers deliver from plans; rostering adjacent) | not emphasized (plan guides therapy; progress notes) | yes (scheduled tasks; service documentation) |
| Progress recording against plan | yes (progress toward goals; outcomes) | yes (visit notes, logs, observations) | yes (daily records; handover notes) | yes (progress notes incorporate plan data) | yes (point-of-service progress notes; ADL documentation) |
| Templates / libraries | yes (customizable care plan libraries) | yes (structured assessment library) | yes (best-practice templates) | configurable workflows; program-specific plans | EHR-embedded content |
| Approval / certification / sign-off | plan-of-care certification (skilled variant) | not observed at page level | not observed at page level | configurable clinical workflows | not observed at page level |
| Consent / person & family involvement | clients + families role page | consent forms; Family App; sharing codes | Family Portal; involvement in care planning | client engagement suite (adjacent) | family communication via progress notes |
| Regulatory/compliance evidence | billing/state programs/internal audits | CQC Q-Score; audit trail | CQC/Ofsted/Care Inspectorate evidence | behavioral health compliance framing | MDS submission; ONC certification |
| Health-record integration | skilled-care orders/vitals/wound docs | GP Connect; eMAR | GP Connect; eMAR adjacent | EHR-native (assessments/notes/eRx) | EHR-native; eMAR; pharmacy |
| AI drafting of plans | AI analytics (not plan drafting) | SmartPlans (AI drafts, human-reviewed) | AI icon present (depth not observed) | iQ AI documentation (adjacent) | AI workflows (positioning) |
| Delivery form | module in agency platform | module in homecare platform | module in social-care platform | module in behavioral-health EHR | module in LTC EHR |

Reading: every product realizes the same four-part structure — an identified person, a structured plan record (needs → goals → interventions/services), accountable authorship, and a living record revised as needs change. Everything else varies by segment and philosophy. The plan→task operationalization is near-universal in agency/social-care settings but absent (or weak) in behavioral health, where the plan guides therapy and progress notes rather than generating caregiver tasks — confirming that task generation is common mature structure, not the defining core.

## Canonical Abstraction

### L0 — Defining Invariant

Care Plan Management exists to maintain the **plan of care as a controlled record** for an identified person. Minimal structure:

```text
Identified care recipient (the person whose care is planned)
└── Structured care plan record
    (assessed needs/problems → goals/outcomes → interventions/services)
    └── Accountable authorship (created and edited by authorized, attributed staff)
        └── Living record (persisted and revised as the person's needs change)
```

- Remove the identified person as the plan's subject → it becomes generic document management or workflow software, not care planning.
- Remove the needs → goals → interventions structure → it becomes a free-text note or an assessment report, not a care plan. (Even paper-era nursing care plans and social-care support plans carried this problem/goal/intervention skeleton.)
- Remove accountable authorship → it becomes an anonymous knowledge base; care plans are evidentiary records whose authorship matters.
- Remove the living, revised-over-time nature → it becomes a one-shot assessment report; "management" implies the plan is kept current as needs change.

Deliberately **not** in L0 (checked against historical/market-sample reasoning): task generation and visit scheduling (behavioral-health treatment plans work without them), mobile point-of-care apps, AI drafting, family portals, eMAR linkage, billing machinery, regulator-specific evidence formats, EHR embedding, standardized terminologies. Older and regional forms — paper nursing care plans (problem list, goals with target dates, interventions, evaluation), UK social-care support plans in paper folders, behavioral-health treatment plans predating EHRs — all fit the L0 structure without any of these.

### L1 — Common Mature Structure

- **Assessments feeding the plan** — structured assessment instruments (health, functional, risk, social) whose findings flow into plan content; in behavioral health, standardized assessment scores tie directly to problems and goals.
- **Templates and content libraries** — best-practice plan/assessment templates and reusable, standardized libraries that accelerate authoring and support consistency.
- **Plan → task/service operationalization** — plan items expressed as scheduled tasks, daily activities, or service schedules for care staff (near-universal in agency/social-care/senior-living settings).
- **Point-of-care execution surfaces** — mobile apps for caregivers to read the plan and record delivery, including offline operation.
- **Progress recording against plan items** — progress notes, observations, logs, and outcome tracking tied to goals/interventions; in behavioral health, plan data incorporated into progress notes (the "golden thread").
- **Review cycles and revision machinery** — assessment/plan reviews, risk-level change tracking, and (in skilled variants) certification cycles; plan updates in response to changing needs.
- **Consent and person/family involvement** — consent records, family portals/apps, sharing controls, person-centred involvement in planning.
- **Regulatory/compliance evidence** — audit trails from assessment through delivery, inspection-ready reporting, regulator-framed quality evidence.
- **Health-record integration** — GP records access (UK), EHR embedding, eMAR linkage, pharmacy/lab integration depending on setting.
- **Version/audit history** — attributable change history over the plan's life.

### L2 — Variant / Optional Structure

- **Setting/segment variants**: home care (agency plans driving visit tasks), residential/care homes (contextual daily-life plans), behavioral health (treatment plans as regulatory clinical documents), IDD services (individualized goal/service plans), skilled nursing (physician-ordered plan of care under certification cycles), senior living (service plans tied to billing), children's services (safeguarding-oriented plans).
- **Regulatory geography**: US-shaped variants (plan-of-care certification, EVV, Medicaid billing linkage, MDS) vs UK-shaped variants (CQC/Ofsted/Care Inspectorate inspection evidence, person-centred planning duty).
- **Clinical depth**: nursing/clinical care plans with standardized terminologies and assessment scores vs social-care support plans centered on daily life and preferences.
- **Packaging**: standalone care-planning module vs module inside an agency platform vs module inside an EHR — the market rarely sells this Type standalone.
- **AI drafting**: AI-generated plan drafts from assessment conversations, human-reviewed before adoption (emerging; observed in one sampled product).
- **Billing linkage**: service plans whose task/service documentation feeds billing (senior living, home care payer programs).

### L3 — Vendor-specific (kept out of the final document)

- Birdie: SmartPlans, Q-Score, "57% time saved", 0.6MB-per-report, "60M+ visits".
- Nourish: product names (Better Care, Better Care at Home, Empower, Transparency, Confidence, Insights); CarePlanner acquisition lineage.
- AxisCare: Axi AI assistant; Plan of Care certification-tracking specifics; scale figures; award badges.
- Qualifacts: Golden Thread terminology; Recommendations Module; platform names (CareLogic, Credible, InSync); iQ AI suite.
- PointClickCare: Companion app; "ADLs in 30 seconds or less"; eMAR "five rights" framing; Best-in-KLAS.

## Rejected Findings (considered, not promoted)

- "Care plan management = generating tasks for caregivers" — rejected: behavioral-health treatment plans (Qualifacts) guide therapy through progress notes without task generation; task operationalization is L1, common in agency settings but not definitional.
- "AI drafting is defining" — rejected: observed in one product (Birdie SmartPlans) as an emerging capability; L2.
- "Plans must be physician-certified" — rejected: certification is the skilled-care plan-of-care variant (AxisCare skilled; US regulatory shape); social-care and behavioral-health plans have different authority models; L2.
- "Care plans are clinical documents" — rejected: UK social-care plans center on everyday needs, preferences, and life history, not clinical problems; the canonical structure must cover both.
- "The care team's shared execution loop is part of this Type" — rejected: that is the coordination Type's defining loop (per the sibling pass); plan management's center is the record itself. The two are commonly bundled in agency platforms, which is packaging, not Type identity.
- "Risk screening is defining" — rejected: risk-level tracking is common (Birdie) but not universal; L1.

## Boundary Findings

- **vs Care Coordination Platform (sibling, processed)** — the sharpest seam, and the recorded working split **holds** under this pass's evidence. Care plan management centers the plan as an authored, structured, controlled record (structure, authorship, review/revision, version history); care coordination centers the team-execution loop (shared team view, tracked activities, status feedback). Test confirmed: remove the team-execution loop → plan management (behavioral-health treatment plans are exactly this); remove document depth but keep the loop → still coordination. Market reality: agency platforms bundle both (AxisCare's care plans + scheduling/caregiver app; Birdie's plans + rostering; PointClickCare's service plans + "real-time service coordination" workflow) — bundling is packaging, not Type collapse. Joint-review flag from the coordination pass is answered here: split confirmed from the plan side.
- **vs EHR** — EHRs contain care plans as one document type among many (PointClickCare SNF: care plans inside Clinical Documentation). This Type is the dedicated system where the plan is the central managed object with its own authoring/review/versioning machinery. The EHR-embedded pole is a packaging variant, not a different Type.
- **vs Home Care Agency Management / Home Health EHR / Hospice Management / Skilled Nursing Facility Management** — those Types center the agency's/facility's delivery operations (scheduling, visits, EVV, billing, clinical documentation breadth). Care plan management is the plan-record layer that those systems commonly include as one module. AxisCare and Birdie demonstrate the bundling from the agency-platform side.
- **vs Chronic Care Management (sibling, unprocessed)** — per the coordination pass, CCM software is coordination under a program overlay; care plans appear there as program artifacts. No direct conflict with this Type; the flag stands for the CCM leaf's own pass.
- **vs Patient Engagement Platform** — family portals/apps are a common surface here (Birdie Family App, Nourish Family Portal) but the center is the staff-side plan record, not patient-facing outreach.
- **vs Assessment tools / Clinical Documentation Platform** — assessments feed plans; documentation platforms center encounter notes. Neither holds the plan as the central managed record.
- **vs Social Services Case Management** — case files center an episode/case workflow; care plans center the plan record. UK social-care platforms (Nourish) sit near this seam but their care-planning layer is plan-record machinery.
- "Remove what, and it becomes another Type" summary: remove the plan-record depth (structure/authorship/revision) and keep team execution → care coordination; remove the person and plan structure → generic document management; remove the plan as central object and center agency operations → home care agency management; center encounter documentation → clinical documentation/EHR.

## Uncertainties

- **No Tier-1 operational documentation reached** (help centers for the sampled products were either not attempted after root-page evidence sufficed, or unreachable: AlayaCare 403 ×2, Log my Care timeout ×2, Netsmart transport error ×2). All observations are from official product/solution/feature pages. Consequently the final document avoids precise operational claims (review cadences, numeric limits, exact state labels, permission matrices).
- **Approval/sign-off machinery** is directly evidenced only in fragments (AxisCare plan-of-care certification; Qualifacts configurable clinical workflows). The general claim "plans commonly carry review/approval steps" is stated at L1 strength from cross-product framing (review cycles, audit trails) rather than from detailed workflow documentation.
- **Versioning depth** (immutable prior versions vs editable current version) could not be confirmed from reachable sources; stated qualitatively as attributable change history.
- **Standalone care-plan products** were not sampled (the market sample shows module/embedded packaging); a pure-play standalone care-plan editor may exist but was not identified among reachable vendors.
- **Epic / Oracle Health / Cerner nursing care plans** were not fetched (documentation login-gated); referenced only as market context, no claims made.

## Final Synthesis

Care Plan Management is the application Type whose central managed object is the **care plan as a controlled record**: one identified care recipient; a structured plan expressing assessed needs/problems → goals/outcomes → interventions/services; accountable authorship by authorized staff; and a living record that is reviewed and revised as the person's needs change. Around this core, mature products add assessments that feed the plan, templates and content libraries, operationalization of plan items into tasks and service schedules, point-of-care mobile execution and progress recording, review/approval and certification cycles, consent and family involvement, audit trails and regulator-facing evidence, and integration with health records and medication systems. The Type is realized across distinct market poles — home-care agency platforms, UK social-care platforms, behavioral-health EHR treatment planning, and LTC/senior-living EHR service plans — almost always as the care-planning module of a wider platform rather than a standalone product. Its defining difference from Care Coordination Platform is the center of gravity: the plan as authored, controlled record versus the plan as the engine of team execution.
