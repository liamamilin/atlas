# Research Notes — Assessment Platform

Research date: 2026-09-06
Methodology: v1.1 (update-v1/)

## Research Goal

Understand what an **Assessment Platform** (Directory §23 Education, Research & Knowledge Institutions) actually is as an application type: its core objects, its defining loop (author → administer → respond → score → report), its roles, its rules, and where its boundaries sit against Survey Platforms, Examination Platforms, LMS quiz modules, and the HR-side assessment types.

## Initial Boundary (hypothesis before research)

- Hypothesis: an assessment platform centers on a **scored instrument** (questions/tasks with defined scoring criteria) administered to a **population of takers**, producing **results attributed to takers**.
- Likely confusions:
  - Survey Platform (collects opinions; no scoring criteria)
  - Examination Platform (adjacent leaf; high-stakes formality?)
  - LMS (assessment as a module)
  - Candidate / Technical / Psychometric Assessment Platform (HR leaves; hiring vs learning)
  - Test Preparation Platform, Assignment Management, Digital Gradebook, Online Proctoring Platform (§23 neighbors)

## Research Questions

1. What is the central authored object, and how is it composed (items, content, scoring)?
2. How are items stored, reused, and organized (item banks, categories, metadata/standards)?
3. How is an assessment delivered: to whom, with what configuration (windows, attempts, security, feedback rules)?
4. How does scoring work: auto-scoring, manual marking, rubrics, partial credit, moderation?
5. What is the attempt lifecycle (start, save/resume, submit, retake)?
6. What result artifacts exist (per-taker scores, aggregates, item analysis, standards mastery, psychometrics, exports)?
7. What roles exist (author, administrator, grader/marker, proctor, taker, org admin)?
8. What integrity/security machinery is attached (randomization, lockdown, proctoring)?
9. What integrations anchor it (LMS/LTI, SIS/SSO, APIs, gradebook/HR systems)?
10. What distinguishes it from surveys, from examination platforms, and from LMS quiz engines?

## Representative Products

Chosen for market-representative spread across segment, stakes, philosophy, and customer tier:

| Product | Segment / philosophy | Customer tier |
|---|---|---|
| Formative | K-12 teacher-centric **formative** assessment; live classroom loop; standards data | Individual teachers → school/district |
| Questionmark | Enterprise **assessment management** for certification & workforce compliance; program-scale, audit-ready | Enterprise / regulated industries |
| Inspera Assessment | Higher-ed / professional **digital examinations**; formal roles (planner, grader, candidate); proctoring | Higher-education institutions |
| ClassMarker | Lightweight general-purpose **online testing** for education & business; simplicity + credits | SMB, training, classrooms |

Historical / market-sample breadth check (§24) applied at abstraction level: paper-based instruments scored by hand, OMR scan-grading tools, and oral/practical examinations evaluated against rubrics should also fit the eventual definition — so online authoring, online delivery, and full auto-scoring must not be definitional requirements.

## Sources

Evidence layers: A = directly observed on this date; B = cross-product commonality; C = canonical inference.

- Formative Help Center — https://help.formative.com/ (home, "Build Activities" collection, "Assign Formatives" collection) — Layer A
- Questionmark — https://www.questionmark.com/ (homepage, lifecycle, capabilities); https://help.questionmark.com/hc/en-us (help-center structure only; article content gated behind organizational sign-in) — Layer A for public pages; structure-only for help center
- Inspera Help Center — https://support.inspera.com/ (home + "Grade" section) — Layer A
- ClassMarker — https://www.classmarker.com/online-testing/faq/ (extensive FAQ/user-manual content) — Layer A

## Product Observations

### Formative (help.formative.com) — Layer A

