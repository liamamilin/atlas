# Lean Construction Planning

## Overview

A **Lean Construction Planning** application is the site production team's collaborative commitment-planning system. It holds the near-term plan of construction work as a **shared commitment plan** — a lookahead of approaching work plus a weekly work plan of promises — built with and held by the performing trade parties themselves. It gates the promotion of planned work into commitments through **make-ready constraint management**: each planned task's prerequisites are tracked as first-class constraint objects that must be cleared before the work is promised. And it closes the loop with **promise-keeping measurement**: completion is checked against the week's commitments, measured with reliability metrics (PPC-class), and every variance is recorded with a reason that feeds re-planning.

The Type operationalizes the Last Planner System® — the lean-construction methodology in which the people who will perform the work make the promises about it, and the production system's reliability is measured and improved week by week. Its center of gravity is the near-term commitment plan, not the calculated master schedule: the master schedule (typically a CPM programme owned elsewhere) is consumed as the upstream target and synchronized, not calculated here.

## Users & Context

The defining context is a construction project in execution, where multiple independent trade partners must coordinate handoffs under schedule pressure. The software is used by the whole production community, not by a single planning office:

- **Trade partner foremen and crews ("last planners")** — the people who will do the work. They add their own tasks, make the weekly commitments, report completion, and record why promised work did not finish. In mature deployments they participate directly in the system rather than receiving plans from above.
- **Superintendents and field engineers** — run the lookahead, chair the weekly work plan meeting and daily huddles, remove constraints, and keep the plan current.
- **Project managers and lean champions** — orchestrate the planning cadence, facilitate pull planning sessions, and work the reliability metrics.
- **Schedulers / planning teams** — own the master schedule upstream; they import or synchronize it and receive progress back.
- **Owners and designers** — observe progress and reliability analytics; several products deliberately give them free access to keep the whole team in one plan.

The characteristic work rhythm is meeting-structured: collaborative pull planning sessions when a phase is sequenced, a weekly work plan meeting where commitments are made and last week's promises are reviewed, and short daily huddles during execution. The software is the shared surface for all of these — in the trailer, in the field on tablets and phones, and on large shared displays in the planning room.

## Core Model

### The Defining Core

Three structures together make the Type. Remove any one and the product stops being recognizable as lean construction planning.

**1. The shared near-term commitment plan of record.** The plan of upcoming site work is held persistently at two horizons:

- the **lookahead** — approaching work (commonly a few weeks out) broken down from phase or master-schedule activities into field-executable tasks, each bound to a trade or crew and a time window;
- the **weekly work plan** — the set of promises the performing parties have made for the current week, drawn from the lookahead.

This plan is *shared* (one current version the whole team sees) and *commitment-based*: a task on the weekly plan is a promise by a specific performing party, not an assignment handed down. The plan is the record — it survives sessions, accumulates history, and is the reference against which reliability is judged.

**2. Make-ready constraint gating.** Planned work carries its prerequisites as explicit **constraints** (also called roadblocks or blockers): missing design information, unapproved submittals, undelivered materials, permits, access, or prerequisite work by another trade. Each constraint has an owner and a status, and is tracked to removal. The discipline the software enforces is directional: work is only promotable into a commitment when its constraints are cleared — the team first establishes what *can* be done, then commits to what *will* be done. Some products make this separation explicit in the interface, separating ready work from work that should be done but is not yet ready.

**3. The promise-keeping reliability loop.** At the end of each week (and continuously during it), committed tasks are evaluated as completed or not completed as planned. Completion is aggregated into a reliability measure — Percent Plan Complete (PPC) or an equivalent — and every task that did not go to plan is recorded with a **reason for variance** (and, in deeper implementations, root causes). The reasons are the improvement engine: they show the team what breaks its promises and feed the next planning cycle.

**Binding: construction production semantics.** The object world is site work — activities broken into field-executable tasks, organized by trade, crew, location, and phase, with handoffs between trades as the thing being coordinated. Remove this binding and the same three structures describe a generic task board.

