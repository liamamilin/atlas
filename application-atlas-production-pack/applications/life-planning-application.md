# Life Planning Application

## Overview

A **Life Planning Application** is a personal application in which one person plans their own life. The person defines goals for the life they want — health, career, finances, relationships, personal growth — breaks each goal down into smaller tracked steps and supporting habits, records progress against those steps over time, and periodically reviews and adjusts the plan.

The defining structure is deliberately small:

```text
The person's own life (the subject of the plan)
└── Personally-defined goals of record
    └── Smaller tracked units (subgoals / milestones / action tasks)
        └── Progress recorded on those units, surfaced over time
```

Everything else commonly associated with this category — values and life-area taxonomies, vision and mission statements, SMART goal templates, habit trackers, journals, weekly review rituals, sharing with supporters or teams — is widespread in current products but is not what makes the product a life planning application. The same model works on paper with a worksheet and a pen; nothing in the definition requires cloud sync, apps, or AI.

When the system's subject stops being the person's own life and becomes an organization's objectives, or when the goal layer disappears and only tasks or habits remain, the product has crossed into a different Application Type (organizational goal/OKR platforms, task managers, habit trackers).

## Users & Context

The primary user is a **private individual acting on their own behalf**: the same person sets the goals, executes the actions, records the progress, and does the reviewing. This self-facing loop is the defining context — there is no manager assigning work, no customer, no counterpart required.

Typical reasons to open the application:

- define or reshape a long-term goal ("run a marathon", "save for a house", "change careers")
- decide what deserves attention now, among everything that matters
- check off today's or this week's actions and log progress
- review the week or month: what moved, what stalled, what to change
- reflect in writing on how the pursuit is going

Secondary usage contexts exist but do not change the model:

- **supporters and accountability partners** — some products let the person share goals with friends, family, or peers who can view progress and encourage them
- **coaches** — a coach may plan and track a client's goals in the same structure, with the client remaining the owner of the plan
- **teams** — several products offer a team mode in which members share (or keep private) their goals and their progress; the goals still belong to the individuals

Use is characteristically long-lived and revisited: the plan persists across months and years, and the application expects to be reopened repeatedly rather than consulted once.

## Core Model

### The Defining Core

Four properties, held together. If any one is removed, the product stops being a life planning application:

- **The person's own life as the subject of record.** The plan belongs to one person and concerns their own life, not an organization's objectives and not assigned work. Every goal in the system is ultimately "mine".
- **Personally-defined goals of record.** Goals are persistent, individually identified intentions the person sets for themselves, usually carrying a target (a completion state, a number, a date). They are the central objects; everything else in the system either feeds them or reports on them.
- **Downward decomposition.** Each goal is linked to smaller tracked units — subgoals, milestones, or concrete action tasks — forming one continuous structure from long-term intention down to what to do next. Some products extend this layer with recurring habits that support a goal.
- **Progress recorded and surfaced over time.** Progress is recorded on the plan's units (steps completed, percentage marks, tracker entries) and is rolled up or charted against the goals. This is what distinguishes a plan from a list of wishes: the application holds not only what the person intends, but how far along they actually are.

The four are load-bearing together:

```text
subject + goals, without decomposition   → a list of aspirations / vision board
goals + decomposition, without the personal subject → an organizational OKR platform
subject + decomposition, without goals   → a task manager or habit tracker
goals + progress, without decomposition  → a goal register with charts but no execution path
```

### The Plan Spans Two Directions at Once

A mature life planning application holds a **vertical span** that few other Application Types cover:

```text
Direction          values · vision · mission · dreams · life areas · roles
                      ↓ give rise to
Goals of record    persistent, time-bound, measurable intentions
                      ↓ broken into
Smaller units      subgoals · milestones · action tasks · supporting habits
                      ↓ feed back
Progress           recorded on the units, rolling up against the goals
                      ↓ closes the loop
Review             periodic reflection → adjust priorities → continue
```

Task managers and to-do lists hold only the bottom of this chain. Vision boards, mission-statement tools, and journals hold only the top. The life planning application is defined by holding both ends in one structure.

