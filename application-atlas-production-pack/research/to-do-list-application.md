# Research Notes — To-do List Application

## Research Goal

Understand the directory leaf **To-do List Application** (§03.06 Tasks, first of three siblings) as an Application Type from real products: what the unit of record is, what role the list plays, what the working loop looks like, which capabilities are common vs defining, and — the pass's central obligation — where the boundary runs against the sibling **Task Management Application**, whose pass (processed 2026-09-09) proposed a center-of-gravity seam and recommended joint review at this pass.

## Initial Boundary

Provisional understanding before research:

- Core use: keeping lists of things to do so they are not forgotten, then checking them off.
- Users: individuals managing everyday personal work and life (household, study, shopping, small shared lists with family/friends/colleagues).
- Nearest neighbors (all flagged by prior passes):
  - **Task Management Application** (§03.06 sibling, processed 2026-09-09) — its proposed seam: "to-do = capture-and-remember list posture (lists of checkable items; completion + reminder are the primary acts; organization thin), task management = managed-execution system (organizing structure + population views as the primary working material)"; joint review recommended at this pass. Its load-bearing note: "1+3 without 2 = undifferentiated lists (to-do pole)".
  - **Personal Organizer** (§03.13, processed 2026-09-08) — its proposed seam: "to-do-list-application — one record type with derived views (a due-date calendar of its own tasks) vs multiple co-equal record types of record in one integrated application".
  - **Kanban Task Board** (§03.06 sibling, processed) — board-as-record vs list-as-surface.
  - **Project Management Application** (§03.07, processed) — task unit + containers without plan-of-record/progress rollup.
  - **Note-taking Application** (§03.02, processed) — its seam: "notes = information to remember; tasks = actions with state to complete; remove the action/state machinery → checklist inside a note (common), not a task app".
  - **Calendar Application** (§03.08, processed) — completion state vs clock anchor.
  - **Household Chore Application** (§29, processed) — cadence-first chore record + fairness/rotation machinery, explicitly not an audience variant of the task side.
  - **Work Management Platform** (§03.07, unprocessed) — carried flag from PPM/PM passes.
  - **Time-blocking / Focus Timer / Life Planning / Meeting Action-item Management** (§03.10/03.13/03.14, processed) — embedding tests recorded in those passes.
