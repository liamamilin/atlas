# Referee Management Platform

## Overview

A **Referee Management Platform** is the officials-workforce system of record for sports organizations. It maintains the roster of officials (referees, umpires, and related game-day roles), tracks the games that need officiating, and runs the assignment loop that ends with every game covered by a qualified, confirmed official.

The defining core is small:

```text
Official roster (people who officiate, with qualifications and status)
+ Game schedule (dated events needing officials in defined positions)
+ Assignment loop (availability/eligibility → assignment → notification
  → confirmation → reassignment of declines)
```

Everything else commonly associated with the category — certification syncing with a governing body, direct deposit of game fees, ratings and evaluations, self-service assignment, mobile apps — is widespread in current products but is not what makes the product a referee management platform. A paper-era assignor with index cards, a wall chart, and a telephone satisfies the same core.

The category sits beside — not inside — league management. A league platform owns the competition (teams, fixtures, results, standings); a referee management platform owns the people who officiate that competition. Many league platforms bundle a referee module, and dedicated platforms exist precisely because officials-assigning has its own workflow, its own rules, and its own users.

## Users & Context

**Primary users:**

- **Assignor** — the person responsible for putting officials on games. Works in the management surface: maintains the game list, checks availability and eligibility, makes or approves assignments, handles declines and late changes, and typically owns payment of game fees. The assignor may be a paid professional (a state or regional assigning authority), a club staff member, or a volunteer.
- **Official** — the referee, umpire, linesman, or similar game-day official. Uses the personal surface: declares availability, receives and confirms assignments, browses open games, submits game reports, and tracks payment.

**Secondary users:**

- **Organization administrator** — configures the site: age groups and fee structures, leagues, eligibility groups and rules, permissions, registration.
- **League or club administrator / athletic director** — consumes coverage visibility (which games are covered, which officials are assigned) without doing the assigning.
- **Evaluator / mentor** — in organizations that run assessment programs, records ratings or feedback against officials.

**Context.** The customer is an organization that must cover a competition calendar with a pool of qualified people it does not employ in the normal sense: leagues, referee/officials associations, state and national governing bodies, clubs, schools and school districts, and tournament operators. Officials commonly serve more than one organization at once, which makes the official — not the league — the shared resource the system must manage carefully.

## Core Model

### The Defining Core

**The official.** A persistent record for each person who officiates: identity and contact details, officiating qualifications and status (certification level, registration state), and restrictions (where, when, and for whom they can work). The official is the unit the whole system exists to manage. Without the roster, the product is a generic scheduler.

**The game.** A dated, scheduled competition event — usually between two named sides at a venue — that needs officiating coverage in one or more **positions** (for example, a head referee and assistant referees, a crew of umpires, a timekeeper). Games typically enter the system created directly or imported from a league's schedule; the referee platform consumes the schedule, it does not normally generate the competition calendar. Without games as the assignment target, the product drifts toward HR-style shift scheduling.

**The assignment.** The binding of one specific official to one position on one game. A game is covered when all its positions are filled by assigned officials; a crew is the set of officials assigned to one game. Assignments are individually tracked — who is on which game, in which role, and whether they have confirmed.

**The assignment loop.** The recurring cycle that gives the Type its name:

```text
Officials declare availability
        ↓
Assignor (or the officials themselves, where permitted) fills game positions
        ↓ under eligibility and conflict constraints
Assignments published and communicated
        ↓
Officials confirm — accept, decline, or stay unconfirmed
        ↓
Declined and unfilled positions return for reassignment
        ↓
Game covered → played → reported → officials paid
```

Remove any leg and the Type collapses: a roster without games is a contact list; games without a roster is a fixture list; both without the loop is a static schedule nobody manages.

### What Mature Products Add

These capabilities are common in current products and expected by the market, but they are additions to the core, not the definition:

- **Availability calendars** — officials declare when they can work; unmarked time is treated as unavailable.
- **Eligibility and conflict machinery** — reasons not to assign a given official to a given game: conflicts of interest with a team, league, venue, or another official; certification or registration status; minimum age; workload limits (per day/week/month); group-based qualification rules.
- **Assignment states and reminders** — accepted / declined / unconfirmed, with reminder cycles and automatic decline handling.
- **Communication** — notifications of new assignments and schedule changes, messages to groups or to the crew of a specific game, acknowledgment tracking.
- **Game fees and payment** — per-position fee structures, travel allowances, and either in-product payment (direct deposit, tax form collection) or clean payment data handed to whoever pays.
- **Game reports** — structured reports submitted by officials after each game (results, discipline, incidents), configurable by the organization.
- **Crew tooling** — copying a crew across back-to-back games at one venue, with position rotation.
- **Ratings and evaluation** — recording assessments of officials and using them in assignment decisions.
- **Mobile app for officials** — the phone is where officials accept games and check schedules.

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:  Official qualification
Realized as:  governing-body certification synced from an external system,
              in-product registration and testing, background-check clearance,
              or a simple internal grade

Concept:  Eligibility constraint
Realized as:  advisory conflict indicators the assignor may override,
              hard blocks on saving an assignment,
              or self-assign gates that refuse ineligible requests

