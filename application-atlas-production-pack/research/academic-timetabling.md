# Research Notes — Academic Timetabling

Research date: 2026-09-06
Slug: academic-timetabling (DIRECTORY §23 Education, Research & Knowledge Institutions)

## Research Goal

Understand what an Academic Timetabling application is from real products: what objects exist inside it, who operates it, how a timetable gets built and maintained, what rules govern placement, and where the boundary lies against neighboring Types (Course Registration, Curriculum Management, SIS, Resource Calendar, Calendar, Employee Scheduling).

## Initial Boundary (hypothesis before research)

- Core use: institution-side construction and maintenance of the teaching schedule (which class meets when, where, with which teacher, to which student group) under conflict constraints.
- Primary users: registrar / timetabling office / school administrators; departmental schedulers; students and staff as consumers of the published timetable.
- Nearest neighbors: Course Registration System (student-side), Curriculum Management (catalog structure), SIS (system of record), Resource Calendar / Enterprise Resource Scheduling (generic booking), Calendar Application (personal), Employee Scheduling (shifts).
- Unknowns: solver vs manual editing split; exam timetabling relationship; higher-ed vs K-12 structural differences; in-term change management; publication model.

## Research Questions

1. What are the core objects (activity, section, room, staff, student group, time structure)?
2. What is the build workflow (data → constraints → generate → adjust → publish → in-term changes → rollover)?
3. What constraints/rules are modeled (clashes, capacity, availability, preferences, distribution)?
4. How do automated generation and manual editing combine?
5. What interfaces exist (grids, lists, conflict reports, portals)?
6. How does data flow to/from SIS / curriculum / registration?
7. What variants exist (higher-ed vs school vs exam timetabling; deployment; platform bundling)?
8. What lifecycle states does a timetable pass through?

## Representative Products

| Product | Segment | Philosophy | Why selected |
|---|---|---|---|
| UniTime | Higher education (open source, Apereo) | solver-first, distributed departmental timetabling | deepest official documentation; defines the constraint-solver pattern |
| Celcat | HE/FE, UK/international, commercial | interactive-first with automated option; mid-term change strength | commercial HE market representative; publishing/room-booking/exam extensions |
| aSc Timetables | K-12 schools worldwide (Slovakia), desktop + online | automatic generator + substitution/cover workflow | school-level model; 200,000 schools claim; global reach |
| Untis | European schools (Austria), desktop + WebUntis cloud | timetabling core inside a school platform (class register, communication) | platform-bundled variant; 30,000+ institutions; primary→university |

Coverage: higher-ed vs K-12; open-source vs commercial; solver-first vs interactive-first; standalone vs platform-bundled; US/UK/EU/global geographies.

## Sources

- UniTime — https://www.unitime.org/ (root, fetched 2026-09-06)
- UniTime — https://help.unitime.org/documentation (documentation index, fetched 2026-09-06)
- UniTime — Course Timetabling Solver Manual https://help.unitime.org/manuals/courses-solver (fetched 2026-09-06)
- UniTime — Course Timetabling Data Entry Manual https://help.unitime.org/manuals/courses-entry (fetched 2026-09-06)
- UniTime — Examination Timetabling Manual https://help.unitime.org/manuals/examination-timetabling (fetched 2026-09-06)
- Celcat — https://celcat.com/ (fetched 2026-09-06)
- Celcat — Interactive Timetabling feature page https://celcat.com/timetabler/features/interactive-timetabling/ (fetched 2026-09-06)
- Celcat — FAQs https://celcat.com/faq/ (fetched 2026-09-06)
- aSc Timetables — https://www.asctimetables.com/ (fetched 2026-09-06; /help/ returned 404)
- Untis — https://www.untis.com/ (fetched 2026-09-06)

### Source-access Limitations

- Untis Help Center (help.untis.at) timed out twice on 2026-09-06 → operational detail for Untis is limited to the official homepage; claims about Untis internals kept general.
- aSc online help URL not found (404 on /help/) → aSc evidence limited to official homepage feature descriptions.
- Celcat technical support portal requires login → Celcat evidence is product-page level (feature names, FAQ), not manual-level.
- No precise numeric limits, default settings, or solver parameters from Celcat/aSc/Untis are asserted anywhere; UniTime specifics stay in these notes.

