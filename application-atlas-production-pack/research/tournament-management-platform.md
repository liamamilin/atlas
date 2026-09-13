# Research Notes — Tournament Management Platform

Research date: 2026-09-09

## Research Goal

Understand what a Tournament Management Platform actually is from real products: what objects exist inside it (tournament, division/category, entrants, brackets/draws/pools, matches, scores, standings/placements), who operates it, how a tournament actually runs from setup to final results, which rules govern progression and exceptions, and where the boundary lies against the neighboring §28 leaves (League Management Platform, Sports Scheduling Platform, Sports Meet Management, Sports Registration Platform, Team Management Application, Referee Management Platform, Race Management Platform) and against §26 Event Management / Event Registration.

## Initial Boundary (hypothesis before research)

- Core use: an organizer runs a **one-off, bounded competition event** — collects entrants, arranges them into a competition structure (brackets, pools, draws, pairings, fields), records results, advances winners / computes rankings, publishes final placements.
- Primary users: tournament organizer/director, co-organizers/staff, scorekeepers, participants (players/team captains), spectators.
- Nearest neighbors: League Management Platform (recurring season + standing membership — the league pass held tournaments as "one-off bracket" vs "season+standings"), Sports Scheduling Platform (bracket container vs calendar placement — forward flag), Sports Meet Management (bracket progression vs program of individually-run events — forward flag), Sports Registration Platform (intake vs competition entry — forward flag), Event Management Platform (attendee logistics vs competition structure).
- Unknowns at start: whether "bracket" is definitional (golf leaderboard-style tournaments suggest not); how containerization nests (tournament vs division vs event); how much scheduling/venue machinery is standard; how the esports realization relates.

## Research Questions

1. What is the tournament object, and what does it contain (divisions, brackets, pools, categories, multiple tournaments per event)?
2. How do entrants enter (public sign-up, invitation, manual add, team rosters), and what does an entrant record carry (custom fields, waivers, eligibility restrictions)?
3. Which formats exist, and how does the platform generate and manage the competition structure (bracket generation, byes, group stage → final stage, Swiss pairings, scoring rounds)?
4. What role does seeding play, and what are the mechanisms (manual, by rating/points, auto, filters)?
5. How are matches placed onto stations/courts/venues/times, and is scheduling definitional or optional?
6. Who records scores (organizer, participants, self-report with confirmation), and how are errors corrected (edit, reset, reopen)?
7. How do exceptions work: no-shows, forfeits, disqualifications, tied standings, late substitutions, refunds?
8. What is published (live brackets, leaderboards, results pages, streams, embeds, printing) and how does the tournament lifecycle run (draft → publish → registration → check-in → start → complete)?
9. How does the event/multi-tournament container work, and how does it relate to ticketing (attendee-shaped) vs registration (competitor-shaped)?
10. Boundaries: vs league (recurring season), vs scheduling (placement), vs meet (event program), vs registration (intake), vs event management (attendees), vs race (timed mass participation), vs referee (officials), vs team management.

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

1. **Challonge** — community/self-serve tournament hosting (esports + general competitions); bracket-first philosophy; free-to-paid consumer tiers; extensive knowledge base (Crisp KB, Tier 1).
2. **Battlefy** — esports organizer platform (organized play at scale); organizer-suite philosophy with strong participant self-service; Intercom help center (Tier 1).
3. **Golf Genius Tournament Management (TM)** — golf competition realization; scoring-first philosophy (formats library, live leaderboards); club/association/facility tier; product page + feature matrix (Tier 2; operational KB not fetched).
4. **PickleballTournaments.com** — pickleball tournament platform; public tournament marketplace + director tools; sanctioning by tours/associations; live surface with tournament statuses (Tier 2).

Cross-check anchors from sibling passes (no new fetches): LeagueRepublic / LeagueApps / SportyHQ / OTTO hold tournaments as **separate features or program types** from leagues (league-management pass, processed 2026-09-08); Challengermode self-frames tournament-first (same pass).

## Sources

