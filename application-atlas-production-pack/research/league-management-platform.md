# Research Notes — League Management Platform

Research date: 2026-09-08
Slug: league-management-platform
Directory leaf: League Management Platform (§28 Sports, Fitness & Recreation)

## Research Goal

Understand what a League Management Platform actually is from real products: what objects exist inside it (league, season, division, team, player, fixture, result, standings), who operates it, how a season actually runs from setup to rollover, which rules govern results and standings, and where its boundary lies against the neighboring §28 leaves (Team Management Application, Tournament Management Platform, Sports Scheduling Platform, Sports Registration Platform, Sports Federation Management, Referee Management Platform).

## Initial Boundary

Initial hypothesis (to be tested, not asserted):

- Core use: organizing and running a recurring sports competition — a league — among multiple member sides (teams or individual players) over a season: build the fixture programme, record results, compute and publish standings.
- Primary users: league administrators/organizers (often volunteers, e.g. "league secretary"), with delegated entry by team administrators/captains/players/referees.
- Nearest types: Team Management Application (one team at the center), Tournament Management Platform (one event/bracket at the center), Sports Scheduling Platform (schedule as the whole job), Sports Registration Platform (intake as the whole job), Sports Federation Management (governing body over many organizations/competitions).
- Unknowns: is scheduling or standings the true center; how far the type stretches (ladder/box leagues, esports); whether registration/payments are definitional or common.

## Research Questions

1. What is the object hierarchy? (league / season / division / side / player / fixture / result / standings)
2. How does a season run end-to-end (setup → fixtures → results → standings → rollover)?
3. What exactly do standings rules configure (scoring method, ranking basis, point values, tie-breakers, exclusions)? Are standings computed or hand-maintained?
4. Who can enter results, through which channels, and how is the results record governed (approval, locking, corrections, forfeits)?
5. How is the fixture programme produced (generator, import, participant-arranged)?
6. Which capabilities are common but not definitional (registration, payments, rosters, communication, referee assigning, facilities, websites, statistics)?
7. Where do the boundaries with the neighboring leaves run, and what "remove" tests separate them?

## Representative Products

Chosen for market representativeness, documentation depth, different product philosophies, and different customer tiers:

1. **LeagueRepublic** — dedicated league-running service for amateur/local leagues (football, darts, pool, bowling, netball, esports...), strong in UK/global grassroots; free core + paid plans; powers the England FA's FULL-TIME system for league secretaries. Fixtures/results/standings-first philosophy. (Tier 1 help centre reachable.)
2. **LeagueApps** — US youth-sports management platform (registration/payments/comms/scheduling/standings/facilities); organization-run leagues as one program type among camps/clubs/tournaments. Registration-led platform philosophy. (Tier 1 help centre reachable.)
3. **SportyHQ** — web competition + membership platform for racket sports (squash, tennis, badminton) serving clubs, facilities, schools and governing bodies; league family includes team leagues, solo leagues, box leagues and ladders — deliberately distinct features. Individual/club competition philosophy. (Tier 2 official feature pages reachable; /help docs not fetched.)
4. **Demosphere / OTTO SPORT AI** — US youth-sports league management (Demosphere lineage rebranded OTTO SPORT AI in the fetched material); registration → scheduling → competition/standings → referee assigning → communication for youth leagues run by volunteer boards. Youth-organization-suite philosophy. (Tier 2 official solution page reachable; legacy support site unreachable.)

Boundary markers (examined but not used as samples):

- **TeamSnap (TeamSnap ONE help)** — team-first consumer product (rosters, schedules, messages, media); the league-side "for Business" docs were unreachable (see Sources). Used as the team-side sibling marker.
- **Challengermode** — esports competition platform; self-describes as tournament/matchmaking/ladder/gamification platform. Tournament-first sibling marker for the esports realization.

## Sources

Fetched 2026-09-08 (WebFetch):

