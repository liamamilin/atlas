# Research Notes — Referee Management Platform

Research date: 2026-09-09
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand what a Referee Management Platform really is from real products: who runs it, what objects exist inside it, how officials get onto games, what rules constrain assignment, and where its boundary lies against League Management, Employee Scheduling, Volunteer Management, and Tournament Management.

## Initial Boundary

Initial hypothesis (before research):

- Core use: sports organizations (leagues, referee/officials associations, state associations, clubs, schools, tournaments) manage their pool of officials — registration, certification, availability, assigning to games, communication, payment, evaluation.
- Primary users: the **assignor** (the person who puts officials on games) and the **official** (referee/umpire who receives assignments).
- Nearest types: League Management Platform (bundled referee module), Employee Scheduling, Volunteer Management, Tournament Management, Sports Scheduling.
- Known prior context: the league-management-platform pass (2026-09-08) recorded "Referee Management (module depth)" as a held boundary — referee assigning appears as a module inside league platforms, and this pass must establish whether a dedicated Type exists and what its center is.

## Research Questions

1. Whose system of record is it — the assignor's organization, the league, or the official?
2. What is the unit of assignment (game? position? crew? duty)?
3. How does availability work, and who declares it?
4. How does assignment happen — assignor-driven, request-based, self-assign?
5. What gates eligibility — certification, age, conflicts, limits? Advisory or blocking?
6. What is the accept/decline/turnback loop and its states?
7. How is payment handled?
8. What interfaces do assignor and official each face?
9. Is evaluation/rating part of the Type?
10. Where exactly is the seam vs League Management Platform?

## Representative Products

| Product | Why sampled | Evidence tier reached |
|---|---|---|
| **assignr** | Dedicated assigning platform since 2009, "focused exclusively on the needs of assignors and officials"; deep Intercom help center reachable | Tier-1 (help-center articles, multiple) |
| **Arbiter (Arbiter One / Assigning)** | Enterprise leader for US assigning associations & K-12; 200,000+ officials claimed; suite context (Pay, Eligibility) | Tier-2 (product/marketing pages); help center timed out ×2 — abandoned per network rules |
| **OTTO SPORT (formerly Demosphere)** | League/club platform with a named "Referee Management" solution — the bundled-module pole | Tier-2 (product page) |
| **Stack Sports** | League-management pole; assigning documented via assignr's own comparison page (vendor-documented boundary evidence) | Tier-2 (indirect, via assignr comparison page + Stack root page) |

Attempted and abandoned (2 failures each, per network rules): HorizonWebRef (403 ×2), ZebraWeb (transport error ×2), Game Officials (transport error), RefTown (login-gated page), Stack Officials direct (403), Wayback for HorizonWebRef (timeout). Regional (non-US) sample not secured — recorded as a sourcing limitation.

## Sources

- assignr root: https://www.assignr.com/ (fetched 2026-09-09)
- assignr assigning page: https://www.assignr.com/assigning-referees-and-umpires/
- assignr help center home: https://support.assignr.com/
- assignr — How to Assign Officials to a Game: https://support.assignr.com/en/articles/8526477
- assignr — Groups and Rules: https://support.assignr.com/en/articles/8526490
- assignr — A Breakdown of Conflict Codes: https://support.assignr.com/en/articles/10149849
- assignr — How to Understand Officials' Availability: https://support.assignr.com/en/articles/8526476
- assignr — How to Enable Self-Assign: https://support.assignr.com/en/articles/8526494
- assignr — What to do after Officials Accept & Decline: https://support.assignr.com/en/articles/8526480
- assignr — Officials - Overview: https://support.assignr.com/en/articles/8526482
- assignr — U.S. Soccer Referee Certifications Integration: https://support.assignr.com/en/articles/8526561
- assignr — Assignr vs. Stack Officials: https://www.assignr.com/assignr-vs-stack-officials/
- assignr help center collections (officials: 24 articles; assignors & non-officials: 108 articles): https://support.assignr.com/en/collections/9689458, https://support.assignr.com/en/collections/9689465
- Arbiter root: https://arbitersports.com/ (fetched 2026-09-09)
- Arbiter Assigning product page: https://arbiter.io/products/assigning/
- OTTO SPORT root: https://www.ottosport.ai/ (fetched 2026-09-09; demosphere.com redirects here)
- OTTO SPORT Referee Management: https://www.ottosport.ai/referee-management
- Stack Sports root: https://stacksports.com/ (fetched 2026-09-09)

