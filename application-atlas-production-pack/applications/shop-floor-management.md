# Shop Floor Management

## Overview

A **Shop Floor Management** application is the shop floor's **daily management system**: software that holds the floor's performance picture as managed board content, structures the recurring tiered meeting rhythm in which that picture is reviewed, and runs the loop that turns the floor's problems into assigned, tracked, completed actions.

Its defining structure is small — three things, held together:

```text
The floor's performance picture (board content)
  │  reviewed at
The tiered management rhythm (recurring meetings, level by level)
  │  which feeds
The issue → escalation → action loop (problems become tracked actions)
```

Remove the performance picture and only generic meetings-and-tasks tooling remains. Remove the rhythm and only a dashboard remains. Remove the issue-to-action loop and performance review becomes theater with no consequence machinery.

Everything else commonly associated with these products — leader standard work, gemba walks, audits, shift handovers, continuous-improvement pipelines, management analytics, mobile capture, multi-site rollups — is widespread in current products but is standard or optional capability built on that core. The practice predates all of it: a wall-mounted performance board, a daily tier meeting, and issues escalated up the management chain with owners and dates satisfy the same definition.

The term "shop floor" is used loosely across manufacturing software. Products that **execute** the floor's production work — dispatching tasks, enforcing routings, producing as-built records — call themselves shop-floor execution or MES and belong to neighboring Types. Shop Floor Management is the different, complementary thing: the **management routine** over the floor.

## Users & Context

The primary users are the **people who manage the floor**, not the machines or the orders:

- **Team leaders and supervisors** — run the first-tier huddle at the line, keep the board current, raise and record issues, own first-line actions.
- **Production, department, and site managers** — attend second- and third-tier meetings, receive escalations, decide and sponsor actions beyond the team's reach.
- **Continuous improvement / operational excellence staff** — structure the routines, run problem-solving, track improvement projects and audit programs.

Secondary users:

- **Support functions** (maintenance, quality, engineering, HR) — act on escalated issues and actions routed to them from the floor.
- **Operators and frontline workers** — raise problems at the source, contribute improvement ideas, and see the board that carries their area's performance.
- **Plant or multi-site leadership** — consume the rollup: which areas are in control, which issues are aging, how the management system itself is functioning.

The work context is the **floor itself and the management day around it**: boards at the line or in team corners, short standing huddles at shift start, tier meetings following one another up the organization on a fixed cadence, and managers walking the floor with checklists between meetings. Deployments range from a single plant to global multi-site programs that standardize one routine across many factories — and, in some products, beyond factories entirely (the same routine serves healthcare and similar frontline operations).

## Core Model

### The defining core

**1. The floor's performance picture as managed board content.** The application holds, for each area or line, a persistent visual board of the floor's key performance indicators — most commonly organized around safety, quality, cost, delivery, and people (the exact vocabulary varies: SQCDP, SQDCME, QCDSM-class schemes are all realizations of the same idea). The board is **review-facing content**, not an analytics engine: figures may be entered by hand, imported from production systems, or fed by integrations, but what makes it this Type's object is that it is the standing agenda of the management routine. The board carries the day's or shift's actuals against targets, the state of open issues, and the status of actions.

**2. The recurring tiered management rhythm.** The application structures the meetings in which the boards are reviewed: short recurring huddles at team level, then department level, then site level — "tiers" in the common vocabulary — each with a defined agenda drawn from the board, a defined time, and a defined membership. The rhythm is the mechanism by which information and problems move **up the management structure**: what a team cannot resolve at its huddle escalates to the next tier's meeting. Mature products model the tiers, the cadences, the agendas, and the attendees explicitly, so the escalation path is a property of the system rather than a habit.

**3. The issue-to-action escalation loop.** Problems surfaced on the floor — during meetings, walks, checks, audits, or directly at the line — are documented as **issues**: categorized, prioritized, owned. An issue is either resolved at the level that raised it or **escalated** to the management level that can resolve it, carrying its context. Resolution is expressed as **actions**: assigned to a named owner, given a deadline, tracked to recorded closure. Corrective and preventive actions, containment steps, and improvement actions all ride this same machinery. The loop closes when outcomes update the board — and recur when the same problem shows up again, which is what makes the record worth keeping.