- LeagueRepublic — https://www.leaguerepublic.com/ (features: League Scheduler, Results & Statistics, Team & Player Registration, Site Builder, Website Integration; FA FULL-TIME partnership note)
- LeagueRepublic Help Centre — https://help.leaguerepublic.com/ (collections: League Setup, Scheduling, Scoring and Statistics, People and Roles, Tournaments; article: "How to enter results, approve and lock")
- LeagueApps — https://leagueapps.com/ (platform features, program types, roles)
- LeagueApps Help Center — https://support.leagueapps.com/hc/en-us (categories incl. Schedules & Standings; articles: "Customize Standings Rules", "Updating Scores & Standings")
- SportyHQ — https://www.sportyhq.com/ (home; features: Team Leagues, Box Leagues; feature index incl. Solo Leagues, Ladders, Rankings & Sanctioning, Court Bookings)
- Demosphere / OTTO SPORT AI — https://demosphere.com/league-management (youth sports league management solution page; also /otto-sport, /sportwrench product pages in nav)
- Challengermode — https://challengermode.com (structured metadata: tournaments, matchmaking, ladders, gamification)
- TeamSnap — https://help.teamsnap.com (TeamSnap ONE help: team-side categories)

Unreachable / abandoned per network rules:

- https://support.leaguerepublic.com → 404 (help centre actually at help.leaguerepublic.com — recovered)
- https://help.teamsnapforbusiness.com → transport error; https://www.teamsnap.com/teamsnap-for-business → 404 → TeamSnap dropped as sample after 2 failures
- https://support.demosphere.com → timeout; https://www.teamsideline.com → timeout → dropped
- https://challengermode.com returned only structured metadata (thin content) → used as boundary marker only
- SportyHQ /help docs and OTTO /help-center not fetched (time budget); Tier 2 pages used with reduced assertion strength

## Product A — LeagueRepublic

Evidence layer: A (direct observation, Tier 1 help centre + official site).

### Key observations

- Self-positioning: "The easiest place to run your sports league"; features listed as League Scheduler, Results & Statistics, Team & Player Registration, League Website, Website Integration (API). Market evidence page shows local/amateur football associations, pool, darts, bowling, netball, and esports leagues worldwide; FA FULL-TIME built on it "for league secretaries". [A]
- Help-centre collections map the working model: League Setup ("League structure — seasons and divisions, league general settings and standings configuration"), Scheduling, Scoring and Statistics, People and Roles, Tournaments ("group stage or knockout tournaments" — a distinct feature from the league), League Website, Integrations & API. [A]
- League structure: seasons and divisions are first-class ("Creating a new season", "Deleting a division", "Removing a team from a division"); division promotion and relegation is a standings-adjacent function. [A]
- Standings configuration is an explicit settings surface: "Changing the way the standings are ranked", "How do I award bonus points to a team?", "Can I manually adjust the standings?", "Division promotion and relegation". [A]
- Scheduling: schedule generator ("free schedule maker"), Template Scheduler vs Advanced Scheduler, options for creating a schedule, scheduling at a single venue, over several timeslots on the same day, venue sharing for teams, inter-division matches, byes, missing matches, creating a schedule from a spreadsheet, print/download. [A]
- Result entry and governance (article "How to enter results, approve and lock"): scores can be entered by league admins, team admins and referees; in singles leagues (darts/pool) players are team admins for themselves; approval option — if enabled, results are not shown and standings are not adjusted until the result is approved; locking option — locked results can no longer be changed by team admins (example given: lock the day after match day); entry channels: league admins via web (Results), team admins via web (own teams only), SMS (UK), referees via web for assigned matches (My Referee Reports). [A]
- The vendor's own guidance to organizers: delegate entry to team admins; "incorrectly entered scores and stats polices itself — the other team will tell you about it"; approval + locking as the trust mechanism. [A]
- Scoring/statistics: match sheets (print), match files, referee match reports, live results, individual player statistics, calculated statistics, Elo player skill ratings, player handicaps, sport-specific setups (e.g. cricket net run rate article), half-time/period scores setting. [A]
- People: roles and security, additional league administrators, team administrators, players on teams, roster update for a new season ("Updating the players on a team for a new season" — season-scoped rosters), registering players and teams into a league, player transfers between teams, multi-team players, player suspension, match referees/officials. [A]
- Misc: multi-language league sites, date formats, disabling venues, match previews/recaps, embeds/API for external sites. [A]