## Product A — UniTime (evidence layer A: direct, manual-level)

Official self-description (unitime.org): "a comprehensive educational scheduling system that supports developing course and exam timetables, managing changes to these timetables, sharing rooms with other events, and scheduling students to individual classes… a distributed system that allows multiple university and departmental schedule managers to coordinate efforts to build and modify a schedule… minimization of student course conflicts… can be used alone… or interfaced with an existing student information system."

Components: Course Timetabling & Management, Examination Timetabling, Event Management, Student Scheduling.

### Input data model (Data Entry Manual)

- **Rooms**: room types (classrooms, computing labs, teaching labs, departmental rooms, special use, non-university locations); capacity; availability time grid; **room sharing** between departments with a controlling department (time-grid based; "free for all" times go to whoever commits first); room features (equipment, e.g. projector, seating type); room groups; distance check (back-to-back travel feasibility); room check (whether a location can host only one class at a time).
- **Instructors**: departmental instructor lists; external ID for SIS matching; instructor preferences (time, building, room feature, room group, distribution) inherited by classes; **Instructor Survey** (instructors enter their own preferences); instructor assignment preferences (teaching load, attributes) for the instructor scheduling module.
- **Instructional Offerings** (= course): configuration → instructional types (LEC/REC/LAB/IND/RES…) → **scheduling subparts** → **classes** (sections). Fields: configuration limit, limit per class, number of classes, minutes per week (determines available time patterns), number of rooms, split attendance, room ratio, managing department. **Grouping** (parent/child attendance relationships, e.g. Lec 01 with Rec 01 with Lab 01). **Cross-listed courses** (meet together; controlling course). Date pattern per class (full term, odd weeks…). Consent at offering level. Notes.
- **Preferences**: time preferences on a time grid with levels (required / strongly preferred / preferred / neutral / discouraged / strongly discouraged / prohibited); room, building, room-feature, room-group preferences; priority order class > instructor > scheduling subpart.
- **Distribution preferences** between classes: back-to-back, N hours between, same time, same room, can share room, etc., with structures (all classes, progressive, groups of two/three/four/five, pairwise, one of each).

### Solver workflow (Solver Manual)

1. **Load** input data into solver memory; consistency warnings (class not loaded if no available room/time/pattern; overlapping same-instructor or same-room required times flagged).
2. **Check** configuration: find a complete feasible solution ignoring preferences (hard constraints only: no instructor overlap, room capacity, etc.). If <100% assigned → Not-Assigned Classes list + **conflict-based statistics** (which constraints/classes the unassigned class competed with) → fix input data.
3. **Optimize** (Default configuration): consider preferences, minimize student conflicts; iterative improvement with timeout (manual: "most problems have a 30-minute time limit"); **student sectioning** step moves students to reduce conflicts; student demand data can be curricula, last-like-semester enrollments, actual course requests, or a combination.
4. **Review**: solution properties (assigned variables %, student conflicts); reports (room allocation, violated distribution preferences, instructor back-to-back, student conflicts, section balancing).
5. **View**: timetable grid (per room / instructor / curriculum; week/day/time filters; background color-codes preferences; show events blocking rooms); assigned classes lists.
6. **Change interactively**: Suggestions screen — current assignment, conflicts per candidate time, scored suggestions (change in objective), placements mode; changes staged until **Assign**; conflicting classes may be left unassigned for later resolution; interactive solver mode allows even breaking hard constraints.
7. **Save**: current → best → saved timetables (multiple saved versions).
8. **Commit**: publish the timetable so other departments see assignments and conflicts; commit can fail if another department committed a conflicting room/instructor use; re-commit possible until institutional deadline.

### Examination Timetabling (separate module)