### Standard Capabilities Mature Products Add

These are common across current products and expected in the market, but they are not what defines the Type:

- **A grouping layer above goals.** Goals are almost always grouped under something: life values, life areas (health / finance / career / relationships), personal roles, or free-form categories. The grouping is realized very differently from product to product — as a values taxonomy the goals must attach to, as simple color-coded areas, as a role list, or as plain folders — but functionally it answers "which part of my life does this goal belong to".
- **Goal authoring frames.** Structured fields for defining a goal: target dates, measurable quantities, descriptions of purpose. The SMART frame (specific, measurable, achievable, relevant, time-bound) is a common authoring pattern; other products instead weight each goal by importance and let the goal map show priority visually. Either way, the goal of record typically carries more structure than a task's one-line title.
- **Habits and trackers as support machinery.** Recurring behaviors (exercise, reading, saving) tracked on calendars or typed trackers (numeric, binary, count, monetary), and — where the product links them — attached to the goals they serve. In some products the tracker entries feed the goal's progress calculation.
- **Review and reflection surfaces.** Journals that combine free entries with an automatic, timestamped record of goal and task activity; charts and reports of progress over time; guidance or structure for a weekly or monthly review.
- **Time and scheduling surfaces.** Target dates and timescales on goals, recurring tasks, calendar views or calendar-feed sync, and weekly planning views that turn next actions into a scheduled week.
- **Sharing and accountability.** Opt-in sharing of goals with supporters or fellow goal-setters; comments and encouragement; team modes with per-goal privacy.
- **Templates.** Pre-authored goals with suggested action plans (and sometimes habits), for people who do not know how to decompose a goal themselves.
- **Motivation apparatus.** Vision boards, streaks, habit-strength measures, achievement charts — optional mechanics aimed at keeping the person engaged.
- **AI assistance.** Era-current: drafting a goal hierarchy from a described objective, suggesting action plans, advising on progress.

### One Structure, Many Implementations

The model is written in conceptual terms; products realize each concept differently:

```text
Concept:  Grouping layer above goals
Implementation:  values taxonomy · life areas · personal roles · categories · color-coded areas

Concept:  Goal authoring frame
Implementation:  SMART fields · importance weighting + timescales · milestones · OKR-style pairs

Concept:  Smaller tracked units
Implementation:  subgoals · milestones · one-off action tasks · recurring tasks · habits

Concept:  Progress
Implementation:  completion marks · percentage that rolls up the hierarchy · typed tracker
                 entries (numeric/binary/count/monetary) · charts and reports

Concept:  Review
Implementation:  weekly review ritual · journal (auto-log + free entries) · progress dashboards
```

A reader who has only seen one implementation — say, a SMART-fields checklist app — should still be able to recognize a visual goal-map product, or a paper planner with roles and weekly reviews, as the same Application Type.

## How It Works

### Set direction and define goals

```text
(optional) articulate values / vision / roles — the direction layer
→ create a goal: name it, give it a target and usually a time frame
→ attach it to a life area, value, or role
→ optionally park vague ambitions as "dreams" or vision-board images
   until they are ready to become goals
```

### Decompose the goal into steps

```text
open the goal
→ break it into subgoals or milestones
→ under each, add concrete action tasks (some one-off, some recurring)
→ optionally link supporting habits ("run 3× weekly" under a fitness goal)
→ some products offer templates: a pre-decomposed goal to start from
```

The result is one structure from intention to action. A person should be able to look at any action task and trace it upward to the goal it serves — and look at any goal and see its full path of steps.

### Act and record

```text
consult the current-focus view (today's / this week's actions, now-next labels)
→ do the work outside the application
→ record it: check off tasks, mark subgoal progress, tick habit calendars
→ the application rolls progress upward — completing steps moves the goal
```

Recording is the engine of the whole model: unrecorded progress is invisible to the plan.

### Review and adjust

```text
weekly or monthly: open the progress picture (roll-ups, charts, reports)
→ compare intention against reality: what moved, what stalled
→ adjust: re-prioritize, re-schedule actions, revise or retire goals
→ (in products with journals) capture reflection alongside the automatic
   log of what was completed
```

