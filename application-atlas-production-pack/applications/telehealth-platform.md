# Telehealth Platform

## Overview

A **Telehealth Platform** is software through which clinical care is delivered remotely. Its unit of work is the **virtual clinical encounter** — a visit that binds an identified patient to an identified clinician and is carried as clinical work: the patient enters the encounter through a managed care process (an appointment, an on-demand request, or a check-in queue), the encounter is delivered live through the platform, and it sits under the posture of regulated clinical care.

The defining structure is small:

```text
Identified patient + identified clinician
└── Remote clinical encounter (the visit)
    └── Care-delivery context (entry as clinical work + regulated handling)
```

Everything else commonly associated with modern telehealth — browser-based patient access, waiting rooms, screen sharing, in-visit documentation aids, consent capture, claim coding, virtual care hardware — is widespread in current products but does not define the Type. If the encounter stops being organized and carried as clinical work, the product is a video conferencing tool; if the platform stops delivering encounters, it drifts toward scheduling, portal, or monitoring territory.

## Users & Context

Three participant groups use a telehealth platform, with different surfaces and stakes:

- **Patients** participate as patients of a practice, a health system, or a care service. They typically join from home or work, on a phone or computer, through a link or an app. In the provider-side model they need no account of their own; in the service model they hold a member identity because the service, not an outside practice, delivers the care.
- **Clinicians** (physicians, nurse practitioners, therapists, specialists) conduct the encounters. They work from the platform's provider surface, often alongside their EHR or practice-management suite, and remain responsible for what would be their clinical duties in a physical visit: assessment, documentation, consent, prescriptions where in scope.
- **Practice, clinic, or program staff** manage the care process around the encounters: scheduling or queueing patients, moving them between providers, handling no-shows and technical problems, and reconciling payment.

The buying context ranges from a solo clinician adopting a standalone virtual-room tool, through private practices using telehealth inside their practice-management suite, to health systems embedding virtual visits in the EHR, and payers or employers buying virtual care as a service delivered by the vendor's own clinician network.

## Core Model

### The Defining Core

```text
Identified patient + identified clinician
└── Remote clinical encounter (the visit)
    └── Care-delivery context (entry as clinical work + regulated handling)
```

Three properties. If any one is removed, the product stops being a telehealth platform:

- **Identified patient and identified clinician.** Every encounter is between a specific patient and a specific care provider. The patient participates as a patient (of a practice or a service), the clinician as the responsible provider. Without the patient side, the product is a generic meeting tool; without the clinician side, it is peer calling.
- **Remote clinical encounter as the unit of work.** The platform's central object is the visit — not the meeting, the booking, or the device data stream. Scheduling, waiting, delivery, and documentation all hang off this encounter. Without it, the product is conferencing software.
- **Care-delivery context.** The encounter is anchored in a care-delivery operation: it is scheduled, requested, or queued as clinical work within a practice or service, and it is handled under the posture of regulated clinical care — healthcare privacy obligations, clinical consent, professional licensure. Without this, the product is a conferencing tool with healthcare branding, not a telehealth platform.

### What Mature Products Add

A typical modern telehealth platform carries most of the following. They make the Type practical; they are not what makes it a telehealth platform.

- **Managed entry into the encounter** — a waiting room and patient check-in, so the patient's arrival mirrors a clinic visit rather than a dropped-in call; an on-demand request queue in service-style products.
- **Link-based patient access** — patients join from a browser, commonly without installing anything and often without any account; a light member identity replaces the guest link in service-style products.
- **Scheduling integration** — telehealth visits usually live on the practice's calendar (sometimes realized as a "virtual" visit location) or in the service's booking flow.
- **Delivery surface** — live video (dominant), audio, and text chat; multi-party configurations for interpreters, family members, supervising clinicians, or group sessions.
- **In-visit clinical aids** — screen sharing, photo capture and file exchange, closed captions, interpreter participation, and domain-specific tools in some specialties.
- **Documentation and consent support** — session history, note templates or structured notes, transcripts, and recorded telehealth consent — either inside the platform or handed off to the EHR where the record lives.
- **Payment and claim hooks** — collecting payment around the visit and, where payer billing applies, telehealth-specific claim coding that distinguishes virtual from in-person care.
- **Compliance machinery** — healthcare privacy agreements (business-associate-class), encryption, and audit posture appropriate to clinical encounters.

### One Structure, Many Implementations

The core model is written conceptually. Products realize it differently depending on which packaging pole they occupy:

```text
Concept:      Encounter entry as clinical work
Realizations: appointment on the practice calendar with a telehealth link
              check-in link into a provider's waiting room
              on-demand care request in a member app
              EHR-embedded scheduled visit launch

Concept:      Patient identity
Realizations: guest link with no account
              light client/member account with the service

Concept:      The clinical record
Realizations: in-platform notes and session history
              documentation drained into the practice's EHR
```

A reader who has only seen one pole (for example, the standalone virtual-room tool) should still be able to recognize the service pole and the embedded pole from the core model.

## How It Works

### Scheduled, provider-side visit (the practice pole)

```text
Patient books (or requests through a portal) a telehealth appointment
→ appointment carries a telehealth link; reminders include it
→ at visit time the patient opens the link, checks in
→ patient waits in the platform's waiting room; clinician sees the queue
→ clinician admits the patient → live encounter (video, audio, chat)
→ in-visit aids as needed (screen share, photos, interpreter, captions)
→ encounter closes; documentation written (in-platform or in the EHR)
→ consent recorded; payment collected or claim prepared
```

### On-demand, service-side visit (the care-service pole)

```text
Member requests care in the app/web (24/7 or scheduled)
→ request enters the service's queue; a clinician from the network is assigned
→ member is connected into the live encounter
→ clinician assesses, documents, and issues prescriptions or care plans where in scope
→ visit summary delivered to the member; record shared with the member's care system where applicable
```

### Enterprise, health-system visit (the embedded pole)

The encounter machinery is embedded in the health system's EHR and workflow: staff launch virtual visits the way they launch in-person ones, the platform routes the consult (internal clinicians, partner network, or the vendor's own network when capacity requires), and the documentation lands directly in the health record. In facility settings, fixed virtual-care hardware can stand in for the patient-side camera.

### What varies and what does not

Across all three poles, the middle of the loop is the same — an identified patient and clinician meet in a live encounter organized by the platform's care process. What varies is who runs the care process (the customer's practice vs the vendor's service), where the record is written (platform vs EHR), and how the patient arrives (guest link, member app, EHR launch).

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Provider dashboard / queue

The clinician's operating surface.

- today's appointments and their telehealth links, the checked-in patient queue, waiting-room status
- primary actions: admit a patient, start a visit, invite a patient, move a patient to another provider (in team settings)

### Waiting room / check-in

The patient's arrival surface — the platform's clinical framing of "please have a seat."

- confirmation that the right provider received the check-in, preparation tips (camera/microphone check), privacy notices or consent prompts
- primary actions: check in, wait, communicate a problem

### The encounter surface

The live visit — video tiles for patient and clinician, with controls around the call.

- video/audio controls, chat, screen share, photo/file capture, captions, interpreter slot, multi-party layout for group or supervised sessions
- primary actions: start/end the encounter, use in-visit aids, pause or transfer where supported

### Scheduling / calendar surface

Where the care process organizes encounters (provider-side and embedded poles).

- calendar or list of telehealth appointments, telehealth locations, availability for virtual visits, portal-initiated requests
- primary actions: book, reschedule, cancel, send links/reminders

### Documentation / history surface

Where the encounter's clinical aftermath lives.

- session history, note templates or structured notes, consent records, transcripts where offered
- primary actions: write/complete documentation, export to the EHR, attach to the patient record

### Patient/member app (service pole)

The care-seeker's surface in service-style products.

- care catalog, request flow, visit history, prescriptions and summaries where issued
- primary actions: request care, join a visit, view records

## Important Rules / Behaviors

### The encounter is regulated clinical work

A telehealth encounter is not a casual call. The platform is operated under healthcare privacy obligations (in the US, HIPAA-class business-associate agreements covering the encounter), clinical consent for remote care is captured, and the clinician's authority to deliver the care is bounded by licensure — in the US, clinicians must be licensed in the state where the patient is located during the visit. These constraints are structural: products surface licensure, consent, and privacy posture as first-class concerns, not fine print.

### Patient location matters

Because licensure and claim rules attach to where the patient physically is during the encounter, the patient's location at visit time is a meaningful datum — products and clinical guidance treat it accordingly (consent rules for minors, for example, follow the patient's location, not the clinician's).

### Entry is mediated, not ad hoc

Patients do not dial into an encounter directly. They check in, wait, and are admitted — the platform preserves the clinic's control over patient flow. In team settings, checked-in patients can be transferred between providers without breaking the care process.

### The record lives elsewhere or beside

The encounter produces clinical documentation, but the platform is not necessarily the system of record: standalone tools keep session history and notes beside the EHR, embedded deployments write into the EHR directly, and service poles deliver summaries to the member and share records with their care system. Telehealth is the encounter-delivery layer, not the chart.

### Connectivity is a clinical risk

