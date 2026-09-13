# After-school Program Management

## Overview

An **After-school Program Management** application is operator-side software for organizations that run scheduled out-of-school-time programs for children — after-school care, enrichment classes, clubs, sports and arts programs, tutoring programs. It lets the operator publish a catalog of scheduled programs, register children into those programs on behalf of their guardians, and run each program from rosters of enrolled children, with attendance, billing, and parent communication built around that enrollment.

The defining structure is small:

```text
Operator program catalog (scheduled offerings for children)
└── Guardian-initiated child enrollment
    └── Per-offering roster of enrolled children
```

Everything else commonly associated with these products — family accounts, session/semester scheduling, waitlists, tuition autopay, check-in kiosks, instructor portals, parent messaging — is standard capability that mature products add to make the core loop practical, not part of what makes the software this Type.

When the center of gravity shifts to full-day licensed care (rooms, ratios, daily reports), the product is drifting toward a Childcare Management System; when it shifts to seasonal consecutive-day sessions, toward a Camp Management System; when it centers a single registration transaction with no ongoing child-program relationship, toward an Event or Course Registration platform.

## Users & Context

**Primary operator-side users:**

- **Program administrator / coordinator** — builds the program catalog, opens and closes registration, manages enrollments (waitlists, transfers, drops), oversees billing, and runs reports. This is the main seat of the software.
- **Site staff / instructors** — work from their assigned rosters: view enrolled children, record attendance, take attendance in class, and message families. Their visibility is deliberately narrower than administrators' (typically no payment data).
- **Front desk staff** — handle walk-in questions, check-in, and same-day enrollment changes at the door.

**Primary participant-side users:**

- **Guardians (parents)** — register their children, complete forms and waivers, pay, and receive confirmations and announcements. They interact through a self-service portal or an embedded registration widget on the operator's website, not through the operator console.

**Typical contexts:** a youth activity business (gymnastics, dance, swim, martial arts, STEM, art), a school district or community-education department running before/after-school and enrichment programs, a childcare provider offering school-age care, or a nonprofit running youth programs. The operator is not the child's school of record; the software manages programs, not schooling.

## Core Model

### The Defining Core

Three structures. If any one is removed, the software stops being recognizable as this Type:

- **Program catalog** — the operator defines the offerings it runs: a class, program, or activity with a name, description, age or grade eligibility, capacity, schedule, and usually a price. The catalog is the operator's product line; nothing can be enrolled into, rostered, or billed without it.
- **Child enrollment** — participation is recorded as an enrollment that binds one specific child to one scheduled offering, created through a guardian. The child is the participant; the guardian is the contracting, paying, and communicating counterparty. This child-plus-guardian shape is what distinguishes the Type from adult course or event registration.
- **Roster** — each scheduled offering has a roster of enrolled children. The roster is the operator's working surface: staff take attendance against it, instructors see their class list from it, and capacity is enforced on it.

```text
Program catalog
  └── Scheduled offering (class / program / session)
        ├── capacity + eligibility (age/grade)
        └── Enrollment (child, via guardian)
              └── Roster of enrolled children
                    └── Attendance
```

### Standard Capabilities Around the Core

Mature products commonly add the following. They make the core loop workable at real-world scale but do not define the Type:

- **Family/guardian account** — one account holding multiple children, guardian contacts (often a primary guardian with secondary access), saved payment methods, communication preferences, and accepted policies/waivers. The account, not the child, owns login and payment.
- **Term structure** — programs are grouped into sessions, semesters, or terms with defined date ranges and registration windows; some products instead support rolling, continuously renewing enrollment. Registration windows control when families can see and register for offerings, sometimes with priority windows for returning families.
- **Attendance and check-in** — staff record attendance on the roster; many products add a check-in kiosk or QR-code sign-in at the door. Care-oriented deployments extend this to sign-in/sign-out custody tracking.
- **Tuition billing** — recurring charges tied to the enrollment and its billing cycle (monthly, per session, or per term), automatic payment collection against a saved, explicitly authorized payment method, discounts and promo codes, payment plans, refunds, and a ledger of charges and payments per family.
- **Waitlists** — when an offering reaches capacity, further registrations enter a waitlist; when a seat opens, the operator (or the system) invites the next family to register.
- **Enrollment changes** — transfers between offerings or days, drops with recorded reasons, makeups for missed sessions, trials, and single-day drop-ins.
- **Instructor surfaces** — a staff or instructor view showing assigned rosters and attendance, with payment and financial data withheld from instructors.
- **Guardian communication** — registration confirmations, announcements to enrolled families (email, and commonly SMS), and templates.
- **Reporting** — enrollment counts, revenue, and retention views over the catalog and rosters.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:   Scheduled offering
Shapes:    recurring weekly class within a semester · fixed session with re-enrollment ·
           rolling ongoing enrollment · consecutive-day camp · one-off event