## Product A — assignr (Tier-1, deep)

### Key observations

**Positioning (Layer A).** "Referee Scheduling Software… Automate assignments, communication, and payments for leagues, associations, and assignors of all sizes." "Built specifically for assigning referees and umpires." Comparison page: "Assignr has been around since 2009, and we have always been focused exclusively on the needs of assignors and officials." Customers named: soccer leagues (MLS NEXT, Elite Academy League), state referee administrations (Arizona State Referee Administration, Colorado Soccer Association), umpire associations (Big Sky Blues Umpire Association), Little League, basketball events (Spokane Hoopfest), gridiron football.

**Official-side model (Layer A).** Officials Overview: "Assignr is a tool used by your organization to manage officiating assignments, communicate with you, and can also be used to pay you as well." Official uses: provide availability; accept or decline assigned games; view or request unassigned games; provide banking information for Direct Deposit; communicate with other officials or the assignor. "Your assignor will create an account for you" — the assignor provisions the official's account. Officials' help collection also covers: profile review, travel restrictions, assignment restrictions, game reports, registration, multiple-organization availability management, W9/bank account/payment status, video module.

**Availability (Layer A).** "Assignr expects that officials will provide their availability to you by indicating the days that they are available to work. The availability calendar defaults to NOT available." Assignors see availability conflicts inline during assignment (D conflict code). Officials manage availability across multiple organizations from one account.

**Assignment mechanics (Layer A).** Games page → Assign button per game → position dropdown (e.g., R, AR1, AR2, 4th official; timekeeper) → search official → conflict codes displayed as letters beside each name → Save → **Publish** (notification happens on publish, not on save). Reassignment notifies both new and previously assigned official. Bulk: Open All / Save All. Crew tools: Copy Assignments, Copy All, Copy One & Rotate, Copy All & Rotate (rotate positions across back-to-back games at same venue). While assigning, an official-detail panel shows tabs: Date (availability that day + other games that day), All Games (±2 weeks), Teams (history with the teams), Comments, US Soccer (certification, if integration on), Requests, Ratings, Groups & Rules, Conflicts.

**Conflict codes (Layer A).** 19 codes, each a reason not to assign: RQ (requested), ⇒ (assigned), A (ability — age-group abilities), B (birthdate — minimum age requirement), C (game counts — assignment limits per day/week/month), D (date — not marked available), E (working elsewhere), F (preferences), G (group — Groups & Rules), K (location — can only work specific site/venue), L (league conflict), O (conflict with other official), P (previously declined this game — system prevents re-assigning; override possible), R (ratings — rating requirement), S (not USSF certified), T (team conflict), U (unregistered — registration module), V (venue conflict), X (external — working elsewhere for another organization on the same platform), Z (zone/district).

**Advisory vs blocking (Layer A — key behavioral finding).** "Conflict codes are informative only and are not hard limits within the system. This means you can technically assign officials to games, regardless of any conflicts by their name." Exception: certification can be made blocking via a "Prevent Unlicensed Assignment" site setting ("If you try to save an assignment with a not-certified referee, the system will give you an error message"). The assignor is the human decision-maker; the machinery advises.

**Eligibility machinery (Layer A).** Groups & Rules: officials added to groups; groups carry **Required** rules (allow assignment to matching games) and **Restricted** rules (prevent assignment to matching games); OR logic within a group; G conflict code for violations. Example: a Timekeepers group with a Required rule "Position: Timekeeper" — only group members can be assigned to the Timekeeper position. Assignment limits configurable per official and site-wide (per day/week/month); "if they are not set, a single referee may assign themselves to all of your open games."

