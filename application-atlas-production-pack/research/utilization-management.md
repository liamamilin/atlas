# Research Notes — Utilization Management

Research date: 2026-09-09
Methodology: WORKFLOW_v1.1 (10-step) + WRITING_GUIDE_v1.1

## Research Goal

Understand, from real products, what Utilization Management (UM) software is as an Application Type: what the payer's (or delegated entity's) clinical review program consists of, what objects exist inside it (cases, criteria, determinations, review modes), how a review actually moves from care under question to a recorded determination, how the program operates across the care timeline, who operates it (in-house vs delegated), and where the boundaries lie against Prior Authorization Platform (sibling leaf that left a joint-review flag pointing here), Payer Care Management, Health Plan Administration System, Payer Claims Processing, and the provider-side utilization-review operation observed in the market.

## Initial Boundary (Understand step)

- Core hypothesis: UM = the health plan's clinical review discipline — evaluating the medical necessity/appropriateness of care against criteria to recorded determinations, spanning prospective (prior auth), concurrent (active stays), and retrospective (post-service) review, run as a standing program with reviewer staffing, compliance/turnaround machinery, and delegation governance.
- Users: UM nurse reviewers (first-level clinical review), physician reviewers / medical directors (escalation, peer-to-peer), UM program/operations managers, delegated UM organizations; providers as counterparties.
- Nearest neighbors: Prior Authorization Platform (processed 2026-09-09 — proposed seam: UM = program vs PA = request machinery), Payer Care Management (processed — flag: review machinery vs program portfolio), Health Plan Administration System (processed — flag: UM linkage standard capability), Payer Claims Processing (processed — authorization status input), Healthcare Quality Management, Referral Management, and the provider-side UM operation (Waystar pole — new question this pass).
- Unknowns entering research: (1) does the leaf's center hold all three review timings or only prior-auth review? (2) is delegation governance L0 or L1? (3) is the provider-seat UM operation the same Type or an adjacent mirror? (4) what role do third-party criteria sets (MCG/InterQual) play — core or substrate?

## Research Questions

1. What is the unit of record in UM software — the request, the case, the review, or the program?
2. What review modes do UM products support, and is concurrent review in-scope for this leaf or the PA sibling?
3. What is the reviewer staffing/escalation structure (nurse first review, physician escalation, peer-to-peer)?
4. How do criteria work — plan medical policy, third-party criteria sets (MCG/InterQual/NCD/LCD), client-defined rules?
5. What automation exists (auto-adjudication, AI recommendation) and where does the human stay in the loop?
6. How does delegation work (insourced/outsourced/hybrid; routing to delegated vendors)?
7. What compliance machinery exists (turnaround times, alerts, audit reporting)?
8. How does UM link outward — to claims adjudication, appeals, care management?
9. Where exactly is the seam with the PA sibling, and how should the packaging overlap in both directions be resolved?
10. Does the provider-side "Utilization Management" product (Waystar) belong to this Type?

## Representative Products

Selection: market representativeness (payer UM operational software across packaging poles) + documentation completeness + different product philosophies (workflow suite / platform module / delegated service / AI decision layer / care-suite solution) + boundary testing (provider seat).

| Product | Pole | Customers |
|---|---|---|
| MHK CareProminence Utilization Management Suite | dedicated payer UM workflow suite; explicit three-timing scope | health plans, PBMs |
| ZeOmega Jiva Utilization Management + Smart UM Suite | UM as module of a payer platform family + agentic-AI UM suite | health plans (commercial/MA/Medicaid), health systems, ACOs |
| Cohere Health (Utilization Management suite) | payer UM automation, in-house + delegated specialty UM operating models | health plans (regional to national) |
| Availity Intelligent Utilization Management | AI decision-support/intake layer that integrates TO payer UM platforms | health plans |
| Medecision (Utilization Management solution) | UM as use-case solution of a payer care-side suite | commercial/government plans, TPAs |
| Waystar Utilization Management | provider-seat utilization review (boundary-test pole) | hospitals/health systems |

## Sources

All fetched 2026-09-09 (Tier 1/2 — official product pages):

