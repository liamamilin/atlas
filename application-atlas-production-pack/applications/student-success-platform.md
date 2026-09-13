# Student Success Platform

## Overview

A **Student Success Platform** is an institution-side application — used mainly in higher education — that operates student success and retention as a managed, measurable program. It holds the institution's enrolled students as addressable records enriched with success context, surfaces early signals about students who may be drifting off-track, coordinates staff outreach and support across offices until each concern is resolved, and tracks persistence and retention outcomes so the institution can see what worked and for whom.

The problem it exists to solve is structural: in most institutions the data needed to see a struggling student lives in several systems, the staff able to help that student sit in several offices, and nobody owns the follow-through. A student success platform joins these pieces — one picture of each student, early warning before departure, coordinated action, and measured outcomes.

The defining core has four parts that only work together:

```text
Enrolled-student population of record (individual + cohort grain)
    ↓ watched by
Proactive success signals (alerts, progress reports, risk indicators)
    ↓ converted into
Coordinated intervention loop (routed, assigned, tracked to resolution)
    ↓ rolled up into
Success-outcome measurement (retention, persistence, initiative impact)
```

Everything else commonly associated with the category — predictive machine-learning models, outreach campaigns, advising appointments, student mobile apps, wellbeing pulse checks — is widespread in current products but is an instrument inside this loop, not what makes the product a student success platform. A paper-era retention office with early-alert referral forms, caseload cards, and term-to-term persistence tallies ran the same four-part operation without any of the modern machinery.

## Users & Context

**Primary users — the institution's success network.** The software's working users are staff, spanning more than one office; the multi-office span is part of the Type:

- **Advisors and success coaches** — carry caseloads, work the alert queue, meet students, record what happened
- **Faculty** — raise early alerts and file progress reports from the classroom side; some also receive referrals
- **Student-affairs and support offices** — tutoring, career services, counseling, financial aid, housing: each receives routed concerns and records the support it delivered
- **Retention and student-success leadership** — watches population health, sets up campaigns and programs, answers to the institution for outcomes

**Secondary users:**

- **Institutional leaders and analysts** — consume dashboards, measure initiative effectiveness, feed institutional reporting
- **Students** — use a companion surface (app or portal) to book appointments, complete tasks, view their plan, and sometimes raise concerns themselves; students are served by the platform, not its operators

**Context.** The work runs on the academic-term rhythm: signals spike at term start and mid-term, intervention caseloads rise and drain, and persistence is judged at term and year boundaries. The platform presupposes surrounding systems — the student information system (the official record and main data source), the learning management system (course engagement), and communication channels — and assembles their data rather than replacing them. Data governance obligations around student records (such as FERPA in the United States) shape who may see what.

## Core Model

### The student population of record

The platform's foundation is the enrolled student held as a persistent, individually addressable record — not a contact entry, but a working file that accumulates success context over the student's time at the institution: academic standing and program drawn from the SIS, course engagement drawn from the LMS, support interactions, alerts raised and resolved, notes from staff conversations. The record persists across terms; the platform's job is explicitly to keep students *from term to term*, so the record spans enrollment periods.

Crucially, the population is operated at **two grains at once**:

- **Individual grain** — one student's profile, history, and open concerns
- **Population grain** — cohorts and segments (first-year students, a program, a risk group) viewed as a whole, because much of the work — campaigns, program reviews, resource decisions — happens at population scale

Neither grain alone is the Type: individual-only collapses toward advising or casework tools; population-only collapses toward institutional research reporting.

### Success signals

A success signal is information that a student may be off-track, reaching staff **without the student having to ask for help**. Signals originate in several ways, and the mechanism is a matter of product and institution choice rather than definition:

- **Faculty-raised alerts** — an instructor flags a student for missed attendance, failing work, or apparent personal difficulty
- **Progress reports** — structured periodic faculty reporting on a class section, from which concerns are extracted
- **Rules-based flags** — configured thresholds (missed deadlines, registration gaps, unpaid balances) that trip automatically
- **Computed risk indicators** — from engagement data, or from predictive models trained on the institution's own history to estimate persistence likelihood

Signals arrive in a shared queue tied to the student's record. What makes them definitional is their *direction*: the platform watches and reaches out, in contrast to tools where work begins only when a student requests a service.

### The intervention loop

Every signal must become work, and the work must be attributable. The recurring objects:

- **Alert / concern** — the raised signal, with source, reason, and student attached
- **Assignment / routing** — a staff member or office takes ownership; institutions configure who handles what
- **Outreach and interaction** — messages, calls, appointments, meetings; each documented on the student's record
- **Tasks and to-dos** — for staff (follow up, check eligibility) and for students (complete a form, meet an advisor)
- **Notes** — shared across the network with access controls, so the next office sees what the last one did
- **Referrals** — a concern passed to a specialist office, with follow-up tracked until the receiving side responds
- **Resolution** — the concern is closed with a recorded outcome; the student's history shows what happened

