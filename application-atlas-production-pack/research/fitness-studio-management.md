# Research Notes — Fitness Studio Management

## Research Goal

Understand what software sits under the directory leaf "Fitness Studio Management" (§28 Sports, Fitness & Recreation, listed between "Fitness Class Booking" and "Personal Training Management"): what objects it manages, what the studio's operating loop is, how money and entitlements couple to classes and attendance, and where its boundary lies against the already-processed slices (Fitness Class Booking, Fitness Membership Management), the unprocessed sibling Gym Management System, the vertical siblings (Dance/Climbing/Martial Arts Studio Management), and Personal Training Management.

## Initial Boundary

- Working hypothesis: an operator-side whole-business system of record for a class-led fitness business (boutique studio, box, small gym): customers/members with entitlements (memberships, class packs, credits, drop-ins), a recurring class schedule with instructors, a booking/attendance loop that consumes entitlements, automated billing and point-of-sale, staff operations, and member-facing self-service.
- Nearest neighbors: Gym Management System (unprocessed sibling — suspected same family, different format), Fitness Membership Management (processed — membership slice), Fitness Class Booking (processed — booking-loop slice; carried a joint-review recommendation for this leaf), Personal Training Management (unprocessed), Dance Studio Management (processed — family/children vertical), Climbing Gym Management (processed — climbing vertical), Sports Club Management / Recreation Center Management (unprocessed).
- Known tensions going in:
  1. The fitness-class-booking pass ratified keep-both with a center-of-gravity seam and recommended joint review when this leaf is processed → this pass must discharge it.
  2. The fitness-membership-management pass recorded that this leaf's core "must be differentiated from this membership slice (whole-business center vs membership center — strip scheduling/staff/POS and this Type stands, strip the membership engine and the suite doesn't run)" → this pass must ratify or correct.
  3. The dance-studio-management pass recorded the adult-member vs guardian-child discriminator for the seam with this leaf → confirm from the fitness side.
  4. Gym Management System is unprocessed; the market appears to sell one product family across gym/studio formats → potential alias/variant problem to record, not resolve unilaterally.

## Research Questions

1. What objects does a studio-management system hold, and which are definitional?
2. How does the operating loop flow (acquire customer → sell entitlement → book class → check in → attend → bill → retain)?
3. How do entitlements couple to booking (credits, pack deduction, membership usage limits, entitlement resolution when several are valid)?
4. How does money gate behavior (failed payments, overdue invoices, offline-payment blocking)?
5. What staff/instructor machinery exists (roles, permissions, pay, scheduling)?
6. What member-facing surfaces exist (booking site, member app, branded app)?
7. What multi-location/franchise machinery exists?
8. Where are the boundaries: vs the booking slice, vs the membership slice, vs gym management, vs dance studios, vs PT management?
9. Historical check: would a paper-era studio (card file + printed schedule + sign-up sheet + cash) satisfy the definition?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

1. **TeamUp** — lean international studio/box/gym software (DaySmart); booking-centric philosophy, strong self-serve setup, direct-debit + card rails, independent-studio tier. Tier-1 help centre (412 business articles) + feature pages.
2. **Mariana Tek** (Xplor) — boutique franchise pole (spin/pilates/barre/HIIT); credit-economy philosophy, spot/floor-plan depth, franchise royalty portal. Tier-1 knowledge base (Intercom) + product pages.
3. **Glofox** (ABC Fitness) — mid-market SaaS for studios and gyms; app-first philosophy, CRM/retention automation, access control, multi-location with royalty structures. Tier-1 Zendesk help center + product pages.
4. **Zen Planner** (Daxko) — multi-vertical fitness business platform (martial arts, functional fitness, boutique, gymnastics/dance, PT); membership-billing-heavy philosophy, staff payroll, retail. Tier-2 product pages (help center is a Salesforce community portal, not fetchable).

**Mindbody** — the market-centering suite — was NOT directly documented: help.mindbody.io (transport error), support.mindbodyonline.com (Salesforce CSS error), mindbodyonline.com/explore (JS-only app). This matches the sourcing limitation recorded by the fitness-class-booking pass. Mindbody's market position is evidenced indirectly (migration articles and comparison pages at Glofox, Mariana Tek, TeamUp, Zen Planner all name it as the incumbent).

## Sources

