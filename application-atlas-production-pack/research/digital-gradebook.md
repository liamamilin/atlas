# Research Notes — Digital Gradebook

Research date: 2026-09-07
Slug: digital-gradebook
Directory leaf: Digital Gradebook (§23 Education, Research & Knowledge Institutions)

## Research Goal

Understand the Digital Gradebook as an Application Type: its core objects, the recurring workflow of a teacher recording academic performance, how grades are computed and reported, and its boundaries against LMS, SIS, Assignment Management, Assessment Platform, Transcript Management, and generic spreadsheets. Determine what is definitional vs. common-mature vs. variant vs. vendor-specific.

## Initial Boundary

Hypothesis before research:

- Core use: a teacher-side application for recording student academic scores on graded work and computing/track­ing per-student grades over a grading term.
- Primary users: classroom teachers / instructors. Secondary: school administrators; students and parents as readers (in products with portals).
- Nearest neighbors: Learning Management System (LMS), Student Information System (SIS), Assignment Management, Assessment Platform, Transcript Management, Student Attendance System, generic spreadsheets.
- Suspected boundary: gradebook = grade-record-centric (grid of students × graded items + computed grades); LMS = content/delivery-centric; SIS = student-records-of-record-centric; Assignment Management = submission-loop-centric (already framed in the assignment-management research pass: "the assignment produces gradebook entries; the gradebook aggregates them").
- Unknowns: calculation model spread (points vs weighted categories vs standards), whether term structure is definitional, how grades leave the gradebook, whether the gradebook stands as an independent Type given heavy embedding inside LMS/SIS products.

## Research Questions

1. What are the core objects (class/section, roster, graded item, score cell, aggregate grade)?
2. How is the score grid organized and entered (grid, per-assignment, per-student, seating chart)?
3. What aggregation models exist (pure points, weighted categories, subterm weighting, standards/outcomes mastery)?
4. What score states and special marks exist (missing, late, excused, absent, dropped, incomplete)?
5. How do grading periods/terms structure the ledger, and how do final/cumulative grades work?
6. How do grades reach students/parents (posting policies, portals, embargoes) and leave to institutions (report cards, transcripts, SIS)?
7. What roles exist (teacher, co-teacher/TA, admin, substitute, support teacher)?
8. What is the packaging axis (standalone teacher tool vs school SIS module vs LMS-embedded)?
9. Historical check: would a paper gradebook, a spreadsheet-based gradebook, or 1990s desktop gradebook software satisfy the definition?
10. Where exactly do the LMS / SIS / Assignment Management / Assessment Platform boundaries run?

## Representative Products

Selection rationale: market representativeness + documentation completeness + different product philosophies + different customer tiers + different packaging realizations.

| Product | Packaging / philosophy | Customer tier |
|---|---|---|
| ThinkWave | Standalone cloud gradebook; free solo gradebook for individual teachers + school-management suite with pre-populated gradebooks | Individual teacher → small/private schools |
| Jupiter | Gradebook-first all-in-one SIS+LMS for K-12 ("Gradebook Communications SIS") | Public/private K-12 schools and districts (claims scalability to 100,000s of students) |
| iDoceo | Offline-first teacher's personal gradebook/planner app (iPad/iPhone/Mac), one-time purchase, data on-device | Individual teachers/professors; school volume licenses |
| Canvas (Instructure) Gradebook | LMS-embedded gradebook within a course, deep operational documentation | Higher-ed institutions, K-12 districts |

Also attempted: Google Classroom gradebook help (support.google.com — timed out twice; abandoned), Moodle gradebook docs (docs.moodle.org — 403 twice; abandoned). No claims from these products are made below.

## Sources

All fetched 2026-09-07 (webfetch, markdown):

