# Nonprofit Case Management

## Overview

A **Nonprofit Case Management** application is the casework system of record for mission-driven service organizations — nonprofits, charities, and community-based organizations that deliver help directly to people. It holds identified records for the people the organization serves, opens and tracks a bounded casework episode (a **case**) for each person under an accountable caseworker, records the contacts, services, and referrals that make up the episode, and carries the case through intake, active service, and a recorded closure. Because these organizations are funded by grants and contracts, the record also feeds the outcome and compliance reporting the organization owes its funders.

The defining core is deliberately small:

```text
Client record (person served, with family/household context)
└── Case (bounded casework episode under an accountable caseworker)
    └── Documented casework record (dated, attributed notes, services, assessments)
        └── Tracked lifecycle: intake → active service → recorded exit/closure
```

Remove the case-and-caseworker machinery and the product becomes a served-population registry (Beneficiary Management territory). Remove the person and service semantics and it becomes a donor CRM or a task tracker. Nothing in the core requires statutory authority, court involvement, or clinical licensing — those belong to neighboring government and health-care Types.

## Users & Context

Primary users:

- **caseworker / case manager** — owns a caseload of cases; conducts intake, assessments, and service sessions; records case notes; makes and receives referrals; moves each case toward its outcome and closure. Products in this category are typically designed around this role first.
- **intake staff** — register new clients, run screening and eligibility questions, open cases.
- **supervisor / program manager** — reviews caseloads, monitors progress and deadlines, approves plans, and answers for the program's outcomes.

Secondary users:

- **administrator** — configures programs, forms, fields, vocabulary, and access permissions; each organization tailors the system to its own programs.
- **executive / development staff** — consume aggregate reports for funders, grant applications, and boards.
- **clients (participants)** — in many products, submit online forms, exchange messages, or book appointments through a portal; some organizations receive referrals from clients or partner agencies through public web forms.

The work environment is an office plus the field: casework happens at desks, in homes, and in community settings, so documentation is often done wherever the contact happens. The organizations operate under grant and contract conditions, which makes documentation discipline and outcome reporting an everyday requirement rather than an afterthought.

## Core Model

### The defining core

Three structures, jointly held, make the product what it is:

**Client records.** Persistent, identified records for each person the organization serves — called *clients*, *participants*, or *service users* depending on the product and region. A client record carries identity and contact details, family or household context, and consent information, and it outlives any single case: a person may return years later, and the history comes with them. Duplicate checking against the existing client base is standard, because the same person often re-enters through different programs or workers.

**Cases (casework episodes).** A case is a bounded episode of service opened for a client — typically when the client is enrolled in one of the organization's programs or services. The case is assigned to a named caseworker who is accountable for it, carries a tracked lifecycle from intake through active service to a recorded exit or closure, and is the unit around which work, deadlines, and supervision are organized. Staff do not experience the system as an undifferentiated list of people; they experience it as a **caseload** — the set of cases they are responsible for.

**Documented casework records.** Every contact, session, and service delivery is documented on the case as dated, attributed entries: case notes, session or service records, completed assessment forms, attached documents. Individually these entries are small; accumulated, they form the client's service history — the evidence of what the organization did, when, and by whom. This documentation is what makes the episode accountable: to the supervisor reviewing the case, to the funder auditing the grant, and to the next worker who picks it up.

### Structures around the core

Mature products commonly organize these structures with:

- **Programs and services** — the organization's defined offerings. An enrollment binds a client to a program, and the case is opened under it; enrollments and exits are tracked per program so the organization can see who is in what.
- **Referrals** — links between the case and other workers, programs, or outside organizations. Products commonly distinguish internal referrals (to a colleague or another program in the same organization) from network referrals (to a partner agency), and track each referral's progress. A service directory of external providers is a common companion.
- **Service plans and goals** — a forward-looking structure on the case: what the client is working toward, what services support it, and what progress looks like. Common in mature products, especially where outcomes are contracted.
- **Assessments** — structured forms capturing needs, risk, or eligibility at intake and at intervals; many products let the organization build its own.
- **Outcome measures** — standardized instruments (often licensed scales) administered at the start and end of service, so improvement can be quantified for funders.
- **Reporting** — aggregates drawn from the case record: enrollment counts, service volumes, outcomes, and compliance data, packaged for funders and oversight bodies.

### How the objects relate

```text
Client (person record, household context, consent)
  ↓ intake & assessment
Enrollment in a Program / Service
  ↓ opens
Case — assigned to a Caseworker
  ↓ accumulates
Case notes · session/service records · assessments · documents
  ↕ includes
Service plan / goals · Referrals (internal & network)
  ↓ ends
Recorded exit / closure with outcome
  ↓ aggregates
Funder & oversight reporting
```

