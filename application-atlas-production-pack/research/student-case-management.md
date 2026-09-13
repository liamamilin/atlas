# Research Notes — Student Case Management

## Research Goal

Understand what a "Student Case Management" application is as an Application Type: who operates it, what objects exist inside it (cases, students, concerns, casework records, tasks, plans), how a case flows from intake to resolution, what roles and rules matter, and where the Type's boundary sits — especially against the processed siblings **Student Behavior Management** (§23, joint-review flag left for this leaf), **Special Education Management** (§23, boundary note naming this leaf), and **Academic Advising Platform** (§23, joint-review flag left for this leaf), and against the unprocessed §23 neighbors **Student Success Platform**, **School Counseling Management**, and **Student Services Portal**.

## Initial Boundary

Initial hypothesis: the education institution's issue-driven casework system — a case is opened about a specific student for a specific concern (welfare/wellbeing, safeguarding, conduct, academic integrity, safety, complaints), assigned to a responsible staff member (case manager, dean, safeguarding lead, CARE/safety team), worked and documented over time (notes, contacts, tasks, referrals, coordination with other offices/agencies), and carried to a recorded resolution; cases accumulate into the student's institutional support history.

Adjacent Types to separate:
- Student Behavior Management — the school's conduct-event loop (events of record closed by administrative resolution; no assigned caseworker).
- Special Education Management — the regulated, plan-centered case process (eligibility gate + mandated plan + compliance timelines).
- Academic Advising Platform — relationship-driven advising (the case is one object inside advising, per that pass).
- Social Services Case Management / Nonprofit Case Management — same casework machinery over external clients/beneficiaries under program mandates.
- Child Welfare Management — the statutory child-protection agency's system (school safeguarding refers out to it).
- Student Success Platform — retention analytics at scale (unprocessed; may embed case objects).
- School Counseling Management — counselor caseload/appointments for ongoing support (unprocessed).
- HR Case Management — same machinery, different population (employees).

## Research Questions

1. Who operates this software (dean-of-students offices, conduct offices, CARE/behavioral-intervention teams, safety teams, safeguarding leads, student affairs staff)?
2. What opens a case — reports, referrals, concerns, alerts? By whom?
3. What is the case object and what does it bind (student, parties, issue type, severity)?
4. What does "working" a case mean — notes, contacts, tasks/follow-ups, plans, referrals, multi-office/agency coordination?
5. How does a case close, and what outcome is recorded?
6. What accumulates per student across cases (the cross-case record/chronology)?
7. What roles and privacy machinery exist (case owner, teams, need-to-know access, audit trails)?
8. What is common-but-not-definitional (report forms, dashboards, AI, transfers, federal/regional reporting)?
9. Where are the boundaries with the sibling Types (removal tests both directions)?

## Representative Products

| Product | Vendor | Pole | Tier |
|---|---|---|---|
| Maxient | Maxient LLC | US higher-ed conduct/care records system — "conduct records management" (discipline, academic integrity, care and concern, Title IX), one product, no modules, 1,300+ client schools incl. state systems and districts | Tier 2 |
| Symplicity Advocate | Symplicity | US/international higher-ed conduct/Title IX/behavioral-intervention case management — case workflows, phases, event log, CARE network; 350+ student conduct offices | Tier 2 |
| Canopy Case Management (Branching Minds) | Branching Minds | US K-12 student-safety case management — behavioral threat assessment (CSTAG) + suicide risk screening (C-SSRS) + case/task follow-up, integrated with the MTSS platform; district customers | Tier 2 |
| CPOMS StudentSafe | CPOMS Systems (Raptor Technologies) | UK K-12 safeguarding/welfare concern recording + case management — concern capture, chronology, incident→case escalation, multi-agency sharing; UK schools/MATs/LAs + international | Tier 2 |
| Salesforce Education Cloud | Salesforce | Platform/CRM-suite pole — case management as a named common capability inside the Student Success module; case records/care plans/alerts on student profiles | Tier 2 |