## Product B — LeagueApps

Evidence layer: A (direct observation, Tier 1 help centre) + Tier 2 marketing.

### Key observations

- Positioning: youth sports management platform for organizations running "clubs, camps, tournaments, and leagues"; platform features: Registration, Payments, Communications, Scheduling, Reporting, Facilities, Integrations, Websites; mobile apps for admins/coaches/parents/players (team schedules, RSVP, chat). [A/T2]
- Help-centre categories reveal the operating model: Organization Account, Member Management, Program Registration, Team Management ("copy and move players and teams"), Schedules & Standings ("Customize schedules, update standings and scores"), Payment Collection, Communication, Reporting, Facilities, Ecommerce, Website Design. [A]
- Container vocabulary: the org runs **programs**; program types include leagues, tournaments, camps, clubs. Standings rules are configurable site-wide or per program ("Standings Rules" settings; can be enabled in Preferences). [A]
- Standings rules article (direct): standings work "in tandem with game schedules"; configuration covers — Scoring Method (Game vs Match), Rankings basis (Point differential / Winning percentage / Cumulative match-based winning percentage), Point Values (adjustable win value, overtime win/loss values, forfeit deductions), Tiebreaker Rules in three stages (Primary/Secondary/Fallback; options incl. more points scored, more wins, fewer points against, more standings points, higher differential, head-to-head), Preferences (exclusions), Fields to Display (points scored/against/differential; "points for/against" from point values), and Game Types that count toward standings (Regular Season, Playoff, Championship, Quarterfinals, Semifinals, Final, Pool Play, Tournament — each with exclude toggles). [A]
- Score entry article (direct): "Game scores can be quickly updated by any level admin"; upon entering a score, standings update automatically according to standings rules; entry happens on the program's schedule page (per-game trophy icon); designated **scorekeepers** among program staff can enter scores in the Member Portal and mobile apps; team captains and designated staff roles can be allowed to edit scores for their games. [A]
- Game outcomes: Final, Final (OT), Cancelled, Rescheduled (triggers new date/time entry), Forfeit (specify which team won the unplayed game); option to omit a game's outcome from standings tabulation; results immediately reflected on schedule views for members. [A]
- Scheduling articles: program-level schedules, global calendar, schedule importer, "How do I schedule tournaments?" (tournament scheduling inside the platform), external teams (scheduling against teams not registered in the platform), creating and managing program schedules. [A]
- Tournament programs are a separate program type (pool play game type only available in tournament programs). [A]

## Product C — SportyHQ

Evidence layer: A/T2 (official feature pages; help docs not fetched — assertions kept moderate).

### Key observations

- Positioning: "web-based sports competition and membership platform" for facilities/clubs, governing bodies (Squash Australia, Tennis South Africa, UAE Badminton logos), schools; racket-sports focus; feature index: Tournament Management, Membership Management, Statistics & Reports, Court Bookings, Communication, User Accounts/Profiles, Rankings & Sanctioning, Event Registration & Forms, Website Builder, Calendar, API — and a distinct **Leagues** family: Team Leagues, Solo Leagues, Box Leagues, Ladders. [A/T2]
- Team leagues: "create seasons, divisions and teams; set team positions, assign captains and vice-captains, create customized scoring systems, set up your schedule, allow players (or just captains) to enter results, set court assignments". [A/T2]
- Scheduler: choose the night of week teams play, limits on teams scheduled per venue, schedule all divisions at once, custom round robin structures. [A/T2]
- Scoring systems: fully customizable; bonus points, penalty points; automatic notifications if a team hasn't entered its results within a desired time period. [A/T2]
- Result entry permission options: entire teams, only captains, or administrators; "as soon as a result is entered, the system updates instantly, sending result confirmations to players and updating league standings and various statistics". [A/T2]
- Live scoring (squash app, sport-specific): point-by-point entry from a phone; at match conclusion the score is automatically entered and standings updated. [A/T2]
- Availability/line-up loop: players set availability per round; captain sets the line-up online; team members notified. [A/T2]
- Season rollover: duplicate divisions/teams/players from the previous season; promote/relegate/add/remove teams. [A/T2]
- Box leagues (definition given by the vendor): "essentially a round robin, split up into divisions [boxes]; most box leagues require players to complete a series of matches against other players in their division, within a set time period (typically one month); at the end of each box cycle, players move up, down or remain unchanged based on their results"; flexible scoring; opt in/out per cycle; automatic promotion/demotion; players enter their own results with email notifications to both players so "errors can be resolved quickly"; box-internal group email. [A/T2]
- Ladders exist as a separate feature family from leagues (same for Solo Leagues). [A/T2]

