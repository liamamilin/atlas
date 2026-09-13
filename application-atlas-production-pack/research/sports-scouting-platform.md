# Research Notes — Sports Scouting Platform

## Research Goal

Understand what software sits under the directory leaf "Sports Scouting Platform" (§28 Sports, Fitness & Recreation, between "Tactical Analysis Platform" and "Athlete Recruiting Marketplace"): what its core objects are, who operates it, what the defining workflow is, and where the boundary sits against Athlete Recruiting Marketplace (joint-review flag from the athlete-recruiting-marketplace pass), Sports Performance Analytics (forward flag from that pass), Tactical Analysis Platform, Sports Video Analysis, Athlete Management System, and data-provider products.

## Initial Boundary (hypothesis before research)

- Hypothesis: evaluator-side talent identification and evaluation software — a registry of athletes (with video and/or performance data), search/discovery over that registry, and scout-authored evaluation records (reports, ratings, notes) tracked through lists/boards toward recruitment decisions. The athlete is the object of record, not a participant.
- Likely neighbors: Athlete Recruiting Marketplace (athlete-authored profiles + two-way contact — the recorded joint-check flag), Sports Performance Analytics (measured performance of athletes as the analyzed center — the recorded forward flag), Tactical Analysis Platform (opposition/tactical match content as center), Sports Video Analysis (video editing/annotation as center), Athlete Management System (own-roster daily management), player-statistics data providers (registry without evaluation).
- Key uncertainties going in: (1) is video definitional or common-mature? (2) is the registry vendor-populated, user-populated, or both? (3) does the Type include live/in-person scouting support? (4) how does the transfer-window/draft-cycle rhythm shape the tracking loop? (5) does any scouting product include athlete-side participation (which would blur the marketplace seam)?

## Research Questions

1. What objects exist? (athlete/player profile, evaluation report, rating/grade, video/match footage, tagged events/clips, statistics, lists/shortlists/boards, comparison, transfer/pipeline status)
2. Who uses it? (scouts, recruitment analysts, technical/sporting directors, GMs/personnel staff, agents, coaches)
3. How does the identification loop work (search → evaluate → shortlist → track → decide)?
4. Where does the registry content come from (vendor content library, user entry, imports, league feeds)?
5. What states and rules matter (evaluation frameworks/templates, rating scales, content licensing, transfer windows)?
6. What is the boundary vs the recruiting marketplace, performance analytics, tactical analysis, video analysis, AMS, and data providers?

## Representative Products

| Product | Segment | Philosophy | Why sampled |
|---|---|---|---|
| Hudl Wyscout (wyscout.com → hudl.com) | global football (soccer); clubs, federations, leagues, agencies, media | content-library-first: vendor-operated licensed video+data registry as the product, with scouting workflow (Scouting Area) on top | market leader in football scouting; richest official documentation (product page + Scouting Area page + FAQ) |
| Teamworks Player Personnel (teamworks.com/scouting) | US college football (and pro baseball/hockey siblings); GM/personnel departments | analytics-first: tracking-data-derived player traits + film, evaluation boards for roster construction | shows the draft/roster-construction pole and the analytics-derived evaluation philosophy; the same vendor sells a separate "Recruiting" product — first-hand evidence for the marketplace seam |
| ScoutDecision (scoutdecision.com) | football (soccer), global SMB/self-serve; scouts, analysts, agents, clubs | workflow-first: user-built player database + scout reports + transfer tracking, bring-your-own data (imports from Wyscout/StatsBomb) | the self-serve/small-organization pole; shows the registry can be user-populated rather than vendor-operated |
| Hudl Instat (hudl.com/en_gb/products/instat) | basketball and ice hockey; high school → pro | dual-use analysis+scouting: video library + statistics shared between coaching analysis and scouting | shows the dual-purpose pole and a second sport family; boundary data point vs Sports Video Analysis / Tactical Analysis |

Rejected/adjusted samples:

- Synergy Sports (synergysports.com) — intended as the US pro-league (NBA/MLB) video+data scouting pole; both fetch attempts returned transport errors (2026-09-09). Dropped per network rule; recorded as sample limitation.
- Digital Scout (digitalscout.com) — intended as the charting-based baseball/softball pole; the site states "Digital Scout is no longer available" (service discontinued). Dropped; recorded as market observation only.
- support.hudl.com Wyscout support topic — JS-rendered support community returned a CSS error with no content (2026-09-09). Dropped after one attempt; no vendor help-center-level step-by-step documentation was reachable for any sampled product.
- FastModel FastRecruit / FastScout (basketball) — observed only as Hudl product-nav entries ("comprehensive tools to evaluate talent and construct rosters"; "custom scouting reports, leveraging player stats and automated opponent breakdowns"); treated as boundary data points, not primary samples.

## Sources

All fetched 2026-09-09 (Layer A unless noted):

- Hudl Wyscout — product page: https://www.hudl.com/en_gb/products/wyscout (wyscout.com redirects here)
- Hudl Wyscout — Scouting Area: https://www.hudl.com/en_gb/products/wyscout/scouting-area
- Hudl Wyscout — FAQ: https://www.hudl.com/en_gb/products/wyscout/faq
- Teamworks — Player Personnel for College Football: https://teamworks.com/scouting (resolves to /player-personnel-college-football/)
- ScoutDecision — homepage + FAQ: https://scoutdecision.com
- Hudl Instat — product page: https://www.hudl.com/en_gb/products/instat

Limitations:

- No vendor help center / knowledge base was reachable this session (support.hudl.com is a JS-rendered community that returned a CSS error; Synergy Sports unreachable). All workflow detail comes from official product/marketing surfaces and one vendor FAQ, not step-by-step operational documentation. Precise field lists, rating-scale values, list-size limits, and pipeline stage vocabularies are therefore described conceptually.
- Synergy Sports unreachable → the US pro-league video+data pole is under-represented; cross-product claims rest on four products.
- Vendor-reported scale figures (1000+ competitions, 500,000+ matches, etc.) are vendor marketing figures; used only as existence evidence, never as facts in the final document.
- The athlete-recruiting-marketplace pass (2026-09-06) and sports-performance-analytics pass (2026-09-09) recorded boundary flags toward this leaf; both are discharged in §Boundary Findings.

## Product Observations

### Hudl Wyscout (incl. Scouting Area)

Key observations (Layer A):

- Positioning (product page): "The world's biggest library of football video and data. And it's all available on one platform." "We collect data and video from more than 1000 competitions worldwide." "With Wyscout, you can flag potential targets and evaluate them through video before sending scouts to see them."
- FAQ definition: "Hudl Wyscout is a scouting and recruiting platform that brings the world's biggest library of football video and performance data together in one place. It helps you identify, evaluate and compare players using full matches, tagged events, and stats across hundreds of competitions."
- Audience (FAQ): "built for football professionals involved in recruitment and scouting, including scouts, agents, analysts and technical directors. It's designed to support workflows from early discovery to deeper evaluation, shortlisting and decision-making."
- Value narrative (FAQ): "reduces the time and cost of discovery by helping you evaluate players through video and data before you ever travel. With search and reporting tools, you can quickly flag targets, validate with video evidence, and build shortlists that are easy to share internally."
- Tool set (FAQ): "search and query tools to quickly identify players, compare and contrast them, and build shortlists, plus reporting across competitions, matches, teams and players. For recruitment teams who want to centralise their work, Scouting Area helps combine scouting reports, curated clips and data into an easily searchable database of your department's evaluations."
- Product-page tool names: "Advanced search to find the right players"; "Players lists for easier comparison"; "Shadow teams help you create shortlists"; Reporting: "analysis on competitions, matches, teams and players, with highly-detailed stats and metrics."
- Scouting Area positioning: "The all-in-one solution for player recruitment. Centralize all your content, reports and tools into one workflow under one location." Organization: "Scouting Area makes it easy to combine subjective scouting reports, curated video clips and both performance and career data to create a searchable database of your recruitment team's work."
- Evaluation standardization (FAQ): "custom report templates (player, match or team) that correspond to your club's framework... adjust settings like rating type and then create new reports from your chosen templates, keeping everyone aligned on the same criteria and outputs." Scouting Area: "Align the club's current scouting philosophy and adapt to changing scouting frameworks thanks to our customizable report templates."
- Content sourcing and licensing (FAQ): "content is sourced through rights agreements with leagues, clubs and rights-holders... Content is contracted for 'professional purposes' and provided on a delayed basis behind a paywall for a B2B audience." Availability timing varies by competition and rights agreement; content can become temporarily unavailable if an agreement expires.
- Content operation (FAQ): minimum 1080p delivery guideline; trained analysts tag an average of 2,500 data points per match; metadata checks; at least 25% of matches fully reviewed for accuracy. Tag on Demand: a full Wyscout report delivered within 48 hours of a match ending (for clubs using it on their own captured footage).
- Coverage variants: 1000+ competitions; Youth Competitions Pack with 190+ major youth competitions ("Don't miss the next breakthrough star... scouting and player development programs").
- Integration: Instant Save — "send full matches, playlists, and individual clips from Wyscout to Hudl in a second, with structure preserved"; Sportscode-compatible XML; Competition Database opens Wyscout matches in Hudl Sportscode.
- Customer evidence: Urawa Reds technical director — "modernized their scouting department's recruiting workflow by introducing Wyscout"; former Wolves head of recruitment — "team of full-time video analysts who work exclusively with Wyscout, so that we're not wasting travel time, airfares, hotels. We can see a lot of good or bad attributes in the players from the Wyscout footage."
- Audiences in navigation: Pro Suite (top organisations), Clubs and Communities, Universities, Data Licensing (Football API), Player Agencies ("Scout smarter, not harder, with world-class recruitment insights").

