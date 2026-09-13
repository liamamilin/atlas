# Athlete Injury / Availability Management

## Overview

An **Athlete Injury / Availability Management** application is organizational sports software used to record athlete injuries and illnesses, document their treatment and recovery, and maintain — for every athlete in a squad — a current availability state: whether they can train and compete fully, only in a modified way, or not at all.

It exists because in organized sport two questions must be answered every day, and they are owned by different people:

- the medical question — *what is wrong with this athlete, and what is being done about it?* (owned by athletic trainers, physiotherapists, team physicians)
- the participation question — *who can take part in today's session or match, and under what restrictions?* (owned by coaches and performance staff)

The application is the structured bridge between the two: medical staff document health events and determine readiness; coaches and other non-medical staff consume a restricted, status-level view that lets them plan sessions and selections without seeing confidential medical detail.

Its boundary: it is not a training-programming or workload tool (that is the surrounding Athlete Management System), it is not a general clinical record for care delivery and billing (that is an EMR/EHR), and it is not an administrative eligibility register (that is Sports Eligibility Management).

## Users & Context

Primary users — the people who record and decide:

- **athletic trainers / physiotherapists / medical staff** — document injuries, illnesses, evaluations, treatments and rehabilitation; set and update each athlete's availability; manage return-to-play progression
- **team physicians / clinical specialists** — provide diagnoses, imaging results, clearances; may be external parties whose input is recorded in the system

Primary consumers — the people who act on availability:

- **coaches** — plan sessions and select lineups around who is available, limited, or out
- **strength & conditioning / performance staff** — adapt training for athletes who are returning or restricted

Participating users:

- **athletes** — report wellness, symptoms, soreness and treatment feedback through athlete-facing apps or forms; receive care plans and appointments

Secondary users:

- **administrators / compliance staff** — manage records, consent, screening requirements, and reporting to schools, leagues or governing bodies
- in school and youth settings: **parents** — receive updates and complete forms about a minor athlete

Typical contexts: professional clubs and leagues, collegiate athletics, high-school athletic training, sports-medicine clinics serving teams, national federations and Olympic programs. The daily rhythm is a recurring loop — morning status review, session decisions, treatment delivery, documentation — repeated across a season.

## Core Model

The defining core is small. Everything else mature products add is described after it.

### The Defining Core

```text
Organizational Athlete Roster
└── Athlete (identified member of a team/squad)
    ├── Injury / Illness Record (dated health event, own lifecycle)
    │   └── Treatment & Rehabilitation documentation
    │   └── Return-to-play progression
    └── Availability State (current + expected, changes over time)
        └── surfaced to participation decision-makers
```

Three structures. Remove any one and the product stops being this Type:

- **Organizational athlete roster** — athletes exist in the system as identified members of teams or squads. Availability is always relative to a squad: without the roster there is nothing to be available *for*. This is what separates the Type from a personal health record or a clinician's private case files.
- **Injury / illness record attached to an athlete** — a dated, documented health event belonging to one athlete, carrying structured context (what body part, what kind of event, how it happened, how severe) plus its own lifecycle from onset through assessment, treatment and progression to closure. The record is the durable memory of the Type; availability decisions and surveillance reports are all derived from it.
- **Per-athlete availability state** — the system maintains, for each athlete, a current participation status (fully available / available with modifications / not available) and usually an expectation of change (e.g., a re-evaluation point or anticipated return). The state changes over time as the underlying injury evolves, and it is surfaced specifically to the people deciding participation — not as medical narrative, but as decision-ready status.

### Standard Capabilities of Mature Products

These are widespread in current products but are not what makes a product an instance of this Type:

- **Treatment and rehabilitation documentation** — encounter notes (often SOAP-style), interventions delivered, rehabilitation plans and exercise programs, progress notes against the injury record
- **Return-to-play progression** — staged protocols with milestones and criteria; a recorded clearance decision by an authorized medical role before full participation resumes
- **Athlete-reported input** — daily wellness/symptom questionnaires, soreness and pain scores, treatment feedback, submitted through an athlete app or web forms; feeds the availability picture alongside clinical findings
- **Injury surveillance and reporting** — incidence, re-injury, time-loss and burden aggregated by team, sport, injury type, or season; the same records power both daily decisions and long-term prevention analysis
- **Role-based information separation** — medical detail is restricted to authorized medical roles; non-medical staff see summarized status and restrictions. This separation is structural, not an add-on (see Rules)
- **Medical calendar and scheduling** — treatments, screenings, diagnostic appointments and follow-ups coordinated among staff and athletes
- **Screening and testing records** — pre-participation screenings, concussion baseline tests, and periodic assessments stored against the athlete
- **Alerts and flags** — signals when an athlete reports a problem, misses a questionnaire, or is due for re-evaluation
- **Mobile surfaces** — field-side documentation for staff; reporting and feedback for athletes

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:  Availability State
Implementations:  a status field on the athlete profile updated by medical staff;
                  a computed daily status assembled from injury state + questionnaire
                  responses + staff input; a per-session availability board