Selection rationale: five different vendors; two segments of higher ed (records-centric single product vs workflow-flex conduct case management), two segments of K-12 (US safety-casework with formal protocols vs UK safeguarding chronology), and one platform suite — different product philosophies, different customer tiers (small liberal-arts colleges to state systems; elementary schools to large districts; MATs and local authorities). Anthology Student was considered as an SIS-suite pole but dropped: anthology.com product pages now surface Blackboard teaching/learning content only (two fetch attempts, no Student Case Management content — recorded as a sourcing limitation).

## Sources

Fetched 2026-09-09 (all Tier 2 official product pages; no Tier-1 help-center documentation reachable — see Uncertainties):

- Maxient — https://www.maxient.com/
- Symplicity — https://www.symplicity.com/ ; https://www.symplicity.com/higher-ed/solutions/advocate
- Branching Minds — https://www.branchingminds.com/ ; https://www.branchingminds.com/student-safety-software
- CPOMS — https://www.cpoms.co.uk/ ; https://www.cpoms.co.uk/cpoms-studentsafe-software/
- Salesforce — https://www.salesforce.com/education-cloud/

Not reachable (recorded limitations): symplicity.com/products/advocate (404), anthology.com/products/student-information-system (404), anthology.com/products (returns Blackboard-only portfolio, no Anthology Student case-management content — abandoned after 2 attempts), salesforce.com/education-cloud/what-is-case-management (404). Sibling-pass evidence used as corroboration: research/academic-advising-platform.md (EAB "Cases & Referrals", Civitas case tools, Salesforce case records with alerts), research/student-behavior-management.md (SWIS framing; boundary note), research/special-education-management.md (regulated-machinery discriminator), research/social-services-case-management.md (casework family pattern).

## Product A — Maxient

### Key observations (Layer A unless noted)

- Positioning: "The Experts in Conduct Software"; "the most trusted provider for incident reporting and behavior records management"; more than 1,300 client schools; focused on one product since 2003.
- Scope: "Whether it's student discipline, academic integrity, care and concern, or Title IX matters, Maxient provides a place to easily manage records for your student body's conduct and well-being." One all-inclusive price: "Conduct, Title IX, care and concern, academic integrity, and more are all covered" (no modules).
- Institutional coordination: "By improving communication and collaboration across the institution, Maxient helps to identify students in need of assistance and coordinate the efforts of departments to provide follow-up."
- Case machinery: training agenda names "Basic Workflow, using Manage Case Types, and information on various processes" — case types and workflows are first-class (Layer B for operational depth; the feature list names workflow only).
- Intake: "Receive reports — Create your own online reporting forms, tailored by purpose and routed based on report content."
- Communication: "Rich text electronic letters with pickup notification and text messaging."
- Analytics: "Powerful analytics and dashboards along with a custom reporting engine"; "Robust Clery features" (US federal campus-crime reporting).
- Privacy/access: "Need to know — Case-based access restrictions and extensive audit trails of user activity."
- Integration: Banner, PeopleSoft, Workday, Colleague, Jenzabar; "Class schedules and ID photos available on-screen"; campus SSO/MFA — the SIS/ERP as the student-population substrate.
- Vendor stance (L3): "Maxient does not utilize artificial intelligence, predictive models, nor any scoring systems"; records are the institution's property; data stored in the US (or Canada).

## Product B — Symplicity Advocate

### Key observations

- Positioning: "The trusted solution for student conduct, Title IX, and behavioral intervention management"; "More than 350 student conduct offices worldwide depend on Advocate."
- Case management framing: "The next generation of case management for conduct, wellbeing, complaints & sexual misconduct"; "Build custom workflows to manage cases for conduct, well-being, complaints, sexual misconduct, and more with easy reporting on key metrics and critical programs."
- Case lifecycle: "Advocate features separate workflows for conduct cases, behavioral intervention, and Title IX… Staff members can easily track the time between phases and include them in reports. All actions taken on a case are captured within the Event Log and can be extracted for investigation purposes."
- Parties on the case: "The workflow includes the respondent, complainant, and witness to ensure each party is represented and communicated to effectively."
- Routing: "Universities can automatically route cases based on the type, the student(s) involved, and/or any other information chosen."
- CARE workflow: "Staff members can plan required assistance for each student and create the best course of action for students in need whether it be mental health support, connecting them to campus resources, or working with faculty to ensure a student is properly supported… universities can set up scoring thresholds, create a Students of Concern List for easy monitoring and create checklists and to-do dates to ensure assigned staff are completing follow-up tasks so no student is left unsupported."
- Feature surface: CARE Network, Case Management, Mobile-Adaptive Report Forms, Advocate Flex, Federal Reporting (Clery), Security & Compliance, Student Group Adjudication, Guest Tracker with Card Swipe Integration, Electronic Signatures, Student Sanction Document Upload, "Parallel Case Management COVID-19" (era-named parallel-case capability).
- Customer stories: UC Davis ("Streamlines Its Student Conduct Adjudication Process", user since 2012); WashU; Central Michigan; Kennesaw State (Advocate Flex "transforms case support"); Diablo Valley College quote: "It's been very helpful to be able to connect to so many different people with one case."
- L3: Advocate GME — a separate product for employee complaints/grievances (population split realized at product level).

