# Assignment Management

## Overview

An **Assignment Management application** is the instructor-facing system for running the classroom work loop: an instructor creates an assignment (a task with instructions and a completion expectation), distributes it to the enrolled students of a class, collects each student's work as a tracked submission, evaluates it, and returns the evaluation — a grade, a completion status, and/or feedback — to that student.

The defining structure is small:

```text
Instructor-authored assignment
└── bound to a defined class roster
    └── per-student submission record (work + tracked state)
        └── instructor evaluation recorded on the submission
            └── returned / visible to the student
```

Everything commonly associated with the category — due dates, late policies, rubrics, gradebooks, notifications, parent visibility, peer review, plagiarism checks — is standard capability layered on that loop. It makes the loop practical; it is not what makes the product an assignment management application. Remove the loop's two-sided structure (instructor authors and evaluates; students submit) and what remains is either a generic task list or a homework broadcast surface, neither of which is this Type.

## Users & Context

**Primary users:**

- **Instructor / teacher** — authors assignments, chooses the receiving class, sets dates and grading rules, reviews submissions, records grades and feedback.
- **Student** — sees assigned work in a personal to-do/calendar view, produces and submits work, tracks their own status, receives grades and feedback.

**Secondary users:**

- **Co-teacher / teaching assistant / grader** — shares the evaluating role in team-taught or large courses; some products support split grading duties with oversight.
- **School or institution administrator** — configures marking schemes, permissions, integrations (roster sync, integrity services), and feature availability.
- **Parent / guardian** (K-12) — sees the child's assignments, statuses, and feedback, either live or through periodic summaries; read-only.

Typical context: K-12 schools, universities, and online programs running on a term or semester rhythm. The class roster normally comes from an institutional system (student information system or school-managed class groups) rather than being built inside the assignment tool. The capability appears in three product forms: as a module of a full learning management system, as a feature embedded in a productivity/education suite, and as a standalone homework platform.

## Core Model

### The Defining Core

Four objects, tightly bound:

- **Assignment** — the instructor-authored task specification: a title, instructions (often with attached resources or links), a completion expectation (canonically a due date), and a grading basis. It belongs to a class/course context and is addressed to that class's enrolled students.
- **Class roster (cohort)** — the defined set of enrolled students who receive the assignment. Membership comes from enrollment in the course or class group, not from self-selection. This binding is what makes the work classroom work rather than open tasks.
- **Submission** — the per-student record of work against the assignment. It carries the submitted content (or an explicit non-submission), a timestamp, and a tracked state. One submission record exists per student per assignment; many products track resubmissions as numbered attempts.
- **Evaluation** — the instructor's (or an authorized automated process's) recorded outcome on a submission: a score or grade, a completion status, and/or feedback comments. The evaluation is returned to the individual student and, in most products, flows onward into the gradebook.

The submission record is the hinge of the model: it is where the instructor's authoring meets the student's work, where lateness is computed, where feedback attaches, and where the grade originates.

### Standard Capabilities

Mature products commonly add the following around the core. They are what users expect, but a product lacking some of them can still be recognized as this Type.

- **Scheduling** — due date and time; some products add availability windows (when the assignment opens and closes) or scheduled release (authored in advance, visible to students only from a set date).
- **Late-submission handling** — automatic late/missing flags derived from the due date; configurable policies such as point deduction or prohibiting submissions after the deadline.
- **Attempts and resubmission** — some products limit how many times a student may submit and preserve attempt history; a resubmission after grading is tracked against the earlier grade.
- **Grading bases** — points, percentage, letter or scheme-based grades, pass/fail or complete/incomplete, and ungraded/completion-only assignments.
- **Rubrics** — criteria with rating levels that drive or advise the grade.
- **Feedback channels** — comments (text, sometimes audio/video or file attachments); some products add inline annotations on submitted documents.
- **Submission-type control** — what students may hand in: file upload (with extension restrictions), typed text, a URL, media recordings, work produced on paper or in class (tracked without a file), or work completed inside an external tool.
- **Gradebook linkage** — each graded assignment becomes a column or entry in the class gradebook; categories and, in some products, weighting aggregate assignments into course grades; some products also separate grade posting from grading.
- **Instructor work queues** — counts of ungraded submissions, unsubmitted students, and overdue work; per-assignment status views across the roster.
- **Notifications** — automatic alerts to students (and, in K-12, parents) when work is assigned, when grades or comments are left, and when work is missing.
- **Reuse** — duplicating an assignment for another class or term; drafts; in some products, shared staff libraries for finding and reusing colleagues' assignments.
- **Roles and permissions** — who may author, grade, and configure; students see only their own submissions; parents see only their child's record.

### One Structure, Many Implementations

The core model is conceptual; products realize each concept differently:

