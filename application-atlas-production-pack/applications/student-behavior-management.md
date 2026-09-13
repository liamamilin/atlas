# Student Behavior Management

## Overview

A **Student Behavior Management** application is a school's conduct system of record. It holds the school's own behavior framework — a defined vocabulary of behaviors with their weights and consequences — records conduct events against identified students as staff observe them, drives a recorded response to every event (recognition points, administrative actions, sanctions), and turns the accumulated record into per-student behavior histories and school-wide patterns that staff use to follow up, intervene early, and measure the school's behavior program.

The defining core is small:

```text
School's conduct framework (one framework for the whole school)
└── Behavior event of record (staff-recorded, per-student, classified)
    └── Recorded response (points / administrative action / sanction)
        └── Accumulating student behavior history
            └── Review: per-student and school-wide patterns for decisions
```

Everything else commonly associated with these products — points economies with rewards stores, parent apps, hall passes, house systems, detention scheduling, mobile awarding — is widespread in current products but is not what makes the product a behavior management system. An incident-and-report system without any of those specifics (the oldest products in this market are built exactly that way) is still fully this Type.

The scope is school-wide by definition. When conduct recording lives inside a single teacher's per-class tool with no school-wide framework or administrative loop, the product belongs to Classroom Management instead. When the system merely stores discipline entries in the student's official record for year-end reporting, it is acting as a Student Information System, not a behavior management application.

## Users & Context

Primary users:

- **Teachers and staff** — record conduct events in the moment, wherever they happen: classroom, hallway, cafeteria, bus. Recording must take seconds; these products are judged on it.
- **Administrators (deans, assistant principals, behavior leads)** — receive referred incidents, decide and record the response (consequences, sanctions, parent contact), oversee the school's conduct data.

Secondary users:

- **Behavior program leads / PBIS or MTSS teams** — read school-wide patterns, monitor staff consistency and program fidelity, target interventions.
- **Families** — receive notifications of events, detentions, and resolutions; visibility is school-configured.
- **Students** — in many products, see their own points, history, and scheduled detentions through a student view.

The work environment is the whole school day. Events are recorded from desktop browsers, mobile phones, and tablets; badge or QR scanning is common where students carry IDs. The rhythm is daily (events recorded as behavior happens), weekly (detention sessions, pattern reviews), and annual (data summarized and handed to official reporting; in some systems point totals reset between years while the history is retained).

## Core Model

### The behavior event

The unit of record is the **behavior event**: a persistent, individually recorded conduct event bound to one or more identified students, attributed to the staff member who recorded it, stamped with a time and usually a place and activity context, and classified against the school's behavior vocabulary. Events carry an optional comment, whose visibility to students and families is separately controlled. An event may involve multiple students in different roles — for example, an incident form can record one student's role as the aggressor and others as witnesses, with different point values per student.

Events come in two broad kinds, and most products carry both:

- **Recognition events** — positive conduct recorded against the school's expectations, usually awarding points.
- **Incident events** — negative conduct or rule violations, usually costing points and/or triggering a response.

### The school's conduct framework

The framework is what the school configures before the system records anything, and it is what makes the record mean the same thing in every classroom:

- **The behavior taxonomy** — the school's list of behaviors or reasons (its expectations on the positive side; its infractions on the negative side), each commonly carrying a default point value. Products differ in how much is pre-standardized versus school-authored, but in every case the school's own list — not an individual teacher's — defines what can be recorded.
- **The consequence structure** — the responses events can call for: administrative actions (consequences assigned by administrators), sanctions such as detentions, and the escalation patterns that connect repeated behavior to stronger responses.
- **Guardrails and automation** — some systems add consistency machinery: limits guiding how many points a staff member may assign per period, and rules that watch the event stream for patterns (a given behavior repeated so often within so many days) and surface a recommended follow-up for staff to act on.

### The response

Every event can drive a recorded response, and the response attaches back to the event and the student's history:

- **Points** — awarded or deducted, accumulating on the student's record. In points-economy products the balance is spendable (rewards stores, events); in incident-focused products points may be absent entirely.
- **Administrative action** — for referred incidents, an administrator reviews and records the action taken (a consequence, a restorative task, parent contact). The referring teacher can see the outcome — the loop closes visibly.
- **Sanctions** — scheduled consequences, most commonly detentions: a dated, located session with a supervising teacher, a student roster, and an attendance register that records who served, who was excused, and who did not attend.

### The student's behavior history

The accumulating per-student record is the system's memory: every event and response, retained across years, viewable as a profile with totals, patterns, and most frequent reasons. This history is what administrators open before a meeting with a family, what program leads slice into school-wide reports, and what feeds official discipline reporting through the student information system.

### Review surfaces

The record is consumed at three grains: the **student** (history, statistics, scheduled sanctions), the **group** (a class's or grade's conduct picture), and the **school** (trends over time, comparisons across staff and locations, demographic and equity breakdowns showing how discipline is experienced by different student groups). Review is not an afterthought — in the incident-of-record tradition it is the product's center: the data exists so teams can make decisions about support.

## How It Works

### Configure the framework (once, then maintained)

```text
Define behaviors/reasons (+ point values, + positive/negative kind)
→ define consequences and sanction types (e.g., detention types)
→ set escalation rules (behavior patterns → recommended follow-up)
→ set visibility policy (what families/students see)
→ set staff permissions (who may record what, see what)
→ connect the roster (sync from the SIS/MIS)
```

### Record events (the daily loop)

```text
Staff member opens the recording surface (roster, search, or badge scan)
→ selects student(s)
→ picks the behavior/reason from the school's list
→ adds context (location, activity, comment) and confirms
→ points awarded/deducted; event stored on the student's record
→ family notification sent (where enabled)
```

Recording is deliberately fast — a few seconds, not a trip to the office — because it happens during instruction, in hallways, and at events, not at a desk.

### Respond and close the loop

```text
Minor/negative event → points, maybe a direct sanction
Serious or repeated event → referral submitted
→ office/administrators notified immediately
→ administrator reviews, records the action taken
→ sanction scheduled if needed (e.g., detention session with register)
→ referring staff see the outcome; family notified per policy
→ incident marked resolved
```

Escalation rules watch the stream in the background: when a student's events match a defined pattern (same behavior, enough occurrences, within a window), a recommended follow-up appears on an administrative dashboard for staff to review and act on. Automation recommends; staff decide.

### Review and intervene

```text
Per-student history → conversations with students/families
Class and grade views → coaching and consistency checks
School-wide reports → program measurement, equity analysis
Patterns identified → interventions (e.g., structured check-in programs)
→ intervention progress tracked against the same record
```

### The annual rhythm

At year end the accumulated data is summarized — for the school's own review and, through the student information system, for official discipline reporting. In some systems point totals reset for a fresh start while the historical record is retained.

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Recording surface (staff)

The workhorse. A roster or searchable student list — often with badge scanning — where staff select students, pick a behavior from the school's list, add optional context, and confirm. Designed for use standing up, mid-lesson, or on playground duty. Group awarding (a whole class at once) and deferred entry (logging after class) are common.

### Behavior overview / incident list

The school-wide ledger: all events (and referred incidents) over a chosen date range, filterable by student, type, status, year group, or location. Each entry shows who recorded it, when, why, the points, and its current state. Primary actions: view, edit, delete (with care), and record new events.

### Student behavior profile

One student's full conduct picture: totals and statistics, most frequent reasons, badges earned, scheduled detentions, and the complete event list with each response recorded. The surface administrators and counselors open before any conversation about a student.

### Administrative queue / sanctions dashboard

The administrator's worklist: referred incidents awaiting review (with assign-to and status), recommended follow-ups surfaced by escalation rules, and the tools to record actions, schedule sanctions, and resolve incidents. In some systems, resolution is what unlocks family visibility.

