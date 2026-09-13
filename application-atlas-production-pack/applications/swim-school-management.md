# Swim School Management

## Overview

A **Swim School Management** application is the operator-side business system for running a swim school — a learn-to-swim lesson business. It organizes the school's world into swimmer records (usually children, held on family accounts), a calendar of recurring lesson offerings grouped into progressive levels, enrollments of swimmers into those lessons, and the lesson-fee money loop over the family account.

The defining structure is small:

```text
Family / guardian account
└── Swimmer record (the learner)
    └── Enrollment in a scheduled lesson offering
        (recurring group lessons organized by level,
        plus private lessons)
        └── Lesson fees settled as payment
            against the family account
```

Everything else commonly associated with modern swim-school software — skill trees and evaluations, certificates and parent progress reports, makeup-lesson booking, check-in kiosks, parent portals, autopay — is widespread in current products but is built on top of this core, not part of it. An older, regional, or paper-era swim school (registration cards, a posted schedule of level classes, collected lesson fees, a paper progress card) has the same structure without any of the modern machinery.

Swim-school software is one realization of a broader family of class-management systems for children's-activity businesses (dance studios, martial arts schools, gymnastics clubs). What marks the swim realization is its emphasis on **level-based progression with evaluations and certificates** and on **makeup lessons** — children miss lessons, and the school must resell that time without friction. When the center of gravity shifts from the lesson business to the building itself (memberships, admissions, lane rentals across many program types), the product is serving the neighboring Recreation Center Management Type.

## Users & Context

Primary users:

- **swim school owner / manager** — configures levels, lesson offerings, and pricing; runs enrollment and billing; watches enrollment, retention, and revenue
- **deck coordinator / program supervisor** — balances rosters across classes and levels, handles transfers and placements
- **swim instructors** — take attendance, record skill evaluations poolside, view their schedules
- **front-desk staff** — register families, take payments, resolve account questions, manage check-in

Portal users:

- **parents / guardians** — the account holders. They enroll children, pay, book makeups, and follow their child's progress. The taught population is usually too young to manage its own account.
- **swimmers (children)** — the subject of every record; they appear in rosters, attendance, evaluations, and certificates rather than as account holders.

Typical contexts: independent learn-to-swim schools; municipal and community aquatic centers where swim lessons are the flagship program alongside memberships and other activities; YMCA/JCC-type community organizations; swim schools run inside larger leisure facilities, sometimes renting pool time rather than owning the pool.

## Core Model

### The Defining Core

Four structures, jointly held. Remove any one and what remains is no longer a swim-school system:

- **Swimmer record** — a persistent identified record of the learner: identity, age, guardian linkage, class history, skills, and payment context. The swimmer is the object around which attendance, progression, and fees accumulate. Without it there is only a contact list.
- **Scheduled lesson offerings** — the school's offer: recurring group lessons placed on the calendar (level, day/time pattern, instructor, pool space, capacity), organized into a progression of levels, plus bookable private lessons. Without it there is only a billing engine.
- **Enrollment** — the persisted registration of a specific swimmer into a specific lesson offering. Enrollments form rosters, consume capacity, and drive charges. Without it there is only a class directory or a sign-up form.
- **The lesson money loop** — enrollment-driven fees posted to the family account and settled by payment (stored payment methods and recurring billing in modern products; cash and manual collection historically), with unpaid balances tracked and actionable. Without it the school is not being run as a business in the system.

The family/guardian account is the dominant implementation — swim schools teach minors, so a guardian holds the payment methods, signs waivers, and receives progress reports — but adult-lesson programs can run on individual records; the invariant is the swimmer record, not the family wrapper.

### What Mature Products Add

Standard capabilities found across the researched sample. They make the core practical at poolside scale but do not define the Type:

- **Level and skill progression** — lessons organized into a progressive level scheme; per-swimmer skill records against the school's curriculum; instructors recording evaluations in real time from a staff portal; progression outputs such as certificates and parent-facing progress reports; evaluation results feeding placement in the next level.
- **Makeup lessons** — a missed lesson (recorded as an absence) generates an eligibility that the family redeems by booking into a makeup-approved class, automatically or through staff allocation. Mature swim products treat this as a first-class workflow because attendance continuity drives retention.
- **Attendance and check-in** — instructor attendance-taking from rosters, and self-service check-in kiosks so families bypass the front desk.
- **Enrollment machinery** — online self-service registration, capacity limits, waitlists, enrollment approval modes, trials, prorated billing.
- **Billing machinery** — recurring billing with failed-payment recovery, one-time charges, refunds, bundled or partnered payment processing.
- **Parent portal / mobile app** — booking lessons and makeups, paying, viewing skills and progress, receiving notifications.
- **Staff machinery** — instructor schedules, staff portal, time clocks (in some products); some products tag instructors by certification or experience to drive assignment to the right class.
- **Private lessons** — appointment-style booking against instructor availability.
- **Communication** — email/SMS/push announcements and automated reminders (enrollments, absences, cancellations, progress).
- **Waivers and emergency information** — collected at registration, attached to the family account.
- **Reporting** — enrollment, retention, class occupancy, revenue.
- **Facility scheduling** — pool/lane/space resource calendars, load-bearing for operators who run the pool, optional for schools renting water time.

### One Structure, Many Implementations

The core is written conceptually. Implementations differ in ways that matter to operators but do not change the Type:

```text
Concept:            progressive instruction structure
Implementations:    named levels with class-per-level groupings;
                    skill trees / skill banks attached to classes;
                    curriculum frameworks adopted from national
                    or industry schemes (degree of software support varies)

Concept:            makeup eligibility
Implementations:    tokens/credits generated on recorded absence;
                    staff-manual makeup allocation;
                    open makeup-booking pools

Concept:            time structure
Implementations:    fixed sessions/terms with per-session enrollment;
                    continuous monthly enrollment with autopay;
                    rolling sessions — many products support several
                    side by side

Concept:            entitlement to attend
Implementations:    enrollment/tuition (dominant);
                    prepaid punch passes;
                    household memberships (facility-led operators)
```

## How It Works

### Register, place, enroll

```text
Family creates an account (guardians + swimmers)
→ new swimmer is evaluated or placed by age/ability
→ family browses the schedule, filtered by level
→ picks a class, joins a waitlist if full, or requests a seat
→ enrollment confirmed (auto-approve or staff-approved)
→ fees attach to the family account
```

Placement is the swim-specific gate: a swimmer joins the class that matches their level, not their preference alone. Mature products let evaluation results suggest or constrain placement.

### The recurring lesson cycle

```text
Enrollment stands (for the session, or continuously month to month)
→ fees bill on the cycle (autopay or staff-collected)
→ swimmer attends; attendance recorded from the roster or kiosk
→ instructor records skill evaluations during class
→ skills complete → level completes
→ certificate / progress report reaches the parent portal
→ swimmer moves up; family re-enrolls at the next level
```

This loop — bill, attend, evaluate, progress — is the heartbeat of the business. Retention depends on families seeing progress, which is why progression artifacts (certificates, reports) are pushed to the parent portal rather than waiting for a paper day.

### Absence and makeup

```text
Swimmer misses a lesson → absence recorded
→ makeup eligibility generated (token/credit, automatic or manual)
→ family books a makeup into an approved class from the portal
→ eligibility consumed
```

Makeup machinery protects revenue and perceived fairness: the family paid for the lesson, and the school recovers the value in a future class instead of a refund.

### Private lessons

```text
Family books an open instructor slot (portal or front desk)
→ lesson scheduled against instructor and pool availability
→ charged as a one-off (or package)
→ taught and recorded like any lesson
```

### Capability tiers

**Defining core** — without these, not a swim-school system:

- swimmer records under guardian accounts
- scheduled recurring lesson offerings
- enrollment forming rosters
- lesson fees settled against the family account

**Standard capabilities** — present in most mature products:

- level/skill progression with evaluations, certificates, and progress reports
- makeup-lesson machinery
- attendance/check-in
- online registration, capacity, waitlists, approval modes
- recurring billing with recovery
- parent portal / app; staff portal
- private lessons; communication automation; waivers; reporting

**Common variants / optional** — depend on operator shape and market:

- session-based vs continuous enrollment vs rolling sessions
- prepaid punch passes; drop-ins; household memberships
- development squads (pre-team programs riding the class machinery)
- camps, parties, events; retail/POS
- pool/lane resource scheduling; admissions and access control (facility-led operators)
- branded apps and integrated websites; multi-location management

## Interfaces

Described conceptually; layouts and labels vary by product.

### Admin / office portal

The operator's control center.

- schedule of lesson offerings across levels, instructors, and pool times; live calendar
- enrollment lists, rosters, occupancy, waitlists, transfers
- family accounts: swimmers, balances, payment methods, waivers
- primary actions: build/copy schedules, manage enrollments, take payments, post charges, message families, run reports

### Staff / instructor portal (usually mobile)

Used at the pool, in the moment.

- today's rosters with swimmer names and notes
- attendance marking and absence recording
- skill-evaluation entry against the school's skill scheme
- primary actions: take attendance, evaluate skills, view schedule, clock time

### Parent portal / app

The family's self-service surface.

- class schedule filtered by child and level; book/enroll, join waitlists
- account: balances, payment methods, receipts
- child's progress: skills completed, current level, certificates, reports
- makeup booking against available makeup-approved classes
- primary actions: enroll, pay, book makeup, view progress, update account

### Check-in kiosk

Front-door surface for attendance.

- swimmer identifies themselves (name lookup, code, or card)
- attendance recorded without front-desk staff

### Facility calendar (facility-led operators)

- pools/lanes/spaces booked as resources alongside lessons, memberships, rentals, and other programs — conflict-controlled

### Reporting

- enrollment and retention trends, class occupancy, revenue, arrears; in mature products, dashboards for owners/managers

## Important Rules / Behaviors

### Capacity and waitlists govern enrollment

Lessons have bounded seats; a class that is full routes families to a waitlist. Some products let staff approve each enrollment manually; others auto-approve when a seat opens. Priority registration for existing families is a common pattern.

### Placement gates progression

A swimmer does not freely join any class: their record carries a level, and enrollment options are filtered by it. Moving up happens when evaluations show the level's skills complete — and is celebrated with parent-facing artifacts (certificates, reports).

### Makeup eligibility is absence-gated

Makeup booking is not open swimming: eligibility arises from a recorded absence (commonly realized as tokens or credits), applies to designated makeup-approved classes, and is consumed on use. Products differ on automation, expiry, and eligibility scope; the eligibility pattern itself is the common structure.

### Money follows enrollment, on the operator's clock

Fees are generated by enrollment, not by attendance. Under continuous enrollment, billing recurs on a cycle whether or not every lesson was attended (makeups absorbing misses); under session enrollment, the term's fees post at registration, with prorating and blackout-date handling common. Unpaid balances surface in the admin portal for follow-up.

### The family account is the financial and communication unit

One balance, one set of payment methods, one inbox — across multiple swimmers. Progress reports, absence notifications, and payment reminders flow to the guardian.

## Variants

