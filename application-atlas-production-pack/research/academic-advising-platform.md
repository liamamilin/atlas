# Research Notes — Academic Advising Platform

Research date: 2026-09-06
Slug: academic-advising-platform
Directory location: §23 Education, Research & Knowledge Institutions (siblings: Student Success Platform, Student Case Management, School Counseling Management, Tutoring Platform, Student Information System / SIS, Course Registration System)

---

## Research Goal

Understand what "Academic Advising Platform" software actually is as an Application Type: who operates it, what core objects exist inside it, how the advising workflow (relationship → appointment → documentation → follow-up) works, how alerts and academic planning fit in, and where its boundary sits against the neighboring Student Success / SIS / Case Management / School Counseling / Tutoring Types.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: institution-operated software that manages the advising relationship between advisors (professional or faculty) and students: student profiles with academic context, advisor assignment/caseloads, appointment scheduling, advising notes, early alerts/progress reports, degree/program planning, outreach campaigns, and reporting for retention.
- Primary users: professional advisors, faculty advisors, advising/success administrators; students as the self-service counterparty; instructors as alert sources; other student-service offices as referral targets.
- Most likely confusions:
  - Student Success Platform (broader retention/analytics framing; same vendors, often same product)
  - Student Information System / SIS (system of record for enrollment/grades; advising consumes its data)
  - Student Case Management (issue-driven cases vs relationship-driven advising)
  - School Counseling Management (K-12 population, postsecondary-planning focus)
  - Tutoring Platform (instruction delivery vs academic guidance)
  - CRM (education CRMs position advising inside a constituent lifecycle)
- Unknowns going in: whether degree audit/planning is definitional or common; whether early alerts are definitional; how strongly the market ties this Type to "student success" positioning; whether appointment scheduling is definitional.

## Research Questions

1. What are the core objects (student profile, advisor, caseload/assignment, appointment, note, alert/flag/referral, plan/audit, campaign/list, case)?
2. How does the advising loop work: who initiates, how are appointments booked and by what semantics (reason/service), what gets documented, what follow-up machinery exists?
3. How does the intervention loop work: where do alerts come from (faculty progress reports, LMS signals, predictive models, self-reports), how are they routed, tracked, closed?
4. How does academic planning work where present: degree audit, term-by-term planner, what-if, pathways, exceptions/waivers, registration hand-off?
5. What roles exist (advisor, faculty, student, admin, other offices) and what can each see/do?
6. What integrations are structural (SIS, LMS, calendar, CRM)?
7. What student-facing surfaces exist (portal/app: scheduling, plan, to-dos, holds, self-report)?
8. Where is the boundary with Student Success Platform, SIS, Student Case Management, School Counseling Management, Tutoring Platform?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

| Product | Segment | Philosophy | Evidence quality |
|---|---|---|---|
| EAB Navigate360 | market leader; 2-yr + 4-yr, public + private, HBCUs, systems, R1s | "student success CRM" — coordinated care network across the student lifecycle | Medium-strong (detailed product page + FAQ; help center behind client login) |
| Stellic | R1s, large publics, small privates, community colleges, international | planning-first — degree audit/planner as the spine, advising "Care" around it | Medium-strong (three detailed product pages + FAQ; support site 404) |
| Salesforce Education Cloud (Student Success module) | large institutions with CRM ecosystems | CRM-platform — advising as a module on a configurable education data platform | Medium (rich product page; help articles not fetched; datasheet PDF binary-only) |
| Civitas Learning | community colleges + universities | analytics-first — institution-specific predictive models driving advising workflows | Medium (product + advising use-case pages; help behind login) |
| TracCloud (Redrock Software) | 2,700+ centers, heavily community colleges; advising/tutoring/testing centers | scheduling-first center management — appointment machinery + early alert + success plans | Medium-strong (root + advising product pages; operational wiki 403) |

Anthology Starfish — historically a defining product of the category (early alert + advising network + degree planning) — could not be used: the vendor has been split up (Anthology → Blackboard / Ellucian / Encoura), Starfish is no longer marketed as a standalone product on the sunset page, and kb.anthology.com returned a transport error. The early-alert heritage is instead evidenced via TracCloud SAGE and the alerts modules of the sampled products.

## Sources

Tier 2 (official product pages; no Tier-1 help-center article was reachable in this environment):