### Sanction management (e.g., detentions)

Scheduling and running consequences: detention types defined by the school, sessions with date/time/location/supervising teacher, student rosters, an attendance register (attended / excused / absent), and rescheduling for students who miss with cause. Family notifications carry the details.

### Reports and insights

School-wide analytics: trends over time, breakdowns by behavior, location, time of day, and staff; demographic and equity views showing referral and sanction rates across student groups; staff-consistency and program-fidelity views; exports for district and official reporting.

### Family and student views

Notifications and read-only views of the student's conduct record — points, events, detentions — governed by the school's visibility policy. Common postures include positive-only visibility, staff-only visibility, and hiding referred incidents until resolved.

### Setup and configuration

The framework editor: behaviors/reasons and point values, badges, consequence and detention types, escalation rules, consistency limits, visibility policy, and the permission model. Permission models in this Type are notably fine-grained — typically distinguishing "events I recorded" from "all events" per action.

## Important Rules / Behaviors

### One framework, one record

The school's framework applies to every classroom and staff member. This is the structural difference between a behavior management system and a collection of teacher tools: the same behavior means the same thing, and carries the same weight, everywhere in the school. Consistency — not any single feature — is what the products sell and what schools buy.

### Events are attributed and governed

Every event carries its reporter. Editing and deletion are permission-gated, and mature products distinguish sharply between what a staff member may do with their own events versus all events. The record is treated as an institutional record, not a personal notebook.

### Visibility is a policy, not a default

What families and students see is configured: which events, which comments, whether negative events appear at all, and whether referred incidents appear before or only after resolution. The same record supports very different transparency postures, and products treat this as a first-class configuration surface rather than an afterthought.

### Automation recommends; people decide

Where products watch for behavior patterns and propose follow-ups, the recommendation lands on a staff dashboard for review — the consequence is recorded by a person. This keeps accountability with the school rather than the algorithm.

### The loop closes visibly

A referral is not done when it is submitted. In mature implementations the referring staff member can see the administrative response; the family is notified per policy; the incident reaches a resolved state. This closed loop — record → respond → confirm — is the operational heart of the Type.

### Points are a layer, not the foundation

In points-economy products, whether negative events subtract from spendable balances is itself a school decision, and the oldest products in this market have no points at all. The event record and the response loop exist independently of any token economy.

### The record feeds official reporting

Discipline data ultimately flows into the student information system for year-end and official reporting. Behavior management products either integrate with the SIS for this handoff or, in module form, live inside it — but the decision-support loop (real-time patterns, program measurement) is what distinguishes the Type from plain discipline storage.

## Variants

