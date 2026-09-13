# Household Chore Application

## Overview

A **Household Chore Application** is an application for managing the routine domestic work of one household — the recurring tasks of keeping a home running: cleaning, tidying, laundry, dishes, trash, pet care and the like.

Its defining core is small:

```text
The household's routine work as the domain
└── The chore (a recurring domestic task with its cadence)
    └── The due-and-done cycle
        (due / overdue / next due → completion → record → schedule advances)
```

What the application replaces is not effort but the *coordination overhead* around household work: noticing what needs doing, remembering when it was last done, planning what today requires, deciding whose turn it is, and chasing everyone until it happens. The application holds that state so it does not have to "live in one person's head".

A chore application is not a general to-do list (arbitrary one-off tasks), not a family calendar hub (shared scheduling of everyone's lives), and not a home-maintenance planner (the physical fabric and systems of the house). The subject here is the household's routine living work, recurring on short cadences, done by the people who live there.

## Users & Context

The primary user is an adult member of a household — a parent, a homeowner, a partner, or a person living alone — who carries (or wants to distribute) the mental load of domestic work.

Typical reasons to open the application:

- see what needs doing today, and what can wait
- check when something was last done (the sheets, the bathroom, the oven)
- record that a chore is done
- assign or rotate chores among household members
- review how much each member has been contributing

Two recurring user configurations exist:

- **Shared households** — couples, families with children, flatmates. Adults assign and rotate chores; children may have their own simplified view, often with an approval step and rewards; roommates care mostly about fairness.
- **Solo users** — one person using the app as a personal cleaning plan for their home. A modern product typically serves this case fully without any member features.

The context of use is short, frequent, task-adjacent interactions: at the sink, on the sofa, on the phone — a glance at what's due, a check-off when done. Household applications therefore work on mobile phones first, with web, email, or print acting as companion or alternative delivery surfaces in some products.

## Core Model

### The defining core

Three structures, held together:

**The chore as the unit of record.** A chore is a recurring routine domestic task, held persistently. Its essential attributes are what to do, how often it realistically needs doing (its cadence), and usually some sense of effort or weight. Many products also attach a scope (the room or area it belongs to) and an assignee. The chore is durable: it exists between its completions, and it is the same chore from week to week.

**The due-and-done cycle.** The application computes, for each chore, its current state from two facts the user should never have to remember: the chore's cadence and when it was last completed. From these it derives whether the chore is due today, overdue, or not yet due, and when it will next come due. The user completes instances; the application records the completion and advances the chore to its next cycle. The accumulating record ("when was this last done, and who did it") is what turns a checklist into a management tool.

**The household as the application's world.** The chores are the routine work of one home. The domain is that household — its members and/or its spaces — not a team, a project, or an undifferentiated life list. This is what separates the Type from generic task software, even when the generic software is configured with a "cleaning" list: the chore record, its cadence-driven cycle, and the household frame are the organizing structure here, not an add-on.

Remove any one of the three and the product stops being recognizable: no chore-of-record → a static checklist or chore-chart template; no due-and-done cycle → cleaning tips with nothing managed; no household frame → a generic recurring to-do list.

### Standard capabilities of mature products

Modern chore applications commonly carry most of the following. They make the core cycle practical, but they are not what makes the product a chore application — a paper chore chart on the fridge satisfies the defining core with none of them.

- **Member profiles and assignment** — each member of the household is a profile; chores are assigned to a member once, or rotated automatically so the burden moves around the household over time.
- **Fairness machinery** — in shared households, products help keep the split acceptable: contribution targets per member, automatic rotation, per-person load limits on given days, or exclusions ("dad never does the litter box").
- **Room / area organization** — chores grouped by the part of the home they belong to (kitchen, bathroom, bedroom…), often with a per-area state indicator of how clean or how overdue things are.
- **Setup libraries** — a catalog of suggested chores with sensible default frequencies, from which the household picks and tweaks, instead of authoring every chore from scratch.
- **Due-state visualization** — color-coded indicators of what is due or overdue, often designed to make dirt or neglect visible and to reset visibly on completion.
- **Reminders and digests** — notifications at the right moment, and in some products scheduled email or printable schedules as the primary delivery surface.
- **Completion history** — a log of what was done, when, and by whom; the basis for contribution statistics and for answering "when was this last done?".
- **Motivational layer** — points per chore (often weighted by effort), streaks, leaderboards, and for children an approval step and rewards; some products add mascots or monthly challenges. Common in consumer products, absent in others.

### One structure, several scheduling philosophies

The most visible difference between products is not the feature set but *how the app decides what to do today*:

- **Dueness-based** — each chore has an interval; the app surfaces what is due since its last completion ("clean when it needs it, not because it's Tuesday"). Fixed weekdays play no role.
- **Schedule-generation** — the household configures people, chores, frequencies and constraints once; the app generates a fair weekly or daily schedule and delivers it by email or print.
- **Effort-budget** — the user says how much cleaning they want to do today; the app fills today's checklist with due tasks up to that budget.

These are alternative answers to the same question, not different Types; a product can combine them.

## How It Works

### Set up the household

```text
Create the household
→ add members (partner, children, roommates) — or skip for solo use
→ define the spaces (rooms/areas) if the product organizes by room
→ populate chores: pick from the product's suggestion library, then adjust
   (name, cadence, effort, room, who does it — or leave unassigned/rotating)
```

Setup is a one-time investment; the products deliberately front-load it ("a few minutes at the start") so that daily use becomes almost effortless.

### Run the daily cycle

```text
Open today's view
→ see the short list of what's due (and what's overdue)
→ optionally filter by room, effort, or time available
→ do the work
→ check the chore off (per member)
→ the completion is recorded; the chore's next due date advances;
   indicators reset
```

The interaction loop is deliberately short: glance → do → check off. The application's side of the loop — recomputing dueness, advancing cadences, updating contribution counts — happens without user action.

### Share the load

```text
Assign chores to members (once) or enable rotation (each cycle moves to the next)
→ members see what's due on their own devices
→ completions count toward each member's record
→ fairness views (targets, leaderboards, per-person schedules) make
   contribution visible
→ for children: completed tasks may require a parent's approval
   before they count and before rewards are granted
```

In the schedule-generation philosophy, this loop looks different on the surface: the household maintains people + chores + constraints, and the application continuously produces and distributes the schedule (by email, on paper, or in-app) rather than surfacing a live due list.

### Exceptions and frictions

- **Overdue chores do not disappear** — they persist visibly as overdue (often with a counter, "5 days overdue") until done; skipping a week degrades nothing permanently.
- **Life interruptions** — vacations and illnesses break the routine; some products provide an explicit pause/vacation mode, others simply let overdue state accumulate.
- **Unfair splits** — when complaints arise, the household adjusts configuration (exclusions, load limits, rotation) rather than re-negotiating daily.
- **Kids' completions** — subject to approval gating in family products, so a child cannot simply award themselves the reward.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Today / what's due

The primary daily surface.

- purpose: answer "what should I do right now?"
- typical information: due and overdue chores, per-room or per-area state, effort or time hints, who is assigned
- primary actions: check off a completion, filter (room / effort / dirtiness), open a chore

### Home / rooms overview

The household at a glance.

- purpose: show the state of the home as a whole, area by area
- typical information: rooms or areas with dueness or cleanliness indicators; sometimes the whole home's condition
- primary actions: drill into an area, open its chores

### Chore editor

Where the record is defined.

- purpose: create and maintain a chore of record
- typical information: name, room/area, frequency or interval, effort/points, assignee or rotation rule, notes/instructions
- primary actions: create from library or from scratch, edit cadence or assignment, delete or pause

### People / household

The member layer.

- purpose: manage who lives (and works) here
- typical information: member profiles (adults and often simplified child profiles), assignment overview, contribution statistics
- primary actions: add/remove members, configure constraints or targets, open a member's chore list

### Progress / motivation

The feedback surface.

- purpose: keep the household engaged and the split visible
- typical information: streaks, points, leaderboards, monthly totals, completion history
- primary actions: review history, approve children's completed tasks, claim or configure rewards

### Delivery surfaces beyond the app

In several products the schedule itself is a first-class artifact: emailed daily or weekly digests, and printable schedules (monthly, per person, per room) for the fridge door. Some products are deliberately web-plus-email-plus-print systems with only a view-only mobile companion; others are mobile-first with sync across members' devices.

## Important Rules / Behaviors

- **Completion advances the cycle.** Checking a chore off is not just list hygiene: it records the completion, resets the chore's due state, and schedules its next due occurrence from the cadence. The record of past completions is what the dueness calculation runs on.
- **Cadence belongs to the chore, not the calendar.** In the dueness-based philosophy, the chore carries its own realistic frequency; the same chore is due again an interval after each completion. In the schedule-generation philosophy, frequency is a scheduling input instead. Either way, recurrence is a property of the chore record, never re-entered by hand each time.
- **Overdue is a state, not an error.** Missed chores remain visible and quantified ("days overdue") until completed; nothing is cancelled or lost by inaction.
- **Children's completions can be gated.** In family products, a child's check-off may mark the task as pending until a parent approves it; only then does it count — for streaks, points, and rewards.
- **Fairness is configuration, not policing.** The application's answer to "it's not fair!" is to change the setup — rotation, targets, exclusions, load limits — so that the everyday loop runs without negotiation.
- **The household survives its members.** Chore records belong to the household, not to whoever did them last; members can leave or be added without the chore record being rebuilt.

## Variants

- **Dueness-based cleaning tracker** — rooms and per-task intervals as the spine; strong solo-user core; household sharing and fairness as an upper tier (e.g. Tody).
- **Gamified shared-cleaning app** — points, streaks and leaderboards as the spine; household members, effort-weighted scoring, and parent approval (e.g. Sweepy).
- **Family chore chart / schedule generator** — people + chores + fairness constraints in, generated schedule out; email and print as first-class delivery; rewards calculated from completions (e.g. ChoreBuster).
- **Chores as a module of a household ERP** — chore tracking inside a broader self-hosted household system (stock, shopping, meal planning, equipment); the chores feature set can be enabled or disabled (e.g. Grocy).
- **Audience variants** — families with young children (approval flows, pre-reader icons, rewards), couples and flatmates (fairness and rotation focus), solo adults (personal cleaning plan).
- **Deployment variants** — consumer cloud apps (mobile-first), web systems with email/print delivery, self-hosted open-source instances.

A variant remains a variant of this Type as long as the chore record and the due-and-done cycle for one household remain the center. When a product's center shifts to the shared family calendar with chores as one item layer, it has become a Family Organizer; when it shifts to the physical upkeep of the house (systems, appliances, seasonal care), it has become a Home Maintenance Application.

## Related Application Types

| Application Type | Distinction |
|---|---|
| To-do List Application | arbitrary one-off tasks with optional due dates; no household domain, no cadence-driven chore record, no member/fairness machinery; a to-do app with a "cleaning" list configured does not acquire this Type's cycle or domain |
| Task Management Application | team/work work-items, projects and workflows; different domain, roles, and structure |
| Family Organizer | a household hub whose defining conjunction includes the shared family calendar; its chore list is one item layer among others. Here no calendar hub is required and chores are the center. Bundling exists in the market, so center-of-gravity decides |
| Home Maintenance Application | recurring upkeep of the home's physical fabric and systems (filters, gutters, appliances) on long/seasonal cadences; here the subject is the household's routine living work on short cadences |
| Home Management Application | the home's whole-information binder of record (documents, appliances, warranties, property details); keeps no chore cycle as its center |
| Habit Tracking products | gamified personal repetition (self-improvement loop); the chore app's object is the household's shared work with assignment and fairness, not a personal habit |
| Cleaning Business Management | commercial software for cleaning companies (client jobs, staff scheduling, invoicing); different customer, different world — households here do their own work |
| Shared Team Calendar / Household Scheduling | schedule-of-record for events; chores here are recurring work records, not events, even when a schedule artifact is produced |

The two most important seams: against the **to-do list** (recurrence + household domain is the definition, not a configuration) and against the **family organizer** (the calendar-as-co-equal-defining-layer is the organizer's, not this Type's).

## Representative Products

- **Tody** — dueness-based cleaning schedule; rooms, per-task intervals, assignment/rotation, fairness targets, household sync.
- **Sweepy** — gamified home cleaning schedule; effort-weighted points, generated daily checklists, household leaderboards, parent approval.
- **ChoreBuster** — automatic fair chore-schedule generation for families; email/print delivery, per-person constraints, rewards from completions.
- **Grocy** — self-hosted household management ("ERP beyond your fridge") with household chores as one module among stock, shopping, and meal planning.

## Sources

Research date: **2026-09-08**

- Tody — official landing page and FAQ: https://todyapp.com/ , https://todyapp.com/faq
- Sweepy — official landing page: https://sweepy.app/
- ChoreBuster — official site and "How it Works": https://chorebuster.net/ , https://chorebuster.net/how-it-works.php
- Grocy — official site and README: https://grocy.info/ , https://github.com/grocy/grocy

> Sourcing limitation: several well-known family chore/allowance apps (including OurHome, Homey, Flatastic) could not be reached from the research environment on 2026-09-08 and were excluded; claims that depend on them (money-allowance economies, roommate-specific tooling) are kept qualified. The sampled products expose no multi-page help centers; official evidence is limited to product pages, FAQ, how-it-works and README content. Precise operational details (pricing, numeric limits, exact default cadences) are therefore not stated in this document.

Detailed observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
