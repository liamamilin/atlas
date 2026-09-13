# Research Notes — Youth Sports Management

Research date: 2026-09-10. Methodology: update-v1 v1.1.

## Research Goal

Understand what software sits under the directory leaf "Youth Sports Management" (§28 Sports & Recreation, between "Sports Membership / Licensing Platform" and "School / College Athletics Management"): what the system is ultimately the record of, who operates it, what the season operation looks like end to end, which structures repeat across the market, and where the boundaries lie against the heavily overlapping §28 siblings — especially Sports Registration Platform, Sports Club Management, Sports Academy Management, League Management Platform, Team Management Application, and Sports Scheduling Platform.

This pass must DISCHARGE pre-hung joint-review flags from three processed sibling passes:

1. **sports-club-management (2026-09-09)**: "vs youth-sports-management — proposed discriminator = registration/season-led (the season's sign-up is the center; rec leagues, volunteer boards) vs membership/competition-led (the standing member organization fielding teams), heavy product overlap expected (TeamSnap serves both explicitly), joint review recommended at that pass."
2. **sports-academy-management (2026-09-09)**: "vs youth-sports-management — youth-sports organizations are registration/season-led (leagues, rec programs, volunteer boards); academies are program/training-led."
3. **sports-registration-platform (2026-09-09)**: "vs youth-sports-management (org-led) — the organization's whole year-round operation — teams, schedules, volunteers, presence — with registration as its busiest step; there the signup transaction and its roster are the center. Directional test: strip the org's year-round operation machinery (schedules, teams, volunteer coordination, website-as-presence) → registration platform; make the organization's own operation the center → Youth Sports Management."

## Initial Boundary (hypothesis before research)

