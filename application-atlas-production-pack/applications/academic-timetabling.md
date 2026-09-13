# Academic Timetabling

## Overview

An **Academic Timetabling** application is the institution-side scheduling system for teaching. It holds the set of teaching activities an academic term must deliver — course sections, lessons, classes — together with the staff and spaces that serve them and the time structure of the term, and it assigns each activity to time slots and resources so that no resource is double-booked. The resulting timetable is a persistent institutional artifact that is published to staff and students, then maintained as reality diverges from the plan during the term.

The defining core is small:

```text
Teaching activities to be placed
└── shared, availability-constrained resources (staff, rooms, student groups)
    └── a term/week time structure
        └── conflict-checked assignment → the timetable
            └── publication to the institution
```

Everything else commonly associated with timetabling — automated solvers, preference levels, what-if scenarios, mobile apps, substitution offices, exam scheduling — is widespread in mature products but is not what makes a product a timetabling system. A tool without activities to place, without shared resources, without a time structure, without conflict checking, or without a published schedule would not be recognizable as academic timetabling.

## Users & Context

The primary operators are institutional scheduling staff, not teachers or students:

- **central timetabling / registrar office** — owns the institutional schedule, runs generation, resolves cross-department conflicts, controls publication
- **department or faculty schedulers** — enter and maintain the activities of their own department, place and adjust their classes, coordinate over shared rooms and shared staff
- **school administrators** (in schools) — build the master timetable, then run the weekly substitution/cover process

Secondary consumers, who usually see the timetable rather than build it:

- **instructors** — view their personal schedule; in some products submit availability and preferences
- **students** — view their personal or cohort timetable through portals and mobile apps
- **facilities / room booking staff** — book leftover space against the same room inventory

The work context is cyclical: a major build cycle before each term or school year, followed by a continuous in-term maintenance loop (absences, room changes, one-off events) until the term ends and the next cycle begins.

## Core Model

### The Defining Core

**Teaching activity.** The unit of demand: a recurring instructional meeting that must take place — a course section with its meeting pattern, a school lesson, a lecture/laboratory/recitation session. An activity carries its teaching load (how long and how often it meets per week), its attached staff, its space needs, and the student group it serves. In higher education, activities are typically organized under course offerings and their section groups; in schools, lessons belong to classes (fixed cohorts) and subjects.

**Shared, constrained resources.** The things an activity consumes and cannot share at the same time:

- **instructors / staff** — each with availability, and in mature products with preferences and workload limits
- **rooms / spaces** — each with a capacity, availability, and often features (equipment, layout) and groupings
- **student groups** — classes, cohorts, or enrolled student bodies, which likewise cannot be in two places at once

Rooms are commonly a shared institutional inventory: multiple departments may draw on the same pool, with rules about who controls a room and when.

**Time structure.** The schedulable canvas: an academic term or school year, divided into a weekly grid of teaching periods or time slots, with patterns for how activities meet (which days, how many minutes, which weeks of the term). The grid is institution-defined, not personal.

**Assignment — the timetable.** The central object: the placement of every activity into time slots bound to resources. A placement is valid only if it violates no hard constraint. The timetable is persistent, versioned through the build cycle, and survives into the term as the operational schedule of record.

**Publication.** The timetable exists to be consumed. Once placed, it is released to the institution: staff and students see their personal schedules derived from it, and downstream systems consume it. An unpublished timetable is a private draft, not an operational schedule.

### Constraints and Preferences

Placement is governed by a rule model that all mature products express in some form:

- **hard constraints** — violations are not allowed: no instructor in two places at once, no two activities in one room at once, no cohort double-booked, room capacity, room and staff availability
- **soft preferences** — satisfied where possible and reported where violated: preferred times and rooms, back-to-back or spread-out arrangements, minimizing student clashes between popular course combinations, avoiding long gaps
- **distribution rules** — relationships between activities (same time, same room, consecutive sessions, ordering)

Preferences attach at multiple levels — to an individual activity, to its instructor, to a group of activities — with more specific settings taking priority over general ones.

### Standard Capabilities

Mature products commonly add, without these being part of the definition:

- **automated generation** — a scheduling engine that computes a complete, conflict-free placement from the activities, resources, and rules (solver-first in some products, an optional mode in others)
- **interactive editing** — manual placement and adjustment on the grid, with the system continuously checking clashes and suggesting alternatives
- **conflict reporting** — clash lists, student-conflict counts, utilization and room-allocation reports
- **data exchange** — import of courses, staff, students, and rooms from the student information system; export of assignments back
- **multi-user collaboration** — central office and departmental schedulers working on one schedule with role-based scope
- **what-if evaluation** — trying a placement or a policy change and seeing the resulting conflicts before committing
- **publishing surfaces** — web portals, mobile apps, personal timetables, change notifications
- **in-term change management** — substitutions and cover for absent staff, room moves, cancellations, propagated to everyone affected
- **rollover** — carrying activities, rooms, and rules into the next term or year as the starting point
- **adjacent booking** — one-off room and event bookings checked against the same inventory the teaching timetable uses

