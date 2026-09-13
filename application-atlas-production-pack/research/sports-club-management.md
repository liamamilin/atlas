# Research Notes — Sports Club Management

## Research Goal

Understand what a "sports club management" application really is by studying how real products serve sports clubs — the member organizations that field teams — and where the boundary lies against the many sibling leaves in §28 (academies, youth sports organizations, leagues, team apps, facility/court products, generic membership systems).

This pass must discharge a pre-hung flag from the sports-academy-management pass (2026-09-09): "vs sports-club-management and youth-sports-management — heavy market overlap (TeamSnap ONE self-labels 'club & league management'; many soccer clubs call themselves academies; Jersey Watch's 'who we serve' spans both), proposed discriminator = center of gravity (program/tuition-led vs membership/competition-led vs registration/season-led), joint review recommended at those passes."

## Initial Boundary

Initial hypothesis before research:

- A sports club is a member organization that fields teams (or individual competitors) in sport: members join (commonly paying dues), the club organizes teams/programs over a season cycle, communicates with members, and collects money.
- The management software is the club's operator-side system of record: member records, teams/rosters, season/registration cycle, money (dues/fees), communication.
- Nearest neighbors: Sports Academy Management, Youth Sports Management, League Management Platform, Team Management Application, Membership Management System (§25), Sports Registration Platform, Sports Facility Management, Sports Court Booking, Racquet Club Management, Golf Course Management, Recreation Center Management, Gymnastics Club Management, Sports Federation Management, Sports Membership / Licensing Platform.
- Known prior seams to respect:
  - league-management-platform (processed): club = "runs a club's internal operations (members, teams, facilities); a league platform runs a competition between sides that the club may only partly control."
  - racquet-club-management (processed): "Sports Club Management | membership-organization-first for any sport (teams, seasons, registration); the court-time capacity model is not its center."
  - golf-course-management (processed): same pattern — "membership-organization-first (any sport); the golf course capacity model is not its center."
  - recreation-center-management (processed): facility + entitlement-validated-at-entry + programmed schedule is that Type's core; a club needs no facility.
  - membership-management-system (§25, processed): member registry + membership record + renewal/dues cycle + org-operated system with self-service — the generic organization version; the sports club's teams/season layer is what this leaf must add.

## Research Questions

1. What is the population of record — members? players? families? How are minors/guardians handled?
2. What are the club's organizing units — teams, squads, groups? How do rosters, coaches, and delegated management work?
3. How does the season/registration cycle work — registration forms, membership types, renewal, season rollover, archiving?
4. How does money work — dues, registration fees, match/training fees, payment requests, instalments, offline payments, arrears?
5. How does communication work — club-wide vs team-level; is it definitional or common?
6. Where does competition sit — do club systems run competitions, import league schedules, or hold results/stats?
7. Where does the facility sit — core or optional module?
8. What governance machinery exists — roles, permissions, committee/volunteer structures, safeguarding/vetting?
9. Where does the governing-body/federation relationship sit (affiliation, member sync)?
10. Where are the seams vs each sibling leaf, especially the academy/youth-sports discriminator?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

| Product | Pole | Tier / Market | Why selected |
|---|---|---|---|
| **TeamSnap ONE (TeamSnap for Business / for Clubs & Leagues)** | US youth sports club & league all-in-one platform | established youth clubs and leagues (US) | The market's biggest consumer brand moving up into club management; self-labels "club & league management" — the exact overlap the academy pass flagged; deep Tier-1 help center (Admin Playbook) |
| **SportEasy Club** | European amateur club management (club + team app) | volunteer-run amateur clubs (FR/EU, multi-sport) | The European amateur pole; explicit club-vs-team product split inside one vendor; member database + teams/groups + collections + sponsors |
| **Spond Club** | communication-first free platform with a club admin layer | grassroots volunteer clubs (UK/Nordics/EU) | The free/volunteer pole; separate Spond App (teams) vs Spond Club (admins) architecture; rich Tier-1 help center incl. federation integration (NIF) |
| **Thrive4Grassroots (formerly LoveAdmin)** | UK grassroots club admin + enablement | volunteer-led grassroots clubs (football, rugby, cricket, multi-sport) | The UK club-admin pole; vendor itself splits grassroots clubs (Thrive4Grassroots) from children's activity providers/academies (Thrive4Activities) — vendor-side boundary evidence |