- Help-center collections: Account Management; Create/Manage Classes; **Build Activities**; **Assign Formatives**; **View & Act on Responses** ("view responses, score, give feedback, and export results"); Organize Formatives/Practice Sets/Folders; **Analyze Data** ("track progress against standards"); Collaboration (School & District); Admins and Org Managers; Student Resources.
- Unit of authoring is the "formative" (an activity) built in an editor combining **question types** (multiple choice, multiple selection, short answer, true/false, free response, drawing "Show Your Work", audio response, categorize, drag-and-drop, file response, fill-in-the-blank, graphing, number line, hot spot, hot text, dropdown, match table grid, matching, numeric, resequence, video response, multi-part) with **content items** (text blocks, videos with timestamps, images/PDFs, embeds, audio, paired passages; import Google Slides/Forms; PDF parsing).
- Question settings: set point value, **set answer key for auto-grading**, partial match / partial credit, required questions, extra credit, hints, answer-choice explanations, **rubrics** (paid tier), sections within activities.
- Reuse: item bank (school & district add-on), pre-made activity library (incl. Newsela-authored content), practice sets; AI generation of activities/questions/passages.
- Delivery: assign to classes; assign or present; teacher-paced mode (present); game-paced mode; assign through LMS platforms (Google Classroom, Canvas, Schoology, Jupiter, Blackbaud); guest students (unrostered); placement-test administration for unrostered students.
- Assign-time settings: control what students can do (e.g., whether scores are returned); retakes (multiple attempts); pause a formative; close an activity; check-answer limits; calculator integration; student groups; LockDown Browser (Respondus) add-on for secure assessment; one-device/session restriction with LockDown.
- Responses: live/real-time response view (product tagline: "gather live insights"); scoring and feedback on responses; export results.
- Data: progress against **standards**; tagging formatives to type; data filtering.
- Organization: school/district collaboration, admins/org managers.

### Questionmark (questionmark.com; help.questionmark.com gated) — Layer A for public pages

- Positioning: "Enterprise assessment platform — create, deliver, and analyze assessment and certification programs."
- Lifecycle stated explicitly: **Manage** (item banks, schedule exams, control access, monitor progress; integrations via SCORM, LTI, xAPI) → **Author** (40+ question types, AI authoring tools, performance-based testing) → **Deliver** (global exams, browser lockdown, identity verification, flexible proctoring, translation management) → **Report** (70+ reporting features, AI-powered feedback, "audit-ready data" for compliance/competency).
- Products: Certification (incl. Academic) and Workforce (incl. Workday Learning, Government).
- Tools: proctoring (live, recorded, onsite), translation delivery (30+ languages), AI tools (authoring, AI scoring "with human control"), reporting & analytics.
- Help-center categories (structure only, content gated): **Authoring** (create/manage/publish questions and assessments), **Administration** ("assessment scheduling, proctoring, user management, and integration"), **Reporting** ("generate meaningful reports to analyze results and inform stakeholders"); authoring guides reference items, question types, "Technology Enhanced Items", scoring engines.
- Platform is built on the Learnosity assessment engine.

### Inspera Assessment (support.inspera.com) — Layer A

- Help-center topic structure for Inspera Assessment: **Author** (question creation, question sets, item bank management) → **Deliver** (test setup, delivery settings, **candidate enrollment**) → **Monitor** (real-time test progress, candidate status, post-test management) → **Grade** (marking tools, grading workflows, result exports) — plus **User Management** (accounts, roles, Access Groups), **Data and Analytics** ("Psychometrics dashboard and API data export"), **Integrity Browser & Resilience Proctoring**, **Recorded / Record & Review / Live Proctoring**, **Integrations** (open APIs, SSO, LTI, SIS), **Candidates** (system requirements, test preparation, exam day tools).
- Role-based user guides: Administrator, Educator, Student.
- Grade section detail: Marking workspaces; Marking; Assessment management; Guides for **Planners**; Marking in Classic Marking; **Offline marking and data export**; Similarity reports.
- Terminology is exam-flavored: candidate, test, planner, grader/marker. Multi-language support site (English/Norsk/Svenska) — Nordic higher-ed origin.

### ClassMarker (classmarker.com FAQ/manual) — Layer A