## Product D — Demosphere (OTTO SPORT AI)

Evidence layer: T2 (official solution page; support site unreachable — assertions kept moderate).

### Key observations

- Positioning: youth-sports league management; "complete operating system for running youth sports leagues" (marketing wording — recorded, not adopted); audience: club directors, league managers, sport organizations; customer quotes from volunteer-run associations. [T2]
- Competition management & standings: "configure your competition… unique divisional structures; custom statuses, age groups and team types; granular permissions for members"; "prioritize tie breakers for each competition to ensure division standings meet your specific needs; display standings tables on team pages". [T2]
- Feature set named for the season loop: Customizable Registration; Smart, Flexible Scheduling ("blackout dates, coaching conflicts, field permits… master calendar… automatically notifies everyone when things change"); Team Management ("build balanced teams… clone last season's teams"); Communication Tools; Analytics & Reporting. [T2]
- Integrated league operations: "keep standings current, track disciplinary information, and advance teams through competitive play within the same system; referees report scores on the field; rosters sync automatically from club to league". [T2]
- Referee assigning: match referees to games by availability/license level/preferences; officials get notifications on assignment and schedule changes; officials submit post-match reports via mobile app; batch payments by competition/date range (1099 handling claimed). [T2]
- Data ownership/privacy posture for minors; role-based admin access. [T2]

## Boundary markers (not samples)

- **TeamSnap (TeamSnap ONE help)**: the consumer product's help center covers Account, Rosters, Schedules, Messages, Media, Live Streaming, Registration — the team-side sibling type (one team's people and events). League-side business docs unreachable. Confirms the seam: roster/availability/messaging for ONE team vs competition among MANY sides. [A, thin]
- **Challengermode**: self-describes as "competition management platform powering tournaments, matchmaking, ladders, and gamification" — tournament/ladder-first vocabulary with no league/season/division/standings framing on the fetched surface. Confirms that esports competition platforms lean tournament-first; league-running there is a variant at most. [A, thin]

## Cross-product Comparison

