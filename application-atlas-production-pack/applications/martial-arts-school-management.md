# Martial Arts School Management

## Overview

A **Martial Arts School Management** application is the operator-side business system for running a martial arts school — a dojo, academy, or gym that teaches disciplines such as karate, taekwondo, Brazilian jiu-jitsu, judo, MMA, or krav maga. It organizes the school's world around its students, the programs and scheduled classes the school offers, the memberships that entitle a student to attend, and the dues those memberships generate — then carries daily operations through attendance check-in at the door, student progression through ranks and promotions, and the lead-to-trial funnel that keeps new students arriving.

The defining core is small:

```text
Student record (held on a family account when children train)
└── Programs + scheduled class offerings
    └── Membership / enrollment (entitlement to attend)
        └── Dues-and-fees loop (charges → payments → arrears)
```

Everything else commonly associated with these products — kiosk check-in, belt and rank tracking, belt testing events, member apps, automated lead follow-up, retail — is standard market structure layered on that core, not what makes the product this Type. A school run on paper (a student card file, a posted schedule, a dues ledger, attendance cards, a promotion record) has the same underlying structure, which is why the definition does not depend on any modern implementation detail.

When the center of gravity shifts to a season/session calendar with costumes and recitals, the product is drifting toward dance studio management; when it shifts to adult members with drop-in passes and no progression machinery, toward fitness studio management; when it shifts to one-shot registration transactions, toward a sports registration platform.

## Users & Context

**Primary users** — the people who run the school:

- **Owner / head instructor** — often the same person. Builds the program and class schedule, defines membership pricing and rank requirements, watches revenue, retention, and enrollment, and follows up on leads. In many schools this user also teaches most classes, so the software's job is to remove desk work from the mat.
- **Front-desk / admin staff** — work the daily loop: enrollments and account changes, billing questions and past-due follow-up, check-in issues, waivers, communication with families.
- **Instructors** — see their class rosters, take or verify attendance, and make progression decisions (who is ready to test, who gets signed off for promotion).

**Secondary users** — the school's customers:

- **Students** — the central record of the system. They check in for class, book classes, and (in the member app) see their current rank, their progression path, and what they need to work on.
- **Parents / guardians** — for children's programs, the account holders. They register their children, pay tuition and fees, sign waivers, receive announcements, and get promotion notifications, typically through a self-service portal or app.

**Typical context:** a commercially run school — usually a single location operated by an owner-instructor, up to multi-location organizations and franchise networks. Unlike season-based activity businesses, martial arts schools typically operate continuously: students join at any time on month-to-month or term memberships, and the calendar is anchored by events (belt tests, tournaments, camps, birthday parties) rather than by enrollment seasons. The customer base mixes children (family accounts, parent payers) and adults (individual members); many schools serve both.

## Core Model

### The defining core

**Student record.** The central object is an identified person enrolled in the school. For children's programs the student sits on a **family account**: one household account holds multiple students, and the family — not the individual child — is the paying unit, so dues, test fees, and retail purchases land on one balance. Adult academies run on individual member records; the student record is the constant across every school, and the family grouping is the dominant implementation when minors train. A mature product's student profile spans identity and contact details, agreements, attendance history, finances, communication settings, and an audit history of changes.

**Programs and scheduled classes.** The school's offer is organized as **programs** (e.g., "Kids Karate", "Adult BJJ") that carry a recurring class schedule — day-and-time slots, instructors, capacity. Programs are the backbone to which other structures attach: memberships, rank structures, and communication segments are all scoped by program. Mature products guard the schedule against double-booking instructors and spaces, and commonly add a second, appointment-style booking type (private lessons).

**Membership / enrollment.** The record that links a student to one or more programs and defines what they may attend — the commercial relationship, not just a roster line. Memberships are typically configured from templates: a duration (continuous with no expiration, a fixed term, or a number of class attendances), a billing structure (recurring, paid-in-full one-time, or no-charge for trials), and program scoping. The membership is what converts a person into a paying, attending student.

**Dues-and-fees loop.** The money loop is membership-driven: recurring dues (and one-time fees — registration, belt testing, events, retail) post as charges against the student or family account, payments settle them, and unpaid balances are tracked as arrears. In modern products, charges run automatically against a stored payment method with reattempts and alerts for failures; smaller or older operations collect manually. The structure — charges accrue, payments settle, arrears are visible and actionable — is what every implementation of this Type shares.

