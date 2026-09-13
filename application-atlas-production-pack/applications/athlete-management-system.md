# Athlete Management System

## Overview

An **Athlete Management System (AMS)** is organizational sports software used to manage the preparation and development of a defined population of athletes: it holds the roster, plans and assigns training work, collects what each athlete actually did and how they are responding, and gives the support staff one longitudinal view per athlete to review and adjust their preparation.

The defining core is small:

```text
Organizational athlete roster
└── Training/development program (planned, assigned, tracked work)
    └── Longitudinal per-athlete preparation record
        └── Staff review → adjust loop
```

Everything commonly associated with modern elite-sport platforms — athlete mobile apps, wellness questionnaires, wearable data pipelines, testing batteries, nutrition, medical modules, machine-learning risk models — is widespread in current products but is not what makes the product an AMS. A paper-era binder holding the squad roster, the season plan, and one file per athlete satisfies the same definition.

When the center of gravity shifts to documenting injuries and determining participation clearance, the product is drifting toward a different Application Type (Athlete Injury / Availability Management); when it shifts to insight dashboards over data collected elsewhere, it is drifting toward Sports Performance Analytics.

## Users & Context

The primary users are the **staff of an organized athletic program** — professional clubs, collegiate athletics departments, national federations and institutes, high schools, tactical units — who are collectively responsible for preparing a squad:

- **strength & conditioning / performance staff** — build and deliver training programs, monitor load and completion, adjust sessions based on readiness
- **coaches** — see athlete status and progress, align on-field practice with off-field preparation
- **sport scientists / performance managers** — configure metrics, build dashboards, analyze trends across athletes and seasons
- **athletes** — receive their programs and schedules, log completed work, report how they feel and respond

Depending on the product and tier, the same system also serves **medical staff** (injury and treatment records, return-to-play), **nutrition staff**, and program **administrators** (roster, roles, integrations). What distinguishes the context from personal training tools is the organizational container: many athletes, multiple specialist roles, one shared record per athlete.

## Core Model

### The Defining Core

```text
Organizational athlete roster
└── Training/development program (planned, assigned, tracked work)
    └── Longitudinal per-athlete preparation record
        └── Staff review → adjust loop
```

Three structures. If any one is removed, the product is no longer recognizable as an AMS:

- **Organizational athlete roster** — athletes exist as identified members of teams, squads, or groups managed in the system. Without this container there is no population to manage, and the product becomes an individual training app.
- **Training/development program as managed work** — the system plans, assigns, and tracks structured work (periodized programs, sessions, workouts, drills) for individual athletes and groups. Without this the product is a monitoring platform, an analytics dashboard, or a medical record.
- **Longitudinal per-athlete preparation record feeding a review/adjust loop** — data about each athlete's preparation and condition (completed work, athlete-reported status, testing and monitoring results) accumulates over time against the athlete, persists across sessions and seasons, and is surfaced to the staff who review it and adjust that athlete's preparation. Without the accumulating record, the product is a scheduling or communication tool.

### Standard Capabilities

A typical modern AMS carries most of these capabilities. They are not what makes the product an AMS, but they make it work in practice:

- **Athlete app** — athletes receive programs and schedules, log completed sessions, submit wellness and effort reports, and receive feedback
- **Athlete-reported status** — wellness, soreness/pain, and perceived-exertion questionnaires, often with configurable forms
- **Daily readiness view** — a per-athlete snapshot (workload, recovery, wellness) that shows staff who needs attention today
- **Prescribed-vs-completed comparison** — what was planned against what was actually done, as a core review mechanic
- **Testing and benchmarking** — performance test results, structured ratings, norms, and progress over time
- **Load and session monitoring** — training-load metrics collected from athletes, staff, and connected devices
- **Dashboards and reporting** — per-athlete and squad-level views, self-service report builders, multi-team comparisons
- **Calendar** — training, gym, recovery, and team activities in one shared schedule
- **Alerts** — signals on thresholds, status changes, or missed submissions
- **Roles and permissions** — organization, team, group, and role structures controlling who sees and does what
- **Integrations** — connections to wearables and performance technologies, plus APIs and exports
- **Development planning** — individual development plans and benchmarking against expectations

### One Structure, Many Implementations

The Core Model is written in conceptual terms. Specific products realize each concept differently:

```text
Concept:            Organizational roster
Implementations:    teams/squads/groups with role structures; rosters synced from
                    wider club-operations platforms; multi-team hierarchies for
                    federations and athletic departments

Concept:            Program as managed work
Implementations:    periodized program builders on calendar or dateless views;
                    session planners with drill libraries; practice scripts;
                    configurable forms used as program containers

Concept:            Preparation record
Implementations:    athlete-completed logs; wellness/RPE submissions; wearable and
                    device feeds; testing results; staff-entered observations

Concept:            Review surface
Implementations:    daily readiness boards; configurable dashboards; scheduled
                    reports; alert-driven queues
```