Concept:   Enrollment
Terms:     booking · registration · enrollment (per product)

Concept:   Roster
Surfaces:  admin roster view · instructor class list · check-in kiosk list
```

A reader who has only seen one implementation (for example, a semester-based class catalog) should still be able to recognize a session-based or rolling-enrollment product from the core model.

## How It Works

### 1. Build the program catalog

```text
Create offering (name, description, category)
→ set eligibility (age range or grade range)
→ set schedule (recurring weekly pattern, session dates, or term)
→ set capacity and price
→ attach forms/waivers and policies
→ publish to the registration surface
```

Scheduling is usually a distinct step from describing the offering: the operator first defines the offering, then places scheduled instances of it inside a term or semester timeframe.

### 2. Open registration

```text
Set registration window (and optional priority window for returning families)
→ offerings become visible in the guardian portal / website widget
→ guardians register children while seats remain
```

### 3. Guardian registers a child

```text
Guardian creates or opens family account
→ adds the child (age/grade, required custom fields)
→ selects an offering and a scheduled time
→ completes forms/waivers and policies
→ pays (or commits to a payment plan)
→ enrollment is created; roster updates in real time
```

If the offering is full, the registration becomes a waitlist entry instead.

### 4. Manage enrollment

```text
Monitor rosters and waitlists
→ transfer a child between offerings or days (with confirmations)
→ drop an enrollment (with a recorded reason)
→ issue makeups for missed sessions, approve trials, sell drop-ins
→ invite waitlisted families when seats open
```

### 5. Run the program

```text
Each session day:
→ staff open the roster
→ record attendance / check children in (roster, staff app, or kiosk)
→ instructors see their class list and take attendance
→ absences can trigger makeup offers
```

### 6. Bill and collect

```text
Billing cycle runs (monthly / per session / per term)
→ tuition charges posted to family ledgers
→ payments collected automatically against authorized payment methods
→ failures, refunds, and adjustments handled on the ledger
```

### 7. Communicate and report

```text
Confirmations and announcements to families (email/SMS)
→ enrollment, revenue, and retention reports for the operator
```

The loop then repeats for the next term: offerings are copied or re-created, families re-enroll (or continue, under rolling enrollment), and new rosters form.

## Interfaces

### Operator console (admin)

The administrator's primary workspace.

- catalog and schedule editors (offerings, terms/sessions, capacity, pricing)
- family and student records (guardians, children, custom fields, policies)
- roster views per offering with enrollment actions (edit, transfer, drop, waitlist)
- billing/ledger views (charges, payments, refunds, payment methods)
- reporting dashboards

### Guardian registration surface

Where families discover and buy programs.

- embedded website widget or hosted portal listing the catalog by age, category, and schedule
- offering detail (description, schedule, eligibility, price, requirements)
- checkout with family profile, forms/waivers, and payment
- family account area (enrollments, payment methods, receipts)

### Instructor / staff surface

A deliberately restricted view.

- assigned rosters and session schedules
- attendance taking (in the office portal, a staff app, or from a phone)
- student details relevant to teaching; payment data withheld

### Check-in kiosk (optional; present in some products)

A shared device at the door for student (and sometimes staff) check-in, in some products driven by scanning a code; care-oriented deployments extend it to sign-in/sign-out.

### Communication console

Templates, announcements, and message logs for reaching families — individually or by roster.

## Important Rules / Behaviors

- **Enrollment is child-specific and guardian-owned.** The guardian account holds login, payment methods, and policy acceptance; the child holds participation. In the researched products, changing the primary guardian on an account is treated as security-relevant: secondary access and stored payment authorizations do not silently carry over.
- **Capacity is enforced at the roster.** When an offering fills, registration closes and the waitlist takes over; seats reopening trigger invitations rather than open racing.
- **Registration windows gate visibility.** Offerings are only registerable inside their window; some operators reserve earlier windows for returning or priority families.
- **Term end has consequences.** Under fixed-session models, enrollments typically end when the session ends and families must re-enroll; under rolling models, enrollment continues until actively dropped. Which model applies is an operator configuration, and switching it mid-stream is treated as a structural change (enrollments are migrated, not silently re-dated).
- **Attendance is the operational record.** The roster plus attendance is what staff rely on for supervision; care-oriented deployments add sign-in/sign-out custody controls around it.
- **Recurring billing is commonly an authorized act.** Mature products commonly require that a saved payment method be explicitly authorized for recurring charges, and notify the family when that authorization changes.
- **Policies and waivers gate participation.** Acceptance is tracked per family (and re-requested when account ownership changes); some operators may record manual acceptance when paper copies are on file.
- **Instructors see rosters, not money.** Payment status and financial controls are administrator-only in the researched products.
- **Money follows the schedule shape.** Billing cycles align to how the program is scheduled (monthly for ongoing classes, per session/term for fixed programs), and proration, refunds, and payment plans are handled against that alignment.

## Variants

Common shapes of the same Type:

- **Youth activity class business** — a single-site or few-site operator (gymnastics, dance, swim, martial arts, art, STEM) running recurring classes; often adds skill/level tracking, trials, makeups, birthday parties, and merchandise sales.
- **District / community education programs** — a public operator running before- and after-school care and enrichment catalogs aligned to the school year; offerings may be free or subsidized, and registration often opens in large seasonal waves.
- **Childcare provider offering school-age care** — the after-school program is one part of a licensed care operation; the deployment carries sign-in/out custody, ratio, and compliance overlays borrowed from childcare management.
- **Camp- and event-heavy operator** — the same core used with consecutive-day camps and one-off events as the dominant offering shape.
- **Marketplace-listed provider** — the operator's catalog is also published on a parent-facing discovery marketplace, so the registration surface doubles as a storefront.
- **Multi-site / franchise operator** — many locations under one organization, with location-scoped catalogs and consolidated oversight reporting.

A variant remains a variant unless it changes the defining core; full-day licensed care changes it enough to be treated as a neighboring Type (see below).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Childcare Management System | adjacent, heavily overlapping | full-day licensed care is primary: rooms, ratios, daily reports, custody; after-school programs are scheduled part-day offerings. Vendors often sell both as one suite |
| Daycare / Preschool Management | adjacent, heavily overlapping | same care-context difference as above, for early-childhood settings |
| Camp Management System | sibling Type sharing the core | seasonal consecutive-day sessions (often overnight, with bunks/groups) vs recurring weekly school-year programs; products commonly implement both as sibling object types |
| Course Registration System | adjacent | centers the registration transaction for courses generally (including adult education); this Type centers the ongoing child-program relationship (rosters, attendance, guardian account) |
| Event Registration Platform | adjacent | one-off events without an ongoing guardian relationship or roster-based supervision |
| Tutoring Platform | adjacent | instruction delivery and tutor matching are primary; here the operator administers programs, of which tutoring may be one |
| Student Information System | different domain | the school of record for enrollment, grades, and transcripts; this Type's operator is not the school of record |
| Membership Management System | adjacent | sells and tracks memberships; here the recurring unit is a program enrollment, not a membership |

The most important boundary is with **Childcare/Daycare Management**: the two share the entire family-enrollment-attendance-billing spine, and the difference is the care context (full-day licensed care vs scheduled part-day programs). The clearest structural test: remove rooms, ratios, and licensing from a childcare deployment and what remains is this Type; remove scheduled sessions and rosters from this Type and what remains is childcare.

## Representative Products

- **iClassPro** — class management platform for youth activity centers (gymnastics, cheer, swim, dance); classes, camps, parties, POS under one operator platform
- **Sawyer (Sawyer for Business)** — registration and management software for children's activity businesses, with a parent-facing marketplace
- **CourseStorm** — registration-first platform for community education, arts organizations, and kids' programs
- **Jackrabbit (Jackrabbit Class)** — class management software for youth activity centers, sold in activity-vertical editions

The care-context boundary was checked against a childcare-suite vendor that explicitly serves before/after-school programs (Procare Solutions), to avoid defining this Type by the enrichment-class pattern alone.

## Sources

Research date: **2026-09-06**

Primary vendor documentation:

- iClassPro Support knowledgebase — https://support.iclasspro.com/hc/en-us/categories/202704148-Knowledgebase (incl. "How Do I Manage Sessions and Rolling Sessions?", "How Do I Manage Families in the Office Portal?")
- Sawyer for Business Support — https://help.hisawyer.com/ (incl. "Sawyerspeak Terminology", "How to Create an Activity", "Schedules and Listings" collection)
- CourseStorm — https://coursestorm.com/ , https://coursestorm.com/class-management-features
- Jackrabbit Technologies — https://www.jackrabbittech.com/
- Procare Solutions — https://www.procaresoftware.com/

> Sourcing limitations: the school-district community-education platform Eleyo could not be reached (support guide timed out repeatedly), and Jackrabbit's help center was unreachable from the research environment; Jackrabbit statements are positioning-level only. District-segment structures are therefore documented with reduced confidence, and precise operational details (numeric limits, exact window defaults, custody-checkout rules) are intentionally not stated in this document.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
