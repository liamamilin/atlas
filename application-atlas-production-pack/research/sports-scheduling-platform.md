# Research Notes — Sports Scheduling Platform

Research date: 2026-09-09
Slug: sports-scheduling-platform
Directory leaf: Sports Scheduling Platform (§28 Sports, Fitness & Recreation)
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand what a Sports Scheduling Platform actually is from real products: what object the system holds (the game schedule?), how schedules are produced (generation, import, negotiation, manual authoring), what constraints shape them (venues, timeslots, blackouts, conflicts, travel), how schedules change over a season (postponements, make-ups, re-generation), who consumes them and through which surfaces, and where the boundary lies against the neighboring leaves (League Management, Tournament Management, Sports Facility Management, Referee Management, Sports Registration, Sports Meet Management, Team Management, and the generic scheduling family: Employee Scheduling, Resource Calendar, Appointment/Meeting Scheduling).

## Initial Boundary

Initial hypothesis (to be tested, not asserted):

- Core use: producing and maintaining the competition calendar for sports organizations — arranging matchups (games/fixtures) into dates, timeslots and venues across a season or event, under constraints, and keeping the published schedule current as things change.
- Primary users: the schedule owner — league/competition secretary, athletic director, club scheduler, tournament operator; consumers are teams, players, families, schools, officials.
- Nearest types: League Management Platform (schedule is one step of the season loop there), Tournament Management Platform (bracket container vs calendar placement), Sports Facility Management (venue as bookable inventory vs venue as scheduling constraint), Referee Management Platform (consumes the schedule; assigns people), Sports Registration Platform (intake vs placement), Sports Meet Management (one meet's internal program vs inter-organizational calendar), Team Management Application (one team's calendar).
- Prior-pass commitments to honor:
  - league-management-platform (2026-09-08): "scheduling platforms exist where the schedule (constraint solving for venues/officials/availability) is the whole job… Remove results/standings → Sports Scheduling Platform. Keep both."
  - referee-management-platform (2026-09-09): "Generates the game schedule; the referee platform consumes it and assigns people to it."
  - sports-meet-management (2026-09-09): "that sibling (working understanding) arranges fixtures/games across organizations and calendars."
  - sports-registration-platform (2026-09-09): "scheduling = bundled module inside registration suites, not a center."
- Unknowns: is venue assignment definitional; is publication/consumption definitional vs generator-only tools; is constraint machinery definitional or graded; is practice scheduling in-type; does a pro/elite optimization tier constitute the same Type.

## Research Questions

1. What is the core object — a "game", "fixture", "event", "slot"? What does each record bind (matchup, date, time, venue, level, officials)?
2. What is the container — league season, tournament, conference season, club program? Does the platform own the container or only the calendar?
3. How is the schedule produced? Auto-generation from pairings + constraints; import (spreadsheet); negotiation between independent organizations; manual placement; a mix?
4. Which constraints exist and how are they enforced — team/coach/division constraints, blackout dates, venue/field availability and permits, timeslots, max games per day, rest between games, back-to-back, travel, home fields?
5. What does the production loop look like — generate → inspect → fix (unscheduled games, retry allocation, regenerate, pause constraints, manual tweaks, lock games, snapshots, drafts)?
6. How do changes flow — postpone/rainout, cancel, insert delay, off-weeks, mid-season rework, forfeits? Who is notified?
7. How is the schedule consumed — public pages, embeds, print/PDF, CSV/Excel export, calendar sync/subscribe, team views, mobile apps, feeds to downstream systems?
8. What rides on the same machinery but is not scheduling — score entry, standings, registration, websites, payments, officials?
9. Where exactly are the seams vs the eight neighboring Types listed above?

## Representative Products

Chosen for market representativeness, documentation depth, different product philosophies, and different customer tiers:

1. **LeagueLobster** — dedicated, scheduling-first product ("League and Tournament Scheduler"); amateur/community organizers; free LITE generator → PRO tiers; Intercom help center with a 64-article Scheduling collection (Tier-1). Philosophy: the schedule generator is the product.
2. **Arbiter (Arbiter Game — "Event and Game Scheduling")** — the enterprise K-12/state-association pole; athletic departments schedule games across schools, conferences and state associations, connected to assigning, facilities and publishing. Product/FAQ pages reachable (Tier-2); help center not fetched this pass (Zendesk known slow from the referee pass). Philosophy: enter once, publish everywhere, connected suite.
3. **OTTO SPORT AI (formerly Demosphere)** — youth-sports club/league suite; scheduling is a named module ("Smart, Flexible Scheduling") inside a suite whose center is registration/club operations. Club-management solution page reachable (Tier-2). Philosophy: the master calendar as one surface of the suite.
4. **PlayMetrics** — club operations platform (club tier); scheduling surfaces (league scheduler tool, field schedule, practice schedules, team events) evidenced at release-notes level (B, thin). Philosophy: club operations with scheduling as a workstream.
5. **LeagueRepublic** — cross-check product: the league pass (2026-09-08) documented its scheduling engine at Tier-1 (Template/Advanced Scheduler, timeslots, venue sharing, single-venue scheduling, byes, spreadsheet import, inter-division matches, print/download). Used as market corroboration, not re-sampled.

Boundary markers (examined, not used as samples):