Concept:  Injury Record context
Implementations:  fixed structured fields; fully configurable injury metadata
                  (type, mechanism, contributing factors) defined per organization

Concept:  Athlete-reported input
Implementations:  native mobile app questionnaires; web forms; surveys;
                  data imported from wearables and third-party devices
```

A reader who has only seen one implementation — say, a school athletic trainer's documentation system — should still be able to recognize a professional club's integrated medical platform as the same Type from the core model.

## How It Works

Four loops carry the work. The first two are the daily heartbeat; the third and fourth span weeks to seasons.

### The injury lifecycle loop

```text
Event occurs (match, training, or reported symptom)
→ injury/illness record created on the athlete
→ assessment documented (evaluation, diagnosis, imaging/results attached)
→ treatment and rehabilitation plan recorded
→ each intervention and progress note appended to the record
→ injury progresses: status updates, milestones met
→ record closed when the athlete is fully returned (or the case ends otherwise)
```

The record is the anchor: every encounter, note, document and result is attached to a specific athlete and a specific injury, so the athlete's file becomes a longitudinal medical history, not a pile of loose notes.

### The daily availability loop

```text
Athletes submit wellness/symptom reports (or staff record observations)
→ medical staff review overnight reports + current injury states
→ each athlete's availability for today is set or confirmed
   (full / modified with specific restrictions / unavailable)
→ coaches and performance staff see the availability picture
→ sessions are planned and modified around it
→ treatments and re-evaluations happen; the loop repeats next day
```

Availability is time-bound and perishable: it is meaningful for a date and a context (today's training, this week's match), and it must be re-confirmed as circumstances change. A status set last week is not trusted this week.

### The return-to-play loop

```text
Injury stabilized → rehabilitation plan with staged milestones
→ athlete progresses through stages (each stage documented)
→ criteria checked (clinical findings, test results, functional performance)
→ authorized medical role records clearance for the next stage
   or for full participation