### Standard capabilities

Mature products across the market carry most of the following:

- **Attendance and check-in.** Daily operations center on a check-in surface at the door: a kiosk where students enter a PIN, search their name, or scan a barcode (printed or shown on their phone), sometimes with staff-side or app-based check-in and bulk check-in for large groups. Check-ins feed a live view and a per-student attendance history.
- **Participation gating.** The check-in surface is where money, entitlement, and paperwork converge: schools can block or flag check-in for students with a past-due balance, an expired membership, or a missing signed waiver, and the kiosk explains why. Some products extend this to door access control for unstaffed hours.
- **Progression tracking — ranks, promotions, and testing.** The martial-arts signature layer. Each program carries a rank structure (belt colors, stripes, kyu/dan degrees, or fully custom progressions; some disciplines have no ranks and track skills instead). Each rank carries promotion requirements — typically attendance minimums, time in rank, required techniques or skills, and instructor sign-off — and the system computes who is ready: test-ready students are surfaced automatically from attendance and time-in-rank data. **Belt testing events** are distinct events that eligible students join, often with a test fee collected through the same billing engine as dues; results are recorded per student (promoted or deferred), the promotion becomes part of the student's permanent history rather than an edit to their profile, and families are notified. Rank histories and promotion records are searchable and reportable.
- **Curriculum content.** Technique videos, kata requirements, and curriculum materials attached to programs or ranks, visible to students in the app so they know what to work on between classes.
- **Lead, trial, and conversion machinery.** Prospecting is a first-class concern in this market: capture forms and landing pages (often embedded in a vendor-hosted website), free trial or intro-class offers, a prospect pipeline with stages, automated follow-up sequences, and two-way texting. The trial — a free or low-commitment first class — is the standard entry point into membership.
- **Waivers and agreements.** Liability waivers and membership agreements as templates with electronic signature, sent by link, email, or text, tracked for unsigned status, and attached to registration — and, in several products, enforced at the door.
- **Member portal / mobile app.** The student's and family's self-service surface: book classes, view the schedule and their own attendance, pay bills and manage payment methods, see current rank and progression, self check-in with a barcode, receive announcements, and register for events.
- **Communication.** Email and SMS announcements (segmented by program or membership), plus automated alerts: expiring memberships, failed or past-due payments, absences ("we haven't seen you in a while"), milestones, and promotion congratulations to student and parents.
- **Events.** Belt tests, tournaments, camps, seminars, and birthday parties as registrable events with capacity, payment, waivers, and reminders — camps in particular are a significant seasonal revenue line for children's schools.
- **Retail / POS.** Selling gear, uniforms, and apparel against inventory, settled on the same account as dues.
- **Reporting.** Revenue, retention, and attendance views — who is training consistently, who is at risk of quitting, what the money is doing — plus prospect-conversion metrics.
- **Multi-location support.** Larger organizations and franchises manage several locations with consolidated oversight; this is a scale feature, not a structural one.

### One structure, many implementations

```text
Concept:   Progression per program
Realized as:  belt colors + stripes (BJJ-style), kyu/dan degrees
              (karate-style taekwondo/judo), custom rank names,
              or no ranks at all — skills and attendance milestones
              for disciplines that don't rank (e.g., wrestling programs)

Concept:   Membership entitlement
Realized as:  continuous month-to-month dues, fixed-term contracts,
              paid-in-full terms, class-count passes, no-charge trials

Concept:   The paying unit
Realized as:  family account (children's programs) or
              individual member record (adult academies)
```

A reader who has only seen one kind of school — say, a kids' karate school on family autopay with belt tests — should still be able to recognize an adult-only jiu-jitsu academy on month-to-month individual memberships, or a rank-less wrestling club, from the same core model.

## How It Works

### Set up programs, schedule, and rank structures

```text
Define programs (kids karate, adult BJJ, …)
→ set the recurring class schedule (day/time, instructor, capacity)
→ configure the rank structure per program (ranks, stripes, requirements)
→ build membership templates (duration, billing, program scope)
→ create waiver/agreement templates
```