- TeamUp: https://www.goteamup.com/features , https://www.goteamup.com/features/memberships , https://support.goteamup.com/en/ , https://support.goteamup.com/en/collections/9210299-for-business-owners-admins-instructors (fetched 2026-09-08)
- Mariana Tek: https://www.marianatek.com/ , https://support.marianatek.com/en/ , https://support.marianatek.com/en/collections/407328-class-management (fetched 2026-09-08)
- Glofox: https://www.glofox.com/ , https://support.glofox.com/hc/en-us , https://support.glofox.com/hc/en-us/categories/46200748724884 (fetched 2026-09-08)
- Zen Planner: https://zenplanner.com/ (fetched 2026-09-08; help center at help.daxko.com not fetchable — Salesforce portal)
- Mindbody: not reachable this pass (see Sourcing Limitations)

## Product Observations

### TeamUp (evidence layer A — Tier-1 help centre + Tier-2 feature pages)

**Positioning:** "Professional management software for fitness studios, boxes and gyms"; business types: group fitness, yoga, CrossFit, pilates, gyms, bootcamps, martial arts, personal training, pole & aerial, enterprise & franchise.

**Objects and structure (from help-centre collections):**
- **Customers** — profiles with contact details, waivers, membership, registration history, injury notes; lifecycle statuses (New / Active / Inactive / "Slipping Away") with operator-configurable criteria; merge accounts; family members on a profile; block from booking; flag issues; CRM lifecycle pipeline (Kanban stages, automations, staff assignment, activity log).
- **Memberships** — recurring plans, prepaid plans, class packs; usage limits per day/week/month/year/billing cycle; holds with payment rescheduling; joining fees; contracts with minimum cancellation notice; upgrades/downgrades; member rates; free/paid trials; new-customers-only; single-purchase; multiple payment plans per membership; manual credit adjustments per customer.
- **Events** — Classes, Courses, Appointments, Rentals (book spaces without instructor/timetable), one-off events (workshops, parties); class types with registration settings.
- **Calendar** — business calendar; bulk cancel; business closures; filtered customer-facing calendar links; calendar sync.
- **Registration settings** — registration timelines (open/close, cancellation cutoff per class type); waitlists (auto-registration, reserved time, max size, disable-able); priority booking per customer groups; age restrictions; nightly blackout for waitlist spot expiry.
- **Forms & documents** — Forms, Waivers, Policies with timing (before/after registration or purchase), expiry/re-submission, e-signatures, missing-forms notifications.
- **Payments** — Stripe (cards, Apple/Google Pay, Stripe Terminal in-person), GoCardless direct debit; payment statuses; failed-payment behavior differs recurring vs non-recurring; offline-payment overdue threshold blocks membership usage; account credit; partial refunds; taxes/fees.
- **POS** — sell store items, gift cards, memberships, appointments from the dashboard.
- **Attendance** — check-ins; no-show tracking and actioning; "record a class usage against a customer's class pack — deduct a credit"; attendance reports identify at-risk customers.
- **Penalties** — infractions counting toward penalties with notifications and resets.
- **Staff** — unlimited staff accounts; permissions (e.g., forms management); instructors can set up and manage their own classes; instructor hours and pay-rate reports; pre/post-class notifications to staff.
- **Communication** — email/SMS notifications (registration confirmations, late cancellation, pack-running-low, birthday, pre/post/milestone class, membership purchase, hold ended); broadcast SMS; customizable branding.
- **Reporting** — attendances, revenue per class type/instructor, memberships (status, purchases, cancellations), holds, lifetime value, store orders, waivers, referrals, field changes.
- **Member surfaces** — customer site + member apps (book, manage registrations, payment details); custom branded app tier; on-demand; online classes (Zoom from the register).
- **Growth** — referrals; marketing suite; AI business advisor; reputation management; access control; free data import.

**Key semantics observed:** entitlement resolution at booking ("I have multiple memberships valid to use for the same event"); money gates entitlement (offline-payment blocking); booking on behalf of tech-averse clients; "change the word membership" customization.

### Mariana Tek (evidence layer A — Tier-1 knowledge base + Tier-2 product pages)

**Positioning:** "Boutique fitness business management software"; studio types: pilates/lagree, yoga, indoor cycling, HIIT/bootcamp, barre, group fitness; customers include franchise brands (multi-location); "70% of our clients migrated from another platform."

