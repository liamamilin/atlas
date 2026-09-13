# Lesson Planning Application

## Overview

A **Lesson Planning Application** is the teacher's schedule-coupled planning application: it lets a teacher author lesson plans — structured records of intended instruction — place them into their recurring teaching slots across the school year, work from them while teaching, adjust them when reality disrupts the schedule, and carry the accumulated planbook forward from year to year.

The defining structure is small:

```text
Teaching schedule (classes/periods × days across a school year)
└── Teaching occasion (a specific class at a specific scheduled time)
    └── Lesson plan (teacher-authored record of intended instruction)
        └── Plan → teach → adjust → reuse, accumulating year over year
```

Everything else commonly associated with the category — standards alignment, file attachments, templates, sharing with colleagues and administrators, unit planning, analytics, AI drafting — is widespread in current products but is not what makes the product a lesson planner. The paper plan book it replaces — a weekly grid with a handwritten note in each period's box — satisfies the same core with no software at all.

When the center of gravity shifts to institution-level curriculum records, review, and publication, the product is drifting toward Curriculum Management; when it shifts to student-facing delivery and grading, toward a Learning Management System.

## Users & Context

The primary user is a **classroom teacher** planning instruction for the classes they teach — typically K-12, across subjects and grade levels. The work happens in two modes:

- **Planning mode** — ahead of teaching: filling in next week's grid, building units, attaching materials, aligning to standards, preparing substitute plans.
- **Working mode** — during and after teaching: glancing at the day's plan, scribbling adjustments, noting what to change next time, bumping plans when an assembly eats a period.

Secondary users appear in school and district deployments:

- **Co-teachers and grade-level/department teams** — co-planning in a shared planbook, borrowing each other's lessons.
- **Substitute teachers** — consuming a view-only plan for the day.
- **Administrators (principals, instructional coaches, coordinators)** — reviewing submitted plans, leaving feedback, monitoring standards coverage and pacing across teachers.
- **District curriculum staff** — in suite deployments, maintaining the curriculum maps and templates the teacher's planning draws from.

The context is the school year: the application's calendar is the district's calendar, with its terms, holidays, and rotation schedules (A/B days, multi-day cycles).

## Core Model

### The Defining Core

Three structures, held together. Remove any one and the product stops being a lesson planner:

**1. The lesson plan.** A persistent, teacher-authored record of intended instruction for a specific teaching occasion — a class or subject at a scheduled time. It carries pedagogical content: what will be taught and how. The exact sections vary by product and pedagogical framework (objectives, materials, activities and their sequence, assessment, homework, differentiation notes are common), and in many products the plan is simply formatted text in the grid box. What matters is that it is a durable record of instruction intended for that occasion — not a calendar event with a title, and not a document in a folder.

**2. The teaching schedule as the organizing frame.** Plans are not free-floating documents; they live in the teacher's planbook — a calendar grid of the teacher's recurring teaching slots (periods or class blocks × days) spanning the school year, bounded by start and end dates, shaped by the school's rotation scheme, and dotted with non-teaching days (holidays, breaks, closures). Planning is done ahead of teaching, and each plan is coupled to its scheduled occasion: when reality disrupts the schedule — a snow day, an assembly, a fire drill — the plans shift with it rather than being stranded.

**3. The plan→teach→adjust loop with accumulation.** The planbook is worked, not just filled: plans are drafted, refined, taught from, annotated, copied into new units, and rolled into the next school year. Over time the planbook becomes the teacher's planning archive — last year's lessons are this year's starting material.

```text
School year (start/end dates, terms, off days, rotation scheme)
└── Planbook grid (day × period/class)
    └── Teaching occasion
        └── Lesson plan (text + standards + materials, in some arrangement)
            ↓ worked through
    draft → refine → teach → adjust → reuse → next year
```

### Standard Capabilities of Mature Products

These are what a typical modern product adds around the core. They make planning practical; they do not define the Type.

- **Standards alignment** — a library of standards sets (state, national, or framework-specific; some products let teachers write custom sets or upload their own), a search-and-attach action on each lesson, and coverage reporting that answers "have I actually taught this standard?" Notably, at least one established product ships standards **off by default** because not every teacher tags plans — evidence that alignment is a capability, not the definition.
- **Templates and recurring plans** — a repeating weekly schedule built once and reused all year; individual entries that repeat daily or on the rotation cycle.
- **Schedule-disruption machinery** — one-click "bump" that moves a day's plans to the next teaching day and pushes everything after them along; marking a day off with plans bumped in the same step; locking a plan to its date so others route around it; undo.
- **Materials and resources** — files, worksheets, and links attached to lessons; personal resource stores they can be pulled from.
- **Sharing** — view-only links to a week, a day, or a single period (for substitutes and observers); ongoing shares for administrators; collaboration on a shared planbook with a co-teacher or team; private notes that stay private.
- **Administration** — in school/district deployments: teachers "turn in" plans, administrators review and comment week by week, school-wide templates and calendars are imposed, and leadership monitors coverage, pacing, and consistency.
- **Unit planning** — a layer above lessons: units (or curriculum maps, in institution deployments) that lessons belong to, often with backward-design structure (goals → assessments → daily lessons).
- **Output and continuity** — printing a clean week, exporting to Word/PDF, calendar integration (in some products), mobile companions, copying a planbook into a new school year, archiving old ones.
- **AI assistance** (era-current) — drafting lesson plans and units aligned to standards, suggesting differentiation adjustments.

