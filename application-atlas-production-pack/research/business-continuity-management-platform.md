# Research Notes — Business Continuity Management Platform

Research date: 2026-09-10
Directory location: §10 Enterprise Operations & Administration (leaf: Business Continuity Management Platform)
Slug: business-continuity-management-platform

## Research Goal

Understand what a Business Continuity Management (BCM) Platform actually is as an Application Type, from real products' official documentation: the core objects (business functions/processes, impact analyses, plans, exercises), the workflows of a continuity program (analyze → plan → maintain → validate → respond → govern), the roles involved, and the boundaries against neighboring Types (GRC Platform, Enterprise/Operational Risk Management, Emergency Management Platform, Disaster Recovery Platform, Incident Management, Crisis Management, Compliance Management).

Two inherited joint-review flags must be discharged from this side:
1. **governance-risk-compliance-platform (§11, processed)** — BCM flagged as "same child-module pattern" (all five sampled GRC platforms ship BCM as modules); joint review recommended.
2. **emergency-management-platform (§24, processed 2026-09-07)** — BC/EM overlap flagged as real and vendor-driven (WebEOC COOP Builder, Veoci/Noggin BC solutions); seam held as BC = plan-of-record vs EM = event-of-record; joint review recommended when this leaf is processed.

## Initial Boundary (pre-research hypothesis)

- Core use: the organization's system of record for its continuity program — which business functions are critical, how long the organization can tolerate their loss, and how each will be recovered.
- Primary users: BCM/resilience program managers, business process owners, executives, IT DR managers.
- Nearest neighbors: GRC platform (suite umbrella), ERM/operational risk (risk register), Emergency Management (event coordination), Disaster Recovery Platform (technical IT recovery), Incident Management (IT incident lifecycle), Crisis Management (event response).
- Likely confusions: "business continuity" is also used loosely by IT HA/replication vendors (Zscaler, GoldenGate) — a naming collision, not a Type overlap; "Critical Event Management" (corporate CEM) may be a marketing umbrella over EM-shaped products.
- Unknowns: whether exercise management is definitional or common; how deep the operational-resilience regulatory pole (financial services) penetrates the core model; whether the BIA is a document or a structured computed record.

## Research Questions

1. What is the continuity subject — what object does the program analyze and plan for (process? function? service? asset?)?
2. What exactly is a BIA in software terms: inputs (questionnaires, impact categories), outputs (RTO/RPO/recovery tiers), dependencies, states?
3. What is a continuity plan of record: structure, binding to analyzed functions, lifecycle (draft → review → approve → publish → review cycle), activation?
4. How do exercises/tests work: types, scenario, findings, corrective actions?
5. What role does risk assessment play relative to impact analysis?
6. Where do incidents/crises fit: in-scope or integration?
7. What roles exist and what can each do?
8. What compliance/regulatory machinery exists (ISO 22301, operational resilience regimes)?
9. How do products differ: dedicated suite vs GRC module vs platform module vs consulting-led?

## Representative Products

Selected for market representativeness + documentation completeness + different product philosophies + different customer tiers:

| Product | Vendor | Philosophy / tier | Evidence tier |
|---|---|---|---|
| Fusion Framework System | Fusion Risk Management | dedicated enterprise-resilience specialist; BCM as foundation of a resilience decision system; built on Salesforce | Tier 2 (official product pages) + Tier 3 (customer deployment description) |
| Business Continuity Management (application) | ServiceNow | platform module on the Now platform; workflow/CMDB-led; large enterprise | Tier 1 (official docs pages, fetched via search excerpts) + Tier 2 (product page, solution brief PDF) |
| Business Continuity & IT Disaster Recovery Planning / Resilience Management | Archer (Archer Technologies, ex-RSA) | GRC-suite use-case/solution area; enterprise | Tier 1 (official help.archerirm.cloud docs) + Tier 2 (community articles, legacy datasheet) |
| Business Continuity Software | Quantivate (an Ncontracts company) | mid-market GRC-suite application; template/methodology-led; banks & credit unions | Tier 2 (official product page) |
| Business Continuity Management / Business Continuity & Resilience | Riskonnect (Castellan heritage) | consulting/methodology-led IRM suite; mid-to-enterprise | Tier 2 (official product pages + fact-sheet PDFs, fetched via search excerpts) |

## Sources

### Fusion Risk Management
- https://www.fusionrm.com/solutions/business-continuity-management/ — BCM product page (fetched 2026-09-10)
- https://www.fusionrm.com/what-is-fusion-risk-management — platform description (search excerpt)
- https://www.fusionrm.com/platform/fusion-framework-system — platform overview (search excerpt)
- https://www.cmu.edu/drbc/fusion-framework.html and https://www.cmu.edu/drbc/bc/index.html — Carnegie Mellon's description of its own Fusion deployment and BC lifecycle (Tier 3, fetched 2026-09-10)