- Structure: **Tests** section holds questions and tests; **Question Bank** stores every question for reuse across tests (edits to a question apply to all tests containing it); **Categories** organize questions/tests and feed random selection; question types: multiple choice, multiple response, true/false, short answer (defined response), **survey (no points)**, essay (longer text, response not defined); tests combine **fixed questions** and/or **auto-selected questions** drawn randomly from categories.
- Grading: auto-scoring for defined-response types; essay/long-answer requires human grading; multiple-response grading styles: full points only / partial points (no deduction) / partial points **with deduction**; per-question scoring configuration.
- Delivery ("Assign"): via **Groups** (registered users log in to the site) or **Links** (non-registered users; public/private; embeddable in websites; password protection; **Access Lists** with per-taker codes; IP restrictions; themes/branding). Each test can be assigned any number of times with different settings.
- Assign settings: time & date availability, number of attempts allowed, pass mark, pass/fail feedback messages, certificates (always on completion, or only when passed), questions per page, "save and finish later" mode (multi-sitting), interface language per user/link, disable printing.
- Results: saved and reviewable; **real-time "in progress" results view** (answers saved as the taker advances pages); results by test/group/link; aggregate statistics for tests, questions, categories; CSV export; email results to extra verified addresses.
- Integrity: randomize question order, randomize answer order, random selection from bank, disable printing, AI proctoring add-on ("ClassMarker Monitor") recording tab-switch/leaving events.
- Data-integrity rule: a question or test **cannot be deleted** while results are saved against it — results must be removed first.
- Org: multiple administrators ("Assistants") with granular permissions (view/grade/delete results, manage tests/questions, manage users, assign tests); assistant without login that only receives emailed results.
- Other: certificates; API + real-time webhooks; paper option (prepare test for printing so it can be taken on paper); credits consumed per test-taken (pricing model — L3); sell access to tests via PayPal (L3); community quiz sharing (L3).

## Cross-product Comparison

| Dimension | Formative | Questionmark | Inspera | ClassMarker |
|---|---|---|---|---|
| Central authored object | "Formative" activity (questions + content) | Assessment (40+ item types, performance-based) | Question set → test | Test (questions from bank) |
| Reusable item store | Item bank (add-on), library, practice sets | Item banks (Manage) | Item bank management | Question Bank + Categories |
| Scoring | Answer keys → auto-grading; rubrics; partial credit | Scoring engine; AI scoring with human control | Auto + marking workspaces; offline marking | Auto + essay manual; partial-credit styles |
| Population binding | Classes (rostered); guest students | Scheduled exams, access control | Candidate enrollment; Access Groups | Groups (registered) / Links (non-registered, access lists) |
| Delivery config | Assign settings: retakes, pause/close, score-return, LockDown | Schedule, identity verification, lockdown, translations | Delivery settings, exam-day tools | Availability windows, attempts, pass mark, feedback msgs, save-and-resume |
| Live monitoring | Live response view | Monitor progress | Monitor (real-time progress, candidate status) | Real-time in-progress results |
| Marking | Score + feedback on responses | AI + human scoring | Marking workspaces; planner/grader roles | Essay grading; assistant grading permissions |
| Results | Per-student + standards progress; export | 70+ reports, audit-ready data | Result exports; psychometrics dashboard | Per-taker + aggregates; CSV export |
| Integrity | Randomization implied via settings? (observed: LockDown add-on) | Lockdown, proctoring (live/recorded/onsite) | Integrity Browser; Resilience/Recorded/Live proctoring | Randomize order/selection; AI proctoring add-on |
| Feedback to taker | Return scores (setting); feedback | Configurable | Grading → results | Pass/fail messages; certificates |
| Integrations | Google Classroom, Canvas, Schoology, Jupiter, Blackbaud | SCORM, LTI, xAPI, Workday, Cornerstone | APIs, SSO, LTI, SIS | API, webhooks |
| Roles | Teacher, student, org manager/admin | Admin, author, proctor, candidate | Administrator, Educator, Planner, Grader, Student/Candidate | Main admin, Assistants (permissions), users/visitors |

**Stable commonalities (Layer B / cross-product):** the author → deliver → respond → score → report loop; items with defined scoring; reusable item storage; assignment/delivery configuration (windows, attempts, access); auto-scoring plus human marking for open responses; durable per-taker results + aggregate reporting + export; live progress/response monitoring; role separation between assessing roles and takers; LMS/HR/IT integrations; integrity controls scaled to stakes.

**Variable by product/segment (Layer B/C):** stakes posture (practice vs high-stakes), security machinery (none → lockdown → live proctoring), standards/competency mapping vs psychometric analytics, taker identity substrate (roster, self-registration, guest link, access list), feedback timing (instant vs withheld pending grading/moderation), certificates, translation, paper/offline paths.

## Canonical Abstraction

