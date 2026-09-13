# Research Notes — Fitness Class Booking

Directory leaf: Fitness Class Booking (§28 Sports, Fitness & Recreation)
Research date: 2026-09-07
Methodology: v1.1 (update-v1/)

## Research Goal

Understand what a "Fitness Class Booking" application actually is as an Application Type: what objects and loops make it up, how the operator side (schedule) and customer side (reservation) fit together, how bookings relate to money and entitlements, and where its boundary lies against Fitness Studio Management, Appointment Scheduling, Event Ticketing/Registration, Course Registration, facility-booking siblings, and class marketplaces.

## Initial Boundary

- **Working hypothesis**: an application that lets a fitness/wellness business publish a schedule of group class occasions (time, instructor, place, capacity) and lets identified customers reserve spots in those occasions, with the reservation persisted as a roster record and managed through cancellation/waitlist/attendance.
- **Nearest neighbors**: Fitness Studio Management (whole-business suite), Fitness Membership Management, Gym Management System, Appointment Scheduling Application (1:1), Event Registration Platform / Event Ticketing Platform (one-shot events), Course Registration System (education), Sports Court Booking / Amenity Booking Platform (facility slots), Restaurant Reservation Platform (structural sibling), Service Marketplace (ClassPass-style aggregation), Recreation Center Management.
- **Known tension going in**: the climbing-gym-management pass characterized Fitness Class Booking as a "capability slice" (booking is one workflow inside a management system). The directory nevertheless lists booking-centric leaves separately elsewhere (Sports Court Booking, Tee Time Booking Platform, Amenity Booking Platform). The keep-vs-slice question is a primary research question.
- **Unknowns**: is booking a standalone Type or only a module? How do products structure class objects (template vs instance)? How do bookings resolve against money/entitlements? Waitlist/cancellation mechanics? Historical (paper-era) fit?

## Research Questions

1. What is a "class" as an object — repeating template, dated occasion, or both? How do products model the class type → schedule → occasion relationship?
2. What is a booking/reservation record, what states does it carry, and who creates it (customer self-service vs staff on behalf)?
3. How does capacity work (spot limits, full/available state), and how do waitlists fill vacated spots?
4. How does a booking resolve against money and entitlements (membership, class pack/credits, pay-per-class, free)?
5. What cancellation rules exist (windows, cutoffs, late-cancel and no-show consequences), and what happens to the released spot?
6. What surfaces exist on each side (operator calendar, roster; customer app/web schedule, my-bookings; check-in)?
7. Where do adjacent shapes (appointments, courses/enrollments, facility rentals, one-off events) sit relative to the class booking loop — inside the product as siblings, or outside the Type?
8. What makes this Type different from Appointment Scheduling, Event Registration/Ticketing, Course Registration, and the studio-management suites?
9. Historical check: would the paper sign-up sheet / punch-card era still satisfy the definition?

## Representative Products

Selected for market-representation spread, documentation depth, and different product philosophies/customer tiers:

1. **TeamUp** — booking-centric SaaS for independent studios and coaches (SMB pole); markets itself around class booking; extensive public help center. Evidence: **A** (help center directly observed, multiple collections/articles).
2. **Bookwhen** — vertical-agnostic class/event booking platform (UK); sells the same booking loop to fitness instructors, pottery workshops, children's activities. Evidence: **A** (help center directly observed). Included deliberately as the abstraction check: proves fitness-specific machinery is not definitional.
3. **Glofox (ABC Glofox)** — boutique studio/gym all-in-one platform where scheduling & booking is one pillar among many (suite pole); strong product-page documentation of the booking feature set. Evidence: **B** (official product pages, feature-level; help center not fetched).
4. Mindbody — the category's best-known incumbent; **NOT researched**: support site is a JS-gated Salesforce community (CSS error) and product pages 404'd from the research environment. Named below only as market context, with **no capability claims** drawn from it.

Rejected candidates: ClassPass (marketplace — belongs to Service Marketplace territory, not this operator-side Type); WodBoard/Fitli (smaller samples, redundant with the poles already covered).

## Sources

