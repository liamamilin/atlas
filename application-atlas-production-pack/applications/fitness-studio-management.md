# Fitness Studio Management

## Overview

A **Fitness Studio Management** application is the operator-side system of record for running a class-led fitness business — a boutique studio, box, or small gym built around scheduled group classes. It holds the business's customers and their entitlements (memberships, class packs, credits, drop-in passes), publishes the recurring class schedule, runs the booking-and-attendance loop in which each reservation consumes an entitlement, and settles the money through automated billing and point-of-sale.

The defining structure is the *coupled operating loop*: customers → entitlements → scheduled classes → bookings that consume entitlements → attendance → billing → retention. Remove any leg and the product becomes a different Application Type: remove the entitlement economy and it is a class-booking tool; remove the class schedule and booking loop and it is a membership-billing system; remove the coupling between them and it is a set of disconnected tools.

Everything else the market associates with this software — branded member apps, waitlists, penalty fees, access control, marketing automation, franchise portals — is standard mature capability or variant structure, not part of the definition.

## Users & Context

Primary users, all on the operator side:

- **studio owner / operator** — configures the schedule, plans the entitlement catalog (memberships, packs, prices), watches revenue and retention, handles escalations
- **front-desk staff** — check members in, sell packs and retail, book on behalf of walk-ins, manage late cancels and no-shows, resolve payment issues
- **instructors** — see their assigned classes and rosters, take attendance, message their classes; in some products they manage their own class listings and are paid from recorded hours

Secondary user: **the member**, who books classes, buys and manages entitlements, and checks their usage through a self-service site or mobile app — but the member acts on surfaces the operator publishes; the system of record belongs to the business.

Typical context: a single commercial fitness location (or a small chain) whose revenue comes from recurring memberships and class packs consumed through scheduled classes — yoga, pilates, cycling, barre, HIIT, CrossFit-style functional training, martial arts fitness, group fitness. The owner's daily rhythm is built around the schedule: today's classes, who is booked, who showed up, whose payments failed.

## Core Model

### The Defining Core

```text
Customer of record
└── Entitlement economy
    (plans: memberships / packs / credits / drop-ins —
     instantiated per customer, billed, held in standing)
└── Scheduled class offerings
    (recurring calendar: class type + time + instructor + place + bounded spots)
└── Booking & attendance loop
    (reserve → entitlement consumed → check in → attend;
     late cancel / no-show carry consequences)
└── Money loop
    (automated recurring billing + point-of-sale settlement
     against the customer's account)
```

Four structures held jointly:

- **Customer of record** — every participant of the business is a persistent, identified person: contact details, payment methods, waivers and notes, attendance history, and the entitlements they hold. The customer record is what the whole loop hangs from; without it the product is an anonymous booking form.

- **Entitlement economy** — the business defines purchasable plans: recurring memberships (dues on a billing cycle, often with usage allowances), prepaid terms, class packs and credits (a credit typically representing one visit), single drop-ins, trials and intro offers. Each sale instantiates a plan on a customer. The instance is the working record staff act on: it carries remaining uses, billing state, and standing (active, on hold, cancelled, expired). Without this economy there is no business relationship — only a schedule.

- **Scheduled class offerings** — the studio's product is its schedule: a recurring calendar of group classes, each carrying a class type, time, instructor, place, and a bounded number of spots. One-off occasions (workshops, special events) ride the same machinery. Without the schedule there is nothing to book and no reason to hold an entitlement.

- **Booking-and-attendance loop consuming entitlements** — members reserve spots themselves (site or app) or staff book on their behalf. Each booking resolves against the customer's entitlements: a credit is deducted, or a membership usage is recorded, or a drop-in is purchased at booking time. Attendance is checked in on the roster. Late cancellation after a cutoff and failure to show carry consequences (fee, forfeited credit, infraction). This consumption coupling is the load-bearing joint: without it, a membership system and a schedule tool are merely adjacent.

### Standard Capabilities

Mature products commonly add — expected by the market, but not what makes the product this Type:

- **Member self-service surfaces** — a booking site and mobile app (often brandable) where members book, buy, manage payment details, and check remaining uses
- **Waitlists** — full classes spawn waitlists with automatic or notified placement when spots open
- **Cancellation cutoffs and penalty machinery** — per-class-type cutoffs; late cancels and no-shows trigger fees, credit forfeiture, or tracked infractions
- **Digital waivers and forms** — signed at signup, required before registration or purchase, expiring and re-collectable
- **Check-in and access machinery** — roster/register check-in, printed sign-in sheets, kiosks, barcode scanning, and in gym-format businesses door access tied to standing
- **CRM and retention** — lead capture, lifecycle stages, automated email/SMS/push journeys (renewal reminders, win-back, milestone congratulations), referrals
- **Reporting** — attendance and utilization, revenue per class type and instructor, membership status and churn, instructor hours and pay
- **Staff management** — roles and permissions, instructor scheduling, hours and pay tracking, sometimes payroll
- **POS and retail** — selling products, gift cards, and entitlements at the desk; inventory; discounts and intro offers
- **Appointments** — 1:1 services (personal training, assessments) booked alongside group classes
- **Multi-location** — shared customers or per-location scoping, cross-location reporting

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:   Entitlement plans
Forms:     recurring membership with usage allowance · prepaid term ·
           class pack / credits · single drop-in · trial / intro offer