Concept:  Assignment authority
Realized as:  assignor-driven assignment, official game requests
              approved by the assignor, or open self-assignment
```

A reader who has only seen one implementation should still be able to recognize the others from the core.

## How It Works

### Set up the season

The organization configures its vocabulary — age groups and their fee/rating requirements, leagues, venues, positions — and populates the roster, one official at a time or by bulk import. Officials' accounts are commonly provisioned by the organization; the official then completes their own profile, availability, and (where used) payment details.

### Load the games

Games arrive from the league schedule (import or integration) or are created in-product. At this point games are unassigned: positions exist, officials do not.

### Run the assignment loop

1. **Officials declare availability** on their personal calendar. Availability is the first filter on who can take a game.
2. **Positions get filled.** The assignor works game by game (or in bulk views of unassigned games), picking an official for each position. As they consider a name, the system surfaces that official's relevant situation: availability on the game's date, other games that day, history with the two teams, certification status, group memberships, and any conflicts. Where permitted, officials instead request open games or self-assign into them, with the same eligibility machinery applied to their request.
3. **Assignments are published.** Publication is the step that makes assignments visible and notifies officials; work-in-progress assigning stays private to the assignor.
4. **Officials confirm.** Each assigned official accepts or declines. Silence leaves the assignment unconfirmed, and reminder cycles chase it. Declines notify the assignor immediately.
5. **Declines are re-covered.** Declined positions return to the unassigned pool for reassignment — with the declining official protected against accidental re-assignment to the same game. The loop repeats until the game is covered.
6. **Game day.** The official works the game; schedule changes and cancellations push out to everyone involved.
7. **After the game.** The official submits a game report where used; the organization records evaluations where it runs them.
8. **Payment.** Game fees resolve per assignment — whether paid in-product or exported to whoever pays. An assignment that was made and worked is payable regardless of how the confirmation went; cancellations and removals are the explicit exceptions.

### Core vs Common vs Optional

**Defining core** — without these, not a referee management platform:

- managed official roster
- games with positions as the assignment target
- the assignment loop (availability/eligibility → assignment → notification → confirmation → reassignment)

**Standard in mature products** — present in most modern products:

- availability calendars, conflict/eligibility machinery, assignment states with reminders, communication, game fees and payment handling, game reports, crew tooling, mobile apps

**Variant / optional** — depends on organization, sport, and jurisdiction:

- governing-body certification sync, registration modules, background checks, testing and training content, video review, ratings programs, self-assignment, in-product direct deposit, multi-organization official pools, non-referee game-day roles (timekeepers, scorekeepers, event workers) run through the same machinery

## Interfaces

### Assignor: Games / Assigning surface

The operational center.

- **Purpose:** fill every game's positions with appropriate officials and keep coverage current as things change.
- **Typical information:** games by date with venue, teams, league, and positions; per-position assigned official and confirmation state; unassigned / declined / unconfirmed views; per-official conflict and availability indicators beside each candidate name.
- **Primary actions:** assign or reassign an official to a position, publish assignments, copy crews across consecutive games, cancel games, message the crew of a game, override a conflict where policy allows.

### Assignor: People surface

- **Purpose:** maintain the official roster.
- **Typical information:** contact details, qualifications and certification status, availability summary, restrictions and preferences, group memberships, assignment history, ratings.
- **Primary actions:** add/import officials, edit profiles, deactivate, batch-update, message.

### Assignor: Settings / maintenance

- **Purpose:** configure the organization's assignment rules.
- **Typical information:** age groups with fees and requirements, leagues, eligibility groups and their rules, assignment limits, notification settings, permission roles.
- **Primary actions:** define rules, set limits, enable or restrict self-assignment and requests.

### Official: personal surface (web and mobile)

- **Purpose:** let the official manage their officiating work.
- **Typical information:** upcoming assignments with confirmation state, open games available to request or self-assign, personal availability calendar, payment status, messages.
- **Primary actions:** declare availability, accept or decline an assignment, request or self-assign into an open position, submit a game report, update profile and payment details.

### Reports

- **Purpose:** answer management questions — coverage gaps, assignment distribution, payment totals, certification compliance.
- **Primary actions:** run, filter, export.

## Important Rules / Behaviors

### Conflicts advise; the assignor decides

The eligibility machinery — availability, certification, conflicts of interest, workload limits — normally presents as visible indicators during assignment rather than absolute blocks. The assignor can proceed past a warning when judgment calls for it. Some constraints can be switched to hard blocks (for example, refusing to save an assignment for an official whose certification has lapsed), but the default posture across the researched sample is advisory-with-override. This keeps a human accountable for every assignment.

### Availability is opt-in

Officials declare when they can work. In the researched implementations, unmarked time counts as unavailable — an official who has not set availability is effectively invisible to the loop until they do.

### A decline has consequences

Declining notifies the assignor immediately and returns the position to the pool. The system remembers the decline and guards against re-assigning the same official to that game, though the assignor can override. Some products enforce a notice window — an official cannot decline a game that is about to start — and treat last-minute schedule changes specially. Unconfirmed assignments are chased by reminders rather than silently dropped.

### Payment follows the assignment

Where the platform handles payment, the natural payable unit is the assignment itself. A documented implementation pays an official assigned to a played game regardless of whether they confirmed on time, with explicit exceptions — game canceled as non-payable, official removed, fee overridden to zero. The pattern that matters is structural: the assignment record, not a timesheet, is the basis of officiating pay.

### Assignment and notification are separate acts

Making an assignment and telling the official about it are distinct steps. Assigning is iterative private work — draft, reshuffle, balance coverage — and officials see assignments and receive notifications when the assignor releases them. One documented implementation makes this an explicit publish step; in others the notification simply follows the assignment. Either way, work-in-progress assigning does not become a commitment the moment a name is typed.

### Self-assignment inherits the same rules

Where officials may request or self-assign games, the request is checked against the same eligibility machinery — no double-booking, no unqualified positions, no conflicts. Availability may be relaxed for self-assignment (the official is choosing their own time), but qualification and conflict rules still bind. Organizations can restrict which games and which officials may self-assign.

## Variants

- **Dedicated assigning platform** — the whole product is the officials workflow; serves assignors across many leagues and sports from one system.
- **Suite module** — referee management packaged inside a club/league management platform; shallower assigning depth, tighter coupling to the league's own schedule and registration.
- **Association / governing-body system** — run by a referees' association or state/national body; certification status, registration, and compliance are first-class; assignment may span many leagues' games.
- **School / district system** — assigning embedded in school athletics administration, with eligibility and background-check emphasis.
- **Assignment-authority cultures** — assignor-driven (traditional), request-based (officials ask, assignor approves), or self-assign (open positions claimed directly); most products support a spectrum, organizations choose their point on it.
- **Paid vs volunteer officials** — changes whether payment machinery is central or absent, not the core loop.
- **Single-sport vs multi-sport** — sport-specific certification vocabularies vs generic position/qualification structures.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| League Management Platform | adjacent, frequently bundled | owns the competition (teams, fixtures, results, standings, player registration); referee platform owns the officials workforce; games flow from league schedule into the referee platform as data |
| Employee Scheduling Platform | structurally similar, different domain | shifts for employed staff vs games for certified (commonly contracted) officials; sport-qualification and neutrality conflicts have no shift-scheduling analogue |
| Volunteer Management System | similar people-to-commitment shape | centered on recruitment and sign-ups for general causes; officials are certified and commonly paid per game, assigned against a competition calendar |
| Tournament Management Platform | adjacent consumer of the same games | owns brackets, event scheduling, venues; officials coverage is one input, often handed off to a referee platform |
| Sports Scheduling Platform | upstream | generates the game schedule; the referee platform consumes it and assigns people to it |
| Sports Federation Management | governance umbrella | federations govern many organizations and originate certifications; a federation running assigning is using a referee platform as one function |
| Team Management Application | team-centric counterpart | manages one team's roster, schedule, and communication; referee platform manages one official pool across many teams' games |

The sharpest seam is with League Management Platform. The test: remove officials-workforce management and what remains is league management; remove competition management and what remains is a referee management platform. Bundling is common — and dedicated platforms position themselves exactly on the depth of the officials workflow that bundled modules tend to lack.

## Representative Products

- **assignr** — dedicated assigning platform; deep officials workflow (conflict machinery, requests/self-assign, direct deposit); soccer, baseball, football, basketball and other youth/amateur sports
- **Arbiter (Assigning / Arbiter One)** — enterprise assigning inside the Arbiter K-12 sports suite; assigning associations, schools, state governing bodies; paired with Arbiter Pay and eligibility products
- **OTTO SPORT (formerly Demosphere) — Referee Management** — referee management as a named module of a club/league management suite
- **Stack Sports** — league-management ecosystem whose assigning capability is a bolt-on; included as the league-pole contrast that clarifies the seam

## Sources

Research date: **2026-09-09**

- assignr — product site and assigning page: https://www.assignr.com/ , https://www.assignr.com/assigning-referees-and-umpires/
- assignr Help Center (officials and assignor collections; assignment, conflicts, availability, self-assign, accept/decline, USSF certification integration articles): https://support.assignr.com/
- Arbiter — product site and Assigning product page: https://arbitersports.com/ , https://arbiter.io/products/assigning/
- OTTO SPORT (formerly Demosphere) — product site and Referee Management solution page: https://www.ottosport.ai/ , https://www.ottosport.ai/referee-management
- Stack Sports — product site: https://stacksports.com/

> Sourcing limitations: official help-center documentation was reachable in depth for one dedicated platform (assignr); the Arbiter help center and several other dedicated products (HorizonWebRef, ZebraWeb, Game Officials, RefTown) could not be fetched from the research environment, so their evidence is limited to product/marketing pages and assertions about them are kept at that strength. No non-US dedicated product could be sampled directly; the definition was checked against the paper-era assigning practice instead. Precise operational defaults observed in one product (decline notice windows, notification cadences, plan limits) are deliberately not stated as category facts.