### ServiceNow
- https://www.servicenow.com/products/business-continuity-management.html — product page (search excerpts)
- https://www.servicenow.com/docs/r/zurich/governance-risk-compliance/business-continuity-mangmt-overview.html — BCM overview (search excerpt)
- https://www.servicenow.com/docs/r/governance-risk-compliance/create-business-impact-analysis.html — create BIA (search excerpt)
- https://www.servicenow.com/docs/r/xanadu/governance-risk-compliance/bia-uib.html — BIA workspace (search excerpt)
- https://www.servicenow.com/docs/r/xanadu/governance-risk-compliance/rto-rpo-calculation.html — RTO/RPO calculation (search excerpt)
- https://www.servicenow.com/docs/r/zurich/governance-risk-compliance/rto-rpo-recovery-tiers.html — RTO/RPO/recovery tiers (search excerpt)
- https://www.servicenow.com/docs/r/washingtondc/release-notes/grc-business-continuity-management-rn.html and Zurich release notes — release notes (search excerpts)
- https://www.servicenow.com/content/dam/servicenow-assets/public/en-us/doc-type/resource-center/solution-brief/sb-bcm.pdf — solution brief (search excerpt)

### Archer
- https://help.archerirm.cloud/archersolutions/en-us/Content/ArcherSolutions/resilience_management.htm — Resilience Management solution (search excerpt)
- https://help.archerirm.cloud/busres_continuity_610/en-us/Content/Solutions/BusResiliency/br_bcdr_design.htm — BC/DR Planning use-case design (search excerpt)
- https://help.archerirm.cloud/busres_continuity_2024.03/Default.htm and 6.12 variant — BC/DR Planning use case (search excerpts)
- https://help.archerirm.cloud/busres_impact_610/Default.htm — Business Impact Analysis use case (search excerpt)
- https://community.archerirm.com/hc/en-us/articles/52147299828499-Archer-Business-Impact-Analysis — BIA community article (search excerpt)
- https://community.archerirm.com/hc/en-us/articles/52147261046675-Archer-Resilience-Management — Resilience Management article (search excerpt)
- https://www.insight.com/content/dam/insight/en_US/pdfs/rsa/archer/rsa-archer-business-continuity-management-datasheet.pdf — legacy RSA Archer BCM datasheet (search excerpt)

### Quantivate
- https://www.quantivate.com/business-continuity-software/ — BCM product page (fetched 2026-09-10)

### Riskonnect
- https://riskonnect.com/solutions/business-continuity-management-software/ and https://riskonnect.com/business-continuity-management-software — BCM product pages (direct fetch returned images only; evidence via search excerpts)
- https://go.riskonnect.com/hubfs/Riskonnect/BCR___Business_Continuity_Management_Fact_Sheet.pdf — BCM fact sheet (search excerpt)
- https://go.riskonnect.com/hubfs/Riskonnect/Business_Continuity_Resilience_Fact_Sheet.pdf — BC&R fact sheet (search excerpt)
- https://ready.uic.edu/planning/bcr/samples — University of Illinois Chicago deployment description (Tier 3, search excerpt)

### Source-access limitations
- ServiceNow docs site is a JavaScript application; direct fetch returned a loading shell. Evidence taken from search-engine excerpts of the official docs pages (verbatim text), treated as Tier 1 with reduced field-level precision.
- Riskonnect pages returned only og:image on direct fetch (two attempts); evidence from search excerpts of official pages and official fact-sheet PDFs, treated as Tier 2 with reduced precision.
- Fusion help center (customer login required) not accessible; official product pages used instead.
- No regime texts (ISO 22301, DORA, FCA/PRA) fetched directly; standards referenced only as products cite them.

---

## Product A — Fusion Framework System (Fusion Risk Management)

### Key observations (evidence layer A unless noted)

