# Patient Portal

## Overview

A **Patient Portal** is a care organization's authenticated patient-facing surface over the patient's own health record and services: the place where a patient logs in to see the clinical information the organization holds about them and to act on their own care — messaging the care team, requesting prescriptions, booking or managing appointments, completing forms, paying balances.

The defining structure is small:

```text
Patient's authenticated identity with the care context
└── Window onto the organization-held health record about that patient
    └── (read-mostly, release-governed, configurable by the organization)
        └── Patient-initiated self-service transactions
            └── into the organization's care workflows
```

Everything commonly associated with patient portals — mobile apps, bill payment, refill workflows, self-scheduling, telehealth links, device data, national identity infrastructure — is widespread in current products but is not what makes a portal a portal. A portal is a *window and a service counter*, not the record itself: the care organization's record system (typically an EHR) remains the owner of the clinical record, and the portal presents it and shuttles the patient's requests back into the organization's workflows.

When the interaction is initiated by the *organization* rather than the patient, the product is drifting toward a different Application Type (Patient Engagement Platform). When the presented content stops being the patient's own record, it is drifting toward a generic self-service account surface.

## Users & Context

Primary user: **the patient** — an identified person in the care organization's population who wants to check something about their own care or do something without calling or visiting: look up a result, see their medications, message their care team, request a refill, book or cancel an appointment, complete a form before a visit, pay a bill. Use is episodic and self-paced; sessions are typically short and purposeful.

A second patient-side role: **proxies and carers** — parents, family members, or carers authorized to act for another patient (a child, an elderly relative, someone they care for). Mature products make this explicit: the carer switches into the other person's profile, sees and does what their granted level of access allows, and the organization can set, change, or revoke it.

Organizational users work on the other side of the glass:

- **front-desk and patient-access staff** — receive and process what patients submit: appointment requests and cancellations, refill requests, forms, messages
- **clinical staff** — answer messages that carry clinical content, review and release results and documents for patient visibility
- **administrators** — decide which services are enabled for patients, what is visible, how enrollment works, and manage credential and proxy issues

Typical context: GP/family practices, medical groups and specialty clinics, hospitals and health systems, community health centers, and national or regional health services running a portal for their whole population. The portal usually runs *alongside* the organization's record system rather than replacing it — in most products it is delivered by the same vendor as the record system or integrated with it.

## Core Model

### The Defining Core

Three structures, held together. Remove any one and the product stops being recognizable as a Patient Portal.

**1. The patient's authenticated identity with the care context.** Access is identity-gated. The login is tied to an identified patient in the organization's records — either verified against existing registration data (identity proofing, activation codes, national identity infrastructure) or issued directly by the organization (staff-created credentials, emailed and reset through a staff workflow). A portal never serves anonymous visitors; without logging in there is nothing to see. The identity layer commonly extends to proxies acting for another patient under governed access.

**2. The patient's own window onto the organization-held record.** The portal presents the clinical information the care organization holds about that patient — test results, medications, allergies and conditions, immunizations, appointments, visit summaries, documents. It is read-mostly by design: the patient reads their record, they do not author it. What is visible is governed on two sides — by release rules (results and reports become visible after professional review/release, and can be withheld or hidden) and by organization configuration (a practice can switch a service off or hide sensitive information). In multi-provider and national variants, the window can aggregate records from several organizations about the same patient.

**3. Patient-initiated self-service transactions.** The patient starts the work. Secure messages to the care team, prescription/refill requests, appointment requests or cancellations, questionnaires and intake-style forms, document uploads, payments. What the patient submits does not change the record directly — it enters the organization's queues and workflows (messaging inboxes, scheduling systems, prescribing workflows, billing) where staff and clinicians review, act, and close the loop. Self-service here means *no staff mediation to start the work*, not *no staff involvement after it*.

### Standard Capabilities

These are what mature products commonly add around the core. They make the portal practical, but a product does not stop belonging to the Type for lacking any single one.