- MHK — CareProminence Utilization Management Suite: https://mhk.com/solutions/mhk-careprominence/utilization-management-suite/
- ZeOmega — Healthcare Utilization Management: https://www.zeomega.com/solutions/healthcare-utilization-management
- ZeOmega — Smart UM Suite: https://www.zeomega.com/solutions/smart-um-suite
- ZeOmega — sitemap (URL discovery): https://www.zeomega.com/sitemap.xml
- Cohere Health — homepage: https://coherehealth.com/
- Cohere Health — Utilization Management suite: https://coherehealth.com/utilization-management-suite/
- Availity — Intelligent Utilization Management: https://www.availity.com/intelligentum/
- Medecision — Utilization Management: https://www.medecision.com/solutions/utilization-management/
- Waystar — Utilization Management: https://www.waystar.com/our-platform/clinical-integrity-revenue-capture/utilization-management/

Inherited from the project's own sibling-pass corpus (recorded in research/prior-authorization-platform.md, fetched 2026-09-09): X12 official transaction-set documentation — 278 Health Care Services Review names "payors, plan sponsors, providers, utilization management and other entities involved in health care services review" as expected users.

Sibling-pass research notes reused for context (same repository): research/prior-authorization-platform.md, research/payer-care-management.md, research/health-plan-administration-system.md.

Sourcing limitations: legacy enterprise payer engines (TriZetto, HealthEdge, Optum/Change) not directly documented (consistent with prior sibling passes — market anchors only); criteria vendors (MCG, InterQual) researched only as integrations referenced by sampled products, not as products; no non-US UM product sampled.

## Product A — MHK CareProminence Utilization Management Suite

Evidence layer: A (direct, official product page).

### Key observations

- Positioning: "Utilization Management Software for Timely, Evidence-Based Care"; health plans "perform high-quality, timely reviews cost-effectively".
- **Three review timings in one sentence**: "Whether conducting medical necessity reviews on prior authorizations, concurrent inpatient cases or post-service requests, MHK's Utilization Management Suite streamlines the entire process." — prospective (prior auth), concurrent (inpatient), retrospective (post-service) all named as the suite's subject. (A)
- "Real-time review capabilities... meet regulatory demands".
- Key features: Operational Efficiency (best-practice workflows, handle times, throughput, consistent reviews); Real-Time Data and Dashboard Reporting ("case volumes, inventory, average handle times, throughput and turnaround times"); Integrated Clinical Decision Support ("clinical decision support content and business rules leveraging medical policy, MCG, InterQual, CMS NCD/LCD and other clinical criteria within the workflow; limit the need for clinician reviewers to use separate applications"); HL7 FHIR Interoperability (CRD/DTR/PAS e-prior-auth APIs); AI and Agentic Automation Plus-Ins; Built-in Compliance ("continual monitoring of regulatory compliance and turnaround times specific to each line of business and contract with active alerts, case prioritization, real-time dashboards, CMS and other self-service reports").
- Scope: "both medical and behavioral utilization activities, including medications under the medical benefit"; "From inpatient and outpatient services to pharmaceuticals and behavioral health"; service types/workflows/categories "fully configurable".
- "Features like automatic approval logic and case routing ensure timely, accurate and appropriate delivery".
- Provider Portal: electronic submission of requests + clinical documentation (medical and behavioral), document upload, status tracking, real-time updates, appeals through the portal.
- Platform context: CareProminence unifies UM, Care Management, Pharmacy Management, Complaints/Appeals/Grievances — UM is one named suite beside siblings.
- Metrics language: faster decision-making, improved compliance, operational efficiency (marketing; not structural).

## Product B — ZeOmega Jiva Utilization Management + Smart UM Suite

Evidence layer: A.

### Key observations (Jiva UM page)