## Product C — Branching Minds Canopy

### Key observations

- Positioning: "Canopy Case Management… securely connecting threat assessment, suicide risk screening, and ongoing student support"; "The only risk-aware MTSS case management platform" (Student Support Staff page); "Student Safety & Case Management" as a named solution category.
- Case as unit: "It helps safety teams document, track, and manage cases with clarity, while integrating that data into your MTSS ecosystem so support doesn't stop at the safety team's door." The before-state names the practice: "Cases are managed in spreadsheets, shared drives, or paper files that are hard to find, update, or audit."
- Lifecycle: "Evaluate Safety Risks → Provide Timely, Targeted Support → Monitor and Collaborate… Track intervention delivery, monitor student progress, and ensure every follow-up action has a clear owner and timeline."
- Guided protocols: "Guided CSTAG and C-SSRS workflows ensure consistent, defensible evaluations — every time, across every school"; C-SSRS, SAFE-T, CSTAG named; "Standardized risk classification ensures teams across buildings are evaluating and documenting threats the same way"; FAQ: "Canopy doesn't make decisions for your team… your team leads the judgment, classification, and next steps."
- Case file: "Maintain a complete, auditable record of every case — decisions made, actions taken, and follow-up completed"; "auto-saving, pause-and-resume flows, a built-in dashboard, change logs, and individual profiles detailing the historic safety information of a student."
- Tasks: "Built-in task management turns evaluation outcomes into assigned, trackable next steps with clear ownership and due dates."
- Holistic student view: "See the full picture behind a concern — attendance patterns, behavior incident history, academic performance, interventions, support meetings, and family communication — all in one place."
- Plan machinery: "Move from threat evaluation to ongoing support with targeted intervention plans directly connected to what the threat assessment revealed about a student's needs."
- Privacy: "Granular access controls support collaboration without compromising the sensitivity of case information"; "FERPA-compliant and secure, with strict user-based permissions and timestamped documentation"; "Only authorized users can access safety cases, and every action is logged for auditing."
- Oversight: "District leaders gain real-time visibility across schools and cases"; "Oversight of all cases and risk determinations."
- Customer evidence: Phoenix ESD #1 (Coordinator of Social Services & Wellness): "I can monitor things on an ongoing basis, new or open cases, task follow-up, and trends"; CCSD 59 (Assistant Superintendent): "we are gathering information on threat assessments and suicide risk assessments in one location, and we have data on what actions schools are taking as a result of those assessments."
- Packaging (L3): Canopy is a separate add-on to the Branching Minds MTSS platform; usable independently "for suicide risk, threat assessment, and case management."

## Product D — CPOMS StudentSafe

### Key observations

