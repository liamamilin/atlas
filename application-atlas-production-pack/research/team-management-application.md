# Research Notes — Team Management Application

## Research Goal

Understand what software sits under the directory leaf "Team Management Application" (§28 Sports, Fitness & Recreation, between "Sports Club Management" and "League Management Platform"): what the central object is, who runs it and who joins it, how the team's week actually flows (schedule → response → event), which structures repeat across the market, and where the boundary lies against the heavily overlapping §28 siblings — all of which pre-hung flags on this leaf — and against cross-family neighbors (Team Messaging, Group Messaging, Shared Team Calendar, Employee Scheduling).

This leaf carries the densest pre-hung flag set in the directory: every processed §28 sibling left a team-side seam expecting discharge at this pass (league-management-platform, sports-club-management, youth-sports-management, sports-registration-platform, sports-academy-management, sports-coaching-platform, sports-meet-management, tournament-management-platform, sports-scheduling-platform, referee-management-platform, school-college-athletics-management, athlete-management-system, athlete-injury-availability-management).

## Initial Boundary (hypothesis before research)

- Hypothesis: the amateur/youth sports team's own operating app — ONE team as the container; a coach/volunteer/team manager creates it and manages the roster; members (or their guardians) join by invitation; the team's schedule of games/practices/activities is the operating calendar; availability/RSVP responses flow back; communication is scoped to the team. Distinct from the organization-level products (club/youth-org/league) which run many teams plus money and governance.
- Prior-pass consensus seam (recorded independently by league, club, youth-sports, registration, academy, coaching, meet, tournament, scheduling, referee, athletics, athlete-management passes): "one team's own life (roster, availability, schedule, communication) vs the organization's many teams + member org + money"; org products embed team management as a delegated module (SportEasy "also the #1 team management app"; Spond app vs Spond Club; LeagueRepublic team admins; TeamLinkt league/team dashboard toggle).
- Key uncertainties going in: (1) is availability/RSVP definitional or just common? (2) is in-team money collection definitional? (3) is competition content (scores, stats, lineups) definitional? (4) is "sports" itself required, given some products serve non-sport groups? (5) is team chat definitional, given group messaging exists as its own Type?

## Research Questions

1. What is the central object — what exactly does "one team" mean in these products?
2. Who creates and runs the team, and what powers do they hold?
3. How do members (and guardians) enter the team?
4. What is the event/availability loop — what states does a scheduled occasion pass through?
5. What communication forms exist and how are they scoped?
6. Which money features exist in the team app proper?
7. Which competition features (results, stats, lineups) exist, and are they team-app or adjacent-Type machinery?
8. What happens across seasons (rollover, archives)?
9. Where do org products (club/league) hand off to the team app, and how?
10. What breaks if a structure is removed (remove-test per structure)?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different geographies/customer levels:

- **TeamSnap** (US) — the flagship monetized team OS; freemium with tier-gated availability tracking; separate TeamSnap ONE for clubs/leagues. Team-first, payments included.
- **Spond** (Norway/UK) — free, communication-and-events-first; team products sold to "groups" including non-sport activities (music, scouting); separate Spond Club product.
- **Heja** (US/EU) — simplest communication-first pole; no payments (fundraising instead); free with Pro tier; small clubs layer.
- **SportEasy** (France) — competition-flavored team app (convocations, lineups, stats, federation calendar imports); explicit "Team vs Club" product split in vendor's own FAQ.

Market context (not sampled, documented by prior sibling passes): TeamLinkt (free team app with league integration; team dashboard inside org system), Sports Connect / SportsEngine (org-side with parent app), Loop/LeagueApps team app.

## Sources

Research date: 2026-09-10. All Tier 1/Tier 2 fetches succeeded.

