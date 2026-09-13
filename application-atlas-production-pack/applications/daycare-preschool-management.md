# Daycare / Preschool Management

> A note on naming: the market sells this software as "daycare management software", "preschool management software", and "childcare management software" — often as separate landing pages that all lead to one product. This document describes that product family from the daycare-and-preschool-program angle; the sibling atlas entry **Childcare Management System** describes the same family from the business-type angle. The overlap is recorded in the atlas status for a directory-level decision.

## Overview

A **Daycare / Preschool Management** application is operator-side software for running a daycare center or preschool — a licensed early-childhood business that holds other people's children in care for a substantial part of the day. It keeps the operator's system of record: which children are enrolled and under whose authority, which children are present right now and with whom they may leave, what happened during each child's day, what the staff covered, and what the family (or a subsidy payer) owes.

The defining core is small:

```text
Guardian/family account
└── Enrolled child (ongoing care enrollment)
    ├── Daily attendance recorded as custody events (check-in / check-out by authorized adults)
    └── Care-day documentation shared with guardians
```

Everything else commonly bundled with these products — classrooms with ratio monitoring, tuition autopay, subsidy billing, waitlists, parent apps, curriculum and progress reporting — is standard capability layered onto that loop to make it workable in a licensed, revenue-collecting business.

When the software instead matches families with individual caregivers, it is a Babysitting Marketplace; when the programs it manages are scheduled part-day sessions around the school day, it is After-school Program Management; when those sessions become seasonal and consecutive-day, it is a Camp Management System.

## Users & Context

**Primary operator-side users:**

- **Director / owner / administrator** — the main seat of the software. Owns the enrollment pipeline, family and child records, tuition billing, staff records and schedules, compliance reporting, and multi-site oversight.
- **Teachers / caregivers / early-years educators** — work at the room level: perform the custody handover at the door, log the day as it happens, message families, and see their room's roster and ratio. Their visibility is deliberately narrower than administrators' — typically no financial data.
- **Front-desk staff** — operate the check-in station, handle walk-in inquiries, and manage same-day custody exceptions.

**Primary participant-side users:**

- **Guardians (parents/families)** — the contracting, paying, and communicating counterparty. They complete enrollment paperwork, pay tuition, receive the care-day documentation, and perform the custody handover itself at drop-off and pick-up, usually with an app credential at the door. Other authorized adults (relatives, approved pickup people, emergency contacts) hold narrower, custody-oriented access.

**Typical contexts:** a licensed daycare or child care center; a preschool or early-education program with a learning curriculum; a nursery or childminder setting (UK naming for the same things); a Montessori or faith-based program; a state-funded program with heavier reporting; a home-based provider running the same loop without rooms; or a multi-site group.

## Core Model

### The Defining Core

Three structures. If any one is removed, the software stops being recognizable as this Type:

- **Enrolled child bound to a guardian/family account.** The child is the cared-for person and the operator's central record; the guardian account is the one that logs in, pays, and communicates. Enrollment is an ongoing care relationship — a child stays enrolled until the family withdraws or the child moves up — not a booked session or a term registration. This child-plus-guardian shape is what separates the Type from adult-facing booking or membership software.
- **Daily care attendance recorded as custody events.** Each care day is recorded through check-in and check-out performed by authorized adults. The event is at once an attendance record (the child is present), a custody record (this authorized adult handed the child over, and this one may take the child away), and the raw input for ratio monitoring and billing. Without it, the system cannot answer the question every care operation must answer continuously: which children are in care right now, and with whom may they leave?
- **Care-day documentation shared with guardians.** The operator records what happened during the child's day — meals, naps, toileting, activities, photos, notes, medication, incidents — and shares it with the child's guardians. This loop is the defining communication structure of care: the operator holds the child during the day and hands back both the child and an account of the day. It predates software (paper daily sheets) and is the primary family-facing surface of every product in the category.

```text
Guardian/family account
  └── Enrolled child (ongoing care enrollment)
        ├── Daily attendance: check-in / check-out (custody events by authorized adults)
        ├── Care-day documentation (meals · naps · toileting · activities · photos · notes · incidents)
        └── Tuition ledger (charges · payments · subsidies)
Rooms / classrooms (children + staff assigned; capacity + ratio)   [center settings]
Staff records & schedules ──┘
```

### Standard Capabilities Around the Core

Mature products commonly add the following. They make the core loop workable in a real licensed business but do not define the Type:

- **Rooms/classrooms with capacity and ratio monitoring** — children and staff assigned to rooms; a capacity limit and desired staff-to-child ratio per room; live ratio views, out-of-ratio warnings, and ratio history for licensing. This organizes center-based care, but it is segment-dependent: home-based providers run the same core loop without rooms.
- **Custody machinery** — per-child lists of authorized adults, contact types (parent, family, approved pickup, emergency contact), check-in codes or digital signatures or scan credentials at the door, controls to block unauthorized pickups, and optional health screening at drop-off.
- **Tuition billing and the family ledger** — recurring billing plans (weekly, monthly, other frequencies), schedule- or attendance-based billing, drop-in charges, deposits, discounts, late-payment handling, automatic payments, charges split between multiple payers, statements and year-end tax documents.
- **Third-party and subsidy money** — billing split between the family and an external payer (a government subsidy agency, a funding scheme, or an employer), with agency payment posting, co-pays, adjustments, and — in some markets — attendance and meal data reported to government systems.
- **Enrollment pipeline machinery** — inquiries and leads, tours, applications, waitlists, and admissions packets bundling forms, contracts, handbooks, document requests, and fees; enrollment statuses carrying each child from prospect to active to graduated, with history retained for licensing.
- **Health and safety records** — immunizations and requirements, medications administered, incident reports, daily health checks.
- **Meals** — menus, per-child meal records, meal counts, and food-program reporting where reimbursement applies.
- **Staff management** — staff records, room assignments, schedules or rotas, time cards, and staffing views that compare child schedules against staff schedules room by room.
- **Family engagement surfaces** — a guardian app or portal: the daily feed, photos and videos, messaging, newsletters, calendars.
- **Learning documentation** — observations mapped to early-learning frameworks, assessments, milestones, lesson plans or bundled curriculum, and progress reports to families. This layer exists across the whole category; it is simply deepest in preschool deployments.
- **Reporting** — attendance, ratios, enrollment, revenue, and family-account views, framed around what licensing authorities and the business need.
- **Multi-site management** — several locations under one organization with consolidated oversight.

### Daycare and Preschool Are Emphasis Poles, Not Two Systems

The same records serve both. A daycare center runs the loop with care logistics at the center — meals, naps, diapering, ratios, custody. A preschool runs the same loop with the learning layer dialed up — curriculum, observations against learning frameworks, progress reports. The researched products sell one system across both: the same check-in, the same ledger, the same guardian app; the segment difference shows up in which capabilities a program leans on, and in how the vendor markets it.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:   Custody attendance
Forms:     kiosk with personal codes · QR scan from the guardian's phone · card or badge swipe ·
           staff-mediated sign-in · staff-side attendance mode

Concept:   Care-day documentation
Forms:     structured entries (meal / nap / toileting types) · free notes · photos and videos ·
           incident and health entries · observation notes against learning frameworks

Concept:   Tuition billing
Models:    flat recurring plans · schedule-based · attendance-based · drop-in ·
           family-plus-subsidy split · regional funding reconciliation

Concept:   The same business under regional names
Names:     daycare · preschool · nursery (UK) · childminder setting (UK home-based) ·
           kindergarten (parts of Asia and Europe) · early-childhood program