- **Secure messaging** — the standing asynchronous channel between patient and care team, usually with attachments; the most universal transaction in the sample of products researched
- **Test results with history** — result values with reference context, commonly trend graphs over repeated tests, always behind the release rules
- **Appointment self-service** — seeing upcoming and past appointments; booking or cancelling where the organization enables it
- **Prescription and refill requests** — requesting repeats of existing prescriptions into the practice's prescribing workflow
- **Documents and letters** — viewing, and in some products downloading, letters, reports, and visit summaries
- **Forms and questionnaires** — pre-visit intake, screenings, patient-reported measures completed by the patient and filed to the organization
- **Proxy/carer access** — governed acting-for-another-patient access with tiered permissions
- **Notifications** — email/SMS/push alerts that draw the patient back in (a new result, a new message, an upcoming appointment)
- **Enrollment machinery** — self-signup with identity verification or organization-issued credentials/activation
- **Health-choices and preferences** — contact preferences, language, and in some systems patient-recordable decisions (symptom notes, data-sharing choices, donation preferences)

### One Structure, Many Implementations

The Core Model is written in conceptual terms. Realizations vary:

```text
Concept:      Patient's authenticated identity
Realizations: identity proofing against registration data (national ID check, photo ID),
              organization-issued credentials (created/reset by staff),
              activation codes from the practice, national identity infrastructure
              (e.g. a national login service), app-store + social accounts layered on top

Concept:      Window onto the organization-held record
Realizations: single-organization EHR module, national single-record window
              (one GP record + selective hospital content), multi-provider
              aggregate platform collecting feeds from many care organizations

Concept:      Patient-initiated transactions
Realizations: in-portal messaging queues feeding staff inboxes; requests written
              into the record system's scheduling/prescribing/billing workflows;
              forms mapped to record-system templates for staff review and filing;
              payments into the billing system
```

A reader who has only seen one realization (for example, a US health-system app) should still be able to recognize a national health-service portal or a thin practice-level web portal from the Core Model.

## How It Works

### Enroll and prove identity

```text
patient starts enrollment (self-signup, or organization invitation)
→ identity is proven: proofing against registration data, photo/ID check,
  activation code from the practice, or national identity service
→ account is linked to the patient's record
→ organization-issued variant: staff create/reset credentials,
  patient forced to set a real password at first login
```

Access levels are common: until identity is proven, only general content is available; full access unlocks record viewing and transactions. The organization can also grant, tier, and revoke proxy access for carers through its own verification and consent process.

### See the record

```text
login → home (upcoming appointments, new results, new messages)
→ record sections: results, medications, allergies/conditions,
  immunizations, documents, visit summaries
→ visibility governed by release rules and organization configuration
```

What appears is what the organization has released for patient visibility — which is why the same portal can show different content to different patients, and why a result the patient knows exists may not yet be visible to them.

### Act: start a transaction

```text
pick an action:
  message the care team  → lands in the team's inbox for an answer
  request a prescription → enters the practice's prescribing workflow
  request/cancel an appointment → enters the scheduling workflow
  complete a form/questionnaire → files toward the record for staff review
  upload a document      → stored with the organization
  pay a balance          → posts to the billing system
→ the portal shows the request as sent; the organization works it
→ outcomes flow back: a reply, a confirmed appointment, a released result,
  a receipt — commonly with a notification drawing the patient back
```

The portal's interaction loop is exactly this round trip: the patient initiates, the organization processes, the outcome returns through the same surface. Nothing the patient submits silently rewrites the clinical record; staff review, correct, and store it.

### Act for someone else

```text
carer switches into the other person's profile (clearly labeled as acting-for)
→ sees and does what the granted level allows
  (appointments / prescriptions / results / record, per tier)
→ switches back; the organization can change or revoke the access at any time
```

### Core vs Common vs Optional

**Defining core** — without these, not a patient portal:

- authenticated patient identity with the care context
- the patient's own window onto the organization-held record
- patient-initiated self-service transactions into the organization's workflows

**Standard capabilities** — present in most modern products:

- secure messaging; results with history; appointment self-service
- prescription/refill requests; documents and visit summaries
- forms/questionnaires; proxy/carer access; notifications
- enrollment machinery; multi-language and accessibility support

**Variant / optional** — depends on market, geography, packaging:

- payments (common where care is billed; absent where it is not)
- self-booking breadth; device/wearable data; symptom diaries
- care-plan co-production; patient-reported measure programs; research matching
- telehealth video visits launched from the portal
- national identity infrastructure; multi-provider aggregation

## Interfaces

Surfaces are described conceptually; names and layouts vary by product.