- Positioning: "Market leading software application for monitoring child protection and safeguarding"; "Supports your school's processes that work to monitor Child Protection, Safeguarding, pastoral and welfare concerns for pupils"; UK schools/MATs/nurseries/FE/international, part of Raptor Technologies.
- Concern capture: "Equips staff to capture safeguarding and wellbeing concerns when they arise — including securely logging incidents on mobile — so information reaches safeguarding leads promptly"; "Securely record incidents and low-level concerns from desktop, mobile, or anonymous QR code, with all entries automatically time- and date-stamped to maintain a clear safeguarding audit trail."
- **Incident→case escalation (key structural evidence): "Cases and Forms: Escalate any incident directly into a case for greater clarity and more effective case management. Link previous and future incidents to a case and collaborate more efficiently with staff and other agencies."**
- Chronology: "From low-level concerns to an array of forms, documents, interventions, notes, interviews and more, StudentSafe provides a comprehensive student chronology."
- Customization: "Tailor CPOMS StudentSafe to meet your school's exact needs, including categories of concern, user roles and permissions, input forms, severity ratings and alerts."
- Form checks: "Incorporate checks and balances such as whether a parent or carer has been notified or if assigned tasks have been completed."
- Caseworkers: "Staff and caseworkers can collaborate more effectively on interventions, tasks, follow-ups, and report sharing"; "ensure all relevant information is passed to caseworkers as quickly as possible."
- Tasks: "With trust-wide task management, school and trust leaders can oversee pupil support activity across every school, assign follow-up actions, and help ensure nothing is missed."
- Records continuity: "Transferable Records — allows schools, with the appropriate consent, to readily obtain and share any portion of a Child Protection history for pupils transferring to and from your school, ensuring continuity of care."
- Audit: "All incidents, actions and key transactions… are time, date and user stamped… Now you can track and analyse what has been done, by whom and when."
- Access: "With intelligent role-based access, CPOMS StudentSafe allows each school to control who has access to what information and when."
- Population substrate: "MIS Integration — Integration with leading MIS systems prevents the need to enter data twice"; links attendance data.
- Multi-agency: Engage products "connect schools, MATs, and external agencies, securely sharing information"; "collaborate more efficiently with staff and other agencies."
- Policy execution framing: "Putting Your Safeguarding, Wellbeing & Attendance Policies into Action… referrals, child-on-child abuse, interventions, attendance, persistent absence, and more."
- Customer evidence (Headteachers/safeguarding leads): "A system that allows you to record, share and track concerns and incidents"; "providing a chronology of our records, allowing all DSPs to have access to the latest information about pupils and enabling us to pass on records securely to new schools… During a recent Safeguarding audit and an Ofsted inspection, inspectors were very happy with our record keeping systems"; "it alerts other staff that you have selected, to read the entry, ensuring that all DSL/DDSLs are kept in the loop"; "chronological reports and also allowing the early identification of trends."
- L3: AI-assisted category suggestion and plain-language descriptions (staff-reviewed); Universal Safeguarding framing; Insight (MAT analytics); VisitorSafe; Ofsted/Estyn inspection checklists.

## Product E — Salesforce Education Cloud

### Key observations

- Case management as a platform capability: "Education Cloud's common capability model for things like scheduling, case management, and application form-building helps reduce total cost of ownership and scale impact institution-wide."
- Student Success module: "Connect students to the right staff with streamlined appointment scheduling. Help learners reach their academic, career, and personal goals with customizable care and action plans… give them one place to manage their learner journeys with a tailored portal"; "Get the early indicators required to identify students in need and quickly intervene with data-driven alerts."
- Case-shaped UI evidence: "A student portal with case engagement details such as the course, GPA, the number of care plans, and record alerts"; "A case record that shows a student's academic details, including alerts"; "A student profile with an event timeline and details like term start and end dates, care plans, and credits earned."
- SIS context: next-gen SIS vision; education-specific objects as native platform objects.
- L3: Agentforce AI; edition pricing; module breadth (recruitment/admissions, academic operations, student financials, advancement). Corroboration from the academic-advising pass: Salesforce "case records with alerts" inside advising — the case object recurs across surfaces.

## Cross-product Comparison