The three are load-bearing together: a picture without a rhythm is a dashboard; a rhythm without a loop is a meeting schedule; a loop without a picture is a generic task tracker. Only the combination — the floor's picture, reviewed on a tier rhythm, driving issues to closed actions — is the daily management system.

### Standard capabilities of mature products

These are common in current products but do not define the Type; the paper-era practice satisfies the core without any of them:

- **Leader standard work** — standardized schedules of the managers' own recurring work: daily checks, data logs, audits, meetings, handovers, reviews, with reminders and adherence visible.
- **Gemba walks and rounds** — structured walkthrough checklists that turn a manager's floor time into observations, captured issues, and improvement ideas.
- **Audits and inspections** — 5S checks, layered process audits, safety and quality rounds as scheduled forms whose answers can require photos, notes, or corrective actions.
- **Shift handovers** — structured exchange of open issues, risks, and priorities between shifts.
- **Structured problem-solving** — categorization and prioritization of issues, root-cause methods, corrective-and-preventive-action handling with due dates.
- **Continuous improvement** — idea capture, kaizen-type projects, and improvement portfolios tracked alongside daily issues.
- **Management analytics** — closure rates, aging of open issues, meeting and routine adherence, issue trends by area — measurement of the management system itself, not just the floor.
- **Mobile capture and live boards** — phones and tablets at the point of work; boards projected in meeting rooms and displayed on the floor.
- **Multi-site rollup** — the same routine standardized across plants, with cross-site comparison of both floor performance and management behavior.
- **Integrations** — board content drawn from production, quality, and enterprise systems (MES, ERP, BI platforms) rather than keyed in by hand.

### One structure, many implementations

```text
Concept:  the floor's performance picture
Realizations:  hand-entered daily figures, imported KPI feeds,
               connected production data; SQCDP / SQDCME / QCDSM board vocabularies

Concept:  the tiered rhythm
Realizations:  named tier ladders (Tier 1/2/3 is common, depth varies),
               huddle agendas, meeting calendars, digital "rooms" mirroring
               the organization

Concept:  the issue and the action
Realizations:  issue cards with category/priority/owner, escalation states,
               corrective-and-preventive actions, improvement ideas and projects

Concept:  the manager routine
Realizations:  leader-standard-work schedules, gemba-walk checklists,
               audit forms, handover notes
```

A reader who has only seen one implementation should still recognize the others: the practice is the constant, the substrate is not.

## How It Works

### Set up the management system

Deployment is an act of **designing the routine**: define areas and lines; define the tier structure and who attends which meeting; lay out the board (which indicators, which targets, which issue and action columns); define the KPI vocabulary and where each number comes from; load the recurring routines — walks, checks, audits, handovers — into managers' calendars. Because the product's subject is management behavior, configuration is closer to installing a management operating rhythm than to commissioning a machine connection.

### The daily loop

```text
Before the shift
→ the board is made current (figures entered, imported, or connected)
→ open issues and actions from yesterday are visible

Tier 1 huddle (team, at the line, short)
→ review the board column by column
→ raise today's problems as issues
→ resolve locally what the team can; the rest is flagged for escalation

Tier 2 (department) and Tier 3 (site) meetings follow on their cadence
→ escalated issues arrive with their context
→ decisions and support actions are made at the level that owns them
→ unresolved issues continue upward; commitments return downward

Through the day
→ issues are worked; actions get owners and deadlines
→ walks, checks, and audits surface new issues at the source

To closure
→ actions are completed and closed with a recorded outcome
→ the board, the issue list, and the history all update
→ the next huddle starts from a current picture
```

### Capture at the gemba

Between meetings, the routine generates its own inputs: a manager's walk records an observation with a photo; an audit answer triggers a corrective action; an operator reports a recurring nuisance. The capture is deliberately lightweight — structured forms and checklists rather than free-text reports — because the value of the record depends on issues being categorized and comparable.

### Escalate and resolve

Escalation is the system's central behavior. An issue that exceeds its level's authority, resources, or deadline moves up with its history — what it is, where it came from, what has been tried, what it is costing. The receiving tier either acts (assigns an owner, commits resources, changes the standard) or escalates further. Everything that comes back down arrives as a tracked action. Escalation "de-escalation" is part of the same machinery: a solved or downgraded issue returns to its origin with the outcome recorded.

