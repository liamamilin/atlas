# Care Coordination Platform

## Overview

A **Care Coordination Platform** is operational software for coordinating the delivery of care to an identified person across the group of people responsible for that care. It anchors one shared record on the person, organizes a multi-participant care team around it, structures the intended care as a coordinated plan or program, and tracks the team's care activities — tasks, outreach, handoffs, referrals, documentation — through attributable, status-bearing states until the person's goals are met or the coordination episode closes.

The defining structure is deliberately small:

```text
Person under coordination
└── Care team (multiple roles, often multiple organizations) sharing one coordinated view
    └── Coordinated care plan / program organizing the intended care
        └── Tracked care activities feeding status back into the shared record
```

Everything else commonly associated with the category — enrollment and consent workflows, risk stratification, patient mobile apps, time tracking, billing reports, EHR integrations, automated outreach — is widespread in current products but is not what makes the product a care coordination platform. The same core structure appears in forms that predate or sit outside today's dominant implementations: hospital discharge coordination, payer case management, and community or social care coordination all fit it without chronic-program billing, patient apps, or population analytics.

When the software's center of gravity shifts — to authoring care-plan documents as controlled records, to routing a single referral to completion, to analytics over a whole patient panel, or to transporting records between organizations — it is drifting toward a different Application Type.

## Users & Context

The people who sit in front of a care coordination platform daily are mostly **non-physician care-delivery staff**:

- **care coordinators / nurse care managers / care navigators** — carry a caseload of people under coordination; run outreach, assess needs, maintain plans, assign and work tasks
- **medical assistants and community health workers** — execute delegated activities (scheduling, education, device check-ins, follow-up calls)
- **social workers** — address social needs surfaced by assessments and connect people to community services
- **supervising clinicians (physicians, nurse practitioners)** — own medical direction: review and sign plans, approve escalations, supervise delegated care under program rules
- **program / operations managers** — monitor caseloads, program performance, documentation quality, and reporting

The person being coordinated is a participant too: at minimum as the subject of the record and the recipient of outreach; in many products as an active user of an app or messaging thread.

Typical operating contexts:

- **physician practices and accountable-care organizations** running longitudinal care-management programs for chronic and at-risk populations
- **outsourced care-management service vendors** that deliver coordination programs on behalf of practices
- **health systems** coordinating transitions — discharge from hospital, follow-up, hand-off into post-acute or home care
- **health plans / payers** managing member care programs and post-acute networks
- **home-based and post-acute providers**, and **community-based organizations**, extending coordination into home and social care

## Core Model

### The Defining Core

**Person under coordination.** One identified human being is the anchor of the record. Everything else in the system — team assignments, plan content, activities, communications, documents — hangs off this record. The vocabulary shifts by deployment (patient, member, client), but the anchor is always an identified person, not an account, a case type, or a process instance.

**Care team with a shared view.** Coordination exists precisely because more than one person is involved. The platform maintains the set of people responsible for the person under coordination — across roles (coordinator, clinician, social worker, pharmacist) and frequently across organizations (practice, hospital, home agency, community service) — and gives every member the same view of the person's state: plan, activities, communications, history. Family members and caregivers are commonly included in the team's collaborative scope.

**Coordinated care plan / program.** The team's intent is organized into a plan: goals (what should improve or be maintained), interventions or steps (what will be done), and progress against them. In many deployments the plan lives inside a named **program** — a defined coordination offering with entry criteria, a service pattern, and an intended duration (an ongoing chronic-care program, or a bounded episode such as a post-discharge transition). The plan is what turns individual goodwill into structured, reviewable work.

**Tracked care activities.** Coordination is executed as discrete, attributable activities — an outreach call, a medication review, an education send, an appointment arranged, a referral placed, a handoff to another setting. Each activity is assigned to a team member, carries state (assigned → in progress → completed, or escalated), and feeds its outcome back into the shared record. This closed loop — nothing falls through, everything lands back on the record — is what distinguishes coordination from merely messaging the team or writing a plan.

Remove any one of these four and the product stops being recognizable as care coordination: without the shared team view it is a single-clinician tool; without the plan it is a generic task tracker; without tracked activities it is a care-plan document system; without the person anchor it is process software.

