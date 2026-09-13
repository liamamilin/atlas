# Research Notes — Patient Scheduling

Research date: **2026-09-08**

## Research Goal

Understand, from real products, what Patient Scheduling software actually is and how it works:

- what the core objects are (appointment, patient, provider, service/visit type, availability, slot, location/room, appointment lifecycle states)
- who uses it and on which surfaces (front-desk/registration staff, providers, administrators, patients self-serving)
- how the booking loop runs (service & provider setup → availability → slots → booking → confirmation → check-in → completion/cancellation)
- how it relates to the provider's record systems (EHR/PM schedule of record; write-back vs native module vs enterprise layer)
- what rules govern it (capacity, conflicts, status transitions, provider gating, future-only booking, override behavior)
- where the boundary lies against Appointment Scheduling Application, Practice Management/EHR, Hospital Management System, Patient Registration & Intake, Patient Engagement, Patient Portal, Patient Flow/Bed & Capacity, Referral Management, Employee Scheduling / Resource Calendar, Telehealth, and service marketplaces

**Special obligations from prior passes (STATUS.md):**

1. **hospital-management-system pass (2026-09-08)** — pre-hung seam: patient-registration-intake + patient-scheduling are "capability slices" of hospital systems in some deployments; this pass must hold the seam (why a standalone Type is justified) and keep assertions about the enterprise/hospital pole weak.
2. **patient-registration-intake pass (2026-09-08)** — recorded: "Scheduling owns slot inventory and booking — upstream of intake; intake begins once a visit exists (or at walk-in arrival); commonly bundled." This pass must discharge that seam from the scheduling side.
3. **appointment-scheduling-application pass (2026-09-06)** — recorded: "vs Patient Scheduling (§22) — the clinical variant: the appointment is an encounter inside a clinical record system with provider licensure, referral, and insurance semantics. Generic appointment scheduling lacks clinical semantics; HIPAA options are an overlay, not a transformation." This pass must ratify or refine that split from the clinical side.
4. **appointment-based-service-business-management / med-spa / beauty passes** — recorded "regulated cousin" rows (appointments become clinical encounters inside medical-record and insurance semantics); consistent treatment expected here.

## Initial Boundary (hypothesis before research)

Working hypothesis: the provider-side system that manages clinical appointment capacity — defining what services/providers can be booked, computing when patients can be seen, booking identified patients into those slots (by staff and increasingly by patients themselves), and managing the appointment through arrival and completion as an operational record inside the provider's care-delivery system. Nearest confusing neighbors: Appointment Scheduling Application (§03.09 — same booking machinery, no clinical anchoring), Practice Management/EHR (which contain the appointment book as a module), Hospital Management System (which bundles it at hospital scale), Patient Registration & Intake (downstream), Patient Engagement/Portal (adjacent loops and windows), Patient Flow/Bed Management (arrival-time operations).

Key risks identified up front:

- Risk of collapsing into "a capability slice of EHR/PM/HMS" — must verify the standalone market and articulate why the Type stands alone.
- Risk of over-fitting to the modern US self-booking pattern (booking links, SMS, eligibility checks) — historical and regional check needed (paper appointment book, hospital OPD sessions, staff-side booking).
- Risk of boundary confusion with the processed §03.09 Appointment Scheduling Application — the two Types share the entire slot/booking machinery; the discriminator must be clinical anchoring, not labels.

## Research Questions

1. What objects exist in the system? (appointment; patient; provider; service / speciality / visit type; service appointment type; availability windows; slots; locations; rooms/operatories; blocks; recalls)
2. How is bookable capacity produced? (provider working hours vs service session times vs EHR-native schedules; max-load vs duration-based slot counts; blocks and time-off; conflict checks)
3. How does a booking happen? (staff-side booking; patient self-booking; walk-in marking; guardian/dependent booking; what is mandatory: patient identity, service, time)
4. What lifecycle does the appointment travel? (states, who changes them, transition rules, reschedule/cancel/missed semantics, what happens at completion)
5. How does the appointment connect to the clinical record? (native module inside EMR; write-back with procedure-code descriptors; display in patient dashboard)
6. What rules are load-bearing? (future-only booking; provider "available for appointments" gating; type-to-availability binding; overridable warnings; slot counts as advisory vs enforced)
7. Where do coverage/insurance, reminders, recalls, waitlists sit — defining or attached?
8. Boundaries: vs the processed neighbors listed above.

## Representative Products

Selected for market representativeness, philosophical diversity, and customer-tier diversity (all three are standalone scheduling offerings or a standalone scheduling module whose center is patient appointment management):

