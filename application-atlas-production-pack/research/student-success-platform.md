# Research Notes — Student Success Platform

Date: 2026-09-09
Slug: student-success-platform
Directory leaf: Student Success Platform (§23 Education, Research & Knowledge Institutions)

## Research Goal

Understand what a Student Success Platform actually is as an Application Type: what objects exist inside it, who uses it, how the work flows from signal to intervention to outcome, and where its boundary sits against neighboring §23 leaves (academic advising platform, SIS, student case management, student services portal, enrollment management) and against the name-collision leaf Customer Success Platform (§07).

## Pre-hung Duties (from STATUS.md Boundary Issues)

1. **academic-advising-platform vs student-success-platform (JOINT REVIEW REQUIRED)** — that pass recorded: "the market largely sells one converged category under both names — EAB Navigate360 self-describes as a student-success CRM and Civitas as an impact platform… the working distinction is center of gravity (advisor–student relationship + advising workflow vs institutional retention analytics/population health/initiative measurement), with a structural test (remove the analytics layer → advising platform remains; remove the advising core → analytics + coordination remain)". **This pass must discharge the flag from the student-success side.**
2. Sibling passes already ratified seams toward this leaf's neighborhood: student-information-system-sis (official record), student-case-management (issue-driven casework), student-services-portal (student-facing front door), student-behavior-management (K-12 conduct loop, flagged school-counseling-management as unprocessed sibling).

## Initial Boundary

Hypothesis before research:

- Core use: help a higher-education institution retain and graduate its students by (a) seeing the whole enrolled population's health, (b) catching students who drift off-track early, (c) coordinating staff intervention, (d) measuring what works.
- Likely users: advisors/success coaches, faculty, student-affairs staff, retention leadership.
- Nearest confusions: Academic Advising Platform (relationship-centered), Student Case Management (case-centered), SIS (record-centered), LMS (course-centered), Customer Success Platform (B2B SaaS, same words).
- Unknowns: whether outcome measurement is definitional or common; whether predictive analytics is definitional (almost certainly not); how strong the enrollment/recruitment overlap is.

## Research Questions

1. What is the unit of record, and how are individual students and populations (cohorts) handled?
2. How do "success signals" originate (faculty early alerts, progress reports, rules, predictive models, engagement data) and how are they routed?
3. What does the intervention loop look like (care teams, caseloads, appointments, tasks, notes, referrals, campaigns)?
4. How are outcomes measured (retention/persistence dashboards, initiative/intervention effectiveness)?
5. What data substrate is presupposed (SIS, LMS, CRM) and what does the platform NOT own?
6. Who are the users and what is the staff role model?
7. Where is the boundary against advising platforms, case management, SIS, portals, enrollment management?

## Representative Products

Selection rationale: market dominance + different product philosophies + different customer levels + documentation available.

| Product | Vendor | Angle | Segment |
|---|---|---|---|
| Navigate360 | EAB | dominant incumbent; self-labels "higher education CRM"; coordinated-care + consulting posture | 850+ two-year and four-year institutions, systems, HBCUs |
| Student Impact Platform | Civitas Learning | analytics/impact-first specialist; "Institutional Impact Platform" | community colleges + universities |
| Student Success & Engagement (SS&E) | Watermark | advising/care-coordination specialist (Aviso heritage); predictive persistence | community colleges, small/private colleges |
| Education Cloud — Student Success module | Salesforce | CRM-platform pole; Student Success one module of a journey-wide suite | large universities, systems |

## Sources

All fetched 2026-09-09.

- EAB — Navigate360 product page: https://www.eab.com/products/navigate (Tier-2 official product surface; includes feature lists, FAQ with data-model statements)
- Civitas Learning — Student Impact Platform overview: https://www.civitaslearning.com/platform/ (Tier-2)
- Civitas Learning — Coordinate Student Care use-case page: https://www.civitaslearning.com/coordinate-student-care/ (Tier-2)
- Watermark — Student Success & Engagement solution page: https://www.watermarkinsights.com/solutions/student-success (Tier-2; includes FAQ with explicit SIS-contrast statement)
- Watermark — Help Center root: https://support.watermarkinsights.com/hc/en-us (Tier-1 surface reachable; "Student Success & Engagement (SSE)" category confirmed to exist; individual articles not fetched)
- Salesforce — Education Cloud overview (Agentforce Education): https://www.salesforce.com/education-cloud/ (Tier-2; Student Success module feature set)
- Salesforce — "What is student success?" definitional article: https://www.salesforce.com/education/student-success-software/what-is-student-success/ (Tier-2 vendor definitional content; market vocabulary: leading/lagging indicators, Tinto framing)

