# Research Notes — Lesson Planning Application

Research date: **2026-09-08**

## Research Goal

Understand what a Lesson Planning Application really is from real products: what the lesson plan object carries, what organizes it (schedule? calendar? units?), how planning work flows (draft → teach → adjust → reuse), what role standards/files/sharing/administration play, and where the Type's boundary sits against Curriculum Management, LMS, eLearning Authoring, Educational Content Platform, and Academic Timetabling.

## Initial Boundary

Initial hypothesis (before research):

- Core use: a teacher authors structured lesson plans — records of intended instruction (objectives, activities, materials, assessment) — organized around their teaching schedule.
- Primary users: K-12 classroom teachers; institutional variants add school/district administrators.
- Nearest Types: Curriculum Management (institution layer), LMS (student-facing delivery), eLearning Authoring Tool (learner-facing courseware), Educational Content Platform (lesson-plan libraries), Academic Timetabling (schedule construction), Classroom Management, Assignment Management, Daycare/Preschool Management (operator program documentation).
- Likely boundary: teacher-facing planning of instruction (before teaching) vs student-facing delivery (LMS) vs institution-level curriculum of record (Curriculum Management).
- Open questions going in: is the schedule/calendar frame definitional or merely common? Is standards alignment definitional? Where does the unit-planning layer belong?

## Research Questions

1. What is the lesson plan as an object — sections, structure, attachment to a teaching occasion?
2. What is the organizing frame — timetable (periods/classes), calendar (day/week/month), units, subjects?
3. How does the container work — school year, terms, non-teaching days, rotation schedules?
4. How does reuse work — templates, repeating plans, copy forward, year rollover?
5. How does the plan respond to schedule disruption (snow days, assemblies) — bump/shift mechanics?
6. How do standards get attached and reported?
7. How do sharing/collaboration/administration work — colleagues, substitutes, admin review/turn-in?
8. What is the relationship to delivery — publish to students/families, LMS/Google integrations?
9. What interfaces exist — planner grid, lesson editor, unit planner, standards browser, resource library?
10. What institutional variants exist — district oversight, curriculum mapping, IB/international frameworks?
11. Historical check: does the paper plan book satisfy the definition?

## Representative Products

Selected for market representation + documentation completeness + different product philosophy + different customer level:

| Product | Philosophy / level | Evidence depth |
|---|---|---|
| PlanbookEdu | solo-teacher online planbook; freemium; the "digital plan book" pole | Deep (help center + training site, Tier 1) |
| Common Planner (Common Curriculum) | collaborative planner with school/district admin layer; free core | Medium (official product pages, Tier 2) |
| Toddle (Curriculum Planning module) | whole-school international platform; planning as one module; IB/British/Cambridge frameworks | Medium (official product pages, Tier 2) |
| PowerSchool Curriculum & Instruction (formerly Chalk) | district suite; lesson planner inside curriculum & instruction; SIS-provisioned | Index-level (official help site structure, Tier 1 index) |

Considered and dropped: Planbook.com (JS-only site, no fetchable content), OnCourse Lesson Planner (site returns 403), iDoceo (native iPad app, no web docs fetched).

## Sources

- PlanbookEdu product page — https://www.planbookedu.com/ (fetched 2026-09-08)
- PlanbookEdu training site — https://learn.planbookedu.com/home (fetched 2026-09-08)
- PlanbookEdu Help Center — https://help.planbookedu.com/ (fetched 2026-09-08), including:
  - Planbook basic options — https://help.planbookedu.com/help/building/planbook-basic-options/
  - The lesson editor — https://help.planbookedu.com/help/writing-plans/the-lesson-editor/
  - Bump plans forward — https://help.planbookedu.com/help/writing-plans/bump-plans-forward/
  - Share with an administrator — https://help.planbookedu.com/help/sharing/share-with-an-administrator/
  - How standards work — https://help.planbookedu.com/help/standards/how-standards-work/
- Common Planner (Common Curriculum) — https://www.commonplanner.com/ (fetched 2026-09-08 via commoncurriculum.com)
- Toddle — https://www.toddleapp.com/ and https://www.toddleapp.com/product/curriculum-planning/ (fetched 2026-09-08)
- PowerSchool Curriculum & Instruction help (Chalk lineage) — https://help.chalk.com/ (fetched 2026-09-08; index level only)
- chalk.com root — redirects to PowerSchool (confirms Chalk acquisition)