### Capabilities Mature Products Add

A typical modern platform carries most of the following. They make coordination practical at scale; they are not part of the definition.

- **Identification machinery** — finding who needs coordination: risk stratification over a population, program-eligibility checks, gaps in care, and event triggers such as admission and discharge notifications.
- **Enrollment and consent** — enrolling a person into a formal coordination program, recording their agreement (program participation and even communication channels commonly require documented consent).
- **Structured assessments** — intake and periodic assessments (health risk, activities of daily living, social needs) that surface barriers and feed the plan.
- **Outreach and communication with the person** — secure messaging or texting, education content delivery with engagement tracking, reminders. Patient-facing messages are typically visible to the whole assigned team in one thread, so the person deals with one conversation, not many staff.
- **Time and service documentation** — recording what service was delivered, by whom, and for how long, where programs are documented or billed on a time basis; in US fee-for-service programs this extends to billing-support outputs and claims automation.
- **Referrals** — sending work to external providers or community services and tracking its return, as one activity type inside the coordination record.
- **EHR and device interoperability** — pulling clinical context from electronic health records, health information exchanges, and monitoring devices (often bi-directional), or being embedded in the EHR suite itself. The platform coordinates on top of clinical systems; it does not replace clinical documentation.
- **Analytics** — dashboards over caseloads and programs: engagement, task throughput, plan adherence, utilization, and financial performance.
- **Patient-facing surfaces** — an app or portal where the person sees their plan, tasks, education, and team.

### One Structure, Many Implementations

The core is conceptual; deployments realize it differently:

```text
Concept:  Person under coordination
Forms:    enrolled patient (practice program) · health-plan member ·
          person in transition (discharge episode) · client of a community program

Concept:  Coordinated plan / program
Forms:    chronic-care program plan · post-discharge transition plan ·
          payer case-management plan · pathway for an episode of care

Concept:  Care activity
Forms:    outreach call · assessment · education delivery · appointment arranging ·
          medication reconciliation · referral · handoff · time documentation

Concept:  Care team member
Forms:    in-house coordinator · outsourced service-vendor nurse · hospital case manager ·
          payer care manager · community organization staff
```

A reader who has only seen one shape — say, a clinic's chronic-care program — should still be able to recognize a hospital discharge-coordination deployment or a payer case-management operation as the same Application Type.

## How It Works

### The longitudinal coordination loop

```text
Identify
  (population analytics flags a person · eligibility check · referral in ·
   admission/discharge notification · clinician points to a candidate)
→ Enroll & consent
  (person agrees to the program; consent recorded; program period starts)
→ Assess
  (structured intake: conditions, medications, functional and social needs, barriers)
→ Plan
  (goals and interventions set with the person; reviewed/approved by the
   responsible clinician; tasks generated from the plan)
→ Execute & coordinate
  (team members work tasks: outreach calls, education, scheduling, medication
   review, referrals, device check-ins; each action documented against the record)
→ Review
  (plan progress checked on a recurring cycle; sign-offs captured; stalled or
   worsening people escalated to the supervising clinician)
→ Report / close
  (service documentation aggregated; program reporting and, where applicable,
   billing outputs; person exits when goals are met or the episode ends —
   or continues on the recurring cycle)
```

The loop is fundamentally **longitudinal**: for an ongoing program it repeats on the program's recurring service cycle and continues until the person exits; for an episodic program (a care transition, a perioperative pathway) it runs from trigger event to closure.

### The transition variant

For care transitions the trigger is an event rather than a program enrollment:

```text
Admission / discharge notification received
→ person's context assembled into the coordination record
→ timely outreach to the person (and family) after the event
→ reconciliation and follow-up tasks (appointments, medication, services in place)
→ track until the person is stable in the next setting, then close the episode
```

The same record, team, plan, and task machinery apply; only the entry path and duration differ.

### Who does what

Day to day, coordinators live in their worklist: pick up assigned tasks, call or message people, document what happened, close tasks, escalate exceptions. Clinicians interact at review points: approve or adjust plans, handle escalations, sign off. Managers watch the dashboards: caseload distribution, task aging, program engagement, documentation completeness. The platform's job is to keep all of these roles converging on one person-state instead of parallel private views.