### Home / dashboard

The entry surface after login.

- Purpose: orient the patient — what is new and what is pending.
- Typical information: upcoming appointments, new results or messages, outstanding forms or balances, notices from the organization.
- Primary actions: open a record section, start a transaction, respond to a notice.

### Record sections

The window onto the record, usually organized by data type.

- Purpose: let the patient read their own health information.
- Typical information: test results (values, reference context, history/trend), medications, allergies and conditions, immunizations, documents, visit summaries.
- Primary actions: view, open a result's detail or history, download where offered, request a correction through the organization.

### Messages

- Purpose: the standing written channel to the care team.
- Typical information: inbox threads with the practice or care teams, sent items, attachments.
- Primary actions: compose, reply, attach files or photos.

### Appointments

- Purpose: manage the patient's schedule with the organization.
- Typical information: upcoming and past appointments, location, provider, preparation instructions.
- Primary actions: book (where enabled), cancel or reschedule, request an appointment, add to personal calendar.

### Prescriptions

- Purpose: manage repeat medication requests.
- Typical information: current repeat medications, requested and completed requests, pharmacy choice where applicable.
- Primary actions: request a repeat, track request status.

### Forms and questionnaires

- Purpose: collect patient-completed information without a visit.
- Typical information: due or assigned forms (pre-visit intake, screenings, patient-reported measures), history of completed forms.
- Primary actions: complete and submit, save a draft where offered.

### Billing (where care is billed)

- Purpose: present and settle the patient's financial responsibility.
- Typical information: balances, statements, payment history, insurance summaries in billed-care markets.
- Primary actions: pay, set up payment methods, view statements.

### Profile, settings, and proxy management

- Purpose: govern identity and access.
- Typical information: personal and contact details, login and security settings, notification preferences, language, linked profiles.
- Primary actions: update contact details, change security settings, manage notifications, switch into/out of an acting-for profile.

## Important Rules / Behaviors

### The portal presents; the record system owns

The portal is a window and a service counter. Clinical records live in the organization's record system; patient submissions are reviewed, corrected, and filed by staff before (and if) they become part of the record. Even in products where the portal is part of the same suite as the record system, the patient side does not directly author clinical content.

### Result visibility is governed, not automatic

Results and reports reach the patient after a release step — professional review, an e-signature, or a configurable delay — and the organization can withhold or hide specific information. Some products deliberately delay results the professional wants to discuss first; some allow patients to opt out of record access or ask for specific items hidden. Exceptions exist where releasing would cause harm or expose third parties. Exact rules vary by product, organization, and jurisdiction.

### Access is earned in levels

Identity proofing gates full access; unverified users see at most general content. The organization decides which services are switched on — two practices on the same product can offer different capabilities. Proxy access is granted by the organization (or controlled by the patient, depending on the product), tiered, clearly signaled while acting for someone else, and revocable at any time; access for adolescents and children is handled with special care because of confidentiality.

### Transactions are asynchronous

A patient request enters the organization's workflow; it is not an instant commitment. Responses come back through the same surface — commonly with a notification — and turnaround depends on the organization. Urgent needs are deliberately routed elsewhere: patient-facing surfaces uniformly direct urgent or emergency situations to phone/urgent services rather than portal messages.

### What patients see is configured, not uniform

The same portal product serves different content and actions per organization and per patient: services switched off, sensitive information hidden, record scope limited to one care setting (for example a GP record, with hospital content coming from a different system or not at all). This is a structural property, not a defect — it is how the organization governs what its patients can reach.

## Variants