Source-access limitations:

- planbook.com serves a JavaScript shell; no operational content retrievable. No claims made about it.
- oncoursesystems.com returns 403 (blocked). No claims made about it.
- help.chalk.com serves article URLs as the index page; article bodies not retrievable. PowerSchool observations are limited to what the help-site structure (section and article titles) directly shows.
- Toddle and Common Planner evidence is product-page depth (marketing + feature enumeration), not help-center depth; operational mechanics (exact bump semantics, exact sharing models) are asserted only where the pages state them.

## Product Observations

### PlanbookEdu (evidence layer A — deep official help center)

**Container ("planbook"):**
- A planbook has four basic settings: Name, Start Date / End Date ("the first and last day of your school year… which weeks exist in the planbook — you can't navigate to a week outside them"), Periods Per Day (1–30, "how many rows (or columns) the grid has"), Rotation (Weekly default; A/B Days, A/B Weeks, or a fixed cycle from 3 up to 12 days). (A)
- Related machinery: reorder/rename periods, rotation labels, off days/holidays/breaks, orientation switch (rows vs columns), copy a planbook, start a new school year, archive a planbook, manage multiple planbooks, change layout mid-year. (A)
- Views: weekly, daily, single day, month, year; navigation "move between day, week, month and year — and find any lesson fast". (A)

**Lesson entry (the plan):**
- Editor: rich text area with formatting (bold, italic, lists, alignment, color, font size); opened from any box in the grid; quick in-place edit vs full edit. (A)
- Recurrence: "This entry should appear" — once (default), daily, or repeat on the schedule's cycle, with a second dropdown for how far it runs. (A)
- Standards: search box in the editor; attached standards show as removable chips. (A)
- Files: "worksheets and handouts that belong with the lesson" attached to the entry. (A)
- Extras: "Hide from shared plans" checkbox; "Lock this entry to this day" so bumping moves other plans around it. (A)
- Save/Cancel/Delete; deleted plans recoverable for three days; Undo link after most actions; private Notes; spell check. (A)

**Schedule-coupled plan management (bump):**
- "You lost a day to a snow day, an assembly, or a fire drill that ate third period. Bumping moves that day's plans forward and pushes everything after them along too." (A)
- Semantics: one-time plans and rotation-cycle plans move; daily and weekly repeating plans stay put ("If Art is every Tuesday, a Monday closure shouldn't drag Art to Wednesday"); locked plans stay and others route around them; bumping lands only on teaching days — off days, holidays, weekends skipped; off-day + bump combined in one step; bump backward and single-period bump exist; undo reverses a bump. (A)

**Templates:** "Build a repeating schedule once and reuse it all year" — entry editor with an outline set to repeat weekly for all weeks. (A)

**Standards:**
- "Standards are off by default, because not every teacher tags plans with them." (A) — key anti-overfitting evidence.
- Three steps: choose sets (state map, national/regional, custom), attach via search in the editor, then coverage reporting ("which standards you've taught, how often, and which you haven't touched"). (A)
- Sources: vendor-maintained state/national sets incl. Common Core; community sets shared by teachers (over 600); custom standards. (A)

**Sharing / administration:**
- Share links: restricted (email-gated) or open, expiry, date range, email notification; share a week/day/single period; recipients need no account; read-only and "always current". (A)
- Collaboration with another teacher; embed in a website; private notes never visible in shares; hidden plans hidden from links but visible to group-account administrators regardless. (A)
- Group accounts (schools/districts): admin dashboard, add/remove teachers, **turn in** ("submit a week's plans to your administrator, who reviews them and can leave comments"), review and comment week by week, group billing. (A)
- Marketing page: "Send plans to your principal, grade-level team or a substitute. You choose exactly what they see." "Administrators get a dashboard to manage every teacher's account… teachers turn in plans with a click instead of a copy machine." (A)

**Output:** print from browser, export to Word/PDF with files included, export entire planbook, push plans to Google Calendar, phone/tablet app. (A)

**Positioning:** free-forever plan + premium ($30/year); testimonial from a 19-year veteran who "always used a hard copy planbook" — direct evidence the paper plan book is the predecessor artifact. (A)

### Common Planner / Common Curriculum (evidence layer A — official product pages)