- ThinkWave — homepage https://www.thinkwave.com/ ; Free Online Gradebook https://www.thinkwave.com/educator.html ; Student & Parent access https://www.thinkwave.com/grades_online.html
- Jupiter — homepage https://www.jupitered.com/ ; Gradebook (Public K-12) https://www.jupitered.com/Gradebook_public.php
- iDoceo — homepage https://idoceo.net/ ; Main features https://idoceo.net/index.php/en/instructions/instructions/idoceofeatures
- Canvas / Instructure — Instructor Guide, "How do I use the Gradebook?" https://community.instructure.com/en/kb/articles/660826-how-do-i-use-the-gradebook (plus Grades-category table of contents fetched from the same guide)

Evidence layers used below: **A** = directly observed on the cited official source of a specific product; **B** = cross-product commonality across the researched sample.

## Product Observations

### ThinkWave (evidence: A)

- Positioning: "School Management Software with Integrated Teacher Gradebooks and Free Gradebook"; a free solo gradebook for individual teachers ("does not expire"), a premium gradebook, and a school-management system where "classes and students are pre-loaded" and "teachers link to their gradebook using an access code at the start of the school year."
- Setup flow (official "How it works"): create account → add students and classes → set up classes → input assignments aligned to custom assignment types → grade from anywhere → progress reports/report cards → parent and student access → reports.
- Grading model: "pure points" or "flexible grading" combining points, letter grades, percentages, pass/fail, complete/incomplete, custom grade scales; assignment types (tests, homework, projects, participation, custom) with assignment-type weighting (official example: Tests 30%, Homework 40%, Projects 15%, Participation 15%); subterm weighting ("the semester grade can be calculated from the quarter grades and final exams"); per-class and per-term grading settings; drop-lowest per category.
- Score ledger context: missing-assignment tracking; standards, skills, and behavior recording; attendance; curriculum mapping.
- Roster import: one-at-a-time, cut-and-paste quick add, import wizard from delimited files (addresses, parent data, custom fields).
- Outward flow: student/parent accounts via unique access codes; day-to-day results, attendance, final grades visible in real time; multiple parent accounts per student; parents with several children in one dashboard; progress reports, custom report cards (printable PDF with logo), transcripts, emailed reports; "Final grades are available for the administration"; "School administrator can override attendance and final grade results"; administrator-set embargo dates for final grade release.
- Continuity: year rollover copies students/classes/settings; copy assignments between classes/terms/years; navigate prior-year gradebooks with date stamps on past entries.

### Jupiter (evidence: A)

- Positioning: "Jupiter — Gradebook Communications SIS"; all-in-one for public K-12; "The gradebook teachers love!"; presents itself as full-featured LMS + gradebook + SIS + communications.
- Score entry: scores as Points, Percents, Letter Grades, or Rubrics; entry "by Grid, Assignment, Student, or Seating Chart"; combine sections on one screen; anonymous grading; grade one test question at a time across students; independent-study/differentiated assignments; adjustments written as "25+2" or "40-5%" (extra credit / penalties); override grades with any percent or mark (e.g., INC, W) or raise/lower by a fixed percent; "Backups to undo any mistakes."
- Aggregation: categories (Homework, Tests, …) optionally weighted; any grade scale "with or without percents" (A/B/C/D/F, E/S/N, 4/3/2/1, custom); special marks for excused/missing; configurable minimum score (official example: 50%) "so it's possible to recover from missing assignments or a bombed test"; drop low scores from a category; curve scores on any assignment; cumulative grades across grading periods with optional weights (official example: Qtr1 40%, Qtr2 40%, Final Exam 20%); What-If grades showing the hypothetical grade if missing work were turned in.
- Standards-based mode: grade on multiple learning objectives, or traditional average, or both; Common-Core standards preloaded or custom; mastery chart comparing students' mastery per objective; curriculum map; summative grade; test questions aligned to objectives for automatic standards grading; rubric charts with weighted requirements.
- Outward flow: admins generate report cards and progress reports automatically from gradebooks ("No extra steps required to synchronize grades and comments"); real-time access for admins and support teachers; dashboard graphs of rising/falling grades (intervention), grade distribution with mean/median, and per-assignment grade impact.
- Roles: multiple teachers per section; teachers may view grades of shared students; teaching assistants with limited access ("take roll and/or enter scores without seeing grades"); substitute logins; resource teachers viewing their students across classes; admin restriction controls.
- Transfer handling: "Transfer Grades automatically when students transfer to a different section"; auto-grading of attendance and discussion participation.

