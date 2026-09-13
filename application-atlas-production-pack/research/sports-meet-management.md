# Research Notes — Sports Meet Management

## Research Goal

Understand what a "sports meet" is as a competition form and what software that manages such meets must contain, how it works, and where its boundaries sit against sibling competition systems (tournament, league, race, timing) and against event/registration software.

Leaf name note: "Sports Meet Management" uses a regional English term for a multi-event athletics competition — the same market segment is served under names like "meet management", "track & field meet manager", "swim meet management". The Type studied here is the meet organizer's competition system of record, independent of which sport's meets it is packaged for.

## Initial Boundary

Working hypothesis before research:

- A sports meet is a bounded, multi-event athletic competition (track meet, swim meet, athletics meet, school sports day) where entrants from one or many sides (teams/schools/clubs) contest a program of distinct events, and per-event results accumulate to the meet's results (often to team points).
- Nearest neighbors: Tournament Management Platform (bracketed team-vs-team), League Management Platform (season programme), Race Management Platform (single mass-participation event), Race Timing System (instrumented capture), Sports Registration Platform (entry intake), School/College Athletics Management (department administration), Event Management/Registration (§26, attendee events).
- Known unknowns at start: is "meet" a real market category with dedicated products (vs a feature of registration platforms)? What is the operational core (entries → seeding → running → results)? Is team scoring definitional? Where exactly does timing hand off?

## Research Questions

1. What is the meet's core object structure — how do meet, event program, entries, heats/flights, results relate?
2. What is the end-to-end organizer workflow, from creating the meet to publishing results?
3. What competition-running machinery is standard (seeding, check-in/scratch, multi-round events, field event series)?
4. What do results look like as data (times/marks, places, non-performance codes, scoring)?
5. How does the meet record interact with timing systems, live-results surfaces, and legacy meet software (file interchange)?
6. Who operates the software (roles), and what do participants see?
7. Which capabilities are definitional vs common vs variant? Does the definition hold for older/regional meet forms (paper-era meets, school sports days)?

## Representative Products

| Product | Domain | Customer tier | Philosophy | Why sampled |
|---|---|---|---|---|
| Athletic.net — AthleticNET + AthleticRUNMEET (+ AthleticLIVE, AthleticLOCAL, AthleticFIELD) | Track & field, cross country | US high schools, colleges, youth | Freemium web platform; meet management + results + rankings as one public ecosystem | Tier 1 help center, deepest operational evidence |
| SwimTopia — Meet Maestro | Swimming (incl. diving) | Summer-league clubs, schools, masters | Cloud-native, volunteer-friendly meet day; bundled with team management | Cloud pole; club/summer-league tier; product-page evidence |
| HY-TEK Meet Manager (MM swim / TM track & field) | Swimming + track & field | Clubs, LSCs, colleges | Long-established incumbent; desktop lineage; file-format lingua franca | Indirect evidence only (see Sources) — included as ecosystem anchor |

Attempted and dropped: OpenTrack (athletics meets, federation-facing — opentrack.run returned 403 twice); LiftingCast (weightlifting meets — JS-only app, no fetchable content). No claims made about them.

## Sources

- Athletic.net Help Center — https://support.athletic.net/ (HelpDocs KB)
  - Support home (category map): fetched 2026-09-09
  - Hosting an Event category: https://support.athletic.net/category/xv7kwoxgiq-event-management — fetched
  - AthleticRUNMEET category: https://support.athletic.net/category/nr0dfytphf-run-the-meet — fetched
  - AthleticRUNMEET Overview: https://support.athletic.net/article/3afoecmp7g-runmeet-overview — fetched
  - RunMeet: Seeding: https://support.athletic.net/article/2mk6rtxmxg-seeding-and-creating-heat-sheets — fetched
  - AthleticRUNMEET: Entering Results: https://support.athletic.net/article/6aoifppdcu-entering-results — fetched