- EAB Navigate360: https://www.eab.com/technology/navigate — fetched 2026-09-06 (feature list, FAQ, integration list, data-source statement)
- Stellic: https://stellic.com/ , https://stellic.com/care , https://stellic.com/progress — fetched 2026-09-06 (module feature lists + FAQs defining "advising technology" and "degree audit software")
- Salesforce Education Cloud: https://www.salesforce.com/education-cloud/ — fetched 2026-09-06 (Student Success / Academic Operations module features, FAQ); Student Success datasheet PDF fetched but binary-only (not usable)
- Civitas Learning: https://www.civitaslearning.com/ , https://www.civitaslearning.com/advising-and-student-success/ — fetched 2026-09-06 (platform framing + advising workflow features)
- TracCloud (Redrock Software Corporation): https://www.go-redrock.com/ , https://www.go-redrock.com/advising-center-management/ — fetched 2026-09-06 (scheduling, SAGE early alert, success plans, staff management, reporting)

Failed / limited sources (abandoned per source-access rules):

- kb.anthology.com — transport error (Starfish documentation unreachable; vendor split)
- wiki.go-redrock.com (TracCloud operational wiki) — 403
- support.stellic.com — 404
- help.salesforce.com Education Cloud articles — not located without search engines (DuckDuckGo timed out; Bing geo-returned unusable regional results)
- EAB and Civitas help centers — behind client login

Evidence consequence: all observations below are from official product/marketing surfaces (Tier 2). They are detailed about module existence and positioning but positioning-level about operational behavior. No precise operational claims (exact statuses, limits, defaults, approval rules) are made from this sample.

---

## Product Observations

### EAB Navigate360 (evidence layer A for feature existence; positioning is Tier 2)

Positioning: "the leading higher education CRM… a powerful technology trusted by more than 850 institutions and serving more than 10 million students… unites administrators, faculty, staff, students, and alumni in a collaborative network that supports the full student journey from recruitment to career success." (vendor claims; recorded as claims, not facts)

Staff workflow & automation features (direct evidence of module existence): Complete Student Profile; Coordinated Care Network; Cases & Referrals; Automated Alerts & Messaging; Two-Way SMS; Campaigns & Template Library; To-Dos; Appointments & Surveys; Events; Notes & Attachments; Faculty Progress Reports.

Key operational findings:

- **Data foundation**: "The main source of data used to populate Navigate360 comes from the institution's student information system (SIS). This data is used to populate student profiles and inform queries that can then be used to drive workflows for specific student populations." Optional LMS data, Common App data, custom datasets (financial aid, housing). System-agnostic integration stance with pre-built integrations (Ellucian, Jenzabar, PeopleSoft, Workday Student, Canvas, Blackboard, Brightspace, Moodle).
- **Student-facing app** (iPhone/Android/desktop): appointment scheduling, campus resources and documents shared by advisors, To-Dos, Student Journeys; Student Engagement module adds Program Advising, Program Explorer, Holds Center, Study Buddies, Financial Planner, Career Match, Student Hand Raise (self-reporting concern), AI knowledge agent.
- **Staff AI assistant**: draft outreach, find data/reports, prep meetings, live transcription and AI meeting summaries, launch campaigns/tasks/alerts/follow-ups from the same workflow.
- **Analytics**: dashboards monitoring student progress; templated reports for "ongoing advising activities"; population health analytics; intervention effectiveness analytics; predictive models (vendor claims 200+ custom-built models); automated workflow from reports.
- **Users**: "Current students, prospective students, faculty, staff, and administrators all use Navigate360 as part of a Coordinated Care Network. Staff users often include… advising, enrollment, career services, and tutoring."
- **Deployment**: cloud SaaS on AWS; enterprise licensing (no per-user fees); dedicated "Strategic Leader" consultant; FERPA/GDPR compliance stated.
- **Scope breadth**: Enrollment CRM (recruitment), Advancement CRM (alumni/donors) extend the same platform beyond advising.

### Stellic (evidence layer A for feature existence; positioning is Tier 2)

Positioning: "The student journey platform for higher education… turns academic planning into a path every student can see and every office can support, all the way to graduation." Four packages: Progress, Care, Explore, Registration. Roles addressed: Registrars, Provosts, Advisors, CIOs.

