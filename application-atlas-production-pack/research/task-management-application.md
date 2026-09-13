# Research Notes — Task Management Application

## Research Goal

Understand the directory leaf **Task Management Application** (§03.06 Tasks, between To-do List Application and Kanban Task Board) as an Application Type from real products: what the unit of record is, what the "management" apparatus consists of, what the working loop looks like, which capabilities are common vs defining, and where the boundary runs against the sibling leaves and neighboring Types.

## Initial Boundary

Provisional understanding before research:

- Core use: organizing work as discrete completable tasks (to-dos) so they can be scheduled, prioritized, delegated, and completed.
- Users: individuals managing their own work and life tasks; small teams and households sharing task lists; larger teams inside heavier work-management packaging.
- Nearest neighbors (all flagged by prior passes):
  - **To-do List Application** (§03.06 sibling, unprocessed) — seam proposed by personal-organizer pass: "work/team subject with assignment/workflow vs personal-life subject".
  - **Kanban Task Board** (§03.06 sibling, processed) — its seam: "task management centers on the task *record* … the kanban board, when present, is a projection view over records".
  - **Project Management Application** (§03.07, processed) — its removal test: "planned decomposition … without the project container = task manager".
  - **Issue Tracker** (§12, processed) — joint-review flag: issue = team-processed work item with issue-population management (triage, backlog, lifecycle, reporting), canonically development/product work; task = personal/team to-do organized for execution.
  - **Work Management Platform** (§03.07, unprocessed) — carried flag from PPM pass.
  - **Calendar Application** (§03.08, processed) — completion state vs clock anchor.
  - **Workflow Management Platform** (§10, processed) — tasks as runtime surface of instances vs individual records.
  - **Household Chore Application** (§29, processed) — explicitly not an audience variant of this Type.
  - **Focus Timer / Life Planning / Meeting Action Item Management** — embedding tests recorded in those passes.
- Unknowns: whether "task management" has a defensible L0 distinct from both the to-do pole and the issue-tracker pole; what the "management" apparatus minimally is; whether assignment/sharing is definitional.

## Research Questions

1. What is the unit of record, and what states does it move through?
2. What organizing structures do products provide (containers, sub-tasks, labels, sections)?
3. What attributes do tasks carry (dates, priority, assignee, duration) and which are definitional vs common?
4. What are the working views over the task population (today/upcoming/calendar/board/filters) and how do they relate to the record model?
5. How does completion work (boolean act, history, recurrence, un-complete, delete/restore)?
6. How do sharing/assignment/collaboration work, and is multi-user definitional?
7. Where does the boundary sit vs To-do List, Kanban Task Board, Issue Tracker, Project Management, Work Management, Calendar, Workflow Management?

## Representative Products

| Product | Pole | Why sampled |
|---|---|---|
| **Todoist** | personal-first cross-platform task manager (freemium + business tier); market's canonical exemplar; self-labels "the world's #1 to-do list app" | market representability + deepest Tier-1 docs |
| **TickTick** | personal productivity bundle (tasks + calendar + pomodoro + habits + Eisenhower matrix) | different product philosophy (bundled productivity suite) |
| **Asana** | team/work pole; markets itself as "work management platform built for scale" with goals/portfolios/workflows | different customer tier; tests the work-management seam |
| **Microsoft To Do** (counterparty) | platform-native personal to-do pole; list-centric; stored on Exchange, integrated with Outlook | anchors the to-do seam |
| **Remember The Milk** (counterparty) | veteran web-native task/to-do app; reminders-centric; sharing lists | historical/web-era pole, personal+shared |

Evidence layers: **A** = directly observed on official pages of that product; **B** = cross-product commonality across the sample; **C** = canonical inference from comparison + boundary reasoning.

## Sources

Todoist (all fetched 2026-09-09, Tier 1):
- Help Center root: https://www.todoist.com/help
- Features hub: https://www.todoist.com/help/todoist/features (feature taxonomy incl. Tasks & Planning, Views/Filters & Labels, Projects & Sections, Reminders, Karma, Teams, AI, Integrations)
- "Introduction to tasks": https://www.todoist.com/help/todoist/features/introduction-to-tasks-080OAXric
- "Introduction to projects": https://www.todoist.com/help/todoist/features/introduction-to-projects-TLTjNftLM
- "Use the board layout in Todoist": https://www.todoist.com/help/todoist/features/use-the-board-layout-in-todoist-AiAVsyEI
- Marketing home (self-positioning): https://www.todoist.com/ ("world's #1 to-do list app"; "19 years" of operation; capture/scheduling/teamwork pillars)