- "The Utilization Management (UM) capabilities in Jiva give healthcare organizations the insights and tools needed to better guide the use and effectiveness of healthcare services. Users can gauge medical necessity and appropriateness of care, and review care assessments, stay requests, and procedures." — medical necessity + appropriateness named as the review content; stay requests = concurrent/inpatient. (A)
- "The system can trigger real-time auto adjudication based on pre-configured or client-defined rules, and supports provider self-service, giving providers the ability to enter authorization requests via multiple methods and obtain real-time approvals."
- "Concurrent review and medical director review for inpatient and outpatient episode types are made easy, while a multi-services review-on-a-click enables faster turnarounds." — concurrent review + medical-director escalation named. (A)
- Behavioral health: "full utilization management services, such as electronic prior authorization, referral, concurrent review, and cost savings management, as well as the ability to conduct behavioral health assessments."
- "Drives overall effectiveness and efficiency of care management through integration of UM with other care management modules"; "payer-provider collaboration... like EMR and ADT data as well as bidirectional exchange" — ADT (admission/discharge/transfer) feeds as concurrent-review trigger substrate. (A)
- "Optional Integrations with MCG Cite AutoAuth and Change Healthcare InterQual Connect Medical Review Service for clinical evaluations" — third-party criteria/review services as optional integrations, not the core. (A)
- Lines of business: government-sponsored populations (MA/Medicaid pages separate), behavioral health; "state-by-state regulatory compliance".

### Key observations (Smart UM Suite page)

- "Smart UM is a modular, Agentic AI-powered Utilization Management (UM) suite designed to automate and orchestrate the entire prior authorization and medical necessity review lifecycle... with strong human-in-the-loop controls".
- Modules: Smart Authorization Gateway (FHIR e-PA; "Eligibility and Benefits Checker"; "Integrated with Commercial, CMS, and Customized Payer Rules and Guidelines"; "Intelligent Network Routing Among Providers, Payers and Delegated Vendors"); Smart Fax Automator (fax ingestion, data extraction, auth creation/routing); Smart Auth Optimizer (likelihood-to-approve prediction, rule engine, fairness monitoring); Medical Guidelines Digitizer (medical policy parsing → decision trees, "Explainable Criteria Presentation", "Clinician Guided and Validated"); Medical Guidelines Assist (human-in-the-loop clinical review agent: "Clinical Data Extraction, Evidence Highlighting, Auto-Suggested Responses, Audit-Ready Summarization").
- "Smart UM is platform-agnostic... aligned with regulatory and turnaround-time requirements".
- Suite context: Jiva solution family lists Utilization Management, Smart UM Suite, Smart Auth Gateway (ePA), Delegated Clinical Services as separate named solutions — UM as sibling solution of a payer platform.

## Product C — Cohere Health

Evidence layer: A.

### Key observations

- Product literally named "Utilization Management" (UM suite): "AI-powered prior authorization automation — touchless prior authorizations and faster medical necessity reviews"; "Touchless prior authorizations, faster medical necessity reviews, inpatient-specific workflows." — PA + medical necessity + inpatient workflows inside one UM product. (A)
- Offerings structure the operating model: **In-House** ("Run UM with your own clinical team" — stage names Intake, Decision, Review Assist, Review Resolve, Align), **Delegated** ("Specialty-specific care management" — MSK, cardiovascular, sleep, diagnostic imaging, GI), **API-Based** ("Embed UM into existing systems"), **Policy Studio** ("Manage clinical policy at scale"). (A)
- How it works: "All-channel intake — Authorization requests are submitted through EHRs, fax, and every other provider channel"; "Real-time approvals — Highly accurate AI can dig into unstructured attachments to find the clinical criteria to satisfy policy"; "AI-guided reviews — In-house clinical reviewers get case summaries, AI-surfaced indication data, and an expert AI assistant". (A)
- "Your policies, rules, and UM population strategy are automated through Cohere Health's clinical intelligence platform."
- Concurrent-adjacent evidence: "50% faster inpatient and outpatient reviews" + "improving care transition management"; "inpatient-specific workflows". (A)
- Platform context: Cohere Unify spans UM, Payment Integrity (Auth Match — "Reconcile claims against authorizations"), Appeals, Care Management, Claims Operations, Quality as separate products. (A)
- Provider-facing surfaces: provider portal, public "Check Auth Status" page, public "Review Criteria" help collection. (A)
- Denial-rate decrease attributed to "evidence-based intelligence that guides clinically appropriate requests before submission" (provider-side nudges) — UM influencing upstream care decisions. (A)

## Product D — Availity Intelligent Utilization Management

Evidence layer: A.

### Key observations