```

A reader who has only seen one implementation — say, an app-first product where guardians scan a code at the door — should still be able to recognize a desktop-era center with a card-swipe station, a UK nursery with rotas and funding reconciliation, or a home-based childminder with no rooms at all, from the core model.

## How It Works

### 1. Enroll a child

```text
Inquiry / lead → tour → application or admissions packet (forms, contracts, fees)
→ (if no seat: waitlist) → enrolled → child record created under the family account
→ child assigned to a room and a schedule → active on the start date
```

Enrollment statuses let the operator run the pipeline and keep departed children's history without deleting it.

### 2. Run the care day

```text
Drop-off: an authorized adult checks the child in (code / scan / signature)
→ the child appears in the room's live roster; the room's ratio updates
→ caregivers log the day as it happens (meals, naps, toileting, activities, photos, notes)
→ room moves recorded when the child changes rooms
→ Pick-up: an authorized adult checks the child out — the custody handover is recorded
```

Staff can record attendance from their own devices (moving children between rooms, marking absences), and administrators see the operation's live attendance and ratio picture.

### 3. Document and share the day

```text
Caregiver logs an entry (for one child or the whole room)
→ the entry lands on each child's feed
→ guardians see it in their app (immediately, or after administrator approval, per settings)
→ staff-only entries (whereabouts checks, sensitive incidents) stay internal
```

### 4. Teach and track development — the preschool emphasis

```text
Teacher plans lessons or follows a curriculum
→ observes children against early-learning frameworks
→ observations accumulate into learning journals and progress reports
→ families receive progress reports; administrators see program coverage
```

### 5. Bill and collect

```text
Billing cycle runs (recurring plan / schedule-based / attendance-based)
→ tuition posts to family ledgers; the subsidy portion posts to the third-party payer
→ automatic payments collected; failures, refunds, adjustments handled on the ledger
→ statements and year-end documents issued to families
```

### 6. Staff the rooms

```text
Director sets staff schedules (rotas) and room assignments
→ live view compares children present vs staff present per room
→ out-of-ratio situations surface as alerts; staffing checked against future enrollment
```

### 7. Manage the relationship over time

```text
Child transitions between rooms as they grow → family's next child enrolls
→ on departure: graduated/inactive; records retained for licensing
→ the enrollment pipeline continuously refills seats (leads → tours → waitlists)
```

The loop runs at three rhythms at once — daily (the care day), monthly (billing), and multi-year (the enrollment lifecycle) — all on the same records.

## Interfaces

### Administrator console (web)

The director's workspace.

- family and child records (guardians, authorized adults, documents, health data)
- enrollment pipeline and waitlist views; admissions packet builder
- room administration (capacity, desired ratio, assignments)
- billing and family ledgers (charges, payments, subsidies, statements)
- staff records, schedules, and time cards
- reporting dashboards (attendance, ratios, enrollment, revenue)

### Classroom / teacher app

A deliberately restricted, room-level surface, usually mobile.

- the assigned room's live roster and ratio
- check-in assistance and room-to-room moves
- activity logging (meal, nap, toileting, photo, note, medication, incident, observation)
- messaging with the room's families; payment data withheld

### Check-in station / kiosk

A shared device at the door — the custody gate.

- guardian- or staff-operated check-in and check-out, gated by a personal code, a scanned code, a card, or a signature
- optional health-screen questions and drop-off notes at check-in
- shows who is currently in care and flags unauthorized pickup attempts

### Guardian app / portal

The family's window into the care day.

- the child's daily feed (activities, photos, notes) and galleries
- messaging with the program; calendars and newsletters
- tuition balance, bills, and payment; enrollment paperwork
- the child's own check-in credential for the door

### Learning and documentation surfaces

Where the preschool emphasis lives: curriculum and lesson planning, observation capture against early-learning frameworks, learning journals, and progress reports to families — plus the administrator's view of coverage and developmental progress.

### Reporting surface

Attendance, ratio, enrollment, and financial reports, typically exportable — the layer that faces licensing authorities and the operator's bookkeeping.

## Important Rules / Behaviors

- **Custody is the gate.** A child leaves only with an authorized adult. Products maintain per-child authorized-pickup lists and can block check-in attempts by anyone else; some capture signatures because licensing authorities may treat the event as the custody record.
- **Attendance is the load-bearing record.** The same event feeds live ratios, attendance-based tuition, subsidy reporting, and the licensing attendance history, so errors propagate — which is why batch corrections and audit views exist.
- **Enrollment is ongoing, and history is retained.** Children move through statuses rather than re-registering per term; departed children's records are archived, not deleted, because licensing requires historical attendance and enrollment records.
- **Rooms bound capacity and ratio.** Room assignment is what makes ratio monitoring possible; going out of ratio is an alertable compliance event, and staffing plans are checked against child schedules room by room.
- **Money has multiple parties.** Tuition may be split between the family and a subsidy payer; the ledger must track who owes what, post agency payments separately, and handle co-pays and adjustments without disturbing the family balance.
- **Documentation has visibility classes.** Not every logged entry is family-visible: internal entries are staff-only, and some products route family-visible posts through administrator approval.
- **Roles are stratified.** Administrators see money and compliance; teachers see their room's children and feeds; guardians see only their own children; approved pickups and emergency contacts see custody functions but not the child's feed.
- **The day is logged in the moment.** Documentation and custody events are captured as care happens; the record is meant to reflect the day, not be reconstructed later.
- **Learning records are documentation, not academic records.** Observations and progress reports describe development; they are not grades, transcripts, or promotion decisions — the care operator is not the child's school of record.

## Variants

Common shapes of the same Type:

- **Daycare / child care center** — the category's center of gravity: full-day, year-round care organized by rooms and ratios, with tuition billing and family engagement; care logistics lead.
- **Preschool / early-education program** — the same core with a heavier learning layer: curriculum, observations, assessments, progress reporting; some preschools run on a school-year calendar on top of the ongoing enrollment.
- **Nursery and childminder settings (UK naming)** — the same structures under regional names, with local regime overlays (rotas, ratios, funding reconciliation, inspection framing); childminder solutions serve the home-based pole.
- **Montessori and faith-based programs** — care operations with pedagogy- or congregation-specific framing.
- **Home-based family childcare** — one or a few caregivers in a home: the core loop (enrollment, custody attendance, daily documentation, billing) intact, with rooms, deep staffing, and multi-site machinery dropped; vendors offer dedicated editions or segments for this provider type.
- **State-funded programs** — the same core with deeper compliance and government reporting.
- **Multi-site / franchise groups** — consolidated enrollment, billing, staffing, and ratio oversight across locations; seat-filling and room-transition planning become analytical surfaces.

A variant remains a variant unless it changes the defining core; matching families with individual caregivers (rather than operating a care business) changes it enough to be a different Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Childcare Management System | same product family — one population behind two directory names | the researched vendors sell one product under both the "childcare management" and "daycare/preschool management" names; daycare and preschool are segment emphases (care logistics vs learning layer) inside that Type, not separate systems. The overlap is recorded in the atlas status for a directory-level review |
| After-school Program Management | sibling sharing the core | scheduled part-day session programs run from rosters around the school day vs full-day custody care with care-day documentation; vendors commonly sell both as sibling solutions |
| Camp Management System | sibling sharing the core | seasonal, consecutive-day sessions (often overnight) vs year-round ongoing care |
| Babysitting Marketplace | different user entirely | two-sided consumer matching between families and individual caregivers; no operator business is managed |
| Student Information System | different domain | the school of record for enrollment, grades, and transcripts; a preschool in this family is not the school of record |
| Parenting / Baby Tracking Application | shares one surface | a family privately logging their own child's day; no enrollment, custody counterparty, staff, or billing |
| Lesson Planning Application | adjacent | teacher-facing authoring tooling; here the learning layer serves the operator's program documentation |

The relationship with **Childcare Management System** is not a seam but an overlap: the structural test that separates the other siblings does nothing here, because removing the daycare emphasis or the preschool emphasis leaves the same system. The boundaries that do hold are the care-context boundaries (after-school, camp, marketplace) recorded above.

## Representative Products

- **brightwheel** — modern app-first platform; sells one product behind parallel "childcare management" and "preschool management" surfaces, which makes the shared structure unusually visible
- **Famly** — UK/EU early-childhood platform ("nursery management software") with solutions for small nurseries, nursery groups, and childminders; daily logs, rotas with automatic ratios, funding reconciliation
- **illumine** — international platform (US, Gulf, South and Southeast Asia) carrying the childcare/daycare/preschool labels on one product; AI-assisted enrollment, attendance, billing, parent communication, and learning records; enterprise multi-center tier
- **Procare Solutions, Lillio, Kangarootime, Smartcare** — further members of the same family, documented from the sibling atlas entry's research (legacy all-in-one suite, documentation-first, multi-location, and payments-centric postures respectively)

The definition was checked against regional naming (nursery, childminder, kindergarten), against home-based deployments (no rooms), and against desktop-era practice recorded in the sibling entry's research, so it does not depend on today's mobile-app pattern.

## Sources

Research date: **2026-09-07**

Fresh vendor surfaces:

- brightwheel — https://mybrightwheel.com/ and https://mybrightwheel.com/preschools/
- Famly — https://www.famly.co/
- illumine — https://illumine.app/

Corroborating surfaces (fetched the same day under the sibling atlas entry):

- Procare Solutions — https://www.procaresoftware.com/ and https://www.procaresupport.com/
- brightwheel Help Center — https://help.mybrightwheel.com/en/
- Kangarootime — https://kangarootime.com/ ; Smartcare / RevTrak — https://www.revtrak.com/child-care ; Lillio — https://www.lillio.com/

> Sourcing limitations: Famly's and illumine's help centers were not fetched for this pass; their structures are taken from official product pages at module level. Vendor scale, review, and performance claims are recorded as claims, not facts. Precise operational details (numeric limits, default settings, exact status vocabularies) are intentionally not stated in this document; such details remain in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison, and the alias joint-review analysis are recorded in the paired Research Notes.