TickTick:
- Help Center root: https://support.ticktick.com/ (redirects to help.ticktick.com; Feature Guide taxonomy: Task, Calendar, Matrix, Focus, Habit, Countdown; unique features: Timeline, widgets, sticky notes, notes, shortcuts) — Tier 1 (fetched 2026-09-09)
- Features page: https://ticktick.com/about/features (capture: NLP/voice/widgets/integrations; lists/filters/tags; reminder types incl. constant/location/repeat; calendar views; list/kanban/timeline modes; habit/pomodoro/Eisenhower/countdown; collaboration: share lists + assign; statistics) — Tier 2 (fetched 2026-09-09)

Microsoft To Do:
- Help hub: https://support.microsoft.com/en-us/todo (nav taxonomy: Lists, Tasks, My Day, To Do in Outlook, sharing) — Tier 1 (fetched 2026-09-09)
- "Create, edit, delete, and restore tasks": https://support.microsoft.com/en-us/ToDo/create-edit-delete-and-restore-tasks (CRUD; Exchange Online storage; visible in Outlook Tasks; restore via Outlook Deleted Items) — Tier 1 (fetched 2026-09-09)

Asana (Help Center help.asana.com is a JS shell — CSS error on fetch; degraded to Tier 2):
- Product page: https://asana.com/product (positioning; FAQ incl. "Can you use Asana for personal use?") — fetched 2026-09-09
- Project management features page + FAQ: https://asana.com/features/project-management (projects/tasks/views/custom fields/inbox/my tasks; plan tiers; dependencies; multi-project membership; task-in-up-to-20-projects claim) — fetched 2026-09-09

Remember The Milk:
- Home: https://www.rememberthemilk.com/ (self-presentation: "smart to-do app for busy people"; NL input examples; reminders; "Share your lists and give tasks to others"; sync; AI/MCP) — Tier 1 root only (fetched 2026-09-09). Help guide not fetched this pass.

## Product A — Todoist (evidence layer A)

- **Task as unit of record** ("Introduction to tasks"): tasks added anywhere via **Quick Add** with natural language ("*Call Mom today*", "*Write thesis introduction at 2 PM for 3 hours*"); a task has name, optional **description**, **date/time** (fixed or floating), **priority**, **labels**, **reminders**, **comments/files**, **sub-tasks**; every task has a **circle icon** — completing it "disappears from the list, it's recorded in your Reporting, and counted as a point to your Karma"; **un-complete** restores it (view must show completed tasks); **uncompleting sub-tasks automatically uncompletes their parent task**; delete is unrecoverable for free tier (paid backups); **recurring dates** — completing an occurrence with a brief undo popup, previous occurrences cannot be uncompleted; "**Create an uncompletable task**" exists as a distinct option.
- **Organization** ("Introduction to projects"): two environments — **My Projects** (personal, sub-projects allowed, restricted by default) vs **Team projects** (team-owned, browsable by members, **folders** instead of sub-projects, restricted-project option); **Inbox** = default landing container for tasks without a project; **sections** subdivide a project; **templates**; project **archive/delete/restore**; shared projects give collaborators full edit rights ("add new tasks, **assign tasks**, complete tasks, add comments, upload files"); **favorites**; project colors; plan-tier project limits (5/300/500) and 21 backups stated in help (L3 detail).
- **Views over the population**: navigation includes **Today**, **Upcoming**, **filters**, **labels**; view layouts switchable per view: **list / board / calendar** (calendar Pro/Business); **board layout**: "tasks are displayed as cards. Each section is displayed as a column"; sections "represent phases"; drag between columns; **layout is a display setting that syncs for everyone** in a shared project — switchable back to list/calendar without changing data; sort/group options; **search**; **Reporting** (completed-tasks records) and **Karma** (productivity feedback).
- **Positioning**: "A To-Do List to Organize Your Work & Life"; pillars: capture ("at the speed of thought"), organize ("Today, Upcoming, or using custom filters"), plan ("due dates, calendar view, recurring tasks"), teamwork ("a shared space … alongside but separate from your personal tasks and projects").

## Product B — TickTick (evidence layer A root + A/B feature page)