- **Genius Sports** — pro-tier candidate; current official surface contains no scheduling product (data/betting/fan engagement) → dropped; pro/elite optimization scheduling recorded as market-structure knowledge only, no product claims.
- **TeamSnap** — team-side consumer calendar (one team's schedule) — the Team Management seam marker, consistent with prior passes.

## Sources

Fetched 2026-09-09 (WebFetch):

- LeagueLobster — https://www.leaguelobster.com/ (positioning: "SIMPLIFY YOUR SPORTS SCHEDULING"; round-robin/tournament/bracket generators; constraints feature list; calendar view with drag-and-drop reschedule; calendar sync/subscribe; public schedule page customization; embed; CSV/Excel export; registration; club pages; API)
- LeagueLobster Help Center — Scheduling collection (64 articles): https://help.leaguelobster.com/en/collections/164411-scheduling (article titles map the workflow: Getting Started LITE/PRO, Manual Tweaks, Bye Weeks, Off-weeks, Sharing Your Schedule, Export to CSV/Excel, Printing, Deleting a Game, Postponing Games, Schedule Checker, Locked Games, Home Fields, Doubleheaders, Divisions/Pools, Playoff Brackets/Modes, Calendar View, Constraints, Insert Delay, Copying a Schedule, Snapshots, Importing Games, Time Slot Balancer, Adding a Game, draft state, mid-season changes, forfeits, standings, scorekeepers)
- LeagueLobster — Constraints article: http://help.leaguelobster.com/en/articles/805124-constraints (full constraint taxonomy + generation loop, quoted below)
- Arbiter — root: https://arbiter.io/ (product line incl. "Event and Game Scheduling", "Facilities Scheduler"; markets K-12 / Assigning Associations / Governing Bodies)
- Arbiter — Arbiter Game product page: https://arbiter.io/products/scheduling/ (feature panels + FAQ, quoted below)
- OTTO SPORT AI — root: https://www.ottosport.ai/ (product/solution navigation; no dedicated scheduling solution page)
- OTTO SPORT AI — Club Management: https://www.ottosport.ai/club-management ("Smart, Flexible Scheduling" module, quoted below)
- PlayMetrics Support Center — search "schedule": https://help.playmetrics.com/hc/en-us/search?query=schedule (release-notes-level evidence of scheduling surfaces)

Unreachable / abandoned per network rules:

- https://www.ottosport.ai/scheduling → 404 (no dedicated scheduling page; club-management page used instead)
- https://geniussports.com/scheduling → 404; https://geniussports.com/ fetched → no scheduling product on current surface → pro-tier pole dropped (sourcing limitation recorded)
- PlayMetrics deeper structural docs not pursued (knowledge base is dominated by release notes; further fetches would yield the same tier)
- Arbiter help center not fetched (Zendesk timeouts in the 2026-09-09 referee pass); Arbiter claims kept at product-page strength

## Product A — LeagueLobster

Evidence layer: A (direct observation, official site + Tier-1 help center).

### Key observations

- Positioning: "The smart choice for tournament and league planners… SIMPLIFY YOUR SPORTS SCHEDULING." Entry actions: "Create a League", "Create a Tournament", "Generate a Bracket"; free LITE round-robin generator "up to 50 games"; paid PRO features. The schedule generator is the product. [A]
- Scheduling objects: teams, divisions/pools, venues/fields, time slots, weeks (league mode), games. A schedule is created per league or tournament; divisions/pools are first-class ("How to create age groups / divisions / pools and assign teams"); byes for odd team counts; off-weeks (skip a week, e.g. holidays); doubleheaders; home fields ("assign teams to certain home fields / venues"). [A]
- Constraints (PRO) — the vendor's own taxonomy [A]:
  - Team constraints (negative): "do not schedule Honey Badgers on Saturday before 2pm"; "do not schedule Neon Ninjaz at the Field 2 after 10pm"; block a team from a venue or a time window.
  - Coach constraints: multiple selected teams "will not be scheduled at the same time (presumably because they share the same coach — but of course this can be used for other scenarios, like a player joining multiple teams)."
  - Division constraints (positive): "for Division 1, only do this" — only a given field, only before 8pm, only Fridays/Saturdays, per-pool variants.
  - Min/max time between games: minimum rest (prevent back-to-back), maximum wait (tournament use); "skip for playoffs" checkbox; league scheduler "treats weeks as entirely isolated and does not move games between weeks."
  - Max back-to-back games; max games per day (general limit + per division/pool/team/day advanced options).
  - Travel constraint: "Distance between venues" (PRO article).
- Production loop [A]: enter constraints → "generate schedule"; constraints can make generation fail ("you might see unscheduled games"); two unscheduled-game variants shown in red — "NO POSSIBLE TIME SLOTS" (constraints blocked all slots that week → move the game to another week, revise constraints, or schedule manually) and "NOT YET SCHEDULED" (eligible slots occupied → retry allocation or regenerate); "retry allocation" takes the same games and refits them, "erase games > generate schedule" also regenerates pairings; individual constraints can be paused for a rerun; games can be scheduled manually.
- Maintenance/authoring [A]: manual tweaks (change venue/time/date/referee per game); adding a game; deleting a game; locked games (protect specific placements while re-allocating); swap two teams' schedules; adding/removing teams/games/weeks mid-season; insert delay (shift games when off-schedule, e.g. rain delay); postponing games (rainouts); forfeits; copy season/tournament; snapshots ("basic version management… make and restore backups / revert to earlier versions"); draft state ("How to set a schedule to draft"); Schedule Checker; Time Slot Balancer ("even out time slots between teams").
- Consumption/distribution [A]: publish and share the schedule with players; public schedule page brandable with filters (division/team) and team highlighter; embed on your site; print / save to PDF; export to CSV/Excel ("easily transfer your fixtures to SportsPress or other tools"); sync games to calendar apps; players subscribe to their team's fixtures; calendar view "color coded by division, and easily reschedule games via drag and drop"; alerts/notes/announcements on the schedule page; API.
- Bundled-but-not-scheduling features: score entry, standings configuration, playoff brackets, registration/payments, club landing pages, marketing emails. Vendor's own framing keeps these beside the scheduler. [A]
- Referee presence: a referee field exists on games (manual tweaks article) — a pointer, not an assignment system. [A]

## Product B — Arbiter Game (Arbiter "Event and Game Scheduling")

Evidence layer: A/T2 (official product + FAQ pages; help center not fetched — claims kept at product-page strength).

### Key observations

- Positioning: "Arbiter Game gives athletic departments one place to schedule games, manage officials and staff, coordinate facilities, and publish updates — all from a connected platform." FAQ: "K-12 athletic scheduling software that connects schools, assigners, and officials… the central hub for Arbiter's athletic management software. From practices to playoffs." [A/T2]
- Named capabilities [A/T2]:
  - "Smart Scheduler: Automatically generate and update schedules."
  - "Conflict Checker: Detect overlapping games or facility usage."
  - "Multi-Level Scheduling: Coordinate across varsity, JV, and middle school levels."
  - "League Scheduler: Manage league schedules and push updates to all participating schools."
  - "Facility Integration: Sync facility bookings through Arbiter Facilities Scheduler."
  - "Integrated Communication: Notify staff, teams, and fans instantly."
- Feature panels: "Schedule athletics and non-athletic events in the same platform"; "Coordinate dates, times, and locations from a single dashboard"; "Prevent conflicts with built-in scheduling rules and validations"; "Update events instantly without disrupting connected workflows"; "Assign coaches, officials, and event workers within the same platform"; "Integrate with assigners and conference scheduling workflows"; "View real-time availability before confirming matchups"; "Link schedules directly to facilities and venue resources"; "Push updates instantly to connected websites and platforms. Publish public schedules in real time. Notify staff, officials, and families automatically." [A/T2]
- "What sets it apart": "Built-In League & Conference Scheduling — coordinate schedules across districts and conferences with integrated League Scheduler — reducing manual back-and-forth between schools"; "Real-Time Distribution Across Platforms." [A/T2]
- Users: athletic directors (oversee event scheduling, rosters, facilities), coaches (view/share schedules), officials & assigners (via Arbiter Assigning), district & league admins (top-down visibility). Governing-body market: "Manage rules, schedules, and compliance across every school from one platform… Championship and postseason scheduling support." [A/T2]
- Customer workflow (AD testimonial): "I enter the info once, and it goes to my state Association. It goes to my Arbiter Live streaming site. It goes to parents and students, and it's published immediately." Another: "Arbiter makes it easy to view opponents' contact information… and see all our games in one place." Facilities Scheduler testimonial: "Staff can now see real-time facility availability when scheduling events." [A/T2]
- Separately packaged neighbors on the same suite: Assigning Solutions (officials), Facilities Scheduler (facility requests/approvals/rentals), Pay, Eligibility, Registration, Websites. [A/T2]

## Product C — OTTO SPORT AI (formerly Demosphere)

Evidence layer: A/T2 (official club-management solution page; support site historically unreachable — claims at solution-page strength).

### Key observations

- Positioning: "complete operating system for running youth sports… club directors, league managers, sport organizations." Scheduling is one named tab among Registration / Scheduling / Teams / Comms / Analytics / Mobile / Website. [A/T2]
- Scheduling module ("Smart, Flexible Scheduling"): "Handle blackout dates, coaching conflicts, and field permits without the spreadsheet juggling. One master calendar tracks every practice, game, and training session — then notifies everyone when things change." [A/T2]
  - "Scheduling that thinks ahead — Your system tracks every event in one place so you are not rebuilding the week by hand every time something shifts."
  - "A calendar that keeps everyone moving — Parents know where to be, coaches see their full week at a glance, and administrators stay ahead of conflicts before they happen."
  - "Integrated league management — Keep standings current, track disciplinary information, and advance teams through competitive play — all within the same system."
- Customer quote: "Scheduling has never been easier and with the new scheduling features. I can now track all of our field loading across our platforms in one place instead of using separate spreadsheets." (field loading = venue utilization as a scheduling concern) [A/T2]
- Change propagation: "Payment reminders, schedule-change alerts, and event reminders go out automatically"; mobile app surfaces "game times, practice schedules, field directions"; club website "schedules, rosters, standings… pull directly from your platform." [A/T2]
- Prior-pass corroboration (league pass, 2026-09-08, league-management solution page): "Smart, Flexible Scheduling (blackout dates, coaching conflicts, field permits… master calendar… automatically notifies everyone when things change)." [A, prior pass]

## Product D — PlayMetrics

Evidence layer: B (thin — release-notes level; no structural docs fetched; assertions kept minimal).

### Key observations

- Club operations platform for youth clubs; search over the support center surfaces scheduling as a first-class workstream: "Schedules > Fields page" (fields/facilities filtering), "league scheduler tool" (with surface filter on view/edit pages), "League schedule matchups are created when a game is manually added" (matchups as schedulable objects), "League schedule supports changing opponents and creating cross-divisional" games, "Practice schedule notifications", "Club Schedules list" (with timezone indication), "Archived team event availabilities included on the schedule export". [B]
- Reading: the club pole schedules practice, games (league + cross-division), and field time inside a club-operations suite; no contradiction with the core model; depth not verifiable from this tier. [B]

## Cross-check — LeagueRepublic (from the league-management pass, Tier-1, 2026-09-08)

- Schedule generator ("free schedule maker"), Template vs Advanced Scheduler, options for creating a schedule, scheduling at a single venue, over several timeslots on the same day, venue sharing for teams, inter-division matches, byes, missing matches, creating a schedule from a spreadsheet, print/download. [A — prior pass]
- Confirms the same production loop and constraint set from a fixtures-first league platform: the scheduler is a deep engine inside a league product; results/standings ride alongside.

## Cross-product Comparison

| Aspect | LeagueLobster | Arbiter Game | OTTO SPORT | PlayMetrics | LeagueRepublic (prior pass) |
|---|---|---|---|---|---|
| Primary customer | amateur/community league & tournament organizers | K-12 athletic departments, conferences, state associations | youth clubs & leagues (suite) | youth clubs (suite) | amateur/local leagues |
| Scheduling's role | the product itself | named product line in connected suite | named module in suite | workstream in club ops | deep engine inside league platform |
| Schedule containers | league (weeks) / tournament (not week-bound) | school season, conferences, leagues, postseason | season; practices+games+training on one master calendar | club programs; league schedules | seasons/divisions |
| Core object | game (matchup × date × time × venue) | game/event (with non-athletic events too) | practice/game/training session on calendar | league schedule matchups; practices; team events | fixture |
| Production modes | generate from pairings + constraints; manual tweaks; import games | Smart Scheduler auto-generate; league scheduler pushed to schools; manual coordination; "confirm matchups" | master calendar; conflict-aware planning | league scheduler tool; manual adding | generator; template/advanced; spreadsheet import |
| Constraint machinery | team/coach/division constraints, venue+time blocks, min/max rest, max games/day, back-to-back, travel, slot balancing | "scheduling rules and validations"; conflict checker (overlapping games/facility use); real-time availability | blackout dates, coaching conflicts, field permits, field loading | (not visible at this tier) | timeslots, venue sharing, single-venue, byes |
| Change management | postpone, insert delay, off-weeks, mid-season rework, swap teams, locks, snapshots, draft | update events instantly; automatic updates/notifications | notifies everyone when things change | schedule-change notifications (release notes) | (rescheduling supported; league pass focus elsewhere) |
| Consumption | public page, embed, print/PDF, CSV/Excel, calendar sync + per-team subscribe, API | publish to websites/ArbiterLive; notify staff/officials/families; state association | parent/coach/admin calendar views; mobile app; club website pulls from platform | club schedules list; schedule export | league site, embeds/API, print |
| Bundled neighbors | scores/standings, brackets, registration, websites | assigning, facilities, pay, eligibility, registration, websites | registration, standings, rosters, comms, website | registration, programs, club ops | results/standings, registration, websites, referees |

Reading of the comparison:

- All samples realize the same spine — matchups of competing sides placed into a dated/venue-bound calendar under the operator's constraints, maintained through changes, published to consumers. [B]
- Production is always multi-modal: generation where the operator has pairings and constraints; manual authoring/tweaking always present; import common; negotiation between organizations appears where organizations are independent (K-12 "confirm matchups", conference league scheduler). [B]
- Constraint machinery is graded, not binary: at minimum the calendar itself (play dates/weeks/timeslots); mature products add venue/permit availability, blackout dates, person-overlap conflicts, rest/travel/game-load rules. [B]
- Change management with propagation to consumers is universal; the schedule is a living record, not a one-time artifact. [B]
- Everything else (results, standings, brackets, registration, payments, websites, officials) rides alongside as bundling in every sample — including the dedicated product (LeagueLobster scores/standings/brackets). The center of gravity remains the calendar. [B]

## Canonical Model (L0/L1/L2/L3)

### L0 — Defining Invariant (three jointly-held structures)

A Sports Scheduling Platform is the competition-calendar system of record: the schedule is the whole job. Three jointly-held structures; remove any one and the product stops being this Type:

1. **The scheduled competition event as the unit of record.** A persistent, maintained set of dated events binding matchups of competing sides (teams or individuals) to a date and time and, typically, a venue/playing surface, held within the operator's competition calendar (season, weeks/rounds, divisions, or event program). The event is a competition event between sides — not a shift, an appointment, or a generic calendar entry; and its *placement in time* is what the system owns. (Remove the matchup semantics → generic calendar/resource scheduling; remove the placement → a matchup list, which is competition structure = league/tournament territory.)
2. **Schedule production as the defining act.** The platform's core function is producing and holding the arrangement of matchups into that calendar — generated from pairings against the operator's constraints (play dates, timeslots, venue availability, blackouts, conflicts), imported, negotiated between participating organizations, or manually authored — with conflict checking inside the production loop. The defining output is the schedule itself, not results, standings, or bookings. (Remove → a league platform, where scheduling is one step of the season loop; or facility booking, where a space transaction replaces the matchup placement.)
3. **The published, living schedule with change propagation.** The schedule exists as current shared state consumed by participants and downstream consumers (public schedule pages, team views, embeds, print/PDF, exports, calendar sync/subscription, feeds), and changes — reschedules, postponements, cancellations, make-ups — are applied to the record and propagated to everyone who consumes it. (Remove → a one-shot generator that emits a file; or a hand-maintained document nobody can consume.)

Jointly-held is load-bearing:

- 1 alone = an event calendar (Calendar Application territory)
- 2 alone = a fixture-generator tool (the thin tool pole of this Type — a program, not a platform)
- 3 alone = a published calendar with no production machinery behind it
- 1+2 without 3 = an offline/private scheduling tool producing outputs
- 1+3 without 2 = a hand-maintained published calendar
- 2+3 without 1 = generic resource/appointment scheduling

### L1 — Common Mature Structure

- Competition-structure inputs: seasons, divisions/pools, teams/sides, byes, home/away, inter-division play, game durations per division
- Venue/field model: fields/courts/venues as schedulable resources with timeslots, permits, home-field assignment, venue sharing, field-loading/utilization visibility
- Constraint machinery: blackout dates; person-overlap conflicts (coach/player on multiple teams); max games per day; minimum rest / max wait between games; back-to-back limits; travel constraints; time-slot balancing
- Production ergonomics: generate → inspect → fix loop; retry allocation vs regenerate; unscheduled-games surfacing; pausing constraints; locked games; snapshots/versioning; draft state; copy season/tournament
- Manual authoring: add/edit/move/delete individual games; change venue/time/date/referee per game; swap teams' schedules; doubleheaders; mid-season restructuring
- Change operations: postpone (rainouts), insert delay (shift the rest of the day), off-weeks, cancellations, forfeits as schedule-affecting outcomes
- Conflict checking/validation (overlapping games, facility use, person conflicts)
- Consumption surfaces: public schedule pages with filters/highlighting; embeds; print/PDF; CSV/Excel export; calendar sync and per-team subscriptions; API feeds; mobile views
- Change notifications to participants, families, staff, officials
- Practice/training scheduling riding the same calendar alongside games (observed at 3 of 4 samples)
- A referee/official field on games and integration hooks toward assigning (the pointer, not the assignment loop)
- Adjacent bundling common in the market: score entry, standings, brackets, registration, websites (bundling, not defining)

### L2 — Variant / Optional Structure

- Negotiated inter-organizational scheduling: independent schools proposing/confirming games; conference-run schedules pushed down to member schools (K-12 pole)
- Governing-body/championship/postseason scheduling oversight across many schools/organizations
- Tournament scheduling mode (not week-bound; pools/knockout placement into slots)
- Non-athletic events scheduled on the same platform (school activities)
- Elite/professional tier: optimization-grade constraint solving for league seasons (market-structure knowledge; not evidenced this pass)
- Registration/payments/websites/apps as suite packaging
- Esports and other competition realizations

### L3 — Vendor-specific (research notes only)

- LeagueLobster: LITE (free, ≤50 games) vs PRO; league scheduler treats weeks as isolated; tournament scheduler not week-bound; unscheduled-game variants "NO POSSIBLE TIME SLOTS" vs "NOT YET SCHEDULED"; retry-allocation vs regenerate distinction (allocation refits the same pairings, regenerate re-draws them); pause-a-constraint toggles; max-wait semantics (≤18h within a day); "skip for playoffs" checkboxes; Snapshots; Insert Delay; Time Slot Balancer; Team Highlighter; draft state; CSV transfer "to SportsPress or other tools"
- Arbiter: Smart Scheduler / Conflict Checker / Multi-Level Scheduling / League Scheduler naming; ArbiterLive publishing; "enter once, published immediately" one-entry workflow; athletics + non-athletic events in one platform; Facilities Scheduler as a sibling product (facility requests/approvals/rentals)
- OTTO: "Smart, Flexible Scheduling" module; master calendar across practices/games/training; field-loading tracking; SafeSport-compliant team chat context
- PlayMetrics: "Schedules > Fields" page; league scheduler tool with surface filter; matchups created when a game is manually added; cross-divisional game creation; timezone-aware club schedules list

## Historical / Market-Sample Check (§24)

Conceptual check (evidence layer C; no pre-digital source fetched):

The paper-era fixture secretary — the competition committee draws the round-robin grid (or uses a fixture wheel) to decide who plays whom; the secretary lays the pairings onto the season's dated calendar against the grounds the club has (Saturdays, which ground, morning/afternoon slots), avoiding clashes with shared grounds and school terms; the fixture list is printed into the handbook, posted on the noticeboard, sent to the local paper; when a match is rained off, the secretary amends the list, arranges a new date, and re-notifies (letter/phone/notice). This satisfies all three L0 legs at analog level: dated matchup events on a competition calendar; production of the arrangement against constraints; a published, amended, re-communicated schedule. Therefore the L0 must not include: software generation engines, drag-and-drop calendars, constraint solvers, calendar sync, exports, notifications infrastructure, mobile apps, or websites. All confirmed as L1/L2. The definition also survives older/regional shapes: a conference athletic secretary coordinating games by mail/phone across schools (negotiated production), a club announcing practice times (practice scheduling is common-but-not-definitional), and a one-off cup schedule drawn and posted (container = tournament, but the scheduling act is the same Type's act).