TeamUp (all fetched 2026-09-07):
- Help Centre root — https://support.goteamup.com/
- For Business Owners, Admins, Instructors (collection) — https://support.goteamup.com/en/collections/9210299-for-business-owners-admins-instructors
- Classes (collection) — https://support.goteamup.com/en/collections/9210344-classes
- Waitlist overview — https://support.goteamup.com/en/articles/10471958-waitlist-overview
- An overview of events: Classes, Appointments, and Courses — https://support.goteamup.com/en/articles/9327728-an-overview-of-events-classes-appointments-and-courses-video
- For Members, Athletes and Customers (collection) — https://support.goteamup.com/en/collections/9210326-for-members-athletes-and-customers

Bookwhen (all fetched 2026-09-07):
- Help Centre root — https://support.bookwhen.com/
- Events & Schedules (collection) — https://support.bookwhen.com/en/collections/1535785-events-schedules
- Entry overview — https://support.bookwhen.com/en/articles/753342-entry-overview
- Waiting Lists — https://support.bookwhen.com/en/articles/753351-waiting-lists
- FAQ: Choosing between passes and memberships — https://support.bookwhen.com/en/articles/8698222-faq-choosing-between-passes-and-memberships
- Cancelling and transferring tickets — https://support.bookwhen.com/en/articles/753657-cancelling-and-transferring-tickets

Glofox (fetched 2026-09-07):
- Home — https://www.glofox.com/
- Scheduling & Booking feature page — https://www.glofox.com/features/scheduling/

Market context (no capability claims): Mindbody (unreachable — see limitation below); Glofox's own comparison/integration pages naming Mindbody, ClassPass, Gympass, Wellhub.