### Teamworks Player Personnel (College Football)

Key observations (Layer A):

- Positioning: "Identify talent early, objectively, and with unmatched speed and precision. Purpose-built for college football General Managers and personnel leaders." "Player Personnel is a video-first, analytics-driven platform purpose-built for General Managers and personnel department leaders. It transforms player tracking data into predictive, position-specific insights — helping teams move fast, surface undervalued talent early, and make confident, data-backed decisions that strengthen the roster from top to bottom."
- Search + evaluate: "Quickly narrow your search and evaluate targets using the traits coaches naturally look for when assessing talent. Our position-specific metrics factor in critical context — like pass difficulty, route depth, and player separation... And because every insight is backed by curated video clips, you get an objective gut-check grounded in film."
- Analytics-derived evaluation: "Our platform uses player-tracking data to surface leading indicators of talent — like Speed, Change of Direction, and Pocket Awareness — before they show up on the stat sheet." Models analyze "tracking data for all 22 players on every snap"; metrics "account for pressure, coverage, blocking, route design, opponent strength"; "Insights are expressed in the language coaches and scouts already use — burst, play speed, run ability, pass rush strain, pocket awareness."
- Features: "Data → Film, Instantly" (access highlights to confirm metrics, identify players/routes with overlays, curate cutups, share and export); "Integrated Teamworks Intelligence Traits" (player traits scouts look for in evaluations; instantly view film to confirm data); "Transfer Portal, With Context" (find players with robust filters; evaluate future potential with Player Traits; portal updates every 5 minutes during transfer windows; quality-control checks); "Player Comps" (find similar players based on any selected player's profile; compare on traits/performance/biographical data); "Custom Lists & Magnet Boards" (upload your own target lists; build unlimited custom lists; create magnet boards with custom grades; edit data such as measurables; manage and export player lists); Phone and Tablet App (staff access from any device; share clips/cutups/reports; offline clip download).
- Product family: Player Personnel – Football / Baseball / Hockey (same "Scouting" product icon); a separate "Recruiting" product; Coaching products; GM; Hub; Compliance; Academics; etc. The demo form lists "Player ID", "Scouting", "Recruiting", "Recruiting Communication" as separate product interests.
- Bundling: "When bundled with Player Personnel, you create a unified football intelligence platform" (with Coaching); Teamworks "Operating System for Sports™" — unified mobile experience, user-management sync.

### ScoutDecision

Key observations (Layer A):

- Positioning: "Software for Football Clubs, Agents, Scouts, and Coaches." Four audience-specific products (Scouts & Analysts; Coaches; Agents; Clubs).
- Scout/Analyst product: "Organize your player database. Create scout reports. Generate automatic comparisons."
  - Player Database Management: "Create, update and filter your player profiles without copy paste rituals." "Combine all relevant player elements effortlessly and say goodbye to scattered data."
  - Effortless Evaluation & Reporting: "Create and automatically compare your scout reports." "Develop your framework(s) for player classification and evaluation and assess them according to your judgment. Import from Wyscout, Statsbomb and others. Create automatic comparisons and simplify analysis."
  - Uncomplicated Transfer Tracking: "Manage potential recruits status, save time and stress during your transfer windows." "Identify unfulfilled capabilities in your team and potential recruitment opportunities. Break down the positions you want to follow and monitor athletes during the transfer window."
- Agent product: centralize player information ("Biographical data, profile links, videos, contracts and scout reports — organize them all instead of having them scattered around emails, Whatsapp, Drive and Excel"); CRM for club requests and contacts ("Suggest players and track their steps in the signing process during transfer windows"); generate PDF and links instantly ("share Scout Reports, Shadow Teams and Graphics automatically with a PDF or a Link").
- Club product: "Organize all your files, videos and scout reports. Negotiate players contracts and network with other clubs and agents."
- FAQ: multi-user collaboration "based on their permissions levels, they can work together to build reports, shortlists, comparisons"; role-based access ("add multiple users and assign permission levels"); data export on cancellation; API access on request; 7-day free trial; suitable for women's football and futsal.
- Customer evidence (testimonials): Al Ahly head scout — "facilitates our scouting reports, technical player assessments, and helps us build a player database and generate reports"; Norwich FC scout — "creating, monitoring and assessing my database of players. The platform provides me with a way to make my scouting template with the KPIs and characteristics that would be more relevant for me in each position"; Southport FC head of football operations — "we thought we would be using it to coordinate our scouting and recruitment department; however, it is far more robust... whilst still proving a high-quality system for scout reports and recruitment documentation."
- Anti-spreadsheet framing: "Stop wasting your time in Excel sheets, PDF documents and computer folders."

### Hudl Instat

Key observations (Layer A):

- Positioning: "Comprehensive Analysis and Scouting Solution" — "the platform trusted by coaches and scouts worldwide, thanks to the largest video library in the game—with over 500,000 matches, 70,000 teams and 60,000 players across basketball and hockey."
- Three pillars: Comprehensive Video Library ("Access games from top leagues"); Best-in-Class Statistics ("All the data you need to make informed decisions and track progress over time"); Simple Collaboration ("Work together, share information and make strategic decisions").
- Film exchanges: "Thanks to the combination of our content library and advanced data, Hudl Instat is the perfect solution for league exchange platforms."
- Database use: "Identify Strengths and Weaknesses — Hudl Instat's advanced video analysis allows you to dive deep into past performances... Break down game footage efficiently. Track player movements and key moments. Identify where each player needs to improve."
- Statistics: "comprehensive dashboard... Compare and contrast data over time. Identify trends and patterns in performance."
- Collaboration: "Share video footage and statistics. Make decisions together, as a team."
- Sportscode integration: "Effortless Clip Playlist Transfer. Synchronized Event Timelines with Video."
- Audiences: high schools/athletic departments, club/youth, collegiate, professional organizations.
- Boundary note: Instat is explicitly dual-purpose (team analysis AND scouting); the same library serves coaching analysis and player evaluation. Included deliberately as the dual-use pole.

## Cross-product Comparison

| Aspect | Hudl Wyscout | Teamworks Player Personnel | ScoutDecision | Hudl Instat |
|---|---|---|---|---|
| Athlete registry | vendor-operated: video+data from 1000+ competitions, licensed under rights agreements | league/tracking-data-derived population + transfer portal + user-uploaded target lists | user-built: scouts/clubs create and maintain player profiles; imports from Wyscout/StatsBomb | vendor-operated video library: 500K+ matches, 70K teams, 60K players (basketball/hockey) |
| Athlete profile content | performance + career data, stats, video, tagged events | tracking-derived traits, performance and biographical data, measurables (editable), film | biographical data, profile links, videos, contracts, scout reports | video, statistics, tagged events |
| Search/discovery | advanced search; filter and find targets; query tools | "quickly narrow your search"; robust filters (transfer portal) | "create, update and filter your player profiles" | library access; database breakdown |
| Evaluation records | scouting reports against customizable templates (player/match/team); rating type configurable; Scouting Area centralizes "your department's evaluations" | magnet boards with custom grades; Player Traits as evaluation vocabulary; film-confirmed insights | scout reports against user-defined frameworks ("KPIs and characteristics... for each position"); automatic report comparison | (analysis-oriented; evaluation via database breakdown) |
| Lists/shortlists | players lists; shadow teams as shortlists | custom lists; magnet boards; uploaded target lists | shortlists; shadow teams (agent share) | (not evidenced) |
| Comparison | "compare and contrast them" | Player Comps (similar-player finding) | "generate automatic comparisons" | "compare and contrast data over time" |
| Video evidence | full matches, tagged events, curated clips; evaluate "before sending scouts" | curated clips behind every insight; cutups; overlays | videos on profiles; scout reports | full video library; clip playlists |
| Statistics/data | performance data, reports across competitions/matches/teams/players | tracking-data metrics, position-specific, context-adjusted | imported external data | statistics dashboards, trends |
| Tracking toward decision | shortlists "easy to share internally"; recruitment workflow | transfer portal tracking (5-minute updates in windows); lists/boards toward roster construction | transfer tracking ("manage potential recruits status... during your transfer windows") | (not evidenced) |
| Collaboration | share internally; Scouting Area as department database | share clips/cutups/reports; unified mobile app | multi-user with permission levels; PDF/link sharing | share video and statistics; team decisions |
| Mobile | (platform web; support/training exist) | phone and tablet app; offline clips | (web; API on request) | (web/iPad surfaces shown) |
| Audience breadth | scouts, agents, analysts, technical directors; clubs/federations/agencies/media | GMs and personnel leaders (college football; baseball/hockey siblings) | scouts, analysts, agents, clubs (SMB/self-serve) | coaches AND scouts; HS→pro |
| Registry substrate | vendor content operation (licensed, delayed, B2B paywall) | league data + portal + user uploads | user entry + imports | vendor content operation |
| Secondary uses | youth scouting pack; media/data licensing | coaching bundle (scout cards, cutups, weekly prep) | agent CRM; club contract/networking | league film exchanges; team analysis |

## Canonical Model (Layer C synthesis)

L0 — Defining Invariant (smallest structure without which the Type is unrecognizable):

1. **The athlete registry** — persistent identified records for athletes (the scouted population), each carrying sport context: identity, position/role, current club/team and competition, career/biographical data, commonly performance history. The athlete is the object of record — never a participating account. The registry may be vendor-operated (licensed content library), user-built (the scouting department's own database), or a hybrid (imports + own entry). Remove → a report-writing tool with no memory, or a generic contacts/CRM database.
2. **The evaluation record** — scout/analyst-authored assessments attached to athletes: reports, ratings/grades, notes, recorded against an evaluation framework (the organization's templates, criteria, rating scales) so that a department's judgments accumulate as a comparable, searchable body of work. Remove → a statistics database or video archive with no evaluation memory (data-provider / media-archive territory).
3. **The identification-and-tracking loop** — search/filter/compare across the registry to surface candidates, collect them into lists/shortlists/boards, and track them over time toward recruitment decisions. Remove → a static archive of reports nobody works from, or a bare search page over nothing.

The defining purpose binding the three: the athlete is held and evaluated as a potential acquisition target (signing, drafting, recruiting into a roster), and the platform's loop serves that acquisition decision. Without the acquisition orientation the same objects describe a player-statistics database or a performance-analysis tool.

Jointly-held load-bearing: (1 alone = player statistics database / data provider; 2 without 1 = scattered report documents; 3 without 1+2 = search over nothing; 1+2 without 3 = report archive, not a working tool; 1+3 without 2 = lists over stats with no evaluation memory; 2+3 without 1 = evaluations of unanchored names with no persistent career context).

Historical check (§24): the paper-era scouting operation — the scout's card file / department report archive (registry), typed scouting reports with ratings (evaluation records), and browsing/cross-referencing the file to surface and track prospects (identification loop) — satisfies all three invariants with no video, no data feeds, no software. Regional shapes (Latin American ojeadores, baseball scouting bureaus selling typed reports to many clubs) also fit; the bureau is the vendor-operated-registry pole in analog form. Therefore video libraries, statistics feeds, tracking-derived metrics, comparison engines, and mobile apps are common mature structure, not definition. The Type predates its current content-library realization.

L1 — Common Mature Structure (cross-product commonality, Layer B):

- Video evidence layer: match footage, tagged events/clips linked to athletes, curated clips attached to evaluations; "evaluate through video before you ever travel" is the shared value narrative (Wyscout, Teamworks, Instat; ScoutDecision carries video on profiles)
- Performance/statistics layer on athlete profiles: match stats, aggregates, advanced metrics (all four)
- Comparison machinery: side-by-side comparison, similar-player finding ("comps"), automatic report comparison (all four)
- Lists/shortlists/boards: named lists, shadow teams, magnet boards with custom grades, uploaded target lists (all four in some form)
- Evaluation standardization: report templates aligned to the club's framework; configurable rating types/scales; shared criteria across the department (Wyscout, ScoutDecision, Teamworks)
- Internal sharing/collaboration: share reports/lists/clips; multi-user with roles/permissions (ScoutDecision explicit; Wyscout Scouting Area as department database; Teamworks staff sharing)
- Import/export and integration: imports from external data providers (ScoutDecision), exports (PDF/CSV/XML), handoff to video-analysis workspaces (Wyscout→Hudl Instant Save; Instat→Sportscode)
- Mobile/tablet companion for staff (Teamworks explicit; others web-first)
- Transfer/recruitment-pipeline tracking of target status (ScoutDecision transfer tracking; Teamworks transfer portal)

L2 — Variant / Optional Structure:

- Registry substrate: vendor-operated licensed content library (Wyscout, Instat) vs user-built database (ScoutDecision) vs league-data/portal-derived (Teamworks) — the main philosophical axis; determines coverage vs control
- Analytics depth: tracking-data-derived predictive traits (Teamworks) vs tagged-event statistics (Wyscout/Instat) vs imported basic data (ScoutDecision)
- Sport/region scope: single-sport global deep (football) vs multi-sport families (basketball/hockey) vs US football/baseball/hockey pro-college axis
- Live/in-person scouting support: event schedules, roster packets, in-venue apps (under-evidenced this pass; the recruiting-marketplace pass documented Coach Packet/EventBeacon on the marketplace side)
- Youth/talent-development orientation (Wyscout Youth Pack)
- Secondary audiences: player agencies (Wyscout, ScoutDecision), media/data licensing (Wyscout API)
- Dual-use analysis+scouting packaging (Instat) vs scouting-dedicated packaging (Wyscout Scouting Area, Teamworks Player Personnel)
- Adjacent bundling: coaching tools, agent CRM, club networking/contract negotiation (ScoutDecision club/agent products) — out-of-Type modules attached to the same vendor

L3 — Vendor-specific (research notes only):

- Wyscout: 1000+ competitions figure; Youth Pack 190+ competitions; Tag on Demand 48-hour report; 1080p delivery guideline; 2,500 data points/match average; 25% full-review QA; "Shadow teams"; Scouting Area template types (player/match/team); rating-type settings; Instant Save; Sportscode XML; Competition Database; Monchi/Urawa/Wolves testimonials; Player Agencies solution page
- Teamworks: Player Traits names (Speed, Change of Direction, Pocket Awareness, burst, play speed, run ability, pass rush strain); frame-level tracking of all 22 players every snap; 1–2M+ data points/game claim; transfer portal 5-minute updates; magnet boards; Player Comps; PFF heritage signals; "Operating System for Sports™"; Player Personnel – Football/Baseball/Hockey product split; separate Recruiting product; demo-form product interests (Player ID / Scouting / Recruiting / Recruiting Communication)
- ScoutDecision: imports from Wyscout/StatsBomb; Shadow Teams sharing; PDF/link generation; agent CRM (club requests, signing-process steps); club contract negotiation/networking; coach-side drills/practices/questionnaires (out-of-Type); 7-day trial; permission levels; API on request; ELOQUENTPROPHECY LDA (Portugal)
- Instat: 500,000 matches / 70,000 teams / 60,000 players figures; league exchange platforms; basketball/hockey scope; Sportscode integration; iPad statistics surface
- Cross-vendor ownership note: Wyscout and Instat are both Hudl products (Hudl also sells FastModel FastRecruit/FastScout and StatsBomb) — one vendor operates multiple scouting-adjacent product lines; market-consolidation observation only

## Vendor-specific Findings

- **The registry substrate is the main philosophical axis**: vendor-operated licensed libraries (coverage at scale, delayed rights, B2B paywall) vs user-built databases (control, no licensing, manual upkeep) vs league-data-derived populations. All three realize the same L0.
- **Evaluation standardization is a first-class concern**: Wyscout sells customizable report templates "corresponding to your club's framework" with configurable rating types; ScoutDecision sells user-defined evaluation frameworks/KPIs per position; Teamworks expresses evaluation in "the language coaches and scouts already use." The template/rating layer is how a department keeps judgments comparable — common mature structure, realized differently.
- **Video-before-travel is the shared economic argument**: Wyscout ("before sending scouts to see them"; Wolves quote on travel costs), Teamworks ("objective gut-check grounded in film"), ScoutDecision (centralization vs scattered files). The platform's value case is remote pre-evaluation; live scouting remains the confirming step.
- **The transfer window / draft cycle is the operational rhythm**: ScoutDecision frames transfer tracking around windows; Teamworks updates the transfer portal every 5 minutes during windows. The tracking loop intensifies around acquisition windows.
- **Scouting products coexist with recruiting products inside one vendor**: Teamworks sells Player Personnel (evaluation) and Recruiting (outreach/communication) as separate products; the demo form lists them separately. This is first-hand vendor evidence for the structural seam against Athlete Recruiting Marketplace.
- **Dual-use products blur toward analysis Types**: Instat markets itself to "coaches and scouts" with the same library serving team analysis and player evaluation; Wyscout content flows into Hudl video-analysis workspaces. The scouting Type is defined by the evaluation/acquisition center of gravity, not by exclusive use of the content.

## Boundary Findings

1. **vs Athlete Recruiting Marketplace (JOINT REVIEW DISCHARGED from this side — keep-both RATIFIED)**: the marketplace's L0 requires athlete-side self/club-authored profiles and a two-way interest/contact channel; this Type's L0 holds the athlete as the object of record with no participation channel. Evidence from this side: none of the four sampled products offers athlete-side authorship or athlete-initiated contact — Wyscout's athletes are licensed-content subjects; Teamworks evaluates portal/tracking-data athletes without athlete participation; ScoutDecision's profiles are created by scouts/agents/clubs; Instat's library athletes are content subjects. The seam is confirmed structurally, and the vendor vocabulary collision is documented first-hand: Teamworks sells both "Recruiting" and "Player Personnel/Scouting" products; Wyscout's own FAQ calls a scouting platform a "scouting and recruiting platform" (there "recruiting" means club-side player recruitment, not athlete participation). Directional tests hold both ways: remove athlete authorship/participation from a marketplace → scouting platform; add a two-way athlete contact channel → marketplace. The marketplace pass's recommendation is discharged; keep-both stands.
2. **vs Sports Performance Analytics (forward flag DISCHARGED from this side — keep-both RATIFIED)**: analytics centers measured performance of an analyzed athlete/team population for performance decisions; scouting centers external athletes as acquisition targets with evaluator-authored records. Player-evaluation/recruitment modules inside analytics products (the StatsBomb recruitment positioning observed on Hudl's nav; Teamworks' tracking-data traits) drift to this Type when external-player recruitment evaluation becomes the center. The two Types share data substrates; the seam is the analyzed center and the decision served (performance vs acquisition).
3. **vs Tactical Analysis Platform**: opposition/tactical match content as the center → that Type. Scouting platforms carry match video, but as evidence about athletes; when match content is broken down for tactical/opposition purposes the product is doing tactical-analysis work (Instat's dual-use packaging shows both under one roof — center-of-gravity seam).
4. **vs Sports Video Analysis**: video-analysis products center the editing/annotation of footage (usually own-team) for coaching; scouting platforms center the athlete registry + evaluation with video as evidence. The Wyscout→Hudl Instant Save handoff (scouting content pushed into a video-analysis workspace "with structure preserved") shows the market itself treats these as adjacent stages.
5. **vs Athlete Management System**: AMS manages the organization's own roster (readiness, programs, daily operations); scouting manages external talent identification. Different population (owned vs external), different loop (daily readiness vs acquisition).
6. **vs player-statistics data providers / Vertical Search**: a data feed or stats database without evaluation records and a tracking loop is a data product. Wyscout itself splits "Wyscout Data" (API for "performance, scouting and recruitment analysis") from the Wyscout platform — the API serves scouting but is not the platform.
7. **vs generic CRM**: ScoutDecision's agent product has CRM features (club requests, contacts) — but the scouting core (player database + reports + tracking) is what makes it a scouting platform; a pure contact manager without an athlete registry and evaluation records is not this Type.

## Uncertainties

- No vendor help-center operational detail was reachable (support.hudl.com JS community failed; Synergy Sports unreachable). Workflow detail is from product pages + one vendor FAQ; precise field vocabularies, rating-scale values, list limits, and pipeline stage names are described conceptually.
- Live/in-person scouting support (scouting assignments, trip reports, event-day apps) is under-evidenced in this sample; Teamworks' phone/tablet app is the closest direct evidence. The recruiting-marketplace pass documented event-day tools (Coach Packet, EventBeacon) on the marketplace side; whether dedicated scouting-side event tools are common could not be confirmed this pass.
- Draft-board/pipeline depth: status tracking of targets is evidenced (transfer tracking, magnet boards, lists), but full stage-machine vocabularies (e.g., board statuses) are vendor-specific and were not observable.
- The bureau/agency pole (an organization producing evaluations sold to many clubs, analog to historical scouting bureaus) was not directly sampled; Wyscout's agency audience and data-licensing line are the nearest observed signals.
- Whether athlete-submission hybrids (athletes uploading video for scout review) exist as a distinct variant could not be verified from official sources this pass; not asserted in the final document.

## Final Synthesis

A Sports Scouting Platform is evaluator-side talent-identification software whose defining core is three jointly-held structures: a persistent athlete registry (the scouted population as identified records with sport context — vendor-operated licensed libraries, user-built databases, or hybrids), evaluation records (scout/analyst-authored reports, ratings, and notes recorded against the organization's evaluation framework, accumulating as the department's comparable judgment memory), and the identification-and-tracking loop (search/filter/compare to surface candidates, collect them into lists/shortlists/boards, and track them toward acquisition decisions). The athlete is the object of record, never a participating account — this is the structural seam against the Athlete Recruiting Marketplace, confirmed from this side and ratified keep-both. Around the core, mature products add video evidence (the "evaluate before you travel" value case), statistics layers, comparison machinery, evaluation standardization (templates, rating scales), internal sharing with roles, import/export and handoff to video-analysis workspaces, mobile companions, and transfer-window/draft-cycle tracking. The market realizes the Type across a substrate axis — vendor content library (Wyscout, Instat), tracking-data analytics (Teamworks Player Personnel), user-built workflow (ScoutDecision) — with dual-use analysis+scouting packaging (Instat) and scouting-dedicated packaging (Wyscout Scouting Area, Teamworks Player Personnel) as packaging variants. The paper-era card file + typed report archive satisfies the core with no software machinery (historical check passed); video, data feeds, and derived metrics are common mature structure, not definition.