**Objects and structure (knowledge-base collections):**
- **Customers** — profile with history and payment options; tags/notes so staff can welcome newcomers, know injuries, celebrate milestones.
- **Credits & Credit Packages** — "One credit is one visit to your studio"; credit packages as a purchasable entitlement form.
- **Memberships** — creation, selling tools (36 articles).
- **Buy Pages** — the customer-facing page displaying credits and memberships.
- **Reservations** — making/managing/viewing customer reservations (26 articles); **Waitlist** (standby, moved to class); **Spots** — swap spots, mark unavailable, hold/release all spots, pick-a-spot with custom floor plans (bikes, reformers/megaformers).
- **Class Management** — roster navigation, find a class, print sign-in sheets, roster map view, roster notes, shoe-size display; **check-ins, late cancels, no-shows** (no-show window; late-cancel/no-show without penalty fee; accidental check-in correction); **Attendance Log** records the "Payment Used" per attendance.
- **Schedule Management** — "everything needed to set the schedule each week" (34 articles).
- **Appointments** — 18 articles (PT/appointment revenue alongside classes).
- **Add-Ons** — items purchased during the reservation process (e.g., shoe rental, mat rental).
- **Money** — POS (34 articles), Quick Sale, Products & Inventory, Discounts, Intro Offers, Gift Cards, Refunds, Stripe, **Purchase Agreements** (signed agreements associated with a credit or membership covering cancellation/refund policy), **Penalty Fees** (8 articles).
- **Employees** — employee management and roles (22 articles).
- **Franchise Fee Portal** — "easily calculate and collect royalties from your franchisees" (24 articles).
- **Third-Party Reservations** — ClassPass / GymPass reservations flowing into the roster (19 articles).
- **Mobile Apps** — 67 articles; branded customer app.
- **Reporting** — 122 articles.
- **Xplor Growth** — separate marketing/gamification suite (challenges, goals).

**Key semantics observed:** the credit economy (one credit = one visit) with per-attendance payment attribution; spot-level operations on a floor plan; penalty fees for late cancel/no-show; franchise royalty collection; third-party reservation networks as a first-class reservation source.

### Glofox (evidence layer A — Tier-1 Zendesk help center + Tier-2 product pages)

**Positioning:** "Fitness studio and gym management software"; "built for class-led fitness businesses of all kinds, from independent studios to growing gym brands"; business types: gym, fitness studio, PT, boxing, yoga, pilates, spin, martial arts, wellness; part of ABC Fitness.

**Objects and structure:**
- **Membership Management** — "single source of truth for their transactions, preferences, goals, and touchpoints"; member self-pause; cancellation reasons when scheduling cancellation; paused-membership search; activity history per client.
- **Scheduling & Booking** — flexible class and appointment booking, waitlists, automated reminders.
- **Branded Member App** — members book, buy, manage accounts.
- **Billing & Payments** — built-in payments, flexible billing, POS tools, cardless in-app purchases, automated failed-payment handling, balances, receipts; payment links to collect failed subscription payments; chargebacks/disputes; sales tax (tax-inclusive and tax-exclusive modes).
- **CRM** — automated messaging across email/SMS/push; journeys; segmentation; lead management (lead statuses, traffic-light targeting, leads report, registration-point attribution).
- **Check-in & Access Control** — fast trackable check-in, kiosks, barcodes/scanners, door-entry integrations (e.g., smart-lock vendors), manual check-in, **overdue-invoice access blocking**.
- **Staff Management** — scheduling tools, performance visibility, dedicated staff app ("Glofox Pro": manage clients, memberships, reports, email class participants from the staff phone app); staff roles and default permissions.
- **Multi-Location** — "from single locations to global operations... flexible models including royalty structures."
- **XLerate automation** — workflow templates: membership renewal reminders, cart abandonment, member expired/cancelled, visits milestones.
- **Reports** — scheduled revenue, membership plan changes, no-shows, lost members, trainer insights, new memberships.
- **Store** — retail products; **Community** — member posts; **Live & on-demand** — streaming classes.
- **Integrations** — aggregator networks (Wellhub/GymPass), lead-marketing vendors, retention vendors.

**Key semantics observed:** money gates access (overdue invoice → access blocking); membership standing machinery (pause, cancellation reasons, plan changes); leads pipeline as a first-class object; staff app as a separate surface; royalty structures at multi-location.

