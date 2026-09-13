# Research Notes — Time Blocking Application

Research date: 2026-09-09
Leaf: Time Blocking Application (DIRECTORY §03.14 Time & Focus)
Slug: time-blocking-application

## Research Goal

Understand what a Time Blocking Application actually is as an Application Type: what objects exist inside it, what the user does with them, how the planning work flows, and where the Type's real boundary sits against Calendar Application, Task Management Application, Focus Timer, Time Tracking / Productivity Activity Tracker, and scheduling Types. The directory places this leaf as a sibling of Time Tracking Application and Focus Timer; two prior passes left forward flags for it:

- productivity-activity-tracker (2026-09-08): "time-blocking-application (plan-future vs record-past; trackers touch planning only as furniture)".
- focus-timer (2026-09-07): "time blocking plans *future* intervals on a schedule; the focus timer runs the *current* interval. Natural pipeline: planned block → executed focus session."
- calendar-application (2026-09-06) recorded the opposite-side note: "Time blocking is a usage pattern of the calendar, not a separate Type here." This pass must discharge that flag from the time-blocking side.

## Initial Boundary

Working hypothesis before research:

1. Core use: planning future work into scheduled time ("time blocking" / "timeboxing") — the user allocates bounded spans of a day/week to specific work items.
2. Users: knowledge workers, founders, operators, students; increasingly teams (shared focus-time norms).
3. Nearest neighbors: Calendar Application (events on a time grid), Task Management Application (work items with dates), Focus Timer (running the current interval), Time Tracking (recording the past), Meeting/Appointment Scheduling (negotiating times with others), Personal Organizer / Life Planning (broader life layer).
4. Likely confusion: a calendar used to "block time" (usage pattern vs product center); a task manager with a calendar view; AI auto-schedulers that look like calendars.
5. Unknowns: is the time block definitional without task linkage? Is auto-scheduling definitional? Is the planning ritual definitional? Is external-calendar integration definitional? Where exactly is the calendar seam?

## Research Questions

1. What is the unit of record? (block? task? event? slot?)
2. How are blocks created — manual placement, auto-scheduling, or both? What is the direction of creation (work→time vs time→event)?
3. What happens to the plan as the day unfolds — completion, rescheduling, carry-over?
4. What role does the external calendar play — substrate, availability source, or optional?
5. What role do tasks/task managers play — native list, imported, optional?
6. What planning rituals do products institutionalize (daily planning, weekly review)?
7. What is common mature structure vs defining core vs variant vs vendor-specific?
8. Historical check: would paper-era time-block planning satisfy the same model?
9. Boundary: what distinguishes this Type from a calendar, a task manager, a focus timer, a tracker?
10. Does the team/organization pole (shared focus time, team analytics) stay inside the Type?

## Representative Products

Selected for market representativeness, documentation quality, distinct product philosophies, and distinct customer tiers:

| Product | Philosophy | Customer tier | Evidence base |
|---|---|---|---|
| Sunsama | planning-ritual-first: human deliberation, daily planning ceremony, workload limits | individual professionals + teams | Tier-1 help center (help.sunsama.com), 8 articles fetched |
| Motion | AI auto-scheduling-first: algorithm continuously builds and maintains the schedule; broader work platform around it | individual + teams | Tier-1 help center (usemotion.com/help, GitBook with .md endpoints), 4 pages fetched |
| Reclaim.ai | calendar add-on pole: AI scheduling written into the user's existing Google/Outlook calendar; habits/focus-time defense | free individual → business → enterprise | Tier-1 help center (help.reclaim.ai) + Tier-2 product pages |
| Morgen | calendar-client-first: full multi-calendar client (desktop heritage) with a planner/time-blocking layer | individual professionals + teams | Tier-2 official product pages (morgen.so); help center unreachable |
| Akiflow | inbox-first time blocking: capture tasks from everywhere, block them fast; rituals + stats | individual professionals (founders/operators) + teams | Tier-1 help center (product.akiflow.com/help), 2 pages fetched |

