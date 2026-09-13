# Research Notes — Assignment Management

Research date: 2026-09-06
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand what an Assignment Management application is as an Application Type: its core objects, the two-sided workflow between instructor and students, the submission/grading lifecycle, and its boundaries against LMS, Digital Gradebook, Assessment Platform, and generic task management.

## Initial Boundary (working hypothesis before research)

- Core use: teachers/instructors create assignments (task + instructions + due date + grading basis), distribute them to a class roster, collect student submissions, grade, and return feedback.
- Primary users: instructors (authoring, grading), students (viewing, submitting), plus co-teachers/TAs, admins, and (in K-12) parents/guardians.
- Nearest neighbors: Learning Management System (broader container), Digital Gradebook (grade-record-centric), Assessment Platform (test/quiz-centric), Classroom Management (live-classroom control), To-do/Task Management (one-sided), SIS (records/enrollment), MOOC Platform (massive scale).
- Unknowns: standalone vs embedded product forms; exact submission lifecycle states; late-submission handling; how deep parent visibility goes; whether grading is definitional or optional.

## Research Questions

1. What fields/structure compose the central "assignment" object?
2. How are assignments distributed to students, and from where does the roster come?
3. What is a "submission"? What forms can it take? What states does it move through?
4. How does the grading/feedback loop work, and how are results returned to students?
5. How are due dates, late submissions, resubmissions, and exceptions handled?
6. What roles and permission surfaces exist (teacher, co-teacher, admin, student, parent)?
7. How does the assignment relate to the gradebook, the LMS course, and the SIS?
8. What does a standalone (non-LMS) product look like, and what does that imply about the Type's minimal form?
9. Which capabilities are Type-defining vs common vs variant vs vendor-specific?

## Representative Products

| Product | Vendor | Form | Segment | Why selected |
|---|---|---|---|---|
| Canvas LMS (Assignments/Submissions) | Instructure | module of full enterprise LMS | higher ed + K-12 | deepest documented assignment model; API exposes object structure |
| Assignments in Microsoft Teams | Microsoft | feature embedded in M365 Education suite | K-12 + higher ed | suite-embedded philosophy; guardian/SDS integration evidence |
| Blackboard Learn (Assessments/Grading) | Anthology | module of enterprise LMS | higher ed (also K-12) | long-standing higher-ed incumbent; Ultra assessment settings |
| Satchel One (Homework) | Team Satchel (formerly Show My Homework) | standalone homework platform | UK K-12 schools | proves the Type exists outside an LMS; parent/timetable-centric variant |
| Google Classroom | Google | lightweight assignment-centric platform | K-12 (also higher ed) | market anchor; **help center unreachable during research** (see Sources) |

## Sources

Tier 1 (official operational documentation) actually fetched on 2026-09-06:

- Canvas LMS REST API Documentation — Assignments API: https://canvas.instructure.com/doc/api/assignments.html
- Canvas LMS REST API Documentation — Submissions API: https://canvas.instructure.com/doc/api/submissions.html
- Canvas LMS REST API Documentation — LTI Assignment Tools / Assignment and Grading Services: https://canvas.instructure.com/doc/api/file.assignment_tools.html
- Microsoft Learn — "Assignments for Teams" (Teams for Education admin documentation): https://learn.microsoft.com/en-us/microsoftteams/expand-teams-across-your-org/assignments-in-teams
- Blackboard Learn Instructor Help (Anthology) — Assessments / Grading hub: https://help.blackboard.com/Learn/Instructor/Assignments (specific sub-pages redirect to the multilingual hub; hub-level structure observed)
- Satchel One Help Center — Staff collection: https://help.satchelone.com/en/collections/6936480-staff
- Satchel One — "Setting tasks": https://help.satchelone.com/en/articles/10669887-setting-tasks
- Satchel One — "Assignment" (task type): https://help.satchelone.com/en/articles/14079744-assignment
- Satchel One — "Marking tasks": https://help.satchelone.com/en/articles/2905138-marking-tasks

Attempted but abandoned (network limitation, per source-access rules):