### L0 — Defining Invariant

An Assessment Platform exists to **measure** people against defined criteria and produce reviewable, attributed results:

1. **Scored assessment instrument** — an authored/imported composition of questions/tasks carrying defined scoring criteria (answer keys, scoring rules, rubrics, point values). Without defined criteria it is a survey, not an assessment.
2. **Administration to a defined taker population** — the assessing side binds the instrument to a set of takers and a delivery occasion/configuration.
3. **Response capture** — takers' answers are recorded as attempts (the attempt is the durable unit even when taker identity is pseudonymous/guest).
4. **Evaluation against the instrument's criteria** — automated scoring and/or human marking of captured responses.
5. **Attributed durable results** — per-taker outcomes persist as records the assessing side can inspect, and feed reporting.

Remove the scoring criteria → survey tool. Remove administration/population binding → item authoring tool. Remove response capture/evaluation → content library. Remove attributed persistent results → ephemeral quiz game. All five are required.

### L1 — Common Mature Structure

- Item bank / reusable question storage with categories or collections; questions composed into instruments by selection.
- Rich question-type catalogs (choice, text, numeric, matching/ordering, interactive/"technology-enhanced" items) and media/content items inside instruments.
- Delivery configuration: availability windows, attempt limits, question ordering/randomization, save-and-resume, per-page pacing.
- Auto-scoring for closed items; manual marking with rubrics for open items; partial-credit policies; feedback/explanations.
- Live monitoring of in-progress attempts and responses.
- Result reporting: per-taker score views, aggregate/item statistics, exports; standards/competency mapping in education-facing products; psychometric analytics in enterprise/exam-facing products.
- Integrity controls scaled to stakes: randomization, lockdown browsers, proctoring add-ons.
- Role separation: author/assessor, administrator, marker/grader, proctor, taker; organization-level administration.
- Feedback and outcome surfaces to takers: returned scores, pass/fail messages, certificates (esp. certification contexts).
- Integrations: LMS/LTI, SIS/SSO, APIs/webhooks, gradebook or HR/L&D system hand-offs.
- AI assistance (authoring, scoring) emerging across tiers.

### L2 — Variant / Optional Structure

- Stakes continuum: ungraded classroom practice → graded coursework → institutional exams → certification/compliance programs (drives security, moderation, auditability).
- Delivery surface: live/presented modes (teacher-paced, game-paced), scheduled formal exam with enrollment, embedded-in-website links, paper printing, offline marking, (offline exam-taking players exist in this market but were not directly observed in this sample).
- Taker identity substrate: rostered students (SIS/LMS), self-registration, guest links, per-taker access codes, exam candidates via SSO.
- Feedback posture: instant score return vs withheld until grading/moderation; result publication.
- Monetization/access model: free classroom tier, enterprise contracts, credit-per-attempt, selling attempts to takers.
- Regional/regulatory: state-standards alignment (US K-12), national curricula, translation management, audit/compliance regimes.
- Adjacent bundled capabilities: plagiarism/similarity reports, surveys (no-points questions or standalone surveys), certificates, community content sharing.

### L3 — Vendor-specific (Research Notes only)

- Formative: teacher-paced/game-paced presentation; practice sets; Newsela integration; PDF parsing; Google Slides/Forms import; check-answer limits; specific LMS add-on behaviors.
- Questionmark: Learnosity engine; Workday/Cornerstone integrations; "40+ question types / 70+ reports / 30+ languages" figures; named product lines (Certification/Workforce).
- Inspera: Integrity Browser, Resilience Proctoring, Classic Marking, Originality product; planner/grader terminology; Nordic market posture.
- ClassMarker: credits-per-taken pricing; PayPal sell-access; Community quiz sharing; Themes; 30-day refund policy.

## Rejected Findings

- "Assessment platforms are defined by gamified quizzes" — rejected: game-paced modes are Formative-specific presentation variants (L3).
- "Assessment platforms require proctoring" — rejected: present only in high-stakes variants; Formative/ClassMarker treat it as add-on; ClassMarker functions without it.
- "Assessment platforms are psychometric measurement systems" — rejected: psychometric analytics observed as an Inspera analytics layer; most classroom products have none; keep as L2 depth variant.
- "Standards alignment is definitional" — rejected: observed in Formative (education) and as competency tracking in Questionmark (workforce), but absent as a requirement in ClassMarker; L1/L2.
- "Certificates are part of the type" — rejected: ClassMarker feature; certification-context common; L2.
- "Assessment platforms are LMS modules" — rejected: several products exist standalone with SIS/LMS *integration*, not embedding; the center of gravity is the assessment lifecycle.