### iDoceo (evidence: A)

- Positioning: "Gradebook and planner for Mac, iPad and iPhone"; teacher's personal all-in-one; one-time purchase; "iDoceo is Offline — the data you store in iDoceo stays only on your device… not an online platform nor does it have servers"; optional encrypted cross-device sync via Apple servers.
- Gradebook structure: class with tabbed gradebook pages ("Organize your data visually with tabs… represent some columns in different tabs at once"); columns with specialized editors per task type (grades, numbers, attendance, icons, colors); double-tap to edit a cell; copy/move/edit columns; icons, text, or colors on any cell; color rows/columns/cells; extensive annotations, files, audio, video, photos attachable to any cell; replicate a class's structure; keep old classes hidden.
- Calculation: "Excel like calculations (weighted averages, additions, conditions, icon counters, coefficients, formulas, etc.)" — simple averages or complex formulas configured by the teacher.
- Outward flow: export full gradebook pages to PDF, XLS, CSV; import students from CSV/XLS/XLSX; configurable student report (summary of grades, attendance, personal details); print; bulk personalized e-mails.
- Surrounding teacher tooling: seating plans (up to 10 per class, attendance taken from the plan), diary/planner/schedule/calendar, rubrics (own or from an online library), random student groups.
- Integration: sync with Google Classroom, Moodle ("Publish your iDoceo assessment results or load any data in your Moodle Gradebook"), MS Teams; optional "iDoceo Connect" service to publish exams/rubrics to students via browser.

### Canvas Gradebook (evidence: A)

- Structure: course-level grid; "The default view… view all students at a time"; "Each column in the Gradebook represents a published assignment"; only graded and published assignments display. Rows = students (with secondary/SIS ID optionally displayed; a "Test Student" row from course student-view).
- Grade display types per assignment: points, percentage, complete/incomplete, GPA scale, letter grade; grades typed directly into the cell, or via a Grade Detail Tray (enter/edit grade, change submission status, leave comments); keyboard shortcuts; optional "Individual Gradebook" (one student × one assignment at a time, screen-reader accessible); "Learning Mastery Gradebook" view for outcome standards; "Gradebook History… logs recent grade changes… according to student, grader, assignment, and date."
- Aggregation: assignment groups created on the Assignments page, optionally weighted ("If your assignment groups are weighted, the weighted grade displays below the group title"); "Grade totals from assignment groups are calculated in the Total column"; totals viewable as percentage or (if unweighted) points; "Final Grade Override" lets an instructor enter an override grade different from the calculated one; "View ungraded as 0" is explicitly a visual change only.
- Policies: Missing Submission policy (automatically apply a grade for submissions labeled Missing — due date passed, not submitted); Late Submission policy (automatically apply a penalty; optional under-threshold floor); Grade Posting Policy — automatic post vs. manual post/hide, set per course or per assignment (posting is a deliberate act that makes grades visible to students); status colors for late, missing, resubmitted, dropped, excused.
- Column operations: sort by grade/status; open SpeedGrader; message students matching criteria; curve grades; set default grade; hide/post grades; enter grades as a specific value (convenience only); download/re-upload submissions; per-assignment posting policy.
- Filters: sections, grading periods, assignment groups, modules, student groups, status, submissions. Grading periods are a course structure ("How do I use grading periods in a course").
- Bulk: import/export grades via CSV (imported assignments auto-publish); columns auto-added for Attendance tool; non-submission (on-paper) assignments create manual columns; assignments can be set up "to be sent to my institution's student information system (SIS)".
- Multi-grader note (official): with multiple graders, Gradebook data is cached in the browser until refresh; changes by other graders are not dynamically reflected.