- Positioning: "business continuity management software that helps resilience, risk, and continuity teams manage **business impact analyses, continuity plans, recovery strategies, exercises, and remediation work** in a single Enterprise Resilience Decision System."
- Three value pillars on the BCM page: **Map and Protect Your Business** ("see how critical processes, systems, locations, people, and third parties connect so teams can identify vulnerabilities"); **Validate Business Continuity Plans** ("validate plans with current data, exercises, dashboards, and remediation tracking that show where your program is ready and where gaps remain"); **Recover Faster with Live Plans** ("use connected continuity data to prioritize recovery, coordinate teams, and reduce confusion when disruption affects critical operations").
- BIA: "Capture business impact analysis data, identify critical processes, understand recovery requirements, and focus continuity planning on the operations that matter most."
- Dependencies: "Visualize **upstream and downstream dependencies** across people, processes, places, systems, and third parties so continuity plans reflect how the business actually operates."
- Plans: "Build and maintain **adaptive business continuity plans** that stay aligned with the business. With intuitive workflows, **ownership tracking, plan reviews**… teams can convert static plans into dynamic, actionable data."
- Exercises: "Test business continuity plans through **exercises, walkthroughs, scenario testing, and readiness reporting**. Fusion connects exercises to actual business impact analysis, risk, recovery, application, vendor, site, and plan data so teams can test realistic disruption scenarios and **capture lessons learned**."
- Anti-static-plan framing throughout: "When plans, dependencies, and recovery data live in documents, spreadsheets, and disconnected systems, teams struggle to trust the data, prove readiness, and act quickly."
- Suite context: BCM is one of six core products (Business Continuity, IT Disaster Recovery, Crisis and Incident Management, Operational Resilience, Third-Party Risk Management, Operational Risk) on one Salesforce-based platform; integrations with ServiceNow, Archer, Everbridge, notification systems, CMDBs.
- Executive layer: "Give executives and board stakeholders a clearer view of continuity readiness, open gaps, remediation progress, and recovery priorities."
- FAQs define: BCP ("documented strategy… risk assessment, business impact analysis, recovery strategies, roles and responsibilities, escalation paths, and testing procedures"); BIA ("determining the criticality of business activities and the resources required to maintain or restore them"); BCMS/ISO 22301.
- Tier 3 (CMU deployment): the BC lifecycle run in Fusion = BIA (interviews with functional owners: services, dependencies — facility/people/technology/vendor, recovery requirements, alternatives/workarounds, risk impact; "BIA data is housed and maintained within the Business Function tab") → Risk Assessment & Gap Analysis (prioritize dependencies by criticality of recovery objectives; compare against current recovery capabilities; gap → accept or remediate) → BC Planning ("all-hazard approach focusing on four key loss scenarios: Loss of Facility, Loss of People, Loss of Supplier, Loss of Technology") → Plan Exercising (walkthrough = detailed plan review; "Exercise information and results are maintained within the Fusion Framework").

## Product B — ServiceNow Business Continuity Management

### Key observations

- Docs overview (Zurich): "The ServiceNow® Business Continuity Management (BCM) application enables your organization to maintain delivery of products and services at acceptable levels during disruptive incidents." Objectives: "Establishing a clear governance structure for business continuity. Defining consistent classification of business processes, dependencies, and recovery objectives through impact and risk analysis. Developing and continuously improving business continuity plans. Identifying, analyzing, and managing process continuity during and after disruptive events."
- BIA as structured computed record: "Business impact analysis is a structured process where you assess the impact categories and dependencies and predict the consequences of a disruption on a business process or business function." Users "respond to the assessment questionnaire… on the Assessment tab"; "Based on the responses received, the BCM application **calculates the recovery time objective (RTO), recovery point objective (RPO), and dependencies** for the business impact analysis." BCM admin "defines the impact ratings and sets up the assessment questions"; dependency tree and dependency assessment grid with configurable columns.
- BIA creation: "Create a business impact analysis (BIA) to get the necessary information for a plan. Use the BIA to identify the recovery time objective for an item and prioritize assets that have most and least critical dependencies." Template carries "primary elements (applications, business processes, and locations), impact categories, and the dependent assets." "Applies to" = "Business process, business application, or any other asset that is assessed in the BIA." Roles: BIA Owner ("person who owns and is responsible for completing the BIA"), BCM Lead (reviews), BCM admin.
- BIA state lifecycle: "In Draft" (edit; add RTO/RPO/dependency assessments) → submit for review → "Pending approval" (read-only) → "Approved" (read-only) or "Returned" (editable). "You must add RTO, RPO, and dependency assessments before you submit for approval."
- RTO/RPO/recovery tiers: "Organizations must assess their business processes for potential downtime due to disruptive events… classifying these processes and determining acceptable limits for recovery time and data loss to minimize operational impact." "Business users and IT owners can perform business impact analysis and **technical impact analysis** respectively."
- Plans: product page — "Continuity Planning: Scope plans to prioritise protecting personnel and restoring assets quickly after a disaster." Release notes reference "business continuity plans (BCPs)" with PDF/Word templates (Document designer), plan assets/activities/recovery teams/documentation/policies/procedures (solution brief).
- CMDB integration: "Harmonise business continuity, disaster recovery, and crisis management through real-time integration with the ServiceNow CMDB"; Washington DC release: "Schedule an auto-update of the dependencies in the business impact analysis (BIA) based on the source data and relationships in the Configuration Management Database (CMDB)"; dependency auto-updates in BIAs and BCPs with email notifications.
- Events/exercises: "Exercise Management: Improve effectiveness and usability of plans during simulated and actual crisis events"; Zurich release: "Avoid duplicate event tasks by identifying and grouping similar tasks in exercises and crises"; "Create action items and send out threat assessments by leveraging Smart Assessment during exercises and crises"; recovery tasks with phases; "finalized RTO and RPO columns in BIAs, BCPs, and events."
- Crisis Management as sibling capability: "Activate continuity plans and monitor ongoing completion of recovery tasks during a crisis event"; Emergency Mass Notifications via Everbridge integration (25+ channels).
- Packaging: BCM is a GRC-family application requested from the ServiceNow Store; related products listed: Integrated Risk Management, TPRM, ITSM, Disaster Recovery and Site Recovery Planning, Operational Resilience Management.