Failed/degraded (network-restricted; 1–2 attempts per source then abandoned):

- https://www.watermarkinsights.com/products/student-success-engagement/ — 404; substituted by /solutions/student-success (success on 2nd attempt)
- https://www.salesforce.com/education-cloud/overview/ — 404; substituted by /education-cloud/ (success on 2nd attempt)
- Watermark help-center article (Early Alerts Overview, guessed URL) — 404; help-center root fetched instead. Consequence: Watermark's operational detail (alert workflow specifics) rests on product-page strength only.
- No EAB or Civitas help-center/knowledge-base articles fetched; no Salesforce help.salesforce.com documentation fetched.

**Evidence posture:** all four products evidenced at official-product-page strength (Layer A direct for feature existence and self-description); no Tier-1 operational walkthroughs (click-path-level help articles) fetched. Therefore the final document asserts structures (objects, loops, roles) but avoids precise numeric limits, exact workflow states, and default settings.

## Product Observations

### EAB Navigate360 (Layer A unless noted)

- Self-description: "the leading higher education CRM… so much more than a CRM"; positions itself under "Student Success and Retention" focus area. Marketing outcome claims (retention +2–12%, graduation +3–15%) are vendor claims, not structural evidence.
- Staff workflow features listed: Complete Student Profile; **Coordinated Care Network**; Cases & Referrals; Automated Alerts & Messaging; Two-Way SMS; Campaigns & Template Library; To-Dos; Appointments & Surveys; Events; Notes & Attachments; **Faculty Progress Reports**.
- Reporting/analytics listed: AI-Powered Report Builder; Advanced Query Builder; Data Visualizer; Templated & Scheduled Reports; Automated Workflow from Reports; **Population Health Analytics**; Activity Analytics; **Intervention Effectiveness Analytics**; Historical Analytics; Predictive Model (vendor states 200+ custom predictive models deployed); Analytics Data Exports.
- Data model statement (FAQ): "The main source of data used to populate Navigate360 comes from the institution's student information system (SIS)"; LMS data optional; custom data sets (financial aid, housing); system-agnostic integrations (Ellucian, Jenzabar, PeopleSoft, Workday Student, Blackboard, Canvas, Moodle, Brightspace); APIs + bulk export outward.
- Users (FAQ): "Current students, prospective students, faculty, staff, and administrators all use Navigate360 as part of a Coordinated Care Network. Staff users often include but are not limited to advising, enrollment, career services, and tutoring."
- Student side: self-service mobile app/desktop (appointment scheduling, resources, To-Dos, Student Journeys); "Student Hand Raise" self-reporting concern feature.
- Scope breadth: Enrollment CRM module (recruitment), Student Engagement Hub, Advancement CRM module — the success core is embedded in a journey-wide suite.
- Licensing: enterprise license covering all staff/students (no per-user fees); cloud SaaS.

### Civitas Learning Student Impact Platform (Layer A unless noted)

- Self-description: "A single platform that brings together advanced predictive analytics, AI assistance and workflows to power smarter decisions, timely support, and better outcomes"; brand framing "Unify Data. Connect Systems. Surface Insights. Enable Action."
- Persona-split feature sets (first-class on the page):
  - Leaders: Student Outcome Analytics; Predictive Factors of Success; **Initiative Analytics**; Course Insights; Course Demand Analytics.
  - Student-facing staff: Student Success Analytics; **Unified Student Profile**; Shared Notes; **Academic Alerts**; SMS & Email.
  - Students: Collaborative Degree Planning; Smart Class Schedule Builder; Appointment Calendaring; Asynchronous Guidance.