## Cross-product Comparison

| Dimension | ThinkWave | Jupiter | iDoceo | Canvas |
|---|---|---|---|---|
| Unit of work | class (roster) per term, multiple classes in one gradebook | class section per term | class with tabbed gradebook pages | course (sections filterable) |
| Roster source | manual / quick-add / import wizard; pre-loaded by school admin (suite) | SIS roster (own SIS), Clever sync | CSV/XLS import; manual | course enrollments (SIS-fed); SIS ID display |
| Score grid | gradebook grid per class | grid + per-assignment + per-student + seating-chart entry | grid with typed column editors | grid + individual view + SpeedGrader |
| Score forms | points, letters, percent, pass/fail, custom, check-marks | points, percents, letters, rubrics; adjustments "25+2"/"40-5%" | grades, numbers, icons, colors, text | points, percentage, complete/incomplete, GPA scale, letter grade |
| Aggregation | pure points or assignment-type weighting; subterm weighting; drop lowest | weighted categories; drop lowest; curve; minimum score floor; cumulative across periods with weights | teacher-built formulas (weighted averages, conditions, coefficients) | weighted assignment groups → Total column; final grade override |
| Special states | missing tracked; attendance | excused/missing special marks; What-If grades | cell-level annotations/icons; attendance | late, missing, resubmitted, dropped, excused; missing/late auto-policies |
| Grading periods | terms/subterms, rollover per year | grading periods with cumulative weights | tabs/pages; teacher-managed | grading periods (filter/weight structure) |
| Visibility to learners | student & parent accounts via access codes; real-time | students & parents see homework/grades on one screen; missing-work reminders | none by default (offline); optional iDoceo Connect publish | posting policy (auto vs manual post/hide) per course/assignment |
| Outward flow | progress reports, report cards, transcripts; admin override + embargo | report cards/progress reports auto-generated from gradebook; admin real-time access | PDF/XLS/CSV export; student report PDF | CSV import/export; post to SIS; Gradebook History audit |
| History/audit | date stamps on past entries; rollover archives | backups/undo | teacher-managed (device) | Gradebook History (student, grader, assignment, date) |
| Standards mode | standards & skills recording | first-class standards/objectives mode with mastery charts | rubrics; icon-based assessments | Learning Mastery gradebook (outcomes) |
| Attendance | yes | yes (auto from login too) | yes (also from seating plan) | Attendance tool creates a column |
| Offline capable | no (cloud) | no (cloud) | yes — fully offline | no (cloud) |

## Abstraction

### Level 0 — Defining Invariant

The smallest structure without which the product stops being a gradebook:

```text
Class/course context with an identified student roster (for a defined grading scope)
└── Graded items (assignments/assessments declared scorable)
    └── Recorded score per student per item  → the students × items score grid (the ledger)
        └── Per-student aggregate grade standing derived from the recorded scores
            (tracked and updated as scores accumulate over the term)
```

Four properties:

1. **Roster-anchored class context** — the ledger is organized around a specific group of identified students in a course/class for a grading scope. Without it, there is no "who is being graded."
2. **Graded items** — the work being scored is declared as scorable entries (assignment/test/project columns). Without it, there is nothing to record.
3. **Score ledger (students × items)** — the defining object: a persistent grid in which each student's score on each item is recorded, revisitable, and correctable. Without it, the product is not a grade record.
4. **Aggregate grade standing** — the grid exists to produce and track a per-student grade outcome (running average/total/mastery standing, and an end-of-term grade), whether computed by the system or by the teacher working on the grid. Without it, the product is a mere score log (a marks register, not a gradebook).

**Historical / market-sample check:** the paper teacher's record book (roster rows × assignment columns, running totals, quarter/final grade), spreadsheet-maintained gradebooks, and 1990s desktop gradebook software all satisfy these four properties without portals, weighting, standards, attendance, or online submission. Conversely, strip any one property and the Type dissolves: no roster → generic table/spreadsheet; no graded items or ledger → attendance/notes tool; no aggregate standing → raw score log. L0 survives the check.