Progress (planning/audit module — direct evidence):

- **Degree audits**: "real-time view of degree progress" for students and academic advisors.
- **Audit-aware planner**: "true multi-year academic planning grounded in degree audit logic, so every term reflects real requirements and constraints."
- **What-if exploration**: switching majors, adding minors, changing catalog years — "every scenario runs against real institutional rules."
- **Pathways**: how different degree paths or timelines impact progress; risk surfaced early.
- **Milestones and requirements**: coursework and non-course degree requirements.
- **Transfer credits and exceptions**: evaluates transfer credits; staff tools for "course substitutions, waivers, and exceptions with real-time updates."
- **Requirements management**: drag-and-drop requirements editor (no code); automated alerts, exceptions, degree completion checks; course demand reports from plans/pathways.
- **Registration**: optional add-on — "one-click course registration… supported by real-time SIS integration."
- FAQ defines degree audit software: "compares a student's completed and in-progress courses against their specific degree requirements… handles the full complexity of institutional rules: repeated courses, prerequisites, GPA thresholds, transfer credits, and course-to-requirement matching."

Care (advising module — direct evidence):

- **Student profile**: "Collaborate on a shared view of student progress, circumstances, and engagement."
- **Notes**: "Log and reference insights about each student in a central hub, with summaries to understand context quickly" — keeps "their support network informed."
- **Messaging**: individual or bulk in-app messaging "tied to the student record."
- **Early alerts and signals**: "early alerts and LMS-driven engagement signals to identify students who may be at risk."
- **Appointments**: "flexible appointment types" for advisor calendars.
- **Filtering and reports**: sort/check in on students "based on indicators like missed appointments, engagement trends, or raised concerns"; saved reports.
- **Student support network**: connect the advising success network "so students understand how to get help."
- **Referrals and concerns**: "Flag critical issues, route referrals to the appropriate offices, and track follow-up."
- **Admin analytics**: student success and support trends for resource decisions.
- FAQ defines advising technology: "software that helps higher education institutions coordinate student support, communication, and outreach across advisors, departments, and teams. It brings together student data, advising interactions, and workflows so that support is proactive rather than reactive."

Explore (transfer/prospective module): pathways for prospective students matching goals and earned credits; transfer rules management; AI transcript analysis.

Institution quotes confirm cross-office use: "not just within academic advising, but also within student affairs and student support units" (UVA); registrar-side curriculum autonomy (Duke).

### Salesforce Education Cloud — Student Success module (evidence layer A for feature existence; positioning is Tier 2)

Positioning: "Education Cloud… bring[s] together the #1 AI CRM and next-gen SIS capabilities"; modules for Recruitment and Admissions, Academic Operations, Student Success, Student Financials, Advancement. (Now marketed under "Agentforce Education (formerly Education Cloud)".)

Student Success module (direct evidence):

- **Personalized Learner Support**: "Connect students to the right staff with streamlined appointment scheduling. Help learners reach their academic, career, and personal goals with customizable care and action plans. And give them one place to manage their learner journeys with a tailored portal."
- **Holistic Advising Experiences**: "Visualize learners' progress faster by activating student data — academic, wellbeing, LMS engagement, and more. Get the early indicators required to identify students in need and quickly intervene with data-driven alerts."
- **Wellbeing and Career Readiness**: "regular cadence of pulse checks to proactively capture student wellbeing"; competency development tracking.
- **Agentforce: Advising Support**: "Generate comprehensive student summaries of key advising details. Obtain campus policy-based insights and identify best-fit resources."
- UI evidence: "An advisor console with one place to schedule appointments and view key student engagement details"; student profile with event timeline, term start/end dates, care plans, credits earned; case record showing course, GPA, number of care plans, record alerts; scheduling console showing "details on the assigned advisors."

Academic Operations module (adjacent, same platform): Flexible Catalog Design (degrees, certificates, badges; prerequisites/corequisites); Intelligent Degree Planning ("Streamline degree progress, empower learners to make informed program decisions"); Effortless Registration Management (waitlists, eligibility, registration).

Platform facts: common capability model ("scheduling, case management, and application form-building" shared across modules); education-specific objects (grades, courses) as native platform objects; per-user pricing editions.

### Civitas Learning (evidence layer A for feature existence; positioning is Tier 2)