Real-world usage treats degraded audio/video as a clinical event, not an inconvenience: products and their guidance push adaptive quality, audio-only fallback, and pre-visit equipment checks, because a failed connection is a failed care delivery.

## Variants

The Type is realized in several recognizable forms. These are variants of one Type, not separate Types:

- **Standalone provider tool** — a clinician or small clinic adopts a virtual-room product; the practice keeps its own patients, schedule, and record (encounter delivery in isolation).
- **Embedded suite module** — telehealth ships inside a practice-management/EMR suite as a virtual visit location on the calendar, with claims and documentation in the same system.
- **Enterprise health-system platform** — the encounter machinery is embedded in the EHR, extended with consult routing across networks and fixed virtual-care hardware in facilities.
- **Vendor-operated care service** — the vendor runs the care process itself: members request care, the vendor's clinician network delivers it, and the platform is the service's delivery engine (D2C and payer/employer programs; specialist programs such as telestroke sit here).
- **Domain emphasis** — behavioral health (longer sessions, group therapy, specialty in-visit tools) vs primary/urgent care vs specialty consults; the emphasis shapes in-visit tooling and session conventions, not the core.
- **Regional/regulatory variants** — claim machinery, consent rules, and licensure models differ by jurisdiction; the core model is regime-neutral.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Video Conferencing Application | object is a meeting between participants; no patient/clinician binding, no care-delivery context, no clinical operations around the session. A conferencing product with healthcare compliance settings does not become a telehealth platform by posture alone — the care-delivery context is the seam. |
| Patient Scheduling | owns the booking machinery for capacity and calendars; telehealth consumes bookings as the entry into an encounter. Remove encounter delivery → Patient Scheduling. |
| Patient Portal | the patient-side access surface (records, messages, results); portals commonly link *into* telehealth visits without hosting the encounter. |
| Remote Patient Monitoring | continuous device-data collection between encounters; telehealth is the episodic encounter. RPM data may feed encounters, but the Types are distinct. |
| Practice Management System | the practice's business system of record (registration, scheduling, billing); telehealth is encounter delivery and is often packaged as a PM module — packaging does not merge the Types. |
| Electronic Health Record / EHR | the clinical record; telehealth delivers the encounter and drains documentation into the record (embedded deployments) or sits beside it (standalone tools). |
| Clinical Communication Platform | staff-to-staff communication for care teams; telehealth is patient-facing encounter delivery. |
| Virtual Classroom | same genus of scheduled remote sessions with a lead and attendees, but education domain: learners, not patients; no care-delivery context or clinical regulation. |

The sharpest boundary is with Video Conferencing Application, because both are live audio/video between two people. The difference is not the codec, the encryption, or the healthcare marketing — it is whether the encounter is organized and carried as clinical work: mediated entry, identified patient and provider in a care relationship, documentation and consent, regulated handling.

## Representative Products

- Doxy.me — standalone provider-side virtual-room tool (individual clinicians to clinics)
- SimplePractice (Telehealth) — telehealth embedded in a practice-management/EMR suite (private practices)
- Teladoc Health — vendor-operated virtual care service (members, employers, health plans, health systems)
- Amwell — enterprise health-system/payer platform with EHR-embedded visits, consult routing, and virtual care hardware

## Sources

Research date: **2026-09-09**

Primary vendor surfaces:

- Doxy.me — https://doxy.me/ ; Help Center: https://helpcenter.doxy.me/en/ (Basic features, Waiting Room, Features and Apps collection)
- SimplePractice — https://www.simplepractice.com/telehealth/ ; Support: https://support.simplepractice.com/hc/en-us (Getting started with telehealth; Telehealth & ePrescribe category)
- Teladoc Health — https://www.teladoc.com/ (individuals / organizations / clinicians pages)
- Amwell — https://business.amwell.com/ ; https://business.amwell.com/the-amwell-platform/

> Sourcing limitation: a generic videoconferencing product marketed to healthcare (Zoom for Healthcare) could not be fetched in this pass (knowledge-base article served no content; product page returned 404). Boundary statements toward conferencing therefore rest on the structural seam (care-delivery context) and market naming rather than on a researched in-sample product, and no Zoom-specific claims are made. One sampled vendor's operational help documentation (Teladoc) was not directly reachable; observations for that vendor are limited to its public product pages, and no precise operational details are asserted. Precise numeric limits, plan-gated features, and region-specific claim codes are intentionally not stated in this document; they remain in the paired Research Notes.

Detailed evidence, product-by-product observations, cross-product comparison, packaging-pole analysis, and the historical/regional check are recorded in the paired Research Notes.