- Google Classroom: support.google.com/edu/classroom (timeout ×2), edu.google.com (timeout), developers.google.com/classroom (timeout ×2). Google Classroom is retained as a market anchor only; no product-specific claims are made from it in the final document.
- Moodle: docs.moodle.org (403 ×2). Dropped from the sample.
- Blackboard sub-pages (e.g. Collect Submissions Offline): requests return the multilingual hub page; only hub-level structure is treated as observed.

## Product Observations

### Product A — Canvas LMS (Instructure) [Evidence layer A]

Observed via official API documentation (generated from source code).

Assignment object (course-scoped):
- identity: id, name, HTML description, course_id, position, created/updated timestamps
- scheduling: due_at, unlock_at, lock_at; assignment overrides (per student / section / group) with their own dates; "all_dates" rollup; important_dates flag
- grading: points_possible; grading_type ∈ {points, percent, letter_grade, gpa_scale, pass_fail, not_graded}; grading_standard_id (letter scheme); rubric with criteria/ratings, use_rubric_for_grading; omit_from_final_grade; hide_in_gradebook; post_to_sis
- submission control: submission_types ∈ {online_upload, online_text_entry, online_url, media_recording, student_annotation, online_quiz, on_paper, none, discussion_topic, external_tool}; allowed_extensions; allowed_attempts (-1 = unlimited); group assignments (group_category_id, grade_group_students_individually)
- publication: published / workflow_state "unpublished"; unpublishable=false once submissions exist
- integrity: Turnitin/VeriCite enablement + settings (originality report visibility, match exclusions); academic_integrity_pledge
- peer review: peer_reviews, automatic_peer_reviews, peer_review_count, peer_reviews_assign_at, anonymous_peer_reviews, intra-group option
- moderated grading: moderated_grading, grader_count, final_grader_id, provisional grades, grader anonymity flags, anonymous_grading
- instructor-side aggregates: needs_grading_count (optionally by section); score_statistics (min/max/mean/quartiles); list buckets: past, overdue, undated, ungraded, unsubmitted, upcoming, future
- operations: duplicate (with original references), submissions_download_url (zip of all submissions), notify_of_update on edit

