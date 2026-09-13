# Digital Gradebook

## Overview

A **Digital Gradebook** is a teacher-side application for recording the academic scores a class earns on graded work and for computing and tracking each student's grade over a grading term.

The defining structure is a ledger:

```text
Class roster (for a grading scope)
└── Graded items (assignments, tests, projects declared scorable)
    └── Recorded score for each student on each item  → the students × items score grid
        └── Per-student aggregate grade standing, updated as scores accumulate
```

That grid — with a grade standing for every student — is what makes the product a gradebook. Everything else commonly associated with it, such as weighted grading categories, student and parent portals, report cards, standards-based mastery views, attendance, or online assignment collection, is widespread in current products but not part of the defining core: older paper-record-book practice, offline personal tools, and spreadsheet-based gradebooks all satisfy the definition without them.

## Users & Context

**Primary user: the classroom teacher or instructor.** The gradebook is their working ledger for a term: they define what counts, enter scores as work is evaluated, keep the grade standing current, and communicate it. A teacher typically runs several classes at once, each with its own roster, grading scheme, and grade history.

**Secondary users:**

- **School administrators** — configure school-wide grading settings, supply rosters, and read the gradebook's output: final grades, report cards, and school-wide progress views. In school-suite products administrators may also override a final grade or control when grades are released.
- **Co-teachers, teaching assistants, substitutes, and support teachers** — where the product serves a school, access is commonly graduated: view-only access for support staff, score-entry without grade visibility for assistants, short-term access for substitutes.
- **Students and parents** — in most cloud products they are readers, not editors: they see posted grades, missing work, and the running grade through a personal portal.

The work environment is a teacher's desk — planning a unit, marking papers, sitting through a work period — and the term calendar that shapes everything: the ledger is organized around grading periods and closes with a final grade.

## Core Model

### The defining core

Four elements. Remove any one and the product is no longer a gradebook.

- **Class roster** — an identified group of students bound to a course or class for a defined grading scope. The roster is the spine of the ledger: every row is a student, and the roster's source is commonly an import or a school-system sync rather than manual entry.
- **Graded items** — the pieces of work declared scorable for the class: assignments, tests, quizzes, projects, participation. Each item carries a scoring basis (points, a scale, a rubric) and becomes a column in the grid.
- **Score ledger (students × items)** — the grid in which each student's score on each item is recorded. The cell is the atomic unit: it can be filled, corrected, annotated, or marked with a special state (excused, missing, incomplete). The ledger is persistent and revisitable — a teacher can return to any past term and read it.
- **Aggregate grade standing** — the grid exists to produce a per-student grade: a running average or total visible while the term is under way, and a final grade when it closes. The computation may be performed by the system (a weighted average, a points total, a mastery calculation) or by the teacher working from the grid, but the grade standing is the point of the tool. Without it the product is a raw score log, not a gradebook.

### Standard capabilities

Mature products carry most of the following. They make the ledger practical; they are not what makes the product a gradebook.

- **Grading scheme** — how scores become a grade. Common forms include pure points, weighted categories (tests, homework, projects each counting a chosen share), pass/fail and letter scales, custom grade scales, and rubric-based scoring. Many products also offer corrective mechanics: dropping a category's lowest scores, curving an assignment, minimum-grade floors, adjustments and extra credit, and a manual override of the computed grade.
- **Special score states** — cells are not only numbers: missing, late, excused, absent, dropped, and resubmitted are typical states, and products commonly attach policies to them (for example, automatically scoring missing work as zero or applying a late penalty).
- **Grading periods** — the term structure (quarters, semesters, blocks). Each period carries its own grade, and final grades commonly combine them — often with configured weights, such as weighting exam periods more heavily than coursework.
- **Entry surfaces** — the grid is the home view, but scores are commonly entered per assignment (one column at a time), per student (one row at a time while marking), and sometimes from a seating chart; scoring aids such as anonymous grading or grading one question at a time serve marking-heavy work.
- **Visibility control** — a grade is entered before it is seen. Products commonly separate recording from publishing: grades can post automatically or be held until the teacher releases them; some school-deployed products additionally let administrators embargo final grades until a set release date.
- **Student and parent portals** — in cloud products, personal accounts (often provisioned via access codes) where students and parents see posted grades, missing work, and the running grade in real time.
- **Outward reporting** — progress reports and report cards generated from the gradebook, exports (PDF, CSV, spreadsheet formats), and hand-off of final grades to school administration or the student information system.
- **History and safety** — a log of grade changes (who changed what, when), undo or backups for entry mistakes, and year-end rollover that carries settings and reusable assignments forward while archiving past terms.