### One Structure, Many Implementations

```text
Concept:   Lesson plan as record of intended instruction
Forms:     formatted text in a grid box · sectioned plan (objectives/activities/assessment) ·
           framework template (IB unit inquiry, UbD stage table) · AI-drafted draft

Concept:   Teaching schedule as organizing frame
Forms:     personal planbook grid the teacher configures (periods per day, rotation) ·
           timetable imported from the school's SIS · school-imposed template calendar

Concept:   Accumulation
Forms:     copy planbook into a new school year · copy lessons into new units ·
           school archive of lessons · district curriculum maps as the reusable layer
```

A reader who has only seen one implementation — say, a solo teacher's web planbook — should still be able to recognize a district suite's lesson-planner module or an international school's planning platform from the core model.

## How It Works

### Set up the planbook

```text
Name the planbook (one per class/section, or one combined)
→ set the school year's start and end dates
→ define the teaching slots (periods per day, their names and order)
→ choose the rotation (plain weekly, A/B days, or a multi-day cycle)
→ mark known non-teaching days (holidays, breaks)
```

From here on, the grid exists: every teaching day of the year has a box for every period.

### Plan ahead

```text
Navigate to a week
→ write (or paste, or template, or AI-draft) the plan into a period's box
→ attach standards, files, and links
→ set recurrence if the plan repeats (daily, weekly, or per rotation cycle)
→ repeat across the week / unit / year
```

Planning is fundamentally forward-looking: the working surface is next week's grid, not a list of past documents.

### Teach and adjust

```text
Open today's (or this period's) plan
→ teach from it
→ annotate what happened (notes, tweaks, what to change next time)
```

### Absorb schedule disruption

```text
A day is lost (snow day, assembly, fire drill)
→ mark the day off, optionally with a reason
→ bump: that day's plans move to the next teaching day,
   everything after shifts along, off days and weekends are skipped,
   locked plans stay put and others route around them
→ undo if wrong
```

This is the behavior most distinctive to the Type: the planbook is a living schedule-coupled document, not a static archive. Repeating plans behave differently from one-time plans under bumping — a plan that happens every Tuesday stays on Tuesday; a one-time lesson slides to the next teaching day.

### Reuse and roll over

```text
Copy a strong lesson into another unit or class
→ build next year's planbook by copying this year's
→ archive the old year
```

### Share and (in institutions) submit

```text
Share a week/day/period with a substitute (view-only link)
→ share the year with a principal or coach
→ co-plan with a teammate in a shared planbook
→ in school deployments: turn in the week's plans → administrator reviews and comments
```

## Interfaces

Described conceptually; exact layouts and names vary by product.

### The planbook grid (week view)

The primary surface — the descendant of the paper plan book.

- days across (usually a school week), periods/classes down (or the transpose)
- each box holds that occasion's plan; standards chips and attachment indicators visible
- primary actions: write/edit a plan, bump a day, mark off a day, navigate weeks/months/years, print

### Lesson editor

Where a plan is written.

- formatted text area (the plan body)
- recurrence controls (once / daily / cycle, with range)
- standards search and attached-standards chips
- file attachments
- visibility extras (hide from shared views; lock to this day)

### Day / month / year views

The same grid at other zooms — a single day for teaching mode, month/year for long-range pacing and finding lessons.

### Standards browser / coverage report

- choose standards sets; search the library
- report of what has been attached and taught, how often, and what remains untouched

### Sharing and administration surfaces

- share creation (who, what date range, how long, read-only or editable)
- administrator dashboard: teacher accounts, turned-in plans week by week, comments
- school-wide template and calendar configuration (institution deployments)

### Unit / curriculum layer (where present)

- unit planner above the lesson grid; curriculum maps at the school/district layer; coverage and pacing analytics

## Important Rules / Behaviors

### The plan is coupled to its occasion

A plan belongs to a scheduled teaching occasion, and the schedule is authoritative: plans land only on teaching days. Weekends, holidays, and marked-off days are skipped by navigation and by bumping. Some products prevent editing days that are not teaching days at all.

### Bumping respects plan semantics

Under a schedule disruption, one-time plans move; plans that repeat on a fixed weekday (an art class every Tuesday) stay put — a Monday closure should not drag Tuesday art to Wednesday; plans locked to a date stay and others route around them. This asymmetry is the schedule-coupling invariant made visible.

### The school year bounds the planbook

Weeks outside the start/end dates do not exist in the planbook. A new year is a new (usually copied) planbook; old years are archived, not deleted. Plans already written stay on their dates if the district calendar shifts — the teacher adjusts the boundaries, not the history.