### How the Objects Relate

```text
Master schedule / phase target  (upstream, often external)
        ↓  pulled from / synchronized with
Phase plan  (built collaboratively, often by pull planning)
        ↓  broken down into
Lookahead tasks  (field-executable, per trade/crew)
        ↓  gated by
Constraints / roadblocks  (owner, status, cleared before commitment)
        ↓  promoted to
Weekly work plan commitments  (promises by performing parties)
        ↓  evaluated as
Completion + PPC + reasons for variance
        ↓  fed back into
Re-planning and the next cycle
```

### Standard Capabilities of Mature Products

These are widespread in the market and make the Type practical, but they are not what makes a product a lean construction planner:

- **Pull planning** — the signature method for building a phase plan: the team sequences work backward from a target date, each trade defining the handoffs it needs, on a shared board where connections between tasks are first-class. Mature products digitize the sticky-note wall (real-time shared boards, touch displays, drag-and-drop) and several add automatic calculations that check whether the emerging sequence can meet its targets and which paths are late.
- **Master schedule linkage** — importing or synchronizing with the CPM programme (P6, MS Project, Asta formats are common interchange targets), with progress on committed work flowing back so the master schedule stays current.
- **Daily huddle support** — surfaces for reviewing yesterday's completions and today's tasks.
- **Mobile field apps** — status updates, constraint reporting, and plan viewing from the jobsite.
- **Analytics and reporting** — PPC trends, variance reports, constraint-removal performance, S-curves; exportable or dashboard-based.
- **Broad participation** — trade partners, owners, and designers invited into the same environment; several products make stakeholder seats free or unlimited, expressing the methodology's collaborative premise in the business model.

## How It Works

The core workflow is the Last Planner cycle. Products differ in emphasis, but the loop is the same:

### 1. Establish the target and build the phase plan

The team takes a phase or milestone from the master schedule (or defines one) and sequences the work to hit it. The characteristic act is **pull planning**: in a facilitated session, the trades work backward from the target, each successor asking its predecessors for what it needs and by when, so the plan emerges as a network of handoffs rather than a top-down list. Digital products run this on a shared canvas — cards for tasks, connections for handoffs, real-time multi-user editing, sometimes with automatic checks of whether the sequence meets its dates.

### 2. Run the lookahead and make the work ready

Work from the phase plan enters the lookahead. As tasks approach, the team identifies their constraints, assigns each an owner, and tracks removal. The lookahead is worked as a readiness pipeline: tasks whose constraints are cleared become candidates for commitment; tasks with open constraints stay in make-ready, and the constraint log is the working list for getting them ready. Several products surface this as an explicit distinction between what *can* be done and what *should* be done.

### 3. Commit the week

In the weekly work plan meeting, each trade commits to the work it will perform in the coming week — drawn from the constraint-cleared candidates. The commitment is the promise: it names the performing party, the task, and the window. The meeting also reviews the past week: what was promised, what was done, and why anything slipped.

### 4. Execute with daily huddles

During the week, crews update task status from the field (mobile apps are the standard surface). Short daily huddles review yesterday's completions and today's plan, and surface new constraints as they arise — products encourage logging roadblocks immediately rather than hiding them, with ownership visible so someone removes each one.

### 5. Measure and learn

Completion is evaluated against the weekly plan. The reliability measure (PPC-class) is computed, variance reasons are recorded for every task that did not go to plan, and the patterns — which constraints recur, which trades' promises fail and why — feed the next cycle. Over time this is the mechanism by which the team's plan reliability improves.

### Capability Tiers