**Challonge (Tier 1 KB + Tier 2 site):**
- Main site: https://www.challonge.com/ (formats, communities, events, pricing) [A/T2]
- KB root: https://kb.challonge.com/ (categories: Setup, Progression, Registration, Events, Account, Community) [A]
- Learn About Challonge Competition Formats: https://kb.challonge.com/en/article/learn-about-challonge-competition-formats-1f8j1cf/ [A]
- How to Create and Assign Stations: https://kb.challonge.com/en/article/how-to-create-and-assign-stations-j1xavx/ [A]
- Why Some Participants Go Straight to Round 2 (byes): https://kb.challonge.com/en/article/why-some-participants-go-straight-to-round-2-1r639q3/ [A]
- Rank and Tie Break Statistics: https://kb.challonge.com/en/article/rank-and-tie-break-statistics-1p5f7y4/ [A]
- Reporting Match Scores: https://kb.challonge.com/en/article/reporting-match-scores-17vxuyb/ [A]
- Registration category (participant management, sign-up page, seeding by rating, restrictions, paid tournaments/refunds): https://kb.challonge.com/en/category/registration-c1s5r6/ [A]
- Events category (create event, tickets, orders, check-in scan, permissions, payout account): https://kb.challonge.com/en/category/events-19qmfr5/ [A]
- Setup category (placement matches, match times, tournament check-in, team tournaments, custom fields, paid/Stripe, region locking, reset/reopen, hide bracket preview, templates, private messages, best-of labels, embedding, printing): https://kb.challonge.com/en/category/setup-426hye/ [A]

**Battlefy (Tier 1 help center):**
- Help center root: http://help.battlefy.com/en/ [A]
- Organizer Assistance collection: http://help.battlefy.com/en/collections/1517893-organizer-assistance (Organization Management, Tournament Creation, Tournament Management, Bracket Seeding sub-collections) [A]
- Player Assistance collection: http://help.battlefy.com/en/collections/9501718-player-assistance (Finding/Joining tournaments, Tournament Pages, Managing Teams, Game Day Instructions, Tournament Brackets) [A]
- Tournament Brackets collection (SE/DE guide, Swiss player guide, Ladder): http://help.battlefy.com/en/collections/9501729-tournament-brackets [A]
- Bracket Management collection (RR, Swiss + tie-breakers + drop, ladder, cumulative score reporting, DQ, manual score report, score reset, BYE, bracket settings/ordering, score confirmation, delete bracket): http://help.battlefy.com/en/collections/1517931-bracket-management [A]
- Single and Double Elimination Brackets: http://help.battlefy.com/en/articles/2616657-single-and-double-elimination-brackets [A]
- Setting up Match Check In: http://help.battlefy.com/en/articles/2806724-setting-up-match-check-in [A]

**Golf Genius (Tier 2 product pages):**
- Company/site root: https://www.golfgenius.com/ [A/T2]
- Tournament Management overview + TM Club vs TM Premium feature matrix: https://golfgenius.com/products/tm [A/T2]

**PickleballTournaments.com (Tier 2 live surface):**
- https://www.pickleballtournaments.com/ (tournament marketplace: cards with venue, dates, entry fee, player counts, statuses "Closing Soon / Playing Now / Reg. Closed / Advertised"; Now Registering / Now Playing filters; Create a Tournament; sanctioning partner filters; separate Leagues/Team Leagues/Clubs sites) [A/T2]
- Help center exists on Freshdesk (pickleballtournaments-help.freshdesk.com) — not fetched.

**Unreachable sources (dropped per network rules):**
- Toornament — 404 + JS shell + support transport error (3 attempts) → dropped
- Smoothcomp — 403 on root and /faq (2 attempts) → dropped
- Tournify — timeout ×2 → dropped
- tournamentsoftware.com — cookie wall ×2 (content unreachable) → dropped
- help.teamsnap.com — 404 on /en/, root has TeamSnap ONE KB without a Tournaments category → TeamSnap Tournaments product line not evidenced
- help.utrsports.com — transport error (1 attempt) → not pursued
- matchtennisapp.com — JS shell (1 attempt) → not pursued
- battlefy.com main site — JS shell; help center used instead

**Source-access limitation:** several major candidate vendors (Toornament, Smoothcomp, Tournify, tournamentsoftware.com) could not be fetched. All claims below rest on the four sampled products plus sibling-pass anchors. No claims are made for the unreachable vendors; generalization is marked B (cross-product within sample) or C (canonical inference) accordingly.

