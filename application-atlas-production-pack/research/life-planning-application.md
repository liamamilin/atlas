# Research Notes — Life Planning Application

Research date: 2026-09-08
Methodology: WORKFLOW v1.1 / WRITING GUIDE v1.1

## Research Goal

Understand what a **Life Planning Application** actually is from real products: what objects exist inside it, how a person's long-term intentions are represented and decomposed, what the working loop is (plan → act → record → review), and where the boundary lies against task managers, habit trackers, calendars, organizational goal platforms, and personal dashboards.

## Initial Boundary (hypothesis before research)

- Hypothesis: a personal, self-facing application holding the person's life goals, organized by life areas/values/roles, decomposed into habits and actions, with progress and periodic review.
- Adjacent Types suspected upfront:
  - To-do List / Task Management Application (task unit, no persistent goal layer)
  - Calendar Application / Time Blocking (time-slot as organizing unit)
  - Habit-tracking products (habit as unit, no goal hierarchy) — note: no dedicated habit-tracker leaf exists in DIRECTORY.md; this Type sits inside that neighborhood
  - OKR / Goal Management Platform (organizational goals, section 09 HR)
  - Personal Organizer / Personal Dashboard (sibling leaves in 03.13)
  - Journaling applications (reflection without plan structure)
- Known risk: the market label "life planner" is loose; some products are weekly task planners with a goal layer, others are pure goal hierarchies. Also a drift risk toward team/enterprise goal management (OKR territory).

## Research Questions

1. What is the central object — goal? area? habit? task?
2. How are goals authored (SMART fields, vision/mission, importance weights, target dates, metrics)?
3. How does decomposition work (subgoals, milestones, tasks, habits)? How deep?
4. Is there an organizing layer above goals (values, roles, areas, categories)? Is it required?
5. How is progress recorded and surfaced (roll-up, charts, streaks, trackers)?
6. What is the review loop (weekly review, journal, reports)?
7. Who uses it — only the person themselves, or also coaches/teams?
8. What social/accountability surfaces exist (shared goals, supporters, teams)?
9. What does the app NOT do — where is the line against task managers and OKR platforms?
10. Historical check: would paper-era life planning (goal worksheets, planner systems) satisfy the same model?

## Representative Products

Selected for different product philosophies and customer levels, all with reachable official documentation:

| Product | Philosophy | Customer level | Evidence quality |
|---|---|---|---|
| Goalscape | visual nested goal map ("big picture" wheel) | solo → teams → enterprise (recent positioning drift) | product overview + home, reachable |
| Lifetick | values → SMART goals → tasks, with trackers/journal/dreams | solo consumers (free + subscription), web + iOS | official homepage narrative; help/support pages unreachable (404) |
| GoalsOnTrack | full chain: goals → subgoals/milestones → action plans → habits → journal → vision board | solo consumers (paid), team version | official homepage + FAQ |
| Week Plan | weekly planning ritual organized by roles (7 Habits heritage), goals/milestones/OKRs above tasks | professionals, coaches, small teams | official site with framework chain, comparison table, FAQ |

Deliberately not sampled / dropped:

- **Strides** (habit & goal tracker) — strides.com is now a pharmaceutical company (Strides Pharma); the tracker product's site was not reachable in this pass. Not sampled.
- **Habitica** (gamified habits/tasks) — homepage returned an empty JS shell; used only as an unverified boundary counter-sample in reasoning, never as evidence.
- **Notion "Life OS" templates** — third-party templates over a generic workspace; noted as a variant phenomenon (reasoning-based), not sampled.
- Paper planners (Franklin Covey-style, bullet journal, passion planner) — used only in the historical check as reasoning anchors, marked as such.

## Sources

Fetched 2026-09-08 (all Layer A direct observation unless noted):

- Goalscape — https://www.goalscape.com/ (home), https://www.goalscape.com/product-overview/ (How Goalscape Works)
- Lifetick — https://www.lifetick.com/ (home; six-step model + feature narrative). Note: /features and /support returned 404; deeper operational docs unreachable this pass.
- GoalsOnTrack — https://www.goalsontrack.com/ (home incl. feature narrative + FAQ)
- Week Plan — https://www.weekplan.net/ (home incl. framework chain, comparison table, FAQ, schema.org featureList)