- **Defining core** — the shared lookahead + weekly work plan; make-ready constraint gating; the reliability loop with variance reasons.
- **Standard in mature products** — pull planning; master-schedule import/sync; daily huddle support; mobile field updates; PPC/variance analytics; broad stakeholder access.
- **Variant / optional** — takt planning (structuring work into repeating time intervals across zones); owning a CPM engine in-product; portfolio-level dashboards across projects; integrations with construction-management platforms (RFIs and submittals feeding the constraint log); BIM/4D linkage; AI-assisted planning (an emerging layer).

## Interfaces

Exact layouts and names vary by product; the following surfaces are common.

### Pull-planning board

The collaborative canvas where a phase's work is sequenced backward from its target.

- typical content: task cards by trade, handoff connections, target milestone, annotations for areas of the plan
- primary actions: add and move tasks, connect handoffs, run readiness calculations, identify late paths, publish the resulting plan to the lookahead

### Lookahead view

The readiness pipeline for approaching work.

- typical content: tasks by week or window, trade/crew assignment, constraint indicators, readiness state
- primary actions: break down master-schedule activities into field tasks, log and assign constraints, promote ready work toward commitment

### Weekly work plan board

The commitment surface for the current week.

- typical content: each trade's committed tasks, status (planned / in progress / complete / not completed as planned), the past week's results
- primary actions: commit tasks, update status from the field, record completion and variance reasons

### Constraint / roadblock log

The make-ready register.

- typical content: each constraint's description, affected tasks, owner, due state, status
- primary actions: log a roadblock, assign an owner, track removal, see which commitments are at risk

### Analytics / reliability dashboard

The measurement surface.

- typical content: PPC over time, reasons for variance, constraint-removal performance, milestone variance, per-trade reliability
- primary actions: review trends, drill into failed commitments, prepare the weekly meeting

### Mobile field app

The jobsite companion.

- typical content: my tasks, today's plan, constraint reporting
- primary actions: update task status, log a roadblock, participate in the huddle

### Master-schedule connection

The upstream integration surface — import of CPM files (P6/MS Project/Asta formats are common) or live synchronization, with progress flowing back to the master schedule.

## Important Rules / Behaviors

- **Only ready work is committed.** The make-ready discipline is directional: constraints must be cleared before a task is promotable to a weekly commitment. Committing unready work is the failure mode the whole structure exists to prevent.
- **Commitments are made by the performers.** Trade partners add and commit their own work; the plan is not assigned top-down. This is both a workflow rule and the methodology's premise — products are designed so trades plan their own tasks rather than receiving them.
- **No silent slippage.** Every committed task is evaluated as done or not done as planned; a task that slips must carry a recorded reason. The variance record is not optional bookkeeping — it is the input to the improvement loop.
- **The past week is reviewed before the next is planned.** The weekly meeting structure (review → learn → commit) is built into how the products present the plan.
- **Progress flows back upstream.** Where a master schedule is synchronized, completion of committed work updates it — the lean record lives in the commitment plan, but the master schedule stays fed.
- **The whole team plans in one place.** Products deliberately admit all stakeholders — trades, owners, designers — often at no per-seat cost, because the methodology depends on the performing parties being present in the planning environment.
- **Constraints are surfaced, not hidden.** Products encourage loading the plan with visible roadblocks early, so they can be removed before crews mobilize.

## Variants