- Help Center Feature Guide structure: **Task** ("To-do list, Free Your Mind": Add Tasks, Effective Reminder, Group & Sort, **Kanban View**, **Timeline View**), **Calendar**, **Matrix** (Eisenhower), **Focus** (pomodoro/timer/statistics), **Habit**, **Countdown** — the task manager is the trunk with calendar/focus/habit bundled.
- Features page: capture (NLP date parsing, voice input, widgets, email/browser integrations, Google Calendar task add); organize with **lists**, **smart filters**, **tags**; reminders (multiple alert times, **constant reminder** until done, email, **repeat rules** weekly/monthly/yearly/custom, **location**, daily planning reminder); **views: list (3-column), kanban ("tasks are organized into columns based on your chosen grouping"), timeline ("lighter project management tool compared to Gantt charts", drag to adjust durations)**; productivity tools (habit tracker, pomodoro, Eisenhower matrix, countdown); **collaboration: "Share lists with friends and colleagues, assign tasks"**; statistics; themes; time zones.
- Reading: the bundling is extensive, but the trunk record model is the task on lists with dates/priority/reminders — the same grammar as Todoist with a broader periphery.

## Product C — Asana (evidence layer A- for positioning, A-/B for structure)

- Help Center is a JS shell (CSS error, fetch failed ×1) — degraded per evidence rules; structure below is from official product/features pages (Tier 2).
- Positioning: "work management platform built for scale"; modules: agentic AI workflows, service management, client management, workflow automation, project management, goals & reporting, resource management, admin & security. FAQ: "Can you use Asana for personal use? Yes… organize personal tasks."
- Task machinery (features page + FAQ): **Projects** as "single shared hub" organizing **tasks**; "**Tasks — break work into bite-size pieces with clear owners and due dates**"; **five project views: list, board ("Kanban boards, backlog work, issue tracking"), calendar, timeline, Gantt**; same tasks/owners/due dates/dependencies/comments appear in each view, switchable without changing setup; **My Tasks — "see all your assignments in one place, so you can prioritize what's next"**; **Inbox — notification center** for assignments/comments/due-date changes; **custom fields** (Starter+); **dependencies** (waiting-on/blocking, for sequencing/handoffs); multi-project membership (task "can belong to up to 20 projects" — vendor FAQ figure, L3); plan tiers gate fields/forms/rules/timeline (L3).
- Reading: Asana's task layer is the same record grammar (owner, due date, views), but the product's center of gravity sits above it (goals, portfolios, workflows, reporting) — the strongest evidence for the work-management seam.

## Product D — Microsoft To Do (counterparty, to-do pole; evidence layer A)

- Help hub taxonomy: **Lists** (organize, **assign shared tasks**, sort/search, share), **Tasks** (create/edit/delete/restore, due dates & reminders, **smart due-date recognition**, "importance, tags & categories", files, move between lists), **My Day** ("for daily focus" + suggestions), **To Do in Outlook** (tasks from flagged email; drag task to calendar), daily habits, sync.
- CRUD article: tasks created from an input field in any list; detail view edits; delete confirmation; **"your tasks are stored on Exchange Online and are also visible in Outlook Tasks"**; deleted tasks recoverable through Outlook's Deleted Items.
- Reading: list-centric containers + task records with dates/importance + My Day smart view + sharing with assignment. Structurally this *already carries* much of the task-management apparatus — direct evidence that the to-do/task boundary is a center-of-gravity judgment, not a hard structural wall. What To Do's docs do not present: multi-container organizing depth (sub-projects/folders), board/timeline layouts, filters, activity reporting — the "management" layer is thinner.

## Product E — Remember The Milk (counterparty, veteran web pole; evidence layer A root)

- Self-presentation: "**The smart to-do app for busy people**"; NL task entry ("Pick up the milk tomorrow. Call Bob at 5pm Thursday."); "Get to-dos out of your head"; "Get reminded, anywhere"; "**Get things done, together. Share your lists and give tasks to others**"; "magically in sync on all your devices"; AI/MCP integration ("Add tasks, organize your lists, and figure out what to focus on").
- Reading: a two-decade-old web-native product still matching the same trunk grammar (capture, dates, reminders, shared lists, sync). Founding year not stated on fetched page (not asserted).

## Cross-product Comparison