## Interfaces

### Coordinator worklist / task queue

The primary working surface for care-delivery staff.

- typical information: assigned people and tasks, due state, program, last-contact recency, flags
- primary actions: work a task, document the outcome, reassign, escalate, add a task

### Person coordination record

The shared anchor view of one person.

- typical information: demographic and program context, care team with roles, plan summary and progress, activity timeline, communications, attached clinical context (conditions, medications — usually synced from the EHR), documents
- primary actions: update plan elements, log an activity, message the person, adjust the team, review history

### Care plan editor

Where intent is structured.

- typical information: goals, interventions/steps, target dates, progress, responsible roles, review status
- primary actions: add/edit goals and interventions, generate tasks, record progress, request or capture review and sign-off

### Communication surface

Secure two-way messaging or texting with the person.

- typical information: one conversation thread per person, visible to the assigned team; outbound education content and engagement state
- primary actions: send/receive messages, send education material, log the exchange

### Assessment forms

Structured instruments that turn conversation into plan-ready data.

- typical information: health-risk, functional, and social-needs question sets; scores and flagged barriers
- primary actions: complete with the person, record responses, feed findings into the plan

### Program / manager dashboard

The oversight surface.

- typical information: caseload and panel views, enrollment status, task aging, engagement and contact metrics, documentation completeness, program-level outcomes
- primary actions: filter and drill into cohorts, redistribute workload, export reports

### Patient-facing app / portal (where offered)

The person's own view of the coordination relationship.

- typical information: care plan and goals, tasks or actions for the person, education content, device readings where monitoring is in scope, a way to reach the team
- primary actions: read and acknowledge, report readings or status, message the team

## Important Rules / Behaviors

### Consent gates program participation

Formal coordination programs require the person's documented agreement before the program starts (and, in many products, before even communication channels are used). A person can be engaged informally; the formal program state — with its service pattern and documentation obligations — begins at consent.

### Every activity is attributable

Coordination records are evidentiary: an activity carries who performed it, when, what was done, and how long it took where time-based documentation applies. This is not optional bookkeeping — program reporting, supervision, audits, and billing all draw on it.

### Team-wide visibility of person communication

Communication with the person is not private to one staff member. The typical design is a single thread per person that the entire assigned team can read, so any member can act with full context. This makes the communication surface simultaneously a relationship channel and part of the record.

### Plans are reviewed, not just written

Plans carry review cycles — reminders that a plan is due for review, captured reviews, and sign-offs from the responsible clinician and sometimes the person. A stale plan is a tracked exception, not the norm.

### The platform coordinates on top of clinical systems, not instead of them

Clinical documentation lives in the EHR; the coordination record holds what the EHR does not: who is coordinating what, against which plan, with what result. Integration fidelity (what syncs in, what writes back) is a structural property of each deployment; where integration is weak, the platform's record is fed manually and the coordination work gets harder, which is why interoperability is treated as a mature capability rather than an accessory.

### Eligibility and scope rules constrain programs

Programs define who may enroll (for example, condition-based criteria) and what may be delegated to which role under whose supervision. These rules shape what tasks appear, who can close them, and when clinician review is required.

### Nothing silently expires

Outstanding tasks and overdue reviews persist visibly until resolved, reassigned, or explicitly closed. The closed loop is the point: an unacted coordination need remains on the record rather than disappearing into an inbox.

## Variants

Common realizations of the Type:

