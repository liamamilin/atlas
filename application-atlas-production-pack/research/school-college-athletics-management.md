# Research Notes — School / College Athletics Management

Research date: 2026-09-09
Slug: `school-college-athletics-management`
Directory leaf: "School / College Athletics Management" (Section 28 — Sports & Recreation, after Youth Sports Management)

---

## Research Goal

Understand what software for managing a school's or college's athletics department actually is: what the department's system of record holds, what work flows through it, who operates it, and where its boundary lies against neighboring Types (team management, sports registration, eligibility management, league management, SIS, referee management, athlete management).

## Initial Boundary (hypothesis before research)

- Hypothesized core: an athletics department (one school or one college) runs many sports programs; the department's software must manage programs, athletes, clearance/eligibility, schedules, facilities, staff, and reporting to governing bodies (state associations / NCAA).
- Likely confusions:
  - Team Management Application (single team, parent/coach-facing)
  - Sports Registration Platform (signup events for clubs/leagues)
  - Sports Eligibility Management (directory sibling — possible overlap)
  - League Management Platform (multi-organization competition)
  - Student Information System / School Management System (whole school)
  - Referee Management Platform (officials assigning)
  - Athlete Management System (performance/preparation, already documented — its doc calls this Type "adjacent: administrative department operations")
- Unknowns: whether scheduling is definitional or only common; whether the college pole (NCAA compliance) shares a core with the K-12 pole; whether "eligibility" products constitute the whole category or one pole.

## Research Questions

1. What is the unit of record — the department, the program, the team, the athlete?
2. What does "registration / clearance / eligibility" concretely consist of, and who computes it?
3. What role do external rule authorities (state associations, districts, NCAA) play in the product?
4. Which operational loops exist (scheduling, facilities, officials, payments, communication) and are they universal?
5. What roles exist (AD, coach, medical staff, district admin, family, association) and what can each do?
6. How does the season/year cycle structure the work?
7. How does the college pole differ from the K-12 pole?
8. Where are the boundaries against neighboring Types?

## Representative Products

Selected for market representation, documentation quality, different product philosophies, and different customer tiers:

| Product | Pole | Tier | Philosophy |
|---|---|---|---|
| FinalForms | registration / clearance / compliance-first | K-12 schools & districts | the department's compliance system of record; forms-driven |
| Arbiter (ArbiterSports / Arbiter Game) | connected department platform | K-12 schools, districts, state associations | one connected system: registration, scheduling, facilities, payments, officials, eligibility, websites |
| DragonFly Max | state-association ecosystem platform | K-12 via 20+ state associations | unite association, schools, officials, families in one platform; preseason/in-season/postseason |
| JumpForward (ACTIVE Network) | college compliance & recruiting | 350+ college athletic departments | NCAA compliance toolbox + recruiting + department digital workflows |

Dropped / noted:
- **BigTeams** — site now presents Arbiter branding and demo links to arbiter.io (acquired; same vendor family). Not usable as an independent sample.
- **Bound (rSchoolToday)** — www.gotobound.com transport error on fetch; dropped after failure (network rule). rSchoolToday appears as an integration partner in DragonFly's partner list, confirming the vendor family is active in this market.

## Sources

All Layer A unless noted. Fetched 2026-09-09.

- FinalForms — homepage: https://www.finalforms.com/
- FinalForms — Athlete Eligibility & Clearance: https://www.finalforms.com/athletic-management/athlete-eligibility-tracking/
- FinalForms — Athletic Forms & Registration (referenced): https://www.finalforms.com/athletic-management/athlete-registration-software/
- Arbiter — homepage: https://www.arbitersports.com/ (served via arbiter.io)
- Arbiter — Arbiter Game (scheduling): https://arbiter.io/products/scheduling/
- Arbiter — K-12 market: https://arbiter.io/markets/k-12/
- DragonFly — homepage: https://www.dragonflymax.com/
- DragonFly — For Schools: https://www.dragonflymax.com/schools
- JumpForward — product page: https://www.jumpforward.com/

Not reached (limitations):
- Vendor help centers / knowledge bases (FinalForms documentation portal, Arbiter Zendesk help center, DragonFly help articles) were not fetched this pass; evidence is from official product/marketing pages, which are Tier 1–2 but not step-by-step operational docs.
- Bound (rSchoolToday successor) unreachable.
- No pricing, no numeric limits, no exact state-name lists were used from memory; all numeric claims below are quoted from fetched pages.