**Assignment authority spectrum (Layer A).** Three modes: (1) assignor assigns (default); (2) Game Requests — officials view available games and request to work one; assignor approves or denies; (3) Self-Assign — optional, disabled by default; "Request It" button auto-assigns if no conflicts; self-assign uses the same conflict machinery ("an official may not assign themselves to two different games at the same time, … a game or position that they are not qualified to work, … a game where the referee has a team, league or venue conflict"); for self-assign and requests, availability is ignored but other conflict codes are checked; eligible games and eligible officials can be restricted.

**Accept/decline loop (Layer A).** Publish → officials receive email asking to confirm. States observed: accepted (daily summary email to assignor), unconfirmed (daily reminder emails to the official; Games → Unconfirmed page), declined (immediate email to assignor; must reassign; Games → Declined page). Declined assignments may auto-remove or remain (site setting). System prevents re-assigning an official who previously declined (P code, override possible). Auto-decline automation exists ("Automated Auto-Decline" article). Decline notice window: "assignr.com ensures that a referee cannot decline a game within 36 hours of a game's start time. This time period can be adjusted" (product-specific default). Short-notice game-change decline behavior configurable.

**Payment (Layer A).** Game fees, pay scales, travel fees, assignor fees, admin fees configured in Maintenance. Direct Deposit for officials (W9 collection, bank account, payment status, Venmo option), 1099 generation; "no fees for officials to receive payments." Paying Hourly Staff collection exists (event staff). Payment follows assignment: "If an official has been assigned to a game, they will be paid for the game, regardless of whether the status of the assignment is accepted, declined, or unconfirmed" — unless game set to Canceled (no pay), official removed, or override fee zeroed.

**Certification integration (Layer A).** USSF integration pulls active certifications (referee, instructor, educator, assessor, assignor, emeritus, coaching); USSF pushes changes (upgrades, renewals, expired/revoked); officials get 60/30-day expiry reminders; assignors get daily summary (license changes for officials assigned in next 14 days) and weekly summary; expired/revoked notifications include the official's upcoming assignments "so that you can see if the referee needs to be removed from their existing game assignments." S conflict code; optional hard block. Certification report downloadable from People page.

**Other modules (Layer A).** Game reports (officials submit; administrator-configurable templates); rating system for officials; video module (share clips, "You Make The Call" survey); registration module (officials register/pay; U conflict code when registration unmet); e-signatures; messages (to groups, to officials on specific games); reports; API; integrations (LeagueApps, Game Officials export, OMS, REFSIX).

**Multi-organization (Layer A).** Officials manage availability across multiple organizations from one account; X conflict code shows when an official is working elsewhere for another organization using the same platform.

## Product B — Arbiter / Arbiter One (Tier-2)

### Key observations

**Positioning (Layer A, marketing).** "The Connected Platform for K-12 Sports and Activities." Products: Pay, Eligibility (coach and official eligibility), Student Registration, Assigning Solutions, Event and Game Scheduling, Arbiter360, Facilities Scheduler, Athletic Websites. Markets: **Assigning Associations**, K-12, Governing Bodies. "200,000+ Officials supported nationwide." 40+ years.

**Assigning product (Layer A, marketing).** "Assign officials quickly and accurately with Arbiter One. Manage availability, scheduling, and performance from a single dashboard. Match officials to games based on rules and availability. Notify officials instantly of new assignments. Track evaluations and performance feedback. Reduce conflicts with built-in eligibility checks." Product page: "Match officials to games based on skills, availability, and requirements… Automatically verify eligibility before assigning roles. Eliminate scheduling conflicts with advanced workflows. Balance assignments with **fair distribution tools**." "Keep assignments connected to event schedules in one place… Share updates with officials automatically." FAQ features: Central Hub (official requirements + assignments), Testing (rules knowledge checks and certifications), Eligibility (registration and compliance status), Clinics & Training, Video, Background Checks. Users: Assigners, Officials, Athletic Directors/Schools.

