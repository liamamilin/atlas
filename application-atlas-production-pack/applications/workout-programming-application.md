# Workout Programming Application

## Overview

A **Workout Programming Application** is the authoring-and-delivery application for training programs: software in which a coach, trainer, clinician, or trainee composes a plan of prescribed exercise sessions — each exercise named from a library and specified with performance parameters — arranges those sessions across days and weeks, and carries the finished program to whoever will execute it, as a single reusable artifact.

It solves a specific problem: training is designed once but performed repeatedly, over weeks, by someone other than (or in addition to) its designer. The program is the bridge — written before it is performed, portable between designer and performer, and reusable across athletes, teams, cycles, or the author's own training.

The defining core is small: exercise-based prescription, the multi-session program artifact, and portability of that artifact as a unit. Everything else commonly associated with these products — exercise video libraries, athlete apps, weight-room tablets, completion dashboards, marketplaces — is standard capability built on that spine. Remove the artifact and what remains is a workout log; add a held client relationship with a review loop and it becomes online coaching; let software continuously decide and adapt the plan and it becomes an AI coach; add accumulated training-state accounting with endurance semantics and it becomes an endurance training platform.

## Users & Context

The primary user is **the program's author** — strength and conditioning coaches (schools, clubs, collegiate and professional programs, tactical organizations), personal trainers, gym programmers, and clinicians who prescribe exercise. Authoring happens between sessions, ahead of the training week, at a desk or on the training floor.

The secondary user is **the executor** — athletes, clients, members, patients, or the author personally. The executor works in the gym, on the field, at home, or in a clinic, usually with a phone, a shared tablet, or a printout in hand.

Distribution contexts span four shapes: one-to-one (a coach and an athlete), one-to-many (a team, a class, a client roster), many-to-one (a program purchased or followed from a catalog), and one-to-self (a lifter programming their own training).

## Core Model

### The defining core

```text
Exercise (named, drawn from a library)
  └── Prescription (sets × reps × load scheme × rest × effort cues)
      └── Session (an ordered composition of prescribed exercises)
          └── Program (sessions arranged across a time structure — days, weeks, phases)
              └── carried as one artifact to its executor(s)
```

Three properties. Remove any one and the product stops being programming:

- **Exercise-based prescription.** Every element of the plan names a concrete exercise and specifies how to perform it — volume, load, rest, effort — as instructions written before the session happens. Without prescriptions the product is a calendar or a content library.
- **The program artifact.** A durable, named, editable composition of multiple sessions arranged across a time structure. The artifact exists before, and independent of, any particular execution; it is the thing that gets stored, copied, revised, and reused. Without it — with only single workouts — the product is a session logger.
- **Portability as a unit.** The program travels to its executor(s) as one thing: assigned to an athlete or client, deployed across a team, published for sale, printed or exported, or followed by its own author. The artifact survives the handoff — a team program is the same object whether one athlete or two hundred open it.

### Standard capabilities

Mature products commonly add, on top of that spine:

- **Exercise library** — a catalog of named exercises with instruction media (demonstration video, images, coaching notes), extendable with custom exercises. The vocabulary from which every program is composed.
- **Templates and program libraries** — reusable program and session templates, duplication, and libraries of previously built programs; building "from scratch or from templates" is the standard authoring accelerator.
- **Load schemes resolved per executor** — in strength programming, prescriptions are commonly written as percentages of a lift's maximum and resolved against each executor's tracked max, so one program scales across a whole roster; max and personal-record tracking support this.
- **Delivery surfaces** — a personal mobile app for executors, shared weight-room tablet or display views for facilities, and print/PDF export where paper still runs the floor.
- **Execution capture and reporting** — executors log what they did; the author sees completion, prescribed-versus-actual comparisons, and progress reports.
- **Groups and teams** — bulk assignment to teams or classes, with individual adjustments layered on as overrides.
- **Communication** — messaging, notes, and video exchange between author and executors around the program.
- **Commerce** — selling programs through a marketplace or payments portal at the coach-facing pole.

### One structure, many realizations

The core is conceptual; implementations vary:

```text
Concept:  Prescription parameters
Realizations:  sets × reps × absolute load (common in consumer and clinical use) ·
               sets × reps × percentage of tracked max (strength-team standard) ·
               timed work/rest circuits · effort targets (RPE-style)

Concept:  Delivery
Realizations:  personal mobile app · shared weight-room device · print/PDF ·
               marketplace purchase · self-follow inside the same app

Concept:  The author
Realizations:  the coach or trainer (dominant) · a published template or named plan ·
               an AI drafting assist · the trainee personally
```