- **Program-billing-centric platforms** — built around formal care-management programs (chronic, transitional, principal care, wellness visits) with eligibility, consent, time documentation, and claims automation as first-class machinery; sold to practices, ACOs, and outsourced coordination service vendors. Dominant in the US market.
- **EHR-embedded modules** — coordination delivered as modules inside an EHR vendor's suite, trading standalone depth for native data access and one login.
- **Enterprise orchestration platforms** — coordination realized as automated, event-driven orchestration over existing systems: pathways execute themselves where safe and route to humans where judgment is needed; deployed once per health system across many use cases (perioperative, discharge, follow-up).
- **Experience-led virtual care platforms** — patient-experience-first deployments where the person's app, coaching, and connected devices are the visible surface and the coordination machinery sits behind them; common in payer and "virtual care" deployments.
- **Transitions and post-acute coordination** — event-triggered coordination across hospital → post-acute → home, including payer-managed post-acute networks; often paired with discharge-planning and referral-intake machinery.
- **Social and community care coordination** — the same core extended to non-clinical needs: social-needs screening, closed-loop referral to community organizations, coordination across health and social care.
- **Regional and historical forms** — hospital case management and discharge planning, payer disease-management programs, and international integrated-care deployments realize the same core with local program structures instead of US billing programs.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Care Plan Management | authors and controls care-plan documents as records; care coordination uses the plan as the engine for team execution and accumulates activity evidence around it |
| Chronic Care Management | program-shaped slice of care coordination bound to specific chronic-care program rules (eligibility, time documentation, billing); closest seam in this category |
| Population Health Management | analytics and registries over whole panels to find who needs attention; care coordination is the person-level execution arm that acts on those findings |
| Payer Care Management | the same coordination machinery owned and run by a health plan over members, tied to utilization and cost oversight rather than provider-side program delivery |
| Referral Management | runs one request→routing→completion loop between organizations; coordination holds a longitudinal record in which referrals are one activity type |
| Patient Engagement Platform | centers patient-facing outreach, education, and content; coordination centers staff-side orchestration, with patient surfaces as one channel |
| Remote Patient Monitoring | collects and monitors device data as its defining loop; coordination consumes those readings but the device loop is not coordination |
| Clinical Communication Platform | secure clinician-to-clinician messaging as the primary product; coordination binds communication to a person's plan and record |
| Health Information Exchange | transports records between organizations; no team, plan, or activity loop |
| Telehealth Platform | delivers virtual visits; a visit is one event, not a longitudinal coordination relationship |
| Patient Scheduling / Registration & Intake | front-door operational tools; no shared longitudinal plan or team record |
| Home Health EHR / Home Care Agency Management | the delivery agency's own system of record for visit-based care; coordination hands off to it across settings |
| Social Services Case Management | the community organization's case file; social care coordination networks sit at the seam, closed-loop-referring between health and social care |

The closest seam is with **Chronic Care Management**: in today's US market the same products are frequently marketed as both, with chronic-care management being the care coordination Type carrying a specific program's eligibility, documentation, and billing rules. **Care Plan Management** is the next-nearest: both revolve around care plans, but only one of them is organized around executing those plans with a team over time.

## Representative Products

- **ThoroughCare** — pure-play care coordination platform for practices, ACOs, and outsourced care-management service vendors, organized around care programs and their documentation/billing workflows
- **eClinicalWorks (Population Health suite)** — EHR-embedded care coordination: care planning, chronic/transition care management, monitoring modules inside the EHR vendor's platform
- **Lumeon** — enterprise care-orchestration platform automating coordination tasks, events, and workflow across health-system use cases (now part of Health Catalyst)
- **Carium** — experience-led virtual care management platform combining patient app, connected devices, and care-team consoles (a Healthmap Solutions company)
- **WellSky** — full-continuum platform family deploying care coordination across hospital discharge, post-acute, home, payer, and community/social settings

## Sources

Research date: **2026-09-06**

- ThoroughCare — https://www.thoroughcare.net/ and https://www.thoroughcare.net/care-coordination
- eClinicalWorks — https://www.eclinicalworks.com/products-services/population-health-ccmr/ , https://www.eclinicalworks.com/products-services/population-health/chronic-care-management-software/ , https://www.eclinicalworks.com/products-services/population-health/care-planning/
- Lumeon — https://www.lumeon.com/
- Carium — https://www.carium.com/
- WellSky — https://wellsky.com/ (care coordination, transitional care, and social care coordination solution lines)

> Sourcing limitation: all sources are official vendor product/solution pages; operational help-center and user-guide documentation was not reachable from the research environment during this pass (one help-center attempt returned an access denial and was not retried). The document therefore states workflow and rules at the level the official pages support and deliberately avoids precise operational figures (time thresholds, numeric limits, default settings, exact state labels). Detailed observations, the cross-product comparison, and vendor-specific findings are recorded in the paired Research Notes.