## Product C — Archer (Business Continuity & IT Disaster Recovery Planning / Resilience Management)

### Key observations

- Solution framing: "The Archer Resilience Management solution enables organizations to **identify critical processes, conduct BIAs, maintain BC/DR plans, and respond effectively to incidents and crises**." Applications: **Business Processes** ("business continuity begins with understanding and managing business processes… store and maintain a comprehensive list of business processes, ensuring clarity in ownership and critical attributes"; "process owners define dependencies on applications, third parties, facilities, and organizations within the BIA"), **BIA**, **BIA Campaign** ("launch multiple business impact analysis at the same time"), **BC/DR Plans**, **BC/DR Plan Exercise**, **Incidents**, **Crisis Events**.
- BIA use case: "determine the criticality of business processes and supporting infrastructure so you can protect and recover what is most important"; "enable business leaders to prioritize recovery strategies, recovery tasks, risk assessments, and other activities"; "New or updated BIA initiation depending on process criticality rating, date of last BIA, or other alerts"; "Access roles for business owners, resilience team and executives to drive BIA completion review and approval"; "Deploy one approach and consolidated system of record for all BIAs."
- BC/DR Plans application: "develop detailed business process recovery plans, IT disaster recovery plans, or crisis team response plans using an automated workflow for approval and testing"; "centralized repository for components of the plan and links them to risk assessments, business impact analysis, and items related to business hierarchy and enterprise infrastructure"; "Distinguish between business continuity plans and IT disaster recovery plans"; "Develop a **library of recovery strategies** and associate them to multiple BC/DR plans"; "Document requirements, such as equipment, facilities, and vital records necessary to recover the target of the BC/DR plan (reference the Requirements application)"; "Connect BC/DR Plans to risks in the BCM Risk Register and Business Impact Analysis applications"; "Document notifications (specific messages)"; "Document **call tree initiators and recipients**."
- Testing/Exercise application: "Select a test type. Select a BC/DR plan to activate, and then copy the selected plans for testing. Select **loss types, such as Facilities, Assets, IT, People or Third Parties**, that are impacted in the test scenario. Document test scenario details… Determine if the exercise identified **gaps in strategies, tasks, or the ability to achieve Recovery Time Objectives (RTOs) or Recovery Point Objectives (RPOs)**. Send the results of the test to a reviewer for approval. Generate results of the test or exercise and record them as **Findings**."
- Activated Plans application: "document BC/DR plans and the associated recovery strategies and tasks that have been **activated as the result of a crisis event or a test scenario**."
- BCM Risk Register: "identify and evaluate risks by documenting them and assessing the likelihood and impact of the risks to business operations… associate the risks to any mitigation and add the necessary steps to BC/DR plans."
- Maturity model: prerequisites/next chain — Issues Management → BC&DR Planning → Crisis Management; BIA → BC/DR Planning → Crisis Management; Incident Management ("Report and manage incidents… Escalate an incident to a crisis event").
- Standards: "ISO 22301, the international standard for business continuity management systems (BCMS)… It's recommended that organizations align to these standards and use Archer to operationalize the processes."
- Legacy datasheet (RSA era): "3-in-1 solution — centralize business continuity, disaster recovery and crisis management"; "Perform Business Impact Analysis (BIA) by collecting information on each business process related to its criticality, Recovery Time Objective (RTO) and Recovery Point Objective (RPO)"; "Test plans to identify process gaps, and remediate test failures"; "Report on plan testing, gap analyses and remediation efforts."

## Product D — Quantivate Business Continuity Software

### Key observations

- Positioning: "An all-in-one solution for business continuity planning and management"; anti-paper-notebook framing: "Many organizations simply maintain large paper notebooks of business continuity and disaster recovery plans that sit on a shelf and quickly become outdated."
- Module list (the program pipeline as shipped features): "**Risk Assessment (Threat and Vulnerability Analysis), Business Impact Analysis (BIA), Strategies and Solutions Development, Plan Development, Plan Maintenance, Exercises, Emergency Notification (SMS, Email, Voice Broadcast), Incident Management**."
- Guided criticality: "Guided processes for identifying critical business processes (criticality and risk scoring)"; "Business process library."
- Plan templates: "Business Continuity, Continuity of Operations, Pandemic Flu, Application Disaster Recovery, Platform Recovery, Server Recovery, Data Center Recovery, Crisis Management (with or without Incident Command System elements)."
- Exercises: "Scenario-based exercising."
- Maintenance/distribution: "Real-time plan updates and electronic distribution"; "Centralized storage for plans and documentation"; mobile app ("Synchronize the most current BC plans to iOS and Android devices… Access the most accurate contact details for key personnel… Push notifications to staff").
- Governance: "Configurable workflows, dashboards, reports, and user permissions"; Report Builder over the GRC platform ("Aggregate data across Quantivate products").
- Suite context: one application in the Quantivate GRC Suite (ERM, Compliance, Vendor, IT Risk, Audit, Issue, Complaint, Policy); industries: banks, credit unions, financial services, mortgage, insurance; consulting services offered ("We Schedule Interviews / We Interview Your Staff / You Get Your Plans").