The program is the unit of configuration: schedule, ranks, memberships, and communication all attach to it.

### Enroll a student

```text
Prospect discovers the school → captures a lead (form / landing page / walk-in)
→ books a trial or intro class → attends
→ converts: family account created (or individual member record)
→ student added; program and membership selected
→ waiver/agreement signed; payment method stored
→ first charges post (registration, dues) → student is active
```

The funnel from lead to trial to member is a managed, automated workflow in mature products — prospects who don't convert are nurtured rather than dropped.

### Run the weekly loop

```text
Students check in at the kiosk (or app barcode)
→ check-in validated against dues, membership, and waiver state
→ attendance recorded → feeds progression counts and at-risk views
→ billing cycle posts dues to family/member accounts
→ automatic card charges settle balances; failures reattempted and alerted
→ staff follow up on arrears and send announcements/reminders
```

This loop repeats continuously — there is no season boundary. Attendance data doubles as an early-warning system: products flag students whose training frequency drops so the school can intervene before they quit.

### Advance students

```text
System computes promotion eligibility (attendance minimums,
   time in rank, instructor sign-off)
→ test-ready students surfaced → school confirms the list
→ belt test event created; invites sent; test fees collected
→ results recorded per student (promoted / deferred)
→ promotions written to the student's permanent rank history
→ families notified; new rank's curriculum becomes visible
```

Progression is the school's retention engine: visible rank paths and upcoming tests are what keep students (and paying families) engaged, which is why the machinery is deep in mature products.

### Grow the school

Between the weekly loop and the testing calendar, the same system runs the commercial cycle: capture and nurture leads, convert trials, run camps and events, sell gear, monitor revenue and retention, and manage additional locations. Pricing for the software itself is typically a monthly subscription scaled to the school's size (by student count or locations).

## Interfaces

### Admin / office dashboard

The operator's working surface, typically web-based.

- dashboards for revenue, enrollment, retention, and at-risk students
- student and family account views: profile, memberships, agreements, attendance, invoices, payment history, rank history, documents, notes
- program and schedule management; membership template configuration; rank/requirement setup
- billing screens: charge posting, payment runs, failed-payment and past-due handling
- prospect pipeline and campaign screens; reporting and exports

### Attendance kiosk

A dedicated check-in surface on a tablet or computer at the door.

- PIN entry, name search, or barcode scan; live check-in feed
- blocking states with configurable messages (past-due, missing membership, missing waiver)

### Member portal / mobile app

The student's and family's self-service surface (web and app).

- class schedule and booking; event registration; self check-in barcode
- account and payment management; waiver signing
- current rank, progression path, promotion notifications, curriculum videos

### Staff / instructor app

The instructor's working surface (mobile-friendly in modern products).

- assigned rosters and class capacities, check-in, alert resolution, attendance history
- progression actions: review readiness, record test results, sign off promotions

### Capture surfaces

Landing pages and forms (often vendor-hosted websites) that feed the prospect pipeline: trial offers, program pages, event sign-ups.

## Important Rules / Behaviors

- **The membership defines entitlement.** What a student may attend is a property of their membership(s), scoped by program — not an ad-hoc decision at the door.
- **Money state reaches the door.** Past-due balances, expired memberships, and unsigned waivers surface at check-in and can block participation; the kiosk message is configurable. This is the structural coupling that makes the system a business system rather than a roster.
- **The family account is the financial unit for children's programs.** Dues, test fees, event fees, and retail accrue to one family balance regardless of how many children train.
- **Promotions are recorded events, not edits.** A rank change is appended to the student's permanent progression history with date and context; requirements per rank (attendance, time-in-rank, skills, instructor sign-off) are configured by the school, and eligibility is computed from tracked data rather than remembered.
- **Attendance is the engagement signal.** It feeds promotion eligibility, at-risk flags, and automated win-back messages — the same record serves progression, retention, and revenue.
- **Programs scope everything.** Memberships, rank structures, communication segments, and reports are organized by program; a school running several disciplines keeps their structures separate under one roof.
- **Time is continuous, anchored by events.** There is no season/session container in the martial-arts pattern: enrollments start any time, dues recur on the billing rhythm, and the calendar's anchors are belt tests, tournaments, and camps.
- **Trials are the standard entry.** The free or intro-class trial, captured and nurtured through the funnel, is the standard path from prospect to paying member.