Deliberately not deep-researched (used only as boundary/variant anchors): Clockwise (team calendar optimization; exit signaled by Reclaim's official "Switching from Clockwise" collection), TickTick (task manager with calendar/time-blocking furniture — covered by the task-management pass), Structured/TimeBloc-class visual day planners (not fetched — uncertainty), Google/Outlook Calendar (calendar-as-capability pole — covered by the calendar-application pass).

## Sources

Tier 1 (official operational documentation):

- Sunsama User Manual — https://help.sunsama.com/ — fetched 2026-09-09:
  - Timeboxing: Concepts and Principles — /docs/usage-guides/timeboxing/timeboxing-concepts-and-principles
  - Daily Planning — /docs/usage-guides/daily-planning
  - Auto-scheduling — /docs/usage-guides/timeboxing/timeboxing-auto-scheduling
  - Auto-rescheduling — /docs/usage-guides/timeboxing/auto-rescheduling
  - Tasks vs Events: the basics — /docs/getting-started/basics/tasks-vs-events-basics
  - Task rollover: the basics — /docs/getting-started/basics/task-rollover-and-recurring-tasks-the-basics
- Motion Help (GitBook) — https://www.usemotion.com/help/ — fetched 2026-09-09:
  - Welcome/README — /help/readme.md
  - Auto-scheduling — /help/time-management/auto-scheduling.md
  - All Things Calendars — /help/time-management/all-things-calendars.md
  - Task — /help/project-management/task.md
- Reclaim.ai Help Center — https://help.reclaim.ai/ — fetched 2026-09-09:
  - Home (collection index)
  - Tasks collection — /en/collections/2476687-tasks
  - Key concepts in Reclaim Tasks — /en/articles/4303610-key-concepts-in-reclaim-tasks
- Akiflow Help Center — https://product.akiflow.com/help — fetched 2026-09-09:
  - Home (collection index)
  - Time Blocking collection — /help/collections/1069791-time-blocking
  - Time Blocking 101 — /help/articles/3677363-time-blocking-101

Tier 2 (official product pages):

- Reclaim.ai — https://reclaim.ai/ and https://reclaim.ai/features/tasks — fetched 2026-09-09
- Morgen — https://www.morgen.so/ , https://www.morgen.so/tasks-and-monotasking , https://www.morgen.so/ai-planner — fetched 2026-09-09

Source-access limitations:

- Morgen help center (help.morgen.so) transport error on fetch; abandoned after first failure per network rules. All Morgen observations are Tier-2 (official product pages incl. FAQ sections). No precise Morgen operational claims (numeric limits, exact behaviors) are canonized.
- Reclaim help-center article URLs under /hc/en-us 404; the Intercom help center at https://help.reclaim.ai/ works. One Tier-1 article fetched; the rest of the Reclaim picture is Tier-2.
- No pricing/plan-gating details were canonized from any vendor.

## Product Observations

### Sunsama (evidence layer A unless noted)

- Vendor's own definition of the practice: "Timeboxing (or 'timeblocking') is a way to turn your task list into a scheduled itinerary for the day by scheduling your tasks to your calendar." (Timeboxing: Concepts and Principles)
- Vocabulary: **Tasks** (items in daily task lists, created natively or imported from integrations), **Meetings** (calendar events, recommended to import as tasks), **Working sessions** ("Calendar events created when you timebox a task. They indicate your planned work periods."), **Planned time** (estimate; sets working-session duration), **Actual time** (timer or manual).
- Tasks vs events: "Tasks will not show up on your underlying Google/Outlook calendar unless you deliberately timebox them" — dragging a task onto the calendar is one timeboxing method. Only tasks in the task list count toward workload/time totals.
- Daily planning ritual (guided flow): reflect on yesterday → add tasks to your day (from integrations, backlog, weekly objectives, or new) → check predicted workload (sum of planned times vs configured workload threshold; timeline of estimated completion vs preferred shutdown time; defer to future day or move to backlog) → finalize your plan (order tasks; optionally timebox to calendar; set shutdown time) → share your plan (post to Slack/Teams). Ritual can be scheduled ("Rituals" setting prompts at a set time); evening mode plans tomorrow.
- Auto-scheduling: keyboard shortcut X / right-click "Add to calendar"; schedules config (default working hours + per-channel schedules); never overlaps calendar events; may split tasks across blocks (tasks >1h "readily split"; ≤1h only if necessary); overcommitted options: schedule anyway / schedule another day / defer; declined meetings and events marked free are ignored.
- Auto-rescheduling: triggers on task-task conflict (deconflict) and on early completion (truncate session, shift remaining tasks forward); only Sunsama-created working sessions are touched — "Regular calendar events (i.e. meetings) are never touched"; undo via Cmd+Z; both behaviors individually disableable.
- Task rollover: incomplete tasks automatically roll to the next day's list; auto-archive captures tasks that rolled over multiple consecutive days (threshold configurable); recurring-task rollover nuances.
- Other surfaces: Kanban board of tasks by day, Today view, Focus Mode, Focus Bar, Breaks, Backlog, Archive, Weekly Objectives (weekly planning + weekly review), Daily Highlights, planned-vs-actual times, menu bar app, command palette, email forwarding, MCP integration.
- Integrations: Jira, Asana, Trello, GitHub, Linear, Notion, Todoist, Microsoft To Do/Planner, Google Tasks, Apple Reminders, Gmail/Outlook, Slack, Teams, Zapier, Toggl.
- Team usage: shared channels/contexts, "Using Sunsama with Teammates" FAQ, plan sharing to Slack/Teams.

### Motion (evidence layer A)

- Positioning: "A platform to manage work, store knowledge, create projects, and coordinate human and AI tasks all in a single place… built around automatic scheduling. It continuously plans your day by deciding what you should work on and when, based on your tasks, deadlines, priorities, and available time. As your work changes, Motion adjusts your schedule in real time."
- Auto-scheduling: "Motion's way of turning your to-do list into a living schedule." Inputs: availability (scans calendar for open slots, respecting existing events), duration, deadlines (hard vs soft; hard deadlines scheduled outside normal hours if needed), priorities (ASAP state overrides everything), start dates, recurrence (recurring placed ahead to maintain cadence). "When your day shifts, Motion reshuffles automatically."
- Chunking: long tasks broken into smaller blocks (e.g., 2-hour task in 30-minute chunks; 10-hour task in 2-hour chunks) when chunk rules set; otherwise one full slot.
- Task definition (vendor's own test): tasks must be actionable + have duration + have deadline; "Can Motion move this around in my schedule? If it has to happen at one fixed time, it's an **event**. If it can be slotted flexibly, it's a **task**." Fixed-time items ("pick up kids at 3:15") are events, not tasks.
- Calendar model: external accounts (Google/Microsoft/iCloud) connected; layers = Accounts / My Calendars / Frequently Met With; calendars toggled into "My Calendars" affect availability (free/busy feeds auto-scheduling); main calendar is default save location; custom schedules (working hours, e.g., mornings deep work); Flexible Hours (one-day overrides: start later, stop early, block hours, block whole day → recalculation).
- Completion: green checkmark; completed-task visibility toggle in calendar view.
- Broader platform around the scheduler: workspaces, projects, docs, dashboards, AI Chat, AI Notetaker (meeting → action items → tasks), AI Agenda, booking links, email-to-task address.
- Creation paths (7 documented): +New, inside docs, inside projects, AI Chat, AI Agenda, email, AI Notetaker — "How a task is created does not change how it is scheduled."

### Reclaim.ai (evidence layer A for help article; A/B for product pages)

- Positioning: "#1 AI calendar for work. AI agents that schedule work, meetings, and life – automatically." Runs on the user's existing Google Calendar or Outlook Calendar ("AI superpowers for your existing calendar"; Google Workspace Marketplace add-on origin).
- Key concepts (Tier-1 article): "The calendar is the source of truth for *what actually happened* in order to determine *what work needs to be scheduled*." **Task** = the overall work item; **Task Event(s)** = the time block(s) on the calendar for doing it (one task → multiple task events, e.g., 6h task as 2h/1h/1.5h/1.5h events with min/max event sizes). "Reclaim assumes the work was done" when a task event's time passes; auto-reopen setting for unmarked tasks. Deleting a task event does not reduce the task's total duration — the time is rescheduled.
- Time defense: task events flip between **Free** (multiple scheduling options remain before due date) and **Busy** (no other options / would push past due date); events scheduled over a task event (e.g., accepted meeting) auto-reschedule it — unless locked.
- Feature set: AI Tasks ("Turn tasks from Jira, Asana, ClickUp, Todoist, and more into dedicated calendar time"; "breaking larger projects into manageable work sessions that adapt as schedules change"; auto-rescheduling for conflicts; deadline-aware planning; split into focused work sessions), AI Habits ("AI-powered recurring events that flex and find time"), AI Focus Time (weekly goal, auto-defend), AI Planner, AI Calendar Sync (defend events across multiple calendars), Scheduling Links, Smart Meetings, Buffer Time, Time Tracking, Workforce Analytics, AI Assistant (chat), Team OOO Calendar, AI Hours.
- Task filters: Open / Scheduled / Done scheduling / Marked done. "Up Next" for tasks. Manage tasks for others.
- Tiers: free Lite → Starter → Business → Enterprise; individuals → teams → enterprise deployments.
- Market signal: official "Switching from Clockwise" collection ("Clockwise is recommending Reclaim") — a team-calendar-optimization competitor exiting toward Reclaim's pole.

### Morgen (evidence layer A for product-page claims; no Tier-1)

- Positioning: "Daily plans designed by AI, perfected by you. A daily planner that prioritizes your most important to-dos, events, and projects in one app. Get AI-powered recommendations or plan manually." Platforms: Windows, Mac, Linux, web, mobile (desktop-first heritage; Swiss company).
- Calendar-first center: "All your calendars in one place" — Google, Outlook, Apple, Fastmail and more; Calendar Sets (view subsets via shortcuts); reminders; built-in scheduling links; team availability; calendar automations (calendar sync, travel time, buffer time).
- Time blocking: "Tasks that matter belong on your calendar… protect valuable focus time by scheduling tasks from Notion, ClickUp, Linear or Todoist in your calendar"; manual drag-and-drop time blocking ("assign specific time slots to important work"); completion synced back to the underlying task manager; subtasks; time estimates; duplicate time blocks for focused execution windows.
- AI Planner: generates daily plans from tasks + capacity + "how you work best"; **Frames** = templated blocks of time devoted to a task type (deep work, quick wins, personal, learning) with custom filters (tags, source, project) and recurring patterns; plans suggested with user approval ("Our suggested plans are only scheduled with your approval"); preview/adjust/confirm; plan 1–7 days at a time; conflict alerts with one-click reschedule; reminders of previously scheduled incomplete tasks; capacity evaluation flags tasks at risk of being late; "Realistic Time Blocking" options (pad estimates, split big tasks, plan breaks with intensity levels); Morgen Priority Factor (vendor term).
- FAQ positions the calendar as "the single source of truth"; manual scheduling remains fully available alongside AI.

### Akiflow (evidence layer A)

- Positioning: "Time-Blocking Digital Planner & Calendar… brings tasks, calendars, and AI into one time-blocking planner, helping busy professionals plan focused days and follow through." Built for "founders, operators, and obsessed doers"; Y Combinator-backed.
- Vendor's own definition: "Time blocking consists of blocking time for your tasks on your calendar to schedule exactly when you're going to work on them. If your day unravels through meetings and you need to focus on your tasks, this is the right time management technique for you."
- Planning: add date+time to tasks (natural language or shortcut P); "Daily Planning" session ("taking just 5 minutes to plan your day"); **Rituals** (named recurring planning moments); **Stats**.
- Locking: "Locking your tasks, Akiflow will schedule events on your Calendar, so your colleagues will know you're on focus time"; visibility options Public / Private / Busy; auto-lock setting; recurring tasks locked 15 instances ahead (vendor figure — L3).
- **Time Slots**: "dedicated containers within your calendar" — organize multiple tasks within specific periods; assign projects (slot takes project color); recurring slots; drag-and-drop adjust; pin slots to a separate column.
- Universal Inbox: capture tasks from many tools (10+ native integrations, thousands via Zapier/IFTTT); task manager with Someday/This month/This week organization; AI sidekick "Aki" (chat, voice, daily briefings); teams; focus time/goals/focus mode toolbox.

## Cross-product Comparison

| Dimension | Sunsama | Motion | Reclaim.ai | Morgen | Akiflow |
|---|---|---|---|---|---|
| Unit of record | Task + "working session" (timeboxed calendar event) | Task (auto-scheduled onto calendar as blocks) | Task + "Task Event(s)" (time blocks) | Task (scheduled onto calendar; "time blocked plan") | Task (+ Time Slot containers); locked tasks become calendar events |
| Block creation | Manual drag / auto-schedule (X) | Automatic by default; parameters guide | Automatic; calendar events can be moved | Manual drag-drop or AI Planner suggestion (approval-gated) | Manual (date/time, drag) + AI suggestions |
| Direction of creation | work → time (task list → calendar) | work → time (to-do list → living schedule) | work → time (tasks → calendar time) | work → time (tasks → calendar slots) | work → time (tasks → calendar blocks) |
| External calendar role | substrate: timebox writes real events; availability input | substrate + availability input (free/busy feeds scheduler) | substrate + "source of truth" | substrate (multi-calendar client) + availability | substrate (lock writes events) + availability |
| Task source | native list + 20+ integrations | native suite (projects/docs/AI) | native + 6+ PM integrations | native + Notion/Todoist/Linear/ClickUp/etc. | native + universal inbox from many tools |
| Planning ritual | guided daily planning + weekly planning/review (signature) | none required (continuous auto-scheduling) | AI Planner; habits carry routine | AI Planner + Frames as weekly template | Daily Planning session + Rituals (signature) |
| Reconciliation | auto-reschedule (deconflict + early completion), rollover, auto-archive | continuous reshuffle on any change | auto-reschedule on conflict; assumes-done; auto-reopen option | conflict alert + one-click replan; incomplete-task reminders | manual drag; rituals; stats |
| Completion semantics | mark done; planned vs actual time | checkmark; visibility toggle | mark done; "assumes the work was done" | checkmark + confetti; syncs back to source tool | complete tasks; stats |
| Workload/capacity | predicted workload vs threshold (signature) | balances against availability + deadlines | deadline-aware risk (Free/Busy defense) | capacity evaluation; at-risk flags | — (not observed on fetched pages) |
| Recurring/routines | recurring tasks; "at roughly" times | recurring tasks (placed ahead) | Habits (flexible recurring) | Frames (recurring templates) | recurring tasks; recurring Time Slots |
| Focus/timer | Focus Mode, Focus Bar, Breaks | — (not observed on fetched pages) | Focus Time (defended blocks) | deep-work timer (free tool); breaks in planner | Focus Mode, Focus Time |
| Team layer | shared channels, plan sharing to Slack/Teams | workspaces, team scheduling | business/enterprise, workforce analytics | team availability, team scheduling | Akiflow for Teams |
| AI layer | Sunny assistant | AI Chat/Agenda/Notetaker | AI agents + Assistant chat | AI Planner + Kai (separate product) | Aki |
| Scheduling links | — (not observed) | Booking Links | Scheduling Links | built-in scheduling links | — (not observed) |
| Platform shape | web app + menu bar | web + desktop | calendar add-on + web app | desktop (Win/Mac/Linux) + web + mobile | web + desktop + mobile |

Reading of the comparison:

- All five products share: work items carried into bounded scheduled spans on a time grid; creation flowing from work to time (manually, automatically, or hybrid); a maintenance loop (completion, rescheduling, carry-over); external-calendar integration as the substrate/availability layer; duration estimates; recurring routines; and a personal-productivity audience with an optional team layer.
- The products differ on philosophy (ritual vs algorithm vs calendar-client vs inbox), on how much of a task manager they bundle, and on how much team/analytics/AI machinery they attach. These differences are variant axes, not Type boundaries.

## Canonical Model

### L0 — Defining Invariant (deliberately small)

The Time Blocking Application is defined by two jointly-held structures:

1. **The time block as the unit of record.** A persistent, individually addressable bounded span on a schedule (a navigable day/week time grid), assigned to a specific piece of work or purpose — what the user intends to do in that span. The block is visually distinct on the grid and carries the work's identity (name, source, category). Remove it → a calendar of coordination events, or a task list with no time allocation; the Type collapses.

2. **The work-to-time planning loop.** Blocks are created by assigning work to time — manually placing work items on the grid, or automatic scheduling that computes placements from a work list against calendar availability — and the plan is then maintained against the unfolding day: blocks are completed, rescheduled (drag or automatic), or carried over when unfinished. The direction of creation is work→time, and the plan stays a living, managed object rather than a one-shot document. Remove the creation direction → a calendar (events created as schedule-of-record entries) or a task manager (work with dates, no time allocation); remove the maintenance → a static plan template, and the "management" is gone.

Jointly-held load-bearing analysis:

- 1 alone = a calendar with colored entries (or a Gantt-style chart) — not time blocking.
- 2 without 1 = a task manager that reschedules due dates — no time-grid allocation.
- 1+2 without the loop's maintenance half = a one-shot plan document.
- The two legs are inseparable in every sampled product: the block exists because work was assigned to it; the loop exists because blocks must track reality.

### L1 — Common Mature Structure (very common, not definitional)

- External calendar integration: read events to compute availability; write blocks back as real calendar events (all 5 sampled; but the paper lineage and a self-contained grid satisfy L0 without it).
- A work-list layer: native task list and/or imported tasks from task/PM tools (Jira, Asana, Linear, Todoist, Notion, ClickUp, Slack, email…).
- Duration estimates on work (planned time) and commonly planned-vs-actual comparison.
- Drag-and-drop placement and rescheduling on the grid.
- Completion marking with carry-over/rollover of unfinished work (Sunsama rollover + archive; Reclaim assumes-done/auto-reopen; Morgen reminders of incomplete scheduled tasks).
- Working-hours / availability configuration that constrains where blocks may land.
- Recurring blocks / routines (recurring tasks, habits, recurring slots, Frames).
- Workload/capacity visualization (Sunsama predicted workload vs threshold; Morgen capacity evaluation; Motion availability balancing).
- Focus support inside a block (Focus Mode/Focus Bar, breaks, deep-work timer).
- Weekly planning/review surfaces.
- Multi-surface clients (web/desktop/mobile/menu bar) with sync.
- Plan sharing (post plan to Slack/Teams; share with teammates).

### L2 — Variant / Optional Structure

- Scheduling philosophy: ritual-first (Sunsama, Akiflow) vs auto-scheduling-first (Motion, Reclaim) vs calendar-client-first (Morgen) vs hybrid AI-with-approval (Morgen AI Planner).
- Auto-scheduling depth: priority hierarchies, hard/soft deadlines, chunking/splitting rules, flexible hours, "at roughly" times, one-click replan.
- Block defense posture: Free/Busy flipping (Reclaim), lock with visibility levels (Akiflow), meetings-never-touched rule (Sunsama).
- Team/organization layer: shared plans, team availability, workforce analytics, org initiatives (Reclaim enterprise; Motion workspaces; Sunsama teams).
- Scheduling links / booking (Reclaim, Morgen, Motion) — neighboring-Type capability bundled.
- Time tracking / stats (Sunsama actual time, Reclaim Time Tracking, Akiflow Stats) — neighboring-Type capability bundled.
- AI assistants (Sunny, Aki, Motion AI Chat, Reclaim Assistant, Morgen Kai) — era machinery, not definitional.
- Goals/objectives layers (Sunsama Weekly Objectives, Akiflow Goals).
- Breaks/buffer/travel-time automation (Sunsama Breaks, Reclaim Buffer Time, Morgen travel/buffer).
- Platform shape: standalone app vs calendar add-on vs full calendar client.

### L3 — Vendor-specific (research notes only)

- Sunsama: "working session" terminology; workload threshold + shutdown-time timeline; playlist method (alternative to timeboxing for meeting-light days); channels/contexts; Daily Shutdown; auto-archive threshold; per-channel schedules; Sunny AI; MCP integration; pricing manifesto.
- Motion: ASAP task state; scheduling hierarchy (ASAP > hard deadline > soft deadline > priority > duration > start date > recurrence); Flexible Hours mechanics; Frequently Met With layer; docs/dashboards/notetaker platform; task@usemotion.com email-to-task; 7 documented creation paths.
- Reclaim: Task vs Task Event min/max event sizes; Free/Busy time-defense rules; locks; "assumes the work was done" semantics; auto-reopen setting; Reclaim 1.0 vs 2.0 doc split; Clockwise switching program; specific marketing metrics (7.6h focus/week etc. — marketing, not canonized).
- Morgen: Frames; Morgen Priority Factor; 20% estimate padding (vendor figure); intensity levels for breaks; Calendar Sets; Kai (separate product); plan 1–7 days at a time.
- Akiflow: Time Slots as containers; lock visibility levels (Public/Private/Busy); 15-instance recurring lock (vendor figure); Rituals; Aki (voice/phone-call roadmap); universal inbox; "Designed in Italy" positioning.

## Vendor-specific Findings

All L3 items above. None promoted into the final document except as unbranded variant examples (e.g., "some products defend blocks by flipping them between free and busy on the underlying calendar" without vendor names). No numeric vendor figures (20% padding, 15 instances, workload thresholds) are canonized.

## Boundary Findings

1. **vs Calendar Application** (§03.08; the calendar pass recorded "time blocking is a usage pattern of the calendar, not a separate Type here" — DISCHARGED from this side, keep-both ratified). Both Types hold bounded spans on a time grid. The seam is the direction of creation and the object's semantics:
   - Calendar: the event is the schedule-of-record object; creation is time→event ("something happens at 3pm"); the mature core carries coordination machinery (invitations, RSVP, sharing, free/busy publishing). Time blocking appears there only as a usage pattern (a user writing "focus time" events).
   - Time blocking: the block is a work-allocation object; creation is work→time (a task/habit/purpose is given time); the mature core carries planning machinery (work list, planning ritual, reconciliation). The calendar becomes substrate and availability input.
   - Direct evidence of the reversal: Sunsama — "Tasks will not show up on your underlying Google/Outlook calendar unless you deliberately timebox them"; Reclaim — "The calendar is the source of truth for what actually happened in order to determine what work needs to be scheduled"; Motion — calendars are connected so the scheduler can "scan your calendar for open slots."
   - Test: remove the work-planning loop (work list, reconciliation) → Calendar Application. Remove coordination-as-center (invitations/RSVP/sharing as the point) → Time Blocking. A calendar product with a "focus time" button stays a calendar; a product whose center is the work-to-time loop is this Type even if it renders on a calendar.
2. **vs Task Management Application** (§03.06; that pass held "bundled periphery (calendar/focus/habit/matrix) variant-NOT-definitional"). The task is a completable unit organized in containers/views; the block is a time allocation. Time blocking products import tasks and complete them, but their center is the schedule; task managers' center is the task population. Motion bundles a full task suite around its scheduler (straddling pole — bundling, not identity). Test: remove the time-grid allocation → task manager; remove the task population (paper planner) → still time blocking.
3. **vs Focus Timer** (§03.14 sibling; forward flag DISCHARGED, ratified). The time block plans a future interval; the focus session runs the current interval. Pipeline relationship: planned block → executed session. Sunsama's Focus Mode/Focus Bar (timer inside a block) and Akiflow's Focus Mode are support capabilities inside this Type. Test: remove "plan ahead" → Focus Timer; remove "run now" → Time Blocking.
4. **vs Time Tracking Application / Productivity Activity Tracker** (§03.14 siblings; forward flag DISCHARGED, ratified). Plan-future vs record-past. Planned-vs-actual time (Sunsama), Time Tracking stats (Reclaim), Stats (Akiflow) are furniture on the plan, not the center. Test: remove the forward plan → tracker.
5. **vs Meeting Scheduling / Appointment Scheduling / Group Availability** (§03.09). Negotiating times with others vs allocating one's own work. Scheduling links (Reclaim, Morgen, Motion) are bundled neighboring-Type capabilities. Test: remove own-work allocation → scheduling Type.
6. **vs Personal Organizer / Life Planning** (§03.13). Life planning's center is goals/roles/review across life domains; time blocking appears there as furniture (life-planning pass: "weekly planning view… time blocking… calendar sync" as common optional). Test: remove the goal/role layer → time blocking; remove the time-allocation loop → life planning.
7. **vs team calendar optimization (Clockwise pole)**. Same substrate (the calendar), different center: optimizing meeting load and focus-time norms across a team vs allocating an individual's (or team's) work into time. Reclaim's official "Switching from Clockwise" collection documents that market's consolidation toward the work-allocation pole; team time blocking (shared focus-time policies, team analytics) is a variant of this Type when work-to-time allocation remains the center.
8. **Lexical warning — "blocking"**: in this Type, "blocking" always means calendar time blocking (reserving time). App/site blocking (distraction blocking) belongs to screen-time/digital-wellbeing territory (focus-timer pass boundary), not here. No sampled product's core includes app blocking.
9. **Historical / market-sample check (§24)**: paper-era time-block planning satisfies both L0 legs with no software: a daily plan written in a paper planner assigns named work to hour spans (blocks), the morning planning act creates them, and the day's reality is reconciled by crossing off, rescheduling, and carrying unfinished work to tomorrow; weekly spreads do the same at week grain. The practice's modern paper embodiments (time-block planner products) and the pre-software management-book tradition fit. Early digital realizations were users manually blocking work time inside Outlook/Google Calendar (calendar-as-capability pole — usage pattern, not this Type). The dedicated Type emerged when the work-list→time-allocation loop became the product's center. No era, region, platform, or AI pattern is baked into L0. Pass.

## Uncertainties

- The visual "day planner" pole (Structured/TimeBloc class: timeline-first day planners with light task features) was not fetched this pass. Structurally they appear to satisfy L0 (blocks + planning + reconciliation), but no direct evidence was collected; they are treated as probable variants, not asserted.
- Whether any in-type product lacks external-calendar integration entirely (self-contained grid only) was not directly observed; all 5 sampled products integrate external calendars. L0 therefore does not require calendar integration, but the sampled market universally has it (recorded as common-mature, not definitional).
- Akiflow's workload/capacity machinery and Motion's focus/timer support were not observed on fetched pages; absence claims are scoped to "not observed on fetched pages," not "does not exist."
- Morgen's operational behaviors (exact conflict handling, rollover semantics) come from product-page FAQ copy, not help-center articles; kept at moderate assertion strength.
- Clockwise's current product state is known only through Reclaim's switching-collection framing; no independent Clockwise claims made.
- The boundary against "day planner" vs "time blocking" may deserve a taxonomy note if a future pass finds day planners lacking the work-list loop entirely.

## Final Synthesis

The Time Blocking Application is the planning-side member of the §03.14 family: its defining core is the work-to-time allocation loop. The unit of record is the time block — a bounded span on a schedule assigned to a specific piece of work or purpose — and the loop creates blocks from work (manual placement or automatic scheduling against calendar availability) and maintains the plan against the unfolding day (completion, rescheduling, carry-over). Everything else is layered maturity: external-calendar integration as substrate and availability source, task-list/import machinery, duration estimates and planned-vs-actual, working-hours constraints, recurring routines, workload visualization, focus support, weekly rituals, team layers, AI assistants, scheduling links, and time-tracking stats. The market realizes one Type in several product shapes — ritual-first planners, auto-scheduling engines, calendar add-ons, and calendar clients with planner layers — differing on who (or what) does the placing and how much task machinery is bundled, not on what the product fundamentally is. The Type's seams are held against the calendar (schedule-of-record vs work-allocation), the task manager (population vs allocation), the focus timer (planned vs running), and the trackers (plan vs record); the calendar pass's "usage pattern" note is discharged with a keep-both ratification: inside calendar products, blocking is a usage pattern; where the work-to-time loop is the center, it is this Type.
