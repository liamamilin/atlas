# Research Notes — Sports Academy Management

## Research Goal

Understand what a "sports academy management" application really is by studying how real products serve sports academies and their neighboring organizations (training facilities, clubs, youth sports organizations, class-based children's activity centers): what the system of record holds, how programs/enrollment/money/sessions actually work, and where the boundary lies against the many sibling leaves in §28.

## Initial Boundary

Initial hypothesis before research:

- A sports academy is a training/development organization (often single-sport, often youth) that runs programs: classes, private/group lessons, camps, clinics, and commonly teams that compete.
- The management software is the operator-side business system: athlete records, program offerings, enrollment/registration, scheduling of sessions, billing/payments, family communication.
- Nearest neighbors: Sports Club Management, Youth Sports Management, Martial Arts School Management, Dance Studio Management, Swim School Management, Gymnastics Club Management, Sports Facility Management, Sports Registration Platform, Sports Scheduling Platform, League Management Platform, Team Management Application, Sports Coaching Platform, School/College Athletics Management, Fitness Studio Management.
- Known prior flags to discharge or extend:
  - dance-studio-management pass flagged a **class-management product family** sold per vertical (Jackrabbit Dance/Class/Swim/Cheer/Music; The Studio Director industries incl. youth sports; Studio Pro; iClassPro) and recommended a family-level joint review across the sibling vertical leaves, explicitly naming "adjacent Sports Academy/Club leaves".
  - martial-arts-school-management pass defined the dojo/academy core as student record + programs + membership/enrollment + dues loop.
  - school-college-athletics-management pass defined the institutional department core (portfolio + participation gate + governing-authority loop) — expected to be a clean seam.
  - league-management-platform pass defined the competition core (league + fixture programme + results + standings) — expected to be a clean seam.

## Research Questions

1. What does a "sports academy" run as its offer? (classes, lessons, camps, clinics, teams, memberships, rentals — which are universal, which are pole-specific?)
2. What is the population of record? Athletes? Families? Members? How are minors handled?
3. How does enrollment/registration work? Forms, eligibility rules, capacity, waitlists, approval modes, tryouts?
4. How are programs scheduled and delivered? Sessions, terms/seasons, attendance, makeups, skill progression?
5. How does money work? Tuition/fees/memberships/packages; billing models; payment plans; refunds; POS?
6. What staff/coach machinery exists? Roles, payroll, background checks, certifications?
7. What family-facing surfaces exist? Portal, app, communication?
8. Where does the facility layer sit (courts/fields/cages, rentals) — core or module?
9. Where do teams/competitions sit — core or variant?
10. Where are the seams vs each sibling leaf?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

| Product | Pole | Tier / Market | Why selected |
|---|---|---|---|
| **Upper Hand** | sports training facility / academy operating platform | individual coaches → single facilities → growing academies (2+) → franchises (5+); many sports | The cleanest "academy" product: homepage literally names "sports facility academy lessons teams camps club programs in one system"; rich help center |
| **TeamSnap ONE** | youth sports club & league organization platform | youth sports clubs/leagues (volunteer-led to established clubs) | The organization/season pole: registration → teams → schedules → family communication at scale |
| **iClassPro** | class-management family (gymnastics, cheer, swim, dance, multi-sport children's activity centers) | children's activity centers incl. sports academies | The class/instruction pole and the direct test of the dance-pass family flag; deep operational documentation |
| **Jersey Watch** | youth sports organization platform (website + registration + payments + messaging) | 2,800+ small youth organizations, rec leagues, club programs, camps | The lean/volunteer pole; explicit "who we serve" taxonomy (youth sports / rec leagues / club programs / camps / high school / travel teams) |

Attempted but unreachable (recorded as sourcing limitations):

- **PlayMetrics** ("Youth soccer's first all-in-one club management app") — site is JS-rendered; two fetches returned no content. Club-management pole covered indirectly via TeamSnap/Jersey Watch.
- **eSoft Planner**, **EZFacility** — HTTP 403 on both root fetches. Facility+academy pole covered via Upper Hand only.

## Sources

- Upper Hand — product site https://upperhand.com/ , features page https://upperhand.com/software/ , Help Center https://help.upperhand.com/ (fetched 2026-09-09)
- TeamSnap — product site https://www.teamsnap.com/ , TeamSnap ONE page https://www.teamsnap.com/one (fetched 2026-09-09); help center https://helpme.teamsnap.com/ (not fetched)
- iClassPro — product site https://www.iclasspro.com/ , class management page https://www.iclasspro.com/class-management (fetched 2026-09-09); support center https://support.iclasspro.com/hc/en-us (linked, not fetched)
- Jersey Watch — product site https://jerseywatch.com/ , registration feature page https://jerseywatch.com/features/sports-registration-software (fetched 2026-09-09); help center https://help.jerseywatch.com (linked, not fetched)

Evidence layers used below: **A** = directly observed on the cited product's official pages; **B** = cross-product commonality across the sampled products; **C** = canonical inference from comparison and boundary reasoning.

## Product Observations

### Upper Hand (Layer A)

Positioning: "A Better Way to Operate Your Sports facility **academy** lessons teams camps club programs in one system." Business types served: individual coach/trainer/instructor; sports facility; growing sports facility (2+ locations); franchise sports (5+ locations). Offerings enumerated: private & group lessons; sports camps & clinics; sports registration; classes & programs; teams; rentals.

Feature set (features page + homepage):

- **Scheduling & Registration**: "Build out your programs… Set registration deadlines, age or gender restrictions, day-specific availability and more"; flexible registration, capacity controls, built-in waitlists; "Run private lessons, classes, teams, and clinics".
- **Integrated Payments**: multiple payment options, pricing tiers or payment plans, discounts, recurring billing.
- **Facility & Resource Management**: "Streamline your staff and resource scheduling, eliminate double-booking, and turn your facility's spaces into profit centers with quick scheduling, quick pay, event check-in".
- **Staff & Payroll**: attendance tracking, scheduling, payments in one view; instructor management, access levels, payroll reporting.
- **Membership Management & Analytics**: auto-renewal memberships, member discounts, exclusive access to events.
- **Contact Management**: "Easily manage family profiles, segment leads, and filter contacts into groups"; "Collect waivers and essential documents digitally".
- **Marketing**: email templates, campaigns, performance tracking.
- **Retail & Inventory**; **Mobile app** (admin + client-facing); **Teams**: "Manage rosters, schedules, payments, and more"; add-ons: AI analytics, custom website builder (WebKit).
- Pricing page states "Starts at just $79 per month" (vendor-claimed; kept here only).

Help Center category structure (Tier 1): Getting Started ("software dedicated to providing solutions for sports facilities"); Account Setup (create account, invite staff, customize settings); **Events** ("create events, make registration easy, and utilize your data"); **Classes** ("giving you and your clients ultimate flexibility"); **Teams** ("Manage your rosters, set up automatic payments, input practice and game schedules for your teams"); Calendar ("manage your day, make quick changes and understand your business at a glance"); Contacts ("Managed profiles, Client Profile Pages and Contact Groups"); Marketing; Reports; Memberships; **Credit Passes** ("Control the type, amount and expiration of credits"); Resources ("Streamline your facility scheduling, eliminate double-booking…"); Retail; Settings; **Point of Sale** ("Get clients registered, collect payment"); Payments ("Customizable billing"); **Client Side** ("Guides to help your clients navigate their side of the software").

### TeamSnap ONE (Layer A)

Positioning: "The new standard in club & league management… run and grow your organization in ONE powerful platform." For clubs & leagues: "Registration & payments, schedules, communications, coaching resources, parent app, live streaming."

Feature list (product page): Registration & Payments; Rostering; Organization-Wide Communications; Scheduling; Practice Plans & Drills; Coaching & Player Development; Parent Mobile App; Live Streaming; Website Builder; Financials & Reporting. Plus Tournaments ("smart brackets, live scoring and automated updates") and Websites.

Narrative flow (product page): "Registrations made simple — fast, flexible, mobile-friendly sign-ups with integrated payments and automated reminders"; "Organized from day one — easy roster-building and schedules… from org-wide alerts to team chats"; "Coaches set up for success — drills, practice plans, parent communications and RSVPs"; "Families stay connected — every schedule, message, live stream and highlight in one app… coming back season after season."

### iClassPro (Layer A)

Positioning: "The #1 Class Management Software for Gymnastics, Cheer, Dance and Swim Schools… Manage Classes, Camps, Private Lessons, Birthday Parties, Events, Student Attendance, Staff, Waivers, Email, SMS and more." Also serves "Multi-sport programs that offer a variety of kids based activities for the family."

Class management page (operational detail):

- Class models: "Choose between monthly, session, or rolling session classes. Bill hourly, flat rate, or by time slot."
- Enrollment control: "Auto-approve enrollments or opt for request-only enrollment mode. Provide options such as priority registration, prorated billing, trial classes, waitlists, drop-ins, and punch passes!"
- Real-time online registration with live availability via the Customer Portal: Request Mode (staff reviews/approves each enrollment), Auto-Approve Mode (eligible students instantly booked when spots open), Priority Registration (select families jump the queue with a special keyword); "no double-booking, no surprises".
- Attendance: "touchless check-in kiosk and your instructors and substitute instructors with the staff portal app to easily track attendance."
- Makeups: "online makeup tokens that can be redeemed for another class or session approved for makeup enrollments."
- Skill Tracking: "Skill Bank" of progressions/milestones; custom Skill Trees with videos/images; "skill evaluations that update to your customer's mobile app and online portal"; tracked "directly from the attendance screen".
- Classes page as control center: "create, edit, or cancel classes, manage enrollments, track attendance, and even send email blasts… Quick Edit, view instructor assignments, class occupancy, schedules."
- Calendar: "Create new classes, camps, appointments and party bookings directly from the Calendar! Blackout schedules let your customers know in advance of planned closures with the option of prorated billing."
- Reports: KPI widgets — "active families, enrollments, student counts, drops, transfers, and payments."
- Communication: announcements/updates/reminders/cancellations via push, SMS, email; Autopilot workflows.
- Staff: staff portal (planned absences, attendance, skill evaluations); Time Clock ("one-punch system"); front-desk and staff attendance.
- Other modules: Point of Sale, Payments (own payment services), Customer Portal (branded), Branded App, Party Booking Management (iPartyPro), Integrated Websites, Appointments (private lessons), Events & Camps, QuickBooks integration, Automatic Card Updater.
- Scale claim: "Over 100 Million Class & Camp Registrations" (vendor-claimed; kept here only).

### Jersey Watch (Layer A)

Positioning: "The all-in-one platform for youth sports organizations — build a website, register players, manage payments, and keep families informed, all in one place." Who they serve: Youth Sports; Rec Leagues; Club Programs; Sports Camps; High School Teams; Travel Teams. One product, all organization shapes.

Registration feature page (operational detail):

- Forms: custom questions; "Include Waivers, Agreements, and Disclaimers… require players complete them during registration"; "Collect Required Documents… player photos, age verification, or proof of address"; family & multi-player discounts.
- Payments: discount codes; "Enable Payment Plans… pay in automatic installments"; donations; "Sell Items During Registration".
- Player management: "Sort players during and after registration by name, age, division, or any other criteria"; "Issue Refunds Quickly… full or partial refunds"; contact info auto-collected; bulk messages.
- Also: export to spreadsheets; team registrations for tournaments (fees from teams, sort by team name/division/coaching info); mobile-compatible forms; multiple age divisions/skill levels ("no limit to the amount of programs you can create… customize the registration form and pricing for each age group").
- Other features: website builder; scheduling ("post game & event schedules online"); communication tools (text/email to teams, divisions, or entire organization); background checks for coaches and volunteers; donations/sponsorships.

## Cross-product Comparison

| Structure | Upper Hand | TeamSnap ONE | iClassPro | Jersey Watch | Strength |
|---|---|---|---|---|---|
| Participant population of record | Contacts: family profiles, client profile pages, contact groups | players/families via registration; parent app | families/students; customer portal | players; contacts auto-collected at registration | B — all four |
| Minors on family accounts (guardian as payer/contact) | family profiles | parent app; families | family-based children's activity centers | parents register players; family discounts | B — all four (youth-dominant market) |
| Program portfolio as the offer | events, classes, lessons, camps/clinics, teams, rentals, memberships | registration programs → teams; tournaments | classes (monthly/session/rolling), camps, appointments (private lessons), parties, events | registration programs by age division/skill level | B — all four; program mix varies by pole |
| Enrollment/registration into programs | registration deadlines, age/gender restrictions, day-specific availability, capacity, waitlists | registration forms → roster building | enrollment wizard; auto-approve/request/priority modes; trials, drop-ins, punch passes, waitlists | forms with custom questions, waivers, document uploads, discounts | B — all four |
| Program money loop | pricing tiers, payment plans, discounts, recurring billing, memberships, credit passes, POS | registration payments; financials & reporting | billing hourly/flat/time slot, prorated billing, autopay, POS, payment services | payments, payment plans, refunds, donations, item sales | B — all four |
| Schedule of sessions/games | calendar; day-at-a-glance | schedules (practices/games) | calendar; blackout schedules with prorated billing | schedules posted online | B — all four |
| Attendance/check-in | attendance tracking (staff view) | RSVPs | kiosk check-in + staff portal attendance | — | B — 3 of 4 (Jersey Watch page silent) |
| Family communication | reminders, targeted messages, client app | org-wide comms, team chats, alerts | push/SMS/email, Autopilot | text/email announcements | B — all four |
| Family self-service surface | client-side mobile app | parent app | customer portal + branded app | website-embedded registration | B — all four |
| Teams (roster, practices/games) | teams module (rosters, schedules, payments) | core unit (rostering, team chats) | — (not in class pole) | team registrations; schedules | A(UH/TS/JW) — pole-dependent |
| Skill/progression tracking | athlete evaluation template (resource) | practice plans/drills (content, not per-athlete tracking) | Skill Bank/Skill Trees, evaluations | — | A(iCP) — pole-dependent |
| Facility/resource scheduling & rentals | core module (resources, rentals, double-booking) | — | — (space implied via parties/appointments) | — | A(UH) — pole-dependent |
| Memberships / packages / credits | memberships, credit passes | — | punch passes, drop-ins | — | A(UH/iCP) — pole-dependent |
| Staff/payroll/time clock | staff & payroll | coaching resources | staff portal, time clock | background checks | B — varied depth |
| Website builder | WebKit add-on | website builder | integrated websites | website builder | B — all four |
| Marketing/lead capture | marketing campaigns, lead segmentation | — | email blasts, Autopilot | donations/sponsorships | B — varied depth |
| Background checks | — | — | — | background checks for coaches/volunteers | A(JW) — youth-pole common |
| Tournaments/brackets | — | tournaments with brackets/live scoring | — | team registrations for tournaments | A(TS/JW) — org-pole |

Reading of the comparison:

- The **shared spine** (population + program portfolio + enrollment + money + schedule + family communication) holds across all four products regardless of pole — evidence layer B, and it matches the spine already documented in the martial-arts and dance sibling passes.
- The **program mix** is the pole signature: training pole = lessons/camps/memberships/rentals; class pole = session classes/skills/makeups; org pole = registration programs/teams/seasons.
- Teams, facility scheduling, memberships, skill tracking, background checks are each present in some products and absent (or silent) in others → standard-or-variant, not definitional.
- No product in the sample is competition-administration-first (fixtures/results/standings) — that machinery belongs to League Management Platform, confirming a clean seam.

## Canonical Model (L0–L3)

### L0 — Defining Invariant

The sports academy's business system of record, held as four jointly-loaded structures:

1. **The academy's athlete population of record** — persistent identified athlete records (commonly minors held on family accounts, with guardians as payers/contacts), accumulating enrollment, attendance, and payment history across seasons. Remove → a contact/CRM database.
2. **The academy's program portfolio as its offer** — the training programs the academy runs (recurring classes, private/group lessons, camps, clinics, teams — the mix varies by academy), each configured with schedule, staff, capacity, and price, and delivered as sessions over a season/term rhythm. Remove → a generic scheduler or a people database with no offer.
3. **Enrollment binding athletes into programs** — registration/enrollment records that bind a specific athlete to a specific program offering under eligibility rules (age/skill/gender where configured) and capacity limits, forming the rosters that determine who attends what; selective programs admit via placement or approval. Remove → a sign-up form or a class directory with no binding.
4. **The program money loop** — program-driven charges (tuition/fees/camp prices/membership dues/package credits) posted to the athlete's family or member account and settled by payment, with payment plans, discounts, prorating, refunds, and arrears actionable in the same system. Remove → a roster app; the academy stops being run as a business in the system.

Jointly-held load-bearing:

- 1 alone = people/CRM database
- 2 alone = timetable/schedule machinery
- 3 without 1+2 = a sign-up form
- 4 without 1–3 = a billing engine with nothing to bill for
- 1+2 without 3+4 = a class directory
- 1+3+4 without 2 = enrollments with no delivery calendar
- 2+3+4 without 1 = anonymous bookings (Sports Court Booking / booking-loop territory)

### L1 — Common Mature Structure (standard, not definitional)

- Session delivery machinery: attendance/check-in (kiosk, staff portal), makeups, RSVPs
- Family communication: email/SMS/push announcements, reminders, cancellation notices
- Family self-service: portal/branded app (enroll, pay, view schedule/progress)
- Staff management: instructor/coach assignment, staff portal, time clock/payroll (depth varies)
- Teams as a program format: tryouts, rosters, practice/game schedules, team communication
- Skill/progression tracking and evaluations (class pole deepest)
- Memberships, packages/credit passes, drop-ins (training/class poles)
- Facility/resource scheduling and rentals (training pole deepest)
- Waivers/agreements collected at registration; document uploads
- Background checks for coaches/volunteers (youth pole)
- Websites (integrated or add-on builder); marketing/lead capture; reporting/dashboards; retail/POS

### L2 — Variant / Optional Structure

- Pole: training-facility/booking-first vs class/instruction-first vs club/season-first (registration→teams→schedule)
- Sport scope: single-sport vs multi-sport; sport-generic vs sport-branded
- Age scope: youth-dominant (family accounts, guardians) vs adult (individual member records; sports-performance facilities)
- Scale: single location vs multi-location/franchise (white-label apps at the top pole)
- Billing model: per-session/per-term tuition vs monthly recurring vs membership/package economy
- Competition posture: non-competitive instruction vs fielding teams in external leagues/tournaments
- Deployment: cloud SaaS universal in sample; web + mobile app + kiosk surfaces vary

### L3 — Vendor-specific (research notes only)

- Upper Hand: WebKit website builder ($50/month vendor-claimed), Camp Pulse camp product, Upper Hand AI add-on, UHU learning platform, UPLIFT community, "starts at $79/month" claim, Loop (announced AI chat), status page, public API "coming soon".
- TeamSnap ONE: Falcon AI streaming camera (XbotGo partnership), MLS NEXT / pro-league practice-plan content, brand sponsorship programs ($20M giveback claim), launchnotes product updates.
- iClassPro: iCampPro sibling product, iPartyPro party booking, Pro Insights dashboard, Autopilot workflows, QuickBooks on Autopilot, Automatic Card Updater, merchant portal, "100M+ registrations" and Inc 5000 claims, one-punch time clock, ProCal calendar, priority-registration keyword mechanism.
- Jersey Watch: schedule generator tool, registration fee calculator, G2/Trustpilot/Capterra review counts, "2,800+ organizations / 1M+ athletes" claims, named comparison pages vs SportsConnect/PlayMetrics/SportsEngine/LeagueApps/LeagueLineup/TeamSnap/TeamLinkt/Crossbar.

## Historical / Market-Sample Check (§24)

- Paper-era academy: a 1980s tennis or soccer academy keeping index-card athlete files, a printed season program brochure, enrollment forms, a session schedule on a whiteboard, and a fee ledger satisfies all four L0 legs with no software. **Passes.**
- Regional academies (e.g., cricket academies in South Asia, football academies in Europe/Africa/Latin America, table tennis academies in East Asia) run the same four structures without US-style registration platforms. **Passes.**
- Adult academies (sports-performance facilities training adults on individual memberships) satisfy the core with individual records instead of family accounts — the family account is the dominant implementation for minors, not the invariant. **Passes.**
- Conclusion: the L0 is era- and region-neutral; nothing in it depends on the current US youth-sports registration pattern.

## Vendor-specific / Rejected Findings

- **Teams are NOT definitional**: gymnastics/swim/tennis academies run class/lesson programs without fielding teams (iClassPro industries; Upper Hand serves those sports). Teams = standard program format, strongest at the club/season pole.
- **Facility scheduling is NOT definitional**: absent/silent in iClassPro and Jersey Watch; a module in Upper Hand. Capability slice, not core.
- **Memberships/packages are NOT definitional**: present in Upper Hand (memberships, credit passes) and iClassPro (punch passes, drop-ins), silent in TeamSnap/Jersey Watch pages.
- **Skill tracking is NOT definitional**: deepest in iClassPro; Upper Hand offers an evaluation template (a resource, not a module); TeamSnap offers practice-plan content, not per-athlete tracking.
- **Background checks are NOT definitional**: youth-pole safeguard (Jersey Watch explicit; others silent on fetched pages).
- **Competition administration (fixtures/results/standings) is NOT part of this Type**: no sampled product centers it; TeamSnap's tournaments are event operations, not league standings computation.
- **Money-state gating at check-in** (block entry on past-due balance): documented in the martial-arts sibling pass but NOT evidenced on the pages fetched this pass — not asserted in the final document.
- PlayMetrics' "club management" positioning could not be verified at documentation level (JS-rendered site) — no claims made about it beyond its tagline.

## Boundary Findings

1. **vs Martial Arts School Management / Dance Studio Management / Swim School Management / Gymnastics Club Management (the class-management family)** — same spine (population + programs + enrollment + money loop); verticals differ in signature extensions (dance: costumes/recitals; martial arts: ranks/belt testing; sports academy: multi-format program mix — classes + camps + clinics + lessons + teams + rentals + memberships — and sport-generic scope). This pass **extends the dance-pass family flag**: a family-level joint review across the vertical leaves is needed to decide keep-both-with-seam vs variant presentation. This leaf holds the seam by keeping the core at the shared spine and documenting the sports layer as standard-not-definitional.
2. **vs Sports Club Management (unprocessed sibling)** — club = member/competition organization (teams in leagues, member governance); academy = training/development organization (program portfolio). Market overlap is heavy: Jersey Watch sells one product into "Club Programs" and "Youth Sports"; TeamSnap ONE self-labels "club & league management" while serving academy-shaped organizations; many soccer "clubs" call themselves academies. **Flag recorded for that pass**: proposed discriminator = center of gravity (program/training-led vs membership/competition-led), with the expectation that the two leaves share most of the spine.
3. **vs Youth Sports Management (unprocessed sibling)** — youth-sports organizations are registration/season-led (leagues, rec programs, volunteer boards); academies are program/training-led (tuition businesses). TeamSnap/Jersey Watch sit between the two; the org pole of this leaf's sample IS youth-sports software. **Flag recorded for that pass.**
4. **vs Sports Facility Management (unprocessed sibling)** — facility = rentable-space inventory + bookings; academy = programs + enrollment. Upper Hand bundles facility/resource scheduling as a module inside academy software (the same capability-slice pattern as fitness-class-booking vs fitness-studio-management). Keep-both with a center-of-gravity seam; **flag recorded for that pass**.
5. **vs Sports Registration Platform (unprocessed sibling)** — one-shot registration transactions vs the ongoing academy relationship (rosters, attendance, recurring billing). Jersey Watch's registration page shows the transaction layer; the academy layer adds the persistent program/enrollment/money loop. Same seam as dance-studio-management vs registration. **Flag recorded for that pass.**
6. **vs League Management Platform (processed)** — clean seam: competition administration (league container, fixture programme, results, computed standings) vs training business (programs, enrollment, tuition). An academy's teams PLAY in leagues run on league platforms; the academy system records enrollment and team logistics, not standings computation.
7. **vs Team Management Application (unprocessed sibling)** — single-team operations (one roster, one schedule, one communication graph) vs multi-program organization (many programs, many rosters, one business). Clean seam; Upper Hand's teams module manages multiple teams inside the business system.
8. **vs School/College Athletics Management (processed)** — clean seam: institutional department (program portfolio + participation gate + governing-authority loop, compliance-facing) vs commercial training business (tuition-facing). An academy is a business selling instruction; a school athletics department administers institutional participation under external rules.
9. **vs Sports Coaching Platform (unprocessed sibling)** — Upper Hand's "individual coach" pole (booking, billing, zero admin) sits at this seam: a single coach's client business vs a multi-program organization. **Flag recorded for that pass.**
10. **vs Fitness Studio Management (processed)** — adult membership/drop-in class economy vs guardian-child program-tuition economy; adult sports-performance facilities sit at this seam (Upper Hand serves "sports performance"). Consistent with the fitness-studio pass's structural seam.

## Uncertainties

- PlayMetrics unreachable (JS-rendered, 2 attempts) — the soccer club-management pole is unverified at documentation level; its tagline ("Youth soccer's first all-in-one club management app") is the only claim recorded.
- eSoft Planner and EZFacility returned HTTP 403 — the facility+academy pole beyond Upper Hand is unverified.
- TeamSnap ONE and Jersey Watch help centers were not fetched; their operational flows (registration → team assignment mechanics, season rollover) are asserted at product-page strength only (Layer A marketing/features), not help-center depth.
- iClassPro support center linked but not fetched; class-pole operational detail comes from the vendor's own feature pages (Layer A, unusually detailed).
- Exact numeric limits (class sizes, credit expirations, pricing) deliberately not asserted — vendor-claimed figures kept in research notes only.
- Whether the market converges on ONE family Type with the class-management verticals (per the dance flag) or keeps separate vertical Types is a taxonomy decision for the recommended family joint review — not decidable from this pass alone.

## Final Synthesis

A Sports Academy Management application is the **sports training organization's business system of record**. Its defining core is four jointly-held structures: the academy's athlete population of record (persistent identified athletes, commonly minors on family accounts), the academy's program portfolio as its offer (classes, lessons, camps, clinics, teams — configured with schedule, staff, capacity, price, delivered as sessions over a season/term rhythm), enrollment binding athletes into programs under eligibility and capacity rules (forming rosters), and the program money loop (program-driven charges posted to the family/member account and settled by payment, with plans, discounts, prorating, refunds, and arrears actionable in-system).

Everything else the market associates with the category — attendance/kiosk check-in, skill tracking, makeups, family portals and apps, communication automation, staff/payroll, facility scheduling and rentals, memberships/packages, teams and tournaments, background checks, websites, marketing, reporting — is standard mature capability or pole-dependent variant, not definition. The Type is realized in poles (training-facility/booking-first, class/instruction-first, club/season-first) that share the spine; the class-management family flag from the dance pass extends here, and a family-level joint review across the vertical sibling leaves is recommended.
