# Research Notes — Focus Timer

## Research Goal

Understand the Focus Timer as an Application Type (DIRECTORY §03.14 Time & Focus): what the defining core is, how products structure timed attention sessions, what varies, and where the boundaries run against Clock/Timer utilities, To-do/Task Management, Time Tracking, Time Blocking, Productivity Activity Tracker, and Distraction-free Writing.

## Initial Boundary (pre-research hypothesis)

- Core hypothesis: an application that structures self-directed work into deliberate, timed sessions of focused attention (the Pomodoro lineage), rather than measuring time for reporting (Time Tracking), planning future time (Time Blocking), or managing tasks (To-do List).
- Nearest confusions: generic countdown timer utilities (Clock app), task managers with a built-in timer, screen-time blockers, distraction-free writing apps with timers, habit trackers.
- Prior-pass anchor: the distraction-free-writing-application pass (STATUS 2026-09-07) recorded "vs Focus Timer (timer serves the writing vs session is the product)" — mirrored here.

## Research Questions

1. What is the minimal structure a product must have to be recognizable as a Focus Timer?
2. Is the work/break cycle (Pomodoro-style alternation) definitional, or only the dominant pattern?
3. Is the session record / statistics layer definitional or common?
4. How do products treat task linkage — optional attachment, or part of the core loop?
5. How do products handle session abandonment / interruption, and what enforcement postures exist (lenient vs strict)?
6. Where does distraction blocking belong — inside the Type (support capability) or outside (screen-time / digital wellbeing)?
7. What does the canonical Pomodoro Technique (the origin) contribute to the definition — which parts do applications digitalize?
8. Where exactly are the boundaries vs task managers that embed timers, and vs time-tracking tools?

## Representative Products

Selected for market representativeness + different product philosophies; all consumer/individual-scale (this Type has no enterprise pole):

| Product | Pole / philosophy | Evidence tier reached |
|---|---|---|
| Pomofocus | Minimal web Pomodoro timer + simple task attach; no account required | Official product page (Tier 2) |
| Forest | Gamified commitment (leave-app = lose the tree) + app blocking; session length user-chosen, no automatic break cycle in core loop | Official product page incl. FAQ (Tier 2) |
| Focus To-Do | Pomodoro + full task management merged pole; historical statistics; multi-device sync | Official product page (Tier 2) |
| Marinara Timer | Pure timing surface: Pomodoro preset / Custom intervals / Kitchen-timer mode; shareable timers; no tasks, no records | Official product page (Tier 2) |
| Pomodoro Technique (Cirillo, official site) | Not a product — canonical technique anchor (timer + planning + interruption handling + records) | Official technique page (Tier 1 for the technique) |
| TickTick (boundary anchor only) | Task manager embedding a Pomodoro feature — evidence for the capability-vs-Type boundary | Official features page (Tier 2) |

Rejected/substituted: Be Focused (desktop classic pole; transport errors ×2 — abandoned per network rules, no claims made). Goodtime (repo URL guess 404 — not retried). Focus Booster (believed discontinued, not attempted).

## Sources

- Pomofocus — https://pomofocus.app/ (fetched 2026-09-07)
- Forest — https://www.forestapp.cc/ (fetched 2026-09-07)
- Focus To-Do — https://www.focustodo.cn/ (fetched 2026-09-07)
- Marinara Timer — https://marinaratimer.com/ (fetched 2026-09-07)
- TickTick — https://ticktick.com/about/features (fetched 2026-09-07; boundary evidence only)
- Pomodoro Technique official — https://www.pomodorotechnique.com/ (fetched 2026-09-07)

Sourcing limitation: no Help Center / User Guide documentation was reachable for any sampled product (all product evidence is from official landing/product pages and on-page FAQs). Assertion strength calibrated accordingly; no precise operational parameters asserted beyond what the fetched pages state. A first fetch of https://ticktick.com/about/pomodoro-timer 404'd; the features page succeeded on the second attempt.

## Product Observations

### Pomofocus (evidence layer A — direct, product page)