## Variants

- **Customer shape.** Kids/family-centric schools (parent payers, promotion notifications to parents, camps) vs adult academies (individual members, no parent layer) — most products serve both; the balance shapes which capabilities lead.
- **Discipline and rank shape.** Striking arts with kyu/dan progressions, BJJ stripe systems, custom rank schemes — or rank-less programs (wrestling, boxing) where progression is tracked as skills and attendance.
- **Membership and billing shape.** Month-to-month recurring, term contracts, paid-in-full, class-count passes; integrated payment processing, partner processors, bring-your-own processor, or manual payment recording where no processor is available.
- **Scale.** Single owner-operator → multi-location organization → franchise/association rollout with centralized control and per-location visibility.
- **Facility posture.** Staffed front desk with kiosk check-in vs unstaffed 24/7 access controlled by app- or smart-lock door systems.
- **Adjacent revenue and services.** Retail gear sales, camps and birthday parties, seminars; vendor add-ons such as website builders, branded member apps, and marketing services.
- **Region.** The market is US-centric with international presence; products are sold across North America, the UK, Australia, and beyond.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Dance Studio Management | sibling vertical on the same spine; dance organizes time by seasons/sessions and adds costume/recital/competition machinery; this Type organizes time continuously and adds rank/testing machinery |
| Swim School / Gymnastics Club Management | sibling vertical realizations of the same class-management family (level cycles and makeups for swim; skill tracking and meets for gymnastics) |
| Fitness Studio Management | centers adult members and the drop-in/class-pack economy; this Type centers enrolled students (often minors on family accounts), program progression, and testing; several vendors sell one product across both markets, so the seam is drawn on structure |
| Gym Management System | broader gym operations (access, amenities, equipment) around the same membership/check-in core; the school/class/progression layer is what this Type adds |
| Membership Management System | a generic dues-and-lifecycle engine without programs, class schedules, attendance, or progression semantics |
| Sports Registration Platform | one-shot registration transactions for programs/seasons rather than the ongoing membership relationship with dues, attendance, and promotion |
| Youth Sports / Team Management | team, league, and game orientation rather than school, class, and membership orientation |
| Learning Management System | curriculum content exists here, but attached to business operations; the teaching loop is not the center — the school's commerce and operations are |
| CRM | the prospect funnel is CRM-shaped and prominent, but embedded in the school's operating loop; the enrolled-student record, not the deal, is the center |

The most important boundary is with **Fitness Studio Management**: the shared membership/dues/check-in core is real, and the market sells one product into both worlds. The structural discriminators are the customer shape (family-with-children vs adult individual) and the progression layer (ranks, requirements, testing events vs none). The second most important is with **Dance Studio Management**: same family spine, different time structure (continuous vs season) and different signature layer (ranks/testing vs costumes/recitals).

## Representative Products

- Kicksite
- MyStudio
- Zen Planner (martial arts vertical of a multi-vertical platform)
- Gymdesk

The core model was checked across these four to avoid over-fitting to any one vendor's packaging: two are martial-arts-first specialists, one is a martial-arts-origin product now sold across gym types, and one is a multi-vertical platform with a dedicated martial-arts offering — which is also why rank/testing machinery is described as the standard extension of a shared core rather than part of the definition, and why both family and individual customer shapes are carried in the core model.

## Sources

Research date: **2026-09-08**

- Kicksite — product home, Martial Arts Management Software, Attendance Tracking, and Member Management feature pages — https://kicksite.com/
- MyStudio — product home, Rank & Belt Management product page, Martial Arts solution page — https://www.mystudio.io/
- Zen Planner — Martial Arts vertical page and Product (full feature list) page — https://zenplanner.com/
- Gymdesk — product home (feature list and FAQ) — https://gymdesk.com/

> Sourcing limitation: official product and feature documentation was used for all four products; no vendor help-center or knowledge-base article bodies were retrieved. Precise operational parameters (billing-cycle defaults, numeric requirement thresholds, exact status names, pricing-plan detail) are intentionally not asserted in this document; claims are calibrated to what the fetched documentation directly shows, and finer product details remain in the paired Research Notes.