- Separate problems per **examination type** (final, midterm, evening…), each with its own **non-overlapping examination periods**, rooms (normal vs **examination seating capacity**), period preferences.
- Exam object: name, type, length (minutes; must fit period), seating type, maximal number of rooms (split), size (students), instructors; associated to classes/courses whose enrolled students attend.
- Student class enrollment data required (from Student Scheduling module or imported via XML).
- Solver: MPP (**Minimal Perturbation Problem**) mode minimizes changes to an existing timetable; single saved solution; manual assignment dialog with conflict counts.
- Conflict taxonomy: **direct** (same period), **back-to-back** (consecutive periods, with distance variant), **>2 a day**, N/A (student unavailable); same taxonomy for instructors.
- Distribution preferences: precedence, same period, same room, can share room, same day (optional).
- Statuses: Examination Disabled → Data Entry → Timetabling → Published (per examination type; per-type managers).
- Extensive reports (23 listed: individual student schedules, direct conflicts, room splits, period usage…).

### Other observations

- Event Management component: one-off events share the same room inventory; committed events block rooms in the timetable grid.
- Student Scheduling component: students scheduled into individual classes (sectioning) — the demand side.
- XML interfaces + APIs + exports (CSV) for SIS integration (Banner interface documented).
- Roles: Session Administrator, Department Schedule Managers, Examination Timetabling Manager, Event Managers.

## Product B — Celcat (evidence layer A for feature existence; marketing-level depth)

Official pages (celcat.com):

- Positioning: timetabling platform for universities and colleges; "over 200 universities and colleges"; "used daily by over a million students"; scale claim up to 100,000+ users (State of Queensland); multi-campus, multi-timezone (UAL six colleges / 17 sites).
- **Interactive Timetabling** (feature page): switch between **automated and manual scheduling modes**; define/prioritise/adjust complex rules (constraints); **decentralised multi-level access** (department timetablers input and manage event parameters); scheduling engine for "optimal, clash-free timetables"; **scenario planning / what-if** previews; space and resource optimisation (room capacity limits, minimize room changes, multiple layouts per space); visual constraint management (relationships/dependencies between resources and events); **course planner and template wizards**; "automate the rollover process for future years".
- **Publishing**: "Keep students and tutors informed, in real time, everywhere."
- **Room Booking**: "An integrated solution handling the whole process, from tutor request to confirmation"; "Automatically avoid clashes."
- **Exam Scheduling** (extension): "Produce optimised schedules for students and invigilators."
- **Automated Premium** (extension): "Input rules & resources and let the system do the rest, for courses and exams."
- Extensions: Attendance Monitoring, Pay Claim (staff pay claims), Now (student self-service).
- FAQ: SIS integration is a first-class concern ("bespoke, in-house systems… we have done many, many times"); cost-per-student pricing; mid-term change handling highlighted ("handling mid-term requests for change is often so quick and easy"); reporting to "see where inefficiencies occur"; publishing "accurate timetable, in real time"; faculty room booking "academics can see and book available rooms, in real time"; estate-cost levers (minimise travel between sessions, run same-setup sessions concurrently, split/combine student groups, take rooms out of use).

Interpretation: same object world as UniTime (activities, rooms, staff, cohorts, constraints) with an interactive-first philosophy; automated generation available (standard or as "Automated Premium" extension). Publishing and in-term change are emphasized as core value.

## Product C — aSc Timetables (evidence layer A for homepage descriptions)

Official homepage (asctimetables.com):

- Positioning: school scheduling software; "trusted by 200,000 schools worldwide"; 30 years; desktop (Windows) + Timetables Online (browser, multi-user collaboration) with compatible data.
- **Automatic generation**: "enter your requirements… evaluate over 5,000,000 possibilities… beautifully-balanced schedule"; "Powerful automatic generator… if a colleague or headmaster comes with new request — the work takes just 5 minutes again" (regeneration loop).
- **Substitution** (in-term operations): "Once the timetable has been created, you just need to input the absentees. aSc Substitutions will advise the best cover teacher — but you are free to choose your own candidate"; published on website and mobile; "all changes are automatically entered in class registers and calendars"; move/split or join lessons; define criteria, absence reasons, substitution types.
- **Share timetable and substitution**: available to teachers, students, parents; personal notifications of daily changes.
- **Class register**: reflects timetable/substitution/event changes; teachers pick lesson topic, check attendance.
- **Calendar**: school events (excursions, holidays); "plan your exams… avoid collision with other school events."
- **Room or event booking**: "system combines up-to-date information from timetables, absent teacher covers, and events… No two classes will ever collide in one classroom."
- **Integrated AI**: type what you want to change; AI can advise and (if allowed) make changes to data.