- Self-description: "a customizable pomodoro timer that works on desktop & mobile browser… to help you focus on any task you are working on, such as study, writing, or coding. This app is inspired by Pomodoro Technique… developed by Francesco Cirillo."
- Stated workflow: choose task → start the 25-minute timer → "work on your task until the timer rings" → take a 5-minute break, then repeat.
- Adjustable intervals: "Adjust work sessions (25 min), short breaks (5 min), and long breaks (15-30 min) to fit your workflow" (marketing-page wording; values are the technique's traditional defaults, presented as adjustable).
- Task linkage: "Select a specific task you want to focus on" — tasks attach to sessions; progress tracking of "completed Pomodoros" and "daily productivity".
- Positioning: minimalist, distraction-free interface; sounds customizable; "no downloads, no registration" — anonymous, browser-based.

### Forest (evidence layer A — direct, product page incl. FAQ)

- Self-description: "a pomodoro-style focus timer with a twist — every minute of concentration grows a tree. Lose focus, and you lose the tree."
- Core loop: "Pick a focus length and a tree species. Your tree grows in real time as you focus." → "Use other apps and your tree dies." → "Finish the session — your tree joins your forest forever."
- Enforcement: leaving the app / using blocked apps during "strict sessions" kills the tree ("During each focus session, a tree grows while you stay focused. Open another app, and the tree dies"). The loss is explicitly framed as intentional motivation design ("that small sense of loss is intentional… visible progress and gentle accountability").
- No automatic work/break cycle in the core loop: the user picks a focus length; breaks appear as a separate tool ("Mindful Space — mindful breaks and guided breathing").
- Session history as visual record: "your sessions build into a visible record of how you spend your time"; "a living record of your focused time — progress you can see at a glance, not a dashboard."
- Focus Analytics: "track focus patterns, streaks, and total focused hours by day, week, or month."
- App blocking as support capability: "Deep Focus blocks selected apps during an active focus session" (allowlists; free on every tier). Also Time Guard — scheduled app blocks *outside* focus sessions ("no social media 9 to 5") — a screen-time/digital-wellbeing surface beyond the session.
- Social/group: "Plant Together — sync focus sessions with friends — everyone plants the same tree. If anyone gives up, the whole forest falls." Plus challenges, ambient sounds, cross-platform sync (iOS/Android/browser), ADHD-friendliness positioning, real-tree-planting partnership.
- Business model: free core (sessions, blocking, group focus, wellbeing tools) + optional upgrades (custom allowlists, advanced statistics, rewards).

### Focus To-Do (evidence layer A — direct, product page)

- Self-description: "an easy-to-use time and task management application… helps you to perform tasks efficiently."
- "Based on the Pomodoro Technique: Set an execution time for the task, focus on the task until the end of the time."
- Task management layer: collect/manage tasks, due dates, reminders, subtasks, repeat rules, notes ("make plans for work and study, record shopping lists…").
- Statistics: "Historical statistics — help you analyze the work time and the completion of the tasks, the time spent on work every day/week/month and the time ratio of your projects. Make time traceable."
- Sync across devices (phone/computer/tablet; Android/iOS/Mac/Windows/Watch/browser extension listed).

### Marinara Timer (evidence layer A — direct, product page)

- Three modes: "Pomodoro — traditional Pomodoro method timer with standard time periods. Each Pomodoro is a 25-minute cycle followed by a 5-minute break. After the fourth Pomodoro, you'll take a 15-minute break." / "Custom Timer — customizable time periods to match your team's needs. Simply add a name for each period and the length of time." / "Kitchen Timer — timeboxing timer – just set it and forget it."
- Motivation: Pomodoro felt "too rigid… 25-minute work segments with five or 15-minute breaks are not ideal for all individuals, companies or industries" → custom named intervals.
- Sharing: "share your productivity timer with teammates."
- No tasks, no accounts, no visible session records on the product page — a pure timing surface. The Kitchen Timer mode shows a generic countdown living *inside* a focus-timer product as an auxiliary mode.

### Pomodoro Technique — official site (evidence layer A for the technique canon)

- "The timer is only the starting point. The full Pomodoro® Technique includes daily planning, interruption management, and effort estimation — a complete system for making deep work sustainable."
- Canon structure (from the free sheets): To-Do Today sheet ("plan your daily Pomodoros… track completed Pomodoros and handle interruptions"), Activity Inventory ("list everything you need to do, estimate effort"), Records sheet ("record completed Pomodoros to understand how long tasks really take. Essential for improving your planning accuracy over time").
- Official free timers (web/Windows/PWA) + the original mechanical kitchen timer ("the physical act of winding creates commitment").
- Technique is trademarked; timer is one part of a larger method. The digital Focus Timer Type digitalizes the timer + session-record slice; planning/interruption machinery stays with other Types (or with paper).

### TickTick (boundary anchor — evidence layer A, direct)

- A to-do/task application. Under "Powerful productivity tools" it lists Habit Tracker, **Pomodoro** ("Break down complex tasks using the Pomodoro, stay focused, and conquer procrastination"), Eisenhower Matrix, Countdown — one feature among many, subordinate to the task model.
- "Statistics: track tasks, focus duration, and habit logs."
- Conclusion: when the timer is one embedded capability of a task-centric product, the product belongs to the task-management Type; the timer does not make it a Focus Timer.

## Cross-product Comparison

| Dimension | Pomofocus | Forest | Focus To-Do | Marinara | Technique canon |
|---|---|---|---|---|---|
| User-initiated timed focus session (A) | yes (25-min preset) | yes (user-chosen length) | yes ("execution time for the task") | yes (pomodoro/custom cycles) | yes |
| Application runs it visibly to a completion boundary (A) | yes (ring) | yes (tree growth real-time) | yes ("until the end of the time") | yes | yes (timer rings) |
| Attention/focus framing as product purpose (A) | yes | yes | yes | yes | yes |
| Work/break alternation (A) | yes, automatic cycle | no automatic cycle (breaks as separate tool) | yes (technique-based) | yes, incl. long break after 4 | yes (25/5/15-after-4) |
| Session records / stats (A) | yes (completed pomodoros) | yes (forest as record + analytics) | yes (day/week/month stats) | no | yes (Records sheet) |
| Task linkage (A) | yes (simple list) | optional tagging | yes (full task suite) | no | yes (To-Do Today sheet) |
| Adjustable intervals (A) | yes | yes | technique-based, adjustable | yes (custom mode is the point) | traditional values |
| Enforcement on abandonment (A) | none observed (lenient) | strict mode: leaving kills the session outcome | not stated on page | none observed (lenient) | interruption handling (paper) |
| Distraction blocking (A) | no (minimal interface framing only) | yes (in-session app blocking) | not on page | no | no |
| Accounts/sync (A) | none required | account + cross-device sync | account + full sync | none observed | paper sheets |
| Social/shared timers (A) | no | group sessions (shared fate) | no | shareable timer URLs | workshops/B2B |

Stable across all samples (B — cross-product commonality): the user-initiated timed focus session run visibly by the application; the attention-structuring purpose; interval customization; completion signaling.

Common but absent in ≥1 sample (L1 candidates): break cycles, session records/stats, task linkage, cross-device availability.

Present in only some (L2/L3): strict enforcement with loss framing (Forest), in-session blocking (Forest), scheduled blocking outside sessions (Forest — drift surface), group/shared focus (Forest, Marinara), gamification (Forest), anonymous use (Pomofocus, Marinara).

## Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

The **application-managed focus session**: a deliberate, bounded interval of intended focus that the user initiates, the application times visibly (count-down or count-up, preset-derived or user-chosen length), and which reaches a completion boundary (or is given up), in an application whose purpose is structuring attention for work/study.

- Remove the timed session → to-do list / planner (no session to run).
- Remove the application-run visible timing → generic productivity advice / activity log.
- Remove the attention-structuring framing (timing any arbitrary event) → Clock/Timer utility (Clock app, kitchen timer as utility).
- All four sampled products + the technique canon satisfy this minimal core; nothing else observed is required (Marinara has no records or tasks; Forest has no automatic breaks; Pomofocus has no account).

### L1 — Common Mature Structure

Very common in mature modern products but not definitional:

- Work/break rhythm (Pomodoro-style cycles: focus interval → short break → repeat; longer break after a set of focus intervals) — the dominant realization; Forest demonstrates it is not required.
- Session records and statistics (completed sessions, focused time per day/week/month; streaks; visual accumulation).
- Task linkage (attach the session to a task from a lightweight list; in one sampled product a full task-management suite).
- Adjustable interval lengths and completion sounds/notifications.
- Cross-device clients (mobile/desktop/browser) with sync (in account-based products).

### L2 — Variant / Optional Structure

- Enforcement posture: lenient (timer runs; user may walk away) vs strict (leaving/using blocked apps destroys the session outcome — loss-framed commitment design).
- In-session distraction blocking (app/site blocklists, allowlists) as a support capability.
- Beyond-session scheduled blocking (screen-time windows) — drift surface toward digital wellbeing/screen-time Types.
- Gamification and motivation design: visual growth metaphors, rewards, challenges, group focus with shared fate; real-world-impact tie-ins.
- Timer-mode flexibility: fixed preset cycles vs fully custom named intervals vs free count-up ("set it and forget it" timeboxing).
- Shared/synced timers for teams or classrooms.
- Ambient soundscapes / mindful break content.
- Account-optional / anonymous operation vs account + sync.
- Audience tuning: students, ADHD positioning, digital detox.

### L3 — Vendor-specific (research notes only)

- Forest: tree species, earned coins, real-tree planting via Trees for the Future (2,102,946 trees claimed), Time Guard / Mindful Space / Deep Focus branded modules, seasonal events, plan tiers (free core vs paid allowlists/statistics), "60M+ downloads" market claims, NYT quote.
- Pomofocus: "2 million users" claim, "Animedoro" blog concept, brand naming.
- Marinara: "Choose a flavor" naming, 352 Inc. attribution.
- Focus To-Do: platform matrix (Android/iOS/Mac/Windows/Watch/extension), "millions of users" claim.
- Pomodoro® trademark regime; Cirillo training program pricing ($49/$149 founding prices); official timer hardware SKUs.

## Vendor-specific Findings

All L3 items above. None promoted to the final document except as brief variant examples without numeric/market claims.

## Boundary Findings

- **vs Clock / Timer utility**: the focus timer's timing is bound to work-attention semantics (sessions of intended focus, breaks, focus framing). A generic countdown times anything. Evidence: Marinara's "Kitchen Timer" mode is a generic countdown living inside a focus-timer product as an auxiliary mode — the product identity comes from the session/attention framing, not from the countdown mechanism itself. Test: remove focus semantics → Clock utility.
- **vs To-do List / Task Management Application**: tasks may attach to sessions, but the task model is optional and thin in the Type (Marinara has none; Pomofocus a simple list). Direct evidence of the seam: TickTick (task-centric product) embeds Pomodoro as one feature among many; Focus To-Do merges a full task suite but still centers the session loop. Test: remove tasks → focus timer remains; remove the session loop → task manager.
- **vs Time Tracking Application (§ sibling, unprocessed)**: the focus timer times *deliberate, bounded* sessions for motivation and attention structure; time tracking's center is the continuous, accurate record of time spent for reporting/analysis/billing. The focus timer's records are a byproduct motivational surface, not a billing-grade ledger. Test: remove motivation framing + session bounding, add reporting/billing → Time Tracking. (Structural reasoning; sibling leaf unprocessed — no claims about specific time-tracking products.)
- **vs Time Blocking Application (§ sibling, unprocessed)**: time blocking plans *future* intervals on a schedule; the focus timer runs the *current* interval. Natural pipeline: planned block → executed focus session. Test: remove "run now" → Time Blocking; remove "plan ahead" → Focus Timer.
- **vs Productivity Activity Tracker (§ sibling, unprocessed)**: activity trackers measure ambient/automatic usage; the focus timer runs deliberately initiated sessions. Test: remove user-initiated sessions → activity tracker.
- **vs Distraction-free Writing Application**: mirrored from that pass's own boundary record — in writing apps the timer serves the writing; in a Focus Timer the session itself is the product.
- **vs Habit Tracker**: both may count streaks; the habit tracker centers a recurring-behavior loop, not timed attention sessions (TickTick lists Habit Tracker and Pomodoro as sibling features — direct evidence they are distinct capabilities).
- **vs screen-time / digital-wellbeing blockers** (no dedicated leaf in DIRECTORY): in-session blocking is a support capability here; when scheduled blocking outside sessions becomes the product's center (Forest's Time Guard pattern), the product is drifting toward a wellbeing Type.
- Historical check (§24): the original technique realization — a mechanical kitchen timer plus paper To-Do Today/Records sheets — satisfies the L0 core (deliberate timed sessions of intended focus, started and run to completion, recorded) with no app, no blocking, no gamification, no stats software. Early-era desktop pomodoro countdowns with 25/5 defaults and no accounts also pass. No era/region/platform pattern is baked into the core.