**Payment (Layer A, marketing + testimonial).** Arbiter Pay: "Pay officials, staff, and vendors… Payments for all 1099 workers… Integrated with schedules and assignments." Testimonial (state association): "With one click they can verify the official showed up for the game and transfer money from the school's account to the official's account." 1099 handling named. "Event workers" also paid through the platform.

**Eligibility (Layer A, marketing).** Separate "Coach and Official Eligibility" product; testimonial: "Running background checks and qualifying officials used to be a hassle… knowing my referees are fully eligible for games."

**Evidence limitation.** Help Center (Zendesk) timed out twice — abandoned. All Arbiter observations are from product/marketing pages; operational mechanics (exact states, defaults) not verified. Assertions kept at marketing-level strength.

## Product C — OTTO SPORT (formerly Demosphere) (Tier-2, bundled-module pole)

### Key observations

**Positioning (Layer A, marketing).** Youth-sports management suite: OTTO SPORT (club & league management), OTTO EVENT (tournaments/ticketing), University Athlete (recruiting). "Referee Management" is one named solution inside the suite — the bundled-module pole.

**Referee Management module (Layer A, marketing).** "Streamline the referee scheduling process… Complete control over your referee operations."
- Referee Registration & Import — "Register or import referees with collection of important information like payment and tax information."
- Availability & Preferences — "Referees set availability and preferences including field coverage maps."
- Drag-and-Drop Assignments — "Assign referees and officials to games with drag-and-drop cloning to maintain back-to-back game crews."
- Custom Post-Match Reports — "Customize the post-match report to collect all the info you need for each game. Track everything from game details to referee performance."
- Mobile App Access; Automated Push Notifications ("new assignments, reminders, and schedule changes"); Crew Communication ("Referees can view and contact other assigned crew members").

Same object set as dedicated platforms (registration/import, availability, assignment, crews, reports, notifications), delivered as a module of a club/league system.

## Product D — Stack Sports (league pole, indirect)

### Key observations

**Boundary evidence (Layer A — vendor-documented by a competitor).** assignr's comparison page: "Stack Sports is a wide-ranging league management platform that teams, players, and parents can benefit from, but assigning referees and umpires has never been their main use case." And: "league management platforms who also offer referee scheduling frequently don't understand how officials are actually assigned. They tend to be a bolt-on, 'yeah we do that too' kind solution that never really clicks with officials and assignors." Stack's own root page (fetched) describes league management, payments, recruiting, endurance, camps — no officials-assigning product surfaced at root. This is the clearest documented seam between League Management and Referee Management: the league platform owns the competition; the referee platform owns the officials workforce that covers it.

## Cross-product Comparison

| Aspect | assignr | Arbiter Assigning | OTTO Referee Management | Stack (league pole) |
|---|---|---|---|---|
| Who it's for | assignors/associations/leagues of all sizes | assigning associations, K-12 schools, governing bodies | clubs/leagues (module of suite) | league/club operations (assigning bolt-on) |
| Official roster | profiles with availability, restrictions, abilities, preferences, conflicts, groups, ratings, certs, financials | official requirements, eligibility, background checks, testing, clinics | referee registration & import incl. payment/tax info | — |
| Assignment target | game + named positions (R/AR/4th/timekeeper…) | officials to games | referees to games, crews | games (bolt-on) |
| Availability | official-declared calendar, default NOT available | availability tracking | referees set availability & preferences (field coverage maps) | — |
| Assignment modes | assignor / requests / self-assign (optional) | assignor, rule-matched | drag-and-drop with crew cloning | — |
| Eligibility machinery | 19 conflict codes; advisory by default, blocking optional | "built-in eligibility checks", "automatically verify eligibility" | — | — |
| Confirmation loop | publish → accept/decline/unconfirmed → reassign declined | notify officials instantly | push notifications for assignments/changes | — |
| Payment | game fees/pay scales/travel fees; direct deposit, W9, 1099 | Arbiter Pay tied to assignments; 1099 | payment & tax info collected | — |
| Evaluation | rating system, game reports, video | evaluations & performance feedback | post-match reports incl. referee performance | — |
| Multi-org officials | yes (multi-org availability, X external conflict) | — (unverified) | — | — |