Interpretation: school-level object world (teachers, classes as cohorts, subjects, classrooms, lessons as cards in a period grid); the build cycle is enter data → generate → adjust → publish; the in-term loop (absentee → cover suggestion → publish → register update) is a first-class workflow, not an afterthought.

## Product D — Untis (evidence layer A for homepage; help center inaccessible)

Official homepage (untis.com, German):

- Positioning: "die Plattform für Schulen" (the platform for schools); "Marktführer im Bereich Stundenplanung" (market leader in timetabling); 30,000+ educational institutions "from the small primary school to the complex university"; 35+ languages; 45+ sales partners.
- Planning scope: "Stundenplan, Unterricht, Vertretungen, Räume, Pausenaufsicht" (timetable, lessons, substitutions, rooms, break supervision).
- Organizing scope: digitales Klassenbuch (digital class register), Termine, Sprechtage (parent days), Noten (grades).
- Collaboration: WebUntis Mitteilungen (messages), Untis Mobile app (current timetable on smartphone).
- Narrative example of in-term loop: teacher sick at 7:00 → substitution planner finds cover at 7:20 → substitute gets push notification at 7:21 → student sees updated timetable at 7:30.
- Products: Untis (timetabling, browser-based planning; vUntis virtual), WebUntis (online extension: class register, messages, mobile app).
- Solutions page mentions universities/HE ("Bildungsanbieter… Unis, FHs").

Interpretation: timetabling core (Untis) + platform layer (WebUntis) with substitution/cover as a named daily workflow; same object world as aSc at school level. Help-center-level detail NOT verified (see limitations).

## Cross-product Comparison

| Dimension | UniTime | Celcat | aSc Timetables | Untis |
|---|---|---|---|---|
| Segment | university | university/college | school (K-12) | school (K-12→HE) |
| Activity unit | class/section under offering/subpart | events/activities (terminology not manual-verified) | lesson (card) | lesson (Unterrichtseinheit) |
| Resources | rooms (shared, features, groups), instructors, curricula/classes | rooms, tutors, cohorts | teachers, classrooms, classes | teachers, rooms, classes |
| Time structure | date patterns + time patterns on a grid | institutional time grid | period grid per school | period grid (Stundenplan) |
| Conflict model | hard constraints + preference levels + distribution prefs + student conflicts | clash-free schedules; rules with priorities | generator criteria; collision avoidance | clash avoidance (detail unverified) |
| Generation | solver (check → optimize → sectioning) | automated mode / Automated Premium | automatic generator | automatic generation (named core function) |
| Manual editing | interactive solver, suggestions with scores | interactive timetabling (primary philosophy) | manual editing + AI panel | manual editing (detail unverified) |
| Publication | commit → visible to all; class assignments screen | Publishing (real time, everywhere) | share to web/mobile; personal notifications | WebUntis + mobile app |
| In-term changes | changes + re-commit until deadline; events | mid-term change strength (positioning) | substitution module (absentees → cover → publish → register) | Vertretungsplanung (substitution planning) |
| SIS integration | XML/API/exports; Banner interface | integration service, bespoke systems | (not detailed on homepage) | platform integrations (WebUntis Plattform) |
| Exam timetabling | separate module (own solver, periods, seating) | extension (Exam Scheduling) | calendar-level exam planning | (not verified) |
| Room booking | Event Management (events block rooms) | Room Booking feature | room/event booking | Raumplanung |
| Rollover | roll forward session (mentioned in exam manual) | rollover automation (course planner) | (not detailed) | next-year planning (narrative) |
| Student-facing | Student Scheduling / sectioning assistant | Now extension (student self-service) | students/parents view timetable | students/parents view via app |

### Stable commonalities (layer B, cross-product)