The client is the anchor of continuity; the case is the engine of work; the documentation is the product of both.

## How It Works

### Intake to open case

```text
A person seeks help (walk-in, website form, phone, partner referral)
→ staff search for an existing client record (duplicate check)
→ create or update the client record
→ capture presenting needs via intake/assessment forms
→ determine program fit or eligibility
→ enroll the client in a program
→ open a case, assigned to a caseworker
```

Some products let clients self-register or refer themselves through public web forms; some let partner agencies send referrals electronically. Either way, entry produces the same thing: a client record and, usually, a case.

### The casework loop

```text
Appointment or contact with the client
→ deliver the session or service
→ document it (case note, service record, attendance)
→ update the service plan and progress
→ make or receive referrals as needs surface
→ schedule the next contact
→ repeat until goals are met or the episode ends
```

This loop is the daily work of the product. Tasks, alerts, and scheduling keep it moving; supervision reviews keep it accountable.

### Closure and reporting

```text
Goals met / client exits / service complete
→ record the exit reason and outcome (often a final outcome measure)
→ close the case
→ the closed case remains part of the client's history
→ aggregates flow into program and funder reports
```

Closure is a recorded act, not silence: the end state of a case is part of the record, which is what lets the organization answer a funder's "what happened to the people you served?"

### Configuration

Because every organization runs different programs with different questions, mature products are configuration-first: administrators design intake and assessment forms, define fields per record type, adapt workflows, and even rename terminology to match the organization's own language. A substantial part of adopting such a system is this tailoring.

## Interfaces

The surfaces below are described conceptually; exact names and layouts vary by product.

### Client / person profile

The anchor surface for one person.

- identity and contact details, household/family links, consents
- all cases and all case notes for the person, together — the person's history with the organization
- primary actions: update details, open a new case or enrollment, review history

### Case view

The working surface for one episode.

- case status, assigned caseworker, program linkage, key dates
- the documentation trail: notes, service records, assessments, attached documents
- plan and goals, referrals in and out, tasks
- primary actions: add a note or service record, update status or plan, make a referral, close the case

### Caseload / work list

The caseworker's daily view.

- the cases assigned to the worker, with status and next actions
- tasks, appointments, alerts (overdue contacts, upcoming deadlines)
- primary actions: open a case, complete a task, record today's contacts

### Intake and assessment forms

Configurable form surfaces used at entry and at review points.

- organization-designed questions, eligibility fields, standardized measures
- primary actions: complete, submit, review earlier submissions

### Program administration

The administrator's surface.

- program and service definitions, enrollment rules, custom fields, form designs, terminology
- primary actions: create/modify programs, build forms, adjust fields and workflows

### Referral tracking

A board or list of referrals.

- incoming, outgoing, and internal referrals with their progress
- primary actions: create a referral, accept/reject, record the outcome

### Reporting and dashboards

- enrollment counts, service volumes, outcomes, compliance data; filters by program, site, worker, demographics
- primary actions: build/run reports, export for funders

### Client-facing surfaces

- online forms, portals, and messaging through which clients submit information, book appointments, or exchange messages with staff — present in most modern products, but optional.

## Important Rules / Behaviors

### Confidentiality is structural

Case records describe people in vulnerable circumstances — health, housing, family, money. Access control is therefore part of the product's substance, not a settings afterthought: role-based permissions are universal, and mature products add finer restrictions (limiting which records or fields a user may see, so that workers see only what their role requires), audit logging of who changed what, and data-protection machinery such as archiving and verified deletion. Some verticals (domestic-violence services, health-adjacent programs) carry stricter confidentiality postures, and products serving them advertise compliance regimes accordingly.

### Documentation is the accountability contract

The record — not memory — is what the organization stands on. Notes are dated and attributed; service deliveries are recorded as they happen; missing fields and duplicates are surfaced as data-quality problems because they weaken the evidence the organization must produce. Automation in mature products often targets exactly this: converting conversations into structured notes, flagging missing data before reporting deadlines, prompting follow-up when a case goes quiet.

### The case has a bounded, tracked life

A case opens, is worked, and ends in a recorded exit. Cases do not silently evaporate; the transition to closed is an explicit act with a reason and usually an outcome. What happens after closure — reopen, new episode, or permanent record — varies by product and program, but the closed case persists in the client's history.

### Programs define the frame, the organization defines the programs

There is no universal program catalog and no universal eligibility rule: eligibility, intake questions, and outcome measures are organization-defined (or funder-defined), which is why configurability is a defining trait of the category's mature products. This is also what separates the Type from government statutory systems, where the frame is set by law.

### Referrals cross boundaries — and are tracked

A case routinely touches other workers, programs, or agencies. Referrals are recorded on the case with their direction (in, out, internal) and progress, so that responsibility is never lost between organizations.

### No statutory machinery in the core