Positioning: "Institutional Impact Management… brings your institutional data, predictive intelligence, and daily operations into one Impact Platform — with AI agents and predictions grounded in your institution's students, programs and patterns, not national averages." Data sources: SIS, LMS, CRM, event/activity data, graduate outcomes.

Advising & Student Success use-case page (direct evidence):

- **"Access Student Information in One Place"**: "Consolidate student information into a comprehensive profile. Coordinate student care across campus with centralized notes and academic alerts."
- **"Easily Prioritize Student Engagement"**: "Monitor individual or groups of students to prioritize and organize outreach. Quickly send communications or schedule appointments from automated student lists."
- **"Simplify Course Enrollment"**: "Collaborate with students on degree plans and class schedules to ease registration. Inform outreach efforts based on real-time student planning and scheduling behavior."
- **Understand the Whole Student**: actionable insights "like which students might not persist or graduate and why… including holds, financial aid status, course history, advising notes, and engagement opportunities."
- **Prioritize Engagement**: "Automatically identify a list of students to engage throughout the term based on factors such as a change in persistence likelihood or unfinished schedules."
- **Personalize Outreach**: scalable personalized communications; "Determine which channels are most effective for particular students… and take action within the same system."
- **Case management tools**: "intelligent case management tools like dynamic lists and shared notes"; "Share notes, raise alerts, and coordinate student care across leadership, advisors, faculty, and student success teams."
- **Collaborate on Academic Plans**: "Collaborate with students on degree plans and class schedules… Monitor degree planning and registration activity to prioritize outreach."
- Advisor testimonial (Jacksonville State): "Student Scheduling saves time during the course selection and registration process."
- Platform-level: institution-specific predictive models ("89% accuracy predicting outcomes" — vendor claim), impact measurement of interventions, AI agents with "autonomy tiers, contact caps, and a full run history."

### TracCloud / Redrock Software (evidence layer A for feature existence; positioning is Tier 2)

Positioning: "Cloud-based software management solutions for learning, advising, and fitness centers at colleges and universities"; "TracCloud is a student retention, scheduling, and reporting system"; customized for "academic advising centers, tutoring centers, admission counseling, career advising, student retention services, testing centers, first year experience…" (2,700+ centers claim).

Advising Center Management page (direct evidence):

- **SIS link**: "Link with your student information system to maintain accurate and up-to-date contact, demographic, and enrollment data from your registrar."
- **Role-based permissions**: "Manage advisors across multiple centers and locations with role-based permissions to limit access to only what's essential for each individual."
- **Reason-based scheduling**: "appointments to be booked by reason or services, ensuring students connect with the right support"; in-person, virtual, phone, and asynchronous appointments; "Specialized Counselor Matching — assign staff based on reason-based specialties or degree paths"; "Student-Driven Scheduling — allow students to request alternative times."
- **Waitlist**: live queue with "place in line and estimated wait time."
- **SAGE early alert**: "a customizable online system that enhances communication between faculty and student support centers"; "Easy Faculty Referrals — intuitive, customizable forms"; "Progress Monitoring — mid-term and final faculty reports"; "Actionable Recommendations — suggests tailored support like tutoring, workshops, or advising"; "Automated Alerts & Tracking — sends targeted emails with follow-up reporting." Client quote describes a "three-tiered SAGE referral process" with email/letter/phone/text outreach.
- **Success Plans**: "structured, trackable pathways… customizable steps and automated progress tracking… tasks like center visits, survey responses, or document uploads… trigger new Success Plans as students complete their milestones."
- **Communications**: mass email, unlimited-length texts, automated appointment reminders (email/text), triggered surveys, dashboard notifications, iCal/calendar sync.
- **Student interface**: "Book advising, tutoring, and other success services in just a few clicks"; self-serve kiosk check-in; student dashboard.
- **Staff management**: 1-on-1, group, or drop-in sessions with subject-specific availability; "stacked availability" across centers; staff work plans; payroll tracking (hours, pay rates, work types).
- **Reporting**: fully customizable reports on any data point; pre-made templates; scheduled delivery; heatmaps by center/subject/date; assessments (custom questionnaires with targeted support in low-scored areas).

---

## Cross-product Comparison