| Structure | Maxient | Advocate | Canopy | CPOMS StudentSafe | Salesforce Edu Cloud | Verdict |
|---|---|---|---|---|---|---|
| Case as unit of record about a student, worked to resolution | "Manage Case Types"/workflow; conduct records | "separate workflows for conduct cases, behavioral intervention, Title IX"; My Cases | "document, track, and manage cases" | "Escalate any incident directly into a case" | case records/case engagement details | **All 5 — core** |
| Identified student bound to the case; population fed from SIS/MIS | Banner/PeopleSoft/Workday/Colleague/Jenzabar; schedules & ID photos | routing by "the student(s) involved" | student profiles; SIS integration; holistic view | MIS integration; attendance links | student profiles/SIS capabilities | **All 5 — core (SIS/MIS feed = dominant implementation)** |
| Issue/concern-driven intake (report/referral/concern/alert) | online reporting forms routed by content | mobile-adaptive report forms; auto-routing | safety concerns; screenings | concerns from staff/mobile/anonymous QR | data-driven alerts | **All 5 — core** |
| Assigned responsible staff carrying the case | workflow (B) | assigned staff; follow-up tasks | "clear owner and timeline" | tasks assigned to staff; caseworkers named | "connect students to the right staff" | **All 5 — core** |
| Dated/attributed casework record accumulating on the case | records; audit trails | Event Log of all actions; extractable | "complete, auditable record of every case" | chronology; time/date/user stamps | event timeline | **All 5 — core** |
| Task/follow-up machinery | (implied by workflow) | checklists, to-do dates | built-in task management | task oversight; follow-up actions | action plans | **4–5 — core** |
| Coordination across offices/agencies | "coordinate the efforts of departments" | CARE network; case parties | safety teams + MTSS staff | "staff and other agencies"; Engage sharing | cross-department platform | **All 5 — core** |
| Need-to-know access control + audit trails | case-based access restrictions; audit trails | security & compliance | granular access controls; action logging | intelligent role-based access; full audit | permissions | **All 5 — core** |
| Plan machinery (care/support/response/intervention plans) | not foregrounded | CARE course of action | response/intervention plans | interventions recorded | care and action plans | **4/5 — common** |
| Guided protocol/framework workflows | school-defined process | Title IX-compliant workflows | CSTAG/C-SSRS guided flows | custom protocols/forms; referral forms | (configurable) | **4/5 — common, content varies** |
| Reporting/analytics on cases (volumes, trends, outcomes) | analytics/dashboards; Clery | reporting on key metrics | dashboards; risk visibility | reports/dashboards; trend analysis | analytics | **All 5 — common** |
| Communication to parties/staff | letters with pickup notification; texting | party communication | (family communication in view) | alerts to selected staff; parent-notified checks | student portal | **All 5 — common** |
| Formal eligibility gate / mandated plan / regulatory timelines | absent | absent | absent (protocols advisory-guided) | absent (statutory context, no in-product gate) | absent | **0/5 — the Special Education seam** |
| Conduct/hearings/sanctions depth | discipline + academic integrity + Title IX + Clery | conduct adjudication; sanction docs; hearings implied | (threat assessment, not conduct) | (racial incidents recorded; conduct not central) | (not foregrounded) | **segment variant** |
| Anonymous intake channels | (not evidenced) | (not evidenced) | (not evidenced) | anonymous QR code | (not evidenced) | **1/5 — optional** |
| Records transfer between institutions | (not evidenced) | (not evidenced) | (not evidenced) | transferable child-protection history | (not evidenced) | **1/5 — optional** |
| AI assistance | explicitly none (vendor stance) | (not evidenced) | Dottie AI/Meeting Assistant (platform) | AI-assisted descriptions/category suggestions | Agentforce | **era-current, optional** |

## Canonical Model

### L0 — Defining Invariant (deliberately small)

Three jointly-held structures:

1. **The student case of record** — a persistent identified case about a specific concern regarding an identified student of the institution, opened through intake (a report, referral, concern, or alert), assigned to a responsible staff member, and carried through a tracked lifecycle to a recorded resolution. Remove → an alert feed or incident log (behavior territory) or a triage queue (service-desk territory).
2. **The worked-and-documented case file** — dated, attributed casework accumulating on the case as staff work it: notes, contacts/meetings, tasks/follow-ups with owners, documents, actions taken, referrals, coordination with other offices/agencies. Remove → empty case shells / a case register nobody works; remove the case container → a free-floating notes log.
3. **The student's cross-case record inside the institution** — cases bind to the institution's enrolled-student population (in practice fed by the SIS/MIS), and cases, incidents, and interactions accumulate per student into a retrievable history ("chronology"/"the full student story") that staff use for context, continuity of care, and accountability. Remove → an anonymous ticket system; remove the institution-student binding → generic case management.