Submission object (per student per assignment):
- identity: assignment_id, user_id, attempt number; anonymous_id for anonymized grading
- content: submission_type, body (text entry), url, attachments (file ids), media comment, student annotation on an annotatable attachment
- state: workflow_state ∈ {unsubmitted, submitted, graded, pending_review}; submitted_at; posted_at (manual grade posting); read_status
- grading: score (raw), grade (translated into the assignment's scheme), grader_id (positive = human grader; negative = autograding process such as quiz autograder or LTI tool), graded_at, rubric_assessment, grade_matches_current_submission (false when student resubmitted after grading)
- lateness: late (bool), late_policy_status ∈ {late, missing, extended, none}, seconds_late, points_deducted (automatic deduction by late/missing policy)
- exceptions: excused (no grade impact), missing, extra_attempts, redo_request (instructor reassignment)
- feedback: submission_comments (text, media audio/video, files), stickers
- history: submission_history (all attempts)

Grading operations: posted_grade accepts points / percentage / letter grade / pass-fail-complete-incomplete; bulk grade update; gradeable students; anonymous grading endpoints; excuse flag. External tools (LTI) can be the submission type and can return scores into the gradebook (Assignment and Grading Services); scores surface in "Submission Details and SpeedGrader Views". Related resources: Late Policy, Grading Periods, Gradebook History, What-If Grades, Peer Reviews, Moderated Grading, Originality Reports.

### Product B — Assignments in Microsoft Teams (Education) [Evidence layer A]

Observed via official Microsoft Learn admin documentation.

- Positioning: "The Assignments and Grades features in Teams for Education allow educators to assign tasks, work, or quizzes to their students. Educators can manage assignment timelines, instructions, add resources to turn in, grade with rubrics, and more. They can also track class and individual student progress in the Grades tab."
- Entities: Assignment and Submission are first-class (diagnostic data includes Assignment ID and Submission ID). Student files for a Submission are stored in a "Student Work" document library; teacher-provided assignment resources in "Class Files".
- Data split: grades and feedback, the list of submitted documents, and assignment details such as due date are stored outside SharePoint (platform store).
- Guardian loop: weekly guardian email digest of assignments due in the previous/upcoming week; guardian contacts ingested via School Data Sync (CSV/API) or Graph; teachers can opt out per class; default off at tenant level.
- Integrations: Turnitin (academic integrity, per-tenant API key), MakeCode (block-based coding assignments), Reading Progress (first-party).
- Classwork: educators organize class resources (assignments, notebook pages, links, files, channels) into a curated view.
- Lifecycle note: students who left a class may still have assignment data present as "no longer enrolled"; bulk export/delete scripts exist per student.
- Admin control: Assignments/Grades apps can be blocked by policy per user or tenant.

### Product C — Blackboard Learn (Anthology) [Evidence layer A, structure level]

Observed via official help-center hub (sub-pages redirect to hub; only structure treated as observed).

- Instructor help is organized around: Assessments, Grading, Plagiarism Tools, Analytics.
- Assessment settings include: Details & Information; Prohibit Late Submissions and New Attempts After Due Date; Submission Details; Collect Submissions Offline; Presentation Options; Grading & Submissions; Assessment Results; Access Code; Proctored Assessments; Location Restriction; Time Limit.
- Grading includes "Flexible Grading" (grade assessments with a flexible grading interface).
- Interpretation caution: Blackboard Ultra labels much of this surface "Assessments"; the assignment-vs-assessment naming differs from Canvas. The structural elements (due-date rules, submission control, offline collection, grading interface, results) match the Type.

### Product D — Satchel One (Team Satchel) [Evidence layer A]

Observed via official help-center articles (staff side).

- Positioning: standalone homework platform for schools; homework tasks are the core; also class management (attendance, behaviour, detentions, timetables, seating plans).
- Task types: Assignment (submit in class / online via Satchel One / via third-party), Classwork, Flexible task (no submission required), Quiz (auto-marked multiple choice), Spelling test (sound-based), Differentiated (per-group "trays" of instructions), Class test (reminder + revision materials). Task types are color-coded on student to-do lists and tracked separately in reports.
- Assignment form fields: Title; Type; Class groups (one or more; advanced search by name/subject/year); Students (default all, deselect individuals); Subject; Description (or AI-generated via "Sidekick"); Issue date (scheduled visibility — task hidden until issue date); Due date; Issue on lesson / Due on lesson (timetable-linked); Attachments (local or cloud drives; size limit 100 MB); Web links; Submission Method (Class submission / Online via Satchel One / Other — configurable methods); Estimated completion time (default 30 minutes); Marking scheme (school-configurable).
- Publication model: drafts; publish → goes live on the issue date; students AND parents receive automatic notification and see the task on their to-do list/calendar.
- Marking: on the task's "Assess" tab, per student or multi-select: submission status ∈ {Submitted, Submitted Late, Partially Submitted, Absent, Not Submitted} (fixed, non-customizable list); grade from the chosen marking scheme; comments (≤1000 characters, file attachment allowed) visible to the student and their parents. Applying a grade auto-records status as Submitted or Submitted Late depending on the due date. Online submission auto-sets status (Submitted before due date / Submitted Late after / Not Submitted when deadline passes).
- Notifications: students and parents notified on grade/comment and on "Not Submitted"; students can comment back (teacher notified); parents read-only.
- Gradebook: class gradebook view where statuses/grades can also be applied.
- Permissions: `My homework tasks` (setting), `Gradebook` (marking), `My homework comments`.
- Reuse/operations: colleagues can find and reuse each other's tasks (Resources area); drafts; export task as PDF; edit/delete after publish triggers a notification to students/parents; export online submissions ("Download work").
- Reports: Issued tasks, Student submissions, Task insights (per task type).
- AI: "Sidekick" (GPT-based) generates task descriptions from topic + class age + estimated time + subject; optional blooms-taxonomy/debate/objective/differentiated-question options; teacher reviews before publishing.

### Product E — Google Classroom [no direct observation]

Official help center and developer docs were unreachable from the research environment (repeated timeouts). Google Classroom is retained as a market anchor (assignment-centric lightweight platform, dominant in K-12) but no product-specific claims are made. Its exclusion from the evidence base is recorded as a sourcing limitation.

## Cross-product Comparison

| Dimension | Canvas | Teams (Education) | Blackboard Learn | Satchel One |
|---|---|---|---|---|
| Product form | module of full LMS | feature inside M365 Education suite | module of enterprise LMS | standalone homework platform |
| Central object | Assignment (course-scoped) | Assignment (class team-scoped) | Assessment/Assignment (course-scoped) | Task/Assignment (class-group-scoped) |
| Roster source | course enrollments (SIS-importable) | class team membership (School Data Sync) | course enrollments | class groups (school-managed; timetable-linked) |
| Assignment spec | name, description, dates, points, grading type, submission types, attempts, rubric, overrides | instructions, timeline, resources to turn in, rubric | details, submission settings, grading settings | title, description, subject, issue/due dates (+lesson binding), attachments, links, submission method, marking scheme, estimated time |
| Scheduling | due/unlock/lock + per-student/section overrides | due dates; guardian digest window | due date; prohibit-late option | issue date (scheduled visibility) + due date (+ timetable lesson) |
| Submission forms | upload/text/URL/media/annotation/quiz/on-paper/none/external tool | files "turned in" per student; quizzes | submission settings incl. offline collection | in-class / online / third-party ("Other") |
| Submission states | unsubmitted/submitted/graded/pending_review (+late/missing/excused flags) | submission per student with turned-in state; data persists for departed students | submission tracking; results view | Submitted / Submitted Late / Partially Submitted / Absent / Not Submitted (fixed list) |
| Grading | points/percent/letter/GPA/pass-fail/not-graded; rubric; moderated; anonymous; autograders via LTI | rubrics; Grades tab | flexible grading interface | marking schemes (school-defined); status-only marking allowed |
| Feedback | comments (text/media/files), annotations, stickers | teacher feedback stored with submission | grading interface feedback | comments (text + file) visible to student + parents |
| Late handling | late flag, late/missing policy with auto point deduction, seconds_late | due-date-based digest; (details not observed) | prohibit late submissions setting | auto status Submitted Late / Not Submitted |
| Exceptions | excuse, extra attempts, redo request, overrides | "no longer enrolled" data retention | access code, time limit, proctoring (assessment-side) | Absent status; multi-select marking |
| Gradebook | assignment → gradebook column; groups/weighting; grading periods; history | Grades tab tracks class/individual progress | gradebook + flexible grading | class Gradebook view |
| Integrity | Turnitin/VeriCite per assignment; pledge | Turnitin integration (tenant key) | Plagiarism Tools section | (not observed) |
| Parent/guardian | observer role (API: observed_users) | weekly guardian email digest | (not observed at hub level) | live parent visibility + notifications (read-only) |
| Peer review | full (manual/auto, anonymous, intra-group) | (not observed) | (not observed) | (not observed) |
| Group work | group assignments, individual or shared grade | (not observed) | (not observed) | (not observed) |
| Reuse | duplicate assignment | (not observed) | (not observed) | colleague-shared task library; drafts; PDF export |
| Auto-marked types | online_quiz (separate Quizzes engine) | quizzes assignable | assessments with results | Quiz, Spelling test (auto-marked) |
| AI | (AI features exist elsewhere in product; not in assignment docs observed) | (not observed) | AI Conversation (content-side) | Sidekick task generation |
| Reporting | score statistics, needs-grading counts, buckets | class/individual progress in Grades tab | Analytics section | Issued tasks, Student submissions, Task insights |

## Canonical Model (synthesis)

### L0 — Defining Invariant (minimal)

1. **Instructor-authored assignment** — a task specification (title + instructions + completion expectation) created by an instructor within a class context.
2. **Binding to a defined cohort** — the assignment is addressed to the enrolled members of a class/section, not to anonymous or self-selected users.
3. **Per-student submission record** — for each student, a tracked record of their work (or non-submission) against the assignment, carrying state.
4. **Instructor evaluation returned to the student** — the instructor (or an authorized process) records an outcome on the submission — a grade/score, a completion status, and/or feedback — which becomes visible to that student.

Remove any one and the Type collapses: without (1) it is generic task management; without (2) it is a personal to-do or marketplace of tasks; without (3) it is homework broadcasting (a calendar/notice surface); without (4) it is a file-drop/collection box, not assignment management.

### L1 — Common Mature Structure

- due date as the canonical completion expectation (near-universal; some products also support availability windows: unlock/lock dates, scheduled issue dates)
- late-submission handling: automatic late/missing flags, configurable late policies (deduction, prohibit-late), late status in marking
- multiple attempts / resubmission (attempt history; grade-vs-current-submission tracking)
- grading basis options: points, percentage, letter/scheme-based, pass-fail/complete-incomplete, ungraded/completion-only
- rubrics (criteria + ratings driving or advising the grade)
- feedback channels: comments (text/media/file), inline annotations on submitted documents
- submission-type control: file upload (with extension restrictions), text entry, URL, media recording, on-paper/offline, external tool
- gradebook linkage: each graded assignment becomes a gradebook column/entry; categories/weighting; grade posting/publishing controls
- instructor work queues: needs-grading counts, unsubmitted/overdue buckets, per-student status views
- notifications to students (and, in K-12, parents/guardians) on assignment issue and on grading
- reuse: duplication/reassignment of assignments; drafts; shared task libraries among staff
- attachments/resources attached to the assignment
- roles/permissions: teacher, co-teacher/TA/grader, admin; student submit/view; parent read visibility
- reporting: completion/submission reports, task/assignment insights, score statistics

### L2 — Variant / Optional Structure

- product form: standalone homework platform ↔ LMS module ↔ suite-embedded feature
- roster substrate: SIS sync vs school-managed class groups vs course enrollments
- parent/guardian visibility depth: live read-only portal vs periodic digest vs observer role
- timetable integration (issue/due bound to scheduled lessons — regional, UK-style schooling)
- auto-marked task types (quizzes, spelling tests) — overlaps Assessment Platform
- external autograding (LTI tools returning scores; coding autograders)
- differentiated assignments (per-student/section variants, override dates, "trays")
- moderated/multi-grader workflows with provisional grades and anonymity (higher-ed large courses)
- anonymous grading; academic-integrity pledges; plagiarism-service integration depth
- standards/outcomes alignment of assignments and rubrics
- AI-assisted task authoring
- grade sync to SIS; admin-level feature toggles; data-export/retention tooling (privacy compliance)
- mobile apps; offline submission tracking ("collect submissions offline", "on paper", "in class")

### L3 — Vendor-specific (research notes only)

- Canvas: SpeedGrader, buckets (past/overdue/ungraded/...), stickers on submissions, GPA-scale grading type, AssignmentFreezer, Kaltura media, VeriCite, What-If grades, Differentiation Tags, Blueprint courses
- Teams: "Student Work"/"Class Files" SharePoint libraries, weekly guardian digest mechanics (SDS V2.1 CSVs), MakeCode, Reading Progress, tenant app-blocking policies, diagnostic gesture tool
- Blackboard: Ultra "Assessments" naming, Flexible Grading, Access Code, Location Restriction, Respondus LockDown Browser (Canvas also), AI Conversation
- Satchel One: Sidekick (GPT-3.5-based), Neeto quiz engine, fixed five-status list, 100 MB attachment limit, 1000-character comment limit, 30-minute default estimated time, "Issue on lesson / Due on lesson" green/red timetable labels, Welfare Notes/Behaviour/Detentions siblings

## Vendor-specific Findings

- The fixed submission-status list (Satchel One) vs open workflow states (Canvas) is an implementation choice, not a Type property.
- Guardian digest (Teams) vs live parent visibility (Satchel One) vs observer role (Canvas) are three different implementations of the same K-12 transparency need.
- Timetable-lesson binding (Satchel One) is regional (UK school timetabling); not observed in the other samples.
- Moderated grading with provisional graders (Canvas) is a higher-ed large-course workflow; single-product evidence in this sample → Optional.
- AI task generation observed only in Satchel One (Sidekick) → product-specific; treat AI authoring as an emerging optional capability, not a common one (evidence limited).

## Boundary Findings

- **vs Learning Management System (LMS)**: the LMS adds course content authoring/delivery, module/sequence structure, enrollment management, and broader assessment tooling. Assignment Management is the assign→submit→evaluate loop. Test: remove content delivery and course structure from an LMS and what remains is this Type; add those to a standalone homework platform and it becomes an LMS. Most sampled products are LMS modules — the Type describes that module's structure, and Satchel One proves it can stand alone.
- **vs Digital Gradebook**: the gradebook's primary object is the grade record (a grid of students × graded items); assignment management's primary object is the assignment and its submissions. The assignment produces gradebook entries; the gradebook aggregates them. Products bundle both; the boundary is the center of gravity.
- **vs Assessment Platform**: assessment platforms center on item-based tests/quizzes scored automatically (or by rubric) with psychometric concerns; assignment management centers on student-produced work evaluated by an instructor. Overlap exists (auto-marked quizzes as task types; quizzes as submission types). Test: if the primary object is a question bank/item engine delivering scored tests, it is an Assessment Platform; if it is a task bound to a cohort with per-student submissions, it is this Type.
- **vs Task/To-do Management**: the student-facing to-do list is a *view* onto assignments, not the Type. Remove the instructor side (authoring, evaluation, roster) and only a personal task list remains.
- **vs Classroom Management**: classroom management governs the live classroom (devices, behavior, attendance in the moment); assignment management governs work completed across time. Satchel One contains both (behaviour/detentions vs homework) as separate modules.
- **vs Student Information System**: the SIS owns enrollment, demographics, and official records; assignment systems consume rosters and (optionally) post grades back. Roster provenance is an integration, not a core object.
- **vs MOOC Platform**: MOOCs operate at massive, self-enrolled scale with auto/peer assessment; this Type operates on bounded, institution-defined cohorts with instructor evaluation.
- **Historical check**: early "homework publishing" tools (e.g., Show My Homework's original form: a homework calendar visible to students/parents without online submission) lack L0 elements (3) and (4). They are precursors/broadcast surfaces, not full instances of the modern Type. The definition above does not over-fit to them; conversely, the modern collection loop is what the market uniformly implements today. Older LMS assignment modules (due date + upload + grade) satisfy the L0 fully, so the definition is not over-fitted to 2020s lightweight products either.

## Uncertainties

- Google Classroom's exact model (e.g., its assignment/submission state machine) could not be verified from official sources in this environment; it is excluded from evidence-bearing claims.
- Moodle's assignment activity could not be fetched (403); its inclusion would likely only reinforce already-cross-verified findings (due dates, submission types, grading), so the sample was not extended.
- Blackboard evidence is hub-structural; detailed per-setting behavior (e.g., exact semantics of "Collect Submissions Offline") was not verified.
- Teams' student-side submission states and rubric mechanics were not directly documented in the fetched page (admin-focused); claims about Teams are limited to what the admin doc states.
- The relative market weight of standalone vs LMS-embedded forms is not quantified here; no claim about market share is made.

## Final Synthesis

Assignment Management is the classroom work-loop application: an instructor authors an assignment bound to a class roster; each student gets a submission record whose state is tracked; the instructor records an evaluation (grade, status, feedback) on that record and returns it to the student. Everything else — due dates and late policies, rubrics, submission-type controls, gradebook linkage, notifications, parent visibility, peer review, plagiarism checks, reuse libraries, reporting — is mature structure layered on that loop. The Type's product form varies (standalone homework platform, LMS module, suite feature), which is why the defining core must be stated in terms of the loop, not any packaging.