### Level 1 — Common Mature Structure

Present across the sampled products (evidence B unless noted) but not definitional:

- Multiple entry surfaces beyond the grid: per-assignment, per-student, seating-chart, speed-grading (Jupiter, Canvas, iDoceo partially)
- Categories/assignment types with optional weighting; alternative aggregation paradigms (pure points, weighted categories, standards/outcomes mastery, teacher-built formulas)
- Grade scales and display forms (letters, percents, pass/fail, GPA, custom scales, rubrics) and special marks (excused, missing, incomplete)
- Score states and policies: missing/late/excused/dropped/resubmitted states; automatic missing/late policies; minimum-score floors; drop-lowest; curves; adjustments and extra credit; grade overrides
- Grading periods/terms structuring the ledger; per-period grades; cumulative/final grades with weights; year rollover and assignment reuse
- Controlled visibility of grades to students/parents: posting/hide policies, portals with access codes, embargo; real-time progress view
- Outward reporting: progress reports, report cards generated from the gradebook, exports (CSV/PDF/XLS), submission to SIS, administrator override
- Audit/continuity: grade change history (by student/grader/assignment/date in Canvas), backups/undo (Jupiter), date-stamped archives (ThinkWave)
- Roster supply: import wizards, SIS/LMS/platform sync, access-code linking

### Level 2 — Variant / Optional Structure

- Packaging realization (the dominant variant axis): standalone teacher tool (ThinkWave free solo, iDoceo), gradebook-first SIS (Jupiter), LMS-embedded (Canvas), school-suite module (ThinkWave Administrator)
- Offline vs cloud posture (iDoceo offline on-device vs the rest cloud)
- Standards-based grading as an alternative paradigm (objectives/mastery vs traditional average — Jupiter supports both; Canvas via outcomes; ThinkWave records standards/skills)
- Online assignment distribution/collection attached to the gradebook (drift toward Assignment Management)
- Attendance, behavior, seating plans, planner/diary bundled into the teacher tool
- Multi-teacher/moderation structures (co-teachers, TAs with limited access, substitutes, anonymous grading) — stronger in school/SIS and higher-ed products
- Regional grading regimes (letter vs numeric vs mastery scales; custom scales "with or without percents")
- Business models: free teacher tier, one-time purchase, school site license, district SaaS

### Level 3 — Vendor-specific (Research Notes only)

- Jupiter: Paste Blocker/Lockdown anti-cheating, animated stickers on graded work, Juno online tests/pods, "grade impact" graphs, NYC DOE packaging
- Canvas: Submission Stickers, Test Student row, Mastery Paths, browser-cache behavior with multiple graders
- ThinkWave: 25 MB file cap (free tier), 100 GB premium storage, ad-free premium tier, custom-designed report card templates
- iDoceo: Grade Scanner / Classroom Teammates companion apps, iDoceo Connect, icon-value assignments to cells, chatGPT/DALL-E integration
- Numeric weights/thresholds cited above (e.g., 40/40/20, 50% floor) are the vendors' own examples, not norms

## Rejected Findings (considered for the core, rejected)

- **Online student/parent portals** — not definitional: iDoceo has none by default; paper-era gradebooks never had them. Common mature structure only.
- **Weighted categories** — one aggregation option among several (pure points, formulas, standards mastery); not definitional.
- **Standards-based grading** — a paradigm variant present in some products; a traditional-average gradebook remains a gradebook.
- **Attendance / behavior / seating plans** — bundled teacher-tooling; absent from some products; not definitional.
- **Online assignment collection** — Assignment Management drift; gradebooks work fully as ledgers without it.
- **Multi-period cumulative weighting** — structural refinement of the grading scope, not the invariant itself.
- **Report cards/transcripts** — outward reporting artifacts; their generation is common but the gradebook remains one without them.

## Boundary Findings