## Product E — Riskonnect Business Continuity Management

### Key observations (evidence layer A via official excerpts; direct fetch failed)

- Positioning: "helps you conduct business impact analyses, engage stakeholders, comply with regulations, and continuously improve your readiness. Instantly access always-current business continuity plans. Automate regular reviews, approvals, and updates from one centralized location."
- Product highlights: "Strategic Continuity Planning, Business Model Definition, Impact Analysis and Risk Assessment, Resilience Testing Exercises, Gap Analysis and Actions"; "built-in global library of plan, incident, business impact analysis, and document templates"; "customizable workflow builder"; "out-of-the-box alignment with ISO 22301, including corrective actions and management reviews"; scorecards/dashboards; "'what if' modeling to visualize relationships and business service-level analysis"; mobile application; SSO/2FA.
- BIA definition (vendor FAQ): "the foundational assessment of a BCM program: the process of identifying which business processes and services are critical, what resources they depend on, and what the consequences of disruption would be over time — financial, operational, reputational, and regulatory. The BIA establishes the recovery priorities that drive everything else in the program: which processes need to recover first, how quickly they need to recover (the Recovery Time Objective, or RTO), and how much data loss is acceptable (the Recovery Point Objective, or RPO)."
- BCP contents (vendor FAQ): "the scope and objectives of the plan, and which business processes or services it covers; the results of the BIA and the RTOs and RPOs for each covered process; defined disruption scenarios and the specific response strategies for each; response team roles, responsibilities, and contact information; activation procedures — the triggers and steps for moving from normal operations to plan activation; recovery procedures for each critical process, including workarounds and alternate resources; communication protocols for internal teams, customers, regulators, and other stakeholders; and a testing and review schedule."
- BCM vs DR (vendor FAQ): "Disaster recovery is a subset of BCM that focuses specifically on restoring IT systems and data… DR alone doesn't constitute a BCM program."
- BCM ↔ ERM (vendor FAQ): "The scenarios that a BCM program prepares for are, by definition, the high-impact risk events that appear in the enterprise risk register… new risks identified through the ERM process can trigger BCM plan updates, and incidents that occur can feed back into risk assessments."
- Exercises: "resilience testing exercise tools that stress-test plans against disruption scenarios and automatically flag gaps identified during testing as corrective actions"; "Business Resilience Agent capability… analyzes stress test results and recommends corrective actions."
- Suite context: "Business Continuity & Resilience" solution family (BCM, Operational Resilience, Emergency Notification, Crisis Management, Threat Intelligence) beside GRC family (ERM, TPRM, Compliance, Audit…); "Start anywhere. Expand everywhere."; consulting and managed services.
- Tier 3 (UIC deployment): the platform exposes "BIAs" and "Plans" sections; sample BIAs/BCPs per function category (Business Operations, Healthcare, Instruction, Research Laboratory, Technology).

---

## Cross-product Comparison