At population scale the same loop runs as **campaigns**: a defined group receives coordinated outreach (commonly by email or text), and responses flow back into the same records.

### The success network

The staff side is organized as a cross-office network — advisors, faculty, tutors, counselors, financial-aid staff, retention teams — with roles, caseloads, and routing rules configured per institution. The defining property is that the network spans offices: no single office's tool would produce this Type.

### Outcome measurement

The platform tracks the institution's success outcomes — persistence, retention, progression, completion — as managed measures at cohort and institution grain, typically shown as trends over terms and against peer or target benchmarks. Mature products add **initiative effectiveness**: connecting an intervention (a campaign, a program, a policy change) to the outcomes of the students it touched, so leadership can see what worked. The measurement layer is what closes the loop: signals → intervention → measured outcome → adjusted strategy.

### What the platform does not own

It does not own the official student record (that is the SIS, from which it draws), course teaching and grades (the LMS), or the enrollment funnel before the student enrolls (recruitment and admissions). Where vendors bundle these, they are separate concerns sharing one platform.

## How It Works

The operational rhythm of the platform is a continuous cycle:

```text
1. Assemble the picture
   SIS + LMS + interaction data flow into each student's profile
        ↓
2. Watch and signal
   Faculty raise alerts; rules and models flag drift; progress reports arrive
        ↓
3. Route and coordinate
   Alerts triaged, assigned to the right staff across offices;
   duplicates and overlaps avoided through shared visibility
        ↓
4. Reach out and support
   Appointments, messages, tasks, referrals; campaigns for whole cohorts
        ↓
5. Record and resolve
   Every action documented on the student's record; concerns closed
   with outcomes; nothing left hanging
        ↓
6. Measure and adjust
   Retention and persistence tracked; initiative effectiveness evaluated;
   findings feed the next term's programs and configurations
```

**A term in practice.** At term start, leadership launches campaigns to key cohorts (first-year students, students with registration gaps). During the term, faculty progress reports and automatic flags feed the alert queue; advisors and coaches work their caseloads — prioritized, in mature products, by risk indicators — meeting students, logging notes, assigning tasks. A concern about one student may route through several offices; the shared record keeps the handoffs coherent. At term's end, persistence is measured; the contribution of specific campaigns and programs is evaluated; the next cycle adjusts.

**Without signals, the loop cannot start** — a platform where staff only see students who book appointments has lost the proactive character that defines it. **Without resolution tracking, the loop stalls** — an alert that nobody is accountable for closing is a notification, not an intervention. **Without measurement, the loop cannot improve** — and the institution cannot distinguish a working program from a busy one.

## Interfaces

The following surfaces are described in conceptual terms; exact layouts and names vary by product.

### Student profile (360° view)

The platform's central record surface.

- Purpose: one place where any authorized staff member understands a student's situation
- Typical information: demographics and program, academic standing, course engagement, alerts and their status, appointments and notes, tasks, plans, support history across offices
- Primary actions: raise an alert or concern, log an interaction, schedule an appointment, assign a task, refer to another office, view history

### Alert queue / caseload worklist

The staff member's working surface.

- Purpose: turn incoming signals into an organized, prioritized workload
- Typical information: open alerts and concerns, source and age, assigned owner, student risk context, overdue follow-ups
- Primary actions: triage, accept or reassign, record contact, close with outcome

### Appointment scheduling

Shared by staff and students.

- Purpose: connect students to the right staff member without friction
- Typical information: staff availability, appointment types, student appointment history
- Primary actions: book, reschedule, cancel, record the session (staff side)

### Campaign / outreach composer

The population-scale surface.

- Purpose: coordinate outreach to a defined group of students
- Typical information: segment definition, message templates, channel (email/SMS), schedule, response tracking
- Primary actions: build a segment, compose and schedule the campaign, monitor responses, route non-responders to follow-up

### Population dashboards and reports

The leadership and analytics surface.

- Purpose: show the institution how its students and its efforts are doing
- Typical information: retention/persistence trends, cohort breakdowns, risk distribution, intervention participation and outcomes, resource utilization
- Primary actions: filter and segment, drill from population to individual, build custom reports, export

### Student companion surface

App or portal for the student.

- Purpose: let students act on their own success — and sometimes ask for help
- Typical information: their appointments, tasks, plan or pathway progress, campus resources, messages from staff
- Primary actions: book appointments, complete tasks, view plan, contact their support team, sometimes raise a concern

## Important Rules / Behaviors

**Proactivity is the defining behavior.** The platform's work originates with the institution, not the student: signals reach staff about students who never asked for help. This is the structural difference from service-portal and advising-appointment patterns.

**The loop closes or it fails.** An alert is a work item with an owner and an expected resolution — not a broadcast. Mature implementations make open, aging, and resolved states visible, so that concerns cannot silently disappear.