| Dimension | EAB Navigate360 | Stellic | Salesforce Education Cloud | Civitas Learning | TracCloud |
|---|---|---|---|---|---|
| Self-description | higher education CRM / student success | student journey & academic planning platform | CRM + next-gen SIS platform, Student Success module | Institutional Impact Platform (analytics-first) | retention, scheduling & reporting system for centers |
| Student record | Complete Student Profile, SIS-populated | shared student profile (progress, circumstances, engagement) | student profile w/ timeline, term dates, care plans, credits | comprehensive profile: holds, financial aid, course history, notes, engagement | SIS-linked contact/demographic/enrollment data |
| Advisor relationship | Coordinated Care Network (advising, enrollment, career, tutoring staff) | advisors + student support network in shared space | "assigned advisors" in scheduling console | advising teams; coordinate care across departments | advisors across centers/locations; role-based permissions; counselor matching by specialty/degree path |
| Appointments | Appointments & Surveys; student self-scheduling | flexible appointment types | streamlined appointment scheduling; advisor console | schedule appointments from student lists | reason-based booking; in-person/virtual/phone/async; waitlist w/ live queue; kiosk check-in; reminders; calendar sync |
| Notes | Notes & Attachments | Notes hub w/ summaries, shared with network | care plans; case records | centralized/shared notes | session documentation (implied by visit tracking); work plans (staff-side) |
| Alerts / early intervention | Automated Alerts; Faculty Progress Reports; Cases & Referrals | early alerts + LMS engagement signals; referrals & concerns w/ follow-up tracking | data-driven alerts; early indicators; wellbeing pulse checks | academic alerts; persistence-likelihood change lists | SAGE faculty referrals; mid-term/final progress reports; recommendations; follow-up reporting |
| Academic planning | Program Advising; Program Explorer; AI course-planning guidance | degree audit + audit-aware multi-year planner + pathways + what-if + exceptions (center of gravity) | Intelligent Degree Planning; catalog design; registration mgmt | collaborate on degree plans & class schedules; monitor planning/registration activity | Success Plans (task-based steps, not degree audit); no degree audit observed |
| Outreach | Campaigns & Template Library; Two-Way SMS; To-Dos | bulk in-app messaging | personalized communications (platform) | automated student lists; channel-effectiveness; take action in-system | mass email; texts; triggered surveys; dashboard notifications |
| Student portal/app | student app: scheduling, To-Dos, Journeys, Holds Center, Hand Raise | student planner/audit experience | tailored student portal | (student scheduling surfaces) | student dashboard; self-serve booking; kiosk |
| Analytics | population health; intervention effectiveness; predictive models (claim: 200+) | admin analytics; course demand reports | proactive analytics integrated per module | institution-specific predictive models; initiative impact measurement | customizable reports; heatmaps; assessments |
| SIS integration | primary data source (explicit) | real-time SIS integration (explicit) | native education objects + next-gen SIS ambition | SIS/LMS/CRM unified in data lakehouse | SIS link for registrar data (explicit) |
| Scope beyond advising | recruitment + advancement CRM on same platform | transfer/prospective (Explore); registration add-on | full learner lifecycle modules | enrollment through graduate outcomes | tutoring/writing/testing/career/fitness centers on same machinery |
| Customer tier | 850+ institutions, all segments (claim) | R1s, large publics, small privates, CCs, international | large institutions on Salesforce ecosystems | CCs + universities | 2,700+ centers, heavily community colleges |

### What is shared by all five (candidate core)

1. **Student as the central record, with academic context drawn from institutional records.** Every product maintains a student profile whose academic substance (enrollment, program, grades/progress, holds) comes from the SIS or equivalent institutional data — stated explicitly by EAB, TracCloud, Stellic, Civitas; structurally present in Salesforce (education objects, credits earned).
2. **Advising staff as a distinct role serving students through caseloads or service matching.** Advisors (plus faculty and other offices) are the operator role in all five; the relationship is either an assigned caseload (Salesforce "assigned advisors"; EAB care network) or service/reason-based matching (TracCloud counselor matching; Stellic support network).
3. **Scheduled, documented advising interactions attached to the student record.** Appointments/meetings plus notes/documentation exist in all five, tied to the student's profile and visible to the support network.
4. **An intervention loop on academic signals.** All five route signals (faculty progress reports, LMS engagement, predictive flags, self-reports) to staff who must act and track follow-up: EAB Cases & Referrals, Stellic referrals & concerns, Salesforce data-driven alerts, Civitas alert lists + shared notes, TracCloud SAGE.
5. **Student-facing self-service.** All five expose a student portal/app surface (scheduling, to-dos, plans, holds, self-reporting).
6. **SIS integration as the data backbone.** Explicit in all five.