Source-access limitation: Lifetick's help center could not be reached; Lifetick-specific operational detail relies on its official homepage narrative only. Habitica and Strides were not sampled; claims involving them are reasoning-based, marked below.

## Product Observations

### Goalscape

Evidence: Layer A (official product-overview page).

- Central object: **goal**, arranged as a nested radial map. Top-level goal at the center, broken into **subgoals and sub-subgoals until concrete actions** — an explicit multi-level hierarchy.
- **Importance** set per goal; visual size reflects priority ("Set Importance on every goal so the visual size reflects what matters most").
- **Now / Next tags** label what to act on; filter by date, progress, responsibility, tag; generate goal lists ("To achieve your long term goals you always need to know what to do right now").
- **Progress**: "Mark progress as you go — the entire structure updates live, rolling up from leaves to the central goal." Explicit roll-up semantics.
- **Review**: "Review weekly to adjust priorities with confidence."
- Per-goal payload: notes, attachments, timescales, responsibility, tags; **color-coding to associate goals in different areas** (the "areas" concept as visual grouping, not a separate entity).
- Collaboration: share goalscapes, goal comments with email notifications, MS Teams integration, responsibility assignment.
- Positioning drift: current marketing leads with teams/enterprise/strategy/OKR ("manage goals and projects with teams of any size", OKR template, Olympic-program case study), but retains an explicit "For Individuals" pillar ("Gain clarity, structure, and the motivation to achieve personal and professional milestones").
- AI: AI Goal Coach drafts a structured goalmap (hierarchy of subgoals) from a described objective; Claude/MCP integration to create/restructure/update the goalmap.

### Lifetick

Evidence: Layer A (official homepage narrative; deeper docs unreachable — assertions restricted to what the page states).

- Six-step self-described model: (1) establish **core values** in life; (2) set goals via **S.M.A.R.T. methodology**; (3) **journal** experiences; (4) **track** any area of life to develop the right habits; (5) capture **dreams** that can later become goals; (6) **chart** progress over time.
- Goals carry tasks; **financial goals** track each task as a monetary amount that "adds up exactly to your goal amount" (savings / debt countdown / sales target) — goal-level quantity computed from child tasks.
- **Dreams** as a distinct object type: "Record it as a Dream so you can convert it to a goal when you are ready" — a pre-goal holding stage.
- **Journal**: "complete time stamped record of goal and task creation and completion, plus your own entries" (own entries at subscription tier).
- **Trackers**: custom life-area tracking with types "descriptive, financial, numerical, binary and count", feeding reports; framed as habit development ("develop the right habits for success").
- **Reports/charts** for goals, tasks, and custom trackers; CSV export.
- **Social**: share goals with friends/family/colleagues to work together; "enlist supporters who can view your own goals and cheer you on".
- Platform: web + iPhone app.

### GoalsOnTrack

Evidence: Layer A (official homepage narrative + FAQ).

