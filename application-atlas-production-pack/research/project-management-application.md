# Research Notes — Project Management Application

Research date: 2026-09-08
Directory leaf: "Project Management Application" (§03.07 Project & Work Management)
Slug: project-management-application

## Research Goal

Understand the Project Management Application as an Application Type: what objects exist inside it (project, task, dependency, milestone, resource, view, report), how planned work is scheduled and tracked, which capabilities are definitional vs common vs variant, and where the boundary sits against the many neighboring Types that share its vocabulary (Agile PM, Task Management, Kanban Task Board, Work Management Platform, PPM, Construction PM, Engineering PM, PSA, Collaborative Workspace, Customer Onboarding Platform).

This leaf carries a **pre-recorded joint-review flag** from the agile-project-management-application pass (STATUS 2026-09-06): "general PM centers a fixed task schedule (dependencies/milestones/baselines/resource leveling) measured by percent-complete; agile PM re-plans a living ordered backlog at each cadence boundary" — to be ratified or refined from this side.

## Initial Boundary

- **Working hypothesis going in**: a PM application is the system of record for managing a bounded planned undertaking (project) as a whole — decompose the work into scheduled, owned, completable units, coordinate their order, track progress against the plan, revise the plan.
- **Nearest neighbors** (per DIRECTORY and prior passes): Agile Project Management Application (03.07, processed); Task Management Application + To-do List Application (03.06, unprocessed); Kanban Task Board (03.06, processed); Work Management Platform (03.07, unprocessed); Project Portfolio Management Application (03.07, unprocessed); Construction Project Management (§17, processed); Engineering Project Management Platform (§12, processed); Professional Services Automation (§10, unprocessed); Collaborative Workspace (03.12, processed); Customer Onboarding Platform (processed); Workflow Management Platform (processed).
- **Known recorded seams I must hold or refine**:
  - agile pass: planning-philosophy boundary (backlog+cadence vs fixed schedule+percent-complete); Gantt-like timelines are optional overlays in agile products.
  - construction pass: generic PM = single-organization team; construction PM adds multi-org contractual community + formal cross-party workflow machinery.
  - engineering-PM pass: general PM has no code-change binding; percent-of-plan vs completed-items measurement.
  - kanban pass: board-as-record vs board-as-projection-view.
  - customer-onboarding pass: two-sided (vendor+customer) work distribution vs internal project execution.
  - M&E pass note: activities in M&E platforms are reporting units, not schedulable managed work.

## Research Questions

1. What is the "project" object? What identifies and bounds it (name, dates, membership, goal)?
2. How is work structured inside a project (groupings, hierarchy/WBS, subtasks)? What does a task carry (owner, dates, status, completion)?
3. Which scheduling machinery exists — dates, durations, dependencies/links, auto-scheduling, critical path, milestones, baselines, resource leveling? Which are universal vs lineage-specific?
4. How do people/resources attach to work (assignment, workload/allocation views)?
5. How is progress measured and rolled up (percent complete, status, overdue/late, health)? Is there a project lifecycle (active → complete → archived)?
6. What interfaces do users actually face (project list/home, list/grid, board, calendar, Gantt/timeline, task detail, dashboards, admin/permissions)?
7. What rules matter (dependency blocking, rollup semantics, computed status, permission/visibility incl. clients)?
8. What exceptions are structural (overdue work, blocked tasks, scope change mid-project, re-planning, over-allocation)?
9. Historical check: would a pre-software or regional product still fit the definition?
10. Boundary tests vs each neighbor; what to record as flags for unprocessed siblings.

## Representative Products

Selected for market representativeness + different product philosophies + different customer tiers:

| Product | Pole | Evidence level |
|---|---|---|
| Microsoft Planner (premium plans; formerly Microsoft Project / Project for the web) | Classic scheduling lineage absorbed into a suite; Microsoft's own tiering of "task" vs "project" features | Tier-1: official comparison article + Project for the web limits (learn.microsoft.com) |
| Teamwork.com | Mid-market client-work/agency PM with scheduling + profitability machinery | Tier-1: four official support articles (Gantt, dependencies, project statuses, percent-complete) |
| Smartsheet | Spreadsheet-idiom work/project management, strong Gantt/dependencies, portfolio layer (Control Center) | Tier-1: two official help/learning articles (project sheet setup incl. dependencies rollup) |
| Basecamp | Opinionated lightweight anti-Gantt pole; boundary-stressor for L0 minimality | Tier-2: official features page (help-center article bodies JS-inert) |
| Asana | Modern collaborative work/project management, huge market presence | **No first-hand evidence** — both official doc portals JS-blocked (Salesforce CSS error ×2); market-recognizability only |