### What varies (candidate variant axes)

- **Center of gravity**: relationship/care network (EAB), planning/audit (Stellic), platform breadth (Salesforce), predictive analytics (Civitas), scheduling machinery (TracCloud).
- **Degree planning depth**: full audit + planner + exceptions (Stellic, Salesforce) vs task-based success plans only (TracCloud) vs plan collaboration (Civitas) vs program exploration (EAB).
- **Analytics depth**: institution-specific predictive models and intervention-effectiveness measurement (Civitas, EAB) vs operational reporting (TracCloud).
- **Scope breadth**: full constituent lifecycle (EAB, Salesforce) vs advising/planning focus (Stellic) vs center operations (TracCloud).
- **Center-type breadth**: same scheduling machinery sold to tutoring/writing/testing/career/fitness centers (TracCloud).
- **Customer tier**: enterprise suites vs single-center deployments.

---

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (minimal)

The Type is recognizable only if all three hold:

1. **Student record with institutional academic context** — the advised person exists as an identified student of the institution, and the record carries academic substance (program/major, enrollment, progress) drawn from institutional records (in practice, integrated from the SIS).
2. **Advisor role and advising relationship** — staff (professional advisors, faculty advisors, success coaches) formally serve students as advisors, through assigned caseloads or service-based matching; the relationship is ongoing, not a single transaction.
3. **Advising interaction record** — advising conversations are scheduled (appointments/meetings) and documented (notes) as records attached to the student, forming a persistent advising history visible to the advising staff.

Tests:
- Remove the academic context (SIS-drawn student substance) → generic appointment scheduling / generic CRM. Not this Type.
- Remove the advisor relationship → a student data warehouse. Not this Type.
- Remove interaction documentation → a directory with a calendar. Not this Type.
- Remove degree planning → still an advising platform (TracCloud demonstrates a real product without degree audit). → L1.
- Remove early alerts → still an advising platform (historical advising schedulers lacked them). → L1.

Historical/market-sample check: a 2000s advising appointment scheduler with SIS-linked student records, advisor schedules, and session notes satisfies all three invariants; a degree-audit-only system (DARS/DegreeWorks era) does NOT satisfy invariants 2–3 and is a different (adjacent) structure — degree audit is a capability that lives inside SISs and advising platforms, not this Type's defining core. The L0 does not overfit to the current "student success CRM" market.

### L1 — Common Mature Structure (very common; not definitional)

- Appointment scheduling machinery: student self-service booking by reason/service type, advisor matching, waitlists/queues, reminders (email/SMS), calendar sync, kiosk check-in, in-person/virtual/phone/asynchronous modalities.
- Advising notes shared across the support network, with summaries; attachments.
- Early alerts and progress reports from faculty; flags and kudos; referral routing to campus offices; follow-up tracking to closure; case-like objects for alerts.
- Academic planning: degree audit against institutional requirements, term-by-term planner, what-if scenarios, program pathways, milestones/non-course requirements, exceptions (waivers/substitutions), transfer-credit evaluation, course-demand reporting.
- To-dos / action plans / success plans assigned to students, with completion tracking and automation.
- Targeted outreach: dynamic student lists (population views), campaigns, templates, two-way messaging (SMS/email), channel-effectiveness feedback.
- Student portal/app: schedule appointments, view plan/progress/audit, to-dos, holds, self-report concerns, resources directory.
- Reporting and analytics: appointment utilization, caseload views, intervention effectiveness; at scale, population-health dashboards and institution-specific predictive models.
- Role-based permissions across offices; multi-office "care network" with shared (visibility-controlled) records.
- Events, surveys, holds center, resource referral directories.

### L2 — Variant / Optional Structure