- Teachers: "Create Unit and Lesson Plans; Add and Track Standards; Easily share plans with others; Reuse plans year after year." (A)
- Mechanics: "Drag and Drop. Rearrange lessons in seconds across days, weeks, and classes." "Bump Lessons. Shift plans forward with one click while keeping pacing intact." "Reuse Great Work. Copy your strongest lessons into new units and new school years." (A)
- Curriculum connection: "Map Your Standards. Track standards coverage as you build daily lessons." "Plan Backward. Start from goals and assessments to align every class period." (UbD-style backward design). (A)
- Collaboration: "Collaborate in Real Time. Co-plan with your team in one shared, living planbook." (A)
- Differentiation: "Adapt plans for learners while preserving one coherent arc"; notes/resources kept in context; "See the week ahead". (A)
- Admins: "Check & follow up on plans in minutes; Custom school-wide template & calendar; Collaborate in plans with the whole team; Build a school archive of lessons"; "Monitor Implementation… Coach with Context. Provide feedback directly in plans"; "Spot Gaps Early. Identify missing standards coverage"; "Align Across Campuses"; share exemplars. (A)
- Scale claim: "Over 300,000 Teachers & Admins"; free core tier ("CP Basic is free. Forever"). (A)
- Positioning: "A lesson planner that helps teachers write their best unit plans and lesson plans faster… Helps admins coach & manage lesson submissions." (A)

### Toddle — Curriculum Planning module (evidence layer A — official product pages)

- Whole-school platform positioned "More than an LMS. Plan, teach, assess, report, and communicate – all in one place." Planning is one module among assessments, portfolios, reports, communications, behavior, class operations, accreditation. (A)
- Planning hierarchy: "Plan your entire curriculum in one place – from school-wide maps and courses to units and lessons." Sections: bird's-eye curriculum maps; courses/yearly plans with coverage tracking; units ("subject-specific or interdisciplinary units with 50+ templates or design your own"); lessons ("Design engaging lessons in minutes… generate creative lesson plans"). (A)
- AI: "Co-create with Toddle AI… generate creative, engaging lesson plans"; AI recommends "thoughtful adjustments to our lesson plans for various learning styles" (differentiation); curriculum design assistant "from courses to units to lessons". (A)
- Standards: "200+ preloaded standard sets… or upload your own." (A)
- Collaboration: "Collaborate on curriculum like you would in Google Docs – across grade levels, subjects, and roles"; coordinator testimonial: "as a coordinator, I can access each of their planners, learning experiences and assessments from one place." (A)
- Analytics: "track alignment, pacing, and coverage to guide smarter planning." (A)
- Governance posture: "Toddle fits your planning approach – centralized, teacher-led, or anywhere in between." (A)
- Exemplars: "exemplar unit and lesson plans from experts." (A)
- Class Operations module: "Attendance, timetable, calendar… Import schedules from SIS or tools like aSc, EdVal… View all lessons in one calendar." (A)
- Frameworks: IB PYP/MYP/DP/CP, English National Curriculum, Cambridge, Australian & NZ, UbD, bespoke. (A)

### PowerSchool Curriculum & Instruction (formerly Chalk) (evidence layer A at index level)

- chalk.com now redirects to PowerSchool; Chalk's products continue as PowerSchool Curriculum & Instruction. (A)
- Official help site (help.chalk.com) is organized as: **Administration** (Academic terms; Add a schedule to an academic term; Assign academic terms to maps; SIS provisioning), **Curriculum** (curriculum maps; assign an academic term to a map), **Lesson Planner** (Add classes or non-teaching blocks to timetable; Add standards to lesson plan), **PowerBuddy for Curriculum & Instruction** (Create or edit a lesson plan; Create and edit curriculum maps). (A — index level)
- Structure directly shows: SIS-provisioned teachers/classes → timetable (classes + non-teaching blocks) → lesson plans carrying standards → curriculum maps at the district layer; AI drafting of lesson plans and maps. (A at index level; article bodies not retrievable)

## Cross-product Comparison