Concept:   Booking resolution
Forms:     credit deducted per booking · membership usage counted ·
           pay-per-class at booking · free with valid plan

Concept:   Standing governance
Forms:     hold/freeze with billing pause · scheduled cancellation with reason ·
           expiry · failed-payment blocking of usage or door access

Concept:   Member surface
Forms:     shared booking site · operator-branded app · embedded website widget
```

A reader who has only seen one realization (say, a credit-per-class cycling studio) should still recognize a membership-dues gym or a paper-era studio from the same core.

## How It Works

### The operating loop

```text
Acquire:  prospect signs up (self-serve form or front desk)
          → waiver captured
          → trial / intro offer purchased
Sell:     entitlement purchased (membership, pack, drop-in)
          → billing method stored
          → recurring charge scheduled or uses loaded
Schedule: operator builds the recurring class calendar
          (types, instructors, rooms, capacity, booking windows)
Book:     member reserves a spot (app/site) or staff books on their behalf
          → entitlement resolved: credit deducted / usage recorded / drop-in bought
          → full class → waitlist
Attend:   member checks in (roster, kiosk, barcode)
          → attendance recorded against the entitlement used
          → late cancel after cutoff / no-show → fee, forfeit, or infraction
Money:    recurring dues charge automatically
          → failures retried; persistent failure can block usage or access
          → retail, gift cards, packs sold at POS
Retain:   attendance and payment data drive lifecycle statuses
          → at-risk members flagged → automated or manual outreach
          → renewal, upgrade, or cancellation (with reason recorded)