### Zen Planner (evidence layer A for positioning/features — Tier-2 product pages; help center not fetchable)

**Positioning:** "Fitness business management & billing software"; "trusted by over 6,000 fitness businesses"; serves martial arts schools, BJJ/MMA gyms, functional fitness, HIIT, sports performance, personal training, boutique (yoga/pilates/barre/cycling/rowing/climbing/group fitness), gymnastics & dance.

**Structure (product pages):**
- Member management (member info, insights, analytics); schedule management; **membership and class package builder**; billing and payment processing; financial reporting and dashboards; **revenue protection / revenue recovery**; retail tools; **staff management and payroll**; skill and belt tracking (martial arts); automated marketing & sales (websites, digital marketing, CRM, lead tracking, funnels, AI assistant that answers calls/messages and books leads); community engagement; member & staff app; fitness tracking (SugarWOD integration); business insurance.

**Key semantics observed:** membership-billing center of gravity with class packages as the second entitlement form; payroll as part of staff management; vertical seasoning (belt tracking) as a feature of the same product; the competitive set named in its comparison pages (Mindbody, PushPress, Wodify, WellnessLiving, Glofox, Virtuagym, Xplor Recreation) confirms one market family.

### Mindbody (evidence layer B/C — indirect only)

Not directly documented (see Sourcing Limitations). Indirect evidence: every sampled competitor names Mindbody as the incumbent to migrate from or compare against (Glofox migration article "Migrating from Mindbody and Other Software to Glofox"; Mariana Tek comparison page and demo form listing current software; TeamUp and Zen Planner comparison pages). Mariana Tek's demo form also names the broader competitive set: Momence, ClubReady, Mindbody, Glofox, Acuity, WellnessLiving, Arketa, Wix, bsport, Hapana, Vagaro, Walla. No Mindbody capability is asserted in this pass.

## Cross-product Comparison

| Structure | TeamUp | Mariana Tek | Glofox | Zen Planner | Evidence |
|---|---|---|---|---|---|
| Customer/member of record (profile, history, payment methods, waivers/notes) | ✓ | ✓ | ✓ | ✓ | A×4 → B |
| Entitlement plans: recurring memberships | ✓ | ✓ | ✓ | ✓ | A×4 → B |
| Entitlement plans: class packs / credits | ✓ ("class packs") | ✓ ("one credit is one visit") | ✓ ("credit packs") | ✓ ("class package builder") | A×4 → B |
| Drop-in / single purchase / trials / intro offers | ✓ | ✓ (intro offers) | ✓ | ✓ | A×4 → B |
| Automated recurring billing + failed-payment handling | ✓ | ✓ (Stripe) | ✓ | ✓ (revenue recovery) | A×4 → B |
| Membership standing machinery (hold/pause, cancel, expire) | ✓ (holds + payment rescheduling) | ✓ | ✓ (self-pause, cancellation reasons) | ✓ | A×4 → B |
| Recurring class schedule (class types, instructors, capacity) | ✓ | ✓ (weekly schedule management) | ✓ | ✓ | A×4 → B |
| Customer self-service booking (site/app) | ✓ | ✓ (branded app, buy pages) | ✓ (branded app) | ✓ (member app) | A×4 → B |
| Booking consumes entitlement (credit deduction / usage limit) | ✓ (explicit "deduct a credit") | ✓ (attendance log "payment used") | ✓ | ✓ | A×4 → B |
| Check-in / attendance recording | ✓ | ✓ (roster, sign-in sheets) | ✓ (kiosks, barcodes) | ✓ | A×4 → B |
| Late-cancel / no-show consequences | ✓ (cancellation cutoffs, no-show tracking, penalties) | ✓ (penalty fees, no-show window) | ✓ (no-shows report) | ✓ | A×4 → B |
| Waitlists | ✓ | ✓ | ✓ | ✓ | A×4 → B |
| POS / retail / gift cards | ✓ | ✓ (POS, quick sale, inventory) | ✓ (store) | ✓ (retail) | A×4 → B |
| Staff roles & permissions | ✓ | ✓ (employee roles) | ✓ (roles + default permissions) | ✓ | A×4 → B |
| Instructor operations (scheduling, hours/pay) | ✓ (hours & pay-rate reports) | ✓ (employees + schedule) | ✓ (trainer insights, staff app) | ✓ (staff payroll) | A×4 → B |
| Reporting (attendance, revenue, retention) | ✓ | ✓ (122 articles) | ✓ | ✓ (dashboards) | A×4 → B |
| Member app / branded app | ✓ | ✓ | ✓ | ✓ | A×4 → B |
| CRM / leads / marketing automation | ✓ (lifecycle pipeline, marketing suite) | ✓ (Xplor Growth add-on) | ✓ (CRM, XLerate) | ✓ (Engage) | A×4 → B |
| Appointments (1:1 services) alongside classes | ✓ | ✓ | ✓ | ✓ | A×4 → B |
| Courses / multi-session programs | ✓ (courses) | — (not observed) | — (not observed) | — (not observed) | A×1 (product-specific) |
| Rentals (spaces without instructor) | ✓ | — | — | — | A×1 (product-specific) |
| Spot/floor-plan operations (pick-a-spot, swap, hold) | — (not observed) | ✓ | — | — | A×1 (product-specific) |
| Franchise royalty portal | — | ✓ (franchise fee portal) | ✓ (royalty structures) | — | A×2 → B (franchise-tier variant) |
| Third-party reservation networks (ClassPass/Wellhub) | — (not observed) | ✓ | ✓ (Wellhub) | — | A×2 → B (variant) |
| Access control / door hardware | ✓ | — (not observed) | ✓ | — | A×2 → B (variant) |
| On-demand / live-stream classes | ✓ | — (not observed) | ✓ | — | A×2 → B (variant) |
| Penalties/infractions system | ✓ | ✓ (penalty fees) | — | — | A×2 → B (variant) |
| Vertical seasoning (belt tracking, workout tracking) | — | — | — | ✓ (SugarWOD, belts) | A×1 (variant) |
| Family/child accounts | ✓ (family settings) | — | — | — | A×1 (variant) |
| Payroll | — (hours/pay reports only) | — | — | ✓ (payroll) | A×1 (variant) |