```text
Concept:  completion expectation
Implementations:  due date + time, availability window, scheduled release date,
                  a timetabled lesson the work is due on

Concept:  submission content
Implementations:  file upload, typed text entry, URL, media recording,
                  in-class / on-paper hand-in (tracked, no file),
                  work completed in an external tool

Concept:  evaluation
Implementations:  numeric points, percentage, letter/scheme grade, pass-fail,
                  completion status only, rubric-scored, automated score

Concept:  roster
Implementations:  SIS-synced enrollments, school-managed class groups,
                  course-section membership
```

A reader who has only seen one implementation — for example, a university LMS with file-upload assignments — should still be able to recognize a standalone K-12 homework platform with in-class hand-ins and status-only marking as the same Type.

## How It Works

### The main loop

```text
Create → Distribute → Work & submit → Evaluate → Return & record → Track
```

**1. Create.** The instructor authors the assignment: title, instructions, attached resources, the receiving class (and, if needed, a subset of students), the completion expectation (due date, availability window, or scheduled release), the grading basis, and the allowed submission forms. Most products keep unfinished work as a draft and require an explicit publish step; publication is the moment the assignment becomes visible to students.

**2. Distribute.** On release, the assignment appears on each enrolled student's to-do list or calendar, and notifications go out (to parents as well, in K-12 products). The instructor sees the assignment in their course's assignment list with its due date and status.

**3. Work & submit.** The student opens the assignment, reads the instructions and resources, produces work, and submits it in an allowed form. The submission record updates: content stored, timestamp recorded, state set. If the due date has passed, the submission is marked late (or refused, if the product enforces a hard deadline). Students who have not submitted remain visible to the instructor as outstanding.

**4. Evaluate.** The instructor works from a queue — submissions needing grading, listed per student. Opening a submission shows the student's work (document preview, text, links, media), where the instructor assigns a score (directly or via rubric) and leaves feedback (comments, annotations). Batch operations let a teacher mark many students at once. Some products allow status-only marking (submitted / late / missing) without a grade.

**5. Return & record.** The evaluation becomes visible to that student (immediately, or when the instructor posts grades). Notifications inform the student — and parents, where applicable. The grade flows into the gradebook as a column entry for that assignment.

**6. Track & report.** Both sides see ongoing state: students see their own statuses and feedback; instructors see completion across the roster, outstanding grading, and — in most products — reports on submissions, completion rates, and task/assignment activity.

### Exception paths

Real classroom work constantly departs from the clean loop, and mature products encode the common departures:

- **Late work** — accepted with a late flag (sometimes with automatic deduction), or blocked after the deadline, depending on configuration.
- **Missing work** — surfaced explicitly as a status so the instructor (and parents) can act.
- **Excused / exempted students** — some products allow a submission to be marked excused so it does not count against the student.
- **Extra attempts and redos** — some products let the instructor allow additional attempts or reassign work; a resubmission after grading is tracked against the prior grade.
- **Individual accommodations** — some products support per-student or per-section due-date overrides for the same assignment.
- **Group work** — some products support a submission shared by a group, graded for the group or for members individually.
- **Departed students** — records of students no longer enrolled typically persist for audit and export rather than vanishing.

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Assignment list / course work view (instructor)

The instructor's overview of work in a class.

- assignments with due dates, publication state, and status summaries (submitted / missing / needs grading)
- primary actions: create assignment, edit, duplicate, open grading, view reports

### Assignment editor

The authoring form.

- title, instructions, resources, class and student selection, dates, grading basis, submission rules
- primary actions: save draft, publish, edit after publication (usually with notification to recipients)

### Grading / submission view

The evaluation surface, per assignment.

- roster of students with per-student submission state; the selected student's work (preview, text, media, links)
- score entry (points or rubric), feedback comments, annotations on documents; batch marking across students
- primary actions: grade, comment, return/redo request, excuse, download submissions

### Gradebook

The aggregate record of grades across assignments.

- grid of students × graded items; category/weight totals; posting controls
- primary actions: enter or adjust grades, post/hide grades, export

### Student to-do / calendar

The student's personal view of assigned work across classes.

- upcoming and overdue items with due dates and task types
- primary actions: open assignment, submit, view status and feedback

### Assignment detail (student)

The per-assignment surface for one student.

- instructions, resources, own submission (content, timestamp, state), grade and feedback once returned
- primary actions: submit or resubmit, comment to the teacher, view rubric/feedback

### Reports / insights

Completion and activity reporting for instructors and administrators.

- submission and completion statistics, per-class or per-task views, export

### Settings / administration

- marking schemes, submission methods, permissions, notification and guardian settings, integrations (roster sync, integrity services)

## Important Rules / Behaviors

