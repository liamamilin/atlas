# Research Notes — School Counseling Management

Research date: 2026-09-10
Leaf: School Counseling Management (§23 Education, Research & Knowledge Institutions)
Slug: school-counseling-management

## Research Goal

Understand what software the "School Counseling Management" leaf names, from real products: what the school counseling department's system contains, who operates it, how counseling work flows through it, and where its boundaries sit against the already-processed §23 siblings (Academic Advising Platform, Student Success Platform, Student Case Management, Student Behavior Management, Special Education Management) and against SIS / Parent Portal / Course Registration.

This pass also carries two inherited obligations:

1. **Discharge the academic-advising-platform pass's joint-review flag** (research/academic-advising-platform.md §Boundary Findings #4): "same structural pattern (counselor–student appointments, notes, plans, alerts) with a different population (K-12) and plan semantics (postsecondary/graduation planning, no degree audit) — a gradient, not a wall; flagged for joint review when School Counseling Management is processed."
2. **Answer the forward notes** left by student-behavior-management (counselor caseload/appointments/notes vs conduct events), student-case-management (relationship-driven loop; counselors appear as caseworkers), and student-success-platform (counselor-caseload center vs institution-wide retention operation).

## Initial Boundary

Working hypothesis before research:

- The leaf names the school counseling department's management software — in the current market realized almost entirely as "college & career readiness" (CCR/CCLR) platforms used by school counselors.
- Primary users: school counselors (the operators), with students, parents/guardians, teachers, and administrators as counterparties.
- Nearest neighbors: Academic Advising Platform (same structural pattern, higher-ed population), Student Success Platform (institution-wide retention), Student Case Management (issue-driven casework), Student Behavior Management (conduct events), Special Education Management (regulated plans), SIS (population + academic record of record), Parent Portal (family surface).
- Main unknowns: whether counselor appointment scheduling and counseling notes are definitional or optional; whether college application processing is definitional or a US-market implementation; whether the personal/social (therapeutic) counseling dimension is part of the center; how international (non-US) counseling fits.

## Research Questions

1. What is the organizing relationship — how do counselors relate to students in the system?
2. What is the central managed object per student (plan? file? application?)
3. What counseling interactions are recorded (appointments, notes, journals)? Are they universal?
4. How does college/postsecondary application processing work (documents, deadlines, recommendations, transcripts)?
5. What exploration/assessment machinery feeds the plan (career/interest assessments, content libraries)?
6. What surfaces exist for students, parents, teachers?
7. What reporting/accountability exists (program outcomes, state mandates, district/group roll-ups)?
8. How does the system relate to the SIS (who owns the population and academic record)?
9. What variants exist (K-5 pole, international/multi-country, district/group-of-schools, wellbeing/SEL overlay)?
10. Where exactly is the seam vs Academic Advising Platform — same Type or keep-both?

## Representative Products

Selected for market representation, documentation quality, different product philosophies, and different customer tiers:

| Product | Vendor | Positioning | Tier / segment |
|---|---|---|---|
| Naviance (Naviance CCLR) | PowerSchool | "the leading college, career, and life readiness (CCLR) platform" | Incumbent; large US districts; suite-embedded (PowerSchool ecosystem) |
| SchooLinks | SchooLinks | "all-in-one college and career readiness platform built for K-12 districts" | Modern all-in-one; US districts; counselor-workflow + compliance emphasis |
| Xello | Xello | "college & career readiness software… puts the student at the center of their planning experience" | Student-experience-first; US/state deployments (state-level contracts) |
| Cialfo | Cialfo | "college counselling and application management platform for high schools" | International schools; multi-country application workflows; group-of-schools |
| MaiaLearning | MaiaLearning | "comprehensive, global counseling platform… tools to run a busy counseling office" | Mid-market; US districts + international; counseling-office management depth (office hours, notes) |

Rejected as primary samples: SCOIR, Overgrad, Unifrog, BridgeU (would repeat evidence already saturated across the five); CollegePlannerPro / CounselMore (independent educational consultants — private-practice population, not school-employed counselors; out-of-scope pole, recorded under Boundary Findings); SCUTA (counselor use-of-time accountability niche — not sampled, recorded as uncertainty).

## Sources

Tier 1 (official operational documentation):

- Naviance documentation (PowerSchool docs site): Naviance overview (product structure, editions, core tools vs extended modules) — https://ps.powerschool-docs.com/naviance/latest/naviance-overview ; Journals — https://ps.powerschool-docs.com/naviance/latest/journals (fetched 2026-09-10)
- MaiaLearning official flier hosted by Arkansas Division of Elementary & Secondary Education (vendor-produced): "A Comprehensive, Global Counseling Platform" — https://dese.ade.arkansas.gov/Files/20210104120147_Maialearning_Flier_1.pdf ; earlier Arkansas vendor-fair deck — https://dese.ade.arkansas.gov/Files/20210104120111_MaiaLearning%20AR%20CCR%20Vendor%20Fair%20March%202020.pdf