- Data pipeline ("Civ Data Pipeline"): SIS, LMS, CRM, event & activity data → unified foundation. Integration logos include competing success platforms (Navigate360, Anthology, Salesforce) — the platform is data-hungry across systems.
- Coordinate Student Care use-case page: "Provide a shared view of student information, track outreach, share notes, raise alerts, and coordinate student care across leaders, advisors, faculty, and student service teams"; "Coordinate proactive engagement efforts across teams to avoid redundant services & scale holistic support."
- Measurement emphasis: "understand the impact of initiatives, courses, programs, and policies on specific student segments… increase initiative ROI"; "Insight into multiple student outcomes, not just GPA/retention metrics" (explicit differentiation claim).
- Service model: dedicated strategic partnership/customer success team alongside software.

### Watermark Student Success & Engagement (Layer A unless noted)

- Self-description: "helps institutions **identify students who need support, coordinate interventions, and improve retention and completion outcomes**" — the tightest one-sentence job statement in the sample.
- Features: advanced/intuitive reporting (custom dashboards without IT); **Early alerts** ("faculty and staff raise alerts… predictive models for persistence and course completion"); guided pathways/success plans monitored with notifications when goals change; **caseload management** ("Predictive analytics help you prioritize which students to contact first"); SIS+LMS integrations (Ellucian, Jenzabar, Blackboard, Canvas, D2L, Moodle) "remove the risk of duplicate data"; student mobile app (connect with support team, appointments, tasks, resources); **cohort workflow stages** ("Manage milestones and track student cohorts through your defined stages for processes like re-enrolling. View stage conversion rates and use automation"); "Demonstrate impact to accreditors… connect your student success initiatives to your institution's mission. Report results against standards."
- FAQ (boundary evidence, Layer A):
  - vs SIS: "While an SIS provider's success tool focuses heavily on degree progression and academic records, Watermark Student Success & Engagement operates as a **proactive extension of your care team** by combining both SIS and LMS data into a single, centralized view… Maintaining Watermark ensures your campus keeps the advanced, specialized capabilities required to track and improve **true student persistence**."
  - Users: "advisors, faculty, student affairs professionals, retention teams, success coaches, and institutional leaders responsible for supporting student achievement and persistence."
  - Early intervention: "faculty and staff raise alerts, track concerns, assign follow-up actions, and monitor intervention outcomes using predictive modeling."
  - Advising support: appointments, documented interactions, progress toward goals — advising is one supported workflow, not the whole product.
- Segment evidence: community colleges prominent in case studies (Amarillo College, HCC); part of Watermark's Educational Impact Suite (assessment/accreditation-adjacent suite).

### Salesforce Education Cloud — Student Success module (Layer A unless noted)

- Self-description: "Education Cloud… includes CRM for higher Education and next-gen student information system (SIS) capabilities"; modules for each journey stage: Recruitment and Admissions, Academic Operations, **Student Success**, Student Financials, Advancement and Alumni Relations. Student Success is one module among five — the suite pole.
- Student Success module features: Agentforce advising support & student goals guidance; Personalized Learner Support (streamlined appointment scheduling; "customizable care and action plans"; tailored portal); Holistic Advising Experiences ("activating student data–academic, wellbeing, LMS engagement, and more. Get the early indicators required to identify students in need and quickly intervene with **data-driven alerts**"); Wellbeing and Career Readiness (pulse checks).
- Definitional article ("What is student success?"): "Student success is defined as how well students navigate their higher education experience and progress toward graduation." Introduces the market's dominant measurement frame: **lagging indicators** (term GPA, courses completed, withdrawals) vs **leading indicators** (in-course performance, course absences, engagement with advisors/career services, transcript requests, unpaid balances) that "allow institutions to respond to student problems as they're happening." Explicit loop statement: "faculty can raise timely alerts to advisors when students are struggling." Closing statement: "The right student success software will help manage and track a student's entire higher education journey in one central place, while making it easy to take action on insight."
- Pricing: per-user/month editions — a different commercial model from EAB's enterprise license (variant, not structural).
- Common capabilities model (FAQ): scheduling, case management, form-building as shared platform primitives reused across modules.

## Cross-product Comparison