## Product Observations

### Challonge

Positioning (T2): "Simplified Tournament Management… EVERY GAME. EVERY SPORT." Web-based SaaS + API; communities as hub for tournaments and events; "36M+ brackets created". Free and paid tiers (numeric plan limits observed — see L3).

Key observations [A unless noted]:

- **Formats library** (formats article): six single-stage formats — Single Elimination (optional Bronze/3rd-place match), Double Elimination (winners'/losers' bracket; "Split Participants" option to start half the field in the losers' bracket), Round Robin (default single pass; 2x/3x option), Swiss (round 1 pairs first half of participant list against second half; later rounds pair similar records; no rematches; configurable round count; Median-Buchholz tie-break), Free For All (multiple participants per match, one or more advance; per-match participant count configurable), Leaderboard (display scores + overall rankings). Two Stage formats: Group Stage (SE/DE/RR/Swiss) → Final Stage (SE/DE/RR/Swiss); advancement count from groups must be a power of 2 for group SE/DE. Racing formats: Single Race (organizer inputs results per participant), Time Trial (open registration; participants log best times), Grand Prix (multiple races, cumulative points across rounds).
- **Byes** (byes article): when participant count is not a power of two, an initial qualifying round balances the bracket (lowest seeds play in; winners "advance to join" the top seeds). Byes cannot be avoided otherwise in elimination formats.
- **Tie-break statistics** (tie-break article): Match Wins, Game/Set Wins, Points Scored, Points Difference, Set Difference, Custom points system (organizer defines points per win/tie — e.g., match win and set wins), Wins vs Tied Participants (head-to-head), Median-Buchholz (Swiss), Manual Tie-Breaks (organizer assigns tie-break points for events outside the platform).
- **Stations** (stations article): "A station can be any location that a game or match will be taking place… courts, rinks, diamonds, tables, consoles, PCs, chessboards, dart boards, corn hole boards, swim lanes, you name it." Stations carry optional live-stream links and private details (room codes/passwords) shown to participants playing there. Matches assigned manually or automatically. Match times set against stations (setup category: "How to Set Times for Matches").
- **Score reporting** (reporting article): inline edit on the Bracket page, or a dedicated "Report Scores" page listing all matches grouped by round ("Tournament organizers managing large tournaments may find this view more useful"). Related articles: participant-side score reporting with match attachments; score reporting for matches in progress; editing match results; reporting forfeits by removing participants.
- **Entrants/registration** (registration category): public sign-up page (any account holder can register) and/or manual invitation by organizer ("make sure that everyone is in place before the competition starts"); participants can be assigned to matches, display names changed, removed, substituted "for last minute changes". Seeding by community rating is a Pro Community feature ("players ranked higher on a given leaderboard receive a higher seeding and therefore a more favorable round 1 matchup (or byes)"). Registration restrictions: organizer blocked list; country-specific events (region locking — setup category). Custom registration fields for waivers/agreements/media releases. Paid tournaments via Stripe ("accepting fees for registration, the venue, the prize pool"); refunds handled by organizer; payout account linked per event.
- **Team tournaments** (setup category): "Require participants to register as a team" — rosters.
- **Check-in** (setup category): tournament check-in required "minutes, hours, or even days before the actual start"; single page with all registered participants; supports substitution planning. Event-level check-in (events category): scanning an attendee's ticket checks them into the event **and every tournament they are signed up to participate in**.
- **Lifecycle / correction** (setup category): "Start Tournament" button on Bracket tab (registration category); **Resetting a Tournament** — "necessary to make large-scale changes" (add last-minute participant, add a 3rd-place match); **Reopen Tournament** — "reopen already finished tournaments, review past matches, and make the necessary adjustments without starting from scratch"; **Hide bracket preview** while registration is open ("bracket is already filling up… not yet definite and is still subject to change… reordering the grouping/seeding according to rank, or even shuffle for transparency").
- **Placement matches** (setup category): optional placement matches (3rd through 16th) for SE/DE "so rankings… can be clearly defined" — full-order completion beyond champion/runner-up.
- **Publication** (setup/registration categories): print bracket (printer-friendly image), embed bracket in external site, social image sharing, private messages/announcements to participants, best-of round labels, multi-lingual descriptions (Premier), contest overlays (bracket prediction "March Madness style", voting) [product-specific features].
- **Event container** (events category): "Creating events is an easy way to group tournaments for any larger scale competition"; dedicated tickets, logo/banner, embedded stream, centralized payment, event admins ("admins have access to everything: can publish your event, sell tickets, see orders, and more"), orders management, unpublish/delete. Tournaments organized inside the event via the Event Dashboard.
- **Community layer** (T2 + registration category): communities group tournaments/series for a competitive interest; ratings (Elo-based) and stats per game/sport.

### Battlefy

Positioning (T2, from help-center framing): esports tournament organizing; organizations help "players find your tournaments"; 62 organizer-assistance articles.

Key observations [A unless noted]:

- **Organization & staff** (organizer collection): Organizations as the publishing entity; staff roles "admins, moderators, or bracket managers"; ownership transfer; staff help "run and manage your tournaments".
- **Tournament creation states** (organizer collection): "Publishing a Tournament — Publish Tournament, Draft Mode, Private Tournament, Public Tournament" — draft/private/public states are first-class. Test tournaments ("easiest way to learn and test the flow"), duplication/templates ("quickly create a second tournament similar to a previous one"), embedding the tournament on the organizer's own website, join codes ("Control exactly who joins your tournament"), region locking ("If they are not within the set eligible territory or Country, they won't be able to join"), custom registration fields ("ask for more information"), translations.
- **Check-in machinery, two levels** [A]:
  - **Tournament check-in**: "Remind players to check-in to the tournament in order to be seeded" — check-in gates seeding.
  - **Match check-in** (match check-in article): "players will be given a notification that their match is ready and they need to go to the match to check in… You can set a timer to the check in so that if the opposing player or team does not check in within the allotted time, they will be automatically dropped from the tournament. **No scores can be reported by the players until both teams have checked in!**" Positioned as "let no shows resolve themselves".
- **Formats & seeding** (bracket/seeding collections): Single Elimination, Double Elimination ("If you lose a match, you're sent down to the loser's bracket… The winner of the tournament is the last one remaining without two losses on their record!" — grand finals bracket-reset explained), Round Robin ("Use round robin brackets when all teams and players must face each other"), Swiss (with tie-breaker format options; organizers can drop players from future rounds), Ladder brackets (beta access article notes Ladder and FFA as beta organizer features). Seeding: manual seeding into specific places, auto-seed, seeding by points, seeding filters ("Use seeding filters to decide who you seed onto your bracket"), per-format seeding guides (elimination/RR/Swiss).
- **Multiple brackets per tournament** (bracket settings/ordering, delete bracket articles): a tournament page lists multiple brackets in organizer-defined order — bracket = the competition structure within a tournament.
- **Scores** (bracket management collection): players report scores; organizers can manually report scores for players; score reset/change for wrongly inputted scores; **Score Confirmation** — "opt to enable Score Confirmation in your brackets, adding an extra step to ensure correct scores are reported"; cumulative score reporting brackets.
- **Exceptions** (bracket management collection): disqualify players/teams ("Handling player disputes"); BYE explained as a dedicated article; drop players from Swiss rounds.
- **Player side** (player collection): finding tournaments, tournament pages, joining (with questions), managing teams, game day instructions; contacting the organizer via the tournament page ("Contact tab. Who to contact for support and questions").

### Golf Genius Tournament Management

Positioning (T2): "The global leader in tournament management. Every year, over 10,000 clubs, associations, resorts, and tours trust Golf Genius to manage 40,000,000+ rounds." (marketing claim — recorded as positioning, not as fact.)

Key observations [A/T2]:

- **Audience**: private clubs, public courses, resorts, simulator facilities, golf associations; events, leagues, outings, trips.
- **Feature matrix** (TM Club vs TM Premium): full library of tournament formats; season-long competitions; league management; basic/custom event websites; TV leaderboards; custom printed materials; GHIN integration (handicap authority); Golf Hub (public search/registration of events); Premium adds mobile app with live scoring, live TV leaderboards, online registration, payment processing, open tee times, custom sponsor content, integration with club systems, text messaging; AI assistant (voice commands for tee sheet adjustments, player substitutions, handicap updates) [product-specific].
- **Live leaderboards as a global surface**: live leaderboards of events happening around the world; real-time standings on golfers' phones (Live Activities) [T2].
- **Reading** (A/T2 — marketing matrix, not operational docs): the golf realization centers on **competition formats + score entry + computed leaderboards** rather than bracket progression; entrants (fields) post round scores; the platform computes standings/placements; event pages/TV displays publish results. Note: the golf-course-management pass (processed 2026-09-08) recorded the seam from its side: GCM owns the tee sheet and blocks it for events; tournament software owns competition scoring/formats and integrates with club systems.

### PickleballTournaments.com

Key observations [A/T2]:

- **Public marketplace surface**: live cards for thousands of tournaments with venue city, multi-day date ranges, entry fee (multi-currency), player counts, and **status badges**: "Closing Soon", "Playing Now", "Reg. Closed", "Advertised"; filters "Now Registering", "Now Playing", featured. Statuses are visible lifecycle states of the tournament as a public offering.
- **Director side**: "Create a Tournament" entry; pricing page for organizers; club import/customization articles on the blog (Tier 2).
- **Sanctioning**: tournaments carry sanctioning by tours/associations (PPA, MLP, GPA, SSIPA, PPA Asia/AUS, etc.) — search filters by sanction partner; sanctioned vs non-sanctioned distinction (`load_sanctioned=true`).
- **Sibling network**: Leagues, Team Leagues, Clubs, Players, Rankings, Results live on **separate sites** in the same network — the vendor itself separates tournament hosting from league/club/rankings surfaces.
- Rating-linked entry observed on card titles (DUPR-rated tournaments; team-average/max rating constraints) [A/T2].

## Cross-product Comparison

| Dimension | Challonge | Battlefy | Golf Genius TM | PickleballTournaments.com | Strength |
|---|---|---|---|---|---|
| Tournament as bounded named competition | ✓ | ✓ | ✓ (event) | ✓ | B |
| Division/category/multi-structure inside one container | multiple tournaments per event; formats per tournament | multiple brackets per tournament | formats per event; events+leagues+outings on one account | skill/age/event-type divisions (draw structure) | B |
| Entrants = players or teams assembling for the event | ✓ sign-up page + invite + manual; team rosters | ✓ join + teams + join codes | fields (entry via registration Premium / open tee times) | ✓ registration with fee | B |
| Format configuration (structure of competition) | SE/DE/RR/Swiss/FFA/Leaderboard/Two-Stage/Racing | SE/DE/RR/Swiss/Ladder | full formats library (scoring formats) | draws/brackets per division | B |
| Seeding/placement into structure | manual + by rating (Pro) + shuffle/hide preview | manual/auto/by points/filters | (not observed) | (not observed directly; implied by draws) | B (2/4) |
| Match-level scheduling onto stations/courts | stations + times (optional) | not observed (online play; round timing) | tee-sheet integration (club systems) | court assignment implied, not fetched | B weak — optional |
| Results entry | organizer inline + bulk page; participant self-report | player report + organizer manual + confirmation | score posting (live scoring Premium; manual) | live results implied (results site sibling) | B |
| Progression/advancement computed | automatic bracket advancement; group→final crossover | automatic bracket advancement; Swiss pairing; drop | (n/a — leaderboard accumulation) | bracket advancement in draws | B |
| Standings/leaderboards/placements computed | standings per format + tie-breaks + placement matches (3rd–16th) | Swiss standings + tie-breakers | leaderboards (TV/phone) as the central output | final results/rankings | B |
| Exceptions: no-show/forfeit/DQ | forfeit via participant removal | match check-in auto-drop; DQ; BYE | (not observed) | (not observed) | B (2/4) |
| Score correction loop | edit, reset tournament, reopen finished tournament | reset/change score, score confirmation | (not observed) | (not observed) | B (2/4) |
| Publication: public page, live bracket/leaderboard, embed/print | ✓ embed/print/streams/social | ✓ public page + embed + streams | ✓ event websites + TV/phone leaderboards | ✓ public tournament pages + results | B |
| Registration/payment machinery | sign-up pages; Stripe paid tournaments; event tickets | join flow + custom fields + region locks | online registration + payments (Premium) | registration with entry fees, multi-currency | B |
| Staff roles / permissions | tournament admin grants; event admins | organization staff (admin/moderator/bracket manager) | (staff implied) | (not observed) | B (2/4) |
| Container hierarchy: event ⊃ tournaments | ✓ explicit (Event groups tournaments) | tournament ⊃ brackets (explicit); org ⊃ tournaments | account ⊃ events/leagues (implicit) | tournament ⊃ divisions/events (implied by card copy) | B — nesting direction varies |

**Reading of the matrix:** every product centers on (1) a bounded named competition, (2) entrants assembled into it, (3) a configured competition structure/format, (4) recorded results, and (5) system-computed progression/rankings and final placements. Everything else (seeding mechanisms, stations/court placement, check-in, payment, staff roles, publication surfaces) varies in depth or presence — standard but not definitional.

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

The tournament platform is the competition system of record for a **bounded competition event** whose defining core is exactly four jointly-held structures:

1. **The tournament as bounded competition container** — a named competition under organizer-configured rules (dates or a bounded window, entry conditions, division/category structure) whose entrants assemble for the event itself, not as standing members of a season. (Remove → generic event management, or a league season.)
2. **The configured competition format** — the organizer-selected structure that determines who meets whom and/or how performance is scored: elimination brackets, groups/pools with crossover, round-robin tables, Swiss pairings, ladders, or full-field scoring rounds. (Remove → a registration/roster tool.)
3. **The recorded result of each competitive unit** — per-match scores or per-entrant performances entered into the competition's results record by the organizer, delegated entrants, or officials. (Remove → an announcement/offer page.)
4. **Computed progression and placements** — outcomes drive continued participation (bracket advancement, group crossover, next-round pairing) and/or computed rankings (standings, leaderboards, final placements) per the configured rules, including tie-break semantics; always computed by the system from results, never primarily hand-assembled. (Remove → a bare results log or media leaderboard.)

Jointly-held is load-bearing: 1 alone = event management; 2 alone = a format generator below the platform bar; 3 alone = a score log; 4 without 1–3 = a leaderboard over nothing; 1+2 without 3+4 = a published draw nobody plays out; 3+4 without 1+2 = a results/rankings tracker.

### L1 — Common Mature Structure

Standard capabilities across the sampled products (B evidence):

- registration/entry machinery (public sign-up pages, invitations, manual add, team rosters, custom fields/waivers, entry fees)
- seeding/placement into the structure (manual, by rating/points, automatic; per-format)
- check-in at tournament and/or match level (no-show resolution)
- match placement onto named stations/courts/venues with optional times
- score entry by multiple actor types (organizer, participants, officials) with confirmation and correction loops
- exception semantics: byes, forfeits/walkovers, disqualification, drop-from-event, tied-standing resolution
- publication surfaces: public tournament page, live brackets/leaderboards, embeds, printing, streams
- staff roles (co-organizers, admins, bracket managers) and contact channels
- correction lifecycle: edit results, reset before/at start, reopen after completion
- containerization: event ⊃ tournaments or tournament ⊃ brackets/divisions; tournament series/communities

### L2 — Variant / Optional Structure

Depends on segment/sport/deployment:

- esports posture: online play, join codes, region locks, game-day instructions, match chat, game-specific features
- racquet/venue posture: draws per division, court/venue assignment, sanctioned competitions, rating-based entry (DUPR-style), multi-currency fees
- golf posture: scoring-format library instead of brackets, handicap-authority integration, tee-sheet integration with club systems, TV/phone leaderboards
- consumer/community posture: self-serve free tiers, communities/series, ratings (Elo-style), prediction/voting contests
- club/association posture: paid annual contracts, club-system integration, printed materials
- marketplace posture: public discovery/filtering of tournaments across organizers
- ticketing/attendee layer wrapped around tournaments (event container with tickets/orders)

### L3 — Vendor-specific (Research Notes only)

- Challonge: named format catalog (Free For All, Leaderboard, Time Trial, Grand Prix, Split Participants); Placement Matches 3rd–16th; Median-Buchholz tie-break; plan caps (256/512 participants; FFA 16/100 per match — plan-level, not asserted in final doc); Toxicity Checker; Elo-based Ratings; bracket generator; Crisp KB.
- Battlefy: organization staff taxonomy (admin/moderator/bracket manager); match check-in timers with auto-drop; Score Confirmation toggle; Ladder/FFA beta; join codes; region locking as registration gate.
- Golf Genius: GHIN integration; Golf Hub; TM Club vs TM Premium split; AI assistant (voice-driven tee sheet adjustments/substitutions); Live Activities lock-screen leaderboards.
- PickleballTournaments.com: sanction-partner filters; SSO network of sibling sites (Leagues/Team Leagues/Clubs); status badges vocabulary ("Advertised", "Playing Now"…).

## Vendor-specific Findings

See L3 above. Cross-check anchors: LeagueRepublic/LeagueApps/SportyHQ/OTTO all hold tournament machinery as separate features/program types/products from their league cores (league pass, 2026-09-08). Challonge itself separates "Tournaments" from "Events" (attendee-shaped ticketing containers). PickleballTournaments separates Leagues/Team Leagues onto sibling sites. The market's own categorization keeps the tournament as a distinct unit.

## Boundary Findings

**vs League Management Platform (processed 2026-09-08) — keep-both; discharges that pass's forward flag from this side.**
The league is a standing competition body whose member sides play a programme across a recurring season, with continuity between seasons and computed standings as the season's running table. The tournament is a bounded event whose entrants assemble for the event, with format-driven progression toward final placements. Market evidence on both sides: every sampled league product holds tournaments as a separate feature/program type (league pass); the sampled tournament products hold no season/standing-membership machinery (Challonge communities/series are episodic groupings, not seasons; Grand Prix multi-race rounds are within one container). Formats overlap (RR appears in both) — the discriminator is standing membership + season continuity, not format. Ladders (ongoing challenge ordering without a bounded event) excluded from both cores by the market's own categorization (SportyHQ lists Ladders separately; league pass recorded the same).

**vs Sports Scheduling Platform (processed 2026-09-09) — keep-both; discharges that pass's forward flag.**
The scheduling platform owns the competition calendar: producing and holding the placement of games into dates/venues with constraint machinery, and propagating changes. The tournament platform owns the competition container: the bracket/draw and what a result does to it. Match placement inside tournament products (Challonge stations + times; court assignment in racquet products; tee-sheet integration in golf) is a component of running the event, not the platform's defining act. Conversely, bracket features in scheduling products are placement tools, not progression records (scheduling pass's own framing). The seam is container-vs-calendar and both passes agree.