## Canonical Model

### L0 — Defining Invariant

The operator-side system of record for a class-led fitness business, holding **jointly**:

1. **The customer of record** — a persistent identified person carrying contact details, entitlements, payment methods, waivers/notes, and attendance history. Remove → anonymous booking form or a bare class list.
2. **The entitlement economy** — operator-defined purchasable plans (recurring memberships, prepaid terms, class packs/credits, drop-ins, trials) instantiated per customer, funded by billing (automated recurring charges and/or point-of-sale settlement) and governed by standing (active / hold / cancelled / expired). Remove → a class-booking tool with no business relationship, or a price list with no customers.
3. **The scheduled class offerings** — a recurring calendar of group classes, each carrying class type, time, instructor, place, and bounded spots (plus one-off occasions riding the same machinery). Remove → membership billing with nothing to attend.
4. **The booking-and-attendance loop that consumes entitlements** — customers (self-service or staff on their behalf) reserve spots; each booking resolves against the customer's entitlements (credit deduction / membership usage); attendance is checked in and recorded; late cancellation and no-show carry consequences. Remove the consumption coupling → a disconnected membership system plus a disconnected schedule tool.

The joint hold is load-bearing: (1)+(2) without (3)+(4) = Fitness Membership Management; (3)+(4) without (1)+(2) = Fitness Class Booking; (2) without (1) = subscription billing; (4) without the entitlement resolution = a sign-up sheet.

### L1 — Common Mature Structure

Present in essentially all mature products; expected by the market but not definitional:

- member self-service surfaces: booking site, member app, branded app
- waitlists with placement/expiry mechanics
- cancellation cutoffs, late-cancel/no-show consequences (penalty fees or credit forfeiture)
- digital waivers/forms with timing and expiry
- check-in machinery (roster, register, kiosk, barcode) and attendance reporting
- CRM/lead pipeline, marketing automation, retention campaigns, referrals
- reporting: attendance, revenue per class/instructor, membership status, retention/churn
- staff management: roles, permissions, instructor scheduling, hours/pay tracking
- POS/retail: products, inventory, gift cards, discounts, intro offers
- appointments (1:1 services) alongside group classes
- multi-location support
- communication: transactional email/SMS notifications, broadcast messaging

### L2 — Variant / Optional Structure