**Stable across all sampled products (Layer B):** officials roster; games needing officials; assignment binding official→game-position; availability as an input; notification of assignments; accept/decline; reassignment of declined/unfilled; payment of game fees; communication.

**Present in some (Layer C candidates):** certification integration with a governing body (assignr-USSF; Arbiter eligibility/testing/clinics as suite modules); self-assign (assignr explicit; others unverified); rating systems (assignr, Arbiter, OTTO — different depths); multi-organization officials (assignr explicit); crew rotation tooling (assignr, OTTO).

## Canonical Model (L0/L1/L2/L3)

### L0 — Defining Invariant (three jointly-held structures)

1. **The official as managed record.** The system maintains persistent records of the people who officiate — identity/contact, officiating qualifications and status, restrictions. Remove → a generic calendar/scheduling tool with no workforce memory.
2. **The game as the assignment target.** Dated scheduled competition events, each needing officiating coverage in one or more defined positions/roles. Remove → contact directory / HR-style shift scheduling (Employee Scheduling territory).
3. **The assignment loop.** The recurring cycle: who is available/eligible informs who can take what → an assignment binds a specific official to a specific game position → the assignment is communicated to the official → the official confirms (accept) or releases it (decline) → declined/unfilled positions return for reassignment until the game is covered. Remove → static roster + schedule with no management; the "management" is gone.

Jointly-held load-bearing: (1) alone = contact list; (2) alone = game schedule; (3) without 1+2 = abstract workflow with no subjects; (1+2) without 3 = roster + fixture list, no loop; (1+3) without 2 = shift scheduling; (2+3) without 1 = anonymous staffing.

### L1 — Common Mature Structure

- Availability declaration by officials (calendar; default-unavailable pattern observed)
- Eligibility/conflict machinery: team/league/person/venue conflicts (neutrality), certification status, minimum age, assignment limits, registration status
- Assignment states: assigned → accepted / declined / unconfirmed; reminders; auto-decline; reassignment of declined
- Publish step gating official visibility/notification
- Communication: notifications, messages, reminders, acknowledgment
- Game fees / pay scales; payment processing (direct deposit, tax forms) or payment-data collection
- Game reports submitted by officials
- Mobile app for officials
- Crew/position structures and rotation across back-to-back games
- Ratings/evaluation of officials
- Multi-assignor collaboration within an organization

### L2 — Variant / Optional Structure

- Certification integration with a sport's governing body (e.g., USSF Learning Center sync) — sport/federation-specific
- Registration module (officials pay annual registration to the organization)
- Background checks / safe-sport clearances (child-safety jurisdictions)
- Testing/clinics/training content (suite-context products)
- Video review/mentoring modules
- Travel restrictions/fees; zone/district structures
- Assignment-authority spectrum position (assignor-driven ↔ request ↔ self-assign)
- Payment depth (in-product direct deposit + 1099 vs external payment)
- Officials shared across multiple organizations on one platform
- Non-referee game-day roles (timekeepers, scorekeepers, event workers) assigned through the same machinery

### L3 — Vendor-specific (research notes only)

- assignr's 19 lettered conflict codes; "Officials Without Conflicts" filter; Copy One & Rotate; 36-hour decline-window default; "Prevent Unlicensed Assignment" toggle; Request It button; daily/weekly license-change summaries (14-day window)
- Arbiter One / Arbiter Pay naming; fair distribution tools; Time Savings Calculator
- OTTO field coverage maps; drag-and-drop cloning
- assignr pricing shape (per-official plans, per-game plans; $240/yr Recreational up to 60 officials)

## Historical / Market-Sample Check (§24)