### Sharing is deliberately scoped

Teachers choose exactly what others see — a single period for an observer, a week for a substitute, the year for an evaluator. Private notes are excluded from shares. In group deployments, administrators may see more than link-based share recipients do.

### Standards are a layer, not a gate

Where standards-based accountability applies, attaching standards to lessons feeds coverage reporting — the answer to "have I covered this?" without rereading the year. But tagging is optional in the defining sense: the Type is fully usable without it.

### Plans are working documents

Drafts are revised in place; deletion is recoverable for a grace period in mature products; undo covers bulk operations like bumping. The planbook tolerates the messiness of real teaching weeks.

## Variants

- **Solo teacher planbook** — the individual teacher's planner, freemium, self-configured grid; no admin layer (e.g., the classic web planbooks).
- **School/district planner with oversight** — the planbook plus turn-in/review workflows, school-wide templates, coaching feedback, coverage monitoring.
- **Platform module** — lesson planning as one surface of a whole-school teaching & learning platform, sitting beneath curriculum maps and beside assessment/portfolio/reporting modules; common in international and independent schools.
- **District suite module** — the lesson planner inside a curriculum & instruction suite, SIS-provisioned, bound to district curriculum maps and academic terms.
- **Framework-specific planning** — IB unit planners (inquiry-centered units above lessons), Understanding by Design backward planning, national-curriculum planning; the lesson-planning loop is intact under each.
- **Rotation-regime variants** — A/B day, A/B week, and multi-day cycle schedules change the shape of the grid, not the model.
- **Delivery-coupled variants** — plans that publish outward to students and families, or push to calendars and LMS tools.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Curriculum Management | adjacent layer above | institution-level records, review, and publication around instruction (programs, courses, curriculum maps, approval); lesson planning is the teacher's schedule-coupled authoring surface beneath it; frequently shipped together |
| Learning Management System / LMS | adjacent layer beside | student-facing delivery — content to learners, assignments, submissions, grades; lesson planning is teacher-facing intention before teaching |
| eLearning Authoring Tool | different object | produces interactive courseware consumed by learners; a lesson plan is a working record consumed by the teacher |
| Educational Content Platform | different loop | distributes lesson plans as content (libraries, marketplaces); no personal schedule-coupled planbook or planning loop |
| Academic Timetabling | upstream neighbor | constructs the institution's master schedule (rooms, teachers, sections); the lesson planner consumes a schedule — its own personal grid or an imported timetable |
| Classroom Management | different time orientation | manages live in-room conduct, devices, and behavior during teaching; lesson planning happens before teaching |
| Assignment Management | different object | issues and tracks student work; a lesson plan records instructional intention |
| Daycare/Preschool Management | different center of gravity | operator-side care and program administration; its learning layer documents the program, it does not give each teacher a working planbook |
| Note-taking / Document Editor | generic substrate | lacks the schedule frame, the teaching-occasion placement, and pedagogical structure; a word processor can hold plans but is not a planner |

The most important seam is with **Curriculum Management**: the two are adjacent layers of one K-12 stack (maps → units → lessons), and many products ship both. The boundary is the center of gravity — the teacher's personal, schedule-coupled planning loop versus the institution's curriculum of record.

## Representative Products

- **PlanbookEdu** — the solo-teacher online planbook; deep public help documentation
- **Common Planner (Common Curriculum)** — collaborative planner with a school/district administration layer
- **Toddle (Curriculum Planning module)** — planning inside a whole-school international platform (IB, British, Cambridge frameworks)
- **PowerSchool Curriculum & Instruction (formerly Chalk)** — the lesson planner inside a district curriculum & instruction suite

The core model was checked against the paper plan book (the predecessor artifact) and against older web-era planners to avoid over-fitting the definition to the current standards-based, AI-assisted market.

## Sources

Research date: **2026-09-08**

- PlanbookEdu — product page https://www.planbookedu.com/ ; training site https://learn.planbookedu.com/home ; Help Center https://help.planbookedu.com/ (including "Planbook basic options", "The lesson editor", "Bump plans forward", "Share with an administrator", "How standards work")
- Common Planner (Common Curriculum) — https://www.commonplanner.com/
- Toddle — https://www.toddleapp.com/ ; Curriculum Planning https://www.toddleapp.com/product/curriculum-planning/
- PowerSchool Curriculum & Instruction (Chalk lineage) — help site https://help.chalk.com/ (section/article structure); chalk.com redirects to PowerSchool

> Sourcing limitation: two market names in this category (Planbook.com, OnCourse Lesson Planner) could not be fetched from the research environment (JavaScript-only site; blocked requests), so no claims about them are made. PowerSchool's help-site article bodies were not retrievable; its evidence is limited to the documented help-site structure. Product-page-depth sources (Toddle, Common Planner) support feature-level claims but not fine-grained operational mechanics.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical sample check are recorded in the paired Research Notes.