A reader who has only seen one shape — say, a team deployment dashboard — should still be able to recognize a printed plan or a consumer program catalog as the same Type from the defining core.

## How It Works

### Compose

```text
Open the builder
→ pick exercises from the library
→ set prescriptions (sets, reps, load scheme, rest, effort)
→ order them into a session
→ arrange sessions across the week or training block
→ save as a named program — from scratch, from a template, or duplicated from the last cycle
```

Authoring is deliberately unconstrained in philosophy: leading products position the tool as giving the author full control of methodology rather than imposing a training system.

### Deliver

```text
Select the program
→ assign it to an athlete, a group, or a team
→ prescriptions resolve per executor (percentage loads computed against each person's max)
→ the program arrives on the executor's surface — app, shared device, or printout
```

One assignment can carry a program to a whole team; individual adjustments are overrides on the shared artifact.

### Execute

The executor performs the session guided by the prescription. Where the product captures execution, the prescribed values and the logged values sit side by side.

### Review and revise

```text
Execution data and completion reports come back
→ the author reviews (completion, prescribed vs actual, progress)
→ revises the program — adjusts the next block, re-assigns, or duplicates into the next cycle
```

Revision between training cycles is a normal part of the loop. Review depth varies widely: a glance at completion percentages at the team pole, prescribed-versus-actual workload analysis where the product tracks load.

### Reuse

The program outlives its first execution: duplicated into the next cycle, kept as a template, deployed to the next team, or published for others to follow. Reuse — not the individual workout — is the economic unit of this Type.

## Interfaces

Surfaces are described conceptually; exact layouts and names vary by product.

### Program builder

The author's primary workspace.

- exercise palette or library search, prescription fields per exercise, session ordering, a calendar or grid of sessions across weeks, access to templates and saved programs
- primary actions: compose, prescribe, arrange, duplicate, save

### Library (exercises and programs)

- browsable exercise catalog with demonstration media and instructions; saved programs, templates, and session blocks
- primary actions: search, preview, insert into a program, create custom entries

### Assignment / roster view

- the author's list of executors and their assigned programs, with delivery status
- primary actions: assign, adjust for an individual, message, review completion

### Executor's session view

- the prescribed session: exercises in order, sets/reps/load/rest, demonstration media; where supported, logging fields next to the prescription and a rest timer
- primary actions: view, log results, watch demonstration, complete the session

### Shared weight-room view

- a station- or rack-mounted shared device rendering each executor's program without personal phones
- primary actions: switch athlete, view the current set, log load and reps

### Reporting

- completion rates, prescribed-versus-actual comparisons, progress and record trends, exportable for staff or administrators
- primary actions: filter, compare, export

## Important Rules / Behaviors

### The prescription precedes the execution

This is the structural center of the Type: the artifact is authored before the sessions happen, and execution is recorded against a prescription that already existed. It is the deliberate contrast with workout logging, where the session itself is the starting point.

### Prescribed and actual remain distinct values

Where execution capture exists, what was prescribed and what was performed stay distinguishable — completion and prescribed-versus-actual reporting depend on it. A revision typically produces an updated program for the next cycle rather than silently rewriting what was already delivered.

### Load prescriptions can be relative

A signature strength-market behavior: prescriptions written as percentages resolve per executor against that person's tracked maxes, so one artifact scales across a roster. Prescriptions may equally be absolute loads, timed work, or effort targets — the parameter vocabulary varies by domain and product.

### One artifact, many executors

Team and class delivery is bulk assignment of a shared program with individual adjustments on top. The artifact stays one object; changes the author makes after delivery reach the executors' copies in mature products.

### The tool does not own the methodology

Products in this Type compete on authoring control and delivery, not on prescribing philosophy; several explicitly position themselves as giving the author full control rather than generating the plan. Adaptive and AI-generated programming exist at the edges but are not the center of the Type.

## Variants