- **Two-sided visibility.** The instructor sees every student's submission and status; a student sees only their own. This asymmetry is structural, not a preference.
- **State is derived from time.** Late and missing statuses are computed against the due date (or the student's overridden due date), not entered by hand — although instructors can usually adjust statuses manually.
- **Publication gates visibility.** Draft assignments are invisible to students; publishing (or a scheduled release date) starts the loop. Editing a published assignment typically notifies recipients.
- **Grading is authorized and attributable.** Only roles with grading rights may record evaluations. Automated graders (quiz engines, external tools) may act as delegated graders; some products track whether a grade came from a human or a process.
- **Grades may be held before release.** Grading and posting are often separate steps, letting an instructor finish marking the whole class before students see results.
- **Resubmission supersedes.** A new attempt replaces the working submission; whether the prior grade still stands is tracked explicitly.
- **Roster binding controls access.** Only enrolled students can submit; enrollment changes affect visibility, while historical records persist.
- **The loop tolerates degenerate forms.** Completion-only (ungraded) assignments and task types that require no submission exist as first-class variants; the evaluation step then reduces to a status, but the two-sided record remains.

## Variants

- **LMS module** — assignments live inside a full learning management system alongside content, modules, and enrollment; the assignment model is deepest here (rubrics, external-tool submissions, outcomes alignment, and — in some products — moderated multi-grader workflows).
- **Suite-embedded feature** — assignments inside a broader education/productivity suite; roster and guardian data flow from tenant directory services, and administrators control availability by policy.
- **Standalone homework platform** — the whole product is the assignment loop, oriented to K-12 schools: parent visibility is prominent, marking schemes are school-configured, and work may be bound to timetable lessons; submission may be explicitly in-class or on paper with only the status tracked.
- **Auto-marked task types** — quizzes and similar self-scoring tasks issued through the same assignment machinery; the more a product centers on these, the closer it sits to an Assessment Platform.
- **Regional shapes** — timetable-lesson binding and formal parent portals reflect schooling conventions (notably in UK-style systems); guardian email digests reflect a lighter-touch transparency model.
- **Subject-specific extensions** — code autograding, media submissions, and proctored or access-controlled work appear where disciplines demand them.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Learning Management System / LMS | the broader container: course content, module sequencing, enrollment management; assignment management is one loop inside it. Remove content delivery and course structure from an LMS and this Type remains |
| Digital Gradebook | the grade record is the primary object (a grid of students × graded items); here the assignment and its submissions are primary, and gradebook entries are produced by the loop |
| Assessment Platform | centers on item-based tests scored automatically from question banks; here the object is student-produced work evaluated by an instructor. Auto-marked quizzes are the overlap zone |
| Task / To-do Management | one-sided personal task tracking; the student to-do list is only a view onto this Type. Remove the instructor's authoring and evaluation and only a task list remains |
| Classroom Management | governs the live classroom (behavior, devices, in-the-moment attendance); this Type governs work completed across time between class meetings |
| Student Information System / SIS | owns enrollment and official records; this Type consumes rosters from it and may post grades back to it |
| MOOC Platform | massive, self-enrolled scale with automated/peer assessment; this Type operates on bounded, institution-defined cohorts with instructor evaluation |
| Lesson Planning Application | plans what and how to teach; does not collect and evaluate per-student work |

The closest boundary is with the LMS: most sampled products implement this Type as an LMS module, and the two are frequently conflated. The structural test is the loop — authoring for a roster, per-student submissions, evaluation returned to students — which exists independently of course-content tooling.

## Representative Products

- Canvas LMS (Instructure) — assignments and submissions as a deeply developed LMS module
- Microsoft Teams Assignments (Teams for Education) — assignments embedded in a productivity suite
- Blackboard Learn (Anthology) — long-standing enterprise LMS with an extensive assessment/grading surface
- Satchel One (Team Satchel) — standalone K-12 homework platform
- Google Classroom — widely adopted lightweight, assignment-centric platform (listed as a market anchor; see sourcing note below)

## Sources

Research date: **2026-09-06**

- Canvas LMS REST API Documentation — Assignments API: https://canvas.instructure.com/doc/api/assignments.html
- Canvas LMS REST API Documentation — Submissions API: https://canvas.instructure.com/doc/api/submissions.html
- Canvas LMS REST API Documentation — LTI Assignment Tools: https://canvas.instructure.com/doc/api/file.assignment_tools.html
- Microsoft Learn — Assignments for Teams (Teams for Education): https://learn.microsoft.com/en-us/microsoftteams/expand-teams-across-your-org/assignments-in-teams
- Blackboard Learn Instructor Help (Anthology): https://help.blackboard.com/Learn/Instructor/Assignments
- Satchel One Help Center — Setting tasks: https://help.satchelone.com/en/articles/10669887-setting-tasks
- Satchel One Help Center — Assignment task type: https://help.satchelone.com/en/articles/14079744-assignment
- Satchel One Help Center — Marking tasks: https://help.satchelone.com/en/articles/2905138-marking-tasks

> Sourcing limitation: Google Classroom's official help and developer documentation could not be reached from the research environment on 2026-09-06 (repeated request timeouts), and Moodle's documentation was similarly unreachable. Google Classroom is therefore listed as a market anchor only, with no product-specific claims drawn from it. Blackboard evidence is limited to the help-center structure level. Precise operational details (numeric limits, exact status lists, default values) observed in individual products are intentionally not stated in this document; they are recorded in the paired Research Notes.

Detailed product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