1. **NexHealth** — the SMB/mid-market practice pole (dental and medical): a "patient experience platform" whose scheduling engine runs **on top of** dozens of external PM/EHR systems through a bidirectional "Synchronizer," with a fully documented public API. Philosophy: keep the practice's record system, add a synced real-time booking layer. Documentation quality is exceptional (Tier-1 developer docs), making it the strongest evidence source for the canonical object model.
2. **Kyruus Health Schedule** — the health-system/enterprise pole: patient self-scheduling grounded in managed provider data ("single source of truth"), integrated directly with Epic, Oracle Health, MEDITECH, athenahealth; pre-booking clinical validation; part of a care-access platform (Provider Data Management + Search + Schedule + Check-In). Philosophy: enterprise-wide access and patient–provider matching, provider-data-anchored.
3. **Bahmni (Appointment Scheduling module)** — the open-source hospital/low-resource pole (500+ sites, 50+ countries; OpenMRS-based EMR+HIS): scheduling as a **native module inside the EMR/HIS**, staff-operated, service-session-oriented (OPD clinics, diagnostics), no patient self-service and no payer machinery. Philosophy: the hospital's own appointment book; also documents the "embedded realization" pole of the HMS capability-slice seam with public Tier-1 docs.

**Rejected / unreachable candidates:** Luma Health (lumahealth.io 403 — would have been the health-system engagement-suite pole; domain lumahealth.com is an unrelated Thai insurer), Zocdoc (403 ×2 — would have been the consumer marketplace pole), Solv (403 — consumer multi-provider booking pole). The consumer marketplace pole is therefore evidenced only indirectly (a NexHealth case study documenting a practice leaving Zocdoc's per-new-patient-booking-fee model). Phreesia's self-scheduling is covered as cross-pass evidence (its center is intake per the patient-registration-intake pass; scheduling is a bundled module).

## Sources

| Product | Source | Tier | Date |
|---|---|---|---|
| NexHealth | nexhealth.com homepage + product/feature navigation (Scheduling, Online Booking, Waitlist, One-Click Recalls, Reminders; Synchronizer positioning; case studies incl. Zocdoc-fee comparison) | Tier 2 | 2026-09-08 |
| NexHealth | docs.nexhealth.com: API index (llms.txt), Introduction, Scheduling Quickstart Guide, Scheduling Configuration Guide, resource reference (appointments, available slots, working hours, appointment types, appointment descriptors, operatories, patients, providers, patient recalls/recall types) | Tier 1 | 2026-09-08 |
| Kyruus Health | kyruushealth.com/solutions/schedule/ ("Online Patient Scheduling" product page + FAQ) and site navigation (Provider Data Management, Search, Check-In, EHR integration pages) | Tier 2 | 2026-09-08 |
| Bahmni | bahmni.org (product overview), Bahmni wiki: Feature Guide → Appointment Scheduling; User Guide → Appointment Scheduling in Bahmni → Creating and Managing Appointments | Tier 1 | 2026-09-08 |
| (cross-pass evidence) | research/patient-registration-intake.md, research/appointment-scheduling-application.md, research/hospital-management-system.md, related-types rows of patient-portal / patient-engagement-platform / patient-flow-management / bed-capacity-management / operating-room-management / dialysis-center-management / med-spa-management / clinical-trial-site-management | internal | 2026-09-08 |

**Source-access Limitation:** The consumer marketplace pole (Zocdoc, Solv) and the health-system engagement-suite pole (Luma Health) returned 403s; vendor help centers for the enterprise EHR pole (Epic-class) are login-gated per prior passes. Direct evidence therefore spans three poles (SMB booking engine, enterprise access layer, open-source hospital module), all official vendor surfaces, two of them Tier-1 operational documentation. Claims about the unreachable poles are kept out of the final document or marked as indirect. No vendor-claimed performance numbers (adoption counts, percentages, dollar figures) are carried into the final document.

## Product A — NexHealth (SMB practice pole; Tier-1 docs + Tier-2 site)

### Key observations (Evidence layer A)

- Positioning: "Patient Experience Platform — Scheduling, intake, and payments that sync to the patient record. Every appointment. Zero reconciliation." Products: Scheduling (Online Booking, Waitlist, One-Click Recalls), Communications (Messaging, Reminders, Campaigns, Reviews), Forms, Payments, Insurance Verification, Insights — all "Powered by the NexHealth Synchronizer."
- The Synchronizer connects to dozens of external PM/EHR systems (a published compatibility list includes Dentrix, Open Dental, Eaglesoft, Epic, athenahealth, eClinicalWorks, MEDITECH, and many more) — the practice keeps its record system; NexHealth syncs data in real time.
- **API object model (Tier 1, from the reference docs):**
  - Institution → Locations (a practice group and its brick-and-mortar offices).
  - Providers; Patients ("Create patient … returns an existing patient if return_existing_if_match is true" — identity matching is built into booking-adjacent flows).
  - **Operatories** — "the physical room (or chair) that the appointment will take place in. (Note: not all EHRs have the concept of operatories.)"
  - **Appointment types** — category records with a name and `minutes` (duration); "When your product asks the patient 'what are you scheduling for?', these are the categories it offers"; carry a `bookable_online` flag; can be bound to working-hour records ("what types of appointments a provider can be booked for" in which windows).
  - **Appointment descriptors** — the EHR's *native* appointment types and procedure codes (example: `D1110 — Prophylaxis Adult`), read from the practice's system; an appointment type can be mapped to a descriptor so a booked appointment "lands in the target health record system with the correct billing code"; descriptors "drive recall messaging and patient outreach."
  - **Working hours** — availability records binding provider × operatory × begin/end time × recurrence (`days`, `specific_date`, or `custom_recurrence`); lunch modeled as a gap between two records; base hours (`label: null`) vs labeled blockout-type hours in synced mode.
  - **Calendar unavailabilities / blocks** — "discrete blocks of time on a provider's calendar that mark the time slot as unavailable"; returned as appointments with `unavailable: true` and `patient_id: null`; automatically excluded from slot search.
  - **Available slots** — "bookable slots … computed from provider availabilities and existing appointments"; slot length from the appointment type's duration or a slot interval; supports `next_available_date`.
  - **Appointments** — create ("books an appointment for the given patient with the given provider at the specified location"; `is_guardian` flag books for a dependent with the guardian providing the patient object; setting `unavailable=true` creates a block instead), edit, list by window.
  - **Patient recalls / recall types** — "A patient recall is a reminder … when it's time to come back in for a follow-up visit, check-up, or preventive care appointment"; recall types carry intervals per patient; one-click recall booking is a flagship feature.
- Scheduling Quickstart (Tier 1): booking requires a patient, a provider, an operatory, start/end time, and institution/location; after booking through the API against a real Open Dental instance, "you should see the appointment appear on the Open Dental schedule (within less than a minute)" — the write-back into the practice's schedule of record is the demonstrated happy path.
- Scheduling Configuration Guide (Tier 1): two configuration postures — **manual** (the application configures working hours through the API; "the shape is identical across every health record system") vs **synced** ("NexHealth reads the schedule directly from the practice's health record system. The practice manages it through their existing workflow"), supported for a listed set of systems; slot derivation = working hours (source of truth) − calendar unavailabilities − existing bookings, cut by appointment-type duration; type-to-window binding means "a request for Cleaning availability only evaluates the 9:00–12:00 window."
- Marketing layer (Tier 2): online booking synced to the record system; waitlist "fills last minute openings"; one-click recalls; automated reminders; case study contrasting NexHealth's pricing with Zocdoc's per-new-patient booking fees (the only evidence obtained about the consumer marketplace pole).
- Vendor-claimed numbers (20,000+ practices; 75% of admin tasks automated; case-study revenue figures) — recorded here with attribution only, excluded from the final document.

**Reading:** the scheduling engine as a *syncing layer over the practice's schedule of record*: availability machinery (working hours, blocks, operatories), typed bookable offerings (appointment types with durations, mapped to the EHR's own appointment types/procedure codes), computed slots, booking with patient identity (including guardian bookings), and lifecycle operations — with recalls tying scheduling to the care-recurrence cycle.