## Boundary Findings

- **Survey Platform** (03.11): survey = opinions with no correct answer; assessment = responses evaluated against defined scoring criteria and attributed as outcomes. Direct evidence of the boundary inside one product: ClassMarker explicitly distinguishes "survey (no points)" questions from scored questions and offers standalone surveys. If scoring criteria/outcome attribution vanish, the product crosses into survey territory.
- **Examination Platform** (§23 neighbor, adjacent leaf): same core loop; the differentiator is **stakes/formality plus exam-operations apparatus** — formal scheduling and candidate enrollment, invigilation/proctoring, moderation boards, official result publication/certification. Inspera and Questionmark sit at this pole while remaining recognizably assessment platforms. This is a **probable variant/sibling pair**: the leaf split is defensible (examination platforms add an operations layer that general assessment tools lack) but the boundary is a gradient, not a wall. Flagged to STATUS.md for a dedicated pass.
- **Learning Management System / LMS**: LMS quiz engines overlap heavily, but an LMS centers course/content delivery and gradebooks; assessment depth (item banking, marking workspaces, psychometrics, program-scale scheduling) is where standalone assessment platforms live. Integration direction (assessment platform → LMS/SIS) supports this.
- **Candidate / Technical / Psychometric Assessment Platform** (§09 HR leaves): same mechanics, different population and purpose (hiring selection vs learning/certification), different regulatory/psychometric emphasis. Kept distinct as audience variants; psychometric assessment additionally centers instrument construction/measurement rigor.
- **Test Preparation Platform** (§23 neighbor): optimizes takers' future scores via practice and instruction; the assessment platform measures current ability. Practice modes overlap (Formative practice sets), but measurement-and-records remains the assessment platform's center.
- **Assignment Management / Digital Gradebook** (§23 neighbors): assignment tools collect work; gradebooks record grades. Assessment platforms produce scored outcomes that feed them; both can receive results via integration.
- **Online Proctoring Platform** (§23 neighbor): an integrity *service* layered onto delivery; in this sample it appears as add-ons/modules (LockDown add-on, ClassMarker Monitor, Inspera proctoring, Questionmark proctoring) — capability inside this type, standalone type elsewhere.
- **Academic Integrity / Plagiarism Platform**: checks authored work against corpora; not a scored-instrument system. Appears embedded as similarity reports (Inspera) — again embedding direction into assessment delivery.
- **Audience Response System** (§26): ephemeral live polling in events; no durable attributed measurement program.

## Uncertainties

- Questionmark's detailed operational workflows could not be verified: help-center article content is gated behind organizational sign-in. Claims about Questionmark rest on public product pages (Layer A for positioning/lifecycle lists) plus help-center structure; no precise operational details were taken from memory.
- Per-attempt **time limits**: strongly implied by the category ("exam day tools", timing being a classic delivery setting) but not directly observed in fetched pages; the final document therefore avoids asserting timed-delivery specifics.
- Offline exam-taking (locked offline players) is common knowledge in the exam market but was **not directly observed** in this sample (offline *marking* was, at Inspera); kept as a hedged variant mention.
- Accommodations (extra time, assistive settings) were not directly observed; excluded from the final document rather than guessed.
- Whether "Assessment Platform" and "Examination Platform" should remain separate leaves is a taxonomy question flagged to STATUS.md, not resolved here.

## Final Synthesis

The Assessment Platform is best understood as a **measurement pipeline for learning and competence**: authored scored instruments → administration to a defined taker population under configured delivery rules → response capture as attempts → evaluation (automatic and/or human) → durable results attributed to takers → reporting that closes the loop back into teaching, certification, or compliance decisions. Everything else — item banks, standards mastery, psychometrics, proctoring, certificates, LMS integration, gamified presentation — is the mature market's layered machinery on top of that pipeline, scaling with stakes from classroom practice checks to high-stakes certification programs.