> Source-access limitation: Mindbody's support site returned a Salesforce "CSS Error" and two product-page URLs 404'd. Per the network-restriction rule the source was abandoned after these failures; no Mindbody operational detail is asserted anywhere in this research or in the final document, and the market-centering pole is evidenced only indirectly (via Glofox's positioning and comparison pages).

## Product Observations

### TeamUp (evidence layer A)

**Object structure.** The business schedules *event types*: **Classes**, **Appointments**, **Courses**, plus one-off events and **Rentals** (book spaces — courts, studios, saunas, rooms — "without attaching an instructor or fixed class timetable"). The product's own overview article distinguishes them: a Class is "a group session that customers register for individually," one-off or repeating (weekly/bi-weekly), charged per session, paid via membership or per-session payment; an Appointment is one-to-one or small-group, "connects directly to your team's availability" (staff availability windows); a Course is "a structured program made up of multiple linked sessions" — one registration enrolls the customer in **all** sessions, charged per course, not per session. (A)

**Class object hierarchy.** A **Class Type** carries name, pricing ("how you can charge customers for class registrations... per class type"), visibility, and a schedule; the schedule generates **time slots** (dated occasions) with venue, class size limit, and instructors. Per-occasion operations exist beside the template: edit/cancel a class on a specific date and time, un-cancel a cancelled class, change class name, end a time slot, bulk-edit venue/class size/instructors across slots, bulk cancel between two dates and mark the business closed for a date range, alternate pricing for specific class times, donation-based classes. (A)

**Registration settings.** "Registration Timelines": registrations open (how far in advance customers can book), registrations close, and a **cancellation cutoff time**, settable per class type, with per-class override. **Priority Booking** creates preferential registration settings for customer groups. **Age restrictions** on class types. Calendar settings control the customer-facing calendar (timezone, attendee visibility, waitlist info display, filters). (A)

**Waitlists.** Dedicated settings: auto-registration (eligible customers with memberships, or free events, are **automatically** moved from waitlist to class if a spot opens more than a configured time before start); below that threshold the customer must **manually claim** within a "reserved time" window or the spot passes to the next person; waitlist max size; per-class waitlist capacity override; waitlists can be disabled per class type. Eligibility for auto-registration: "completed all necessary forms, signed the waivers, hold an applicable membership, and have available credits." A "Nightly Blackout Period" governs waitlist spot expirations and class cancellations. Waitlists "are only applied to Classes, and are currently not available for Courses or Appointments." Push notifications announce waitlist spots in the member app. (A)

**Entitlements and money.** Customers "register using their membership, or pay per session"; class packs ("Record a class usage against a customer's class pack — deduct a credit from a customer's membership"; check remaining uses; "Pack Running Low" notifications; complimentary credits); memberships (recurring billing, holds, upgrades/downgrades); "I have multiple memberships valid to use for the same event" (entitlement resolution at booking is a documented scenario); account credit; Apple Pay/Google Pay at checkout; refunds when a customer removes themselves from a class. Staff can register a customer for a class (booking on behalf) and record a class usage manually. (A)

**Discipline and attendance.** "How to track and action no shows"; **Penalties and Infractions** with a resettable penalty counter and penalty notifications; late-cancellation notifications; customer check-ins (set up and manage); "All Attendances" report ("identify at-risk customers, track no-shows, review membership usage"); attendance check-off on the calendar. (A)

**Customer side.** Member Booking App + web Customer Site: sign up/sign in (a TeamUp customer account connects across businesses), view the schedule, register for a class or course session, edit or cancel a class reservation, unregister from a class, make a recurring reservation for a class time slot, view attendances, export upcoming registrations to personal calendars (iCal/Google/Outlook), complete waivers/questions before booking, family member accounts. (A)

**Adjacent machinery.** Staff permissions; instructor hours/pay reports; venues and rooms; forms/waivers/policies gating registration; CRM lifecycle pipeline; POS; notifications (registration confirmations, pre/post class, staff pre/post class notifications, broadcast SMS). (A)

### Bookwhen (evidence layer A)

**Object structure.** An **Entry** is "a term for an event on your schedule. It can be a single date for a once-occurring event, a course, or an entry covering multiple dates for a recurring event." Entry tabs: Information, Location, Dates & Times, Booking form, Tickets & Costs (with **Maximum event size** = capacity), More options. Changes in an entry affect all its dates; per-date amendments and per-date capacity overrides exist. **Schedules** are public booking pages (multiple schedule pages per account, reorderable, duplicable; monthly/termly schedules; the difference between a scheduling page and public page is documented). A **Leader** (person leading the event) with public profiles; **Locations** managed per entry. (A)

**Booking model.** Customers book through the public page (embeddable iframe, filter buttons, password-protected/private/invite-only entries); a **Booking** is the transaction container with a booking reference; tickets attach per attendee; "Event capacity vs ticket availability and maximum tickets per booking" distinguishes event capacity from per-booking ticket limits. Staff add attendees manually; test bookings are distinct from customer bookings. (A)

**Cancellation/transfer lifecycle.** Admins cancel or transfer tickets from the Bookings page; cancellation "cannot be undone," does **not** automatically refund (refunds are a separate admin action), and notifies attendees; transfers move a ticket to another entry/date (upcoming only), with a documented restriction matrix (no transfer between schedules, between single and course tickets, for different course lengths, for cancelled tickets, to unpublished/unavailable events); course transfers add the attendee only to upcoming dates with an "owed" amount for price differences; customers can transfer via the customer portal where the business enables it ("Allow ticket cancellations", "Allow ticket transfers" in Booking preferences); deleting a booking exists for paper-trail-free cleanup (unavailable for some paid bookings). (A)

**Passes and memberships.** "Passes and memberships both offer flexible ways to package your events." A **pass** is a one-off payment for a fixed or unlimited number of uses within a timeframe (fixed calendar window, no expiry, or window from first use); a **membership** is recurring billing with a usage allowance per period, unlimited access, or discounted tickets. Pass use can be configured to be **returned on ticket cancellation** ("Pass use returned on cancellation" preference). Group/family passes; gifting passes; pass-usable "exclusive tickets" restricted to members/pass-holders. The FAQ explicitly cross-verticals: "A fitness instructor might opt for a membership, while a pottery workshop provider might prefer a specific pass." (A)

**Waitlists.** Notify-based: when an event is fully booked, customers join a waiting list (name/email); when a spot opens, the system emails the first person a unique booking link; each person has a configurable window (each customer has 30 minutes to complete booking in the documented example) before the next person is notified; the event stays marked fully booked to the public during processing; if nobody claims, the spot reopens publicly. Waitlists are per-date (each date of a course has its own list); waiting-list-only entries (capacity 0) harvest demand; waitlists don't trigger after an event has started; capacity increases during processing wait until the list is processed. (A)

**Adjacent machinery.** Checkout reservation periods (incomplete checkouts hold spaces); customer groups for priority bookings; discount codes/bulk discounts; vouchers; reporting; OpenActive data sharing; API/calendar feeds. (A)

### Glofox (evidence layer B — official product pages only)

**Positioning.** "All-in-one" platform for gyms/studios ("fitness management software"); Scheduling & Booking is one of nine marketed features beside Membership Management, Billing & Payments, CRM, Check-in & Access Control, Staff Management, Multi-location, Reporting, Branded Member App. Owned by ABC Fitness ("ABC Glofox"). (B)

**Scheduling & Booking feature claims.** "Set up recurring classes, courses, and appointments"; "members book instantly from your branded app or website"; "automated waitlists and reminders." Step descriptions: build recurring classes with instructor assignment and availability, capacity limits, **booking windows and cancellation policies per class**, copy entire weekly schedules, room assignments; members book classes, appointments, and **facilities** (saunas, courts) from the member app; **embed a booking widget** on the studio website; **interactive room map spot selection** ("choose their preferred spot"); instant confirmation and automated pre-class reminders (email/SMS); dynamic waitlists filling cancelled spots; **no-show penalty rules** and **late-cancel fees**; tracking late cancellations, no-shows, and class performance; manage classes, appointments, courses, and facility time from one calendar with per-offering booking windows, pricing, capacity, and access rules ("which memberships can access specific classes"); staff app (Glofox Pro) to view schedules, manage bookings, check clients in, view waitlists and roster tags, edit/cancel classes, manage trainer schedules. Family/friend bookings; booking windows and class restrictions by membership type. (B)

**Demand channels.** "Open your schedule to millions of wellness platform users. Members on ClassPass, Gympass, and Wellhub discover and book your classes directly" — external marketplaces push demand into the operator's schedule. (B)

**FAQ-level claims.** Members book via branded app or web booking experience; dynamic waitlists, automated waitlist confirmations, no-show penalty settings; group classes, PT appointments, courses, facility bookings from one calendar with configurable schedules/pricing/capacity/booking windows/cancellation settings; multi-location support. (B)

### Cross-product Comparison

| Structure | TeamUp (A) | Bookwhen (A) | Glofox (B) | Layer |
|---|---|---|---|---|
| Operator-published schedule of class occasions | Class Type → time slots; calendar | Entry (single/multi-date/recurring) → public schedule page | recurring classes, copy weekly schedules, one calendar | **L0** |
| Occasion attributes: time, leader, place, capacity | venue, instructors, class size per slot | dates & times, leader, location, Maximum event size | instructor, room, capacity limits | **L0** |
| Spot reservation by identified customer, persisted on a roster | registration (self or staff on behalf) | booking + tickets + attendees | members book via app/web widget; roster | **L0** |
| Bounded spots; release & re-book loop | class size limit; unregister/cancel; waitlist refill | capacity; cancel/transfer tickets; waitlist or public reopen | capacity; waitlists fill cancelled spots | **L0** |
| Ongoing customer relationship across bookings | memberships/packs; recurring reservations | passes/memberships; booker portal | memberships/credit packs; member app | **L0** (relationship), forms vary L1/L2 |
| Recurring-template machinery with per-occasion overrides | Class Type vs per-date edit/cancel/un-cancel | entry vs per-date amendment/capacity override | recurring setup + per-class overrides | L1 |
| Waitlist with expiry/claim mechanics | auto-registration vs manual claim; reserved time; max size | notify-by-email with booking window; per-date lists | "dynamic waitlists"; automated confirmations | L1 |
| Cancellation cutoffs + late-cancel/no-show consequences | registration timelines; penalties/infractions; no-show reports | admin/customer cancellation restrictions; no auto-refund | cancellation policies per class; no-show/late-cancel fees | L1 |
| Entitlement resolution at booking | membership/pack/account credit; multi-membership case; free events | pass/membership covers ticket; pass-use return on cancel | memberships grant access to specific classes; credit packs | L1 |
| Customer self-service surfaces | Customer Site + Member Booking App | public page + booker help center/portal | branded member app + web widget | L1 |
| Booking on behalf (front desk) | register a customer for a class | add attendees manually | staff app check-in/booking | L1 |
| Attendance/check-in + no-show flags | check-ins; attendance check-off; All Attendances report | attendee lists; booking statuses | staff app check-in; attendance milestones (suite) | L1 |
| Reminders/confirmations | registration confirmations; pre/post class notifications | confirmation/notification emails (documented in waitlist flow) | automated reminders email/SMS | L1 |
| Courses/enrollments (book the series at once) | Course type: one registration = all sessions, per-course price | course entries; per-date waitlists; course transfer rules | courses ride the same calendar | L2 |
| Appointments (staff-availability slots) | distinct event type; "transitioning from classes to appointments" | appointment-based events/schedules documented | appointments in same calendar | L2 |
| Facility rentals (court/room/sauna slots) | Rentals ("courts, studios, saunas, rooms") | appointment-based events for children's activities | facility bookings (saunas, courts) | L2 |
| One-off events/workshops | one-off events with own pricing | single-date entries | workshops | L2 |
| Spot selection / room maps | — (not observed) | — (not observed) | interactive room map | L2 (single-product at evidence level) |
| Priority booking windows by customer group | priority booking | customer groups for priority bookings | access rules by membership | L1 (concept), mechanics vary |
| External marketplace demand channels | — (not observed) | OpenActive data sharing | ClassPass/Gympass/Wellhub integration | L2 |
| Online/virtual class delivery | Online Classes collection (74 articles); On Demand section | online events collection | member app booking (online not explicit on fetched pages) | L2 |
| Family/dependent booking | family settings; family app management | group and family passes/tickets | family and friend bookings | L2 |
| Multi-location | venues; (multi-location not emphasized) | schedule pages (per-venue concept) | multi-location feature pillar | L2 |

## Canonical Model — Four Abstraction Layers

### L0 — Defining Invariant (minimal)

Three structures, held jointly:

1. **The class schedule of record.** The operator maintains and publishes a calendar of scheduled group class occasions — each occasion carrying a time, a leader (instructor), a place (room/venue, or a virtual location), and a bounded number of spots. Recurring programs (the same class across weeks) are the dominant shape; one-off occasions ride the same machinery. Remove → a timetable poster / class listing (display, not booking).
2. **The spot reservation.** An identified customer reserves a place on a specific occasion; the reservation persists as a roster record against that occasion; it can be created by the customer self-service or entered by staff on the customer's behalf. Remove → attendance tracker, waitlist form, or a marketing sign-up list.
3. **The bounded, reversible spot economy over an ongoing schedule.** Spots are countable and finite (full/available state is real); a reservation can be released and the spot re-offered to someone else; and the same customers return to book repeatedly across the schedule — the loop is ongoing, not one-shot. Remove the boundedness+release → unlimited sign-up form; remove the ongoing relationship → one-shot event registration.

Jointly-held is load-bearing: schedule + reservation without bounded/reversible spots = event sign-up; reservation + spot economy without the operator's group-class schedule = appointment scheduling; schedule + spot economy without reservations = a display calendar.

### L1 — Common Mature Structure

- Recurring class templates generating occasions, with per-occasion overrides (edit/cancel one date, substitute, capacity change) beside the template
- Waitlists that fill vacated spots in order, with time-boxed claim windows (automatic placement or notified claim — both documented forms)
- Cancellation cutoffs/windows; late-cancel and no-show recording with consequences (fees/penalties) and reporting
- Entitlement resolution at booking: recurring membership with usage allowance or unlimited use, class pack/credit bundles with expiry, pay-per-class, free admission — the reservation consumes or is covered by something
- Customer self-service surfaces: public/app schedule browsing, booking, my-bookings management, calendar export
- Booking on behalf at the front desk; instructor-facing roster; attendance check-in and no-show flags
- Confirmation and reminder messaging (email/SMS/push)
- Booking windows (how far in advance), priority windows for customer groups, participant restrictions (age etc.)
- Reporting: attendance, no-shows, class utilization, revenue per class/instructor

### L2 — Variant / Optional Structure

- Course/enrollment objects (one booking covering a multi-session program, priced per program) — documented as a distinct event type inside products; season/tuition-style registration remains education territory
- Appointments (staff-availability slots) and facility rentals (courts, rooms, saunas) riding the same calendar
- One-off events/workshops with own pricing
- Spot selection (room/bike/mat maps), family/dependent and book-a-friend bookings
- External demand channels (wellness marketplaces pushing bookings into the schedule; open data sharing)
- Online/virtual class delivery and on-demand libraries
- Private/invite-only/password-protected classes; multi-location/franchise operations; branded native apps
- Cancellation-fee automation depth; credit return on cancellation as a configurable policy

### L3 — Vendor-specific Structure (research notes only)

- TeamUp: Class Type → time-slot model; nightly blackout period for waitlist expirations; documented default waitlist mechanics (1-day auto-registration cutoff; 30-minute reserved-time window); penalty/infraction counter with resets; waitlists only for Classes (not Courses/Appointments); Rentals as a named event type; Stripe Terminal POS; membership holds with payment rescheduling; CRM lifecycle pipeline.
- Bookwhen: entry model (one entry = event definition holding many dates); notify-by-email waitlist processing with a 30-minute-per-person window in the documented example; booking references; the transfer restriction matrix (no cross-schedule transfer, no single↔course transfer, equal-length course-to-course); "pass use returned on cancellation" preference; checkout reservation periods; OpenActive sharing; plan-gated transfers/waitlists.
- Glofox: interactive room map spot booking; branded member app + staff app (Glofox Pro); ABC Fitness suite coupling (Trainerize for coaching); class-fills/no-show cost calculators; royalty-structure multi-location.

## Rejected Findings (deliberately NOT definitional)

- **Memberships/class packs** — the credit economy is the fitness market's signature, but the vertical-agnostic sample sells the identical booking loop with passes/memberships as one packaging option among free and pay-per-booking, and donation-based classes are documented. Money form is variant; the entitlement *resolution step* is common-mature, not invariant.
- **Waitlists** — disable-able per class type in one sample; plan-gated in another; the paper era just stayed full. Common mature, not defining.
- **Apps / online self-service** — front-desk and phone booking satisfy the Type; self-service is the modern default, not the definition.
- **Check-in/attendance** — the roster's terminal states are common mature; a booking system that only holds the roster still qualifies (paper tick-sheet era).
- **Course/enrollment objects** — real and documented inside products, but the Type stands on per-occasion reservation; whole-series enrollment is the Course Registration shape (kept as L2 sibling inside the loop).
- **Fitness-specific content semantics** — the vertical-agnostic sample proves the structure (schedule + reservation + spot economy) carries no fitness-specific invariant; fitness is the dominant market realization with fitness-specific entitlement and waiver conventions.
- **Payments at booking** — free and donation-priced classes are directly documented; payment cannot be an invariant (same conclusion as the sibling event-ticketing pass).

## Historical / Market-Sample Check

Paper-era realization: the weekly sign-up sheet at a studio/gym front desk — the operator posts the week's class schedule (rows = occasions), each row has a finite number of lines (bounded spots), members write their names (self-service reservation), staff strike through names to release spots (cancellation/re-release), the instructor reads the sheet at class time (roster), and the same members return every week (ongoing relationship). No apps, waitlists, online payment, or credit automation are required — the L0 holds. Punch cards as the entitlement substrate (pass use consumed at attendance) also predate automation. Community/recreation-center class registration (a regional/institutional realization) fits the same core. Historical check **passed**: nothing in L0 requires the current SaaS implementation.

## Boundary Findings

1. **vs Fitness Studio Management / Gym Management System** (directory siblings): those Types center the whole business — members, memberships/billing, staff, POS, access control — with class scheduling as one module. This Type centers the booking loop itself. Removal tests both directions: strip everything but the booking loop from a studio suite and the remainder is still a working class booking product (the pure-play pole exists and sells exactly this); strip the booking loop from a studio suite and it still manages memberships, billing, staff, and POS. Keep-both with a center-of-gravity seam; the capability-slice characterization from the climbing-gym pass is honored by noting that inside suites booking *is* a workflow, while the standalone Type is ratified by the pure-play market.
2. **vs Appointment Scheduling Application**: appointments are individual slots generated from a staff member's availability; a class is a scheduled group occasion on the operator's published program with bounded spots. The sampled products themselves separate the two (one product documents "the difference between Classes and Appointments" and even a migration guide; another documents appointment-based schedules as a distinct setup). Remove the group class program and per-occasion group roster → appointment scheduling.
3. **vs Event Registration Platform / Event Ticketing Platform**: one-shot events center the occasion and (in ticketing) the sold ticket artifact as a checkable entitlement; class booking centers the ongoing schedule and the roster, with no ticket artifact. Remove the recurring schedule + ongoing customer relationship (sell individual dated admissions with tickets) → event registration/ticketing. One-off workshops are the L2 degenerate case inside this Type's machinery.
4. **vs Course Registration System (education)**: course registration enrolls a person in a program/term with tuition; class booking reserves spots in individual occasions. Products document the seam internally (one sample prices classes per session and courses per program; another's course transfers only carry upcoming dates). Season-enrollment-with-tuition remains the education/children's-activity family (see the dance-studio pass); drop-in/per-occasion reservation is this Type.
5. **vs Sports Court Booking / Amenity Booking Platform**: facility booking reserves time on a resource (court, room, sauna); class booking reserves a participant spot in a staffed program. Both appear inside sampled products as sibling capabilities (Rentals; facility bookings) — cross-capability presence supports keep-separate Types.
6. **vs Service Marketplace (ClassPass class)**: the marketplace aggregates many operators' schedules and sells cross-operator access; here the operator publishes its own schedule and the customer books into it. Marketplace demand arrives as an integration channel (documented), i.e., a handoff seam, not a merger.
7. **vs Fitness Membership Management**: membership/billing is one structure (entitlements) inside this Type's booking resolution; the membership pass owns the billing relationship lifecycle. Here memberships appear only as the thing a booking consumes or is covered by.
8. **vs Restaurant Reservation Platform**: same abstract reservation shape (party books a slot with capacity bounds), different domain semantics (tables/sittings vs program spots; no entitlement economy). Structural sibling, not the same Type; not deep-researched this pass.

## Taxonomy / Boundary Issue

- **Capability-slice tension (for joint review)**: the climbing-gym-management pass recorded Fitness Class Booking as "a capability slice (offerings/calendar) inside the management system." This pass ratifies keep-both (booking-loop pure-plays are a real, marketed product form) and proposes the center-of-gravity seam in Boundary Finding 1 for joint review when **fitness-studio-management** and **fitness-membership-management** are processed.
- **Family note**: the dance-studio-management pass flagged one class-management product family realized per vertical (children's activity classes, tuition/enrollment). This Type is adjacent but structurally distinct — per-occasion reservation of drop-in spots by individual adults with a credit/membership economy, vs guardian-child season enrollment with tuition. The seam is documented inside a single sampled product (its own Classes-vs-Courses split).

## Uncertainties

- Mindbody, the category's largest vendor, could not be reached; the market-centering suite pole is evidenced indirectly (via Glofox's positioning and the general market frame). No Mindbody-specific mechanics are asserted.
- Glofox evidence is feature-page level (B): detailed waitlist mechanics, cancellation-window granularity, and penalty rule configuration were not verifiable at help-center depth; no numeric parameters asserted for it.
- Check-in/attendance depth and instructor-substitution workflows were observed only at collection-title level for some products (attendance check-off, staff app check-in); treated as common-mature at capability level, without mechanics.
- Whether waitlist auto-registration (vs notify-and-claim) is the dominant market pattern is unknown; both forms are directly documented, ratio not established.
- Consumer-marketplace pole (ClassPass consumer app) not researched; its placement as a marketplace Type rests on the boundary reasoning, not on direct study.
- Pricing/packaging differences (plan-gating of waitlists/transfers) observed in one product each; not generalized.

## Final Synthesis

A Fitness Class Booking application is the booking-loop system for scheduled group fitness classes: the operator publishes and maintains a recurring schedule of class occasions — time, instructor, place, and a bounded number of spots — and identified customers reserve spots on specific occasions, self-service or through the front desk, with the reservation held as a persistent roster record. The defining loop is ongoing and reversible: customers book repeatedly across the schedule under the operator's admission rules (membership, class pack, per-class payment, or free), cancellations release spots that are re-offered through waitlists or public availability, and the roster becomes the operational state the class runs on (check-in, no-shows, instructor view). Everything else the market associates with modern products — branded apps, room-map spot selection, automated late-cancel fees, course and appointment siblings on the same calendar, marketplace demand channels — is common mature structure or variant, not the definition. The Type's edge: remove the recurring group-class schedule and it becomes appointment scheduling or event registration; remove the booking loop and it becomes studio management; aggregate many operators' schedules and it becomes a marketplace.