- Unknowns: whether the to-do pole has a defensible L0 distinct from the task pole; whether "organization thin" (the task pass's characterization) survives contact with the modern platform-native to-do products; whether the daily-focus ritual is structural or incidental.

## Research Questions

1. What is the unit of record, and what is its defining act?
2. What is the role of the list — container only, or the primary working surface?
3. How do derived views (daily-focus lists, smart lists) relate to the lists — do items live in the views or in the lists?
4. What attributes do items carry (dates, reminders, priority, tags, notes, subtasks) and which are common vs defining?
5. How does the daily-planning ritual work (My Day-class surfaces), and what happens to uncompleted items?
6. How do sharing and assignment work, and is the shared layer a separate object class anywhere?
7. Where does the boundary sit vs Task Management (the joint-review obligation), Personal Organizer, Note-taking, Calendar, Kanban Task Board, Project Management, Household Chore, Work Management?

## Representative Products

| Product | Pole | Why sampled |
|---|---|---|
| **Microsoft To Do** | platform-native personal to-do (Exchange/Outlook substrate) | the task pass's to-do-pole counterparty; deepest platform integration; Tier-1 docs reachable |
| **Apple Reminders** | platform-native personal to-do (iCloud substrate) | the other dominant platform-native pole; full user guide reachable |
| **Any.do** | consumer cross-platform to-do with daily-planning ritual + family/workspace layer | different product philosophy (ritual + bundled calendar/focus); family/workspace Boards test the shared-layer seam |
| **Remember The Milk** | veteran web-native to-do | two-decade web pole; names the paper lineage itself; richest reminder-channel spread |
| **Todoist** (counterparty only) | task-pole product that self-labels a to-do list app | vocabulary-straddle evidence for the joint review; deeply sampled by the task pass |

Google Tasks was attempted as the minimal platform pole and **abandoned** (support.google.com timed out twice on 2026-09-09) — recorded under Uncertainties; no claims rest on it.

Evidence layers: **A** = directly observed on official pages of that product; **B** = cross-product commonality across the sample; **C** = canonical inference from comparison + boundary reasoning.

## Sources

Microsoft To Do (all fetched 2026-09-09, Tier 1):
- Help hub: https://support.microsoft.com/en-us/todo (nav taxonomy: Get started / Lists / Tasks / Productivity / To Do in other apps / Quick Start / Troubleshooting)
- "Organize your lists": https://support.microsoft.com/en-us/ToDo/organize-your-lists
- "My Day and suggestions": https://support.microsoft.com/en-us/ToDo/my-day-and-suggestions
- (CRUD article previously fetched at Tier 1 by the task-management pass, 2026-09-09: create/edit/delete/restore; Exchange Online storage; Outlook Tasks visibility)

Apple Reminders (all fetched 2026-09-09, Tier 1):
- User Guide (macOS): https://support.apple.com/guide/reminders/welcome/mac (full TOC)
- "Get started with Reminders on Mac": https://support.apple.com/guide/reminders/get-started-remne4b02adc/mac
- "Create custom Smart Lists": https://support.apple.com/guide/reminders/create-custom-smart-lists-remnfec66479/mac

Any.do (fetched 2026-09-09, Tier 1 at help-center collection level):
- Help Center root: https://support.any.do/ (collection taxonomy)
- "Tasks & Lists" collection: https://support.any.do/en/collections/7048507-tasks-lists (8 article titles)

Remember The Milk (fetched 2026-09-09, Tier 1):
- Help Center root: https://www.rememberthemilk.com/help/ (full per-app taxonomy)
- "What is Remember The Milk?": https://www.rememberthemilk.com/help/answer/about-whatrtm

Todoist (counterparty; fetched 2026-09-09, Tier 1):
- Home: https://www.todoist.com/ ("A To-Do List to Organize Your Work & Life"; "the world's #1 to-do list app"; nav "Made For: Task Management / Project Management / Time Management / Habit Forming / Teamwork"; capture/organize/plan/teamwork pillars)

## Product A — Microsoft To Do (evidence layer A)

- **Help-hub taxonomy**: top sections are **Lists** (Organize your lists, Assign shared tasks, Sort and search, Customize lists, Delete and restore lists, Get notifications for shared lists, Report abusive content in shared lists) and **Tasks** (Create/edit/delete/restore, Due dates & reminders, Smart due date recognition, Importance/tags & categories, Add files, Move tasks between or within lists), plus Productivity (Prioritizing yourself, Creating daily habits) and Using To Do in other apps (Outlook, Outlook.com, flagged email, Launcher).
- **Lists are the containers; groups organize lists** ("Organize your lists"): create list groups, drag lists into groups, rename/ungroup — one grouping layer above lists; lists remain the unit of organization.
- **My Day** ("My Day and suggestions"): "Use My Day to help focus on daily tasks. You can add new tasks directly to My Day, or add tasks from other lists, by selecting a task to view its details and then selecting **Add to My Day**"; suggestions (light-bulb) propose tasks to add. **"The My Day smart list resets every night, so you have a blank slate to add the tasks you want to accomplish each day. Any tasks in My Day that aren't completed before the list resets will be saved to your Tasks list and included in your suggestions the following day."** — the daily-focus surface is a ritual lens; uncompleted work returns to the default Tasks list (the home of record).
- From the task pass's Tier-1 fetch (2026-09-09): tasks stored on Exchange Online and visible in Outlook Tasks; restore via Outlook's Deleted Items; smart due-date recognition; importance/tags/categories; steps; sharing with assignment.

## Product B — Apple Reminders (evidence layer A)

- **Self-description**: "Quickly get started using Reminders to **track and organize your to-dos**."
- **Guide structure** is organized around lists: Create reminders (add/change, subtasks, create in Calendar, add from another app, list templates) → Manage reminders (mark complete/incomplete, move, delete, tag, dates or locations, assign shared reminders) → View reminders (lists or columns, view reminder lists, sort, print, widgets) → **Manage reminder lists** (create/change/delete, custom Smart Lists, organize lists, sections in lists, share a list, default list) → Grocery lists.
- **Smart Lists are lenses, not homes** ("Create custom Smart Lists"): "Smart Lists gather reminders from all your lists based on criteria you choose—such as tags, date, time, priority, flag, or location… **The reminders themselves remain in their original lists.**" Criteria combine with all/any matching (tags, date, time, priority, flag, location, lists; relative ranges supported). Conversion semantics confirm the list-as-home model: converting a regular list to a Smart List tags the existing reminders and **moves them to the default reminder list**; subtasks are flattened to top level; shared lists and the default list cannot be converted.
- **Daily/scheduled views**: "You can see all your scheduled reminders sorted by date and time in the **Today or Scheduled lists** in the sidebar."
- **Sharing**: invite to collaborate on a list via Messages/Mail/link; "track activity, manage collaboration, and even **assign shared reminders**."
- **Grocery lists**: a list type that "automatically sorts the items you add into different sections, like Meat, Produce, and Snacks & Candy."
- **Calendar integration**: "Create, manage, and complete your scheduled reminders right in the Calendar app on Mac" ("Your to-dos and schedule—all in one place").

## Product C — Any.do (evidence layer A at collection level)

- **Help-center collections**: **Tasks & Lists** — "Manage your **personal to-do lists and tasks** using tags, reminders, notes, and subtasks" (Managing Personal Lists; Smart Grocery Lists; Converting Personal Lists & Tasks to Family/Workspace Boards; Managing Personal Tasks and Subtasks; Color Tags; Notes & Files; Managing Overdue Personal Tasks; Completing & Archiving Personal Tasks); **Calendar & Planning** — "Use Any.do's calendar, **My Day**, and **Focus Mode** tools to plan and prioritize your time effectively"; **Boards (Family & Workspace)** — "Create and manage shared boards for family/team projects"; Collaboration & Roles; Notifications & Reminders; Integrations (WhatsApp, Gmail, ChatGPT, Slack, Zapier); Navigation & Input Tools (voice, views, shortcuts, smart input, search).
- **Reading**: the personal side is lists + tasks (tags/reminders/notes/subtasks; overdue management; completing & archiving); the daily ritual (My Day) and focus tools sit beside a calendar; the shared layer is a **separate object class** — family/workspace **Boards** — with a documented conversion path from personal lists/tasks to boards. The personal to-do core and the shared-board layer are distinct worlds in one product.

## Product D — Remember The Milk (evidence layer A)

- **Self-description** ("What is Remember The Milk?"): "Remember The Milk is the best way to manage your tasks… We created Remember The Milk so that you no longer have to write your **to-do lists on sticky notes, whiteboards, random scraps of paper, or the back of your hand**." — the product itself names the paper to-do list as its lineage.
- **Help taxonomy** (per app): **Tasks** (add, rename, edit properties, delete, **complete**, **postpone**, multi-edit, sort, drag-and-drop, default due date, view completed); **Subtasks**; **Notes**; **Attachments**; **Reminders** (email, SMS, desktop, push; overdue-task reminders; per-task reminders); **Lists** (add, rename, favorite, delete, sort order, default list, **Inbox list**, **'Given to others' list** / **Sent list**, shared lists); **Smart Lists** (criteria-based; "What happens when I add a task to a Smart List?"; change criteria); **Contacts**; **Tags**; **Locations** (location alerts, nearby distance); **Search** (advanced operators); **Sharing & Giving** (share a list, **give a task to a contact**, ungive, unshare); calendar integration ("Can I view my tasks in Apple/Google Calendar?"); MilkSync for Outlook; widgets.
- **Reading**: the full to-do grammar at web-era maturity — lists with an Inbox as default landing, smart lists as saved criteria, giving/sharing as the collaboration layer, reminders as the signature capability, postpone as a first-class act.

## Product E — Todoist (counterparty; evidence layer A, home page only)

- Self-labels "**A To-Do List to Organize Your Work & Life**" and "the world's #1 to-do list app", while its own navigation is "Made For: **Task Management**, **Project Management**, Time Management, Habit Forming, Teamwork" and its pillars are capture ("at the speed of thought"), organize ("sorting tasks into **Today, Upcoming, or using custom filters**"), plan ("due dates, calendar view, recurring tasks"), teamwork ("a shared space… alongside but separate from your personal tasks and projects"). Templates include Grocery List, Issue Tracking, Hiring Pipeline (board), Content Calendar.
- **Reading**: the market's canonical task manager claims the to-do vocabulary — direct Tier-1 evidence that to-do and task management form one vocabulary continuum (the straddle the task pass recorded from its side).

## Cross-product Comparison

| Dimension | Microsoft To Do | Apple Reminders | Any.do | Remember The Milk | Layer |
|---|---|---|---|---|---|
| Item = unit of record, open→done | yes (Tasks section; restore) | yes ("mark reminders complete or incomplete") | yes ("Completing & Archiving Personal Tasks") | yes (complete; view completed) | B |
| List as the container of record | yes (Lists section; list groups above) | yes ("reminders… remain in their original lists") | yes ("personal to-do lists") | yes (Lists section; Inbox default) | B |
| Derived views are lenses over lists | yes (My Day = smart list; uncompleted return to Tasks list) | yes (Smart Lists; "remain in their original lists") | yes (My Day over tasks) | yes (Smart Lists = saved criteria) | B |
| Daily-focus ritual | My Day + suggestions, nightly reset | Today/Scheduled smart lists | My Day + Focus Mode | (daily-summary reminders claimed historically; not on fetched pages) | B (D: weak) |
| Due dates + reminders | yes (smart due-date recognition) | yes (dates, locations) | yes (reminders) | yes (email/SMS/desktop/push; overdue) | B |
| Recurrence | yes (per task pass fetch) | yes (guide: dates; repeat in settings) | yes (reminders) | yes (repeat formats; NL entry) | B |
| Subtasks | yes (steps) | yes | yes | yes | B |
| Priority/importance/flag | yes (importance) | yes (priority, flag) | color tags | tags (priority not on fetched pages) | B |
| Tags/notes/files on items | yes (importance, tags & categories; files) | yes (tags, notes) | yes (color tags, notes & files) | yes (tags, notes, attachments) | B |
| Shared lists + assignment | yes (assign shared tasks; shared-list notifications) | yes (share list; assign shared reminders) | via family/workspace Boards + roles | yes (share lists; give tasks; Given-to-others/Sent lists) | B |
| Smart/saved views with criteria | My Day/Planned/Flagged/Assigned (per task pass) | custom Smart Lists (all/any filters) | (filters claimed; not on fetched pages) | Smart Lists (criteria; advanced search) | B |
| Grocery/shopping specialization | — (not on fetched pages) | grocery lists with auto-categorization | Smart Grocery Lists | — | B (2/4) |
| Calendar integration | To Do in Outlook; drag task to calendar | create/manage/complete reminders in Calendar | calendar + My Day + Focus Mode | view tasks in Apple/Google Calendar | B |
| Email→task bridge | flagged email → To Do | add a reminder from another app | Gmail integration | Gmail add-on; MilkSync for Outlook | B |
| Shared layer as separate object class | no (shared lists) | no (shared lists) | **yes** (family/workspace Boards, conversion path) | no (shared lists) | A (C only) |
| Platform substrate | Exchange Online + Outlook | iCloud | cloud account | cloud account | vendor-specific |
| Bundled periphery | daily habits, Outlook suite | Calendar app, widgets | calendar, Focus Mode, WhatsApp/ChatGPT | SMS/email/desktop reminders, MilkSync | vendor-specific |

## Canonical Model

### L0 — Defining Invariant (jointly held; remove any one and the Type is unrecognizable)

1. **The to-do item as the unit of record.** A persistent, individually addressable record of one thing the person intends to do — lightweight by design (a short title, optional notes, date, reminder) — whose defining act is **completion**: checking it off, open → done. (Remove → a text list or note; nothing to complete.)
2. **The list as the primary container and working surface.** Items are held on named lists; the list is the surface the user opens, reviews, and works from — capture, review, and completion happen on the list. Derived views (daily-focus lists, smart lists) are lenses over the lists; the items' home remains the list. (Remove the list-centrality → a managed population worked through organizing structure + population views = task-management territory; remove containers entirely → a checkable stream.)

Load-bearing jointly: 1 alone = a checkable-note store (the note pole); 2 without 1 = plain text lists; 1+2 = the to-do list. The record grammar is two-state (open→done) — the **same grammar as task management**; the two Types are separated by the management apparatus and the working material, not by the record (see Boundary Findings #1). The posture the structure realizes is **capture-and-remember**: the app's promise is that what you intend to do is held, reminded, and checked off — not that a population of work is organized and worked.

### L1 — Common Mature Structure (market-expected, not defining)

- due dates with reminders (time-based; location-based in several products)
- recurrence/repeat rules (the item re-materializes after completion)
- subtasks/steps
- priority/importance/flag
- tags/categories, notes, file attachments on items
- smart lists / saved views with criteria (Today, Scheduled, custom) — lens semantics
- a daily-focus surface (My Day-class: pick today's items, often with suggestions; some reset nightly)
- shared lists with assignment (collaborator-level, not org-chart)
- search/sort; postpone; completed-item history
- cross-device sync; quick capture; widgets
- calendar integration (view tasks in a calendar; create items from the calendar; drag to calendar)
- email→task bridges (flagged email, Gmail add-ons)
- grocery/shopping-list specialization, sometimes with automatic categorization
- list templates

### L2 — Variant / Optional Structure

- platform-native substrate and suite integration (iCloud; Exchange/Outlook; platform account) — the item store may live inside a wider personal-data suite
- family/workspace shared layer as a **separate object class** beside personal lists (boards with roles and a conversion path from personal lists)
- bundled periphery: calendar, focus sessions, habit patterns built on recurring items
- AI assistance (suggested tasks, smart input, assistant integrations)
- reminder-channel breadth (email/SMS/desktop/push)
- gamification/motivation layers — **not observed in this sample**; unverified

### L3 — Vendor-specific (kept out of the final document)

- Microsoft To Do: My Day nightly-reset semantics; Exchange Online storage + Outlook Tasks visibility + restore via Outlook Deleted Items; flagged-email bridge; list groups; Copilot-assisted help.
- Apple Reminders: grocery auto-categorization; smart-list conversion semantics (existing reminders tagged + moved to the default list; subtasks flattened; shared/default lists not convertible); creating/managing reminders inside the Calendar app; list templates; printing lists.
- Any.do: personal lists vs family/workspace Boards as separate object classes with a documented conversion path; WhatsApp reminders; Focus Mode; Smart Grocery Lists.
- Remember The Milk: Inbox/Sent/'Given to others' lists; SMS/email/desktop reminder channels; MilkSync for Outlook; advanced search operators; postpone as a named act; smart-list 'smart' count display; "over four million" users claim.
- Todoist (counterparty): "world's #1 to-do list app" self-label; "19 years and 223 days"; "2+ billion tasks completed"; template gallery incl. Issue Tracking and Hiring Pipeline boards.

## Vendor-specific Findings

See L3. Additional: the vocabulary straddle is itself a finding — Todoist (task pole) self-labels a to-do list app, while Microsoft To Do's own help center carries a "Tasks" section; the market uses "to-do list" and "task management" as one continuum of labels (both poles' primary sources confirm).

## Boundary Findings

1. **vs Task Management Application (§03.06 sibling, processed 2026-09-09) — JOINT REVIEW DISCHARGED from this side; keep-both RATIFIED, seam REFINED.** The task pass proposed a center-of-gravity seam (capture-and-remember list posture vs managed-execution system) and characterized the to-do pole as "organization thin". This pass's evidence **confirms the seam and refines the characterization**: the record grammar (item, open→done) is shared, and the modern platform-native to-do pole is **not** feature-thin — Apple Reminders carries sections in lists, tags, priority/flag, and custom Smart Lists with all/any filter criteria; Microsoft To Do carries list groups, importance/tags, files, and assignment on shared lists. What actually distinguishes the poles: (a) **the list is the home of record** — "The reminders themselves remain in their original lists" (Apple, direct Tier-1); My Day's uncompleted items "will be saved to your Tasks list" (Microsoft, direct Tier-1); (b) **derived views are lenses, not the working material** — smart lists gather from lists; the user's working surface remains the list; (c) **no plan-of-record, no progress rollup, no reporting layer** above the items; (d) the daily-focus ritual (nightly reset + suggestions) expresses the capture-and-remember posture rather than population management. The task pole inverts (a)–(d): organizing structure (containers + decomposition + classification) is deliberate and multi-layered, and population views (today/upcoming/board/filters) are the primary working material. The subject axis (personal vs team) is **not** the wall — confirmed from this side: all four sampled to-do products share lists with assignment; the task pass's Todoist serves work and life. Removal tests both directions: deepen the apparatus and make views the working material → the product is functioning as a task manager (Todoist's own evolution, self-labeled a to-do list app); strip the apparatus to lists of checkable items with the list as home → a to-do list (Microsoft To Do). Market blur is real and mutual; the two leaves are kept because the market contains structurally distinct product populations at each pole (platform-native to-do apps vs cross-platform task managers) and the center-of-gravity reading is stable.
2. **vs Personal Organizer (§03.13, processed 2026-09-08) — seam adopted; keep-both.** To-do = **one record type** (the item) with derived views; organizer = **multiple co-equal record domains** (schedule, tasks, contacts, notes) integrated in one application with cross-domain linkage. Removal test: add co-equal contact/calendar/note domains with attribute-driven linkage → organizer territory. No sampled to-do product presents contacts or notes as co-equal domains of record.
3. **vs Note-taking Application (§03.02, processed) — keep-both confirmed from this side.** The note pass held: "notes = information to remember; tasks = actions with state to complete; remove the action/state machinery → checklist inside a note (common), not a task app." Consistent: in note products the checklist is content inside a note record; in to-do products the item is the record of record, managed at list level with reminder/date affordances.
4. **vs Calendar Application (§03.08, processed) — completion-vs-clock seam confirmed from this side.** Items carry completion state and no inherent clock anchor; events are clock-anchored occurrences. Integration sits at the scheduled edge: Reminders' "create, manage, and complete your scheduled reminders right in the Calendar app"; To Do's "drag a task to your Outlook calendar"; RTM's "view my tasks in Apple/Google Calendar" — bridges, not merger.
5. **vs Kanban Task Board (§03.06 sibling, processed) — keep-both confirmed.** No sampled to-do product presents a board as the record or position-as-state; the list remains the container. The kanban pass's board-as-record seam holds from this side.
6. **vs Project Management Application (§03.07, processed) — keep-both confirmed.** No sampled product has a bounded-undertaking container, plan-of-record, or progress rollup; containers are lists, not projects with completion semantics.
7. **vs Household Chore Application (§29, processed) — confirmed not an audience variant.** Chore apps' cadence-first chore record and fairness/rotation machinery are absent here; recurrence in to-do products is an item attribute (the item re-materializes), not a chore-population management system.
8. **vs Work Management Platform (§03.07, unprocessed) — seam confirmed from this side; flag carried.** Discrete completable items for a person vs a team's whole operational work (requests, processes, approvals). Any.do's family/workspace Boards are the closest drift in this sample — shared boards with roles for household/team projects — but the record remains the task on a board; no request/approval/process machinery observed. The work-management pass should treat this as counterparty context.
9. **vs Focus Timer (§03.14, processed) — embedding test confirmed.** Any.do's Focus Mode is a bundled capability beside the lists; the product stays a to-do app (mirror of the task pass's TickTick pomodoro test).
10. **vs Time-blocking (§03.14, processed) — confirmed.** No time-block unit of record; calendar integration is at the scheduled edge, not work-to-time planning.
11. **vs Life Planning (§03.13, processed) — consistent with that pass's seam.** No persistent goal layer above the items; the Week Plan FAQ framing ("a to-do app does everything a to-do app does" + goal layer) holds from this side.
12. **vs Meeting Action-item Management (§03.10, processed) — consistent.** Action items birthed from meeting context are that Type's entry; the to-do app is the generic holder, meeting-agnostic.
13. **Grocery/shopping lists** — a specialization inside to-do products (Reminders grocery lists with auto-categorization; Any.do Smart Grocery Lists), not a separate Type; no directory leaf exists and none is requested.

## Historical / Market-Sample Check

- **Paper era**: a written to-do list (items on a sheet, crossed off when done) satisfies both L0 legs at analog level — item records with a completion act, held on a list that is the working surface. Remember The Milk's own self-description names this lineage ("sticky notes, whiteboards, random scraps of paper, or the back of your hand") — direct Tier-1 evidence that the paper list is the recognized ancestor.
- **Early PIM/Palm/Outlook-task generation** (1990s–2000s): list-centric to-dos with due dates and priority inside PIMs — satisfies the core with no cloud, smart lists, or sharing. (Asserted structurally; no primary page fetched this pass — kept at conceptual strength, consistent with the task pass's treatment.)
- **Web-native generation** (Remember The Milk, fetched): lists, Inbox, tags, dates, reminders, smart lists, sharing/giving — the same grammar at web maturity.
- **Modern platform-native generation** (To Do, Reminders, fetched): adds smart-list lenses, daily-focus rituals, location reminders, grocery categorization, suite integration — all excluded from the invariant.
- Verdict: the definition survives the historical check; it does not over-fit the current mobile-cloud pattern, and the list-as-home structure is the oldest and most stable part.

## Uncertainties

- **Google Tasks unreachable**: support.google.com timed out twice on 2026-09-09; the minimal platform pole is NOT evidenced in this pass and no claim rests on it. If a later pass needs the minimal pole, it should re-attempt Google Tasks plus a minimal third-party product.
- Any.do evidence is at help-center collection/article-title level (Tier 1 taxonomy); article bodies were not fetched, so My Day/Focus Mode/Boards mechanics are asserted at taxonomy level only.
- Remember The Milk's smart-list add-task routing ("What happens when I add a task to a Smart List?") was observed as a help question only; the answer page was not fetched — the existence of the question implies routing behavior, but the semantics are unverified.
- Microsoft To Do's "Creating daily habits" article body was not fetched; the habit pattern is evidenced at nav level only.
- The to-do/task gradient is a center-of-gravity judgment with real market blur (Todoist's self-label; To Do's "Tasks" section); recorded as a gradient, not a hard wall.
- Gamification layers (streaks/scores) common in the broader market were not observed in this sample's fetched pages; left unverified rather than claimed.
- Wunderlist/TeuxDeux-class historical consumer poles not fetched; held as conceptual lineage only.

## Final Synthesis

A To-do List Application is the personal application whose world is **lists of to-do items** — lightweight, individually addressable records of things the person intends to do, each completable by a check-off act (open→done). The **list is the primary container and the primary working surface**: capture, review, and completion happen on lists; derived views — daily-focus lists (often with suggestions and, in some products, a nightly reset that returns uncompleted items to their home list) and criteria-based smart lists — are lenses over the lists, and the items' home remains the list. Around this core, mature products add due dates and reminders (time and location), recurrence, subtasks, priority/flag, tags/notes/files, shared lists with assignment, search/sort/postpone, completed history, sync, quick capture, widgets, calendar and email bridges, and grocery-list specialization; platform substrates (iCloud/Exchange), family/workspace board layers, bundled focus/habit/calendar periphery, and AI assistance are variant packaging. The Type shares its record grammar with the Task Management Application — the wall between them is the management apparatus and the working material (list-as-home with lens views vs organized population with views-as-working-material), a center-of-gravity seam ratified by joint review, not a structural wall. The posture the Type realizes is capture-and-remember: hold what you intend to do, remind you, let you check it off.
