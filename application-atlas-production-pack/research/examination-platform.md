# Research Notes — Examination Platform

Research date: 2026-09-07
Methodology: v1.1 (update-v1/)

## Research Goal

Understand what an **Examination Platform** (Directory §23 Education, Research & Knowledge Institutions) is as an application type: what the "examination" object is, how exam occasions are planned and run, what exam-day operations look like, how evaluation and result publication are governed, and where the boundary sits against Assessment Platform (the §23 sibling that carried a joint-review flag into this pass), Online Proctoring Platform, LMS quiz engines, and certification test-delivery networks.

This pass also discharges a pending joint review recorded in STATUS.md: *assessment-platform vs examination-platform (§23 siblings)* — the sibling research pass concluded the core loop is identical and the differentiator is a stakes/formality gradient plus exam-operations apparatus, flagged for resolution "when Examination Platform is processed".

## Initial Boundary (hypothesis before research)

- Hypothesis: an Examination Platform is the organizer-side system of record for **formal examinations** — scheduled exam occasions with enrolled candidates, controlled delivery (supervision/lockdown/proctoring), governed marking (graders, committees, moderation), and official result publication (to candidates and onward to student-record systems).
- Likely confusions:
  - Assessment Platform (sibling leaf; the sibling pass already observed the two share the author → deliver → respond → score → report loop)
  - Online Proctoring Platform (integrity service; own leaf)
  - LMS quiz engines
  - Test Preparation Platform (learner-side)
  - Certification/licensure test-delivery networks (Pearson VUE/PSI-style; sponsor-facing delivery operations)
  - Candidate / Technical / Psychometric Assessment Platform (§09 HR leaves)

## Research Questions

1. What is the central managed object — how is an exam defined, planned, scheduled, and activated?
2. How do candidates get bound to an exam occasion (enrollment, import, access codes, invitations)?
3. What does exam-day operation look like: start/end authority, monitoring, candidate status, incidents, resumes, make-ups, irregularities?
4. What delivery-control apparatus exists (lockdown browsers, clients, invigilation/proctoring, anonymization) and is any of it definitional?
5. How is evaluation organized: graders, committees, workflows, moderation, confirmation, grading scales?
6. What makes a result "official": publication, explanations, appeals/reassessment, transfer to student-record systems?
7. What roles exist on both sides (organizer-side vs candidate-side)?
8. Do paper/offline/oral exam modes exist (historical + hybrid check)?
9. What integrations anchor the platform (SIS/LIS, LMS, SSO, registries, APIs)?
10. What actually separates this Type from the Assessment Platform — operations, stakes, or nothing?

## Representative Products

Chosen for market-representative spread across segment, philosophy, customer tier, and control model:

| Product | Segment / philosophy | Customer tier |
|---|---|---|
| Inspera Assessment (Norway) | Institutional digital examinations end to end; exam-operations-heavy (planner/invigilator/committee machinery); Nordic HE + national exams | Universities, national exam programs |
| ExamSoft (US, by Turnitin) | High-stakes professional education; device-lockdown offline client (Examplify); integrity + accreditation analytics | Nursing/law/health-science programs, certification & licensure bodies, bar examiners |
| Digiexam (Sweden) | Simplicity-first exam platform for schools; teacher-created exams; invigilator surface; LMS-adjacent | K-12 → higher education institutions |
| TAO Testing (open source) | Open-standards delivery engine beneath large testing programs; rostering/delivery/test centers; white-label | National ministries of education, large districts, certification programs |

Historical / market-sample breadth check applied at abstraction level: the paper exam in a supervised hall (printed papers, invigilators, attendance lists, hand-marked scripts, published grade lists) and OMR scan-graded exams must also satisfy the eventual definition — so online authoring, digital delivery, and lockdown clients must not be definitional. Direct evidence of the paper–digital seam inside current products: ExamSoft "post or print an assessment", Inspera "Grading only" test type (register scanned handwritten responses) and InsperaScan, Digiexam "Offline exam file".