1. Teaching activities as the demand: things that must meet (classes/sections/lessons/events), each requiring staff and space and attached to a student group.
2. Shared, capacity-limited resources: rooms/spaces and instructors, each with availability; student groups/cohorts as the third conflict axis.
3. A time structure: term + week grid of periods/slots into which activities are placed.
4. Conflict-checked assignment: the timetable is the central object; double-booking of any resource is the fundamental violation; products differ in whether they prevent it automatically, detect it interactively, or both.
5. Constraint/preference model: hard requirements vs soft preferences (all four products express rules/preferences; UniTime exposes the full level taxonomy).
6. Automated generation + manual adjustment combined (solver-first, interactive-first, or generator+AI — all four offer both poles).
7. Publication to consumers: the timetable is an institutional artifact delivered to staff/students (commit, publishing, share, WebUntis app).
8. In-term change management: substitutions/cover, room moves, cancellations flow through the same system and propagate to consumers.
9. SIS/curriculum integration: data in (courses, staff, students, rooms) and out (assignments) is a structural concern (UniTime interfaces, Celcat integration service, Untis platform).
10. Term/year rollover: the schedule is rebuilt each term/year from the previous one.

### Product-specific findings (layer A, single-product)

- UniTime: departmental room sharing with controlling department; commit model with cross-department conflict feedback; MPP re-solve; student sectioning as part of the solver; examination module with seating capacity and 23 report types; instructor survey.
- Celcat: Pay Claim (staff pay claims), Attendance Monitoring, Now (student self-service) as commercial extensions; AI-native positioning.
- aSc: class register module fed by timetable changes; AI panel for natural-language data changes; free trial until satisfied with generated schedule.
- Untis: break supervision (Pausenaufsicht) planning; digital class register; parent-teacher day coordination; platform framing.

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the Type stops being recognizable:

1. **Teaching activities to be placed** — a managed set of recurring instructional meetings (course sections, lessons) that each require resources.
2. **Shared, availability-constrained resources** — staff/instructors and rooms/spaces (and the student groups they serve) that cannot be double-booked.
3. **A time structure** — an institutional term/week grid of schedulable time slots.
4. **Conflict-checked assignment** — placing activities into time slots bound to resources such that clashes are prevented/detected; the resulting timetable is the central persistent object.
5. **Publication to the institution** — the timetable exists as a shared artifact consumed by staff and students.

Test: remove activities → nothing to schedule; remove resources → a mere event calendar; remove the time structure → no schedule; remove conflict checking → a drawing tool; remove publication → a private solver sandbox, no longer an institutional timetabling system. All five are needed.

### L1 — Common Mature Structure

- Constraint/preference model with hard/soft distinction (required vs preferred levels; distribution constraints such as back-to-back; capacity and availability rules)
- Combined automated generation + interactive manual editing (suggestions, drag/move, what-if)
- Conflict detection and reporting (clash reports, student-conflict counts, utilization)
- SIS/curriculum data exchange (import courses/staff/students/rooms; export assignments)
- Multi-user institutional operation (roles: central timetabling office vs department schedulers)
- Publishing surfaces (web portals, mobile apps, personal timetables, notifications)
- In-term change management (substitutions/cover, room changes, cancellation propagation)
- Term/year rollover and template reuse
- Reporting/analytics (utilization, workload, room allocation)
- Adjacent resource use: room/event booking against the same inventory

### L2 — Variant / Optional Structure

- Segment structure: higher-ed (offerings → sections, meeting patterns, student sectioning, departmental distributed timetabling) vs school (classes as fixed cohorts, period grid, master schedule, substitution office)
- Exam timetabling as a sibling problem (separate periods, seating capacity, invigilators, direct/back-to-back/>2-a-day conflicts) — separate module or extension in sampled products
- Solver posture: solver-first vs interactive-first vs generator+AI-assist
- Deployment: desktop app, client-server, SaaS/cloud, online multi-user
- Platform bundling: standalone timetabling vs school platform (class register, attendance, communication, grades) vs SIS-embedded module
- Regional conventions: period structures, week patterns (e.g., alternating weeks), term shapes
- Student-facing self-scheduling (sectioning assistants, student portals)

### L3 — Vendor-specific (research notes only)

- UniTime: commit/deadline model, room-sharing time grids, conflict-based statistics screen, Banner addon, HQL custom reports, solver parameter classes.
- Celcat: Pay Claim, Attendance Monitoring, Now, "Automated Premium" packaging, AI graph-database marketing.
- aSc: class register, Edupage ecosystem, AI panel, trial-until-satisfied licensing.
- Untis: Pausenaufsicht (break supervision), Volljährigkeit (adult-student administration), Schülerzuordnung (flexible student assignment), Mitteilungen.