| Aspect | LeagueRepublic | LeagueApps | SportyHQ | Demosphere/OTTO |
|---|---|---|---|---|
| Primary customer | volunteer-run amateur leagues | youth sports organizations | racket-sport clubs/facilities/governing bodies | youth sports leagues/associations |
| Center of gravity | fixtures → results → standings | registration-led org platform with league programs | competition + membership for racket sports | youth league season operations |
| Season object | explicit ("Creating a new season") | implicit in programs; program-level schedules | explicit ("create seasons, divisions and teams") | explicit ("Seasons Created" metric; season loop framing) |
| Divisions | first-class | first-class | first-class | first-class ("divisional structures") |
| Member side | team; singles players act as own team admin | team (+ external teams for scheduling) | team OR individual (solo leagues, box leagues) | team (youth rosters) |
| Match programme | schedule generator, templates, spreadsheet import, byes, venue sharing | generator/importer, program schedules, global calendar | scheduler (round robin, venue limits, division-at-once) | generator with blackout dates/conflicts, master calendar |
| Result entry actors | league admins, team admins, referees; players in singles leagues | any admin level, scorekeepers, captains (scoped) | administrators, captains, players | referees report scores; admins |
| Entry channels | web, SMS (UK), referee reports, live results | console, member portal, mobile apps | web, live squash scoring app | mobile app (referee reports) |
| Result governance | approval + locking (explicit settings) | omit-from-standings toggle; outcomes incl. forfeit | notifications to both players for error resolution | disciplinary tracking |
| Outcome types | (article covers entry/approve/lock) | Final / Final (OT) / Cancelled / Rescheduled / Forfeit | draws/incomplete results configurable | (not detailed) |
| Standings rules | ranked-by changes, bonus points, manual adjustments | scoring method, ranking basis, point values, 3-stage tie-breakers, game-type exclusions, field display | customizable scoring systems, bonus/penalty points | tie-breaker priority per competition |
| Standings computed from results | yes (auto on approval if approval on) | yes ("update automatically according to the standings rules") | yes ("updating league standings" on entry) | yes ("keep standings current") |
| Registration/payments | team & player registration with Stripe | core (registration + payments platform) | team registration + payment online | core (registration-led suite) |
| Rosters/players | per-season rosters, transfers, suspension | copy/move players & teams | captains, line-ups, availability | rosters sync club→league; team building |
| Referees/officials | referee match reports; referee entry | (scorekeepers; not referee mgmt on fetched pages) | (not on fetched pages) | referee assigning + payments + reports |
| Communication | league site, email, social; SMS entry prompts | messaging platform; mobile apps | email to participants; box group email | email/text/push; automated reminders |
| Facilities/venues | venues, venue sharing, single-venue scheduling | Facilities category (bookings across spaces) | court bookings; court assignments | field permits, master calendar |
| Statistics | player stats, calculated stats, Elo, handicaps, sport setups | (reporting; not player-stat depth on fetched pages) | statistics & reports | disciplinary info |
| Tournaments | separate feature (group stage/knockout) | separate program type; tournament game types | separate feature | separate product (OTTO EVENT) |
| Publishing | league website, embeds, API | youth sports websites | website builder | standings on team pages; (websites in suite) |

Reading of the comparison:

- The four products realize the same spine — organizing body → season → divisions → member sides → match programme → results → computed standings — with different entry points (fixtures-first, registration-first, competition/membership, youth-suite). [B]
- Standings are always computed from recorded results according to configurable rules; no product treats the table as a hand-assembled artifact (manual adjustment exists only as an administrator overlay on top of computation). [B]
- Result entry is universally delegable downward (team admins/captains/players/referees/scorekeepers) with governance upward (approval/locking, notifications, forfeit semantics). [B]
- Registration, payments, rosters, communication, facilities, statistics, websites and referee tools appear in most but with very different depth and packaging — common mature structure, not definitional. [B]
- Tournaments and ladders are, in every product that has them, held out as separate features/types from leagues. [B]

## Canonical Model

### Level 0 — Defining Invariant

A League Management Platform is the league organizer's system of record for running a recurring competition among member sides. Four jointly-held structures; remove any one and the product stops being this Type:

1. **The league as competition container.** An organizing body whose member sides — teams or individual players — compete against each other under the organizer's rules, across a recurring competition cycle (the season). The sides are participants in the organizer's competition, not the organizer's customers. (Remove → club/team management, or an event operator with no standing membership = Tournament territory.)
2. **The season's match programme.** The set of match-ups each side must complete over the cycle — held as fixtures (pairing, date/time, venue), whether centrally generated by a scheduler or arranged by participants within defined windows (box-league style). (Remove → a results-and-rankings tracker or ladder, where ordering exists without a defined programme.)
3. **Recorded match results.** Each match-up's outcome captured into the competition's results record — by the organizer or by delegated entrants — carrying outcome semantics (played, forfeit, cancelled, rescheduled). (Remove → fixture/publishing tool with nothing to score.)
4. **Computed standings.** The running competition table derived from recorded results according to the league's configured scoring rules (point values, ranking basis, tie-breakers, what counts). The table is computed, never primarily hand-assembled; manual adjustment exists only as a governance overlay. (Remove → schedule + score log with no competition semantics.)

Jointly-held is load-bearing:

- 1 alone = club/team/roster management
- 2 alone = a schedule generator
- 3 alone = a score log
- 4 without 1–3 = a spreadsheet of points with no competition behind it
- 1+2 without 3+4 = fixture publishing
- 2+3 without 1+4 = individual result tracking
- 1+3 without 2+4 = score archive
- 1+4 without 2+3 = standings with no matches producing them