## Sources

Evidence layers: A = directly observed on this date; B = cross-product commonality; C = canonical inference.

- Inspera Help Center — https://support.inspera.com/ (home; Deliver section incl. Test creation and settings, Committees and contributors, Committee moderation, Multiple attempts and test duration, Assessment path, Appeals, InsperaScan; Monitor section incl. Post-test management; Grade; Candidates) — Layer A
- Inspera articles: "How to create a test"; "General test settings"; "Security test settings"; "Collaborative grading workflow in test settings"; "Create and manage Committees" — Layer A
- ExamSoft — https://examsoft.com/ (positioning: offline device lockdown, high-stakes, certification/licensure, bar applicants); https://examsoft.com/support — Layer A
- ExamSoft Help Center — https://support.examsoft.com/hc/en-us (home; Exam-Makers category: Enterprise Portal, Map, Exam Integrity, Benchmark Exams, Examplify; Exam-Takers category: Before/Taking/Viewing Results, Bar Exam; Enterprise Portal section: User Management, Portal Management, Assessments (Create/Post/Proctor/Grade), Questions and Categories, LMS Integrations, Reports; article: "Exam Integrity: Use the Exam-Takers List to Review Incidents") — Layer A
- Digiexam — https://digiexam.com/ and https://digiexam.com/platform/how-it-works (platform loop, lockdown/proctoring products) — Layer A
- Digiexam Knowledge Center — https://support.digiexam.se/hc/en-us (category/section structure: Teachers, Students, Administrators, Account managers, Invigilator; guide titles incl. Create/Start/Schedule an exam, Exam Library, QTI, rubrics, Canvas/Moodle schedule→start→end→grade→publish, Offline exam file, Invigilator view, Monitor an exam) — Layer A for structure; article-level pages returned 403/timeout (see Uncertainties)
- TAO Testing — https://www.taotesting.com/ (platform modules, editions, national-scale case studies); https://www.taotesting.com/rostering-delivery/ (SIS connect, LTI launch, scheduled deliveries with availability/duration/attempt constraints, test centers and groups, white-label, proctoring, accessibility) — Layer A
- Sibling pass (2026-09-06): research/assessment-platform.md — Questionmark public posture (Manage/Author/Deliver/Report; scheduling, lockdown, proctoring) and the joint-review hypothesis — Layer A (sibling's own fetches), Layer B here

## Product Observations

### Inspera Assessment — Layer A

- **Roles**: Planner (creates/activates tests), Author (question sets), Grader, Invigilator, Candidate/Student; Access Groups gate who can be assigned tests; per-test **Contributors** (users not added as contributors have no access to the test or its candidate list).
- **Test creation** (Deliver module): test name + question set(s) (shared by the Author) + Access Group + optional template; scheduling fields: **Test opens** (start time), **Standard end time**, **test duration**; activation step makes the test visible to assigned candidates and it "opens automatically at the start time"; invitations go to Graders; enable/disable switch. Precise limits exist (duration cap, candidate-count cap) — recorded in L3, not promoted.
- **Candidate enrollment**: manual add (one-time users, CSV/SSO import, permanent users) or **Test Code** invitation; anonymization is default-visible for tests connected to external systems or joined by test code (candidates anonymous to Planners/Graders/Invigilators unless "non-anonymous" enabled).
- **Settings groups**: General / Security / Exam day / After test / Grading workflow / Explanation of grades.
- **General settings**: fully **oral exam** mode (candidates do not interact digitally; oral question type only); **auto submission** for home exams (no Safe Exam Browser) — auto-submit at closing time; **thesis** designation; **"Grading only"** test type — candidates do not respond in the platform; the test exists to register responses originating outside (e.g., scanned handwritten answers) or to record grades for transfer to external systems; idle-candidate warning; **Marking 2.0** grading tool; **Candidate report** (candidate-facing review); grading scale with **threshold values** (marks per question compute a grade) vs grader-set grades.
- **Security settings**: require **lockdown browser** (Safe Exam Browser / Inspera Lockdown for Chromebooks); open-browser mode with **invigilator password** (e.g., controlled-network computer labs); **day password** for open school-based exams; ID verification checks (candidate ID card confirmed after submission); tests **started manually by Invigilators via the Monitor module**; **invigilator instructions PDF** with configurable availability window; originality/similarity check surfacing in the marking tool.
- **Committees**: a **Committee is a group of one or more Graders responsible for assessing and grading candidate work**; graders and candidates assigned per committee; per-committee workflow overrides (general workflow, collaboration settings, **confirmation of marks and grade**); grading workflow options: confirm all candidates at once vs confirm each candidate individually (grade shared with co-grader before final); candidates unavailable for grading until their deadline passes under auto-submission; a **Committee moderation** section exists (workflow detail not fetched).
- **Monitor**: real-time test progress; **candidate status and intervention**; post-test management — download/print submissions, CSV export, **open a test for resubmission**, submit on behalf of a candidate.
- **After results**: **Explanation of grades** machinery (candidates log in to read explanations sent by Planner/Grader); post-submission review and feedback settings; **Appeals/Reassessment workflow** (candidate management, setup, and "Transfer appeals grades to FS" — an external student-record system); result exports; psychometrics dashboard + API data export.
- **Hybrid/paper**: **InsperaScan** section (paper/scanning); "Grading only" test type (above); offline marking and data export in the Grade section.
- **Integrations**: open APIs, SSO, LTI, SIS; multi-language help center (English/Norsk/Svenska) — Nordic institutional origin.
- **Candidates section**: system requirements, test preparation, exam-day tools, post-test resources.

### ExamSoft — Layer A

- **Positioning**: "digital exam platform" for **secure high-stakes assessment**; delivers exams **offline**, locking down the entire testing device and disabling network connection (blocking AI tools, websites, other apps); remote and in-person; audiences: higher/secondary education (health sciences, law, business, humanities) plus "businesses, organizations, and government entities with certification and licensure exams"; dedicated **Bar Applicant** portal (bar.examsoft.com) for bar exams (registration, exam dates, mock exam download, Examplify re-download).
- **Exam-maker lifecycle** (Enterprise Portal → Assessments): **Create an assessment** (assessment types, settings, security options, **pre-assessment notifications**, rubrics) → **Post an assessment** ("post or print an assessment for your exam-takers") → **Proctor an assessment** (setup and management: view **downloaded/uploaded exam data**, create **make-up assessments**, issue **resume codes**) → **Grade an assessment** (import/export results, view exam-takers' **log files**, grade and **post assessment results**) → Archive an assessment.
- **Portal model**: Enterprise Portal (vs Legacy Portal): **User Management** (admin + exam-taker accounts, groups/courses); **Portal Management** (departments and courses at term start/end); **Questions and Categories** (question types, statistics, categories — item banking); **LMS Integrations** (sync courses and grades; export questions/quizzes into ExamSoft); **Reports** (performance reports per student, assessment, course, or category).
- **Exam integrity operations**: **Exam Integrity** tab; **ExamID** (identity verification with baseline images) and **ExamMonitor** (proctoring) reports; incident review via the **Exam-Takers list** or a **Review Queue** per assessment; **Exam-Taker Details** page where staff **submit a disposition**; AI-assisted integrity review tips; mock-assessment best practices; resume codes tied to reboot time limits.
- **Candidate side** (Exam-Takers): device setup + Examplify install (Windows/Mac/iPad), minimum system requirements, antivirus disable guidance, **mock exams**, "Before Taking Your Exam" preparation, "Taking Your Exam", answer-file **uploads** (offline capture → upload), **Viewing Exam Results** (portal results; **Secure Exam Review** in Examplify), **accommodation troubleshooting** and accessibility features.
- **Accreditation analytics**: **Map** — mapping documents, **Accreditation Standards documents**, user accounts/permissions; question tagging to categories feeds program-level outcome reporting ("longitudinal performance data… accreditation requirements" per product pages).
- **Benchmark Exams**: faculty workflow; view reports and **release results**.
- **Support posture**: 24/7 global phone support for exam-makers and exam-takers (exam-day support as an operational norm).

### Digiexam — Layer A (structure + product pages; article pages blocked)

- **Positioning**: "Exam Platform — create, deliver, and grade secure assessments" end to end for educational institutions; separate **Lockdown** product (secure layer around LMS-run assessments) and **Online Proctoring** (AI + live) as related services; Classroom Management Tool.
- **Loop** (how-it-works): log in (admins/teachers via browser; students via LMS, browser, or student application) → create/fetch exam from **Exam Library**, choose settings/format → **start or schedule** the exam "using an Exam ID or by selecting a group" → monitor progress (student status, submission details) while active → grade per question or per student (auto-grading for objective questions, AI-assisted feedback, teacher collaboration, **anonymous grading**) → **publish results instantly or scheduled**, with analytics.
- **Roles** (Knowledge Center categories): **Teachers, Students, Administrators, Account managers, Invigilator**; Invigilator guides: **Invigilator view**, **Monitor an exam**, **Offline exam file**.
- **Teacher guides** (titles observed): create account, create exam, add questions, **start an exam**, **schedule an exam**, rubrics, **QTI files** (create/convert), groups, exam library, delete exams, allow copy-paste/links, **external tools in an exam**, remote exams with Google Meet, **centrally administered exams and assignments**, AI quiz creation.
- **LMS integration flows** (Canvas and Moodle sections): **Schedule → Start → End → Grade → Publish** the exam — the exam occasion is managed as a unit even when launched from an LMS.
- **Students**: separate student application / "Take an exam" login.

### TAO Testing — Layer A

- **Modular platform**: Authoring (item banking, open standards) · **Rostering & Delivery** ("manage exam candidates and deliver… via test-centers, groups or the LTI standard") · Reporting · Cloud Services; next-gen: **TAO Advance** delivery engine, **TAO Grader** (technology-assisted human scoring, collaborative open-response marking), TAO Insights (data API).
- **Rostering & Delivery detail**: connect with the **Student Information System** to manage candidates; launch assessments from the LMS via LTI; **schedule online test deliveries** with timing constraints for **test availability, duration of tests, and maximum attempts**; access via standard web browsers **including lock-down browsers for individuals or groups of candidates**; **test centers and groups** ("exam registration capabilities make it easy to organize your test takers and assign assessments"); automatic scoring for traditional question types; white-label branding; AI-based remote proctoring with lockdown + test integrity reporting; accessibility/accommodation tooling (WCAG 2.1 AA positioning).
- **Scale posture**: editions from open-source Community Edition to Enterprise; case studies with national ministries of education (Japan, France), a national agency (Lithuania), NYC DOE, and an OECD PISA 2025 platform partnership — large scheduled testing campaigns ("critical testing campaign windows").
- **Open standards**: QTI-class interoperability emphasized (authoring "based on open education standards").

### Questionmark (via sibling pass, corroborating only)

- Public posture (2026-09-06 sibling fetches): Manage (item banks, **schedule exams**, access control, monitoring) → Author → Deliver (global exams, browser lockdown, identity verification, flexible proctoring) → Report (audit-ready data); certification + workforce lines; help-center article content gated. Not re-fetched this pass; used only as corroborating evidence that exam-scheduling/proctoring machinery exists in the assessment-management pole.

## Cross-product Comparison

| Dimension | Inspera | ExamSoft | Digiexam | TAO |
|---|---|---|---|---|
| Central object | Test (question set + schedule + candidates), activated | Assessment (created → posted → proctored → graded → archived) | Exam (created/library, started or scheduled) | Assessment delivery (rostered, scheduled, delivered) |
| Occasion semantics | Explicit opens/end times + duration; auto-open on start time | Post → exam-takers download/take offline → upload; make-ups | Start or schedule via Exam ID or group | Scheduled deliveries; availability windows, duration, max attempts |
| Candidate binding | Manual add / CSV-SSO import / one-time users / test code; Access Groups | Exam-taker accounts, groups/courses; Examplify registration; bar-applicant registration | Groups; Exam ID; LMS login | SIS rostering; test centers and groups; LTI launch |
| Exam-day control | Lockdown (SEB/Chromebook) or open browser + invigilator password; day password; invigilator-started tests; Monitor with candidate status & intervention | Offline device lockdown (no network); proctoring setup; resume codes; log files | Lockdown app; invigilator view; monitor exam; offline exam file | Lockdown browsers (individuals/groups); remote proctoring; integrity reporting |
| Integrity products | Integrity Browser; Recorded/Record & Review/Live proctoring modules | ExamID (identity), ExamMonitor (proctoring), dispositions, review queue | Lockdown product; AI + live proctoring (related services) | AI remote proctoring + lockdown (module) |
| Evaluation governance | Committees of graders; per-committee workflows; confirmation of marks/grade; co-grader sharing; grading scales + thresholds; mark schemes; committee moderation section | Grade step with result import/export; post results; scoring adjustments (legacy); categories statistics | Grade per question/student; collaboration between teachers; anonymous grading | TAO Grader (collaborative human scoring) alongside auto-scoring |
| Result officiality | Displaying final marks/grades + general feedback settings; explanations of grades; candidate report; appeals/reassessment; transfer to external registry (FS) | Post assessment results; release results (benchmark); Secure Exam Review for candidates; reports | Publish results instantly or scheduled | Results & reporting; API data access |
| Incident handling | Resubmission; submit on behalf of candidate; post-test management | Resume codes; make-up assessments; wrong-account triage; dispositions | (Not directly observed at article level) | (Not directly observed) |
| Paper/offline hybrid | InsperaScan; "Grading only" (register scanned/external responses); offline marking | Print assessment; offline client with upload | Offline exam file | (Not directly observed) |
| Oral/practical | Oral exam mode (oral question type) | (Not observed) | (Not observed) | (Not observed) |
| Analytics | Psychometrics dashboard; API export | Per student/assessment/course/category reports; accreditation mapping (Map); benchmark | Performance analytics | Reporting module; Insights API |
| Integrations | APIs, SSO, LTI, SIS | LMS integrations (course/grade sync); LMS question export | Canvas/Moodle flows (schedule→start→end→grade→publish); LMS login | SIS, LTI/LMS, open standards (QTI-class) |
| Taker-side surface | Candidate dashboard; exam-day tools; mock/demo tests | Examplify client (download, mock exams, upload); results views | Student app / browser / via LMS | Browser or lockdown client |
| Scale posture | Institutional + national exams (Nordic) | Program/high-stakes; certification/licensure; bar | Institutions ("900+ institutions" marketing) | National campaigns, multi-language delivery |

**Stable commonalities (Layer B):** the exam as a planned, scheduled, activated occasion built from an authored instrument; formal candidate enrollment binding identified takers to the occasion; enforced occasion rules (window, duration, submission) with delivery control scaled from open browser to full device lockdown; an organizer-side monitoring surface during the sitting; a governed evaluation step (graders/committees; auto + human scoring); results **published/released/posted** as the official outcome; post-result machinery (candidate result views, explanations, appeals) at least at the institutional pole; SIS/LMS/SSO/API integration spine; paper/offline hybrid paths preserved.

**Variable by product/segment (Layer B/C):** stakes posture; control apparatus strength (lockdown/offline vs invigilated lab vs open home exam); committee/moderation depth; anonymized marking; national-registry transfer; accreditation mapping; white-label/open-source posture; test-center networks.

## Canonical Abstraction

### L0 — Defining Invariant

An Examination Platform is the **organizer-side system of record for running formal examinations**. Four properties; remove any one and the product stops being an examination platform:

1. **The examination as a formal occasion of record** — an identified exam assembled from an assessment instrument and declared rules (when it opens, how long it runs, what conditions apply), planned and activated by the organizer as an official event rather than an ad-hoc quiz. Without occasion-of-record semantics the product is a generic assessment/quiz tool.
2. **Enrolled candidate population** — the organizer formally binds identified candidates to the occasion (registration, import, enrollment, or access granting), making the sitting a rostered event with attendance/accountability, not an open self-serve activity.
3. **The sitting conducted under organizer-enforced conditions** — the platform, not the candidate, controls the boundaries of the exam session: the window opens and closes, duration is enforced, submission is captured, and the sitting runs under conditions the organizer declares (from invigilated/lockdown/proctored environments to controlled open-browser modes), with an organizer-side surface to monitor the sitting and handle exceptions. Without enforced session boundaries the product is a practice/self-study tool.
4. **Governed evaluation producing official results** — captured responses are evaluated through a managed marking/grading process (human and/or automated, with grader roles and — at the institutional pole — committees/moderation), and the outcome is **released as the official result of record** attributed to each candidate (published to candidates, reported to the institution, transferable to student-record systems). Without governed release of attributed results the product is an ephemeral quiz game.

Model:

```text
Examination (occasion of record: instrument + declared rules + schedule)
└── Enrolled candidates (formal roster binding)
    └── Sitting (platform-enforced session under declared conditions)
        └── Captured responses
            └── Governed evaluation (graders / committees / moderation)
                └── Official result of record per candidate
                    └── Publication / transfer (candidates, institution, registries)
```

Historical check: the paper exam in a supervised hall satisfies all four (printed instrument = occasion; candidate list = enrollment; invigilated timed hall = enforced sitting; marked scripts → published grade list = governed results). OMR-scan grading satisfies response capture and evaluation. The definition therefore does not depend on online authoring, digital delivery, lockdown clients, or proctoring.

### L1 — Common Mature Structure

- Authored instrument layer: item banks / question sets, question-type catalogs, rubrics and mark schemes; auto-scoring for closed items plus human marking for open ones.
- Grading machinery: grading scales and thresholds, marking workspaces, grader assignment, anonymous marking, result review by candidates.
- Exam-day monitoring: real-time progress, candidate status, intervention tools; download/export of submissions.
- Exception operations: resubmission, submit-on-behalf, make-up assessments, resume codes, incident review.
- Integrity apparatus scaled to stakes: lockdown browsers / lockdown clients / offline-capable clients, identity verification, AI or live proctoring, similarity checks.
- Post-result rights: explanations of grades, appeals/reassessment workflows.
- Reporting: per-candidate results, aggregates, item/category statistics; psychometric or accreditation analytics at the enterprise pole.
- Integration spine: SIS/SIS-class rosters, LMS/LTI, SSO, open APIs; result transfer to student-record systems.
- Candidate preparation surfaces: system requirements, mock/demo exams, exam-day instructions.
- Multi-language delivery and accessibility/accommodation support in several products.

### L2 — Variant / Optional Structure

- Stakes continuum: school test → course final → institutional/national exam → certification/licensure/bar (drives control, governance, audit depth).
- Venue/client model: campus computer labs, BYOD with lockdown clients, fully offline device lockdown, remote proctored take-anywhere, open home exams.
- Supervision posture: invigilated hall + monitor module vs proctoring services vs unproctored controlled windows.
- Governance depth: single grader → grading committees → formal moderation; confirmation workflows.
- Result publication semantics: instant vs scheduled vs after moderation; candidate-visible feedback depth.
- Registry integration depth: LMS grade sync vs SIS export vs national student-record transfer.
- Paper/oral hybrid: printed assessments, scanned scripts, offline exam files, oral exam modes, "grading only" recording shells.
- Program-level analytics: psychometrics vs accreditation/outcomes mapping.
- Packaging: institutional SaaS, national platform, open-source engine under institutional programs, LMS-adjacent lockdown add-on.

### L3 — Vendor-specific (Research Notes only)

- Inspera: duration cap and per-test candidate-count cap; idle warning threshold; invigilator-instruction availability window; Marking 2.0 vs Classic Marking; InsperaScan; Resilience/Recorded/Record & Review/Live proctoring product names; "Grading only" and thesis designations; FS appeals-grade transfer; Originality module; demo tests; Swedish national-exam preparation guides.
- ExamSoft: Examplify client (Windows/Mac/iPad); ExamID/ExamMonitor; dispositions; Review Queue; resume codes + reboot limits; Map accreditation documents; Benchmark Exams; ExamNow (lightweight live assessments); bar.examsoft.com portal; Secure Exam Review; Legacy vs Enterprise portals; 24/7 phone support posture.
- Digiexam: Exam ID joining; proprietary Lockdown app; Classroom Management Tool; LMS-wrapping Lockdown product (closed beta at research time); "900+ institutions" marketing figure.
- TAO: TAO Advance engine; TAO Grader; TAO Insights; Community/Accelerate/Ignite/Enterprise editions; white-label; "100 million+ tests, 30+ languages" marketing figure; OECD PISA 2025 partnership.

## Rejected Findings

- "Examination platforms are defined by lockdown browsers/proctoring" — **rejected**: Inspera documents open-browser home exams with auto-submission and invigilated open-browser labs; Digiexam documents allowed links/external tools; control apparatus is a graded implementation (L1/L2 knob), not the invariant.
- "Examination = online-only delivery" — **rejected**: ExamSoft "post or print", InsperaScan, Inspera "Grading only" for scanned handwritten responses, Digiexam offline exam file; paper-era exams pass the historical check.
- "Proctoring is part of the definition" — **rejected**: proctoring appears as add-on modules in every sampled product (Inspera proctoring modules, ExamSoft ExamMonitor, Digiexam proctoring service, TAO remote-proctoring module); Online Proctoring Platform is its own Type.
- "Examination platforms require high stakes" — **rejected**: Digiexam runs ordinary school tests; stakes tune the configuration, not the Type.
- "Any timed quiz in an LMS is an examination platform" — **rejected**: LMS quiz engines lack occasion-of-record planning, formal candidate enrollment, exam-day monitoring/exception operations, evaluation governance, and official result release.
- "Certification test-delivery networks are the same Type" — **rejected/boundary**: sponsor-facing delivery networks (test-center operations) center on delivery logistics for certification sponsors rather than the institution's examination record; kept as a boundary, needs its own pass if ever cataloged.

## Boundary Findings

- **Assessment Platform (§23 sibling; joint review discharged)**: the core loop (instrument → administration → response capture → evaluation → attributed results) is **shared** — Inspera/Questionmark-style products sit at this pole and remain recognizable assessment platforms. The retained split rests on four exam-operations structures that general assessment tools do not carry as a defining layer: (a) the exam as a **scheduled occasion of record** with declared conditions; (b) **formal candidate enrollment** into that occasion; (c) **exam-day operations** (monitoring, invigilation/proctoring integration, incidents, make-ups, resume codes); (d) **governed official results** (committees/moderation, publication, explanations, appeals, registry transfer). The boundary is a gradient in the market (corroborated: the sibling pass reached the same conclusion independently), but the leaf split is defensible — center-of-gravity discriminator: strip the exam-operations layer (enrollment, sitting operations, official publication machinery) and what remains is an Assessment Platform; add those structures as the reason the product exists and it is an Examination Platform. Keep both leaves; no merge.
- **Online Proctoring Platform (§23 neighbor)**: an integrity *service* consumed by examination platforms (module/add-on in all four sampled products); own leaf when sold standalone as supervised-exam-as-a-service.
- **Assessment Platform family member Online Proctoring vs invigilation**: invigilation (supervision of the sitting) is an exam-operations role inside this Type; AI/live remote proctoring is the standalone sibling Type.
- **Learning Management System**: LMS quiz engines and LMS-run tests exist (Digiexam even wraps LMS assessments with lockdown), but the LMS's center of gravity is course/content delivery and the gradebook; examination platforms center the exam occasion and result-of-record, integrating *into* LMS/SIS rather than being features of them.
- **Test Preparation Platform**: optimizes the taker's *future* performance (practice, instruction); the examination platform runs the *official* measurement event. Mock exams exist on both sides (candidate familiarization vs practice curriculum) — the record-formal outcome is the discriminator.
- **Digital Gradebook / Transcript Management**: recipients of results via integration; the examination platform produces the official outcome but is not the ongoing academic record system.
- **Certification & Licensure delivery (adjacent market)**: certification sponsors use examination-platform machinery (ExamSoft explicitly serves certification/licensure), but dedicated test-delivery networks (test-center operations, sponsor-facing scheduling APIs) are a distinct operational shape; boundary noted, not cataloged here.
- **Candidate / Technical / Psychometric Assessment Platforms (§09)**: same delivery mechanics, hiring purpose, HR record semantics; audience variant of the assessment family, not this Type.
- **Audience Response System / polling**: ephemeral, unrostered, unattributed — none of the four L0 properties.

## Uncertainties

- **Digiexam article-level content** returned 403/timeout (after two attempts, abandoned per source-access rules). Digiexam claims rest on the fetched product pages plus Knowledge Center category/section/guide titles — structure-level evidence only. No precise Digiexam operational rules are asserted anywhere.
- **Committee moderation workflow** at Inspera: the section exists (title observed); article detail not fetched. Treated as present-at-institutional-pole, detail unverified.
- **Accommodations**: directly observed at TAO (accommodation tools, accessibility positioning) and ExamSoft (accommodation troubleshooting, accessibility features); not directly observed at Inspera/Digiexam. Written as common-in-sample, not definitional.
- **Questionmark**: help-center content gated (sibling pass, 2026-09-06); used only as corroborating posture evidence.
- **Exam-day "attendance" semantics** (formal check-in/attestation beyond login): implied by enrollment + monitoring structures, but no sampled product documented a standalone attendance ritual in fetched content; the L0 phrase "formal roster binding" avoids asserting check-in mechanics.
- **Offline exam-taking**: resolved during this pass — directly observed (ExamSoft offline lockdown + upload; Digiexam offline exam file), superseding the sibling pass's hedge.
- **Timed delivery**: resolved during this pass — directly observed (Inspera duration setting; TAO availability/duration/attempt constraints), superseding the sibling pass's hedge.

## Final Synthesis

The Examination Platform is best understood as the **operations system for formal examinations**: it turns an assessment instrument into a **scheduled, rostered, officially sanctioned event** — candidates are enrolled, the sitting is run under conditions the organizer enforces and monitors, exceptions (resubmissions, make-ups, incidents) are worked as part of the event, evaluation is governed through grader roles (up to committees and moderation), and the outcome is **released as the official result of record** — published to candidates, reported to the institution, and transferable to student-record systems. Delivery control (lockdown, proctoring), analytics, paper/oral hybrids, and national-scale deployment are the mature market's layered machinery, scaling with stakes. The Type shares its measurement loop with the Assessment Platform; what makes it a distinct Type is that the **exam occasion and its official outcome — not the scored instrument alone — are the objects the whole product exists to run**.