Paper-era assigning: the assignor keeps index cards per official (name, certification grade, phone, availability notes), a wall-chart game schedule, writes names into game slots, phones each official to confirm, replaces decliners by hand, keeps a fee ledger for the treasurer. This satisfies all three L0 legs with no software, no mobile apps, no direct deposit, no conflict-code letters, no self-assign. Older/regional products (Game Officials, ZebraWeb, RefTown — all unreachable this pass but known members of the same product population) fit the same shape. Therefore L0 must not include: mobile apps, direct deposit/1099, governing-body integrations, lettered conflict codes, self-assign, ratings. All confirmed as L1/L2.

## Vendor-specific Findings

See L3 above. Also: assignr's self-documentation of the league-platform seam (comparison page) is itself a market-structure datum — dedicated platforms position against league suites on depth of officials-workflow understanding.

## Boundary Findings

1. **vs League Management Platform.** The league platform is the competition's system of record (teams, fixtures, results, standings, registration of players). The referee platform is the officials workforce's system of record. Games enter a referee platform as data (assignr: bulk game import; "whether you manage the schedule yourself, or are provided the schedule from the league"). Test: remove officials-workforce management → league management; remove competition management → referee management. Bundling exists (OTTO module; Stack bolt-on) — assignr's own page documents the seam from the dedicated side. The league pass (2026-09-08) held "Referee Management (module depth)" — ratified from this side: module depth is real, and the dedicated Type's center is the assignment loop, not the competition.
2. **vs Employee Scheduling Platform.** Shifts vs games; the workforce is typically external/contracted (1099 pattern in both assignr and Arbiter) rather than employed; eligibility is sport-certification-based; neutrality conflicts (cannot officiate a team one belongs to) have no employee-scheduling analogue.
3. **vs Volunteer Management System.** Similar people-to-commitment shape, but officials are certified and commonly paid per game; volunteer systems center recruitment/sign-ups for general causes, not per-event qualified coverage of a competition calendar.
4. **vs Tournament Management Platform.** Tournament ops own brackets/scheduling/venues; officials coverage is one input, commonly handed off to a referee platform (assignr serves tournament events — Hoopfest — via the same game-assignment machinery).
5. **vs Sports Scheduling Platform.** Generates the game schedule; the referee platform consumes it and assigns people to it.
6. **vs Sports Federation Management.** Federation = umbrella governance over many organizations; certification originates there and flows into referee platforms (USSF integration pattern). A federation may run assigning for its officials — then it is using a referee platform as one of its functions.
7. **vs Team Management Application.** Team-centric (one team's roster/schedule/comms) vs officials-workforce-centric (many teams' games, one official pool).

## Uncertainties

- Regional (non-US) dedicated products could not be fetched (ZebraWeb, Game Officials, RefTown, HorizonWebRef all failed). The sample is US-centric; L0 was checked against the paper-era conceptual lineage instead of a live regional product. Risk: some L1 items (e.g., direct deposit/1099) are US-specific and were kept out of L0/L1-definitional positions accordingly (payment processing held as L1-common, not invariant).
- Arbiter's operational mechanics (exact assignment states, defaults) unverified — help center unreachable. Arbiter claims kept at marketing strength.
- Self-assign prevalence across the market unverified beyond assignr (explicit) — held as variant, not common structure.
- Whether "event workers" (non-officiated roles) are in-scope for the Type or a spillover: observed in assignr (hourly staff, timekeepers) and Arbiter (event workers) — held as L2 spillover, not definitional.
- Evaluation depth (ratings vs structured assessor/mentor programs) varies; only marketing-level evidence for Arbiter/OTTO.

## Final Synthesis

A Referee Management Platform is the officials-workforce system of record for sports organizations. Its defining core is three jointly-held structures: the managed official roster, the game schedule as assignment target, and the assignment loop (availability/eligibility → assignment → communication → confirmation → reassignment of declines) that ends with every game covered by qualified officials. Everything else — certification sync, payments, ratings, self-assign, mobile apps, multi-org sharing — is common mature or variant structure. The Type's sharpest seam is with League Management Platform: the league owns the competition; the referee platform owns the people who officiate it; bundling is common but the centers are distinct, and the market itself (dedicated platforms' positioning) documents the seam.