## Historical / Market-Sample Check

Would older, regional, platform-native products still fit the L0? Yes: timetabling predates modern SaaS — batch mainframe solvers, desktop single-user products (Untis itself dates from the 1970s DOS era; aSc claims 30 years), and paper/grid methods all share activities + resources + time grid + conflict-checked assignment + a published schedule. None of the modern wrappers (cloud, mobile apps, AI panels, portals) is required by the definition. Conversely, the definition excludes generic room-booking tools (no teaching-activity/curriculum model) and personal calendars (no shared-resource conflict model).

## Boundary Findings

1. **vs Course Registration System (§23 sibling)**: registration captures student-side demand (which sections students take); timetabling constructs institution-side supply (when/where sections meet). They interlock — UniTime ships both (course timetabling + student scheduling/sectioning), and course requests feed the solver's student-conflict minimization. Test: remove the institution-side construction loop → a registration system remains; remove student enrollment/selection → a timetabling system remains. Related Types sharing a data flow, not duplicates.
2. **vs Curriculum Management (§23 sibling)**: curriculum defines what courses/programs exist (catalog structure); timetabling places them in time/space. Curriculum is an upstream input (UniTime: offerings come from subject areas; Celcat: course planner/templates). Capability/input relationship.
3. **vs SIS / School Management System**: system of record for students/staff/courses; timetabling is either a module inside it or a specialized satellite that exchanges data (UniTime explicitly "used alone… or interfaced with an existing student information system"; Celcat's integration service; Untis platform). Overlap is packaging, not structure.
4. **vs Resource Calendar (§03.08) / Enterprise Resource Scheduling Platform (§10) / Room Booking**: generic resource scheduling lacks the teaching-activity model (curriculum attachment, cohorts, teaching loads, academic terms). Timetabling products embed room/event booking as a capability (Celcat Room Booking, aSc booking, UniTime Event Management) — capability-inside-Type relationship, consistent with the retail-POS-style pattern.
5. **vs Calendar Application (§03.08)**: personal time display vs institutional construction under resource constraints; no conflict model in a calendar.
6. **vs Employee Scheduling Platform (§09)**: shares the constraint-satisfaction pattern (staff + shifts + availability) but objects are shifts/jobs, not curriculum-attached teaching activities with student cohorts; different rules (labor law vs academic clashes). Related pattern, different Type.
7. **Exam timetabling**: same core pattern (activities → periods → rooms → conflict minimization) with different objects (exam periods, seating, invigilators, per-student conflict taxonomy). In the sample it always appears as a module/extension of a timetabling product, not a separate purchase — probable Variant/Capability rather than independent Type; flagged for joint review if an Examination Scheduling leaf is processed.
8. **Naming**: the leaf name "Academic Timetabling" matches market usage (university "timetabling office", products named "Timetabler", "Stundenplanung"). No alias problem found.

## Uncertainties

- Untis operational detail (solver behavior, object terminology) unverified — help center inaccessible; claims kept general.
- Celcat object terminology (its internal data model) not manual-verified — support portal gated; feature existence verified only.
- aSc internal model (how lessons/classes/teachers are structured) inferred from homepage descriptions only.
- Whether every commercial HE timetabler includes student-sectioning (UniTime does; others may leave it to the SIS) — treated as L2, not asserted generally.
- Exact relationship between timetabling products and exam-only scheduling vendors (some institutions buy separate exam software) — not researched beyond the sample.

## Final Synthesis

Academic Timetabling is the institution-side scheduling application for teaching: it holds the set of teaching activities a term must deliver, the staff and spaces that serve them, and the time structure of the term; it assigns activities to times and resources under conflict constraints (automated generation, interactive adjustment, or both); and it publishes the resulting timetable to the institution, then manages in-term changes against it. Higher-ed and school products implement the same core with different structural emphasis (sections/meeting patterns vs fixed cohort grids), and exam timetabling recurs as a sibling problem inside the same products. The defining core is deliberately minimal: activities + constrained shared resources + time structure + conflict-checked assignment + published institutional artifact.