- **vs LMS**: an LMS centers course content delivery and the learning loop; its gradebook is one surface. The gradebook's primary object is the score ledger, not content. Strip the roster × items ledger with computed grades and keep content/modules → LMS. A gradebook with no content delivery (iDoceo, ThinkWave solo) is still fully a gradebook. Evidence: Canvas documents the Gradebook as a view within a course; iDoceo needs no course content at all.
- **vs SIS**: the SIS is the system of record for enrollment, demographics, scheduling, transcripts. The gradebook is the working ledger during a term; its final grades flow to the SIS/administration (ThinkWave: "final grades are available for the administration"; Canvas: assignments "sent to SIS"; Jupiter: report cards generated from gradebooks). Keep the student record and demote grades to a field → SIS.
- **vs Assignment Management**: the assignment loop (author → distribute → submit → evaluate → return) produces gradebook entries; the gradebook aggregates them. Primary object test already established in the assignment-management pass: gradebook = grade record (grid); assignment management = assignment + submissions. Consistent with what this research observed (ThinkWave/Jupiter bundle both; the boundary is the center of gravity).
- **vs Assessment Platform**: assessment platforms compose/deliver scored instruments to a taker population and produce scored outcomes (item analysis, psychometrics); the gradebook is the downstream class-context ledger that records those outcomes (Canvas LTI tools return scores into the gradebook; iDoceo imports from quiz apps). Remove the class/term grade-standing context and keep instrument delivery → assessment platform.
- **vs Transcript Management**: transcripts are the official permanent academic record across years; the gradebook is the term-scoped working ledger that feeds them.
- **vs Spreadsheet**: a generic grid lacks education semantics (roster identity, graded items, scales, grade computation, terms, portals). The Type's value is pre-built semantics; spreadsheets remain a common DIY substrate (which supports keeping the definition implementation-neutral).
- **"Remove what to become another Type"**: remove the roster/graded-items/aggregate-grade structure → generic table; remove the aggregate grade standing but keep submissions → assignment collector; remove class context but keep scored instruments → assessment platform; keep only the student-of-record side → SIS.
- **Type independence**: although a large share of the market realizes the gradebook as an embedded module (LMS/SIS/suite), standalone gradebook products persist across tiers (free solo web gradebook, offline paid app, gradebook-first SIS), and their structural cores match the embedded realizations. The leaf stands as an independent Type; embedding is a packaging variant, not evidence of being merely a capability.

## Uncertainties

- Google Classroom and Moodle gradebooks could not be fetched (timeouts/403); statements about platform-embedded gradebooks rely on Canvas as the embedded sample plus Canvas's own LTI/SIS integration surfaces. Assertion strength for the "platform-embedded" pole is correspondingly reduced (single embedded sample observed).
- Exact numeric behaviors (weight examples, minimum-score floors, storage caps) are vendor-published examples, not market norms; no numeric claims were generalized.
- Degree of SIS write-back standardization (grade-posting formats) was observed only via Canvas SIS-sending documentation and Jupiter/ThinkWave native SIS behavior; precise data formats were not researched.
- Relative market share of embedded vs standalone realizations is unquantified; the research established existence and structural equivalence of both, not proportions.

## Final Synthesis

The Digital Gradebook is the teacher-side academic-score ledger. Its defining core is a class roster bound to a grading scope, graded items declared over that class, a persistent students × items score grid recording each student's scores, and a per-student aggregate grade standing computed from those scores. Everything that makes modern products feel complete — weighted categories, grading periods with cumulative finals, missing/late policies, special marks and overrides, student/parent portals with posting controls, report cards, standards-based mastery views, attendance and seating tooling, imports/exports and SIS write-back — is mature structure layered on that ledger, and each of those layers is absent in some legitimate member of the Type (paper-era, offline, solo). The product form varies from offline teacher-planner apps to gradebook-first SIS suites to LMS views, which is why the definition must be stated in terms of the ledger and the grade standing, not any packaging.