Depends on segment, format, geography, business model:

- **Entitlement-mix emphasis**: credit-economy (boutique: credits per visit, packs) vs membership-economy (gym/box: EFT dues with usage allowances) — both forms present in all sampled products, emphasis varies
- **Franchise/multi-location tier**: royalty collection portals, brand-level reporting (franchise pole)
- **Third-party reservation networks** (ClassPass, Wellhub/GymPass) as reservation sources
- **Access control depth**: door hardware, kiosks, 24/7 unstaffed access (gym-format pole)
- **Spot-level operations**: floor plans, pick-a-spot, spot swaps/holds (format-dependent: bikes/reformers)
- **On-demand / live-streaming classes**
- **Penalty/infraction systems** as a governed consequence engine
- **Family/child accounts** (adult-member core with optional dependents)
- **Regional payment rails**: direct debit vs cards; tax-inclusive vs tax-exclusive pricing
- **Vertical seasoning**: belt/skill tracking (martial arts), workout tracking (functional fitness), rentals (multi-purpose venues)
- **Adjacent business services**: business insurance, capital/financing, website building, AI assistants

### L3 — Vendor-specific Structure (research notes only)

- TeamUp: penalty system with infractions and resets; "change the word membership" labeling customization; AI Business Advisor; rentals as a distinct event type; courses as a distinct event type; nightly blackout period; Learn-to-Skate integration
- Mariana Tek: floor-plan map view with printable rosters; shoe-size display in rosters; Quick Sale; Xplor Capital/Insurance; Xplor Growth gamification suite; purchase agreements bound to credits/memberships
- Glofox: traffic-light lead targeting; XLerate workflow templates; Glofox Pro staff app; ABC Insights; overdue-invoice access blocking as a named feature
- Zen Planner: SugarWOD workout-tracking bundle; belt tracking; AI receptionist positioning; business insurance marketplace

## Vendor-specific Findings

See L3. None of these entered the canonical model. The closest call was spot/floor-plan operations (Mariana Tek only in this sample) — kept as L2 variant because it is format-dependent (bike/reformer studios) rather than definitional; the bounded-spots property of a class offering IS definitional (L0 leg 3), but spot-swap/hold machinery is not.

## Boundary Findings

1. **vs Fitness Class Booking** (processed 2026-09-07; joint review DISCHARGED from this side): the booking loop is one workflow inside the studio system. Center-of-gravity seam, removal tests both directions: strip everything but the booking loop from a studio suite and the remainder is still a working class-booking product (the pure-play pole exists and is marketed as such); strip the booking loop from a studio suite and it still manages members, entitlements, billing, staff, and POS. Keep-both ratified. The studio Type is defined by the whole coupled loop (customer + entitlements + schedule + consumption + money), not by the booking loop alone. The booking pass's characterization of suites ("inside suites booking *is* a workflow") is confirmed by all four sampled products.

2. **vs Fitness Membership Management** (processed 2026-09-08; ratified from this side): the membership slice = member of record + held membership + dues-and-standing cycle. This Type holds the whole business: the membership engine is one pillar; the class schedule/booking loop, staff operations, and POS are the others. The membership pass's removal test is confirmed: strip scheduling/staff/POS and the membership Type stands; strip the membership engine and the studio suite doesn't run. The two Types share the entitlement-economy skeleton; the studio Type is the superset with the class-led operating loop as the added defining structure.

3. **vs Gym Management System** (unprocessed sibling; TAXONOMY FLAG): market evidence shows one product family sold across gym and studio formats — TeamUp sells "gym management software" and "yoga studio software" as the same product on different pages; Glofox serves Gym + Fitness Studio + Boxing + Martial Arts + Wellness from one platform; Zen Planner serves functional-fitness gyms and boutique studios from one platform; Mariana Tek's demo form lists gym-format competitors alongside studio ones. The gym/studio distinction in the market is format and scale (access-centric big-box with amenities vs class-led boutique with a credit/pack economy), not structure. This pass documents the class-led realization; whether the directory wants two leaves (gym vs studio) or one Type with format variants is a joint-review question for the gym-management-system pass. Recorded in STATUS Boundary Issues.