- TeamSnap — teams landing page: https://www.teamsnap.com/teams [T2]
- TeamSnap — Help Center hub: https://helpme.teamsnap.com/ [T1]
- TeamSnap — Consumer Playbook (team-side help book): https://teamsnap-consumer-playbook.helpscoutdocs.com/ [T1]
- TeamSnap — Consumer Playbook, Scheduling & Availability category: https://teamsnap-consumer-playbook.helpscoutdocs.com/category/2712-scheduling-availability [T1]
- Spond — teams page: https://spond.com/en/teams/ [T2]
- Spond — Events feature page: https://www.spond.com/events/ [T1-level operational FAQ]
- Spond — Availability Requests feature page: https://www.spond.com/availability-requests/ [T1-level operational FAQ]
- Spond — App help center: https://help.spond.com/app/en/ [T1]
- Heja — home page: https://heja.io/ [T2]
- Heja — help center: https://help.heja.io/ [T1]
- SportEasy — teams page (FR): https://www.sporteasy.net/fr/teams/ [T2]
- SportEasy — Invitations & attendance feature page (EN): https://www.sporteasy.net/en/teams/features/invitations-and-attendance/ [T1-level official feature doc]

## Product Observations

### TeamSnap

Key observations:

- Self-label (T2): "the leading team management app" for youth sports coaches and parents; toolkit described as "team chat, last-minute alerts and scheduling to assignments, payment collection"; "Know who'll show for practices and games, get the word out about changes, build rosters — you can do it all in one place." [A]
- Separate product for organizations (T2): "TeamSnap ONE" for Clubs & Leagues — "Registration & payments, schedules, communications, coaching resources, parent app, live streaming." Team product and org product are distinct lines with separate help books. [A]
- Pricing tiers on teams page (T2): Free includes Scheduling, Messaging, Assignments, Payments, small-team roster; Premium/Ultra add "Availability and RSVP Tracking" (tier-gated), ad-free, larger rosters. Availability tracking is monetized. [A]
- Vendor claim: "supports more than 200 activities." [A — vendor marketing number, not independently verified]
- Help-center hub (T1) splits two books: organization admins (registration, payments, invoicing, administrative settings) vs coaches/families/players (schedules, communication, stats, account settings). [A]
- Consumer help book categories (T1): Roster Profile & Member Management; Communication; **Scheduling & Availability (43 articles — the largest category)**; Tracking & Statistics; Photos, Videos & Files; Settings; Security & Privacy; Account & Plan Management. [A]
- Article titles in Scheduling & Availability (T1): Subscribe to a Team Schedule; Viewing your all-team schedule; Share Schedule with Family and Friends; Scheduling for teams; **Organization calendar**; **Enter Game Results**; Export or Print a Team Schedule; Manually adding schedule events; **Set Game and Event Availability**; **Importing organization schedules**; Add Schedule Locations; **Create games and practices in scheduler**; Accessing Archived or Retired Seasons; Edit Games and Events. [A]
- Org-side help categories (T1): Season Management and Organization Structuring; Invoicing, Registration, and Financials; TeamSnap for Clubs and Leagues; TeamSnap Tournaments — org machinery lives in the other product/book. [A]
- Vendor-specific: TeamSnap+ practice plans (partner content from MLS, MLB, Jr. NBA etc.) — coaching-content add-on. [A — vendor module]

### Spond

Key observations:

- Self-label (T2): "A free app trusted by over 12 million people to organise sports and activities"; "created to simplify how people manage their clubs, teams and groups"; "Looking to efficiently manage your team, or club?" [A — user counts are vendor claims]
- Feature map (T2): Group Setup; Events; Invites & Reminders; File Storage; Messaging; Payments; Group Fundraising; Add Guardians; Notifications; Availability Requests. [A]
- Events mechanics (T2, operational FAQ): event types = single, repeating, season planner, time poll; meet-up times before event start; auto-accept option ("participants automatically attending or ... confirm each time"); waiting lists — "When the maximum number of participants is reached, the next people to sign up will be put on a waiting list. If a registered participant cancels ... Spond will automatically notify the first person on the waiting list." [A]
- Availability Requests mechanics (T2, operational FAQ): admin checks availability BEFORE creating an event; responses categorized (Available, Unanswered, Declined, Other); "Select people and create event" from responses; message non-selected recipients; automatic reminders to non-responders; optional response deadline; requests visible only to chosen recipients; admin sees all requests in the group event list even if not host. [A]
- Messaging (T2): "fully GDPR-compliant ... complete traceability for all users, including comprehensive oversight for parents/guardians." [A]
- Payments (T2): "create payment requests within your group or subgroups" (trips, membership fees, uniforms). [A]
- Guardians (T2): dedicated "Add Guardians" feature; help center Getting Started covers "profiles for guardians and children." [A]
- Help-center collections (T1): Getting started (guardian/child profiles); Account settings (calendar sync, notifications); **Groups and messages ("Create or join a group")**; **Events ("Matches, season planner, recurring and one-time events")**; Post, polls and files; Payments; Fundraising; GDPR/Privacy; Safeguarding. [A] — Note: Spond calls the team a "group"; matches are an event kind.
- Audiences (T2): Group Admins & Coaches; Club Admins; Guardians & Parents; Organisations & Schools; Participants & Players. [A]
- Separate org product (T2): Spond Club — club management, manage members & groups, club website, courses & academies, collecting payments, club fundraising. Vendor publishes a "Spond Club vs App — what's the difference?" explainer. [A]
- Non-sport reach (T2): activity list includes Music and Scouting alongside sports. [A]