Tier 2 (official product pages):

- PowerSchool Naviance product pages — https://www.powerschool.com/solutions/naviance , https://www.powerschool.com/naviance-ppc , Naviance brochure/flyer PDFs (go.powerschool.com)
- SchooLinks — https://www.schoolinks.com/ , https://www.schoolinks.com/platform?resource-type=Student%20%26%20Counselor%20Tools , https://www.schoolinks.com/platform/college-application-manager
- Xello — https://www.xello.world/ , http://xello.world/en/features-gallery , http://xello.world/en/middle-and-high-school , official brochure PDFs (xello.world/wp-content)
- Cialfo — https://www.cialfo.co/what-is-cialfo (fetched 2026-09-10) , http://cialfo.co/k12-platform , http://cialfo.co/
- MaiaLearning — https://www.maialearning.com/ , https://www.maialearning.com/schools-districts , https://www.maialearning.com/what-we-do/applying-to-college , https://maialearning.com/states/new-york

Tier 3 (school/district deployments describing the products — used only to corroborate feature existence):

- School/district pages: Pittsburgh Public Schools (Naviance), Hunterdon Central (Naviance), DoDEA (SchooLinks), NCSSM counseling site (SchooLinks), Broward County & St. Johns FL (Xello), Portland Public Schools (MaiaLearning), Orono Schools (MaiaLearning)

Sourcing limitations: SchooLinks, Xello, Cialfo, and MaiaLearning help centers were not reached this pass (evidence is official product pages, official brochures, and one vendor flier hosted on a state education agency site). Naviance documentation was reachable (Tier 1). Consequently: feature existence and positioning are well-evidenced; operational detail (exact statuses, limits, defaults, permission matrices) is NOT asserted anywhere. Vendor scale claims (e.g., "2,500+ colleges", "15,000+ universities", "700+ schools", "10M+ students") are recorded as vendor claims only.

## Product Observations

### Naviance (PowerSchool) — evidence layer A unless noted

Positioning: "the leading college, career, and life readiness (CCLR) platform that enables students to discover their strengths and interests, build critical life readiness skills, create actionable goals and find their best fit path after high school."

Documented product structure (Tier 1 docs):

- **Core tools**: College Planning ("research colleges, compare admissions statistics, track applications, and request transcripts/letters of recommendation"); Career Planning ("explore careers, clusters, and pathways, view wages and job outlooks"); Self-Discovery (assessments: AchieveWorks, Career Interest Profiler, StrengthsExplorer); Success Planning ("actionable goal tracking, task assignments, and to-do lists to keep students on track toward post-secondary goals"); eDocs ("electronic document submission system for sending transcripts, recommendations, and school profiles to higher education institutions"); Alumni Tracker ("track post-secondary outcomes and college enrollment trends"); PowerBuddy (AI assistant).
- **Extended modules (subscription)**: Course Planner ("multi-year course plans aligned with graduation requirements and career pathways"); Curriculum (CCLR digital lessons); Insights Premium (advanced analytics); Test Prep; Career Key (Holland Code assessment).
- **Editions**: District Edition (manage schools, district reports, assign programs/tasks, transfer students between schools, share historical application results across the district, restrict staff access) and School Edition (customize Naviance Student; manage self-discovery, college planning/application management, scholarships, career planning, eDocs).
- **Roles**: staff with teacher job function get a Teacher dashboard/Teacher Desk ("manage letter of recommendation requests"); other staff get the default dashboard with customizable widgets; students get Naviance Student (assessments, college/career searches, planning tools, resume builder); parents/guardians get accounts ("access college, career, and life planning resources and gain insight into their student's post-secondary plans").
- **Journals** (Tier 1): "Use the journal feature to gain insight into students' college, career, and life readiness activities" — with sub-features: set up journals, journals in Naviance Student, track journal entries, add journal entries from Naviance. (Semantics beyond existence + student visibility not asserted.)
- **Other documented features**: RepVisits (college/military rep visits), Document Manager, Email, Surveys, Scholarships, Portfolio, Resume builder, Work-Based Learning, Student Readiness Indicators / Student Readiness Report, Reports, Data Management, Login/Account Management, Naviance for Elementary.
- SIS relationship (product page, layer A): "Naviance integrates with PowerSchool SIS, connecting student academic records, GPA, transcripts, and course history to college and career planning."
- CCLR Framework: six competencies with grade-specific objectives/activities and metrics; curriculum aligned to ASCA Mindsets & Behaviors and CASEL 5 (product pages).
- Counselor value proposition (product pages): "Manage student postsecondary planning in one central location"; "support the student college application process, encourage career exploration and participation, track student progress toward graduation and goals, and report on student outcomes, all within a single platform."
- Not observed in documentation: counselor appointment scheduling; counseling session notes beyond Journals. (Recorded as absence-of-evidence, not evidence of absence.)