4. **vs Dance Studio Management** (processed 2026-09-07; confirmed from this side): the dance pass's discriminator holds — fitness products center the adult individual member with memberships/packs/drop-ins; dance products center guardian-child family accounts with season-enrollment tuition and performance machinery. In this pass's sample, family/child capability exists only as an optional add-on (TeamUp family settings); the adult member is the core customer record across all four products.

5. **vs Personal Training Management** (unprocessed): PT business software centers the trainer-client appointment relationship and coaching delivery; studio software centers group classes with appointments as an adjacent service (all four sampled products carry appointments as a secondary booking type). Flag for that pass: the seam is likely center-of-gravity (appointment-led vs class-led), with studio suites absorbing small PT operations.

6. **vs Climbing Gym Management** (processed 2026-09-07): that leaf = climbing-facility business system whose independent identity rests on the safety posture and the wall/routesetting layer atop the shared fitness-business core. Consistent: the shared core observed there (members, entitlements, check-in, billing, POS, booking) is the same core documented here; climbing adds its vertical layer.

7. **vs Sports Club Management / Recreation Center Management** (unprocessed): those center multi-sport/multi-program operations for clubs and municipalities (memberships across facilities, program registration, facility schedules); the studio Type centers one commercial class-led fitness business. Not deeply researched here; noted for those passes.

8. **"去掉什么就变成另一个 Type" 判据**: remove the entitlement economy → class booking tool; remove the class schedule/booking loop → membership management; remove the customer record → anonymous booking; remove the consumption coupling → disconnected tools; add guardian-child family accounts + season tuition + performance machinery → dance-studio territory; add the wall/routesetting layer + safety certifications → climbing-gym territory; make the appointment the center → personal-training management; make multi-sport program registration the center → sports club / recreation center territory.

## Historical / Market-Sample Check

Paper-era studio: a card file of members with punch cards (customer of record + entitlement instances), a printed weekly class schedule with instructor names (scheduled offerings), a sign-up sheet at the desk (booking against bounded spots), cash/cheque collection and card punching (money + consumption), an instructor roster with pay notes (staff). This satisfies the defining core with no apps, portals, hardware, or automation — the historical check passes; none of the modern machinery (branded apps, waitlist automation, penalty engines, access control, CRM) is in L0. Early software-era studio systems (desktop scheduling + billing databases) likewise satisfy the core.

## Uncertainties

1. **Mindbody unverified at documentation level** — the market-centering suite pole is evidenced only indirectly (migration/comparison pages). No Mindbody-specific capability is asserted. This limitation is shared with the fitness-class-booking pass.
2. **Zen Planner evidence is Tier-2 only** (product pages; help center is a Salesforce portal that did not render). Its feature claims are vendor marketing pages; workflow-level detail was not verified. Assertions about Zen Planner are kept at feature-list strength.
3. **Exact mechanics vary and were not exhaustively researched**: waitlist placement rules, penalty-fee amounts, credit-expiry policies, dunning sequences — all documented here only at the level of "exists and is configurable"; precise defaults/limits are vendor-specific and were not asserted.
4. **Gym Management System boundary** — resolved provisionally (same family, format variants) but the sibling leaf is unprocessed; final keep/split decision belongs to that pass's joint review.
5. **Salon/wellness multi-vertical products** (e.g., the booking-software-for-everyone pole named in Mariana Tek's competitor list) were not sampled; the studio Type's edge against them is asserted from the fitness-first positioning of the sampled products only.

## Final Synthesis

Fitness Studio Management is the operator-side whole-business system of record for a class-led fitness business. Its defining core is the coupled operating loop: identified customers carrying entitlements (recurring memberships, class packs/credits, drop-ins, trials) funded by billing and governed by standing; a recurring schedule of group class offerings with instructors, places, and bounded spots; and a booking-and-attendance loop in which each reservation consumes an entitlement and each attendance is recorded, with consequences for late cancellation and no-show. Around that core, mature products add the standard machinery of the market: member self-service apps, waitlists, waivers, check-in and access control, CRM and retention automation, reporting, staff management with instructor pay, POS/retail, and multi-location support. The Type contains the two processed slices as pillars — the membership engine (Fitness Membership Management) and the booking loop (Fitness Class Booking) — and is defined by their coupling with the class schedule and the money loop, not by any one of them alone. The market sells this family across gym and studio formats; the class-led boutique realization is documented here, with the gym-format seam flagged for joint review with the unprocessed Gym Management System leaf.