---

## Product A — FinalForms (K-12, registration/clearance/compliance-first)

### Key observations (Layer A)

Positioning: "School Registration, Compliance & Safety Software"; "Manage your athletic department with real-time visibility across sports, seasons, and compliance"; "FinalForms isn't a forms software. It's the system of record for compliance, communication, and safety." Solutions list: K-12 Enrollment & Registration; **Athletic Management**; Staff Forms & Certification; Parent Communication; Emergency Medical Preparation; State, District & Department Compliance; Association Management Platform.

Athletic Management solution set:
- **Athletic Forms & Registration** — "Collect physicals, consents, and sport policies online."
- **Athlete Eligibility & Clearance** — "Track forms, clearance, and return-to-play in real time."
- **Alerts, Notifications & Countdowns** — "Alert on expirations, missing items, and eligibility changes."

Eligibility page (operational detail):
- "Eligibility dashboards: View clearance status by athlete, sport, school, or coach — updated in real time."
- "Physical expiration tracking: Monitor countdowns and send automatic reminders before athletes fall out of compliance."
- "Return-to-play documentation: Track injury reports, upload doctor clearances, and verify status before athletes return."
- "Form status filters & flags: Instantly identify athletes who are missing forms, overdue for physicals, or flagged for medical reasons."
- FAQ: "Eligibility is determined by form completion, physical clearance, medical flags, and required acknowledgments — all tracked in real time."
- FAQ: "Every action — submission, approval, expiration — is time-stamped and stored for future reference or audit purposes."
- Stakeholders: coaches ("Know who's cleared and who's not — before practice starts"), athletic directors ("Ensure athletes meet district and state eligibility rules across all teams... full visibility across levels and seasons"), parents ("automated alerts... submit forms and updates from any device").
- Compliance framing: FERPA compliance; audit-ready records; "district and state eligibility rules".

Other structures: SIS integration (PowerSchool, Infinite Campus, Skyward); staff forms & coaching certifications with role-based access; parent communication targeted "by status, sport, clearance, or role"; emergency medical E-Cards ("team-synced student medical info") and injury/return-to-play records; partnerships with NFHS, NIAAA, state athletic associations.

**Notably absent from FinalForms' athletic solution: contest scheduling, facilities, officials, ticketing.** The product is a registration/clearance/compliance pole.

## Product B — Arbiter / ArbiterSports (K-12 + associations, connected department platform)

### Key observations (Layer A)

Positioning: "The Connected Platform for K-12 Sports and Activities. Manage registrations, schedules, payments, facilities, and eligibility in one connected system." Products: Pay, Eligibility (coach and official eligibility), Student Registration, Assigning Solutions, Event and Game Scheduling, Arbiter360, Facilities Scheduler, Athletic Websites. Markets: Assigning Associations, K-12, Governing Bodies.