| Dimension | Todoist | TickTick | Asana | Microsoft To Do | Remember The Milk | Layer |
|---|---|---|---|---|---|---|
| Task = unit of record with open→done | yes (circle icon; Reporting) | yes | yes ("clear owners and due dates") | yes (detail view, restore) | yes | B |
| Containers above the flat list | projects/sections/sub-projects (personal), folders (team) | lists | projects (+sub-objects) | lists | lists | B |
| Sub-task decomposition | yes (parent-child; uncomplete cascades) | yes (group & sort docs) | yes ("bite-size pieces") | steps | yes (help not fetched; homepage level) | B (E: A-) |
| Due dates + recurrence | yes (NL dates, recurring dates w/ undo) | yes (repeat rules) | yes (due dates; dependencies paid) | yes (smart due-date recognition) | yes (NL dates) | B |
| Priority machinery | yes (priority levels) | yes (Eisenhower matrix) | custom fields (paid) | importance | — (not on fetched page) | B |
| Reminders/notifications | yes (incl. location, paid custom) | yes (multiple alerts, constant, location) | yes (Inbox notifications) | yes | yes (signature) | B |
| Assignment to others | yes (assign in shared projects) | yes (share lists, assign) | yes ("clear owners") | yes (assign shared tasks) | yes (give tasks to others) | B |
| Population views | Today/Upcoming/filters/labels; list/board/calendar layouts | lists/filters; list/kanban/timeline; calendar | list/board/calendar/timeline/Gantt; My Tasks; Inbox | My Day/Planned/Flagged/Assigned | (smart lists claimed historically; not on fetched page) | B |
| Board as a layout over records | yes — "view icon → Board"; sections become columns; switchable, synced | yes ("chosen grouping") | yes (board = one of five views) | no board observed | no | B |
| Completed-task history/reporting | Reporting + Karma | statistics | status updates/reporting (above task layer) | completed tasks visible; restore | — | B |
| Bundled periphery | Karma; productivity methods | calendar/pomodoro/habit/matrix/countdown | goals/portfolios/workflows/AI | Outlook/flagged email integration | AI/MCP | vendor-specific |
| Storage substrate | cloud sync | cloud sync | cloud | Exchange Online + Outlook Tasks | cloud sync | vendor-specific |

## Canonical Model

### L0 — Defining Invariant (jointly held; remove any one and the Type is unrecognizable)

1. **The task as the unit of record.** A persistent, individually addressable record of one discrete completable item of work; its defining state change is **open → done** (a completion act), with the record carrying the work's content (title, notes, attachments) and its execution attributes. (Remove → a note pile or discussion thread; nothing to complete.)
2. **Managed organization of the task population.** The user deliberately organizes tasks into managed structures — containers (projects/lists/sections), decomposition (sub-tasks), classification (labels/tags/priority) — so the population is navigable and actionable rather than a single capture list. (Remove → a flat checklist: the to-do pole. Promote the container to a bounded-undertaking plan of record → Project Management territory.)
3. **Execution views over the population.** The application re-arranges the whole task population into working surfaces — today/upcoming, calendar, board, filters/smart lists, search/sort/group — driven by the tasks' own attributes (dates, priority, assignee), and the user works *from* these surfaces; completion updates the population. (Remove → a static filing cabinet of lists; the app stops organizing work.)

Load-bearing jointly: 1 alone = a checkable-note store; 2 without 1 = empty containers; 3 without 1+2 = a dashboard over nothing; 1+2 without 3 = storage, not an execution system; 1+3 without 2 = undifferentiated lists (to-do pole). The **record grammar is two-state (open/done) with derived urgency (overdue/due today)** — richer custom multi-stage workflows are neighboring-Type machinery.

### L1 — Common Mature Structure (market-expected, not defining)

- due dates with natural-language date entry and reminders (time/location/multiple alerts)
- recurrence rules (task re-materializes after completion)
- priority levels and labels/tags
- sub-tasks / checklists
- shared containers with **assignment** (collaborator-level granularity, not org chart)
- comments and attachments on tasks
- multiple view layouts (list/board/calendar; timeline in some)
- saved filters / smart lists (Today, Upcoming, Assigned to me)
- completed-task history; activity/log
- notifications; cross-platform sync; quick-add (global shortcut, email/voice capture)
- templates for repeating setups

### L2 — Variant / Optional Structure

- personal vs team workspace separation (separate personal and team project spaces in one account)
- bundled productivity periphery: calendar with subscriptions, pomodoro/focus timer, habit tracker, Eisenhower matrix, countdowns (bundled suite pole)
- heavier packaging above the task layer: custom fields, dependencies with blocking semantics, forms/intake, portfolio/goal/reporting layers, admin consoles (work-management/enterprise pole; plan-gated)
- gamification/motivation layers (streaks, scores)
- storage/substrate posture: cloud sync, platform account (Exchange), offline modes
- AI assistance (capture from text/images, suggested dates, drafting)

### L3 — Vendor-specific (kept out of the final document)