| Structure | Navigate360 | Civitas | Watermark SS&E | Salesforce SS module | Verdict |
|---|---|---|---|---|---|
| Enrolled-student population as addressable records w/ success context | Complete Student Profile (SIS-fed) | Unified Student Profile | SIS+LMS centralized view | 360-degree student view | **All 4 — core** |
| Individual + population/cohort grain | Population Health Analytics; queries drive workflows | leader-level Student Outcome Analytics | cohort workflow stages; institutional metrics | dashboards; "at scale" | **All 4 — core** |
| Proactive signals raised w/o student request | Automated Alerts; Faculty Progress Reports; Predictive Model | Academic Alerts; institution-specific predictive models | Early alerts; persistence/course-completion prediction | data-driven alerts; early/leading indicators | **All 4 — core** |
| Signal → tracked intervention (routing, assignments, outreach, resolution) | Coordinated Care Network; Cases & Referrals; To-Dos; Appointments; Notes | track outreach, share notes, coordinate care across teams | assign follow-up actions; monitor intervention outcomes; caseloads | care/action plans; appointment scheduling; referrals | **All 4 — core** |
| Multi-office success network (not one office's tool) | "advising, enrollment, career services, tutoring" | "leaders, advisors, faculty, and student service teams" | "advisors, faculty, student affairs, retention teams, success coaches, leaders" | cross-department common capabilities | **All 4 — core** |
| Campaign/population-scale outreach | Campaigns & Template Library; Two-Way SMS | SMS & Email outreach; filtered lists | automation; stage conversion | Marketing Cloud adjacent | **Common (L1)** |
| Success/degree plans, to-dos for students | To-Dos; Student Journeys | Degree Planning; Schedule Builder | Guided pathways | care and action plans | **Common (L1)** |
| Retention/persistence outcome measurement | Intervention Effectiveness; Historical Analytics | Initiative Analytics; multiple outcomes | retention outcomes; "report results against standards" | lagging/leading indicator frame | **All 4 — core (depth varies)** |
| Predictive ML models | 200+ custom models (vendor claim) | institution-specific models (core pitch) | persistence/course-completion models | Einstein/Agentforce AI | **Common (L1); not definitional** |
| Student-facing app/portal | yes (mobile + desktop) | yes | yes (native mobile) | tailored portal | **Common (L1)** |
| Advising appointment machinery | yes | yes | yes | yes | **Common (L1) — advising-embedded** |
| Case/referral objects | Cases & Referrals | (care coordination semantics) | concerns/follow-up | case management primitive | **Common (L1) — case machinery inside the loop** |
| Enrollment/recruitment module | Enrollment CRM module | Strategic Enrollment use case | (pre-enrollment context minimal) | Recruitment & Admissions module | **Optional/adjacent (L2)** |
| Advancement/alumni module | Advancement CRM | — | — | Advancement module | **Optional/adjacent (L2)** |
| Wellbeing/pulse checks | sentiment analysis (engagement hub) | "not just GPA" outcomes framing | — | wellbeing pulse checks | **Optional (L2)** |
| AI assistants/agents | AI agents, knowledge agent | CivIQ AI | AI in higher-ed positioning | Agentforce | **Era-current (L2)** |
| SIS as primary data substrate, LMS second | explicit | explicit (pipeline) | explicit | explicit | **Common substrate (L1)** |
| Enterprise vs per-user licensing | enterprise license | (not stated) | (not stated) | per-user/month | **Variant (L2)** |
| Consulting/strategic services bundled | Strategic Leader; Collaborative | dedicated partnership | client experience team | partner ecosystem | **Variant (L2)** |

Layer-B (cross-product commonality) conclusions:

1. Every sampled product holds the enrolled student population as persistent addressable records enriched from other institutional systems, operated at both individual and population grain.
2. Every sampled product has proactive signal machinery reaching staff without student-initiated contact — faculty-raised alerts/progress reports and computed risk/persistence indicators at minimum.
3. Every sampled product turns signals into tracked, assigned, resolvable work distributed across multiple offices.
4. Every sampled product measures success outcomes (retention/persistence/progression) and commonly attributes them to interventions/initiatives.
5. Advising machinery, case/referral objects, campaigns, plans, student apps, and predictive ML are universal-but-derived: present everywhere, but each is one instrument inside the loop rather than the organizing center.

## Canonical Model (abstraction levels)

### L0 — Defining Invariant (minimal)

The higher-education institution's student-success operation platform. Four jointly-held structures:

1. **The enrolled-student success population of record** — persistent identified student records enriched with success context (academic standing, engagement, support history) drawn from across the institution's systems, held and managed at both individual and cohort/population grain, spanning terms.
   - Remove → SIS report layer / student data warehouse; nothing to operate on.
2. **Proactive success signals** — students who may be off-track surfaced to staff without student-initiated contact: faculty/staff-raised early alerts and progress reports, rules-based flags, engagement indicators, or predictive persistence models. The mechanism is a variant axis; the proactive surfacing is the invariant.
   - Remove → a reactive relationship tool (work starts only when a student asks) or a passive report.
3. **The coordinated intervention loop** — each signal becomes tracked work across the institution's success network: screened/routed, assigned outreach (appointments, messages, tasks, notes, referrals) carried to recorded resolution, at single-student and campaign/population scale.
   - Remove → an alert feed nobody works, or a dashboard nobody coordinates through.
4. **The success-outcome measurement layer** — retention/persistence/progression tracked as managed measures at cohort/institution grain, with intervention/initiative effectiveness commonly attributed against those outcomes.
   - Remove → care coordination without the institutional outcome loop, or institutional-research reporting over nothing.

Jointly-held load-bearing analysis:

- 1 alone = student data warehouse / SIS reporting
- 2 without 1+3 = alert feed / notification tool
- 3 without 1+2 = generic casework or advising scheduler
- 4 without 1–3 = BI / institutional-research dashboard
- 1+2 without 3 = watchboard nobody acts on
- 1+3 without 2 = responsive casework (advising/case-management territory)
- 2+3 without 1 = anonymous alert handling
- 1+4 without 2+3 = IR analytics
- 2+3+4 without 1 = intervention tracking with no population memory
- 1+2+3 without 4 = coordinated care without the outcome loop — the advising-adjacent pole (boundary vs Academic Advising Platform)

### L1 — Common Mature Structure

- SIS/LMS integration spine (SIS primary data source, LMS engagement second) — substrate, not structure
- Campaigns / population-scale outreach (SMS/email, templates, lists)
- Success plans / guided pathways / to-dos; student-facing app or portal (appointments, tasks, resources, self-raised concerns)
- Advising appointment machinery and documentation inside the loop
- Case/referral objects inside the loop
- Predictive analytics (institution-specific persistence models) and AI assistance
- Custom reporting/dashboards, query builders
- Shared notes / cross-team visibility controls

### L2 — Variant / Optional Structure

- Analytics depth: consulting-model-with-embedded-analytics vs predictive-platform-first vs configurable-CRM-module
- Packaging: dedicated product vs module of a journey-wide suite (recruitment/advancement/financials bundled around the success core)
- Segment: community-college first-year/transfer emphasis vs 4-year persistence vs K-12 "early warning" posture (attendance/behavior/grades signals)
- Student-facing depth: full engagement hub vs thin companion app
- Commercial model: enterprise license vs per-user subscription vs suite editions
- Service model: bundled strategic consulting vs software-only
- Wellbeing/sentiment measurement, career-readiness modules
- Deployment: cloud SaaS dominant; hosting posture varies

### L3 — Vendor-specific Detail (Research Notes only)

- EAB: "Coordinated Care Network" branding; Strategic Leader role; Student Success Collaborative; Student Hand Raise; 200+ custom models claim; 95%+ renewal claim; revenue-ROI calculator
- Civitas: CivIQ AI; Civ Data Pipeline; "multiple outcomes not just GPA/retention" differentiation; initiative ROI reporting; integration with competing platforms' data
- Watermark: Educational Impact Suite adjacency (assessment/accreditation); heritage lineage (Aviso → Watermark); "one-term prediction" time-to-value claim; accreditor-facing reporting framing
- Salesforce: Agentforce agents; common capabilities model (scheduling/case management/form-building as platform primitives); next-gen SIS ambition; per-user edition pricing; Tinto-model content marketing
- Marketing outcome numbers (retention +2–12% etc.) — vendor claims, excluded from canonical document

### Rejected Findings (anti-overfit)

- **Predictive ML is NOT definitional.** All four sampled products have it, but per the shared-implementation rule this is era-current market convergence, not the Type's identity. Faculty-raised flags and rules-based leading indicators satisfy the signal leg; the paper-era retention office (early-alert referral forms, caseload cards, term-to-term persistence tallies) satisfies all four legs at analog level. Historical check passed.
- **Advising machinery is NOT definitional.** Universal in-sample but advisors are one staff class inside a cross-office network; the advising pass centers the advisor–student relationship itself. Keeping advising in this Type's L0 would collapse the two leaves.
- **Case objects are NOT definitional.** Present in-sample as one object type; Student Case Management owns issue-driven casework as the center.
- **Campaigns/nudges are NOT definitional.** Single-student coordination satisfies the intervention leg; campaigns are the population-scale form.
- **Student-facing app is NOT definitional.** The Type's primary user is staff; the student surface is a companion layer (all sampled, but paper-era analog satisfies the core without it).
- **"Population health" vocabulary is NOT definitional.** It is one vendor-family's term for the population grain; cohort dashboards and institutional metrics express the same invariant elsewhere.

## Boundary Findings

### 1. vs Academic Advising Platform (§23 sibling) — DISCHARGES the pre-hung joint-review flag

- The academic-advising-platform pass's L0: student record with SIS-drawn academic context + advisor role with ongoing advising relationship (assigned caseload or service/reason matching) + scheduled documented advising interactions. Its L1 included early alerts & faculty progress reports/referrals with follow-up tracking — i.e., success machinery exists INSIDE advising products as common structure.
- This pass's L0 (four legs) does not require the advising relationship: every sampled product places advisors inside a wider network (EAB FAQ: "advising, enrollment, career services, and tutoring"; Watermark FAQ: "advisors, faculty, student affairs professionals, retention teams, success coaches, and institutional leaders"; Civitas: "leaders, advisors, faculty, and student service teams").
- Removal tests (both directions):
  - Strip the advising relationship/workflow from a student success product → population of record + signals + coordination + measurement remain = still recognizably this Type (the CRM-pole configuration, e.g., campaign-and-cohort-led deployments).
  - Strip population/signals/coordination/measurement from an advising product → the advisor–student relationship with documented interactions remains = still recognizably an advising platform.
- Verdict: **keep-both RATIFIED** on the center-of-gravity seam that pass proposed: advising = the advisor–student relationship + advising workflow at the center; student success = the institution-wide success operation (population + signals + coordination + outcome measurement) at the center. The overlap pole is real and converged in marketing (one market, two names for its two centers) — exactly as that pass predicted; the seam runs through products (both Types carry the other's machinery as L1), not between them.

### 2. vs Student Information System (§23 sibling, processed)

- SIS = the institution's system of record for official student data (that pass's L0: population of record + enrollment binding into academic structure + operational loop with rollover). The success platform consumes SIS data and does not own the official record.
- First-hand vendor-drawn seam: Watermark's FAQ contrasts "an SIS provider's success tool focuses heavily on degree progression and academic records" with its own "proactive extension of your care team… track and improve true student persistence." EAB FAQ: "The main source of data used to populate Navigate360 comes from the institution's student information system (SIS)" — the SIS is the substrate, the success platform the operation layer above it.
- Consistent with the SIS pass's record-ownership framing. No conflict.

### 3. vs Student Case Management (§23 sibling, processed)

- That pass's L0: the student case of record (issue-driven, opened through intake, tracked lifecycle to resolution) + worked case file + caseload coordination. Its center is the case; this Type's center is the population loop.
- In-sample evidence: Navigate360 lists "Cases & Referrals" as one feature among many; Salesforce names case management a shared platform primitive. Case-like objects are instruments inside the coordination loop, not the organizing unit.
- Removal test: strip population grain + signals + measurement from this Type, keep case lifecycle → Student Case Management. Strip case machinery, keep population loop → still this Type. Keep-both holds (consistent with that pass and the student-services-portal discharge).

### 4. vs Student Services Portal (§23 sibling, processed)

- Portal = the student-facing authenticated front door aggregating institutional services (that pass's L0). Success platform = staff-facing operation of the population. The student app/portal inside success products is a companion surface (appointments, tasks, resources), not the front door to institutional services.
- Keep-both; direction of operation differs (student-initiated self-service vs staff-initiated outreach).

### 5. vs Enrollment Management / Student Recruitment CRM (§23 siblings)

- Pre-enrollment funnel (prospect → applicant → deposit) vs enrolled-population persistence. Bundling is documented and heavy (Navigate360 Enrollment CRM module; Salesforce Recruitment & Admissions module; Civitas Strategic Enrollment use case) because the same profile and communication machinery serves both sides of enrollment.
- The seam is the population's enrollment state: pre-enrollment prospects = recruitment/enrollment territory; enrolled students operated for persistence = this Type. Products spanning both are suite realizations of two Types.

### 6. vs Customer Success Platform (§07, processed) — name collision

- Same word "success", different universe: B2B subscriber health/renewal (customer success) vs student persistence/graduation (this Type). Different subjects (paying customer accounts vs enrolled students), different outcome measures (churn/NRR vs retention/completion), different regulatory context (FERPA). No structural relationship; documented to prevent vocabulary confusion.

### 7. vs Institutional Effectiveness Platform / Higher Education Administration System (§23 siblings)

- Institutional effectiveness = unit-level mission/outcome assessment and improvement loop (program review, accreditation evidence) — the unit is the program/unit, not the individual student. This Type operates at student grain with cohort rollups. Higher-ed administration = institution-level academic-structure administration. The measurement leg of this Type is student-outcome grain (retention/persistence), not program-outcome assessment.

### 8. vs LMS / engagement analytics (no dedicated leaf)

- LMS engagement data is a common signal source (all four sample products integrate LMS data); the LMS centers course teaching/learning, this Type centers institutional persistence operation. Engagement-analytics tools (e.g., LMS-native dashboards) are signal suppliers, not competitors.

## Uncertainties

1. **Tier-1 depth.** No product's click-path help articles were fetched (Watermark HC category confirmed but articles not reached; EAB/Civitas/Salesforce KBs not fetched). All evidence is product-page strength. The final document therefore avoids precise workflow states, field lists, and numeric limits.
2. **K-12 pole.** EAB sells K-12 solutions and the K-12 "early warning system" pattern exists, but no K-12-native product was sampled. The K-12 posture is described as a variant axis, not verified in depth.
3. **Regional markets.** Sample is North-America-centric (US higher-ed vocabulary: retention, persistence, FERPA). Regional analogues (e.g., UK/AU engagement-analytics-led products) were not sampled; the L0 is phrased to admit them (population + signals + coordination + outcome tracking) but this is inference, not observation.
4. **Suite-module boundary.** Whether a Salesforce-class deployment using only generic CRM primitives constitutes a separate "success module" or a configured CRM is a packaging question; the document treats the module's capability set as the Type and notes the packaging variant.
5. **Measurement-leg minimality.** The measurement leg is deliberately minimal (tracked persistence/retention measures at population grain). If a future sample found a mature success-platform product with NO outcome tracking (signals + coordination only), the four-leg L0 would need revisiting; the advising-adjacent pole is recorded as the boundary at that edge.

## Final Synthesis

A Student Success Platform is the higher-education institution's operation layer for student success and retention. Its defining core is four jointly-held structures: the enrolled-student population held as addressable records with success context at individual and cohort grain; proactive signals that surface students who may be off-track without waiting for them to ask; a coordinated intervention loop that turns signals into tracked, assigned, resolvable work across a multi-office success network; and the institution's persistence/retention outcomes tracked as managed measures against which interventions are commonly evaluated. Advising machinery, case objects, campaigns, plans, predictive models, and student-facing apps are standard instruments inside this loop — common in every mature product, but none of them is what makes the Type. The Type shares a converged market with Academic Advising Platform (relationship-centered) and holds a substrate relationship with the SIS (official record) — both seams ratified as keep-both. Remove the population grain → casework; remove the signals → reactive advising; remove the coordination → a dashboard; remove the measurement → care coordination at the Type's edge.