- Central object: **goal**, set as SMART (a testimonial quotes the product's fields: "the goal, the purpose, start date, end date, metrics, subgoals, habits, and action plans"; the feature section states SMART goals with purpose and metrics).
- **Decomposition**: "break down long-term goals into milestones or sub-goals"; **categories** organize goals; per-goal single page shows "all its subgoals or milestones and what action to take for each of them".
- **Action plans**: tasks attached to goals, with **recurring tasks** and drag-and-drop calendar scheduling ("simply drag and drop tasks on your calendar to revise your schedule").
- **Habits**: "build good habits and link them to support your goals"; user decides duration/frequency; check off on "habit tracker calendars"; "software automatically tracks your habit strength and daily execution". Habits are explicitly goal-supporting machinery, not standalone.
- **Vision board**: upload pictures/music, animated slideshow for "visualization practice" — motivation apparatus above the goal.
- **Journal**: organized by goals and calendar months; bookmarks; small-wins recording without opening the journal.
- **Templates**: built-in goal templates "each providing a detailed action plan, some even with habits created for you".
- **Team version**: members share goals or keep them private; the team sees only publicly shared goals; visibility of "what everyone else is working on and how much progress is being made".
- Extras: iCalendar feed sync (Google/Yahoo/Outlook/iCal), one-click full-account data backup, AI toolbox for goal advice, responsive web + iOS/Android.

### Week Plan

Evidence: Layer A (official homepage incl. framework chain, comparison table, FAQ; the site links a structured "academy" for its concepts).

- Self-described stack: **Vision → Roles → Goals → OKRs → Tasks → Schedule** — a vertical chain from life direction to scheduled time.
- **Vision**: "finding your direction… getting clear on your long-term goals and what you want to get out of life"; includes a **mission statement** space ("Start with the End in Mind" — explicit 7 Habits heritage; testimonials and comparison table cite the Covey framework).
- **Roles**: role-based planning as the organizing layer ("I like how it links together roles, goals, tasks and a planner").
- **Goals**: "set clear objectives, break them into smaller steps", with **milestones**; Goals Planner page: "set long-term goals and create milestones, connect them with weekly actions".
- **OKRs**: an OKR layer ("track OKRs", "Big goals… kept visible with milestones and OKRs").
- **Tasks**: High Impact Tasks (HITs), **Eisenhower Matrix** prioritization, **weekly planning view** as the working ritual, **time blocking**, **Pomodoro timer**, time tracking, calendar sync.
- Self-definition via FAQ: "Is Week Plan a to-do list app alternative? — It does everything a to-do app does and adds features like goal tracking and focus planning." The comparison table lists "OKR / Goal Layer", "Role-Based Planning", "High Impact Tasks" as differentiators vs Motion/Sunsama/Todoist.
- Audience pages include a **Life Coach** use: "Plan your practice and your clients' progress in one weekly view. Share plans, track goals, and keep clients accountable between sessions."

## Cross-product Comparison

| Structure | Goalscape | Lifetick | GoalsOnTrack | Week Plan | Strength |
|---|---|---|---|---|---|
| Personally-defined goal as central object | A ✓ (top-level goal + subgoals) | A ✓ (SMART goals) | A ✓ (SMART goals) | A ✓ (goals under roles) | Universal in sample |
| Downward decomposition into smaller units | A ✓ subgoals → sub-subgoals → actions | A ✓ goals → tasks (financial: tasks sum to goal) | A ✓ subgoals/milestones → action-plan tasks | A ✓ goals → milestones → weekly actions | Universal in sample |
| Progress recorded and surfaced | A ✓ mark progress, live roll-up leaves→root | A ✓ charts, reports, typed trackers | A ✓ progress tracking with metrics; visible in team view | A ✓ progress; milestones/OKR visibility | Universal in sample |
| Organizing layer above goals | A ✓ color-coded areas/tags (visual grouping) | A ✓ core values | A ✓ categories | A ✓ roles + vision/mission | Universal but differently shaped — grouping device, not a fixed entity |
| Time-bound goal authoring | A ✓ timescales | A ✓ SMART (time-specific) | A ✓ start/end dates, metrics | A ✓ milestones, OKR periods | Common; SMART fields not universal (Goalscape uses importance weights instead) |
| Habits/routines attached to goals | ✗ (none documented) | A ✓ trackers framed as habit development | A ✓ habits linked to goals, strength tracking | A ~ "focused routine" framing | Common, not universal |
| Review/reflection surface | A ✓ weekly review guidance | A ✓ journal (timestamped auto-record + own entries) | A ✓ journal by goal/month | A ✓ weekly planning/reflect ritual | Common; form varies strongly |
| Pre-goal / aspirational objects | ✗ | A ✓ Dreams, convertible to goals | A ~ vision board (visualization) | A ✓ Vision/mission statement above goals | Common in some shape, optional as structure |
| Sharing / accountability | A ✓ shared goalscapes, comments, responsibility | A ✓ shared goals + supporters | A ✓ team version, per-goal privacy | A ✓ coach/team planning pages | Common optional; personal-solo remains the base case |
| Templates | A ✓ (business/OKR flavored) | ✗ not documented | A ✓ goal templates with action plans | ✗ not documented | Optional |
| Calendar / scheduling surface | ✗ (timescales only) | ✗ not documented | A ✓ recurring tasks, drag-drop calendar, iCal sync | A ✓ weekly view, time blocking, calendar sync | Common optional |
| Motivation apparatus (vision board, streaks, gamification) | ✗ | A ~ charts/achievements framing | A ✓ vision board | A ~ Pomodoro/bell | Optional/variant |
| AI assistance | A ✓ AI goal coach, Claude/MCP | ✗ | A ✓ AI toolbox advice | ✗ | Era-current optional |

Reading of the table:

- Four structures hold across all four sampled products (Layer B, universal-in-sample): personally-defined goals as central object; downward decomposition; recorded and surfaced progress; an organizing grouping layer above goals (values / roles / areas / categories — shape varies).
- Everything else varies: SMART authoring is common but not universal; habits, journals, review rituals, sharing, templates, calendars, motivation apparatus are common-to-optional.
- The vertical span is the signature: intention above (values/vision/roles/dreams) → goal of record → decomposition below (subgoals/milestones/actions/habits) → progress rolling back up → periodic review closing the loop. Task managers hold only the bottom of this chain; vision boards/journals hold only the top; OKR platforms hold the same chain but for an organization instead of a person's life.

## Canonical Model (synthesis)

### L0 — Defining Invariant

The smallest structure without which the Type stops being recognizable as a Life Planning Application:

1. **The person's own life as the subject of record** — the plan belongs to one person, self-defined and self-facing (even when shared with supporters or a team, the goals remain that person's).
2. **Personally-defined goals of record** — persistent, individually identified intentions the person sets for their own life, carrying some notion of target and time.
3. **Downward decomposition** — each goal is linked into smaller tracked units (subgoals, milestones, action tasks; optionally supporting habits), forming one plan structure from intention to action.
4. **Progress on the plan, surfaced over time** — progress is recorded on the plan's units (tasks done, subgoal percentages, tracker entries) and rolled up / charted against the goals; recording and reviewing progress is what makes it a plan rather than a list of wishes.