- Predictive-analytics depth: institution-specific persistence/completion models, nightly rescoring, initiative impact measurement (analytics-first products).
- Degree-audit depth: requirements editors, exception workflows, transfer rules management, catalog-year logic (planning-first products).
- CRM breadth: recruitment-to-alumni constituent lifecycle on the same platform (success-CRM suites).
- AI capabilities: staff assistants (drafting, meeting transcription/summaries, report building), student-facing guidance agents, autonomous agents with autonomy tiers/contact caps.
- Wellbeing/care overlay: pulse checks, wellbeing alerts, care plans, counseling referrals.
- Center-type breadth: the same scheduling/case machinery sold to tutoring, writing, testing, career, and fitness centers.
- Registration integration: plan-to-register hand-off (optional add-on vs native module).
- Population variant: K-12 school counseling (adjacent leaf) — same structure, different population and plan semantics.
- Deployment: standalone SaaS vs module of an SIS/CRM/suite; per-user vs enterprise licensing.

### L3 — Vendor-specific (research notes only)

- EAB Navigate360: Navigate360 branding; Student Success Collaborative; dedicated "Strategic Leader" consultant; Student Journeys; Hand Raise; Holds Center; Study Buddies; Career Match; Forage job-simulation integration; ROI calculator; claims of 850+ institutions / 10M students / 200+ predictive models / 2–12% retention lifts.
- Stellic: Care / Progress / Explore / Registration package names; "audit-aware planner"; Santa Monica College "2,000+ hidden degrees" story; Pathfinders Challenge; stellic.ai sister site.
- Salesforce: Agentforce (advising summaries, student goals guidance); Einstein; education objects as native platform objects; "next-gen SIS" initiative; per-user edition pricing; common capability model across modules.
- Civitas Learning: "Institutional Impact Management" framing; data lakehouse; build-your-own AI agents; 2026 Impact Report; claims of 89% prediction accuracy, 3–11% retention lifts, $4:$1 ROI.
- TracCloud: SAGE early-alert system; SurveyTrac; TracSystems heritage (30+ years); stacked availability; staff work plans; payroll tracking; heatmap generator; kiosk check-in; NIST/HECVAT compliance packaging.

---

## Vendor-specific Findings

See L3. None promoted to the canonical model. The strongest over-generalization risks, checked and rejected:

1. **Degree audit as definitional** — rejected: TracCloud is a real, widely deployed advising platform with no degree audit; Stellic/Salesforce make planning central. Degree planning is L1 with a philosophy gradient (planning-first vs care-first).
2. **Predictive analytics as definitional** — rejected: TracCloud and (in module terms) Salesforce treat analytics as reporting; predictive models are an analytics-first variant.
3. **"Student success CRM" positioning as the definition** — rejected: it describes one market framing (EAB, Salesforce, Civitas), not the structure; TracCloud and Stellic do not use it.
4. **Caseload assignment as the only relationship form** — rejected: TracCloud's service/reason-based matching (students book the right specialist without a standing assignment) is an equally supported relationship form; L0 phrased to cover both.

## Boundary Findings