### Measure and improve the management system itself

Because issues, actions, meetings, and routines are all recorded, the application can measure the **management process**: how many issues were raised and how many closed, how fast, at which tier, which areas escalate the most, whether walks and audits happened as scheduled. Management and improvement staff use this to coach leaders and to tune the routine — the Type's improvement loop points at the management system, not only at the floor's machines.

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Visual management board

The center of gravity — the digital form of the wall board.

- indicator columns (safety, quality, cost, delivery, people) with actuals against targets for the current period; open-issue and open-action counts; color-coded status
- primary actions: update figures, add an issue, review the day, project the board during the huddle

### Meeting / huddle surface

The surface the tier meeting runs on.

- the board as agenda, the attendee list, the meeting calendar, notes and decisions
- primary actions: run through the agenda, raise issues from the board, escalate to the next tier, record decisions

### Issue detail and action tracker

The loop's working surface.

- issue record: what, where, when, category, priority, current level, history of escalation; attached photos and documents
- actions: owner, deadline, status, outcome; corrective/preventive classification where used
- primary actions: document, categorize, prioritize, assign, escalate, close

### Manager routine calendar

The leader-standard-work surface.

- each manager's daily/weekly/monthly recurring duties — checks, walks, audits, meetings, handovers — with completion state and reminders
- primary actions: complete a routine, record its findings, review adherence

### Walk / audit forms

Mobile checklists for the floor.

- question sets with photos, notes, and automatic corrective-action triggers on failed answers
- primary actions: run a walk or audit, record findings, raise issues, assign actions

### Management analytics

The layer over the record.

- issue and action trends, closure and aging statistics, escalation flows, routine and meeting adherence, cross-area and cross-site comparison
- primary actions: filter, compare, drill into issues, export

### Configuration

Where the routine is defined.

- organizational structure and tiers, board layouts and KPI definitions, meeting cadences and agendas, form and checklist builders, roles and permissions, integrations to production data sources

## Important Rules / Behaviors

### Escalation is structural, not informal

The defining behavior of the Type: an issue does not quietly die at the level where it was raised. It is either resolved there or moved up with its context to the tier whose authority matches it — and the movement itself is recorded. Products implement this as first-class escalation states on the issue, tied to the tier structure.

### The board is the agenda

The performance picture and the meeting rhythm are one artifact, not two: the huddle walks the board, and the board is updated as a result of the huddle. This coupling is what distinguishes the Type from a dashboard plus a calendar.

### Actions have owners and deadlines

An escalated problem resolves into named commitments. Open actions without owners, and "closed" actions without recorded outcomes, are exactly what the system is built to make visible. Management analytics depend on this discipline.

### The performance picture is review content, not live telemetry

The routine does not depend on machine connectivity. Figures can be entered by hand, imported on a cadence, or fed live; deployments at the paper-inspired end of the market run the full routine on manually updated boards. Honest labeling of where each number came from is part of the operating model.

### The routine itself is standardized and measured

Mature deployments run the same meeting structure, board layout, and routines across shifts, departments, and sites — and treat adherence to the routine (meetings held, walks done, actions closed on time) as data. The management system is itself an object of improvement.

### Management items, not production postings

Issues, actions, and improvement items are not inventory movements, capacity entries, or production postings, and the application does not maintain them as such. Where execution or financial recording is needed, it happens in the neighboring systems the routine connects to.

## Variants