Jointly-held load-bearing: 1 alone = case register nobody works; 2 without 1 = documentation log with no container; 3 without 1 = student CRM; 1+2 without 3 = generic case tracker (HR/help-desk shape); 1+3 without 2 = case shells; 2+3 without 1 = chronology with no case container (behavior-log shape).

### L1 — Common Mature Structure

- Report/concern intake forms (web and mobile), routed by content, type, or parties
- Task/follow-up management with owners and due dates; reminders/checklists
- Plan machinery on the case: care/support plans, intervention plans, response plans, courses of action
- Multi-party case records (complainant/respondent/witness; family/guardian-notified checks)
- Need-to-know role-based access control; case-based access restrictions; full audit trails
- Reporting/dashboards on case volumes, categories, trends, outcomes; institutional oversight views
- SIS/MIS integration as the student-population substrate (rosters, schedules, ID photos, attendance links)
- Communication tools: letters/notifications to parties and staff, pickup/read receipts, staff alerting

### L2 — Variant / Optional Structure

- Concern-domain packaging: conduct + Title IX + academic integrity (higher-ed conduct offices); safeguarding/welfare (K-12 UK); safety/threat assessment (K-12 US); wellbeing/CARE; complaints/sexual misconduct; attendance
- Case-construction grammar: case-first (every report becomes a case with a workflow type) vs escalation-first (concerns/incidents logged, escalated into cases when sustained casework is needed) vs protocol-assessment-first (guided evaluation flows that generate case follow-up)
- Guided protocols: formal assessment instruments (CSTAG/C-SSRS/SAFE-T class) vs institution-defined categories/processes
- Anonymous intake channels; records transfer between institutions; multi-agency data-sharing portals
- Regional accountability machinery: Clery federal reporting (US higher ed), Ofsted/Estyn audit-readiness (UK) — variants, not structure
- Segment straddle: higher-ed conduct loops administered through case machinery (see Boundary Findings 1)
- AI assistance (descriptions, category suggestions, summaries, drafting) — era-current
- Deployment: standalone specialist products vs modules of SIS/CRM suites (Anthology-class unverified; Salesforce verified as suite-capability pole)

### L3 — Vendor-specific (Research Notes only)

- Maxient: no-modules single price; "no AI/predictive models/scoring" stance; Clery features; records-ownership framing; 1,300+ schools; founded 2003.
- Advocate: Advocate Flex (custom workflows); Advocate GME (employee-side sibling product); Federal Reporting Engine; Students of Concern List; scoring thresholds; guest tracker with card swipe; sanction document upload; "Parallel Case Management COVID-19."
- Canopy: CSTAG/C-SSRS/SAFE-T guided flows; add-on packaging beside the MTSS core platform; Dottie AI + Meeting Assistant; risk map; SOC 2 framing; district customer evidence.
- CPOMS: Universal Safeguarding framing; StudentSafe/StaffSafe/Engage/Insight/VisitorSafe family; anonymous QR capture; transferable records; Ofsted/Estyn checklists; Raptor Technologies ownership.
- Salesforce: Agentforce; Education Data foundation; edition pricing; module breadth.

## Vendor-specific Findings

See L3. None promoted to the canonical document except as de-branded illustrations (e.g., formal threat-assessment protocols as a guided-workflow variant; anonymous QR intake as an optional channel; records-transfer as an optional continuity capability).

## Boundary Findings

**1. vs Student Behavior Management (§23, processed; joint-review flag DISCHARGED from this side). Keep-both RATIFIED.** That pass recorded the seam: "case management is issue-driven casework with an ongoing responsible party… the incident loop itself has no eligibility gate, no mandated plan, no caseload." This pass confirms and sharpens it: Student Behavior Management runs the school's conduct-event loop over the general population — events of record classified against a school-wide framework, closed by administrative resolution, accumulated for pattern measurement — with no assigned case owner and no sustained worked container. Student Case Management holds issue-driven cases with an assigned responsible party worked over time. The seam runs through products, and CPOMS StudentSafe documents it structurally: staff record low-level concerns/incidents first (behavior-log shape, time-stamped), then "escalate any incident directly into a case" when sustained management is needed — with previous and future incidents linked to the case. The higher-ed segment shows the converse: university conduct loops (Maxient, Advocate) are administered through case machinery (case types, workflows, parties, phases, outcomes) — a segment realization where conduct is case-managed; see Boundary Issue A. Removal tests: remove the case container + responsible party, keep the school-wide framework + event loop → Student Behavior Management; add the case container + owner → this Type.