This loop — plan, decompose, act and record, review and adjust — is the defining working rhythm of the Type. The weekly cadence is the one products most often structure themselves around; some people also step back at longer intervals to re-plan.

### Share for accountability (optional)

```text
choose a goal to share
→ invite supporters or fellow goal-setters, or publish to a team with privacy limits
→ others view progress and comment / encourage
→ the plan remains the person's own; sharing changes visibility, not ownership
```

### Defining core vs common vs optional

**Defining core** — without these, not a life planning application:

- the person's own life as subject of record
- personally-defined goals of record
- downward decomposition into smaller tracked units
- progress recorded on those units and surfaced over time

**Standard capabilities** — present in most mature products:

- grouping layer above goals (values / areas / roles / categories)
- structured goal authoring (dates, measures, SMART-style fields or importance weights)
- supporting habits and typed trackers
- review surfaces (journals, charts, reports) and weekly planning views
- time/scheduling surfaces (target dates, recurring tasks, calendar views)
- sharing and accountability features

**Optional / variant** — depends on product philosophy and audience:

- dreams / vision boards / mission statements as first-class objects
- templates with pre-authored action plans
- team and coach modes
- gamification, streaks, habit-strength scoring
- AI goal coaching

## Interfaces

The surfaces below are described conceptually; exact layouts and names vary by product.

### Goal map / goal tree

The home of the plan itself.

- shows all goals and their decomposition — as a nested visual map (with importance shown by size or position), an outline tree, or a list grouped by life area
- typical information: goal name, area/role, target or deadline, progress state, importance/priority
- primary actions: create a goal, decompose into subgoals/milestones, set importance or dates, open goal detail

### Goal detail

Everything about one goal on one surface.

- typical information: description/purpose, target and time frame, milestones or subgoals, linked tasks and habits, progress indicator, notes and attachments
- primary actions: add or complete a step, mark progress, edit the goal, record a note, share

### Today / week action view

Where the plan becomes daily behavior.

- typical information: today's or this week's tasks drawn from the goals, habit check-offs due, high-priority labels, sometimes a calendar or time-block layout
- primary actions: complete or defer an action, tick a habit, plan next week

### Progress dashboard / reports

The "how far along am I" surface.

- typical information: goal progress roll-ups, charts over time, tracker histories, completed-versus-pending views
- primary actions: inspect trends, filter by area/period, export where supported

### Review / journal

The reflection surface.

- typical information: a timestamped log of goal and task activity, the person's own dated entries
- primary actions: write an entry, bookmark notable moments, revisit past review periods

### Sharing / team surface

Optional accountability view.

- typical information: shared goals, supporters or team members, per-goal visibility state
- primary actions: share or unshare a goal, invite a supporter, comment

## Important Rules / Behaviors

### Progress rolls upward

The most consequential behavior in the model: recording progress at the smallest units changes the state of everything above them. Completing a task moves its subgoal; moving subgoals moves the goal; the goal map or dashboard reflects the change immediately. In some products this roll-up is a literal computation (child task amounts summing to a goal quantity; completion percentages averaging up the hierarchy); in others it is a live visual update. Either way, the person records at the bottom and reads at the top.

### Goals are durable and revisited

Goals persist across sessions, weeks, and years, with target dates rather than disappearing after completion of a single action. The application is built for long-term return visits; stale goals are adjusted or retired during reviews rather than silently lost.

### Sharing changes visibility, not ownership

Even in products with sharing, supporters, or team modes, the default posture is private, and shared goals remain the person's own: others view and encourage, they do not reassign or re-scope the plan. Team modes expose progress of opted-in members only.

### Habits serve the plan where they exist

When a product includes habits, they are framed as machinery supporting goals — checked off on calendars, measured over time — rather than as an independent life record. Products whose habits stand alone with no goal above them are drifting toward a different shape of product.

### Motivation mechanics stay optional

Vision boards, streaks, and celebration moments are present in several products but are not load-bearing: the plan's integrity does not depend on them, and many products in the Type have none.

## Variants

Common product philosophies within the Type:

- **visual goal-map** — the plan as one navigable picture, priority shown by size and position; decomposition depth over daily-planning features
- **values-and-SMART** — goals must attach to life values; structured SMART authoring; typed trackers and journals for the record-keeping side
- **full-chain** — goals plus everything downstream and upstream in one product: subgoals, action plans, recurring tasks, habit trackers, journal, vision board
- **weekly-ritual** — the week as the working unit: goals and milestones reviewed through a weekly planning pass, organized by personal roles and priority frameworks

Common variants by audience and packaging:

- **methodology packaging** — products built explicitly around a named self-management method (role-based weekly planning, SMART coaching) versus method-neutral tools
- **coach-facing** — the same structure used to plan and track a client's goals between sessions
- **team mode** — individual goals shared into a small team view; the organizational-goal territory begins where goals stop belonging to individuals' lives
- **"life OS" workspaces** — the same model assembled by individuals on generic note-and-database tools through community templates; a common contemporary pattern rather than a distinct product Type
- **mobile-first trackers** — lightweight apps centered on habit and metric tracking with a light goal layer; the thinner end of the Type

## Related Application Types

| Application Type | Distinction |
|---|---|
| To-do List Application | the task is the unit of record and the top of its world; no persistent goal layer above. In a life planning application the task is instrumental — a child of a goal |
| Task Management Application | organizes work by project and task, typically for execution breadth; lacks the long-horizon goal-of-record layer and life-domain grouping |
| Calendar Application / Time Blocking Application | the time slot is the organizing unit; in life planning, dates and weekly views are projections of the plan, not the system of record (a visual goal-map product may have no calendar at all) |
| OKR / Goal Management Platform | same vertical chain (objective → milestones → actions → progress) but the subject is the organization and its employees' work objectives; goals cascade through an org hierarchy and reviews are managerial. The boundary is the subject: whose life the goals belong to |
| Personal Organizer | a console for miscellaneous personal information (notes, contacts, files, lists); no plan of record with goals, decomposition, and progress |
| Personal Dashboard | an aggregation/display surface that can *show* goal progress but does not hold or operate the plan |
| Personal Finance Management Application | a money-domain system of record (transactions, budgets, accounts); a life planning product may carry a savings *goal* with monetary steps, but it keeps no ledger |
| Journaling applications | reflection records with no plan structure; in life planning products, the journal (where present) is review machinery attached to goals |
| Domain-specific planning Types (travel itinerary, retirement, estate planning) | plan a single domain with their own object models; the life planning application is the person's general, cross-domain self-directed plan |

The most important boundary is the **subject line**: organizational goal platforms run the same machinery for a company's objectives; task and habit tools run the bottom half of the chain for anyone's immediate work. What makes this Type distinct is that the *person's own life* is the subject, and the whole vertical span — direction, goals, steps, progress, review — is held in one place.

## Representative Products

- Goalscape — visual nested goal map; importance-weighted goals with live progress roll-up
- Lifetick — values → SMART goals → tasks, with trackers, journal, dreams, and progress charts
- GoalsOnTrack — goals with subgoals/milestones, action plans, goal-linked habits, journal, vision board
- Week Plan — weekly planning ritual organized by roles, with goals, milestones, and OKR-style tracking above tasks

The defining core was also checked against older and paper-based planning practice (goal worksheets decomposed into steps, habit tick-calendars, journaling, weekly review with roles) to avoid defining the Type by any single current implementation.

## Sources

Research date: **2026-09-08**

- Goalscape — https://www.goalscape.com/ , https://www.goalscape.com/product-overview/
- Lifetick — https://www.lifetick.com/
- GoalsOnTrack — https://www.goalsontrack.com/
- Week Plan — https://www.weekplan.net/

> Sourcing limitation: official product pages were reachable; Lifetick's help-center paths returned errors, so Lifetick-specific operational detail relies on its official homepage narrative only. A habit-tracker counter-sample and a mobile-first tracker product could not be documented directly in this pass; related claims are held at reduced strength. Precise numeric limits, defaults, and pricing are intentionally not stated in this document; detailed observations are recorded in the paired Research Notes.