## Sources

- Microsoft Support — "Compare Microsoft Planner basic vs. premium plans" — https://support.microsoft.com/en-us/planner/compare-microsoft-planner-basic-vs-premium-plans (fetched 2026-09-08)
- Microsoft Learn — "Project for the web limits and boundaries" — https://learn.microsoft.com/project-for-the-web/project-for-the-web-limits-and-boundaries (fetched 2026-09-08; notes Project for the web becoming Microsoft Planner)
- Teamwork.com Support — "Viewing Your Project in a Gantt Chart" — https://support.teamwork.com/projects/planning-managing-work/viewing-your-project-in-a-gantt-chart (fetched 2026-09-08)
- Teamwork.com Support — "Creating Task Dependencies in the Gantt Chart" — https://support.teamwork.com/projects/project-sections/creating-task-dependencies-in-the-gantt-chart (fetched 2026-09-08)
- Teamwork.com Support — "Understanding Project Statuses" — https://support.teamwork.com/projects/planning-managing-work/project-statuses (fetched 2026-09-08)
- Teamwork.com Support — "Percentage Complete Calculation for Task Lists on the Gantt Chart" — https://support.teamwork.com/projects/project-sections/percentage-complete-calculation-for-task-lists-on-the-gantt-chart (fetched 2026-09-08)
- Teamwork.com Support Center tree — https://support.teamwork.com/projects/ (task lists, milestones, cross-project dependencies, permissions, client users, time tracking; fetched 2026-09-08)
- Teamwork.com product pages (resource management, capacity, budgets/profitability) — https://www.teamwork.com nav (Tier-2, fetched 2026-09-08)
- Smartsheet Help Center — "Set up your project sheet" — https://help.smartsheet.com/learning-track/project-fundamentals-part-1-intake-archive/set-your-project-sheet (fetched 2026-09-08)
- Smartsheet Help Center — "Create a project sheet" — https://help.smartsheet.com/learning-track/project-fundamentals-part-1-intake-archive/create-project-sheet (fetched 2026-09-08)
- Basecamp — Features page — https://basecamp.com/features (fetched 2026-09-08)

**Source-access limitations**: help.asana.com and asana.com/guide both returned a Salesforce "CSS Error" (JS-required) on two attempts — Asana dropped to market-recognizable status with zero first-hand claims. Basecamp's Help Scout category pages render no article links without JS; the official features page was used instead (structure-level claims only). Classic Microsoft Project desktop documentation was not directly reachable (support.microsoft.com/en-us/project now redirects to the Planner hub); the Planner-premium comparison and Project for the web limits serve as the Microsoft Tier-1 layer. Baselines, resource leveling, effort-driven scheduling, and critical-path semantics were NOT verified in any product's operational documentation this pass (named only in Planner's premium feature list; Smartsheet's import note corroborates that constraint-based scheduling belongs to the Microsoft Project lineage) — held at lineage-characteristic strength, no semantics asserted. No market-share, pricing, or numeric-limit claims are made in the final document.

## Product Observations

### Microsoft Planner (premium plans; Project lineage) — evidence layer A