→ availability state upgraded accordingly
```

The pattern that matters: progression is gated. Moving from "rehab only" to "full training" to "competition" is a recorded medical decision, not an automatic consequence of time passing.

### The surveillance loop

```text
Injury records accumulate across teams/seasons
→ aggregated into incidence, time-loss, burden, re-injury reports
→ patterns identified (by injury type, mechanism, team, schedule context)
→ prevention programs and protocol changes follow
→ the effect shows up in future records
```

## Interfaces

### Athlete medical profile

The center of gravity for medical staff.

- Purpose: one longitudinal view of an athlete's health status
- Typical information: current medical status, injury history, assessments and test results, alerts, active care plans, documents and imaging
- Primary actions: open or create an injury record, document an encounter, attach results, update status, review history

### Daily status / availability board

The center of gravity for team decisions.

- Purpose: show, at a glance, who can participate today and under what restrictions
- Typical information: per-athlete status indicator (configurable in mature products — recovery, wellness, availability), restrictions, expected return, flags
- Primary actions: set or confirm availability, apply a restriction, export or share a status summary with non-medical staff

### Documentation surfaces

Where the record gets written.

- Purpose: fast capture of evaluations, treatments and notes, often from the field
- Typical information: note templates (including SOAP-style), intervention records, injury log entries with structured context questions
- Primary actions: create documentation from templates, log a treatment, complete an injury log entry

### Athlete app / athlete portal

- Purpose: collect athlete-reported input and deliver care information
- Typical information: daily wellness/symptom questionnaires, assigned forms, appointments, care instructions
- Primary actions: submit a report, complete a form, confirm an appointment, message staff securely

### Reports and dashboards

- Purpose: turn accumulated records into surveillance and accountability
- Typical information: injury counts and types by team/sport/period, time-loss, treatment volumes, encounter and referral counts
- Primary actions: build or open a report, filter, share with administrators or governing bodies

### Administration and configuration

- Purpose: shape what the organization records and who may see it
- Typical information: role definitions, form and note templates, injury-context fields, consent settings
- Primary actions: configure forms and fields, manage roles and access, manage consent

## Important Rules / Behaviors

### Medical confidentiality with a status exception

The most consequential rule: medical detail is restricted to authorized medical roles, while participation decision-makers receive a *status-level* summary — readiness and restrictions without clinical narrative. Mature products implement this as role-based access plus an explicit mechanism for sharing sanitized daily status with non-medical staff. In school settings the same rule extends to parents (updates permitted, records protected), and products serving that setting document compliance with health-privacy regimes and, in the researched sample, education-privacy regimes as well.

### Availability is derived, gated, and perishable

- Availability reflects the medical picture — injury states, reported symptoms, clearance decisions — rather than being an independent scheduling preference
- Escalation to full participation is gated by recorded medical clearance; time alone does not restore availability
- Availability is valid for a point in time and must be re-confirmed; yesterday's status does not automatically carry forward

### The injury record is append-and-preserve

Treatment and progress documentation accumulates against the injury record; the athlete's file is a longitudinal history that survives seasons. Records are edited with care and retained — they may be needed for surveillance, insurance, or governance review.

### Athlete-reported input is an input, not a verdict

Questionnaire responses (wellness, symptoms, pain) feed the availability picture but do not by themselves determine medical status; they trigger staff review. A missed or alarming report typically raises a flag rather than automatically changing availability.

### Partial availability is a normal state

Between "fully available" and "out" lies a routinely used middle: available with specific modifications (limited contact, no sprinting, minutes caps). The system must express restrictions, not just binary presence/absence.

## Variants

- **Elite professional / integrated platform** — the injury/availability core embedded in a club- or league-wide platform alongside performance, workload and operations; heavy configurability, league standardization, API integrations
- **Collegiate athletics** — multi-team organizations with compliance requirements; medical documentation and availability shared across sports medicine, strength and conditioning, and coaching staffs
- **School / youth athletic training** — documentation-first, mobile-first; strong parent-communication and minor-protection posture; products serving this setting document compliance with health-privacy regimes and, in the researched sample, education-privacy regimes as well
- **Sports-medicine clinic / outreach** — clinicians serving multiple schools or employers; documentation, referrals and value reporting for the contracting organization
- **Wearable-integrated monitoring** — load and device data (GPS, heart rate) feeding the availability picture; injury tracking rides on a monitoring platform rather than a medical record system
- **Concussion-program emphasis** — baseline testing, standardized assessment protocols and staged return-to-play tracks as a distinct program inside the product

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Athlete Management System | broader container | AMS adds training programming, workload, nutrition and testing; injury/availability is its medical slice. Remove injury records + availability from this Type and only a training tool remains; remove training programming from an AMS and this Type still stands |
| Sports-medicine EMR (no separate directory leaf; nearest: EHR) | overlapping pole | documentation-first implementations of the same core; a generic EHR serves care delivery and billing for a general patient population, while this Type serves participation decisions in an organizational sports context |
| Sports Eligibility Management | sibling, often confused | eligibility is the *administrative* right to compete (registration, academic standing, licensing); availability is *medical* readiness. Different records, different decision owners |
| Team Management Application | adjacent | roster, scheduling and communication for teams; may display availability but does not derive and manage it from medical documentation |
| Sports Performance Analytics | adjacent | analyzes performance data; injury surveillance reporting overlaps as a capability, but analytics platforms do not own the medical record or clearance decisions |
| Leave & Absence Management (HR) | structural analog | same abstract shape (person + absence record + expected return + restricted medical detail + clearance to return), different domain: employment rather than sport participation |

The most important boundary is with the Athlete Management System: in today's market the injury/availability core usually ships *inside* an AMS or a sports-medicine EMR. This leaf documents that core as a definable Type in its own right — the same way absence management is definable even though it usually ships inside an HR suite.

## Representative Products

- **Kitman Labs** — iP: Intelligence Platform with its Performance Medicine solution (elite clubs, leagues, collegiate)
- **Teamworks** — AMS (formerly Smartabase) and Sports EMR (collegiate, professional, Olympic, tactical)
- **Healthy Roster** — sports-medicine EMR for athletic trainers (US high schools, colleges, clinics, industrial)
- **Catapult** — athlete monitoring platform with injury and recovery tracking (wearable-first elite teams)

These four span the documentation-first pole, the availability-operations pole, and the load-monitoring pole, across professional, collegiate and school customer tiers.

## Sources

Research date: **2026-09-06**

- Kitman Labs — Performance Medicine: https://www.kitmanlabs.com/platform/performance-medicine/ ; homepage: https://www.kitmanlabs.com/ ; injury-lifecycle article: https://www.kitmanlabs.com/blog/optimize-injury-management-and-recovery-with-performance-medicine/
- Teamworks — AMS: https://www.teamworks.com/ams/ ; Sports EMR: https://www.teamworks.com/sports-emr/
- Healthy Roster — homepage and EMR platform: https://www.healthyroster.com/ , https://www.healthyroster.com/our-platform ; Knowledge Base: https://healthyroster.helpjuice.com/
- Catapult — Athlete Monitoring: https://www.catapult.com/solutions/athlete-monitoring

> Sourcing limitation: vendor help-center articles describing exact availability-status vocabularies were not reachable during research; status names and workflows are therefore described conceptually rather than as product-specific state lists. A planned availability-first sample (AthleteMonitoring) was unreachable and was replaced; standalone availability-first products are consequently under-represented in the sample. Detailed observations, cross-product comparison and boundary analysis are recorded in the paired Research Notes.