### Level 1 — Common Mature Structure

Present in most mature products; expected by the market; not definitional:

- Season management and rollover (duplicate last season's structure; promote/relegate between divisions)
- Divisions/sections as parallel competitions, each with its own table
- Rosters and player records scoped to the season; captains/team administrators; transfers; suspensions; eligibility
- Schedule generator (round-robin templates, timeslots, venue sharing, blackout dates, byes, inter-division matches) plus calendar views and print/export
- Delegated multi-channel result entry (web console, member portal, mobile apps, SMS, live scoring) by team admins/captains/players/referees/scorekeepers
- Result governance: approval before publication/tabulation, locking after a deadline, notifications for error resolution, forfeit/cancelled/rescheduled outcome handling
- Standings rules configuration: scoring method (game vs match), ranking basis (points / win percentage / differential), point values incl. bonus/penalty, staged tie-breakers (e.g. head-to-head, differential), game-type exclusions (regular season vs playoffs), display fields
- Player statistics and leaderboards (goals/points, calculated stats; in some sports ratings/handicaps)
- Public publishing: league website/pages with fixtures, results, tables, stats; embeds/API
- Communication: email/SMS/push to members; schedule-change and result notifications
- Team/player registration and payments

### Level 2 — Variant / Optional Structure

- Referee/official assigning and payments (module depth varies; a full referee-management system is its own Type)
- Facilities/venue management and court bookings (module or separate product)
- Governing-body layers: sanctioning, rankings, standardization across many leagues/clubs
- Racket-sport formats: solo leagues, box leagues (participant-arranged matches within cycles with promotion/demotion)
- Esports realizations (often tournament/ladder-first platforms; league-running appears as a variant)
- Tournament mode inside league products (knockout components, pool play)
- Ecommerce, sponsors, website builders, analytics/business reporting
- Federation/multi-organization administration

### Level 3 — Vendor-specific (research notes only)

- LeagueRepublic: powers the England FA's FULL-TIME league-administration system for league secretaries; Template vs Advanced Scheduler; UK SMS result entry (per-prompt cost); Elo-based player skill ratings; match previews/"match hub" recaps; multi-language league sites
- LeagueApps: "program" container with types (leagues/tournaments/camps/clubs); site-wide vs program-level standings rules; scorekeeper role in Member Portal/mobile; MLB & MiLB club support category; Elite Academy League member support category; FundPlay/NextUp community programs; Facilities module
- SportyHQ: Score Squash live-scoring app (squash-only, point-by-point → auto result + standings update); sponsor exposure features on league pages; box-cycle opt-in/opt-out machinery; governing-body customers (Squash Australia, Tennis South Africa)
- Demosphere/OTTO: OTTO PILOT AI assistant for admin Q&A; OTTO EVENT (SportWrench) tournament/ticketing product; University Athlete recruiting product; referee ACH payments/1099 handling claims

## Vendor-specific Findings

See Level 3 above; none of these are load-bearing for the Type. The FA FULL-TIME relationship (LeagueRepublic) is notable as market evidence that "league secretary" volunteer administration is the canonical user story, not a vendor story.

## Boundary Findings

- **vs Team Management Application (§28 sibling, unprocessed).** Team management centers on ONE team: its roster, availability, practices, and its own schedule/communication. A league platform centers on the COMPETITION among many sides; the team appears as one member side, and team-management features appear only as a delegated module (LeagueRepublic "Team Administrators"; OTTO "Team Management"; LeagueApps mobile team app). Remove-test: remove the multi-side competition and computed standings → Team Management Application; keep them → league platform. Keep both as separate Types.
- **vs Tournament Management Platform (§28 sibling, unprocessed).** A tournament is a one-off competition event (bracket/knockout, entrants assemble for the event); a league is a standing competition body whose sides play a programme over a season, with continuity across seasons (rollover, promotion/relegation). Market evidence: LeagueRepublic holds "Tournaments" as a separate feature; LeagueApps holds tournament programs as a separate program type (with pool-play available only there); SportyHQ separates Tournament Management from Leagues; OTTO sells tournaments as a separate product (OTTO EVENT). League platforms embed tournament mode as a component; the reverse (tournament products growing full league seasons) was not observed on fetched surfaces. Remove-test: remove recurring standing membership + season continuity → tournament platform. Keep both.
- **vs Sports Scheduling Platform (§28 sibling, unprocessed).** Scheduling is one step of the league loop; scheduling platforms exist where the schedule (constraint solving for venues/officials/availability) is the whole job. League platforms contain a scheduler as a feature (LeagueRepublic, LeagueApps, SportyHQ, OTTO all do). Remove-test: remove results/standings → Sports Scheduling Platform. Keep both.
- **vs Sports Registration Platform (§28 sibling, unprocessed).** Registration is the intake step that builds the member-side roster; registration platforms stop at intake/payments. LeagueApps and OTTO show the registration-led packaging, but the standings loop is what makes them league platforms. Remove-test: remove the competition loop → Sports Registration Platform. Keep both.
- **vs Sports Federation Management (§28 sibling, unprocessed).** A federation governs many clubs/leagues/competitions (sanctioning, governance, membership of organizations). Overlap exists: SportyHQ serves governing bodies directly; LeagueRepublic's customers include county/regional associations. The league platform runs ONE competition body's season; the federation platform administers many organizations. Flag for joint review when that leaf is processed.
- **vs Referee Management Platform (§28 sibling, unprocessed).** Referee assigning appears as a module (OTTO deep; LeagueRepublic light). Officials management at depth (licensing, self-service, payments at scale) is its own Type.
- **Ladder exclusion.** SportyHQ — the one sample with ladders — treats Ladders as a separate feature from its Leagues family: a ladder has ordering updated by results/challenges but no defined match programme. This supports keeping "the match programme" inside the defining core, with ladders outside the strict Type.
- **Esports boundary marker.** Challengermode's own framing (tournaments, matchmaking, ladders, gamification) shows esports competition platforms lean tournament-first; "league management" there is a variant posture, not the center.

## Uncertainties

- Historical check is conceptual (evidence layer C): no pre-digital source was fetched. Reasoning: the paper-era league secretary's toolkit — team entry forms, written fixture list, result cards phoned/posted in, hand-computed table published to the noticeboard/local paper — satisfies all four core structures at analog level (container, programme, recorded results, computed table). The definition is therefore abstracted above any specific technology (no scheduler, SMS, apps, or payments in the core).
- Registration/payments ubiquity: present in 4/4 samples in some form, but packaging varies (core platform vs Stripe option vs not-fetched). Held as common mature structure, not invariant.
- Whether "season" must be explicit in every implementation: all four samples model seasons/cycles explicitly; a continuous year-round league was not observed. Season kept inside core structure #1's "recurring competition cycle" rather than as a separate fifth invariant.
- OTTO/Demosphere evidence is Tier 2 only (solution page); support docs unreachable; features recorded with moderate confidence.
- TeamSnap's league-side ("for Business") capability depth is unknown (docs unreachable); used only as a team-side seam marker.
- Player-statistics depth (Elo, handicaps, sport-specific setups) is A-evidence for LeagueRepublic only; held product-specific/optional.

## Final Synthesis

The League Management Platform is the organizer-side system of record for a recurring multi-side competition. Its world: an organizing body runs competition cycles (seasons) in which member sides (teams or individuals) complete a defined programme of match-ups; each match-up's outcome is recorded into the results record — increasingly by delegated entrants (team captains, players, referees, scorekeepers) through web/mobile/SMS/live channels; and the standings table is continuously computed from those results under the league's configured scoring rules. Around that spine, mature products add season rollover, divisions, rosters, scheduling machinery, result governance (approval/locking, forfeits), statistics, publishing, communication, registration/payments, and officials/venue modules. The type is defined by the competition loop (programme → results → standings), not by any module; remove the loop and the product is team management, tournament operation, scheduling, or registration — all real neighboring Types.

The user story that anchors the Type across every sample: a (usually volunteer) league administrator sets up the season's divisions and member sides, produces the fixture list, lets teams/officials report scores, watches the table update itself, publishes fixtures/results/tables to participants, and rolls the league into the next season.