- Todoist: plan-tier project limits (5/300/500), 21 backups, Karma scoring, uncompletable tasks, recurring-occurrence undo behavior, uncomplete-cascades-to-parent rule, "19 years" longevity claim.
- TickTick: constant reminder until completion, three-column desktop list layout, timeline "lighter Gantt" framing, 40+ themes.
- Asana: task-in-up-to-20-projects figure, desktop pomodoro timer, plan-gated custom fields/forms/rules/timeline, agentic AI modules.
- Microsoft To Do: Exchange Online storage, visibility in Outlook Tasks, restore via Outlook Deleted Items, flagged-email→task bridge.
- Remember The Milk: MCP/AI-assistant integration.

## Vendor-specific Findings

See L3 above; plus: Todoist's own marketing straddles the to-do/task vocabulary ("the world's #1 to-do list app" while its help center is organized around "tasks & planning") — direct Tier-1 evidence that the market treats to-do and task management as one vocabulary continuum (see Boundary Findings #4).

## Boundary Findings

1. **vs Issue Tracker (§12, processed) — JOINT REVIEW DISCHARGED from this side; keep-both.** The issue-tracker pass held: "the issue is a team-processed work item in a shared product/project container whose population is managed (triage, backlog, assignment, lifecycle, reporting), canonically about development/product work; the task is a personal/team to-do organized for execution without the issue-population management character." Confirmed with fresh evidence: task-management products center a **two-state record grammar** (open→done) with derived urgency, personal-first organization, and no triage/backlog/workflow/population-reporting machinery as the primary loop (sample: none of the five presents custom workflow states as the record model; Asana's dependencies are plan-gated adjacent machinery). Removal tests: strip triage/backlog/workflow/reporting from an issue tracker → a task list remains; add issue-population management to a task manager → it is functioning as an issue tracker. Market blur acknowledged and mutual (Jira markets task management; Todoist ships an "Issue Tracking" template).
2. **vs Kanban Task Board (§03.06 sibling, processed) — keep-both confirmed from this side with direct Tier-1 evidence.** The kanban pass held the seam at "board as primary working surface and model of record … not a projection view over task records — remove → task list / task-management territory". This pass's sample provides the mirror image: Todoist's board is a **view/layout setting** ("Open Today, Upcoming, or any project, label, or filter → view icon → Board"); sections become columns; the layout is switchable per view and syncs as a display preference; TickTick's kanban is "tasks organized into columns based on your chosen grouping"; Asana's board is one of five project views. Center-of-gravity test adopted: if the board is one view over task records, it is task management; if position-as-state is the record, it is a Kanban Task Board.
3. **vs Project Management Application (§03.07, processed) — keep-both confirmed; the PM pass's seam adopted.** PM's L0: project as unit of record (bounded undertaking) + planned decomposition as plan of record + track-to-completion loop **at project scope** (progress rollup read and acted on by revising the plan). This pass's L0 keeps the **task** as the unit of record; containers organize tasks but carry no plan-of-record/progress-rollup machinery in the sample (Todoist projects have no percent-complete; To Do lists none). The PM pass's own removal test ("2 without 1 = task manager") is consistent: planned decomposition without the bounded-undertaking container is this Type. Asana illustrates the drift: with goals/portfolios/timeline machinery, the product's center of gravity is work management, not the task record.
4. **vs To-do List Application (§03.06 sibling, UNPROCESSED) — seam PROPOSED for that pass; joint review recommended.** The personal-organizer pass proposed "work/team subject with assignment/workflow vs personal-life subject"; this pass's evidence refines it — the subject axis is NOT the wall (Todoist and To Do both explicitly serve personal tasks; TickTick targets work *and* life). The defensible seam is **center of gravity in the management apparatus**: to-do = capture-and-remember posture (lists of checkable items; completion + reminder are the primary acts; organization thin), task management = managed-execution system (organizing structure + population views as the primary working material). Evidence that the boundary is a gradient, not a wall: Microsoft To Do (to-do pole) already carries assignment, importance/tags, My Day smart view; Todoist (task pole) self-labels a to-do list app. Both leaves kept; the to-do pass should treat this finding as counterparty context.
5. **vs Work Management Platform (§03.07 sibling, UNPROCESSED) — seam PROPOSED.** Work management (per the PPM pass's flag) centers a team's whole ongoing operational work (requests, processes, approvals) where projects are one container; task management centers discrete completable tasks for people. Asana documents the overlap zone (one product family marketing both). Removal test: remove forms/requests/approval/process machinery → task management remains.
6. **vs Calendar Application (§03.08, processed) — consistent with that pass.** Tasks carry completion state and no inherent clock anchor; events are clock-anchored occurrences. The integration is at the scheduled edge (drag task to calendar; calendar layout over dated tasks; TickTick/To Do/Todoist calendar views) — a view, not a merger.
7. **vs Workflow Management Platform (§10, processed) — confirmed from this side.** There, "tasks are the runtime surface of instances moving through a reusable multi-step definition — remove the definition/instance machinery and only a task list remains." The inverse holds here: no reusable process definition is present in any sampled product; each task stands alone.
8. **vs Household Chore Application (§29, processed) — confirmed.** That pass already held: chore apps' cadence-first chore record + fairness/rotation machinery are not covered by this Type; keep separate.
9. **vs Agile Project Management Application (§03.07, processed) — consistent.** Team-owned ordered backlog + cadence + flow metrics sit on top of work-item machinery; a task manager without backlog/cadence stays in type.
10. **vs Focus Timer / Life Planning / Meeting Action Item Management (§03.10/03.13/03.14, processed) — consistent with the focus-timer pass's embedding test** ("when the timer is one embedded capability of a task-centric product, the product belongs to the task-management Type" — TickTick's pomodoro/habits are the live example). Life planning adds the persistent goal layer above tasks; meeting action-item tools birth tasks from meeting context.

## Historical / Market-Sample Check

- **Paper era**: a planner/task-paper system (task entries with due dates and priority letters, project lists, contexts, a daily to-do page) satisfies all three L0 legs at analog level: task records (written entries), managed organization (projects/contexts/priorities), execution views (the daily page assembled from the population). No software capability required.
- **Early PIM/task-list software generation** (1990s–2000s task lists inside PIMs, Palm-class to-dos, Outlook Tasks): task record + due date/priority + list organization + today-style views satisfies the core with no cloud, boards, AI, or sharing. (Historical leg asserted structurally; no primary page fetched this pass for those products — kept at conceptual strength.)
- **Web-native generation** (Remember The Milk, fetched): capture with NL dates, reminders, shared lists, sync — same trunk grammar.
- **Modern generation** (Todoist/TickTick/Asana): adds layouts, filters, plans, AI — all excluded from the invariant.
- Verdict: the definition survives the historical check; it does not over-fit the current mobile-cloud pattern.

## Uncertainties

- Asana evidence is Tier 2 (product/features/FAQ pages): help-center article bodies were not reachable (JS shell, 1 attempt). Task-level mechanics (subtasks, My Tasks sectioning) asserted only at the level those pages state.
- Remember The Milk captured at homepage/root level only; help guide not fetched. Claims from RTM limited to its self-presentation (capture, reminders, sharing, sync).
- TickTick help-center article bodies not fetched (only the feature-guide taxonomy + features page); sub-task and group/sort mechanics asserted at taxonomy level.
- Founding dates/lineages of RTM (2005) and Todoist (2007) are common knowledge but were not stated on fetched pages (Todoist's "19 years" self-claim is fetched); no precise-dated historical claims appear in the final document.
- The to-do/task seam is a center-of-gravity judgment with real market blur; left to the to-do-list-application pass for joint review rather than resolved here.
- The exact borderline where "richer task attributes" become "issue-population management" (e.g., multiple custom statuses in a task tool) was not tested against a product that sits exactly on that line; recorded as a gradient.

## Final Synthesis

A Task Management Application is the personal/team application whose world is a **population of task records** — individually addressable, completable items of work — that the user **organizes into managed structures** (containers, sub-tasks, labels, priorities) and **works from execution views** (today/upcoming, calendar, board, filters) that the population's own attributes drive; completion is a first-class act that updates the population, and recurring/scheduled work re-materializes as the cycle advances. The record grammar is two-state (open→done) with derived urgency; richer multi-stage workflows, triage/backlog population management, board-as-record, project-level plan-of-record machinery, process definitions, and goal layers belong to neighboring Types. Around the core, mature products add dates/reminders/recurrence, sub-tasks, assignment on shared containers, comments/attachments, multiple layouts, filters, history/reporting, sync, quick capture, and templates; bundles and plan-gated suites (calendar/focus/habit; fields/dependencies/portfolios) are variant packaging, not identity. The market spans a personal-first pole, a bundled-productivity pole, a platform-native to-do pole, a veteran web pole, and a work-management pole — one grammar, different centers of gravity.