Attempted but unreachable (recorded as sourcing limitations):

- **PlayMetrics** ("Youth soccer's first all-in-one club management app") — site is JS-rendered; fetch returned no content again this pass (third failure across passes). The competitive/elite club pole is therefore covered only indirectly (TeamSnap program attributes name competition levels "Division I, AAA, Silver, Varsity"; TeamSnap's own example program structures include "Academy").
- **Heja** (team-communication-first) not sampled; its posture is closer to Team Management Application territory and is used only as market context.

## Sources

- TeamSnap — product site https://www.teamsnap.com/ ; TeamSnap ONE page https://www.teamsnap.com/one ; Help Center https://helpme.teamsnap.com/ ; Admin Playbook https://teamsnap-admin-playbook.helpscoutdocs.com/ (fetched 2026-09-09: help home, Clubs & Leagues category, Season Management & Organization Structuring category, Invoicing/Registration/Financials category, "Setting up your organization structure", "Program structure setup guide")
- SportEasy — club home https://www.sporteasy.net/en/clubs/ ; club features https://www.sporteasy.net/en/clubs/features/ ; main site https://www.sporteasy.net/en/ ; Help Centre https://sporteasy.zendesk.com/hc/en-gb (fetched 2026-09-09)
- Spond — main site https://www.spond.com/ ; Spond Club overview https://www.spond.com/spond-club-overview/ ; club management https://www.spond.com/club-management/ ; Spond Club Help Centre https://help.spond.com/club/en/ incl. Members collection (193627), Finance collection (193632), "Renewal of Membership in Spond Club" (162557), "Payments in Spond Club" (177554) (fetched 2026-09-09)
- Thrive4 — network site https://thrive4.com/ ; Thrive4Grassroots https://thrive4grassroots.com/ (fetched 2026-09-09); legacy LoveAdmin app login https://app.loveadmin.com/ (linked, not fetched)
- PlayMetrics — https://www.playmetrics.com/ (JS-rendered, no content; abandoned per network rule)

Evidence layers used below: **A** = directly observed on the cited product's official pages; **B** = cross-product commonality across the sampled products; **C** = canonical inference from comparison and boundary reasoning.

## Product Observations

### TeamSnap ONE / TeamSnap for Business (Layers A + Tier-1 help)

Positioning (Layer A, product page): "The new standard in club & league management… From registration to live streaming, TeamSnap ONE has every tool you need to run and grow your organization in ONE powerful platform." Audiences split: "For Clubs & Leagues" (business product) vs "For Coaches & Parents" (team app). Feature list: Registration & Payments; Rostering; Organization-Wide Communications; Scheduling; Practice Plans & Drills; Coaching & Player Development; Parent Mobile App; Live Streaming; Website Builder; Financials & Reporting; plus Tournaments ("smart brackets, live scoring and automated updates") and Websites as separate lines. Narrative: "Registrations made simple — fast, flexible, mobile-friendly sign-ups with integrated payments and automated reminders"; "Organized from day one — easy roster-building and schedules… from org-wide alerts to team chats"; "Families stay connected — every schedule, message, live stream and highlight in one app… coming back season after season."

Organization structure (Tier 1, "Program structure setup guide"): "organizations are structured using programs. Programs contain seasons, and seasons contain a single layer of divisions. Divisions contain teams, which contain participants." Definitions given: Program = "the organized grouping of activities for categorizing services to athletes"; Season = "the portion of the year in which the program is active"; Division = "a number of teams grouped together by a common attribute(s)"; Team = "a group of participants working together to score points, reach a goal, and have fun." Program attributes: descriptive (sport, areas of operation) vs structural (Age Divisions "U16, Grade 6-8, 12 & Under, 14U"; Competition Genders "Male, Female"; Competition Levels "Division I, AAA, Silver, Varsity, Major"). Operational notes from the same article: registration is at the season level ("allowing you to focus forms on the needs of that specific program"); forms can be duplicated within a season and copied to the next season; schedules are set up at the season level; bank accounts attach per season and drive financial reporting; staff roles & permissions "utilize the program structure"; example program structures include "Recreation / Competitive / Camps & Clinics" and "Academy / Camps and Clinics / Eastern Recreational / Western Recreational".

Organization setup (Tier 1, "Setting up your organization structure… for Clubs and Leagues"): plan divisions before teams ("Divisions cannot be created if teams are created first"); group by age/sport/level/season with subdivisions; overlapping seasons supported (structure divisions as seasons to archive each as it ends); full-league vs division archive; team transfers into the organization account; reorganization via new team + roster import + delete.

Registration & financials (Tier 1, category inventory, 82 articles): creating a registration form; add fees and advanced fee adjustments; select payment methods and automatic adjustments; add documents and waivers; customize form fields; installment plans (edit; parents update payment info); org-issued invoices; managing invoices; submitting invoice payments; issue refunds; registration discounts; multi-child registration discounts (Clubs & Leagues category); capacity limits and waitlists; delete/cancel a registration entry; recording cash/check/offline payments; handling payment disputes; merchant account guide.

Rostering & scheduling (Tier 1, category titles): drag-and-drop rostering on the Rostering tab; scheduling for teams; importing organization schedules; importing team schedules; organization calendar; archiving a season / a team season; accessing archived or retired seasons; copy a program season; setting up divisions; team transfers; show/hide teams; removing a team.

Other categories: Roster Profile & Member Management (62 articles); Communication (27); Scheduling and Availability; Tracking and Statistics (6); Reporting (8); Partnerships & Integrations (19); Health & Safety (2); Security & Privacy (5).

### SportEasy Club (Layer A, product/feature pages + help-center structure)

Positioning: "The n°1 app for sports club management, helping your managers, coaches, volunteers and players spend more time on the field and less time in the office." Context claim: amateur clubs "require a lot of management time… with an average of 3 800 volunteer hours per year per club" (vendor-claimed; kept here only). Scale claims: 20,000 active clubs; 4.5M users (vendor-claimed).

Club features (club home + features pages):

- **Member management** — "No more Excel files!": import the whole roster, update members/parents/volunteers, attach files to profiles, export at any time, GDPR compliance.
- **Team and group management** — "Create and manage as many teams and groups as you want. Youth teams, adults, volunteer groups, board members: everyone has a role to play"; "Delegate the management of each group while supervising them"; "Easily transfer your members from one group to another."
- **Club messaging** — newsletters to all members, communicate with any group or member, share files (photos, videos, PDF); "the only way of communication for the entire club."
- **Shared calendar** — "all the club's events… from the end-of-year party to the weekly practices of the youth teams"; events created by each team (games, tournaments, practices), by each group (board meeting), or by the club; filter by type/group; view day/week/month/season.
- **Registrations, memberships and fee collections** — "create any type of payment collection (membership fees, game fees, etc.)… collect your members payments online or track offline ones"; "Allow new members to register to your club"; unlimited collections.
- **Sponsor management** — sponsor banners in the web/mobile app (up to 15), campaign results per sponsor (subscription option).
- **"CRM for amateur sports clubs"** — "structure the work of your management teams and guarantee the consistency of the methods used within your association."
- Roles named in marketing: technical directors, treasurers, secretaries, coaches.
- Testimonial evidence (Layer A): a club general secretary: "Before SportEasy, we had to track all of our members payments on Excel spreadsheets… Fee collections on SportEasy take a huge weight off our shoulders."
- The club product embeds the team product: "SportEasy is also the #1 team management app: coaches save time, players love it and parents are reassured"; team features include event invitations/reminders, availability, lineups, stats, messaging.
- Help center (Tier 1 structure): "Create and manage your seasons"; "Collecting payments for club teams: membership, summer camp, equipment…"; "Add/invite members to join your CLUB"; creating events; polls.

### Spond Club (Layers A + Tier-1 help)

Positioning: "Spond is a free app and club management solution… no matter the activity or sport." Two-product architecture (FAQ, Layer A): "The Spond app (for groups and teams) & Spond Club: A complete & free membership management system, including communication & payment. The Spond app would be used by group admin (coaches, team managers etc.), guardians and members while Spond Club is used by the club admins." Scale claim: 12M+ users (vendor-claimed).

Spond Club overview (Layer A): "Spond Club allows admins with multiple groups and teams to manage their entire club from a simple and intuitive web-based interface." Setup sequence: settings (grant permissions for club and group admins; "create member types and fields so you can choose how to organize and keep track of your members"); import groups and/or members (existing Spond groups, or Excel template); create a signup form for new members (embeddable on the club webpage); add club admins ("different club roles, with different permissions"); set up club accounts ("add as many club accounts as you want… say how often your payouts should happen… add your groups/teams accounts… say that group admins are only allowed to use these accounts"); set up payment requests (discounts, individual customisations, split payments); create course registration ("product variations… pay upfront or have a monthly subscription… refund and cancel a registration"); set up a website; set up a fundraising campaign.

Help center structure (Tier 1): Members (16 articles: "Sign-ups, active, pending, and deactivated members"); Departments and Groups (5); Finance (22: "Payment, settlement report, invoice"); Club registration forms (4); Booking Forms ("Courses and academies forms/Forms for camps & clinics", 5); Fundraising (3); Messages (2); Events (4: "Create and manage club events and get an overview of app events"); Club Website (18); Spond Discover ("Make the club and its activities visible", 3); Settings (14: "General club settings, member fields, club accounts, group roles, security"); **NIF Integration (🇳🇴 only)** (12: "Integration, branches, reporting, member synchronisation"); GDPR/Privacy (5).

Members collection (Tier 1): member sections — Active members / Unprocessed / Sign-ups / Deactivated; articles: Add and Import New Member; **Renewal of Membership in Spond Club**; merge members / duplicates; Managing Member Information; Filtering and Columns; **Payment Contact in Spond Club**; Police Certificate 🇳🇴 (vetting); remove a guardian from a member; Norwegian sports clubs can integrate with NIF.

Renewal of Membership (Tier 1, article body): "The feature sends a personalised link to existing members with pre-filled information. This allows members to quickly re-register without having to enter the same details multiple times… ensures that members' information is kept up to date, including consent to the club's terms and photo permissions." Mechanics: recipients selectable (members and guardians / members only / guardians only / member's payment contact); link validity duration selectable (1 day → 6 months); the member's current membership type must be available as an option in the form for the renewal to link to the existing profile ("Member 2025" vs "Member 2026" example); invitation statuses Sent → Signed up (automatic approval, or admin approves/declines under Members → Sign-ups) / Expired; admin actions: approve, **approve after payment**, or decline; renewal links are personal (siblings cannot share); using the standard registration form instead of the personal link creates a duplicate registration.

Payments in Spond Club (Tier 1, article body): "Create payment requests for membership fees, match fees, equipment, trips, annual memberships, and new uniforms"; descriptions, due dates, mandatory or optional; fixed amount or multiple options with varying prices and quantities; payment methods: single payment, instalments, or flexible (member chooses full upfront or instalments); manual invoices; registration forms with waiting lists linked to payment requests; sign-up forms with payment as single payment or subscription; monitor incoming payments in real time; reminders for outstanding payments; reports on payment requests, settlements, outstanding payments; club bank accounts linked (app group payments visible in Club); payments via Stripe (payment partner).

Finance collection structure (Tier 1): Payment request (9 articles); Subscription Payments for Payment Requests "Such as Training Fees, Seasonal Memberships, etc."; Payments; Settlement reports; Generate Invoice; Finance settings; App-side payments view/export.

### Thrive4Grassroots, formerly LoveAdmin (Layer A)

Positioning: "Thrive4Grassroots supports volunteer-led sports clubs where more members, more activity and higher expectations are putting extra pressure on the people running them." Who they help: football clubs ("Managing teams, registrations, volunteers, fixtures and communication across the season"), rugby clubs ("Supporting members, facilities and volunteers"), cricket clubs ("Balancing fixtures, facilities, communication and community involvement across the season"), multi-sport and community clubs ("Keeping memberships, communication and operations organised across multiple activities and programmes").

Software core (Layer A): "Most grassroots clubs start by looking for club management software to help with registrations and payments. That reduces admin and makes day-to-day tasks easier to manage." "We've spent more than 15 years helping clubs manage registrations, payments and communication" (as LoveAdmin, since 2011; rebrand confirmed on-site: "LoveAdmin is now Thrive4").

Vendor-side Type boundary (Layer A): "Looking for Sports Academy or Swim support? If you run a sports academy or swim school then head over to **Thrive4Activities**, the brand set up to support how children's activity providers are run." — the same company sells to grassroots clubs and to children's activity providers/academies under different brands, corroborating the club-vs-academy seam from the vendor side.

Beyond-software layer (positioning, not product structure): "enablement" plans, ThriveHub courses, Fund Finder (grants), customer stories (clubs with 500+ members, ~1,000 players, 350+ players).

## Cross-product Comparison

| Structure | TeamSnap ONE | SportEasy Club | Spond Club | Thrive4Grassroots | Strength |
|---|---|---|---|---|---|
| Member population of record (persistent, identified; guardians for youth) | Roster Profile & Member Management (62 help articles); parent app; member registrations | Member database ("no more Excel"); members/parents/volunteers; import/export | Members collection with states (active/unprocessed/sign-ups/deactivated); guardians; payment contact; member fields | "memberships… organised"; registrations for members | **B — all four** |
| Teams/squads as organizing units with rosters + delegated management | Program > Season > Division > Team > Participants; drag-and-drop rostering; team transfers | Unlimited teams & groups; "delegate the management of each group while supervising" | Departments and Groups; group admins with scoped permissions; Spond App for teams | "Managing teams… across the season" | **B — all four** |
| Season/registration cycle (register/renew into the season; rollover; club persists) | Program seasons: set up, copy, archive, overlapping seasons; registration at season level | "Create and manage your seasons"; shared calendar per season | Membership renewal via personalised links; membership types per year ("Member 2025/2026"); registration forms | "across the season"; registrations and payments as the core | **B — all four** |
| Member money loop (dues/fees → requests/collections → settlement → arrears) | Registration fees, installments, discounts, invoices, refunds, offline payments, disputes | Fee collections (membership fees, game fees); online or tracked offline | Payment requests (membership, match fees, kit, trips); instalments; reminders; approve-after-payment; Stripe | "registrations and payments" as the software core | **B — all four** |
| Communication (club-wide + team-level) | Org-wide alerts + team chats; parent app | Newsletters + group/member messaging; "the only way of communication for the entire club" | Messages collection; Spond App messaging with guardian oversight | "communication" named in every club type | **B — all four (common, loud)** |
| Scheduling (team events; club calendar; league-schedule import) | Scheduling for teams; import organization/team schedules; organization calendar | Shared calendar (team events, group events, club events) | Events (club events + overview of app events) | "fixtures… across the season" | **B — all four (common)** |
| Registration-form machinery (fields, waivers/documents, discounts, capacity, waitlists, approval) | Forms, fees, documents/waivers, discounts, capacity/waitlists, installment plans | Registration to the club; collections linked | Club registration forms; auto vs admin approval; waitlists; approve-after-payment | registrations (depth not documented at this tier) | **B — 3 of 4 at Tier-1/A depth** |
| Roles & delegated administration | Staff roles & permissions tied to program structure | Delegate group management; named officer roles (treasurer, secretary) | Club roles with permissions; club vs group admins | volunteer-led operations | **B — all four (common)** |
| Website / public presence | Website Builder (separate line) | (not sampled as feature) | Club Website (18 help articles); Spond Discover | (marketing-site level) | **B — common, optional depth** |
| Fundraising / sponsorship | Sponsorships (separate line) | Sponsor banners + campaign results | Fundraising campaigns (club + group) | Fund Finder (grants) | **B — common in volunteer economy** |
| Safeguarding / vetting | Health & Safety (2 articles) | (not observed) | Police Certificate 🇳🇴; GDPR guardian oversight | (not observed) | **A — product-specific realization, common concern** |
| Governing-body/federation sync | Partnerships & Integrations (19 articles, content unverified) | (not observed) | NIF Integration (Norway): branches, reporting, member synchronisation | (not observed) | **A — one product; regional variant** |
| Competition machinery (fixtures generation, results, standings) | Tournaments as separate product line; league schedules imported, not generated | Team stats/lineups (team-level) | (not observed) | "fixtures" as managed items, not generated competition | **Absent as center — import/consume, not run** |
| Facility/court/field booking | (not marketed as core) | (not observed) | (not in club feature list) | "facilities" named for rugby/cricket clubs (depth undocumented) | **Optional/variant at best** |
| Courses/camps/academies as club offerings | Program example "Camps & Clinics"; "Academy" as a program name | Summer-camp collections (help title) | Booking Forms: "Courses and academies forms/Forms for camps & clinics"; pay upfront or subscription | Thrive4Activities as separate brand | **B — common optional offering** |

## Canonical Model

### L0 — Defining Invariant (jointly held; deliberately small)

1. **The club's member population of record** — persistent identified people belonging to the club, held with their membership standing (member types/categories, lifecycle states such as pending/active/deactivated, renewal history); youth clubs hold children linked to guardians, with a designated payment contact. Remove → a contact/CRM database.
2. **Teams/squads as the club's organizing units** — the club fields teams (age-grade, adult, veteran squads; in some products also non-playing groups such as boards and volunteer crews) with rosters drawn from the membership, coaches/managers assigned, and day-to-day management delegated to team-level admins under club oversight. Remove → a generic membership management system.
3. **The season/registration cycle** — the club's year is structured as recurring seasons/registration periods: members register or renew into the season's teams and programs (registration forms, membership types, renewal links), rosters are (re)built each cycle, seasons are archived/copied, and the club and its member records persist across cycles. Remove → a static member registry with team lists.
4. **The member money loop** — the club's recurring money relationship with its members: membership dues, registration fees, match/training fees, kit and trip charges raised as payment requests/collections against members (or their guardian payment contacts) and settled by payment (online, instalments, or recorded offline), with outstanding payments tracked and actionable (reminders, approve-after-payment). Remove → a roster/communication app; the club stops being run as an organization in the system.

Jointly-held is load-bearing: 1 alone = membership management system; 2 alone = team management application; 3 alone = registration platform; 4 alone = a collections tool; 1+2 without 3+4 = member directory with team lists; 1+3 without 2 = generic membership org with renewal cycles; 2+3 without 1 = season tooling with no club memory; 1+4 without 2 = dues collection for a member org; 2+4 without 1 = team-level payments.

### L1 — Common Mature Structure

- registration-form machinery (custom fields, waivers/documents, discounts incl. multi-child/family, capacity limits, waitlists, approval modes: automatic vs admin review, payment at registration)
- communication (club-wide announcements/newsletters + team-level messaging + notifications; the market's loudest capability)
- scheduling (team events — practices, games; a shared club calendar; import of league/competition schedules the club does not generate)
- member/guardian self-service (mobile app/portal; availability/RSVP)
- roles and delegated administration (club admins vs group/team admins with scoped permissions; officer roles such as treasurer/secretary)
- season rollover tooling (copy season, archive, renewal links)
- reporting (membership, payments, participation)
- website / public presence
- fundraising and sponsorship (the volunteer-club economy)
- safeguarding/vetting machinery for coaches and volunteers (background checks; police certificate in one national realization)

### L2 — Variant / Optional Structure

- governing-body/federation integration (member synchronisation, branch reporting — documented in one national realization; regional variant)
- facility/court/field booking for clubs that own grounds (optional module; not observed as a club-product center)
- tournaments/events as separate product lines or program types
- courses/camps/academies run by the club (booking forms; upfront or subscription payment)
- live streaming, practice-plan content libraries (era-current extras in one product)
- multi-sport vs single-sport; youth vs adult; volunteer-run vs professionally run
- payment rails and merchant arrangements (payment-partner dependency in one product; merchant accounts in another)

### L3 — Vendor-specific (research notes only)

- TeamSnap: Program > Season > Division > Team > Participant hierarchy; program attributes (structural: age divisions, competition genders, competition levels; descriptive: sport, areas of operation); divisions cannot be created if teams exist first; recommendation not to exceed 30 divisions per season; bank account per season driving financial reporting; Falcon live-streaming camera; practice plans from pro-league partners; Tournaments as a separate product.
- Spond: member states (Active / Unprocessed / Sign-ups / Deactivated); renewal-link mechanics (personal link, membership-type matching requirement, validity durations 1 day–6 months, approve / approve-after-payment / decline); NIF integration (Norway); Police Certificate (Norway); Spond Discover; Stripe as payment partner; club accounts with payout frequency and group-admin account restrictions; "complete & free membership management system" self-description.
- SportEasy: sponsor banners (up to 15) with per-sponsor campaign results; "CRM for amateur sports clubs" framing; vendor-claimed figures (20,000 clubs; 4.5M users; 3,800 volunteer hours/club/year).
- Thrive4: enablement plans, ThriveHub courses, Fund Finder; LoveAdmin→Thrive4 rebrand; Thrive4Grassroots vs Thrive4Activities brand split.

## Vendor-specific Findings

See L3 above. None of these are promoted to the canonical model. The TeamSnap program-structure hierarchy is the clearest example of a vendor-specific realization of the more abstract "teams organized under season/program containers" structure; Spond's member-state vocabulary and renewal-link mechanics are one realization of member lifecycle + renewal; SportEasy's sponsor machinery is one realization of the volunteer-club funding layer.

## Boundary Findings

**vs Sports Academy Management (processed) — DISCHARGES that pass's pre-hung flag.** Keep-both RATIFIED on the center-of-gravity seam that pass proposed. Academy = training/development business: the offer is a program portfolio (classes, lessons, camps, clinics), athletes enroll to be trained, tuition is program-driven, family accounts are payer relationships. Club = member organization: people belong (membership standing, renewal), the club fields teams that compete in competitions run by others, money is member-driven (dues, registration, team fees). Market overlap is real and documented from the vendor side: TeamSnap ONE self-labels "club & league management" while its own program-structure examples include "Academy" as a program name; Thrive4 (one company) sells to grassroots clubs via Thrive4Grassroots and to sports academies/swim schools via Thrive4Activities — the vendor's own brand split matches the Type split. Many organizations are both (a soccer club with an academy arm); products are sold into both labels. Directional test: strip the program/tuition portfolio and the training-delivery machinery → what remains (members, teams, seasons, dues) is this Type; strip the member organization and field only programs for enrolled athletes → academy territory.

**vs Youth Sports Management (unprocessed) — flag left for that pass.** Proposed discriminator (extending the academy pass's center-of-gravity scheme): youth sports organizations are registration/season-led — the season's registration is the center (rec leagues, volunteer boards, one-shot program seasons); clubs are membership/competition-led — the standing member organization fielding teams is the center. The same products serve both (TeamSnap serves both explicitly). Joint review recommended at that pass.

**vs League Management Platform (processed) — ratified from this side.** The league platform runs a competition between sides (fixtures, results, computed standings) for an organizing body; the club system runs one organization's internal operations (members, teams, money). The club's teams play in leagues run elsewhere: club products import league schedules (TeamSnap "Importing organization schedules" / "Importing team schedules") rather than generating competition, and hold competition machinery only as separate product lines (TeamSnap Tournaments) or light team-level stats (SportEasy). Consistent with the league pass's own boundary row.

**vs Team Management Application (unprocessed) — flag left for that pass.** The team app centers on ONE team's life (roster, availability, schedule, communication); the club system runs the organization's many teams plus the member organization and its money. The club product embeds team management as a delegated module (SportEasy: "SportEasy is also the #1 team management app"; Spond: app for groups/teams used by coaches, Club used by club admins). Directional test: one team with no club container → team app; many teams under a member organization with dues → this Type.

**vs Membership Management System (§25, processed) — held.** Generic MMS = member registry + membership record + renewal/dues cycle + org-operated self-service for any organization; this Type = that member organization PLUS teams/squads and the season/competition-participation layer. Boundary evidence: sports clubs can and do run on generic membership software (Wild Apricot-class, per the MMS pass's own club-label observation) — which shows membership alone is not the club's center; what MMS lacks is exactly legs 2–3. Keep-both.

**vs Racquet Club Management / Golf Course Management (processed) — ratified.** Those Types center on playing-capacity inventory (court-time inventory; tee sheet) with bookings as the booking of record; this Type centers on the member organization. Facility/court booking appears here only as an optional module for clubs that own grounds. Consistent with both passes' boundary rows.

**vs Recreation Center Management (processed) — held.** Recreation center = operated facility (spaces + entitlement validated at entry + programmed schedule); the club needs no facility at all. The fitness-studio pass's related-types row ("Sports Club / Recreation Center Management | multi-sport, multi-program operations for clubs and municipalities") conflates the two labels; the structural seam is facility-at-the-center vs member-organization-at-the-center.

**vs Sports Facility Management / Sports Court Booking (unprocessed) — flags left.** Rentable-space inventory and demand-side booking vs the member organization; a club's facility bookings (where they exist) are one module inside this Type.

**vs Sports Federation Management (unprocessed) — flag left.** The federation governs many clubs (affiliations, sanctioning, licensing); the club is one member organization. The club↔federation data flow (Spond's NIF integration: member synchronisation, branch reporting) is an integration edge of this Type, not its center.

**vs Gymnastics Club Management (unprocessed) — flag left.** "Club" word collision: gymnastics clubs in the directory's class-management family are instruction businesses (the shared class-management spine); sports clubs here are member organizations. The Thrive4 vendor split (Grassroots vs Activities) is vendor-side corroboration that the market itself separates these audiences.

**vs Sports Registration Platform (unprocessed) — flag left.** One-shot registration transactions vs the ongoing club relationship (member standing, teams, seasons, recurring money); same seam as academy-vs-registration.

**Private-club word collision (no directory change).** "Club" also denotes country/golf clubs (private-club suites sampled under the golf and racquet passes). Those are amenity clubs; this leaf is the sport-participation club. No taxonomy conflict — the directory documents the amenity pole under its facility leaves.

## Uncertainties

- **Competitive/elite club pole undocumented.** PlayMetrics (the named US competitive soccer club OS) is JS-rendered and unreachable (three failures across passes). The elite/competitive club pole is covered only indirectly (TeamSnap program attributes name competition levels; TeamSnap example structures include "Academy"). Assertions about competitive-club-specific machinery (tryouts, player placement, carding/registration with governing bodies) are NOT made in the final document.
- **Facility-booking depth in club products** is under-evidenced (named for two club types in one product's marketing; absent from two others' feature lists) — held as optional/variant, not common.
- **Governing-body integration** is evidenced in one product (Spond/NIF, Norway); US/UK affiliation flows are market-known but not documented at Tier 1 this pass — held as regional variant.
- **Thrive4 product depth** is marketing-site level only (no help center fetched); its structures are used as corroborating evidence, not as operational ground truth.
- **SportEasy operational mechanics** (renewal, approval modes) are not documented at article level; its evidence is product/feature-page strength.

## Historical / Market-Sample Check

Paper-era sports club administration: the membership secretary's register (members, categories, subscriptions paid), the treasurer's dues ledger, team selection sheets posted each season, fixture lists received from the league and copied to the noticeboard, the club handbook, AGM minutes. This satisfies all four L0 legs with zero modern machinery: member population of record (register), teams (selection sheets), season/registration cycle (annual subscriptions + annual team formation), member money loop (dues ledger, arrears chased by the treasurer). Regional and platform-native realizations (Norwegian NIF-integrated clubs, UK county-affiliated football clubs, volunteer GAA clubs) fit without any of the modern extras. The definition therefore does not depend on mobile apps, websites, online payments, or communication tooling — offline payment recording is documented in-sample (TeamSnap records cash/check; SportEasy tracks offline payments).

## Final Synthesis

A Sports Club Management application is the club's operator-side system of record: it holds the club's member population (with membership standing and guardian links for youth), organizes that population into teams/squads with delegated day-to-day management, runs the club's recurring season/registration cycle (register/renew into each season's teams and programs, roll the structure forward, keep the club's memory across cycles), and carries the member money loop (dues, registration and team fees raised against members and settled, with arrears actionable). Around this core, mature products add registration-form machinery, club-wide and team-level communication, scheduling with league-schedule import, self-service apps, delegated roles, websites, fundraising/sponsorship, and safeguarding. Competition between sides is run elsewhere (league platforms) and consumed via schedule import; playing-capacity inventory is a different Type (racquet/golf/facility leaves); the training-program portfolio as the offer is the academy's center. The Type stands as a distinct leaf: the member organization fielding teams is a real, coherent center of gravity that no sibling leaf owns.