- **Pure-play collaborative lean overlay** — the lean workflow is the product; the master schedule lives in external scheduling software and is synchronized in (Touchplan, vPlanner, Nialli Visual Planner).
- **Combined scheduling + lean platforms** — the product owns both a master-schedule module (up to a full CPM engine) and the lean commitment layer, selling "one platform from master schedule to weekly commitment" (Outbuild, VisiLean).
- **Org-scale lean transformation platforms** — lean planning embedded in a broader lean-method portfolio (visual management, 5S, continuous improvement, takt at organizational scale), sold as a company-wide practice platform (lcmd).
- **Takt-oriented production planning** — takt zones, repeating time intervals, and cadence-based sequencing as a first-class method beside or instead of pull planning.
- **AI-assisted planning (emerging)** — generated pull plans, automatic constraint detection from project documents, predictive reliability, and AI-prepared huddle summaries.
- **Suite-embedded** — enterprise construction/scheduling suites offering Last Planner-aligned task management as a module.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Construction Scheduling | closest sibling | Scheduling owns the **calculated master schedule** — the activity network whose dates are derived from durations, dependencies, and calendars, with critical path, float, and baseline discipline. Lean planning owns the **near-term commitment plan**; the master schedule is consumed and synchronized, not calculated. Lookaheads exist in both: in scheduling they are derived working views of the master; in lean planning the lookahead and weekly plan are where the record lives. Some products (VisiLean, Outbuild) span both — the lean layer is what they sell as the differentiator. |
| Construction Project Management | broader sibling | PM manages the whole project record — RFIs, submittals, drawings, cost, documents. Lean planning centers the production commitment loop; RFIs and submittals may feed its constraint log as integrations, but the project record is not its object world. |
| Project Controls Platform | adjacent sibling | Controls govern cost + schedule + risk + change at program level. Lean planning's metrics (PPC, variance reasons) are production-reliability measures at the workface, not controls metrics. |
| Construction Field Management | complementary | Field systems record site execution events (daily logs, punch, safety, quality). Lean planning orchestrates near-term production commitments; field progress feeds both. |
| Task Management / Kanban (generic) | overlapping surface, different Type | Lean boards look kanban-like, but generic task tools lack the construction production binding: trade partners, handoffs, master-schedule lineage, make-ready constraint machinery, and reliability measurement. |
| Production Planning / APS (manufacturing) | same word, different world | Factory finite-capacity sequencing of orders on work centers — not site commitments by trade partners. Lean construction borrows manufacturing philosophy, not its software object world. |
| Preconstruction Management | different phase | Preconstruction covers estimating, bidding, and constructability before field work; lean planning operates on in-flight production. |

## Representative Products

- **Touchplan** (MOCA Systems) — pure-play collaborative Last Planner platform synchronized with the master schedule; widely used by large US general contractors
- **vPlanner** — pull-planning-first system implementing the Enhanced Last Planner System, with advanced production metrics and CPM integration
- **lcmd** — European org-scale lean construction platform spanning strategic planning to daily jobsite control, with strong takt support
- **Outbuild** — combined master-schedule and field-coordination platform with lookahead, weekly work plan, roadblock management, and pull planning
- **VisiLean** — combined browser platform with a full CPM engine plus Last Planner and takt planning, used by European enterprise contractors

Also present in the market: Nialli Visual Planner (visual planning designed for the Last Planner System), Oracle Primavera Cloud task management (Last Planner alignment inside an enterprise scheduling suite), and AI-era entrants.

## Sources

Research date: **2026-09-10**

- Touchplan — product site: https://touchplan.io/ ; Lean Construction Planning page: https://touchplan.io/digitize-lean-construction-planning/
- vPlanner — Products page: https://vplannerapp.io/products
- lcmd — Lean Construction page: https://www.lcmd.io/en/lean-construction
- Outbuild — product site and module map: https://www.outbuild.com/ ; Pull Planning page: https://www.outbuild.com/pull-planning-software/
- VisiLean — Planner page: https://visilean.com/planner ; Construction Management Solutions page: https://visilean.com/construction-management-solutions
- Methodology context: P2SL (UC Berkeley) — Last Planner System 2020 Benchmark (Ballard & Tommelein): https://p2sl.berkeley.edu/wp-content/uploads/2021/03/Ballard_Tommelein-2021-LPS-Benchmark-2020-2.pdf (linked from vPlanner's site; not fetched directly)

> Sourcing limitation: research relied on official product/marketing pages; vendor help-center depth was not fetched. Task and constraint state vocabularies, exact lifecycle transitions, permission models, and precise metric computation rules are therefore described generically, and no numeric limits, default windows, or thresholds are asserted. Detailed product-by-product observations are recorded in the paired Research Notes.