**2. vs Special Education Management (§23, processed) — RATIFIED from this side.** That pass's discriminator holds exactly: the regulated machinery (evaluation→eligibility gate + legally-mandated plan content + regulatory timeline tracking) is present in none of the five sampled student-case products. Special-ed plans are produced under legal mandate with in-product timeline/compliance state; case-management plans (care/intervention/response) are institution-defined support plans. Remove the eligibility gate + mandated plan from special-ed → this Type; add them → special-ed.

**3. vs Academic Advising Platform (§23, processed; joint-review flag DISCHARGED from this side). Keep-both RATIFIED.** That pass recorded: "Case management is issue-driven: a case is opened for a problem and worked to closure. Advising is relationship-driven: an ongoing advisor–student bond with recurring interactions… The case is one object type inside this Type, not its center." This pass confirms the case as the unit of record on this side: every sampled product's center is the case worked to closure; none centers an ongoing staffed relationship. Same products straddle (Salesforce case records inside Student Success; EAB "Cases & Referrals" inside advising) — center-of-gravity seam, consistent with the mobile-pos/retail-pos sibling precedent. Removal tests: strip the case container and keep the ongoing relationship/appointments/notes → advising; strip the relationship and keep issue-driven cases → this Type.

**4. vs Social Services Case Management (§24, processed) and Nonprofit Case Management (§25, processed).** Same casework-machinery family (person of record + episode + documented record). The seam is the served population and the mandate: those Types serve external clients/beneficiaries under public-program or org-program mandates with recorded eligibility/need determinations against program rules; Student Case Management serves the institution's OWN enrolled student body for concerns arising in student life, with education-privacy framing instead of program eligibility. K-12 safeguarding refers out to statutory agencies (CPOMS Engage multi-agency sharing) — the referral handoff marks the line; the statutory agency's casework is Child Welfare Management / Social Services territory.

**5. vs Child Welfare Management (§24, processed).** School-side safeguarding (CPOMS-class) records concerns, maintains chronologies, and refers to authorities; the statutory child-protection agency's machinery (mandated-report screening with legal force, placement, court-anchored permanency) is Child Welfare Management. The school-side safeguarding case stays in-type here as a welfare/safeguarding variant.

**6. vs HR Case Management (§09, processed).** Same machinery, different population and context (employees vs enrolled students; workplace concerns vs student-life concerns). The population split is real enough that vendors split products (Symplicity sells Advocate for students and Advocate GME for employees as separate offerings).

**7. vs Student Success Platform (§23, UNPROCESSED — flag for that pass).** Retention-analytics platforms center population-level risk/measurement; case objects may be embedded (Salesforce Student Success ships case records, care plans, alerts; the academic-advising pass found the same pattern). Center-of-gravity test: population-scale analytics/measurement vs issue-driven casework. Flag recorded.

**8. vs Student Services Portal (§23, UNPROCESSED — flag for that pass).** Transaction-resolution service requests (one-and-done answers, agent queues, SLA-shaped handling) are customer-service machinery; this Type's center is sustained casework over student concerns. Where a student-services operation runs service tickets, the tooling converges toward the customer-service family. Flag recorded.

**9. vs School Counseling Management (§23, UNPROCESSED — note for that pass).** Consistent with the advising seam: counseling centers an ongoing counselor–student support relationship (caseload, appointments, notes); this Type centers issue-driven cases. Counselors commonly participate in cases as caseworkers (CPOMS role surface) — role overlap, object separation.

**10. vs CRM (§07).** "Education CRM" is a positioning wrapper (Salesforce self-labels so). The constituent population, the case-of-record model, and the education context are what this leaf documents.