## Vendor-specific Findings

See L3. Additional market-structure observations:

- The dedicated product (LeagueLobster) bundles scores/standings/brackets/registration yet markets itself as a scheduler — evidence that bundling is universal while the center of gravity stays the calendar. This is the same center-of-gravity pattern the league pass recorded from the league side.
- The K-12 pole (Arbiter) shows scheduling as a connected hub: one entry propagates to state association, websites, streaming, families. The suite separates Assigning and Facilities Scheduler as distinct products — corroborating the referee and facility seams from the vendor's own packaging.
- The youth/club suites (OTTO, PlayMetrics) show scheduling as the master calendar that registration feeds and communication consumes — the registration pass's "bundled module, not a center" characterization confirmed from the suite side.

## Boundary Findings

1. **vs League Management Platform.** The league platform owns the competition loop — container, programme, results, computed standings; scheduling is one step. This Type owns the calendar as the whole job. Ratified from both sides: the league pass's remove-test ("remove results/standings → Sports Scheduling Platform"), and this pass's reverse test (add results/standings/computed tables as the center → league platform). LeagueRepublic and LeagueLobster both bundle results/standings around a scheduling engine — center of gravity decides. Keep both.
2. **vs Tournament Management Platform (unprocessed).** A tournament platform owns the bracket/competition container (entrants, seeding, advancement). This Type owns calendar placement of games. Bracket *structures* appear here only as features (LeagueLobster bracket generator; playoff modes), and tournament *scheduling mode* appears here as a variant (placing tournament games into slots). Forward flag for that pass: the seam is container-vs-calendar (bracket progression vs placement), consistent with the meet pass's container framing.
3. **vs Sports Facility Management.** The facility platform is the venue operator's system of record: rentable-space inventory, booking transactions, revenue. The scheduling platform treats venues as constraints and inputs — it places games into venue time; it does not sell or contract space. Ratified against the facility pass's core (rentable-space inventory + booking transaction + money record). A "Home Fields" assignment is not a booking. Keep both.
4. **vs Referee Management Platform.** This Type generates the schedule; the referee platform consumes it and assigns people to it (referee pass seam). The referee field on a game here is a pointer; the assignment loop (availability → assignment → accept/decline) lives there. Arbiter's own packaging separates Scheduling from Assigning Solutions. Keep both.
5. **vs Sports Registration Platform.** Registration is the intake transaction building the roster; scheduling is calendar placement. The registration pass held "scheduling = bundled module inside registration suites, not a center" — confirmed from the suite side (OTTO/PlayMetrics). Keep both.
6. **vs Sports Meet Management.** A meet orders its own event program into sessions/heats (internal competition logistics). This Type arranges games/fixtures across organizations and calendars (the meet pass's working understanding, ratified). Keep both.
7. **vs Team Management Application.** One team's calendar/roster/availability vs the competition-wide schedule spanning many sides. Team-side products consume published schedules (per-team subscriptions observed at LeagueLobster; family views at OTTO). Keep both.
8. **vs generic scheduling Types (§03.09 Meeting/Appointment, §09 Employee Scheduling, §03.08 Resource Calendar).** No matchup-of-competing-sides semantics; no competition calendar; no venue/permit constraint family shaped by sport. Employee scheduling binds staff to shifts; appointment scheduling books services; resource calendars record reservations. The scheduled competition event is the distinguishing object. Keep separate.

## Uncertainties

- **Elite/professional tier not directly evidenced.** Genius Sports' current surface contains no scheduling product (dropped after one failed guess + one root fetch); ORTEC-class optimization vendors not attempted within budget. The pro tier is described only at market-structure level (optimization-grade constraint solving for league seasons); no product claims made. Risk: the pro pole might emphasize computational optimization far beyond the sampled constraint machinery — recorded as L2 market-structure knowledge, not L1.
- **Arbiter operational mechanics unverified** (help center not fetched; product-page evidence only). All Arbiter claims kept at product-page strength; no precise workflow/state claims.
- **OTTO evidence is solution-page level** (support site historically unreachable across passes).
- **PlayMetrics evidence is release-notes level** — used only to establish that the club-pole scheduling surface exists with league/practice/field/game objects; no depth claims.
- **Venue as invariant:** games with TBD venues were not directly observed in fetched materials; venue placement held as "typically, not always" — the minimal reading (date/time + matchup) is what L0 asserts.
- **Historical check is conceptual** (layer C) — no archival fixture-handbook source fetched.
- **Practice scheduling** observed at 3/4 samples (LeagueLobster's help center is game/tournament-focused); held common, not definitional — a practice-only tool would drift toward facility/team territory.

## Final Synthesis

A Sports Scheduling Platform is the competition-calendar system of record for sports organizations. Its defining core is three jointly-held structures: the scheduled competition event (matchups of competing sides bound to date, time and typically venue, within the operator's competition calendar); schedule production as the whole job (generating/arranging matchups into that calendar against constraints — by engine, import, negotiation, or hand — with conflict checking in the loop); and the published, living schedule (current shared state consumed through pages, embeds, exports, calendar sync and feeds, with every reschedule/postponement/cancellation applied to the record and propagated to its consumers). Around that spine, mature products add venue/permit and timeslot machinery, constraint engines (blackouts, person conflicts, rest, travel, game loads), production ergonomics (locks, snapshots, drafts, retry/regenerate), change operations (postpone, insert delay, mid-season rework), and rich consumption surfaces; practice scheduling, score entry, standings, brackets, registration, websites and officials pointers ride alongside as common or bundled structure. The Type is defined by the calendar, not by any container: leagues, tournaments, conferences and club seasons all place their games through it, while the competition containers themselves (results, standings, brackets, programs) belong to the neighboring Types.