## Uncertainties

- No Tier-1 help-center documentation was reachable for any sampled product; operational details (exact default values per product, what happens on session interruption in each product, auto-start behaviors, notification specifics) are asserted only where product pages state them.
- Focus To-Do's enforcement/interruption behavior and Pomofocus's record retention are not documented on the fetched pages — left unasserted.
- The desktop-companion pole (Be Focused-class menu-bar timers) is uncharacterized (product unreachable ×2); the menu-bar/widget surface is documented structurally, not from a fetched source.
- Whether any sampled product supports count-up "flowtime" style sessions was not directly confirmed from official pages; the count-up form is admitted into the core model on structural grounds (the session is timed and bounded either way) and kept out of product-specific claims.
- Break-cycle default values (25/5/15-after-4) are stated by Marinara's page and the technique canon and Pomofocus's copy; they are presented in the final document as the technique's traditional values that products commonly expose as adjustable defaults — not as universal product constants.

## Final Synthesis

The Focus Timer is the application realization of timed-attention methods (dominantly the Pomodoro lineage): its defining core is the application-managed focus session — a deliberate, bounded interval of intended focus that the user starts, the application times visibly, and that ends in completion or give-up — plus the attention-structuring purpose that makes such a session meaningful. Around this core, mature products add the work/break rhythm, session records and statistics, task linkage, and adjustable intervals. Products differentiate along enforcement posture (lenient vs strict loss-framed commitment), motivation design (gamification, social focus, real-world impact), blocking support, timer-mode flexibility, and audience tuning. The Type sits between planning (Time Blocking), measuring (Time Tracking / Activity Tracker), and task management — distinct from each by its center: the run-now, deliberately-bounded attention session.