| Structure | Fusion | ServiceNow | Archer | Quantivate | Riskonnect | Layer |
|---|---|---|---|---|---|---|
| Business function/process inventory with owners | Business mapping ("critical processes, systems, locations, people, third parties"); CMU: "Business Function tab" | business processes / applications / locations as BIA primary elements; "consistent classification of business processes" | Business Processes application ("comprehensive list… ownership and critical attributes") | Business process library; guided criticality scoring | Business Model Definition; processes/services in BIA | A→B |
| Impact analysis (BIA) as structured record | BIA data capture; recovery requirements | assessment questionnaire → **calculated** RTO/RPO/dependencies; states Draft→Pending→Approved/Returned | BIA application + campaigns; criticality + RTO/RPO per process | BIA module in pipeline | BIA as "foundational assessment"; RTO/RPO established | A→B |
| Impact-over-time / impact categories | disruption impact understanding | impact categories; impact ratings defined by admin | criticality of processes and supporting infrastructure | criticality and risk scoring | consequences "over time — financial, operational, reputational, regulatory" | B |
| Recovery objectives (RTO/RPO-class) | recovery requirements | RTO/RPO calculated; recovery tiers; technical impact analysis by IT owners | RTO/RPO per process; exercise gap test vs RTO/RPO | in BIA module | RTO/RPO central | A→B |
| Dependency mapping (people/facility/technology/vendor) | upstream/downstream across people/processes/places/systems/third parties | dependency assessments; dependency tree; CMDB auto-update | dependencies on applications, third parties, facilities, organizations | "connections and dependencies across your organization" | "what resources they depend on" | A→B |
| Recovery strategy library | recovery strategies managed | plan assets/activities/recovery teams | "library of recovery strategies… associate to multiple plans" | "Strategies and Solutions Development" | response strategies per scenario | B |
| Continuity plan of record w/ lifecycle | adaptive plans; ownership tracking; plan reviews | BCPs with templates, PDF/Word generation; plan maintenance workflows | BC/DR Plans application; automated approval/testing workflow; plan components repository | Plan Development + Plan Maintenance; templates; electronic distribution | always-current plans; automated reviews/approvals | A→B |
| Plan typology (BC / IT DR / crisis response) | BCM vs ITDR as separate products | BCM + Disaster Recovery and Site Recovery Planning as related products | "Distinguish between business continuity plans and IT disaster recovery plans"; crisis team response plans | BC/DR/pandemic/COOP/app-DR/server/data-center templates | DR = subset of BCM | B |
| Exercise/test management | exercises, walkthroughs, scenario testing; lessons learned | Exercise Management; event tasks; Smart Assessment action items | Testing/Exercise application; test types; loss types; findings; reviewer approval | scenario-based exercising | resilience testing exercises; gaps → corrective actions | A→B |
| Gaps / corrective actions / remediation | remediation tracking; open gaps | action items | findings; Issues Management as prerequisite | issue management (suite) | gaps flagged as corrective actions; ISO corrective actions | B |
| Risk assessment feeding program | risk connected to BIA/exercises | "impact and risk analysis" | BCM Risk Register (likelihood/impact → mitigation → plan steps) | Risk Assessment (threat & vulnerability) | Impact Analysis and Risk Assessment; ERM linkage | A→B |
| Incident/crisis integration | Crisis & Incident Management product beside BCM | Crisis Management capability; activate plans during crisis events | Incidents → escalate to Crisis Events; Activated Plans | Incident Management module; Emergency Notification | Crisis Management + Emergency Notification in family | A→B |
| Notification / call trees | integrations (Everbridge etc.) | Everbridge emergency notifications | call tree initiators and recipients; notifications documented | Emergency Notification (SMS/email/voice) | Emergency Notification product | B |
| Program governance & reporting | readiness dashboards for executives/board | governance structure; dashboards | dashboards (BR Process Manager); reporting on testing/gaps/remediation | dashboards/reports/permissions; Report Builder | scorecards/dashboards; management reviews | A→B |
| Compliance machinery | regulations and standards content | — (not surfaced in sampled pages) | ISO 22301 alignment recommended | regulator/auditor requirements framing | out-of-the-box ISO 22301 alignment incl. corrective actions + management reviews | B |
| Mobile plan access | — (not surfaced) | BCM Mobile application | — (not surfaced) | mobile app with plan sync | mobile application | B |
| Templates / out-of-the-box content | BC Plan inFusion (AI conversion) | BIA/BCP templates; Document designer | pre-built workflows, reference data | template library (8 plan types) | global template library | B |
| Delivery model | SaaS on Salesforce | platform app (Store) | GRC suite use cases/solution areas | GRC suite application + consulting | suite + consulting/managed services | B |

## Canonical Model (Layer C synthesis)

### L0 — Defining Invariant (minimal)

Three jointly-held structures over one binding:

1. **The organization's own business functions/processes as the continuity subject of record** — identified records (process/function/service-level entries) with owners and critical attributes, held in a structured inventory that the whole program hangs from. Remove → a document library or a generic risk register; nothing is "continuing."
2. **The impact analysis that converts disruption into recovery objectives** — for each subject record: the consequence of losing it over time (impact categories), the dependencies it needs (people, facilities, technology, suppliers), and time-based recovery objectives (RTO/RPO-class targets) computed or recorded from that analysis. Remove → plan documents with no analytical basis; recovery priorities become guesswork.
3. **The continuity plan of record bound to the analyzed functions** — recovery strategies and response/recovery procedures held as persistent, owned, maintained records (reviewed and updated as the business changes), written to be executed when disruption strikes. Remove → analysis with no operational response; the "management" disappears.

Binding: **the organization's own continuity** — its own functions continuing at acceptable levels through disruption. Remove the binding → generic risk/EM/GRC machinery.

Jointly-held load-bearing:
- 1 alone = process inventory / org chart of processes
- 2 alone = an impact survey or analytics exercise
- 3 without 1+2 = the paper-notebook plan library (the anti-pattern every sampled vendor names)
- 1+2 without 3 = analysis with no operational response
- 1+3 without 2 = plans with no recovery priorities
- 2+3 without 1 = free-floating plans and analyses with no subject of record

### L1 — Common Mature Structure

- Dependency mapping across people, facilities/processes, technology/applications, suppliers/third parties — upstream and downstream; increasingly auto-refreshed from asset/CMDB data.
- Risk assessment / threat analysis feeding the program (BCM risk register; likelihood × impact; mitigation steps flowing into plans).
- Exercise/test management: test types (walkthrough/tabletop/simulation class), scenario definition (loss types), execution, findings/lessons learned, corrective actions.
- Plan lifecycle machinery: approval workflows, review cycles, versioning, distribution (PDF/Word generation, electronic distribution, mobile access).
- Recovery strategy library reusable across plans.
- Notification/call-tree machinery (contacts, call trees, emergency notification integration).
- Gaps/issues/remediation tracking closing the improvement loop.
- Program governance: dashboards, readiness reporting, executive/board views, audit trails.
- Compliance support: ISO 22301-class alignment, evidence for regulators/auditors.
- Incident/crisis integration: escalation paths, plan activation during events, recovery task tracking.