Jointly-held is load-bearing:

- 1+2 without 3 → an aspiration list / vision board.
- 2+3 without 1 → an organizational goal/OKR platform.
- 1+3 without 2 → a task/habit tracker (actions with no goal of record above).
- 2+4 without 3 → a goal register with charts but no execution path.
- 3+4 without 2 → a generic productivity tracker.

Anti-overfitting note: SMART goal fields are near-ubiquitous in the sample but Goalscape implements goal authoring through importance weighting and timescales with no SMART framing — so SMART is a **common authoring frame**, not an invariant. Likewise the organizing layer above goals is universal-in-sample but takes four different shapes (values / categories / color areas / roles), so the canonical concept is a *grouping layer*, not "values" or "roles" specifically.

### L1 — Common Mature Structure

Widespread in mature modern products, not required for the definition:

- organizing layer above goals: values, life areas, roles, mission/vision, categories — grouping devices, implemented very differently (values taxonomy / role list / color tags / categories)
- habits & trackers attached to goals as support machinery (habit calendars; typed trackers: binary/count/numerical/financial/descriptive)
- review/reflection surfaces: journals (auto-timestamped goal/task records + free entries), weekly review guidance, reports/charts
- sharing & accountability: shared goals, supporters, comments, per-goal privacy, team versions
- time/scheduling surfaces: target dates, timescales, recurring tasks, calendar views/sync, weekly planning views
- templates providing pre-authored goals with action plans
- motivation apparatus: vision boards, streak/habit-strength computation, achievement framing
- AI assistance for drafting goals/action plans (era-current)

### L2 — Variant / Optional Structure

- packaging philosophy: visual goal-map pole (Goalscape) vs values/SMART pole (Lifetick) vs full-chain pole (GoalsOnTrack: goals+habits+journal+vision board) vs weekly-ritual/roles pole (Week Plan)
- methodology packaging: 7 Habits/roles (Week Plan), SMART (Lifetick, GoalsOnTrack), importance-weighting (Goalscape); wheel-of-life/areas grouping common in the category
- social posture: solo-private default with opt-in sharing (supporters, shared goals) vs team mode
- audience variants: coaches planning clients' progress; families; ADHD-focused positioning (Week Plan audience pages)
- "life OS" phenomenon: the same model assembled on generic workspace tools via community templates (reasoning-based observation, not sampled)
- monetization: free tiers vs one-time/subscription; journal and custom trackers behind paywall in one product (Lifetick subscription note)

### L3 — Vendor-specific Structure