- Microsoft's own two-tier split: **Basic** plan (Grid view, Board view, Charts view, filter/group, assigned-to-me, copy plan, To Do integration, task conversations) vs **Premium-only** ("View tasks in Timeline (Gantt chart)", "Add dependencies between tasks", "Add milestones, task custom fields, conditional coloring", "See critical path in the plan", "People view – see where team members may be over- or under-allocated and find potential opportunities for workload balancing", "Goals", "Custom calendars", "Task history"). **This is vendor-documented tiering of generic task machinery vs project machinery inside one product.**
- Premium plan also ships "**Agile PM with backlogs and sprints**" as a separate feature family alongside the timeline/dependency machinery — the same product holds both the general-PM and agile-PM feature families (straddle evidence).
- Project for the web limits (Tier-1): project = container with tasks; **maximum hierarchy level 10** (summary tasks are structural); "links (successor + predecessor)" per task ≤ 20 (max 2000 per project); resources assigned to tasks (≤ 20 per task); durations for leaf and summary tasks; custom fields; goals. The classic object vocabulary (project → summary task → task, links, resources) is confirmed from official docs.
- Project for the web "will soon become Microsoft Planner" — the Project lineage is being folded into the Planner brand; premium plans carry the former Project capabilities.
- Basic plan keeps "Schedule view" (calendar-ish) as a basic feature; premium moves Gantt-grade timeline in.

### Teamwork.com — evidence layer A

- **Project container**: "Create a Project", "Adding People to a Project", project administrators, per-project permissions; companies "Owner and External" + "Client Users" (client participation is a first-class access concept). Project areas include tasks, messages, files, notebooks, milestones (support-center blurb: "manage projects and tasks, track time, create milestones, share files").
- **Work structure**: projects contain **task lists → tasks → subtasks**; "Tasks (List) View" across projects; repeating tasks; estimated time per task.
- **Gantt view (Tier-1 article)**: per-project Gantt tab; left pane lists task lists/tasks/subtasks with **a completion percentage that tracks progress when tasks complete**; timeline with months/days, weekends highlighted; tasks as colored bars (color bound to assigned person); **task lists bracketed by earliest start / latest due**; **dependencies drawn as arrow lines between tasks**; **milestones as diamonds attached to their task list** on the due day; show-completed toggle; export/print.
- **Dependencies (Tier-1 article)**: created by dragging between tasks; purpose stated as "make sure the tasks are completed in a particular order"; **the dependent task's completion checkmark is replaced by a red blocked-dependency icon — "the task cannot be completed until the first task is completed"**. Cross-project dependencies supported (tree). So dependencies act as both schedule links and workflow constraints.
- **Percent-complete rollup (Tier-1 article)**: task-list progress = **duration-weighted formula ∑(duration × progress) / ∑duration over active tasks**; **subtask progress does NOT roll into parent task progress** ("the progress of subtasks does not affect the progress of the parent task at all"); completed tasks are excluded from the calculation unless "Show Completed" is enabled — with a worked numeric example.
- **Project statuses (Tier-1 article)**: statuses group projects by "where they are in their current timeline" — **all / active / late ("passed its due date, not yet marked complete, still contains active items") / upcoming ("start date later than today") / complete (marked as complete) / archived** — each with counts; site administrators see all projects even if not members.
- **Adjacent commercial machinery (Tier-2 nav)**: resource management, capacity planning, resource forecasting, utilization, time tracking with timesheet approval, budgets & profitability, quoting/costing, retainer budgets, invoice export to accounting — the client-work/PSA-grade pole.

### Smartsheet — evidence layer A

- **Project sheet**: a project is realized as a sheet created from a project template ("Simple Project Plan"), import (Excel, **Microsoft Project .mpp/.mpx/.mspdi/.xml**, Google Sheets, Trello) — Microsoft Project file import is officially documented, anchoring lineage continuity.
- **Hierarchy**: rows indented into parent/child (phases → tasks); **"If your sheet has dependencies enabled, parent rows automatically reflect a roll-up summary of the Start Date, End Date, Duration, and % Complete values from their child rows"** (Tier-1) — dependencies are an **enabling switch** that activates scheduling semantics + parent rollup.
- **Views** (help-center category): "Visualize your project using **timeline, board, grid, Gantt, card, and calendar views**" — one body of work, multiple projections.
- Import caveat (Tier-1): "Microsoft Project has some features, **such as constraints**, that aren't supported in Smartsheet" — corroborates that constraint-driven scheduling is a Microsoft-Project-lineage characteristic, not universal.
- Adjacent machinery: dashboards, reports, forms/intake, automated workflows, Control Center ("Standardize, automate, and scale project and portfolio management"), WorkApps, Resource Management premium (time/expense, projects), document builder. Smartsheet's own category straddles project management and work management.