### SchooLinks — evidence layer A (official product pages)

Positioning: "an all-in-one college and career readiness platform built for K-12 districts… brings exploration, planning, course planning, work-based learning, compliance tracking, and reporting into a single system."

Counselor-facing features (platform page, feature names + descriptions):

- **Caseload Management** — "Give counselors a clear, actionable view of their students so they can prioritize outreach, monitor progress, and support every learner more efficiently."
- **Counselor Meeting Logs & Notes** — "Keep a running history of student conversations, follow-ups, and interventions in one place so counselors can stay organized and collaborate more effectively."
- **College Application and Transcript Sending** — "Capture every document and transmit them electronically."
- **College Application Manager** (dedicated page): deep Common App integration (real-time status syncing, document matching); document management and workflow automation ("automate transcript requests, letters of recommendation, school reports, and counselor forms"); college list strategy tools (Guaranteed/Likely/Target/Reach categorization, scattergrams from the school's/district's own historical data, comparisons); counselor visibility and reporting (application status, deadlines, missing materials, document fulfillment in real time).
- **College Visit Scheduler** — coordinate college rep visits, campus events, student registrations.
- **Scattergrams**, **Service Hour Tracking**, **Scholarships**, **College Search**, **Course Planning**, **Career Exploration**, **Elementary K-5 CCR**, **Industry Partnerships**, **Alumni Network**, **Rep Visits**, **Transcripts**, **Virtual Reality Campus Tours**.
- AI (marketing claims, layer A for existence): "AI agents that surface who needs attention before you have to ask"; "Alerts flag students with incomplete milestones"; "Nudges recommend next counselor actions"; "Student Insights Agent synthesizes each casefile before a meeting."
- Compliance/state reporting: "configurable compliance framework that adapts to state and district requirements, including graduation requirements and college and career readiness indicators"; "real-time state reporting dashboards… across CCMR, CCRI, CCR, and Seal attainment"; "State-specific PLP templates pre-built and auto-completing."
- Family Engagement portal: "parents to explore their students' pathways, keep track of their progress and communicate with counselors."
- Integrations: SSO, secure data uploads, native SIS integrations (stated generically).
- District-leader framing: "District-wide solution for capturing and automating data to give you a single solution for understanding your district's graduation status."

### Xello — evidence layer A (official pages + official brochure)

Positioning: "College & career readiness software… Xello's award-winning program puts the student at the center of their planning experience. Students document their journey as they build self-knowledge, explore post-secondary options, create plans, and continually reassess."

Student side:

- Self-knowledge: Matchmaker career assessment, Skills Lab, Learning Styles assessment; personalized digital portfolio; goal setting (short/long-term); dashboard feed; built-in lessons (social-emotional competencies + skill-building).
- Exploration: career profiles/interviews, career clusters, college/university profiles ("database of over 3,500 national, state-specific, and local school profiles"), scattergrams, scholarships, test prep integration (Method Test Prep), work-based learning opportunities, volunteer/experience hour tracking, resume builder.
- Planning: **Four-Year Course Planner** ("students build academic plans that align to their postsecondary goals while counselors save time through automated prerequisite validation, specialization tracking, and graduation tracking"; brochure adds "prerequisite checking, graduation tracking, parent or guardian electronic approval, and the ability to export course requests for scheduling in your student information system (SIS)"); **Plans tool** ("teaches students about their pathway options and helps them build an actionable to-do list").
- Applications: "College planning & applications tracking" — students "draft, send, and track requests for letters of recommendation while educators can view requests, send letters, and keep track of their progress"; Application Tracker with important dates; transcript requests; Common App account sync; FAFSA application tracking (California page).

Educator side:

- **Educator tools**: "view student profiles and progress, communicate with students and groups, organize courses and specializations, help students with transcripts, run and view reports" (brochure). Student profiles show "assessment results, saved options, goals & plans, course planner, lesson progress, assignment progress, college applications, portfolios, parents and guardians."
- **Reports**: "Dozens of real-time, ready-made reports… at an aggregate and per-student level"; brochure lists report contents (top career matches, saved options, course planner submissions and alerts, Common App requests and applications, volunteer hours, lesson progress for mandate compliance, college and scholarship applications, alumni tracking with NSC StudentTracker).
- **State Mandate Reporting** — "a customized report gives you a clear view into how Xello's lessons meet each of your state requirements."
- **In-app messaging**, **Surveys** (educator-created, student-completed), demo student accounts, Xello Academy (educator LMS).
- **Family portal**: read-only parent/guardian visibility ("progress on lessons, course selection, and career and college exploration").
- K-12 span: elementary (kindergarten up) through high school; state-level deployments (Florida official provider per district page; California page).