**Shared visibility is deliberately engineered.** The whole point is cross-office coordination, so notes, alerts, and history are visible across the success network — but scoped by role and governed by student-records regulations. Who may see what is a configured, audited property of the system.

**The official record is borrowed, not owned.** Academic standing, program, and enrollment come from the SIS; course activity from the LMS. The platform keeps its own operational record (alerts, outreach, notes, outcomes) but does not become the registrar's system. Divergence between the two is a known integration concern that vendors explicitly address.

**Individual actions roll up.** Every alert handled, appointment held, and campaign responded to contributes to population-level measurement. The two grains are continuously reconciled: a cohort dashboard is the sum of student records, and a student profile shows the campaigns and programs that touched them.

**Measurement spans terms.** Retention and persistence are only meaningful across enrollment periods, so the platform's history is deliberately long-lived; last term's data is next term's baseline.

## Variants

Common variants of the Type:

- **Analytics-first platforms** — built around institution-specific predictive models and outcome analytics, with workflows attached to the insight
- **Care-coordination-first platforms** — built around advising caseloads, alerts, and appointments, with analytics added
- **CRM-suite modules** — student success as one module of a journey-wide suite alongside recruitment, academic operations, financials, and advancement, sharing platform primitives
- **Community-college shapes** — emphasis on first-year persistence, transfer pathways, re-enrollment campaigns, and heavy caseload prioritization
- **Four-year and system shapes** — emphasis on cohort programs, equity-gap measurement, and multi-campus rollups
- **K-12 early-warning posture** — the same four-part operation driven by attendance, behavior, and grade signals rather than course persistence
- **Student-facing depth** — from thin companion apps to full student engagement hubs with self-raised concerns and guided journeys

A variant remains a variant as long as the four-part core holds. If the population grain and outcome measurement disappear, the product has become advising or casework software; if the intervention loop disappears, it has become an analytics dashboard.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Academic Advising Platform | closest sibling; converged market | centers the advisor–student relationship and advising workflow; alerts and referrals are common features there, but the population-wide operation and outcome measurement are not its center. Advisors are one staff class inside a success platform's network |
| Student Information System | substrate | the institution's official record system; the success platform draws academic and enrollment data from it and does not own the official record |
| Student Case Management | neighbor | issue-driven casework over individual cases is its center; here case-like objects (alerts, referrals) are instruments inside a population loop |
| Student Services Portal | neighbor | the student-facing front door for institutional services; the success platform is the staff-side operation, with a student companion surface at most |
| Enrollment Management / Student Recruitment CRM | upstream | operates the pre-enrollment funnel (prospect → applicant → deposit); the success platform operates the enrolled population for persistence; commonly bundled in one suite |
| Learning Management System | signal source | owns course teaching and engagement data; the success platform consumes that data as risk signal input |
| Institutional Effectiveness Platform | adjacent measurement | assesses unit/program outcomes for accreditation and improvement; the success platform measures student persistence outcomes and individual-level intervention effectiveness |
| Customer Success Platform | name collision only | B2B subscriber health and renewal — a different domain, different subjects, different measures; shares only the word "success" |

The boundary with Academic Advising Platform deserves emphasis because vendors market one converged category under both names. The practical test: strip the advising relationship from a student success product and the population, signals, coordination, and measurement remain — the Type survives; strip those from an advising product and the advisor–student relationship remains — that Type survives. The two leaves are kept separate on this center-of-gravity seam.

## Representative Products

- EAB Navigate360
- Civitas Learning Student Impact Platform
- Watermark Student Success & Engagement
- Salesforce Education Cloud (Student Success module)

Together these cover the dominant incumbent, the analytics-first specialist, the care-coordination specialist, and the CRM-suite pole, across community colleges, four-year institutions, and university systems.

## Sources

Research date: **2026-09-09**

- EAB — Navigate360 product page: https://www.eab.com/products/navigate
- Civitas Learning — Student Impact Platform: https://www.civitaslearning.com/platform/ ; Coordinate Student Care: https://www.civitaslearning.com/coordinate-student-care/
- Watermark — Student Success & Engagement: https://www.watermarkinsights.com/solutions/student-success ; Help Center root: https://support.watermarkinsights.com/hc/en-us
- Salesforce — Education Cloud overview: https://www.salesforce.com/education-cloud/ ; "What is student success?": https://www.salesforce.com/education/student-success-software/what-is-student-success/

> Sourcing limitation: all evidence is official product-page strength. Product help-center and knowledge-base articles were not reachable during research (the Watermark help-center category was confirmed to exist but its articles were not fetched; EAB, Civitas, and Salesforce knowledge bases were not reached). The document therefore describes structures, loops, and roles observable on official product surfaces, and deliberately avoids precise numeric limits, default settings, and exact workflow states. Vendor-published outcome figures (retention-rate improvements and similar marketing claims) are excluded from this document.

Detailed evidence, product-by-product observations, the cross-product comparison, and the boundary analysis are recorded in the paired Research Notes.