**vs Sports Meet Management (processed 2026-09-09) — keep-both; discharges that pass's forward flag.**
A meet is a program of individually-run events (each event runs independently; entrants declared per event; per-event results with places). A tournament is a progression structure over head-to-head competition (the outcome of one match determines continued participation in the next). No structural overlap: brackets have no lane/flight machinery; meets have no bracket advancement. Championship-series/qualifying features (advancement across events) sit between the two as packaged capability, not center — consistent with the meet pass's note. Note a soft edge: golf-style full-field tournaments (no head-to-head) are closer to "one repeated event + cumulative leaderboard" — they still satisfy the tournament L0 via container + format + results + computed placements, but head-to-head progression is NOT definitional. The tournament/meet seam therefore runs on the entrant-assembly and format semantics: in a meet the program defines events; in a tournament the format defines the entrants' path.

**vs Sports Registration Platform (processed 2026-09-09) — keep-both.**
Registration there centers the signup transaction into a season/division participation structure; here entry is one step into the tournament loop, bound to the competition container (entry carries format placement, seeds, check-in, division). Tournament products bundle registration heavily (all four samples), and registration suites bundle tournament offer shapes (registration pass) — bundling is symmetric; the center differs.

**vs Event Management Platform / Event Registration Platform (§26) — keep-both.**
Event management centers attendee logistics (tickets, orders, attendance check-in). The Challonge Event feature is exactly attendee-shaped (tickets, orders, scan-to-check-in) wrapped around competitor-shaped tournaments — the vendor keeps the two shapes distinct in its own model. A tournament's registration is entry-as-competitor (carries division/seed/bracket consequences), not attendance.