- **Team / institutional strength & conditioning** — programs deployed across teams and whole athletic departments; shared weight-room hardware; monitoring and testing modules adjacent to the core.
- **Coach roster (1:1 + groups)** — personal trainers and coaches programming for a client roster, often with messaging and compliance views; sits on the seam toward online coaching.
- **Consumer program-library apps** — a catalog of ready-made programs the trainee picks, follows, and logs in one app; authorship outsourced to published coaches; auto-progression may adjust prescribed loads between sessions.
- **Clinical exercise prescription** — clinicians compose exercise programs from clinical libraries and share them with patients via app or print; the same artifact structure in a healthcare context.
- **Program commerce** — marketplaces and payments portals where programs are products; the artifact is sold without a relationship.
- **Facility / class programming** — a venue publishes the day's workout to its members, common in functional-fitness-style training.

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| Workout Tracking Application | closest everyday seam | the tracker centers the executed session — what was done; this Type centers the prescribed artifact — what is to be done, composed before execution. Trackers' "routines" are a capability layer here; logging here is a capability layer there |
| Online Fitness Coaching | sibling, easily confused | coaching centers the held client relationship with a review-and-adaptation loop; here delivery may be one-way and no relationship is required — a team, a marketplace buyer, a printout. Coaching platforms ship strong builders; the overlap is capability-tier, not Type-level |
| AI Fitness Coach | adjacent | there, the software itself composes and continuously adapts the plan for one trainee; here the artifact is composed — by a human, a template, or an AI assist — and then governs execution as written. Auto-progression and AI drafting sit on the gradient between |
| Endurance Training Platform | adjacent | endurance platforms close the loop: plan + captured execution + accumulated training state + season periodization with endurance semantics (thresholds, zones, load). Here the artifact is the center and capture is reporting, not accumulated state |
| Personal Training Management | different center | the training business — appointments, packages, billing, staff; programming may appear as a module |
| Fitness Assessment Application | upstream | assessment produces the measured references (maxes, baselines, test results) that prescriptions consume; testing modules inside programming products borrow that capability |
| Gym Management System / Fitness Studio Management | different center | member, facility, and class operations; programming is at most an add-on |
| Athlete Management System | adjacent add-on | wellness, readiness, and load monitoring layered over programming; the monitoring center is its own Type, separate from the programming artifact |

The most important everyday boundary is with the **Workout Tracking Application**, because the two meet inside the same consumer apps: the discriminator is what the product treats as its unit of record — the prescribed plan composed ahead of time (this Type) or the executed session logged after the fact (tracking).

## Representative Products

- **TeamBuildr (Strength)** — team/institutional strength & conditioning: periodized program builder with calendar and dateless views, percentage-based loading against athlete maxes, team deployment, shared weight-room tablet view, reporting and testing modules
- **TrainHeroic** — coach-facing programming and delivery for 1:1 clients and teams, with a program marketplace and athlete app
- **BridgeAthletic** — club/organizational strength programming: builder and exercise library, templates, prescribed-versus-actual reporting, delivery to phones and weight-room tablets
- **Boostcamp** — consumer pole: a free program library to pick and follow with built-in logging, plus self-authoring with AI assistance
- **ExorLive** — clinical prescription pole: a large video exercise library with program composition and sharing for clinic, fitness, municipal, and education customers

The definition was checked against the displaced baselines these products themselves name — paper program cards, whiteboards, spreadsheets, and printed plans — so the Type is not defined by any single delivery era or market segment.

## Sources

Research date: **2026-09-09**

- TeamBuildr — product site, Strength platform page, and features page: https://www.teambuildr.com/en/ , https://www.teambuildr.com/platform-strength , https://www.teambuildr.com/features
- TrainHeroic — product site and coach page: https://www.trainheroic.com/ , https://www.trainheroic.com/coach/
- BridgeAthletic — product site: https://www.bridgeathletic.com/
- Boostcamp — product site and FAQ: https://boostcamp.app/
- ExorLive — product site and help-center "Get started" article: https://www.exorlive.com/ , https://support.exorlive.com/hc/en-gb/articles/360000576589

> Sourcing limitations: the support/help centers of TrainHeroic and BridgeAthletic, and the deeper ExorLive help articles, were unreachable from the research environment (timeouts). Claims about those products rest on official product pages at feature-name strength; no operational details were asserted from them. Precise figures observed during research (exercise and program catalog sizes, pricing tiers, athlete-count limits, device capacities) are recorded in the paired Research Notes, not in this document.

Detailed product-by-product observations, the cross-product comparison, and the boundary analysis are recorded in the paired Research Notes.