- **Manufacturing core and frontline extensions** — the practice is centered on the shop floor; some products extend the same routine to non-manufacturing frontline operations (healthcare, logistics, service sites) without structural change.
- **Routine-first vs canvas-first products** — one family models the routine explicitly (cadences, forms, standard-work schedules); another starts from visual boards and "rooms" that mirror the organization and hangs meetings, escalation, and actions off the canvas. Same core, different center of gravity in the interface.
- **Site-level daily management vs enterprise programs** — single-plant deployments versus multi-site standardization programs that roll one routine across dozens of factories, with rollup dashboards and cross-plant comparison.
- **Board vocabulary and tier depth** — SQCDP/SQDCME/QCDSM-class indicator schemes and tier ladders differ by organization; the structure (picture + rhythm + loop) does not.
- **Data posture** — hand-entered boards, integration-fed boards, or a mix; products differ in how much production data they consume directly versus receive through exports and integrations.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Manufacturing Execution System / MES | adjacent sibling, frequently connected | MES executes released production orders at operation grain against the defined process and produces the as-built record. Shop Floor Management runs the management routine — no order execution, no genealogy, no process enforcement. Products in the execution family call themselves shop-floor execution or MES, not shop floor management |
| Factory Operations Management | closest large sibling | holds the live production-operations picture (machine/line/order state), routes events to response functions (maintenance, quality, materials), and keeps the operational performance record. Shop Floor Management holds the management routine over the floor: boards are review content rather than live state, and escalation runs up management tiers rather than out to response functions. Operations-management systems are natural data sources for the boards |
| OEE Management Platform | shares board content | centers the equipment-effectiveness measure and its loss-analysis loop. An effectiveness score can appear on a management board as content; the management routine can exist with no computed effectiveness score at all |
| Production Planning / APS | upstream | owns the plan pipeline (requirements, schedules, order release). The floor's plan and targets appear on the management board as content; no schedule is generated here |
| Manufacturing ERP | upstream system of record | owns orders, materials, costing, and business-grain production recording. Management actions are not financial or inventory postings |
| CMMS / EAM | adjacent | maintenance appears as a frequent action target for escalated issues, but asset care and work-order management live there, not here |
| Manufacturing QMS / CAPA Management | adjacent | formal quality records and CAPA systems overlap with the corrective-action machinery; the management routine, boards, and tier structure are the differentiator, and quality events raised here can feed a QMS |
| Task Management Application / Work Management Platform | the generic-tooling boundary | tasks, meetings, and trackers without the floor-performance binding (SQCDP-class board content, tier structure, gemba and audit routines) are generic work management. The domain binding plus the performance picture is what makes this a separate Type |
| Digital Whiteboard | superficial resemblance | canvas-style boards may look alike; a whiteboard has no tiered management rhythm, no performance-of-record binding, and no escalation semantics |

The sharpest boundary in practice is with Factory Operations Management, because both manage "what happens on the floor." The structural test: remove the live production state and function-routed response — what remains is the management routine (this Type). Remove the tiered routine and the board-as-agenda — what remains is operations management.

## Representative Products

- **Tervene** — daily-management and shop-floor-management suite: leader standard work, gemba walks, tiered meetings, issue and action management, SQCDP-class boards (self-labels "Shop Floor Management System (SFM)" software)
- **iObeya** — digital Obeya platform for operational excellence: tiered digital rooms, SQCDP digitization, visual management, escalation and action tracking (self-labels Daily Management System / Operational Excellence)

These two were sampled as the Type's defining evidence, chosen for different product philosophies (routine-first and canvas-first) and different customer scales. The boundary seams were checked against products from the execution neighborhood — a shop-floor-execution platform, a discrete-manufacturing MES, and a frontline-platform vendor's documentation — all recorded in the paired Research Notes.

## Sources

Research date: **2026-09-09**

- Tervene — home: https://tervene.com/
- Tervene — "Digital Shop Floor Management Software": https://tervene.com/solution/shop-floor-management-software/
- iObeya — home (positioning, Lean Manufacturing use case, FAQ, customer reviews): https://www.iobeya.com/
- L2L — "Shop Floor Execution" (boundary evidence, execution family): https://www.l2l.com/platform/shop-floor-execution
- ShopVue MES (CAI Software) — product page (boundary evidence, MES family): https://caisoft.com/products/shopvue-mes/
- Tulip — "Shop floor management" support doc (label-usage evidence): https://support.tulip.co/docs/shop-floor-management

> Sourcing limitations: a third management-side candidate (Factory Operating System) was unreachable (transport failures), and a small-shop execution-side candidate's documentation could not be retrieved, so cross-product claims on the management side rest on two independent product confirmations and are worded accordingly. Depth beyond product pages and official marketing/support surfaces (help-center articles, use-case pages) was not reached for all sampled products; no numeric limits, cadences, or defaults are asserted in this document. Vendor outcome metrics in marketing materials were excluded. Detailed observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