- **Independent swim school** — dedicated learn-to-swim facility; the class-management core is the whole system.
- **Municipal / community aquatic center** — lessons alongside memberships, admissions, lane rentals, and other programming on one platform; facility scheduling and access control swell in importance.
- **YMCA / JCC / community organization** — lessons as one program line of a multi-program membership operation.
- **Leisure-facility swim school** — a school renting water time; minimal facility machinery.
- **Session-based vs continuous operation** — fixed terms with per-term enrollment vs perpetual monthly enrollment; many products support both, and some schools mix them (e.g., school-year sessions, summer continuous).
- **Private-lesson-led operations** — appointment-driven revenue beside or beyond group lessons.
- **Competitive-bridge programs** — development squads preparing swimmers for club/team swimming, run on the same class machinery; full team/competition operations are a different Type.
- **Regional markets** — products concentrate in North America and Australasia/UK; curriculum alignment and terminology vary by market.

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| Martial Arts School Management | same family sibling | shares the family-account/class/enrollment/tuition spine; its signature is rank/testing/promotion machinery and continuous memberships, not level-evaluation cycles and makeup emphasis |
| Dance Studio Management | same family sibling | shares the spine; its signature is the season/session container plus costume/recital/competition machinery |
| Gymnastics Club Management | same family sibling (unprocessed) | expected to share the spine with skill-tracking as its signature; boundary to be confirmed by its own research pass |
| Sports Academy Management | sibling | broader training organization (lessons, camps, clinics, teams) over an athlete population; swim school is a single-activity lesson business |
| Recreation Center Management | adjacent (facility-first) | centers the building — membership entitlements validated at entry, many activity types, facility operations; swim lessons are one program line |
| Sports Club Management | adjacent | member organization with teams, seasons, and volunteers rather than a lesson business with levels and rosters |
| Swim-team management software (team/meet systems) | adjacent market | rosters of competitive swimmers, meet entries, and performance times; no lesson business, levels, or family fee loop at the center |
| Sports Registration Platform | weaker overlap | one-shot registration transactions for programs; no ongoing lesson relationship, progression, or recurring fees |
| Membership Management System | component | generic dues/lifecycle engine without lessons, levels, or rosters |
| School Management System / SIS | different domain | educational institution records; the swim school is a commercial lesson business |
| Childcare Management System | different domain | care context (rooms, ratios, custody check-in/out) vs scheduled lessons |

The closest boundaries are within the family: every sibling sells the same spine, and the vertical identity lives in the signature layer. The distinguishing swim structures are the level-evaluation-certificate cycle and first-class makeup machinery — remove them and add the sibling's signature, and the product becomes the sibling.

## Representative Products

- **iClassPro** — class-management platform with a dedicated swim-school offering; documents the swim pedagogy layer (skill trees, evaluations, certificates, progress reports) and makeup-token machinery in depth
- **Dash** — recreation-facility platform with an aquatics/swim-club solution; the facility-led pole (memberships, lane/resource scheduling, lesson registration, check-in)
- **Amilia** — recreation and membership platform serving swim schools inside municipal/community aquatic organizations; the community-aquatics pole

The market also includes vertical editions of the broader class-management family (a dedicated swim edition exists alongside dance, cheer, and music editions from one family vendor) and leisure-platform swim-course modules; those were identified but not directly researchable in this pass.

## Sources

Research date: **2026-09-09**

Official product surfaces:

- iClassPro — Swim School Software Features: https://www.iclasspro.com/swim-software-features
- iClassPro — Skill Tracking: https://www.iclasspro.com/skill-tracking
- iClassPro — home: https://www.iclasspro.com/
- Dash — home: https://dashplatform.com/
- Dash — Swim Club Management Software (Aquatics): https://dashplatform.com/solutions/swim-club-management-software/
- Amilia — home: https://www.amilia.com/
- Amilia — Swim School Management & Registration Software: https://www.amilia.com/industry/swim-school-software
- Jackrabbit Technologies — corporate home (family product map): https://jackrabbittech.com/

Cross-observation context from prior research passes in this project: sports-academy-management (iClassPro class-management operational detail), dance-studio-management, martial-arts-school-management, recreation-center-management, sports-club-management.

> Sourcing limitation: vendor product-site pages only — no help-center or knowledge-base article bodies were retrieved, and two candidate products could not be fetched at all (a dedicated swim vertical edition of a class-management vendor returned access errors; a UK/ANZ swim-course specialist timed out). Precise operational parameters (makeup-token expiry rules, billing-cycle defaults, level-count structures, numeric limits) are intentionally not stated in this document. Claims about makeup machinery rest on one product's in-depth documentation plus family-level precedent, and are worded accordingly; claims about the level/progression layer reflect two of the three sampled products. Product-by-product observations, the cross-product matrix, and vendor-specific detail are recorded in the paired Research Notes.