- Named "Intelligent Utilization Management"; subject framed as "transforming the prior authorization process" — a UM-branded product whose center is the PA decision layer. (A — the packaging-overlap pole)
- AuthAI: "delivers real-time, policy-aligned recommendations, not predictions based on regression models. Every recommendation is traceable, auditable, and grounded in a health plan's medical criteria"; "Availity AuthAI does not auto-deny, deny or approve prior authorizations. Availity AuthAI is a recommendation engine, not a decisioning engine." — decision support recommends; the payer decides. (A)
- Codified policy: "aligning the patient's clinical data to codified policy logic using Clinical Quality Language (CQL)... pended cases requiring human review are surfaced with relevant evidence visually organized".
- End-to-end stages named: "Intake & Submission... Attestation (CRD/DTR/PAS)... UM Decision support... UM Exception handling: For complex cases, Availity AuthAI organizes clinical evidence for UM clinicians... UM Feedback loop: captures outcomes and updates medical policy logic... Determination." (A)
- **Delegation and the UM platform seam**: "Availity's Intelligent Utilization Management solution is platform-agnostic, integrating via FHIR API to UM systems and any EHR. Configuration at implementation enables requests to route to or from delegated vendors supporting insourced, outsourced, or hybrid UM operating models." — Availity itself distinguishes its product from "UM systems" (the payer's UM platform) and names delegated vendors. (A — strong seam evidence: the market itself models UM platform vs decision layer as separate layers)
- FAQ confirms CMS-0057-F FHIR API framing (CRD/DTR/PAS) and AI governance ("coverage determinations must consider the individual patient's circumstances").

## Product E — Medecision Utilization Management

Evidence layer: A.

### Key observations

- "Streamline reviews to ensure effective, appropriate care delivery." Challenge framing: "Fragmented intake — manual faxes and unstructured data"; "Documentation overload — reviewers waste hours scanning irrelevant records for clinical evidence"; "Regulatory pressure — strict CMS mandates demand faster determinations and total transparency"; "Provider abrasion". (A)
- Solution capabilities: "AI Policy Management — automate approvals, ensure compliance"; "Interoperability — beyond CRD, DTR, and PAS requirements... touchless prior authorization"; "Auto Workflow Rules"; "Decision Rules — smarter, automated determinations that drive consistency, policy accuracy, and administrative efficiency in utilization management"; "Routing — intelligent routing to ensure the right tasks reach the right teams"; "Model Content — ready-to-use, customizable templates" (request intake); "Appeals & Grievances"; "Provider Portal — submit, track, and manage authorization requests"; "Fax AI — extracts, structures, and auto-generates UM requests"; **"Peer to Peer Scheduling — peer-to-peer MD review scheduling—letting providers self-schedule Outlook-integrated appointments to accelerate UM decisions."** (A — peer-to-peer physician review machinery directly evidenced)
- Agentic AI agents (Medical Necessity Agent, Document Review Agent, etc.) — era-current layer.
- Case study voice: "We started years ago with utilization management workflow, administration and reporting" (HMSA analyst) — UM = workflow + administration + reporting triad as customer-experienced scope. (A)
- Suite context: Medecision "By Use Case" lists Care Management, Utilization Management, Quality Management, Risk Management as separate use-case solutions — UM as sibling solution of a care-side suite family.

## Product F — Waystar Utilization Management (boundary-test pole)

Evidence layer: A.

### Key observations

- Provider-side product named "Utilization Management", sitting under "Clinical Integrity + Revenue Capture" pillar — separate from "Authorization" under "Financial Clearance" (the provider-seat mirror of the PA-vs-UM packaging split). (A)
- Center: "make quick, confident status decisions — allowing your team to strengthen compliance, tell a more complete patient story, and boost financial performance"; "Every missed or delayed status review puts patient care and your revenue at risk." (A)
- "Waystar's UM solution scans patient records in real-time and flags high-priority cases"; "summarizing key chart information, surfacing status issues, and satisfying payer requirements"; "Establish medical necessity — insights to support your team's clinical judgment"; "integrated escalation tools for UM nurses and physicians"; "Make and document status decisions more timely, and with greater evidence, to minimize denials and potential audit risk." (A)
- Testimonial: "Within two hours of ED presentation, we have a reliable prediction of inpatient vs. observation — helping both our UM and ED teams prioritize quickly." — level-of-care/observation-status determination is the provider-seat UM work product. (A)
- Paired products: Clinical Documentation Integrity, Prebill Anomaly Detection — adjacent machinery, distinct from UM itself.
- Interpretation: same discipline vocabulary (utilization review, medical necessity, UM nurses/physicians, status decisions), opposite seat: the provider reviews its own active admissions against payer/level-of-care criteria to defend status decisions and revenue, rather than the payer deciding coverage. Prospective leg displaced to the Authorization module.

## Cross-product Comparison

| Structure | MHK | ZeOmega | Cohere | Availity | Medecision | Waystar (provider seat) |
|---|---|---|---|---|---|---|
| Standing review program (configured scope/workflows/LOB) | ✔ configurable service types/workflows/categories | ✔ configurable rules, LOBs | ✔ in-house/delegated/API offerings, UM population strategy | ✔ operates within payer UM program (integrates TO UM systems) | ✔ workflow rules/decision rules per plan | ✔ provider UR program over active admissions |
| Review case as work object (member + care + documentation + reviewer + status) | ✔ prior-auth/concurrent/post-service cases | ✔ assessments, stay requests, procedures | ✔ cases, case summaries, review stages | ✔ requests + clinical evidence for UM clinicians | ✔ UM requests, routing, templates | ✔ case reviews of active admissions, chart summaries |
| Criteria-based clinical determination (medical necessity/appropriateness) | ✔ medical policy + MCG/InterQual/NCD-LCD | ✔ medical necessity + appropriateness; client-defined rules | ✔ clinical criteria to satisfy policy | ✔ codified policy (CQL) recommendations, plan decides | ✔ decision rules, AI policy management | ✔ medical necessity/status criteria (payer requirements) |
| Clinical reviewer staffing + physician escalation | ✔ clinician reviewers in workflow | ✔ concurrent review + medical director review | ✔ in-house clinical reviewers, AI-guided | ✔ UM clinicians for complex/exception cases | ✔ peer-to-peer MD scheduling | ✔ UM nurses + physicians escalation |
| Prospective (prior-auth) review | ✔ | ✔ (ePA, real-time approvals) | ✔ touchless PA | ✔ (product center) | ✔ | displaced to Authorization module |
| Concurrent (active-stay) review | ✔ concurrent inpatient cases | ✔ concurrent review, stay requests, ADT feeds | ✔ inpatient-specific workflows, care transitions | not evidenced | not named explicitly | ✔ (center of the product) |
| Retrospective/post-service review | ✔ post-service requests | implied (full UM services) | not named explicitly | not evidenced | not named explicitly | post-bill defense adjacent (Prebill/DRG modules separate) |
| Auto-approval / decision support under human control | ✔ automatic approval logic + case routing | ✔ real-time auto adjudication on rules | ✔ 85% real-time claims; remaining reviewed by clinician | ✔ recommendation-not-decision, override | ✔ automated determinations + workflow | ✔ AI flags/summaries; nurse/physician decide |
| Multi-channel intake + documentation assembly | ✔ provider portal, documents | ✔ multiple methods, fax module | ✔ EHRs, fax, every channel; unstructured attachments | ✔ EMR/portal intake, CRD/DTR/PAS | ✔ portal + Fax AI | scans patient records |
| Provider self-service surfaces | ✔ portal: submit/track/appeal | ✔ provider self-service, real-time approvals | ✔ portal, auth status, criteria | ✔ provider-facing recommendations/status | ✔ portal | n/a (provider IS the operator) |
| Delegation (insourced/outsourced/hybrid) | platform siblings (CAG etc.), not named on page | ✔ routing among providers/payers/delegated vendors; Delegated Clinical Services | ✔ delegated specialty UM offering | ✔ route to/from delegated vendors | ✔ routing to right teams | n/a |
| Compliance / turnaround machinery | ✔ per-LOB turnaround monitoring, alerts, CMS reports | ✔ aligned with regulatory and turnaround-time requirements | ✔ compliance team, CMS-0057 | ✔ CMS mandate framing | ✔ CMS mandates framing | ✔ compliance/audit-risk framing |
| Appeals linkage | ✔ appeals via portal | ✔ Appeals & Grievances sibling | ✔ Appeals product on platform | ✔ appeals/grievances reduction claimed | ✔ Appeals & Grievances module | denial/audit-risk defense |
| Auth-vs-claims reconciliation | not named | not named | ✔ Auth Match | not named on page | not named | denial prevention framing |
| Behavioral health / pharmacy-med-benefit scope | ✔ | ✔ behavioral UM | specialty lines (MSK/cardio/imaging/sleep/GI) | not named | not named | n/a |

## Canonical Model (Model + Compare + Synthesize)

### L0 — Defining Invariant (jointly-held; deliberately small)

The Type is the health plan's — or its delegated UM entity's — standing clinical review program. Three jointly-held structures; remove any one and the product is no longer a UM application:

1. **The review program of record** — the plan's standing configured review operation: which services are subject to review, under which review modes across the care timeline, against which criteria, executed by which reviewer staffing structure, across lines of business — held as program configuration the organization operates, not one-off transactions. (Remove → scattered request processing with no standing review operation = prior-authorization request machinery, or ad-hoc approvals.)

2. **Criteria-based clinical review to a recorded determination** — each case is evaluated against the plan's medical-necessity/coverage criteria (plan medical policy and referenced criteria content, digitized into executable logic where automated) to a recorded, reasoned determination — meets-criteria/approve, not-met/deny, partial or pend for information — with not-met cases escalating to physician-level review (medical director review, peer-to-peer). Decision support and auto-approval logic may resolve routine meets-criteria cases, but the determination content is clinical-criteria application, and the human exception path is preserved. (Remove → administrative approval routing = generic approval workflow; or a bare rules engine.)

3. **Care-timeline review coverage** — the program's review modes span the care timeline: prospective review before service (the prior-authorization face), concurrent review of active admissions/stays (continued-stay, level-of-care reviews), and retrospective/post-service review — one program machinery operating across modes, with concurrent review of active care the mode the pre-service request machinery lacks. (Remove concurrent + retrospective → pre-service request gate = Prior Authorization Platform territory.)

Joint-holding tests: 1 alone = a policy/program document; 2 alone = criteria library + one-off determinations; 3 alone = a timeline taxonomy with no machinery; 1+2 without 3 = pre-service review program (UM collapsed to its prospective face); 1+3 without 2 = review scheduling with no clinical determination content; 2+3 without 1 = scattered reviews with no program operation.

Historical/market-sample check (§24): paper-era utilization review — telephoned/mailed admission notifications, nurse reviewers applying printed criteria manuals, physician escalation and committee-documented determinations, concurrent review worksheets for active stays, post-service retrospective review — satisfies all three legs with no software, AI, FHIR, or US-specific machinery in the core. Regional/delegated UM organizations (managed-care UM vendors operating on behalf of plans) satisfy the same core. The definition names no US regulatory machinery; CMS/FHIR/X12-era requirements are era-current implementation layers.

### L1 — Common Mature Structure

- Multi-channel intake (provider portal, fax automation, electronic transactions/FHIR APIs, EHR-embedded) with clinical documentation assembly (attachments, evidence extraction/highlighting, chart summaries).
- Auto-approval logic / decision support (rules engines, AI recommendations, likelihood scoring) with human-in-the-loop exception handling and override.
- Criteria & policy management (plan medical policy; third-party criteria sets — MCG, InterQual, CMS NCD/LCD — as integrated content; policy digitization into executable decision logic).
- Reviewer work queues, intelligent routing, case prioritization, case inventory management.
- Provider self-service: submission, status tracking, real-time updates, document upload, peer-to-peer scheduling.
- Delegation routing and oversight (insourced/outsourced/hybrid models; routing among providers, payers, delegated vendors).
- Compliance machinery: turnaround-time monitoring and alerts per line of business/contract, case prioritization against clocks, audit/self-service regulatory reports.
- Appeals & grievances linkage.
- Authorization-vs-claims reconciliation.
- Operational dashboards (case volumes, inventory, handle times, throughput, turnaround times).
- Scope breadth: medical + behavioral health; medications under the medical benefit; inpatient/outpatient/procedure lines.

### L2 — Variant / Optional Structure

- Operating model: in-house vs delegated (specialty UM organizations) vs hybrid vs API-embedded decision layer.
- Product shape: dedicated UM suite vs module of a payer platform family vs use-case solution of a care-suite family vs decision-support/intake layer integrating TO UM platforms vs delegated-service-plus-platform.
- Specialty program emphasis (MSK, cardiovascular, imaging, sleep, GI; behavioral health; pharmacy).
- Review-mode emphasis: PA-centric suites vs full-timeline programs vs inpatient-focused concurrent operations.
- Seat: payer/delegated (dominant market center) vs provider-side utilization review (Waystar pole — status/level-of-care review of the provider's own admissions; flagged below).
- Regulatory regime depth (US CMS-0057-F/FHIR/X12 278 machinery, per-LOB turnaround rules; regional regimes unverified — sample is US-centric).

### L3 — Vendor-specific (Research Notes only)

- Availity: AuthAI, CQL codification, "Insourcing Blueprint" content, CMS-0057 solution suites.
- Cohere: Unify platform, stage names (Intake/Decision/Review Assist/Review Resolve/Align), Policy Studio, Auth Match, specialty delegated lines, marketing stats (85% real-time, 18x ROI, 25M lives).
- ZeOmega: Smart UM module names (Smart Fax Automator, Smart Auth Optimizer, MG Digitizer, MG Assist), MCG Cite AutoAuth + InterQual Connect optional integrations, Jiva platform family.
- Medecision: AgentFoundry agents, Fax AI, Outlook-integrated peer-to-peer scheduling, Model Content templates.
- MHK: SmartProminence Orchestrator, DataVisor, CareProminence platform unification.
- Waystar: AltitudeAI, inpatient-vs-observation prediction, Obs-to-IP conversion metrics, paired CDI/Prebill modules.

## Vendor-specific Findings

- Availity's own copy draws the layer seam: its product "integrates via FHIR API to UM systems" — the market itself models the payer UM platform (program machinery) as distinct from decision-support/intake layers sold under UM branding. (A)
- Cohere is the clearest delegated-UM-with-platform pole (offering structure + specialty lines). ZeOmega evidences delegation routing and a separate Delegated Clinical Services solution. (A)
- Peer-to-peer physician review machinery appears directly as product capability only at Medecision (scheduling) and implicitly at Waystar/Cohere (physician escalation tools); treat physician-escalation as L0 content, peer-to-peer scheduling tooling as L1. (A→calibration)
- Concurrent-review triggering via ADT feeds evidenced only at ZeOmega (one product) — treat ADT-triggered concurrent review as a common-pattern instance, not a universal. (A, single-source → held L1 with qualification)

## Boundary Findings

1. **vs Prior Authorization Platform — FLAG DISCHARGED from this side.** Keep-both RATIFIED on exactly the seam that pass proposed: PA platform = the multi-party request machinery (request as unit of record; intake → review support → determination → notification → authorization of record → status; whichever side hosts it). UM = the payer's standing clinical review program (criteria program, reviewer staffing/escalation, care-timeline review coverage incl. concurrent + retrospective, delegation governance, compliance/turnaround operation). Evidence for the seam: (a) packaging overlap runs both directions and cannot separate the leaves — Cohere's UM suite and Availity's "Intelligent UM" sell payer prior auth inside UM-branded offerings, while ZeOmega splits Smart Auth Gateway (ePA) from UM/Smart UM Suite, MHK's UM suite names all three timings as one subject, and Waystar splits Authorization (financial clearance) from UM (clinical integrity); (b) Availity's own copy distinguishes its UM-branded product from "UM systems"; (c) concurrent review appears in the UM sample (MHK concurrent inpatient cases, ZeOmega concurrent review + stay requests + ADT, Cohere inpatient workflows, Waystar status reviews) and was NOT evidenced in the PA pass's sample. Resolution of the PA pass's open question: **concurrent-review machinery belongs to the UM leaf** — the PA leaf keeps the advance-approval request/authorization-of-record machinery; where a product runs concurrent review through request-shaped machinery the two Types interpenetrate (packaging overlap, same resolution pattern as CAPS-vs-claims-engine).
2. **vs Payer Care Management — flag from that pass ANSWERED from this side.** Keep-both confirmed: UM is review machinery (criteria-based determinations on care); payer care management is the program portfolio + care loop (identify/stratify/enroll/plan/intervene). In this sample UM always appears as a sibling suite/solution/module (MHK separate suites unified on a platform; ZeOmega separate solutions; Cohere separate products on one platform; Medecision separate use-case solutions) — never as the whole of care management, and care management never performs the review-determination act.
3. **vs Health Plan Administration System** — consistent with that pass: HPAS is the payer's system of record (member/eligibility/benefit rulebook incl. authorization rules); UM operates the review program against that rulebook, consuming eligibility (ZeOmega's "Eligibility and Benefits Checker") and holding no premium/enrollment/claims of record.
4. **vs Payer Claims Processing** — determination ≠ adjudication. The UM determination (and its authorization outcome) is an input claims adjudication consumes; auth-vs-claims reconciliation (Cohere Auth Match) is seam machinery; X12's own corpus separates 278 review transactions from 837/835 claim machinery (inherited A evidence from the sibling pass's official-source fetch).
5. **vs the provider-side utilization-review operation (Waystar pole) — NEW FLAG for taxonomy stewards.** The market also sells "Utilization Management" software to providers: the hospital's own UR operation reviewing its active admissions against level-of-care/medical-necessity criteria (inpatient-vs-observation status decisions, documentation to withstand payer review/audit, UM nurse + physician escalation). It shares the discipline vocabulary and the concurrent-review machinery but its seat and purpose differ (provider's status/revenue/compliance defense vs payer's coverage program), and its prospective leg is displaced to authorization/financial-clearance tooling. This pass defines the leaf per the delegated seam as the payer's (or delegated entity's) clinical review program and does NOT silently absorb the provider seat; the directory question (one two-seat Type vs payer-scoped leaf) is left open.
6. **vs Healthcare Quality Management / Clinical Documentation Integrity** — adjacent: CDI = documentation completeness/integrity (Waystar pairs but separates them); quality = measure/gap machinery. UM's subject is necessity/appropriateness of care against coverage criteria.
7. **vs Referral Management** — referrals are routing/authorization of care relationships; UM reviews necessity of services against criteria. Referral review can be one reviewed service type inside a UM program (ZeOmega names referral among UM services).

## Uncertainties

- UM committee/program-governance bodies, inter-rater reliability programs, annual program reviews: standard in the discipline's regulatory framing but NOT directly evidenced on fetched product pages — kept out of the defining core; compliance machinery (turnaround monitoring, audit reporting, per-LOB alerts) is evidenced and held as L1.
- Whether any UM product operates as strictly prospective-only (would weaken the multi-mode minimum of L0 leg 3): none observed; Availity's UM-branded product is PA-centric but explicitly positions itself as integrating to UM systems rather than replacing the program. Held as inference (C), noted.
- International (non-US) UM/regional prior-approval regimes: not researched; US-centric sample limitation recorded (consistent with sibling passes).
- Legacy enterprise engines (TriZetto, HealthEdge, Optum/Change InterQual-native suite) unreachable (consistent with prior sibling passes' 403/transport failures) — dominant enterprise poles rest on market anchors + criteria-integration references from sampled products.
- Delegated-entity oversight mechanics (audit rights, reporting cadence, delegation agreements as objects): evidenced only as routing/operating-model language, not as first-class objects — held L1, no precise mechanics claimed.

## Final Synthesis

A Utilization Management application is the health plan's — or its delegated UM entity's — standing clinical review program: the software through which care under the plan's coverage is reviewed against medical-necessity and coverage criteria to recorded determinations, across the care timeline (prospective prior-auth review, concurrent review of active admissions, retrospective post-service review), executed by a nurse-first reviewer staffing structure with physician escalation, operated as a configured program with compliance/turnaround machinery, provider-facing intake and status surfaces, and delegation support for insourced/outsourced/hybrid operating models. Its defining core is exactly three jointly-held structures: the review program of record, criteria-based clinical review to a recorded determination with physician escalation, and care-timeline review coverage over one program machinery. Prior authorization is UM's prospective, transactional face — the PA sibling leaf owns the multi-party request machinery and the authorization of record; the UM leaf owns the program. Claims adjudication consumes the outcome; care management receives the handoff; the provider-side utilization-review operation is the mirror seat, flagged for taxonomy stewards rather than silently absorbed.