### Basecamp — evidence layer B/A− (official features page, Tier-2)

- **"Every project you create gets a dedicated page"** — the project is a page/container assembled from built-in tools: **to-dos, message boards, chat rooms, a calendar, kanban card tables**, docs & files, automatic check-ins; invite co-workers, clients, volunteers.
- **To-do lists**: "Make a list, or ten lists… Assign items, set due dates, have discussions, attach files, even create subtasks. Drag items between lists. Set up who gets notified when a to-do is completed."
- **Progress machinery without Gantt/percent**: **Hill Charts** ("where things really stand… Is the project going to be done on time? Are people stuck?"); **Reports**: The Lineup (projects plotted on a timeline), Mission Control (every project's status in one view), Hilltop, Added/Completed, **Overdue ("everything that's late")**, Unassigned, Timesheets; Everything Views; personal "My Tasks".
- **Calendar** covers "deadlines, milestones, events, meetings" — milestones as calendar entries, not schedule objects; global calendar aggregates per-project calendars.
- **Client mode**: per-project control of what clients see.
- **Notably absent**: no dependencies, no Gantt/timeline editing, no baselines, no critical path, no resource leveling, no percent-complete rollups. Yet Basecamp is universally recognized as project management software. **This is the pole that forces L0 minimality.**

### Asana — no first-hand evidence

- Official help center and guide both JS-blocked (recorded). Market position as a leading collaborative work/project management tool is common knowledge in the category but is NOT used to support any structural claim. Listed in Representative Products for market anchoring only.

## Cross-product Comparison

| Dimension | Planner premium (MS) | Teamwork | Smartsheet | Basecamp | Layer |
|---|---|---|---|---|---|
| Project = persistent identified container with people + time span | Yes (plan/project with tasks, goals) | Yes (project + members + dates) | Yes (project sheet in workspace) | Yes (project page + invited people) | A (4/4) |
| Work = discrete completable items with owner + dates | Yes (tasks, assigned-to-me) | Yes (tasks/subtasks + assignee + start/due) | Yes (rows + contact list + date columns) | Yes (to-dos: assign, due dates) | A (4/4) |
| Decomposition/structure (groups, hierarchy, subtasks) | Summary-task hierarchy (≤10 levels) | Task lists → tasks → subtasks | Row hierarchy (indent, phases) | To-do lists; subtasks; card tables | A (4/4) |
| Completion of items tracked | Yes (completion state) | Yes (checkmark; blockable) | Yes (checkbox/rollup) | Yes (check-off + notification) | A (4/4) |
| Project-level progress picture | Charts view; timeline with milestones | % complete per list (duration-weighted); statuses incl. late | Parent rollup of dates/%complete; dashboards/reports | Hill charts; Mission Control; Overdue report | A (4/4), form varies |
| Multiple views over same work | Grid / Board / Charts / Timeline | List / Gantt / Calendar | Grid / Gantt / Board / Card / Calendar / Timeline | Lists / Card Table / Calendar | A (4/4) |
| Milestones | Premium feature | Diamond schedule object on task list | (not verified this pass) | Calendar entries | A (3/4 verified) |
| Dependency links between tasks | Premium ("add dependencies between tasks") | Yes; arrow links; **block completion until predecessor done** | Yes (dependencies-enabled sheets; schedule semantics) | **Absent** | A (3/4) |
| Gantt/timeline view | Premium Timeline (Gantt) | Gantt tab per project | Gantt view | **Absent** | A (3/4) |
| Critical path | Premium feature | Not verified | Not verified | Absent | A (1/4 named) |
| Resource allocation / workload view | Premium "People view" (over/under-allocation) | Resource management product line (Tier-2) | Resource Management premium add-on | Absent (someone's assignments report only) | A/B (2 verified + 2 partial) |
| Baselines / plan-vs-actual | Named in lineage, not verified this pass | Not verified | Not verified | Absent | Unverified → variant-tier |
| Task comments/attachments | Task conversations (basic) | Discussions on tasks; files | Discussions/attachments | Discussions + files on to-dos | A (4/4) |
| Templates for new projects | Copy plan | (importers from Asana/Basecamp/Wrike documented) | Project templates officially documented | Project templates/tools on page | A/B |
| Project lifecycle states | (not verified) | active / late / upcoming / complete / archived | (not verified as named states) | (status via reports; no verified lifecycle set) | A (1/4 detailed) → conceptual states, labels vary |
| Client/external visibility control | (not verified) | Client Users + External companies | Sharing/WorkApps | Client mode per project | A (2 verified) + B |
| Time tracking on tasks | Absent (basic) | Yes (timers, timesheets, approval) | Premium Resource Management | Timesheets report | B — common, not definitional |
| Billing/profitability | Absent | Budgets, profitability, invoice export | Absent in PM core | Absent | Vendor/segment pole (Teamwork) |
| Agile feature family (backlog/sprints) | Premium ships it as separate family | Agile hub (marketing) | (not core) | Absent | Straddle machinery, not definitional |
| Portfolio/program layer above projects | Goals (premium) | (PSA hierarchy reference guide) | Control Center (portfolio standardization) | Lineup (light) | B — common above-seam layer |

## Canonical Model (abstraction)

### L0 — Defining Invariant (jointly held; deliberately small)

1. **The project as the unit of record** — a persistent, identified container for one bounded undertaking: a name/identity, an intended time span, and the people who will do the work. Everything else in the system attaches to it. Remove → work items floating in a task manager, or a content/discussion workspace.
2. **The planned decomposition of the undertaking** — the project's work is held as discrete completable units (tasks), organized in structure (groupings/hierarchy), each carrying an owner and a place in time (dates), constituting a plan of record that exists before and during execution. Remove → a container with discussion/docs only (workspace), or an unstructured backlog.
3. **The track-to-completion loop at project scope** — completion/date state of the units accumulates into a project-level picture of progress and health (however computed: percent complete, status incl. late/complete, overdue views, subjective positioning charts), which the system surfaces to the people accountable, who then adjust the plan. Remove → a static planning document or a check-off board with no management surface.

Jointly-held is load-bearing: 1 alone = workspace/register; 2 without 1 = task manager; 3 without 1+2 = status shell; 1+2 without 3 = planning artifact never reconciled with reality; 1+3 without 2 = status without managed work.

**Historical check (§24 analog test)**: a pre-software project — a project file with a work breakdown, a hand-drawn bar chart or CPM network with assigned owners and dates, and progress marks/re-planning against the plan (as-planned vs as-built) — satisfies all three legs. So do 1980s–90s desktop PM (the lineage Microsoft imported), 2000s web PM, and modern work-OS products. Definition names no Gantt chart, no dependency math, no baselines, no cloud/AI — all are era/segment machinery. PAPER-ERA FIT CONFIRMED.

### L1 — Common Mature Structure (very common, not defining)

- milestones (as schedule objects in scheduling products; as calendar entries in lightweight products)
- dependency links between work units, with order-enforcement and often completion-blocking
- multiple synchronized views over the same work body (list/grid, board, calendar, timeline/Gantt)
- subtasks; grouping into phases/lists; task comments/attachments
- templates instantiated per new project
- task-level completion marks and (in many) percent-complete values; duration-weighted or count-based rollups
- project-level status grouping (active/late/upcoming/complete), overdue surfacing
- reporting/dashboards at and above project level; activity feeds
- notifications; my-work personal views across projects
- project membership roles/permissions; external/client visibility control
- recurring tasks; cross-project views (all my tasks; all overdue)

### L2 — Variant / Optional Structure

- **Scheduling-intensive machinery** (classic desktop/enterprise lineage): auto-rescheduling from dependency edits, constraints, critical path, float/slack, effort-driven durations, resource leveling, baselines vs actual. Verified as *named premium features* in one sample; semantics not verified anywhere this pass; absent in the lightweight pole. Characteristic of the lineage, NOT of the Type.
- portfolio/program/PPM layer above projects; goals/OKR linkage
- time tracking and (client-work pole) budgets/billing/profitability on the same records
- forms/intake into project work; automation rules; custom fields
- agile feature family (backlogs/sprints) shipped alongside general-PM machinery (Planner premium) — straddle packaging
- document/wiki/chat surfaces inside the project container (workspace-adjacent bundling)
- AI assistance (era-current: AI teammates, Copilot in Planner, AI writing/forecasting)

### L3 — Vendor-specific (kept out of the final document)

- Basecamp: hill charts, card tables, campfires, automatic check-ins, The Lineup/Mission Control/Hilltop naming, client mode naming
- Smartsheet: sheet/grid idiom, primary column, dependencies as an enabling switch, Control Center, WorkApps, .mpp import workaround notes
- Teamwork: PSA product hierarchy mapping, profitability/budgets machinery, AI teammates/forecasting, "Tentative Work", keyboard-shortcut Gantt
- Microsoft: basic-vs-premium plan packaging, Planner/Project brand migration, exact numeric limits (3000 tasks/project premium, 3650-day project span, 20 links/task, 10-level hierarchy, 20 resources/task, supported date range 2000–2149) — numbers recorded here only, not asserted in the final document
- Teamwork's exact percent-complete formula (∑d*p/∑d) and its completed-tasks-excluded nuance — recorded as evidence that rollup semantics are *product-specific implementations* of the same conceptual rollup

## Rejected Findings

- "PM applications center on Gantt charts" — rejected: the recognized lightweight pole (Basecamp) ships none; Gantt/timeline is 3/4 in-sample, absent in 1. Timeline views are common, not defining.
- "Dependencies are definitional" — rejected: Basecamp (and much real use) has none; even Microsoft gates them behind the premium tier. L1.
- "Percent-complete rollups are definitional" — rejected: Basecamp uses subjective hill charts instead; rollup *form* varies. The invariant is a project-level progress/health picture, not the formula.
- "Resource leveling / baselines define the Type" — rejected: unverified this pass in any product's operational docs; absent in the modern collaborative pole. Held as scheduling-lineage characteristics (L2).
- "PM = Microsoft Project's feature set" — the classic lineage is the historical anchor (and the .mpp import standard), but the market population is broader; anti-overfitting rule applied.
- "Client work/billing is part of PM" — rejected: profitability machinery is the Teamwork pole (client-work segment); not present in the others' PM cores.

## Boundary Findings

1. **vs Agile Project Management Application (03.07 sibling — PRE-FLAGGED JOINT REVIEW, DISCHARGED THIS PASS)**: RATIFIED **keep-both**, with a refinement of the agile pass's characterization. The durable seam is the **planning object**: general PM centers a **one-off bounded undertaking** whose work is planned, scheduled, and tracked to that undertaking's end; agile PM centers a **standing team's ordered backlog** re-planned at each cadence boundary with flow metrics. The agile pass's shorthand for general PM ("fixed task schedule, dependencies/milestones/baselines/resource leveling, percent-complete") accurately describes the **scheduling-heavy lineage** (Microsoft Project-class) — which is indeed what distinguishes it most sharply from agile — but the fuller general-PM population includes recognized products with **no dependencies/Gantt/baselines at all** (Basecamp), so those mechanisms cannot be the wall. Discriminator test holds in both directions: strip backlog/cadence/estimation machinery from a product → the general-PM core (bounded undertaking + planned work + track-to-completion) remains → general PM; strip the bounded undertaking (work flows to a standing backlog forever) → agile PM. The market straddles: Planner premium ships timeline/dependencies AND backlogs/sprints in one product; Jira/Azure Boards span both with separate feature families (agile pass recorded the same). Both documents cross-reference the seam; no directory change proposed.
2. **vs Task Management Application / To-do List Application (03.06, unprocessed — FLAG for joint review)**: task management centers the task as the primary object of everyday individual/team work without an undertaking-level plan of record or project-scope progress machinery; general PM centers the undertaking and its plan. Seam test: remove the project container + plan-to-end loop → task management; add them → PM. Joint review recommended at that pass.
3. **vs Kanban Task Board (03.06, processed)**: consistent with that pass — the board is one *view* over PM work (Basecamp Card Tables, Smartsheet board/card views, Planner board view); board-as-model-of-record with no plan machinery is the other Type. Ratified.
4. **vs Work Management Platform (03.07 sibling, unprocessed — FLAG for joint review)**: center of gravity — PM applications organize **bounded scheduled undertakings**; work management platforms organize a team's **whole ongoing work** (requests, processes, approvals, non-project recurring work) where the project is one container among several. The market blurs hard (Smartsheet and Asana are marketed in both vocabularies; Smartsheet's own help center straddles). Products above the seam should be attributed by center of gravity, not feature lists. Joint review recommended at that pass.
5. **vs Project Portfolio Management Application (03.07 sibling, unprocessed — light flag)**: above-seam layer — portfolio aggregates, selects, and governs many projects; the PM application holds and runs the individual project. Rollup dashboards appear in both; the unit of record differs (portfolio of projects vs the project).
6. **vs Construction Project Management (§17, processed — RATIFIED from this side)**: their seam is confirmed — generic PM serves a **single organization's team** planning and tracking its own work; construction PM adds the **multi-organization contractual community** and formal cross-party instruments. Strip multi-org + instruments → generic PM. No change.
7. **vs Engineering Project Management Platform (§12, processed — RATIFIED)**: confirmed — no code-change binding in this Type; percent-of-plan vs completed-deliverables measurement; schedule machinery here is a first-class native dimension, not an optional overlay. No change.
8. **vs Professional Services Automation (§10, unprocessed — light flag)**: PSA adds billable economics (rates, budgets, invoicing, utilization targets) as the center; PM applications without billing machinery remain this Type. Teamwork realizes both in one suite (packaging overlap, not Type merger), same pattern as Businessmap in the kanban pass.
9. **vs Collaborative Workspace (03.12, processed)**: consistent with that pass's own note — the workspace centers content/discussion with tasks as one content type; the PM application centers the undertaking and its planned work, with discussion/files as attached context. Straddle risk when the structured-data layer becomes the product's center.
10. **vs Customer Onboarding Platform (processed — RATIFIED)**: confirmed — onboarding's per-customer engagement + two-sided work distribution vs internal single-org execution of this Type.
11. **vs M&E Platform (§25, processed — note held)**: activities in M&E platforms are attribution/reporting units, not schedulable managed work — consistent with this pass's L0.
12. **Umbrella note (consistent with construction pass)**: point leaves such as RFI Management, Punch List Management, Daily Log Application, Construction Scheduling etc. are construction-scoped; no equivalent generic point-leaf machinery (e.g., "milestone tracking") exists in DIRECTORY as separate leaves — milestone/dependency views remain capabilities of this Type, not separate Types.

## Uncertainties

- Baselines, critical-path semantics, resource leveling, effort-driven scheduling: named in Planner's premium feature list (A) but no operational documentation fetched for any product — held at lineage-characteristic strength; final document does not assert how they work.
- Smartsheet milestone objects and project lifecycle states: not verified this pass (only views/rollup/dependencies verified).
- Asana: zero first-hand evidence (both doc portals JS-blocked). Its inclusion in Representative Products is for market anchoring only.
- Whether the "project lifecycle (active→complete→archived)" is universal: verified in detail only in Teamwork; Basecamp has reports-based status; held as conceptual states with varying labels.
- Classic Microsoft Project desktop documentation not directly reached (redirect to Planner hub); its inclusion as the classic-lineage anchor rests on the Planner-premium comparison, the Project-for-the-web limits doc, Smartsheet's documented .mpp import with constraint caveat, and general market recognizability.

## Final Synthesis

A Project Management Application is the system of record for a bounded planned undertaking: a persistent project container; its work decomposed into owned, dated, completable units arranged in structure; and a management loop that turns item completion and date state into a project-level progress picture used to steer the work to its end. The scheduling-intensive machinery (dependencies, Gantt math, critical path, baselines, leveling) is the historic differentiating lineage of the category — Microsoft's own premium tier marks it as such — but it is not the defining core: recognized lightweight products operate the same core without it. The Type's edges are drawn by the planning object (bounded undertaking vs standing backlog vs loose tasks vs ongoing work portfolio) and by what is added *around* the core (multi-org contractual community → construction; code binding → engineering PM; billable economics → PSA; customer as worker → onboarding; portfolio governance → PPM).