### L2 — Variant / Optional Structure

- **Operational-resilience regulatory pole**: important business services, impact tolerances, scenario analysis/testing against tolerances (financial-services regimes; Archer Operational Scenario Analysis, ServiceNow Operational Resilience Management, Fusion/Quantivate/Riskonnect operational-resilience solutions).
- **IT DR planning as sibling plan type**: BC vs IT DR plan distinction; technical impact analysis by IT owners; DR planning products beside BCM (ServiceNow DR/Site Recovery; Fusion ITDR product).
- **Crisis management / emergency notification as bundled or sibling modules** (all five samples).
- **COOP / public-sector variant**: Continuity of Operations plan templates; ICS elements (Quantivate; WebEOC COOP Builder per EM pass).
- **Campaign-style BIA rollout at scale** (Archer BIA Campaign; ServiceNow assessments).
- **Consulting/methodology-led delivery**: template libraries, out-of-the-box content, done-for-you BIA/plan services (Quantivate, Riskonnect, Fusion Fuel).
- **AI assistance**: plan generation from documents, scenario testing, corrective-action recommendation (Fusion inFusion, Riskonnect Business Resilience Agent, ServiceNow Smart Assessment).
- **Pandemic/health-scenario plans** (Quantivate pandemic flu template; ServiceNow pandemic-response plans per its own FAQ).

### L3 — Vendor-specific (research notes only)

- Fusion: Salesforce platform base; "Enterprise Resilience Decision System" framing (Expose/Model/Optimize); inFusion AI; Recovery Optimization; Scenario Testing extension; four-loss-scenario framing (facility/people/supplier/technology); "decision layer above GRC" positioning.
- ServiceNow: CMDB dependency auto-update; Everbridge integration; UIB Workspace; Smart Assessment Engine; Document designer (Word); recovery-task phases; Store licensing; BCM Mobile.
- Archer: use-case maturity chain (Issues → BIA → BC/DR → Crisis); Requirements application; Activated Plans application; BCM Risk Register; loss types (Facilities/Assets/IT/People/Third Parties); BR Process Manager dashboard; solution-area packaging (Resilience Management).
- Quantivate: eight named plan templates (COOP, pandemic flu, ICS crisis, app/platform/server/data-center DR); Report Builder; mobile sync app; "1-2-3" consulting service; Ncontracts ownership; bank/credit-union focus.
- Riskonnect: Castellan heritage; Business Resilience Agent; built-in threat intelligence; encrypted chat; "start anywhere, expand everywhere"; fact-sheet packaging.

## Vendor-specific Findings

See L3. Additional cross-observation: the same five vendors all sell the event side (crisis/incident management, notification) as a separate capability or product beside the plan side — the plan/event split is structural in the market, not just in the taxonomy.

## Rejected Findings

- **"BCM = IT disaster recovery"** — rejected. Every sampled product distinguishes them (Archer distinguishes BC vs IT DR plans; ServiceNow pairs BCM with a separate DR product; Fusion sells ITDR as a separate product; Riskonnect FAQ verbatim: "DR alone doesn't constitute a BCM program"). IT DR planning appears inside BCM as a plan type; DR *execution* (failover machinery) belongs to the §14 Disaster Recovery Platform.
- **"BCM = crisis management"** — rejected. Crisis/event management appears in all samples as a sibling capability (escalation target, activation context), not as the BCM core. The BCM core is preparedness-of-record, not event coordination.
- **"BCM = risk management"** — rejected. Risk assessment feeds the program (BCM risk register in Archer; ERM linkage in Riskonnect), but the managed objects are functions/BIAs/plans, not risks.
- **"The BIA is a document"** — rejected as the canonical form. In the two deepest samples (ServiceNow, Archer) the BIA is a structured record with questionnaires, computed RTO/RPO, dependency grids, states, and approval — the plan consumes it. Document-form BIAs exist (paper era, template libraries) as the historical/variant form.
- **"Exercise management is definitional"** — rejected for L0 (see historical check), despite ISO 22301 making it near-universal in mature products.
- **"BCM requires operational-resilience impact tolerances"** — rejected for L0; the tolerance/scenario machinery is the regulated-industry variant pole.

## Boundary Findings