### Heja

Key observations:

- Self-label (T2): "Sports team management and communication app"; "A team includes everybody, from families to coaches, friends and supporters. Easily organize and communicate with everybody on your sports team in one free and simple app." [A]
- Schedule + availability (T2): "Easily plan upcoming practices, games and team activities for all to see. Get updated on who's available to play. Heja helps out by reminding everyone to reply!" [A]
- Messaging posture (T2): "Everything doesn't have to go through the coach. Team messaging, coach communication, organizing carpools and much more"; "see who viewed all posts and the schedule." Read-state on posts observed. [A]
- Calendar sync to personal calendars (T2). Privacy posture (T2): "Teams are only accessed by team members and it's up to them what info they share and with whom." [A]
- Fundraising (T2): per-player webshops with individual goals and team goal aggregation. No payments/collections feature observed at team level — the money pole of the sample. [A]
- Help-center collections (T1): Getting started (27 articles); Managing your profile (23); **Managing your teams (45)**; Heja for Clubs (8 — "Managing multi-team clubs on Heja"). [A]
- Heja Pro paid tier exists (T2 nav). [A]

### SportEasy

Key observations:

- Self-label (T2): free app for coaches/educators to "gérer votre équipe sportive" — shared calendar, convocations with automatic reminders, attendance and statistics tracking, centralized messaging. [A]
- Team vs Club split in the vendor's own FAQ (T2): "La version Équipe est conçue pour la gestion d'un seul effectif de manière autonome. Si vous souhaitez centraliser et gérer plusieurs équipes au sein d'une même structure, partager une base de données membres ou centraliser les cotisations ... passez à notre version Club." — the vendor's own one-team-vs-organization boundary statement. [A]
- Convocation/invitation mechanics (official feature page, T1): automatic invitation system sends notifications to indicate availability; automatic reminders before each event; manual invitation optional; organizer watches "the number of players available increase until you reach the required amount" (required headcount); attendance list can be hidden from players (to prevent withdrawal "because their friend isn't available"); channel choice email or push; "Youth team coaches can add parents and guardians to their children's profiles. In this case, they will also receive and respond to the invitations to events." [A]
- Attendance vs response distinction (T1): responses are pre-event; on the day the coach "can update the attendance status of each player in real time ... whether a player was on time, late, absent but excused or absent and unexcused"; data accumulates in a season attendance report (Premium) usable "to set up a selection system ... based on players' attendance at training sessions." [A]
- Feature map (T1/T2): member management (roster & profiles, custom fields e.g. allergies/jersey size, parent access); team messaging; shared calendars; **import official match calendars from partner federations (FFF, FFR, FFBB, FFVB) with automatic updates of calendars, results and standings**; team lineups (compositions); task management (jerseys washed, balls inflated, carpools — assigning responsible members per match); stats & live stats (individual/collective, MVP "Star of the match" votes); after-the-game (reports, photos); payments/collections from members; championships management. [A]
- Free tier limited to 30 members; Premium unlimited (T2, vendor figures). [A — vendor-specific limits, not generalized]
- Three-sided audience (T2): coaches / players / parents (Live Match for remote parents). [A]

## Cross-product Comparison