A reader who has only seen one implementation — for example an elite-club platform with wearable pipelines — should still be able to recognize a high-school strength program's simpler setup as the same Type from the Core Model.

## How It Works

### Set up the organization

```text
Create the program/organization
→ roster athletes into teams, squads, or groups
→ define staff roles and permissions
→ connect data sources (devices, forms, imports) where used
```

### Plan and assign the work

```text
Build training programs and sessions (from scratch, templates, or drill libraries)
→ schedule them on the calendar
→ assign to individual athletes or groups
→ publish to the athlete app / weight-room surface
```

### Execute and collect

```text
Athletes open their assigned session and log what they completed
→ athletes submit wellness / soreness / perceived-exertion reports
→ connected devices and integrations feed load and testing data
→ staff record observations and test results where collected manually
```

### Review and adjust

```text
Staff open the daily readiness view and squad dashboards
→ compare prescribed vs completed work and check athlete-reported status
→ flag athletes who need attention
→ adjust upcoming sessions, modify programs, or hand off to medical staff
→ communicate the change to the athlete
```

### Develop over the long term

```text
Testing results and preparation data accumulate on the athlete's record
→ staff review progress against benchmarks and development plans
→ season and multi-season reports inform next-cycle planning
```

The loop — plan → deliver → collect → review → adjust — is the defining workflow. Everything else in the product exists to serve one of its steps.

### Core vs Common vs Optional

**Defining core** — without these, not an AMS:

- organizational athlete roster
- training/development program planned, assigned, and tracked
- longitudinal per-athlete preparation record
- staff review → adjust loop

**Standard capabilities** — present in most modern products:

- athlete app; athlete-reported status; daily readiness view
- prescribed-vs-completed comparison; testing and benchmarking
- load/session monitoring; dashboards and reporting; calendar; alerts
- roles and permissions; integrations; development planning

**Common variants / optional** — depends on segment, tier, and deployment:

- medical/injury module (injury records, treatment, return-to-play, availability determination) — common in elite-tier platforms, absent in programming-first products
- nutrition management; wearable data pipelines as first-class ingestion
- machine-learning injury-risk prediction; concussion-specific protocol modules
- clinical/privacy compliance certifications (HIPAA, FERPA, GDPR, COPPA) for school and collegiate contexts
- no-code configurability of forms, workflows, and dashboards
- league/federation-wide standardization; growth-and-maturation adjustment for youth programs
- practice planning for sport coaches; gym/business management sold alongside

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Squad dashboard / daily readiness board

The staff's primary entry surface.

- per-athlete status indicators (readiness, recovery, wellness, availability), squad-level trends, flags
- primary actions: identify athletes needing attention, drill into an athlete, export or share a status summary

### Athlete profile

The longitudinal view of one athlete.

- preparation history (sessions, load, test results, submitted reports), current program, flags and notes
- primary actions: review progress, adjust program, record an observation, open related records (e.g., medical, where present)

### Program / session builder

Where staff author the work.

- periodized program views (calendar or dateless), exercise and drill libraries, session templates
- primary actions: build and edit programs, assign to athletes/groups, schedule, publish

### Forms / questionnaire builder

Where data collection is configured.

- custom forms for wellness, soreness, testing, and check-ins; delivery via mobile, web, or kiosk
- primary actions: create forms, schedule collection, review submissions

### Calendar

- training, gym, recovery, testing, and team activities in one shared schedule
- primary actions: schedule sessions and events, resolve conflicts, publish to athletes

### Reports / analytics

- per-athlete and group-level analysis: load trends, testing progress, prescribed-vs-completed, multi-team comparisons
- primary actions: build dashboards, generate reports, export data

### Athlete app

The athlete's surface.

- today's session and schedule, program history, wellness/effort submission, feedback from staff
- primary actions: log completion, submit reports, view schedule and profile

### Admin / settings

- roster and org structure, roles and permissions, integrations, data configuration

## Important Rules / Behaviors

### Role-based visibility, with a medical privacy wall where medical data exists

Access is organized by role and group. Where the medical module is present, a structural boundary separates restricted clinical detail from coach-facing summaries: performance and coaching staff see readiness and restrictions, not medical narrative. This privacy wall is a defining behavior of products that embed the medical slice.

### The record is longitudinal and durable

Preparation data persists across sessions and seasons. The athlete's file is a history, not a daily scratchpad — long-term development review depends on it. Records are edited with care and often retained for governance or compliance review.

### Prescribed vs completed is the core comparison

The system continuously holds two sides — the planned work and the executed work — and the review step is built on comparing them. Gaps between the two are primary signals for adjustment.

### Athlete-reported input is an input, not a verdict

Wellness and effort reports feed the readiness picture alongside objective data; they inform staff decisions but do not by themselves determine participation or program changes.

### Alerts depend on configured thresholds and submissions