### One structure, many implementations

The core model is conceptual; products realize it differently:

```text
Concept:        Roster                     → imports, access-code linking, school-system sync
Concept:        Graded item                → assignment columns, tests, rubrics, outcome-aligned work
Concept:        Score ledger               → web grid, offline app tabs, course-gradebook view
Concept:        Aggregate grade standing   → points totals, weighted categories,
                                             teacher-built formulas, standards/mastery standing
Concept:        Grade visibility           → portals, posting policies, printed reports, exports
```

A reader who has only seen one realization — say, a gradebook inside a learning platform — should still recognize a stand-alone teacher app or a paper record book as the same Type.

## How It Works

### Set up the class

```text
Create or receive the class
→ supply the roster (draw, paste, import, or sync it)
→ set the grading scheme (scale, categories, weights, periods)
→ define graded items as the term's work is planned
```

In school-deployed products the class and roster typically arrive pre-populated from the institution, and the teacher links to the gradebook with an access code; solo products let the teacher build this by hand or by import.

### Record scores — the recurring loop

```text
Work is evaluated
→ enter scores (in the grid, per assignment, or per student)
→ apply states where needed (missing, excused, late)
→ the aggregate grade standing updates
→ correct or annotate cells as needed
```

This loop is the gradebook's heartbeat: it runs continuously across the term, scores accumulate, and the standing grade for each student stays current. Where scores originate from online submissions or linked assessment tools, they flow into the same cells.

### Publish and report

```text
Grades recorded
→ release them (automatically, or deliberately posted/held)
→ students and parents see posted grades and missing work
→ at period end: close the period, combine into the final grade
→ generate progress reports / report cards / exports
→ hand final grades to the administration or student information system
```

### Close the term and carry forward

```text
Final grades computed (and overridable)
→ report cards / transcripts produced downstream
→ term archived with its history
→ rollover: settings and reusable assignments carried into the next term
```

## Interfaces

Exact layouts and names vary by product.

### Grade grid (the home surface)

- rows of students × columns of graded items, with a totals/grade column
- per-cell states, colors, and annotations; keyboard entry; sorting and filtering by student, group, period, or status
- primary actions: enter/edit a score, set a status, comment, jump to the assignment or student

### Per-assignment and per-student entry views

- one column or one row at a time, often with the underlying work (a submission, a photo, a rubric) alongside for marking
- primary actions: score, comment, advance to the next student or item

### Grade detail (cell drill-down)

- the full story of one score: the value, its status, its history, comments, and attached evidence
- primary actions: edit score, change status, annotate

### Grading scheme / settings

- scales, categories and weights, periods, missing/late policies, visibility defaults
- primary actions: configure, apply per class or per term

### Reports and exports

- progress reports, report cards, exports and printouts; period-close outputs
- primary actions: generate, customize template, print, export, send

### Portals (where present)

- student/parent view of posted grades, missing work, and the running grade; teacher view of the same data as it will appear to them

## Important Rules / Behaviors

- **Recording is not the same as publishing.** A score entered in the grid is the teacher's working data; what students and parents see is governed by release behavior — automatic posting, deliberate posting, or an administrative embargo on final grades. This separation is a structural feature, not an afterthought.
- **The standing grade is derived, and overridable.** The aggregate grade is computed from the ledger under the class's scheme; teachers can typically override the computed result for an individual student (with any mark or value the scale allows). The override coexists with the calculation rather than replacing the ledger.
- **Not every cell is a number.** Excused, missing, and similar states change how the aggregation treats a cell: missing work may score automatically as zero under a configured policy, and an excused item is typically treated as outside the calculation. The semantics of special states are part of the grading scheme.
- **The roster is upstream.** Students come from imports or institution systems; mid-term roster changes (transfers, drops) preserve the work already recorded rather than erasing it.
- **The ledger outlives the term.** Past terms remain readable, grade changes remain attributable, and final grades persist as the input to report cards, transcripts, and the student record.