| Structure / capability | TeamSnap | Spond | Heja | SportEasy | Evidence |
|---|---|---|---|---|---|
| One-team container created/run by organizer (coach/manager) | ✓ | ✓ ("group" + admins) | ✓ | ✓ | B |
| Managed roster of member records | ✓ (66-art. category) | ✓ (group members) | ✓ | ✓ (profiles, custom fields) | B |
| Guardian/parent layer for minors | ✓ (families; family sharing) | ✓ (Add Guardians; oversight) | ✓ ("families ... included") | ✓ (respond on child's behalf) | B |
| Team schedule: games + practices + activities | ✓ (43-art. category) | ✓ (17-art.; event types) | ✓ | ✓ | B |
| Availability/RSVP loop with reminders to non-responders | ✓ (tier-gated) | ✓ (requests + auto reminders) | ✓ ("reminding everyone to reply") | ✓ (convocations + relances) | B |
| Response categories incl. unanswered state | ✓ (set availability) | ✓ (Available/Unanswered/Declined/Other) | ✓ (who's available) | ✓ (available or not) | B |
| Post-event attendance recorded (vs pre-event response) | not directly observed | not directly observed | not directly observed | ✓ (on time/late/excused/unexcused + season report) | A — single product |
| Team-scoped messaging/announcements | ✓ | ✓ (GDPR/traceable) | ✓ (core) | ✓ | B |
| Read-state / visibility tracking on posts or schedule | — | — | ✓ (who viewed posts) | — | A — single product |
| Payments/collection inside team | ✓ (free tier list) | ✓ (payment requests in group) | — (fundraising instead) | ✓ | B (3/4) |
| Fundraising | not observed at team tier | ✓ group fundraising | ✓ per-player webshops | — | B (2/4) |
| Game results / scores entry | ✓ (Enter Game Results) | — (matches as events; not observed) | — | ✓ (+ live stats, MVP votes) | B (2/4) |
| Lineups | — | — | — | ✓ | A — single product |
| Task/assignment duty loop (carpools, kit) | ✓ (Assignments) | — | ✓ (carpools via messaging) | ✓ (task management) | B (3/4) |
| External schedule import (org / federation) | ✓ (import organization schedules) | — | — | ✓ (federation calendars auto-sync) | B (2/4) |
| Practice plans / coaching content | ✓ (TeamSnap+ partner content) | — | — | — | A — single product |
| Calendar sync / notifications | ✓ | ✓ | ✓ | ✓ | B |
| Separate organization-side product (club/league) | ✓ TeamSnap ONE | ✓ Spond Club | ✓ Heja for Clubs | ✓ SportEasy Club | B — 4/4, decisive |
| Season persistence (archives/rollover) | ✓ (archived/retired seasons) | ✓ (season planner) | — | ✓ (season-spanning stats) | B (3/4) |

## Canonical Abstraction

### L0 — Defining Invariant

Three jointly-held structures. If any one is removed, the product stops being recognizable as a Team Management Application:

1. **The team as container of record** — one standing group, created and run by its organizer(s) (coach, team manager, volunteer admin), holding a managed roster of participant records. Membership is organizer-managed (invite/join by link, email/phone, or org handoff), not self-discovered. Participants are commonly minors with guardian linkage, but adult teams are in-type.
2. **The team's event schedule** — the team's occasions (games, practices, training, team activities) placed on a shared team calendar that is the operating surface of the team's life.
3. **The participation response loop** — responses collected from roster members against scheduled events (available / not available / no answer), automatic reminders chasing non-responders, and the organizer planning from the resulting availability picture. The loop is the reason the app exists: it converts a static roster+schedule into an operated team.

Remove-tests (jointly-held load-bearing):
- 1 alone = a roster/contact list (or a club's member database slice)
- 2 alone = a calendar / schedule tool
- 3 without 1+2 = an RSVP/poll tool
- 1+2 without 3 = a static team page / bulletin-board schedule nobody operates (pre-app-era team websites sit here)
- 2+3 without 1 = anonymous event sign-up (booking-poll territory)
- 1+3 without 2 = availability polls with no schedule to anchor them
- The one-team binding is itself load-bearing: add a multi-team organization container with member org, season operation, and org-level money → Youth Sports / Club Management; add competition among many sides with computed standings → League Management.

Historical / market-sample check: a paper-era youth team — coach's paper roster, handout season schedule, phone-tree availability collection, carpool coordination — realizes all three structures in substance (roster, schedule, availability gathered by another medium, communication outside the artifact). The definition therefore must not require in-app payments, in-app chat as the only channel, scoring, or any specific identity substrate. Pre-app static team websites (roster + schedule, no response loop) fail leg 3 — consistent with treating them as static pages, not team management applications. The check passes.

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Team-scoped messaging/announcements/chat (universal in-sample, but the availability loop already supplies the definitional communication behavior; without chat the product remains in-type — communication-first pole Heja still centers roster/schedule/availability)
- Guardian/parent mediation (universal in-sample because youth is the dominant market; adult teams run without it)
- Payments/collections inside the team (3/4; Heja demonstrates the type without it)
- Fundraising (2/4)
- Notifications, calendar sync, file/photo sharing
- Duty/task assignment (carpools, kit, snacks) (3/4)
- Game results/scores entry (2/4)
- External schedule import from org/federation calendars (2/4 — the documented handoff edge)
- Season archives/rollover
- Privacy controls over member visibility (Spond per-recipient visibility; Heja member-only access; SportEasy hidden attendance lists)

### L2 — Variant / Optional Structure

- Money mechanics: in-team payment requests vs fundraising webshops vs none
- Competition flavor: results/stats/live/MVP votes (SportEasy, TeamSnap) vs none (Heja, Spond)
- Availability-loop mechanics: pre-event availability requests (Spond) vs per-event RSVP (others); auto-accept vs confirm-each-time; waiting lists; response deadlines; time-poll events; season planner bulk creation
- Post-event attendance states and season attendance reports (deep at SportEasy; presence elsewhere unverified)
- Activity domain: sports-dominant; some products explicitly serve non-sport groups (Spond: music, scouting; TeamSnap: "200+ activities" claim)
- Business model: free with ads/tiers (TeamSnap, SportEasy) vs free-no-ads + payment processing (Spond) vs free + Pro (Heja)
- Roster size limits / ad postures (vendor-specific)

### L3 — Vendor-specific (Research Notes only)

- TeamSnap: tier-gated Availability & RSVP tracking; TeamSnap+ partner practice plans (MLS/MLB/Jr. NBA etc.); "Find my team" invite lookup; separate ONE product line with live streaming
- Spond: Friskus payment integration (🇳🇴); safeguarding collection; Life360 match-day logistics partnership blog
- Heja: per-player fundraising webshops; who-viewed-post read states
- SportEasy: federation calendar auto-import (FFF/FFR/FFBB/FFVB) with auto-updating results/standings; lineup builder; Star-of-the-match voting; 30-member free cap; hidden-attendance-list social mechanic
- Vendor user-count claims (12M Spond / 500K teams Heja / 30M people TeamSnap) — marketing numbers, not verified

## Vendor-specific Findings

See L3 above. The decisive vendor-corroborated structural fact: **all four sampled vendors split their product line into a team app and an organization product** (TeamSnap ONE / Spond Club / Heja for Clubs / SportEasy Club), with the vendor's own documentation describing the team product as "one effectif / one team" and the org product as "multiple teams + shared member database + centralized money." This is the strongest possible market-side confirmation of the center-of-gravity seam every prior sibling pass recorded.

## Boundary Findings

**Discharge of pre-hung §28 sibling flags (all keep-both, ratified from this side):**

1. **vs Sports Club Management** (flag: one team vs member org + money). CONFIRMED. Every sampled vendor sells both poles as separate products; SportEasy's FAQ states the team version manages "un seul effectif" and directs multi-team structures to the Club version; Spond publishes a "Club vs App — what's the difference?" explainer. Remove-test: remove the member organization, its dues, and multi-team scope from the club system → team app territory. Reverse: add org container → club territory. KEEP BOTH.
2. **vs Youth Sports Management** (flag: team dashboard as surface inside org system). CONFIRMED — the team app is the delegated module inside org products (SportEasy markets its Club product as also "the #1 team management app" pole; TeamSnap ONE includes a parent app). The org system's season operation (formation, family coordination at org level) is not in the team app's core. KEEP BOTH.
3. **vs Sports Registration Platform** (flag: roster-handoff). CONFIRMED — the handoff is a documented integration edge, not shared structure: TeamSnap's help has "Importing organization schedules"; SportEasy imports federation calendars. Registration owns the signup transaction; the team app owns life after the roster exists. KEEP BOTH.
4. **vs League Management Platform** (flag: competition among many sides vs one team's life; league products embed team modules). CONFIRMED — team app has no competition-between-sides machinery as structure (results entry is a team-scoped log, not computed standings over a season programme). Remove computed standings + multi-side competition → team app. KEEP BOTH (league pass already ratified keep-both; this pass ratifies from the team side).
5. **vs Tournament Management Platform / Sports Meet Management** (flags: team-side vs event-side). CONFIRMED — teams hold rosters and respond; the tournament/meet system is the host-side record. KEEP BOTH.
6. **vs Sports Scheduling Platform** (flag: one team's calendar vs competition-wide schedule machinery). CONFIRMED — team-side products consume schedules (import edges observed at TeamSnap/SportEasy); the scheduling platform produces them. KEEP BOTH.
7. **vs Sports Coaching Platform** (flag: team ops vs client practice). CONFIRMED — the team app's roster is a fixed team membership operated around events; the coaching platform's roster is a client book operated around delivered sessions. KEEP BOTH.
8. **vs Referee Management Platform** (flag: team-centric counterpart). CONFIRMED — one team's roster/schedule/comms vs one official pool across many teams' games. KEEP BOTH.
9. **vs Sports Academy Management / School & College Athletics / Athlete Management / Injury-Availability** — confirmed adjacent or narrower/broader per prior passes' directional tests; the team app has no tuition programs, no department portfolio, no longitudinal preparation record, no health-derived availability states (it *collects* availability responses, it does not *derive* them from medical documentation). KEEP BOTH in each case.

**Cross-family seams:**

10. **vs Team Messaging Application (§01.01)** — workspace chat binds conversation to organizational channels; the team app binds conversation to a team container whose center is the event/availability loop. Chat is a capability inside team apps, not their center. KEEP BOTH.
11. **vs Group Messaging Application (§01.01)** — membership is organizer-managed roster + event machinery vs member-defined self-joining conversation. A group chat with a shared calendar does not become a team management application until the response loop and managed roster exist. KEEP BOTH.
12. **vs Shared Team Calendar (§03.08)** — a calendar surface without roster or participation responses. KEEP BOTH.
13. **vs Employee Scheduling Platform (§09)** — direction of obligation: an employer assigns shifts that workers are obligated to work; a team organizer proposes occasions that members volunteer to attend. Different object world (shifts/coverage vs games/practices) and different user relationship. KEEP BOTH.

## Uncertainties

- Post-event attendance marking beyond SportEasy could not be confirmed from the sampled surfaces at TeamSnap/Spond/Heja; written as product-specific. (TeamSnap's "Tracking & Statistics" category suggests presence, but article content was not fetched.)
- Whether TeamSnap's org-schedule import creates full team rosters (vs schedules only) unverified — the handoff edge documented at schedule level only.
- Heja's club layer depth (8 help articles) not inspected beyond collection titles.
- Exact roster-size limits, tier boundaries, and ad postures are vendor-specific and time-varying; kept out of the canonical document.
- Single-source findings (Heja read-states, SportEasy lineups/attendance taxonomy) marked product-specific; not promoted.

## Final Synthesis

The Team Management Application is the single-team operating app of grassroots/amateur sports: one standing team, created and run by its coach/manager/volunteer admin, holding a managed roster (guardian-linked where players are minors), living on a shared team calendar of games/practices/activities, and operated through the participation response loop — invitations out, availability responses back, reminders chasing non-responders, the organizer planning from the answered picture. Team-scoped messaging, guardian mediation, in-team money, results/stats, duty assignment, and schedule imports are the standard machinery that makes the loop practical; none of them defines the Type. The market itself draws the boundary: every sampled vendor sells a separate organization-side product for clubs/leagues, reserving the team app for one team's own life. The Type is the team-side pole of the §28 sports-management market — keep-against all org-level siblings on the center-of-gravity seam every prior pass recorded, and keep-against messaging/calendar Types on the container+response-loop seam.
