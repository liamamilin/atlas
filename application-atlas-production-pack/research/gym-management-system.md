# Research Notes — Gym Management System

## Research Goal

Understand what a Gym Management System actually is as an Application Type: its defining core, its standard whole-business structure, how the daily access-led operation works, and how it is bounded against the processed §28 siblings (Fitness Membership Management, Fitness Studio Management, Fitness Class Booking, Climbing Gym Management) and adjacent Types.

## Initial Boundary

Hypothesis before research: an operator-side business system for a facility-membership fitness business (gym/health club/big-box), where the member's standing relationship is a dues-bearing membership consumed primarily by **facility entry** (staffed check-in through 24/7 door control), with classes, bookings, POS, staff and lead-funnel machinery integrated in the same console. Distinguished from the class-led studio format (booking-and-attendance is the consumption loop) and from the pure membership-engine slice (no door, no whole-business span).

Nearest types: Fitness Membership Management (slice), Fitness Studio Management (sibling format), Fitness Class Booking (slice), Climbing Gym Management (vertical sibling), Recreation Center Management (institutional counterpart), Membership Management System §25 (generic counterpart), CRM (funnel only), Appointment Scheduling (machinery only).

## Research Questions

1. What is the member of record in gym-format products, and what does it carry?
2. What is the membership structure (plans, access/usage restrictions, standing states)?
3. How does entry verification / check-in / access control actually work, and how tightly is it coupled to membership standing and billing?
4. How does the dues cycle run in gym-format products (billing providers, failed payments, arrears → access consequences)?
5. What role do classes, bookings, appointments play in the gym format (versus the studio format)?
6. What whole-business machinery surrounds the core (leads/sales funnel, POS/retail, staff, reporting, marketing automation, multi-location)?
7. How do cross-format vendors position the same product for gym vs studio (the fitness-studio-management pass's taxonomy flag)?
8. What does the enterprise-chain pole add (centralized membership, roaming access, debt collection)?
9. Historical check: does the definition hold for a pre-software gym (card file, front-desk card check, monthly dues ledger)?

## Representative Products

Selected for market representation, documentation quality, and different product philosophies / customer tiers:

| Product | Pole | Tier | Evidence level reached |
|---|---|---|---|
| GymMaster | access-led flagship (native 24/7 access control + billing partners) | SMB/24-7 gyms | official product pages (access control, membership management) — deep |
| TeamUp | cross-format SaaS (same product sold as gym and studio software; booking-led heritage) | SMB boutique→gym | help centre at article level (collections + check-in article) — deepest |
| PerfectGym | enterprise chain platform (multi-club, debt collection, access control at scale) | mid-market/enterprise chains | official product pages (root, club management) |
| Zen Planner | multi-vertical SMB suite (functional fitness/martial arts/boutique; Daxko) | SMB | official homepage/product nav |
| Mindbody | market-centering suite across fitness/wellness/beauty | SMB→enterprise | official homepage + feature FAQ (reachable this pass; previous sibling passes could not reach it) |

Rationale: covers the access-led pole (GymMaster, PerfectGym), the booking-led/cross-format pole (TeamUp), the multi-vertical suite pole (Zen Planner, Mindbody), and three customer tiers (SMB, mid, enterprise chain). Avoids same-vendor duplication.

## Sources

- GymMaster — https://www.gymmaster.com/gym-access-control/ (fetched 2026-09-08); https://www.gymmaster.com/membership-management/ (fetched 2026-09-08)
- TeamUp — Help Centre: https://support.goteamup.com/en/ (fetched 2026-09-08); collection "For Business Owners, Admins, Instructors" (https://support.goteamup.com/en/collections/9210299-for-business-owners-admins-instructors); "How to set up and manage customer check-ins" (https://support.goteamup.com/en/articles/9331074-how-to-set-up-and-manage-customer-check-ins)
- PerfectGym — https://www.perfectgym.com/ (fetched 2026-09-08); https://www.perfectgym.com/en/solutions/gym-management-software (fetched 2026-09-08)
- Zen Planner — https://zenplanner.com/ (fetched 2026-09-08)
- Mindbody — https://www.mindbodyonline.com/ (fetched 2026-09-08, incl. feature FAQ)
- Sibling passes consulted for joint review: research/climbing-gym-management.md, research/fitness-studio-management.md, research/fitness-membership-management.md (via applications/* and STATUS.md entries)

Sourcing limitation: article-level operational documentation was reachable only for TeamUp. GymMaster, PerfectGym, Zen Planner and Mindbody were observed at official product-page level (confirms structure presence and positioning, not precise operational rules). No article-level claims are made for those four; no numeric limits, default values or state ladders are asserted anywhere in the final document except as product-specific detail held in these notes. (Mindbody main site was reachable this pass — an improvement over the three sibling passes that recorded it as unreachable; help-center article depth was still not attempted beyond the homepage FAQ.)

## Product Observations

### GymMaster (evidence layer A — product pages, two pages fetched directly)

**Access control page** (https://www.gymmaster.com/gym-access-control/):
- Built-in 24/7 access control as a headline native feature; "runs itself" — automated access lets the facility run outside staffed hours; "generate membership revenue without a proportional increase in overhead".
- "Access permissions, visit logging, and membership checks all update automatically."
- Membership tiers by access window: "Offer standard, off-peak, and full 24/7 membership tiers"; "Specify time restrictions on membership"; "Assign different access hours to different membership plans".
- "Choose whether you offer 24 hour access to everyone, or just selected memberships."
- Fully integrated into the member database; automatic actions: "Expired memberships are instantly applied to member cards"; "Deny gym access to those who are too far behind on their payments"; "Concession visits are automatically counted against the membership"; "Members visiting for classes are automatically checked into the session upon entry"; "All visits are logged, giving you the opportunity to identify visitation patterns".
- Alerts surfaced at check-in on staff devices: new/returning member (for coaching attention), missed payment (staff prompted to remind), expiring memberships.
- Visitation pattern reports: staffing resource use, at-risk members (visit drop-off), growth patterns.
- Group-scoped doors: "Set up specific doors … accessible only by women, or any other groups"; "Configure entry based on time, membership type, or staff seniority".
- Tailgating detection: camera monitors movement and compares against the visitor log; second camera photographs suspected tailgaters for evidence-based member reporting; remote live view.
- Hardware: RFID + Bluetooth door readers, member-app phone unlock, GateKeeper controller linking readers to the membership database, works with turnstiles/electronic locks (12v/24v); remote unlock and check-in from the operator's mobile; database backed up to keep doors working offline ("backing up your database to work even when the internet goes down").

**Membership management page** (https://www.gymmaster.com/membership-management/):
- Online signups & waivers: sell memberships on the gym's website or on a tablet in-club.
- Sales funnel / leads management: leads fed from website and other sources; staff work steps (call, email, tour); "the funnel is updated for everyone to see".
- Customizable member profiles: member details, acquisition channel, "memberships and billing records, visitation, booking habits, communications, measurements, and even purchases".
- Self-service portal + mobile app: sign-ups, bookings, membership management.
- "Ultra configurable memberships": "Pick your desired combination of visit, booking type or access restrictions when building your memberships. Control who can visit and when, what classes and services they can use, or set limits for these."
- Trial, promo & concession passes as a distinct offer shape.
- Flexible billing: "up-front, weekly, monthly, annually or anything in-between"; choice of billing providers ("pick your own provider").
- Member communications: bulk or automated email/SMS/push to leads, members, "clients at-risk of cancelling or historic members".
- Reporting & KPIs: preset and custom reports.
- FAQ: "Memberships, billing and debt collection are all taken care of"; "the 24/7 access hardware means you can run your business without staff even having to be there".

### TeamUp (evidence layer A — help centre, article level)

**Check-in article** (https://support.goteamup.com/en/articles/9331074-how-to-set-up-and-manage-customer-check-ins):
- Check In tool purpose: "check in customers that arrive on site and track and log their attendance without a booking" — explicitly for "Open Gym or any other activity that allows customers with applicable memberships to enter and use your facility without booking a specific class or appointment". This is the gym-format consumption mode inside a booking-led product.
- Check-in is disabled by default and enabled business-wide or per venue.
- Eligibility is membership-bound: staff select the customer and "which one of the customer's memberships you want to use — only the customer's memberships that are eligible for check-in at the selected venue will be displayed … If one of the customer's memberships has reached its limit for check-ins, it will show up … but you won't be able to select it (greyed out)". Check In is configured in each membership's "Frequency Restrictions".
- Standing flags surfaced before completing check-in: "certain issues flagged on the customer's profile, whether they've got missing forms and waivers or even if their registrations have been blocked".
- Staff may "bypass the membership requirements and register the customer for free" — the gate is advisory in this product, not hard-enforced at a door.
- Product-specific detail (research notes only): check-ins limited to once per day per customer; attendance auto-marked and flows into the All Attendances report; status corrections via profile or activity feed.

**Collection page** (https://support.goteamup.com/en/collections/9210299-for-business-owners-admins-instructors):
- Event machinery: Classes (30 articles), Courses, Appointments, one-off events, Rentals ("let customers book spaces in your venue (courts, studios, saunas, rooms)").
- Registration machinery: registration timelines (open/close/cancellation cutoff), waitlists (auto-registration, reserved time), priority booking, age restrictions, nightly blackout.
- Memberships: holds & payment rescheduling (proration), cancelling on behalf with expiry-date options, joining fees, custom usage limits per customer ("manually add or remove credits"), multiple memberships valid for the same event.
- Payments: multiple processors per purchase type (Stripe, GoCardless), payment statuses, in-person/mobile (Stripe Terminal, POS, cash/offline), account credit against recurring payments, "block a membership from being used when it has pending offline payments" (overdue threshold → blocked membership), failed direct-debit resolution.
- Customer management: profiles, fields, forms/waivers/policies with expiry and required-before-purchase timing, missing-forms notifications, family settings, merge accounts, flags, no-show tracking, penalties & infractions counters.
- CRM: Lifecycle Pipeline (stages, Kanban, automations, staff assignment, interactions log).
- Reporting: attendance (All Attendances), memberships by status, holds, store orders, customer lifespan, lifetime value, "Slipping Away" at-risk criteria, Inactive customer criteria, waivers, referrals.
- POS: sell store items and gift cards, take payments, book from POS.
- Communication: automated email/SMS notifications (registration confirmations, late cancels, pack running low, birthdays), broadcast SMS.

### PerfectGym (evidence layer A on pages; capability-level only)

**Root + club management page**:
- Positioning: "Gym Management Software For Fitness Chains & Enterprises"; "Fitness Enterprise Management System"; "Simplify the management of your entire multi-club network. Centralize all your member, club, and employee data."
- FAQ defines scope: "comprehensive administration of multi-location gyms … manage club facilities, employee affairs, member and guest accounts, product and service sales, payments, marketing initiatives, reporting, and client communication."
- Page sections: Operations (multi-location, automated workflows, scheduling, invoicing); **Memberships** ("Centralized Membership Management — all your members' key data – payment history, attendance, contracts"); **Access Control** ("Control Every Entry, Ensure Security — Minimise on-site staffing needs while ensuring secure, automated entry through a variety of methods - RFID cards, QR codes and more"; customer quote: "Our members can easily access any of our Level Up Fitness locations, 24/7, even outside of regular staff hours. With a simple RFID card scan, PerfectGym instantly verifies their membership status, unlocking the doors"); Reports (churn at-risk, predictive sales insights, member behaviour); Employees (access control permissions, skill assignments, scheduling, daily tasks, dedicated employee app).
- Suite modules: Club Management; Sales & Marketing (targeted campaigns, comprehensive lead management); Financial Services (automated billing, **debt collection services**, financial forecasting); Member Engagement (self-service tools, personalized communication, loyalty program); Open Platform integrations (ClassPass, Wellhub, EGYM, Technogym, Stripe, GoCardless, HubSpot…).
- Add-ons: member portal and app, kiosks, CRM; Open API; multilingual / multi-currency for international chains.
- Clients shown: international chains (Crunch, Fit 4 Less, Revo Fitness, SportCity, Invictus, Level Up…). Positioning: "mid-sized and enterprise-level fitness businesses, wellness and sports facilities, regional and international fitness chains and franchises, as well as public and private leisure operators."

### Zen Planner (evidence layer A on homepage; capability-level only)

- Positioning: "Fitness Business Management & Billing Software"; "Gym Member Management Software"; serves martial arts, functional fitness, HIIT, sports performance, personal training, boutique (yoga/pilates/barre/cycling/rowing), gymnastics & dance, climbing — one platform, many vertical pages (cross-format evidence).
- Suite pillars: Member Management; Billing & Payments; Automated Marketing & Sales (CRM, lead tracking and funnel visibility, automated campaigns); Community Engagement; Member & Staff App; Fitness Tracking (SugarWOD); Retail tools; Staff management and payroll; Reporting & Dashboards; Revenue Recovery (failed payments); scheduling; websites.
- "Membership and class package builder" — membership and class-pack shapes in one catalog.
- Owner Daxko; help center hosted on Daxko community site; add-on services (digital marketing, business insurance, onboarding coaching).

### Mindbody (evidence layer A on homepage+FAQ; capability-level only)

- Positioning: "Business management software" for fitness (gym, fitness club/athletic club, studios), wellness, beauty; enterprise multi-location tier. Multi-vertical breadth confirmed by business-type nav (gym software, athletic club software, studio verticals…).
- Feature set (nav + homepage): Payments; Marketing tools; Staff management (scheduling, substitutions, payroll); Scheduling (one calendar for classes and appointments, real-time updates on every touchpoint); Booking (consumer app, branded web tools, branded app); Business reporting; Multi-location management.
- FAQ evidence:
  - "Mindbody can serve as a comprehensive platform that combines CRM, scheduling, and POS functionality in one system."
  - Door access: integrations include "Door access systems that manage entry to your studio or gym, including turnstiles, doors, and lock hardware" — access control realized via integration rather than native hardware.
  - Lead Management: "Sales pipeline dashboard … automated lead capture … follow-up tasks … sales funnel analytics."
  - Payments/collections: failed/expiring payment auto-emails, Autopay Detail and Credit Card Expirations reports, "declined autopays can be converted into account balances that you can monitor and collect", chargeback tracking.
  - Waivers/forms: forms required per service with digital signature; waivers as digital acknowledgment with timestamp at booking/account creation/front desk.
  - Multi-location: datashare setup (shared services/pricing/clients/staff across nearby locations) vs Enterprise (corporate dashboard, cross-location reports, network-wide staff permissions, IP restrictions, staff login locations).
- Marketplace side: consumer Mindbody app (discovery/booking channel), ClassPass for business, Mindbody Capital financing — demand-channel and financing extensions, not business-core.

## Cross-product Comparison

| Structure | GymMaster | TeamUp | PerfectGym | Zen Planner | Mindbody |
|---|---|---|---|---|---|
| Member of record (profile: memberships, billing, visitation, agreements, history) | ✓ (customizable profiles incl. visitation, measurements, purchases) | ✓ (profiles, fields, forms/waivers) | ✓ (centralized member data: payment history, attendance, contracts) | ✓ (member management) | ✓ (client management) |
| Membership plan → held membership (with usage/access rights) | ✓✓ (visit + booking-type + access restrictions in one plan builder; passes) | ✓✓ (frequency restrictions incl. check-in eligibility/limits) | ✓ (contracts) | ✓ (membership and class package builder) | ✓ (contracts) |
| Dues billing + failed-payment recovery | ✓ (billing providers; debt collection) | ✓ (processors per purchase type; offline-overdue → membership block) | ✓ (automated billing; debt collection services) | ✓ (billing & payments; revenue recovery) | ✓ (autopay; declined → account balance collection) |
| Entry verification against standing | ✓✓ native (expired → card instantly; arrears → deny; RFID/BT/mobile; 24/7) | ✓ tool (Open Gym check-in, membership-eligible, venue-scoped; advisory flags) | ✓✓ (RFID/QR; "instantly verifies membership status, unlocking the doors", 24/7 roaming) | (not evidenced at page level this pass) | ✓ via door-access integrations (turnstiles/doors/locks) |
| Access tiers by time window / scope | ✓✓ (standard/off-peak/24-7; time restrictions; group-scoped doors) | (venue scoping only) | ✓ (24/7, multi-location roaming) | — | — |
| Class/booking machinery | ✓ (online booking, scheduling) | ✓✓ (classes/courses/appointments/rentals, waitlists, timelines) | ✓ (class & staff scheduling) | ✓ (schedule management) | ✓ (classes + appointments, one calendar) |
| POS/retail | ✓ (POS & stock control) | ✓ (POS, store, gift cards) | ✓ (product & service sales) | ✓ (retail tools) | ✓ (complete POS) |
| Staff management | partial evidence (staff seniority in access rules) | ✓ (permissions, instructor hours/pay) | ✓✓ (employee mgmt: scheduling, skills, tasks, app) | ✓ (staff mgmt + payroll) | ✓✓ (substitutions, payroll, network permissions) |
| Leads / sales funnel | ✓✓ (sales funnel dashboard) | ✓ (CRM lifecycle pipeline) | ✓ (lead management, sales & marketing) | ✓ (CRM, funnel visibility) | ✓✓ (sales pipeline dashboard, funnel analytics) |
| Member self-service (portal/app) | ✓ (portal + member app) | ✓ (customer site + members app) | ✓ (portal/app add-on, kiosks) | ✓ (member & staff app) | ✓ (branded app, booking surfaces) |
| Multi-location | (not directly evidenced this pass) | ✓ (venues; per-venue config) | ✓✓ (centralized multi-club, roaming 24/7, multi-currency) | ✓ (multiple locations) | ✓✓ (datashare + enterprise corporate dashboard) |
| Waivers / digital forms | ✓ (online waivers) | ✓✓ (forms/waivers with expiry, required before purchase/registration) | — | — | ✓ (forms + waivers, timestamped) |
| Marketing / retention automation | ✓ (at-risk comms, automation) | ✓ (Slipping Away/Inactive criteria) | ✓ (targeted campaigns, retention) | ✓ (Engage, pre-built campaigns) | ✓ (automated campaigns) |
| Vertical seasoning | — | — | — | ✓ (SugarWOD, skill/belt tracking) | — |

## Canonical Model

### L0 — Defining Invariant (four jointly-held structures)

1. **The member of record.** A persistent, individually identified person holding the commercial relationship with the gym: identity and contact data, signed agreements/waivers, payment methods, current and past memberships, dues history, and recorded visits. Remove → anonymous pass sales / CRM contacts.
2. **The standing facility membership.** An operator-defined plan catalog (dues, billing cadence, access and usage rights — entry windows, booking rights, visit limits) instantiated per member as a renewable entitlement carrying a governed standing state (active / frozen / ended). This is what makes a person "a member of this gym" on any given day. Remove → price list / day-pass counter.
3. **Entry verification against standing.** The daily consumption loop: the member identifies themselves at the facility (staffed desk, kiosk, tag/card/QR/phone) and the system resolves their standing before entry is granted — membership active, entitlement valid for what they are using, account not blocked for arrears, required forms present — then records the visit. Entry is also the data source for visitation analytics and at-risk detection. Remove → membership register + billing with no gym operation (the Fitness Membership Management slice).
4. **The dues-and-money cycle.** Recurring dues charged automatically against stored payment methods on the billing schedule; failed-payment recovery; arrears able to suspend the entitlement or block access. Remove → attendance tracking / door hardware with no business record.

Jointly-held is load-bearing:
- 1+2+4 without 3 = Fitness Membership Management (membership engine slice).
- 3+4 without 1–2 = turnstile/paid-entry hardware with no member relationship.
- 1+3 without 2+4 = free attendance register.
- All four = the gym system: a person can only be a member (1) by holding a standing entitlement (2) whose exercise is facility entry (3) funded by dues (4).

Historical check (older / regional / platform-native products): a 1980s gym satisfies the core with no software-era machinery — a membership card file (1), a signed contract with dues terms (2), front-desk card checking and a visit book (3), and a monthly dues ledger with collections follow-up (4). Access windows existed as peak/off-peak pricing long before RFID. The defining core carries no app, no door hardware, no cloud, no payment rails.

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Class and booking machinery (group classes, appointments, courses, waitlists; entry can auto-check-in a booked session — GymMaster, TeamUp)
- Point of sale and retail/inventory
- Lead-to-member sales funnel / CRM pipeline (all five sampled)
- Member self-service portal / branded app / online signup with waivers
- Staff management (scheduling, permissions, payroll — depth varies by pole)
- Reporting and dashboards (membership counts, recurring revenue, visitation/attendance, retention/churn, at-risk members)
- Marketing & retention automation (at-risk, win-back, lapsed outreach)
- Multi-location support (venues, chains; roaming access; per-location reporting)
- Access-hardware integrations or native door control (tag/card/QR/phone; kiosk; tailgating detection as advanced)
- Waivers and digital forms bound to signup and surfaced at check-in

### L2 — Variant / Optional Structure

- Format posture within one product family: access-led gym vs class-led studio vs hybrid (same vendor sells both; format = which consumption mode dominates)
- Access-window economics: standard / off-peak / 24-7 tiers; group-scoped doors (women-only areas)
- Enforcement posture: hard gating at the door (native access control) vs advisory flags to staff (check-in tool) vs third-party door-hardware integration
- Billing posture: in-product processing vs external billing partner vs manual rails; debt collection in-house vs service
- Enterprise chain extras: centralized membership, roaming across locations, multi-currency/multi-language, corporate dashboards, IP/location login restrictions
- Demand-channel integration (marketplace apps, ClassPass/Wellhub-class networks) and financing add-ons
- Vertical seasoning (workout tracking, belt/skill ranks) when sold into functional-fitness/martial-arts segments

### L3 — Vendor-specific (research notes only, excluded from final document)

- GymMaster: GateKeeper controller hardware, tailgating-detection camera system with photo evidence, women-only door configuration, remote unlock from owner's phone, offline door resilience ("backing up your database"), custom branded key fobs, card-reader API.
- TeamUp: check-in limited to once per day per customer; staff bypass "register for free"; penalties/infractions counters; rentals of courts/saunas/rooms; Stripe Capital financing; nightly blackout for waitlist expiry.
- PerfectGym: two-hour database backup claim, ISO 27001 posture, dedicated employee app, named chain customers (Invictus, Level Up quotes).
- Zen Planner: SugarWOD workout tracking, business insurance cross-sell, Zen Academy onboarding.
- Mindbody: Mindbody Capital, AI Concierge, ClassPass for business, Playlist parent-company platform, IP restrictions/staff login locations, Autopay Detail / Credit Card Expirations report names.

## Vendor-specific Findings

See L3 above. None of these are promoted to the canonical model. The access-led machinery (24/7 door control) is treated as the native implementation pole of entry verification, not as a definitional requirement — TeamUp's advisory check-in tool and Mindbody's third-party door integrations prove the concept exists without native hardware.

## Boundary Findings

1. **vs Fitness Membership Management (processed sibling) — ratified from this side.** The membership engine (member of record + plan catalog/held membership + dues-and-standing cycle) is one pillar of the gym system. Removal tests recorded both directions: strip classes/booking/staff/POS/leads/access-hardware and the gym system still stands on member + membership + entry verification + dues; strip the membership engine and nothing in the gym system runs. The gym Type adds entry verification as the defining consumption mode (in the sibling Type, check-in is standard capability, not core) and the whole-business span.
2. **vs Fitness Studio Management (processed sibling) — joint review DISCHARGED.** Market evidence confirms the sibling pass's flag: one product family is sold across gym and studio formats (TeamUp sells "gym management software" and "yoga studio software" as the same product; Zen Planner serves functional-fitness gyms and boutique studios from one platform; Mindbody lists gym and fitness-club verticals beside studio verticals). Resolution: keep-both with a **format seam** — the seam is which consumption mode defines the business: gym format = standing membership consumed by facility entry (booking optional; "Open Gym" entry without booking is an explicit structure — TeamUp check-in article); studio format = entitlements consumed by the booking-and-attendance loop over a class schedule (definitional there, standard capability here). Test: a gym where nobody ever books anything still runs entirely on this Type; a studio without classes is not a studio. The two leaves document the two realizations of the same product family; no structural contradiction found.
3. **vs Climbing Gym Management (processed sibling) — joint review DISCHARGED.** Keep-all-vertical-leaves ratified: the climbing leaf's identity rests on the climbing-specific structures around the shared business core (waiver-gated participation as flagship workflow, proficiency/certification flags surfaced at entry, perishable wall/routesetting inventory). This leaf documents the generic core those verticals extend. Consistent with the climbing pass's own framing (it cites a GymMaster-class generic product as its non-climbing anchor). The same pattern presumably holds for other vertical siblings (martial arts, swim, gymnastics, dance — dance already processed).
4. **vs Fitness Class Booking (processed sibling):** the booking loop is one workflow inside this Type; the pure-play booking product stands alone (ratified in that pass).
5. **vs Recreation Center Management:** institutional/municipal facilities run on facility-and-program machinery with public funding and registration semantics; the gym system is the commercial membership business. Adjacent, not duplicate.
6. **vs Membership Management System (§25, unprocessed):** same dues/lifecycle skeleton for associations; the gym discriminator is facility-access entitlement semantics (entry verification, access windows) and the commercial-facility operator seat — consistent with the fitness-membership pass's recorded discriminator.
7. **vs CRM / Marketing platforms:** the lead funnel is one standard capability; the member-with-facility-entitlement and the door loop are not CRM structures.
8. **vs Appointment Scheduling / Personal Training Management:** PT appointments are common machinery inside gym systems; the appointment book is not the center.
9. **vs Sports Facility Management:** that Type manages the physical plant; this Type manages the commercial relationship with members and the operation of the business.

## Uncertainties

- Article-level operational docs were reachable only for TeamUp; the other four products are evidenced at product-page level. Accordingly the final document states structures at concept level and avoids numeric limits, default values, and per-product state names (TeamUp's once-per-day check-in limit is held in these notes as product-specific).
- Zen Planner's access-control/check-in machinery was not directly evidenced this pass (page-level only); no access claim rests on it.
- Mindbody was reachable this pass (homepage + FAQ) where three sibling passes recorded it unreachable; help-center article depth was still not reached, so no article-level Mindbody capability is asserted.
- Whether GymMaster supports multi-location chains was not directly evidenced this pass; no multi-location claim rests on GymMaster.
- Market-share or category-leadership statements are deliberately not made; vendor award badges and review-site rankings were observed but not used as evidence.

## Final Synthesis

A Gym Management System is the operator-side whole-business system of record for a facility-membership fitness business. Its defining core is four jointly-held structures: the member of record; the standing facility membership (plan catalog → held entitlement → standing state); entry verification against standing (the daily door loop that both admits and records); and the dues-and-money cycle that funds and governs the entitlement. Everything else the market associates with the category — classes and bookings, appointments, POS/retail, lead funnels, staff management, marketing automation, member apps, 24/7 door hardware, multi-location control — is standard or optional structure integrated around that core. The same product family spans gym and studio formats; the gym leaf is the access-led realization where the membership is consumed by walking through the door, and the studio leaf is the class-led realization where it is consumed by booking. Vertical leaves (climbing, martial arts, dance, swim, gymnastics) extend the generic core with activity-specific safety and program structures.