**vs Race Management Platform (researched sibling) — keep-both.**
A race is a single mass-participation timed event with individual finishers; timing is the instrument. Tournament products' racing formats (Challonge Single Race/Grand Prix) import results and allocate points — they are result-consumers, not timing systems; consistent with the race/meet/timing record-vs-instrument split.

**vs Referee Management Platform (processed) — keep-both; consistent with that pass's boundary row.**
The referee platform assigns people to games; the tournament platform consumes the same games' results and sometimes carries an officials input field, often handing off to a referee platform.

**vs Team Management Application (processed) — keep-both.**
One team's own life (roster, schedule, comms) vs a competition among many entrants. Tournament entrants may be teams, but the platform centers the competition, not any team's internal life.

**vs Sports Federation Management (unprocessed neighbor)** — sanctioning (PickleballTournaments sanction filters) shows federations granting sanction to tournaments; the governing-body umbrella may subsume competition administration. Joint review recommended when that leaf is processed (same flag as the league pass).

**Esports competition platforms** (Battlefy sampled; Challengermode flagged by the league pass) self-frame tournament-first — they are a market realization of this same Type (online posture), not a separate Type.

## Historical / Market-Sample Check (§24)

Paper-era check (conceptual): a tournament director with entry forms (entrants assembling for the event), a hand-drawn bracket wall chart (configured format), penciled scores per match (recorded results), winners advancing up the chart to a champion and ordered final placements (computed progression/placements) — satisfies all four legs with no software. Chess Swiss pairings via cards, golf scorecard leaderboards, regional judo brackets — all fit. Modern conveniences (online registration, live scoring, check-in, seeding-by-rating, payment, streams) are all absent from the paper check → standard, not definitional. Older/regional products (desktop Swiss pairing programs, club ladder software for ongoing play, federated tennis draws) fit the definition via the four legs; ongoing ladders without a bounded event fall outside toward league/ranking territory — noted as a boundary edge, not a failure of the definition.