1. **vs Student Success Platform (§23 sibling) — the primary boundary problem.** Same vendors, often the same product: EAB Navigate360 self-describes as a student-success CRM; Civitas as an impact platform; both would be documented under either leaf. The distinction is center of gravity: the Academic Advising Platform centers the advisor–student relationship and the advising workflow (appointments, notes, plans, alerts routed to advisors); the Student Success Platform centers institutional retention outcomes at scale (predictive analytics, population health, cross-office coordination, initiative measurement) with advising as one workflow inside it. Structural test: remove the advising relationship/interaction core and analytics + cross-office coordination remain (student success); remove the analytics/population layer and the advising workflow remains (this Type). In the current market the two have largely converged into one product category, so this leaf must be written as the advising-workflow core, with analytics as an L1/L2 layer. Flag for joint review when Student Success Platform is processed.
2. **vs Student Information System / SIS (§23 sibling).** The SIS is the institution's system of record (enrollment, grades, transcripts, registration); the advising platform consumes that data — every sampled product states SIS integration as its data backbone (EAB: "main source of data… comes from the institution's SIS"; TracCloud: "maintain… enrollment data from your registrar"; Stellic: "real-time SIS integration"). The advising platform does not become the registrar's record system. Some SISs bundle advising modules (Anthology Student), which is a deployment variant. Test: remove the record-of-record functions → advising platform; remove the advising relationship layer → SIS.
3. **vs Student Case Management (§23 sibling).** Case management is issue-driven: a case is opened for a problem and worked to closure. Advising is relationship-driven: an ongoing advisor–student bond with recurring interactions. Overlap is real and explicit: alert handling inside advising platforms uses case-like objects (EAB "Cases & Referrals"; Civitas "intelligent case management tools"; Salesforce case records with alerts). The case is one object type inside this Type, not its center.
4. **vs School Counseling Management (§23 sibling).** Same structural pattern (counselor–student appointments, notes, plans, alerts) but a different population (K-12), different plan semantics (postsecondary/college-application planning, graduation requirements — not degree audit), and different regulatory context. A gradient, not a wall; vendors differ. Flag for joint review when School Counseling Management is processed.
5. **vs Tutoring Platform (§23 sibling).** Tutoring centers deliver learning support; advising centers guide academic decisions. TracCloud ships both with the same scheduling/case machinery — evidence that the operational core is shared while the service semantics differ. The Tutoring Platform Type centers instruction delivery and tutor matching; this Type centers the academic relationship and plan.
6. **vs Course Registration System (§23 sibling).** Registration is the enrollment transaction; advising platforms collaborate on plans and may hand off to registration (Stellic optional add-on; Salesforce registration management; Civitas "scheduling behavior" signals). Registration remains a separate system of record in all sampled architectures.
7. **Degree audit systems (no dedicated directory leaf).** Degree audit/planning is a capability inside advising platforms (Stellic Progress, Salesforce Intelligent Degree Planning) and inside SISs (DegreeWorks/uAchieve lineage). No leaf conflicts; recorded as an observation supporting the L1 placement.
8. **vs CRM (§07).** EAB and Salesforce position advising inside "education CRM." The constituent population (students), the workflow (advising), and the objects (academic context, plans, alerts) are what this leaf documents; "CRM" is a positioning wrapper, not a competing Type.

## Uncertainties

- **No Tier-1 operational documentation reachable.** EAB and Civitas help centers are behind client login; Stellic support 404; TracCloud wiki 403; Salesforce help articles not located (search engines unusable in this environment; datasheet PDF binary-only). All evidence is Tier-2 product surfaces — detailed about module existence, positioning-level about operational behavior. Consequently the final document makes no precise operational claims (no exact statuses, limits, defaults, approval rules) and uses calibrated wording throughout.
- **Faculty-side workflow depth**: progress-report forms, referral routing rules, and approval semantics are evidenced at feature-name level only (EAB "Faculty Progress Reports"; TracCloud SAGE "mid-term and final faculty reports"); internal behavior unverified.
- **Advisor-assignment mechanics**: caseload assignment vs service matching is confirmed as two existing forms; how products mix them (e.g., primary advisor + network) is not operationally verified.
- **Geographic scope**: sample is North America-centric (Stellic adds Australia/UK institutions as customers). Regional advising structures (UK personal-tutor systems, European study-advising) were not sampled; the L0 is kept implementation-neutral to accommodate them, but their overlays are unverified.
- **Starfish lineage**: the historically defining early-alert product could not be documented (vendor split; docs unreachable). The early-alert pattern is instead evidenced across four sampled products, so the finding stands, but the historical anchor is weaker than ideal.

## Final Synthesis

Academic Advising Platform is institution-operated software for managing academic advising as an ongoing staffed relationship. Its defining structure is small: a student record carrying academic context drawn from institutional records (in practice integrated from the SIS); advisors who formally serve students through assigned caseloads or service-based matching; and scheduled, documented advising interactions (appointments plus notes) attached to the student as a persistent advising history. Around that core, mature products add the machinery that makes advising operational at scale: student self-service scheduling with reason-based routing and waitlists; shared notes across a multi-office support network; early alerts and faculty progress reports with referral routing and follow-up tracking; degree audit and term-by-term planning with what-if exploration (planning-first products make this their center; scheduling-first products may omit it entirely); to-dos and success plans; targeted outreach from dynamic student lists; student portals; and reporting up to institution-specific predictive analytics. The Type's primary boundary tension is with the Student Success Platform — in today's market the same products are sold under both names, the difference being center of gravity (advising workflow vs institutional retention analytics) — and its structural dependencies are the SIS (data backbone, not replaced) and case management (an object type inside the advising loop, not the center).