- Goalscape: radial nested wheel with size-encoding of importance; Now/Next tags; MS Teams integration; Claude/MCP goalmap editing; EU co-funded "Goalscape Flow" initiative
- Lifetick: Dreams object with goal-conversion; financial goals whose tasks carry monetary amounts summing to the goal; typed trackers (descriptive/financial/numerical/binary/count); CSV export
- GoalsOnTrack: vision board slideshow with transition effects/music; habit strength auto-computation; iCalendar feed sync; e-book/course marketing apparatus
- Week Plan: High Impact Tasks (HITs); Eisenhower Matrix; Pomodoro timer; 7 Habits framing and academy; "Sharpened the Saw" bell

## Historical / Market-Sample Check (§24 reasoning, marked reasoning-based)

Question: would older, regional, platform-native, or differently positioned products still fit the L0?

- **Paper-era life planning** (goal worksheets broken into steps, habit tick-calendars, journals, weekly review with roles — e.g. Franklin Covey-style planners): subject = the person ✓, goals of record ✓ (written goals with target dates), decomposition ✓ (steps under each goal), progress + review ✓ (ticked steps, weekly review). Satisfies the core with no cloud, no AI, no gamification. Pass.
- **Wheel-of-life coaching worksheets**: goals grouped by life areas with actions and review — same core, different organizing layer. Pass (confirms the organizing layer must stay abstract).
- **Pre-smartphone web goal trackers / new-year resolution lists with progress bars**: goals + progress satisfy the core; a bare resolution *list without progress tracking* fails leg 4 — correctly outside the Type (a wish list).
- **Team/enterprise goal products (OKR platforms)**: same four legs except leg 1 (subject is the organization/employee role, not the person's own life). Correctly a different Type; Goalscape's enterprise drift shows the boundary is real and actively crossed by vendors.

Conclusion: the L0 survives the historical check; nothing modern (cloud, AI, streaks, gamification, phone apps) is required.

## Vendor-specific Findings

Recorded above under L3. None promoted into the canonical document beyond neutral, non-branded description.

## Boundary Findings

| Nearby Type | Distinguishing test |
|---|---|
| To-do List / Task Management Application | Unit of record is the task; no persistent goal layer above. Week Plan's own FAQ frames the difference: a to-do app "does everything a to-do app does" while this Type **adds the goal layer above**. In a life planning app the task is instrumental — a child of a goal. Remove the goal layer → task manager. |
| Calendar Application / Time Blocking Application | Organizing unit is the time slot; in life planning time surfaces (dates, weekly views, timescales) are secondary projections of the plan, not the system of record. Goalscape has no calendar at all — and is still fully in-type. |
| Habit-tracking products (no dedicated directory leaf) | Unit of record is the habit; no goals of record above. In this Type, habits attach to goals as support machinery (GoalsOnTrack links habits to goals explicitly). Counter-sample (Habitica-class, reasoning-based): gamified habit/task tracker without a goal layer — different shape, adjacent Type. |
| OKR / Goal Management Platform (09 HR) | Same vertical chain (objective → key results/milestones → actions → progress) but the subject is the organization and the goals are work objectives assigned through an org hierarchy; review is managerial. The person's life is not the subject. Market drift is real: Goalscape now leads with teams/enterprise/OKR while retaining an individuals pillar — a live drift zone. |
| Personal Organizer / Personal Dashboard (siblings in 03.13) | Aggregation/console surfaces over miscellaneous personal information (email, files, widgets, feeds). No plan of record with goals/decomposition/progress. A dashboard can *display* goal progress but does not hold the plan. |
| Journaling applications | Reflection records without a plan structure. In this Type the journal (where present) is review machinery attached to goals (Lifetick and GoalsOnTrack both auto-log goal/task events into the journal). |
| Personal Finance Management / Budgeting | Money-domain system of record. Lifetick's financial goals (tasks as monetary amounts summing to the goal) are goal-planning semantics applied to money — not a transaction ledger. |
| Travel Itinerary Planner / Retirement Planning Application / Estate Planning Application | Domain-specific planning Types (trip / retirement finances / estate) with their own object models; "life planning" here is the person's *general* self-directed plan across domains. |

"去掉什么就变成另一个 Type" 判据总结：

- remove the person's-own-life subject → organizational goal/OKR platform
- remove the goal-of-record layer → task manager / habit tracker
- remove decomposition → aspiration list / vision board
- remove progress+review → static wish list / goal register

## Uncertainties

1. Whether periodic review should be L0. Resolved judgment: progress-recorded-and-surfaced is L0; the *review ritual* is a standard workflow supported by progress surfaces (all four products support it in some form — weekly review guidance, journals, reports), but no product enforces review as a structural gate. Held as L1 with strong wording in the workflow section.
2. Depth/naming of decomposition units varies (subgoals/milestones/actions/tasks); the canonical model keeps "smaller tracked units" deliberately generic. Exact per-product depth limits were not researched.
3. Lifetick evidence is homepage-only (help center 404); Lifetick-specific operational claims were kept to what the page states. Subgoal support in Lifetick is unverified — only goals→tasks documented.
4. Social/team sharing appeared in all four samples, but sampling may be biased toward web products with team monetization; mobile-first trackers were not sampled (Strides unreachable). Kept as "common optional", not core.
5. Habitica-class gamified trackers not directly documented (SPA shell); boundary claim is reasoning-based.
6. Directory has no dedicated habit-tracker leaf; noted as a taxonomy observation, not a problem with this leaf.

## Final Synthesis

A Life Planning Application is a **personal life-planning system of record**: the person's own life is the subject; the person defines persistent goals of record; each goal decomposes downward into smaller tracked units (subgoals/milestones/actions, optionally habits); progress is recorded on those units, rolled up/charted against goals, and reviewed to adjust the plan. An organizing grouping layer above goals (values, areas, roles, vision), SMART authoring frames, journals, sharing/supporters, templates, calendars, and motivation apparatus are standard or optional capabilities rather than the definition. The Type is bounded against task managers (no goal layer), habit trackers (no goal of record), OKR platforms (subject is not the person's life), dashboards/organizers (no plan of record), and journals (no plan structure). Paper-era life planning satisfies the core, confirming the definition is not overfit to modern implementations.