Alert machinery (missed check-ins, threshold breaches, status changes) only works when collection is configured; a squad that does not submit reports produces an incomplete readiness picture. Staff workflows account for this.

### Availability has multiple sources

Where availability is surfaced, it can derive from medical status, staff decision, or scheduled absence; the system aggregates rather than owns a single source in products without the medical module.

## Variants

The AMS Type is implemented in several recognizable shapes:

- **standalone performance platform** — the AMS as the organization's central system, with configurable data collection and dashboards (e.g., Teamworks AMS, formerly Smartabase)
- **solution on a multi-solution platform** — the same concern packaged as one solution beside medical and development solutions on a shared platform (e.g., Kitman Labs' Performance Optimization on its Intelligence Platform)
- **programming-first with a readiness add-on** — a strength & conditioning programming tool at the core, with the readiness/monitoring layer sold as an add-on; common at the high-school and college tier (e.g., TeamBuildr Strength + AMS)
- **monitoring-first platforms** — wearable/load data as the center of gravity with injury tracking but no programming loop; adjacent to this Type and to Sports Performance Analytics (e.g., Catapult Athlete Monitoring)
- **federation / league deployments** — the same platform standardized across many clubs or a player pathway, with league-wide governance
- **school and tactical programs** — simpler configurations centered on strength programming and group training, often with student-privacy compliance postures

A variant remains a **Variant** unless it changes users, core objects, workflow, or rules so much that the Core Model no longer applies — as happens when the programming loop disappears entirely (monitoring platforms) or the preparation record is replaced by clinical documentation (sports-medicine EMRs).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Athlete Injury / Availability Management | embedded sibling | the medical-availability slice (injury records, treatment, return-to-play, participation clearance); usually ships inside elite-tier AMS products as a module. Remove the programming loop from an AMS and the remainder is this Type; remove injury/availability and an AMS still stands |
| Sports Performance Analytics | adjacent | insight layer over performance data; does not own program delivery or the managed roster. AMS products embed reporting and often sell analytics separately |
| Team Management Application | adjacent | team/event-centered (roster, schedule, communication for games and practices); no longitudinal preparation record or programming loop |
| Sports Coaching Platform | adjacent | centers on coach-led session delivery and skill development content; the AMS centers on the organization's management of athlete preparation across domains |
| AI Fitness Coach | different user model | individual trainee + system-composed programming; the AMS is organizational with staff-composed programming |
| School / College Athletics Management | adjacent | administrative department operations (eligibility, compliance, event operations); often sold as separate products from performance tools |
| Sports Eligibility Management | adjacent | administrative right to compete (registration, academic standing, licensing); different record types and decision owners from preparation management |
| Sports Video Analysis | complementary | technique and tactical video review; feeds the preparation picture but does not manage programming or the athlete record |

The most important boundary is with Athlete Injury / Availability Management: the two Types share the roster and the athlete-reported input layer, and in today's market the medical slice usually ships inside an AMS. The structural difference is what the system manages as work — preparation (programming, readiness, development) versus medical episodes (injury lifecycle, clearance).

## Representative Products

- Teamworks AMS (formerly Smartabase) — standalone configurable platform; collegiate, professional, Olympic, military
- Kitman Labs (iP: Performance Optimization) — enterprise platform solution; elite clubs, leagues, collegiate
- TeamBuildr (Strength + AMS add-on) — programming-first with readiness add-on; high schools, colleges, gyms, tactical
- Catapult (Athlete Monitoring) — monitoring-first boundary data point; elite teams

The Core Model was checked against the documentation-first medical pole (sports-medicine EMR products) and against paper-era and spreadsheet-era equivalents to avoid over-fitting to the modern elite-platform pattern.

## Sources

Research date: **2026-09-06**

- Teamworks — AMS: https://www.teamworks.com/ams/
- Kitman Labs — Performance Optimization: https://www.kitmanlabs.com/platform/performance-optimization/
- TeamBuildr: https://teambuildr.com/
- Catapult — Athlete Monitoring: https://www.catapult.com/solutions/athlete-monitoring
- Kitman Labs — Performance Medicine: https://www.kitmanlabs.com/platform/performance-medicine/
- Teamworks — Sports EMR: https://www.teamworks.com/sports-emr/
- Healthy Roster: https://www.healthyroster.com/

> Sourcing limitation: vendor help-center articles describing exact program-builder mechanics, readiness-indicator vocabularies, and role models were not reachable during research; those structures are described conceptually rather than as product-specific details. Two intended samples (an availability-first standalone product and a long-standing category vendor) were unreachable and were dropped; the monitoring-first boundary therefore relies on one sampled product plus vendor naming usage. Precise vendor claims (integration counts, report counts, pricing) are intentionally not stated in this document; they remain in the Research Notes.

Detailed evidence, product-by-product observations, cross-product comparison, and the joint boundary review with Athlete Injury / Availability Management are recorded in the paired Research Notes.