- **EHR-embedded portal** — the dominant packaging, especially in US-market health systems: the portal is a module of the record system vendor's family, launched under its own brand, sharing identity and data with the EHR.
- **Standalone multi-provider record platform** — a patient-facing platform independent of any single EHR, collecting feeds from multiple care organizations into one patient-accessible record; common where patients see many providers, and often the vehicle for patient sharing and patient-generated data.
- **National / regional health-service portal** — a public-health-service portal serving a whole population: identity anchored in national infrastructure, record scope anchored to the patient's registered practice, selective content from other care settings, and services shaped by the health system (which may include having no billing at all).
- **Thin practice-level portal** — a minimal web portal at a single practice: credentials, a record view, and a few transactions; the open-source self-hosted pole. Some products front the portal with a separate content-management layer for security isolation.
- **Inpatient / stay-based engagement** — bedside and during-stay variants; the same window idea applied inside a hospital admission, usually as part of a broader engagement product.
- **Adjacent family: payer/member portals** — health-plan member surfaces (claims, benefits, coverage) share the self-service grammar but anchor on the payer relationship, not the clinical record; they are a different population of products even when marketed with the same "portal" word.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Patient Engagement Platform | closest neighbor, frequently bundled | who initiates: the portal *waits* for the patient (login → view → act); the engagement platform *goes to* the patient (outreach, campaigns, journeys) and manages the response loop in staff queues; engagement products commonly exist to recruit patients into the portal and announce portal content |
| Electronic Health Record / EHR | containing / adjacent | the EHR is the record of record and the clinician's working chart; the portal is the patient-facing window over it — an EHR-embedded portal is the dominant packaging, but the Type also exists standalone and national without an EHR of its own |
| Customer Portal | same family, different domain | the same self-service grammar (authenticated stakeholder, own-records window, self-service actions, organization-curated surface); the patient portal's anchor is the patient record and care relationship, with health-specific machinery — identity proofing against patient records, release-governed result visibility, law-sensitive proxy access |
| Patient Scheduling | capability linkage | scheduling owns slot inventory and the booking system; the portal offers self-service entry points into it |
| Patient Registration & Intake | capability linkage | intake owns the episodic pre-visit registration workflow of record; portal forms are patient-initiated submissions that feed it |
| Telehealth Platform | capability linkage | the telehealth platform delivers the visit; a video-visit launch inside the portal is one action among many |
| Remote Patient Monitoring | adjacent | RPM owns device-telemetry monitoring loops and clinical review of them; portals display patient-entered or device data without owning a monitoring loop |
| Health Information Exchange | substrate vs surface | HIE moves records between organizations; when the cross-organization aggregate is presented to the *patient* as the product's center, that surface is a patient portal |
| Personal Health Record (market concept, no directory leaf) | naming-blur neighbor | a PHR is the person's own, person-controlled record; the portal presents the *organization-held* record back to the patient — some products self-label "PHR" while functionally being organization-fed patient windows, so market naming is porous |

## Representative Products

- NHS App (NHS England) — national health-service portal for a whole population
- Patients Know Best — standalone multi-provider patient record platform (delivered standalone and inside the NHS App)
- OpenEMR Patient Portal — open-source EHR-embedded portal module (native and CMS-fronted architectures)
- MyChart-class EHR-embedded portals — the dominant US health-system packaging; documented here only indirectly because their vendor documentation was not reachable in this research pass

## Sources

Research date: **2026-09-08**

- NHS — NHS App overview, help index, setting up / getting full access, viewing test results, family and carer access — https://www.nhs.uk/nhs-app/ , https://www.nhs.uk/nhs-app/help/ , https://www.nhs.uk/nhs-app/setting-up/get-full-access/ , https://www.nhs.uk/nhs-app/help/test-results/ , https://www.nhs.uk/nhs-app/help/profile/family-and-carer-access/
- Patients Know Best — platform overview and capabilities — https://www.patientsknowbest.com/ , https://patientsknowbest.com/capabilities/
- OpenEMR Project Wiki — OpenEMR Features (Patient Portal section), Patient Portal — https://www.open-emr.org/wiki/index.php/OpenEMR_Features , https://www.open-emr.org/wiki/index.php/Patient_Portal
- MEDITECH — Expanse Patient Connect (boundary evidence: the engagement layer that drives MyHealth portal enrollment) — https://ehr.meditech.com/ehr-solutions/expanse-patient-connect

> Sourcing limitation: the dominant US EHR-embedded portal vendors (MyChart/Oracle Health/athenahealth/Veradigm/NextGen) were unreachable from the research environment (403/404 on 2026-09-08), and one regional national-portal source (1177.se) was also unreachable. The US EHR-embedded variant is therefore documented only indirectly (open-source module pattern, vendor family naming, and cross-references from earlier research passes in this project). Claims about that variant are deliberately kept at "common/typical" strength; no precise limits, timings, defaults, or regulatory specifics are asserted. Detailed per-product observations, evidence layers, and the rejected-findings list are recorded in the paired Research Notes.