**"去掉什么就变成另一个 Type" 判据汇总**: remove the case container + responsible party (keep framework + event loop) → Student Behavior Management; add the eligibility gate + mandated plan + regulatory timelines → Special Education Management; replace issue-driven cases with an ongoing relationship loop → Academic Advising (or School Counseling, K-12); serve external clients under program eligibility mandates → Social Services / Nonprofit Case Management; move to the statutory agency's side of the safeguarding referral → Child Welfare Management; swap students for employees → HR Case Management; drop the student model → generic case tracker; drop the worked container → behavior log / notes chronology; drop sustained casework for one-and-done transaction resolution → service-desk territory.

## Historical / Market-Sample Check

- **Paper-era dean-of-students office (conceptual check)**: a case file opened on a student concern (complaint letter, incident report), assigned to a dean, dated notes of meetings and calls, letters to the parties, recorded outcome, filed with the student's record — all three L0 legs at analog level. No digital intake, no dashboards, no AI.
- **Paper-era school safeguarding (UK)**: child-protection concern log, per-child chronology, referral forms to external agencies, case-conference notes, inspection-ready record keeping — satisfies the same three legs.
- **2003-generation conduct systems (Maxient's founding generation)**: report forms, case records, workflow, records retention — fits without modern alerting/AI/portal layers.
- Conclusion: the L0 names no report forms, no protocols, no concern domains, no AI, no portals — it does not over-fit to the current SaaS shape.

## Uncertainties

1. **No Tier-1 operational documentation reachable for any sampled product** — all direct evidence is Tier-2 official product pages. No exact case-status vocabularies, numeric limits, default values, phase counts, or timing rules are asserted anywhere; the final document describes lifecycle and structures conceptually.
2. The precise object grammar inside products (case vs incident vs concern vs referral as separate object types vs states of one object) varies and is not operationally verified; CPOMS evidences incident→case escalation, Advocate evidences typed case workflows, but the full range is not mapped.
3. Assignment mechanics (named case owner vs shared team ownership vs role queues) are evidenced at feature-name level only (task owners, caseworkers, "assigned staff"); how products mix them is unverified.
4. The SIS-suite module pole (Anthology-class) could not be verified — anthology.com product pages now surface Blackboard content; the suite-pole evidence rests on Salesforce Education Cloud alone.
5. Non-US/non-UK regimes (e.g., European university student-affairs casework, Australian wellbeing systems) were not sampled; the jurisdiction-neutral framing rests on the two-region sample (US + UK).
6. Whether K-12 US districts commonly run welfare/wellbeing casework on dedicated case products (vs folding it into MTSS/success platforms) was not fully tested; Canopy's add-on independence suggests both postures exist.
7. Market size/ordering of the poles (conduct offices vs safeguarding leads vs safety teams vs student-affairs CARE teams) could not be quantified from accessible sources.

## Final Synthesis

Student Case Management is the education institution's issue-driven casework system for its own student body. Its defining core is three jointly-held structures: the student case of record (a persistent identified case about a specific concern regarding an identified student, opened through intake — report, referral, concern, or alert — assigned to a responsible staff member, carried through a tracked lifecycle to a recorded resolution); the worked-and-documented case file (dated attributed casework — notes, contacts, tasks/follow-ups with owners, documents, actions, referrals, cross-office/agency coordination — accumulating on the case); and the student's cross-case record inside the institution (cases bind to the SIS/MIS-fed student population and accumulate per student into a retrievable chronology used for context, continuity, and accountability). Mature products add intake forms with routing, task management, plan machinery (care/intervention/response plans), multi-party records, need-to-know access control with audit trails, reporting/dashboards, and SIS integration. The Type is concern-domain-agnostic: conduct/Title IX/academic integrity (higher-ed), safeguarding/welfare (K-12 UK), safety/threat assessment (K-12 US), wellbeing/CARE, complaints — segment configurations, not separate Types, with the market realizing case-first, escalation-first, and protocol-first grammars. The Type is bounded by Student Behavior Management (event loop without casework; the seam is documented in-product by incident→case escalation), Special Education Management (the regulated eligibility/plan/timeline machinery), Academic Advising (relationship-driven vs issue-driven; case objects inside advising), Social Services/Nonprofit Case Management (external clients under program mandates), Child Welfare Management (the statutory agency's side of the referral), and HR Case Management (population swap), with flags left for Student Success Platform and Student Services Portal.