- **Incident-of-record systems** — office discipline referrals, standardized classifications, action taken, and school-wide reporting; no points economy. The academic/nonprofit tradition, and the oldest shape of the Type.
- **Points-economy platforms** — school-wide recognition systems with rewards stores, events, and house competitions as the visible surface, with incident/referral machinery beside them. The dominant commercial shape in the US market.
- **Whole-school platform modules** — behavior management as one module of a broader school platform (homework, attendance, timetabling), commonly with the deepest sanction machinery (detention administration, escalation rules) and national MIS integration.
- **SIS-suite behavior modules** — the same loop packaged inside a student information system; strongest where official discipline reporting drives the requirement.
- **Program framings** — implementations aligned to a named framework (PBIS/MTSS/SEL in the US; plain behaviour/discipline in the UK; restorative-practice framings), which change vocabulary and reports more than structure.
- **Intervention-depth variants** — products adding structured support tracking (check-in/check-out programs, individual support plans) for students needing more than classroom-level response; the deepest forms overlap the special-education machinery's inputs.
- **Scale variants** — single-school deployments through district and multi-school roll-ups with consolidated reporting.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Classroom Management | adjacent; the closest seam | governs the live classroom — in-the-moment direction (device/screen control, seating, timers) and per-class conduct recording with the teacher's own categories. Student Behavior Management is school-wide: one framework, one central record, an administrative response loop. The seam runs through products that carry both as separate modules. |
| Student Information System / SIS | substrate + downstream | owns the student population and the official record; stores discipline data for year-end/official reporting. Behavior management runs the real-time conduct loop on top of the SIS's roster and hands data back. An SIS behavior module is this Type's loop in packaged form. |
| Student Case Management | adjacent | issue-driven casework for individual students with an assigned, ongoing responsible party. Behavior incidents are closed by administrative resolution, not caseloads; repeated incidents may refer into case or intervention processes. |
| Special Education Management | consumer of this Type's data | owns the regulated intervention process (evaluation, eligibility, plans, compliance). Behavior events may inform it; the conduct loop itself has no eligibility gate or mandated plan. |
| Student Attendance System | sibling loop | records presence; behavior records conduct. Tardy/attendance features bundled into behavior products are adjacent machinery, not the conduct loop. |
| School Counseling Management | adjacent | counselor caseloads, appointments, notes, and support plans. Counselors consume behavior data; the objects and loops differ. |
| Parent Portal | capability, not a Type | the family-facing visibility of behavior records is one surface of this Type (and of the SIS), not a standalone system. |

The boundary with **Classroom Management** is the most important one, because both Types record student conduct with points. The structural test: is the conduct framework school-defined and school-wide, with a central record and an administrative response loop (this Type), or per-classroom and teacher-owned, inside a live-classroom tool (Classroom Management)?

## Representative Products

- **SWIS (School-Wide Information System)** — PBISApps, University of Oregon — the incident-of-record pole; office discipline referral data for school-wide decision making
- **SchoolMint Hero** — SchoolMint — behavior + attendance suite; PBIS/MTSS/SEL/RTI framework support
- **PBIS Rewards** — Navigate360 — schoolwide PBIS points economy with an add-on behavior referral system
- **LiveSchool** — LiveSchool — teacher-first school-wide points platform with rewards store and houses
- **Satchel One (Behaviour)** — Team Satchel — UK whole-school platform module; behaviour points, referred incidents, detentions, escalation rules; MIS-integrated

The defining core was checked against the oldest sampled product (a 25-year-old incident-of-record system) and against paper-era practice (referral forms, demerit ledgers, detention slips) to avoid over-fitting the definition to the modern points-app pattern.

## Sources

Research date: **2026-09-09**

- PBISApps — SWIS product page: https://www.pbisapps.org/products/swis (plus site root and referral-entry resource page)
- SchoolMint — Hero product page: https://schoolmint.com/hero
- PBIS Rewards (Navigate360) — product root, How It Works, and Behavior Referral System pages: https://www.pbisrewards.com/ , https://www.pbisrewards.com/how-it-works/ , https://www.pbisrewards.com/features/behavior-referral-system/
- LiveSchool — product root and Behavior Tracking feature page: https://www.whyliveschool.com/ , https://www.whyliveschool.com/features/behavior-tracking
- Satchel One Help Centre — Behaviour events and badges; Referred Incidents; Detentions; Thresholds setup; Sanction rule setup: https://help.satchelone.com/en/articles/11095655 , https://help.satchelone.com/en/articles/4934555 , https://help.satchelone.com/en/articles/11504031 , https://help.satchelone.com/en/articles/11524365 , https://help.satchelone.com/en/articles/11136811

> Sourcing limitation: the SchoolMint help center was not reachable from the research environment (JavaScript-gated); all statements about that product are positioning- and feature-surface-level, and no operational details (workflows, field lists, numeric limits) are asserted for it. Precise operational specifics for other products (exact report counts, permission names, attendance-code vocabularies, rule timeframes) are retained in the paired Research Notes rather than asserted as Type-wide facts.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