- SwimTopia — Meet Maestro product/blog page: https://www.swimtopia.com/meet-maestro — fetched 2026-09-09 (Tier 2)
- SwimTopia help center — help.swimtopia.com and support.swimtopia.com: 3 failures (timeout, transport error ×2) — abandoned per network rules
- HY-TEK — hy-tekltd.com and hytek.com: transport errors ×2 — abandoned per network rules; HY-TEK evidenced only indirectly through cross-vendor compatibility statements (below)
- OpenTrack — opentrack.run: 403 ×2 — dropped
- LiftingCast — liftingcast.com: JS-only shell — dropped
- Prior processed sibling passes consulted for boundary seams: race-timing-system (research + application + STATUS), race-management-platform (research), league-management-platform, referee-management-platform, sports-facility-management, sports-federation-management (STATUS entries)

## Product A — Athletic.net (AthleticNET / AthleticRUNMEET) — evidence layer A (official help center, directly observed)

### Meet creation & hosting (Hosting an Event category)

- Meets are created per sport: "Creating a Track & Field Meet" (step-by-step, 10 articles) and "Creating a Cross Country Meet" (8 articles) are separate guides — the meet is the container in both.
- Meet hosting includes: invitations to attend ("Managing Meet Invitations" — send invitations, manage invitation requests), confirming team attendance, allowing unattached athlete registration, custom forms (agreements, opt-ins, data collection) at registration, event financial features (entry fees, pre-sold items, donations), meet communications (emails to attending coaches, downloadable coach contacts).
- Meet shape options: multi-day meets ("stretches over two or more days, even if they're not consecutive"), single-gender meets, event-level advanced options (display, per-event registration settings, division sorting).
- Meet page administration: upload & manage meet files attached to the meet page/emails, host/co-host roles, "Add a Timer or Event Manager to Your Meet" (delegated administration for hired timers), reschedule flows (host-side vs attending-team-side), deletion/cancellation semantics (a meet stays on invited teams' calendars until removed there; cancellation may be signaled in the title), merge duplicate meets (duplicates are an operational reality), meet records by division or overall, XC course records as historical lists.
- Championship Series: "source and destination meets, qualifying standards and advancement, coach communication, RunMeet and ALive integration" — series-level machinery linking multiple meets.

### Entry collection → seeding → running → results (AthleticRUNMEET)

- RunMeet integrates with "the entry collection functions of an AthleticNET meet on the Manage Meet page": entries collected via the meet page flow into RunMeet. Entries can also be imported from other entry systems via semicolon-delimited files; entries can be downloaded.
- RunMeet is gated behind a paid "Team Site Supporter" account (positioning-level fact).
- The RunMeet screen: per-event display of gender/event/division/round; heats count, entries count (color-coded by whether all entrants are assigned a heat and lane), results count; Seeding/Results toggle; Track/Field toggle; division & event selectors.
- Seeding (running events): start types — Lanes (best seeds in center lanes), Alleys (two athletes per lane), Waterfall, Staggered Waterfall; lane/position counts; max/min heat size; heat assignment by seed time / random / last name / team name; heat order fast-to-slow / slow-to-fast / random; heat distribution weighted vs even; break points (manual dividing lines between heats/flights); alternating lanes; lane exclusions; team position assignment ("team lanes" for dual meets).
- Auto-reseeding: off by default; reseeds events as entries/seed marks change; documented caution because heat/lane assignments may change and published data can become stale.
- Manual seeding: drag-and-drop athletes between/within heats, add/delete heats, unseeded pool ("Unseed" places an athlete back for reassignment), scratch (removes from heat; reseed after scratching adjusts heats), mark exhibition ("prevents the athlete from scoring or placing"), add athletes on the fly (quick-add by name or competitor number; added athletes also join the team roster on AthleticNET), competitor numbers for data entry/identification.
- Field events: flights with max flight size, flight assignment by seed mark / random / last name / team name, flight order, position assignment within flight, seed-mark and result measurement units.
- Multi-round events: configure prelims, quarter finals, semi finals.
- Combined events/multis: score and run triathlons, pentathlons (indoor/outdoor/throws), heptathlons etc. in RunMeet.
- Wind readings recorded for sprints and horizontal jumps (m/s, per heat).
- Timing: per-event timing method FAT vs hand; hand times converted by published conversion standards when posted; FAT integration via AthleticLOCAL (Windows companion app acting as interface between meet management and timing) supporting FinishLynx, Flash Timing, Eagle Eye; AthleticLIVE for live results; per-heat FAT toggle; XC timer app for hand-timed finishes without chips.
- Reports: heat sheets, athlete rosters, meet programs, finish line sheets (running), field event scoring sheets, "organized by height/flight" for field; reports fall into 4 categories; team scores report.
- Results entry: time or mark per athlete per heat/flight; Heat Place (Hpl), Overall Place (Pl), Points Awarded (Pts) auto-calculated from the configured scoring scheme, overridable; punctuation-free entry with interpretation preview; validation warnings ("Time is too fast", "Mark is too good").
- Result codes: DNS (did not start), DNF, DQ, NT (no time), NH (no height), ND (no distance), NM (no mark), SCR (scratch).
- Field results: final mark directly, or Field Series (each jump/throw entered) enabling tie-breaking and ranking by the software.
- Completion semantics: all entries in an event must have a result (including codes) before the event can be marked complete; marking complete publishes the event to the public meet page immediately; scores from completed events enter the Team Scores report; when all events are complete (or canceled), the meet switches from "In Progress" to "Official"; corrections after Official are possible but require republishing the event (Mark Complete button turns orange); events can be canceled only before results are entered.
- Exports: results downloadable as HyTek Semicolon Delimited, TFRRS CSV, or Tab Delimited formats.

## Product B — SwimTopia Meet Maestro — evidence layer A for feature existence (official product/blog page); no workflow depth (help center unreachable)

- Positioned as "meet management" included with every SwimTopia account; sold into summer leagues, schools, masters, collegiate, parks & rec, year-round clubs; a "Computer Rep Operator" role page exists (meet-day operator as a named role).
- Stated capabilities: reusable meet templates; entries collected in SwimTopia and sent "straight to Meet Maestro — no emailing files back and forth"; one-click relay generation; reports "from heat sheets to ribbon labels" with filtering/customization; real-time athlete and event edits on meet day; timing system integrations (CTS 5/6/7, CTS Dolphin, Time Drops, Wylas "and more"); mobile app live results (with Pro subscription); records & time standards (highlight broken records, show team standings during the meet); diving events tracked alongside swim events; division-based scoring for league/multi-team structures; compatibility with SD3, HY3, and EV3 files and export in formats compatible with HY-TEK and other systems; web-based with multiple people working on the meet simultaneously from different devices; a free Lite tier exists ("Meet Maestro without the entire team management suite").
- Marketing framing ("tame meet day chaos") confirms the pain the Type addresses: entries tracking, heat-sheet updates, timing systems, volunteers on meet day.
- Because the help center was unreachable, no claims are made about Meet Maestro's internal screens, states, or defaults beyond the above feature-existence list.

## Product C — HY-TEK Meet Manager — indirect evidence only (Source-access Limitation)

- Both official domains failed (transport errors ×2) — dropped per network rules. No operational claims asserted from memory.
- Indirect, cross-vendor corroboration of its ecosystem role (each statement itself is Layer A for the *stating* product):
  - Athletic.net documents exporting results in "HyTek Semicolon Delimited" format and importing entries via semicolon-delimited files from other entry systems.
  - SwimTopia documents working with "SD3, HY3, and EV3 files" and exporting results "in formats compatible with HY-TEK and other systems."
- Conclusion allowed at Layer B strength: file-format interchange with the long-established incumbent's meet-data formats is a mature structural expectation across independently built meet products — the incumbent's formats function as the segment's lingua franca. Nothing further about HY-TEK's own screens/states is claimed.

## Cross-product Comparison

| Dimension | Athletic.net (T&F/XC) | SwimTopia Meet Maestro (swim) | Incumbent ecosystem (indirect) |
|---|---|---|---|
| Meet as container | named, dated meet; multi-day option; per-sport creation guides | meet with reusable templates; hosted per team/league | incumbent formats carry whole meet data between systems |
| Event program | events per division per gender; rounds; combined events; ordering | events defined in template; swimming + diving events | implied by file formats |
| Entries | collected on meet page (invitations, fees, forms); import/export; accept/reject | collected in SwimTopia, sent straight into Meet Maestro | interchange files carry entries |
| Competition units | heats/lanes/alleys/waterfall; flights; break points; team lanes | heat sheets; relay generation | implied |
| Results | time/mark per entry; Hpl/Pl/Pts; codes; field series; validation | entered live on meet day; live results via app; records highlighted | HY3/SD3-class result files |
| Scoring | configurable scoring scheme → team scores report | divisional scoring; team standings during meet | implied |
| Timing | FAT ingest via companion app; hand-time conversion; per-event method | timing system integrations (multiple vendors) | incumbent is a peer of timing systems |
| Publishing | event complete → publish; meet In Progress → Official | live results; ribbon labels | results files |
| Roles | host/co-host, timer, event manager; unattached athletes | computer rep operator; volunteers | — |
| Business model | freemium platform; RunMeet paywalled | included with account; Lite tier free | desktop license era (inferred weakly — not asserted) |

Layer B findings (across the two directly-observed poles, both independent implementations in different sports):

1. The meet record binds **program → entries → competition units → results**; both poles realize this chain.
2. **Entries carry seed marks** and are organized into competition units by configurable rules.
3. **Results are entered or ingested**, auto-computed into places and points, with explicit non-performance codes.
4. **Publishing is a meet-record act** (public meet page / live results), with a completion→official lifecycle.
5. **Timing is a boundary, not a core**: meet management consumes times from timing systems (or hand times); it does not measure.
6. **Interchange with the incumbent ecosystem** is implemented by both poles.
7. **Roles split** between meet administration and meet-day operation (computer rep/timer), with volunteers as a labor reality.

## L0 — Defining Invariant

Four jointly-held structures; each individually fails the "still this Type?" test:

1. **The meet as competition container** — a named, dated, bounded athletics competition (one to a few days; multi-day documented) under meet rules, hosted by an organizing body, whose entrants compete on behalf of sides (teams/schools/clubs) or as unattached individuals.
   - Remove → a generic sports event with attendees (§26 territory) or a season-long structure (league territory).
2. **The meet's event program** — the meet's defined set of distinct competitive events, each an individually scheduled, run, and recorded unit (division/gender/age class × discipline); multi-round events a documented extension.
   - Remove → a single race (race-management territory) or a mere timetable/agenda.
3. **Entries binding entrants to events** — per-entrant declarations of which program events they contest, carrying seed marks/times and statuses (unattached, exhibition, scratch).
   - Remove → attendee registration or a bare roster; there is no competition to run.
4. **The per-event results record with outcome semantics** — each event's outcomes recorded against its entries (times/marks → computed places; explicit non-performance codes), accumulating into the meet's results of record and published from it.
   - Remove → a leaderboard with no entries, a timing log, or a results-media site.

Jointly-held is load-bearing:

- 1 without 2 = a generic sports event/gathering
- 2 without 3 = a programme of events nobody is entered in
- 3 without 2 = a registration list
- 4 without 1+3 = an anonymous results board / statistics site
- 1+2 without 3+4 = a promotional event page
- 3+4 without 1+2 = a results/rankings tracker (results-media territory)

## L1 — Common Mature Structure

- Seeding machinery: assignment of entries into heats (with lane/alley/waterfall start types) and flights; configurable heat size, assignment basis (seed time/random/name), heat order and distribution; break points; auto-reseed; manual drag adjustments; unseeded pool.
- Check-in / scratch processing; competitor numbers; exhibition status; on-the-fly athlete/entry edits.
- Meet reports and print outputs: meet programs, heat sheets, finish line sheets, field scoring sheets, ribbon labels.
- Team scoring: configurable scoring schemes per placement; team scores report/standings during the meet.
- Meet records and time standards (per division/overall; highlight broken records).
- Entry collection: invitations, accept/reject, entry deadlines, entry fees and forms (often bundled; alternatively file import from external entry systems).
- Timing integration: FAT ingest via companion/integration; hand-time handling with conversion standards; per-event timing method.
- Publishing: public meet page with live/published results; completion→official lifecycle.
- Roles: host/co-host, timer, event manager/computer operator; guest/volunteer access patterns.
- File interchange with legacy meet software (entries in, results out).

## L2 — Variant / Optional Structure

- Sport-domain packaging: swim (relay generation, diving events/scores, lane-oriented heats), track & field (wind readings, field series, combined events/multis), cross country (race-per-division events, course records, combined divisions, hand-timed app capture).
- Scale/venue: single-school meets, dual meets (team lanes), invitational/open meets, championship series with qualifying standards and advancement across meets.
- Business/deployment: freemium public platform vs subscription suite vs desktop license; paywalled meet operations vs included.
- Regional forms: school sports days / annual sports meets with house teams (regional English "sports meet") — no dedicated in-sample product evidence; held as a plausible deployment of the same structure, not asserted as a market implementation.
- Virtual meets (documented as a distinct Athletic.net category).
- Collection depth: full registration/fees/forms machinery in-product vs entry import only.

## L3 — Vendor-specific (Research Notes only)

- SwimTopia: one-click relay generation; mobile app live results gated behind Pro; Lite tier; named timing integrations (CTS 5/6/7, CTS Dolphin, Time Drops, Wylas); SD3/HY3/EV3 import compatibility statement.
- Athletic.net: AthleticLOCAL Windows companion app; AthleticLIVE/AthleticFIELD/AthleticSB product family; Site Supporter paywall gating RunMeet; Championship Series packaged feature; Excel Meet Manager (XC); TFRRS CSV export; guest access via QR codes; meet-status automation (auto Official switch).
- Incumbent format names (HY3, SD3, EV3, "HyTek Semicolon Delimited") — vendor-named artifacts of an L1 structural finding.

## Vendor-specific Findings

See L3. None of these entered the canonical model.

## Rejected Findings

- "Meet management = track & field only." Rejected: swim pole (with diving) in-sample; XC, combined events documented in the same platform.
- "Team scoring is definitional." Rejected: scoring is a configured scheme (overridable places/points; exhibition non-scoring status), and meet formats without team points are an accepted form; scoring is common-not-definitional.
- "Online registration is definitional." Rejected: entry import from external systems and admin-side entry adding are documented; registration bundling is a packaging choice.
- "FAT/timing integration is definitional." Rejected: hand timing with conversion standards is a supported first-class mode; timing sits on the boundary (consumed, not performed).
- "The Type is a registration platform." Rejected: entry collection is one step of the meet loop; without program/results the product is the sibling registration Type.
- "Meet = modern cloud product." Rejected: the incumbent is desktop-file-based; interchange with it is a structural expectation; paper-era meets satisfy the definition conceptually (see Final Synthesis).

## Boundary Findings

1. **vs Race Timing System (processed)** — record vs instrument. Ratified from this side: the meet record holds entries/schedule/results and compiles outcomes; the timing system measures and produces times; times flow from timing into the meet record (in-sample: FAT ingest via companion app; timing integrations). Cross-seal bundling observed in-sample (the same vendor families ship both). Consistent with the timing pass's own ratification.
2. **vs Race Management Platform (researched, sibling pass)** — competition container shape. Race = a single mass-participation timed event (course identity, one finish, finisher roster); meet = a program of distinct events with per-event entries. Cross-country meets sit near this seam: an XC meet's events are races, but the meet container organizes multiple divisions/races with meet-level records and team scoring. The race pass's research grouped "League / Tournament / Sports Meet" as different competition containers — consistent. Keep both.
3. **vs Tournament Management Platform (unprocessed)** — different competition containers. Meet = multi-event program of individual/relay entries run to per-event results (athletics model); tournament (working understanding) = bracketed head-to-head match progression. Lane/flight machinery has no bracket analogue; bracket advancement has no meet analogue. FORWARD FLAG for joint review when that leaf is processed. (Championship-series features — qualifying standards + advancement across meets — sit between the two; in-sample they are a packaged feature, not the meet's center.)
4. **vs League Management Platform (processed)** — bounded meet vs recurring season. The league pass's season programme (fixtures among standing members) is structurally distinct from the meet's event program (individual entries into disciplines). Products bundle both (league suites offer meet/tournament modules) — module depth, not identity. Keep both.
5. **vs Sports Registration Platform (unprocessed)** — entries vs intake. Entry collection is inside the meet loop and meaningless without the event program; a registration platform organizes intake for organizations/programs without a competition record. FORWARD FLAG: expect bundling; seam = the event program + results record.
6. **vs School / College Athletics Management (unprocessed)** — the athletics department's ongoing administration (schedules, rosters, compliance) vs the meet as a single competition's record of account. A meet is one unit inside the department's calendar; meet software is operated for the meet, often by delegated meet-day roles.
7. **vs Event Management / Event Registration (§26)** — attendees vs competitors. §26 events have agendas and ticket/admission semantics; a meet has an event program, entries with seed marks, and results. A meet page shares surface vocabulary (schedule, registration) — the distinction is competition semantics.
8. **vs Sports Scheduling Platform (unprocessed)** — the meet orders its own program into sessions; that sibling (working understanding) arranges fixtures/games across organizations and calendars. Meet-day session/heat ordering is internal competition logistics, not inter-organization scheduling.
9. **vs Team Management Application (unprocessed)** — team-side vs meet-side. Team products hold lineups and submit entries to meets; the meet system is the host-side record that receives and processes them. SwimTopia bundles both sides (team + meet platform) — bundling documented, centers differ.

## Uncertainties

- SwimTopia Meet Maestro's internal screens/states/defaults: help center unreachable (3 failures); everything beyond the feature list is unobserved. No workflow claims made for it.
- HY-TEK: nothing operational asserted; its role is evidenced only by cross-vendor compatibility statements.
- Whether a swim-specific non-performance vocabulary (e.g., DQ codes per stroke) is standard across swim meet products: not observed; only the track-side code set (DNS/DNF/DQ/NT/NH/ND/NM/SCR) is evidenced (product-specific).
- Regional "school sports day / annual sports meet" dedicated products: not sampled; the definition covers them conceptually but no market implementation evidence was gathered.
- Entry-limit rules (max events per athlete), entry deadline enforcement behavior, heat-sheet publication timing: not researched in depth; not asserted.
- Session/timetable management (ordering of events across meet days): evidenced weakly (multi-day meets exist; event ordering is configurable); session machinery per se not directly observed as a first-class object — held L1-uncertain, phrased cautiously in the final document.

## Final Synthesis

A sports meet is a bounded, multi-event athletics competition. Sports Meet Management is the meet organizer's competition system of record: it holds the meet's event program, binds entrants to events through entries (carrying seed marks and statuses), organizes those entries into the meet's running order (heats/lanes/flights — the mature implementation of that step), captures each event's results against its entries with explicit outcome semantics, and publishes the meet's results, team scores, and records from that record. Timing instruments feed it times; registration may feed it entries; leagues and championship series may chain meets together — but the meet record with its program–entries–results chain is the Type's center.

Historical check (§24, conceptual): the paper-era meet director — printed programme of events, entry cards per athlete, lane draws, hand-recorded results sheets, points table to the team trophy, results posted to the noticeboard — satisfies all four legs with none of the modern machinery (no seeding software, no FAT, no cloud publishing). The regional school sports day (house teams, event program, results, points) likewise fits. The definition therefore abstracts above the modern cloud/regional implementation: program, entries, results-of-record are the invariants; seeding depth, timing integration, live publishing, scoring schemes, and interchange formats are mature structure or variants.