Not observed: counselor appointment scheduling; counselor meeting notes (educator side is profile/report/messaging-centric).

### Cialfo — evidence layer A (official product-definition page, fetched)

Positioning: "Cialfo is the world's leading college counselling and application management platform for high schools. Cialfo helps schools manage career exploration, university research, college applications, recommendation workflows, parent communication, student tasks, and counselling outcomes in one connected system."

Stakeholders (vendor's own framing): school management ("standardise counselling workflows, benchmark outcomes, track university application trends across every school"); counselling team ("Caseloads, deadlines, and letters — managed from one dashboard instead of three"); parents ("See exactly where an application stands, without waiting on an email back"); students ("Research universities, build a college list, and track milestones alongside their counsellor").

Seven documented functions:

1. College & career exploration (strengths, interests, career pathways)
2. University & program discovery (global destinations; "shared starting point for every student conversation")
3. Application management ("applications are tracked and submitted across the destinations and application routes a student chooses" — Direct Apply, UCAS, Common App, partner pathways, country-specific processes)
4. Recommendation workflows ("counsellors can coordinate requests, teachers can write and submit recommendations"; cDocs document system: "compile, track, and send application documents from one centralised portal"; bulk drag-and-drop uploads)
5. Parent & student communication
6. **Caseload management** ("counsellors can view students, deadlines, college lists, documents, recommendations, applications, and progress in one place… prioritise where attention is needed")
7. Group schools reporting ("counselling activity, application trends, and outcomes across one school or an entire group of schools")

Journey structure: Discover → Plan → Apply → Arrive → Measure (Arrive = visas, orientation, pre-departure; Measure = outcomes across cohort/school/group).

Adjacent vendor offerings (kept out of the Type): Direct Apply (application submission tool, 1,200+ partner universities), Saige (AI layer: university discovery, LOR drafting support, UCAS application review), Cialfo Guides (outsourced counseling capacity — "internationally trained counsellors available through Cialfo"), Comet (student services marketplace — explicitly "separate from the core counselling platform").

Compliance: GDPR, FERPA, PIPL; SSO & role-based permissions; student consent controls.

Not observed: counselor appointment scheduling; counselor meeting notes; US state-mandate reporting; wellbeing/SEL machinery.

### MaiaLearning — evidence layer A (official pages + official flier on state agency site)

Positioning: "MaiaLearning provides counselors with the comprehensive tools they need to run a busy counseling office." LinkedIn self-description: "School Counseling Platform" among specialties.

Counseling-office management (flier, "Student Management"):

- **Office hours**: "Counselors can define office hours which students and parents can book and add automatically to calendars."
- **Meeting notes**: "Counselors can keep notes on student meetings and optionally share them with other counselors, students, and families."
- Calendar items and communication with students and families.

Planning objects:

- **Career Plans** ("Automatic Career Plans help students define their paths"; assessments evaluate "interests, personality, work values, and social/emotional skills")
- **Academic Plans** ("supports course planning, and shows grades and progress toward graduation"; built around the school's course catalog)
- **College Plans** (college research over "over 18,000 universities and vocational schools in 145 countries"; applications and results tracking; scattergrams; scholarships)

Applications: Common App and Parchment integrations; "bulk sending of recommendations, transcripts and documents"; dashboards to "follow-up with students, teachers, or colleges on missing or incomplete documents"; essay tools (student topics/outline/draft; counselor annotated feedback); AI letter writer (considers the brag sheet).

Wellbeing (distinctive): "daily 30-second student check-ins and a Flourishing at School survey, so counselors are alerted to the students who need intervention now. Counselors can monitor wellbeing at an individual, a grade, or a whole school level."

Events: MaiaVisits — "Schedule and track college visits, fairs, and events… colleges can also schedule their own visits in available time slots, subject to counselor approval."

Curriculum: 69 CCR lessons grades 6–12 "mapped to ASCA and CASEL"; 39 SEL units; Pathfinders K-5 career exploration.

Reporting: "Counselors and administrators at school and district levels track college and career readiness with real-time executive summaries and detailed reports. Reports generate dynamic groups for easy messaging."

Data: "Automatic SIS Data Transfer – SFTP" (Infinite Campus named); FERPA & GDPR compliant.

Geography: "70+ countries using MaiaLearning"; state-specific pages (New York: Career Plans, CDOS standards, Multiple Pathways).

## Cross-product Comparison

| Structure | Naviance | SchooLinks | Xello | Cialfo | MaiaLearning |
|---|---|---|---|---|---|
| Counselor caseload / student lists | ✓ (counselor dashboards; district/school editions; staff accounts) | ✓ (Caseload Management) | ✓ (educator tools over the student population) | ✓ (caseload management) | ✓ (counselor student lists) |
| Per-student postsecondary plan | ✓ (Success Planning goals/tasks/to-dos; Course Planner module) | ✓ (course plans, graduation plans, goals) | ✓ (Plans tool, goals, four-year course planner) | ✓ (Plan stage: timelines, requirements, goals) | ✓ (Career + Academic + College Plans) |
| Application/document processing | ✓ (eDocs; track applications; request transcripts/LORs) | ✓ (College Application Manager; transcript sending) | ✓ (LOR workflow; application tracker; transcript requests; Common App sync) | ✓ (application management; cDocs; recommendation workflows) | ✓ (Common App/Parchment; bulk recommendations/transcripts) |
| Career/interest assessments | ✓ (Self-Discovery suite; Career Key module) | ✓ | ✓ (Matchmaker, Skills Lab, Learning Styles) | ✓ (strengths/interests exploration) | ✓ (interests, personality, values, aptitudes, wellbeing) |
| College/career content libraries | ✓ (SuperMatch; career clusters/pathways; Roadtrip Nation) | ✓ | ✓ (school profiles; career profiles) | ✓ (global university database) | ✓ (18k institutions, 145 countries) |
| Counselor notes / journals | ✓ (Journals) | ✓ (Meeting Logs & Notes) | — not evidenced | — not evidenced | ✓ (meeting notes, shareable) |
| Counselor appointment / office-hours booking | — not in docs | — not evidenced (meeting logs only) | — not evidenced | — not evidenced | ✓ (office hours bookable by students/parents) |
| Early alerts / flags | ~ (Student Readiness Indicators) | ✓ (AI alerts on incomplete milestones; nudges) | — | — | ✓ (wellbeing alerts) |
| Parent/family access | ✓ (parent accounts) | ✓ (Family Engagement portal) | ✓ (read-only family portal) | ✓ (parents see application status) | ✓ (parents book/communicate) |
| Reporting / outcomes | ✓ (Reports; Insights Premium; Alumni Tracker) | ✓ (state reporting dashboards) | ✓ (ready-made reports; state mandate reporting) | ✓ (group-schools reporting; outcomes) | ✓ (engagement/progress reports; dynamic groups) |
| Curriculum / lessons | ✓ (Curriculum module; CCLR Live) | ✓ (self-guided curriculum) | ✓ (built-in lessons) | — | ✓ (69 CCR + 39 SEL lessons; K-5 Pathfinders) |
| College rep visits | ✓ (RepVisits) | ✓ (College Visit Scheduler) | — | — | ✓ (MaiaVisits, counselor approval) |
| Scholarships | ✓ | ✓ | ✓ | — | ✓ |
| Work-based learning / CTE | ✓ | ✓ (WBL, CTE, industry partnerships) | ✓ | — | ✓ |
| SIS integration | ✓ (PowerSchool SIS: records, GPA, transcripts, course history) | ✓ (native SIS integrations) | ✓ (course-request export to SIS) | — not evidenced on page | ✓ (SFTP transfer; Infinite Campus) |
| AI assistant | ✓ (PowerBuddy) | ✓ (alerts/nudges/Insights Agent) | — | ✓ (Saige) | ✓ (Maia AI; AI letter writer) |
| Multi-country applications | — (US-centric) | — | — | ✓ (UCAS/Common App/Direct Apply; group schools) | ✓ (145 countries) |
| District / group-of-schools layer | ✓ (District Edition) | ✓ (district dashboards) | ✓ (district reports) | ✓ (group schools) | ✓ (district reports) |
| Wellbeing / SEL overlay | ✓ (life-readiness/SEL lessons) | ~ (mindset assessments) | ✓ (SEL lessons) | — | ✓ (wellbeing check-ins + alerts) |

Reading of the table (evidence layer B for the cross-product rows):

- Universal (5/5): counselor caseload organization; per-student postsecondary plan; application/document processing; career/interest assessments; college/career content; parent/family visibility; reporting/outcomes.
- Near-universal (4/5): counselor–student communication; scholarships; district/group layer.
- Strong minority (3/5): counselor notes/journals (Naviance, SchooLinks, MaiaLearning); curriculum/lessons; college rep visits; work-based learning.
- Minority (≤2/5): counselor appointment/office-hours booking (MaiaLearning only, clearly); early alerts (SchooLinks, MaiaLearning, ~Naviance); wellbeing machinery (MaiaLearning deepest); multi-country application routes (Cialfo, MaiaLearning); AI assistants (era-current, 4/5 but recent).

## Canonical Model

### L0 — Defining Invariant

School Counseling Management is the school counseling department's system for managing its counseling program over the school's enrolled students. Three jointly-held structures:

1. **The counselor caseload.** The school's enrolled students are organized under responsible counselors; the counselor–student assignment is the organizing relationship of the system (assignment mechanics vary — alphabetical, grade-level, cohort, program-based). The counselor works their caseload from dashboards/lists that surface each student's plan progress, deadlines, and needed attention. Remove → a caseload roster (SIS slice) or a generic CRM.

2. **The student's postsecondary plan.** The central managed object per student: an evolving, multi-year plan carrying course selections against graduation requirements, career direction (from exploration and assessments), and postsecondary goals with to-dos — built by the student, guided and tracked by the counselor across years. Remove → a student exploration app or a document tracker with no guidance substance.

3. **The counseling program's operational loop.** The office's guided workflow around the plan: application and document processing (transcripts, recommendations, school forms, deadlines, submission and outcome tracking), communication with students and families, and progress/outcome reporting up to school/district/group level. Remove → planning content with no operational workload, or a transcript service with no counseling program.

Binding: the school's own counseling program (K-12, centered on the middle/high-school postsecondary transition) operated by school-employed counseling staff over enrolled students. Remove the school binding → independent-consultant practice tools (different population/relationship); remove the counseling-program binding → SIS or generic student-success tooling.

Joint load-bearing: 1 alone = caseload roster; 2 alone = student planning/exploration tool; 3 alone = application document service; 1+2 without 3 = planning tool with rosters (the K-5 pole — in-type only as a grade variant of products that carry 3 elsewhere); 1+3 without 2 = document tracker with rosters; 2+3 without 1 = counselor-less self-service planning/application tool (direct-to-consumer shape, not school counseling management).

### L1 — Common Mature Structure

- Career/interest/self-knowledge assessments feeding the plan (interest inventories, personality, learning styles, strengths)
- College and career content libraries (institution profiles, admission statistics, career profiles/clusters/pathways, wage/outlook data)
- College application tracking with deadline and requirement visibility; scattergrams from the school's own historical results
- Document transmission networks/integrations (electronic transcript/recommendation sending; Common App-class integrations)
- Recommendation-letter workflows (student request → teacher writes → counselor sends)
- Parent/guardian accounts with visibility into plans and progress
- Counselor–student (and family) messaging/communication
- Reporting: engagement/progress/outcome reports at counselor, school, and district/group grain
- Counselor notes/journals on students (3/5 sampled; strong minority)
- Scholarships; college rep visit management; resume builders; alumni/outcome tracking
- District/group-of-schools management layer (editions, cross-school reporting, workflow standardization)
- SIS integration as the data backbone (population, demographics, academic records, transcripts, GPA, course history)

### L2 — Variant / Optional Structure

- Counselor appointment/office-hours scheduling with student/parent self-booking (clearly present in one sampled product; not universal)
- Early-warning/alert machinery (incomplete milestones, wellbeing alerts, readiness indicators)
- Wellbeing/SEL overlay (check-ins, flourishing surveys, SEL curricula)
- Curriculum/lessons (CCLR/SEL lesson libraries mapped to ASCA/CASEL; grade-banded)
- K-5 elementary pole (play-based career awareness; grade variant of the same products)
- US state-compliance machinery (state CCR indicators, graduation plans/PLPs, mandate reporting) — regional variant
- Multi-country application routes (UCAS, country-specific systems, direct-application networks) — international-school variant
- Work-based learning / CTE program management, industry partnerships, service-hour tracking
- Test prep, essay tools, financial-aid/scholarship depth
- AI assistants (student guidance, counselor prioritization, letter drafting) — era-current
- Deployment: standalone SaaS vs suite module (PowerSchool ecosystem); district vs school vs group-of-schools licensing

### L3 — Vendor-specific (research notes only)

- Naviance: CCLR Framework (six competencies); SuperMatch; RepVisits; eDocs; Alumni Tracker; PowerBuddy; Success Planner 2.0; District/School Edition split; Insights Premium; Gallup StrengthsExplorer / AchieveWorks / Career Key assessment portfolio; Kaplan CCLR Live; claims of 10M+ students.
- SchooLinks: Student Insights Agent; nudges; CCMR/CCRI/CCR/Seal state dashboards; VR campus tours; industry-partnership network; "Guaranteed/Likely/Target/Reach" list categorization.
- Xello: Matchmaker; Skills Lab; Plans tool; Xello Academy; demo student accounts; Method Test Prep integration; NSC StudentTracker alumni tracking; state-level contracts (Florida official provider per district page).
- Cialfo: Direct Apply (1,200+ partner universities; fee waivers; 48-hour offer claims); Saige AI; cDocs; Cialfo Guides (outsourced counselors); Comet (student-services marketplace, explicitly separate); group-schools benchmarking; claims of 700+ schools / 105+ countries / 1M+ students.
- MaiaLearning: MaiaVisits; Pathfinders K-5; Flourishing at School survey; daily 30-second check-ins; AI letter writer; NY CDOS/Multiple Pathways packaging; claims of 18,000 institutions / 145 countries / 70+ countries.

## Vendor-specific Findings

See L3. None promoted to the canonical model. Over-generalization risks checked and rejected:

1. **College application processing as US-only furniture** — rejected as a definitional exclusion: it is 5/5 in the sample including the two international-facing products (Cialfo multi-country; MaiaLearning 145 countries). It is part of the operational loop, with route variety (UCAS/Common App/direct networks) as the variant axis.
2. **Appointment scheduling as definitional** — rejected: only one sampled product documents student/parent bookable office hours; the advising pass's "appointments" pattern is NOT universal here. Notes/journals are the better-evidenced interaction record (3/5), and even those are a strong minority, not the center.
3. **"College & career readiness" marketing framing as the definition** — the market label describes the student-facing content layer; the Type's management substance (caseloads, plans, operational loop, reporting) is what the leaf documents. Products self-describe variously as CCLR platform, counseling platform, "run a busy counseling office" — the shared structure is stable across all framings.
4. **Wellbeing/SEL as definitional** — rejected: absent from Cialfo; present as overlay/lessons elsewhere; deepest in one product. Variant overlay.
5. **State-compliance machinery as definitional** — rejected: US-regional variant (Cialfo's international market has none).
6. **Caseload assignment as the only relationship form** — partially checked: all five sampled products organize counselors over student populations; formal "advisor of record" semantics were not operationally verified (help centers unreached). L0 phrased as "counselors responsible for defined groups of students" to tolerate assignment-mechanism variety.

## Boundary Findings

1. **vs Academic Advising Platform (§23) — JOINT REVIEW DISCHARGED from this side: keep-both RATIFIED.** The advising pass's flag said "same structural pattern… a gradient, not a wall." This pass confirms the gradient and ratifies the split on a center-of-gravity + population + plan-semantics seam:
   - **Population/operator**: K-12 school counseling department (school-employed counselors; minors; parents as first-class counterparties) vs higher-ed advising (professional/faculty advisors; adult students; family marginal).
   - **Plan semantics**: postsecondary plan (course plans against graduation requirements, career direction, college/postsecondary goals, application lists) vs degree audit and term-by-term academic planning against institutional requirements. Graduation-requirement tracking here is simpler than degree audit; there is no degree-audit machinery in any sampled product.
   - **Operational loop**: the counseling loop is dominated by application/document processing (transcripts, recommendations, deadlines, outcome recording) and family communication — workflows with no analog in the advising sample; conversely, registration hand-off and degree-audit exception workflows (advising) have no analog here.
   - **Interaction record**: advising centers scheduled, documented advising interactions (appointments + notes are its L0); here appointments are a minority feature and the interaction record (notes/journals) is a strong minority — the plan and the application workflow carry the continuity instead.
   - Removal tests both ways: strip the application/document machinery and family layer, re-point the plan at degree requirements and the population at enrolled adults → an advising platform; strip degree audit and registration hand-off, re-point at postsecondary transition with parents and application documents → school counseling management. Both leaves stand; the seam is documented in both final documents.
2. **vs Student Success Platform (§23)** — confirms that pass's forward note: the sampled counseling products center the counselor's caseload and per-student postsecondary plan, not an institution-wide retention operation. Predictive/priority machinery appears only as add-ons (Naviance Insights Premium module; SchooLinks AI nudges at caseload grain). K-12 "early warning" systems remain Student Success territory when they carry the four-leg retention operation; counseling platforms consume readiness indicators rather than operating retention campaigns. Seam held.
3. **vs Student Case Management (§23)** — confirms that pass's flag: relationship-driven counseling (ongoing counselor–student bond around a plan) vs issue-driven casework (a case opened for a problem, worked to closure). Counselors appear as caseworkers inside case systems (role overlap, object separation); a counseling concern may become a case, but the case is not this Type's unit of record. Seam held.
4. **vs Student Behavior Management (§23)** — confirms that pass's flag: conduct events and the school-wide response loop vs the counseling relationship and plan. Counselors consume behavior data (referrals may route to counselors); the counseling record is plan + interaction + application workflow, not the conduct event loop. Seam held.
5. **vs Special Education Management (§23)** — counselors may coordinate accommodations (e.g., 504-style plans in the US), but the regulated machinery (eligibility gate, mandated individualized plans, jurisdiction timelines) is special-ed territory; counseling plans are guidance artifacts, not legally mandated instruments. Seam held.
6. **vs Student Information System / SIS (§23)** — the SIS owns the population and the academic record (enrollment, grades, GPA, transcripts, course history); every sampled product that states a data relationship consumes the SIS as its backbone (Naviance–PowerSchool SIS; MaiaLearning SFTP transfer; Xello course-request export; SchooLinks native integrations). The counseling platform plans against graduation requirements but does not become the record system. Course plans export to scheduling; registration stays in the SIS/Course Registration System. Seam held.
7. **vs Parent Portal (§23)** — family visibility is a capability surface of this Type (5/5 sampled), not a competing Type; the parent portal leaf covers the general family-facing surface.
8. **vs independent educational-consultant tools (no directory leaf)** — CollegePlannerPro/CounselMore-class products serve private-practice consultants over client families, not school-employed counselors over enrolled students. The school binding breaks; out of scope for this leaf. Recorded as an out-of-scope pole, not sampled.
9. **vs therapeutic/mental-health counseling records (no directory leaf)** — the sampled Type's center of gravity is postsecondary/college-career counseling. Products that centered confidential therapeutic session documentation would sit adjacent to Student Case Management / health-record territory; wellbeing check-ins here are an overlay (L2), not the record center. Recorded as a scope note.
10. **vs college-application networks (Common App, Parchment, UCAS; no directory leaves)** — receiving-side networks that counseling platforms integrate with; capability slice, no conflict.
11. **vs Tutoring Platform / Assessment Platform (§23)** — signal sources and service destinations inside the counseling loop, not competitors; no overlap observed in the sample.

## Uncertainties

- **Help centers unreached for 4/5 products** (SchooLinks, Xello, Cialfo, MaiaLearning). Evidence is official product pages, official brochures, and one vendor flier hosted on a state education agency site; Naviance documentation is the only Tier-1 docs site reached. Feature existence and positioning are well-evidenced; operational behavior (statuses, limits, defaults, permission semantics, note-visibility rules) is deliberately not asserted.
- **Counselor assignment mechanics** (how caseloads are built and maintained; whether students can be re-assigned mid-year) not operationally verified in any product.
- **Note visibility semantics** (who sees counselor notes — other counselors, teachers, students, parents — and under what controls) evidenced only as "optionally share" (MaiaLearning) and feature existence (Naviance Journals, SchooLinks Meeting Logs); confidentiality configuration unverified. This matters because counseling notes can be sensitive; the final document speaks only in calibrated terms.
- **Appointment scheduling breadth** — MaiaLearning's office-hours booking is documented; whether other sampled products offer it in some form is unknown (absence of evidence in marketing/docs surfaces, not proof of absence).
- **Non-US regional counseling structures** — UK/form-tutor systems, EU guidance structures, and other regional counseling models were not sampled beyond Cialfo's international-school market and MaiaLearning's country count; the L0 is kept implementation-neutral, but regional overlays are unverified.
- **Independent-consultant pole** (CollegePlannerPro/CounselMore) and **use-of-time accountability niche** (SCUTA) not sampled; recorded as out-of-scope pole and uncertainty respectively.
- **Vendor scale claims** (institution counts, university database sizes, student counts) recorded as claims only; not repeated in the final document.

## Historical / Market-Sample Check

Paper-era school counseling office (pre-software): a counselor with a caseload list (alphabet/grade assignment), student folders carrying course-selection sheets and four-year plans, career-interest inventories, college files with transcripts and recommendation letters prepared and mailed, an appointment calendar, parent letters, and outcome tallies reported to the principal. This satisfies all three L0 structures (caseload; per-student plan; operational loop with documents, communication, reporting) with none of the modern furniture (no assessments library, no AI, no state dashboards, no parent portal). Older and regional forms (UK careers/destinations guidance; international-school counseling; mid-20th-century US vocational guidance) fit the same abstraction. The L0 therefore survives the historical check; the market label "college & career readiness" is the current dominant implementation framing, not the definition.

## Final Synthesis

School Counseling Management is the school counseling department's system for managing its counseling program over the school's enrolled students. Its defining structure is small: counselors responsible for defined groups of students (caseloads); a per-student postsecondary plan — course plan against graduation requirements, career direction, postsecondary goals — that counselors guide and track across years; and the counseling program's operational loop around that plan — application and document processing (transcripts, recommendations, deadlines, outcomes), communication with students and families, and progress/outcome reporting. Around that core, mature products add the machinery that makes the program run: career/interest assessments and college/career content libraries that feed the plan; application tracking with the school's own historical admission data; recommendation-letter workflows and electronic document sending; parent/guardian visibility; counselor notes; scholarships, rep visits, resume builders, alumni tracking; district/group reporting layers; and SIS integration as the data backbone. Variant structure depends on segment and geography: appointment booking, early alerts, wellbeing/SEL overlays, lesson curricula, K-5 poles, US state-compliance machinery, multi-country application routes, work-based learning, and AI assistants. The Type's most important boundary is with the Academic Advising Platform — same structural pattern, different population (K-12 vs higher-ed), different plan semantics (postsecondary/graduation vs degree audit), different operational loop (application documents and family communication vs registration and degree-audit exceptions) — keep-both ratified. The SIS remains the population and academic record of record; behavior, case, and special-education systems own their respective loops, with counselors consuming their data rather than owning it.