## Rejected Findings

Candidate structures considered and rejected for the defining core:

1. **SMART goal authoring** — present in 2/4 products explicitly (Lifetick, GoalsOnTrack) and echoed in Week Plan's milestone/OKR framing, but Goalscape authors goals through importance weights + timescales with no SMART fields. Rejected as invariant; held as a common authoring frame.
2. **Values / life areas as a required entity** — universal-in-sample but realized as four different mechanisms (values taxonomy, categories, color tags, roles). Promoting any one shape (e.g. "core values") would define the Type by one implementation. Held as an abstract grouping layer, L1.
3. **Habits as defining** — Goalscape has no habit structure and is fully in-type. Rejected; habits are goal-attached support machinery, L1.
4. **Journal as defining** — present in 2/4 (Lifetick, GoalsOnTrack), absent in Goalscape's documented structure, and in Week Plan folded into the weekly ritual. L1.
5. **Review as a structural gate** — supported everywhere as practice (weekly review guidance, reports, journals) but not enforced as a system state anywhere in the sample. Held as a defining *activity* in the workflow narrative, not a structural invariant.
6. **Vision/mission/dreams objects as defining** — week-plan vision, Lifetick dreams, GoalsOnTrack vision board, Goalscape top-level goal-as-root. The common function (direction above goals) is already covered by the goal-of-record + grouping-layer abstraction; the specific objects are variant realizations. L1/L2.
7. **Sharing/team features as defining** — all four sampled products have some sharing, but solo-private use is the base case and mobile-first trackers were unsampled. Held as common optional; single-source nuances (supporters vs team privacy) stay in notes.
8. **OKR machinery as defining** — only Week Plan names OKRs; Goalscape offers an OKR template. Rejected; it's the organizational-goal drift zone, not the personal Type.
9. **AI goal coaching** — 2/4 products, era-current. Optional.

## Evidence Notes for the Final Document

- Strong wording ("the defining structure is…") supported for: person-as-subject, goals of record, decomposition, progress surfaced (all Layer B, 4/4).
- Moderate wording ("mature products commonly…") for: grouping layer above goals, SMART authoring, habits, journals/review surfaces, sharing, calendars, templates.
- Qualified wording ("some products…") for: dreams/vision objects, vision boards, gamification/streaks, AI assistance, financial-goal arithmetic.
- No precise numeric limits, defaults, or pricing stated anywhere in the final document (none were researched to that depth; vendor pricing pages deliberately out of scope).