1. **vs GRC Platform (§11) — joint-review flag DISCHARGED, keep-both RATIFIED.** BCM is a distinct child application with its own defining core (function inventory + BIA + plans), delivered as a module/solution/use-case inside every sampled suite: Archer (Resilience Management solution area), Quantivate (application in GRC Suite), Riskonnect (solution family), ServiceNow (GRC-family application), while Fusion explicitly positions itself as *not* GRC ("GRC handles governance. Fusion handles execution…"). Same disposition pattern as the ERM ratification: umbrella Type + register/program-centric child applications. No directory change.
2. **vs Emergency Management Platform (§24) — joint-review flag DISCHARGED, seam RATIFIED from this side.** BC = plan-of-record for continuing organizational functions (inventory + BIA + plans + exercises as a standing preparedness program); EM = event-of-record for coordinating a response (incident container, shared picture, tracked work). The seam is visible inside the samples: BCM products hold plans/BIAs/exercises and *hand over* at activation (Archer Activated Plans linked to Crisis Events; ServiceNow "activate continuity plans… during a crisis event"; Riskonnect/Fusion crisis products beside BCM). Vendor overlap (WebEOC COOP Builder; Veoci/Noggin BC solutions) is real but is suite packaging of both structures under one platform, not evidence of one Type. Keep-both.
3. **vs Disaster Recovery Platform (§14) — seam held, consistent with the DR pass.** DR platform = technical recovery of IT workloads (replication, failover, recovery points); BCM = organizational continuity program over business functions. BCM products commonly include IT DR *planning* as a plan type and integrate with DR execution systems; they do not execute technical recovery.
4. **vs Enterprise/Operational Risk Management (§11)** — risk register vs continuity program; risk feeds in (Archer BCM Risk Register; Riskonnect ERM bidirectional linkage); the continuity program's objects are functions/BIAs/plans.
5. **vs Incident Management (§14)** — IT/operational incident lifecycle vs continuity preparedness; incidents escalate to crises which activate plans (Archer chain).
6. **vs Compliance Management Platform (§11)** — compliance is a driver and an output (ISO 22301 alignment, audit evidence, regulatory reporting), not the core object; no obligations register here.
7. **vs Business Case Management Platform (§10)** — namesake trap only (confirmed the business-case pass's holding: "BCM manages impact analysis, continuity plans, exercises. No overlap in object or workflow").
8. **Naming collision (non-Type)**: "business continuity" is also used by IT infrastructure vendors for HA/replication features (Zscaler Business Continuity; GoldenGate business-continuity use case per the data-replication pass) — a feature name, not this Type.
9. **CEM observation (from EM pass, not directly researched here)**: corporate "Critical Event Management" (Everbridge/OnSolve-class) appears to be EM-shaped structure in corporate clothing; left as a forward observation for any future CEM-adjacent pass.

## Historical / Market-Sample Check (§24)

Paper-era BCM (1990s–2000s, pre-cloud): a binder of business function inventories + BIA questionnaires/interviews + recovery plan binders with owners and annual review + periodic drills — satisfies all three L0 structures without cloud, CMDBs, AI, or campaign tooling. Regional/standard-era products aligned to BS 25999 (UK, pre-ISO 22301) or US federal COOP guidance fit the same core (COOP = plan-template variant). University/mid-market deployments (CMU on Fusion, UIC on Riskonnect) run the same three structures at small scale. The L0 is therefore not an artifact of the modern SaaS implementation.

## Uncertainties

- Impact-category sets are not standardized across products (financial/operational/reputational/regulatory is Riskonnect's articulation; ServiceNow lets admins define impact ratings; Archer/Quantivate use criticality scoring). The canonical model keeps "impact categories" generic.
- Whether plan *approval workflow* is definitional or common: treated as the common implementation of "maintained plan of record"; a product with owner + review cycle but no formal workflow would still satisfy L0.
- Operational-resilience regulatory depth (DORA, FCA/PRA, FFIEC-class) was not researched against regime texts; the regulatory pole is documented only as products present it.
- ServiceNow field-level details (exact states beyond those quoted, exact task semantics) limited by the JS docs site; quoted text is verbatim from official pages via search excerpts.
- Riskonnect evidence is excerpt-level; no direct page fetch succeeded.
- Fusion help center inaccessible (login-gated); product-page + third-party deployment descriptions used.

## Final Synthesis

The Business Continuity Management Platform is the organization's continuity-program system of record. Its defining core is three jointly-held structures: (1) the organization's own business functions/processes held as an owned, criticality-bearing inventory; (2) the impact analysis that converts each function's disruption into recovery objectives (RTO/RPO-class) and exposes its dependencies; (3) the continuity plan of record — recovery strategies and procedures bound to the analyzed functions and maintained as living, approvable, activatable records. Around this core, mature products add dependency mapping, risk assessment, exercise management with findings and corrective actions, plan lifecycle and distribution machinery, notification/call trees, governance dashboards, and compliance support; variant poles include the financial-services operational-resilience regime, IT DR planning as sibling plan type, crisis/notification modules, COOP/public-sector templates, consulting-led delivery, and AI assistance. The Type is bounded from GRC (umbrella), ERM/operational risk (risk register), Emergency Management (event-of-record), Disaster Recovery (technical execution), Incident Management (incident lifecycle), and Compliance Management (obligations) — all of which it consumes from or hands off to, none of which it is.