## Product B — Kyruus Health Schedule (health-system/enterprise pole; Tier 2)

### Key observations

- Page: "Online Patient Scheduling — Patient self scheduling made easy … based on real-time, accurate provider availability—integrated with Oracle Health, Epic, MEDITECH, and athenahealth EHRs." Part of Kyruus Connect ("the care access platform for provider organizations"), whose Provider Data Management is "the single source of truth to manage and utilize provider data."
- The vendor's own FAQ defines the Type's mechanics: "An online patient scheduling solution is a tool that integrates with a provider's electronic health record (EHR) system to display real-time appointment availability for providers and services … patients can view and book appointments … and easily reschedule or cancel appointments digitally, eliminating the need to call the office."
- Integration FAQ: "Online scheduling solutions integrate with existing practice management systems through secure, real-time data exchange … access to up-to-date provider availability, appointment types, and scheduling rules directly from the practice management system (PMS). When a patient books an appointment online, the system writes that appointment back into the practice's native scheduling system, ensuring accuracy, avoiding double-booking."
- **Pre-booking clinical validation**: "Ensure accurate patient routing with clinically validated pre-booking workflows that pair care needs with clinical expertise"; "templated or custom pre-booking validation questions based on … proprietary clinical taxonomy of 35,000+ terms—ensuring no one's time is wasted as patients are routed correctly."
- Customization FAQ: providers control which appointment types are bookable (e.g., only new-patient appointments), scheduling rules (availability opening N days out "to allow time for necessary paperwork"), bookable days and locations; "mapping of visit types between the practice management system and consumer-facing options."
- Service breadth: "patients aren't always looking for a specific doctor … many solutions also enable scheduling for services like annual mammograms, flu shots, lab work, and urgent care visits" — services, not just provider visits.
- Enterprise framing: unify Search + Schedule within "your organization's digital front door"; "aggregates enterprise-wide scheduling data in real time" to "align network capacity and patient demand"; new-patient acquisition through the Kyruus Network.
- Reminders FAQ: automated reminders via email/SMS/app reduce no-shows; HIPAA compliance posture stated.
- Vendor-claimed numbers (5M+ appointments scheduled; 1-in-3 outside business hours; 36% new patients; a health-system client's first-six-months figures) — recorded with attribution only, excluded from the final document. (2026 corporate note: Kyruus Health announced joining RevSpring — branding context only.)

**Reading:** the enterprise realization of the same structure — real-time availability pulled from the EHRs of record, write-back into the native scheduler, appointment types/visit-type mapping, plus an enterprise-specific layer: managed provider data and clinically validated pre-booking questions that route the right patient to the right provider before a slot is consumed.

## Product C — Bahmni, Appointment Scheduling module (open-source hospital pole; Tier 1)

### Key observations

- Bahmni is an open-source EMR & hospital system (OpenMRS distribution) for low-resource settings; hosted at the hospital site; modular ("choose parts of Bahmni").
- The Appointment Scheduling feature's own framing: "Patients are often given appointments to meet providers and consequently access the requisite care and services. By scheduling appointments, healthcare settings try to manage the schedules of various providers and services offered and also in streamlining the patient load."
- Bookable scope: "General OPDs or Specialised OPD services like a Diabetic Clinic or a Dental clinic; particular providers coming only on specific days and times of the week; a service like X-ray or Ultrasound scan; surgery slots in Operation theatres" — with Operation Theatre scheduling shipped as a **separate module**.
- Setup model: services are defined with availabilities ("Diabetic clinic runs every Monday 10.00 AM - 12.00 PM"); providers deliver services; only providers with the OpenMRS attribute "Available for appointments" set to true can be selected.
- **Creating an appointment (Tier 1, exact fields)**: Patient (mandatory; searched by name or ID), Speciality (optional/configurable), Service, Service Appointment Type, Walk-in flag ("By default appointments are marked as Scheduled"), Date ("Only current and future dates are allowed"), Time slot ("dropdown will suggest possible slot times based on service availability … End time will auto populate based on the duration of the service/service appointment type. Default of 30 mins if no durations are mentioned. Users can override the suggested times"), Provider, Location ("By default the location will be Service location").
- **Override behavior**: booking outside service availability warns; booking the same patient into overlapping times warns; "In both cases … the user can still go ahead and book an appointment by ignoring the warning."
- **Slot accounting**: open/total/booked slots computed from the service's max load or availability window+duration — and explicitly "only an indicative information for the user and will not stop the user from overbooking."
- **Lifecycle (Tier 1, exact rules)**: statuses Checked-in, Completed, Cancelled, Missed (plus default Scheduled, and a walk-in marking). "A 'Cancelled', 'Completed' and a 'Missed' Appointment should not be available for editing to change to any other status. A Scheduled appointment can move to any of the statuses. A 'checked in' appointment can only be marked as Completed, Missed or Cancelled. A checked-in Appointment if rescheduled, the status must go back to being 'Scheduled' until checked-in again for the rescheduled time." Past or terminal appointments allow only Notes edits.
- Users: Registration Clerk (assign appointments, check in patients), Provider (view/schedule, complete after consultation), Screener (track patient load, manage queues), Administrator (set up services and availabilities).
- Surfaces: summary page of patient loads across services; appointment list with filter panel; calendar view; add/edit panel; and an "Appointments Custom Display Control in Patient Dashboard" — the appointment is visible inside the patient's chart UI.
- The example narrative: "An appointment is created for a Patient for the Diabetes Clinic on Monday at 11.20 AM. Once the patient reaches the hospital, the patient would be checked in. The patient will be guided to the assigned provider. The appointment will be deemed completed after consultation … Alternately the appointment can also get cancelled or rescheduled … Also it is possible that the patient misses the appointment."

**Reading:** the *native-module* realization — no patient self-service, no payer machinery, no external sync: the hospital's own staff-side appointment book over clinical services and providers, with an explicit encounter lifecycle (check-in feeding the clinical flow) and per-service capacity accounting. This is also the evidence for the HMS capability-slice seam: the same structure embedded in a hospital system.

## Cross-pass corroboration

- **patient-registration-intake pass (2026-09-08)**: all four sampled intake vendors (Phreesia, Clearwave, Kyruus, Yosi) bundle **self-scheduling** as an adjacent module — independent confirmation that patient self-scheduling is the standard companion layer, and that scheduling owns "slot inventory and booking" upstream of intake.
- **appointment-scheduling-application pass (2026-09-06)**: sampled generic scheduling vendors position clinical-grade variants as out of their Type ("clinical-grade variants belong to Patient Scheduling (§22)"); HIPAA options are an overlay, not a transformation.
- **hospital-management-system pass (2026-09-08)**: hospital systems bundle scheduling as a capability slice; the seam was pre-hung for this pass to hold.
- Related-types rows already published by processed §22/§03/§09 neighbors (portal: "scheduling owns slot inventory and the booking system"; engagement: "owns slot inventory and booking … without owning the calendar"; flow/bed: "future time slots" vs "live, event-driven progression"/"beds in the present"; OR management: "the room and the surgical case are the center"; dialysis: "scheduling is one capability … no prescription, session record, or machine context"; med-spa/appointment-based: "regulated cousin").

## Cross-product Comparison

| Structure / capability | NexHealth | Kyruus Schedule | Bahmni (module) |
|---|---|---|---|
| Appointment binds patient × provider × defined service/type × time | ● (patient + provider + appointment type + times; guardian bookings) | ● (visit types; provider + service appointments) | ● (patient + provider + service + service appt type + time; walk-in flag) |
| Patient is an identified record, matched/created at booking | ● (create-or-match patient endpoint; guardian provides dependent details) | ● (patient context; new-patient flows) | ● (patient searched by name/ID — must exist in the EMR) |
| Bookable offerings are typed with durations | ● (appointment types with `minutes`; descriptor mapping to EHR procedure codes) | ● (appointment/visit types; mapping between PMS and consumer-facing options) | ● (service appointment types; auto end-time from duration; 30-min default; overridable) |
| Availability machinery | ● (provider working hours per operatory/day; manual or synced from the EHR) | ● (real-time availability from the EHRs; provider data kept current) | ● (service session availability; provider "Available for appointments" attribute) |
| Slots computed from availability − blocks − bookings | ● (`/available_slots` = working hours − unavailable blocks − existing appointments; next-available) | ● ("real-time appointment availability"; "aggregates enterprise-wide scheduling data") | ● (slot suggestions; open/total/booked from max load or availability) |
| Rooms/chairs as optional constraints | ● (operatories; "not all EHRs have them") | ○ (locations; rooms not named on page) | ○ (locations; service location default) |
| Write-back into the provider's schedule/record of record | ● (appointment "lands in the target health record system" with correct descriptor/billing code) | ● ("writes that appointment back into the practice's native scheduling system") | ● (appointment is native to the EMR; shown in patient dashboard) |
| Managed lifecycle with status rules | ● (create/edit; cancel via product flows) | ● (book; "digitally reschedule or cancel") | ● (Scheduled→Checked-in→Completed/Missed/Cancelled with explicit transition validations) |
| Encounter-anchored statuses (checked-in → completed) | ○ (edit operations; no fetched status machine) | ○ (not on fetched pages) | ● (explicit; check-in is a clerk duty) |
| Patient self-service booking | ● (online booking; `bookable_online` flag) | ● (24/7 self-scheduling; "reschedule or cancel … without picking up the phone") | — (staff-side only in the classic module) |
| Pre-booking clinical screening/matching | ○ (type-to-window binding constrains what is bookable) | ● (clinically validated pre-booking questions; clinical taxonomy; patient–provider matching) | — |
| Reminders | ● (automated reminders product module) | ● (FAQ: reminders via email/SMS/app) | — (not on fetched pages) |
| Waitlist / cancellation backfill | ● (Waitlist fills last-minute openings) | ○ ("surfacing openings" framing) | — |
| Recall / recurrence machinery | ● (recall types with intervals; one-click recall booking) | — (not on fetched pages) | — |
| Coverage/insurance semantics | ○ (insurance coverages/balances in API; Verification sibling product) | ○ (not on Schedule page; payer-side products exist in suite) | — (billing separate module) |
| Multi-location / multi-provider | ● (institution → locations) | ● (enterprise-wide; days/locations bookable controls) | ● (locations; multi-department services) |
| Staff-side booking | ● (via product/API; Synchronizer) | ● (front-desk/call-center relief framing) | ● (primary mode) |
| No payer machinery anywhere in the module | — (Verification/insurance APIs present) | — | ● (none; single-payer/self-pay contexts) |

● = directly observed on official surfaces; ○ = partial/indirect; — = not observed.

### What repeats across all three poles (candidate core)

1. **The appointment is a binding of an identified patient × provider × defined clinical service/visit type × time**, held in or reconciled into the provider's scheduling/record system. The patient is never anonymous; booking either matches/creates a patient record or requires one to exist.
2. **Bookable capacity is computed, not hand-drawn**: provider schedules/working hours, service session times, durations of appointment types, blocks/unavailabilities, and (optionally) rooms/locations combine into open slots; slot counts and conflict warnings manage load.
3. **Appointments carry a managed lifecycle** ending in an encounter-relevant outcome (completed / cancelled / missed), with status rules governing transitions; the record feeds the provider's clinical/operational flow (provider queues, patient load, chart).
4. **Clinical typing of time**: appointment/visit types (with durations) are the categories patients book; they can be constrained by provider, by availability window, by location — and in the EHR-integrated poles they map to the provider's own native appointment types/procedure codes.
5. **The provider's system of record stays authoritative**: whether the scheduler is a syncing layer (NexHealth), an enterprise access layer (Kyruus), or a native module (Bahmni), the appointment lands in (or is) the practice's schedule of record; avoiding double-booking is the explicit reason.
6. **Staff-side booking is universal; patient self-booking is the modern additive layer** — present in two of three poles, absent in the third, and absent from the historical paper book.

### What varies (candidate variant axes)

- Who books: staff-side (Bahmni pole) vs patient self-service-first (Kyruus, NexHealth) vs third-party marketplace (unreachable pole, evidenced indirectly).
- Relationship to the record system: native module vs bidirectional sync overlay vs enterprise access layer over multiple EHRs.
- Capacity model: service sessions with max load (Bahmni) vs provider working hours cut into typed slots (NexHealth) vs EHR-native availability surfaced in real time (Kyruus).
- Enforcement posture: advisory capacity with staff override (Bahmni's warnings; "will not stop overbooking") vs hard slot computation (NexHealth API).
- Clinical depth of pre-booking logic: none (Bahmni) vs type/window constraints (NexHealth) vs clinically validated question sets and matching (Kyruus).
- Customer tier: single practice / dental group (NexHealth) → specialty groups & health systems (Kyruus) → hospitals in low-resource settings (Bahmni).

## Abstraction Hierarchy

### L0 — Defining Invariant

Three jointly-held structures:

1. **The clinical appointment of record.** A persistent, identified booking binding an **identified patient × provider × defined clinical service/visit type × time**, held in or reconciled into the provider's scheduling/clinical system of record. The patient exists as a clinical record (matched or created, never anonymous); the service is a defined clinical offering (a visit reason with duration); the provider is a clinical actor whose availability and scope gate what can be booked. *Remove the patient-record anchoring and clinical typing → a generic appointment scheduling application; remove defined services → a blank calendar.*

2. **Availability-derived bookable capacity.** The system computes when patients can be seen — from provider schedules/working hours, service session times, appointment-type durations, blocks/time-off, and optionally rooms/locations — and manages booking against that computed capacity (open slots, next-available search, open/total/booked accounting, conflict and availability warnings). *Remove the computation → request-taking or a hand-drawn diary; the "management" collapses.*

3. **The encounter lifecycle loop.** The appointment travels an explicit state path — booked → arrival (check-in) → completed, with cancelled and missed as first-class outcomes — under transition rules (what may change in which state), and its outcomes feed the provider's clinical/operational flow (provider queues, patient-load views, the chart). *Remove the lifecycle → static calendar entries; nothing flows into care delivery.*

**Jointly-held load-bearing analysis:**

- 1 alone = an appointment log/ledger with no capacity logic (an ADT-style booking list)
- 2 without 1+3 = free-busy publishing / a resource grid (no patients, no follow-through)
- 3 without 1+2 = a generic task board
- 1+2 without 3 = a one-shot booking form (slots consumed, nothing tracked to the encounter)
- 1+3 without 2 = the front-desk diary booking into hand-drawn space (historical precursor)
- 2+3 without 1 = employee/resource scheduling (staff-to-shifts, rooms-to-times)

**Historical / market-sample check:** the paper appointment book satisfies all three legs with none of the modern machinery: the pre-printed slot grid is the availability template (leg 2, realized statically), the written entry naming patient/service/provider/time is the appointment of record (leg 1), and the pencil line-outs, reschedule arrows, no-show marks, and check-in lines are the lifecycle (leg 3). Hospital OPD session books and public-system GP booking satisfy the same legs without payer machinery. The definition therefore names no patient self-service, no SMS/reminders, no insurance/eligibility APIs, no cloud, no marketplace, no era machinery. **Anti-overfit:** patient self-booking is NOT definitional (Bahmni's module is staff-only and fully in-type; the paper book is the historical pole); insurance/eligibility capture is NOT definitional (single-payer and self-pay contexts schedule patients without it; absent from the Bahmni module); marketplace discovery is NOT definitional; multi-location/cloud/AI are NOT definitional.

**Divergence from the §03.09 family signature, recorded deliberately:** in the Appointment Scheduling Application Type, client-initiated self-booking is the defining loop. In Patient Scheduling it is not — the defining loop is the managed clinical appointment book itself (who is coming, for what service, with which provider, and how the encounter progresses), with self-booking as the dominant modern access layer. This is corroborated by the sample (a full in-type pole without self-booking) and by history (the paper book).

### L1 — Common Mature Structure

Present in most mature products; not required to recognize the Type:

- patient self-service booking (web/portal/app) over real-time availability, with provider/service selection and slot picking
- automated confirmations and reminders (SMS/email/app), commonly with self-service reschedule/cancel links and two-way messaging
- waitlists with automatic backfill of cancellations
- recall / recare machinery (recall types with intervals; one-click recall booking) driving preventive-care cycles
- appointment-type configuration: durations, buffers, lead times, booking windows, online-bookable flags
- per-provider schedule management; assignment of appointment types/services to providers and availability windows
- synchronization with (or native presence in) the practice's PM/EHR schedule of record; double-booking prevention; visit-type/descriptor mapping
- multi-provider and multi-location operation; rooms/chairs (operatories) as optional constraints
- visit reason capture; pre-booking screening questions; new-patient routing and provider matching (specialty/insurance-accepted) in enterprise deployments
- coverage capture at or around booking (market-dependent)
- reporting: no-shows, utilization, patient load, booking-channel performance
- telehealth visits as appointment types alongside in-person ones

### L2 — Variant / Optional Structure

- consumer marketplace discovery pole: patients search providers by specialty/insurance/location across many practices and book; providers pay for exposure (indirect evidence only this pass — unreachable vendor docs)
- enterprise access layer: managed provider data as the scheduling foundation; enterprise-wide aggregation across sites/EHRs; search+schedule "digital front door" bundling
- open-source hospital module: scheduling embedded in an EMR/HIS; service-session orientation; staff-only operation
- engagement-suite bundling: scheduling wrapped with intake, communications, payments, reviews (the "patient experience platform" packaging)
- specialty reshapes: dental recare-driven scheduling, physical-therapy plan-of-care series, behavioral-health recurring appointments; dialysis/infusion chair scheduling (becomes its own Types where prescription/machine/session-record context enters)
- payments/deposits/no-show fees at booking (market-dependent)
- AI scheduling assistants and conversational booking (2026-era)
- multi-language patient experience; accessibility posture

### L3 — Vendor-specific (research notes only)

- **NexHealth:** Synchronizer bidirectional-sync architecture and per-EHR compatibility list; "appointment descriptors" as a distinct resource mapped from NexHealth appointment types to EHR-native procedure codes (e.g., D1110 — Prophylaxis Adult) that drive billing and recall messaging; manual vs synced working hours (per-system support list; "mixing … creates overlapping records"); operatories with the "not all EHRs have them" caveat; `is_guardian` dependent booking; `bookable_online` flags; `next_available_date`; slot-derivation gotchas (unbound types return no slots; operatory scoping).
- **Kyruus Health:** proprietary clinical taxonomy (35,000+ terms) behind pre-booking validation; Search/Schedule/Check-In suite composition atop Provider Data Management; Kyruus Network acquisition framing; Epic/Oracle Health/MEDITECH/athenahealth integration pages; RevSpring merger banner; all performance claims.
- **Bahmni:** service max-load vs availability-based slot-calculation table; configuration toggles that can turn off the speciality/service layers; OpenMRS "Available for appointments" provider attribute; walk-in flag semantics; the explicit "indicative only — will not stop the user from overbooking" caveat; separate Operation Theatre Scheduling module; version history of the module (0.90/0.91).
- **Zocdoc (unreachable):** per-new-patient booking fee model referenced only via a NexHealth case study — no first-hand claims recorded.

## Rejected Findings

- **"Patient scheduling = online self-booking for patients."** Rejected: a full sampled pole (Bahmni) operates staff-side only and is squarely in-type; the historical paper book had no self-service. Self-booking is the dominant modern access layer (L1), not the definition.
- **"Patient scheduling is just appointment scheduling with medical labels."** Rejected as identity: the clinical anchoring changes the object set and the rules — patients are matched clinical records (never anonymous leads), services carry clinical durations/types and can map to procedure codes, the lifecycle ends in encounter-relevant outcomes (checked-in/completed/missed) that feed care operations, and the record system of record is the practice's clinical schedule. Keep-both with the §03.09 sibling on the clinical-anchoring test (gradient acknowledged: generic tools hosting a "patient appointment" event type sit on the far side of the seam).
- **"Scheduling is a mere capability slice of EHR/PM/HMS — not a Type."** Rejected as identity; held as the embedded realization: the HMS pass itself pre-hung the seam rather than merging. The standalone market is evidenced across three poles with a stable standalone object set, and embedded realizations (Bahmni; Epic-class, weakly) satisfy the same L0.
- **"Insurance/eligibility verification is definitional."** Rejected: absent from the Bahmni module and from historical/public-system contexts; the intake pass reached the same conclusion for its Type. Coverage capture is market-dependent (L1/L2).
- **"Recalls/recall cycles are definitional."** Rejected: Tier-1 evidence from one product only (NexHealth); absent from the Bahmni module pages; common in some specialties (dental), not universal. Held as L1 with single-product depth noted.
- **"Rooms/equipment scheduling is the center."** Rejected: operatories/locations appear as optional constraints on booking in all sampled poles; when the room and its session are the managed center, the product belongs to Operating Room Management or resource scheduling.

## Boundary Findings

| Neighbor Type | Relationship | Distinction (what to remove/keep) |
|---|---|---|
| Appointment Scheduling Application (§03.09, processed) | sharpest sibling — JOINT SEAM DISCHARGED from this side | Generic scheduling centers a **service business's bookable offerings** with the **client-initiated self-booking loop** as the family signature and appointment policies (deposits, cancellation windows). Patient Scheduling centers the **clinical appointment of record**: patients are matched clinical records, services are clinical offerings (mapping to native visit types/procedure codes), the lifecycle ends in encounter outcomes, and the practice's clinical schedule is the record of record — self-booking common but not required. Remove clinical anchoring → appointment scheduling; add clinical anchoring → this Type. HIPAA options stay an overlay (per that pass). Keep-both ratified. |
| Practice Management System / EHR | contains the appointment book as a native module | PM/EHR hold the clinical record and business administration; scheduling is one module among many. The standalone Type exists where scheduling/access machinery (availability engines, self-booking, waitlists, recalls, enterprise scheduling layers) is the product's center. Embedded scheduling modules remain in-type realizations. |
| Hospital Management System (§22, processed) | embedded realization context — seam HELD per that pass | An HMS bundles appointment demand management among ward/lab/pharmacy/billing functions; Bahmni documents exactly this embedded pole. The standalone Type is justified by the dedicated vendor population (SMB engines, enterprise access layers) and the stable standalone object set. Enterprise/Epic-class pole kept at weak assertions (no reachable operational docs, consistent with prior passes). |
| Patient Registration & Intake (§22, processed) | downstream sibling — seam DISCHARGED from this side | Scheduling owns slot inventory and booking; intake begins once a visit exists (or at walk-in arrival) and prepares that visit (packet, consents, coverage). Intake vendors bundle self-scheduling as an adjacent module — bundling, not identity. Remove slot management and the booking loop → intake; add them → this Type. |
| Patient Engagement Platform (§22, processed) | adjacent loop | Engagement runs the **ongoing provider-initiated loop** across visits (campaigns, outreach, journeys); scheduling owns the slot/encounter machinery; reminders and self-schedule links are the interlock. Remove the booking core → engagement; remove the ongoing loop → this Type. |
| Patient Portal (§22, processed) | entry point vs inventory | The portal is the patient-initiated longitudinal window onto records and services; scheduling owns the slot inventory the portal links into. Portal-hosted booking is a delivery surface, not the Type's center. |
| Patient Flow Management / Bed & Capacity Management (§22, processed) | future slots vs live operations | Scheduling books patients into future time slots in advance; flow/bed manage live, event-driven progression and present-tense bed state after arrival. Check-in is the handoff event between them. |
| Referral Management (§22, unprocessed) | upstream feeder | A referral is the clinical instruction/order that establishes the need for care; scheduling converts an existing need into a booked encounter with a provider. Forward flag: referral-native routing may bundle booking — expect the "instruction/order of record vs slot booking" seam. |
| Employee Scheduling Platform (§09, processed) / Resource Calendar (§03.08, processed) | different bound object | Employee scheduling binds **staff to shifts** (the roster is the artifact); resource calendars are calendars owned by bookable things. Patient scheduling binds **patients into clinical capacity** (the appointment is the artifact; provider schedules are inputs). |
| Telehealth Platform (§22) | visit medium vs booking | Telehealth delivers the remote visit; scheduling books it. A telehealth slot is one appointment type here. Telehealth vendors bundling booking stay telehealth-centered unless the booking machinery becomes the center. |
| Service Marketplace (§05.02) / consumer discovery | third-party pole adjacency | A consumer marketplace curates multi-provider choice and patient acquisition (the unreachable Zocdoc/Solv pole); scheduling is provider-side capacity management. Where discovery across many independent providers is the center, the product is a marketplace; booking rides on scheduling. Evidence this pass: indirect only. |
| Calendar Application (§03.08, processed) | personal time vs organizational clinical capacity | A calendar manages a user's own events; patient scheduling manages an organization's clinical booking capacity, typed services, and encounter lifecycle. Provider calendars feed availability; they are not the artifact. |

## Uncertainties

- **Consumer marketplace pole unverified:** Zocdoc and Solv returned 403s (×2 each); Luma Health also 403. The marketplace pole's internals are documented only via the NexHealth case study (Zocdoc per-booking fees). No structural claims about it appear in the final document beyond the market's existence.
- **Enterprise hospital pole weak:** Epic Cadence-class scheduling is documented only indirectly (cross-pass HMS evidence; Kyruus/NexHealth integration claims). Assertions about that pole are kept at realization level.
- **Reminder commonality:** confirmed by Kyruus FAQ + NexHealth product module; not documented on the fetched Bahmni pages. Held common-not-definitional.
- **Recall machinery depth:** single-product Tier-1 evidence (NexHealth). Held L1.
- **Appointment state labels:** Bahmni documents an explicit status machine; the API-integrated poles document edit/cancel operations rather than a public state machine. Canonical states written conceptually ("booked → arrived → completed, with cancelled/missed outcomes"); exact labels vary.
- **Payment-at-booking:** NexHealth ships payments as a sibling module (not scheduling-native on the fetched pages); deposits/no-show fees are market-dependent (L2). Not asserted as definitional anywhere.
- **Enforcement posture spread:** Bahmni's advisory capacity + staff override vs NexHealth's hard slot computation — both documented Tier-1; the final document presents override behavior as a designed spectrum, not a universal rule.

## Final Synthesis

Patient Scheduling software is the provider's system for managing clinical appointment capacity. Its defining structure is the jointly-held trio: (1) the **clinical appointment of record** — an identified patient booked with a provider for a defined clinical service/visit type at a time, matched to (or required to exist in) the provider's clinical records and held in or written back to the practice's schedule of record; (2) **availability-derived bookable capacity** — computed open slots produced from provider schedules, service session times, appointment-type durations, blocks, and optionally rooms/locations, with load accounting and conflict management; and (3) the **encounter lifecycle loop** — booked → checked-in → completed (cancelled/missed as first-class outcomes) under explicit transition rules, feeding provider queues, patient-load views, and the chart. Around that core, mature products add patient self-service booking over real-time availability, reminders and two-way messaging, waitlists with cancellation backfill, recall/recare cycles, typed-offering configuration with EHR visit-type/procedure-code mapping, multi-provider/multi-location operation, pre-booking clinical screening and patient–provider matching, coverage capture, and reporting. The market realizes the Type as native EHR/HIS modules (the embedded pole), bidirectional-sync booking engines over existing PM/EHR systems (the SMB pole), enterprise access layers grounded in managed provider data (the health-system pole), and consumer marketplace discovery surfaces (a third-party pole, indirectly evidenced). Remove the clinical anchoring and it collapses into generic appointment scheduling; remove the slot computation into a diary; remove the lifecycle into a calendar; remove the patient and it becomes employee/resource scheduling.
