# Pet Training Management

## Overview

A **Pet Training Management** application is the operator-side system of record for a dog-training business — the software a training facility or trainer-owned business runs its programs in: client and dog records, a catalog of scheduled training offerings (group class series and private lessons), enrollment of specific dogs into those offerings, and the money that enrollment produces.

It solves a specific problem: a training business sells structured programs, not one-off appointments. A "Puppy Kindergarten" is a six-week series with pre-set dates, one roster, a size limit, and one tuition payment; a private-lesson client buys a block of sessions and uses them over months. Spreadsheets and generic calendars lose the thread between the offering, the dogs enrolled in it, the sessions that make it up, and who has paid for what. This Type exists to hold that thread: the offering, the enrollment, the sessions, and the tuition are one connected record.

The defining core is small:

```text
Client account with dogs
└── Scheduled training offerings (class series + private lessons)
    └── Enrollment binding dog → offering (roster / booking)
        └── Tuition resolving on the client account
```

Everything else commonly associated with these products — trainer assignment, attendance tracking, report cards, graduation, vaccination reminders, online registration, waitlists — is widespread in current products but is not part of what makes the Type. A paper-era training club with a class list, an enrollment sheet, and a fee ledger holds the same core with none of it.

## Users & Context

Primary users, all inside the business:

- **Trainers / instructors** — teach the classes and private lessons; work from the schedule they are assigned; record what happened in a session (attendance, notes, progress).
- **Front-desk / administrator staff** — create and publish class offerings, enroll dogs, take payment, answer "is there room in the next beginner class", manage rosters and waitlists.
- **Owner-operator** — configures the offering catalog and pricing, manages trainer accounts and availability, watches enrollment and revenue.

Secondary participants:

- **Dog owners (clients)** — through a self-service surface (online registration, portal, or mobile app) they register for classes and lessons, request enrollment, sign agreements, upload vaccination records, and pay. They never operate the system of record.
- **Accountants / bookkeepers** — reached indirectly through payment processing and accounting exports.

The work environment is a training facility's front desk and training floor: a persistent view of the class calendar (which series are running, which are full), today's sessions and their rosters, and the money side of enrollment.

## Core Model

### The Defining Core

Four structures, held jointly:

**1. The client account with dogs.** Every customer is an identified owner account holding one or more animal sub-records. The dog — not a person — is the enrolled subject: it is the thing that gets enrolled, attends, and is billed for. The dog record carries the data training work runs on: vaccination status (group settings commonly require proof of current vaccines), behavior and temperament notes, age/breed details where relevant, and the accumulated training history. The client account accumulates the relationship: enrollments past and future, packages and credits, notes, and balances. Without the animals and their care semantics, this is just a class-booking tool.

**2. The scheduled training offering.** The business's training services exist as scheduled structures in two standard shapes:

```text
Class series    → a named multi-session program (e.g. a beginner course
                  meeting weekly for a fixed number of sessions), with
                  pre-set or recurring dates and one roster for the series
Private lesson  → a dated one-to-one appointment with a trainer
```

The offering definition (what the class is: name, description, number of sessions, session length, price, capacity) is held separately from its scheduled occurrences (when a specific instance runs, where, with which instructor). This separation is what lets a business publish a catalog once and schedule instances of it repeatedly. Without scheduled offerings, the system is a client list with nothing to enroll in.

**3. The enrollment binding.** Enrolling a dog creates a persisted record binding that dog to a specific offering — the roster entry for a class series (spanning all its sessions) or the booking for a private lesson. The roster is the class's participant list: visible on the offering, capacity-bounded, and the basis for attendance. Enrollment is per dog, from the same owner account; multi-dog households enroll dogs individually. Without the binding, a schedule exists but nobody is in it.

**4. The tuition loop.** Enrollment resolves into money on the client's account. The typical forms: the series tuition paid upfront as a package (credits tracked as used/remaining across the sessions), per-session payment where no package applies, deposits to hold a spot, and balances carried on the account until settled. Lesson businesses sell blocks of sessions the same way. Without this, the system is a free sign-up sheet.

The four stand or fall together:

```text
client/dog records alone              → a client/dog CRM
offerings without records/enrollment  → a class brochure
enrollment without records/offerings  → an anonymous sign-up sheet
money without records/enrollment      → an invoicing shell
records + offerings without enrollment→ a catalog with no rosters
offerings + enrollment without records→ anonymous class booking
all three without money               → a free community class roster
```

### Standard Capabilities of Mature Products

These are common across the researched sample and expected by the market, but they are additions to the core, not the definition:

- **Trainer/instructor assignment** — instructors attached to scheduled offerings (with co-instructor support in deeper products); trainer user accounts with roles, availability, and schedules; automated notifications when services are assigned. A solo operator who teaches everything themselves satisfies the core without named assignment.
- **Class capacity machinery** — maximum (and sometimes minimum) registration limits per class, full/canceled flags, waitlists with their own notifications.
- **Attendance and session records** — attendance tracked per session (in products that model the series as one record per session, each session is checked in and out like any other service); class notes; printed rosters to carry into class.
- **Progress records** — report cards sent to owners; graduation semantics for open-ended classes (a dog starts any week, completes the required number of sessions, and graduates).
- **Vaccination machinery** — vaccine records stored on the dog with expiry tracking and reminders; uploaded records and signed contracts; eligibility for group classes commonly tied to vaccine currency.
- **Client self-service** — online registration for classes, lessons, and packages (often embedded on the business's own website); customer portals and mobile apps for enrollment requests, forms, and payment; staff-side approval of requests.
- **Forms and agreements** — training agreements, liability waivers, emergency-contact and veterinarian forms, per-offering registration forms.
- **Communications** — registration confirmations, reminders, class-wide emails to a roster.
- **Pricing machinery** — pricing rules and add-ons, discounts (sometimes assignable to whole class categories), deposits.
- **Business machinery** — payment processing, invoices, reporting (enrollment, revenue), accounting exports, staff management.

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:  scheduled training offering
Realized as:  a class definition scheduled as a recurring series,
              a group-class object with a session schedule,
              a training product/service configured then placed on a calendar

Concept:  enrollment binding
Realized as:  a roster entry on the class,
              reservations created per session on the animal's profile,
              a training request approved onto a roster

Concept:  tuition loop
Realized as:  a package purchased at enrollment and drawn down per session,
              a cart checkout at enrollment,
              a balance added to the account for later payment
```

A reader who has only seen one product should still be able to recognize any other from the core.

## How It Works

### Configure the program

```text
Define the offering catalog: class names, descriptions, session counts,
  session lengths, prices, capacity limits, registration forms
→ set pricing rules, discounts, deposits
→ add trainer accounts, roles, and availability
→ configure vaccination requirements, agreements, and waiver forms
```

### Schedule and publish

```text
Schedule an occurrence of a class: start date, repeat structure
  (a fixed series repeats for the session count; an open-ended class
  repeats indefinitely), location, instructor
→ set it public (visible for online registration) or private
→ mark occurrences canceled or full when needed
```

### Enroll

```text
A dog is enrolled — by staff, or by the owner through online registration
→ select the offering and the dog(s) from the same owner account
→ capacity checked against the roster; full classes close or waitlist
→ payment resolved: series package purchased upfront, deposit taken,
  or balance added to the account
→ the enrollment appears on the class roster and on the dog's profile;
  in per-session models, a reservation is created for each session
```

### Run the series

```text
Each session: attendance taken from the roster (check-in/check-out where
  the session is modeled as a service record)
→ notes and progress recorded; report cards sent to owners
→ open-ended classes track sessions completed toward graduation
→ a missed or canceled session is handled against the roster
```

### Settle and retain

```text
Package credits drawn down as sessions are used; balances collected
→ un-enrollment and refunds handled against the roster and account
→ class-wide communications; next-level or next-series prompts
→ enrollment and revenue reporting
```

The interaction loop that defines daily use is the enrollment cycle: **publish offerings → enroll dogs → run sessions → draw down tuition**, repeated as each series fills, runs, and completes.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Class calendar / schedule

The scheduling surface.

- typical information: scheduled offerings by day/week/month, session times, locations, instructors, full/canceled states, color-coding per class
- primary actions: schedule an occurrence, edit or duplicate a series, mark canceled/full, jump to a roster

### Offering catalog

The definition surface for what the business sells.

- typical information: class names and descriptions, session counts and lengths, prices, deposits, capacity limits, categories, linked registration forms
- primary actions: create/edit/archive offerings, assign categories, set rates

### Class roster / enrollment view

The participant surface for one offering.

- typical information: enrolled dogs and their owners, roster size against capacity, per-session attendance, waitlist
- primary actions: enroll a dog, un-enroll, move to waitlist, take payment, email the class, print the roster

### Client and dog profiles

The record-of-record surfaces.

- client: contact details, dogs, enrollment history, packages/credits, invoices, notes, signed agreements
- dog: care and eligibility data (vaccinations, behavior notes), enrollment history, session records
- primary actions: edit, enroll, take payment, add notes, message

### Payment / checkout

The money surface.

- typical information: enrollment charges, package prices, deposits, account balances, remaining credits
- primary actions: take payment, apply a package, add a balance, refund

### Client-facing surfaces

- online registration page (embedded on the business's website): browse the class list, register a dog, pay
- customer portal / mobile app: request enrollment, sign forms, upload vaccine records, pay balances

### Reports and settings

- reports: enrollment fill rates, revenue by class, trainer schedules
- settings: offerings and pricing, trainers and permissions, locations, forms, integrations

## Important Rules / Behaviors

### The roster is capacity-bounded

A class admits a bounded number of dogs. At the limit, enrollment closes or the dog goes to a waitlist. This is the overbooking guard of the Type — a group class without a size limit stops being a class.

### Enrollment outlives any single session

The roster entry spans the series. A dog that misses one session remains enrolled; attendance is recorded per session against the standing enrollment. Open-ended classes invert this: the dog completes a required number of sessions to graduate, so the enrollment tracks progress rather than dates.

### Payment form varies; the loop does not

A series may be paid upfront as a package, per session as each occurs, or held as a balance on the account. What is invariant is that enrollment resolves into money on the client account — one of these forms always applies.

### Vaccine currency gates group participation

Group classes bring unknown dogs together, so current vaccinations are commonly required: records are stored on the dog, expiry is tracked, and eligibility for enrollment is tied to vaccine status. Enforcement style varies by product (hard block vs alert-and-verify).

### Requests are requests until confirmed

Owner-initiated enrollment through a portal commonly lands as a request that staff confirm — keeping capacity and eligibility decisions with the business.

### Custody stays with the owner

Dogs arrive for class or a lesson and go home the same day. There are no placement or custody-transfer outcomes here — that is shelter territory. The one structural overlap is board-and-train (below).

## Variants

Common shapes of the same Type:

- **Training facility** — classes-led: a catalog of running series across levels (puppy → beginner → advanced), the fullest expression of the Type.
- **Private-lesson-led business** — appointment-book-centric: one-to-one lessons, behavior consultations, session packages; classes secondary or absent.
- **Training desk of a multi-line facility** — training run inside a boarding/daycare/grooming business; the training core is unchanged, the surrounding platform is the umbrella Type.
- **Board-and-train programs** — training delivered while the dog boards; the stay side uses boarding machinery (accommodation, per-stay billing), the program side uses training machinery (packages, progress). The overlap is real but the cores remain distinct.
- **Specialty programs** — therapy-dog preparation classes, seminars and workshops with tiered registration, virtual/online classes.
- **Session-structure variants** — fixed series (enroll once, pre-set dates), open/modularized enrollment (start any week, complete N sessions, graduate), drop-in classes (pay per attendance).
- **Scale and deployment** — solo trainer → single facility → multi-location; cloud SaaS is the current norm, with long-lived web-application generations behind it and paper-era club records as the conceptual pre-history.

A variant remains a variant unless it changes the core: a private-lesson-only business still holds offerings, enrollment, and tuition; a business that adds boarding/daycare/grooming lines on one shared system has become the umbrella Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Pet Care Business Management | umbrella sibling | same product population at whole-business scope: multi-line booking, cross-line accounts and billing; here the training line stands alone (one vendor sells it as a standalone subscription) |
| Pet Grooming Management | single-line sibling | grooming's unit of work is a single hours-billed appointment priced from a breed/coat/size menu; training's unit is the enrollment — a multi-session series with a roster and series-level payment |
| Pet Boarding Management | single-line sibling | boarding's unit of work is a stay consuming accommodation inventory; board-and-train programs touch both Types, but neither core subsumes the other |
| Pet Daycare Management | single-line sibling | daycare's unit is the same-day attendance consuming daily capacity; no roster/series/tuition semantics |
| Dance Studio Management | structural analog (human students) | same class-series skeleton (catalog → series → enrollment → tuition), but the student is a child/person with guardian accounts, levels, and recital machinery; here the student is an animal with vaccination and behavior data |
| Fitness Studio Management | structural analog (human members) | class-led business with a membership/entitlement economy for the member's own body; here the served subject is the owner's animal and the economy is tuition/packages |
| Corporate LMS / Customer Training platforms | different domain | those manage learning content and learner completion records for people; here the class is a scheduled service consuming capacity and producing revenue — no courseware, no learner profiles, no certification machinery |
| Appointment-based Service Business Management | generic skeleton | appointments + clients + billing without the animal subject, the multi-session class series, or series/tuition semantics |
| Event Management | adjacent capability | one-off seminars/workshops ride registration machinery; the Type's center is the recurring series and the lesson |
| Dog Walking Platform / Pet Sitting Platform | consumer-side neighbors | two-sided matching of strangers vs operator-side administration of a business's own clients and offerings |
| Veterinary Practice Management | adjacent (both hold client+animal records) | vet is clinical care; vaccination data here is eligibility data, never a clinical workflow |

The most important boundary is the one against the umbrella sibling: this leaf and Pet Care Business Management describe the same product population at different scope cuts. The test is scope, not features — remove the multi-line whole-business scope and the remaining core is this Type; add the other service lines on one shared schedule, account, and billing loop and the umbrella reappears.

## Representative Products

- **DogBizPro** — dedicated dog-business software with training as the founding module (classes, private training, events, therapy) beside optional daycare/boarding modules; solo trainers to training facilities (US)
- **Gingr** — multi-line pet-care SaaS whose Group Classes machinery (series enrollment, per-session reservations, package payment) is a reference implementation of the training line; SMB to enterprise/multi-location (US)
- **ProPet Software** — multi-line platform with a named Dog Training module, sold also as a training-only subscription; founder-owned, kennel-operator origins (Canada)
- **PetExec** — multi-line platform with a dedicated trainers offering (rosters, class calendar, board-and-train packages); now part of the Gingr corporate family (US)

The definition was checked against the paper-era training club (class list + enrollment sheet + fee ledger) to avoid over-fitting to today's cloud/portal pattern.

## Sources

Research date: **2026-09-09**

- DogBizPro — https://dogbizpro.com/ ; Features: https://dogbusinessprogram.com/software/features/ ; Support portal (Classes): https://support.dogbizpro.com/category/7-category ; articles: Creating Classes & Categories, Scheduling Classes
- Gingr — Help Center: https://support.gingrapp.com/hc/en-us ; section: Reservations, Appointments, and Group Classes; articles: Group Classes (Topic Outline), Set Up a Group Class (Process), Enroll a Pet in a Group Class (How-To)
- ProPet Software — https://www.propetware.com/ ; Dog Training module: https://www.propetware.com/dog-training-software/
- PetExec — https://petexec.net/ ; PetExec for Trainers: https://petexec.net/service/trainers ; Documentation center: https://docs.petexec.net/ (Training subject area)
- Time To Pet — https://www.timetopet.com/ (solutions navigation; negative evidence — no training solution)

> Sourcing limitations: Trainer's Best Friend could not be reached (transport error), so the independent training-only vendor pole beyond DogBizPro is not directly sampled. PetExec's training documentation exists as PDFs that do not render as text; its evidence is product-page and documentation-structure depth. ProPet's evidence is module-page depth. Precise numeric limits, default settings, and internal state names are intentionally not stated in this document; detailed observations are recorded in the paired Research Notes.