## How It Works

The work moves through one defining cycle and one defining loop.

### The build cycle (before the term)

```text
Assemble input
→ activities (from the curriculum / SIS), staff, rooms, student groups
→ define constraints and preferences
→ generate a placement (automated) or place activities manually
→ inspect conflicts and quality reports
→ adjust interactively until acceptable
→ publish / commit the timetable
```

Input assembly is usually an integration task: courses and enrollments come from the student information system, rooms from the facilities inventory, staff from HR. The scheduling office then expresses the rules — which times and rooms are required, preferred, or excluded for which activities, and how activities relate to each other.

Generation and manual editing are complementary poles, and every researched product offers both in some combination. A generation run computes a complete placement and reports what could not be placed and why — typically which resource was over-demanded. Manual editing then adjusts: the scheduler moves an activity and the system shows the resulting clashes, the alternatives that would resolve them, and what else would need to move. In higher education, generation may also include placing students into sections of multi-section courses to minimize predicted clashes.

Review is report-driven: room allocation, violated preferences, student conflicts, and utilization tell the scheduler whether the timetable is acceptable, not just feasible.

Publication is an explicit act with consequences: once released, the assignments become visible to other schedulers and to consumers, conflicts with other departments' choices become real, and further changes flow through a controlled path rather than silent edits.

### The in-term loop (during the term)

```text
reality diverges (absence, room outage, one-off event)
→ scheduler records the change
→ system proposes compliant options (cover teacher, free room, new slot)
→ scheduler chooses
→ change propagates to published timetables, notifications, and records
```

In schools this loop is a named daily workflow: enter who is absent, receive suggested cover, publish the day's substitutions, and have every affected student's and teacher's schedule update. In universities it appears as managed changes to the committed schedule — room moves, cancellations, one-off bookings — each checked against the same constraints as the original build. The loop is what keeps the timetable the schedule of record rather than a term-start snapshot.

### The rollover (between terms)

The next cycle starts from the last one: activities, rooms, rules, and often the previous placement are carried forward as templates, edited for the new term, and the cycle repeats.

## Interfaces

### Timetable grid

The primary working and viewing surface: a week (or term) grid of time slots, rendered per resource — one grid per room, per instructor, per class or cohort — or as the whole institution's schedule. Cells hold the placed activities; color and markers express preference satisfaction, conflicts, or publication state. Primary actions: inspect a placement, open an activity, move or reassign it.

### Activity lists and detail editors

Lists of the activities to be scheduled (offerings, sections, lessons) with their requirements and current placement. The detail editor is where an activity's meeting pattern, staff, space needs, limits, and preferences are defined. Primary actions: create/edit activity, attach staff and rooms, set time and room preferences.

### Constraint and preference editors

Time-grid editors in which availability and preference levels are painted onto days and slots — required, preferred, discouraged, prohibited — for activities, staff, and rooms; plus editors for relationships between activities. Primary actions: set levels, define distribution rules.

### Generation console and conflict reports

The surface where automated generation is run and watched: progress, what was placed, what could not be placed and which constraint blocked it. Alongside it, the report set: clash lists, student conflicts, violated preferences, room utilization. Primary actions: run/stop generation, drill into unplaced activities, open reports.

### Publication and consumer surfaces

