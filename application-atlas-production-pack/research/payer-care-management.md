# Research Notes — Payer Care Management

Research date: 2026-09-08
Slug: payer-care-management
Leaf: Payer Care Management (§22 Healthcare & Life Sciences)

## Research Goal

Understand, from real products, what "Payer Care Management" software is: what world it models (members? programs? cases? care plans? gaps? risk?), who operates it (health plans' own care teams? delegated vendors?), what the operating loop is (identify → enroll → assess → plan → intervene → document → close), what quality/risk machinery attaches to it, and where its boundaries sit against the §22 siblings that prior passes flagged: Health Plan Administration System (processed — left a flag pointing here), Utilization Management, Care Coordination Platform (processed — left a flag), Chronic Care Management (processed — left a flag), Population Health Management, Value-based Care Platform.

Standing flags carried into this pass:

- From health-plan-administration-system (2026-09-08): "payer-care-management (clinical-program layer evidenced as a distinct center — sampled care platform carries no enrollment/premium/claims of record)"; "Medecision and MHK CareProminence evidence the clinical-program layer as a distinct center (care plans, quality measures, risk models) with no enrollment/premium/claims of record. Keep-both expected; flag for that pass."
- From care-coordination-platform (2026-09-08): "same coordination machinery; boundary is organizational owner and purpose (payer-side utilization/cost oversight of members vs provider-side delivery of coordinated care). Products deploy on both sides (WellSky payer lines; Carium payviders), so treat as deployment pole, not separate Type — boundary belongs to the payer leaf when processed."
- From chronic-care-management (2026-09-08): "the same program machinery owned and operated by health plans over members (TimeDoc and Prevounce sell to health plans as customers). Organizational ownership and purpose (utilization/cost oversight vs provider-side program delivery) is the boundary; the payer leaf owns it."

## Initial Boundary (pre-research hypothesis)

- Hypothesis: Payer Care Management is the health plan's (payer's) clinical-program operating layer: the software health plans use to run care-management programs (case management, disease/chronic care management, transitions, LTSS, behavioral) over their member population — identifying members, enrolling them into programs, assessing, planning care, intervening, documenting, and closing gaps — with quality-measure and risk-adjustment machinery attached.
- Expected core: member-as-care-subject + program portfolio + documented care-management loop.
- Likely confusions: Health Plan Administration System (the payer's system of record — member/eligibility/benefit/premium/claims), Utilization Management (review machinery, often bundled), Care Coordination Platform / Chronic Care Management (provider-side delivery of the same machinery), Population Health Management (analytics layer), Value-based Care Platform (payer↔provider contract/quality-reporting machinery), Patient Engagement Platform (member-facing surfaces), generic Case Management (non-clinical).

## Research Questions

1. What is the central object set — member, program, case, care plan, assessment, intervention/task, gap, risk score — and which object anchors the world?
2. How do members enter programs: identification (claims/clinical analytics, risk stratification), referrals, consent, eligibility criteria?
3. What does the care-management loop look like step by step, and who executes it (plan staff vs delegated vendors)?
4. What program types do payers run, and are they configurable structures or fixed modules?
5. How do quality measures (HEDIS/Stars) and care gaps attach — are they definitional or variant machinery?
6. How does risk adjustment (HCC) attach — definitional or variant?
7. Is utilization management inside this Type, a sibling module, or a separate Type?
8. Does the platform hold any enrollment/premium/claims record of its own (the health-plan-administration flag)?
9. What member-facing and provider-facing surfaces exist?
10. What compliance machinery is structural (documentation standards, regulatory timelines, audit-readiness) vs regime-dependent?
11. What are the market poles (standalone suite vs module vs bundled-in-CAPS vs delegated services; commercial vs Medicare vs Medicaid; payer-run vs payvider)?
12. Historical check: would pre-cloud, pre-HEDIS-Stars payer "medical management" / disease-management operations satisfy the definition?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer poles. The market category name is independently confirmed twice: ZeOmega self-identifies with "Payer Care Management" (Best in KLAS "Payer Care Management Solutions" 2022–2025) and Gartner runs a "Market Guide for U.S. Healthcare Payer Care Management Workflow Applications" (ZeOmega cited as "Visionary Incumbent", 2025).

| Product | Vendor | Philosophy / segment | Evidence reached |
|---|---|---|---|
| Jiva platform — Care Management solution | ZeOmega | Workflow-first payer care management platform; Best in KLAS Payer Care Management 2022–2025; commercial/MA/Medicaid/ACO | Homepage + Care Management solution page (Tier 2), layer A |
| Care Management (+ UM/Quality/Risk solutions) | Medecision | Payer+provider care/UM/quality/risk platform on a unified data layer; Black Book "#1 Client-Rated Payer IT Vendor — Care management, LTSS and complex-care coordination" | Homepage + Care Management solution page (Tier 2), layer A |
| CareProminence Care Management Suite | MHK (MedHok, Hearst Health) | Modular payer suite, care side; Medicare Advantage / D-SNP / LTSS depth; unified with UM + Pharmacy + CAG | Care Management Suite page + UM Suite page (Tier 2), layer A |
| Payer Cloud (quality/risk/outreach) | Inovalon | Data/analytics-first payer pole — boundary anchor; also documents a provider-side "Care Management" product-line mismatch | Payer Cloud navigation + provider-cloud care-management redirect page (Tier 2), layer A |

Unreachable (attempts recorded; no product-specific claims made from them):

- Altruista Health (GuidingCare) — altruistahealth.com 403 ×2 (www and bare domain)
- HealthEdge (Guideline Advantage) — healthedge.com 403 ×1 this pass (also 403 ×2 in the health-plan pass)
- Casenet (TruCare) — transport errors ×2
- Cognizant TriZetto — blocked in the health-plan pass (not retried)

Context sources (already-processed sibling/neighbor leaves, for boundary consistency):

- research/health-plan-administration-system.md + applications/health-plan-administration-system.md (system-of-record vs clinical-program seam; HealthAxis bundles "Utilization Management" + "Patient Care Management" as CAPS capabilities — the bundling pole)
- research/care-coordination-platform.md + applications/care-coordination-platform.md (payer-side deployment pole; owner/purpose boundary)
- research/chronic-care-management.md (payer customers of provider-side CCM vendors; owner/purpose boundary)

## Sources

Fetched 2026-09-08:

- ZeOmega — homepage: https://www.zeomega.com/
- ZeOmega — Care Management solution: https://www.zeomega.com/solutions/care-management-solution
- Medecision — homepage: https://www.medecision.com/
- Medecision — Care Management solution: https://www.medecision.com/solutions/care-management/
- MHK — CareProminence Care Management Suite: https://mhk.com/solutions/mhk-careprominence/care-management-suite/
- MHK — CareProminence Utilization Management Suite: https://mhk.com/solutions/mhk-careprominence/utilization-management-suite/
- Inovalon — payer-cloud care-management URL (redirected to Provider Cloud Care Management): https://www.inovalon.com/products/payer-cloud/care-management/

## Product Observations

### ZeOmega — Jiva platform, Care Management solution (evidence layer: A)

- Category self-identification: homepage title "ZeOmega | #1 Best in KLAS | Payer Care Management | Population Health & More"; "ZeOmega is ranked #1 Best in KLAS for Payer Care Management Solutions in 2022, 2023, 2024, and 2025"; recognized as "Visionary Incumbent" in the "2025 Gartner Market Guide for U.S. Healthcare Payer Care Management Workflow Applications"; Leader in "Everest Group Care Management PEAK® Matrix Assessment for 2024 and 2025". Three independent market-category namings of this Type on one vendor's pages.
- Who we serve: Commercial Health Plans ("A one-stop shop for care management, benefits administration, process automation..."), Health Systems, Accountable Care Organizations ("From risk-stratification to gap identification and closure strategies... built in SDOH criteria"), Medicare Advantage plans ("Built-in risk adjustment to drive consistent success in PMPM payment models and maximize Star ratings performance"), Medicaid-Managed Care Plans ("state-by-state regulatory compliance").
- Solution portfolio (nav): Jiva Platform, Care Management, Population Health Management, Quality Improvement, Risk Adjustment, SDOH, Smart Auth Gateway (electronic prior authorization), Member Engagement, Utilization Management, Social Care Connect ("closed-loop referral management"), Smart UM Suite, Delegated Clinical Services. Observation: care management, UM, quality, risk adjustment, and member engagement are separate named solutions of one platform — the workflow-application family bundled.
- Care Management key features (verbatim list): "Performs risk identification and visibility"; "Updates to risk identifiers to appropriately manage risk levels"; "Fully supports NCQA's complex case management practices"; "Holistically generates assessment to evaluate member needs"; "Creates auto recommendations of care plan goals and interventions for ongoing management".
- AI-powered care management: "combining the power of AI with world-class clinical content and workflow automation logic to focus your teams on 'next best actions.' By automating routine tasks and screening out the 'noise' in member data..."
- UM relationship: "The Utilization Management (UM) capabilities in Jiva give healthcare organizations the insights and tools needed to better guide the use and effectiveness of healthcare services"; UM described as "a highly efficient, early adopter tool for identifying quality candidates for chronic care management programs" — UM as sibling module AND as an identification source for care programs.
- Program scope: "Jiva covers all the bases for identifying and managing members who would benefit from chronic care management programs and/or acute care management"; "evidence-based protocols and automated workflow guides users through the appropriate steps"; analytics "helps predict a member's health outcome and appropriately schedule care interventions".
- Quality machinery: Jiva Care Quality (CQ) Navigator — "centralizes HEDIS and CMS Stars quality program data, improves care gap closure rates, and empowers value-based care reporting".
- Case-study evidence of deployments: Alliance Behavioral Health (NC — "mental health challenges, addiction issues, and intellectual disabilities"); Kern Health Systems ("Consolidate Data and Identify Opportunities to Improve and Streamline Care Management"); a large ACO ("Connect Interdisciplinary Care Teams"); Amalgamated Medical Care Management ("100% Compliance for Depression Screening").
- Platform-breadth nuance: homepage markets "benefits administration" among Jiva's uses — a platform-breadth claim; the care-management solution page itself names no enrollment/premium/claims machinery. Recorded as a packaging-breadth variant, not evidence that the care-management center holds a claims of record.

### Medecision — Care Management solution (evidence layer: A)

- Positioning: "Data to doing." "Purpose-built for health plans and providers, our platform transforms fragmented data into actionable intelligence, powering event-driven workflows and timely, automated interventions"; audiences: Commercial Health Plans, Government Health Plans, Third-Party Administrators, Providers. Black Book 2026: "#1 Client-Rated Payer IT Vendor — Category: Care management, LTSS and complex-care coordination"; Frost & Sullivan Innovator 2026 (US Population Health Management).
- Solutions by use case: Care Management, Utilization Management, Quality Management, Risk Management, Pharmacy Management, Provider Enablement, Patient Engagement. Observation (re-confirmed this pass): NO enrollment, eligibility, premium billing, or claims adjudication anywhere on the payer solutions — the clinical-program layer beside the administration core.
- Care Management page components: **Plan of Care** ("real-time collaboration and goal tracking... patient-centered care"); **Guided Health Journeys** ("Engage individuals across all risk profiles—from low, to rising, to high-risk—through personalized, real-time, guided health journeys"); **Pharmacy Care Management**; **Care Gaps** ("Proactively close care gaps... every patient gets the attention they need, when they need it"); **Digital HRA** ("Drive higher HRA completion rates and accelerate risk identification & care program enrollment through digital HRA").
- AI agents (AgentFoundry): Care Plan Recommendation Agent ("Suggests evidence-based plans of care tailored to patient needs"), Medical Necessity Agent, Document Review Agent, Gap Closure Agent ("Improve quality scores and incentive performance through proactive, data-driven gap identification"), Risk Adjustment Coding Agent, Benefits Review Agent.
- Quality Management solution: "industry-standard HEDIS measures engine", "retrospective and post-audit reviews", "administrator worklist to track performance and close quality gaps".
- Risk Management solution: "advanced HCC risk models and streamlined chart review workflows"; "Identify uncaptured diagnosis codes"; "intelligent suspect condition insights".
- UM solution: "prior authorization and care review with AI-powered policy management and automated decision rules"; "integrated appeals and grievances"; "peer-to-peer scheduling".
- Testimonial evidence (roles and actions): "find our patients, evaluate acuity, prioritize and coordinate actions" (home/community-based care IT director); "process authorizations much more easily for all of our Medicare Advantage members"; "members' risk scores – including pharmacy and lab data – are there"; "everything coordinated in one system" (MA plan data-management VP).

### MHK — CareProminence Care Management Suite (evidence layer: A)

- Positioning: "End-to-End Care Management Software for Whole-Person Care"; "unify all medical management activities across the member journey"; D-SNP emphasis ("Whether addressing the needs and complexity of Dual Eligible Special Needs Plans (D-SNPs) or other member groups").
- Key features: **Holistic Care Management** ("team-based, member-centered approach... unify all care management activities"); **Streamlined Processes** ("Eliminate manual case assignments... bulk assignment capabilities and workflow automations"); **Care Plan Automation** ("Create, update and track care plan progress... in accordance with regulatory compliance requirements"); **Comprehensive Member View** ("360Member®" — "real-time access to medical, pharmacy and behavioral health data"); **Seamless Transitions of Care** ("reduce readmissions and improve care continuity"); **Built-in Compliance** ("audit-readiness... regulatory reviews"); **Effective Population Health Management** ("Identify and manage high-risk members... early interventions and eliminate care gaps").
- Journey sentence: "Simplify the entire care management journey—from referral to resolution—with intelligent workflows, embedded assessments and personalized care planning."
- Named components (the program portfolio, verbatim): **Case Management** ("assessments, individualized care plans, provider communication, member education and ongoing monitoring"); **Disease Management** ("Identify and support members with chronic conditions using configurable templates, work queues and resource referral tools"); **Care Coordination** ("transitions across care settings... real-time provider communication and integrated care handoffs"); **Long-Term Services and Support / Managed Long-Term Care** ("detailed assessments to determine service needs, community-based service referrals and personalized care or service plans"); **D-SNP Care Management** ("complex health needs, high-compliance standards and tight regulatory timelines"); **Medication Reconciliation and Drug Utilization Review** ("auto-generates medication lists, flags duplications or interactions and prompts clinician follow-up").
- Member-facing: Cares Member Mobile App (iOS/Android) — "video messaging, medication alerts and real-time data synchronization with CareProminence".
- Platform context: "CareProminence places the member at the center of care... unifying Utilization Management, Care Management, Pharmacy Management, and Complaints, Appeals, & Grievances within a single platform". The market-side suites (enrollment, premium billing, financial reconciliation, web portals) live in the sibling MarketProminence line — care side and market side are separate suite families.
- UM Suite page (sibling-module evidence): "medical necessity reviews on prior authorizations, concurrent inpatient cases or post-service requests"; integrated clinical criteria (MCG, InterQual, CMS NCD/LCD named); FHIR APIs (CRD/DTR/PAS); "continual monitoring of regulatory compliance and turnaround times specific to each line of business".

### Inovalon — Payer Cloud (evidence layer: A — boundary anchor + mismatch)

- Product-mismatch finding: the URL /products/payer-cloud/care-management/ redirects to the **Provider Cloud "Care Management"** page — a provider-side care-quality suite (infection prevention, pharmacy surveillance, safety management, MDS intelligence, quality management, audit management) serving health systems and facilities. That product line belongs to a different Application Type (provider-side care quality management), NOT payer care management. Recorded to prevent future passes from sampling it here.
- Inovalon's payer-side portfolio (navigation): Quality Measurement (Converged Quality, Digital Quality Measures, benchmarking), Risk Score Accuracy (Converged Risk, Converged Record Review, Converged Patient Assessment, encounter submissions), Member Outreach (Converged Outreach, Converged Patient Assessment), Value-Based Care Management (Converged Provider Enablement), Healthcare Data Lake.
- Observation: Inovalon's payer pole is data/analytics-first — quality-measure and risk-score machinery plus outreach — with no documented care-management workflow application in the fetched material. Useful as the analytics-pole boundary anchor: the quality/risk/outreach machinery exists both attached to workflow platforms (ZeOmega/Medecision/MHK) and as standalone data products (Inovalon).

### Context from sibling passes (evidence layer: B — cross-product/cross-pass)

- health-plan-administration-system pass: Medecision observed as the clinical-program layer with no enrollment/premium/claims of record; MHK CareProminence as the care-side suite family; HealthAxis (CAPS) bundles "Utilization Management" and "Patient Care Management" as capabilities of the administration core — the bundling pole, confirming that the same machinery can ship inside a CAPS as a module.
- care-coordination-platform pass: the same coordination machinery deploys on both sides; payer-side = utilization/cost oversight of members; provider-side = delivery of coordinated care. WellSky payer lines and Carium payviders named as both-sides evidence.
- chronic-care-management pass: provider-side CCM vendors (TimeDoc, Prevounce) sell to health plans as customers — the program machinery is shared; organizational ownership and purpose is the seam.

## Cross-product Comparison

| Dimension | ZeOmega Jiva | Medecision | MHK CareProminence CM | Inovalon Payer Cloud |
|---|---|---|---|---|
| Member as care subject (assembled picture) | risk identification/visibility; member data "noise" screened | unified data platform; risk scores incl. pharmacy/lab data | 360Member: medical + pharmacy + behavioral in real time | data lake; quality/risk analytics over linked data |
| Program portfolio | chronic + acute care management programs; NCQA complex case management | guided health journeys by risk tier; care programs via digital HRA enrollment | case mgmt, disease mgmt, care coordination, LTSS/MLTC, D-SNP, med rec — named components | (no workflow programs documented — outreach campaigns instead) |
| Documented loop (assess → plan → intervene → document) | assessment → auto care plan goals/interventions → next-best-action workflow | plan of care w/ goal tracking; check-ins & alerts; care-gap closure | referral → resolution; embedded assessments; care plan create/update/track; bulk assignment | (outreach + record review, no care-plan loop) |
| Quality/gaps machinery | CQ Navigator: HEDIS + CMS Stars, gap closure | HEDIS measures engine; gap closure agent; administrator worklist | population health & quality sibling suite; "eliminate care gaps" | Converged Quality / Digital Quality Measures (standalone) |
| Risk adjustment machinery | built-in risk adjustment (MA, PMPM, Stars) | HCC risk models; chart review; uncaptured codes; coding agent | (via sibling suites) | Converged Risk / Record Review (standalone) |
| UM relationship | embedded UM capabilities; UM as identification source | separate UM solution (prior auth, appeals) | separate UM suite, unified on platform | (not in fetched scope) |
| Member-facing | Member Engagement Navigator | patient engagement: campaigns, scheduling, check-ins, chat | Cares member app: video messaging, medication alerts | Converged Outreach (campaigns) |
| Provider-facing | Jiva provider portal | provider enablement: portal, direct messaging to EMR, SMART on FHIR | provider communication, care handoffs | Converged Provider Enablement |
| Compliance posture | NCQA practices; fully-compliant programs; state-by-state (Medicaid) | (audit reviews in quality) | built-in compliance; audit-readiness; D-SNP regulatory timelines | (submissions machinery) |
| SDOH | SDOH platform + Social Care Connect closed-loop referrals | (social determinants named in positioning) | community-based service referrals (LTSS) | SDOH market insights (analytics) |
| Enrollment/premium/claims of record | none named on care solution (platform claims broader "benefits administration") | none — confirmed absent | none — lives in sibling MarketProminence | none |

Stable across the workflow-platform sample (ZeOmega, Medecision, MHK): member-as-care-subject with an assembled multi-source picture; a program portfolio with eligibility/stratification; the assess → plan → intervene → document loop executed by plan care teams; care-gap and quality machinery; member- and provider-facing seams; compliance-grade documentation. Variable: UM bundling, risk-adjustment depth, SDOH depth, member-app depth, program mix, packaging.

## Canonical Abstraction

### Level 0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being recognizable as payer care management:

1. **The member as care subject** — the plan's enrolled population held as identified members, each carrying an assembled care picture (conditions, risk, utilization, medications, quality gaps, social factors) built from claims, clinical, pharmacy, and assessment data. The member is held as a *care subject*, not as a coverage record: the platform holds no enrollment, premium, or claims-adjudication record of its own. Remove → member analytics dashboard / data warehouse.
2. **The care program portfolio** — the plan's defined clinical programs (case management, disease/chronic-care management, utilization management, transitions of care, LTSS, behavioral health, maternity…) held as configurable structures with identification/stratification criteria, into which members are matched, prioritized, and enrolled. Remove → ad-hoc outreach tool with no program semantics.
3. **The documented care-management loop** — per-member work executed by the plan's care teams: assessment → individualized care plan (goals + interventions) → outreach/intervention/coordination (with members, providers, community resources) → documentation → progress/outcome tracking to resolution or graduation, under compliance-grade, audit-ready documentation. Remove → analytics/reporting layer with no operational loop.

Jointly-held is load-bearing:

- 1 alone = member data/analytics platform (the Inovalon pole without the loop)
- 2 alone = a program catalog
- 3 without 1+2 = generic care-coordination/case tool (provider-side territory)
- 1+2 without 3 = stratification and program assignment with no executed care work
- 1+3 without 2 = ad-hoc outreach with no program semantics
- 2+3 without 1 = program machinery with no member population

The payer overlay (operated by/for a health plan over its insured population, toward cost/quality/utilization aims) is what separates this Type from provider-side care coordination — carried inside structure 1 (the plan's member population) and structure 3 (the plan's care teams).

### Level 1 — Common Mature Structure

Present in most mature products; not definitional:

- risk stratification & predictive identification (analytics over claims/clinical/pharmacy data; "next best action" surfacing)
- care-gap identification & closure worklists (quality-measure machinery: HEDIS/Stars-class)
- risk-adjustment support (HCC-class coding gaps, chart review, suspect conditions)
- utilization-management workflow as a sibling module (prior auth, concurrent review) — commonly co-deployed, sometimes bundled
- member engagement surfaces (portal/app, campaigns, check-ins, secure messaging, HRAs)
- provider-facing seam (provider portal, clinical data exchange, FHIR-class APIs, care handoffs)
- SDOH assessment & community referral (closed-loop referral management)
- pharmacy management / medication reconciliation & drug-utilization review
- appeals & grievances linkage
- work queues, task automation, bulk/case assignment
- compliance & audit machinery (documentation standards, regulatory timelines, audit-readiness)
- reporting & dashboards (program performance, quality scores, utilization)

### Level 2 — Variant / Optional Structure

- packaging: standalone care-management suite vs module inside a payer platform family vs bundled inside a CAPS (HealthAxis pole) vs delegated clinical services (vendor operates programs for the plan)
- program-mix depth: government-program pole (D-SNP, LTSS/managed long-term care, Medicaid state-specific compliance) vs commercial pole; behavioral-health carve-outs
- deployment owner: payer-run vs payvider (provider organizations running payer-style programs) vs delegated vendors
- data/analytics-first vs workflow-first poles (Inovalon vs ZeOmega/MHK)
- member-app depth (from none to full mobile apps with messaging and alerts)
- regional regimes: statutory-fund chronic-disease programs outside the US-shaped sample (inferred, low confidence — no vendor docs fetched)

### Level 3 — Vendor-specific Structure

- ZeOmega: Jiva Care Quality (CQ) Navigator, Smart Auth Gateway, Social Care Connect, Smart UM Suite, Delegated Clinical Services, KLAS/Gartner/Everest award claims
- Medecision: Unified Data Platform, AgentFoundry named agents (Care Plan Recommendation, Medical Necessity, Document Review, Gap Closure, Risk Adjustment Coding, Benefits Review), ember client portal, "guided health journeys" framing
- MHK: 360Member, Cares Member Mobile App, SmartProminence Orchestrator, DataVisor, MarketProminence/CareProminence suite split
- Inovalon: Converged product family naming, Healthcare Data Lake

## Vendor-specific Findings

- ZeOmega's platform-breadth claim ("benefits administration" on the homepage) — a Jiva-platform marketing breadth; the care-management solution page names no enrollment/premium/claims machinery. Held as packaging nuance, not boundary evidence in either direction.
- Medecision's "guided health journeys" (engagement across low/rising/high-risk tiers) — a consumer-engagement-flavored framing of program enrollment; single-vendor.
- MHK's D-SNP/LTSS depth — government-program pole specialization; single-vendor depth evidence, consistent with the MA/Medicaid variant.
- Medecision's AI-agent naming — vendor-specific packaging of gap-closure/risk-coding automation.

## Rejected Findings

- "Payer care management = population health management" — rejected: population-health analytics is a bundled capability or adjacent solution (ZeOmega sells PHM as a separate solution; Medecision's Frost category is pop health but its solutions split care/UM/quality/risk). The operational program loop is the center.
- "UM is part of the definition" — rejected: UM ships as a separate suite (MHK), a separate solution (Medecision), and has its own directory leaf; co-deployment/bundling is packaging. UM appears here as sibling module and identification source.
- "The platform includes enrollment/premium/claims of record" — rejected for the Type's center: Medecision's payer solutions have none; MHK splits market-side from care-side; only ZeOmega's platform-level marketing claims broader enterprise scope. The care-management center carries no such record.
- "AI / next-best-action is definitional" — rejected: current-cycle machinery; the loop predates it.
- "HEDIS/Stars machinery is definitional" — rejected: US government-program machinery; variant depth (commercial plans use different quality programs; older/regional regimes have none).
- "Inovalon's 'Care Management' product line is payer care management" — rejected: provider-side care-quality suite (mismatch documented above).

## Boundary Findings

1. **vs Health Plan Administration System (processed sibling — flag answered)**: the payer's system of record (member/eligibility/benefit/premium/obligation) vs the clinical-program layer (programs, care plans, interventions, gaps, risk). Test: remove the care programs and loop → administration system; add enrollment/premium/claims of record to a care-management product → it becomes a CAPS. Keep-both confirmed; the sampled care platforms carry no enrollment/premium/claims of record (Medecision absent; MHK splits suites; ZeOmega care solution silent).
2. **vs Utilization Management (§22 sibling, unprocessed)**: UM is the review machinery (prior authorization, concurrent/retrospective review, medical necessity); payer care management is the broader program portfolio of which UM is one program type. In this sample UM always appears as a sibling module or separate solution — never as the whole. The UM leaf should own the review depth; this leaf owns the program portfolio and loop. Joint-review flag for the UM pass.
3. **vs Care Coordination Platform / Chronic Care Management (processed siblings — flags answered)**: same coordination/program machinery, different organizational owner and purpose — payer-side oversight of members (cost/quality/utilization) vs provider-side delivery of coordinated care. Products deploy on both sides; the payer leaf owns the payer-owned deployment. Both prior flags resolved consistent with this split.
4. **vs Population Health Management (§22 sibling, unprocessed)**: PHM is the analytics/segmentation layer (risk models, panels, measure reporting); payer care management is the operational program loop executed on members. Commonly bundled; separable solutions in-sample. Flag for the PHM pass.
5. **vs Value-based Care Platform (§22 sibling, unprocessed)**: VBC machinery is the payer↔provider contract/payment/quality-reporting layer; payer care management is the plan's own member-facing care operations. Adjacent, often co-deployed in the same vendor portfolios (ZeOmega "value-based care reporting"; Inovalon "Value-Based Care Management").
6. **vs Patient Engagement Platform**: engagement surfaces (campaigns, apps, check-ins) are capabilities inside this Type, not the center.
7. **vs provider-side care quality management (Inovalon provider-cloud pole)**: different owner entirely (facilities/health systems); the "Care Management" label collision is documented as a mismatch.
8. **vs generic Case Management**: generic case tools lack the clinical program machinery, quality/risk machinery, and payer population context.

## Historical / Market-Sample Check

- 1990s–2000s payer "medical management" / disease-management operations: nurse case managers working from claims-triggered reports, paper or early-electronic case files, phone outreach, program enrollment criteria, documented care plans and closures — satisfies all three L0 structures with no cloud, AI, HEDIS Stars, FHIR, or member apps. The definition names none of those.
- Managed-care organizations' combined "medical management" platforms (UM + CM in one system) — the MHK "medical management activities" umbrella wording documents the lineage term.
- Regional/statutory regimes: statutory insurance funds running chronic-disease management programs (enrolled population, program criteria, documented coordination) fit the same structures — inferred, low confidence, no vendor documentation fetched.
- The definition therefore holds across eras and regimes; HEDIS/Stars/D-SNP machinery is regime depth, not the Type.

## Uncertainties

- No universal program taxonomy: each vendor lists its own program mix; the portfolio's exact composition varies by plan and regime. Documented as configurable portfolio, not a fixed list.
- ZeOmega's "benefits administration" platform claim could not be verified deeper (no enrollment/billing product page fetched); recorded as platform-breadth claim only.
- Delegated clinical services (ZeOmega) — single-vendor page; product-specific until corroborated.
- Regional (non-US) payer care programs — inferred from structure, not from fetched sources; low confidence.
- Exact NCQA/URAC accreditation posture of sampled products — not researched; not asserted.
- The precise seam behavior when UM is bundled (does the UM determination feed the care program automatically?) — evidenced only as "UM as identification source" at ZeOmega; held product-specific.

## Final Synthesis

Payer Care Management is the health plan's clinical-program operating layer: the software a payer uses to run care-management programs over its member population. Its defining core is three jointly-held structures: the member as care subject (an enrolled population held with assembled clinical/cost/quality pictures built from claims, clinical, pharmacy, and assessment data — with no enrollment/premium/claims record of its own); the care program portfolio (the plan's defined clinical programs — case management, disease management, utilization management, transitions, LTSS, behavioral — as configurable structures that identify, stratify, and enroll members); and the documented care-management loop (assessment → individualized care plan → outreach/intervention/coordination → documentation → outcome tracking, executed by the plan's care teams under compliance-grade documentation). Around that core, mature products add risk stratification and predictive identification, care-gap closure and quality-measure machinery, risk-adjustment support, UM workflow as a sibling module, member engagement surfaces, provider-facing seams, SDOH referral, pharmacy management, appeals linkage, work-queue automation, and audit-ready compliance machinery. The market realizes the Type across packaging poles (standalone suite, module in a payer platform family, bundled inside a CAPS, delegated services), program-mix poles (commercial vs Medicare/D-SNP/LTSS vs Medicaid), and posture poles (workflow-first vs data/analytics-first). The boundaries that matter: system of record vs clinical-program layer (health plan administration), review machinery vs program portfolio (utilization management), payer-side oversight vs provider-side delivery (care coordination / chronic care management), analytics layer vs operational loop (population health management), and payer↔provider contract machinery vs the plan's own care operations (value-based care).