## Variants

- **Standalone teacher gradebook** — a self-service ledger for an individual teacher, often free or low-cost, cloud-based (with portals) or sold as a one-time-purchase offline app.
- **Offline personal gradebook/planner** — data kept on the teacher's device; export and import replace portals; integration with learning platforms is optional rather than structural.
- **Gradebook within a school system (SIS)** — rosters, grading settings, report cards, and final grades are institution-controlled; teachers receive pre-populated classes and submit grades to the administration.
- **Gradebook within a learning platform (LMS)** — the grid lives inside the course; columns arise from published course work; scoring tools and outcome views sit alongside.
- **Standards-based grading mode** — the grade standing is expressed as mastery of defined objectives or outcomes rather than (or alongside) a traditional average, with rubric-style scales.
- **Regional and regime variants** — letter, numeric, percentage, and mastery scales; some systems grade without percentages at all. Custom scales are a normal configuration, not an exception.

A variant remains a variant as long as the roster + graded items + score ledger + grade-standing structure holds; packaging differences do not create a different Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Learning Management System (LMS) | host / adjacent | the LMS centers course content and the learning loop; its gradebook is one surface. A gradebook needs no content delivery to be complete |
| Student Information System (SIS) | adjacent | the SIS is the system of record for enrollment, demographics, scheduling, and transcripts; the gradebook is the term-scoped working ledger that feeds it final grades |
| Assignment Management | upstream | the assignment loop (distribute → submit → evaluate → return) produces gradebook entries; the gradebook aggregates them. The primary object differs: assignment + submissions vs the score grid |
| Assessment Platform | upstream | assessment platforms compose and deliver scored instruments and produce scored outcomes; the gradebook is the downstream class-context ledger that records them |
| Transcript Management | downstream | transcripts are the official permanent academic record across years; the gradebook is the working ledger within a term |
| Student Attendance System | bundled capability | attendance recording often lives in gradebook products, but attendance is not a grade ledger; attendance-only products are a different Type |
| Spreadsheet application | common substitute | a generic grid lacks the education semantics (roster, graded items, scales, grade computation, periods); spreadsheets are a common DIY substrate, which is why the Type's definition must not depend on any particular form factor |

## Representative Products

- ThinkWave — standalone cloud gradebook for individual teachers, plus a school-management suite with pre-populated gradebooks
- Jupiter — gradebook-first all-in-one school system for K-12 (gradebook + communications + SIS)
- iDoceo — offline-first gradebook and planner app for iPad/iPhone/Mac for individual teachers
- Canvas (Instructure) — gradebook embedded in a widely used learning platform, higher education and K-12

## Sources

Research date: **2026-09-07**

- ThinkWave — product and FAQ pages: https://www.thinkwave.com/ , https://www.thinkwave.com/educator.html , https://www.thinkwave.com/grades_online.html
- Jupiter — product and gradebook pages: https://www.jupitered.com/ , https://www.jupitered.com/Gradebook_public.php
- iDoceo — product site and feature manual: https://idoceo.net/ , https://idoceo.net/index.php/en/instructions/instructions/idoceofeatures
- Canvas / Instructure — Instructor Guide, "How do I use the Gradebook?": https://community.instructure.com/en/kb/articles/660826-how-do-i-use-the-gradebook

> Sourcing limitation: official gradebook documentation for two other widely used platforms (Google Classroom, Moodle) could not be retrieved from the research environment on 2026-09-07 (request timeouts / access denial). Claims about platform-embedded gradebooks therefore rest on the documented embedded sample above plus its integration surfaces; no details from the unreachable sources were used. Numeric values published by any single vendor (weights, floors, caps) were treated as vendor examples and are not stated as norms in this document.

Detailed evidence, product-by-product observations, and the cross-product comparison are recorded in the paired Research Notes.