| Dimension | PlanbookEdu | Common Planner | Toddle (Curriculum Planning) | PowerSchool C&I (Chalk) |
|---|---|---|---|---|
| Container | planbook = school year + periods/day + rotation | planbook (school-wide template & calendar on admin side) | school platform: maps → courses → units → lessons | academic terms + timetable inside district suite |
| Lesson plan object | rich-text entry in a day×period box + standards chips + files + recurrence + lock | lesson plans (with unit plans above) | lesson plans inside units, AI-draftable | lesson plans with standards attached |
| Schedule coupling | bump fwd/back, off days, rotation-aware, locked plans | bump one click, drag & drop across days/weeks/classes | timetable import; "all lessons in one calendar" | timetable with classes + non-teaching blocks |
| Standards | optional (off by default), sets + coverage report | add & track, coverage gaps | 200+ sets or upload; alignment analytics | standards on lesson plans |
| Reuse | templates, repeat, copy planbook, new school year, archive | copy into new units/years | templates + exemplar libraries | curriculum maps as the reusable district layer |
| Sharing | view links, colleague collaboration, turn-in + admin comments | share; real-time co-planning | real-time co-planning; coordinator access to all planners | district oversight (SIS-provisioned) |
| Admin layer | group accounts: dashboard, turn-in review, billing | admin dashboard, school archive, coaching feedback | leadership analytics, centralized↔teacher-led | district suite around the planner |
| AI | none observed | "AI built-in" (positioning) | AI lesson/unit/map generation, differentiation suggestions | PowerBuddy lesson-plan drafting |
| Customer level | individual teacher (freemium) | teacher + school/district | school (international/independent) | district (K-12 suite) |

**Stable across all four (B):** the lesson plan as a teacher-authored record of intended instruction; placement into a scheduled teaching occasion within a school-year frame; forward planning ahead of teaching; schedule-disruption shifting (bump); reuse across units/years; standards attachment (where standards-based regimes apply); sharing with colleagues/administration; export/print.

**Variable (implementation or variant):** whether the container is a personal planbook or a school platform; whether units sit above lessons; whether standards are on by default; whether administration reviews plans (turn-in) or merely accesses them; whether AI drafts plans; whether plans publish to students/families; rotation schemes; framework templates (IB unit planners vs UbD vs state standards).

## Canonical Abstraction

### Level 0 — Defining Invariant

Three jointly-held structures:

1. **The lesson plan of record** — a persistent, individually placed, teacher-authored record of intended instruction for a specific teaching occasion (a class/subject at a scheduled time), carrying pedagogical content — what will be taught and how (objectives, content/activities, materials, assessment in some arrangement). The exact section set is product/framework-defined.
   - Remove → a lesson-plan template tool or a lesson-plan content library (Educational Content Platform territory); nothing is being planned into the working year.

2. **The teaching schedule as the organizing frame** — plans live in the teacher's recurring teaching slots (classes/periods × days) across a school-year calendar with non-teaching days; planning is done ahead of teaching, and the plan is coupled to its scheduled occasion so that schedule disruption shifts plans (bump) rather than orphaning them.
   - Remove → a document editor (plans as free documents) or a timetable tool (slots with no instructional content).

3. **The plan→teach→adjust loop with accumulation** — plans are drafted, refined, taught from, annotated/adjusted, reused (copied, templated), and accumulate across terms and years as the teacher's planning archive (rollover, copy into a new year, archive).
   - Remove → a static calendar of lesson documents; the "planning" work is gone.

Jointly-held is load-bearing:
- 1 alone = template tool / content library
- 2 alone = timetabling / calendar
- 3 alone = generic journal/notes
- 1+2 without 3 = a filled calendar of documents with no working loop
- 1+3 without 2 = plan-writing tool with no schedule anchor
- 2+3 without 1 = slots with nothing instructional in them

### Level 1 — Common Mature Structure

Present in most mature products, not required for the Type:

- **Standards alignment** — standards sets (state/national/framework), attach to lessons by search, coverage reporting ("taught / how often / not touched"). Notably optional: PlanbookEdu ships standards **off by default** — direct evidence it is not definitional.
- **Lesson templates and recurring plans** — repeating schedule built once; entries repeating daily/weekly/cycle.
- **Schedule-disruption machinery** — one-click bump forward/backward, off-day marking combined with bump, locked plans, undo. (The *coupling* is L0; these mechanics are its common implementations.)
- **Resources per lesson** — attached files/worksheets/links; personal file stores (PlanbookEdu "Cubby").
- **Sharing** — view-only links (expiry, date range), colleague collaboration, substitute plans, private notes withheld.
- **Administration layer** — turn-in/review/comment loops, admin dashboards, school-wide templates, school archives (Common Planner, PlanbookEdu group accounts, Toddle coordinators, PowerSchool district suite).
- **Unit planning above lessons** — units → lessons hierarchy (Common Planner, Toddle; PowerSchool curriculum maps feed planning).
- **Output** — print, Word/PDF export, whole-planbook export, calendar push (Google Calendar), mobile apps.
- **Year machinery** — copy planbook, start a new school year, archive, multiple planbooks.
- **Safety** — undo, deletion recovery, version-ish protections.
- **AI assistance** (era-current) — lesson/unit/map drafting, differentiation suggestions (Toddle AI, PowerBuddy, Common Planner AI).

### Level 2 — Variant / Optional Structure

- **Customer level**: individual teacher (freemium) ↔ school/district subscription ↔ module of a whole-school platform.
- **Curriculum framework**: US state standards / Common Core; IB PYP/MYP/DP unit planners; English National Curriculum; Cambridge; Australian; UbD backward design; bespoke school curricula.
- **Planning philosophy**: centralized (school-prescribed templates, admin review) ↔ teacher-led; Toddle explicitly spans "centralized, teacher-led, or anywhere in between".
- **Schedule regime**: weekly repeat, A/B days, A/B weeks, 3–12 day rotation cycles.
- **Delivery coupling**: publishing plans/lessons to students and families (Toddle), Google Calendar push, LMS adjacency — optional, not definitional.
- **Subject/role breadth**: specialists, non-teaching blocks, multiple planbooks per teacher.
- **Deployment**: standalone web app vs module inside SIS/suite (PowerSchool) vs school platform (Toddle).

### Level 3 — Vendor-specific (Research Notes only)

- PlanbookEdu: "Cubby" file store; 3-day deletion recovery; 600+ community standards sets; state-map set picker; embed-in-website; $30/yr premium.
- Common Planner: "CP Basic" free tier; school archive; cross-campus alignment tooling.
- Toddle: AI suite (Curriculum Design Assistant, Assignment Builder, Feedback & Grading Assistant…); exemplar libraries; accreditation management; 50+ integrations; aSc/EdVal timetable import.
- PowerSchool: PowerBuddy AI; SIS provisioning; curriculum maps bound to academic terms.

## Rejected Findings (anti-overfitting)

- **Standards alignment is NOT definitional.** PlanbookEdu documents standards as off-by-default ("not every teacher tags plans with them"); the paper plan book predates standards tagging entirely. Standards are L1 (common in standards-based regimes, esp. US K-12), not L0.
- **Rich-text editors, specific section sets (objectives/materials/exit tickets), and framework templates are NOT definitional** — they vary by product and pedagogical framework; the paper plan book used handwriting.
- **AI drafting is era-current, not definitional.**
- **Admin oversight is NOT definitional** — the solo-teacher pole (PlanbookEdu individual plan) has no admin at all.
- **Unit layer is NOT definitional** — PlanbookEdu's core grid has no unit object; units appear in Common Planner/Toddle.
- **Student/family publishing is NOT definitional** — optional (Toddle), absent in solo planners.
- **A shared implementation pattern (e.g., all sampled products being web apps) is not an invariant** — the paper plan book satisfies the core with no software.

## Historical / Market-Sample Check