K-12 market page:
- "Digital student registration and form management"; "Integrated payment collection"; "Centralized scheduling for academics and athletics"; "Automated payments for contractors, coaches, and staff"; "Real-time financial reporting and expense tracking"; "Integrated ticketing, streaming, and fan gear"; "Event notifications for parents, students, and staff"; FERPA + SOC 2; "Real-time compliance alerts and automated tracking".
- Case-study framing: "Single point of access for all athletic operations"; "Manage 14 varsity sports programs" (one school's count — product-specific).

Arbiter Game (scheduling product):
- "Arbiter Game gives athletic departments one place to schedule games, manage officials and staff, coordinate facilities, and publish updates."
- "Schedule athletics and non-athletic events in the same platform"; "Prevent conflicts with built-in scheduling rules and validations"; "Multi-Level Scheduling: Coordinate across varsity, JV, and middle school levels"; "League Scheduler: Manage league schedules and push updates to all participating schools"; "Conflict Checker: Detect overlapping games or facility usage"; "Facility Integration: Sync facility bookings through Arbiter Facilities Scheduler."
- "Maintain accurate team and roster data year-round"; "Sync eligibility details with Arbiter Registration."
- "Publish updates instantly to connected websites and platforms... Notify staff, officials, and families automatically."
- Users: "Athletic Directors: Oversee event scheduling, rosters, and facilities in one system. Coaches: View and share schedules... Officials & Assigners: Connect seamlessly to assignments through Arbiter Assigning. District & League Admins: Gain top-down visibility across schools."

Governing Bodies market: "Manage rules, schedules, and compliance across every school from one platform... Visibility into schedules and eligibility across all schools; consistent rule enforcement and compliance tracking; championship and postseason scheduling support."

Payments: Arbiter Pay — pay officials and event workers; 1099/W-2 automation; "verify the official showed up for the game and transfer money from the school's account to the official's account" (association officer quote).

Also: injury management feature inside registration (blog title); athletic websites publishing schedules/results (ArbiterLive).

## Product C — DragonFly Max (K-12 via state associations, ecosystem platform)

### Key observations (Layer A)

Positioning: "A Comprehensive Solution for Athletics Management... specifically designed to streamline the complexities of high school sports administration... for state athletic associations, schools, athletic directors, and officials." Reach: "Over 20 State Associations", "1.5 Million+ student athletes", "300,000 officials", "80,000+ athletic directors and coaches". Framing: "a cost effective and flexible platform built to manage the Preseason, In-Season & Postseason."

Pain-point list (vendor's own framing of the department's job): certifications/exams/eligibility management; coordinating officials; paperwork for coaches and parents; limited visibility into athletic department finances; inconsistent data management for schools and teams.

For Schools:
- **Rosters & Eligibility** — "It's Your School's Athletic Data Hub"; "Simplify roster management for teams and levels"; "Easily see who is eligible to play"; "Custom forms for simplified, paperless registration"; "3rd party data integration for academic eligibility."
- **In-Season tools** — "Unified Game Schedules"; "Game Contracts and tracking game detail changes"; "Easy and secure payments for officials and game workers"; "Collect Team Fees easily"; "Manage tournaments"; data integration with partners.
- **Player Safety** — "Fingertip access to physicals and medical information"; "Injury reports"; "Emergency contact information"; oversight of communication; "Key People reports with photos and contact info for school resource officers on game day."
- **Communication** — unified messaging with oversight ("+1 communication"); team news feeds; "Free public website with game schedules, rosters, and links to ticketing providers and live streams."
- Trainer quote: "quickly communicate to coaches regarding their athletes' playing status, compliance with rehab, and restrictions."

For Associations: "Membership Management; Unified Game Schedules; Eligibility & Certifications; Officials Assignments; Communication Tools." For Officials: certifications, NFHS COS & Exam Center integration, payments. For Financial Admins: payments and financial reporting.

Integration partners: GoFan, HomeTown Ticketing, MaxPreps, PowerSchool, RenWeb, rSchoolToday, Stripe, VNN, SquadLocker, etc. — ticketing/streaming/publishing are partner-integrated, not owned.

## Product D — JumpForward / ACTIVE Network (college athletics departments)

### Key observations (Layer A)

Positioning: "Take your athletics department to the next level... over 350 college athletic departments use JumpForward." Numbers: 20k coaches, 255k+ student athletes, 16m recruiting profiles.

Solution set:
- **NCAA Compliance** — "From automating the reporting of recruiting activities by coaches and staff to submitting and approving CARA logs, The Compliance Toolbox® saves time... Built-in NCAA rules engine; Comp ticket management; Flexible workflows; Financial aid monitoring."
- **Recruiting** — recruiting board, calendar, mobile apps, branded email system for coaches.
- **Marketing** — branded emails, custom websites, registration pages (fans, alumni, recruits).
- **Digital forms & workflows** — department-wide digital processes; compliance director quote: "scholarship renewal process shorter and easier"; "redesigned some procedures in our department and across campus."
- **Camp Registration** — online camp registration and payment processing.
- **Equipment Management** — inventory, assign/check-in, roster updates, reporting.

The college pole centers on the governing-body compliance loop (NCAA rules engine, CARA logs, financial aid) plus recruiting and department operations; no K-12-style physical-clearance machinery is described on the fetched pages.

---

## Cross-product Comparison

| Structure | FinalForms | Arbiter | DragonFly | JumpForward | Strength |
|---|---|---|---|---|---|
| Department as context (school/college athletics dept) | ✔ "athletic department... across sports, seasons" | ✔ "athletic departments one place" | ✔ "School's Athletic Data Hub" | ✔ "athletics department" | Universal (A) |
| Portfolio of sports/teams/levels/seasons | ✔ "sports, seasons... levels" | ✔ teams/rosters year-round; varsity/JV/middle school | ✔ "roster management for teams and levels" | ✔ (implied; sports programs) | Universal (A) |
| Student-athlete records bound to school | ✔ athletes w/ clearance status | ✔ rosters synced with registration | ✔ rosters & eligibility | ✔ 255k+ student athletes | Universal (A) |
| Participation gate (clearance/eligibility state) | ✔ explicit: forms+physical+medical+acknowledgments | ✔ eligibility product; sync w/ registration | ✔ "see who is eligible to play" | ✔ NCAA rules engine (compliance gate) | Universal (A) |
| Physical/medical clearance & return-to-play | ✔ explicit | ✔ injury management feature (blog) | ✔ physicals, injury reports, playing status | ✖ (not on fetched pages) | Common K-12 (A) |
| Governing-authority layer (state assoc./district/NCAA rules + reporting) | ✔ district & state eligibility rules; compliance dashboards | ✔ Governing Bodies market; compliance tracking | ✔ association membership, eligibility & certifications | ✔ NCAA rules engine, CARA logs, financial aid | Universal (A) |
| Family/student self-service registration | ✔ | ✔ | ✔ custom forms, paperless | ✔ (camps; digital forms) | Universal (A) |
| Contest/event scheduling | ✖ absent | ✔ core (Arbiter Game) | ✔ unified game schedules, contracts, tournaments | ✖ (recruiting calendar only) | Common, NOT universal |
| Facilities coordination | ✖ | ✔ Facilities Scheduler | (partner integrations) | ✖ | Optional |
| Officials assigning & payments | ✖ | ✔ Arbiter One / Pay | ✔ officials assignments, payments | ✖ | Common K-12, optional |
| Communication w/ oversight | ✔ by status/sport/clearance/role | ✔ notifications | ✔ unified messaging, oversight | ✔ branded email | Universal (A) |
| Public-facing surfaces (websites, schedules) | ✖ | ✔ athletic websites, ArbiterLive | ✔ free public website | ✔ custom websites | Common |
| Staff/coach certification tracking | ✔ | ✔ (officials/coach eligibility) | ✔ certifications, exams | (compliance workflows) | Common |
| Payments/fees | (registration payments implied) | ✔ Pay, fees | ✔ team fees, officials pay | ✔ camp payments | Common |
| Academic eligibility data | (SIS integration) | (eligibility sync) | ✔ "3rd party data integration for academic eligibility" | ✔ financial aid monitoring | Common |
| Medical/injury & emergency info | ✔ E-Cards, injury reports | ✔ injury management | ✔ player safety suite | ✖ | Common K-12 |
| Recruiting / camps / equipment / NIL | ✖ | ✖ | ✖ | ✔ | College-pole variant |
| Ticketing / streaming / fan gear | ✖ | ✔ partner-integrated | ✔ partner links | ✖ | Optional, partner-integrated |

### Reading of the comparison

- The **department + program portfolio + athlete records + participation gate + governing-authority layer** appear in all four products across both tiers → definitional candidates.
- **Contest scheduling** is absent from the registration-first pole (FinalForms) and from the college pole's fetched pages → common mature structure, not definitional.
- **Officials, facilities, payments, public websites** are module-level capabilities distributed unevenly → common/optional.
- **Physical/medical clearance machinery** is K-12-dominant; the college pole gates participation through NCAA compliance instead → the abstract invariant is the *gate*, not the physical.
- **Recruiting/camps/equipment** are college-pole variants.

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

The school/college athletics department's system of record, holding exactly three jointly-dependent structures:

1. **The department's program portfolio as the unit of record** — persistent records for the school's/college's sports programs (teams by sport, level, season) and the people attached to them (coaching staff, student-athletes), maintained across seasons as the department's authoritative picture. Remove → a single-team app (Team Management) or a form tool with no department memory.
2. **The participation gate over student-athletes** — each athlete carries a tracked clearance/eligibility state (registration requirements, medical/physical clearance, acknowledgments, academic standing, association rules) that determines whether they may practice or compete, visible to staff before activity. Remove → a schedule/website tool with no right-to-play machinery, or generic form collection.
3. **The governing-authority loop** — the rules the department enforces are set by authorities above it (district, state association, collegiate body); the system carries the department's obligations to those authorities (rule-configured requirements, reporting/attestation, audit-ready time-stamped records). Remove → private-club/league management with no institutional accountability layer.

Jointly-held load-bearing:
- 1 alone = roster/org database
- 2 without 1 = standalone eligibility/registration tool (Sports Eligibility Management / Sports Registration Platform territory)
- 3 without 1+2 = compliance rulebook with nothing to govern
- 1+2 without 3 = private club with clearance but no institutional authority
- 1+3 without 2 = compliance reporting with no participation gating
- 2+3 without 1 = eligibility machinery with no department memory

### L1 — Common Mature Structure

- family/student self-service registration with e-forms and status tracking
- contest/event scheduling with conflict checking, multi-level teams, league/conference coordination
- facilities coordination; officials/staff assignment and payment
- targeted communication (by sport, status, role) with automated reminders
- public-facing surfaces (schedules, rosters, athletic websites)
- medical/injury tracking, emergency info, return-to-play documentation (K-12)
- coaching-staff certification tracking
- fee collection and payments to officials/event workers
- reporting/dashboards for department, district, association
- SIS / student-data integration for academic eligibility

### L2 — Variant / Optional Structure

- deployment model: school-purchased vs state-association-mandated ecosystem (association membership management, association-side dashboards)
- tier variant: college pole — NCAA/collegiate compliance machinery (rules engine, recruiting-activity logs, financial aid monitoring, comp tickets), recruiting boards, camps, equipment management
- activities-beyond-sports (bands, clubs, activities departments)
- ticketing, streaming, fan gear (partner-integrated)
- fundraising; team-store integrations
- academic-eligibility data feeds (3rd-party)
- non-athletic events sharing the same platform

### L3 — Vendor-specific (Research Notes only)

- Arbiter: Arbiter Game / Arbiter One / Arbiter Pay / Arbiter360 / ArbiterLive product naming; "Smart Scheduler"; W-2/1099 automation claims; "2 hours a day" time-savings claim; 200,000+ officials; 7M families; De La Salle "14 varsity sports" case figure.
- FinalForms: E-Cards; "3,000+ schools" / "10,000+ schools" (inconsistent on-page counts); 99.7% retention claim; countdowns vocabulary.
- DragonFly: "+1 communication" oversight concept; "Key People reports" for game-day school resource officers; NFHS COS & Exam Center integration; "free for schools" model; 20+ associations / 1.5M athletes / 300k officials / 80k ADs-coaches counts.
- JumpForward: Compliance Toolbox®; MyJF profile tab; "16m recruiting profiles"; 350+ institutions.

## Rejected Findings (not promoted)

- **Contest scheduling as definitional** — rejected: FinalForms (in-type, registration/clearance pole) has no scheduling; JumpForward's fetched pages show none. Held common-mature.
- **Physical-examination clearance as definitional** — rejected: college pole gates via NCAA compliance, not physicals; the invariant is the gate, not the physical. Held common K-12.
- **Officials assigning as definitional** — rejected: absent from FinalForms and JumpForward. Held common/optional.
- **State-association deployment as definitional** — rejected: FinalForms and JumpForward are institution-purchased. Held variant.
- **"Activities" (non-sports) scope as definitional** — rejected: marketing framing in two products; sports remain the center. Held variant.
- **Phone/app form factor, specific status vocabularies, specific expiration windows** — no cross-product evidence; not stated.

## Boundary Findings

- **vs Team Management Application** — team apps serve one team's roster/schedule/communication for coaches and parents; this Type's unit is the whole department's portfolio with a clearance/compliance loop. Remove the department scope and the governing-authority loop → Team Management.
- **vs Sports Registration Platform** — registration here is a capability feeding the participation gate inside a standing department system; a sports registration platform's unit is the signup event/program, without department memory or authority loop. Registration-first products (FinalForms) sit inside this Type because the registration output is the gate over the department's athletes.
- **vs Sports Eligibility Management** (directory sibling, unprocessed) — the eligibility gate is the defining core of THIS Type; a standalone eligibility product is this Type minus department operations. Overlap is severe; flagged for joint review in STATUS.md.
- **vs League Management Platform** — leagues own multi-organization competition structures (standings, cross-club scheduling); here the department is one institution's programs under a governing authority. League scheduling appears only as a coordination capability (League Scheduler push-to-schools).
- **vs Student Information System / School Management System** — the SIS owns enrollment/grades/attendance; this Type owns participation. SIS integration supplies academic-eligibility inputs (both directions documented: FinalForms SIS sync; DragonFly 3rd-party academic data).
- **vs Referee Management Platform** — officials assigning appears as a module (Arbiter One; DragonFly officials side); the standalone Type centers on officials' own careers/associations. Shared substrate: the same products serve both markets.
- **vs Sports Facility Management** — facility *scheduling/requests* is a module; facility operations/maintenance is the other Type.
- **vs Event Ticketing Platform** — ticketing is partner-integrated (GoFan, HomeTown links), not owned.
- **vs Athlete Management System** (already documented) — AMS manages athlete *preparation* (programming, readiness, medical availability); this Type manages the department's *administration* (eligibility, compliance, event operations). The existing AMS doc already records this seam ("administrative department operations... often sold as separate products").
- **vs Youth Sports Management** — youth-sports systems serve community/club leagues; this Type serves school-affiliated interscholastic/intercollegiate programs under educational authorities, with student-data privacy posture (FERPA-type) and academic coupling.

**"Remove what to become the other Type" judgments:**
- Remove the department portfolio + authority loop, keep one team → Team Management Application.
- Remove the department portfolio + authority loop, keep signup events → Sports Registration Platform.
- Remove the participation gate → generic department admin/scheduling tool (or SIS module).
- Remove the governing-authority loop → private club/team management.
- Remove the school/college institutional context (parent organization, students, educational governance) → League/Club management territory.

## Historical / Market-Sample Check

- Paper-era athletic department: AD with paper eligibility sheets, physical cards, schedule books, state-association forms — satisfies all three L0 structures with no modern machinery (portfolio = the season's sports; gate = eligibility sheet/physical card; authority = state association rules). Passes.
- Regional: the sampled market is US-shaped (state associations, NCAA). The abstract core (institutional department + participation gate + governing authority) also describes non-US school/college sport governance (national/provincial school sport bodies), but no non-US product was sampled — recorded as a limitation, not a boundary failure.
- Platform-native/older software generations (desktop athletic-department schedulers with eligibility tracking) satisfy the core without websites, payments, or officials modules. Passes.

## Uncertainties

1. Help-center-level operational detail (exact workflow steps, status vocabularies, role permission matrices) was not fetched; the model is built from official product/marketing pages (Tier 1–2). Assertion strength kept at "commonly/typically" for anything below the four products' explicit statements.
2. Bound (rSchoolToday) unreachable — the "department hub" pole is covered by Arbiter instead; rSchoolToday's own structure unverified this pass.
3. BigTeams independence — now Arbiter-branded; treated as same-family, not a sample.
4. College-pole scheduling/facilities operations (game management, travel) exist in the college market but were not evidenced on JumpForward's fetched pages; not claimed.
5. Whether "Sports Eligibility Management" (unprocessed sibling) will be documented as a separate Type or folded here — flagged for joint review.
6. Non-US school-athletics software not sampled.

## Final Synthesis

School / College Athletics Management is the athletics department's administrative system of record. Its defining core is three jointly-held structures: (1) the department's program portfolio — sports/teams by level and season with their coaching staffs and student-athletes — as the persistent unit of record; (2) the participation gate — per-athlete clearance/eligibility state (registration requirements, medical clearance, acknowledgments, academic standing, association rules) that determines who may practice and compete, tracked in real time and visible to staff before activity; (3) the governing-authority loop — the department enforces rules set above it (district, state association, collegiate body) and reports its standing back with audit-ready records. Around this core, mature products add registration self-service, contest scheduling, facilities, officials and payments, communication, public surfaces, medical/injury machinery, and reporting. The K-12 pole weights toward clearance and event operations; the college pole weights toward governing-body compliance and recruiting; both remain the same Type because the portfolio + gate + authority loop is intact in both.