Nothing in the defining core requires mandated reporting, court orders, state custody, or placement authority. Where a program carries statutory duties (child protection, court-involved work), specialized Types apply; a generic nonprofit case management system may *record* such events, but the machinery that gives them legal force is not part of this Type.

## Variants

The Type is one market realized in several postures and flavors:

- **Packaged tiered SaaS (US human-services flagship posture)** — boxed case management with good-practice templates, sold in tiers; funder compliance and outcome reporting at the center.
- **Configurable person-centric platform** — modern SaaS built around the person's whole story rather than single programs; emphasizes caseworker experience.
- **Enterprise multi-program platform** — large platforms consolidating many programs (and sometimes many organizations) on one data foundation, with warehouse-grade analytics and high-volume claims or HMIS-style data standards in some verticals.
- **Small-organization tailored system** — lighter, modular systems for small charities; profile-based records, session registers, outcome measures, and self-service configuration; common in the UK charity sector.
- **Vertical flavors** — behavioral health (adds clinical documentation, standardized clinical measures, and billing, straddling toward health EHRs); homelessness/housing (coordinated-entry and data-standard postures); domestic violence and victim services (heightened confidentiality); workforce and employment; youth and family services; aging and disability services; criminal-justice reentry; refugee and migrant support.
- **Operator straddle** — the same products are frequently sold to government agencies under government-oriented editions; the casework spine is identical, the mandate differs.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Beneficiary Management | closest sibling (§25) | centers the served-population registry: who is registered, what was delivered to them, aggregated upward — without a bounded casework episode or accountable-caseworker machinery as the product's center; remove the case/episode machinery here and that is what remains |
| Social Services Case Management | government counterpart (§24) | same casework spine, but operated under statutory mandate with government-defined eligibility and entitlement; here programs and eligibility are organization-defined and accountability runs to funders |
| Child Welfare Management | statutory specialization (§24) | adds the child-protection loop: mandated reports with screening decisions, safety/risk assessments with legal force, placement and permanency machinery, need-to-know confidentiality over an identified child |
| Nonprofit CRM / Donor Management System | opposite flow | records money flowing in (gifts, memberships, campaigns, stewardship); this Type records services flowing out (eligibility, delivery, casework, outcomes); one vendor family can sell both |
| Nonprofit Program Management | container vs. contents | manages programs as initiatives (plans, budgets, milestones); this Type manages the people and cases inside them |
| Monitoring & Evaluation Platform | results vs. casework | centers planned-results frameworks and indicator actuals for funder accountability, often with no person-level registry; this Type's floor is the case-level service record |
| Care Plan Management / Care Coordination (health) | clinical neighbor | health care plans are clinical records under health-sector governance; the behavioral-health vertical of this Type straddles toward them |
| HR / Legal Case Management, ITSM tickets | name only | the word "case" is shared; the objects (employees, legal matters, incidents) and rules are entirely different |

The boundary with Beneficiary Management is the most important one, because market vocabulary uses "case management" for both. The structural line is the center of gravity: an accountable caseworker driving a bounded episode to closure versus a population registry accumulating deliveries and participation state. Many real products straddle the line; the Types remain distinct.

## Representative Products

- **Apricot (Bonterra)** — packaged case management for nonprofits; caseloads, enrollments and exits, referrals, funder-ready reporting (US)
- **Casebook** — configurable, person-centric case management for community organizations, schools, and public agencies (US)
- **CaseWorthy (incl. the former ClientTrack)** — enterprise multi-program human-services platform spanning nonprofits and government (US)
- **Lamplight** — tailored "case management CRM" for small and medium charities (UK)

The sample spans packaged/configurable/enterprise/small-org postures and two regions; products serving government agencies were included to check the government/nonprofit seam.

## Sources

Research date: **2026-09-08**

- Apricot (Bonterra) — product page and official feature FAQ — https://www.bonterratech.com/product/apricot
- Casebook — platform overview and case management solution pages — https://www.casebook.net/platform-overview/ , https://www.casebook.net/case-management-solution/
- CaseWorthy — product homepage and FAQ (fetched via the former ClientTrack URL following the February 2025 Eccovia/CaseWorthy merger) — https://eccovia.com/product/clienttrack/
- Lamplight Database Systems — homepage and system features — https://www.lamplightdb.co.uk/ , https://www.lamplightdb.co.uk/system-features/

> Sourcing limitation: operational help-center documentation was not reachable for any sampled product from the research environment on 2026-09-08 (blocked or unavailable); all direct evidence comes from official vendor product pages and FAQs. Lifecycle stages, object structures, and rules in this document are therefore described conceptually; no numeric limits, exact status vocabularies, or default settings are asserted. Detailed evidence, product-by-product observations, and the cross-product comparison are recorded in the paired Research Notes.