- **Paper plan book** (the direct predecessor, confirmed by PlanbookEdu's own testimonial: a 19-year veteran who "always used a hard copy planbook"): a physical book with a weekly grid — days across, periods/subjects down — in which the teacher handwrites each lesson ahead of the week, scribbles adjustments while teaching, carries ideas forward, and keeps past years' books as an archive. Satisfies all three L0 structures with no software, no standards tagging, no sharing, no AI. ✔
- **Older web-era planners** (PlanbookEdu itself dates to ~2010 per its "15+ years" claim and archived Mashable/NEA features): same core, no AI, thinner admin. ✔
- **Regional/framework variants**: IB unit planners (Toddle) place a heavier unit layer above lessons but the lesson-planning loop is intact; UK-style planning regimes satisfy the same core. ✔
- Conclusion: the definition does not over-fit the current US standards-based, AI-assisted market.

## Boundary Findings

1. **vs Curriculum Management** — the central seam. Curriculum management is the institution-level layer of records, review, standards coverage, and publication *around* instruction (programs, courses, curriculum maps, approval workflows). Lesson planning is the individual teacher's schedule-coupled authoring surface. They are adjacent layers frequently shipped together (Toddle: maps → courses → units → lessons; PowerSchool C&I: curriculum maps + lesson planner in one suite). Test: remove the teacher's personal schedule-coupled planning loop and keep institution-level maps/approval/publication → Curriculum Management; remove the institution layer and keep the teacher's planbook → Lesson Planning Application. **Joint review flagged by curriculum-management research is DISCHARGED here: keep both as separate Types (layer seam, not duplicates).**
2. **vs LMS** — LMS centers on student-facing delivery (content to learners, assignments, submissions, grades). Lesson planning centers on teacher-facing intention before teaching. Toddle markets itself "more than an LMS" precisely because planning sits beside delivery. Test: remove teacher planning and add student delivery/grading → LMS.
3. **vs eLearning Authoring Tool** — authoring produces interactive courseware consumed by learners; lesson plans are working records consumed by the teacher (and optionally observers). Different audience, different object.
4. **vs Educational Content Platform** — lesson-plan libraries (marketplaces/collections of teaching content) distribute plans as content; no schedule-coupled planning loop, no personal planbook. Test: remove the personal schedule frame → content platform.
5. **vs Academic Timetabling** — timetabling constructs the institution's master schedule (rooms, teachers, sections); the lesson planner *consumes* a schedule (its own personal grid, or an imported SIS timetable — Toddle imports from aSc/EdVal; PowerSchool provisions from SIS). Test: remove lesson content and add constraint-solving schedule construction → timetabling.
6. **vs Classroom Management** — live in-room conduct, devices, behavior. Different time orientation (during teaching vs before teaching).
7. **vs Daycare/Preschool Management** — per that leaf's research, the learning/curriculum layer inside care-operator products serves program documentation; the dedicated lesson-planning Type is teacher authoring tooling. Consistent.
8. **vs Note-taking / Document Editor** — generic editors lack the schedule frame, the teaching-occasion placement, and pedagogical structure. A teacher can use a word processor for plans; that does not make the word processor a lesson planner.
9. **vs Assignment Management** — assignments are student work issued and tracked; lesson plans are instructional intention. Adjacent in the LMS neighborhood, different object.

"去掉什么就变成另一个 Type" summary: remove the schedule frame → plan-writing tool or content library; remove the lesson content → timetable; remove the teacher-facing loop and add student delivery → LMS; move the center to institution maps/approval → Curriculum Management; remove the personal planbook and distribute plans as content → Educational Content Platform.

## Uncertainties

- Planbook.com and OnCourse Lesson Planner could not be fetched; both are known market names in this category, but no claims about them are made anywhere in this research or the final document.
- PowerSchool C&I evidence is index-level; operational details of its lesson planner (exact editor structure, sharing model) are unverified.
- Exact bump semantics in products other than PlanbookEdu are asserted only where their pages state them (Common Planner: one-click bump "keeping pacing intact").
- Homeschool and higher-ed usage of this Type was not sampled; the sample is K-12/international-school dominant. The definition does not depend on school level, but market weighting does.
- The relative market weight of solo planners vs platform modules may be shifting toward platform modules (Toddle/PowerSchool pattern); not quantified here.

## Final Synthesis

A Lesson Planning Application is the teacher's schedule-coupled instructional planning application. Its defining core is three jointly-held structures: (1) the lesson plan of record — a persistent teacher-authored record of intended instruction placed at a specific teaching occasion; (2) the teaching schedule as the organizing frame — the planbook grid of classes/periods across a school-year calendar, planned ahead of teaching and shifted when reality disrupts the schedule; (3) the plan→teach→adjust loop with accumulation — drafting, refining, teaching from, annotating, reusing, and rolling plans over year to year as the teacher's planning archive.

Everything else the market associates with the category — standards alignment, files, templates, sharing, admin review, unit layers, analytics, AI — is standard mature capability or variant, not definition. The Type sits directly beneath Curriculum Management (institution layer) and beside the LMS (delivery layer); the layer seams are clean and the joint-review flag from the curriculum-management pass is discharged with a keep-both verdict.