```

The loop is continuous: every class on the calendar regenerates bookings; every booking touches an entitlement; every entitlement is fed by billing; every attendance feeds retention. The operator's daily work is supervising this loop from the dashboard — today's classes and rosters, pending payments, new and at-risk customers.

### Building the schedule

The operator defines class types (name, duration, capacity, booking rules), assigns instructors and rooms, and lays out the recurring weekly pattern. Booking windows (how far in advance members may book) and cancellation cutoffs are set per class type. One-off events are created on the same calendar. Changes propagate to the member-facing schedule.

### Selling and governing entitlements

The operator builds the plan catalog: recurring memberships with billing frequency and usage limits, packs with a number of credits, drop-in prices, trials. A sale instantiates the plan on a customer with a start date and a payment method. From then on the system bills automatically, tracks remaining uses, and applies standing changes: holds pause billing and usage, cancellations take effect per contract terms, expired or failed-payment entitlements stop working — sometimes including door access.

### Running a class

Before class the instructor or front desk opens the roster: who is booked, from which waitlist, with what notes (injuries, first-timers). Members check in; staff can check in everyone, print a sign-in sheet, or mark no-shows after the window. A no-show or late cancel applies the configured consequence. The attendance record carries which entitlement paid for the visit — this is what keeps usage counts, billing, and revenue reporting consistent.

## Interfaces

Described conceptually; names and layouts vary by product.

### Business dashboard

The operator's entry surface: today's upcoming classes, pending payments, recent signups, to-dos, revenue trends. Primary actions: jump to a class roster, chase a payment, contact a customer.

### Calendar / schedule builder

The class calendar — day, week, or list view, filterable by instructor, venue, or class type. Primary actions: create/edit class types and recurring slots, cancel or reschedule sessions (with member notification), close the business for a period, adjust booking windows.

### Class roster / register

The per-class working surface: booked members with check-in state, waitlist, spot or floor-plan layout where the format uses assigned positions, notes and alerts per member. Primary actions: check in, mark no-show or late cancel, move from waitlist, swap spots, message the class.

### Customer profile

One member's whole relationship: contact details, entitlements with remaining uses and billing state, payment methods, attendance history, waivers and forms, notes and tags, lifecycle status. Primary actions: sell or change an entitlement, adjust credits, put on hold, cancel, book on their behalf, log contact.

### Plan / membership builder

The entitlement catalog: plan types, prices, billing frequencies, usage limits, contract terms, eligibility rules (new customers only, trials). Primary actions: create and retire plans, change pricing for new vs existing members.

### Point of sale

Desk-side selling: retail products, gift cards, packs, single classes, account payments. Primary actions: ring a sale, take payment (card, terminal, cash), refund.

### Reporting

Attendance and utilization, revenue by class type and instructor, membership counts and churn, instructor hours and pay, failed payments. Primary actions: filter, group, export.

### Member-facing surfaces

Booking site and/or mobile app: the published schedule, booking with one tap, waitlist joining, buying and managing entitlements, updating payment details, viewing visit history. Some products offer a separately branded app as an upgrade.

### Staff surfaces

Role-scoped access to the same system: instructors see their classes and rosters (sometimes from a dedicated staff app); front desk gets POS and check-in; managers get everything. Permissions decide who can manage forms, plans, and settings.

## Important Rules / Behaviors

- **Booking requires a resolvable entitlement.** A reservation succeeds when the customer holds a valid entitlement covering the class — an active membership with remaining allowance, a pack with credits, or a purchasable drop-in. When several entitlements qualify, the product applies a resolution rule; operators can usually adjust which one is used.
- **Money gates the entitlement.** Recurring dues are charged automatically; repeated failure triggers recovery attempts, and a persistently unpaid account can have its membership blocked from booking — and, where access control exists, from entering.
- **Standing governs everything.** An entitlement in hold/frozen state neither bills nor books; cancellation follows contract notice terms; expiry stops usage. Holds typically pause billing rather than forgive it.
- **Cancellation cutoffs are per class type.** Cancelling after the cutoff counts as a late cancel: fee, forfeited credit, or tracked infraction, depending on configuration. No-shows are marked automatically after a defined window if not checked in.
- **Waivers can gate participation.** A required waiver missing at booking or purchase blocks the action until signed; waivers can expire and require re-signing.
- **Attendance is attributed.** Each attendance records the entitlement (and payment) used, which is what keeps usage counts, dues value, and revenue reports consistent.
- **Roles bound the surface.** Staff permissions decide who can sell, refund, edit plans, manage forms, and see financials; instructors typically see only their own classes.

## Variants

- **Credit-economy boutique studio** — cycling, pilates, barre, HIIT: credits per visit, packs, assigned spots or floor plans, waitlists and penalty fees heavily used
- **Membership-economy gym / box** — functional fitness and small gyms: recurring dues with generous or unlimited usage, open-gym access, access-control hardware, workout-tracking add-ons
- **Franchise / multi-location brand** — royalty collection, brand-level standards and reporting, cross-location member rules
- **Solo / independent instructor business** — the same loop at one-person scale, lean configuration, booking-centric
- **Hybrid studio + gym** — classes plus 24/7 access, retail, and amenities in one business
- **Multi-vertical platforms** — the same product sold to martial arts schools, dance studios, climbing gyms, and wellness businesses with light vertical seasoning (belt tracking, skill levels)
- **Regional variants** — direct-debit vs card billing rails, tax-inclusive vs tax-exclusive pricing, local aggregator networks as booking sources

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Fitness Class Booking | contained slice | the booking loop is one workflow inside the studio system; a booking pure-play strips away members, billing, staff, and POS and still stands |
| Fitness Membership Management | contained slice | the membership engine (member + plan + dues/standing cycle) is one pillar here; the studio Type adds the class schedule, the consumption loop, staff, and POS |
| Gym Management System | sibling (format seam) | same product family sold across formats; the gym pole centers access-centric membership operations at larger facilities, the studio pole centers the class economy — the market boundary is format and scale, not structure |
| Personal Training Management | adjacent | centers the trainer-client appointment relationship; here appointments are a secondary booking type beside group classes |
| Dance Studio Management | vertical sibling | centers guardian-child family accounts, season-enrollment tuition, and performance machinery; here the customer is an adult individual with memberships/packs |
| Climbing Gym Management | vertical sibling | shares this business core and adds the climbing-specific safety posture and wall/routesetting layer |
| Appointment Scheduling Application | adjacent | generic 1:1 time booking with no entitlement economy or class roster |
| Sports Club / Recreation Center Management | adjacent | multi-sport, multi-program operations for clubs and municipalities rather than one commercial class-led business |
| Subscription Billing Platform | capability overlap | recurring charging exists here but bound to fitness entitlement semantics (usage, standing, access), not as a standalone billing engine |

## Representative Products

- **Mindbody** — the long-standing market-centering suite (not directly documented in this pass; see Sources)
- **Mariana Tek** — boutique franchise pole: credit economy, floor plans, franchise royalty portal
- **Glofox** — mid-market SaaS pole: branded app, CRM/retention automation, access control, multi-location
- **TeamUp** — lean international pole: booking-centric, direct-debit + card rails, independent studios
- **Zen Planner** — multi-vertical membership-billing pole: martial arts to boutique, staff payroll, retail

## Sources

Research date: **2026-09-08**

- TeamUp — feature pages and Help Centre (business collection): https://www.goteamup.com/features , https://www.goteamup.com/features/memberships , https://support.goteamup.com/en/
- Mariana Tek — product site and Knowledge Base: https://www.marianatek.com/ , https://support.marianatek.com/en/
- Glofox — product site and Help Center (User Guides): https://www.glofox.com/ , https://support.glofox.com/hc/en-us
- Zen Planner — product site: https://zenplanner.com/

> Sourcing limitation: Mindbody's official documentation could not be reached from the research environment (help-center transport errors; support portal rendering failure). Mindbody's market position is evidenced indirectly through competitor migration and comparison pages. No Mindbody-specific capability is asserted in this document. Zen Planner's documentation was reachable only at product-page level; its workflow-level behavior is asserted at feature-list strength only. Precise operational details (fee amounts, waitlist timing rules, credit-expiry defaults) are intentionally not stated; they vary by product and configuration.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