## Uncertainties

- Toornament, Smoothcomp, Tournify, tournamentsoftware.com unreachable — no product claims for them; the L1 set rests on four products (B layer). Breadth beyond the sample (e.g., tennis director tools, track wrestling) is canonical inference (C).
- Golf Genius operational documentation not fetched (product page + feature matrix only) — golf claims held at T2 strength; no operational-parameter claims.
- Whether match/court-level placement scheduling is "common" vs "optional" across the wider market: observed as optional in Challonge (stations), present via club integration in golf, not observed in Battlefy — treated as common-but-not-definitional, with soft confidence.
- Seeding mechanisms vary; seeding-by-rating is a paid feature at Challonge and core at Battlefy — mechanism details are L2/L3.
- Precise participant caps, check-in timer defaults, fee percentages: observed only at plan level on one product (Challonge) — kept in L3, none asserted in the final document.

## Final Synthesis

The Tournament Management Platform is the **competition system of record for a bounded competition event**. Its defining core is four jointly-held structures: the tournament container (entrants assemble for a named event under organizer rules — not standing season membership), the configured competition format (bracket/draw/pools/pairings/scoring structure determining who meets whom and what counts), recorded results of the competitive units, and system-computed progression and placements (advancement and/or rankings per configured rules, including tie-breaks). The market realizes one Type in poles: esports/online organizer suites (Battlefy; Challengermode self-framed tournament-first), self-serve community hosting (Challonge), sport-specific scoring-first systems (Golf Genius TM), and sport-specific marketplace+director platforms with sanctioning (PickleballTournaments.com). League platforms hold tournament mode as a separate feature — the market itself keeps the two competition containers distinct. Standard (not definitional): registration/payments, seeding, check-in/no-show machinery, station/court placement, live publication, staff roles, correction loops. Boundaries all held: league (season+standing membership), scheduling (calendar placement), meet (event program), registration (intake), event management (attendees), race (timed mass participation), referee (officials), team management (one team's life).