The staff/student-facing side: personal and cohort timetables on web and mobile, change notifications, calendars. In schools, the substitution view (today's cover arrangements) is a distinct consumer surface. Primary actions: view my schedule, subscribe, receive changes.

### Substitution / cover console (school variant)

The in-term operations surface: absentees in, cover suggestions out, one-click publication of the day's changes. Primary actions: record absence, choose cover, publish substitutions.

## Important Rules / Behaviors

### No double-booking is the fundamental invariant

The same instructor, the same room, and the same student group cannot host two activities at the same time. Every behavior in the product — generation, manual editing, booking, substitution — is checked against this. Products differ in whether they block violations outright or allow them as flagged exceptions during drafting, but the rule itself is universal.

### Hard constraints and soft preferences behave differently

Hard constraints (capacity, availability, clashes) bound what placements are legal. Soft preferences shape quality and are reported when violated, not blocked. A timetable can be legal yet poor; the reports exist to expose the gap.

### More specific settings override general ones

Preferences attach at several levels (activity, instructor, activity group). When levels conflict, the more specific setting wins. This is what lets an institution express both general policy and individual exceptions.

### Publication is a state change, not a save

Draft placements are working objects; publishing (committing) them makes them visible to other schedulers and consumers, and makes conflicts with already-published schedules real. After publication, changes still happen — but through the controlled in-term path, and they propagate: a room move or a cover arrangement updates every affected personal schedule and notification feed.

### The timetable constrains adjacent bookings

One-off room bookings and events are checked against the teaching timetable's occupancy of the same rooms — the teaching schedule has priority, and ad-hoc use fills the gaps.

### Unplaced activities are first-class problems

When generation cannot place an activity, the product does not silently drop it: it is listed, with the conflicts that blocked it, until the scheduler resolves the over-demand by changing requirements, freeing a resource, or accepting a violation.

## Variants

- **Higher education timetabling** — activities are sections of course offerings with meeting patterns; scale runs to tens of thousands of students; scheduling is often distributed across departmental schedulers coordinating over shared rooms and staff; student sectioning (placing students into sections to minimize clashes) may be part of the same system; exam timetabling is a frequent sibling module.
- **School (K-12) timetabling** — classes are fixed cohorts; the master timetable assigns lessons to a period grid; the in-term substitution/cover office is a first-class daily workflow; publication targets students and parents directly.
- **Exam timetabling** — the same core pattern applied to examinations: exams placed into non-overlapping exam periods and rooms (with exam-specific seating capacity), minimizing direct clashes, back-to-back sequences, and students with too many exams in one day; invigilator assignment often included. In the researched sample it always appears as a module or extension of a timetabling product rather than a separate purchase.
- **Solver posture** — solver-first products (generation is the primary act, editing refines it) vs interactive-first products (manual placement is primary, generation assists) vs generator-plus-AI-assistant products (natural-language changes to data and placements).
- **Deployment and packaging** — desktop single-user applications, client-server installations, cloud/SaaS services, and timetabling embedded in a wider school platform (class register, attendance, communication) or interfaced as a satellite to a student information system.

A variant remains a variant while the defining core still applies; a product whose primary object is not the teaching schedule (for example, a pure room-booking tool, or a shift scheduler for staff) belongs to a different Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Course Registration System | downstream / upstream partner | registration captures student-side demand (which sections students take); timetabling constructs institution-side supply (when and where sections meet); course requests feed timetabling, published sections feed registration |
| Curriculum Management | upstream input | defines what courses and programs exist (the catalog); timetabling places them in time and space |
| Student Information System / School Management System | container or data partner | system of record for students, staff, courses; timetabling is either a module inside it or a specialized satellite exchanging data with it |
| Resource Calendar / Room Booking | capability inside the Type | generic space booking lacks the teaching-activity model (curricula, cohorts, teaching loads); timetabling products embed room/event booking against the same inventory |
| Calendar Application | different object | personal time display and appointment management; no shared-resource conflict model, no institutional construction |
| Employee Scheduling Platform | shared pattern, different domain | also assigns people to time slots under availability constraints, but the objects are work shifts, not curriculum-attached teaching activities serving student cohorts |
| Event Management Platform | adjacent | one-off events vs the recurring teaching schedule; timetabling products typically include event/room booking as a capability |
| Learning Management System | downstream consumer | LMS delivers teaching; the timetable determines when and where it meets |

The most important boundary is with **Course Registration**: the two interlock around the same sections, but the direction of work differs — registration asks "which sections do students take?", timetabling asks "when and where do all sections meet without conflicts?" A product can contain both (some do), but the scheduling-construction loop is what defines this Type.

## Representative Products

- **UniTime** — open-source university timetabling (Apereo): solver-first, distributed departmental scheduling, course and exam timetabling, student sectioning, event management
- **Celcat** — commercial timetabling for universities and colleges (UK/international): interactive-first with automated scheduling, publishing, room booking, exam scheduling
- **aSc Timetables** — school timetabling used worldwide: automatic generator, substitution/cover workflow, publishing to web and mobile
- **Untis** — European school timetabling platform (Untis/WebUntis): timetable core with substitution planning, room planning, class register, and mobile publication

The defining core was checked across these four deliberately different positions (higher-ed vs school, open-source vs commercial, solver-first vs interactive-first, standalone vs platform-bundled) to avoid over-fitting the definition to any one market's implementation.

## Sources

Research date: **2026-09-06**

- UniTime — https://www.unitime.org/ ; online documentation https://help.unitime.org/documentation ; Course Timetabling Solver Manual https://help.unitime.org/manuals/courses-solver ; Course Timetabling Data Entry Manual https://help.unitime.org/manuals/courses-entry ; Examination Timetabling Manual https://help.unitime.org/manuals/examination-timetabling
- Celcat — https://celcat.com/ ; Interactive Timetabling https://celcat.com/timetabler/features/interactive-timetabling/ ; FAQs https://celcat.com/faq/
- aSc Timetables — https://www.asctimetables.com/
- Untis — https://www.untis.com/

> Sourcing limitation: operational help-center documentation was reachable for UniTime (manual-level detail). For Celcat, aSc, and Untis, evidence is limited to official product pages and FAQs (feature existence and positioning, not internal manuals): the Celcat support portal requires login, the aSc help URL was not reachable, and the Untis help center timed out during research. Claims about those products are therefore kept at feature level, and no precise numeric limits, defaults, or internal workflows are asserted for them.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