- Hypothesis: the operator-side system of record for youth sports organizations — leagues, rec associations, community clubs, travel programs — that runs the organization's seasonal participation operation: registering players (and volunteers), forming divisions/teams, building the season schedule, coordinating families, and collecting season fees. The market self-label "youth sports management" is carried by a distinct product family (Sports Connect, TeamSnap, LeagueApps, TeamLinkt, SportsEngine, Jersey Watch, Crossbar, PlayMetrics) that overlaps heavily with the club/registration labels.
- Nearest neighbors: Sports Registration Platform (the signup transaction), Sports Club Management (the standing member organization), Sports Academy Management (tuition programs), League Management Platform (competition between sides), Team Management Application (one team's life, unprocessed), Sports Scheduling Platform (scheduling machinery, unprocessed), Tournament Management Platform (processed), School/College Athletics Management (processed — school-affiliated), Sports Federation Management (processed — governance register), Sports Facility Management / Sports Court Booking (facility inventory), Sports Membership / Licensing Platform (processed — renewable member relationship + credential), Camp Management System (§29).
- Key uncertainties going in: (1) whether "season" or "registration" is the better center; (2) whether the youth/guardian structure is definitional or just dominant; (3) whether money (season fees) is definitional here as it is in club management; (4) whether in-house league play (scores/standings) is definitional or variant.

## Research Questions

1. What is the organization's participant population of record, and how do minors/guardians appear in it?
2. What is the operational container of the org's year — season, program, or something else — and what does it hold?
3. How does intake work (registration in-product vs imported/linked teams), and what does the org do with the intake?
4. How are divisions/teams formed and rosters built? What rules bind players to seasons/teams?
5. What does "running the season" consist of on the system: schedule, communication, scores, officials, facilities?
6. Where does money sit — definitional or standard?
7. What does the family/guardian side look like, and what does the team/coach side look like?
8. What safety/compliance machinery exists (volunteer vetting, minor-data posture)?
9. How do governing-body relationships appear (data sync upward, verification)?
10. Where exactly do the seams to registration platform / club management / league management hold?

## Representative Products

Selected for market representativeness, doc completeness, different product philosophies, and different customer levels:

1. **Sports Connect (Stack Sports)** — the NGB-affiliated enterprise pole; self-labels "Websites, Registration, Youth Sports Management Tools"; official technology partner of large US youth governing bodies (US Youth Soccer, Little League, Pop Warner, USA Football, AAU, US Lacrosse); serves National & State Governing Bodies, Local Clubs & Leagues, and Parents/Coaches/Athletes.
2. **TeamLinkt** — the free/no-platform-fee volunteer pole; self-labels "Easy-to-Use Youth Sports Management Software"; positions on registration + scheduling + communication for leagues, clubs & associations, governing bodies, parks & recreation; strong help center.
3. **Crossbar** — the parent-volunteer-built mid-market pole; self-describes as "Sports Management Platform — Clubs • Leagues • Facilities • Tournaments" for "everything you need to manage youth sports"; deep Intercom help center with role-scoped resource collections (Registrar, Scheduler, Staff, Finance, Coach & Team Staff, Volunteer Management, League Management).
4. **LeagueApps** — the youth-sports-as-business operator pole; self-labels "Youth Sports Management Platform — the tools to manage your programs"; roles Admins/Coaches/Parents; program types Camps/Clubs/Leagues/Tournaments; revenue-growth orientation. Registration-module detail cross-referenced from the 2026-09-09 sports-registration-platform pass's help-center fetches.
5. **TeamSnap (for Business / Clubs & Leagues)** — the consumer-app-descended giant pole; self-labels "club & league management" (the club pass recorded the overlap verbatim); Admin Playbook category structure fetched fresh this pass; operational mechanics cross-referenced from the 2026-09-09 sports-club-management pass's help-center evidence.

Deliberately NOT used as primary samples: SportsEngine (unreachable 403 ×2 in the registration pass; its pole evidenced only indirectly — TeamLinkt runs migration promos targeting SportsEngine switchers; no SportsEngine claims made); PlayMetrics (JS-rendered, unreachable per the club pass; now parent of both Sports Connect and Crossbar per their home pages — market-consolidation note); Jersey Watch (marketing-tier evidence only, recorded in the registration pass; used here only as a self-label witness); Spond/SportEasy/Thrive4 (European pole belongs to the club pass's sample).

## Sources

Fetched this pass (2026-09-10):

- Sports Connect — home: https://www.sportsconnect.com/ ; clubs & leagues page: https://sportsconnect.com/local-clubs-and-leagues/ ; parents/coaches/athletes page: https://sportsconnect.com/parents-coaches-athletes/
- TeamLinkt — home: https://www.teamlinkt.com/ ; Help Center root: https://help.teamlinkt.com/en/ ; Managing Season collection: https://help.teamlinkt.com/en/collections/11072913-managing-season ; "Create a New Season": https://help.teamlinkt.com/en/articles/4938670-create-a-new-season
- Crossbar — home: https://www.crossbar.org/ ; Help Center root: https://help.crossbar.org ; Registrar Resources collection: https://help.crossbar.org/en/collections/3076580-registrar-resources ; "Registrar Overview": https://help.crossbar.org/en/articles/9860089-registrar-overview ; "Creating & Rostering Your Teams": https://help.crossbar.org/en/articles/8613107-creating-rostering-your-teams
- LeagueApps — "Youth Sports Management Platform": https://leagueapps.com/youth-sports-management-platform/
- TeamSnap — Admin Playbook root (category structure): https://teamsnap-admin-playbook.helpscoutdocs.com/

Cross-referenced from prior passes (recorded there with their own fetches):

- sports-registration-platform pass: LeagueApps registration feature page + Program Registration help articles; Jersey Watch self-label page; SportsEngine unreachable.
- sports-club-management pass: TeamSnap help center + Admin Playbook operational content; Spond Club; SportEasy; Thrive4.

Evidence layers used below: **A** = directly observed on a fetched official source for a named product; **B** = cross-product commonality across the sample; **C** = canonical inference from comparison and boundary reasoning.

## Product Observations

### Sports Connect (Stack Sports)

Key observations (Tier 2 product pages; no operational help center fetched this pass):

- Self-label (A): "SPORTS MADE EASY — Websites, Registration, Youth Sports Management Tools, & More!" Feature list: Mobile First Registration, Professional Websites, Payment Processing, Team Management, Reporting, Scheduling, Communication Tools, Premium Support, Online Fan Wear, Safety & Compliance.
- Audience segmentation (A): "Who We Serve" = National & State Governing Bodies / Local Clubs & Leagues / Parents, Coaches, & Athletes. Positioning: "Join the thousands of youth sports programs nationwide using Sports Connect to manage the full lifecycle of their organization."
- Clubs & leagues page (A): "Easy Online Registration — Player and volunteer registration built for any device; Manage any sport, event, or level of play; Safe and secure online payment processing; Family dashboard for easy signups season after season." "Your Entire Season Under One Roof": Scheduling ("Quickly create game and practice schedules, manage your league calendar, and auto notify parents and coaches"); Team & Volunteer Management ("Auto assign rosters in a few clicks, quickly communicate rosters, and verify players and volunteers in one place"); Communication Tools ("Targeted emailing with auto list management, use professional templates"); Reporting & Financial Management ("customize reports, and financial reconciliation, all in real time"). Plus fan wear, fundraising, league websites, data insights.
- Youth structure evidence (A): "Family dashboard for easy signups season after season"; player AND volunteer registration as the two intake populations; "verify players and volunteers in one place"; Children's Privacy Policy in the footer legal set.
- NGB layer (A): per-sport pages name official partnerships — US Youth Soccer/U.S. Soccer with "integrations to the USSF National Data Center"; Little League and PONY "with pitch count tracking to simplify your season"; USA Football, Pop Warner, AAU, US Lacrosse ("easy scheduling and automated team creation"). "Stay compliant" machinery exists at the governing-body interface; "automatic verification for NGBs" is LeagueApps's phrasing of the same market behavior (see below).
- Suite cross-sell (A): Stack Officials (scheduling, paying, managing officials), Stack Tourney (tournaments), TeamApp (team communication), TeamInn (event housing), Gameplan, CaptainU (recruiting) — the org system is one member of a vendor family; these are adjacent products, not this Type's core.
- Testimonial language (A): "easily manage hundreds of registrations year after year, including all the pains that come with a youth sports program"; "we run multiple registrations for our regular season, camps, and fundraisers all at the same time."

### TeamLinkt

Key observations (home page Tier 2 + help center Tier 1):

- Self-label (A): "Easy-to-Use Youth Sports Management Software — TeamLinkt unifies registration, scheduling, and communication for sports organizations. No platform fees, no contracts." Tagline: "Sports Registration, Scheduling, and Admin. Handled."
- Audience set (A): Programs "For Leagues / For Clubs and Associations / For Governing Bodies / For Tournament Organizers / For Parks and Recreation / For Multi-Location Operators." Feature list: Registration, Website Builder, Team App, Scheduling, Fundraisers, Game Sheets, Tournaments, Sponsorship Matching.
- The season as operational container (A, help article "Create a New Season"): "Seasons allow you to silo your data across years, sports, programs etc. Adding a season will provide a new canvas for: Registration Forms and Participants; Teams and Rosters; Schedules, Scores, Standings, Statistics; Transactions." And: "previous season structures and teams can be copied during season creation." This single sentence enumerates the season's contents — intake, formation, schedule+competition, money — and the rollover mechanism.
- Season-level operations (A, "Managing Season" collection, 24 articles): Create/Clone/Edit a Season; Link Existing Teams to your League; Toggle Between League and Team Account Dashboard; Share Registration Information with Team Admins; Find a Team's Join Code; Display Practices on Website; Registration for Small Groups; Request Payments on a Pay Later Form; Create another Organization; Custom Invoices; refunds ("Why can't I issue a refund?"); payment plans; Association Member Additional Info; Upload a Document; Send an Email; "What is a Dispute"; Disable Team Rosters.
- Season promise in market language (A, home): "Your registration opens & payments come in quickly (build custom forms, collect online payments, implement waitlists)"; "Schedules are built & easily published in days (set facility availability, balance game counts, conflict-free schedules)"; "Every announcement reaches everyone instantly." Family-side: "Never Miss a Game, Practice, or Result — Schedules, attendance, scores, standings, and more keep everyone up to date automatically"; "Urgent Updates Sent in Real-Time — game reminders, schedule changes, and announcements are delivered instantly to every member"; "One Place for Every Conversation — Team chat replaces scattered texts and email chains."
- Help-center shape (A): collections = Getting Started; Registration & Forms (29 articles: payments, payment plans, data collection); Teams and Rosters (17: "Team Management and Rosters for App Usage"); Website Builder; Schedule (15: "Create & manage stats, scores, standings for your events"); Managing Season (24); Team App (35); Bundles & Add-ons; Officials & Gamesheets (3); Other Features; Video Library.
- Org shape evidence (A): "Toggle Between League and Team Account Dashboard" — the organization dashboard and the team app are two surfaces of one system; "Link Existing Teams to your League" and "Importing Team Rosters" — intake of pre-formed teams exists alongside registration-led formation.
- Migration posture (A): migration promos explicitly target switchers from SportsEngine and Sports Connect ("$3,000+ in Savings Switching From SportsEngine or Sports Connect") — market-structural evidence that these products are one interchangeable population.

### Crossbar

Key observations (home Tier 2 + help center Tier 1):

- Self-label (A): "Sports Management Platform — Clubs • Leagues • Facilities • Tournaments"; "Everything you need to manage youth sports in one, easy-to-use, platform." Origin story: "We have first-hand experience managing youth sports organizations, so we built the platform we needed to make our own lives easier as parent volunteers."
- League product (A): "Everything you need to run a league including multiple registration types, scores, standings and playoff brackets. And it automatically syncs with our club product!"
- Registration machinery (A, Registrar Resources + "Registrar Overview"): registration types = Programs ("best for full season, camp, tryouts, or single-session type events"), Leagues (player-registration league AND team-registration league), Memberships ("monthly, annual or one-time"), Tournaments ("accept new Team registrations"), Forms ("collect basic info from web users or members — function similarly to Google Forms/Survey Monkey"). Recommended two-tier structure: registration ("Travel Season", "Your League") → Season ("Fall 2024", "2024-2025"). "The season becomes the foundation from which your teams are created, rostered, and managed throughout the year." Signups section per registration season: filter, email the full or filtered list, export CSV.
- Formation and rostering (A, "Creating & Rostering Your Teams"): teams created inside a Season; team attributes = Type (Team vs Group — Groups for "Position Groups, Skills Clinics" with no team contact info/feed/chat/roster in the app; "Groups & Teams are scheduled the same way"), Age Level (drawn from the season's Age Levels for Program Registrations or Divisions for League Registrations), Skill Level, Team Name/Abbreviation, Scheduling Details ("Touches & Allocation… upload code (used with the Scheduler)… scheduling limitations"). Rostering: players default to the team's Age Level, can be rostered up or down an age group; a player can be on more than one team; "Players do need to be signed up in the same season where the teams are created in order to be rostered to that team." The Offer system handles tryout-based admission ("If you need to utilize the Send Offer option for Programs that have tryouts").
- Documents and completion (A): "Player Document Upload & Completion", "Document Signature & Completion", session/program waitlists, registration insurance.
- Role-scoped help (A): collections for Registrar, Scheduler, Staff, Finance, Coach & Team Staff, Webmaster, Volunteer Management, Facility Managers, League Management, Importing League Schedules (8 articles — "automatically import your teams' game schedules directly from league websites"), Mobile Application, Admin.
- Consolidation note (A): Crossbar home banner: "Crossbar is now part of PlayMetrics!" — same parent as Sports Connect ("Sports Connect & PlayMetrics: A new era for youth sports!").

### LeagueApps

Key observations (youth-sports platform page Tier 2; registration help detail from the registration pass):

- Self-label (A): "Youth Sports Management Platform — The tools to manage your programs." Hero: "Take Your Youth Sports Organization to the Next Level — Operate more efficiently, build stronger relationships with your members, and grow your business." "Manage your clubs, camps, tournaments, leagues, and facilities with the best youth sports management platform that is designed for any sport."
- Structure (A): Platform features = Registration, Payments, Communications, Scheduling, Reporting, Facilities, Integrations. Roles = Admins, Coaches, Parents. Program types = Camps, Clubs, Leagues, Tournaments. Capability bullets: "Advanced team management capabilities; Flexible schedule management; Seamless facility and bookings management; Flexible registration flows and rules; Family, parent, and player data management; Multiple program types and sports supported."
- Youth/family structure (A): "Family, parent, and player data management"; roles page set explicitly includes Parents; "Easy-to-use member portal and mobile app"; dedicated "Youth Registrant Privacy Policy" and "Youth Registrant Terms of Service" in the footer.
- Compliance (A): "Stay compliant with automatic verification for NGBs"; "Integrations with safety and compliance tools."
- Business orientation (A): "Drive Revenue Growth — with reliable, flexible invoicing, and payment options you stay organized and collect more fees on time so you can drive revenue all season long" (payment plans, Stripe gateway, cards + ACH, ecommerce in registration flow, registration fee insurance); "Full ownership and control of your data; Role-based security"; "Evaluations with actionable player development insights."
- Registration detail (A via cross-reference, sports-registration-platform pass): platform-run program registration with seasons/divisions, custom questions, waivers, payments; Help Center Program Registration category documented there.

### TeamSnap (for Business / Clubs & Leagues)

Key observations (Admin Playbook category structure fetched fresh; operational mechanics from the club pass's help-center evidence):

- Admin Playbook categories (A): TeamSnap for Business (40); TeamSnap for Clubs & Leagues (16); TeamSnap Tournaments (43); Website Builder (46); Season Management & Organization Structuring (23); Invoicing, Registration, and Financials (82); Roster Profile & Member Management (62); Communication (27); Scheduling and Availability (9); Reporting (8); Partnerships & Integrations (19); Security & Privacy (5); Health & Safety (2).
- The category names themselves are structural evidence (A): the org-side system is organized around season management + organization structuring, registration/financials, roster/member management, communication, scheduling/availability — with the team/consumer app, tournaments, and websites as adjacent product lines.
- Overlap witness (A, recorded by the club pass): TeamSnap ONE self-labels "club & league management" while its "who we serve" spans youth sports, rec leagues, club programs, camps, high school, and travel teams — the same product sold into the club label and the youth-sports label.

## Cross-product Comparison

| Dimension | Sports Connect | TeamLinkt | Crossbar | LeagueApps | TeamSnap |
|---|---|---|---|---|---|
| Self-label | "Youth Sports Management Tools" | "Youth Sports Management Software" | "manage youth sports in one platform" (Clubs/Leagues/Facilities/Tournaments) | "Youth Sports Management Platform" | "club & league management" (overlap witness) |
| Org population | players + volunteers registered; family dashboard; "verify players and volunteers" | registration forms & participants; association members | players (program/league/membership registrations); team staff; volunteers | "Family, parent, and player data management"; roles Admins/Coaches/Parents | roster profile & member management; parents as member contacts |
| Season container | "signups season after season"; "Your Entire Season Under One Roof" | season = silo: forms/participants, teams/rosters, schedules/scores/standings/stats, transactions; clone season | Program → Season two-tier; "the season becomes the foundation from which your teams are created, rostered, and managed" | program types incl. Leagues; season set-up via scheduling module | Season Management & Organization Structuring category |
| Formation | "auto assign rosters in a few clicks" | teams & rosters per season; link existing teams; import rosters | divisions/age levels/skill levels; roster up/down; multi-team players; same-season eligibility rule | team management capabilities across program types | organization structuring → programs → teams (club pass) |
| Schedule | "quickly create game and practice schedules, manage your league calendar, auto notify parents and coaches" | build & publish schedules; balance game counts; facility availability | scheduler resources; touches/allocation; import league schedules | flexible schedule management module | scheduling & availability (team-side; org-side structuring) |
| Scores/standings | n/e at fetched tier (sport pages mention pitch counts, competition tools) | "stats, scores, standings" in season canvas; game sheets | "scores, standings and playoff brackets" (league product) | leagues program type; evaluations | tournaments product line adjacent |
| Family surface | parents/coaches/athletes served; family dashboard | team app: schedules, attendance, scores, chat, reminders | parent-volunteer built; mobile application; coach & team staff resources | member portal and mobile app; parents role | parent/consumer app (club pass) |
| Money | payment processing; financial reconciliation | online payments, payment plans, pay-later, invoices, refunds (Stripe) | finance resources; registration insurance; tuition auto-payments testimonial | payments/invoicing/plans/ACH/ecommerce/fee insurance | invoicing/registration/financials (82 articles) |
| Safety/compliance | "Safety & Compliance"; verify players and volunteers | document upload; disputes | document upload & completion; signatures; volunteer management collection | "automatic verification for NGBs"; safety & compliance integrations; youth-registrant legal docs | security & privacy; health & safety (2 articles) |
| Facility module | websites/fan wear; facilities not at fetched tier | "set facility availability" in scheduling; tournaments | facilities platform line + facility managers collection | facilities feature line | website builder line |
| Officials | Stack Officials cross-sell (separate product) | Officials & Gamesheets collection (in-product) | n/e at fetched tier | n/e at fetched tier | n/e at fetched tier |
| Governing-body layer | NGB partnerships; USSF data center integration | "For Governing Bodies" program | governing bodies platform line | NGB verification | partnerships & integrations |

n/e = not evidenced at the tier fetched this pass. Absence of a row entry is not absence of the feature.

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the product stops being a youth sports management system. Four structures, held jointly:

1. **The youth-sports organization as the container of record, holding a youth-shaped participant population.** The league, association, club, or rec program is the entity the system records and operates from; its population is child participants held with guardian/family linkage (guardians are the operating contacts for accounts, consent, communication, and typically payment) plus the adults who staff the operation — coaches and team staff, characteristically volunteers at the rec pole. Remove the org container → a team app or a bare form; remove the youth/guardian structure → an adult-league tool, a different domain.

2. **The season as the org's operational unit, recurring as the org's cycle.** Participation is organized as seasons/programs; each season is a fresh container that gathers the season's intake (players and volunteers), the season's team structure, the season's schedule and play, and the season's transactions; seasons close and roll forward (copy/clone of structure), while the organization and its people persist across seasons. Remove → an unstructured tool or a one-shot event/transaction surface.

3. **Formation: the org converts its registered pool into a division/team structure.** Age-based divisions (skill levels, grades as variants) organize the participant pool; rosters are built per team under the season — by assignment, balancing for rec play, or selection via tryouts/offers; rostering is bound to the same season and commonly movable across age levels. Remove → a participant database or a registration platform's output roster with no season structure.

4. **Season operation: the org runs its season on the system and coordinates it with families.** The season's calendar of practices and games is built and adjusted as an operated object; changes, reminders, and announcements propagate to guardians; responses (availability) flow back through family/team surfaces. Remove → a roster directory nobody operates, or scheduling/communication scattered to external tools.

Jointly load-bearing (C):

- 1 alone = participant/member database
- 2 alone = an offer catalog / registration structure
- 3 alone = a roster tool
- 4 alone = a team app or scheduling utility
- 1+2 without 3+4 = Sports Registration Platform territory (intake transaction with the org operation stripped)
- 1+3 without 2+4 = teams directory with no season being run
- 2+3 without 1+4 = season scaffolding nobody operates (spreadsheet-era practice)
- 1+4 without 2+3 = an organization broadcasting around ad-hoc teams
- 3+4 without 1+2 = one team's life (Team Management Application) or competition machinery without an org (League Management Platform)

Domain binding: the Type is bound to youth sports — the participant is characteristically a minor, and the operating relationships (account, consent, communication, money) run through guardians; the volunteer dependence of rec organizations shapes the software's simplicity posture. Products extending the same machinery to adult leagues are extending beyond the leaf's center, not redefining it.

### L1 — Common Mature Structure

Present across the sample (B), expected in the market, not definitional:

- In-product registration machinery (forms, custom questions, waivers/signatures, document uploads, waitlists, tryout offers, payment plans) — though external intake exists (linking pre-formed teams, importing rosters, consuming governing-body registration)
- Season fee collection and the money loop (online payments, invoices, plans, refunds, financial reconciliation)
- Family/guardian-facing app or portal (schedule, RSVP/availability, chat) and team/coach app (rosters, team chat, availability)
- Organization-wide and targeted communication with automatic reminders/notifications
- Scores/standings/statistics for the org's own divisional play; game sheets
- Org website as public presence and registration storefront
- Volunteer management and safety screening (volunteer registration/verification, background-check-oriented safety & compliance machinery, minor-data privacy posture)
- Reporting over registration, participation, and finances
- Fundraising, sponsorship, fan-wear (the youth-org economy)
- Season rollover tooling (clone/copy structure forward)
- Governing-body integration (roster data upward, NGB verification, sport-specific compliance such as pitch counts)

### L2 — Variant / Optional Structure

- Org shape served: rec leagues / travel clubs / community associations / governing bodies / parks & recreation / multi-location operators / tournament organizers
- In-house divisional competition (standings, playoffs) vs consuming external league schedules (import) — both realizations in-sample; many orgs do both
- Officials coordination (in-product vs cross-sold sibling product)
- Facility/rental management as a bundled module
- Tournaments as a program type
- Free/volunteer pricing pole vs business/revenue-growth pole
- Geographic regime: the sampled market is North-America-centric; European youth organizations more often run on club-management-shaped software (membership-led) — a regional variant, low-strength assertion
- Sport-specific modules (pitch counts, scorekeeping/streaming apps)

### L3 — Vendor-specific (Research Notes only)

- Sports Connect: Stack Sports suite cross-sell (Stack Officials, Stack Tourney, TeamApp, TeamInn, Gameplan, CaptainU, Skyhawks); USSF National Data Center integration; Little League/PONY pitch-count framing; Capterra rating artifacts.
- TeamLinkt: "Emi" AI assistant; migration savings calculator and SportsEngine/Sports Connect switcher promos; "no platform fees, no contracts" posture; live-chat support positioning; Game Sheets; sponsorship matching.
- Crossbar: Team-vs-Group semantics (groups lack team contact info/feed/chat/app roster); Offer system for tryouts; "Touches & Allocation" scheduler inputs; upload codes; "Click-and-drag" scheduling not fetched; now part of PlayMetrics.
- LeagueApps: FundPlay / PLAYS coalition / NextUp community; registration fee insurance; evaluations module; Design Shop websites; Stripe/ACH specifics.
- TeamSnap: Tournaments product line (43-article category); Admin Playbook category taxonomy; team-join mechanics; Health & Safety article pair.

## Vendor-specific Findings

- The safety/screening depth (background-check workflows) is marketed (Sports Connect "Safety & Compliance", "verify players and volunteers"; LeagueApps "integrations with safety and compliance tools") but the screening workflow itself was not documented at help-article level in this pass's fetches — assertions kept weak; Crossbar carries a Volunteer Management collection (3 articles) whose internals were not fetched.
- Crossbar's same-season rostering rule ("Players do need to be signed up in the same season where the teams are created in order to be rostered to that team") is the cleanest in-sample statement of season-scoped eligibility; whether other products enforce it as strictly is unverified — treat season-scoped rostering as L1-common with Crossbar as the A-tier witness, not as a universal rule.

## Boundary Findings

**1. vs Sports Registration Platform (processed 2026-09-09) — pre-hung flag DISCHARGED, keep-both RATIFIED.** The discriminator every pass independently reached: center of gravity. The registration platform centers the signup transaction (participation offer → platform-run intake → registered roster); this Type centers the organization's season operation — the registered roster is where this Type *begins* (formation, schedule, family coordination, season close). Directional tests (both recorded in research/): strip formation + schedule + family coordination + rollover, keeping offer+transaction+roster → Sports Registration Platform remains; strip the transaction machinery (import rosters, record players on paper intake) keeping the org's season operation → this Type remains. Evidence: Crossbar documents "Forms" as a registration type "similar to Google Forms/Survey Monkey" and "Link Existing Teams"/roster import exists (TeamLinkt) — the org operation does not depend on platform-run intake. Market packaging corroborates: LeagueApps and TeamLinkt self-label "youth sports management" for the *whole* operation while the registration pass's own sample sold "registration" as the feature page.

**2. vs Sports Club Management (processed 2026-09-09) — pre-hung flag DISCHARGED, keep-both RATIFIED.** The club pass's proposed discriminator holds from this side: youth sports organizations are registration/season-led (the season's sign-up and the season operation are the center; rec leagues, volunteer boards), clubs are membership/competition-led (the standing member organization fielding teams; member standing + dues). Refinements from this side: (a) the money seam differs — the club Type treats the member money loop as definitional; this Type holds season fees as a standard capability (feeless community programs and pay-later forms remain in-type; Crossbar ships "Forms" and memberships as registration types alongside fee-charging programs); (b) the club Type consumes external competition calendars, while this Type commonly *runs* its own divisions' play (schedules, scores, standings) as season machinery — closer to a league, yet still not the league's center; (c) heavy product overlap is confirmed (TeamSnap self-labels "club & league management" and serves both; migration promos treat Sports Connect/SportsEngine/TeamLinkt as one population) — the leaves are center-of-gravity lenses on one market, keep-both with the seam documented both sides.

**3. vs Sports Academy Management (processed 2026-09-09) — pre-hung flag DISCHARGED, keep-both RATIFIED.** Academies are program/tuition-led training businesses (class portfolios, sessions, recurring tuition); youth sports organizations are season-participation-led (register to play a season, not to be trained). Crossbar's registration types show the seam from inside one product: "Programs — full season, camp, tryouts, or single-session" remain participation offers, while the class-management family's offer is instruction delivery. Camps appear in both markets as program shapes; the center test decides.

**4. vs League Management Platform (processed) — seam held.** The league platform runs a competition between sides (fixtures, results, computed standings) for an organizing body as its center. Here, when the org runs its own divisions' play, scores/standings/schedules are season machinery inside the org's operation (TeamLinkt's season canvas; Crossbar's league product "automatically syncs with our club product" — the vendor itself models league as a sibling of the org system). A product whose center is generating and operating competitions across many organizations' sides remains League Management Platform.

**5. vs Team Management Application (UNPROCESSED sibling) — FORWARD FLAG.** Expected seam: one team's life (roster, schedule, communication, availability) vs the organization's many teams under season structure with formation and family coordination at org level. In-sample evidence that the boundary is real: TeamLinkt documents "Toggle Between League and Team Account Dashboard" — the team dashboard is a surface *inside* the org system; Sports Connect cross-sells a separate team app; Crossbar scopes team staff resources inside the org product. Joint review recommended at that pass.

**6. vs Sports Scheduling Platform (UNPROCESSED sibling) — FORWARD FLAG.** Expected seam: the org's own season calendar as an operated surface (game/practice schedules built, balanced, published to families) vs scheduling machinery (fixture generation, optimization, multi-org scheduling) as the center. TeamLinkt's "balance game counts / conflict-free schedules" and Crossbar's scheduler resources + touches/allocation sit close to that seam; this pass makes no scheduling-machinery claims. Joint review recommended at that pass.

**7. vs School/College Athletics Management (processed 2026-09-09) — consistent.** That pass's distinction holds: community/club youth organizations vs school-affiliated programs under educational authorities with student-data privacy posture. Sports Connect's audience triad (governing bodies / local clubs & leagues / parents-coaches-athletes) contains no school pole; the registration pass's FinalForms covers the school-registration side.

**8. vs Tournament Management Platform (processed 2026-09-09) — consistent.** Tournaments appear here as a program type / intake shape (Crossbar "accept new Team registrations" for tournaments; TeamLinkt tournaments feature; TeamSnap Tournaments as a separate line) — a capability slice, not the center.

**9. vs Sports Federation Management / Sports Membership / Licensing Platform (processed) — consistent.** Governing-body relationships appear at this Type's edge: NGB verification, data sync upward (Sports Connect's USSF National Data Center integration; LeagueApps "automatic verification for NGBs"), "For Governing Bodies" audience (TeamLinkt). The federation's governance register and the membership/licensing credential remain those Types' centers.

**10. Lower-boundary probe.** Bare team apps and free team-communication tools sit below this Type (no org container, no season cycle, no formation across divisions); registration-only tools sit beside it (registration platform). The org+season+formation+operation joint core is what lifts a product above the line.

## Uncertainties

1. **SportsEngine** remains unverified (403 ×2 in the registration pass). It is plausibly the largest single vendor in this market; its territory is evidenced indirectly (TeamLinkt migration promos; Sports Connect as the Stack sibling). No SportsEngine-specific claims made anywhere.
2. **Safety/screening workflow depth** (background checks, SafeSport-type flows) not documented at help-article level this pass; only feature presence asserted.
3. **European youth-sports pole** sampled only via the club pass's products (Spond, SportEasy, Thrive4) whose center is the member organization; whether a distinct European "youth sports management" product family exists with the season-operation center is unverified — geographic variant held at low strength.
4. **Facilities, officials, tournaments** depths vary across products and were mostly observed at feature-line level; no operational claims.
5. **Pricing/plan gating** not researched; no numeric claims anywhere in this pass.
6. **PlayMetrics** (now parent of Sports Connect and Crossbar) unreachable per prior passes; the consolidation is recorded from the two home-page banners only.

## Final Synthesis

Youth Sports Management is the operator-side system of record for youth sports organizations, and its center is the organization's season operation. The defining core is four jointly-held structures: (1) the youth-sports organization as container of record holding a youth-shaped participant population — child players with guardian/family linkage plus the coaches/volunteers who staff teams; (2) the season as the operational unit of the org's year, gathering intake, team structure, schedule/play, and transactions into a container that closes and rolls forward; (3) formation — the org converts its registered pool into age/skill divisions and rostered teams under the season's rules; (4) season operation — the org runs its season on the system (schedule built and adjusted, changes and reminders propagated to families, responses flowing back). Season fees, communication tooling, scores/standings, websites, volunteer vetting, safety compliance, reporting, fundraising, and governing-body integrations are the standard mature machinery that makes the operation practical but do not define the Type. The seams: the signup transaction belongs to the Sports Registration Platform; the standing member organization with member dues belongs to Sports Club Management; the tuition program belongs to Sports Academy Management; the competition between sides belongs to League Management Platform; one team's life belongs to Team Management Application. The market sells one product family into all these labels; the leaves are center-of-gravity lenses, keep-both ratified against all processed neighbors.
